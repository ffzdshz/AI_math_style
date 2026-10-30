# Book 1 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 9 | 1.3, 1.16, 1.17, 1.19, 1.25, 1.27, 1.35, 1.36, 1.43 |
| Granularity difference (G) | 38 | 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.18, 1.20, 1.21, 1.22, 1.23, 1.26, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.37, 1.38, 1.39, 1.40, 1.41, 1.42, 1.44, 1.45, 1.46, 1.47, 1.48 |
| Path difference (D) | 1 | 1.24 |
| AI proof error (E) | 0 |  |

**Total**: 48 propositions

## Per-Proposition Analysis

### 1.1
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) AC=AB from the definition of circle center, (2) BC=BA from the same definition, (3) CA=CB via Common Notion 1, and (4) the triangle is equilateral. The only citation difference is that the AI explicitly cites D1.20 (definition of equilateral triangle) when concluding the triangle is equilateral in Step 9, while Heath states the same conclusion without an explicit definition reference. Since D1.20 is a definition and the underlying logical step is present at the same position in both proofs, this is a citation-depth difference (Case A of Q2), yielding Granularity difference. The citation sets are not identical (ai_used contains D1.20 which heath_refs lacks), so Perfect match is ruled out.

### 1.2
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) BC=BG from the circle with center B, (2) DL=DG from the circle with center D, (3) DA=DB from the equilateral triangle, (4) AL=BG by subtraction via CN3, and (5) AL=BC by transitivity via CN1. The only difference is that the AI explicitly cites D1.15 (definition of a circle) to justify that radii of a circle are equal, and D1.20 (definition of equilateral triangle) to justify that sides of the equilateral triangle are equal, whereas Heath invokes these same facts without citing the underlying definitions. Since the backbones are identical and the ai_only items are definitional citations providing additional justification depth for the same logical steps, this is a citation-depth difference classified as G.

### 1.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 1.3 follow the exact same logical backbone: place AD equal to C at point A using I.2, describe circle DEF with center A and distance AD using Postulate 3, conclude AE equals AD by Definition 1.15, and then conclude AE equals C by Common Notion 1 (transitivity). The citation sets are identical (1.2, CN1, D1.15, P3) with Jaccard similarity 1.0, ai_only and heath_only both empty. Since the key intermediate conclusions are the same and the citation sets match exactly, this is a perfect match under the protocol's perfect match check.

### 1.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical superposition method for SAS congruence: place triangle ABC on DEF aligning A with D and AB along DE, show B coincides with E (AB=DE), AC falls along DF (equal angles), C coincides with F (AC=DF), then BC must coincide with EF (two lines cannot enclose a space), so the whole triangles and remaining angles are equal. The key intermediate conclusions are identical in both proofs. The only citation difference is that the AI adds P1 (Postulate 1) in Step 5 when arguing that BC coincides with EF, while Heath does not cite this postulate. Since P1 is an axiom-level citation and the logical backbone is the same, this is a Case A granularity difference — the AI over-cites at the foundational level without changing the argument structure.

### 1.5
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct auxiliary points F and G with AF=AG using I.3, join FC and GB, apply I.4 to triangles AFC/AGB to establish congruence and equal angles, derive BF=CG by subtraction, apply I.4 again to triangles BFC/CGB, then subtract to get the base angles equal, with the under-base angles following directly. The only difference is that the AI explicitly cites CN3 (equals subtracted from equals) for the subtraction steps and CN5 (the whole is greater than the part) to justify that AF is greater than AB, whereas Heath applies these common notions implicitly without citation. Since ai_only contains only common notions (CN3, CN5) and heath_only is empty, and the key intermediate conclusions are identical in both proofs, this is Case A of Q2: same backbone with different citation depth, yielding a granularity difference.

