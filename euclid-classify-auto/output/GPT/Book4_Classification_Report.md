# Book 4 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 12 | 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.9, 4.10, 4.11, 4.13, 4.14, 4.16 |
| Path difference (D) | 4 | 4.1, 4.8, 4.12, 4.15 |
| AI proof error (E) | 0 |  |

**Total**: 16 propositions

## Per-Proposition Analysis

### 4.1
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof inscribes the chord by cutting the diameter to the desired length and drawing an auxiliary circle to locate the endpoint on the given circle, a simple circle-intersection construction. The AI instead finds the center, verifies that the two radii and the desired length satisfy the triangle inequality, and constructs a triangle with those three sides via 1.22, deducing that the third vertex lies on the circle because its distance from the center equals the radius. These are genuinely different construction methods with different logical backbones, and the AI's path is logically complete, so the classification is D.

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs follow the same tangent-chord strategy: draw a tangent to the circle at a point A, construct angles between the tangent and two chords equal to two angles of the given triangle (I.23), apply the tangent-chord theorem (III.32) to show the inscribed triangle's angles equal those of the given triangle, and use the angle-sum property (I.32) for the remaining angle. The AI proof adds explicit citations for construction existence (3.17), postulates (P1, P2), common notions (CN1, CN2, CN3), a definition (D4.3), and auxiliary ordering lemmas (1.13, 1.17), all of which Heath uses implicitly. Since heath_only is empty and the ai_only items are entirely over-citations of construction steps and axioms, the backbone is identical at different citation depths, giving Granularity difference (G).

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share the same backbone: construct central angles equal to the exterior angles of the given triangle, draw tangent lines at the three determined points on the circle, establish that these tangent lines are perpendicular to the radii at the contact points, and then show each angle of the circumscribed triangle equals the corresponding angle of the given triangle. The single heath_only citation (3.18, tangent-radius perpendicularity) is addressed by the AI through reversed construction order: the AI constructs perpendiculars to the radii using 1.11 and then confirms tangency via 3.16, achieving the identical geometric fact that Heath obtains by drawing tangents first and citing 3.18 for perpendicularity. The AI's angle computation uses isosceles triangle base angles (1.5) and 1.32 on sub-triangles rather than Heath's quadrilateral angle sum approach, but both arrive at the same key conclusion that each vertex angle of the circumscribed triangle equals the corresponding angle of the given triangle. The fourteen ai_only items consist of definitions, common notions, postulates, and explicit construction steps (1.11, 1.5) that represent over-citation and additional detail rather than a different logical path.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.211
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: bisect two interior angles of the triangle, find their intersection point, drop perpendiculars to the three sides, use I.26 to show the three perpendicular distances are equal, draw a circle through the three feet, and argue tangency via III.16 to conclude the circle is inscribed (IV.Def.5). The AI bisects angles at A and B rather than B and C, which is immaterial. All 15 ai_only items are over-citations reflecting greater explicitness rather than a different proof strategy: construction propositions (1.12), postulates (P1-P5), definitions (D1.10, D1.12, D1.15, D1.17, D3.2), common notions (CN1, CN5), and subsidiary results (1.16, 1.17) used to justify steps that Heath leaves implicit, such as proving the bisectors meet and that the perpendicular feet lie on the sides. The heath_only set is empty, confirming that the AI covers all of Heath's reasoning. Case A of Q2 holds: same backbone, different citation depth.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect two sides of the triangle at their midpoints, draw perpendiculars at those midpoints, show the intersection point is equidistant from all three vertices using I.4, and conclude the circle centered there circumscribes the triangle. The AI proof adds an explicit proof by contradiction (using 1.14, 1.29, 1.30, 1.31) that the perpendicular bisectors must meet, whereas Heath addresses this by enumerating three cases of where the intersection might lie. The AI also over-cites by including construction references (1.11, P1, P2, P3), definitions (D1.10, D1.15, D1.23, D4.6), common notions (CN1, CN4), and a postulate (P4) that Heath leaves implicit. Since heath_only is empty and all key intermediate conclusions are the same in both proofs, this is a granularity difference where the AI provides greater citation depth than Heath.

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct two perpendicular diameters in the circle, join their endpoints to form quadrilateral ABCD, prove ABCD equilateral using I.4 (congruent triangles from equal radii and equal angles at the center), prove ABCD right-angled using III.31 (angles in semicircles are right), and conclude ABCD is a square by definition. The AI proof over-cites by explicitly listing construction propositions (1.11, 3.1), definitions (D1.10, D1.15, D1.17, D4.3), postulates (P1, P2, P4), a common notion (CN1), and vertical angles (1.15), all of which Heath's proof invokes implicitly. Since heath_only is empty and all ai_only items are construction-level or foundational references, this is Case A of Q2: same backbone, different citation depth.

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct two perpendicular diameters, establish tangent lines at the four endpoints that are perpendicular to the radii, show opposite tangent lines are parallel (1.28, 1.30), form parallelograms, prove the circumscribed quadrilateral has right angles and equal sides via parallelogram properties (1.34), and conclude it is a square. The only substantive citation difference is that Heath uses 3.18 (radius to point of tangency is perpendicular to the tangent) after constructing tangent lines via 3.16, while the AI reverses the logical direction by first constructing perpendicular lines at the diameter endpoints (1.11) and then using 3.16 to show these perpendiculars are tangent. The key intermediate conclusion -- that the tangent lines are perpendicular to the radii at the points of contact -- is established in both proofs, just from opposite directions. All other ai_only items are definitions, common notions, postulates, and construction propositions, representing over-citation rather than path divergence. This is Case A of Q2: same backbone, different citation depth.

