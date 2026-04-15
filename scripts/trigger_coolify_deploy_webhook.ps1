param(
    [Parameter(Mandatory = $true)][string]$WebhookUrl,
    [Parameter(Mandatory = $true)][string]$WebhookSecret,
    [string]$Repository = "",
    [string]$Branch = "main",
    [string]$BeforeSha = "",
    [string]$AfterSha = "",
    [string]$PusherName = "codex"
)

function Get-GitValue {
    param([string[]]$Arguments)

    $value = & git @Arguments 2>$null
    if ($LASTEXITCODE -ne 0) {
        return ""
    }

    return ($value | Out-String).Trim()
}

function Get-RepositoryName {
    $remote = Get-GitValue @("config", "--get", "remote.origin.url")
    if (-not $remote) {
        return ""
    }

    if ($remote -match "github\.com[:/](.+?)(?:\.git)?$") {
        return $matches[1]
    }

    return ""
}

if (-not $Repository) {
    $Repository = Get-RepositoryName
}

if (-not $Repository) {
    throw "Could not infer repository name from git remote. Pass -Repository owner/name explicitly."
}

if (-not $AfterSha) {
    $AfterSha = Get-GitValue @("rev-parse", "HEAD")
}

if (-not $AfterSha) {
    throw "Could not determine HEAD commit. Pass -AfterSha explicitly."
}

if (-not $BeforeSha) {
    $BeforeSha = Get-GitValue @("rev-parse", "$AfterSha^")
}

if (-not $BeforeSha) {
    $BeforeSha = $AfterSha
}

$commitMessage = Get-GitValue @("log", "-1", "--pretty=%s", $AfterSha)
if (-not $commitMessage) {
    $commitMessage = "manual deploy trigger"
}

$commitUrl = "https://github.com/$Repository/commit/$AfterSha"
$compareUrl = "https://github.com/$Repository/compare/$BeforeSha...$AfterSha"

$payload = @{
    ref        = "refs/heads/$Branch"
    before     = $BeforeSha
    after      = $AfterSha
    compare    = $compareUrl
    created    = $false
    deleted    = $false
    forced     = $false
    base_ref   = $null
    commits    = @(
        @{
            id        = $AfterSha
            message   = $commitMessage
            timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
            url       = $commitUrl
            author    = @{ name = $PusherName; email = "" }
            committer = @{ name = $PusherName; email = "" }
            added     = @()
            removed   = @()
            modified  = @()
        }
    )
    head_commit = @{
        id        = $AfterSha
        message   = $commitMessage
        timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
        url       = $commitUrl
        author    = @{ name = $PusherName; email = "" }
        committer = @{ name = $PusherName; email = "" }
        added     = @()
        removed   = @()
        modified  = @()
    }
    repository = @{
        name           = ($Repository -split "/")[-1]
        full_name      = $Repository
        private        = $false
        default_branch = $Branch
        html_url       = "https://github.com/$Repository"
        clone_url      = "https://github.com/$Repository.git"
        ssh_url        = "git@github.com:$Repository.git"
        owner          = @{
            name  = ($Repository -split "/")[0]
            login = ($Repository -split "/")[0]
        }
    }
    pusher = @{ name = $PusherName }
    sender = @{ login = $PusherName }
}

$json = $payload | ConvertTo-Json -Depth 8 -Compress
$secretBytes = [System.Text.Encoding]::UTF8.GetBytes($WebhookSecret)
$payloadBytes = [System.Text.Encoding]::UTF8.GetBytes($json)
$hmac = [System.Security.Cryptography.HMACSHA256]::new($secretBytes)
$signature = "sha256=" + ([System.BitConverter]::ToString($hmac.ComputeHash($payloadBytes)).Replace("-", "").ToLowerInvariant())

$headers = @{
    "Content-Type"       = "application/json"
    "X-GitHub-Event"     = "push"
    "X-Hub-Signature-256" = $signature
    "User-Agent"         = "aion-coolify-webhook-trigger"
}

Invoke-RestMethod `
    -Uri $WebhookUrl `
    -Method Post `
    -Headers $headers `
    -Body $json
