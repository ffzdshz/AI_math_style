# Book 3 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 30 | 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.10, 3.11, 3.12, 3.14, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23, 3.25, 3.27, 3.28, 3.29, 3.30, 3.32, 3.33, 3.34, 3.35, 3.36, 3.37 |
| Path difference (D) | 6 | 3.9, 3.13, 3.15, 3.16, 3.24, 3.31 |
| AI proof error (E) | 1 | 3.26 |

**Total**: 37 propositions

## Error Details

| Proposition | Error type | Details |
|---|---|---|
| 3.26 | Unsupported assertion | CANDIDATE E — 3.26   violated_claim : "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF" (Step 6)   failure_mode   : unsupported_assertion  |

## Per-Proposition Analysis

### 3.1
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs follow the same reductio ad absurdum backbone: construct chord AB, bisect at D, draw perpendicular CE through D, bisect CE at F, then assume some other point G is the centre, use SSS congruence (I.8) to show the angle at D must be right, and derive a contradiction with the constructed right angle. The AI proof establishes every key intermediate conclusion that Heath's proof does, in the same logical order. The ai_only set consists entirely of over-citations: construction propositions (1.10 for bisection, 1.11 for perpendicular), postulates (P1 for joining lines, P2 for producing lines), a definition (D1.15 for the radius property), a common notion (CN5 for the whole-greater-than-part contradiction), and P4 (all right angles are equal) -- all of which Heath uses implicitly without explicit citation. The heath_only set is empty, confirming that the AI covers all of Heath's cited references. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions in the same logical order: finding center D, establishing DA=DB as radii, showing angle DAE equals angle DBE via I.5, using the exterior angle theorem I.16 to show angle DEB is greater than angle DAE, combining these to get angle DEB greater than angle DBE, and then applying I.19 to conclude DB is greater than DE. The only structural difference is that Heath uses a reductio ad absurdum framing while the AI uses a direct proof, but the geometric backbone is identical. The ai_only items (D1.15 and P1) are a definition and a postulate representing over-citation of foundational items, which is a classic granularity indicator. The heath_only set is empty, confirming no substantive citations are missing from the AI proof.

### 3.3
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs establish the same two-direction biconditional through identical key intermediate conclusions: Direction 1 uses SSS congruence (I.8) on triangles EFA and EFB to show angles EFA and EFB are equal, then applies D1.10 to conclude right angles; Direction 2 uses the isosceles base angle theorem (I.5) to get equal angles EAF and EBF, then AAS congruence (I.26) to conclude AF equals FB. The logical backbone is the same in both proofs. The AI's three extra citations (3.1 for finding the centre, D1.15 for the circle definition justifying equal radii, and P1 for joining line segments) are all construction, definition, or postulate over-citations that Heath leaves implicit. Since heath_only is empty and the ai_only items reflect only citation depth differences rather than different logical paths, this is a granularity difference (G).

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume for contradiction that two non-diametral chords bisect each other at E, find the center F (3.1), join FE, conclude via 3.3 that angle FEA is right and angle FEB is right, then derive the contradiction that two unequal angles would be equal. The AI proof adds explicit citations for axiom-level steps that Heath leaves implicit: P1 for joining FE, P4 for the equality of right angles, and CN5 for the whole-greater-than-part principle. Since heath_only is empty and ai_only contains only postulates and common notions (P1, P4, CN5), this is a clear Case A: same backbone with different citation depth, yielding Granularity difference (G).

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume by contradiction that the two intersecting circles share a centre E, show that a radius to the intersection point C equals a radius to point F on one circle and also equals a radius to point G on the other circle, and conclude that EF = EG which is impossible since F and G lie at different distances from E. The AI proof makes explicit citations to foundational items (CN1, CN5, D1.16, P1, P2) that Heath uses implicitly without citing, while Heath cites only D1.15. The heath_only set is empty, confirming all of Heath's references are contained in the AI set. Since the key intermediate conclusions are identical and the citation differences consist entirely of axioms, definitions, and postulates that the AI over-cites, this is a granularity difference.

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Heath's proof uses a single proof by contradiction: assuming a common center F, it derives FC = FB (center of ABC) and FC = FE (center of CDE), yielding FE = FB which contradicts FE being less than FB. The AI's Case 1 reproduces this identical backbone with the same key intermediate conclusions. The AI adds a separate Case 2 for external tangency, but the core logical structure matches Heath. All citation differences (ai_only) consist entirely of definitions (D1.15, D1.16, D3.1, D3.2, D3.3), common notions (CN1, CN5), and postulates (P1, P2) which are foundational items Heath uses implicitly without citing. Heath has no explicit citations listed (heath_only is empty), so the entire symmetric difference reflects the AI's over-citation of axioms and definitions rather than any substantive path divergence. This is a classic Case A under Q2: same backbone, different citation depth.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Classification was decided at Q2 (Case A: same backbone, different citation depth). Both proofs establish the same key intermediate conclusions: (1) FA is greatest via the triangle inequality with radii equality, (2) FD is least via triangle inequality and subtraction, (3) nearer lines are greater via angle comparison at centre E and Proposition 1.24, and (4) exactly two equal lines via constructing an equal angle and SAS congruence. The AI's citation set is a strict superset of Heath's (heath_only is empty), with ai_only containing definitions (D1.15, D1.17), postulates (P1), common notions (CN2, CN3), supplementary angles (1.13), and SSS congruence (1.8). The definitions, postulates, and common notions are standard over-citations that Heath leaves implicit. Proposition 1.13 is cited by the AI to explicitly justify supplementary angles in the nearer-greater-than-remote argument, which Heath handles implicitly. Proposition 1.8 is used in the AI's uniqueness sub-argument (SSS to show angles equal, hence rays coincide) rather than Heath's approach of invoking the already-proved ordering result, but this is a minor methodological variation within the same logical backbone. All key conclusions align, making this a granularity difference.