### 1.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume AB > AC for contradiction, cut DB equal to AC on AB, join DC, apply SAS congruence to show triangle DBC equals triangle ACB, then derive a contradiction from the part equaling the whole. The AI proof explicitly cites 1.3 (cutting off a segment), 1.4 (SAS congruence), CN5 (whole greater than part), and P1 (joining two points), while Heath's references field is empty even though his proof text implicitly relies on exactly the same results. Since the key intermediate conclusions are identical and the only difference is that the AI makes explicit citations that Heath leaves implicit, this is Case A of Q2: same backbone, different citation depth, yielding a granularity difference (G).

### 1.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction that joins CD, applies Proposition I.5 twice (once to isosceles triangle ACD and once to isosceles triangle BCD), derives angle inequalities showing an angle is simultaneously greater than and equal to another, and concludes with a contradiction. The AI proof is more granular in two respects: it explicitly cites CN5 (the whole is greater than the part) for the angle inequality steps and P1/P2 for constructions (joining CD, producing lines), whereas Heath uses these implicitly without citation. Additionally, the AI covers two explicit cases (D inside and D outside triangle ACB) while Heath addresses one case directly. The heath_only set is empty, confirming no substantive citations are missing from the AI proof. All ai_only items (CN5, P1, P2) are common notions and postulates representing over-citation at the construction/axiom level, which is the hallmark of a granularity difference.

### 1.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: superposition of triangle ABC onto DEF, coincidence of C with F via equal bases, a reductio ad absurdum argument invoking I.7 to show the sides must coincide, and the conclusion that the contained angles are equal. The only citation difference is that the AI explicitly cites CN4 (Common Notion 4, that things which coincide are equal) when concluding angle equality from coincidence, while Heath leaves this common notion implicit. Since heath_only is empty and ai_only contains only CN4 (an axiom-level item, not a substantive proposition), this is a classic over-citation case representing a difference in citation depth, not in logical structure. Case A of Q2 holds, yielding G.

### 1.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: take D on AB, cut AE equal to AD (I.3), construct equilateral triangle DEF on DE, note DF = EF and AF common, then apply SSS congruence (I.8) to conclude angle DAF = angle EAF. The ai_only set {1.1, D1.20, P1} consists entirely of a construction proposition, a definition, and a postulate that Heath uses implicitly without citation. Heath constructs the equilateral triangle without citing I.1, uses the equal sides without citing D1.20, and joins lines without citing P1. The AI makes these implicit steps explicit. Since heath_only is empty and the key intermediate conclusions are identical in both proofs, this is Case A of Q2: same backbone with different citation depth, yielding a Granularity difference.

### 1.10
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct equilateral triangle ABC on AB (1.1), bisect angle ACB with line CD (1.9), note AC=CB from the equilateral triangle, CD is common, angle ACD = angle BCD, therefore AD=BD by SAS (1.4). The only difference is that the AI explicitly cites D1.20 (definition of equilateral triangle) to justify the step CA=CB, whereas Heath states this fact without citing the definition. Since D1.20 is a definition (not a substantive proposition), this is a classic over-citation pattern representing a citation-depth difference with the same backbone, yielding Case A of Q2 and a Granularity classification.

### 1.11
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: take D on AC, cut CE equal to CD (I.3), construct equilateral triangle on DE (I.1), join FC, then prove triangles DCF and ECF congruent by SSS (I.8) yielding equal adjacent angles DCF and ECF, which are therefore right angles by Definition 1.10. The only citation difference is that the AI explicitly cites Postulate 1 for joining FC, which Heath performs without explicit citation. Since P1 is a construction postulate and the key intermediate conclusions are identical in both proofs, this is a pure citation-depth difference (Case A in Q2), yielding Granularity difference.

### 1.12
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: take point D on the other side of line AB, draw a circle with center C and distance CD intersecting AB at G and E, bisect GE at H, join CG/CH/CE, then use the SSS triangle congruence (I.8) to show angle CHG equals angle CHE, and conclude perpendicularity from adjacent equal angles via Def. 10. The only difference is that the AI explicitly cites D1.15 (the definition of a circle) to justify CG = CE as radii of the same circle, whereas Heath states this fact implicitly from the construction without citing the definition. Since D1.15 is a definition (not a substantive proposition) and the underlying geometric fact is present in both proofs at the same logical position, this is a citation-depth difference under Case A of Q2, yielding G.

