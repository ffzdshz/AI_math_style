# Book 3 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 25 | 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.11, 3.12, 3.14, 3.17, 3.18, 3.20, 3.21, 3.22, 3.23, 3.26, 3.27, 3.28, 3.29, 3.31, 3.32, 3.33, 3.34, 3.35, 3.36 |
| Path difference (D) | 12 | 3.1, 3.8, 3.9, 3.10, 3.13, 3.15, 3.16, 3.19, 3.24, 3.25, 3.30, 3.37 |
| AI proof error (E) | 0 |  |

**Total**: 37 propositions

## Per-Proposition Analysis

### 3.1
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 determined the classification. Heath's proof uses reductio ad absurdum: it constructs the midpoint F of a perpendicular chord CE, assumes some other point G is the centre, and derives a contradiction via I.8 (angle GDB would be right but angle FDB is already right, yielding greater equals less). The AI proof instead takes a direct constructive approach with case analysis: it proves the centre must lie on the perpendicular bisector of chord AB (handling O on AB and O not on AB separately, using I.8 in the latter case), then locates the centre by bisecting the resulting diameter. These are genuinely different key intermediate conclusions and different logical architectures (reductio vs. direct construction with cases), so the backbones differ (Case B). Q3 confirms the AI's path is valid: every step is properly supported by citations and sound reasoning, with no gaps under the hardened 1(b) standard.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: finding the center and establishing equal radii (via 3.1), deriving equal base angles (via I.5), applying the exterior angle theorem (I.16) to obtain an angle inequality, and converting that to a side inequality (via I.19) to show every point on the chord is closer to the center than the radius. The AI uses a direct proof rather than Heath's contradiction, and adds an explicit sub-case for the center lying on line AB, but the core geometric mechanism and key intermediate conclusions are identical. The ai_only set consists entirely of axiom-level over-citations (CN5, D1.15, P1) that Heath leaves implicit, and heath_only is empty. This is a clear Case A in Q2: same backbone, different citation depth.

### 3.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same biconditional through identical key intermediate conclusions: in the first direction, SSS congruence (I.8) yields equal adjacent angles, which are then right by definition (D1.10); in the second direction, equal radii give equal base angles (I.5), equal right angles and a shared side give triangle congruence (I.26), yielding equal segments. The AI proof cites four additional foundational items (CN4, D1.15, P1, P4) that Heath leaves implicit, all of which are common notions, definitions, or postulates rather than substantive propositions. Since heath_only is empty and the ai_only items are purely axiom-level over-citations, the backbones match and the difference is one of citation depth, yielding G.

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume for contradiction that two non-diametral chords bisect each other at E, find the centre, join it to E, apply 3.3 twice to conclude that two angles at E are both right, then observe that one angle is a proper part of the other, yielding a contradiction. The AI proof explicitly cites CN5 (whole greater than part), P1 (joining a line), and P4 (right angles are equal), which Heath invokes implicitly. Since heath_only is empty and all ai_only items are axiom-level citations (common notions and postulates) representing the same reasoning at greater depth, Case A of Q2 holds: same key intermediate conclusions, different citation depth.

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume a common centre, then show via the definition of centre (D1.15) that two radii force two geometrically unequal segments to be equal, yielding a contradiction. Heath's proof uses segments EC=EF and EC=EG along a random line EFG; the AI's proof uses OA=OB and OA=OC along a line from O through B to C. The key intermediate conclusion is identical in both: two segments, one a proper part of the other, are shown equal through the centre definition, producing a contradiction. The AI simply cites more foundational references explicitly (CN1 for transitivity, CN5 for the whole-greater-than-part axiom, D1.16 for the circle definition, P1 and P2 for line constructions), while Heath leaves these implicit. With heath_only empty and ai_only consisting entirely of common notions, definitions, and postulates, this is a clear case of over-citation at the same backbone, giving Granularity difference (G).

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use proof by contradiction assuming a common centre, then show that equal radii from that centre to points on each circle yield a contradiction with unequal distances. Heath draws a random line FEB through the supposed centre F to get FC = FB (first circle) and FC = FE (second circle), deriving FE = FB which contradicts FE < FB. The AI uses the touch point A and a chosen point B on the first circle (not on the second), finding C on the second circle along ray OB, to get OB = OA and OC = OA, deriving OB = OC which contradicts CN5 since B and C are distinct on the same ray. The key intermediate conclusions are the same: radii from the common centre are forced equal but the geometry makes them unequal. The entire ai_only set (CN1, CN5, D1.15, D1.16, D3.3, P1, P2) consists of definitions, common notions, and postulates that Heath uses implicitly without explicit citation. Heath has no explicit citations at all, so the Jaccard is 0.0, but this reflects only that the AI is more explicit about foundational references, not a path divergence.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: the triangle inequality (I.20) with radii equality establishes the greatest and least lines, the SAS inequality (I.24) with equal radii, common side, and angle comparison establishes the ordering of intermediate lines, and angle construction (I.23) combined with SAS congruence (I.4) proves that exactly two equal lines exist. The ai_only set consists entirely of common notions (CN2, CN3, CN5), definitions (D1.15, D1.17), and postulates (P1, P2), which are foundational items Heath uses implicitly but the AI cites explicitly. Since heath_only is empty and all key intermediate conclusions appear in both proofs at the same logical positions, this is Case A of Q2: same backbone, different citation depth.