### 3.8
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: DA is greatest on the concave circumference (via I.20 triangle inequality), the ordering DE > DF > DC on the concave side (via I.24 angle comparison), DG is least on the convex side (via I.20 remainder argument), the ordering DK < DL < DH on the convex side, exactly two equal lines from D via SAS congruence (I.4), and no others by reductio. The only substantive difference is that Heath uses I.21 (lines inside a triangle are less than the remaining sides) for the convex ordering step, while the AI uses I.24 (SAS inequality via angle comparison) for the same step, reaching the identical conclusion. Since the backbone of key conclusions is the same and only the justifying citation differs at one step, this is a granularity difference rather than a path difference. The AI's ai_only items (1.23, CN1, CN3, CN5, D1.15, D1.16, P1) are construction propositions, common notions, definitions, and postulates representing over-citation. Heath's 3.1 is a construction citation the AI omits by simply naming the center. The low Jaccard (0.25) reflects these citation-level differences, not backbone divergence.

### 3.9
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 3.9 directly by constructing perpendicular bisectors of two chords (AB and BC) through the point D, using I.8 to establish right angles, D1.10 for the definition of right angles, and III.1 to conclude the centre lies on each bisector, then noting D is their unique intersection. The AI instead proves the result by contradiction: assuming D is not the centre, it applies 3.7 (which limits a non-centre point on a diameter to at most two equal lines to the circle) to derive a contradiction with the hypothesis that three equal lines fall from D. These are fundamentally different logical backbones — direct construction via perpendicular bisectors versus indirect proof via contradiction using 3.7. The AI's path is valid: any interior point that is not the centre lies on a diameter (the one through it and the centre), so 3.7 applies. The Jaccard similarity of 0.0 reflects the completely disjoint citation sets, consistent with a genuine path difference.

