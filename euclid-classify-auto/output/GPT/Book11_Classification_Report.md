# Book 11 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 24 | 11.1, 11.5, 11.6, 11.9, 11.10, 11.11, 11.12, 11.14, 11.15, 11.16, 11.17, 11.18, 11.20, 11.21, 11.22, 11.24, 11.25, 11.27, 11.28, 11.29, 11.30, 11.33, 11.36, 11.39 |
| Path difference (D) | 15 | 11.2, 11.3, 11.4, 11.7, 11.8, 11.13, 11.19, 11.23, 11.26, 11.31, 11.32, 11.34, 11.35, 11.37, 11.38 |
| AI proof error (E) | 0 |  |

**Total**: 39 propositions

## Per-Proposition Analysis

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use contradiction by the same backbone: suppose part AB is in the reference plane and part BC is elevated, construct a straight continuation of AB beyond B within the plane, then argue that two distinct straight continuations of the same segment from the same endpoint are impossible, so BC must lie in the plane as well. Heath justifies the impossibility via a common-segment argument with a circle, while the AI invokes Definition 1.4 (a straight line lies evenly with its points) to argue uniqueness of continuation directly. The key intermediate conclusions are identical; the difference is purely one of citation depth. The AI explicitly cites D1.4, D1.7, and P2, all of which are definitions and postulates that Heath leaves implicit (heath_refs is empty). This is Case A in Q2: same backbone, different citation depth, yielding G.

### 11.2
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath proves XI.2 by contradiction: he assumes part of the triangle ECB formed by the intersecting lines lies in a different plane, derives that parts of the constituent lines would lie in different planes (contradicting XI.1), and concludes the triangle and the lines are coplanar. The AI instead takes a constructive approach, using I.31 to draw a line parallel to one of the intersecting lines through a point on the other, then invoking the definition of parallel lines (D1.23) to establish that the parallel and the original line share a plane, and finally applying XI.1 to show the second intersecting line must also lie entirely in that plane. These are fundamentally different backbones: Heath relies on proof by contradiction, while the AI relies on a constructive argument via parallel lines. Since the AI's chain is logically complete with every step supported by an explicit citation, Q3 confirms the different path is valid, yielding category D.

### 11.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof is a direct reductio that cites no prior propositions: it assumes the common section is not straight, draws two different straight lines between the endpoints (one in each plane), and derives a contradiction from the impossibility of two straight lines enclosing an area. The AI proof takes a fundamentally different route by invoking Proposition 11.1 (a straight line partly in a plane remains in that plane). The AI first shows that the line through two common points lies entirely in the common section, then proves by contradiction that no point outside this line can belong to the common section, since a triangular region common to both planes would allow constructing a line that is partly in and partly outside one plane, violating 11.1. These are genuinely different key intermediate conclusions forming different logical backbones, and the AI's path is logically complete under the Q1(b) hardened standard, yielding D.

