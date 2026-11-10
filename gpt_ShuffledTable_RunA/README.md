# Euclid 乱序子表工程 — Run A / Books 1–13

13 卷、465 命题生成完成，结构和保存结果审计通过；不代表数学正确性已验证。worker 请求配置 gpt-6-astra / xhigh，上游模型权重未独立鉴证。

## 文件

- `docs/SHUFFLED_RUNA_RESULT_INDEX_20261106.md`：按卷结果入口。
- `outputs/`：13 份整卷证明 MD、13 份引用 CSV、13 份执行元数据 JSON。CSV 的 AI 引用在 `AI_USED` 列，保留原 Human/Jaccard 字段。
- `proofs/`：465 份逐命题 MD。
- `runs/`：各卷冻结结果、manifest、顺序和保存结果审计、批次状态及完成报告。
- `docs/`：导出审计及成功执行耗时对照和逐命题表。

原始输出按字节保存；本包不含 raw/ 原始会话、stage2_context/、资源子表、凭据或可从头运行的完整源工程。执行文件中的工程绝对路径仅为来源记录。旧版与本版的可用前卷陈述不同，不能视为纯乱序单变量对照。

`PACKAGE_MANIFEST.json` 列明其余所有文件的字节数和 SHA-256；ZIP 外另有文件整体 SHA-256。