### 3.8
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined the classification. Heath uses 1.21 (lines constructed within a triangle from its extremities are shorter than the remaining two sides) for the convex circumference ordering, while the AI employs angle comparison arguments and the hinge theorem (1.24) uniformly for both concave and convex cases. Since 1.21 does not appear inside the proof of 1.24 (containment test fails), this constitutes a genuine backbone difference rather than a citation-depth variation. The AI also takes a distinct approach to uniqueness, applying 1.7 directly to show at most one circumference point on each side of the least segment can yield a given distance, instead of Heath's construction-plus-contradiction method using 1.4 and previously proved ordering results. Both alternative paths are logically sound, so Q3 confirms the classification as D.

### 3.9
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification. Heath proves 3.9 directly by bisecting two chords (AB and BC), using I.8 to show the bisecting lines are perpendicular, invoking III.1 to conclude each perpendicular bisector passes through the center, and noting their unique intersection is D. The AI instead proves 3.9 by contradiction: assuming the point P is not the center, it finds the actual center O via 3.1, constructs the diameter through O and P, and applies 3.7 to conclude that at most two equal straight lines can fall from P on the circle, contradicting the hypothesis of three. These are fundamentally different logical backbones — direct construction versus proof by contradiction via a different theorem — placing this squarely in Case B of Q2. The AI's chain is logically complete under Q3(b), so the classification is D.

### 3.10
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath proves 3.10 by contradiction using the perpendicular-bisector method: assuming four intersection points, he bisects chords between them and draws perpendiculars that, by 3.1, must pass through the center, forcing both circles to share a single center in contradiction to 3.5. The AI takes a fundamentally different route: assuming three intersection points A, B, C, it notes that the center T of the second circle sends three equal radii TA = TB = TC to the circumference of the first circle, then invokes 3.7 (interior point) and 3.8 (exterior point) to show that at most two equal lines can fall from any point to a circle, yielding a contradiction in every case. The two backbones share no key intermediate conclusion: Heath never invokes 3.7 or 3.8, and the AI never constructs perpendicular bisectors. The AI's path is logically complete under Q3, so the classification is D.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy: assume the line through the two centers does not pass through the point of internal tangency, form a triangle with the two centers and the contact point, apply the triangle inequality, substitute equal radii, and derive a length contradiction. The key intermediate conclusions (triangle inequality on the centers-contact triangle, radii substitutions, length contradiction) are identical in both proofs. The only difference is citation depth: Heath leaves all references implicit (heath_refs is empty), while the AI explicitly cites 1.20 for the triangle inequality, 3.6 for the distinctness of centers, definitions D1.15, D1.16, D3.3, common notions CN1, CN2, CN5, and postulates P1, P2. Since the logical backbone is the same and the citation differences reflect only explicitness of referencing, this is a granularity difference.

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish a relationship between the center-to-center distance and the sum of the two radii to the contact point, then invoke I.20 (the triangle inequality) to derive a contradiction with the assumption that the centers and the contact point are not collinear. Heath's proof assumes the line FG does not pass through A and shows FG > FA + AG from the path FCDG while I.20 gives FA + AG > FG; the AI proof shows OP >= OT + PT from radii equalities and then applies I.20 to get OT + TP > OP if not collinear. The ai_only set consists entirely of definitions (D1.15, D1.16, D3.3), common notions (CN2, CN5), a postulate (P1), and one foundational result (3.6, that touching circles have distinct centers) -- all items Heath uses implicitly without citation. heath_only is empty. This is Case A: same backbone with different citation depth, yielding G.