### 3.10
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs use identical logical backbones: assume two circles cut at more than two points, show a single point is the center of both circles, then derive a contradiction via III.5. The difference is purely in citation depth. Heath re-derives the content of III.9 inline within the proof of 3.10, using perpendicular bisectors of chords (via III.1) to locate the center of each circle separately. The AI instead finds the center K of circle ABC via 3.1, observes KB = KG = KF (by D1.15), and then invokes 3.9 directly to conclude K is also the center of DEF. Heath's proof of 3.9 itself uses III.1 and the perpendicular bisector technique, confirming the proof-tree containment test: the AI cites 3.9 as a unit while Heath re-derives 3.9's internals inline. The ai_only items (3.9, D1.15, P1) reflect over-citation and higher-level abstraction, not a different logical path.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both the AI and Heath proofs use the same proof-by-contradiction strategy: assume the line joining centres F and G, when produced, does not pass through the point of contact A; form triangle FGA and apply the triangle inequality (1.20); use equal radii to derive a contradiction with the geometric containment of the internally tangent circles. The key intermediate conclusions are identical in both proofs. The AI proof is more explicit in its citations (1.20, 3.6, CN1, CN2, CN5, D1.15, P1, P2) while Heath's reference set is recorded as empty, making the Jaccard of 0.0 an artifact of missing reference annotations rather than a genuine divergence. Since the backbones match and the difference is only in citation depth and explicitness, this is a granularity difference.

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decides this classification as G (Granularity difference). Both proofs use the same proof-by-contradiction backbone: assume the line FG joining the centres does not pass through the contact point A, then show FG > FA + GA using radii properties and FG < FA + GA using the triangle inequality (I.20), reaching a contradiction. The AI proof makes the same key intermediate conclusions as Heath but over-cites foundational items: definitions D1.15, D1.16, D3.3, common notions CN1, CN2, and postulate P1 that Heath uses implicitly. The heath_only set is empty, confirming the AI covers everything Heath does. The ai_only set consists entirely of definitions, common notions, and a postulate, which are classic over-citation indicators. This is Case A of Q2: same backbone, different citation depth.

### 3.13
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Classification was decided at Q2/Q3. Both proofs cover the two required cases (internal and external tangency), but they argue through fundamentally different key intermediate conclusions in both cases. For the internal case, Heath uses radius inequalities (BG = GD implies BG > HD implies BH >> HD, contradicting BH = HD) while the AI uses algebraic reasoning from equal radii (GA = GB and HA = HB with both points on line GH) to deduce G = H (same center), contradicted by 3.6. For the external case, Heath joins the two contact points and uses 3.2 (chord falls within circle) and D3.3 (definition of touching) to reach a contradiction, while the AI uses 3.12 (line through centers passes through contact point) applied twice to show both points lie on segment GH at equal distance from a center, forcing A = B. These are genuinely different logical backbones, not mere citation-depth differences. The AI's alternative path is logically valid in both cases, yielding a sound proof by a different route.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions in the same logical order for both parts of this biconditional: (1) perpendiculars from the centre bisect the chords via III.3, (2) radii are equal, (3) the Pythagorean theorem I.47 yields equations relating the squares of the perpendicular distances and half-chords, (4) algebraic subtraction yields the desired equality. The citation differences are purely at the granularity level: the AI over-cites foundational items (CN1, CN2, CN3 for algebraic steps Heath leaves implicit, D1.15 for the definition of a circle to justify radii equality, and P1 for joining lines), while Heath cites 3.1 for finding the centre which the AI treats as given. None of these differences affect the logical backbone, which is the same in both proofs.

### 3.15
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification as D (Path difference). The two proofs establish the same proposition through fundamentally different key intermediate conclusions. For Part 1 (diameter is greatest), Heath constructs an auxiliary chord MN and uses 3.14 to show MN equals BC, then applies the triangle inequality (1.20) to triangle MEN; the AI instead directly forms a triangle from the center and chord endpoints and applies 1.20 without any auxiliary construction or use of 3.14. For Part 2 (nearer chord is greater), Heath uses angle comparison via 1.24 (unequal angles in triangles yield unequal bases); the AI uses the Pythagorean theorem (1.47) to compare squares of half-chord lengths derived from right triangles formed by perpendicular distances. These constitute genuinely different analytical paths -- Heath's method is synthetic-geometric (auxiliary construction, angle comparison) while the AI's method is more direct and metric (Pythagorean theorem, algebraic comparison of squares). Both paths are logically complete and valid, satisfying Q3.

### 3.16
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof of Part 1 (tangent falls outside the circle) uses I.5 to establish that in triangle DAC with DA = DC (radii), the base angles are equal, so since angle DAC is right, angle ACD is also right, yielding two right angles in a triangle (contradicting I.17). The AI instead argues that in triangle FAG with a right angle at A, by I.17 and I.19 the side FG opposite the right angle must be the greatest side, hence FG > FA, contradicting the assumption that G lies on or inside the circle. This constitutes a genuinely different logical backbone for Part 1: Heath's route goes through the isosceles-triangle theorem (I.5) while the AI's route goes through the angle-side inequality (I.19). Parts 2 and 3 share essentially the same backbone in both proofs. Since the AI's different path is logically valid and complete, the classification is D.

