# Euclid Proof Classification Report — RunA

Classification of all 465 AI-generated proofs against Heath's reference proofs, into four categories: **Perfect match (P)**, **Granularity difference (G)**, **Path difference (D)**, and **AI proof error (E)**. P denotes identical citation sets and a complete proof; G denotes the same proof strategy with differences confined to citation granularity (over-citing construction primitives or definitions, inlining or expanding sub-lemmas); D denotes a genuinely different valid route to the same conclusion (typically the AI's algebraic or arithmetic manipulation in place of Heath's geometric proposition chain); E denotes a positively identifiable logical defect in the AI proof.

## Overall Summary

| Category | Count | Share |
|---|---|---|
| P — Perfect match | 22 | 4.7% |
| G — Granularity difference | 317 | 68.2% |
| D — Path difference | 120 | 25.8% |
| E — AI proof error | 6 | 1.3% |
| **Total** | **465** | **100.0%** |

## Per-Book Distribution

| Book | P | G | D | E | n | Mean Jaccard |
|---|---|---|---|---|---|---|
| 1 | 9 | 38 | 1 | 0 | 48 | 0.623 |
| 2 | 0 | 5 | 9 | 0 | 14 | 0.162 |
| 3 | 0 | 30 | 6 | 1 | 37 | 0.279 |
| 4 | 0 | 14 | 2 | 0 | 16 | 0.318 |
| 5 | 5 | 12 | 8 | 0 | 25 | 0.423 |
| 6 | 0 | 25 | 8 | 0 | 33 | 0.385 |
| 7 | 1 | 31 | 6 | 1 | 39 | 0.317 |
| 8 | 2 | 16 | 9 | 0 | 27 | 0.432 |
| 9 | 3 | 15 | 16 | 2 | 36 | 0.340 |
| 10 | 0 | 89 | 25 | 1 | 115 | 0.371 |
| 11 | 2 | 28 | 8 | 1 | 39 | 0.374 |
| 12 | 0 | 10 | 8 | 0 | 18 | 0.295 |
| 13 | 0 | 4 | 14 | 0 | 18 | 0.212 |
| **All** | **22** | **317** | **120** | **6** | **465** | **0.373** |

## Error Detail (E Classifications)

| Proposition | Error type | Violated claim |
|---|---|---|
| 3.26 | Unsupported assertion | "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF" (Step 6) |
| 7.33 | Invalid inference | "E and F are prime to one another (from Step 7, any common measure of E and F would also measure G, giving a common measure of all three greater than one, which was shown imposs... |
| 9.9 | Missing case | The cube case: 'if the number after the unit be cube, all the rest will also be cube' |
| 9.10 | Invalid inference | "by 8.25, A is also square" (Step 3, and repeated in Steps 4-5) |
| 10.12 | Invalid inference | A:B :: pm:nq (Step 8) |
| 11.31 | Invalid inference | In Step 5, the AI applies 11.29/11.30 (which require solids on 'the same base') to solids AB (on base FGHK) and RS (on base FGPQ), which are on different (though equal) bases sh... |

---

## Per-Proposition Analysis (All Books)


## Book 1

| Category | Count |
|---|---|
| Perfect match (P) | 9 |
| Granularity difference (G) | 38 |
| Path difference (D) | 1 |
| AI proof error (E) | 0 |

**Total**: 48 propositions

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


## Book 2

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 5 |
| Path difference (D) | 9 |
| AI proof error (E) | 0 |

**Total**: 14 propositions

### 2.1
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow identical key intermediate conclusions: constructing rectangle BGHC with BG equal to A, identifying sub-rectangles BGKD, DKLE, and ELHC as the rectangles contained by A and each segment (BD, DE, EC) using I.34 to show the relevant sides equal A, and concluding that the whole rectangle equals the sum of the sub-rectangles. The AI proof adds three citations not in Heath (1.29, CN2, D2.1) that make explicit what Heath leaves implicit: 1.29 justifies that DK is perpendicular to BC since it is parallel to BG, CN2 justifies that the whole equals the sum of parts, and D2.1 names the definition of a rectangle. Heath cites nothing the AI omits (heath_only is empty). Since both proofs share the same logical backbone with the AI simply citing at a finer granularity, this is a granularity difference (G).

### 2.2
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Classification was decided at Q2/Q3. Heath proves 2.2 by constructing a square ADEB on AB (I.46), drawing a parallel CF through C (I.31), then decomposing the square geometrically into two rectangles AF and CE, identifying them as rect(BA,AC) and rect(AB,BC) respectively. The AI takes a fundamentally different approach: it applies Proposition 2.1 to the special case where both straight lines equal AB, with one copy cut at C, directly obtaining rect(AB,AB) = rect(AB,AC) + rect(AB,CB), then identifies rect(AB,AB) with sq(AB) via Definitions D2.1 and D1.22, and substitutes via CN1. The key intermediate conclusions differ entirely: Heath's backbone is geometric area decomposition of a constructed square via parallel lines, while the AI's backbone is an algebraic specialization of the general distributive-like result 2.1. Since the AI's different path is logically complete and valid -- 2.1 legitimately applies to the case where both lines are AB, the definitional identification is sound, and the substitution is valid -- this is a path difference (D).

### 2.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs a geometric figure (square CDEB on CB via I.46, parallel line AF via I.31) and decomposes the resulting rectangle into sub-areas to establish the identity. The AI instead applies Proposition 2.1 directly as an algebraic identity — treating BC as the uncut line and AB as the line cut into segments AC and CB — then recognizes that rect(BC, CB) equals sq(BC) by definition of a square. These represent fundamentally different logical backbones: Heath uses geometric construction and area decomposition, while the AI uses a previously proved distributive-law proposition and definitional substitution. The proof-tree containment test confirms this is not merely a citation-depth difference, since I.46 (used by Heath to construct the square) does not appear inside Heath's proof of 2.1 (the AI's key citation). The AI's different path is logically valid — 2.1 is correctly applied, the definitional identification of rect(BC,CB) with sq(BC) is sound, and the substitution completes the proof — yielding classification D.

### 2.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs the square on AB, draws the diagonal and parallels, then identifies sub-squares (on AC and CB) and complementary rectangles within the figure using Book 1 propositions (1.29, 1.31, 1.34, 1.46, 1.5, 1.6). The AI proof takes a fundamentally different algebraic route: it applies Proposition 2.2 to decompose sq(AB) into rect(AB,AC) + rect(AB,CB), then applies Proposition 2.3 twice to expand each rectangle term, and collects terms using Common Notions. The Jaccard similarity is 0.0 with completely disjoint citation sets, reflecting genuinely different logical backbones rather than mere depth differences. The AI's path is logically complete and valid -- 2.2 and 2.3 are both prior results, correctly applied, and the algebraic substitution and collection steps are sound.

### 2.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof uses a geometric construction approach: building a square on CB, drawing parallels (I.31), using complement equality (I.43), equal parallelograms on equal bases (I.36), and square construction (I.46) to establish the result through area relationships of constructed figures including the gnomon NOP. The AI proof takes a fundamentally different algebraic path, decomposing rectangles and squares using Book II identities: 2.3 decomposes rect(CB,DB), 2.1 decomposes rect(AD,DB), and 2.4 expands sq(CB), then substitution yields the result. The key intermediate conclusions are entirely different -- Heath argues through geometric complements and gnomons while the AI argues through algebraic rectangle/square decompositions. The zero Jaccard similarity (0.0) reflects this complete divergence in approach. The AI proof is logically complete under Q1 and Q3: each step validly applies its cited proposition, and the chain from premises to conclusion is sound. This is Case B (different backbone) with a valid alternative path, yielding classification D.

### 2.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses a geometric construction approach: building a square on CD, drawing parallels (I.31), then using properties of equal parallelograms (I.36) and complements (I.43) to establish area equalities through gnomons. The AI proof takes a completely different algebraic path, decomposing rect(AD,BD) via Proposition 2.3, expanding rect(AB,BD) via 2.1 with the bisection condition AC=CB, and then recognizing the result as sq(CD) via 2.4. The two proofs share no citations (Jaccard=0.0) and their key intermediate conclusions are entirely different: Heath argues through parallelogram complements and gnomon areas, while the AI argues through algebraic rectangle decomposition using earlier Book 2 results. This is a genuine backbone difference (Case B). The AI's algebraic chain is logically complete and valid under Q3, so the classification is D.

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses a geometric construction approach: building a square ADEB on AB, using I.43 (complements about the diagonal are equal) and I.46 (constructing squares), then working with gnomons and area decompositions to reach the conclusion. The AI proof takes a fundamentally different algebraic path: it applies Proposition 2.4 to expand sq(AB), adds sq(BC) to both sides, then uses Proposition 2.3 to express rect(AB,BC), doubles the result, adds sq(AC), and establishes equality of the two sides by observing identical right-hand sides (CN1). The key intermediate conclusions are entirely different -- Heath works with geometric regions (gnomon KLM, square CF, complements AG and GE) while the AI works with algebraic identities from 2.3 and 2.4. The proof-tree containment test confirms this is not merely a citation-depth difference: while 1.46 appears inside the proofs of 2.3 and 2.4, the critical citation 1.43 does not, and more importantly, the overall proof strategy (algebraic manipulation vs. geometric area decomposition) is genuinely different. The AI's algebraic chain is logically complete and sound, so this is a valid different path (D).

### 2.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works by constructing a square on AD and dissecting it into component rectangles, using I.36 (parallelograms on equal bases are equal) and I.43 (complements about the diameter are equal) to show that eight sub-areas forming a gnomon are quadruple of the rectangle AB,BD, then adding the square on AC. The AI proof takes an entirely different algebraic route: it applies Proposition 2.4 to the line AD cut at B to express sq(AD) in terms of sq(AB), sq(BD), and 2*rect(AB,BD), then applies Proposition 2.7 to the line AB cut at C to replace sq(AB)+sq(CB) with 2*rect(AB,CB)+sq(AC), and combines these via substitution to obtain sq(AD) = 4*rect(AB,CB)+sq(AC). The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are fundamentally different: Heath reasons about geometric area decomposition of a square figure, while the AI chains two prior algebraic identities. Both paths are logically complete, so this is a valid path difference (D).

### 2.9
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: angles of half a right angle in isosceles right triangles ACE and ECB, angle AEB is right, EG equals GF equals CD via isosceles triangle EGF, DF equals DB, and the same sequence of Pythagorean theorem applications (I.47) to derive that the squares on AD and DB are double the squares on AC and CD. The AI takes a slightly different sub-route to show DF=DB (using parallelogram algebra rather than Heath's angle-based I.6 argument), but this is a minor variation in establishing the same intermediate conclusion, not a different backbone. Heath_only is empty, and all ai_only items (1.11, 1.13, 1.3, 1.31, 1.5, CN1, CN2, CN3, P1) are construction propositions, basic postulates, common notions, or elementary results that Heath leaves implicit, confirming this is over-citation at a finer granularity rather than a path difference.

### 2.10
**Category**: Path difference
**Jaccard**: 0.059
**Analysis**: The classification is decided at Q2/Q3. Heath's proof is entirely geometric/synthetic: it constructs auxiliary perpendiculars and parallels, establishes three right isosceles triangles through angle-chasing (using I.5, I.32, I.29, I.15, I.6, I.34), then applies the Pythagorean theorem (I.47) repeatedly to derive the result. The AI proof takes a completely different algebraic path, applying earlier Book 2 propositions (2.7 to decompose sq(AD)+sq(BD), 2.6 to express rect(AD,BD) in terms of sq(CD) and sq(CB), and 2.4 to expand sq(AB)) and then performing algebraic substitution to reach the conclusion. The key intermediate conclusions are entirely disjoint: Heath argues through isosceles triangle properties and Pythagorean decompositions of auxiliary right triangles, while the AI argues through rectangle-square algebraic identities. The Jaccard similarity of 0.059 reflects this near-total divergence, with only CN1 shared. The AI proof is logically complete and sound under the hardened Q1(b) standard, so Q3 yields D.

### 2.11
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Both proofs share the same construction and the same first major intermediate conclusion: rect(CF, FA) = sq(AB), established via II.6 and I.47 with area subtraction. However, the proofs diverge in how they bridge from this result to the final conclusion rect(AB, BH) = sq(AH). Heath uses direct geometric area identification in the diagram (FK = AD, subtract AK to get FH = HD, then identify HD as rect(AB,BH) and FH as sq(AH)). The AI instead takes an algebraic route, applying Proposition 2.3 to decompose rect(CF,FA) into rect(CA,FA) + sq(FA), substituting CA = AB and FA = AH to get rect(AB,AH) + sq(AH) = sq(AB), then using Proposition 2.2 to establish rect(AB,AH) + rect(AB,HB) = sq(AB), and equating to conclude sq(AH) = rect(AB,HB). The AI's use of 2.2 and 2.3 as substantive intermediate steps constitutes a genuinely different backbone for the second half of the proof, making this a path difference rather than a granularity difference. Q2 Case B applies, and Q3 confirms the AI's alternative path is logically valid and complete.

### 2.12
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: apply II.4 to the line formed by extending a side through the obtuse angle vertex, add a square to both sides, then apply I.47 twice to right triangles formed by the perpendicular to substitute and obtain the final result. The AI uses a different vertex labeling (obtuse angle at B rather than Heath's A) but the geometric argument is structurally identical. The ai_only citations (1.12 for constructing the perpendicular and CN2 for adding equals to both sides) are construction and axiom over-citations that Heath leaves implicit, confirming a citation-depth difference rather than a path difference. The heath_only set is empty, so no substantive propositions are missing from the AI proof.

### 2.13
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: drop a perpendicular AD from A to BC, apply II.7 to the line BC cut at D, use I.47 (Pythagorean theorem) on both right triangles ABD and ACD, then combine the results to show that sq(AC) = sq(AB) + sq(BC) - 2*rect(BC, BD). The key intermediate conclusions are identical. The AI's extra citations (1.12 for the perpendicular construction, CN1 and CN3 for algebraic manipulation, D1.12 and D1.21 for definitions) are all construction, common notion, or definition-level items that Heath uses implicitly. Heath cites nothing that the AI omits (heath_only is empty). This is a clear case of same backbone with different citation depth, yielding Granularity difference (G).

### 2.14
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G. Both proofs follow identical logical backbones: construct a rectangular parallelogram equal to the given figure (I.45), handle the trivial case where the sides are equal, then for the non-trivial case produce a side and bisect it, draw a semicircle, apply II.5 to establish that BE*EF + GE^2 = GF^2, substitute GH for GF as radii are equal, apply I.47 to the right triangle GEH, subtract GE^2 to get BE*EF = EH^2, and conclude the square on EH equals the given figure. The AI proof cites all three Heath references (1.45, 1.47, 2.5) plus twelve additional items that are all construction propositions (1.3, 1.10, 1.46), postulates (P1, P2, P3), common notions (CN1, CN3), and definitions (D1.15, D1.17, D1.22, D2.1). Heath leaves these implicit while the AI makes them explicit. With heath_only empty and ai_only consisting entirely of sub-step-level citations, this is a clear Case A same-backbone, different-depth classification.


## Book 3

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 30 |
| Path difference (D) | 6 |
| AI proof error (E) | 1 |

**Total**: 37 propositions

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
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: draw the diameter of the given circle, handle the trivial case where the given line equals the diameter, then for the non-trivial case construct a segment equal to the given line on the diameter, draw a circle with that segment as radius, find the intersection with the given circle, and use the definition of a circle plus transitivity of equality to conclude the fitted chord equals the given line. Heath's reference list is empty (no explicit citations), while the AI explicitly cites definitions (D1.15, D1.17, D4.7), postulates (P1, P3), a common notion (CN1), and Proposition 1.3 for cutting off a segment. All of these are foundational references that Heath leaves implicit. Since the key intermediate conclusions are identical and the only differences are in citation depth, this is a granularity difference (G).

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a tangent to the circle at a point, construct two angles at the tangent point equal to two angles of the given triangle, join the resulting chord, apply the alternate segment theorem (III.32) twice to transfer the tangent-chord angles to inscribed angles, and then use the angle-sum property (I.32) to establish equality of the remaining pair of angles. The AI proof swaps which tangent angle corresponds to which triangle angle compared to Heath, but the key intermediate conclusions are identical. The ai_only set consists entirely of common notions (CN1, CN3), a definition (D4.3), and a postulate (P1) — none are substantive propositions. Heath uses these implicitly without citing them. This is a classic Case A same-backbone, different-citation-depth scenario, yielding G.

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decides the classification. Both proofs share the same logical backbone: construct center K, build angles BKA = DEG and BKC = DFH, draw tangents at A, B, C, establish right angles at tangent points, use quadrilateral angle sums to show corresponding angles of the circumscribed triangle equal those of DEF, and conclude with I.32 for the remaining angle. The ai_only citations (D4.4, P1, P2) are a definition and postulates representing over-citation of basic constructions. The heath_only citation (3.18) covers the fact that tangent-radius angles are right, but the AI establishes this same fact directly from its construction: the tangent lines were explicitly drawn perpendicular to the radii in Step 5 (using 3.16 to confirm they are tangents), so the right angles follow from construction rather than requiring a separate invocation of 3.18. The underlying geometric fact is present at the same logical position in both proofs. This is Case A of Q2: same backbone, different citation depth.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: bisect two angles of the triangle to locate center D (I.9), drop perpendiculars from D to the three sides, prove DE=DF and DF=DG via triangle congruence (I.26), conclude all three distances are equal so a circle centered at D passes through E, F, G, show the circle touches the sides rather than cutting them (III.16), and invoke the definition of inscribed circle (IV.Def.5). The AI's three extra citations (ai_only: 1.12, CN1, P3) are all construction-level or axiomatic: I.12 for drawing perpendiculars, CN1 for the transitivity step equating all three distances, and P3 for describing the circle. Heath uses these same steps implicitly without explicit citation. Since heath_only is empty, there is no missing substantive content in the AI proof. The identical backbone with over-citation of construction and axiom steps is a textbook granularity difference.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two sides of the triangle, erect perpendicular bisectors, find their intersection point F, then use SAS congruence (I.4) to show FA = FB and FB = FC (or CF = AF), concluding all three distances are equal so a circle centered at F passes through all three vertices. Both proofs cover all three cases (F inside, on a side, outside the triangle). The AI bisects AB and BC while Heath bisects AB and AC, but this is merely a different choice of which two sides to bisect and does not change the logical backbone. The ai_only set consists entirely of over-citations: construction propositions (1.11 for erecting perpendiculars), postulates (P1 for joining lines, P3 for describing circles), common notions (CN1 for transitivity of equality), and definitions (D1.10, D4.6) that Heath uses implicitly without explicit citation. The heath_only set is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided this classification. Both proofs establish the same two key intermediate conclusions: (1) the quadrilateral ABCD is equilateral, proved via I.4 (SAS triangle congruences using radii and right angles at the center), and (2) the quadrilateral ABCD is right-angled, proved via III.31 (angle in a semicircle is right). Both then conclude ABCD is a square by I.Def.22. The AI proof simply reverses the order (right angles first, then equilateral) and provides more explicit foundational citations. The ai_only set consists entirely of definitions (D1.15, D1.17, D4.3), postulates (P1, P2, P4), a common notion (CN1), and one construction proposition (1.11) -- all representing over-citation of steps Heath leaves implicit. The heath_only set is empty. This is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.188
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct tangent lines at the endpoints of two perpendicular diameters, show opposite sides are parallel (forming a parallelogram), prove the figure is equilateral via radii equality and parallelogram properties, prove it is right-angled, and conclude it is a circumscribed square. The heath_only citations (3.18 and 1.30) reflect different granularity rather than a different path: Heath uses 3.18 to derive perpendicularity from tangency, while the AI reverses the order by constructing perpendiculars first (1.11) and then deducing tangency (3.16), arriving at the same intermediate fact. Heath uses 1.30 for transitivity of parallelism, while the AI establishes each pair of parallel sides directly from 1.28. The ai_only citations are predominantly definitions (D1.10, D1.15, D1.17, D1.22, D4.4), common notions (CN1, CN2), postulates (P1), and construction or supplementary propositions (1.11, 1.29, 1.32) that represent over-citation of foundational items. The identical backbone with differing citation depth places this squarely in Case A of Q2, yielding a granularity difference.

### 4.8
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: bisect sides of the square to find midpoints, establish parallelograms to show four equal segments from center to midpoints of sides, construct a circle through those four points, and prove tangency via III.16. The sole heath_only citation (1.31, drawing a parallel through a point) reflects Heath's construction method of explicitly drawing parallels through midpoints, while the AI achieves the same geometric configuration by bisecting all four sides, joining opposite midpoints with P1, and proving those joins are parallel via I.33 and I.29. The ai_only set is dominated by over-citation of definitions (D1.15, D1.22, D4.5), common notions (CN1, CN3), and postulates (P1, P3), with the substantive additions 1.29 and 1.33 serving as the AI's alternative to Heath's 1.31. Since the key intermediate conclusions are identical and only the construction depth and citation granularity differ, this is a granularity difference.

### 4.9
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof establishes that the diagonals bisect the angles of the square (using I.8 on triangles formed by equal sides and a common diagonal), then infers equal half-angles at adjacent vertices to conclude EA=EB by I.6. The AI takes a fundamentally different route: it first proves opposite sides are parallel (I.28), derives equal alternate angles with the diagonals as transversals (I.29), applies ASA congruence (I.26) to opposite triangles AEB and CED to get AE=CE and BE=DE, then uses SSS congruence (I.8) on adjacent triangles AEB and AED, derives right angles at E via I.13 and the angle sum theorem I.32, and finally shows angle EAB = angle ABE to conclude AE=BE by I.6. The key intermediate conclusions differ: Heath's backbone runs through angle bisection of the square's corners, while the AI's backbone runs through parallelism of sides and ASA congruence of diagonally opposite triangles. Since the AI's different path is logically complete and valid, Q3 confirms classification as D.

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.583
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) AB*BC = BD^2 from the construction and BD=AC, (2) BD is tangent to circle ACD via III.37, (3) angle BDC = angle DAC via III.32, (4) angle BDA = angle BCD via angle addition with I.32 and I.5, (5) BD = DC via I.6, (6) CA = CD so angle CDA = angle DAC via I.5, and (7) each base angle is double the vertex angle. The ai_only set consists entirely of construction propositions (4.1), definitions (D1.15, D1.20), and postulates (P1, P3) that the AI cites explicitly for steps Heath leaves implicit or uncited in the reference set. Since the logical backbone is the same and the citation differences reflect only over-citation of construction and foundational items, this is a granularity difference (G).

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: construct the isosceles triangle FGH via IV.10, inscribe an equiangular triangle ACD via IV.2, bisect angles ACD and CDA via I.9 to obtain five equal angles, apply III.26 (equal inscribed angles stand on equal arcs) and III.29 (equal arcs subtend equal chords) to prove the pentagon equilateral, then combine arcs and apply III.27 (equal arcs subtend equal inscribed angles) to prove it equiangular. The AI proof adds four over-citations not in Heath: P1 (postulate for joining lines), CN2 (common notion for adding equals to equals), D4.3 (definition of polygon inscribed in circle), and 1.32 (angle-sum theorem, listed in USED but never actually invoked in the proof steps). Heath uses the same underlying operations without explicitly citing these basic axioms and definitions. Since heath_only is empty and the ai_only items are all postulates, common notions, definitions, or phantom citations, this is a pure citation-depth difference with no backbone divergence, yielding category G.

### 4.12
**Category**: Granularity difference
**Jaccard**: 0.389
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: inscribe a regular pentagon (4.11), draw tangents at each vertex (3.16), establish perpendicularity of radii to tangent lines (3.18), use triangle congruence (1.8, 1.26) and the Pythagorean theorem (1.47) to show tangent segments from adjacent vertices are equal, deduce equilateral by doubling equal segments, and deduce equiangular through congruent triangles. The AI's ai_only citations are predominantly over-citations: definitions (D1.15, D1.16, D4.4), common notions (CN1, CN2, CN3), and a postulate (P1) that Heath leaves implicit, plus substantive but depth-level additions (3.26 as an explicit bridge to 3.27, 1.32 for angle-sum reasoning Heath leaves implicit, 1.4 for SAS congruence where Heath uses different but equivalent congruence results). The sole heath_only item, 3.1 (finding the center), is a construction step that the AI replaces with the definitional citation D1.16. All key intermediate conclusions are present in both proofs at the same logical positions, making this a citation-depth difference rather than a path difference.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two angles of the equilateral equiangular pentagon to locate the incenter F, prove that the remaining three angles are also bisected by lines from F (using I.4 and the equilateral/equiangular properties), drop perpendiculars from F to all five sides, prove all perpendiculars equal via I.26, describe the inscribed circle, and verify tangency via III.16. The AI proof is more explicit, citing construction tools (1.9 for angle bisection, 1.12 for dropping perpendiculars), postulates (P1, P3, P4), common notions (CN1, CN3), and definitions (D3.2, D4.5) that Heath leaves implicit. Heath's citation set is a proper subset of the AI's, and all ai_only items are foundational over-citations rather than substantive propositions indicating a different path. This is a clear Case A granularity difference.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same backbone: bisect angles BCD and CDE to find point F, show F is equidistant from all five vertices, then circumscribe the circle. Heath compresses the equidistance argument with 'similarly it can be proved' and 'in manner similar to the preceding,' citing only I.6. The AI spells out each equidistance step explicitly using SAS congruence (I.4) applied to multiple triangle pairs, plus construction citations (I.9, P1, P3), common notions (CN1, CN3), and a definition (D4.6). The ai_only set consists entirely of construction propositions, postulates, common notions, a definition, and I.4 used to expand what Heath leaves as 'similarly' arguments. The heath_only set is empty. The key intermediate conclusions are identical in both proofs; only the citation depth differs.

### 4.15
**Category**: Path difference
**Jaccard**: 0.308
**Analysis**: Q2 determined the classification. Both proofs reach the same final conclusions (equilateral and equiangular hexagon via six equal central angles, equal arcs, equal chords, and equal inscribed angles), but they follow genuinely different logical backbones to establish the six equal central angles. Heath constructs one auxiliary circle (centered at D), uses I.5 and I.32 to show three adjacent central angles are each one-third of two right angles, then uses I.15 (vertical angles) to obtain the remaining three. The AI constructs two auxiliary circles (centered at D and at A), creating four equilateral triangles that directly yield four of the six central angles, then computes the remaining two angles by subtraction using I.13 (supplementary angles) and CN3. The different construction (two circles vs. one) and different method for the remaining angles (supplementary angle subtraction vs. vertical angles) constitute a different path. The AI's reasoning chain is logically complete and sound throughout, so this is a valid path difference.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical backbone: inscribe an equilateral triangle side AC and regular pentagon side AB in the circle, deduce that arc BC is two-fifteenths of the circumference, bisect BC at E using 3.30 to get one-fifteenth arcs, then fit equal chords contiguously around the circle to produce the 15-gon. The key intermediate conclusions are the same in both proofs. The only difference is citation depth: Heath cites only 3.30 and leaves implicit the constructions (4.2, 4.11, 4.1), the arc-chord relationships (3.28, 3.29), the angle equality (3.27), the definition of inscription (D4.3), and the postulate for joining points (P1). The AI explicitly cites all of these. Since heath_only is empty and all ai_only items are explicit citations of steps Heath performs implicitly, this is a classic over-citation granularity difference.


## Book 5

| Category | Count |
|---|---|
| Perfect match (P) | 5 |
| Granularity difference (G) | 12 |
| Path difference (D) | 8 |
| AI proof error (E) | 0 |

**Total**: 25 propositions

### 5.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). The forward dependency gate passed since all AI citations (CN3, D5.1, D5.2) are definitions and common notions, which are never forward. Q1 found no logical errors: the AI proof is logically complete, establishing each step from premises through decomposition into unit parts, pairwise subtraction via CN3, to the conclusion that the remainder is the same equimultiple. The AI proof and Heath's proof share the same structural backbone of decomposing equimultiples into unit-sized parts and pairing corresponding parts, though the operations applied to pairs differ to match their respective conclusions. Heath's reference has zero citations, while the AI adds only axiom-level items (CN3, D5.1, D5.2), which are all common notions and definitions rather than substantive propositions. Per the protocol, ai_only consisting entirely of common notions and definitions indicates over-citation, which is a hallmark of granularity difference. With heath_only empty, there are no missing substantive steps to investigate. The citation difference is purely one of depth, not of logical path.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) the first magnitude contains the same number of equal parts as the third in their respective units, (2) the fifth magnitude contains the same number of equal parts as the sixth, and (3) the sums therefore contain the same total number of parts in their respective units. The AI makes the multipliers explicit (m and n) and explicitly cites D5.2 (definition of equimultiple) and CN2 (addition of equals), while Heath uses the same reasoning implicitly without formal citations. Heath's recorded citation set is empty, so ai_only consists entirely of a definition and a common notion, which are not substantive propositions. This is a classic over-citation pattern where the AI cites foundational definitions and axioms that Heath treats as understood. The backbones are identical, confirming Case A of Q2.

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: divide EF into n parts equal to A and GH into n parts equal to C, observe that each part of EF is the same multiple of B as the corresponding part of GH is of D (since A is the same multiple of B as C is of D), then apply Proposition 5.2 to sum the parts and conclude EF is the same multiple of B as GH is of D. The only citation difference is that the AI explicitly cites Definition 5.2 (the definition of equimultiple) which Heath uses implicitly without citation. Since the backbones are identical and the sole ai_only item is a definition (over-citation), this is a granularity difference (G).

### 5.4
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both proofs follow identical logical structure: set up equimultiples of the first/third and second/fourth magnitudes, take arbitrary equimultiples of those, use Proposition 5.3 to combine the iterated multiples into single multiples of the original magnitudes, apply Definition 5.5 (the definition of same ratio) to the hypothesis to get the excess/equal/less condition, then apply Definition 5.5 again to conclude the desired ratio. The citation sets are exactly the same (5.3 and D5.5), the key intermediate conclusions match, and the Jaccard similarity is 1.0. Since no category was assigned by Q1-Q3 and ai_used equals heath_refs exactly, this is a perfect match.

### 5.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof introduces an auxiliary magnitude CG, constructs EB as the same multiple of CG, then uses proposition 5.1 (equimultiple composition) to establish GF = CD, subtracts CF to get GC = FD, and substitutes back. The AI proof takes a fundamentally different path: it works directly from Definition 5.2, decomposing AB and AE into m individual copies of CD and CF respectively, computing pairwise remainders FD_i = CD - CF = FD using CN3, and summing to get EB = m times FD. The key intermediate conclusions differ — Heath's backbone pivots on the auxiliary construction and the equality GF = CD via 5.1, while the AI's backbone pivots on pairwise decomposition and direct summation from the definition. Since the backbones are different (Case B in Q2), Q3 was applied: the AI's chain from definitions and CN3 to the conclusion is logically complete and sound, yielding a valid different path (D).

### 5.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses an additive strategy: it constructs CK equal to F, then applies 5.2 (addition of equimultiples) to show AB is the same multiple of E that KH is of F, deduces KH equals CD, and subtracts to get KC equals HD equals F. The AI proof uses a subtractive strategy: it directly applies 5.1 (subtraction of equimultiples) to conclude that the remainder GB is the same multiple of E that the remainder HD is of F, then splits into cases based on whether the multiplier difference is 1 or greater. These are genuinely different logical backbones with different key intermediate conclusions and different core citations (5.2 for Heath vs 5.1 for the AI). The proof-tree containment test confirms 5.2 does not appear inside Heath's proof of 5.1, so this is not a citation-depth difference but a true path divergence. The AI's path is logically valid and complete, so the classification is D.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same two-part backbone: first proving A:C = B:C by showing that equimultiples of equal magnitudes are equal and then applying the definition of same ratio (D5.5), then proving C:A = C:B by the symmetric argument. The only difference is that the AI explicitly cites CN2 (Common Notion 2: if equals be added to equals, the wholes are equal) to justify the step that equal multiples of equal magnitudes yield equal results, whereas Heath treats this as self-evident from A = B. Since CN2 is an axiom-level citation and heath_only is empty, this is a straightforward case of the AI providing greater axiomatic granularity for the same logical backbone, yielding a Granularity difference (G).

### 5.8
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) finding equimultiples m of A,B and n of C such that mA > nC while mB does not exceed nC, using Proposition 5.1 to handle multiples of sums, and (2) applying Definition 5.7 to conclude both parts of the theorem (A:C > B:C and C:B > C:A). The AI's construction differs in style — decomposing A = B + E directly and avoiding Heath's two-case structure — but the backbone logical conclusions are identical. The only citation difference is CN5 (Common Notion 5), which the AI cites to justify the existence of the excess E = A - B, a fact Heath treats as obvious. This is a standard over-citation of a basic axiom, indicating a granularity difference rather than a path difference.

### 5.9
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath prove this two-part proposition by identical logical strategies: for each part, assume A is not equal to B, then invoke Proposition 5.8 to derive a contradiction with the hypothesis of equal ratios, concluding A = B. The AI is more explicit in showing both subcases (A > B and B > A) separately for each part, while Heath compresses the contradiction argument, but the key intermediate conclusions are the same in both proofs. The citation sets are identical (both cite only 5.8), with ai_only and heath_only both empty and Jaccard similarity of 1.0. Since the backbone and citations match exactly, this is a perfect match (P).

### 5.10
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 5.10 follow identical logical structures with identical citation sets. Both proofs address the two parts of the proposition (Part 1: if A:C > B:C then A > B; Part 2: if C:B > C:A then B < A) using proof by contradiction in each part, eliminating the equality case via Proposition 5.7 and the wrong inequality case via Proposition 5.8. The key intermediate conclusions are the same in both proofs: in each part, the equality hypothesis is refuted by 5.7 and the wrong inequality hypothesis is refuted by 5.8, leaving the desired conclusion by exhaustion of cases. Since the citation sets are identical (ai_used = heath_refs = {5.7, 5.8}, Jaccard = 1.0) and the logical backbones match exactly, this is a perfect match.

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: they take equimultiples of A, C, E with one multiplier and of B, D, F with another, then chain the definition-of-proportion comparisons through C:D as the common middle ratio to conclude A:B :: E:F. The only citation difference is that the AI explicitly cites D5.5 (the equimultiple definition of same ratio) while Heath uses it implicitly without citation. Since D5.5 is a definition and not a substantive proposition, and both proofs argue through the same logical backbone at the same key steps, this is a same-backbone, different-citation-depth situation (Case A of Q2), yielding G.

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) using V.1 to show that equimultiples of individual magnitudes combine to give equimultiples of their sums, (2) using D5.5 to extract the three-way comparison (greater, equal, less) from the proportionality hypothesis, (3) adding term-by-term inequalities/equalities to obtain the sum comparison, and (4) applying D5.5 to conclude the final proportion. The logical backbone is identical despite a slight reordering of steps. The AI explicitly cites CN2 and CN5 to justify adding inequalities term by term, a step Heath performs implicitly without citing common notions. Since ai_only contains only common notions (CN2, CN5) and heath_only is empty, this is a clear case of over-citation at the axiom level — same backbone, different citation depth.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof share identical citation sets (D5.5, D5.7) and argue through the same key intermediate conclusions. Both proofs (1) invoke D5.7 to obtain equimultiples m, n such that mC > nD but mE is not greater than nF, (2) construct corresponding equimultiples of A and B, (3) apply D5.5 (definition of same ratio for A:B = C:D) to deduce mA > nB from mC > nD, and (4) apply D5.7 again to conclude A:B > E:F. Since the backbone is identical and the citation sets match exactly (Jaccard = 1.0, with empty ai_only and heath_only), the classification is P (Perfect match).

### 5.14
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Heath proves Case 1 (A > C implies B > D) directly: he establishes A:B > C:B via 5.8, transfers the greater-ratio relation to C:D > C:B via 5.13 (transitivity of greater ratios), then concludes D < B via 5.10. The AI instead uses proof by contradiction for Cases 1 and 3, assuming the negation and eliminating subcases (B = D and B < D) using 5.7, 5.9, 5.11, and 5.8/5.10. This is a fundamentally different logical backbone: Heath's is direct while the AI's is indirect, and they rely on different key propositions (Heath uses 5.13 which the AI does not cite; the AI uses 5.7, 5.9, 5.11 which Heath does not cite). The AI also provides explicit detailed proofs for all three cases whereas Heath only proves Case 1 in detail and dismisses Cases 2 and 3 as similar. The AI proof is logically complete and valid throughout, establishing a sound alternative path to the same conclusion.

### 5.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof decomposes the multiples AB and DE into equal parts, applies 5.7 (equal magnitudes have the same ratio) to establish that each pair of corresponding parts has the same ratio, then applies 5.12 (proportional antecedents sum with proportional consequents) to conclude the whole multiples have the same ratio as the parts. The AI proof takes a fundamentally different approach: it works directly from the definition of proportion (D5.5), showing the equimultiple test condition holds by using 5.3 to rearrange nested multiples and 5.1 to show that multiplying preserves order. The key intermediate conclusions are entirely different — Heath's backbone is structural decomposition plus summing of proportionals, while the AI's backbone is algebraic manipulation of multiples plus order-preservation under multiplication. Both proofs are logically complete, but they argue through different intermediate steps, yielding a path difference.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided this classification. Both proofs follow the same logical backbone: take equimultiples of A,B and of C,D; use V.15 to express the ratio of equimultiples as equal to the ratio of the originals; use V.11 for transitivity to link the equimultiples; apply V.14 to establish the ordering relationship; and conclude by V. Def. 5 that A:C :: B:D. The AI proof's only extra citation is D5.12 (definition of alternate ratio), which is a definitional over-citation rather than a substantive divergence. Since the key intermediate conclusions are identical and the only difference is the AI citing an additional definition, this is a granularity difference (Case A of Q2).

### 5.17
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification as D (path difference). Heath's proof constructs four sets of equimultiples (of AE, EB, CF, FD and separate equimultiples of EB, FD), uses 5.1 to relate equimultiples of the parts to equimultiples of the wholes (AB, CD), uses 5.2 to combine equimultiples of the same magnitude, applies the componendo hypothesis, then subtracts to derive the separando result. The AI proof takes a structurally different route: it starts with arbitrary equimultiples m of AB, CD and n of EB, FD (the separando magnitudes), uses 5.1 to decompose m*AE = m*AB + m*EB, then cleverly selects equimultiples m of AE, CF and (m+n) of EB, FD from the componendo hypothesis, and algebraically simplifies the comparison to obtain the separando condition directly. The AI avoids 5.2 entirely by choosing the equimultiple (m+n) so that subtraction of m*EB cancels immediately. These represent genuinely different logical backbones: Heath builds up from parts to wholes then subtracts back, while the AI decomposes wholes into parts and matches equimultiples. The AI's path is logically valid and complete, yielding a sound alternative proof.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as D (Path difference). Heath proves 5.18 by reductio ad absurdum: he assumes the componendo proportion fails, applies the converse 5.17 (separando from componendo) to the assumed ratio, then uses 5.11 (transitivity) and 5.14 (ordering from equal ratios) to derive a contradiction. The AI takes a completely different approach, proving the result directly from the definition of proportion (D5.5): it takes arbitrary equimultiples m and n, uses 5.1 and 5.2 to manipulate multiples of sums, and verifies the trichotomy condition of D5.5 across all three cases (m*AB > n*BE, m*AB = n*BE, m*AB < n*BE). The citation sets are entirely disjoint (Jaccard = 0.0), reflecting genuinely different logical backbones rather than mere granularity differences. The AI proof is logically complete and valid throughout, establishing a sound direct proof where Heath used an indirect one.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 5.19 follow the identical logical chain: starting from the given proportion AB:CD = AE:CF, both apply alternation (5.16) to rearrange it, then use separando (5.17) to obtain ratios involving the remainders, then apply alternation (5.16) again to relate the remainders to each other, and finally invoke transitivity of equal ratios (5.11) to reach the conclusion EB:FD = AB:CD. The citation sets are identical ({5.11, 5.16, 5.17}) with Jaccard similarity 1.0, and no ai_only or heath_only items exist. Since the key intermediate conclusions match and the citation sets are the same, the classification is P (Perfect match).

