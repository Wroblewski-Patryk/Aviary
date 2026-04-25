$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot\..
try {
    ..\.venv\Scripts\python .\scripts\run_user_data_cleanup.py @args
}
finally {
    Pop-Location
}
