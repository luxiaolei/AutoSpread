---
name: agent-readiness-zh
description: 让网站更适合代表用户操作的 AI Agent 使用，同时明确区分 Agent 可操作性和 GEO 排名/引用。
---

# Agent Readiness

这和 GEO 是不同问题。GEO 关注答案引擎是否能理解/引用内容；Agent Readiness 关注代表用户行动的 AI Agent 能否稳定读取、导航、填写、提交并确认真实流程。

## 基础

1. 优先可访问的语义 HTML、清晰 Label/Role、键盘可操作控件、稳定确认状态，避免只有 Hover 才可发现的关键交互。
2. 重要公开内容应通过适合站点的渲染/服务端方式可靠出现；关键动作要有确定性的成功/失败状态。
3. 按用途区分访问政策：搜索/索引、模型训练、用户触发 Agent 不是同一类，不能用一个 Bot 的 Robots 状态推断另一类。
4. 只有授权后才测试 WAF/CAPTCHA/Login 行为，并准确报告测试范围，不能声称所有 Agent 都可访问。
5. 私有或重大动作应依靠认证和明确确认保护，而不是 robots.txt。

## 可选增强

Markdown 版本、Discovery 文件、API Catalog、Agent Card、WebMCP 类工具可能改善某些 Agent 工作流，但支持取决于平台和浏览器。把它们视为可选互操作实验，不是 SEO 必需项，也不能保证流量或引用。

对 Agent 可调用的交易/写入工具，应暴露最小真实操作、准确描述、明确重大动作标记、参数校验、确认、日志，以及适用时的幂等性。工具描述绝不能诱导 Agent 绕过用户确认。

## 核验

有条件时用已批准的真实 Browser/Agent 跑完整链路：发现 -> 导航 -> 填写/选择 -> 提交 -> 观察确认。记录 Accessibility、动态渲染、Auth/WAF、状态歧义或工具安全问题。排名/引用问题仍交给 `geo-optimization` 和 `ai-visibility`。
