# 专家验证文档：D 类证明路径差异审核

---

## 前情提要

本研究使用 Claude Opus 4.6 对欧几里得《几何原本》全部 465 条命题进行了三轮独立证明（Run A、Run B、Run C）。随后，通过自动分类系统将每条 AI 证明与 Heath 的人类证明进行对比，分为四类：

- **P（Perfect match）**：引用集完全一致
- **G（Granularity difference）**：证明路径相同，仅引用粒度不同
- **D（Path difference）**：有效的替代证明路径
- **E（Error）**：可正面识别的逻辑缺陷

三轮实验共产生 1,395 条分类结果，其中 D 类（路径差异）共 381 条。其中 11 条在后续几何一致性检查中被判定为 FAIL（存在空间矛盾），已归入错误类别单独处理。剩余 370 条 D 类证明被判定为逻辑正确但采用了与 Heath 不同的证明策略——例如 AI 倾向于代数方法而非几何构造，或选择了不同的引理链。

为验证 D 类分类的准确性，我们从这 370 条 D 类条目中随机抽样 18 条（random seed=42），请专家审核 AI 证明与人类证明之间是否确实存在路径差异（而非粒度差异或错误）。

## 验证方案

请专家对以下 18 个 D 类条目逐一审核。每个条目包含：

1. **命题陈述**：该命题的原始表述
2. **AI 证明原文**：AI 在该轮实验中产出的完整逐步证明
3. **Heath 人类证明原文**：Heath 英译本中的证明文本
4. **自动分类报告原文**：分类系统对两份证明的分析与判定依据

请专家对每个条目判断：

- **路径差异判定是否正确**：AI 证明与人类证明是否确实采用了不同的证明路径？还是仅为粒度差异（应为 G）或存在错误（应为 E）？
- **补充意见**：对路径差异性质的进一步说明，或分类系统分析中未注意到的问题

---

### D-1: Proposition 2.7（Run B）

**命题陈述：** If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

#### AI 证明原文（Run B）

## Proposition 2.7
**Statement:** If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

**Step 1.** Let AB be a straight line cut at random at the point C. We must show that the square on AB together with the square on CB is equal to twice the rectangle contained by AB and CB together with the square on AC.

**Step 2.** Since the straight line AB has been cut at C, by Proposition 2.4, the square on AB is equal to the squares on AC and CB together with twice the rectangle contained by AC and CB. That is, sq(AB) = sq(AC) + sq(CB) + 2·rect(AC, CB).

**Step 3.** Add the square on CB to both sides. By Common Notion 2, sq(AB) + sq(CB) = sq(AC) + sq(CB) + 2·rect(AC, CB) + sq(CB). Hence sq(AB) + sq(CB) = sq(AC) + 2·sq(CB) + 2·rect(AC, CB).

**Step 4.** Now, since AB has been cut at C, by Proposition 2.3, the rectangle contained by AB and CB is equal to the rectangle contained by AC and CB together with the square on CB. That is, rect(AB, CB) = rect(AC, CB) + sq(CB).

**Step 5.** Therefore twice the rectangle contained by AB and CB equals twice the rectangle contained by AC and CB together with twice the square on CB. That is, 2·rect(AB, CB) = 2·rect(AC, CB) + 2·sq(CB), by Common Notion 2 (adding equals to equals, specifically each quantity to itself).

**Step 6.** From Step 3 we have sq(AB) + sq(CB) = sq(AC) + 2·sq(CB) + 2·rect(AC, CB). From Step 5 we have 2·rect(AB, CB) = 2·rect(AC, CB) + 2·sq(CB). Since the right-hand sides are equal (both equal sq(AC) subtracted from the same quantity — more precisely, both 2·sq(CB) + 2·rect(AC, CB) and 2·rect(AB, CB) are equal by Step 5), we substitute: sq(AB) + sq(CB) = sq(AC) + 2·rect(AB, CB), by Common Notion 1.

**Step 7.** Therefore the square on the whole AB and the square on one of the segments CB, both together, are equal to twice the rectangle contained by AB and CB together with the square on the remaining segment AC. Q.E.D.

**USED:** 2.3, 2.4, CN1, CN2
**Human refs (from References field):** 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.3', '2.4', 'CN1', 'CN2']; Human adds ['1.43', '1.46']

#### Heath 人类证明原文

For let a straight line AB be cut at random at the point C;  I say that the squares on AB, BC are equal to twice the rectangle contained by AB, BC and the square on CA. For let the square ADEB be described on AB, [I. 46] and let the figure be drawn. Then, since AG is equal to GE, [I. 43] let CF be added to each; therefore the whole AF is equal to the whole CE. Therefore AF, CE are double of AF. But AF, CE are the gnomon KLM and the square CF; therefore the gnomon KLM and the square CF are double of AF. But twice the rectangle AB, BC is also double of AF; for BF is equal to BC; therefore the gnomon KLM and the square CF are equal to twice the rectangle AB, BC. Let DG, which is the square on AC, be added to each; therefore the gnomon KLM and the squares BG, GD are equal to twice the rectangle contained by AB, BC and the square on AC. But the gnomon KLM and the squares BG, GD are the whole ADEB and CF, which are squares described on AB, BC; therefore the squares on AB, BC are equal to twice the rectangle contained by AB, BC together with the square on AC.

#### 分类报告原文（Run B）

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 2.7 uses a geometric gnomon approach: constructing square ADEB on AB (I.46), applying I.43 (complements about the diagonal are equal) to establish AG = GE, then working through the gnomon KLM and square areas to reach the conclusion. The AI proof takes a fundamentally different algebraic path: it applies 2.4 to expand sq(AB) into sq(AC) + sq(CB) + 2*rect(AC,CB), then applies 2.3 to show rect(AB,CB) = rect(AC,CB) + sq(CB), and combines these via CN1 and CN2 to reach the same conclusion. The key intermediate conclusions are entirely different — Heath argues through gnomons and area complements while the AI argues through algebraic identities from earlier Book 2 propositions. The proof-tree containment test confirms this is not mere citation-depth difference: I.43, which is central to Heath's proof, does not appear inside the proofs of either 2.3 or 2.4, so the AI's route is genuinely independent. The AI's algebraic chain is logically complete and valid (Q3(b) holds), so the classification is D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-2: Proposition 3.9（Run B）

**命题陈述：** If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

#### AI 证明原文（Run B）

## Proposition 3.9
**Statement:** If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

**Step 1.** Let a point D be taken within circle ABC, and let more than two equal straight lines fall from D on the circle, namely DA, DB, and DC, such that DA = DB = DC.

**Step 2.** Suppose, for the sake of contradiction, that D is not the centre of circle ABC.

**Step 3.** Find the centre E of circle ABC [3.1].

**Step 4.** Since D is not the centre and E is, D and E are distinct points. Draw the straight line from D to E [P1] and produce it in both directions to meet the circle, forming a diameter of the circle through D [P2, D1.17].

**Step 5.** Since D is a point on this diameter which is not the centre of the circle, by Proposition 3.7, only two equal straight lines can fall from D on the circle, one on each side of the least straight line.

**Step 6.** But DA, DB, and DC are three equal straight lines falling from D on the circle, which is more than two. This contradicts the conclusion of Step 5.

**Step 7.** Therefore the assumption in Step 2 is false, and D is the centre of circle ABC [D1.16].

**Step 8.** Hence, if a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle. Q.E.F.

**USED:** 3.1, 3.7, D1.16, D1.17, P1, P2
**Human refs (from References field):** 1.8, 3.1, D1.10
**Jaccard:** 0.125 — AI adds ['3.7', 'D1.16', 'D1.17', 'P1', 'P2']; Human adds ['1.8', 'D1.10']

#### Heath 人类证明原文

Let ABC be a circle and D a point within it, and from D let more than two equal straight lines, namely DA, DB, DC, fall on the circle ABC; I say that the point D is the centre of the circle ABC. For let AB, BC be joined and bisected at the points E, F, and let ED, FD be joined and drawn through to the points G, K, H, L. Then, since AE is equal to EB, and ED is common, the two sides AE, ED are equal to the two sides BE, ED; and the base DA is equal to the base DB; therefore the angle AED is equal to the angle BED. [I. 8]  Therefore each of the angles AED, BED is right; [I. Def. 10] therefore GK cuts AB into two equal parts and at right angles. And since, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line, [III. 1] the centre of the circle is on GK. For the same reason the centre of the circle ABC is also on HL. And the straight lines GK, HL have no other point common but the point D; therefore the point D is the centre of the circle ABC.

#### 分类报告原文（Run B）

### 3.9
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath proves 3.9 directly by joining chords AB and BC, bisecting them, showing via I.8 that the perpendicular bisectors pass through D, and concluding by III.1 that D lies on the locus of centers; the intersection of two such loci forces D to be the center. The AI instead uses proof by contradiction: assuming D is not the center, it finds the actual center via 3.1, draws a diameter through D, and applies 3.7 to conclude that only two equal lines can fall from D on the circle, contradicting the hypothesis of three. These are fundamentally different logical backbones — Heath uses perpendicular bisector locus (I.8, D1.10, III.1) while the AI uses the diameter extremal property (3.7) via reductio. Since the AI's path is logically complete and valid under the hardened 1(b) standard, the classification is D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-3: Proposition 3.16（Run A）

**命题陈述：** The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

#### AI 证明原文（Run A）

## Proposition 3.16
**Statement:** The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

**Step 1.** Let there be a circle with centre F and diameter AB. Draw the straight line AE from the extremity A of the diameter at right angles to AB [1.11]. I say that the straight line so drawn falls outside the circle; that no other straight line can be interposed between AE and the circumference; that the angle of the semicircle is greater than any acute rectilineal angle; and that the remaining angle between AE and the circumference is less than any acute rectilineal angle.

**Step 2.** Suppose, for contradiction, that AE does not fall outside the circle, but rather falls within it, so that some point G on AE lies inside or on the circle. Then since F is the centre, join FG [P1].

**Step 3.** Since FA is a radius and G is supposed to lie on or within the circle, we have FG less than or equal to FA (if G were on the circumference, FG = FA; if inside, FG < FA by D1.15). But since the angle FAG is a right angle (by construction), the triangle FAG has a right angle at A.

**Step 4.** In triangle FAG, the angle at A is a right angle. By 1.17, any two angles of a triangle are together less than two right angles; but more specifically, by 1.18, the greater side is opposite the greater angle. Since the angle FAG is a right angle, and by 1.17 the sum of the other two angles is less than two right angles, the angle at A (being right) is the greatest angle in triangle FAG (since the other two must each be less than a right angle). Therefore by 1.19, the side FG opposite the greatest angle must be greater than FA.

**Step 5.** But FG greater than FA is impossible, since FA is a radius and G was assumed to lie on or within the circle (so FG should be at most equal to FA). This contradiction shows that the straight line AE drawn at right angles to the diameter at its extremity falls entirely outside the circle, except at the point A itself.

**Step 6.** Next, I say that no other straight line can be interposed between the straight line AE and the circumference. Suppose, for contradiction, that some straight line AH can be placed in the space between AE and the circumference, so that AH is distinct from AE and falls outside the circle.

**Step 7.** From centre F, draw FH perpendicular to AH, meeting AH at H [1.12], and let this perpendicular meet or be extended as needed. Actually, let us proceed more carefully: draw from F the perpendicular to AH, and let the foot of the perpendicular from F to line AH be the point K, so that FK is perpendicular to AH [1.12].

**Step 8.** Since the angle FKA is a right angle (FK perpendicular to AH), and the angle FAK (which equals angle FAH) is less than a right angle (because AH lies in the region between AE and the circumference, so angle EAH is positive, meaning angle FAH = angle FAE minus angle EAH is less than the right angle FAE), then in triangle FAK the angle at K is right and the angle at A is acute.

**Step 9.** In triangle FAK, the angle FKA is right, so it is the greatest angle. By 1.19, the side FA opposite the right angle is the greatest side, so FA is greater than FK.

**Step 10.** Now, since FK is perpendicular to line AH dropped from the centre F, and FA is a radius with FA > FK, the line AH intersects the circle. This is because: draw from F along the line FK a distance equal to FA to find a point; since FA > FK, the circle passes beyond K along line AH. More precisely, let L be the point where line FA (a radius) extended from F meets the circumference. Consider any point D on line AH between A and the circumference: by 3.2, the line segment from any point on the circumference to another point on the circumference falls within the circle.

**Step 11.** Let me argue more directly. Since FK (perpendicular from centre F to line AH) is less than FA (the radius) by Step 9, the line AH must cut the circle [by the reasoning of 3.14 and 3.15: the perpendicular distance from the centre to line AH is less than the radius]. Specifically, from F draw FD such that FD equals FA (a radius), where D is a point on line AH (this is possible since FK < FA, so the circle with centre F and radius FA intersects line AH) [P3]. Then D is on the circumference. But AH was supposed to lie entirely in the space between the circumference and AE, meaning AH does not cut the circle. This is a contradiction.

**Step 12.** Therefore no straight line can be interposed between the tangent line AE and the circumference of the circle.

**Step 13.** Now I say that the angle of the semicircle, namely the angle contained by the diameter AB and the circumference, is greater than any acute rectilineal angle, and the remaining angle between AE and the circumference is less than any acute rectilineal angle.

**Step 14.** Let angle BAC be any given acute rectilineal angle, where AC is a straight line making an acute angle with AB at A. I must show that the angle of the semicircle (the mixed angle between diameter BA and the arc) is greater than angle BAC, and the horn angle between AE and the arc is less than angle BAC.

