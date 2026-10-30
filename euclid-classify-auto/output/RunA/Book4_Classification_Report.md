# Book 4 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 14 | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.10, 4.11, 4.12, 4.13, 4.14, 4.16 |
| Path difference (D) | 2 | 4.9, 4.15 |
| AI proof error (E) | 0 |  |

**Total**: 16 propositions

## Per-Proposition Analysis

### 4.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: draw the diameter of the given circle, handle the trivial case where the given line equals the diameter, then for the non-trivial case construct a segment equal to the given line on the diameter, draw a circle with that segment as radius, find the intersection with the given circle, and use the definition of a circle plus transitivity of equality to conclude the fitted chord equals the given line. Heath's reference list is empty (no explicit citations), while the AI explicitly cites definitions (D1.15, D1.17, D4.7), postulates (P1, P3), a common notion (CN1), and Proposition 1.3 for cutting off a segment. All of these are foundational references that Heath leaves implicit. Since the key intermediate conclusions are identical and the only differences are in citation depth, this is a granularity difference (G).

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a tangent to the circle at a point, construct two angles at the tangent point equal to two angles of the given triangle, join the resulting chord, apply the alternate segment theorem (III.32) twice to transfer the tangent-chord angles to inscribed angles, and then use the angle-sum property (I.32) to establish equality of the remaining pair of angles. The AI proof swaps which tangent angle corresponds to which triangle angle compared to Heath, but the key intermediate conclusions are identical. The ai_only set consists entirely of common notions (CN1, CN3), a definition (D4.3), and a postulate (P1) — none are substantive propositions. Heath uses these implicitly without citing them. This is a classic Case A same-backbone, different-citation-depth scenario, yielding G.

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decides the classification. Both proofs share the same logical backbone: construct center K, build angles BKA = DEG and BKC = DFH, draw tangents at A, B, C, establish right angles at tangent points, use quadrilateral angle sums to show corresponding angles of the circumscribed triangle equal those of DEF, and conclude with I.32 for the remaining angle. The ai_only citations (D4.4, P1, P2) are a definition and postulates representing over-citation of basic constructions. The heath_only citation (3.18) covers the fact that tangent-radius angles are right, but the AI establishes this same fact directly from its construction: the tangent lines were explicitly drawn perpendicular to the radii in Step 5 (using 3.16 to confirm they are tangents), so the right angles follow from construction rather than requiring a separate invocation of 3.18. The underlying geometric fact is present at the same logical position in both proofs. This is Case A of Q2: same backbone, different citation depth.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: bisect two angles of the triangle to locate center D (I.9), drop perpendiculars from D to the three sides, prove DE=DF and DF=DG via triangle congruence (I.26), conclude all three distances are equal so a circle centered at D passes through E, F, G, show the circle touches the sides rather than cutting them (III.16), and invoke the definition of inscribed circle (IV.Def.5). The AI's three extra citations (ai_only: 1.12, CN1, P3) are all construction-level or axiomatic: I.12 for drawing perpendiculars, CN1 for the transitivity step equating all three distances, and P3 for describing the circle. Heath uses these same steps implicitly without explicit citation. Since heath_only is empty, there is no missing substantive content in the AI proof. The identical backbone with over-citation of construction and axiom steps is a textbook granularity difference.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two sides of the triangle, erect perpendicular bisectors, find their intersection point F, then use SAS congruence (I.4) to show FA = FB and FB = FC (or CF = AF), concluding all three distances are equal so a circle centered at F passes through all three vertices. Both proofs cover all three cases (F inside, on a side, outside the triangle). The AI bisects AB and BC while Heath bisects AB and AC, but this is merely a different choice of which two sides to bisect and does not change the logical backbone. The ai_only set consists entirely of over-citations: construction propositions (1.11 for erecting perpendiculars), postulates (P1 for joining lines, P3 for describing circles), common notions (CN1 for transitivity of equality), and definitions (D1.10, D4.6) that Heath uses implicitly without explicit citation. The heath_only set is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided this classification. Both proofs establish the same two key intermediate conclusions: (1) the quadrilateral ABCD is equilateral, proved via I.4 (SAS triangle congruences using radii and right angles at the center), and (2) the quadrilateral ABCD is right-angled, proved via III.31 (angle in a semicircle is right). Both then conclude ABCD is a square by I.Def.22. The AI proof simply reverses the order (right angles first, then equilateral) and provides more explicit foundational citations. The ai_only set consists entirely of definitions (D1.15, D1.17, D4.3), postulates (P1, P2, P4), a common notion (CN1), and one construction proposition (1.11) -- all representing over-citation of steps Heath leaves implicit. The heath_only set is empty. This is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.188
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct tangent lines at the endpoints of two perpendicular diameters, show opposite sides are parallel (forming a parallelogram), prove the figure is equilateral via radii equality and parallelogram properties, prove it is right-angled, and conclude it is a circumscribed square. The heath_only citations (3.18 and 1.30) reflect different granularity rather than a different path: Heath uses 3.18 to derive perpendicularity from tangency, while the AI reverses the order by constructing perpendiculars first (1.11) and then deducing tangency (3.16), arriving at the same intermediate fact. Heath uses 1.30 for transitivity of parallelism, while the AI establishes each pair of parallel sides directly from 1.28. The ai_only citations are predominantly definitions (D1.10, D1.15, D1.17, D1.22, D4.4), common notions (CN1, CN2), postulates (P1), and construction or supplementary propositions (1.11, 1.29, 1.32) that represent over-citation of foundational items. The identical backbone with differing citation depth places this squarely in Case A of Q2, yielding a granularity difference.