### 3.13
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves the internal case by placing the contact points on the centre-line (3.11) and deriving a distance-domination contradiction (BG > HD implies BH much greater than HD, yet BH = HD), and the external case by an entirely separate argument using 3.2 (a chord falls inside a circle) to show the joining line is simultaneously inside one circle and outside the other. The AI instead unifies both cases: it applies 3.11 and 3.12 individually to each supposed contact point to establish that both contact points and both centres are collinear, then shows each centre must lie strictly between the two contact points (by equal radii and CN5), and derives AO < AQ = QB < OB = AO, a single contradiction covering both internal and external tangency. The backbones differ in structure (Heath separates cases with different methods; the AI merges them via betweenness), and the containment test confirms independence: 3.2 (heath_only) does not appear in Heath's proof of 3.12 (ai_only). The AI's chain is logically complete under the hardened 1(b) standard, so Q3 yields D.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.158
**Analysis**: Q2 decides the classification. Both proofs follow the same logical backbone: drop perpendiculars from the centre to the two chords, note that these perpendiculars bisect the chords (3.3), apply the Pythagorean theorem (1.47) to the resulting right triangles, and use the equality of radii to equate the sums of squares, then subtract equal terms to obtain the desired conclusion in each direction of the biconditional. The AI's sole heath_only gap (3.1, finding the centre) is a construction step the AI handles implicitly by assuming the centre exists. The AI's large ai_only set consists primarily of over-citations: definitions (D1.10, D1.15, D1.17, D1.22), common notions (CN1-CN5), postulates (P1, P4), and basic constructions (1.10, 1.3). The substantive ai_only propositions (2.4, 1.20) appear in ancillary arguments -- a lemma about equal squares having equal sides in Step 2, and the diameter special case in Step 7 -- that supplement the shared backbone without altering it. Since the key intermediate conclusions are the same and the differences are in citation depth and supplementary elaboration, this is a granularity difference.

### 3.15
**Category**: Path difference
**Jaccard**: 0.118
**Analysis**: Q2 revealed genuinely different backbones, and Q3 confirmed the AI's alternative path is valid, yielding category D. Heath's proof constructs an auxiliary chord MN at the same distance from the center as BC, uses 3.14 to establish MN = BC, then compares triangles by unequal included angles via 1.24 to show MN > FG. The AI's proof takes an entirely different route: it bisects the chords, obtains perpendicular distances via 3.3, applies the Pythagorean theorem (1.47) to right triangles formed by the radii and half-chords, then uses algebraic manipulation of squares (2.4) to show the half-chord of the nearer chord exceeds that of the more remote chord. The two proofs share almost no substantive citations (Jaccard 0.118), with heath_only containing 1.24 and 3.14 and ai_only containing 1.47, 2.4, 3.3 among others. Neither the containment test nor any logical defect applies; the AI's Pythagorean-algebraic chain is complete and sound.

