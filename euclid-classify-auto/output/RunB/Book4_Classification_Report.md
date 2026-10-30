# Book 4 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 14 | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.10, 4.11, 4.13, 4.14, 4.15, 4.16 |
| Path difference (D) | 2 | 4.9, 4.12 |
| AI proof error (E) | 0 |  |

**Total**: 16 propositions

## Per-Proposition Analysis

### 4.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: draw a diameter BC, handle the trivial case where BC equals D, then for the main case cut off a segment CE equal to D, draw a circle with center C and radius CE, join C to the intersection point on the given circle, and conclude by the definition of circle that the new chord equals CE and hence D. Heath's proof cites no references at all, while the AI explicitly cites 1.3 (cutting off equal segments), CN1 (transitivity of equality), D1.15 (definition of circle), D1.17 (definition of diameter), D4.7 (definition of fitting a line in a circle), P1 (joining points), and P3 (drawing a circle). All ai_only items are definitions, common notions, postulates, or a basic construction proposition, representing over-citation of steps Heath treats as implicit. Since the key intermediate conclusions are identical and only citation depth differs, this is a granularity difference.

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct a tangent at point A on the circle, construct two angles at A equal to the angles of the given triangle using I.23, join BC to form the inscribed triangle, apply the alternate segment theorem (III.32) to establish that two angles of the inscribed triangle equal two angles of the given triangle, then conclude the third angles are equal via I.32. The AI proof cites the same core propositions as Heath (1.23, 1.32, 3.16, 3.32) but adds over-citations: 3.17 alongside 3.16 for tangent construction, P1 for joining BC, D4.3 for the definition of an inscribed triangle, and CN1/CN3 for explicit common notion invocations. Heath's citation set is a proper subset of the AI's, with heath_only empty. Since the key intermediate conclusions are identical and the differences are purely in citation depth, this is a granularity difference.

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing angles at the centre equal to the exterior angles of the given triangle, establishing right angles at tangent points via III.18, using quadrilateral angle sums to show each angle of the circumscribed triangle equals the corresponding angle of the given triangle, and concluding the third angle equality via I.32. The citation differences are purely about depth: the AI over-cites by explicitly invoking CN1, CN3, D4.4, and P2 for foundational steps that Heath leaves implicit, while Heath cites III.1 for finding the circle's centre, which the AI treats as given. No key intermediate conclusion differs between the proofs.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: bisect two angles of the triangle to find the incenter D, drop perpendiculars DE, DF, DG to the three sides, prove DE=DF and DF=DG via I.26 triangle congruence, conclude all three distances are equal, construct the circle with center D, and show tangency via III.16. The ai_only set {1.12, CN1, D1.15, P3} consists entirely of a construction proposition (I.12 for drawing perpendiculars), a common notion (CN1 for transitivity of equality), a definition (D1.15 for the circle), and a postulate (P3 for describing a circle) -- all foundational items that Heath uses implicitly without citation. The heath_only set is empty, confirming no substantive propositions are missing from the AI proof. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: bisect AB and AC, draw perpendicular bisectors, analyze three cases (meeting inside, on BC, or outside the triangle), prove FA=FB and FA=FC via SAS congruence (I.4), conclude FA=FB=FC, and describe the circumscribed circle. The AI's additional citations (1.11, CN1, D1.10, D1.15, D4.6, P1, P3) are all construction propositions, definitions, common notions, and postulates that Heath uses implicitly but does not cite. The heath_only set is empty, confirming the AI omits nothing Heath cites. This is a clear Case A same-backbone, different-depth scenario yielding G.

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) construct two perpendicular diameters and join endpoints, (2) prove ABCD equilateral via I.4 using equal radii and right angles at the center, (3) prove ABCD right-angled via III.31 (angles in semicircles are right), and (4) conclude ABCD is a square by the definition of a square (I.Def.22/D1.22). The AI proof cites all three of Heath's references (1.4, 3.31, D1.22) and adds six more (3.1, 1.11, 1.15, D1.15, D4.3, P1), all of which are construction propositions, postulates, or definitions that make explicit the steps Heath leaves implicit. Heath_only is empty, confirming the AI covers everything Heath does. This is Case A of Q2: same backbone with different citation depth, yielding a granularity difference.

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same logical backbone: draw perpendicular diameters, construct tangent lines at the endpoints, establish perpendicularity of tangents to radii (III.18), prove opposite sides of the circumscribed figure are parallel (I.28), show all four corner angles are right angles, show all four sides are equal, and conclude the figure is a square. The ai_only items are predominantly over-citations: construction props (1.11), postulates (P1), common notions (CN1, CN2), and definitions (D1.15, D1.22, D4.4). The substantive ai_only citation 1.32 (triangle angle sum) is used where Heath uses 1.34 (parallelogram properties) to establish the same key conclusion that the corner angles are right angles -- a different tool for the same intermediate result. The heath_only item 1.30 (transitivity of parallelism) is not needed by the AI because it establishes parallelism of opposite sides directly via I.28 (both perpendicular to the same diameter), rather than Heath's two-step route through an intermediate parallel. These are citation-depth differences, not backbone differences.

