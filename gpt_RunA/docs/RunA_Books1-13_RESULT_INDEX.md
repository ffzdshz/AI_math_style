# RunA Book 1–13 证明结果位置索引

- 日期：2026-10-02（客户端日期；Asia/Shanghai）。
- 工程目录：`/data/WYC/mathProofV2/euclid-proof-project`。
- 全 13 卷，共 465 个命题；均为 RunA，默认输出保持不变。
- Markdown 保存完整逐步 AI 证明；CSV 的 `AI_USED` 列为 AI 引用列表，保留原有对比字段。
- 只生成证明，不评判数学正确性或逻辑完整性。

| 卷 | 命题数 | 完整证明 MD | 引用 CSV | 执行元数据 | 逐命题证明 |
|---|---:|---|---|---|---|
| Book 1 | 48 | [MD](../outputs/RunA_Book1_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book1_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book1_Execution_Metadata.json) | [目录](../proofs/RunA_Book1/) |
| Book 2 | 14 | [MD](../outputs/RunA_Book2_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book2_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book2_Execution_Metadata.json) | [目录](../proofs/RunA_Book2/) |
| Book 3 | 37 | [MD](../outputs/RunA_Book3_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book3_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book3_Execution_Metadata.json) | [目录](../proofs/RunA_Book3/) |
| Book 4 | 16 | [MD](../outputs/RunA_Book4_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book4_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book4_Execution_Metadata.json) | [目录](../proofs/RunA_Book4/) |
| Book 5 | 25 | [MD](../outputs/RunA_Book5_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book5_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book5_Execution_Metadata.json) | [目录](../proofs/RunA_Book5/) |
| Book 6 | 33 | [MD](../outputs/RunA_Book6_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book6_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book6_Execution_Metadata.json) | [目录](../proofs/RunA_Book6/) |
| Book 7 | 39 | [MD](../outputs/RunA_Book7_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book7_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book7_Execution_Metadata.json) | [目录](../proofs/RunA_Book7/) |
| Book 8 | 27 | [MD](../outputs/RunA_Book8_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book8_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book8_Execution_Metadata.json) | [目录](../proofs/RunA_Book8/) |
| Book 9 | 36 | [MD](../outputs/RunA_Book9_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book9_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book9_Execution_Metadata.json) | [目录](../proofs/RunA_Book9/) |
| Book 10 | 115 | [MD](../outputs/RunA_Book10_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book10_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book10_Execution_Metadata.json) | [目录](../proofs/RunA_Book10/) |
| Book 11 | 39 | [MD](../outputs/RunA_Book11_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book11_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book11_Execution_Metadata.json) | [目录](../proofs/RunA_Book11/) |
| Book 12 | 18 | [MD](../outputs/RunA_Book12_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book12_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book12_Execution_Metadata.json) | [目录](../proofs/RunA_Book12/) |
| Book 13 | 18 | [MD](../outputs/RunA_Book13_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book13_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book13_Execution_Metadata.json) | [目录](../proofs/RunA_Book13/) |

## 路径规则

```text
outputs/RunA_BookX_StepByStep_Proofs.md
outputs/RunA_BookX_AI_vs_Human_Citations.csv
outputs/RunA_BookX_Execution_Metadata.json
proofs/RunA_BookX/
runs/RunA_BookX/book_result.json
```

以上 X 为 1–13；所有相对路径均以工程目录为根目录。

## 打包内容

- ZIP 内使用同样的相对目录，根目录为 `Euclid_RunA_Books1-13/`。
- 包含 13 份整卷 MD、13 份引用 CSV、13 份执行元数据、465 份逐命题 MD。
- 同时包含所选最终结果 JSON、运行清单、越序审计、保存审计和批次完成汇报。
- 不包含原始会话日志、私有推理/会话记录、认证文件或运行上下文副本。
- 这是结果快照，不包含可独立重跑的完整代码与源数据环境。
