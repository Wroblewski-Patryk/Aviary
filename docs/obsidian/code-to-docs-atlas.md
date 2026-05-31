# Aviary Code To Docs Atlas

Updated: 2026-05-31

## Canonical Inputs

| Input | Status | Role |
| --- | --- | --- |
| [[architecture/registry/nodes.csv|nodes.csv]] | present | Feature/page/API/service/data/test/doc registry. |
| [[architecture/chains/chains.csv|chains.csv]] | present | End-to-end function chains. |
| [[architecture/indices/user-action-index.csv|user-action-index.csv]] | missing | User-visible action proof map. |
| [[architecture/indices/function-chain-evidence-index.csv|function-chain-evidence-index.csv]] | missing | Generated function evidence index. |

## Feature Atlas

| Feature | Nodes | Chains | Actions |
| --- | --- | --- | --- |
| foreground_runtime | 11 | 0 | not generated |
| architecture_graph | 8 | 0 | not generated |
| app_chat | 7 | 0 | not generated |
| memory_flow | 5 | 0 | not generated |
| profile_settings | 5 | 0 | not generated |
| tools | 5 | 0 | not generated |
| web_shell | 4 | 0 | not generated |
| data_model | 3 | 0 | not generated |
| api_contracts | 2 | 0 | not generated |
| delivery | 2 | 0 | not generated |
| event_ingress | 2 | 0 | not generated |
| learned_state | 2 | 0 | not generated |
| auth | 1 | 0 | not generated |
| dashboard | 1 | 0 | not generated |
| personality | 1 | 0 | not generated |
| research_evidence | 1 | 0 | not generated |
| telegram | 1 | 0 | not generated |

## Navigation Rule

Before changing behavior, identify the owning feature, route/page, API route, backend function, data model, tests, docs, and proof path. If a project does not yet have a user-action index, do not pretend it has action-level proof; add that as cleanup work.