### 1.13
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they handle the same two cases (angles equal implies right angles; angles not equal requires constructing a perpendicular via I.11), and in the second case both establish the same key intermediate conclusions in the same order — decomposing angles into parts, adding equals to equals (CN2), and applying transitivity (CN1). The only difference is that the AI explicitly cites CN5 to justify that a whole angle equals the sum of its parts, whereas Heath states this decomposition without citing any axiom. Since ai_only contains only CN5 (a common notion/axiom) and heath_only is empty, this is a straightforward case of over-citation at the axiom level, making it a granularity difference (G).

### 1.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decides the classification. Both proofs share the same logical backbone: assume BD is not in a straight line with BC, let BE be in a straight line with CB, use I.13 to show ABC+ABE equals two right angles, equate this with the given ABC+ABD equals two right angles, subtract ABC to get ABE=ABD, and derive a contradiction since ABE is greater than ABD. The citation differences are entirely at the axiom/postulate level: the AI over-cites by including P2 (for producing the line) and CN5 (for the whole-greater-than-part contradiction), while Heath cites P4 (all right angles are equal) which the AI omits. None of these differences affect the key intermediate conclusions, which are identical in both proofs. The AI's omission of Heath's "similarly" clause for other candidate lines is not a logical gap because the AI's construction uniquely determines E by producing BC. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 1.15
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: apply I.13 twice to establish that two different pairs of supplementary angles each sum to two right angles, equate the sums, then subtract the common angle using CN3 to conclude that the vertical angles are equal. The only citation difference is that Heath explicitly cites Postulate 4 (all right angles are equal) when equating the two sums, while the AI implicitly relies on P4 by directly stating that since both sums equal two right angles they must be equal by CN1. This is a citation-depth difference rather than a backbone difference: the AI uses the same geometric fact but at a coarser granularity, omitting the explicit P4 citation. The AI also explicitly proves the second pair of vertical angles rather than using Heath's "similarly" shorthand, but the key intermediate conclusions remain identical. This is Case A of Q2, yielding G.

### 1.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Q2 confirms that both proofs share the same key intermediate conclusions: bisecting AC at E, constructing EF equal to BE, establishing congruent triangles ABE and CEF via SAS (I.4) using vertical angles (I.15), deducing equal angles BAE and ECF, then applying CN5 to conclude ACD greater than BAC, and handling the second case (ACD greater than ABC) by an analogous argument using vertical angles. The citation sets are identical (Jaccard = 1.0) with no ai_only or heath_only items, and the logical backbones match exactly, yielding a Perfect match.

### 1.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 1.17 follow identical logical backbones: both produce a side of the triangle to create an exterior angle, apply I.16 to establish the exterior angle is greater than each remote interior angle, apply I.13 to note the supplementary angles equal two right angles, and conclude the pair of interior angles sums to less than two right angles. The AI proof is more explicit, proving all three pairs of angles in detail whereas Heath proves one case and handles the others with "similarly," but the key intermediate conclusions and logical structure are the same. The citation sets are identical (1.13, 1.16, P2) with Jaccard 1.0, empty ai_only and heath_only, satisfying the perfect match check: no category was assigned by Q1-Q3, and ai_used equals heath_refs exactly.

### 1.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: cut AD equal to AB on AC (I.3), observe that triangle ABD is isosceles so angle ADB equals angle ABD, note that angle ADB is an exterior angle of triangle BDC and hence greater than angle DCB/BCA (I.16), conclude angle ABD is greater than angle ACB, and therefore angle ABC is greater than angle ACB. The AI's three extra citations (1.5 for the isosceles base angle equality, P1 for joining BD, and CN5 for the whole-greater-than-part inference) each correspond to facts that Heath uses implicitly at the same logical positions. Heath states "angle ADB equals angle ABD since AB equals AD" without citing 1.5, says "let BD be joined" without citing P1, and writes "much greater" without citing CN5. Since every ai_only item represents over-citation of an already-present step rather than a different argumentative path, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 1.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical structures: both use proof by exhaustion of the trichotomy (AC = AB, AC < AB, AC > AB), eliminating the first case via 1.5 (base angles of isosceles triangles are equal, leading to contradiction) and the second case via 1.18 (greater side subtends greater angle, leading to contradiction), concluding AC > AB. The citation sets are exactly equal (both cite 1.5 and 1.18 only), and the key intermediate conclusions are the same in both proofs, satisfying the perfect match check.