### 5.20
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone for the primary case (A > C): they establish A:B > C:B via 5.8, transfer the ratio inequality to the D,E,F magnitudes via 5.13, and conclude D > F via 5.10. Heath handles the A = C and A < C cases with 'similarly we can prove,' while the AI explicitly works through all three cases, adding citations 5.7, 5.9, and 5.11 for the equal and less-than cases. The AI also cites definitions D5.5 and D5.7 to spell out equimultiple reasoning that Heath leaves implicit. Since heath_only is empty (nothing in Heath is missing from the AI) and the ai_only items represent either explicit treatment of cases Heath abbreviates or definition-level detail Heath leaves implicit, this is a citation-depth difference with the same backbone, yielding G.

### 5.21
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone for the primary case (A > C): A > C implies A:B > C:B by 5.8, then E:F > E:D by 5.13 (using the given ratio A:B = E:F and the inverse C:B = E:D), then F < D by 5.10. The AI proof is more granular in two ways: (1) it explicitly proves all three cases (A > C, A = C, A < C) where Heath abbreviates Cases 2 and 3 as 'Similarly we can prove,' introducing citations 5.7, 5.9, and 5.11 for those cases; and (2) it explicitly derives the inverse ratio C:B = E:D using definitions D5.5 and D5.13, and cites D5.17 and D5.18 for the perturbed proportion setup, where Heath uses these implicitly. Heath's citation set {5.8, 5.10, 5.13} is a proper subset of the AI's set, and heath_only is empty, confirming that all divergence is due to the AI's greater explicitness rather than a different proof path.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs establish the same key intermediate conclusions for the core three-magnitude case: taking equimultiples of the magnitudes, applying V.4 twice to obtain proportionality of the equimultiples, invoking V.20 for the trichotomy comparison, and concluding via V. Def. 5. The AI proof adds an explicit induction argument (Steps 9-12) to extend the result to any number of magnitudes, which Heath leaves implicit by only proving the three-magnitude case. The sole citation difference is D5.17 (the definition of ex aequali ratio) which the AI cites explicitly while Heath does not list it as a formal reference. Since the backbones are the same and the only differences are citation depth (an extra definition citation) and the AI's additional explicit induction layer, this is a granularity difference rather than a path difference.

### 5.23
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Both proofs establish the same key intermediate conclusions before applying 5.21: (1) G:H :: M:N and (2) H:L :: K:M, where G,H,K are equimultiples of A,B,D and L,M,N are equimultiples of C,E,F. The difference lies in how H:L :: K:M is derived. Heath uses a multi-step chain involving 5.16 (alternation), 5.15 (equimultiples preserve ratios), and 5.11 (transitivity) applied repeatedly to pass through intermediate ratios B:D :: C:E, H:K :: B:D, H:K :: C:E, L:M :: C:E, H:K :: L:M, and then alternation again to get H:L :: K:M. The AI instead applies 5.4 directly to B:C :: D:E to obtain mB:nC :: mD:nE, i.e., H:L :: K:M in one step. Since both proofs arrive at the same backbone of key intermediate conclusions and differ only in the propositions used to derive one of those intermediates, this is a granularity difference (Q2 Case A). The ai_only items D5.17, D5.18, and D5.5 are definitions (overcitation), and 5.4 replaces Heath's multi-step 5.16-based derivation to reach the same intermediate result.

### 5.24
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 reveals fundamentally different proof backbones, leading to classification D at Q3. Heath's proof operates at a high algebraic level: he inverts BG:C = EH:F, applies ex aequali (5.22) twice, and uses componendo (5.18) to move from separando to componendo form, obtaining AG:C = DH:F in four steps. The AI instead returns to the equimultiple definition of proportion (D5.5) and proves the result from first principles: it distributes multiples over sums (D5.2), applies 5.4 to transfer the given ratios to equimultiples, then conducts a three-case analysis on the relative sizes of mA and mE versus nB. The hardest case (C) requires alternando (5.16), the remainder proposition (5.19), and transitivity of ratios (5.11) to show that mE vs the excess P tracks mF vs the excess Q. The completely disjoint citation sets (Jaccard 0.0) confirm the structural divergence. The AI's path is logically complete: every step is justified by a cited proposition or definition, and the case analysis exhaustively covers all possibilities, so Q3(b) holds and the classification is D.

### 5.25
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs use 5.19 as a key step, but their overall logical backbones differ substantially. Heath constructs auxiliary points AG=E and CH=F, then applies 5.19 directly to the original proportion to get a remainder-to-remainder relationship, and concludes via a simple additive inequality argument. The AI instead uses alternando (5.16) to transform the proportion, applies 5.14 to establish B > D, then applies 5.19 to get (A-C):(B-D) :: A:B, performs another alternando, and uses a case-by-case elimination argument with 5.14 to show A-C > B-D, finally concluding via CN5. The key intermediate conclusions are different: Heath's backbone centers on constructed equal segments and direct addition of unequals to equals, while the AI's backbone centers on alternando transformations and case analysis via 5.14. Since the AI's different path is logically complete with every step properly justified, this is a valid path difference (D).


## Book 6

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 25 |
| Path difference (D) | 8 |
| AI proof error (E) | 0 |

**Total**: 33 propositions

### 6.1
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing equimultiples of the bases by extending the line, joining the vertex to new points, using I.38 to show triangles on equal bases are equal, applying V.Def.5 to establish BC:CD = triangle ABC:triangle ACD, then using I.41 to relate parallelograms to triangles and chaining the ratios. The ai_only citations (1.3, CN5, P1, P2) are all construction propositions, postulates, and common notions representing over-citation of construction steps that Heath leaves implicit. The heath_only citation (5.11, transitivity of ratios) represents a step that is logically present in both proofs at the same position: the AI actually mentions 5.11 in its Step 12 text but does not formally list it, instead handling the ratio-chaining through 5.15 and D5.5. Since the key intermediate conclusions are identical and the citation differences reflect depth of citation rather than different logical paths, this is a granularity difference.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs establish the same key intermediate conclusions in both parts of this biconditional proposition: (1) triangles BDE and CDE are equal by I.38, (2) triangle-to-segment ratios via VI.1, (3) ratio equality via V.7, and (4) transitivity via V.11 for the forward direction; and symmetrically for the converse using VI.1, V.11, V.9, and I.39. The only citation difference is that the AI explicitly cites Postulate 1 for joining lines BE and CD, which Heath uses implicitly without citation. Since P1 is a construction postulate and the logical backbone is identical, this is a classic granularity (citation-depth) difference, not a path difference.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided this classification. Both proofs (AI and Heath) establish identical key intermediate conclusions in both directions of this biconditional proposition: in Part I, both construct CE parallel to DA, establish angle equalities via I.29, deduce AE = AC via I.6, then apply VI.2 to get the proportionality; in Part II, both use VI.2, V.11, V.9 to deduce AE = AC, then I.5 and I.29 to establish the angle bisection. The AI's additional citations (1.31, 5.7, CN1, P2, P5) are all over-citations of construction steps, postulates, and common notions that Heath uses implicitly without explicit citation. Since heath_only is empty and ai_only consists entirely of construction/axiom-level references, this is a clear Case A: same backbone, different citation depth.

### 6.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical geometric backbone: placing BC in line with CE, producing BA and ED to meet at F, establishing BF parallel to CD and AC parallel to FE (both via 1.28), forming parallelogram ACDF with AF=CD and AC=FD (via 1.34), and applying 6.2 twice to triangle BFE to extract the base proportions BA:AF=BC:CE and BC:CE=FD:DE. The only divergence is in the final proportion-manipulation stage: Heath uses alternando (5.16) to rearrange ratios and ex aequali (5.22) to derive the third pair BA:AC=CD:DE, while the AI uses transitivity of ratios (5.11) to show BA:CD=BC:CE=AC:DE directly. The ai_only items 1.13 and P2 are over-citations of construction steps that Heath leaves implicit. Since the key intermediate geometric conclusions are the same in both proofs and only the algebraic manipulation technique for the final proportions differs, this is a granularity/depth difference (Case A of Q2), not a path difference.

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical backbone: construct an auxiliary triangle equiangular with ABC (Heath on EF, AI on DE), prove proportionality of sides via VI.4, deduce side equalities via V.9, establish congruence with DEF via I.8, and transfer angle equalities back to conclude ABC is equiangular with DEF. The citation differences are purely depth-related: the AI cites CN1 for ratio transitivity where Heath cites V.11, and the AI attributes all angle equalities from congruence directly to I.8 where Heath explicitly invokes I.4 after I.8 to obtain remaining angle equalities. These are citation-depth differences on the same logical backbone, not different proof paths.

### 6.6
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decides the classification. Heath's proof constructs a triangle DGF equiangular to ABC on line DF using I.23, derives via VI.4 that BA:AC = GD:DF, combines with the hypothesis via V.11 to get ED:DF = GD:DF, concludes ED = GD by V.9, then applies I.4 (SAS) to prove DEF congruent to DGF and thereby transfers the angles. The AI proof takes a fundamentally different approach: it constructs points G on DE and H on DF with DG = AB and DH = AC (using I.3), then through a chain of ratio manipulations (5.7, 5.11, 5.16, 5.17) shows the sides DE and DF are cut proportionally at G and H, invokes the converse of 6.2 to establish GH parallel to EF, uses 1.29 for alternate angle equalities, and applies I.4 (SAS) to show triangle ABC congruent to DGH rather than to a separate equiangular construction. The key intermediate conclusions differ: Heath's backbone runs through equiangularity of a constructed triangle and equality of segments (V.9), while the AI's runs through proportional side-cutting, parallelism (6.2), and alternate angles (1.29). Both paths are logically complete and valid, but they establish different intermediate geometric facts, constituting a genuine path difference.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.875
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume angle ABC is not equal to angle DEF, construct an auxiliary triangle equiangular with one given triangle (Heath at point B, AI at point E), derive segment equality via proportionality (VI.4, V.11, V.9), establish an isosceles triangle (I.5), then derive contradictions in both cases (angles less than a right angle, angles not less than a right angle). The only citation difference is that Heath cites I.17 (any two angles of a triangle are less than two right angles) for the Case 2 contradiction, while the AI derives the equivalent result from I.32 (angle sum equals two right angles) by showing that if two angles account for two right angles the third angle would be zero, which is impossible. This is a citation-depth difference: the AI derives inline what Heath cites as a ready-made theorem. The key intermediate conclusions are identical, placing this firmly in Case A of Q2 as a granularity difference.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both the AI and Heath proofs follow the same logical backbone: they establish equiangularity of each sub-triangle (ABD and ACD) with the whole triangle ABC by noting that two angles are equal (one right angle and one common angle) and deducing the third angle equality via I.32 (angle sum), then apply VI.4 for proportionality and VI.Def.1 for similarity, and finally prove the two sub-triangles similar to each other by combining previously established angle equalities. The ai_only set consists entirely of axioms, definitions, and postulates (CN3, D1.10, D1.21, P4) that Heath invokes implicitly but the AI cites explicitly. The heath_only set is empty. This is a pure citation-depth difference with no backbone divergence, confirming Case A of Q2.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct three equal segments along an auxiliary line from one endpoint, draw a parallel through the first division point to the line joining the last division point to the other endpoint, and apply VI.2 to establish a proportion that yields the prescribed 1/n part. The AI proof cites 5.18 (componendo) to formally derive AG:AB = 1:3 from AD1:D1D3 = AG:GB, whereas Heath performs the equivalent ratio reasoning informally without citing a specific proposition. The remaining ai_only items (D5.1, D5.2, D5.5, P1) are definitions and a postulate that Heath leaves implicit. Heath_only is empty. Since the key intermediate conclusions are identical and the citation differences reflect only depth of explicit reference, this is a granularity difference (G).

### 6.10
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification as D (path difference). Heath's proof constructs a line through D parallel to AB, creating parallelograms FH and HB, then uses I.34 (opposite sides of a parallelogram are equal) to establish segment equalities DH=FG and HK=GB, followed by two applications of VI.2 to triangles DKC and AGE. The AI proof takes a fundamentally different geometric approach: it draws DF and EG both parallel to BC (rather than creating a parallelogram), establishes DF parallel to EG via I.30, then applies VI.2 three times (to triangle ABC twice and to triangle AEG), and uses ratio-theoretic machinery from Book 5 (5.18 componendo and 5.22 ex aequali) to derive the required proportions. The AI avoids parallelogram construction entirely, substituting ratio algebra for geometric segment equality. Since the key intermediate conclusions differ -- Heath works through parallelogram side equalities while the AI works through a chain of three proportion applications combined with Book 5 ratio operations -- this is Case B (different backbone). The AI's path is logically valid at Q3, with each step properly justified, so the classification is D.

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: place lines BA, AC at any angle, produce them, set BD equal to AC via I.3, join BC and draw DE parallel to BC via I.31, apply VI.2 to obtain AB:BD = AC:CE, then substitute AC for BD to conclude AB:AC = AC:CE. The AI's extra citations (P1, P2 for construction lines, CN1 for equals substitution, and 5.7 for the formal justification of replacing BD with AC in the proportion) are all over-citations that make explicit what Heath leaves implicit. Heath's proof performs the same substitution step without citing any supporting proposition. Since the key intermediate conclusions are identical and the citation differences reflect only depth of justification, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct triangle DEF with DG=A, GE=B, DH=C, draw EF parallel to GH via I.31, apply VI.2 to obtain DG:GE::DH:HF, then substitute equals to conclude A:B::C:HF. The AI proof cites three additional items (1.3, P1, P2) that Heath leaves implicit, all of which are construction propositions or postulates justifying the explicit construction steps (cutting off equal segments, drawing and joining lines, extending lines). Since heath_only is empty and ai_only consists entirely of construction-level over-citations, the proofs share the same key intermediate conclusions at different citation depths, yielding a granularity difference.

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: they construct a semicircle on AC, draw BD perpendicular to the diameter, and establish two key intermediate conclusions in the same order: (1) angle ADC is a right angle by III.31, and (2) DB is a mean proportional between AB and BC by VI.8. The AI proof cites the same core propositions as Heath (3.31 and 6.8) but additionally cites postulates P1, P2, P3 for construction steps, definitions D1.17 and D1.18 for the semicircle, definition D6.1 for similarity, and proposition 1.11 for the perpendicular construction. These are all foundational items that Heath leaves implicit, representing over-citation rather than a different proof strategy. Heath_only is empty, confirming no substantive steps are missing. This is Case A of Q2: same backbone, different citation depth.

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decides: both proofs follow the same backbone. They place the equal and equiangular parallelograms with equal angles adjacent, complete a third reference parallelogram (Heath calls it FE, the AI constructs BCHF), then use VI.1 to express area ratios as side ratios, V.7 to exploit the equality of the original parallelograms, V.11 for transitivity, and V.9 for the converse direction. The AI's four extra citations (1.13, 1.30, 1.31, 5.16) all make explicit construction or algebraic steps that Heath leaves implicit: 1.31 for constructing the reference parallelogram, 1.13 and 1.30 for establishing collinearity of sides, and 5.16 for alternation of the proportion. Since heath_only is empty and the ai_only items are all over-citations of construction and supplementary steps with no change to the logical backbone, this is Case A of Q2, a granularity difference.

### 6.15
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. The AI proof uses a different auxiliary construction from Heath: it joins BE to create intermediate triangle ABE, whereas Heath joins BD to create intermediate triangle BAD. This leads to different key intermediate conclusions: the AI establishes ratios ABC:ABE = CA:AE and ABE:ADE = BA:AD via VI.1, then uses alternando (V.16) to rearrange to the desired reciprocal proportion CA:AD = AE:BA, while Heath establishes CAB:BAD = CA:AD and EAD:BAD = EA:AB via VI.1, obtaining the result directly through transitivity of ratios (V.11). The different auxiliary line produces genuinely different intermediate geometric facts, not merely a difference in citation depth. The AI's path is logically valid throughout both directions of the biconditional, correctly applying V.16 where Heath uses V.11, and V.7/V.9 as Heath does. This constitutes a genuine path difference (D).

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: construct two equiangular parallelograms (rectangles) representing the rectangles of the extremes and means, establish that the sides about the equal angles are reciprocally proportional, and apply 6.14 to conclude equality of the parallelograms (and hence the rectangles). The converse direction is handled identically in both proofs by reversing the application of 6.14. The ai_only set consists entirely of construction propositions (1.3, 1.11, 1.31), postulates (P1, P4), and a definition (D2.1) that Heath uses implicitly but does not cite. The heath_only set is empty. This is a classic case of the AI over-citing foundational construction steps that Heath leaves tacit, with no difference in the logical backbone.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: converting the three-line proportion into a four-line proportion context and applying 6.16 in both the forward and converse directions. Heath introduces an explicit auxiliary line D equal to B to set up the four-line proportion, while the AI directly observes that A, B, B, C constitute four proportional lines without needing an auxiliary construction. The key intermediate conclusions are identical in both proofs. The ai_only set consists entirely of definitions (D1.22, D2.1, D5.6, D5.8) that the AI cites explicitly where Heath leaves them implicit, and heath_only is empty. This is a classic Case A same-backbone-different-depth scenario.

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the identical backbone: decompose the given rectilineal figure into triangles by joining diagonals, construct equiangular counterpart triangles on the given line using I.23, show remaining angles equal by I.32, establish proportional sides by VI.4, chain the proportional ratios to show all corresponding sides are in the same ratio, show all corresponding angles equal by construction and addition, and conclude similarity by VI. Def. 1. The AI proof generalizes to a pentagon while Heath uses a quadrilateral, but the method is the same iterative triangle-matching procedure. The ai_only citations (5.11, CN2, P1) are all over-citations of basic infrastructure: 5.11 for ratio transitivity that Heath uses implicitly when chaining proportions, CN2 for adding angles that Heath performs without naming the common notion, and P1 for joining diagonals. The heath_only set is empty, confirming that every substantive citation in Heath also appears in the AI proof. This is Case A of Q2: same backbone, different citation depth.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing a third proportional BG to BC and EF via 6.11, establishing that AB:DE = EF:BG via transitivity (5.11), proving triangle ABG equals triangle DEF via reciprocally proportional sides about equal angles (6.15), using 6.1 to relate triangle ABC : triangle ABG to the base ratio BC:BG, and concluding that triangle ABC has to triangle DEF the duplicate ratio of BC:EF via D5.9. The citation differences are purely granularity: the AI cites 6.4 (equiangular triangles have proportional sides) to obtain AB:DE = BC:EF directly, whereas Heath derives this same proportion by applying 5.16 (alternation) to the given ratio AB:BC = DE:EF. The proof-tree containment test confirms that 5.16 appears inside Heath's proof of 6.4, so the AI is citing at a higher level while Heath re-derives the internals inline. The AI also explicitly cites 5.7 (equal magnitudes have the same ratio) for the substitution of equal triangles ABG and DEF, which Heath performs without explicit citation, and cites D6.1 (definition of similar figures) where Heath cites D5.11 (definition of corresponding magnitudes). These are all citation-depth differences with identical key intermediate conclusions.

### 6.20
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs establish that similar polygons decompose into similar triangles in the same ratio, but they use genuinely different logical backbones. Heath triangulates from vertex E (diagonals BE, EC) and establishes the ratio part through an elaborate sub-triangle argument using I.32 (angle sums), VI.1 (triangles as their bases), and VI.4 (equiangular triangles have proportional sides), constructing additional diagonals AC and FH to create intermediate points M and N. The AI triangulates from vertex A (diagonals AC, AD) and takes a more direct path for the ratio argument: it applies 6.19 directly to each pair of similar triangles to obtain duplicate ratios, observes these duplicate ratios are all equal because the polygon side ratios are equal, and sums them via 5.12. The heath_only citations (1.32, 6.1, 6.4) are not subsumed by any AI-cited proposition — they reflect genuinely different intermediate steps, not mere citation depth differences. The AI's different path is logically complete and valid, with each step properly justified.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: unpack the similarity of A and B to C via Definition 6.1 (equiangular with proportional sides), then conclude A is similar to B. Heath compresses the final inference into a single 'therefore' step, while the AI proof explicitly cites CN1 for transitivity of angle equality and uses Propositions 5.16 (inverse ratios) and 5.22 (ex aequali) to rigorously derive the proportionality of sides between A and B. The ai_only set {5.16, 5.22, CN1} consists entirely of ratio machinery and a common notion that flesh out steps Heath handles implicitly. The heath_only set is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 6.22
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone in both parts: the forward direction constructs third proportionals via 6.11, applies ex aequali (5.22) to obtain a key ratio, invokes the duplicate-ratio property of similar figures, and chains ratios via 5.11; the converse constructs a fourth proportional (6.12), builds a similar figure (6.18), applies the forward direction, then uses 5.11 and 5.9. The only citation differences are that the AI cites 6.20 (similar polygons are in duplicate ratio of corresponding sides) where Heath cites 6.19 (similar triangles are in duplicate ratio), and the AI explicitly cites D5.9 (definition of duplicate ratio) which Heath uses implicitly. Since 6.19 appears inside Heath's proof of 6.20, the proof-tree containment test confirms the AI is citing 6.20 as a higher-level unit while Heath uses its sub-result 6.19 directly, making this a citation-depth difference rather than a path difference. D5.9 is a definition and represents over-citation. The key intermediate conclusions are identical in both proofs.

### 6.23
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 determined the classification. Both proofs share the initial setup (placing parallelograms so BC is collinear with CG, proving DC collinear with CE, completing an intermediate parallelogram) and both apply 6.1 twice to establish the ratios of the parallelograms to the intermediate parallelogram in terms of the ratios of their sides. However, the mechanism for combining these ratios into the compounded ratio differs fundamentally. Heath constructs explicit auxiliary magnitudes K, L, M via 6.12 (fourth proportional), uses 5.11 (transitivity of ratio equality) to link these to the parallelogram ratios, and applies ex aequali to conclude. The AI bypasses this entire apparatus by directly invoking D6.5 (definition of compounded ratio) with the intermediate parallelogram DCGK as the linking magnitude, concluding immediately that ABCD:CEFG is compounded of the two side-ratios. The AI also provides more explicit detail for the collinearity argument (citing 1.13, 1.14) and the construction (citing 1.31), which Heath leaves implicit. Since the key intermediate conclusions about the auxiliary magnitudes K, L, M and the ex aequali step form the backbone of Heath's proof but are entirely absent from the AI proof, which follows a logically valid but structurally different path, this is a genuine path difference.

### 6.24
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) establishing equiangularity of the sub-parallelogram with the whole, (2) establishing proportionality of sides about equal angles, (3) concluding similarity by D6.1, and (4) using 6.21 for mutual similarity. The critical difference is citation depth. The AI cites 6.4 (equiangular triangles have proportional sides) to obtain all proportional relationships directly from equiangular sub-triangles, while Heath re-derives the internals of 6.4 inline using 6.2 (proportional intercepts), 5.16 (alternately), 5.18 (componendo), and 5.22 (ex aequali). The proof-tree containment test confirms that three of the four heath_only items (6.2, 5.16, 5.22) appear inside Heath's own proof of 6.4, indicating the AI cites 6.4 as a unit while Heath unpacks its internals. The remaining heath_only item 5.18 (componendo) is avoided by the AI because 6.4 applied to appropriate sub-triangles gives the proportionality of sides about common angles directly, without needing the ratio manipulation step. The AI's additional citations (1.29, 1.32, 1.34, CN1) are foundational angle and parallelogram theorems used to set up the equiangular triangles, consistent with over-citation at a finer granularity level.

### 6.25
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: construct parallelograms BE equal to ABC and CM equal to D, take GH as a mean proportional to BC and CF, construct KGH similar to ABC on GH, establish that the ratio of the parallelogram areas equals the ratio of the similar figures via the duplicate ratio property, and conclude by the equality chain that KGH equals D. The citation differences are all citation-depth variations: the AI cites 6.20 (similar polygons in duplicate ratio) where Heath cites 6.19 (similar triangles in duplicate ratio), and 6.19 appears inside Heath's proof of 6.20, satisfying the proof-tree containment test. Similarly, the AI cites 1.45 for both parallelogram constructions where Heath distinguishes 1.44 and 1.45, and 1.44 is used inside the proof of 1.45. The AI's use of 5.11 and 5.14 instead of Heath's 5.16 represents a minor algebraic variation in ratio manipulation (transitivity plus equal-ratios-imply-equality vs alternando) that achieves the same proportional conclusion. The additional AI citations of 1.14, 1.29, CN1, and D5.9 are over-citations of construction details, common notions, and definitions that Heath leaves implicit.

### 6.26
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Both proofs are by contradiction: they assume the smaller parallelogram is not about the same diameter as the whole, construct a parallelogram about the diameter using I.31, and apply VI.24 to establish similarity. However, the mechanism for deriving the contradiction differs substantially. Heath uses the proportionality DA:AB = GA:AK (from VI.24) and DA:AB = GA:AE (from similarity of the given parallelograms), then via V.11 gets GA:AK = GA:AE, and by V.9 concludes AE = AK, which is impossible. The AI instead uses VI.21 (transitive similarity) to conclude AEFG is similar to AKHL, then employs an elaborate argument using D6.1 for proportional sides, V.16 (alternando), and VI.2 (parallel lines cutting triangle sides proportionally) to show that vertex F must lie on the diagonal AC, contradicting the assumption. Since the key intermediate conclusions and the contradiction mechanism are different (V.9-based magnitude equality vs. VI.2-based positional argument), and the AI's path is logically valid throughout, this is classified as a path difference (D).

### 6.27
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect AB at C, use 6.26 to establish that the similar deficient parallelograms are about the same diagonal, and use 1.43 to identify equal complements about that diagonal. The difference lies in how each proof concludes the inequality. Heath uses 1.36 (parallelograms on equal bases in same parallels are equal) to establish CH = CG from AC = CB, then derives the gnomon relationship to show AD > AF. The AI omits 1.36 and instead argues more directly from the geometric containment of KF within CF (since KF is similar to CF but on a shorter base), concluding CE > AF by CN5 (whole greater than part). The ai_only item CN5 is a common notion that Heath uses implicitly, and the heath_only item 1.36 is an intermediate step the AI compresses away through its containment argument. These represent different levels of citation depth on the same backbone, not a fundamentally different proof path.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect AB, construct a similar parallelogram EBFG on the half, handle two cases (C equals EBFG, or C is less), construct the excess parallelogram similar to D, show it is about the same diameter as EBFG via VI.21 and VI.26, establish that the gnomon equals C, and then use area equalities to show the applied parallelogram TS equals C. The AI proof cites many additional construction-level propositions (1.10, 1.3, 1.31, P1) and axioms (CN3) that Heath leaves implicit, which are standard over-citations. The substantive citation difference is that the AI uses 1.43 (complements about the diameter are equal) where Heath uses 1.36 (parallelograms on equal bases in same parallels are equal) to establish the same area equality leading to TS = gnomon = C. The AI also cites 6.24 and 6.27 which Heath omits, but these support the same conclusions Heath reaches by other means. Since the key intermediate conclusions are identical and only the citation granularity differs, this is a granularity difference.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same backbone: bisect AB at E, construct a parallelogram on EB similar to D, use VI.25 to build a larger parallelogram equal to the first plus C and similar to D, show the two parallelograms are about the same diameter via VI.26, demonstrate the gnomon equals C, and conclude the applied parallelogram equals C with the excess similar to D via VI.24. The AI's eight ai_only citations (1.10, 6.18, 6.22, CN3, CN5, D6.1, P1, P2) are all construction propositions, common notions, definitions, or postulates that provide finer granularity to steps Heath treats as self-evident. The single heath_only citation (1.36, parallelograms on equal bases in same parallels are equal) is used at the same logical position in both proofs — Heath cites it explicitly to show AN = NB, while the AI makes the same argument more tersely without the explicit citation. This is a citation-depth difference at the same backbone, not a structural divergence.

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs a square on AB, applies a parallelogram equal to it exceeding by a similar figure (6.29), then uses reciprocal proportionality of equiangular parallelograms (6.14) to derive BA:AE = AE:EB. The AI takes an entirely different path: it uses 2.11 to cut AB so that rect(AB,BC) = sq(AC), then applies the converse of 6.17 to convert this rectangle-equals-square relation into the proportion AB:AC = AC:BC, and invokes D6.3 to conclude the extreme and mean ratio. The Jaccard similarity is 0.0 with completely disjoint citation sets, and the proof-tree containment test confirms the AI citations (2.11, 6.17) do not appear inside Heath's cited propositions (6.29, 6.14). Both proofs are logically complete but argue through fundamentally different intermediate conclusions, making this a genuine path difference.

### 6.31
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: drawing the perpendicular AD from the right angle to BC, establishing similarity of sub-triangles ABD and ACD to the whole triangle ABC via 6.8, deriving the proportional relationships CB:BA = BA:BD and BC:CA = CA:CD, connecting these to the ratios of similar figures on the sides, and concluding via BD+DC=BC that the figure on BC equals the sum of the figures on BA and AC. The key citation difference is that Heath uses 6.19 (similar triangles are in duplicate ratio of corresponding sides) to establish the figure-ratio step, while the AI uses 6.20 (similar polygons in duplicate ratio of corresponding sides) along with explicit Book V ratio manipulations (D5.9, 5.24, 5.9). The proof-tree containment test confirms that 6.19 appears explicitly within Heath's proof of 6.20, so the AI is citing the higher-level result as a unit while Heath uses the more specific sub-result directly. The remaining ai_only items (1.12 for the perpendicular construction, D5.9 for the duplicate ratio definition, 5.24 for ratio addition, 5.9 for ratio equality) represent over-citation of construction steps and ratio arithmetic that Heath leaves implicit.

### 6.32
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: The AI proof takes a fundamentally different geometric approach from Heath's proof. Heath establishes angle equalities via I.29, uses VI.6 to show the triangles are equiangular, then combines angle sums with I.32 and applies I.14 (adjacent angles equal to two right angles imply collinearity). The AI instead introduces an auxiliary intersection point G where line AE crosses line BD, establishes equiangularity of triangles ABG and EDG via I.29, I.15, and I.32, uses 6.4 for proportional sides, then applies ratio manipulation (5.17/5.9) to show G coincides with C, concluding collinearity. The key intermediate conclusions are entirely different: Heath argues through angle sums at vertex C, while the AI argues through proportional segments and point coincidence. Q2 Case B applies (different backbone). Under Q3, the AI's chain is logically complete despite misciting 5.17 where 5.18 is needed — under the lenience rule, the mathematical inference is sound (informal but sound), so this is NOT-E. Classification is D (path difference).
**Audit Record**: CANDIDATE E — 6.32
  violated_claim : "by 5.17 (composition of a ratio) we obtain (BG + GD)/GD = (BC + CD)/CD"
  failure_mode   : invalid_inference
  missing_is     : expansion — the correct proposition 5.18 would justify this step; it is a citation number error, not a logical gap
  evidence       : AI Step 8 cites 5.17 for going from BG/GD = BC/CD to (BG+GD)/GD = (BC+CD)/CD, but 5.17 is separando (componendo to separando), not componendo (separando to componendo, which is 5.18)
  why_not_terse  : This is a miscitation of proposition number, not a logical gap. The mathematical step is sound via 5.18.
VERDICT: NOT-E — missing_is = expansion; the inference is mathematically sound, just incorrectly numbered. Reclassified as D.

### 6.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: constructing equimultiple arcs and corresponding central angles, applying the Eudoxian definition of proportion (V. Def. 5 / D5.5) via the equimultiple comparison, and then extending the ratio to inscribed angles using the central-angle-is-double-inscribed-angle relationship. The AI proof cites exactly the same propositions as Heath (3.27 and D5.5) plus six additional references (3.20, 5.15, CN2, D3.1, P1, P3) that Heath leaves implicit. Among these, P1 and P3 are construction postulates, CN2 is a common notion, and D3.1 is a definition, all representing standard over-citation. The substantive additions 3.20 (inscribed angle theorem, which Heath invokes implicitly as 'they are doubles respectively') and 5.15 (halves in same ratio) make explicit what Heath states without citation. With heath_only empty and all ai_only items corresponding to the same underlying reasoning at finer granularity, this is a clear Case A same-backbone-different-depth scenario.


## Book 7

| Category | Count |
|---|---|
| Perfect match (P) | 1 |
| Granularity difference (G) | 31 |
| Path difference (D) | 6 |
| AI proof error (E) | 1 |

**Total**: 39 propositions

### 7.1
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: a reductio ad absurdum assuming some number E greater than a unit measures both AB and CD, then arguing through the anthyphairesis (Euclidean algorithm) process that E must measure every successive remainder until it must measure the unit, yielding a contradiction since a number greater than one cannot measure the unit. The AI proof follows this same structure but is more summary-style, arguing the general principle that if E measures two quantities it measures their difference, rather than tracing each specific step as Heath does. The citation difference is entirely attributable to the AI over-citing definitions and a common notion (D7.1, D7.3, D7.5, D7.15, CN5) that Heath uses implicitly without citation. Heath cites only D7.12, which the AI also cites. Since heath_only is empty and all ai_only items are axiom-level (definitions and common notions), this is a clear case of same backbone with different citation depth.

### 7.2
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: (1) trivial case where CD measures AB, (2) successive subtraction (antanairesis) terminates at a number greater than a unit by contrapositive of 7.1, (3) the final remainder FC is shown to be a common measure of AB and CD by chaining divisibility upward through the subtraction steps, and (4) FC is shown to be the greatest common measure by proving any common measure G must divide FC and therefore cannot exceed it. The key intermediate conclusions are identical in both proofs. The only difference is citation depth: the AI explicitly cites definitions (D7.2, D7.3, D7.5, D7.12) and common notions (CN2, CN3, CN5) that Heath invokes implicitly. Heath's only explicit citation is 7.1, which the AI also cites. Since heath_only is empty and ai_only consists entirely of definitions and common notions, this is a pure over-citation case with the same backbone, yielding Granularity difference (G).

### 7.3
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: find D = GCM(A,B) via 7.2, split into two cases (D measures C or not), and in the second case find E = GCM(D,C) via 7.2. The key intermediate conclusions are identical in both proofs. The only citation difference is that the AI explicitly cites definitions D7.12 (numbers not prime to one another) and D7.3 (greatest common measure), which Heath uses implicitly without citation. The AI's proof technique for establishing 'greatest' uses the universal divisor property directly (every common measure divides the GCM) rather than Heath's proof by contradiction, but this is a stylistic difference in the final step of each case, not a difference in the backbone of key intermediate conclusions. Since the backbones match and the ai_only items are purely definitional over-citations, this is a same-backbone, different-depth situation characteristic of G.

### 7.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof establishes three substantive cases (prime to each other, measures, does not measure) and in the non-trivial cases constructs the GCD via 7.2 and decomposes the smaller number into equal aliquot parts to demonstrate it is 'parts' of the greater. The AI proof takes a fundamentally different approach: it treats the proposition as following directly from Definitions 7.3 and 7.4, which define 'part' as measuring and 'parts' as not measuring. The AI argues by exhaustion (either measures or does not) that one definition always applies. These are genuinely different backbones: Heath's proof is constructive, building the decomposition through GCD computation, while the AI's is purely definitional. Under the hardened Q1(b) standard, the AI's definitional argument is logically complete (each claim is supported by a cited definition), so no E applies. Since the backbones differ (Case B in Q2), Q3 confirms the AI's different path is valid, yielding D.

### 7.5
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) B consists of n copies of A, (2) D consists of n copies of C, (3) their sum B+D consists of n copies of A+C, and (4) therefore A+C is the same part of B+D as A is of B. Heath works concretely by dividing segments and pairing them (BG with EH, GC with HF), while the AI uses algebraic notation (B = n*A, D = n*C, so B+D = n*(A+C)), but the logical backbone is identical. The only citation difference is that the AI explicitly cites D7.3 and D7.5 for the definitions of 'part' and 'multiple,' which Heath uses implicitly without citation. Since heath_refs is empty and ai_only contains only definitions, this is a clear case of over-citation at the definitional level — same backbone, different citation depth.

### 7.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: divide AB into parts AG, GB of C and DE into parts DH, HE of F with equal multitudes, then apply Proposition 7.5 twice to show that AG+DH and GB+HE are each the same part of C+F as the corresponding part is of C, and conclude that AB+DE is the same parts of C+F as AB is of C. The AI proof's only divergence from Heath is the additional citation of Definitions 7.3 and 7.4 (definitions of 'part' and 'parts'), which are implicitly used by both proofs but explicitly cited only by the AI. Since heath_only is empty and ai_only contains only definitions (over-citation), this is a citation-depth difference with the same logical backbone, yielding Granularity difference (G).

### 7.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary number CG such that EB is the same part of CG as AE is of CF, then applies Proposition 7.5 (parts summing to the same part of a sum) to conclude AB is the same part of GF, derives GF equals CD, and substitutes via the equality GC equals FD. The AI proof takes a fundamentally different approach: it decomposes the wholes into m copies of the parts (BC = m times A, E = m times D), then performs componentwise subtraction using CN3 to obtain BC minus E = m times (A minus D), concluding directly from definitions D7.3 and D7.5 that the remainder is the same part. The key intermediate conclusions differ entirely: Heath's backbone pivots on the construction of CG and the application of 7.5, while the AI's backbone pivots on the multiplicative decomposition and componentwise subtraction. Since the AI's chain from premises to conclusion is logically complete and sound (verified under Q3), the classification is D.

### 7.8
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: divide the wholes into corresponding parts of CD and CF, apply Proposition 7.7 twice to each pair of corresponding parts to establish that each remainder is the same part of FD that the corresponding whole part is of CD, then sum the remainders to obtain the conclusion. The AI proof follows this identical structure with different letter labels. The only citation difference is that the AI explicitly cites D7.4 and D7.20 (definitions of 'part' and 'parts') to justify the decomposition into parts and the recombination, while Heath applies these definitions implicitly. Since ai_only contains only definitions and heath_only is empty, this is a Case A granularity difference: same backbone, different citation depth.

### 7.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: decompose the larger numbers into equal parts, then use Propositions 7.5 and 7.6 to show that the part-or-parts relationship is preserved under addition. Heath divides BC into parts equal to A and EF into parts equal to D, then applies 7.5 and 7.6 to conclude. The AI proof does the same, decomposing B into n copies of A and D into n copies of C, then iteratively applying 7.5 (for the part case) and 7.6 (for the parts case). The ai_only citations (7.4, D7.3, D7.4, D7.5) are all over-citations: definitions that make explicit what Heath leaves implicit, and Proposition 7.4 which justifies the case split that Heath treats as obvious. Heath's citation set is a proper subset of the AI's, and heath_only is empty. The key intermediate conclusions are identical in both proofs, differing only in the level of explicit citation detail.