### 11.4
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 revealed fundamentally different backbones, sending the classification to Q3. Heath's proof uses a symmetric construction with equal segments on both intersecting lines, then applies I.26 (AAS congruence) to establish equal segments on an arbitrary line through the intersection, building up through an auxiliary point F to show the perpendicular makes right angles with that arbitrary line. The AI instead uses a reflection argument: it places points A and A' symmetrically on the perpendicular (OA = OA'), shows via I.4 and I.8 that triangles on opposite sides are congruent, and uses the parallel postulate (P5) with I.17 to establish that an arbitrary line through O intersects a segment joining points on the two given lines. The AI never invokes I.26 (the sole heath_only item), while Heath never uses 1.14, 1.17, 1.3, 11.1, 11.2, or P5. Under Q3, the AI's different path is logically complete: each step follows validly from the preceding ones, and the chain runs from premises to the conclusion that the line is perpendicular to the plane.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume the third line is not coplanar, establish the erected line is perpendicular to the plane of the other two (11.4), find the intersection line of the two planes (11.3), deduce perpendicularity to that intersection line (D11.3), and derive a contradiction. The AI makes explicit via 1.14 the step that Heath leaves implicit (that two right angles on the same side force collinearity), and explicitly cites 11.2 for plane existence and P2 for line extension, both implicit in Heath. Since heath_only is empty and all ai_only items are over-citations making implicit steps explicit, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.6
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a symmetric auxiliary figure in the reference plane, apply I.4 (SAS) to establish equal lengths, apply I.8 (SSS) to establish angle equality yielding perpendicularity, use XI.5 to establish coplanarity of the relevant lines, and conclude parallelism via I.28. The AI proof explicitly cites construction propositions (1.11, 1.3), postulates (P1, P2, P4), definitions (D1.10, D1.7), and additional Book 11 lemmas (11.1, 11.3) that Heath uses implicitly. The AI also includes a distinctness-of-feet argument in Step 1 using 1.14, 11.2, and 11.3. Since heath_only is empty, every proposition Heath cites is also cited by the AI; the extra AI citations represent finer-grained explicit citation of construction steps and foundational results, not a different proof path.

### 11.7
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs use reductio ad absurdum to show the joining line lies in the plane of the parallels, but they reach their contradictions through fundamentally different key intermediate conclusions. Heath supposes the joining line is in a more elevated plane as EGF, then uses 11.3 to show a plane through EGF cuts the reference plane in a straight line EF, so two distinct lines EGF and EF would enclose an area, which is impossible. The AI instead uses 11.2 to establish that the joining line AB and the parallel line l determine a plane Sigma, then assumes Sigma differs from the plane Pi of the parallels; since both planes contain l, their intersection (by 11.3) is along l, forcing B onto l and making the parallels meet, contradicting their definition. The contradiction mechanisms differ (two lines enclosing an area vs. parallel lines meeting), and the AI substantively employs 11.2 in a way Heath does not, constituting a genuine path difference. Q3 confirmed the AI path is logically complete and valid.

### 11.8
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 reveals genuinely different backbones, deciding this as a path difference (D). Heath's proof establishes the key intermediate conclusion that ED is perpendicular to the plane through BD and DA by using triangle congruence (implicitly I.4 for SAS and I.8 for SSS), then deduces that CD is perpendicular to DE because DC lies in that plane. The AI's proof instead establishes a different key intermediate conclusion: that BE is perpendicular to the plane Sigma containing the parallel lines, using the Pythagorean theorem (1.47) and its converse (1.48) to show angle ABE is right. From BE perpendicular to Sigma, the AI deduces BE perpendicular to m. Both proofs share the initial step of showing CD (or m) perpendicular to BD (or s) via I.29, but after that they diverge in both technique and intermediate geometric facts. The AI's different path is logically complete under Q3: every step is justified, the Pythagorean approach is mathematically sound, and the chain runs from premises to conclusion without gaps.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct perpendiculars to the common parallel line in each plane, show the common parallel is perpendicular to the plane determined by those perpendiculars (11.4), transfer that perpendicularity to each of the two given lines via their parallelism with the common line (11.8), and conclude the two lines are parallel because both are perpendicular to the same plane (11.6). The AI proof cites four additional items (1.11, 11.2, 11.3, D1.23) that are all construction steps, foundational plane-geometry facts, or definitions which Heath uses implicitly without explicit citation. Since heath_only is empty, the AI's citation set is a strict superset of Heath's, and the key intermediate conclusions are identical in both proofs, this is a granularity difference with the AI providing finer-grained citations.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: cut equal segments on the four rays, show via I.33 that the joins AD-BE and AD-CF are each equal and parallel, deduce BE = CF and BE parallel to CF (via XI.9), then obtain BC = EF (via I.33), and conclude the angles are equal by the SSS criterion I.8. The AI proof cites seven additional references (1.3, 11.1, 11.7, CN1, D1.23, D1.7, P1) that Heath leaves implicit; these are all construction propositions, postulates, common notions, and definitions, amounting to over-citation at finer granularity rather than a different logical path. Heath_only is empty, confirming that every substantive step Heath uses also appears in the AI proof. This is Case A of Q2: same key intermediate conclusions with different citation depth.

### 11.11
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: draw a line in the plane, drop a perpendicular from A to it, handle the trivial case where that perpendicular is already perpendicular to the plane, then in the main case draw a second line perpendicular to the first in the plane, establish that the first line is perpendicular to a certain plane (XI.4), drop a perpendicular to the second line within that plane, draw a parallel and transfer perpendicularity via XI.8, and conclude the constructed segment is perpendicular to the given plane by XI.4. The AI adds five extra citations (11.1, 11.2, D1.23, P1, P2) that are all foundational or constructive -- postulates for drawing lines, a definition, and basic results about lines and planes in space -- which Heath treats as implicit. Since heath_only is empty and the ai_only items are all over-citations for foundational steps, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a perpendicular BC from an elevated point to the plane via 11.11, draw AD through the given point A parallel to BC via 1.31, and conclude AD is perpendicular to the plane via 11.8. The AI adds explicit citations for 11.2 (that intersecting lines AB and BC determine a plane, justifying the environment for the parallel construction) and P1 (joining A to B), both of which are implicit in Heath's more concise treatment. Since the key intermediate conclusions are identical and the ai_only items represent finer citation granularity rather than a different argumentative path, this is a granularity difference.

### 11.13
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 11.13 by drawing a plane through the two assumed perpendiculars, producing a line in the reference plane, and showing by D11.3 that two angles in that plane must both be right, which is impossible. The AI takes an entirely different route: it invokes 11.6 (lines perpendicular to the same plane are parallel) and D1.23 (parallel lines do not meet) to obtain a contradiction with the two lines sharing a common point. The citation sets are completely disjoint (Jaccard 0.0), and the key intermediate conclusions differ fundamentally: Heath reasons about angles forced to be equal in a plane, while the AI reasons about parallelism forcing the lines not to meet. Since the AI's chain is logically complete and valid under the hardened 1(b) standard, this is a path difference.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume the two planes meet, form a triangle with the perpendicular line, establish that two angles of that triangle are right angles (via D11.3), and derive a contradiction using I.17 (the sum of two angles of a triangle is less than two right angles). The AI proof adds extra sub-arguments not in Heath (showing the feet A and B are distinct via 11.5, showing the common point cannot lie on the perpendicular line via 11.1) and is more explicit about foundational facts (citing 11.2 for the triangle lying in one plane, D1.7 for lines lying in planes, P1 for joining points), but these do not alter the key intermediate conclusions. Since heath_only is empty and all ai_only items are either over-citations of implicit constructions or extra rigor steps within the same backbone, this is Case A: same backbone, different citation depth, yielding G.

### 11.15
**Category**: Granularity difference
**Jaccard**: 0.538
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a perpendicular from a point to one plane, build parallel lines through the foot of the perpendicular, use XI.9 and I.29 to show the perpendicular is also at right angles to lines in the second plane, conclude it is perpendicular to the second plane via XI.4, and then invoke XI.14 to establish the planes are parallel. The AI proof includes additional explicit steps that Heath leaves implicit, such as proving B lies outside the first plane (using 11.3), establishing the existence of the planes (11.2), justifying coplanarity of the perpendicular with parallel line pairs (11.7), and citing transitivity of parallelism (1.30). Since heath_only is empty and all six extra AI citations serve to elaborate on the same chain of reasoning rather than introducing a different logical path, this is a granularity difference.

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing that the common sections of a cutting plane with two parallel planes are straight lines, then arguing by contradiction that if those lines met at a point, that point would lie in both parallel planes (by 11.1), forcing the planes to meet and contradicting the hypothesis of parallelism, and finally concluding parallelism of the sections by Definition 1.23. The AI proof adds explicit citations to 11.3 (that sections of intersecting planes are straight lines), D11.8 (definition of parallel planes), and P2 (production of a line), all of which Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are foundational or definitional over-citations that do not alter the logical backbone, this is a granularity difference.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: construct an auxiliary point where a joining line meets the middle plane, apply XI.16 twice to establish parallelism of common sections, apply VI.2 twice in two triangles to obtain proportional segments, and chain the ratios via V.11. The AI constructs AF meeting the middle plane at G while Heath constructs AD meeting plane KL at O, but the key intermediate conclusions (two parallelism results, two proportional-cutting results, one transitivity step) are identical in structure and role. The ai_only citations (11.1, 11.2, 11.3, D11.8, P1) are all foundational construction and definition references that Heath uses implicitly without citation, confirming a citation-depth difference rather than a path difference.

### 11.18
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Both proofs share the same logical backbone: they establish that any line drawn in the plane through AB at right angles to the common section must be perpendicular to the reference plane, by showing parallelism to AB via I.28 and then transferring perpendicularity via XI.8, concluding with D11.4. The citation differences are entirely at the granularity level. Heath uses I.11 to construct a specific perpendicular from a point on the common section, while the AI takes an arbitrary perpendicular as given and handles two sub-cases (coincidence with AB when C=B, and the general case when C differs from B), citing additional foundational items (11.3 for the common section's existence as a line, and P4/CN5/D1.10 for the coincidence argument). Since the key intermediate conclusions are the same and the citation differences reflect depth rather than direction, Q2 Case A applies and the classification is G.

### 11.19
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs establish the shared intermediate that lines drawn in each plane perpendicular to their traces on the reference plane are themselves perpendicular to the reference plane (via Def. 11.4). However, the logical strategies then diverge fundamentally: Heath uses proof by contradiction, assuming the common section is not perpendicular and deriving two perpendiculars from the same point on the same side, which contradicts 11.13. The AI uses a direct proof, showing that the two constructed perpendiculars must coincide because perpendiculars to a plane are parallel (11.6) yet these lines meet at the same point (contradicting D1.23), and the coincident line is the common section (11.3), which is therefore perpendicular. These constitute genuinely different proof backbones — reductio via uniqueness of perpendicular (11.13) versus direct argument via parallelism of perpendiculars (11.6) — satisfying Case B in Q2 and yielding a valid different path under Q3.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct an auxiliary point splitting the greatest face angle, use I.4 to establish equal segments, apply I.20 (triangle inequality) to derive a base inequality, then use I.25 to convert it to an angle inequality, and finally add angles to reach the conclusion. The AI proof cites additional construction propositions (1.23, 1.3), common notions (CN2, CN3, CN5), definitions (D11.11), postulates (P1, P2), and a supporting geometric fact (11.2) that Heath leaves implicit, while heath_only is empty, confirming all of Heath's citations are subsumed by the AI's set. This is a clear case of same backbone with different citation depth, yielding G.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: (1) apply XI.20 at each base vertex to establish that the sum of two lateral face angles exceeds the corresponding base polygon angle, (2) use I.32 to compute the base polygon angle sum and the lateral triangle angle sums, and (3) subtract to conclude that the solid angle's plane angles sum to less than four right angles. The AI generalizes from Heath's 3-face case to n faces, but the proof technique is structurally identical. The ai_only set consists entirely of definitions (D11.11), common notions (CN2, CN3, CN5), postulates (P1, P4), and basic solid geometry construction propositions (11.2, 11.3) that Heath leaves implicit, while heath_only is empty. This is a citation-depth difference, not a backbone difference, so the classification is G.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided this classification. Both proofs handle two cases (angles equal vs. unequal) and share the same logical backbone in the unequal case: construct an auxiliary figure that replicates one of the smaller angles within the largest angle's configuration, use I.4 to establish a base equality, derive an angle inequality from the hypothesis, apply I.24 to obtain a base inequality, then invoke the triangle inequality to conclude that any two of the three bases together exceed the third. The constructions differ in geometric detail (Heath places the angle on segment HK; the AI uses a circle with center O and radius r), but constructive sub-steps are not key conclusions under the protocol. The AI's nine additional citations (1.20, 1.22, 1.23, 3.2, CN2, CN5, D1.15, P1, P3) are either propositions Heath uses implicitly without citing (1.20 for the triangle inequality, 1.22 for constructability), construction tools (1.23, P1, P3, D1.15), axioms (CN2, CN5), or a constructive sub-step detail specific to the circle approach (3.2). Heath's citation set is a proper subset of the AI's, and heath_only is empty. This is a clear case of same backbone with different citation depth.

### 11.23
**Category**: Path difference
**Jaccard**: 0.129
**Analysis**: Q2 determines the classification. Heath's proof constructs a triangle from the base lengths of the three angle arms, circumscribes a circle about it, and proves by contradiction (two sub-cases using I.25, V.16, VI.2, VI.4) that the arm length exceeds the circumradius, then lifts perpendicularly from the center. The AI proof takes a fundamentally different route: it places points on a circle at the prescribed angular separations, identifies two chords whose endpoints alternate cyclically so they must intersect at an interior point D, uses the intersecting-chords theorem (3.35) and II.5 to establish power-of-point relations linking the circumradius, chord distances, and arm distances to a common quantity k, constructs a perpendicular lift from D with height h where h-squared equals k, and derives the required side equalities via I.47 before concluding with SSS congruence (I.8). The only shared key conclusion is the final angle-equality step; the entire intermediate mechanism differs. The AI's chain is logically complete under the hardened standard, so the different backbone yields D.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) show all six faces are parallelograms via XI.16, (2) establish equality of corresponding sides of opposite faces via I.34, (3) show corresponding included angles are equal via XI.10, (4) prove corresponding triangles congruent via I.4 (SAS), and (5) conclude opposite parallelograms are equal by doubling the congruent triangles via I.34 (diagonal bisection). The AI proof adds four over-citations not in Heath: 11.3 for edges being straight lines as common sections of planes, P1 for joining diagonals, and CN1/CN2 for combining equal triangles. Heath uses all of these facts implicitly. Since heath_only is empty and the ai_only items are all foundational (a postulate, common notions, and a basic intersection result), this is Case A of Q2: same backbone, different citation depth.

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.105
**Analysis**: Q2 decided the classification. Both proofs follow the same equimultiple strategy for proving the proportion between bases and solids: construct unit slabs by extending edges, show slabs with equal intercepts have equal faces and are therefore equal solids with equal bases, stack m and n copies to form equimultiples, perform the three-way comparison (exceeds, equals, falls short), and apply V.Def.5. The backbones are identical. The large ai_only set (17 items) consists entirely of sub-results that Heath uses implicitly: where Heath cites XI.24 as a single unit to establish that opposite planes are equal, the AI explicitly derives face congruence through parallel line properties (1.29, 1.30), parallelogram properties (1.34), SAS (1.4), and solid geometry foundations (11.2, 11.10, 11.15, 11.16), along with construction propositions (1.3, 1.31, P2), common notions (CN2, CN4, CN5), and definitions (D5.2, D6.1, D11.10). The empty heath_only set confirms the AI covers all of Heath's reasoning. This is a clear case of same backbone with different citation depth, yielding G.

### 11.26
**Category**: Path difference
**Jaccard**: 0.357
**Analysis**: Q2 reveals different logical backbones, leading to classification D. Heath establishes face-angle equality by proving corresponding side equalities through three applications of I.4 (SAS congruence) and then applying I.8 (SSS congruence) to conclude that the face angles of the constructed solid angle match the given one. The AI instead uses a superposition and coincidence argument: after copying the base triangle and reproducing perpendicular offsets, it invokes XI.13 (uniqueness of perpendicular to a plane from a point on the same side) to show the perpendicular rays coincide, and CN5 (the whole is greater than the part) to establish that endpoints of equal-length segments on coincident rays must coincide. The AI never establishes the individual side equalities (KB=GE, HB=FE, AH=FD) and never uses I.8; it reaches the conclusion through an independent geometric method based on configuration coincidence. Since this constitutes a different backbone (Case B in Q2), and the AI's chain from premises to conclusion is logically complete under Q3(b), the classification is D.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.150
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct an equal solid angle, set edge-length proportions via VI.12, apply ex aequali (V.22), complete the parallelepiped, show three pairs of faces are similar through proportional sides about equal angles, and conclude whole-solid similarity by XI.Def.9. Heath cites only three references (5.22, 6.12, D11.9), all of which appear in the AI's set, while the AI explicitly cites 17 additional items that are construction steps (1.2, 1.31, P2, P3), basic parallelogram properties (1.29, 1.34, P4, CN3), Book 11 foundational results used implicitly by Heath (11.2, 11.10, 11.15, 11.16, 11.24, 11.26), similarity transitivity (6.21), and definitions (D11.11, D6.1). Heath takes all of these for granted or invokes them without citation. The heath_only set is empty, confirming the AI covers every step Heath cites. This is Case A of Q2: same backbone, different citation depth.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: the cutting plane divides the parallelepiped into two parts whose bounding faces are pairwise equal in multitude and magnitude, hence the parts are equal by XI. Def. 10. Heath applies I.34 directly to show each diagonal bisects a parallelogram face into equal triangles and notes that opposite faces are equal, concluding tersely by Def. 10. The AI proof reaches the same conclusion through a more elaborated route, explicitly citing 11.24 for opposite-face equality, 1.4 (SAS) with sides from 1.34 and angles from 11.10 for the triangular faces, and additional definitions and common notions (D1.7, D11.2, D6.1, CN1, CN4) to justify each sub-step. Since heath_only is empty and all ai_only items are supporting details that expand the same backbone argument, this is Case A of Q2: same backbone, different citation depth.

### 11.29
**Category**: Granularity difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish segment equalities from parallelogram properties, prove congruence of the triangular faces of two complementary end sub-solids, prove equality of the remaining faces, conclude sub-solid equality, and then use addition/subtraction of a common piece to obtain the final equality of the two parallelepipeds. The differences lie in the specific tools deployed at each step: Heath uses I.8 (SSS) for triangle congruence while the AI uses SAS (I.4) with angles from I.29 and 11.10; Heath uses I.36 for parallelogram equality while the AI establishes all face equalities and applies D11.10 for solid equality. The AI also cites many additional supporting items (definitions, common notions, postulates, and book 11 spatial lemmas) that Heath leaves implicit. Since the key intermediate conclusions are the same at corresponding logical positions and the citation differences reflect different levels of detail and choice of supporting lemma rather than a fundamentally different proof strategy, this is a granularity difference.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.077
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct an intermediate parallelepipedal solid, then apply XI.29 twice to show each original solid equals the intermediate one, concluding the two original solids are equal. Heath's proof is concise, citing only XI.29 for the two applications. The AI proof provides the same strategy but with far more explicit detail, citing supporting propositions for why the upper faces are coplanar (11.16, 11.6, 1.34), why the intermediate construction forms a valid parallelepiped (11.24, 11.9, 1.30), and foundational items (CN1, D1.23, D11.3, D6.4, P1, P2) that Heath leaves implicit. Since heath_only is empty and the ai_only items are all supporting or foundational citations that flesh out the same argument, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 11.31
**Category**: Path difference
**Jaccard**: 0.267
**Analysis**: Q2 decided the classification. Heath proves the right-parallelepiped case by copying the base of solid AE alongside solid CF using I.23, constructing auxiliary solid XU equal to AE via XI.24 and D11.10, then showing XU equals an intermediate solid XY via XI.29, and finally using XI.25 ratio arguments on two extended solids to conclude CF equals YX and hence AE. The AI takes a fundamentally different three-stage reduction: it first replaces each solid by an equal right parallelepiped (XI.29/XI.30), then converts each right parallelepiped to an equal rectangular box by constructing a rectangle of equal area on the same base (I.11, I.31, I.35) and applying XI.29, and finally compares the two rectangular boxes by constructing a single containing box W and cutting it in two perpendicular directions, using XI.25 ratios with V.18 composition and V.9 to conclude equality. The rectangular box conversion and containing-box comparison strategy are entirely absent from Heath, and Heath's base-copying construction via I.23 and appeal to D11.10 are absent from the AI proof. These constitute genuinely different logical backbones. The AI's path is logically complete, with each step properly justified by valid citations.

### 11.32
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 reveals genuinely different logical backbones. Heath constructs a parallelogram FH equal to base AE alongside the second solid's base CF (using I.45), completes parallelepiped GK, establishes AB = GK via XI.31, then cuts the combined parallelepiped CK by a plane to obtain the base ratio via XI.25. The AI instead extends the first parallelepiped S by dividing the second base into triangles, applying I.44 twice to build an auxiliary parallelepiped U with base area equal to the second base, then applies XI.25 to the combined solid W = S + U to get S:U = P:R, establishes U = T via XI.31, and completes the proof with ratio substitution (5.7, 5.11). The constructions differ fundamentally (copy-alongside vs extend-and-cut), the order of applying XI.25 and XI.31 is reversed, and the AI introduces ratio algebra (5.7, 5.11) absent from Heath. Under Q3 the AI's path is logically valid with every step properly cited, so the classification is D.

### 11.33
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish edge proportionality from similarity of the parallelepipeds, construct a solid equal and similar to the second solid adjacent to the first, insert two intermediate solids each differing by one edge, use XI.32 and VI.1 to show that the ratio between each consecutive pair equals the ratio of corresponding edges, then invoke V.Def.10 to conclude the triplicate ratio. The sole heath_only citation (11.24) passes the proof-tree containment test: the AI re-derives in Step 3 the fact that opposite faces of a parallelepiped are equal and similar using 11.10, 1.34, and 1.4, which are exactly the propositions appearing inside Heath's own proof of 11.24. The thirteen ai_only items are construction postulates (P2, P3), elementary planimetric results (1.4, 1.31, 1.34), a solid-geometry lemma (11.10, 11.15), ratio-manipulation steps (5.11, 5.16), definitions (D11.9, D6.1), and common notions (CN1, CN2) -- all representing finer-grained citation of the same underlying argument rather than a different proof path.

### 11.34
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary solid on the second solid's base NQ, uses XI.25 (plane-cutting ratio) and XI.32 to establish the reciprocal proportion, and reduces the oblique case to the right-angle case via XI.29/30. The AI proof takes a fundamentally different approach: it constructs two right parallelepipeds R1 and R2 on the same base F1 with heights h1 and h2, equates R1 with the original solid S1 via XI.31 (which handles both right and oblique solids directly), and then derives R2:R1 = h2:h1 through a novel lateral-face argument applying XI.32 in a rotated orientation combined with VI.1. This different backbone avoids XI.25, XI.29, and XI.30 entirely, replacing them with XI.31, XI.15, XI.12, XI.8, and the lateral-face technique. Since the key intermediate conclusions differ (same-base auxiliary pair vs. second-base auxiliary; lateral-face ratios vs. plane-cutting ratios; direct oblique handling vs. perpendicular reduction) but the AI's chain is logically complete, this is a genuine path difference.

### 11.35
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof relies on the Pythagorean theorem (I.47) and its converse (I.48) to establish right angles at key points, then uses ASA congruence (I.26) repeatedly to propagate equalities through the configuration before finishing with SSS (I.8). The AI proof takes a fundamentally different route: it constructs a transversal through the perpendicular foot, builds up side equalities through multiple applications of SAS (I.4), and critically identifies the perpendicular foot via a proof by contradiction using I.17 (any two angles of a triangle sum to less than two right angles). The key intermediate conclusions differ entirely: Heath establishes right angles via the Pythagorean theorem, whereas the AI constructs corresponding segments and triangles via a transversal and proves the perpendicular foot coincidence by contradiction. The heath_only citations (1.26, 1.47, 1.48) are not subsumed by any higher-level AI citation; the AI simply uses different tools (1.13, 1.17, 1.31, 6.2, 11.2, 11.4) to reach the same conclusion by a different path. The AI proof is logically complete across its 11 explicit steps, with every claim properly supported by cited propositions, so Q3 confirms the path is valid.

### 11.36
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish equal bases via reciprocal proportionality using VI.14, (2) establish equal heights, (3) conclude equal solids via XI.31. The sole heath_only citation, XI.35 Porism, is used by Heath to show equal perpendiculars from elevated points to the base planes, but the AI achieves the same intermediate conclusion (equal heights) through a different construction strategy: by building both solids at the same vertex O with the same standing edge OB, both solids share the same base plane and opposite-base plane, making equal heights immediate. The underlying fact (equal heights) is present in both proofs at the same logical position, satisfying Case A condition (a). The eight ai_only items (1.29, 1.3, 1.31, 1.34, 11.10, 11.15, D5.6, P2) are all construction-level or elementary citations that Heath leaves implicit, representing over-citation of basic steps rather than a different proof path.

### 11.37
**Category**: Path difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification. For the forward direction, both proofs share the same backbone: they invoke XI.33 to establish that similar parallelepipeds have ratios triplicate of their corresponding edges, then infer proportionality of solids from proportionality of edges. However, for the converse direction the proofs diverge fundamentally. Heath treats the converse as an immediate consequence of the triplicate ratio relationship established by XI.33, directly inferring equal edge ratios from equal solid ratios in a single step. The AI instead introduces a substantially different constructive strategy: it constructs a fourth proportional using 6.12, builds an auxiliary similar solid using 11.27, applies the forward result to establish C:E, invokes 5.9 to prove equality of solids D and E, then uses proof by contradiction via 5.14 to establish equality of edges d and e. These key intermediate conclusions (fourth proportional construction, auxiliary solid, equality of solids, contradiction argument) are entirely absent from Heath's proof, constituting a genuinely different logical backbone for the converse direction. The AI's path is logically valid throughout, so the classification is D.

### 11.38
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof works through SAS congruence (I.4) of edge-midpoint triangles to establish DU=UE and then uses I.14 to show DUE is a straight line, followed by AAS congruence (I.26) of diagonal triangles to reach the bisection result. The AI proof takes a fundamentally different route: it constructs a diagonal parallelogram ACC'A', applies the converse of VI.2 (the midline/proportional-division theorem from Book 6) to establish collinearity of the midpoints on each face, identifies the common section of the cutting planes as the line XY, proves X, T, Y collinear via VI.2 applied within the diagonal parallelogram, and finishes with I.26 triangle congruence. Heath never invokes Book 6 proportionality; the AI never uses SAS (I.4) or the supplementary-angle straight-line test (I.14). The key intermediate conclusions differ: Heath's pivot is the SAS-based edge bisection and I.14-based collinearity, while the AI's pivot is proportionality-based collinearity via 6.2. This constitutes a different logical backbone (Q2 Case B). Under Q3 the AI's path is logically complete and valid, yielding classification D.

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: complete the two prisms to parallelepipeds, show the parallelepipedal bases are equal (each being double the given triangle, via I.34), apply XI.31 to conclude the parallelepipeds are equal, apply XI.28 to note each prism is half its parallelepiped, and conclude the prisms are equal. The AI proof cites the same three core propositions as Heath (1.34, 11.28, 11.31) but adds ten further citations that are either construction details (1.31, 1.33, P1, 11.9, 11.15), definitions (D11.13, D5.5, D6.4), a common notion (CN1), or a ratio-theory result (5.9) used to justify the final step that halves of equals are equal, which Heath treats as immediate. Since heath_only is empty and all ai_only items represent finer-grained citation of the same logical steps, this is Case A of Q2: same backbone, different citation depth.
