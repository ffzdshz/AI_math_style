# Book 3 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 35 | 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.10, 3.11, 3.12, 3.13, 3.14, 3.15, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23, 3.24, 3.25, 3.26, 3.27, 3.28, 3.29, 3.30, 3.31, 3.32, 3.33, 3.34, 3.35, 3.36, 3.37 |
| Path difference (D) | 2 | 3.9, 3.16 |
| AI proof error (E) | 0 |  |

**Total**: 37 propositions

## Per-Proposition Analysis

### 3.1
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect a chord AB at D, erect a perpendicular CE through D, bisect CE at F, then prove by contradiction (using SSS via I.8) that no other point G can be the centre because angle GDB would be right while angle FDB is also right. The AI proof follows this identical chain but explicitly cites many foundational references Heath leaves implicit -- construction propositions (1.10, 1.11), postulates (P1, P2, P4), definitions (D1.15, D1.16), common notions (CN5), and the vertical angles theorem (1.15) for an elaborated angle comparison. Heath cites only I.8 and Def. 10; the AI cites these plus nine additional items, all of which support the same backbone at finer granularity. heath_only is empty, confirming the AI covers everything Heath does. This is Case A of Q2: same key intermediate conclusions, different citation depth.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: finding the center D, establishing DA = DB as radii, proving base angles equal via I.5, applying the exterior angle theorem I.16 to get angle DEB > angle DAE, combining to get angle DEB > angle DBE, then applying I.19 to conclude DB > DE and reaching a contradiction. The AI proof explicitly handles both cases (E on the circumference and E outside the circle) that Heath treats with a 'similarly' remark, but this is elaboration of the same argument. The citation difference is entirely in ai_only = {CN5, D1.15, P1}, all foundational items (a common notion, a definition, and a postulate) that Heath uses implicitly. With heath_only empty and the backbone identical, this is Case A of Q2: same key intermediate conclusions at different citation depth.

### 3.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions across both directions of the biconditional: in Part 1, both use SSS congruence (I.8) on triangles AFE and BFE to derive equal adjacent angles and then invoke Def I.10 to conclude right angles; in Part 2, both use isosceles base angles (I.5) and AAS congruence (I.26) to derive AF = FB. The AI's four extra citations (3.1 for finding the centre, D1.15 for the definition of circle justifying equal radii, P1 for joining lines, P4 for equality of right angles) are all explicit references to construction steps, definitions, and postulates that Heath employs implicitly without citation. Since heath_only is empty and all ai_only items are over-citations of foundational items rather than substantive propositions indicating a different proof path, this is Case A of Q2: same backbone, different citation depth.

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assuming the two chords bisect each other for contradiction, finding the center F, joining FE, then using III.3 twice to show that both angle FEA and angle FEB are right angles, and finally deriving a contradiction from the impossibility of these two angles being equal when one must be part of the other. The AI proof explicitly cites foundational axioms that Heath uses implicitly: P1 for joining the line FE, P4 for the equality of right angles, and CN5 for the principle that the whole is greater than the part. Since the key intermediate conclusions are identical and the citation difference consists entirely of postulates and common notions, this is a granularity difference.

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assume two intersecting circles share a center E, establish EC = EF (E is center of circle ABC) and EC = EG (E is center of circle CDG), then derive the contradiction EF = EG where one is part of the other. The AI proof explicitly cites foundational items that Heath leaves implicit -- CN1 for the transitivity step yielding EF = EG, CN5 for the whole-greater-than-part principle, D1.16 for the definition of center, and P1/P2 for line constructions. Since heath_only is empty and all ai_only items are common notions, definitions, or postulates, this is a clear case of over-citation at the same logical backbone, yielding G.

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume by contradiction that F is the centre of both circles ABC and CDE touching at C; join FC and draw a line through F meeting both circumferences; show FC = FB (F centre of ABC) and FC = FE (F centre of CDE), so FE = FB; but one segment is part of the other, yielding a contradiction. The AI proof is more verbose and explicitly cites foundational items (definitions D1.15, D1.16, D3.3; common notions CN1, CN5; postulates P1, P2) that Heath uses implicitly without citation. Since Heath's reference list is empty while the AI's consists entirely of these foundational over-citations, the Jaccard is 0.0, but the backbone is identical. This is Case A of Q2: same key intermediate conclusions, different citation depth, yielding G.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) FA is greatest via triangle inequality (1.20) and radius equality, (2) FB > FC > FG via angle comparison and I.24, (3) FD is least via triangle inequality and subtraction, (4) exactly two equal lines via angle construction (1.23) and SAS congruence (1.4), and (5) uniqueness by contradiction. The AI proof cites the same four theorem-level propositions as Heath (1.4, 1.20, 1.23, 1.24) and adds only foundational items that Heath uses implicitly: definitions (D1.15 for radius equality, D1.17 for diameter), common notions (CN1, CN3, CN5), and a postulate (P1). The heath_only set is empty, confirming no substantive citations are missing. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 3.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: using the triangle inequality (1.20) to establish DA as greatest on the concave circumference, the SAS inequality (1.24) for ordering on the concave side, the triangle inequality again for DG as least on the convex side, the interior-lines theorem (1.21) for ordering on the convex side, angle construction plus SAS congruence (1.4) to produce exactly two equal lines, and a uniqueness argument by contradiction. The AI proof explicitly cites foundational items that Heath uses implicitly: 1.23 for angle construction, CN1 for transitivity of equality, CN3 for subtraction of equals, D1.15 for the definition guaranteeing equal radii, and P1 for drawing lines. Since heath_only is empty and all ai_only items are over-citations of definitions, common notions, postulates, or a basic construction proposition, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 3.9
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification. Heath proves 3.9 directly by bisecting two chords AB and BC, using I.8 and I.Def.10 to show the perpendicular bisectors pass through D, then invoking the porism to III.1 to place the center on both bisectors, concluding D is the center since the two lines meet only at D. The AI instead uses a reductio ad absurdum via 3.7: assuming D is not the center, it finds the actual center E by 3.1, draws diameter FG through D and E, and applies 3.7 to conclude that only two equal straight lines can fall from D on the circle, contradicting the hypothesis of three equal lines. These are fundamentally different backbones — a direct constructive proof versus an indirect proof by contradiction leveraging a different theorem — so Q2 yields Case B. Q3 confirms the AI's reductio is logically complete and sound, giving category D.