### 1.20
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: extend BA to D with DA = AC, apply I.5 to get equal base angles in the isosceles triangle ACD, use CN5 to establish angle BCD > angle ADC, apply I.19 to conclude BD > BC, then derive BA + AC > BC. The only difference is citation depth: the AI explicitly cites P1 (joining DC), P2 (producing BA to D), and 1.3 (cutting off AD equal to AC) for construction steps that Heath performs without explicit citation. Since heath_only is empty and all ai_only items are construction propositions and postulates, this is a pure over-citation granularity difference with the same underlying reasoning.

### 1.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: extend BD to meet AC at point E, apply I.20 twice to establish BA+AC > BE+EC and BE+EC > BD+DC (yielding BA+AC > BD+DC by transitivity), then apply I.16 twice to establish angle BDC > angle CED and angle CEB > angle BAC (yielding angle BDC > angle BAC by transitivity). The key intermediate conclusions match exactly between the two proofs. The only difference is that the AI explicitly cites Postulates P1 and P2 for the construction of extending line BD, which Heath leaves implicit. Since ai_only contains only postulates (P1, P2) and heath_only is empty, this is a clear Case A — same backbone with different citation depth in the construction axioms — resulting in classification G.

### 1.22
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: set out a line and mark off segments equal to the three given lines using I.3, draw two circles centered at the appropriate points, identify their intersection point K, then use the radii equalities (FK=FD=A, GK=GH=C) and the construction (FG=B) to conclude that triangle KFG has sides equal to A, B, C. The AI proof adds an explicit argument for why the two circles must intersect (using the triangle inequality from 1.20) and explicitly cites foundational items (CN1, D1.15, P1, P2, P3) that Heath uses implicitly. Since heath_only is empty and ai_only consists entirely of postulates, definitions, and common notions, this is a clear Case A — same backbone with the AI citing at a finer granularity level than Heath.

### 1.23
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Classification was decided at Q2 (Case A). Both proofs share the same logical backbone: form triangle DCE by taking arbitrary points D, E on lines CD, CE and joining them; construct triangle AFG with sides equal to CD, DE, CE; then apply I.8 (SSS congruence) to conclude angle DCE equals angle FAG. The ai_only citations (1.22 and P1) are construction-level references that Heath leaves implicit — Heath says "let the triangle AFG be constructed" without explicitly naming 1.22, and joins DE without citing Postulate 1. The AI makes these foundational steps explicit. Since the backbone is identical and the citation differences are purely depth-of-citation matters, this is a granularity difference (G).

### 1.24
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same start (BC = EG via I.4) and end (EG > EF via I.19), but their key intermediate conclusions differ fundamentally. Heath uses I.5 (isosceles triangle theorem) to establish that angles DGF and DFG are equal (since DF = DG), then argues through angle ordering. The AI instead uses I.21 (interior point angle theorem) to establish directly that angle DFE > angle DGE, then chains inequalities via CN5 to reach angle EFG > angle EGF. The proof-tree containment test confirms genuine path difference: I.5 (heath_only) does not appear inside Heath's proof of I.21 (the AI's distinctive citation), which relies on I.20 and I.16 instead. Since the AI's different path is logically complete and sound, this is a valid path difference (D).

### 1.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical structures: both use proof by trichotomy, assuming the angle BAC is equal to angle EDF (eliminated via I.4, which would force equal bases, contradicting the hypothesis) and then assuming angle BAC is less than angle EDF (eliminated via I.24, which would force the base BC to be less than EF, again contradicting the hypothesis), leaving the conclusion that angle BAC is greater than angle EDF. The citation sets are identical (1.4 and 1.24), the key intermediate conclusions match exactly, and the Jaccard similarity is 1.0, satisfying the perfect match check.

