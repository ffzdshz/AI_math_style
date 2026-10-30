# Book 11 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 1 | 11.15 |
| Granularity difference (G) | 26 | 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.9, 11.10, 11.11, 11.12, 11.13, 11.14, 11.16, 11.17, 11.20, 11.21, 11.22, 11.24, 11.25, 11.26, 11.27, 11.28, 11.29, 11.30, 11.34, 11.39 |
| Path difference (D) | 11 | 11.7, 11.18, 11.19, 11.23, 11.31, 11.32, 11.33, 11.35, 11.36, 11.37, 11.38 |
| AI proof error (E) | 1 | 11.8 |

**Total**: 39 propositions

## Error Details

| Proposition | Error type | Details |
|---|---|---|
| 11.8 | Invalid inference | CANDIDATE E — 11.8   violated_claim : "angle ADB equals angle DBC" derived from 1.29 in Step 4, used as basis for AAS congruence in Step 5 to conclude AB = CD   failure_mode   : invalid_inference   mi |

## Per-Proposition Analysis

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Both proofs follow the same reductio ad absurdum backbone: assume part AB of line ABC is in the reference plane and part BC in an elevated plane, construct BD as the continuation of AB in the reference plane so that ABC and ABD share the common segment AB, and derive a contradiction from the impossibility of two distinct straight lines sharing a common segment. The key intermediate conclusion (common segment of two straight lines) is identical in both proofs. Heath's proof is extremely terse, citing no formal propositions at all and appealing briefly to a circle argument for the impossibility. The AI proof provides an elaborate, explicitly-cited triangle-congruence argument (using 1.10, 1.13, 1.3, 1.4, CN3, CN4, D1.4, D1.7, P1, P2) to demonstrate the same impossibility. Since the backbones match and the difference lies entirely in citation depth and explicitness (heath_only is empty, all ai_only items are over-citations providing explicit justification where Heath provides none), Q2 Case A applies, yielding Granularity difference (G).

### 11.2
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct a triangle from parts of the two intersecting lines, use Proposition 11.1 to conclude that the full lines lie in the plane of that triangle, and then extend the argument to show every triangle lies in one plane. The AI's approach is slightly more direct (asserting the triangle lies in some plane and then applying 11.1) compared to Heath's reductio (assuming the triangle is partly in one plane and partly in another), but the key intermediate conclusions are the same. The ai_only citations (D1.19, D1.7, P1) are all definitions and a postulate that Heath uses implicitly without explicit citation, representing a citation-depth difference rather than a structural divergence. With heath_only empty, the AI captures all of Heath's substantive reasoning. This is Case A of Q2: same backbone, different citation depth.

### 11.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Both proofs share the same logical backbone: assume the common section DB is not straight, draw straight lines DEB in plane AB and DFB in plane BC, observe that two straight lines with the same endpoints would enclose a space (which is impossible), and conclude DB must be straight. The AI proof adds explicit citations (P1 for drawing straight lines, D1.7 for the definition of plane surfaces, and 11.1 for additional rigor about straight lines lying in planes) that Heath leaves entirely implicit. Heath cites no propositions at all, treating the argument as self-evident from basic axioms. The ai_only set consists of a postulate, a definition, and one substantive proposition (11.1) used for supplementary justification in the AI's expanded restatement, but the core contradiction argument is identical in both proofs. Q2 Case A applies: same backbone, different citation depth, yielding classification G.

### 11.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish equal segments on either side of E, prove congruent triangles to derive FA=FB, FC=FD, then build up to FG=FH via angle equalities, and finally show angle GEF = angle HEF are right angles using I.8, concluding EF is perpendicular to the plane via XI. Def. 3. The key difference is that Heath uses I.26 (ASA) to derive GE=EH and AG=BH from previously established angle equalities, while the AI constructs GE=EH directly using I.3 and then proves GA=HB via I.4 (SAS), bypassing the need for I.26. The AI also over-cites foundational items (I.3 for construction, 11.2 for coplanarity, D1.10 for the right angle definition, P1 for joining lines, P4 for right angle equality) that Heath leaves implicit. Despite these citation-depth differences, both proofs reach the same key intermediate conclusions (equal corresponding segments, FA=FB, FC=FD, FG=FH, and right angles at E), making this a granularity difference rather than a path difference.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs follow the same logical backbone: a proof by contradiction assuming one of the three lines is not in the plane of the other two, constructing an intersection line BF via 11.3, establishing AB perpendicular to the plane via 11.4, deriving that angle ABF is right via D11.3, and reaching a contradiction because two distinct lines from B would each make right angles with AB. The AI proof is more explicit in its foundational citations, invoking 11.2 to establish coplanarity of pairs of lines, P4 for equality of right angles, and CN5 for the whole-part axiom, all of which Heath takes as understood without explicit citation. Since heath_only is empty and all ai_only items (11.2, P4, CN5) are foundational or axiomatic citations that merely make explicit what Heath leaves implicit, this is a citation-depth difference with the same backbone, satisfying Case A of Q2.

