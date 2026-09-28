# 方法来源说明

AutoSpread 使用 MIT License，并刻意不把第三方 Skill 库整包 vendoring 进来。调研过程中会吸收通用的工作流结构、路由方法和质量门。

## Claude SEO

`AgriciDaniel/claude-seo`（MIT）明显影响了 AutoSpread v0.3 的“条件式 SEO 专家层”。主要吸收的是这些通用思想：

- 先识别站点/业务信号，再按需调用专家检查，而不是所有网站全部跑一遍；
- 把 SEO Drift 当成发布前后 Baseline/Diff 问题；
- 把 Search Experience / 页面类型与意图匹配从技术 SEO 中单独拿出来；
- Local、International/Hreflang、E-commerce、Schema/Sitemap/Image、Agent 可操作性分别作为条件式问题处理；
- 把 GEO/AI Citation 与 Agent Operability 明确区分；
- 只有外部数据源已配置且预算允许时，才用 DataForSEO/Firecrawl 等增强。

AutoSpread 没有复制 Claude SEO 的脚本、评分体系、数据集或第三方统计结论。两者存在差异时，AutoSpread 优先保持宿主无关、业务结果导向、保守证据表达，以及自己的自主权/能力模型。

来源：https://github.com/AgriciDaniel/claude-seo
