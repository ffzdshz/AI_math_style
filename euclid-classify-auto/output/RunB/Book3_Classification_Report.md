# Book 3 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 29 | 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 3.10, 3.11, 3.12, 3.14, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23, 3.26, 3.27, 3.28, 3.29, 3.30, 3.31, 3.32, 3.33, 3.34, 3.35, 3.36, 3.37 |
| Path difference (D) | 8 | 3.3, 3.8, 3.9, 3.13, 3.15, 3.16, 3.24, 3.25 |
| AI proof error (E) | 0 |  |

**Total**: 37 propositions

## Per-Proposition Analysis

### 3.1
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct a chord AB, bisect it at D, erect a perpendicular CE and bisect it at F, then argue by contradiction that any other supposed centre G would force the angle GDB (equivalently GDA) to be right by I.8 and I.Def.10, contradicting the fact that angle FDB (FDA) is already right. The AI proof reaches exactly the same key intermediate conclusions in the same order as Heath. The only difference is citation granularity: the AI explicitly cites construction propositions (1.10, 1.11), postulates (P1, P2, P4), definitions (D1.15, D1.16), and a common notion (CN5) that Heath invokes implicitly. Since heath_only is empty and all ai_only items are foundational axioms, definitions, postulates, and construction propositions that support the same backbone steps Heath uses without citation, this is a clear Case A granularity difference.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions through the same logical chain: finding the center, establishing equal radii, deriving equal base angles via I.5, applying the exterior angle theorem I.16, and using the side-angle relationship I.19 to conclude that a point on the chord is closer to the center than the radius. Heath uses a proof by contradiction (assuming the line falls outside) while the AI uses a direct approach (taking an arbitrary point on the segment), but the core geometric argument is identical. The only citation differences are that the AI explicitly cites D1.15 (definition of circle for equal radii) and P1 (postulate for joining lines), which Heath uses implicitly. This is classic over-citation with no substantive path divergence, yielding a same-backbone, different-depth classification.

### 3.3
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Part I of both proofs shares the same backbone: both use SSS congruence (1.8) to show the two triangles formed by the center, midpoint, and endpoints are congruent, then apply D1.10 to conclude the angles are right. However, Part II diverges fundamentally. Heath proves that bisection follows from perpendicularity by using the isosceles triangle property (1.5) to get equal base angles, then AAS congruence (1.26) to conclude AF = FB. The AI instead applies the Pythagorean theorem (1.47) to both right triangles, then uses algebraic manipulation of squares (CN1, CN3) to conclude the segments are equal. These are genuinely different logical strategies: one relies on triangle congruence via angle-side relationships, the other on the Pythagorean theorem and algebraic subtraction. Since the AI's path is logically valid and complete (Q3 holds), the classification is D.

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: assume the two non-diametral chords bisect each other at E, locate the centre F and join FE, apply 3.3 twice to conclude that angles FEA and FEB are both right, then derive a contradiction (the less equals the greater, or equivalently the whole equals the part). The AI's three extra citations (P1 for drawing line FE, P4 for equality of right angles, CN5 for the whole-greater-than-part axiom) merely make explicit the postulates and common notions that Heath invokes silently. Since heath_only is empty and ai_only contains only axiom-level items, this is a straightforward citation-depth difference with the same backbone, yielding category G.

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume two intersecting circles share a centre E, join EC, draw a line EFG through E meeting both circles, derive EC=EF and EC=EG from the definition of centre, conclude EF=EG, then obtain a contradiction because F lies between E and G so EF<EG. The AI proof explicitly cites the axioms and postulates underlying each step (CN1 for transitivity of equality, CN5 for the whole being greater than the part, D1.16 as a supplementary definition, P1 and P2 for constructions) while Heath cites only D1.15 and leaves the rest implicit. Since heath_only is empty and all ai_only items are common notions, definitions, and postulates representing over-citation of the same reasoning, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone for the core case: assume a common centre F, derive FC = FB and FC = FE from F being the centre of each circle, conclude FE = FB by transitivity, then reach a contradiction because FE is a part of FB (the less equals the greater). The AI proof adds an explicit treatment of the external touching case that Heath does not address separately, and the AI explicitly cites foundational items (CN1, CN5, D1.15, D1.16, D3.3, P1, P2) that Heath uses implicitly without citation, resulting in a Jaccard of 0.0 against Heath's empty reference set. Since heath_only is empty and all ai_only items are definitions, common notions, and postulates rather than substantive propositions, this is a classic over-citation pattern reflecting different citation granularity, not a different proof path.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this classification as G (granularity difference). Both proofs share the same four-part backbone: (1) FA is greatest via the triangle inequality on triangle BEF, (2) FD is least via the triangle inequality and subtraction, (3) nearer lines are greater via I.24 applied to triangles with equal radii and unequal included angles, and (4) exactly two equal lines exist, one on each side, via angle construction (I.23) and SAS congruence (I.4). The AI's eight additional citations (ai_only) fall into two categories: explicit axiom/definition/postulate citations (CN2, CN3, D1.15, D1.16, P1, P3) that Heath leaves implicit, and two substantive propositions (1.13 for supplementary angles in Part III, 1.8 for SSS uniqueness in Part IV) that make explicit what Heath handles implicitly or via a brief contradiction argument. The AI uses 1.13 to formally derive that angle BEF > angle CEF, which Heath simply asserts; and uses 1.8 (SSS) for the uniqueness sub-argument where Heath uses the already-proved ordering result. These are differences in citation depth and local argumentation style rather than differences in the key intermediate conclusions, which are identical across both proofs. Heath cites nothing the AI omits (heath_only is empty).