### 4.8
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: bisect sides of the square to find midpoints, establish parallelograms to show four equal segments from center to midpoints of sides, construct a circle through those four points, and prove tangency via III.16. The sole heath_only citation (1.31, drawing a parallel through a point) reflects Heath's construction method of explicitly drawing parallels through midpoints, while the AI achieves the same geometric configuration by bisecting all four sides, joining opposite midpoints with P1, and proving those joins are parallel via I.33 and I.29. The ai_only set is dominated by over-citation of definitions (D1.15, D1.22, D4.5), common notions (CN1, CN3), and postulates (P1, P3), with the substantive additions 1.29 and 1.33 serving as the AI's alternative to Heath's 1.31. Since the key intermediate conclusions are identical and only the construction depth and citation granularity differ, this is a granularity difference.

### 4.9
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof establishes that the diagonals bisect the angles of the square (using I.8 on triangles formed by equal sides and a common diagonal), then infers equal half-angles at adjacent vertices to conclude EA=EB by I.6. The AI takes a fundamentally different route: it first proves opposite sides are parallel (I.28), derives equal alternate angles with the diagonals as transversals (I.29), applies ASA congruence (I.26) to opposite triangles AEB and CED to get AE=CE and BE=DE, then uses SSS congruence (I.8) on adjacent triangles AEB and AED, derives right angles at E via I.13 and the angle sum theorem I.32, and finally shows angle EAB = angle ABE to conclude AE=BE by I.6. The key intermediate conclusions differ: Heath's backbone runs through angle bisection of the square's corners, while the AI's backbone runs through parallelism of sides and ASA congruence of diagonally opposite triangles. Since the AI's different path is logically complete and valid, Q3 confirms classification as D.

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.583
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) AB*BC = BD^2 from the construction and BD=AC, (2) BD is tangent to circle ACD via III.37, (3) angle BDC = angle DAC via III.32, (4) angle BDA = angle BCD via angle addition with I.32 and I.5, (5) BD = DC via I.6, (6) CA = CD so angle CDA = angle DAC via I.5, and (7) each base angle is double the vertex angle. The ai_only set consists entirely of construction propositions (4.1), definitions (D1.15, D1.20), and postulates (P1, P3) that the AI cites explicitly for steps Heath leaves implicit or uncited in the reference set. Since the logical backbone is the same and the citation differences reflect only over-citation of construction and foundational items, this is a granularity difference (G).

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: construct the isosceles triangle FGH via IV.10, inscribe an equiangular triangle ACD via IV.2, bisect angles ACD and CDA via I.9 to obtain five equal angles, apply III.26 (equal inscribed angles stand on equal arcs) and III.29 (equal arcs subtend equal chords) to prove the pentagon equilateral, then combine arcs and apply III.27 (equal arcs subtend equal inscribed angles) to prove it equiangular. The AI proof adds four over-citations not in Heath: P1 (postulate for joining lines), CN2 (common notion for adding equals to equals), D4.3 (definition of polygon inscribed in circle), and 1.32 (angle-sum theorem, listed in USED but never actually invoked in the proof steps). Heath uses the same underlying operations without explicitly citing these basic axioms and definitions. Since heath_only is empty and the ai_only items are all postulates, common notions, definitions, or phantom citations, this is a pure citation-depth difference with no backbone divergence, yielding category G.

