# AI Launch Red Team (ai-launch-red-team)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Skill](https://img.shields.io/badge/type-agent%20skill-blue)
![Platforms](https://img.shields.io/badge/Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20Codex-supported-lightgrey)

[中文说明](README.md)

For project status, scope, feedback, and public-material boundaries, see [`STATUS.md`](STATUS.md).

A zero-code agent skill for reviewing an “our AI is ready to launch” proposal. It applies **eight veto conditions** and **seven review dimensions**, then returns a **launch veto card** for the review meeting: which conditions are triggered, which proposal sentence supports each finding, and what the team should answer next.

It answers one question:

> The demo works. What conditions still need to be addressed before it touches a real workflow?

## Install

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

The card contains four parts: an eight-row veto scan that quotes the proposal, a seven-dimension check (answered / vague / missing), a risk-ordered question list, and a recommendation for the next review step. The example above triggers two vetoes: automatic refund execution has no human review, and the plan names no error or rollback owner. Full output: [examples/01-refund-agent.md](examples/01-refund-agent.md).

## How it reviews

The eight vetoes and seven dimensions come from the frozen review contract of the [AI Prototype-to-Production Toolkit](https://github.com/Anonymousyz/ai-prototype-to-production-toolkit): unauthorized data use, sensitive data to an unapproved model, high-risk decisions without human review, no logs or traceability, no error or rollback owner, unevaluable output quality, uncontrolled cost, and a demo marketed as production-ready.

## Scope

- **Fact checking remains outside the skill.** “We have logs” is recorded as a claim, and the question list asks for evidence.
- **The card does not score or approve a plan.** For a filed, reviewable assessment with reports, use the full toolchain:

| Need | Go to |
|---|---|
| Formal 70-point assessment with vetoes and HTML reports | [ai-prototype-to-production-toolkit](https://github.com/Anonymousyz/ai-prototype-to-production-toolkit) (`ai-ready` CLI) |
| Turn assessment results into a decision packet | [research-to-decision-toolkit](https://github.com/Anonymousyz/research-to-decision-toolkit) (`r2d` CLI) |
| Find evaluation, guardrail, and observability tools by gap | [awesome-ai-production-readiness](https://github.com/Anonymousyz/awesome-ai-production-readiness) (resource catalog) |

## License

MIT. See [LICENSE](LICENSE). All examples are fictional; no real client, employer, or operational data.
