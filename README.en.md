# AI Launch Red Team (ai-launch-red-team)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Skill](https://img.shields.io/badge/type-agent%20skill-blue)
![Platforms](https://img.shields.io/badge/Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20Codex-supported-lightgrey)

[中文说明](README.md)

A zero-code agent skill. Paste an "our AI is ready to launch" proposal and it red-teams the plan against **eight veto conditions and seven review dimensions**, returning a **launch veto card** you can take straight into a review meeting: which vetoes fired, which sentence of the proposal triggered each one, and what to ask next.

It answers one question:

> The demo works. What has nobody thought through before this touches a real workflow?

## Install in 30 seconds

```bash
# Claude Code
git clone https://github.com/Anonymousyz/ai-launch-red-team.git ~/.claude/skills/ai-launch-red-team

# Cursor
git clone https://github.com/Anonymousyz/ai-launch-red-team.git ~/.cursor/skills/ai-launch-red-team

# Codex
git clone https://github.com/Anonymousyz/ai-launch-red-team.git ~/.codex/skills/ai-launch-red-team
```

On Windows, replace `~` with `%USERPROFILE%`.

## Usage

Describe what you want after installing:

```text
Red-team this launch plan:
We built a customer-refund agent on an LLM. Accuracy tested at 95%.
It executes refunds automatically. We launch to all users next week;
monitoring comes later.
```

You get back a veto card with four parts: an eight-row veto scan (each verdict quoting your own words), a seven-dimension check (answered / vague / missing), a risk-ordered question list for the review meeting, and a red-team recommendation. The plan above trips two vetoes: automatic refund execution with no human review, and no error/rollback owner. Full output: [examples/01-refund-agent.md](examples/01-refund-agent.md).

## How it reviews

The eight vetoes and seven dimensions come from the frozen review contract of the [AI Prototype-to-Production Toolkit](https://github.com/Anonymousyz/ai-prototype-to-production-toolkit): unauthorized data use, sensitive data to an unapproved model, high-risk decisions without human review, no logs or traceability, no error or rollback owner, unevaluable output quality, uncontrolled cost, and a demo marketed as production-ready.

## What it does not do

- **It does not verify facts.** "We have logs" is treated as a claim, and the question list asks for evidence.
- **It does not score or approve.** For a filed, reviewable assessment with reports, use the full toolchain:

| Need | Go to |
|---|---|
| Formal 70-point assessment with vetoes and HTML reports | [ai-prototype-to-production-toolkit](https://github.com/Anonymousyz/ai-prototype-to-production-toolkit) (`ai-ready` CLI) |
| Turn assessment results into a decision packet | [research-to-decision-toolkit](https://github.com/Anonymousyz/research-to-decision-toolkit) (`r2d` CLI) |
| Find evaluation/guardrail/observability tools by gap | [awesome-ai-production-readiness](https://github.com/Anonymousyz/awesome-ai-production-readiness) (57 verified entries) |

## License

MIT. See [LICENSE](LICENSE). All examples are fictional; no real client, employer, or operational data.
