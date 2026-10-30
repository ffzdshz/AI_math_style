# Book 12 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 7 | 12.6, 12.7, 12.8, 12.9, 12.10, 12.14, 12.15 |
| Path difference (D) | 11 | 12.1, 12.2, 12.3, 12.4, 12.5, 12.11, 12.12, 12.13, 12.16, 12.17, 12.18 |
| AI proof error (E) | 0 |  |

**Total**: 18 propositions

## Per-Proposition Analysis

### 12.1
**Category**: Path difference
**Jaccard**: 0.227
**Analysis**: The forward dependency gate passes (all citations are from Books 1-6). Q1 finds no logical error: the AI proof is complete and valid, with each step properly supported by citations. Q2 compares the backbones. Both proofs share the same early intermediate conclusions: equiangular triangles from polygon similarity (6.6), inscribed angle transfer (AI uses 3.21 where Heath uses 3.27 for the same geometric fact), and equiangular diameter-triangles giving side-to-diameter proportionality (6.4). However, they diverge at the final step: Heath invokes the duplicate ratio concept via 6.20 (similar polygons have to each other a ratio duplicate of corresponding sides), while the AI explicitly constructs squares on the diameters, shows they are similar, and applies 6.22 (proportional lines yield proportional similar figures). Since 6.20 and 6.22 are independent propositions -- neither contains the other in its proof tree -- and the duplicate ratio intermediate conclusion is present in Heath but absent from the AI, Case A of Q2 fails. Under Q3, the AI's different path is positionally valid and logically complete, yielding category D.

### 12.2
**Category**: Path difference
**Jaccard**: 0.036
**Analysis**: Q2 determined the classification. Heath proves XII.2 by the classical double reductio ad absurdum: assuming the ratio of circles equals the ratio of diameter-squares to a lesser area S, he inscribes polygons using exhaustion (10.1), applies XII.1 for similar polygon ratios, and uses proportion manipulation theorems V.11 (transitivity) and V.16 (alternando) to derive a contradiction, then repeats the argument for a greater area. The AI proof takes a fundamentally different path, directly verifying the equimultiple definition of proportion (D5.5): it inscribes and refines polygons showing P_j : Q_j = S : T at every stage by XII.1, uses exhaustion to make remainders arbitrarily small, and then for arbitrary positive integers m and n demonstrates that mC vs nD matches mS vs nT, concluding C : D = S : T without any reductio. Because the key intermediate conclusions differ -- Heath argues through contradiction via proportion manipulation while the AI argues through direct equimultiple verification -- this is a genuine path difference, and Q3 confirms the AI's chain is logically complete.

### 12.3
**Category**: Path difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs establish the same final conclusions (sub-pyramids equal and similar to each other and the whole; two equal prisms greater than half the whole), but the intermediate reasoning differs in two substantive ways. First, Heath uses XI.10 (equal angles from parallel lines in different planes) to establish face congruence via SAS (I.4), while the AI avoids XI.10 entirely by using edge proportionality and SSS similarity (6.5). Second, Heath establishes prism equality directly via XI.39, while the AI constructs a parallelepiped Z, bisects it using XI.28, and shows both prisms are halves of it via superposition (CN4). The AI's parallelepiped construction is an intermediate geometric object absent from Heath's proof, and the AI's method differs even from XI.39's internal proof (which constructs two parallelepipeds and uses XI.31, not one parallelepiped with superposition). Since the containment test fails for both heath_only items and the AI employs genuinely different geometric methods, Case A (same backbone) fails, yielding Case B. Under Q3, the AI's different path is logically complete and valid, so the classification is D.

### 12.4
**Category**: Path difference
**Jaccard**: 0.087
**Analysis**: Q2 decided the classification. Heath's proof establishes the base-to-prism ratio through similar triangles (VI.22) and alternando (V.16), connecting triangle ratios to prism ratios via the Lemma following XII.3 and using XI.39 to equate prisms with parallelogram and triangular bases. The AI proof takes a fundamentally different route: it computes the base area relationship directly using equal-altitude triangles (VI.1) applied twice to show the pyramid base is four times the prism base, then completes prisms to parallelepipeds (I.31, XI.28) and compares them using XI.32 (equal-height parallelepipeds proportional to bases), reducing back to prism ratios via V.15 and V.11. The heath_only citations (6.22, 5.16, 11.39) are not subsumed by any higher-level AI citation but are replaced by an entirely different proof strategy, confirming Case B (different backbone). Q3 confirms the AI's path is logically valid, with every step properly supported by cited propositions, yielding D.

