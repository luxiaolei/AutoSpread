# 快速开始

1. 运行 `python3 scripts/autospread.py init-context PATH/.autospread` 初始化产品工作区，会生成产品事实、自主权策略、能力清单、实验台账和工作日志。
2. 只填写已经知道的事实，未知信息保持未知。
3. 让承担 Growth Lead 的 Agent 会话读取 `skills/autospread/SKILL.md`。
4. 给 Lead 产品仓库/路径、线上地址、经营目标、时间范围，以及你明确希望调整的自主权。
5. 先要求只读项目体检和增长约束诊断，不要预先指定一定要做某个渠道。
6. Lead 只加载解决当前约束真正需要的 Playbook。
7. 重要动作前登记实验并检查 `autonomy-policy.yaml`。
8. 可重复工作优先 API/MCP、CLI 和确定性代码；UI-only 或登录态流程再使用 `ego-browser`。
9. 写操作之后核验外部真实状态，并把证据/ID 写入工作日志。
10. 观察窗口结束后重新诊断约束。

把全部 AutoSpread Skills 安装到另一个本地项目：

```bash
python3 scripts/autospread.py install /path/to/project
```

安装器默认不覆盖已有 Skill 目录，只有加 `--force` 才会覆盖。
