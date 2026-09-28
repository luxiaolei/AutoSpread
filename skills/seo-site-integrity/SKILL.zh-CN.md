---
name: seo-site-integrity-zh
description: 从 Schema、Sitemap、图片和发布后 Drift 四个方面检查并保护 SEO 关键站点完整性。
---

# SEO 站点完整性

站点需要结构化 SEO QA、重大 Deploy 后检查，或排名/流量在网站改动后异常时使用。这里把四类高度相关的完整性检查放在一个 Skill 里，而不是强制拆成四个常驻 Agent。

## 按模式路由

- **schema**：检测结构化数据、验证语法和实体关系，确认标记与页面可见真实内容一致，并检查该类型当前是否对搜索界面真的有价值。
- **sitemap**：发现 robots 声明和常见 Sitemap，验证 URL 与 canonical/indexability 一致性，并比较重要可抓取页面的覆盖情况。
- **images**：检查适用的 Alt、装饰图片处理、尺寸/CLS、响应式加载、LCP 图片策略、格式/压缩、文件名和图片可发现性。
- **drift**：在重要发布前后保存或比较 SEO 关键字段的已知良好基线。

## Drift 基线

对重要模板/页面至少记录：HTTP 状态、Title、Meta Description、Canonical、Robots、H1/H2、关键 JSON-LD 类型/内容 Hash、重要 Open Graph、渲染后主内容 Hash，以及相关性能信号。比较前先规范化 URL。

变化分为：

- **critical**：可能让重要页面消失、跳转或失去索引资格的状态码/Canonical/Robots 变化；
- **warning**：Schema、Heading、Metadata、内容或性能回退，需要调查；
- **info**：有意或低风险变化，记录复核即可。

时间上同时发生不等于因果关系。Drift 只能作为调查线索，不能直接证明流量变化原因。

## 质量规则

- 合适时优先 JSON-LD，但绝不能生成页面上不存在或无法验证的事实。
- 不能因为 Schema.org 有某个类型就机械添加；先确认当前搜索支持和业务价值。
- Sitemap 应包含首选 Canonical、可索引目标，不应塞 Redirect、Noindex 或重复 Variant。
- `lastmod` 应反映有意义的页面变化，不能机械刷新日期。
- 首屏/LCP 主图不要 Lazy Load；图片要有尺寸或 Aspect Ratio，减少布局抖动。
- 不把固定 KB 阈值当作所有图片的普遍真理，要结合实际尺寸、质量、传输和性能优化。

## 核验

修复后重新抓取渲染页面和外部文件，重新验证 Schema/Sitemap、比较 Drift 基线并记录实际变化字段。涉及搜索意图/布局和转化的问题交给 `search-experience` 或 `conversion-optimization`。