### 12.5
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as Case B (different backbone), confirmed valid in Q3. Heath's proof proceeds by double reductio ad absurdum: it assumes the ratio of pyramids to bases equals a ratio to a hypothetical solid W less than (then greater than) the second pyramid, subdivides via XII.3, compares prism collections via XII.4, and derives contradictions using alternando (V.16), the XII.2 Lemma, and V.2. The AI proof takes a fundamentally different path: it directly verifies all three conditions of Definition V.5 (the Eudoxian definition of equal ratios) by showing that for arbitrary positive integers m and n, the ordering of mP vs nQ matches that of mA vs nB. The AI uses the same core exhaustion machinery (XII.3, XII.4, X.1) but deploys it within a direct equimultiple framework, employing V.11 (transitivity of ratios), V.19 (subtraction of proportional parts), and common notions for the algebraic manipulations. This is a genuinely different logical strategy — direct verification versus indirect contradiction — and the AI's chain from premises to conclusion is logically complete and sound.

### 12.6
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same geometric backbone: triangulate the polygonal bases, apply XII.5 to compare triangular pyramids of equal height, aggregate the triangular ratios to relate full polygonal pyramids, and conclude via V.22 (ex aequali). The sole substantive citation difference is that Heath uses V.18 (componendo) iteratively to build up polygon-to-triangle ratios one step at a time, while the AI uses V.24 (addendo, which adds antecedents with a fixed consequent) to sum all ratios at once. The proof-tree containment test confirms that V.18 appears inside Heath's own proof of V.24, so the AI is citing V.24 as a unit while Heath re-derives its internals inline. The remaining ai_only items (11.2, CN2, D11.12, D5.5, D6.4, P1) are all definitions, common notions, postulates, or construction-level citations, representing over-citation rather than a path divergence. Since the key geometric conclusions are the same and the citation difference is one of depth, this is a granularity difference.

