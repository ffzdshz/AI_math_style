# Book 11 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 38 | 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 11.10, 11.11, 11.12, 11.13, 11.14, 11.15, 11.16, 11.17, 11.18, 11.19, 11.20, 11.21, 11.22, 11.23, 11.24, 11.25, 11.26, 11.27, 11.28, 11.29, 11.30, 11.31, 11.32, 11.33, 11.34, 11.35, 11.36, 11.38, 11.39 |
| Path difference (D) | 1 | 11.37 |
| AI proof error (E) | 0 |  |

**Total**: 39 propositions

## Per-Proposition Analysis

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume part AB lies in the reference plane and part BC in an elevated plane, produce AB to D within the reference plane so that ABC and ABD are two distinct straight lines sharing the common segment AB, draw a circle with center B and distance AB, and derive a contradiction from the diameters cutting off unequal circumferences. The AI proof is more detailed, explicitly citing P2 (line production), P3 (circle construction), D1.17 (diameter definition), and CN5 (whole greater than part), all of which Heath invokes implicitly without naming. Since heath_only is empty and ai_only consists entirely of foundational axioms, definitions, and postulates, this is a clear case of over-citation at the same logical backbone, yielding G.

### 11.2
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: proving triangle ECB lies in one plane by contradiction using XI.1, then extending from the triangle's sides (EC, EB) to the full lines (AB, CD) via XI.1, and finally generalizing to every triangle. The AI proof's extra citations (D1.19 for the definition of a triangle, P1 for the postulate allowing points to be joined) are explicit references to foundational items that Heath invokes implicitly without citation. Since heath_only is empty and ai_only contains only a definition and a postulate, the difference is purely one of citation depth, not of logical path. Case A of Q2 holds, yielding G.

### 11.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: proof by contradiction assuming the common section DB is not a straight line, constructing straight lines DEB in plane AB and DFB in plane BC, showing these two lines share extremities D and B and would therefore enclose a space (which is impossible), concluding that DB must be a straight line. The AI proof adds more explicit justification in Step 4 (arguing that DEB cannot lie in plane BC) and explicitly cites D1.7 (definition of a plane surface) and P1 (the postulate for joining two points by a straight line), both of which Heath uses implicitly without citation. Since ai_only contains only a definition and a postulate -- foundational references rather than substantive theorems -- and the key intermediate conclusions are the same in both proofs, this is a granularity difference where the AI over-cites relative to Heath.

### 11.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs argue through exactly the same key intermediate conclusions: equal segments yield AD=BC and angle DAE=angle EBC via I.4, then GE=EH and AG=BH via I.26 on vertical-angle triangles, then FA=FB and FC=FD via I.4 on right-angle triangles, then angle FAD=angle FBC via I.8, then FG=FH via I.4, then angle GEF=angle HEF via I.8, and finally perpendicularity to an arbitrary line in the plane gives perpendicularity to the plane by XI.Def.3. The backbones are identical. The AI proof adds five citations not in Heath (1.3 for cutting equal segments, 11.2 for intersecting lines lying in a plane, P1 for joining lines, P4 for right angles being equal, D1.10 for the definition of perpendicular), all of which are construction-level, postulate, or definition citations that Heath uses implicitly. The heath_only set is empty. This is a clear case of over-citation at the foundational level, constituting a granularity difference.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs employ an identical proof by contradiction: assume BC is not in the plane of reference containing BD and BE, construct line BF as the common section of the plane through AB, BC with the plane of reference (11.3), establish that AB is perpendicular to the plane of reference (11.4), derive that angle ABF is right (D11.3), note that angle ABC is also right, and reach a contradiction. The AI proof cites three additional items not in Heath: 11.2 (to justify explicitly that BD, BE lie in one plane and that AB, BC lie in one plane), P4 (to justify that all right angles are equal), and CN5 (to name the axiom that the whole is greater than the part). All three are over-citations of steps Heath treats as implicit. Since heath_only is empty and the key intermediate conclusions are identical in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.6
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: establishing right angles via D11.3, proving AD = BE through triangle congruence (I.4), showing angle EDA is right via I.8, concluding coplanarity of BD, DA, DC through XI.5, placing AB in that plane via XI.2, and deriving parallelism via I.28. The ai_only set {1.11, 1.3, P1, P4} consists entirely of construction propositions and postulates that Heath uses implicitly without citation: 1.11 for drawing a perpendicular, 1.3 for cutting off an equal length, P1 for joining lines, and P4 for the equality of right angles. The AI explicitly justifies each construction step while Heath performs them silently. With identical backbones and differences confined to citation depth on construction and axiomatic steps, this is Case A of Q2, yielding G.

