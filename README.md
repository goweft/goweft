# goweft

Security tooling for the AI agent supply chain.

## The problem

AI agents ship code, consume tools, fork codebases, persist memory across sessions, and generate commits without attribution — but the security tooling hasn't caught up. goweft builds the tools that close these gaps.

## The suite

| | Tool | What it does | When it runs |
|---|---|---|---|
| **Pre-publish** | [**tenter**](https://github.com/goweft/tenter) | Scans packages for source maps, secrets, debug artifacts before they ship | Before `npm publish` / `pip upload` / `cargo publish` |
| **Post-fork** | [**unshear**](https://github.com/goweft/unshear) | Detects stripped safety mechanisms, removed auth, disabled guardrails in forks | After a fork appears or a leak triggers mass cloning |
| **Runtime** | [**heddle**](https://github.com/goweft/heddle) | Policy-and-trust layer for MCP tool servers — trust tiers, credential brokering, audit | Every tool invocation at runtime |
| **Across sessions** | [**ratine**](https://github.com/goweft/ratine) | Agent memory poisoning detector — injected instructions, hidden payloads, belief drift | Periodic scans of agent persistent state |
| **In git history** | [**crocking**](https://github.com/goweft/crocking) | AI authorship detector — commit patterns, timing signals, tool markers, code style | Before merge, during audit, or on any repo |

Each tool is zero external dependencies (Python stdlib only), MIT licensed, and independently installable.

## Background

Built by Steve — IT and cybersecurity professional with 6 years in enterprise infrastructure, a BS in Cybersecurity, and seven CompTIA certifications including Security+ and Secure Infrastructure Specialist.

## Links

- [Tenter on GitHub Marketplace](https://github.com/marketplace/actions/tenter-scan) — GitHub Action for CI integration