### 7.10
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the initial structure of dividing AB into parts AG, GB of C and DE into parts DH, HE of F, and both apply 7.9 to establish that whatever part or parts AG is of DH, the same part or parts C is of F. However, the combining step diverges: Heath applies 7.9 again to GB and HE separately, then uses 7.5 and 7.6 to combine the results for the sum AB of DE. The AI instead argues that since AG equals GB and DH equals HE (each being equal parts of C and F respectively), AB is the same multiple of AG that DE is of DH, so the part-or-parts relationship between AB and DE is identical to that between AG and DH, which was already linked to C and F via 7.9. This is a genuinely different logical backbone at the combining step: Heath uses addition-of-parts propositions (7.5, 7.6) while the AI uses an equal-multiples argument grounded in definitions (D7.20). Both paths are logically valid, yielding classification D.

### 7.11
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they convert the proportion AB:CD = AE:CF into a part/parts relationship via D7.20, apply 7.7 and 7.8 to transfer that relationship from wholes to remainders, and convert back to a proportion via D7.20. The AI proof is more granular in two ways: it explicitly separates the three cases from D7.20 (part, parts, multiple) whereas Heath compresses them into 'part or parts', and it cites supporting definitions (D7.3, D7.4, D7.5), a common notion (CN3), and a justifying proposition (7.4) that Heath leaves implicit. Since heath_only is empty and the ai_only items are all definitional over-citations or support for the explicit case structure, this is a same-backbone, different-depth situation characteristic of granularity difference.

### 7.12
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that proportionality (A:B = C:D) means A is the same part or parts of B as C is of D (via D7.20), then use 7.5 and 7.6 to show that the sums preserve this part/parts relationship, and finally invoke D7.20 to conclude proportionality of the sums. The AI proof adds an explicit three-way case split using 7.4 (part, parts, or multiple) and cites the underlying definitions D7.3, D7.4, and D7.5, whereas Heath combines the part and parts cases in a single invocation of '7.5, 7.6' without explicitly citing 7.4 or those definitions. Since heath_only is empty and the AI's extra citations (7.4, D7.3, D7.4, D7.5) represent deeper citation granularity rather than a different argumentative path, this is Case A of Q2: same backbone, different citation depth.

### 7.13
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: unpack the proportion A:B :: C:D via D7.20, apply the alternation property to establish the corresponding relationship between A,C and B,D, then restate as a proportion via D7.20. The AI proof is more explicit, separating into three cases (part, parts, multiple) and citing 7.9 for the 'part' case and 7.10 for the 'parts' case, plus D7.3 for the 'multiple' case. Heath's proof handles 'part or parts' in a single invocation of 7.10. The proof-tree containment test confirms that 7.9 appears inside Heath's proof of 7.10, so the AI's separate citation of 7.9 is a citation-depth difference rather than a path difference. D7.3 is a definition used for the AI's additional explicit 'multiple' case, which does not change the backbone. The key intermediate conclusions are the same in both proofs.

### 7.14
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone for the three-term case: apply VII.13 (alternate proportion) to get A:D = B:E, then apply VII.13 again to get B:E = C:F, chain these to conclude A:D = C:F, and apply VII.13 once more to obtain A:C = D:F. The AI's ai_only citations are D5.17 (definition of ex aequali) and D7.20 (definition of ratio for numbers), both of which are definitions that Heath uses implicitly without citation. The AI also adds an explicit inductive argument (Steps 7-9) to extend the three-term result to the general case, whereas Heath proves only the three-term case directly. These differences are matters of citation depth and explicitness, not different logical paths, placing this squarely in Case A of Q2.

### 7.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof decomposes BC into its constituent units and EF into equal parts equal to D, then uses 7.12 (summing equal ratios) to establish that unit:part = BC:EF, yielding A:D = BC:EF directly. The AI instead establishes the proportion A:B :: C:D using the definition of proportional numbers (D7.20), then applies 7.13 (alternation of proportion) to obtain A:C :: B:D and concludes from the proportional relationship. The containment test confirms that 7.12 does not appear inside Heath's proof of 7.13 (which uses 7.10 and D7.20), so the two approaches are genuinely independent routes to the same conclusion. The Jaccard similarity of 0.0 reflects this complete divergence in citation sets. The AI's path is logically valid: each step is properly justified, and the chain runs soundly from premises to conclusion.

### 7.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) from A*B=C, the unit measures A the same number of times that B measures C; (2) by alternation via 7.15, the unit measures B the same number of times that A measures C; (3) from B*A=D, the unit measures B the same number of times that A measures D; (4) combining these, A measures both C and D the same number of times, so C=D. The logical backbone is the same in both proofs. The only citation difference is that the AI explicitly cites D7.15 (the definition of multiplication) to justify the measurement relationships arising from multiplication, while Heath uses this definition implicitly without citing it. Since ai_only contains only a definition and heath_only is empty, this is a classic over-citation at the definitional level, which is a citation-depth difference under Case A of Q2, yielding G.

### 7.17
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determined the classification. Heath's proof introduces a unit F and establishes the ratios F:A = B:D and F:A = C:E via D7.20, then uses transitivity to get B:D = C:E, and finally applies 7.13 (proportional alternation) to conclude B:C = D:E. The AI proof takes a fundamentally different route: it reasons through the 'part' relationship (D7.3), establishing that B is a part of D and C is the same part of E (both measured the same number of times, namely the units in A), then applies 7.9 (part alternation) to conclude that whatever part or parts B is of C, the same is D of E, and finishes with D7.20. The key intermediate conclusions differ — Heath works through unit-based ratio chains while the AI works through part-of relationships — making this a genuine path difference. The AI's alternative chain is logically sound and complete.

### 7.18
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones and cite exactly the same propositions. Both proofs first invoke 7.16 to establish commutativity of multiplication (rewriting A times C as C times A, and B times C as C times B), then apply 7.17 to conclude that since one number C multiplied both A and B to produce D and E, the ratio D:E equals A:B. The citation sets are identical (ai_used = heath_refs = {7.16, 7.17}), the Jaccard similarity is 1.0, and the key intermediate conclusions match exactly, satisfying the perfect match check.

### 7.19
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Heath's proof uses the auxiliary product G = A*C as its pivot, establishing the ratio chains G:E and G:F (via 7.17 and 7.18) and then applying 5.9 (equal ratios to the same magnitude imply equality) and 5.7 (equal magnitudes have the same ratio) to complete both directions. The AI instead uses B*D as its pivot, establishing A*D : B*D = A:B (via 7.18) and B*C : B*D = C:D (via 7.17), then concluding equality from the fact that both A*D and B*C bear the same ratio to B*D, citing D7.20 rather than 5.9. This constitutes a genuinely different algebraic backbone: the key intermediate conclusions involve different auxiliary quantities (A*C vs B*D) and different ratio chains. Both proofs are logically complete. The AI's reasoning through D7.20 to conclude equality from equal ratios to a common reference is compressed but sound, satisfying Q3(b) under the lenience rule. Therefore the classification is D (path difference).

### 7.20
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: (1) assume for contradiction that C is 'parts' of A, (2) derive the existence of smaller numbers in the same ratio, contradicting the minimality of C and D, (3) conclude C is a 'part' of A and measures it, (4) conclude D measures B the same number of times. The proofs differ in the technical mechanism within these steps: Heath divides into equal parts and uses 7.12 (aggregation of proportions) for the contradiction, while the AI uses 7.17 (multiplication preserving ratios); Heath uses 7.13 and Def. 20 directly for the second conclusion, while the AI chains through 7.17, 7.19, 7.16, and CN5. The proof-tree containment test confirms that heath_only item 7.13 appears inside Heath's proof of 7.17 (which the AI cites), supporting a citation-depth interpretation. The item 7.12 reflects a technique-level variation within the same key intermediate conclusion (finding smaller numbers in same ratio), not a different backbone. The AI's additional citations (7.16, 7.17, 7.19, CN5, D7.3, D7.4) represent a more algebraic approach at finer granularity to reach the same conclusions Heath reaches more directly.

### 7.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: assume for contradiction that smaller numbers C, D exist in the same ratio as A, B; apply 7.20 to derive that the least numbers measure A and B the same number of times; conclude that a common measure greater than 1 exists for A and B; contradict D7.12 (A and B are prime to one another). The heath_only citation 7.16 (commutativity of multiplication) is used by Heath to convert the measurement relationship into a form showing the common measure, while the AI achieves the same conclusion by directly observing that A = mE and B = mF implies m divides both A and B, an arithmetic reformulation that does not require 7.16. The ai_only citation D7.3 (definition of part) is a definition the AI cites explicitly but Heath does not, representing over-citation. These are citation-depth differences, not path differences, as both proofs establish the same key intermediate conclusions in the same logical order.

### 7.22
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume A, B (least numbers in same ratio) are not coprime; deduce some number C measures both; define D and E so that C*D = A and C*E = B; apply 7.17 to conclude D:E = A:B; observe D < A and E < B, contradicting the hypothesis that A, B are least. The AI proof adds explicit citations to foundational definitions (D7.3 for 'measures', D7.12 for 'prime to one another') and Common Notion 5 to justify D < A and E < B, whereas Heath leaves these implicit. Since heath_only is empty and ai_only contains only definitions and a common notion, this is a clear case of over-citation at a more granular level with no divergence in the proof's backbone.

### 7.23
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone: assume for contradiction that C and B are not prime to one another, derive that some number D measures both C and B, then use the transitivity of 'measures' (D measures C and C measures A, so D measures A) to show D is a common measure of A and B, contradicting the hypothesis. The AI proof cites D7.3 and D7.15 explicitly when unpacking the transitivity argument, spelling out the definitional basis for what it means to measure and multiply, while Heath simply states the transitive step without citing these definitions. Since heath_only is empty and ai_only contains only definitions (D7.3, D7.15), this is a pure over-citation case where the AI provides more granular definitional justification for the same intermediate conclusions.

### 7.24
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume a common measure E of C and D, use 7.23 to show A and E are prime, construct F such that D = E*F, set up the proportion E:A = B:F via 7.19, apply 7.21 and 7.20 to conclude E measures B, then derive a contradiction with B and C being prime via D7.12. The only citation differences are that the AI adds D7.14 (definition of composite numbers, an over-citation when setting up the contradiction hypothesis) and omits 7.16 (which Heath uses to explicitly justify the measurement relationship between F and D, while the AI handles this directly from the definition of measurement and D7.15). Since the key intermediate conclusions are identical and the differences are purely citation-depth matters, this is a granularity difference.

### 7.25
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they observe that A is prime to B in two instances (Heath makes this explicit by introducing an auxiliary variable D equal to A; the AI simply uses A twice), then apply Proposition 7.24 to conclude that the product A*A is prime to B. The ai_only set consists entirely of definitions (D7.12, D7.15, D7.18) that Heath uses implicitly without citation, representing over-citation by the AI rather than any substantive difference in reasoning. The heath_only set is empty, confirming no steps are missing from the AI proof. The proofs reach the same key intermediate conclusions through the same logical path, differing only in citation depth.

### 7.26
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) since A and B are each prime to C, their product AB is prime to C by 7.24; (2) since A and B are each prime to D, their product AB is prime to D by 7.24; (3) since C and D are each prime to AB, their product CD is prime to AB by 7.24; therefore the products are prime to one another. The AI proof explicitly cites Definition 7.12 to justify the symmetry of the coprimality relation (switching from 'AB is prime to C' to 'C is prime to AB'), whereas Heath uses this symmetry implicitly without citation. Since D7.12 is a definition and the only difference is that the AI over-cites by making explicit what Heath leaves implicit, this is a citation-depth difference with the same backbone, yielding G.

### 7.27
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same theorem citation set (7.25 and 7.26) and follow the same fundamental strategy: establish pairwise coprimality conditions using 7.25, then apply 7.26 to conclude that the products (squares and cubes) are coprime. The ai_only set consists entirely of definitions (D7.12 for prime-to-one-another, D7.15 for multiply, D7.18 for square/cube), which Heath uses implicitly without explicit citation. The heath_only set is empty. The slight difference in the order of intermediate steps (the AI applies 7.26 directly to prove squares coprime, while Heath uses iterated 7.25 applications) represents a minor variation in presentation rather than a genuinely different backbone, since both approaches reduce to the same pair of core propositions. This is a classic over-citation pattern where the AI explicitly cites foundational definitions that Heath treats as understood.

### 7.28
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs argue through the same key intermediate conclusions: in each direction of the biconditional, they assume a common measure D exists for the pair that should not have one, then use the additive relationship (sum = part + part) to show D also measures the third quantity, yielding a contradiction with the primality hypothesis via D7.12. The AI proof makes explicit use of CN2 (adding equals), CN3 (subtracting equals), D7.3 (part), and D7.15 (measuring) where Heath simply states the consequence without citing these foundational items. Since heath_only is empty and all ai_only items are definitions and common notions that merely spell out what Heath leaves implicit, this is a same-backbone, different-depth situation — Case A of Q2 — yielding Granularity difference (G).

### 7.29
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Both proofs follow the same logical backbone: a proof by contradiction assuming the prime and the number are not coprime, deriving that a common divisor must relate to the prime in a way that contradicts either the definition of primality or the hypothesis, and concluding they are coprime. The AI explicitly cites D7.11 (definition of prime) and D7.12 (definition of numbers prime to one another) while Heath uses these definitions implicitly without citation. Since heath_only is empty and ai_only contains only definitions, this is a clear case of the AI over-citing definitional references that Heath leaves implicit. The key intermediate conclusions are identical in both proofs, making this a granularity difference decided at Q2 Case A.

### 7.30
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs follow the same logical backbone: assuming the prime does not measure A, they establish coprimality via 7.29, introduce the quotient of C by the prime, derive the proportion prime:A :: B:quotient via 7.19, invoke 7.21 to establish the prime and A as least in their ratio, and conclude via 7.20 that the prime measures B. The key intermediate conclusions are identical in both proofs. The only difference is that the AI explicitly cites D7.11 (definition of prime number) and D7.3 (definition of 'measures'), which Heath leaves implicit. Since heath_only is empty and ai_only contains only definitions, this is a clear case of over-citation at the definitional level with the same argumentative backbone, yielding a granularity difference.

### 7.31
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone: (1) A is composite so some number B measures it; (2) if B is prime, done; (3) if B is composite, some C measures B, and since C measures B and B measures A, C also measures A; (4) the sequence of divisors is strictly decreasing and bounded below by 1; (5) therefore the process terminates at a prime that measures A. Heath's proof cites no explicit propositions, treating the definitional foundations as understood. The AI proof explicitly cites definitions D7.2, D7.3, D7.11, D7.13, D7.15 and Common Notion CN5 to justify the same steps. Since heath_only is empty and ai_only contains only definitions and one common notion, this is a classic Case A of Q2: same backbone with different citation depth, where the AI over-cites foundational definitions that Heath leaves implicit.

### 7.32
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same two-case backbone: (1) if A is prime, the conclusion holds immediately; (2) if A is composite, then by 7.31 some prime number measures it. The AI proof explicitly cites definitions D7.11 (prime) and D7.13 (composite) to justify why each case satisfies the relevant definition, while Heath leaves these definitional justifications implicit. Since ai_only contains only definitions and heath_only is empty, and both proofs establish the same key intermediate conclusions in the same logical order, this is a citation-depth difference under Q2 Case A, yielding G.

### 7.33
**Category**: AI proof error
**Jaccard**: 0.300
**Analysis**: The classification was decided at Q1(b). The AI's proof contains an invalid inference in Step 8: it claims that E and F are pairwise coprime because 'any common measure of E and F would also measure G,' but this is false in general. Group coprimality (gcd(E,F,G)=1, established in Steps 5-7) does not entail pairwise coprimality. For example, with A=6, B=10, C=15, D=gcd=1, we get E=6, F=10, G=15 where gcd(6,10)=2 but 2 does not divide 15, yet gcd(6,10,15)=1. The AI then applies Proposition 7.21 (numbers prime to one another are least in their ratio) to the pair E, F, but 7.21 requires pairwise coprimality which was not validly established. This breaks the proof chain: without pairwise coprimality, the AI cannot invoke 7.21 to get that E, F are least in ratio E:F, and therefore cannot use 7.20 to derive the contradiction. Heath avoids this issue entirely by using a direct contradiction argument through 7.19 (cross-multiplication proportion). The audit record completes convincingly: the AI infers Q (pairwise coprimality) from P (group coprimality) where P does not entail Q, satisfying the 'invalid inference' mode.
**Audit Record**: CANDIDATE E — 7.33
  violated_claim : "E and F are prime to one another (from Step 7, any common measure of E and F would also measure G, giving a common measure of all three greater than one, which was shown impossible)"
  failure_mode   : invalid_inference
  missing_is     : support
  evidence       : Step 8 claims pairwise coprimality of E, F from group coprimality of E, F, G. The parenthetical justification "any common measure of E and F would also measure G" is stated without proof and is false in general (e.g., gcd(6,10)=2 does not divide 15, yet gcd(6,10,15)=1). The subsequent invocation of 7.21 (numbers prime to one another are least in their ratio) requires pairwise coprimality, so the proof chain from Step 7 to Step 8's conclusion is broken.
  why_not_terse  : This is not compression of a valid argument but an incorrect logical inference. No valid argument exists from group coprimality to pairwise coprimality in general, so there is nothing being abbreviated — the claimed implication is simply false.

### 7.34
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: find the least numbers in the ratio A:B (7.33), construct the LCM as the cross-product (7.19), then prove minimality by contradiction using the least-ratio property (7.20) to establish divisibility. The sole heath_only citation 7.17 (if a number multiplies two numbers, the products have the same ratio) is used by Heath in the final contradiction step to conclude that since E measures G, C measures D. The AI replaces this with 7.16 (commutativity of multiplication) to directly show G = E * M >= E, achieving the same contradiction by a slightly different algebraic rearrangement rather than a proportionality argument. The ai_only items are mostly definitions and common notions (CN1, D7.1, D7.2, D7.3, D7.5) representing over-citation, plus 7.22 which the AI uses to explicitly justify that least-ratio numbers are coprime before invoking 7.21, a step Heath leaves implicit. The AI also unifies Heath's two cases (coprime and non-coprime) into a single argument via 7.33, which is a presentational difference, not a backbone difference. Since the key intermediate conclusions are the same and only citation depth and the final contradiction technique differ, this is a granularity difference.

### 7.35
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: proof by contradiction assuming the LCM does not measure the given number, showing that the remainder after repeated subtraction (Heath) or division (AI) is a smaller positive number measured by both original numbers, contradicting minimality of the LCM. The AI proof explicitly cites 7.34 (existence of LCM), D7.3, and D7.5 (definitions of measurement), while Heath's proof uses no explicit citations, leaving these references implicit. The ai_only set consists entirely of definitions and the immediately prior supporting proposition, which are over-citations that do not alter the proof's logical structure. The heath_only set is empty. Since the key intermediate conclusions are identical and the only differences are in citation depth, Case A of Q2 holds, yielding G.

### 7.36
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: construct D = LCM(A, B) using 7.34, then construct E = LCM(D, C) using 7.34, show all three numbers measure E, and prove minimality using 7.35 applied twice. Heath splits into two cases (C measures D vs. C does not measure D), while the AI handles only the general case which subsumes both. The ai_only citations (D7.3, D7.5) are definitions that the AI uses to make explicit the transitivity of divisibility (if A divides D and D divides E, then A divides E), which Heath leaves implicit. Since heath_only is empty and the ai_only items are purely definitional, this is a citation-depth difference with the same backbone, yielding Granularity difference (G).

### 7.37
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) unit measures C the same number of times as B measures A, (2) by VII.15 alternation, unit measures B the same number of times as C measures A, (3) whatever part the unit is of B, C is the same part of A, (4) since the unit is the part of B called by B's name, C is the part of A called by B's name. The AI proof explicitly cites four definitions (D7.3, D7.5, D7.15, D7.20) that Heath uses implicitly without citation, making the ai_only set consist entirely of definitional over-citations. With identical backbones and heath_only empty, this is Case A: same key intermediate conclusions at different citation depth, yielding G.

### 7.38
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: they establish that a unit measures one number the same number of times that another number measures A, then apply alternation via 7.15 to conclude that A is measured by the number called by the same name as the part. The AI and Heath use different variable-name assignments but the roles and logical chain are identical. The only citation difference is that the AI explicitly cites D7.3 (definition of 'part') to justify the initial measurement relationship, whereas Heath invokes the same concept implicitly without citing the definition. Since heath_only is empty and ai_only contains only a definition, this is a pure citation-depth difference under Case A of Q2.

### 7.39
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) define the given parts and their corresponding numbers, (2) find the LCM of those numbers via 7.36, (3) show the LCM has the required parts via 7.37, (4) prove minimality by contradiction using 7.38. The AI proof is more detailed in the minimality argument (Steps 9-11), explicitly reconstructing the LCM construction by citing 7.34 and 7.35, which are sub-propositions used within the proof of 7.36. The AI also adds definitions D7.3 and D7.5 and common notion CN5 as explicit justification for steps that Heath leaves implicit. Since heath_only is empty and all ai_only items are either sub-results of already-cited propositions (7.34, 7.35 are internal to 7.36) or axiom-level items (CN5, D7.3, D7.5), this is a clear case of over-citation at finer granularity with the same backbone.


## Book 8

| Category | Count |
|---|---|
| Perfect match (P) | 2 |
| Granularity difference (G) | 16 |
| Path difference (D) | 9 |
| AI proof error (E) | 0 |

**Total**: 27 propositions

### 8.1
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume smaller numbers in the same continued proportion, derive via ex aequali (7.14) that the ratio of extremes is the same, apply 7.21 to conclude the original extremes are least in that ratio, then use 7.20 to show the first extreme measures the corresponding smaller number, yielding a contradiction. The AI proof extends the argument further by showing all terms must be equal (Steps 7-8), but this is additional detail atop the same backbone. The only citation difference is D7.20 (a definition of proportionality) in ai_only, which the AI cites explicitly in Step 8 when Heath leaves it implicit. Since the key intermediate conclusions are identical and the citation difference is a single definition, this is a same-backbone, different-depth case — Granularity difference (G).

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing a sequence of products, showing each consecutive pair has ratio A:B via 7.17 and 7.18, establishing that A and B are prime to one another via 7.22, using 7.27 to show the extremes of the sequence are prime to one another, and concluding by 8.1 that the sequence is the least in continued proportion with the given ratio. The only citation difference is that the AI explicitly cites 7.33 to justify obtaining A and B as the least numbers in the given ratio, whereas Heath simply states this as the setup without citation. This is a classic over-citation at the construction/setup level, making this a Case A same-backbone granularity difference. The AI also generalizes to n terms using algebraic notation rather than Heath's specific four-term example, but this is a presentational difference rather than a backbone difference.

### 8.3
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: The forward dependency gate passed (all citations are from Book 7 or earlier in Book 8). Q1 found no logical errors: the AI proof follows a clear chain from taking e,f as the least numbers in the ratio (7.33), showing they are prime (7.22), building the least continued proportion via 8.2 to get extremes e^(n-1) and f^(n-1), applying 7.27 to show these powers are prime, and identifying them with the original extremes by uniqueness. Q2 determined that both proofs share the same backbone of key intermediate conclusions: (1) take the least pair in the ratio, (2) show that pair is coprime, (3) build up to the full sequence via 8.2, (4) show the extremes are coprime via 7.27, (5) identify with the original sequence by uniqueness. The only citation difference is that the AI additionally cites definitions D7.12 and D7.20, which are non-substantive over-citations of definitions. Since the backbones match but the citation sets differ by these extra definitions, this is a granularity difference (G).

### 8.4
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Heath's proof constructs the continued proportion using LCM (7.34) as the linking mechanism between consecutive ratios, establishing proportionality via 7.13 and D7.20, and requires a two-case split (whether E measures K or not), with minimality proved via 7.20 and 7.35. The AI proof takes a fundamentally different approach: it constructs intermediate sequences by forming products of terms (using 7.17 and 7.18 for ratio properties of products) and then reduces to least terms using 7.33, avoiding the case split entirely. The AI's construction via multiplication followed by reduction to least numbers is a genuinely different logical backbone from Heath's LCM-based construction. Since both proofs are logically complete but argue through different key intermediate conclusions, the classification is D (path difference).

### 8.5
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 determined the classification. Heath's proof uses 8.4 to construct least numbers G, H, K in continued proportion with the given ratios, introduces an auxiliary product L = D*E, establishes A:L = C:E and L:B = D:F via VII.17, and then combines them via ex aequali (VII.14) to reach A:B = G:K. The AI proof takes a fundamentally different route: it directly constructs an intermediate number E = c*b, shows A:E = a:c via 7.18 and E:C = b:d via 7.17, and then invokes the definition of compounded ratio (D6.5) to conclude. The AI never needs least numbers in continued proportion (8.4) or ex aequali (7.14); Heath never uses 7.18 or the definition of compounded ratio explicitly. These are genuinely different logical backbones, not merely different citation depths of the same argument. The AI's path is logically valid under Q3, so the classification is D.

### 8.6
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) take the least numbers in the same ratio as the continued proportion, (2) show the first of these least numbers is not a unit (since A does not measure B), (3) use VIII.3 to establish coprimality of the extremes of the least continued proportion, (4) apply VII.14 (ex aequali) to transfer the ratio, and (5) derive a contradiction by showing the first least number would have to be 1. The AI proof is more explicit, separately handling consecutive and non-consecutive terms and citing auxiliary results (7.20, 7.21, 7.22 for properties of least ratios and coprimality, 8.2 for constructing the least continued proportion, and D7.3 for the definition of measurement direction) that Heath either uses implicitly or covers with 'similarly we can prove.' Heath_only is empty, confirming that the AI includes all of Heath's citations. The ai_only items are all depth-expansions of the same underlying logical steps, not evidence of a different proof path.

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs establish 8.7 by an identical proof by contradiction: assume the first number does not measure the second, apply 8.6 to conclude no number in the continued proportion measures any other, derive a contradiction with the hypothesis that the first measures the last, and conclude the first must measure the second. The citation sets are identical (both cite only 8.6), the key intermediate conclusions are the same, and the logical structure matches exactly, yielding a perfect match classification.

### 8.8
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Heath's proof works by applying VII.33 to the entire continued proportion sequence (all four numbers A,C,D,B) to find the least numbers G,H,K,L in the same ratio, then uses ex aequali (VII.14) to derive that the extreme ratio G:L equals A:B and hence E:F, followed by VII.21 and VII.20 to establish the measuring relationship. The AI takes a fundamentally different path: it applies VII.33 only to the two-number ratio A:B to find the least pair F,G, then explicitly constructs the full continued proportion via VIII.2, uses VIII.1 and VIII.3 to confirm these are least with prime extremes, applies VII.20 to get the measuring relationship, and finally uses VII.17 to show that multiplying by a common factor preserves the ratios. The backbones differ in their key intermediate conclusions: Heath's pivot is the ex aequali step connecting the full-sequence least numbers to the extreme ratio, while the AI's pivot is the explicit construction of the continued proportion via VIII.2 and ratio preservation via VII.17. Both paths are logically complete, making this a genuine path difference (D).

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they use 8.1 to establish the given sequence as the least in its ratio, then 8.2 to construct the power sequences, and finally exhibit the continued proportions from the unit to A and from the unit to B. The AI's two extra citations (ai_only: 7.22 and D7.15) represent citation-depth differences rather than path divergences. Specifically, 7.22 (the least numbers in a ratio are coprime) appears inside Heath's own proof of 8.2, confirmed by the proof-tree containment test, so the AI is citing an internal ingredient of a shared proposition. D7.15 is a definition used to justify the multiplication/exponent notation, which is standard over-citation. With heath_only empty and both proofs reaching the same key intermediate conclusions through the same logical route, this is a granularity difference in citation depth, not a different proof path.

### 8.10
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Heath's proof constructs the intermediate numbers explicitly by multiplying the geometric-sequence bases (D*F=H, D*H=K, F*H=L) and then establishes the continued proportion A:K=K:L=L:B step-by-step using 7.17 and 7.18 to relate ratios. The AI takes a fundamentally different high-level approach: it expresses A and B as powers of their respective bases, reduces the ratio of bases to least terms via 7.33, establishes coprimality via 7.22, uses 8.2 to find least numbers in continued proportion between the relevant powers, and then applies 8.8 to transfer the continued proportion to A and B. The backbones are genuinely different -- Heath works constructively with explicit products while the AI packages the argument through higher-level results (8.2, 8.8). The AI's path is logically complete, with each step supported by valid citations, so Q3 confirms a valid different path, yielding D.

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing the product of the two sides as a mean proportional, establishing two ratio equalities via VII.17 and VII.18, combining them to show the mean proportional, and then applying V.Def.9 for the duplicate ratio. The AI proof adds three explicit citations not in Heath (5.11 for transitivity of ratios, D7.15 for the definition of multiplication, and D7.18 for the definition of square number), but all three correspond to steps that Heath uses implicitly. Since heath_only is empty and the ai_only items are all definitions or an explicit transitivity citation that Heath applies without naming, this is a same-backbone, different-depth situation characteristic of granularity difference.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they construct mean proportionals (A-squared-B and A-B-squared) between two cube numbers, build a continued proportion chain showing the ratio between consecutive terms equals the ratio of the sides, and conclude via V. Def. 10 that the cube-to-cube ratio is triplicate of the side-to-side ratio. The logical backbone is identical. The AI's extra citations (7.16 for commutativity of multiplication, and definitions D7.16, D7.18, D7.19) are over-citations that make explicit what Heath leaves implicit. Heath's proof relies on the same arithmetic facts but does not cite commutativity or the definitions of square and cube numbers explicitly. Since heath_only is empty and the ai_only items are all basic properties or definitions, this is a citation-depth difference with the same backbone, yielding G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: constructing auxiliary mean proportional numbers between the squares and cubes, establishing that the intermediate ratio chains are all in the same ratio (since A:B = B:C), and then applying ex aequali (7.14) to conclude D:E = E:F and G:H = H:K. The AI explicitly cites 7.17 and 7.18 to justify each ratio step, while Heath compresses these steps into the phrase 'in manner similar to the foregoing' (referring to 8.12, whose proof uses 7.17 and 7.18 explicitly). The AI also cites CN1 for equality transitivity. Since heath_only is empty and ai_only contains {7.17, 7.18, CN1} which are the propositions Heath invokes implicitly via the reference to 8.12's method, this is a citation-depth difference with the same backbone, yielding G.

### 8.14
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. While the forward direction (if A^2 measures B^2 then A measures B) follows the same backbone in both proofs — establishing a continued proportion via 8.11, applying 8.7 to deduce measurement of the middle term, then concluding via D7.20 — the converse direction diverges. Heath's converse mirrors the forward direction, using the same continued proportion and D7.20 to transfer measurement from sides to squares. The AI instead takes a fundamentally different path for the converse: it applies 7.17 twice to establish that A^2 measures AB (from A:B = A^2:AB) and AB measures B^2 (from A:B = AB:B^2), then concludes by transitivity of divisibility that A^2 measures B^2. This is a valid but structurally different logical backbone that does not pass through the continued proportion reasoning Heath employs, constituting a genuine path difference.

### 8.15
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish a continued proportion between the cube numbers with ratio equal to the sides' ratio (via 8.12), apply 8.7 to show the first term measures the second, then use D7.20 to transfer divisibility from cubes to sides (Part I), with the reverse for Part II. The citation differences are all at the granularity level: the AI adds D7.19 (definition of cube, used for notation setup) and D7.3 (definition of measurement, used to make transitivity of divisibility explicit), while Heath adds 8.11 (the square analogue cited alongside 8.12, but unnecessary since the proposition concerns cubes and 8.12 alone suffices). These are citation-depth differences, not backbone differences, placing this squarely in Case A of Q2.

### 8.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same two-part contrapositive result using identical logical backbones: each part is proved by contradiction via Proposition 8.14. The AI proof (Steps 2 and 3) mirrors Heath's structure exactly, assuming the negation of the desired conclusion, applying 8.14 to derive the contradicted hypothesis, and concluding. The only citation difference is that the AI adds Definition 7.18 (ai_only = [D7.18]) when introducing the notion that square numbers are 'equal multiplied by equal,' which Heath leaves implicit. Since D7.18 is a definitional over-citation and heath_only is empty, this is a pure citation-depth difference with the same key intermediate conclusions, satisfying Case A of Q2.

### 8.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 8.17 are structurally identical and cite exactly the same proposition (8.15). Both proofs establish the biconditional by proving each direction via proof by contradiction: in part 1, assuming the side measures the side leads via 8.15 to the cube measuring the cube, contradicting the hypothesis; in part 2, assuming the cube measures the cube leads via 8.15 to the side measuring the side, contradicting the hypothesis. The citation sets are identical (ai_used = heath_refs = {8.15}), the Jaccard similarity is 1.0, and the key intermediate conclusions match exactly, so this is a perfect match.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish proportionality of corresponding sides from the definition of similar plane numbers, (2) construct a mean proportional by multiplying a side of one number by a non-corresponding side of the other, (3) use properties of multiplication and proportion to show the three numbers are in continued proportion, and (4) conclude the duplicate ratio via V. Def. 9. The citation differences are granularity-level: Heath uses 7.13 (alternation) to rearrange the proportion from C:D::E:F to C:E::D:F, then applies 7.17 twice; the AI extracts the corresponding-sides proportion a:c::b:d directly from the similarity definition and uses 7.17 once and 7.18 once (7.18 being the dual of 7.17 with multipliers swapped). The AI's additional citations (7.19 for verification, CN1, D7.16) are axiom/definition-level over-citations. The key intermediate conclusions — the mean proportional, the continued proportion, and the duplicate ratio — are identical in both proofs.

### 8.19
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 reveals different backbones: Heath constructs plane numbers K=C*D and L=F*G, invokes 8.18 to find a mean proportional M between them, then builds the four-term continued proportion A, N, O, B using additional multiplications by E and H. The AI takes a direct route, constructing C1=a*e*c and C2=d*e*c as explicit mean proportionals, then proving each consecutive ratio equals the common side ratio using 7.17, 7.18, and 7.16 (commutativity). The two constructions produce different intermediate numbers and follow different logical chains: Heath's proof pivots on 8.18 and 7.13 (alternation), while the AI uses 7.19 and 7.16 instead. Since the key intermediates differ and the AI's path is logically valid (Q3 confirmed), this is classified as D.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: they establish the two target numbers as plane numbers with specific sides (D,F and E,G) via 7.33 and 7.20, then prove the sides are proportional (D:E = F:G), and conclude similarity. The difference lies in citation depth for the proportionality step. Heath uses 7.17 twice (to derive D:E = A:C = C:B and F:G = C:B) and then 7.13 (alternation to get D:F = E:G), while the AI derives E*F = D*G from the equalities and applies 7.19 (cross-multiplication converse) to get D:E = F:G directly. The proof-tree containment test confirms this is a depth difference: 7.17 (a heath_only item) appears inside Heath's own proof of 7.19 (an ai_only item), meaning the AI cites 7.19 as a unit while Heath re-derives its internals inline. The AI's additional citations of D7.16 and D7.21 are explicit definitions that Heath uses implicitly. Heath's use of 7.13 is an additional step to restate the proportionality in alternate form, which the AI bypasses by working with D:E = F:G directly for the similarity conclusion. All differences are citation-depth variations around the same logical backbone.

### 8.21
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path. Heath's proof works through VIII.20 (similar plane numbers) by taking the least triple E, F, G in ratio with A, C, D, showing E and G are prime (VIII.3) and hence similar plane numbers, then building up solid number structure from plane number sides using VII.14 (ex aequali), VII.21, VII.18 and VII.20. The AI proof takes a fundamentally different algebraic approach: it repeatedly applies VII.19 and VII.20 to decompose the continued proportion A:C:D:B = p:q step by step, ultimately deriving A = t*p^3 and B = t*q^3, then factors these as products of three numbers to establish solidity and uses VII.17 to show all three pairs of corresponding sides share ratio p:q. The AI never establishes similar plane numbers as an intermediate result and does not use VIII.20, VIII.3, VIII.2, VII.14, VII.18, or VII.21 at all. The AI's chain is logically complete and sound, running from premises to conclusion via a valid but distinct algebraic decomposition route, warranting classification as D.

### 8.22
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: they use 8.20 to establish that A and C are similar plane numbers, then conclude that since A is square, C must also be square. Heath's proof accomplishes this in two sentences, treating the final inference as obvious. The AI proof expands this same inference over six additional steps (Steps 4-8), explicitly citing definitions D7.16, D7.18, D7.21 and lower-level Book 7 propositions 7.16, 7.17, 7.19 to unpack what it means for similar plane numbers with one being square to force the other to be square. All six ai_only citations are sub-steps that elaborate the same conclusion Heath reaches implicitly. With heath_only empty, every citation Heath uses is also present in the AI proof. This is a clear Case A: same backbone, different citation depth.

### 8.23
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that B and C are two mean proportionals between A and D, apply 8.21 to conclude A and D are similar solid numbers, and then conclude D is cube because A is cube. Heath's proof leaves the final inference implicit ('But A is cube; therefore D is also cube'), while the AI explicitly unpacks why a similar solid to a cube must itself be a cube, citing D7.21 (similar solids have proportional sides), 7.13 (alternation of proportion), and D7.20 to show all three sides of D are equal, then D7.19 (definition of cube). These ai_only citations (7.13, D7.19, D7.20, D7.21) represent over-citation of definitions and an elaboration of a step Heath treats as obvious, not a different proof path. heath_only is empty, confirming the AI covers all of Heath's reasoning and more. This is Case A: same backbone, different citation depth.

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish one mean proportional between the two given square numbers, (2) transfer that mean proportional to A and B via 8.8, and (3) conclude B is square via 8.22. The only difference is the citation used in step 1: Heath cites 8.18 (between two similar plane numbers there is one mean proportional) while the AI cites 8.11 (between two square numbers there is one mean proportional). These are two different propositions that both validly establish the same intermediate conclusion for this case, since square numbers are similar plane numbers. The AI chose the more specific result (8.11, tailored to squares) while Heath chose the more general result (8.18, for similar plane numbers). Since the key intermediate conclusions are identical and the difference is only in which valid prior result is cited to justify the same step, this is a citation-depth difference under Case A of Q2.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish that two mean proportionals exist between the given cube numbers in the ratio, (2) use 8.8 to transfer those mean proportionals to A and B, (3) conclude B is cube via 8.23. The only difference is in how step (1) is justified: Heath notes that cubes are similar solid numbers and invokes 8.19 (the general theorem for similar solids), while the AI directly invokes 8.12 (the specific theorem for cubes). These are parallel results that yield exactly the same intermediate conclusion. Since the key intermediate conclusions are identical and only the citation depth differs at a single step, this is a granularity difference. The AI's additional citation of D7.19 (definition of similar solid numbers) is harmless over-citation consistent with G.

### 8.26
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decides this classification. Heath's proof finds the least numbers D, E, F in the same ratio as A, C, B (using 7.33/8.2), shows the extremes D, F are square (8.2), and concludes from D:F = A:B. The AI takes a fundamentally different path: it decomposes the similar plane numbers into their sides (a,b and c,d), establishes the mean proportional via 8.18, uses 8.11 to find the mean proportional between the square numbers a^2 and c^2, then applies 5.11 (transitivity of ratios) and 7.14 (ex aequali) to conclude A:B = a^2:c^2. The two backbones differ in their key intermediate conclusions — Heath works through least numbers in ratio while the AI works through the sides' squares directly. Both paths are logically complete, so the classification is D.

### 8.27
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Heath's proof directly applies VIII.2 to find the least numbers in the continued proportion A, C, D, B and notes that the extremes are cubes, concluding immediately that A:B is a ratio of cubes. The AI proof takes a structurally different path: it extracts the side ratio in least terms p:q (7.33), explicitly constructs cube numbers p^3 and q^3 (D7.19), invokes 8.12 to establish that between these cubes there are two mean proportionals with the same common ratio p:q, then uses 8.2 to find the least four-term continued proportion with ratio p:q, and finally applies CN1 to equate A:B with p^3:q^3. The introduction of 8.12 (between two cube numbers there are two mean proportional numbers) as a key intermediate conclusion is absent from Heath's proof and constitutes a genuinely different logical backbone, not merely a difference in citation depth. The AI's path is logically valid and complete, so Q3(b) holds, yielding classification D.


