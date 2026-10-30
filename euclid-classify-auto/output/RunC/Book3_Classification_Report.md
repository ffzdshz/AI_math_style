# Book 3 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 24 | 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 3.11, 3.12, 3.14, 3.16, 3.18, 3.19, 3.20, 3.21, 3.23, 3.27, 3.28, 3.29, 3.30, 3.32, 3.33, 3.34, 3.36, 3.37 |
| Path difference (D) | 13 | 3.3, 3.8, 3.9, 3.10, 3.13, 3.15, 3.17, 3.22, 3.24, 3.25, 3.26, 3.31, 3.35 |
| AI proof error (E) | 0 |  |

**Total**: 37 propositions

## Per-Proposition Analysis

### 3.1
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct a chord AB, bisect it, draw a perpendicular, bisect the resulting diameter, then prove by contradiction that the midpoint of the diameter is the centre using SSS congruence (I.8) to show that an assumed alternative centre would force two right angles at the same point to be equal when one is a proper part of the other. The AI proof cites eight additional foundational items (1.10, 1.11, CN5, D1.15, D1.16, P1, P2, P4) that Heath leaves implicit, all of which are construction propositions, postulates, definitions, or common notions rather than substantive theorems introducing a different proof path. Heath's citation set is a proper subset of the AI's, with heath_only empty. This is a clear case of over-citation at the foundational level, not a different argumentative route.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate geometric conclusions: equal base angles of the isosceles triangle formed by two radii (I.5), the exterior angle inequality at the arbitrary point on the chord (I.16), combining these to get a strict angle inequality, and then applying I.19 to conclude the side opposite the larger angle is greater, yielding that the distance from center to the arbitrary point is less than the radius. The structural difference (Heath uses proof by contradiction assuming the line falls outside; the AI uses a direct proof taking an arbitrary point on the segment) does not change the geometric backbone. The citation difference is entirely non-substantive: the AI explicitly cites D1.15 (definition of circle) and P1 (postulate for joining lines) where Heath uses them implicitly. heath_only is empty, confirming the AI covers all of Heath's cited results. This is Case A of Q2: same backbone, different citation depth.

### 3.3
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs handle the two cases of the biconditional. Case 1 (bisection implies right angles) uses the same backbone in both proofs: SSS congruence via I.8 followed by the definition of right angles. However, Case 2 (right angles implies bisection) diverges fundamentally. Heath argues through I.5 (isosceles base angles) and I.26 (AAS triangle congruence) to establish AF=FB, while the AI uses I.47 (the Pythagorean theorem) to set up equations on the squares of the sides, then applies CN1 and CN3 to algebraically derive that the square on AE equals the square on EB, concluding AE=EB. These are genuinely different key intermediate conclusions: Heath's path goes through angle equality and triangle congruence, while the AI's path goes through the Pythagorean relation and algebraic subtraction of squares. The AI's path is logically valid, making this a path difference (D).

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: assuming the two chords bisect each other at E, finding center F, joining FE, showing FE perpendicular to AC (so angle FEA is right) and FE perpendicular to BD (so angle FEB is right) via 3.3, then deriving the contradiction that the two right angles are equal yet one is a proper part of the other. The AI proof cites CN5 (whole greater than part), P1 (drawing FE), and P4 (all right angles are equal), which are axioms and postulates that Heath uses implicitly without citation. Since heath_only is empty and ai_only consists entirely of foundational axioms/postulates/common notions, this is a clear case of the AI over-citing at a finer granularity while following the same logical backbone. Case A of Q2 applies: same backbone, different citation depth.

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs follow identical logical backbones: assume the two intersecting circles share a centre E, establish EC = EF (from E being centre of circle ABC) and EC = EG (from E being centre of circle CDG), derive EF = EG, then note that F lies between E and G so EG > EF, reaching a contradiction. The key intermediate conclusions are the same in both proofs at the same logical positions. The ai_only set consists entirely of CN1, CN5, P1, and P2 -- all common notions and postulates that Heath uses implicitly but the AI cites explicitly. CN1 justifies the transitive equality step, CN5 justifies the 'less to the greater' inequality, and P1/P2 justify the line constructions. Heath's proof performs the same steps without citing these foundational axioms. The empty heath_only set confirms there are no substantive propositions the AI omits. This is a clear case of over-citation by the AI, fitting Case A (same backbone, different citation depth).

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume a common centre F for circles ABC and CDE touching at C, join FC and draw line FEB, establish FC = FB (F is centre of ABC) and FC = FE (F is centre of CDE), derive FE = FB by transitivity, then note FE < FB since E lies between F and B, reaching a contradiction. The key intermediate conclusions are the same in both proofs. The citation difference arises because the AI explicitly cites foundational items (CN1, CN5, D1.15, D1.16, D3.3, P1, P2) that Heath leaves implicit. Heath cites no prior propositions at all, and the AI also cites no prior propositions — its ai_only set consists entirely of definitions, common notions, and postulates. This is a classic over-citation pattern representing a difference in citation granularity, not a difference in proof strategy.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions through the same logical backbone: (1) FA is greatest via the triangle inequality (1.20) and radii equality, (2) FD is least via the triangle inequality and subtraction, (3) nearer lines are greater than more remote lines via the SAS inequality (1.24) with equal radii and unequal included angles, and (4) exactly two equal lines exist via angle construction (1.23), SAS congruence (1.4), and a uniqueness argument by contradiction. The AI's additional citations (CN3, D1.15, D1.16, P1, P3) are all foundational items -- a common notion for subtraction, definitions justifying radii equality, and postulates for line-drawing constructions -- that Heath invokes implicitly. Heath_only is empty, confirming that the AI covers everything Heath cites. This is a classic over-citation pattern where the AI makes explicit the foundational steps that Heath leaves tacit, with no difference in the logical backbone.

