# 快速开始

1. 把 `templates/product-context.md` 和 `templates/work-log.md` 复制到产品工作区，
   或运行 `python3 scripts/autospread.py init-context PATH`。
2. 在 Codex 会话中读取 `skills/autospread/SKILL.md`。
3. 带着范围和安全约束请求一次产品体检。
4. 只加载下一步真正需要的角色 Skill。
5. 在工作记录中保存证据和外部动作状态。

将 Lead Skill 安装到另一个本地工作区：

```bash
python3 scripts/autospread.py install /path/to/project
```

安装器发现已有文件时会停止，只有加 `--force` 才会覆盖。