### 3.17
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone for constructing a tangent from an external point: construct a larger circle centered at the given circle's centre with radius equal to the distance to the external point, draw a perpendicular from a point on the given circle to the line joining the external point and centre, apply SAS congruence (1.4) to establish that the angle at the tangent point is right, then invoke 3.16 to conclude tangency. The ai_only citations (1.11, D1.15, P1, P3) are all construction postulates, definitions, and basic construction propositions that Heath omits as implicit, representing over-citation by the AI. The heath_only citation (3.1, finding the centre of a circle) reflects Heath's explicit use of this proposition where the AI simply names the centre directly as given data. The AI also adds a preliminary case where the point lies on the circumference, which is extra coverage rather than a backbone divergence. All differences are citation-depth matters, not structural path differences.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: assume FC is not perpendicular to DE, draw FG perpendicular to DE, show angle FGC is right so angle FCG is acute (I.17), conclude FC > FG (I.19), and derive a contradiction from the fact that FG is less than the radius. The divergence is purely in citation depth: the AI explicitly cites the construction step (1.12), definitions (D1.10, D1.15, D3.2), and proposition 3.2 to spell out why the contradiction arises (G inside circle implies tangent DE crosses the circle, contradicting tangency), whereas Heath leaves the final contradiction implicit with just 'the less than the greater: which is impossible.' Heath cites no references that the AI omits (heath_only is empty), and all ai_only items are either construction/definition over-citations or the substantive 3.2 which merely makes explicit what Heath's argument leaves implicit. This is Case A: same backbone, different citation depth.

### 3.19
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume the center F is not on the perpendicular CA, invoke 3.18 to show FC is perpendicular to DE (so angle FCE is right), note that angle ACE is also right by construction, derive that angle FCE equals angle ACE, then show this leads to the contradiction that a lesser angle equals a greater. The AI proof establishes the same key intermediate conclusions as Heath but explicitly cites axiom-level references that Heath leaves implicit: P1 (joining FC), D1.10 (definition of right angle), P4 (all right angles are equal), and CN5 (whole is greater than the part). Since heath_only is empty and ai_only contains only postulates, common notions, and a definition, this is a clear case of over-citation at the axiom level with the same logical backbone, yielding a granularity difference (G).

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: forming isosceles triangles from radii of the circle, applying the isosceles triangle theorem (1.5) to establish equal base angles, then using the exterior angle theorem (1.32) to show the central angle is double the inscribed angle. Both handle the case where the diameter falls inside the angle (addition of sub-angles) and where it falls outside (subtraction). The AI proof is more explicit in covering three cases (center on a side, inside, and outside the inscribed angle) and in citing the underlying axioms and definitions. The ai_only set consists entirely of common notions (CN2, CN3), a definition (D1.15), and postulates (P1, P2) -- all of which Heath uses implicitly without explicit citation. The heath_only set is empty. This is a textbook Case A in Q2: same backbone, different citation depth, yielding a Granularity difference.

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: find the centre of the circle, show that the central angle is double each inscribed angle (via III.20), and conclude the two inscribed angles are equal. The AI proof cites additional construction-level and definitional references (3.1 for finding the centre, P1 for joining lines, CN1 for the equality inference, and definitions D1.15, D3.6, D3.8) that Heath leaves implicit. Since heath_only is empty and all ai_only items are construction props, common notions, postulates, or definitions, this is a clear case of the AI over-citing at a finer granularity while following the identical proof strategy.