### 11.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs employ the same proof-by-contradiction backbone: assume the line joining E and F lies in an elevated plane as EGF, draw a plane through EGF whose intersection with the reference plane yields a straight line EF by 11.3, observe that EGF and EF would then be two distinct straight lines enclosing a space (impossible), and conclude the joining line lies in the reference plane. The AI proof explicitly cites D1.23 (definition of parallel lines lying in one plane), D1.4 (definition of a straight line), and P1 (postulate for joining two points), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions and a postulate, the proofs share the same logical backbone at different citation depths, yielding Granularity difference (G).

### 11.8
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: from the perpendicularity of AB to the plane, they establish that angles ABD and ABE are right, use I.29 on the parallels to show CDB is right, apply SAS congruence to get AD = BE, apply SSS congruence to show angle EDA is right, then use XI.4 twice (first to show ED is perpendicular to the plane through BD and DA, then to show CD is perpendicular to the plane of reference) with XI.2 supplying that DC lies in the relevant plane. The AI proof cites seven additional references (1.11, 1.3, 1.4, 1.8, CN3, P1, P4) that Heath uses implicitly without citation. These are all construction propositions, basic congruence theorems, postulates, and a common notion, none of which represents a different logical path. With identical backbones and ai_only consisting entirely of over-citations for implicit steps, this is a granularity difference.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct perpendiculars GH and GK to EF in the two planes, show EF is perpendicular to the plane through GH and GK (11.4), infer that AB and CD are each perpendicular to that plane because they are parallel to EF (11.8), and conclude AB is parallel to CD because both are perpendicular to the same plane (11.6). The AI proof adds three citations not in Heath: D1.23 (definition that parallel lines lie in a plane), 1.11 (construction of a perpendicular at a point on a line), and 11.3 (common section of two planes is a line, used to justify that GH and GK are not collinear). These are a definition, a construction proposition, and a supporting lemma for a detail Heath leaves implicit. Heath cites nothing the AI omits. Since the key intermediate conclusions are identical and the citation differences reflect only granularity of justification, this is a granularity difference.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing equal segments BA=ED and BC=EF, showing AD and CF are each equal and parallel to BE via I.33, applying XI.9 to conclude AD is parallel to CF, then using I.33 again to establish AC equal and parallel to DF, and finally applying I.8 (SSS) for the angle equality. The AI's four additional citations (1.3 for cutting equal segments, P1 for joining lines, CN1 for transitivity of equality, and 11.7 for establishing non-coplanarity) are all explicit justifications for steps Heath performs implicitly. With heath_only empty and ai_only consisting entirely of construction, postulate, common notion, and supporting-detail citations, this is a clear Case A granularity difference.

### 11.11
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs construct the perpendicular AF from elevated point A to the given plane by the same method: dropping AD perpendicular to an arbitrary line BC in the plane, then (if AD is not already perpendicular to the plane) drawing DE perpendicular to BC in the plane, AF perpendicular to DE, and GH parallel to BC through F, and arguing through the same sequence of key intermediate conclusions -- BC is perpendicular to the plane through DA and DE (XI.4), GH is perpendicular to that plane by parallel transfer (XI.8), AF is perpendicular to GH (XI.Def.3), and AF being perpendicular to both DE and GH is perpendicular to the plane through them (XI.4), which is the plane of reference. The backbones are identical. The AI adds only D1.10 (definition of right angles) and P1 (postulate for drawing a line), both foundational items that Heath uses implicitly, making this a citation-depth difference rather than a path difference.

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: conceive an elevated point B, draw BC perpendicular to the plane (11.11), draw AD through A parallel to BC (1.31), conclude AD is perpendicular to the plane (11.8). The AI proof adds two extra citations not in Heath: P1 (to join AC, a postulate over-citation) and 11.2 (to explicitly establish that AC and BC lie in one plane, a detail Heath handles implicitly). Since heath_only is empty and the ai_only items represent finer-grained justification of steps that are implicit in Heath, this is a citation-depth difference with the same backbone, yielding G.