### 3.8
**Category**: Path difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. While both proofs establish the same overall conclusions (ordering on concave circumference, ordering on convex circumference, uniqueness of equal lines), the logical paths diverge in two substantive ways. First, for the convex circumference ordering, Heath uses 1.21 (lines constructed within a triangle are less than the remaining two sides) to show DK < DL, while the AI uses 1.24 (SAS inequality) with an angle comparison argument noting that B lies between A and M, making the angle at M directly comparable. Second, for the uniqueness argument, Heath constructs the equal angle directly and uses 1.4, then argues by contradiction citing the earlier ordering result, while the AI uses 1.23 to construct the angle, 1.4 for SAS congruence, and then 1.8 (SSS) in the contradiction argument. These are genuinely different intermediate reasoning steps (not merely different citation depth), confirmed by the fact that heath_only items (1.21, 3.1) are not subsumed by any higher-level proposition the AI cites. The AI's alternative path is logically valid throughout, so the classification is D rather than E.

### 3.9
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3. Heath proves 3.9 constructively by joining chords, bisecting them, and using triangle congruence (I.8) to show the bisectors are perpendicular, then applying III.1 to conclude the center lies on each perpendicular bisector, with their unique intersection at D establishing D as the center. The AI instead uses proof by contradiction: assuming D is not the center and invoking Proposition 3.7, which states that from a non-center interior point only two equal straight lines can fall on the circle, directly contradicting the hypothesis that more than two equal lines fall from D. These are fundamentally different logical backbones — constructive perpendicular-bisector argument versus indirect argument via 3.7 — making this a genuine path difference. The AI's contradiction proof is logically complete and valid, so Q3 yields D.

