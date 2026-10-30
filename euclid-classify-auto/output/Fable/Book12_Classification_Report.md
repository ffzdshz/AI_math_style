# Book 12 — Classification Report (Fable)

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
