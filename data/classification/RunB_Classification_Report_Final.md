# Euclid Proof Classification Report — RunB

Classification of all 465 AI-generated proofs against Heath's reference proofs, into four categories: **Perfect match (P)**, **Granularity difference (G)**, **Path difference (D)**, and **AI proof error (E)**. P denotes identical citation sets and a complete proof; G denotes the same proof strategy with differences confined to citation granularity (over-citing construction primitives or definitions, inlining or expanding sub-lemmas); D denotes a genuinely different valid route to the same conclusion (typically the AI's algebraic or arithmetic manipulation in place of Heath's geometric proposition chain); E denotes a positively identifiable logical defect in the AI proof.

## Overall Summary

| Category | Count | Share |
|---|---|---|
| P — Perfect match | 18 | 3.9% |
| G — Granularity difference | 325 | 69.9% |
| D — Path difference | 122 | 26.2% |
| E — AI proof error | 0 | 0.0% |
| **Total** | **465** | **100.0%** |

## Per-Book Distribution

| Book | P | G | D | E | n | Mean Jaccard |
|---|---|---|---|---|---|---|
| 1 | 10 | 38 | 0 | 0 | 48 | 0.657 |
| 2 | 0 | 6 | 8 | 0 | 14 | 0.198 |
| 3 | 0 | 29 | 8 | 0 | 37 | 0.278 |
| 4 | 0 | 14 | 2 | 0 | 16 | 0.332 |
| 5 | 2 | 17 | 6 | 0 | 25 | 0.374 |
| 6 | 0 | 27 | 6 | 0 | 33 | 0.386 |
| 7 | 1 | 29 | 9 | 0 | 39 | 0.316 |
| 8 | 1 | 15 | 11 | 0 | 27 | 0.359 |
| 9 | 2 | 21 | 13 | 0 | 36 | 0.356 |
| 10 | 1 | 82 | 32 | 0 | 115 | 0.371 |
| 11 | 1 | 29 | 9 | 0 | 39 | 0.382 |
| 12 | 0 | 11 | 7 | 0 | 18 | 0.295 |
| 13 | 0 | 7 | 11 | 0 | 18 | 0.257 |
| **All** | **18** | **325** | **122** | **0** | **465** | **0.375** |

## Error Detail (E Classifications)

No E-class propositions remain after correction.

---

## Book 1

| Category | Count |
|---|---|
| Perfect match (P) | 10 |
| Granularity difference (G) | 38 |
| Path difference (D) | 0 |
| AI proof error (E) | 0 |

**Total**: 48 propositions

### 1.1
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct two circles with centres A and B, join intersection point C to A and B, establish AC=AB and BC=BA from the definition of a circle (D1.15), derive CA=CB by transitivity (CN1), and conclude that triangle ABC is equilateral. The only citation difference is that the AI explicitly cites D1.20 (definition of equilateral triangle) when concluding the triangle is equilateral, while Heath leaves this definition implicit. Since heath_only is empty and ai_only contains only a definition (D1.20), this is a pure citation-depth difference with the same backbone, satisfying Case A of Q2 for Granularity difference.

### 1.2
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) BG = BC from the circle CGH, (2) DL = DG from the circle GKL, (3) DA = DB from the equilateral triangle, (4) AL = BG by subtracting equals (CN3), and (5) AL = BC by transitivity (CN1). The only citation difference is that the AI explicitly cites Definition 1.15 (definition of a circle) to justify that radii are equal, whereas Heath leaves this justification implicit in phrases like 'since the point B is the centre of the circle CGH, BC is equal to BG.' This is a classic citation-depth difference with no structural divergence, placing it squarely in Case A of Q2, yielding Granularity difference (G).

### 1.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of 1.3 follows the exact same logical backbone as Heath's proof: placing AD equal to C at point A using I.2, describing circle DEF with center A and distance AD using Postulate 3, concluding AE equals AD by Definition 1.15 (radii of the same circle), and then deriving AE equals C by transitivity via Common Notion 1. The citation sets are identical (1.2, CN1, D1.15, P3) with Jaccard similarity 1.0, and ai_only and heath_only are both empty. Since both the key intermediate conclusions and the citation sets match exactly, this is classified as a Perfect match (P).

### 1.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions using the method of superposition: placing A on D, showing B coincides with E (AB=DE), AC lies along DF (equal angles), C coincides with F (AC=DF), BC coincides with EF (reductio), whole triangles coincide and are equal (CN4), and remaining angles coincide and are equal. The logical backbones are the same. The only difference is that the AI explicitly cites Postulate 1 in Step 4 when arguing that BC must coincide with EF, while Heath does not cite P1. Since P1 is an axiom-level citation and the underlying geometric argument is identical in both proofs, this is a citation-depth difference (Case A in Q2), yielding Granularity difference (G).

### 1.5
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: constructing equal segments AF=AG on the produced lines via I.3, applying SAS (I.4) to triangles AFC and AGB, deducing BF=CG by subtraction, applying SAS (I.4) again to triangles BFC and CGB, and finally subtracting angles to conclude the base angles are equal and the angles under the base are equal. The AI cites two additional foundational items not in Heath's citation set: CN3 (equals subtracted from equals, used explicitly in Steps 5 and 7) and D1.20 (definition of isosceles triangle, cited in Step 4 for the given AB=AC). Heath performs the same subtractions and uses the same given without citing these foundational items explicitly. Since the key intermediate conclusions are identical and the only citation differences are over-citations of a common notion and a definition, this is a citation-depth difference (Case A), yielding G.

### 1.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume AB is not equal to AC with AB greater, cut DB equal to AC from AB (1.3), join DC (P1), show triangles DBC and ACB are congruent by SAS (1.4), derive contradiction via the whole being greater than the part (CN5), conclude AB equals AC. The key intermediate conclusions are the same in both proofs. Heath's reference list is empty (he cites no propositions by label), while the AI explicitly cites 1.3, 1.4, CN5, and P1 for steps that Heath performs without labeling. Since heath_only is empty and ai_only contains only construction props, a common notion, and a postulate, this is a pure citation-depth difference with the same backbone, yielding Granularity difference (G).

### 1.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: assume the contrary (two pairs of equal lines from the same endpoints meeting at different points), join CD, apply I.5 twice to the isosceles triangles ACD and BCD to derive contradictory angle inequalities. Heath uses I.5 to get angle ACD = angle ADC, then argues angle CDB is much greater than angle DCB, then uses I.5 again on triangle BCD to get angle CDB = angle DCB, reaching contradiction. The AI proof follows the identical strategy in its interior case (Steps 3-8), deriving the same contradiction through the same pair of I.5 applications. The AI additionally handles exterior and boundary cases explicitly, and over-cites by listing CN5 (whole greater than part, which Heath invokes implicitly), P1 (joining CD), and P2 (extending lines). Since heath_only is empty and ai_only contains only postulates and common notions used implicitly by Heath, this is a citation-depth difference with the same backbone, yielding G.

### 1.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: superposition of one triangle onto the other, coincidence of base endpoints due to equal bases, a reductio argument via I.7 showing the remaining vertices must coincide, and concluding equality of the contained angles. The only difference is that the AI explicitly cites CN4 (things which coincide with one another are equal) for the final step where coincidence of angles implies equality, whereas Heath leaves this inference implicit. Since heath_only is empty and ai_only contains only the common notion CN4, this is a citation-depth difference with the same key intermediate conclusions, yielding Granularity difference (G).

### 1.9
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: take D on AB, cut off AE equal to AD (I.3), construct equilateral triangle DEF on DE, join AF, then use SSS congruence (I.8) with AD=AE, DF=EF, AF common to conclude angle DAF equals angle EAF. The AI's two extra citations (1.1 for constructing the equilateral triangle and P1 for joining straight lines) are construction-level references that Heath uses implicitly without explicit citation. Since the key intermediate conclusions are the same and the only difference is citation depth for construction steps, this is a granularity difference.

### 1.10
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: construct an equilateral triangle ABC on AB (1.1), bisect angle ACB with line CD (1.9), then apply SAS congruence (1.4) with AC=BC, CD common, and angle ACD = angle BCD to conclude AD=BD. The only citation difference is D1.20 in ai_only, which is the definition of an equilateral triangle that the AI explicitly cites when justifying AC=BC. Heath uses the same fact implicitly without citing the definition. Since heath_only is empty and the sole ai_only item is a definition providing extra justification for a step both proofs share, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 1.11
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow an identical logical backbone: take a random point D on AC, cut off CE equal to CD via I.3, construct equilateral triangle DEF on DE via I.1, join FC, then use I.8 to show triangles DCF and ECF are congruent so angles DCF and ECF are equal, and finally apply Def. 1.10 to conclude each is a right angle. The only citation difference is that the AI explicitly cites Postulate 1 for joining FC, while Heath performs this construction without explicit citation. Since P1 is a construction postulate and the underlying geometric fact (joining two points by a line) is present in both proofs at the same logical position, this is a citation-depth difference, not a backbone difference.

### 1.12
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: take point D on the other side of AB, draw circle with center C and distance CD, bisect the chord GE at H, join CG/CH/CE, then use I.8 (SSS congruence of triangles GHC and EHC via GH=HE from bisection, HC common, CG=CE as radii) to conclude angle CHG equals angle CHE, and finally apply Def. 10 to establish that these equal adjacent angles are right angles, making CH perpendicular to AB. The only difference is that the AI explicitly cites Definition 1.15 (the definition of a circle) to justify CG=CE as radii, whereas Heath states this fact without an explicit definition citation. Since heath_only is empty and ai_only contains only D1.15 (a definition providing extra citation depth for a step both proofs share), this is a clear Case A granularity difference.

### 1.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 1.13 follow the identical logical backbone through the same two cases: (1) if the adjacent angles are equal, they are two right angles by Definition 1.10, and (2) if not, a perpendicular is constructed using Proposition 1.11, angles are decomposed on each side using Common Notion 2, and Common Notion 1 establishes that the original angle pair equals the pair of right angles. The citation sets are exactly equal (1.11, CN1, CN2, D1.10) with Jaccard similarity 1.0, ai_only and heath_only both empty, and the key intermediate conclusions match at every stage. Since the proofs share the same backbone and the same citation set, this is a Perfect match.

### 1.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: assume BD is not in a straight line with CB, let BE be the straight-line extension, use I.13 to get ABC+ABE = two right angles, equate with the hypothesis ABC+ABD = two right angles, subtract the common angle ABC to get ABE = ABD, then derive contradiction since ABE is greater than ABD. The citation differences are purely at the axiom/postulate level: the AI explicitly cites P2 (for the line extension construction) and CN5 (for the whole-greater-than-part contradiction) where Heath leaves these implicit, while Heath explicitly cites P4 (all right angles equal) alongside CN1 where the AI cites only CN1. These are citation-depth differences on the same backbone, making this a granularity difference.

### 1.15
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share identical key intermediate conclusions: applying I.13 twice to show that each pair of supplementary angles sums to two right angles, then using CN1 to equate the sums, and CN3 to subtract the common angle. The AI proof even expands Heath's 'similarly' remark by explicitly proving the second pair of vertical angles. The only citation difference is that Heath cites Postulate 4 alongside CN1 when equating the two sums (ensuring 'two right angles' is a well-defined quantity), while the AI omits P4 and relies on CN1 alone. This is a citation-depth difference rather than a backbone divergence, since P4 is a foundational postulate and the logical step is the same in both proofs.

### 1.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 1.16 follow identical logical backbones: bisecting AC at E, constructing F with EF = BE via I.3, establishing vertical angles AEB = FEC via I.15, applying SAS congruence (I.4) to conclude angle BAE = angle ECF, then using CN5 to show angle ACD > angle BAE. Both proofs address the second case (angle ACD > angle ABC) using I.15 to equate angle ACD with the vertical angle BCG and applying the same construction. The citation sets are exactly equal ({1.10, 1.15, 1.3, 1.4, CN5, P1, P2}) with Jaccard similarity 1.0, and the key intermediate conclusions match at every step. No forward dependencies, no logical errors, and no path or granularity differences were found, satisfying the perfect match criteria.

### 1.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: produce BC to D via P2, apply I.16 to establish that exterior angle ACD exceeds interior angle ABC, add angle ACB to both sides, invoke I.13 to equate angles ACD and ACB with two right angles, and conclude that angles ABC and BCA sum to less than two right angles, with the other two pairs handled by symmetry. The citation sets are exactly equal (1.13, 1.16, P2) with Jaccard 1.0, and no ai_only or heath_only items exist. Since the key intermediate conclusions match and the citation sets are identical, the perfect match check at the end of the protocol yields category P.

### 1.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: cut AD equal to AB on AC (I.3), observe that the exterior angle ADB of triangle BDC exceeds angle DCB (I.16), note that angle ADB equals angle ABD because AB equals AD (isosceles triangle), and conclude that angle ABC is greater than angle ACB. The AI proof's three extra citations (I.5 for the isosceles base angles, CN5 for the whole being greater than the part, and P1 for joining BD) all correspond to facts that Heath uses implicitly. Heath writes 'the angle ADB is equal to the angle ABD, since the side AB is equal to AD' without naming I.5, and uses 'much greater' without naming CN5. Since the key intermediate conclusions are identical and all ai_only items represent explicit citation of implicitly used results, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 1.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 1.19 follow an identical logical structure: both prove that the greater angle is subtended by the greater side by trichotomy elimination. Both eliminate AC = AB using I.5 (base angles of an isosceles triangle are equal) and AC < AB using I.18 (the greater side subtends the greater angle), arriving at the same conclusion AC > AB. The citation sets are exactly equal (ai_used = heath_refs = {1.5, 1.18}), with empty ai_only and heath_only sets and a Jaccard similarity of 1.0. Since the key intermediate conclusions are the same and the citation sets match perfectly, this is classified as P (Perfect match).

### 1.20
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: extend BA to D with DA equal to AC, establish angle ADC equals angle ACD via I.5, show angle BCD is greater than angle ADC via CN5, conclude DB is greater than BC via I.19, and derive BA plus AC is greater than BC since DB equals BA plus AC. The AI proof explicitly cites P2 (to extend BA) and 1.3 (to cut off AD equal to AC), which are construction steps that Heath performs without explicit citation. These ai_only items are construction propositions and postulates, which are classic indicators of over-citation at the construction level. Since heath_only is empty and all key intermediate conclusions match, this is a same-backbone, different-citation-depth situation (Case A), yielding G.

### 1.21
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Classification was decided at Q2 (Case A). Both proofs follow the identical logical backbone: construct BD produced to meet AC at E, apply I.20 twice (in triangles ABE and DEC/CED) with additions to establish BA+AC > BD+DC for the length part, then apply I.16 twice (exterior angles BDC > CED and CEB > BAC) with chaining for the angle part. The ai_only set {CN2, P1, P2} consists entirely of a common notion (CN2 for the addition steps) and postulates (P1, P2 for producing BD to meet AC), which Heath uses implicitly without citation. The empty heath_only set confirms no substantive proposition is missing from the AI's citations. This is a classic over-citation pattern where the AI makes explicit the foundational axioms that Heath leaves tacit, yielding a granularity difference rather than a path difference.

### 1.22
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing segments DF=A, FG=B, GH=C on a line using I.3, drawing two circles (center F with radius FD, center G with radius GH), finding their intersection K, and establishing FK=A, GK=C, FG=B to conclude triangle KFG has sides equal to the given lines. The AI proof adds explicit foundational citations (CN1 for transitivity of equality, D1.15 for the definition of a circle ensuring radii are equal, P1 for joining lines, P2 for extending a line, P3 for drawing circles) that Heath leaves implicit. The AI also includes an extended argument (Step 4) justifying why the two circles must intersect, which Heath omits. Since heath_only is empty and all ai_only items are postulates, definitions, and common notions representing deeper citation depth rather than a different logical path, this is Case A of Q2: same backbone, different citation depth, yielding category G.

### 1.23
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: take arbitrary points D and E on the rays of the given angle, join DE to form triangle DCE, construct triangle AFG with sides equal to CD, CE, and DE respectively, then apply I.8 (SSS congruence) to conclude angle FAG equals angle DCE. The AI explicitly cites 1.22 (construction of a triangle from three line segments) and P1 (postulate to join two points), which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only a construction proposition (1.22) and a postulate (P1), this is a clear Case A: same backbone with the AI providing finer citation granularity.

### 1.24
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct angle EDG equal to BAC and DG equal to DF, use SAS congruence (I.4) to establish BC = EG, use the isosceles triangle theorem (I.5) to show angle DGF = angle DFG, chain the angle inequalities to conclude angle EFG > angle EGF, then apply I.19 to get EG > EF, and finally substitute BC = EG. The AI proof cites three additional items not in Heath (1.3 for segment construction, P1 for joining lines, CN5 for whole-greater-than-part), all of which are construction-level or axiom-level citations that justify steps Heath performs implicitly. Heath's citation set is a proper subset of the AI's, and heath_only is empty. Since the key intermediate conclusions are identical and the only differences are in citation depth for constructions and common notions, this is a granularity difference.

### 1.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 1.25 follow identical logical structure: both prove by exhaustion that angle BAC must be greater than angle EDF by eliminating the two alternatives. Both eliminate the case BAC = EDF using I.4 (which would force BC = EF, contradicting BC > EF) and eliminate BAC < EDF using I.24 (which would force EF > BC, again contradicting BC > EF). The citation sets are identical at {1.4, 1.24} with Jaccard similarity 1.0, and all key intermediate conclusions match exactly, satisfying the perfect match criteria.

### 1.26
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same two-case reductio structure: Case 1 (side adjoining equal angles) constructs a shorter segment, applies I.4 to derive a contradiction with a part equaling the whole, then concludes via I.4; Case 2 (side subtending an equal angle) similarly constructs a shorter segment, applies I.4, and derives a contradiction via the exterior angle theorem (I.16), then concludes via I.4. The key intermediate conclusions are identical in both proofs. The AI's extra citations (1.3 for segment construction, P1 for joining points, CN1 for transitivity of equality, CN5 for whole-greater-than-part) merely make explicit the construction steps and common notions that Heath leaves implicit. Since heath_only is empty and all ai_only items are construction-level or axiom-level citations, this is a clear case of same backbone with different citation depth, yielding Granularity difference (G).

### 1.27
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 1.27 follow identical logical backbones: both proceed by contradiction, assuming the two lines are not parallel and therefore meet at a point on one side, forming a triangle in which the exterior angle (one of the alternate angles) must be greater than the interior and opposite angle (the other alternate angle) by I.16, contradicting the hypothesis that the alternate angles are equal. Both proofs handle both directions (meeting on side B,D and on side A,C) and conclude by Def. 23 that the lines are parallel. The citation sets are exactly equal (1.16 and D1.23), yielding Jaccard 1.0, and the key intermediate conclusions are the same, so the classification is Perfect match (P).

### 1.28
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided this classification. Both proofs handle the same two cases (exterior angle equal to interior opposite, and co-interior angles summing to two right angles) and reach the same key intermediate conclusion in each case: that the alternate angles AGH and GHD are equal, then applying I.27 to conclude parallelism. The AI's Case 2 takes a slightly different micro-route (using I.13 on EGB+BGH rather than AGH+BGH, then converting via I.15), but arrives at the identical key conclusion. The only difference in citations is that the AI explicitly cites CN1 and CN3 for the equality transitions and subtraction that Heath performs implicitly without citation. Since heath_only is empty and ai_only contains only common notions (CN1, CN3), this is a classic over-citation pattern representing a citation-depth difference with the same logical backbone, yielding G.

### 1.29
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: a reductio ad absurdum showing that if alternate angles AGH and GHD are unequal, Post. 5 forces the parallel lines to meet, contradicting the parallel hypothesis; then deriving the exterior angle equality via I.15 and CN1, and the interior angles summing to two right angles via CN2 and I.13. The only citation difference is that the AI explicitly cites D1.23 (the definition of parallel lines) when invoking the contradiction, whereas Heath states the same fact implicitly ('because they are by hypothesis parallel'). Since heath_only is empty and ai_only contains only a definition, this is a pure citation-depth difference with identical backbone, yielding G.

### 1.30
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the identical logical backbone: draw a transversal across three parallel lines, apply I.29 twice to establish that alternate angles AGK and GHF are equal and that angles GHF and GKD are equal, then use CN1 (transitivity) to conclude angle AGK equals angle GKD, and finally infer AB is parallel to CD because the alternate angles are equal. The only difference is that the AI explicitly cites 1.27 (the converse direction: equal alternate angles imply parallel lines) for the final step, while Heath leaves this inference implicit, simply stating 'and they are alternate. Therefore AB is parallel to CD' without a citation. Since heath_only is empty and ai_only contains only 1.27, and the underlying logical steps are identical in both proofs, this is a Case A same-backbone citation-depth difference.

### 1.31
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing angle DAE equal to angle ADC using I.23, establishing that the alternate angles EAD and ADC are equal, and concluding that EAF is parallel to BC by I.27. The logical backbone is the same in both proofs. The only difference is that the AI explicitly cites Postulates P1 (to join AD) and P2 (to produce EA to F), which Heath uses implicitly without citation. Since ai_only contains only postulates (construction axioms) and heath_only is empty, this is a straightforward Case A citation-depth difference, yielding Granularity difference (G).

### 1.32
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: construct CE parallel to AB via I.31, establish BAC = ACE and ECD = ABC via two applications of I.29, combine to get ACD = BAC + ABC, add angle ACB to both sides, invoke I.13 to show ACD + ACB = two right angles, and conclude the three interior angles equal two right angles. The AI proof explicitly cites CN1 and CN2 for the equality-manipulation steps (adding equals to equals and substituting equals for equals), while Heath performs these same steps without citing the common notions. Since the key intermediate conclusions are identical and the only citation difference is the AI's explicit invocation of common notions that Heath uses implicitly, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 1.33
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) alternate angles ABC and BCD are equal via I.29, (2) triangles ABC and BCD are congruent by SAS via I.4, yielding AC = BD and the alternate angles ACB and DBC equal, and (3) AC is parallel to BD via I.27. The only citation difference is that the AI explicitly cites Postulate 1 for joining BC, while Heath performs the same construction without a formal citation. Since the ai_only set contains only P1 (a construction postulate) and heath_only is empty, this is a same-backbone, different-citation-depth scenario, making it a granularity difference.

### 1.34
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: they use I.29 twice to establish alternate angles, then I.26 (ASA) for triangle congruence yielding equal opposite sides and the remaining angle, then CN2 to combine angles for the second pair of opposite angles, and finally establish that the diagonal bisects the parallelogram via triangle equality. The sole difference is that Heath separately invokes I.4 (SAS) in the bisection part to prove the two triangles are equal in area, whereas the AI attributes triangle equality directly to I.26 without a separate I.4 step. Since I.26 establishes all corresponding sides and angles equal, triangle equality follows immediately from I.4 using those results, making the AI's omission of I.4 a citation-depth difference rather than a logical gap. The heath_only set {1.4} represents an under-citation by the AI, not a different proof path. Both proofs reach the same key intermediate conclusions at the same logical positions, confirming Case A of Q2.

### 1.35
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 1.35 follow the same logical backbone with identical citation sets (Jaccard = 1.0). Both proofs establish the same key intermediate conclusions in the same order: AD = EF via I.34 and CN1, AE = DF via CN2, triangle EAB equals triangle FDC via I.29 and I.4, subtraction of triangle DGE via CN3 to get equal trapezia, and addition of triangle GBC via CN2 to reach equal parallelograms. The AI proof includes one additional derivation (EB = FC via I.34 in Step 4), but this does not introduce any new citations or alter the logical structure. Since ai_used equals heath_refs exactly and the key intermediate conclusions match, the classification is Perfect match (P).

### 1.36
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 1.36 follow identical logical backbones and cite exactly the same set of references. Both proofs construct parallelogram EBCH by joining BE and CH, establish BC = EH via CN1 (transitivity through FG = EH from I.34 and BC = FG given), use I.33 to show EBCH is a parallelogram, apply I.35 twice to show ABCD = EBCH and EFGH = EBCH, and conclude ABCD = EFGH by CN1. The citation sets are identical (ai_used = heath_refs = {1.33, 1.34, 1.35, CN1}), yielding Jaccard = 1.0 with no ai_only or heath_only items. Since the key intermediate conclusions match and the citation sets are equal, this is a perfect match.

### 1.37
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing parallelograms EBCA and DBCF via I.31, showing their equality via I.35 (same base BC, same parallels), establishing each triangle as half its respective parallelogram via I.34, and concluding the triangles are equal as halves of equals. The AI proof follows exactly the same logical backbone as Heath's. The only differences are that the AI explicitly cites CN3 (halves of equal things are equal) where Heath leaves this implicit (bracketed in the text), and P2 (postulate for producing lines) for the construction steps. These are axiom-level over-citations representing citation-depth differences, not backbone divergences. The AI's misidentification of diagonal BC (instead of AB for EBCA and DC for DBCF) is an imprecision in naming the geometric element, but the citation of I.34 correctly licenses the conclusion that each triangle is half its parallelogram, so under the lenience rule this does not constitute an invalid inference.

### 1.38
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct parallelograms GBCA and DEFH using I.31, establish their equality via I.36 (parallelograms on equal bases in the same parallels), show each triangle is half its respective parallelogram via I.34, and conclude that the triangles are equal because halves of equal things are equal. The sole citation difference is that the AI explicitly cites CN3 (halves of equal things are equal to one another) while Heath uses this principle implicitly (noted in brackets but not in the formal reference list). Since CN3 is a Common Notion (axiom) and the underlying logical step is present in both proofs, this is a citation-depth difference, making this a granularity difference (G).

### 1.39
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same proof-by-contradiction backbone: assume AD is not parallel to BC, draw AE parallel to BC via I.31, join EC, show triangle ABC equals triangle EBC by I.37, derive DBC equals EBC by CN1 and hypothesis, then reach a contradiction because DBC is greater than EBC. The key intermediate conclusions are identical in both proofs. The ai_only set contains CN5 (whole greater than part) and P1 (drawing a straight line), both axiom-level items that Heath uses implicitly without citing. CN5 makes explicit the informal reasoning Heath states as 'the greater to the less: which is impossible', and P1 justifies the construction 'let EC be joined'. The heath_only set is empty. These are purely over-citations of foundational axioms, confirming a citation-depth difference rather than a path difference.

### 1.40
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical reductio ad absurdum backbone: assume AD is not parallel to the base line, construct a parallel through A via 1.31, apply 1.38 to show the constructed triangle equals the given triangle, then use CN1 transitivity to derive that two different triangles are equal, reaching a contradiction. The AI's ai_only citations (CN5 and P1) are over-citations of implicitly used principles: CN5 explicitly names the 'whole is greater than the part' axiom that Heath invokes implicitly when stating 'the greater to the less: which is impossible', and P1 explicitly cites the postulate for joining straight lines that Heath performs without citation. The heath_only set is empty, confirming no missing steps. The key intermediate conclusions are identical in both proofs, making this a same-backbone, different-citation-depth case under Q2 Case A.

### 1.41
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same two key intermediate conclusions: (1) the diagonal AC bisects parallelogram ABCD, making it double of triangle ABC (via I.34), and (2) triangle ABC equals triangle EBC because they share the same base and lie between the same parallels (via I.37). The only difference is citation depth: the AI explicitly cites P1 for joining AC and CN1 for the substitution step that combines the two intermediate results, whereas Heath leaves these implicit. Since ai_only contains only a postulate (P1) and a common notion (CN1) and heath_only is empty, this is a clear Case A same-backbone, different-depth scenario, yielding Granularity difference (G).

### 1.42
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: bisect BC at E, join AE, construct angle CEF equal to D, draw parallels to form parallelogram FECG, then show triangle ABE equals triangle AEC (by I.38), triangle ABC is double triangle AEC, parallelogram FECG is double triangle AEC (by I.41), therefore FECG equals triangle ABC. The AI proof adds explicit citations for construction steps and common notions that Heath leaves implicit: 1.10 for bisection, P1 for joining a line, CN2 for the doubling conclusion, and CN1 for the final equality. Since heath_only is empty and all ai_only items (1.10, P1, CN1, CN2) are construction propositions, postulates, or common notions representing over-citation of implicit steps, this is Case A of Q2 -- same backbone with different citation depth -- yielding a Granularity difference (G).

### 1.43
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 1.43 follow identical logical backbones and cite exactly the same references. Both proofs proceed by (1) using I.34 to establish that the diagonal AC bisects the whole parallelogram ABCD into equal triangles ABC and ACD, (2) using I.34 again to show each sub-parallelogram about the diameter is bisected by its diagonal (AEK=AHK and KFC=KGC), (3) applying CN2 to add the equal sub-triangle pairs, and (4) applying CN3 to subtract equals from equals, yielding the equality of the complements. The citation sets are identical (ai_used = heath_refs = {1.34, CN2, CN3}) with Jaccard similarity 1.0, and the key intermediate conclusions match exactly, satisfying the perfect match check.

### 1.44
**Category**: Granularity difference
**Jaccard**: 0.778
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct parallelogram BEFG equal to triangle C in the required angle (I.42), place it adjacent to AB, draw AH parallel to BG/EF (I.31), show HB and FE meet at K using the parallel line angle sum (I.29) and Postulate 5, form parallelogram HLKF with KL parallel to EA (I.31), establish LB = BF as complements about diameter HK (I.43), conclude LB = C (CN1), and show angle ABM = D via vertical angles (I.15). The only citation differences are P1 and P2 in ai_only, which are basic postulates the AI explicitly cited for joining line HB and producing line FG to H, operations Heath performs without explicit citation. This is a straightforward over-citation of construction postulates, making this Case A of Q2: same backbone, different citation depth.

### 1.45
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same logical backbone: divide the rectilineal figure into triangles, construct parallelograms via I.42 and I.44, prove collinearity of corresponding sides using I.14 and I.29, establish parallelism using I.34 and I.30, and conclude the combined figure is a parallelogram equal to the original figure. The AI proof handles a pentagon (three triangles, three parallelograms) while Heath handles a quadrilateral (two triangles, two parallelograms), but this is simply a matter of generality in the example, not a structural difference. The citation differences are at the granularity level: ai_only contains D1.22 (definition of parallelogram, used explicitly by the AI but implicitly by Heath) and P1 (postulate for joining lines, again explicit vs implicit), while heath_only contains 1.33 (used by Heath to show the final figure is a parallelogram, where the AI achieves the same conclusion via 1.30 and D1.22) and CN1 (used explicitly by Heath but implicitly by the AI). The key intermediate conclusions -- collinearity of sides, parallelism of opposite sides, the combined figure being a parallelogram, and area equality -- are the same in both proofs, making this a same-backbone, different-depth situation.

### 1.46
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct a parallelogram ADEB by drawing a perpendicular and parallels, prove it equilateral by showing all four sides equal (using I.34 and the construction AD=AB), then prove it right-angled by applying I.29 to show co-interior angles sum to two right angles and I.34 to transfer the right angle to opposite angles. The ai_only set consists entirely of over-citations: 1.3 (cutting off a segment, which Heath performs without citation), CN1 (common notion for transitivity of equality), D1.10 and D1.22 (definitions of right angle and square), and P1 (a postulate for drawing a line). Heath_only is empty. These differences reflect citation depth, not a different proof strategy.

### 1.47
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow identical backbones: constructing squares on all three sides of the right triangle (I.46), drawing a parallel through the right-angle vertex, proving collinearity of extended sides via I.14, showing congruence of auxiliary triangles via I.4, using the double-area relationship via I.41 to equate each rectangle partition of the hypotenuse square with the corresponding leg square, and summing via CN2. The ai_only set consists entirely of over-citations: 1.31 (parallel construction Heath leaves implicit), P1 (joining lines Heath leaves implicit), D1.22 (definition of square used to justify right angles Heath states without citation), P4 (all right angles are equal, stated by Heath as obvious), and CN1 (equals of equals, where Heath uses an equivalent bracketed remark). heath_only is empty. Every ai_only item represents the AI explicitly citing a construction step, postulate, definition, or common notion that Heath leaves tacit, with no change to the logical backbone.

### 1.48
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct AD perpendicular to AC with DA equal to AB, join DC, show that DC squared equals BC squared via I.47 and the hypothesis, conclude DC equals BC, then apply SSS (I.8) to establish angle DAC equals angle BAC, and since DAC is right, BAC is right. The AI proof cites five additional references (1.11, 1.3, P1, CN1, CN2) that Heath leaves implicit. These are all construction-level propositions (1.11 for drawing a perpendicular, 1.3 for cutting off an equal segment, P1 for joining a line) and common notions (CN1 for transitivity of equality, CN2 for adding equals to equals). Heath's proof performs the same constructions and uses the same logical steps without explicitly citing these foundational results. Since heath_only is empty and ai_only consists entirely of construction and axiom references, this is a clear Case A granularity difference.


## Book 2

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 6 |
| Path difference (D) | 8 |
| AI proof error (E) | 0 |

**Total**: 14 propositions

### 2.1
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct rectangle BGHC with BG equal to A, then identify each sub-rectangle (BGKD, DKLE, ELCH) as the rectangle contained by A and the corresponding segment (BD, DE, EC), using I.34 to show the vertical sides equal BG and hence equal A. The AI proof adds three explicit citations not in Heath: I.29 (to justify that DK is perpendicular to BC because it is parallel to BG which is perpendicular to BC), CN2 (to justify summing the sub-rectangles), and D2.1 (the definition of rectangle, to formally identify each parallelogram as a rectangle). Heath leaves all three implicit. Since heath_only is empty and the ai_only items are all over-citations providing finer justification for steps that appear in both proofs at the same logical position, this is Case A of Q2: same backbone, different citation depth.

### 2.2
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof decomposes the square on AB geometrically by drawing a parallel line CF through C (using I.31), splitting the square ADEB into two rectangles AF and CE, then identifying each as rect(BA, AC) and rect(AB, BC) respectively. The AI takes a fundamentally different approach: it invokes Proposition 2.1 (the distributive property of rectangles over line segments) with both lines set equal to AB, obtaining rect(AB, AB) = rect(AB, AC) + rect(AB, CB), then identifies rect(AB, AB) with sq(AB) by definition. The key intermediate conclusions differ entirely -- Heath's central step is the geometric decomposition via a parallel line, while the AI's central step is the algebraic application of 2.1. Since these represent genuinely different logical backbones (Case B in Q2), Q3 was applied: the AI's path is logically complete and valid, so the classification is D.

### 2.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as D (path difference). Heath's proof constructs a square CDEB on CB (I.46), draws a parallel line AF (I.31), and then decomposes the resulting rectangle AE into sub-rectangles AD and CE, identifying each with the required terms. The AI takes a fundamentally different approach by recognizing 2.3 as a direct corollary of Proposition 2.1: it treats AB and BC as two straight lines where AB is cut at C, applies 2.1 to get rect(AB,BC) = rect(AC,BC) + rect(CB,BC), and then identifies rect(CB,BC) as the square on BC by definition. The proof-tree containment test was applied since the AI cites 2.1 as a higher-level proposition and heath_only contains {1.31, 1.46}. While 1.31 appears in Heath's proof of 2.1, 1.46 does not, so containment fails. The key intermediate conclusions differ: Heath's backbone is geometric area decomposition of a constructed figure, while the AI's backbone is algebraic application of 2.1. The AI's path is logically valid (2.1 is correctly applied, the identification of rect(CB,BC) with sq(BC) is sound), yielding a valid different path.

### 2.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs the square ADEB on AB, draws parallels, and geometrically decomposes it into four areas (two smaller squares HF and KC on segments AC and CB, plus two rectangles AG and GE each equal to rect(AC,CB)), using Book 1 propositions about parallel lines, angle equality, and parallelograms (1.29, 1.31, 1.34, 1.46, 1.5, 1.6). The AI proof takes a completely different algebraic path: it applies Proposition 2.3 twice (once for each segment) to get rect(AB,AC) = rect(AC,CB) + sq(AC) and rect(AB,CB) = rect(CB,AC) + sq(CB), adds these equations via CN2, then substitutes using 2.2 (which states rect(AB,AC) + rect(AB,CB) = sq(AB)) via CN1 to reach the conclusion. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different: Heath identifies geometric sub-regions within a constructed figure, while the AI manipulates algebraic identities from earlier Book 2 propositions. Both paths are logically complete and valid, making this a genuine path difference.

### 2.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof is geometric-constructive: it builds a square on CB (1.46), draws parallels (1.31), uses the complement theorem (1.43) and area equivalence (1.36) to establish the identity through gnomons and area rearrangement. The AI proof is algebraic: it applies 2.4 to expand sq(CB), uses 2.3 and 2.1 to decompose rect(AD, DB), then combines these results through substitution and Common Notions to reach the same conclusion. The two proofs share zero citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different — Heath argues through complements and gnomons while the AI argues through algebraic identities from earlier Book 2 propositions. This is a clear Case B (different backbone) in Q2. The AI's algebraic chain is logically complete and sound (Q3(b) holds), so the classification is D.

### 2.6
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: constructing square CEFD on CD, drawing parallels, establishing AL = CH (I.36), CH = HF (I.43), deriving AL = HF by transitivity, identifying the gnomon as equal to rect(AD,DB), and adding sq(CB) to both sides to reach the conclusion. The ai_only set {CN1, CN2, P1} consists entirely of common notions and a postulate that Heath uses implicitly but the AI cites explicitly: CN1 for the transitive step AL = HF, CN2 for the addition step, and P1 for drawing the diagonal. The heath_only set is empty. This is Case A of Q2 -- same backbone with different citation depth, where the AI over-cites foundational axioms that Heath leaves implicit.

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 2.7 uses a geometric gnomon approach: constructing square ADEB on AB (I.46), applying I.43 (complements about the diagonal are equal) to establish AG = GE, then working through the gnomon KLM and square areas to reach the conclusion. The AI proof takes a fundamentally different algebraic path: it applies 2.4 to expand sq(AB) into sq(AC) + sq(CB) + 2*rect(AC,CB), then applies 2.3 to show rect(AB,CB) = rect(AC,CB) + sq(CB), and combines these via CN1 and CN2 to reach the same conclusion. The key intermediate conclusions are entirely different — Heath argues through gnomons and area complements while the AI argues through algebraic identities from earlier Book 2 propositions. The proof-tree containment test confirms this is not mere citation-depth difference: I.43, which is central to Heath's proof, does not appear inside the proofs of either 2.3 or 2.4, so the AI's route is genuinely independent. The AI's algebraic chain is logically complete and valid (Q3(b) holds), so the classification is D.

### 2.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 2.8 works geometrically by constructing a square on AD, then using properties of parallelogram complements (I.43) and parallelograms on equal bases (I.36) to show that eight sub-areas forming a gnomon are quadruple of the rectangle AK, then adding the square on AC to obtain the full square on AD. The AI proof takes an entirely different algebraic route: it applies 2.4 twice to expand sq(AD) and sq(CD), uses 2.1 to decompose rect(AC,CD), then applies 2.3 to relate rect(AB,CB) to rect(AC,CB) + sq(CB), combining these to reach the same conclusion. The key intermediate conclusions are completely different — Heath passes through gnomon areas and complement equalities, while the AI passes through algebraic decomposition identities from earlier Book 2 propositions. The citation sets are fully disjoint (Jaccard = 0.0), confirming genuinely different proof strategies. The AI proof is logically complete and sound throughout, so Q3(b) holds, yielding category D.

### 2.9
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct CE perpendicular to AB and equal to AC/CB, join lines, draw parallels, establish half-right-angle properties in isosceles right triangles ACE and ECB, show EG=GF via I.6 in triangle EGF, show FD=DB via I.6, identify GF=CD via I.34, then apply the Pythagorean theorem (I.47) three times to conclude sq(AE)=2*sq(AC), sq(EF)=2*sq(CD), and combine via sq(AF) expressed two ways. The AI proof is a superset of Heath's citations: heath_only is empty, and ai_only consists entirely of construction propositions (1.11, 1.3, 1.31), foundational references (1.13, 1.5, CN1, P1) that Heath uses implicitly without citing. This is a clear Case A granularity difference where the AI over-cites construction and axiomatic steps.

### 2.10
**Category**: Path difference
**Jaccard**: 0.053
**Analysis**: Q2 decided the classification. Heath's proof constructs a geometric figure with perpendiculars (I.11), parallels (I.31), and uses isosceles triangle properties (I.5, I.6) and the Pythagorean theorem (I.47) four times to establish the result through geometric relationships in a constructed figure. The AI proof takes an entirely different algebraic route, applying three earlier Book 2 identities (2.7, 2.6, 2.4) and combining them via algebraic manipulation with common notions to reach the same conclusion. The key intermediate conclusions are completely different: Heath establishes that sq(EA) = 2*sq(AC) and sq(EG) = 2*sq(CD) via right triangles, while the AI establishes rect(AD,DB) = sq(CD) - sq(AC) and sq(AB) = 4*sq(AC) via rectangle identities. The Jaccard similarity of 0.053 (only CN1 shared) reflects this fundamental divergence in proof strategy. The AI proof is logically complete and valid, with each step correctly applying its cited proposition.

### 2.11
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Both proofs share the same construction and the same first four key intermediate conclusions through rect(CF,FA) = sq(AB), established via 2.6, I.47, and subtraction. However, the proofs diverge fundamentally after this point. Heath completes the proof by geometric rectangle identification within the diagram (FK = AD, subtracting AK to get FH = HD, then identifying HD = rect(AB,BH) and FH = sq(AH)). The AI instead takes an algebraic route: it uses 2.3 to decompose rect(CF,FA) into rect(AB,AH) + sq(AH), and 2.2 to decompose sq(AB) into rect(AB,AH) + rect(AB,HB), then equates and subtracts to reach sq(AH) = rect(AB,HB). These are genuinely different backbones from step 4 onward — the AI never establishes Heath's key intermediates FK = AD or FH = HD, and Heath never invokes 2.2 or 2.3. Q2 Case B applies, and Q3 confirms the AI's algebraic path is logically complete and valid, yielding classification D.

### 2.12
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: apply II.4 to the line composed of two segments (one side and the external segment cut off by the perpendicular), add the square on the perpendicular to both sides, then use I.47 twice on the two right triangles formed by the perpendicular to substitute and reach the conclusion. The key intermediate conclusions are identical in both proofs despite different vertex labeling. The AI's extra citations (1.12 for drawing the perpendicular, D1.11 for the obtuse angle definition, P2 for producing a line, CN1 and CN2 for equality operations) are all construction-level, definitional, or common-notion citations that Heath uses implicitly but does not cite explicitly. Since heath_only is empty and ai_only contains only over-citations at a finer granularity level, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 2.13
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification. Both proofs follow the same logical backbone: drop a perpendicular from vertex A to the opposite side BC, apply II.7 to the line BC cut at the foot D, apply I.47 twice to the two right triangles formed (ADB and ADC), then combine via addition and substitution to reach the conclusion. The AI proof differs only in explicitly citing construction references (1.12 for drawing the perpendicular), common notions (CN1, CN2, CN3 for equality manipulations), and definitions (D1.10, D1.11, D1.12, D1.21 for right angles, obtuse angles, acute angles, and acute-angled triangles) that Heath leaves implicit. Since heath_only is empty and all ai_only items are construction props, common notions, and definitions, this is a clear Case A (same backbone, different citation depth), yielding G.

### 2.14
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: construct a rectangle equal to the given figure (I.45), extend one side and bisect (creating the semicircle construction), apply II.5 to relate the rectangle to squares, use I.47 (Pythagorean theorem) on triangle GEH, and subtract the common square on GE to conclude that the rectangle equals the square on EH. The AI proof cites 14 references while Heath cites only 3, but the ai_only set consists entirely of construction propositions (1.3, 1.10, 1.46), postulates (P1, P2, P3), common notions (CN1, CN3), and definitions (D1.15, D1.17, D2.1) — all foundational-level citations that Heath uses implicitly without explicit reference. The heath_only set is empty, confirming that the AI covers everything Heath does and more. Since the key intermediate conclusions are identical and the citation difference is purely one of depth (over-citation by the AI of foundational steps), this is a granularity difference.


## Book 3

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 29 |
| Path difference (D) | 8 |
| AI proof error (E) | 0 |

**Total**: 37 propositions

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


## Book 4

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 14 |
| Path difference (D) | 2 |
| AI proof error (E) | 0 |

**Total**: 16 propositions

### 4.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: draw a diameter BC, handle the trivial case where BC equals D, then for the main case cut off a segment CE equal to D, draw a circle with center C and radius CE, join C to the intersection point on the given circle, and conclude by the definition of circle that the new chord equals CE and hence D. Heath's proof cites no references at all, while the AI explicitly cites 1.3 (cutting off equal segments), CN1 (transitivity of equality), D1.15 (definition of circle), D1.17 (definition of diameter), D4.7 (definition of fitting a line in a circle), P1 (joining points), and P3 (drawing a circle). All ai_only items are definitions, common notions, postulates, or a basic construction proposition, representing over-citation of steps Heath treats as implicit. Since the key intermediate conclusions are identical and only citation depth differs, this is a granularity difference.

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct a tangent at point A on the circle, construct two angles at A equal to the angles of the given triangle using I.23, join BC to form the inscribed triangle, apply the alternate segment theorem (III.32) to establish that two angles of the inscribed triangle equal two angles of the given triangle, then conclude the third angles are equal via I.32. The AI proof cites the same core propositions as Heath (1.23, 1.32, 3.16, 3.32) but adds over-citations: 3.17 alongside 3.16 for tangent construction, P1 for joining BC, D4.3 for the definition of an inscribed triangle, and CN1/CN3 for explicit common notion invocations. Heath's citation set is a proper subset of the AI's, with heath_only empty. Since the key intermediate conclusions are identical and the differences are purely in citation depth, this is a granularity difference.

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing angles at the centre equal to the exterior angles of the given triangle, establishing right angles at tangent points via III.18, using quadrilateral angle sums to show each angle of the circumscribed triangle equals the corresponding angle of the given triangle, and concluding the third angle equality via I.32. The citation differences are purely about depth: the AI over-cites by explicitly invoking CN1, CN3, D4.4, and P2 for foundational steps that Heath leaves implicit, while Heath cites III.1 for finding the circle's centre, which the AI treats as given. No key intermediate conclusion differs between the proofs.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: bisect two angles of the triangle to find the incenter D, drop perpendiculars DE, DF, DG to the three sides, prove DE=DF and DF=DG via I.26 triangle congruence, conclude all three distances are equal, construct the circle with center D, and show tangency via III.16. The ai_only set {1.12, CN1, D1.15, P3} consists entirely of a construction proposition (I.12 for drawing perpendiculars), a common notion (CN1 for transitivity of equality), a definition (D1.15 for the circle), and a postulate (P3 for describing a circle) -- all foundational items that Heath uses implicitly without citation. The heath_only set is empty, confirming no substantive propositions are missing from the AI proof. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: bisect AB and AC, draw perpendicular bisectors, analyze three cases (meeting inside, on BC, or outside the triangle), prove FA=FB and FA=FC via SAS congruence (I.4), conclude FA=FB=FC, and describe the circumscribed circle. The AI's additional citations (1.11, CN1, D1.10, D1.15, D4.6, P1, P3) are all construction propositions, definitions, common notions, and postulates that Heath uses implicitly but does not cite. The heath_only set is empty, confirming the AI omits nothing Heath cites. This is a clear Case A same-backbone, different-depth scenario yielding G.

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) construct two perpendicular diameters and join endpoints, (2) prove ABCD equilateral via I.4 using equal radii and right angles at the center, (3) prove ABCD right-angled via III.31 (angles in semicircles are right), and (4) conclude ABCD is a square by the definition of a square (I.Def.22/D1.22). The AI proof cites all three of Heath's references (1.4, 3.31, D1.22) and adds six more (3.1, 1.11, 1.15, D1.15, D4.3, P1), all of which are construction propositions, postulates, or definitions that make explicit the steps Heath leaves implicit. Heath_only is empty, confirming the AI covers everything Heath does. This is Case A of Q2: same backbone with different citation depth, yielding a granularity difference.

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same logical backbone: draw perpendicular diameters, construct tangent lines at the endpoints, establish perpendicularity of tangents to radii (III.18), prove opposite sides of the circumscribed figure are parallel (I.28), show all four corner angles are right angles, show all four sides are equal, and conclude the figure is a square. The ai_only items are predominantly over-citations: construction props (1.11), postulates (P1), common notions (CN1, CN2), and definitions (D1.15, D1.22, D4.4). The substantive ai_only citation 1.32 (triangle angle sum) is used where Heath uses 1.34 (parallelogram properties) to establish the same key conclusion that the corner angles are right angles -- a different tool for the same intermediate result. The heath_only item 1.30 (transitivity of parallelism) is not needed by the AI because it establishes parallelism of opposite sides directly via I.28 (both perpendicular to the same diameter), rather than Heath's two-step route through an intermediate parallel. These are citation-depth differences, not backbone differences.

### 4.8
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: start with the given square, find the center by bisecting sides and drawing parallels, establish four equal distances from the center to the midpoints of the sides, show right angles at each tangent point, then describe the circle and invoke III.16 to prove tangency rather than intersection. The AI proof is more explicit in its citations, adding 1.29 (for deriving right angles from parallel lines), 1.33 (for establishing parallelograms), and several definitions (D1.15, D1.22, D4.5), common notions (CN1), and postulates (P1, P3) that Heath uses implicitly. Since heath_only is empty, every citation Heath makes is also made by the AI, and the ai_only items are all either sub-steps of the same argument or foundational references cited explicitly by the AI but left implicit by Heath. The key intermediate conclusions are identical in both proofs, confirming Case A of Q2.

### 4.9
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 reveals a genuinely different backbone between the two proofs, leading to classification D. Heath's proof establishes that each angle of the square is bisected by a diagonal using I.8 (SSS congruence), then uses I.6 to conclude EA = EB from the equal half-angles, and similarly for all four segments. The AI proof takes an entirely different route: it first establishes that opposite sides of the square are parallel (1.28), then uses alternate angles (1.29) and ASA congruence (1.26) to show triangle AEB is congruent to triangle CED, yielding EA = EC and EB = ED. Separately, it analyzes the angles via isosceles triangle properties (1.5) and the angle sum theorem (1.32) to show EA = EB via I.6. The proof-tree containment test confirms that I.8 (the sole heath_only item) does not appear in the proof of any AI-cited proposition such as 1.26, so the divergence is not a matter of citation depth but a genuinely different logical path. The AI's path is logically complete and valid, satisfying Q3(b).

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.583
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing AB cut at C via II.11, fitting BD = AC in the circle via IV.1, circumscribing circle ACD via IV.5, establishing BD as tangent to circle ACD via III.37, deriving angle BDC = angle DAC via III.32, showing the three base-related angles are equal, deriving BD = DC via I.6, and concluding DC = CA so each base angle is double the vertex angle. The AI proof uses explicit algebraic notation (phi, psi) and applies angle-sum (I.32) and supplementary angle (I.13) arguments more explicitly, while Heath uses geometric narrative. The ai_only set consists entirely of construction postulates (P1, P3), a construction proposition (4.1), a definition (D1.20), and a basic angle fact (1.13) that Heath uses implicitly without citing. Since heath_only is empty and all ai_only items are over-citations of construction steps, axioms, and definitions rather than substantive alternative propositions, this is Case A of Q2: same backbone with different citation depth, yielding Granularity difference.

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct isosceles triangle FGH (4.10), inscribe equiangular triangle ACD in the circle (4.2), bisect the base angles with 1.9 to produce five equal angles, use 3.26 to get five equal arcs, use 3.29 to get five equal chords (equilateral), then use 3.27 with equal arcs to prove equiangular. The AI adds four citations not in Heath: 1.32 (used in Step 5 to explicitly compute that each of the five equal angles is one-fifth of two right angles, a calculation Heath omits), CN2 (explicitly cited where Heath implicitly uses it when adding arcs), and D4.3/D4.7 (definitions cited in the concluding remark). All ai_only items represent deeper citation of steps Heath leaves implicit or definitions Heath does not cite, while heath_only is empty. This is Case A of Q2: same backbone, different citation depth, yielding Granularity difference.

### 4.12
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 determines the classification. Heath's proof draws tangent lines at the vertices A, B, C, D, E of the inscribed regular pentagon and uses III.1 to find the center, then proves the circumscribed pentagon equilateral and equiangular through Pythagorean arguments and triangle congruence at those contact points. The AI proof takes a structurally different approach: it bisects each arc of the inscribed pentagon using 3.30, draws tangents at those arc midpoints, then uses angle sums of quadrilaterals (1.32) and equal-arc arguments (3.26, 3.27) to establish equiangularity, and congruent triangles to establish equilaterality. The tangent points differ (arc midpoints vs. vertices), the construction differs (arc bisection vs. center-finding), and the equiangularity argument differs (quadrilateral angle sum vs. doubled angle pairs). These are genuinely different backbones, not mere citation-depth variations. Under Q3, the AI's alternative path is logically complete: the chain from inscribed pentagon through arc bisection, tangent construction, equal arcs, equal central angles, equal vertex angles, and equal tangent segments to the equilateral-and-equiangular conclusion is sound throughout.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow identical logical backbones: bisect two angles of the regular pentagon to locate center F, use I.4 to prove triangle congruences establishing that all five angles are bisected by lines from F, drop perpendiculars from F to all five sides, use I.26 to show all perpendiculars are equal, describe a circle with center F and that common perpendicular distance as radius, and invoke III.16 to show the circle is tangent to each side. The AI proof cites the same three substantive propositions as Heath (I.4, I.26, III.16) and adds seven additional foundational references: construction propositions (1.9 for angle bisection, 1.12 for dropping perpendiculars), postulates (P1, P3, P4), a common notion (CN1), and a definition (D4.5). Heath leaves these construction steps and axioms implicit. The empty heath_only set confirms no substantive proposition is missing from the AI proof. This is a clear case of same backbone with different citation depth.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect angles BCD and CDE to locate center F, prove all five distances FA=FB=FC=FD=FE are equal, and circumscribe the circle. The AI proof is substantially more detailed than Heath's, explicitly working through SAS congruences (I.4) where Heath uses 'similarly it can be proved' and 'in manner similar to the preceding'. The ai_only set consists entirely of over-citations: I.4 (basic SAS congruence used to establish equal distances), I.9 (angle bisection construction), CN1 (transitivity of equality), P1 (joining lines), P3 (drawing circles), and D4.6 (definition of circumscribed circle). Heath's sole citation of I.6 is also used by the AI. The heath_only set is empty. This is a clear case of the AI providing a more granular, explicit proof of the same argument that Heath presents in compressed form.

### 4.15
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct equilateral triangles at the center to establish that all six central angles equal one-third of two right angles, then use III.26 to get equal arcs, III.29 for equal sides (equilateral), and III.27 for equal inscribed angles (equiangular). The proofs differ only in the sub-method used to establish all six central angles as equal. Heath proves three angles directly via two equilateral triangles (EGD, DGC) and supplementary angles, then applies I.15 (vertical angles) to obtain the other three. The AI instead constructs an additional circle centered at A (beyond Heath's circle at D), directly proving four equilateral triangles (EGD, DGC, AGB, AGF) and then uses I.13 (supplementary angles on a line) to derive the remaining two angles (BGC, FGE) by subtraction. This substitution of I.13 for I.15 represents a minor variation in the sub-argument for one key step, not a different backbone. The ai_only set consists entirely of definitions, postulates, common notions, and proposition I.13 — all representing over-citation or the I.13-for-I.15 substitution. The key intermediate conclusions are identical in both proofs.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: inscribe an equilateral triangle side (arc AC = 1/3 circle) and a regular pentagon side (arc AB = 1/5 circle), compute arc BC = 2/15 circle, bisect BC at E via III.30 to get arcs of 1/15 each, then fit equal chords around the circle to complete the 15-gon. The AI proof explicitly cites 4.2 and 4.11 for the triangle and pentagon constructions that Heath performs without citation, cites P1 for joining points, 4.1 for fitting chords, and 3.29 and 3.27 to justify that equal arcs yield equal chords (equilateral) and equal inscribed angles (equiangular) — conclusions Heath simply asserts. All ai_only items (3.27, 3.29, 4.1, 4.11, 4.2, P1) are over-citations making explicit what Heath leaves implicit, while heath_only is empty. This is a clear Case A: same backbone, different citation depth.


## Book 5

| Category | Count |
|---|---|
| Perfect match (P) | 2 |
| Granularity difference (G) | 17 |
| Path difference (D) | 6 |
| AI proof error (E) | 0 |

**Total**: 25 propositions

### 5.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification as G (Granularity difference). Heath's proof of 5.1 cites no references (heath_refs is empty), working entirely from first principles and the definition of equimultiples. The AI proof establishes the same type of result using the same fundamental method -- decomposing multiples into unit parts and manipulating them -- but explicitly cites CN2 (equals added to equals), CN3 (equals subtracted from equals), D5.1, and D5.2 (definition of multiple). These are all common notions and definitions that Heath invokes implicitly without formal citation. The ai_only set contains exclusively axioms and definitions (CN2, CN3, D5.1, D5.2) with no substantive propositions, which is the hallmark of over-citation at a finer granularity. No forward dependencies were found. No logical errors were identified in the AI proof under the hardened 1(b) standard. The Jaccard similarity is 0.0 because Heath has no citations while the AI has four, but this reflects citation-depth difference rather than a genuine path divergence.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: decompose the first pair of equimultiples into equal parts, decompose the second pair into equal parts, then combine them to show the sums contain the same count of equal parts. The AI's key intermediate conclusions match Heath's exactly. The only difference is citation depth: Heath's proof uses no explicit citations (his reference list is empty), while the AI explicitly cites D5.2 (definition of equimultiple) and CN2 (Common Notion 2, addition of equals). Both of these are foundational items (a definition and a common notion) that Heath uses implicitly. This is a textbook Case A granularity difference: same backbone, the AI is simply more explicit about its definitional and axiomatic foundations.

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: decompose the equimultiples into parts equal to A and C respectively, observe that each part is the same multiple of B (or D) by hypothesis, then apply Proposition 5.2 to combine the parts and conclude that the total equimultiples are equimultiples of B and D. The only citation difference is that the AI explicitly cites Definition 5.2 (D5.2) when establishing the equimultiple relationships, while Heath uses the concept implicitly without citing the definition. This is a citation-depth difference (over-citation of a definition), not a backbone difference, placing this squarely in Case A of Q2.

### 5.4
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take arbitrary equimultiples of the given equimultiples, use Proposition 5.3 to collapse double equimultiples into single equimultiples of the original magnitudes, apply Definition 5.5 to the hypothesis A:B :: C:D with these collapsed equimultiples to obtain the three-way exceed/equal/less-than comparison, then apply Definition 5.5 a second time to conclude the desired ratio. The only citation difference is that the AI explicitly cites D5.2 (the definition of equimultiple), which Heath leaves implicit. Since D5.2 is a non-substantive definition and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference under Q2 Case A, yielding G.

### 5.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they use Proposition 5.1 as the central tool to combine multiples, then use algebraic manipulation (subtraction of equal parts) to isolate the remainder EB and show it is the same multiple of FD as AB is of CD. The AI's ai_only citations (CN1, CN3, D5.2) are exclusively common notions and a definition that Heath uses implicitly without citing. Heath implicitly applies CN3 when subtracting CF from both GF and CD, implicitly uses CN1 when equating magnitudes that are both equal to the same multiple, and implicitly relies on D5.2 (the definition of equimultiple) without citing it. The AI merely makes these implicit steps explicit, which is a citation-depth difference, not a path difference. The heath_only set is empty, confirming no substantive proposition is missing from the AI proof.

### 5.6
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they show that the subtracted equimultiple plus the remainder equals the original equimultiple (using 5.2), then subtract to isolate the remainder, and finally split into two cases (remainder equals the magnitude, or remainder is a proper equimultiple). The AI uses algebraic multiplier notation while Heath uses geometric construction with named magnitudes, but the logical backbone is identical. The ai_only set consists entirely of common notions (CN3, CN5) and a definition (D5.2), which are axiom-level items that Heath uses implicitly without citing. Since heath_only is empty and all ai_only items are non-substantive over-citations, this is a citation-depth difference with the same backbone, yielding G.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: for each of the two parts (A:C=B:C and C:A=C:B), they take equimultiples, derive equality of the equimultiples from A=B, apply the trichotomy comparison, and conclude via Definition 5.5. The AI proof explicitly cites CN1 (equals compared to the same yield the same relation), CN2 (equals added to equals yield equals, used to justify that equimultiples of equal magnitudes are equal), and D5.2 (definition of equimultiple), all of which Heath uses implicitly without citation. The heath_only set is empty, confirming no substantive divergence. This is a clear case of same backbone with different citation depth, classifying as G.

### 5.8
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof constructs equimultiples of AB and C (via splitting AB into AE and EB with BE=C) compared against successive multiples of an arbitrary third magnitude D, requiring two cases depending on whether AE is less or greater than EB. The AI proof takes a fundamentally different approach: it defines D as the excess A minus B, chooses m so that mD exceeds C via the Archimedean property (D5.4), then uses 5.1 to express mA as mB plus mD, and selects n as the greatest integer with nC not exceeding mB. This single unified construction avoids case analysis entirely and directly produces multipliers satisfying D5.7 for both parts of the proposition. The key intermediate conclusions differ structurally: Heath establishes that FH exceeds N while K does not exceed N (where FH and K are equimultiples of AB and C, and N is a multiple of D), whereas the AI establishes that mA exceeds (n+1)C while mB does not exceed (n+1)C. Both paths are logically complete but arrive at the D5.7 application through genuinely different constructions and intermediate facts.

### 5.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the identical logical backbone: a two-case proof by contradiction, where each case assumes A is not equal to B and derives a contradiction using Proposition 5.8, which states that the greater magnitude has a greater ratio. The AI proof and Heath's proof establish the same key intermediate conclusions in the same order for both parts of the proposition. The only difference is that the AI explicitly cites Definition 5.5 (same ratio) and Definition 5.7 (greater ratio) to clarify the notions being used, whereas Heath invokes these definitions implicitly. Since ai_only contains only definitions (D5.5, D5.7) and heath_only is empty, this is a case of over-citation by the AI at the definitional level, which is a citation-depth difference rather than a path difference.

### 5.10
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decides: both proofs argue through identical key intermediate conclusions across both required parts of this two-case proposition. Part 1 (A:C > B:C implies A > B) and Part 2 (C:B > C:A implies B < A) each proceed by proof by contradiction, eliminating the equality case via V.7/5.7 and the wrong-inequality case via V.8/5.8. The logical backbone is the same in both proofs. The only citation difference is that the AI explicitly cites D5.7 (the definition of greater ratio) when setting up its hypotheses, while Heath uses the concept implicitly. Since D5.7 is a definition and the ai_only set contains only this definitional over-citation with an empty heath_only set, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone: take equimultiples of A, C, E by the same multiplier and equimultiples of B, D, F by the same multiplier; from A:B :: C:D deduce that the comparison of mA vs nB determines the comparison of mC vs nD; from C:D :: E:F deduce that the comparison of mC vs nD determines the comparison of mE vs nF; chain these to conclude that mA vs nB determines mE vs nF; and conclude A:B :: E:F by the definition of proportionality. The only citation difference is that the AI explicitly cites D5.5 (Definition V.5 of equal ratios) while Heath applies the same definition implicitly without a formal citation. This is a classic over-citation of a foundational definition, making the proofs identical in substance but different in citation depth.

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: take equimultiples G, H, K of the antecedents A, C, E and equimultiples L, M, N of the consequents B, D, F; use the proportionality hypothesis with D5.5 to establish that G, H, K simultaneously exceed, equal, or fall short of L, M, N; combine these to show G+H+K simultaneously exceeds, equals, or falls short of L+M+N; establish that G+H+K is the same multiple of A+C+E as G is of A (and similarly for the consequents); then conclude by D5.5. The only difference is citation depth: Heath cites 5.1 as a packaged result for the step that combines equimultiples into a single multiple of the sum, while the AI derives this same fact inline using CN2 (addition axiom) and D5.2 (definition of equimultiples). The ai_only items (CN2, D5.2, D5.6) are all definitions and common notions, not substantive theorems, confirming this is a depth-of-citation difference rather than a different proof path.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs establish the same key intermediate conclusions using the same citation set {D5.5, D5.7}. The logical backbone is identical: (1) apply D5.7 to obtain equimultiples of C,E and D,F where the multiple of C exceeds the multiple of D but the multiple of E does not exceed the multiple of F; (2) form corresponding equimultiples of A and B; (3) apply D5.5 to conclude that since A:B :: C:D and the multiple of C exceeds the multiple of D, the multiple of A exceeds the multiple of B; (4) apply D5.7 to conclude A:B > E:F. Since both the key conclusions and the citation sets are identical, this is a perfect match.

### 5.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Heath's proof of 5.14 explicitly proves only Case 1 (A > C) using 5.8, 5.13, and 5.10, then handles Cases 2 (A = C) and 3 (A < C) with 'similarly we can prove.' The AI proof establishes the identical backbone for Case 1 — A:B > C:B by 5.8, then C:D > C:B by 5.13, then D < B by 5.10 — but goes further by explicitly proving the other two cases: Case 2 uses 5.7, 5.11, and 5.9, and Case 3 mirrors Case 1 with 5.8, 5.13, and 5.10. The ai_only citations (5.7, 5.9, 5.11, D5.5) are entirely attributable to the AI's greater explicitness in proving cases Heath leaves implicit and citing the definition for the ratio hypothesis. With heath_only empty and the key logical backbone identical for the explicitly proved case, this is a same-backbone, different-depth situation characteristic of G.

### 5.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof divides the multiples AB and DE into parts equal to C and F respectively, then uses V.7 (equal magnitudes have the same ratio) to establish proportionality among corresponding parts, and V.12 (as one antecedent to one consequent, so all antecedents to all consequents) to recombine. The AI proof takes a fundamentally different approach: it goes directly to Definition 5.5's criterion for ratio equality, uses V.5.3 to show commutativity of iterated multiples (nC = m(nA) and pD = m(pB)), then verifies all three order cases using CN2 and CN5. The proof-tree containment test confirms the divergence: neither 5.7 nor 5.12 (Heath's key citations) appears in the proof tree of any AI-cited proposition. The backbones are entirely different, making this Case B. Q3 confirms the AI's path is logically valid and complete, yielding classification D.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: take equimultiples of A,B and C,D, use V.15 to relate each pair's ratio to the original ratio, chain via V.11 with the hypothesis to equate the equimultiple ratios, apply V.14 for trichotomy, and conclude by D5.5. The AI's only extra citation is D5.12 (a definition about magnitudes of the same kind), which is a purely definitional over-citation that Heath leaves implicit. Since the key intermediate conclusions are the same in both proofs and the citation difference is limited to a single definition, this is a granularity difference (Case A of Q2).

### 5.17
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) construct equimultiples and use 5.1 to form multiples of the composite magnitudes AB and CD, (2) use 5.2 to form combined equimultiples of EB and FD, (3) apply the proportion hypothesis to get the excess/equal/less trichotomy, (4) subtract common quantities to transfer the condition to the component parts AE vs EB and CF vs FD, and (5) conclude by the definition of proportion. The ai_only citations CN3, D5.14, D5.15, and D5.5 are all definitions and common notions that Heath uses implicitly without explicit citation. The AI makes these foundational references explicit, which is a citation-depth difference, not a structural divergence. Since heath_only is empty and all ai_only items are axiom-level over-citations, this is a clear Case A granularity difference.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this classification as D (path difference). Heath proves 5.18 by contradiction: assuming the componendo proportion fails, he applies 5.17 (the converse, separando from componendo), then 5.11 (transitivity of ratios) and 5.14 (order-preserving property of equal ratios) to derive a contradiction. The AI proof takes an entirely different approach, working directly from the equimultiple definition of proportion (D5.5). It uses 5.1 to distribute multiples over sums, then breaks into cases based on whether n > m or n <= m, verifying the equimultiple condition in each case using the hypothesis and common notions. The two proofs share zero citations (Jaccard = 0.0) and have completely different logical backbones: Heath's contradiction via the converse versus the AI's direct definitional verification. The AI's path is logically sound and complete, satisfying Q3, so the classification is D.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: both start from the hypothesis AB:CD = AE:CF, apply alternation (5.16) to obtain AB:AE = CD:CF, then apply separando (5.17) to get EB:AE = FD:CF, then alternate again (5.16) to obtain EB:FD = AE:CF, and finally use transitivity (5.11) to conclude EB:FD = AB:CD. The citation sets are exactly identical at {5.11, 5.16, 5.17} with Jaccard similarity 1.0, and the key intermediate conclusions match at every stage, satisfying the perfect match criteria.

### 5.20
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 determines the classification. Heath's proof of the A>C case establishes D:E > F:E by combining both given proportions with 5.13 (using the inverse), then concludes D > F via 5.10 (greater ratio to the same implies greater magnitude). The AI proof instead uses 5.13 only to get D:E > C:B, then drops to definition-level equimultiple reasoning (D5.7, D5.5) to establish D > F directly without ever forming the comparison D:E > F:E or citing 5.10. The heath_only citation 5.10 does not appear inside Heath's proofs of any AI-cited proposition, so the proof-tree containment test fails and this is not a granularity difference. Furthermore, for the A=C case, Heath says 'similarly we can prove' while the AI uses an entirely different proof by contradiction approach via 5.7 and 5.11. These constitute genuinely different logical backbones. The AI's path is logically complete and valid throughout all three cases, so Q3 yields D.

### 5.21
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone for Case I (A > C): deriving A:B > C:B from A > C via 5.8, obtaining E:F > E:D via 5.13 and the inverse ratio, then concluding D > F via 5.10. Heath dismisses Cases II and III with 'similarly,' while the AI proves all three cases explicitly, which accounts for the ai_only propositions 5.7, 5.9, and 5.11 (used in the equal and less-than cases). The remaining ai_only items are definitions (D5.5, D5.13, D5.18) that the AI cites explicitly where Heath leaves them implicit. Since heath_only is empty and all divergences are explained by the AI's greater explicitness rather than a different proof strategy, this is a citation-depth difference, not a path difference.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions for the three-magnitude case: (1) applying V.4 twice to derive ratio relationships among equimultiples, (2) applying V.20 to conclude the ex aequali ordering, and (3) applying V. Def. 5 to conclude A:C = D:F. The AI proof has the same logical backbone as Heath's. The only citation difference is that the AI explicitly cites D5.17 (the definition of ex aequali ratio), which Heath uses implicitly without citation. Since D5.17 is a definition and not a substantive proposition, this is a citation-depth difference. The AI also extends the proof to the general case via induction (Steps 8-12), which Heath omits, but this is additional granularity rather than a different path. Case A of Q2 holds, yielding G.

### 5.23
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decides the classification as D (path difference). The two proofs use fundamentally different equimultiple groupings: Heath takes G, H as equimultiples of A, B and K of D (first group), with L, M of C, E and N of F (second group), then uses alternation (5.16) twice as a key technique to establish H:L = K:M. The AI instead takes G, H, K as equimultiples of A, D, E and L, M, N of B, C, F, then uses 5.4 to directly derive G:L = K:N from A:B = E:F across the two multiplier groups. This leads to different intermediate conclusions: Heath establishes G:H = M:N and H:L = K:M before applying 5.21, while the AI establishes G:L = K:N and L:M = H:K before applying 5.21 to a differently-constituted set of six magnitudes. The containment test confirms this is genuine path divergence since 5.16 (heath_only) does not appear inside Heath's proof of 5.4 (ai_only). The AI's alternative path is logically valid throughout, with each step properly justified by cited propositions.

### 5.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: (1) invert one given ratio, (2) apply ex aequali (5.22) to combine with the other given ratio, (3) apply componendo (5.18), and (4) apply ex aequali (5.22) again to reach the final conclusion. The AI's only extra citations are D5.5 and D5.13, which are definitions used to explicitly justify the inversion step that Heath performs without citing a definitional basis. Since heath_only is empty and the ai_only items are purely definitional over-citations, this is a clear Case A granularity difference with the same backbone at different citation depth.

### 5.25
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs auxiliary magnitudes AG=E and CH=F, then applies V.19 (the remainder proposition) to establish GB:HD :: AB:CD, deducing GB > HD from AB > CD, and finally combines the equalities AG+F = CH+E with GB > HD to reach AB+F > CD+E. The AI takes a fundamentally different route: it establishes ordering relations (A > B, B > D, C > D) using 5.14 and 5.16, then applies 5.17 (separando) directly to the original proportion to get (A-B):B :: (C-D):D, uses 5.14 to show A-B > C-D, and adds B+D to both sides via CN2. Although 5.16 and 5.17 appear inside Heath's proof of 5.19, the AI does not cite 5.19 and uses these propositions in entirely different logical roles — the AI's key intermediates (establishing G > H where G=A-B, H=C-D) differ from Heath's (establishing GB:HD proportionality via the remainder theorem). This constitutes a genuinely different backbone, confirmed as logically valid at Q3.


## Book 6

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 27 |
| Path difference (D) | 6 |
| AI proof error (E) | 0 |

**Total**: 33 propositions

### 6.1
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: construct equimultiples of bases and triangles, use I.38 to show the equimultiple relationship preserves between bases and triangles, apply V. Def. 5 to conclude the proportion for triangles, then extend to parallelograms via I.41 and V.15. The ai_only set {1.3, 1.39, CN2, P1, P2} consists entirely of construction propositions, postulates, and common notions reflecting the AI's more detailed citation of constructive steps. The heath_only set {5.11} reflects Heath's explicit citation of ratio transitivity, which the AI handles implicitly by chaining equalities in Step 10 without a separate citation. Since the key intermediate conclusions are identical and all citation differences are matters of depth rather than substance, this is a granularity difference.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: in Part I, they establish the equality of triangles BDE and CDE (via same base DE between same parallels), derive triangle-to-triangle ratios using VI.1, and conclude proportionality via V.11; in Part II, they reverse the argument using V.9 and I.39. The only citation difference is that the AI cites I.37 (triangles on the same base in the same parallels are equal) where Heath cites I.38 (triangles on equal bases in the same parallels are equal). Since triangles BDE and CDE share the literally same base DE, both propositions apply and establish the identical geometric fact. The AI also adds the construction postulate P1 for joining lines, which is an over-citation. These are citation-depth differences with identical key intermediate conclusions, yielding G.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs establish the angle bisector proportion theorem and its converse through identical key intermediate conclusions: constructing CE parallel to DA, establishing angle equalities via I.29, deriving that AE equals AC via the isosceles triangle theorem (I.6 forward, I.5 converse), applying proportionality with parallel lines (VI.2), and using ratio properties (V.11, V.9) for the converse. The AI's additional citations (1.31 for parallel construction, P2 for line extension, CN1 for transitivity of equality, and 5.7 for substituting equal magnitudes in a ratio) are all explicit statements of construction steps and axioms that Heath applies implicitly. The heath_only set is empty, confirming this is pure over-citation by the AI. Since the logical backbones are the same and the citation differences reflect only depth of explicit justification, this is a granularity difference.

### 6.4
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 determines the classification. Heath constructs a parallelogram by placing BC in line with CE, extending BA and ED to meet at F, establishing FACD as a parallelogram (using I.17, Post.5, I.28, I.34), then derives proportions via VI.2 with alternation (V.16) and ex aequali (V.22). The AI uses a fundamentally different superposition approach: it places triangle DEF onto ABC twice (once at vertex B, once at vertex A), each time establishing a parallel line via I.28, applying VI.2 for proportional segments, then using componendo (5.18) with ratio definitions (D5.13, D5.5) to obtain the desired ratios, and finally combining results via ratio transitivity (5.11). The key intermediate conclusions differ entirely: Heath's backbone runs through parallelogram construction and properties (I.34) with alternation and ex aequali, while the AI's backbone runs through double superposition with componendo and transitivity. Both paths are logically complete and valid, yielding a path difference (D).

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow identical backbones: construct triangle GEF on EF equiangular with ABC (I.23, I.32), use VI.4 for proportionality, then V.11 and V.9 to show DE=GE and DF=GF, and finally SSS congruence to conclude DEF is congruent to GEF and transfer angles. The only citation difference is that Heath uses I.4 alongside I.8 to establish full triangle congruence (I.8 for one angle from three equal sides, then I.4 for the remaining angles and triangle equality), while the AI attributes full SSS congruence to I.8 alone. This is a citation depth difference: the same geometric conclusion (full congruence of DEF and GEF with all corresponding angles equal) appears at the same logical position in both proofs, but the AI compresses the two-step I.8+I.4 inference into a single citation of I.8.

### 6.6
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Heath's proof constructs a triangle DGF equiangular with ABC by copying angles (I.23), then uses VI.4 to derive a proportion, and V.11/V.9 to show ED = DG, leading to congruence of DEF and DGF via I.4. The AI instead constructs a triangle DGH congruent to ABC by marking off equal segments on DE and DF (I.3), then uses the converse of 6.2 to show GH is parallel to EF from the proportional cutting, and I.29 to transfer alternate angles. These are fundamentally different backbones: Heath works through angle-copying, proportional similarity (VI.4), and proportion algebra (V.11, V.9), while the AI works through side-copying, proportional cutting (6.2 converse), and parallel-line angle transfer (I.29). Both paths are logically complete and valid, yielding classification D.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.778
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: assume angle ABC is not equal to angle DEF, construct angle ABG equal to DEF via I.23, show triangles ABG and DEF are equiangular via I.32, derive the proportion AB:BG = DE:EF via VI.4, conclude BG = BC via V.11 and V.9, establish the isosceles triangle via I.5, and reach contradictions in both the less-than-right-angle and not-less-than-right-angle cases. The citation difference is purely one of depth: Heath cites I.17 directly for the Case 2 contradiction (two angles in a triangle are less than two right angles), while the AI derives the same contradiction by working through the angle sums using I.32 and I.13, which are the constituent parts of I.17. The AI additionally cites Postulate 5 to justify that ray BG meets line AC, which is an explicit construction detail Heath leaves implicit. Since the key intermediate conclusions are identical and the differences are limited to citation depth, this is a granularity difference.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: they establish equiangularity of sub-triangles ABD and ADC with the whole triangle ABC using I.32 (angle sum), then derive proportionality of sides via VI.4 and similarity via VI.Def.1, and finally prove mutual similarity of ABD and ADC. The AI proof is more explicit than Heath in two respects: it fully works out the ADC case where Heath says 'similarly we can prove,' and it explicitly cites foundational items (CN1 for transitivity of equality, CN3 for subtraction of equals, D1.10 for the definition of a right angle, and P4 for right angle equality) that Heath uses implicitly. The ai_only set consists entirely of common notions, definitions, and a postulate, which are classic over-citations indicating a granularity difference rather than a path difference. Heath_only is empty, confirming the AI covers all of Heath's reasoning.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a line AC at an angle from A with three equal segments AD=DE=EC, draw a parallel to BC through D, apply VI.2 (6.2) to obtain the proportionality, then use the 2:1 ratio of CD to DA to conclude that the prescribed third part has been cut off. The AI proof cites the same three substantive propositions as Heath (1.3, 1.31, 6.2) and adds only axiom-level items (CN1, CN2, D5.1, P1) that make explicit what Heath leaves implicit. With heath_only empty and ai_only consisting entirely of common notions, a definition, and a postulate, this is a clear case of over-citation at the same backbone, yielding a granularity difference.

### 6.10
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined this classification. Heath's proof constructs a parallelogram by drawing DHK parallel to AB through D, then uses I.34 to establish segment equalities (DH=FG, HK=GB) before applying VI.2 to triangles DKC and AGE. The AI proof takes a fundamentally different approach: it draws only lines parallel to BC (no parallelogram construction), applies VI.2 to triangles AEG and ABC, then uses ratio algebra (5.18 componendo, 5.16 alternando, and CN1 transitivity) to derive the required proportionalities. The key intermediate conclusions differ substantially -- Heath relies on parallelogram equalities while the AI relies on ratio manipulation chains. The AI's path is logically complete and valid, with each step properly justified, so Q3 confirms a valid path difference (D).

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct BD equal to AC, join BC, draw DE parallel to BC, apply VI.2 to obtain AB:BD = AC:CE, then substitute BD = AC to conclude AB:AC = AC:CE. The AI makes the substitution step more explicit by citing 5.7 (equal magnitudes have the same ratio) and 5.11 (transitivity of ratios), whereas Heath performs this substitution informally in a single sentence. The ai_only items P1 and P2 are postulates cited for construction steps (over-citation). Since heath_only is empty and the ai_only items all represent deeper citation of the same reasoning steps rather than a different proof path, this is Case A of Q2: same backbone, different citation depth.

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct lines DE, DF at an angle, mark DG=A, GE=B, DH=C, join GH, draw EF parallel to GH through E (via I.31), apply VI.2/6.2 to conclude DG:GE::DH:HF, then substitute to get A:B::C:HF. The AI's three extra citations (1.3, P1, P2) are all construction-level references and postulates that make explicit the tools used for setting out lines and cutting off equal segments, which Heath leaves implicit. With heath_only empty and ai_only containing only construction/postulate items, this is a clear Case A in Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: place the two lines AB, BC in a straight line, describe a semicircle on AC, draw BD perpendicular to AC, then conclude that angle ADC is right by III.31 and that BD is a mean proportional between AB and BC by VI.8. The AI proof is more explicit in its construction steps (citing 1.10 for bisection, 1.11 for perpendicular construction, P1/P2/P3 for postulates, D1.18 for semicircle definition) and expands the final proportionality step by explicitly citing 6.4 for the proportionality of sides in similar triangles. The proof-tree containment test confirms that 6.4 appears inside Heath's proof of 6.8, so the AI is merely unpacking what Heath cites as a single unit. The heath_only set is empty, meaning Heath cites nothing that the AI does not also cite. All ai_only items are construction propositions, postulates, a definition, or a proposition contained within a cited result, confirming a citation-depth difference rather than a path difference.

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: arranging the equiangular parallelograms so that sides are collinear, completing an auxiliary parallelogram, using VI.1/6.1 to express area ratios as base ratios, applying V.7/5.7 for equal areas having the same ratio to a third magnitude, and using V.11/5.11 for transitivity of ratios, with the converse using V.9/5.9 to conclude equality from equal ratios to the same magnitude. The ai_only set consists entirely of construction and foundational propositions (1.13, 1.30, 1.31, 1.34) and common notions (CN1, CN2) that Heath leaves implicit. For instance, Heath simply states 'let the parallelogram FE be completed' without citing 1.31 or 1.34, and notes collinearity citing only I.14 while the AI explicitly invokes I.13 and I.30 for the supplementary angle and parallel-line arguments. The heath_only set is empty, confirming the AI cites a strict superset of Heath's references. This is a clear Case A: same backbone, different citation depth.

### 6.15
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same logical backbone: arrange the two equal triangles so that CA is collinear with AD and EA is collinear with AB, join BD, use VI.1 to establish ratio relationships between the triangles and their sides, then combine these ratios to reach the conclusion (forward direction: reciprocal proportionality; converse: equality via V.9). The citation differences are purely about depth of justification for identical logical steps. The AI over-cites by including 1.13 (supplementary angles) to explicitly justify the collinearity before applying 1.14, where Heath simply invokes I.14 directly. For the ratio-combining step, Heath uses V.11 (transitivity of ratios) while the AI uses V.7 (equal magnitudes have the same ratio to the same) with informal inversion, but both reach the same intermediate conclusion at the same logical position. Neither 5.11 nor 5.7 contains the other in its proof tree, but both serve the identical role of combining established ratio equalities, making this a citation-depth difference rather than a path difference.

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as G (Granularity difference). Both Heath and the AI prove the biconditional in two parts using the same logical backbone: construct equiangular parallelograms (rectangles) whose sides equal the given lines, establish that the sides about equal angles are reciprocally proportional from the hypothesis, then apply 6.14 to conclude equality of the parallelograms (forward direction) or reciprocal proportionality of sides (converse direction). The ai_only set consists entirely of construction propositions (1.11 for right angles, 1.31 for parallel lines), a definition (D2.1), and postulates (P1, P4) that Heath leaves implicit. Heath cites only 6.14, which the AI also cites. The empty heath_only set confirms no substantive step is missing from the AI proof. This is a clear Case A in Q2: same backbone, different citation depth.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they reduce the three-line proportion to four proportional lines, apply 6.16 to equate the rectangle of the extremes with the rectangle of the means, then identify the rectangle of the means with the square on the middle line. The only difference is that the AI explicitly cites definitions D1.22 and D2.1 to justify that rect(B,B) = sq(B), whereas Heath leaves this step implicit (noting 'the rectangle B, D is the square on B, for B is equal to D' without citing definitions). The AI also skips Heath's formal construction of an auxiliary line D = B, instead directly treating B, B as both means, which is a presentational variation rather than a structural divergence. Since the key intermediate conclusions are the same and the ai_only items are purely definitional over-citations, this is a same-backbone, different-depth case yielding Granularity difference (G).

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs follow the same logical backbone: decompose the given rectilineal figure into triangles by joining diagonals, construct corresponding equiangular triangles on the given line segment using I.23 and I.32, establish proportionality of sides via VI.4, show composite angles are equal by angle addition, chain the proportions to cover all corresponding sides, and conclude similarity by VI. Def. 1. The AI uses a pentagon (3 triangles) where Heath uses a quadrilateral (2 triangles), but this is a difference in illustrative complexity, not logical method. The ai_only citations (P1, CN2, 5.22) reflect over-citation: P1 is a postulate for joining diagonals, CN2 makes explicit the angle addition Heath uses implicitly, and 5.22 (ex aequali) explicitly chains proportions across three triangle pairs where Heath's simpler two-triangle decomposition chains them through a directly shared ratio. Heath_only is empty, confirming the AI covers all of Heath's cited ground. The key intermediate conclusions are the same in both proofs, just expressed at different levels of citation granularity.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same logical backbone: construct BG as third proportional to BC and EF via 6.11, establish that AB:DE = EF:BG through ratio manipulation, conclude triangle ABG equals triangle DEF via 6.15 (reciprocal proportionality), relate triangle ABC to triangle ABG via 6.1 (same height), substitute DEF for ABG, and apply the duplicate ratio definition D5.9. The citation differences are all depth-related: the AI cites 6.4 directly to establish proportional sides in similar triangles, while Heath derives the same proportion inline using the similarity condition plus alternando (5.16) — and 5.16 appears inside Heath's own proof of 6.4, satisfying the proof-tree containment test. The AI's additional citations of 5.7 (for substitution of equal magnitudes in ratio), CN1, and D6.1 are over-citations of axiom/definition-level steps that Heath performs without explicit citation. Heath's additional D5.11 (definition of corresponding magnitudes) is similarly a definition-level difference. Since all key intermediate conclusions match and all citation differences reduce to depth rather than substance, this is a granularity difference.

### 6.20
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: The classification is decided at Q2/Q3. While both proofs share the same backbone for Part 1 (decomposing similar polygons into similar triangles via 6.6 with angle subtraction), they diverge significantly in Part 2 (establishing that the component triangles are in the same ratio as the whole polygons). Heath constructs auxiliary diagonals AC and FH, uses 1.32 to show auxiliary triangles are equiangular, applies 6.1 to relate triangle areas to their bases, and chains ratios via 5.22 (ex aequali). The AI takes a genuinely different path: it observes that adjacent pairs of similar triangles share a common side (BE/GL or EC/LH), applies 6.19 directly to obtain duplicate ratios of those shared sides, then uses 5.11 (ratio transitivity) to chain the equal ratios. The heath_only citations 1.32, 5.22, and 6.1 are not merely subsumed by an AI-cited higher-level proposition (only 6.1 appears inside 6.19's proof tree, but 1.32 and 5.22 do not), confirming this is a backbone-level divergence rather than a depth difference. The AI's alternative path is logically complete and valid, so Q3 yields D.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that A is similar to C and B is similar to C (unpacking the definition D6.1 to get equiangularity and proportional sides), then conclude that A must be similar to B. Heath treats the transitivity of angle equality and side proportionality as self-evident, citing only D6.1. The AI proof provides the same key intermediate conclusions but explicitly justifies the transitivity steps: CN1 for angle equality, and 5.16 (alternando) plus 5.22 (ex aequali) for chaining the side proportions, with 5.11 also mentioned for ratio transitivity. All four ai_only citations (5.11, 5.16, 5.22, CN1) are additional granularity filling in steps that Heath leaves implicit, not a different proof path. Since heath_only is empty, there is no missing content from the AI side. This is Case A of Q2: same backbone, different citation depth.

### 6.22
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided this as Granularity (G). Both proofs share the same logical backbone for both directions: in the forward direction, both find third proportionals, express figure ratios via duplicate ratios, apply ex aequali (5.22), and conclude via transitivity (5.11). In the converse, both construct a line via 6.12, describe a similar figure via 6.18, apply the forward direction, use 5.9 to conclude equality of figures, and derive equality of lines. The sole heath_only citation 6.19 (similar triangles in duplicate ratio of sides) is contained within Heath's proof of 6.20 (similar polygons in duplicate ratio of sides), which the AI cites instead. This passes the proof-tree containment test: 6.19 appears explicitly inside the proof of 6.20, so the AI cites 6.20 as a unit while Heath uses the triangle-specific 6.19. The ai_only items D5.9 and D6.1 are definitions (over-citation), and 5.8 provides extra explicitness in the converse about why equal similar figures imply equal sides, where Heath simply asserts this. All differences are citation-depth, not backbone.

### 6.23
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Both proofs share the initial setup of placing equiangular parallelograms with collinear sides and completing an intermediate parallelogram, and both use VI.1 twice to establish that the ratios of adjacent parallelograms equal the ratios of the corresponding sides. However, the backbone diverges significantly in how the compound ratio is established. Heath introduces auxiliary magnitudes K, L, M via VI.12 (fourth proportional), transfers the parallelogram ratios to K:L and L:M using V.11, then applies ex aequali to the K:L:M sequence to reach the conclusion. The AI bypasses this entire auxiliary construction, instead directly applying D6.5 (definition of compound ratio) and V.22 (ex aequali) to the three-term parallelogram sequence ABCD:DCKH:CEFG. The heath_only items (5.11 and 6.12) are integral to Heath's auxiliary-magnitude strategy, not subsumed by any single AI citation; they represent an independent route. This constitutes a genuine path difference, and the AI's direct approach is logically sound.

### 6.24
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decides: both proofs establish the same key intermediate conclusions -- equiangularity of the sub-triangles (AEF with ACB, AKF with ADC) with the whole parallelogram's component triangles, proportionality of all corresponding sides about equal angles, similarity via D6.1, and transitivity via 6.21. The difference lies in the tools used to derive these shared conclusions. Heath uses 6.2 (parallel line cuts sides proportionally) to extract ratios, then manipulates them with 5.18 (componendo), 5.16 (alternando), and 5.22 (ex aequali). The AI instead establishes equiangularity first using 1.29 and 1.32, then applies 6.4 (equiangular triangles have proportional sides) to derive the needed ratios directly, combining them with 5.11. The proof-tree containment test confirms that three of the four heath_only items (6.2, 5.16, 5.22) appear inside Heath's proof of 6.4, meaning the AI cites 6.4 as a unit while Heath re-derives its internals inline. The fourth heath_only item (5.18) is not needed by the AI because its use of 6.4 naturally produces ratios in the required form, avoiding the separando-to-componendo conversion. The ai_only items (1.29, 1.32, 1.34, CN1) are over-citations of elementary facts that Heath uses implicitly. This is a citation-depth difference with the same logical backbone, yielding G.

### 6.25
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same geometric backbone: apply parallelograms equal to the two given figures, find a mean proportional, construct a similar figure on it, then use the duplicate ratio property and proportional reasoning to show the constructed figure equals the target. The key differences are citation-depth variations. Heath cites 1.44 for the first parallelogram application (to a triangle), while the AI uses the more general 1.45 for both. Heath cites 6.19 (similar triangles in duplicate ratio), while the AI cites 6.20 (similar polygons in duplicate ratio); since 6.19 appears explicitly inside Heath's proof of 6.20, the AI is citing a higher-level unit that subsumes it, satisfying the proof-tree containment test. For the final proportional arithmetic, Heath uses alternando (5.16), while the AI uses 5.7 (equal magnitudes have same ratio), 5.9 (same ratio implies equality), and 5.11 (transitivity), which are different Book V tools reaching the same conclusion. All differences are in citation granularity rather than in the logical backbone.

### 6.26
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same backbone: assume the inner parallelogram is not about the same diameter, construct a parallelogram about the diameter via I.31, use VI.24 to establish similarity/proportionality, derive that two segments must be equal via V.9, and reach a contradiction. The sole heath_only citation is 5.11 (transitivity of ratios), which the AI replaces with CN1 (transitivity of equality applied to ratio expressions) combined with 6.21 (transitivity of similarity) and D6.1 (definition of similar figures) to derive the same ratio equality. The ai_only items (P1, D6.1, CN1, 1.34, 6.21) are a mix of over-citation of constructions/definitions/axioms and alternative citation-depth for the ratio transitivity step. The key geometric conclusions are identical in both proofs, making this a same-backbone, different-citation-depth case.

### 6.27
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they bisect the line, take an arbitrary parallelogram applied to the line with a similar defect, use VI.26 to establish the parallelograms are about the same diameter, use I.43 to establish complement equality, construct the gnomon argument, and conclude the half-parallelogram is greatest. The heath_only citation {1.36} represents a citation-depth difference: Heath explicitly invokes I.36 to show that parallelograms on equal bases (the two halves of the bisected line) are equal, while the AI proof implicitly uses the same fact by noting AE = EB from the midpoint construction without formally citing I.36. The ai_only citations {1.10, CN5, D6.1, P1} are all construction steps (1.10 for bisection), definitions (D6.1 for similar figures), postulates (P1 for drawing), and common notions (CN5 for whole > part) that Heath leaves implicit. This is a symmetric over/under-citation pattern with the same key intermediate conclusions, characteristic of a granularity difference.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same backbone: bisect AB, construct a similar parallelogram EBFG on the half-line EB, handle the trivial equality case, construct a parallelogram KLMN equal to the excess (EBFG minus C) and similar to D, show it is similar to EBFG via 6.21, construct an inner parallelogram (OGPQ/EOPQ) equal and similar to KLMN, establish it is about the same diameter as EBFG via 6.26, then show the gnomon equals C and the resulting parallelogram applied to AB satisfies the requirements. The AI's ai_only citations (1.10, 1.3, 1.43, 6.24, 6.27, CN3, D6.1) are all granularity-level differences: 1.10 and 1.3 are construction propositions cited explicitly, 1.43 is the complement equality that Heath uses implicitly, 6.24 and 6.27 are cited for intermediate similarity and the maximality condition, and CN3 and D6.1 are axiom/definition over-citations. Heath's sole unique citation 1.36 (parallelograms on equal bases are equal) is used in the step OB = TE since AE = EB, which the AI handles through its complement-based argument using 1.43 instead, representing a micro-level difference in how the same geometric fact is established rather than a different logical path.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect AB at E, construct a parallelogram on EB similar to D, use VI.25 to construct a larger parallelogram equal to the original plus C and similar to D, show the two parallelograms are about the same diameter via VI.26, establish via gnomon arithmetic that the gnomon equals C, and conclude the applied parallelogram equals C with the excess similar to D via VI.24. The AI's ai_only citations (1.10, 6.18, 5.14, 6.22, CN3, CN5) are construction steps, ratio lemmas, and common notions that Heath leaves implicit -- typical over-citation at a finer granularity. Heath's sole unique citation (1.36, parallelograms on equal bases are equal) is used to establish AN = NB; the AI handles this area relationship through a broader application of 1.43 (complements about a diameter) without explicitly citing 1.36. The key intermediate conclusions are identical in both proofs, making this a same-backbone, different-depth case (Case A) under Q2.

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs the golden section via area methods: applying a parallelogram equal to the square on AB and exceeding by a similar figure (6.29), then using reciprocal proportionality in equiangular parallelograms (6.14) to derive the proportion. The AI takes a fundamentally different route, invoking the Book 2 result (2.11) that directly cuts a line so that the rectangle of the whole and one segment equals the square on the other, then converting this area equality to a proportion via the converse of 6.17. The citation sets are completely disjoint (Jaccard 0.0), and the key intermediate conclusions differ: Heath's backbone passes through parallelogram constructions and reciprocal proportionality, while the AI's passes through the rectangle-square equality from 2.11 and the proportion-rectangle equivalence from 6.17. Both paths are logically complete and valid, making this a genuine path difference.

### 6.31
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: draw AD perpendicular to BC, establish similarity of triangles ABD and ACD to ABC via 6.8, derive the continued proportions BC:BA=BA:BD and BC:CA=CA:DC, show that figure ratios equal segment ratios (duplicate ratio argument), then sum and use BD+DC=BC to conclude equality. The sole heath_only citation is 6.19 (similar triangles in duplicate ratio of corresponding sides), while the AI cites the more general 6.20 (similar polygons in duplicate ratio of corresponding sides). The proof-tree containment test confirms that 6.19 appears inside Heath's proof of 6.20, so the AI is citing 6.20 as a unit while Heath uses the triangle-specific 6.19 that 6.20 subsumes. The ai_only citations (5.24, 5.7, 5.9, 6.4, D5.9) represent explicit lower-level steps that Heath's proof handles more tersely or implicitly. This is a citation-depth difference with identical key intermediate conclusions.

### 6.32
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: using I.29 to establish alternate angle equalities (BAC = ACD and ACD = CDE), deducing BAC = CDE by transitivity, applying VI.6 to conclude equiangular triangles from the proportional sides about equal angles, extracting the angle equality ABC = DCE, then summing angles at C to show BCA + ACE equals two right angles via I.32, and finally applying I.14 for collinearity. The only citation difference is that the AI explicitly cites CN1 (Common Notion 1) for the transitivity step where Heath leaves it implicit. Since CN1 is a common notion (not a substantive proposition) and the underlying logical step is present in both proofs at the same position, this is a same-backbone, different-depth situation (Case A of Q2), yielding a granularity difference classification.

### 6.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the identical logical backbone: construct equimultiples of arcs BC and EF, show via III.27 that the corresponding central angles are equimultiples of BGC and EHF, verify the equimultiple comparison tracks (greater/equal/less), invoke V.Def.5 to conclude BC:EF :: BGC:EHF, then use the doubling relationship (central angle = 2 * inscribed angle) to extend the proportion to inscribed angles. The heath_only set is empty, confirming that every Heath citation appears in the AI set. The ai_only items (3.20, 3.26, 5.11, 5.15, CN2, D3.1) are all explicit citations for steps that Heath handles implicitly: 3.20 for the doubling relationship, 3.26 used in an indirect argument for the comparison step, 5.15 and 5.11 for ratio manipulation, and CN2/D3.1 as foundational citations. This is classic over-citation at greater depth, placing the classification squarely in Case A of Q2.


## Book 7

| Category | Count |
|---|---|
| Perfect match (P) | 1 |
| Granularity difference (G) | 29 |
| Path difference (D) | 9 |
| AI proof error (E) | 0 |

**Total**: 39 propositions

### 7.1
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction assuming a number E greater than a unit measures both AB and CD, then tracing through the successive remainders of the anthyphairesis (Euclidean algorithm) to show E must measure every remainder including the final unit, yielding a contradiction. Heath traces through each specific named remainder (BF, FA, DG, GC, FH, HA) while the AI presents the same argument in a more general, summary form. The ai_only set consists entirely of definitions (D5.1, D7.1, D7.2, D7.3) that the AI explicitly cites to justify sub-steps Heath treats as implicit, and heath_only is empty. Since the key intermediate conclusions are identical and the citation difference is only in the depth of definitional justification, this is a granularity difference (G).

### 7.2
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) handle the trivial case where CD measures AB; (2) apply the antenaresis (repeated subtraction) algorithm, invoking 7.1 to guarantee termination in a number rather than a unit; (3) trace the final remainder back up through each step to show it measures both original numbers; (4) prove maximality by showing any common measure must divide down to the final remainder, contradicting the assumption it could be larger. The AI proof is a faithful reproduction of Heath's argument with only a minor naming difference (FD vs CF for the final remainder). The citation difference is purely one of depth: the AI explicitly cites definitions (D7.3, D7.5, D7.12, D7.14) and common notions (CN3, CN5) that Heath invokes implicitly without citation. Heath's only explicit citation is 7.1, which the AI also cites. Since heath_only is empty and ai_only contains only foundational definitions and common notions, this is a classic over-citation granularity difference.

### 7.3
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take D as the GCM of A and B via 7.2, then split into two cases (D measures C, or D does not measure C). In Case 1 both proofs show D is the greatest common measure of A, B, C. In Case 2 both proofs show D and C are not prime to one another, take E as GCM(D, C) via 7.2, show E measures A, B, C, and prove E is the greatest. The AI proof adds explicit citations to definitions D7.1, D7.12, and D7.3 that Heath uses implicitly, and adds a sub-case where A and B might be prime to one another (setting D to the unit), which is an elaboration on the same backbone. Since the ai_only items are all definitions (over-citation) and the heath_only set is empty, this is Case A of Q2: same backbone, different citation depth, yielding a Granularity difference.

### 7.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof argues through three sub-cases with constructive decompositions: when the numbers are coprime, each unit of BC is a part of A; when BC measures A, BC is a part directly; when BC does not measure A, the GCD (via 7.2) is used to decompose BC into equal parts, each being a part of A. The AI proof takes a fundamentally different path, appealing directly to Definitions 7.3 and 7.4 to cover the two exhaustive cases (A measures B or A does not measure B) without any constructive decomposition. Since D7.3 defines 'part' as 'when it measures' and D7.4 defines 'parts' as 'when it does not measure,' the AI's argument is logically valid but structurally different from Heath's constructive approach. The backbones differ: Heath uses substantive proposition 7.2 and constructive reasoning to show parts exist, while the AI relies purely on definitional coverage. This is a genuine path difference, not a granularity difference, because the AI's approach omits all constructive content and follows an entirely different logical strategy.

### 7.5
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: decompose the larger numbers into equal parts (n copies of the smaller numbers), pair corresponding parts to show each pair sums to A+D (or A+C in the AI's notation), and conclude the sum of the larger numbers is the same multiple of the sum of the smaller numbers. The AI proof is logically complete with no defects under Q1. The citation difference arises because Heath cites no explicit references while the AI explicitly cites definitions D7.3, D7.5, D7.15 and Common Notion CN2 to justify the concepts of 'part', 'multiple', 'multiplied by', and the addition of equals. Since all ai_only items are definitions and common notions (not substantive propositions), and heath_only is empty, this is purely a citation-depth difference with the same backbone, satisfying Case A of Q2.

### 7.6
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: divide AB into parts AG, GB of C and DE into parts DH, HE of F, apply Proposition 7.5 twice to show that AG+DH and GB+HE are each the same part of C+F as the corresponding part is of C, then reassemble to conclude AB+DE is the same parts of C+F that AB is of C. The AI proof explicitly cites CN2 (for the addition step), D7.3 (definition of part), and D7.4 (definition of parts) where Heath leaves these foundational references implicit. Since heath_only is empty and all ai_only items are definitions and common notions rather than substantive propositions, this is a clear Case A situation: same backbone, different citation depth, yielding a Granularity difference.

### 7.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary quantity CG and uses Proposition 7.5 (addition of equal parts yields equal part of the sum) to establish that AB is the same part of GF as AE is of CF, then deduces GF = CD, subtracts CF to get GC = FD, and substitutes back. The AI proof takes a fundamentally different approach: it works directly from definitions D7.3 and D7.5, decomposing CD into n copies of AB and CF into n copies of AE, then subtracts the sums component-wise using CN3 to show FD equals n copies of EB. The key intermediate conclusions differ in kind -- Heath relies on an auxiliary construction and the additive proposition 7.5, while the AI uses direct algebraic decomposition from definitions. The proof-tree containment test does not apply since the AI cites no higher-level proposition that could subsume 7.5; rather, the AI bypasses 7.5 entirely by working at the definitional level. The AI's different path is logically complete and valid, yielding classification D.

### 7.8
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: divide the whole and the subtracted number into equal aliquot parts, apply Proposition 7.7 to each corresponding pair of parts to show that each remainder is the same part of FD as the corresponding part is of CD, then combine the remainders to reach the conclusion. The AI proof adds explicit citations to 7.5 (summing parts), D7.3, and D7.4 (definitions of part and parts) that Heath leaves implicit, but the key intermediate conclusions are identical in both proofs. Since heath_only is empty and the ai_only items (7.5, D7.3, D7.4) represent over-citation of supporting results rather than a different logical path, this is Case A of Q2: same backbone with different citation depth, yielding a Granularity difference.

### 7.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decomposing the numbers into equal parts (Heath explicitly names segments BG, GC and EH, HF; the AI uses the equivalent n copies of A and n copies of C), then using Propositions 7.5 and 7.6 to show that the part-or-parts relationship is preserved when the copies are summed, and concluding by identifying those sums with the original numbers. The AI explicitly separates the two cases (part via 7.5, parts via 7.6) while Heath handles them together with a combined reference [VII. 5, 6], but the key intermediate conclusions are identical. The ai_only set consists entirely of definitions (D7.3, D7.4, D7.5) that the AI cites explicitly where Heath leaves them implicit, which is a citation-depth difference rather than a structural divergence. Since heath_only is empty, no substantive propositions are missing. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 7.10
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: divide the first number into equal aliquot parts of the second, divide the third into equal aliquot parts of the fourth, establish equal multitude of parts, apply Proposition 7.9 (alternation for a part) to each individual part, then combine using Propositions 7.5 and 7.6. The AI proof makes the case split (part vs. parts) explicit in Cases I and II, while Heath leaves this implicit in the disjunctive phrasing. The ai_only set consists entirely of over-citations: definitions D7.3, D7.4, D7.20 that Heath invokes implicitly, Common Notion CN1 used for transitivity that Heath does not explicitly name, and Proposition 7.4 (any number is either a part or parts of any number) which provides foundational justification for the division step. The heath_only set is empty, confirming no substantive proposition is missing from the AI proof. This is a clear case of same backbone with different citation depth.

### 7.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: converting the given proportion into a part/parts relationship via D7.20, applying 7.7 and 7.8 to establish the remainder has the same relationship, then converting back via D7.20. The AI adds a third explicit case for multiples (using D7.5 and CN3), which Heath treats as implicitly covered by the 'part or parts' formulation under D7.20. The ai_only citations (CN3, D7.5) are a common notion and a definition used in this additional case, not substantive propositions representing a different proof path. Since heath_only is empty and the core reasoning chain is identical, this is Case A of Q2: same backbone, different citation depth.

### 7.12
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: convert the proportion to a part/parts relationship via D7.20, show that sums preserve this relationship using 7.5 and 7.6, then convert back to a proportion via D7.20. The AI proof is more explicit, breaking into five exhaustive cases (part, parts, equal, multiple, inverse parts) justified by 7.4, whereas Heath handles 'whatever part or parts' compactly in a single argument citing 7.5 and 7.6. The AI's additional citations (7.4, CN2, D7.3, D7.4, D7.5) are all over-citations providing granular justification for steps Heath treats implicitly. Since heath_only is empty, every citation Heath uses also appears in the AI's set. The key intermediate conclusions are identical in both proofs; only the depth of explicit justification differs.

### 7.13
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof uses a single unified argument: by D7.20, whatever part or parts A is of B, the same is C of D; then by 7.10, alternately whatever part or parts A is of C, the same is B of D; then by D7.20 again, A:C :: B:D. The AI proof instead breaks into three separate cases based on D7.20 (part, parts, and multiple), handling each independently. Case I uses 7.9 for the part case, Case II uses 7.10 for the parts case, and Case III introduces 7.4 to further sub-divide the multiple case into sub-cases involving part, parts, equality, and reverse relationships. This three-case structure with arithmetic sub-cases in Case III constitutes a genuinely different backbone from Heath's single unified argument. The heath_only set is empty, confirming that the AI covers all of Heath's ground, but the AI's approach is structurally different, not merely more granular. Both proofs are logically complete, so this is a valid different path (D).

### 7.14
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. The AI proof's base case (Steps 2-6) establishes the same key intermediate conclusions as Heath: alternation of A:B=D:E to get A:D=B:E, alternation of B:C=E:F to get B:E=C:F, chaining these to get A:D=C:F, then alternating again to conclude A:C=D:F. The backbones are identical. The AI adds three extra citations (CN1 for the transitivity step Heath performs implicitly, D5.17 and D7.20 as definitional references) and extends the proof with an inductive generalization to n terms, but these are differences in citation depth and exposition rather than a different logical path. Since heath_only is empty and ai_only contains only common notions and definitions, this is a clear granularity difference.

### 7.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof decomposes BC into individual units and EF into equal parts of D, then uses Proposition 7.12 (aggregation of antecedents and consequents in a proportion) to establish that the unit is to D as BC is to EF. The AI proof takes a fundamentally different route: it establishes the proportion A:B = C:D using Definition 7.20 (since A is the same part of B that C is of D), then applies Proposition 7.13 (alternation of proportions) to obtain A:C = B:D, and reads off the measurement conclusion. These represent genuinely different logical backbones — Heath aggregates via 7.12 while the AI alternates via 7.13 — yielding different key intermediate conclusions. The AI's chain is logically complete and valid at every step, so Q3 confirms a valid different path, resulting in classification D.

### 7.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that the unit measures A the same number of times that B measures C (from the hypothesis A*B=C), then apply VII.15 to alternate and conclude that the unit measures B the same number of times that A measures C. The divergence is only in how they complete the proof: Heath repeats a symmetric argument for D (showing A measures D according to units in B from B*A=D) and then compares the two measurement relations, while the AI compresses the final steps by observing that A measures C as many times as there are units in B, which by Definition 7.15 means C = B*A = D. The AI's only extra citation (D7.15) is a definition used to shortcut the concluding steps, and heath_only is empty, confirming this is a citation-depth difference rather than a path difference.

### 7.17
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decides the classification. Heath's proof establishes the proportion B:C = D:E by first introducing a unit F and deriving two intermediate ratios F:A = B:D and F:A = C:E via D7.20, combining them to get B:D = C:E, and then applying alternation (7.13) to reach B:C = D:E. The AI proof takes a different path: it directly establishes that B measures D and C measures E each exactly n times (where n is the number of units in A), concludes that D is the same multiple of B as E is of C, and then applies D7.20 to jump directly to D:E = B:C without establishing the intermediate unit-based ratios or using alternation. These are genuinely different backbones -- Heath routes through a unit-ratio intermediary and alternation, while the AI argues directly from the equimultiple relationship. The AI's path is logically sound (if D = nB and E = nC, then D:E = B:C follows), so under Q3 this is a valid different path, yielding category D.

### 7.18
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) set up D = A*C and E = B*C, (2) apply VII.16 (commutativity of multiplication) to rewrite as C*A = D and C*B = E, (3) apply VII.17 to conclude that since C multiplying A and B produces D and E, the ratio A:B = D:E. The only citation difference is that the AI explicitly cites Definition 7.15 (the definition of multiplication) to justify the initial setup, while Heath does not. Since D7.15 is a definition rather than a substantive proposition, this is a straightforward over-citation representing a citation-depth difference, not a path divergence. The identical logical backbone with a minor definitional over-citation yields Granularity difference (G).

### 7.19
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone for the biconditional: in the forward direction, both form an auxiliary product (A*C), apply VII.17 and VII.18 to establish ratio chains, then conclude the two target products are equal; in the converse, both start from equality of products and use VII.17 and VII.18 to derive proportionality. The difference is purely in citation depth: Heath invokes V.9 (magnitudes with the same ratio to the same are equal) and V.7 (equal magnitudes have the same ratio to the same) as the mechanism for converting between equality and ratio statements, while the AI works directly from D7.20 (the definition of proportional numbers) and uses 7.16 (commutativity of multiplication) for a minor technical step. The ai_only items (7.16, D7.15, D7.20) are definitions and a basic arithmetic fact operating at a lower level than Heath's Book V citations, confirming this is a citation-depth difference rather than a path difference.

### 7.20
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath proves 7.20 by the part-versus-parts dichotomy (7.4): he assumes CD is 'parts' of A, divides CD and EF into equal sub-parts, then uses alternate proportions (7.13) and summation of proportionals (7.12) to derive smaller numbers in the same ratio, contradicting minimality; he concludes CD must be a 'part' of A. The AI takes a fundamentally different route: it invokes 7.19 (cross-multiplication of proportionals) to establish A*D = B*C, then argues by contradiction that if A does not measure C there is a remainder R < A yielding a smaller pair R,S in the same ratio via 7.19 converse, contradicting minimality. The key intermediate conclusions differ entirely — Heath's backbone rests on the part/parts dichotomy and proportional sums, while the AI's backbone rests on cross-multiplication and division with remainder. Both paths are logically complete, so the classification is D.

### 7.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Both proofs share the same logical backbone: assume for contradiction that smaller numbers C, D exist with the same ratio as A, B; apply 7.20 to establish that C measures A and D measures B the same number of times; derive that a common measure greater than the unit exists for A and B; and reach a contradiction with the hypothesis that A and B are prime to one another (D7.12). The difference lies in how the common measure is extracted: Heath uses 7.16 (commutativity of multiplication) to convert 'C measures A according to E' into 'E measures A according to C', while the AI goes directly from A = nC to 'n measures A' by invoking D7.3 (the definition of 'measures'). The AI also explicitly cites D7.3 where Heath leaves the definition implicit. Since the key intermediate conclusions are identical and only the citation depth differs (heath_only = 7.16 is a theorem whose role is replaced by a direct definitional argument in the AI proof, and ai_only = D7.3 is a definition), this is a granularity difference decided at Q2 Case A.

### 7.22
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume A,B are the least numbers in ratio and are not coprime, so some C>1 measures both; construct D,E such that C*D=A and C*E=B; apply 7.17 to get D:E :: A:B; observe D<A and E<B, contradicting the minimality of A,B. The only difference is citation depth: the AI explicitly cites D7.12 (definition of coprimality), D7.3 (definition of part), and CN5 (whole greater than part) to justify the steps that Heath leaves implicit. Heath_only is empty, confirming no substantive step is missing from the AI proof. All ai_only items are definitions and common notions, which are foundational over-citations characteristic of granularity difference.

### 7.23
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume C and B are not prime to one another, deduce that some number D measures both C and B, use transitivity of the 'measures' relation to show D also measures A, then derive a contradiction since A and B were assumed prime to one another. The only difference is citation depth: the AI explicitly cites D7.3 (definition of 'part') and D7.15 (definition of 'multiply') to justify the transitivity step where D measures C and C measures A implies D measures A, whereas Heath states this transitivity without citing any additional definitions beyond D7.12. The ai_only set contains only definitions (D7.3, D7.15) and heath_only is empty, confirming this is over-citation by the AI rather than a path divergence. Same backbone, different citation depth yields Granularity difference (G).

### 7.24
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone: assume by contradiction that some E > 1 measures both C and D, derive that A and E are coprime via 7.23, express D = E*F = A*B, establish proportionality E:A = B:F via 7.19, conclude E and A are least in their ratio via 7.21, apply 7.20 to show E measures B, then reach a contradiction since B and C are coprime but E measures both. The only citation difference is that Heath explicitly cites 7.16 (commutativity of multiplication) as an intermediate step when deriving that F measures D before applying Def 7.15, while the AI directly states the existence of F with E*F = D without this intermediate citation. This is a citation-depth difference with identical backbone, satisfying Case A of Q2.

### 7.25
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this classification as G (Granularity difference). Both proofs share the same logical backbone: they observe that A appears as both factors in A*A, that each factor is prime to B, and then apply VII.24 to conclude the product is prime to B. Heath introduces an auxiliary variable D equal to A as a formal device to make the two factors syntactically distinct, while the AI simply references A twice directly, which is a notational rather than structural difference. The ai_only items (D7.12 and D7.18) are definitions that the AI explicitly cites but Heath uses implicitly, representing over-citation rather than a path divergence. The heath_only set is empty, confirming no steps are missing from the AI proof.

### 7.26
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this classification as D (path difference). Heath's proof consolidates primality along the product AB first: it shows AB is prime to C (since A and B are each prime to C, by 7.24), then AB is prime to D (similarly), and finally concludes CD is prime to AB (since C and D are each prime to AB, by 7.24). The AI proof takes the symmetric approach, consolidating along CD first: it uses D7.12 to flip the given relations, shows CD is prime to A (since C and D are each prime to A, by 7.24), then CD is prime to B (similarly), then CD is prime to AB (since CD is prime to both A and B, by 7.24), and finally uses symmetry to state AB is prime to CD. The key intermediate conclusions differ: Heath's backbone runs through 'AB is prime to C' and 'AB is prime to D', while the AI's runs through 'CD is prime to A' and 'CD is prime to B'. Both paths are logically valid and complete, but they establish different intermediate facts, making this a genuine path difference. The AI's additional citations of D7.12 and D7.15 reflect its explicit use of the symmetry of the coprimality relation and the definition of multiplication, which Heath leaves implicit.

### 7.27
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI and Heath proofs of 7.27 both establish that if A and B are coprime, then their squares are coprime and their cubes are coprime, using exactly the same citation set (7.25 and 7.26). The variable naming conventions differ (Heath uses C=A^2, E=B^2, D=A^3, F=B^3 while the AI uses C=A^2, D=B^2, E=A^3, F=B^3), but after accounting for this relabeling, the key intermediate conclusions align: both establish that the square of each number is coprime to the other number and to the other square, then use the four pairwise coprimality conditions with 7.26 to conclude the cubes are coprime. The AI uses 7.26 to prove the squares coprime (applying it to (A,A) and (B,B)) while Heath uses a 7.25 chain, which is a minor structural variation, but the key conclusions and citation sets are identical. Since ai_used equals heath_refs exactly ({7.25, 7.26}) and the backbone of key intermediate conclusions matches, the classification is P (Perfect match).

### 7.28
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs establish the same key intermediate conclusions in the same logical order for both directions of the biconditional: in Part 1, both assume a common measure of the sum and one addend, deduce it measures the other addend (the remainder), and reach a contradiction with coprimality via D7.12; in Part 2, both assume a common measure of the two addends, deduce it measures their sum, and again reach a contradiction with coprimality. The AI's ai_only citations (7.5, 7.6, 7.7, 7.8, D7.3, D7.5) are all explicit justifications for divisibility-of-sum and divisibility-of-remainder steps that Heath treats as self-evident without citation. Since heath_only is empty and the backbones are identical, the difference is purely one of citation depth, not logical path.

### 7.29
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume for contradiction that the prime p and number A are not coprime, derive that some number C measures p, then reach a contradiction with the definition of prime (only the unit measures a prime). The AI explicitly cites D7.11 (definition of prime) and D7.12 (definition of coprime) while Heath invokes these definitions implicitly without formal citation. Since heath_only is empty and ai_only contains only definitions, this is a straightforward citation-depth difference where the AI is more explicit about its definitional foundations. The key intermediate conclusions are the same in both proofs, making this a granularity difference rather than a path difference.

### 7.30
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: assume the prime does not measure one factor, conclude coprimality via 7.29, establish a proportion via 7.19, invoke the least-ratio property via 7.21, and apply 7.20 to conclude divisibility of the other factor. The AI proof cites all five of Heath's references and adds three more (7.13 for explicit ratio rearrangement, D7.3 and D7.11 as definitional justifications), which are over-citations providing extra explicitness rather than a different logical path. Since heath_only is empty and the ai_only items are either definitions or a ratio-manipulation lemma used to make an implicit step explicit, the proofs differ only in citation depth, not in key intermediate conclusions.

### 7.31
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Both proofs follow the same logical backbone: starting from a composite number A, finding a divisor B, checking if B is prime, and if not iterating to find smaller divisors, then arguing termination by the impossibility of an infinite strictly decreasing sequence of natural numbers. The key intermediate conclusions are identical in both proofs. Heath cites no propositions, relying on definitions implicitly, while the AI explicitly cites D7.11 (prime number definition), D7.13 (composite number definition), and D7.3 (measurement definition). Since ai_only contains only definitions and heath_only is empty, and the backbone is the same, this is a citation-depth difference classified as G under Q2 Case A.

### 7.32
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same two-case backbone: (1) if A is prime, the proposition holds immediately; (2) if A is composite, then by 7.31 some prime number measures A. The AI proof explicitly cites definitions D7.11 (prime number) and D7.13 (composite number) to justify the transition from 'not prime' to 'composite,' whereas Heath leaves this definitional step implicit. Since ai_only contains only definitions and heath_only is empty, the proofs share the same key intermediate conclusions with the AI simply providing greater citation depth at the definitional level. This is a clear Case A granularity difference.

### 7.33
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides: both proofs share the same two-case backbone (Case 1: prime-to-one-another implies already least; Case 2: find GCD D, divide to get E,F,G, show same ratio, prove minimality by contradiction with the GCD). The differences are purely in citation depth and lemma selection. For Case 1, Heath cites 7.21 directly while the AI re-derives 7.21's content inline. For the ratio step, Heath uses D7.20 and 7.16 while the AI uses 7.17. For the contradiction, Heath uses 7.19 (equal products imply proportion) to show M > D, while the AI uses 7.16 (commutativity), 7.20, and CN5 to reach the same conclusion that D times M exceeds D. The AI's citation of 7.20 in Step 7 is imprecise (7.20 requires the numbers to be the least, not merely smaller), but under the lenience rule the overall inference is compressed-but-sound rather than invalid. All key intermediate conclusions are identical across both proofs, making this a granularity difference.

### 7.34
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Q2 reveals a different logical backbone between the two proofs, leading to classification D via Q3. Heath proves the proposition in two separate cases (A,B prime vs not prime), using 7.21 to establish that primes are least in their ratio (Case 1) and 7.17 to derive the final contradiction via proportionality (C measures D, the greater the less) in both cases. The AI unifies both cases into a single general argument using 7.2 to find the GCD, then 7.33 and 7.22 to establish the least ratio numbers and their primality. Most significantly, the AI avoids 7.17 entirely by using a direct size argument: since 7.20 shows F measures H, we get H >= F, hence G = A*H >= A*F = C, contradicting G < C. This is a substantively different contradiction mechanism from Heath's proportionality-based approach. The AI's alternative path is logically complete and valid, satisfying Q3(b).

### 7.35
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: a proof by contradiction showing that if the least common multiple L (or E in Heath) does not measure the given number C (or CD), then repeated subtraction yields a positive remainder R less than L that is still measured by both A and B, contradicting L being the least such number. Heath's proof uses no explicit citations while the AI cites 7.34 (existence of LCM), 7.4 (parts), CN5 (whole greater than part), and definitions D7.3 and D7.5. All of these AI-only citations provide explicit justification for steps that Heath performs implicitly, representing a difference in citation depth rather than a difference in the logical path. The key intermediate conclusions are identical in both proofs.

### 7.36
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: find D = LCM(A,B) via 7.34, then find E = LCM(D,C) via 7.34, show A, B, C all measure E via transitivity of divisibility, and prove minimality by contradiction using 7.35. Heath's proof explicitly handles two cases (C measures D vs. C does not measure D), while the AI's proof uses a single general argument that subsumes both cases by always computing LCM(D,C). The only citation difference is ai_only = {D7.5}, a definition the AI cites explicitly to justify that E measuring F implies F >= E, which Heath leaves implicit. This is a citation-depth difference, not a path difference, confirming Case A of Q2.

### 7.37
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 7.37 uses VII.15 (alternate proportion) as its key mechanism: given that B measures A with quotient C, Heath establishes that the unit measures C the same number of times as B measures A, then applies 7.15 to conclude the unit measures B the same number of times as C measures A, thereby showing C is the B-th part of A. The AI takes a fundamentally different path: it reframes the problem through multiplication definitions (D7.5, D7.15), uses 7.16 (commutativity of multiplication) to establish C times B equals B times C equals A, and then reasons directly that since A is composed of B copies of C, C measures A exactly B times and is therefore the B-th part. Although 7.15 appears inside Heath's proof of 7.16 (satisfying the containment test structurally), the two proofs use their respective citations for entirely different logical purposes -- Heath uses alternate proportion while the AI uses commutativity of multiplication -- making this a genuine path difference rather than a granularity difference. The AI's chain is logically complete and sound throughout.

### 7.38
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs follow the same logical backbone: (1) establish that the unit measures one number the same number of times that the part measures the whole, using the definition of a part; (2) apply Proposition 7.15 (alternation) to conclude the unit measures a third number the same number of times the named number measures the whole; (3) conclude the named number measures the whole. The AI's extra citations D7.2 and D7.3 are definitions that Heath uses implicitly without citing. The heath_only set is empty, meaning the AI covers all of Heath's references. This is a clear Case A in Q2: same backbone with different citation depth, where the AI over-cites the definitional basis. The Jaccard of 0.333 reflects only this definitional over-citation, not any structural divergence.

### 7.39
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: (1) find the LCM of the given numbers using 7.36, (2) show the LCM has the required parts via 7.37, (3) prove minimality by contradiction assuming a smaller number also has the parts, using 7.38 to show the given numbers measure this smaller number, and (4) derive a contradiction with the LCM being least. The AI proof cites four additional references (7.34, 7.35, CN5, D7.3) that are not in Heath but do not reflect a different proof strategy. 7.34 is merely mentioned parenthetically as the two-number version of 7.36; 7.35 makes explicit the step that the LCM divides E (which Heath leaves implicit in saying 'which is impossible'); CN5 and D7.3 make explicit the inference from 'D measures E' to 'D is at most E'. These are all elaborations of steps Heath compresses, representing citation-depth differences rather than backbone differences.


## Book 8

| Category | Count |
|---|---|
| Perfect match (P) | 1 |
| Granularity difference (G) | 15 |
| Path difference (D) | 11 |
| AI proof error (E) | 0 |

**Total**: 27 propositions

### 8.1
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof works by assuming a smaller set in the same ratio, applying ex aequali (7.14) to reduce to the ratio of extremes A:D = E:H, invoking 7.21 to conclude A,D are the least in that ratio, then using 7.20 to derive that A measures E, which contradicts E < A. The AI proof takes a fundamentally different approach: it invokes 7.33 to guarantee the existence of a least set B with the same ratios, then applies 7.20 to show that the least set measures the original with a common multiplier m (so A_i = m*B_i for all i), then uses D7.12 (definition of coprimality) to conclude m must be a unit since it is a common measure of the coprime extremes, yielding A_i = B_i, which contradicts the assumption that the A's are not the least. The key intermediates differ: Heath establishes a ratio equality of extremes and uses the 'primes are least' theorem, while the AI establishes a uniform multiplier relationship and uses the definition of coprimality directly. Both paths are logically valid but arrive at the contradiction through genuinely different intermediate conclusions.

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing terms as products of powers of A and B, showing consecutive terms have ratio A:B, establishing the extremes are prime to each other via 7.22 and 7.27, and concluding minimality via 8.1. The citation differences are all depth-level: the AI's ai_only items (7.33 for reducing to least terms, 7.29 as extra primality support, D7.15 as a definition citation) are over-citations that do not alter the logical structure. Heath's sole heath_only item (7.18) is subsumed by the AI's use of 7.17 alone, since 7.18 reduces to 7.17 via commutativity of multiplication (7.16), and the AI simply reformulates the ratio arguments so that only 7.17 is needed. The key intermediate conclusions are identical in both proofs, making this a same-backbone, different-depth case.

### 8.3
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decides this classification as G (granularity difference). Both proofs share the same logical backbone: (1) identify the two-term least ratio pair and establish coprimality via 7.22, (2) construct the n-term continued proportion via 8.2, (3) show the constructed sequence equals the given sequence (both being least with the same multitude), and (4) conclude coprimality of extremes via 7.27. The citation differences are matters of depth, not path. Heath cites 7.33 to explicitly find the least pair in the ratio, while the AI takes the existence of such a pair for granted (an under-citation). The AI cites 7.20 to argue mutual measurement implies equality of the two least sequences, while Heath states this equality more directly without invoking 7.20. These are citation-depth variations around the same key intermediate conclusions, not different logical routes.

### 8.4
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same key intermediate conclusions: (1) finding LCMs via 7.34 to bridge consecutive ratio pairs, (2) establishing proportional relationships through multiplication, (3) proving minimality via 7.20 and 7.35. The AI cites 7.17 where Heath cites 7.13 and D7.20; the proof-tree containment test confirms this is a depth difference, since Heath's proof of 7.17 explicitly uses 7.13 internally. The AI's additional citation of 7.22 (coprimality of least-ratio pairs) is an over-citation of a fact Heath treats as implicit from the ratios being 'in least numbers.' The AI organizes the proof iteratively (handle two ratios, then extend) rather than Heath's case-based split (E measures K vs. E does not measure K), but this is a presentational choice: the AI's general method (always taking LCM of the last term with the next antecedent) subsumes both of Heath's cases, and the underlying logical backbone of LCM construction, ratio preservation, and minimality proof is the same.

### 8.5
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof constructs least numbers in continued proportion via 8.4, then uses ex aequali (7.14) to link the ratio A:B to the compounded ratio G:K. The AI instead constructs a single intermediate product F = a*d, uses 7.17 and 7.18 to establish A:F = b:d and F:C = a:c respectively, then applies the definition of compounded ratio (D6.5) directly. These represent genuinely different logical backbones: Heath works through least numbers in continued proportion and ex aequali reasoning, while the AI takes a more direct algebraic route through an auxiliary product and the definition of compounded ratio. Both paths are logically complete and valid, making this a path difference.

### 8.6
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 reveals different logical backbones, leading to classification via Q3. Heath's proof takes the least numbers in the same ratio as a subsequence (e.g., A, B, C mapped to F, G, H via VII.33), then uses ex aequali (VII.14) to relate the ratio of non-adjacent terms (A:C = F:H), transfers the non-measuring property via D7.20, and concludes from VIII.3 that F, H are coprime. The AI takes a fundamentally different path: it first extracts the basic ratio e:f (VII.33), proves e is not unity via VII.20 and D7.3, then for any subsequence A_i through A_j uses VIII.2 to explicitly construct the least continued proportion, applies VIII.3 to show the extremes e^(j-i) and f^(j-i) are coprime, uses VII.20 to express A_i and A_j as coprime-coefficient multiples of a common factor m, and derives a contradiction from assuming divisibility. The AI's path through 8.2 (constructing least continued proportions) and its explicit power-based argument replaces Heath's ex aequali approach entirely. Both proofs are logically complete, so Q3 confirms D.

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs use identical proof-by-contradiction structures relying solely on Proposition 8.6. The key intermediate conclusion in both is that if the first number does not measure the second, then by 8.6 no number in the sequence measures any other, which contradicts the hypothesis that the first measures the last. The citation sets are identical (both cite only 8.6), giving Jaccard similarity of 1.0, and the logical backbones match exactly, satisfying the perfect match criteria.

### 8.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs share the same backbone of key intermediate conclusions: (1) find least numbers in continued proportion with the given ratio, (2) show extremes are prime via 8.3, (3) use 7.21 and 7.20 to establish that the extremes measure D and E the same number of times, (4) construct intermediate terms by multiplying the least proportionals by that common factor, and (5) verify the resulting sequence is in continued proportion. The citation differences reflect substitutions at the same logical positions: the AI uses 8.2 to explicitly construct least continued proportionals where Heath uses VII.33 on the full sequence, the AI uses 7.17 to show multiplication preserves ratios where Heath invokes D7.20, and the AI reasons directly about extreme ratios of continued proportions where Heath cites VII.14 (ex aequali). These are citation-depth differences for the same underlying logical steps, not different proof paths.

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification as Granularity difference (G). Both proofs share the same logical backbone: reduce the ratio A:C1 to least terms, use 8.2 to construct the least numbers in continued proportion as powers of those least terms, identify A and B with the extreme powers via uniqueness of least numbers (8.1), then construct the geometric sequences 1, p, p^2, ..., p^(k+1)=A and similarly for B. The AI explicitly cites 7.33 (to find least terms), 7.22 (to show they are prime), and 8.3 (to confirm extremes of least sequence are prime), while Heath handles these steps implicitly or within the internal proofs of 8.2 (which itself uses 7.22). The proof-tree containment test confirms that 7.22 appears inside Heath's proof of 8.2, and both 7.33 and 7.22 appear inside Heath's proof of 8.3. Heath's sole unique citation D7.20 is a definition used to justify proportionality statements that the AI handles through explicit power notation without citing the definition. The key intermediate conclusions are identical in both proofs, differing only in citation depth.

### 8.10
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Heath's proof explicitly constructs intermediate numbers H=D*F, K=D*H, L=F*H and directly verifies the continued proportion A, K, L, B using VII.17 and VII.18 in a computational, step-by-step manner. The AI proof takes a fundamentally different route: it characterizes A and B as (m+1)-th powers of their respective geometric-progression bases C1 and D1, then invokes 8.2 to find least numbers in continued proportion with ratio C1:D1, and applies 8.8 to transfer the existence of m intermediate terms to A and B. These are genuinely different logical backbones — Heath builds the intermediates by hand while the AI leverages higher-level existence results (8.2, 8.8). The AI's path is logically valid: 8.2 correctly produces continued proportions whose extremes are powers of the base ratio elements, and 8.8 legitimately transfers the count of intermediates to numbers in the same ratio. Under Q3, the AI's different path passes the hardened 1(b) standard with no unsupported assertions, circular citations, or invalid inferences, yielding classification D.

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct the product of the two sides of the square numbers, use 7.17 to establish the ratio of the first square to the product equals the ratio of the sides, use 7.18 to establish the ratio of the product to the second square equals the same ratio of the sides, conclude the product is a mean proportional, then apply D5.9 for the duplicate ratio. The AI proof additionally cites CN1 (to explicitly justify equating the two ratio expressions), D7.15 (definition of multiplication), and D7.18 (definition of square number), all of which are foundational items Heath uses implicitly. Since heath_only is empty and ai_only contains only Common Notions and Definitions, this is a clear Case A granularity difference with the AI over-citing foundational material.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) the ratio of the sides equals the ratio between corresponding products (a^2:ab = ab:b^2), (2) the four numbers a^3, a^2b, ab^2, b^3 are in continued proportion, and (3) the triplicate ratio follows from V.Def.10. The AI reaches conclusion (1) by citing 8.11 as a packaged result, while Heath derives it inline using VII.17 and VII.18 directly; the underlying geometric fact is identical. The ai_only set consists of definitions (D7.15, D7.18, D7.19), a common notion (CN1), commutativity (7.16), and 8.11 — all representing either over-citation of foundational items or a different citation depth for the same logical step. Since heath_only is empty, every citation Heath uses is also used by the AI. The backbones match with differing granularity, yielding G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing intermediate terms to form continued proportions among the squares and cubes, showing these continued proportions share a common ratio (since A:B = B:C), and applying ex aequali (7.14) to conclude D:E = E:F and G:H = H:K. The ai_only citations 7.17 and 7.18 are the explicit multiplication-proportion results that Heath uses implicitly through his phrase 'in manner similar to the foregoing' (referring back to 8.12, where 7.17 and 7.18 are cited explicitly). The AI spells out each application of 7.17 and 7.18 step by step, while Heath compresses these into a back-reference. Since heath_only is empty and the ai_only items represent over-citation of the same underlying reasoning, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 8.14
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same backbone: they establish a continued proportion via 8.11, apply 8.7 to derive divisibility of the mean term, and then use the ratio relationship to conclude divisibility of the sides (forward direction) or squares (converse). The citation differences reflect depth, not path: Heath cites D7.20 (definition of proportional numbers) to move directly from a ratio equality and a divisibility to the conclusion, while the AI explicitly cites 7.17 (products of a number multiplying two numbers have the same ratio as the multiplied numbers) and 7.20 (least numbers in ratio measure proportional numbers equally) to spell out the same inferential step at a finer grain. The AI's additional citation of D7.3 is likewise a definitional over-citation. The key intermediate conclusions are identical in both proofs at every logical position, making this a same-backbone, different-depth case.

### 8.15
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determines the classification. While Part (i) of the AI proof follows a similar backbone to Heath (using 8.12 for mean proportionals, 8.7 for divisibility in continued proportion, then establishing the ratio to conclude side divisibility), Part (ii) takes a fundamentally different path. Heath re-uses the same continued proportion construction (A, H, K, B in ratio C:D) for both directions, applying the converse reasoning with D7.20. The AI instead invokes 8.14 (the square analogue) to establish that a^2 measures b^2, then builds a divisibility chain using 7.17 and 7.20: first showing a^3 measures a^2*b (from a measuring b), then showing a^2*b measures b^3 (from a^2 measuring b^2), and concluding by transitivity that a^3 measures b^3. This is a genuinely different logical backbone for the converse direction, yielding different key intermediate conclusions (using the square result as a stepping stone rather than the continued proportion). The AI's path is logically complete and valid under Q3, so the classification is D.

### 8.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Both the AI and Heath proofs establish the same two-part contrapositive argument: (1) if the square does not measure the square, assume the side measures the side, then by 8.14 the square measures the square, contradiction; (2) if the side does not measure the side, assume the square measures the square, then by 8.14 the side measures the side, contradiction. The key intermediate conclusions and logical backbone are identical. The only citation difference is that the AI explicitly cites D7.18 (the definition of square numbers) in its setup, while Heath leaves this implicit. Since ai_used and heath_refs differ only by this definitional over-citation, this is a granularity difference (G) rather than a perfect match (P) or a path difference (D).

### 8.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs share the same logical backbone: a two-part contrapositive argument where each direction is proved by contradiction using 8.15. In Part 1, both assume the side measures the side, derive via 8.15 that the cube measures the cube, and reach a contradiction. In Part 2, both assume the cube measures the cube, derive via 8.15 that the side measures the side, and reach a contradiction. The only difference is that the AI explicitly cites D7.19 (definition of cube number) when setting up notation, while Heath does not cite any definition. Since D7.19 is a definitional citation representing over-citation rather than a substantive intermediate conclusion, this is a citation-depth difference with the same backbone, yielding G. The citation sets are not identical (ai_used includes D7.19 while heath_refs does not), so P is ruled out.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they set up similar plane numbers with proportional sides, construct a mean proportional number (Heath constructs G = D*E; the AI constructs M = c*f and uses 7.19 to show c*f = d*e, which is the same number), apply 7.17 twice to establish the continued proportion A:mean::mean:B, and then invoke V.Def.9 for the duplicate ratio. The difference lies in how a sub-step is justified: Heath uses 7.13 (alternation) to rearrange the proportion c:d = e:f into c:e = d:f, while the AI uses 7.19 (cross-multiplication property) to establish c*f = d*e directly, bypassing the need for alternation. The ai_only citation D7.16 is simply the definition of plane number (over-citation). Since the key intermediate conclusions are identical and only the justification technique for one sub-step differs, this is a same-backbone, different-depth case under Q2 Case A.

### 8.19
**Category**: Path difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Heath's proof constructs intermediate numbers K=CD and L=FG as similar plane numbers, applies 8.18 to find their mean proportional M=DF, uses 7.13 for alternation, then builds N=EM and O=HM to establish the continued proportion A,N,O,B. The AI proof takes a genuinely different path: it directly constructs P=a*e*c and Q=d*e*c, then uses 7.17 and 7.18 to show A:P=b:e, P:Q=a:d, and Q:B=c:f. Since the sides are proportional by similarity (D7.21), all three ratios are equal, giving continued proportion A,P,Q,B immediately without invoking 8.18 or 7.13. The key intermediate conclusions differ substantially: Heath routes through similar plane numbers and their mean proportional, while the AI constructs entirely different intermediates that avoid the plane-number machinery. Both paths are logically valid, making this a path difference.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they take D, E as the least numbers in the ratio A:C via 7.33, use 7.20 to decompose A and B into products (A = F*D, B = G*E), establish that A and B are plane numbers, and then show that D:E = F:G to conclude the sides are proportional and hence A, B are similar plane numbers. The citation difference arises because the AI uses 7.19 (product equality implies proportionality) to establish D:E = F:G directly from F*E = G*D, whereas Heath uses 7.17 twice to establish D:E = A:C and F:G = C:B, then chains these and applies 7.13 (alternation). Since 7.17 appears inside Heath's own proof of 7.19, this satisfies the proof-tree containment test: the AI cites 7.19 as a unit while Heath re-derives its internals inline. The AI's additional citations of 7.22, D7.16, and D7.21 are either explicit statements of facts Heath uses implicitly or supporting lemmas not strictly needed. This is a citation-depth difference with the same backbone, yielding G.

### 8.21
**Category**: Path difference
**Jaccard**: 0.308
**Analysis**: Q2 determined the classification. Heath's proof works through three least numbers in continued proportion (VIII.2), proves their extremes are prime (VIII.3), applies VIII.20 to conclude the extremes are similar plane numbers with identifiable sides, then uses ex aequali (VII.14) and VII.21 to establish the measurement relations, finally building the solid decomposition from plane-number sides. The AI takes a fundamentally different route: it works with the least four numbers in continued proportion e^3, e^2f, ef^2, f^3 (VIII.1, VIII.2), directly deduces A = ke^3 and B = kf^3 via VII.20, and factors these into sides (e, e, ke) and (f, f, kf) to show both are solid numbers with proportional sides. The backbones differ substantially: Heath relies on VIII.20 (similar plane numbers from one mean proportional), VIII.3 (prime extremes), VII.14 (ex aequali), and VII.21 (primes are least), none of which the AI uses. The AI instead relies on VIII.1 (least in continued proportion), VII.15, VII.17, and the explicit cubic structure. Since the AI's different path is logically complete and valid, this is a path difference.

### 8.22
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof pivots on a single structural result (8.20) that if one mean proportional falls between two numbers then they are similar plane numbers, and since A is square, C must also be square. The AI instead takes a direct algebraic route: using 7.19 to establish A*C = B*B from the continued proportion, then applying 8.14 to conclude that a (the side of the square A) divides B, and finally algebraically deriving C = c*c. The key intermediate conclusions are entirely different: Heath argues through 'A and C are similar plane numbers' while the AI argues through 'A*C = B*B' and 'a divides B'. The citation sets are completely disjoint (Jaccard = 0.0), confirming the path divergence. The AI's alternative route is logically sound and complete, so the classification is D (path difference).

### 8.23
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof has a two-step backbone: (1) since A and D have two mean proportionals between them, they are similar solid numbers by 8.21, and (2) since A is a cube and similar solid numbers to a cube are cubes, D is also cube. The AI proof takes a fundamentally different path: it finds the least numbers p, q in the ratio A:D (7.33, 7.22), uses 8.8 and 8.9 to show that continued proportions from unit to p and from unit to q exist, proves p and q are each cubes via arithmetic on those proportions, then uses 7.20 to establish that p measures A and q measures D the same number of times, applies 8.15 to show the cube root relationship transfers, derives that the common multiplier m is itself a cube, and concludes D = m*q is a product of two cubes and hence a cube. The Jaccard similarity of 0.0 (zero overlap between citation sets) reflects this genuine path divergence. The AI's proof is logically complete and valid throughout, establishing the conclusion through a longer but sound chain of number-theoretic reasoning rather than Heath's concise appeal to similar solid numbers.

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish that one mean proportional falls between the two given square numbers, (2) apply 8.8 to transfer the mean proportional relationship to A and B, (3) apply 8.22 to conclude B is square since A is square and A, E, B are in continued proportion. The sole difference is that Heath cites 8.18 (between two similar plane numbers there is one mean proportional) after noting that squares are similar plane numbers, while the AI cites 8.11 (between two square numbers there is one mean proportional), which is the specialization of 8.18 to square numbers. The AI also cites D7.18 (a definition), which Heath leaves implicit. These are citation-depth differences, not backbone differences, since the key intermediate conclusion — that a mean proportional exists between the two square numbers — is identical in both proofs.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that two mean proportionals exist between the given cube numbers C and D, (2) apply 8.8 to transfer those mean proportionals to A and B which have the same ratio, and (3) apply 8.23 to conclude B is cube since A is cube and four numbers are in continued proportion. The sole difference is how step (1) is justified: Heath cites 8.19 (mean proportionals between similar solid numbers) after noting that cube numbers are similar solids, while the AI cites 8.12 (mean proportionals between cube numbers) which applies directly. These are two independent propositions reaching the same intermediate conclusion, with 8.12 being a more specialized result for cubes and 8.19 being the general result for similar solids. Since the key intermediate conclusions are identical at every logical position and only the citation supporting one step differs, this is a citation-depth difference (Case A in Q2), yielding classification G.

### 8.26
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Heath's proof finds the least numbers D, E, F in the same ratio as A, C, B (using 7.33/8.2), then observes the extremes D, F are square (8.2), so A:B is a ratio of squares. The AI takes a fundamentally different route: it extracts the sides a, b from the similar plane numbers, constructs the explicit squares a^2 and b^2, uses 8.11 to establish a continued proportion a^2:(a*b):(b^2), then applies ex aequali (7.14) to conclude A:B = a^2:b^2. These are genuinely different backbones — Heath works with abstract least numbers in ratio while the AI works with concrete side-derived squares — so Q2 Case B applies. The AI's path is logically complete under Q3, with every step properly cited and sound, yielding category D.

### 8.27
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs share the initial step of using 8.19 to establish two mean proportionals between the similar solid numbers A and B, but they diverge completely after that. Heath's proof finds the least numbers in the same ratio (via 7.33/8.2) and shows their extremes are cubes (via 8.2), concluding that A:B equals a cube-to-cube ratio. The AI proof instead constructs explicit cube numbers a^3 and d^3 from the sides of the similar solid numbers, uses 8.12 to establish that between these cubes also fall two mean proportionals with the same common ratio a:d, then applies ex aequali (5.22) to conclude A:B = a^3:d^3, which is directly a cube-to-cube ratio. These are genuinely different logical backbones: Heath works through reduction to least numbers, while the AI works through explicit construction of cubes with matching continued proportions. The AI's path is logically complete and valid, yielding classification D.


## Book 9

| Category | Count |
|---|---|
| Perfect match (P) | 2 |
| Granularity difference (G) | 21 |
| Path difference (D) | 12 |
| AI proof error (E) | 1 |

**Total**: 36 propositions

### 9.1
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification. Heath's proof constructs D = A*A (square), establishes A:B = D:C via 7.17, transfers the mean proportional from (A,B) to (D,C) via 8.8, then applies 8.22 (if three numbers in continued proportion and the first is square, the third is square). The AI takes a fundamentally different route: it finds the mean proportional G between A and B via 8.18, then directly applies 7.19 to conclude A*B = G*G from the proportion A:G = G:B, making C = G^2 a square by definition. The AI never introduces D = A^2, never uses the ratio transfer (7.17, 8.8), and never invokes 8.22. These are genuinely different logical backbones producing different key intermediate conclusions, and the AI's path is logically sound at every step.

### 9.2
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification. Heath's proof constructs D=A*A (a square), establishes A:B = D:C via 7.17, then uses the fact that D and C are both similar plane numbers (squares) to find a mean proportional between D and C (8.18), transfers this to A and B via the same-ratio result 8.8, and finally applies 8.20. The AI takes a fundamentally different route: it directly extracts N from S=N*N (by D7.18), applies the converse of 7.19 to A*B=N*N to immediately establish A:N=N:B, and then applies 8.20. The AI bypasses Heath's entire intermediate construction involving D=A^2 and the chain 7.17/8.18/8.8. The proof-tree containment test confirms this is not a depth difference: while 7.19 does cite 7.17, the heath_only items 8.18 and 8.8 do not appear inside the proof of 7.19, so the AI is using a genuinely independent argumentative route. Both proofs are logically complete and arrive at the same conclusion via valid but different intermediate steps.

### 9.3
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decides the classification as D (path difference). Heath's proof establishes two mean proportionals between the unit and A (via VII.Def.20), then uses VIII.8 to transfer the continued proportion structure to the pair (A, B), and finally applies VIII.23. The AI proof takes a fundamentally different route: it decomposes A into a*a*a using D7.19, directly constructs four numbers A, A*a, A*(a*a), A*A in continued proportion using VII.17 and VII.18, and then applies VIII.23 to conclude A*A = B is cube. The AI never works with the unit or uses VIII.8 to transfer proportions; instead it explicitly builds the required continued proportion chain through multiplication properties. These represent genuinely different logical backbones — Heath argues by proportion transfer while the AI argues by direct construction — making this a path difference rather than a granularity difference.

### 9.4
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) D = A*A is cube by 9.3, (2) two mean proportionals exist between D and C, and (3) C is cube by 8.23. However, the route to establishing the mean proportionals between D and C differs substantively. Heath uses 8.19 (between similar solid numbers fall two mean proportionals) to get mean proportionals between A and B, then 8.8 to transfer those mean proportionals to D and C via the ratio A:B :: D:C. The AI instead uses 8.12 (between two cube numbers there are two mean proportionals) to get mean proportionals between A and B, then explicitly constructs the mean proportionals between D and C through three applications of 7.17 rather than using 8.8. Since 8.12 does not contain 8.19 in its proof tree (they are independent parallel results for cubes vs. similar solids), and 8.8 is replaced by explicit construction, the proof-tree containment test fails for both heath_only items, so Case A does not hold. Under Q3, the AI's different path is logically valid: 8.12 correctly provides mean proportionals for cubes, and the 7.17 construction soundly establishes the continued proportion D, G, H, C.

### 9.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same initial backbone: establishing D = A*A is cube via 9.3, then deriving the ratio A:B = D:C via 7.17. They diverge in how they conclude B is cube: Heath re-derives the internals of 8.25 inline by going through mean proportionals (8.19 to show two mean proportionals fall between cubes D and C, 8.8 to transfer this to A and B, then 8.23 to conclude B is cube from four numbers in continued proportion), while the AI directly cites 8.25 which packages exactly those three steps. The proof-tree containment test confirms this: all three heath_only citations (8.19, 8.8, 8.23) appear inside Heath's own proof of 8.25, so the AI is citing at a higher level of abstraction rather than taking a genuinely different path. The ai_only definitions D7.15 and D7.19 are simple over-citation of definitions, a hallmark of granularity difference.

### 9.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this classification as G (granularity difference) via the proof-tree containment test. The AI proof reduces 9.6 to 9.5 by showing that B = A*A is cube (hypothesis), B*A = A^3 is cube (by D7.19), and then applying 9.5 (if a cube times a number gives a cube, that number is cube) to conclude A is cube. Heath's proof instead re-derives the internal machinery of 9.5 inline, establishing proportion chains (unit:A = A:B = B:C via D7.20), invoking 8.19 for mean proportionals between similar solid cubes, transferring via 8.8, and concluding via 8.23. All three substantive heath_only propositions (8.19, 8.8, 8.23) appear inside Heath's own proof of 9.5, satisfying the containment test: the AI cites 9.5 as a single higher-level unit while Heath re-derives 9.5's internals. This is a citation-depth difference, not a backbone difference.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) since A is composite, it is measured by some number (D7.13); (2) express A as a product of two factors using the definition of multiplication (D7.15); (3) the final product is therefore the product of three numbers, making it solid. The AI proof explicitly cites D7.16 (plane number definition) and D7.17 (solid number definition) to formally label A as plane and the result as solid, while Heath applies these same concepts implicitly without citing the definition numbers. The ai_only set contains only definitions (D7.16, D7.17), and heath_only is empty, confirming this is a citation-depth difference rather than a path difference. This is Case A in Q2: same backbone, different citation depth, yielding G.

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this as G (granularity difference). Both proofs share the same logical backbone: (1) show the third term from unit is square because A*A = B, (2) extend to all odd-indexed terms via VIII.22, (3) show the fourth term is cube because A*A*A = C, (4) extend to all terms leaving out two via VIII.23, (5) conclude the seventh term is both cube and square. The only difference is in which definitions are explicitly cited: the AI cites D7.15 (multiplication), D7.18 (square), and D7.19 (cube) while Heath cites D7.20 (proportional numbers). Both proofs use 8.22 and 8.23 as the key propositions. Since all ai_only and heath_only items are definitions used at the same logical positions within the same argumentative structure, this is a citation-depth difference, not a path difference.

### 9.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification as G (Granularity difference). The AI proof and Heath's proof share the same logical backbone for the square case stated in the proposition: both establish that B (the third from the unit) is square via 9.8, then use 8.22 iteratively on consecutive triples to show C, D, E, etc. are all square. The heath_only citations (8.23, 9.3) appear exclusively in Heath's proof of the cube extension case, which goes beyond the stated proposition; they do not represent a different backbone for the square case. The ai_only citation (D7.18) is a definition reference (square number), representing an over-citation of foundational definitions. Since both proofs argue through identical key intermediate conclusions for the proposition as stated, with differences only in citation depth and scope of coverage, this is a granularity difference.

### 9.10
**Category**: Path difference
**Jaccard**: 0.2
**Analysis**: Both proofs use contradiction to show no odd-positioned term is square when A is not square, and both use 9.8 to establish even-positioned terms are square. However, the logical routes diverge at the critical step. Heath uses the ratio argument: B:C = square:square, so A:B = square:square, then by 8.26 converse A and B are similar plane numbers, hence A is square. The AI uses the product argument: A^(k-1)*A = A^k is square, so by 9.2 A^(k-1) and A are similar plane numbers, then by D7.18/D7.21 (definitions of square and similar plane numbers) the equal sides of A^(k-1) force A to have equal sides, making A square. The key intermediate 'ratio is square-to-square' (Heath) vs 'product is square triggering 9.2' (AI) are substantively different routes to the similar-plane-numbers conclusion. Both are logically complete. Scope note: the cube case in Heath's proof is excluded from comparison since proposition 9.10 only asks about the square case.
### 9.11
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath's proof uses a specific proportional relationship (A:B = D:E from the continued proportion) and then applies alternation via 7.15 to conclude that the unit measures D the same number of times as B measures E, thereby establishing the measurement result. The AI proof takes a fundamentally different algebraic approach: it represents each term Ak in the geometric sequence as A2^(k-1), then shows that Aj = Ai times Aj-i+1 by direct computation of powers, concluding that Ai measures Aj according to the proportional number Aj-i+1. These are genuinely different logical backbones — Heath relies on the alternation property of proportions while the AI relies on the explicit multiplicative/power structure of the geometric sequence. The AI's path is logically valid under Q3, as the chain from premises to conclusion is sound, yielding classification D.

### 9.12
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determined the classification. Heath proves 9.12 by contradiction: assuming the prime E does not measure A, he uses coprimality (7.29), least ratio properties (7.21, 7.20), and proportionality (7.19) to descend through the geometric sequence and derive a contradiction. The AI instead gives a direct proof by descent using 7.30 (if a prime measures a product it measures one of the factors): from E = A*D it applies 7.30 to get p|A or p|D, and if p|D then D = A*C yields p|A or p|C, continuing until reaching B = A*A where 7.30 forces p|A. The two proofs have fundamentally different logical backbones -- Heath relies on the coprimality/ratio chain (7.29, 7.21, 7.20) while the AI relies on the prime product divisibility theorem (7.30). The AI's approach is mathematically valid, constituting a sound alternative path to the same conclusion, so the classification is D.

### 9.13
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: proof by contradiction assuming a divisor E not among the proportional numbers, showing E cannot be prime (via 9.12), that E must be divisible by A (the number after unity) using 7.31 and 9.12, then performing a descent through the sequence terms until reaching the prime A itself, yielding a contradiction. The citation differences are purely about depth: the AI uses 7.17 (equal products imply same ratio when multiplied by same number) where Heath uses 7.19 (the proportion-from-equal-products result) for the same logical step of concluding that quotients measure earlier terms. Heath explicitly cites 9.8 for the fact that A multiplied by itself makes B (the square property of the third term), while the AI handles this implicitly through the general descent argument recognizing proportional numbers as powers of A_2. The AI's additional citations of definitions (D7.3, D7.11, D7.15) and 7.20 (transitivity of measurement) represent over-citation of foundational facts that Heath leaves implicit. All key intermediate conclusions are established in both proofs at the same logical positions, making this a citation-depth difference rather than a path difference.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: assume a new prime measures A, express A as a product of that prime and a cofactor, apply 7.30 to conclude the original primes must measure the cofactor, and derive a contradiction with minimality. The AI proof adds explicit intermediate steps that Heath leaves implicit: it cites 7.29 to establish that each original prime is coprime to the new prime before applying 7.30, and explicitly invokes definitions (D7.11, D7.15, D7.3) and CN5 for steps Heath handles without citation. All ai_only items (7.29, CN5, D7.11, D7.15, D7.3) represent over-citation of definitions, common notions, and a sub-lemma that Heath subsumes into the direct application of 7.30. The heath_only set is empty, confirming the AI covers all of Heath's cited material. This is a clear Case A: same backbone, different citation depth.

### 9.15
**Category**: Path difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. For the first two sub-cases (A+B prime to C, and B+C prime to A), both proofs share the same backbone: establish a,b coprime (7.22), their sum coprime to each (7.28), then use 7.25 and 7.24 to show the result. The AI omits the explicit citation of II.3 for the factoring but achieves the same intermediate conclusion, which alone would be a granularity difference. However, for the third sub-case (A+C prime to B), the proofs take genuinely different paths. Heath uses II.4 to expand (DE+EF)^2, establishes that this square is coprime to DE*EF, then applies separando twice to conclude that DE^2+EF^2 is coprime to DE*EF. The AI instead uses a direct divisibility argument: assuming d divides both a^2+b^2 and a, it shows d must divide b^2, but since b^2 is coprime to a (by 7.25) and d divides a, d must be unity. This proves a^2+b^2 is coprime to a (and symmetrically to b), then invokes 7.24 to get coprimality with ab. This is a valid but structurally different logical path that does not pass through II.4 or the separando steps at all, constituting a genuine path difference under Q2 Case B, confirmed valid under Q3.

### 9.16
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof reaches contradiction via the ratio-minimality route: since A and B are prime they are the least numbers in that ratio (7.21), so A measures B (7.20), contradicting coprimality. The AI proof takes a fundamentally different path through product arithmetic: from A:B = B:C it derives A*C = B*B (7.19), then uses the fact that B*B is prime to A (7.25) to show A must be the unit, contradicting A being a number. The key intermediate conclusions are entirely different — Heath's backbone is 'least ratio implies measuring' while the AI's backbone is 'product equality plus coprimality of square implies A is a unit.' The citation sets are completely disjoint (Jaccard = 0.0), and the proof-tree containment test confirms neither AI-cited proposition subsumes the Heath-cited ones. Both proofs are logically complete, so Q3 confirms the AI's different path as valid, yielding category D.

### 9.17
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof uses alternation (7.13) to convert the assumed proportion into A:D = B:E, then applies 7.21 (primes are least in their ratio) and 7.20 to conclude A measures B, and cascades through the continued proportion to show A measures D, contradicting coprimality. The AI proof takes a fundamentally different route: it uses 7.33 to find the least numbers F,G in the ratio A_1:A_2, applies 7.20 to show F divides both A_1 and A_n, uses coprimality (D7.12) to conclude F is a unit, then derives the multiplicative structure A_k = G^{k-1}*A_1 to show A_1 divides A_n, and uses D7.2 to establish A_1 is not a unit, reaching a contradiction. The key intermediate conclusions differ: Heath argues through alternation and a divisibility cascade (A|B, then A|C, then A|D), while the AI argues through least-ratio representatives and multiplicative structure (F=unit, then A_1|A_n directly). Both paths are logically complete, making this a genuine path difference.

### 9.18
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: compute B squared, check whether A measures it, and if so use 7.19 to establish the proportionality A:B = B:D, otherwise prove impossibility by contradiction. Heath separately handles the case where A and B are prime to one another by citing 9.16 before proceeding to the general case, while the AI subsumes this under its general criterion (A measures B squared or not), which is exhaustive and implicitly covers the prime case. The ai_only items D7.15 and D7.3 are definitions the AI cites for explicitness that Heath uses implicitly. The heath_only item 9.16 is not evidence of a different path but rather of Heath citing a previously proven special case that the AI handles through its more direct general argument. The key intermediate conclusions (third proportional exists iff A measures B squared, established via 7.19 and contradiction) are identical in both proofs, making this a citation-depth difference rather than a path difference.

### 9.19
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification. Heath's proof is a multi-case argument that distinguishes four scenarios based on whether the three numbers are in continued proportion and whether the extremes are prime to one another, using 9.17 for the continued-proportion-with-primes case, 7.14/7.21/7.20 for the non-continued-proportion-with-primes case, and 7.19 for the remaining cases where A measures B*C. The AI proof takes a fundamentally different path: it gives a single unified criterion that a fourth proportional exists if and only if A measures B*C, proved entirely via 7.19 and definitions. The AI avoids all case-splitting by primality or continued proportion, instead reducing the problem to a single divisibility condition. This constitutes a genuinely different logical backbone (Q2 Case B). Under Q3, the AI's path is logically valid: the forward direction constructs D from the divisibility, and the reverse direction uses contradiction via 7.19's product-proportion equivalence. The proof is complete and sound, yielding classification D.

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a number divisible by all given primes (Heath uses the LCM, the AI uses the product), add a unit, then consider two cases -- if the result is prime, it is a new prime; if not, by 7.31 some prime divides it, and that prime cannot be any of the given primes because it would then have to divide the unit, a contradiction. The key intermediate conclusions are identical in both proofs. The AI's ai_only citations (CN5, D7.11, D7.13, D7.15, D7.3, D7.5) are all definitions and common notions that Heath invokes implicitly without citation, representing over-citation rather than a substantive path difference. With heath_only empty and the backbones matching, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 9.21
**Category**: Granularity difference
**Jaccard**: 1.000
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusion: each even number has a half part (by D7.6), therefore the whole sum also has a half part, therefore the whole is even. The citation sets are identical (both cite only D7.6), with Jaccard 1.0 and empty ai_only and heath_only sets. The difference is purely one of exposition depth: Heath states directly that since each part has a half, the whole has a half; the AI proof elaborates this with an explicit inductive argument showing the base case (sum of two even numbers) and the inductive extension. This additional detail constitutes a granularity difference (Case A of Q2) rather than a path difference, since the underlying logical backbone and citations are the same.

### 9.22
**Category**: Path difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Heath's proof decomposes each odd number individually by subtracting a unit (D7.7), sums the even remainders via 9.21, notes the multitude of units is even, and adds the two even sums via 9.21 again. The AI proof takes a fundamentally different approach: it pairs the odd numbers (since their multitude is even, via D7.6), shows each pair of odd numbers sums to an even number using D7.7 and algebra, then sums all the even pair-sums via 9.21. The key intermediate conclusions differ — Heath's backbone has 'sum of remainders is even AND sum of units is even' while the AI's backbone has 'each pair of odd numbers sums to even.' Since these are different backbones (Case B in Q2), the proof proceeds to Q3 where the AI's alternative path is verified as logically complete, yielding classification D.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof cite the identical set {9.21, 9.22, D7.7} (Jaccard 1.0) and argue through the same key intermediate conclusions: separating the odd-count collection into an even-count subcollection whose sum is even (9.22) plus one remaining odd number, decomposing that odd number into an even part plus a unit (D7.7), combining the two even parts via 9.21, and concluding the total is odd by D7.7. No forward dependencies, no logical errors, no missing cases, and no citation differences exist. The perfect-match check at the end of the protocol confirms category P.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) AB is even so it has a half part, (2) BC is even so it has a half part, (3) the remainder CA therefore also has a half part and is even. The AI makes the subtraction step explicit by citing CN3 (equals subtracted from equals leave equal remainders) and introduces named quantities D and E as the halves, while Heath leaves the subtraction implicit and simply states the remainder also has a half part. The single ai_only item CN3 is a Common Notion (axiom) that justifies a step Heath performs without explicit citation, making this a citation-depth difference rather than a backbone difference. Case A of Q2 holds, yielding Granularity difference (G).

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow the identical logical backbone with the identical citation set. Both proofs (1) subtract the unit CD from odd BC to obtain even BD/DB via Definition VII.7, (2) conclude that the remainder AD is even since both AB and BD are even by Proposition IX.24, and (3) deduce that AC/CA is odd because it differs from the even number AD by the unit CD, again invoking Definition VII.7. The citation sets are exactly equal (ai_used = heath_refs = {9.24, D7.7}), yielding Jaccard 1.0, and the key intermediate conclusions match at every stage. Since both the logical backbone and the citation sets are identical, the classification is P (Perfect match).

### 9.26
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: subtract a unit from each odd number to obtain two even numbers (by D7.7), then apply 9.24 (even minus even is even) to conclude the remainder is even. The AI's only additional citation is CN3, a common notion used to explicitly justify the algebraic step of canceling the equal units (BD = BE) when showing AC = AD - CE. Heath performs the same reasoning but treats the cancellation as implicit. Since heath_only is empty and ai_only contains only a common notion (axiom-level over-citation), this is a citation-depth difference with the same key intermediate conclusions, yielding Granularity difference (G).

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath proves 9.27 directly: he subtracts a unit from the odd number to obtain an even number, then applies 9.24 (even minus even is even) to show an intermediate remainder is even, and concludes via D7.7 that the target remainder is odd. The AI instead uses proof by contradiction: it assumes the remainder is even, then applies 9.21 (sum of even numbers is even) to show the original odd number would be even, reaching a contradiction. These are fundamentally different proof strategies with different key intermediate conclusions -- Heath's backbone relies on unit subtraction and 9.24, while the AI's backbone relies on the contrapositive reasoning via 9.21. Since the AI's contradictory path is logically sound and complete, this is a valid path difference (D).

### 9.28
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) C is made up of as many copies of B as there are units in A (by D7.15), (2) since B is even, all summands are even, and (3) by 9.21, the sum of even numbers is even, so C is even. The only citation difference is that the AI explicitly cites D7.6 (definition of even number) when noting B is even, while Heath simply states the fact without citing the definition. This is a classic over-citation of a definition, a citation-depth difference that does not alter the logical backbone. Since the key intermediate conclusions are identical and the difference is purely in citation granularity, the classification is G. The citation sets are not identical (ai_only contains D7.6), so P does not apply.

### 9.29
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: (1) by the definition of multiplication (D7.15/VII.Def.15), the product C equals A copies of B; (2) since each copy B is odd and the number of copies A is odd, we have an odd multitude of odd numbers; (3) by 9.23/IX.23, the sum of an odd number of odd addends is odd, so C is odd. The only citation difference is that the AI explicitly cites D7.7 (the definition of odd number) when identifying A and B as odd, whereas Heath treats oddness as directly given by hypothesis without citing the definition. This is a shallow over-citation of a definition, not a path divergence, placing the proof squarely in the granularity-difference category.

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) A (odd) measures B (even) so B = A times some multiplier, (2) proof by contradiction that the multiplier cannot be odd because that would make B odd, contradicting B being even, (3) the multiplier is therefore even, (4) A therefore measures the half of B. The only difference is citation depth. Heath cites 9.23 directly (sum of an odd count of odd numbers is odd) to establish that the product of two odd numbers is odd, while the AI cites 9.29 (product of two odd numbers is odd), which itself uses 9.23 in its proof per the proof-tree containment test. The AI's remaining ai_only citations (7.5, CN3, D7.15, D7.3, D7.6, D7.7) are definitions, common notions, and basic propositions that make explicit what Heath leaves implicit in the final steps. This is a citation-depth difference with identical backbone, confirming Case A of Q2.

### 9.31
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: a proof by contradiction where one assumes the odd number A and the double of B share a common measure, shows that common measure must be odd, applies 9.30 to conclude it also measures B, and derives a contradiction with the coprimality of A and B. The only difference is in how the oddness of the common measure is established: Heath leaves it implicit (a measure of an odd number is odd), while the AI explicitly argues via 9.21 that if the common measure were even, A would be a sum of even numbers and hence even, contradicting the hypothesis. The AI also over-cites several definitions (D7.12, D7.3, D7.5, D7.6, D7.7) that Heath leaves implicit. Since heath_only is empty and all ai_only items are either definitions or a theorem used to make explicit a step Heath takes implicitly, this is a same-backbone, different-depth scenario — Case A of Q2.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they set up the sequence of powers of 2 as a continued proportion from unity with the prime number 2 after the unit, invoke Proposition 9.13 to establish that the only divisors are the powers of 2 in the sequence, observe that all these divisors (except unity) are even, and conclude even-times even only via Definition 7.8. The AI proof makes additional explicit steps (showing 2^k is not even-times odd by contradiction in Step 6) and cites three extra definitions (D7.11 for prime, D7.6 for even, D7.9 for even-times odd) that Heath leaves implicit. Since heath_only is empty and the ai_only items are all definitions providing explicit grounding for facts Heath treats as obvious, this is a clear case of same backbone with different citation depth.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Both proofs share the same logical backbone: (1) the half of the number is odd, so the number is even-times odd by D7.9; (2) assume for contradiction the number is also even-times even per D7.8; (3) then the half would be measured by an even number, making it even; (4) but the half is odd, contradiction; (5) therefore the number is even-times odd only. The AI proof is substantially more verbose, explicitly unpacking foundational definitions (D7.6 for even, D7.7 for odd, D7.15 for multiplication) and CN2 (adding equals to equals) that Heath treats as implicit. Since heath_only is empty and ai_only contains only definitions and a common notion, this is a clear case of the AI over-citing foundational items while following the identical argument structure. Q2 Case A applies: same backbone, different citation depth, yielding classification G.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decides this as Granularity difference (G). Both proofs establish the same two key intermediate conclusions: (1) the number is even-times even because its half is not odd, appealing to D7.8, and (2) the number is even-times odd via repeated bisection until an odd factor is reached, with a contradiction argument that otherwise the number would be among those continually doubled from a dyad. The AI proof makes these steps more explicit by citing D7.6 (definition of even), D7.9 (definition of even-times odd), and 9.32 (characterizing doubled-from-dyad numbers as even-times even only), while Heath leaves these definitional and propositional references implicit. The AI also lists 9.33 in its USED citations though it is not explicitly invoked in the proof steps. The heath_only set is empty, confirming no step present in Heath is missing from the AI. This is Case A of Q2: same logical backbone with different citation depth.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they apply separando (VII.11) to derive equal ratios among consecutive differences, then use the antecedents-to-consequents principle (VII.12) to aggregate the differences and terms, arriving at the conclusion that the excess of the last over the first is to the sum of all preceding terms as the excess of the second over the first is to the first. Heath also references VII.13 in a combined annotation with VII.11 for the separando step, which the AI makes more explicit as a separate alternando application. The only citations in ai_only are CN1, CN2, and CN3, which are common notions (basic axioms for equality and addition/subtraction) that Heath uses implicitly without citation. Since heath_only is empty, every substantive proposition Heath cites is also cited by the AI. The key intermediate conclusions are identical in both proofs, with the AI simply over-citing foundational axioms, making this a citation-depth difference rather than a path difference.

### 9.36
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) using 9.35 to establish the sum of the geometric series, (2) enumerating all divisors of the product P = S * A(n-1) using the primality of S and 9.13, (3) summing all proper divisors to show they equal P, and (4) concluding P is perfect by D7.22. The large symmetric difference (Jaccard 0.25) is explained by citation-depth differences: the AI cites 7.24 as a unit, while Heath re-derives the same reasoning inline using 7.19, 7.20, and 7.21 — all three of which appear inside Heath's own proof of 7.24, satisfying the proof-tree containment test. Similarly, Heath uses 7.14 (ex aequali) for proportion manipulation where the AI uses direct algebraic reasoning, and the AI cites 9.11, 7.16, and several definitions (D7.11, D7.15, D7.3, D7.5) that Heath leaves implicit. These are all citation-granularity differences, not backbone differences, yielding G.


## Book 10

| Category | Count |
|---|---|
| Perfect match (P) | 1 |
| Granularity difference (G) | 79 |
| Path difference (D) | 32 |
| AI proof error (E) | 3 |

**Total**: 115 propositions

### 10.1
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) invoke the Archimedean property (D5.4) to find a multiple of C exceeding AB, (2) partition that multiple into parts reaching down to C, (3) perform successive subtractions of more-than-half from AB, (4) compare the remainders of AB at each stage with the corresponding parts of DE, showing AB's remainder is always smaller, and (5) conclude that the final remainder is less than C. The AI's only additional citation is CN5 (the whole is greater than the part), which is a Common Notion — an axiom-level fact that Heath uses implicitly but does not cite. The AI constructs DE by successive doubling rather than Heath's arbitrary multiple divided into equal parts, but this is a presentational variation, not a different logical path. Since the key intermediate conclusions are the same and the citation difference is limited to an over-cited common notion, this is a granularity difference.

### 10.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs use the same logical backbone: assume commensurability, deduce that a common measure must divide every successive remainder in the anthyphairesis, show that a remainder eventually becomes smaller than the common measure, and reach a contradiction. Heath's proof leaves all proposition and definition citations implicit, resulting in an empty heath_refs set. The AI explicitly cites 10.1 (to justify that the decreasing remainders eventually fall below the common measure), CN3 (for the subtraction reasoning that the common measure divides each remainder), D10.1.1 (definition of commensurable), and D5.1 (a part cannot exceed its whole). These are all citations that make explicit what Heath treats as obvious, representing a citation-depth difference rather than a path divergence. The key intermediate conclusions are identical in both proofs.

### 10.3
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) if the smaller measures the larger, it is the GCM; (2) otherwise apply antanairesis, which terminates by 10.2 since the magnitudes are commensurable; (3) the last remainder is a common measure (shown by tracing backwards through the subtraction chain); (4) it is the greatest common measure (any other common measure must measure the last remainder, so cannot exceed it). The AI proof explicitly cites CN3, CN5, D10.1.1, and D5.1 where Heath leaves these foundational items implicit. Since all ai_only items are common notions and definitions (not substantive propositions) and heath_only is empty, this is a citation-depth difference with the same backbone, yielding G.

### 10.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: find the GCM of two of the three magnitudes (D), show that D is commensurable with the third magnitude (C), find the GCM of D and C, then prove this is the GCM of all three. Heath splits into two explicit cases (D measures C vs D does not measure C), while the AI gives a single unified argument that demonstrably covers both cases, so no missing-case error arises under Q1(a). The ai_only citations (D10.1.1, D5.1) are definitions that Heath invokes implicitly without citation, representing a citation-depth difference rather than a substantive divergence. The method of proving maximality differs slightly (Heath uses contradiction, AI uses a direct divisibility argument), but both establish the same key intermediate conclusion. Since the backbone is the same and the citation differences are all definitional, this is a granularity difference (G).

### 10.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof establishes the ratio A:B = D:E by building intermediate ratios (C:A = unit:D via VII. Def. 20, inverting to A:C = D:unit via V.7, similarly C:B = unit:E) and then combining them ex aequali via V.22. The AI proof takes a fundamentally different path: it expresses A = D*C and B = E*C, then uses V.3 to show mA = mD*C and nB = nE*C, and directly verifies the trichotomy condition of Definition V.5 by comparing integer multiples of the same magnitude C. The AI never establishes intermediate ratios or uses ratio inversion/composition; instead it works from first principles with the definition of equal ratio. The completely disjoint citation sets (Jaccard = 0.0) reflect this genuine structural difference in logical backbone, not merely a difference in citation granularity.

### 10.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs reach the same final conclusion (B = E*C, so C is a common measure of A and B), but they argue through fundamentally different logical backbones. Heath works entirely within the proportion theory of Book 5: he constructs an auxiliary magnitude F = E*C, establishes ratios via D7.20, inverts with V.7, composes ex aequali with V.22, applies transitivity via V.11, and concludes B = F from equal ratios via V.9. The AI instead takes an equimultiple/algebraic approach: it applies the definition of same ratio (D5.5) with specific equimultiples p=E and q=D, uses commutativity of number multiplication (7.16) to rearrange, and cancels via CN3 to derive B = E*C directly. The citation sets are completely disjoint (Jaccard = 0.0), reflecting the genuine path divergence. Since the AI's algebraic chain is logically sound and complete, this is a valid different path, yielding category D.

### 10.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use identical proof-by-contradiction structure: assume A has to B the ratio of a number to a number, apply 10.6 to conclude A and B are commensurable, then derive a contradiction with the hypothesis that A and B are incommensurable. The key intermediate conclusion (commensurability via 10.6) is the same in both proofs at the same logical position. The only citation difference is that the AI explicitly cites D10.1.1 (definition of incommensurable magnitudes) while Heath leaves this implicit. Since ai_only contains only a definition and heath_only is empty, this is a citation-depth difference at the definitional level, making it a granularity difference (G) rather than a perfect match (P), as the citation sets are not identical.

### 10.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the same reductio ad absurdum backbone: assume A and B are commensurable, apply 10.5 to conclude they would have a number-to-number ratio, note the contradiction with the hypothesis, and conclude incommensurability. The AI's only extra citation is D10.1.1 (the definition of commensurable/incommensurable magnitudes), which the AI explicitly invokes when setting up the assumption and stating the conclusion. Heath uses the same concept without citing the definition explicitly. Since heath_only is empty and ai_only contains only a definition, this is a pure citation-depth difference with identical logical backbone, yielding G.

### 10.9
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decides: both proofs share the same four-part backbone (commensurable implies square-number ratio, its converse, and the two contrapositive parts). The key intermediate conclusions are identical: ratio of lengths equals ratio of numbers via 10.5, duplicate-ratio argument via 6.20/8.11 gives ratio of squares equal to ratio of square numbers, and the converse via 10.6. The AI additionally cites 6.22 (proportionality of similar figures on proportional lines) as an explicit step where Heath achieves the same conclusion directly from 6.20, and cites D7.18 (definition of square numbers) which Heath leaves implicit. heath_only is empty, confirming no substantive steps are missing from the AI proof. Since the backbones match and the citation differences are purely depth-of-citation matters, this is a granularity difference.

### 10.10
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 reveals different backbones in how each proof establishes that the second found line is incommensurable in square with the assigned line. Heath uses V. Def. 9 to obtain the proportion A:D = sq(A):sq(E) from the mean proportional, then applies 10.11 (proportional transfer of incommensurability) to conclude sq(A) incommensurable with sq(E). The AI instead uses 6.17 to show sq(C) = rect(A,B) from the mean proportional, then 6.1 to derive sq(A):sq(C) = A:B, then applies 10.7 and 10.8 directly to conclude incommensurability of the squares. These are genuinely different logical routes: Heath relies on the high-level proportional transfer theorem 10.11, while the AI builds the ratio relationship through rectangle-proportion machinery (6.1, 6.17) and applies the lower-level number-ratio criteria (10.7, 10.8) that are internal to 10.11. The containment test does not apply here because the AI cites lower-level rather than higher-level propositions. Since the AI's chain is logically sound from premises to conclusion, Q3 yields D.

### 10.11
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs handle the same two cases (commensurable and incommensurable) and establish the same key intermediate conclusions: in Case 1, A:B is a ratio of numbers (10.5), therefore C:D is a ratio of numbers (proportion transfer), therefore C is commensurable with D (10.6); in Case 2, A:B is not a ratio of numbers (10.7), C:D is not a ratio of numbers, therefore C is incommensurable with D (10.8). The AI uses a proof by contradiction in the incommensurable case (Step 6) rather than Heath's direct transfer, but both arrive at the same intermediate conclusion that C:D is not a ratio of numbers, and both cite the same four propositions (10.5, 10.6, 10.7, 10.8). The only citation difference is that the AI additionally cites D5.6 (definition of proportion), which is a definition over-citation rather than a substantive path difference. This is Case A in Q2: same backbone, different citation depth, yielding G.

### 10.12
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same endpoints: establishing that A:C and C:B are numerical ratios (via 10.5), combining them via ex aequali (5.22), and concluding commensurability (10.6). However, the mechanism for making the middle terms equal differs substantively. Heath constructs numbers in continued proportion using VIII.4 and applies transitivity of ratios (V.11) to link back to the original magnitudes. The AI instead directly scales the numerical ratios using arithmetic (7.17) to force a common middle term, inverts the second ratio using 5.7, and confirms products are numbers via 7.19. These are genuinely different techniques — arithmetic scaling versus geometric construction of continued proportionals — making this Case B (different backbone). Q3 confirms the AI's path is valid: every step is cited and the inferences are sound, so the classification is D.

### 10.13
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume for contradiction that B is commensurable with C, then since A is commensurable with B and B is commensurable with C, apply 10.12 (transitivity of commensurability) to conclude A is commensurable with C, contradicting the hypothesis that A is incommensurable with C. The only difference is that the AI explicitly cites D10.1.1 (the definition of commensurable and incommensurable magnitudes) at multiple steps, while Heath leaves this definitional reference implicit. Since the key intermediate conclusions are the same and the citation difference is limited to an additional definition, this is a granularity difference (G). The citation sets are not identical (ai_used includes D10.1.1 which heath_refs does not), so it cannot be P.

### 10.14
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) establish sq(A):sq(B) :: sq(C):sq(D) via 6.22, (2) derive the crucial ratio A:E :: C:F, and (3) apply 10.11 to transfer commensurability or incommensurability. The difference lies in how each proof gets from conclusion 1 to conclusion 2: Heath uses separando (5.17) to get sq(E):sq(B) :: sq(F):sq(D), then 6.22 for E:B :: F:D, inversion, and ex aequali (5.22) to reach A:E :: C:F; the AI uses convertendo (5.19) to go directly from sq(A):sq(B) :: sq(C):sq(D) to sq(A):sq(E) :: sq(C):sq(F), then the converse of 6.22 to get A:E :: C:F. These are different proportion-theory manipulations achieving the same intermediate result, representing a citation-depth difference rather than a structural divergence. The ai_only items 1.47, D5.5, P1, P3 are construction/axiom over-citations typical of granularity differences, while the substantive difference (5.19 vs 5.17+5.22) reflects a more direct vs multi-step algebraic route to the same key conclusion.

### 10.15
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath proves both parts of 10.15 using a direct common-measure argument: a magnitude D that measures the parts also measures the whole (Part I), and a magnitude D that measures the whole and one part also measures the remainder (Part II), citing only Definition 10.1.1. The AI takes a fundamentally different path through proportion theory: it converts commensurability into numerical ratios via 10.5, applies componendo (5.18) and separando (5.17) to manipulate those ratios, then converts back via 10.6, using transitivity of commensurability (10.12) to complete Part I. These represent genuinely different logical backbones — Heath works with existential common measures while the AI works with numerical ratios and proportion operations — constituting Case B (different backbone). Q3 confirms the AI's path is logically valid: all citations (10.5, 10.6, 10.12, 5.17, 5.18) correctly support their claimed inferences, and the chain from premises to conclusion is complete in both parts.

### 10.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: a proof by contradiction for both the forward direction (if AB, BC incommensurable then AC incommensurable with each) and the converse (if AC incommensurable with AB then AB, BC incommensurable). In each case, the contradiction arises from showing that the assumed commensurability would force the supposedly incommensurable magnitudes to be commensurable. The difference is purely one of citation depth: Heath argues directly using a common measure D and the fact that a measure of the whole and a part also measures the remainder, while the AI packages this same reasoning by citing 10.15 (the commensurable analogue), which is essentially the contrapositive. Heath's own proof of 10.15 contains exactly the elementary reasoning that Heath re-derives inline in 10.16, confirming this is a depth-of-citation difference rather than a different logical path. The ai_only set contains only 10.15, and heath_only is empty, consistent with the AI citing at a higher level what Heath proves from scratch.

### 10.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs establish the same key intermediate conclusions: (1) using II.5 to derive the algebraic identity relating the squares, (2) identifying the excess square as the square on a specific line segment (DF in Heath, AE-EB in AI), and (3) using transitivity chains with X.15, X.6, and X.12 to establish commensurability in both the forward and converse directions. The ai_only set {10.5, 5.15, CN1, CN3} represents over-citation: CN1 and CN3 are common notions Heath uses implicitly, while 10.5 and 5.15 are used by the AI in the converse direction to convert from commensurability of doubles (2*AE, 2*EB) to commensurability of AE and EB via numerical ratios, whereas Heath achieves the same conclusion more directly through X.15 separando. Since heath_only is empty and the AI's extra citations merely elaborate steps that Heath compresses, this is a same-backbone, different-depth situation fitting Case A of Q2.

### 10.18
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 identifies different logical backbones in the commensurability chains. Heath's proof references 10.17 for the construction and then establishes incommensurability through a direct chain: BD incomm DC implies BC incomm CD (10.16), DC comm with BF+DC (10.6), BC incomm with BF+DC (10.13), hence BC incomm FD (10.16). The AI instead re-derives the construction from scratch using 2.5 and 1.10, then uses a fundamentally different strategy: it works through the midpoint E to prove EC and ED are incommensurable by contradiction (using 10.15 and 10.12), then transfers this incommensurability to BC and DF via proportional magnitudes (10.11). These are genuinely different intermediate conclusions, not merely different citation depths. The AI's path is logically valid and complete, so Q3 yields D.

### 10.19
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct the square on one side, establish it is rational, use VI.1 (6.1) to relate the rectangle to the square via the ratio of the bases, show commensurability of the rectangle with the square, and conclude the rectangle is rational. The key difference is citation depth: Heath cites 10.11 directly to move from the proportion and commensurability of bases to commensurability of areas, while the AI re-derives 10.11's internals inline using 10.5 (commensurability implies number ratio) and 10.6 (number ratio implies commensurability). The proof-tree containment test confirms that 10.5 and 10.6 appear inside Heath's proof of 10.11, so the AI is simply unpacking that lemma. The AI also makes explicit the transitivity of commensurability via 10.12 and cites D10.1.3 for the definition of rational lines, which Heath leaves implicit. These are all citation-depth differences, not backbone differences, yielding a Granularity classification.

### 10.20
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: establish that the applied rational area and the square on the given rational line are commensurable, use VI.1/6.1 to convert the area ratio into a length ratio, apply X.11/10.11 to conclude commensurability of the breadth with the base, and then invoke the definition of rationality. The only difference is citation depth: the AI explicitly cites 10.12 (transitivity of commensurability) and D10.1.3 (definition of rational lines) to spell out the step where Heath simply observes that two rational areas are commensurable by definition. Since heath_only is empty and the ai_only items (10.12, D10.1.3) merely make explicit what Heath handles implicitly through definitional reasoning, this is a citation-depth difference, not a path difference.

### 10.21
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that the square on one of the rational lines is rational, show the two lines are incommensurable in length (from being commensurable in square only), use 6.1 to set up a proportion between the square and the rectangle, apply 10.11 to conclude the square and rectangle are incommensurable, and then conclude the rectangle is irrational since it is incommensurable with a rational area. The AI's extra citations (D10.1.2, D10.1.3) are definitions that Heath uses implicitly, representing over-citation of definitions. The AI's use of 6.13 and 6.17 provides an explicit construction of the mean proportional to show the side of the square equal to the rectangle is irrational, whereas Heath simply states this conclusion directly from D10.1.4 without constructing the side. Since heath_only is empty and the key intermediate conclusions are the same in both proofs, with the AI merely providing additional depth on the final step and citing definitions explicitly, this is a granularity difference.

### 10.22
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) sq(A) equals a rectangle contained by rational lines commensurable in square only, (2) the breadth is rational (commensurable in square with the given rational line), and (3) the breadth is incommensurable in length with the given rational line. The differences are purely in citation depth. The AI cites 6.16 where Heath uses 6.14 directly, but 6.14 appears inside Heath's proof of 6.16, satisfying the proof-tree containment test: the AI cites 6.16 as a unit while Heath applies 6.14 at a lower level. The AI explicitly cites 6.1 for the ratio relationship that Heath invokes through an unnamed Lemma. The AI uses 10.5, 10.6, and 10.12 to spell out the commensurability chain for proving rationality, whereas Heath compresses these steps. The AI splits the definition reference into D10.1.2 and D10.1.3 where Heath uses D10.1.4. All differences are citation-depth variations on the same logical backbone.

### 10.23
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: apply squares on A and B to a rational line CD to get breadths DE and DF, show DE is rational and incommensurable with CD via 10.22, show the squares are commensurable so DE and DF are commensurable via 6.1 and 10.11, deduce DF is rational and incommensurable with CD via 10.13, conclude CD and DF are rational and commensurable in square only so B is medial via 10.21. The AI proof cites all six of Heath's references plus five additional sub-step citations (10.5, 10.6, 10.12, D10.1.2, D5.9) that provide explicit justification for transitions Heath treats as implicit, such as the step from commensurable lines to commensurable squares and the definition of commensurable in square. Since heath_only is empty and the ai_only items are all lower-level justifications for the same logical steps, this is a clear Case A granularity difference.

### 10.24
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same key intermediate conclusion: the rectangle contained by the two medial lines is commensurable with the square on one of them (a medial area), and therefore the rectangle is medial by 10.23. The citation differences are explained by depth: Heath cites 10.11 (if proportional magnitudes have commensurable first and second, then the third and fourth are commensurable), while the AI cites 10.5 and 10.6 directly, which are the sub-propositions used inside Heath's proof of 10.11 — satisfying the proof-tree containment test in reverse (AI goes deeper than Heath). The remaining ai_only items are definitions (D10.1.2, D10.1.4), an over-cited reference to the definition of medial (10.21), and a construction proposition (2.14) for introducing an auxiliary line. The AI's extra construction of an auxiliary line C whose square equals the rectangle is a presentational variation but does not change the logical backbone.

### 10.25
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: apply the medial squares to a rational line to get rational breadths incommensurable with it (10.22), show the breadths are commensurable in length via the commensurability of the original squares (6.1, 10.11), conclude their rectangle is rational (10.19), establish a mean proportional showing a certain square equals that rational rectangle (6.17), deduce the resulting breadth is rational, and then split into two cases — commensurable in length gives rational (10.19), commensurable in square only gives medial (10.21). The citation differences are purely at the granularity level: the AI explicitly cites definitions D10.1.2, D10.1.3, D10.1.4 that Heath leaves implicit, while Heath explicitly cites 5.11 (transitivity of ratios) for chaining ratio equalities that the AI handles implicitly. These are citation-depth differences with identical key intermediate conclusions.

### 10.26
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Both proofs share the same initial setup (contradiction assumption, application to rational line EF, establishing two rational lines incommensurable with EF and one rational line commensurable with EF via 10.22 and 10.20, then deriving incommensurability via 10.13), but they diverge fundamentally in how they reach contradiction. Heath uses 10.11 (proportion-based incommensurability transfer) to show sq(EG) is incommensurable with rect(EG,GH), then builds up via 10.6 and 10.13 to show sq(EG)+sq(GH) incommensurable with 2*rect(EG,GH), then uses 10.16 to conclude sq(EH) is irrational while EH is rational. The AI instead uses 10.21 to establish that rect(EH,HG) is irrational (since EH and HG are rational and commensurable in square only), then independently shows via II.4 expansion and commensurability arithmetic (10.12, 10.15, 10.9, 10.6) that rect(EH,HG) must also be rational, yielding contradiction. The key intermediate conclusions after step 3 are entirely different (Heath: sq(EH) irrational; AI: rect(EH,HG) both irrational and rational), constituting a genuine path difference decided at Q2 Case B. The AI's path is logically complete under the hardened Q1(b) standard.

### 10.27
**Category**: Path difference
**Jaccard**: 0.158
**Analysis**: The classification is decided at Q2/Q3. The two proofs construct D in fundamentally different ways: Heath uses VI.12 to find a fourth proportional D with A:B = C:D, then applies X.11 to transfer commensurability and X.23 to show D is medial, and derives rect(C,D) = sq(B) via V.16 alternando. The AI instead uses I.44 to construct D such that rect(C,D) = sq(A) directly (making rationality of rect(C,D) immediate), then proves C,D commensurable in square only through a long chain involving 6.1, 10.7, 10.8, 6.22, 10.5, and 10.6, and proves D is medial through an auxiliary construction involving 10.20 and a line F. These are genuinely different backbones with different key intermediate conclusions (different construction of D, different rationality argument, different mediality argument for D, different commensurability argument). The AI proof is logically complete with every step properly cited, so Q3 confirms a valid different path, yielding D.

### 10.28
**Category**: Path difference
**Jaccard**: 0.158
**Analysis**: Q2 determined the classification. Heath's proof starts with three abstract rational straight lines A, B, C commensurable in square only, constructs D as mean proportional of A,B and E via the ratio B:C = D:E, then uses 10.11 to transfer commensurability, 10.23 to establish E as medial, and 5.16 (alternando) to show rect(D,E) = rect(A,C) which is medial. The AI proof takes a fundamentally different path: it starts from a single rational line A, explicitly constructs B as the diagonal of A's square (so sq(B):sq(A) = 2:1 via 1.47) and C = 3B, then builds D and E as mean proportionals of A,B and A,C respectively, proving both medial directly via 10.21. The AI uses numerical ratios with 10.6/10.9 instead of 10.11 to establish commensurability in square only, and introduces an auxiliary rational line F (mean proportional of B,C) to show rect(D,E) = rect(A,F) via 6.22 and 6.16, then applies 10.21 to the pair A,F. The construction strategy, the intermediate conclusions, and the proof mechanism for the medial rectangle all differ substantially, constituting a genuine path difference. Both proofs are logically complete.

### 10.29
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs establish the same key intermediate conclusions: (1) two rational straight lines commensurable in square only, and (2) the square on the greater exceeds the square on the less by the square on a line commensurable in length with the greater. The difference lies in the construction mechanism and citation depth. Heath uses a semicircle construction requiring 3.31 (angle in semicircle is right) and 5.19 (convertendo) for the ratio manipulation, while the AI uses specific numerical values (4, 1, difference 3) with direct arithmetic and cites 5.17 (separando) instead of 5.19. Since 5.17 appears inside Heath's own proof of 5.19, this is a citation-depth difference rather than a backbone difference. Heath's use of 3.31 is tied to his semicircle construction approach, which the AI replaces with direct numerical ratio construction, but the resulting geometric facts are identical. The ai_only items (1.22, 10.12, CN3, D10.1.3, P1, P3) are construction aids, definitions, postulates, and common notions consistent with over-citation at a finer granularity level.

### 10.30
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 reveals different backbones: Heath constructs a semicircle on AB, uses III.31 (angle in semicircle is right) and I.47 to establish that BF^2 = AB^2 - AF^2, then applies convertendo (V.19) to obtain CD:DE = AB^2:BF^2 and concludes via X.9 that AB and BF are incommensurable in length. The AI instead works purely arithmetically with three numbers d, e, f where d = e + f, uses separando (V.17) to derive G^2:B^2 = f:e from A^2:B^2 = d:e, then chains via ex aequali (V.22) to get A^2:G^2 = d:f, and concludes via X.9. The heath_only citations (3.31, 5.19) reflect Heath's geometric semicircle method, while the ai_only citations (5.17, 5.22, D10.1.2, D10.1.3) reflect the AI's arithmetic route. These are not containable under the proof-tree test since 3.31 and 5.19 are not sub-results of any proposition the AI cites; they belong to a genuinely different construction approach. Q3 confirms the AI's path is logically valid: separando is correctly applied to the componendo form, ex aequali correctly chains the ratios, and 10.9 validly yields incommensurability. Classification is D.

### 10.31
**Category**: Granularity difference
**Jaccard**: 0.385
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) constructing A, B via 10.29, (2) establishing that C is medial from sq(C) = rect(A,B) via 10.21, (3) establishing rect(C,D) = sq(B) is rational, (4) deriving A:B = C:D, (5) concluding C and D are commensurable in square only via 10.11, (6) D is medial via 10.23, and (7) transferring the excess property via 10.14. The AI reaches these same conclusions through an explicitly different mechanism — using mean proportionals (6.13, 6.17) and proportional similar figures (6.22) with ratio manipulation (5.16), whereas Heath establishes area equalities and proportions directly. The AI also cites definitions D10.1.2, D10.1.3, D10.1.4 explicitly. Heath's sole unique citation 10.30 appears only in a supplementary 'similarly' remark about the incommensurable variant, not in the main proof body. Since the key conclusions align and the differences are in citation depth for establishing those conclusions, this is a granularity difference.

### 10.32
**Category**: Path difference
**Jaccard**: 0.192
**Analysis**: Q2 reveals genuinely different backbones. Heath constructs D and E from three auxiliary rational lines A, B, C using rectangle equalities (sq(D)=rect(A,B), rect(D,E)=rect(B,C)), then derives the ratio D:E=A:C to transfer commensurability properties. The AI instead starts with two rational lines FG and GH, introduces a third rational line A incommensurable with both, constructs B as the mean proportional of A and FG via 6.13, and determines C via the proportion B:C=FG:GH using 6.12. The AI shows C is medial through an elaborate argument involving area application to a rational line (10.22), whereas Heath uses 10.23 (addition: a line commensurable with a medial is medial). The AI shows rect(B,C) is medial by establishing rect(B,C)=rect(A,GH) using 6.16, whereas Heath directly uses rect(D,E)=rect(B,C). These are different intermediate mechanisms yielding the same conclusion. Under Q3, the AI's path is logically complete with every step justified by citations, so it is classified as D.

### 10.33
**Category**: Granularity difference
**Jaccard**: 0.227
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs use the same geometric construction: starting from two rational lines commensurable in square only (via 10.30), applying a rectangle deficient by a square (6.28) to get incommensurable segments (10.18), constructing a semicircle and perpendicular, then proving three properties of the resulting pair of lines (incommensurable in square, sum of squares rational, rectangle medial). The key intermediate conclusions are identical in both proofs. The citation differences arise because the AI explicitly cites the similar-triangle machinery (3.31, 6.8, 6.4, 6.17, 6.16) and commensurability transitivity results (10.7, 10.8, 10.12, 10.13) that Heath leaves implicit, plus construction postulates (P1, P3, 1.11) and definitions (D10.1.2-4). The sole heath_only citation 10.23 reflects a minor sub-route difference: Heath transfers mediality from rect(AB,BC) to rect(AB,EF) via 10.23 (commensurable with medial is medial), while the AI directly proves rect(DE,GH) is medial by showing DE and GH are rational commensurable in square only and applying 10.21, then equating rect(DG,GE) = rect(DE,GH). This is a difference in citation depth for the same backbone conclusion, not a different logical path.

### 10.34
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 reveals a different backbone between the two proofs. While both share the geometric framework (semicircle construction, 3.31 for the right angle, 1.47 for the Pythagorean theorem, 6.28 for application of areas, and the conclusion that the sum of squares is medial and the rectangle is rational), they diverge in two fundamental ways. First, the initial setup differs: Heath invokes 10.31 to obtain two medial lines with the required properties directly, while the AI constructs them from scratch using 10.10 (to find incommensurable lines) and 10.21 (to establish the medial line). Second, and more critically, the method for establishing incommensurability in square is entirely different: Heath uses 10.18 to conclude AF is incommensurable with FB from the deficient-rectangle application, then transfers this via 10.11 (proportional incommensurability) to the squares on AD, DB; the AI instead uses 6.8 to express AD² and DB² in terms of AC and CB, then proves AC/CB is irrational through explicit algebraic computation involving 10.9 (square number ratios and commensurability), 10.7 (incommensurability and number ratios), and 2.5 (algebraic identity). The heath_only propositions (10.11, 10.18, 10.31) are not contained within the proofs of any AI-cited proposition; they represent a genuinely independent route. The AI's path is logically complete under the Q1(b) hardened standard, so Q3 yields D.

### 10.35
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same logical backbone: (1) obtain two medial lines commensurable in square only, containing a medial rectangle, with the square on the greater exceeding the square on the less by the square on a line incommensurable with the greater; (2) apply the semicircle construction; (3) verify incommensurability in square of the resulting lines; (4) verify the sum of squares is medial; (5) verify the rectangle is medial; (6) verify incommensurability between the sum of squares and the rectangle. The sole structural difference is that Heath cites 10.32 (ad fin.) as a unit to establish the initial medial lines, while the AI re-derives this construction from more primitive results (10.30, 6.13, 6.12, 6.17, 6.22, 10.21, 10.10, 10.12, 10.14, 10.15, etc.). Several of these ai_only citations (10.21, 10.11, 10.14) appear inside Heath's own proof of 10.32, confirming that the AI is expanding 10.32's internals rather than taking a genuinely different path. The remaining ai_only items (10.6, 10.7, 10.8, 10.9, 6.8, D10.1.2, D10.1.3, D10.1.4) represent additional granularity in the verification steps that Heath handles more tersely. The Jaccard similarity of 0.200 reflects this deep citation-depth difference while the logical backbone remains identical.

### 10.36
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Q2 determined a different backbone: Heath proves the irrationality of AC directly by establishing rect(AB,BC) incommensurable with sq(BC) via proportions (10.11), then chaining through 10.13 and 10.16 (componendo for incommensurable magnitudes) to show sq(AC) is incommensurable with the rational sum sq(AB)+sq(BC). The AI instead cites 10.21 directly for the irrationality of rect(AB,BC), then uses a proof by contradiction assuming sq(AC) is rational, deriving via 10.12 (commensurability transitivity) and 10.15 (second part) that 2*rect(AB,BC) would be rational, contradicting its established irrationality. The containment test shows 10.11 is inside 10.21 (citation-depth difference), but 10.16 is not inside 10.21 and represents an entirely different proof strategy (direct vs. contradiction), making this Case B. Q3 confirms the AI's contradiction argument is logically complete with all steps properly justified, so the classification is D.

### 10.37
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: decomposing the square on AC via II.4 into the sum of squares on AB, BC plus twice the rectangle AB, BC, showing these two components are incommensurable, then applying X.16 to conclude the square on AC is irrational. Heath abbreviates the incommensurability argument by referencing the pattern from X.36 ('cf. X. 36, ll. 9-20'), while the AI re-derives the same argument explicitly using 10.15, 10.13, and 10.6 — which are exactly the propositions used inside Heath's proof of 10.36. The proof-tree containment test confirms that the ai_only items (10.13, 10.15, 10.6) appear inside Heath's proof of 10.36, and the additional AI citations D10.1.2 and D10.1.3 are definitions made explicit by the AI. This is a citation-depth difference with the same key intermediate conclusions, not a path divergence.

### 10.38
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decides: both proofs establish the same key intermediate conclusions through the same logical backbone. Both (1) show that the sum of the squares on AB, BC and twice the rectangle AB, BC are each medial areas, (2) apply them to a rational line DE to obtain rational lines incommensurable with DE, (3) prove these two lines are incommensurable in length with each other, (4) conclude their sum is irrational via X.36, and (5) conclude AC is irrational. The citation differences are granularity matters: the AI cites definitions D10.1.2 and D10.1.3 explicitly where Heath does not; the AI cites 10.23 (commensurable with medial is medial) explicitly where Heath states the mediality more directly; the AI uses a contradiction argument via 10.12 (transitivity of commensurability) where Heath applies 10.13 (transitivity of incommensurability) directly, but both reach the same sub-conclusion that the two applied lines are incommensurable in length. Heath cites 1.44 for the area application construction and 10.6 for establishing commensurability of twice the rectangle with the rectangle, which the AI treats as implicit. These are all citation-depth differences, not backbone divergences.

### 10.39
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that twice the rectangle AB,BC is medial/irrational, that this quantity is incommensurable with the rational sum of squares, and then apply 10.16 to conclude that sq(AC) is incommensurable with the sum of squares and hence irrational. The citation differences reflect depth rather than path: Heath cites 10.23 to directly assert that twice a medial is medial, while the AI reaches the same conclusion more explicitly via 10.6 (commensurability of 2*rect with rect) and 10.13 (transitivity of incommensurability). Heath cites 10.33 for the existence construction, which the AI omits as a standard setup assumption. The AI additionally cites 2.4 for the algebraic identity and 10.21 for the definition of medial, which Heath leaves implicit. All key intermediate conclusions are the same in both proofs.

### 10.40
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determines the classification. Heath proves 10.40 directly: the sum of squares (medial) is incommensurable with twice the rectangle (rational) by 10.16, so the square on AC is incommensurable with twice the rectangle, hence irrational since twice the rectangle is rational. The AI instead uses a proof by exhaustive elimination: it shows AC^2 cannot be rational (since the difference AC^2 - 2*AB*BC = AB^2+BC^2 would then be rational, contradicting the medial hypothesis) and cannot be medial (since two medial areas cannot differ by a rational area, by 10.26), concluding AC^2 must be irrational. These are fundamentally different logical backbones -- direct incommensurability via 10.16 versus contradiction-based elimination using 10.15, 10.21, and 10.26. The AI's path is logically sound and complete, satisfying Q3, so the classification is D.

### 10.41
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification as G. Both proofs share the same logical backbone: express sq(AC) via II.4, apply both medial areas to a rational line DE, show each resulting breadth is rational and incommensurable in length with DE via 10.22, show the breadths are mutually incommensurable via 6.1 and 10.11, conclude the sum is irrational via 10.36 (binomial), and hence AC is irrational. The AI proof cites additional granular propositions (10.6 for commensurability of 2*rect with rect, 10.13 for transitivity of incommensurability, 10.12 and D10.1.3 for commensurability in square of the breadths, and 10.20 as contrapositive to establish irrationality of sq(AC)), while Heath achieves the same steps more tersely. Heath's sole unique citation 10.35 is the existence proposition for lines satisfying the conditions, a standard setup reference the AI omits. All differences are citation-depth variations at the same logical positions, making this a granularity difference.

### 10.42
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they set up the binomial line AB divided at C, assume a second division at D, decompose sq(AB) two ways via II.4, identify that the sum of squares is rational while the double rectangle is medial, and reach a contradiction via X.26 (medial cannot exceed medial by rational). The AI proof adds explicit citations for steps Heath leaves implicit (10.15 for the rationality of the sum of squares, 10.26 for the medial-rational incompatibility, definitions D10.1.3/D10.1.4 for setup, common notions CN1-CN3 for algebraic rearrangement, and 2.7 for additional algebraic manipulation in steps 10-11). The AI also extends the proof beyond Heath's stopping point by algebraically deriving AC=AD and CB=DB rather than simply stopping at the contradiction. Since heath_only is empty and all ai_only items are either over-citations (definitions, common notions) or explicit justifications of implicitly used results, and the key intermediate conclusions are the same, this is a granularity difference.

### 10.43
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Both proofs follow the same logical backbone: assume two different division points C and D for the first bimedial line AB, establish that twice the rectangles rect(AC,CB) and rect(AD,DB) are rational, derive via algebraic identity that the difference of sums of squares equals the difference of double rectangles, and conclude that medial areas (the sums of squares) would differ by a rational area, contradicting 10.26. The AI proof explicitly cites subsidiary results (10.13, 10.15, 10.21 for establishing mediality of sums of squares; 2.4 for the algebraic identity; 10.37 for the definition of first bimedial; CN2, CN3, D10.1.4 for arithmetic and definitions) that Heath leaves implicit, and extends the argument with additional steps (12-17) showing C=D explicitly rather than stopping at the contradiction. Heath's captured reference set is empty (though the text cites x.26), making the Jaccard 0.0, but this reflects a data capture gap rather than a genuine path difference. The key intermediate conclusions are identical in both proofs, with the AI providing finer-grained justification at each step, which is a citation-depth difference characteristic of G.

### 10.44
**Category**: Granularity difference
**Jaccard**: 0.5
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: apply areas from both proposed divisions of the second bimedial to a rational straight line, show the resulting breadths are rational and commensurable in square only, conclude their sum is a binomial via 10.36, and invoke the uniqueness of binomial division (10.42) to force the two division points to coincide. The AI proof explicitly cites 10.42 while Heath uses it implicitly, and the AI additionally cites definitions (D10.1.2, D10.1.3), common notions (CN1, CN3), and intermediate lemmas (10.21, 10.23, 10.12, 2.5) that Heath leaves tacit. Since heath_only is empty and all ai_only items are over-citations of steps already implicit in the shared argument, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.45
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: assume two division points C and D of a major line, observe that the difference of the sums of squares (both rational) equals the difference of twice the rectangles (both medial), and derive a contradiction via 10.26 since a medial area cannot exceed another medial area by a rational amount. The AI's eight additional citations (1.10, 10.12, 10.15, 2.4, 2.9, CN1, CN3, D10.1.4) are either over-citations making Heath's implicit steps explicit (2.4 for the algebraic identity, CN1/CN3 for equalities, D10.1.4/10.12/10.15 for the rationality of the difference) or support a supplementary midpoint argument (1.10, 2.9 in Steps 7-12) that goes beyond the contradiction but does not change the core backbone. Heath's citation set is a subset of the AI's, and the key intermediate conclusion — the contradiction via 10.26 — is identical in both proofs.

### 10.46
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume AB is divided at two points C and D satisfying the conditions of 10.40, show that the difference of twice the rectangles (rational) equals the difference of the sums of squares (medial), then invoke 10.26 to reach a contradiction since a medial area cannot exceed a medial area by a rational area. The AI proof then elaborates further by explicitly showing the division points must coincide using 2.4, 2.7, and algebraic manipulation, while Heath simply concludes from the contradiction. The ai_only citations (10.45, 2.4, 2.7, CN1, CN2, CN3, D10.1.4) represent over-citation of foundational steps and an extended uniqueness argument that goes beyond Heath's concise contradiction-based conclusion. Since heath_only is empty and all key intermediate conclusions match, this is a granularity difference in citation depth and proof elaboration.

### 10.47
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume AB is divided at two points satisfying 10.41 conditions, apply the four medial areas to a rational straight line to produce breadths, show these breadths are rational and commensurable in square only (via 10.22, 6.1, 10.11), conclude the total breadth forms a binomial (10.36), and invoke 10.42 (binomial divided at one point only) to reach contradiction. The AI proof cites all six of Heath's references and adds ten more (common notions CN1/CN3/CN5, intermediate commensurability lemmas 10.6/10.12/10.13, setup reference 10.41, construction 1.10, and cross-case elimination tools 2.5/2.9). These extra citations support the same backbone at finer granularity: the AI explicitly justifies why each area is medial, handles the cross-case (b1=c2, c1=b2) that Heath leaves implicit, and cites common notions for algebraic steps. Since heath_only is empty and all ai_only items are either axioms, constructions, or intermediate lemmas supporting the same key conclusions, this is Case A of Q2 — same backbone, different citation depth — yielding G.

### 10.48
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification as Granularity difference (G). Both proofs construct a first binomial straight line by finding two rational lines commensurable in square only whose squares satisfy the required excess condition, then applying 10.36 to form the binomial and verifying the first-binomial conditions. Heath performs the construction inline using 10.6 (to establish commensurability of squares from number ratios), 10.9 (to establish length incommensurability from non-square ratios and length commensurability for the excess), and 5.19 (convertendo for the ratio manipulation), while the AI delegates this entire construction to 10.29, which packages exactly these steps. The proof-tree containment test confirms that all substantive heath_only citations (10.6, 10.9, 5.19) appear inside Heath's own proof of 10.29, establishing that the AI cites 10.29 as a unit while Heath re-derives its internals inline. The remaining heath_only item 10.28 refers to the Lemma after X.28 about number selection, which is similarly subsumed. The shared citation of 10.36 and the identical logical endpoint confirm the same backbone at different citation depth.

### 10.49
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same logical backbone: they set up numbers with appropriate ratio properties, use 10.6 to find a line creating a specific square ratio, show two rational lines commensurable in square only to form a binomial (10.36), then demonstrate the square on the greater exceeds the square on the lesser by a square on a line commensurable in length with the greater (via 10.9), and finally verify the lesser term is commensurable with the rational line set out. The ai_only items D10.1.3 and D10.2.2 are explicit definition citations that Heath uses implicitly, which is standard over-citation. The 5.17 (AI) vs 5.19 (Heath) difference reflects the same proportional conversion step cited under different proposition numbers: the AI labels it separando while Heath labels it convertendo, but the mathematical operation performed is identical. Since both proofs establish the same key intermediate conclusions with differences only in citation depth and labeling, this is Case A of Q2.

### 10.50
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: The forward-dependency gate found no violations. Q1 confirmed the AI proof is logically complete with all steps properly supported by citations. Q2 determined that both proofs share the same backbone of key intermediate conclusions in the same logical order: constructing FG and GH as rational lines via 10.6, establishing incommensurability in length via 10.9, concluding binomial by 10.36, using ex aequali (5.22) and convertendo (5.19) to verify the third binomial conditions. The ai_only items (CN3, D10.1.3, D10.1.4, D10.2.3) are all definitions and a common notion that Heath uses implicitly at the same logical positions but does not cite explicitly. Since heath_only is empty and the ai_only items are purely definitional over-citations at matching logical positions, this is Case A of Q2: same backbone, different citation depth, yielding classification G.

### 10.51
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this as Granularity difference (Case A). Both proofs establish the same key intermediate conclusions: two rational lines commensurable in square only whose sum is binomial, with the square on the greater exceeding the square on the lesser by a square incommensurable in length with the greater, and the greater term commensurable in length with the rational line set out. Heath builds these facts from primitives (10.6 to set up proportional squares, 10.9 to derive incommensurability in length, 5.19 for convertendo), while the AI invokes 10.30 as a unit to obtain lines with exactly these properties. The proof-tree containment test confirms that all three heath_only items (10.6, 10.9, 5.19) appear inside Heath's proof of 10.30, so the AI is citing at a higher level of abstraction rather than following a genuinely different path. The AI additionally cites 10.36 to establish the binomial property explicitly (Heath states the same fact from the definition without citing 10.36) and references definitions D10.1.3 and D10.2.4. The Jaccard similarity is 0.0 because the citation sets are completely disjoint, but textual comparison shows the same backbone at different citation depths.

### 10.52
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct two rational straight lines commensurable in square only, form a binomial via 10.36, then show the square on the greater term exceeds the square on the lesser by a square on a line incommensurable with the greater, and finally verify that the lesser term is commensurable in length with the assigned rational line to satisfy the definition of a fifth binomial. The only substantive citation difference is that Heath uses 5.19 (convertendo) while the AI uses 5.17 (separando) to manipulate the ratio of squares, but both arrive at the same intermediate conclusion about the ratio relationship. The AI additionally cites 10.18 as an alternative justification for the incommensurability conclusion, and explicitly cites definitions D10.1.2, D10.1.3, and D10.2.5 that Heath leaves implicit. All ai_only items are either definitions (over-citation) or alternative routes to the same intermediate fact, and the heath_only item 5.19 is replaced by 5.17 serving the same logical role. This is Case A of Q2: same backbone, different citation depth.

### 10.53
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Both proofs establish the same key intermediate conclusions for constructing a sixth binomial straight line: two rational straight lines each incommensurable in length with the set-out rational line, commensurable in square only with each other, whose sum is binomial (10.36), with the square on the greater exceeding the square on the lesser by the square on a line incommensurable with the greater, and neither term commensurable in length with the set-out rational. The backbone is identical. The citation differences arise from different arithmetic setups: Heath uses three numbers AC, CB, D with ratios D:AB and BA:AC, requiring 5.22 (ex aequali) and 5.19 (convertendo) for ratio manipulation, while the AI constructs lines with squares in ratios p:1 and q:1 to the square on e, avoiding the need for those ratio composition steps but instead citing 10.5 and 10.12 explicitly for commensurability reasoning. The AI also over-cites definitions (D10.1.3, D10.2.6), a common notion (CN3), and the Pythagorean theorem (1.47) that Heath leaves implicit. Q2 Case A applies: same backbone, different citation depth arising from a different but equivalent arithmetic construction technique.

### 10.54
**Category**: Path difference
**Jaccard**: 0.368
**Analysis**: Q2 reveals different backbones, leading to Q3 which confirms a valid different path (D). Heath establishes the area equality sq(MO) = rect(AB,AD) through a geometric mean proportional argument using 6.17 and the Lemma about mean proportionals between squares SN and NQ (constructed via 2.14), and establishes MN incommensurable with NO through a chain AG incommensurable with EF via 10.13 propagated through areas using 6.1 and 10.11, with commensurability of AG, GE with AB established transitively via 10.15 and 10.12. The AI takes a fundamentally different algebraic approach: it directly defines MN, NO by their squares equaling rect(AB,AG) and rect(AB,GE), establishes the sum of squares is rational from rect(AB,AE) being rational (10.19), independently shows rect(AB,ED) is medial using 10.21 (a proposition Heath does not cite), and uses the mediality of 2*rect(MN,NO) to prove MN and NO are incommensurable in length. The AI uses algebraic identities 2.1 and 2.4 to assemble the area equality rather than Heath's geometric mean proportional construction. While Step 16's treatment of 2*rect(MN,NO) = rect(AB,ED) as a requirement rather than a proven identity is terse, the supporting ingredients are present in the proof (rect(AG,GE) = sq(EF) from construction, EF = ED/2), and under the lenience rule this is classified as terse-but-supported rather than unsupported. The different use of 10.21 vs the 6.17/Lemma/2.14 approach, and the algebraic vs geometric handling of the area equality, constitute a genuine path divergence.
**Audit Record**: CANDIDATE E — 10.54
  violated_claim : 2*rect(MN,NO) = rect(AB,ED), needed for sq(MO) = area AC
  failure_mode   : unsupported_assertion
  missing_is     : expansion — the AI has the supporting ingredients (rect(AG,GE) = sq(EF) from construction, EF = ED/2) in Steps 9-10 but does not explicitly connect them to this equation; under the lenience rule this is terse-but-supported, not a genuine logical gap
  evidence       : Step 16: "we require twice the rectangle MN by NO to equal the rectangle AB by ED" — stated as requirement, then used as established fact in Steps 17 and 19
  why_not_terse  : CANNOT COMPLETE — the supporting material (rect(AG,GE) = sq(EF), EF = ED/2) is present in the proof text and mathematically entails the claim; this is compressed presentation, not a missing support relation. Reclassified as NOT-E.

### 10.55
**Category**: Granularity difference
**Jaccard**: 0.348
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: dividing the second binomial into its terms, applying a rectangle to get commensurable segments via 10.17, constructing two medial straight lines that are commensurable in square only and contain a rational rectangle, then concluding the sum is a first bimedial by 10.37. The heath_only citations (10.12, 10.15) represent intermediate commensurability lemmas that the AI handles through equivalent but differently-cited reasoning -- the AI derives the same facts using 10.13 directly and algebraic computation (showing 2wx = AB*EC via area identities) rather than the commensurability transitivity chain. The ai_only citations are predominantly construction and arithmetic propositions (1.10, 2.1, 2.4, 2.5, 2.14, 6.13, 6.16, 6.17, 6.28) representing explicit over-citation of steps Heath treats implicitly, plus 10.9 used in the reductio for 'commensurable in square only' where Heath uses a different sub-argument via 10.13. All key intermediate conclusions (medial lines, commensurable in square only, rational rectangle, first bimedial conclusion) appear in both proofs at the same logical positions.

### 10.56
**Category**: Granularity difference
**Jaccard**: 0.211
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: setting up the third binomial construction, showing MO is the side of area AC via the method of 10.54, establishing that MN and NO are medial straight lines commensurable in square only, proving that the rectangle MN by NO is medial (via 10.13 showing EF incommensurable with EK, then 10.21), and concluding MO is a second bimedial by 10.38. Heath abbreviates the entire construction and the proof that MO is bimedial with 'in manner similar to the foregoing,' citing only D10.2.3, 10.13, 10.21, and 10.38. The AI spells out all the internal steps of the 10.54 construction in full detail, adding 15 citations (1.10, 10.11, 10.15, 10.17, 10.22, 10.24, 10.5, 10.9, 2.1, 2.4, 2.5, 6.28, D10.1.2, D10.1.3, D10.1.4) that are all sub-steps of the construction Heath refers to en bloc. Since heath_only is empty and all ai_only items are construction machinery, algebraic identities, and definitions supporting the same backbone at finer granularity, this is a same-backbone, different-depth scenario — Case A of Q2.

### 10.57
**Category**: Granularity difference
**Jaccard**: 0.412
**Analysis**: Q2 decided the classification. Both proofs establish the same backbone: (1) the fourth binomial terms CE, ED are rational and commensurable in square only with CE commensurable to AB, (2) CE is divided into parts CG, GE that are incommensurable in length via 10.18, (3) the sum of squares on the constructed line segments is rational via 10.19, (4) the rectangle contained by them is medial via 10.21 and 10.13, (5) the segments are incommensurable in square, and (6) the conclusion follows by 10.39. The sole heath_only citation 10.11 is explained by the proof-tree containment test: the AI cites 10.7 and 10.8 directly, which are the internal steps of Heath's proof of 10.11, so the AI re-derives that result inline rather than citing it as a unit. The remaining ai_only items (1.10, 10.20, 10.22, 10.23, 2.4, D10.1.3, D10.1.4) are constructive steps, definitions, or explicit citations of facts Heath uses implicitly. The AI proof is verbose with some false starts in Steps 4-5 but ultimately establishes all key conclusions at greater citation depth than Heath.

### 10.58
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that two constructed line segments are incommensurable in square, that the sum of their squares is medial, and that their rectangle is rational, then conclude by X.40 that the side is of the type 'side of a rational plus a medial area.' The ai_only citations (1.10, 2.1, 2.5, 6.28, D10.1.3, D10.1.4) are all construction steps and definitions that the AI spells out explicitly while Heath abbreviates them as 'let the same construction be made as before shown.' The single heath_only citation (10.12, transitivity of commensurability) is used by Heath in establishing that EF is commensurable with EK; the AI reaches the equivalent conclusion about the rectangle being rational through a slightly different but equivalent application of commensurability, arriving at the same key intermediate conclusion. Since both proofs argue through the same key intermediate conclusions with differences only in citation depth, this is a granularity difference.

### 10.59
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs establish the same four key intermediate conclusions required to invoke 10.41: (1) the sum of the squares on the two component lines is medial, (2) the rectangle contained by them is medial, (3) the component lines are incommensurable in square, and (4) the sum of squares is incommensurable with the rectangle. The backbone is identical. The sole heath_only citation, 10.13, appears inside Heath's own proof of 10.22 (which the AI cites), satisfying the proof-tree containment test: the AI cites 10.22 as a unit while Heath re-derives its internals inline. The ai_only items consist of definitions (D10.1.3, D10.1.4, D10.2.6), basic algebraic identities (2.1, 2.4), proportion lemmas (6.17), and auxiliary results (10.18, 10.22) that make explicit what Heath handles via the standard construction reference. These are citation-depth differences, not path differences.

### 10.60
**Category**: Path difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs share the same backbone through the first five key conclusions: establishing AC, CB as rational lines commensurable in square only, showing the sum of squares is rational (yielding DM/DG rational and commensurable with DE), showing twice the rectangle is medial (yielding MG/GF rational and incommensurable with DE), establishing DM/DG is incommensurable with MG/GF so the breadth is binomial, and proving DM/DG > MG/GF. However, the critical middle section where each proof shows that sq(DM) > sq(MG) by a commensurable square diverges completely. Heath uses the Lemma after 10.53 (mean proportional), 6.17 (rectangle of extremes equals square on mean), 10.11 (commensurability transfer through proportions), and 10.17 (the parallelogram deficiency criterion) to establish this. The AI instead uses a direct algebraic approach: decomposing via Book 2 identities (2.4, 2.5, 2.7), showing sq(AC)+sq(CB) is commensurable with sq(AC)-sq(CB) through number ratios (10.5, 10.6), and directly computing sq(DG)-sq(GF) as the square on a line commensurable with DG. This constitutes a genuinely different logical path that is mathematically valid, yielding classification D.

### 10.61
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that the sum of squares on AC and CB is medial, derive that the greater term is rational and incommensurable with the rational line while the lesser term is rational and commensurable with it, conclude the breadth is binomial via 10.36, and then show it is specifically the second binomial by verifying that the square on the greater term exceeds the square on the lesser by a commensurable square. The heath_only citations (10.17 and 10.21) represent higher-level results that Heath invokes directly, while the AI re-derives the same conclusions at a finer grain: instead of citing 10.21 for the mediality of the squares, the AI uses D10.1.2 and commensurability reasoning; instead of citing 10.17 for the commensurable-square-excess condition, the AI performs explicit algebraic computation using 2.4, 2.5, 6.1, 10.11, and 10.15 — ingredients that appear inside 10.17's own proof (notably 2.5). The ai_only items (2.4, 2.5, D10.1.2) are basic algebraic identities and a definition, consistent with over-citation at a lower level. This is a citation-depth difference with the same backbone, fitting Case A of Q2.

### 10.62
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: AC and CB are medial commensurable in square only with medial rectangle; sum of squares on AC, CB is medial; DM and MG are each rational and incommensurable with DE; DM is incommensurable with MG so DG is binomial; the square on DM exceeds the square on MG by the square on a line commensurable with DM; and DG is a third binomial. The backbone is identical. The AI-only citations (10.5, 10.9, 2.4, 2.7, 5.12, 8.11, D10.1.2, D10.1.4) are sub-lemma elaborations of steps Heath abbreviates with phrases like 'in manner similar to the foregoing,' plus definitions and algebraic identities cited explicitly. The heath-only citation 10.13 is used by Heath directly to transfer incommensurability, while the AI achieves the same conclusion through a reductio argument using 10.11, 10.12, 10.15, and 6.1 — an equivalent micro-path that does not alter the overall logical backbone. This is a citation-depth difference, not a path difference.

### 10.63
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs establish the same key intermediate conclusions: (1) the first term of the binomial is rational and commensurable with DE, (2) the second term is rational and incommensurable with DE, (3) the two terms are incommensurable with each other, (4) the sum is binomial, (5) the greater term exceeds the lesser appropriately, and (6) the result is a fourth binomial. The heath_only citation 10.13 (transitivity of incommensurability) is replaced in the AI proof by an area-based argument using definitions D10.1.3 and D10.1.4 with 6.1 and 10.11, reaching the same conclusion that the two terms are incommensurable in length. The ai_only citations 2.4, 2.7, and CN3 reflect the AI's explicit algebraic expansion of the square on AB, while Heath compresses this with 'let the same construction be made as before shown.' The ai_only citations 10.15 and 10.16 appear in the AI's more detailed algebraic argument for the square-excess incommensurability, where Heath applies 10.18 more directly via geometric construction. All differences are in citation depth and explicitness, not in the logical backbone.

### 10.64
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) the sum of squares on AC, CB is medial, so DK is rational and incommensurable in length with DE (via 10.22); (2) twice rect(AC,CB) is rational, so KG is rational and commensurable with DE (via 10.20); (3) DK incommensurable with KG, hence DG is binomial (via 10.13, 10.36); (4) sq(DK) exceeds sq(KG) by a square on a line incommensurable with DK; (5) KG commensurable with DE, so DG is a fifth binomial. The sole heath_only citation is 10.18, which Heath uses directly for conclusion (4). The AI instead re-derives the content of 10.18 from first principles using 10.15, 10.16, 10.6, 10.13, and algebraic identities (2.4, 2.7), which are exactly the propositions used inside Heath's own proof of 10.18. This satisfies the proof-tree containment test: the heath_only items appear inside the proof of 10.18, whose content the AI inlines rather than citing as a unit. The remaining ai_only items are definitions (D10.1.3, D10.1.4, D10.2.4, D10.2.5), supporting algebraic propositions (2.4, 2.7, 6.1, 10.11), and 10.21, all representing over-citation of elementary steps. Same backbone, different citation depth.

### 10.65
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same key intermediate conclusions: (1) AC, CB have the properties from 10.41, (2) the applied rectangles produce rational breadths incommensurable with DE via 10.22, (3) the breadths are incommensurable with each other via 6.1 and 10.11, (4) the breadths are rational and commensurable in square only so the result is binomial by 10.36, (5) the square on the greater exceeds the square on the lesser by the square on a line incommensurable with the greater, and (6) neither term is commensurable with DE, yielding a sixth binomial. Heath's proof compresses the fifth conclusion with 'similarly again we can prove' and 'for the same reason,' while the AI spells out these steps in detail using 2.4, 2.7, 6.13, 6.17, 6.22, 10.12, 10.15, and 10.23. The heath_only set is empty, confirming that Heath's citations are a proper subset of the AI's. All ai_only items are sub-steps, algebraic identities, definitions, or common notions that elaborate the same logical backbone at finer granularity.

### 10.66
**Category**: Granularity difference
**Jaccard**: 0.579
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) divide the commensurable line proportionally to the binomial's terms, (2) show the new terms are rational and commensurable in square only, (3) conclude the line is binomial, and (4) show it is the same order via the six-case analysis using 10.14, commensurability checks, and the order definitions. The citation differences are explained by granularity: the AI cites 10.5 and 10.6 directly where Heath cites 10.11, and 10.11's proof internally uses 10.5 and 10.6 (proof-tree containment). The AI handles the case covered by Heath's 10.13 citation by re-deriving 10.13's argument inline via contradiction using 10.12, which is the sole citation in 10.13's own proof. Heath uses 5.19 (remainder proportionality) and 5.16 (alternation) to establish the proportion AE:EB = CF:FD, while the AI's construction via 6.12 sets up all parts in the same ratio directly and uses 5.11 to derive the same proportion, bypassing those lemmas but reaching the identical key conclusion. The AI's additional citation of 6.22 and D10.1.3 are over-citations that do not change the logical backbone. All key geometric facts are established at the same positions in both proofs.

### 10.67
**Category**: Granularity difference
**Jaccard**: 0.353
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish identical key intermediate conclusions: dividing AB at E into medials, constructing CF and FD on CD in the same ratio, proving CF and FD are each medial and commensurable in square only, concluding CD is bimedial, and then showing the rectangle commensurability preserves the order (first or second bimedial). The sole heath_only citation, 5.19 (remainder proportion), is functionally replaced by the AI's use of 6.12 (fourth proportional construction) to achieve the same proportional division, arriving at the identical conclusion that EB:FD = AB:CD. The AI's ten ai_only citations (10.5, 10.6, 10.9, 10.12, 6.1, 6.12, 6.16, 6.22, D10.1.2, D10.1.4) are lower-level foundational steps, construction propositions, and definitions that provide finer-grained justification for steps Heath performs in fewer citations. The logical backbone is the same throughout; the difference is purely in citation depth.

### 10.68
**Category**: Path difference
**Jaccard**: 0.083
**Analysis**: Q2 decided this classification as D (path difference). Heath's proof works directly with the components of the major line, dividing AB at E and CD at F, then using proportion theory (5.11, 5.16, 5.18) and 6.20 to transfer the rational-sum-of-squares and medial-rectangle properties from AE,EB to CF,FD, concluding via the definition of major (10.39). The AI takes a fundamentally different route through the classification theory of irrationals: it applies the square on AB to a rational line to obtain a fourth binomial breadth (10.63), shows the corresponding breadth for CD is commensurable and therefore also a fourth binomial (10.66), then recovers that CD is major because its square equals a rational line times a fourth binomial (10.57). The key intermediate conclusions are entirely different — Heath reasons about incommensurable-in-square components and their sum/rectangle properties, while the AI reasons about binomial classifications of breadths. The Jaccard similarity of 0.083 with only 10.11 shared confirms the near-total divergence. The AI's alternative path is logically complete with every step properly cited.

### 10.69
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: (1) the two component lines of CD are incommensurable in square, (2) the sum of squares on the components of AB is commensurable with the sum of squares on the components of CD, (3) the rectangle contained by the components of AB is commensurable with the rectangle contained by the components of CD, (4) the sum of squares on the components of CD is medial, and (5) the rectangle contained by the components of CD is rational. Heath abbreviates all the intermediate work with 'Let the same construction be made as before' and 'We can then prove similarly,' citing only 10.40. The AI spells out every sub-step explicitly, citing 10.11, 10.12, 10.13, 10.23, 5.12, 5.16, 6.1, 6.12, 6.20, and D10.1.4 for the proportional construction, commensurability transfers, and mediality/rationality preservation. The ai_only set consists entirely of sub-lemmas underlying Heath's abbreviated argument, and the heath_only set is empty, confirming this is a citation-depth difference with the same logical backbone.

### 10.70
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: CF and FD are incommensurable in square, the sum of squares on CF and FD is medial, the rectangle CF by FD is medial, and the sum of squares on CF and FD is incommensurable with the rectangle CF by FD, concluding that CD is the side of the sum of two medial areas by 10.41. Heath's proof compresses the entire argument into 'let the same construction be made as before' and 'we can then prove similarly,' citing only 10.41, while the AI proof explicitly works through every subsidiary step, citing 10.5, 6.12, 10.6, 10.11, 10.12, 10.15, 10.23, and 10.13 for the proportional construction, commensurability transfers, and incommensurability propagation. The ai_only set consists entirely of propositions that underlie the steps Heath summarizes with 'similarly,' and heath_only is empty, confirming that the logical backbone is identical and only the citation depth differs.

### 10.71
**Category**: Granularity difference
**Jaccard**: 0.647
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: they apply the rational and medial areas to a rational straight line to produce two breadths, show one breadth is rational and commensurable in length with the reference line (10.20) while the other is rational and incommensurable in length with it (10.22), establish that the two breadths are incommensurable in length with each other, conclude the whole is a binomial (10.36), then classify into four sub-cases yielding binomial (10.54), first bimedial (10.55), major (10.57), or side of rational plus medial area (10.58). The only structural difference is in establishing the incommensurability of the two breadths: Heath uses VI.1 (proportion of rectangles under same height) combined with 10.11 (proportional magnitudes preserve commensurability), while the AI uses 10.13 (if two magnitudes are commensurable and one is incommensurable with a third, so is the other) as a single-step alternative. This achieves the identical key intermediate conclusion through a different but equivalent micro-level justification. The AI also over-cites definitions D10.1.3, D10.2.3, and D10.2.6 that Heath leaves implicit. Since all key intermediate conclusions match and the differences are confined to citation depth, this is a granularity difference.

### 10.72
**Category**: Granularity difference
**Jaccard**: 0.889
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow an identical logical backbone: applying two incommensurable medial areas to a rational straight line, showing the breadths are rational and incommensurable in length with the rational line (10.22), proving the breadths are incommensurable with each other via 6.1 and 10.11, forming a binomial via 10.36, classifying it as third or sixth binomial (D10.2.3, D10.2.6), and concluding with the appropriate irrational type via 10.56 or 10.59. The only citation difference is that the AI adds D10.1.3 (a definition of rational lines) in Step 6 to explicitly justify why rational lines incommensurable in length are commensurable in square only. This is a definitional over-citation representing a finer granularity of justification, not a substantive path difference. Since the citation sets are not exactly equal, P is excluded.

### 10.73
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Q2 reveals genuinely different logical backbones. Heath proves the result directly: he uses 10.11 to transfer the incommensurability of AB and BC (in length) to the incommensurability of sq(AB) and rect(AB,BC), then uses 10.13 and 10.16 to conclude that sq(AB)+sq(BC) is incommensurable with sq(AC), hence AC is irrational. The AI takes a different path: it uses 10.21 to establish that rect(AB,BC) is medial (irrational), then shows 2*rect(AB,BC) is also irrational via 10.6 and 10.13, and finally argues by contradiction — assuming AC rational leads to 2*rect(AB,BC) being rational (via 10.12 and 10.15), contradicting its established irrationality. The contradiction strategy and the use of 10.21 (mediality) instead of 10.11 (proportional incommensurability transfer) and 10.16 (additive incommensurability) constitute a genuinely different logical route, not merely a difference in citation depth. Both paths are logically complete, so the classification is D.

### 10.74
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 reveals different backbones: Heath uses a direct argument via X.16 (if the whole is incommensurable with one part, the original magnitudes are incommensurable) to show that since squares on AB,BC are incommensurable with twice rect(AB,BC), twice rect(AB,BC) is incommensurable with sq(AC), and since twice rect(AB,BC) is rational, sq(AC) must be irrational. The AI instead takes a proof-by-contradiction approach, first establishing that the sum of squares on AB,BC is a medial area (using 10.13, 10.15), then showing sq(AC) cannot be rational (it would force the sum of squares to be rational via 10.12 and 10.15, contradicting its medial status) and cannot be medial (a medial area cannot exceed a medial area by a rational area, by 10.26). These are genuinely different logical strategies with different key intermediates. The AI's indirect path is logically valid under Q3, yielding classification D.

### 10.75
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they set out a rational line DI, apply areas corresponding to the sum of the squares on AB and BC and to twice the rectangle AB,BC to DI, show that the resulting breadths are rational and incommensurable in length with DI, prove these breadths are incommensurable with each other, invoke 10.73 to conclude the difference is an apotome, and use II.7 and X.20 to establish that AC is irrational. The AI separates sq(AB) and sq(BC) into individual applications (with breadths DG and DF) and then works with DG+DF, while Heath applies the combined sum of squares as a single area, but the key intermediate conclusions are identical. The citation differences are minor: heath_only contains 10.28, which is merely a construction reference for the hypothetical setup and not part of the deductive chain; ai_only contains 10.12 (an explicit transitivity step in the incommensurability argument), D10.1.3, and D10.1.4 (definitions cited for explicitness). These are all citation-depth differences, not backbone differences.

### 10.76
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 determined the classification. Heath's proof argues directly via incommensurability transfer (10.16): since the sum of squares (rational) is incommensurable with twice the rectangle (medial), by convertendo the sum of squares is incommensurable with the square on AC, making AC^2 irrational. The AI instead uses proof by contradiction: it first explicitly shows that twice the rectangle is medial (via 10.6 and 10.13), then assumes AC^2 is rational, derives that twice the rectangle would be rational (as the difference of two rational areas), contradicting its medial status. These represent genuinely different logical backbones -- Heath uses direct incommensurability reasoning with 10.16 while the AI uses an indirect/contradiction argument with 10.6 and 10.13. Both paths are logically complete and valid, making this a path difference.

### 10.77
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determines the classification. Heath's proof works directly with commensurability of areas: since the sum of squares on AB, BC is medial and twice the rectangle AB, BC is rational, these are incommensurable; by II.7 and X.16, the square on AC is incommensurable with the rational quantity, hence irrational. The AI instead introduces an auxiliary rational line DI and applies areas to it, constructing breadths DH and HK with specific commensurability properties (via X.22 and X.20), then uses X.13 to show DH and HK are incommensurable in length, identifies DH-HK as an apotome via X.73, and finally argues that the square on AC equals an irrational area. These are fundamentally different backbones: Heath argues through direct incommensurability of areas while the AI argues through the apotome construction with an auxiliary line. Since the AI's chain is logically complete under Q3 (each step follows validly from cited propositions), the classification is D.

### 10.78
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing rectangles on a rational line DI equal to the sum of squares and twice the rectangle, showing the breadths are rational and incommensurable in length with DI (via 10.22), deriving their mutual incommensurability (via 6.1 and 10.11), concluding the difference is an apotome (via 10.73), and then that the rectangle of a rational line and an apotome is irrational, hence AC is irrational. The citation differences are all depth-related: the AI adds D10.1.4 (a definition for irrationality) while Heath cites it implicitly; Heath cites 10.35 as an existence lemma for the initial configuration which the AI takes as given; and Heath cites a deduction from 10.20 for the fact that a rational times an apotome is irrational, while the AI states this as a known fact without explicit citation. All key intermediate conclusions are present in both proofs at the same logical positions, making this a citation-depth difference rather than a path difference.

### 10.79
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they set up the apotome AB with annex BC, assume a second annex BD for contradiction, apply II.7 (= 2.7) to express both sums of squares in terms of sq(AB) and twice-rectangles, identify the sums of squares as rational and the rectangles as medial (via 10.21), and derive a contradiction using 10.26 (a medial area cannot exceed a medial by a rational area). The AI proof explicitly cites foundational results that Heath uses implicitly: 10.12 and 10.15 for commensurability of the sums of squares, 10.6 for showing doubled medial areas remain medial, definitions D10.1.3 and D10.1.4 for rational and commensurable, and common notions CN2, CN3, CN5 for arithmetic manipulations. The AI also elaborates by considering the zero-difference case (Steps 13-21), showing AC=AD and BC=BD, which Heath handles implicitly by the structure of his contradiction. Since heath_only is empty and all ai_only items are over-citations of definitions, common notions, and supporting commensurability lemmas that Heath invokes without explicit reference, this is a citation-depth difference with the same backbone.

### 10.80
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the identical logical backbone: (1) assume a second annex exists per 10.74, (2) derive the algebraic identity from II.7 equating the excess of sums-of-squares to the excess of twice-rectangles, (3) show the twice-rectangle difference is rational, (4) show each sum-of-squares is medial, and (5) reach contradiction via 10.26 since a medial area cannot exceed a medial by a rational area. The only difference is citation depth for step (4): Heath cites 10.15 and 10.23 (a straight line commensurable with a medial is medial) as a packaged result, while the AI re-derives the same fact from lower-level ingredients — definitions D10.1.2 and D10.1.4, proposition 10.12 (transitivity of commensurability), and 10.15. The ai_only items (10.12, CN1, D10.1.2, D10.1.4) are all sub-steps or explicit citations of definitions/common notions, and the heath_only item 10.23 is the higher-level result the AI unpacks. This is a classic citation-depth difference with identical backbone.

### 10.81
**Category**: Path difference
**Jaccard**: 0.421
**Analysis**: Q2 decided the classification. Heath's proof reduces the uniqueness problem to showing that a certain constructed length EH is an apotome (via 10.73) with two putative annexes, then invokes the uniqueness of apotome annexes (10.79) for the contradiction. The AI proof takes a fundamentally different path: instead of reducing to apotome uniqueness, it directly argues through algebraic case analysis. In the case where the sums of squares on the two decompositions are equal, it uses algebraic identities (2.4, 2.7) to show the two annexes must be identical. In the case where the sums are unequal, it derives a contradiction via 10.26 (a medial area cannot exceed a medial area by a rational area), since the difference of sums of squares would be rational (applied to rational line EF with rational breadth) but equal to a difference of medial areas. The AI never establishes that EH is an apotome and never cites 10.73 or 10.79, which are the backbone of Heath's proof. This constitutes a genuinely different logical backbone (Q2 Case B). Under Q3, the AI's alternative path is logically complete and valid, so the classification is D.

### 10.82
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume BC is an annex to minor straight line AB, suppose BD is also an annex satisfying the same conditions (10.76), show that the excess of the sums of squares equals the excess of the double rectangles, note the sums of squares are both rational so their difference is rational, but the double rectangles are both medial, and by 10.26 a medial area cannot exceed a medial area by a rational area, yielding a contradiction. The AI proof adds significantly more algebraic detail, explicitly deriving the identity using 2.7, citing 10.15 for rational differences, using 2.4 to reconstruct the full lengths, and applying CN1/CN2/CN3 throughout, then further proving AC=AD and CB=DB. These are all finer-grained steps supporting the same backbone that Heath states more concisely. With heath_only empty and ai_only consisting entirely of algebraic identities and common notions, this is a clear case of same backbone at different citation depth.

### 10.83
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same logical backbone: assume two distinct annexes BC and BD satisfying the conditions of 10.77, show that the difference of the sums of squares equals the difference of twice the rectangles, note the rectangle difference is rational while the square-sum difference is medial, then apply 10.26 to reach a contradiction. The AI proof adds explicit Book 2 algebraic citations (2.1, 2.3, 2.4) and Common Notions (CN3, CN5) to justify the algebraic manipulations that Heath performs implicitly, and extends the argument with a detailed verification that BD equals BC. Since heath_only is empty and ai_only contains only elementary algebraic propositions and axioms that support the same intermediate conclusions, this is a same-backbone, different-depth case (Case A of Q2).

### 10.84
**Category**: Granularity difference
**Jaccard**: 0.412
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: set out a rational line EF, apply the sum of squares and twice-rectangle areas from each decomposition to EF to obtain rational breadths incommensurable with EF (10.22), show these breadths are mutually incommensurable (6.1, 10.11), conclude they are rational lines commensurable in square only forming an apotome (10.73), do the same for the second decomposition, and derive a contradiction via 10.79 (uniqueness of the annex to an apotome). The AI proof reaches the same key intermediate conclusions but is far more verbose, adding extensive exploratory analysis of commensurability relationships (Steps 13-37) and additional algebraic derivations (Steps 45-48) that Heath omits. The AI's extra citations (10.13, 10.15, 10.16, 10.26, 2.4, CN2, CN3, D10.1.4, D10.3.3, D10.3.6) all support this additional depth rather than a different logical path. Heath_only is empty, confirming the AI covers all of Heath's reasoning and adds more detail on top. This is Case A: same backbone, different citation depth.

### 10.85
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) BG is rational and commensurable in length with the set-out rational line A, (2) a second rational line (GC/GD) is found that is commensurable in square only with BG, (3) their difference is an apotome by 10.73, and (4) the two conditions of D10.3.1 (excess-square commensurability and whole commensurable with A) are verified to make it a first apotome. The difference is purely one of citation depth: Heath constructs the second line from scratch using number-theoretic machinery (10.6 for commensurability from number ratios, 10.9 for the square-number-ratio criterion, 5.19 convertendo), while the AI invokes 10.29 which packages that exact construction. The proof-tree containment test confirms that all three heath_only items (10.6, 10.9, 5.19) appear inside Heath's own proof of 10.29, so the AI is citing 10.29 as a unit while Heath re-derives its internals inline. The ai_only item D10.1.3 is merely a definition reference. This is a textbook citation-depth difference.

### 10.86
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: set out a rational line A, choose numbers with specific ratio properties (not-square-to-square and square-to-square), construct two lines where one is commensurable in length with A and the other has its square in a number ratio to the first, establish both are rational and commensurable in square only to conclude an apotome (10.73), then verify the three conditions for a second apotome -- annex commensurable with A, excess commensurable with the whole (via 5.19 and 10.9), and whole not commensurable with A -- concluding by D10.3.2. The sole difference is that the AI explicitly cites 10.12 (transitivity of commensurability) in two places where Heath performs the same reasoning without citation: once to chain square commensurabilities through the rational line A, and once in the contradiction argument showing the whole is not commensurable with A. This is a citation-depth difference (Case A), not a backbone difference.

### 10.87
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: setting out rational line A and numbers E, BC, CD with specific ratio conditions, constructing FG and GH via proportions, establishing that FG and GH are rational and commensurable in square only (so FH is an apotome by 10.73), proving via ex aequali (5.22) that neither FG nor GH is commensurable with A, and using convertendo (5.19) with the square-number ratio condition on BC:BD to show the square on FG exceeds the square on GH by the square on a line commensurable with FG, concluding FH is a third apotome by D10.3.3. The ai_only citations are 6.12 (explicitly citing the construction mechanism for finding proportional lines) and D10.1.3 (definition of rational), both of which represent over-citation at the construction/definition level rather than any backbone divergence. Heath's proof uses the same steps but does not explicitly cite these lower-level references. The heath_only set is empty, confirming no missing substantive steps.

### 10.88
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same backbone: set out a rational line, find two rational lines commensurable in square only whose square difference is incommensurable with the greater, form the apotome, and classify it as a fourth apotome using D10.3.4. The key difference is citation depth: Heath constructs the two lines inline using number-theoretic ratios and applies 10.6, 5.19 (convertendo), and 10.9 individually, while the AI invokes 10.30 directly, which packages exactly these steps (Heath's own proof of 10.30 uses 10.6, 5.19, and 10.9 internally). The proof-tree containment test confirms that all three heath_only propositions appear inside Heath's proof of 10.30, so the AI is citing 10.30 as a unit while Heath re-derives its internals inline. The AI's additional citations of 10.12 (transitivity of commensurability) and D10.1.3 (definition of rational) are explicit low-level details that Heath handles implicitly. This is a same-backbone, different-depth scenario.

### 10.89
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs follow the same backbone: set out a rational line A with CG commensurable to it, choose numbers DF and FE with DE not having square-number ratios to either, contrive the ratio so that sq(CG):sq(GB) = FE:ED, establish BG is rational via 10.6, show BG and GC are incommensurable in length via 10.9, form the apotome via 10.73, use ratio conversion (convertendo) to analyze the excess square, show the excess is incommensurable via 10.9, and conclude BC is a fifth apotome via the definition. The heath_only citation 5.19 (convertendo) is used by Heath for ratio conversion, while the AI performs the same conversion inline without citing the proposition. The ai_only citations are all at a finer granularity: D10.1.3 and D10.1.4 are definitions of rationality cited explicitly by the AI but used implicitly by Heath; 10.12 provides transitivity of commensurability that Heath leaves implicit; 10.13 is used by the AI to explicitly show AB is incommensurable with A (a step Heath leaves unstated); and 10.18 provides an alternative but equivalent justification for the incommensurability of the excess. All key intermediate conclusions appear in both proofs at the same logical positions, making this a citation-depth difference.

### 10.90
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs follow identical logical backbones: constructing numbers E, BC, CD with specific ratio constraints, deriving FG and GH via proportions, establishing their rationality and incommensurability in length (making FH an apotome via 10.73), using ex aequali (5.22) to show A incommensurable with GH, and using convertendo (5.19) to show the square on FG exceeds the square on GH by a square incommensurable with FG, concluding FH is a sixth apotome by D10.3.6. The only difference is that the AI adds two extra citations not in Heath: 10.11 (to explicitly justify transferring the non-square-ratio property through a proportion in Step 7) and D10.1.3 (to explicitly cite the definition of rational when establishing rationality of FG and GH). These are over-citations providing additional granularity for steps Heath leaves implicit, not path differences.

### 10.91
**Category**: Path difference
**Jaccard**: 0.281
**Analysis**: Q2 decides the classification. Both proofs share the initial setup (first apotome AD with annex DG, application of 10.17 to divide AG into commensurable parts) and the final step (applying 10.73 to conclude the side is an apotome), but the entire intermediate construction differs fundamentally. Heath constructs parallel lines to form rectangles AI, FK (rational) and DH, EK (medial), then builds squares LM and NO about a common diameter (6.26), using geometric mean proportionals (6.17, 5.11) and the lemma after 10.53 to assemble the algebraic identity showing AB equals the square on LN. The AI instead uses a semicircle construction on AG (via 2.14, 3.31, 6.8), defines abstract quantities p and q as square roots of AC*AE and AC*EG, derives (p-q)^2 = AB algebraically (2.1, 2.7), and proves p and q are rational and commensurable in square only using 10.26 to establish that the medial area 2pq cannot be commensurable with the rational area p^2+q^2. The large symmetric difference (Jaccard 0.281) with substantive propositions on both sides (heath_only: 6.17, 6.26, 5.11, 10.53, 10.11; ai_only: 10.26, 10.5, 10.6, 10.9, 6.8, 2.14, 2.7, 1.47, 3.31) confirms different backbones. The AI's path is logically complete under Q3, so the classification is D.

### 10.92
**Category**: Path difference
**Jaccard**: 0.450
**Analysis**: Q2 decides the classification. Both proofs share the same initial steps: establishing AG and GD as rational lines commensurable in square only, applying 10.17 to divide AG into commensurable parts AF and FG, and showing AF and FG are incommensurable with AC. However, from that point the proofs diverge substantially. Heath constructs squares LM and NO equal to the medial areas AI and FK, uses 6.26 to show they share a diameter, uses 6.17 and 5.11 to establish EK as a mean proportional, and works through a gnomon argument to show area AB equals the square on LN. The AI instead takes an algebraic approach, defining lines o and p such that sq(o)+sq(p) = rho*AC and 2*rect(o,p) = rho*BC, then showing sq(o-p) = rho*AB directly. The AI avoids the geometric square construction entirely, which explains why heath_only contains 6.26, 6.17, and 5.11 (all tied to the geometric construction) while ai_only contains 2.4, 2.5, 10.12, and 10.26 (used in the algebraic approach). Both paths validly reach the same conclusion via 10.74, but through genuinely different intermediate constructions and conclusions, making this a path difference.

### 10.93
**Category**: Path difference
**Jaccard**: 0.348
**Analysis**: Q2 reveals a different backbone between the two proofs, leading to classification D via Q3. Both proofs share the initial 10.17 application to decompose AG into commensurable parts, and both conclude via 10.75 that the side is a second apotome of a medial straight line. However, the methods diverge significantly in the middle: Heath uses a geometric construction with squares LM and NO about the same diameter (6.26), a mean proportional argument (6.17, 5.11), and gnomon reasoning to identify the side LN, while the AI introduces auxiliary lines o and p algebraically via sq(o) = r*AH and sq(p) = r*HG, uses algebraic identities (2.1, 2.7, 6.16) to show sq(o-p) = r*AD, and proves incommensurability in length through an original contradiction argument invoking 10.22, 10.73, and 10.87 (showing that commensurability would force the apotome AD to be simultaneously rational and irrational). The heath_only citations (5.11, 6.17, 6.26) belong to the geometric construction approach that the AI entirely bypasses, and the ai_only citations (10.22, 10.23, 10.73, 10.87, 2.1, 2.7, 6.16, etc.) reflect the algebraic strategy. Since these represent genuinely different proof paths rather than different citation granularity of the same argument, and the AI's path is logically complete under Q3(b), the classification is D.

### 10.94
**Category**: Granularity difference
**Jaccard**: 0.471
**Analysis**: Both proofs follow the same logical backbone: they decompose the fourth apotome AD into whole AG and annex GD, partition AG into AF and FG using 10.18, establish that AC times AG is rational (10.19) and AC times GD is medial (10.21), construct two lines whose squares sum to the rational area and whose double rectangle equals the medial area, show these lines are incommensurable in square, and apply 10.76 to conclude the side is minor. The difference lies in how the intermediate lines are constructed: Heath uses a geometric approach with squares LM and NO sharing a diameter (6.26), a mean proportional argument via ratio transitivity (5.11), and the gnomon, while the AI defines lines p and q directly via p-squared equals AC times AF and q-squared equals AC times FG, then uses algebraic identities (2.5, 2.7) and common notions (CN3). The AI also over-cites by making explicit references Heath leaves implicit (10.73 for the apotome definition, 10.12 for transitivity of commensurability, D10.1.3, D10.1.4). Since the key intermediate conclusions are identical and only the citation depth and constructive method differ, Q2 Case A applies, yielding Granularity difference.

### 10.95
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish the fifth apotome properties, show that r*AG is medial and r*GD is rational, apply a parallelogram construction that divides into incommensurable parts (via 10.18), introduce two straight lines whose squares sum to r*AG and whose double rectangle equals r*GD, establish the three conditions of 10.77 (incommensurable in square, medial sum of squares, rational double rectangle), and conclude that the difference is the irrational called 'that which produces with a rational area a medial whole.' The citation differences are depth-related: the AI cites 6.28 (application of areas) while Heath cites 6.26 (about same diameter), and the proof-tree containment test confirms that 6.26 appears inside Heath's proof of 6.28, so the AI is citing a higher-level proposition as a unit. The AI's additional citations (10.73 for the apotome definition, 10.11 for commensurability transfer, 2.7 for the algebraic identity) are auxiliary references that Heath uses implicitly or handles through geometric construction rather than explicit algebra.

### 10.96
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs follow the same logical backbone: extract properties of the sixth apotome AG, GD from D10.3.6, apply 10.18 to obtain incommensurable segments, then verify the four conditions required by 10.78 (incommensurability in square, medial sum of squares via 10.21, medial double rectangle via 10.21, and mutual incommensurability of these via 10.11). The key intermediate conclusions are identical in both proofs. The difference lies in the constructive approach: Heath constructs squares LM, NO and uses 6.26 to show they share a diameter, whereas the AI constructs straight lines MN, NP directly and uses algebraic identities (2.1, 2.7, 6.17) and explicit construction citations (1.10, 6.28) to establish the same relationships. The AI's additional citations (1.10, 2.1, 2.7, 6.17, 6.28, D10.1.3, D10.1.4) are construction tools, arithmetic identities, and definitions that make explicit what Heath handles through the geometric square construction via 6.26. This is a citation-depth difference, not a backbone difference.

### 10.97
**Category**: Granularity difference
**Jaccard**: 0.350
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) AG/BG rational commensurable in square only, (2) the sum of squares is rational so CM/EL is rational and commensurable with CD, (3) twice the rectangle is medial so FM/LF is rational and incommensurable with CD, (4) CM/EL and FM/LF are incommensurable, (5) CF/EF is an apotome, (6) the square on CM/EL exceeds the square on FM/LF by a square commensurable with CM/EL, and (7) CM/EL is commensurable with CD, making CF/EF a first apotome. The AI's ai_only citations (10.12, 10.13, 10.15, 10.5, 10.6, 10.21, 2.4, CN2, CN3, D10.1.3, D10.1.4) are predominantly sub-lemmas, definitions, and common notions that make explicit what Heath leaves implicit. Heath's 10.11 (proportional commensurability transfer) is replaced by the AI's use of 10.13 for incommensurability and 10.12 for commensurability transitivity. Heath's 10.17 (excess-square criterion from parallelogram application) is replaced by the AI's direct algebraic computation via 2.4 and 2.7 showing sq(EL)-sq(LF)=sq(EK-KL). Both routes reach the identical key conclusions, making this a citation-depth difference rather than a path difference.

### 10.98
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Both proofs share the same backbone of key intermediate conclusions: (1) decomposing sq(AB) via II.7 and applying the components to the rational line CD, (2) showing the breadth for the sum of squares is rational and incommensurable with CD while the breadth for twice the rectangle is rational and commensurable with CD, (3) concluding the result is an apotome via 10.73, and (4) establishing it is specifically a second apotome via D10.3.2. The citation differences reflect different sub-routes to the same conclusions: the AI uses 10.13 and 10.16 for transitivity of incommensurability where Heath uses VI.1 and X.11 more directly, the AI uses 10.14 to transfer commensurability properties where Heath constructs a mean proportional using 5.11 and 6.17, and the AI cites 10.22 for each square individually rather than using 10.23 to establish mediality of the combined area. These are all depth and method variations within the same logical backbone, making this a granularity difference (Q2 Case A). E was considered for Step 27's assertion that sq(AF) > sq(BF) by a commensurable amount, but the audit record showed missing_is = expansion since the AI cites 10.14 and 10.17 as supporting propositions, making the gap one of terse exposition rather than a genuine logical defect.
**Audit Record**: CANDIDATE E — 10.98
  violated_claim : sq(AF) > sq(BF) by the square on a line commensurable with AF (Step 27)
  failure_mode   : unsupported_assertion
  missing_is     : expansion (the AI cites 10.14 and 10.17, and the overall chain of reasoning is present but compressed)
  evidence       : Step 27: "they arise from the construction of 10.31 or equivalent, where sq(AF) > sq(BF) by the square on a line commensurable with AF. By 10.14, since CD * CK = sq(AF) and CD * KL = sq(BF), and sq(AF) > sq(BF) by a square commensurable with AF, then sq(CK) > sq(KL) by a square commensurable with CK"
  why_not_terse  : Cannot be completed convincingly — the AI does cite 10.14 and 10.17 which together would establish the result, and the gap is in the premise for 10.14 which is asserted tersely rather than truly missing. The argument is compressed but not logically broken. Reclassify as NOT-E.

### 10.99
**Category**: Granularity difference
**Jaccard**: 0.688
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they set up the same rectangle construction on a rational line CD, establish that the sum of squares on AG and GB is medial (yielding a rational breadth incommensurable with CD), establish that twice the rectangle AG-GB is medial (yielding another rational breadth incommensurable with CD), prove the two breadths are incommensurable with each other and hence form an apotome, and then verify the third apotome conditions (neither breadth commensurable with CD, square excess by a commensurable line). The citation differences are depth-level: the AI cites 10.14 as a shortcut for the square-excess property that Heath derives through a detailed mean-proportional argument using V.11 and 10.17; the AI cites 10.26 and references 10.75 properties for the incommensurability of sum-of-squares with twice-rectangle where Heath uses 10.13 explicitly; and the AI adds definitions D10.1.3 and D10.1.4 that Heath uses implicitly. All key intermediate conclusions are identical in both proofs.

### 10.100
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) decomposing sq(AB) via II.7, (2) establishing CF rational and commensurable with CD via X.20, (3) establishing FE rational and incommensurable with CD via X.22, (4) concluding CF-FE is an apotome via X.73, (5) establishing CK incommensurable with KF, (6) showing sq(CF) exceeds sq(FE) by the square on a line incommensurable with CF, and (7) concluding fourth apotome via D10.3.4. The citation differences reflect depth, not backbone divergence: Heath cites X.18 to directly conclude the incommensurability-of-excess condition from the fact that rect(CK,KM) = (1/4)sq(FM) with CK,KM incommensurable, while the AI re-derives this same result from scratch using II.5, X.15, and X.12 in a proof by contradiction. Similarly, Heath uses V.11 and VI.17 for the mean proportional argument, while the AI uses direct algebraic manipulation to establish sq(FE) = 4*rect(CK,KF). The AI's additional citations (10.6, 10.23, 10.13, 10.15, 10.12, D10.1.2) are elementary auxiliary propositions used in its more explicit derivation of the same conclusions.

### 10.101
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) applying the sum of squares on AG, GB to CD yields a medial area whose breadth is rational and incommensurable with CD (via 10.22); (2) twice the rectangle AG,GB applied to CD yields a rational area whose breadth is rational and commensurable with CD (via 10.20); (3) these two breadths are incommensurable, making the result an apotome (via 10.73); (4) the sub-areas CH and KL are incommensurable, leading via 10.18 to the square on the larger breadth exceeding the square on the smaller by a square on an incommensurable line; (5) the annex is commensurable with CD, identifying the result as a fifth apotome (via D10.3.5). The AI proof adds six citations not in Heath (10.13, 10.15, 10.26, 10.9, D10.1.3, D10.1.4) while Heath has no unique citations. These extra AI citations are supporting lemmas (10.13 for incommensurability transitivity, 10.15 for commensurability of sums, 10.26 for medial-rational incompatibility, 10.9 for square number ratios) and definitions that Heath uses implicitly. Since the backbone is identical and the differences are purely citation depth, this is a granularity difference.

### 10.102
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of 10.102 follows the same logical backbone as Heath's proof: decomposing the line which produces with a medial area a medial whole using 10.78, applying the component squares to a rational line CD, showing via 10.22 that both resulting lengths are rational and incommensurable with CD, establishing their mutual incommensurability via 6.1 and 10.11, concluding the result is an apotome via 10.73, then proving it is specifically a sixth apotome by showing CK incommensurable with KL, applying 10.18 for the square-excess condition, and verifying both conditions of definition D10.3.6. The citation sets are identical (Jaccard 1.0) with ai_only and heath_only both empty, and the key intermediate conclusions match throughout, satisfying the perfect match criteria.

### 10.103
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: they decompose the apotome AB into AE - BE via 10.73, construct corresponding lines CF and DF for CD, establish that CF and DF are rational and commensurable in square only, derive the proportion CF:DF = AE:BE, and then show both criteria determining the order of apotome are preserved using 10.14, 10.12, and 10.13. The AI's ai_only citations (10.5, 10.6, 10.7, 10.8) appear inside Heath's proof of 10.11, confirming the AI re-derives 10.11's internals rather than citing it as a unit. The AI cites 5.11 where Heath cites 5.16 (alternation), but the underlying logical step is the same alternation inference, making this a mis-citation rather than an invalid inference. The AI avoids 5.12 by constructing CF and DF directly via 6.12, and adds 6.22 and 10.9 as explicit sub-lemmas. The numerous definition citations (D10.1.2-D10.1.4, D10.3.1-D10.3.6) are over-citations of definitional material. All differences are citation-depth differences with the same key intermediate conclusions.

### 10.104
**Category**: Granularity difference
**Jaccard**: 0.353
**Analysis**: Q2 decides this classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) construct new segments proportional to the original annex segments, (2) show the new segments are medial, (3) show they are commensurable in square only, (4) show the rectangle formed by the new segments is commensurable with the original rectangle, and (5) conclude same order based on whether the rectangle is rational or medial. The differences lie entirely in which proportionality and commensurability lemmas are invoked: Heath uses 5.12 and 5.16 for proportion manipulation and 10.13 for transferring incommensurability, while the AI uses 5.19 and 6.22 for proportion handling and a direct contradiction argument via 10.11. The AI also adds extra citations (10.80, 10.81 for uniqueness of decomposition, 10.24, 6.16, CN3) and explicitly splits into two cases (first vs second apotome of medial) where Heath uses a single conditional argument, but these are presentation and citation-depth differences, not backbone differences.

### 10.105
**Category**: Path difference
**Jaccard**: 0.062
**Analysis**: The AI proof takes a fundamentally different path from Heath's proof. Heath works directly with the parts of the minor line, showing that the corresponding parts CF, FD of CD satisfy the defining properties of a minor line (incommensurable in square, sum of squares rational, rectangle medial) using proportions (5.12, 5.16, 6.22, 5.18) and properties of the minor line (10.76). The AI instead uses an application-of-areas strategy: it applies the squares on AB and CD to a rational line, shows that the breadth from AB is a fourth apotome (10.100), that the breadth from CD is commensurable with it and hence also a fourth apotome (10.103), and then invokes 10.94 to conclude that CD is minor. These are entirely different logical backbones with different key intermediate conclusions. Q2 Case B applies (different backbone), and Q3 confirms the AI's path is logically valid, with each step properly supported by cited propositions. The Jaccard similarity of 0.062 reflects this near-complete divergence in citation sets.

### 10.106
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this classification as D (path difference). Heath's proof works directly with the geometric decomposition via the annex construction, showing that CF and FD satisfy the same conditions as AE and EB (incommensurable in square, sum of squares medial, rectangle rational) and then invoking 10.77 to conclude CD is the required irrational line. The AI takes an entirely different approach through the theory of apotomes: it applies the squares on AB and CD to a rational line to produce breadths, shows the breadth from AB is a fifth apotome (10.101), transfers the apotome order via commensurability (10.103), and then uses 10.95 to conclude that CD produces with a rational area a medial whole. The two proofs share zero citations (Jaccard = 0.0) and establish completely different key intermediate conclusions — Heath works with direct geometric properties of line segments while the AI works with areas applied to rational lines and apotome classification. The AI's path is logically complete and valid, with every step properly supported by cited propositions, so this is a genuine path difference rather than an error.

### 10.107
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined this classification. The two proofs have entirely different backbones (Jaccard 0.0, zero citation overlap). Heath's proof works directly with the segment-based characterization from 10.78: it transfers the algebraic properties (incommensurability in square, medial sum of squares, medial rectangle, incommensurability between sum and rectangle) from the segments of AB to the corresponding segments of CD via commensurability, then re-applies 10.78. The AI proof instead uses the apotome classification machinery: it applies the square on AB to a rational line to obtain a sixth apotome breadth (10.102), shows commensurability of AB and CD transfers to commensurability of the breadths (10.11, 6.1), concludes the second breadth is also a sixth apotome (10.103), and then converts back via 10.96 to conclude CD is the right line type. These are fundamentally different intermediate conclusions forming independent logical paths, both valid. Under Q3, the AI's chain is logically complete and sound, so the classification is D.

### 10.108
**Category**: Granularity difference
**Jaccard**: 0.889
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: apply the rational and medial areas to a rational line, use 10.20 and 10.22 to determine commensurability properties of the resulting breadths, use 10.13 to show they are incommensurable in length, invoke 10.73 to identify an apotome, then split into two cases (first apotome via D10.3.1 leading to apotome via 10.91, or fourth apotome via D10.3.4 leading to minor via 10.94). The only citation difference is that the AI explicitly cites D10.1.3 (definition of rational lines being commensurable in square) in Step 6 to justify a fact that Heath treats as implicit. Since ai_only contains only a definition and heath_only is empty, and the key intermediate conclusions are identical, this is a granularity difference where the AI over-cites by making an implicit definitional step explicit.

### 10.109
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone: apply the medial and rational areas to a rational line FG to obtain breadths FH and FK, establish that FH and FK are rational and commensurable in square only (hence KH is an apotome via 10.13 and 10.73), then split into two exhaustive cases based on whether the square excess is commensurable or incommensurable with FH, yielding a second apotome (leading to a first apotome of a medial via 10.92) or a fifth apotome (leading to a line producing with a rational area a medial whole via 10.95). The only difference is that the AI explicitly cites 10.20 and 10.22 to justify the commensurability properties of FK and FH when applied to FG, while Heath states these facts without explicit citation. Since heath_only is empty and ai_only contains only these two supporting propositions that justify steps present in both proofs, this is a same-backbone, different-citation-depth situation.

### 10.110
**Category**: Granularity difference
**Jaccard**: 0.700
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: applying medial areas to a rational line to obtain rational breadths incommensurable with the rational line, establishing the breadths are mutually incommensurable, concluding the difference is an apotome, then splitting into two cases (third apotome yielding a second apotome of a medial straight line via 10.93, or sixth apotome yielding a line producing with a medial area a medial whole via 10.96). The citation differences are superficial: the AI adds 10.25 (a side observation about rectangles of rational lines not essential to the argument) and D10.1.3 (a definition), while Heath cites 6.1 for the proportionality step that the AI handles via 10.11. Both reach the same key intermediate conclusion (FH incommensurable with HK) by slightly different citation routes. This is a same-backbone, different-citation-depth scenario, yielding G.

### 10.111
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: The classification is decided at Q2/Q3. Heath's proof applies the square on AB to a rational straight line to produce a breadth DE, then shows DE must simultaneously be a first apotome (10.97) and a first binomial (10.60), deriving a contradiction by showing a segment EG would be both an apotome and rational. The AI instead takes a direct algebraic approach: it decomposes AB as a binomial sum (CD+DE) and an apotome difference (FG-GH), computes AB squared two different ways using 2.4 and 2.7, shows the sums of squares are rational while the double rectangles are medial (via 10.21), and derives a contradiction because a rational area would equal a sum of medial areas. The key intermediate conclusions are entirely different -- Heath's pivot is that a segment is simultaneously an apotome and rational, while the AI's pivot is that a rational area equals a sum of medial areas. The AI's path is logically sound, with all steps properly cited and the case analysis (commensurable vs incommensurable medial areas) being exhaustive. This constitutes a genuine path difference (D).

### 10.112
**Category**: Path difference
**Jaccard**: 0.083
**Analysis**: Q2 determines the classification as D (path difference). Heath's proof constructs auxiliary segments H, K within the breadth EF, uses proportion chains (VI.16, V.17, V.12, V.11) to establish FK and KE as the terms of the apotome, then verifies the order via explicit case analysis with X.14. The AI proof takes a fundamentally different approach: it forms L = BD - DC, shows L is an apotome by X.73, uses II.5 and VI.1 to establish that EF is commensurable in length with L, then invokes X.103 to transfer the apotome classification and term structure from L to EF. The AI argues that L shares the same order as the binomial BC because they share the same pair of terms (BD, DC), so the two order-determining conditions are identical. These are genuinely different logical backbones — Heath never forms BD - DC or uses X.103, while the AI never constructs the proportion-based auxiliary segments HK, KF, KE. The AI's path is logically valid: each step is supported by cited propositions, and X.103's proof (verified in Heath) does establish that commensurable apotomes have commensurable terms in the same ratio. No E-level defect is present under the hardened standard.

### 10.113
**Category**: Path difference
**Jaccard**: 0.121
**Analysis**: The AI proof takes a fundamentally different path from Heath's. Heath directly constructs the terms KF and FH of the binomial KH through a chain of proportion manipulations (using convertendo, alternando, and commensurability results 5.11, 5.14, 5.16, 5.19, 6.16, 10.12, 10.14, 10.20) and then verifies their properties step by step. The AI instead constructs the auxiliary binomial BF = AC + CB, shows the breadth DE is commensurable in length with BF (hence binomial of the same order by 10.66), then invokes the converse theorem 10.112 to establish that applying sq(rho) to the binomial DE yields apotome AB with terms matching DE's terms, and finally uses the uniqueness of apotome decomposition (10.79) to conclude the term correspondence. The two proofs share almost no key intermediate conclusions — Heath builds up through direct proportion manipulation while the AI leverages the converse theorem and commensurability transfer — producing a Jaccard of only 0.121. Q3 confirms the AI's path is logically valid: the difference-of-squares identity (2.5), the commensurability chain (10.11, 10.15, 6.1), the binomial transfer (10.66), the converse application (10.112), and the uniqueness argument (10.79) all form a sound chain from premises to conclusion.

### 10.114
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: apply a rational square to the binomial to produce an apotome breadth (10.112), establish commensurability of terms (10.12), derive that the original apotome is commensurable with the new apotome, then use 6.1 and commensurability to conclude the rectangle is commensurable with the rational square, making the side rational. The sole heath_only citation is 10.11 (proportional commensurability transfer), whose own proof uses 10.5 and 10.6 — exactly the ai_only substantive citations. The AI re-derives the internals of 10.11 inline rather than citing it as a unit, which is a citation-depth difference. The remaining ai_only items (5.16 alternation used implicitly by Heath, 5.17 for ratio manipulation achieving the same conclusion as Heath's use of 5.19, and D10.1.4 as an implicit definition) are all over-citations of steps Heath leaves implicit. Since the key intermediate conclusions are identical and the differences are purely in citation granularity, this is G.

### 10.115
**Category**: Path difference
**Jaccard**: 0.056
**Analysis**: Q2 decided the classification. Heath's proof constructs an infinite sequence of irrationals by iteratively forming sq(C) = rect(B, A), deducing C is irrational via a deduction from 10.20 and X. Def. 4, then repeating with D where sq(D) = rect(B, C), and so on. The AI proof takes a fundamentally different approach: it applies the square of each medial line to a rational line to get a rational breadth (via 10.22), then forms a new medial from the rectangle of that breadth with the rational line (via 10.21), iterating to produce infinite medials. The AI further constructs additional irrational types (first bimedial via 10.37, second bimedial via 10.38, first and second apotomes of medials via 10.74 and 10.75) and uses uniqueness results (10.111, 10.42, 10.43, 10.44, 10.79, 10.80, 10.81) to prove distinctness. The key intermediate conclusions differ: Heath works with generic irrationals through a simple iterated rectangle-and-square construction, while the AI specifically constructs classified medial lines and then branches into multiple irrational types. This constitutes a different logical backbone (Q2 Case B). Under Q3, the AI's path is logically complete with a valid chain from premises to conclusion, so the classification is D.


## Book 11

| Category | Count |
|---|---|
| Perfect match (P) | 1 |
| Granularity difference (G) | 28 |
| Path difference (D) | 10 |
| AI proof error (E) | 0 |

**Total**: 39 propositions

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume for contradiction that part AB of line ABC lies in the reference plane while part BC is elevated, construct a line BD as the continuation of AB entirely within the reference plane, identify that ABC and ABD share the common segment AB, and derive a contradiction from the impossibility of two distinct straight lines sharing a common segment. Heath appeals to a circle-based argument (diameters cutting unequal circumferences) while the AI appeals to D1.4 (uniqueness of straight line continuation) to establish the impossibility, but these are different expressions of the same geometric fact forming the same key intermediate conclusion. The citation sets differ because Heath has no recorded citations while the AI explicitly cites foundational items (D1.4, D1.7, P2), which are definitions and a postulate representing over-citation at the axiomatic level. Since the backbones match and the differences are only in citation depth, this is a granularity difference (G).

### 11.2
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: that two intersecting straight lines lie in one plane (via contradiction using 11.1) and that every triangle lies in one plane (again via contradiction using 11.1). The AI reverses the order of argument compared to Heath (proving coplanarity of intersecting lines first, then triangles, whereas Heath proves the triangle result first), but the backbone geometric facts are identical. The ai_only items D1.19 (definition of triangle) and P1 (postulate for joining points) are a definition and a postulate that Heath uses implicitly, making this a citation-depth difference rather than a path difference. Since the citation sets are not identical (AI adds D1.19 and P1), this is G rather than P.

### 11.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume for contradiction that the common section DB is not straight, construct straight lines DEB in plane AB and DFB in plane BC, observe that two distinct straight lines share the same endpoints and thus enclose a space (which is impossible), and conclude DB must be straight. The AI proof explicitly cites D1.7 (definition of a plane surface) and P1 (postulate for drawing straight lines) while Heath's proof uses these same foundations implicitly without explicit citation. Since heath_refs is empty and ai_only contains only a definition and a postulate (not substantive propositions), this is a straightforward case of the AI over-citing foundational axioms and definitions, which is a citation-depth difference with the same backbone. This yields Granularity difference (G).

### 11.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) AD=BC and angle DAE=angle EBC via triangle congruence I.4 with vertical angles I.15, (2) GE=EH and AG=BH via I.26, (3) FA=FB and FC=FD via I.4, (4) angle FAD=angle FBC via I.8, (5) FG=FH via I.4, (6) angle GEF=angle HEF via I.8, concluding that EF is perpendicular to the plane via XI.Def.3. The logical backbones are identical. The ai_only set consists entirely of construction/foundational items (1.3, P1, P4, CN1, D1.10) that Heath leaves implicit, while heath_only is empty. This is a clear Case A granularity difference where the AI over-cites axiomatic and constructive steps.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: assume one of the three lines is not in the plane determined by the other two, use 11.3 to find the intersection line of the assumed separate plane with the original plane, use 11.4 to establish perpendicularity to the original plane, then use D11.3 to show a right angle with the intersection line, and derive a contradiction from having two equal right angles with distinct lines from the same point. The AI proof explicitly cites P4 (all right angles are equal) and CN5 (the whole is greater than the part) to articulate the final contradiction, while Heath leaves these steps implicit, simply stating the equality is impossible. Since heath_only is empty and ai_only contains only axiom-level citations (P4, CN5) that make explicit what Heath uses implicitly, this is a same-backbone, different-citation-depth situation — Case A of Q2.

### 11.6
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decides the classification. Both proofs share the same high-level strategy (construct DE perpendicular to BD, prove angle EDA is right, use XI.5 for coplanarity, conclude parallelism), but the key intermediate conclusions differ substantively. Heath proves angle EDA is right via triangle congruence: I.4 (SAS) yields AD = BE, then I.8 (SSS) yields angle ABE = angle EDA, so EDA is right. The AI instead uses a Pythagorean approach: I.47 applied three times gives squared-length relationships, algebraic substitution (CN1, CN2) yields AE squared = AD squared + DE squared, and I.48 (converse Pythagorean theorem) gives angle ADE is right. These are genuinely different mathematical techniques with different intermediate geometric facts (equality of segments vs. squared-length identities), not merely different levels of granularity. Additionally, the final parallelism step uses different propositions: Heath applies I.28 (co-interior angles) while the AI applies I.27 (alternate angles). The AI's path is logically valid throughout, so this is a path difference (D), not an error.

### 11.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 11.7 by contradiction: assuming the joining line EF is in a more elevated plane, he uses 11.3 (plane intersection yields a straight line) to derive two lines EGF and EF enclosing an area, which is impossible. The AI instead gives a direct proof: since parallel lines share a plane P (D1.23), it constructs triangle EHF from points on those lines, uses 11.2 (every triangle is in one plane) to place it in plane Q, extends AB fully into Q via 11.1, shows EF lies in Q as a side of the triangle, then similarly shows CD is in Q, and concludes P equals Q by uniqueness of the plane through three non-collinear points. The two proofs have entirely different key intermediate conclusions and share no citations (Jaccard 0.0). The AI's direct constructive path is logically sound, so Q3 confirms a valid different path, yielding category D.

### 11.8
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) angle ABD is right via D11.3, (2) A,B,C,D coplanar via 11.7, (3) CD perpendicular to BD via 1.29, (4) construct DE perpendicular to BD in the reference plane, (5) angle ABE is right via D11.3, (6) angle ADE is right, (7) DE perpendicular to the plane through BD and AD via 11.4, (8) DC in that plane, (9) DE perpendicular to CD, (10) CD perpendicular to the reference plane via 11.4. The difference lies in how step (6) is established: Heath uses triangle congruence (SAS then SSS, requiring DE = AB) while the AI uses the Pythagorean theorem (1.47) and its converse (1.48). This is a different micro-level technique reaching the same key intermediate conclusion, not a different backbone. The AI's additional citations of 1.11 and P1 are construction-level over-citations, and its omission of 11.2 is a granularity matter since the AI makes the equivalent argument textually without citing 11.2. Same backbone with different citation depth yields G.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct GH and GK perpendicular to EF in their respective planes, apply XI.4 to establish EF is perpendicular to the plane through GH and GK, then use XI.8 to show AB and CD are each perpendicular to that plane, and finally apply XI.6 to conclude AB is parallel to CD. The only difference is that the AI explicitly cites I.11 for the construction of perpendiculars GH and GK, while Heath states the construction without citing this justification. Since 1.11 is a construction proposition and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference (Case A in Q2), yielding Granularity difference.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: cutting BA, BC, ED, EF equal, showing AD and CF are each equal and parallel to BE (via I.33 applied twice), deducing AD is equal and parallel to CF (via XI.9 and transitivity), concluding AC equals DF (via I.33 a third time), and finally applying SSS congruence (I.8) to obtain angle ABC = angle DEF. The AI's three extra citations (1.3 for cutting off equal segments, P1 for joining lines, CN1 for transitivity of equality) are all construction-level or axiom-level steps that Heath performs implicitly without explicit citation. With heath_only empty and ai_only consisting entirely of over-citations of foundational steps, this is a clear Case A same-backbone, different-depth scenario, yielding Granularity difference (G).

### 11.11
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: draw BC in the plane, drop AD perpendicular to BC, draw DE at right angles to BC in the plane, draw AF perpendicular to DE, draw GH parallel to BC through F, then argue that BC is perpendicular to the plane through DA and DE (XI.4), GH is likewise perpendicular to that plane (XI.8 via parallelism), GH is therefore perpendicular to AF (XI.Def.3), and since AF is perpendicular to both GH and DE it is perpendicular to the reference plane (XI.4). The only citation difference is that the AI includes P1 (a postulate for drawing a line) which Heath leaves implicit. Since ai_only contains only a postulate and heath_only is empty, and all key intermediate conclusions match, this is a granularity difference (Case A of Q2).

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: (1) conceive an elevated point B, (2) draw BC perpendicular to the given plane using 11.11, (3) draw AD through A parallel to BC using 1.31, (4) conclude AD is perpendicular to the plane by 11.8 since it is parallel to a line perpendicular to the plane. The only citation difference is that the AI explicitly cites D11.3 (the definition of a line being at right angles to a plane) to frame the construction goal and the conclusion, while Heath leaves this definition implicit. Since D11.3 is a definition and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference classifying as G.

### 11.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs follow the same logical backbone: assume two lines AB, AC from point A are perpendicular to the same plane on the same side; the plane through AB and AC cuts the reference plane in a straight line DE (by 11.3); both angles BAE and CAE are right by D11.3; therefore BAE equals CAE, yet one is part of the other since AB and AC are distinct lines on the same side, giving a contradiction. The AI proof adds three citations not in Heath: 11.2 (for the fact that AB and AC determine a plane, which Heath simply assumes without citation), P4 (all right angles are equal, which Heath states implicitly), and CN5 (whole is greater than part, which Heath expresses as 'which is impossible' without citing the common notion). All three ai_only items are over-citations of foundational or axiomatic steps that Heath leaves implicit, representing citation-depth differences rather than backbone divergence. Heath_only is empty, confirming the AI covers all of Heath's reasoning. The citation sets differ so this is not P.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume the planes are not parallel, derive a common section line GH via 11.3, take a point K on GH, join AK and BK, use D11.3 to establish that both angles ABK and BAK are right angles, then obtain a contradiction via 1.17 (two angles of a triangle sum to two right angles), and conclude the planes are parallel by D11.8. The only citation difference is that the AI explicitly cites postulate P1 for the construction step of joining AK and BK, while Heath performs this step implicitly without citing the postulate. Since ai_only contains only P1 (a postulate/construction axiom) and heath_only is empty, this is a straightforward case of over-citation at the construction level, which is a citation-depth difference under Case A of Q2, yielding category G.

### 11.15
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: constructing BG perpendicular to the plane through DE, EF (11.11), drawing GH parallel to ED and GK parallel to EF in that plane (1.31), establishing that angles BGH and BGK are right via the definition of perpendicularity to a plane (D11.3), using 11.9 to show AB is parallel to GH and BC is parallel to GK, applying 1.29 to show the transversal BG creates right angles ABG and CBG, concluding via 11.4 that BG is perpendicular to the plane through AB, BC, and finally invoking 11.14 to establish the planes are parallel. The citation sets are identical (Jaccard = 1.0) with ai_only and heath_only both empty, and the key intermediate conclusions match at every stage, yielding a perfect match classification.

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: proof by contradiction assuming the two common-section lines meet at a point K, showing K must lie in both parallel planes (contradicting the hypothesis), and concluding the lines are parallel by definition. The citation differences are purely depth-related. Heath cites 11.1 to justify that a point on a line in a plane must be in that plane; the AI makes the equivalent argument directly from the definition of common section without citing 11.1. The AI explicitly cites 11.3 (common section of two planes is a straight line) and D11.8 (definition of parallel planes), which Heath uses implicitly. These are over-citations of construction and definitional facts. The key intermediate conclusions are identical in both proofs, with only the citation granularity differing.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct AD meeting the middle plane at a point, use 11.16 twice to establish parallelisms (EO/EG parallel to BD, and OF/FG parallel to AC), apply 6.2 twice to obtain proportional relationships in triangles ABD and ACD, and then conclude via 5.11 (transitivity of ratios). The AI's only structural difference is that it applies 6.2 from the opposite vertex in triangle ACD, yielding DF:FC = DG:GA instead of Heath's direct AO:OD = CF:FD, and then explicitly inverts the ratio using definitions D5.5 and D5.13. The ai_only citations (P1, D5.5, D5.13) are all postulates or definitions representing over-citation of construction steps and ratio manipulation that Heath handles implicitly. Since heath_only is empty and the key intermediate conclusions are identical, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 11.18
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: take an arbitrary plane through AB, identify its common section with the reference plane, draw a line in that plane perpendicular to the common section (I.11), show AB is perpendicular to the common section via D11.3, conclude AB is parallel to FG via I.28, deduce FG is perpendicular to the reference plane via XI.8, and apply D11.4 to conclude the plane is at right angles to the reference plane. The only citation difference is that the AI explicitly cites 11.3 to justify that the intersection of two planes is a straight line, a fact Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only 11.3 (a foundational proposition making explicit what Heath takes for granted), this is a same-backbone, different-citation-depth scenario, yielding Granularity difference (G).

### 11.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume BD is not perpendicular to the reference plane, draw perpendiculars in each of the two planes to the lines of intersection with the reference plane, apply Definition 11.4 to conclude both constructed lines are perpendicular to the reference plane, then invoke 11.13 to reach a contradiction (two lines from the same point cannot both be perpendicular to a plane on the same side). The AI's two extra citations (1.11 for drawing perpendicular lines and 11.3 for the common section being a straight line) are construction-level propositions that Heath uses implicitly without explicit citation. Since the key intermediate conclusions are identical and the citation differences reflect only citation depth, this is a granularity difference.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: (1) construct angle BAE equal to DAB in the plane of BAC with AE equal to AD, (2) show DB = BE via I.4, (3) use I.20 on triangle BDC to derive DC > EC, (4) apply I.25 to conclude angle DAC > angle EAC, and (5) combine to get DAB + DAC > BAC. The AI proof cites additional construction propositions (1.23 for angle construction, 1.3 for cutting off equal lengths), postulate P1 (for drawing lines), and common notions (CN2, CN3, CN5) for the arithmetic inequality reasoning, all of which Heath leaves implicit. Since heath_only is empty and all ai_only items are construction/axiom over-citations, this is a clear Case A granularity difference.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: (1) use XI.20 to show that at each base vertex the face angles exceed the corresponding base polygon angle, (2) use I.32 to establish that both sets of triangles have equal total angle sums, and (3) conclude by subtraction that the face angles at A are less than four right angles. The AI generalizes from Heath's three-face-angle case to a five-face-angle case with an interior point O, but this is a presentational generalization, not a different logical path. The ai_only citations (1.13, 1.15, CN5, D11.11, P1) are all postulates, definitions, common notions, or low-level supporting propositions that Heath uses implicitly without citation. Heath_only is empty, confirming the AI cites everything Heath cites plus additional granularity. This is a clear case of over-citation at a finer granularity level.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same key backbone: constructing an auxiliary angle equal to one of the given angles at point H, cutting off a segment equal to the common side length, then using I.4 (SAS congruence) to equate a chord and I.24 (greater angle yields greater opposite side) to establish the needed inequality. Heath's proof constructs KHL equal to angle ABC and derives AC + GK > DF, noting 'similarly' for the other two inequalities. The AI proof takes the largest angle (GHK) first to dispatch two easy inequalities directly, then uses the same construction technique (angle GHL = angle BAC) to prove the critical inequality BC + EF > GK. The heath_only set is empty, confirming the AI cites every proposition Heath cites. The ai_only set consists entirely of construction and auxiliary propositions (1.3, 1.20, 1.22, 1.23, P1) that Heath uses implicitly but does not cite explicitly. This is a citation-depth difference with the same logical backbone, placing it squarely in the G category.

### 11.23
**Category**: Granularity difference
**Jaccard**: 0.190
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) constructing triangle LMN from the three angle bases via 11.22, (2) circumscribing a circle and finding its center O, (3) establishing that AB is greater than OL, (4) erecting a perpendicular at O and setting its square equal to the excess of AB-squared over OL-squared, (5) showing the resulting segments from the apex equal AB, and (6) proving the solid angle has the given plane angles via I.8. The large symmetric difference in citations (Jaccard 0.19) reflects different methods for proving subsidiary steps rather than different backbones. Heath proves AB > LO through a two-case contradiction using proportionality (VI.2, VI.4, V.16) and I.25/I.29, while the AI proves it by arguing that O must lie inside triangle LMN (using 1.13, 1.21) and then inferring AB > OL. Heath uses I.4 (SAS) to establish RL = RM, while the AI uses I.47 (Pythagorean theorem) directly. The AI also explicitly cites construction steps (P1, P3, 1.3, 4.5, 2.14) and definitions (D1.15, D11.3) that Heath leaves implicit. Since all key intermediate conclusions are the same and the differences are in citation depth and subsidiary argument methods, this is a granularity difference.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish all six faces are parallelograms using XI.16, (2) show corresponding sides of opposite faces are equal using I.34, (3) prove corresponding angles are equal using XI.10, (4) establish congruence of the triangles formed by diagonals using I.4 (SAS), and (5) conclude opposite faces are equal. The AI's two extra citations (1.29 and CN2) represent over-citation rather than a different path. CN2 is used explicitly to add equal triangles into equal parallelograms, where Heath uses I.34 to say each parallelogram is double of the respective triangle. I.29 is used to justify that supplementary angles are equal when their supplements are equal, a step Heath leaves implicit. Since the key intermediate conclusions are identical and the citation differences reflect only explicitness of minor steps, this is a granularity difference (G).

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same equimultiple strategy: construct replicas of the parallelepiped to form equimultiples of the bases and solids, show the replicated solids are equal by XI.24, verify that the exceed/equal/fall-short relationship between base multiples carries over to solid multiples, and conclude by V. Def. 5 (D5.5) that base is to base as solid is to solid. The AI proof is more verbose and cites many additional foundational results (1.3, 1.34, 1.4, 11.16, 6.1, CN4, CN5, D11.1, D11.2, D11.8, P1) that Heath takes as implicit. The citation of 6.1 in Step 9 is a parenthetical observation not essential to the argument. Heath_only is empty, confirming the AI covers all of Heath's reasoning. The key intermediate conclusions are identical in both proofs, with the AI simply providing finer-grained justification for each step.

### 11.26
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 determined this classification. The two proofs construct the same solid angle but through structurally different methods. Heath drops a perpendicular from F to the plane through ED and DC, constructs angles BAL and BAK at A equal to EDC and EDG respectively, then uses three applications of I.4 (SAS) and one of I.8 (SSS) to establish the face angle equalities. The AI instead drops a perpendicular from E to the plane DFC, constructs perpendiculars from the foot G to edges DC and DF, uses 11.18 to establish perpendicularity of planes, D11.4 for line-plane perpendicularity, and employs I.26 (AAS congruence) rather than I.8 (SSS). The construction geometry differs (different perpendicular direction, different intermediate points), and the triangle congruence strategy differs (AAS vs SSS), yielding a genuinely different backbone. The AI's path is logically complete under Q3, with each step supported by cited propositions, so the classification is D.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) construct an equal solid angle at A corresponding to C, (2) establish proportional edges about the equal solid angles, (3) show corresponding faces are similar parallelograms, (4) conclude the solids are similar by D11.9. The difference lies in how proportions are established: Heath sets up two separate proportions (EC:CG=BA:AK and GC:CF=KA:AH) and derives the third via ex aequali (5.22), while the AI sets up all three proportions directly from a single common ratio AB:CE, avoiding the need for 5.22. The heath_only citation 5.22 appears inside Heath's proof of 6.24 (which the AI cites), satisfying the proof-tree containment test and confirming a citation-depth difference. The ai_only items (1.3, 1.31, 11.24, 11.26, 6.24, D6.1) are construction-level and definitional citations that Heath leaves implicit. Since both proofs reach the same geometric conclusions through the same logical backbone at different levels of citation granularity, this is a granularity difference.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they cut the parallelepiped by a plane through the diagonals of opposite faces, use I.34 to show those diagonals bisect the faces into equal triangles, establish that the lateral faces of the two resulting prisms are equal (because opposite faces of the parallelepiped are equal), and conclude by D11.10 that the two prisms are equal. The AI additionally cites 11.24 explicitly to justify the equality of opposite faces, whereas Heath simply states this as a known fact ('for they are opposite'). The AI also cites D11.13 (definition of a prism) to identify each half as a prism, which Heath leaves implicit. Both ai_only items (11.24 and D11.13) represent over-citation of supporting facts that Heath takes for granted, making this a same-backbone, different-depth situation — Case A of Q2 — yielding Granularity difference (G).

### 11.29
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Both proofs follow the same backbone strategy: identify two triangular prisms filling the gaps between the two parallelepipeds, show the prisms are equal via pairwise face equality, then use addition/subtraction to conclude the parallelepipeds are equal. Q2 Case A applies because all key intermediate conclusions appear in both proofs at the same logical positions. The citation differences are theorem-variant substitutions at the same step (AI uses 1.8/SSS where Heath uses 1.4/SAS for triangle congruence; AI uses 1.35 where Heath uses 1.36 for parallelogram equality) plus the AI explicitly citing definitions (D11.10, D11.13), common notions (CN3, CN4), and prior results (1.33, 11.24) that Heath leaves implicit. These are citation-depth differences, not backbone differences.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct an auxiliary parallelepiped by extending edges of the two given solids until they meet, show each original solid equals this auxiliary solid via XI.29 (since they share the same base and their standing edges terminate on the same straight lines), then conclude by transitivity that the two original solids are equal. The AI's additional citations (1.31, 1.34, 11.1, 11.24, CN1, D11.13, P1, P2) are all over-citations of construction tools, definitions, postulates, and common notions that Heath leaves implicit. Heath_only is empty, confirming no substantive steps are missing from the AI proof. This is a clear Case A in Q2: same backbone with different citation depth.

### 11.31
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 determines the classification. Heath's proof constructs a copy of one solid adjacent to the other, then uses geometric arguments with XI.29 (parallelepipeds with edges on same lines), I.35 (parallelogram equality), and V.11 (ratio transitivity) to show equality. The AI takes a fundamentally different path: it reduces both parallelepipeds to rectangular boxes via two applications of XI.30 (a re-orientation technique not in Heath), then proves the boxes equal using Book VI ratio arguments (6.1, 6.16) and ex aequali (5.22) -- propositions Heath does not use. The backbones differ at the level of key intermediate conclusions: Heath's intermediate is a constructed copy solid shown equal via geometric cutting and proportion transitivity, while the AI's intermediate is a pair of rectangular boxes shown equal via area-based proportion arguments. Both paths are logically complete, so Q3 confirms D.

### 11.32
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: construct a parallelogram FH equal to AE (by I.45), complete a parallelepiped GK on FH with the same height as CD, show AB equals GK by XI.31 (equal bases, same height), apply XI.25 to establish the ratio between the solids and their bases, then substitute equals to conclude AE:CF = AB:CD. The AI's three extra citations (11.27 for the parallelepiped construction, 5.7 and 5.11 for explicit ratio substitution steps) represent over-citation of steps that Heath performs implicitly without naming specific propositions. Since heath_only is empty and the ai_only items are all construction or ratio-manipulation propositions that merely make explicit what Heath leaves implicit, this is Case A of Q2: same key intermediate conclusions with different citation depth, yielding a Granularity difference.

### 11.33
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 reveals genuinely different backbones. Heath establishes the continuous proportion among four solids by first using 6.1 to relate parallelogram areas to edge ratios, then 11.32 to convert parallelogram ratios into solid ratios (AB:EO, EO:QL, QL:KP). The AI takes a fundamentally different route: it constructs different intermediate solids (EX and EY rather than Heath's EO and QL) and applies 11.25 directly three times to establish solid-to-solid ratios without passing through parallelogram ratios at all. The proof-tree containment test confirms this is not mere citation depth: while 11.32 does use 11.25 internally, Heath applies 11.32 to solids sharing the same height (comparing bases), whereas the AI applies 11.25 to cuts of combined solids (effectively comparing heights given the same base), producing a structurally different argument. Both paths validly reach the triplicate ratio via D5.10, making this a path difference rather than a granularity difference.

### 11.34
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs construct an auxiliary parallelepiped and use proportion chains to establish the reciprocal relationship between bases and heights, but the specific constructions and intermediate conclusions differ substantively. Heath places the auxiliary solid CV on base NQ with height equal to AG and uses 6.1 (parallelograms under same height as bases) and 5.7 (equal magnitudes have same ratio) to establish intermediate ratios, while the AI places the auxiliary solid FO on base EH with height equal to CN and uses 11.25 (solid cut by parallel plane) for height ratios and 5.11/5.16 for ratio manipulation. The heath_only citations (11.30, 5.7, 6.1) do not appear inside the proofs of any AI-cited proposition, confirming this is not a containment/granularity difference but a genuinely different geometric path. The AI's path is logically valid under Q3: each step follows from cited propositions (the miscitation of 5.16 for inverse proportion is a naming error, not a logical gap, since the inversion operation is sound), and the proof covers both the forward direction and the converse.

### 11.35
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determined this classification. Heath's proof works by drawing a line HK parallel to GL through a point H on the elevated line (using 11.8 to transfer perpendicularity), then uses 1.48 to establish right angles at C and F, applies 1.26 (AAS) repeatedly to derive equal segments, and ultimately reaches the conclusion via 1.8 (SSS). The AI proof takes a fundamentally different path: it constructs AB = DE and AC = DF directly on the rays (using 1.3), establishes congruence of multiple triangle pairs via 1.4 (SAS) and 1.8 (SSS), then proves the critical equality GH = MN through an innovative area-based contradiction argument using 1.41, showing that unequal perpendicular heights would force unequal triangle areas, contradicting the established equality. The key intermediate conclusions differ substantially -- Heath's backbone involves perpendiculars to the sides of the angle and AAS congruence (1.26), while the AI's backbone involves an area decomposition and proof by contradiction. Since the AI's different path is logically sound, the classification is D.

### 11.36
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 reveals fundamentally different proof backbones, leading to classification D at Q3. Heath's proof directly constructs two parallelepipeds with the given edges and shows they have equal bases (via reciprocal proportionality, VI.14) and equal heights (via XI.35 Porism), then concludes equality by XI.31. The AI proof takes an entirely different ratio-based approach: it introduces an intermediate solid Q with edges A, B, B, uses XI.32 and VI.1 to establish the ratios S:Q = C:B and Q:P = A:B, then applies ex aequali (V.22) to obtain S:P = B:B, concluding S = P by V.9. The citation sets are completely disjoint (Jaccard = 0.0), reflecting genuinely different mathematical strategies rather than mere differences in citation depth. The AI's ratio-chain approach is logically complete and valid, satisfying Q3(b).

### 11.37
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: they use XI.33 to establish that similar parallelepipedal solids are in the triplicate ratio of their corresponding sides, then in the forward direction conclude that equal base ratios yield equal solid ratios, and in the converse that equal solid ratios yield equal base ratios. Heath's proof is extremely concise, treating the triplicate ratio relationship as a direct consequence of XI.33 in both directions. The AI proof makes the triplicate ratio construction explicit by building continuous proportions via 6.11 and D5.10, chains proportions using 5.11 and 5.22 (ex aequali), and uses proof by contradiction via 5.8 for the converse direction. Despite the AI's more elaborate machinery and different technique in the converse, the key intermediate conclusions are the same: the triplicate ratio of side ratios determines the solid ratios (forward) and vice versa (converse). The ai_only citations (5.11, 5.22, 5.8, 6.11, D5.10, D5.9) represent over-citation of proportion-theory results that Heath leaves implicit, and heath_only is empty, confirming that no substantive step present in Heath is absent from the AI proof.

### 11.38
**Category**: Path difference
**Jaccard**: 0.188
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof works by showing DUE and BSG are collinear straight lines (via I.4 SAS congruence and I.14), establishing DB parallel to EG (via XI.9 transitivity of parallelism), then proving DE parallel to BG (via I.33), and finally using AAS triangle congruence (I.26) on triangles DTU and GTS to conclude DT=TG and UT=TS. The AI proof takes a fundamentally different approach: it identifies the intersection points S and T as the centers of opposite faces of the cube, constructs the cross-sectional parallelogram ASTG (using I.34, 11.24, 6.2, and I.33), and concludes that since AG and ST are diagonals of parallelogram ASTG, they bisect each other (via I.29 alternate angles and I.26 triangle congruence). The key intermediate conclusions differ substantially: Heath never constructs parallelogram ASTG, and the AI never establishes collinearity of DUE or the parallelism DB to EG via XI.9. Both paths are logically complete, yielding a valid path difference.

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: complete both prisms to parallelepipeds, show their bases are equal (since both are double the given triangle), conclude the parallelepipeds are equal by XI.31, then conclude the prisms are equal since each is half its parallelepiped by XI.28. The AI's three extra citations (CN1, CN2, D11.13) are all common notions and a definition that Heath leaves implicit. CN1 makes explicit the transitivity step equating the two parallelogram bases, CN2 makes explicit the inference that halves of equal things are equal, and D11.13 cites the definition of a prism. Since heath_only is empty and ai_only contains only axiom-level items, this is a clear case of over-citation at the same logical depth, yielding a granularity difference.


## Book 12

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 11 |
| Path difference (D) | 6 |
| AI proof error (E) | 1 |

**Total**: 18 propositions

### 12.1
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish that triangles ABM and FGN (formed by joining polygon vertices to the endpoints of the diameters) are equiangular, derive the proportion BM:GN = BA:GF via VI.4, and then use the duplicate ratio (VI.20) to connect the polygon ratio to the ratio of squares on the diameters. The difference lies in how each proof obtains the key angle equality feeding into the triangle equiangularity. Heath uses VI.6 to first prove triangles ABE and FGL equiangular (from one equal angle and proportional sides in the similar polygons), then extracts the angle equality, and applies III.27 for inscribed angles on equal circumferences. The AI instead reads the corresponding angle equality directly from the definition of similar polygons (D6.1), bypasses VI.6 entirely, and uses III.21 (angles in the same segment) rather than III.27 for the inscribed angle step. The AI's additional citations (5.11, CN1, D5.9, P4) are axiom/definition-level over-citations making explicit what Heath leaves implicit. Since the key intermediate conclusions (equiangularity of the diameter-triangles, the side proportion, and the duplicate ratio conclusion) are the same in both proofs, the difference is one of citation depth rather than a fundamentally different proof path.

### 12.2
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same double reductio ad absurdum backbone using the method of exhaustion: assume circles are not as the squares on their diameters, then derive contradictions for both S < circle EFGH and S > circle EFGH, concluding S = circle EFGH. The key intermediate conclusions are identical in both proofs: the exhaustion process yields an inscribed polygon exceeding S, similar polygons relate as squares on diameters (12.1), proportion reasoning (5.11, 5.16) produces the contradiction. The ai_only set (1.34, 1.41, 10.1, 3.30, 4.6, 5.14, CN5) consists entirely of construction steps, auxiliary results, and common notions that Heath uses implicitly but does not cite explicitly — the inscribed square construction (4.6), arc bisection (3.30), the exhaustion lemma (10.1), area relationships (1.34, 1.41), proportion reasoning (5.14), and the whole-greater-than-part axiom (CN5). heath_only is empty, confirming the AI cites a strict superset of Heath's references. This is a clear case of the AI providing greater citation depth for the same logical backbone.

### 12.3
**Category**: Path difference
**Jaccard**: 0.263
**Analysis**: Q2 decides the classification. Heath's proof establishes the equality of the two sub-pyramids via SAS congruence (I.4) applied to corresponding face triangles, using XI.10 to establish angle equality between lines in different planes, and proves the prisms exceed half the whole pyramid by geometric containment (showing each prism contains a pyramid equal to one of the sub-pyramids). The AI's proof takes a fundamentally different path: it establishes similarity of the sub-pyramids by directly computing all six edge lengths as half the corresponding edges of the original (using 6.2 midline properties), proves equality via SSS congruence (1.8 instead of I.4), identifies the prisms through parallelogram structures (1.33), and argues the prisms exceed half the whole via a volume-ratio calculation (claiming each sub-pyramid is 1/8 of the original using 11.33 and 6.19). The backbones differ in both the congruence method and the approach to the prisms-greater-than-half conclusion. E was considered for the AI's application of 11.33 (similar parallelepipeds) to pyramids, but under the lenience rule, the underlying mathematical inference is sound (similar pyramids do have volumes in the cube of the linear ratio), making this an informal-but-sound inference rather than an invalid one. The different logical backbone (SSS vs SAS, direct edge computation vs angle-based congruence, volume ratios vs geometric containment) constitutes a genuine path difference.
**Audit Record**: CANDIDATE E — 12.3
  violated_claim : "each similar pyramid has all linear dimensions halved, so each has volume (1/2)^3 = 1/8 of the original [the ratio of similar solids is the cube of the linear ratio, following from 11.33 and 6.19]"
  failure_mode   : invalid_inference
  missing_is     : expansion
  evidence       : AI Step 11 cites 11.33 (similar parallelepipeds in triplicate ratio) and 6.19 (similar triangles in duplicate ratio) to justify that similar pyramids have volumes in the cube of the linear ratio. 11.33 applies to parallelepipeds, not pyramids. The correct result for pyramids is 12.8 (forward from 12.3).
  why_not_terse  : Cannot complete convincingly — the mathematical inference is sound (similar pyramids do have volumes in cubic ratio), the AI merely cited the wrong covering proposition. Under lenience rule, this is informal-but-sound, not invalid. Reclassified to NOT-E (D).

### 12.4
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 reveals different logical backbones. Heath establishes the key ratio (prisms from one pyramid to prisms from the other as base to base) through a chain involving similarity of triangles (ABC~LOC, DEF~RVF), Proposition 6.22 (similar figures on proportional lines are proportional), 5.16 (alternation), the Lemma following 12.3, and 11.39 (relating parallelogram-based and triangle-based prisms). The AI instead uses Proposition 6.1 (triangles of the same height are as their bases) applied directly to the prism bases, arguing that the equal-height condition and uniform midpoint scaling make 6.1 sufficient to establish the same ratio. This is a genuinely different geometric argument — not a matter of citation depth but of which geometric facts drive the proof. The AI's path is logically valid: 6.1 does apply to the prism bases given the equal height of the original pyramids, and the combination via 5.12 and recursive application are sound. Q3 confirms validity, yielding classification D.

### 12.5
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Both proofs follow the same exhaustion-by-contradiction backbone: assume the ratio base:base equals pyramid:W where W is not the second pyramid, handle Case 1 (W less than the second pyramid) via successive subdivision by XII.3, exhaustion by X.1, and prism ratio by XII.4 to derive a contradiction, then handle Case 2 (W greater) by reducing to Case 1 via inversion. The key intermediate geometric conclusions are identical. The differences lie entirely in which Book V ratio-manipulation propositions are cited for the algebraic steps: the AI uses 5.11 (transitivity), 5.14 (ordering of proportionals), CN5 (whole greater than part), and D5.13 (definition of inverse ratio) where Heath uses V.11/V.16 (alternation) and XII.2 Lemma. The AI's use of 5.14 plus CN5 to derive the contradiction is a valid alternative to Heath's alternation step via 5.16, and the AI's use of D5.13 for inversion replaces Heath's reference to the XII.2 Lemma. These are citation-depth differences in the ratio algebra, not backbone differences, making this a granularity difference.

### 12.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: decompose polygonal bases into triangles via diagonals, apply XII.5 to compare triangular pyramids of equal height, then recombine the ratios to obtain the final proportion. The key difference is the recombination mechanism: Heath uses V.18 (componendo) sequentially to build up the polygon ratio one triangle at a time, while the AI uses V.24 (ratio addition with a common second term) to aggregate all triangular sub-pyramid ratios simultaneously. The proof-tree containment test confirms this is a depth difference rather than a path difference: V.18 appears inside Heath's own proof of V.24, so the AI is citing a higher-level result (5.24) that internally relies on the step Heath applies directly (5.18). The remaining ai_only items (P1 for drawing diagonals, D5.5 for ratio inversion) are construction and definitional over-citations consistent with granularity difference.

### 12.7
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification. Both the AI and Heath proofs argue through identical key intermediate conclusions: (1) diagonal BD bisects parallelogram ABED so triangle ABD equals triangle BDE (I.34), (2) pyramids with equal triangular bases and the same height are equal (XII.5), yielding pyramid ABCD = pyramid BCDE, (3) diagonal CE bisects parallelogram BCFE so triangle BCE equals triangle CEF (I.34), (4) again by XII.5 pyramid BCDE = pyramid CDEF, and (5) therefore all three pyramids are equal. The AI proof adds explicit citations to definitions D11.12 and D11.13 (for prism and related solid geometry terms) and CN1 (transitivity of equality), which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions and a common notion, this is a clear case of over-citation at the same logical backbone, making it a granularity difference.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: complete parallelepipedal solids on the similar pyramids, show the parallelepipeds are similar (XI.24), apply XI.33 to get the triplicate ratio of corresponding sides, then relate pyramid to parallelepiped via prism = half parallelepiped (XI.28) and prism = triple pyramid (XII.7), yielding the pyramid ratio equals the triplicate ratio. The AI cites all four of Heath's references (11.24, 11.28, 11.33, 12.7) and adds nine further citations (11.31, 5.11, 5.15, 6.4, CN1, D11.9, D5.10, D6.1, P1) which are definitions, common notions, postulates, and lower-level propositions supporting the same steps at finer granularity. heath_only is empty, confirming the AI misses nothing Heath uses. The key intermediate conclusions are identical in both proofs, making this a citation-depth difference, not a path difference.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decides this as G (granularity difference, Case A). Both proofs share the same logical backbone: construct parallelepipeds from the given pyramids, apply XI.34 to obtain reciprocal proportionality of parallelogram bases and heights, then use I.34 to relate triangular bases to parallelogram bases, and chain the proportions. The difference is purely in citation depth and which specific lemmas are invoked for equivalent steps. Heath goes directly from pyramid to parallelepiped (factor of 6) and uses V.11 to chain proportions, while the AI takes a more explicit two-step route through prisms (XII.7 for pyramid-to-prism, XI.28 for prism-to-parallelepiped) and uses V.15 instead of V.11 for the proportion chaining. The ai_only items (XII.7, XI.28, CN2, CN3) are construction-level and common-notion citations that spell out what Heath does more concisely, and V.15 replaces V.11 for an equivalent logical step. The heath_only item V.11 is a proportion-transitivity result that the AI replaces with V.15 (parts have the same ratio as their multiples), achieving the same intermediate conclusion. The key geometric facts established are identical in both proofs.

### 12.10
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification. In Case 1 (cylinder > 3 times cone), both proofs follow essentially the same exhaustion argument: inscribe polygons, show the prism on the polygon exceeds 3 times the cone, invoke 12.7 to get the pyramid exceeds the cone, contradicting containment. However, in Case 2 (cylinder < 3 times cone), the backbones diverge. Heath inscribes pyramids within the cone, exhausts the cone from the inside, and shows the inscribed pyramid exceeds a third of the cylinder, yielding a prism exceeding the cylinder while being contained in it. The AI instead circumscribes a polygon about the circle, constructs a prism and pyramid that contain the cylinder and cone respectively, and derives a contradiction from the circumscribed pyramid exceeding the cone while the corresponding prism is less than 3 times the cone. This circumscribed-polygon strategy in Case 2 is a genuinely different logical path from Heath's inscribed-pyramid approach, producing different key intermediate conclusions. Q3 confirms the AI's path is logically valid: the exhaustion principle applies to circumscribed polygons, 12.7 gives prism = 3 times pyramid for any polygon, and the containment and contradiction arguments are sound.

### 12.11
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 identified genuinely different backbones between the two proofs, leading to classification under Q3. Heath proves the result for cones first using an exhaustion argument with inscribed pyramids, applies alternando (5.16) as a key ratio step, and then extends to cylinders via 12.10. The AI reverses the order entirely: it proves the result for cylinders first using an exhaustion argument with inscribed prisms (justified by decomposing prisms into pyramids via 12.7 and applying 12.5/12.6), uses ratio comparison properties (5.8, 5.10) instead of alternando (5.16), and then derives the cone result from the cylinder result via 12.10 and 5.15. These structural differences -- proving cylinders before cones, using prisms rather than pyramids as the primary exhaustion objects, and substituting different ratio-manipulation propositions -- constitute a different logical path. The AI's path is logically valid throughout: the exhaustion argument is properly structured, the prism-to-pyramid decomposition is sound, and the derivation of the cone result from the cylinder result is correct.

### 12.12
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Heath's proof uses the method of exhaustion with inscribed polygons and pyramids: it inscribes polygons in the base circles, erects pyramids, proves these pyramids are similar (via VI.6, V.16, V.22, VI.5), applies XII.8 (similar pyramids in triplicate ratio), sums them with V.12, and obtains the result by double reductio ad absurdum. The AI takes a fundamentally different path: it introduces an intermediate solid C sharing A's base and B's height, decomposes the ratio A:B into A:C (height ratio, established via prisms and exhaustion) and C:B (base ratio squared, via XII.11 and XII.2), then compounds these via V.22 ex aequali to obtain the triplicate ratio. The backbones are entirely different -- Heath works through similar pyramids and exhaustion while the AI works through ratio decomposition via an intermediate solid. The AI's Step 4 mis-cites XI.32 (same height implies ratio of bases) for the converse claim (same base implies ratio of heights), but the underlying mathematical fact is correct and provable in Euclid's system; under the lenience rule this is not an error but a citation issue. The AI's proof path is logically complete and valid, yielding classification D.
**Audit Record**: CANDIDATE E — 12.12
  violated_claim : "These prisms, being parallelepipedal solids on equal bases, are to one another as their heights h_A and h_B by 11.32"
  failure_mode   : invalid_inference
  missing_is     : expansion — XI.32 establishes same-height-as-bases; the AI needs same-base-as-heights which is the converse, but the mathematical fact is correct and derivable; this is a citation error not a logical gap
  evidence       : AI Step 4 cites XI.32 ("Parallelepipedal solids which are of the same height are to one another as their bases") but applies it to prisms on equal bases to conclude they are as their heights — the converse
  why_not_terse  : Cannot complete convincingly — the underlying mathematical claim is true and the AI's broader argument is sound; the error is in citing the wrong proposition number, not in the logical structure. Reclassify as NOT-E.

### 12.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the identical equimultiple strategy mandated by Definition V.5: they construct arbitrary multiples of the two axis segments, erect corresponding cylinders by cutting with parallel planes, use XII.11 to show that the small cylinders with equal bases and equal heights are equal, establish that the m-fold and n-fold composite cylinders are equimultiples of the respective segment cylinders, verify the trichotomy (excess, equal, less) between the composite cylinders tracks the trichotomy between the composite axes, and conclude by V. Def. 5 that the ratio of cylinders equals the ratio of axes. The key intermediate conclusions are identical in both proofs. The only difference is citation depth: the AI explicitly cites common notions (CN1, CN2, CN5), definitions (D11.21, D11.22, D11.23, D11.8, D5.2), and postulates (P1, P2) that Heath leaves implicit. Since heath_only is empty and all ai_only items are foundational (no substantive theorems), this is a clear Case A granularity difference.

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct an auxiliary cylinder sharing one parameter (base or height) with each of the two original cylinders, use XII.11 (cylinders of same height are as their bases) to show the auxiliary equals one original, use XII.13 (cutting a cylinder by a parallel plane gives proportional axes) to establish the proportion with the other, then extend to cones via XII.10. The AI explicitly cites Book 5 proportion-theory results (5.7 for substituting equals in ratios, 5.15 for parts having the same ratio as multiples, 5.11 for transitivity of ratios) that Heath applies implicitly without citation. Since heath_only is empty and ai_only contains only proportion-manipulation lemmas that justify steps Heath performs without explicit citation, this is a classic over-citation granularity difference.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same biconditional structure: forward direction with two cases (equal heights and unequal heights) and the converse. The key intermediate conclusions are identical in both proofs: in the unequal-heights case, both construct an auxiliary solid sharing one base with one original and the height of the other, then establish two ratio equalities (one from equal-height comparison via 12.11, one from equal-base/height comparison) and combine them via 5.11. The only substantive citation difference is that the AI uses 12.14 (cones/cylinders on equal bases are as their heights) where Heath uses 12.13 (cylinder cut by parallel plane gives ratio equal to ratio of axes). The proof-tree containment test confirms that 12.13 appears inside Heath's proof of 12.14, so the AI is citing a higher-level result as a unit while Heath effectively re-derives its internals inline. The AI's additional citation of CN1 is a common notion (over-citation). This is a citation-depth difference with the same logical backbone.

### 12.16
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 reveals different backbones, leading to Q3 which confirms a valid different path (D). Heath's proof constructs a tangent line AC to the lesser circle (III.16), then bisects arcs until arc LD < AD, draws LM perpendicular to BD, shows LD = DN (III.3, I.4), and argues that since LN is parallel to AC and AC touches the lesser circle, LN does not touch it either — a parallelism-based argument. The AI proof instead argues through perpendicular distances: it uses the Pythagorean theorem (1.47) and III.14 to show that as arcs decrease through repeated bisection, the perpendicular distance from the center to each chord increases, and by X.1 this distance eventually exceeds the radius of the lesser circle, so no side touches it. These are genuinely different intermediate mechanisms — Heath uses tangent-parallelism while the AI uses perpendicular-distance comparison — producing different key intermediate conclusions with different supporting citations. The AI's perpendicular distance chain is logically sound and complete, satisfying Q3.

### 12.17
**Category**: Path difference
**Jaccard**: 0.133
**Analysis**: Q2 decided the classification. Heath's proof establishes the non-touching property via a synthetic chain: showing faces are cyclic quadrilaterals (using III.27, I.26, VI.2 for parallelism and I.33, XI.9 for coplanarity), then bounding the perpendicular AX via KB^2 > 2*BX^2 and KB^2 < 2*KZ^2 (using III.31 and VI.8), concluding AX > AZ > AG. The AI proof takes a fundamentally different route: it applies 12.16 twice (once for the meridional polygon yielding d_0 > r, once for the azimuthal subdivision yielding a_2/R > r/d_0), reduces the 3D perpendicular distance to a 2D computation in the meridional plane via symmetry (11.13), then uses the 'two-base area method' (1.41) to express perpendicular distances as ratios and bounds them using the Pythagorean theorem (1.47). The backbones share no key intermediate conclusions: Heath never computes areas or uses 12.16; the AI never establishes cyclic quadrilaterals or uses proportion theory (VI.2, VI.8). The Jaccard similarity of 0.133 reflects this deep divergence. The AI proof is logically complete with all claims properly supported, yielding a valid different path (D).

### 12.18
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same double reductio backbone: (1) assume the triplicate ratio holds to a sphere less than the target, inscribe similar polyhedral solids via 12.17, derive a contradiction where the lesser sphere must be both greater and less than the inscribed polyhedron; (2) handle the greater-than case by inversion reducing to the already-refuted case; (3) conclude. The AI's ai_only citations (12.8, 5.11, 5.12, CN5, D11.14, D11.17, D5.10) represent finer-grained detail: the AI explicitly breaks down why similar polyhedra have the triplicate ratio via 12.8 (similar pyramids in triplicate ratio of sides) and 5.12 (combining parts), while Heath cites 12.17 as a unit covering this. The definitions and CN5 are implicit in Heath. Heath's heath_only citations (12.2 Lemma for the greater-case reduction, 5.16 for alternando) correspond to steps the AI performs by direct reasoning or uses without listing: the AI applies alternando in Step 11 and handles the greater case by straightforward inversion rather than citing 12.2 Lemma. The key intermediate conclusions are identical at matching logical positions in both proofs, confirming Case A of Q2.


## Book 13

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 6 |
| Path difference (D) | 12 |
| AI proof error (E) | 0 |

**Total**: 18 propositions

### 13.1
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Heath's proof works through geometric figures: he constructs squares on AB and DC, identifies rectangles and gnomons within those figures, and uses VI.1 (proportionality of parallelograms under the same height) to establish that CK is double CH, building up to show the whole square AE equals the gnomon MNO and then that sq(CD) = 5*sq(DA). The AI instead takes an algebraic approach: it expands sq(AC+AD) using II.4 (the square-of-a-sum identity), substitutes rect(AB,CB)=sq(AC) from the golden ratio property, then uses II.1 (distribution of rectangles) to combine terms, and simplifies to reach 5*sq(AD). These are genuinely different key intermediate conclusions -- Heath's backbone runs through gnomon-area comparisons and VI.1 proportionality, while the AI's backbone runs through algebraic expansion via II.4 and distribution via II.1. Since the AI's algebraic path is logically complete with every step properly cited or justified, Q3 confirms this as a valid path difference (D).

### 13.2
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof constructs squares on AB and CD, then through area computations involving gnomons shows that gnomon MNO equals CG, leading to rectangle CD*DB = CB squared, thereby establishing DC:CB = CB:BD via area relationships and VI.1. The AI proof takes a fundamentally different approach: it cuts CD in extreme and mean ratio using VI.30 to obtain greater segment CE, then applies XIII.1 (the converse-direction result about extreme-and-mean-ratio cuts) to show (CE + CD/2) squared = 5 times (CD/2) squared. Since CD/2 = AC and the hypothesis gives AB squared = 5 times AC squared, the AI deduces CE + AC = AB, hence CE = CB. The two proofs have entirely different key intermediate conclusions -- Heath's backbone is area-based gnomon equalities while the AI's backbone leverages XIII.1 as a key lemma. The AI's path is logically valid at every step, so Q3 confirms D rather than E.

### 13.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) the extreme-and-mean-ratio property gives rect(AB,BC) = sq(AC), (2) the bisection AC = 2DC yields sq(AC) = 4*sq(DC), and (3) combining these with the expansion of sq(DB) produces sq(DB) = sq(AC) + sq(DC) = 5*sq(DC). Heath uses geometric area manipulation with gnomons and named regions (FG, RS, CE, gnomon OPQ) while the AI uses algebraic identities from Book 2 (propositions 2.1 and 2.4), but the logical backbone is identical. Since heath_refs is empty, all AI citations (1.10, 2.1, 2.4, 6.17, CN2, D6.3) appear in ai_only, representing explicit citations for facts that Heath uses implicitly without formal citation. This is a citation-depth difference (Case A in Q2), yielding G.

### 13.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) rect(AB,BC) = sq(AC) from the golden ratio definition and 6.17, (2) the algebraic identity sq(AB) + sq(BC) = 2*rect(AB,BC) + sq(AC), and (3) substitution to get sq(AB) + sq(BC) = 3*sq(AC). The difference is in citation depth: the AI explicitly cites proposition 2.7 to establish the algebraic identity in step (2), while Heath re-derives the equivalent result inline through a geometric gnomon argument on the constructed figure. The AI also explicitly cites CN1 for the substitution step, which Heath leaves implicit. Since the backbone of key conclusions is the same and the only difference is that the AI cites 2.7 as a packaged result while Heath unpacks the equivalent reasoning geometrically, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 13.5
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they start from the golden ratio definition to establish AB*BC = AC^2 (via D6.3 and 6.17), then derive DA*DB = AB^2, convert this to the proportion DB:BA = BA:AD (via 6.17), and finally show BA > AD. The difference is in the tools used to traverse this backbone. Heath uses a geometric diagram with squares and rectangles (AE, CE, HC, DK) to reach DA*DB = AB^2, while the AI uses algebraic manipulation via 2.3 and CN2 to reach the same conclusion. For the ordering step, Heath cites 5.14 (proportion-preserves-ordering from DB > BA), while the AI argues directly via CN5 (whole > part, since AC is a proper part of AB and DA = AC). The ai_only items (1.3, 2.3, CN2, CN5, P2, P3) are construction propositions, common notions, postulates, and an algebraic identity — all reflecting different citation depth rather than a different backbone. The heath_only item (5.14) is replaced by an equivalent direct argument. Since both proofs establish the same key intermediate conclusions through the same logical chain but at different levels of citation granularity, this is a granularity difference.

### 13.6
**Category**: Path difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification. Both proofs agree on the first half: AC is shown to be an apotome via XIII.1 (sq(CD) = 5 sq(DA)), establishing CD and DA as rational lines commensurable in square only, then applying X.73. However, the proofs diverge fundamentally on the second half (showing CB is an apotome). Heath uses the application-of-areas technique: since AB is cut in extreme and mean ratio, rect(AB,BC) = sq(AC) by VI.Def.3 and VI.17, and then X.97 shows that applying the square on an apotome to a rational line produces a first apotome, so CB is a first apotome. The AI instead takes a direct algebraic path: computing CB = 3D - F (where D = AB/2 and F = AC + D), proving 3D is rational and that 3D and F are commensurable in square only (since sq(3D):sq(F) = 9:5, not a ratio of square numbers), then applying X.73 to conclude CB is an apotome. These represent genuinely different key intermediate conclusions -- Heath's route through application of areas (VI.17) and X.97 versus the AI's direct commensurability argument via X.73. The AI's path is logically valid (Q3 confirmed), yielding classification D.

### 13.7
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 determined the classification. Heath's proof of Case I (three consecutive equal angles) introduces the intersection point F of diagonals AC and BE, uses I.6 to derive AF = BF, then deduces FC = FE, and applies I.8 to triangles FCD and FED to obtain angle FCD = angle FED. The AI proof never introduces any intersection point; instead it works with whole diagonals, applying I.4 to different triangle pairs (ABC/DCB rather than Heath's ABC/ABE), derives angle equalities via I.5 on isosceles sub-triangles, uses CN3 for angle subtraction, and ultimately applies I.8 to triangles ADE and BEA to establish the fifth angle. The key intermediates differ: Heath's backbone runs through AF = BF (via I.6) and FC = FE, while the AI's runs through angle ACD = angle ABD and angle CDA = angle BAD. For Case II (not in order), Heath handles it as a single case while the AI splits into two sub-cases (consecutive pair among the three vs. no consecutive pair). Both proofs are logically complete, but they follow genuinely different geometric paths, so the classification is D.

### 13.8
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 determined this classification. Heath's proof circumscribes a circle about the pentagon (4.14) and uses arc-angle relationships (3.28, 6.33) to establish that angle EAC is double angle BAC, then derives the extreme-and-mean-ratio proportion EB:BA = AB:BH directly via similar triangles and uses 5.14 for the magnitude comparison. The AI proof takes a fundamentally different approach: it computes the pentagon's interior angle as 6R/5 from the angle sum theorem (1.32), derives base angles of isosceles triangles directly (2R/5 and 4R/5), establishes intermediate results like BC = HC and HE = AE = AB from isosceles triangle properties, then uses similar triangles with 6.4 and converts via 6.17 to reach the extreme-and-mean-ratio form. The key intermediate conclusions differ: Heath relies on circumscribed-circle arc properties while the AI uses explicit angle computation and introduces the intermediate conclusion BC = HC (not in Heath). The heath_only citations (3.28, 4.14, 5.14, 6.33) are not subsumed by any single AI-cited proposition; they represent a genuinely different geometric route. The AI's path is logically complete with each step properly cited, so this is a valid path difference.

### 13.9
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 determined this classification. Heath proves the extreme-and-mean-ratio property directly by angle-chasing through arc-angle relationships (6.33), establishing equiangularity of triangles EBD and EBC, and then applying proportionality in similar triangles (6.4) to derive BD:DC = DC:CB. The AI takes a fundamentally different route: it recognizes the central triangle of the decagon as the isosceles triangle from 4.10 (whose base angles are each double the vertex angle), extracts from 4.10's construction (which uses 2.11) that the radius r is cut in extreme and mean ratio with s_10 as the greater segment, and then applies 13.5 (the additive property of extreme and mean ratio) to conclude that s_6 + s_10 is cut in EMR with s_6 as the greater segment. The key intermediate conclusions differ: Heath's backbone runs through similar triangles and direct proportionality, while the AI's backbone runs through the 4.10 triangle identification and the 13.5 additive lemma. Both paths are logically complete and valid, making this a genuine path difference.

### 13.10
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Heath's proof establishes that triangles ABF and BFN are equiangular (using I.5, I.26, I.32, VI.33) to derive AB*BN = BF^2 via VI.4 and VI.17, then establishes that triangles KBA and KNA are equiangular (using I.4, I.32) to derive BA*AN = AK^2, and finally combines these via II.2 to obtain BA^2 = BF^2 + AK^2. The AI proof takes a fundamentally different approach: it uses the Pythagorean theorem (1.47) on right triangles formed by the perpendicular from the center to the chord, invokes 13.9 (the hexagon-plus-decagon golden ratio property) to establish h^2 = hd + d^2, and then proceeds through algebraic manipulation (2.4, 2.7) to derive s^2 = h^2 + d^2. The two proofs share essentially no key intermediate conclusions -- Heath works through similar triangles and rectangle equalities while the AI works through perpendicular distances, the Pythagorean theorem, and 13.9. The Jaccard similarity of 0.1 (only 4.15 and 6.17 shared) reflects this genuine path divergence. The AI's proof is logically complete and valid throughout, so Q3 confirms D.

### 13.11
**Category**: Path difference
**Jaccard**: 0.227
**Analysis**: Q2 decides this classification as D (path difference). Heath's proof works directly with the geometry of the inscribed pentagon, using similar triangles (I.32), proportion theory (V.18 componendo, V.19 convertendo), commensurability transfer (X.12, X.15), and XIII.8 (diagonals of the pentagon cut in extreme and mean ratio) to establish that a key segment MB is a fourth apotome. The AI proof takes a fundamentally different route via the hexagon-decagon decomposition: it uses XIII.10 (sq on pentagon side = sq on hexagon side + sq on decagon side), XIII.9 (hexagon + decagon sides in extreme-mean ratio), and XIII.6 (segments of rational line cut in extreme-mean ratio are apotomes), then constructs the breadth w = 5r/2 - N algebraically and classifies it as a fourth apotome. The key intermediate conclusions differ entirely: Heath derives DC:CM = MF:FK through triangle similarity and then sq(MK) = 5*sq(KF); the AI derives sq(s) = r*(2r - s_10) through the hexagon-decagon relationship. Both paths validly reach the conclusion that the pentagon side is the irrational called minor via X.94, but through genuinely different geometric reasoning.

### 13.12
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: inscribe the equilateral triangle, show a specific arc is 1/6 of the circumference, conclude the corresponding chord equals the radius (via 4.15), establish a right angle in a semicircle (via 3.31), apply the Pythagorean theorem (via 1.47), show the diameter squared is four times the radius squared, and subtract to obtain that the side squared is triple the radius squared. The AI proof adds eleven citations beyond Heath's three (1.47, 3.31, 4.15), but these are all over-citations of definitions (D1.15, D1.17, D1.18, D1.20, D4.3), postulates (P1, P2), common notions (CN3), a construction step (3.1), and intermediate results that Heath uses implicitly without citation (3.28 for equal arcs from equal chords, 2.4 for the square on the diameter being four times the square on the radius). Heath's citation set is a proper subset of the AI's, and heath_only is empty, confirming identical reasoning at different levels of citation granularity.

### 13.13
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Heath constructs the tetrahedron with apex K raised above center H of the base circle via perpendicular HK, proving edge equality through SAS congruence (I.4) and comprehending the figure in the sphere via a semicircle rotation argument using VI.8, VI.17, and III.31. The AI instead constructs the tetrahedron with vertex A at one endpoint of the diameter, proves edge equality through direct Pythagorean computation (I.47), and demonstrates sphere comprehension by computing each vertex's distance from the sphere center O. These are genuinely different geometric constructions yielding different logical backbones: the AI's algebraic-computational approach via I.47 replaces Heath's synthetic-congruence approach via I.4, and the AI's center-distance argument for sphere inscription replaces Heath's semicircle-rotation argument. Since both paths are logically complete and valid, the classification is D.

### 13.14
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs construct the octahedron identically: setting out square EFGH with sides equal to DB, erecting perpendiculars KL and KM from the center K, and joining edges to form eight equilateral triangular faces. Both proofs establish the same key intermediate conclusions: (1) the square on DB is half the square on AB, (2) edges like LE equal the side DB via I.47 applied to right triangles at K, (3) all eight faces are equilateral, (4) the octahedron is inscribed in the given sphere because LM = AB, and (5) the square on the diameter is double the square on the side. The AI proof cites 17 references while Heath cites only 4, but heath_only is empty, meaning the AI cites every proposition Heath uses. The 13 ai_only items are entirely construction propositions (1.10, 1.11, 1.3, 1.46), properties of parallelograms used for the square (1.29, 1.34), definitions (D1.20, D11.3, D11.14, D11.17, D11.26), a common notion (CN1), and a postulate (P1). These represent explicit citation of steps that Heath performs silently, which is the hallmark of a citation-depth difference rather than a path difference.

### 13.15
**Category**: Granularity difference
**Jaccard**: 0.118
**Analysis**: Q2 decides this classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) constructing a cube with side equal to DB, (2) showing the space diagonal squared equals three times the side squared, (3) showing the space diagonal equals the diameter AB, and (4) concluding the cube is comprehended in the given sphere with the diameter squared being triple the side squared. The heath_only set is empty, meaning every Heath citation (I.47, XI.Def.3) appears in the AI set. The AI's 15 additional citations (ai_only) consist of construction postulates (P1, P3), common notions (CN1, CN2), definitions (D11.14, D11.25), construction propositions (1.10, 1.46, 11.12), parallelogram properties (1.33, 1.34), the semicircle angle theorem (3.31), proportionality results (6.8, 6.17), and parallel line criteria (11.6) -- all representing explicit citation of steps that Heath leaves implicit. The AI's use of 6.8 and 6.17 for the mean proportional derivation and its equidistance approach for sphere comprehension (via 1.33, 1.34) are more detailed articulations of the same geometric facts that Heath establishes without explicit citation. This is Case A of Q2: same backbone, different citation depth.

### 13.16
**Category**: Granularity difference
**Jaccard**: 0.281
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) AB^2 = 5*DB^2 via the initial construction, (2) all 30 edges equal s_5 using XIII.10 (pentagon^2 = hexagon^2 + decagon^2) applied to right-triangle decompositions, (3) all 12 vertices lie on a sphere of diameter AB using XIII.3 and XIII.9, and (4) the side is the irrational line called minor via XIII.11. The constructions are topologically equivalent -- both create two parallel pentagons offset by 36 degrees at distance r apart plus two apex points. The AI proof over-cites definitions (12 items), postulates, and foundational propositions (1.47, 6.17, 6.9, 10.6, 11.8, 11.12, 11.14, 1.11, 4.11) that Heath leaves implicit, while the single heath_only citation (D5.9) is a definition. This is Case A: same backbone, different citation depth.

### 13.17
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q1 found no positively identifiable logical defect: the AI proof's chain from golden-ratio identity (g^2 + sg = s^2 via 6.17/6.30) through direct Pythagorean computation to circumsphere, edge-length, and apotome results is complete, with all algebraic steps verified correct. Q2 identified different backbones (Case B): Heath relies on XIII.4 (triple-square property, used four times for equilateral and circumsphere sub-proofs), XIII.5 (reverse EMR extension), VI.32 (proportional-triangle collinearity for coplanarity), XI.38 (cube-diagonal bisection to locate sphere center), and V.15 (equimultiple ratio for the apotome argument), while the AI instead derives and repeatedly applies the algebraic identity g^2 + sg = s^2, uses XI.2 for coplanarity, directly computes OV^2 from coordinates without XI.38, and invokes X.6 for rationality of the cube side, yielding genuinely different intermediate conclusions at each sub-proof stage. These heath_only propositions are not subsumed by any single AI citation via the containment test; they represent independent sub-arguments replaced wholesale by the AI's algebraic approach. Q3 confirmed the AI's alternative path is logically valid, with all computations checking out and the chain from premises to conclusion unbroken, yielding classification D.

### 13.18
**Category**: Path difference
**Jaccard**: 0.280
**Analysis**: Q2 reveals a different backbone in the latter portion of the proof. Both proofs establish the same key conclusions for the three rational sides (pyramid, octahedron, cube) using 13.13, 13.14, and 13.15, deriving the ratio 4:3:2 for their squares. However, the proofs diverge significantly in how they handle the two irrational sides. Heath constructs explicit geometric segments and proves through a detailed argument using 6.8, 6.4, V.Def.9, and 6.20 that the icosahedron side is greater than the dodecahedron side. The AI instead uses an algebraic species-distinction approach, citing 10.111 to establish that the minor (icosahedron side) and apotome (dodecahedron side) are distinct kinds of irrational lines, but omits the size comparison entirely. The AI also uses different supporting citations throughout (5.8, 5.14, 6.10, CN1-3, D10.1.1, D10.1.2 instead of 6.4, 6.8, 6.20, D5.9, 4.15). This constitutes a genuinely different argumentative path rather than a granularity difference, since the AI's approach to the irrational sides relies on a species-theoretic argument absent from Heath while omitting the geometric magnitude comparison that forms a key part of Heath's backbone. Under Q3, the AI's path is logically valid in what it establishes, so D is appropriate.
