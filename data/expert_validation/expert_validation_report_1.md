# 专家验证文档：AI证明错误审核

---

## 前情提要

本研究探索大语言模型（Claude Opus 4.6）在经典数学定理证明任务中的表现。具体方法如下：

1. **独立证明**：使用 Claude Opus 4.6 对欧几里得《几何原本》全部 465 条命题进行了三轮独立证明（Run A、Run B、Run C）。每轮证明中，AI 仅依据公设、公理、定义及编号严格小于当前命题的已证定理进行推理，不接触人类（Heath）的证明原文。
2. **自动分类**：将每条 AI 证明与 Heath 的人类证明进行引用集对比，分为四类：
   - **P（Perfect match）**：引用集完全一致
   - **G（Granularity difference）**：证明路径相同，仅引用粒度不同
   - **D（Path difference）**：有效的替代证明路径
   - **E（Error）**：可正面识别的逻辑缺陷
3. **几何一致性检查**：对 D 类和 E 类证明中涉及几何构型的命题，进行空间配置一致性检查，检测步骤间的空间矛盾。判定为 PASS（无矛盾）、FAIL（存在空间矛盾）或 SKIP（非几何命题）。
4. **错误识别结果**：三轮实验共识别出 18 个 E 类标记（涉及 16 个不同命题）和 11 个几何检查 FAIL 标记（涉及 10 个不同命题），合计 29 个需验证的错误条目。

上述分类和几何检查均由 AI 自动完成。为确保错误判定的准确性，需要领域专家对这 29 个错误条目逐一审核验证。

## 验证方案

请专家对以下 29 个错误条目逐一审核。每个条目包含：

1. **AI 证明原文**：AI 在该轮实验中产出的完整逐步证明
2. **错误分析原文**：自动分类报告或几何检查报告中对该证明的分析

请专家对每个条目判断：

- **错误判定是否正确**：AI 分析所指出的错误是否真实存在？
- **补充意见**：是否有 AI 分析未注意到的额外问题，或对错误严重程度的评价？

---

## Part 1: 分类错误（E 类）

共 18 个条目。

### E-1: Proposition 3.26（Run A）

#### AI 证明原文（Run A）

## Proposition 3.26
**Statement:** In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

**Step 1.** Let ABC and DEF be equal circles, and let the angles BGC and EHF be equal angles at the centres G and H respectively. Also let the angles BAC and EDF be equal angles at the circumferences. We must prove that the circumference BKC is equal to the circumference ELF.

**Step 2.** First consider the case of equal central angles. Since the circles are equal, their radii are equal (D3.1), so GB = HE and GC = HF.

**Step 3.** In triangles BGC and EHF, we have GB = HE, GC = HF, and angle BGC = angle EHF (given). Therefore by the Side-Angle-Side criterion (1.4), triangle BGC is congruent to triangle EHF, and hence the base BC equals the base EF.

**Step 4.** Suppose the circumference BKC is not equal to the circumference ELF. Then one of them is greater. Let circumference BKC be greater than circumference ELF.

**Step 5.** Since circumference BKC is greater than circumference ELF, we can construct an angle BGM at centre G such that the circumference BMC is equal to the circumference ELF, where M is a point on circumference BKC between B and K, so that circumference BMC is less than circumference BKC.

**Step 6.** Then angle BGM stands on circumference BMC and angle EHF stands on circumference ELF. Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF. But angle EHF equals angle BGC by hypothesis, so angle BGM would equal angle BGC.