### 3.22
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: apply I.32 to a triangle formed by a diagonal of the cyclic quadrilateral, then use III.21 (angles in the same segment are equal) to replace two of the triangle's angles with parts of the opposite angle of the quadrilateral, yielding that one pair of opposite angles sums to two right angles, and then repeat the argument for the other pair. The AI uses diagonal BD first while Heath uses AC first, and the AI explicitly works out both pairs whereas Heath says 'similarly' for the second, but these are presentational differences, not backbone differences. The sole citation discrepancy is that the AI explicitly cites CN1 for its substitution steps while Heath performs the same substitutions without citing the Common Notion. Since CN1 is a common notion (axiom-level), this is a classic over-citation representing a citation-depth difference, confirming Case A of Q2 and category G.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: assume two similar unequal segments on the same side of AB, establish that angles in the segments are equal by definition of similar segments (D3.11), then derive a contradiction via the exterior angle theorem (1.16) since one angle must be exterior to the other. The AI proof adds three citations not in Heath (3.10, D3.8, P1), but none represent a different logical path. Proposition 3.10 is used to explicitly justify why one arc lies inside the other (a fact Heath takes as evident from the construction); D3.8 explicitly cites the definition of angle in a segment (which Heath leaves implicit under D3.11); and P1 is a routine postulate citation for joining lines. Heath cites nothing the AI omits (heath_only is empty). All differences are citation-depth differences within the same backbone, satisfying Case A of Q2.

### 3.24
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use superposition to place segment AEB onto CFD, establishing that B coincides with D. However, the contradiction arguments diverge: Heath argues that if the segments do not coincide, a circle would cut another circle at more than two points, contradicting 3.10; the AI argues that non-coincidence would yield two similar and unequal segments on the same straight line on the same side, contradicting 3.23. Since 3.10 does not appear in Heath's proof of 3.23 (which uses III.Def.11 and I.16), the proof-tree containment test fails, confirming these are independent logical routes. The AI's path through 3.23 is valid and logically complete, so Q3 yields D.

### 3.25
**Category**: Granularity difference
**Jaccard**: 0.077
**Analysis**: Q2 decides this classification as G. Both proofs follow the same geometric backbone: bisect AC at D, draw DB perpendicular to AC, construct an angle to locate center E, then use I.6 to show EA=EB, and SAS congruence on triangles EDA and EDC to show EA=EC, concluding EA=EB=EC. The AI handles the equal-angle case identically to Heath with center at D. The only substantive citation difference is the final justification: Heath cites III.9 (three equal radii imply center) while the AI cites III.10 (two circles cannot intersect at more than two points, so the constructed circle must be the original). This is a different justification for the same conclusion at the same logical position, not a different backbone. The remaining ai_only items (1.10, 1.11, 1.23, 1.4, CN1, D1.15, D3.6, P1, P2, P3) are all construction steps, definitions, postulates, and common notions that Heath leaves implicit, confirming over-citation consistent with G.

