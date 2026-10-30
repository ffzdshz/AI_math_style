# Book 1 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 10 | 1.3, 1.13, 1.16, 1.17, 1.19, 1.25, 1.27, 1.35, 1.36, 1.43 |
| Granularity difference (G) | 38 | 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.14, 1.15, 1.18, 1.20, 1.21, 1.22, 1.23, 1.24, 1.26, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.37, 1.38, 1.39, 1.40, 1.41, 1.42, 1.44, 1.45, 1.46, 1.47, 1.48 |
| Path difference (D) | 0 |  |
| AI proof error (E) | 0 |  |

**Total**: 48 propositions

## Per-Proposition Analysis

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
