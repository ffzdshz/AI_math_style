# RunA Books 2–13 AI 证明生成进度

- 更新时间：2026-10-02T15:00:14.584878+08:00（Asia/Shanghai）。
- 目标：依次生成 Book 2–13 的 417 个命题，全部 RunA。
- 配置：gpt-6-astra / xhigh；legacy；每卷并发 4；卷间严格串行。
- 范围：生成、格式/引用顺序检查与原有引用比较；不评判数学正确性。
- 批次状态：[batch.json](../runs/RunA_Books2-13_Batch/batch.json)。
- 状态：已完成 / 进行中 / 受阻 / 待推进。

## 目标总览

| Target | 目标简洁定义 | 状态 | 最新结论 | 关键结果文档 | 结果目录 | 正在进行 | 下一 gate |
|---|---|---|---|---|---|---|---|
| Book 2 | RunA 生成该卷全部 14 个命题 | 已完成 | 14/14 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book2_COMPLETION.md) · [证明 MD](../outputs/RunA_Book2_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book2_AI_vs_Human_Citations.csv) | [RunA_Book2](../runs/RunA_Book2/) | 无 | 已关闭生成目标 |
| Book 3 | RunA 生成该卷全部 37 个命题 | 已完成 | 37/37 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book3_COMPLETION.md) · [证明 MD](../outputs/RunA_Book3_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book3_AI_vs_Human_Citations.csv) | [RunA_Book3](../runs/RunA_Book3/) | 无 | 已关闭生成目标 |
| Book 4 | RunA 生成该卷全部 16 个命题 | 已完成 | 16/16 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book4_COMPLETION.md) · [证明 MD](../outputs/RunA_Book4_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book4_AI_vs_Human_Citations.csv) | [RunA_Book4](../runs/RunA_Book4/) | 无 | 已关闭生成目标 |
| Book 5 | RunA 生成该卷全部 25 个命题 | 已完成 | 25/25 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book5_COMPLETION.md) · [证明 MD](../outputs/RunA_Book5_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book5_AI_vs_Human_Citations.csv) | [RunA_Book5](../runs/RunA_Book5/) | 无 | 已关闭生成目标 |
| Book 6 | RunA 生成该卷全部 33 个命题 | 已完成 | 33/33 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book6_COMPLETION.md) · [证明 MD](../outputs/RunA_Book6_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book6_AI_vs_Human_Citations.csv) | [RunA_Book6](../runs/RunA_Book6/) | 无 | 已关闭生成目标 |
| Book 7 | RunA 生成该卷全部 39 个命题 | 已完成 | 39/39 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book7_COMPLETION.md) · [证明 MD](../outputs/RunA_Book7_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book7_AI_vs_Human_Citations.csv) | [RunA_Book7](../runs/RunA_Book7/) | 无 | 已关闭生成目标 |
| Book 8 | RunA 生成该卷全部 27 个命题 | 已完成 | 27/27 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book8_COMPLETION.md) · [证明 MD](../outputs/RunA_Book8_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book8_AI_vs_Human_Citations.csv) | [RunA_Book8](../runs/RunA_Book8/) | 无 | 已关闭生成目标 |
| Book 9 | RunA 生成该卷全部 36 个命题 | 已完成 | 36/36 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book9_COMPLETION.md) · [证明 MD](../outputs/RunA_Book9_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book9_AI_vs_Human_Citations.csv) | [RunA_Book9](../runs/RunA_Book9/) | 无 | 已关闭生成目标 |
| Book 10 | RunA 生成该卷全部 115 个命题 | 已完成 | 115/115 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book10_COMPLETION.md) · [证明 MD](../outputs/RunA_Book10_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book10_AI_vs_Human_Citations.csv) | [RunA_Book10](../runs/RunA_Book10/) | 无 | 已关闭生成目标 |
| Book 11 | RunA 生成该卷全部 39 个命题 | 已完成 | 39/39 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book11_COMPLETION.md) · [证明 MD](../outputs/RunA_Book11_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book11_AI_vs_Human_Citations.csv) | [RunA_Book11](../runs/RunA_Book11/) | 无 | 已关闭生成目标 |
| Book 12 | RunA 生成该卷全部 18 个命题 | 已完成 | 18/18 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book12_COMPLETION.md) · [证明 MD](../outputs/RunA_Book12_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book12_AI_vs_Human_Citations.csv) | [RunA_Book12](../runs/RunA_Book12/) | 无 | 已关闭生成目标 |
| Book 13 | RunA 生成该卷全部 18 个命题 | 已完成 | 18/18 生成；未解决越序 0 | [汇报](../runs/RunA_Books2-13_Batch/Book13_COMPLETION.md) · [证明 MD](../outputs/RunA_Book13_StepByStep_Proofs.md) · [引用 CSV](../outputs/RunA_Book13_AI_vs_Human_Citations.csv) | [RunA_Book13](../runs/RunA_Book13/) | 无 | 已关闭生成目标 |

## 正在进行

| 分支 | Owner | 当前进展 | 预期产物 | 下一关键检查 |
|---|---|---|---|---|
| 无 | 无 | 当前没有正在执行的卷 | — | 查看批次状态 |

## 关键结果索引

- [批次事件](../runs/RunA_Books2-13_Batch/events.jsonl)
- [操作手册](CODEX_OPERATION_GUIDE.md)

## 阻塞与结论边界

- 本批次不新增数学正确性或完整性门禁，不依语义疑问重证。
- 初稿＋最多三次越序重证；仍未解决的引用按原协议标记并保留。
- 失败/配额/超时不自动降级，不跳过卷，不覆盖既有结果。
- 每卷完成事件和具体路径单独落盘，主会话据此汇报。
