# Euclid 倒序子表工程 — Run A / Books 1–13

13 卷、465 个命题已生成；结构和保存结果审计通过，但**不代表数学证明正确性已验证**。证明 worker 请求和 CLI 会话配置为 gpt-6-astra / xhigh；上游实际模型权重没有独立鉴证。

## 阅读入口

- `docs/REVERSE_RUNA_RESULT_INDEX_20261107.md`：分卷链接。
- `outputs/`：13 份整卷证明 Markdown、13 份引用对照 CSV 和 13 份执行元数据 JSON。CSV 的 `AI_USED` 列是 AI 引用列表，保留原 Human/Jaccard 等列。
- `proofs/`：465 份逐命题 Markdown。
- `runs/`：每卷冻结结果、manifest、顺序及保存结果审计，以及批次进度和完成报告。
- `examples/`：6.10 的倒序表 prepare-only 样例，不是正式 6.10 工作会话的文件。

数据行按原 Excel 物理行逆序后筛选该命题允许引用的条目，保留表头。每卷审计独立重新核对源表倒序、资源集合及哈希；提示词与乱序实验一致。输出和原始证明按字节复制，不改默认格式。

本包不含 `raw/` 原始模型会话、`stage2_context/`、逐命题资源子表、账号凭据、临时 HOME 或完整可运行源工程。文件中的原工程绝对路径仅作来源记录。`PACKAGE_MANIFEST.json` 列明其他每个文件的大小和 SHA-256；压缩包外另有同名 `.sha256` 文件。