### 3.10
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Classification was decided at Q2/Q3. Heath's proof uses perpendicular bisectors of chords connecting intersection points to show that both circles share the same center (contradicting III.5), citing only III.1 and III.5. The AI proof takes a fundamentally different approach: it finds the center K of one circle via III.1, observes that three equal radii KB=KG=KF fall from K onto the second circle (by D1.15), then performs an exhaustive case analysis on K's position relative to the second circle — inside (contradicted by III.9 implying K is also center of circle 2, violating III.5), outside (contradicted by III.8 allowing at most two equal lines), or on the circumference (contradicted by III.7 allowing at most two equal lines from a non-center point on the diameter). These are genuinely different logical backbones: Heath derives a shared center via perpendicular bisector geometry, while the AI derives contradictions via equal-line-count propositions III.7/III.8/III.9. The AI's path is logically complete — every step is supported by valid citations and the case analysis is exhaustive — so Q3(b) holds, yielding D.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs use identical logical backbones: a proof by contradiction assuming the line joining the centres does not pass through the point of contact, applying the triangle inequality to derive that a radius of one circle exceeds a radius of the other (or a segment that should be larger), yielding a contradiction. Heath's proof cites no explicit references (heath_refs is empty), while the AI explicitly cites 1.20 (triangle inequality), CN5 (whole greater than part), D1.15 (definition of circle/centre), and P1 (joining lines) -- all foundational items that Heath uses implicitly without citation. The key intermediate conclusions are the same in both proofs: the contradiction setup, the triangle inequality application, the radii equalities, and the final contradiction. The only difference is that the AI over-cites foundational references that Heath leaves implicit, which is a classic citation-depth difference (Case A of Q2).

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Both proofs use the same proof-by-contradiction strategy: assume the line joining the centres does not pass through the point of contact, form a triangle with the centres and the contact point, apply I.20 (triangle inequality), and derive a contradiction by comparing the sum of radii to the centre-to-centre distance. The key intermediate conclusions are the same backbone: radii from each centre to the contact point equal radii to points where the centre line meets each circle, and I.20 provides the contradicting inequality. The AI proof explicitly cites D1.15 (definition of circle/centre), D3.3 (definition of externally tangent circles), CN5 (whole greater than part), and P1 (joining points by a line), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only consists entirely of definitions, common notions, and a postulate, this is a clear Case A in Q2: same backbone with different citation depth, classifying as G.

### 3.13
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 reveals different backbones in both cases. For the internal tangency case, Heath derives a metric contradiction by comparing radii directly (BG = GD implies BG > HD, but BH = HD gives BH much greater than HD, contradiction), while the AI argues that collinearity plus equal radii forces both centers to be the midpoint of the segment between contact points, so the centers coincide, contradicting 3.6. For the external tangency case, Heath uses 3.2 (a chord falls within each circle) combined with D3.3 (external tangency means the chord falls outside one circle) to reach contradiction, while the AI uses 3.12 (line through centers passes through contact point) and the same midpoint-coincidence argument with 3.6. These are genuinely different logical paths: Heath never invokes 3.6, 3.12, or the midpoint argument, and the AI never invokes 3.2 or the metric inequality. Both paths are logically complete, so the classification is D.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions in both directions of the biconditional: perpendiculars from the center bisect the chords (III.3), halves of equal chords are equal, radii are equal, the Pythagorean theorem (I.47) yields squared equalities on the perpendicular distances, and subtraction of equals yields the result. The citation differences are purely at the granularity level: the AI over-cites foundational items (CN1, CN2, CN3 for arithmetic on equals, D1.15 for the definition of radius, P1 for drawing lines) that Heath uses implicitly, while Heath explicitly cites III.1 to find the center of the circle, which the AI assumes as given without citation. All ai_only items are common notions, definitions, or postulates (over-citation), and the single heath_only item (3.1) is a construction proposition for locating the center, which the AI handles by simply positing the center without formal citation. The logical backbone is the same throughout.

### 3.15
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 determined the classification. Both proofs establish the same two-part conclusion (diameter is greatest; nearer chord is greater) but through fundamentally different backbones. For Part 1, Heath constructs an auxiliary chord MN equal to BC using 3.14 and then applies the triangle inequality (1.20), while the AI directly applies the triangle inequality to the triangle formed by the center and the chord endpoints, noting BC equals the sum of two radii. For Part 2, Heath uses the SAS inequality theorem (1.24) on triangles with equal sides but unequal included angles, while the AI uses perpendicular bisection of chords (3.3) combined with the Pythagorean theorem (1.47) and algebraic manipulation of squares to compare half-chord lengths. The key intermediate conclusions differ in both parts: Heath's proof pivots on 3.14 and 1.24 (neither cited by the AI), while the AI's proof pivots on 1.47 and 3.3 (neither cited by Heath). The AI's path is logically valid throughout, satisfying Q3, so the classification is D.

