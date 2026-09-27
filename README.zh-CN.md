# AutoSpread

AutoSpread 是一个轻量、双语的 AI 增长经营系统。你把产品仓库、线上地址、经营目标和自主权边界交给一个能力足够的 Agent；Lead 先诊断当前最大增长约束，只加载真正需要的打法，使用已连接工具执行，核验真实外部结果，再根据结果进入下一轮学习。

它刻意不做另一个多 Agent Runtime。角色是方法，不是必须常驻的 Bot。一个 Codex / ChatGPT / Hermes / Claude 类会话可以承担多个角色；宿主支持时，也可以把相互独立的工作分给子 Agent。

## v0.2 工作模型

```text
产品 + 经营目标 + 自主权策略
          |
      Growth Lead
          |
      诊断最大约束
          |
    选择最小有效打法
          |
产品 / 漏斗 / 变现 / SEO-GEO / 内容 / 渠道 / 生命周期 / 付费
          |
API/MCP -> CLI -> SDK/代码 -> ego-browser -> 人工
          |
        执行 + 核验
          |
激活 / 收入 / 留存 / 学习
          `----> 下一轮
```

## v0.2 包含

- Growth Lead 总路由和增长约束诊断；
- 明确的自主权策略 Skill 和可编辑 Policy 模板；
- 项目体检、客户研究、CRO、定价变现、生命周期、付费获客和数据复盘；
- 把搜索拆成 SEO 基础、GEO/答案引擎优化、AI 可见度测量三层；
- 内容策略、内容/视频生产、渠道选择和渠道运营；
- 把每次重要动作连接到业务证据的增长实验契约；
- 19 套中英文 Agent Skills；
- 5 个产品工作区模板：产品事实、自主权策略、能力清单、实验台账、工作日志；
- 64 项机器可读能力目录，包括 Skill、Plugin、MCP、CLI、平台和可选 Runtime；
- 只依赖 Python 标准库的校验、目录筛选、上下文初始化和项目级 Skill 安装工具。

## 使用方式

在能力足够的会话里读取 `skills/autospread/SKILL.md`，然后给它产品路径/仓库、线上地址、经营目标，以及你愿意授予的自主权。

```text
读取 /path/to/AutoSpread/skills/autospread/SKILL.md。
接手 /path/to/my-product 和 https://example.com 的增长。
遵守产品目录里的 autonomy-policy.yaml。
先做只读体检和增长约束诊断，再在授权范围内提出或执行最小有效增长实验。
```

初始化产品记录：

```bash
python3 scripts/autospread.py init-context /path/to/my-product/.autospread
```

按角色或关键词找资源：

```bash
python3 scripts/autospread.py catalog --role geo-optimization
python3 scripts/autospread.py catalog --query stripe
```

运行离线校验：

```bash
python3 scripts/autospread.py validate
python3 -m pytest -q
```

完整逻辑见 `docs/zh-CN/operating-model.md`；英文版见 `docs/en/operating-model.md`。