### 3.26
**Category**: AI proof error
**Jaccard**: 0.125
**Analysis**: The AI proof's reductio argument for the central angles case (Steps 4-8) contains an unsupported assertion in Step 6: 'Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF.' This claim that equal arcs in equal circles yield equal central angles is precisely the content of Proposition 3.27, the converse of the theorem being proved (3.26). No citation is given, and no earlier proposition in Euclid establishes this result. The inference is therefore unsupported: the only justification would be the converse of the theorem under proof (circular) or the forward proposition 3.27. Heath's proof avoids this entirely by using a direct approach via segment similarity (D3.11) and III.24 rather than reductio. The audit record completes convincingly because the missing element is genuine support (not mere expansion of a supported step), making this a clear unsupported assertion under the hardened 1(b) standard.
**Audit Record**: CANDIDATE E — 3.26
  violated_claim : "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF" (Step 6)
  failure_mode   : unsupported_assertion
  missing_is     : support — there is no cited or invoked proposition that licenses the inference from equal arcs to equal angles. The result that would license it (3.27) is the converse of the theorem being proved and is a forward dependency.
  evidence       : Step 6 text: "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF." No citation is provided. The needed result is 3.27 (equal arcs -> equal angles in equal circles), which is the next proposition (forward).
  why_not_terse  : This is not mere brevity — the step invokes the converse of the very theorem being proved. No earlier proposition in Euclid establishes that equal arcs in equal circles yield equal central angles. The logical gap is circular/forward reasoning, not a skipped algebraic step.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share identical key intermediate conclusions: (1) assume angle BGC is not equal to angle EHF and derive a contradiction by constructing angle BGK equal to EHF via I.23, (2) apply III.26 to get circumference BK equal to EF, (3) use transitivity with the hypothesis EF = BC to get BK = BC which is impossible since BK is a proper part of BC, (4) conclude BGC = EHF, and (5) extend to circumference angles using III.20 showing each circumference angle is half the corresponding centre angle. The AI proof explicitly cites CN1 (for the transitivity step equating BK to BC through EF) and CN5 (for the principle that a part cannot equal the whole), whereas Heath uses these common notions implicitly without citation. Since ai_only contains only common notions and heath_only is empty, this is a straightforward Case A same-backbone-different-depth situation.

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: take centres of equal circles, join radii, use SSS (I.8) to establish equal central angles, apply III.26 to get equal minor circumferences, then subtract from equal whole circles to obtain equal major circumferences. The ai_only set {3.1, CN3, CN5, D3.1, P1} consists entirely of construction propositions (3.1 for finding centres), postulates (P1 for joining lines), definitions (D3.1 for equal circles having equal radii), and common notions (CN3 for subtraction, CN5 for part-whole). These make explicit the implicit steps Heath performs without citation. The heath_only set is empty, confirming the AI covers everything Heath does and more. This is a clear Case A in Q2: same backbone, different citation depth.

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: (1) find the centres of the equal circles and join radii, (2) establish that the radii are equal because the circles are equal, (3) use III.27 to conclude the central angles are equal from the equal circumferences, and (4) apply I.4 (SAS) to conclude BC = EF. The ai_only citations (3.1, D3.1, P1) are all construction-level or definitional references that Heath uses implicitly without explicit citation: 3.1 for finding centres, D3.1 for the definition that equal circles have equal radii, and P1 for joining straight lines. Heath_only is empty. Since the key intermediate conclusions are identical and the citation difference consists entirely of construction and definitional over-citation by the AI, this is a granularity difference.

### 3.30
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: bisect chord AB at C, draw CD perpendicular to AB, prove triangles ACD and BCD congruent by SAS (I.4) yielding AD = DB, then apply III.28 to conclude arc AD = arc DB. The AI proof cites the same core propositions as Heath (I.4, III.28) plus three additional construction-level references (1.10 for bisecting a segment, 1.11 for drawing a perpendicular, P1 for joining points) that Heath invokes implicitly. Since heath_only is empty and ai_only contains only construction propositions and a postulate, this is a clear case of same backbone with different citation depth, classifying as G.

### 3.31
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 identifies a different backbone between the AI and Heath proofs. For part 1 (angle in semicircle is right), both proofs use the same approach via I.5 and I.32, though the AI adds supplementary angle reasoning via I.13. However, for part 2 (angle in greater segment is acute), Heath argues directly from I.17 (two angles of a triangle sum to less than two right angles) applied to the triangle containing the right angle, while the AI takes a fundamentally different route through III.20 (central angle equals double the inscribed angle) to conclude the inscribed angle is acute. The proof-tree containment test confirms this is a genuine path difference: I.17 does not appear in Heath's proof of III.20, so the AI is not simply citing a higher-level result that subsumes Heath's steps. For parts 4-5 (angles OF the segments), the AI uses III.16 about mixed angles while Heath argues directly from the rectilineal right angle, representing another backbone difference. The AI also introduces III.20 which Heath does not use at all. Q3 confirms the AI's different path is logically valid: the chain from central angles to inscribed angle acuteness is sound, and the arguments for the mixed-angle parts, while convoluted, reach supported conclusions. Classification is D.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions in the same order: (1) BA is a diameter perpendicular to tangent EF, (2) angle ADB is right by 3.31, (3) angles ABD + DAB equal one right angle by 1.32, (4) angle DBF equals angle DAB by subtraction, (5) opposite angles in cyclic quadrilateral ABCD sum to two right angles by 3.22, and (6) angle DBE equals angle BCD by subtraction. The backbone is the same. The citation difference is that Heath uses 3.19 (centre lies on the perpendicular to the tangent from the point of contact) to establish that BA is a diameter, while the AI uses 3.1 (finding the centre) and 3.18 (line from centre to point of contact is perpendicular to tangent) to establish the same fact by a different construction route. Since 3.18 appears inside Heath's own proof of 3.19, this satisfies the proof-tree containment test: the AI cites 3.18 directly while Heath cites the higher-level 3.19 that depends on 3.18. The remaining ai_only items (1.13, CN1, CN3, D1.17, D3.8, P1) are explicit citations of construction steps, definitions, common notions, and basic results that Heath uses implicitly, confirming a citation-depth difference rather than a path difference.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs address all three required cases (acute, right, obtuse) with identical logical backbones: constructing the angle BAD equal to C, drawing AE perpendicular to AD, bisecting AB, drawing FG perpendicular to AB, proving GA=GB via I.4, constructing the circle through A and B, showing AD is tangent via III.16, and applying the tangent-chord angle theorem III.32 to conclude the angle in the alternate segment equals C. The right-angle case uses III.31 identically. The ai_only set consists entirely of construction propositions (1.10, 1.11, 1.23), postulates (P1, P3, P5), and definitions (D3.6, D3.8) that Heath uses implicitly without explicit citation. heath_only is empty, confirming the AI covers all of Heath's reasoning. This is a straightforward case of over-citation at the construction level with no difference in the argumentative backbone.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: draw a tangent at a point B on the circle, construct angle FBC equal to the given angle D using I.23, then apply III.32 (the alternate segment theorem) to conclude that the angle in segment BAC equals angle D. The AI proof cites three additional references not in Heath (3.17 for constructing the tangent line, P1 for drawing line BC, and CN1 for the transitivity of equality), but these are all construction-step and axiom-level over-citations that do not alter the key intermediate conclusions. Heath's proof uses the same steps implicitly without citing them. Since heath_only is empty and the ai_only items are all construction/axiom references, this is a clear Case A in Q2: same backbone, different citation depth.