## Book 9

| Category | Count |
|---|---|
| Perfect match (P) | 3 |
| Granularity difference (G) | 15 |
| Path difference (D) | 16 |
| AI proof error (E) | 2 |

**Total**: 36 propositions

### 9.1
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Heath's proof constructs D = A*A (square), establishes the ratio A:B = D:C via 7.17, transfers the mean proportional from A,B to D,C via 8.8, then applies 8.22 (if three numbers in continued proportion and the first is square, the third is also square). The AI takes a fundamentally different and more direct route: after obtaining mean proportional G between A and B via 8.18 (the one shared citation), it uses 7.19 to conclude that A*B = G*G (since A:G :: G:B implies the product of extremes equals the product of means), and then C = G*G is square by definition. The key intermediate conclusions differ entirely: Heath works through an auxiliary square D and ratio transfer, while the AI directly identifies C as a product of equal factors. Both paths are logically complete, making this a valid path difference (D).

### 9.2
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof introduces D = A*A, establishes A:B = D:C via 7.17, argues D and C are similar plane numbers (both square), uses 8.18 to get a mean proportional between D and C, then transfers that mean proportional to A and B via 8.8, and finally applies 8.20. The AI takes a fundamentally different path: it decomposes C = k*k by the definition of square number (D7.18), observes A*B = k*k, and directly applies the converse of 7.19 to conclude A:k = k:B, establishing k as a mean proportional between A and B without the intermediate auxiliary square D or the transfer via 8.8. Both proofs share only 8.20 as the final step. The AI's path is logically sound — 7.19's converse validly yields proportionality from equal products — but the key intermediate conclusions differ entirely, making this a genuine path difference.

### 9.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof establishes two mean proportionals between the unit and A (using VII. Def. 20), then uses VIII.8 to transfer those mean proportionals to the interval between A and B, and finally applies VIII.23 (if four numbers are in continued proportion and the first is cube, the fourth is also cube) to conclude B is cube. The AI proof takes a fundamentally different route: it uses the elementary proportion results 7.17 and 7.19 to build the continued proportion C:D = D:A = A:E directly, then algebraically derives that B = E*D = D^2*D = D^3, concluding B is cube by definition D7.19. The Jaccard similarity is 0.0 with completely disjoint citation sets, reflecting genuinely different logical backbones. The AI's path is logically valid throughout, with each step correctly following from the cited propositions, so Q3 confirms a valid different path yielding classification D.

### 9.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) A*A = D is cube by 9.3, (2) A:B = D:C by 7.17, (3) two mean proportionals exist between A and B, (4) therefore two mean proportionals exist between D and C by 8.8, (5) D is cube so C is cube by 8.23. The only substantive citation difference is that Heath uses 8.19 (between two similar solid numbers there are two mean proportionals) while the AI uses 8.12 (between two cube numbers there are two mean proportionals). Since cube numbers are similar solid numbers, both propositions yield the same intermediate conclusion at the same logical position — the AI simply chose the more specific result. The AI's additional citations of D7.15 and D7.19 are explicit definition references (over-citation). All key intermediate conclusions are identical, making this a same-backbone, different-citation-depth case (Case A of Q2).

### 9.5
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Heath's proof works by forming D = A*A (cube by 9.3), establishing A:B = D:C via 7.17, using 8.19 to get two mean proportionals between the cubes D and C, transferring those proportionals to A and B via 8.8, then concluding B is cube via 8.23. The AI proof takes a fundamentally different route: it uses 8.12 to place two mean proportionals D, E directly between the cubes A and C, then uses 8.7 to show A measures D, constructs a factor f such that D = A*f, and through ratio arithmetic (7.17, 5.11, 5.9) establishes E = D*f and C = E*f, yielding B = f*f*f, hence B is cube by D7.19. The key intermediate conclusions differ — Heath's backbone pivots on transferring mean proportionals from D,C to A,B and applying 8.23, while the AI explicitly constructs the cube root of B. The only shared citation is 7.17. The AI's path is logically complete with every step properly cited, so this is a valid path difference.

### 9.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof works through proportional number theory, establishing the chain of ratios 1:A = A:B = B:C, then using the similarity of cube numbers (VIII.19) and transfer of mean proportionals (VIII.8) to conclude A is cube via VIII.23. The AI takes a completely different path: it observes that C = A*A is cube by hypothesis, then shows A*A*A is cube by the definition of cube (D7.19), and finally applies Proposition 9.5 (if a cube multiplied by a number produces a cube, then that number is cube) to conclude A is cube. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different -- Heath's intermediates concern proportional relationships and mean proportionals, while the AI's sole intermediate is that A^3 is a cube number. The AI's path is logically valid and complete, making this a genuine path difference (D).

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) the composite number A is measured by some number (D7.13), (2) A can be expressed as a product of two numbers (D7.15), and (3) the final product equals three numbers multiplied together, making it solid. The only difference is that the AI explicitly cites D7.17 (the definition of a solid number) when concluding that the product of three numbers is solid, while Heath simply states the conclusion without citing the definition. Since D7.17 is a definition rather than a substantive proposition, this is a straightforward case of over-citation at the definitional level — the AI is more explicit about which definition warrants the final step. The backbones are identical, and the citation difference is purely one of depth, making this Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: they establish that the 3rd term from the unit is square (by showing the ratio from the unit implies the term equals itself multiplied by itself), the 4th term is cube (by extending the multiplication argument), then use VIII.22 to propagate squareness every two terms, VIII.23 to propagate cubeness every three terms, and combine both results at the 7th term. The only difference is in which definitions are cited: the AI cites D7.18 (definition of square number) and D7.19 (definition of cube number) when concluding terms are square or cube, while Heath cites D7.20 (definition of proportional numbers) when setting up the proportional reasoning. Since the entire symmetric difference consists of definitions rather than substantive propositions, and the key intermediate conclusions and logical structure are identical, this is a citation-depth difference falling under Case A of Q2.

### 9.9
**Category**: AI proof error
**Jaccard**: 0.400
**Analysis**: Proposition 9.9 as proved by Heath contains two cases: (1) if the number after the unit is square, all the rest are square, and (2) if the number after the unit is cube, all the rest are cube. Heath's proof explicitly addresses both cases, using 9.8 and 8.22 for the square case, and 9.8, 9.3, and 8.23 for the cube case. The AI proof only addresses the square case (Steps 1-8) and never mentions cubes at all. This is a genuine missing case under Q1(a): the cube case is entirely absent from the AI proof, not merely compressed or terse. The audit record completes convincingly since the omission is unambiguous — there is no general argument or reference in the AI proof that could cover the cube case.
**Audit Record**: CANDIDATE E — 9.9
  violated_claim : The cube case: 'if the number after the unit be cube, all the rest will also be cube'
  failure_mode   : missing_case
  missing_is     : support
  evidence       : Heath's proof explicitly addresses two cases: 'let A, the number after the unit, be square' and 'Next, let A be cube'. The AI proof text only addresses the square case (Steps 1-8) and never mentions cubes. The heath_only citations 8.23 and 9.3 are precisely the propositions used in the cube case.
  why_not_terse  : This is not brevity — the entire second case (cube) is absent from the AI proof. There is no general argument or reference that covers the cube case.

### 9.10
**Category**: AI proof error
**Jaccard**: 0.500
**Analysis**: The AI proof of 9.10 cites proposition 8.25 to conclude that a number is square (Steps 3, 4, and 5), but 8.25 states 'If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube' -- it concerns cubes, not squares. The correct proposition for the square case is 8.24 ('If two numbers have to one another the ratio which a square number has to a square number, and the first be square, the second will also be square'). Since the AI explicitly cites 8.25 as its warrant and 8.25 does not entail any conclusion about square numbers, this is an invalid inference under Q1(b). The audit record completes convincingly: the missing element is support (not mere expansion), the cited proposition genuinely does not entail the conclusion, and this is not a matter of terseness or compression but of citing the wrong proposition entirely. Heath correctly uses 8.25 only in the cube case and uses 8.26 (converse) for the square case.
**Audit Record**: CANDIDATE E -- 9.10
  violated_claim : "by 8.25, A is also square" (Step 3, and repeated in Steps 4-5)
  failure_mode   : invalid_inference
  missing_is     : support -- 8.25 is about cubes; the AI needs 8.24 (squares) but cites 8.25 (cubes)
  evidence       : AI Step 3: "Since B is square and A has to B the ratio of a square number to a square number, by 8.25, A is also square." Proposition 8.25: "If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube." The AI applies 8.25 to a square-ratio context where it does not apply.
  why_not_terse  : The AI explicitly names 8.25 as the warrant for its conclusion about squares. 8.25 concerns cubes exclusively and cannot justify any conclusion about square numbers. The correct warrant is 8.24, which the AI does not cite.

### 9.11
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 9.11 relies on a single key mechanism: alternation of ratios via 7.15, directly converting the fact that the unit measures D into the conclusion that B measures E according to D. The AI proof takes a fundamentally different path, using the multiplicative structure of geometric sequences beginning from unity. It builds up from showing A multiplied by each term yields the next term (via definitions D7.15 and D7.20), then generalizes to show that for any two terms T_i and T_j with i < j, T_i multiplied by T_{j-i+1} equals T_j, using propositions 7.14 (ex aequali), 7.16 (commutativity of multiplication), 7.17 (ratio preservation), and 8.7. The key intermediate conclusions differ entirely: Heath uses ratio alternation while the AI uses recursive multiplication properties. Since the AI's multiplicative approach is mathematically sound and reaches the correct conclusion through validly cited propositions, this is a valid different path, yielding classification D.

### 9.12
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 determined this classification. Heath's proof uses proof by contradiction, assuming the prime E does not measure A, then descending through the specific chain D to C to B to A-squared using ratio and proportion arguments (7.19, 7.20, 7.21) combined with the coprimality result (7.29), ultimately reaching a contradiction. The AI proof takes a fundamentally different approach: it uses induction on the number of terms in the continued proportion, applying 7.30 (if a prime divides a product it divides a factor) at each step. The AI decomposes L = A*K via 7.19 from the proportion 1:A = K:L, then uses 7.30 to conclude p|A or p|K, descending to shorter sequences until the base case of three terms where B = A*A and 7.30 gives p|A. The key intermediate conclusions differ entirely: Heath establishes E|C, then E|B, then E|A via contradiction; the AI establishes a descent through 7.30 at each level. The proof-tree containment test confirms this is genuine path divergence rather than citation-depth difference: while 7.30 does subsume 7.29, 7.21, and 7.20 from heath_only, the remaining heath_only items 9.11 and 9.8 are not inside Heath's proof of 7.30, and more importantly the overall proof architecture (contradiction vs induction) is different. The AI proof is logically complete under the hardened 1(b) standard, so Q3 confirms category D.

### 9.13
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 reveals fundamentally different backbones. Heath's proof uses an intricate descent argument: assuming E measures D and is not among A, B, C, Heath shows E is composite (via 9.12 and 7.31), that A measures E, then introduces quotient F, proves F is not among A, B, C, and repeats the argument, descending through F, G, H using proportionality (7.19) and 9.11, ultimately reaching a contradiction via 9.8 when H measures A (prime). The AI takes a markedly different path: it shows directly that every prime factor of any divisor C of A_n must equal A_2 (using 9.12 and transitivity via 7.20), concludes C is a power of A_2, observes the proportional numbers are exactly the successive powers of A_2, and applies 9.11 to conclude C must be among them, reaching contradiction immediately. The AI's argument is logically sound throughout: the step from 'only prime factor is A_2' to 'C is a power of A_2' is terse but valid, and the identification of proportional terms as powers of A_2 follows from the definition of continued proportion. This constitutes a genuinely different valid path, not merely a granularity difference, since the key intermediate conclusions (prime-factor characterization vs. descent through quotients) are structurally distinct.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same contradiction structure: assume a prime E distinct from B, C, D measures the least number A measured by B, C, D; deduce A = E*F; apply 7.30 to show B, C, D each measure E or F; eliminate E (since E is prime and distinct); conclude B, C, D measure F; derive contradiction since F < A. The AI proof works through B, C, D individually (Steps 3-7) rather than collectively as Heath does, and explicitly cites definitions (D7.1, D7.3, D7.11, D7.15) and a common notion (CN5) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions and common notions representing over-citation of foundational items, this is Case A (same backbone, different citation depth), yielding G.

### 9.15
**Category**: Path difference
**Jaccard**: 0.556
**Analysis**: Q2 reveals a different backbone between the two proofs. For the first two cases (A+B prime to C and B+C prime to A), Heath uses II.3 to decompose the product FD*DE into the sum DE^2 + DE*EF, whereas the AI directly factors A+B as p*(p+q) without needing any algebraic identity proposition. For the third case (A+C prime to B), Heath uses II.4 to expand DF^2, then applies separando twice to establish that DE^2 + EF^2 is prime to DE*EF, whereas the AI uses proof by contradiction to show p^2+q^2 is prime to p and to q separately, then combines via VII.24. Both approaches are logically complete, but the AI avoids the Book II algebraic identities entirely, substituting direct factoring and proof by contradiction. This constitutes a genuine path difference, not merely a granularity difference, since the key intermediate conclusions differ in structure.

### 9.16
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works entirely within ratio theory: since A,B are coprime they are the least in their ratio (7.21), and least numbers measure proportional numbers equally (7.20), so A measures B, contradicting coprimality. The AI proof takes a fundamentally different route via products: it converts the proportion A:B=B:C into A*C=B^2 using 7.19, then invokes 7.25 to show A and B^2 are coprime, which contradicts A dividing B^2 (forcing A to be a unit). The key intermediate conclusions are entirely different — Heath reasons about least ratios and measuring, while the AI reasons about products, divisibility, and coprimality of squares. This is a genuine backbone difference (Case B). The AI's alternative path is logically complete under Q3, with each step properly supported by cited propositions, so the classification is D.

### 9.17
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses alternation (7.13) to get A:D = B:E, then the coprimality/least-ratio facts (7.21, 7.20) to conclude A measures B, and chains divisibility through the continued proportion (A|B, B|C implies A|C, then A|D) to reach a contradiction with gcd(A,D)=1. The AI takes an entirely different route: it invokes 8.1 to establish the terms are the least in their ratio, then uses 8.2 to express the first and last terms as powers of the base ratio p:q (A_1 = p^(n-1), A_n = q^(n-1)), sets up a cross-multiplication via 7.19, and derives that p divides q^n. Since 7.27 guarantees p^n and q^n are coprime, p must be a unit, making A_1 a unit and contradicting it being a number. The two proofs share zero citations (Jaccard = 0.0) and their key intermediate conclusions are completely different: Heath argues through a divisibility chain along the terms, while the AI argues through the explicit power structure of the least continued proportion. Although the heath_only items 7.20 and 7.21 appear inside Heath's proof of 8.1 (which the AI cites), the AI does not merely subsume Heath's argument under 8.1; rather, 8.1 serves as the launching point for a fundamentally different algebraic strategy. This is a genuine path difference.

### 9.18
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Classification was decided at Q2/Q3. Heath's proof first distinguishes whether A and B are prime to one another, invoking 9.16 to dismiss that case, then handles the non-prime situation by checking whether A measures B-squared. The AI proof omits the prime/not-prime distinction entirely and uses a single exhaustive dichotomy: either A measures B-squared or it does not. This is a genuinely different logical backbone -- Heath has a three-branch structure (prime, not-prime-and-measures, not-prime-and-does-not-measure) while the AI has a two-branch structure (measures, does-not-measure). The AI's approach is valid because the measure/not-measure dichotomy is exhaustive and the prime case is subsumed under the not-measuring case. Both proofs share the core use of 7.19 for the positive case and contradiction for the negative case, but the structural difference in case organization and the AI's omission of 9.16 constitute a different path rather than mere granularity difference. The AI's path is logically complete and sound, yielding classification D.

### 9.19
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof uses a four-case analysis based on whether the three numbers are in continued proportion and whether their extremes are prime to one another, employing 9.17, 7.14, 7.21, and 7.20 to establish impossibility in the prime-extremes cases and 7.19 for the constructive cases. The AI proof takes an entirely different structural approach: it bypasses the case analysis altogether and provides a single unified criterion that a fourth proportional to A, B, C exists if and only if A measures the product B times C. The AI's backbone relies solely on the biconditional in 7.19 (proportionality iff product equality) combined with definitions D7.15 and D7.3 for the measuring relation. Since the key intermediate conclusions differ fundamentally — Heath argues through prime number properties and continued proportion cases while the AI argues through a direct divisibility criterion — this is Case B (different backbone) at Q2, leading to Q3. At Q3, the AI's path is logically complete: each step follows validly, the biconditional is correctly established, and the impossibility direction is proved by clean contradiction. Therefore the classification is D (path difference).

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: take the LCM (or any common multiple) of the assigned primes, add a unit to form a new number, then split into two cases (new number is prime, or new number is composite and measured by some prime G via 7.31). In both cases a contradiction argument shows the new prime cannot equal any of the assigned primes. The AI proof's only divergence from Heath is the explicit citation of six definitions (D5.1, D7.1, D7.11, D7.13, D7.15, D7.3) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, this is a clear case of over-citation at finer granularity with no backbone difference, yielding G.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusion: each even summand has a half part, and the collection of all half parts yields a half of the whole sum, making it even by Definition 7.6. The AI proof makes the 'adding equals to equals' step explicit by citing CN2, while Heath's proof performs the same reasoning implicitly ('so that the whole AE also has a half part'). The sole ai_only citation CN2 is a Common Notion (not a substantive proposition), representing over-citation of a foundational axiom rather than a different logical path. Since the backbones align and the citation difference is purely one of depth, this is a granularity difference.

### 9.22
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Heath's proof decomposes each odd number by subtracting a unit, sums the even remainders (9.21), notes the even count of units, then adds those two even quantities (9.21) to get an even total. The AI proof instead pairs the odd numbers (since their multitude is even, by D7.6), shows each pair of odd numbers sums to an even number (decomposing via D7.7, adding via CN2, concluding evenness via 9.21), then sums the even pair-sums (9.21). These represent genuinely different logical backbones: Heath works by subtract-units-then-recombine while the AI works by pair-then-sum. The ai_only items (CN2, D7.6) are not mere over-citations but reflect the AI's distinct pairing strategy. Since the different path is logically complete under the hardened 1(b) standard, the classification is D.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21, 9.22, and D7.7 are all prior to 9.23). Q1 found no logical defects: the AI proof correctly separates the last odd number from the rest, shows the remaining even-count sum is even via 9.22, decomposes the last odd number into an even number plus a unit via D7.7, combines the even parts via 9.21, and concludes oddness by D7.7. Q2 confirmed both proofs share the same logical backbone: isolate the last odd number, show the partial sum is even, then show adding the last odd number produces an odd total. The citation sets are identical (ai_used = heath_refs = {9.21, 9.22, D7.7}, Jaccard = 1.0), and the key intermediate conclusions match, so the perfect match check assigns category P.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: (1) AB is even so it has a half part, (2) BC is even so it has a half part, (3) the remainder AC therefore also has a half part and is even. The AI proof explicitly cites CN3 (if equals be subtracted from equals, the remainders are equal) to justify deriving that AC consists of two equal parts, while Heath's proof simply states that the remainder also has a half part without citing any common notion. The ai_only set contains only CN3, a Common Notion (axiom-level citation), and heath_only is empty. This is a classic over-citation pattern where the AI makes explicit an axiom that Heath uses implicitly, with no difference in the key intermediate conclusions or logical path.

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 9.25 use identical citation sets (9.24 and D7.7) and argue through the same key intermediate conclusions: decomposing the odd subtrahend into an even number plus a unit via D7.7, applying 9.24 to show that subtracting the even part from the original even number yields an even remainder, and then observing that the final result differs from that even remainder by a unit and is therefore odd by D7.7. Since the logical backbones match and the citation sets are identical (Jaccard 1.0, with empty ai_only and heath_only), this is a perfect match under the protocol's final check.

### 9.26
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI and Heath proofs of 9.26 follow the same logical backbone: subtract a unit from the odd number AB to get even remainder AD (D7.7), establish that CD is also even (D7.7), and conclude that the remainder CA is even by 9.24. The AI proof is more explicit in justifying why CD is even (showing that the unit subtracted from BC yields the same point as the unit subtracted from AB), but this is additional detail, not a different path. The citation sets are identical: both use exactly 9.24 and D7.7, yielding Jaccard 1.0. Since the key intermediate conclusions match and the citation sets are equal, this is a perfect match (P).

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as D (Path difference). Heath proves 9.27 directly: from odd AB, subtract unit AD to get even DB, then since DB and BC are both even, their difference CD is even by 9.24, leaving CA odd by D7.7. The AI instead uses proof by contradiction: assuming the remainder C is even, it applies 9.21 (sum of even numbers is even) to conclude B+C=A would be even, contradicting A being odd. The key intermediate conclusions differ fundamentally — Heath's backbone relies on subtracting a unit and applying 9.24 (even minus even is even) to establish an even intermediate, while the AI's backbone relies on assuming evenness of the remainder and applying 9.21 (sum of evens is even) to derive a contradiction. Since the logical backbones are genuinely different and the AI's proof by contradiction is logically complete and sound, this is a valid different path.

### 9.28
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: (1) express the product C as B added to itself A times via D7.15, (2) observe that since B is even each summand is even, and (3) apply 9.21 to conclude the sum of even numbers is even. The AI additionally cites D7.6 (the definition of even number) when establishing that B and each summand are even, while Heath leaves this implicit. Since heath_only is empty and ai_only contains only a definition (D7.6), this is a straightforward case of over-citation at the definition level, which is a citation-depth difference under Case A of Q2.

### 9.29
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) C is the product of A and B and hence equals a sum of copies of one factor repeated as many times as the units in the other (by Definition 7.15), (2) each summand is odd and the count of summands is odd, and (3) therefore C is odd by Proposition 9.23. The only citation difference is that the AI explicitly cites D7.7 (definition of odd number) to justify calling A and B odd, whereas Heath simply states that A and B are odd without citing the definition. Since D7.7 is a foundational definition and not a substantive proposition, and the logical backbone is identical, this is a citation-depth difference under Case A of Q2, yielding G. The citation sets are not identical (ai_used includes D7.7 which heath_refs does not), so P is ruled out.

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: given odd A measures even B via C, they prove C must be even by contradiction (if C were odd, the product of two odd numbers would be odd, contradicting B being even), then conclude A measures B/2. The only substantive citation difference is that the AI uses 9.29 (product of two odds is odd) while Heath uses 9.23 (sum of an odd count of odds is odd). The proof-tree containment test confirms this is a depth difference: Heath's own proof of 9.29 cites 9.23 as its key step, so the AI is citing 9.29 as a packaged unit while Heath effectively re-derives the reasoning of 9.29 inline using 9.23. The remaining ai_only items (D7.3, D7.6, D7.7, D7.15) are all Book 7 definitions representing over-citation by the AI. This is a citation-depth difference with identical logical backbones, yielding G.

### 9.31
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as Case B (different backbone), leading to Q3. Heath proves 9.31 by contradiction: assuming some D measures both A and C=2B, D must be odd (since it divides odd A), and then by 9.30 an odd divisor of an even number also divides its half, so D divides B, contradicting A and B being coprime. The AI instead gives a direct proof: since A is odd, 2 does not divide A, so by 7.29 (a prime not dividing a number is coprime to it) 2 is coprime to A; since B is coprime to A by hypothesis, 7.24 (the product of two numbers each coprime to a third is coprime to that third) gives that 2B is coprime to A. These are fundamentally different proof strategies with completely disjoint citation sets (Jaccard 0.0), yet the AI's direct proof is logically sound at every step, so Q3(b) holds and the classification is D.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) each number in the doubled-from-dyad sequence is even-times even, (2) by 9.13, the only divisors of any number in the sequence are the preceding terms and the unit, (3) since all those terms are even, no odd number greater than 1 divides any term, so no term is even-times odd, hence each is even-times even only. The AI proof explicitly cites three definitions (D7.6 for even, D7.9 for even-times odd, D7.11 for prime) that Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are definitions providing extra citation depth for the same underlying reasoning, this is a clear Case A: same backbone, different citation depth.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this as G (granularity difference). Both proofs share the same logical backbone: (1) the half of the number is odd, so the number is even-times odd by D7.9; (2) if the number were also even-times even (D7.8), then the half would be measured by an even number, contradicting the half being odd; (3) therefore the number is even-times odd only. The AI proof adds an additional argument (Steps 8-10) ruling out odd-times-odd using 9.29, which Heath does not include, but this supplements rather than replaces the shared backbone. The ai_only set consists of definitions (D7.6, D7.7, D7.10) that Heath uses implicitly without citation, plus 9.29 for the supplementary odd-times-odd argument. The heath_only set is empty, confirming the AI covers all of Heath's reasoning. Since the core backbone is identical and the differences are extra explicit definition citations and an additional thoroughness argument, this is a same-backbone, different-depth situation classifying as G.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: (1) A is even-times even because its half is not odd (citing D7.8), and (2) A is even-times odd because repeated bisection must reach an odd number (proved by contradiction — if not, we reach a dyad and A would be in the doubling sequence from 2, contradicting the hypothesis). The AI proof explicitly cites definitions D7.6 (even), D7.7 (odd), and D7.9 (even-times odd) that Heath uses implicitly, and cites 9.32 to justify the contradiction step where Heath simply states 'A will be among those which are doubled from a dyad' without an explicit citation. All ai_only items (9.32, D7.6, D7.7, D7.9) represent over-citation at a finer granularity, not a different proof path, and heath_only is empty, confirming Case A of Q2.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they apply separando (7.11) to the continued proportion to obtain differences of consecutive terms, use alternando (7.13) to rearrange and establish that all ratio pairs (A(k+1)-Ak):Ak are equal, then apply ratio summation (7.12) to combine all the equal ratios, and finally simplify the resulting telescoping sum to reach the conclusion. The AI proof explicitly cites CN2 and CN3 to justify the telescoping sum simplification, while Heath performs the same simplification by substituting named segments without citing these Common Notions. Since the key intermediate conclusions are identical and the only difference is that the AI over-cites Common Notions for added rigor, this is a granularity difference (G).

### 9.36
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same backbone of key intermediate conclusions: (1) setting up a geometric series in double proportion from unity with prime sum S, (2) using 9.35 to relate the sum to a power of 2, (3) using 9.13 to identify that the divisors of D are exactly the terms of the geometric progression, (4) proving that all divisors of E = S*D are either divisors of D or S times a divisor of D, (5) summing proper divisors to show the total equals E, and (6) concluding perfection by D7.22. The citation differences reflect alternative paths to the same conclusions: Heath uses 7.14 (ex aequali) and 7.19 (proportional products) where the AI uses 7.17 and 7.18 (direct ratio preservation under multiplication), and Heath uses 7.19+7.21+7.20 for the divisor uniqueness argument where the AI uses 7.30 (prime divides product implies divides a factor) more directly. The ai_only definitions (D7.1, D7.3, D7.11, D7.15) are minor overcitations. The Jaccard of 0.312 reflects these citation-level differences rather than structural divergence.


## Book 10

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 89 |
| Path difference (D) | 25 |
| AI proof error (E) | 1 |

**Total**: 115 propositions

### 10.1
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: invoke the Archimedean property (D5.4) to construct a magnitude DE exceeding AB from multiples of C, perform parallel subtraction processes on AB and DE (subtracting more than half from AB at each step), compare the remainders at each stage to show the AB remainder is less than the corresponding DE piece, and conclude the final remainder is less than C. The AI's only additional citation is CN5 (the whole is greater than the part), a Common Notion used explicitly in Step 5 to justify the comparison that Heath performs without explicit citation. Since heath_only is empty and the sole ai_only item is an axiom-level over-citation, this is Case A of Q2: same backbone, different citation depth, yielding a Granularity difference (G).

### 10.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: assume commensurability to derive a common measure, trace that common measure through the anthyphairesis process showing it divides every successive remainder, then reach a contradiction when a remainder smaller than the common measure inevitably appears. The AI proof explicitly cites 10.1 (for the convergence of remainders below the common measure), CN3 (for the subtraction reasoning), D10.1.1 (definition of commensurable), and D5.1 (definition of measure), while Heath's proof uses these same principles entirely implicitly without any explicit citations (heath_refs is empty). Since the key intermediate conclusions are identical and the difference lies solely in the depth of citation, this is Case A of Q2: same backbone, different citation depth.

### 10.3
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: (1) handle the trivial case where one magnitude measures the other, (2) apply the Euclidean algorithm (antanairesis) when it does not, (3) invoke Proposition 10.2 to guarantee termination since the magnitudes are commensurable, (4) show the last nonzero remainder is a common measure by unwinding the chain of subtractions, and (5) show it is the greatest by proving any common measure must divide the last remainder. The AI proof cites additional definitions (D10.1.1, D5.1, D5.2) and common notions (CN2, CN3, CN5) that Heath uses implicitly but does not explicitly cite, while heath_only is empty. This is a classic over-citation pattern where the AI makes foundational references explicit. Since the key intermediate conclusions are identical and the citation differences are entirely axioms and definitions, this is Case A of Q2: same backbone, different citation depth, yielding classification G.

### 10.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: find D = GCM(A,B) via 10.3, show D and C are commensurable, find E = GCM(D,C) via 10.3, prove E measures A,B,C, then prove E is the greatest common measure. The AI proof omits the explicit two-case split (D measures C vs D does not measure C) present in Heath, but this is not an error because the AI's single general argument demonstrably covers both cases — the procedure of finding GCM(D,C) works regardless of whether D directly measures C. The only citation difference is that the AI explicitly cites D10.1.1 (definition of commensurability) where Heath uses the concept implicitly without citation. Since heath_only is empty and ai_only contains only a definition, this is a classic over-citation pattern indicating same backbone at different citation depth, yielding G.

### 10.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determines the classification. Heath's proof establishes proportion via a chain-of-ratios strategy: setting up C:A :: unit:D using VII.Def.20, inverting via V.7, establishing C:B :: unit:E, then composing ex aequali via V.22 to obtain A:B :: D:E. The AI proof takes a fundamentally different approach, working directly from the equimultiple definition of proportion (D5.5 = V.Def.5): after expressing A = mC and B = nC, it uses 5.3 to compute equimultiples sA = (sm)C and tB = (tn)C, then shows via CN5 that the comparison of sm vs tn matches the comparison of sA vs tB, concluding by D5.5. The proof-tree containment test fails because the heath_only items 5.22 and 5.7 do not appear inside the proof of 5.3 (the AI's only theorem citation). Since the backbones differ (ratio-chain composition vs direct equimultiple verification) and the AI's path is logically sound, this is a path difference.

### 10.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: divide A into D equal parts to get C, construct a magnitude equal to E copies of C, establish that A has the same ratio to this constructed magnitude as D has to E, apply V.11 (transitivity of ratio equality) and V.9 (equal ratios imply equal magnitudes) to conclude B equals the constructed magnitude, then conclude C measures both A and B. The difference lies in how the ratio A:(E copies of C) = D:E is established: Heath chains through V.7 (inversion) and V.22 (ex aequali), while the AI proves D*C : E*C = D:E directly from the definition of same ratio (D5.5). The ai_only citations are all definitions (D10.1.1, D5.1, D5.2, D5.5), indicating over-citation, and the heath_only citations (5.22, 5.7) are substantive propositions that Heath uses to establish the same intermediate conclusion the AI reaches by a more direct definitional route. Since the key intermediate conclusions are identical and only the citation depth differs, this is a granularity difference.

### 10.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: assume for contradiction that incommensurable magnitudes A and B have a ratio equal to a ratio of numbers, apply Proposition 10.6 to conclude A and B are commensurable, note the contradiction with the hypothesis, and conclude the assumption is false. The only citation difference is that the AI explicitly cites Definition D10.1.1 (definition of incommensurable magnitudes) when invoking the hypothesis, while Heath leaves this implicit. Since D10.1.1 is a definition rather than a substantive proposition, this constitutes over-citation at a different level of granularity, not a path difference. The key intermediate conclusions are identical in both proofs, so this is a granularity difference (G).

### 10.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the identical logical backbone: a proof by contradiction assuming commensurability, applying 10.5 to derive that A and B would have a numerical ratio, contradicting the hypothesis, and concluding incommensurability. The only citation difference is that the AI explicitly cites D10.1.1 (the definition of commensurable/incommensurable magnitudes) while Heath leaves the definitional reference implicit. Since ai_only contains only a definition and heath_only is empty, this is a pure citation-depth difference with the same key intermediate conclusions, yielding Granularity difference (G).

### 10.9
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions across all four parts of the proposition: (I) using 10.5 to get a numerical ratio, then 6.20 and 8.11 to show the squares have the duplicate ratio which equals a square-number-to-square-number ratio; (II) reversing the argument using 6.20 and 8.11 to extract the numerical ratio, then applying 10.6; (III) and (IV) proving the incommensurable cases by contradiction using Parts II and I respectively. The sole citation difference is that the AI explicitly cites Definition 7.18 (the definition of square numbers) when justifying that m-squared and n-squared are square numbers, whereas Heath leaves this definitional fact implicit. This is a pure over-citation of a definition, which is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 10.10
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 determines the classification. Both proofs establish the same two key conclusions: (1) a line commensurable in square but incommensurable in length with the assigned line, and (2) a line incommensurable in square via a mean proportional. However, the construction methods differ substantively. Heath uses abstract numbers not in square-to-square ratio with X.6 (porism) to construct the first line, while the AI uses a specific geometric construction via the Pythagorean theorem (1.47) to produce a line whose square is twice the assigned square. For the second line, Heath applies X.11 (proportional commensurability transfer) and V. Def. 9 (duplicate ratio) directly, while the AI re-derives the result using 6.17, 6.1, 10.7, and 10.8. The use of 1.47 is a substantive proposition argued in the AI proof but entirely absent from Heath's, which causes Case A (same backbone) to fail under the protocol's requirement that no ai_only/heath_only substantive fact be argued in one proof but absent from the other. This makes the proofs Case B (different backbone). The AI's path is logically complete under Q3 since every step is supported by a valid citation, yielding classification D.

### 10.11
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the identical two-case structure: (1) A commensurable with B implies A:B is a ratio of numbers (10.5), which transfers via the given proportion to C:D, yielding C commensurable with D (10.6); (2) A incommensurable with B implies A:B is not a ratio of numbers (10.7), which again transfers to C:D, yielding C incommensurable with D (10.8). The key intermediate conclusions are the same in both proofs. The only difference is that the AI explicitly cites definitions D5.5, D5.6 (proportion) and D10.1.1 (commensurability) that Heath invokes implicitly. Since ai_only consists entirely of definitions and heath_only is empty, this is a citation-depth difference with the same logical backbone, yielding G.

### 10.12
**Category**: AI proof error
**Jaccard**: 0.500
**Analysis**: Q1(b) decides: the AI proof commits an invalid inference when applying 5.22 (ex aequali) in Step 8. The AI establishes A:C :: pm:np and C:B :: nq:np, then claims that 5.22 yields A:B :: pm:nq. However, 5.22 requires matching middle terms -- the second term of the first ratio must equal the first term of the second ratio. Here the second term of A:C is np and the first term of C:B is nq; since p and q are generally distinct, np != nq and 5.22 is inapplicable. Moreover, the claimed result A:B = pm:nq is arithmetically incorrect (the correct ratio would be mq:np). The AI's strategy of using 7.17 to multiply numerators and denominators fails to produce the common middle term that Heath achieves via 8.4. This is not a matter of terseness or compression -- the cited proposition genuinely does not entail the claimed conclusion from the given premises.
**Audit Record**: CANDIDATE E -- 10.12
  violated_claim : A:B :: pm:nq (Step 8)
  failure_mode   : invalid_inference
  missing_is     : support -- 5.22 does not entail A:B :: pm:nq from A:C :: pm:np and C:B :: nq:np because the middle terms (np vs nq) do not match
  evidence       : Step 8: 'We now have A:C :: pm:np and C:B :: nq:np... By Proposition 5.22 (ex aequali), A:B :: pm:nq.' Proposition 5.22 requires A:C :: pm:X and C:B :: X:nq with matching middle term X. Here the middle terms are np (from A:C) and nq (from C:B), which are unequal when p != q.
  why_not_terse  : This is not brevity -- the ratios as stated have non-matching middle terms (np vs nq), making 5.22 structurally inapplicable. The resulting ratio pm:nq is arithmetically incorrect (A/B = (m/n)*(q/p) = mq/np, not pm/nq).

### 10.13
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume B is commensurable with C for contradiction, apply 10.12 (magnitudes commensurable with the same magnitude are commensurable with one another) to derive that A is commensurable with C, note the contradiction with the given incommensurability of A and C, and conclude B is incommensurable with C. The only difference is that the AI explicitly cites D10.1.1 (the definition of commensurable and incommensurable magnitudes) at each step where those concepts are invoked, while Heath uses the definition implicitly without citation. Since the key intermediate conclusions are identical and the ai_only set contains only a definition citation, this is a same-backbone, different-citation-depth situation, yielding G.

### 10.14
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) sq(A):sq(B) :: sq(C):sq(D) via 6.22, (2) sq(E):sq(B) :: sq(F):sq(D) via separando 5.17, (3) E:B :: F:D via 6.22, (4) A:E :: C:F, and (5) application of 10.11 for both the commensurable and incommensurable cases. The sole substantive difference is how conclusion (4) is reached: Heath uses the inverse proportion and then ex aequali (5.22) to combine A:B::C:D with B:E::D:F into A:E::C:F, while the AI uses alternando (5.16) on both proportions to get A:C::B:D and E:F::B:D, equates them via CN1, then applies alternando again to obtain A:E::C:F. Since the key intermediate results are identical and only the sub-derivation technique for one step differs, this is Case A (same backbone, different citation depth). The ai_only items 1.47, 5.14, and CN1 are over-citations of construction and auxiliary facts that Heath leaves implicit. The AI's use of 5.16 instead of Heath's 5.22 represents a different but equivalent micro-level technique to reach the same conclusion, confirming a granularity difference.

### 10.15
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same two-part logical backbone: Part 1 finds a common measure of the two summands and shows it measures the whole, establishing commensurability of the whole with each part; Part 2 finds a common measure of the whole and one summand and shows it measures the remainder, establishing commensurability of the original magnitudes. The AI proof is more explicit about the underlying arithmetic, citing D5.2 (definition of measure as multiple), CN2 (combining multiples under addition), CN3 (subtraction of equals), and CN5 (whole greater than part), whereas Heath leaves these foundational steps implicit and cites only D10.1.1. Since heath_only is empty and ai_only contains exclusively Common Notions and Definitions (axiom-level items), this is a clear case of the AI over-citing foundational axioms while following the same logical path — a citation-depth difference, not a path difference.

### 10.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: a proof by contradiction for each part of the biconditional, where assuming commensurability (or a common measure) where incommensurability was hypothesized leads to a contradiction. Heath derives the intermediate commensurability conclusion directly from the definition of a common measure (showing a measure of the whole and one part also measures the remainder), citing only D10.1.1. The AI instead cites 10.15 (the commensurable counterpart of 10.16) to establish the same intermediate conclusions in a single step. Since heath_only is empty and ai_only contains only 10.15, and the AI's citation of 10.15 packages the same reasoning Heath performs inline, this is Case A: same key intermediate conclusions, different citation depth. The AI operates at a higher level of abstraction by invoking the previously proved 10.15 rather than re-deriving its content from definitions.