### 3.16
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same three-part structure with identical key intermediate conclusions: (i) the tangent falls outside the circle by contradiction via an isosceles triangle (I.5) yielding two right angles in a triangle (contradicting I.17); (ii) no line can be interposed between the tangent and circumference, shown by dropping a perpendicular from the center to the supposed interposed line and using I.19 to show the foot of the perpendicular lies inside the circle, forcing the interposed line to cross the circumference; (iii) the angle of the semicircle exceeds any acute rectilineal angle and the horn angle is less, by showing any such angle would require an interposed line contradicting part (ii). The AI cites all three of Heath's references (1.5, 1.17, 1.19) plus ten additional items: definitions (D1.10, D1.12, D1.15, D1.17, D3.7), postulates (P1, P4), a construction proposition (1.12), and two substantive propositions (3.2, 3.7) that make explicit the reasoning Heath leaves implicit about points inside the circle and chords crossing the circumference. Since heath_only is empty and all ai_only items represent over-citation of steps that Heath performs without explicit reference, this is a citation-depth difference with the same logical backbone.

### 3.17
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 decides the classification as D (Path difference). Heath's proof constructs an auxiliary circle centered at E with radius EA, draws a perpendicular DF to EA, and uses triangle congruence (I.4) to show that angle EBA equals the right angle EDF, concluding tangency by III.16. The AI proof uses a fundamentally different construction: it bisects AE at midpoint M, draws a Thales circle with center M and radius MA, finds the intersection B with the given circle, and then proves angle ABE is a right angle through an elaborate but valid argument using isosceles triangle properties (I.5), supplementary angles (I.13), and angle sum in triangles (I.32). The key intermediate conclusions differ in both construction and logical method — Heath relies on SAS congruence while the AI relies on Thales circle properties proved via angle arithmetic. Additionally, the AI covers an extra case (point on the circle) not explicitly treated by Heath. The AI's path is logically complete and valid, satisfying Q3.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Both proofs use the same proof-by-contradiction structure: assume FC is not perpendicular to DE, draw FG perpendicular to DE, establish that angle FGC is right and angle FCG is acute (I.17), then conclude FC > FG (I.19). The key intermediate conclusions through step 3 are identical in both proofs. The proofs diverge only in how they articulate the final contradiction: Heath compresses it into FC = FB (radii) so FB > FG which is impossible, while the AI expands it by explicitly arguing that G lies inside the circle (D1.15), so DE cuts the circle (3.2, 3.16), contradicting tangency (D3.2). This divergence is a matter of citation depth, not a different logical backbone. The AI over-cites by including construction references (1.12), definitions (D1.10, D1.15, D3.2), a postulate (P1), and substantive propositions (3.2, 3.16) that merely expand the contradiction step Heath handles tersely. Since heath_only is empty, every Heath citation appears in the AI set, confirming no substantive step is missing. Q2 Case A applies: same backbone, different depth. Classification is G.