### 3.8
**Category**: Path difference
**Jaccard**: 0.364
**Analysis**: Q2 reveals a different backbone in how the two proofs handle the convex circumference ordering. Heath proves that DK < DL by constructing triangle MLD and showing that the interior lines MK, KD are less than the exterior sides ML, LD via 1.21, then using the equal radii MK = ML to conclude DK < DL. The AI instead proves the convex ordering by comparing angles at the center: since H is nearer to G than K, angle DMH < angle DMK, and then by 1.24 (with equal sides DM common and MH = MK as radii), the base DH < DK. This is a genuinely different intermediate approach, not merely a citation-depth variation. The AI's angle-based method is logically sound, applying 1.24 directly to the convex case rather than Heath's 1.21-based interior-lines argument. The remaining differences in citations (ai_only items 1.13, 1.23, CN3, D1.15, P1, P3) are over-citations of construction steps, definitions, and axioms that do not affect the backbone classification. Since both proofs are logically complete but diverge in a key intermediate step, this is a path difference.

### 3.9
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath proves 3.9 directly by joining chords AB and BC, bisecting them, showing via I.8 that the perpendicular bisectors pass through D, and concluding by III.1 that D lies on the locus of centers; the intersection of two such loci forces D to be the center. The AI instead uses proof by contradiction: assuming D is not the center, it finds the actual center via 3.1, draws a diameter through D, and applies 3.7 to conclude that only two equal lines can fall from D on the circle, contradicting the hypothesis of three. These are fundamentally different logical backbones — Heath uses perpendicular bisector locus (I.8, D1.10, III.1) while the AI uses the diameter extremal property (3.7) via reductio. Since the AI's path is logically complete and valid under the hardened 1(b) standard, the classification is D.