### 11.6
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification as G. Both proofs share the same key intermediate conclusions: (1) angles ABD and CDB are right by D11.3, (2) construction of DE perpendicular to BD and equal to AB, (3) BE equals AD, (4) angle ADE is right, (5) XI.5 yields coplanarity of BD, DA, DC, and (6) I.28 gives parallelism. The difference lies in the tools used to reach conclusions (3) and (4): Heath uses triangle congruence (I.4 for SAS to get AD=BE, then I.8 for SSS to get angle ABE = angle EDA), while the AI uses the Pythagorean theorem (I.47 to compute squares and show BE=AD, then I.48 converse to show angle ADE is right). Since I.4 appears inside Heath's proof of I.47 and I.8 appears inside Heath's proof of I.48, and the backbone conclusions are identical at each logical position, this is a citation-depth difference. The remaining ai_only items (1.11, 1.3, P1, P4, CN1, CN2) are construction axioms and common notions representing over-citation. The heath_only item 11.2 (every triangle is in one plane) is handled informally in the AI's Step 14 without citation. Same backbone, different granularity.

### 11.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined that the two proofs have different backbones, leading to classification at Q3. Heath's proof assumes the joining line EGF lies in a more elevated plane, then uses 11.3 to show the plane through EGF intersects the reference plane in a straight line EF, producing two distinct straight lines enclosing an area (impossible). The AI proof instead establishes via D1.23 that parallel lines lie in the same plane P, deduces that points E and F are in P, and then applies 11.1 directly to reach a contradiction: if any part of EF were not in P, part of a straight line would be in the reference plane and part elevated, which 11.1 forbids. These are genuinely different contradiction mechanisms (11.3 plus the two-lines-enclosing-area impossibility vs. 11.1 directly), constituting different key intermediate conclusions. The AI's path is logically complete and valid under the Q3 assessment, so the classification is D.