### 10.17
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) construct the application of areas dividing the greater line into two segments, (2) use II.5 to establish that sq(greater) - sq(less) = sq(difference of segments), (3) prove in the forward direction that commensurability of the segments implies commensurability of the difference with the whole via a chain of X.15, X.6, X.12, and (4) prove the converse by reversing the commensurability chain. The AI proof cites all four of Heath's references (2.5, 10.6, 10.12, 10.15) plus six additional ones (6.28 for the construction, 6.1 and 6.22 for the scaling-by-four step, CN2 and CN3 for arithmetic, and 10.5 for the halving argument in the converse). Since heath_only is empty and all extra AI citations represent finer-grained justification of steps that Heath performs implicitly, this is a same-backbone, different-depth situation, yielding Granularity difference (G).

### 10.18
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Q2 reveals different backbones in the incommensurability chain. Heath's proof references 10.17 for the shared construction and then establishes BC incommensurable with FD via the chain: BD incomm. DC implies BC incomm. CD (10.16), DC commensurable with sum(BF, DC) (10.6), BC incomm. sum(BF, DC) (10.13), BC incomm. FD (10.16) -- pivoting on the sum (BF + DC) as the key intermediary. The AI re-derives the construction explicitly (citing 1.10, 2.5, CN2, CN3) and uses a different logical chain: BD incomm. DC implies BC incomm. BD (10.16), BC commensurable with BE (10.6), BE incomm. BD (10.13), BE incomm. ED (10.16 converse), then 2ED incomm. 2BE = BC via ratio doubling (5.15, 10.11) -- pivoting on BE as the key intermediary and using ratio preservation for the doubling step. Both chains are logically complete and reach the same conclusion via genuinely different intermediate steps, so this is a valid path difference (D).

### 10.19
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish that a reference square is rational, (2) use VI.1 to set up a proportion between the rectangle and the square, (3) conclude the rectangle is commensurable with the rational square, hence rational. The key difference is citation depth. Heath cites X.11 as a single unit to transfer commensurability through the proportion, while the AI decomposes this into its constituent parts X.5 (commensurable implies number ratio) and X.6 (number ratio implies commensurable), which are exactly the propositions used inside Heath's proof of X.11. The AI's additional citation of X.12 handles an extra transitivity step arising from routing through the assigned rational line C rather than working directly with the constructed square, and D10.1.3 is a definitional citation the AI makes explicit. The proof-tree containment test confirms that heath_only item 10.11 contains the ai_only items 10.5 and 10.6, establishing this as a citation-depth difference rather than a path difference.

### 10.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as Granularity difference (G). Both proofs share the same logical backbone: they establish that the applied rational area and the square on the rational line are commensurable, use VI.1/6.1 to obtain a proportion relating the breadth to the line, and conclude that the breadth is commensurable in length with the line and hence rational. The sole substantive citation difference is that Heath cites 10.11 (if proportional magnitudes have one pair commensurable, the other pair is commensurable) as a single unit, while the AI breaks this down into its component steps 10.5 (commensurable magnitudes have number-to-number ratio) and 10.6 (number-to-number ratio implies commensurability), which are exactly the propositions used inside Heath's own proof of 10.11. This satisfies the proof-tree containment test: heath_only item 10.11 contains the ai_only items 10.5 and 10.6, confirming a citation-depth difference rather than a path difference. The remaining ai_only items (D10.1.2, D10.1.3, 10.12) are definitional expansions and an explicit transitivity citation for steps Heath leaves implicit.

### 10.21
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that the ratio of the square on a rational line to the rectangle equals the ratio of the two lines (via 6.1), deduce incommensurability of the square and rectangle, conclude the rectangle is irrational since the square is rational, and then conclude the side of the equal square is irrational. The key difference is that Heath cites 10.11 to pass from proportional incommensurability to area incommensurability in one step, while the AI breaks this into its constituent parts by citing 10.7 (incommensurable magnitudes do not have a number-to-number ratio) and 10.8 (magnitudes without such a ratio are incommensurable). The proof-tree containment test confirms this is a depth difference: Heath's own proof of 10.11 explicitly uses 10.7 and 10.8 internally. The AI's additional citations of 6.13, 6.17, D10.1.2, and D10.1.3 represent further over-citation where the AI explicitly constructs the mean proportional and cites definitions that Heath leaves implicit. Same backbone, different citation depth yields G.

### 10.22
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 decides the classification. Both proofs establish the same rationality conclusion through a similar backbone (setting up sq(A) = rect(E,F) = rect(B,C), deriving a proportion via 6.14/6.16, squaring via 6.22, and transferring commensurability via 10.11). However, the incommensurability arguments diverge substantially. Heath establishes that sq(EF) is incommensurable with rect(FE,EG) via the Lemma and 10.11, then uses 10.13 to transfer this through commensurable intermediates (sq(CD) comm. sq(EF), rect(DC,CB) comm. rect(FE,EG)) to conclude sq(CD) incomm. rect(DC,CB), and finally converts back to length incommensurability. The AI instead uses 6.1 to directly relate rect(B,C)/sq(B) to C/B, then argues that rect(B,C) (being medial/irrational) is incommensurable with sq(B) (being rational), concluding C is incommensurable in length with B via 10.11. This is a genuinely different logical route: the AI avoids 10.13 entirely and uses 6.1 (not cited by Heath) as the pivotal step. Under Q3, the AI's alternative path is logically valid, yielding classification D.

### 10.23
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: apply rectangular areas equal to sq(A) and sq(B) to a rational line CD, producing breadths; establish the first breadth is rational and incommensurable in length with CD via 10.22; show the squares on A and B are commensurable, hence the breadths are commensurable via 6.1 and 10.11; conclude the second breadth is rational and incommensurable with CD via 10.13; then apply 10.21 to conclude B is medial. The AI adds three extra citations (10.9, 10.6, 10.12) that provide more granular justification for steps Heath treats as immediate: 10.9 and 10.6 spell out why commensurability in length implies commensurability of squares, and 10.12 explicitly justifies that CF is rational because it is commensurable with the rational CE. These are citation-depth differences, not backbone differences, so the classification is G.

### 10.24
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same backbone: (1) sq(A) is medial since A is medial, (2) rect(A,B) is commensurable with sq(A) because A and B are commensurable in length, (3) therefore rect(A,B) is medial. The difference lies entirely in citation depth. Heath invokes X.23 ('a straight line commensurable with a medial straight line is medial') as a packaged unit to go from step 2 to step 3. The AI instead re-derives the content of X.23 inline, introducing a rational reference line and applying areas to it, citing X.22, X.11, X.13, and X.21 -- all of which appear inside Heath's proof of X.23. The proof-tree containment test confirms this: the AI's additional citations (10.22, 10.13, 10.21) are the internal machinery of 10.23, and the AI's use of 10.5 and 10.6 is an alternative method for establishing the commensurability sub-step that Heath handles by direct geometric reasoning (AB=BD). The key intermediate conclusions are the same in both proofs, with the AI simply operating at finer granularity.

### 10.25
**Category**: Path difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Heath's proof applies three rectangles (squares on AB, BC and rectangle AC) to rational line FG, producing breadths FH, HK, KL in a straight line, then establishes the mean proportional FH:HK = HK:KL (using V.11 and VI.1), applies VI.17 to get FH*KL = HK^2, concludes HK is rational, and splits on HK's commensurability with FG. The AI proof instead applies only two rectangles (square on A and rectangle A*B) to rational line C, producing breadths D and E, then uses an entirely different route through duplicate ratios (6.20) to show D and E are commensurable in square, establishes E is rational via D10.1.3, and splits directly on C's commensurability with E. The mean proportional backbone (V.11, VI.17) central to Heath is absent from the AI proof, and the duplicate ratio backbone (6.20) central to the AI is absent from Heath. These represent genuinely different logical paths to the same conclusion. The AI's path is logically complete: every step is supported by valid citations and the chain runs from premises to conclusion without gaps.

### 10.26
**Category**: Path difference
**Jaccard**: 0.188
**Analysis**: Q2 reveals fundamentally different backbones. Heath derives the contradiction by showing EH is both rational and irrational: he establishes EG incommensurable with GH (10.13), then via proportions (10.11) and commensurability properties (10.6, 10.13, 10.16) shows the square on EH (expanded via 2.4) is incommensurable with the rational sum of squares on EG and GH, making EH^2 irrational. The AI instead factors p^2 - q^2 = (p+q)(p-q) via 2.1, then uses repeated applications of 10.20 and 10.12 to show p+q is commensurable in length with e, which forces p itself to be commensurable in length with e, contradicting the established incommensurability of p with e. Both proofs are logically complete proofs by contradiction using the same initial setup (applying medial areas to a rational line), but they pursue entirely different intermediate conclusions to reach the contradiction. The low Jaccard (0.188) and large symmetric difference with substantive propositions on both sides (heath_only: 10.11, 10.13, 10.16, 10.6, 2.4; ai_only: 10.12, 10.15, 10.21, 2.1) confirm the path divergence. The AI proof was verified step-by-step and found sound under Q1 and Q3(b).

### 10.27
**Category**: Granularity difference
**Jaccard**: 0.467
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) start with two rational lines commensurable in square only, (2) take a mean proportional to get a medial line, (3) use a fourth proportional to get a second line, (4) show both lines are medial and commensurable in square only, and (5) show their rectangle equals the square on a rational line, hence is rational. The AI proof adds explicit construction of the initial rational lines via 10.10 (Heath simply 'sets out' them), provides more granular justification for commensurability in square using 10.5, 10.6, and 6.20 (where Heath relies more directly on 10.11), and cites definitions D10.1.2, D10.1.3, D10.1.4 and CN1 that Heath leaves implicit. Since heath_only is empty (all Heath citations appear in the AI set) and the ai_only items are all over-citations providing deeper justification for the same key intermediate conclusions, this is a clear Case A granularity difference.

### 10.28
**Category**: Path difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Heath's proof constructs medial lines D and E by taking D as the mean proportional of A,B and arranging B:C = D:E, then uses 10.11 to transfer commensurability in square and 10.23 (addition) to show E is medial, and finally shows rect(D,E) = rect(A,C) is medial by direct proportion alternation (V.16) and VI.16. The AI proof takes a fundamentally different route: it constructs three rational lines A, B, C using specific number ratios with carefully chosen non-square-ratio properties, forms mean proportionals G (of A,B) and H (of B,C) as the medial lines, and then proves their rectangle is medial by contradiction -- assuming rect(G,H) is rational leads via 10.20 to K being commensurable in length with B, which contradicts the number-theoretic result (via 7.17, 8.11) that sq(B):sq(K) is not a square ratio. The logical backbones are genuinely different: Heath uses proportion transfer (10.11) and the 10.23 addition, while the AI uses number theory (7.17, 8.11), 10.25 classification, and proof by contradiction. Both paths are logically valid and complete, so the classification is D.

### 10.29
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) two rational lines are found, (2) they are shown incommensurable in length via 10.9, (3) they are commensurable in square, making them rational commensurable in square only, (4) the ratio of the square on the greater to the square on the excess is a ratio of square numbers, and (5) the greater is commensurable in length with the line representing the excess. The proofs differ in construction method: Heath uses a semicircle construction requiring 3.31 (angle in semicircle) and 1.47 (Pythagorean theorem) to geometrically establish sq(BF) = sq(BA) - sq(AF), while the AI works directly with specific numbers (9 and 4) and algebraically defines sq(C) = sq(A) - sq(B) without geometric construction. The AI cites 5.17 (separando) and definitions D10.1.2 and D10.1.3 that Heath omits. These citation differences reflect different construction granularity rather than different backbone conclusions, placing this firmly in Case A of Q2 as a granularity difference.

### 10.30
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) establish two rational straight lines commensurable in square only, (2) derive the ratio relationship involving the difference of squares and show it is not the ratio of a square number to a square number, (3) conclude incommensurability of the difference line with the greater. The difference lies in how the ratio involving the difference of squares is established: Heath uses a semicircle construction with III.31 (angle in semicircle is right) and I.47 (Pythagorean theorem) along with V.19 (convertendo), while the AI works purely with ratio manipulation using V.17 (separando) and avoids the geometric construction entirely. The AI also explicitly cites D10.1.3 for rationality of the second line. These are citation-depth differences in reaching the same backbone conclusions, placing this in Case A of Q2, yielding G.

### 10.31
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: set out rational lines A, B via 10.29, construct C as mean proportional so sq(C) = rect(A,B) making C medial (10.21), construct D so A:B = C:D, establish C and D are commensurable in square only (10.11), show D is medial, show rect(C,D) is rational (equals sq(B)), and conclude sq(C) > sq(D) by a commensurable square (10.14). The key difference is citation depth: Heath invokes 10.23 (addition) directly to conclude D is medial from C being medial and C,D commensurable in square, while the AI re-derives the content of 10.23 from first principles in Steps 5-9, citing the subsidiary propositions 6.22, 10.12, 10.11, 10.22, 10.13, and 10.21 that appear inside Heath's proof of 10.23. The proof-tree containment test confirms that the heath_only item 10.23 is subsumed by the AI's inline re-derivation. The other heath_only item 10.30 appears only in Heath's closing remark about the analogous incommensurable case, which is not part of the core proof. The ai_only items are either construction references (6.12, 6.13), definition references (D10.1.4), or parts of the 10.23 re-derivation, all consistent with greater citation depth rather than a different path.

### 10.32
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same logical order: (1) three rational lines A, B, C commensurable in square only with the right square-difference property via 10.29, (2) D is medial because sq(D) = rect(A,B) is medial by 10.21, (3) the ratio A:C = D:E is established, (4) D and E are commensurable in square only via 10.11, (5) E is medial, (6) rect(D,E) is medial because it equals rect(B,C) which is medial by 10.21, and (7) the square-difference property transfers by 10.14. The citation differences reflect depth rather than backbone divergence: the AI proves E is medial through the definition D10.1.4 and transitivity of incommensurability (10.13) instead of Heath's direct appeal to 10.23 (commensurable with medial is medial), and the AI cites finer-grained proportional reasoning steps (6.1, 6.12, 6.22, 5.9) and commensurability characterizations (10.5, 10.6, 10.10, 10.12) that Heath leaves implicit. Heath's citations 6.4, 6.8, 6.16, 6.17 belong to an appended Lemma not part of the 10.32 proof proper, and 10.30 appears only in Heath's remark about the incommensurable variant case. The low Jaccard (0.200) reflects extensive citation-depth differences while the underlying logical backbone remains the same.

### 10.33
**Category**: Path difference
**Jaccard**: 0.174
**Analysis**: Q2 reveals a different backbone in how the two proofs establish that the rectangle contained by the constructed lines is medial. Heath shows rect(AE,EB) = sq(EF) = sq(BD), derives BC = 2*FE, concludes rect(AB,BC) is commensurable with rect(AB,EF), then applies 10.23 (a line commensurable with a medial line is medial) to transfer medialness. The AI instead shows GE is commensurable in length with BC via 10.9, derives that AB and GE are rational commensurable in square only using 10.12, applies 10.21 directly to rect(AB,GE) to establish medialness, then equates rect(AG,GB) = rect(GE,AB) via 6.16. These are genuinely different intermediate conclusions, not merely different citation depths. The AI's path is logically valid (Q3 confirmed), so the classification is D.

### 10.34
**Category**: Path difference
**Jaccard**: 0.042
**Analysis**: The classification is decided at Q2/Q3. Heath's proof uses a semicircle construction (10.31, 3.31) with application of areas (6.28) to find lines AD, DB in the semicircle, establishing incommensurability of squares via 10.11 and 10.18, the medial sum via the semicircle angle property (3.31) and Pythagoras (1.47), and the rational rectangle via a doubling argument with 10.6. The AI proof takes a fundamentally different algebraic approach: it constructs lines p, q with p^2 = 3r^2 and q^2 = 2r^2, defines a = p+q and b = p-q, uses 2.5 to establish rect(a,b) = r^2, then constructs X and Y with X^2 = r*a and Y^2 = r*b. The AI proves the sum of squares is medial via 10.21, the rectangle is rational through a mean proportional argument using 6.17, and incommensurability in square through a proof by contradiction using 10.7, 10.8, 10.15, and 10.12. The two proofs share only citation 1.47 (Jaccard = 0.042), and their key intermediate conclusions are entirely different: semicircle geometry vs. explicit numerical ratios and algebraic identities. This is a clear Case B (different backbone) at Q2. The AI's different path is logically complete and valid under the Q3 assessment, yielding classification D.

### 10.35
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: start with two medial straight lines commensurable in square only containing a medial rectangle with the square on the greater exceeding the square on the less by a line incommensurable with the greater, then use a semicircle construction with a perpendicular to produce two lines that are incommensurable in square, whose sum of squares is medial, whose rectangle is medial, and whose sum of squares is incommensurable with their rectangle. The sole heath_only citation (10.32) is a higher-level proposition that bundles the initial construction; the AI decomposes this into 10.28 (medial lines with medial rectangle) plus 10.18 (incommensurability condition) plus 10.10 (auxiliary construction). The proof-tree containment test confirms this: Heath's proof of 10.32 and its attached Lemma internally use 10.21, 10.23, 6.8, 6.17, and other propositions that appear in the AI's ai_only set, showing the AI re-derives at finer granularity what Heath cites as a unit. The remaining ai_only items are construction steps (1.11, P1), definitions (D10.1.2, D10.1.4), common notions (CN1), and explicit sub-steps (6.1, 6.8, 6.17, 2.14, 10.6) that Heath leaves implicit. All key intermediate conclusions match between the two proofs.

### 10.36
**Category**: Path difference
**Jaccard**: 0.364
**Analysis**: Q2 determined the classification. Heath proves the irrationality of AC directly by building an incommensurability chain: using 10.11 to show rect(AB,BC) is incommensurable with sq(BC), then 10.13 to show 2*rect(AB,BC) is incommensurable with sq(AB)+sq(BC), and 10.16 to show sq(AC) is incommensurable with the rational sum sq(AB)+sq(BC). The AI instead uses a proof by contradiction: it invokes 10.21 to establish that rect(AB,BC) is medial (irrational), then assumes AC is rational and derives that rect(AB,BC) would have to be rational (using 10.12 for transitivity of commensurability), contradicting its mediality. The key intermediate conclusions differ fundamentally: Heath never uses 10.21 or proof by contradiction, and the AI never establishes the incommensurability chain through 10.11, 10.13, and 10.16. The containment test confirms this is a genuine path difference since heath_only items 10.13 and 10.16 do not appear inside the proof of 10.21 (the AI's key differentiating citation). The AI's contradictory path is logically valid, so the classification is D.

### 10.37
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 decides this classification as D (path difference). Heath proves 10.37 by a direct argument: he shows that the squares on AB, BC are incommensurable with twice the rectangle AB, BC (referencing the argument pattern from 10.36), then uses componendo and 10.16 to conclude that the square on AC is incommensurable with the rational rectangle AB, BC, hence irrational. The AI takes a fundamentally different route via contradiction: it first establishes that the sum of squares AB^2 + BC^2 is irrational (since it is commensurable with the medial/irrational AB^2, using 10.15), then separately establishes that 2*rect(AB,BC) is rational, and finally argues by contradiction that if AC^2 were rational then the difference AC^2 - 2*rect(AB,BC) = AB^2 + BC^2 would also be rational, contradicting its irrationality. The key intermediate conclusions differ: Heath's backbone centers on incommensurability of squares-sum with double-rectangle (direct), while the AI's backbone centers on irrationality of the squares-sum and a reductio ad absurdum. Both proofs are logically complete, but they reach the conclusion through genuinely different logical paths, warranting classification as D.

### 10.38
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided this classification. Both proofs establish identical key intermediate conclusions: (1) the sum of squares and twice the rectangle are each medial areas, (2) the corresponding widths DH/DG and HG/GM are rational and incommensurable with DE, (3) the square on AB is incommensurable with the rectangle AB,BC, (4) the sum of squares is incommensurable with twice the rectangle, (5) the two widths are incommensurable in length hence commensurable in square only, (6) their sum is irrational by 10.36, and (7) AC is irrational. The citation differences are purely granularity: the AI over-cites by including 10.12 (transitivity of commensurability), 10.23 (commensurable with medial is medial), and definitions D10.1.2 and D10.1.3 as explicit intermediate steps that Heath leaves implicit, while Heath cites 1.44 for the parallelogram application construction that the AI performs without citation. Same backbone, different citation depth yields G.

### 10.39
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) twice the rectangle AB,BC is medial, (2) twice the rectangle is incommensurable with the sum of the squares on AB and BC, (3) by 10.16 the square on AC is incommensurable with the sum of the squares, and (4) the square on AC is irrational so AC is irrational. The citation differences are entirely at the granularity level. The AI explicitly cites 2.4 for the algebraic identity sq(AC) = sq(AB) + sq(BC) + 2*rect(AB,BC), which Heath uses without citation. The AI uses 10.13 (transitivity of incommensurability) in place of Heath's 10.23 (a line commensurable with a medial line is medial) to establish that twice the rectangle is medial, but both reach the same conclusion. Heath cites 10.33 as the existence reference for the given configuration, which the AI omits as it simply states the hypotheses. Heath cites 10.23 to conclude twice rect is medial; the AI reaches this same conclusion via 10.6 and 10.13. Since 10.13 appears within Heath's proof of 10.23, this is a citation-depth difference. All backbone conclusions match, making this a granularity difference.

### 10.40
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification as D (path difference). Heath's proof is direct: since the sum of squares on AB, BC is medial and twice the rectangle AB, BC is rational, these two areas are incommensurable; by 10.16, when incommensurable magnitudes are added, the whole (AC^2) is incommensurable with each summand, so AC^2 is incommensurable with twice the rectangle; since twice the rectangle is rational, AC^2 is irrational, hence AC is irrational. The AI proof instead uses a contradiction approach: it first establishes that 2*AB*BC is rational (via 10.6 and 10.12), then uses 2.4 to decompose AC^2, and assumes AC is rational to derive that the sum of squares would be rational, contradicting the medial hypothesis. The AI then additionally (and unnecessarily) rules out AC^2 being medial via 10.26. The two proofs have fundamentally different backbones: Heath's key intermediate conclusion is that AC^2 is incommensurable with twice the rectangle (via 10.16), while the AI never establishes this, instead arguing by contradiction through the assumption that AC is rational. The AI's path is logically valid under Q3, yielding classification D.

### 10.41
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: set out a rational line DE, apply areas equal to the sum of squares and twice the rectangle to produce breadths DG and GK/GF, show both breadths are rational and incommensurable with DE via 10.22, show the breadths are incommensurable with each other via 6.1 and 10.11, conclude the sum is binomial by 10.36 and hence irrational, then conclude AC is irrational. The heath_only citation 10.35 is merely the construction reference for the given conditions, which the AI states directly without citing. The ai_only citations 10.23 (justifying that twice a medial area is medial) and 10.20 (used contrapositively to establish irrationality of the area in the final step, where Heath simply invokes X. Def. 4) represent over-citation and a slightly more elaborate final step, but the key intermediate conclusions and logical structure are identical throughout.

### 10.42
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume a second division of the binomial line, apply II.4 to express the square on the whole line two ways, rearrange to show that a difference of rational areas equals a difference of medial areas, and invoke X.26 to reach a contradiction. The AI proof is more verbose, explicitly citing 10.15 to establish that sums of squares are rational (which Heath states without citation), and adding an extended argument (Steps 12-19) handling the case where the difference is zero. Heath's proof includes a preliminary argument that AC is not the same as DB and that C, D are not equidistant from the bisection point, which the AI omits, but these are not essential to the main contradiction. The ai_only set consists entirely of over-citations: definitions (D10.1.2, D10.1.3, D10.1.4), common notions (CN1, CN2, CN3), an intermediate proposition (10.15), a proposition Heath uses in text but omits from refs (10.26), and a construction proposition (2.7) used in supplementary steps. Heath_only is empty. The core intermediate conclusions are the same, making this a granularity difference.

### 10.43
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume AB is divided at two points C and D into first bimedial terms, establish that the difference between the sums of squares (AC^2+CB^2 vs AD^2+DB^2) equals the difference between the doubled rectangles (2*rect(AD,DB) vs 2*rect(AC,CB)), note that the doubled rectangles are both rational so their difference is rational, but the sums of squares are both medial, and a medial area cannot exceed a medial area by a rational area (10.26), yielding the contradiction. The AI proof fills in substantially more detail (citing 2.4 for the algebraic identity, 10.15 and 10.23 for establishing mediality of the sums of squares, 10.37 for the definition of first bimedial, CN1-CN3 for arithmetic steps, D10.1.4 for medial areas, and 2.7 for the difference-of-squares identity) and extends the argument to explicitly show C=D, but the key intermediate conclusions are the same as Heath's. Heath's reference list in the data is empty (though the text cites 10.26), making all AI citations appear in ai_only, but this reflects citation-depth difference rather than a path divergence. This is Case A of Q2: same backbone, different citation depth.

### 10.44
**Category**: Granularity difference
**Jaccard**: 0.350
**Analysis**: Q2 decided the classification. Both proofs use the same fundamental technique: assuming a second bimedial line AB is divided at two points C and D, setting out a rational line EF, applying the relevant areas (sums of squares and twice the rectangles) to EF, showing the resulting breadths are rational and commensurable in square only, deducing that EN is a binomial straight line divided at two different points, and deriving a contradiction. The AI proof is more verbose and explicitly splits into cases (equal vs unequal sums of squares) and explicitly cites 10.42 for the binomial uniqueness result, while Heath leaves the final contradiction more implicit. The ai_only citations (1.45, 10.15, 10.21, 10.23, 10.24, 10.42, 2.7, CN1, CN2, CN3, D10.1.2, D10.1.4) are a mix of over-cited definitions/common notions/construction details and intermediate results that Heath uses implicitly or at a coarser granularity. The single heath_only citation 10.6 (commensurability from number ratios) is used by Heath for showing twice the rectangle is commensurable with the rectangle; the AI covers this same logical step through different explicit citations (10.23, 10.24). Since the key intermediate conclusions are the same and the differences are in citation depth, this is a granularity difference.

### 10.45
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: assume AB is a major straight line divided at C, suppose for contradiction it is also divided at D with the same properties, then show that the difference between the sums of squares on the two pairs equals the difference between twice the rectangles, that the sums of squares are both rational so their difference is rational, but twice the rectangles are both medial, contradicting 10.26. The AI proof makes this same argument but with greater citation depth: it explicitly invokes 2.4 to expand sq(AB) (which Heath uses implicitly), cites CN1 and CN3 for equating and rearranging, references D10.1.4 for the definition of rational, and uses 10.12 and 10.15 to explicitly justify that the difference of two commensurable rational areas is rational (which Heath states without citation as obvious). The AI also adds a second case (sums of squares equal) using 2.5, which Heath does not explicitly address. The heath_only set is empty, confirming that all of Heath's citations are subsumed by the AI's set. All ai_only items are either lower-level algebraic identities (2.4, 2.5), common notions (CN1, CN3), definitions (D10.1.4), or propositions that explicitly justify steps Heath treats as obvious (10.12, 10.15), making this a clear granularity difference.

### 10.46
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same key backbone: assume AB is divided at two points C and D with the properties of 10.40, derive that the difference between twice the rectangles (rational areas) equals the difference between the sums of squares (medial areas), and invoke 10.26 to reach a contradiction since a medial area cannot exceed a medial area by a rational area. The AI proof contains this entire backbone in Steps 3-8. The AI then extends the argument constructively in Steps 9-12, using II.5 and the midpoint to show C=D directly, whereas Heath simply concludes from the contradiction. The ai_only citations (10.12, 10.15, 2.4, 2.5, CN3, D10.1.4) reflect this deeper citation of implicit steps and the additional constructive finish. Heath_only is empty, confirming the AI covers all of Heath's reasoning. The core logical path is identical; the differences are in citation depth and the extended constructive argument.

### 10.47
**Category**: Path difference
**Jaccard**: 0.294
**Analysis**: Q2 determined the classification. Heath's proof applies areas to a rational line, shows the resulting breadths form a binomial (via VI.1, X.11, X.22, X.36), and derives a contradiction from X.42 in a single unified argument. The AI proof takes a fundamentally different structural approach by splitting into two cases: (1) when the sums of squares are equal, it uses an algebraic argument via II.7 showing (AC-CB)^2 = (AD-DB)^2 to force C=D, a key intermediate conclusion entirely absent from Heath; (2) when the sums of squares are unequal, it eventually reaches a binomial-based argument but handles the X.42 term-swap case separately (Steps 26-28) using an AM-GM inequality argument to derive a contradiction, another key conclusion absent from Heath. The AI also cites many additional substantive propositions (X.15, X.16, X.23, X.26) and avoids VI.1 entirely. These differences constitute a genuinely different logical backbone, not merely a difference in citation depth, making this a path difference (D).

### 10.48
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G. Both proofs follow the same logical backbone: set out numbers with specific ratio properties, construct a line whose square ratio matches the number ratio (10.6), establish the lines are rational and commensurable in square only (10.6, 10.9), conclude the sum is binomial (10.36), use ratio conversion (5.19) to show the square on the greater exceeds the square on the lesser by a square on a line commensurable with the greater (10.9), and conclude this is a first binomial. The ai_only citations (D10.1.3, D10.1.4, D10.2.1) are all definitions that Heath invokes implicitly, representing over-citation by the AI. The heath_only citation (10.28, specifically Lemma I after X.28) is used to guarantee the existence of numbers with the required ratio properties; the AI instead provides explicit numerical examples (BC=4, CD=3) to demonstrate such numbers exist, achieving the same constructive goal by a slightly different method. Since the key intermediate conclusions are identical and the citation differences reflect depth of citation rather than a different proof path, this is a granularity difference.

### 10.49
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: constructing two lines whose squares are in a ratio involving numbers where the ratio is not square-to-square, showing the lines are rational and commensurable in square only, concluding the sum is binomial via 10.36, and then proving the square on the greater exceeds the square on the lesser by a square commensurable with the greater so the result is a second binomial. The citation differences are all depth-related: Heath cites 5.19 (convertendo) as a packaged result, while the AI uses the more fundamental 5.17 (separando) and re-derives the needed proportion manipulation directly -- Heath's own proof of 5.19 uses 5.17 internally. The AI additionally cites 6.13 for explicit construction of the mean proportional (implicit in Heath), and definitions D10.1.3 and D10.2.2 which Heath references only implicitly. These are all granularity differences in citation depth, not backbone differences.

### 10.50
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow an identical backbone: they set out numbers with specified ratio properties, construct FG and GH via X.6, prove each is rational, establish their incommensurability in length via X.9, conclude FH is binomial via X.36, use ex aequali (5.22) to show E is incommensurable with GH, and prove the square on FG exceeds the square on GH by the square on a line commensurable with FG. The only substantive citation difference is that the AI uses separando (5.17) where Heath uses convertendo (5.19) to derive the same intermediate result sq(FG):sq(K) = AB:BC; both techniques reach the identical key conclusion via slightly different ratio manipulation. The remaining ai_only items (D10.1.3, D10.1.4, D10.2.3) are definitions that the AI explicitly cites but Heath leaves implicit, which is pure over-citation. Since the key intermediate conclusions are the same and the differences are limited to citation depth and an equivalent algebraic micro-step, this is a granularity difference.

### 10.51
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: two rational straight lines commensurable in square only, whose square excess is incommensurable with the greater term, with the greater term commensurable in length with the assigned rational line, yielding a fourth binomial. The Jaccard similarity is 0.0 because the citation sets are entirely disjoint, but the proof-tree containment test resolves this: Heath's proof of 10.30 (the AI's primary construction citation) uses exactly 10.6, 10.9, and 5.19 -- the three propositions in heath_only. The AI cites 10.30 as a packaged unit to obtain the pair of rational lines with the required properties, while Heath re-derives those properties inline using 10.6, 10.9, and 5.19. The AI's additional citations (10.36, 10.13, D10.1.3, D10.2.4) are explicit references to the binomial theorem, transitivity of incommensurability, and definitions that Heath invokes implicitly. This is a citation-depth difference with the same logical backbone, not a different proof path.

### 10.52
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: set up numbers with no square-number ratio, use 10.6 to construct lines whose squares are in that ratio, apply 10.9 to show commensurability in square only, invoke 10.36 to conclude binomial, then use convertendo (5.19) and 10.9 again to establish that the square on the greater term exceeds the square on the lesser by a line incommensurable with the greater, with the lesser term commensurable with the rational line set out. The AI proof is more verbose and includes a self-correction (Steps 6-7) where it adjusts the construction to ensure the lesser term is the one commensurable with the given rational line, but the final argument (Steps 7-12) follows the same key intermediate conclusions as Heath. The only citation differences are the AI's explicit references to definitions D10.1.3 and D10.2.5, which Heath uses implicitly. This is a classic over-citation pattern indicating a granularity difference rather than a path difference.

### 10.53
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) FG and GH are rational straight lines commensurable in square only, (2) E/A is incommensurable in length with both FG and GH, (3) FH is binomial by 10.36, (4) the square on FG exceeds the square on GH by a square on a line incommensurable with FG, and (5) FH is a sixth binomial. The citation differences are entirely matters of depth: the AI explicitly cites definitions (D10.1.2, D10.1.3, D10.2.6, D5.16) that Heath uses implicitly, cites 10.12 for the transitivity of commensurability of squares where Heath handles this implicitly, and cites 10.18 as an explicit warrant for the incommensurability-of-excess conclusion that Heath reaches via 10.9 and convertendo (5.19). The heath_only item 5.19 (convertendo) is used in the same logical step as the AI's D5.16 (definition of conversion of ratio) — both apply the convertendo operation at the same point in the argument. The logical backbone is identical; only the citation granularity differs.

### 10.54
**Category**: Path difference
**Jaccard**: 0.421
**Analysis**: Q2 determined the classification. Heath's proof constructs geometric squares SN and NQ equal to parallelograms AH and GK (using II.14), then establishes EL as a mean proportional between them (using VI.1 and VI.17), and uses a geometric Lemma to show MR is also a mean proportional, ultimately showing AC equals the square SQ. The AI proof takes a fundamentally different algebraic approach: it defines lines p and q with p-squared equal to AB times AG and q-squared equal to AB times GE, then shows p-squared plus q-squared is rational (via II.1 and X.19), that p-squared is commensurable with q-squared (via X.5 and X.6), and that twice the rectangle p by q is irrational (via X.21), concluding that p and q are rational commensurable in square only, making p+q binomial by X.36. The key intermediate conclusions differ: Heath works through geometric mean proportionals and square constructions, while the AI works through sum-of-squares rationality and product irrationality. This constitutes a genuine path difference (Case B in Q2), and Q3 confirms the AI's alternative chain is logically valid throughout.

### 10.55
**Category**: Granularity difference
**Jaccard**: 0.409
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: setting up the second binomial with bisection and deficient application (10.17), showing the two component lines are medial (10.21), commensurable in square (6.1, 10.11), incommensurable in length, and that their rectangle is rational (10.19), concluding via 10.37. The ai_only citations (1.10, 10.5, 10.7, 10.9, 2.1, 2.5, 6.16, 6.17, 6.28, D10.1.2, D10.1.3, D10.1.4) are over-citations of construction details, definitions, and auxiliary number-theory propositions that Heath leaves implicit. The sole heath_only citation 10.12 (transitivity of commensurability) is used by Heath to show EF commensurable with EK in proving the rectangle is rational; the AI achieves the same conclusion via the algebraic identity 2*rect(R,S) = A*CE, bypassing 10.12 but reaching the identical key intermediate conclusion. The backbone is the same at all key logical positions; differences are in citation depth only.

### 10.56
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: the side of the area is a sum of two medial straight lines that are commensurable in square only and contain a medial rectangle, hence the sum is a second bimedial by 10.38. Heath's proof achieves this concisely by referring to 'the foregoing' (10.55) for the bimedial structure and then proving the rectangle is medial via 10.13 and 10.21. The AI proof spells out every detail explicitly across 19 steps, citing 13 additional propositions (10.11, 10.12, 10.15, 10.17, 10.23, 10.9, 2.1, 2.5, 6.1, 6.17, D10.1.2, D10.1.3, D10.1.4) that Heath treats as implicit through the reference to prior work. Heath_only is empty, confirming the AI covers all of Heath's cited material. The logical backbone is identical; the difference is purely citation depth.

### 10.57
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: establish the properties of the fourth binomial from the definition, bisect DE and apply a rectangle to get AG incommensurable with GE via 10.18, construct two auxiliary lines (MN/NO in Heath, r/s in the AI) that are incommensurable in square, show the sum of their squares is rational (via 10.19), show the rectangle contained by them is medial (via 10.21 and the incommensurability of ED with AB from 10.13), and then apply 10.39 to conclude the result is a major irrational. The ai_only set consists entirely of over-citations: construction propositions (1.10 for bisection, 6.28 for application of areas), foundational results (2.4 for algebraic expansion, 6.17 for proportions), a reference to 10.36 for binomial properties Heath derives from the definition, and additional definitions (D10.1.3, D10.1.4). The heath_only set is empty, confirming that the AI cites everything Heath cites and more. This is a clear Case A same-backbone, different-citation-depth scenario.

### 10.58
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish two lines incommensurable in square, show that the sum of their squares is medial, show that their rectangle is rational, and conclude by 10.40 that the sum is the side of a rational plus a medial area. The large citation symmetric difference (Jaccard 0.40) is explained by the AI explicitly citing construction propositions (1.10, 1.47, 2.4, 2.5, 2.14, 3.31) that Heath subsumes under the phrase 'let the same construction be made as before shown,' and by a methodological difference in establishing commensurability: Heath uses VI.1 (proportionality of areas under same height) with X.11, while the AI directly applies areas to rational lines and uses 10.20 and 10.22 to characterize the breadths. These are differences in citation depth and sub-method, not in the key intermediate conclusions, making this a granularity difference rather than a path difference.

### 10.59
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification. Both proofs establish the same four conditions required by 10.41 to conclude that the side is the side of the sum of two medial areas: (1) two lines incommensurable in square, (2) sum of squares on them is medial, (3) rectangle contained by them is medial, and (4) sum of squares incommensurable with the rectangle. Heath's proof is concise, referencing 'the same construction as before shown' from earlier propositions in the series (10.54-10.58) and working with areas MN, NO, MO. The AI proof is much more verbose, explicitly constructing lines H and K via bisection (1.10), application of areas (6.28), and mean proportionals (6.13, 2.14), and citing many foundational results (10.36, 10.18, 10.7, 10.23, 2.1, 6.16, D10.1.4, D10.2.6) that Heath leaves implicit. The single heath_only citation (10.13, transitivity of incommensurability) is used by Heath to transfer incommensurability from ED/AB to FE/EK; the AI handles this step by a slightly different but equivalent route, applying 10.21 directly to AB*ED. Since the key intermediate conclusions are identical and the differences are entirely in citation depth and explicitness of construction, this is a granularity difference.

### 10.60
**Category**: Granularity difference
**Jaccard**: 0.476
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) sq(AC)+sq(CB) is rational, so the corresponding breadth is rational and commensurable in length with DE; (2) 2*rect(AC,CB) is medial, so its breadth is rational and incommensurable in length with DE; (3) the two breadths are rational and commensurable in square only, making their sum binomial; (4) the greater breadth exceeds the lesser by the square on a line commensurable with the greater; (5) hence first binomial by definition. The citation differences are all depth-level: the AI explicitly cites 2.4 and 2.7 for algebraic identities Heath uses implicitly, uses 10.5+10.6 where Heath uses 10.11 for commensurability transfer, cites 10.23 for mediality that Heath derives directly from 10.21, and includes definitions D10.1.2-D10.1.4 that Heath invokes implicitly. Heath's citation of the Lemma after 10.53 for the mean proportional property is covered by the AI's direct use of 6.17. Since all backbone conclusions match and differences are only in citation granularity, this is Case A of Q2.

