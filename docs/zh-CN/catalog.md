# 资源目录

机器可读目录在 [`../catalog.json`](../catalog.json)。AutoSpread v0.2 收录 64 项按角色整理的能力指针，包括 Agent Skills、官方 MCP/API、CLI、内容/发布工具、分析系统和可选 Runtime。

目录条目只是“可以考虑使用的能力”，不代表已经安装，也不代表账号已经授权。真正执行前仍要核对提供方最新文档、权限、价格、平台政策，以及用户的自主权策略。

v0.2 重点新增了 Corey AI SEO、Aaron Marketing Skills 的 SEO/GEO 生命周期、UnifAPI AI Visibility、Google Search 官方 AI 功能说明、ScrapeCreators 社媒研究 Skills、Social Media Skills，以及 Cloudflare / Supabase / Stripe / Vercel 的官方 Agent 接入能力。

按角色筛选或全文搜索：

```bash
python3 scripts/autospread.py catalog --role ai-visibility
python3 scripts/autospread.py catalog --query cloudflare
```