### 4.8
**Category**: Path difference
**Jaccard**: 0.056
**Analysis**: Q2 decided the classification. Both proofs establish the same final conclusions (equal perpendicular distances from center to all four sides, tangency via III.16), but they reach these conclusions through fundamentally different methods. Heath bisects two sides (I.10), draws parallels through the midpoints (I.31), forms parallelograms, and uses I.34 to show equal opposite sides, thereby establishing equal distances from center G to the four sides. The AI instead joins the diagonals to find center O, uses SAS (I.4) to prove the diagonals bisect the square's angles, drops perpendiculars from O to each side (I.12), and applies AAS (I.26) to prove all four perpendicular distances are equal. The heath_only propositions (I.10, I.31, I.34) represent substantive geometric constructions and facts that are entirely absent from the AI proof, which never bisects a side, draws a parallel, or invokes parallelogram properties. Case A of Q2 therefore fails, yielding Case B (different backbone). Under Q3, the AI's alternative path is logically complete with every step explicitly justified, so the classification is D.

### 4.9
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Both proofs follow the same logical backbone: join the diagonals of the given square, establish triangle congruence at adjacent vertices to show that the corresponding angles are equal, apply I.6 to conclude that the four distances from the diagonal intersection to the vertices are all equal, and then describe the circumscribed circle. The sole substantive divergence is that Heath invokes I.8 (SSS congruence) while the AI invokes I.4 (SAS congruence) to establish the triangle congruence at each pair of adjacent vertices -- both are valid congruence criteria reaching the identical intermediate conclusion (angle equality). The remaining ai_only items (CN1, CN4, D1.15, D1.22, D4.6, P1, P3, P4) are definitions, common notions, and postulates that Heath uses implicitly without citation. Q2 Case A holds: the key intermediate conclusions are identical, and the citation differences reflect granularity rather than a different proof path.

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.467
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: golden section construction (2.11), tangency to circumscribed circle (3.37), tangent-chord angle theorem (3.32), exterior angle theorem (1.32), and isosceles triangle properties (1.5, 1.6) leading to the conclusion that each base angle is double the vertex angle. The AI uses a different construction method (1.22 for three-side triangle construction instead of Heath's IV.1 chord-fitting approach) and adds explicit citations for common notions (CN1, CN2, CN4, CN5), a postulate (P1), a definition (D1.20), and 3.2 (to justify B lying outside the circumscribed circle), but these are all construction-level or axiom-level over-citations that do not alter the key intermediate conclusions. Since heath_only is empty and every ai_only item is either a construction proposition, common notion, postulate, definition, or supporting lemma, this is Case A: same backbone with different citation depth.

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: construct a special isosceles triangle with base angles double the vertex angle (4.10), inscribe an equiangular triangle ACD in the circle (4.2), bisect the two base angles to locate points E and B on the circle (1.9), deduce five equal inscribed angles and hence five equal arcs (3.26), five equal chords (3.29) for equilateral, then show interior angles stand on equal composite arcs and are therefore equal (3.27) for equiangular. The AI cites the same six substantive propositions as Heath; its ai_only set consists entirely of common notions (CN1, CN2, CN5), definitions (D3.9, D4.3), and postulates (P1, P2) that Heath leaves implicit. Heath_only is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 4.12
**Category**: Path difference
**Jaccard**: 0.087
**Analysis**: Q2 determined the classification. Heath's proof works through the centre of the circle, using perpendicularity of radii to tangent lines (III.18), the Pythagorean theorem (I.47) to establish BK = CK, SSS congruence (I.8) to bisect angles at the centre, and equal arcs yielding equal central angles (III.27) to prove triangle congruences via ASA (I.26). The AI proof takes a fundamentally different route: it avoids the centre entirely, instead joining diagonals to establish an inscribed-angle beta via SAS (I.4) and isosceles base angles (I.5), then applying the tangent-chord theorem (III.32) to show each tangent makes angle beta with the adjacent pentagon side. Meeting of tangent rays is proved through angle-sum arguments (I.32, P5), and congruence of all five exterior triangles follows from the isosceles converse (I.6) and ASA (I.26). The key intermediate conclusions differ at every stage: centre-based perpendicularity and Pythagorean reasoning versus tangent-chord angles and isosceles-triangle theory. The AI's chain is logically complete under the hardened Q1(b) standard, so the different backbone yields D.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.150
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two interior angles of the regular pentagon to locate the incenter, show all five vertex angles are bisected by lines from that center (via I.4 and symmetry), drop perpendiculars to all five sides and prove them equal by AAS (I.26), then construct the inscribed circle and establish tangency via III.16. The AI adds supplementary reasoning -- computing the interior angle sum via 1.32, invoking P5 to justify the intersection of bisectors, and citing 1.16 to verify perpendicular feet lie on the side segments -- but these do not alter the backbone. The ai_only set consists entirely of over-citations: postulates (P1-P5), common notions (CN1, CN2, CN3, CN5), definitions (D1.10, D1.15, D3.2, D4.5), and construction or auxiliary propositions (1.9, 1.12, 1.16, 1.32) that Heath leaves implicit. The empty heath_only set confirms that every proposition Heath cites is also cited by the AI, with no substantive divergence.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: bisect two adjacent interior angles of the regular pentagon, find their intersection as the center, prove all five distances from center to vertices are equal, and circumscribe the circle. Heath compresses the equidistance argument with I.6 and repeated 'similarly' clauses, while the AI spells out each equality explicitly, using I.6 for one pair (OB = OC) and I.4 (SAS) for the remaining pairs. The ai_only set consists entirely of over-citations: postulates (P1, P2, P3, P5), the bisection construction (I.9), common notions (CN1, CN2, CN3, CN5), definitions (D1.15, D4.6), and the substantive but supporting citations I.17 (angle sum bound ensuring bisectors meet) and I.4 (SAS as an alternative route to the same equidistance conclusion). Heath_only is empty. The key intermediate conclusions appear at the same logical positions in both proofs, making this a same-backbone, different-depth case.

### 4.15
**Category**: Path difference
**Jaccard**: 0.150
**Analysis**: Q2 identified a genuine backbone divergence in the second half of the proof. Both proofs establish that all six central angles equal one-third of two right angles using the same method (equilateral triangle properties via I.5 and I.32, then supplementary and vertical angles). However, they diverge on how they conclude the hexagon is equilateral and equiangular. Heath routes through arc theory: equal central angles imply equal arcs (III.26), equal arcs imply equal chords (III.29) for the equilateral claim, and equal arcs imply equal inscribed angles (III.27) for the equiangular claim. The AI instead uses triangle congruence: equal radii and equal central angles give SAS-congruent radial triangles (I.4), yielding equal bases (equilateral) and equal base angles whose pairwise sums give equal interior angles (equiangular). The key intermediate 'equal arcs' in Heath is entirely absent from the AI proof, and the key intermediate 'congruent radial triangles via SAS' in the AI is absent from Heath. Since the AI's path is logically complete and valid, the classification is D.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.062
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: inscribe an equilateral triangle side (1/3 = 5/15 of the circumference) and an equilateral pentagon side (1/5 = 3/15), observe the difference arc is 2/15, bisect it with III.30 to obtain 1/15, then fit equal chords in contiguity to complete the 15-gon. Heath's proof is extremely terse, explicitly citing only 3.30, while implicitly relying on 4.2 (inscribed triangle), 4.11 (inscribed pentagon), 4.1 (fitting equal chords), 3.26/3.28 (equal arcs from equal chords/angles), and 3.27 (equal angles on equal arcs). The AI proof makes all of these implicit dependencies explicit, along with supporting axioms (CN1, CN2, CN3, CN5), postulates (P1), definitions (D4.3), and lower-level construction results (1.1, 1.5, 3.15). Since heath_only is empty and every ai_only item is either an implicit dependency Heath uses without citation or a foundational axiom/definition, this is a clear Case A granularity difference: same backbone, different citation depth.