### 3.35
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: for the case where lines are not both through the centre, they bisect a chord using III.3, apply II.5 to get rect(AE,EC) + sq(EG) = sq(GC), use I.47 to consolidate squares into sq(FE) and sq(FC), establish that FC = FB as radii, derive rect(AE,EC) + sq(FE) = sq(FB), apply the same reasoning to the other chord to get rect(DE,EB) + sq(FE) = sq(FB), and subtract sq(FE) to conclude equality. The AI additionally handles three explicit sub-cases (both through centre, one through centre, neither through centre) whereas Heath handles two (both through centre, not through centre), but the core argument is identical. The ai_only set consists entirely of over-citations: construction props (1.12), auxiliary finding of centre (3.1), common notions (CN1, CN2, CN3), a definition (D1.15), and postulates (P1, P2). Heath_only is empty. The same key intermediate conclusions appear in both proofs at the same logical positions, differing only in citation granularity.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs treat the same two cases (secant through the centre and secant not through the centre) with identical key intermediate conclusions: establishing a right angle at the tangent point via 3.18, bisecting the chord (3.3 in Case 2), applying the algebraic identity 2.6, using the Pythagorean theorem 1.47 on right triangles formed with the centre, and subtracting equal squares to reach the conclusion. The ai_only set consists entirely of over-citations of foundational items that Heath uses implicitly: construction props (1.12 for drawing a perpendicular, P1 for joining lines), definitions (D1.15 for radius equality, D1.17 for diameter), and common notions (CN2 for adding equals, CN3 for subtracting equals). The heath_only set is empty, confirming no substantive propositions are missing from the AI proof. This is a clear Case A (same backbone, different citation depth), yielding a Granularity difference.

### 3.37
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions in the same logical order: (1) angle FED is right via III.18, (2) rect(AD,DC) = sq(DE) via III.36, (3) sq(DE) = sq(DB) so DE = DB, (4) triangle congruence via I.8 yielding angle DBF = angle DEF, (5) angle DBF is right, (6) DB touches the circle via III.16. The AI proof wraps this in an unnecessary proof-by-contradiction frame and explicitly cites construction and foundational steps that Heath leaves implicit (3.1 for finding the center, 3.17 for drawing the tangent, P1 for joining lines, CN1 for transitive equality, D1.15 for the radius definition, D3.2 for the tangent definition), but these are all over-citations of basic constructions, axioms, and definitions. Heath_only is empty, confirming that Heath's citations are a proper subset of the AI's. The backbones are the same; only citation depth differs.