### 11.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume two lines AB, AC perpendicular to the reference plane from point A on the same side, draw a plane through them that intersects the reference plane in line DAE (11.3), show angle CAE is right and angle BAE is right (D11.3), then derive a contradiction from their equality. The AI proof adds explicit citations for steps Heath leaves implicit: 11.2 to justify that AB and AC determine a plane, P4 to state that all right angles are equal, and CN5 to articulate why the equality is impossible (one angle is a proper part of the other, so the whole exceeds the part). Since heath_only is empty and all ai_only items (11.2, CN5, P4) are foundational propositions, postulates, or common notions that make explicit what Heath assumes tacitly, this is a citation-depth difference with the same logical backbone, yielding G.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow an identical proof-by-contradiction backbone: assume the planes are not parallel, derive that their common section is a straight line GH (11.3), take a point K on GH and join AK, BK, show that angles ABK and BAK are both right by the definition of perpendicularity to a plane (D11.3), and reach a contradiction via I.17 (two angles of a triangle cannot sum to two right angles). The only citation difference is that the AI explicitly cites Postulate 1 for joining AK and BK, while Heath invokes this construction implicitly. Since the key intermediate conclusions are identical and the sole difference is citation depth for a construction postulate, Case A of Q2 holds, yielding G.

### 11.15
**Category**: Granularity difference
**Jaccard**: 0.583
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: drop a perpendicular BG from B to the plane through DE and EF (XI.11), construct parallels GH to ED and GK to EF in that plane (I.31), use the perpendicularity to establish right angles BGH and BGK (XI.Def.3), invoke XI.9 to show BA is parallel to GH, apply I.29 to derive that angle GBA is right, repeat for BC, conclude GB is perpendicular to the plane through BA and BC (XI.4), and finally apply XI.14 to establish the planes are parallel. The AI proof adds five citations not in Heath (1.30, 11.3, 11.7, CN3, D1.23), all of which serve as sub-step justifications for reasoning Heath performs implicitly: Step 1 uses 1.30 and D1.23 to prove B is elevated above plane Q (a prerequisite for XI.11 that Heath assumes), Step 5 uses 11.3 to justify that BA and GH are not coplanar with ED (needed for XI.9), Step 6 uses 11.7 to show BG lies in the plane of BA and GH and CN3 to subtract the right angle. Heath cites nothing the AI omits (heath_only is empty). Since the key intermediate conclusions match and the citation differences reflect only the depth of explicit justification, this is a granularity difference.

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction backbone: assuming the common sections EF, GH meet at a point K, applying 11.1 to show K lies in both parallel planes, deriving a contradiction, and repeating for the other direction to conclude EF is parallel to GH by the definition of parallel lines. The AI proof adds explicit citations for foundational facts that Heath leaves implicit: 11.3 (common sections are straight lines), D11.8 (definition of parallel planes), and P2 (postulate to produce lines). Since heath_only is empty and all ai_only items are over-citations at the construction/definition/postulate level, the proofs share the same logical backbone at different citation depths, yielding G.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: construct auxiliary line AD meeting plane KL at O, join EO and OF, establish EO parallel to BD and AC parallel to OF via XI.16, apply VI.2 twice to obtain AE:EB = AO:OD and AO:OD = CF:FD, then conclude AE:EB = CF:FD by V.11. The AI proof adds explicit citations of 11.2 (two intersecting lines determine a plane), 11.3 (common section of two planes is a line), and Postulate 1 (joining lines), which are foundational steps Heath leaves implicit. Since heath_only is empty and all ai_only items are construction or foundational propositions making explicit what Heath takes as understood, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 11.18
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct FG in plane DE perpendicular to the common section CE, show angle ABF is right via the definition of perpendicularity to a plane (Def. 3), deduce AB parallel to FG (I.28), transfer perpendicularity from AB to FG (XI.8), and conclude by Def. 4. The only citation difference is that the AI explicitly cites 11.3 to justify that the intersection of two planes is a straight line, a foundational step Heath takes as given without citation. This is a citation-depth difference (over-citation by the AI), not a backbone divergence, placing the proof squarely in Case A of Q2.

