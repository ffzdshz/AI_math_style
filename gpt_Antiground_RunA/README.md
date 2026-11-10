# Euclid Anti-grounding — Run A / Books 1–13

本包为新迁移工程的完整 Run A 结果，不是旧工程 Run A。

- 13 卷，465 个命题，全部完成；批次结束 2026-11-03T14:15:24.808793+08:00。
- 证明 worker 请求配置 gpt-6-astra / xhigh，默认 legacy 上下文。
- 使用 anti-grounding 策略句；不根据 Jaccard 或数学正确性筛选证明。
- 13 份整卷证明 Markdown、13 份引用 CSV、13 份执行元数据 JSON。
- 465 份逐命题 Markdown，13 卷冻结 JSON、顺序审计和保存结果审计。
- 完整性审计通过不等于证明正确；上游实际模型权重没有独立鉴证。

## 阅读入口

打开 `docs/RunA_Books1-13_RESULT_INDEX.md`，或直接进入 `outputs/`。
CSV 的 AI 引用列表为 `AI_USED` 列，保留 Human_Refs/Jaccard 等原始字段。
原始证明和输出按字节保存，未重写为新的默认格式。

## 校验

`PACKAGE_MANIFEST.json` 列出除它自身之外每个文件的字节数和 SHA-256。
ZIP 外另有同名 `.sha256` 校验文件。

## 边界

不包含原始模型会话 raw/、提示词上下文 stage2_context/、认证资料或临时 HOME。
审计 JSON 保留执行摘要和来源路径，不包含原始模型会话日志。
原工程绝对路径仅作来源记录；解压后使用包内相对路径。
此包不提供从头运行证明所需的全部源工程。