### 3.16
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. The two proofs establish the same three assertions (tangent outside, no interposition, angle comparisons) but through genuinely different key intermediate conclusions at every stage. For Part 1, Heath uses the isosceles triangle theorem (I.5) in a contradiction proof, while the AI uses a direct distance comparison via I.17 and I.19. For Part 2, Heath drops a perpendicular from the center to the interposed line and derives a contradiction from radius vs perpendicular-distance inequality, whereas the AI constructs a symmetric point across a perpendicular foot using SAS congruence (I.4) and then invokes chord containment (3.2) to show every ray inside the angle immediately enters the circle. For Part 3, Heath argues indirectly from part 2, while the AI directly constructs rays at any given acute angle using I.23. These different backbones, confirmed by the very low Jaccard similarity (0.1) and the large set of substantive ai_only propositions (1.4, 1.12, 1.16, 1.23, 3.2), constitute a genuine path difference. The AI proof is logically complete under the hardened Q1(b) standard, so Q3(b) confirms a valid alternative path.

### 3.17
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct an auxiliary circle with the given point's distance as radius, use a perpendicular construction to create a right angle, apply SAS congruence (I.4) to transfer that right angle to the tangent point, and conclude tangency via III.16. The AI's ai_only set consists entirely of postulates (P1, P2, P3), common notions (CN4, CN5), definitions (D1.10, D1.15, D1.17, D3.2), and one construction proposition (1.11) that Heath uses implicitly without citing. Heath_only is empty. The AI also adds an extra case (point on the circumference), but the core argument for the main case matches Heath's backbone exactly, making this a citation-depth difference rather than a path difference.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: a contradiction argument assuming the radius to the point of contact is not perpendicular to the tangent, drawing a perpendicular from the center instead, and deriving two contradictory inequalities about the perpendicular distance versus the radius using I.17 and I.19. The AI proof elaborates steps that Heath leaves implicit, explicitly citing 1.12 for the perpendicular construction, 3.2 and D3.2 to justify the perpendicular foot lies outside the circle, CN5 for the whole-greater-than-part inference, and various definitions and postulates. Since heath_only is empty and all ai_only items are over-citations or explicit supporting details for the same logical backbone, this is Case A of Q2: same key intermediate conclusions, different citation depth.

### 3.19
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves 3.19 by contradiction: assuming the centre F is not on the perpendicular AC, he derives via 3.18 that FC is perpendicular to the tangent, yielding angle FCE equal to angle ACE (the less to the greater), a contradiction. The AI instead gives a direct proof: it establishes via 3.18 that OT is perpendicular to the tangent, notes the drawn line n is also perpendicular to the tangent at T, shows the adjacent angles sum to two right angles, and applies 1.14 to conclude OT and n are collinear, so the centre lies on n. The key intermediate conclusions differ fundamentally — Heath's pivotal step is an angle-inequality contradiction under the assumption the centre is off the perpendicular, while the AI's pivotal step is a collinearity argument via 1.14. This constitutes a genuine path difference. The AI's direct proof is logically complete and sound, so Q3 confirms D.

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: forming isosceles triangles from radii and applying I.5, then using the exterior angle theorem I.32 to establish the doubling relationship for each sub-angle, and finally combining results by addition (center inside the inscribed angle) or subtraction (center outside). The AI proof is more explicit about case enumeration (diameter, interior, exterior) and explicitly cites definitions (D1.15, D1.17, D3.9, D3.10), common notions (CN2, CN3, CN4), and postulates (P1, P2) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, common notions, and postulates rather than substantive theorems, this is a clear case of over-citation with identical backbone, yielding G.

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: find the center, apply 3.20 twice to show the central angle is double each inscribed angle, then conclude the inscribed angles are equal. The AI proof adds substantial over-citation (3.1 for finding the center, definitions D1.17/D3.6/D3.8/D3.9, postulates P1/P2, and common notions CN1/CN2/CN5) and an extra case analysis for arcs larger than a semicircle, but these are citation-depth elaborations, not backbone differences. heath_only is empty, confirming no missing steps. Since the backbones match but citation sets differ, this is a granularity difference.