### 3.10
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs use the same overall strategy: proof by contradiction assuming the two circles intersect at more than two points, then showing a single point must be the center of both circles, contradicting 3.5. The key intermediate conclusion in both proofs is identical: the same point serves as center for both circles. Heath establishes this by applying the perpendicular bisector method (3.1) symmetrically to both circles, while the AI finds the center of the first circle via 3.1, shows equal radii fall on the second circle (citing D1.15), and then invokes 3.9 to conclude the point is also the center of the second circle. Since Heath's proof of 3.9 itself uses 3.1 and the perpendicular bisector method internally, the AI is effectively citing 3.9 as a packaged unit rather than re-deriving its content inline. The ai_only items (3.9, D1.15, P1) reflect this different citation depth: 3.9 encapsulates the second application of 3.1, D1.15 makes the equal-radii property explicit, and P1 explicitly cites the postulate for joining lines. Heath_only is empty, confirming the AI covers all of Heath's cited results. This is Case A of Q2: same backbone, different citation depth.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs use the same backbone: a reductio ad absurdum assuming the line joining the centers does not pass through the point of contact, forming a triangle with the two centers and the contact point, applying the triangle inequality to derive a contradiction with the radii equalities. Heath's proof uses the triangle inequality implicitly (stating AG + GF > FA without citation) while the AI explicitly cites 1.20 along with definitions (D1.15, D1.16) and common notions (CN2, CN3, CN5). The heath_refs set is empty (no citations recorded for Heath), so all AI citations appear in ai_only, yielding Jaccard 0.0, but this reflects over-citation rather than a path difference. The key intermediate conclusions are identical in both proofs: the same geometric construction, the same contradiction strategy, the same logical chain. This is Case A of Q2 — same backbone with different citation depth.

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: a proof by contradiction assuming the line joining the centers does not pass through the point of contact, establishing equalities between radii to the contact point and radii to intersection points on the line, applying the triangle inequality (1.20) to get one inequality, and deriving a contradictory inequality from the collinear arrangement of points on the line. The AI's only additional citations (CN1, CN5, D1.15, D1.16, D3.3, P1) are all definitions, common notions, and postulates that Heath invokes implicitly, representing over-citation of foundational items rather than any substantive path divergence. Heath_only is empty, confirming the AI covers all of Heath's cited dependencies.

### 3.13
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. In the internal tangency case, Heath derives a contradiction through an inequality chain (BG=GD implies BG>HD implies BH much greater than HD, but BH=HD), while the AI takes a fundamentally different path: it shows that since G is equidistant from B and D on line BD, G must be the midpoint of BD, and similarly H must be the midpoint of BD, so G=H, contradicting Proposition 3.6 (tangent circles cannot share a center). The external tangency case is argued identically in both proofs (joining AC, showing it falls within both circles via 3.2, contradicting D3.3). Because the internal tangency case has a genuinely different backbone — different key intermediate conclusions and a different contradiction mechanism — this is Case B in Q2. Q3 confirms the AI's different path is valid: the midpoint reasoning is logically sound and all citations (3.1, 3.6, 3.11, D1.15, CN1) are correctly applied, yielding classification D.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone for both directions of the biconditional: bisecting chords via perpendiculars from the centre (3.3), establishing half-chord equality from chord equality, applying the Pythagorean theorem (1.47) to right triangles formed by radii, perpendiculars, and half-chords, and subtracting equal squares to derive the conclusion. The ai_only set (CN1, CN2, CN3, D1.15, P1) consists entirely of common notions, definitions, and a postulate, representing over-citation of foundational axioms that Heath leaves implicit. The heath_only set contains only 3.1 (finding the centre of a circle), which the AI omits as a citation but whose logical role (having a centre to work with) is present in the AI proof text. This is a citation-depth difference, not a structural divergence.

### 3.15
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 reveals fundamentally different backbones in both parts of the proof. For part (i), Heath constructs an auxiliary chord MN equal to BC via III.14, then applies I.20 to triangle MEN to show AD > MN = BC; the AI instead applies I.20 directly to triangle EAD and substitutes radii to get BC > AD without needing III.14. For part (ii), Heath uses I.24 (the hinge theorem) to compare bases MN and FG via unequal included angles; the AI uses I.47 (Pythagorean theorem) on right triangles formed by radii, perpendicular distances, and half-chords, comparing squares to deduce the nearer chord is greater. The heath_only citations (1.24, 3.14) are not contained within the proof trees of the AI's citations — rather, the AI employs an entirely different metric/algebraic method (I.47, III.3) versus Heath's purely synthetic geometric approach (I.24, III.14). Both proofs are logically complete, establishing the same conclusion by genuinely different intermediate reasoning, so this is classified as D.