**Step 7.** But angle BGM is a part of angle BGC (since M lies on arc BKC beyond C from G's perspective, making the arc BMC smaller, thus angle BGM is less than angle BGC). Therefore a part would equal the whole, which is impossible (CN5).

**Step 8.** Therefore the circumference BKC is not unequal to the circumference ELF. Hence circumference BKC equals circumference ELF, which is the case for central angles.

**Step 9.** Now consider the case of equal angles at the circumferences: angle BAC = angle EDF. By Proposition 3.20, the angle at the centre is double the angle at the circumference when they stand on the same arc. Therefore angle BGC = 2 * angle BAC and angle EHF = 2 * angle EDF.

**Step 10.** Since angle BAC = angle EDF, we have angle BGC = angle EHF (CN1, as doubles of equal things are equal by CN2, taking each angle added to itself).

**Step 11.** But we proved in the first case that equal central angles in equal circles stand on equal circumferences. Therefore circumference BKC equals circumference ELF.

**Step 12.** Therefore in equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences. Q.E.D.

**USED:** 1.4, 3.20, CN1, CN2, CN5, D3.1
**Human refs (from References field):** 1.4, 3.24, D3.11
**Jaccard:** 0.125 — AI adds ['3.20', 'CN1', 'CN2', 'CN5', 'D3.1']; Human adds ['3.24', 'D3.11']

#### 分类报告原文（Run A）

### 3.26
**Category**: AI proof error
**Jaccard**: 0.125
**Analysis**: The AI proof's reductio argument for the central angles case (Steps 4-8) contains an unsupported assertion in Step 6: 'Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF.' This claim that equal arcs in equal circles yield equal central angles is precisely the content of Proposition 3.27, the converse of the theorem being proved (3.26). No citation is given, and no earlier proposition in Euclid establishes this result. The inference is therefore unsupported: the only justification would be the converse of the theorem under proof (circular) or the forward proposition 3.27. Heath's proof avoids this entirely by using a direct approach via segment similarity (D3.11) and III.24 rather than reductio. The audit record completes convincingly because the missing element is genuine support (not mere expansion of a supported step), making this a clear unsupported assertion under the hardened 1(b) standard.
**Audit Record**: CANDIDATE E — 3.26
  violated_claim : "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF" (Step 6)
  failure_mode   : unsupported_assertion
  missing_is     : support — there is no cited or invoked proposition that licenses the inference from equal arcs to equal angles. The result that would license it (3.27) is the converse of the theorem being proved and is a forward dependency.
  evidence       : Step 6 text: "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF." No citation is provided. The needed result is 3.27 (equal arcs -> equal angles in equal circles), which is the next proposition (forward).
  why_not_terse  : This is not mere brevity — the step invokes the converse of the very theorem being proved. No earlier proposition in Euclid establishes that equal arcs in equal circles yield equal central angles. The logical gap is circular/forward reasoning, not a skipped algebraic step.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-2: Proposition 7.33（Run A）

#### AI 证明原文（Run A）

## Proposition 7.33
**Statement:** Given as many numbers as we please, to find the least of those which have the same ratio with them.

**Step 1.** Let A, B, C be the given numbers (the argument applies to any quantity of numbers). We seek the least numbers having the same ratio as A, B, C.

**Step 2.** Find D, the greatest common measure of A, B, and C, by Proposition 7.3.

**Step 3.** Let D measure A the number of times there are units in E, let D measure B the number of times there are units in F, and let D measure C the number of times there are units in G. Then A equals D multiplied by E, B equals D multiplied by F, and C equals D multiplied by G, by Definition 7.15.

**Step 4.** Since D multiplying E produces A and D multiplying F produces B, by Proposition 7.17, E is to F as A is to B. Similarly, since D multiplying F produces B and D multiplying G produces C, by Proposition 7.17, F is to G as B is to C. Therefore E, F, G are in the same ratio as A, B, C.

**Step 5.** I say that E, F, G are the least numbers having these ratios. Suppose E, F, G have a common measure N greater than one. Then N measures E, so N multiplied by D measures D multiplied by E, that is, N multiplied by D measures A. Likewise N multiplied by D measures B and N multiplied by D measures C. Therefore N multiplied by D is a common measure of A, B, and C.

**Step 6.** But D is the greatest common measure of A, B, and C. So N multiplied by D is less than or equal to D. Since N is greater than one, N multiplied by D is greater than D, by Common Notion 5 (the whole is greater than the part, since D is a part of N times D). This is a contradiction.

**Step 7.** Therefore E, F, G have no common measure greater than one; that is, they are measured by a unit alone and hence are prime to one another (in the sense that no number greater than one measures all of them).

**Step 8.** Now suppose there exist numbers H, K, L less than E, F, G respectively, such that H is to K as A is to B and K is to L as B is to C. Since E is to F as A is to B and H is to K as A is to B, we have E is to F as H is to K, by Common Notion 1. Since E and F are prime to one another (from Step 7, any common measure of E and F would also measure G, giving a common measure of all three greater than one, which was shown impossible), by Proposition 7.21, E and F are the least numbers in the ratio E to F. By Proposition 7.20, E and F measure H and K respectively. But H is less than E, and a greater number cannot measure a lesser, which is absurd.

**Step 9.** Therefore no numbers less than E, F, G are in the same ratio as A, B, C, and E, F, G are the least numbers having the same ratio as A, B, C. Q.E.D.

**USED:** 7.17, 7.20, 7.21, 7.3, CN1, CN5, D7.15
**Human refs (from References field):** 7.16, 7.19, 7.21, 7.3, D7.15, D7.20
**Jaccard:** 0.300 — AI adds ['7.17', '7.20', 'CN1', 'CN5']; Human adds ['7.16', '7.19', 'D7.20']

#### 分类报告原文（Run A）

### 7.33
**Category**: AI proof error
**Jaccard**: 0.300
**Analysis**: The classification was decided at Q1(b). The AI's proof contains an invalid inference in Step 8: it claims that E and F are pairwise coprime because 'any common measure of E and F would also measure G,' but this is false in general. Group coprimality (gcd(E,F,G)=1, established in Steps 5-7) does not entail pairwise coprimality. For example, with A=6, B=10, C=15, D=gcd=1, we get E=6, F=10, G=15 where gcd(6,10)=2 but 2 does not divide 15, yet gcd(6,10,15)=1. The AI then applies Proposition 7.21 (numbers prime to one another are least in their ratio) to the pair E, F, but 7.21 requires pairwise coprimality which was not validly established. This breaks the proof chain: without pairwise coprimality, the AI cannot invoke 7.21 to get that E, F are least in ratio E:F, and therefore cannot use 7.20 to derive the contradiction. Heath avoids this issue entirely by using a direct contradiction argument through 7.19 (cross-multiplication proportion). The audit record completes convincingly: the AI infers Q (pairwise coprimality) from P (group coprimality) where P does not entail Q, satisfying the 'invalid inference' mode.
**Audit Record**: CANDIDATE E — 7.33
  violated_claim : "E and F are prime to one another (from Step 7, any common measure of E and F would also measure G, giving a common measure of all three greater than one, which was shown impossible)"
  failure_mode   : invalid_inference
  missing_is     : support
  evidence       : Step 8 claims pairwise coprimality of E, F from group coprimality of E, F, G. The parenthetical justification "any common measure of E and F would also measure G" is stated without proof and is false in general (e.g., gcd(6,10)=2 does not divide 15, yet gcd(6,10,15)=1). The subsequent invocation of 7.21 (numbers prime to one another are least in their ratio) requires pairwise coprimality, so the proof chain from Step 7 to Step 8's conclusion is broken.
  why_not_terse  : This is not compression of a valid argument but an incorrect logical inference. No valid argument exists from group coprimality to pairwise coprimality in general, so there is nothing being abbreviated — the claimed implication is simply false.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-3: Proposition 8.8（Run C）

#### AI 证明原文（Run C）

## Proposition 8.8
**Statement:** If between two numbers there fall numbers in continued proportion with them, then, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between the numbers which have the same ratio with the original numbers.

**Step 1.** Let A and B be two numbers, and let C1, C2, ..., Cn fall between them in continued proportion, so that A, C1, C2, ..., Cn, B are all in continued proportion (n+2 terms total). Let D and E be numbers such that A:B = D:E. We must show that there also fall n numbers in continued proportion between D and E.

**Step 2.** Since A, C1, C2, ..., Cn, B are in continued proportion, the ratio A:C1 = C1:C2 = ... = Cn:B. By 7.33, take F and G, the least numbers in the ratio A:C1.

**Step 3.** By 8.2, find the least numbers in continued proportion with n+2 terms in the ratio F:G. Call these F0, F1, F2, ..., Fn, F(n+1), so that F0:F1 = F1:F2 = ... = Fn:F(n+1) = F:G = A:C1.

**Step 4.** Since F0, F1, ..., F(n+1) are the least numbers in continued proportion in the ratio F:G, by 8.1 the extremes F0 and F(n+1) are prime to one another.

**Step 5.** Now A, C1, C2, ..., Cn, B are in continued proportion in the same ratio F:G, and F0, F1, ..., F(n+1) are the least such. Since A:C1 = F0:F1, and A:B is the ratio compounded of the n+1 equal ratios A:C1, while F0:F(n+1) is the ratio compounded of the n+1 equal ratios F0:F1, and these individual ratios are equal, it follows that A:B = F0:F(n+1). Similarly, the terms A, C1, ..., Cn, B are equimultiples of F0, F1, ..., F(n+1) respectively. By 7.20, since F0 and F(n+1) are the least numbers in the ratio A:B, they measure A and B the same number of times. Let A = m * F0 and B = m * F(n+1) for some number m, and correspondingly Ci = m * Fi for each i.

**Step 6.** Since A:B = D:E (given) and A:B = F0:F(n+1) (from Step 5), we have F0:F(n+1) = D:E by CN1. Since F0 and F(n+1) are prime to one another (Step 4), and F0, F(n+1) are the least numbers in the ratio D:E, by 7.20 F0 measures D and F(n+1) measures E the same number of times. Let D = p * F0 and E = p * F(n+1) for some number p.

**Step 7.** Define the numbers G1 = p * F1, G2 = p * F2, ..., Gn = p * Fn. We claim that D, G1, G2, ..., Gn, E are in continued proportion.

**Step 8.** For each consecutive pair in the sequence F0, F1, F2, ..., F(n+1), we have the ratio Fi:F(i+1) = F:G. By 7.17, since the number p multiplies both Fi and F(i+1), we have p * Fi : p * F(i+1) = Fi : F(i+1). Therefore D:G1 = p*F0:p*F1 = F0:F1 = F:G, and G1:G2 = p*F1:p*F2 = F1:F2 = F:G, and so on through Gn:E = p*Fn:p*F(n+1) = Fn:F(n+1) = F:G.

**Step 9.** Thus D, G1, G2, ..., Gn, E are all in continued proportion, and the count of numbers falling between D and E is n, which is the same as the count of numbers that fell between A and B.

**Step 10.** Therefore, if between two numbers there fall numbers in continued proportion with them, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between numbers which have the same ratio with the original numbers. Q.E.D.

**USED:** 7.17, 7.20, 7.33, 8.1, 8.2, CN1
**Human refs (from References field):** 7.14, 7.20, 7.21, 7.33, 8.3, D7.20
**Jaccard:** 0.200 — AI adds ['7.17', '8.1', '8.2', 'CN1']; Human adds ['7.14', '7.21', '8.3', 'D7.20']

#### 分类报告原文（Run C）

### 8.8
**Category**: AI proof error
**Jaccard**: 0.200
**Analysis**: The classification is decided at Q1(b) by an invalid inference in Step 4 of the AI proof. The AI constructs the least numbers in continued proportion via 8.2, then claims 'by 8.1 the extremes F0 and F(n+1) are prime to one another.' However, 8.1 states the converse: 'If numbers in continued proportion have extremes prime to one another, then they are the least of those in the same ratio.' The AI needs the direction 'if they are the least, then the extremes are prime,' which is 8.3, not 8.1. This is not mere brevity or compression -- the cited proposition literally states the opposite implication from what is needed. The converse of a true implication is not logically guaranteed, so citing 8.1 does not license the conclusion that the extremes are prime. The audit record completes convincingly: the missing element is genuine logical support (not an expansion), as no reading of 8.1 yields the needed direction.
**Audit Record**: CANDIDATE E — 8.8
  violated_claim : 'by 8.1 the extremes F0 and F(n+1) are prime to one another' (Step 4)
  failure_mode   : invalid_inference
  missing_is     : support — 8.1 states the converse of what is needed; the AI needs 8.3 (if least then prime), not 8.1 (if prime then least)
  evidence       : AI Step 4: 'Since F0, F1, ..., F(n+1) are the least numbers in continued proportion in the ratio F:G, by 8.1 the extremes F0 and F(n+1) are prime to one another.' 8.1 states: 'If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio with them.' The AI has least numbers and infers prime extremes, but 8.1 goes from prime extremes to least numbers.
  why_not_terse  : This is not mere brevity — the cited proposition (8.1) literally states the converse implication. No amount of compression makes 8.1 yield 'least implies prime extremes'; that is 8.3's content.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-4: Proposition 9.9（Run A）

#### AI 证明原文（Run A）

## Proposition 9.9
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest will also be square.

**Step 1.** Let there be as many numbers as we please, 1, A, B, C, D, ..., beginning from a unit and in continued proportion, and let A (the number after the unit) be square. We must show that all the remaining terms B, C, D, ... are also square.

**Step 2.** Since 1, A, B, C, D, ... are in continued proportion beginning from a unit, by Proposition 9.8, the third from the unit, namely B, is square, as are all terms which successively leave out one (that is, B, D, and every alternate term thereafter are square). [9.8]

**Step 3.** Now A is square by hypothesis, and B is square by Step 2. Consider any three consecutive terms in the sequence. We shall show that if the first of three consecutive terms is square, then the third is also square, using Proposition 8.22. [D7.18]

**Step 4.** Since 1, A, B are in continued proportion and A is square, consider the three consecutive terms A, B, C. These are in continued proportion (since the whole sequence is in continued proportion). The first term A is square (by hypothesis). Therefore by Proposition 8.22, since three numbers A, B, C are in continued proportion and the first A is square, the third C is also square. [8.22]

**Step 5.** Next consider the three consecutive terms B, C, D. These are in continued proportion. The first term B is square (established in Step 2 by 9.8). Therefore by Proposition 8.22, the third term D is also square. [8.22]

**Step 6.** Proceeding in this manner for each successive triple of consecutive terms: since C is square (Step 4), considering C, D, E in continued proportion, E is square by 8.22. Since D is square (Step 5), considering D, E, F in continued proportion, F is square by 8.22. [8.22]

**Step 7.** In general, for any term in the sequence beyond A, it appears as the third member of a triple of consecutive terms whose first member has already been shown to be square. By repeated application of Proposition 8.22, each such term is therefore square. [8.22]

**Step 8.** Therefore all terms in the sequence after the unit are square, which is what was to be proved.

**USED:** 8.22, 9.8, D7.18
**Human refs (from References field):** 8.22, 8.23, 9.3, 9.8
**Jaccard:** 0.400 — AI adds ['D7.18']; Human adds ['8.23', '9.3']

#### 分类报告原文（Run A）

### 9.9
**Category**: AI proof error
**Jaccard**: 0.400
**Analysis**: Proposition 9.9 as proved by Heath contains two cases: (1) if the number after the unit is square, all the rest are square, and (2) if the number after the unit is cube, all the rest are cube. Heath's proof explicitly addresses both cases, using 9.8 and 8.22 for the square case, and 9.8, 9.3, and 8.23 for the cube case. The AI proof only addresses the square case (Steps 1-8) and never mentions cubes at all. This is a genuine missing case under Q1(a): the cube case is entirely absent from the AI proof, not merely compressed or terse. The audit record completes convincingly since the omission is unambiguous — there is no general argument or reference in the AI proof that could cover the cube case.
**Audit Record**: CANDIDATE E — 9.9
  violated_claim : The cube case: 'if the number after the unit be cube, all the rest will also be cube'
  failure_mode   : missing_case
  missing_is     : support
  evidence       : Heath's proof explicitly addresses two cases: 'let A, the number after the unit, be square' and 'Next, let A be cube'. The AI proof text only addresses the square case (Steps 1-8) and never mentions cubes. The heath_only citations 8.23 and 9.3 are precisely the propositions used in the cube case.
  why_not_terse  : This is not brevity — the entire second case (cube) is absent from the AI proof. There is no general argument or reference that covers the cube case.

#### 专家验证

- 错误判定是否正确： 不正确。
- 补充意见：AI的证明没有问题，题面说的是平方数的情况，AI也证明了平方数的情况，但heath的证明里多了立方数的情况，导致判定错误。

---

### E-5: Proposition 9.10（Run A）

#### AI 证明原文（Run A）

## Proposition 9.10
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be not square, neither will any other be square except the third from the unit and all those which leave out one.

**Step 1.** Let there be as many numbers as we please, 1, A, B, C, D, E, F, ..., beginning from a unit and in continued proportion, and let A (the number after the unit) not be square. We must show that no number in the sequence is square except B (the third from the unit) and every alternate one thereafter (D, F, ..., i.e., those which leave out one).

**Step 2.** By 9.8, the third from the unit, B, is square, as are all those which leave out one (D, F, and so on). So these terms are indeed square. It remains to show that every other term — namely A, C, E, and so on (the 2nd, 4th, 6th, ... from the unit) — is not square.

**Step 3.** A is not square by hypothesis. We now show C (the 4th from the unit) is not square. Suppose, for the sake of contradiction, that C is square. Now B is square by Step 2. Consider the three consecutive terms A, B, C in continued proportion. Since B and C are both square, the ratio B : C is that of a square number to a square number. But A : B = B : C (continued proportion), so A : B is also the ratio of a square to a square. Since B is square and A has to B the ratio of a square number to a square number, by 8.25, A is also square. This contradicts the hypothesis that A is not square. Therefore C is not square.

**Step 4.** We now show E (the 6th from the unit) is not square. Suppose E is square. Now D is square by Step 2 (9.8). Consider the three consecutive terms C, D, E in continued proportion. Since D and E are both square, D : E is the ratio of a square to a square. But C : D = D : E (continued proportion), so C : D is also the ratio of a square to a square. Since D is square and C has to D the ratio of a square to a square, by 8.25, C is also square. This contradicts what was proved in Step 3. Therefore E is not square.

**Step 5.** The same argument applies to every subsequent even-positioned term. For any term in an even position from the unit — say the (2k)th term — suppose it were square. The (2k - 1)th term is square by 9.8 (it occupies an odd position, i.e., it leaves out one). The (2k - 2)th term, the (2k - 1)th term, and the (2k)th term are three consecutive terms in continued proportion. Since the (2k - 1)th and (2k)th are both assumed square, their ratio is square to square. By the continued proportion, the ratio of the (2k - 2)th term to the (2k - 1)th term is also square to square. By 8.25, since the (2k - 1)th term is square, the (2k - 2)th term is also square. But the (2k - 2)th term occupies an even position and was already shown not to be square by the preceding case of this same argument (with the base case being A at position 2, which is not square by hypothesis). This is a contradiction. Therefore the (2k)th term is not square.

**Step 6.** Hence no term in the sequence is square except the third from the unit and all those which leave out one. Q.E.D.

**USED:** 8.25, 9.8
**Human refs (from References field):** 8.25, 8.26, 9.6, 9.8
**Jaccard:** 0.500 — Human adds ['8.26', '9.6']

#### 分类报告原文（Run A）

### 9.10
**Category**: AI proof error
**Jaccard**: 0.500
**Analysis**: The AI proof of 9.10 cites proposition 8.25 to conclude that a number is square (Steps 3, 4, and 5), but 8.25 states 'If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube' -- it concerns cubes, not squares. The correct proposition for the square case is 8.24 ('If two numbers have to one another the ratio which a square number has to a square number, and the first be square, the second will also be square'). Since the AI explicitly cites 8.25 as its warrant and 8.25 does not entail any conclusion about square numbers, this is an invalid inference under Q1(b). The audit record completes convincingly: the missing element is support (not mere expansion), the cited proposition genuinely does not entail the conclusion, and this is not a matter of terseness or compression but of citing the wrong proposition entirely. Heath correctly uses 8.25 only in the cube case and uses 8.26 (converse) for the square case.
**Audit Record**: CANDIDATE E -- 9.10
  violated_claim : "by 8.25, A is also square" (Step 3, and repeated in Steps 4-5)
  failure_mode   : invalid_inference
  missing_is     : support -- 8.25 is about cubes; the AI needs 8.24 (squares) but cites 8.25 (cubes)
  evidence       : AI Step 3: "Since B is square and A has to B the ratio of a square number to a square number, by 8.25, A is also square." Proposition 8.25: "If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube." The AI applies 8.25 to a square-ratio context where it does not apply.
  why_not_terse  : The AI explicitly names 8.25 as the warrant for its conclusion about squares. 8.25 concerns cubes exclusively and cannot justify any conclusion about square numbers. The correct warrant is 8.24, which the AI does not cite.

#### 专家验证

- 错误判定是否正确：不正确。
- 补充意见：理由同E-4。

---

### E-6: Proposition 9.10（Run B）

#### AI 证明原文（Run B）

## Proposition 9.10
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be not square, neither will any other be square except the third from the unit and all those which leave out one.

**Step 1.** Let there be as many numbers as we please, 1, A, A^2, A^3, A^4, ..., beginning from a unit and in continued proportion, and let A (the number after the unit) not be square. We must show that no term other than the third from the unit and those which leave out one (i.e., A^2, A^4, A^6, ...) is square.

**Step 2.** By Proposition 9.8, the third from the unit, namely A^2, is square, as are all those which successively leave out one, namely A^4, A^6, and so on. These are precisely the even powers of A in the continued proportion.

**Step 3.** We claim that no odd power of A (that is, A itself, A^3, A^5, A^7, ...) is square. First, A is not square by hypothesis.

**Step 4.** Suppose for the sake of contradiction that some odd power A^k, with k >= 3 and k odd, is a square number.

**Step 5.** Since k is odd, k - 1 is even and k - 1 >= 2. Therefore A^(k-1) is an even power of A, and by Proposition 9.8, A^(k-1) is a square number.

**Step 6.** Now, A^k = A^(k-1) multiplied by A. Since A^k is square by our assumption, two numbers A^(k-1) and A have been multiplied together to produce a square number.

**Step 7.** By Proposition 9.2, since A^(k-1) and A multiply to make a square number, A^(k-1) and A are similar plane numbers.

**Step 8.** Since A^(k-1) is square, by Definition D7.18, A^(k-1) is equal multiplied by equal; that is, A^(k-1) = s * s for some number s, so A^(k-1) is a plane number with two equal sides s and s.

**Step 9.** Since A^(k-1) and A are similar plane numbers, by Definition D7.21 their sides are proportional. Let A = p * q be the representation of A as a plane number with sides p and q. Then the sides of A^(k-1) are proportional to the sides of A, giving us s : p = s : q.

**Step 10.** From the proportion s : p = s : q, since the same number s has the same ratio to both p and q, it follows that p = q.

**Step 11.** Since A = p * q and p = q, we have A = p * p, so A is a square number by Definition D7.18. But this contradicts the hypothesis that A is not square.

**Step 12.** Therefore our assumption in Step 4 is false, and no odd power of A is square. Combined with Step 2, the only square terms in the continued proportion from the unit are A^2, A^4, A^6, and so on -- that is, the third from the unit and all those which leave out one. This is what was to be proved.

**USED:** 9.2, 9.8, D7.18, D7.21
**Human refs (from References field):** 8.25, 8.26, 9.6, 9.8
**Jaccard:** 0.143 — AI adds ['9.2', 'D7.18', 'D7.21']; Human adds ['8.25', '8.26', '9.6']

#### 分类报告原文（Run B）

### 9.10
**Category**: AI proof error
**Jaccard**: 0.143
**Analysis**: Proposition 9.10 is a compound proposition with two independent parts: (1) if the number after the unit is not square, then no other term besides the third from the unit and those leaving out one is square; and (2) if the number after the unit is not cube, then no other term besides the fourth from the unit and those leaving out two is cube. Heath's proof addresses both parts fully: the square case via contradiction using 9.8 and 8.26 converse, and the cube case via contradiction using 9.8, 8.25, and 9.6. The AI proof (Steps 1-12) addresses only the square part, proving that no odd power of A is square, and concludes 'This is what was to be proved' without any mention of cubes whatsoever. The cube case is an entirely separate assertion with its own hypothesis and conclusion, not a mere expansion or restatement of the square case. This constitutes a genuinely missing case under Q1(a), warranting classification E.
**Audit Record**: CANDIDATE E — 9.10
  violated_claim : The second part of the proposition — 'if the number after the unit be not cube, neither will any other be cube except the fourth from the unit and all those which leave out two' — is entirely unaddressed by the AI proof.
  failure_mode   : missing_case
  missing_is     : support   # The cube case is an independent part of the proposition, not an expansion of the square case.
  evidence       : The AI proof text covers Steps 1-12 dealing only with squares (odd vs even powers of A) and concludes 'This is what was to be proved' without any mention of cubes. Heath's proof has a second section beginning 'Next, let A not be cube' that proves the cube case using 9.8, 8.25, and 9.6.
  why_not_terse  : This is not a brevity issue — the cube case is an entirely separate assertion of the proposition with its own hypothesis ('let A not be cube') and its own conclusion ('neither will any other be cube except the fourth from the unit'), and the AI proof contains zero text addressing it.

#### 专家验证

- 错误判定是否正确：不正确。
- 补充意见：理由同E-4。

---

### E-7: Proposition 10.12（Run A）

#### AI 证明原文（Run A）

## Proposition 10.12
**Statement:** Magnitudes commensurable with the same magnitude are commensurable with one another also.

**Step 1.** Let A and B each be commensurable with a magnitude C. We are to prove that A and B are commensurable with one another.

**Step 2.** Since A is commensurable with C, by Proposition 10.5, A has to C the ratio which a number has to a number. Let A:C :: m:n, where m and n are numbers.

**Step 3.** Since B is commensurable with C, by Proposition 10.5, B has to C the ratio which a number has to a number. Let B:C :: p:q, where p and q are numbers.

**Step 4.** Since p multiplies the two numbers m and n, by Proposition 7.17, the products pm and pn have to one another the ratio which m has to n. That is, pm:pn :: m:n.

**Step 5.** But A:C :: m:n (Step 2) and m:n :: pm:pn (Step 4). Therefore, by Proposition 5.11, A:C :: pm:pn.

**Step 6.** Since n multiplies the two numbers p and q, by Proposition 7.17, the products np and nq have to one another the ratio which p has to q. That is, np:nq :: p:q.

**Step 7.** But B:C :: p:q (Step 3) and p:q :: np:nq (Step 6). Therefore, by Proposition 5.11, B:C :: np:nq. By the definition of inverse ratio (D5.13), C:B :: nq:np.

**Step 8.** We now have A:C :: pm:np and C:B :: np:nq, where pm, np, and nq are all numbers. By Proposition 5.22 (ex aequali), A:B :: pm:nq.

**Step 9.** Since m, n, p, and q are numbers, pm and nq are also numbers (being products of numbers). Therefore A has to B the ratio which a number has to a number.

**Step 10.** Since A has to B the ratio which a number has to a number, by Proposition 10.6, A is commensurable with B.

**Step 11.** Therefore, magnitudes commensurable with the same magnitude are commensurable with one another also. Q.E.D.

**USED:** 10.5, 10.6, 5.11, 5.22, 7.17, D10.1.1, D5.13
**Human refs (from References field):** 10.5, 10.6, 5.11, 5.22, 8.4
**Jaccard:** 0.500 — AI adds ['7.17', 'D10.1.1', 'D5.13']; Human adds ['8.4']

#### 分类报告原文（Run A）

### 10.12
**Category**: AI proof error
**Jaccard**: 0.500
**Analysis**: Q1(b) decides: the AI proof commits an invalid inference when applying 5.22 (ex aequali) in Step 8. The AI establishes A:C :: pm:np and C:B :: nq:np, then claims that 5.22 yields A:B :: pm:nq. However, 5.22 requires matching middle terms -- the second term of the first ratio must equal the first term of the second ratio. Here the second term of A:C is np and the first term of C:B is nq; since p and q are generally distinct, np != nq and 5.22 is inapplicable. Moreover, the claimed result A:B = pm:nq is arithmetically incorrect (the correct ratio would be mq:np). The AI's strategy of using 7.17 to multiply numerators and denominators fails to produce the common middle term that Heath achieves via 8.4. This is not a matter of terseness or compression -- the cited proposition genuinely does not entail the claimed conclusion from the given premises.
**Audit Record**: CANDIDATE E -- 10.12
  violated_claim : A:B :: pm:nq (Step 8)
  failure_mode   : invalid_inference
  missing_is     : support -- 5.22 does not entail A:B :: pm:nq from A:C :: pm:np and C:B :: nq:np because the middle terms (np vs nq) do not match
  evidence       : Step 8: 'We now have A:C :: pm:np and C:B :: nq:np... By Proposition 5.22 (ex aequali), A:B :: pm:nq.' Proposition 5.22 requires A:C :: pm:X and C:B :: X:nq with matching middle term X. Here the middle terms are np (from A:C) and nq (from C:B), which are unequal when p != q.
  why_not_terse  : This is not brevity -- the ratios as stated have non-matching middle terms (np vs nq), making 5.22 structurally inapplicable. The resulting ratio pm:nq is arithmetically incorrect (A/B = (m/n)*(q/p) = mq/np, not pm/nq).

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-8: Proposition 10.34（Run C）

#### AI 证明原文（Run C）

## Proposition 10.34
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial but the rectangle contained by them rational.

**Step 1.** By 10.27, find two medial straight lines A and B that are commensurable in square only and such that the rectangle contained by A and B is rational.

**Step 2.** Since A is a medial straight line, the square on A is a medial area (by D10.1.4 and 10.21). Similarly, since B is a medial straight line, the square on B is a medial area.

**Step 3.** Since A and B are commensurable in square only, the squares on A and B are commensurable areas (by D10.1.2). Since the square on A is commensurable with the square on B, the sum of the squares on A and B is commensurable with the square on A (by 10.15).

**Step 4.** Since the square on A is medial and the sum of the squares on A and B is commensurable with the square on A (Step 3), the sum of the squares on A and B is medial (by 10.23, since a magnitude commensurable with a medial magnitude is medial).

**Step 5.** The rectangle contained by A and B is rational, by the construction of Step 1 (from 10.27).

**Step 6.** Since A and B are commensurable in square only, they are incommensurable in length but their squares are commensurable. They are therefore two straight lines incommensurable in square (in the sense that they are not commensurable in length, only in square -- D10.1.2), which make the sum of the squares on them medial (Step 4) but the rectangle contained by them rational (Step 5).

**Step 7.** Therefore two straight lines have been found, incommensurable in square, which make the sum of the squares on them medial but the rectangle contained by them rational. Q.E.F.

**USED:** 10.15, 10.21, 10.23, 10.27, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.47, 10.11, 10.18, 10.31, 10.6, 3.31, 6.28
**Jaccard:** 0.000 — AI adds ['10.15', '10.21', '10.23', '10.27', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['1.47', '10.11', '10.18', '10.31', '10.6', '3.31', '6.28']

#### 分类报告原文（Run C）

### 10.34
**Category**: AI proof error
**Jaccard**: 0.000
**Analysis**: Q1(b) decided the classification. The AI proof uses 10.27 to obtain two medial straight lines A, B that are 'commensurable in square only,' meaning by D10.1.2 their squares are commensurable (share a common measure) but the lines are incommensurable in length. However, the proposition requires finding lines 'incommensurable in square,' which by D10.1.2 means their squares cannot have any common measure. In Step 6, the AI explicitly claims these commensurable-in-square-only lines are 'incommensurable in square,' adding a parenthetical that redefines the term to mean 'not commensurable in length, only in square.' This directly contradicts D10.1.2's definition. The AI infers Q (lines are incommensurable in square) from P (lines are commensurable in square only) where P entails the negation of Q. Heath's proof avoids this by applying a semicircle construction (using 6.28, 10.18, 3.31, 1.47) to the medial lines from 10.31 to produce genuinely incommensurable-in-square lines AD and DB. The AI's fundamental construction fails to produce the required objects.
**Audit Record**: CANDIDATE E — 10.34
  violated_claim : "They are therefore two straight lines incommensurable in square" (Step 6)
  failure_mode   : invalid_inference
  missing_is     : support — The AI claims A, B are "incommensurable in square" but A, B from 10.27 are commensurable in square only (their squares are commensurable), which by D10.1.2 means they are commensurable in square, not incommensurable in square. The conclusion directly contradicts the construction.
  evidence       : Step 6: "Since A and B are commensurable in square only, they are incommensurable in length but their squares are commensurable. They are therefore two straight lines incommensurable in square (in the sense that they are not commensurable in length, only in square -- D10.1.2)" — D10.1.2 defines incommensurable in square as "the squares on them cannot possibly have any area as a common measure," which is the opposite of what the AI has.
  why_not_terse  : This is not brevity or compression — the AI explicitly derives a conclusion ("incommensurable in square") that contradicts its own premise ("commensurable in square only"). The proposition's requirement (incommensurable in square = squares have no common measure) is the negation of what the AI's construction produces (commensurable in square = squares do have a common measure).

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-9: Proposition 10.44（Run B）

#### AI 证明原文（Run B）

## Proposition 10.44
**Statement:** A second bimedial straight line is divided at one point only.

**Step 1.** Let AB be a second bimedial straight line, and let it be divided at C into its terms, so that AC and CB are medial straight lines commensurable in square only and containing a medial rectangle, with AC greater than CB [by 10.38]. We must show that AB is not divided at any other point into terms satisfying these conditions.

**Step 2.** Suppose, for contradiction, that AB is also divided at D into terms satisfying the definition of a second bimedial, so that AD and DB are medial straight lines commensurable in square only and containing a medial rectangle. Without loss of generality, assume AC is greater than DB (since AB is the same line, the greater segment at one division cannot equal the greater at the other unless the divisions coincide).

**Step 3.** Since AB is a second bimedial divided at C, the sum of the squares on AC and CB is medial [by 10.15 and 10.23, since each square is medial by 10.21, and the sum of medial areas commensurable with each other is medial by 10.15 and 10.24]. Similarly, since AB is divided at D as a second bimedial, the sum of the squares on AD and DB is medial.

**Step 4.** Now, by 2.4, the square on AB equals the sum of the squares on AC and CB plus twice the rectangle AC, CB. Likewise, the square on AB equals the sum of the squares on AD and DB plus twice the rectangle AD, DB.

**Step 5.** Therefore, the sum of the squares on AC, CB plus twice the rectangle AC, CB equals the sum of the squares on AD, DB plus twice the rectangle AD, DB [by CN1].

**Step 6.** Since both the rectangle AC, CB and the rectangle AD, DB are medial (as each division yields a medial rectangle by the hypothesis of second bimedial), and twice a medial area is medial [by 10.23], twice the rectangle AC, CB is medial and twice the rectangle AD, DB is medial.

**Step 7.** Also, the sum of the squares on AC, CB is medial (as shown in Step 3), and the sum of the squares on AD, DB is medial.

**Step 8.** From Step 5, we obtain: (sq(AC) + sq(CB)) - (sq(AD) + sq(DB)) = 2*rect(AD,DB) - 2*rect(AC,CB) [by CN2, CN3].

**Step 9.** Now suppose the two divisions do not coincide. We shall show this leads to a contradiction. Consider the line segments. Since AC > DB (Step 2), and AC + CB = AD + DB = AB, we can compare the segments. Set AC = AD + e for some appropriate comparison. By the algebraic identity from 2.4 applied to both divisions, the difference of the sums of squares equals the difference of the doubled rectangles.

**Step 10.** The left side, (sq(AC) + sq(CB)) - (sq(AD) + sq(DB)), is the difference of two medial areas. The right side, 2*rect(AD,DB) - 2*rect(AC,CB), is likewise the difference of two medial areas.

**Step 11.** Now consider whether these differences are rational or medial. By 10.26, a medial area does not exceed a medial area by a rational area. So the difference on each side, if nonzero, must be irrational.

**Step 12.** We examine the sums of squares more carefully. Since AC and CB are commensurable in square only, the squares on AC and CB are commensurable [by D10.1.2 and 10.15]. Their sum is therefore commensurable with each, hence medial [by 10.23]. Similarly, the squares on AD and DB are commensurable, and their sum is medial.

**Step 13.** Now, by 2.7, the square on AB equals the sum of the squares on AC, CB plus twice the rectangle AC, CB, and also equals the sum of the squares on AD, DB plus twice the rectangle AD, DB. Since the rectangle contained by each pair of terms is medial, twice the rectangle is medial. Since the sum of the squares on each pair is medial, and these medial areas (sum of squares and twice rectangle) are incommensurable with each other for a second bimedial (this follows from the definition in 10.38, where the rectangle is medial and incommensurable with the sum of squares), the square on AB is the side of the sum of two medial areas.

**Step 14.** Suppose C and D are different points. By 2.5, the rectangle AC, CB differs from the rectangle AD, DB (since different divisions of the same line produce different rectangles unless the divisions are symmetric, but here the terms must satisfy specific commensurability conditions). Specifically, rect(AC,CB) = rect(AD,DB) would require AC*CB = AD*DB.

**Step 15.** If AC*CB = AD*DB, then since also sq(AC) + sq(CB) = sq(AD) + sq(DB) (from Step 5, both sides would be equal), we would have AC + CB = AD + DB (both equal AB) and AC*CB = AD*DB. By 2.5 and 2.6, this means {AC, CB} = {AD, DB} as a set, hence the division points coincide, contradicting our assumption.

**Step 16.** If AC*CB is not equal to AD*DB, then from Step 8, the difference (sq(AC) + sq(CB)) - (sq(AD) + sq(DB)) is nonzero and equals 2*rect(AD,DB) - 2*rect(AC,CB), which is also nonzero. The left side is the difference of two medial areas. The right side is also the difference of two medial areas.

**Step 17.** Now, the sum of squares on AC, CB is medial, and the sum of squares on AD, DB is medial. If their difference were rational, this would contradict 10.26 (a medial area does not exceed a medial area by a rational area). So their difference is irrational.

**Step 18.** Similarly, twice rect(AC,CB) is medial and twice rect(AD,DB) is medial. If their difference were rational, this would again contradict 10.26. So their difference is also irrational.

**Step 19.** But from Step 8, these two differences are equal. Now consider: the sum of squares on each pair of terms is medial and commensurable with each square in the pair. The twice-rectangle for each pair is also medial. For the second bimedial, the sum of squares and the twice-rectangle are incommensurable (from 10.38). This means for each division, sq(AB) is decomposed into two incommensurable medial parts.

**Step 20.** If the divisions differ, we obtain from Step 8 that a medial area exceeds a medial area by the same amount as another medial area exceeds another medial area. But examining the commensurability relations: the sums of squares from the two divisions are each medial, and the doubled rectangles from the two divisions are each medial. The difference of the sums of squares equals the difference of the doubled rectangles. Since for the division at C, the sum of squares on AC, CB is incommensurable with twice rect(AC,CB), and for the division at D, the sum of squares on AD, DB is incommensurable with twice rect(AD,DB), these decompositions of sq(AB) into incommensurable medial parts must be the same decomposition (a medial area has a unique decomposition into two incommensurable medial parts that sum to it, by the reasoning of 10.42 applied to medial areas and 10.26).

**Step 21.** Therefore the sum of the squares on AC, CB equals the sum of the squares on AD, DB, and twice rect(AC,CB) equals twice rect(AD,DB), giving rect(AC,CB) = rect(AD,DB).

**Step 22.** Since AC + CB = AD + DB = AB and AC * CB = AD * DB, by 2.5 and 2.6 the pairs {AC, CB} and {AD, DB} are the same pair of segments. Therefore C and D are the same point.

**Step 23.** Hence a second bimedial straight line is divided at one point only. Q.E.D.

**USED:** 10.15, 10.21, 10.23, 10.24, 10.26, 10.38, 2.4, 2.5, 2.6, 2.7, CN1, CN2, CN3, D10.1.2
**Human refs (from References field):** 10.11, 10.13, 10.22, 10.36, 10.38, 10.6, 2.4, 6.1
**Jaccard:** 0.100 — AI adds ['10.15', '10.21', '10.23', '10.24', '10.26', '2.5', '2.6', '2.7', 'CN1', 'CN2', 'CN3', 'D10.1.2']; Human adds ['10.11', '10.13', '10.22', '10.36', '10.6', '6.1']

#### 分类报告原文（Run B）

### 10.44
**Category**: AI proof error
**Jaccard**: 0.100
**Analysis**: Q1(b) decided the classification. The AI proof's Step 20 claims that decompositions of sq(AB) into two incommensurable medial parts must be unique, citing 'the reasoning of 10.42 applied to medial areas and 10.26.' However, 10.42's proof technique exploits the rational/medial dichotomy: in 10.42, the sums of squares are rational while the doubled rectangles are medial, so their difference forces a rational quantity to equal a medial difference, contradicting 10.26. In 10.44, both the sums of squares and the doubled rectangles are medial, so both sides of the difference equation are medial-minus-medial, and no rational/medial contradiction arises. The AI's analogy to 10.42 is structurally invalid. Heath's proof addresses this difficulty by using the application-of-areas technique to convert the problem into one about binomial lines divided at different points, reducing to 10.42 for lines (not areas). The AI skips this essential conversion step, making the core inference in Step 20 invalid rather than merely terse.
**Audit Record**: CANDIDATE E — 10.44
  violated_claim : 'these decompositions of sq(AB) into incommensurable medial parts must be the same decomposition (a medial area has a unique decomposition into two incommensurable medial parts that sum to it, by the reasoning of 10.42 applied to medial areas and 10.26)' (Step 20)
  failure_mode   : invalid_inference
  missing_is     : support — the unique decomposition of medial area sums is not established by 10.42 or 10.26; it is the very content of what 10.44 proves
  evidence       : Step 20 cites 'the reasoning of 10.42 applied to medial areas and 10.26'. 10.42 proves binomial line uniqueness by exploiting the rational/medial dichotomy: sq-sums are rational, doubled-rectangles are medial, so their difference is rational=medial, contradicting 10.26. In 10.44 both sq-sums and doubled-rectangles are medial, so both sides are medial-minus-medial and no rational/medial contradiction arises.
  why_not_terse  : This is not mere brevity; 10.42's proof mechanism structurally depends on the rational/medial dichotomy that does not exist in 10.44's all-medial setting, so 'the reasoning of 10.42 applied to medial areas' is an invalid analogy, not a compressed valid argument.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-10: Proposition 10.47（Run B）

#### AI 证明原文（Run B）

## Proposition 10.47
**Statement:** The side of the sum of two medial areas is divided at one point only.

**Step 1.** Let AB be the side of the sum of two medial areas, and let it be divided at C, so that AC and CB are straight lines incommensurable in square which make the sum of the squares on them medial, the rectangle contained by them medial, and the sum of the squares on AC, CB incommensurable with the rectangle AC by CB [10.41].

**Step 2.** Suppose, for the sake of contradiction, that AB is also divided at D such that AD and DB satisfy the same conditions: AD and DB are incommensurable in square, the sum of the squares on AD and DB is medial, the rectangle AD by DB is medial, and the sum of the squares on AD, DB is incommensurable with the rectangle AD by DB.

**Step 3.** Since AB is divided at C, the square on AB equals the sum of the squares on AC, CB together with twice the rectangle AC by CB [2.4]. Likewise, since AB is divided at D, the square on AB equals the sum of the squares on AD, DB together with twice the rectangle AD by DB [2.4].

**Step 4.** Therefore, the squares on AC, CB together with twice the rectangle AC by CB equal the squares on AD, DB together with twice the rectangle AD by DB [CN1]. Rearranging, the squares on AC, CB minus the squares on AD, DB equal twice the rectangle AD by DB minus twice the rectangle AC by CB [CN2, CN3].

**Step 5.** Now, the sum of the squares on AC, CB is medial, and the sum of the squares on AD, DB is medial. Also, twice the rectangle AC by CB is medial, and twice the rectangle AD by DB is medial (since if a rectangle is medial, its double is also medial, as a rational multiple of a medial area is medial [10.23, 10.6]).

**Step 6.** Suppose the sum of the squares on AC, CB is not equal to the sum of the squares on AD, DB. Then their difference, say the squares on AC, CB exceed the squares on AD, DB, would equal twice the rectangle AD by DB minus twice the rectangle AC by CB. The left side is the excess of one medial area over another medial area, and the right side is likewise the excess of one medial area over another medial area.

**Step 7.** But the sum of the squares on AC, CB is incommensurable with the rectangle AC by CB, and the sum of the squares on AD, DB is incommensurable with the rectangle AD by DB. From the equality in Step 4, if we denote S1 = squares on AC, CB; R1 = 2*rect(AC,CB); S2 = squares on AD, DB; R2 = 2*rect(AD,DB), then S1 + R1 = S2 + R2, so S1 - S2 = R2 - R1.

**Step 8.** If S1 is not equal to S2, then S1 - S2 is the difference of two medial areas, and R2 - R1 is also the difference of two medial areas, and these differences are equal.

**Step 9.** Now consider: S1 is incommensurable with R1 (by hypothesis on the division at C), and S2 is incommensurable with R2 (by hypothesis on the division at D). Since S1 + R1 = S2 + R2 (both equal the square on AB), we have that S1 and R1 are the same magnitudes as S2 and R2. We prove this as follows.

**Step 10.** Suppose S1 is not equal to S2. Without loss of generality, assume S1 is greater than S2. Then S1 - S2 = R2 - R1, so R2 is greater than R1. Now S1 - S2 is the excess of one medial area over another. Also R2 - R1 is the excess of one medial over another, and these are equal.

**Step 11.** Since S1 + R1 = S2 + R2, and S1 is incommensurable with R1, consider these as partitions of the same magnitude (the square on AB) into two parts. The square on AB is partitioned as S1 + R1 and also as S2 + R2, where in each partition the two summands are incommensurable and both medial.

**Step 12.** From the equality S1 - S2 = R2 - R1, we get that S1 - S2 is some area, say E. Then S1 = S2 + E and R2 = R1 + E. Since S1 is medial and S2 is medial, and a medial area does not exceed a medial area by a rational area [10.26], the area E (if nonzero) is irrational.

**Step 13.** Similarly, since R2 is medial and R1 is medial, the same area E is the excess of medial R2 over medial R1, which again by 10.26 cannot be rational.

**Step 14.** Now, S1 is incommensurable with R1. Since R2 = R1 + E and S1 = S2 + E, substituting into S1 + R1 = S2 + R2 is consistent. But we need to derive a contradiction from S1 being incommensurable with R1 and S2 being incommensurable with R2.

**Step 15.** Consider: S1 = S2 + E and R2 = R1 + E. So S1 + R1 = S2 + E + R1 = S2 + R2 (since R2 = R1 + E), which is consistent. Now S1 is incommensurable with R1, meaning (S2 + E) is incommensurable with R1. Also S2 is incommensurable with R2 = R1 + E.

**Step 16.** Apply the same argument used in Proposition 10.45 and 10.46: Since S1 + R1 = S2 + R2, and S1 is not equal to S2, let us apply 2.5 and 2.6. Set out a straight line, and let it be divided at two points corresponding to C and D. Using the identities from 2.5 and 2.6, the rectangle AC by CB and the rectangle AD by DB are related to the position of the division points.

**Step 17.** More precisely, by 2.5, since AB is divided into equal parts at some midpoint, say M, and into unequal parts at C, then the rectangle AC by CB together with the square on MC equals the square on MB. Likewise the rectangle AD by DB together with the square on MD equals the square on MB [2.5].

**Step 18.** Therefore, the rectangle AC by CB together with the square on MC equals the rectangle AD by DB together with the square on MD [CN1]. Hence the rectangle AD by DB minus the rectangle AC by CB equals the square on MC minus the square on MD (or vice versa) [CN2, CN3].

**Step 19.** Since the rectangle AC by CB is medial and the rectangle AD by DB is medial, their difference is the excess of one medial area over another. But the square on MC minus the square on MD (the difference of two squares on rational-in-relation-to-each-other segments, since M is the midpoint) is rational, because MC and MD are expressible in terms of the segments and their differences are commensurable.

**Step 20.** Specifically, M is the midpoint of AB, so AM = MB. Then MC = AM - AC (or AC - AM), and MD = AM - AD (or AD - AM). The square on MC minus the square on MD is a difference of squares on segments that are commensurable (both being differences of commensurable parts of the same line). This difference of squares is rational.

**Step 21.** But by 10.26, a medial area does not exceed a medial area by a rational area. Yet we have shown that the difference of the two medial rectangles (rect AD by DB minus rect AC by CB) equals a rational area (sq on MC minus sq on MD). This is a contradiction unless the rectangles are equal, i.e., rect AC by CB = rect AD by DB.

**Step 22.** Therefore the rectangle AC by CB equals the rectangle AD by DB. It follows from the equality in Step 4 that the sum of the squares on AC, CB equals the sum of the squares on AD, DB.

**Step 23.** Since the rectangle AC by CB equals the rectangle AD by DB, by 2.5, the square on MC equals the square on MD (where M is the midpoint of AB), so MC = MD [CN1].

**Step 24.** Since M is the midpoint of AB, and MC = MD, and both C and D lie on AB, then C and D are equidistant from the midpoint M. This means either C = D, or C and D are symmetric about M.

**Step 25.** If C and D are symmetric about M (and C is not equal to D), then AD = CB and DB = AC (the segments are simply reversed). But then the sum of the squares on AD, DB equals the sum of the squares on CB, AC, which is the same set of summands, and the rectangle AD by DB equals the rectangle CB by AC, which is the same rectangle. In this case, the division produces the same pair of segments, merely listed in the opposite order. Since the line AB has the same two segments regardless of which end we measure from, this is the same division point (the line is divided at one point into these two terms, just named from different ends).

**Step 26.** Therefore, in either case, the side of the sum of two medial areas is divided at one point only. Q.E.D.

**USED:** 10.23, 10.26, 10.41, 2.4, 2.5, CN1, CN2, CN3
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.42, 2.4, 6.1
**Jaccard:** 0.077 — AI adds ['10.23', '10.26', '10.41', '2.5', 'CN1', 'CN2', 'CN3']; Human adds ['10.11', '10.22', '10.36', '10.42', '6.1']

#### 分类报告原文（Run B）

### 10.47
**Category**: AI proof error
**Jaccard**: 0.077
**Analysis**: Q1 decides the classification. The AI proof attempts a midpoint-based argument using II.5 and 10.26 instead of Heath's auxiliary-line construction. The crux of the AI's contradiction (Steps 19-20) is the claim that the difference sq(MC) - sq(MD) is rational, where M is the midpoint of AB, because 'MC and MD are expressible in terms of the segments and their differences are commensurable.' This claim is unsupported: MC = AB/2 - AC and MD = AB/2 - AD, but AC and CB are incommensurable in square (by hypothesis), and there is no cited proposition or prior step that establishes MC and MD as commensurable or their difference of squares as rational. In Heath's proof of the closely related 10.42, a similar argument works because the sums of squares on the parts are rational (for binomial terms); here they are medial, which is precisely why Heath takes a completely different approach via area application to a rational line. The AI's unsupported rationality claim is the sole basis for the contradiction, making this a genuine logical gap rather than mere brevity.
**Audit Record**: CANDIDATE E — 10.47
  violated_claim : "The square on MC minus the square on MD is a difference of squares on segments that are commensurable (both being differences of commensurable parts of the same line). This difference of squares is rational." (Steps 19-20)
  failure_mode   : unsupported_assertion
  missing_is     : support — no cited proposition or prior step establishes that MC and MD are commensurable or that sq(MC)-sq(MD) is rational. MC = AB/2 - AC and MD = AB/2 - AD; the hypothesis states AC,CB are incommensurable in square, providing no basis for commensurability of MC and MD.
  evidence       : Steps 19-20 assert sq(MC)-sq(MD) is rational because "MC and MD are expressible in terms of the segments and their differences are commensurable." No citation supports this. The segments MC,MD are differences involving incommensurable magnitudes (AC, AD measured from the midpoint), and no proposition in the proof chain licenses the rationality claim.
  why_not_terse  : This is not brevity — it is the central claim on which the entire contradiction depends. The assertion that sq(MC)-sq(MD) is rational cannot be derived from any cited or available proposition given the hypotheses (sums of squares are medial, not rational). Heath's proof of 10.42 uses a structurally similar argument that works only because binomial terms have rational sums of squares; the AI incorrectly transfers this reasoning to the medial-area case.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-11: Proposition 10.52（Run C）

#### AI 证明原文（Run C）

## Proposition 10.52
**Statement:** To find the fifth binomial straight line.

**Step 1.** Let a rational straight line A be set out, and let two numbers CG and GD be set out such that CG and GD have not to one another the ratio which a square number has to a square number, and let CD also not have to CG the ratio which a square number has to a square number, but let it have to GD the ratio which a square number has to a square number.

**Step 2.** Let the square number p^2 be such that CD has to GD the ratio p^2 : q^2 for some number q, while CD : CG is not such a ratio and CG : GD is not such a ratio. For example, let CD = 5, CG = 3, GD = 2. Then CD : GD = 5 : 2 (not a ratio of square numbers), so adjust: let CD = 8, CG = 3, GD = 5, then CD : GD = 8 : 5 (not square to square). We need CD : GD to be square to square. Let CD = 5, GD = 4, CG = 1, then CD : GD = 5 : 4 (not square to square). Let CD = 4, GD = 1, CG = 3, then CD : GD = 4 : 1 (square to square), CD : CG = 4 : 3 (not square to square), CG : GD = 3 : 1 (not square to square). These numbers satisfy our requirements.

**Step 3.** Let the square on E be to the square on A as the number CG is to GD, so that the square on E has to the square on A the ratio 3 : 1, which is not a ratio of square numbers. Then E and A are rational straight lines commensurable in square only, by 10.6 and 10.9: since CG : GD is not the ratio of a square number to a square number, E and A are incommensurable in length (by 10.9), yet commensurable in square since both squares are commensurable (the ratio 3 : 1 being a ratio of numbers, so by 10.6 the squares are commensurable).

**Step 4.** Since E and A are rational and commensurable in square only, the sum E + A is a binomial straight line, by 10.36.

**Step 5.** We must now show that this binomial is a fifth binomial. By the definition D10.2.5, we need: (i) the square on the greater term exceeds the square on the lesser by the square on a straight line incommensurable in length with the greater, and (ii) the lesser term is commensurable in length with the rational straight line set out.

**Step 6.** Now identify the terms. Since the square on E is to the square on A as 3 : 1, the square on E is greater than the square on A, so E is the greater term and A is the lesser term of the binomial. The lesser term A is the rational straight line set out, so A is commensurable in length with itself. This satisfies condition (ii).

**Step 7.** For condition (i), we must show that the square on E (the greater) exceeds the square on A (the lesser) by the square on a straight line incommensurable in length with E. The square on E is to the square on A as CG : GD = 3 : 1. So the square on E equals 3 times the square on A. Then the square on E minus the square on A equals 2 times the square on A. Let F be such that the square on F equals the square on E minus the square on A. Then the square on F equals 2 times the square on A.

**Step 8.** Now the square on E is to the square on F as the square on E is to (the square on E minus the square on A), which equals (3 times the square on A) to (2 times the square on A), which equals 3 : 2. By 5.11 (or direct calculation), the ratio of the square on E to the square on F is 3 : 2.

**Step 9.** Equivalently, the square on E is to the square on F as CD : CG = 4 : 3. Since CD : CG = 4 : 3, and 4 : 3 is not the ratio of a square number to a square number, then by 10.9 the straight lines E and F are incommensurable in length.

**Step 10.** Thus the square on E is greater than the square on A by the square on a straight line F that is incommensurable in length with E. This satisfies condition (i).

**Step 11.** We also verify that E (the greater term) is incommensurable in length with A (the rational straight line set out), as already shown in Step 3. And A (the lesser term) is commensurable in length with the rational straight line A. These are exactly the conditions for a fifth binomial, by D10.2.5 (given D10.2.4: the square on the greater exceeds the square on the lesser by the square on a line incommensurable with the greater; D10.2.5 specifies: if the lesser term is commensurable in length with the rational straight line, it is a fifth binomial).

**Step 12.** Therefore E + A is a fifth binomial straight line, and the fifth binomial straight line has been found. Q.E.F.

**USED:** 10.36, 10.6, 10.9, D10.1.3, D10.2.4, D10.2.5
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.429 — AI adds ['D10.1.3', 'D10.2.4', 'D10.2.5']; Human adds ['5.19']

#### 分类报告原文（Run C）

### 10.52
**Category**: AI proof error
**Jaccard**: 0.429
**Analysis**: The AI proof contains a clear invalid inference in Step 9. After correctly computing in Steps 7-8 that sq(E):sq(F) = 3:2 (from sq(E) = 3*sq(A) and sq(F) = 2*sq(A)), the AI asserts in Step 9 that 'Equivalently, the square on E is to the square on F as CD : CG = 4 : 3.' The claim that 3:2 equals 4:3 is a mathematical falsehood. The AI attempts to connect the ratio to the number-theoretic ratio CD:CG to invoke 10.9, but the correct convertendo relationship (parallel to Heath's use of 5.19) would give sq(E):sq(F) = CG:(CG-GD) = 3:2, not CD:CG = 4:3. While the final conclusion (E and F are incommensurable) happens to be correct because 3:2 is also not square-to-square, the stated inference is invalid: the AI explicitly claims an equality between two unequal ratios. This is not terse-but-sound reasoning; it is a positively identifiable false mathematical claim in the proof chain. The audit record completes convincingly under the invalid_inference mode.
**Audit Record**: CANDIDATE E — 10.52
  violated_claim : In Step 9, the AI asserts 'Equivalently, the square on E is to the square on F as CD : CG = 4 : 3' after correctly computing the ratio as 3:2 in Step 8.
  failure_mode   : invalid_inference
  missing_is     : support — the AI states a false mathematical equality (3:2 = 4:3) as the basis for applying 10.9; this is not a matter of omitted expansion but a wrong inference.
  evidence       : Step 8 states 'the ratio of the square on E to the square on F is 3 : 2.' Step 9 then claims 'Equivalently, the square on E is to the square on F as CD : CG = 4 : 3.' With CD=4 and CG=3, the ratio CD:CG = 4:3 does not equal the previously computed 3:2. The correct convertendo relationship (analogous to Heath's use of 5.19) gives sq(E):sq(F) = CG:(CG-GD) = 3:2, not CD:CG = 4:3.
  why_not_terse  : This is not brevity or compression — the AI explicitly writes two contradictory numerical ratios (3:2 in Step 8, then 4:3 in Step 9) and calls them 'equivalent,' which is a false mathematical assertion.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-12: Proposition 10.86（Run B）

#### AI 证明原文（Run B）

## Proposition 10.86
**Statement:** To find the second apotome.

**Step 1.** Let a rational straight line A be set out.

**Step 2.** By 10.29, find two rational straight lines FG and GH, commensurable in square only, such that FG is greater than GH, the square on FG is greater than the square on GH by the square on a straight line commensurable in length with FG, and GH is commensurable in length with the rational straight line A.

**Step 3.** Since FG and GH are rational straight lines commensurable in square only, FG - GH is an apotome [by 10.73]. Let this apotome be K, with FG as the whole and GH as the annex.

**Step 4.** I say that K is a second apotome. We must verify the three conditions of the definition D10.3.2.

**Step 5.** First, the annex GH is commensurable in length with the rational straight line A set out. This holds by the construction in Step 2.

**Step 6.** Second, the square on the whole FG is greater than the square on the annex GH by the square on a straight line commensurable in length with FG. This also holds directly by the construction in Step 2, since 10.29 guarantees precisely this property.

**Step 7.** Third, we must show that the whole FG is not commensurable in length with the rational straight line A. Suppose, for the sake of contradiction, that FG is commensurable in length with A. Since GH is also commensurable in length with A [Step 5], it would follow by 10.12 that FG is commensurable in length with GH. But FG and GH are commensurable in square only [Step 2], hence incommensurable in length. This is a contradiction. Therefore FG is not commensurable in length with A.

**Step 8.** Since the annex GH is commensurable in length with A, the square on the whole FG is greater than the square on the annex GH by the square on a straight line commensurable in length with FG, and the whole FG is not commensurable in length with A, the apotome K = FG - GH is a second apotome [by D10.3.2].

**Step 9.** Therefore the second apotome has been found. Q.E.F.

**USED:** 10.12, 10.29, 10.73, D10.3.2
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.2
**Jaccard:** 0.286 — AI adds ['10.12', '10.29']; Human adds ['10.6', '10.9', '5.19']

#### 分类报告原文（Run B）

### 10.86
**Category**: AI proof error
**Jaccard**: 0.286
**Analysis**: Q1 decided the classification. The AI proof in Step 2 asserts that Proposition 10.29 can find two rational straight lines FG and GH such that 'GH is commensurable in length with the rational straight line A.' However, 10.29 states only: 'To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.' It guarantees no relationship between either output line and any external rational line. In Heath's proof of 10.29, the starting rational line AB becomes the greater, and the lesser AF is constructed via a semicircle and shown to be incommensurable in length with AB. If one sets the starting line commensurable with A, then the lesser line (GH) would be incommensurable in length with A, the opposite of what the AI claims. The AI positively attributes to 10.29 a property it does not entail, making the entire construction unsound. This is not mere brevity or compression -- no gap-filling can make 10.29 yield commensurability of the lesser line with a separately given rational line. The rest of the AI proof (Steps 3-9) is logically valid given Step 2's false premises, but the foundational construction step is an invalid inference from the cited proposition.
**Audit Record**: CANDIDATE E — 10.86
  violated_claim : Step 2 asserts that 10.29 can find FG, GH such that 'GH is commensurable in length with the rational straight line A'
  failure_mode   : invalid_inference
  missing_is     : support — 10.29 guarantees no such relationship between the lesser line and any external rational line; the lesser line produced by 10.29 is commensurable in square only with the greater, and choosing the starting line commensurable with A makes the lesser INCOMMENSURABLE in length with A
  evidence       : AI Step 2: 'By 10.29, find two rational straight lines FG and GH, commensurable in square only, such that... GH is commensurable in length with the rational straight line A.' 10.29 statement: 'To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.' No mention of commensurability with an external line.
  why_not_terse  : The AI is not being brief; it is positively asserting that 10.29 entails a property (GH commensurable in length with A) that 10.29 does not provide. The construction in 10.29 starts with 'any rational straight line' as the greater, and the lesser is constructed to be incommensurable in length with it. There is no parameter in 10.29 that controls commensurability of the lesser with any external line.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-13: Proposition 10.87（Run C）

#### AI 证明原文（Run C）

## Proposition 10.87
**Statement:** To find the third apotome.

**Step 1.** Let a rational straight line A be set out, and let three numbers E, BC, and CD be given such that E and BC have not to one another the ratio which a square number has to a square number, but BC has to CD the ratio which a square number has to a square number, and E is not a square number. [Such numbers can be found; for instance, let E be a non-square number, and let BC and CD be chosen so that BC : CD is a square-to-square ratio while E : BC is not a square-to-square ratio.]

**Step 2.** Let it be contrived that E is to BC as the square on A is to the square on FG. [10.6, applied in reverse: since E : BC is a ratio of numbers, we can find FG such that sq(A) : sq(FG) = E : BC.] Then the square on A is commensurable with the square on FG. [10.6] Therefore FG is rational. [D10.1.3, since A is rational and FG is commensurable in square with A.]

**Step 3.** Since E is to BC not as a square number to a square number, the square on A has not to the square on FG the ratio which a square number has to a square number. [By construction from Step 2.] Therefore A is incommensurable in length with FG. [10.9]

**Step 4.** Now let it be contrived that BC is to CD as the square on FG is to the square on GH. [10.6, applied similarly to find GH.] Then the square on FG is commensurable with the square on GH. [10.6] Therefore GH is rational. [D10.1.3]

**Step 5.** Since BC is to CD as the square on FG is to the square on GH, and BC has to CD the ratio which a square number has to a square number, therefore the square on FG has to the square on GH the ratio which a square number has to a square number. Therefore FG is commensurable in length with GH. [10.9]

**Step 6.** Since E is to BC as the square on A is to the square on FG, and BC is to CD as the square on FG is to the square on GH, therefore ex aequali E is to CD as the square on A is to the square on GH. [5.22]

**Step 7.** But E is not a square number, and CD is a number (hence if E : CD were a square-to-square ratio, since BC : CD is square-to-square, then E : BC would also be square-to-square by the properties of ratios among numbers, contradicting our hypothesis). Therefore E has not to CD the ratio which a square number has to a square number. Therefore the square on A has not to the square on GH the ratio which a square number has to a square number. [By the construction in Step 6.] Therefore A is incommensurable in length with GH. [10.9]

**Step 8.** Since FG is commensurable in length with GH [Step 5], and FG is greater than GH (which can be ensured by taking BC > CD), FG and GH are both rational straight lines commensurable in square only with respect to A but commensurable in length with each other.

**Step 9.** Let the straight line FH equal to FG minus GH be taken, so that FH is an apotome with whole FG and annex GH. [10.73, since FG and GH are rational and commensurable in square only — but here we need to note: FG and GH are commensurable in length, so we must verify the apotome structure differently.] We set FH = FG - GH.

**Step 10.** Now consider the square on FG versus the square on GH. Since FG is commensurable in length with GH [Step 5], the square on FG is greater than the square on GH by the square on a straight line commensurable in length with FG. [10.17, since FG and GH are commensurable in length, when we apply the parallelogram to FG equal to the fourth of the square on GH, it divides FG into commensurable parts, hence sq(FG) - sq(GH) = sq(K) where K is commensurable with FG.]

**Step 11.** Neither FG nor GH is commensurable in length with the rational straight line A. [FG is incommensurable in length with A by Step 3; GH is incommensurable in length with A by Step 7.]

**Step 12.** Now FG and GH are rational straight lines commensurable in square only (they are commensurable in length with each other, but each is rational — commensurable in square with A). The straight line FH = FG - GH is an apotome. [10.73, for FG and GH are rational lines; since FG is commensurable in length with GH, we need to re-examine. In fact, since FG and GH are commensurable in length, FH is not formed as in 10.73 directly. Rather, we establish that FH is the difference of two terms of an apotome as follows.]

**Step 13.** We verify the three conditions for a third apotome [D10.3.3]: (i) The square on the whole FG is greater than the square on the annex GH by the square on a straight line commensurable with FG. This was established in Step 10 via 10.17. (ii) The whole FG is not commensurable in length with the assigned rational straight line A. This was established in Step 3. (iii) The annex GH is not commensurable in length with A. This was established in Step 7.

**Step 14.** Therefore FH is a third apotome relative to the rational straight line A. [D10.3.3]

**Step 15.** Thus the third apotome FH has been found. Q.E.F.

**USED:** 10.17, 10.6, 10.73, 10.9, 5.22, D10.1.3, D10.3.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.3
**Jaccard:** 0.625 — AI adds ['10.17', 'D10.1.3']; Human adds ['5.19']

#### 分类报告原文（Run C）

### 10.87
**Category**: AI proof error
**Jaccard**: 0.625
**Analysis**: The AI proof uses a different numerical setup from Heath's: the AI stipulates that BC:CD IS a square-to-square ratio (Step 1), whereas Heath stipulates that BC:CD is NOT a square-to-square ratio. This difference is fatal. With the AI's setup, Step 5 correctly derives that FG is commensurable in LENGTH with GH (not merely in square). But 10.73, which the AI cites to establish FH as an apotome, requires that FG and GH be 'commensurable in square only' -- that is, commensurable in square but NOT in length. The AI itself acknowledges the contradiction in Steps 9 and 12 ('since FG is commensurable in length with GH, FH is not formed as in 10.73 directly') but never provides a valid alternative justification. With FG and GH commensurable in length and both rational, FH = FG - GH would itself be rational, not an apotome. Since FH is never validly shown to be an apotome, it cannot be classified as a third apotome. This is a genuine invalid inference -- the AI infers a conclusion (FH is an apotome via 10.73) from premises that contradict the cited proposition's hypothesis -- not mere brevity or compression.
**Audit Record**: CANDIDATE E — 10.87
  violated_claim : FH is an apotome (cited as following from 10.73 in Steps 9 and 12)
  failure_mode   : invalid_inference
  missing_is     : support
  evidence       : AI Step 1 sets BC:CD as a square-to-square ratio. AI Step 5 derives FG commensurable in length with GH from this. AI Steps 9 and 12 cite 10.73, which requires 'commensurable in square only,' but the AI's own construction gives commensurable in length. The AI explicitly notes the problem ('FG and GH are commensurable in length, so we must verify the apotome structure differently' in Step 9; 'since FG is commensurable in length with GH, FH is not formed as in 10.73 directly' in Step 12) but never resolves it.
  why_not_terse  : This is not brevity -- the AI's own construction produces premises (FG comm. in length with GH) that contradict the hypothesis of the theorem it cites (10.73 requires comm. in square only). The AI acknowledges the contradiction but provides no resolution. With FG and GH commensurable in length and both rational, FH would be rational, not an apotome.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-14: Proposition 11.8（Run C）

#### AI 证明原文（Run C）

## Proposition 11.8
**Statement:** If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

**Step 1.** Let AB and CD be two parallel straight lines, and let AB be at right angles to a plane P. Let B and D be the points where AB and CD meet the plane P respectively. I say that CD is also at right angles to plane P. Join BD [P1]; since B and D both lie in P, BD lies in P. By 11.7, the line BD also lies in the same plane as the parallel lines AB and CD.

**Step 2.** Since AB is at right angles to plane P, AB makes right angles with every line in P meeting it at B [D11.3]. In particular, angle ABD is a right angle.

**Step 3.** Since AB is parallel to CD and BD is a transversal, the alternate interior angles are equal [1.29]. Therefore angle BDC equals angle ABD. Since angle ABD is a right angle, angle BDC is also a right angle. Thus CD is perpendicular to BD.

**Step 4.** I will show that ABDC is a parallelogram (hence a rectangle). Since AB is parallel to CD [given], BD is a transversal, and angle ABD equals angle BDC (both right angles) [Steps 2, 3], apply 1.29 to obtain that the alternate angles angle ADB and angle DBC are also equal. In triangle ABD, angle ABD is a right angle, so angle BAD plus angle ADB equals a right angle [1.32]. In triangle BDC, angle BDC is a right angle, so angle BCD plus angle DBC equals a right angle [1.32]. Since angle ADB equals angle DBC [1.29], it follows that angle BAD equals angle BCD.

**Step 5.** By 1.26 (AAS), applied to triangles ABD and CDB: angle ABD equals angle CDB [both right angles], angle ADB equals angle DBC [1.29], and BD is common. Therefore AB equals CD and AD equals BC.

**Step 6.** Since AB is parallel to CD and AB equals CD [Step 5], the straight lines AC and BD joining their endpoints in the same direction are equal and parallel [1.33]. Therefore ABDC is a parallelogram; indeed it is a rectangle since angles at B and D are right angles.

**Step 7.** In plane P, draw line DE through D perpendicular to BD [1.11]. Through B, draw line BG in plane P parallel to DE [1.31]. Since BG is parallel to DE and BD is a transversal, the alternate angles are equal [1.29], so angle GBD equals angle BDE, which is a right angle [construction]. Thus BG is perpendicular to BD at B.

**Step 8.** Cut off BG equal to DE [1.3]. Since BG is parallel to DE [Step 7] and BG equals DE, the segments BD and GE joining their endpoints in the same direction are themselves equal and parallel [1.33]. Thus BGED is a parallelogram in plane P, with BD equal to GE and BD parallel to GE [1.34].

**Step 9.** Since AC is parallel to BD and AC equals BD [Step 6], and GE is parallel to BD and GE equals BD [Step 8], it follows that AC is parallel to GE and AC equals GE [1.30 gives AC parallel to GE; equality follows since both equal BD].

**Step 10.** Since AC and GE are equal and parallel, the straight lines AG and CE joining their endpoints in the same direction are themselves equal and parallel [1.33]. Therefore AG equals CE.

**Step 11.** Since AB is at right angles to plane P and BG lies in plane P, angle ABG is a right angle [D11.3]. In right triangle ABG, by 1.47, AG squared equals AB squared plus BG squared.

**Step 12.** Now consider triangles ABG and CDE. We have AB equals CD [Step 5], BG equals DE [Step 8, by construction], and AG equals CE [Step 10]. By 1.8 (SSS), triangles ABG and CDE are congruent. Therefore angle ABG equals angle CDE.

**Step 13.** Since angle ABG is a right angle [Step 11], angle CDE is also a right angle [Step 12]. Thus CD is perpendicular to DE.

**Step 14.** We have shown that CD is perpendicular to BD [Step 3] and CD is perpendicular to DE [Step 13]. The lines BD and DE both lie in plane P and meet at the point D (and they are not parallel, being perpendicular to each other). By 11.4, since CD is at right angles to two straight lines BD and DE which cut one another at D, CD is at right angles to the plane through BD and DE, which is the plane P.

**Step 15.** Therefore, if two straight lines are parallel and one of them is at right angles to any plane, the remaining one is also at right angles to the same plane. Q.E.D.

**USED:** 1.11, 1.26, 1.29, 1.3, 1.30, 1.31, 1.32, 1.33, 1.34, 1.47, 1.8, 11.4, 11.7, D11.3, P1
**Human refs (from References field):** 1.29, 11.2, 11.4, 11.7, D11.3
**Jaccard:** 0.250 — AI adds ['1.11', '1.26', '1.3', '1.30', '1.31', '1.32', '1.33', '1.34', '1.47', '1.8', 'P1']; Human adds ['11.2']

#### 分类报告原文（Run C）

### 11.8
**Category**: AI proof error
**Jaccard**: 0.250
**Analysis**: The AI proof contains an invalid inference in Step 4 where it claims 'apply 1.29 to obtain that the alternate angles angle ADB and angle DBC are also equal.' Proposition 1.29, applied to parallel lines AB and CD with transversal BD, yields the alternate interior angles ABD = BDC (which the AI correctly used in Step 3), but does NOT yield angle ADB = angle DBC. The angles ADB and DBC are not formed at the intersection of the transversal with the parallel lines and thus are not alternate angles under 1.29. This invalid angle equality is then used in Step 5 via AAS (1.26) to conclude AB = CD, a result that is not generally true for parallel lines one of which is perpendicular to a plane. The false conclusion AB = CD propagates through Steps 6, 9, 10, and 12, undermining the SSS congruence argument in Step 12 that establishes angle CDE is right. Without this, the proof fails to show CD is perpendicular to a second line DE in the plane, which is essential for the application of 11.4 in Step 14. Heath's proof avoids this issue entirely by constructing an auxiliary point E with DE = AB rather than attempting to prove AB = CD.
**Audit Record**: CANDIDATE E — 11.8
  violated_claim : "angle ADB equals angle DBC" derived from 1.29 in Step 4, used as basis for AAS congruence in Step 5 to conclude AB = CD
  failure_mode   : invalid_inference
  missing_is     : support — the angle equality has no valid justification; 1.29 does not yield this result for the given configuration
  evidence       : Step 4 states "apply 1.29 to obtain that the alternate angles angle ADB and angle DBC are also equal" — 1.29 applied to parallels AB||CD with transversal BD yields angle ABD = angle BDC (already used in Step 3), not angle ADB = angle DBC. The latter angles are not alternate interior angles formed at intersection points of the transversal with the parallel lines.
  why_not_terse  : The AI explicitly cites 1.29 as justification for a specific angle equality that 1.29 cannot produce for this configuration. This is not abbreviated reasoning but a misapplication of the cited proposition. The false conclusion AB = CD that follows is essential to the SSS argument in Steps 12-13 and cannot be independently verified.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-15: Proposition 11.31（Run A）

#### AI 证明原文（Run A）

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let the parallelepipedal solids AB and CD be on equal bases, namely the parallelograms FGHK and LMNO respectively, and let them have the same height. We must prove that solid AB equals solid CD.

**Step 2.** On the straight line FG, and at the point F on it, apply the parallelogram FGPQ equal to the parallelogram LMNO in the angle GFQ equal to angle MLO, using Proposition 1.45. Since FGHK and LMNO are equal by hypothesis, and FGPQ equals LMNO by construction, it follows that FGPQ equals FGHK [CN1].

**Step 3.** Erect on the base FGPQ a parallelepipedal solid RS with the same height as solids AB and CD, and with the edges standing up from F, G, P, Q parallel to the corresponding edges of solid AB standing up from F, G, H, K. This is possible by Proposition 11.27 (describing a parallelepiped similar and similarly situated to a given one on a given line) and the construction of parallel lines by Proposition 1.31.

**Step 4.** Since solid AB stands on base FGHK and solid RS stands on base FGPQ, and these two bases are equal (as shown in Step 2), and both solids have the same height, and they share the edge FG with their lateral edges from F and G being the same lines, the remaining lateral edges stand up from H, K and from P, Q respectively. Since FGHK and FGPQ are equal parallelograms on the same straight line FG, they lie in the same plane [11.7, 11.2]. The solids AB and RS are on the same base line FG with the same height.

**Step 5.** Now, solids AB and RS are on the same base (sharing the side FG in the base plane) and of the same height, with lateral edges standing up from the vertices of their respective bases. If the extremities of the sides which stand up lie on the same straight lines, then by Proposition 11.29 the solids are equal. If not, then by Proposition 11.30 they are still equal. In either case, solid AB equals solid RS.

**Step 6.** Similarly, since solid CD stands on base LMNO and solid RS stands on base FGPQ, and FGPQ was constructed equal to LMNO (Step 2), we must show solid CD equals solid RS. Apply the same method: on the straight line LM, we could construct the comparison, or equivalently, since FGPQ = LMNO, we construct on LM a parallelogram equal to FGPQ in the appropriate angle. But more directly: erect on LMNO a parallelepiped with the same lateral edge directions as RS. Since FGPQ equals LMNO and both solids have the same height, the same argument using 11.29 or 11.30 shows solid CD equals solid RS.

**Step 7.** Since solid AB equals solid RS (Step 5) and solid CD equals solid RS (Step 6), by Common Notion 1, solid AB equals solid CD.

**Step 8.** Therefore, parallelepipedal solids which are on equal bases and of the same height are equal to one another. Q.E.D.

**USED:** 1.31, 1.45, 11.2, 11.27, 11.29, 11.30, 11.7, CN1
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.125 — AI adds ['1.31', '1.45', '11.2', '11.27', '11.7', 'CN1']; Human adds ['1.23', '1.35', '11.24', '11.25', '5.11', '5.7', '5.9', 'D11.10']

#### 分类报告原文（Run A）

### 11.31
**Category**: AI proof error
**Jaccard**: 0.125
**Analysis**: The classification was decided at Q1(b). The AI proof constructs a comparison solid RS on base FGPQ (constructed equal to LMNO via I.45) and then claims in Step 5 that solids AB (on base FGHK) and RS (on base FGPQ) are 'on the same base (sharing the side FG in the base plane)' and applies 11.29 or 11.30 to conclude AB equals RS. However, 11.29 and 11.30 both require the solids to be on THE SAME base - meaning the identical base parallelogram - not merely on equal bases that share one edge. FGHK and FGPQ are different parallelograms (equal in area but geometrically distinct), so the hypothesis of 11.29/11.30 is not satisfied. This is not a matter of compression or terseness: the AI explicitly identifies two different bases and then incorrectly claims they constitute 'the same base' for purposes of applying 11.29/11.30. Heath's proof avoids this by using a ratio argument through 11.25, 5.7, 5.9, and 5.11 to compare solids on different but related bases.
**Audit Record**: CANDIDATE E — 11.31
  violated_claim : In Step 5, the AI applies 11.29/11.30 (which require solids on 'the same base') to solids AB (on base FGHK) and RS (on base FGPQ), which are on different (though equal) bases sharing only edge FG
  failure_mode   : invalid_inference
  missing_is     : support — there is no proposition or valid argument licensing the conclusion that solids on different bases sharing one edge can be compared via 11.29/11.30, which explicitly require the same base
  evidence       : AI Step 5: 'solids AB and RS are on the same base (sharing the side FG in the base plane) and of the same height... by Proposition 11.29 the solids are equal. If not, then by Proposition 11.30 they are still equal.' But 11.29 states 'on the same base' meaning the identical parallelogram, not equal parallelograms sharing an edge. FGHK ≠ FGPQ.
  why_not_terse  : The AI explicitly identifies two distinct bases (FGHK and FGPQ) in Step 4, then incorrectly equates sharing one edge with being 'on the same base' in Step 5. This is not compression of a sound argument but misapplication of a proposition whose central hypothesis is not met. Heath's proof shows the gap is real: comparing solids on equal-but-different bases requires the ratio argument via 11.25, 5.7, 5.9, 5.11, which the AI entirely omits.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-16: Proposition 12.17（Run B）

#### AI 证明原文（Run B）

## Proposition 12.17
**Statement:** Given two spheres about the same centre, to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface.

**Step 1.** Let there be two spheres about the same centre A, and let it be required to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface.

**Step 2.** Cut the spheres by any plane through the centre A. This produces two concentric circles: the great circle BCDE of the greater sphere and the great circle FGHK of the lesser sphere, both with centre A [D11.14, D11.17].

**Step 3.** Draw two diameters BD and CE of the greater circle at right angles to one another [1.11]. These diameters also pass through the centre A of the lesser circle.

**Step 4.** By 12.16, inscribe in the greater circle BCDE an equilateral polygon with an even number of sides which does not touch the lesser circle FGHK. Let this polygon have sides BM, ME, EN, ND, DO, OC, CP, PB (or similar vertices on the circle), so that no side touches circle FGHK [12.16].

**Step 5.** Let BM be one of the sides of the inscribed polygon that cuts one of the quadrants. Draw a perpendicular from the centre A to BM; let it meet BM at the point L [1.12]. Then AL, being the perpendicular from the centre to a chord of the greater circle, is less than the radius of the greater circle, but since the polygon does not touch the lesser circle, AL is greater than the radius AF of the lesser circle [3.14, 3.15]. That is, the perpendicular distance from A to each side of the polygon is greater than the radius of the lesser sphere.

**Step 6.** Through each side of the inscribed polygon (such as BM), erect a plane perpendicular to the plane of the great circle BCDE [11.12]. Each such plane intersects the greater sphere in a great circle (since the plane passes through a chord of the great circle and is perpendicular to the plane containing that great circle).

**Step 7.** On each chord (such as BM), within the circle formed by the plane through that chord, the chord BM subtends an arc of that circle. In this new circle, inscribe the same equilateral polygon as in Step 4 (with the same number of sides), placing BM as one side, and erecting the remaining vertices on the circle in the perpendicular plane [4.1, 12.16]. Since this new circle is a great circle of the greater sphere (having the same radius), the inscribed polygon is congruent to the polygon in the original plane.

**Step 8.** Carry out this construction for every side of the original polygon from Step 4. Connect adjacent vertices of polygons in adjacent perpendicular planes to form triangular faces. The result is a polyhedral solid whose vertices all lie on the surface of the greater sphere, hence it is inscribed in the greater sphere [D11.14].

**Step 9.** It remains to show that this polyhedral solid does not touch the lesser sphere. Consider any face of the polyhedral solid. Each face is either a side of one of the inscribed polygons in a perpendicular plane or a triangle connecting vertices of adjacent polygons. In every case, the face is a plane figure.

**Step 10.** Drop a perpendicular from the centre A to the plane of any face of the solid [11.11]. This perpendicular is the shortest distance from A to that plane. Since every face of the solid lies on a chord or triangle that is at least as far from the centre A as the perpendicular distance AL found in Step 5, and since AL is greater than the radius of the lesser sphere, the perpendicular from A to any face must also be greater than the radius of the lesser sphere [1.19, CN5].

**Step 11.** More precisely, in the original plane, the perpendicular from A to each side of the polygon exceeds the radius of the lesser circle (Step 5). For a face in a perpendicular plane, the perpendicular from A to that face is at least as great as the perpendicular from A to the corresponding chord in the original plane, because the face in the perpendicular plane lies on or beyond the chord relative to A. Thus the perpendicular from A to every face of the polyhedron is greater than the radius of the lesser sphere [3.15, 11.38].

**Step 12.** Since the distance from the centre A to every face of the polyhedral solid exceeds the radius of the lesser sphere, the surface of the lesser sphere cannot meet any face of the solid. Therefore the polyhedral solid inscribed in the greater sphere does not touch the lesser sphere at its surface [D11.14].

**Step 13.** Therefore, given two spheres about the same centre, we have inscribed in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface, which is what was required to construct. Q.E.F.

**USED:** 1.11, 1.12, 1.19, 11.11, 11.12, 11.38, 12.16, 3.14, 3.15, 4.1, CN5, D11.14, D11.17
**Human refs (from References field):** 1.26, 1.33, 1.47, 11.11, 11.18, 11.2, 11.6, 11.7, 11.9, 3.27, 3.31, 6.2, 6.8, D11.14, D11.3, D11.4
**Jaccard:** 0.074 — AI adds ['1.11', '1.12', '1.19', '11.12', '11.38', '12.16', '3.14', '3.15', '4.1', 'CN5', 'D11.17']; Human adds ['1.26', '1.33', '1.47', '11.18', '11.2', '11.6', '11.7', '11.9', '3.27', '3.31', '6.2', '6.8', 'D11.3', 'D11.4']

#### 分类报告原文（Run B）

### 12.17
**Category**: AI proof error
**Jaccard**: 0.074
**Analysis**: The AI proof takes a fundamentally different constructive approach from Heath, erecting perpendicular planes through each side of the inscribed polygon and building the polyhedron from polygons in those planes. The critical question is Q1(b)/Q3(b): whether the AI's argument that the polyhedron does not touch the lesser sphere is logically complete. The AI's Steps 10-11 assert that the perpendicular from the centre A to any face of the solid exceeds the radius of the lesser sphere, claiming this follows because 'the face in the perpendicular plane lies on or beyond the chord relative to A.' This is the essential geometric claim of the entire proposition, and Heath devotes the majority of his proof to establishing it through an elaborate chain involving 3.27, 1.26, 6.2, 11.6, 1.33, 11.9, 11.7, 1.47, 3.31, and 6.8. The AI provides no valid supporting chain: the cited propositions 3.15 (chords nearer centre are greater), 11.38 (about bisecting cube faces, completely irrelevant), 1.19 (angle-side inequality in triangles), and CN5 (whole greater than part) do not license the 3D perpendicular-distance claim. This is not mere terseness but an unsupported assertion of the core conclusion, satisfying the hardened E standard.
**Audit Record**: CANDIDATE E — 12.17
  violated_claim : In Steps 10-11, the AI asserts 'the perpendicular from A to that face is at least as great as the perpendicular from A to the corresponding chord in the original plane, because the face in the perpendicular plane lies on or beyond the chord relative to A' and concludes the perpendicular from A to every face exceeds the radius of the lesser sphere.
  failure_mode   : unsupported_assertion
  missing_is     : support — this is the core geometric claim of the entire proposition, not an expansion of an already-supported step. Heath's proof requires an elaborate chain (3.27, 1.26, 6.2, 11.6, 1.33, 11.9, 11.7, 1.47, 3.31, 6.8) to establish the analogous result.
  evidence       : Step 10 cites 1.19 (angle-side inequality in triangles) and CN5 (whole > part); Step 11 cites 3.15 (diameter greatest chord) and 11.38 (bisecting cube faces). None of these propositions license the claim that the 3D perpendicular distance from A to a face in a perpendicular plane exceeds the perpendicular distance from A to the corresponding chord in the base plane. 11.38 is about cubes and is entirely irrelevant.
  why_not_terse  : This is not mere brevity — the claim is the essential geometric argument of the entire proposition. Heath devotes the bulk of his proof to exactly this argument, requiring detailed reasoning about equal perpendiculars, parallel lines, quadrilaterals in planes, inscribed quadrilaterals in circles, and Pythagorean relationships. The AI skips all of this, asserting the conclusion without any valid supporting chain.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-17: Proposition 12.17（Run C）

#### AI 证明原文（Run C）

## Proposition 12.17
**Statement:** Given two spheres about the same centre, to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface.

**Step 1.** Let there be two spheres about the same centre A, and let it be required to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface. Let the spheres be cut by any plane through the centre A. The sections will be circles [D11.14], the greater circle being in the greater sphere and the lesser in the lesser sphere, since the centre of the sphere is also the centre of the circle [D11.16]. Let these circles have centre A.

**Step 2.** Draw two diameters of the greater circle, BC and DE, at right angles to one another [1.11]. These diameters also pass through A, the common centre of both spheres.

**Step 3.** By Proposition 12.16, inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle. Let the sides of this polygon in the quadrant BE be BF, FG, GH, HE, and let the corresponding sides be placed similarly in the other quadrants by symmetry.

**Step 4.** Since the polygon is equilateral with an even number of sides and is inscribed in the greater circle, and does not touch the lesser circle, the perpendicular from A to any side of the polygon is greater than the radius of the lesser sphere. In particular, let AK be the perpendicular from A to the side BF [1.12]. Then AK is greater than the radius of the lesser sphere.

**Step 5.** Now set up the construction in three dimensions. Let the plane of the circle BDCE be a base plane. Through the diameter BD, erect a plane perpendicular to the plane BDCE [11.12]. In this perpendicular plane, the great circle through BD will also have centre A and the same radius as circle BDCE [D11.17].

**Step 6.** In each great circle plane through the diameter BD that is perpendicular to the base, the same polygon can be inscribed with sides equal to those of the polygon in the base circle, since all great circles of the sphere have the same radius [D11.17, 12.16]. Thus we inscribe the same equilateral polygon in each such great circle.

**Step 7.** Now connect the vertices: the polygon in the base plane has vertices such as F, G, H on the semicircle BED. Through each of these vertices, pass a plane parallel to the plane of the circle through BD perpendicular to BE [11.15]. Each such plane cuts the sphere in a lesser circle.

**Step 8.** Consider the plane through F parallel to the equatorial plane containing DE. This plane cuts the sphere in a circle with centre on the line BA [11.17 applied via the geometry of the sphere]. Let this circle have centre N, where N lies on BA. The radius NF of this circle is the distance from N to F.

**Step 9.** On each of these lesser circles, the corresponding vertices of the polygons inscribed in the various great circles through BD all lie, forming a regular polygon inscribed in that lesser circle [1.4, 3.14]. Connect adjacent vertices on each such lesser circle, and connect corresponding vertices on adjacent parallel circles, forming triangular and quadrilateral faces.

**Step 10.** The resulting solid figure is bounded by polygonal faces (triangles and quadrilaterals) whose vertices all lie on the greater sphere. Therefore, the polyhedral solid is inscribed in the greater sphere [D11.1, D11.2].

**Step 11.** It remains to show that this polyhedral solid does not touch the lesser sphere. Consider any face of the polyhedron. Draw the perpendicular from the centre A to the plane of that face [11.11]. This perpendicular is the shortest distance from A to that plane [11.38].

**Step 12.** Consider a face on the side surface of the polyhedron, such as a quadrilateral face BFQP where Q and P are corresponding vertices in an adjacent great-circle plane. The perpendicular from A to this face falls within the face or its plane. Now BF is a side of the inscribed polygon, and the perpendicular from A to line BF has length AK [from Step 4].

**Step 13.** The perpendicular distance from A to the plane of any face of the polyhedron is at least as great as the perpendicular distance from A to any edge of that face, which in turn is at least AK [1.19, 11.38]. Since AK is greater than the radius of the lesser sphere [Step 4, from 12.16], the perpendicular from A to every face is greater than the radius of the lesser sphere.

**Step 14.** Since every face of the polyhedral solid has the property that the perpendicular distance from the centre A to the plane of that face exceeds the radius of the lesser sphere, no face can touch or intersect the surface of the lesser sphere [D11.3, 3.16 applied to the cross-sections]. The lesser sphere, being a surface of revolution at fixed distance from A, lies entirely within the interior of the polyhedron.

**Step 15.** Therefore, a polyhedral solid has been inscribed in the greater sphere which does not touch the lesser sphere at its surface, which is what was required to be done.

**USED:** 1.11, 1.12, 1.19, 1.4, 11.11, 11.12, 11.15, 11.17, 11.38, 12.16, 3.14, 3.16, D11.1, D11.14, D11.16, D11.17, D11.2, D11.3
**Human refs (from References field):** 1.26, 1.33, 1.47, 11.11, 11.18, 11.2, 11.6, 11.7, 11.9, 3.27, 3.31, 6.2, 6.8, D11.14, D11.3, D11.4
**Jaccard:** 0.097 — AI adds ['1.11', '1.12', '1.19', '1.4', '11.12', '11.15', '11.17', '11.38', '12.16', '3.14', '3.16', 'D11.1', 'D11.16', 'D11.17', 'D11.2']; Human adds ['1.26', '1.33', '1.47', '11.18', '11.2', '11.6', '11.7', '11.9', '3.27', '3.31', '6.2', '6.8', 'D11.4']

#### 分类报告原文（Run C）

### 12.17
**Category**: AI proof error
**Jaccard**: 0.097
**Analysis**: The AI proof contains an invalid inference in Step 13 that is central to its conclusion. The AI claims 'The perpendicular distance from A to the plane of any face of the polyhedron is at least as great as the perpendicular distance from A to any edge of that face, which in turn is at least AK.' This inequality is reversed: the perpendicular from a point to a plane is the MINIMUM distance to any point in the plane, so dist(A, plane) <= dist(A, edge), not >=. The AI's chain dist(A,plane) >= dist(A,edge) >= AK is mathematically false. Correcting the inequality direction yields dist(A,plane) <= AK, which does not establish the desired conclusion that every face is farther from A than the lesser sphere's radius. Heath requires an elaborate argument using Pythagorean theorem (I.47), properties of circles (III.31), and similar triangles (VI.8) to show that the perpendicular from A to the face plane exceeds the lesser sphere radius. The AI bypasses this entirely through a reversed inequality. The cited references (1.19 about triangle sides, 11.38 about cube bisection) do not support the claim. This is not a matter of terseness but a positive logical error: the stated mathematical relationship is the opposite of the true one, and the conclusion does not follow.
**Audit Record**: CANDIDATE E — 12.17
  violated_claim : "The perpendicular distance from A to the plane of any face of the polyhedron is at least as great as the perpendicular distance from A to any edge of that face, which in turn is at least AK" (Step 13)
  failure_mode   : invalid_inference
  missing_is     : support — the inequality is reversed; the perpendicular from a point to a plane is the MINIMUM distance to any point in the plane, so it is LESS than or equal to the distance to any edge line, not greater. The AI's chain dist(A,plane) >= dist(A,edge) >= AK is backwards.
  evidence       : AI Step 13 text: "The perpendicular distance from A to the plane of any face of the polyhedron is at least as great as the perpendicular distance from A to any edge of that face, which in turn is at least AK [1.19, 11.38]." The cited refs (1.19 — greater angle subtends greater side; 11.38 — about cube bisection) do not support this claim. Correcting the inequality gives dist(A,plane) <= AK, which fails to establish the desired conclusion.
  why_not_terse  : This is not brevity — the AI makes an explicit mathematical claim (dist to plane >= dist to edge) that is the exact opposite of the geometric fact (dist to plane <= dist to edge). The correct direction would not yield the desired conclusion without Heath's detailed argument involving I.47, III.31, VI.8.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### E-18: Proposition 13.16（Run C）

#### AI 证明原文（Run C）

## Proposition 13.16
**Statement:** To construct an icosahedron and comprehend it in a sphere, like the aforesaid figures; and to prove that the side of the icosahedron is the irrational straight line called minor.

**Step 1.** Set out the diameter AB of the given sphere, and let it be cut at C so that AC is quadruple of CB. That is, AC = 4*CB, so if AB = d then CB = d/5 and AC = 4d/5.

**Step 2.** Describe a semicircle ADB on AB, and from C draw CD at right angles to AB [1.11]. Join DA and DB [P1].

**Step 3.** Since AC = 4*CB and AB = AC + CB = 5*CB, we have AB * BC = CB * 5CB, so AC * CB + CB^2 = CB * AB. By the properties of the semicircle, the angle ADB is a right angle [3.31], so in the right triangle ADB, DC is the perpendicular from the right angle to the hypotenuse. Thus DC^2 = AC * CB [6.8, 6.13], and DB^2 = AB * BC [6.8], and DA^2 = AB * AC [6.8].

**Step 4.** Describe a circle EFGHK with radius equal to DB. Since DB^2 = AB * BC, and AB = 5*BC, we have DB^2 = 5 * BC^2. Now the square on the radius DB of circle EFGHK equals 5 times the square on BC.

**Step 5.** Inscribe a regular decagon in circle EFGHK, and let its vertices in order be the points around the circle. The side of this decagon equals BC. For the side of a decagon inscribed in a circle of radius r satisfies: r^2 = s_10 * (s_10 + r), where s_10 is the decagon side. Setting r = DB and s_10 = BC, we verify: DB^2 = 5*BC^2 and BC*(BC + DB) gives the required relationship. More precisely, 2*DB is cut in extreme and mean ratio with BC as the greater segment [13.9, 13.5], and the decagon side equals BC.

**Step 6.** Inscribe a regular pentagon EFGHK in circle EFGHK with vertices at alternating vertices of the decagon [4.11]. The side of the pentagon is the side of the regular pentagon inscribed in the circle. By 13.10, the square on the side of the pentagon equals the squares on the side of the hexagon and the side of the decagon inscribed in the same circle.

**Step 7.** Now establish the arrangement in three dimensions. Let O be the center of the sphere, with AB a diameter. Set up a plane through O perpendicular to AB. In this plane describe a circle with center O and radius equal to DB. Inscribe a regular decagon in this circle, producing ten equally spaced points.

**Step 8.** Through C (where AC = 4*CB on diameter AB) draw a plane perpendicular to AB. This plane cuts the sphere in a circle. Compute the radius of this circle: since C divides AB so that AC = 4*CB, the distance from the center O of the sphere to C can be determined. O is the midpoint of AB, so OC = OA - AC = d/2 - 4d/5 = -3d/10, meaning C is at distance 3d/10 from O on the side of B. The radius r_C of the circle cut by the sphere at height C satisfies r_C^2 = (d/2)^2 - (3d/10)^2 = d^2/4 - 9d^2/100 = 16d^2/100 = (2d/5)^2 [1.47].

**Step 9.** Similarly, let C' be the point on AB on the other side of O such that BC' = 4*AC', i.e., C' is symmetric to C with respect to the center. Then OC' = 3d/10 on the side of A. The circle cut at C' also has radius 2d/5.

**Step 10.** In the circle at C (radius 2d/5), inscribe a regular pentagon with vertices P1, P2, P3, P4, P5 [4.11]. In the circle at C' (radius 2d/5), inscribe a regular pentagon with vertices Q1, Q2, Q3, Q4, Q5, rotated by 36 degrees relative to the first pentagon (offset by half a decagonal arc).

**Step 11.** The icosahedron has 12 vertices: the two poles A and B (the endpoints of the diameter), plus P1,...,P5 and Q1,...,Q5. Each pole connects to the five vertices of the nearer pentagon (A to Q1,...,Q5 and B to P1,...,P5). The ten vertices on the two pentagons connect in an antiprism pattern, with each Pi connected to Qi and Q(i+1).

**Step 12.** We must show all edges are equal. First, compute the side of the pentagon inscribed in a circle of radius 2d/5. The distance between adjacent Pi vertices is the side of a regular pentagon in a circle of radius 2d/5.

**Step 13.** Compute the distance from B to a vertex Pi. Point B is at the end of the diameter, and Pi lies on the circle at height C with radius 2d/5. The axial distance from B to the plane at C is BC = d/5. By the Pythagorean theorem [1.47], BP_i^2 = (d/5)^2 + (2d/5)^2 = d^2/25 + 4d^2/25 = 5d^2/25 = d^2/5.

**Step 14.** So BP_i^2 = d^2/5 = DB^2 (from Step 4, since DB^2 = AB * BC = d * d/5 = d^2/5). Therefore BP_i = DB, confirming each pole-to-pentagon edge equals DB [CN1].

**Step 15.** Now compute the side of the regular pentagon inscribed in a circle of radius r = 2d/5. By 13.10, (side of pentagon)^2 = (side of hexagon)^2 + (side of decagon)^2, where the hexagon side equals r = 2d/5. So we need the decagon side in this circle.

**Step 16.** For the side of the decagon inscribed in circle of radius 2d/5: By 13.9, the sum of the hexagon side and decagon side equals a line cut in extreme and mean ratio with the hexagon side as the greater segment. The decagon side s_10 in a circle of radius r satisfies the golden ratio relationship. For radius r = 2d/5, the decagon side is r*(sqrt(5)-1)/2.

**Step 17.** The pentagon side squared equals (2d/5)^2 + s_10^2 = 4d^2/25 + (the decagon side)^2 by 13.10. However, we need to verify this equals d^2/5 = DB^2 to confirm the pentagon edges match the pole-to-vertex edges.

**Step 18.** Actually, the pentagon side in a circle of radius R has side^2 = R^2 * (10 - 2*sqrt(5))/4 from 13.10. With R = 2d/5: side^2 = (4d^2/25)*(10 - 2*sqrt(5))/4 = d^2*(10 - 2*sqrt(5))/25. We need this to equal d^2/5 = 5d^2/25, so 10 - 2*sqrt(5) = 5, giving sqrt(5) = 5/2, which does not hold. So the pentagon sides are not equal to the pole edges. The construction requires more careful verification.

**Step 19.** Returning to Euclid's construction more carefully: Set the diameter of the sphere AB with AB = d. Let AB be cut at C so that AC = 4*CB, giving CB = d/5. Draw the semicircle on AB and erect CD perpendicular to AB. Then DC^2 = AC*CB = 4d^2/25 [6.8, 6.13], so DC = 2d/5. Also DB^2 = AB*BC = d^2/5 [6.8, 3.31].

**Step 20.** Set out a circle with center O and radius OE = DB (where O will be the center of the sphere). In this circle inscribe a regular decagon, and let E, F, G, H, K be alternate vertices forming a regular inscribed pentagon [4.11]. Erect a line from O perpendicular to the plane of circle EFGHK.

**Step 21.** On this perpendicular, mark points S above and T below the plane such that OS = OT = half of the side of the decagon inscribed in circle EFGHK. The side of the decagon inscribed in a circle of radius DB can be computed using 13.9: if the radius is DB, then the hexagon side is DB and the decagon side s satisfies that DB + s is cut in extreme and mean ratio with DB the greater segment. By 13.9, s is determined.

**Step 22.** Now, the key construction: Let the sphere have diameter AB = d with center at midpoint M. Set up two circles, both perpendicular to AB, at heights determined by cutting AB in extreme and mean ratio. In one circle (upper), inscribe a regular pentagon; in the other (lower), inscribe a regular pentagon rotated by 36 degrees. Add the two poles A and B.

**Step 23.** To verify the edges are equal, we compute the distance between adjacent vertices of the antiprism band. Take vertex Pi on the upper circle and vertex Qj on the lower circle, where they are adjacent. The vertical distance between the two pentagonal planes is determined by the construction. The horizontal displacement is determined by the rotation. By the Pythagorean theorem [1.47] and the properties of the regular pentagon and decagon [13.9, 13.10], this distance equals DB.

**Step 24.** More precisely: let the circle at C have radius DC = 2d/5 and the circle at C' (symmetric on the other side of center) also have radius 2d/5. The vertical separation CC' = AC' - AC or equivalently the distance between the two planes. Since OC = 3d/10, we have CC' = 2 * 3d/10 = 3d/5. Each pentagon has its vertices on a circle of radius 2d/5.

**Step 25.** Consider two vertices Pi and Qj in adjacent pentagons offset by 36 degrees. The angular separation between them, projected onto the horizontal, is 36 degrees (pi/5 radians). The horizontal distance between Pi and Qj can be computed. Let R = 2d/5 be the radius of each pentagonal circle. Then the horizontal squared distance is R^2 + R^2 - 2R^2*cos(36) = 2R^2(1 - cos 36).

**Step 26.** Now cos(36) = (1 + sqrt(5))/4 by the properties of the regular pentagon [13.8, 13.9]. So horizontal^2 = 2*(4d^2/25)*(1 - (1+sqrt(5))/4) = (8d^2/25)*((3-sqrt(5))/4) = 2d^2(3-sqrt(5))/25.

**Step 27.** The total distance PiQj^2 = horizontal^2 + (CC')^2/... wait, the vertical component is (3d/5)^2 = 9d^2/25. So PiQj^2 = 2d^2(3-sqrt(5))/25 + 9d^2/25 = d^2(6-2*sqrt(5)+9)/25 = d^2(15-2*sqrt(5))/25. For this to equal DB^2 = d^2/5 = 5d^2/25, we need 15-2*sqrt(5) = 5, i.e., sqrt(5) = 5, which is false.

**Step 28.** This indicates the two pentagonal planes are not at C and C' as naively placed. Euclid's actual construction proceeds differently. Let us follow Euclid more carefully. Set out circle EFGHK with radius r. In this circle inscribe a regular decagon. Take alternate vertices to form a regular pentagon EFGHK. At the center O erect a perpendicular. On this perpendicular set OL above and OL' below, where OL = OL' equals half of the straight line which is the side of the hexagon and the side of the decagon added together. This ensures the correct spacing.

**Step 29.** By 13.9, the side of the hexagon (= r) and the side of the decagon inscribed in the same circle, when added together, give a line cut in extreme and mean ratio with the hexagon side as greater segment. So OL = (r + s_10)/2 where s_10 is the decagon side.

**Step 30.** At height L above the plane, the five vertices of the pentagon, when connected to L, form edges of length: EL^2 = OL^2 + OE^2 = ((r+s_10)/2)^2 + r^2 [1.47]. For the icosahedron, we need EL to equal the side of the pentagon inscribed in circle EFGHK.

**Step 31.** The actual Euclidean construction sets up the icosahedron as follows. Take a circle of radius r and inscribe a regular pentagon EFGHK and a regular decagon. At the center, erect perpendiculars above and below. Above the plane at height h, inscribe another pentagon (from the midpoints of the decagonal arcs) in a circle of appropriate radius. Below, do the same. Add two apex points.

**Step 32.** Following Euclid precisely: Let AB be the diameter of the sphere. Set AB such that AB^2 = 5 * (side)^2 where side is the icosahedron edge. Cut AB at C so that AC = 4*CB. On the semicircle ADB, DC^2 = AC*CB [6.8], DB^2 = BC*BA [6.8, 3.31]. Describe circle EFGHK with radius DB. Inscribe regular pentagon EFGHK.

**Step 33.** Set up the icosahedron with its vertices as follows: Five upper vertices (N-ring) at the intersections of the sphere with lines drawn from the midpoints of the decagonal arcs at a calculated height. Five lower vertices at corresponding positions below. Two poles at top and bottom.

**Step 34.** Now, for the proof that all twenty faces are equilateral triangles: Each face consists of three vertices of the icosahedron. By the construction and the symmetry, there are three types of edges: (i) edges within each pentagonal ring, (ii) edges connecting the two rings, and (iii) edges from poles to the nearest ring. The equality of all edges follows from the specific choice of the height h and the radii, which are determined by the golden ratio relationships encoded in 13.8, 13.9, and 13.10.

**Step 35.** To show that the vertices lie on a sphere: By the construction, all twelve vertices are equidistant from the center. The five vertices of each pentagonal cap are at equal distance from the center by symmetry, and the two poles are at distance d/2 from center. The equal distance of pentagonal vertices from center follows from OE^2 + h^2 = (d/2)^2 where OE is the radius of the pentagonal circle and h is the height above center, verified by the relationship DC^2 = AC*CB and DB^2 = AB*BC [6.8, 6.13].

**Step 36.** Therefore twenty equilateral triangles have been constructed, and all twelve vertices lie on the sphere of diameter AB. This is an icosahedron comprehended in the sphere [D11.27].

**Step 37.** It remains to prove that the side of the icosahedron is the irrational straight line called minor. Let the diameter AB of the sphere be rational.

**Step 38.** We showed DB^2 = AB * BC where BC = AB/5. So DB^2 = AB^2/5. Since AB is rational, AB^2 is a rational area, and AB^2/5 is rational [D10.1.3, D10.1.4]. Therefore DB^2 is rational, and hence DB is rational (commensurable in square with AB).

**Step 39.** The side of the icosahedron is equal to the side of the regular pentagon inscribed in circle EFGHK of radius DB. By 13.11, if in a circle which has its diameter rational an equilateral pentagon be inscribed, the side of the pentagon is the irrational straight line called minor.

**Step 40.** The diameter of circle EFGHK is 2*DB. Since DB^2 = AB^2/5, and AB is rational, DB is irrational (not commensurable in length with AB, as sqrt(5) is irrational) but commensurable in square. The diameter 2*DB satisfies (2*DB)^2 = 4*DB^2 = 4*AB^2/5, which is rational in area. Hence 2*DB is rational in the sense required [D10.1.3]: it is commensurable in square with AB.

**Step 41.** More precisely, the diameter 2*DB is rational because (2*DB)^2 = 4*(AB^2/5) = (4/5)*AB^2, and since 4/5 is a ratio of numbers, (2*DB)^2 is commensurable with AB^2 [10.6], making 2*DB commensurable in square with the rational line AB, hence 2*DB is rational [D10.1.3].

**Step 42.** Since the diameter of circle EFGHK is rational, and a regular pentagon is inscribed in it, by 13.11 the side of the pentagon is the irrational straight line called minor.

**Step 43.** Since the side of the icosahedron equals the side of this inscribed pentagon, the side of the icosahedron is the irrational straight line called minor [CN1].

**Step 44.** Therefore an icosahedron has been constructed and comprehended in the given sphere, and it has been proved that the side of the icosahedron is the irrational straight line called minor. Q.E.F. and Q.E.D.

**USED:** 1.11, 1.47, 10.6, 13.10, 13.11, 13.5, 13.8, 13.9, 3.31, 4.11, 6.13, 6.8, CN1, D10.1.3, D10.1.4, D11.27, P1, P3
**Human refs (from References field):** 1.33, 11.6, 13.10, 13.11, 13.3, 13.9, 3.31, 4.15, 6.8, D5.9
**Jaccard:** 0.217 — AI adds ['1.11', '1.47', '10.6', '13.5', '13.8', '4.11', '6.13', 'CN1', 'D10.1.3', 'D10.1.4', 'D11.27', 'P1', 'P3']; Human adds ['1.33', '11.6', '13.3', '4.15', 'D5.9']

#### 分类报告原文（Run C）

### 13.16
**Category**: AI proof error
**Jaccard**: 0.217
**Analysis**: Q1(b) decided this classification. The AI proof attempts to construct an icosahedron but its own calculations in Steps 17-18 and 26-27 explicitly demonstrate that the construction parameters it chose do not yield equilateral triangular faces (Step 18 concludes 'So the pentagon sides are not equal to the pole edges' and Step 27 derives sqrt(5) = 5 'which is false'). After these failed attempts, the AI vaguely restates Euclid's approach in Steps 28-35 but never identifies correct construction parameters or verifies that any revised construction produces equal edges. Nevertheless, in Step 36 the AI asserts 'Therefore twenty equilateral triangles have been constructed, and all twelve vertices lie on the sphere of diameter AB.' This is an unsupported assertion under the hardened standard: the AI showed its construction fails, attempted but could not fix it, and then asserted the key conclusion without any valid supporting argument. This is not mere terseness or compression of a sound argument — it is the absence of any valid argument for the central claim. The second half of the proof (showing the side is minor, Steps 37-43) is logically sound, but the construction portion — the core of the proposition — lacks logical support.
**Audit Record**: CANDIDATE E — 13.16
  violated_claim : "Therefore twenty equilateral triangles have been constructed, and all twelve vertices lie on the sphere of diameter AB" (Step 36)
  failure_mode   : unsupported_assertion
  missing_is     : support — the AI's own calculations in Steps 17-18 and 26-27 show that edge equalities needed for equilateral triangles do not hold under the construction parameters it chose, and the AI never identifies correct construction parameters in its revised approach (Steps 28-35)
  evidence       : Step 18: "We need this to equal d^2/5 = 5d^2/25, so 10 - 2*sqrt(5) = 5, giving sqrt(5) = 5/2, which does not hold. So the pentagon sides are not equal to the pole edges." Step 27: "we need 15-2*sqrt(5) = 5, i.e., sqrt(5) = 5, which is false." Step 34: "The equality of all edges follows from the specific choice of the height h and the radii, which are determined by the golden ratio relationships encoded in 13.8, 13.9, and 13.10" — asserted without verification after two demonstrated failures.
  why_not_terse  : The AI demonstrated its construction is wrong via explicit computation, attempted to fix it but never completed a working construction, then asserted the conclusion; this is not compression of a valid argument but absence of any valid argument for the key claim that all twenty faces are equilateral triangles.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

## Part 2: 几何检查错误（FAIL）

共 11 个条目。

### GEO-1: Proposition 1.24（Run A）

#### AI 证明原文（Run A）

## Proposition 1.24
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

**Step 1.** Let ABC and DEF be two triangles with AB = DE, AC = DF, and angle BAC greater than angle EDF. We are to show that BC is greater than EF. Without loss of generality, assume DE is not less than DF (equivalently AB is not less than AC); if otherwise, relabel the vertices of each triangle accordingly.

**Step 2.** On the straight line DE, at the point D, construct the angle EDG equal to the angle BAC, with G on the same side of DE as F. [1.23]

**Step 3.** Along ray DG, cut off DG equal to AC (which equals DF). [1.3]

**Step 4.** Join EG and FG. [P1]

**Step 5.** Since AB equals DE, AC equals DG, and angle BAC equals angle EDG, the two sides BA and AC are equal to the two sides ED and DG respectively, and the contained angles are equal. Therefore, by the side-angle-side theorem, triangle ABC is congruent to triangle DEG; in particular, BC equals EG. [1.4]

**Step 6.** Since angle EDG equals angle BAC, which is greater than angle EDF, the ray DF lies strictly between rays DE and DG. Since DF equals DG and DE is not less than DF, the point F falls inside triangle DEG.

**Step 7.** Since F lies inside triangle DEG, the straight lines DF and EF are drawn from the extremities of side DE to the interior point F. Therefore, by Proposition 1.21, the angle DFE is greater than the angle DGE. [1.21]

**Step 8.** At point F, since E and G lie on opposite sides of the line DF, the ray FD falls between rays FE and FG. Therefore the angle EFG is the sum of angles EFD and DFG. Since the whole is greater than the part, angle EFG is greater than angle EFD, that is, angle EFG is greater than angle DFE. [CN5]

**Step 9.** At point G, since F lies inside triangle DEG, the ray GF falls between rays GD and GE. Therefore angle DGE is the sum of angles DGF and EGF. Since the whole is greater than the part, angle DGE is greater than angle EGF. [CN5]

**Step 10.** Combining Steps 7, 8, and 9: angle EFG is greater than angle DFE, angle DFE is greater than angle DGE, and angle DGE is greater than angle EGF. Therefore angle EFG is greater than angle EGF.

**Step 11.** In triangle EFG, since the angle EFG at vertex F is greater than the angle EGF at vertex G, the side opposite the greater angle is greater than the side opposite the lesser angle. Therefore EG is greater than EF. [1.19]

**Step 12.** Since BC equals EG (Step 5), it follows that BC is greater than EF, which was to be proved.

**USED:** 1.19, 1.21, 1.23, 1.3, 1.4, CN5, P1
**Human refs (from References field):** 1.19, 1.23, 1.4, 1.5
**Jaccard:** 0.375 — AI adds ['1.21', '1.3', 'CN5', 'P1']; Human adds ['1.5']

#### 几何检查报告原文（Run A）

#### Proposition 1.24

**Contradictory steps**: Step 6, Step 8

**Spatial claim 1** (Step 6): F lies inside triangle DEG, so the three angles DFE, EFG, GFD around F sum to 360 degrees
  - Required by: Application of Proposition 1.21 in Step 7

**Spatial claim 2** (Step 8): Ray FD falls between rays FE and FG, so angle EFG = angle EFD + angle DFG (additive decomposition)
  - Required by: Angle inequality chain in Steps 8-10 establishing angle EFG > angle DFE

**Contradiction**: If F is inside triangle DEG, the three angles DFE, EFG, GFD around F sum to 360 degrees. The additive decomposition angle EFG = angle EFD + angle DFG is equivalent to angle EFG = angle DFE + angle GFD. Substituting into the 360-degree sum gives: angle DFE + (angle DFE + angle GFD) + angle GFD = 360, so 2(angle DFE + angle GFD) = 360, forcing angle EFG = 180 degrees. But angle EFG = 180 degrees means E, F, G are collinear, contradicting both F being inside triangle DEG and triangle EFG being a valid triangle (as used in Step 11). Numerical verification confirms: from F, ray FD points away from the interior angle EFG, and it is the opposite ray (from F toward side EG) that actually falls between FE and FG.

**Fixable**: True
  - Heath avoids this error entirely by using Proposition 1.5 (isosceles triangle base angles) instead of Proposition 1.21. Since DF = DG, triangle DFG is isosceles, giving angle DGF = angle DFG. The valid decomposition at G (angle DGE = angle DGF + angle FGE, which IS correct) then gives angle DGF > angle EGF, so angle DFG > angle EGF. Since angle EFG is strictly greater than angle DFG (the opposite ray from D through F shows this), we get angle EFG > angle EGF without ever needing the invalid angle decomposition at F.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：并且不只它说的这一个错误。

---

### GEO-2: Proposition 3.25（Run C）

#### AI 证明原文（Run C）

## Proposition 3.25
**Statement:** Given a segment of a circle, to describe the complete circle of which it is a segment.

**Step 1.** Let ABC be the given segment of a circle, with base AC and arc ABC, where B is any point on the arc. We are to describe the complete circle of which this segment is a part. [D3.6]

**Step 2.** Bisect AC at D. [1.10]

**Step 3.** From D, draw DB at right angles to AC, where B is on the arc of the segment, and produce DB in both directions as needed. [1.11]

**Step 4.** Join AB. [P1]

**Step 5.** Now consider the angles ABD and BAD. Exactly one of three cases holds: (i) angle ABD equals angle BAD, (ii) angle ABD is greater than angle BAD, or (iii) angle ABD is less than angle BAD.

**Step 6.** Case (i): Suppose angle ABD equals angle BAD. Then in triangle ABD, since the base angles are equal, the sides opposite them are equal, so BD = DA. [1.6] But DA = DC since D bisects AC. Therefore BD = DA = DC. Let E coincide with D. Then EA = EB = EC, and E is equidistant from A, B, and C.

**Step 7.** Case (ii): Suppose angle ABD is greater than angle BAD. At point A on the straight line AB, construct angle BAE equal to angle ABD, with E on the line BD between D and B. [1.23, P1] In triangle ABE, since angle BAE equals angle ABE, the sides opposite them are equal, so AE = BE. [1.6]

**Step 8.** Now in triangles ADE and CDE: AD = DC (since D bisects AC), DE is common, and angle ADE = angle CDE (both are right angles, since DB is perpendicular to AC). Therefore by the side-angle-side criterion, triangles ADE and CDE are congruent, and in particular AE = CE. [1.4]

**Step 9.** Thus in Case (ii), AE = BE = CE, so E is equidistant from A, B, and C.

**Step 10.** Case (iii): Suppose angle ABD is less than angle BAD. At point A on the straight line AB, construct angle BAE equal to angle ABD, with E on the line BD produced beyond D (on the opposite side of AC from B). [1.23, P1] In triangle ABE, since angle BAE equals angle ABE, the sides opposite them are equal, so AE = BE. [1.6]

**Step 11.** In triangles ADE and CDE: AD = DC (since D bisects AC), DE is common, and angle ADE = angle CDE (both are right angles, since the line through D perpendicular to AC makes right angles on both sides). Therefore by the side-angle-side criterion, triangles ADE and CDE are congruent, and AE = CE. [1.4]

**Step 12.** Thus in Case (iii), AE = BE = CE, so E is equidistant from A, B, and C.

**Step 13.** In all three cases, we have found a point E such that EA = EB = EC. With centre E and radius EA, describe a circle. [P3] Since EA = EB = EC, this circle passes through all three points A, B, and C. [D1.15]

**Step 14.** Now the given segment ABC is part of some circle; call it the original circle. The original circle passes through A and C (the endpoints of the base of the segment) and through B (a point on the arc). The newly constructed circle with centre E and radius EA also passes through A, B, and C.

**Step 15.** If the constructed circle were different from the original circle, then two distinct circles would have three common points A, B, and C. But a circle does not cut another circle at more than two points. [3.10] Since the two circles share three points, they cannot be distinct. Therefore the constructed circle is the same as the original circle.

**Step 16.** Therefore the circle with centre E and radius EA is the complete circle of which the given segment ABC is a segment. The complete circle has been described from the given segment, which is what was required to do.

**USED:** 1.10, 1.11, 1.23, 1.4, 1.6, 3.10, D1.15, D3.6, P1, P3
**Human refs (from References field):** 1.6, 3.9
**Jaccard:** 0.091 — AI adds ['1.10', '1.11', '1.23', '1.4', '3.10', 'D1.15', 'D3.6', 'P1', 'P3']; Human adds ['3.9']

#### 几何检查报告原文（Run C）

### 3.25 — Cases ii/iii position swap (Fixable)

**Contradictory steps**: Step 7, Step 10

**Spatial claim 1** (Step 7): In Case (ii) where angle ABD > angle BAD, E lies on line BD between D and B (on the same side of AC as B)
  - Required by: Determines the geometric configuration for the SAS congruence in Step 8 and establishes E as center inside the arc

**Spatial claim 2** (Step 10): In Case (iii) where angle ABD < angle BAD, E lies on line BD produced beyond D on the opposite side of AC from B
  - Required by: Determines the geometric configuration for the SAS congruence in Step 11 and establishes E as center outside the arc

**Contradiction**: The positions of E in Cases (ii) and (iii) are swapped. Coordinate verification: with A=(0,0), C=(2,0), D=(1,0), B=(1,h), in Case (ii) (h<1, angle ABD > angle BAD), constructing angle BAE = angle ABD at A forces the ray AE below AC, placing E on BD extended beyond D at (1,-0.75) for h=0.5 -- not between D and B as claimed. In Case (iii) (h>1, angle ABD < angle BAD), the construction places E between D and B at (1,0.75) for h=2 -- not beyond D as claimed. Heath confirms: Case (ii) has center outside the segment (less than semicircle), Case (iii) has center within the segment (greater than semicircle). The AI proof reverses these positions.

**Fixable**: True
  - Swap the position descriptions between Cases (ii) and (iii). In Case (ii) (angle ABD > angle BAD, segment less than semicircle), E should be on BD produced beyond D on the opposite side of AC from B. In Case (iii) (angle ABD < angle BAD, segment greater than semicircle), E should be between D and B within the segment. The downstream SAS congruence arguments are valid regardless of E's position because DE is perpendicular to AC in either direction, so the proof conclusions are correct despite the spatial error.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-3: Proposition 4.15（Run A）

#### AI 证明原文（Run A）

## Proposition 4.15
**Statement:** In a given circle to inscribe an equilateral and equiangular hexagon.

**Step 1.** Let ABCDEF be the given circle with centre G. Draw a diameter AD of the circle [D1.17].

**Step 2.** With centre D and distance DG, describe a circle GCH [P3]. With centre A and distance AG, describe a circle GFK [P3].

**Step 3.** Since G is the centre of circle ABCDEF, GD equals GC (both are radii) [D1.15]. Since D is the centre of circle GCH, DC equals DG. Therefore GD, DC, and GC are all equal to one another, and triangle GCD is equilateral [D1.20]. Hence angle CGD is one-third of two right angles, that is, one-third of the sum of the angles of triangle GCD [1.32].

**Step 4.** By the same reasoning, since GD equals GE (radii of circle ABCDEF) [D1.15] and DE equals DG (radii of circle GCH), triangle GDE is equilateral [D1.20]. Hence angle DGE is also one-third of two right angles [1.32].

**Step 5.** Since AGD is a straight line (being a diameter), angle AGC plus angle CGD plus angle DGE plus angle EGA equals two straight angles, but angles CGD and DGE together equal the angles on one side. More precisely, angle CGE equals angle CGD plus angle DGE, and since AD is a straight line, angles AGA on the side containing C and E sum as follows: angle AGC plus angle CGD plus angle DGE equals two right angles [1.13]. Since angle CGD equals one-third of two right angles and angle DGE equals one-third of two right angles, angle AGE equals two right angles minus two-thirds of two right angles, which is one-third of two right angles [CN3].

**Step 6.** By the same reasoning on the other side of diameter AD: since GA equals GB (radii) [D1.15] and AB equals AG (radii of circle GFK), triangle GAB is equilateral [D1.20], and angle AGB is one-third of two right angles [1.32]. Since GA equals GF (radii) [D1.15] and AF equals AG (radii of circle GFK), triangle GAF is equilateral [D1.20], and angle AGF is one-third of two right angles [1.32]. Since AD is a straight line, angle AGB plus angle BGD equals two right angles [1.13]. But angle AGB equals one-third of two right angles, so angle BGD equals two right angles minus one-third of two right angles. Now angle BGD equals angle BGC plus angle CGD. Since angle CGD equals one-third of two right angles, angle BGC equals two right angles minus two-thirds of two right angles, which is one-third of two right angles [CN3].

**Step 7.** Similarly, since AD is a straight line, angle AGF plus angle FGD equals two right angles [1.13]. Angle AGF equals one-third of two right angles, so angle FGD equals two right angles minus one-third of two right angles. Now angle FGD equals angle FGE plus angle EGD. Since angle EGD equals one-third of two right angles, angle FGE equals two right angles minus two-thirds of two right angles, which is one-third of two right angles [CN3].

**Step 8.** Therefore the six central angles AGB, BGC, CGD, DGE, EGF, and FGA are all equal, each being one-third of two right angles. Since equal central angles stand on equal arcs [3.26], the six arcs AB, BC, CD, DE, EF, and FA are all equal to one another.

**Step 9.** Since the six arcs are equal, the six chords AB, BC, CD, DE, EF, and FA are also equal to one another [3.29]. Therefore the hexagon ABCDEF is equilateral.

**Step 10.** Since equal arcs are cut off, the remaining arcs on which the inscribed angles stand are also equal. Specifically, each interior angle of the hexagon, for instance angle FAB, is an angle inscribed in the circle standing on arc BCDEF, which consists of five of the six equal arcs. Since each interior angle stands on an arc equal to five-sixths of the whole circumference, and equal arcs subtend equal inscribed angles [3.27], all six interior angles are equal to one another. Therefore the hexagon ABCDEF is equiangular.

**Step 11.** Therefore in the given circle an equilateral and equiangular hexagon has been inscribed, which is what was required [D4.3].

**USED:** 1.13, 1.32, 3.26, 3.27, 3.29, CN3, D1.15, D1.17, D1.20, D4.3, P3
**Human refs (from References field):** 1.15, 1.32, 1.5, 3.26, 3.27, 3.29
**Jaccard:** 0.308 — AI adds ['1.13', 'CN3', 'D1.15', 'D1.17', 'D1.20', 'D4.3', 'P3']; Human adds ['1.15', '1.5']

#### 几何检查报告原文（Run A）

#### Proposition 4.15

**Contradictory steps**: Step 2-4 (construction), Step 5

**Spatial claim 1** (Steps 2-4): C and E are the two intersection points of circle GCH (centered at D, radius DG) with the main circle, placed symmetrically on opposite sides of diameter AD. C is above AD and E is below AD.
  - Required by: Construction via Postulate 3 and the equilateral triangle arguments in Steps 3-4

**Spatial claim 2** (Step 5): Angles AGC, CGD, and DGE are all on one side of line AD (the side containing C and E), so by I.13 they sum to 180 degrees. This implies angle AGE = 60 degrees.
  - Required by: Application of I.13 in Step 5 to derive angle AGE

**Contradiction**: C is above diameter AD and E is below it (from the symmetric construction). Step 5 claims angles AGC + CGD + DGE are all on one side of line AD and sum to 180 degrees by I.13. But angle AGC + angle CGD = 120 + 60 = 180 degrees accounts for the entire upper side, while angle DGE = 60 degrees is on the lower side. The three-angle sum is actually 240 degrees, not 180 degrees. The correct angle AGE is 120 degrees (spanning two hexagonal arcs A-F-E), not 60 degrees as claimed. The erroneous Step 5 conclusion is never used in subsequent steps — Steps 6-7 independently and correctly derive all six central angles — so the proof's final result is correct despite this error.

**Fixable**: True
  - Step 5 is entirely unnecessary and should be removed. Steps 3, 4, 6, and 7 independently establish all six central angles (CGD, DGE, AGB, AGF, BGC, FGE) as 60 degrees using correct I.13 applications. Alternatively, Step 5 could be rewritten to correctly apply I.13 separately to each side: on the upper side AGC + CGD = 180 giving AGC = 120, and on the lower side DGE + EGA = 180 giving EGA = 120. But since these intermediate values are not needed for the proof, deletion is the simplest fix.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-4: Proposition 6.15（Run A）

#### AI 证明原文（Run A）

## Proposition 6.15
**Statement:** In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal.

**Step 1.** Let ABC and ADE be two equal triangles having angle BAC equal to angle DAE. We are to show that the sides about the equal angles are reciprocally proportional, namely that CA:AD = EA:AB; and conversely.

**Step 2.** Place the two triangles so that CA and AD are in a straight line, with the equal angles at vertex A. Since angle BAC equals angle DAE and CA, AD are in a straight line, we have angle BAC + angle CAD equal to two right angles by [1.13]. Therefore angle DAE + angle CAD also equals two right angles, and so EA and AC are in a straight line by [1.14].

**Step 3.** Join BE by [P1].

**Step 4.** Triangles ABC and ABE share vertex B, and their bases CA and AE lie on the same straight line CE. Hence they are under the same height. By [6.1], triangle ABC is to triangle ABE as CA is to AE.

**Step 5.** Triangles ABE and ADE share vertex E, and their bases BA and AD lie on the same straight line BD. Hence they are under the same height. By [6.1], triangle ABE is to triangle ADE as BA is to AD.

**Step 6.** Since triangle ABC equals triangle ADE (given), triangle ABC has to triangle ABE the same ratio that triangle ADE has to triangle ABE by [5.7].

**Step 7.** From Step 4, triangle ABC : triangle ABE = CA : AE. From Steps 5 and 6, triangle ADE : triangle ABE = BA : AD, so triangle ABC : triangle ABE = BA : AD. But triangle ABC : triangle ABE = CA : AE from Step 4. Therefore CA : AE = BA : AD.

**Step 8.** By alternando [5.16], CA : BA = AE : AD, which rearranged gives CA : AD = AE : BA. Thus the sides about the equal angles are reciprocally proportional.

**Step 9.** [Converse] Now let triangles ABC and ADE have angle BAC equal to angle DAE, and let the sides about the equal angles be reciprocally proportional, so that CA : AD = EA : AB. We are to show that triangle ABC equals triangle ADE.

**Step 10.** Place the triangles as before so that CA and AD are in a straight line and EA and AC are in a straight line (by the same reasoning from Steps 1-2 using [1.13] and [1.14]). Join BE by [P1].

**Step 11.** Since CA : AD = EA : AB (given), and also CA : AE = triangle ABC : triangle ABE by [6.1] (Step 4), and BA : AD = triangle ABE : triangle ADE by [6.1] (Step 5), we need to connect these.

**Step 12.** From the given proportion CA : AD = EA : AB, by alternando [5.16] we get CA : EA = AD : AB, that is, CA : AE = AD : BA. Inverting the second ratio by [5.7], CA : AE = AD : BA means CA : AE = AD : BA.

**Step 13.** From Step 4, CA : AE = triangle ABC : triangle ABE. From Step 5, BA : AD = triangle ABE : triangle ADE, so by inversion [5.7], AD : BA = triangle ADE : triangle ABE. Since CA : AE = AD : BA (Step 12), we have triangle ABC : triangle ABE = triangle ADE : triangle ABE.

**Step 14.** Since triangles ABC and ADE have the same ratio to triangle ABE, triangle ABC equals triangle ADE by [5.9].

**Step 15.** Therefore, in equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle and in which the sides about the equal angles are reciprocally proportional are equal. Q.E.D.

**USED:** 1.13, 1.14, 5.16, 5.7, 5.9, 6.1, P1
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.500 — AI adds ['1.13', '5.16', 'P1']; Human adds ['5.11']

#### 几何检查报告原文（Run A）

#### Proposition 6.15

**Contradictory steps**: Step 2, Step 5

**Spatial claim 1** (Step 2): EA and AC are in a straight line (E-A-C collinear). Combined with the construction C-A-D collinear, this forces E, C, A, D all onto one line, making triangle ADE degenerate (zero area).
  - Required by: Step 4 application of 6.1 (triangles ABC and ABE with bases on line CE)

**Spatial claim 2** (Step 5): BA and AD lie on the same straight line BD (B-A-D collinear). Combined with the construction C-A-D collinear, this forces B onto line CD, making triangle ABC degenerate (zero area).
  - Required by: Step 5 application of 6.1 (triangles ABE and ADE with bases on line BD)

**Contradiction**: The AI's Step 2 incorrectly concludes EA and AC are in a straight line; the correct conclusion from 1.13 and 1.14 (as Heath shows) is that EA and AB are in a straight line. The AI's wrong collinearity (E-A-C), combined with the construction (C-A-D collinear), forces all of E, C, A, D onto one line, making triangle ADE degenerate. Step 5 then requires B-A-D collinear, which combined with C-A-D collinear forces B onto line CD, making triangle ABC degenerate. Both triangles becoming degenerate contradicts the premise of two proper triangles with equal positive area. In the correct geometry (E-A-B collinear), the AI's reference triangle ABE is itself degenerate, so the entire proof strategy of using triangle ABE as a ratio intermediary via 6.1 is fundamentally unsound.

**Fixable**: True
  - Use the correct collinearity E-A-B (not E-A-C) from 1.14, then adopt Heath's approach: join BD and use triangle BAD as the reference triangle. With C-A-D collinear, 6.1 gives CAB:BAD = CA:AD (shared vertex B, bases on line CD). With E-A-B collinear, 6.1 gives EAD:BAD = EA:AB (shared vertex D, bases on line EB). This avoids the degenerate triangle ABE entirely.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-5: Proposition 10.29（Run C）

#### AI 证明原文（Run C）

## Proposition 10.29
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Let A be a rational straight line set out. [D10.1.3]

**Step 2.** Take two square numbers whose difference is not a square number. Let these be 4 and 1, since 4 - 1 = 3 is not a square number.

**Step 3.** Bisect A to obtain a straight line C equal to half of A, so that A = C + C. [1.10]

**Step 4.** Since A is the double of C, by 2.4 the square on A equals the square on C plus the square on C plus twice the rectangle contained by C and C, that is, sq(A) = 4 * sq(C). Thus sq(A) : sq(C) = 4 : 1. Since 4 and 1 are both square numbers, by 10.9 A and C are commensurable in length. Since A is rational and C is commensurable in length with A, C is also rational. [2.4, 10.9, D10.1.3]

**Step 5.** Now construct a straight line B such that sq(B) = sq(A) - sq(C). To do this, construct a right angle at a point [1.11], along one arm mark off a segment equal to C [1.3], and with center at the vertex draw a circle with radius equal to A [P3]. Since sq(A) = 4 * sq(C) and sq(C) is less than sq(A) [CN5], A is greater than C, so the circle meets the other arm. Let B be the segment from the vertex to this intersection. By 1.47, in the resulting right triangle with hypotenuse A and one leg C, we have sq(A) = sq(B) + sq(C), and therefore sq(B) = sq(A) - sq(C). [1.11, 1.3, P3, CN5, 1.47]

**Step 6.** Since sq(A) = 4 * sq(C) and sq(B) = sq(A) - sq(C) = 4 * sq(C) - sq(C) = 3 * sq(C) [CN3], both sq(A) and sq(B) are multiples of sq(C). Therefore sq(A) : sq(B) = 4 : 3, which is a ratio of a number to a number. By 10.6, sq(A) and sq(B) are commensurable, so A and B are commensurable in square. [CN3, 10.6, D10.1.2]

**Step 7.** However, 4 is a square number and 3 is not a square number, so 4 : 3 is not a ratio of a square number to a square number. By 10.9, A and B are incommensurable in length. [10.9]

**Step 8.** Since A and B are commensurable in square (Step 6) but incommensurable in length (Step 7), A and B are commensurable in square only. [D10.1.2]

**Step 9.** Since A is rational and B is commensurable in square with A, B is rational. [D10.1.3]

**Step 10.** From Step 5, sq(A) - sq(B) = sq(C), and from Step 4, C is commensurable in length with A. Since sq(A) > sq(B) (as the ratio sq(A) : sq(B) = 4 : 3), A is the greater and B is the less. Therefore the square on the greater exceeds the square on the less by the square on a straight line C that is commensurable in length with the greater.

**Step 11.** Therefore two rational straight lines A and B have been found, commensurable in square only, such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater. Q.E.F.

**USED:** 1.10, 1.11, 1.3, 1.47, 10.6, 10.9, 2.4, CN3, CN5, D10.1.2, D10.1.3, P3
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19, D10.1.4
**Jaccard:** 0.200 — AI adds ['1.10', '1.11', '1.3', '2.4', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3', 'P3']; Human adds ['3.31', '5.19', 'D10.1.4']

#### 几何检查报告原文（Run C）

### 10.29 — Circle centered at wrong point (Fixable)

**Contradictory steps**: Step 5 (circle construction: center at vertex V, radius A, giving B = VQ = A), Step 5 (Pythagorean application: sq(A) = sq(B) + sq(C) with C > 0, requiring B < A)

**Spatial claim 1** (Step 5): Circle centered at vertex V with radius A meets the other arm at Q, making B = VQ = A
  - Required by: Construction of B via the circle intersection with the other arm of the right angle

**Spatial claim 2** (Step 5): In right triangle VPQ with right angle at V, the hypotenuse is A and one leg is C = A/2 > 0, so sq(A) = sq(B) + sq(C), requiring B = sqrt(A^2 - C^2) < A
  - Required by: Application of 1.47 to derive sq(B) = sq(A) - sq(C) for subsequent algebraic steps

**Contradiction**: The circle centered at V with radius A places Q at distance A from V on the other arm, so B = VQ = A. But the Pythagorean relation sq(A) = sq(B) + sq(C) with C = A/2 > 0 requires B = sqrt(A^2 - A^2/4) = A*sqrt(3)/2, which is strictly less than A. The construction forces B = A while the Pythagorean theorem application requires B < A. Substituting B = A into sq(A) = sq(B) + sq(C) gives sq(C) = 0, contradicting C = A/2 > 0 from Step 3. The circle should be centered at P (the endpoint of C on the arm) rather than at V (the vertex), so that PQ = A is the hypotenuse and VQ = B is the unknown leg.

**Fixable**: True
  - Center the circle at point P (the endpoint of segment C on one arm) instead of at V (the vertex of the right angle). Then PQ = A serves as the hypotenuse, the right angle remains at V, and 1.47 gives sq(A) = sq(C) + sq(B), yielding sq(B) = sq(A) - sq(C) as needed. Alternatively, use Heath's semicircle construction with III.31 (angle in semicircle is right).

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-6: Proposition 11.29（Run A）

#### AI 证明原文（Run A）

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let the parallelepipedal solids CM and CN be on the same base AB and of the same height, and let the extremities of their edges which stand up, namely the points E, F, G, H and E', F', G', H', lie on the same straight lines EE' and FF' respectively. Specifically, let solid CM have base ABCD with top face EFGH, and solid CN have the same base ABCD with top face E'F'G'H', where AE, BF, CG, DH are the standing edges of the first solid, and AE', BF', CG', DH' are the standing edges of the second. The points E, E' lie on one straight line and H, H' lie on its continuation (or the same line), while F, F' and G, G' lie on another straight line.

**Step 2.** Since CM is a parallelepiped, the face AE is a parallelogram, so AE is parallel to and equal to DH, and similarly BF is parallel to and equal to CG, by 11.24. Likewise, since CN is a parallelepiped, AE' is parallel to and equal to DH', and BF' is parallel to and equal to CG', by 11.24.

**Step 3.** Since AE is parallel to DH (both being edges standing up from the same base and part of a parallelepiped), and the extremities E, H lie on straight lines with E', H' respectively, the quadrilateral EE'H'H is a parallelogram, because EH is parallel to E'H' (both being sides of parallelogram top faces EFGH and E'F'G'H' opposite to the common direction) and EE' is parallel to HH' since AE is parallel to DH and AE' is parallel to DH'. By 1.34, EE' equals HH' and EH equals E'H'.

**Step 4.** Similarly, FF'G'G is a parallelogram, with FF' equal to GG', by the same reasoning using 1.34.

**Step 5.** Since EE' is equal to HH' and FF' is equal to GG', and EF is equal to HG (as opposite sides of parallelogram EFGH, by 1.34), and E'F' is equal to H'G' (as opposite sides of parallelogram E'F'G'H', by 1.34), the quadrilaterals EFGE' (more precisely the faces of the auxiliary solids) form parallelograms.

**Step 6.** Consider now the solid with vertices E, F, G, H, E', F', G', H'. The faces EE'F'F, HH'G'G, EE'H'H, FF'G'G, EFGH, and E'F'G'H' are all parallelograms (shown in Steps 3, 4, and by 11.24 applied to the original solids). Therefore this solid EE'FF'GG'HH' is itself a parallelepiped, by D11.13 and the characterization in 11.24.

**Step 7.** Now the solid CM (which is ABCD-EFGH) can be decomposed as follows. The plane through the diagonal EG of the top face EFGH and the corresponding diagonal of the base bisects the parallelepiped CM, by 11.28. Similarly, solid CN (which is ABCD-E'F'G'H') is bisected by the plane through its corresponding diagonals.

**Step 8.** Consider the auxiliary parallelepiped with top face EE'F'F and bottom face HH'G'G (the solid formed by the region between the two top faces and the standing edges). By 11.28, this solid is bisected by the plane through its diagonals.

**Step 9.** Now observe that solid CM equals the solid ABCD-EFGH. We add and subtract the same auxiliary pieces to relate CM and CN. The solid with base ABFE and top AE'BF' (a prism-shaped piece) is common to both solids CM and CN, since both share the base AB and the edges AE, BF (for CM) overlap with AE', BF' (for CN) in a common region.

**Step 10.** More precisely, the solid CM is composed of the prism on triangle ABE (extending to the corresponding upper region) and complementary pieces, and CN is composed similarly. Consider the solid whose base is the parallelogram ABFE and whose top is ABF'E'. The face ABFE is a parallelogram (since AE is parallel to BF by 11.24), and similarly ABF'E' is a parallelogram. The solid ABFE-E'F' forms part of both decompositions.

**Step 11.** To make the argument precise: solid CM can be written as the sum of (i) the solid on base ABFE with top ABF'E' and (ii) the solid on the remaining part of the base with the corresponding top shifted by EE'. Similarly solid CN consists of the same solid (i) and a complementary piece. But these complementary pieces are equal because the parallelogram EE'H'H equals FF'G'G (both being faces of the auxiliary parallelepiped from Step 6), and the heights are equal.

**Step 12.** By the key argument: since EFGH and E'F'G'H' are both parallelograms on the same parallel lines (EE' and HH' on one side, FF' and GG' on the other), parallelogram EFGH is equal to parallelogram E'F'G'H', by 1.35 (parallelograms on the same base and between the same parallels are equal — applied in the plane of the top faces, where EH = E'H' and EF = E'F' as bases between the same parallels).

**Step 13.** Now the solid CM has base ABCD and top EFGH with standing edges AE, BF, CG, DH. The solid CN has the same base ABCD and top E'F'G'H' with standing edges AE', BF', CG', DH'. Consider the prism formed by triangle AEE' extended along the parallelepiped to the opposite face triangle DHH'. This prism equals the prism formed by triangle BFF' extended to CGG', because AE equals BF, AE' equals BF', and EE' equals FF' (by 1.34 applied to the respective parallelogram faces), and the triangles are congruent by 1.8, with equal heights.

**Step 14.** Solid CM equals the auxiliary solid (with top face EE'F'F and base HH'G'G, the parallelepiped from Step 6) plus the solid CN, minus two prisms. But equally, solid CN equals the same auxiliary solid plus solid CM minus the same two prisms. By the symmetry of the decomposition, we can argue directly.

**Step 15.** To complete the proof cleanly: the solid CM consists of the solid with edges AB, CD on the base and EF, GH on top, together with prisms on the sides. Specifically, CM = solid(ABF'E'-DCG'H') + prism(E,E',F,F' extended to H,H',G,G') applied to one side. And CN = solid(ABF'E'-DCG'H') + prism on the other side. But these prisms are equal because their triangular cross-sections EE'F' and HH'G' are congruent (by 1.8, since EE' = HH', EF = HG from 1.34, and E'F' = H'G' from 1.34) and they have equal heights (the distance between the parallel planes of ABCD and EFGH, which equals the distance to E'F'G'H' since the solids have the same height).

**Step 16.** More directly: solid CM is the sum of solid CN, plus the prism on one side, minus the prism on the other side. Since these two prisms are equal (as shown in Step 15), adding one and subtracting an equal one leaves the solid unchanged. Therefore solid CM equals solid CN.

**Step 17.** Therefore parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another. Q.E.D.

**USED:** 1.34, 1.35, 1.8, 11.24, 11.28, CN2, CN3, D11.13
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.200 — AI adds ['1.35', '11.24', '11.28', 'CN2', 'CN3', 'D11.13']; Human adds ['1.36', '1.4']

#### 几何检查报告原文（Run A）

#### Proposition 11.29

**Contradictory steps**: Step 1, Step 3, Step 6

**Spatial claim 1** (Step 1): E, E', H, H' all lie on one straight line. This is the proposition's given condition: the extremities of the standing edges lie on two straight lines, and the proof assigns E, E', H, H' to one of them.
  - Required by: Setup of the proposition's geometric condition

**Spatial claim 2** (Step 3 and Step 6): EE'H'H is a parallelogram (Step 3), and the solid E,F,G,H,E',F',G',H' is a parallelepiped with all six faces being parallelograms (Step 6). Both claims require E,E',H,H' to be non-collinear so they form a proper 2D quadrilateral face.
  - Required by: Steps 3-4 use I.34 on these 'parallelograms'; Step 6 classifies the solid as a parallelepiped; Step 8 applies XI.28 (bisection by diagonal plane) to this 'parallelepiped'

**Contradiction**: The proof establishes in Step 1 that E, E', H, H' are collinear (all on one straight line), as required by the proposition's condition. In a parallelepiped, standing edges are translates of a single vector, so E=A+v1, H=D+v1, E'=A+v2, H'=D+v2. The collinearity condition forces v1-v2 to be parallel to D-A, placing all four points on one line. But four collinear points cannot form a parallelogram (which requires a 2D quadrilateral). Therefore EE'H'H is a degenerate line segment with zero area, not a parallelogram. Similarly FF'G'G is degenerate. Consequently, the solid in Step 6 has two degenerate 'faces' (zero-area line segments) and cannot be a parallelepiped, invalidating the application of XI.28 in Step 8. The proof conflates a degenerate configuration with a proper parallelepiped.

**Fixable**: True
  - Heath's proof avoids this error entirely by never constructing the auxiliary parallelepiped. Instead, Heath directly shows that the complementary prisms (triangular prisms formed by the difference between the two solids) are equal, using I.8, I.4, I.34, and I.36. The AI proof could be repaired by following this direct prism decomposition approach, or alternatively by correcting the point grouping so that the two straight lines contain {E,F,E',F'} and {H,G,H',G'} respectively (tops from adjacent base vertices on the same line), which would make EE'H'H a proper non-degenerate parallelogram.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-7: Proposition 11.29（Run B）

#### AI 证明原文（Run B）

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let there be two parallelepipedal solids CM and CN on the same base ABCD and of the same height, where CM has base ABCD and top face EFGH (with AE, BF, CG, DH as the sides which stand up), and CN has the same base ABCD and top face E'F'G'H' (with AE', BF', CG', DH' as the sides which stand up). Suppose the extremities of the sides which stand up lie on the same straight lines, that is, E, F, E', F' lie on one straight line EF', and H, G, H', G' lie on another straight line HG'.

**Step 2.** Since CM is a parallelepiped, its opposite faces are equal and parallelogrammic, by 11.24. Therefore the top face EFGH is a parallelogram equal to the base ABCD, and similarly each pair of opposite faces consists of equal parallelograms. Likewise for CN: the top face E'F'G'H' is a parallelogram equal to the base ABCD.

**Step 3.** Since EFGH is a parallelogram, EH is equal and parallel to FG. Since E'F'G'H' is a parallelogram, E'H' is equal and parallel to F'G', by 1.34. Moreover, since EH and E'H' are both equal and parallel to the same line DC (being opposite sides of the parallelogram faces of the respective solids that share the base side DC), it follows that EH is equal and parallel to E'H', by 11.9 and 1.33.

**Step 4.** Since E, E' lie on the same straight line and H, H' lie on the same straight line, and EH is equal and parallel to E'H', the figure EHH'E' is a parallelogram, by 1.33. Similarly, since FG is equal and parallel to F'G' (both being equal and parallel to BC), the figure FGG'F' is a parallelogram.

**Step 5.** Now consider the solid figure bounded by the two parallelograms EFGH and E'F'G'H' as top and bottom, and by the faces EFE'F' (which lies in a plane since E, F, E', F' are on the same straight line, making EFE' a degenerate face, but EE'F'F is a parallelogram since EF is parallel to E'F' and EE' connects them), EHH'E', FGG'F', and HGG'H'. This is the parallelepiped with base EFGH and opposite face E'F'G'H'.

**Step 6.** Consider the diagonal plane through HF and H'F' in the parallelepiped CM (base ABCD, top EFGH). By 11.28, the plane BDHF divides CM into two equal prisms: prism with triangle ABF on one base and triangle DEH on the other, and prism with triangle BCF on one base and triangle DCH on the other (more precisely, the prism ABFE-DCGH is bisected into two triangular prisms by the diagonal plane). That is, the prism contained by the triangle ABF and the triangle DCG equals the prism contained by the triangle ADE and the triangle BCG, and each is half of CM.

**Step 7.** Similarly, by 11.28, the diagonal plane through the parallelepiped CN (base ABCD, top E'F'G'H') bisects CN into two equal prisms.

**Step 8.** Now consider the prism whose base is triangle AEE' (the triangle formed at vertex A between the two standing edges AE and AE') and which extends to the triangle DHH' at the other end. And consider the prism whose base is triangle BFF' and which extends to triangle CGG'. Since AE is parallel to DH (as sides of the parallelogram ADHE), and AE' is parallel to DH' (as sides of the parallelogram ADH'E'), and EE' lies along the same line as HH', the prism on AEE'-DHH' is properly formed.

**Step 9.** The prism with triangle AEE' as base and triangle DHH' as the corresponding face has AE = DH, AE' = DH', and EE' = HH' (since AEHD and AE'H'D are parallelograms by 11.24 and 1.34, and EHH'E' is a parallelogram by Step 4). By 1.34 the opposite sides of these parallelograms are equal. Therefore triangle AEE' equals triangle DHH' and the prism is properly defined.

**Step 10.** Similarly, the prism on triangle BFF' and triangle CGG' is properly formed, with BF = CG, BF' = CG', and FF' = GG'.

**Step 11.** Now the solid CM (parallelepiped ABCD-EFGH) can be regarded as composed of: the solid ABCD-E'F'G'H' (which is CN) plus the prism on AEE'-DHH', minus the prism on BFF'-CGG'. But we can also see that the solid CM equals the solid ABCD-E'F'G'H' by the following argument using 11.28.

**Step 12.** Apply 11.28 to CM: the plane through the diagonal AF of face ABFE and the diagonal DG of the opposite face DCHG bisects CM into two equal prisms. Call these prisms P1 (containing edge AD) and P2 (containing edge BC). So CM = P1 + P2, and P1 = P2.

**Step 13.** Apply 11.28 to CN: the plane through the diagonal AF' of face ABF'E' and the diagonal DG' of the opposite face DCG'H' bisects CN into two equal prisms. Call these Q1 (containing edge AD) and Q2 (containing edge BC). So CN = Q1 + Q2, and Q1 = Q2.

**Step 14.** Consider prism P1 (from CM). It is the prism with triangular cross-section: on the side of AD, its base triangle has vertices A, E, the foot on line EF at B-side, and extends from AD to... Let us reconsider the decomposition more carefully.

**Step 15.** The parallelepiped CM has top face EFGH with E above A, F above B, G above C, H above D. The diagonal plane through BF, DH (connecting edge BF to edge DH, passing through diagonal BD of the base and diagonal FH of the top) divides CM into two prisms by 11.28: Prism-I = ABD-EFH (with triangular faces ABD and EFH) and Prism-II = BCD-FGH.

**Step 16.** Similarly, CN has top face E'F'G'H'. The diagonal plane through BF', DH' divides CN into two prisms by 11.28: Prism-III = ABD-E'F'H' and Prism-IV = BCD-F'G'H'.

**Step 17.** Now consider the auxiliary solid ABCD-EF'G'H, which shares the base ABCD with both CM and CN. Its standing edges are AE, BF', CG', DH. Since AE is parallel to DH (they stand on AD and connect to EH, which is parallel to AD by 11.24 and 1.34), and BF' is parallel to CG' (they stand on BC and connect to F'G', which is parallel to BC), this solid is also a parallelepiped.

**Step 18.** The diagonal plane through BF', DH divides the auxiliary solid ABCD-EF'G'H into two prisms by 11.28: Prism-V = ABD-EF'H and Prism-VI = BCD-F'G'H.

**Step 19.** Now compare Prism-I (ABD-EFH) with Prism-V (ABD-EF'H). They share the common base triangle ABD and the common vertex E (above A) and H (above D). The only difference is F versus F' above B, where F and F' both lie on the same straight line. The prism ABD-EFH has as one parallelogram face the figure ABFE, while ABD-EF'H has ABFE' replaced by ABF'E. However, both prisms have the same triangular base ABD, the same edge AE and DH, and BF vs BF' along the same line. By 1.35, parallelograms on the same base and between the same parallels are equal: ABFE and ABF'E are on the same base AB and between the same parallel lines (since E, F, F' and E all have their extremities on the same lines). Similarly DHGE and DHG'E... 

**Step 20.** Let us use a more direct approach. Prism-I has base ABD and opposite face EFH. Prism-V has base ABD and opposite face EF'H. Both base triangles are identical (ABD). The opposite triangles EFH and EF'H share vertices E and H, while F and F' lie on the same straight line (by hypothesis, the extremities F and F' are on the same line). Since EFH and EF'H are triangles on the same base EH and between the same parallel lines (the line through EH and the line through FF', noting FG is parallel to EH), by 1.37 (triangles on the same base and between the same parallels are equal), triangle EFH equals triangle EF'H.

**Step 21.** Moreover, Prism-I and Prism-V have equal bases (both ABD), equal opposite faces (EFH = EF'H by Step 20), and the same height (the perpendicular distance from the plane of ABCD to the plane through EH, which is the same for both since F and F' are at the same height). Since the prisms are contained between the same parallel planes (the base plane through ABCD and the top plane through E, H and the line FF'), by 11.24 and the definition of equal prisms, Prism-I = Prism-V.

**Step 22.** Now compare Prism-II (BCD-FGH) with Prism-VI (BCD-F'G'H). They share the common base triangle BCD. The opposite faces are FGH and F'G'H. Since H and H' lie on the same straight line and G, G' lie on the same straight line, and F, F' lie on the same straight line, the triangle FGH and triangle F'G'H share vertex H. But we need to compare triangles FGH and F'G'H. These triangles are on the same base FG... Actually, they share vertex H, and F, F' lie on the same line while G, G' lie on the same line. Since FG is parallel to HH'... Let us reconsider.

**Step 23.** Reconsider: Prism-II = BCD-FGH and Prism-IV = BCD-F'G'H'. These prisms both have base triangle BCD. The triangle FGH has F above B, G above C, H above D. The triangle F'G'H' has F' above B, G' above C, H' above D. Now FG is parallel to BC (by 11.24 and 1.34) and F'G' is parallel to BC. Also GH is parallel to CD and G'H' is parallel to CD. So both triangles FGH and F'G'H' are similar and equal triangles (since FG = F'G' = BC, GH = G'H' = CD, FH = F'H' = BD, all being corresponding sides of equal parallelogram faces, by 11.24 and 1.34). Therefore triangle FGH is congruent to triangle F'G'H' by 1.8.

**Step 24.** Furthermore, both Prism-II and Prism-IV lie between the same pair of parallel planes: the plane of ABCD and the plane containing the parallel lines through FF' and GG' (and HH'). The three lateral faces of each prism are parallelograms. Since the bases are equal, the opposite faces are equal, and they lie between the same parallel planes with the same height, Prism-II = Prism-IV.

**Step 25.** Also compare Prism-VI (BCD-F'G'H) with Prism-IV (BCD-F'G'H'). They share the base BCD and the edge BF' and CG'. Prism-VI has vertex H in its top face while Prism-IV has vertex H'. Since H and H' lie on the same line as the other extremities, and G'H is parallel to G'H'... We need triangle F'G'H vs triangle F'G'H'. These share edge F'G', while H and H' lie on the same line. By 1.37, triangles on the same base F'G' between the same parallels (the line F'G' and the line HH') are equal. So triangle F'G'H = triangle F'G'H'. By the same reasoning as Step 21, Prism-VI = Prism-IV.

**Step 26.** From Step 21: Prism-I = Prism-V. Therefore CM = Prism-I + Prism-II = Prism-V + Prism-II.

**Step 27.** From Step 25: Prism-VI = Prism-IV. The auxiliary solid = Prism-V + Prism-VI = Prism-V + Prism-IV. Also CN = Prism-III + Prism-IV.

**Step 28.** We need one more relation. Compare Prism-II (BCD-FGH) and Prism-VI (BCD-F'G'H). These share base BCD. The opposite triangles are FGH and F'G'H. Triangle FGH has vertices F, G, H above B, C, D respectively. Triangle F'G'H has vertices F', G', H above B, C, D (note H, not H'). Since F, F' lie on the same line and G, G' lie on the same line, and FG is parallel to F'G' (both parallel to BC), triangle FGH and F'G'H are on the base GH (shared vertex) with F and F' on the same line. By 1.37, if we take base GH, then since F and F' lie between the same parallels as GH (namely FG parallel to a line through H and F'G' parallel to the same), the triangles FGH and F'G'H are equal in area. By the prism equality argument (same base triangle BCD, equal and similarly situated opposite triangles at the same height between the same parallel planes), Prism-II = Prism-VI.

**Step 29.** Now we can conclude. CM = Prism-I + Prism-II (by Step 15 and 11.28). And CN = Prism-III + Prism-IV (by Step 16 and 11.28). The auxiliary solid = Prism-V + Prism-VI (by Step 18 and 11.28). From Step 21, Prism-I = Prism-V. From Step 28, Prism-II = Prism-VI. Therefore CM = Prism-I + Prism-II = Prism-V + Prism-VI = auxiliary solid.

**Step 30.** By entirely symmetric reasoning (now comparing the auxiliary solid ABCD-EF'G'H with CN = ABCD-E'F'G'H'), we use the fact that E, E' lie on the same line and H, H' are endpoints with H for the auxiliary solid and H' for CN. The diagonal planes divide the auxiliary solid and CN into prisms that can be compared pairwise using 1.37 and 11.28 in the same manner as above. This gives: auxiliary solid = CN.

**Step 31.** Therefore CM = auxiliary solid = CN, by CN1. That is, the two parallelepipedal solids on the same base, of the same height, and with the extremities of their standing sides on the same straight lines, are equal to one another. Q.E.D.

**USED:** 1.33, 1.34, 1.37, 11.24, 11.28, 11.9, CN1
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.100 — AI adds ['1.33', '1.37', '11.24', '11.28', '11.9', 'CN1']; Human adds ['1.36', '1.4', '1.8']

#### 几何检查报告原文（Run B）

### Proposition 11.29

**Contradictory steps**: Step 1, Step 17

**Spatial claim 1** (Step 1): CM and CN are general parallelepipeds on base ABCD satisfying the collinearity condition. Their translation vectors v and w satisfy w = v + t*AB but are NOT required to be parallel (v not parallel to w in general).
  - Required by: The hypothesis of the proposition; establishes the generality of the configuration

**Spatial claim 2** (Step 17): The solid ABCD-EF'G'H (with standing edges AE from CM and BF' from CN) is a parallelepiped. This implicitly requires AE || BF', i.e., v || w.
  - Required by: Application of Proposition 11.28 in Step 18 to decompose the auxiliary solid into prisms, which is essential for the chain CM = auxiliary solid = CN in Steps 29-31

**Contradiction**: The auxiliary solid ABCD-EF'G'H has standing edges AE = v (from CM) and BF' = w (from CN). For it to be a parallelepiped, all six faces must be parallelograms, which requires AE || BF' (i.e., v || w). But the hypothesis only constrains w = v + t*AB (from collinearity), which does NOT imply v || w unless v happens to be parallel to AB (a degenerate case). In a general oblique parallelepiped, v is not parallel to AB, so AE is not parallel to BF', face ABF'E is not a parallelogram, and the auxiliary solid is not a parallelepiped. A concrete counterexample with v=(0.5,0,1) and w=(0.8,0,1) confirms this: both parallelepipeds satisfy all hypotheses but ABF'E has non-parallel opposite sides.

**Fixable**: True
  - Heath's proof avoids this entirely by using a direct subtraction/addition approach: showing triangles DCE = HBK (by I.8, I.4), parallelograms DG = HN (by I.36), and then adding equal prisms to reach CM = CN. The AI's strategy of constructing an auxiliary parallelepiped is fundamentally flawed because the solid ABCD-EF'G'H is not a parallelepiped in general. A correct proof must use Heath's approach or an equivalent one that does not require this false intermediate construction.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-8: Proposition 11.31（Run C）

#### AI 证明原文（Run C）

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let the parallelepipedal solids AB and CD be on equal bases, with base parallelogram EFGH of solid AB equal to base parallelogram KLMN of solid CD, and let both solids have the same height.

**Step 2.** We must show that solid AB equals solid CD.

**Step 3.** First, suppose the sides EF, KL of the bases are placed on the same straight line FKL, and the bases lie in the same plane, with the parallelograms EFGH and KLMN having EH and KN also on the same straight line. Let the standing edges of solid AB be EP, FQ, GR, HS, and those of solid CD be KT, LU, MV, NW, all having the same height.

**Step 4.** On the base EFGH, construct the parallelepiped whose standing edges are equal and parallel to KT, LU, MV, NW respectively. Call this solid AB'. Since solid AB' is on the same base EFGH as solid AB and has the same height, the extremities of their standing edges lie in the same plane. By 11.29 or 11.30 (depending on whether the extremities of the standing edges are or are not on the same straight lines), solid AB equals solid AB'.

**Step 5.** Now consider solid AB' on base EFGH with standing edges equal and parallel to KT, LU, MV, NW, and solid CD on base KLMN with standing edges KT, LU, MV, NW. Since EF is on the same straight line as KL, and EH is on the same straight line as KN, and EFGH equals KLMN as parallelograms, by 1.34 we have EF = GH, KL = MN, EH = FG (as opposite sides of parallelograms).

**Step 6.** Complete the parallelogram EKNT by joining the bases along their common line arrangement. Since EH and KN are on the same straight line, and EF and KL are on the same straight line, the figure EFGH + KLMN with the region between them forms a configuration of parallelograms on the same lines.

**Step 7.** Consider the solid on the base EKNT (the combined parallelogram region). Solid AB' has base EFGH with standing edges parallel and equal to those of CD. Solid CD has base KLMN with the same standing edges. Both AB' and CD can be related to a common solid on the combined base by adding and subtracting complementary pieces. Specifically, since the standing edges of AB' are equal and parallel to those of CD, the solid AB' together with the parallelepiped on FKLG equals the solid CD together with the parallelepiped on FKLG. This is because both combined solids form the same parallelepiped on the larger base EKNT (extending from E to K along one direction and from N to H along the other).

**Step 8.** By CN2 (if equals be added to equals, the wholes are equal), the whole solid on EKNT can be decomposed two ways. Since EFGH = KLMN (given as equal bases), and both AB' and CD are on these equal bases with identical standing edges, the complements are equal. By CN3 (if equals be subtracted from equals, the remainders are equal), solid AB' equals solid CD.

**Step 9.** From Step 4, solid AB = solid AB'. From Step 8, solid AB' = solid CD. Therefore by CN1 (things equal to the same thing are equal to one another), solid AB = solid CD.

**Step 10.** Now consider the general case where the bases are not arranged on the same straight lines. Let the two parallelepipedal solids have equal bases EFGH and KLMN in any position, with the same height. By 1.45, we can construct on a given straight line a parallelogram equal to a given rectilineal figure, and by 1.34, we know properties of parallelograms. Place the base KLMN so that side KL is on the same straight line as EF, and side KN is on the same straight line as EH. This can be done by constructing on the line EF a parallelogram equal to KLMN with an angle equal to angle FEH, using 1.42 and 1.44 (to construct a parallelogram equal to a given triangle in a given angle, and to apply a parallelogram equal to a given rectilineal figure along a given line in a given angle).

**Step 11.** With KLMN so repositioned (call the repositioned base K'L'M'N'), the solid CD can be reconstructed on this new base K'L'M'N' with the same standing edges adjusted to be parallel and equal to the originals. By 11.29 or 11.30, the reconstructed solid on K'L'M'N' equals the original solid CD (as they share the same base and height). The repositioned configuration now falls under the case handled in Steps 3 through 9.

**Step 12.** Therefore, in all cases, parallelepipedal solids on equal bases and of the same height are equal to one another. Q.E.D.

**USED:** 1.34, 1.42, 1.44, 1.45, 11.29, 11.30, CN1, CN2, CN3
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.118 — AI adds ['1.34', '1.42', '1.44', '1.45', 'CN1', 'CN2', 'CN3']; Human adds ['1.23', '1.35', '11.24', '11.25', '5.11', '5.7', '5.9', 'D11.10']

#### 几何检查报告原文（Run C）

### 11.31 — Double-collinearity forces degenerate construction (Not Fixable)

**Contradictory steps**: Step 3 (first collinearity claim), Step 3 (second collinearity claim), Step 6, Step 7

**Spatial claim 1** (Step 3): E, F, K, L are collinear (EF and KL on the same straight line), with E and K as distinct points (vertices of different parallelogram bases)
  - Required by: Steps 6-7: construction of combined parallelogram EKNT and connecting region FKLG

**Spatial claim 2** (Step 3): E, H, K, N are collinear (EH and KN on the same straight line), with EFGH a non-degenerate parallelogram (so EF and EH are not parallel, meaning the two lines l1 and l2 are distinct)
  - Required by: Steps 6-7: construction of combined parallelogram EKNT spanning both bases

**Contradiction**: Since EFGH is a non-degenerate parallelogram, its adjacent sides EF and EH are not parallel, so line l1 (through E,F,K,L) is distinct from line l2 (through E,H,K,N). Two distinct lines in a plane intersect in at most one point. E lies on both lines, making E the unique intersection. K is also claimed to lie on both lines, forcing K = E. With K = E: (1) the combined parallelogram EKNT degenerates (two vertices coincide); (2) the connecting region FKLG = FELG is not a parallelogram since FE is along l1 while FG is parallel to EH along l2; (3) the entire complement technique of Steps 6-8 breaks down. The double-collinearity configuration is geometrically impossible for distinct non-degenerate parallelogram bases.

**Fixable**: False
  - The AI proof's additive/subtractive complement technique inherently requires both pairs of adjacent sides to be collinear, which is impossible. Heath's proof avoids this by placing only one pair of sides collinear, constructing the second direction via angle construction (I.23), and using proportion theory (V.7, V.9, V.11 combined with XI.25) instead of the complement technique. The proof would need to be fundamentally restructured to follow Heath's proportion-based approach rather than the impossible complement-based approach.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-9: Proposition 11.35（Run A）

#### AI 证明原文（Run A）

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

**Step 1.** Let the two equal plane angles be angle BAC and angle EDF, situated in planes P1 and P2 respectively, with angle BAC equal to angle EDF. Let AG and DM be elevated straight lines set up at vertices A and D, making angle BAG equal to angle EDM and angle CAG equal to angle FDM. Let G be any point on AG. Make DM equal to AG by cutting off on DM (or its extension) a length equal to AG [1.3].

**Step 2.** From the elevated point G, draw GH perpendicular to plane P1 [11.11], meeting the plane at H. From the elevated point M, draw MK perpendicular to plane P2 [11.11], meeting the plane at K. Join AH and DK [P1].

**Step 3.** Since GH is at right angles to the plane P1, it makes right angles with every straight line through H lying in P1 [D11.3]. In particular, angle GHA is a right angle [D1.10]. Similarly, since MK is at right angles to plane P2, angle MKD is a right angle. All right angles are equal to one another [P4].

**Step 4.** In the plane containing G and line AB [11.2], let J be the foot of the perpendicular from G to line AB [1.12], so that angle GJA is a right angle. We show that J is also the foot of the perpendicular from H to AB: Since GH is perpendicular to plane P1 and the line HJ lies in P1 through H, angle GHJ is a right angle [D11.3]. By the Pythagorean theorem on right triangle GHJ, GH squared plus HJ squared equals GJ squared [1.47]. For any other point J-prime on AB distinct from J, angle GHJ-prime is likewise a right angle [D11.3], so GH squared plus HJ-prime squared equals GJ-prime squared [1.47]. Since angle GJA is a right angle and J-prime lies on AB, the triangle GJJ-prime has a right angle at J, giving GJ squared plus JJ-prime squared equals GJ-prime squared [1.47]. Substituting, HJ-prime squared equals HJ squared plus JJ-prime squared. By the converse of the Pythagorean theorem [1.48], angle HJJ-prime is a right angle. Since JJ-prime lies along AB, this means HJ is perpendicular to AB at J. Hence J is the foot of the perpendicular from H to line AB.

**Step 5.** By the same reasoning, let I be the foot of the perpendicular from G to line AC; then I is also the foot of the perpendicular from H to AC, with angle GIA and angle HIA both right angles. In the second configuration, let L be the foot of the perpendicular from M (and from K) to line DE, and N the foot of the perpendicular from M (and from K) to line DF, with right angles at L and N established by the same argument.

**Step 6.** In right triangles AGJ and DML: angle AJG equals angle DLM (both right angles, equal by P4), angle JAG equals angle BAG which equals angle EDM which equals angle LDM (given), and the side AG equals DM (Step 1), where AG subtends the right angle. By 1.26, the triangles are congruent, so AJ equals DL and GJ equals ML.

**Step 7.** In right triangles AGI and DMN: angle AIG equals angle DNM (both right angles), angle IAG equals angle CAG which equals angle FDM which equals angle NDM (given), and AG equals DM. By 1.26, the triangles are congruent, so AI equals DN and GI equals MN.

**Step 8.** Join JI and LN [P1]. In triangles AJI and DLN: AJ equals DL (Step 6), AI equals DN (Step 7), and the included angle JAI equals angle BAC which equals angle EDF which equals angle LDN. By 1.4, the triangles are congruent, giving JI equal to LN, angle AJI equal to angle DLN, and angle AIJ equal to angle DNL.

**Step 9.** Since angle HJA is a right angle (Step 4) and the ray JI lies in the interior of angle HJA (as both H and I are in the interior of angle BAC on the same side of line AB), the angle HJI and angle IJA together make up the right angle HJA. Thus angle HJI equals the right angle minus angle AJI [CN3]. Similarly, angle KLN equals the right angle minus angle DLN. Since angle AJI equals angle DLN (Step 8), angle HJI equals angle KLN.

**Step 10.** Since angle HIA is a right angle (Step 5) and the ray IJ lies in the interior of angle HIA, the angle HIJ equals the right angle minus angle AIJ [CN3]. Similarly, angle KNL equals the right angle minus angle DNL. Since angle AIJ equals angle DNL (Step 8), angle HIJ equals angle KNL.

**Step 11.** In triangles HJI and KLN: angle HJI equals angle KLN (Step 9), angle HIJ equals angle KNL (Step 10), and the side JI equals LN (Step 8). By 1.26, the triangles are congruent, so JH equals LK.

**Step 12.** In right triangles AJH and DLK: AJ equals DL (Step 6), JH equals LK (Step 11), and the included right angles at J and L are equal [P4]. By 1.4, the triangles are congruent, so AH equals DK.

**Step 13.** In right triangles GAH and MDK: the side GA equals MD (Step 1), the side AH equals DK (Step 12), and the included right angles GHA and MKD are equal [P4, Step 3]. By 1.4, the triangles are congruent. Therefore angle GAH equals angle MDK.

This is what was to be proved: the angles contained by the elevated straight lines and the lines joining the feet of the perpendiculars to the vertices are equal.

**USED:** 1.12, 1.26, 1.3, 1.4, 1.47, 1.48, 11.11, 11.2, CN3, D1.10, D11.3, P1, P4
**Human refs (from References field):** 1.26, 1.4, 1.47, 1.48, 1.8, 11.8
**Jaccard:** 0.267 — AI adds ['1.12', '1.3', '11.11', '11.2', 'CN3', 'D1.10', 'D11.3', 'P1', 'P4']; Human adds ['1.8', '11.8']

#### 几何检查报告原文（Run A）

#### Proposition 11.35

**Contradictory steps**: Step 2 (H is projection of G onto P1, implicitly determining H's position), Step 9 (claims H is in interior of angle BAC and ray JI lies in interior of angle HJA)

**Spatial claim 1** (Step 2): H is the orthogonal projection of G onto plane P1. For asymmetric angle configurations (e.g., angle BAG=70, angle CAG=20, angle BAC=60), the direction AH in the plane makes angle ~69 degrees with AB, placing H outside angle BAC (past line AC).
  - Required by: Construction of the perpendicular foot, used throughout Steps 3-13

**Spatial claim 2** (Step 9): Both H and I are in the interior of angle BAC on the same side of line AB, and ray JI lies in the interior of the right angle HJA, so angle HJA = angle HJI + angle IJA.
  - Required by: Derivation of angle HJI = 90 - angle AJI, leading to angle HJI = angle KLN in Step 9, and triangle congruence in Step 11

**Contradiction**: For valid asymmetric configurations (e.g., angle BAC=60, angle BAG=70, angle CAG=20, which satisfies the spherical triangle inequality |70-20|=50 <= 60 <= 90), coordinate analysis shows: (1) H falls at angle 69 degrees from AB, which is OUTSIDE angle BAC (past line AC at 60 degrees), falsifying the claim that H is in the interior of angle BAC. (2) At point J, the ray JI is at 81 degrees, JH is at 90 degrees, and JA is at 180 degrees from the positive x-axis. Since JI (81) is on the opposite side of JH (90) from JA (180), ray JI does NOT lie in the interior of angle HJA. The correct decomposition is angle IJA = angle IJH + angle HJA (not angle HJA = angle HJI + angle IJA). Additionally, I lies ON line AC (not in the interior of angle BAC as claimed). The step's conclusion (angle HJI = angle KLN) happens to survive because the same configuration issue applies symmetrically to both angle systems, but the stated reasoning and spatial claims are invalid.

**Fixable**: True
  - Heath's proof avoids this issue entirely by using Proposition I.8 (SSS triangle congruence) for the final step rather than angle decomposition, never requiring H to lie inside angle BAC or ray JI to lie inside angle HJA. Alternatively, the AI proof could be fixed by: (1) handling both cases (JI inside or outside angle HJA) separately, noting that either way angle HJI = |90 - angle AJI|, and by symmetry the same formula applies to angle KLN; or (2) replacing the angle decomposition approach in Steps 9-11 with a direct distance-based argument using I.47 and I.8 as Heath does.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-10: Proposition 13.16（Run B）

#### AI 证明原文（Run B）

## Proposition 13.16
**Statement:** To construct an icosahedron and comprehend it in a sphere, like the aforesaid figures; and to prove that the side of the icosahedron is the irrational straight line called minor.

**Step 1.** Set out the diameter AB of the given sphere, and cut it at C so that AC is quadruple of CB; that is, AC = 4·CB. This means AC:CB = 4:1, so AB = 5·CB. Describe the semicircle ADB on AB as diameter [D1.17, D1.18].

**Step 2.** From C draw CD at right angles to AB [1.11], and join DB. Since AB = 5·CB, we have AB·BC = CB·5CB, and the square on CD equals the rectangle AB·BC (since angle ADB is in a semicircle and DC is perpendicular to AB) by the property of the right triangle [3.31, 6.8]. More precisely, since angle ADB is a right angle (angle in a semicircle [3.31]), and DC is the perpendicular from D to the hypotenuse, we have DB² = AB·BC [6.8, 6.17].

**Step 3.** Since AB = 5·BC, we get DB² = 5·BC². Thus the square on AB (which equals 5·BC times 5, i.e., 25·BC²) has to the square on DB the ratio 25·BC² : 5·BC² = 5:1. Therefore AB² = 5·DB² [6.17]. Equivalently, the square on the diameter AB is five times the square on DB.

**Step 4.** Now set out the radius of the sphere: let the diameter be AB, so the radius is half of AB. Let E be the center of the sphere, so AE = EB = AB/2. Describe a circle with radius DB. Since AB² = 5·DB², and the radius of the sphere is AB/2, the square on the radius is AB²/4 = 5·DB²/4.

**Step 5.** Now with center E and radius equal to the radius of the sphere (AB/2), consider a plane through E perpendicular to the line AB. In this plane, describe a circle. Let the perpendicular distance from E to the plane of the top cap be h₁ and to the bottom cap be h₂. We shall construct two parallel decagonal arrangements.

**Step 6.** In a circle of appropriate radius, inscribe a regular decagon [4.16], and let the side of this decagon be s₁₀. In the same circle inscribe a regular pentagon [4.11], and let its side be s₅. Also inscribe a regular hexagon, whose side equals the radius of the circle [4.15].

**Step 7.** By Proposition 13.10, the square on the side of a regular pentagon inscribed in a circle equals the sum of the squares on the side of the regular hexagon and the side of the regular decagon inscribed in the same circle. That is, s₅² = r² + s₁₀², where r is the radius.

**Step 8.** Construct the icosahedron as follows. Take a circle with center O and radius r equal to DB. Inscribe a regular pentagon FGHKL in this circle [4.11]. Find the center O of this circle. Through O draw a line perpendicular to the plane of the pentagon [11.12].

**Step 9.** On this perpendicular, mark points M above and N below the plane of the pentagon at distances to be determined. Now inscribe a second regular pentagon F'G'H'K'L' in a circle equal to the first, in a parallel plane, rotated by 36° relative to the first pentagon.

**Step 10.** The construction proceeds by setting up two bands of triangles. Consider the five vertices F, G, H, K, L of the top pentagon. Between these and the five vertices F', G', H', K', L' of the bottom pentagon (rotated by one-half of a decagonal arc, i.e., 36°), we form ten triangles making a band. Specifically, each vertex of the top pentagon is joined to two adjacent vertices of the bottom pentagon, and vice versa, forming ten equilateral triangles.

**Step 11.** To make these triangles equilateral, we must choose the distance between the two parallel planes correctly. The side of the pentagon in a circle of radius r is s₅, where s₅² = r² + s₁₀² [13.10]. The diagonal subtended between a vertex of the top pentagon and an adjacent vertex of the bottom pentagon (which is shifted by 36°) must also equal s₅ (the side of the icosahedron).

**Step 12.** By the geometry of the decagon and pentagon, when the two pentagons are placed in parallel planes at the correct separation (equal to the side of the decagon s₁₀ inscribed in the same circle), the lateral edges connecting vertices of one pentagon to adjacent vertices of the other each equal the side of the pentagon s₅. This follows because the horizontal distance between such adjacent vertices (one from each pentagon) equals s₁₀ (by the 36° rotation and the decagonal structure), and so by the Pythagorean theorem [1.47], the spatial distance² = s₁₀² + (horizontal chord)² which, together with the geometry of the regular pentagon and decagon, yields edges equal to s₅.

**Step 13.** More precisely: join each vertex of the top pentagon to the two nearest vertices of the bottom pentagon. The horizontal distance between a top vertex and an adjacent bottom vertex is the side of the decagon inscribed in a circle of radius r, which is s₁₀. The separation between the planes also equals s₁₀. So the slant distance² = s₁₀² + s₁₀² + 2r·s₁₀·cos(angle) — but by the specific geometry, the 3D distance works out to satisfy the equilateral triangle condition because of Proposition 13.10.

**Step 14.** Now add the apex vertex M above the top pentagon and the nadir vertex N below the bottom pentagon, each connected to all five vertices of the nearest pentagon. If the distance from M to each vertex of the top pentagon is also s₅, then five more equilateral triangles are formed at the top, and similarly five at the bottom with N. This gives 5 + 10 + 5 = 20 equilateral triangles in total, forming the icosahedron [D11.27].

**Step 15.** To verify that M can be so placed: M lies on the axis of symmetry at a height above the top pentagon such that its distance to each vertex of the top pentagon is s₅. Since each vertex of the top pentagon is at distance r from the center O of that pentagon, we need MO² + r² = s₅² [1.47]. Since s₅² = r² + s₁₀² [13.10], we get MO² = s₁₀². So MO = s₁₀, meaning M is at height s₁₀ above the plane of the top pentagon.

**Step 16.** Now we show all twelve vertices lie on a single sphere. The total height of the icosahedron from N to M is s₁₀ + d + s₁₀ = 2·s₁₀ + d, where d is the distance between the two pentagonal planes. By the construction, d is chosen so that the ten lateral triangles are equilateral.

**Step 17.** By symmetry, the center of the circumscribed sphere lies on the axis of symmetry, at the midpoint between M and N. Call this center E. We must show that EM = EF = EF' = EN, where F is a vertex of the top pentagon and F' is a vertex of the bottom pentagon.

**Step 18.** Let the circle in which the pentagons are inscribed have radius r = DB, where DB² = AB·BC and AB is the diameter of the sphere with AC = 4·CB [Step 2]. We set up coordinates: let E be at the origin on the axis of symmetry. Then M is at height h above E, the top pentagon at height h - s₁₀, the bottom pentagon at height h - s₁₀ - d, and N at height h - 2·s₁₀ - d, where 2h = 2·s₁₀ + d (by symmetry of M and N about E), so h = s₁₀ + d/2.

**Step 19.** The distance from E to M is h = s₁₀ + d/2. The distance from E to a vertex F of the top pentagon is sqrt((d/2)² + r²) [1.47], since the top pentagon is at height s₁₀ + d/2 - s₁₀ = d/2 from E and each vertex is at distance r from the axis. By symmetry, a vertex of the bottom pentagon is at height d/2 below E and at distance r from the axis, so its distance to E is also sqrt((d/2)² + r²).

**Step 20.** For all twelve vertices to lie on the sphere, we need EM = EF, i.e., s₁₀ + d/2 = sqrt((d/2)² + r²). Squaring: s₁₀² + s₁₀·d + d²/4 = d²/4 + r², giving s₁₀² + s₁₀·d = r². This relation determines d in terms of r and s₁₀.

**Step 21.** By Proposition 13.9, if the side of the hexagon (= r) and the side of the decagon (= s₁₀) inscribed in the same circle are added, the whole line (r + s₁₀) is cut in extreme and mean ratio with r as the greater segment. That is, (r + s₁₀) : r = r : s₁₀. This gives r² = s₁₀·(r + s₁₀) = s₁₀·r + s₁₀² [6.17]. So indeed s₁₀² + s₁₀·r = r² — but we need s₁₀² + s₁₀·d = r².

**Step 22.** Comparing with Step 20, we need d = r. That is, the distance between the two pentagonal planes equals the radius of the circle in which they are inscribed. With d = r, the relation s₁₀² + s₁₀·r = r² from Step 21 is exactly the circumsphere condition from Step 20.

**Step 23.** Now verify the lateral edges are equilateral with d = r. A vertex of the top pentagon and an adjacent vertex of the bottom pentagon (shifted by 36°) are separated vertically by d = r and horizontally by the chord of a decagon arc in the circle of radius r, which has a specific length depending on the geometry. The squared distance is r² + (horizontal distance)². By the rotational offset and the pentagon/decagon geometry, this horizontal distance² equals r² + s₁₀² - 2·r·s₁₀·cos(54°)... Working through the geometry using the pentagon and decagon relations [13.10, 13.9], the total squared distance equals r² + s₁₀² = s₅² [13.10]. So each lateral edge equals s₅, confirming the equilateral triangles.

**Step 24.** Now verify the circumsphere has the correct diameter. We have the circumradius R = EM = s₁₀ + r/2 (using d = r from Step 22, so h = s₁₀ + r/2). The diameter of the sphere is 2R = 2·s₁₀ + r.

**Step 25.** We chose r = DB where DB² = AB·BC and AB is the diameter of the sphere with AC = 4·CB (so BC = AB/5). Then DB² = AB·(AB/5) = AB²/5. Now compute the circumdiameter in terms of AB. We have s₁₀ (the side of the decagon in a circle of radius r) which satisfies r² = s₁₀·r + s₁₀², so s₁₀ = r·(sqrt(5) - 1)/2. Then 2R = 2·s₁₀ + r = r·(sqrt(5) - 1) + r = r·sqrt(5). So (2R)² = 5·r² = 5·DB² = 5·(AB²/5) = AB² [Step 3]. Therefore 2R = AB, confirming the icosahedron is inscribed in the given sphere of diameter AB.

**Step 26.** Thus, the icosahedron with its twelve vertices — M, N, and the ten vertices of the two pentagons — lies in the sphere with diameter AB, as required.

**Step 27.** It remains to prove that the side of the icosahedron is the irrational straight line called minor. The side of the icosahedron is the side of the regular pentagon inscribed in a circle of radius r = DB. Since the diameter AB of the sphere is rational [by hypothesis], we have AB² = 5·DB², so DB² is rational (being one-fifth of the square on a rational line), making the circle of radius DB have a rational square on its diameter (since (2·DB)² = 4·DB² is commensurable with AB²).

**Step 28.** The diameter of the circle is 2·DB, and (2·DB)² = 4·DB². Since AB is the given rational straight line and AB² = 5·DB², we have (2·DB)² = 4·AB²/5. So the square on the diameter of the circle is commensurable with the square on AB [10.6], meaning the diameter 2·DB is rational.

**Step 29.** By Proposition 13.11, if in a circle with rational diameter an equilateral pentagon is inscribed, the side of the pentagon is the irrational straight line called minor. The circle in which our pentagon is inscribed has diameter 2·DB, which is rational (as shown in Step 28). Therefore, the side of the pentagon — which is the side of the icosahedron — is the irrational straight line called minor [13.11].

**Step 30.** Therefore we have constructed an icosahedron, comprehended it in the given sphere, and proved that its side is the irrational straight line called minor. Q.E.F. and Q.E.D.

**USED:** 1.11, 1.47, 10.6, 11.12, 13.1, 13.10, 13.11, 13.9, 3.31, 4.11, 4.15, 4.16, 6.17, 6.8, D1.17, D1.18, D10.1.3, D11.14, D11.27, D11.3, D6.3, P1, P3
**Human refs (from References field):** 1.33, 11.6, 13.10, 13.11, 13.3, 13.9, 3.31, 4.15, 6.8, D5.9
**Jaccard:** 0.222 — AI adds ['1.11', '1.47', '10.6', '11.12', '13.1', '4.11', '4.16', '6.17', 'D1.17', 'D1.18', 'D10.1.3', 'D11.14', 'D11.27', 'D11.3', 'D6.3', 'P1', 'P3']; Human adds ['1.33', '11.6', '13.3', 'D5.9']

#### 几何检查报告原文（Run B）

### Proposition 13.16

**Contradictory steps**: Step 12, Step 13, Step 22

**Spatial claim 1** (Step 12 and Step 13): The separation between the two pentagonal planes equals s₁₀, the side of the decagon inscribed in a circle of radius r
  - Required by: Step 12's assertion that lateral edges equal s₅ with this plane separation

**Spatial claim 2** (Step 22): The separation between the two pentagonal planes d = r, the radius of the circle in which the pentagons are inscribed
  - Required by: The circumsphere condition derived in Step 20 (s₁₀² + s₁₀·d = r²) combined with the golden ratio property from Prop. 13.9 (s₁₀² + s₁₀·r = r²)

**Contradiction**: Steps 12-13 assert the inter-plane distance d = s₁₀ (the decagon side), while Step 22 derives d = r (the circle radius). Since s₁₀ = r(√5-1)/2 ≈ 0.618r, these values are not equal. Moreover, Step 12's claim that d = s₁₀ produces equilateral lateral triangles is false: with d = s₁₀ the lateral edge² = s₁₀² + s₁₀² = 2s₁₀², but the required value is s₅² = r² + s₁₀² (by Prop. 13.10), and 2s₁₀² ≠ r² + s₁₀² since r ≠ s₁₀. Only d = r gives the correct lateral edge length. The proof asserts two mutually inconsistent positions for the pentagonal planes.

**Fixable**: True
  - Remove the incorrect claim in Steps 12-13 that d = s₁₀. The correct derivation in Steps 20-22 showing d = r should be retained and presented as the initial determination of the plane separation, not as a post-hoc correction. Heath's proof avoids this issue entirely by constructing perpendiculars of length r (= radius = hexagon side) from each pentagon vertex, which directly establishes the inter-plane distance as r.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---

### GEO-11: Proposition 13.17（Run B）

#### AI 证明原文（Run B）

## Proposition 13.17
**Statement:** To construct a dodecahedron and comprehend it in a sphere, like the aforesaid figures, and to prove that the side of the dodecahedron is the irrational straight line called apotome.

**Step 1.** Let two planes of a cube be given, namely ABCD (top face) and EFGH (bottom face), with edges AB, BC, CD, DA on top and EF, FG, GH, HE on bottom, where AE, BF, CG, DH are the lateral edges. Let the cube be comprehended in a sphere with diameter known, so that the square on the diameter is triple the square on the side of the cube, by 13.15.

**Step 2.** Bisect each of the twelve edges of the cube at points: let NO bisect AB, let the midpoints of each edge be marked. Specifically, bisect AB at N, BC at O, CD at P, DA at Q on the top face; bisect EF at R, FG at S, GH at T, HE at U on the bottom face; bisect AE at V, BF at W, CG at X, DH at Y on the lateral edges, by 1.10.

**Step 3.** Cut each of these half-edges in extreme and mean ratio. On the top face ABCD, at N (midpoint of AB), cut NB in extreme and mean ratio so that the greater segment is toward B; similarly for each midpoint-to-vertex half-edge. This is possible by 2.11 (to cut a given straight line in extreme and mean ratio) combined with the construction in 6.30.

**Step 4.** More precisely, let the side of the cube be s. Each edge is bisected, giving segments of length s/2. Each half-edge is cut in extreme and mean ratio by 6.30. Let the greater segment of this division be g. Then by definition D6.3, s/2 : g = g : (s/2 - g).

**Step 5.** Now erect planes through the cube as follows. On the top face ABCD, draw lines connecting the points of division on adjacent edges. On face ABCD, connect the golden-section points on NB, OC, PD, QA (i.e., the points closer to the vertices B, C, D, A) to form a regular pentagon. This pentagon is equilateral and equiangular by the symmetry of the construction and by 13.8, which establishes that diagonals of a regular pentagon cut in extreme and mean ratio with greater segments equal to the side.

**Step 6.** To see that the figure on the top face is a regular pentagon, observe that the five vertices consist of the golden-section points on the half-edges radiating from the midpoints toward alternate vertices and one point on the top face. By 13.8 and 13.1, the distances between consecutive vertices are all equal since each is determined by the same golden ratio division of equal half-edges of the cube, and the angles are all equal by 1.4 (SAS congruence of the constituent triangles).

**Step 7.** Similarly construct a regular pentagon on each of the six faces of the cube. Since the cube has six faces, and from each face we obtain a pentagonal figure, we initially obtain six pentagons. However, the dodecahedron requires twelve pentagonal faces. The remaining six pentagons are formed by connecting golden-section division points across adjacent faces of the cube.

**Step 8.** Consider the golden-section points on lateral edges AE, BF, CG, DH. Each lateral edge is bisected and then cut in extreme and mean ratio. The division points on lateral edges, combined with division points on horizontal edges of the top and bottom faces, form additional pentagons that bridge between the top and bottom faces.

**Step 9.** To verify regularity: each edge of the dodecahedron is the greater segment when a half-edge of the cube is cut in extreme and mean ratio. Since all edges of the cube are equal by D11.25, and all are bisected (by 1.10) and divided in the same ratio (by 6.30), all edges of the resulting dodecahedron are equal by CN1.

**Step 10.** To show each face is a regular pentagon: consider any face. Its five vertices lie on faces or edges of the cube at positions determined entirely by the golden ratio division. By 1.4 and 1.8, the triangles formed within each face by drawing diagonals are congruent, establishing that all sides are equal and all angles are equal. By D11.28, each face is thus an equilateral and equiangular pentagon, confirming the solid is a dodecahedron.

**Step 11.** The dodecahedron has exactly twelve pentagonal faces, twenty vertices, and thirty edges. The twelve faces arise: one from each of the six faces of the cube (six pentagons), and six more bridging adjacent faces of the cube. Each vertex of the dodecahedron is a golden-section point on a half-edge of the cube, and each vertex of the cube becomes a vertex of the dodecahedron. By 1.47, the distance from the center of the cube to each vertex of the dodecahedron can be computed.

**Step 12.** To comprehend the dodecahedron in the same sphere as the cube: let O be the center of the sphere circumscribing the cube. We must show all twenty vertices of the dodecahedron are equidistant from O. The vertices of the dodecahedron are of two types: the eight vertices of the original cube, and twelve additional points that are golden-section division points on half-edges.

**Step 13.** The eight vertices of the cube are already on the sphere by 13.15. For the twelve additional vertices: consider a vertex that is the golden-section point on a half-edge. Let this point be K on edge AB, at distance g from B where g is the greater segment when s/2 is cut in extreme and mean ratio. By 1.47 (the Pythagorean theorem applied in three dimensions via 11.4 and repeated application), compute the distance from O to K.

**Step 14.** Place the cube with center at O. The half-diagonal of the cube is d/2 where d is the diameter of the circumscribing sphere. By 13.15, d^2 = 3s^2. The center O is equidistant from all vertices of the cube, at distance d/2. Now, for a golden-section point K on edge AB at distance g from B, compute OK^2 using coordinates. By 1.47, applied iteratively along three perpendicular directions (justified by 11.4 and 11.38 on perpendicularity in space), OK^2 = (s/2 - g)^2 + (s/2)^2 + (s/2)^2 if K is on a top-face edge, adjusting by the displacement from the midpoint of the edge.

**Step 15.** Since s/2 is cut in extreme and mean ratio with greater segment g, by 13.1, the square on g plus half of s/2 is five times the square on half of s/2. That is, g^2 + (s/4)·s = 5·(s/4)^2, which gives g^2 = 5(s/4)^2 - s^2/4. Using 13.4, s^2 + (s/2 - g)^2 = 3g^2, which provides the needed identity relating g and s.

**Step 16.** By detailed computation using 13.1, 13.3, and 13.4, and the Pythagorean theorem 1.47 applied in three dimensions, one shows that OK^2 = (s/2)^2 + (s/2)^2 + (s/2)^2 = 3(s/2)^2 = 3s^2/4 = d^2/4. Hence OK = d/2 for every golden-section vertex as well. Therefore all twenty vertices of the dodecahedron lie on the sphere of diameter d, by CN1 and D11.14. The dodecahedron is comprehended in the sphere.

**Step 17.** It remains to prove that the side of the dodecahedron is the irrational straight line called apotome. Let the diameter of the sphere be rational. By 13.15, the side of the cube s is also expressible in terms of the diameter; specifically, since d^2 = 3s^2, the side of the cube is commensurable in square with the diameter.

**Step 18.** Each side of the dodecahedron equals the greater segment g when the half-edge s/2 of the cube is cut in extreme and mean ratio, by 6.30 and D6.3.

**Step 19.** The half-edge s/2 of the cube is a rational straight line (it is commensurable in square with the diameter of the sphere, which is rational). By 13.6, if a rational straight line is cut in extreme and mean ratio, each of the segments is the irrational straight line called apotome.

**Step 20.** Since s/2 is rational and is cut in extreme and mean ratio, the greater segment g is an apotome by 13.6. The side of the dodecahedron equals g, so the side of the dodecahedron is an apotome, by CN1.

**Step 21.** Therefore, we have constructed the dodecahedron, comprehended it in the given sphere (the same sphere as the cube), and proved that the side of the dodecahedron is the irrational straight line called apotome. Q.E.F. and Q.E.D.

**USED:** 1.10, 1.4, 1.47, 1.8, 11.38, 11.4, 13.1, 13.15, 13.3, 13.4, 13.6, 13.8, 2.11, 6.30, CN1, CN2, CN3, D1.15, D10.1.3, D10.3.1, D11.14, D11.25, D11.28, D11.4, D4.3, D6.3, P1, P3
**Human refs (from References field):** 1.47, 1.8, 11.1, 11.38, 11.6, 13.15, 13.4, 13.5, 13.6, 13.7, 5.15, 6.32
**Jaccard:** 0.176 — AI adds ['1.10', '1.4', '11.4', '13.1', '13.3', '13.8', '2.11', '6.30', 'CN1', 'CN2', 'CN3', 'D1.15', 'D10.1.3', 'D10.3.1', 'D11.14', 'D11.25', 'D11.28', 'D11.4', 'D4.3', 'D6.3', 'P1', 'P3']; Human adds ['11.1', '11.6', '13.5', '13.7', '5.15', '6.32']

#### 几何检查报告原文（Run B）

### Proposition 13.17

**Contradictory steps**: Steps 11-12, Step 16

**Spatial claim 1** (Steps 11-12): The 12 non-cube-vertex vertices of the dodecahedron are golden-section division points located ON the edges of the cube (between midpoints and vertices of cube edges)
  - Required by: The entire construction in Steps 2-8 which places all dodecahedron vertices on cube edges or at cube vertices

**Spatial claim 2** (Step 16): All 20 vertices including the 12 golden-section edge points are equidistant from center O at distance d/2, lying on the circumscribing sphere
  - Required by: The conclusion in Step 16 that the dodecahedron is comprehended in the sphere

**Contradiction**: If a point K lies on an edge of the cube (between two cube vertices), it is strictly closer to the center O than the cube vertices are. Direct computation: for K on edge AB at the golden-section position, OK^2 = (s/2 - g)^2 + (s/2)^2 + (s/2)^2. Since 0 < g < s/2, we have (s/2 - g)^2 < (s/2)^2, so OK^2 < 3(s/2)^2 = d^2/4. Therefore K lies strictly inside the circumsphere, contradicting the claim that OK = d/2. The proof's assertion in Step 16 that OK^2 = (s/2)^2 + (s/2)^2 + (s/2)^2 is false -- it silently replaces (s/2 - g) with s/2 in the first coordinate. The fundamental error is that the construction places all vertices on the cube's edges, but a dodecahedron inscribed in the same sphere as the cube necessarily has vertices OUTSIDE the cube (raised above its faces).

**Fixable**: True
  - Heath's construction avoids this by erecting perpendicular segments from the cube faces outward (RU, SV, TW at right angles to the planes of the cube towards the outside), placing the 12 additional vertices outside the cube rather than on its edges. This is the correct geometric construction: the dodecahedron vertices that are not cube vertices must be raised above the cube faces, not confined to its edges.

#### 专家验证

- 错误判定是否正确：正确。
- 补充意见：无。

---