### 3.19
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction assuming the centre F lies off the perpendicular line CA, using III.18 to show FC is also perpendicular to the tangent DE, yielding two right angles at the point of contact where one is part of the other, which is impossible. The AI proof adds explicit citations to foundational items (P4 for equality of right angles, CN5 for whole-greater-than-part, D1.10 for right angle definition, D3.2 for tangent definition) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, common notions, and postulates, this is a clear case of over-citation at a deeper foundational level, making this a granularity difference.

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions using the identical logical backbone: (1) radii are equal so base angles of the isosceles triangle are equal (I.5), (2) the exterior angle of the triangle equals the sum of the two remote interior angles (I.32), giving the doubling relationship for each sub-angle, and (3) combining via addition or subtraction for the different cases. The AI proof covers three explicit cases (center on a side, center inside the angle, center outside the angle) while Heath covers two, but the underlying reasoning is the same. The ai_only set consists entirely of definitions (D1.15, D1.16, D3.8, D3.9), common notions (CN2, CN3), and postulates (P1, P2) — all foundational items that Heath uses implicitly without citation. The heath_only set is empty. This is a classic over-citation pattern where the AI explicitly cites construction and axiomatic foundations that Heath leaves implicit, constituting a citation-depth difference with the same backbone (Case A of Q2).

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: find the center of the circle, apply III.20 twice to show that the central angle subtending the chord is double each of the two inscribed angles in the same segment, then conclude the inscribed angles are equal. The AI proof cites additional items (3.1 for finding the center, P1 for joining lines, CN1 for the equality inference, D1.15 and D3.8 for definitions) that Heath leaves implicit, but these are all construction steps, postulates, common notions, and definitions — classic over-citation of non-substantive steps. Since heath_only is empty and the ai_only items are entirely non-substantive, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 3.22
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof joins the diagonals AC and BD, forms triangle ABC, uses I.32 (triangle angle sum equals two right angles) and III.21 (angles in the same segment are equal) to show that angle ADC equals the sum of angles BAC and ACB, then adds angle ABC to both sides to conclude that ABC + ADC = two right angles. The AI takes a fundamentally different approach: it finds the center O, applies III.20 (central angle is double the inscribed angle) to show that the two central angles at O corresponding to the two opposite inscribed angles are each double those inscribed angles, then argues that these two central angles partition the full revolution around O (four right angles, via I.13), so the two inscribed angles sum to two right angles. The key intermediate conclusions are entirely different -- Heath never uses the center or central angles, and the AI never uses diagonals, triangles, or the inscribed-angles-in-same-segment theorem. This is a genuine path difference with a valid alternative proof strategy, yielding classification D.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: assume two similar unequal segments ACB and ADB on the same side of AB, establish that a line from A through a point D on the outer arc crosses the inner arc at C, form a triangle BCD, and derive a contradiction by showing that the angle at C (exterior angle) must be both greater than (by I.16) and equal to (by Def. 3.11, similarity) the angle at D. The AI proof is more explicit in its construction and justification, citing D3.6 (definition of segment), D3.8 (definition of angle in a segment), and P1 (postulate for drawing lines), none of which Heath cites because he uses them implicitly. The heath_only set is empty, confirming that the AI covers all of Heath's reasoning. The difference is purely one of citation depth, not logical path.

### 3.24
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Both proofs use superposition: they apply segment AEB onto CFD, note that B coincides with D because AB equals CD, and then argue by contradiction that the segments must coincide. However, the key intermediate conclusion establishing the contradiction differs. Heath argues that if the segments do not coincide, a circle cuts a circle at more than two points, which is impossible by 3.10. The AI instead argues that non-coincidence would produce two similar and unequal segments on the same side of the same straight line, which is impossible by 3.23. Since 3.23 and 3.10 are substantive propositions establishing different geometric facts (3.23 concerns similar unequal segments on the same side of a line; 3.10 concerns circles cutting at more than two points), the backbones genuinely diverge at the contradiction step, making this Case B. The AI's path via 3.23 is logically valid since the superposed segment is similar to CFD by hypothesis and unequal by assumption, directly triggering 3.23's impossibility result. Q3 confirms the AI's different path is sound, yielding classification D.

### 3.25
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Both proofs share the same construction (bisect AC at D, draw DB perpendicular to AC, join AB) and the same three-case structure establishing that AE = BE = CE. The key intermediate conclusions are identical across all three cases. However, the final concluding argument differs substantively: Heath uses III.9 (if more than two equal straight lines fall from a point to a circle, that point is the center) to directly identify E as the center, while the AI constructs a new circle with center E and radius EA, shows it passes through A, B, and C via D1.15, and then invokes III.10 (a circle does not cut another at more than two points) to argue the constructed circle must be the same as the original. Since III.9 does not appear inside the proof of III.10 and these represent genuinely different logical strategies for the final step, the proof-tree containment test does not reduce this to a granularity difference. The AI's path is valid but distinct, yielding classification D.