**Step 15.** Since angle BAC is an acute angle and angle BAE is a right angle, the line AC falls between AB and AE, that is, angle BAC is less than angle BAE. By the argument in Steps 6 through 12, no straight line from A falling between AE and the circumference can be interposed without cutting the circle. Since AC lies between AB and AE (being an acute angle with AB), line AC must enter the interior of the circle (it cannot lie entirely outside, since only AE and lines on the other side of AE from the circle lie entirely outside).

**Step 16.** Since line AC enters the interior of the circle, it cuts the circumference at some point, say D. Then the circumference of the semicircle passes beyond AC (between AC and the diameter AB, the arc bulges out past AC). This means the mixed angle contained by the diameter AB and the arc of the semicircle is greater than the rectilineal angle BAC, since the arc extends beyond AC on the side of AB.

**Step 17.** Since this holds for any arbitrary acute rectilineal angle BAC, the angle of the semicircle is greater than every acute rectilineal angle.

**Step 18.** Similarly, for the remaining horn angle (the angle between AE and the circumference on the side of the semicircle): since the circumference passes between AE and any line AC making an acute angle with AE on that side (equivalently, since AC cuts the circle and therefore the arc lies between AE and AC), the horn angle between AE and the arc is less than the angle between AE and AC, which can be made to equal any given acute angle. Therefore the horn angle is less than every acute rectilineal angle.

**Step 19.** Therefore: (1) the straight line drawn at right angles to the diameter from its extremity falls outside the circle; (2) between that straight line and the circumference no other straight line can be interposed; (3) the angle of the semicircle is greater than any acute rectilineal angle; and (4) the remaining horn angle is less than any acute rectilineal angle. Q.E.F.

**USED:** 1.11, 1.12, 1.17, 1.19, 3.2, D1.10, D1.12, D1.15, D1.17, D3.2, P1, P3
**Human refs (from References field):** 1.17, 1.19, 1.5
**Jaccard:** 0.154 — AI adds ['1.11', '1.12', '3.2', 'D1.10', 'D1.12', 'D1.15', 'D1.17', 'D3.2', 'P1', 'P3']; Human adds ['1.5']

#### Heath 人类证明原文

Let ABC be a circle about D as centre and AB as diameter; I say that the straight line drawn from A at right angles to AB from its extremity will fall outside the circle. For suppose it does not, but, if possible, let it fall within as CA, and let DC be joined. Since DA is equal to DC, the angle DAC is also equal to the angle ACD. [I. 5]  But the angle DAC is right; therefore the angle ACD is also right: thus, in the triangle ACD, the two angles DAC, ACD are equal to two right angles: which is impossible. [I. 17] Therefore the straight line drawn from the point A at right angles to BA will not fall within the circle. Similarly we can prove that neither will it fall on the circumference; therefore it will fall outside. Let it fall as AE; I say next that into the space between the straight line AE and the circumference CHA another straight line cannot be interposed. For, if possible, let another straight line be so interposed, as FA, and let DG be drawn from the point D perpendicular to FA. Then, since the angle AGD is right, and the angle DAG is less than a right angle, AD is greater than DG. [I. 19]  But DA is equal to DH; therefore DH is greater than DG, the less than the greater: which is impossible. Therefore another straight line cannot be interposed into the space between the straight line and the circumference. I say further that the angle of the semicircle contained by the straight line BA and the circumference CHA is greater than any acute rectilineal angle, and the remaining angle contained by the circumference CHA and the straight line AE is less than any acute rectilineal angle. For, if there is any rectilineal angle greater than the angle contained by the straight line BA and the circumference CHA, and any rectilineal angle less than the angle contained by the circumference CHA and the straight line AE, then into the space between the circumference and the straight line AE a straight line will be interposed such as will make an angle contained by straight lines which is greater than the angle contained by the straight line BA and the circumference CHA, and another angle contained by straight lines which is less than the angle contained by the circumference CHA and the straight line AE. But such a straight line cannot be interposed; therefore there will not be any acute angle contained by straight lines which is greater than the angle contained by the straight line BA and the circumference CHA, nor yet any acute angle contained by straight lines which is less than the angle contained by the circumference CHA and the straight line AE.

#### 分类报告原文（Run A）

### 3.16
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof of Part 1 (tangent falls outside the circle) uses I.5 to establish that in triangle DAC with DA = DC (radii), the base angles are equal, so since angle DAC is right, angle ACD is also right, yielding two right angles in a triangle (contradicting I.17). The AI instead argues that in triangle FAG with a right angle at A, by I.17 and I.19 the side FG opposite the right angle must be the greatest side, hence FG > FA, contradicting the assumption that G lies on or inside the circle. This constitutes a genuinely different logical backbone for Part 1: Heath's route goes through the isosceles-triangle theorem (I.5) while the AI's route goes through the angle-side inequality (I.19). Parts 2 and 3 share essentially the same backbone in both proofs. Since the AI's different path is logically valid and complete, the classification is D.

#### 专家验证

- 路径差异判定是否正确：不完全正确，原证明是不完整但可修补的。
- 补充意见：3.14 + 3.15推 step 10/11 需要进一步的论证。

---

### D-4: Proposition 4.9（Run A）

**命题陈述：** About a given square to circumscribe a circle.

#### AI 证明原文（Run A）

## Proposition 4.9
**Statement:** About a given square to circumscribe a circle.

**Step 1.** Let ABCD be the given square. By D1.22, all four sides are equal (AB = BC = CD = DA) and all four angles are right angles.

**Step 2.** Draw diagonals AC and BD by P1. Let E be the point at which they intersect.

**Step 3.** Since angle DAB and angle ABC are both right angles (Step 1), the co-interior angles formed by lines DA and CB with transversal AB sum to two right angles. By 1.28, DA is parallel to CB. Similarly, since angle ABC and angle BCD are both right angles, the co-interior angles formed by lines AB and DC with transversal BC sum to two right angles, so AB is parallel to DC by 1.28.

**Step 4.** Since AB is parallel to DC and BD is a transversal, angle ABD = angle BDC as alternate interior angles by 1.29. That is, angle ABE = angle CDE. Similarly, since AB is parallel to DC and AC is a transversal, angle BAC = angle DCA by 1.29. That is, angle BAE = angle DCE.

**Step 5.** In triangles AEB and CED: angle BAE = angle DCE (Step 4), AB = CD (D1.22), and angle ABE = angle CDE (Step 4). By 1.26 (ASA), triangle AEB is congruent to triangle CED. Therefore AE = CE and BE = DE.

**Step 6.** In triangles AEB and AED: AB = AD (D1.22), BE = DE (Step 5), and AE is common. By 1.8 (SSS), triangle AEB is congruent to triangle AED. Therefore angle AEB = angle AED.

**Step 7.** Since E lies on line BD, angles AEB and AED together make the angles on one side of line BD at point E. By 1.13, angle AEB + angle AED equals two right angles. Since angle AEB = angle AED (Step 6), each equals a right angle.

**Step 8.** From the congruence in Step 6, angle EAB = angle EAD. Since angle EAB + angle EAD = angle BAD = a right angle (D1.22), and angle EAB = angle EAD, we have angle EAB + angle EAB equals a right angle, by CN1.

**Step 9.** In triangle AEB, angle AEB is a right angle (Step 7). By 1.32, the three angles of triangle AEB equal two right angles, so angle EAB + angle ABE = two right angles minus one right angle = one right angle. That is, angle EAB + angle ABE equals a right angle.

**Step 10.** From Step 8, angle EAB + angle EAB equals a right angle. From Step 9, angle EAB + angle ABE equals a right angle. By CN1, angle ABE = angle EAB.

**Step 11.** In triangle AEB, since angle EAB = angle ABE (Step 10), the side opposite angle ABE equals the side opposite angle EAB. By 1.6, AE = BE.

**Step 12.** From Step 5, AE = CE and BE = DE. From Step 11, AE = BE. Therefore EA = EB = EC = ED, so all four vertices of the square are equidistant from E.

**Step 13.** With center E and radius EA, describe a circle ABCD by P3. Since EA = EB = EC = ED (Step 12), this circle passes through all four vertices A, B, C, D. By D1.15, all straight lines from E to the circumference are equal, confirming A, B, C, D lie on the circle.

**Step 14.** Since the circumference of the circle passes through each angle of the square ABCD, the circle is circumscribed about the square by D4.6.

Therefore, about the given square ABCD, a circle has been circumscribed, which is what was required to do.

**USED:** 1.13, 1.26, 1.28, 1.29, 1.32, 1.6, 1.8, CN1, D1.15, D1.22, D4.6, P1, P3
**Human refs (from References field):** 1.6, 1.8
**Jaccard:** 0.154 — AI adds ['1.13', '1.26', '1.28', '1.29', '1.32', 'CN1', 'D1.15', 'D1.22', 'D4.6', 'P1', 'P3']

#### Heath 人类证明原文

Let ABCD be the given square; thus it is required to circumscribe a circle about the square ABCD. For let AC, BD be joined, and let them cut one another at E. Then, since DA is equal to AB, and AC is common, therefore the two sides DA, AC are equal to the two sides BA, AC; and the base DC is equal to the base BC; therefore the angle DAC is equal to the angle BAC. [I. 8]  Therefore the angle DAB is bisected by AC. Similarly we can prove that each of the angles ABC, BCD, CDA is bisected by the straight lines AC, DB. Now, since the angle DAB is equal to the angle ABC, and the angle EAB is half the angle DAB, and the angle EBA half the angle ABC, therefore the angle EAB is also equal to the angle EBA; so that the side EA is also equal to EB. [I. 6] Similarly we can prove that each of the straight lines EA, EB is equal to each of the straight lines EC, ED. Therefore the four straight lines EA, EB, EC, ED are equal to one another. Therefore the circle described with centre E and distance one of the straight lines EA, EB, EC, ED will pass also through the remaining points; and it will have been circumscribed about the square ABCD. Let it be circumscribed, as ABCD. Therefore about the given square a circle has been circumscribed.

#### 分类报告原文（Run A）

### 4.9
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof establishes that the diagonals bisect the angles of the square (using I.8 on triangles formed by equal sides and a common diagonal), then infers equal half-angles at adjacent vertices to conclude EA=EB by I.6. The AI takes a fundamentally different route: it first proves opposite sides are parallel (I.28), derives equal alternate angles with the diagonals as transversals (I.29), applies ASA congruence (I.26) to opposite triangles AEB and CED to get AE=CE and BE=DE, then uses SSS congruence (I.8) on adjacent triangles AEB and AED, derives right angles at E via I.13 and the angle sum theorem I.32, and finally shows angle EAB = angle ABE to conclude AE=BE by I.6. The key intermediate conclusions differ: Heath's backbone runs through angle bisection of the square's corners, while the AI's backbone runs through parallelism of sides and ASA congruence of diagonally opposite triangles. Since the AI's different path is logically complete and valid, Q3 confirms classification as D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-5: Proposition 5.5（Run A）

**命题陈述：** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

#### AI 证明原文（Run A）

## Proposition 5.5
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let magnitude AB be the same multiple of magnitude CD that the part AE subtracted is of the part CF subtracted. We must show that the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD. [Setup from the hypothesis]

**Step 2.** Since AB is the same multiple of CD that AE is of CF, let this common multiplicity be m. Then AB = m times CD, and AE = m times CF, meaning AB is made up of m magnitudes each equal to CD, and AE is made up of m magnitudes each equal to CF. [D5.2]

**Step 3.** Decompose AB into m parts, each equal to CD: let these be CD_1, CD_2, ..., CD_m, so that AB = CD_1 + CD_2 + ... + CD_m where each CD_i equals CD. Likewise, decompose AE into m parts, each equal to CF: let these be CF_1, CF_2, ..., CF_m, so that AE = CF_1 + CF_2 + ... + CF_m where each CF_i equals CF. [D5.2]

**Step 4.** Since CF is a part of CD (CF is subtracted from CD to leave remainder FD), we have CF less than CD, and FD = CD - CF. For each i from 1 to m, let FD_i = CD_i - CF_i. Since CD_i = CD and CF_i = CF for each i, each remainder FD_i = CD - CF = FD. [CN3]

**Step 5.** Now the remainder EB = AB - AE = (CD_1 + CD_2 + ... + CD_m) - (CF_1 + CF_2 + ... + CF_m). Since we subtract equals from equals in corresponding pairs, EB = (CD_1 - CF_1) + (CD_2 - CF_2) + ... + (CD_m - CF_m) = FD_1 + FD_2 + ... + FD_m. [CN3]

**Step 6.** Since each FD_i equals FD (from Step 4), the sum FD_1 + FD_2 + ... + FD_m consists of m magnitudes each equal to FD. Therefore EB is the same multiple of FD as AB is of CD, namely m times FD. [D5.2]

**Step 7.** Therefore the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD, which is what was to be proved.

**USED:** CN3, D5.1, D5.2
**Human refs (from References field):** 5.1
**Jaccard:** 0.000 — AI adds ['CN3', 'D5.1', 'D5.2']; Human adds ['5.1']

#### Heath 人类证明原文