### 1.26
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for both cases of this multi-case proposition: Case 1 (ASA) uses reductio by constructing a segment equal to the allegedly unequal side, applying I.4 to derive an angle equality that contradicts the part-whole relationship, then applying I.4 for the final conclusion. Case 2 (AAS) similarly uses reductio with I.4 to set up an angle equality, then invokes I.16 (exterior angle theorem) to obtain a contradiction. The AI's Case 2 uses a slightly different geometric configuration (assuming AB unequal to DE and using the exterior angle at G in triangle AGC, versus Heath assuming BC unequal to EF and using the exterior angle at H in triangle AHC), but the key intermediate conclusions and logical tools are identical. The ai_only set consists entirely of construction-level and axiom-level citations (1.3 for cutting off equal segments, P1 for joining points, CN1 for transitivity of equality, CN5 for part-whole) that Heath uses implicitly but does not cite. With heath_only empty, this is a clear Case A same-backbone-different-depth scenario.

### 1.27
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Q2 confirms both proofs share the same logical backbone: assume the lines are not parallel, deduce they meet at a point forming a triangle, apply 1.16 to show the exterior angle exceeds the interior opposite angle, contradicting the hypothesis that alternate angles are equal, then conclude parallelism by D1.23. The AI proof is slightly more explicit about the second case (meeting in the A,C direction) while Heath uses "similarly it can be proved," but the key intermediate conclusions and reasoning structure are identical. Since the citation sets are also exactly equal (both use precisely 1.16 and D1.23, with empty ai_only and heath_only), this meets the criteria for a Perfect match.

### 1.28
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs handle the same two cases of this multi-case proposition and establish the same key intermediate conclusions: in Case 1, both show vertical angles are equal (I.15), derive alternate angle equality by transitivity, and apply I.27 for parallelism; in Case 2, both use I.13 to establish a pair of supplementary angles, equate the two supplementary sums, subtract the common angle to obtain alternate angle equality, and again apply I.27. The only difference is citation depth: the AI explicitly cites CN1 (transitivity of equality) and CN3 (subtraction of equals) where Heath uses these common notions implicitly without citation. Since heath_only is empty and ai_only contains only common notions, this is a pure over-citation pattern characteristic of granularity difference.

### 1.29
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs share identical logical backbones: a proof by contradiction for alternate angles (assuming AGH > GHD, adding BGH to both sides, using I.13 to get two right angles, applying Post. 5 to derive that the parallels would meet, contradicting the hypothesis), then using I.15 and CN1 for the exterior angle result, and CN2 with I.13 for the co-interior angles result. The only citation difference is the AI explicitly citing D1.23 (definition of parallel lines) when concluding that parallel lines do not meet, whereas Heath states this implicitly from the hypothesis. Since D1.23 is a definition (not a substantive proposition) and represents over-citation rather than a different logical path, this is a Case A granularity difference.

### 1.30
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the identical logical backbone: draw a transversal across the three parallel lines, apply I.29 twice to establish that angle AGK equals angle GHF and angle GHF equals angle GKD, then use CN1 to conclude angle AGK equals angle GKD, and finally deduce AB is parallel to CD because the alternate angles are equal. The AI's two extra citations (ai_only = 1.27, P1) represent over-citation rather than a different path: P1 is cited for drawing the transversal line (a construction postulate Heath performs without citing), and 1.27 is cited to explicitly justify the final step where equal alternate angles imply parallelism, which Heath invokes implicitly by saying "they are alternate, therefore AB is parallel to CD." Since heath_only is empty and all key intermediate conclusions match, this is Case A of Q2 — same backbone, different citation depth.

### 1.31
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: take a point D on BC, join AD, construct angle DAE equal to angle ADC using I.23, produce the line through A, then conclude parallelism via I.27 because the alternate angles are equal. The key intermediate conclusions are the same in both proofs. The only difference is that the AI explicitly cites postulates P1 (for joining the line AD) and P2 (for producing EA to F), which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only construction postulates, this is a clear Case A — same backbone with different citation depth — yielding a Granularity difference.