### 3.10
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs use the same contradiction strategy: assume more than two intersection points, construct perpendicular bisectors of chords through those points, invoke III.1 to show the center of each circle lies on the same pair of perpendicular bisectors, conclude both circles share a center, and derive a contradiction via III.5. The AI proof is substantially more detailed, explicitly citing 1.10 for bisection, 1.11 for drawing perpendiculars, P1 and P2 for construction postulates, 3.2 to establish non-collinearity of the intersection points, and 1.17 to prove the two perpendicular bisectors are distinct lines. These are all intermediate justifications for steps that Heath performs without citation. Since heath_only is empty and all ai_only items are construction or auxiliary propositions supporting the same logical backbone, this is Case A of Q2: same key intermediate conclusions at different citation depth, yielding G.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction structure, arriving at the same contradiction: GD < GH (because D lies between G and H on the produced diameter) yet GD > GH (because AG > GH and AG = GD as radii of circle ADE). The key intermediate conclusions are identical in both proofs. The only difference is in the supporting method for the step AG > GH: Heath implicitly uses the triangle inequality on triangle AGF (AG + GF > FA = FH, subtract FG), while the AI invokes 3.7 directly (GH is the least distance from a non-center point on a diameter to the circumference). Since the backbone is the same and the AI's explicit citations (3.1, 3.6, 3.7, CN5, D1.15, D1.17, D3.3, P1, P2) represent over-citation of steps Heath leaves implicit (heath_refs is empty in the parsed data), this is Case A of Q2: same backbone, different citation depth.

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs follow the identical contradiction strategy: assuming the line of centers FG does not pass through the external contact point A, establishing FA = FC and GA = GD via radii equality, deducing FA + AG = FC + GD, and deriving a contradiction with the triangle inequality (1.20). The key intermediate conclusions are the same in both proofs. The citation difference consists entirely of explicit foundational references the AI adds (3.1 for finding centers, D1.15 for the definition of a circle, D3.3 for the definition of external tangency, CN2 and CN5 for arithmetic properties, P1 for drawing lines) that Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are construction, definition, common notion, or postulate-level over-citations, this is a granularity difference (G).

