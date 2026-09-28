---
name: international-seo-zh
description: 设计并验证多语言/多地区搜索架构、Hreflang、本地化、Canonical 和地区体验。
---

# International SEO

产品通过不同 URL/内容服务多语言或多地区市场时使用。

## 架构

1. 盘点 Locale/Region Variant，判断业务真正需要 Language-only、Country-specific 还是两者结合。
2. 映射不同 Locale 的等价页面；不是实际等价内容就不要建立 Hreflang 关系。
3. 确认每个 Locale 都有稳定 Canonical，Alternate 关系互相返回且一致。
4. 使用搜索引擎支持的有效语言/Script/Region 组合，具体 Code 要验证，不能猜。
5. 只有存在真正 Fallback/Selector 体验时才用 `x-default`，并非所有站点必需。
6. 根据维护成本和页面类型选择 HTML、HTTP Header 或 XML Sitemap 方式，避免多个实现互相冲突。

## 本地化质量

International SEO 不是只做翻译。检查当地术语、单位、币种、价格/可用性、法律/合规说明、案例/Proof、Support、Shipping/Service、CTA 目标和当地搜索意图。避免强制 IP Redirect 让搜索引擎难以抓取，或不给用户退出选择。

## 核验

检查 Self/Return、Canonical、HTTP 状态、Indexability、Locale 内容，以及有数据时的地区搜索表现。SERP 差异重要时记录市场、日期和设备。

实体本地业务问题交给 `local-seo`；全站结构问题交给 `seo-site-integrity`。