### 10.61
**Category**: Granularity difference
**Jaccard**: 0.526
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: (1) the sum of squares on the medial segments is medial, (2) applied to the rational line it produces a rational segment incommensurable with that line, (3) twice the rational rectangle produces a rational segment commensurable with the rational line, (4) the two segments are incommensurable making the breadth binomial, (5) the greater segment exceeds the lesser, (6) the square on the greater exceeds the square on the lesser by a square on a commensurable line, and (7) the lesser term is commensurable with the rational line making it a second binomial. The citation differences are entirely depth-related: the AI cites 10.5 and 10.6 directly where Heath cites the higher-level 10.11 (whose own proof uses 10.5 and 10.6, confirmed by the proof-tree containment test), and the AI explicitly cites foundational results like 2.4, 2.7, 6.17, 10.43, and D10.1.4 that Heath leaves implicit or covers via 10.21. No backbone divergence exists.

### 10.62
**Category**: Granularity difference
**Jaccard**: 0.348
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) the breadth corresponding to the sum of squares on the medial segments is rational and incommensurable in length with the rational line (Heath uses X.22 directly on DM; AI decomposes into DG and GM individually via 10.22, then combines via 10.15); (2) the breadth corresponding to twice the rectangle is rational and incommensurable with the rational line (both via 10.22); (3) these two breadths are incommensurable with each other (Heath via X.12, X.13; AI via 10.11, 10.13 applied to sum-of-squares vs twice-rectangle); (4) the result is binomial via 10.36; (5) the square on the greater exceeds the square on the lesser by a commensurable square (Heath says 'in manner similar to the foregoing'; AI explicitly cites 10.14 and 10.17); (6) neither term is commensurable with the rational line, yielding third binomial via D10.2.3. The backbone is identical. The citation differences are depth-related: the AI over-cites algebraic identities (2.4, 2.5, 2.7), common notions (CN1-3), definitions (D10.1.3), construction props (10.28, 10.32), and uniqueness (10.44), while making explicit the propositions Heath leaves implicit with 'in manner similar to the foregoing' (10.14, 10.17). Heath's use of 10.12 and 10.23 Porism is replaced by AI's use of 10.21 and direct application of 10.11/10.15 for the same underlying facts.

### 10.63
**Category**: Granularity difference
**Jaccard**: 0.538
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same key intermediate conclusions: (1) the sum of squares on AC, CB is rational, yielding a rational breadth commensurable with DE via 10.20; (2) twice the rectangle AC,CB is medial, yielding a rational breadth incommensurable with DE via 10.22; (3) the two breadth components are incommensurable with each other; (4) they are rational commensurable in square only, making DG binomial; (5) the square on the greater exceeds the square on the less by the square on a line incommensurable with the greater, via 10.18; (6) the greater component is commensurable with DE, so DG is a fourth binomial by D10.2.4. The citation differences are purely at the granularity level: the AI adds explicit lower-level citations (2.4 for the algebraic identity, 10.23 for twice a medial area being medial, and definitions D10.1.3/D10.1.4 for rational-medial incommensurability) while Heath cites intermediate results the AI omits (10.13 for transitivity of incommensurability, and 10.36 for the definition of binomial). In both cases the underlying geometric facts are present at the same logical positions in both proofs, with the AI reaching incommensurability of the breadth components via area ratios (6.1, 10.11) rather than Heath's use of 10.13, and omitting the explicit 10.36 citation since it proceeds directly to the more specific fourth binomial classification.

### 10.64
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions in the same order: (1) the sum of squares on AC, CB applied to DE yields a breadth (DM/DH) that is rational and incommensurable with DE; (2) twice the rectangle AC, CB applied to DE yields a breadth (MG/HG) that is rational and commensurable with DE; (3) these breadths are incommensurable with each other, making DG binomial; (4) the square on the greater exceeds the square on the lesser by the square on a line incommensurable with the greater; (5) the lesser term is commensurable with DE, yielding a fifth binomial. The sole heath_only citation (10.18) is not missing from the AI proof but is instead re-derived explicitly in Steps 10-12 using sub-components (10.15, 10.16, 10.6, 6.1, 6.22, 2.5) that appear within or closely relate to 10.18's own proof structure. The proof-tree containment test confirms this: Heath's proof of 10.18 uses 10.16, 10.6, and 10.13, all of which appear in the AI's citations. The large ai_only set consists of algebraic identities (2.4, 2.5, 2.7), ratio propositions (6.1, 6.22), commensurability sub-results (10.15, 10.16, 10.6), a common notion (CN5), and a definition (D10.2.5), all reflecting finer citation granularity rather than a different logical path.

### 10.65
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: decomposing the square on AB via 2.4, applying medial areas to a rational line DE to get rational segments incommensurable with DE (via 10.22), showing those segments are incommensurable with each other (via 6.1 and 10.11) to establish a binomial (10.36), then proving the binomial is specifically sixth by showing the square on the greater exceeds the square on the lesser by a square on a line incommensurable with the greater, and neither segment is commensurable with DE. The AI proof cites all five of Heath's references and adds ten more (10.12, 10.13, 10.15, 10.23, 10.6, 2.4, 2.7, D10.1.3, D10.1.4, D10.2.6) which are sub-lemmas, algebraic identities, and definitions that Heath invokes implicitly or via phrases like 'in accordance with what was before proved' and 'similarly again we can prove.' Heath's citation set is a proper subset of the AI's, and heath_only is empty, confirming this is a citation-depth difference rather than a path divergence.

### 10.66
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) CF is commensurable in length with AE and FD with EB, (2) CF and FD are rational, (3) CF and FD are commensurable in square only, (4) CD is binomial, and (5) the order is preserved through the same six-case analysis. The citation differences reflect different depths of justification for these same facts. Heath constructs the proportion AB:CD = AE:CF using 6.12 and derives the remainder proportion via 5.19, then uses 5.11/5.16 for alternation and 10.11 for commensurability. The AI instead uses 10.5 and 10.6 (commensurable magnitudes have ratios of numbers) to directly establish commensurability of CF with AE and FD with EB. For commensurability in square only, Heath uses the alternating proportion with 10.11 while the AI uses a contradiction argument via 10.12. For the neither-commensurable case in order determination, Heath cites 10.13 while the AI uses the contrapositive of 10.12. These are all alternative justification paths to the same intermediate conclusions, constituting a citation-depth difference rather than a backbone difference.

### 10.67
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: (1) AE and EB are medial and commensurable in square only; (2) CF and FD are each commensurable in length with AE and EB respectively; (3) CF and FD are medial; (4) CF and FD are commensurable in square only; (5) the rectangle AE by EB is commensurable with the rectangle CF by FD; (6) CD is bimedial and the same in order as AB. The backbones match exactly. The citation differences are all matters of depth: the AI cites 5.17 (separando) where Heath cites 5.19 (remainder proportion), but 5.19's own proof uses 5.17, 5.16, and 5.11, so the AI is citing a sub-step of Heath's compound reference. Similarly, Heath cites 5.11 (transitivity of ratios) for deriving AE:EB = CF:FD, while the AI uses 5.16 (alternando) for the equivalent step. The AI's additional citations (10.5, 10.6, 10.9, 10.12, 6.16, 6.22) are all foundational or technical propositions that Heath invokes implicitly or compresses, representing over-citation rather than a different proof strategy.

### 10.68
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determined the classification. Heath proves 10.68 by directly decomposing the major line AB into components AE, EB and using proportional reasoning (5.11, 5.16, 5.18, 6.20) to show the corresponding components CF, FD of the commensurable line CD satisfy the same defining conditions of a major line (sum of squares rational, rectangle medial via 10.23), then applies the definition 10.39. The AI proof takes a fundamentally different route through binomial classification: it applies the square on AB to a rational line to obtain a fourth binomial breadth (10.63), transfers commensurability to the breadth for CD (10.11), preserves binomial order (10.66), and reverses the classification to conclude CD is major (10.57). These are genuinely different logical backbones operating in different domains of Book 10 theory, with no overlap in key intermediate conclusions. The AI's path is logically complete and valid, so Q3 yields D.

### 10.69
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish identical key intermediate conclusions: (1) AB is divided at E with AE, EB incommensurable in square, sum of squares medial, rectangle rational (by 10.40); (2) CF, FD are constructed and shown to be incommensurable in square; (3) sum of squares on CF, FD is medial; (4) rectangle CF, FD is rational; (5) therefore CD is the side of a rational plus a medial area. Heath's proof is extremely summary-style, stating 'same construction as before' and 'we can then prove similarly,' citing only 10.40. The AI proof explicitly works through every step with detailed citations (10.11, 10.12, 10.13, 10.15, 10.23, 10.46, 5.16, 6.12, 6.16, D10.1.4). Since heath_only is empty and all AI-only citations are sub-steps that flesh out the reasoning Heath compresses into 'prove similarly,' this is a clear case of same backbone with different citation depth.

### 10.70
**Category**: Granularity difference
**Jaccard**: 0.083
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they divide the original line into two components with the three defining properties of the side of the sum of two medial areas (10.41), construct a proportional division of the commensurable line, establish commensurability of corresponding parts, then transfer all three properties (medial sum of squares, medial rectangle, incommensurability of sum of squares with rectangle) to the new line's components. Heath's proof is highly abbreviated, using 'the same construction as before' and 'we can then prove similarly' to compress the argument into a single citation of 10.41. The AI proof fills in every detail explicitly, citing 11 additional lower-level propositions (ratio/proportion results 5.12, 5.16, 5.18, construction 6.12, rectangle proportion 6.16, commensurability results 10.11, 10.12, 10.13, 10.15, mediality transfer 10.23, and definition D10.1.4). Since heath_only is empty and all ai_only items are sub-steps of the same logical backbone, this is a clear Case A granularity difference.

### 10.71
**Category**: Granularity difference
**Jaccard**: 0.733
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: apply the rational and medial areas to a rational line EF to obtain two breadths, show one is commensurable and the other incommensurable in length with EF, establish that the two breadths are incommensurable with each other (making their sum a binomial by 10.36), then distinguish four sub-cases based on which term is greater and the commensurability of the excess of squares, yielding four types of binomial (first, second, fourth, fifth) and correspondingly four types of irrational side (binomial, first bimedial, major, side of rational plus medial) via 10.54, 10.55, 10.57, and 10.58. The only difference is in how the incommensurability of the two breadths is established: Heath uses 6.1 (proportionality of parallelograms) and 10.11 (transfer of incommensurability through proportions), while the AI uses 10.13 (if one magnitude is commensurable with a third and another is incommensurable with it, the two are incommensurable). The AI also adds D10.1.4 (definition of medial area) as an explicit definitional citation. These are citation-depth differences at the same logical position, not backbone differences, so the classification is G.

### 10.72
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: applying two medial areas to a rational line to obtain rational breadths (10.22), showing those breadths are incommensurable (6.1, 10.11), concluding their sum is binomial (10.36), then distinguishing the third binomial case yielding a second bimedial (D10.2.3, 10.56) from the sixth binomial case yielding a side of the sum of two medial areas (D10.2.6, 10.59). The AI proof cites all of Heath's references plus seven additional items: construction propositions 1.44 and 1.45 for applying areas as rectangles, definition D10.1.3 for justifying commensurability in square, and definitions D10.2.1, D10.2.2, D10.2.4, D10.2.5 for explicitly eliminating four binomial types. These are all over-citations making explicit what Heath leaves implicit. Heath's citation set is a proper subset of the AI's, confirming same backbone at different citation depth.

### 10.73
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: The classification is decided at Q2/Q3. Heath's proof is a direct argument: it uses 10.11 to transfer the incommensurability of AB and BC (in length) to the incommensurability of sq(AB) and rect(AB,BC), then combines 10.15, 10.6, and the II.7 identity with 10.13 and 10.16 to conclude that sq(AB)+sq(BC) is incommensurable with sq(AC), hence AC is irrational. The AI proof takes a fundamentally different path: a proof by contradiction. It first establishes that sq(AB)+sq(BC) is rational (via 10.12) and that rect(AB,BC) is irrational (via 10.21), then assumes AC is rational and uses the II.7 identity with 10.15 (converse) to show 2*rect(AB,BC) would be rational, which via 10.6 would make rect(AB,BC) rational, contradicting 10.21. The key intermediate conclusions differ: Heath's backbone pivots on the incommensurability transfer via 10.11 and the additive incommensurability via 10.16, while the AI's backbone pivots on establishing rect(AB,BC) as medial via 10.21 and deriving a contradiction. The AI's contradiction-based path is logically complete and valid, so this is a path difference (D).

### 10.74
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determined the classification. Heath's proof works by direct argument: since sq(AB)+sq(BC) (medial) is incommensurable with 2*rect(AB,BC) (rational), by 10.16 the remainder sq(AC) from the II.7 identity is also incommensurable with 2*rect(AB,BC), hence irrational. The AI instead takes a fundamentally different route using proof by contradiction with two sub-cases: assuming sq(AC) is rational leads to a rational sum equaling a medial area (contradiction), and assuming sq(AC) is medial leads to a medial area exceeding another medial area by a rational area, contradicting 10.26. The AI never uses 10.16 and Heath never uses 10.26, reflecting genuinely different logical backbones rather than mere citation-depth variation. The AI's contradiction-based path is logically complete and valid, satisfying Q3, yielding classification D.

### 10.75
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they set out a rational line DI, apply the sum of squares and twice the rectangle as areas on DI, show each area is medial (yielding rational breadths DG and DF incommensurable with DI), establish that the sum of squares is incommensurable with twice the rectangle via the chain AB incomm. in length with BC, then conclude DG incomm. with DF so FG is irrational by 10.73, and finally that AC is irrational. The citation differences are purely granularity: the AI over-cites three definitions (D10.1.2, D10.1.3, D10.1.4) for explicitness, while Heath cites 10.28 as a bracketed reference to the construction proposition guaranteeing the existence of the hypothesized configuration, which the AI simply assumes as given. All key intermediate conclusions appear in both proofs at the same logical positions.

### 10.76
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) the sum of squares on AB, BC is rational while twice the rectangle AB, BC is medial, (2) these two areas are incommensurable, (3) by II.7/2.7 the square on AC equals their difference, (4) therefore the square on AC is irrational via X.16/10.16, and (5) AC is irrational. The AI proof elaborates the same reasoning with additional explicit citations for the properties of medial and rational areas (10.21, 10.23, D10.1.3, D10.1.4) and uses CN3 for algebraic rearrangement, while Heath's proof is more concise and uses 'convertendo' to reach the incommensurability conclusion. Heath's sole unique citation 10.33 is a back-reference to the construction that produces lines satisfying the hypothesis conditions, not a deductive step in the proof itself. The AI's Step 8 uses a more elaborate indirect argument where Heath compresses the same inference, but both arrive at the same intermediate and final conclusions. This is a clear Case A: same backbone with different citation depth.

### 10.77
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 reveals genuinely different proof backbones, leading to classification at Q3. Heath's proof works directly: using 2.7 to express sq(AC) in terms of the given quantities, then applying 10.16 (incommensurable magnitudes added together yield an incommensurable whole) to conclude sq(AC) is incommensurable with the rational quantity 2*rect(AB,BC), hence irrational. The AI proof instead uses two contradiction arguments: Step 3 shows sq(AC) is not rational (if it were, by 10.12 and 10.15 the sum sq(AB)+sq(BC) would be rational, contradicting its being medial), and Step 4 shows sq(AC) is not medial (if it were, a medial area would exceed a medial area by a rational area, contradicting 10.26). These intermediate conclusions -- 'not rational' and 'not medial' -- are fundamentally different from Heath's 'incommensurable with 2*rect(AB,BC)' via 10.16. The AI's contradiction-based elimination path is logically sound, with all cited propositions applied correctly, satisfying Q3(b). Classification is therefore D.

### 10.78
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: setting up rectangles on a rational line DI with remainder equal to the square on AC (via 2.7), showing both breadths DG and DF are rational and incommensurable in length with DI (via 10.22), establishing incommensurability of DG and DF, concluding the difference is an apotome (via 10.73), and deducing AC is irrational. The citation differences are all depth-related: Heath cites 6.1 for the proportion linking area ratios to breadth ratios while the AI compresses this into the 10.11 step; Heath cites 10.35 as a construction reference which the AI omits since the lines are taken as given; Heath cites a deduction from 10.20 for irrationality of the rectangle of rational and apotome while the AI mentions 10.21 and 10.13 in the text; and the AI explicitly cites definitions D10.1.3 and D10.1.4 which Heath leaves implicit. The backbone is the same throughout, making this a same-conclusions-different-depth Case A under Q2.

### 10.79
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they assume a second annex BD to apotome AB, use II.7 to express sq(AB) two ways, rearrange to show the difference of two rational areas (sums of squares) equals the difference of two medial areas (doubled rectangles), then invoke X.26 to reach a contradiction. The AI proof is more explicit, citing definitions (D10.1.2, D10.1.4), common notions (CN1, CN2, CN3), and 10.15 to justify that sums of squares are rational, and additionally uses 2.4 in an extended algebraic conclusion (Steps 11-14) showing AC=AD and CB=DB. Heath leaves these sub-steps implicit. Since heath_only is empty and all ai_only items are definitions, common notions, or supporting propositions that elaborate the same backbone at finer granularity, Case A of Q2 holds.

### 10.80
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume a second annex exists with the required properties (via 10.74), apply II.7 to express sq(AB) in two ways, equate and rearrange to show the difference of sums-of-squares equals the difference of twice-rectangles, identify the rectangle side as rational and the sum-of-squares side as medial (via 10.15 and 10.23), then invoke 10.26 to reach a contradiction. The AI proof cites all five of Heath's references and adds seven more (10.11, 10.12, 2.4, CN1, CN2, CN3, D10.1.4). These extras are common notions, a definition, supporting commensurability propositions (10.11, 10.12), and II.4 used in additional steps (10-13) where the AI explicitly derives AC=AD and BC=BD after establishing the contradiction. Heath stops at the contradiction itself. Since the key intermediate conclusions are identical and the differences are purely in citation depth and additional elaboration, this is a granularity difference.

### 10.81
**Category**: Granularity difference
**Jaccard**: 0.421
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: setting up a rational line, applying the sum of squares and twice the rectangle to it to obtain rational breadths incommensurable with the rational line, showing those breadths are incommensurable with each other, constructing apotomes via 10.73, and invoking the uniqueness of the apotome annex (10.79) to reach a contradiction. The heath_only citations (10.11, 10.13, 10.6) all appear inside Heath's proof of 10.75, which the AI cites as a unit to establish the incommensurability of the sum of squares with twice the rectangle; this satisfies the proof-tree containment test and confirms a citation-depth difference rather than a backbone divergence. The ai_only items are mostly construction propositions (1.44, 1.45), axioms/definitions (CN1, CN3, D10.1.1), and basic identities (2.4) representing over-citation, while 6.16 is used in the AI's slightly different finishing argument after applying 10.79, which does not alter the shared backbone of key intermediate conclusions.

### 10.82
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assuming two different annexes BC and BD to the minor straight line AB, they derive that the difference between the sums of squares (both rational) equals the difference between the double rectangles (both medial), yielding a rational difference between medial areas, which contradicts 10.26. The AI proof expands this reasoning with explicit algebraic identities (2.7 to set up the relation, 2.4 for the final uniqueness argument) and explicit commensurability steps (10.12, 10.15, D10.1.4 to justify that the difference of rational areas is rational), plus common notions (CN1, CN2, CN3) for arithmetic manipulations. Heath compresses all of these into direct observations. Since heath_only is empty and every ai_only citation is an expansion of steps Heath performs implicitly, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference.

### 10.83
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume a second annex BD exists (via 10.77), establish an algebraic identity showing the difference of the sums of squares equals the difference of the double rectangles, observe that the right side is a difference of rational areas while the left side is a difference of medial areas, then invoke 10.26 to obtain a contradiction. The AI proof explicitly cites lower-level results that Heath uses implicitly: algebraic identities 2.4 and 2.7 for expanding squares of sums and differences, common notions CN1, CN2, CN3 for arithmetic manipulations, definition D10.1.4 for the concept of rational area, and 10.12 for commensurability of rational areas. Heath's proof references only 10.77 and 10.26, compressing the intermediate algebra with the phrase 'as in the preceding cases.' Since heath_only is empty and all ai_only items are foundational or constructive citations underlying the same key conclusions, this is a same-backbone, different-depth scenario: Granularity difference (G).

### 10.84
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: assume two possible annexes BC and BD to AB, construct rectangles on a rational line EF representing the sums of squares and twice the rectangles for each decomposition, show that EH is an apotome with HM as annex (first decomposition) and with HN as annex (second decomposition), then invoke 10.79 to reach a contradiction. The AI proof establishes all the same key intermediate conclusions as Heath. The difference is that the AI over-cites by including 1.45 (for the explicit construction of applying areas), 2.4 (the algebraic identity for expanding squared sums in Step 18), and CN2/CN3 (for the final arithmetic deductions in Step 20). Heath reaches the contradiction directly from 10.79, while the AI derives HM = HN and then works through additional algebraic steps to show AC = AD and CB = DB explicitly. These extra steps and citations represent greater granularity and explicitness, not a different proof path. With heath_only empty, there are no missing Heath citations to investigate.

### 10.85
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: BG is rational and commensurable in length with A, BG and GC are rational straight lines commensurable in square only, BC is an apotome via 10.73, the square on BG exceeds the square on GC by the square on a line commensurable with BG, and BG is commensurable in length with A so BC is a first apotome via D10.3.1. The difference is purely in citation depth: Heath constructs the pair BG, GC from scratch using number-theoretic machinery (10.6 for commensurability of squares, 10.9 for length incommensurability, and 5.19 convertendo for the commensurability of the excess), while the AI invokes 10.29 which packages exactly this construction as a single unit result. The proof-tree containment test confirms that all three heath_only propositions (10.6, 10.9, 5.19) appear inside Heath's own proof of 10.29, making this a citation-depth difference rather than a path difference.

### 10.86
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G. Both proofs establish the same key intermediate conclusions: (1) the annex is rational and commensurable in length with the set-out rational line, (2) the whole is rational and incommensurable in length with the annex, (3) the whole and annex are rational lines commensurable in square only making the difference an apotome via 10.73, (4) the square on the whole exceeds the square on the annex by the square on a line commensurable in length with the whole, and (5) the annex is commensurable with the rational line, yielding a second apotome by D10.3.2. The citation differences reflect the use of different Book V proportion manipulation tools to reach the same geometric conclusions: Heath uses convertendo (5.19) to derive the excess commensurability, while the AI uses separando (5.17) and ex aequali (5.22) to achieve the same result through a slightly different algebraic route. The AI also explicitly cites D10.1.3 (definition of rational) which Heath uses implicitly. Since the geometric backbone is identical and the differences lie only in which proportion-manipulation lemmas are invoked, this is a granularity difference rather than a genuine path divergence.

### 10.87
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: FG is rational and incommensurable in length with A, GH is rational and incommensurable in length with FG (commensurable in square only), FH is an apotome via 10.73, A is incommensurable with GH via ex aequali (5.22) and 10.9, and the square on FG exceeds the square on GH by the square on a line commensurable with FG, yielding a third apotome by D10.3.3. The citation differences are purely granularity: the AI explicitly cites definitions D10.1.3 and D10.1.4 where Heath leaves the rationality inference implicit, and the AI uses separando (5.17) where Heath uses convertendo (5.19) to derive the same ratio relationship at the same logical position in the proof. Since these are different ratio manipulation techniques achieving the identical intermediate conclusion at the same step, the backbone is the same and the difference is one of citation depth, not path.

### 10.88
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: two rational straight lines commensurable in square only, their difference is an apotome (via 10.73), the square on the greater exceeds the square on the lesser by the square on a line incommensurable with the greater, and the whole is commensurable in length with the rational line set out, yielding a fourth apotome by D10.3.4. The difference is purely one of citation depth: Heath re-derives the construction step-by-step using 10.6, 10.9, and 5.19, while the AI packages this entire construction via 10.30. The proof-tree containment test confirms that all three heath_only items (10.6, 10.9, 5.19) appear inside Heath's own proof of 10.30, so the AI is citing 10.30 as a unit while Heath inlines its components. The AI's additional citations of 10.13, D10.1.1, and D10.1.3 are over-citations (an extra transitivity step and explicit definition references) that do not alter the logical backbone.

### 10.89
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) two rational lines commensurable in square only, (2) their difference is an apotome via 10.73, (3) the square on the whole exceeds the square on the annex by a square on a line incommensurable in length with the whole, and (4) the annex is commensurable with the rational line set out, yielding a fifth apotome by D10.3.5. The backbone is identical. The citation differences arise because the AI uses 10.18 (a higher-level packaged result about parallelogram application and incommensurability) to establish the incommensurability of the excess, whereas Heath uses 5.19 (convertendo) to manipulate the proportion and then applies 10.9 directly. Although 5.19 does not appear inside 10.18's proof tree, both methods serve to justify the same intermediate conclusion (that the excess is incommensurable with the whole), so the backbone conclusions match and the difference is one of citation depth rather than logical path. The AI's additional citations of D10.1.3, D10.1.4 (definitions) and 10.13 (transitivity of incommensurability, making explicit what Heath leaves implicit) are over-citations consistent with a granularity difference.

### 10.90
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: FG and GH are rational and commensurable in square only (yielding FH as an apotome by 10.73), neither is commensurable in length with A (via ex aequali using 5.22), and the square on FG exceeds the square on GH by the square on a line incommensurable with FG (via convertendo using 5.19), satisfying the definition of sixth apotome (D10.3.6). The AI proof contains garbled wording in Step 3 (claiming squares are incommensurable when it should say lines are incommensurable in length), but immediately reaches the correct conclusion (commensurable in square only), so under the lenience rule this is not an error. The ai_only citations CN3 and D10.1.3 are a common notion and a definition, representing over-citation of foundational items rather than a different logical path. With identical backbones and only definitional/axiomatic over-citation, this is Case A of Q2: same backbone, different citation depth, yielding G.
**Audit Record**: CANDIDATE E — 10.90
  violated_claim : "the square on FG is incommensurable with the square on GH [by 10.9]"
  failure_mode   : invalid_inference
  missing_is     : expansion — the AI correctly concludes "commensurable in square only" which IS the correct conclusion; the intermediate wording is garbled but the step is supported by the cited propositions
  evidence       : AI Step 3 says "the square on FG is incommensurable with the square on GH [by 10.9]" but 10.9 actually yields incommensurability in length, not incommensurability of the squares. The AI then immediately states the correct conclusion.
  why_not_terse  : The AI makes an explicitly wrong intermediate claim (squares incommensurable) but then immediately states the correct conclusion (commensurable in square only), indicating garbled wording rather than a genuine logical gap. Under the lenience rule (invalid vs compressed-but-sound), this is NOT-E.

### 10.91
**Category**: Path difference
**Jaccard**: 0.364
**Analysis**: Q2 determined the classification. Both proofs share the same initial setup (first apotome AD with annex DG, bisection at E, application of areas yielding AF commensurable with FG, and AF/FG each rational and commensurable with AC), but they diverge fundamentally in how they construct and identify the 'side' of the area. Heath uses a geometric approach: constructing squares LM and NO about the same diameter (6.26), establishing EK as a mean proportional between AI and FK (via 6.17, 5.11), using the Lemma after 10.53 for MN as mean proportional, and a gnomon argument to show AB equals the square on LN. The AI instead takes an algebraic route: introducing auxiliary lines H and K as sides of squares equal to AC*AF and AC*FG, computing H^2+K^2 = AC*AG (rational) and 2*H*K = AC*DG (medial) via direct algebraic manipulation, then using the identity (H-K)^2 = H^2+K^2-2HK (2.7) to show the side is H-K. The AI proves H and K are incommensurable in length by contradiction (commensurability would make rational and medial areas commensurable), while Heath uses proportion-based reasoning with 6.1 and 10.11. These are genuinely different logical backbones, and the AI's algebraic path is logically sound throughout, yielding classification D.

### 10.92
**Category**: Path difference
**Jaccard**: 0.364
**Analysis**: Q2 determines the classification as D (path difference). Both proofs share the same setup (DG as annex to AD, applying 10.17 to get commensurable segments AH and HG) and the same conclusion (applying 10.74 to identify the first apotome of a medial straight line). However, the middle portions diverge substantially. Heath constructs geometric squares LM and NO about the same diameter (6.26), establishes EK as a mean proportional between AI and FK (6.17, 5.11), and uses a gnomon argument to show the area AB equals sq(LN). The AI instead works more algebraically: it sets up lines MN and NO defined by sq(MN)+sq(NO) = rect(AC,AG) and rect(MN,NO) = (1/2)rect(AC,DG), shows these are medial and commensurable in square only using 10.21, 10.15, and 10.26, and then uses the algebraic identity 2.7 to show sq(MN-NO) = rect(AC,AD). These constitute genuinely different backbones -- Heath's geometric gnomon construction versus the AI's algebraic decomposition -- making this a path difference rather than a granularity difference. The AI's path is logically complete under the Q3 check.

### 10.93
**Category**: Path difference
**Jaccard**: 0.353
**Analysis**: Q2 determined the classification. Heath's proof uses a geometric construction with squares LM and NO about the same diameter (6.26), establishing EK as a mean proportional between AI and FK via 6.17 and 5.11, and relying on commensurability transfer lemmas 10.13 and 10.15 throughout. The AI proof takes a fundamentally different algebraic-constructive path: it defines auxiliary lines o and p via sq(o) = AC * AN and sq(p) = AC * HG, then uses algebraic identities (2.5, 2.7) and 10.22 (medial area applied to rational line) to establish that o and p are medial, commensurable in square only, and contain a medial rectangle, before concluding by 10.75. The AI bypasses the entire LM/NO square-and-diameter construction, replacing geometric proportionality arguments (5.11, 6.17, 6.26) with direct algebraic manipulation. The five substantive heath_only propositions (10.13, 10.15, 5.11, 6.17, 6.26) are not subsumed by any single AI citation but represent an independent geometric route. This constitutes a genuine backbone divergence (Case B in Q2). Under Q3, the AI's alternative path is logically complete despite being presented in a disorganized manner with multiple restarts, as the final chain (Steps 17-30) connects premises to conclusion without unsupported assertions or invalid inferences.

### 10.94
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they set up the fourth apotome with its annex, apply 10.18 to obtain incommensurable parts, establish that the sum of squares on the constructed lines is rational (via 10.19), that twice their rectangle is medial (via 10.21), that the lines are incommensurable in square (via 10.11), and conclude the side is minor by 10.76. The heath_only citations 5.11 and 6.26 are used by Heath for a geometric construction with squares LM, NO about a common diameter and the mean proportional relationship, while the AI achieves the same key conclusions algebraically using s1 and s2 directly, citing basic commensurability transitivity results (10.12, 10.13, 10.15, 10.16) and 2.5 for the bisection identity that Heath leaves implicit. The ai_only citations are all basic commensurability or algebraic identity propositions representing over-citation of foundational steps. Since all key intermediate conclusions match and the differences are only in citation depth and the level of explicit justification, this is a granularity difference.

### 10.95
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish the properties of the fifth apotome (AG, GD rational, commensurable in square only, GD commensurable with the rational line, sq(AG) > sq(GD) by incommensurable), bisect GD, apply a rectangle to get incommensurable parts, then verify three conditions for 10.77 -- that the sum of squares is medial (via 10.21), twice the rectangle is rational (via 10.19), and the squares are incommensurable. The key difference is construction technique: Heath constructs geometric squares LM, NO and uses 6.26 to establish they share a diameter, while the AI constructs lines MN, NO algebraically via 2.14 and uses algebraic identities (2.1, 6.1, 10.11) to reach the same intermediate conclusions. The AI's ai_only citations (1.10, 10.11, 10.73, 2.1, 2.14, 6.1, 6.28, D10.1.3, D10.1.4, P1) are predominantly construction steps, definitions, and intermediate lemmas that Heath leaves implicit or handles via a different construction method. Heath's sole unique citation 6.26 belongs to the geometric construction approach that the AI replaces with its algebraic method, but both arrive at identical key conclusions.

### 10.96
**Category**: Granularity difference
**Jaccard**: 0.385
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same four key conditions required by 10.78 to conclude that the 'side' is a line which produces with a medial area a medial whole: (1) two segments incommensurable in square, (2) sum of squares on them is medial, (3) twice the rectangle contained by them is medial, and (4) the sum of squares is incommensurable with twice the rectangle. Heath reaches these conclusions using 6.1 for ratio transfer (AF:FG = AI:FK and AG:GD = AK:KD) and 6.26 for the same-diameter square construction, while the AI uses 10.13 (transitivity of incommensurability), 10.22 (medial square applied to rational line), 2.5 (bisection identity), and explicit definitions D10.1.3 and D10.1.4 to establish the same intermediate incommensurabilities through a slightly different but equivalent route. The AI also cites 10.41 which is not strictly needed. Since the logical backbone is identical -- both decompose the sixth apotome, partition via 10.18, establish mediality via 10.21, and conclude via 10.78 -- and the citation differences reflect alternative ways of licensing the same geometric facts at different levels of granularity, this is Case A of Q2: same backbone, different citation depth.

### 10.97
**Category**: Granularity difference
**Jaccard**: 0.471
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs establish the same key intermediate conclusions: (1) the 'whole' part of the breadth is rational and commensurable in length with the rational line CD, (2) the 'annex' part is rational and incommensurable in length with CD, (3) the two parts are incommensurable in length and both rational, making the breadth an apotome by 10.73, and (4) the commensurability condition required by 10.17 holds, making it specifically a first apotome per D10.3.1. The AI's eight additional citations (10.12, 10.13, 10.15, 10.19, 10.21, D10.1.1, D10.1.3, D10.1.4) are over-citations representing intermediate commensurability results and definitions that Heath leaves implicit. Heath's sole extra citation (6.17) reflects a geometric mean-proportional construction used to set up the condition for 10.17, whereas the AI reaches the same condition through a more algebraic ratio-based argument. The backbone is identical despite the different citation depth.

### 10.98
**Category**: Granularity difference
**Jaccard**: 0.529
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) the components are medial lines commensurable in square only with rational rectangle, (2) the sum of squares is medial so the corresponding breadth is rational and incommensurable with the rational line, (3) twice the rectangle is rational so the other breadth is rational and commensurable with the rational line, (4) the two breadths are rational and commensurable in square only so their difference is an apotome, (5) the square on the greater exceeds the square on the lesser by a commensurable square, and (6) the annex is commensurable with the rational line, making it a second apotome. The citation differences reflect alternative methods for establishing the same conclusions: the AI uses 10.13 where Heath uses VI.1 plus 10.11 to show incommensurability of the breadths, and the AI invokes 10.14 directly to transfer the commensurability-of-excess property where Heath constructs an explicit geometric argument using bisection, mean proportionals (6.17, 5.11), and 10.17. The AI also explicitly cites definitions D10.1.2 and D10.1.4 that Heath uses implicitly. Since all key intermediate conclusions match and only the justification depth and specific proposition choices differ, this is a granularity difference.

### 10.99
**Category**: Granularity difference
**Jaccard**: 0.579
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: decomposing the second apotome of a medial straight line into its components AG and GB, applying their squares and twice their rectangle to a rational straight line CD, showing the resulting breadths are rational and incommensurable in length (via 10.22), establishing incommensurability between the sum-of-squares area and twice-the-rectangle area (via 10.13, 6.1, 10.11), concluding the breadth is an apotome (via 10.73), and finally verifying it is specifically a third apotome by showing neither component is commensurable with CD and the square on the whole exceeds the square on the annex by a commensurable amount (via 10.17 and D10.3.3). The citation differences are all depth-related: the AI adds 10.5, 10.6, 10.14, 10.81, 6.20, D10.1.3, and D10.1.4 as explicit supporting citations for steps Heath handles implicitly, while Heath cites 5.11 (transitivity of ratios) for a proportion chain that the AI handles without explicit citation. These are citation-depth differences with identical key intermediate conclusions, yielding Granularity difference.

### 10.100
**Category**: Granularity difference
**Jaccard**: 0.450
**Analysis**: Both proofs establish the same key intermediate conclusions: (1) the sum of squares on AG, GB applied to the rational line gives a rational breadth commensurable with the rational line (via 10.20), (2) twice the rectangle AG, GB applied gives a rational breadth incommensurable with the rational line (via 10.22), (3) these breadths are incommensurable with each other making the total breadth an apotome (via 10.73), (4) the squares on AG, GB correspond to incommensurable segments, and (5) the square on the larger term exceeds the square on the smaller by the square on a line incommensurable with the larger (via 10.18), yielding a fourth apotome (via D10.3.4). The backbone is identical. The citation differences arise because Heath uses a proportion chain through 5.11 and 6.17 to show rect(CK,KM) = 1/4 sq(FM) before invoking 10.18, while the AI more directly invokes 10.17/10.18 by establishing the incommensurability of the segments DH and HK. The AI also explicitly cites lower-level propositions (10.13, 10.16, CN2, CN3, 2.1, 2.5, D10.1.3, D10.1.4) that Heath leaves implicit. These are citation-depth differences for the same logical backbone, so Q2 Case A applies, giving classification G.

### 10.101
**Category**: Granularity difference
**Jaccard**: 0.727
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) establishing CL (or CM in Heath's labeling) as rational and incommensurable with CD via 10.22, (2) FL (FM) as rational and commensurable with CD via 10.20, (3) concluding the difference is an apotome via 10.73, (4) showing CH and KL are incommensurable, (5) applying 10.18 to establish that the square on CL exceeds the square on FL by a square incommensurable with CL, and (6) concluding the result is a fifth apotome via D10.3.5. The citation differences are in how each proof reaches the same intermediate facts: Heath uses VI.1 (6.1) to convert proportionality of rectangles with a common side into proportionality of their other sides, then applies X.11 to derive incommensurability; the AI instead uses 10.13 (transitivity of incommensurability) directly and 10.15 (commensurability of sums) in a contradiction argument to support the application of 10.18. These are alternative citation-depth routes to identical geometric conclusions, making this a granularity difference.

### 10.102
**Category**: Granularity difference
**Jaccard**: 0.889
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: decomposing AB via its annex using 10.78, applying the sum of squares and twice the rectangle to the rational line CD to obtain rational breadths incommensurable with CD (10.22), establishing the incommensurability of those breadths (6.1, 10.11), concluding the result is an apotome (10.73), then showing it satisfies the sixth apotome conditions via 10.18 and D10.3.6. The AI proof reaches every key intermediate conclusion that Heath's proof does, just with more verbose exposition and some false starts. The only citation difference is that the AI adds 2.4 (square on a sum) as an extra reference during its exploratory steps, while Heath does not cite it. Heath's proof has no citations absent from the AI's set. This is a clear Case A situation: same backbone, with the AI over-citing a basic algebraic identity.

### 10.103
**Category**: Granularity difference
**Jaccard**: 0.316
**Analysis**: Q2 decided the classification. Both proofs share the same geometric backbone: they establish that AE and BE are rational commensurable in square only (the annex construction), derive the proportionality AE:CF = BE:DF = AB:CD, show CF and FD are each commensurable in length with AE and BE respectively, prove CF and FD are rational and commensurable in square only (making CD an apotome), and then transfer both the excess-of-squares condition and commensurability with the rational line to establish the same order. The difference lies entirely in which Book V/VI proportionality lemmas are used to justify the same algebraic manipulations: Heath uses 5.12 (as one to one so all to all) and 5.16 (alternando) while the AI uses 5.17 (separando), 5.11 (transitivity of ratios), and 6.22 (proportional lines yield proportional squares). The AI also over-cites definitions (D10.1.3, D10.3.1-D10.3.6) and 10.5. Since the key intermediate conclusions are identical and only the citation depth for proportionality sub-steps differs, this is a granularity difference.

### 10.104
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) the parts CF, DF are individually medial, (2) CF, DF are commensurable in square only, (3) the rectangle CF*DF is commensurable with rectangle AE*EB, and (4) CD is the same order of apotome of a medial as AB. The citation differences are all at the level of which specific proportionality or commensurability lemmas are invoked to reach these shared conclusions. Heath uses 5.12 (proportional antecedents/consequents) while the AI uses 5.19 (separando); Heath uses 5.16 (alternando) while the AI uses 6.16 and 6.22 (rectangle and similar-figure proportions); Heath uses 10.13 (commensurable + incommensurable implies incommensurable) directly while the AI re-derives its content via a contradiction argument using 10.12, which is the key lemma inside Heath's proof of 10.13 (satisfying the proof-tree containment test). The AI's additional citations of P1 and P2 are construction postulate over-citations. All these represent citation-depth differences, not backbone differences.