### 3.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs argue through the same two-case structure (internal and external touching) with identical key intermediate conclusions: for the internal case, the line through the two centers passes through both alleged contact points (3.11), radii from one center are equal while the segment to the other center's contact point is strictly smaller, yielding a contradiction with equal radii from the second center; for the external case, the joining line falls within both circles (3.2) contradicting the external tangency condition (D3.3). The AI proof is more explicit, citing constructions (3.1), definitions (D1.15, D1.17), a supporting lemma (3.6), a common notion (CN5), and a postulate (P1) that Heath uses implicitly. Since heath_only is empty and all ai_only items are over-citations of foundational results used implicitly by Heath, this is Case A of Q2: same backbone, different citation depth.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish the same biconditional through identical key intermediate conclusions: perpendiculars from the centre bisect each chord (3.3), radii are equal, the Pythagorean theorem (1.47) yields sum-of-squares equations, and subtraction of equal squares produces the desired equality in each direction. The AI proof's six additional citations (1.12, CN1, CN2, CN3, D1.15, P1) are all construction propositions, common notions, definitions, and postulates that Heath invokes implicitly without explicit citation. With heath_only empty, every substantive proposition Heath cites is also cited by the AI, confirming the backbone is the same. This is a clear Case A granularity difference: same logical backbone, different citation depth.

### 3.15
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct a chord MN equidistant from the center as BC, prove BC = MN via III.14, show AD exceeds BC via the triangle inequality (I.20), and show MN exceeds FG via I.24 on triangles MEN and FEG. The slight variation in Step 5 (Heath uses triangle MEN while the AI uses triangle EBC to apply I.20) is an equivalent restatement of the same intermediate conclusion, not a different path. The heath_only set is empty, meaning the AI cites everything Heath does. The ai_only set consists entirely of construction propositions (1.3, 1.11, 1.12), postulates (P1, P2), common notions (CN2, CN5), and definitions (D1.15, D1.17, D3.4) that Heath uses implicitly but does not cite. This is a clear Case A: same backbone, different citation depth.

### 3.16
**Category**: Path difference
**Jaccard**: 0.176
**Analysis**: Q2 decides the classification. The first two parts of the proof (tangent falls outside the circle, no line can be interposed) share the same backbone in both Heath and the AI, with the AI over-citing definitions, postulates, and construction propositions such as I.12 and I.13. However, for the third part (angle comparisons), the proofs take genuinely different paths: Heath uses reductio ad absurdum, arguing that if a greater or lesser rectilineal angle existed then a line would be interposed between the tangent and circumference, contradicting part 2. The AI instead uses a direct construction via I.23 and III.2, establishing the key intermediate that every line drawn from A within angle BAE falls within the circle, then constructing an angle equal to any given acute angle K and comparing via the part-whole relation (CN5). This constitutes different key intermediate conclusions for the third part, making Case B in Q2 apply. Since the AI's different path is logically sound and complete (Q3 holds), the classification is D.

### 3.17
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided this classification. Both proofs establish identical key intermediate conclusions in the same order: (1) EA = EF and ED = EB as radii of the two circles, (2) triangles DEF and BEA are congruent by SAS (I.4), (3) angle EBA equals angle EDF, (4) angle EBA is right because EDF is right, and (5) AB touches the circle by III.16. The AI proof is a strict superset of Heath's citations, adding only definitions (D1.15, D1.17, D3.2), postulates (P1, P2, P3), and one construction proposition (1.11) that Heath leaves implicit. With heath_only empty and all ai_only items being basic building blocks, this is a clear case of the AI citing at finer granularity while following the same logical backbone.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assume FC is not perpendicular to the tangent DE, draw FG perpendicular to DE, establish that angle FGC is right and angle FCG is acute (I.17) so FC > FG (I.19), then show that G lies outside the circle so FG crosses the circumference at B making FG > FB, while FB = FC as radii, yielding a contradiction. The AI proof cites every construction, definition, and axiom explicitly (1.12 for drawing the perpendicular, 3.1 for finding the centre, D1.10 and D1.15 for definitions, D3.2 for the tangent definition, CN5 for the whole-greater-than-part axiom, P1 for joining points, and 3.2 to justify that G lies outside the circle), whereas Heath leaves all of these implicit and cites only I.17 and I.19. Since heath_only is empty and all ai_only items are construction propositions, definitions, postulates, common notions, or a supporting proposition used at the same logical position, this is a citation-depth difference with identical logical backbone, yielding G.