### 3.26
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. For the centres case, Heath establishes arc equality by showing BC = EF via I.4, then arguing that segments BAC and EDF are similar (Def. 11), applying III.24 to conclude the similar segments on equal lines are equal, and finally subtracting the equal segments from the equal whole circles to get equal remaining circumferences. The AI instead uses a superposition method: after establishing BC = EF via I.4, it places one circle on the other so that centres, radii, and points coincide, then invokes CN4 (things that coincide are equal) to conclude the arcs are equal. For the circumferences case, Heath handles it through similar segments and III.24 as part of a unified argument, while the AI uses III.20 (central angle is double the inscribed angle) and CN2 to reduce the circumferences case to the already-proved centres case. The key intermediate conclusions differ substantively: Heath's backbone runs through similar segments and III.24, while the AI's runs through superposition (centres case) and III.20 with angle-doubling (circumferences case). Both paths are logically complete, so this is a genuine path difference.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: a proof by contradiction showing the central angles must be equal (assuming inequality, constructing an equal angle via I.23, applying III.26 to get equal arcs, deriving a contradiction), then using III.20 to transfer the result to inscribed angles. The AI proof explicitly cites CN1 (transitivity of equality for arcs BK and BC both equaling EF) and CN5 (whole is greater than part, for the contradiction) at the same logical positions where Heath uses these Common Notions implicitly. Since the key intermediate conclusions are identical and the only differences are the AI's explicit citation of foundational axioms that Heath leaves tacit, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs follow the same logical backbone: establish that radii of equal circles are equal, form two triangles with equal sides (two radii and the given equal chord), apply I.8 (SSS) to show the central angles are equal, invoke III.26 to conclude the minor arcs are equal, then subtract from the whole equal circles to conclude the major arcs are equal. The ai_only set {3.1, CN3, D3.1, P1} consists entirely of a construction proposition (3.1 for finding the center), a common notion (CN3 for subtracting equals), a definition (D3.1 for equal circles having equal radii), and a postulate (P1 for joining lines) — all of which Heath uses implicitly but does not cite explicitly. The heath_only set is empty, confirming the AI covers everything Heath cites. This is a classic Case A same-backbone situation with the AI providing finer citation granularity.

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) equal circumferences in equal circles yield equal central angles via III.27, (2) equal circles have equal radii, and (3) SAS congruence via I.4 gives BC = EF. The AI proof adds three over-citations not in Heath: 3.1 (finding centers), P1 (joining lines), and D3.1 (definition of equal circles), all of which are construction-level or definitional references whose underlying facts Heath states but does not formally cite. Since heath_only is empty and all ai_only items are construction/axiomatic over-citations with the same backbone present in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 3.30
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: bisecting AB at C, drawing CD perpendicular to AB, proving AD = DB by SAS (I.4), and concluding arc AD = arc DB via III.28 (equal chords cut off equal arcs). The ai_only citations (1.10, 1.11, P1, D1.10, D3.1) are exclusively construction propositions (bisecting a line, drawing a perpendicular), a postulate (joining points), and definitions (right angle, equal circles) that Heath leaves implicit. The heath_only set is empty, confirming no substantive step is missing from the AI proof. The AI's Step 8 explicitly justifying that a circle is equal to itself (via D3.1) to satisfy III.28's hypothesis about equal circles is an extra granularity step, not a different logical path. Since the backbones match and all differences are citation-depth matters, this is a granularity difference.