For let the magnitude AB be the same multiple of the magnitude CD that the part AE subtracted is of the part CF subtracted; I say that the remainder EB is also the same multiple of the remainder FD that the whole AB is of the whole CD. For, whatever multiple AE is of CF, let EB be made that multiple of CG. Then, since AE is the same multiple of CF that EB is of GC, therefore AE is the same multiple of CF that AB is of GF. [V. 1] But, by the assumption, AE is the same multiple of CF that AB is of CD. Therefore AB is the same multiple of each of the magnitudes GF, CD; therefore GF is equal to CD. Let CF be subtracted from each; therefore the remainder GC is equal to the remainder FD. And, since AE is the same multiple of CF that EB is of GC, and GC is equal to DF,therefore AE is the same multiple of CF that EB is of FD. But, by hypothesis,  AE is the same multiple of CF that AB is of CD; therefore EB is the same multiple of FD that AB is of CD. That is, the remainder EB will be the same multiple ofthe remainder FD that the whole AB is of the whole CD.

#### 分类报告原文（Run A）

### 5.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof introduces an auxiliary magnitude CG, constructs EB as the same multiple of CG, then uses proposition 5.1 (equimultiple composition) to establish GF = CD, subtracts CF to get GC = FD, and substitutes back. The AI proof takes a fundamentally different path: it works directly from Definition 5.2, decomposing AB and AE into m individual copies of CD and CF respectively, computing pairwise remainders FD_i = CD - CF = FD using CN3, and summing to get EB = m times FD. The key intermediate conclusions differ — Heath's backbone pivots on the auxiliary construction and the equality GF = CD via 5.1, while the AI's backbone pivots on pairwise decomposition and direct summation from the definition. Since the backbones are different (Case B in Q2), Q3 was applied: the AI's chain from definitions and CN3 to the conclusion is logically complete and sound, yielding a valid different path (D).

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-6: Proposition 6.6（Run B）

**命题陈述：** If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

#### AI 证明原文（Run B）

## Proposition 6.6
**Statement:** If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let ABC and DEF be two triangles having angle BAC equal to angle EDF, and the sides about the equal angles proportional, so that AB is to DE as AC is to DF. We must prove that the triangles are equiangular and have those angles equal which the corresponding sides subtend.

**Step 2.** On the straight line DE, from D, mark off DG equal to AB, and on the straight line DF, from D, mark off DH equal to AC. This is possible by 1.3, since if DE is greater than AB we cut off the equal length, and similarly for DF and AC. (If DE equals AB and DF equals AC, the triangles are congruent by 1.4 and the result is immediate; so assume at least one pair is unequal.) Join GH by P1.

**Step 3.** In triangles ABC and DGH, we have AB equal to DG (by construction), AC equal to DH (by construction), and angle BAC equal to angle GDH (since angle GDH is the same as angle EDF, which equals angle BAC by hypothesis). Therefore triangle ABC is congruent to triangle DGH by 1.4 (Side-Angle-Side). In particular, angle ABC equals angle DGH, angle ACB equals angle DHG, and BC equals GH.

**Step 4.** Since AB is to DE as AC is to DF (by hypothesis), and DG equals AB and DH equals AC (by construction), we have DG is to DE as DH is to DF, substituting equals by CN1.

**Step 5.** Since DG is to DE as DH is to DF, the sides DE and DF of triangle DEF are cut proportionally by the line GH at points G and H respectively. Therefore, by 6.2 (converse part), GH is parallel to EF.

**Step 6.** Since GH is parallel to EF, and DE is a straight line falling on these parallel lines, the alternate angles are equal. Specifically, angle DGH equals angle DEF, by 1.29.

**Step 7.** Similarly, since GH is parallel to EF, and DF is a straight line falling on these parallel lines, angle DHG equals angle DFE, by 1.29.

**Step 8.** Now we have established that in triangles DGH and DEF: angle GDH equals angle EDF (they are the same angle), angle DGH equals angle DEF (Step 6), and angle DHG equals angle DFE (Step 7). Therefore triangles DGH and DEF are equiangular.

**Step 9.** From Step 3, triangle ABC is congruent to triangle DGH, so angle ABC equals angle DGH and angle ACB equals angle DHG. From Steps 6 and 7, angle DGH equals angle DEF and angle DHG equals angle DFE. Therefore, by CN1, angle ABC equals angle DEF and angle ACB equals angle DFE. Together with the hypothesis that angle BAC equals angle EDF, the triangles ABC and DEF are equiangular, with equal angles subtended by corresponding sides.

**Step 10.** Therefore, if two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles are equiangular and have those angles equal which the corresponding sides subtend. Q.E.D.

**USED:** 1.29, 1.3, 1.4, 6.2, CN1, P1
**Human refs (from References field):** 1.23, 1.32, 1.4, 5.11, 5.9, 6.4
**Jaccard:** 0.091 — AI adds ['1.29', '1.3', '6.2', 'CN1', 'P1']; Human adds ['1.23', '1.32', '5.11', '5.9', '6.4']

#### Heath 人类证明原文

Let ABC, DEF be two triangles having one angle BAC equal to one angle EDF and the sides about the equal angles proportional, so that, as BA is to AC, so is ED to DF; I say that the triangle ABC is equiangular with the triangle DEF, and will have the angle ABC equal to the angle DEF, and the angle ACB to the angle DFE. For on the straight line DF, and at the points D, F on it, let there be constructed the angle FDG equal to either of the angles BAC, EDF, and the angle DFG equal to the angle ACB; [I. 23] therefore the remaining angle at B is equal to the remaining angle at G. [I. 32]  Therefore the triangle ABC is equiangular with the triangle DGF. Therefore, proportionally, as BA is to AC, so is GD to DF. [VI. 4] But, by hypothesis, as BA is to AC, so also is ED to DF; therefore also, as ED is to DF, so is GD to DF. [V. 11] Therefore ED is equal to DG; [V. 9] and DF is common; therefore the two sides ED, DF are equal to the two sides GD, DF; and the angle EDF is equal to the angle GDF; therefore the base EF is equal to the base GF, and the triangle DEF is equal to the triangle DGF, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend. [I. 4] Therefore the angle DFG is equal to the angle DFE, and the angle DGF to the angle DEF. But the angle DFG is equal to the angle ACB; therefore the angle ACB is also equal to the angle DFE. And, by hypothesis, the angle BAC is also equal to the angle EDF; therefore the remaining angle at B is also equal to the remaining angle at E; [I. 32] therefore the triangle ABC is equiangular with the triangle DEF.

#### 分类报告原文（Run B）

### 6.6
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Heath's proof constructs a triangle DGF equiangular with ABC by copying angles (I.23), then uses VI.4 to derive a proportion, and V.11/V.9 to show ED = DG, leading to congruence of DEF and DGF via I.4. The AI instead constructs a triangle DGH congruent to ABC by marking off equal segments on DE and DF (I.3), then uses the converse of 6.2 to show GH is parallel to EF from the proportional cutting, and I.29 to transfer alternate angles. These are fundamentally different backbones: Heath works through angle-copying, proportional similarity (VI.4), and proportion algebra (V.11, V.9), while the AI works through side-copying, proportional cutting (6.2 converse), and parallel-line angle transfer (I.29). Both paths are logically complete and valid, yielding classification D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：AI证明应小修，补写由对称性不妨设。

---

### D-7: Proposition 7.38（Run C）

**命题陈述：** If a number have any part whatever, it will be measured by a number called by the same name as the part.

#### AI 证明原文（Run C）

## Proposition 7.38
**Statement:** If a number have any part whatever, it will be measured by a number called by the same name as the part.

**Step 1.** Let the number A have a part, and let the part be called by the same name as the number C. We must show that C measures A.

**Step 2.** Let B be the part of A that is called by the same name as C. Since B is a part of A called by the same name as C, by the definition of parts and their naming (D7.3, D7.15), B is a 1/C-th part of A. This means that the unit measures C the same number of times that B measures A.

**Step 3.** Since B is a 1/C-th part of A, B measures A, and the number of times B measures A equals C. In other words, B multiplied by C produces A, that is, B added to itself as many times as there are units in C yields A (D7.15, D7.3).

**Step 4.** Since B multiplied by C produces A, then by Proposition 7.16, C multiplied by B also produces A. That is, C added to itself as many times as there are units in B yields A.

**Step 5.** Since C multiplied by B produces A, C measures A (D7.3, D7.5). The number of times C measures A is B.

**Step 6.** Therefore, if a number have any part whatever, it will be measured by a number called by the same name as the part. Q.E.D.

**USED:** 7.16, D7.15, D7.3, D7.5
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.16', 'D7.15', 'D7.3', 'D7.5']; Human adds ['7.15']

#### Heath 人类证明原文

For let the number A have any part whatever, B, and let C be a number called by the same name as the part B; I say that C measures A. For, since B is a part of A called by the same name as C, and the unit D is also a part of C called by the same name as it, therefore, whatever part the unit D is of the number C, the same part is B of A also; therefore the unit D measures the number C the same number of times that B measures A. Therefore, alternately, the unit D measures the number B the same number of times that C measures A. [VII. 15] Therefore C measures A.

#### 分类报告原文（Run C）

### 7.38
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same starting point (the part definition establishing that unit measures C the same number of times B measures A), but they diverge in how they reach the conclusion that C measures A. Heath applies VII.15 (alternation of unit measure) to directly swap the measuring relationship, concluding that C measures A. The AI instead converts the measuring relationship into a multiplication (B times C equals A), then applies VII.16 (commutativity of multiplication) to get C times B equals A, and infers from this that C measures A. These represent genuinely different logical backbones: alternation of ratios versus commutativity of multiplication. The AI's path is logically sound throughout, with each step properly justified by cited definitions and propositions, so Q3 confirms validity, yielding category D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-8: Proposition 8.26（Run A）

**命题陈述：** Similar plane numbers have to one another the ratio which a square number has to a square number.

#### AI 证明原文（Run A）

## Proposition 8.26
**Statement:** Similar plane numbers have to one another the ratio which a square number has to a square number.

**Step 1.** Let A and B be similar plane numbers with sides a, b and c, d respectively, so that A = a * b and B = c * d. Since A and B are similar plane numbers, by D7.21 their corresponding sides are proportional: a : c :: b : d.

**Step 2.** By 8.18, between two similar plane numbers there is one mean proportional number. Let M be the mean proportional between A and B, so that A, M, B are in continued proportion: A : M :: M : B. Furthermore, by 8.18, A has to B the ratio duplicate of that which the corresponding side a has to the corresponding side c. In particular, A : M :: a : c.

**Step 3.** Since A : M :: M : B (continued proportion) and A : M :: a : c, it follows by 5.11 that M : B :: a : c.

**Step 4.** Now consider the square numbers a * a and c * c, which are square numbers by D7.18. By 8.11, between the two square numbers a * a and c * c there is one mean proportional number, namely a * c, and the square a * a has to the square c * c the ratio duplicate of that which a has to c. That is, a * a : a * c :: a * c : c * c, and in particular a * a : a * c :: a : c.

**Step 5.** Since A : M :: a : c (from Step 2) and a * a : a * c :: a : c (from Step 4), by 5.11 we have A : M :: a * a : a * c.

**Step 6.** Since M : B :: a : c (from Step 3) and a * c : c * c :: a : c (from Step 4, since a * c : c * c :: a : c by the continued proportion in Step 4), by 5.11 we have M : B :: a * c : c * c.

**Step 7.** We now have A : M :: a * a : a * c (Step 5) and M : B :: a * c : c * c (Step 6). By 7.14 (ex aequali for numbers), A : B :: a * a : c * c.

**Step 8.** Since a * a and c * c are square numbers by D7.18, A and B have to one another the ratio which a square number has to a square number. This is what was to be proved.

**USED:** 5.11, 7.14, 8.11, 8.18, D5.9, D7.16, D7.18, D7.21
**Human refs (from References field):** 7.33, 8.18, 8.2
**Jaccard:** 0.100 — AI adds ['5.11', '7.14', '8.11', 'D5.9', 'D7.16', 'D7.18', 'D7.21']; Human adds ['7.33', '8.2']

#### Heath 人类证明原文

Let A, B be similar plane numbers; I say that A has to B the ratio which a square number has to a square number. For, since A, B are similar plane numbers, therefore one mean proportional number falls between A, B. [VIII. 18] Let it so fall, and let it be C; and let D, E, F, the least numbers of those which have the same ratio with A, C, B, be taken; [VII. 33 or VIII. 2] therefore the extremes of them D, F are square. [VIII. 2] And since, as D is to F, so is A to B, and D, F are square, therefore A has to B the ratio which a square number has to a square number.

#### 分类报告原文（Run A）

### 8.26
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decides this classification. Heath's proof finds the least numbers D, E, F in the same ratio as A, C, B (using 7.33/8.2), shows the extremes D, F are square (8.2), and concludes from D:F = A:B. The AI takes a fundamentally different path: it decomposes the similar plane numbers into their sides (a,b and c,d), establishes the mean proportional via 8.18, uses 8.11 to find the mean proportional between the square numbers a^2 and c^2, then applies 5.11 (transitivity of ratios) and 7.14 (ex aequali) to conclude A:B = a^2:c^2. The two backbones differ in their key intermediate conclusions — Heath works through least numbers in ratio while the AI works through the sides' squares directly. Both paths are logically complete, so the classification is D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-9: Proposition 9.2（Run A）

**命题陈述：** If two numbers by multiplying one another make a square number, they are similar plane numbers.

#### AI 证明原文（Run A）

## Proposition 9.2
**Statement:** If two numbers by multiplying one another make a square number, they are similar plane numbers.

**Step 1.** Let A and B be two numbers such that A multiplied by B makes a square number C. We must show that A and B are similar plane numbers.

