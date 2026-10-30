# Book 4 — Classification Report (Fable)

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