### 11.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing perpendiculars DE and DF in planes AB and BC respectively, showing each is perpendicular to the reference plane by Definition 11.4, and then invoking 11.13 (uniqueness of the perpendicular from a point to a plane) to reach the conclusion. Heath presents this as a reductio and the AI as a direct argument, but the key intermediate conclusions are identical. The ai_only citations (1.11 for constructing perpendiculars, 11.3 for identifying common sections as straight lines) are construction-level propositions that Heath uses implicitly, representing over-citation rather than a different proof path. With heath_only empty and the backbone matching, this is Case A of Q2: same backbone, different citation depth.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification as G. Both proofs follow the same logical backbone: construct angle BAE equal to DAB and AE equal to AD in the plane through BA and AC, prove DB equals BE by I.4, derive DC greater than EC from the triangle inequality I.20 and the equality DB equals BE, then conclude angle DAC greater than angle EAC by I.25, and finally combine with DAB equals BAE to get DAB plus DAC greater than BAC. The AI proof is more granular, explicitly citing construction propositions (1.23 for angle construction, 1.3 for cutting off equal segments), common notions (CN2, CN3, CN5 for addition, subtraction, and whole-greater-than-part), a definition (D11.11 for solid angles), and postulates (P1, P2 for joining and producing lines) that Heath leaves entirely implicit. Since heath_only is empty, every proposition Heath cites also appears in the AI set, and all ai_only items are construction, axiom, or definition citations rather than substantive theorems, confirming the same backbone at different citation depth.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions for the three-face solid angle case: using XI.20 to show the six non-face angles at vertices B, C, D exceed the three base triangle angles, then using I.32 to establish that the base angles equal two right angles and the nine total triangle angles equal six right angles, and finally subtracting to conclude the three face angles are less than four right angles. The AI proof additionally extends the argument to the general n-face case (Steps 10-14), but the shared three-face backbone is the same. The ai_only set {CN2, D11.11, P1} consists entirely of a common notion, a definition, and a postulate that Heath invokes implicitly, representing over-citation rather than a different proof path. heath_only is empty. Case A of Q2 holds, yielding G.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification as G. Both proofs share the same logical backbone: the equal-angles case is handled trivially via I.4, and the unequal-angles case constructs an auxiliary angle and triangle to copy one of the given angles, uses I.4 to equate the resulting base to one of AC/DF/GK, applies I.24 to establish a base inequality, and then invokes the triangle inequality to combine these results into the required condition that any two of AC, DF, GK exceed the third. The AI constructs the auxiliary angle at B on line AB (copying angle GHK) while Heath constructs it at H on line HK (copying angle ABC), but this is a minor variation in execution, not a different logical path. Every ai_only citation is either a construction step (1.3, 1.23, P1), a common notion (CN1, CN3, CN5), or an explicit citation of a result Heath uses implicitly (1.20 for the triangle inequality, 1.22 for the framing construction theorem). heath_only is empty. This is a clear case of same backbone with different citation depth.

### 11.23
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing triangle LMN via XI.22, circumscribing a circle with centre O, proving AB > LO by contradiction, setting up OR perpendicular to the plane of the circle with OR squared equal to the excess of AB squared over LO squared, establishing RL = RM = RN = AB, and concluding equal angles via I.8. The AI proof is strictly more granular, explicitly treating three sub-cases for the position of O relative to triangle LMN (inside, on a side, outside) and explicitly constructing the line whose square equals the excess via a semicircle, where Heath invokes a Lemma. The heath_only set is empty, confirming that the AI cites every proposition Heath does; the 26 ai_only items consist of construction steps, common notions, definitions, and additional propositions needed for the more detailed case analysis, all reflecting citation-depth differences rather than a different logical path.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use XI.16 to show that common sections of parallel planes cut by a third plane are parallel, establishing that each face is a parallelogram; then they use XI.10 to prove that angles between pairs of meeting parallel lines in different planes are equal, I.34 to obtain equal opposite sides from the parallelograms, I.4 for triangle congruence, and I.34 again for the diagonal-bisection property to conclude that opposite faces are equal. The AI proof cites every foundational item it invokes (CN1 for transitivity of equality, CN2 for adding equals to equals, D11.8 for the definition of parallel planes, P1 for joining points), whereas Heath leaves these implicit. Since heath_only is empty and all ai_only items are common notions, a definition, and a postulate, this is a clear case of over-citation at the same backbone, yielding a granularity difference.

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Both proofs follow the identical equimultiples strategy for establishing the proportion base:base :: solid:solid via V.Def.5. The key intermediate conclusions are the same in both: constructing replicated segments and completing solids, showing component parallelograms and solids are equal, establishing that base-multiples and solid-multiples track together, handling the equal/greater/less trichotomy, and applying V.Def.5. The AI proof cites 13 references while Heath cites only 2 (11.24 and D5.5), but the 11 ai_only items are all construction propositions (1.3, 1.31, P2), auxiliary results about parallels and equal parallelograms (1.30, 1.36, 11.15, 11.16), common notions (CN1, CN5), and definitions (D11.10, D5.2) that Heath uses implicitly without citation. heath_only is empty, confirming the AI covers all of Heath's cited ground. This is a clear case of same backbone with different citation depth, yielding G.