### 3.22
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: drawing diagonals AC and BD, using the inscribed angle theorem (III.21) to equate angles in the same segment, and applying the triangle angle sum (I.32) to conclude that opposite angles of the cyclic quadrilateral sum to two right angles. The AI proof is more explicit, providing a full argument for both pairs of opposite angles rather than Heath's 'similarly' for the second pair, and citing foundational items (CN1, CN2, CN4, D3.8, D4.3, P1) that Heath leaves implicit. Since the key intermediate conclusions are identical and the citation differences are purely at the axiom and definition level, this is a granularity difference.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs argue by contradiction through the same backbone: assume two similar unequal segments on the same side of AB, construct a line through points on both arcs meeting at B, establish angle equality from the definition of similar segments (D3.11), then derive a contradiction via the exterior angle theorem (I.16). The AI proof adds explicit citations for the geometric configuration (3.10 to justify nesting of segments, definitions D3.6 and D3.8 for segment terminology, postulates P1 and P2 for line constructions, and CN4 for equality reasoning), but these elaborate on the same logical steps rather than introducing different key intermediate conclusions. With heath_only empty and ai_only consisting entirely of foundational items plus one configurational proposition, this is a clear Case A: same backbone at different citation depth.

### 3.24
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Both proofs use superposition to bring one segment onto the other's baseline, but the key reasoning step diverges. Heath argues by contradiction: if the segments do not coincide after superposition, one falls 'awry', meaning a circle cuts another circle at more than two points, contradicting III.10. The AI instead directly invokes III.23 (similar and unequal segments cannot be constructed on the same side of the same line) after superposition places both segments on the same base and same side. The proof-tree containment test confirms this is a genuine path difference: III.10 (heath_only) does not appear in Heath's proof of III.23 (which uses only Def. 11 and I.16), so these represent independent logical routes rather than citation-depth variation. The AI's path is valid, as III.23 directly yields equality once both segments share the same base and side. Q2 Case B leads to Q3, and Q3(b) holds, giving classification D.

### 3.25
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof proceeds by bisecting chord AC, drawing a perpendicular from the midpoint, then splitting into three cases based on whether angle ABD is greater than, equal to, or less than angle BAD, using I.6 (isosceles triangle theorem) and III.9 (circle through three equidistant points) to locate the center. The AI takes an entirely different path: it selects a third point C on the arc, constructs perpendicular bisectors of two chords AB and AC using I.10 and I.11, then applies III.3 (the perpendicular bisector of a chord passes through the center) to show the center lies on both perpendicular bisectors, with I.28 used to prove the two bisectors are distinct lines that must intersect at a unique point. This yields Jaccard 0.0 with completely disjoint citation sets, confirming different logical backbones. The AI's perpendicular-bisector method is logically complete and avoids the three-case structure entirely through a single general argument, making this a valid path difference.

