# AI 上线否决卡（ai-launch-red-team）

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Skill](https://img.shields.io/badge/type-agent%20skill-blue)
![平台](https://img.shields.io/badge/Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20Codex-supported-lightgrey)

[English](README.en.md)

这是一个无需运行代码的 Agent 技能。把“我们的 AI 准备上线”这类方案描述交给它，它会按 **8 条一票否决**和**七个维度**做结构化红队评审，并生成一张可带进评审会的上线否决卡：哪些条件触发了否决、依据是方案中的哪句话、还应当追问什么。

它只回答一个问题：

> 演示已经跑通。若要接触真实业务，还缺哪些条件？

## 安装

```bash
# Claude Code
git clone https://github.com/Anonymousyz/ai-launch-red-team.git ~/.claude/skills/ai-launch-red-team

# Cursor
git clone https://github.com/Anonymousyz/ai-launch-red-team.git ~/.cursor/skills/ai-launch-red-team

# Codex
git clone https://github.com/Anonymousyz/ai-launch-red-team.git ~/.codex/skills/ai-launch-red-team
```

Windows 把 `~` 换成 `%USERPROFILE%`。也可以直接下载 ZIP,把文件夹放进对应的 skills 目录。

## 怎么用

安装后，在支持该技能的 Agent 中提出评审请求，例如：

```text
用上线否决卡红队一下这个方案:
我们做了个客服退款 Agent,用大模型处理用户退款请求,准确率测过 95%,
可以自动执行退款,下周对全部用户上线,监控后面再补。
```

你会得到一张否决卡：

- **一票否决扫描表**：8 条逐一判定【触发 / 存疑 / 未触发】，每条引用方案原话；
- **七维快检**：业务价值、数据边界、质量评估、人工复核、日志审计、运维成本、组织采纳，逐项标注【已答 / 含糊 / 缺失】；
- **追问清单**：按风险排序，可在评审会上直接提出；
- **红队建议**：先处理什么，再讨论上线范围。

上例会触发两条否决：“自动执行退款”对应高风险决策无人工复核；“监控后面再补”说明没有差错处理或回滚负责人。完整输出见 [examples/01-refund-agent.md](examples/01-refund-agent.md)。

## 评审逻辑

```mermaid
flowchart LR
    A["方案描述<br/><i>你粘贴的上线计划</i>"] --> B["8 条一票否决扫描<br/><i>逐条判定,引用原文</i>"]
    B --> C["七维快检<br/><i>已答 / 含糊 / 缺失</i>"]
    C --> D["上线否决卡<br/><i>判定 + 追问清单 + 建议</i>"]
    D -- "有否决触发" --> E["先解决否决项<br/>再谈上线范围"]
    D -- "无否决,缺口少" --> F["用 ai-ready CLI 做<br/>可留档的 70 分完整评估"]
```

8 条否决与七个维度来自 [AI Prototype-to-Production Toolkit](https://github.com/Anonymousyz/ai-prototype-to-production-toolkit) 的固定评审契约:未经授权使用数据、敏感数据进入未批准的模型、高风险决策无人工复核、无日志或不可追溯、无差错处理或回滚负责人、输出质量无法评估、成本失控、演示冒充生产就绪。

## 三个示例

| 示例 | 演示什么 |
|---|---|
| [01 客服退款 Agent](examples/01-refund-agent.md) | 两条否决触发:资金动作无人复核、无回滚负责人 |
| [02 内部知识库助手](examples/02-kb-assistant.md) | 敏感数据流向未批准模型;授权与日志说不清 |
| [03 合同条款初筛](examples/03-controlled-pilot.md) | 无否决触发的干净方案长什么样,以及它仍然欠的三件事 |

## 使用边界

- **不核实事实。**方案写“有日志”时，技能只能记录为“声称有日志”，并在追问清单中索要证据。
- **不打分，也不批准。**它给出结构性缺口和初步判断。需要可留档、可复核并生成报告的评估时，可使用完整工具链：

| 你需要 | 去哪 |
|---|---|
| 70 分制 + 8 条否决的正式评估与 HTML 报告 | [ai-prototype-to-production-toolkit](https://github.com/Anonymousyz/ai-prototype-to-production-toolkit)(`ai-ready` CLI) |
| 把评估结果变成负责人能拍板的决策包 | [research-to-decision-toolkit](https://github.com/Anonymousyz/research-to-decision-toolkit)(`r2d` CLI) |
| 按缺口查找评估、护栏和可观测工具 | [awesome-ai-production-readiness](https://github.com/Anonymousyz/awesome-ai-production-readiness)（资源目录） |

## 许可证

MIT，见 [LICENSE](LICENSE)。示例均为虚构内容，不含真实客户、雇主或运行数据。