### 11.26
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided this classification as Granularity difference (Case A). Both proofs follow the identical logical backbone for constructing a solid angle at A equal to the given solid angle at D: both drop a perpendicular from the elevated point to the base plane, construct matching angles and segments at A, then use three applications of I.4 (SAS congruence) to establish equality of corresponding bases (KB=GE, HB=FE, AH=FD), followed by I.8 (SSS congruence) to establish equality of the plane angles composing the solid angle. The only structural difference is that the AI explicitly works through the proof of angle HAL = angle FDC in four detailed steps (Steps 10-13, using CN3, I.4, I.4, and I.8), whereas Heath compresses this with 'for the same reason.' The ai_only set consists entirely of construction propositions (1.3), common notions (CN3), definitions (D11.11), and postulates (P1, P4), all making explicit what Heath leaves implicit. The heath_only set is empty, confirming the AI covers all of Heath's cited results at greater depth.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a solid angle at A equal to the solid angle at C, set up the proportions EC:CG = BA:AK and GC:CF = KA:AH via VI.12, derive EC:CF = BA:AH ex aequali via V.22, complete the solid AL, show three pairs of similar parallelograms, extend to all six faces, and conclude similarity of the solids via XI.Def.9. The AI proof cites 10 additional references that Heath uses implicitly: 11.26 for solid angle construction, 1.3 and 1.31 for construction steps, 1.34, 1.29, CN3, and D6.1 for spelling out the parallelogram similarity argument, 11.15 for parallel planes, 11.24 for opposite faces being equal and similar, and 6.21 for transitivity of similarity. The empty heath_only set confirms that every citation Heath uses is also present in the AI proof. This is a clear case of same backbone with different citation depth, yielding G.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they bisect face parallelograms into equal triangles via I.34, note that opposite faces are equal parallelograms, and conclude that the two resulting prisms are equal by XI. Def. 10 (D11.10). The AI proof additionally cites 11.3 (to establish that the cutting plane intersects each face in a straight line), 11.16 (to show the resulting section is a parallelogram by proving opposite sides are parallel), and 11.24 (to justify that opposite faces are equal), all of which Heath uses implicitly without citation. Since heath_only is empty and the ai_only items are all construction or setup propositions that make explicit what Heath leaves tacit, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.29
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: establishing DE=HK and FG=MN by subtraction from equal opposite sides of parallelograms (I.34), proving triangles DCE=HBK and AFG=MLN via I.8 and I.4, showing the relevant parallelograms equal via I.36, concluding the two prisms are equal, and adding the same solid to obtain CM=CN. The AI proof is substantially more detailed, explicitly citing common notions (CN1, CN2, CN3), definitions (D11.10), and supporting propositions (11.24, 11.9, 1.29) that Heath uses implicitly or without citation. Since heath_only is empty and all ai_only items are either common notions, definitions, or minor propositions providing explicit justification for steps Heath takes as understood, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Both proofs follow the identical strategy of constructing a third parallelepipedal solid on the same base by producing edges in the upper plane to meet at auxiliary points, then applying 11.29 twice to show each original solid equals the third, and concluding by transitivity. The AI's nine extra citations (11.1, 11.3, 11.9, 11.24, CN1, D1.23, D11.8, P1, P2) are all definitions, postulates, common notions, and foundational Book 11 propositions that spell out the construction details Heath leaves entirely implicit. Heath's citation set (11.29 alone) is a proper subset of the AI's, and heath_only is empty, confirming complete coverage with no independent route. This is a clear case of same logical backbone at different citation depth, yielding G.

