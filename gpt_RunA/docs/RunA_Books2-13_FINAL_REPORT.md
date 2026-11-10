# RunA Books 2–13 完成总汇报

- 批次完成时间：2026-10-02T14:53:50.121229+08:00（Asia/Shanghai）。
- 任务：按 Book 2 → Book 13 顺序，生成各卷全部命题，全部 RunA。
- 结果：12 卷、417/417 个命题；加上此前 Book 1 的 48 个，RunA 全 13 卷共 465 个命题。
- 所选证明的 417 个 session ID 各不相同；CLI 观测配置均为 gpt-6-astra / xhigh。
- 模式：legacy；每卷最大并发 4；卷间串行；默认输出未改变。
- 越序重证：0 次；未解决越序引用：0 个。
- 不评判证明的数学正确性或逻辑完整性；审计仅针对生成/格式/引用顺序/文件和元数据。
- 模型证据验证 CLI 会话配置，不是代理上游模型的独立认证。

## 各卷产物

| 卷 | 生成数量 | 平均 Jaccard（原舍入口径） | AI 证明 MD | 引用 CSV（含 AI_USED） | 元数据 | 完成汇报 |
|---|---:|---:|---|---|---|---|
| Book 2 | 14/14 | 0.085429 | [MD](../outputs/RunA_Book2_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book2_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book2_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book2_COMPLETION.md) |
| Book 3 | 37/37 | 0.194649 | [MD](../outputs/RunA_Book3_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book3_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book3_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book3_COMPLETION.md) |
| Book 4 | 16/16 | 0.182438 | [MD](../outputs/RunA_Book4_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book4_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book4_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book4_COMPLETION.md) |
| Book 5 | 25/25 | 0.360920 | [MD](../outputs/RunA_Book5_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book5_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book5_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book5_COMPLETION.md) |
| Book 6 | 33/33 | 0.277545 | [MD](../outputs/RunA_Book6_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book6_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book6_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book6_COMPLETION.md) |
| Book 7 | 39/39 | 0.249769 | [MD](../outputs/RunA_Book7_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book7_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book7_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book7_COMPLETION.md) |
| Book 8 | 27/27 | 0.341333 | [MD](../outputs/RunA_Book8_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book8_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book8_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book8_COMPLETION.md) |
| Book 9 | 36/36 | 0.245583 | [MD](../outputs/RunA_Book9_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book9_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book9_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book9_COMPLETION.md) |
| Book 10 | 115/115 | 0.246287 | [MD](../outputs/RunA_Book10_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book10_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book10_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book10_COMPLETION.md) |
| Book 11 | 39/39 | 0.257923 | [MD](../outputs/RunA_Book11_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book11_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book11_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book11_COMPLETION.md) |
| Book 12 | 18/18 | 0.175500 | [MD](../outputs/RunA_Book12_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book12_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book12_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book12_COMPLETION.md) |
| Book 13 | 18/18 | 0.180167 | [MD](../outputs/RunA_Book13_StepByStep_Proofs.md) | [CSV](../outputs/RunA_Book13_AI_vs_Human_Citations.csv) | [JSON](../outputs/RunA_Book13_Execution_Metadata.json) | [汇报](../runs/RunA_Books2-13_Batch/Book13_COMPLETION.md) |

## 中断与恢复记录

- Book 8：8.6 的原始尝试超时，保留原 26 个结果，仅用新会话补跑缺失的 1 个。
- Book 10：1 个超时、18 个返回用量限制，保留原 96 个结果；模型重新可用后补齐 19 个。
- 两次恢复均保持 gpt-6-astra / xhigh、相同前提预算和默认产物格式。
- 补跑依据执行可用性，不依据证明正确性、逻辑完整性或 Jaccard 高低。
- 共 437 次实际执行记录，其中 417 个结果被选为最终证明，20 个失败记录保留；无越序重证。
- 旧尝试/旧成功结果的字节哈希在恢复时核对，不覆盖原始记录。

## 索引与审计

- [批次最终审计 JSON](../runs/RunA_Books2-13_Batch/FINAL_AUDIT.json)
- [进度看板](RunA_Books2-13_PROGRESS.md)
- [批次状态](../runs/RunA_Books2-13_Batch/batch.json)
- [完整事件记录](../runs/RunA_Books2-13_Batch/events.jsonl)
- [Book 1 原有证明](../outputs/RunA_Book1_StepByStep_Proofs.md)
- [Book 1 原有引用比较](../outputs/RunA_Book1_AI_vs_Human_Citations.csv)

所有目录前缀均为 `/data/WYC/mathProofV2/euclid-proof-project/`。
每卷逐命题证明在 `proofs/RunA_BookX/`；原始结果、失败记录与单次 session 证据在 `runs/RunA_BookX/`。