### 1.32
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing CE parallel to AB via I.31, establishing angle BAC = angle ACE and angle ECD = angle ABC via I.29, combining to show the exterior angle ACD equals the two interior opposite angles, adding angle ACB to both sides, applying I.13 to get that ACD + ACB = two right angles, and concluding the three interior angles equal two right angles. The only difference is citation depth: the AI explicitly cites CN1 (for the final equality substitution), CN2 (for combining and adding angles), and P2 (for producing the side BC to D), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only common notions and a postulate, this is a clear Case A same-backbone, different-depth scenario warranting G.

### 1.33
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: join diagonal BC, use I.29 for alternate angles ABC and BCD, apply I.4 (SAS) to establish triangle congruence yielding AC = BD and the alternate angle equality ACB = CBD, then invoke I.27 to conclude AC is parallel to BD. The only citation difference is that the AI explicitly cites Postulate 1 for the construction of line BC, which Heath performs without explicit citation. Since ai_only contains only a construction postulate (P1) and heath_only is empty, this is a straightforward case of over-citation at the construction level with no difference in the argumentative backbone, making this a granularity difference.

### 1.34
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same backbone: (1) use I.29 for alternate angles, (2) apply I.26 (ASA) to prove triangle congruence and derive opposite sides equal, (3) combine angles via CN2 to show one pair of opposite angles equal, (4) establish the second pair of opposite angles equal, and (5) conclude the diameter bisects from triangle equality. The heath_only citation I.4 is used by Heath to re-prove triangle equality for the bisection claim via SAS, while the AI reuses the triangle equality already established by I.26; since I.4 appears inside Heath's own proof of I.26, the proof-tree containment test confirms this is a citation-depth difference. The ai_only citations CN1 and CN3 are common notions used by the AI in an explicit algebraic step (co-interior angles) to show the second pair of opposite angles equal, where Heath instead extracts this directly from the remaining angle equality given by I.26. The key intermediate conclusions are identical in both proofs — only the granularity of citation and the level of detail in intermediate algebraic steps differ.

### 1.35
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof establish the same key intermediate conclusions in the same order: AD = EF via both equaling BC (I.34, CN1), AE = DF by adding the common segment DE (CN2), triangle EAB congruent to triangle FDC by SAS (I.4, using I.29 for the angle and I.34 for the sides), subtracting the common triangle DGE to get equal trapezia (CN3), and adding the common triangle GBC to reach the final equality of the parallelograms (CN2). The citation sets are identical -- both use exactly {1.29, 1.34, 1.4, CN1, CN2, CN3} -- yielding a Jaccard similarity of 1.000 with empty ai_only and heath_only sets. Since both the logical backbone and the citation sets match perfectly, this is classified as P (Perfect match).

### 1.36
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The classification is decided at the perfect-match check. Both proofs follow the same logical backbone: they construct parallelogram EBCH by joining BE and CH, establish BC = EH via transitivity (CN1), use 1.33 to show EBCH is a parallelogram, apply 1.35 twice to show ABCD = EBCH and EFGH = EBCH, and conclude ABCD = EFGH by CN1. The citation sets are identical (ai_used = heath_refs = {1.33, 1.34, 1.35, CN1}), with ai_only and heath_only both empty and Jaccard = 1.0, confirming a perfect match in both reasoning structure and citation depth.

### 1.37
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing parallelograms EBCA and DBCF via I.31, proving their equality via I.35, showing each triangle is half its respective parallelogram via I.34, and concluding the triangles are equal as halves of equal things. The AI's two extra citations (D1.22 for the definition of parallelogram and CN3 for "halves of equal things are equal") are purely foundational references that Heath leaves implicit — Heath brackets the CN3 statement and does not label it, and does not cite the definition when establishing the parallelograms. Since the backbone is the same and the ai_only items consist only of a definition and a common notion representing over-citation of foundational justifications, this is Case A (same backbone, different citation depth), yielding G.