### 3.16
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. In Part 1 of the proof (showing the tangent falls outside the circle), Heath and the AI use genuinely different logical backbones. Heath uses I.5 (isosceles triangle base angles are equal) to show that equal radii imply equal base angles, then derives a contradiction via I.17 (two right angles in a triangle). The AI instead applies I.17 directly to show the non-right angle in the triangle must be less than a right angle, then uses I.19 (greater angle subtended by greater side) to show the segment exceeds the radius, placing the point outside the circle. These are different key intermediate conclusions: Heath's pivot is the equality of base angles (I.5), while the AI's pivot is the angle-side inequality (I.17 + I.19). Parts 2 and 3 share essentially the same backbone. The AI's alternative path in Part 1 is logically complete and valid, so Q3 yields D rather than E. The ai_only citations (1.12, CN5, D1.10, D1.15, D1.17, D3.2, P1) are all definitions, postulates, common notions, or construction propositions reflecting the AI's greater explicitness, while heath_only contains I.5 which the AI genuinely replaces with a different argument.

### 3.17
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow an identical logical backbone: find the center E of the given circle, construct a larger circle AFG with center E and radius EA, draw DF perpendicular to EA, apply SAS congruence (I.4) to show triangles DEF and BEA are congruent, conclude angle EBA is right since angle EDF is right, and then invoke III.16 to establish that AB touches the circle. The AI proof cites the same core propositions as Heath (1.4, 3.1, 3.16) and adds explicit citations for construction steps and definitions that Heath leaves implicit: 1.11 for drawing the perpendicular from D, P1 for joining line segments, P3 for describing the circle AFG, and D3.2 for the definition of tangency. Since heath_only is empty and ai_only contains only construction propositions, postulates, and a definition, this is a clear case of over-citation at a finer granularity level with identical key intermediate conclusions.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: assume FC is not perpendicular to the tangent DE, draw FG perpendicular to DE, use I.17 to establish that angle FCG is acute (hence angle FGC > angle FCG), and then use I.19 to conclude FC > FG, leading to a contradiction. The AI proof's additional citations (1.12, 3.1, D1.10, D1.15, D3.2, P1) are all construction tools, definitions, and postulates that Heath invokes implicitly without explicit citation. The AI explicitly cites 1.12 for constructing the perpendicular FG, 3.1 for finding the center, P1 for joining FC, and definitions D1.10 (perpendicular), D1.15 (circle), and D3.2 (tangent) to spell out what Heath treats as understood. Heath cites no propositions that the AI omits (heath_only is empty). Since the key intermediate conclusions are identical and the citation differences are purely a matter of explicitness, this is a same-backbone, different-depth case.