**Step 2.** Since C is a square number, by Definition D7.18 (a square number is equal multiplied by equal), there exists a number k such that C = k multiplied by k. That is, A multiplied by B equals k multiplied by k.

**Step 3.** Since the product of A and B equals the product of k and k, by Proposition 7.19 (the converse part: if the number produced from the first and fourth equals the number produced from the second and third, the four numbers are proportional), the numbers A, k, k, B are proportional. That is, A is to k as k is to B.

**Step 4.** Therefore k is one mean proportional number falling between A and B.

**Step 5.** Since one mean proportional number falls between A and B, by Proposition 8.20 (if one mean proportional number falls between two numbers, those numbers are similar plane numbers), A and B are similar plane numbers (D7.21).

**Step 6.** Therefore, if two numbers by multiplying one another make a square number, they are similar plane numbers. Q.E.D.

**USED:** 7.19, 8.20, D7.18, D7.21
**Human refs (from References field):** 7.17, 8.18, 8.20, 8.8
**Jaccard:** 0.143 — AI adds ['7.19', 'D7.18', 'D7.21']; Human adds ['7.17', '8.18', '8.8']

#### Heath 人类证明原文

Let A, B be two numbers, and let A by multiplying B make the square number C; I say that A, B are similar plane numbers. For let A by multiplying itself make D; therefore D is square. Now, since A by multiplying itself has made D, and by multiplying B has made C, therefore, as A is to B, so is D to C. [VII. 17] And, since D is square, and C is so also, therefore D, C are similar plane numbers. Therefore one mean proportional number falls between D, C. [VIII. 18] And, as D is to C, so is A to B; therefore one mean proportional number falls between A, B also. [VIII. 8] But, if one mean proportional number fall between two numbers, they are similar plane numbers; [VIII. 20] therefore A, B are similar plane numbers.

#### 分类报告原文（Run A）

### 9.2
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof introduces D = A*A, establishes A:B = D:C via 7.17, argues D and C are similar plane numbers (both square), uses 8.18 to get a mean proportional between D and C, then transfers that mean proportional to A and B via 8.8, and finally applies 8.20. The AI takes a fundamentally different path: it decomposes C = k*k by the definition of square number (D7.18), observes A*B = k*k, and directly applies the converse of 7.19 to conclude A:k = k:B, establishing k as a mean proportional between A and B without the intermediate auxiliary square D or the transfer via 8.8. Both proofs share only 8.20 as the final step. The AI's path is logically sound — 7.19's converse validly yields proportionality from equal products — but the key intermediate conclusions differ entirely, making this a genuine path difference.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-10: Proposition 9.12（Run A）

**命题陈述：** If as many numbers as we please beginning from an unit be in continued proportion, by however many prime numbers the last is measured, the next to the unit will also be measured by the same.

#### AI 证明原文（Run A）

## Proposition 9.12
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, by however many prime numbers the last is measured, the next to the unit will also be measured by the same.

**Step 1.** Let there be as many numbers as we please beginning from the unit in continued proportion: 1, A, B, C, ..., L, where A is the term next to the unit and L is the last term. Suppose a prime number p measures L. We must show that p also measures A.

**Step 2.** We proceed by considering the number of terms. First, if there are only two terms, namely 1 and A, then L is A itself, and since p measures A, the conclusion holds immediately.

**Step 3.** If there are three terms, 1, A, B, then the continued proportion gives 1:A = A:B. By 7.19, since four numbers are proportional (1, A, A, B), the product of the first and fourth equals the product of the second and third, so 1 * B = A * A, that is, B = A * A. Since p is prime and p measures B = A * A, by 7.30, p measures one of the two factors, hence p measures A.

**Step 4.** Now suppose there are more than three terms: 1, A, B, C, ..., K, L, where K is the term immediately before L. From the continued proportion, the ratio of each consecutive pair is the same, so in particular 1:A = K:L. By 7.19, 1 * L = A * K, that is, L = A * K. This means A multiplied by K produces L (D7.15).

**Step 5.** Since p is prime and p measures L, and L is the product of A and K, by 7.30, p measures at least one of A or K.

**Step 6.** If p measures A, we are done.

**Step 7.** If p measures K, we observe that K is itself the last term of the shorter continued proportion 1, A, B, ..., K, which begins from the unit and has one fewer term than the original sequence, with A still being the term next to the unit.

**Step 8.** We now apply the same argument to this shorter sequence. The term before K in the continued proportion is some term J, and by the same reasoning (using 7.19), K = A * J. Since p measures K and K is the product of A and J, by 7.30, p measures A or p measures J.

**Step 9.** Continuing this descent through successively shorter sequences, at each stage either p measures A (and we are done) or p measures the preceding term in the proportion. Since the sequence is finite and decreasing in length, this process must eventually terminate.

**Step 10.** The descent terminates at the latest when we reach the sequence 1, A, B (three terms), at which point B = A * A as shown in Step 3, and since p is prime and measures B, by 7.30, p measures A.

**Step 11.** Therefore, in all cases, the prime p measures the term next to the unit A. Since p was an arbitrary prime measuring the last term, by however many prime numbers the last is measured, the next to the unit will also be measured by the same. Q.E.D.

**USED:** 7.19, 7.30, D7.15
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, 9.11, 9.8, D7.14
**Jaccard:** 0.111 — AI adds ['7.30', 'D7.15']; Human adds ['7.20', '7.21', '7.29', '9.11', '9.8', 'D7.14']

#### Heath 人类证明原文

Let there be as many numbers as we please, A, B, C, D, beginning from an unit, and in continued proportion; I say that, by however many prime numbers D is measured, A will also be measured by the same. For let D be measured by any prime number E; I say that E measures A. For suppose it does not; now E is prime, and any prime number is prime to any which it does not measure; [VII. 29] therefore E, A are prime to one another. And, since E measures D, let it measure it according to F, therefore E by multiplying F has made D. Again, since A measures D according to the units in C, [IX. 11 and Por.] therefore A by multiplying C has made D. But, further, E has also by multiplying F made D; therefore the product of A, C is equal to the product of E, F. Therefore, as A is to E, so is F to C. [VII. 19] But A, E are prime, primes are also least, [VII. 21] and the least measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent; [VII. 20] therefore E measures C. Let it measure it according to G; therefore E by multiplying G has made C. But, further, by the theorem before this, A has also by multiplying B made C. [IX. 11 and Por.] Therefore the product of A, B is equal to the product of E, G. Therefore, as A is to E, so is G to B. [VII. 19] But A, E are prime, primes are also least, [VII. 21] and the least numbers measure those which have the same ratio with them the same number of times, the antecedent the antecedent and the consequent the consequent: [VII. 20] therefore E measures B. Let it measure it according to H; therefore E by multiplying H has made B. But further A has also by multiplying itself made B; [IX. 8] therefore the product of E, H is equal to the square on A. Therefore, as E is to A, so is A to H. [VII. 19] But A, E are prime, primes are also least, [VII. 21] and the least measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent; [VII. 20] therefore E measures A, as antecedent antecedent. But, again, it also does not measure it: which is impossible. Therefore E, A are not prime to one another. Therefore they are composite to one another. But numbers composite to one another are measured by some number. [VII. Def. 14] And, since E is by hypothesis prime, and the prime is not measured by any number other than itself, therefore E measures A, E, so that E measures A. [But it also measures D; therefore E measures A, D.] Similarly we can prove that, by however many prime numbers D is measured, A will also be measured by the same.

#### 分类报告原文（Run A）

### 9.12
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 determined this classification. Heath's proof uses proof by contradiction, assuming the prime E does not measure A, then descending through the specific chain D to C to B to A-squared using ratio and proportion arguments (7.19, 7.20, 7.21) combined with the coprimality result (7.29), ultimately reaching a contradiction. The AI proof takes a fundamentally different approach: it uses induction on the number of terms in the continued proportion, applying 7.30 (if a prime divides a product it divides a factor) at each step. The AI decomposes L = A*K via 7.19 from the proportion 1:A = K:L, then uses 7.30 to conclude p|A or p|K, descending to shorter sequences until the base case of three terms where B = A*A and 7.30 gives p|A. The key intermediate conclusions differ entirely: Heath establishes E|C, then E|B, then E|A via contradiction; the AI establishes a descent through 7.30 at each level. The proof-tree containment test confirms this is genuine path divergence rather than citation-depth difference: while 7.30 does subsume 7.29, 7.21, and 7.20 from heath_only, the remaining heath_only items 9.11 and 9.8 are not inside Heath's proof of 7.30, and more importantly the overall proof architecture (contradiction vs induction) is different. The AI proof is logically complete under the hardened 1(b) standard, so Q3 confirms category D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-11: Proposition 9.18（Run A）

**命题陈述：** Given two numbers, to investigate whether it is possible to find a third proportional to them.

#### AI 证明原文（Run A）

## Proposition 9.18
**Statement:** Given two numbers, to investigate whether it is possible to find a third proportional to them.

**Step 1.** Let A and B be two given numbers. We investigate whether it is possible to find a number C such that A : B = B : C, i.e., a third proportional to A and B.

**Step 2.** Let D be the number produced by B multiplied by B, so that D = B * B. [D7.15]

**Step 3.** Now there are two cases: either A measures D, or A does not measure D.

**Step 4.** First, suppose A measures D. Then there exists a number C such that D = A * C, that is, A * C = B * B. [D7.3]

**Step 5.** Since A * C = B * B, the number produced from the first (A) and fourth (C) equals the number produced from the second (B) and third (B). Therefore by 7.19 (converse part), the four numbers A, B, B, C are proportional, that is, A : B = B : C. [7.19, D7.20]

**Step 6.** Thus C is a third proportional to A and B, and it has been found.

**Step 7.** Now suppose A does not measure D (where D = B * B). We claim no third proportional to A and B exists.

**Step 8.** For suppose, by way of contradiction, that there exists a number C such that A : B = B : C. Then since these four numbers are proportional, by 7.19, the product A * C equals B * B, that is, A * C = D. [7.19]

**Step 9.** But then A measures D, since D = A * C. This contradicts our assumption that A does not measure D. [D7.3]

**Step 10.** Therefore, when A does not measure B * B, it is not possible to find a third proportional to A and B.

**Step 11.** Hence, given two numbers A and B, a third proportional to them exists if and only if A measures the product of B with itself. Q.E.D.

**USED:** 7.19, D7.15, D7.20, D7.3
**Human refs (from References field):** 7.19, 9.16
**Jaccard:** 0.200 — AI adds ['D7.15', 'D7.20', 'D7.3']; Human adds ['9.16']

#### Heath 人类证明原文

Let A, B be the given two numbers, and let it be required to investigate whether it is possible to find a third proportional to them. Now A, B are either prime to one another or not. And, if they are prime to one another, it has been proved that it is impossible to find a third proportional to them. [IX. 16] Next, let A, B not be prime to one another, and let B by multiplying itself make C. Then A either measures C or does not measure it. First, let it measure it according to D; therefore A by multiplying D has made C. But, further, B has also by multiplying itself made C; therefore the product of A, D is equal to the square on B. Therefore, as A is to B, so is B to D; [VII. 19] therefore a third proportional number D has been found to A, B. Next, let A not measure C; I say that it is impossible to find a third proportional number to A, B. For, if possible, let D, such third proportional, have been found. Therefore the product of A, D is equal to the square on B. But the square on B is C; therefore the product of A, D is equal to C. Hence A by multiplying D has made C; therefore A measures C according to D. But, by hypothesis, it also does not measure it: which is absurd. Therefore it is not possible to find a third proportional number to A, B when A does not measure C.

#### 分类报告原文（Run A）

### 9.18
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Classification was decided at Q2/Q3. Heath's proof first distinguishes whether A and B are prime to one another, invoking 9.16 to dismiss that case, then handles the non-prime situation by checking whether A measures B-squared. The AI proof omits the prime/not-prime distinction entirely and uses a single exhaustive dichotomy: either A measures B-squared or it does not. This is a genuinely different logical backbone -- Heath has a three-branch structure (prime, not-prime-and-measures, not-prime-and-does-not-measure) while the AI has a two-branch structure (measures, does-not-measure). The AI's approach is valid because the measure/not-measure dichotomy is exhaustive and the prime case is subsumed under the not-measuring case. Both proofs share the core use of 7.19 for the positive case and contradiction for the negative case, but the structural difference in case organization and the AI's omission of 9.16 constitute a different path rather than mere granularity difference. The AI's path is logically complete and sound, yielding classification D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-12: Proposition 9.27（Run C）

**命题陈述：** If from an odd number an even number be subtracted, the remainder will be odd.

#### AI 证明原文（Run C）

## Proposition 9.27
**Statement:** If from an odd number an even number be subtracted, the remainder will be odd.

**Step 1.** Let A be an odd number, and let the even number B be subtracted from A, leaving the remainder C, so that A = B + C.

**Step 2.** Suppose, for the sake of contradiction, that C is even.

**Step 3.** Since B is even and C is even, by Proposition 9.21 (if as many even numbers as we please be added together, the whole is even), their sum B + C is even.

**Step 4.** But B + C equals A, so A would be even.

**Step 5.** This contradicts the hypothesis that A is odd (D7.7: an odd number is not divisible into two equal parts, and so is not even per D7.6).

**Step 6.** Therefore the assumption that C is even is false, and hence C is odd. Q.E.D.

**USED:** 9.21, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.250 — AI adds ['9.21', 'D7.6']; Human adds ['9.24']

#### Heath 人类证明原文