### 3.31
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: The classification is decided at Q2/Q3. Both proofs share the same backbone for the semicircle-right-angle case (I.5 twice for isosceles triangles, then I.32 and D1.10) and for the lesser-segment-obtuse case (III.22). However, for the greater-segment-acute case, the proofs diverge substantively: Heath uses I.17 (two angles of a triangle are less than two right angles) to conclude directly that angle ABC is less than a right angle given that BAC is right, while the AI uses III.20 (the inscribed angle theorem relating central and inscribed angles) to show that the inscribed angle standing on the minor arc must be less than a right angle. Since I.17 does not appear inside the proof of III.20, this is a genuinely different logical path, not a containment/granularity difference. Additionally, for the angle-of-segment parts (4 and 5), the AI explicitly invokes III.16 where Heath treats the result as manifest. The AI's alternative path via III.20 is logically valid, so Q3(b) holds, yielding classification D.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: (1) BA is a diameter and angle ABF is right, (2) angle ADB is right by 3.31, (3) angles ABD + BAD equal one right angle by 1.32, (4) angle DBF equals angle BAD by subtraction, (5) opposite angles of inscribed quadrilateral ABCD sum to two right angles by 3.22, and (6) angle DBE equals angle BCD by subtraction. The sole heath_only citation 3.19 (perpendicular to tangent passes through center) and the AI's citation of 3.18 (line from center to tangent point is perpendicular) are converses used to establish the same geometric fact. Indeed, Heath's proof of 3.19 itself relies on 3.18, so the AI is citing the more fundamental result directly. The remaining ai_only items (1.13, 3.21, D1.17, D3.2, D3.8, P1) are explicit citations of supplementary angle facts, angle-in-segment equality, definitions, and postulates that Heath leaves implicit. This is a clear case of same backbone with different citation depth.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions across all three cases (acute, right, obtuse): bisecting AB and using I.4 to show the circle passes through both endpoints, invoking III.16 to establish tangency of AD, and applying III.32 to equate the constructed angle with the angle in the alternate segment (with III.31 handling the right-angle case via semicircle). The AI proof's backbone matches Heath's exactly. The citation difference is entirely due to over-citation: the AI explicitly cites construction propositions (1.10, 1.11, 1.23), definitions (D1.15, D1.17, D1.18, D3.6, D3.8), and postulates (P1, P3) that Heath uses implicitly without formal citation. Heath_only is empty, confirming the AI captures all of Heath's cited steps. This is a same-backbone, different-depth situation (Case A in Q2), yielding Granularity difference.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct a tangent to the circle at a point B, construct angle FBC equal to the given angle D using I.23, then apply the alternate segment theorem III.32 to conclude that the angle in segment BAC equals angle D. The AI proof's additional citations (1.11, 3.1, 3.16, P1) all pertain to the explicit construction of the tangent line, which Heath handles implicitly with 'Let EF be drawn touching ABC at the point B.' The heath_only set is empty, confirming that Heath cites nothing beyond what the AI also cites. The ai_only items are purely construction and foundational references (finding center, drawing a line, erecting a perpendicular, tangent characterization), representing over-citation of construction details rather than any difference in logical path. This is a clear Case A in Q2: same backbone, different citation depth.

### 3.35
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: The AI proof uses a fundamentally different case structure from Heath's proof. Heath divides into two cases (both chords through the centre; neither through the centre), while the AI divides into three cases (both through centre; exactly one through centre; neither through centre) and reduces Case 3 to Case 2 by constructing a diameter through the intersection point E. In Heath's main case, perpendiculars are drawn from the centre to both chords, both are bisected by III.3, and II.5 plus I.47 are applied symmetrically to both chords. In the AI's Case 2, one chord is the diameter itself so II.5 is applied differently (the diameter is bisected at the centre rather than by a perpendicular), producing a distinct chain of intermediate conclusions. The AI's Case 3 reduction via a constructed diameter is an entirely different strategy from Heath's direct argument. Since the key intermediate conclusions and case organization differ but the AI's chain is logically sound throughout, this is classified as D (path difference) at Q2/Q3.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs address the same two cases (secant through the center, secant not through the center) and establish identical key intermediate conclusions in each case: angle at tangent point is right (III.18), the chord is bisected (by the center in Case 1, by perpendicular from center in Case 2 via III.3), application of II.6 to get the rectangle plus a square equals another square, repeated applications of I.47 (Pythagorean theorem) to replace sums of squares, equality of radii, and subtraction to reach the final result. The ai_only set consists entirely of over-citations: construction propositions (1.12, P1), common notions (CN1, CN2, CN3), and definitions (D1.15, D1.17) that Heath uses implicitly. The heath_only set is empty, confirming no substantive citation divergence. This is Case A of Q2: same backbone, different citation depth.

### 3.37
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct a tangent DE from the external point D, apply III.36 to establish rect(AD,DC) = sq(DE), combine with the hypothesis rect(AD,DC) = sq(DB) to get DE = DB, then use triangle congruence (I.8) with radii FE = FB and common side FD to show angle DBF = angle DEF, conclude angle DBF is right since angle DEF is right (III.18), and finally invoke III.16 to conclude DB is tangent. The ai_only set consists entirely of construction propositions (3.1, 3.17), a common notion (CN1), a definition (D1.15), and a postulate (P1) that Heath uses implicitly without citation. The heath_only set is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.