### 11.31
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical logical backbones across both cases (right-angle sides and oblique sides). In Case 1, both construct an auxiliary parallelepiped XU equal and similar to AE, show XU equals YX via XI.29, establish YT equals CD via I.35, and conclude CF equals YX through the same ratio chain (XI.25, V.7, V.11, V.9). In Case 2, both drop perpendiculars to create right-angled solids and reduce to Case 1 via XI.30. The heath_only set is empty, meaning every reference Heath cites also appears in the AI proof. The 15 ai_only items are entirely construction propositions (1.3, 1.31), basic plane geometry results (1.4, 1.29, 1.30, 1.34), common notions (CN1, CN2), definitions (D1.23, D11.3, D6.1, D6.4, D11.10), and postulates (P2, P4), all representing lower-level steps that Heath leaves implicit. The Jaccard of 0.40 reflects this one-sided over-citation rather than any structural divergence.

### 11.32
**Category**: Granularity difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: (1) construct a parallelogram equal to base AE adjacent to base CF, (2) complete a parallelepipedal solid on that parallelogram with the same height as CD, (3) invoke XI.31 to establish that the new solid equals AB, (4) invoke XI.25 on the cutting plane to obtain the ratio CF:new-base = CD:new-solid, and (5) substitute to conclude AE:CF = AB:CD. The sole structural difference is how step (1) is accomplished: Heath cites I.45 in a single step, while the AI first converts the parallelogram AE into an equal triangle (via I.38, I.34, CN1, CN2) and then applies I.44 to the given line GF, followed by collinearity verification (I.29, I.14) and parallelogram completion (I.30, I.31). Since I.45's own proof uses I.44 internally along with I.29, I.14, I.30, I.34, CN1, and CN2, the AI is re-deriving the internals of I.45 rather than citing it as a unit. The additional ai_only citations 5.7 and 5.11 make explicit the ratio substitution that Heath handles informally. All key intermediate conclusions match at the same logical positions, making this a citation-depth difference (Case A), hence G.

### 11.33
**Category**: Granularity difference
**Jaccard**: 0.227
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: constructing auxiliary solid KP equal and similar to CD by extending sides AE, GE, HE and cutting off segments equal to CF, FN, FR; establishing the continuous proportion AG:GK = GK:KL = QE:KM via VI.1; converting to the solid ratio AB:EO = EO:QL = QL:KP via XI.32; and applying V.Def.10 for the triplicate ratio. The heath_only set is empty, confirming the AI cites every reference Heath uses. The 17 ai_only items are entirely construction propositions (1.3, 1.31, P1, P2), basic geometric results (1.15, 1.29, 1.34, 1.4, 11.10), proportion-theory lemmas (5.7, 5.11, 5.16), common notions (CN1, CN2, CN3), and definitions (D11.9, D6.1), all representing finer citation granularity for steps Heath treats as understood. The AI even includes a full lemma (Step 4) proving that parallelograms with equal adjacent sides and included angles are equal and similar, which Heath states without proof. This is a clear case of same backbone with different citation depth.

### 11.34
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs share the same backbone structure: a right-angle case (with equal-base and unequal-base sub-cases for both directions of the biconditional) followed by an oblique case reduced to the right-angle case via perpendiculars and XI.29/30. The key intermediate conclusions are identical in both proofs: (1) AB:CV = EH:NQ from 11.32, (2) CD:CV = CM:CT, and (3) the oblique-to-right-angle reduction. The two heath_only items represent depth differences, not backbone differences: Heath uses 11.25 to obtain CD:CV = MQ:TQ by cutting with a parallel plane, whereas the AI uses 11.32 by reorienting which face is considered the base (Step 8), reaching the same proportion; Heath uses 11.31 directly for the equal-base sub-case, whereas the AI derives the same equality through 11.32 and proportion theory (5.9). The ten ai_only items are construction propositions (1.3, 1.31, 11.11, 11.15, 11.24, 11.6), proportion-chain intermediates (5.11), axioms (CN1), and definitions (D5.5, D6.4) that Heath applies implicitly. Same backbone, different citation depth: G.

