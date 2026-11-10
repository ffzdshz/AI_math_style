# Euclid RunA Books 1–13 结果包

客户端日期：2026-10-02；Asia/Shanghai。

13 卷、465 个命题。保持工程原有默认输出，未对证明数学正确性作判断。

## 打开方式

- 先阅读 docs/RunA_Books1-13_RESULT_INDEX.md。
- outputs/：13 份整卷完整 AI 证明 MD，13 份引用比较 CSV，13 份执行元数据。
- CSV 的 AI_USED 列就是模型引用列表，多引用用 | 分隔。导入 Excel 时请将 Proposition 列指定为文本，避免 1.10 被转成 1.1。
- proofs/RunA_BookX/：465 份逐命题完整证明 MD。
- runs/RunA_BookX/：最终结果 JSON、运行清单、越序审计、保存审计。
- docs/RunA_Books2-13_FINAL_REPORT.md：批次汇总与执行失败恢复说明。

## 证据与范围

- 证明子会话配置记录为 gpt-6-astra / xhigh；证据验证的是 CLI 配置，不是代理上游的独立模型认证。
- 运行清单中的原工程绝对路径只用于来源追溯；解压后请从本包的相对目录访问文件。
- 不包含 raw/ 会话日志、stage2_context/、认证文件、API 凭据、临时 runtime home 或私有推理记录。
- 本包是最终结果快照，不是可独立运行的完整工程。
- 文件内容与原结果字节一致，原结果未覆盖；PACKAGE_MANIFEST.json 列出逐文件 SHA-256。
