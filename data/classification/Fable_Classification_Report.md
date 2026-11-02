# Fable (Claude Fable 5.1) — Classification Report (All Books)

## Overall Summary

| Book | P | G | D | E | Total |
|---|---|---|---|---|---|
| 1 | 9 | 39 | 0 | 0 | 48 |
| 2 | 0 | 12 | 2 | 0 | 14 |
| 3 | 0 | 35 | 2 | 0 | 37 |
| 4 | 0 | 13 | 3 | 0 | 16 |
| 5 | 3 | 20 | 2 | 0 | 25 |
| 6 | 0 | 28 | 5 | 0 | 33 |
| 7 | 5 | 32 | 2 | 0 | 39 |
| 8 | 3 | 21 | 3 | 0 | 27 |
| 9 | 8 | 26 | 2 | 0 | 36 |
| 10 | 0 | 110 | 5 | 0 | 115 |
| 11 | 0 | 38 | 1 | 0 | 39 |
| 12 | 0 | 17 | 1 | 0 | 18 |
| 13 | 0 | 12 | 6 | 0 | 18 |
| **Total** | **28** | **403** | **34** | **0** | **465** |

---

## Book 1 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 9 | 1.3, 1.13, 1.15, 1.16, 1.17, 1.19, 1.25, 1.35, 1.43 |
| Granularity difference (G) | 39 | 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.14, 1.18, 1.20, 1.21, 1.22, 1.23, 1.24, 1.26, 1.27, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.36, 1.37, 1.38, 1.39, 1.40, 1.41, 1.42, 1.44, 1.45, 1.46, 1.47, 1.48 |
| Path difference (D) | 0 |  |
| AI proof error (E) | 0 |  |

**Total**: 48 propositions

## Per-Proposition Analysis

### 1.1
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing two circles with Post. 3, joining lines with Post. 1, establishing AC=AB and BC=BA via Def. 15, deriving CA=CB by CN1 transitivity, and concluding the triangle is equilateral. The only citation difference is that the AI explicitly cites D1.20 (definition of equilateral triangle) when concluding equilateral status, while Heath leaves this implicit. Since all key intermediate conclusions are identical and the sole ai_only item is a definition cited for explicitness, this is a citation-depth difference under Q2 Case A, yielding G.

### 1.2
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: BC=BG (from the circle with center B), DL=DG (from the circle with center D), DA=DB (from the equilateral triangle), AL=BG (by subtraction, CN3), and AL=BC (by transitivity, CN1). The AI's two extra citations (D1.15 and D1.20) are definitions of circle and equilateral triangle that Heath invokes implicitly when asserting radius equality and side equality. Since the backbone is the same and the difference is only that the AI explicitly cites foundational definitions Heath leaves tacit, this is a granularity difference (G).

### 1.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues. Q1 confirmed the AI proof is logically complete, with no missing cases and no defects under the hardened standard. Q2 confirmed both proofs share the same key intermediate conclusions: placing AD equal to C by I.2, describing circle DEF by Post. 3, establishing AE equals AD by Def. 15, and concluding AE equals C by CN1. Since ai_used equals heath_refs exactly ({1.2, CN1, D1.15, P3}), the perfect match check assigns category P.

### 1.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the method of superposition with identical key intermediate conclusions: placing A on D, showing B coincides with E (AB=DE), AC falls along DF (angle equality), C coincides with F (AC=DF), BC coincides with EF (uniqueness of line), and then applying CN4 to establish equality of bases, triangles, and remaining angles. The only difference is that the AI explicitly cites Postulate 1 to justify the determinacy of the straight line joining two points (Step 5), whereas Heath makes the same argument without an explicit postulate citation. This is a citation-depth difference (Case A in Q2), not a backbone difference, yielding G.

### 1.5
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share identical logical backbones: constructing points F and G on the produced sides, proving triangles AFC and AGB congruent via I.4 (yielding FC=GB, angle ACF = angle ABG, angle AFC = angle AGB), subtracting to get BF=CG, proving triangles BFC and CGB congruent via a second application of I.4 (yielding angle FBC = angle GCB, angle BCF = angle CBG), and subtracting to conclude angle ABC = angle ACB. The AI proof adds explicit citations of CN3 (Common Notion 3, for the two subtraction steps) and D1.20 (definition of isosceles triangle), which Heath leaves implicit. Since the key intermediate conclusions are identical and the only differences are in citation depth -- the AI being more explicit about foundational axioms and definitions -- this is a granularity difference (Case A of Q2).

### 1.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the identical proof by contradiction: assuming AB > AC, cutting DB equal to AC from AB, joining DC, applying SAS (I.4) to show triangle DBC equals triangle ACB, then deriving a contradiction via the whole-greater-than-part principle (CN5). The key intermediate conclusions are the same in both proofs. The AI explicitly cites 1.3, 1.4, CN5, and P1, while Heath's parsed references are empty because these dependencies are used implicitly without formal citation. Since all ai_only items are construction propositions (1.3), a postulate (P1), SAS (1.4), and a common notion (CN5), and heath_only is empty, this is a citation-depth difference with identical logical backbone, yielding G.

### 1.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a reductio assuming the existence of equal-length lines AD=AC and DB=CB meeting at a different point D, joining CD, applying I.5 twice to the two isosceles triangles ACD and BCD, and deriving a contradiction where angle CDB must be both equal to and greater than angle DCB. The AI's Case I (Steps 4-7) reproduces this backbone exactly. The ai_only citations (CN5, P1, P2) are all axiom-level items that Heath uses implicitly without citing: CN5 (whole greater than part) underlies Heath's 'greater than' and 'much greater' inferences, P1 underlies 'let CD be joined', and P2 is used only in the AI's additional Case II. The AI proof is more thorough than Heath's by explicitly covering three positional cases (D outside, D inside triangle ACB, D on AC), but the core argument is the same. With heath_only empty and ai_only containing only postulates and common notions, this is a clear Case A granularity difference.

### 1.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the identical superposition argument: applying triangle ABC to DEF by placing B on E and BC on EF, showing C coincides with F because BC equals EF, then arguing by contradiction via I.7 that the sides BA and AC must coincide with ED and DF, and concluding the angles are equal. The AI proof explicitly cites CN4 (things which coincide are equal) to justify the final equality of angles, whereas Heath states the same conclusion without formal citation. Since the key intermediate conclusions are identical and the only citation difference is the AI's explicit invocation of a Common Notion that Heath uses implicitly, this is Case A in Q2: same backbone, different citation depth, yielding G.

### 1.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: cut AE equal to AD on AC (I.3), construct equilateral triangle DEF on DE, join AF, then apply SSS congruence (I.8) using AD=AE, AF common, and DF=EF to conclude angle DAF equals angle EAF. The AI proof explicitly cites construction and definitional steps that Heath leaves implicit: 1.1 for constructing the equilateral triangle, P1 for joining lines, and D1.20 (definition of equilateral triangle) to justify DF=EF. Since heath_only is empty and all ai_only items are over-citations of construction props, definitions, and postulates, Q2 Case A holds, yielding G.

### 1.10
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct an equilateral triangle on AB (I.1), bisect angle ACB with line CD (I.9), then apply SAS congruence (I.4) using AC = CB, CD common, and angle ACD = angle BCD to conclude AD = BD. The only citation difference is that the AI explicitly cites Definition 1.20 (equilateral triangle) to justify AC = CB, whereas Heath states this fact without citing the definition. Since the ai_only set contains only a definition and the heath_only set is empty, this is a clear Case A in Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 1.11
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing equal segments DC = CE via I.3, building an equilateral triangle FDE via I.1 to establish DF = FE, applying SSS congruence (I.8) to conclude angle DCF equals angle ECF, and invoking the definition of right angles (Def. 10) to reach the conclusion. The three ai_only citations (D1.20, P1, P2) are all definitions and postulates that make implicit construction steps explicit: D1.20 justifies that sides of an equilateral triangle are equal, P1 justifies joining FC, and P2 justifies producing AB if needed. None represent a different logical path. Since the key intermediate conclusions are identical and the citation differences reflect only over-citation of foundational axioms and definitions, this is a granularity difference (G).

### 1.12
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a circle centered at C crossing AB at E and G, bisect EG at H, then use SSS congruence (I.8) to show the adjacent angles CHG and EHC are equal, concluding perpendicularity via the definition of right angles (D1.10). The only citation difference is that the AI explicitly cites D1.15 (definition of a circle) to justify that CG equals CE as radii, while Heath states the same fact without citing the definition. This is a pure citation-depth difference with no divergence in the key intermediate conclusions, yielding G.

### 1.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (1.11 is prior, CN1/CN2/D1.10 are axioms/definitions). Q1 confirmed logical completeness: the AI proof covers both required cases (equal angles yielding two right angles by D1.10, and unequal angles handled via construction of a perpendicular and angle addition). Q2 confirmed identical backbone: both proofs construct BE perpendicular to CD, decompose angles CBE and DBA into the same three sub-angles using CN2, then apply transitivity via CN1 to conclude the sum equals two right angles. The citation sets are exactly equal (1.11, CN1, CN2, D1.10), yielding Jaccard 1.0 and a perfect match classification.

### 1.14
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: proof by contradiction assuming BD is not collinear with CB, constructing E on the extension of CB, applying 1.13 to establish ABC+ABE equals two right angles, equating with the hypothesis that ABC+ABD equals two right angles, subtracting the common angle ABC to get ABE=ABD, and deriving a contradiction because one angle is part of the other. The AI proof over-cites by explicitly invoking P2 (to produce the line to E) and CN5 (whole is greater than the part), both of which Heath uses implicitly without citation. Since ai_only contains only axiom-level items (a postulate and a common notion) and heath_only is empty, and all key intermediate conclusions appear at the same logical positions in both proofs, this is Case A of Q2: same backbone, different citation depth.

### 1.15
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate found no issues (1.13 is prior, CN1/CN3/P4 are axioms). Q1 confirmed the AI proof is logically complete: both pairs of vertical angles are explicitly proved with correct citations at every step. Q2 confirmed both proofs share the same backbone: apply I.13 twice to establish that two pairs of adjacent angles each sum to two right angles, equate the sums via P4 and CN1, then subtract the common angle via CN3. The citation sets are identical (ai_used = heath_refs = {1.13, CN1, CN3, P4}, Jaccard = 1.0), and no ai_only or heath_only items exist. The perfect-match check is decisive: same key intermediate conclusions and identical citation sets yield P.

### 1.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (all theorem citations 1.10, 1.15, 1.3, 1.4 precede 1.16). Q1 confirmed logical completeness: the AI proof explicitly addresses both required cases (ACD > BAC in Steps 1-7 and ACD > ABC in Steps 8-11), with no unsupported assertions, circular citations, or invalid inferences. Q2 confirmed the same backbone: both proofs bisect AC at E, construct F with EF equal to BE, apply vertical angles (1.15) and SAS congruence (1.4) to establish angle BAE equals angle ECF, then use CN5 to conclude ACD is greater than BAE, with the second case handled analogously by bisecting BC. Since the citation sets are identical (ai_used equals heath_refs exactly, Jaccard 1.0), the classification is P.

### 1.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (1.13, 1.16, and P2 are all prior to 1.17). Q1 confirmed the AI proof is logically complete: it explicitly proves all three pairs of angles are less than two right angles, actually providing more detail than Heath who uses 'similarly' for two of the three cases. Q2 confirmed the same logical backbone in both proofs: produce a side to create an exterior angle, apply I.16 to show the exterior angle exceeds the interior opposite angle, add the remaining angle to both sides, invoke I.13 to establish the linear pair equals two right angles, and conclude the pair of triangle angles is less than two right angles. With ai_only and heath_only both empty and Jaccard similarity of 1.0, the citation sets are identical, yielding a perfect match.

### 1.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct AD equal to AB on AC (I.3), join BD, establish that triangle ABD is isosceles so angle ABD equals angle ADB, apply the exterior angle theorem (I.16) to show angle ADB is greater than angle DCB, conclude angle ABD is greater than angle ACB, and finally conclude angle ABC is greater than angle ACB. The AI proof adds explicit citations for steps Heath leaves implicit: I.5 for the isosceles triangle base angles, CN5 for the whole-greater-than-part inference, and P1 for joining BD. Since heath_only is empty and ai_only contains only a postulate (P1), a common notion (CN5), and a foundational theorem (I.5) that make explicit what Heath assumes, this is a citation-depth difference with identical backbone, yielding G.

### 1.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of 1.19 follows the exact same logical structure as Heath's proof: a proof by exhaustion showing that AC must be greater than AB by eliminating the possibilities that AC equals AB (via I.5, leading to equal base angles, contradicting the hypothesis) and that AC is less than AB (via I.18, the greater side subtends the greater angle, again contradicting the hypothesis). The citation sets are identical at {1.18, 1.5} with Jaccard similarity 1.0, and the key intermediate conclusions match perfectly, so the perfect match check assigns category P.

### 1.20
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: extend BA to a point D with DA equal to CA, establish angle ADC equals angle ACD via the isosceles triangle theorem (1.5), use CN5 to show angle BCD is greater than angle ADC, apply 1.19 to conclude DB is greater than BC, and derive BA plus AC is greater than BC. The ai_only set {1.3, CN2, P1, P2} consists entirely of construction propositions (1.3), postulates (P1, P2), and a common notion (CN2) that Heath leaves implicit but employs in the same logical steps. The heath_only set is empty. This is a textbook citation-depth difference where the AI over-cites foundational steps that Heath treats as understood, yielding Case A of Q2 and a G classification.

### 1.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: extending BD to meet AC at E, applying I.20 twice to triangles ABE and CED to establish the side inequality, and applying I.16 twice to triangles CDE and ABE to establish the angle inequality, with transitivity completing each part. The AI proof cites CN2 (equals added to equals) and P2 (extending a line) explicitly, whereas Heath uses these implicitly without citation. Since heath_only is empty and ai_only contains only axiom-level items (a Common Notion and a Postulate), this is Case A of Q2: same backbone, different citation depth, yielding G.

### 1.22
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the identical construction: laying out segments DF=A, FG=B, GH=C on a line using I.3, drawing two circles (centered at F with radius FD and centered at G with radius GH), taking their intersection point K, and establishing that FK=A, GK=C, FG=B to form triangle KFG. The ai_only set consists entirely of axiom-level items (CN1, D1.15, P1, P2, P3) that Heath uses implicitly; the AI explicitly cites the definition of a circle (D1.15) for equal radii, common notion CN1 for transitivity of equality, and postulates P1-P3 for the construction steps. The heath_only set is empty, confirming the AI citations are a strict superset. Since both proofs share the same logical backbone and differ only in citation depth at the axiom level, this is a granularity difference.

### 1.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take arbitrary points D and E on the rays of the given angle, form segment DE, construct triangle AFG at point A with sides equal to CD, CE, and DE, then apply SSS (I.8) to conclude that angle DCE equals angle FAG. The AI proof adds explicit citations for steps Heath leaves implicit: I.22 for the triangle construction, I.20 for the triangle inequality precondition of I.22, and P1 for joining DE. Since heath_only is empty and all ai_only items (1.20, 1.22, P1) are supporting citations for the same geometric operations Heath performs without citation, this is Case A of Q2 — same backbone, different citation depth — yielding G.

### 1.24
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct G on DE such that angle EDG equals angle BAC and DG equals DF, prove BC equals EG by SAS (I.4), use the isosceles triangle DFG to get angle DGF equals angle DFG (I.5), establish the angle chain showing angle EFG is greater than angle EGF, and conclude EG is greater than EF by I.19. The AI proof is substantially more detailed, explicitly proving positional facts that Heath assumes from the figure (that DF falls within angle EDG, that DF produced meets EG at a point K between E and G), using I.16 and I.18 for these sub-arguments. The ai_only citations (1.3, 1.16, 1.18, CN1, CN5, P1) are all construction steps, common notions, or propositions deployed to rigorously establish steps Heath leaves implicit. With heath_only empty and both proofs reaching the same key intermediate conclusions via the same route, this is Case A of Q2: same backbone at different citation depth.

### 1.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (1.24 and 1.4 both precede 1.25). Both proofs use identical proof by contradiction via trichotomy: assuming angle BAC is not greater than angle EDF, they eliminate the equal case using I.4 (which would force BC = EF, contradicting BC > EF) and the less-than case using I.24 (which would force BC < EF, again contradicting BC > EF), concluding BAC > EDF. The key intermediate conclusions are identical in both proofs, and the citation sets match exactly (ai_used = heath_refs = {1.24, 1.4}, Jaccard = 1.0), satisfying the perfect match criteria.

### 1.26
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones across both required cases: Case 1 (side adjoining equal angles) uses proof by contradiction assuming AB unequal to DE, constructing BG equal to DE, applying I.4 to derive angle GCB equal to angle DFE, then obtaining a contradiction with the part-equals-whole impossibility; Case 2 (side subtending an equal angle) similarly assumes BC unequal to EF, constructs BH equal to EF, applies I.4 and then I.16 to reach a contradiction between an exterior angle being equal to and greater than an interior angle. The AI proof additionally cites I.3 for cutting off equal segments, P1 for joining lines, CN1 for transitivity of equality, and CN5 for the whole-greater-than-part principle, all of which Heath uses implicitly without citation. Since the key intermediate conclusions are the same and the differences are purely in citation depth, this is a granularity difference.

### 1.27
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction structure: assume the lines meet in one direction, form a triangle, apply I.16 to derive that the exterior angle exceeds the interior opposite angle, contradicting the hypothesis of equal alternate angles, then handle the symmetric case and conclude by Def. 23. The AI proof explicitly works out both cases while Heath says 'similarly' for the second, and the AI additionally cites Postulate 2 for producing the lines, which Heath invokes implicitly. Since the key intermediate conclusions are identical and the only citation difference is an extra postulate citation (P2), this is Case A of Q2: same backbone, different citation depth, yielding G.

### 1.28
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs handle the same two cases with identical key intermediate conclusions: in Case 1, vertical angles (I.15) yield EGB = AGH, then transitivity gives AGH = GHD as alternate angles, and I.27 concludes parallelism; in Case 2, supplementary angles (I.13) give AGH + BGH = 2R, subtraction of BGH yields AGH = GHD as alternate angles, and I.27 again concludes parallelism. The AI proof follows this exact logical backbone but explicitly cites foundational axioms that Heath uses implicitly: CN1 for transitivity of equality, CN3 for the subtraction step, and P4 for the equality of right angles. Since heath_only is empty and the ai_only items (CN1, CN3, P4) are all common notions and a postulate representing over-citation of foundational steps, this is Case A of Q2: same backbone, different citation depth.

### 1.29
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (i) proof by contradiction showing alternate angles AGH = GHD by assuming inequality, deriving via Post. 5 that the parallel lines would meet, contradicting the parallel hypothesis; (ii) establishing EGB = GHD via vertical angles (I.15) and transitivity (CN1); (iii) showing BGH + GHD = two right angles via CN2 and I.13. The sole citation difference is that the AI explicitly cites D1.23 (definition of parallel lines) where Heath invokes the same concept implicitly by saying 'because they are by hypothesis parallel.' The AI also handles both directions of the inequality in part (i) more explicitly, but this is a thoroughness choice, not a different logical path. Since the key intermediate conclusions are identical and the only difference is citation depth, this is a granularity difference.

### 1.30
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they draw a transversal across three parallel lines, apply I.29 twice to establish that two angles each equal an intermediate angle, then use CN1 (transitivity) to conclude the alternate angles are equal, yielding parallelism. The AI's ai_only citations of 1.27 and P1 are purely citation-depth differences: Heath implicitly invokes I.27 when concluding 'they are alternate, therefore AB is parallel to CD' without citing it, and the transversal construction (P1) is a standard over-citation. The AI also handles two geometric cases for the transversal's position, which is more thorough than Heath but follows the same logical approach in each case. Since the backbones match but the citation sets differ, this is a granularity difference.

### 1.31
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) join a random point D on BC to the given point A, (2) construct angle DAE equal to angle ADC at point A using I.23, (3) produce the line through EA to form EAF, and (4) conclude EAF is parallel to BC by I.27 because the alternate angles EAD and ADC are equal. The AI proof additionally cites postulates P1 and P2 for the joining and producing steps, which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only construction postulates, this is a straightforward citation-depth difference with identical backbone, yielding G.

### 1.32
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: construct CE parallel to AB via I.31, establish BAC = ACE by alternate angles (I.29), establish ECD = ABC by exterior-interior angles (I.29), combine to show ACD = BAC + ABC, add ACB to both sides, apply I.13 to conclude ACD + ACB equal two right angles, and deduce the three interior angles equal two right angles. The AI's only additional citations (CN1, CN2, P2) are common notions and a postulate that Heath uses implicitly without explicit citation. Since the key intermediate conclusions are identical and the citation difference is purely one of axiom-level explicitness, this is a granularity difference.

### 1.33
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) alternate angles ABC=BCD via I.29, (2) SAS triangle congruence via I.4 establishing AC=BD and angle ACB=CBD, (3) AC parallel to BD via I.27. The only citation difference is that the AI explicitly cites Postulate 1 for the construction step of joining BC, which Heath performs without explicit citation. This is a pure citation-depth difference for a construction postulate, placing the proofs in Case A of Q2, yielding Granularity difference (G).

### 1.34
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions: alternate angles established twice via I.29, triangle congruence by ASA (I.26) yielding equal opposite sides and one pair of equal opposite angles, addition of equal angles via CN2 for the other pair of opposite angles, and finally SAS congruence (I.4) for the area bisection. The only citation difference is that the AI explicitly cites Postulate 1 for drawing the diameter BC, while Heath leaves this construction implicit. Since the backbones are identical and the sole ai_only item is a postulate-level over-citation, this is Case A of Q2: same backbone, different citation depth.

### 1.35
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (all citations 1.29, 1.34, 1.4, CN1, CN2, CN3 precede 1.35). Q1 confirmed the AI proof is logically complete, with no unsupported assertions, circular citations, or invalid inferences; the AI even addresses additional geometric configurations beyond Heath's single case. Q2 confirmed both proofs share the same backbone of key intermediate conclusions: establishing AD=EF via I.34 and CN1, deriving AE=DF via CN2, showing AB=DC via I.34, proving angle equality via I.29, concluding triangle congruence via I.4, then using CN3 subtraction and CN2 addition to equate the parallelograms. Since ai_used equals heath_refs exactly ({1.29, 1.34, 1.4, CN1, CN2, CN3}) and the key intermediate conclusions are the same, the classification is P (Perfect match).

### 1.36
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: joining BE and CH to construct parallelogram EBCH, establishing BC = EH via I.34 and CN1, proving EBCH is a parallelogram via I.33, then applying I.35 twice to show ABCD = EBCH and EFGH = EBCH, and concluding ABCD = EFGH by CN1. The only citation difference is that the AI explicitly cites Postulate 1 for the construction step of joining lines BE and CH, which Heath performs without explicit citation. Since P1 is a construction postulate and the key intermediate conclusions are identical, this is a citation-depth difference (Case A), yielding Granularity difference.

### 1.37
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decides this as G (granularity difference). Both proofs follow identical logical backbones: constructing parallelograms EBCA and DBCF by drawing lines parallel to the triangles' sides (I.31), proving the parallelograms equal via I.35 (same base BC, same parallels BC and EF), showing each triangle is half its respective parallelogram via I.34 (the diameter bisects a parallelogram), then concluding the triangles are equal as halves of equal things. The only citation difference is the AI's explicit citation of Postulate 2 for extending line AD in both directions, a construction step Heath performs without formal citation. This is a pure over-citation of a construction postulate, fitting Case A of Q2.

### 1.38
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: construct parallelograms GBCA and DEFH by drawing parallels through B and F (1.31), show the parallelograms are equal by 1.36, show each triangle is half its respective parallelogram by 1.34, and conclude that halves of equal things are equal. The AI proof differs only in citation depth, explicitly citing P2 for producing line AD and CN1, CN2, CN5 in an elaborate reductio argument justifying the halves-of-equals step that Heath applies implicitly. Since heath_only is empty and all ai_only items are common notions and a postulate (foundational axioms used implicitly by Heath), this is a same-backbone, different-depth scenario: Case A of Q2 holds, yielding G.

### 1.39
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy: assume AD is not parallel to BC, draw AE parallel to BC via I.31, show triangle ABC equals triangle EBC via I.37, derive that DBC equals EBC via CN1, and reach a contradiction. The key intermediate conclusions appear at the same logical positions in both proofs. The AI proof is more explicit, citing postulates P1 and P2 for construction steps, definition D1.23 for the definition of parallel lines, proposition 1.30 to show why AE must meet BD, and common notion CN5 to name the axiom behind the contradiction, whereas Heath leaves all of these implicit. Since heath_only is empty and all ai_only items are over-citations of details Heath glosses over, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 1.40
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assume AD is not parallel to BE, draw AF parallel to BE via I.31, show triangle ABC equals triangle FCE by I.38, derive the contradiction that DCE equals FCE (greater equals less) via CN1, and conclude AD is parallel to BE. The AI proof adds explicit citations for steps Heath leaves implicit: P1 for joining lines, D1.23 and 1.30 to justify that DC produced must meet AF, and CN5 for the whole-greater-than-part principle that Heath invokes without citation. Since heath_only is empty and all ai_only items (P1, D1.23, 1.30, CN5) represent over-citation of construction postulates, definitions, common notions, and a supporting proposition used for an elaborated detail, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 1.41
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) join AC, (2) establish triangle ABC equals triangle EBC via I.37 (same base BC, same parallels BC and AE), (3) use I.34 to show the diameter AC bisects parallelogram ABCD, and (4) conclude the parallelogram is double the triangle. The AI proof makes three additional explicit citations -- P1 for the construction of joining AC, CN1 for the transitivity step equating triangle ACD to triangle EBC, and CN2 for the doubling conclusion -- all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only common notions and a postulate, this is a clear case of the AI citing at finer granularity while following the identical argumentative path, yielding G.

### 1.42
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect BC at E, form parallelogram FECG via parallel constructions, show triangle ABE equals triangle AEC by I.38, conclude triangle ABC is double of triangle AEC, show parallelogram FECG is double of triangle AEC by I.41, and therefore FECG equals triangle ABC. The AI proof adds six citations not in Heath (1.10 for bisection, 1.30 for transitivity of parallels, CN1 for the final equality, D1.23 for the definition of parallel lines, P1 for joining points, P2 for extending lines), all of which are construction-level propositions, postulates, common notions, or definitions that Heath leaves implicit. Heath cites nothing that the AI omits. This is Case A of Q2: same backbone with different citation depth, yielding G.

### 1.43
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (1.34 is prior, CN2 and CN3 are common notions). Q1 confirmed the AI proof is logically complete with every step explicitly justified. Q2 revealed identical logical backbones: both proofs bisect the main parallelogram via its diameter (1.34), bisect each sub-parallelogram about the diameter (1.34), combine the equal triangle pairs (CN2), and subtract from the equal whole triangles to obtain equal complements (CN3). Since neither a citation depth difference nor a backbone difference exists, Q2 assigned no category. The perfect match check then confirmed that ai_used equals heath_refs exactly ({1.34, CN2, CN3}), yielding P.

### 1.44
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing BEFG equal to C via I.42, drawing parallels via I.31, establishing angle sums via I.29, invoking P5 to show lines meet at K, using I.43 for complements to derive equality, and applying I.15 for vertical angles. The AI proof cites a strict superset of Heath's references, adding 1.30 (transitivity of parallels, which Heath uses implicitly), CN5 (whole greater than part, for angle inequality), and basic postulates P1 and P2 (for joining and producing lines). Heath's proof uses these same steps without explicitly citing them. Since heath_only is empty and all ai_only items are either basic axioms or a low-level transitivity result that Heath applies implicitly, this is Case A: same backbone with different citation depth, yielding G.

### 1.45
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: splitting ABCD into triangles ABD and DBC, constructing parallelograms FH and GM equal to those triangles in angle E, proving KH collinear with HM and FG collinear with GL, establishing KFLM as a parallelogram, and summing the areas. The only difference lies in the sub-steps for establishing that KFLM is a parallelogram: Heath uses I.34 (properties of parallelograms) and I.33 (equal-and-parallel joining segments), while the AI uses D1.23 (definition of parallel lines, arguing that extensions of parallel lines remain parallel) and omits I.33 and I.34. The AI also over-cites P1 for joining DB. Since the backbone of key conclusions is the same and the differences are confined to the citation depth of one sub-step, this is Case A of Q2, yielding G.

### 1.46
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing ADEB as a parallelogram via I.31, showing all four sides equal using I.34 and the construction AD=AB, proving ADE is a right angle via I.29 on the parallels AB and DE given that BAD is right, and extending right-angledness to all corners via I.34 on opposite angles. The AI proof explicitly cites foundational items that Heath leaves implicit: I.3 for cutting off AD equal to AB, P2 for producing the line AC, CN1 for transitivity of equality among the sides, CN3 and P4 for the subtraction yielding angle ADE as right, and D1.22 for the definition of a square. All six ai_only items are construction propositions, postulates, common notions, or definitions representing over-citation of foundational steps, while heath_only is empty. Since the logical backbone is the same and only citation depth differs, this is a granularity difference (G).

### 1.47
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing squares on each side, proving collinearity of CA with AG and BA with AH via I.14, establishing angle DBA equals angle FBC, proving triangle congruence via I.4, using I.41 for the doubling relationship between parallelograms/squares and triangles, and concluding the two sub-rectangles equal the two smaller squares. The AI proof works out both halves explicitly while Heath uses 'similarly' for the second half, and the AI cites additional foundational items (1.30, 1.31 for parallels; CN1 for equality transitivity; D1.22 for the definition of square; P1 for joining lines; P4 for right angle equality) that Heath uses implicitly. Since heath_only is empty and all ai_only items are construction propositions, definitions, postulates, and common notions representing over-citation rather than a different proof path, this is Case A of Q2: same backbone, different citation depth.

### 1.48
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: construct DA perpendicular to AC and equal to BA, join DC, show DA squared equals AB squared, add AC squared to both sides, apply I.47 to get DC squared equals DA squared plus AC squared, invoke the hypothesis that BC squared equals BA squared plus AC squared, conclude DC equals BC, then apply I.8 (SSS congruence) to show angle DAC equals angle BAC, and since angle DAC is right, angle BAC is right. The AI proof differs only in citation depth, explicitly citing construction propositions (1.11 for drawing the perpendicular, 1.3 for cutting off the equal length), postulates (P1 for joining points, P4 for right angles being equal), and common notions (CN1, CN2, CN4, CN5) that Heath leaves implicit. All ai_only items are construction steps, postulates, or common notions, and heath_only is empty, confirming Case A of Q2: same backbone, different citation depth.


---

## Book 2 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 12 | 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.9, 2.10, 2.11, 2.12, 2.13, 2.14 |
| Path difference (D) | 2 | 2.7, 2.8 |
| AI proof error (E) | 0 |  |

**Total**: 14 propositions

## Per-Proposition Analysis

### 2.1
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical geometric argument: construct rectangle BH with BG equal to A, then identify each sub-rectangle (BK, DL, EH) with the corresponding rect(A, segment) using I.34, and conclude BH equals their sum. The key intermediate conclusions are the same in both proofs. The AI proof explicitly cites 1.29 (to show right angles via parallel lines), 1.30 (transitivity of parallelism), CN1 (transitivity of equality), and D2.1 (definition of rectangle), whereas Heath uses these facts implicitly without citation. Since heath_only is empty and all ai_only items are foundational elaborations of steps present in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 2.2
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow identical backbones: construct square ADEB on AB, draw CF through C parallel to AD to divide the square into two rectangles AF and CE, identify AF as rect(AB,AC) since DA equals AB and CE as rect(AB,BC) since BE equals AB, and conclude their sum equals the square on AB. The AI proof cites 1.34 (opposite angles in parallelograms are equal), D1.22 (definition of square), and D2.1 (definition of rectangle) as additional justifications for the same intermediate steps that Heath handles implicitly. Since heath_only is empty and ai_only consists entirely of over-citations (two definitions and one supporting theorem applied to the same conclusions), this is a clear granularity difference.

### 2.3
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct square CDEB on CB, draw AF parallel to CD/BE through A, decompose figure AE into AD and CE, then identify AE as the rectangle contained by AB and BC, AD as the rectangle contained by AC and CB, and CE as the square on CB. The AI proof adds explicit citations for foundational steps that Heath leaves implicit -- 1.28 and 1.29 for proving parallelism via interior angles, 1.30 for transitivity of parallelism, D1.22 for the definition of a square, D2.1 for the definition of a rectangle, and P2 for producing a line segment. Since heath_only is empty and all ai_only items are over-citations supporting the same intermediate conclusions at greater depth, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 2.4
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same geometric argument: constructing a square on the whole line, subdividing it with parallels through the cut point, showing the resulting sub-figures are squares on the segments and rectangles equal to the product of the segments, then summing the parts. The key intermediate conclusions are identical in both proofs: CGKB is equilateral and right-angled hence a square on CB, HF/HDFG is a square on AC, AG equals the rectangle contained by AC and CB, AG equals GE as complements about the diameter, and the four regions sum to the whole square ADEB. The AI's eight additional citations (1.28, 1.30, 1.43, CN1, CN2, D1.22, D2.1, P1) represent over-citation of construction propositions (1.28, 1.30), a complement theorem Heath uses without citing (1.43), definitions, common notions, and a postulate that Heath invokes implicitly, constituting a citation-depth difference rather than a substantive path divergence.

### 2.5
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions through the same logical backbone: construct square CEFB on CB, show CH=HF by I.43, derive CM=DF by adding DM, show AL=CM by I.36 (since AC=CB), deduce AH=gnomon NOP, identify AH as rect(AD,DB) since DH=DB, and conclude rect(AD,DB)+sq(CD)=sq(CB). The AI proof is far more verbose, explicitly citing definitions (D1.22, D2.1, D2.2), common notions (CN1, CN2), a postulate (P1), and supporting propositions (1.34 for opposite sides of a parallelogram, 2.4 Porism for parallelograms about a diameter being squares) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations making explicit what Heath uses tacitly, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 2.6
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct square CEFD on CD, draw parallels through B, H, and A, establish AL = CH (I.36), CH = HF (I.43), combine to show AM equals the gnomon NOP which equals the rectangle AD,DB, then add LG (the square on BC) to reach the conclusion. The AI proof follows this identical chain in its Steps 5-12, matching every key intermediate conclusion of Heath's proof. The ai_only set (1.29, 1.30, 1.34, 2.4, CN1, CN2, D1.22, D2.1, D2.2, P1) consists entirely of additional explicit citations for steps Heath leaves implicit: common notions for equals-added-to-equals, definitions for rectangles and gnomons, parallelism transitivity, a postulate for joining lines, and the porism to 2.4 for identifying sub-squares. Heath_only is empty, confirming Heath's references are a strict subset of the AI's. This is a clear Case A in Q2: same backbone with the AI providing greater citation depth.

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3 (path difference). The AI proof uses an algebraic approach, combining the decomposition identity 2.4 (square on a line equals squares on segments plus twice the rectangle) with the rectangle identity 2.3 (rectangle on whole and segment equals rectangle on segments plus square on segment), then uses arithmetic operations (doubling and addition, justified by CN2) and transitivity (CN1) to derive the desired equality. Heath's proof takes a direct geometric approach: constructing the square on AB (I.46), using the complement theorem (I.43) to establish equality of areas about the diagonal, then manipulating the gnomon and squares. The key intermediate conclusions are entirely different -- Heath works with gnomons, complements about the diagonal, and geometric area decomposition, while the AI works with previously proved algebraic identities from 2.3 and 2.4. The proof-tree containment test confirms genuine divergence: I.43, which is central to Heath's proof of 2.7, does not appear in Heath's proofs of 2.3 or 2.4, so the AI's route is not merely a higher-level packaging of the same geometric argument. The AI's algebraic chain is logically complete and valid, so the classification is D.

### 2.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 2.8 by the gnomon method: constructing the square on AD, dissecting it into squares and complements using I.36 (parallelograms on equal bases) and I.43 (complements), and showing the gnomon STU equals four times rect(AB,BD). The AI instead takes an algebraic route, applying 2.4 to expand sq(AD) into sq(AB)+sq(BD)+2*rect(AB,BD), substituting BD=CB, then using 2.7 to relate sq(AB)+sq(CB) to 2*rect(AB,CB)+sq(AC), and combining these identities to reach 4*rect(AB,CB)+sq(AC)=sq(AD). The key intermediates are entirely different: Heath's backbone is geometric decomposition of the gnomon into eight equal rectangular areas, while the AI's backbone is algebraic combination of two prior quadratic identities. The citation sets are completely disjoint (Jaccard=0.0), confirming genuinely different paths. The AI's chain is logically complete, each step justified by cited propositions or common notions, so Q3 confirms validity, yielding D.

### 2.9
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing CE perpendicular to AB and equal to AC/CB, establishing half-right angles in triangles ACE and ECB, proving angle AEB is right, showing EG=GF and FD=DB via angle arguments and I.6, then chaining Pythagorean applications (I.47) to conclude that the squares on AD and DB are double the squares on AC and CD. The AI proof cites the same core propositions as Heath (1.29, 1.32, 1.34, 1.47, 1.6) and additionally cites construction steps (1.11, 1.3, 1.31), the isosceles base-angle theorem (1.5), supplementary angles (1.13), common notions (CN1, CN2, CN3), a definition (D1.10), and postulates (P1, P2) that Heath leaves implicit. With heath_only empty and all ai_only items being construction propositions, axioms, or postulates, this is a clear Case A same-backbone, different-depth scenario warranting G.

### 2.10
**Category**: Granularity difference
**Jaccard**: 0.706
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: constructing CE perpendicular to AB at C equal to AC, joining EA and EB, drawing parallels EF and FD, producing EB and FD to meet at G, then establishing half-right-angle arguments in isosceles triangles ACE, BCE, and BDG, proving BD=GD and GF=EF, and applying the Pythagorean theorem (I.47) three times to derive that the squares on AD and DB together are double the squares on AC and CD. The AI proof explicitly cites Common Notions CN2, CN3, CN5 and Postulates P1, P2 that Heath leaves implicit, constituting over-citation of basic axioms rather than any structural divergence. With heath_only empty and ai_only consisting entirely of foundational axioms and postulates, this is a clear case of same backbone with different citation depth.

### 2.11
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: construct square ABDC, bisect AC at E, join BE, extend CA to F with EF equal to BE, construct square AFGH on AF, extend GH to K, then apply II.6 to obtain rect(CF,FA)+sq(AE)=sq(EF), substitute EF=EB, apply I.47 at the right angle, subtract sq(AE), identify FK=AD, subtract AK, and conclude rect(AB,BH)=sq(AH). The AI proof cites every construction step, postulate, common notion, and definition explicitly (1.10, 1.13, 1.3, CN1, CN3, D1.22, D2.1, P1, P2) where Heath leaves these implicit. The heath_only set is empty, confirming that the AI omits nothing Heath cites. This is Case A of Q2: same backbone, different citation depth.

### 2.12
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: applying 2.4 to the line CD cut at point A to express sq(DC) in terms of sq(CA), sq(AD), and 2*rect(CA,AD); adding sq(DB) to both sides; applying 1.47 twice to replace sq(CD)+sq(DB) with sq(CB) and sq(AD)+sq(DB) with sq(AB); and substituting to reach the conclusion. The AI's additional citations (1.12, 1.17, P2, D1.10, D1.11, CN1, CN2) are all over-citations of construction steps, postulates, definitions, and common notions that Heath leaves implicit. Since heath_only is empty and all ai_only items are foundational-level references, the proofs differ only in citation depth, not in their key intermediate conclusions.

### 2.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: apply 2.7 to the line CB cut at D, add the square on DA to both sides, apply 1.47 twice to the right triangles ABD and ACD, substitute to obtain CB^2 + BA^2 = AC^2 + 2*rect(CB,BD), and conclude. The AI proof adds an explicit verification that D lies within BC (Step 2, using 1.16) and cites definitions (D1.10, D1.12, D1.21), common notions (CN1, CN2, CN3), postulates (P2, P4), and a construction proposition (1.12) that Heath leaves implicit. The heath_only set is empty, confirming the AI covers everything Heath does. All ai_only items are foundational references cited at a finer granularity, not substantive divergences, so Case A of Q2 holds and the classification is G.

### 2.14
**Category**: Granularity difference
**Jaccard**: 0.188
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct rectangular parallelogram BD equal to A via I.45, handle the trivial BE=ED case, then for the non-trivial case produce BE to F with EF=ED, bisect BF at G, draw semicircle BHF, apply II.5 to obtain rect(BE,EF)+sq(EG)=sq(GF), substitute GH for GF as radii, apply I.47 to get sq(HE)+sq(EG)=sq(GH), subtract sq(EG) to conclude rect(BE,EF)=sq(HE), and finally substitute to reach A=sq(HE). The key intermediate conclusions are identical in both proofs. The AI proof differs only in citation depth: it explicitly cites every construction step (1.3, 1.10, 1.11, 1.46), definitions (D1.15, D1.22, D2.1), common notions (CN1, CN3), postulates (P1, P2, P3), and a basic result (1.34) that Heath leaves implicit. The empty heath_only set confirms that the AI covers all of Heath's cited material. This is Case A of Q2: same backbone, different citation depth.


---

## Book 3 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 35 | 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.10, 3.11, 3.12, 3.13, 3.14, 3.15, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23, 3.24, 3.25, 3.26, 3.27, 3.28, 3.29, 3.30, 3.31, 3.32, 3.33, 3.34, 3.35, 3.36, 3.37 |
| Path difference (D) | 2 | 3.9, 3.16 |
| AI proof error (E) | 0 |  |

**Total**: 37 propositions

## Per-Proposition Analysis

### 3.1
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect a chord AB at D, erect a perpendicular CE through D, bisect CE at F, then prove by contradiction (using SSS via I.8) that no other point G can be the centre because angle GDB would be right while angle FDB is also right. The AI proof follows this identical chain but explicitly cites many foundational references Heath leaves implicit -- construction propositions (1.10, 1.11), postulates (P1, P2, P4), definitions (D1.15, D1.16), common notions (CN5), and the vertical angles theorem (1.15) for an elaborated angle comparison. Heath cites only I.8 and Def. 10; the AI cites these plus nine additional items, all of which support the same backbone at finer granularity. heath_only is empty, confirming the AI covers everything Heath does. This is Case A of Q2: same key intermediate conclusions, different citation depth.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: finding the center D, establishing DA = DB as radii, proving base angles equal via I.5, applying the exterior angle theorem I.16 to get angle DEB > angle DAE, combining to get angle DEB > angle DBE, then applying I.19 to conclude DB > DE and reaching a contradiction. The AI proof explicitly handles both cases (E on the circumference and E outside the circle) that Heath treats with a 'similarly' remark, but this is elaboration of the same argument. The citation difference is entirely in ai_only = {CN5, D1.15, P1}, all foundational items (a common notion, a definition, and a postulate) that Heath uses implicitly. With heath_only empty and the backbone identical, this is Case A of Q2: same key intermediate conclusions at different citation depth.

### 3.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions across both directions of the biconditional: in Part 1, both use SSS congruence (I.8) on triangles AFE and BFE to derive equal adjacent angles and then invoke Def I.10 to conclude right angles; in Part 2, both use isosceles base angles (I.5) and AAS congruence (I.26) to derive AF = FB. The AI's four extra citations (3.1 for finding the centre, D1.15 for the definition of circle justifying equal radii, P1 for joining lines, P4 for equality of right angles) are all explicit references to construction steps, definitions, and postulates that Heath employs implicitly without citation. Since heath_only is empty and all ai_only items are over-citations of foundational items rather than substantive propositions indicating a different proof path, this is Case A of Q2: same backbone, different citation depth.

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assuming the two chords bisect each other for contradiction, finding the center F, joining FE, then using III.3 twice to show that both angle FEA and angle FEB are right angles, and finally deriving a contradiction from the impossibility of these two angles being equal when one must be part of the other. The AI proof explicitly cites foundational axioms that Heath uses implicitly: P1 for joining the line FE, P4 for the equality of right angles, and CN5 for the principle that the whole is greater than the part. Since the key intermediate conclusions are identical and the citation difference consists entirely of postulates and common notions, this is a granularity difference.

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assume two intersecting circles share a center E, establish EC = EF (E is center of circle ABC) and EC = EG (E is center of circle CDG), then derive the contradiction EF = EG where one is part of the other. The AI proof explicitly cites foundational items that Heath leaves implicit -- CN1 for the transitivity step yielding EF = EG, CN5 for the whole-greater-than-part principle, D1.16 for the definition of center, and P1/P2 for line constructions. Since heath_only is empty and all ai_only items are common notions, definitions, or postulates, this is a clear case of over-citation at the same logical backbone, yielding G.

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume by contradiction that F is the centre of both circles ABC and CDE touching at C; join FC and draw a line through F meeting both circumferences; show FC = FB (F centre of ABC) and FC = FE (F centre of CDE), so FE = FB; but one segment is part of the other, yielding a contradiction. The AI proof is more verbose and explicitly cites foundational items (definitions D1.15, D1.16, D3.3; common notions CN1, CN5; postulates P1, P2) that Heath uses implicitly without citation. Since Heath's reference list is empty while the AI's consists entirely of these foundational over-citations, the Jaccard is 0.0, but the backbone is identical. This is Case A of Q2: same key intermediate conclusions, different citation depth, yielding G.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) FA is greatest via triangle inequality (1.20) and radius equality, (2) FB > FC > FG via angle comparison and I.24, (3) FD is least via triangle inequality and subtraction, (4) exactly two equal lines via angle construction (1.23) and SAS congruence (1.4), and (5) uniqueness by contradiction. The AI proof cites the same four theorem-level propositions as Heath (1.4, 1.20, 1.23, 1.24) and adds only foundational items that Heath uses implicitly: definitions (D1.15 for radius equality, D1.17 for diameter), common notions (CN1, CN3, CN5), and a postulate (P1). The heath_only set is empty, confirming no substantive citations are missing. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 3.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: using the triangle inequality (1.20) to establish DA as greatest on the concave circumference, the SAS inequality (1.24) for ordering on the concave side, the triangle inequality again for DG as least on the convex side, the interior-lines theorem (1.21) for ordering on the convex side, angle construction plus SAS congruence (1.4) to produce exactly two equal lines, and a uniqueness argument by contradiction. The AI proof explicitly cites foundational items that Heath uses implicitly: 1.23 for angle construction, CN1 for transitivity of equality, CN3 for subtraction of equals, D1.15 for the definition guaranteeing equal radii, and P1 for drawing lines. Since heath_only is empty and all ai_only items are over-citations of definitions, common notions, postulates, or a basic construction proposition, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 3.9
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification. Heath proves 3.9 directly by bisecting two chords AB and BC, using I.8 and I.Def.10 to show the perpendicular bisectors pass through D, then invoking the porism to III.1 to place the center on both bisectors, concluding D is the center since the two lines meet only at D. The AI instead uses a reductio ad absurdum via 3.7: assuming D is not the center, it finds the actual center E by 3.1, draws diameter FG through D and E, and applies 3.7 to conclude that only two equal straight lines can fall from D on the circle, contradicting the hypothesis of three equal lines. These are fundamentally different backbones — a direct constructive proof versus an indirect proof by contradiction leveraging a different theorem — so Q2 yields Case B. Q3 confirms the AI's reductio is logically complete and sound, giving category D.

### 3.10
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs use the same contradiction strategy: assume more than two intersection points, construct perpendicular bisectors of chords through those points, invoke III.1 to show the center of each circle lies on the same pair of perpendicular bisectors, conclude both circles share a center, and derive a contradiction via III.5. The AI proof is substantially more detailed, explicitly citing 1.10 for bisection, 1.11 for drawing perpendiculars, P1 and P2 for construction postulates, 3.2 to establish non-collinearity of the intersection points, and 1.17 to prove the two perpendicular bisectors are distinct lines. These are all intermediate justifications for steps that Heath performs without citation. Since heath_only is empty and all ai_only items are construction or auxiliary propositions supporting the same logical backbone, this is Case A of Q2: same key intermediate conclusions at different citation depth, yielding G.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction structure, arriving at the same contradiction: GD < GH (because D lies between G and H on the produced diameter) yet GD > GH (because AG > GH and AG = GD as radii of circle ADE). The key intermediate conclusions are identical in both proofs. The only difference is in the supporting method for the step AG > GH: Heath implicitly uses the triangle inequality on triangle AGF (AG + GF > FA = FH, subtract FG), while the AI invokes 3.7 directly (GH is the least distance from a non-center point on a diameter to the circumference). Since the backbone is the same and the AI's explicit citations (3.1, 3.6, 3.7, CN5, D1.15, D1.17, D3.3, P1, P2) represent over-citation of steps Heath leaves implicit (heath_refs is empty in the parsed data), this is Case A of Q2: same backbone, different citation depth.

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs follow the identical contradiction strategy: assuming the line of centers FG does not pass through the external contact point A, establishing FA = FC and GA = GD via radii equality, deducing FA + AG = FC + GD, and deriving a contradiction with the triangle inequality (1.20). The key intermediate conclusions are the same in both proofs. The citation difference consists entirely of explicit foundational references the AI adds (3.1 for finding centers, D1.15 for the definition of a circle, D3.3 for the definition of external tangency, CN2 and CN5 for arithmetic properties, P1 for drawing lines) that Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are construction, definition, common notion, or postulate-level over-citations, this is a granularity difference (G).

### 3.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs argue through the same two-case structure (internal and external touching) with identical key intermediate conclusions: for the internal case, the line through the two centers passes through both alleged contact points (3.11), radii from one center are equal while the segment to the other center's contact point is strictly smaller, yielding a contradiction with equal radii from the second center; for the external case, the joining line falls within both circles (3.2) contradicting the external tangency condition (D3.3). The AI proof is more explicit, citing constructions (3.1), definitions (D1.15, D1.17), a supporting lemma (3.6), a common notion (CN5), and a postulate (P1) that Heath uses implicitly. Since heath_only is empty and all ai_only items are over-citations of foundational results used implicitly by Heath, this is Case A of Q2: same backbone, different citation depth.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish the same biconditional through identical key intermediate conclusions: perpendiculars from the centre bisect each chord (3.3), radii are equal, the Pythagorean theorem (1.47) yields sum-of-squares equations, and subtraction of equal squares produces the desired equality in each direction. The AI proof's six additional citations (1.12, CN1, CN2, CN3, D1.15, P1) are all construction propositions, common notions, definitions, and postulates that Heath invokes implicitly without explicit citation. With heath_only empty, every substantive proposition Heath cites is also cited by the AI, confirming the backbone is the same. This is a clear Case A granularity difference: same logical backbone, different citation depth.

### 3.15
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct a chord MN equidistant from the center as BC, prove BC = MN via III.14, show AD exceeds BC via the triangle inequality (I.20), and show MN exceeds FG via I.24 on triangles MEN and FEG. The slight variation in Step 5 (Heath uses triangle MEN while the AI uses triangle EBC to apply I.20) is an equivalent restatement of the same intermediate conclusion, not a different path. The heath_only set is empty, meaning the AI cites everything Heath does. The ai_only set consists entirely of construction propositions (1.3, 1.11, 1.12), postulates (P1, P2), common notions (CN2, CN5), and definitions (D1.15, D1.17, D3.4) that Heath uses implicitly but does not cite. This is a clear Case A: same backbone, different citation depth.

### 3.16
**Category**: Path difference
**Jaccard**: 0.176
**Analysis**: Q2 decides the classification. The first two parts of the proof (tangent falls outside the circle, no line can be interposed) share the same backbone in both Heath and the AI, with the AI over-citing definitions, postulates, and construction propositions such as I.12 and I.13. However, for the third part (angle comparisons), the proofs take genuinely different paths: Heath uses reductio ad absurdum, arguing that if a greater or lesser rectilineal angle existed then a line would be interposed between the tangent and circumference, contradicting part 2. The AI instead uses a direct construction via I.23 and III.2, establishing the key intermediate that every line drawn from A within angle BAE falls within the circle, then constructing an angle equal to any given acute angle K and comparing via the part-whole relation (CN5). This constitutes different key intermediate conclusions for the third part, making Case B in Q2 apply. Since the AI's different path is logically sound and complete (Q3 holds), the classification is D.

### 3.17
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided this classification. Both proofs establish identical key intermediate conclusions in the same order: (1) EA = EF and ED = EB as radii of the two circles, (2) triangles DEF and BEA are congruent by SAS (I.4), (3) angle EBA equals angle EDF, (4) angle EBA is right because EDF is right, and (5) AB touches the circle by III.16. The AI proof is a strict superset of Heath's citations, adding only definitions (D1.15, D1.17, D3.2), postulates (P1, P2, P3), and one construction proposition (1.11) that Heath leaves implicit. With heath_only empty and all ai_only items being basic building blocks, this is a clear case of the AI citing at finer granularity while following the same logical backbone.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assume FC is not perpendicular to the tangent DE, draw FG perpendicular to DE, establish that angle FGC is right and angle FCG is acute (I.17) so FC > FG (I.19), then show that G lies outside the circle so FG crosses the circumference at B making FG > FB, while FB = FC as radii, yielding a contradiction. The AI proof cites every construction, definition, and axiom explicitly (1.12 for drawing the perpendicular, 3.1 for finding the centre, D1.10 and D1.15 for definitions, D3.2 for the tangent definition, CN5 for the whole-greater-than-part axiom, P1 for joining points, and 3.2 to justify that G lies outside the circle), whereas Heath leaves all of these implicit and cites only I.17 and I.19. Since heath_only is empty and all ai_only items are construction propositions, definitions, postulates, common notions, or a supporting proposition used at the same logical position, this is a citation-depth difference with identical logical backbone, yielding G.

### 3.19
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction assuming the centre F lies off the perpendicular AC to the tangent DE, then invoking III.18 to establish that FC is also perpendicular to DE, and finally deriving the impossible conclusion that a proper part of an angle equals the whole angle. The ai_only set {CN5, D1.10, P1, P4} consists entirely of common notions, definitions, and postulates that Heath uses implicitly but does not cite. The AI simply makes these foundational references explicit (e.g., citing P4 for equality of right angles, CN5 for the whole being greater than the part, D1.10 for the definition of right angle, P1 for joining points). Since the key intermediate conclusions are identical and the citation difference is purely one of depth, this is a granularity difference (G).

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that radii from the center create isosceles triangles (I.5), apply the exterior angle theorem (I.32) to show each sub-angle at the center is double the corresponding sub-angle at the circumference, and then combine the results. The AI covers three explicit cases (center inside, outside, and on one side of the inscribed angle) while Heath covers two, but the core argument is identical. The ai_only set consists entirely of common notions (CN1, CN2, CN3), a definition (D1.15), and postulates (P1, P2) that Heath leaves implicit, while heath_only is empty. This is a textbook Case A from Q2: same backbone, different citation depth, yielding G.

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: find the center F of the circle, join BF and FD, apply III.20 twice to show that the central angle BFD is double of each inscribed angle BAD and BED, and conclude that BAD equals BED. The AI proof cites five additional references (3.1, CN1, D3.8, D3.9, P1) that Heath leaves implicit; these are all construction propositions, definitions, postulates, and common notions, not substantive theorems. Heath's proof performs the same constructions and uses the same common notion but without explicit citation. Since the key intermediate conclusions are identical and the citation difference reflects only the depth of explicit justification, this is a granularity difference.

### 3.22
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: join diagonals AC and BD, apply the triangle angle sum (I.32) to triangle ABC, then use the inscribed angle theorem (III.21) to equate angle CAB with angle BDC and angle ACB with angle ADB, combine these to show the whole angle ADC equals angles BAC plus ACB, add angle ABC to both sides, and conclude ABC plus ADC equals two right angles. The AI proof additionally cites CN1, CN2, D3.8, and P1, all of which are axiom-level or definition-level references that Heath uses implicitly. Since the key intermediate conclusions are the same and the citation difference consists entirely of foundational items the AI made explicit, this is a granularity difference.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy: assume two similar and unequal segments ACB and ADB on the same side of AB, draw line ACD through so that A, C, D are collinear, then show angle ACB equals angle ADB by similarity (Def. 11) while also being an exterior angle of triangle BCD and hence greater than ADB by I.16, yielding a contradiction. The AI proof establishes exactly the same backbone but with greater citation depth, explicitly invoking 3.10 to justify that the two circumferences meet only at A and B, CN4 to justify that unequal segments do not coincide, and citing definitions D3.6 and D3.8 plus postulates P1 and P2 that Heath leaves implicit. Since heath_only is empty and the ai_only items are all over-citations of the same underlying argument, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 3.24
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same superposition backbone: placing segment AEB onto CFD so A falls on C and B on D (since AB = CD), then arguing by contradiction that the arcs must coincide by considering three cases (the transported arc falls within, outside, or awry of the target arc), and concluding the segments are equal. The AI proof handles all three cases explicitly, using 3.23 to refute the within/outside cases and 3.10 for the awry case, whereas Heath's compressed proof mentions all three cases but only explicitly resolves the awry case via III.10. The AI also cites definitions (D3.6, D3.11) and common notions (CN4, CN5) that Heath invokes implicitly. Since the key intermediate conclusions are identical and the citation differences reflect depth of justification rather than a different logical path, this is a granularity difference.

### 3.25
**Category**: Granularity difference
**Jaccard**: 0.056
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: bisecting AC at D with DB perpendicular, distinguishing three cases by the relative size of angles ABD and BAD, and in each case establishing three equal lines from a point to the circumference (AE = BE = CE in Cases I and III, DA = DB = DC in Case II). The only substantive citation difference is in the final justification: Heath uses 3.9 (three equal lines from an interior point to a circle imply the point is the centre) while the AI constructs the circle explicitly via P3 and D1.15, then argues uniqueness via 3.10 (a circle does not cut a circle at more than two points). These achieve the same geometric conclusion through different citations. The remaining 15 ai_only items are over-citations of construction steps (1.10, 1.11, 1.23), postulates (P1-P5), common notions (CN1), definitions (D1.15, D1.17, D1.18), and elementary propositions (1.4, 1.6, 1.13, 1.17). The Jaccard of 0.056 reflects this heavy over-citation rather than a genuine path divergence.

### 3.26
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: equal radii yield BC=EF via I.4, the equal angles make segments BAC and EDF similar via Def. 11, similar segments on equal lines are equal via III.24, and subtracting equal segments from equal circles gives equal circumferences. The AI proof adds an explicit preliminary step using 3.20 to show that equality of either central or circumference angles implies equality of both, whereas Heath handles this implicitly. All ai_only items are either definitions, common notions, and postulates cited explicitly by the AI but left implicit by Heath, or 3.20 which provides additional case-handling depth rather than a different path. Since heath_only is empty and the key intermediate conclusions are identical, this is a granularity difference.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: a proof by contradiction for the central angle case (assuming BGC > EHF, constructing angle BGK = EHF via I.23, deriving arc BK = arc EF via III.26, reaching a contradiction with arc BC = arc EF), followed by deriving the circumference angle case via III.20. The AI's only additional citations are CN1 (transitivity of equality, used to chain arc BK = arc EF = arc BC) and CN5 (whole greater than part, used to state the contradiction explicitly), both of which Heath invokes implicitly. Since the ai_only set consists entirely of common notions making explicit what Heath leaves implicit, and the key intermediate conclusions are identical in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification. Both proofs follow an identical logical backbone: take the centres of the equal circles, join the radii, apply SSS (I.8) to establish equal central angles, invoke III.26 to conclude the lesser circumferences are equal, and subtract to obtain equal greater circumferences. The ai_only set {3.1, CN3, D1.15, D3.1, P1} consists entirely of a construction proposition (3.1 for finding centres), definitions (D1.15, D3.1), a common notion (CN3), and a postulate (P1) that Heath employs implicitly without citation. The heath_only set is empty. Since the key intermediate conclusions are the same and the citation differences reflect only the depth at which foundational steps are cited, this is a granularity difference (G).

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) equal circumferences imply equal central angles via 3.27, (2) equal circles have equal radii, and (3) SAS congruence via 1.4 yields BC = EF. The AI's additional citations (3.1 for finding centres, D3.1 for the definition of equal circles, P1 for joining lines) are all construction-level or definitional references that Heath performs implicitly without citation. Since heath_only is empty and all ai_only items are construction/definition/postulate over-citations, this is a clear Case A granularity difference.

### 3.30
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: bisect chord AB at C, erect a perpendicular CD to meet the arc, prove AD = DB by triangle congruence (I.4), then conclude arc AD = arc DB via III.28 because equal chords cut equal lesser arcs. The AI proof cites eight additional references that Heath leaves implicit: construction propositions (P1, 1.10, 1.11), the postulate that all right angles are equal (P4), and an elaborate justification that each arc is less than a semicircle using 3.1 Porism, D1.17, D1.18, and CN5. Since heath_only is empty and all ai_only items are construction steps, axioms, definitions, or deeper elaborations of the same intermediate conclusion, this is Case A -- same backbone, different citation depth -- yielding G.

### 3.31
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct AE and produce BA to F, use two applications of I.5 on isosceles triangles to equate base angles, invoke I.32 to show angle BAC equals exterior angle FAC and hence each is right (D1.10), apply I.17 to conclude the angle in the greater segment is less than a right angle, and apply III.22 to conclude the angle in the less segment is greater than a right angle. The AI proof covers all five required cases just as Heath does. The ai_only set consists entirely of definitions (D1.15, D1.17, D1.18, D3.6, D3.7, D3.8), common notions (CN1, CN2, CN5), postulates (P1, P2), and two minor propositions (3.2 used to justify that a chord lies within the circle, 3.21 used to generalize from the specific angle to all angles in the same segment). Heath leaves all of these implicit. The heath_only set is empty, confirming the AI cites everything Heath does and more. This is a clear case of the same backbone argued at greater citation depth.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same logical order: BA is a diameter because the center lies on BA (III.19), angle ADB is right as an angle in a semicircle (III.31), angles BAD and ABD sum to one right angle (I.32), angle DBF equals angle BAD by subtracting ABD from the right angle ABF, and then angle DBE equals angle DCB using the cyclic quadrilateral property (III.22) and the supplementary angle relation. The ai_only set consists entirely of definitions (D1.10, D1.17, D1.18, D3.8), postulates (P1, P2, P4), common notions (CN1, CN3), construction propositions (1.11, 1.13), and 3.18 used only in an additional explicit case where BD passes through the center. Heath leaves all of these implicit. heath_only is empty. This is Case A in Q2: same backbone, different citation depth, yielding G.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions across all three cases (acute, right, obtuse): constructing the angle equal to C, bisecting AB, showing AG=BG via I.4, describing the circle, establishing tangency via III.16, and applying the alternate segment theorem III.32 (acute and obtuse cases) or the semicircle angle theorem III.31 (right case). The heath_only set is empty, confirming every substantive step in Heath appears in the AI proof. The ai_only set consists entirely of construction propositions (1.10, 1.11, 1.23), postulates (P1-P5), common notions (CN1), and definitions (D1.15, D1.17, D1.18, D3.6, D3.8) that Heath leaves implicit. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: draw a tangent at B, construct angle FBC equal to the given angle D using I.23, then apply the tangent-chord angle theorem (III.32) to conclude that the angle in the alternate segment BAC equals angle FBC and hence equals D. The AI proof adds explicit citations for supporting constructions and axioms that Heath leaves implicit: 3.17 for the existence of the tangent, 3.16 for the property that a tangent touches the circle at exactly one point (used to justify that BC enters the circle), CN1 for the transitivity step, and D3.8 for the definition of an angle in a segment. Since heath_only is empty and all ai_only items are construction propositions, a common notion, and a definition, this is a clear case of over-citation with the same logical backbone, yielding Granularity difference.

### 3.35
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that for each chord through the intersection point E, the rectangle of the segments plus the square on EF equals the square on the radius (using III.3 bisection, II.5 algebraic identity, and I.47 Pythagorean theorem), then use equality of radii and subtraction to conclude rect(AE,EC) = rect(DE,EB). The AI proof is more thorough in case coverage (handling chords through the centre and the degenerate sub-case where E coincides with the perpendicular foot) and more explicit in citing foundational references. All ai_only items (1.12, 3.1, CN1, CN2, CN3, D1.10, D1.15, P1) are construction propositions, common notions, definitions, and postulates that Heath uses implicitly, and heath_only is empty. This is Case A of Q2: same backbone, different citation depth.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs address the same two cases (secant through the centre and secant not through the centre) with identical key intermediate conclusions: establishing that the tangent-radius angle is right (III.18), applying the rectangle-plus-square identity (II.6) to the bisected chord with added segment, and using the Pythagorean theorem (I.47) to convert sums of squares before subtracting to reach the final equality. The AI proof cites every foundational item explicitly (postulate P1 for joining lines, 1.12 for perpendicular construction, 3.1 for finding the centre, D1.15 for radii equality, and common notions CN1/CN2/CN3 for equality manipulations), while Heath leaves these implicit. Since heath_only is empty and all ai_only items are construction propositions, postulates, definitions, and common notions, this is a clear case of over-citation at a finer granularity with no backbone divergence.

### 3.37
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided this classification. Both proofs follow an identical logical backbone: construct a tangent DE from external point D, find the center F, show angle FED is right (III.18), use III.36 to establish AD*DC = DE^2, derive DE = DB from the hypothesis, note FE = FB as radii, apply I.8 for triangle congruence to conclude angle DBF equals the right angle DEF, and invoke III.16 to conclude DB is tangent. The AI's seven extra citations (3.1, 3.17, CN1, D1.15, D1.17, P1, P2) are all construction steps, postulates, definitions, and common notions that Heath uses implicitly without citing. Since heath_only is empty and all ai_only items represent over-citation of auxiliary steps rather than substantive divergence, this is Case A of Q2: same backbone, different citation depth.


---

## Book 4 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 13 | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.10, 4.11, 4.13, 4.15, 4.16 |
| Path difference (D) | 3 | 4.9, 4.12, 4.14 |
| AI proof error (E) | 0 |  |

**Total**: 16 propositions

## Per-Proposition Analysis

### 4.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: draw a diameter BC, handle the trivial case BC = D, and for BC > D cut CE = D from the diameter, draw a circle with center C and radius CE, join CA to an intersection point, and conclude CA = CE = D. The AI proof is more verbose, explicitly citing foundational items that Heath leaves implicit: postulates P1, P2, P3 for constructions, definitions D1.15 (radii equal), D1.17 (diameter), D4.7 (fitting into a circle), common notion CN1 (transitivity of equality), and construction propositions 1.3 (cutting a segment) and 3.1 (finding center). Since heath_refs is empty and all ai_only items are definitions, postulates, common notions, or basic construction results, this is a clear case of over-citation with the same backbone, yielding Granularity difference (G).

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct a tangent at a point on the circle, construct two angles at the tangent point equal to two angles of the given triangle, apply III.32 (tangent-chord angle equals inscribed angle in alternate segment) to establish two angle equalities, then use I.32 (angle sum) for the third. The AI proof is more explicit about the tangent construction (finding the center with 3.1, drawing a perpendicular with 1.11, then invoking 3.16 Porism) and cites common notions (CN1, CN3), a definition (D4.3), and postulates (P1, P2) that Heath leaves implicit. The heath_only set is empty, confirming that the AI covers all of Heath's citations and simply adds lower-level detail. This is Case A of Q2: same backbone, different citation depth.

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided this classification as Case A (same backbone, different citation depth). Both proofs construct central angles BKA equal to DEG and BKC equal to DFH, establish that the tangent lines at A, B, C are perpendicular to the radii, then use the quadrilateral angle sum to show AMB equals DEF and BNC equals DFE, and finally invoke I.32 to conclude the remaining angle NLM equals FDE. The sole substantive difference is how perpendicularity at the tangent points is established: Heath draws tangent lines via III.16 then invokes III.18 to conclude they are perpendicular to the radii, while the AI constructs perpendiculars to the diameters via I.11 then uses the Porism of III.16 to conclude these perpendicular lines are tangent. The key intermediate conclusions are identical throughout. The ai_only set consists entirely of over-citations (construction prop I.11, common notions CN1-CN3, definitions D1.17 and D4.4, postulates P1-P2), and the single heath_only item III.18 is functionally replaced by the AI's equivalent I.11 plus III.16 Porism approach. This is a citation-depth difference, not a backbone difference.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: bisect two angles of the triangle, show the bisectors meet at D, drop perpendiculars DE, DF, DG to the three sides, use I.26 twice to establish DE=DF=DG, describe the circle with center D and that common radius, invoke III.16 to show the circle touches each side, and conclude the circle is inscribed by IV. Def. 5. The heath_only set is empty, confirming that every citation Heath makes also appears in the AI proof. The ai_only set consists entirely of construction propositions (1.12), a lemma justifying why the bisectors meet (1.17), postulates (P3, P4, P5), common notions (CN1, CN5), and definitions (D1.10, D1.15), all of which represent the AI citing foundational steps that Heath leaves implicit. This is a clear Case A in Q2: same key intermediate conclusions with different citation depth, yielding G.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two sides of the triangle at their midpoints, erect perpendiculars at those midpoints, show the intersection point F is equidistant from all three vertices using I.4, and circumscribe the circle. The AI's additional citations (1.11, 1.13, 1.28, 1.29, 1.30, common notions, definitions, postulates) reflect over-citation of construction steps and foundational principles, plus an explicit proof that the perpendicular bisectors must meet (Steps 3-4), which Heath simply assumes and handles through three separate cases. Since heath_only is empty and the ai_only items are either foundational over-citations or support for an expanded argument within the same logical framework, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct two perpendicular diameters, prove the quadrilateral equilateral via I.4, prove it right-angled via III.31 (angle in a semicircle), and conclude it is a square by definition (I.Def.22). The heath_only set is empty, confirming the AI omits nothing Heath cites. The ai_only set consists entirely of construction propositions (1.11, 3.1), a basic lemma on vertical angles (1.15), definitions (D1.15, D1.17, D1.18, D3.8, D4.3), common notions (CN1), and postulates (P1, P2, P4) — all of which Heath uses implicitly but does not cite. This is a textbook granularity difference: the same proof argued at a finer level of explicit citation.

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: drawing two perpendicular diameters, constructing tangent lines at their endpoints, proving opposite sides of the circumscribed quadrilateral are parallel (via I.28 and I.30), establishing equilaterality through parallelogram properties (I.34) and the equality of diameters, and proving right-angled corners via parallelogram angle relationships. The sole heath_only citation, III.18 (tangent-radius perpendicularity), is replaced in the AI proof by constructing the tangent lines as perpendiculars at the diameter endpoints (I.11 plus the porism to III.16), yielding the same geometric fact by a different but equivalent route. The 12 ai_only items are all construction propositions (1.11, 3.1), postulates (P1, P2), definitions (D1.10, D1.15, D1.17, D1.22, D4.4), common notions (CN1, CN2), and vertical angles (1.15), representing explicit over-citation of foundational steps that Heath leaves implicit. Since the key intermediate conclusions match and the citation differences reflect depth rather than path, this is a granularity difference.

### 4.8
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two sides of the square at E and F, construct lines EH and FK through these midpoints to form parallelograms, use parallelogram properties (1.34) to show the four segments GE, GF, GH, GK are equal, then inscribe a circle with center G tangent to all four sides via III.16. The sole structural difference is the construction method for EH and FK: Heath draws them as parallels directly using 1.31, while the AI draws them as perpendiculars using 1.11 and then proves they are parallel using 1.28. This is a construction-level decomposition of the same step, not a different backbone. The remaining ai_only items (CN1, D1.10, D1.15, D1.17, D1.22, D4.5, P3) are definitions, common notions, and postulates that Heath leaves implicit. This is Case A of Q2: same key intermediate conclusions, different citation depth.

### 4.9
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Heath's proof establishes that the diagonals bisect the angles of the square via I.8 (SSS congruence), then argues that halves of equal right angles are equal, yielding the base-angle equality needed for I.6. The AI proof takes a genuinely different route: it applies I.4 (SAS congruence) directly to triangle pairs such as DAB and CBA, using the equal sides and equal right angles of the square, to obtain the base-angle equalities without ever establishing angle bisection. Since I.8 does not appear in the proof-tree of I.4 (I.4 precedes I.8), the containment test confirms this is not a granularity difference but a distinct geometric argument. Both proofs converge at the same final conclusion (EA = EB = EC = ED, hence a circle centered at E circumscribes the square), but the key intermediate step of angle bisection in Heath is replaced by direct SAS congruence in the AI proof, making this a path difference. The AI's chain is logically complete and sound, so Q3 confirms D.

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.467
**Analysis**: Q2 decides this classification as G. Both proofs construct isosceles triangle ABD through identical key intermediate conclusions: cutting AB at C so that rect(AB,BC) = sq(AC) via II.11, fitting BD = AC into circle BDE via IV.1, circumscribing circle ACD via IV.5, establishing BD as tangent to circle ACD via III.37, applying the alternate segment theorem III.32 to get angle BDC = angle DAC, deriving the chain of angle equalities through I.32 and I.5, and using I.6 to show BD = DC leading to CA = CD and the final doubling relation. The ai_only set consists entirely of foundational over-citations: common notions (CN1, CN2, CN5), definitions (D1.15, D1.20), postulates (P1, P3), and the construction proposition 4.1 which Heath also uses in his proof text but is not captured in heath_refs. Heath_only is empty, confirming that every substantive proposition Heath cites the AI also cites. The proofs share the same logical backbone at different citation depths.

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: constructing isosceles triangle FGH with angles at G and H double the angle at F (4.10), inscribing triangle ACD equiangular with FGH (4.2), bisecting angles ACD and CDA (1.9), deriving five equal inscribed angles, applying III.26 for equal circumferences, III.29 for equal sides (equilateral), then combining circumferences and applying III.27 for equal vertex angles (equiangular). The AI proof is logically complete with no defects under the hardened 1(b) standard. The citation difference consists entirely of the AI explicitly citing foundational items that Heath invokes implicitly: common notions CN1 and CN2, definitions D3.9 and D4.3, and postulates P1 and P2. With heath_only empty and ai_only containing only axioms, definitions, and postulates, this is a clear Case A same-backbone-different-depth scenario, yielding G.

### 4.12
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined the classification. Heath's proof works through the center F of the circle, using perpendicularity of tangent and radius (III.18), the Pythagorean theorem (I.47) on right triangles FBK and FCK to establish BK=CK, SSS congruence (I.8) for angle bisection, equal central angles from equal arcs (III.27), and ASA congruence (I.26) of triangles FKC and FLC. The AI proof takes a genuinely different route that stays entirely at the circumference: it uses the tangent-chord angle theorem (III.32) to show that both angles KBC and KCB equal the inscribed angle BDC, then the converse of the isosceles triangle theorem (I.6) to conclude BK=CK, applies the isosceles base angle theorem (I.5) to triangle BCD, and establishes triangle congruences KBC and LCD via ASA (I.26) without ever using the center for the main argument. The heath_only propositions (I.47, I.8, III.18, III.27) represent an independent geometric method not subsumed by any AI citation, and the ai_only substantive propositions (I.5, I.6, III.32) represent the AI's alternative circumference-based approach. The AI proof is logically complete and valid under the hardened Q1(b) standard, so Q3 confirms D.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: bisecting angles BCD and CDE to locate the incenter F, using I.4 to show BF equals DF and angle CBF equals angle CDF, demonstrating that all five angles of the pentagon are bisected by lines joining their vertices to F, dropping perpendiculars from F to all five sides and proving them equal via I.26, and finally inscribing the circle tangent to all sides via III.16. The AI's 12 additional citations (ai_only) consist entirely of construction propositions (1.9, 1.12), postulates (P1, P3, P4, P5), common notions (CN1, CN3), and definitions (D1.10, D1.15, D3.2, D4.5), all foundational items that Heath invokes implicitly without explicit citation. Heath_only is empty, confirming the AI covers all of Heath's reasoning at the same or finer granularity. This is a clear Case A granularity difference where the AI over-cites foundational results.

### 4.14
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof establishes that all five distances from center F to the vertices are equal by using I.6 (if two angles of a triangle are equal, the subtending sides are equal): since the half-angles FCD and CDF are equal, triangle FCD is isosceles and FC = FD, and similarly for the other radii. The AI proof takes a fundamentally different route, using I.4 (SAS congruence) repeatedly on pairs of adjacent triangles sharing a common side from F: triangles BCF and DCF yield BF = DF, triangles CDF and EDF yield CF = EF, and so on, with angle bisections of the remaining angles proved by CN3 subtraction. The AI explicitly remarks that it avoids the isosceles-triangle route. Since I.6 and I.4 are independent propositions and the logical backbones differ (angle-to-side via I.6 versus side-angle-side congruence via I.4), this is a genuine path difference. The proof-tree containment test confirms that I.6 does not appear inside the proof of I.4, so the heath_only citation represents an independent method, not a depth difference. The AI's SAS-based chain is logically complete and valid.

### 4.15
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: constructing the hexagon via a second circle centered at D, showing triangle EGD is equilateral, deriving each central angle as one-third of two right angles, using vertical angles (I.15) to establish all six central angles equal, then converting equal angles to equal arcs (III.26) to equal chords (III.29) for equilateral, and equal cumulative arcs to equal inscribed angles (III.27) for equiangular. The heath_only set is empty, confirming the AI cites every proposition Heath does. The ai_only set consists entirely of over-citations at a more foundational level: postulates (P1, P2, P3), definitions (D1.15, D1.17, D1.20, D4.3), common notions (CN1, CN2, CN3), and basic propositions (1.13 for supplementary angles, 3.1 for finding the center) that Heath leaves implicit. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.062
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: inscribe a side of the equilateral triangle (1/3 circumference) and a side of the equilateral pentagon (1/5 circumference), compute the remainder BC as 2/15, bisect BC at E using 3.30 to obtain arcs of 1/15, then fit equal chords around the circle to produce the equilateral and equiangular 15-gon. The AI proof is far more explicit, citing 16 propositions where Heath cites only 3.30, but the additional citations (4.2 for inscribing the triangle, 4.11 for the pentagon, 3.26 and 3.28 for arc-chord relationships, 4.1 for fitting lines, 3.27 for equiangularity, and several common notions) all make explicit what Heath's terse proof leaves implicit. The heath_only set is empty, confirming Heath uses no citation absent from the AI proof. This is Case A of Q2: same backbone, different citation depth.


---

## Book 5 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 3 | 5.4, 5.13, 5.19 |
| Granularity difference (G) | 20 | 5.2, 5.3, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11, 5.12, 5.14, 5.15, 5.16, 5.17, 5.20, 5.21, 5.22, 5.23, 5.24, 5.25 |
| Path difference (D) | 2 | 5.1, 5.18 |
| AI proof error (E) | 0 |  |

**Total**: 25 propositions

## Per-Proposition Analysis

### 5.1
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The forward-dependency gate passes since all AI citations (CN1, CN2, CN3, CN5, D5.2) are Common Notions and Definitions. Q1 finds no logical defects: the AI proof is a thorough, step-by-step demonstration with every claim properly supported by cited Common Notions and the definition of multiples. Q2 reveals completely different backbones: the Heath proof establishes that equimultiples of magnitudes sum to equimultiples of the sum, while the AI proof establishes that if the whole and the subtracted part are equimultiples, then the remainders are also equimultiples. Since the two proofs argue through entirely different key intermediate conclusions (Case B), Q3 applies. The AI's path is logically complete and valid -- every step is justified by cited axioms or definitions, and the chain runs from premises to conclusion without gaps -- yielding a D classification.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this classification. Both proofs establish identical key intermediate conclusions: decomposing the first and fifth magnitudes into counted parts equal to the second magnitude, decomposing the third and sixth into counted parts equal to the fourth, then combining to show the sums are the same multiple. The AI explicitly cites Definition 5.2 (definition of multiple) at each step while Heath applies the same definition implicitly without formal citation. Since heath_only is empty and ai_only contains only a definition (D5.2), this is a citation-depth difference (Case A of Q2), yielding G.

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: dividing the equimultiples EF and GH into parts equal to A and C respectively, establishing that each part of EF is the same multiple of B as the corresponding part of GH is of D, and then applying V.2 to conclude that the sums maintain this equimultiple relationship. The only citation difference is that the AI explicitly invokes Definition 5.2 (the definition of equimultiple) where Heath leaves this implicit. Since D5.2 is a definition rather than a substantive proposition, this represents a citation-depth difference with no change to the logical backbone. This is Case A of Q2, yielding G.

### 5.4
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (5.3 is prior to 5.4 and D5.5 is a definition). Both proofs follow the identical logical backbone: after setting up the equimultiples E, F of A, C and G, H of B, D, both take further equimultiples K, L of E, F and M, N of G, H; both invoke 5.3 to show K, L are equimultiples of A, C and M, N are equimultiples of B, D; both apply Definition 5.5 to obtain the trichotomy and then again to conclude E:G :: F:H. The citation sets are identical (ai_used = heath_refs = {5.3, D5.5}), the Jaccard similarity is 1.0, and the key intermediate conclusions match exactly, yielding a Perfect match classification.

### 5.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct an auxiliary magnitude as the same multiple (Heath uses CG, the AI uses FD directly), apply V.1/5.1 to sum equimultiples, invoke the hypothesis to establish equality with AB, subtract to identify the auxiliary with the remainder EB, and conclude that EB is the desired multiple of FD. The ai_only set consists entirely of common notions (CN1, CN2, CN3) and a definition (D5.2) that Heath employs implicitly without citation, while heath_only is empty. This is a textbook over-citation pattern: the AI makes explicit the foundational axioms that Heath leaves tacit, producing a citation-depth difference with no divergence in the argumentative backbone.

### 5.6
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct CK equal to F (or the appropriate multiple of F), apply 5.2 to show AB is the same multiple of E that KH is of F, conclude KH equals CD since both are the same multiple of F, subtract the common magnitude CH to get KC equals HD, and then conclude HD equals F (Case 1) or HD is the same multiple of F as GB is of E (Case 2). The AI proof explicitly handles both cases while Heath dispatches Case 2 with 'similarly,' but the underlying argument structure is identical. The ai_only citations (CN1, CN3, CN5, D5.2) are all Common Notions and a Definition that Heath invokes implicitly at the same logical positions, representing over-citation rather than a different proof path. This is Case A of Q2: same backbone, different citation depth.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing equimultiples D, E of A, B and an arbitrary multiple F of C, proving D=E from the equality A=B, applying the three-way size comparison of D/E against F, and invoking Definition 5.5 to conclude first that A:C = B:C and then symmetrically that C:A = C:B. The AI proof explicitly cites CN1 (equals to the same are equal), CN2 (equals added to equals yield equals), and D5.2 (definition of equimultiple), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only common notions and a definition, the difference is purely one of citation depth with the same logical backbone, yielding G.

### 5.8
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: constructing equimultiples FH and K of AB and C via 5.1, showing GH equals K because EB equals C, finding the first multiple N of D exceeding K, proving FH exceeds N, and applying Definition 5.7 to conclude both ratio inequalities. The AI avoids Heath's two-case distinction (AE less than EB vs AE greater than EB) by always multiplying AE, handling the sub-case in Step 7, but this structural difference does not change the logical backbone. The ai_only citations CN2 and CN5 are Common Notions that Heath uses implicitly but the AI cites explicitly, confirming over-citation rather than a path difference. With the same backbone and different citation depth, this is a granularity difference.

### 5.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for both cases of the proposition: assume equal ratios, suppose the magnitudes are unequal, invoke 5.8 to derive that the ratios would in fact be unequal, reaching a contradiction. The AI proof explicitly cites definitions D5.5 (equal ratio) and D5.7 (greater ratio) to unpack what 5.8 yields, while Heath leaves these definitions implicit. Since heath_only is empty and ai_only contains only definitions, this is a citation-depth difference with an identical backbone, yielding G.

### 5.10
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs argue through exactly the same key intermediate conclusions using the same reductio ad absurdum structure: for each of the two parts of the proposition, they show the magnitudes are not equal (via 5.7) and that the wrong inequality is impossible (via 5.8), then conclude by exhaustion. The AI proof explicitly cites definitions D5.5 and D5.7 that Heath invokes implicitly, resulting in a pure citation-depth difference with no change to the logical backbone. Since heath_only is empty and ai_only contains only definitions, this is Case A of Q2, yielding Granularity difference.

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: setting up equimultiples G, H, K of A, C, E and L, M, N of B, D, F; deriving the equimultiple trichotomy from each given ratio equality (A:B = C:D and C:D = E:F); chaining the two trichotomies; and concluding A:B = E:F by the definition of same ratio. The only difference is that the AI explicitly cites Definition V.5 (D5.5) at each application of the definition of same ratio, whereas Heath applies the same definition without a formal citation. This is a citation-depth difference with the same logical backbone, placing the proof in Case A of Q2, yielding Granularity difference (G).

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take equimultiples of the antecedents and consequents, apply D5.5 to establish ordering relationships between individual equimultiples, conclude the same ordering holds for the sums, invoke 5.1 to show those sums are themselves equimultiples of the totals, and finish by D5.5. The AI proof adds two axiom-level over-citations not found in Heath: CN2 (common notion justifying addition of equals in Step 5) and D5.6 (definition of proportional magnitudes in Step 1). Heath uses both facts implicitly without citing them. Since the backbones are identical and the ai_only items are purely axiom-level elaborations, Case A of Q2 holds, yielding G.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues since both AI citations (D5.5, D5.7) are definitions. Q1 confirmed the AI proof is logically complete: it correctly invokes D5.7 to obtain equimultiples witnessing the greater ratio C:D > E:F, constructs corresponding equimultiples of A and B, applies D5.5 (same ratio definition) to transfer the inequality, and concludes via D5.7. Q2 confirmed both proofs share the same key intermediate conclusions in the same logical order. The citation sets are identical (ai_used = heath_refs = {D5.5, D5.7}) with Jaccard 1.0, yielding a perfect match.

### 5.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for the primary case (A > C): establishing A:B > C:B via 5.8, deriving C:D > C:B via 5.13, and concluding D < B via 5.10. The AI's four extra citations (5.7, 5.9, 5.11, D5.5) all arise from explicitly proving the two subsidiary cases (A = C and A < C) that Heath abbreviates with 'Similarly we can prove.' Since heath_only is empty, every citation Heath uses also appears in the AI proof. The difference is purely one of citation depth: the AI spells out the analogous reasoning Heath leaves to the reader, requiring the additional propositions for the equality and less-than cases. This is Case A of Q2, same backbone with different granularity.

### 5.15
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs share the same backbone: decompose the multiples into equal parts, establish that each pair of corresponding parts has the same ratio via 5.7, then apply 5.12 to aggregate one-antecedent-to-one-consequent into all-antecedents-to-all-consequents, and finally substitute back to obtain the desired ratio. The AI proof differs only in citation depth: it explicitly cites 5.11 (transitivity of equal ratios) for substitution steps that Heath performs implicitly, and it explicitly cites definitions D5.1, D5.2, and D5.6 that Heath uses without citation. Since heath_only is empty and all ai_only items (5.11, D5.1, D5.2, D5.6) represent over-citation of supporting lemmas and definitions rather than a different logical path, this is Case A of Q2: same key intermediate conclusions at different citation granularity.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish the identical backbone of key intermediate conclusions: equimultiples E,F of A,B and G,H of C,D are taken; 5.15 gives A:B=E:F and C:D=G:H; 5.11 chains these to get E:F=G:H; 5.14 yields the ordering comparison; and D5.5 delivers the conclusion A:C=B:D. The AI proof adds explicit citations to definitions D5.6 (ratio) and D5.12 (alternate proportion) that Heath invokes implicitly, making ai_only consist entirely of definitions with heath_only empty. This is a straightforward citation-depth difference with identical logical structure, yielding G.

### 5.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing equimultiples GH, HK, LM, MN of AE, EB, CF, FD and other equimultiples KO, NP of EB, FD; using 5.1 to show GK and LN are equimultiples of AB and CD; using 5.2 to show HO and MP are equimultiples of EB and FD; applying the given proportion to obtain the excess/equal/less correspondence for GK vs HO and LN vs MP; then subtracting common parts to transfer the correspondence to GH vs KO and LM vs NP; and concluding AE:EB = CF:FD. The ai_only citations (CN2, CN5, D5.14, D5.15, D5.5, D5.6) are exclusively definitions and common notions that Heath uses implicitly without explicit citation, representing over-citation rather than a structural difference. The heath_only set is empty. This is a clear case of the same backbone argued at different citation depth.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 5.18 by reductio ad absurdum, supposing AB:BE = CD:DG for DG less than FD, then applying 5.17 (componendo implies separando), 5.11 (transitivity of ratios), and 5.14 (ordering preservation) to derive a contradiction. The AI instead constructs a direct proof from D5.5 (the equimultiple definition of proportion), decomposing arbitrary equimultiples of the wholes into sums of equimultiples of the parts via 5.1 and 5.2, then performing exhaustive case analysis on the multiplier relationship to verify the equimultiple condition directly. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different: Heath reasons through higher-level proportion theorems in a reductio framework, while the AI works at the definitional level with direct equimultiple arithmetic. Since the AI's chain is logically complete with every step justified, this is a valid different path.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (all citations 5.11, 5.16, 5.17 precede 5.19). Both proofs follow an identical logical backbone: apply alternation (5.16) to the hypothesis AB:CD = AE:CF, then separando (5.17) to isolate the remainders, then alternation (5.16) again to obtain EB:FD = AE:CF, and finally transitivity (5.11) to conclude EB:FD = AB:CD. The citation sets are exactly equal with Jaccard 1.0, ai_only and heath_only are both empty, and the key intermediate conclusions match at every stage. The perfect match check at Step 6 confirms category P.

### 5.20
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions for the principal case (A > C): establishing A:B > C:B via 5.8, deriving D:E > F:E, and concluding D > F via 5.10. The AI proof is a strict superset of Heath's citations, with heath_only empty. The five ai_only items (5.7, 5.9, 5.11, D5.5, D5.7) are all explicitations of steps Heath leaves implicit: 5.7 for the inversion Heath performs without citation, 5.9 and 5.11 for the equal-magnitudes case Heath covers with 'similarly we can prove,' and D5.5/D5.7 for definitional expansions of ratio comparisons that Heath handles with a single application of 5.13. The backbone is identical across all three cases; the AI simply provides greater citation depth.

### 5.21
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for the principal case (A > C): establishing A:B > C:B via 5.8, deriving E:F > E:D via 5.13 and the proportion hypotheses, then concluding D > F via 5.10. The AI proof differs only in depth: it explicitly proves all three cases (A > C, A = C, A < C) where Heath says 'similarly we can prove,' and it cites definitions (D5.5, D5.7, D5.13, D5.17, D5.18) and additional propositions (5.7, 5.9, 5.11) needed for the equal and less cases. The AI also works through definition-level arguments rather than relying solely on 5.13 for ratio substitution. Since heath_only is empty and all AI-only citations represent either explicit definitions or propositions for cases Heath handles summarily, this is a granularity difference rather than a path difference.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone for the three-magnitude case: take equimultiples G,H of A,D; K,L of B,E; M,N of C,F; apply 5.4 twice to get G:K=H:L and K:M=L:N; invoke 5.20 for the ex aequali comparison on equimultiples; then conclude A:C=D:F by Definition 5.5. The AI proof adds an explicit citation to D5.17 (the definition of ex aequali ratio) and an inductive extension to more than three magnitudes (Step 7), neither of which changes the backbone. Since the key intermediate conclusions are identical and the only citation difference is the AI's additional definition reference D5.17, this is Case A of Q2: same backbone, different citation depth, yielding G. The citation sets are not identical (ai_used includes D5.17), so P does not apply.

### 5.23
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided this classification. Both proofs share an identical logical backbone: taking equimultiples G,H,K of A,B,D and L,M,N of C,E,F; using V.15 and V.11 to establish G:H = M:N; using V.16, V.15, and V.11 to derive H:K = C:E then H:K = L:M; alternating to get H:L = K:M; applying V.21 to the resulting perturbed proportion among multiples; and concluding A:C = D:F. The AI cites the same four theorems as Heath (5.11, 5.15, 5.16, 5.21) and additionally cites three definitions (D5.5, D5.17, D5.18) that Heath invokes implicitly without explicit citation. Since the key intermediate conclusions are identical and the only citation differences are definitional over-citations by the AI, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 5.24
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: inverting BG:C = EH:F to C:BG = F:EH, applying ex aequali (5.22) to obtain AB:BG = DE:EH, using componendo (5.18) to get AG:GB = DH:HE, and a final ex aequali (5.22) to reach AG:C = DH:F. The AI proof adds explicit citations for definitions (D5.5, D5.13, D5.14, D5.15, D5.17) and the inversion proposition (5.7) that Heath uses without explicit citation. Since heath_only is empty and all ai_only items are definitions or the inversion result underlying a step Heath performs implicitly, this is a citation-depth difference with the same logical backbone, yielding G.

### 5.25
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: substituting AG=E and CH=F, applying V.19 to obtain GB:HD = AB:CD, deducing GB > HD from AB > CD, noting AG+F = CH+E, and combining these to conclude AB+F > CD+E. The AI proof cites the same key proposition (5.19) as Heath but adds explicit citations for steps Heath performs implicitly: 1.3 for cutting off equal segments, 5.7 and 5.11 for the ratio substitution justifying AB:CD = AG:CH, 5.16 (alternando) and 5.14 for deducing the inequality GB > HD from the proportion, and CN2 and CN5 for combining the final results. Since heath_only is empty and all ai_only items are deeper-level citations for the same logical steps, this is Case A of Q2: same backbone, different citation depth, yielding G.


---

## Book 6 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 28 | 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 6.11, 6.12, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18, 6.19, 6.21, 6.24, 6.25, 6.26, 6.27, 6.28, 6.29, 6.32, 6.33 |
| Path difference (D) | 5 | 6.20, 6.22, 6.23, 6.30, 6.31 |
| AI proof error (E) | 0 |  |

**Total**: 33 propositions

## Per-Proposition Analysis

### 6.1
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: constructing equimultiples of the bases by extending the base line and marking equal segments, establishing equal triangles on equal bases via I.38, showing equimultiple correspondence between bases and triangles, verifying the three cases (equal, excess, less) for the definition of proportion (V. Def. 5), then extending to parallelograms via I.41, transferring the ratio via V.15, and concluding by transitivity via V.11. The AI proof cites six additional foundational references that Heath uses implicitly without citation: postulates P1 and P2 for joining and extending lines, proposition 1.3 for cutting off equal segments, common notion CN5 for the whole being greater than the part, and definitions D5.2 and D6.4 for equimultiples and height respectively. Since heath_only is empty and all ai_only items are postulates, common notions, definitions, or a basic construction proposition present implicitly in both proofs, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs follow identical two-part structures with the same key intermediate conclusions in the same order: in Part I, establishing BDE = CDE, deriving equal ratios to ADE, converting triangle ratios to segment ratios via VI.1/6.1, and concluding BD:DA = CE:EA via V.11/5.11; in Part II, reversing the argument through VI.1/6.1, V.11/5.11, V.9/5.9, and I.39/1.39. The only citation differences are that the AI uses I.37 (triangles on the same base in the same parallels are equal) where Heath uses I.38 (triangles on equal bases in the same parallels are equal) — both valid for the same logical fact since the triangles share the literal same base DE — and the AI over-cites D6.4 (definition of height) and P1 (postulate for joining lines). These are citation-depth differences at the same logical positions, making this Case A in Q2: same backbone, different granularity.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs are biconditional and prove both directions using the identical construction (draw a line through C parallel to DA, extend BA to meet it at E). The key intermediate conclusions are the same in both parts: establishing angle equalities via I.29, deducing AE = AC via I.6 (part 1) or I.5 (part 2), applying VI.2 for the proportionality, and substituting equals. The AI's seven extra citations (1.17, 1.31, 5.7, CN1, P1, P2, P5) are all construction-level postulates, common notions, or lower-level propositions that Heath uses implicitly. heath_only is empty, confirming that the AI cites everything Heath does and more. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 6.4
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: placing BC in line with CE, producing BA and ED to meet at F, establishing BF parallel to CD and AC parallel to FE via I.28, obtaining parallelogram FACD with FA equal to CD and AC equal to FD via I.34, then applying VI.2 twice to derive proportions, substituting equal sides, using alternando (V.16), and concluding with ex aequali (V.22). The AI proof adds four over-citations not in Heath: 5.7 and 5.11 to make the ratio substitution steps explicit (where Heath simply says 'But AF is equal to CD; therefore...'), P2 for producing lines, and D5.11 for the definition of corresponding sides. Since heath_only is empty and all ai_only items are granularity-level elaborations of steps Heath performs implicitly, this is Case A of Q2: same backbone, different citation depth.

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.700
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: construct triangle GEF on EF with angles equal to those of ABC (I.23), deduce remaining angle equality (I.32), apply VI.4 to obtain proportionality in the equiangular triangles, use V.11 and V.9 to show DE=GE and DF=GF, then apply I.8 and I.4 to establish congruence of triangles DEF and GEF, and chain the angle equalities to conclude. The AI's three additional citations (1.17, P5, CN1) are all over-citations providing explicit justification for steps Heath leaves implicit: 1.17 and P5 justify that the lines constructed at E and F actually meet to form triangle GEF, while CN1 makes the transitivity of angle equality explicit. Since the key intermediate conclusions are identical and the citation difference is purely one of depth, this is a granularity difference.

### 6.6
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: construct triangle DGF on DF with angles matching those of ABC (I.23), show ABC equiangular with DGF via the angle-sum property (I.32), apply proportionality of equiangular triangles (VI.4) to obtain GD:DF = BA:AC, combine with the hypothesis through V.11 to get ED:DF = GD:DF, conclude ED = DG (V.9), then use SAS congruence (I.4) to show DEF congruent to DGF and derive all angle equalities. The only citation difference is that the AI explicitly invokes CN1 (Common Notion 1, transitivity of equality) for the angle equality chains in Steps 7, 9, and 10, while Heath applies these substitutions implicitly without citation. Since CN1 is a common notion (axiom-level reference) and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference under Case A of Q2, yielding G.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.889
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assuming angle ABC is not equal to angle DEF, constructing angle ABG equal to DEF via I.23, showing triangle ABG equiangular with DEF via I.32, deriving AB:BG = DE:EF via VI.4, combining with the hypothesis via V.11 to get BC = BG via V.9, applying I.5 for the base angles, and then reaching a contradiction in each of the two cases (angles less than a right angle via I.13, angles not less via I.17). The AI proof addresses both cases explicitly and completely. The only citation difference is that the AI explicitly cites CN3 (Common Notion 3, equals subtracted from equals) in Steps 4 and 14, where Heath leaves the same reasoning implicit when invoking I.32 to conclude that remaining angles are equal. Since CN3 is a common notion (axiom) and not a substantive proposition, this is a straightforward over-citation, confirming Case A of Q2: same backbone, different citation depth.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing equiangularity of each sub-triangle with the whole triangle (right angles equal, one angle common, third angle equal by I.32), deriving proportional sides via VI.4, and concluding similarity via VI.Def.1, then proving mutual similarity of the two sub-triangles by the same method. The AI proof is more explicit, writing out both sub-triangle cases in full rather than using Heath's 'similarly,' and adding Step 2 (proving D lies between B and C using 1.16, 1.17). The ai_only set {1.16, 1.17, CN3, D1.10, P4} consists entirely of foundational over-citations: postulates, common notions, definitions, and basic Book 1 propositions used for construction details or implicit steps that Heath leaves uncited. The heath_only set is empty, confirming the AI covers everything Heath does at greater granular depth. This is Case A of Q2: same backbone, different citation depth.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) DF is drawn parallel to BC, (2) CD:DA = BF:FA by VI.2, (3) CD being double DA implies BF is double FA, (4) BA is triple of AF. The AI proof cites the same three substantive propositions as Heath (1.3, 1.31, 6.2) but adds five foundational items (CN2, D5.1, D5.5, P1, P2) that Heath leaves implicit. Since the backbones match and the citation difference consists entirely of postulates, definitions, and common notions that the AI makes explicit, this is a same-backbone, different-depth case under Q2 Case A, yielding G.

### 6.10
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: constructing parallels DF and EG to BC and DHK to AB, identifying parallelograms FGHD and GBKH to obtain DH=FG and HK=GB via I.34, then applying VI.2 twice in triangles DKC and AGE to derive the two required proportions CE:ED=BG:GF and ED:DA=GF:FA. The four ai_only citations (1.30, 5.7, 5.11, P1) are all explicit references for steps Heath performs implicitly: 1.30 for transitivity of parallelism, 5.7 and 5.11 for ratio substitution of equal magnitudes, and P1 for joining line BC. Heath_only is empty, confirming the AI cites a strict superset. Since the key intermediate conclusions are the same and only citation depth differs, this is Case A of Q2, yielding G.

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct BD equal to AC, join BC, draw DE parallel to BC through D, apply 6.2 to obtain AB:BD = AC:CE, then substitute BD = AC to conclude AB:AC = AC:CE. The AI proof over-cites by explicitly invoking P1 and P2 for basic constructions and 5.7 and 5.11 to spell out the ratio substitution that Heath performs implicitly in a single sentence. Since heath_only is empty and all ai_only items (P1, P2, 5.7, 5.11) represent finer-grained citations of steps Heath takes without explicit reference, this is a citation-depth difference with the same backbone, yielding G.

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct two lines DE, DF at any angle, mark off segments DG=A, GE=B, DH=C, join GH, draw EF parallel to GH through E, then apply 6.2 to obtain DG:GE = DH:HF, and substitute to conclude A:B = C:HF. The AI proof cites five additional references (P1, P2, 1.3, 5.7, 5.11) that Heath uses implicitly without citation. P1 and P2 justify setting out and producing lines, 1.3 justifies cutting off equal segments, and 5.7 and 5.11 justify the ratio substitution steps. Heath's proof has no citations absent from the AI proof (heath_only is empty). Since the key intermediate conclusions are identical and the citation differences reflect only the depth at which construction and ratio-substitution steps are made explicit, this is a granularity difference.

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: place AB and BC in a straight line, construct a semicircle on AC, draw BD perpendicular to AC, establish that angle ADC is right by III.31, and conclude that DB is a mean proportional by VI.8. The AI proof is far more explicit, citing construction postulates (P1, P2, P3), construction propositions (1.3, 1.10, 1.11), definitions (D1.15, D1.17, D1.18, D1.21, D6.1), and 6.4 to unpack the proportionality that Heath derives in a single step from VI.8. Since heath_only is empty and all ai_only items are construction citations, definitions, or an elaboration of VI.8's conclusion, this is Case A: same backbone with different citation depth, yielding Granularity difference (G).

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: placing the parallelograms so DB and BE are collinear, showing FB and BG are collinear via I.14, completing parallelogram FE, then using VI.1 twice with V.7 and V.11 for the forward direction, and VI.1 twice with V.11 and V.9 for the converse. The AI's six extra citations (1.13, 1.31, CN1, CN2, D6.2, D6.4) are all construction propositions, common notions, and definitions that Heath uses implicitly. The AI explicitly justifies the collinearity of FB and BG through supplementary angles (1.13, CN1, CN2) before invoking I.14, explicitly cites 1.31 for drawing parallels to complete FE, and references definitions D6.2 and D6.4 for clarity. Since heath_only is empty and all ai_only items represent over-citation of construction and foundational steps, this is Case A of Q2: same backbone, different citation depth.

### 6.15
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in both directions of the biconditional: placing the triangles so that CA is collinear with AD and EA with AB (via I.14), joining BD, using V.7 to establish equal ratios of the equal triangles to the common triangle BAD, converting triangle ratios to side ratios via VI.1, and concluding with V.11; the converse reverses the chain using VI.1, V.11, and V.9. The AI proof is strictly more explicit, adding 1.13, CN1, and CN2 to justify the collinearity step that Heath handles implicitly with I.14 alone, citing P1 for the join construction, and referencing D6.2 for the definition of reciprocal proportionality. All ai_only items (1.13, CN1, CN2, D6.2, P1) are construction props, axioms, or definitions representing over-citation, and heath_only is empty. The identical logical backbone with differing citation depth yields G.

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone for both directions of the biconditional: construct perpendiculars AG=F and CH=E, complete parallelograms BG and DH, derive the reciprocal proportion AB:CD=CH:AG from the hypothesis, then apply 6.14 to conclude equality of the parallelograms (and hence of the rectangles). The converse uses the same construction and applies 6.14 in reverse. The AI proof is substantially more verbose, explicitly citing 1.11 for perpendicular construction, 1.3 for cutting equal lengths, 1.31 for completing parallelograms, 1.29 for angle properties of parallels, 5.7 and 5.11 for proportion substitution steps, D2.1 for the definition of a rectangle, and P4 for equality of right angles, all of which Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are construction propositions, proportion lemmas, definitions, and postulates, this is a clear case of same backbone with different citation depth.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone for each direction of the biconditional: construct D equal to B, establish the four-term proportion A:B::D:C, apply 6.16 to equate rect(A,C) with rect(B,D), and identify rect(B,D) as sq(B) since B equals D, with the converse reversing this chain. The ai_only citations (1.2, 5.7, 5.11, D1.22, D2.1) are all over-citations that make explicit what Heath leaves implicit: the construction step (1.2), the ratio substitution when B equals D (5.7), transitivity of ratios (5.11), and the definitions identifying a rectangle and square (D1.22, D2.1). With heath_only empty and the logical backbone matching, this is Case A: same key intermediate conclusions at different citation depth, yielding G.

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: divide the given rectilineal figure into triangles by joining a diagonal, construct equiangular triangles on the given line AB using I.23 and I.32, establish proportional sides via VI.4, combine the proportions to show the whole figures have equal corresponding angles and proportional sides, and conclude similarity by VI.Def.1. The AI proof is strictly more explicit than Heath's, citing 1.17 and P5 to justify that constructed lines will meet, CN2 and CN3 for angle addition and subtraction, P1 for joining lines, and 5.22 for the ex aequali step combining proportions. All of these are foundational steps that Heath performs implicitly. Since heath_only is empty and all ai_only items represent deeper citation of the same reasoning rather than different intermediate conclusions, Case A of Q2 holds, yielding G.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing a third proportional BG via VI.11, using alternation (V.16) and transitivity (V.11) to establish AB:DE = EF:BG, applying VI.15 to show triangle ABG equals triangle DEF, invoking V.Def.9 for the duplicate ratio, and using VI.1 to relate the triangles by their bases. The ai_only set consists entirely of construction propositions (1.3, P1, P2), definitions (D6.1, D6.2), and ratio substitution (5.7), all reflecting more explicit citation of steps that Heath performs implicitly. The heath_only item D5.11 (definition of corresponding sides) is a definitional reference that the AI addresses through D6.1 instead. Since the logical backbone is the same and the citation differences are purely a matter of depth, this is a granularity difference.

### 6.20
**Category**: Path difference
**Jaccard**: 0.462
**Analysis**: The forward-dependency gate passes cleanly. Q1 finds no logical defect: the AI proof is complete and every step is properly supported by cited propositions. Q2 reveals that while the first part of the proof (dividing similar polygons into similar triangles, Steps 1-11) shares the same backbone as Heath — both use VI.6, VI.4, angle subtraction, and V.22 ex aequali in the same sequence — the second part (proving the triangles are in the same ratio as the wholes) follows a fundamentally different route. Heath joins the further diagonals AC and FH, uses I.32 to show partial triangles equiangular, and compares the component triangles through their bases using VI.1 and V.12 with alternation. The AI instead applies VI.19 to the shared corresponding sides (BE:GL and EC:LH) of adjacent similar triangle pairs, constructs third proportionals via 6.11, identifies the duplicate ratio via D5.9, equates the triangle ratios via 5.11, and sums via V.12. The heath_only references 1.32 and 6.1 belong entirely to Heath's diagonal-based approach and are not subsumed by any proposition the AI cites; conversely, the ai_only references 5.11, 6.11, and D5.9 belong to the AI's duplicate-ratio approach. This constitutes a genuine path divergence (Case B). Q3 confirms the AI's alternative chain is logically valid, running soundly from premises to conclusion, so the classification is D.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they unpack the similarity of A to C and B to C using Definition 6.1, then conclude that A must be equiangular with B and have proportional sides, hence A is similar to B. The AI proof makes two implicit transitivity steps explicit by citing CN1 (things equal to the same thing are equal to one another, for angle equality) and 5.11 (ratios the same with the same ratio are the same with one another, for side proportionality), while Heath performs these same logical moves without explicit citation. Since heath_only is empty and the ai_only items (CN1, 5.11) merely supply deeper justification for steps that both proofs share, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 6.22
**Category**: Path difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Part I of both proofs shares the same backbone: taking third proportionals, applying ex aequali (5.22), and linking figure ratios to line ratios via 6.19. However, Part II (the converse) follows a fundamentally different logical path. Heath constructs a line QR such that AB:CD = EF:QR, then uses 6.18 to build a similar figure SR on QR, applies the forward direction to get MF:SR = MF:NH, deduces NH = SR, and concludes GH = QR from the equal and similar figures. The AI instead constructs a fourth proportional X and a third proportional Y, derives through ratio arithmetic that P = Y and EF:X = X:P, then proves X = GH by a contradiction argument using ratio inequality propositions (5.8, 5.10, 5.13). The AI never constructs a similar figure and works entirely within Book V ratio theory for the converse, making the key intermediate conclusions genuinely different. Both paths are logically valid, so the classification is D.

### 6.23
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: The forward-dependency gate passes (all AI citations are from Books 1 and 6 with no forward references). Q1 finds the AI proof logically complete: it correctly constructs the intermediate parallelogram CH, establishes two ratio equalities via 6.1, and applies the definition of compound ratio (D6.5) directly to conclude. Q2 reveals Case B (different backbone): while both proofs share the same geometric core (constructing CH and using 6.1 twice to get AC:CH = BC:CG and CH:CF = DC:CE), Heath's proof introduces auxiliary magnitudes K, L, M via 6.12 (fourth proportional construction) and transfers ratios via 5.11 (transitivity), then combines via ex aequali. This auxiliary-line method is entirely absent from the AI proof, which instead bypasses the construction by directly applying D6.5 to the parallelogram chain AC, CH, CF. Since 5.11 and 6.12 are substantive propositions argued in Heath but absent from the AI proof (and not contained in any proposition the AI cites), Case A fails. At Q3, the AI's different path is logically complete and valid, yielding classification D.

### 6.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: using VI.2 on the two triangles formed by the diameter to establish proportions, combining via transitivity, composition, and alternation to show sides about the common angle are proportional, establishing equiangularity of the relevant triangles through parallel lines and common angles, deriving all proportional side ratios with ex aequali (V.22), and concluding similarity by VI.Def.1. The AI's six extra citations (1.29, 1.30, 1.34, 5.11, 6.4, CN1) all explicitly name propositions that Heath uses implicitly at the same logical positions: 1.29 for angle equalities from parallel lines, 1.30 for transitivity of parallelism, 1.34 for opposite angles of parallelograms, 5.11 for transitivity of proportions, 6.4 for proportional sides in equiangular triangles, and CN1 for equality of equals. Heath's proof leaves all of these implicit. With heath_only empty and all ai_only items being over-citations at the same logical steps, this is a clear Case A granularity difference.

### 6.25
**Category**: Granularity difference
**Jaccard**: 0.353
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: they construct the same parallelograms BE (equal to ABC) and CM (equal to D), establish collinearity of BC with CF and LE with EM, take GH as a mean proportional of BC and CF, construct KGH similar to ABC on GH, establish the core ratio BC:CF = ABC:KGH = BE:CM, and conclude KGH = D. The AI proof is significantly more explicit, citing sub-step propositions (1.14, 1.29, 1.34, CN1, CN2) for the collinearity arguments that Heath states without justification, and citing D5.9, 5.11, and 6.20 for steps Heath leaves implicit or handles with the triangle-specific 6.19 alone. The only substantive algebraic difference is that Heath uses V.16 (alternately) for the final deduction while the AI uses V.7 and V.9 instead, but both start from the same proportion (ABC:KGH = BE:CM) and the same equality (ABC = BE) and reach the same conclusion (KGH = CM = D). This is the same backbone argued at different citation depth, making it a granularity difference.

### 6.26
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy with identical key intermediate conclusions: assume the inner parallelogram is not about the same diameter, produce GF to meet the diameter at H, draw HK through H parallel to AD (1.31), establish that parallelogram AKHG is similar to ABCD (6.24), derive DA:AB = GA:AK and DA:AB = GA:AE from the two similarity relations, conclude GA:AK = GA:AE by 5.11, hence AK = AE by 5.9, contradicting the fact that one is a proper part of the other. The AI proof adds extensive foundational citations (1.30, CN5, D1.23, D6.1, P1, P2) that Heath leaves implicit, but these are entirely postulates, definitions, common notions, and a basic proposition about parallel lines. The heath_only set is empty. This is Case A: same backbone, different citation depth, yielding G.

### 6.27
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: establishing that DB and FB are about the same diameter via VI.26, using complements CF = FE via I.43, building the equality chain CH = KE and CG = CH via I.36, and concluding that AF equals only a portion of DB so AD > AF. The AI proof is more detailed, explicitly handling two cases and citing construction steps (1.10), postulates (P1, P2), and common notions (CN1, CN2, CN3, CN5) that Heath uses implicitly. Since heath_only is empty and all ai_only items are axioms, postulates, or construction references, this is a clear case of overcitation at the same backbone — a granularity difference.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: bisect AB at E, construct EBFG on EB similar to D (6.18), complete the parallelogram AG, handle the trivial case AG = C, then for the main case construct KM equal to the excess of GB over C and similar to D (6.25), show KM is similar to GB (6.21), prove GE > KL and GF > LM, cut off GO = KL and GP = LM to construct OGPQ, establish OGPQ is about the same diameter as EBFG (6.26), derive that the gnomon equals C, use complement equality and equal-base parallelogram results to conclude TS = C. The heath_only set is empty, confirming every Heath citation appears in the AI set. The 15 ai_only items are all construction propositions (1.10, 1.3, 1.31), foundational results (1.4, 1.34, 1.43), common notions (CN1-CN5), postulates (P1, P2), a definition (D6.1), 5.14 for inequality reasoning, and 6.24 for explicitly establishing similarity of parallelograms about the diameter, all of which are sub-steps Heath leaves implicit. This is a clear case of the same backbone argued at different citation depth.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect AB, construct BF similar to D on EB, construct GH equal to BF+C and similar to D via 6.25, build MN equal and similar to GH, invoke 6.26 for the common diameter, extract the gnomon equal to C, and use I.36 and I.43 to show the applied parallelogram equals C with the excess similar to D via 6.24. The heath_only set is empty, confirming every Heath citation appears in the AI's set. The 16 ai_only items are all elaborations of steps Heath leaves implicit: construction propositions (1.10, 1.3, 1.30, 1.31, 6.18), basic results used to prove sub-steps in detail (1.4, 1.34 for triangle congruence to establish MN=GH; 5.14 for the inequality FM>FL), common notions (CN1, CN2, CN3, CN5), definitions (D2.2, D6.1), and postulates (P1, P2). The AI's path note explicitly states it chose 5.14 over 6.20 and 1.4+1.34 over 6.14 for sub-arguments, but the key intermediate conclusions remain identical. This is Case A of Q2: same backbone, different citation depth.

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs the golden section via parallelogram application (6.29) and derives the proportion through reciprocal proportionality of equiangular parallelograms (6.14). The AI takes an entirely different route: it uses 2.11 to cut AB so that the rectangle contained by the whole and one segment equals the square on the other, then applies the converse of 6.17 to convert that rectangle-equals-square condition directly into the required proportion, and finally uses CN5 and 5.14 to establish the ordering of segments. The two proofs share zero citations (Jaccard = 0.0) and have fundamentally different key intermediate conclusions -- Heath argues through area subtraction and reciprocal proportionality while the AI argues through the mean proportional theorem. The AI proof is logically complete: each step is correctly justified by the cited proposition, and the chain runs soundly from premises to conclusion. The AI itself explicitly acknowledges Heath's route and explains why it chose the alternative path through 2.11 and 6.17.

### 6.31
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same construction (perpendicular from vertex to hypotenuse, yielding similar sub-triangles via 6.8), but their key intermediate conclusions diverge. Heath derives the continued proportion CB:BA = BA:BD from similarity and then applies 6.19 (similar triangles are in duplicate ratio of corresponding sides) to directly relate figure ratios to line-segment ratios. The AI takes a genuinely different route: it establishes the sub-triangles DBA and DAC as similar figures similarly described on the relevant sides (via D6.1), then uses 6.22 (proportional lines yield proportional similar figures) to set up Q:P = DBA:ABC and R:P = DAC:ABC, and finishes by combining these ratios with 5.24 and concluding via 5.16 and 5.9. Although 6.19 appears in Heath's proof of 6.22 (satisfying the containment test), the proofs' key intermediates are structurally different: Heath reasons through line-to-figure ratios via duplicate ratio, while the AI reasons through area-to-area ratios using sub-triangles as mediating similar figures. The AI itself acknowledges this is an alternative route chosen deliberately. Since the backbones differ (Case B) and the AI's chain is logically complete under Q3, the classification is D.

### 6.32
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: parallel lines yield equal alternate angles via I.29 applied twice, transitivity gives angle BAC equal to angle CDE, VI.6 establishes equiangular triangles so angle ABC equals angle DCE, the angle sum at C is shown equal to two right angles via I.32, and collinearity of BC and CE follows from I.14. The AI proof explicitly cites Common Notions CN1 and CN2 for transitivity of equality and addition of equals, whereas Heath applies these same axioms implicitly without citation. Since heath_only is empty and ai_only contains only Common Notions (axioms, not substantive propositions), this is a citation-depth difference with the same backbone, satisfying Case A of Q2.

### 6.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same Eudoxean equimultiple method: constructing equimultiple circumferences, establishing that the corresponding central angles are the same multiples (via III.27), verifying the triple comparison, applying V. Def. 5 to conclude the ratio of circumferences equals the ratio of central angles, and then extending to inscribed angles via the doubling relationship. The key intermediate conclusions are identical in both proofs. The AI simply cites more explicitly what Heath leaves implicit: P1 for joining lines, CN5 for the whole-greater-than-part comparison, III.20 for the inscribed angle theorem (Heath writes 'they are doubles respectively' without citation), V.15 for the ratio of halves, and V.11 for transitivity of ratios. With heath_only empty and all ai_only items being over-citations of construction details, axioms, and propositions that Heath invokes implicitly, this is a clear Case A granularity difference.


---

## Book 7 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 5 | 7.18, 7.23, 7.26, 7.36, 7.39 |
| Granularity difference (G) | 32 | 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 7.10, 7.11, 7.12, 7.13, 7.14, 7.15, 7.16, 7.17, 7.19, 7.20, 7.21, 7.22, 7.24, 7.25, 7.28, 7.29, 7.30, 7.31, 7.32, 7.34, 7.35, 7.37, 7.38 |
| Path difference (D) | 2 | 7.27, 7.33 |
| AI proof error (E) | 0 |  |

**Total**: 39 propositions

## Per-Proposition Analysis

### 7.1
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: a proof by contradiction assuming some number E measures both AB and CD, then tracing E through each remainder of the Euclidean algorithm (BF, AF, DG, CG, FH) until E must measure the unit AH, yielding a contradiction. The AI proof explicitly cites foundational definitions and common notions (CN3, CN5, D7.1, D7.2, D7.5) that Heath uses implicitly, while both cite D7.12. Since the key intermediate conclusions are the same and the citation difference consists entirely of definitions and common notions the AI made explicit, this is a granularity difference (G).

### 7.2
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the identical Euclidean algorithm backbone: two cases (CD measures AB directly; repeated subtraction otherwise), termination by 7.1, the chain showing CF measures both AB and CD, and the maximality proof by contradiction. The AI proof's only extra citations (CN5, D7.2, D7.3, D7.5) are definitions and a common notion explicitly cited in Step 2 to justify basic divisibility properties that Heath uses implicitly without citation. With heath_only empty and ai_only consisting entirely of definitions and common notions, this is a clear citation-depth difference under Case A of Q2, yielding G.

### 7.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same two-case backbone: take D = GCM(A,B) by 7.2, then either D measures C (Case 1) and D is the GCM, or D does not measure C (Case 2) and the GCM of C and D is taken as the overall GCM. Both cases are proved by contradiction using 7.2. The AI proof adds an explicit citation of D7.12 (the definition of numbers being prime to one another) to justify steps that Heath handles implicitly, such as establishing that A and B are not prime to one another before applying 7.2. Since the key intermediate conclusions are identical and the only citation difference is the AI's explicit use of a definition, this is a granularity difference (G).

### 7.4
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish the same three cases (BC measures A; BC does not measure A and A,BC are prime; BC does not measure A and A,BC are not prime) and reach the same key intermediate conclusions in each case. The AI proof explicitly cites definitions D7.2, D7.3, D7.4, and D7.12 that Heath invokes implicitly without citation, while both share the sole theorem citation 7.2. Since the logical backbone is identical and the only difference is citation depth for definitions, this is a granularity difference.

### 7.5
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: dividing BC into parts BG, GC equal to A and EF into parts EH, HF equal to D, showing the multitudes are equal, pairing corresponding parts to establish BG+EH = A+D and GC+HF = A+D, and concluding that BC+EF has the same number of parts equal to A+D as BC has parts equal to A. The AI proof explicitly cites CN2 (for adding equals) and D7.3 (definition of part/measures) where Heath leaves these foundational references implicit, resulting in ai_only containing only definitions and common notions with an empty heath_only set. This is Case A of Q2: same backbone with different citation depth, yielding G.

### 7.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decomposing AB into parts AG, GB of C and DE into parts DH, HE of F, applying VII.5 twice to show that AG+DH and GB+HE are each the same part of C+F as the corresponding part is of C, then reassembling to conclude that AB+DE is the same parts of C+F as AB is of C. The AI additionally cites definitions D7.3 (definition of part) and D7.4 (definition of parts) to justify the decomposition steps, which Heath uses implicitly without citation. Since the key intermediate conclusions are identical and the only difference is the AI's explicit citation of definitions, this is a citation-depth difference, yielding G.

### 7.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: constructing CG so that EB is the same part of CG as AE is of CF, applying VII.5 to show AB is the same part of GF as AE is of CF, deducing GF equals CD, subtracting CF to get GC equals FD, and concluding EB is the same part of FD as AB is of CD. The ai_only citations (CN1, CN3, D7.3) are all common notions and a definition that Heath uses implicitly but the AI cites explicitly. CN1 is invoked when concluding GF equals CD from both being the same multiple of AB, CN3 when subtracting CF from equal quantities, and D7.3 when interpreting the meaning of one number being a part of another. Since heath_only is empty and the backbone is identical, this is Case A of Q2: same key intermediate conclusions with different citation depth, yielding G.

### 7.8
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification. Both proofs follow the identical backbone: setting GH equal to AB and dividing it into parts GK, KH of CD while dividing AE into parts AL, LE of CF; showing GK > AL and KH > LE because CD > CF; applying VII.7 twice to establish that MK and NH are each the same part of FD as GK and KH are of CD; and combining to reach the conclusion. The AI proof cites CN2, CN3, CN5, D7.3, and D7.4 explicitly where Heath uses these common notions and definitions implicitly without citation. Since heath_only is empty and all ai_only items are foundational axioms and definitions, this is a pure citation-depth difference with the same logical backbone, yielding G.

### 7.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: divide BC and EF into parts equal to A and D respectively with equal multitudes, establish that the equal parts bear the same part-or-parts relationship, then aggregate via 7.5 and 7.6 to conclude the result for the whole numbers. The AI proof adds explicit citations to CN1 (to justify BG=GC and EH=HF from each being equal to A or D), D7.3 (definition of part/measuring), and D7.4 (definition of parts), which Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions and common notions rather than substantive propositions, this is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 7.10
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: dividing AB and DE into their respective parts of C and F with equal multitudes, applying 7.9 (alternation for a single part) to each corresponding pair, and then combining the results via 7.5 and 7.6. The AI proof is more explicit, splitting the final combination into dedicated cases (Step 6 for 'part' via 7.5, Step 7 for 'parts' via 7.6) and citing definitions D7.3 and D7.4 that Heath leaves implicit. Since ai_only contains only definitions and heath_only is empty, the symmetric difference reflects over-citation of axiom-level items rather than any structural divergence. The key intermediate conclusions are identical in both proofs, making this a granularity difference.

### 7.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: unfold the proportion AB:CD :: AE:CF via Definition 7.20 into a 'same part or parts' relation, apply the subtraction lemmas 7.7 (part) and 7.8 (parts) to establish the remainder relation, then fold back via D7.20 to conclude EB:FD :: AB:CD. The AI proof makes explicit a third case (multiples) by invoking definitions D7.3 and D7.5 to reduce it to the part case, whereas Heath handles this implicitly within the phrase 'whatever part or parts.' The ai_only items (D7.3, D7.5) are both definitions used to make this implicit step explicit, not substantive propositions introducing a different proof path. Since the key intermediate conclusions are identical and the difference is only in citation depth, this is Case A of Q2, yielding G.

### 7.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: from the given proportion A:B = C:D, Definition 7.20 extracts that A is the same part or parts of B that C is of D, then propositions 7.5 and 7.6 establish that the sum A+C bears the same relationship to the sum B+D, and Definition 7.20 concludes A:B = (A+C):(B+D). The AI proof adds explicit treatment of a 'multiple' case (citing definitions D7.3 and D7.5 to reduce it to the part case) and an explicit inductive extension to arbitrarily many proportional pairs, but these are expansions in depth, not changes in backbone. Since ai_only contains only definitions (D7.3, D7.5) and heath_only is empty, this is Case A: same key intermediate conclusions at different citation depth, yielding G.

### 7.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: from the given proportion A:B = C:D, they extract the 'same part or parts' relation via Def.20, apply an alternation lemma to switch the pairing of terms, and conclude A:C = B:D again by Def.20. The difference is purely one of citation depth: Heath handles all sub-cases together under the phrase 'whatever part or parts' and cites only 7.10, whereas the AI explicitly separates three cases (part, parts, multiple) and cites 7.9 for the 'part' case, 7.10 for the 'parts' case, and definitions D7.3 and D7.5 to reduce the 'multiple' case. Since heath_only is empty and all ai_only items (7.9, D7.3, D7.5) support the same intermediate conclusion at finer granularity, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 7.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: alternation (7.13) applied to each given proportion to obtain A:D=B:E and B:E=C:F, chaining these equalities to get A:D=C:F, then alternating again to reach A:C=D:F. The AI's only divergence is citing Definition 7.20 to explicitly spell out what ratio equality means (same multiple, part, or parts) during the transitivity step, whereas Heath leaves this implicit. Since ai_only contains only D7.20 (a definition providing additional justification depth) and heath_only is empty, this is a clear case of same backbone with different citation depth, yielding G.

### 7.15
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: dividing BC into units and EF into equal parts of D, establishing that the multitudes are equal, showing the pairwise proportionality BG:EK = GH:KL = HC:LF, applying 7.12 to aggregate the ratios into BG:EK = BC:EF, and substituting A for BG and D for EK to reach the conclusion. The AI proof explicitly cites definitions (D7.1, D7.2, D7.3, D7.20) and a common notion (CN1) that Heath uses implicitly without citing, producing a larger citation set but the same argumentative structure. This is a citation-depth difference, not a path difference, so the classification is G.

### 7.16
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) B measures C the same number of times that unit E measures A, (2) by alternation via 7.15, E measures B the same number of times that A measures C, (3) A measures D the same number of times that E measures B, and (4) since A measures both C and D the same number of times, C equals D. The AI proof's only additional citations (CN1, D7.1, D7.2, D7.15) are definitions and a common notion that Heath uses implicitly without explicit citation. This is a citation-depth difference with the same logical backbone, yielding G.

### 7.17
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that B measures D and C measures E each according to the units in A, conclude B:D = C:E via Definition 7.20, then alternate to B:C = D:E via Proposition 7.13. The AI proof differs only in citation depth, explicitly citing Definition 7.15 (multiplication as repeated addition), Definition 7.3 (definition of part), and Common Notion 1 (things equal to the same thing are equal to each other), all of which Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are definitions and common notions that support steps Heath performs without naming them, this is Case A of Q2: same backbone, different granularity of citation.

### 7.18
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (7.16 and 7.17 are both prior to 7.18). Both proofs follow an identical logical chain: first applying VII.16 to swap the order of multiplication (showing that A multiplying C equals C multiplying A, and similarly for B and C), then applying VII.17 to conclude that since C multiplying A and B produces D and E, the ratio A:B equals D:E. The citation sets are identical (7.16, 7.17) with Jaccard similarity 1.0, and the key intermediate conclusions match exactly, so the perfect match check at the end of the protocol assigns category P.

### 7.19
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in both directions of the biconditional: constructing G = A*C, deriving C:D :: G:E via VII.17, deriving A:B :: G:F via VII.18, combining the equal ratios to get G:E :: G:F, and concluding E = F via V.9 (forward direction), with the symmetric converse argument using V.7. The sole citation difference is that the AI explicitly cites 5.11 (transitivity of equal ratios) at multiple points where Heath performs the same logical step — chaining equal ratios — without naming a specific proposition. This is a straightforward over-citation: the AI names the transitivity principle that Heath leaves implicit. Since the backbones are identical and the only difference is citation depth, this is Case A of Q2, yielding G.

### 7.20
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: a proof by contradiction showing CD cannot be 'parts' of A (since that would yield smaller numbers CG, EH in the same ratio as CD, EF, contradicting minimality), followed by concluding CD is a part of A (by 7.4) and EF is the same part of B, so both measure the same number of times. The only difference lies in the internal mechanism of the contradiction step: Heath uses 7.12 (summing antecedents and consequents) to establish CG:EH = CD:EF, while the AI uses D7.20 and 7.13 (definition of proportion plus alternation) to establish CG:EH = A:B = CD:EF. Both reach the identical sub-conclusion. The ai_only items (CN5, D7.3, D7.4) are all definitions and common notions representing over-citation, and the heath_only item (7.12) is replaced by an equivalent derivation using propositions both proofs already cite. Since the key intermediate conclusions are the same and differences are limited to citation depth and internal derivation detail, this is a granularity difference.

### 7.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow an identical contradiction structure: assume A, B (prime to one another) are not the least pair in their ratio, take C, D as a lesser pair, apply 7.20 to get that C measures A the same number of times E as D measures B, derive that E measures both A and B, and reach a contradiction with D7.12. The key intermediate conclusions are identical in both proofs. The sole difference is that Heath cites 7.16 (commutativity of multiplication) while the AI cites 7.15 (alternation of unit measurement) to justify the same intermediate step: that E measures A according to the units in C. Since both propositions establish the same fact at the same logical position, this is Case A of Q2 -- same backbone with a different citation choice -- yielding G.

### 7.22
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: assume A, B are least in their ratio but not coprime, construct D and E from the measurement by C, derive D:E = A:B, show D < A and E < B, and reach a contradiction. The sole substantive difference is that Heath applies 7.17 directly (one number C multiplying two numbers D, E preserves ratio), while the AI applies 7.18 (two numbers D, E multiplying one number C preserves ratio). Since Heath's proof of 7.18 uses both 7.16 and 7.17 internally, the proof-tree containment test confirms that heath_only item 7.17 appears inside the proof of the AI's cited 7.18, making this a citation-depth difference. The remaining ai_only items are definitions (D7.12, D7.2, D7.3), a common notion (CN5), and proposition 7.16 used to explicitly justify D < A and E < B, which Heath states without citation. All differences are granularity, not backbone.

### 7.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate found no issues (D7.12 is a definition). Both proofs use identical proof-by-contradiction structures: assume C and B are not prime to one another, derive that some number D measures both C and B, then show D measures A (since D measures C and C measures A), yielding D as a common measure of A and B, contradicting that A and B are prime to one another via D7.12. The key intermediate conclusions are identical, and the citation sets match exactly (ai_used = heath_refs = {D7.12}, Jaccard = 1.0), so the perfect-match check assigns category P.

### 7.24
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs use the same contradiction backbone: assuming a non-unit E measures both C and D, deriving that A and E are coprime (7.23), establishing E*F = A*B, forming a proportion (7.19), using the coprimality of A and E to show they are least in that ratio (7.21), then applying 7.20 to conclude E measures B, contradicting B and C being coprime. The sole difference is that Heath explicitly cites 7.16 (commutativity of multiplication) as an intermediate sub-step when noting that F also measures D according to the units in E, whereas the AI goes directly from the definition of E measuring D to E*F = D using D7.15 without needing to swap the order. Since the key intermediate conclusions are identical and the only discrepancy is citation depth for a minor sub-step, this is a granularity difference.

### 7.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: introducing D equal to A, establishing that both D and A are prime to B, applying 7.24 to conclude the product D times A is prime to B, and identifying that product with C. The only difference is that the AI explicitly cites Definition 7.12 (the definition of numbers prime to one another) to justify the substitution step that Heath treats as self-evident from the setup. This is a citation-depth difference (over-citation of a definition), not a structural divergence, placing this squarely in category G.

### 7.26
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (7.24 is prior to 7.26). Both proofs establish the same three key intermediate conclusions using the same single citation: (1) since A and B are each prime to C, their product E is prime to C by 7.24; (2) since A and B are each prime to D, E is prime to D by 7.24; (3) since C and D are each prime to E, their product F is prime to E by 7.24. The citation sets are identical (ai_used = heath_refs = {7.24}), the Jaccard similarity is 1.0, and the logical backbones match exactly, yielding a Perfect match classification.

### 7.27
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. For the squares part, both proofs share an identical backbone using two applications of 7.25. For the cubes part, the backbones diverge: Heath establishes A prime to B-squared and A-squared prime to B-squared as key intermediates, then applies 7.26 (if two numbers are prime to two numbers both to each, their products are also prime) to conclude the cubes are coprime. The AI instead establishes A-cubed prime to B and A-cubed prime to B-squared as intermediates using 7.24 (if two numbers are each prime to a number, their product is prime to it) combined with 7.25, then applies 7.24 again to conclude the cubes are coprime. Although 7.24 appears inside the proof of 7.26, the AI does not re-derive 7.26 inline; it uses 7.24 in a structurally different arrangement that avoids establishing the cross-coprimality pairs Heath needs for 7.26. The AI's path is logically valid at every step, yielding a genuine path difference.

### 7.28
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for each direction of the biconditional: they argue by contradiction that a common measure of the sum and one part must also measure the other part, contradicting the coprimality hypothesis. The AI proof's extra citations (CN2, CN3, D7.14) are common notions and a definition that Heath uses implicitly without citing. CN3 justifies the subtraction step ('measures the remainder'), CN2 justifies the addition step ('measures the whole'), and D7.14 defines composite numbers. Since heath_only is empty and all ai_only items are axioms or definitions rather than substantive propositions, this is a clear case of over-citation at the same backbone, making it a granularity difference.

### 7.29
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Both proofs use an identical proof-by-contradiction backbone: assume A and B are not prime to one another, so some number C measures both; since C measures B but A does not measure B, C is not A; yet C measures A which is prime, contradicting the definition of prime. The AI proof explicitly cites D7.11 (definition of prime) and D7.12 (definition of prime to one another) while Heath uses these definitions implicitly without citation. Since the key intermediate conclusions are the same and the only difference is the AI's explicit citation of definitions that Heath invokes implicitly, this is a citation-depth difference under Case A of Q2, yielding G.

### 7.30
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume D does not measure A, conclude A and D are coprime (7.29), establish D*E = C via Def. 15, combine with A*B = C to obtain the proportion D:A = B:E (7.19), invoke that coprime numbers are least in their ratio (7.21), and apply that least numbers measure proportional numbers (7.20) to conclude D measures B. The AI's two extra citations -- 7.16 (commutativity of multiplication) and CN1 (things equal to the same are equal) -- make explicit steps that Heath leaves implicit, without altering the argumentative structure. With identical key intermediate conclusions and empty heath_only, this is Case A: same backbone, different citation depth.

### 7.31
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions: (1) A is composite so some number B measures it, (2) if B is prime the result follows, (3) if B is composite then some C measures B and transitivity gives C measuring A, (4) continuing this descent, if no prime is found an infinite strictly decreasing sequence of numbers all measuring A arises, which is impossible, (5) therefore some prime number measures A. The AI proof follows this same backbone in its eight steps. The only difference is that the AI explicitly cites definitions (D7.11 for prime, D7.13 for composite, D7.2 for number as multitude of units, D7.3 for part, D7.5 for multiple) that Heath leaves implicit. Since heath_refs is empty and all ai_only items are definitions, this is a citation-depth difference with identical logical structure, yielding Granularity difference (G).

### 7.32
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: (1) every number A is either prime or composite, (2) if A is prime the conclusion holds immediately, (3) if A is composite then by 7.31 some prime number measures it. The AI proof explicitly cites D7.11 (definition of prime) and D7.13 (definition of composite) to justify the prime-or-composite dichotomy, whereas Heath leaves these definitions implicit. Since ai_only contains only definitions and heath_only is empty, the proofs differ only in citation depth, not in their key intermediate conclusions. Case A of Q2 holds, yielding G.

### 7.33
**Category**: Path difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification. Heath's minimality proof constructs M (the number of times H measures A), shows E*D = H*M, then uses 7.19 to derive E:H = M:D, concluding M > D to reach a contradiction. The AI's minimality proof takes a fundamentally different route: it uses alternation (7.13) to establish E:H = F:K = G:L, invokes the least-numbers theorem (7.20) to find P measuring E, F, G with P not a unit, then builds T = P*D as a common measure greater than D for the contradiction. The two proofs share the same setup (GCD construction via 7.3) and the same contradiction target (exceeding the GCD), but their key intermediate conclusions -- Heath's product-proportion step (7.19) versus the AI's alternation-least-numbers chain (7.13, 7.20) -- are entirely different. The heath_only propositions (7.16, 7.19, 7.21) are not subsumed by any higher-level proposition the AI cites; they belong to an independent logical route. The AI's path is logically complete with every step justified, so this is a valid path difference.

### 7.34
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification. Both proofs follow the same two-case structure (A,B prime to one another vs. not prime) with identical key intermediate conclusions in each case: construct the candidate LCM, assume a smaller common multiple exists, derive a proportion via 7.19, use the minimality of the ratio (7.21 in Case 1, 7.33 in Case 2) with 7.20 to establish divisibility, then apply 7.17 to reach a contradiction. The logical backbones match exactly across both cases. The AI proof additionally cites definitions (D7.3, D7.12, D7.20) and a common notion (CN5) that Heath uses implicitly without explicit citation, making this a pure citation-depth difference. With heath_only empty and ai_only containing only definitions and common notions, the proofs differ only in the granularity of their references, not in their reasoning paths.

### 7.35
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy: assume the LCM E does not measure CD, perform repeated subtraction to obtain a remainder CF less than E, show that A and B both measure DF (by transitivity of measuring) and hence both measure the remainder CF, contradicting E being the least number measured by A and B. The key intermediate conclusions are identical in both proofs. The AI over-cites by explicitly referencing 7.34 (existence of LCM), CN3 (subtraction of equals), and D7.5 (definition of measuring), all of which Heath uses implicitly without citation. Since heath_refs is empty, the Jaccard is 0.0, but the proofs share the same logical backbone with the AI simply providing more granular citation depth, yielding G.

### 7.36
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (7.34 and 7.35 are both prior to 7.36). Q1 confirmed the AI proof is logically complete: both required cases (C measures D and C does not measure D) are fully addressed with correct contradiction arguments using 7.35. Q2 confirmed both proofs share the same backbone: find D as the least number measured by A and B via 7.34, then split into two cases and prove minimality by contradiction in each. Since the key intermediate conclusions are identical and the citation sets match exactly (ai_used = heath_refs = {7.34, 7.35}), the perfect match check yields category P.

### 7.37
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: defining C as the number of units corresponding to how many times B measures A, showing that the unit D measures C the same number of times as B measures A, applying alternation (7.15) to conclude D measures B the same number of times as C measures A, and then concluding that C is a part of A called by the same name as B. The AI proof adds explicit citations of D7.2 (definition of number as multitude of units) and D7.3 (definition of part), which Heath uses implicitly without citation. Since the key intermediate conclusions are identical and the only difference is the AI's explicit citation of definitions that Heath takes for granted, this is a citation-depth difference classified as G.

### 7.38
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: establishing that unit D measures C the same number of times that B measures A (from the definition of part and same-name numbering), then applying 7.15 (alternation) to conclude that D measures B the same number of times C measures A, and finally concluding that C measures A. The only difference is citation depth: the AI explicitly cites definitions D7.1 (unit), D7.2 (number as multitude of units), and D7.3 (part) that Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions, this is a classic over-citation granularity difference with identical proof structure.

### 7.39
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of 7.39 follows the exact same logical structure as Heath's proof: it constructs G as the least common multiple of D, E, F using 7.36, shows G has the required parts A, B, C using 7.37, and proves minimality by contradiction using 7.38. The citation sets are identical (ai_used = heath_refs = {7.36, 7.37, 7.38}) with Jaccard similarity 1.0, and the key intermediate conclusions match precisely, yielding a perfect match classification.


---

## Book 8 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 3 | 8.3, 8.7, 8.16 |
| Granularity difference (G) | 21 | 8.1, 8.2, 8.4, 8.6, 8.8, 8.9, 8.10, 8.11, 8.12, 8.13, 8.14, 8.15, 8.17, 8.18, 8.19, 8.20, 8.23, 8.24, 8.25, 8.26, 8.27 |
| Path difference (D) | 3 | 8.5, 8.21, 8.22 |
| AI proof error (E) | 0 |  |

**Total**: 27 propositions

## Per-Proposition Analysis

### 8.1
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume for contradiction that smaller numbers E, F, G, H exist in the same ratio as A, B, C, D; apply ex aequali (7.14) to obtain A:D = E:H; invoke the fact that prime numbers are least (7.21); conclude via 7.20 that A measures E, contradicting E < A. The AI proof adds explicit citations to definitions D7.12 (prime to one another) and D7.3 (part/measure), which Heath uses implicitly without citation. Since the key intermediate conclusions are identical and the only differences are additional definition citations by the AI, this is a citation-depth difference under Q2 Case A, yielding G.

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: they construct the same products (C, D, E, F, G, H, K) from A and B, establish each consecutive ratio equals A:B using VII.17 and VII.18 in the same logical positions, and prove minimality through the same chain (A,B coprime by VII.22, extremes coprime by VII.27, least by VIII.1). The AI proof adds two over-citations not in Heath: 7.33 to explicitly justify finding A, B as the least numbers in the given ratio (Heath simply assumes this), and D7.15 to cite the definition of multiplication for the construction steps (Heath takes this as implicit). Since the backbones match and the only differences are additional citation depth in the AI proof, Case A of Q2 holds, yielding G.

### 8.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (all citations 7.22, 7.27, 7.33, 8.2 precede 8.3). Q1 found the AI proof logically complete with no defects. Q2 confirmed both proofs share the same key intermediate conclusions: taking the least pair E, F in the common ratio via 7.33, establishing their coprimality via 7.22, building up sequences of least numbers via 8.2, cascading coprimality of extremes via 7.27, and concluding via uniqueness of least sets that A=L and D=O. The citation sets are identical (ai_used = heath_refs = {7.22, 7.27, 7.33, 8.2}), yielding Jaccard 1.0, so the perfect match check assigns category P.

### 8.4
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same two-case structure (E measures K vs. E does not measure K) and the same logical backbone: construct G as LCM(B,C) via 7.34, establish the ratio equalities A:B = H:G and C:D = G:K, extend by one more ratio, then prove minimality by contradiction showing G must measure a number smaller than itself. The AI's two extra citations (7.17 and D7.3) reflect citation-depth differences, not backbone divergence: the AI uses 7.17 directly to establish ratio equalities where Heath uses the combination of VII. Def. 20 and VII. 13, and the AI explicitly cites definition D7.3 for divisibility claims that Heath leaves implicit. Since heath_only is empty and the key intermediate conclusions are identical, this is Case A of Q2, yielding G. The citation sets are not identical (ai_used is a proper superset of heath_refs), so P does not apply.

### 8.5
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs construct L = D*E and establish the same two key intermediate ratio equalities (C:E = A:L and D:F = L:B), but they diverge in how they combine these into the compound ratio conclusion. Heath introduces auxiliary least numbers G, H, K via 8.4 and uses ex aequali (7.14) to establish G:K = A:B before concluding the compound ratio. The AI avoids this auxiliary construction entirely and instead directly applies the definition of compound ratio (D6.5) to the chain A, L, B. Since the heath_only propositions 7.14 and 8.4 are substantive theorems absent from the AI proof and not contained within any proposition the AI cites, Case A of Q2 fails. This yields Case B (different backbone), and Q3 confirms the AI path is logically complete (7.17 and 7.18 correctly establish the ratio equalities, and D6.5 validly concludes the compound ratio), giving classification D.

### 8.6
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: taking least numbers in the same ratio via VII.33, establishing coprimality of extremes via VIII.3, applying ex aequali via VII.14, and transferring the 'not measuring' relation via Def. 20 to reach the conclusion. The AI proof is more explicit, separately handling consecutive and non-consecutive cases and citing definitions (D7.3 for 'part', D7.12 for coprimality, D7.2 for number) that Heath leaves implicit. Since heath_only is empty and ai_only contains only definitions, the AI over-cites at the definitional level while following the identical argumentative path, making this a clear Case A granularity difference.

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (8.6 < 8.7). Both proofs employ an identical proof-by-contradiction strategy: assume A does not measure B, invoke 8.6 to conclude that no number in the continued proportion measures any other, then note the contradiction with the hypothesis that A measures D. The AI and Heath citation sets are identical ({8.6}), yielding Jaccard 1.0, and the key intermediate conclusions match exactly, so the perfect match check assigns category P.

### 8.8
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take the least numbers G, H, K, L in the same ratio as A, C, D, B (7.33), establish that the extremes G, L are prime to one another (8.3), apply ex aequali to get A:B = G:L (7.14), equate G:L = E:F, use the leastness of G, L (7.21) and the measurement property (7.20) to find that G and L measure E and F the same number of times, construct intermediates M and N by applying that same multiplicity to H and K, and conclude that E, M, N, F are in continued proportion. The citation differences are purely at the level of definitional and low-level justification: the AI explicitly cites 7.17 (ratio preservation under multiplication) and D7.15 (definition of multiplication) to justify the ratio equalities in the construction step, whereas Heath invokes D7.20 (definition of proportionality) for the same purpose. These are different ways of articulating the same underlying reasoning at the same logical position, making this a granularity difference rather than a path difference.

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: they take the least numbers F, G in the common ratio, construct four numbers M, N, O, P in continued proportion via VIII.2, show these equal A, C, D, B respectively using VIII.1, then build the proportion chains E:F = F:H = H:A and E:G = G:L = L:B using the definition of multiplication and VII Def 20. The AI's three extra citations (7.33 for explicitly finding the least ratio pair, D7.15 for the definition of multiplication, D7.2 for the definition of unit) all represent over-citation: the AI makes explicit definitional and foundational steps that Heath leaves implicit. Heath's proof contains no citations absent from the AI (heath_only is empty). Since the key intermediate conclusions are identical and only citation depth differs, this is a granularity difference.

### 8.10
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: they construct E=D*D, A=D*E, G=F*F, B=F*G, then H=D*F, K=D*H, L=F*H, and use VII.17 and VII.18 repeatedly to show that all ratios A:K, K:L, L:B equal D:F, establishing A, K, L, B in continued proportion. The AI proof adds explicit citations of D7.15 (definition of multiplication) and D7.2 (definition of number as composed of units), which Heath invokes implicitly without naming. Since the key intermediate conclusions are identical and the only difference is the AI's additional definitional citations, this is a granularity difference (Case A of Q2).

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing E as the product of sides C and D, establishing A:E = C:D via 7.17, E:B = C:D via 7.18, deriving transitivity to get A:E = E:B, and applying D5.9 for the duplicate ratio. The AI adds two over-citations not in Heath: 5.11 (transitivity of equal ratios, which Heath applies without explicit citation) and D7.18 (definition of square number, which Heath invokes implicitly). Since heath_only is empty and both ai_only items are explicit citations for steps present in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs construct the same intermediate numbers E, F, G, H, K from the sides C, D of cubes A, B, and establish the identical chain of proportions (C:D = E:F, C:D = F:G, A:H = C:D, H:K = C:D, K:B = C:D) using VII.17 and VII.18, concluding that A, H, K, B are in continued proportion and that A:B is the triplicate ratio of C:D via V. Def. 10. The key intermediate conclusions are identical in both proofs. The AI over-cites by explicitly invoking 5.11 for transitivity of equal ratios (which Heath applies implicitly in substitution steps) and D7.19 for the definition of cube number (which Heath uses without citation). Since heath_only is empty and the ai_only items are a definition and a transitivity lemma that Heath applies without citation, this is a citation-depth difference with the same backbone, yielding G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing intermediate products between the original numbers and their squares/cubes, establishing that consecutive sequences are in continued proportion in the ratio A:B or B:C, and then applying ex aequali (7.14) to conclude that the squares and cubes are each in continued proportion. The AI proof explicitly cites 7.17 and 7.18 at each step to justify ratio relationships, while Heath uses these same results implicitly under the phrase 'in manner similar to the foregoing, we can prove' without explicit citation. Since heath_only is empty and ai_only contains only 7.17 and 7.18 (propositions that Heath applies but does not cite), this is a citation-depth difference with the same backbone, yielding G.

### 8.14
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct E = C*D, establish that A, E, B are in continued proportion with ratio C:D, then for Part 1 use 8.7 to show A measures E and the ratio relationship to conclude C measures D, and for Part 2 reverse the argument. The sole substantive divergence is citation depth: Heath cites 8.11 as a unit to establish the continued proportion, while the AI re-derives it from 7.17 and 7.18, which are the internal components of Heath's own proof of 8.11 (proof-tree containment test satisfied). The additional ai_only items D7.18 and D7.3 are definitional over-citations. Since the key intermediate conclusions are identical and only citation granularity differs, the classification is G.

### 8.15
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct the same products (E, F, G, H, K), establish that A, H, K, B are in continued proportion with common ratio C:D, then for the first direction apply 8.7 to get A|H from A|B and use the proportion (D7.20) to conclude C|D, and for the second direction reverse the argument through the proportion chain. The only difference is citation depth: Heath cites 8.11 and 8.12 as packaged results to establish the continued proportion, while the AI re-derives the same proportion directly from the more primitive 7.17 and 7.18, which are exactly the propositions used inside Heath's proofs of 8.11 and 8.12. The remaining ai_only items (D7.19, D7.3) are definitions that the AI cites explicitly where Heath leaves them implicit. This satisfies the proof-tree containment test for Case A, yielding G.

### 8.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (8.14 < 8.16). Both proofs handle the two required cases of this biconditional contrapositive proposition identically: each case proceeds by contradiction, assuming the negation and applying 8.14 to derive a contradiction. The AI proof covers case 1 (A not measuring B implies C not measuring D) in Steps 2-4 and case 2 (C not measuring D implies A not measuring B) in Steps 5-7, matching Heath's structure exactly. The citation sets are identical (both cite only 8.14), giving Jaccard similarity of 1.0, and the key intermediate conclusions are the same, so this is a perfect match.

### 8.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same two contrapositive cases: (1) if cube A does not measure cube B then side C does not measure side D, and (2) if side C does not measure side D then cube A does not measure cube B. Both use proof by contradiction invoking 8.15 in each case. The key intermediate conclusions are identical. The only citation difference is that the AI explicitly cites D7.19 (the definition of cube numbers) while Heath does not, which is a minor over-citation of a definition. This is Case A in Q2: same backbone, different citation depth, yielding G.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: they establish similarity via D7.21, apply alternation via 7.13, construct G = D*E, use 7.17 twice to derive the continued proportion A:G :: G:B, and conclude with the duplicate ratio via D5.9. The AI's two extra citations (5.11 and D7.16) are over-citations that make explicit what Heath leaves implicit: 5.11 formalizes the transitivity of equal ratios where Heath simply writes 'therefore also,' and D7.16 cites the definition of plane number where Heath invokes it without citation. Since the key intermediate conclusions are identical and the only differences are in citation depth, this is a granularity difference.

### 8.19
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: the equality of corresponding side ratios (C:F=D:G=E:H), the continuous proportion K,M,L in ratio C:F, the construction of N=E*M and O=H*M yielding A,N,O,B continuously proportional, and the triplicate ratio conclusion. The sole substantive citation difference is that Heath invokes 8.18 to obtain the mean proportional M between similar plane numbers K and L, while the AI constructs M=F*D directly and proves K:M=M:L inline using 7.17 and 7.18. The proof-tree containment test confirms that 8.18's own proof uses VII.17 and VII.13 to establish exactly the same result, so the AI is re-deriving 8.18's internals rather than taking a different path. The ai_only item D7.17 is a definition (minor over-citation). This is Case A of Q2: same backbone, different citation depth.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: A is plane with sides D and F, B is plane with sides E and G, and the sides are proportional, so A and B are similar plane numbers. The substantive citation difference is that the AI uses 7.19 (if products from first-fourth and second-third are equal, the four numbers are proportional) to establish F:G = D:E in one step, whereas Heath derives the same proportionality via 7.17 (twice) and 7.13 (alternation). The proof-tree containment test confirms this is a depth difference: Heath's proof of 7.19 cites 7.17, and Heath's proof of 7.17 cites 7.13, so both heath_only items (7.13, 7.17) lie inside the proof tree of the AI's citation 7.19. The AI additionally cites definitions D7.15, D7.16, D7.20, and D7.21 that Heath invokes implicitly, which is over-citation. Since the backbone is the same and all citation differences reduce to depth, this is Granularity difference (G).

### 8.21
**Category**: Path difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Heath's proof finds the least triple E, F, G via VIII.2, shows their extremes coprime via VIII.3, and then applies VIII.20 to decompose E, G as similar plane numbers with distinct sides H,K and L,M, yielding solids A = N*H*K and B = O*L*M. The AI takes a fundamentally different construction: it finds the least pair H, K in ratio A:C (7.33), builds E = H^2, F = HK, G = K^2 directly, proves coprimality of E, G through 7.22 and 7.27, and decomposes A and B as solids with sides (H, H, N) and (K, K, O). The AI bypasses 8.2, 8.3, and 8.20 entirely, replacing them with a direct square-based construction that avoids the similar-plane-numbers intermediate conclusion. Since these represent genuinely different key intermediate conclusions and the AI's chain from premises to conclusion is logically complete and sound, the classification is D.

### 8.22
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses VIII.20 to establish that A and C are similar plane numbers (since B is one mean proportional between them), then immediately concludes that since A is square, C must also be square. The AI takes a completely different route: it decomposes A as D*D, derives A*C = B*B from the continued proportion via 7.19, applies 8.14 to conclude D divides B, then constructs B = D*E and uses ratio manipulation (7.17, 7.18) and 5.9 to show C = E*E. The key intermediate conclusions differ entirely -- Heath's backbone pivots on similarity of plane numbers, while the AI's pivots on divisibility of sides and direct algebraic reconstruction. The Jaccard similarity is 0.0 with completely disjoint citation sets, confirming a genuine path divergence. The AI proof is logically complete with every step explicitly justified, so Q3(b) holds and the classification is D.

### 8.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: B and C are two mean proportionals between A and D, so by 8.21 A and D are similar solid numbers, and since A is cube D must also be cube. The AI proof explicitly cites definitions D7.19 (cube as product of three equal factors), D7.21 (similar solids have proportional sides), and D7.20 (equal ratios imply equal parts) to unpack the final inference that Heath leaves implicit in the single sentence 'But A is cube; therefore D is also cube.' Since ai_only consists entirely of definitions and heath_only is empty, this is a citation-depth difference with the same key intermediate conclusions, yielding G.

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) one mean proportional falls between the square numbers C and D, (2) since A:B = C:D, one mean proportional also falls between A and B (8.8), (3) since A is square and has a mean proportional to B, B is also square (8.22). The sole difference is the citation for step 1: Heath cites 8.18 (between two similar plane numbers there is one mean proportional) after noting squares are similar plane numbers, while the AI cites 8.11 (between two square numbers there is one mean proportional), which applies directly to squares without going through the more general similar-plane-numbers result. Since the underlying fact is the same at the same logical position and the proofs differ only in which proposition justifies that step, this is Case A of Q2, a citation-depth difference yielding G.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) two mean proportional numbers fall between the cube numbers C and D, (2) by 8.8, two mean proportionals also fall between A and B, and (3) by 8.23, since A, E, F, B are in continued proportion and A is cube, B is cube. The sole difference is the justification for step (1): Heath observes that cubes are similar solid numbers and invokes the general result 8.19, while the AI directly applies the cube-specific result 8.12. Since the underlying fact established at the same logical position is identical in both proofs, this is Case A of Q2, a citation-depth difference yielding G.

### 8.26
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish a mean proportional C between similar plane numbers A, B via 8.18, (2) find the least numbers D, E, F in continued proportion with the same ratio, (3) show D and F are square via 8.2, and (4) conclude A:B = D:F is a ratio of square numbers. The citation differences are purely about depth: Heath cites 7.33 for finding least numbers in a given ratio, while the AI uses 8.2 directly for least numbers in continued proportion; conversely, the AI explicitly cites 7.14 (ex aequali) to establish A:B = D:F, while Heath states that proportion without explicit citation. Since the key intermediate conclusions are identical and only the citation granularity differs, this is Case A of Q2, yielding G.

### 8.27
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) since A, B are similar solid numbers, two mean proportionals C, D fall between them by 8.19; (2) the least numbers in that continued proportion have cube extremes by 8.2; (3) the ratio of those cube extremes equals A:B, so A:B is a cube-to-cube ratio. The AI proof adds explicit citations for 7.14 (ex aequali reasoning that Heath leaves implicit) and D7.19 (definition of cube number), but these are over-citations making implicit steps explicit rather than introducing a different argumentative path. Heath_only is empty, confirming no substantive step is missing from the AI proof. This is Case A of Q2: same backbone, different citation depth.


---

## Book 9 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 8 | 9.9, 9.22, 9.23, 9.25, 9.26, 9.27, 9.28, 9.29 |
| Granularity difference (G) | 26 | 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.10, 9.12, 9.13, 9.14, 9.15, 9.16, 9.17, 9.18, 9.20, 9.21, 9.24, 9.30, 9.31, 9.32, 9.33, 9.34, 9.35, 9.36 |
| Path difference (D) | 2 | 9.11, 9.19 |
| AI proof error (E) | 0 |  |

**Total**: 36 propositions

## Per-Proposition Analysis

### 9.1
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) D = A*A is square, (2) A:B = D:C by VII.17, (3) one mean proportional between A and B by VIII.18, (4) one mean proportional between D and C by VIII.8, (5) D square implies C square by VIII.22. The only difference is that the AI explicitly cites Definition 7.18 to justify that a number multiplied by itself is square, whereas Heath states this without citation. This is a classic over-citation of a definition, placing the proofs in Case A of Q2: same backbone, different citation depth, yielding category G.

### 9.2
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: construct D = A*A, establish A:B = D:C via VII.17, observe that D and C are both square and therefore similar plane numbers, find a mean proportional between D and C via VIII.18, transfer the mean proportional to A and B via VIII.8, and conclude that A and B are similar plane numbers via VIII.20. The only difference is that the AI explicitly cites definitions D7.16 (plane number), D7.18 (square number), and D7.21 (similar plane numbers) to justify steps that Heath leaves implicit. Since heath_only is empty and ai_only contains only definitional citations, this is a straightforward citation-depth difference with the same logical backbone, yielding G.

### 9.3
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: decomposing cube A via its side C to establish the continued proportion unit:C = C:D = D:A, then deriving unit:A = A:B from A multiplying itself, applying VIII.8 to obtain two mean proportionals between A and B, and concluding via VIII.23 that B is cube. The only difference is that the AI explicitly cites definitions D7.15 (multiplication as repeated addition) and D7.19 (cube number definition) at each step, whereas Heath invokes these concepts implicitly without formal citation. Since heath_only is empty and ai_only contains only definitions, this is a clear case of over-citation at the definitional level with no change in the proof's logical structure, yielding a granularity difference.

### 9.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification via the proof-tree containment test. Both proofs share the same backbone: construct D = A*A so D is cube (9.3), establish A:B = D:C (7.17), then conclude C is cube from D being cube and the ratio being cube-to-cube. The sole difference is citation depth at the final step: Heath re-derives the internals of 8.25 inline by showing A,B are similar solid numbers with two mean proportionals between them (8.19), transferring those mean proportionals to D,C (8.8), and concluding via 8.23; the AI instead cites 8.25 directly, which is exactly the proposition whose proof uses 8.19, 8.8, and 8.23. Since all three heath_only items appear inside Heath's proof of 8.25, this is a citation-depth difference under Case A of Q2, yielding G.

### 9.5
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: A multiplied by itself gives cube D (9.3), the ratio A:B equals D:C (7.17), D and C are similar solid numbers so two mean proportionals fall between them (8.19), two mean proportionals therefore fall between A and B (8.8), and since A is cube B must be cube (8.23). The AI proof adds explicit citations to Definitions 7.19 and 7.21 to justify why cube numbers are similar solid numbers, a step Heath states without citing the definitions. Since ai_only contains only definitions and heath_only is empty, and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference under Case A of Q2, yielding G.

### 9.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: The forward dependency gate passes (9.5 precedes 9.6; D7.19 is a definition). Q1 finds no logical defect: the AI correctly establishes C = A^3 is cube by D7.19, then correctly applies 9.5 (if a cube multiplied by a number yields a cube, that number is cube) to conclude A is cube. Q2 applies the proof-tree containment test to the three substantive heath_only propositions (8.19, 8.8, 8.23): all three appear inside Heath's own proof of 9.5, which the AI cites as a single higher-level unit. Heath re-derives the internals of 9.5 inline in his proof of 9.6 (establishing proportions via VII.Def.20, finding mean proportionals via VIII.19/VIII.8, concluding via VIII.23), while the AI packages that entire argument by citing 9.5 directly. The remaining differences (D7.19 vs D7.20) are definitional. Since the containment test passes for all substantive heath_only items, this is Case A -- same logical backbone at different citation depth -- yielding G.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: The forward dependency gate found no issues since all AI citations (D7.13, D7.15, D7.17) are definitions, which are never forward. Q1 confirmed the AI proof is logically complete with no errors: every step is supported by a citation or follows from prior steps. Q2 revealed that both proofs share identical key intermediate conclusions -- decomposing the composite number A into factors D and E via D7.13 and D7.15, then showing that D x E x B = C makes C a solid number. The sole difference is that the AI explicitly cites Definition 7.17 (the definition of a solid number) to justify the final conclusion, while Heath applies the same concept without a formal citation. Since D7.17 is a definition rather than a substantive proposition, this is over-citation at the definitional level, placing this squarely in Case A of Q2: same backbone, different citation depth. The classification is therefore G.

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that A multiplied by itself produces the square B (via VII Def 20), extend squareness along the geometric progression using VIII.22, show that A multiplied by B produces the cube C, and extend cubeness using VIII.23, then combine both results for the seventh term. The AI proof explicitly cites three definitions (D7.15 for multiplication, D7.18 for square, D7.19 for cube) that Heath invokes implicitly without formal citation. Since heath_only is empty and the ai_only items are all definitions providing finer citation granularity for the same reasoning steps, this is Case A of Q2: same backbone, different citation depth.

### 9.9
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Scope correction applied: Proposition 9.9's statement asks only about the square case. Heath's proof includes the cube case as a bonus extension after completing the square case, but the cube case is not part of the proposition statement. Citations 8.23 and 9.3 are excluded as cube-case-only. After this correction, the effective Heath citations for the square case are {8.22, 9.8}, matching the AI citations exactly. Forward-dependency gate: 8.22 (book 8 < 9) and 9.8 (n=8 < 9) are both backward; no forward dependencies. Q1(a): Single-case proposition (square case only). The AI addresses the square case fully; no missing case. Q1(b): The AI proof is logically complete — Step 2 uses 9.8 to establish odd-position numbers are square, Steps 3–4 use 8.22 to cascade the square property through even-position numbers via consecutive triples, and Step 5 generalizes the induction. No E triggers. Q2: Both proofs share the same backbone: (1) odd-position numbers are square by 9.8, (2) even-position numbers are shown square by applying 8.22 to consecutive triples. Case A holds. Perfect match check: AI citations {8.22, 9.8} equal the scope-corrected Heath citations {8.22, 9.8}. Classification: P.

### 9.10
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Scope correction applied: the proposition statement concerns only the square case. Heath's proof includes a cube case extension (using 8.25 and 9.6) that goes beyond the proposition statement; these citations are excluded from comparison. Effective Heath citations for the square case: 8.26, 9.8. Forward dependency gate passes (8.24 in Book 8, 9.8 precedes 9.10, D7.20 is a definition). Q1(a): only the square case is required; the AI addresses it completely. Q1(b): every step is supported by citation or prior steps — 9.8 licenses B being square, D7.20 licenses the proportion inversion, 8.24 licenses the conclusion that A is square from ratio of square to square and B being square. NOT-E. Q2: both proofs share the same backbone for the square case — (1) B is square [9.8], (2) assume C square, (3) establish that A and B have ratio of square to square, (4) conclude A is square (contradiction), (5) C not square, (6) extend to subsequent terms. The citation difference is at step (4): the AI uses D7.20 to invert the proportion and 8.24 directly (ratio of sq:sq + first is square implies second is square), while Heath uses 8.26 converse (ratio of sq:sq implies similar plane numbers, then similar to a square is square). D7.20 is an explicit definition citation left implicit by Heath. Same backbone, different citation depth — G.

### 9.11
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves only that B (the first term after the unit) measures the last term E, using a single application of 7.15 (alternation). The AI proves the fully general case that any earlier term M measures any later term N, by first establishing (like Heath) that B measures each later term Q according to its predecessor P via 7.15, and then extending to arbitrary pairs M, N through an ex aequali argument using 7.14. The ex aequali step is an indispensable key intermediate conclusion in the AI proof that is entirely absent from Heath's proof, making this Case B (different backbone). The AI's generalized path is logically sound (Q3 confirmed), yielding D.

### 9.12
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction assuming prime E does not measure A (the term next to the unit), followed by a descent chain showing E|D implies E|C implies E|B implies E|A, yielding a contradiction. The two heath_only citations (9.8 and D7.14) reflect citation-depth differences, not backbone divergence. Heath cites 9.8 explicitly for the fact that A squared equals B, while the AI derives the same fact from 9.11 and its Porism (since A measures B according to the term in the same position from B as A is from the unit, which is A itself). Heath cites D7.14 (definition of composite numbers) in the final argument step, while the AI proceeds directly from the contradiction to the conclusion, omitting the definitional intermediary. The ai_only set is empty, confirming the AI uses a subset of Heath's citations. Since the key intermediate conclusions are identical and the citation differences are purely matters of depth, this is Case A in Q2, yielding G.

### 9.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same descent argument: assuming a number E not among the proportional numbers measures the greatest term D, they show E is composite and measured by A (via 9.12 and 7.31), introduce F with E*F=D and F not among the proportional numbers (via 9.11), then use proportionality (7.19) to descend through F measuring C, G measuring B, and finally H measuring A, contradicting A being prime. The key intermediate conclusions are identical. The sole heath_only citation, 9.8 (A multiplied by itself makes B), is re-derived inline by the AI from definitions D7.20 and D7.15, which appear inside Heath's own proof of 9.8 — satisfying the proof-tree containment test. All ai_only items are definitions (D7.2, D7.3, D7.11, D7.13, D7.15, D7.20) and the commutativity result 7.16, representing over-citation of foundational material. This is a same-backbone, different-citation-depth case.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume a prime E different from B, C, D measures A, derive E times F = A, apply VII.30 to conclude B, C, D each measure E or F, rule out E because it is prime and distinct, so they measure F, and reach a contradiction since F is less than A. The AI proof cites exactly the same key proposition (7.30) as Heath and adds explicit references to definitions (D7.11 for prime, D7.15 for multiplication, D7.3 for part), a common notion (CN5), and the commutativity of multiplication (7.16), all of which Heath uses implicitly. Since heath_only is empty and all ai_only items are over-citations of definitions and basic results, this is Case A in Q2: same backbone, different citation depth, yielding G.

### 9.15
**Category**: Granularity difference
**Jaccard**: 0.875
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: they take DE, EF as the least numbers with the given ratio via VIII.2, establish A=DE^2, B=DE*EF, C=EF^2, prove DE and EF coprime (VII.22), prove DF coprime to each (VII.28), then demonstrate all three coprimality results (A+B prime to C, B+C prime to A, A+C prime to B) using the same chain of VII.24, VII.25, II.3, and II.4. The AI proof additionally cites VII.33 for finding the least numbers with a given ratio, a construction step that Heath subsumes under VIII.2 alone. Since heath_only is empty and ai_only contains only this construction-level over-citation, the backbones are identical and the difference is purely one of citation depth, placing this squarely in Case A of Q2 as a granularity difference.

### 9.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs follow the same backbone: assume for contradiction that A:B = B:C, invoke 7.21 to establish that A and B are the least numbers in their ratio, then apply 7.20 to conclude that A measures B, and since A measures itself, A measures both A and B, contradicting their being prime to one another. The AI proof adds explicit citations to D7.2 (definition of number, to show A is not a unit) and D7.12 (definition of prime to one another) to spell out the final contradiction step that Heath leaves implicit. Since heath_only is empty and ai_only contains only definitions, this is a clear case of over-citation at the same logical backbone, yielding a granularity difference.

### 9.17
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction through identical key intermediate conclusions: assuming D:E = A:B, applying alternation (7.13) to get A:D = B:E, invoking the primality-implies-least result (7.21), using the least-numbers measuring property (7.20) to show A measures B, then propagating divisibility through the continued proportion to show A measures D, contradicting the premise that A and D are prime to one another. The AI proof cites four additional definitions (D7.3, D7.20, D7.12, D7.2) that Heath leaves implicit, but these are purely citation-depth differences: the underlying logical steps and key conclusions are identical in both proofs. Case A of Q2 holds, yielding G.

### 9.18
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 (Case A) decided the classification. Both proofs establish identical key intermediate conclusions through the same logical backbone: both divide into three cases (A,B prime to one another; A,B not prime and A measures B-squared; A,B not prime and A does not measure B-squared), invoke 9.16 for the prime case, and use 7.19 for the proportionality argument in the remaining cases, with a proof by contradiction for the non-measuring sub-case. The AI proof explicitly cites CN1 (for equality transitivity, e.g., A*D = B*B) and D7.15 (for the definition of multiplication), both of which Heath uses implicitly without citation. Since ai_only contains only a common notion and a definition while heath_only is empty, and the logical backbones are identical, this is a citation-depth difference yielding category G.

### 9.19
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Heath's proof treats four separate cases, with Case 2 (not in continued proportion, extremes prime to one another) proved impossible through a dedicated chain using 7.14 (ex aequali), 7.21 (primes are least), and 7.20 (least numbers measure those with same ratio). The AI proof bypasses this entire argument by providing a unified criterion for all cases except the 9.17 case: form D = B*C and check whether A measures D. The AI's two-branch structure (9.17 case vs. unified A|B*C criterion) constitutes a genuinely different logical backbone from Heath's four-case treatment. The proof-tree containment test confirms these heath_only propositions are not subsumed by any higher-level proposition the AI cites; the AI simply takes a different route. Q3 confirms the AI's path is valid: the A|B*C criterion is correctly proved in both directions using 7.19, with no logical gaps.

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct DE as the least common multiple of the assigned primes, add a unit to obtain EF, then consider two cases. In Case 1 (EF prime), both proofs conclude that EF is a new prime different from the assigned ones. In Case 2 (EF not prime), both proofs show EF is measured by some prime G and then prove by contradiction that G cannot equal any of the assigned primes, since G would then measure the unit. The only differences are in citation depth: the AI cites 7.32 (any number is either prime or measured by some prime) where Heath cites 7.31 (any composite number is measured by some prime), and the proof-tree containment test confirms that 7.31 appears inside Heath's proof of 7.32, so the AI simply cites the higher-level result. The remaining ai_only items (7.36 for finding the LCM, CN5, D7.2, D7.3) are foundational or construction citations that Heath invokes implicitly without explicit reference. This is Case A of Q2: same backbone, different citation depth.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: the sum AE is divisible into two equal parts (has a half part), and therefore AE is even. Heath's proof states this concisely by noting each summand has a half part so the whole does too. The AI proof spells out the same argument in greater detail, explicitly constructing the grouped halves F and G', invoking CN2 (equals added to equals yield equals) to show F = G', and then concluding AE = F + G'. The only citation difference is that the AI explicitly cites CN2 where Heath leaves the inference implicit. Since CN2 is a Common Notion (axiom-level), this is over-citation at the axiom level, a classic granularity difference. The logical backbones are identical, so this is Case A of Q2.

### 9.22
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21 is prior and D7.7 is a definition). Q1 confirmed the AI proof is logically complete: each step is supported by a citation or the hypothesis. Q2 confirmed both proofs share the same key intermediate conclusions -- subtract a unit from each odd number to get even remainders (D7.7), sum the even remainders (9.21), note the units form an even number, and conclude AE is even (9.21). The citation sets are identical (ai_used = heath_refs = {9.21, D7.7}, Jaccard = 1.0), so the perfect match check assigns category P.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21, 9.22, and D7.7 are all prior to 9.23). Q1 confirmed the AI proof is logically complete: each step is properly justified with appropriate citations. Q2 confirmed both proofs share the same key intermediate conclusions -- subtracting a unit from the last odd number to obtain an even remainder, establishing that the sum of the remaining odd numbers is even via 9.22, combining the two even parts via 9.21, and concluding the whole is odd by D7.7. The citation sets are identical (ai_used = heath_refs = {9.21, 9.22, D7.7}), yielding Jaccard 1.0 and classification P.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same chain of key intermediate conclusions: AB has a half part (by D7.6), BC has a half part (by D7.6), the remainder AC also has a half part, and therefore AC is even. The AI proof takes a more formally detailed route by invoking Definition 7.3 to define what a 'part' is and Proposition 7.7 to formally justify that if D is the half of AB and E is the half of BC, then D minus E is the half of AC. Heath treats this final step as immediately obvious from the definition of even numbers. Since the key conclusions are identical and the extra AI citations (7.7, D7.3) provide additional depth of justification rather than a different logical route, this is a granularity difference.

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow the same logical backbone with identical citations. Both subtract a unit from the odd number BC to obtain the even number DB (by D7.7), then subtract the even DB from the even AB to conclude AD is even (by 9.24), and finally observe that the remainder CA differs from the even AD by exactly one unit, making CA odd (by D7.7). The citation sets are identical (9.24, D7.7), yielding a Jaccard similarity of 1.0. Since Q1 found no logical defect, Q2 confirmed the same key intermediate conclusions, and the citation sets match exactly, the perfect-match check assigns category P.

### 9.26
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.24 is prior and D7.7 is a definition). Both proofs follow an identical logical chain: subtract a unit BD from the odd number AB to get even remainder AD (by Definition VII.7), observe that CD is also even by the same reasoning, then conclude that CA is even because an even number subtracted from an even number leaves an even remainder (by IX.24). The citation sets are identical (9.24 and D7.7), yielding Jaccard 1.0. Since the key intermediate conclusions and citations match exactly, this is a perfect match.

### 9.27
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 9.27 follow the same logical backbone: subtract the unit AD from odd number AB to obtain even DB (by Def. 7.7), then since both DB and BC are even, their difference CD is even (by 9.24), and finally CA equals CD plus the unit DA, making CA odd (by Def. 7.7). The citation sets are identical ({9.24, D7.7} = {9.24, D7.7}, Jaccard = 1.0), and the key intermediate conclusions match exactly, so the perfect-match check at the end of the protocol assigns category P.

### 9.28
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21 is prior and D7.15 is a definition). Both proofs follow the identical logical chain: by the definition of multiplication (D7.15), C is made up of as many copies of B as there are units in A; since B is even, C is a sum of even numbers; by 9.21, the sum of even numbers is even, so C is even. The citation sets are exactly equal (ai_used = heath_refs = {9.21, D7.15}), with Jaccard similarity 1.0 and empty ai_only and heath_only sets. Since no category was assigned by Q1-Q3 and the citation sets match exactly, the classification is P (Perfect match).

### 9.29
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate found no issues (9.23 is prior and D7.15 is a definition). Both proofs follow the same logical backbone: applying VII. Def. 15 to express the product C as a sum of A copies of B, noting each summand is odd and their count is odd, then invoking IX. 23 to conclude C is odd. The AI proof is logically complete with no defects under Q1. Since the citation sets are exactly equal ({9.23, D7.15} = {9.23, D7.15}) and the key intermediate conclusions match, the classification is P (Perfect match).

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they set up A times C equals B, prove by contradiction that C cannot be odd (which would make B odd, contradicting the hypothesis that B is even), conclude C is even, and derive that A measures the half of B. The sole substantive divergence is the citation used in the contradiction step: Heath cites 9.23 directly (a sum of odd numbers taken an odd number of times is odd), while the AI cites 9.29 (the product of two odd numbers is odd). The proof-tree containment test confirms that 9.23 appears inside Heath's own proof of 9.29, so the AI is citing 9.29 as a unit while Heath re-derives its internals inline. The remaining ai_only items (D7.15, D7.6, D7.7) are definitions reflecting over-citation at a finer granularity. This is Case A of Q2: same backbone, different citation depth.

### 9.31
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as G. Both proofs follow the same backbone: assume by contradiction that A (odd, prime to B) is not prime to C = 2B, derive that some D measures both A and C, show D must be odd, apply 9.30 to conclude D measures half of C which is B, and reach a contradiction since D then measures both A and B which are coprime. The AI proof adds explicit definitional citations (D7.5, D7.6, D7.7, D7.12) and proposition 9.21 to justify steps that Heath states without citation, such as the step that D is odd because it divides the odd number A. Since heath_only is empty, the AI covers every step Heath uses. The difference is purely citation depth — the AI over-cites definitions and a supporting lemma — placing this firmly in Case A of Q2.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: establish that the doubled numbers are all even, set out a unit to form a continued proportion with A (the dyad) as the prime after the unit, apply 9.13 to show D is measured only by A, B, and C, and conclude that since all divisors are even, D is even-times even only. The AI proof cites nine additional items beyond Heath's two references (9.13, D7.8), but these are almost entirely definitions (D7.2, D7.3, D7.6, D7.7, D7.9, D7.11, D7.15, D7.20) that Heath invokes implicitly, plus one theorem (7.16) used in an explicit contradiction argument showing D is not even-times odd, which Heath derives more directly from D7.8. Since heath_only is empty and the ai_only items are all foundational definitions or a theorem used to spell out what Heath states concisely, this is Case A: same backbone, different citation depth.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) show A is even-times odd because its odd half measures it an even number of times, and (2) show A is not even-times even by contradiction, since assuming so forces the half to be even, contradicting its oddness. The AI proof is substantially more detailed, explicitly citing definitions (D7.6, D7.7, D7.15), a common notion (CN5), commutativity of multiplication (7.16), and a result on sums of even numbers (9.21) at steps that Heath leaves implicit. Heath cites only D7.8 and D7.9, and all of these appear in the AI's citation set as well (heath_only is empty). The six ai_only items are all foundational results and definitions used to flesh out sub-steps of the same argument, representing over-citation and greater explicitness rather than a different proof path. Case A of Q2 holds, yielding G.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Both proofs share the same two-part backbone: (1) A is even-times even because its half is not odd, justified by D7.8; (2) A is even-times odd because repeated bisection must terminate at an odd number (not a dyad, by contradiction with the hypothesis), and that odd number measures A according to an even number. The AI proof follows this identical logical path but makes explicit every definitional and auxiliary step that Heath leaves implicit, citing definitions D7.2, D7.3, D7.6, D7.7, D7.9, D7.15, common notion CN5, and propositions 7.16 (commutativity) and 9.29 (odd times odd is odd) to justify details Heath treats as obvious. Since heath_only is empty and all ai_only items are over-citations providing deeper justification for the same backbone conclusions, this is Case A of Q2: same key intermediate conclusions at different citation depth.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing FK=BC and FL=D within EF, establishing KH=GC by remainder equality, applying separando (7.11) and alternando (7.13) to obtain the chain of equal ratios EL:FL = LK:FK = KH:FH, then combining antecedents and consequents via 7.12 to reach the final proportion GC:A = EH:(D+BC+A). The AI proof adds explicit citations to common notions (CN1, CN3) and definitions (D7.3, D7.4, D7.20) that Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are foundational axioms rather than substantive propositions, this is a clear Case A in Q2: same key intermediate conclusions with different citation depth.

### 9.36
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: establishing E, HK, L, M, FG in continuous double proportion, applying 9.35 to show OG equals the sum E+HK+L+M, demonstrating FG equals the sum of all its parts, showing each part measures FG, and proving by contradiction that no other number measures FG. The only difference is the sub-argument mechanism for the uniqueness step: the AI uses 7.30 (a prime dividing a product divides one factor) to split into two cases, while Heath re-derives the internals of 7.30 inline using 7.29 (prime not measuring a number is coprime to it), 7.21 (coprime numbers are least in ratio), and 7.20 (least numbers measure proportionals the same number of times). The proof-tree containment test confirms that all three heath_only propositions (7.29, 7.21, 7.20) appear inside Heath's own proof of 7.30, so the AI is citing 7.30 as a packaged unit while Heath unpacks it. The remaining ai_only items are definitions (D7.2, D7.3, D7.11, D7.15), common notions (CN1, CN2, CN5), and basic results (7.13, 7.16, 7.17) that represent explicit over-citation of steps Heath leaves implicit. This is a citation-depth difference, not a path difference.


---

## Book 10 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 110 | 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10, 10.11, 10.12, 10.13, 10.14, 10.15, 10.16, 10.17, 10.18, 10.19, 10.20, 10.21, 10.22, 10.23, 10.24, 10.25, 10.26, 10.27, 10.28, 10.30, 10.31, 10.32, 10.33, 10.34, 10.35, 10.36, 10.37, 10.38, 10.40, 10.41, 10.42, 10.43, 10.44, 10.45, 10.46, 10.47, 10.49, 10.50, 10.51, 10.52, 10.53, 10.54, 10.55, 10.56, 10.57, 10.58, 10.59, 10.60, 10.61, 10.62, 10.63, 10.64, 10.65, 10.66, 10.67, 10.68, 10.69, 10.70, 10.71, 10.72, 10.73, 10.74, 10.75, 10.76, 10.77, 10.78, 10.79, 10.80, 10.81, 10.82, 10.83, 10.84, 10.85, 10.86, 10.87, 10.88, 10.89, 10.90, 10.92, 10.93, 10.94, 10.95, 10.96, 10.97, 10.98, 10.99, 10.100, 10.101, 10.102, 10.103, 10.104, 10.105, 10.106, 10.107, 10.108, 10.109, 10.110, 10.111, 10.112, 10.114, 10.115 |
| Path difference (D) | 5 | 10.29, 10.39, 10.48, 10.91, 10.113 |
| AI proof error (E) | 0 |  |

**Total**: 115 propositions

## Per-Proposition Analysis

### 10.1
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: invoke the Archimedean property (D5.4) to obtain a multiple DE of C exceeding AB, divide DE into n parts each equal to C, perform n-1 successive subtractions of more-than-half from AB, and compare the remainders at each stage to show the final remainder is less than C. The AI proof is strictly more detailed, explicitly proving auxiliary lemmas (halves of unequals, remainder bounds after subtracting more or less than half) that Heath leaves implicit, citing Common Notions CN2, CN3, and CN5 in those lemma proofs. Since heath_only is empty and ai_only contains only Common Notions used in the AI's deeper elaboration of the same argument, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction: assume AB and CD are commensurable measured by E, show E measures every remainder in the anthyphairetic subtraction process, derive a remainder less than E that E still measures, and reach a contradiction. The backbone is identical. The difference is purely one of citation depth: Heath's proof cites nothing explicitly and simply asserts the process eventually yields a remainder less than E, while the AI proof explicitly invokes Proposition 10.1 (after showing each subtraction removes more than half), and also cites definitions D10.1.1, D5.1, D5.2 and Common Notion CN5 that Heath leaves implicit. Since heath_refs is empty and ai_only consists entirely of over-citations (one substantive predecessor plus definitions and a common notion), this is Case A of Q2: same key intermediate conclusions at different citation depth, yielding G.

### 10.3
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same two-case structure: Case 1 where AB measures CD and is trivially the GCM, and Case 2 where the anthyphairesis (Euclidean algorithm) is applied, terminating by 10.2 because the magnitudes are commensurable. The key intermediate conclusions are identical in both proofs: AF measures CE at termination, AF measures FB, AF measures AB, AF measures ED, AF measures CD, and the contradiction argument showing no magnitude greater than AF can measure both AB and CD. The AI proof explicitly cites CN5 (the whole is greater than the part), D10.1.1 (definition of commensurable), and D5.1 (definition of part) to justify steps that Heath treats as implicit, such as why a measure of AB cannot exceed AB and why the commensurability hypothesis applies. Since heath_only is empty and all ai_only items are foundational definitions and common notions rather than substantive propositions, this is a citation-depth difference (Case A), yielding G.

### 10.4
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: find D = GCM(A,B) via 10.3, split into two cases (D measures C or not), and in the second case establish that C and D are commensurable, find E = GCM(C,D), prove E measures A, B, C, and prove E is the greatest by contradiction. The only citation differences are the AI's explicit references to definitions D10.1.1 (commensurability), D5.1 (part), and D5.2 (multiple), which Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are definitions, this is a straightforward case of over-citation at the same backbone, yielding Granularity difference (G).

### 10.5
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: given commensurable magnitudes A and B, they construct a common measure C and numbers D, E counting how many times C measures A and B respectively, establish C:A = unit:D (by Def. 7.20), invert to A:C = D:unit (by 5.7), establish C:B = unit:E similarly, and conclude A:B = D:E by ex aequali (5.22). The key intermediate conclusions are identical in both proofs. The AI proof adds four definitional citations (D10.1.1 for commensurable, D5.1 for part, D7.2 for number, D7.3 for unit-as-part) that Heath invokes implicitly without explicit citation. Since ai_only contains only definitions and heath_only is empty, this is a citation-depth difference with the same backbone, yielding G.

### 10.6
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: divide A into D equal parts to get C, form F from E copies of C, establish A:C = D:unit and C:F = unit:E, apply ex aequali to get A:F = D:E, equate with the hypothesis A:B = D:E to conclude B = F, then note C measures both A and B. The only structural difference is that Heath obtains A:C = D:unit by first establishing C:A = unit:D via VII.Def.20 and then inverting via V.7, whereas the AI applies VII.Def.20 directly to obtain A:C = D:unit without needing inversion. The key intermediate conclusion (A:C = D:unit) appears at the same logical position in both proofs. The ai_only citations are all definitions (D5.1, D5.2, D7.2, D7.3, D10.1.1) representing over-citation of implicit definitional steps, and heath_only contains only 5.7 which the AI legitimately avoids. This is Case A of Q2: same backbone, different citation depth.

### 10.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction that assumes A:B equals a ratio of numbers, applies 10.6 to conclude A and B would be commensurable, and derives a contradiction with the hypothesis of incommensurability. The only difference is that the AI explicitly cites D10.1.1 (the definition of incommensurable magnitudes) to unpack the meaning of 'incommensurable,' while Heath leaves this definition implicit. Since ai_only contains only a definition and heath_only is empty, this is a citation-depth difference with the same backbone, yielding G. The citation sets are not identical (AI adds D10.1.1), so P is ruled out.

### 10.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the same reductio ad absurdum backbone: assume A and B are commensurable, apply 10.5 to derive that they have a ratio of number to number, note the contradiction with the hypothesis, and conclude incommensurability. The AI proof explicitly cites Definition D10.1.1 (the definition of commensurable magnitudes) at the assumption and conclusion steps, while Heath leaves this implicit. Since D10.1.1 is a definition rather than a substantive proposition, and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference under Case A of Q2, yielding G.

### 10.9
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) commensurable in length implies A:B = number:number by X.5, which implies sq(A):sq(B) = square:square; (2) the converse, establishing A:B = number:number from the square ratio, hence commensurable by X.6; and (3-4) the incommensurable cases as contrapositives. The difference is citation depth. In the forward direction, Heath cites VI.20 (duplicate ratio for similar figures) and VIII.11 (mean proportional between square numbers) as complete units, while the AI re-derives their content from lower-level propositions: 7.17 and 7.18 appear inside VIII.11's proof, and 6.1 and 5.22 appear inside VI.20's proof, passing the proof-tree containment test. In the converse direction, Heath reverses the duplicate ratio via VI.20, while the AI constructs an auxiliary line H and uses 6.22 (proportional similar figures imply proportional sides) to achieve the same logical step. The remaining ai_only items are definitions (D1.22, D10.1.1, D2.1, D6.1, D7.18), a postulate (P4), and connective propositions (5.11), all representing over-citation. Despite the low Jaccard (0.125), the backbone is the same with the AI working at a finer granularity.

### 10.10
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) choosing numbers B, C not in square-to-square ratio, (2) establishing sq(A):sq(D) = B:C, (3) concluding A is commensurable in square but incommensurable in length with D via 10.9, (4) constructing E as a mean proportional and deriving A:D = sq(A):sq(E), and (5) concluding sq(A) is incommensurable with sq(E) so A is incommensurable in square with E. The sole heath_only citation, 10.11, passes the proof-tree containment test: Heath's proof of 10.11 internally uses 10.7 and 10.8, which the AI cites directly instead of invoking 10.11 as a unit. The remaining ai_only items are definitions (D7.11, D7.15, D7.18, D10.1.2), a common notion (CN5), and construction or ratio lemmas (6.13, 6.20, 5.11, 8.24) that represent explicit over-citation of sub-steps Heath leaves implicit. Since the logical backbones match and the citation differences reflect depth rather than direction, Case A of Q2 holds, yielding G.

### 10.11
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs share the same two-case structure and identical key intermediate conclusions: in case 1, A:B being a number ratio (10.5) transfers via the proportion to C:D, yielding commensurability (10.6); in case 2, A:B not being a number ratio (10.7) transfers to C:D, yielding incommensurability (10.8). The AI's sole extra citation, 5.11 (transitivity of equal ratios), makes explicit the step Heath treats as immediate from the proportion hypothesis. In case 2 the AI uses reductio ad absurdum where Heath infers directly, but the backbone conclusion is the same. Since the key intermediate conclusions match and only citation depth differs, this is a granularity difference.

### 10.12
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that A:C and C:B are ratios of numbers (10.5), construct numbers H, K, L in continued proportion matching these ratios (8.4), chain the ratios via transitivity of equal ratios (5.11), apply ex aequali to obtain A:B as a ratio of numbers (5.22), and conclude commensurability (10.6). The AI adds one extra citation, 7.33, which explicitly reduces the ratios to least terms before applying 8.4. Heath does not cite this step but implicitly relies on the same idea. Since the key intermediate conclusions are identical and the only difference is the AI's additional citation depth for an auxiliary construction step, this is a granularity difference (G).

### 10.13
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: a proof by contradiction that assumes B is commensurable with C, applies 10.12 (transitivity of commensurability) to conclude A is commensurable with C, notes the contradiction with the hypothesis that A is incommensurable with C, and concludes B must be incommensurable with C. The only citation difference is that the AI explicitly cites D10.1.1 (the definition of commensurable and incommensurable magnitudes) when explaining why the contradiction is impossible, whereas Heath leaves this definitional point implicit. Since heath_only is empty and ai_only contains only a definition, this is a clear case of over-citation at the definition level with no backbone divergence, yielding Granularity difference (G).

### 10.14
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: the proportion A:B = C:D yields sq(A):sq(B) = sq(C):sq(D) via VI.22, separando gives sq(E):sq(B) = sq(F):sq(D) via V.17, then VI.22 recovers E:B = F:D, the inverse and ex aequali (V.22) produce A:E = C:F, and X.11 transfers commensurability. The AI proof explicitly constructs F via a semicircle (citing 1.10, P3, 4.1, 3.31, 1.47, P1) and adds basic citations (5.14 for C>D, 5.7 for the inverse step, CN5) that Heath leaves implicit. Since heath_only is empty and all ai_only items are construction propositions, postulates, common notions, or elementary proportion results, this is Case A: same backbone with the AI citing at finer granularity.

### 10.15
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish the same biconditional through identical key intermediate conclusions: in Part 1, a common measure D of AB and BC also measures the whole AC; in Part 2, a common measure D of AC and AB also measures the remainder BC. The AI proof makes the underlying arithmetic explicit by introducing multiples (D5.2) and citing Common Notions (CN2 for addition of equals, CN3 for subtraction of equals, CN5 for the whole being greater than the part) where Heath leaves these steps implicit. Since heath_only is empty and ai_only consists entirely of Common Notions and a Definition, the proofs share the same logical backbone at different levels of citation depth, satisfying Case A of Q2. The citation sets differ (Jaccard 0.200) only because the AI over-cites foundational axioms, not because it follows a different path.

### 10.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decides this classification. Both proofs establish the same key intermediate conclusions through the same reductio structure: in Part 1, both derive that AB and BC would be commensurable (contradicting the hypothesis of incommensurability), and in Part 2, both derive that AC and AB would be commensurable (again contradicting the hypothesis). The sole difference is citation depth: Heath re-derives the core reasoning of 10.15 inline (that a common measure of the whole and one part also measures the remainder), while the AI cites 10.15 directly as a packaged result. Since the logical backbone is identical and the only divergence is that the AI cites at a higher level of abstraction, this is a granularity difference (G).

### 10.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: they set up the same construction (bisect BC at E, make EF equal to DE), derive the core identity sq(A) + sq(DF) = sq(BC) via II.5, and then chain commensurability relations through X.15 and X.12 for both directions of the biconditional. The sole heath_only citation, 10.6, is replaced by the AI with D10.1.1 (the definition of commensurability): Heath invokes the proposition that magnitudes in a number-to-number ratio are commensurable, while the AI appeals directly to the definition since DC measures BF+DC (being its double). All ai_only items are construction propositions (1.10, 1.3), an algebraic identity made explicit (2.4), common notions (CN1-CN5), or the definition (D10.1.1), reflecting over-citation rather than a different logical path. Since the key intermediate conclusions are identical and only the citation depth differs, this is a granularity difference.

### 10.18
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish that sq(BC) > sq(A) by sq(FD) via the bisection construction, then derive the incommensurability of BC and FD through the chain BD incomm. DC -> BC incomm. DC -> DC comm. BF+DC -> BC incomm. BF+DC -> BC incomm. FD, for both the forward and converse directions. The key difference is citation depth. Heath cites 10.17 as a shortcut ('with the same construction as before, we can prove similarly'), while the AI re-derives 10.17's construction inline using the underlying propositions (1.10, 1.3, 2.4, 2.5, common notions). The proof-tree containment test confirms these ai_only items appear inside Heath's proof of 10.17. Similarly, Heath cites 10.6 to establish DC is commensurable with BF+DC, while the AI reaches the same conclusion directly from definition D10.1.1 (since BF = DC, the sum is 2*DC, which DC measures). All key intermediate conclusions match; only the depth of justification differs.

### 10.19
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct square AD on AB, establish that AD is rational, show BD is commensurable in length with BC (since AB = BD), apply 6.1 to get the proportion BD:BC = DA:AC, invoke 10.11 to conclude DA is commensurable with AC, and then conclude AC is rational. The AI proof is substantially more explicit, citing 8 additional items (1.46 for square construction, 10.12 for an explicit transitivity step, and six definitions D1.22, D10.1.1, D10.1.2, D10.1.3, D2.1, D6.4) that Heath leaves implicit or compressed under a single Def 4 citation. Since heath_only is empty and the ai_only items consist of definitions, a construction proposition, and one proposition (10.12) making an implicit transitivity step explicit, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 10.20
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a square on the rational line, establish that the square is rational, show commensurability between the square and the given rational area, apply VI.1 (6.1) to obtain a proportion between the areas and the base segments, transfer commensurability via X.11 (10.11), and conclude that the breadth is rational and commensurable in length. The AI proof is a strict superset of Heath's citations (heath_only is empty), adding construction propositions (1.14, 1.46), definitions (D1.22, D2.1, D10.1.1-D10.1.3), and intermediate results Heath uses implicitly (10.6, 10.9 for commensurable-squares reasoning, 10.12 for transitivity of commensurability). Since the key intermediate conclusions are identical and the citation differences reflect only the level of explicit detail, this is a granularity difference.

### 10.21
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct square AD on AB (which is rational), show DB is incommensurable in length with BC, establish the proportionality DB:BC :: AD:AC via 6.1, conclude AD is incommensurable with AC via 10.11, and therefore AC is irrational. The AI proof adds extensive over-citations: construction propositions (1.14 for collinearity of DBC, 1.46 for constructing the square, 2.14 for constructing a square equal to the rectangle), numerous definitions (D1.22, D10.1.1, D10.1.2, D10.1.3, D2.1, D6.4), and one additional substantive proposition (10.13, transitivity of incommensurability through commensurability) which provides a more explicit logical bridge for the step Heath accomplishes directly via the definition of irrational (D10.1.4). Since heath_only is empty and all ai_only items represent deeper citation of steps already present in both proofs, this is Case A: same backbone, different citation depth.

### 10.22
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs follow an identical backbone: establishing that the square on a medial line equals a rectangle contained by rationals commensurable in square only (10.21), applying reciprocal proportionality (6.14), deducing proportional squares (6.22), concluding CD is rational via commensurability of squares (10.11, Def 10.4), then proving CD incommensurable in length with CB through the incommensurability chain (Lemma/6.1, 10.11, 10.13). The heath_only set is empty, meaning the AI cites every proposition Heath does. The ai_only set consists entirely of over-citations: construction propositions (1.44, 1.45), a transitivity lemma (10.12) that Heath applies implicitly, the area-ratio result 6.1 used in place of Heath's unnamed Lemma (which derives from 6.1), and foundational items Heath leaves implicit (CN1, P4, definitions D2.1, D10.1.1-3). Same key intermediate conclusions at different citation depth yields G.

### 10.23
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: applying rectangles equal to the squares on A and B to a rational line CD, showing the breadth ED is rational and incommensurable with CD (10.22), deducing the commensurability of CE and CF from that of the squares on A and B, using the proportion ED:DF = CE:CF (6.1) to obtain commensurability of ED and DF (10.11), concluding DF is rational (Def. 3) and incommensurable with CD (10.13), and finally invoking 10.21 to establish B is medial. The AI's eight extra citations (1.45, 1.46 for constructions; D10.1.1, D10.1.2, D2.1 for definitions; 10.6, 10.9 for the commensurability-of-squares sub-argument; 10.12 for transitivity) all supply deeper justification for steps Heath leaves implicit, with heath_only empty. This is a classic citation-depth difference with the same backbone, yielding G.

### 10.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct the square AD on AB, establish that AD is medial, show that DB (equal to AB) is commensurable in length with BC, use VI.1 and X.11 to conclude DA is commensurable with AC, then apply X.23 to conclude AC is medial. The AI proof adds three citations not in Heath (1.46 for constructing the square, 10.21 for the definition of medial straight line, 5.7 for the ratio substitution when replacing DB with AB), all of which are over-citations providing explicit justification for steps Heath takes as obvious. Heath cites nothing the AI omits (heath_only is empty). This is a clear Case A in Q2: same backbone, different citation depth.

### 10.25
**Category**: Granularity difference
**Jaccard**: 0.389
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: FH and KL are rational and incommensurable with FG (via 10.22), FH is commensurable in length with KL (via 6.1 and 10.11), the rectangle FH.KL is rational (via 10.19), the proportionality chain FH:HK=HK:KL yields FH.KL=HK^2 so HK is rational (via 6.17), and the two-case conclusion (HK commensurable or incommensurable with FG) gives AC either rational or medial (via 10.19 and 10.21). The AI cites a strict superset of Heath's references, adding construction propositions (1.14, 1.34, 1.44, 1.45, 1.46), definitions (D10.1.1-D10.1.4), and two additional theorem citations (5.7, 10.12) that Heath leaves implicit. Heath_only is empty. The logical backbone is identical with the AI providing greater citation depth, giving Case A of Q2 and classification G.

### 10.26
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction structure: assume medial area AB exceeds medial area AC by rational area DB, apply these to a rational line EF, show EH and EG are rational and incommensurable with EF (10.22), GH is rational and commensurable with EF (10.20), then derive through a chain of incommensurability results (10.13, 10.11, 10.6, 10.16) that the square on EH is irrational, contradicting EH being rational. The key intermediate conclusions are identical in both proofs. heath_only is empty, confirming that every citation Heath makes is also made by the AI. The ai_only set consists entirely of over-citations: construction propositions (1.44, 1.45), definitions (10.21, D10.1.3), common notions (CN3, CN5), and intermediate commensurability results (10.12, 10.15, 2.1, 6.1) that Heath invokes implicitly. This is Case A of Q2: same backbone, different citation depth.

### 10.27
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) sq(C) = rect(A,B) via the mean proportional, (2) C is medial from X.21, (3) C and D are commensurable in square only via X.11, (4) D is medial via X.23, (5) rect(C,D) = sq(B) via alternation and transitivity of ratios, and (6) rect(C,D) is rational because sq(B) is rational. The AI proof cites a strict superset of Heath's references (heath_only is empty), adding 10.10 for the explicit construction of commensurable-in-square-only rational lines, 6.22 for the proportionality of squares, 5.11 for ratio transitivity, and definitions D10.1.1-D10.1.4. These are all over-citations that unpack steps Heath treats as implicit. The backbone is the same; only the citation depth differs, yielding Granularity difference (G).

### 10.28
**Category**: Granularity difference
**Jaccard**: 0.615
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: construct D as mean proportional between A and B, and E with B:C = D:E; then establish (1) D is medial because sq(D) = rect(A,B) which is medial, (2) D and E are commensurable in square only via X.11, (3) E is medial via X.23, and (4) rect(D,E) = rect(A,C) which is medial. The AI proof reaches every key intermediate conclusion in the same order as Heath. The ai_only citations (5.7, 5.11, 6.22, CN1, D10.1.2) are all over-citations making explicit what Heath leaves implicit: 5.7 for inverting a ratio, 5.11 for chaining equal ratios, 6.22 for deriving proportional squares from proportional lines, plus a common notion and a definition. Heath_only is empty, confirming that no substantive step is missing. This is Case A of Q2: same backbone, different citation depth.

### 10.29
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: The classification hinges on Q2 (Case B) and Q3. Heath's proof constructs a semicircle AFB on AB and relies on III.31 (angle in semicircle is right) to obtain the right triangle, setting up the ratio DC:CE equal to sq(BA):sq(AF) directly via X.6, then using convertendo (V.19) to derive the BF relationship. The AI proof instead erects a perpendicular BF at B using I.11, starts with the ratio CE:DE equal to sq(AB):sq(BF), and builds up to the AF ratio via componendo (V.18) and then convertendo (V.19), reversing the derivation order. The proof-tree containment test fails for the substantive heath_only citation III.31: it is an independent proposition from I.11, not contained within it, confirming these are independent geometric routes rather than a citation-depth difference. The AI's path is logically complete under Q3, with every step properly justified, yielding classification D. The AI itself explicitly notes the alternative construction: erecting the perpendicular at B and taking AF as hypotenuse rather than fitting a chord into a semicircle.

### 10.30
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: constructing a semicircle on rational line AB, using 10.6 to establish the ratio DC:CE = sq(BA):sq(AF), proving BA and AF are rational commensurable in square only, then applying convertendo (5.19) with 3.31 and 1.47 to obtain CD:DE = sq(AB):sq(BF), and concluding via 10.9 that AB is incommensurable in length with BF. The AI proof is substantially more detailed, explicitly citing construction steps (1.10, 4.1), definitions (D1.18, D10.1.2, D10.1.3, D7.18), postulates (P1, P3), and auxiliary propositions (5.14, 5.7, 8.24) that Heath leaves implicit or abbreviates with phrases like 'in a similar manner to the preceding.' Heath's citation set is a proper subset of the AI's (heath_only is empty), confirming that the difference is purely one of citation depth, not logical path.

### 10.31
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct rational straight lines A, B commensurable in square only via 10.29, define C with sq(C) = rect(A,B) and show C is medial via 10.21, define D with rect(C,D) = sq(B) and show rect(C,D) is rational, establish the proportion A:B = C:D, conclude C and D are commensurable in square only via 10.11, show D is medial via 10.23, and transfer the square-difference commensurability property via 10.14. The AI's additional citations (1.44, 2.14, 5.7, 5.11, 5.14, 6.1, 6.22, D10.1.2, D10.1.3, D10.1.4) are all lower-level construction, proportion, and definition references that Heath uses implicitly. The sole heath_only citation (10.30) appears only in Heath's closing 'similarly' remark about the incommensurable variant, which is an addendum beyond the proposition's stated requirement. This is Case A of Q2: same backbone with different citation depth, yielding G.

### 10.32
**Category**: Granularity difference
**Jaccard**: 0.438
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing three rational lines A, B, C commensurable in square only (via 10.29), forming D as medial through sq(D)=rect(A,B), defining E through rect(D,E)=rect(B,C), establishing A:C=D:E, deducing D and E are commensurable in square only, showing E is medial, proving sq(D)>sq(E) by a commensurable amount, and concluding rect(D,E) is medial. The ai_only citations (10.10, 5.11, 5.16, 6.12, 6.13, 6.22) are all construction propositions or ratio-manipulation lemmas that Heath invokes implicitly, representing over-citation at a finer granularity. The heath_only citations (10.30, 6.4, 6.8) come from the appended second-case dispatch and the separate LEMMA about right triangles, neither of which belongs to the main proof backbone. Since both proofs reach the same key intermediate conclusions through the same logical path, differing only in explicit citation depth, this is a granularity difference.

### 10.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same geometric construction (setting out rational lines AB, BC via X.30, bisecting BC, applying VI.28 area application, constructing a semicircle with perpendicular to obtain AF and FB) and establish the same key intermediate conclusions in the same order: AE incommensurable with EB, AF and FB incommensurable in square, sum of squares on AF and FB rational via I.47, FE equals BD so BC is double FE, rectangle AB,BC commensurable with rectangle AB,EF, rectangle AB,BC medial so rectangle AB,EF medial, and rectangle AB,EF equals rectangle AF,FB so rectangle AF,FB medial. The AI proof is substantially more granular, explicitly citing 15 additional propositions that Heath leaves implicit or compresses: construction steps (1.10, 1.11, P1, P3), the detailed similarity arguments underlying the semicircle construction (3.31, 6.8, 6.4, 6.17, 6.16, 6.1), commensurability sub-steps (10.11, 10.6), and foundational items (CN1, D10.1.2, D10.1.4). Since heath_only is empty, the AI covers all of Heath's citations and adds finer-grained justifications for the same logical backbone, making this a clear Case A granularity difference.

### 10.34
**Category**: Granularity difference
**Jaccard**: 0.318
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) AF incommensurable with FB via area application and 10.18, (2) sq(AD) incommensurable with sq(DB) via 10.11, (3) sum of squares on AD and DB is medial since sq(AB) is medial via 3.31 and 1.47, and (4) rect(AD,DB) is rational via the equality rect(AD,DB) = rect(AB,FD) and rationality of rect(AB,BC). The heath_only set is empty, meaning every proposition Heath cites also appears in the AI's citation set. The AI's 15 additional citations are all over-citations adding granularity: construction propositions (1.10, 1.11, P1, P3), sub-steps of implicit similar-triangle arguments Heath performs without citing (6.1, 6.4, 6.8, 6.17), intermediate Book 10 results (10.12, 10.21, 10.30), the area relation 1.41 used where Heath invokes an unnamed Lemma for the same conclusion, and definitions and axioms (CN1, D10.1.2, D10.1.4). Since the backbone is identical and the differences are purely in citation depth, this is a granularity difference.

### 10.35
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same four-part backbone: (1) AD and DB are incommensurable in square, (2) the sum of squares on AD and DB is medial, (3) the rectangle AD,DB is medial, and (4) the sum of squares is incommensurable with the rectangle. Heath's proof establishes these conclusions concisely, citing only 1.47, 3.31, 10.11, 10.13, 10.18, and 10.32. The AI proof reaches the same conclusions through the same geometric construction but explicitly cites every intermediate step, including construction propositions (1.10, 1.11, P1, P3), a definition (D10.1.2), proportionality and similar-triangle results (6.1, 6.8, 6.16, 6.17, 6.28), and commensurability results (10.6, 10.23) that Heath invokes without explicit citation. The empty heath_only set confirms that the AI covers all of Heath's references and adds finer-grained citations. This is Case A of Q2: same backbone, different citation depth.

### 10.36
**Category**: Granularity difference
**Jaccard**: 0.583
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: rect(AB,BC) is incommensurable with sq(BC) via X.11, twice that rectangle is commensurable with the rectangle via X.6, the sum of squares is commensurable with sq(BC) via X.15, twice the rectangle is incommensurable with the sum of squares via X.13, sq(AC) is incommensurable with the sum of squares via II.4 and X.16, and the sum of squares is rational so sq(AC) is irrational. The AI proof adds five over-citations not in Heath (6.1 for the proportion step, 10.12 for commensurability transitivity in showing the sum of squares is rational, and definitions D10.1.1, D10.1.2, D10.1.3), while heath_only is empty. These additional citations make explicit what Heath leaves implicit, representing a citation-depth difference rather than a path divergence.

### 10.37
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: establishing that AB and BC are incommensurable in length, showing that the sum of the squares on AB and BC is incommensurable with twice the rectangle AB, BC, applying II.4 to express the square on AC, and concluding that AC is irrational via X. Def. 4. The key divergence is that Heath references 'cf. X. 36, ll. 9-20' to compress the incommensurability argument by analogy with the previous proposition, while the AI re-derives the full chain from scratch using propositions 10.11, 10.6, 10.15, and 10.13. The proof-tree containment test confirms this: heath_only contains only 10.36, and Heath's own proof of 10.36 uses exactly the substantive propositions in ai_only (10.11, 10.13, 10.15, 10.6). The remaining ai_only items (6.1, D10.1.1, D10.1.2) are over-citations of constructions and definitions. This is a citation-depth difference, not a different proof path.

### 10.38
**Category**: Granularity difference
**Jaccard**: 0.647
**Analysis**: Q2 decided the classification. Both proofs share an identical backbone: apply sq(AC) to rational DE via I.44, decompose via II.4 into EH (squares on AB, BC) and HF (twice rect AB,BC), show both areas are medial, derive DH and HG as rational and incommensurable with DE via X.22, prove sq(AB) incommensurable with rect(AB,BC) via X.11, conclude EH incommensurable with HF via X.13/X.15/X.6, hence DH incommensurable with HG via VI.1/X.11, making DG a binomial irrational via X.36, so DF is irrational and AC is irrational. The AI cites six additional items (10.12, 10.21, 10.23, CN3, D10.1.2, D10.1.3) that Heath leaves implicit: 10.21 justifies that squares on medial lines are medial, 10.23 justifies that an area commensurable with a medial area is medial, 10.12 provides transitivity of commensurability in showing DH and HG are commensurable in square, CN3 licenses the subtraction step, and D10.1.2/D10.1.3 cite definitions of commensurability in square and rationality. Heath cites nothing the AI omits (heath_only is empty). These are all over-citations making explicit what Heath treats as understood, confirming same backbone with different citation depth.

### 10.39
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Heath's proof establishes that twice rect(AB,BC) is medial using 10.6 and 10.23 (a straight line commensurable with a medial straight line is medial), then infers incommensurability with the rational sum of squares from the medial-vs-rational distinction. The AI proof takes a genuinely different path: it first establishes that rect(AB,BC) is incommensurable with R using 10.21 (the rectangle of rational lines commensurable in square only is irrational), then uses transitivity of incommensurability (10.13) repeatedly to show twice rect is incommensurable with R, and hence incommensurable with the rational sum of squares. The key intermediate conclusion 'twice rect(AB,BC) is medial' in Heath is replaced by 'twice rect(AB,BC) is incommensurable with R' in the AI, which is a substantively different intermediate fact obtained through a different chain of reasoning. Since the AI's different path is logically complete and valid under Q3, the classification is D.

### 10.40
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: given that the sum of squares on AB, BC is medial and twice the rectangle AB, BC is rational, both establish that these two quantities are incommensurable, then apply 10.16 to conclude the square on AC is incommensurable with twice the rectangle, and finally conclude AC is irrational via D10.1.4. The heath_only citation 10.34 is merely a parenthetical existence reference for lines satisfying the hypothesis, not a substantive proof step. The ai_only citations (2.4, 10.6, 10.12, 10.13, 10.21) are all sub-steps that Heath compresses into immediate inferences: the AI explicitly invokes 2.4 for the algebraic expansion, 10.6 and 10.12 to establish that twice the rectangle is rational, 10.21 to characterize the medial area, and 10.13 for transitivity of incommensurability. Since the key intermediate conclusions are identical and the citation differences reflect only depth of justification, this is a granularity difference.

### 10.41
**Category**: Granularity difference
**Jaccard**: 0.316
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: construct rectangles DF and GH on rational line DE equal to the sum of squares and twice the rectangle respectively, show DH equals the square on AC by 2.4, establish DG and GK are each rational and incommensurable in length with DE via 10.22, show DG is incommensurable with GK via 6.1 and 10.11, conclude DK is binomial by 10.36, then conclude DH and AC are irrational. The AI proof cites 12 additional references (construction props 1.34/1.45, common notions CN1/CN2, definitions D10.1.2/D10.1.3, and intermediate results 10.6/10.12/10.13/10.20/10.21/10.23) that spell out sub-steps Heath leaves implicit, while Heath's sole unique citation 10.35 merely references the conditions on the lines which the AI states directly from the proposition. Since the key intermediate conclusions are the same and the citation differences reflect depth of justification rather than a different proof path, this is a granularity difference.

### 10.42
**Category**: Granularity difference
**Jaccard**: 0.188
**Analysis**: Q2 decided this classification. Both proofs follow the same proof-by-contradiction structure for showing a binomial line has a unique division point: assume two divisions at C and D, show AC is not the same as DB, use II.4 to relate sums of squares and doubled rectangles, establish the sums of squares are rational and the doubled rectangles are medial, then derive a contradiction via X.26 (a medial cannot exceed a medial by a rational area). The key intermediate conclusions are identical in both proofs. The AI's 13 additional citations (ai_only) consist of definitions (D10.1.1-4), common notions (CN1, CN3), and subsidiary propositions (10.12, 10.15, 10.23, 10.26, 5.9, 5.17, 6.16) that make explicit the reasoning Heath performs implicitly or tersely. With heath_only empty and the same backbone confirmed by reading both texts, this is a granularity difference (Case A).

### 10.43
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: they establish that the rectangles AC,CB and AD,DB are rational (by the definition of a first bimedial), derive that the sums of squares on each pair differ by a rational area, show each sum of squares is medial, and reach contradiction via 10.26 (a medial area cannot exceed a medial area by a rational area). The AI proof provides far more geometric detail -- introducing bisection at E (1.10), using II.5 to relate rectangles and squares, and explicitly justifying rationality through 10.12, 10.15, and 10.6 -- while Heath states the same argument concisely, noting simply that both rectangles are rational so their difference is rational, and citing only X.26. The bisection and II.5 steps are constructive sub-steps that establish the same key fact (the rational difference) by a more elaborate route, not a different backbone. The recorded heath_refs is empty (yielding Jaccard 0.0), but the logical backbone is identical. Q2 Case A applies: same key intermediate conclusions at different citation depth.

### 10.44
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification as G (Case A: same backbone, different citation depth). Both proofs follow the same core strategy of reducing the uniqueness of division of a second bimedial straight line to the uniqueness of division of a binomial straight line (10.42). They establish identical key intermediate conclusions: applying rectangles to a rational line EF, showing EH and HN are rational and commensurable in square only, and concluding that EN is a binomial divided at both H and M. The divergence is only in the endgame: Heath shows EH is not equal to MN via a direct inequality argument and implicitly invokes 10.42 for the contradiction, while the AI explicitly cites 10.42 to force H=M and then carries back to AB through 2.5 and 2.7 to show AC=DB. The heath_only set is empty, meaning every Heath citation appears in the AI set; the 18 ai_only items consist of construction propositions (1.10, 1.3, 1.45), common notions (CN1-5), definitions (D10.1.1-3), and substantive propositions (10.12, 10.15, 10.21, 10.23) that Heath uses in the text but omits from the reference list, plus 10.42, 2.5, and 2.7 used in the AI's extended endgame. This is a clear case of over-citation and finer citation granularity with the same underlying logical backbone.

### 10.45
**Category**: Granularity difference
**Jaccard**: 0.133
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assume AB is a major straight line divided at two distinct points C and D, derive the algebraic identity showing the difference of the sums of squares equals the difference of the doubled rectangles, conclude the difference is rational (both sums of squares are rational), note both doubled rectangles are medial, and reach contradiction via 10.26 (a medial area cannot exceed a medial area by a rational area). The AI proof is far more granular, explicitly citing construction steps (1.10 for bisection), algebraic identities (2.4, 2.5), common notions (CN1, CN2, CN3), definitions (D10.1.1, D10.1.2, D10.1.4), and intermediate Book 10 propositions (10.6, 10.12, 10.15, 10.23) that Heath leaves implicit. The heath_only set is empty, confirming the AI covers all of Heath's reasoning. The additional AI steps (bisection at E, detailed EC/ED inequality) represent elaboration of the same argument, not a different logical path. This is Case A of Q2: same backbone, different citation depth.

### 10.46
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Classification is decided at Q2, Case A (same backbone, different citation depth). Both proofs use proof by contradiction: they assume the side of a rational plus a medial area can be divided at two points C and D satisfying the 10.40 conditions, derive that the difference between the sums of squares equals the difference between the twice-rectangles, show this difference is rational, and reach a contradiction via 10.26 since both sums of squares are medial. The AI proof adds substantially more explicit detail: it proves the divisions are genuinely different, bisects AB at E (1.10), derives the algebraic identity through 2.5 and 2.4 rather than stating it directly, and explicitly proves the excess is rational using commensurability transitivity (10.12, 10.15) and the definition of rationality (D10.1.4). All ai_only items (1.10, 10.12, 10.15, 2.4, 2.5, CN1, CN3, CN5, D10.1.2, D10.1.4) are construction propositions, algebraic identities, commensurability results, common notions, and definitions that represent finer-grained justification of steps Heath compresses. heath_only is empty, confirming all Heath citations are subsumed. The key intermediate conclusions are identical in both proofs, so this is a granularity difference.

### 10.47
**Category**: Granularity difference
**Jaccard**: 0.261
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume two divisions of AB, apply areas to a rational line EF, show EH and HN are each rational and incommensurable in length with EF (10.22), show EH incommensurable with HN (6.1, 10.11), conclude EN is a binomial divided at H and similarly at M (10.36), and reach contradiction via 10.42. The AI proof adds a more constructive elaboration in Steps 8-13 (using 2.5, 2.9, 1.10 to show H=M forces C=D), but this is additional detail within the same logical framework, not a different backbone. heath_only is empty, confirming that every Heath citation appears in the AI set, while ai_only consists of construction propositions (1.10, 1.36, 1.44, 1.45), common notions (CN1-CN5), definitions (D10.1.1-D10.1.3), and intermediate propositions (10.12, 10.13, 10.23, 10.41) that make explicit what Heath leaves implicit. Case A of Q2 holds: same backbone, different citation depth.

### 10.48
**Category**: Path difference
**Jaccard**: 0.188
**Analysis**: Q2 decides the classification. Both proofs reach the same final conclusions about EG being a first binomial, but via genuinely different backbones. Heath constructs EF and FG directly from number ratios: he selects numbers AC, CB with specific ratio properties (Lemma after X.28), uses X.6 to set up the ratio of squares, and applies convertendo (V.19) to establish the square-difference property. The AI instead leverages 10.29 to obtain an abstract pair of rational lines A, B already possessing the required properties (commensurable in square only, square-difference commensurable with the greater), then transfers those properties to EF, FG via a fourth proportional (6.12), using 10.11, 6.22, and 10.14 as transfer lemmas. While the heath_only items (10.28, 5.19) do appear inside Heath's proof of 10.29 (satisfying containment in that direction), the ai_only items 10.11, 10.14, 6.12, 6.22, and 5.14 are substantive propositions representing a proportionality-transfer mechanism entirely absent from Heath's direct-construction approach, so Case A fails. The AI's different path is logically complete under Q3: every step is properly justified, and the chain from 10.29 through the fourth proportional to the final classification as first binomial is sound.

### 10.49
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions: setting up numbers with AB:BC a square-to-square ratio but AB:AC not, constructing EF commensurable in length with D (rational), making sq(EF):sq(FG) = CA:AB so FG is rational, establishing EF incommensurable in length with FG, concluding EG is binomial via 10.36, using the inverse ratio and convertendo (5.19) to show sq(FG) exceeds sq(FE) by the square on a line commensurable with FG, and classifying EG as a second binomial. The AI proof is far more granular: it picks explicit numbers (9, 4, 5) instead of citing a lemma, uses the semicircle method (3.31, 1.47, 4.1) to construct H rather than defining it implicitly, and cites definitions (D10.1.2, D10.1.3, D10.2.2, D5.5, D7.18), postulates (P1, P2), and sub-step propositions (5.7, 10.12, 8.24) that Heath leaves tacit. Since heath_only is empty and all ai_only items are over-citations of sub-steps, definitions, or postulates, this is Case A of Q2: same backbone, different citation depth.

### 10.50
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing FG and GH as rational lines commensurable in square only to form a binomial FH (10.36), then using ex aequali (5.22) to show E is incommensurable in length with GH, and convertendo (5.19) to show the square on FG exceeds the square on GH by the square on a line commensurable with FG, with neither term commensurable with E. The AI proof adds an explicit geometric construction via a semicircle to find the line K (citing 1.10, 3.31, 4.1, 1.47) where Heath simply posits its existence, and explicitly cites definitions (D10.1.2, D10.1.3, D10.2.3), postulates (P1, P2, P3), common notions (CN5), and elementary propositions (1.3, 5.14) that Heath leaves implicit. The heath_only set is empty, confirming Heath cites nothing the AI omits. This is Case A of Q2: same backbone with the AI providing greater citation depth.

### 10.51
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions in the same logical order: EF is rational (commensurable with D), FG is rational, EF and FG are incommensurable in length, EG is binomial, the convertendo step yields AB:BC = EF^2:H^2, EF is incommensurable in length with H, and EG is a fourth binomial. The AI proof cites 11 references versus Heath's 3, but heath_only is empty -- every Heath citation appears in the AI set. The 8 ai_only items (10.12, 10.13, 10.36, 5.14, CN5, D10.1.2, D10.1.3, D10.2.4) are all definitions, common notions, construction lemmas, and supporting propositions that Heath uses without explicit citation. This is a clear case of same backbone with different citation depth, yielding G.

### 10.52
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: constructing FG so that CA:AB equals sq(EF):sq(FG), showing EF and FG are rational commensurable in square only, concluding EG is binomial by 10.36, showing sq(FG) exceeds sq(FE), applying convertendo to obtain AB:BC equals sq(FG):sq(H), proving FG incommensurable in length with H, and concluding EG is a fifth binomial. The heath_only set is empty, meaning the AI cites every proposition Heath cites. The 13 ai_only items are all construction propositions (1.3, 2.14, 6.13), proportion properties (5.7, 5.11), transitivity of commensurability (10.12), definitions (D10.1.2, D10.1.3, D10.2.4, D10.2.5, D5.5), a common notion (CN5), and a postulate (P2), all of which Heath uses implicitly. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.53
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing FG and GH via proportions (10.6) from numbers with non-square-ratio conditions, showing FG and GH are rational and commensurable in square only to establish FH as binomial (10.36), using ex aequali (5.22) to show E incommensurable with GH, and using convertendo (5.19) to show the square on FG exceeds the square on GH by a square incommensurable with FG, yielding a sixth binomial. The AI proof adds explicit construction citations (1.3, P2), algebraic lemmas for the square decomposition (2.5, 2.14), a ratio comparison step (5.14), a common notion (CN5), and definitions (D10.1.2, D10.1.3, D10.2.4, D10.2.6) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations making implicit steps explicit, this is Case A of Q2: same backbone, different citation depth.

### 10.54
**Category**: Granularity difference
**Jaccard**: 0.379
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same backbone of key intermediate conclusions: (1) the properties of the first binomial AD divided at E, (2) AG commensurable with GE via 10.17, (3) EL as mean proportional between AH and GK, (4) sq(MO) = AC so MO is the side, (5) AH and GK rational and commensurable, (6) MN incommensurable in length with NO via the chain from AE incommensurable with ED, and (7) MN and NO rational commensurable in square only so MO is binomial by 10.36. The heath_only set is empty, meaning every citation Heath uses also appears in the AI set. The 18 ai_only items are all over-citations at finer granularity: construction steps (1.10, 1.31, 1.36), algebraic identities (2.1, 2.4), proportion-theory lemmas (5.7, 5.9, 5.11), application of areas (6.12, 6.28), additional commensurability results (10.6, 10.21), common notions (CN1, CN2), and definitions (D2.1, D10.1.2, D10.1.3, D10.1.4). The AI's slight constructive difference of using a fourth proportional (6.12) instead of Heath's Lemma is a sub-step variation, not a backbone divergence. This is Case A: same backbone, different citation depth.

### 10.55
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: dividing the second binomial AD at E, applying the area-deficiency construction to get AG commensurable with GE (10.17), constructing squares SN and NQ equal to the sub-rectangles AH and GK, showing MO is the side of area AC, then proving MN and NO are medial and commensurable in square only with a rational rectangle, concluding MO is a first bimedial by 10.37. The heath_only set is empty, meaning the AI cites every proposition Heath uses. The ai_only set of 22 items consists entirely of construction propositions (1.10, 1.31, 1.34, 1.36, 2.14, 6.12, 6.17, 6.28), algebraic identities (2.4, 5.11, 5.7, 5.9), commensurability lemmas (10.6, 10.9, 10.36), definitions (D10.1.1-D10.1.4, D10.2.1), and common notions (CN1, CN2) that Heath invokes implicitly or without citation. This is a clear case of the AI providing a more granular citation trail for the same proof structure.

### 10.56
**Category**: Granularity difference
**Jaccard**: 0.138
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing the third binomial properties of AD, constructing MO as the 'side' of area AC, showing MN and NO are medial straight lines commensurable in square only, and then proving MO is specifically a second bimedial by showing EF is incommensurable with EK (via 10.13), that FE and EK are rational commensurable in square only so the rectangle EL (= MN.NO) is medial (via 10.21), and concluding with 10.38. The sole difference is citation depth: Heath compresses the construction and all intermediate steps into 'in manner similar to the foregoing' (a back-reference to 10.54/10.55), while the AI spells out every step explicitly, citing 25 additional propositions that are all construction steps (1.10, 1.3, 1.31, 1.34, 1.36), algebraic and proportion lemmas (2.4, 2.14, 5.11, 5.9, 6.1, 6.12, 6.17, 6.28), commensurability results (10.11, 10.12, 10.15, 10.17, 10.36), definitions, common notions, and a postulate. heath_only is empty, confirming the AI subsumes all of Heath's citations. This is Case A of Q2: same backbone, different citation depth.

### 10.57
**Category**: Granularity difference
**Jaccard**: 0.276
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: setting up the fourth binomial properties, bisecting DE at F, applying a rectangle AG,GE equal to sq(EF) to AE, showing AG incommensurable with GE via 10.18, constructing parallels, proving the relevant segments are incommensurable in square, establishing the sum of squares is rational (via 10.19), proving the rectangle is medial (via 10.13 and 10.21), and concluding the side is major via 10.39. The AI proof is far more explicit in its citations (29 vs 8), but every Heath citation appears in the AI set (heath_only is empty), and all 21 ai_only items are over-citations of construction steps (1.10, 1.3, 1.31, 1.36), algebraic identities (2.4, 2.14), proportion lemmas (5.7, 5.9, 5.11, 6.22, 6.28), commensurability lemmas (10.6, 10.12, 10.36), definitions (D10.1.1-D10.1.4, D2.1), a common notion (CN2), and a postulate (P2). This is a clear Case A under Q2: same backbone, different citation depth.

### 10.58
**Category**: Granularity difference
**Jaccard**: 0.281
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) MN, NO are incommensurable in square (via 10.18, 6.1, 10.11), (2) the sum of squares on MN, NO is medial (via 10.13, 10.21), (3) the rectangle MN, NO is rational (via 10.19), and (4) MO is the side of a rational plus a medial area (by 10.40). Heath abbreviates the construction as 'let the same construction be made as before shown,' while the AI explicitly constructs the figure in Steps 1-8 with detailed citations to 1.10, 1.3, 1.31, 1.36, 1.46, 2.4, 2.14, 5.7-5.13, 6.17, 6.28, and proves EL = MR by a proportion argument. The AI also cites definitions (D10.1.1-D10.1.4, D10.2.4, D10.2.5), common notions (CN1, CN2), and 10.36 for properties of binomials. Since heath_only is empty and all ai_only items are construction steps, proportion lemmas, definitions, or axioms, this is a clear case of over-citation at the same logical backbone -- Case A of Q2, yielding G.

### 10.59
**Category**: Granularity difference
**Jaccard**: 0.227
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish MO as the 'side' of AC, show MN and NO are incommensurable in square, prove the sum of the squares on MN and NO (AK) is medial, prove the rectangle MN-NO (EL) is medial, establish AK incommensurable with EL, and conclude via 10.41 that MO is the side of the sum of two medial areas. The AI proof is far more explicit about the underlying construction and intermediate steps that Heath abbreviates with 'Let the same construction be made as before shown,' explicitly citing construction propositions (1.10, 1.31, 1.36, 6.28), definitions (D10.1.1, D10.1.2, D10.1.3, D10.2.6), algebraic identities (2.4, 2.14, 5.11, 5.9), proportion results (6.22), and intermediate Book 10 results (10.18, 10.23, 10.36). Since heath_only is empty, every Heath citation appears in the AI set, and the 17 additional AI citations are all supporting detail at finer granularity. This is Case A: same backbone, different citation depth.

### 10.60
**Category**: Granularity difference
**Jaccard**: 0.393
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: setting up rectangles DH, KL, MF on the rational line DE; showing DL is rational so DM is rational and commensurable in length with DE; showing MF is medial so MG is rational and incommensurable in length with DE; concluding DM and MG are rational commensurable in square only so DG is binomial; establishing rect(DK,KM) = sq(MN) via the mean proportional relationship; showing DK is commensurable with KM; proving DL > MF hence DM > MG; applying 10.17 to conclude the square on DM exceeds the square on MG by a commensurable amount; and finally classifying DG as a first binomial. The citation differences are purely depth-related: the AI explicitly cites 16 additional items (construction propositions 1.10, 1.3, 1.31, 1.36; algebraic identities 2.4, 2.7; proportion results 5.11, 5.7; definitions D10.1.1-D10.1.4; common notions CN3, CN5; and transitivity lemmas 10.12, 10.23) that Heath leaves implicit, while Heath cites the Lemma after X.53 for the mean proportional fact that the AI re-derives inline from 6.1 and 5.11. Same backbone, different citation granularity.

### 10.61
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same logical order: DL is medial so DM is rational and incommensurable with DE; MF is rational so MG is rational and commensurable with DE; DM and MG are rational commensurable in square only so DG is binomial; DL exceeds MF so DM exceeds MG; DK is commensurable with KM; the rectangle DK by KM equals the square on MN; the square on DM exceeds the square on MG by the square on a line commensurable with DM; and MG is commensurable with DE so DG is a second binomial. The backbones are the same. heath_only is empty, meaning every proposition Heath cites the AI also cites. The 20 ai_only items are all lower-level results that Heath invokes implicitly: construction propositions (1.3, 1.10, 1.31, 1.34, 1.36, 1.44, 1.45), algebraic identities (2.4, 2.7), proportion lemmas (5.7, 5.11, 6.17), a commensurability transfer (10.12), common notions (CN2, CN3, CN5), and definitions (D10.1.1-D10.1.4). This is a clear case of the AI over-citing at finer granularity while following the same proof path, yielding G.

### 10.62
**Category**: Granularity difference
**Jaccard**: 0.385
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they construct a parallelogram equal to the square on the second bimedial, decompose it into parts corresponding to the squares on the medial segments and twice their rectangle, show that the resulting breadth segments are rational and incommensurable in length with the rational line DE, show these segments are incommensurable with each other (hence the breadth is binomial), and then show the square on the greater exceeds the square on the lesser by a line commensurable with the greater, with neither term commensurable with DE, yielding a third binomial. The AI proof is substantially more detailed (13 explicit steps vs Heath's condensed narrative), citing 16 additional propositions that Heath either assumes implicitly or handles with phrases like 'in manner similar to the foregoing.' Crucially, heath_only is empty, meaning the AI cites every proposition Heath cites plus many more construction, algebraic, and auxiliary results. This is Case A of Q2: same key intermediate conclusions, different citation depth.

### 10.63
**Category**: Granularity difference
**Jaccard**: 0.346
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing DL as rational to obtain DM rational and commensurable with DE (10.20), MF as medial to obtain MG rational and incommensurable with DE (10.22), DM incommensurable with MG so DG is binomial (10.13, 10.36), DM greater than MG, DK incommensurable with KM, DK times KM equal to the square on MN, and finally applying 10.18 to conclude DG is a fourth binomial. The heath_only set is empty, meaning the AI cites every proposition Heath cites. The ai_only items consist entirely of construction steps (1.10, 1.3, 1.31, 1.36, 1.44), common notions (CN2, CN3, CN5), definitions (D10.1.1, D10.1.2, D10.1.3), and intermediate algebraic or proportion results (10.12, 10.23, 2.4, 2.7, 5.11, 6.17) that Heath abbreviates with phrases like 'same construction as before' and 'in manner similar to the foregoing.' This is a clear Case A in Q2: same backbone, different citation depth.

### 10.64
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: the properties of AC and CB from 10.40, DL being medial so DM is rational and incommensurable with DE (10.22), MF being rational so MG is rational and commensurable with DE (10.20), DM incommensurable with MG (10.13) yielding DG binomial (10.36), the rectangle DK times KM equaling the square on MN with DK incommensurable with KM, and the square on DM exceeding the square on MG by the square on a line incommensurable with DM (10.18), concluding DG is a fifth binomial. The AI proof spells out every sub-step that Heath condenses, including the construction details (1.3, 1.10, 1.31, 1.36, 1.44), the algebraic identity work (2.4, 2.7), ratio theory (5.11, 6.1, 6.17), intermediate commensurability results (10.6, 10.11, 10.12), common notions (CN2, CN3, CN5), and definitions (D10.1.2, D10.1.3, D10.1.4, D10.2.4, D10.2.5). Heath's proof abbreviates the rectangle-equals-square and incommensurability steps as provable similarly, while the AI derives them explicitly. Since heath_only is empty and all ai_only items are lower-level citations supporting the same backbone conclusions, this is a citation-depth difference, not a path difference.

### 10.65
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they invoke 10.41 to establish the properties of AC and CB, show that DL and MF are each medial, derive that DM and MG are each rational and incommensurable in length with DE via 10.22, prove DL incommensurable with MF and hence DM incommensurable with MG via 6.1 and 10.11, conclude DG is binomial by 10.36, then show the square on DM exceeds the square on MG by the square on a line incommensurable with DM, with neither term commensurable with DE, yielding the sixth binomial. The heath_only set is empty, meaning every citation Heath uses also appears in the AI proof. The 20 ai_only items are all construction steps (1.10, 1.31, 1.34, 1.36, 1.44), algebraic identities (2.4, 2.7), proportionality results (5.11, 6.17), commensurability lemmas (10.12, 10.13, 10.18, 10.23), common notions (CN3, CN5), and definitions (D10.1.1, D10.1.2, D10.1.3, D10.2.4, D10.2.6) that Heath leaves implicit. This is a classic over-citation pattern with identical backbone, producing a granularity difference.

### 10.66
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: dividing the binomial AB at E, setting up the proportion AB:CD = AE:CF via 6.12, deriving the remainder relation via 5.19, establishing commensurability of corresponding terms via 10.11, proving CF and FD rational and commensurable in square only, concluding CD is binomial via 10.36, and then exhaustively handling all six sub-cases for order preservation. The AI proof adds five extra citations (10.6, 10.9, 5.14, D10.1.2, D10.1.3) that Heath does not use: 10.9 and 10.6 appear in the AI's more detailed derivation that CF and FD are rational (where Heath simply asserts this follows from commensurability with rational lines), 5.14 is cited for ordering comparisons Heath leaves implicit, and D10.1.2/D10.1.3 are definitions of rationality that Heath does not explicitly cite. Since heath_only is empty and the AI's extra citations all support the same intermediate conclusions at finer granularity, this is Case A of Q2: same backbone, different citation depth.

### 10.67
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: dividing CD at F proportionally to AB at E, showing CF and FD are medial and commensurable in square only (hence CD is bimedial), then showing rect(AE,EB) is commensurable with rect(CF,FD) to conclude same order via two cases (first bimedial if rational rectangle, second bimedial if medial rectangle). The differences are purely in which proportion and construction lemmas are invoked. Heath uses V.19 (separando) and V.11 for ratio establishment and V.16 (alternando) for the rectangle commensurability step, while the AI uses 6.10 for similar cutting, 5.12/5.16 for proportion manipulation, 6.1 and 10.12 for rectangle commensurability via an intermediate rectangle, and 6.22 for similar figures on proportional lines. The AI also explicitly cites definitions D10.1.2 and D10.1.4. All key intermediate conclusions are the same in both proofs; only the citation depth and specific proportion tools differ, making this a granularity difference.

### 10.68
**Category**: Granularity difference
**Jaccard**: 0.263
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) the proportions AB:CD = AE:CF = EB:FD, (2) AE commensurable with CF and EB commensurable with FD, (3) CF and FD incommensurable in square, (4) the sum of squares on CF, FD is rational, (5) the rectangle CF*FD is medial, and (6) CD is major by 10.39. The AI proof uses a different construction method (fourth proportional via 6.12 and remainder proportion via 5.19 instead of Heath's implicit similar-division construction) and different supporting lemmas (6.22 instead of 6.20 for the ratio of squares, 5.12 instead of 5.18 for componendo), but these substitutions achieve the same intermediate results at each logical step. The large ai_only set (12 items) consists of construction propositions (1.3, 6.12), definitions (D10.1.2, D10.1.4), and granular sub-lemmas (10.6, 10.9, 10.12, 5.14, 6.1) that Heath leaves implicit. The heath_only items (5.18, 6.20) are replaced by equivalent alternative lemmas in the AI proof. Since the backbone is identical and only the citation depth differs, this is a granularity difference.

### 10.69
**Category**: Granularity difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: AB is divided at E into lines incommensurable in square with medial sum of squares and rational rectangle (by 10.40); CD is cut at F in the same ratio; CF and FD are shown to be incommensurable in square; the sum of squares on CF, FD is shown medial; the rectangle CF, FD is shown rational; therefore CD is the side of a rational plus a medial area. Heath's proof is extremely compressed, summarizing the entire argument as 'Let the same construction be made as before. We can then prove similarly that...' and citing only 10.40. The AI proof spells out every step of this 'prove similarly' argument in full detail, explicitly citing the proportion theory (5.11, 5.12, 5.16), construction (6.10), area and ratio results (6.1, 6.22), commensurability lemmas (10.6, 10.9, 10.11, 10.12, 10.23), and definitions (D10.1.2, D10.1.4). All 13 ai_only items are sub-steps of the argument Heath abbreviates, making this a clear Case A (same backbone, different citation depth) under Q2.

### 10.70
**Category**: Granularity difference
**Jaccard**: 0.071
**Analysis**: Q2 Case A decides the classification. Both proofs follow the same logical backbone: decompose AB as the side of the sum of two medial areas using 10.41 to obtain AE and EB with three properties (incommensurable in square, sum of squares medial, rectangle medial, sum of squares incommensurable with rectangle), construct CF and FD as corresponding parts of CD via a fourth proportional, and then verify that CF and FD satisfy all three conditions required by the definition. Heath compresses the argument with 'let the same construction be made as before' and 'we can then prove similarly,' while the AI proof spells out every intermediate step with explicit citations to Book 5 ratio propositions (5.11, 5.12, 5.14, 5.16, 5.19), Book 6 proportion propositions (6.1, 6.12, 6.22), and Book 10 commensurability results (10.6, 10.9, 10.11, 10.23). The empty heath_only set confirms that the AI covers all of Heath's citations and simply adds lower-level detail, making this a citation-depth difference rather than a path divergence.

### 10.71
**Category**: Granularity difference
**Jaccard**: 0.481
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: EH is rational and commensurable in length with EF (via 10.20), HK is rational and incommensurable in length with EF (via 10.22), EH is incommensurable in length with HK (via 6.1 and 10.11), EH and HK are rational commensurable in square only so EK is a binomial (via 10.36), and then four subcases classified by binomial order definitions yield the four irrational line types (binomial via 10.54, first bimedial via 10.55, major via 10.57, side of rational plus medial via 10.58). The heath_only set is empty, meaning every citation Heath uses also appears in the AI proof. The AI adds 14 extra citations consisting of construction propositions (1.13, 1.34, 1.44, 1.45), definitions (D10.1.1-D10.1.4, D5.5), common notions (CN2), postulates (P2), and intermediate propositions (10.12, 10.13, 10.21) that Heath leaves implicit. This is a clear case of over-citation with the same logical backbone, placing it squarely in Case A of Q2 as a granularity difference.

### 10.72
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: applying the two medial areas to a rational line to obtain rational breadths EH and HK each incommensurable with EF (10.22), showing EH incommensurable with HK via 6.1 and 10.11, concluding EK is binomial (10.36), then splitting into two cases based on commensurability of the excess square to yield either a third binomial mapped to a second bimedial (10.56) or a sixth binomial mapped to the side of the sum of two medial areas (10.59). The AI cites a strict superset of Heath's references, with heath_only empty and ai_only consisting entirely of construction propositions (1.34, 1.44), a transitivity lemma (10.12), a common notion (CN2), and definitions (D10.1.1-D10.1.4), all of which spell out steps Heath leaves implicit. Since the key intermediate conclusions are the same and the citation differences reflect only depth of explicitness, this is a granularity difference.

### 10.73
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: sq(AB) incommensurable with rect(AB,BC), sq(AB)+sq(BC) commensurable with sq(AB), 2*rect(AB,BC) commensurable with rect(AB,BC), the II.7 identity, sq(AB)+sq(BC) incommensurable with sq(AC), rationality of sq(AB)+sq(BC), and irrationality of AC. The citation differences are purely depth-related: the AI explicitly cites 6.1 for the proportion that Heath states implicitly, appeals directly to the definition of commensurable magnitudes (D10.1.1) where Heath invokes X.6, and adds definitions D10.1.2 and D10.1.3 plus the transitivity result 10.12 for the rationality argument. The sole heath_only item (10.6) is replaced by the AI's direct definitional argument reaching the same conclusion, making this a citation-depth difference rather than a backbone divergence.

### 10.74
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: (1) squares on AB and BC are medial, (2) twice the rectangle AB,BC is rational, (3) the squares are incommensurable with twice the rectangle, (4) by the II.7 identity and X.16, twice the rectangle is incommensurable with the square on AC, (5) the square on AC is irrational so AC is irrational. The AI proof follows this identical logical chain but provides more granular citations at each step: it explicitly invokes 10.21 to justify that squares on medial lines are medial areas, 10.15 and D10.1.2 for commensurability of the sum of squares, 10.23 to show the sum is medial, and 10.12 and D10.1.1 for transitivity of commensurability arguments. Heath leaves these intermediate justifications implicit. Since heath_only is empty and all ai_only items are supporting citations that flesh out the same logical path, this is a clear granularity difference.

### 10.75
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided this classification. Both proofs follow the identical application-of-areas strategy: they apply the squares on AB,BC and twice the rectangle AB,BC to a rational line DI, show the resulting breadths DG and DF are each rational and incommensurable with DI, establish that DE is incommensurable with DH through the chain sq(AB) incommensurable with rect(AB,BC) via X.11, conclude DG and DF are rational commensurable in square only so FG is an apotome by X.73, and then deduce AC is irrational because its square equals the irrational area FE. The key intermediate conclusions are identical in both proofs. The ai_only citations (1.44, 10.12, CN3, CN5, D10.1.2, D10.1.3, D10.1.4) are all construction references, common notions, definitions, or explicit transitivity steps (10.12 for showing DG,DF commensurable in square) that provide additional granularity for the same logical backbone. The single heath_only citation (10.28) is merely a reference in the setting-out to guarantee the hypotheses are satisfiable and plays no role in the deductive chain. Since the backbone is the same and the citation differences reflect only depth of explicit detail, the classification is G.

### 10.76
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing that the sum of the squares on AB and BC is incommensurable with twice the rectangle AB, BC, then using the II.7 decomposition and X.16 to conclude that the sum of squares is incommensurable with the square on AC, and finally inferring that the square on AC is irrational because the sum of squares is rational. The citation differences are entirely depth-related: the AI explicitly cites transitivity (10.13), the medial-implies-irrational lemma (10.21), and definitions (D10.1.1, D10.1.4) that Heath invokes implicitly, while Heath cites the construction reference 10.33 that the AI omits by stating the conditions directly. No backbone divergence exists, making this a granularity difference.

### 10.77
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) the sum of squares on AB, BC is incommensurable with twice the rectangle AB, BC because one is medial and the other rational, (2) by II.7 and X.16 the square on AC is incommensurable with twice the rectangle AB, BC, (3) since twice the rectangle is rational the square on AC is irrational, hence AC is irrational. The citation differences are all matters of depth: the AI explicitly cites 10.13 for transitivity of incommensurability (used implicitly by Heath), 10.21 to justify that a medial area is irrational, and D10.1.4 for the definition of rational and irrational areas, while Heath cites 10.34 as the source of the initial conditions which the AI takes as given. Since the key intermediate conclusions are identical and only the citation granularity differs, the classification is G.

### 10.78
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct rational line DI, apply DE equal to the squares on AB and BC producing breadth DG, apply DH equal to twice the rectangle AB,BC producing breadth DF, show DG and DF are each rational and incommensurable in length with DI via X.22, show DG incommensurable with DF via VI.1 and X.11, conclude they are rational commensurable in square only so FG is an apotome by X.73, and finally that the rectangle under rational DI and apotome FG is irrational (deduction from X.20) making AC irrational. The ai_only citations (1.44, 1.45, 10.12, CN3, CN5, D10.1.2, D10.1.3, D10.1.4) are construction propositions, common notions, definitions, and one explicit transitivity step that Heath handles implicitly, all representing over-citation at a finer granularity. The heath_only citation (10.35) is a condition reference that the AI states directly without citation. Since the key intermediate conclusions are identical and only citation depth differs, this is a granularity difference.

### 10.79
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume a second annex BD so that AD and DB are rational commensurable in square only, apply II.7 to both pairs to relate the squares and rectangles, show the excess of the sums of squares is rational while both twice-rectangles are medial, and derive a contradiction via X.26. The AI proof establishes every one of these key intermediate conclusions in the same logical order as Heath. The ai_only set consists entirely of sub-citations that Heath uses implicitly: transitivity of commensurability (10.12), commensurability of sum and remainder (10.15), commensurability with medial is medial (10.23), ratio of numbers gives commensurability (10.6), common notions (CN1, CN3, CN5), and definitions of rationality (D10.1.3, D10.1.4). Heath_only is empty, confirming that the AI covers all of Heath's cited material. This is Case A of Q2: same backbone, different citation depth.

### 10.80
**Category**: Granularity difference
**Jaccard**: 0.385
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction through identical key intermediate conclusions: setting up two annexes via 10.74, applying II.7 to express each sum of squares as twice the rectangle plus the square on AB, deriving that the excess of the sums of squares equals the excess of the doubled rectangles, showing the doubled rectangles differ by a rational area, showing both sums of squares are medial, and reaching contradiction via 10.26. The AI proof cites the same five references Heath uses plus eight additional items (10.6, 10.12, 10.21, CN1, CN3, CN5, D10.1.2, D10.1.4) that are common notions, definitions, and lower-level commensurability and medial-area propositions Heath invokes implicitly. Since heath_only is empty and all ai_only items are sub-steps of the same reasoning Heath performs without explicit citation, this is Case A of Q2: same backbone, different citation depth.

### 10.81
**Category**: Granularity difference
**Jaccard**: 0.550
**Analysis**: Q2 decided the classification. Both proofs employ the same uniqueness-by-contradiction strategy: they assume two annexes to the second apotome of a medial straight line, apply rectangle areas to a rational line EF to produce breadths EM/HM and EN/HN, show these breadths are rational and commensurable in square only (making EH an apotome with two distinct annexes), and derive a contradiction via X.79. The key intermediate conclusions are identical in both proofs. Heath_only is empty, meaning every citation Heath makes also appears in the AI proof. The nine ai_only items (1.45, 10.12, 10.21, 5.14, CN1, CN2, CN5, D10.1.2, D10.1.3) are construction propositions, definitions, common notions, and supporting lemmas that provide explicit justification for steps Heath treats more concisely. The AI also adds an explicit step (Step 10) proving HM and HN are distinct, using 5.14, whereas Heath states the analogous conclusion ('similarly') without separate proof. This is a clear case of same backbone with different citation depth, yielding G.

### 10.82
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) set up AB as a minor straight line with annex BC satisfying the conditions of 10.76, (2) assume a second annex BD satisfying the same conditions, (3) establish that the excess of the squares on AD,DB over AC,CB equals the excess of twice the rectangle AD,DB over twice the rectangle AC,CB, (4) show this excess is rational because both sums of squares are rational, (5) derive a contradiction via 10.26 since both twice-rectangles are medial yet their difference would be rational. The AI proof reproduces every key intermediate conclusion of Heath's proof but provides far more explicit detail, citing 2.1 and 2.7 for the algebraic identities Heath applies without citation, CN1/CN2/CN5 for basic axioms Heath invokes implicitly, and 10.12/10.15/D10.1.4 for the commensuratibility and rationality steps Heath compresses into the phrase 'for both are rational'. Since heath_only is empty and all ai_only items are sub-steps of reasoning Heath performs implicitly, this is Case A of Q2: same backbone, different citation depth.

### 10.83
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs establish uniqueness of the annex by the same contradiction: showing the excess of the sums of squares on AD,DB over AC,CB equals the excess of twice the rectangles, concluding that medial areas differ by a rational area, which contradicts 10.26. The AI proof spells out lower-level steps (2.7 for the algebraic identity, CN1/CN3/CN5 for arithmetic, 10.12/10.15/D10.1.4 for commensurability reasoning) that Heath compresses as 'as in the preceding cases.' The empty heath_only set confirms the AI covers all of Heath's reasoning at greater citation depth, making this a clear granularity difference.

### 10.84
**Category**: Granularity difference
**Jaccard**: 0.389
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume BC is an annex to AB per X.78, suppose BD is another annex, set out a rational line EF, apply areas equal to the relevant sums of squares and doubled rectangles to EF, use II.7 to identify the remainder with the square on AB, invoke X.22 to show the resulting breadths are rational and incommensurable with EF, use VI.1 and X.11 to show mutual incommensurability of breadths, conclude via X.73 that EH is an apotome with two distinct annexes, and reach contradiction via X.79. The AI proof cites the same core propositions as Heath (10.11, 10.22, 10.73, 10.78, 10.79, 2.7, 6.1) and adds only construction propositions (1.44, 1.45), a commensurability transitivity result (10.12), a medial-area characterization (10.21), common notions (CN1-CN5), and definitions (D10.1.2, D10.1.3) that Heath leaves implicit. With heath_only empty and ai_only consisting entirely of foundational over-citations, this is a clear case of same backbone with different citation depth.

### 10.85
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: setting out a rational line A with BG commensurable in length, choosing square numbers with a non-square difference, applying 10.6 to establish the ratio of squares, showing GC is rational and BG is incommensurable in length with GC (10.9), concluding BC is an apotome (10.73), then using convertendo (5.19) to show BG is commensurable with H, and finally concluding BC is a first apotome (D10.3.1). The heath_only set is empty, meaning every Heath citation appears in the AI set. The 13 ai_only items are all lower-level expansions: the AI explicitly constructs the line H via the semicircle method (1.10, P3, 4.1, P1, 3.31, 1.47) where Heath simply posits it, uses 8.24 to justify a number-theoretic step Heath treats as obvious, cites 10.12 for transitivity of commensurability, and names every definition (D10.1.2, D10.1.3, D5.5, D7.18) and construction step (1.3) that Heath leaves implicit. This is a clear Case A under Q2: same backbone, different citation depth.

### 10.86
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs construct a second apotome through identical key intermediate conclusions: establishing GC as rational, contriving the ratio FD:DE = sq(CG):sq(GB) to obtain commensurability in square, showing incommensurability in length via the non-square ratio, concluding BC is an apotome by 10.73, then proving BG is commensurable in length with H (where sq(H) = sq(BG) - sq(GC)) and noting the annex CG is commensurable with A to satisfy the definition of a second apotome. The heath_only set is empty, meaning the AI cites a strict superset of Heath's references. All ai_only items are definitions (D10.1.2, D10.1.3, D10.1.4, D5.5, D7.18) and auxiliary or intermediate propositions (10.12, 2.14, 5.7, 8.24) that make explicit the steps Heath performs implicitly. This is a clear Case A in Q2: same backbone, different citation depth.

### 10.87
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: FG is rational and incommensurable in length with A (via 10.6 and 10.9); GH is rational and incommensurable in length with FG; FG and GH are rational commensurable in square only, making FH an apotome (10.73); via ex aequali (5.22), A is incommensurable with GH so neither FG nor GH is commensurable with A; the square on FG exceeds the square on GH by the square on a line commensurable with FG (via convertendo, 5.19); therefore FH is a third apotome. The AI adds nine citations beyond Heath's set, but heath_only is empty, confirming Heath's references are a strict subset. The ai_only items are definitions (D10.1.2, D10.1.3, D10.1.4), a common notion (CN5), construction propositions (1.47, 3.31, 4.1 for the explicit geometric construction of K via a semicircle that Heath handles abstractly), and supporting results (10.12 for transitivity of commensurability, 5.14 for the ratio comparison). All represent deeper citation of the same logical backbone, not a different proof path.

### 10.88
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: setting out rational A and BG commensurable in length with A, constructing GC via a number-theoretic ratio, establishing that sq(GC) is rational and GC is rational, showing BG and GC are rational commensurable in square only so BC is an apotome (10.73), introducing H such that sq(BG) exceeds sq(GC) by sq(H), applying convertendo (5.19) to obtain sq(BG):sq(H) = ED:DF, deducing BG incommensurable with H (10.9), and concluding BC is a fourth apotome (D10.3.4). The key intermediate conclusions match exactly. The ai_only set consists entirely of definitions (D10.1.2, D10.1.3, D10.1.4, D5.16, D5.5), a common notion (CN5), and construction or auxiliary propositions (1.3, 10.12, 10.13) that Heath applies implicitly; heath_only is empty, confirming the AI cites a strict superset of Heath's references. This is a citation-depth difference, not a path difference.

### 10.89
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: CG rational and commensurable with A, BG rational via the number ratio, BG incommensurable in length with GC, BC an apotome by 10.73, then BG incommensurable with H via convertendo and 10.9, concluding BC is a fifth apotome. The AI proof is a strict superset of Heath's citations (heath_only is empty), adding construction-level detail (1.47, 3.31, 4.1 for the geometric construction of H that Heath assumes), an intermediate ratio step (5.7), a transitivity lemma (10.12), and explicit definitions (D10.1.2, D10.1.3, D10.1.4, D5.5). These are all deeper justifications for steps Heath takes for granted, making this a citation-depth difference under Case A of Q2.

### 10.90
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing FG and GH via 10.6, establishing FG and GH as rational and commensurable in square only, proving FH is an apotome via 10.73, using ex aequali (5.22) to show A is incommensurable in length with GH, using convertendo (5.19) to show FG is incommensurable in length with K, and concluding FH is a sixth apotome by definition. The ai_only set consists entirely of over-citations: 2.14 (explicit construction of K that Heath leaves implicit), CN5 (common notion for BC > CD), and definitions D10.1.2, D10.1.3, D5.5 that Heath invokes without citation. With heath_only empty and the backbones identical, this is Case A — same backbone, different citation depth — yielding G.

### 10.91
**Category**: Path difference
**Jaccard**: 0.387
**Analysis**: Q2 decided the classification. Both proofs share the same initial backbone through Step 4: setting up the first apotome AD with annex DG, bisecting DG at E, applying 10.17 to get AF and FG commensurable, and establishing that the relevant rectangles are rational or medial. However, the proofs diverge at the critical construction step. Heath constructs squares LM and NO about the same diameter (6.26), then uses the Lemma after 10.53 to show MN is a mean proportional between LM and NO, and derives AB = sq(LN) through a gnomon argument. The AI instead constructs Q as a fourth proportional via 6.12, uses ratio algebra (5.11, 5.7, 5.9) to show rect(LP,Q) = rect(AC,EG) and sq(Q) = rect(AC,FG), then applies the algebraic identity 2.7 to derive AB = sq(W). The heath_only propositions (6.26 and 10.53) are not contained within any AI-cited proposition's proof; they represent an independent geometric method (squares about a diameter with mean proportional lemma) versus the AI's proportional-algebraic method (fourth proportional with ratio properties). This constitutes a genuine path difference with a valid alternative route.

### 10.92
**Category**: Granularity difference
**Jaccard**: 0.387
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish AF commensurable with FG via 10.17, show the rectangles AC*AF and AC*FG are medial and AC*EG is rational, derive the mean proportional relationship, and conclude that LP and PN are medial straight lines commensurable in square only containing a rational rectangle, yielding LN as a first apotome of a medial straight line via 10.74. The proofs differ only in the constructive technique for showing sq(LN) = AB: Heath uses 6.26 to place squares about the same diameter and a gnomon argument, while the AI uses 2.14 to construct LP, 6.12 for a fourth proportional PX, and algebraic identities (2.7, 2.1) to reach the same equality. Since all key intermediate conclusions are the same and the citation differences consist of the AI over-citing construction steps, definitions, and common notions that Heath leaves implicit, plus Heath's single use of 6.26 being replaced by the AI's equivalent algebraic construction, this is a granularity difference.

### 10.93
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: establishing AF, FG commensurable via 10.17; showing AI, FK, and EK are medial rectangles; proving AF incommensurable with EG and hence AI incommensurable with EK; constructing LN as the side of area AB; and concluding that LP, PN are medial straight lines commensurable in square only containing a medial rectangle, so LN is a second apotome of a medial straight line by 10.75. The differences are entirely in citation depth: the AI explicitly cites construction steps (1.10, 1.3, 1.31, 1.36, 6.28), definitions (D10.1.2, D10.1.3), common notions (CN1, CN3, CN5), and a postulate (P2) that Heath leaves implicit, and uses alternative but equivalent technical lemmas (6.22, 5.9, 2.7, 2.14 instead of Heath's 6.17 and 6.26) to reach the same intermediate results. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.94
**Category**: Granularity difference
**Jaccard**: 0.290
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: AF incommensurable with FG (X.18), AK rational (X.19), DK medial (X.21), AI incommensurable with FK (VI.1, X.11), the area AB equals the square on LN, and LN is minor (X.76). The single heath_only citation (6.26) is used by Heath for the geometric gnomon construction showing that squares LM and NO are about the same diameter; the AI replaces this with an algebraic proportion chain using 6.22, 5.9, and the identity 2.7, arriving at the same result. The 21 ai_only items are overwhelmingly construction citations (1.10, 1.3, 1.31, 1.34, P2), definitions (D10.1.1-D10.1.4, D6.1), common notions (CN3, CN5), algebraic identities (2.1, 2.14, 2.7), and supporting propositions (10.13, 10.23, 10.73, 6.28) that Heath leaves implicit. Since the logical backbone is the same with only citation depth differing, this is a granularity difference.

### 10.95
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: setting up the fifth apotome with annex DG, bisecting DG and applying a parallelogram to AG to get AF incommensurable with FG (10.18), establishing AK as medial (10.21) and DK as rational (10.19), constructing squares with sides LP and PN, and concluding that LN produces with a rational area a medial whole (10.77). The sole heath_only citation (6.26, squares about the same diameter) is a construction step that the AI handles through a more explicit route using 2.14, 6.22, and detailed proportionality arguments (5.7, 5.9, 5.11, 6.1). The 24 ai_only citations are overwhelmingly construction steps (1.10, 1.3, 1.31, 1.36), common notions (CN1-3, CN5), definitions (D10.1.1-4), and intermediate results that Heath uses implicitly or abbreviates with the phrase 'Similarly then we can prove that LN is the side of the area AB.' This is Case A of Q2: same backbone, different citation depth.

### 10.96
**Category**: Granularity difference
**Jaccard**: 0.292
**Analysis**: Q2 Case A decided the classification. Both proofs follow the same logical backbone: establishing the sixth apotome properties of AG and GD, bisecting DG and applying a parallelogram to obtain AF incommensurable with FG (10.18), showing AK and DK are medial (10.21), showing AK incommensurable with KD (6.1, 10.11), constructing squares LM and NO about the same diameter (6.26), proving LN is the 'side' of the area, and concluding via the conditions of 10.78. The heath_only set is empty, meaning every citation Heath makes also appears in the AI proof. The AI adds 17 explicit sub-step citations (construction propositions 1.10, 1.31, 1.34, 1.36, 1.43; ratio results 5.8, 5.11, 5.13, 6.17; application of areas 6.28; square construction 2.14; apotome properties 10.73; definitions D10.1.2, D10.1.3; common notions CN2, CN3; and postulate P2) that Heath leaves implicit or covers with the phrase 'in manner similar to the above.' This is a clear case of the AI providing greater citation depth for the same argumentative backbone, yielding classification G.

### 10.97
**Category**: Granularity difference
**Jaccard**: 0.321
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: AG and GB are rational commensurable in square only; the remainder FL equals twice the rectangle AG,GB via II.7; the rational area CL applied to CD yields CM rational and commensurable with CD (X.20); the medial area FL applied to CD yields FM rational and incommensurable with CD (X.22); CM is incommensurable with FM via VI.1 and X.11; CF is an apotome via X.73; the mean proportional argument yields rect(CK,KM) = (1/4)sq(FM) via VI.17; CK is commensurable with KM; and sq(CM) exceeds sq(FM) by a commensurable square via X.17, making CF a first apotome. The AI proof follows this same logical backbone but cites construction propositions (I.10, I.31, I.36, I.44, I.45), common notions (CN3, CN5), definitions (D10.1.1-4), and subsidiary results (10.12, 10.13, 10.15, 10.21, 10.23, II.4, V.11, V.7) that Heath leaves implicit. Since heath_only is empty and all ai_only items represent finer-grained citation of the same steps, this is a clear Case A granularity difference.

### 10.98
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: that CL (the sum of squares on AG, GB) is medial, that CM is rational and incommensurable with CD, that FL (twice rect AG,GB) is rational, that FM is rational and commensurable with CD, that CM is incommensurable with FM so CF is an apotome, and that via the mean proportional argument rect(CK,KM) equals one-fourth the square on FM, yielding CF as a second apotome. The heath_only set is empty, meaning the AI cites every proposition Heath cites. The ai_only items are all over-citations: construction propositions (1.10, 1.31, 1.36, 1.45), common notions (CN3, CN5), definitions (D10.1.2, D10.1.3, D10.1.4), and intermediate results (10.12, 10.13, 10.21, 2.4) that make explicit what Heath leaves implicit. This is Case A of Q2: same backbone, different citation depth, hence G.

### 10.99
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: CL equals the sum of squares on AG and GB and is medial, CM is rational and incommensurable with CD, FL equals twice the rectangle AG-GB, FM is rational and incommensurable with CD, CL is incommensurable with FL so CM is incommensurable with FM, CF is an apotome by X.73, CK is commensurable with KM, NL is a mean proportional between CH and KL, the rectangle CK-KM equals the fourth part of the square on FM, and by X.17 the square on CM exceeds the square on FM by a commensurable square, yielding a third apotome. The heath_only set is empty, confirming the AI covers every citation Heath uses. The 14 ai_only items are all construction propositions (1.10, 1.31, 1.36, 1.45), common notions (CN2, CN3, CN5), definitions (D10.1.2, D10.1.3), and basic results (10.6, 10.12, 10.21, 2.4, 6.17) that the AI cites explicitly while Heath leaves them implicit. This is a same-backbone, different-depth scenario characteristic of granularity difference.

### 10.100
**Category**: Granularity difference
**Jaccard**: 0.440
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: establishing AG and GB as incommensurable in square with rational sum of squares and medial rectangle (10.76), showing CL is rational so CM is rational and commensurable with CD (10.20), deriving FL as twice the rectangle AG,GB (2.7), showing FL is medial so FM is rational and incommensurable with CD (10.22), proving CM incommensurable with MF to establish CF as an apotome (10.73), then proving CK incommensurable with KM via the squares on AG and GB, constructing the mean proportional NL between CH and KL (5.11), deriving rect CK,KM equals one-fourth sq FM (6.17), and concluding via 10.18 and the definition D10.3.4 that CF is a fourth apotome. The AI adds 14 citations not in Heath (construction steps 1.10, 1.31, 1.34, 1.36, 1.44; intermediate commensurability lemmas 10.12, 10.13; medial-area result 10.23; common notions CN2, CN3, CN5; and definitions D10.1.1, D10.1.2, D10.1.3), while heath_only is empty. All AI-only citations are construction propositions, common notions, definitions, or sub-lemmas that Heath invokes implicitly, representing citation-depth over-specification rather than a different proof path.

### 10.101
**Category**: Granularity difference
**Jaccard**: 0.409
**Analysis**: Q2 decided the classification. The AI proof follows the identical logical backbone as Heath's proof for 10.101, establishing the same key intermediate conclusions in the same order: CL is medial (sum of squares on AG, GB), CM is rational and incommensurable with CD (by X.22), FL equals twice the rectangle AG,GB and is rational giving FM commensurable with CD (by X.20), CM and MF are rational commensurable in square only making CF an apotome (by X.73), the rectangle CK times KM equals one quarter of the square on FM, CK is incommensurable with KM, and thus CF is a fifth apotome by X.18 and Definition III.5. The heath_only set is empty, meaning every citation Heath uses also appears in the AI's citation list. The AI's thirteen additional citations (1.10, 1.31, 1.36, 1.45, 10.12, 10.13, 5.7, 5.11, 6.17, CN3, CN5, D10.1.2, D10.1.3) are all construction steps, common notions, definitions, or intermediate proportion and commensurability results that Heath employs implicitly. Q2 Case A applies: same backbone, different citation depth, yielding Granularity difference.

### 10.102
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: setting up AG, GB as incommensurable-in-square lines with medial sums-of-squares and medial double-rectangle (10.78), applying areas to CD and using II.7 to identify FL as twice the rectangle AG.GB, establishing CM and FM as rational and incommensurable with CD via X.22, proving CM incommensurable with FM via VI.1 and X.11, concluding CF is an apotome via X.73, bisecting FM and establishing the mean proportional to show CH incommensurable with HM, applying X.18 to conclude the square on CM exceeds that on FM by an incommensurable square, and finally identifying CF as a sixth apotome via Def.X.III.6. The heath_only set is empty, confirming that every Heath citation appears in the AI's set. The ai_only items are all construction propositions (1.10, 1.31, 1.34, 1.36, 1.45), common notions (CN2, CN3, CN5), definitions (D10.1.2, D10.1.3), and sub-lemmas (10.12, 2.4, 5.11, 6.17) that Heath leaves implicit. This is a clear case of same backbone with different citation depth, yielding G.

### 10.103
**Category**: Granularity difference
**Jaccard**: 0.421
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing DF such that BE:DF = AB:CD, deriving that AE is commensurable with CF and BE with DF (via V.12 and X.11), establishing that CF and FD are rational commensurable in square only, obtaining AE:EB = CF:FD by alternation (V.16), and then transferring both the commensurability/incommensurability of the excess and the commensurability conditions with the rational line (via X.14, X.12, X.13) to conclude CD is an apotome of the same order. The AI proof adds explicit citations for lower-level propositions (10.6, 10.9), definitions of rationality and commensurability (D10.1.2, D10.1.3), all six apotome order definitions (D10.3.1-D10.3.6), and a postulate (P2), none of which alter the logical backbone. The empty heath_only set confirms the AI covers all of Heath's cited propositions. This is Case A of Q2: same backbone, different citation depth.

### 10.104
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: AE and EB are medial commensurable in square only, the proportion AB:CD = BE:DF is established, AE is commensurable with CF and EB with FD, CF and FD are medial commensurable in square only, rect(AE,EB) is commensurable with rect(CF,FD), and the rational or medial character is preserved across the two cases. The differences lie entirely in the sub-step derivation routes to these identical conclusions: Heath uses V.12 for the proportion manipulation while the AI uses 5.16 and 5.18 (alternation and componendo); Heath uses X.13 for commensurability in square while the AI uses 6.22 and 10.11; Heath establishes rectangle commensurability via V.16 while the AI uses two applications of 6.1 through an intermediate rectangle CF*EB combined with 10.12. These are citation-depth differences, not backbone differences, yielding Case A of Q2 and classification G.

### 10.105
**Category**: Granularity difference
**Jaccard**: 0.389
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) CF, FD are incommensurable in square, (2) the sum of the squares on CF, FD is rational, and (3) the rectangle CF, FD is medial, leading to the conclusion that CD is minor by 10.76. The heath_only citations (10.13, 5.12) are functionally replaced by AI citations that achieve identical results at different granularity: the AI uses 10.11 (which transfers both commensurability and incommensurability through proportions) in place of Heath's 10.13 (which transfers incommensurability via commensurable magnitudes), and uses 6.12 with related Book 5 steps in place of Heath's 5.12. The large ai_only set (1.3, 10.12, 10.6, 10.9, 5.11, 6.1, 6.12, D10.1.2, P2) consists of construction steps and lower-level lemmas that Heath leaves implicit, confirming a citation-depth difference rather than a backbone divergence. Case A of Q2 holds, yielding G.

### 10.106
**Category**: Granularity difference
**Jaccard**: 0.067
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing that AE and EB satisfy the conditions of 10.77, constructing CF and FD in the same ratio, then showing that the sum of squares on CF and FD is commensurable with (and hence medial like) the sum on AE and EB, and that the rectangle CF, FD is commensurable with (and hence rational like) the rectangle AE, EB, concluding via 10.77 that CD is of the required type. Heath abbreviates steps 2 through 5 with the phrase 'in manner similar to the foregoing,' while the AI writes out every detail, explicitly citing proportion results (5.11, 5.15, 5.16, 5.18), ratio and similarity results (6.1, 6.12, 6.22), commensurability results (10.6, 10.9, 10.11, 10.12, 10.23), and definitions (D10.1.2, D10.1.4). The heath_only set is empty, confirming that the AI covers everything Heath cites plus more. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 10.107
**Category**: Granularity difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) AE, EB satisfy the conditions of 10.78, (2) AE, EB are commensurable with CF, FD and the corresponding sums of squares and rectangles are commensurable, (3) CF, FD inherit all properties (incommensurability in square, mediality of sum of squares, mediality of rectangle, incommensurability between sum of squares and rectangle), (4) CD produces with a medial area a medial whole by 10.78. The sole difference is citation depth: Heath abbreviates the entire construction and commensurability argument as 'as was proved' (referring to parallel structure from 10.104-10.106), citing only 10.78, while the AI explicitly derives every step using fundamental propositions from Books 5, 6, and 10 (ratio manipulation, proportionality, commensurability criteria). The heath_only set is empty, confirming Heath cites nothing the AI omits; the 13 ai_only items are all sub-results of the argument Heath abbreviates. This is Case A of Q2: same backbone, different citation depth.

### 10.108
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: constructing rectangles GH and GK on rational line FG equal to the rational area BC and medial area BD respectively, establishing that FH is rational and commensurable in length with FG (10.20), FK is rational and incommensurable in length with FG (10.22), deriving their mutual incommensurability (10.13), concluding KH is an apotome (10.73), then splitting into two cases -- first apotome yielding an apotome side (10.91) and fourth apotome yielding a minor side (10.94). The AI proof cites every proposition Heath cites (heath_only is empty) plus additional construction propositions (1.44, 1.45), an intermediate commensurability lemma (10.12), a medial characterization (10.21), common notions (CN1, CN3, CN5), and definitions (D10.1.2, D10.1.3, D10.1.4) that Heath leaves implicit. This is a strict superset citation pattern with identical key intermediate conclusions, which is the hallmark of a granularity difference.

### 10.109
**Category**: Granularity difference
**Jaccard**: 0.316
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they set out a rational straight line FG, apply the medial and rational areas to obtain breadths FH and FK, establish that FH is rational and incommensurable in length with FG while FK is rational and commensurable in length with FG, conclude that FH and FK are commensurable in square only so that KH is an apotome, and then split into two cases depending on whether the square on HF exceeds the square on FK by the square on a line commensurable or incommensurable with HF, yielding a second or fifth apotome respectively. The AI proof cites all six of Heath's references plus thirteen additional ones (construction propositions 1.44 and 1.45, supporting results 10.12, 10.20, 10.22, irrationality propositions 10.74 and 10.77, common notions CN3 and CN5, and definitions D10.1.1-D10.1.4) that Heath invokes implicitly. Since heath_only is empty and all ai_only items are finer-grained sub-steps of the same argument, this is a citation-depth difference with identical key intermediate conclusions, giving Granularity difference (G).

### 10.110
**Category**: Granularity difference
**Jaccard**: 0.615
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: applying medial areas BC and BD to a rational line FG to obtain rational breadths FH and FK incommensurable in length with FG (via 10.22), establishing that FH and FK are incommensurable in length with each other (via 6.1 and 10.11), concluding KH is an apotome (via 10.73), and then splitting into two cases depending on the commensurability condition for the excess of squares, yielding either a third apotome (leading to a second apotome of a medial via 10.93) or a sixth apotome (leading to a line producing with a medial area a medial whole via 10.96). The AI proof adds five citations that Heath leaves implicit: 1.45 for the rectangle construction, 10.12 for establishing commensurability in square between FH and FK, CN3 and CN5 for arithmetic steps, and D10.1.3 for the definition of rational. Since heath_only is empty and all ai_only items are construction references, common notions, a definition, or a supporting intermediate step, this is a clear case of over-citation with the same backbone, yielding G.

### 10.111
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume AB is both apotome and binomial, apply its square to a rational line DC to get breadth DE, show DE is simultaneously a first apotome (10.97) and a first binomial (10.60), derive that DF and DG are both commensurable with DC and hence with each other (10.12), then that GF is commensurable with DF (10.15) but incommensurable with EF (10.13), making GF and FE rational commensurable in square only so that GE is an apotome (10.73) yet also rational, yielding a contradiction. The AI proof adds seven citations beyond Heath (1.45, 10.36, 10.6, 10.9, CN5, D10.1.2, D10.1.3), all of which are either construction propositions, definitions, common notions, or supporting lemmas that provide finer-grained justification for steps Heath handles implicitly. In particular, the AI explicitly proves GF and FE are commensurable in square via 10.9, 10.6, and 10.12, a step Heath states without proof. Since heath_only is empty and every AI-only citation represents deeper justification of a shared intermediate conclusion, this is Case A of Q2: same backbone, different citation depth.

### 10.112
**Category**: Granularity difference
**Jaccard**: 0.359
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: setting up rectangles BC*EF = BD*G = A squared, deriving proportions CB:BD = HE:EF and CD:BD = HF:FE via separando, constructing FK:KE = HF:FE to obtain the continued proportion HK:KF:KE = CD:DB, proving commensurability of squares and lengths to establish that EH and EK are rational, showing FK and KE are rational and commensurable in square only so EF is an apotome, and demonstrating order preservation through all six binomial/apotome cases. The ai_only set consists entirely of construction propositions (1.3, 1.45, 6.11), auxiliary proportion results (5.7, 5.18, 6.19), common notions (CN1, CN5), a postulate (P2), and definitions of binomial/apotome orders (D10.1.2-D10.3.6) that Heath uses implicitly. The sole heath_only item D5.9 is a definition that the AI addresses through 6.19 Porism instead. The low Jaccard (0.359) is entirely attributable to the AI's over-citation of basic steps and definitions, not to any structural divergence.

### 10.113
**Category**: Path difference
**Jaccard**: 0.243
**Analysis**: Q2 decided the classification. Heath's proof introduces an auxiliary line G via rect(BC,G) = sq(A), uses 10.20 to establish G rational and commensurable with BC, then applies 6.16 for the proportion CB:BD = KH:G, convertendo (5.19) to obtain BC:CD = KH:HE, and a continued proportion construction to locate F with KF:FH = BC:CD. The AI proof takes a fundamentally different route: it uses 2.6 (a Book 2 rectangle identity) with a bisection-and-addition construction to establish BM*BD + CD^2 = BC^2, shows rect(BM,BD) is rational, derives KH commensurable with BM via 6.1 (rectangles under same height), then cuts KH at F similarly to BM at C using 6.10, and applies 5.12 for ratio composition. The key intermediate conclusions differ in construction and method: Heath's auxiliary G and convertendo route versus the AI's 2.6 identity and similar-cutting route. Neither set of heath_only propositions (10.20, 5.19, 6.16, 5.11, D5.9) is contained in any higher-level proposition cited by the AI; they represent an independent proof strategy. The AI proof is logically complete under Q1(b), with every step properly supported by valid citations, so Q3 confirms the AI's different path as valid, yielding D.

### 10.114
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: construct rational line H, apply its square to binomial CD to produce apotome KL (10.112), establish AF:FB = KM:ML by ratio transitivity, take the proportion alternately, apply the remainder theorem (5.19) to get AB:KL = AF:KM, chain commensurability from AF-KM (10.12) to AB-KL (10.11), then to the rectangles (6.1, 10.11), and conclude that G is rational. The AI cites every reference Heath cites (heath_only is empty) plus seven additional items: construction prop 1.44, apotome definition 10.73, proportion rules 5.11 and 5.16, and rationality definitions D10.1.2-D10.1.4. These are all steps Heath performs implicitly without explicit citation. The symmetric difference reflects citation depth, not a different proof strategy, making this a granularity difference.

### 10.115
**Category**: Granularity difference
**Jaccard**: 0.062
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct C with C squared equal to the rectangle B times A (B rational, A medial), prove C is irrational via X. Def. 4 and X.20, show C is not the same as any preceding irrational type, then repeat for D with D squared equal to B times C, and note the process continues ad infinitum. The AI proof is far more explicit, providing a lemma that a medial is neither rational nor binomial nor apotome (citing 10.21, 10.22, 10.60, 10.97, 10.36, 10.73), then exhaustively verifying C and D against all 13 preceding irrational types using 10.60-10.65, 10.97-10.102, and the corresponding definitions. Heath accomplishes the same in a single sentence. Since heath_only is empty and all ai_only items are propositions and definitions that expand on arguments Heath makes tersely, this is Case A of Q2: same backbone, different citation depth, yielding G.


---

## Book 11 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 38 | 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 11.10, 11.11, 11.12, 11.13, 11.14, 11.15, 11.16, 11.17, 11.18, 11.19, 11.20, 11.21, 11.22, 11.23, 11.24, 11.25, 11.26, 11.27, 11.28, 11.29, 11.30, 11.31, 11.32, 11.33, 11.34, 11.35, 11.36, 11.38, 11.39 |
| Path difference (D) | 1 | 11.37 |
| AI proof error (E) | 0 |  |

**Total**: 39 propositions

## Per-Proposition Analysis

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume part AB lies in the reference plane and part BC in an elevated plane, produce AB to D within the reference plane so that ABC and ABD are two distinct straight lines sharing the common segment AB, draw a circle with center B and distance AB, and derive a contradiction from the diameters cutting off unequal circumferences. The AI proof is more detailed, explicitly citing P2 (line production), P3 (circle construction), D1.17 (diameter definition), and CN5 (whole greater than part), all of which Heath invokes implicitly without naming. Since heath_only is empty and ai_only consists entirely of foundational axioms, definitions, and postulates, this is a clear case of over-citation at the same logical backbone, yielding G.

### 11.2
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: proving triangle ECB lies in one plane by contradiction using XI.1, then extending from the triangle's sides (EC, EB) to the full lines (AB, CD) via XI.1, and finally generalizing to every triangle. The AI proof's extra citations (D1.19 for the definition of a triangle, P1 for the postulate allowing points to be joined) are explicit references to foundational items that Heath invokes implicitly without citation. Since heath_only is empty and ai_only contains only a definition and a postulate, the difference is purely one of citation depth, not of logical path. Case A of Q2 holds, yielding G.

### 11.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: proof by contradiction assuming the common section DB is not a straight line, constructing straight lines DEB in plane AB and DFB in plane BC, showing these two lines share extremities D and B and would therefore enclose a space (which is impossible), concluding that DB must be a straight line. The AI proof adds more explicit justification in Step 4 (arguing that DEB cannot lie in plane BC) and explicitly cites D1.7 (definition of a plane surface) and P1 (the postulate for joining two points by a straight line), both of which Heath uses implicitly without citation. Since ai_only contains only a definition and a postulate -- foundational references rather than substantive theorems -- and the key intermediate conclusions are the same in both proofs, this is a granularity difference where the AI over-cites relative to Heath.

### 11.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs argue through exactly the same key intermediate conclusions: equal segments yield AD=BC and angle DAE=angle EBC via I.4, then GE=EH and AG=BH via I.26 on vertical-angle triangles, then FA=FB and FC=FD via I.4 on right-angle triangles, then angle FAD=angle FBC via I.8, then FG=FH via I.4, then angle GEF=angle HEF via I.8, and finally perpendicularity to an arbitrary line in the plane gives perpendicularity to the plane by XI.Def.3. The backbones are identical. The AI proof adds five citations not in Heath (1.3 for cutting equal segments, 11.2 for intersecting lines lying in a plane, P1 for joining lines, P4 for right angles being equal, D1.10 for the definition of perpendicular), all of which are construction-level, postulate, or definition citations that Heath uses implicitly. The heath_only set is empty. This is a clear case of over-citation at the foundational level, constituting a granularity difference.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs employ an identical proof by contradiction: assume BC is not in the plane of reference containing BD and BE, construct line BF as the common section of the plane through AB, BC with the plane of reference (11.3), establish that AB is perpendicular to the plane of reference (11.4), derive that angle ABF is right (D11.3), note that angle ABC is also right, and reach a contradiction. The AI proof cites three additional items not in Heath: 11.2 (to justify explicitly that BD, BE lie in one plane and that AB, BC lie in one plane), P4 (to justify that all right angles are equal), and CN5 (to name the axiom that the whole is greater than the part). All three are over-citations of steps Heath treats as implicit. Since heath_only is empty and the key intermediate conclusions are identical in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.6
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: establishing right angles via D11.3, proving AD = BE through triangle congruence (I.4), showing angle EDA is right via I.8, concluding coplanarity of BD, DA, DC through XI.5, placing AB in that plane via XI.2, and deriving parallelism via I.28. The ai_only set {1.11, 1.3, P1, P4} consists entirely of construction propositions and postulates that Heath uses implicitly without citation: 1.11 for drawing a perpendicular, 1.3 for cutting off an equal length, P1 for joining lines, and P4 for the equality of right angles. The AI explicitly justifies each construction step while Heath performs them silently. With identical backbones and differences confined to citation depth on construction and axiomatic steps, this is Case A of Q2, yielding G.

### 11.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs employ the same proof-by-contradiction backbone: assume the line joining E and F lies in an elevated plane as EGF, draw a plane through EGF whose intersection with the reference plane yields a straight line EF by 11.3, observe that EGF and EF would then be two distinct straight lines enclosing a space (impossible), and conclude the joining line lies in the reference plane. The AI proof explicitly cites D1.23 (definition of parallel lines lying in one plane), D1.4 (definition of a straight line), and P1 (postulate for joining two points), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions and a postulate, the proofs share the same logical backbone at different citation depths, yielding Granularity difference (G).

### 11.8
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: from the perpendicularity of AB to the plane, they establish that angles ABD and ABE are right, use I.29 on the parallels to show CDB is right, apply SAS congruence to get AD = BE, apply SSS congruence to show angle EDA is right, then use XI.4 twice (first to show ED is perpendicular to the plane through BD and DA, then to show CD is perpendicular to the plane of reference) with XI.2 supplying that DC lies in the relevant plane. The AI proof cites seven additional references (1.11, 1.3, 1.4, 1.8, CN3, P1, P4) that Heath uses implicitly without citation. These are all construction propositions, basic congruence theorems, postulates, and a common notion, none of which represents a different logical path. With identical backbones and ai_only consisting entirely of over-citations for implicit steps, this is a granularity difference.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct perpendiculars GH and GK to EF in the two planes, show EF is perpendicular to the plane through GH and GK (11.4), infer that AB and CD are each perpendicular to that plane because they are parallel to EF (11.8), and conclude AB is parallel to CD because both are perpendicular to the same plane (11.6). The AI proof adds three citations not in Heath: D1.23 (definition that parallel lines lie in a plane), 1.11 (construction of a perpendicular at a point on a line), and 11.3 (common section of two planes is a line, used to justify that GH and GK are not collinear). These are a definition, a construction proposition, and a supporting lemma for a detail Heath leaves implicit. Heath cites nothing the AI omits. Since the key intermediate conclusions are identical and the citation differences reflect only granularity of justification, this is a granularity difference.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing equal segments BA=ED and BC=EF, showing AD and CF are each equal and parallel to BE via I.33, applying XI.9 to conclude AD is parallel to CF, then using I.33 again to establish AC equal and parallel to DF, and finally applying I.8 (SSS) for the angle equality. The AI's four additional citations (1.3 for cutting equal segments, P1 for joining lines, CN1 for transitivity of equality, and 11.7 for establishing non-coplanarity) are all explicit justifications for steps Heath performs implicitly. With heath_only empty and ai_only consisting entirely of construction, postulate, common notion, and supporting-detail citations, this is a clear Case A granularity difference.

### 11.11
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs construct the perpendicular AF from elevated point A to the given plane by the same method: dropping AD perpendicular to an arbitrary line BC in the plane, then (if AD is not already perpendicular to the plane) drawing DE perpendicular to BC in the plane, AF perpendicular to DE, and GH parallel to BC through F, and arguing through the same sequence of key intermediate conclusions -- BC is perpendicular to the plane through DA and DE (XI.4), GH is perpendicular to that plane by parallel transfer (XI.8), AF is perpendicular to GH (XI.Def.3), and AF being perpendicular to both DE and GH is perpendicular to the plane through them (XI.4), which is the plane of reference. The backbones are identical. The AI adds only D1.10 (definition of right angles) and P1 (postulate for drawing a line), both foundational items that Heath uses implicitly, making this a citation-depth difference rather than a path difference.

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: conceive an elevated point B, draw BC perpendicular to the plane (11.11), draw AD through A parallel to BC (1.31), conclude AD is perpendicular to the plane (11.8). The AI proof adds two extra citations not in Heath: P1 (to join AC, a postulate over-citation) and 11.2 (to explicitly establish that AC and BC lie in one plane, a detail Heath handles implicitly). Since heath_only is empty and the ai_only items represent finer-grained justification of steps that are implicit in Heath, this is a citation-depth difference with the same backbone, yielding G.

### 11.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume two lines AB, AC perpendicular to the reference plane from point A on the same side, draw a plane through them that intersects the reference plane in line DAE (11.3), show angle CAE is right and angle BAE is right (D11.3), then derive a contradiction from their equality. The AI proof adds explicit citations for steps Heath leaves implicit: 11.2 to justify that AB and AC determine a plane, P4 to state that all right angles are equal, and CN5 to articulate why the equality is impossible (one angle is a proper part of the other, so the whole exceeds the part). Since heath_only is empty and all ai_only items (11.2, CN5, P4) are foundational propositions, postulates, or common notions that make explicit what Heath assumes tacitly, this is a citation-depth difference with the same logical backbone, yielding G.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow an identical proof-by-contradiction backbone: assume the planes are not parallel, derive that their common section is a straight line GH (11.3), take a point K on GH and join AK, BK, show that angles ABK and BAK are both right by the definition of perpendicularity to a plane (D11.3), and reach a contradiction via I.17 (two angles of a triangle cannot sum to two right angles). The only citation difference is that the AI explicitly cites Postulate 1 for joining AK and BK, while Heath invokes this construction implicitly. Since the key intermediate conclusions are identical and the sole difference is citation depth for a construction postulate, Case A of Q2 holds, yielding G.

### 11.15
**Category**: Granularity difference
**Jaccard**: 0.583
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: drop a perpendicular BG from B to the plane through DE and EF (XI.11), construct parallels GH to ED and GK to EF in that plane (I.31), use the perpendicularity to establish right angles BGH and BGK (XI.Def.3), invoke XI.9 to show BA is parallel to GH, apply I.29 to derive that angle GBA is right, repeat for BC, conclude GB is perpendicular to the plane through BA and BC (XI.4), and finally apply XI.14 to establish the planes are parallel. The AI proof adds five citations not in Heath (1.30, 11.3, 11.7, CN3, D1.23), all of which serve as sub-step justifications for reasoning Heath performs implicitly: Step 1 uses 1.30 and D1.23 to prove B is elevated above plane Q (a prerequisite for XI.11 that Heath assumes), Step 5 uses 11.3 to justify that BA and GH are not coplanar with ED (needed for XI.9), Step 6 uses 11.7 to show BG lies in the plane of BA and GH and CN3 to subtract the right angle. Heath cites nothing the AI omits (heath_only is empty). Since the key intermediate conclusions match and the citation differences reflect only the depth of explicit justification, this is a granularity difference.

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assuming the common sections EF, GH meet at a point K, applying 11.1 to show K lies in both parallel planes, deriving a contradiction, and repeating for the other direction to conclude EF is parallel to GH by the definition of parallel lines. The AI proof adds explicit citations for foundational facts that Heath leaves implicit: 11.3 (common sections are straight lines), D11.8 (definition of parallel planes), and P2 (postulate to produce lines). Since heath_only is empty and all ai_only items are over-citations at the construction/definition/postulate level, the proofs share the same logical backbone at different citation depths, yielding G.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: construct auxiliary line AD meeting plane KL at O, join EO and OF, establish EO parallel to BD and AC parallel to OF via XI.16, apply VI.2 twice to obtain AE:EB = AO:OD and AO:OD = CF:FD, then conclude AE:EB = CF:FD by V.11. The AI proof adds explicit citations of 11.2 (two intersecting lines determine a plane), 11.3 (common section of two planes is a line), and Postulate 1 (joining lines), which are foundational steps Heath leaves implicit. Since heath_only is empty and all ai_only items are construction or foundational propositions making explicit what Heath takes as understood, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 11.18
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct FG in plane DE perpendicular to the common section CE, show angle ABF is right via the definition of perpendicularity to a plane (Def. 3), deduce AB parallel to FG (I.28), transfer perpendicularity from AB to FG (XI.8), and conclude by Def. 4. The only citation difference is that the AI explicitly cites 11.3 to justify that the intersection of two planes is a straight line, a foundational step Heath takes as given without citation. This is a citation-depth difference (over-citation by the AI), not a backbone divergence, placing the proof squarely in Case A of Q2.

### 11.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing perpendiculars DE and DF in planes AB and BC respectively, showing each is perpendicular to the reference plane by Definition 11.4, and then invoking 11.13 (uniqueness of the perpendicular from a point to a plane) to reach the conclusion. Heath presents this as a reductio and the AI as a direct argument, but the key intermediate conclusions are identical. The ai_only citations (1.11 for constructing perpendiculars, 11.3 for identifying common sections as straight lines) are construction-level propositions that Heath uses implicitly, representing over-citation rather than a different proof path. With heath_only empty and the backbone matching, this is Case A of Q2: same backbone, different citation depth.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification as G. Both proofs follow the same logical backbone: construct angle BAE equal to DAB and AE equal to AD in the plane through BA and AC, prove DB equals BE by I.4, derive DC greater than EC from the triangle inequality I.20 and the equality DB equals BE, then conclude angle DAC greater than angle EAC by I.25, and finally combine with DAB equals BAE to get DAB plus DAC greater than BAC. The AI proof is more granular, explicitly citing construction propositions (1.23 for angle construction, 1.3 for cutting off equal segments), common notions (CN2, CN3, CN5 for addition, subtraction, and whole-greater-than-part), a definition (D11.11 for solid angles), and postulates (P1, P2 for joining and producing lines) that Heath leaves entirely implicit. Since heath_only is empty, every proposition Heath cites also appears in the AI set, and all ai_only items are construction, axiom, or definition citations rather than substantive theorems, confirming the same backbone at different citation depth.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions for the three-face solid angle case: using XI.20 to show the six non-face angles at vertices B, C, D exceed the three base triangle angles, then using I.32 to establish that the base angles equal two right angles and the nine total triangle angles equal six right angles, and finally subtracting to conclude the three face angles are less than four right angles. The AI proof additionally extends the argument to the general n-face case (Steps 10-14), but the shared three-face backbone is the same. The ai_only set {CN2, D11.11, P1} consists entirely of a common notion, a definition, and a postulate that Heath invokes implicitly, representing over-citation rather than a different proof path. heath_only is empty. Case A of Q2 holds, yielding G.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification as G. Both proofs share the same logical backbone: the equal-angles case is handled trivially via I.4, and the unequal-angles case constructs an auxiliary angle and triangle to copy one of the given angles, uses I.4 to equate the resulting base to one of AC/DF/GK, applies I.24 to establish a base inequality, and then invokes the triangle inequality to combine these results into the required condition that any two of AC, DF, GK exceed the third. The AI constructs the auxiliary angle at B on line AB (copying angle GHK) while Heath constructs it at H on line HK (copying angle ABC), but this is a minor variation in execution, not a different logical path. Every ai_only citation is either a construction step (1.3, 1.23, P1), a common notion (CN1, CN3, CN5), or an explicit citation of a result Heath uses implicitly (1.20 for the triangle inequality, 1.22 for the framing construction theorem). heath_only is empty. This is a clear case of same backbone with different citation depth.

### 11.23
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing triangle LMN via XI.22, circumscribing a circle with centre O, proving AB > LO by contradiction, setting up OR perpendicular to the plane of the circle with OR squared equal to the excess of AB squared over LO squared, establishing RL = RM = RN = AB, and concluding equal angles via I.8. The AI proof is strictly more granular, explicitly treating three sub-cases for the position of O relative to triangle LMN (inside, on a side, outside) and explicitly constructing the line whose square equals the excess via a semicircle, where Heath invokes a Lemma. The heath_only set is empty, confirming that the AI cites every proposition Heath does; the 26 ai_only items consist of construction steps, common notions, definitions, and additional propositions needed for the more detailed case analysis, all reflecting citation-depth differences rather than a different logical path.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use XI.16 to show that common sections of parallel planes cut by a third plane are parallel, establishing that each face is a parallelogram; then they use XI.10 to prove that angles between pairs of meeting parallel lines in different planes are equal, I.34 to obtain equal opposite sides from the parallelograms, I.4 for triangle congruence, and I.34 again for the diagonal-bisection property to conclude that opposite faces are equal. The AI proof cites every foundational item it invokes (CN1 for transitivity of equality, CN2 for adding equals to equals, D11.8 for the definition of parallel planes, P1 for joining points), whereas Heath leaves these implicit. Since heath_only is empty and all ai_only items are common notions, a definition, and a postulate, this is a clear case of over-citation at the same backbone, yielding a granularity difference.

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Both proofs follow the identical equimultiples strategy for establishing the proportion base:base :: solid:solid via V.Def.5. The key intermediate conclusions are the same in both: constructing replicated segments and completing solids, showing component parallelograms and solids are equal, establishing that base-multiples and solid-multiples track together, handling the equal/greater/less trichotomy, and applying V.Def.5. The AI proof cites 13 references while Heath cites only 2 (11.24 and D5.5), but the 11 ai_only items are all construction propositions (1.3, 1.31, P2), auxiliary results about parallels and equal parallelograms (1.30, 1.36, 11.15, 11.16), common notions (CN1, CN5), and definitions (D11.10, D5.2) that Heath uses implicitly without citation. heath_only is empty, confirming the AI covers all of Heath's cited ground. This is a clear case of same backbone with different citation depth, yielding G.

### 11.26
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided this classification as Granularity difference (Case A). Both proofs follow the identical logical backbone for constructing a solid angle at A equal to the given solid angle at D: both drop a perpendicular from the elevated point to the base plane, construct matching angles and segments at A, then use three applications of I.4 (SAS congruence) to establish equality of corresponding bases (KB=GE, HB=FE, AH=FD), followed by I.8 (SSS congruence) to establish equality of the plane angles composing the solid angle. The only structural difference is that the AI explicitly works through the proof of angle HAL = angle FDC in four detailed steps (Steps 10-13, using CN3, I.4, I.4, and I.8), whereas Heath compresses this with 'for the same reason.' The ai_only set consists entirely of construction propositions (1.3), common notions (CN3), definitions (D11.11), and postulates (P1, P4), all making explicit what Heath leaves implicit. The heath_only set is empty, confirming the AI covers all of Heath's cited results at greater depth.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a solid angle at A equal to the solid angle at C, set up the proportions EC:CG = BA:AK and GC:CF = KA:AH via VI.12, derive EC:CF = BA:AH ex aequali via V.22, complete the solid AL, show three pairs of similar parallelograms, extend to all six faces, and conclude similarity of the solids via XI.Def.9. The AI proof cites 10 additional references that Heath uses implicitly: 11.26 for solid angle construction, 1.3 and 1.31 for construction steps, 1.34, 1.29, CN3, and D6.1 for spelling out the parallelogram similarity argument, 11.15 for parallel planes, 11.24 for opposite faces being equal and similar, and 6.21 for transitivity of similarity. The empty heath_only set confirms that every citation Heath uses is also present in the AI proof. This is a clear case of same backbone with different citation depth, yielding G.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they bisect face parallelograms into equal triangles via I.34, note that opposite faces are equal parallelograms, and conclude that the two resulting prisms are equal by XI. Def. 10 (D11.10). The AI proof additionally cites 11.3 (to establish that the cutting plane intersects each face in a straight line), 11.16 (to show the resulting section is a parallelogram by proving opposite sides are parallel), and 11.24 (to justify that opposite faces are equal), all of which Heath uses implicitly without citation. Since heath_only is empty and the ai_only items are all construction or setup propositions that make explicit what Heath leaves tacit, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.29
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: establishing DE=HK and FG=MN by subtraction from equal opposite sides of parallelograms (I.34), proving triangles DCE=HBK and AFG=MLN via I.8 and I.4, showing the relevant parallelograms equal via I.36, concluding the two prisms are equal, and adding the same solid to obtain CM=CN. The AI proof is substantially more detailed, explicitly citing common notions (CN1, CN2, CN3), definitions (D11.10), and supporting propositions (11.24, 11.9, 1.29) that Heath uses implicitly or without citation. Since heath_only is empty and all ai_only items are either common notions, definitions, or minor propositions providing explicit justification for steps Heath takes as understood, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Both proofs follow the identical strategy of constructing a third parallelepipedal solid on the same base by producing edges in the upper plane to meet at auxiliary points, then applying 11.29 twice to show each original solid equals the third, and concluding by transitivity. The AI's nine extra citations (11.1, 11.3, 11.9, 11.24, CN1, D1.23, D11.8, P1, P2) are all definitions, postulates, common notions, and foundational Book 11 propositions that spell out the construction details Heath leaves entirely implicit. Heath's citation set (11.29 alone) is a proper subset of the AI's, and heath_only is empty, confirming complete coverage with no independent route. This is a clear case of same logical backbone at different citation depth, yielding G.

### 11.31
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical logical backbones across both cases (right-angle sides and oblique sides). In Case 1, both construct an auxiliary parallelepiped XU equal and similar to AE, show XU equals YX via XI.29, establish YT equals CD via I.35, and conclude CF equals YX through the same ratio chain (XI.25, V.7, V.11, V.9). In Case 2, both drop perpendiculars to create right-angled solids and reduce to Case 1 via XI.30. The heath_only set is empty, meaning every reference Heath cites also appears in the AI proof. The 15 ai_only items are entirely construction propositions (1.3, 1.31), basic plane geometry results (1.4, 1.29, 1.30, 1.34), common notions (CN1, CN2), definitions (D1.23, D11.3, D6.1, D6.4, D11.10), and postulates (P2, P4), all representing lower-level steps that Heath leaves implicit. The Jaccard of 0.40 reflects this one-sided over-citation rather than any structural divergence.

### 11.32
**Category**: Granularity difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: (1) construct a parallelogram equal to base AE adjacent to base CF, (2) complete a parallelepipedal solid on that parallelogram with the same height as CD, (3) invoke XI.31 to establish that the new solid equals AB, (4) invoke XI.25 on the cutting plane to obtain the ratio CF:new-base = CD:new-solid, and (5) substitute to conclude AE:CF = AB:CD. The sole structural difference is how step (1) is accomplished: Heath cites I.45 in a single step, while the AI first converts the parallelogram AE into an equal triangle (via I.38, I.34, CN1, CN2) and then applies I.44 to the given line GF, followed by collinearity verification (I.29, I.14) and parallelogram completion (I.30, I.31). Since I.45's own proof uses I.44 internally along with I.29, I.14, I.30, I.34, CN1, and CN2, the AI is re-deriving the internals of I.45 rather than citing it as a unit. The additional ai_only citations 5.7 and 5.11 make explicit the ratio substitution that Heath handles informally. All key intermediate conclusions match at the same logical positions, making this a citation-depth difference (Case A), hence G.

### 11.33
**Category**: Granularity difference
**Jaccard**: 0.227
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: constructing auxiliary solid KP equal and similar to CD by extending sides AE, GE, HE and cutting off segments equal to CF, FN, FR; establishing the continuous proportion AG:GK = GK:KL = QE:KM via VI.1; converting to the solid ratio AB:EO = EO:QL = QL:KP via XI.32; and applying V.Def.10 for the triplicate ratio. The heath_only set is empty, confirming the AI cites every reference Heath uses. The 17 ai_only items are entirely construction propositions (1.3, 1.31, P1, P2), basic geometric results (1.15, 1.29, 1.34, 1.4, 11.10), proportion-theory lemmas (5.7, 5.11, 5.16), common notions (CN1, CN2, CN3), and definitions (D11.9, D6.1), all representing finer citation granularity for steps Heath treats as understood. The AI even includes a full lemma (Step 4) proving that parallelograms with equal adjacent sides and included angles are equal and similar, which Heath states without proof. This is a clear case of same backbone with different citation depth.

### 11.34
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs share the same backbone structure: a right-angle case (with equal-base and unequal-base sub-cases for both directions of the biconditional) followed by an oblique case reduced to the right-angle case via perpendiculars and XI.29/30. The key intermediate conclusions are identical in both proofs: (1) AB:CV = EH:NQ from 11.32, (2) CD:CV = CM:CT, and (3) the oblique-to-right-angle reduction. The two heath_only items represent depth differences, not backbone differences: Heath uses 11.25 to obtain CD:CV = MQ:TQ by cutting with a parallel plane, whereas the AI uses 11.32 by reorienting which face is considered the base (Step 8), reaching the same proportion; Heath uses 11.31 directly for the equal-base sub-case, whereas the AI derives the same equality through 11.32 and proportion theory (5.9). The ten ai_only items are construction propositions (1.3, 1.31, 11.11, 11.15, 11.24, 11.6), proportion-chain intermediates (5.11), axioms (CN1), and definitions (D5.5, D6.4) that Heath applies implicitly. Same backbone, different citation depth: G.

### 11.35
**Category**: Granularity difference
**Jaccard**: 0.316
**Analysis**: Q2 decided this classification. Both proofs follow an identical logical backbone: construct AH equal to DM, show HK perpendicular to the plane via XI.8, establish that angles HCA and MFD are right via I.47 and I.48, prove AC equal to DF and AB equal to DE by AAS congruence (I.26), derive BC equal to EF by SAS (I.4), decompose the right angles to get equal remaining angles, use a second AAS (I.26) to get CK equal to FN, apply SAS (I.4) to get AK equal to DN, use the Pythagorean theorem to show HK equal to MN, and finally conclude angle HAK equals angle MDN by SSS (I.8). The ai_only set consists entirely of construction propositions (1.3, 1.12, 1.31, 11.11), foundational planarity results (11.2, 1.30), definitions (D1.23, D11.3), common notions (CN1, CN2, CN3), and postulates (P1, P4), all of which Heath leaves implicit. The heath_only set is empty, confirming the AI cites every proposition Heath cites plus additional lower-level justifications. This is a textbook case of over-citation at the same logical depth, yielding G.

### 11.36
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs construct two parallelepipedal solids (EK equilateral on the mean B, and LH formed from A, B, C) with equal solid angles, then establish identical key intermediate conclusions in the same order: (1) reciprocal proportionality of sides about equal angles NLM and DEF, (2) equality of parallelograms MN and DF via 6.14, (3) equality of perpendicular heights via 11.35 Porism, and (4) equality of the solids via 11.31. The AI cites additional construction propositions (1.3, 11.26), proportion lemmas (5.7, 5.11), and a common notion (CN1) that Heath leaves implicit, while heath_only is empty, confirming that every proposition Heath cites is also cited by the AI. This is a classic Case A granularity difference: same logical backbone with the AI citing at finer depth.

### 11.37
**Category**: Path difference
**Jaccard**: 0.077
**Analysis**: Q2 decided the classification. For Part 1 (the forward direction), both proofs share the same backbone: each establishes that KA:LC is the triplicate of AB:CD and ME:NG is the triplicate of EF:GH via XI.33, then concludes the solid ratios are equal. However, for Part 2 (the converse), the AI takes a fundamentally different path from Heath. Heath simply reverses the triplicate ratio argument directly, while the AI constructs a fourth proportional O (6.12), builds a similar solid PO on O (11.27), applies Part 1 to deduce ME:PO = KA:LC = ME:NG, concludes NG = PO (5.9), establishes similarity of NG and PO (6.21, D11.9), and then proves GH = O through an elaborate indirect argument using 5.14. These key intermediate conclusions -- the construction of O and PO, the equality NG = PO, and the indirect proof that GH = O -- are entirely absent from Heath's proof. The AI's different path is logically complete and valid (Q3 holds), yielding category D.

### 11.38
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: they establish that midpoint-connecting segments form straight lines through triangle congruence, show that key diagonals across the cube are equal and parallel using XI.9 and I.33, and then use congruent triangles at the intersection point T (via alternate angles I.29, vertical angles I.15, and ASA congruence I.26) to conclude that the common section and the diameter bisect one another. The AI proof adds four citations not in Heath (1.13 for supplementary angles, 11.3 for plane intersections yielding lines, 11.7 for lines lying in planes of parallels, and D11.25 for the definition of a cube), all of which are foundational or constructive facts that Heath leaves implicit. Since heath_only is empty and the AI's extra citations are all over-citations of foundational material rather than substantive path differences, this is Case A of Q2: same backbone with different citation depth.

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical path: complete parallelepipedal solids on each base, establish that the base parallelograms are equal (using I.34), apply XI.31 to conclude the completed solids are equal, then use XI.28 to show each prism is half its respective solid, yielding equality of the prisms. The AI proof cites the same three substantive propositions as Heath (1.34, 11.28, 11.31) and adds explicit references to common notions (CN1, CN2, CN5) and a definition (D11.13) that Heath uses implicitly. The heath_only set is empty, confirming no missing steps. This is Case A of Q2: same backbone, different citation depth, yielding G.


---

## Book 12 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 17 | 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 12.10, 12.11, 12.12, 12.13, 12.14, 12.15, 12.17, 12.18 |
| Path difference (D) | 1 | 12.16 |
| AI proof error (E) | 0 |  |

**Total**: 18 propositions

## Per-Proposition Analysis

### 12.1
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that triangles BAE/GFL are equiangular via VI.6, use the same-segment angle theorem to transfer angles (AI cites 3.21, Heath cites 3.27 for the identical geometric fact), prove triangles ABM/FGN equiangular via III.31 and I.32, and derive the proportion BM:GN = BA:GF via VI.4. The only substantive citation difference is at the final deductive step: Heath invokes 6.20 (duplicate ratio of similar polygons) while the AI invokes 5.16 (alternation) and 6.22 (proportional similar figures on proportional lines) to reach the same conclusion. Since all key intermediate conclusions are identical and the differences amount to alternative citations at the same logical junctures plus over-citation of axioms (CN1, CN2, CN3, P1, P4, D4.3), this is Case A of Q2: same backbone, different citation depth.

### 12.2
**Category**: Granularity difference
**Jaccard**: 0.080
**Analysis**: Q2 decided the classification. Both proofs follow the same exhaustion backbone: assume the ratio of circles differs from the ratio of squares on diameters, consider S less than and greater than the second circle, inscribe polygons that exhaust more than half the remaining area via 10.1, inscribe a similar polygon in the other circle, use 12.1 to relate the polygons as the squares on diameters, and derive a contradiction via proportion theory. Every key intermediate conclusion is identical. The sole heath_only item (5.16, alternando) is a tactical choice: Heath alternates the proportion before applying the greater-than inference, while the AI applies 5.14 directly to the original proportion to reach the same conclusion (S > polygon). The 22 ai_only items are entirely construction-level sub-steps (1.11, 1.27, 1.31, 1.5, 3.1, 3.16, 3.27-3.32, 4.6, P1), common notions (CN1, CN5), definitions (D1.22, D6.1), and supporting results (1.32, 1.41, 10.1, 5.7, 5.14) that Heath performs implicitly. This is Case A: same backbone, different citation depth.

### 12.3
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing midpoints of all six edges, establishing parallelisms via VI.2, proving four pairs of face congruences via I.4 and XI.10, concluding sub-pyramid equality via XI.Def.10, establishing similarity of each sub-pyramid to the whole, proving prism equality via XI.39, and showing the prisms exceed half the pyramid. The heath_only set is empty, meaning the AI cites every proposition Heath does. The 14 ai_only items are all construction-level citations (1.10, P1), common notions (CN1, CN5), definitions (D11.12, D11.13, D11.9), and sub-step propositions that Heath invokes implicitly (1.38, 1.41, 1.8, 11.15, 11.9, 5.15, 6.5). The AI's use of 5.15 and 6.5 for the similarity argument rather than Heath's I.29 approach reaches the identical intermediate conclusion (face similarity to the whole) via a slightly different sub-route, which is a citation-depth difference, not a backbone difference. This is Case A of Q2: same key intermediate conclusions, different citation depth.

### 12.4
**Category**: Granularity difference
**Jaccard**: 0.190
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they divide the pyramids per XII.3, establish the similarity of sub-triangles LOC to ABC and RVF to DEF, derive the base ratio ABC:DEF = LOC:RVF via VI.22 and V.16, show that the prism ratio equals the base ratio (via the Lemma following XII.3), combine the two types of prisms in each pyramid, and conclude by induction. The sole heath_only citation XI.39 is used by Heath to directly relate the parallelogram-based prism to the triangle-based prism; the AI reaches the same conclusion instead through the equality of prisms I and II from XII.3 combined with ratio properties V.7 and V.11. The 16 ai_only items consist of construction citations (1.29, 1.31, 6.2), similarity-establishment steps (6.4, D6.1, D5.5), and the internal machinery of the Lemma proof (11.11, 11.17, 11.28, 11.32, 1.34, D11.13, D6.4), all of which support the same intermediate conclusions Heath states more tersely. This is Case A of Q2: same backbone, different citation depth.

### 12.5
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical exhaustion structure: assume the ratio fails, subdivide pyramids via 12.3, apply the exhaustion principle 10.1 to get prisms exceeding a hypothetical solid W, use 12.4 to establish that prisms are in the ratio of the bases, derive a contradiction for the case W < DEFH, then handle W > DEFH by inverting proportions and reducing to the first case via the 12.2 Lemma. The key intermediate conclusions are the same at every stage. The citation differences are entirely within proportion theory: the AI uses 5.14 directly (if first > third then second > fourth) instead of Heath's 5.16 (alternation) followed by an implicit ordering step, achieving the same inequality W > prisms in DEFH by a slightly more direct route. The AI also explicitly cites 5.11 for transitivity of ratios where Heath's corresponding step is recorded as 5.2, and cites CN5 and the Porism to 5.7 for steps Heath treats as implicit. All differences are citation-depth variations at identical logical positions, making this Case A of Q2: same backbone, different depth.

### 12.6
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: decomposing polygonal pyramids into triangular ones via diagonals, then iterating XII.5 (triangular pyramids of same height are as their bases) with V.18 (componendo) and V.22 (ex aequali) to build up the ratio from individual triangular pyramids to the full polygonal pyramids. The key intermediate conclusions are identical in both proofs, established in the same order. The ai_only set consists entirely of over-citations: definitions (D11.12, D6.4), a postulate (P1), and a basic proportion result (5.7) used to explicitly invert a ratio that Heath performs implicitly. Heath_only is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 12.7
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: they bisect parallelograms ABED and BCFE via their diagonals BD and CE using I.34 to obtain equal triangles, then apply XII.5 to equate pyramids with those equal bases and the same height, and finally note that the middle pyramid is the same solid viewed from two different bases to chain the equalities by transitivity. The AI's five extra citations (11.2, CN1, D11.12, D11.13, P1) are all definitions, common notions, postulates, or a basic plane-existence proposition that Heath uses implicitly without citation. Since heath_only is empty and the ai_only items are purely foundational over-citations with no substantive divergence in the argument, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct parallelepipeds on the two similar pyramids, show the corresponding parallelograms are similar (from the angle and side-ratio conditions of pyramid similarity), conclude the solids are similar and hence in the triplicate ratio of corresponding sides by XI.33, then note each pyramid is one-sixth of its parallelepiped (half by XI.28 gives a prism, one-third by XII.7 gives the pyramid) to transfer the triplicate ratio to the pyramids. The AI cites all four of Heath's references (11.24, 11.28, 11.33, 12.7) plus ten additional lower-level items: construction propositions (1.29, 1.31, 1.34), ratio-manipulation results (5.11, 5.15), a similarity-transitivity lemma (6.21), common notions (CN1, CN3), and definitions (D11.9, D6.1). These fill in steps Heath treats as obvious, and heath_only is empty, confirming identical logical structure at different citation depth.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decides this as Granularity difference (G). Both proofs establish the same biconditional through identical key intermediate conclusions: completing parallelepipeds around the pyramids, showing each parallelepiped equals six times its pyramid, applying XI.34 to relate bases and heights of equal parallelepipeds, and converting between parallelogram and triangle bases via proportionality. The AI proof follows exactly Heath's logical backbone in both directions but cites construction steps (1.31, 11.15, 11.28), the pyramid-to-parallelepiped relationship (12.7), ratio manipulation lemmas (5.15, 5.7, 5.9), common notions (CN1, CN2), and a definition (D6.4) that Heath leaves implicit. Since heath_only is empty, every proposition Heath cites also appears in the AI's citation set, confirming that the AI merely over-cites rather than taking a different path.

### 12.10
**Category**: Granularity difference
**Jaccard**: 0.238
**Analysis**: Q2 decided the classification. Both proofs use identical double reductio ad absurdum structure: Case 1 assumes the cylinder exceeds triple the cone and derives a contradiction via exhaustion, Case 2 assumes the cylinder is less than triple and derives a contradiction similarly. The key intermediate conclusions match exactly: inscribed square exceeds half the circle, each inscribed triangle exceeds half its circle segment, prisms/pyramids on triangles exceed half the corresponding cylinder/cone segments, exhaustion (10.1) reduces leftover segments below any given excess, and prism on polygon equals triple the pyramid on the same polygon (12.7). The sole heath_only citation 12.2 is accounted for by the AI re-deriving the triangle-exceeds-half-segment lemma from elementary constructions (Steps 5-6 using 1.34, 3.16, etc.) rather than citing the prior result. The large ai_only set consists of construction propositions (1.29, 1.31, 1.34, 3.1, 3.16, 3.30, P1), definitions and common notions (CN2, CN5, D11.18, D11.21, D3.2), and props like 11.28 and 12.6 that provide directly what Heath derives through 11.32 and taking thirds. All differences are citation-depth, not backbone differences, yielding Case A of Q2.

### 12.11
**Category**: Granularity difference
**Jaccard**: 0.207
**Analysis**: Q2 decided the classification. Both proofs follow the same double reductio by exhaustion structure: assume the ratio of circles does not equal the ratio of cones, consider O less than cone EN, inscribe polygons and build pyramids approximating the cone, use X.1 to make remaining segments arbitrarily small, establish the proportion cone AL : O :: pyramid_L : pyramid_N via XII.1, XII.2, XII.6, and V.11, derive that O > pyramid_N (contradicting pyramid_N > O from the exhaustion), then handle the symmetric case and the case O > cone EN by reduction. The cylinder extension uses XII.10 in both. The sole heath_only citation is V.16 (alternando), which Heath uses to rearrange the proportion before comparing magnitudes; the AI instead applies V.14 directly to the same proportion to reach the identical conclusion. This is a different ratio-theorem tool at the same logical position, not a different backbone. The 22 ai_only items are entirely definitions (D11.18, D11.19, D11.20, D11.23, D3.2, D6.4), common notions (CN3, CN5), a postulate (P1), construction propositions (4.6, 4.7, 3.30, 1.31, 3.17), elementary geometry (1.28, 1.41, 1.47, 3.1, 3.18), and ratio theorems (5.7, 5.14, 5.15) that Heath leaves implicit. Case A of Q2 holds: same backbone, different citation depth.

### 12.12
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same method-of-exhaustion argument: they assume the triplicate ratio holds to a solid O less than (then greater than) the second cone, inscribe polygons in the base circles, prove similarity of corresponding triangular pyramids via triangle similarity (VI.6, VI.5), apply XII.8 for the triplicate ratio of similar pyramids, sum the ratios via V.12, reach a contradiction, handle the symmetric and greater-than cases, and extend to cylinders via XII.10. The key intermediate conclusions are identical throughout. The AI proof over-cites by explicitly referencing 30 additional items -- definitions (D1.15, D1.22, D11.18-23, D5.10, D5.13, D5.5), postulates (P1, P4), common notions (CN5), lower-level construction propositions (1.11, 1.28, 1.31, 1.41, 1.47, 3.1, 3.16, 3.27, 3.30, 4.7), intermediate proportion-theory steps (5.7, 5.11, 5.14, 5.15), 6.4, and 12.6 -- that Heath uses implicitly. Since heath_only is empty, every Heath reference appears in the AI set, and the symmetric difference is entirely one-sided, confirming citation-depth difference rather than path divergence.

### 12.13
**Category**: Granularity difference
**Jaccard**: 0.133
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they use XII.11 to relate cylinders with equal axes to their bases, conclude that cylinders with equal axes and equal bases are equal, establish the equimultiple relationship between axes and cylinders, perform the three-case comparison (equal, greater, less), and apply V.Def.5 to conclude the proportion. The AI proof adds substantial explicit detail (proving the axis is perpendicular to the bases, showing that parallel planes produce equal circles via 11.16 and 1.34, citing definitions D11.21-23 and common notions CN1, CN5), but these are constructive sub-steps and over-citations, not different key conclusions. Heath_only is empty, confirming that no substantive content is missing from the AI proof. The large ai_only set consists entirely of definitions, common notions, postulates, and elementary construction propositions that Heath leaves implicit, which is the hallmark of a granularity difference.

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.130
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a cylinder CM with axis LN equal to axis GH, show EB equals CM via equal heights and equal bases (12.11), derive CM:FD = LN:KL by cutting cylinder FM with a parallel plane (12.13), substitute to get EB:FD = GH:KL, and extend to cones via 12.10. The AI proof follows this identical chain but provides far more granular justification, explicitly citing Book 1 construction propositions (1.3, 1.13, 1.28, 1.33, 1.34) for building the rectangle LNMD, definitions (D11.18-D11.23, D11.3, D5.5, D6.4) for describing the solids, Book 11.14 for parallel planes, postulates (P1, P2) for basic constructions, and proportion theory results (5.7, 5.11, 5.15) for ratio manipulations that Heath performs implicitly. Since heath_only is empty and all ai_only items are lower-level support for the same key conclusions, this is a pure citation-depth difference (Case A), yielding G.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.267
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: construct an auxiliary solid ES on the same base as EO with height equal to KL, establish that AX:ES equals the ratio of the bases via 12.11, establish that EO:ES equals the ratio of the heights, then chain these ratios for the forward direction (using 5.7 and 5.11) and the converse (using 5.11 and 5.9). The sole substantive citation difference is that the AI cites 12.14 (cones and cylinders on equal bases are proportional to heights) where Heath cites 12.13 (cutting a cylinder by a parallel plane gives axis-proportional sub-cylinders). The proof-tree containment test confirms that 12.13 appears inside Heath's proof of 12.14, so the AI is citing 12.14 as a unit while Heath re-derives 12.13's content inline. The remaining ai_only items are definitions (D11.18-D11.23, D5.5, D6.2) and a construction proposition (1.3), all representing over-citation rather than path divergence. The AI's unified treatment of the equal-height and unequal-height cases is a presentational choice that does not alter the backbone.

### 12.16
**Category**: Path difference
**Jaccard**: 0.036
**Analysis**: Q2 decided the classification. Heath's proof establishes that the inscribed polygon does not touch the lesser circle by a tangent-parallelism argument: AC is tangent to the lesser circle (III.16), LD equals DN (III.3, I.4), LN is parallel to AC, and therefore LN does not touch the lesser circle. The AI proof takes a fundamentally different route based on distance from center: it shows LD < AC by comparing triangles KLD and KAC with unequal included angles (1.24), then proves via contradiction using 3.14 and 3.15 that the perpendicular from the center to LD exceeds the perpendicular from the center to AC (which equals the lesser circle's radius), and finally argues that every point of every side of the polygon is farther from the center than the lesser radius using the perpendicular-hypotenuse relationship (1.17, 1.19). These are genuinely different key intermediate conclusions -- tangency and parallelism versus chord-distance comparison and point-by-point distance bounding -- making this Case B (different backbone) in Q2. The AI's path is logically complete and sound under Q3, so the classification is D.

### 12.17
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: inscribing an equilateral polygon in the greater circle that does not touch the lesser (via 12.16), erecting a perpendicular to define great-circle semicircles, fitting equal chords and proving the parallelism and planarity of the quadrilateral faces, constructing the polyhedral solid of pyramids, and then proving AX > AZ > AG through the chain BK^2 > 2*BY^2 (from the obtuse angle at Y) and BK^2 < 2*KZ^2 (from similar triangles on the perpendicular KZ to BD). The heath_only set is empty, meaning every proposition Heath cites is also cited by the AI. The 32 ai_only items consist of construction propositions (1.11, 1.12), definitions (D1.11, D1.15, D1.16, D3.1, D11.12, D11.16), common notions (CN3, CN5), postulates (P1, P2, P4), and substantive propositions that Heath uses implicitly (e.g., 1.5, 1.8, 2.12, 3.26, 3.28, 5.7, 6.4, 12.16). The AI proof follows the same logical backbone as Heath but makes every intermediate step and its justification explicit, which is a pure citation-depth difference.

### 12.18
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs follow the same double reductio ad absurdum structure with identical key intermediate conclusions: inscribe a polyhedral solid in the larger sphere that does not touch the smaller (12.17), establish the triplicate ratio of the polyhedra (12.17 Porism), derive the proportion equality between spheres and polyhedra, show the smaller sphere is both greater and less than the polyhedron (contradiction), and reduce the greater-sphere case to the lesser-sphere case. The sole differences are in which Book V proportion-theory tools are invoked: Heath uses V.16 (alternation) to rearrange the proportion and XII.2 Lemma to handle the greater-sphere reduction, while the AI uses V.11 (transitivity of equal ratios) and V.14 (ordering in proportions) for the proportion steps, V.7 Porism (inversion) and D5.10 (definition of triplicate ratio) to work through the greater-sphere reduction explicitly, and CN5 (whole greater than part) for the inequality. Since the backbone of key geometric conclusions is the same and only the specific proportion-theory machinery differs, this is a citation-depth difference (Case A), yielding G.


---

## Book 13 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 12 | 13.3, 13.6, 13.8, 13.9, 13.10, 13.11, 13.13, 13.14, 13.15, 13.16, 13.17, 13.18 |
| Path difference (D) | 6 | 13.1, 13.2, 13.4, 13.5, 13.7, 13.12 |
| AI proof error (E) | 0 |  |

**Total**: 18 propositions

## Per-Proposition Analysis

### 13.1
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof constructs geometric squares and a gnomon figure, using VI.1 (triangles under the same height are proportional to their bases) to establish that CK is double CH, then shows the whole square AE equals the gnomon MNO, and derives the 5:1 ratio through gnomon arithmetic. The AI proof takes a fundamentally different algebraic route using Book II area identities: it applies 2.2 to get rect(AB,AC) + sq(AC) = sq(AB), applies 2.4 to decompose sq(DC) into sq(DA) + sq(AC) + 2*rect(DA,AC), uses 2.1 to show rect(AB,AC) = 2*rect(DA,AC), and uses 2.4 again to show sq(AB) = 4*sq(AD), then combines these to reach sq(DC) = 5*sq(AD). The two proofs share only the initial step of converting the extreme-and-mean-ratio definition into rect(AB,CB) = sq(AC) via D6.3 and 6.17; after that, the key intermediate conclusions diverge entirely. Heath's use of VI.1 for proportional areas within a constructed figure has no counterpart in the AI proof, and the AI's Book II decompositions have no counterpart in Heath. This is a genuine path difference (Case B in Q2), and Q3 confirms the AI's path is logically complete and valid.

### 13.2
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q1 found no logical errors in the AI proof; every step follows validly from the preceding ones. Q2 identified different backbones (Case B): Heath proves rect(CD,DB) = CB squared through a geometric construction involving squares AF and CG, gnomon area manipulations, and the proportionality result VI.1 (triangles under the same height are proportional to their bases), while the AI derives the same key equality entirely through algebraic identities from Book 2 (II.4 for expanding squares of sums, II.1 for distributing rectangles, II.2 for another rectangle decomposition), plus an explicit proof by contradiction that CB < CD. The completely disjoint citation sets (Jaccard = 0.0) confirm the path divergence: Heath uses none of the Book 2 propositions, and the AI uses none of Heath's geometric proportionality machinery. Q3 verified that the AI's algebraic chain is logically complete, so the classification is D (path difference).

### 13.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs establish the same three key intermediate conclusions in the same logical order: (1) rect(AB,BC) = sq(AC) from the extreme and mean ratio property, (2) sq(AC) = 4*sq(DC) since AC = 2*DC, and (3) sq(DB) = rect(AB,BC) + sq(DC), combining to yield sq(DB) = 5*sq(DC). Heath reaches these through geometric area manipulation within a constructed figure (gnomons and square regions), while the AI cites explicit propositions (6.17, 2.4, 2.6) for the same steps. The Jaccard of 0.0 is an artifact of Heath's proof having no extracted references; all AI citations (1.10, 2.4, 2.6, 6.17, CN1, CN2, D1.22, D6.3) make explicit what Heath uses implicitly, constituting a citation-depth difference rather than a path divergence.

### 13.4
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the initial key conclusion that rect(AB,BC) = sq(AC) via the golden ratio definition and 6.17, but their backbones diverge after that point. Heath constructs the square on AB and argues through a gnomon decomposition of areas within the figure, while the AI takes a purely algebraic route using 2.3 to decompose rect(AB,CB) into rect(AC,CB) + sq(CB), then 2.4 to expand sq(AB), and substitutes to reach the triple relation. The AI's intermediate conclusion rect(AC,CB) + sq(CB) = sq(AC) has no counterpart in Heath, and Heath's gnomon argument has no counterpart in the AI proof. Since the backbones differ and the AI's algebraic path is logically complete and valid (Q3), the classification is D.

### 13.5
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: The classification hinges on Q2 (backbone comparison). Heath's proof converts the extreme-and-mean-ratio proportion into an area equality via 6.17, constructs a square on AB and manipulates the resulting rectangles geometrically (showing rect(BD,DA) = sq(AB) through figure-based area additions), then converts back to a proportion using 6.17. The AI proof stays entirely within the domain of proportions, applying Book 5 ratio manipulations -- inversion (5.7 Porism), transitivity (5.11), and componendo (5.18) -- to transform the initial EMR proportion AB:AC :: AC:CB directly into the target proportion DB:AB :: AB:AD without ever passing through areas. These are genuinely different key intermediate conclusions: Heath argues through area equalities (rect(AB,BC)=sq(AC) and rect(BD,DA)=sq(AB)), while the AI argues through intermediate ratio chains (AC:AB :: CB:AC, then AD:AB :: CB:AC, then DB:AB :: AB:AC). The AI's purely proportional path is logically complete and valid, warranting classification as D (Path difference).

### 13.6
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: sq(CD) = 5*sq(DA) via 13.1, commensurability of sq(CD) and sq(DA) via 10.6, rationality of DA and CD, incommensurability of CD and DA in length via 10.9, AC is an apotome via 10.73, rect(AB,BC) = sq(AC) via 6.17, and CB is a first apotome via 10.97. The backbones are identical. The AI proof adds over-citations for construction steps (1.10, 1.3), a postulate (P2), definitions (D10.1.2, D10.1.3, D10.3.1), and one intermediate result for transitivity of commensurability (10.12), all of which Heath leaves implicit. Since heath_only is empty, every proposition Heath cites also appears in the AI proof. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 13.7
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Heath's Case 1 proof works by joining diagonals AC and BE, showing they are equal (I.4), then using their intersection point F to derive AF=BF via I.6 (converse of the isosceles triangle theorem), subtracting to get FC=FE, and applying I.8 on triangles FCD and FED. The AI's Case 1 proof takes a fundamentally different route: it joins AC, BD, and AD, shows AC=DB via I.4 on triangles ABC and DCB, then applies I.8 on triangles ACD and DBA to get angle CDA = angle BAD, invokes I.5 on triangle EAD, and adds equal angles via CN2 to conclude angle CDE = angle BAE. The AI never introduces the intersection point F and never uses I.6, instead relying on a different set of triangle congruences (I.8 applied to different triangle pairs) combined with the isosceles triangle theorem (I.5) and angle addition (CN2). Heath's unique citation I.6 reflects a genuinely different logical backbone, not mere citation-depth variation. The AI's second case also differs: it reduces the non-consecutive case to the consecutive case by showing angle C = angle B, whereas Heath proves the non-consecutive case independently using I.4 and I.5 on different triangles. Both proofs are logically complete, covering both required cases, but through different key intermediate conclusions.

### 13.8
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: BE=AC by I.4, angle AHE = 2*angle BAH by I.32, angle EAC = 2*angle BAC, HE=EA=AB by I.6, triangles ABE and ABH equiangular yielding EB:BA=AB:BH by VI.4, and BE:EH=EH:HB with V.14 giving extreme and mean ratio. The sole heath_only citation (VI.33) passes the proof-tree containment test: III.27, which the AI cites instead, appears inside Heath's proof of VI.33, so the AI re-derives the needed special case from the more elementary equal-arc-equal-angle result rather than invoking the general proportionality theorem. The remaining ai_only items are Common Notions (CN1, CN2, CN3, CN5), a definition (D6.3), a postulate (P1), and proportion-manipulation lemmas (5.7, 5.11) that Heath applies implicitly. The AI also explicitly proves the AC case (Steps 11-12) where Heath says 'similarly'. All differences are citation-depth differences within the same logical backbone, yielding G.

### 13.9
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: arc AC equals four times arc CB, angle AEC equals four times angle CEB (via 6.33), angle AEC equals twice angle ECB (via 1.5 and 1.32), EC equals CD as both equal the radius (via 4.15), angle ECB equals twice angle EDC (via 1.5 and 1.32), angle EDC equals angle BEC, triangles EBD and EBC are equiangular, DB:BE equals EB:BC (via 6.4), and BD:DC equals DC:CB by substituting EB for CD. The logical backbone is the same in both proofs. The AI's 13 extra citations (ai_only) are entirely construction propositions (3.1, P1, P2), definitions (D1.15, D1.17, D6.3), common notions (CN1, CN3, CN5), and auxiliary proportion results (3.28, 5.7, 5.11, 5.14) that Heath leaves implicit. The heath_only set is empty, confirming the AI cites everything Heath does plus additional granularity. This is Case A of Q2: same backbone, different citation depth.

### 13.10
**Category**: Granularity difference
**Jaccard**: 0.409
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish arc relationships showing AK is a decagon side, derive angle relationships leading to triangle ABF being similar to triangle BFN (yielding rect(AB,BN) = sq(BF)), prove triangle KBA similar to triangle KNA (yielding rect(BA,AN) = sq(AK)), and combine these via II.2 to reach sq(AB) = sq(BF) + sq(AK). The key intermediate conclusions are identical at every stage. The citation differences are purely depth-related: the AI's 12 additional citations (1.12, 3.1, 3.28, 3.29, 3.3, CN1-3, D1.10, D1.17, P1, P2) are all construction propositions, basic circle theorems, common notions, definitions, and postulates that Heath uses implicitly. The sole heath_only citation (1.26, ASA congruence) is replaced by the AI's use of 1.4 (SAS congruence) at the same logical position to reach the same conclusion (angle AFK = angle KFB), a micro-level substitution of congruence criteria that does not alter the backbone. This is Case A of Q2: same backbone, different citation depth.

### 13.11
**Category**: Granularity difference
**Jaccard**: 0.209
**Analysis**: Q2 decided the classification. Both proofs establish the same sequence of key intermediate conclusions: FK=AF/4 with FK and BK rational, right angles at L and M with CD=2CL and AC=2CM, triangles ACL and AMF equiangular, the proportion DC:CM=MF:FK, componendo to (DC+CM):CM=MK:KF, the ratio of squares, sq(MK)=5*sq(KF) via XIII.8 and XIII.1, MK rational, sq(BK)=5*sq(MK) with BK incommensurable in length with KM, MB as a fourth apotome via X.73, and finally sq(side)=BH*BM yielding the side as minor via X.94. The two heath_only citations (10.15 and 5.19) are sub-step tools whose underlying conclusions appear in both proofs at the same logical positions: Heath uses X.15 to show BK commensurable with BH while the AI establishes this directly via arithmetic (BK=5FK, FK measures BH), and Heath uses V.19 (convertendo) while the AI computes sq(BK)-sq(MK)=4*sq(MK) directly. The 32 ai_only items are overwhelmingly construction propositions, definitions, postulates, common notions, and lower-level ratio tools that fill in steps Heath leaves implicit. This is Case A: same backbone, different citation depth.

### 13.12
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs reach the same ultimate conclusion (AB^2 = 3DE^2) and share the final algebraic steps (angle ABE right via 3.31, Pythagorean theorem via 1.47, AE^2 = 4DE^2). However, the key intermediate lemma BE = DE is established through fundamentally different mathematical techniques: Heath uses arc reasoning and the hexagon property (4.15), showing that arc BE is 1/6 of the circle so BE equals the radius, while the AI uses angle-at-center reasoning (3.20, 1.13, 1.5, 1.6, 1.32), showing through angle-chasing that triangle BDE has all angles equal to angle ACB and therefore BE = DE. The containment test fails because the AI does not cite a higher-level proposition subsuming 4.15 but instead employs entirely different geometric concepts (central angles vs. arcs/hexagons). The AI's sub-proof tools (3.20, 1.13, 1.6) are largely absent from Heath's proof of 4.15 (which uses 3.26, 3.27, 3.29, 1.15). Since the backbones diverge in their indispensable intermediate facts, this is Case B (different backbone). Q3 confirms the AI's path is logically complete and valid, yielding D.

### 13.13
**Category**: Granularity difference
**Jaccard**: 0.258
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: cutting the diameter so AC = 2CB, establishing sq(AD) = 3 sq(CD) via the semicircle construction, inscribing equilateral triangle EFG in a circle of radius CD, using XIII.12 to show AD = EF, proving all six edges equal via I.4 to construct the pyramid, comprehending it in the sphere with diameter KL = AB, and proving the 3:2 ratio of squares. The AI's 22 extra citations are overwhelmingly over-citations: postulates (P1-P4), common notions (CN1, CN2), definitions (D1.15, D11.12, D11.14, D11.17), construction propositions (1.1, 1.3, 1.10, 1.11), and elementary results (1.5, 1.6, 1.13, 6.9) that Heath leaves implicit. The AI's use of II.5 and I.47 for the sphere-comprehension argument (versus Heath's more compact VI.8/III.31 approach) and 6.1/6.4 for explicit proportion steps represent sub-argument detail, not a different logical path. The sole heath_only item (III.1, finding the center of a circle) is avoided because the AI constructs the circle with center H from the start rather than finding the center afterward. All key conclusions appear at the same logical positions in both proofs.

### 13.14
**Category**: Granularity difference
**Jaccard**: 0.160
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing square EFGH with side equal to DB, erecting perpendiculars KL and KM from the center K, using I.47 to show sq(EH) = 2*sq(EK) and sq(LE) = 2*sq(EK) hence LE = EH, concluding all eight triangles are equilateral to form the octahedron, comprehending it in a sphere via semicircle rotation (KL=KM=KE), then establishing sq(LM) = 2*sq(LE) via III.31 and I.47, and sq(AB) = 2*sq(DB) to conclude LM = AB. The heath_only set is empty, meaning every proposition Heath cites (I.4, I.47, XI.12, III.31) is also cited by the AI. The ai_only set consists entirely of postulates (P1, P2, P3), definitions (D1.15, D1.17, D1.18, D1.20, D1.22, D11.14, D11.17, D11.26, D11.3), common notion (CN1), and basic construction and triangle propositions (1.3, 1.5, 1.6, 1.8, 1.10, 1.11, 1.32, 1.46), all of which are elementary steps that Heath uses implicitly. The AI's slightly different sub-derivation of sq(AB) = 2*sq(DB) (using I.4 to show AD = DB directly, rather than Heath's proportional route) reaches the same key conclusion and does not alter the backbone. This is Case A: same backbone, different citation depth.

### 13.15
**Category**: Granularity difference
**Jaccard**: 0.065
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: setting up the diameter and establishing sq(AB) = 3*sq(BD) via the semicircle construction, constructing the cube with side equal to DB, proving all eight vertices lie on a sphere with diameter KG by showing each angle subtended at a vertex is right, proving sq(KG) = 3*sq(EF) via the Pythagorean theorem, and concluding KG = AB. The heath_only set is empty, meaning Heath's two citations (I.47 and XI.Def.3) are a strict subset of the AI's 31 citations. The AI's 29 additional citations are all postulates (P1, P3), definitions (D1.18, D1.22, D1.23, D11.14, D11.17, D11.25, D5.5, D5.9), common notions (CN1), construction propositions (1.3, 1.10, 1.11, 1.46), Book 11 solid geometry fundamentals (11.4, 11.6, 11.7, 11.9, 11.10, 11.12), and standard theorems (1.28, 1.29, 1.33, 3.31, 5.11, 6.8, 6.9, 6.20) that Heath invokes implicitly. This is Case A of Q2: same backbone, different citation depth.

### 13.16
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs construct the icosahedron through identical key intermediate conclusions: cutting the diameter so the square on AB equals five times the square on BD, inscribing the pentagon and decagon in a circle of radius DB, raising perpendiculars to form the upper pentagon QRSTU, applying XIII.10 (the pentagon-hexagon-decagon relation) to verify that all connecting edges equal the pentagon side, constructing the 20 equilateral triangles in three bands (10 middle, 5 upper cap at Z, 5 lower cap at X), using XIII.9 and XIII.3 to establish the extreme-and-mean-ratio property for the sphere comprehension, proving XZ equals AB so the sphere matches the given sphere, and finally applying XIII.11 to classify the side as minor. The large ai_only set (29 items) consists entirely of postulates, common notions, definitions, and elementary construction or foundational theorems that Heath invokes without explicit citation. The sole heath_only item D5.9 (V. Def. 9, duplicate ratio) is a definition the AI covers through its direct use of 6.8. The identical logical backbone with differing citation depth places this squarely in Case A of Q2, yielding G.

### 13.17
**Category**: Granularity difference
**Jaccard**: 0.267
**Analysis**: Q2 decided the classification. Both proofs share an identical backbone: constructing a regular pentagon on a cube edge by bisecting sides, cutting segments in extreme and mean ratio, erecting perpendiculars, then proving the pentagon equilateral (via XIII.4, I.47), coplanar (via VI.32, XI.1), equiangular (via I.8, XIII.7), extending to all twelve edges for the dodecahedron, comprehending it in the sphere (via XI.38, XIII.15), and showing the side is an apotome (via V.15, XIII.6). heath_only is empty, meaning the AI cites every proposition Heath does. The 33 ai_only items consist entirely of definitions, common notions, postulates, basic construction propositions (1.3, 1.10, 1.29, 1.30, 1.33, 1.34, 6.30, 11.12), elementary computational and ratio results (2.4, 5.7, 5.11, 5.14), spatial propositions (11.7, 11.9), and one substantive reference (10.6) used to explicitly justify that the cube side is rational, a fact Heath also establishes at the same logical position but without naming the proposition. This is a pure over-citation pattern where the AI makes explicit every foundational step that Heath leaves implicit, yielding Case A of Q2: same backbone, different citation depth.

### 13.18
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs construct and identify the sides of all five Platonic solids inscribed in a sphere of diameter AB through the same sequence of key intermediate conclusions: AF as the pyramid side (via sq(AB) = 1.5 sq(AF) and 13.13), BF as the cube side (via sq(AB) = 3 sq(BF) and 13.15), BE as the octahedron side (via sq(AB) = 2 sq(BE) and 13.14), KL as the icosahedron-circle radius and hexagon side (via sq(AB) = 5 sq(KL) and 13.16), AK and LB as decagon sides, MB as the icosahedron side (via 13.10 and 13.16), and NB as the dodecahedron side (via 13.17). The comparison section and the proof that MB > NB follow the same logical chain. The heath_only set is empty, meaning every reference Heath cites is also cited by the AI. The 24 ai_only items are entirely construction propositions (1.10, 1.11, 1.12, 1.3), postulates (P1, P3, P4), common notions (CN1, CN2, CN3, CN5), definitions (D1.15, D1.18, D5.5, D5.9, D6.3, D10.1.2, D10.1.3), and elementary propositions (1.32, 1.47, 3.31, 6.17, 6.30, 6.9, 10.13) that Heath uses implicitly but does not cite. This is a clear Case A: same backbone, different citation depth.