### 11.35
**Category**: Granularity difference
**Jaccard**: 0.316
**Analysis**: Q2 decided this classification. Both proofs follow an identical logical backbone: construct AH equal to DM, show HK perpendicular to the plane via XI.8, establish that angles HCA and MFD are right via I.47 and I.48, prove AC equal to DF and AB equal to DE by AAS congruence (I.26), derive BC equal to EF by SAS (I.4), decompose the right angles to get equal remaining angles, use a second AAS (I.26) to get CK equal to FN, apply SAS (I.4) to get AK equal to DN, use the Pythagorean theorem to show HK equal to MN, and finally conclude angle HAK equals angle MDN by SSS (I.8). The ai_only set consists entirely of construction propositions (1.3, 1.12, 1.31, 11.11), foundational planarity results (11.2, 1.30), definitions (D1.23, D11.3), common notions (CN1, CN2, CN3), and postulates (P1, P4), all of which Heath leaves implicit. The heath_only set is empty, confirming the AI cites every proposition Heath cites plus additional lower-level justifications. This is a textbook case of over-citation at the same logical depth, yielding G.

### 11.36
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs construct two parallelepipedal solids (EK equilateral on the mean B, and LH formed from A, B, C) with equal solid angles, then establish identical key intermediate conclusions in the same order: (1) reciprocal proportionality of sides about equal angles NLM and DEF, (2) equality of parallelograms MN and DF via 6.14, (3) equality of perpendicular heights via 11.35 Porism, and (4) equality of the solids via 11.31. The AI cites additional construction propositions (1.3, 11.26), proportion lemmas (5.7, 5.11), and a common notion (CN1) that Heath leaves implicit, while heath_only is empty, confirming that every proposition Heath cites is also cited by the AI. This is a classic Case A granularity difference: same logical backbone with the AI citing at finer depth.

### 11.37
**Category**: Path difference
**Jaccard**: 0.077
**Analysis**: Q2 decided the classification. For Part 1 (the forward direction), both proofs share the same backbone: each establishes that KA:LC is the triplicate of AB:CD and ME:NG is the triplicate of EF:GH via XI.33, then concludes the solid ratios are equal. However, for Part 2 (the converse), the AI takes a fundamentally different path from Heath. Heath simply reverses the triplicate ratio argument directly, while the AI constructs a fourth proportional O (6.12), builds a similar solid PO on O (11.27), applies Part 1 to deduce ME:PO = KA:LC = ME:NG, concludes NG = PO (5.9), establishes similarity of NG and PO (6.21, D11.9), and then proves GH = O through an elaborate indirect argument using 5.14. These key intermediate conclusions -- the construction of O and PO, the equality NG = PO, and the indirect proof that GH = O -- are entirely absent from Heath's proof. The AI's different path is logically complete and valid (Q3 holds), yielding category D.

### 11.38
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: they establish that midpoint-connecting segments form straight lines through triangle congruence, show that key diagonals across the cube are equal and parallel using XI.9 and I.33, and then use congruent triangles at the intersection point T (via alternate angles I.29, vertical angles I.15, and ASA congruence I.26) to conclude that the common section and the diameter bisect one another. The AI proof adds four citations not in Heath (1.13 for supplementary angles, 11.3 for plane intersections yielding lines, 11.7 for lines lying in planes of parallels, and D11.25 for the definition of a cube), all of which are foundational or constructive facts that Heath leaves implicit. Since heath_only is empty and the AI's extra citations are all over-citations of foundational material rather than substantive path differences, this is Case A of Q2: same backbone with different citation depth.

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical path: complete parallelepipedal solids on each base, establish that the base parallelograms are equal (using I.34), apply XI.31 to conclude the completed solids are equal, then use XI.28 to show each prism is half its respective solid, yielding equality of the prisms. The AI proof cites the same three substantive propositions as Heath (1.34, 11.28, 11.31) and adds explicit references to common notions (CN1, CN2, CN5) and a definition (D11.13) that Heath uses implicitly. The heath_only set is empty, confirming no missing steps. This is Case A of Q2: same backbone, different citation depth, yielding G.