### 3.19
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction assuming the centre F lies off the perpendicular AC to the tangent DE, then invoking III.18 to establish that FC is also perpendicular to DE, and finally deriving the impossible conclusion that a proper part of an angle equals the whole angle. The ai_only set {CN5, D1.10, P1, P4} consists entirely of common notions, definitions, and postulates that Heath uses implicitly but does not cite. The AI simply makes these foundational references explicit (e.g., citing P4 for equality of right angles, CN5 for the whole being greater than the part, D1.10 for the definition of right angle, P1 for joining points). Since the key intermediate conclusions are identical and the citation difference is purely one of depth, this is a granularity difference (G).

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that radii from the center create isosceles triangles (I.5), apply the exterior angle theorem (I.32) to show each sub-angle at the center is double the corresponding sub-angle at the circumference, and then combine the results. The AI covers three explicit cases (center inside, outside, and on one side of the inscribed angle) while Heath covers two, but the core argument is identical. The ai_only set consists entirely of common notions (CN1, CN2, CN3), a definition (D1.15), and postulates (P1, P2) that Heath leaves implicit, while heath_only is empty. This is a textbook Case A from Q2: same backbone, different citation depth, yielding G.

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: find the center F of the circle, join BF and FD, apply III.20 twice to show that the central angle BFD is double of each inscribed angle BAD and BED, and conclude that BAD equals BED. The AI proof cites five additional references (3.1, CN1, D3.8, D3.9, P1) that Heath leaves implicit; these are all construction propositions, definitions, postulates, and common notions, not substantive theorems. Heath's proof performs the same constructions and uses the same common notion but without explicit citation. Since the key intermediate conclusions are identical and the citation difference reflects only the depth of explicit justification, this is a granularity difference.

### 3.22
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: join diagonals AC and BD, apply the triangle angle sum (I.32) to triangle ABC, then use the inscribed angle theorem (III.21) to equate angle CAB with angle BDC and angle ACB with angle ADB, combine these to show the whole angle ADC equals angles BAC plus ACB, add angle ABC to both sides, and conclude ABC plus ADC equals two right angles. The AI proof additionally cites CN1, CN2, D3.8, and P1, all of which are axiom-level or definition-level references that Heath uses implicitly. Since the key intermediate conclusions are the same and the citation difference consists entirely of foundational items the AI made explicit, this is a granularity difference.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy: assume two similar and unequal segments ACB and ADB on the same side of AB, draw line ACD through so that A, C, D are collinear, then show angle ACB equals angle ADB by similarity (Def. 11) while also being an exterior angle of triangle BCD and hence greater than ADB by I.16, yielding a contradiction. The AI proof establishes exactly the same backbone but with greater citation depth, explicitly invoking 3.10 to justify that the two circumferences meet only at A and B, CN4 to justify that unequal segments do not coincide, and citing definitions D3.6 and D3.8 plus postulates P1 and P2 that Heath leaves implicit. Since heath_only is empty and the ai_only items are all over-citations of the same underlying argument, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 3.24
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same superposition backbone: placing segment AEB onto CFD so A falls on C and B on D (since AB = CD), then arguing by contradiction that the arcs must coincide by considering three cases (the transported arc falls within, outside, or awry of the target arc), and concluding the segments are equal. The AI proof handles all three cases explicitly, using 3.23 to refute the within/outside cases and 3.10 for the awry case, whereas Heath's compressed proof mentions all three cases but only explicitly resolves the awry case via III.10. The AI also cites definitions (D3.6, D3.11) and common notions (CN4, CN5) that Heath invokes implicitly. Since the key intermediate conclusions are identical and the citation differences reflect depth of justification rather than a different logical path, this is a granularity difference.