### 3.19
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G. Both proofs use identical proof-by-contradiction backbones: assume the center F is not on the perpendicular CA from the point of tangency, invoke 3.18 to establish that FC is also perpendicular to DE, derive that a right angle (FCE/FCD) equals another right angle (ACE/ACD) while being a proper part of it, and conclude by contradiction that the center must lie on CA. The AI proof adds explicit citations for construction steps (3.1, P1), definitions (D1.10, D3.2), a common notion (CN5), and a postulate (P4) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, postulates, common notions, or construction propositions, this is a clear case of over-citation at the same logical depth, fitting Case A of Q2.

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions through an identical logical backbone: (1) radii EA=EB and EA=EC establish isosceles triangles, (2) I.5 gives equal base angles, (3) I.32 (exterior angle theorem) shows each exterior angle at the center equals twice the corresponding inscribed angle part, and (4) the full central angle equals twice the full inscribed angle by addition or subtraction. The AI proof is actually more thorough in case coverage (three explicit cases vs Heath's two), but the core reasoning chain is the same. The ai_only set consists entirely of over-citations of foundational items: CN2 (addition of angles), CN3 (subtraction of angles), D1.15 (definition of circle/radius), and P1/P2 (postulates for joining and producing lines), all of which Heath uses implicitly without citation. Heath_only is empty, confirming no substantive proposition is missing from the AI proof. This is a clear case of same backbone with different citation depth.

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share identical logical backbones: find the center of the circle, show the central angle is double the first inscribed angle via III.20, show the same central angle is double the second inscribed angle via III.20, then conclude the two inscribed angles are equal. The AI's extra citations (3.1 for finding the center, P1 for joining lines, CN1 for the equality inference) are all construction steps and axioms that Heath uses implicitly but does not cite. Since heath_only is empty and ai_only contains only construction/axiom references, this is a clear Case A granularity difference: same backbone, different citation depth.

### 3.22
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs use the identical logical backbone: draw the diagonals of the inscribed quadrilateral, apply the triangle angle sum theorem (1.32), then use the inscribed angle theorem (3.21) to substitute equal angles in the same segment, yielding that each pair of opposite angles sums to two right angles. The AI proof is more explicit, proving both pairs of opposite angles in full detail rather than using Heath's 'similarly' shorthand, and it explicitly cites CN1 (substitution of equals), CN2 (addition of equals), and P1 (drawing a straight line) where Heath leaves these implicit. The ai_only set {CN1, CN2, P1} consists entirely of common notions and a postulate — basic axioms that Heath uses without citation — confirming this is a citation-depth difference rather than a path difference. The heath_only set is empty, meaning every substantive result Heath cites is also cited by the AI.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs use the same logical backbone: assume two similar and unequal segments on the same side of a straight line, construct a configuration where an angle in one segment becomes an exterior angle of a triangle containing an angle in the other segment as an interior angle, then invoke I.16 (exterior angle theorem) to show the angles cannot be equal, contradicting the similarity requirement (D3.11). Heath draws line ACD through both arcs to set up the exterior-interior angle relationship, while the AI takes a point D on the outer arc and shows line DB intersects the inner arc at E, forming triangle ADE with the same exterior angle relationship. The key intermediate conclusions are identical: equal angles from similarity, and an exterior-interior angle contradiction via I.16. The AI's additional citations (3.2 for the arc intersection, D3.6, D3.8, P1) are construction-level and definitional over-citations that do not alter the backbone, and heath_only is empty. This is Case A of Q2: same backbone, different citation depth.

### 3.24
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decides the classification. Both proofs share the same superposition framework (placing segment AEB onto CFD and noting that B coincides with D because AB equals CD), but they diverge at the key contradiction step. Heath argues that if the segments do not coincide, a circle would cut another circle at more than two points, contradicting 3.10. The AI instead argues that non-coincidence would produce two similar but unequal segments on the same straight line on the same side, contradicting 3.23. Since 3.10 does not appear in the proof tree of 3.23 (Heath's proof of 3.23 uses I.16, not 3.10), these are genuinely independent contradiction targets from different domains, not a containment relationship. The AI's path via 3.23 is logically valid, making this a path difference rather than a granularity difference.

### 3.25
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses a three-case angle analysis (angle ABD vs angle BAD), constructing an angle equal to ABD and applying I.6 (isosceles triangle) to establish equal distances, then invoking III.9 (equidistant point is centre). The AI instead uses a single general perpendicular-bisector method: it bisects both AC and AB, draws perpendicular bisectors from the midpoints, proves by contradiction (using I.29 and I.32) that these bisectors must meet at a point F, then applies SAS (I.4) twice to show FA = FB and FA = FC, and constructs the circle directly via P3. The key intermediate conclusions differ fundamentally — Heath relies on angle construction and the isosceles triangle theorem whereas the AI relies on perpendicular bisectors and repeated SAS congruence — establishing a genuine path difference. The AI proof is logically complete under the hardened 1(b) standard, with every step supported by explicit citations, so Q3 confirms the different path is valid.

### 3.26
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they use I.4 to establish BC = EF from equal central angles and equal radii, then use D3.11 to identify similar segments, then III.24 to conclude those similar segments on equal straight lines are equal, and finally subtract to obtain equal remaining arcs. The AI additionally cites 3.20 to explicitly bridge between central and inscribed angles (which Heath handles without explicit citation), and cites CN2, CN3 for arithmetic steps, D3.1 for the definition of equal radii, and D3.6 for the definition of a segment. All ai_only items (3.20, CN2, CN3, D3.1, D3.6) represent over-citation of implicit steps rather than a genuinely different proof path. The heath_only set is empty, confirming that the AI covers all of Heath's cited propositions. This is a classic Case A same-backbone scenario with the AI providing finer citation granularity.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) proof by contradiction for the centre-angle case, constructing angle BGK equal to EHF via I.23, applying III.26 to get circumference BK equal to EF, then deriving the contradiction that BK equals BC (part equals whole); (2) for the circumference-angle case, using III.20 to show the central angles are double the inscribed angles, so equality of central angles implies equality of inscribed angles. The AI proof cites the same three substantive propositions as Heath (1.23, 3.20, 3.26) and additionally makes explicit three common notions (CN1, CN3, CN5) that Heath uses implicitly. Since ai_only contains only common notions and heath_only is empty, this is a straightforward citation-depth difference with identical backbone, yielding Granularity difference (G).

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) radii of equal circles are equal, (2) triangle congruence by I.8 yields equal central angles, (3) III.26 gives equal minor arcs, (4) subtraction from equal whole circumferences gives equal major arcs. The AI proof cites 3.1 for finding centres, P1 for joining lines, D3.1 for radii equality, and CN3 for the subtraction step, all of which Heath leaves implicit. Since heath_only is empty and all ai_only items are construction, definition, common notion, or postulate citations that make explicit what Heath treats as understood, this is Case A: same backbone with different citation depth, yielding Granularity difference (G).

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) angle BKC equals angle ELF from equal circumferences via III.27, (2) radii are equal because the circles are equal, and (3) base BC equals base EF by SAS via I.4. The AI proof follows the exact same logical backbone as Heath's proof. The ai_only citations (3.1 for finding centres, P1 for joining lines, D3.1 for the definition of equal circles implying equal radii) are all construction-level or definitional over-citations that Heath performs implicitly without citing. Heath_only is empty, confirming no substantive steps are missing. This is Case A of Q2: same backbone, different citation depth, yielding a Granularity difference.