### 1.38
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: construct parallelograms GBCA and DEFH (or HEFD) around the triangles using I.31, establish equality of the parallelograms via I.36 (equal bases, same parallels), show each triangle is half its parallelogram via I.34, and conclude the triangles are equal because halves of equal things are equal. The only citation difference is that the AI explicitly cites CN3 for the final inference ("halves of equal things are equal to one another"), while Heath uses this principle implicitly, marking it with brackets in the text. Since heath_only is empty and ai_only contains only CN3 (a common notion), this is a straightforward over-citation of an axiom that Heath chose not to formally reference, making this Case A of Q2: same backbone, different citation depth.

### 1.39
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: a proof by contradiction where AD is assumed not parallel to BC, AE is drawn parallel to BC via 1.31, triangle ABC is shown equal to triangle EBC via 1.37, and since ABC equals DBC by hypothesis, DBC equals EBC by CN1, contradicting that DBC is greater than EBC. The ai_only citations (P1 and CN5) are a postulate for joining lines and a common notion for "the whole is greater than the part," both of which Heath uses implicitly without explicit citation. Since the key intermediate conclusions are identical and the citation difference consists only of axiom-level over-citation by the AI, this is Case A of Q2: same backbone, different citation depth, yielding a Granularity difference.

### 1.40
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G. Both proofs use identical proof-by-contradiction structures: assume AD is not parallel to BE, construct AF parallel to BE, show triangle ABC equals triangle FCE (via 1.38), derive that DCE equals FCE (via CN1 and the hypothesis), reach a contradiction because one triangle is part of the other, and conclude AD is parallel to BE. The key intermediate conclusions are the same in both proofs. The ai_only items (CN5 and P1) are over-citations of foundational axioms: P1 is cited for the construction of joining a line (which Heath performs without citation), and CN5 ("the whole is greater than the part") makes explicit what Heath states informally as "the greater to the less: which is impossible." Heath_only is empty. This is Case A of Q2 — same backbone, different citation depth — yielding G.

### 1.41
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) the diagonal of the parallelogram bisects it, making the parallelogram double of one of the resulting triangles (I.34), and (2) that triangle equals the given triangle by having the same base and being in the same parallels (I.37). The AI proof presents these steps in reverse order compared to Heath but reaches the same key intermediate conclusions. The ai_only citations (CN1, CN2, P1) are all axiom-level or construction-level items that the AI made explicit while Heath left them implicit: P1 for drawing the diagonal, CN2 for the doubling argument, and CN1 for substituting equals. Since heath_only is empty and ai_only contains only common notions and a postulate, this is a clear Case A same-backbone-different-depth scenario, yielding G.

### 1.42
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: bisect BC at E, construct angle CEF equal to D, draw parallels to form parallelogram FECG, show triangles ABE and AEC are equal (via I.38), conclude triangle ABC is double triangle AEC, show parallelogram FECG is also double triangle AEC (via I.41), and conclude equality. The AI proof cites 1.10 for bisection, P1 for joining a line, CN1 for the final equality step, and CN2 for the doubling step, none of which Heath explicitly cites. These are all over-citations of construction operations and common notions that Heath treats as implicit. Since heath_only is empty and all ai_only items are foundational construction/axiomatic references, this is a clear Case A: same backbone with the AI providing greater citation depth at the foundational level.

### 1.43
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: both use I.34 three times to establish that the diameter bisects each of the three parallelograms (ABCD, AEKH, KGCF), yielding the triangle equalities ABC=ACD, AEK=AHK, and KGC=KFC. Both then apply CN2 to add the smaller triangle pairs and CN3 to subtract equals from equals, concluding that the complements are equal. The citation sets are identical (1.34, CN2, CN3) with Jaccard 1.0, and the key intermediate conclusions match exactly in both content and logical position, satisfying the perfect match criteria.