### 3.25
**Category**: Granularity difference
**Jaccard**: 0.056
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: bisecting AC at D with DB perpendicular, distinguishing three cases by the relative size of angles ABD and BAD, and in each case establishing three equal lines from a point to the circumference (AE = BE = CE in Cases I and III, DA = DB = DC in Case II). The only substantive citation difference is in the final justification: Heath uses 3.9 (three equal lines from an interior point to a circle imply the point is the centre) while the AI constructs the circle explicitly via P3 and D1.15, then argues uniqueness via 3.10 (a circle does not cut a circle at more than two points). These achieve the same geometric conclusion through different citations. The remaining 15 ai_only items are over-citations of construction steps (1.10, 1.11, 1.23), postulates (P1-P5), common notions (CN1), definitions (D1.15, D1.17, D1.18), and elementary propositions (1.4, 1.6, 1.13, 1.17). The Jaccard of 0.056 reflects this heavy over-citation rather than a genuine path divergence.

### 3.26
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: equal radii yield BC=EF via I.4, the equal angles make segments BAC and EDF similar via Def. 11, similar segments on equal lines are equal via III.24, and subtracting equal segments from equal circles gives equal circumferences. The AI proof adds an explicit preliminary step using 3.20 to show that equality of either central or circumference angles implies equality of both, whereas Heath handles this implicitly. All ai_only items are either definitions, common notions, and postulates cited explicitly by the AI but left implicit by Heath, or 3.20 which provides additional case-handling depth rather than a different path. Since heath_only is empty and the key intermediate conclusions are identical, this is a granularity difference.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: a proof by contradiction for the central angle case (assuming BGC > EHF, constructing angle BGK = EHF via I.23, deriving arc BK = arc EF via III.26, reaching a contradiction with arc BC = arc EF), followed by deriving the circumference angle case via III.20. The AI's only additional citations are CN1 (transitivity of equality, used to chain arc BK = arc EF = arc BC) and CN5 (whole greater than part, used to state the contradiction explicitly), both of which Heath invokes implicitly. Since the ai_only set consists entirely of common notions making explicit what Heath leaves implicit, and the key intermediate conclusions are identical in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification. Both proofs follow an identical logical backbone: take the centres of the equal circles, join the radii, apply SSS (I.8) to establish equal central angles, invoke III.26 to conclude the lesser circumferences are equal, and subtract to obtain equal greater circumferences. The ai_only set {3.1, CN3, D1.15, D3.1, P1} consists entirely of a construction proposition (3.1 for finding centres), definitions (D1.15, D3.1), a common notion (CN3), and a postulate (P1) that Heath employs implicitly without citation. The heath_only set is empty. Since the key intermediate conclusions are the same and the citation differences reflect only the depth at which foundational steps are cited, this is a granularity difference (G).

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) equal circumferences imply equal central angles via 3.27, (2) equal circles have equal radii, and (3) SAS congruence via 1.4 yields BC = EF. The AI's additional citations (3.1 for finding centres, D3.1 for the definition of equal circles, P1 for joining lines) are all construction-level or definitional references that Heath performs implicitly without citation. Since heath_only is empty and all ai_only items are construction/definition/postulate over-citations, this is a clear Case A granularity difference.

### 3.30
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: bisect chord AB at C, erect a perpendicular CD to meet the arc, prove AD = DB by triangle congruence (I.4), then conclude arc AD = arc DB via III.28 because equal chords cut equal lesser arcs. The AI proof cites eight additional references that Heath leaves implicit: construction propositions (P1, 1.10, 1.11), the postulate that all right angles are equal (P4), and an elaborate justification that each arc is less than a semicircle using 3.1 Porism, D1.17, D1.18, and CN5. Since heath_only is empty and all ai_only items are construction steps, axioms, definitions, or deeper elaborations of the same intermediate conclusion, this is Case A -- same backbone, different citation depth -- yielding G.