### 4.12
**Category**: Granularity difference
**Jaccard**: 0.389
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: inscribe a regular pentagon (4.11), draw tangents at each vertex (3.16), establish perpendicularity of radii to tangent lines (3.18), use triangle congruence (1.8, 1.26) and the Pythagorean theorem (1.47) to show tangent segments from adjacent vertices are equal, deduce equilateral by doubling equal segments, and deduce equiangular through congruent triangles. The AI's ai_only citations are predominantly over-citations: definitions (D1.15, D1.16, D4.4), common notions (CN1, CN2, CN3), and a postulate (P1) that Heath leaves implicit, plus substantive but depth-level additions (3.26 as an explicit bridge to 3.27, 1.32 for angle-sum reasoning Heath leaves implicit, 1.4 for SAS congruence where Heath uses different but equivalent congruence results). The sole heath_only item, 3.1 (finding the center), is a construction step that the AI replaces with the definitional citation D1.16. All key intermediate conclusions are present in both proofs at the same logical positions, making this a citation-depth difference rather than a path difference.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two angles of the equilateral equiangular pentagon to locate the incenter F, prove that the remaining three angles are also bisected by lines from F (using I.4 and the equilateral/equiangular properties), drop perpendiculars from F to all five sides, prove all perpendiculars equal via I.26, describe the inscribed circle, and verify tangency via III.16. The AI proof is more explicit, citing construction tools (1.9 for angle bisection, 1.12 for dropping perpendiculars), postulates (P1, P3, P4), common notions (CN1, CN3), and definitions (D3.2, D4.5) that Heath leaves implicit. Heath's citation set is a proper subset of the AI's, and all ai_only items are foundational over-citations rather than substantive propositions indicating a different path. This is a clear Case A granularity difference.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same backbone: bisect angles BCD and CDE to find point F, show F is equidistant from all five vertices, then circumscribe the circle. Heath compresses the equidistance argument with 'similarly it can be proved' and 'in manner similar to the preceding,' citing only I.6. The AI spells out each equidistance step explicitly using SAS congruence (I.4) applied to multiple triangle pairs, plus construction citations (I.9, P1, P3), common notions (CN1, CN3), and a definition (D4.6). The ai_only set consists entirely of construction propositions, postulates, common notions, a definition, and I.4 used to expand what Heath leaves as 'similarly' arguments. The heath_only set is empty. The key intermediate conclusions are identical in both proofs; only the citation depth differs.

### 4.15
**Category**: Path difference
**Jaccard**: 0.308
**Analysis**: Q2 determined the classification. Both proofs reach the same final conclusions (equilateral and equiangular hexagon via six equal central angles, equal arcs, equal chords, and equal inscribed angles), but they follow genuinely different logical backbones to establish the six equal central angles. Heath constructs one auxiliary circle (centered at D), uses I.5 and I.32 to show three adjacent central angles are each one-third of two right angles, then uses I.15 (vertical angles) to obtain the remaining three. The AI constructs two auxiliary circles (centered at D and at A), creating four equilateral triangles that directly yield four of the six central angles, then computes the remaining two angles by subtraction using I.13 (supplementary angles) and CN3. The different construction (two circles vs. one) and different method for the remaining angles (supplementary angle subtraction vs. vertical angles) constitute a different path. The AI's reasoning chain is logically complete and sound throughout, so this is a valid path difference.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical backbone: inscribe an equilateral triangle side AC and regular pentagon side AB in the circle, deduce that arc BC is two-fifteenths of the circumference, bisect BC at E using 3.30 to get one-fifteenth arcs, then fit equal chords contiguously around the circle to produce the 15-gon. The key intermediate conclusions are the same in both proofs. The only difference is citation depth: Heath cites only 3.30 and leaves implicit the constructions (4.2, 4.11, 4.1), the arc-chord relationships (3.28, 3.29), the angle equality (3.27), the definition of inscription (D4.3), and the postulate for joining points (P1). The AI explicitly cites all of these. Since heath_only is empty and all ai_only items are explicit citations of steps Heath performs implicitly, this is a classic over-citation granularity difference.