### 3.26
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) equal radii from equal circles, (2) SAS (I.4) yields equal chords, (3) equal circumferential angles yield similar segments (D3.11), (4) similar segments on equal bases are equal (III.24), (5) subtracting equal segments from equal circles gives equal remaining circumferences. The AI proof adds explicit citations for definitions, common notions, and postulates that Heath leaves implicit, plus two substantive theorems (III.20 to unify the central and circumferential angle cases, I.13 for reflex angle handling) that elaborate on steps Heath treats more concisely. Since heath_only is empty and all ai_only items are either foundational over-citations or elaborations of the same logical steps, this is Case A of Q2: same backbone, different citation depth.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs use an identical contradiction strategy to establish one type of angle equality (construct an equal angle with I.23, apply III.26 to obtain arc equality, reach contradiction), then derive the other type via III.20. Heath proves central angles first and derives circumference angles by halving; the AI reverses this order, proving circumference angles first and deriving central angles by doubling. The key intermediate conclusions are the same in both proofs. The ai_only citations (CN1, CN2, CN5, D3.9, P1, P2) are exclusively common notions, definitions, and postulates that Heath uses implicitly, representing over-citation of foundational items rather than a substantive path difference.

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: establishing that radii of equal circles are equal, applying SSS (I.8) to show the central angles are equal, invoking III.26 to conclude the lesser arcs are equal, and subtracting from equal whole circumferences to obtain equal greater arcs. The AI proof adds an explicit diameter sub-case (using 3.15) and over-cites by listing definitions (D1.15, D1.17, D1.18, D3.1, D3.9), common notions (CN1, CN3, CN4), a postulate (P1), and a construction proposition (3.1) that Heath leaves implicit. Since heath_only is empty and all ai_only items are supplementary citations or an extra sub-case rather than different key intermediate conclusions, this is Case A of Q2: same backbone, different citation depth.

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: equal arcs yield equal central angles via 3.27, radii of equal circles are equal, and SAS (1.4) gives equal chords. The AI adds explicit case analysis distinguishing semicircular, minor, and major arcs (Steps 2-3) and cites many foundational items (definitions D1.15, D1.17, D3.1, common notions CN3-CN5, postulate P1, and construction proposition 3.1) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, common notions, postulates, or a construction tool, this is classic over-citation with the same underlying argument, placing it squarely in Case A of Q2.

### 3.30
**Category**: Path difference
**Jaccard**: 0.083
**Analysis**: The classification is decided at Q2-Q3. Both proofs construct a perpendicular from the midpoint of chord AB to the arc and use I.4 (SAS) to establish triangle congruence. However, they extract different conclusions from the congruence and employ different bridge propositions to reach arc equality: Heath extracts chord equality (AD = DB) and applies III.28 (equal chords cut off equal arcs), while the AI extracts inscribed angle equality (angle BAC = angle ABC) and applies III.26 (equal inscribed angles stand on equal arcs). Since III.28 does not appear in the proof tree of III.26, the containment test confirms these are independent logical routes rather than a depth difference. The AI's path through inscribed angles is logically complete and valid, yielding a genuine path difference (D).

### 3.31
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: The forward dependency gate passes (all AI theorem citations precede 3.31). Q1 finds no logical errors: all five parts of this multi-case proposition are addressed, and every step is supported by cited propositions or sound reasoning. Q2 reveals that both proofs share the same backbone of key intermediate conclusions: both use I.5 on isosceles triangles formed by radii to decompose the inscribed angle, both apply I.32 (exterior angle theorem) to establish the angle in a semicircle is right via D1.10, both conclude the angle in the greater segment is less than a right angle, both use III.22 on a cyclic quadrilateral to show the angle in the less segment is greater than a right angle, and both handle the angles of the segments. The single heath_only citation (I.17) is replaced by a logically equivalent micro-argument: the AI derives angle ABC < R directly from angle ABC + angle ACB = R and CN5, whereas Heath invokes I.17 to reach the same conclusion. The 17 ai_only items consist overwhelmingly of definitions, common notions, postulates, and construction propositions that Heath leaves implicit, representing over-citation rather than a different proof path. Q2 Case A (same backbone, different citation depth) applies, yielding G.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Both proofs follow the same logical backbone: establishing that the tangent is perpendicular to a diameter through the point of contact, using the angle in a semicircle (3.31), decomposing a right angle via the triangle angle sum (1.32), subtracting to obtain the first tangent-chord angle equality, and applying the cyclic quadrilateral property (3.22) for the second. The AI uses 3.18 (radius to contact point is perpendicular to tangent) where Heath uses its converse 3.19 (line perpendicular to tangent at contact passes through center); since 3.19 itself depends on 3.18, they establish the identical geometric fact at slightly different citation depth. The AI additionally cites 3.21 (angles in the same segment are equal) to generalize from a specific inscribed angle to all such angles, and explicitly lists construction steps (3.1, 3.2), definitions, common notions, and postulates that Heath leaves implicit. These are citation-depth differences, not backbone differences. Q2 Case A holds, yielding G.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.130
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct the given angle at one endpoint of the line, locate the circle center on the perpendicular bisector of AB, show the circle passes through both endpoints via I.4, establish tangency via III.16, and conclude that the angle in the appropriate segment equals the given angle via the tangent-chord relationship. The AI gives a unified argument covering all three angle types (acute, right, obtuse) through III.32 alone, while Heath separates into three explicit cases and uses III.31 for the right-angle case; this is a presentation choice, not a backbone difference, since III.32 subsumes the right-angle result of III.31. The large ai_only set (19 items) consists entirely of definitions, common notions, postulates, and construction propositions that Heath leaves implicit, confirming over-citation rather than path divergence. The sole heath_only item (3.31) is subsumed by the AI's uniform application of III.32. Same key intermediate conclusions at different citation depth yields G.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs follow an identical backbone: draw a tangent to the circle, construct an angle between the tangent and a chord equal to the given angle using I.23, then apply the alternate segment theorem III.32 to conclude the angle in the alternate segment equals the given angle. The AI's seven extra citations (ai_only: 3.17, 3.2, CN1, D3.6, D3.8, P1, P2) are all over-citations of construction propositions, definitions, common notions, and postulates that Heath invokes implicitly without explicit reference. Heath cites nothing the AI omits (heath_only is empty). This is Case A of Q2: same key intermediate conclusions with different citation depth, yielding Granularity difference.