### 3.30
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: join AB, bisect at C, draw CD perpendicular to AB, use SAS (I.4) to show AD = DB, then invoke III.28 to conclude arc AD = arc DB. The ai_only set {1.10, 1.11, D3.1, P1} consists entirely of construction propositions (1.10 for bisecting a segment, 1.11 for drawing a perpendicular), a postulate (P1 for joining a line), and a definition (D3.1 for circle equality) -- all of which Heath uses implicitly without citation. The heath_only set is empty, confirming no substantive step is missing from the AI proof. This is a textbook Case A: same backbone, different citation depth, yielding a Granularity difference.

### 3.31
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs establish the same five key intermediate conclusions through the same logical backbone: (1) using I.5 on isosceles triangles formed by radii to show base angles are equal, (2) deriving that the angle in a semicircle equals a right angle, (3) the angle in a greater segment is less than a right angle, (4) the angle in a less segment is greater than a right angle via III.22, and (5) the mixed angle results for the greater and less segments. The differences are purely in citation depth: Heath cites I.17 to conclude angle ABC is acute, while the AI reaches the same conclusion via I.32 and CN5/D1.12 (the angle sum of a triangle equals two right angles, so if one angle is right the other two sum to a right angle, hence each is less than a right angle). For parts 4-5 about mixed angles, Heath says the result is 'at once manifest' without citing a proposition, while the AI explicitly invokes 3.16 and D3.7. The remaining ai_only items (D1.11, D1.12, D1.15, D3.7, P1, P2, CN5) are all definitions, common notions, and postulates that the AI cites for explicitness. All key conclusions appear at the same logical positions in both proofs.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as Granularity difference (G). Both proofs establish identical key intermediate conclusions: (1) BA is a diameter perpendicular to the tangent EF, (2) angle ADB is right by 3.31, (3) angles BAD + ABD equal one right angle by I.32, (4) angle DBF equals angle BAD, and (5) angle DBE equals angle BCD via 3.22. The sole substantive citation difference is that the AI uses 3.18 (tangent perpendicular to radius from center) while Heath uses 3.19 (center lies on line drawn perpendicular to tangent from contact point). These are converse results arriving at the same geometric fact (BA is a diameter perpendicular to EF). Critically, Heath's proof of 3.19 itself cites 3.18 internally, so by the proof-tree containment test the AI cites the sub-result directly while Heath cites the parent result that wraps it. The remaining ai_only items (1.13, D1.15, D1.17, D3.2, D3.8, P1, P2) are definitions, postulates, and a supplementary-angle proposition that Heath invokes implicitly, representing typical over-citation rather than path divergence.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both the AI and Heath proofs address the same three cases (acute, right, obtuse angle) and establish identical key intermediate conclusions in each case: congruence of GA and GB via I.4, the circle through A passing through B, tangency of DA via III.16, equality of angle DAB with the angle in the alternate segment via III.32, and the angle in the semicircle being right via III.31. The heath_only set is empty, meaning the AI cites every proposition Heath cites. The ai_only set consists entirely of construction propositions (1.10, 1.11, 1.23), postulates (P1, P3, P4), a common notion (CN1), and a definition (D1.15), all of which represent explicit citation of basic construction and axiomatic steps that Heath uses implicitly without citation. This is a textbook case of over-citation at a finer granularity with the same logical backbone.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: draw a tangent at a point B on the circle, construct angle FBC equal to the given angle D using I.23, apply the alternate segment theorem III.32 to equate angle FBC with the angle in segment BAC, then conclude that the angle in segment BAC equals angle D. The AI proof cites four additional references not in Heath (3.17 for the tangent construction, CN1 for transitivity of equality, D3.6 and D3.8 for segment definitions), but all of these are over-citations making explicit what Heath leaves implicit. Heath's proof has no citations absent from the AI (heath_only is empty). Since the key intermediate conclusions are identical and the citation differences reflect only depth of explicit justification, this is a granularity difference.