### 11.8
**Category**: AI proof error
**Jaccard**: 0.250
**Analysis**: The AI proof contains an invalid inference in Step 4 where it claims 'apply 1.29 to obtain that the alternate angles angle ADB and angle DBC are also equal.' Proposition 1.29, applied to parallel lines AB and CD with transversal BD, yields the alternate interior angles ABD = BDC (which the AI correctly used in Step 3), but does NOT yield angle ADB = angle DBC. The angles ADB and DBC are not formed at the intersection of the transversal with the parallel lines and thus are not alternate angles under 1.29. This invalid angle equality is then used in Step 5 via AAS (1.26) to conclude AB = CD, a result that is not generally true for parallel lines one of which is perpendicular to a plane. The false conclusion AB = CD propagates through Steps 6, 9, 10, and 12, undermining the SSS congruence argument in Step 12 that establishes angle CDE is right. Without this, the proof fails to show CD is perpendicular to a second line DE in the plane, which is essential for the application of 11.4 in Step 14. Heath's proof avoids this issue entirely by constructing an auxiliary point E with DE = AB rather than attempting to prove AB = CD.
**Audit Record**: CANDIDATE E — 11.8
  violated_claim : "angle ADB equals angle DBC" derived from 1.29 in Step 4, used as basis for AAS congruence in Step 5 to conclude AB = CD
  failure_mode   : invalid_inference
  missing_is     : support — the angle equality has no valid justification; 1.29 does not yield this result for the given configuration
  evidence       : Step 4 states "apply 1.29 to obtain that the alternate angles angle ADB and angle DBC are also equal" — 1.29 applied to parallels AB||CD with transversal BD yields angle ABD = angle BDC (already used in Step 3), not angle ADB = angle DBC. The latter angles are not alternate interior angles formed at intersection points of the transversal with the parallel lines.
  why_not_terse  : The AI explicitly cites 1.29 as justification for a specific angle equality that 1.29 cannot produce for this configuration. This is not abbreviated reasoning but a misapplication of the cited proposition. The false conclusion AB = CD that follows is essential to the SSS argument in Steps 12-13 and cannot be independently verified.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct perpendiculars GH and GK to EF in the respective planes, apply XI.4 to show EF is perpendicular to the plane through GH and GK, apply XI.8 twice to show AB and CD are also perpendicular to that plane, then apply XI.6 to conclude AB is parallel to CD. The AI adds explicit citations of I.11 (for drawing perpendiculars) and I.29 (for reasoning about angles formed by a transversal cutting parallel lines) which Heath leaves implicit. Since heath_only is empty and ai_only contains only lower-level construction and parallel-line propositions that provide additional detail for steps Heath takes as given, this is a clear Case A granularity difference with the AI over-citing at a finer level of detail.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: cutting off equal segments on the four rays, showing AD is equal and parallel to BE (I.33), CF is equal and parallel to BE (I.33), concluding AD is parallel to CF (XI.9) and AD equals CF, then AC is equal and parallel to DF (I.33), and finally applying SSS (I.8) to conclude angle ABC equals angle DEF. The AI's additional citations (1.3 for cutting off equal segments, P1 for joining lines, 11.7 for coplanarity justification when applying I.33 in 3D, and CN1 for transitivity of equality) are all construction-level, postulate-level, or common-notion-level over-citations that make explicit what Heath leaves implicit. Heath cites nothing that the AI omits (heath_only is empty). Since the key intermediate conclusions are the same and only the citation depth differs, this is a granularity difference.

### 11.11
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: (1) construct perpendiculars and a parallel line, (2) use XI.4 to show BC is perpendicular to the plane through DA and DE, (3) use XI.8 to transfer that perpendicularity to GH via parallelism, (4) use XI.Def.3 to conclude GH is perpendicular to FA, and (5) use XI.4 again to conclude FA is perpendicular to the given plane. The only citation difference is that the AI additionally cites Postulate 1 (P1) in its setup step for drawing line BC in the plane, which Heath does not explicitly cite. Since P1 is a basic postulate (construction axiom) and the proofs share the same backbone with the same key intermediate conclusions, this is a granularity difference in citation depth, not a path difference.

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: conceive an elevated point B, drop BC perpendicular to the plane via 11.11, draw AD through A parallel to BC via 1.31, then conclude AD is perpendicular to the plane via 11.8. The only citation difference is the AI's explicit reference to D11.3 (the definition of a line perpendicular to a plane) in its closing statement, which Heath leaves implicit. Since ai_only contains only a definition and heath_only is empty, this is a straightforward over-citation representing a citation-depth difference. The backbone is the same, so Case A of Q2 holds, yielding G. The citation sets are not identical (ai_used includes D11.3 while heath_refs does not), so P is ruled out.

### 11.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs argue by contradiction from the same assumption: that two lines AB and AC are at right angles to a reference plane from the same point A on the same side. Both establish the same key intermediate conclusions: (1) the lines and their intersection with the reference plane lie in one plane, (2) the common section DAE is a straight line (by 11.3), (3) angles BAE and CAE are both right angles (by D11.3), and (4) this leads to a contradiction since one angle is a proper part of the other yet both are right angles. The AI proof adds explicit citations for 11.2 (coplanarity of two intersecting lines), 1.13 (supplementary angles on a straight line), CN5 (whole is greater than the part), and P4 (all right angles are equal), which are all steps Heath leaves implicit when he simply states 'which is impossible.' The heath_only set is empty, confirming that Heath uses no citation the AI does not also use. Since the backbone of key conclusions is identical and the differences are purely in citation depth, this is a granularity difference.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume the two planes are not parallel, derive a common section line via 11.3, take a point on that line and join it to the endpoints of the perpendicular AB, show both resulting angles are right angles via D11.3, form a triangle in which two angles sum to two right angles, and reach a contradiction with 1.17, concluding the planes are parallel by D11.8. The AI proof is essentially the same argument with different labels and explicit citation of foundational items (P1 for joining points, P4 for right angles being equal, CN2 for adding angles) that Heath uses implicitly. Since heath_only is empty and ai_only contains only postulates and a common notion, this is Case A of Q2: same backbone, different citation depth, yielding a Granularity difference.

