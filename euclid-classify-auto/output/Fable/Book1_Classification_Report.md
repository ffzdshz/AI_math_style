# Book 1 — Classification Report (Fable)

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
