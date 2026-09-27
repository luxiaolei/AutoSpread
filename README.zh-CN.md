# AutoSpread

AutoSpread 是一个轻量的 Codex 增长工作插件。它让一个会话承担增长 Lead，
按需加载角色方法、选择可用工具，并用证据核验交付结果。它不要求消息总线、
数据库、常驻团队或固定的营销平台。

## 内容

- 一个决定最小工作流的 Lead Skill；
- 十套体检、研究、SEO/GEO、转化、内容、渠道、数据、生命周期和付费获客方法；
- `skills/autospread/references/` 下的角色与分工规则；
- 双语快速开始、产品事实和工作记录模板；
- 有来源的机器可读资源目录；
- 只用标准库的校验、目录筛选、产品记录初始化和项目技能安装工具。

## 使用

在 Codex 会话中读取 `skills/autospread/SKILL.md`，并提供产品目录。Lead 会先
读取产品记录、检查当前可用工具，再选择需要的角色 Skill。小任务由当前会话完成；
宿主支持时，独立工作可以分工给子 Agent。

```text
读取 /path/to/AutoSpread/skills/autospread/SKILL.md。
作为 /path/to/my-product 的唯一增长 Lead，用中文工作。
先完成产品体检。没有我的明确批准，不要发布、花钱、修改生产环境或创建定时任务。
```

运行离线检查：

```bash
python3 scripts/autospread.py validate
python3 tests/test_structure.py
```

英文文档见 `README.md` 和 `docs/en/`。