### 12.7
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decides the classification. Both proofs share the same logical backbone: decompose the prism into three triangular pyramids, then establish pairwise equality by showing base triangles are equal halves of parallelogram faces (I.34) and applying the pyramid ratio result (XII.5). Though the AI uses different cutting diagonals (AF, BF, AE vs. Heath's BD, EC, CD), the key intermediate conclusions are structurally identical in both proofs. The ai_only set (11.2, CN1, D11.12, D11.13, D5.5, D6.4, P1) consists entirely of definitions, common notions, postulates, and one foundational Book 11 proposition, all of which Heath takes as implicit. With heath_only empty and the backbone the same, this is a citation-depth difference classifying as G.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct parallelepipeds on the similar pyramids, show these parallelepipeds are similar, apply XI.33 for the triplicate ratio of similar parallelepipeds, then use XI.28 and XII.7 to establish that each pyramid is one-sixth of its parallelepiped, and transfer the ratio. The sole heath_only citation, XI.24 (opposite faces of a parallelepiped are equal and similar), is used by Heath to help establish the similarity of the two parallelepipeds. The AI reaches the same conclusion by citing lower-level results: I.34 for opposite sides of parallelograms, I.29 for supplementary angles, XI.10 for dihedral angles, and the definitions D6.1 and D11.9 for similarity of figures and solids. The ai_only set consists entirely of definitions, common notions, construction propositions, parallelogram properties, and ratio algebra propositions that support the same key conclusions Heath establishes more tersely. This is Case A of Q2: same backbone, different citation depth.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct parallelepipeds around the pyramids, establish that each parallelepiped is six times its pyramid, apply XI.34 for reciprocal proportionality of parallelepipeds, connect parallelepiped bases to triangular bases via I.34, and chain ratio equalities to reach the conclusion, with the converse proved by reversing the argument. The heath_only citation (5.11, transitivity of equal ratios) is used by Heath to chain ratio equalities; the AI achieves the identical logical step using 5.15 (equimultiples preserve ratios) and direct substitution. The large ai_only set consists almost entirely of construction details (1.31, 11.15, 11.28), the explicit pyramid-prism relation (12.7), definitions (D5.5, D6.4), and a common notion (CN2) that Heath leaves implicit. Since both proofs argue through the same key intermediate conclusions and differ only in citation depth, the classification is G.

### 12.10
**Category**: Granularity difference
**Jaccard**: 0.107
**Analysis**: Q2 decides this classification as G. Both proofs share the same logical backbone: a double reductio ad absurdum via exhaustion, inscribing successively refined polygons in the circular base, establishing that each refinement removes more than half of the remaining solid (conical or cylindrical), invoking X.1 (exhaustion), and using XII.7 to convert between prisms and pyramids (prism = 3 times pyramid). The AI addresses both required cases (cylinder > 3 times cone in Step 7, cylinder < 3 times cone in Step 8). The heath_only items (11.32, 12.2, 4.7) all correspond to facts present in the AI proof at the same logical position but argued at finer granularity or with different equivalent lemmas: Heath uses 11.32 (parallelepipeds of same height are as bases) for comparing prisms, while the AI uses 12.5 and 12.6 (pyramids of same height are as bases) for the analogous comparison; Heath references 12.2 for the more-than-half exhaustion technique, while the AI re-derives it explicitly using 1.41 and 3.16; Heath circumscribes a square (4.7) for the initial more-than-half argument, while the AI uses a rectangle containment argument instead. The large ai_only set consists overwhelmingly of definitions, common notions, postulates, and elementary construction propositions, indicating over-citation at a finer granularity level rather than a different proof path.

### 12.11
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Heath proves 12.11 by the classic double reductio ad absurdum: assuming the proportion between cones and bases fails, he inscribes exhausting polygonal pyramids, applies alternation of proportions (5.16) to derive a contradiction, then handles the greater-solid case by inversion. The AI instead gives a direct proof via the Eudoxian definition of equal ratios (D5.5): after constructing similar inscribed polygons and showing their pyramid ratios match the base ratios (12.1, 12.2, 12.6), the AI directly verifies all three comparison cases of the definition (mB1 = nB2, mB1 > nB2, mB1 < nB2) using gap-control arguments with 5.15 and 5.19 rather than alternation. These represent genuinely different logical backbones -- Heath's pivotal intermediate conclusion is the alternation step yielding cone:pyramid = O:pyramid, while the AI's pivotal conclusions are the direct gap-control inequalities in Steps 7-9. The AI's path is logically complete and valid under Q3.

### 12.12
**Category**: Path difference
**Jaccard**: 0.103
**Analysis**: Q2 determined the classification. Heath's proof uses the method of exhaustion: inscribing similar polygonal pyramids in the cones, applying X.1 to exhaust the gap, invoking XII.8 (similar pyramids in triplicate ratio of corresponding sides), aggregating via V.12, and reaching a double reductio ad absurdum (less-than and greater-than cases). The AI proof takes an entirely different route: it introduces an auxiliary cylinder T sharing the second cylinder's base but the first cylinder's height, proves T:C2 = h:k = a:b by a stacking argument from the definition of equal ratios (D5.5), then applies 12.11 (same-height cylinder comparison) and 12.2 (circles as squares on diameters) to build a chain of proportions, which it combines via ex aequali (5.22) to obtain the triplicate ratio for cylinders, transferring to cones via 12.10 and 5.15. The backbones share no key intermediate conclusions: Heath's pivots on pyramid similarity (XII.8) and exhaustion (X.1), while the AI's pivots on direct cylinder-ratio algebra (12.11, 12.2, 6.20). At Q3, the AI's chain is logically complete, with each step supported by cited propositions, so the verdict is D.

### 12.13
**Category**: Path difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification. Heath's proof relies on XII.11 (cones and cylinders of the same height are proportional to their bases, proved by exhaustion) to establish that cylinder segments with equal heights and equal bases are equal, then builds equimultiples and applies V. Def. 5. The AI proof takes a fundamentally different route, avoiding XII.11 entirely: it defines cylinders via generating rectangles, assembles congruent copies end-to-end to form equimultiples, and compares the assembled cylinders by geometric inclusion or coincidence of their generating rectangles. The proof-tree containment test confirms that XII.11 (the sole heath_only substantive proposition) is not subsumed by any AI-cited higher-level result; the AI's approach is an independent path from first principles using definitions (D11.21-D11.23), common notions (CN2, CN4, CN5), and low-level Book 1/11 propositions. Since the backbones differ (Case B) and the AI's chain is logically complete under the Q3 check, the classification is D.

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct an auxiliary cylinder by extending an axis, use XII.13 (cylinder cut by a parallel plane gives ratio equal to axis ratio) to establish the proportion between cylinders and their axes, use XII.11 (cylinders on equal bases with the same height are equal) to substitute the auxiliary cylinder for the target, and extend to cones via XII.10. The AI proof cites the same three core propositions as Heath (12.10, 12.11, 12.13) but additionally cites construction steps (1.3, P2), definitions (D11.21, D11.22, D11.23, D3.1, D5.5), a geometric lemma for parallel planes (11.14), and ratio manipulation propositions (5.7, 5.11, 5.15) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations of constructions, definitions, and ratio lemmas filling out steps present but implicit in Heath, this is Case A: same backbone with different citation depth, yielding G.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs construct an auxiliary solid sharing the base of one original solid and the height of the other, then establish that the ratio to the auxiliary equals the ratio of bases (via 12.11) and the ratio of heights (Heath via 12.13, AI via 12.14), combining with 5.11, 5.7, and 5.9 to reach the reciprocal proportion and its converse. The proof-tree containment test confirms that 12.13 appears inside Heath's own proof of 12.14, so the AI cites 12.14 as a single higher-level unit while Heath re-derives its internals inline. The remaining ai_only items D11.18 and D11.21 are definitions (overcitation). Heath case-splits the forward direction into equal and unequal heights, whereas the AI handles both uniformly through 12.14, which applies regardless; this is a presentational, not structural, difference. Same backbone, different citation depth: G.

### 12.16
**Category**: Path difference
**Jaccard**: 0.105
**Analysis**: Q2 decided the classification. Heath's proof argues through tangent-line and parallelism intermediates: AC is tangent to the inner circle (3.16), the perpendicular bisector yields LD = DN (3.3, 1.4), and LN parallel to the tangent AC therefore does not touch the inner circle. The AI proof instead argues through angle-chord comparison and distance inequalities: the hinge theorem (1.24) establishes that any polygon side UV is shorter than the reference chord BC, the chord-distance theorem (3.15) then shows the perpendicular from the center to UV exceeds r, and triangle properties (1.17, 1.19) extend this to every point on every side. These are fundamentally different key intermediate conclusions -- neither set is a refinement or compression of the other -- placing the proofs in Case B of Q2. Q3 confirms the AI path is logically complete: every step is justified by cited propositions, and the chain from premises to conclusion is sound.

### 12.17
**Category**: Path difference
**Jaccard**: 0.171
**Analysis**: Classification was decided at Q2/Q3. The two proofs share the high-level goal of inscribing a polyhedron in the greater sphere that avoids the lesser, but their key intermediate conclusions and distance arguments differ fundamentally. Heath inscribes the equilateral polygon so it does not touch the lesser circle directly, then analyzes the perpendicular distance from the center to each face through a specific chain of square comparisons (KB^2 > 2BX^2 via the circumscribed-circle property, KB^2 < 2KZ^2 via III.31 and VI.8), concluding AX > AZ > AG. The AI instead constructs a mean proportional s = sqrt(Rr) between the two radii (6.13, 6.17), inscribes the polygon so it does not touch a circle of radius s rather than r (explicitly citing 12.16), then uses a general projection-and-scaling argument to show every face point P satisfies OP >= ka = a^2/R > s^2/R = r. The constructions, the cited propositions, and the logical backbones are all different, yielding a Jaccard of only 0.171. The AI's path is logically complete under the hardened Q1(b) standard, so the classification is D.

### 12.18
**Category**: Path difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification. Heath's proof uses the classic double reductio (method of exhaustion): assuming the ratio holds to a smaller sphere, inscribing a non-touching polyhedral solid (12.17), deriving a contradiction via alternation (5.16), then handling the greater sphere case via 12.2 Lemma. The AI proof takes a fundamentally different path: it introduces concentric cubes as intermediaries whose ratio is the triplicate of the diameters (11.33), subdivides inscribed polyhedra into similar triangular pyramids (12.8, 6.6, 6.4, 6.5), constructs cubical shell approximations controlled by 10.1, and directly verifies the equimultiple definition (D5.5) to establish the ratio without any reductio argument. These are clearly different backbones -- the AI avoids double reductio entirely and instead gives a direct equimultiple proof. Under Q3, the AI's different path is logically complete: each step is explicitly justified with cited propositions, the chain runs from premises to conclusion, and the mathematical strategy of using cubes as intermediaries with controlled approximation error is sound.