### 11.15
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of 11.15 follows the identical logical backbone as Heath's proof: constructing BG perpendicular to the plane through DE, EF (11.11), drawing GH parallel to ED and GK parallel to EF (1.31), establishing that BG is at right angles to both GH and GK via D11.3, showing BA parallel to GH and BC parallel to GK via 11.9, deducing that angles GBA and GBC are right via 1.29, concluding BG is perpendicular to the plane through BA, BC via 11.4, and finally applying 11.14 to conclude the planes are parallel. The citation sets are identical (Jaccard = 1.0) with ai_only and heath_only both empty, and all key intermediate conclusions match in substance and order, satisfying the perfect match check.

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: a proof by contradiction showing that if the common sections EF and GH of two parallel planes met at a point K, then K would lie in both planes, contradicting their parallelism. The key intermediate conclusions (K in plane AB, K in plane CD, contradiction with parallel hypothesis, therefore lines are parallel) are identical in both proofs. The citation differences are all matters of depth: the AI explicitly cites 11.3 (common sections are straight lines) and D11.8 (definition of parallel planes) where Heath leaves these implicit, while Heath cites 11.1 to justify that K lies in plane AB whereas the AI achieves the same conclusion directly from the definition of common section. These are citation-depth differences around the same backbone, satisfying Case A of Q2.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct the diagonal AD meeting the middle plane at a point (O in Heath, G in the AI), use 11.16 twice to establish parallel lines in the two triangles ABD and ACD, apply 6.2 twice to obtain proportions, and chain the results via 5.11. The AI's three extra citations (5.7, D11.8, P1) are all over-citations reflecting greater explicitness rather than a different proof path. The AI applies 6.2 to triangle ACD measuring from D rather than A, yielding DG:GA = DF:FC instead of Heath's direct AO:OD = CF:FD, which requires an additional inversion step via 5.7.Corollary. D11.8 (definition of parallel planes) and P1 (postulate for joining lines) are both implicit in Heath's proof. Since heath_only is empty and the ai_only items are all construction-level, definitional, or depth-level citations, the proofs share the same backbone at different citation depths.

### 11.18
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 reveals different backbones: Heath constructs an auxiliary point F on the common section CE and draws FG perpendicular to CE in the plane DE, then proves AB is parallel to FG (via I.28 using two right angles) and transfers perpendicularity to FG via XI.8, finally applying D11.4 to FG. The AI takes a more direct path by observing that AB itself lies in plane Q, is perpendicular to the common section CE (by D11.3), and is perpendicular to plane P (given), so D11.4 applies directly to AB without needing an auxiliary construction. This eliminates the need for I.11, I.28, and XI.8 entirely. The AI adds 11.3 (common section of two planes is a straight line) which Heath uses implicitly. Since the key intermediate conclusions differ -- Heath's proof pivots on the parallelism of AB and FG and the transfer of perpendicularity via XI.8, while the AI's proof has neither -- this is a genuine path difference. The AI's path is logically valid under Q3.