### 3.31
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct AE and produce BA to F, use two applications of I.5 on isosceles triangles to equate base angles, invoke I.32 to show angle BAC equals exterior angle FAC and hence each is right (D1.10), apply I.17 to conclude the angle in the greater segment is less than a right angle, and apply III.22 to conclude the angle in the less segment is greater than a right angle. The AI proof covers all five required cases just as Heath does. The ai_only set consists entirely of definitions (D1.15, D1.17, D1.18, D3.6, D3.7, D3.8), common notions (CN1, CN2, CN5), postulates (P1, P2), and two minor propositions (3.2 used to justify that a chord lies within the circle, 3.21 used to generalize from the specific angle to all angles in the same segment). Heath leaves all of these implicit. The heath_only set is empty, confirming the AI cites everything Heath does and more. This is a clear case of the same backbone argued at greater citation depth.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same logical order: BA is a diameter because the center lies on BA (III.19), angle ADB is right as an angle in a semicircle (III.31), angles BAD and ABD sum to one right angle (I.32), angle DBF equals angle BAD by subtracting ABD from the right angle ABF, and then angle DBE equals angle DCB using the cyclic quadrilateral property (III.22) and the supplementary angle relation. The ai_only set consists entirely of definitions (D1.10, D1.17, D1.18, D3.8), postulates (P1, P2, P4), common notions (CN1, CN3), construction propositions (1.11, 1.13), and 3.18 used only in an additional explicit case where BD passes through the center. Heath leaves all of these implicit. heath_only is empty. This is Case A in Q2: same backbone, different citation depth, yielding G.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions across all three cases (acute, right, obtuse): constructing the angle equal to C, bisecting AB, showing AG=BG via I.4, describing the circle, establishing tangency via III.16, and applying the alternate segment theorem III.32 (acute and obtuse cases) or the semicircle angle theorem III.31 (right case). The heath_only set is empty, confirming every substantive step in Heath appears in the AI proof. The ai_only set consists entirely of construction propositions (1.10, 1.11, 1.23), postulates (P1-P5), common notions (CN1), and definitions (D1.15, D1.17, D1.18, D3.6, D3.8) that Heath leaves implicit. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: draw a tangent at B, construct angle FBC equal to the given angle D using I.23, then apply the tangent-chord angle theorem (III.32) to conclude that the angle in the alternate segment BAC equals angle FBC and hence equals D. The AI proof adds explicit citations for supporting constructions and axioms that Heath leaves implicit: 3.17 for the existence of the tangent, 3.16 for the property that a tangent touches the circle at exactly one point (used to justify that BC enters the circle), CN1 for the transitivity step, and D3.8 for the definition of an angle in a segment. Since heath_only is empty and all ai_only items are construction propositions, a common notion, and a definition, this is a clear case of over-citation with the same logical backbone, yielding Granularity difference.

### 3.35
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that for each chord through the intersection point E, the rectangle of the segments plus the square on EF equals the square on the radius (using III.3 bisection, II.5 algebraic identity, and I.47 Pythagorean theorem), then use equality of radii and subtraction to conclude rect(AE,EC) = rect(DE,EB). The AI proof is more thorough in case coverage (handling chords through the centre and the degenerate sub-case where E coincides with the perpendicular foot) and more explicit in citing foundational references. All ai_only items (1.12, 3.1, CN1, CN2, CN3, D1.10, D1.15, P1) are construction propositions, common notions, definitions, and postulates that Heath uses implicitly, and heath_only is empty. This is Case A of Q2: same backbone, different citation depth.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs address the same two cases (secant through the centre and secant not through the centre) with identical key intermediate conclusions: establishing that the tangent-radius angle is right (III.18), applying the rectangle-plus-square identity (II.6) to the bisected chord with added segment, and using the Pythagorean theorem (I.47) to convert sums of squares before subtracting to reach the final equality. The AI proof cites every foundational item explicitly (postulate P1 for joining lines, 1.12 for perpendicular construction, 3.1 for finding the centre, D1.15 for radii equality, and common notions CN1/CN2/CN3 for equality manipulations), while Heath leaves these implicit. Since heath_only is empty and all ai_only items are construction propositions, postulates, definitions, and common notions, this is a clear case of over-citation at a finer granularity with no backbone divergence.

### 3.37
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided this classification. Both proofs follow an identical logical backbone: construct a tangent DE from external point D, find the center F, show angle FED is right (III.18), use III.36 to establish AD*DC = DE^2, derive DE = DB from the hypothesis, note FE = FB as radii, apply I.8 for triangle congruence to conclude angle DBF equals the right angle DEF, and invoke III.16 to conclude DB is tangent. The AI's seven extra citations (3.1, 3.17, CN1, D1.15, D1.17, P1, P2) are all construction steps, postulates, definitions, and common notions that Heath uses implicitly without citing. Since heath_only is empty and all ai_only items represent over-citation of auxiliary steps rather than substantive divergence, this is Case A of Q2: same backbone, different citation depth.