For from the odd number AB let the even number BC be subtracted; I say that the remainder CA is odd. Let the unit AD be subtracted; therefore DB is even. [VII. Def. 7] But BC is also even; therefore the remainder CD is even. [IX. 24] Therefore CA is odd. [VII. Def. 7]

#### 分类报告原文（Run C）

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Classification was decided at Q2/Q3. Heath proves the proposition directly by subtracting a unit from the odd number AB to get even DB, then using 9.24 (even minus even is even) to show that the intermediate segment CD is even, and finally applying Def. 7.7 to conclude the remainder CA is odd. The AI instead uses proof by contradiction: assuming the remainder C is even, it applies 9.21 (sum of even numbers is even) to B + C to derive that A would be even, contradicting the hypothesis. These represent fundamentally different logical backbones -- Heath uses direct decomposition via unit subtraction and even-minus-even (9.24), while the AI uses reductio ad absurdum with sum-of-evens (9.21). The AI's contradictory path is logically complete and valid, so this is a path difference (D).

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-13: Proposition 10.36（Run A）

**命题陈述：** If two rational straight lines commensurable in square only be added together, the whole is irrational; and let it be called binomial.

#### AI 证明原文（Run A）

## Proposition 10.36
**Statement:** If two rational straight lines commensurable in square only be added together, the whole is irrational; and let it be called binomial.

**Step 1.** Let AB and BC be two rational straight lines commensurable in square only. Set AC equal to AB together with BC; we must show that AC is irrational.

**Step 2.** Since AC is cut at B, by Proposition 2.4, the square on AC is equal to the sum of the squares on AB and BC together with twice the rectangle contained by AB and BC. That is, sq(AC) = sq(AB) + sq(BC) + 2*rect(AB, BC).

**Step 3.** Since AB and BC are rational, the squares on AB and on BC are each rational areas (by Definition D10.1.3 and D10.1.4, rational straight lines have rational squares). Since AB and BC are commensurable in square, sq(AB) is commensurable with sq(BC) (by Definition D10.1.2). Therefore, by Proposition 10.15, the sum sq(AB) + sq(BC) is commensurable with each of sq(AB) and sq(BC), and hence sq(AB) + sq(BC) is a rational area.

**Step 4.** Since AB and BC are rational straight lines commensurable in square only, by Proposition 10.21, the rectangle contained by AB and BC is irrational, and the side of the square equal to it is called medial. That is, rect(AB, BC) is a medial (and hence irrational) area.

**Step 5.** Now suppose, for the sake of contradiction, that AC is rational. Then the square on AC would be a rational area (by D10.1.4).

**Step 6.** Since sq(AC) would be rational and sq(AB) + sq(BC) is rational (from Step 3), both are commensurable with the square on the assigned rational straight line. By Proposition 10.12, two areas each commensurable with the same area are commensurable with one another, so sq(AC) and sq(AB) + sq(BC) would be commensurable with each other.

**Step 7.** From Step 2, we have 2*rect(AB, BC) = sq(AC) - sq(AB) - sq(BC). Since sq(AC) and sq(AB) + sq(BC) are commensurable (by Step 6), by Proposition 10.15, the whole sq(AC) being commensurable with the part sq(AB) + sq(BC) implies that the remainder 2*rect(AB, BC) is also commensurable with sq(AC). Since sq(AC) is rational, 2*rect(AB, BC) would therefore be a rational area.

**Step 8.** Since 2*rect(AB, BC) is in the ratio 2:1 to rect(AB, BC), and this is the ratio of a number to a number, by Proposition 10.6, rect(AB, BC) is commensurable with 2*rect(AB, BC). If 2*rect(AB, BC) were rational, then rect(AB, BC) would be commensurable with a rational area, and hence rational itself (by D10.1.4 and 10.12).

**Step 9.** But this contradicts Step 4, which established that rect(AB, BC) is irrational (medial). Therefore the assumption in Step 5 is false, and AC cannot be rational.

**Step 10.** Therefore AC is irrational. And let such a line, the sum of two rational straight lines commensurable in square only, be called binomial. Q.E.D.