### 11.19
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Heath proves 11.19 by contradiction: assuming the common section BD is not perpendicular to the reference plane, he draws lines DE and DF in the respective planes perpendicular to their common sections with the reference plane, shows both are perpendicular to the reference plane by D11.4, and derives a contradiction via 11.13 (two perpendiculars from the same point). The AI instead uses a direct constructive proof: it erects a perpendicular EK to the reference plane at the intersection point (11.12), then shows via D11.4 and 11.13 that EK must lie in both plane AB and plane CD, and therefore must coincide with their common section EF (by 11.3). These are fundamentally different logical backbones -- indirect versus direct -- with different key intermediate conclusions, so this is a genuine path difference. The AI's direct proof is logically complete, with every step properly supported by cited propositions and definitions.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: (1) construct angle BAE equal to DAB and AE equal to AD in the plane of BAC, (2) use I.4 to establish BD = BE, (3) use the triangle inequality I.20 to derive DC > EC, (4) apply I.25 to conclude angle DAC > angle EAC, and (5) combine DAB = BAE with DAC > EAC to reach DAB + DAC > BAC. The AI proof establishes every key intermediate conclusion that Heath's proof does, in the same logical order. The citation difference is entirely on the AI side: ai_only contains 1.23 (angle construction), 1.3 (cutting off equal segments), CN2 (addition), CN3 (subtraction), and P1 (drawing a line), all of which are construction propositions, common notions, or postulates that Heath leaves implicit. Heath_only is empty, confirming that Heath's citations are a proper subset of the AI's. This is a clear Case A: same backbone with the AI citing at finer granularity.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) apply XI.20 at each base vertex to show the two face-triangle base angles exceed the corresponding base polygon angle, (2) sum these inequalities to show total base angles exceed the base polygon angle sum which equals (n-2) times two right angles by I.32, (3) observe total face-triangle angles equal n times two right angles by I.32, and (4) subtract to conclude the vertex angles at A sum to less than four right angles. The AI generalizes from Heath's trihedral case to an arbitrary n-faced solid angle, but the key intermediate conclusions and logical structure are identical. The ai_only set consists entirely of common notions (CN2, CN5), a definition (D11.11), and a postulate (P1), all of which Heath leaves implicit. The heath_only set is empty. This is a pure citation-depth difference with the same backbone, yielding G.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they handle the trivial case where all three angles are equal, then for the unequal case, construct an auxiliary angle equal to one of the given angles at a vertex, use I.4 to establish a base equality, use I.24 to establish a base inequality, and combine with the triangle inequality to show all three triangle inequality conditions hold. Heath's proof is concise, citing only I.4 and I.24 while leaving construction steps and common notions implicit. The AI proof makes all sub-steps explicit, adding citations for the construction (1.23, P1, P3), isosceles triangle properties (1.5), the triangle inequality (1.20), the final construction theorem (1.22), and common notions (CN2, CN3, CN5). Since heath_only is empty and all ai_only items are explicit sub-citations of steps Heath performs implicitly, this is Case A of Q2: same backbone, different citation depth.

### 11.23
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Both proofs share the same overall structure: construct triangle LMN from equal-arm chords, circumscribe a circle with center O, establish that AB > LO, erect a perpendicular OR at O with OR squared equal to AB squared minus OL squared, show RL = RM = RN = AB via the Pythagorean theorem, and conclude by I.8 that the angles at R equal the given angles. The key divergence is in how the critical inequality AB > LO is established in the AB < LO contradiction case. Heath constructs auxiliary points P and Q on the radii with OP = AB, uses VI.2 to show LM is parallel to PQ, then I.29, VI.4, and V.16 to establish LM > PQ, and finally I.25 to conclude angle ABC > angle POQ. The AI instead directly applies I.24/I.25 (the hinge theorems): if OL >= AB, then with equal bases LM = AC and equal side pairs, I.25 gives angle LOM <= angle ABC for each pair, so the angles at O sum to at most the sum of the given angles, contradicting the fact that angles around O sum to four right angles while the given angles sum to less. This is a substantively different and valid method for the same sub-conclusion, using triangle inequality results directly rather than proportion theory. The heath_only citations (1.29, 5.16, 6.2, 6.4) all belong to Heath's proportion-based sub-argument and are not contained in the proof tree of any AI-cited proposition, confirming a genuine path difference. Q2 Case A fails because these substantive facts are argued in Heath but absent from the AI proof. Q3 confirms the AI's path is valid, yielding classification D.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone: (1) establish parallelism of opposite edges via XI.16, (2) conclude each face is a parallelogram, (3) prove equal angles on corresponding edges of opposite faces via XI.10, (4) establish equal corresponding sides via I.34, (5) prove congruent triangles via I.4, and (6) conclude opposite faces are equal since each parallelogram is double its congruent triangle via I.34. The AI's two extra citations (1.33 and CN1) are citation-depth differences: the AI explicitly cites 1.33 to justify that quadrilaterals with two pairs of parallel sides are parallelograms, a step Heath performs implicitly from the definition, and CN1 to make explicit the equality inference in the doubling argument. Heath's citation set is a proper subset of the AI's, and heath_only is empty. The key intermediate conclusions are identical in both proofs, making this a clear Case A granularity difference.

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same backbone: construct equimultiples of the bases by extending edges and completing parallelepipeds, use 11.24 to show the component parallelepipeds are equal, establish that the equimultiple of the base corresponds to the equimultiple of the solid, then apply D5.5 (the equimultiple definition of proportion) to conclude the ratio. The AI's additional citations (1.35, 1.36, 11.16) are all lower-level results that support the same logical steps: 11.16 appears inside Heath's proof of 11.24 (confirmed by inspection), making its citation a depth difference; 1.35 and 1.36 provide explicit justification for comparing parallelepipeds by their bases, which Heath handles implicitly. With heath_only empty and ai_only consisting entirely of sub-results underlying the same argument, this is Case A of Q2: same backbone, different citation depth.