### 3.35
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same mathematical backbone: using III.3 to bisect a chord, II.5 to decompose the rectangle from bisected segments, I.47 (Pythagorean theorem) for right triangle relationships with the centre, and radii equality to equate the two rectangle-plus-square expressions before subtracting FE-squared. The AI organizes the proof into three explicit cases (both through centre, one through centre, neither through centre) while Heath uses two (both through centre, neither through centre), but the core algebraic chain is identical. The ai_only set consists entirely of over-citations: construction props (1.12 for perpendiculars, 3.1 for finding the centre), common notions (CN1, CN2, CN3 for equality manipulations), definitions (D1.15, D1.17 for circle and radius), and a postulate (P1 for drawing lines), all of which Heath invokes implicitly. The heath_only set is empty, confirming no substantive proposition is missing from the AI proof. This is a clear case of same backbone with different citation depth.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they handle two cases (secant through the centre and secant not through the centre), both establish the right angle at the tangent point via III.18, both bisect the chord (III.3 in Case 2), and both use I.47 (Pythagorean theorem) multiple times to reach the same key intermediate conclusion that AD times DC equals FD squared minus FB squared, which then equals BD squared. The only substantive citation difference is that the AI uses II.5 (difference of squares identity) where Heath uses II.6 (rectangle on bisected-and-extended line) at the same logical position to establish the same algebraic relationship. These are parallel algebraic identities applied to the same geometric configuration, making this a citation-depth choice rather than a backbone divergence. The remaining ai_only items (1.12, 3.1, P1, D1.15, D3.2) are construction steps, postulates, and definitions that the AI cites explicitly but Heath leaves implicit, which is characteristic over-citation consistent with G.

### 3.37
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: draw a tangent DE from the external point D, find the center F, establish angle FED is right (III.18), apply III.36 to get rect(AD,DC) = sq(DE), equate with sq(DB) by hypothesis, conclude DE = DB, prove triangle congruence via I.8 (SSS), transfer the right angle from FED to FBD, and conclude DB is tangent by III.16. The ai_only set {3.1, 3.17, CN1, D1.15, P1} consists entirely of construction propositions (3.1 for finding the center, 3.17 for drawing a tangent), a common notion (CN1 for equality transitivity), a definition (D1.15 for radii equality), and a postulate (P1 for joining lines) -- all foundational steps that Heath uses implicitly without citation. Heath's proof mentions a secondary case where the center lies on AC, which the AI omits, but the AI's general argument covers this case since its construction and reasoning do not depend on the center's position relative to AC. This is Case A: same backbone, different citation depth, yielding G.