### 4.8
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: start with the given square, find the center by bisecting sides and drawing parallels, establish four equal distances from the center to the midpoints of the sides, show right angles at each tangent point, then describe the circle and invoke III.16 to prove tangency rather than intersection. The AI proof is more explicit in its citations, adding 1.29 (for deriving right angles from parallel lines), 1.33 (for establishing parallelograms), and several definitions (D1.15, D1.22, D4.5), common notions (CN1), and postulates (P1, P3) that Heath uses implicitly. Since heath_only is empty, every citation Heath makes is also made by the AI, and the ai_only items are all either sub-steps of the same argument or foundational references cited explicitly by the AI but left implicit by Heath. The key intermediate conclusions are identical in both proofs, confirming Case A of Q2.

### 4.9
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 reveals a genuinely different backbone between the two proofs, leading to classification D. Heath's proof establishes that each angle of the square is bisected by a diagonal using I.8 (SSS congruence), then uses I.6 to conclude EA = EB from the equal half-angles, and similarly for all four segments. The AI proof takes an entirely different route: it first establishes that opposite sides of the square are parallel (1.28), then uses alternate angles (1.29) and ASA congruence (1.26) to show triangle AEB is congruent to triangle CED, yielding EA = EC and EB = ED. Separately, it analyzes the angles via isosceles triangle properties (1.5) and the angle sum theorem (1.32) to show EA = EB via I.6. The proof-tree containment test confirms that I.8 (the sole heath_only item) does not appear in the proof of any AI-cited proposition such as 1.26, so the divergence is not a matter of citation depth but a genuinely different logical path. The AI's path is logically complete and valid, satisfying Q3(b).

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.583
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing AB cut at C via II.11, fitting BD = AC in the circle via IV.1, circumscribing circle ACD via IV.5, establishing BD as tangent to circle ACD via III.37, deriving angle BDC = angle DAC via III.32, showing the three base-related angles are equal, deriving BD = DC via I.6, and concluding DC = CA so each base angle is double the vertex angle. The AI proof uses explicit algebraic notation (phi, psi) and applies angle-sum (I.32) and supplementary angle (I.13) arguments more explicitly, while Heath uses geometric narrative. The ai_only set consists entirely of construction postulates (P1, P3), a construction proposition (4.1), a definition (D1.20), and a basic angle fact (1.13) that Heath uses implicitly without citing. Since heath_only is empty and all ai_only items are over-citations of construction steps, axioms, and definitions rather than substantive alternative propositions, this is Case A of Q2: same backbone with different citation depth, yielding Granularity difference.

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct isosceles triangle FGH (4.10), inscribe equiangular triangle ACD in the circle (4.2), bisect the base angles with 1.9 to produce five equal angles, use 3.26 to get five equal arcs, use 3.29 to get five equal chords (equilateral), then use 3.27 with equal arcs to prove equiangular. The AI adds four citations not in Heath: 1.32 (used in Step 5 to explicitly compute that each of the five equal angles is one-fifth of two right angles, a calculation Heath omits), CN2 (explicitly cited where Heath implicitly uses it when adding arcs), and D4.3/D4.7 (definitions cited in the concluding remark). All ai_only items represent deeper citation of steps Heath leaves implicit or definitions Heath does not cite, while heath_only is empty. This is Case A of Q2: same backbone, different citation depth, yielding Granularity difference.