### 11.26
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: dropping a perpendicular from an elevated point to the plane of the solid angle, constructing equal angles and segments at the new vertex, applying SAS congruence (I.4) three times to establish corresponding triangle sides are equal, and then applying SSS congruence (I.8) to establish the face angles are equal. The AI proof is a strict superset of Heath's citations (heath_only is empty). The ai_only items fall into three categories: (1) over-citation of construction steps, axioms, and definitions (1.3, P1, CN1, D11.11); (2) use of the Pythagorean theorem (1.47) as an alternative technique to establish a length equality that Heath derives directly from I.4; and (3) an additional verification step using 11.20, 11.21, and 11.23 to explicitly justify that the three constructed plane angles can form a solid angle, where Heath simply concludes directly. These represent differences in citation depth and explicitness, not differences in the logical backbone.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a solid angle at A equal to the solid angle at C, set up proportional edges using VI.12, derive that corresponding face parallelograms are similar (using proportional sides about equal angles), complete the solid, and conclude similarity via XI.Def.9. The AI proof cites 12 additional propositions beyond Heath's three references (5.22, 6.12, D11.9), but all of these are sub-results supporting the same key intermediate conclusions at finer granularity: 11.26 for constructing the solid angle, 11.20 and 11.21 for verifying its conditions, 6.6 and D6.1 for parallelogram similarity, 5.11, 5.16 for proportion manipulation, 11.24 and 1.34 for opposite faces, P1 and 1.31 for construction steps, and D11.11 for the definition of a solid angle. Heath's proof subsumes these steps implicitly. Since heath_only is empty and all ai_only items represent deeper citation of the same logical steps, this is Case A of Q2: same backbone, different citation depth.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) the diagonals of the opposite faces create equal triangles that form the triangular faces of two prisms, (2) the remaining faces are equal parallelograms (opposite faces of the parallelepiped plus the shared cutting plane), and (3) the two prisms are therefore equal solids by Def. 11.10 since they are contained by planes equal in multitude and magnitude. The AI proof is substantially more detailed, explicitly establishing that the cutting plane forms a parallelogram (via 1.33 and 11.9), identifying the solids as prisms (D11.13), proving triangle congruence via SSS (1.8), and citing 11.24 for the equality of opposite faces, whereas Heath handles these same logical steps more concisely. All six ai_only citations (1.33, 1.8, 11.24, 11.9, CN1, D11.13) represent deeper-level justifications for steps that Heath takes as evident or handles more tersely, and heath_only is empty, confirming this is a citation-depth difference rather than a path difference.

### 11.29
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Both proofs share the same fundamental backbone: decompose each parallelepiped into a common solid plus a triangular prism on the side, show the two side prisms are equal, then add the common solid to conclude the two parallelepipeds are equal. The differences lie in the supporting details. Heath establishes the prism equality by showing individual component equalities using I.4 (SAS congruence) and I.36 (parallelograms on equal bases in same parallels), while the AI establishes it by explicitly citing 11.24 (opposite faces of parallelepipeds are parallelogrammic), 11.6 (lines perpendicular to same plane are parallel), 1.33 (lines joining equal parallel lines are equal and parallel), and CN2 (equals added to equals). The AI uses I.8 (SSS) alone for triangle congruence where Heath uses both I.8 and I.4. The heath_only items (1.36 and 1.4) represent steps that the AI handles through alternative but equivalent supporting propositions rather than a fundamentally different logical path. Q2 Case A applies: same backbone, different citation depth, yielding G.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct an auxiliary parallelepiped CP, show CM equals CP by 11.29, show CN equals CP by 11.29, and conclude CM equals CN by transitivity. The AI proof explicitly cites CN1 for the transitivity step and P2 for the production of line segments, whereas Heath uses these implicitly without citation. Since heath_only is empty and the ai_only items (CN1, P2) are a common notion and a postulate representing over-citation of steps Heath leaves implicit, this is a same-backbone, different-citation-depth scenario, yielding Granularity difference (G).