### 10.105
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Both proofs establish the same three key intermediate conclusions needed to show CD is minor: (1) CF and FD are incommensurable in square, (2) the sum of the squares on CF and FD is rational, and (3) the rectangle CF by FD is medial. The logical backbone is identical. The citation differences reflect different technical routes to these same conclusions. Heath uses V.12, V.16, and V.18 (componendo) to manipulate proportions and transfer commensurability of sums via the ratio of sums-of-squares to individual squares, while the AI establishes individual commensurabilities of AE with CF and EB with FD first (via 10.11), then builds commensurability of the sums directly using 10.15 and 10.12. The AI also cites 10.82 (uniqueness of decomposition) and 6.12/5.19 for construction, which are supplementary to the backbone. Heath cites 10.13 for transferring incommensurability where the AI uses the equivalent reasoning through 6.22 and 10.11. Since Q2 Case A holds -- same backbone with different citation depth -- the classification is G.

### 10.106
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determines this classification. Heath's proof works directly with the annex decomposition: it identifies the parts AE, EB of AB (incommensurable in square, medial sum of squares, rational rectangle), constructs analogous parts CF, FD for CD, and transfers the defining properties via commensurability ratios, concluding by 10.77. The AI proof takes a fundamentally different route through the apotome classification theory: it applies the square on AB to a rational line to obtain a fifth apotome breadth (10.101), shows the corresponding breadth for CD is commensurable and hence also a fifth apotome (10.103), then invokes 10.95 to conclude that CD is a line producing with a rational area a medial whole. The key intermediate conclusions are entirely different -- Heath's backbone involves annex decomposition properties while the AI's backbone involves fifth apotome characterization -- establishing Case B (different backbone) at Q2. The AI's alternative path is logically complete and valid at Q3, yielding classification D.

### 10.107
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof works directly with the geometric characterization from 10.78, showing that the components of CD (namely CF, FD) inherit the three defining properties (incommensurable in square, medial sum of squares, medial rectangle, with these two incommensurable) from the components of AB (namely AE, EB) via commensurability. The AI proof takes an entirely different route through the apotome classification system: it applies the squares to a rational line to obtain sixth apotomes (via 10.102), transfers the apotome order through commensurability of breadths (via 6.1, 10.11, and 10.103), and converts back to the desired line type (via 10.96). The key intermediate conclusions are completely different -- Heath argues through properties of the annex components while the AI argues through apotome orders of applied areas. The Jaccard similarity of 0.0 with zero citation overlap confirms the entirely different proof strategies. The AI's path is logically complete and valid under Q3, so the classification is D (Path difference).

### 10.108
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: they apply the rational and medial areas to a rational straight line, derive that the resulting breadths are rational and commensurable in square only (using 10.20, 10.22, and 10.13), invoke 10.73 to conclude the difference is an apotome, then split into the same two cases — first apotome yielding an apotome side (D10.3.1, 10.91) and fourth apotome yielding a minor side (D10.3.4, 10.94). The AI's four extra citations (10.11, 10.12, D10.1.3, D10.1.4) provide additional granular justification for why the medial area applied to a rational line produces a breadth that is rational and incommensurable in length, whereas Heath simply cites 10.22 directly. Since heath_only is empty and the ai_only items are all lower-level supporting propositions and definitions that elaborate on the same conclusions Heath reaches more tersely, this is a citation-depth difference, not a path difference.

### 10.109
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decides this classification as G (Granularity difference). Both proofs share the same logical backbone: they apply the medial and rational areas to a rational line, establish that the resulting breadths are rational lines commensurable in square only (via 10.13), conclude the difference is an apotome (via 10.73), then split into two cases depending on whether the square excess is commensurable or incommensurable, yielding a second apotome (leading to a first apotome of a medial via 10.92) or a fifth apotome (leading to a line producing with a rational area a medial whole via 10.95). The AI's four extra citations (10.12, 10.20, 10.22, D10.1.3) are all explicit justifications for intermediate steps that Heath states without citation: 10.20 and 10.22 justify why the applied breadths have the stated commensurability properties, 10.12 provides a transitivity step, and D10.1.3 explicitly invokes the definition of rational lines commensurable in square. Since heath_only is empty and all ai_only items support the same conclusions Heath reaches implicitly, this is a citation-depth difference with identical backbone.

### 10.110
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided this classification. Both proofs establish the same key intermediate conclusions in the same order: (1) applying medial areas to a rational line yields rational breadths incommensurable in length with that line (10.22), (2) the breadths are incommensurable with each other (6.1, 10.11), (3) the breadths are rational and commensurable in square only, (4) their difference is an apotome (10.73), (5) a case split based on whether the apotome is a third apotome (yielding a second apotome of a medial straight line via 10.93) or a sixth apotome (yielding a line producing with a medial area a medial whole via 10.96). The AI proof's additional citations (1.45 for area application, 10.12 for commensurability of squares, D10.1.3 for the rational line definition, and D10.3.1/D10.3.2/D10.3.4/D10.3.5 for explicitly ruling out other apotome types) are all construction steps, definitions, or over-citations that make explicit what Heath leaves implicit. With heath_only empty and identical logical backbones, this is a granularity difference.

### 10.111
**Category**: Path difference
**Jaccard**: 0.636
**Analysis**: Q2 reveals different logical backbones: Heath derives a contradiction by showing a segment EG is both an apotome (via 10.73, using 10.13 for incommensurability transfer) and rational, while the AI derives a contradiction by showing q+h (the sum of the lesser binomial term and the apotome annex) is both rational (via 10.15 and D10.1.3) and irrational (a binomial via 10.36). The key intermediate conclusions differ substantially: Heath uses 10.13 to transfer incommensurability and 10.73 to classify EG as an apotome, whereas the AI algebraically manipulates the expressions w = p+q and w = g-h, establishes commensurability properties of q and h individually, and applies 10.36 to reach the contradiction. Since the backbones differ (Case B in Q2) and the AI's chain is logically sound under Q3, the classification is D.

### 10.112
**Category**: Path difference
**Jaccard**: 0.156
**Analysis**: Q2 determines this classification as D (Path difference). Heath's proof constructs auxiliary points G, H, K on line segments and builds the apotome structure of EF directly through elaborate proportion chains using VI.16, V.17, V.12, V.11, VI.22, D5.9, and X.20, establishing FK and KE as the terms of the apotome. The AI takes a fundamentally different route: it shows that sq(BD) - sq(DC) is rational (via 10.15 and 10.12), uses 2.5 to express BC*(BD-DC) = sq(BD)-sq(DC), and then via 6.1 and 10.11 establishes that EF is commensurable in length with BD-DC. Since BD-DC is itself an apotome (by 10.73), the AI invokes 10.103 (a line commensurable with an apotome is an apotome of the same order) to conclude that EF is an apotome of the same order. The terms and ratio argument follows by scaling. These are genuinely different logical backbones: Heath directly constructs the terms of the apotome through proportion manipulation, while the AI leverages the higher-level result 10.103 to transfer the apotome structure. The proof-tree containment test confirms this is not mere granularity difference, since many of Heath's citations (6.16, 6.22, 5.17, 5.14, 10.20, D5.9) do not appear inside the proof of 10.103, and the AI's key intermediate conclusion (EF commensurable with BD-DC) has no counterpart in Heath's proof. The AI proof is logically complete under the hardened 1(b) standard.

### 10.113
**Category**: Granularity difference
**Jaccard**: 0.233
**Analysis**: Q2 decides this as Granularity difference (Case A). Both proofs follow the same logical backbone: they establish that the terms of the apotome are rational and commensurable in square only (10.73), set up a proportion between the terms of the resulting binomial and the terms of the apotome (6.16), show the binomial terms are rational and commensurable in square only (10.11), conclude the result is binomial (10.36), and match the order (10.14). The AI's ai_only citations are predominantly over-citations: CN1 and CN3 are common notions, D10.2.1-D10.2.6 and D10.3.1-D10.3.6 are exhaustive order definition citations, 6.22 replaces Heath's use of D5.9 for duplicate ratios (same mathematical content), and 10.112 is used only as a verification step. The heath_only substantive items (10.12, 10.15, 5.11, 5.14, 5.16) are infrastructure propositions for proportion manipulation and commensurability transitivity that the AI applies implicitly without explicit citation. The Jaccard of 0.233 is low primarily due to the AI's exhaustive definition citations and Heath's granular proportion lemma citations, but the key intermediate conclusions and logical structure are the same.

### 10.114
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: construct a rational line, apply its square to the binomial CD to obtain an apotome (by 10.112), show the terms of the new apotome are commensurable with the terms of the original apotome, use alternando and the remainder proportion (5.19) to show AB is commensurable with the new apotome, use rectangle proportionality (6.1) to show the target rectangle is commensurable with the square on the rational line, and conclude rationality. The key intermediate conclusions are identical. The citation differences are purely at the granularity level: the AI explicitly cites 10.5 and 10.6 to establish commensurability through the number-ratio route, while Heath cites 10.11 (proportional commensurability transfer) to accomplish the same steps. The AI also explicitly cites 5.16 (alternando), CN1, and D10.1.4, which Heath invokes implicitly or without citation. These are all depth-of-citation differences, not differences in the logical backbone.

### 10.115
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: they construct an infinite sequence of irrational lines by repeatedly forming a square equal to the rectangle of the previous line and a rational line, show each line is irrational via 10.20 and D10.1.4, and argue that none of the constructed lines coincides with any previously named irrational type. Heath's proof is terse, summarizing the distinctness argument in one sentence ('the square on none of the preceding, if applied to a rational straight line produces as breadth a medial straight line'). The AI proof exhaustively verifies distinctness from each of the 13 named irrational types by citing the specific breadth propositions (10.60-10.65, 10.97-10.102) and additional supporting results (10.21, 10.22, 10.36, 10.111, 2.14, D10.1.3). Since heath_only is empty and all ai_only items are elaborations of steps Heath handles tersely, this is Case A of Q2: same key intermediate conclusions at different citation depth, yielding G.


## Book 11

| Category | Count |
|---|---|
| Perfect match (P) | 2 |
| Granularity difference (G) | 28 |
| Path difference (D) | 8 |
| AI proof error (E) | 1 |

**Total**: 39 propositions

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume for contradiction that part AB of line ABC lies in the reference plane while part BC is elevated, construct a line BD continuing AB within the reference plane, then derive a contradiction from the fact that the extension of AB beyond B is unique (so BC and BD must coincide, yet one is in the plane and the other is not). Heath arrives at this contradiction via an implicit common-segment impossibility argument citing no explicit references, while the AI explicitly invokes D1.4 (straight line lies evenly with its points), D1.7 (plane surface lies evenly with straight lines on itself), and P2 (finite straight line can be produced) to justify the same uniqueness conclusion. Since heath_only is empty and ai_only contains only definitions and a postulate, this is a classic Case A granularity difference: same key intermediate conclusions, different citation depth.

### 11.2
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use a contradiction argument via XI.1 to establish that triangle ECB is in one plane, then extend this to show the full lines AB and CD lie in that plane, and finally generalize to show every triangle is in one plane. The AI's ai_only citations (P1, P2) are postulates cited for construction steps (drawing straight lines and extending lines), which Heath uses implicitly without citation. The heath_only set is empty, confirming no substantive propositions are missing from the AI proof. This is a classic over-citation pattern where the AI explicitly references basic postulates that Heath takes for granted, making it a granularity difference rather than a path difference.

### 11.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs use the same reductio ad absurdum backbone: assume the common section is not straight, draw two distinct straight lines DEB and DFB from D to B in the respective planes, observe that two straight lines would enclose a space (absurd), and conclude the common section must be straight. The AI proof adds explicit citations to P1 (drawing straight lines), D1.4 (definition of straight line), and 11.1 (a line joining two points in a plane lies entirely in that plane) where Heath's proof cites nothing at all, leaving these foundational steps implicit. Since heath_refs is empty and all ai_only items are either postulates, definitions, or an early proposition making explicit what Heath assumes, this is a citation-depth difference with the same logical backbone, satisfying Case A of Q2.

### 11.4
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: they set up equal segments AE=EB and CE=ED from E, draw an arbitrary line GEH through E, and then establish the chain of equalities GE=EH, AG=BH, FA=FB, FC=FD, FG=FH, culminating in angle GEF = angle HEF via I.8 to prove EF is perpendicular to the arbitrary line and hence to the plane. The AI uses a symmetrically equivalent triangle pair (AEC/BED yielding AC=BD) compared to Heath (AED/CEB yielding AD=CB), and routes through triangles GCF/HDF rather than Heath's implicit FAG/FBH path, but these are minor presentational variations that establish the same key intermediate conclusions. The ai_only set consists entirely of construction references (1.3, P1, 11.2), axioms/common notions (CN3, P4), and a definition (D1.10) that Heath uses implicitly but does not cite. The heath_only set is empty, confirming the AI cited a superset of Heath's references. This is a citation-depth difference, not a backbone difference.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs employ the same proof-by-contradiction backbone: assume one of the three lines is not in the plane determined by the other two, use 11.4 to establish that AB is perpendicular to that plane, use 11.3 to find the common section line BF of two intersecting planes, invoke D11.3 to conclude that angle ABF is right, note the given right angle with the assumed-out-of-plane line, and derive a contradiction from the impossibility of two equal right angles on distinct lines in one plane. The AI proof differs only in explicitly citing P4 (to equate the right angles) and CN5 (whole greater than part, for the contradiction), which Heath leaves implicit by simply stating 'which is impossible.' Since heath_only is empty and ai_only contains only axiom-level citations (P4, CN5) that make explicit what Heath's proof uses implicitly, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 11.6
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) AD = BE, (2) angle ADE is right, (3) BD, DA, DC are coplanar via XI.5, (4) AB parallel to CD via I.28. The difference lies in citation depth: Heath uses I.4 (SAS) to show AD = BE and I.8 (SSS) to transfer the right angle, while the AI uses I.47 (Pythagorean theorem) and I.48 (its converse) to reach the same conclusions via metric computation. The proof-tree containment test confirms that I.4 appears inside Heath's proof of I.47 and I.8 appears inside Heath's proof of I.48, so the AI cites higher-level results that subsume the lower-level tools Heath deploys. The AI's remaining ai_only items (1.11, 1.3, P1, P4, CN1) are construction props, postulates, and common notions, indicating over-citation. Heath's citation of 11.2 (every triangle is in one plane) is handled informally by the AI in Step 12 without explicit citation, a minor under-citation. Since the backbone conclusions are the same and the citation differences are explained by depth, this is a granularity difference.

### 11.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined this classification. Heath's proof argues by contradiction using 11.3: assuming the joining line EGF is in a more elevated plane, a plane through EGF intersects the reference plane in a straight line EF (by 11.3), producing two distinct straight lines between the same endpoints that enclose an area, which is impossible. The AI proof takes a fundamentally different path: it establishes that both endpoints E and F lie in the plane P (since they lie on the parallel lines which are in P by D1.23), then argues by contradiction using 11.1 that if EF were not entirely in P, part would be in P and part elevated, directly contradicting 11.1. The key intermediate conclusions differ — Heath's pivotal step is constructing a planar section via 11.3 to get two lines between the same points, while the AI's pivotal step is showing both endpoints are in the plane and invoking 11.1 to force the entire line into the plane. Both arguments are logically complete and valid, but they proceed through different geometric reasoning, yielding a Jaccard of 0.0 with entirely disjoint citation sets.

### 11.8
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) angle CDB is right via I.29 and the parallel lines, (2) AD equals BE, (3) angle ADE/EDA is right so ED is perpendicular to AD, (4) ED is perpendicular to the plane through BD and DA via XI.4, (5) CD lies in that plane, and (6) CD is perpendicular to the plane of reference via XI.4 again. The difference lies in how certain intermediate results are derived: Heath uses implicit SAS and SSS triangle congruence (I.4 and I.8, which are not even in his citation list) to establish AD = BE and angle EDA = right, while the AI uses the Pythagorean theorem (I.47) and its converse (I.48) to reach those same conclusions. The ai_only set {1.11, 1.3, 1.47, 1.48, CN1, P1} consists of construction/postulate over-citations (1.11, 1.3, P1, CN1) and the Pythagorean approach (1.47, 1.48), while the heath_only item {11.2} is used by Heath to place CD in the plane through BD and DA, which the AI handles through 11.7 at Step 13 to the same effect. Since all key conclusions are the same and the differences are purely in citation depth and auxiliary lemma choice, this is Case A of Q2.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct perpendiculars GH and GK to EF in the respective planes, show EF is perpendicular to the plane through GH and GK (11.4), use parallelism to transfer perpendicularity to AB and CD (11.8), then conclude AB is parallel to CD (11.6). The AI adds two extra citations not in Heath: 1.11 (explicitly citing the construction of perpendiculars, which Heath performs implicitly) and 1.29 (establishing that GH is perpendicular to AB and GK is perpendicular to CD via parallel line properties, an intermediate step Heath does not include). These are over-citations providing additional granularity on the same argument, not a different proof path. Since heath_only is empty and the ai_only items are construction and supporting propositions that elaborate the same backbone at finer detail, this is Case A of Q2: same backbone, different citation depth.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: cut off equal segments on the meeting lines, show that two auxiliary segments (AD/GD and CF/HF) are each equal and parallel to BE via I.33, conclude those two auxiliary segments are parallel and equal to each other via XI.9 and transitivity, then show the bases (AC/GH and DF) are equal and parallel via I.33, and finally conclude the angles are equal by SSS (I.8). The AI proof is structurally identical to Heath's but explicitly cites additional foundational items that Heath uses implicitly: I.3 for cutting off equal segments, XI.7 for establishing coplanarity of parallel lines, CN1 for transitivity of equality, and P1 for joining lines. Since heath_only is empty and all ai_only items are construction, axiomatic, or auxiliary citations present implicitly in both proofs, this is Case A of Q2: same backbone, different citation depth.

### 11.11
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of proposition 11.11 follows the exact same logical structure as Heath's proof, establishing identical key intermediate conclusions in the same order: (1) BC is at right angles to the plane through ED and DA via 11.4, (2) GH is at right angles to that same plane via 11.8 since GH is parallel to BC, (3) GH is at right angles to AF via D11.3, (4) AF is at right angles to both GH and DE, and (5) AF is therefore at right angles to the reference plane via 11.4. The citation sets are identical (ai_used = heath_refs = {1.11, 1.12, 1.31, 11.4, 11.8, D11.3}) with Jaccard similarity 1.0, and both proofs share the same backbone of key conclusions. Since both the logical backbone and the citation sets match exactly, the classification is Perfect match (P).

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: conceive an elevated point B, draw BC perpendicular to the plane via 11.11, draw AD parallel to BC through A via 1.31, and conclude AD is perpendicular to the plane via 11.8. The AI proof adds two over-citations (D11.3 for the definition of perpendicularity to a plane, and P1 for drawing a line), which are a definition and a postulate respectively, and also handles a trivial special case where the foot of the perpendicular coincides with A. Since heath_only is empty and ai_only contains only definitional/postulatory items, this is a classic Case A granularity difference: same backbone, different citation depth.

### 11.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: assume two perpendiculars AB, AC from point A to a plane, establish their coplanarity, find the intersection line DAE of the two planes via 11.3, show both angles with DAE are right via D11.3, then derive a contradiction. The AI proof explicitly cites 11.2 (two intersecting lines are in one plane), P4 (all right angles are equal), and CN5 (the whole is greater than the part) to justify steps that Heath leaves implicit. Since heath_only is empty and the three ai_only items (11.2, CN5, P4) are a construction proposition, a common notion, and a postulate that make explicit what Heath takes for granted, this is a same-backbone, different-depth case — classic granularity difference.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume the planes are not parallel, derive a common section line (11.3), pick a point on it to form a triangle with the endpoints of the perpendicular line, show both base angles are right using D11.3 (perpendicularity to each plane), and reach a contradiction via 1.17 (two angles of a triangle must be less than two right angles). The AI proof adds two extra citations not in Heath: P1 (to justify joining points) and 11.2 (to justify the triangle lies in one plane). These are construction-level and supporting-detail over-citations that do not alter the logical backbone. Heath's proof omits these as implicit. Since the key intermediate conclusions match at every logical position and the citation differences reflect only depth of justification, this is a granularity difference (G).

### 11.15
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 11.15 follow an identical logical backbone: construct BG perpendicular to the plane through DE, EF (11.11), draw parallels GH to ED and GK to EF in that plane (1.31), establish right angles BGH and BGK via the definition of perpendicularity to a plane (D11.3), use transitivity of parallels (11.9) to show AB is parallel to GH and BC to GK, apply the co-interior angle theorem (1.29) to deduce that angles GBA and GBC are right, conclude GB is perpendicular to the plane through AB, BC (11.4), and finally invoke that planes perpendicular to the same line are parallel (11.14). The citation sets are exactly identical with Jaccard similarity 1.0, and the key intermediate conclusions match perfectly. Since ai_used equals heath_refs exactly and both proofs argue through the same intermediate steps, the classification is P (Perfect match).

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: a proof by contradiction showing that if the common sections EF and GH of parallel planes met at a point K, then K would lie in both parallel planes, contradicting their being parallel, hence the lines are parallel by definition. The citation differences are all at the granularity level: the AI explicitly cites 11.3 (common sections are straight lines) and D11.8 (definition of parallel planes) where Heath leaves these implicit, while Heath cites 11.1 to justify that K lies in plane AB whereas the AI reasons directly from the definition of common section without needing 11.1. Since the key intermediate conclusions (K in both planes, contradiction with parallelism, conclusion of line parallelism) are identical in both proofs and the differences are only in citation depth, this is a granularity difference.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: join AD, find its intersection with the middle plane, use XI.16 twice to establish two parallel lines (EO||BD and AC||OF in Heath; EG||BD and GF||AC in the AI), apply VI.2 twice to obtain proportionality in two triangles sharing the segment AD, then use V.11 to chain the equal ratios and conclude AE:EB = CF:FD. The only citation difference is that the AI additionally cites P1 (the postulate for joining straight lines), which is a construction postulate constituting over-citation. Since the key intermediate conclusions are the same and the citation difference is limited to a construction postulate, this is a granularity difference (Case A of Q2).

### 11.18
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as D (path difference). Heath and the AI reach the same conclusion (the tilted plane is perpendicular to the reference plane) through genuinely different intermediate conclusions. Heath constructs a line FG in the tilted plane perpendicular to the common section, proves FG is parallel to AB via I.28, then deduces FG is perpendicular to the reference plane via XI.8, and applies XI.Def.4. The AI instead constructs a line AG in the reference plane perpendicular to the common section, shows AG is perpendicular to both AB and CE (which lie in the tilted plane Q) via D11.3, deduces AG is perpendicular to plane Q via XI.4, and then applies D11.4. The key intermediate conclusions differ: Heath's backbone relies on parallelism (AB parallel to FG) while the AI's backbone relies on perpendicularity to a plane (AG perpendicular to plane Q via the two-line criterion). Both paths are logically complete and valid, but they employ different geometric strategies and different substantive propositions (heath_only: 1.28, 11.8 vs ai_only: 11.3, 11.4).

### 11.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) construct a perpendicular within each plane to its common section with the reference plane, (2) apply D11.4 to show each constructed perpendicular is perpendicular to the reference plane, and (3) invoke 11.13 to force the conclusion that BD is perpendicular to the reference plane. The AI uses a direct proof structure while Heath uses proof by contradiction, but the key geometric facts are identical. The AI's extra citations (1.11 for constructing perpendiculars in a plane, 11.3 for the common section being a straight line) are construction and infrastructure propositions that Heath uses implicitly without citation, representing over-citation rather than a different logical path. Heath_only is empty, confirming the AI covers all of Heath's cited material. This is Case A: same backbone, different citation depth.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) construct angle BAE equal to angle DAB with AE equal to AD, (2) apply SAS congruence (I.4) to obtain DB = BE, (3) use the triangle inequality (I.20) on triangle BDC to derive DC > EC, (4) apply I.25 to conclude angle DAC > angle EAC, and (5) combine to show DAB + DAC > BAC. The AI's additional citations (1.23, 1.3, P1) are all construction-level propositions and a postulate that Heath uses implicitly without citing. Heath says 'let the angle BAE be constructed equal to the angle DAB' without citing I.23, 'let AE be made equal to AD' without citing I.3, and 'let DB, DC be joined' without citing P1. The AI explicitly cites these construction steps, making the difference purely one of citation depth rather than logical backbone. This is a clear Case A granularity difference.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct triangles from the solid angle vertex to a base figure, apply XI.20 at each base vertex to show the paired base angles exceed the corresponding base figure angle, sum these inequalities, compute total triangle angles via I.32, and subtract to conclude the face angles sum to less than four right angles. The AI generalizes Heath's 3-face proof to n faces using an n-sided polygon cross-section rather than a triangle, but this is a generalization of the same method, not a different path. The ai_only citations (11.2, CN2, CN3, CN5, P1) are all over-citations: 11.2 explicitly justifies that each triangle is in a plane (implicit in Heath), and the common notions and postulate are axioms Heath invokes without citation. heath_only is empty, confirming the AI covers all of Heath's cited dependencies. The proofs establish the same key intermediate conclusions at the same logical positions, differing only in citation granularity.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they handle the trivial equal-angles case, then for the unequal case construct auxiliary triangles using SAS congruence (I.4) to transfer chord lengths to a common vertex, apply I.24 to compare bases via angle comparison, and use the triangle inequality to establish that the sum of two chords exceeds the third. The AI proof is more verbose and has some false starts in its construction, but the final argument (Steps 14-24) follows the same key intermediate conclusions as Heath. The heath_only set is empty, confirming the AI covers all of Heath's reasoning. The ai_only set consists entirely of over-citations: construction propositions (1.23, 1.3), axioms (CN5, P1), and propositions Heath uses implicitly without citation (1.20 for triangle inequality, 1.22 for the final construction, 1.5 for isosceles base angles). This is Case A of Q2: same backbone with different citation depth.

### 11.23
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same key intermediate conclusions: construct triangle LMN from sides AC, DF, GK using XI.22; circumscribe a circle about LMN with center O; establish that AB > OL; erect a perpendicular from O to the plane of the circle; show that PL = PM = PN = AB via the Pythagorean theorem (I.47); and use SSS congruence (I.8) to establish that the solid angle's plane angles equal the given angles. The critical difference lies in how each proof establishes AB > OL: Heath provides a rigorous two-case contradiction using detailed proportional reasoning through VI.2, I.29, VI.4, V.16, and I.25, plus I.4 for congruence, while the AI provides a compressed but logically sound argument based on central angle sums versus given angle sums without citing these specific sub-steps. The heath_only citations (1.25, 1.29, 1.4, 5.16, 6.2, 6.4) all serve Heath's detailed proof of the sub-case 'AB is not less than LO,' and the ai_only citations (1.22, 1.3, 4.5, D1.15, D11.11, D11.3, D3.1, P1) are construction, definitional, and postulate references that Heath treats as implicit. This is a classic same-backbone, different-depth scenario.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: use XI.16 to establish that opposite edges of the solid are parallel, thereby showing each face is a parallelogram; then use XI.10 for equal angles between non-coplanar parallel lines, I.34 for equal sides of parallelograms, I.4 for SAS triangle congruence, and I.34 again to conclude that each parallelogram is double the congruent triangle and therefore opposite faces are equal. The AI proof is more explicit, citing D1.22 (definition of parallelogram) where Heath applies it implicitly, citing CN1 and CN2 (common notions for transitive equality and doubles of equals) where Heath leaves them implicit, and using 1.8 (SSS) for a secondary triangle congruence that Heath handles via 'similarly we can prove.' All ai_only items (1.8, CN1, CN2, D1.22) are over-citations reflecting greater explicitness, not a different proof path. Heath_only is empty. This is Case A of Q2: same backbone, different citation depth.

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs follow the same equimultiple strategy: they cut the parallelepiped with a parallel plane to form two sub-parallelepipeds, construct m-fold and n-fold copies of these sub-solids by extending the base segments, show each copy is equal to the original sub-solid (via XI.24), establish that the ordering of the m-fold and n-fold bases matches the ordering of the m-fold and n-fold solids, and conclude proportionality by V. Def. 5. The key intermediate conclusions are identical in both proofs. The AI cites additional lower-level results that Heath uses implicitly: 1.33 and 1.34 for parallelogram properties, 11.16 for intersections of parallel planes, 6.1 for ratios of parallelograms, CN4 and CN5 for common notions, and D11.10 for the definition of equal solid figures. Since heath_only is empty and all ai_only items are supporting sub-steps of the same logical backbone, this is a granularity difference (Case A of Q2).

### 11.26
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 reveals genuinely different logical backbones, leading to classification via Q3. Heath constructs the solid angle directly using perpendiculars to planes (11.11 to drop a perpendicular from an elevated point, 11.12 to erect a perpendicular from a point in a plane, and D11.3 for the definition of perpendicularity to a plane), constructing only two face angles explicitly and then proving the third face angle matches via congruent triangles (I.4, I.8). The AI takes a fundamentally different approach: it constructs all three face angles explicitly at the vertex using I.23 and I.3, verifies the conditions of 11.20 (any two face angles sum to more than the third) and 11.21 (all three sum to less than four right angles), then invokes 11.23 as a black-box existence theorem to assert that a solid angle with those face angles can be constructed. The AI's path is logically valid under Q3: the chain from premises to conclusion is complete, with 11.23 providing the key construction step that replaces Heath's perpendicular-based approach. The large symmetric difference (Jaccard 0.25) reflects this genuine path divergence rather than mere granularity differences.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a solid angle at A equal to the solid angle at C, set up proportional edges using VI.12/6.12, derive the third proportion via V.22/5.22 ex aequali, show that three pairs of corresponding faces are similar parallelograms (by equal angles with proportional sides), note that opposite faces are equal and similar, and conclude by XI.Def.9 that the solids are similar. The AI proof cites all three of Heath's references (5.22, 6.12, D11.9) and adds five more (11.26 for solid angle construction, 11.24 for opposite faces being equal and similar, 11.15 and P1 for completing the solid, D6.1 for the definition of similar rectilinear figures). Heath uses all of these facts implicitly without formal citation. Since heath_only is empty and every ai_only item is an over-citation of a step Heath performs without explicit reference, this is a citation-depth difference with the same backbone, yielding category G.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) the diagonal of each opposite face bisects it into two equal triangles via I.34, (2) opposite faces of the parallelepiped are equal parallelograms, (3) the cutting plane divides the solid into two prisms, and (4) these two prisms are equal because they are contained by planes equal in multitude and magnitude (D11.10). The AI proof makes the same argument as Heath but with more explicit detail. The ai_only items (11.24, CN1, CN4, D11.13) are all over-citations where the AI makes explicit what Heath leaves implicit: Heath says 'for they are opposite' without citing 11.24, refers to prisms without citing D11.13, and uses equality reasoning without citing CN1 or CN4. heath_only is empty, confirming the AI covers all of Heath's citations. This is Case A of Q2: same backbone, different citation depth.

### 11.29
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath's proof works directly with plane geometry results (I.34, I.36, I.4, I.8), establishing specific triangle equalities (DCE=HBK, AFG=MLN) and parallelogram equalities (DG=HN) to show two prisms are equal, then adding a common solid. The AI proof takes a structurally different approach, invoking parallelepiped properties (11.24), constructing an auxiliary parallelepiped between the two top faces, using the bisection theorem (11.28), and arguing through decomposition into a common solid plus two equal prisms whose equality follows from I.8 and I.34. The AI uses I.35 (parallelograms on same base) where Heath uses I.36 (parallelograms on equal bases), and brings in 11.24 and 11.28 which Heath does not cite at all. Since I.36 is not contained in any AI-cited proposition's proof tree and represents a genuinely different approach to establishing the key parallelogram equalities, the backbones differ (Case B). Under Q3, the AI's chain is logically sound — valid propositions are cited and the decomposition argument, though verbose, runs from premises to conclusion — yielding D.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: construct an auxiliary parallelepiped, show it equals solid CM by XI.29 (standing edges on the same straight lines), show it equals solid CN by XI.29 (same reasoning for the other pair of sides), then conclude CM equals CN by transitivity. The AI proof cites additional supporting references (1.34 for parallelogram properties, 11.24 for opposite faces of parallelepipeds, CN1 for the transitivity step, and P1/P2 for line constructions) that Heath leaves implicit. Since heath_only is empty, the AI covers everything Heath cites and more. The ai_only items are all auxiliary citations providing deeper justification for the same logical steps, making this a granularity difference rather than a path difference.

### 11.31
**Category**: AI proof error
**Jaccard**: 0.125
**Analysis**: The classification was decided at Q1(b). The AI proof constructs a comparison solid RS on base FGPQ (constructed equal to LMNO via I.45) and then claims in Step 5 that solids AB (on base FGHK) and RS (on base FGPQ) are 'on the same base (sharing the side FG in the base plane)' and applies 11.29 or 11.30 to conclude AB equals RS. However, 11.29 and 11.30 both require the solids to be on THE SAME base - meaning the identical base parallelogram - not merely on equal bases that share one edge. FGHK and FGPQ are different parallelograms (equal in area but geometrically distinct), so the hypothesis of 11.29/11.30 is not satisfied. This is not a matter of compression or terseness: the AI explicitly identifies two different bases and then incorrectly claims they constitute 'the same base' for purposes of applying 11.29/11.30. Heath's proof avoids this by using a ratio argument through 11.25, 5.7, 5.9, and 5.11 to compare solids on different but related bases.
**Audit Record**: CANDIDATE E — 11.31
  violated_claim : In Step 5, the AI applies 11.29/11.30 (which require solids on 'the same base') to solids AB (on base FGHK) and RS (on base FGPQ), which are on different (though equal) bases sharing only edge FG
  failure_mode   : invalid_inference
  missing_is     : support — there is no proposition or valid argument licensing the conclusion that solids on different bases sharing one edge can be compared via 11.29/11.30, which explicitly require the same base
  evidence       : AI Step 5: 'solids AB and RS are on the same base (sharing the side FG in the base plane) and of the same height... by Proposition 11.29 the solids are equal. If not, then by Proposition 11.30 they are still equal.' But 11.29 states 'on the same base' meaning the identical parallelogram, not equal parallelograms sharing an edge. FGHK ≠ FGPQ.
  why_not_terse  : The AI explicitly identifies two distinct bases (FGHK and FGPQ) in Step 4, then incorrectly equates sharing one edge with being 'on the same base' in Step 5. This is not compression of a sound argument but misapplication of a proposition whose central hypothesis is not met. Heath's proof shows the gap is real: comparing solids on equal-but-different bases requires the ratio argument via 11.25, 5.7, 5.9, 5.11, which the AI entirely omits.

### 11.32
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a parallelogram equal to one base using I.45, complete a parallelepiped on it with matching height, apply XI.25 to establish a ratio between the solids and their bases, use XI.31 to equate the constructed solid with the other given solid, then substitute equals to reach the conclusion. The only difference is that the AI explicitly cites 5.7 (equal magnitudes have the same ratio to the same magnitude) to justify the final substitution step, while Heath performs this substitution without explicit citation. Since heath_only is empty and ai_only contains only 5.7 (a ratio-substitution principle used implicitly by Heath), this is a citation-depth difference with the same backbone, yielding category G.

### 11.33
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decides this classification as Case B (different backbone), leading to Q3 which confirms the AI's path is valid. Heath's proof constructs an auxiliary solid KP equal to CD, then builds intermediary solids EO and QL to establish a four-term continued proportion of solids (AB:EO = EO:QL = QL:KP) using XI.32 and VI.1, then applies V.Def.10 for the triplicate ratio. The AI proof takes a fundamentally different approach: it sets up a continued proportion of lengths (AE, CF, EN, EP), then separates the volume comparison into a base-ratio component (using 6.22 for similar parallelograms to get the duplicate ratio) and a height-ratio component (using 11.25 and 11.32), chaining them via 5.22 (ex aequali) to obtain AB:CD = AE:EP, which is the triplicate ratio by D5.10. These are genuinely different logical backbones. The AI's path is logically complete under the hardened Q1(b) standard: each step is supported by a cited proposition, and the chain runs from premises to conclusion, so Q3(b) holds and the classification is D.

### 11.34
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: they construct an auxiliary parallelepiped on one base with the other solid's height, establish two key proportions (the ratio of the original solids to the auxiliary via XI.32 and the ratio involving heights via XI.25/VI.1), and then combine these with ratio arithmetic (V.7/V.9) for the forward and converse directions respectively. The heath_only items (11.29, 11.30) are explained by the proof-tree containment test: both appear inside Heath's own proof of XI.31, which the AI cites as a unit. Heath re-derives the oblique-to-perpendicular reduction inline at the level of 11.34, while the AI relies on XI.31 and XI.32 already covering all parallelepipeds (perpendicular and oblique). The ai_only items (5.11, 5.18, D5.13) reflect the AI's more explicit ratio manipulation and its cutting-plane technique for establishing CD:FO = h_CD:h_AB, where Heath uses a slightly different construction but reaches the same intermediate conclusion. These differences are citation-depth variations, not backbone differences.

### 11.35
**Category**: Path difference
**Jaccard**: 0.267
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path (D). Heath's proof constructs AH equal to DM, draws HK parallel to GL, applies XI.8 to establish HK perpendicular to the plane, then works through perpendiculars from K and N to the original lines, ultimately concluding via I.8 (SSS). The AI proof instead makes DM equal to AG, drops perpendiculars from G directly to lines AB and AC using I.12, proves these feet are also the feet of perpendiculars from H (via I.47 and I.48), then proceeds through a chain of I.26 and I.4 applications to reach the conclusion via I.4 (SAS). The constructive strategies differ fundamentally: Heath uses a parallel-line construction with XI.8, while the AI uses direct perpendicular-to-line constructions with I.12 and XI.11. The intermediate conclusions also differ: Heath establishes right angles at C and F as key intermediates, while the AI establishes that perpendicular feet from G to the original lines coincide with perpendicular feet from H. The AI's final step uses I.8's converse direction (I.4 with SAS) rather than Heath's I.8 (SSS). The AI proof is logically complete and sound throughout.