### 4.12
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 determines the classification. Heath's proof draws tangent lines at the vertices A, B, C, D, E of the inscribed regular pentagon and uses III.1 to find the center, then proves the circumscribed pentagon equilateral and equiangular through Pythagorean arguments and triangle congruence at those contact points. The AI proof takes a structurally different approach: it bisects each arc of the inscribed pentagon using 3.30, draws tangents at those arc midpoints, then uses angle sums of quadrilaterals (1.32) and equal-arc arguments (3.26, 3.27) to establish equiangularity, and congruent triangles to establish equilaterality. The tangent points differ (arc midpoints vs. vertices), the construction differs (arc bisection vs. center-finding), and the equiangularity argument differs (quadrilateral angle sum vs. doubled angle pairs). These are genuinely different backbones, not mere citation-depth variations. Under Q3, the AI's alternative path is logically complete: the chain from inscribed pentagon through arc bisection, tangent construction, equal arcs, equal central angles, equal vertex angles, and equal tangent segments to the equilateral-and-equiangular conclusion is sound throughout.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow identical logical backbones: bisect two angles of the regular pentagon to locate center F, use I.4 to prove triangle congruences establishing that all five angles are bisected by lines from F, drop perpendiculars from F to all five sides, use I.26 to show all perpendiculars are equal, describe a circle with center F and that common perpendicular distance as radius, and invoke III.16 to show the circle is tangent to each side. The AI proof cites the same three substantive propositions as Heath (I.4, I.26, III.16) and adds seven additional foundational references: construction propositions (1.9 for angle bisection, 1.12 for dropping perpendiculars), postulates (P1, P3, P4), a common notion (CN1), and a definition (D4.5). Heath leaves these construction steps and axioms implicit. The empty heath_only set confirms no substantive proposition is missing from the AI proof. This is a clear case of same backbone with different citation depth.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect angles BCD and CDE to locate center F, prove all five distances FA=FB=FC=FD=FE are equal, and circumscribe the circle. The AI proof is substantially more detailed than Heath's, explicitly working through SAS congruences (I.4) where Heath uses 'similarly it can be proved' and 'in manner similar to the preceding'. The ai_only set consists entirely of over-citations: I.4 (basic SAS congruence used to establish equal distances), I.9 (angle bisection construction), CN1 (transitivity of equality), P1 (joining lines), P3 (drawing circles), and D4.6 (definition of circumscribed circle). Heath's sole citation of I.6 is also used by the AI. The heath_only set is empty. This is a clear case of the AI providing a more granular, explicit proof of the same argument that Heath presents in compressed form.

### 4.15
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct equilateral triangles at the center to establish that all six central angles equal one-third of two right angles, then use III.26 to get equal arcs, III.29 for equal sides (equilateral), and III.27 for equal inscribed angles (equiangular). The proofs differ only in the sub-method used to establish all six central angles as equal. Heath proves three angles directly via two equilateral triangles (EGD, DGC) and supplementary angles, then applies I.15 (vertical angles) to obtain the other three. The AI instead constructs an additional circle centered at A (beyond Heath's circle at D), directly proving four equilateral triangles (EGD, DGC, AGB, AGF) and then uses I.13 (supplementary angles on a line) to derive the remaining two angles (BGC, FGE) by subtraction. This substitution of I.13 for I.15 represents a minor variation in the sub-argument for one key step, not a different backbone. The ai_only set consists entirely of definitions, postulates, common notions, and proposition I.13 — all representing over-citation or the I.13-for-I.15 substitution. The key intermediate conclusions are identical in both proofs.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: inscribe an equilateral triangle side (arc AC = 1/3 circle) and a regular pentagon side (arc AB = 1/5 circle), compute arc BC = 2/15 circle, bisect BC at E via III.30 to get arcs of 1/15 each, then fit equal chords around the circle to complete the 15-gon. The AI proof explicitly cites 4.2 and 4.11 for the triangle and pentagon constructions that Heath performs without citation, cites P1 for joining points, 4.1 for fitting chords, and 3.29 and 3.27 to justify that equal arcs yield equal chords (equilateral) and equal inscribed angles (equiangular) — conclusions Heath simply asserts. All ai_only items (3.27, 3.29, 4.1, 4.11, 4.2, P1) are over-citations making explicit what Heath leaves implicit, while heath_only is empty. This is a clear Case A: same backbone, different citation depth.