### 1.44
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct parallelogram BEFG equal to triangle C with the required angle via I.42, establish that AH is parallel to EF, show that HB and FE must meet at K by Post. 5, form the larger parallelogram HLKF, invoke I.43 to equate the complements LB and BF, and conclude LB equals triangle C via CN1. The angle equality (ABM = D) is established identically in conclusion but by different citation depth: Heath invokes I.15 (vertical angles) directly, while the AI derives the same result via I.13 (supplementary angles), showing both ABM and GBE are supplements of ABG and therefore equal. The ai_only items (1.13, 1.14, 1.30, 1.34, CN5, P1, P2) are all either explicit construction citations (P1, P2), parallelogram property citations (1.34), transitivity of parallels (1.30), collinearity (1.14), or the supplementary-angle alternative to vertical angles (1.13, CN5). The heath_only item (1.15) is replaced by the AI's equivalent but more verbose supplementary-angle argument. Since both proofs reach the same key intermediate conclusions with the AI simply providing more granular justification, this is a granularity difference.

### 1.45
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decides this classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) construct parallelogram FGHK equal to triangle ABD via I.42, (2) apply parallelogram GHLM equal to triangle DBC via I.44, (3) show KHM is a straight line via I.14, (4) show FGL is a straight line via I.14, (5) establish KFLM is a parallelogram, and (6) conclude KFLM equals ABCD. The citation differences are purely at the depth level: Heath explicitly cites I.34 to extract that opposite sides of a parallelogram are equal and parallel, and I.33 to conclude that lines joining equal and parallel lines are themselves equal and parallel, while the AI uses the parallelism properties of the component parallelograms directly without naming those propositions. Conversely, the AI explicitly cites I.13 (supplementary angles on a straight line) and P1 (drawing a line) where Heath leaves these implicit or uses alternate routes (I.29 plus CN1/CN2). The underlying geometric reasoning is the same in both proofs; only the granularity of citation differs.

### 1.46
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing a parallelogram ADEB by drawing a perpendicular and equal segment then parallels, proving all four sides equal via I.34, proving all angles right via I.29 and I.34, and concluding ADEB is a square. The AI proof cites the same core propositions (1.11, 1.29, 1.31, 1.34) as Heath but additionally cites 1.3 for cutting off the equal segment, CN1 and CN3 for the transitivity and subtraction inferences Heath performs implicitly, D1.22 for the definition of a square, and P1 as a postulate. All five ai_only items are construction props, common notions, definitions, or postulates representing finer-grained citations of the same logical steps, and heath_only is empty. This is a clear Case A: same backbone, different citation depth, yielding G.

### 1.47
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone for the Pythagorean theorem: construct squares on all three sides, draw AL parallel to BD/CE, prove triangle ABD equals triangle FBC (and similarly triangle ACE equals triangle BCK) via I.4, then use I.41 to show each sub-rectangle of the large square equals the corresponding smaller square. The AI proof explicitly works through the "similarly" part that Heath abbreviates, and over-cites foundational items: 1.31 for drawing the parallel line, P1 for joining lines, P4 for right angles being equal, and CN1 for the principle that doubles of equals are equal. Heath uses all these principles implicitly but does not assign them formal citation numbers. The heath_only set is empty, confirming no missing steps in the AI proof. All ai_only items (1.31, CN1, P1, P4) are construction propositions, postulates, or common notions representing over-citation of foundational steps, which is the hallmark of a granularity difference.

### 1.48
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct AD perpendicular to AC and equal to BA, join DC, show DA^2 = AB^2, add AC^2 to both sides, apply 1.47 to get DC^2 = DA^2 + AC^2, use the hypothesis BC^2 = BA^2 + AC^2 to conclude DC = BC, then apply SSS (1.8) to conclude angle DAC = angle BAC, and since DAC is right, BAC is right. The ai_only set consists entirely of construction propositions (1.11 for the perpendicular, 1.3 for equal segment), a postulate (P1 for joining DC), and common notions (CN1, CN2 for equality reasoning) — all steps that Heath performs implicitly but the AI cites explicitly. The heath_only set is empty, confirming the AI covers all of Heath's references. This is Case A: same backbone, different citation depth, yielding G.