### 11.31
**Category**: Path difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Heath's proof uses a ratio-based argument: constructing an auxiliary solid XU equal to AE, then using XI.25 (cutting by parallel plane) twice to set up ratios, followed by V.7, V.11, and V.9 to conclude CF equals YX equals AE. The AI instead takes a direct construction approach: building an auxiliary parallelepiped AB' on the same base as AB but with CD's standing edges, showing AB equals AB' via 11.29/11.30, then arguing that AB' and CD with complementary pieces form the same larger solid, using CN2/CN3 to conclude AB' equals CD. These are genuinely different key intermediate conclusions — Heath argues through proportions and parallel-plane sections while the AI argues through complementary solid pieces and common notions. Both proofs handle the oblique-edge case: Heath drops perpendiculars and applies Case 1 via XI.30, while the AI repositions the base using I.42/I.44/I.45. The AI's chain is logically complete under the hardened standard, making this a valid different path (D) rather than an error.

### 11.32
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary parallelogram FH equal to AE on the line FG (using I.45), completes a parallelepiped GK on it with the same height as CD, establishes AB = GK by XI.31, then cuts solid CK by a plane to obtain the proportion directly via XI.25. The AI instead uses the Eudoxean equimultiple definition of proportion (D5.5): it takes arbitrary multiples m and n of the bases and corresponding solids, shows (via XI.25 and XI.31) that the ordering of m-fold vs n-fold multiples of the bases matches the ordering of the corresponding multiples of the solids, and concludes the proportion by D5.5. These are fundamentally different proof strategies with different key intermediate conclusions — Heath's key step is constructing an equal auxiliary solid adjacent to CD, while the AI's key steps are verifying the equimultiple ordering condition. The AI's path is logically valid, yielding classification D.

### 11.33
**Category**: Path difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Heath's proof constructs a copy of CD (solid KP) within the same diagram and establishes a continued proportion of four solids (AB, EO, QL, KP) using VI.1 for parallelogram ratios and XI.32 to convert to solid ratios, then applies V.Def.10 directly for the triplicate ratio. The AI proof takes a structurally different approach: it constructs an auxiliary solid AO similar to CD on edge AE (via 11.27), then decomposes the volume ratio dimension by dimension using intermediate parallelepipeds Q1, Q2, Q3 that each differ by one edge. Each dimensional ratio equals AE:CF (established via 11.25, 11.32, and 6.1), and these are combined by ex aequali (5.22) to yield the triplicate ratio (D5.10). The backbones differ: Heath uses a four-term continued proportion of solids, while the AI uses a three-step dimensional decomposition. Both paths are logically complete, so the classification is D.

### 11.34
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided this as Granularity (G). Both proofs share the same logical backbone: constructing an auxiliary parallelepiped on the base of one given solid with the height of the other, then using XI.32 (same-height solids are as their bases) and XI.25 (same-base solids are as their heights) to establish the ratio chain, and finally applying V.7 (inversion) and V.9 (equal ratios to the same imply equality) to complete both the forward and converse directions. The differences are in case structure and citation depth: Heath splits into sub-cases (equal bases using XI.31, unequal bases with the auxiliary construction) and separately handles the oblique case by reducing to right-angled solids via XI.29/XI.30, while the AI works directly with general parallelepipeds in a single general argument. Heath also uses VI.1 to convert base ratios to segment ratios, which the AI compresses. The AI explicitly cites V.11 (transitivity of ratios) where Heath chains ratios implicitly. These are all granularity-level differences around a shared backbone, not different proof paths.