**USED:** 10.12, 10.15, 10.21, 10.6, 2.4, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.4, D10.1.4
**Jaccard:** 0.364 — AI adds ['10.12', '10.21', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.13', '10.16']

#### Heath 人类证明原文

For let two rational straight lines AB, BC commensurablein square only be added together; I say that the whole AC is irrational. For, since AB is incommensurable in length with BC —for they are commensurable in square only— and, as AB is to BC, so is the rectangle AB, BC to the square on BC, therefore the rectangle AB, BC is incommensurable with the square on BC. [X. 11] But twice the rectangle AB, BC is commensurable with the rectangle AB, BC [X. 6], and the squares on AB, BC are commensurable with the square on BC —for AB, BC are rational straight lines commensurable in square only— [X. 15] therefore twice the rectangle AB, BC is incommensurablewith the squares on AB, BC. [X. 13] And, componendo, twice the rectangle AB, BC together with the squares on AB, BC, that is, the square on AC [II. 4], is incommensurable with the sum of the squares on AB, BC. [X. 16] But the sum of the squares on AB, BC is rational;therefore the square on AC is irrational, so that AC is also irrational. [X. Def. 4] And let it be called binomial.

#### 分类报告原文（Run A）

### 10.36
**Category**: Path difference
**Jaccard**: 0.364
**Analysis**: Q2 determined the classification. Heath proves the irrationality of AC directly by building an incommensurability chain: using 10.11 to show rect(AB,BC) is incommensurable with sq(BC), then 10.13 to show 2*rect(AB,BC) is incommensurable with sq(AB)+sq(BC), and 10.16 to show sq(AC) is incommensurable with the rational sum sq(AB)+sq(BC). The AI instead uses a proof by contradiction: it invokes 10.21 to establish that rect(AB,BC) is medial (irrational), then assumes AC is rational and derives that rect(AB,BC) would have to be rational (using 10.12 for transitivity of commensurability), contradicting its mediality. The key intermediate conclusions differ fundamentally: Heath never uses 10.21 or proof by contradiction, and the AI never establishes the incommensurability chain through 10.11, 10.13, and 10.16. The containment test confirms this is a genuine path difference since heath_only items 10.13 and 10.16 do not appear inside the proof of 10.21 (the AI's key differentiating citation). The AI's contradictory path is logically valid, so the classification is D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-14: Proposition 10.78（Run C）

**命题陈述：** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the sum of the squares on them medial, twice the rectangle contained by them medial, and further the squares on them incommensurable with twice the rectangle contained by them, the remainder is irrational; and let it be called that which produces with a medial area a medial whole.

#### AI 证明原文（Run C）

## Proposition 10.78
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the sum of the squares on them medial, twice the rectangle contained by them medial, and further the squares on them incommensurable with twice the rectangle contained by them, the remainder is irrational; and let it be called that which produces with a medial area a medial whole.

**Step 1.** Let AB be a straight line, and from AB let BC be subtracted, where BC is incommensurable in square with AB, the sum of the squares on AB and BC is medial, twice the rectangle contained by AB and BC is medial, and the sum of the squares on AB and BC is incommensurable with twice the rectangle contained by AB and BC. We must show that the remainder AC is irrational.

**Step 2.** Set out a rational straight line DI. To DI apply the area DE equal to the sum of the squares on AB and BC, producing breadth DG. To DI apply the area DF equal to twice the rectangle contained by AB and BC, producing breadth DH, where DF is subtracted from DE (so that H falls between D and G). Then the remaining area HG (that is, DE minus DF) applied to DI has breadth HG corresponding to the square on AC.

**Step 3.** By 2.7, the squares on AB and BC together are equal to twice the rectangle AB, BC together with the square on AC. Therefore the square on AC equals the sum of the squares on AB and BC minus twice the rectangle AB, BC, which is the area HG applied to DI.

**Step 4.** Since the sum of the squares on AB and BC is medial, the area DE is medial. This medial area DE is applied to the rational straight line DI. By 10.22, the breadth DG is rational and incommensurable in length with DI.

**Step 5.** Since twice the rectangle contained by AB and BC is medial, the area DF is medial. This medial area DF is applied to the rational straight line DI. By 10.22, the breadth DH is rational and incommensurable in length with DI.

**Step 6.** Since the sum of the squares on AB and BC is incommensurable with twice the rectangle contained by AB and BC, the area DE is incommensurable with the area DF. But DE is the rectangle DI by DG, and DF is the rectangle DI by DH. Therefore the rectangle DI by DG is incommensurable with the rectangle DI by DH. By 6.1, as DG is to DH, so is the rectangle DI by DG to the rectangle DI by DH. Therefore DG is incommensurable in length with DH, by 10.11.

**Step 7.** Both DG and DH are rational (from Steps 4 and 5). Since DG and DH are rational and incommensurable in length, they are commensurable in square only. Therefore by 10.21, the rectangle contained by DG and DH is irrational, and by 10.36, their sum DG + DH is a binomial, which is irrational. However, what we need is that their difference is irrational.

**Step 8.** Since DG and DH are each incommensurable in length with DI (Steps 4 and 5), and they are incommensurable in length with each other (Step 6), we have that DG and DH are rational straight lines commensurable in square only. Consider the breadth HG, which corresponds to the difference DG minus DH. By 10.73, since DG is rational and DH is rational and commensurable with DG in square only, the remainder HG (that is, DG minus DH) is irrational; it is an apotome.

**Step 9.** The area corresponding to the square on AC is the rectangle DI by HG. Now DI is rational and HG is an apotome (from Step 8). However, we need to determine what kind of irrational the side of this rectangle is, which will tell us about AC.

**Step 10.** We reconsider the structure more directly. The area equal to the square on AC is the difference of two medial areas (DE minus DF) that are incommensurable with each other. By 10.72, when two medial areas incommensurable with one another are added together, the side is either a second bimedial or a side of the sum of two medial areas. For the subtractive case, we apply the analogous reasoning.

**Step 11.** We proceed to show that the square on AC is neither rational nor medial, and that AC does not belong to any previously classified irrational type. The square on AC equals the sum of the squares on AB and BC minus twice the rectangle AB, BC. Since the sum of the squares on AB and BC is medial, the square on AC is not rational (for if it were, then the sum of the squares on AB, BC would be the sum of a rational area and a medial area, namely twice the rectangle; but the sum of the squares is medial, and a medial area cannot equal the sum of a rational and a medial area by 10.26 and the properties of rational and medial areas).

**Step 12.** Suppose the square on AC were rational. Then the area HG on DI is rational. The area DE equals DF plus HG. Since DE is medial and HG would be rational, DF would equal DE minus HG. But DE is medial and DF is medial, and their difference HG would be rational. By 10.26, a medial area does not exceed a medial area by a rational area. This is a contradiction. Therefore the square on AC is not rational, so AC is not rational.

**Step 13.** Suppose the square on AC were medial. Then the area HG on DI is medial, and by 10.22, the breadth HG is rational and incommensurable in length with DI. Now both DG and HG would be rational, and since DE equals DF plus the area for the square on AC, the three areas DE, DF, and the area for the square on AC are all medial. The area DE (on DI with breadth DG) is medial, and the area for the square on AC (on DI with breadth HG) is medial. Then DF = DE minus the area for AC squared, which means DF is the difference of two medial areas. But DF is itself medial. We need to check commensurability. Since DE is incommensurable with DF (given), and DE equals DF plus the area of AC squared, the area of AC squared is incommensurable with DF. So the area of AC squared is incommensurable with DF, meaning HG is incommensurable with DH (by 6.1 and 10.11). But also from the medial area for AC squared applied to DI, HG is rational and incommensurable in length with DI. Now DH is also rational and incommensurable in length with DI. And HG is incommensurable in length with DH. So DG = DH + HG. Since DG, DH, and HG are all rational, and DH and HG are incommensurable in length, by 10.36, DG = DH + HG is a binomial, which is irrational. But DG is rational (Step 4). This is a contradiction. Therefore the square on AC is not medial.

**Step 14.** Since the square on AC is neither rational nor medial, AC is irrational and is neither rational nor medial. The square on AC equals the excess of a medial area over a medial area, where the two medial areas are incommensurable. This configuration (subtracting from a straight line a part incommensurable in square with the whole, where the squares sum to a medial, twice the rectangle is medial, and these are incommensurable) produces an irrational remainder distinct from those previously classified. Let AC be called that which produces with a medial area a medial whole.

**Step 15.** To confirm the name: if one constructs a rectangle on AC equal to a medial area, the resulting figure relates to medial areas in the manner indicated. The remainder AC is irrational, and it is called that which produces with a medial area a medial whole. This completes the proof.

**USED:** 10.11, 10.22, 10.26, 10.36, 10.73, 2.7, 6.1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.35, 10.73, 2.7, 6.1
**Jaccard:** 0.455 — AI adds ['10.26', '10.36', 'D10.1.3', 'D10.1.4']; Human adds ['10.20', '10.35']

#### Heath 人类证明原文

For from the straight line AB let there be subtracted the straight line BC incommensurable in square with AB and fulfilling the given conditions; [X. 35] I say that the remainder AC is the irrational straight line called that which produces with a medial area a medial whole. For let a rational straight line DI be set out, to DI let there be applied DE equal to the squares on AB, BC, producing DG as breadth, and let DH equal to twice the rectangle AB, BC be subtracted. Therefore the remainder FE is equal to the square on AC, [II. 7] so that AC is the “side” of FE. Now, since the sum of the squares on AB, BC is medial and is equal to DE, therefore DE is medial. And it is applied to the rational straight line DI, producing DG as breadth; therefore DG is rational and incommensurable in length with DI. [X. 22] Again, since twice the rectangle AB, BC is medial and is equal to DH, therefore DH is medial. And it is applied to the rational straight line DI, producing DF as breadth; therefore DF is also rational and incommensurable in length with DI. [X. 22] And, since the squares on AB, BC are incommensurable with twice the rectangle AB, BC, therefore DE is also incommensurable with DH. But, as DE is to DH, so also is DG to DF; [VI. 1] therefore DG is incommensurable with DF. [X. 11] And both are rational; therefore GD, DF are rational straight lines commensurable in square only. Therefore FG is an apotome. [X. 73] And FH is rational; but the rectangle contained by a rational straight line and an apotome is irrational, [deduction from X. 20] and its “side” is irrational. And AC is the “side” of FE; therefore AC is irrational. And let it be called that which produces with a medial area a medial whole.

#### 分类报告原文（Run C）

### 10.78
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Both proofs share the same backbone through four key intermediate conclusions: setting up areas on a rational line DI, establishing that the breadths DG and DH (or DF) are rational and incommensurable in length with DI (via X.22), showing DG is incommensurable with DH/DF (via VI.1 and X.11), and concluding that the difference HG/FG is an apotome (via X.73). However, the proofs diverge at the final step of establishing irrationality. Heath directly applies a deduction from X.20 (that the rectangle of a rational line and an apotome is irrational) to conclude AC is irrational. The AI instead takes an independent indirect route in Steps 10-14, proving by contradiction that the square on AC is neither rational (using 10.26, that a medial area does not exceed a medial area by a rational area) nor medial (using 10.36, that the sum of two rational lines commensurable in square only is a binomial, which contradicts DG being rational). These additional intermediate conclusions (square on AC is not rational, square on AC is not medial) are substantive facts argued by the AI but entirely absent from Heath, causing Case A of Q2 to fail. Under Q3, the AI's different path is logically valid, so the classification is D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-15: Proposition 11.33（Run C）

**命题陈述：** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

#### AI 证明原文（Run C）

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

**Step 1.** Let AB and CD be similar parallelepipedal solids, and let AE be a side of AB corresponding to the side CF of CD. We are to show that solid AB is to solid CD in the triplicate ratio of AE to CF.

**Step 2.** Since AB and CD are similar parallelepipedal solids, by D11.9 and D6.1 the corresponding edges are proportional. Let the three edges of AB meeting at one vertex be AE, AG, AH, and let the corresponding edges of CD meeting at one vertex be CF, CK, CL. Then AE:CF = AG:CK = AH:CL, and the solid angles at A and C are equal [D11.9, D6.1].

**Step 3.** Produce the edge AE to N, and make EN a third proportional to AE and CF, so that AE:CF = CF:EN [6.11]. Then produce AE further to X, and make NX a third proportional to CF and EN, so that CF:EN = EN:NX [6.11]. Thus AE, CF, EN, NX are in continued proportion.

**Step 4.** On AE, construct the parallelepipedal solid AO similar and similarly situated to CD, using 11.27. On CF, construct the parallelepipedal solid CP similar and similarly situated to CD, using 11.27. Since CP is similar and similarly situated to CD and is constructed on the same edge CF, the solid CP equals the solid CD [D11.10, CN4].

**Step 5.** Since the solid AO is similar to CD, and AE is the edge of AO corresponding to CF of CD, the three edges of AO at vertex A are to the three edges of CD at vertex C as AE is to CF [D6.1]. Therefore the edges of AO at A are AE, AG', AH' where AG' = AE·(CK/CF) and AH' = AE·(CL/CF).

**Step 6.** Now construct on EN a parallelepiped EW similar and similarly situated to CD [11.27]. The edges of EW at vertex E are EN, EN·(CK/CF), EN·(CL/CF). Similarly, all edges of EW bear the same ratio to the corresponding edges of AO as EN does to AE.

**Step 7.** Consider the solids AO and EW. They are similar (both similar to CD). The solid AO has edge AE corresponding to edge EN of EW, and AE:CF = CF:EN, so AE:EN = (AE:CF)·(CF:EN). We shall use the solids AO and EW as intermediaries.

**Step 8.** Consider the solid AO on base with edges AE and AG'. The solid EW has corresponding base with edges EN and EG'' where AG':EG'' = AE:EN (since both are similar to CD). By 11.25, parallelepipedal solids on the same base cut by parallel planes have the ratio of their heights. More precisely, since AO and EW are similar to each other, we proceed by comparing solids that share two dimensions.

**Step 9.** Construct on AE a parallelepiped P1 with edges AE, AG', and EL' where EL' equals the third edge of EW (i.e., EN·(CL/CF)). Then P1 and AO share the base determined by AE and AG', but differ in their third edges AH' and EL'. Since AH' = AE·(CL/CF) and EL' = EN·(CL/CF), we have AH':EL' = AE:EN. By 11.25, solid AO : solid P1 = AH' : EL' = AE : EN.

**Step 10.** Construct on AE a parallelepiped P2 with edges AE, EG'' (= EN·(CK/CF)), and EL' (= EN·(CL/CF)). Then P1 and P2 share the edges AE and EL', and their bases with edge AE are parallelograms with the other sides AG' and EG'' respectively. Since AG' = AE·(CK/CF) and EG'' = EN·(CK/CF), we have AG':EG'' = AE:EN. By 11.25 (applied to solids with one pair of opposite faces in the same planes), solid P1 : solid P2 = AG' : EG'' = AE : EN.

**Step 11.** Now P2 and EW have the same three edge-directions. P2 has edges AE, EG'', EL' and EW has edges EN, EG'', EL'. They share two edges EG'' and EL', and differ in the edges AE and EN. By 11.32 (parallelepipeds of the same height are as their bases), and 11.25, solid P2 : solid EW = AE : EN.

**Step 12.** Combining Steps 9, 10, and 11 by 5.22 (ex aequali in proportion): solid AO : solid EW = (AE:EN) composed three times. Since AE:CF = CF:EN from Step 3, we have AE:EN = the duplicate ratio of AE:CF [D5.9]. Therefore AE:EN composed with AE:EN once more gives the ratio composed three times. But more precisely: solid AO : solid P1 = AE:EN, solid P1 : solid P2 = AE:EN, solid P2 : solid EW = AE:EN.

**Step 13.** From Step 3, we have AE, CF, EN in continued proportion. Thus AE:CF = CF:EN. By D5.9, AE:EN is the duplicate ratio of AE:CF. Now consider the three ratios solid AO : P1, P1 : P2, P2 : EW, each equal to AE:EN. By 5.22 (ex aequali), solid AO : solid EW is the ratio compounded of these three, each equal to AE:EN.

**Step 14.** However, we need the triplicate ratio of AE:CF, not of AE:EN. Let us reconsider the construction. Return to the continued proportion AE, CF, EN, NX from Step 3. By D5.10, AE has to NX the triplicate ratio of that which AE has to CF, since AE:CF = CF:EN = EN:NX is a continued proportion of four terms.

**Step 15.** Now we directly compare the similar solids by reducing to one dimension at a time. The solid AO is similar and similarly situated to CD with corresponding edge AE to CF. Consider the parallelepipedal solid AO with edges AE, AG', AH' at vertex A, where AE:CF = AG':CK = AH':CL.

**Step 16.** Construct on CF a parallelepiped Q1 with edges CF, CK, CL (this is just the solid CD itself). Construct on CF a parallelepiped Q2 with edges CF, CK, AH'. Then Q2 and CD share the base with edges CF and CK, but have third edges AH' and CL respectively. By 11.25, Q2:CD = AH':CL = AE:CF.

**Step 17.** Construct on CF a parallelepiped Q3 with edges CF, AG', AH'. Then Q3 and Q2 share the edges CF and AH', while their bases with edge CF have the other sides AG' and CK respectively. By 11.32, since they have the same height, Q3:Q2 = (base of Q3):(base of Q2). The bases are parallelograms with one common side CF, and the other sides AG' and CK. By 6.1, the ratio of parallelograms with equal heights equals the ratio of their bases, so Q3:Q2 = AG':CK = AE:CF.

**Step 18.** Now compare the solid AO (with edges AE, AG', AH') with Q3 (with edges CF, AG', AH'). These two solids share the edges AG' and AH', and differ in the edges AE and CF. By 11.32, solid AO : Q3 = (base of AO containing edge AG') : (base of Q3 containing edge AG'). These bases are parallelograms with one common side AG', and the other sides AE and CF. By 6.1, AO:Q3 = AE:CF.

**Step 19.** From Steps 16, 17, and 18: AO:Q3 = AE:CF, Q3:Q2 = AE:CF, Q2:CD = AE:CF. By 5.22 (ex aequali), solid AO : solid CD = the ratio compounded of AE:CF taken three times.

**Step 20.** Since AE, CF, EN, NX are four terms in continued proportion (Step 3), by D5.10, AE has to NX the triplicate ratio of AE to CF. The ratio compounded of AE:CF three times equals AE:NX [5.22, D5.10]. Therefore solid AO : solid CD = AE : NX, which is the triplicate ratio of AE:CF.

**Step 21.** But solid AO was constructed similar and similarly situated to CD on edge AE. Since AB is also similar and similarly situated to CD (given), and both AO and AB are constructed on the same edge AE with the same solid angle at A, the solids AO and AB are equal [11.24, D11.10]. Specifically, since AB and AO are both similar to CD and share the edge AE corresponding to CF, their remaining edges must be equal (the proportionality with CD determines all edges uniquely from AE and the angles), so AB = AO.

**Step 22.** Therefore solid AB : solid CD is in the triplicate ratio of AE to CF [D5.10].

**Step 23.** Therefore similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides. Q.E.D.

**USED:** 11.25, 11.27, 11.32, 5.22, 6.1, 6.11, CN4, D11.10, D11.9, D5.10, D5.9, D6.1
**Human refs (from References field):** 11.24, 11.32, 6.1, D11.10, D5.10
**Jaccard:** 0.308 — AI adds ['11.25', '11.27', '5.22', '6.11', 'CN4', 'D11.9', 'D5.9', 'D6.1']; Human adds ['11.24']

#### Heath 人类证明原文

Let AB, CD be similar parallelepipedal solids, and let AE be the side corresponding to CF; I say that the solid AB has to the solid CD the ratio triplicate of that which AE has to CF. For let EK, EL, EM be produced in a straight line with AE, GE, HE, let EK be made equal to CF, EL equal to FN, and further EM equal to FR, and let the parallelogram KL and the solid KP be completed. Now, since the two sides KE, EL are equal to the two sides CF, FN, while the angle KEL is also equal to the angle CFN, inasmuch as the angle AEG is also equal to the angle CFN because of the similarity of the solids AB, CD, therefore the parallelogram KL is equal <and similar> to the parallelogram CN. For the same reason the parallelogram KM is also equal and similar to CR, and further EP to DF; therefore three parallelograms of the solid KP are equal and similar to three parallelograms of the solid CD. But the former three parallelograms are equal and similar to their opposites, and the latter three to their opposites; [XI. 24] therefore the whole solid KP is equal and similar to the whole solid CD. [XI. Def. 10] Let the parallelogram GK be completed, and on the parallelograms GK, KL as bases, and with the same height as that of AB, let the solids EO, LQ be completed. Then since; owing to the similarity of the solids AB, CD, as AE is to CF, so is EG to FN, and EH to FR, while CF is equal to EK, FN to EL, and FR to EM, therefore, as AE is to EK, so is GE to EL, and HE to EM. But, as AE is to EK, so is AG to the parallelogram GK, as GE is to EL, so is GK to KL, and, as HE is to EM, so is QE to KM; [VI. 1] therefore also, as the parallelogram AG is to GK, so is GK to KL, and QE to KM. But, as AG is to GK, so is the solid AB to the solid EO, as GK is to KL, so is the solid OE to the solid QL, and, as QE is to KM, so is the solid QL to the solid KP; [XI. 32] therefore also, as the solid AB is to EO, so is EO to QL, and QL to KP. But, if four magnitudes be continuously proportional, the first has to the fourth the ratio triplicate of that which it has to the second; [V. Def. 10] therefore the solid AB has to KP the ratio triplicate of that which AB has to EO. But, as AB is to EO, so is the parallelogram AG to GK, and the straight line AE to EK [VI. 1]; hence the solid AB has also to KP the ratio triplicate of that which AE has to EK. But the solid KP is equal to the solid CD, and the straight line EK to CF; therefore the solid AB has also to the solid CD the ratio triplicate of that which the corresponding side of it, AE, has to the corresponding side CF.

#### 分类报告原文（Run C）

### 11.33
**Category**: Path difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Heath's proof constructs a copy of CD (solid KP) within the same diagram and establishes a continued proportion of four solids (AB, EO, QL, KP) using VI.1 for parallelogram ratios and XI.32 to convert to solid ratios, then applies V.Def.10 directly for the triplicate ratio. The AI proof takes a structurally different approach: it constructs an auxiliary solid AO similar to CD on edge AE (via 11.27), then decomposes the volume ratio dimension by dimension using intermediate parallelepipeds Q1, Q2, Q3 that each differ by one edge. Each dimensional ratio equals AE:CF (established via 11.25, 11.32, and 6.1), and these are combined by ex aequali (5.22) to yield the triplicate ratio (D5.10). The backbones differ: Heath uses a four-term continued proportion of solids, while the AI uses a three-step dimensional decomposition. Both paths are logically complete, so the classification is D.

#### 专家验证

- 路径差异判定是否正确：不完全正确。
- 补充意见：存在跳步。

---

### D-16: Proposition 11.36（Run B）

**命题陈述：** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

#### AI 证明原文（Run B）

## Proposition 11.36
**Statement:** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

**Step 1.** Let A, B, C be three straight lines in proportion, so that A : B :: B : C. Let S be the parallelepipedal solid formed out of the three lines A, B, C at a given solid angle, and let P be the equilateral parallelepipedal solid on B which is equiangular with S, that is, P has all three edges equal to B and the same solid angle as S. We are to prove that S equals P.

**Step 2.** Construct an intermediate parallelepipedal solid Q having edges A, B, B at the same solid angle as S and P. This is possible by constructing a solid angle equal to the given one [11.26] and completing the parallelepiped with the specified edge lengths.

**Step 3.** Compare S and Q. The solids S (with edges A, B, C) and Q (with edges A, B, B) share the same solid angle and the same edge A in one direction. Taking as their respective bases the parallelogrammic faces opposite to the edge A, both solids have the same height (the perpendicular distance between the pair of opposite faces determined by the direction of edge A, which is the same for both since the solid angle and the edge A are the same). By 11.32, S : Q equals the ratio of the base of S to the base of Q.

**Step 4.** The base of S is the parallelogram with sides B and C at the angle determined by the solid angle, and the base of Q is the parallelogram with sides B and B at the same angle. These two parallelograms share the same side B and the same included angle, so they have the same height (the perpendicular from the endpoints of side B to the line of the other side). By 6.1, parallelograms under the same height are to one another as their bases, so the base of S is to the base of Q as C is to B. Therefore S : Q :: C : B.

**Step 5.** Compare Q and P. The solids Q (with edges A, B, B) and P (with edges B, B, B) share the same solid angle and both have edge B in two of the three directions. Taking as their respective bases the parallelogrammic faces with sides B and B (which are identical parallelograms), both solids have the same base. However, we compare them by taking the direction of the differing edge as providing the height. Consider the faces with sides B and B (the second and third edges) as bases; Q has height determined by edge A and P has height determined by edge B, both in the same direction from the same solid angle. By 11.32, Q : P equals the ratio of the base of Q to the base of P, where now we orient the solids so the differing edge determines the height. Taking the pair of opposite faces perpendicular to the direction of the first edge, Q and P have the same height (both having edge B in that perpendicular direction). Their bases are parallelograms with sides A, B and sides B, B respectively, at the same angle. By 6.1, these bases are as A is to B. Therefore Q : P :: A : B.

**Step 6.** From the given proportion A : B :: B : C, by inversion [5.7 corollary], we obtain B : A :: C : B, which can be rewritten as C : B :: B : A. Therefore from Step 4, S : Q :: C : B :: B : A.

**Step 7.** We now have S : Q :: B : A (from Step 6) and Q : P :: A : B (from Step 5). Applying the ex aequali rule [5.22], which states that if S : Q :: B : A and Q : P :: A : B, then S : P :: B : B.

**Step 8.** Since B equals itself, the ratio B : B is the ratio of equality. From S : P :: B : B it follows that S : P :: P : P (since any magnitude has to itself the ratio of equality, which is the same as B : B). Therefore S and P are magnitudes to which the same magnitude P has the same ratio, and by 5.9, S equals P.

**Step 9.** Therefore the parallelepipedal solid S formed out of the three proportional straight lines A, B, C is equal to the equilateral parallelepipedal solid P on the mean B which is equiangular with S. This is what was to be proved.

**USED:** 11.26, 11.32, 5.22, 5.7, 5.9, 6.1
**Human refs (from References field):** 11.31, 11.35, 6.14
**Jaccard:** 0.000 — AI adds ['11.26', '11.32', '5.22', '5.7', '5.9', '6.1']; Human adds ['11.31', '11.35', '6.14']

#### Heath 人类证明原文

Let A, B, C be three straight lines in proportion, so that, as A is to B, so is B to C; I say that the solid formed out of A, B, C is equal to the solid on B which is equilateral, but equiangular with the aforesaid solid. Let there be set out the solid angle at E contained by the angles DEG, GEF, FED, let each of the straight lines DE, GE, EF be made equal to B, and let the parallelepipedal solid EK be completed, let LM be made equal to A, and on the straight line LM, and at the point L on it, let there be constructed a solid angle equal to the solid angle at E, namely that contained by NLO, OLM, MLN; let LO be made equal to B, and LN equal to C. Now, since, as A is to B, so is B to C, while A is equal to LM, B to each of the straight lines LO, ED, and C to LN, therefore, as LM is to EF, so is DE to LN. Thus the sides about the equal angles NLM, DEF are reciprocally proportional; therefore the parallelogram MN is equal to the parallelogram DF. [VI. 14] And, since the angles DEF, NLM are two plane rectilineal angles, and on them the elevated straight lines LO, EG are set up which are equal to one another and contain equal angles with the original straight lines respectively, therefore the perpendiculars drawn from the points G, O to the planes through NL, LM and DE, EF are equal to one another; [XI. 35, Por.]hence the solids LH, EK are of the same height. But parallelepipedal solids on equal bases and of the same height are equal to one another; [XI. 31] therefore the solid HL is equal to the solid EK. And LH is the solid formed out of A, B, C, and EK the solid on B; therefore the parallelepipedal solid formed out of A, B, C is equal to the solid on B which is equilateral, but equiangular with the aforesaid solid.

#### 分类报告原文（Run B）

### 11.36
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 reveals fundamentally different proof backbones, leading to classification D at Q3. Heath's proof directly constructs two parallelepipeds with the given edges and shows they have equal bases (via reciprocal proportionality, VI.14) and equal heights (via XI.35 Porism), then concludes equality by XI.31. The AI proof takes an entirely different ratio-based approach: it introduces an intermediate solid Q with edges A, B, B, uses XI.32 and VI.1 to establish the ratios S:Q = C:B and Q:P = A:B, then applies ex aequali (V.22) to obtain S:P = B:B, concluding S = P by V.9. The citation sets are completely disjoint (Jaccard = 0.0), reflecting genuinely different mathematical strategies rather than mere differences in citation depth. The AI's ratio-chain approach is logically complete and valid, satisfying Q3(b).

#### 专家验证

- 路径差异判定是否正确：不完全正确。
- 补充意见：存在跳步。

---

### D-17: Proposition 13.12（Run A）

**命题陈述：** If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.

#### AI 证明原文（Run A）

## Proposition 13.12
**Statement:** If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.

**Step 1.** Let ABC be an equilateral triangle inscribed in a circle with center E [D4.3, D1.20]. Let AE, BE, CE be radii of the circle, so that AE = BE = CE [D1.15].

**Step 2.** Since AB = BC = CA [D1.20] and AE = BE = CE [D1.15], triangles AEB, BEC, and CEA have all three sides respectively equal. Therefore by SSS congruence [1.8], the three triangles are congruent, and in particular angle AEB = angle BEC = angle CEA.

**Step 3.** Let D be the point diametrically opposite A on the circle, so that AD is a diameter passing through E [D1.17]. Then AED is a straight line and AE = ED (each being a radius).

**Step 4.** Since AED is a straight line, angle AEB + angle BED = two right angles [1.13], and angle AEC + angle CED = two right angles [1.13].

**Step 5.** From the equal central angles (Step 2), angle AEB = angle AEC. By Step 4, angle BED = two right angles minus angle AEB and angle CED = two right angles minus angle AEC. Since angle AEB = angle AEC, it follows that angle BED = angle CED.

**Step 6.** Also from Step 2, angle BEC = angle AEB. Since D lies between rays EB and EC from center E (the equilateral triangle having B and C symmetrically placed about the diameter AD), angle BEC = angle BED + angle DEC = angle BED + angle BED = two times angle BED [Step 5]. Therefore angle AEB = two times angle BED.

**Step 7.** Substituting into the relation from Step 4: two times angle BED + angle BED = two right angles, so three times angle BED = two right angles.

**Step 8.** Consider triangle BED. The sum of its angles equals two right angles [1.32]. Since EB = ED (both radii) [D1.15], the base angles are equal: angle EBD = angle EDB [1.5]. Therefore angle BED + angle EBD + angle EDB = angle BED + two times angle EBD = two right angles.

**Step 9.** But three times angle BED also equals two right angles [Step 7]. Hence angle BED + two times angle EBD = three times angle BED. Subtracting angle BED from both sides [CN3], two times angle EBD = two times angle BED, so angle EBD = angle BED.

**Step 10.** Since angle EBD = angle BED in triangle BED, the side opposite angle EBD (namely ED) equals the side opposite angle BED (namely BD) [1.6]. Therefore BD = ED. Since ED = AE (both radii) [D1.15], BD = AE [CN1].

**Step 11.** Since AD is a diameter and B lies on the circle, the angle ABD (the angle in a semicircle) is a right angle [3.31].

**Step 12.** In right triangle ABD with the right angle at B, by the Pythagorean theorem the square on AD equals the square on AB together with the square on BD [1.47]. That is, sq(AD) = sq(AB) + sq(BD).

**Step 13.** Since AD is bisected at E (with AE = ED), apply the identity for a bisected line [2.4]: the square on AD equals the square on AE plus the square on ED plus twice the rectangle contained by AE and ED. Since AE = ED, this gives sq(AD) = sq(AE) + sq(AE) + two times sq(AE) = four times sq(AE).

**Step 14.** Since BD = AE [Step 10], the square on BD equals the square on AE. Substituting into Step 12: four times sq(AE) = sq(AB) + sq(AE).

**Step 15.** Subtracting the square on AE from both sides [CN3]: sq(AB) = three times sq(AE).

**Step 16.** Since AE is the radius of the circle, the square on the side of the equilateral triangle is triple of the square on the radius of the circle. Q.E.D.

**USED:** 1.13, 1.32, 1.47, 1.5, 1.6, 1.8, 2.4, 3.31, CN1, CN3, D1.15, D1.17, D1.20, D4.3
**Human refs (from References field):** 1.47, 3.31, 4.15
**Jaccard:** 0.133 — AI adds ['1.13', '1.32', '1.5', '1.6', '1.8', '2.4', 'CN1', 'CN3', 'D1.15', 'D1.17', 'D1.20', 'D4.3']; Human adds ['4.15']

#### Heath 人类证明原文

Let ABC be a circle, and let the equilateral triangle ABC be inscribed in it; I say that the square on one side of the triangle ABC is triple of the square on the radius of the circle. For let the centre D of the circle ABC be taken, let AD be joined and carried through to E, and let BE be joined. Then, since the triangle ABC is equilateral, therefore the circumference BEC is a third part of the circumference of the circle ABC. Therefore the circumference BE is a sixth part of the circumference of the circle; therefore the straight line BE belongs to a hexagon; therefore it is equal to the radius DE. [IV. 15] And, since AE is double of DE, the square on AE is quadruple of the square on ED, that is, of the square on BE. But the square on AE is equal to the squares on AB, BE; [III. 31, I. 47] therefore the squares on AB, BE are quadruple of the square on BE. Therefore, separando, the square on AB is triple of the square on BE. But BE is equal to DE; therefore the square on AB is triple of the square on DE. Therefore the square on the side of the triangle is triple of the square on the radius.

#### 分类报告原文（Run A）

### 13.12
**Category**: Path difference
**Jaccard**: 0.133
**Analysis**: Q2 decided the classification. Heath's proof establishes that BE equals the radius by invoking IV.15 (the hexagon inscription result), then uses III.31 and I.47 to reach the algebraic conclusion sq(AB) = 3*sq(DE). The AI proof takes a fundamentally different geometric path: it uses SSS congruence (I.8) to show the three central triangles are congruent, derives through angle arithmetic (I.13, I.32) that angle BED is one-third of two right angles, then uses isosceles triangle properties (I.5, I.6) to show BD = ED = radius. The AI also uses II.4 to expand sq(AD) = 4*sq(AE) rather than Heath's direct observation that AE = 2*DE. These are genuinely different key intermediate conclusions -- the AI never establishes the hexagon-side-equals-radius fact that is Heath's backbone, instead deriving an equivalent result (BD = radius) through central angle analysis. Since the AI's different path is logically complete and valid, this is classified as D.

#### 专家验证

- 路径差异判定是否正确：正确。
- 补充意见：无。

---

### D-18: Proposition 13.18（Run A）

**命题陈述：** To set out the sides of the five figures and to compare them with one another.

#### AI 证明原文（Run A）

## Proposition 13.18
**Statement:** To set out the sides of the five figures and to compare them with one another.

**Step 1.** Let the diameter of the given sphere be set out, and let it be AB. Let AB be cut at C so that AC equals 2*CB, i.e., AC = (2/3)AB and CB = (1/3)AB. Describe a semicircle ADB on AB as diameter, draw CD perpendicular to AB from C, and join DA and DB. [P1, P3, 1.11]

**Step 2.** Since AB*BC = CD^2 (by the property of the semicircle, as the angle ADB is a right angle by 3.31), and since AB*BC is also the square on the side of the pyramid inscribed in the sphere of diameter AB, the side of the pyramid (tetrahedron) is CD, which is set out. By 13.13, the square on the diameter AB is one and a half times the square on the side of the pyramid, that is, AB^2 = (3/2)*s_tet^2, so s_tet^2 = (2/3)*AB^2. [3.31, 13.13]

**Step 3.** For the octahedron inscribed in the same sphere: by 13.14, the square on the diameter of the sphere is double the square on the side of the octahedron, that is, AB^2 = 2*s_oct^2, so s_oct^2 = (1/2)*AB^2. Set out the side of the octahedron accordingly. [13.14]

**Step 4.** For the cube inscribed in the same sphere: by 13.15, the square on the diameter of the sphere is triple the square on the side of the cube, that is, AB^2 = 3*s_cube^2, so s_cube^2 = (1/3)*AB^2. Set out the side of the cube accordingly. [13.15]

**Step 5.** Now we compare the sides of these three figures. From Steps 2-4, s_tet^2 = (2/3)*AB^2, s_oct^2 = (1/2)*AB^2, and s_cube^2 = (1/3)*AB^2. Since (2/3) > (1/2) > (1/3), we have s_tet^2 > s_oct^2 > s_cube^2, and therefore s_tet > s_oct > s_cube. That is, the side of the pyramid is greater than the side of the octahedron, and the side of the octahedron is greater than the side of the cube. [CN5]

**Step 6.** We further establish the ratio between the side of the pyramid and the side of the cube. We have s_tet^2 = (2/3)*AB^2 and s_cube^2 = (1/3)*AB^2. Therefore s_tet^2 / s_cube^2 = 2, that is, the square on the side of the pyramid is double the square on the side of the cube. Hence the side of the pyramid is to the side of the cube in the ratio of a diagonal to a side, i.e., they are incommensurable in length but commensurable in square. [6.1, 10.9]

**Step 7.** We also compare the side of the octahedron with that of the cube. We have s_oct^2 = (1/2)*AB^2 and s_cube^2 = (1/3)*AB^2. Therefore s_oct^2 / s_cube^2 = 3/2. Since 3/2 is not a ratio of square numbers, the side of the octahedron and the side of the cube are incommensurable in length but commensurable in square. [10.9]

**Step 8.** Thus for the three figures -- pyramid, octahedron, and cube -- their sides have been set out and compared. The side of the pyramid has the square double of the square on the side of the cube, and the side of the octahedron has the square that is one and a half times the square on the side of the cube. [13.13, 13.14, 13.15]

**Step 9.** For the icosahedron inscribed in the same sphere: by 13.16, the side of the icosahedron has been constructed and shown to be the irrational straight line called minor. Set out the side of the icosahedron accordingly. [13.16]

**Step 10.** For the dodecahedron inscribed in the same sphere: by 13.17, the side of the dodecahedron has been constructed and shown to be the irrational straight line called apotome. Set out the side of the dodecahedron accordingly. [13.17]

**Step 11.** It remains to show that the side of the icosahedron is greater than the side of the dodecahedron. In the constructions of 13.16 and 13.17, both figures are inscribed in the same sphere. The cube is inscribed in the sphere first, and the icosahedron and dodecahedron are constructed from the cube. By 13.17, the side of the dodecahedron is the side of the regular pentagon inscribed in the face of the icosahedron, since both are constructed from the same cube inscribed in the sphere. The diagonal of a regular pentagon is cut in extreme and mean ratio, and the greater segment equals the side of the pentagon, by 13.8. Since the side of the icosahedron relates to the side of the dodecahedron through these constructions, and the side of the dodecahedron is obtained by cutting certain segments in extreme and mean ratio, the side of the icosahedron exceeds the side of the dodecahedron. [13.8, 13.16, 13.17]

**Step 12.** Moreover, the side of the icosahedron, being a minor irrational, and the side of the dodecahedron, being an apotome, are not only different irrationals but also not comparable by any rational ratio. By 10.111, a minor and an apotome are different in kind, confirming they are distinct irrational lines. The side of no one of the five figures is the same as the side of any other, for the side of the pyramid is rational (commensurable in square with the diameter), the side of the octahedron is rational, the side of the cube is rational, while the side of the icosahedron is minor and the side of the dodecahedron is apotome; and minor and apotome are distinct irrationals. [10.111, D10.1.3]

**Step 13.** Therefore the sides of the five figures have been set out and compared with one another: the side of the pyramid is the greatest among the three commensurable sides, then the side of the octahedron, then the side of the cube; the side of the icosahedron is a minor irrational and is greater than the side of the dodecahedron which is an apotome; and no two of the five sides are equal. Q.E.D.

**USED:** 1.11, 10.111, 10.9, 13.13, 13.14, 13.15, 13.16, 13.17, 13.8, 3.31, 6.1, CN5, D10.1.3, P1, P3
**Human refs (from References field):** 13.10, 13.13, 13.14, 13.15, 13.16, 13.17, 13.9, 4.15, 6.20, 6.4, 6.8, D5.9
**Jaccard:** 0.227 — AI adds ['1.11', '10.111', '10.9', '13.8', '3.31', '6.1', 'CN5', 'D10.1.3', 'P1', 'P3']; Human adds ['13.10', '13.9', '4.15', '6.20', '6.4', '6.8', 'D5.9']

#### Heath 人类证明原文

Let AB, the diameter of the given sphere, be set out, and let it be cut at C so that AC is equal to CB, and at D so that AD is double of DB; let the semicircle AEB be described on AB, from C, D let CE, DF be drawn at right angles to AB, and let AF, FB, EB be joined. Then, since AD is double of DB, therefore AB is triple of BD. Convertendo, therefore, BA is one and a half times AD. But, as BA is to AD, so is the square on BA to the square on AF, [V. Def. 9, VI. 8] for the triangle AFB is equiangular with the triangle AFD; therefore the square on BA is one and a half times the square on AF. But the square on the diameter of the sphere is also one and a half times the square on the side of the pyramid. [XIII. 13] And AB is the diameter of the sphere; therefore AF is equal to the side of the pyramid. Again, since AD is double of DB, therefore AB is triple of BD. But, as AB is to BD, so is the square on AB to the square on BF; [VI. 8, V. Def. 9] therefore the square on AB is triple of the square on BF. But the square on the diameter of the sphere is also triple of the square on the side of the cube. [XIII. 15] And AB is the diameter of the sphere; therefore BF is the side of the cube. And, since AC is equal to CB, therefore AB is double of BC. But, as AB is to BC, so is the square on AB to the square on BE; therefore the square on AB is double of the square on BE. But the square on the diameter of the sphere is also double of the square on the side of the octahedron. [XIII. 14] And AB is the diameter of the given sphere; therefore BE is the side of the octahedron. Next, let AG be drawn from the point A at right angles to the straight line AB, let AG be made equal to AB, let GC be joined, and from H let HK be drawn perpendicular to AB. Then, since GA is double of AC, for GA is equal to AB, and, as GA is to AC, so is HK to KC, therefore HK is also double of KC. Therefore the square on HK is quadruple of the square on KC; therefore the squares on HK, KC, that is, the square on HC, is five times the square on KC. But HC is equal to CB; therefore the square on BC is five times the square on CK. And, since AB is double of CB, and, in them, AD is double of DB, therefore the remainder BD is double of the remainder DC. Therefore BC is triple of CD; therefore the square on BC is nine times the square on CD. But the square on BC is five times the square on CK; therefore the square on CK is greater than the square on CD; therefore CK is greater than CD. Let CL be made equal to CK, from L let LM be drawn at right angles to AB, and let MB be joined. Now, since the square on BC is five times the square on CK, and AB is double of BC, and KL double of CK, therefore the square on AB is five times the square on KL. But the square on the diameter of the sphere is also five times the square on the radius of the circle from which the icosahedron has been described. [XIII. 16] And AB is the diameter of the sphere; therefore KL is the radius of the circle from which the icosahedron has been described; therefore KL is a side of the hexagon in the said circle. [IV. 15] And, since the diameter of the sphere is made up of the side of the hexagon and two of the sides of the decagon inscribed in the same circle, [XIII. 16] and AB is the diameter of the sphere, while KL is a side of the hexagon, and AK is equal to LB, therefore each of the straight lines AK, LB is a side of the decagon inscribed in the circle from which the icosahedron has been described. And, since LB belongs to a decagon, and ML to a hexagon, for ML is equal to KL, since it is also equal to HK, being the same distance from the centre, and each of the straight lines HK, KL is double of KC, therefore MB belongs to a pentagon. [XIII. 10] But the side of the pentagon is the side of the icosahedron; [XIII. 16] therefore MB belongs to the icosahedron. Now, since FB is a side of the cube, let it be cut in extreme and mean ratio at N, and let NB be the greater segment; therefore NB is a side of the dodecahedron. [XIII. 17] And, since the square on the diameter of the sphere was proved to be one and a half times the square on the side AF of the pyramid, double of the square on the side BE of the octahedron and triple of the side FB of the cube, therefore, of parts of which the square on the diameter of the sphere contains six, the square on the side of the pyramid contains four, the square on the side of the octahedron three, and the square on the side of the cube two. Therefore the square on the side of the pyramid is fourthirds of the square on the side of the octahedron, and double of the square on the side of the cube; and the square on the side of the octahedron is one and a half times the square on the side of the cube. The said sides, therefore, of the three figures, I mean the pyramid, the octahedron and the cube, are to one another in rational ratios. But the remaining two, I mean the side of the icosahedron and the side of the dodecahedron, are not in rational ratios either to one another or to the aforesaid sides; for they are irrational, the one being minor [XIII. 16] and the other an apotome [XIII. 17]. That the side MB of the icosahedron is greater than the side NB of the dodecahedron we can prove thus. For, since the triangle FDB is equiangular with the triangle FAB, [VI. 8] proportionally, as DB is to BF, so is BF to BA. [VI. 4] And, since the three straight lines are proportional, as the first is to the third, so is the square on the first to the square on the second; [V. Def. 9, VI. 20] therefore, as DB is to BA, so is the square on DB to the square on BF; therefore, inversely, as AB is to BD, so is the square on FB to the square on BD. But AB is triple of BD; therefore the square on FB is triple of the square on BD. But the square on AD is also quadruple of the square on DB, for AD is double of DB; therefore the square on AD is greater than the square on FB; therefore AD is greater than FB; therefore AL is by far greater than FB. And, when AL is cut in extreme and mean ratio, KL is the greater segment, inasmuch as LK belongs to a hexagon, and KA to a decagon; [XIII. 9] and, when FB is cut in extreme and mean ratio, NB is the greater segment; therefore KL is greater than NB. But KL is equal to LM; therefore LM is greater than NB. Therefore MB, which is a side of the icosahedron, is by far greater than NB which is a side of the dodecahedron.

#### 分类报告原文（Run A）

### 13.18
**Category**: Path difference
**Jaccard**: 0.227
**Analysis**: Q2 decides this classification as D (path difference). Both proofs reach the same ultimate conclusions (setting out all five Platonic solid sides and comparing them), but they argue through substantively different intermediate machinery. Heath constructs each side geometrically from a single diagram using similar triangles (VI.8, VI.4), duplicate ratios (V.Def.9), and detailed proportional reasoning, then identifies each constructed segment with the relevant solid's side via XIII.13-XIII.17. The AI instead cites XIII.13-XIII.17 directly as summary results and uses algebraic ratio computation. More significantly, for the crucial icosahedron-greater-than-dodecahedron comparison, Heath deploys an elaborate geometric argument using XIII.9 (extreme and mean ratio of hexagon + decagon sides), VI.4, VI.8, V.Def.9, and VI.20 to establish a chain of inequalities (AD > FB, AL > FB, KL > NB, LM > NB, therefore MB > NB). The AI instead cites XIII.8 (about pentagon diagonals and extreme and mean ratio), a genuinely different proposition from a different geometric context. The proof-tree containment test shows that while some heath_only items (13.10, 4.15) appear inside XIII.16's proof, other substantive heath_only items (6.4, 6.20, 13.9) are deployed independently in Heath's XIII.18 proof and do not appear inside any proposition the AI cites, confirming genuine path divergence rather than mere citation-depth difference. Under Q1's hardened standard, the AI's terse Step 11 was considered for E but rejected because it cites relevant propositions (13.8, 13.16, 13.17) and the missing detail is expansion, not support (lenience rule applies).
**Audit Record**: CANDIDATE E — 13.18
  violated_claim : "the side of the icosahedron exceeds the side of the dodecahedron" (Step 11)
  failure_mode   : unsupported_assertion
  missing_is     : expansion (AI cites 13.8, 13.16, 13.17 which are relevant propositions; the missing content is the detailed geometric argument expanding how these citations yield the conclusion)
  evidence       : AI Step 11: "Since the side of the icosahedron relates to the side of the dodecahedron through these constructions, and the side of the dodecahedron is obtained by cutting certain segments in extreme and mean ratio, the side of the icosahedron exceeds the side of the dodecahedron. [13.8, 13.16, 13.17]"
  why_not_terse  : CANNOT COMPLETE — this IS terse-but-supported. The AI invokes relevant propositions (13.8 on extreme and mean ratio in pentagons, 13.16 and 13.17 for the constructions) that bear on the claim. The missing content is an expansion of how these citations combine, not the absence of any supporting citation. Lenience rule applies → NOT-E.

#### 专家验证

- 路径差异判定是否正确：证明书写存在问题。
- 补充意见：Step 2 声称 AB\*BC = CD^2 是完全错误的，但 Step 2 中后面又正确地说 s_tet^2 = (2/3)\*AB^2。后续的证明利用的是后者，而不是前者，也就是说，AI在这一步给出了一个冗余的、后续没有被用到的错误陈述。

---