### 3.35
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a trivial case when the intersection is at the centre (equal radii yield equal rectangles), followed by establishing for each chord the identity rect(segments) + sq(distance-to-centre) = sq(radius) using III.3 for bisection, II.5 for the rectangle identity, and I.47 for the Pythagorean theorem, then combining via equal radii and subtracting the common square. The AI proof is more granular, handling additional sub-cases explicitly and citing foundational items (definitions D1.15, D1.22, D2.1; common notions CN1-CN4; postulate P1; construction propositions 1.10 and 3.1) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations of foundational elements, Case A of Q2 holds: same backbone, different citation depth.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.267
**Analysis**: Q2 decided the classification. Both proofs handle the same two cases (secant through the centre, secant not through the centre) and argue through identical key intermediate conclusions: tangent perpendicularity via III.18, bisection of the chord (implicit or via III.3), application of II.6 to the bisected-and-extended chord, Pythagorean theorem I.47 on right triangles, and cancellation using equal radii. The ai_only set consists entirely of over-cited foundational items (1.10 for bisection construction, 3.1 for finding the centre, common notions CN1-CN4, definitions D1.15/D1.17/D1.22/D2.1, and postulate P1) that Heath leaves implicit, while heath_only is empty. Since the logical backbones coincide and the citation difference reflects only citation depth, this is a granularity difference.

### 3.37
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decides this classification as D. Both proofs share the opening strategy of constructing a tangent and applying III.36 to equate squares, but their key intermediate conclusions diverge thereafter. Heath uses triangle congruence (I.8): he shows DE = DB, then with FE = FB and FD common concludes triangles DEF and DBF are congruent, transferring the known right angle at E to B. The AI instead uses the Pythagorean theorem and its converse (I.47, I.48): after establishing AT squared equals AD squared, it applies I.47 to the right triangle OAT to get OA squared = OT squared + AT squared, substitutes equal radii and equal squares to obtain OA squared = OD squared + AD squared, then invokes I.48 to conclude angle ODA is right. The containment test was checked since heath_only contains 1.8 which appears inside the proof of AI-cited I.48, but Heath is not re-deriving I.48 inline; rather Heath uses I.8 in an entirely independent congruence-based route that never reconstructs the Pythagorean converse argument. These are genuinely different logical backbones yielding a valid path difference.