### 11.35
**Category**: Path difference
**Jaccard**: 0.267
**Analysis**: Q2 decides the classification. Heath's proof constructs a point H on the elevated line AG with AH equal to DM, draws HK parallel to GL to get HK perpendicular to the plane (via 11.8), then establishes right angles at C and F using the converse Pythagorean theorem (1.48), and works through a chain of triangle congruences involving perpendiculars from B and E to the sides AC and DF. The AI proof instead drops perpendiculars from G directly to the sides AB and AC (via 1.12), uses 11.4 to establish that the perpendicular foot projections are perpendicular to the sides, and then argues through a uniqueness-of-configuration approach (Steps 44-47) that the perpendicular feet H and N must correspond in congruent configurations, ultimately concluding via 1.8. The AI never uses 1.48 or 11.8, and Heath never uses 11.4 or 11.11, reflecting genuinely different geometric strategies. The proof-tree containment test confirms that heath_only propositions 1.48 and 11.8 are not subsumed by any AI-cited higher-level result. Under Q3, the AI's different path is logically complete under the hardened 1(b) standard, as its chain from premises to conclusion is sound, despite being verbose and circuitous.

### 11.36
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 identified different logical backbones, and Q3 confirmed the AI's alternative path is valid, yielding classification D. Heath's proof establishes base equality via reciprocal proportionality of sides about equal angles (6.14) and height equality via the perpendicular result (11.35 Porism), then applies 11.31. The AI takes a fundamentally different route: it observes both solids share the same height B by construction, uses 11.32 to reduce the problem to comparing base ratios, then uses 6.1 to express the base ratio as a ratio of rectangles on the sides, and finally uses 6.16 to show A times C equals B squared, establishing base equality and concluding via 11.31. The only shared citation is 11.31; all other citations differ and come from independent mathematical domains (reciprocal proportionality and perpendicular geometry vs. ratio of solids and rectangle arithmetic). The AI's chain is logically complete and sound, constituting a valid different path.

### 11.37
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: The forward direction of both proofs shares the same backbone: using XI.33 to establish that the ratio of similar parallelepipedal solids is the triplicate ratio of their corresponding sides, and then concluding proportionality from the given proportionality of the sides. However, the converse directions diverge significantly. Heath's converse simply reverses the triplicate ratio argument directly, while the AI constructs a fourth proportional E (using 6.12), builds a new similar solid SE on E (using 11.27), applies the forward direction to obtain SA:SB = SE:SD, then deduces SE = SC (using 5.9 and 5.11), and finally proves E = C by contradiction (using 11.33 and 5.8). This construction-and-contradiction approach for the converse constitutes a genuinely different logical backbone from Heath's direct argument, making this a path difference (D). The AI's path is logically complete and valid throughout.

### 11.38
**Category**: Path difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification. Heath's proof works through triangle congruence: it joins specific segments (DU, UE, BS, SG), uses SAS (I.4) to prove triangle congruence and derive that DUE is a straight line (I.14), shows DE parallel to BG via XI.9 and I.33, then applies vertical angles (I.15) and AAS congruence (I.26) to prove triangles DTU and GTS are congruent, yielding DT = TG and UT = TS. The AI proof takes an entirely different geometric route: it establishes that the midpoint-connecting planes form two parallelograms (KOMQ and LPRN), identifies their common section as the line connecting the centers of opposite faces, constructs parallelogram ACGE from face diagonals, and then uses the property that parallelogram diagonals bisect each other (I.34) together with proportionality (6.2) to show the cube diagonal and the common section meet at their mutual midpoint. The key intermediate conclusions differ fundamentally -- Heath relies on triangle congruence (I.4, I.26) and angle results (I.14, I.15), while the AI relies on parallelogram properties (I.34) and proportional cutting (6.2). This constitutes a genuine path difference with a valid alternative logical chain.

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) show the base parallelograms are equal using I.34, (2) conclude the completed parallelepipeds are equal via XI.31, (3) show each prism is half its parallelepiped via XI.28, and (4) conclude the prisms are equal. The AI proof explicitly cites CN1 (equals to the same thing are equal) and CN3 (halves of equals are equal) where Heath leaves these common-notion steps implicit. Since heath_only is empty and ai_only contains only common notions (CN1, CN3), the proofs share identical key intermediate conclusions but differ in citation depth, making this a clear Case A granularity difference.
