# goweft

Security tooling for the AI agent supply chain.

## The problem

AI agents ship code, consume tools, fork codebases, and persist memory across sessions — but the security tooling hasn't caught up. Packages ship with debug artifacts and secrets. Forks strip safety guardrails. Runtime tool servers have no trust enforcement. Agent memory accumulates poisoned instructions that execute days later. goweft builds the tools that close these gaps.

## The suite

| | Tool | What it does | When it runs |
|---|---|---|---|
| **Pre-publish** | [**tenter**](https://github.com/goweft/tenter) | Scans packages for source maps, secrets, debug artifacts, and sensitive files before they ship | Before `npm publish` / `pip upload` / `cargo publish` |
| **Post-fork** | [**unshear**](https://github.com/goweft/unshear) | Detects stripped safety mechanisms, removed auth, disabled guardrails in forked codebases | After a fork appears or a leak triggers mass cloning |
| **Runtime** | [**heddle**](https://github.com/goweft/heddle) | Policy-and-trust layer for MCP tool servers — trust tiers, credential brokering, audit logging | Every tool invocation at runtime |
| **Across sessions** | [**ratine**](https://github.com/goweft/ratine) | Agent memory poisoning detector — injected instructions, hidden payloads, credential leakage, belief drift | Periodic scans of agent persistent state |

Each tool is zero external dependencies (Python stdlib only), MIT licensed, and independently installable.

## Background

Built by Steve — IT and cybersecurity professional with 6 years in enterprise infrastructure, a BS in Cybersecurity, and seven CompTIA certifications including Security+ and Secure Infrastructure Specialist.

## Links

- [Tenter on GitHub Marketplace](https://github.com/marketplace/actions/tenter-scan) — GitHub Action for CI integration