### 11.36
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3. Heath's proof establishes that the base parallelograms of the two solids are equal (via VI.14, reciprocal proportion in equiangular parallelograms) and that their perpendicular heights are equal (via XI.35 Porism), then concludes equality by XI.31 (equal bases and same height implies equal solids). The AI takes a fundamentally different route: it uses VI.1 to establish that the ratio of the base areas equals A:B, combines this with the given proportion A:B = B:C and the ratio of heights B:C to show the bases are reciprocally proportional to the heights, then invokes XI.34 (the converse: reciprocally proportional bases and heights implies equal solids). Heath works with equalities throughout while the AI works with proportions and ratios. XI.35 (equal perpendiculars from elevated lines) plays no role in the AI proof, and 11.34 plays no role in Heath's proof for this proposition, confirming genuinely different logical backbones. The AI's chain is logically complete and valid, so this is a path difference.

### 11.37
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: in the forward direction, apply 11.33 to establish that each pair of similar parallelepipedal solids has the triplicate ratio of their corresponding edges, then conclude from equal base ratios that the triplicate ratios (and hence the solid ratios) are equal; in the converse, reverse the argument. The AI proof explicitly cites 5.11 for the transitivity of equal ratios, 5.9 for duplicate ratio properties, and definitions D5.9/D5.10 for the concepts of duplicate and triplicate ratio, whereas Heath leaves all of this implicit, citing only 11.33. Since heath_only is empty and all ai_only items (5.11, 5.9, D5.10, D5.9) are supporting citations for reasoning steps that Heath performs without explicit citation, this is a citation-depth difference rather than a path difference.

### 11.38
**Category**: Path difference
**Jaccard**: 0.056
**Analysis**: Q2 decided the classification. Heath's proof establishes the bisection result through triangle congruence: first showing DUE is a straight line via congruent triangles DOU and PUE (I.4, I.14), then proving triangles DTU and GTS are congruent (I.26) using alternate angles (I.29) and vertical angles (I.15). The AI takes a fundamentally different approach: it identifies the common section ST by showing S and T each lie on both cutting planes via midpoint-proportionality collinearity arguments (6.2), then constructs a parallelogram ACGE using properties of the cube's parallel faces (11.24, 1.34, 1.30, 1.33), builds a sub-parallelogram ASTG, and concludes that AG and ST bisect each other as diagonals of ASTG (1.34). The key intermediate conclusions are entirely different — Heath never forms parallelograms ACGE or ASTG, and the AI never uses triangle congruence or the straight-line arguments central to Heath. The Jaccard similarity of 0.056 with only 1.33 shared confirms the near-total divergence. The AI's path is logically complete and valid, so this is a path difference (D).

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: complete each prism to a parallelepiped, show the parallelogram bases are equal (since both are double the given triangle, via I.34), apply XI.31 to conclude the parallelepipeds are equal, then use XI.28 to note each prism is half its parallelepiped and conclude the prisms are equal. The AI's extra citations (CN1, CN3, D11.13) are common notions and a definition that Heath uses implicitly — CN1 for the transitivity step establishing base equality, CN3 for the 'halves of equals are equal' conclusion, and D11.13 as a definition. These are over-citations of axiom-level items, not substantive path differences. Since the key intermediate conclusions are identical but the citation sets differ only by these implicit axioms/definitions, this is a granularity difference (G).


## Book 12

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 10 |
| Path difference (D) | 8 |
| AI proof error (E) | 0 |

**Total**: 18 propositions

### 12.1
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish triangles ABE and FGL as equiangular via VI.6, (2) show inscribed angles AEB=AMB and FLG=FNG, (3) deduce triangles ABM and FGN are equiangular via I.32, (4) derive BM:GN=BA:GF via VI.4, and (5) conclude via duplicate ratios from VI.20. The sole heath_only citation is 3.27 (angles in equal circles on equal circumferences are equal), which the AI replaces with 3.21 (angles in the same segment are equal). Since each inscribed-angle step operates within a single circle, 3.21 is actually the more directly applicable proposition; Heath's choice of 3.27 works but is more general than necessary. The ai_only items (CN1, P4, D5.9, 5.11) are all axioms, definitions, and common notions that Heath leaves implicit. Since all key intermediate conclusions are identical and the citation differences reflect only depth of explicit citation and choice of equivalent foundational proposition, this is a granularity difference.

### 12.2
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs follow the identical exhaustion structure: assume the ratio of squares on diameters equals the ratio of one circle to an area S different from the other circle, then derive contradictions for both S < circle EFGH and S > circle EFGH using inscribed polygons, the exhaustion principle (10.1), similar polygon ratios (12.1), and proportion theory (5.11, 5.16). The AI proof's key intermediate conclusions match Heath's exactly in the same logical order. The ai_only citations (1.41, 10.1, 4.6, 5.14, CN5) are all over-citations making explicit what Heath uses implicitly: 10.1 is mentioned by name in Heath's text but not bracket-cited, 4.6 is a construction step for inscribing the square, 1.41 justifies the triangle-parallelogram area relationship, 5.14 licenses the inference from the polygon being less than the circle, and CN5 is a common notion invoked for the containment relationship. Heath_only is empty, confirming the AI cites a strict superset. This is a clear Case A granularity difference.

### 12.3
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 reveals genuinely different backbones, leading to classification via Q3. Heath proves face congruences using I.4 (SAS) and establishes similarity to the whole via XI.10 (equal angles from parallel lines in different planes) and VI.Def.1, then proves prism equality via XI.39 (prisms with parallelogram base double of triangle base are equal). The AI instead proves face congruences via edge-length ratios from VI.2 and I.8 (SSS), establishes similarity via VI.4 and Def.XI.9, and proves prism equality through an entirely different route using XI.28, XI.32, and XI.34 (parallelepiped volume theory — completing each prism to a parallelepiped and comparing via reciprocally proportional bases and heights). These are substantively different logical routes: SSS vs SAS for congruence, edge-ratio similarity vs angle-based similarity, and parallelepiped volume comparison vs direct prism equality. The heath_only citations (I.4, XI.10, XI.39, Def.VI.1) represent genuine alternative machinery, not mere depth differences. Q3 confirms the AI's path is logically valid and complete, so the classification is D.

### 12.4
**Category**: Path difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Heath's proof establishes the key proportionality ABC:DEF :: prisms:prisms by using VI.22 (similar rectilinear figures on proportional lines are proportional) and V.16 (alternando) to transfer the similarity relation between sub-triangles into a proportion between the original bases. The AI takes a fundamentally different route: it uses VI.19 (similar triangles have areas in duplicate ratio of sides) to compute that each prism base is exactly one-fourth of the original triangle's area, then applies V.15 (parts have same ratio as same multiples) to conclude that the ratio of prism bases equals the ratio of original bases. These are different key intermediate conclusions -- Heath works through similarity-based proportion transfer (6.22 + 5.16), while the AI works through area-fraction computation (6.19 + 5.15). The proof-tree containment test confirms these are independent routes: 5.16 and 6.22 are not sub-steps of any AI-cited proposition used for the same purpose. The AI's path is logically complete and valid, with each step properly cited, yielding a path difference (D).

### 12.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Both proofs follow the same method-of-exhaustion backbone: assume the ratio of pyramids to bases yields a solid W less than the second pyramid, divide using 12.3 repeatedly, apply 10.1 to get small remainders, use 12.4 to establish the ratio of prisms, then derive a contradiction where W must be both greater and less than the sum of prisms. Both also handle the greater-than case by reducing it to the less-than case. The difference lies in which Book 5 proportion tools are used to reach the same intermediate conclusions: Heath uses 5.16 (alternando) and 5.11 (transitivity of ratios) to derive the contradiction, while the AI uses 5.14 (comparison of magnitudes in proportions) and CN1. For the second case, Heath invokes the 12.2 Lemma while the AI uses inversion (D5.13) and symmetry. These are different citation-depth choices for the same logical steps, not different proof paths. The ai_only items are predominantly definitions and common notions (D11.12, D5.13, D5.5, CN1, CN5) indicating over-citation, plus 5.14 as an alternative proportion tool. Q2 Case A applies: same backbone, different citation depth, yielding G.

### 12.6
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decides this classification. Heath's proof builds up the polygonal pyramid ratio incrementally, adding one triangle at a time using componendo (5.18) and ex aequali (5.22) in alternation. The AI proof takes a fundamentally different approach: it establishes individual triangular pyramid ratios via 12.5 relative to a common reference pyramid (FGHN), then aggregates all ratios simultaneously using a summation principle (cited as 5.12, though 5.12's preconditions of equal ratios are not strictly met -- the result the AI claims is nevertheless mathematically correct as a property of ratios with a common consequent). The AI then uses inversion and 5.22 to combine the two aggregated ratios into the final result. Since Heath uses 5.18 (componendo) as a core structural element while the AI never uses componendo and instead relies on direct summation of ratios, these constitute genuinely different logical backbones (Case B in Q2). Under Q3, the AI's different path is logically sound -- the mis-citation of 5.12 is an imprecise reference rather than an invalid inference, as the conclusion drawn is correct -- so the classification is D.

### 12.7
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: join diagonals BD, EC, and CD to divide the prism into three pyramids, then use I.34 twice to show the diagonals of parallelograms ABED and BCFE bisect them into equal triangles, apply XII.5 twice to equate pairs of pyramids with equal bases and the same height, and conclude by transitivity that all three pyramids are equal. The AI's only additional citations are CN1 (used explicitly for transitivity, which Heath invokes implicitly), D11.12, and D11.13 (definitions of pyramid and prism that Heath uses without citation). Since heath_only is empty and all ai_only items are axiom-level over-citations (a common notion and two definitions), the proofs share the same backbone at different citation depths, yielding a Granularity difference.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: complete parallelepipeds on the two similar pyramids, show the parallelepipeds are similar, apply 11.33 for the triplicate ratio of similar parallelepipeds, then use 11.28 and 12.7 to establish that each pyramid is one-sixth of its parallelepiped, and conclude that the pyramids are in triplicate ratio of corresponding sides. The sole heath_only citation, 11.24 (opposite planes of a parallelepiped are equal and parallelogrammic), is replaced in the AI proof by its internal component 1.34 (opposite sides of a parallelogram are equal), which appears inside Heath's own proof of 11.24, satisfying the proof-tree containment test. The ai_only items consist of construction propositions (1.31), lower-level results (1.34, 5.15), and definitions (D11.9, D5.10, D6.1) that the AI cites explicitly where Heath leaves them implicit. All key intermediate conclusions are the same in both proofs, making this a citation-depth difference rather than a path difference.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: complete triangular bases to parallelograms, construct parallelepipeds, establish the 6x pyramid-to-parallelepiped relationship, apply XI.34 for reciprocal proportionality of parallelepipeds, then convert back to triangular bases using I.34. The AI's additional citations (11.28, 12.7) explicitly derive the 1/6 relationship that Heath treats as established, while CN1, CN2, CN3 are over-citations of common notions. The AI uses 5.15 for a ratio step where Heath uses V.11 (5.11), but both achieve the same logical transition at the same position in the argument. The heath_only item 5.11 (transitivity of ratios) corresponds to a step the AI handles with CN1 at the same logical juncture. All differences are citation-depth rather than backbone differences.

### 12.10
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 decides the classification. Both proofs use double reductio ad absurdum with the method of exhaustion, and Case 1 (cylinder > 3*cone) follows essentially the same backbone in both proofs: inscribe polygons, exhaust segments via 10.1, relate prism to pyramid via 12.7, derive contradiction from pyramid being inscribed in cone. However, Case 2 (cylinder < 3*cone) reveals a genuine path difference. Heath inscribes polygons in the circle and sets up pyramids, deriving a contradiction when the prism on the inscribed polygon exceeds the cylinder despite being inscribed in it. The AI instead circumscribes polygons about the circle (citing 3.16 and 1.12 for tangent constructions), deriving a contradiction when the pyramid on the circumscribed polygon is less than the cone despite the cone being inscribed in it. These are different intermediate constructions yielding different key intermediate conclusions, constituting Case B in Q2. Q3 confirms the AI's circumscribed-polygon approach is logically valid, with a sound chain from premises to conclusion.

### 12.11
**Category**: Path difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs use the same overall strategy of double reductio ad absurdum combined with the method of exhaustion (X.1) and proportionality of inscribed polygons to circles (XII.1, XII.2). However, the key intermediate conclusions differ in two substantive ways. First, Heath works with pyramids on inscribed polygons and cites XII.6 (pyramids of same height with polygonal bases are as their bases) to establish the ratio of the solid figures, while the AI works with prisms on inscribed polygons and re-derives an analogous result for prisms using XII.7 (triangular prism equals three pyramids), XII.5 (pyramids with triangular bases are as their bases), and V.24 (summing proportions). Second, Heath reaches the contradiction via V.16 (alternation of proportions), while the AI uses V.14 (if A:B=C:D and A<C then B<D). Additionally, Heath proves the result for cones first and extends to cylinders via XII.10, whereas the AI proves for cylinders first and extends to cones. These constitute genuinely different intermediate conclusions and logical paths, not merely different citation depth, so the classification is D. The AI's path was verified as logically valid in Q3.

### 12.12
**Category**: Path difference
**Jaccard**: 0.158
**Analysis**: Q2 determines the classification. Heath's proof uses a double reductio (exhaustion) approach: inscribing polygons in circles, building pyramids approximating the cones, proving individual pyramids are similar via triangle similarity (VI.5, VI.6, V.16, V.22), applying XII.8 for the triplicate ratio of similar pyramids, summing via V.12, and completing the exhaustion argument via X.1. The AI takes a fundamentally different direct ratio approach: constructing a continued proportion via 6.11 to define the triplicate ratio (D5.10), introducing an intermediate cone/cylinder C of mixed dimensions, showing A:C via 12.11 and 12.2 (same height, different bases), proving C:B by establishing from D5.5 that cylinders on the same base are proportional to their heights (with 12.10 reducing cones to cylinders), and chaining via ex aequali (5.22). The key intermediate conclusions are entirely different -- Heath's backbone rests on pyramid similarity and exhaustion, while the AI's rests on direct ratio composition through an auxiliary solid. Both paths are logically complete, so this is a valid path difference (D).

### 12.13
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the identical Eudoxean proportion backbone: they cut the cylinder by a parallel plane, take arbitrary equimultiples of the two sub-axes, construct corresponding equimultiple cylinders using XII.11 (since bases are equal, cylinders on equal axes are equal), verify the equimultiple criterion (greater/equal/less holds simultaneously for axes and cylinders), and conclude by V. Def. 5. The ai_only set consists entirely of definitions (D11.21, D11.23), common notions (CN2, CN5), and a geometric construction proposition (11.16) that the AI cites explicitly to justify that the cross-section is a circle equal to the bases, while Heath treats this as obvious from the setup. heath_only is empty. Since the key intermediate conclusions are the same and the citation differences reflect only the depth of explicit justification, this is a granularity difference.

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: construct or identify a cylinder equal to one of the given cylinders (using equal bases and same height via XII.11), apply XII.13 to establish the ratio between cylinders and their axes, substitute the equal cylinder to obtain the desired proportion, and then extend the result to cones via XII.10. The AI proof adds explicit citations for steps Heath performs implicitly: 5.7 for the substitution of equal magnitudes, 5.15 for transferring the cylinder ratio to cones (as one-third submultiples), CN1 and D5.5 for establishing cylinder equality, and D11.21 for the definition of cylinder. Since heath_only is empty and all ai_only items are definitions, common notions, or ratio-manipulation propositions that support the same intermediate conclusions Heath reaches without citation, this is a citation-depth difference rather than a path difference.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish a biconditional by (1) constructing a third cone/cylinder sharing one dimension with each given solid, (2) using the same-height ratio (12.11) and a same-base ratio result to relate the constructed solid to each original, (3) combining via 5.7 and 5.11. The sole citation difference is that Heath uses 12.13 (cylinder cut by parallel plane gives axis ratio) to establish the height-ratio step, while the AI uses 12.14 (cones/cylinders on equal bases are as their heights). The proof-tree containment test confirms that 12.13 appears inside Heath's own proof of 12.14, so the AI is citing 12.14 as a packaged unit while Heath re-derives its content inline via 12.13. This is a citation-depth difference, not a path difference. The AI's general argument also validly covers both of Heath's sub-cases (heights equal and heights unequal) through a single construction that works regardless.

### 12.16
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Classification was decided at Q2/Q3 (different backbone, valid path). Heath's proof establishes the non-touching condition via a parallelism argument: AC is drawn tangent to the inner circle, then repeated arc bisection yields a chord LN parallel to AC, so LN also does not touch the inner circle. The AI proof instead takes a direct perpendicular-distance approach: it inscribes a square, then bisects arcs repeatedly (using 10.1 for convergence) until the perpendicular distance from the centre to each chord exceeds the inner circle's radius, citing 3.16 and 3.18 to conclude non-touching. The key intermediate conclusions differ fundamentally: Heath argues through tangent-parallel geometry and triangle congruence (1.4), while the AI argues through perpendicular distances and chord-arc relationships (3.14, 3.15, 3.29). Both paths are logically complete, so this is a genuine path difference.

### 12.17
**Category**: Path difference
**Jaccard**: 0.130
**Analysis**: Q2 determines this classification. The AI and Heath proofs have fundamentally different backbones. Heath constructs the polyhedron by drawing a perpendicular OA from center to sphere surface, creating planes through OA, inscribing arcs in the resulting semicircles, then establishing an intricate chain of parallel lines (WV parallel to KB via VI.2, PV parallel to SW via XI.6), showing KBPS is a quadrilateral in a circle (XI.7, XI.9, I.33), and using a detailed algebraic argument with squares and rectangles (III.31, VI.8) to prove AX > AZ > AG. The AI takes a rotational approach, explicitly citing 12.16 to inscribe the polygon, then rotating the construction around an axis by passing planes through AC, constructing the polyhedron from connected vertices in adjacent planes, and arguing that the perpendicular from center to each face exceeds the lesser sphere's radius using a Pythagorean framework (OT^2 + r^2 = R^2). E was considered for the terse assertion of OT >= OS in Step 16, but the audit record yields missing_is = expansion (the claim is stated with supporting structure, just not fully expanded), so the lenience rule applies and the verdict is NOT-E. The very low Jaccard (0.13) with 7 AI-only and 13 Heath-only citations confirms the substantial path divergence.
**Audit Record**: CANDIDATE E — 12.17
  violated_claim : OT >= OS (perpendicular from O to face plane >= perpendicular from O to polygon side)
  failure_mode   : unsupported_assertion
  missing_is     : expansion  # The AI states the claim and sketches why, but doesn't fully expand the argument
  evidence       : Step 16: "OT >= OS > OE" - asserted without detailed derivation; the AI provides OT^2 + r^2 = R^2 framework but does not rigorously derive the inequality
  why_not_terse  : Cannot complete convincingly - the AI provides structural reasoning (Pythagorean framework, angle subtension argument) that informally supports the claim, making this an expansion gap rather than a logical gap

### 12.18
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same exhaustion backbone: assume the triplicate ratio holds to something less than the second sphere, inscribe a polyhedral solid in the second sphere not touching an inner sphere (12.17), inscribe a similar polyhedron in the first sphere, establish that similar polyhedra are in the triplicate ratio of diameters, use alternation (5.16) to derive a contradiction, then handle the greater case by inversion reducing to the less case. The ai_only citations (12.8, 5.11, 5.12, 5.14, CN5, D11.14, D11.17, D5.10) represent over-citation of proportion-theory lemmas, definitions, and common notions that Heath uses implicitly, plus an explicit derivation of the triplicate ratio of similar polyhedra via 12.8 and 5.12 where Heath cites 12.17's corollary as a unit. The heath_only citation (12.2) is a lemma Heath invokes in the greater case that the AI handles by direct parallel argument instead. These are all citation-depth differences on the same logical backbone, not path divergences.


## Book 13

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 4 |
| Path difference (D) | 14 |
| AI proof error (E) | 0 |

**Total**: 18 propositions

### 13.1
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same starting point (rect(AB,BC) = sq(AC) from the golden ratio definition and 6.17) and the same final conclusion (sq(CD) = 5*sq(AD)), but they reach it through fundamentally different intermediate backbones. Heath constructs geometric square figures and uses 6.1 (proportionality of parallelograms under the same height) to relate parts of the diagram, working through gnomons to show that the whole square AE equals gnomon MNO, then that gnomon MNO is quadruple of AP, so DF is five times AP. The AI instead takes a purely algebraic route using Book 2 identities (2.1, 2.2, 2.4) to decompose and recombine rectangular areas, establishing sq(AB) = rect(AB,AC) + sq(AC), then sq(AC+AD) = sq(AB) + sq(AD), and finally substituting sq(AB) = 4*sq(AD) to obtain 5*sq(AD). The heath_only citation 6.1 is not subsumed by any AI citation but rather reflects Heath's geometric method, while the ai_only citations (1.10, 2.1, 2.2, 2.4, CN2) reflect the AI's algebraic method. Since the key intermediate conclusions differ but the AI's path is logically complete and valid (Q3 confirmed), the classification is D.

### 13.2
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof works through geometric area manipulation on constructed squares, establishing that the gnomon MNO equals CG, then using VI.1 to relate segment lengths, ultimately showing rect(CD,DB) = sq(CB) to conclude the extreme and mean ratio property. The AI takes a fundamentally different path: it constructs CD = 2*AC, cuts CD in extreme and mean ratio via 6.30, then applies 13.1 to derive that sq(CE + AC) = 5*sq(AC), equates this with the hypothesis sq(AB) = 5*sq(AC), and concludes CE = CB. The two proofs share no key intermediate conclusions -- Heath reasons through area equalities on constructed squares while the AI leverages 13.1 as a tool to algebraically identify the greater segment. The AI's different path is logically complete and valid (Q3 confirmed), yielding a path difference classification.

### 13.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same starting facts (AB*BC = AC^2 from the extreme and mean ratio definition, and AC^2 = 4*DC^2 from bisection), but they reach the conclusion DB^2 = 5*DC^2 through fundamentally different intermediate reasoning. Heath's proof uses geometric area manipulation on a constructed figure, working with squares, rectangles, and gnomons (OPQ, FG, etc.) to show that gnomon OPQ = CE = 4*FG and then gnomon OPQ + FG = 5*FG = square on DB. The AI proof takes an algebraic approach, using Proposition 2.4 to expand DB^2 = DC^2 + CB^2 + 2*DC*CB, then using Proposition 2.3 to show AB*CB = AC*CB + CB^2, and substituting to derive DB^2 = DC^2 + AC^2 = DC^2 + 4*DC^2 = 5*DC^2. The intermediate backbone differs: Heath's gnomon-based area argument has no counterpart in the AI proof, and the AI's algebraic decomposition via Book 2 propositions has no counterpart in Heath's. Heath cites no propositions at all (empty heath_refs), while the AI explicitly cites 1.10, 2.3, 2.4, 6.17, CN1, CN2, and D6.3. Both paths are logically complete, making this a valid path difference (D).

### 13.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) from the extreme and mean ratio definition, establish rect(AB,BC) = sq(AC) via D6.3 and 6.17, then (2) show sq(AB) + sq(BC) = 2*rect(AB,BC) + sq(AC), and (3) substitute to get 3*sq(AC). The key difference is citation depth: Heath re-derives the content of 2.7 inline using gnomon reasoning on the constructed square ADEB (the same geometric argument that constitutes Heath's own proof of 2.7), while the AI cites 2.7 directly as a unit. The proof-tree containment test confirms this: Heath's gnomon argument in 13.4 (AF=FE, AK=CE, gnomon LMN) mirrors the structure of Heath's proof of 2.7 (AG=GE, AF=CE, gnomon KLM). The AI also explicitly cites CN1 and CN2 for substitution and arithmetic steps that Heath performs implicitly. Since heath_only is empty and ai_only contains 2.7 (whose content Heath re-derives inline) plus two common notions, this is a clear granularity difference rather than a path divergence.

### 13.5
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish that the rectangle on the whole and the added segment equals the square on the original line, then derive the golden ratio proportion and the inequality. However, the methods diverge at the backbone level: Heath uses a geometric construction (square AE and figure) to identify equal rectangles and squares within the constructed figure (CE=HC, DH=HE, DK=AE), while the AI uses an algebraic decomposition via II.1 to expand rectangle AD*BD, substitutes BD=AC, and reassembles the terms to reach the same equality. Additionally, Heath uses V.14 (ratio comparison) for the inequality, while the AI uses CN5 (whole greater than part) directly. Since the key intermediate route differs -- geometric figure manipulation vs algebraic rectangle decomposition -- this is a genuine path difference. The AI's algebraic path is logically complete and valid at every step.

### 13.6
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same backbone for the first part (showing AC is an apotome via 13.1, 10.6, 10.9, and 10.73), but diverge fundamentally for the second segment CB. Heath establishes AB*BC = AC^2 using the golden ratio definition (D6.3) and 6.17, then applies 10.97 (square on an apotome applied to a rational line produces a first apotome) to conclude CB is a first apotome. The AI instead constructs a new line DF = 3*DB, establishes that DF^2 : DE^2 = 9:5 (a ratio of numbers but not of square numbers), uses 10.6 and 10.9 to show DF and DE are rational and commensurable in square only, then shows CB = DF - DE and applies 10.73 directly to conclude CB is an apotome. This is a genuinely different logical path with different key intermediate conclusions (no use of 6.17 or 10.97), and the AI's chain is logically sound, so Q3(b) confirms validity, yielding classification D.

### 13.7
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decides the classification. Both proofs correctly handle the two required cases (consecutive and non-consecutive equal angles), but they argue through fundamentally different key intermediate conclusions. In Case 1, Heath introduces diagonals AC, BE, FD and uses I.6 (converse of the isosceles triangle theorem) to establish AF = BF, then derives FC = FE, and applies I.8 (SSS) on triangles FCD and FED to conclude angle FCD = angle FED. The AI never introduces point F and instead uses I.4 to establish AC = BD and BE = BD, making triangle BDE isosceles, then deploys I.32 (angle sum theorem) for explicit angle calculations in terms of alpha = (180 - angle ABC)/2, showing angles D and E both equal 3*alpha, and finally uses further congruence arguments (I.4, I.8) to prove phi = angle ABC. In Case 2, Heath uses I.4 and I.5 directly while the AI reduces to Case 1 after establishing four equal angles via angle arithmetic. The AI proof is logically complete and valid throughout, but the backbones differ: Heath approach is purely synthetic (using I.6 and the auxiliary point F), while the AI approach is computational (using I.32 for angle-sum reasoning). This constitutes a genuine path difference.

### 13.8
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decides the classification. Both proofs reach the same final conclusions (diagonals cut in extreme and mean ratio with greater segments equal to the pentagon side), and share key intermediate conclusions such as HE = AE via I.6, equiangularity of triangles ABH and ABE, and the resulting proportion via VI.4. However, the route to establishing the critical angle equalities diverges fundamentally: Heath circumscribes a circle about the pentagon (IV.14), uses SAS congruence (I.4) to show triangle ABE congruent to ABC, then employs arc reasoning (III.28, VI.33) to show angle EAC = 2 * angle BAC, deducing angle HAE = angle AHE. The AI instead computes all angles directly from the pentagon angle sum via I.32 and isosceles triangle properties (I.5), determining each interior angle as 3/5 of two right angles, then computing sub-angles arithmetically. The heath_only citations (1.4, 3.28, 4.14, 5.14, 6.33) represent this circumscribed-circle method chain and are not contained in any AI citation's proof tree; the AI simply takes an entirely different approach. Since these represent genuinely different methods rather than citation-depth differences, this is Case B (different backbone). Q3 confirms the AI's angle-arithmetic path is logically complete and valid, yielding classification D.

### 13.9
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determined the classification. Heath's proof works by angle chasing: using the arc-angle correspondence (VI.33), isosceles triangle properties (I.5), and the exterior angle theorem (I.32) to show triangles EBD and EBC are equiangular, then applying similar-triangle proportionality (VI.4) to directly establish BD:DC = DC:CB. The AI proof takes an entirely different route: it establishes that the hexagon side equals the radius (4.15), that the decagon side is the greater segment when the radius is cut in extreme and mean ratio (via 4.10 and 2.11), and then applies the additive EMR property (13.5) to conclude that h + d is cut in EMR with h as the greater segment. The key intermediate conclusions are completely different -- Heath uses equiangular triangles and proportional sides, while the AI uses the EMR decomposition of the radius and 13.5's additive property. The Jaccard similarity of 0.1 (only 4.15 shared) reflects this fundamental path divergence. The AI proof is logically complete and valid, establishing a sound chain from premises to conclusion through different mathematical machinery.

### 13.10
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decides this classification. Heath's proof establishes the result through similar triangles: he shows triangle ABF is equiangular with triangle BFN (yielding rect(AB,BN) = sq(BF) via VI.4 and VI.17), then triangle KBA is equiangular with triangle KNA (yielding rect(BA,AN) = sq(AK) via VI.4 and VI.17), and combines these via II.2 to get sq(BA) = sq(BF) + sq(AK). The AI takes a fundamentally different approach: it identifies BN as a decagon side via arc midpoints, applies the Pythagorean theorem (I.47) twice to derive d^2 = 2r(r - OM), then invokes 13.9 (the golden ratio property of hexagon and decagon sides) with 6.17 to obtain r^2 = rd + d^2, and finally uses algebraic manipulation to derive s^2 = r^2 + d^2. The two proofs share only 4.15 and 6.17 out of 20 distinct citations (Jaccard = 0.10), and their key intermediate conclusions are entirely different -- similar triangles and proportionality versus Pythagorean theorem and golden ratio algebra. The AI proof is logically complete under the Q1(b) hardened standard, so this is a valid different path (D).

### 13.11
**Category**: Path difference
**Jaccard**: 0.217
**Analysis**: Q2 determines the classification. Heath's proof works directly with the geometric configuration of the pentagon inscribed in the circle, using triangle similarity (I.32) and the property that diagonals cut in extreme and mean ratio (XIII.8) to establish proportions leading to the identification of MB as a fourth apotome via X.73, X.15, X.12, and V.18/V.19. The AI takes a fundamentally different algebraic approach through the hexagon-decagon decomposition: it uses XIII.10 (sq(pentagon side) = sq(hexagon side) + sq(decagon side)) and XIII.9 (hexagon + decagon side cut in extreme and mean ratio) to express sq(BC) = rect(r, d-s), then algebraically constructs q = d-s as a fourth apotome by setting up auxiliary quantities a = 5N and b = s+N (where N = r/2) and verifying the fourth apotome conditions directly. The key intermediate conclusions differ substantially: Heath establishes the result through geometric segment relationships within the circle figure (triangles ACL and AMF, segments MK, KF, BK), while the AI never uses these geometric constructions, instead building entirely from the radius-hexagon-decagon framework. Both paths are logically complete and valid, representing a genuine path difference (D).

### 13.12
**Category**: Path difference
**Jaccard**: 0.133
**Analysis**: Q2 decided the classification. Heath's proof establishes that BE equals the radius by invoking IV.15 (the hexagon inscription result), then uses III.31 and I.47 to reach the algebraic conclusion sq(AB) = 3*sq(DE). The AI proof takes a fundamentally different geometric path: it uses SSS congruence (I.8) to show the three central triangles are congruent, derives through angle arithmetic (I.13, I.32) that angle BED is one-third of two right angles, then uses isosceles triangle properties (I.5, I.6) to show BD = ED = radius. The AI also uses II.4 to expand sq(AD) = 4*sq(AE) rather than Heath's direct observation that AE = 2*DE. These are genuinely different key intermediate conclusions -- the AI never establishes the hexagon-side-equals-radius fact that is Heath's backbone, instead deriving an equivalent result (BD = radius) through central angle analysis. Since the AI's different path is logically complete and valid, this is classified as D.

### 13.13
**Category**: Granularity difference
**Jaccard**: 0.412
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) cutting the diameter AB so AC = 2CB, (2) constructing a semicircle and perpendicular CD, (3) inscribing an equilateral triangle EFG in a circle of radius CD perpendicular to the diameter, (4) proving all apex-to-base edges are equal via I.4, (5) using XIII.12 to show the base side equals the lateral edges, (6) concluding all six edges are equal giving a regular tetrahedron, (7) showing the tetrahedron is inscribed in the sphere, and (8) deriving the metric relation that the square on the diameter is 1.5 times the square on the side. The AI uses a more streamlined construction placing the apex at endpoint A of the diameter with center C, while Heath constructs a separate center H and erects perpendicular HK via XI.12 (= 11.12) and finds the center via III.1 (= 3.1). This construction-level difference explains the heath_only citations (11.12, 3.1) which the AI avoids by its direct use of the diameter endpoint. The ai_only citations are mostly over-citations of construction axioms and definitions (P1, P3, CN1, D11.12, D11.14, 1.11) plus 1.47 (Pythagorean theorem used directly where Heath uses proportion arguments) and 6.9 (explicit citation for dividing the line). The logical backbone and key geometric conclusions are the same in both proofs.

### 13.14
**Category**: Path difference
**Jaccard**: 0.062
**Analysis**: Q2 decided the classification as D (path difference). Heath constructs the octahedron by setting out a square EFGH in a plane, erecting a perpendicular from its center K using XI.12, and proving sphere inscription via a semicircle argument using I.4 (SAS congruence to show LE=EM) and III.31 (angle in semicircle is right). The AI instead places the center E on the diameter and constructs three mutually perpendicular axes through E using XI.4, making all six vertices equidistant from E by construction, then proves sphere inscription directly from equal radii and derives the diameter-to-side relation through simple algebra (AB=2AE, AB^2=4AE^2, side^2=2AE^2). The heath_only propositions (I.4, XI.12, III.31) are not depth differences but reflect a fundamentally different geometric strategy: Heath uses a semicircle-based argument while the AI uses a coordinate-style perpendicular-axes construction. The AI proof is logically complete and valid under the hardened Q1(b) standard, establishing a sound but genuinely different path to the same conclusion.

### 13.15
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Both proofs follow the same key intermediate conclusions: constructing the cube from square EFGH with side equal to DB, establishing that the face diagonal squared equals twice the side squared (I.47), that the space diagonal squared equals three times the side squared (I.47), that AB squared equals three times BD squared (via the 1:3 ratio of BC to AB and BD as mean proportional), and concluding the space diagonal equals the diameter. The heath_only set is empty, meaning every citation Heath uses also appears in the AI proof. The 20 ai_only citations are predominantly construction justifications (1.11, 1.3, 1.46, 11.12, P1, P3), definitions (D1.17, D1.22, D11.25), common notions (CN1, CN2), and subsidiary propositions (1.33, 1.34, 11.6, 3.31, 6.1, 6.8, 6.10, 6.17) that Heath invokes implicitly. The AI uses 11.38 for the inscribing argument (center-of-symmetry) where Heath uses a rotating semicircle, but this is a minor methodological variation in a sub-argument, not a wholesale backbone difference; the main quantitative backbone is identical. This is Case A: same backbone, different citation depth.

### 13.16
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as Granularity difference. Both proofs share the same backbone: constructing the icosahedron from a base circle EFGHK with inscribed pentagon/decagon, using XIII.10 as the central tool to show all edges equal the pentagon side, proving all 20 triangular faces are equilateral, proving comprehension in the given sphere via a 'five times the square' relationship, and proving the side is minor via XIII.11. The large ai_only set (18 items) consists mostly of over-citations: construction postulates (P1, P3), auxiliary construction propositions (1.11, 11.12, 11.15, 4.11, 4.16), definitions (D1.20, D10.1.3, D11.27), common notions (CN1), and sub-lemma props (3.28, 3.29, 1.4, 1.47). The heath_only items (1.33, 13.3, D5.9) are accounted for by corresponding AI citations at different granularity: the AI uses 11.6 and 1.47 where Heath uses 1.33 for parallelism, 13.1 and 13.2 where Heath uses 13.3 for the sphere-fitting argument, and 13.9 where Heath references D5.9. The key intermediate conclusions are established identically in both proofs, making this a same-backbone, different-depth scenario.

### 13.17
**Category**: Path difference
**Jaccard**: 0.148
**Analysis**: Q2 determined the classification. The AI and Heath proofs both construct a dodecahedron from a cube, inscribe it in a sphere, and prove the side is an apotome, but they reach these conclusions through fundamentally different key intermediate steps. Heath proves the pentagon is equilateral via explicit segment-length computations using 13.4 and 1.47, proves coplanarity as a separate key conclusion using 6.32 and 11.6, and proves equiangularity through 13.5, 1.8, and 13.7. The AI instead appeals to 13.1 for segment relations, uses 13.8 (pentagon diagonal properties) and 1.32 for equiangularity, and does not isolate coplanarity as a separate intermediate conclusion. The heath_only propositions (1.8, 11.1, 11.6, 13.5, 13.7, 6.32) are not subsumed by any single higher-level AI citation; they represent genuinely different argumentative steps in Heath's proof. The AI's substantive ai_only citations (13.1, 13.8, 1.32) represent a different logical route. Under Q3, the AI's path is valid: each major claim cites relevant propositions, and the overall chain from construction to conclusion is logically connected, though terse. The very low Jaccard of 0.148 corroborates the significant path divergence.

### 13.18
**Category**: Path difference
**Jaccard**: 0.227
**Analysis**: Q2 decides this classification as D (path difference). Both proofs reach the same ultimate conclusions (setting out all five Platonic solid sides and comparing them), but they argue through substantively different intermediate machinery. Heath constructs each side geometrically from a single diagram using similar triangles (VI.8, VI.4), duplicate ratios (V.Def.9), and detailed proportional reasoning, then identifies each constructed segment with the relevant solid's side via XIII.13-XIII.17. The AI instead cites XIII.13-XIII.17 directly as summary results and uses algebraic ratio computation. More significantly, for the crucial icosahedron-greater-than-dodecahedron comparison, Heath deploys an elaborate geometric argument using XIII.9 (extreme and mean ratio of hexagon + decagon sides), VI.4, VI.8, V.Def.9, and VI.20 to establish a chain of inequalities (AD > FB, AL > FB, KL > NB, LM > NB, therefore MB > NB). The AI instead cites XIII.8 (about pentagon diagonals and extreme and mean ratio), a genuinely different proposition from a different geometric context. The proof-tree containment test shows that while some heath_only items (13.10, 4.15) appear inside XIII.16's proof, other substantive heath_only items (6.4, 6.20, 13.9) are deployed independently in Heath's XIII.18 proof and do not appear inside any proposition the AI cites, confirming genuine path divergence rather than mere citation-depth difference. Under Q1's hardened standard, the AI's terse Step 11 was considered for E but rejected because it cites relevant propositions (13.8, 13.16, 13.17) and the missing detail is expansion, not support (lenience rule applies).
**Audit Record**: CANDIDATE E — 13.18
  violated_claim : "the side of the icosahedron exceeds the side of the dodecahedron" (Step 11)
  failure_mode   : unsupported_assertion
  missing_is     : expansion (AI cites 13.8, 13.16, 13.17 which are relevant propositions; the missing content is the detailed geometric argument expanding how these citations yield the conclusion)
  evidence       : AI Step 11: "Since the side of the icosahedron relates to the side of the dodecahedron through these constructions, and the side of the dodecahedron is obtained by cutting certain segments in extreme and mean ratio, the side of the icosahedron exceeds the side of the dodecahedron. [13.8, 13.16, 13.17]"
  why_not_terse  : CANNOT COMPLETE — this IS terse-but-supported. The AI invokes relevant propositions (13.8 on extreme and mean ratio in pentagons, 13.16 and 13.17 for the constructions) that bear on the claim. The missing content is an expansion of how these citations combine, not the absence of any supporting citation. Lenience rule applies → NOT-E.
