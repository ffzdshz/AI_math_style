# Euclid Proof Classification Report — RunC

Classification of all 465 AI-generated proofs against Heath's reference proofs, into four categories: **Perfect match (P)**, **Granularity difference (G)**, **Path difference (D)**, and **AI proof error (E)**. P denotes identical citation sets and a complete proof; G denotes the same proof strategy with differences confined to citation granularity (over-citing construction primitives or definitions, inlining or expanding sub-lemmas); D denotes a genuinely different valid route to the same conclusion (typically the AI's algebraic or arithmetic manipulation in place of Heath's geometric proposition chain); E denotes a positively identifiable logical defect in the AI proof.

## Overall Summary

| Category | Count | Share |
|---|---|---|
| P — Perfect match | 24 | 5.2% |
| G — Granularity difference | 303 | 65.2% |
| D — Path difference | 138 | 29.7% |
| E — AI proof error | 0 | 0.0% |
| **Total** | **465** | **100.0%** |

## Per-Book Distribution

| Book | P | G | D | E | n | Mean Jaccard |
|---|---|---|---|---|---|---|
| 1 | 11 | 37 | 0 | 0 | 48 | 0.656 |
| 2 | 0 | 4 | 10 | 0 | 14 | 0.139 |
| 3 | 0 | 25 | 12 | 0 | 37 | 0.255 |
| 4 | 0 | 16 | 0 | 0 | 16 | 0.342 |
| 5 | 4 | 16 | 5 | 0 | 25 | 0.417 |
| 6 | 0 | 25 | 8 | 0 | 33 | 0.386 |
| 7 | 1 | 27 | 11 | 0 | 39 | 0.351 |
| 8 | 4 | 14 | 9 | 0 | 27 | 0.440 |
| 9 | 3 | 17 | 16 | 0 | 36 | 0.317 |
| 10 | 0 | 78 | 37 | 0 | 115 | 0.344 |
| 11 | 1 | 28 | 10 | 0 | 39 | 0.380 |
| 12 | 0 | 9 | 9 | 0 | 18 | 0.302 |
| 13 | 0 | 7 | 11 | 0 | 18 | 0.251 |
| **All** | **24** | **303** | **138** | **0** | **465** | **0.372** |

## Error Detail (E Classifications)

No E-class propositions remain after reprove.

---

## Book 1

| Category | Count |
|---|---|
| Perfect match (P) | 11 |
| Granularity difference (G) | 37 |
| Path difference (D) | 0 |
| AI proof error (E) | 0 |

**Total**: 48 propositions

### 1.1
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided this classification. Both proofs share identical key intermediate conclusions: (1) AC = AB from A being the centre of the circle, (2) BC = BA from B being the centre of the other circle, (3) CA = CB via Common Notion 1, and (4) triangle ABC is equilateral. The only citation difference is that the AI explicitly cites Definition 1.20 (equilateral triangle) when concluding the triangle is equilateral, whereas Heath applies the same concept implicitly without a formal citation. Since the logical backbone is the same and the sole ai_only item is a definition cited for explicitness, this is Case A of Q2: same backbone, different citation depth, yielding a Granularity difference (G).

### 1.2
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: BC = BG (radii of circle CGH), DL = DG (radii of circle GKL), DA = DB (equilateral triangle), AL = BG (by subtracting equals via CN3), and AL = BC (by transitivity via CN1). The constructions are also identical. The only difference is that the AI explicitly cites Definition 1.15 (definition of a circle, justifying that radii are equal) and Definition 1.20 (definition of equilateral triangle, justifying DA = DB), whereas Heath leaves these definitional grounds implicit. Since ai_only contains only definitions and heath_only is empty, this is a pure citation-depth difference with the same logical backbone, satisfying Case A of Q2 for Granularity difference (G).

### 1.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: place AD equal to C at point A (I.2), draw circle DEF with centre A and distance AD (Post.3), conclude AE = AD from the definition of a circle (Def.15), and then conclude AE = C by transitivity (C.N.1). The citation sets are exactly equal (ai_used = heath_refs = {1.2, CN1, D1.15, P3}) with Jaccard similarity 1.0 and empty symmetric difference. Since Q1 found no logical defects, Q2 confirmed the same key intermediate conclusions, and the citation sets match perfectly, the classification is P (Perfect match).

### 1.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the identical superposition method: placing triangle ABC on triangle DEF, showing B coincides with E (AB=DE), AC coincides with DF (angle BAC=angle EDF), C coincides with F (AC=DF), BC must coincide with EF (otherwise two straight lines would enclose a space), and concluding equality of bases, triangles, and remaining angles. The key intermediate conclusions are the same in both proofs in the same logical order. The only difference is that the AI explicitly cites Postulate 1 to justify the impossibility of two distinct straight lines enclosing a space, whereas Heath makes the same argument without a formal postulate citation. This is a citation-depth difference (over-citation by the AI of a postulate), placing the classification squarely in Case A of Q2, yielding G.

### 1.5
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) applying I.4 to triangles AFC and AGB to establish FC=GB and corresponding angle equalities, (2) subtracting equal segments to get BF=CG, (3) applying I.4 again to triangles BFC and CGB to establish the angle equalities under the base, and (4) subtracting angles to conclude the base angles are equal. The only citation difference is that the AI explicitly cites CN3 (equals subtracted from equals) for the subtraction steps in Steps 5 and 7, while Heath performs these same subtractions without an explicit Common Notion citation. Since the backbone is identical and the sole ai_only citation (CN3) is a Common Notion making explicit what Heath leaves implicit, this is a citation-depth difference yielding G.

### 1.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use identical proof-by-contradiction structure: assume AB is not equal to AC with AB greater, cut DB equal to AC from AB, join DC, establish triangle DBC congruent to triangle ACB by SAS, derive a contradiction (part equals whole), and conclude AB equals AC. The key intermediate conclusions are the same in both proofs. The only difference is citation depth: the AI explicitly cites 1.3 (cutting off a segment), 1.4 (SAS congruence), CN5 (part cannot equal whole), and P1 (joining a line), while Heath leaves all of these implicit with an empty reference set. Since heath_only is empty and all ai_only items are construction-level or axiomatic citations that make explicit what Heath uses implicitly, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 1.7
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: proof by contradiction assuming two pairs of equal lines from the endpoints of AB meeting at distinct points C and D, joining CD, applying I.5 to both isosceles triangles ACD and BCD, using angle containment to derive contradictory angle inequalities. The AI proof explicitly cites CN5 (for the angle containment/inequality reasoning) and P1 (for joining CD), while Heath uses these same facts implicitly without citing them. The ai_only set contains only CN5 and P1 (a common notion and a postulate), and heath_only is empty, confirming that the difference is purely one of citation depth rather than logical path. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 1.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical superposition argument: place triangle ABC onto DEF with B on E and BC along EF, deduce C coincides with F (since BC=EF), then argue by contradiction using I.7 that sides BA and AC must coincide with ED and DF, and therefore angle BAC equals angle EDF. The key intermediate conclusions are the same in both proofs. The only citation difference is that the AI explicitly cites CN4 (things which coincide are equal) to justify the final equality step, while Heath leaves this common notion implicit. Since CN4 is an axiom-level citation representing over-citation rather than a different logical path, this is a citation-depth difference, yielding G.

### 1.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: construct AE equal to AD on AC using I.3, construct equilateral triangle DEF on DE, then apply SSS congruence (I.8) with AD=AE, DF=EF, and AF common to conclude angle DAF equals angle EAF, thereby bisecting angle BAC. The AI proof differs only in citation depth, explicitly citing Proposition 1.1 for the equilateral triangle construction, Postulate 1 for joining lines, and Definition 1.20 for the definition of equilateral triangle, all of which Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are construction propositions, postulates, and definitions (classic over-citation), this is a clear Case A granularity difference.

### 1.10
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: construct an equilateral triangle on AB (1.1), bisect angle ACB with line CD (1.9), then apply SAS congruence (1.4) to conclude AD = BD. The only citation difference is that the AI explicitly cites D1.20 (definition of equilateral triangle) to justify AC = CB, while Heath states this fact without citing the definition. Since heath_only is empty and ai_only contains only a definition that makes explicit what Heath leaves implicit, the proofs have the same backbone at different citation depths, yielding a Granularity difference.

### 1.11
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: take point D on AC, cut CE equal to CD (I.3), construct equilateral triangle DEF on DE (I.1), join FC, prove triangles DCF and ECF congruent by SSS (I.8) so angle DCF equals angle ECF, then conclude each is a right angle by Definition 10. The only citation difference is that the AI explicitly cites Postulate 1 for joining FC, which Heath leaves implicit. Since ai_only contains only P1 (a construction postulate) and heath_only is empty, this is a pure citation-depth difference with no backbone divergence, satisfying Case A of Q2 for Granularity difference.

### 1.12
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct a circle with center C and radius CD, find intersection points E and G on line AB, bisect EG at H, establish three pairs of equal sides (CG=CE, GH=HE, CH=CH), apply SSS congruence (I.8) to conclude equal adjacent angles, then invoke the definition of right angles (D1.10) to conclude perpendicularity. The sole difference is that the AI explicitly cites D1.15 (definition of a circle) to justify CG = CE, while Heath leaves this implicit from the construction. Since D1.15 is a definition and represents an over-citation rather than a substantive path divergence, this is a citation-depth difference falling under Case A of Q2, yielding Granularity difference (G).

### 1.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 1.13 follow identical logical structures with identical citation sets (Jaccard = 1.0). Both proofs handle the same two cases: (1) when angle CBA equals angle ABD, each is a right angle by Definition 10, and (2) when they are not equal, a perpendicular BE is constructed via I.11, and angle addition with CN2 applied twice followed by transitivity via CN1 establishes that angles DBA and ABC together equal two right angles. Since the key intermediate conclusions match exactly and ai_used equals heath_refs ({1.11, CN1, CN2, D1.10}), the perfect match check yields category P.

### 1.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: assume BD is not in a straight line with CB, let BE be in a straight line with CB, apply I.13 to get ABC+ABE = two right angles, compare with the hypothesis ABC+ABD = two right angles, subtract ABC to get ABE=ABD, then derive a contradiction since one angle is a proper part of the other. The citation differences are entirely at the axiom/postulate level: the AI adds P2 (for producing the line) and CN5 (whole greater than part) while Heath adds P4 (all right angles equal). These are not substantive backbone differences but rather differences in which foundational axioms are explicitly cited versus left implicit. Since the key intermediate conclusions are the same and only citation depth varies, this is a granularity difference (G).

### 1.15
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they apply I.13 to establish that supplementary angle pairs each sum to two right angles, equate the sums via CN1, and subtract the common angle via CN3 to conclude equality of vertical angles. The only citation difference is that Heath cites P4 (all right angles are equal) alongside CN1 when equating the two sums, while the AI omits P4 and relies solely on CN1 for the transitivity step. This is a citation depth difference at the same logical position, not a backbone divergence. Since the key intermediate conclusions are identical but the citation sets differ (heath_only contains P4), this is a granularity difference rather than a perfect match.

### 1.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI and Heath proofs of Proposition 1.16 share identical citation sets (1.10, 1.15, 1.3, 1.4, CN5, P1, P2) with Jaccard similarity 1.0. Both proofs follow the same logical backbone: bisect AC at E, construct F on the extension of BE with EF equal to BE, apply SAS congruence (I.4) to triangles AEB and CEF to establish angle BAE equals angle ECF, then use CN5 to conclude the exterior angle ACD is greater than angle BAC. The second case (ACD greater than angle ABC) is handled by Heath with a 'similarly' argument and by the AI with an explicit parallel construction bisecting BC. Since the key intermediate conclusions are the same and the citation sets match exactly, the classification is Perfect match (P).

### 1.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 1.17 use the identical citation set {1.13, 1.16, P2} and argue through the same key intermediate conclusions: producing a side to create an exterior angle, applying I.16 to show the exterior angle exceeds the remote interior angle, applying I.13 to show the exterior angle plus the adjacent interior angle equal two right angles, and concluding that the two interior angles sum to less than two right angles. The only difference is that the AI explicitly works out all three pairs of angles while Heath proves one pair and says 'similarly' for the other two, but this is not a structural or citation-depth difference -- it is the same argument elaborated more fully. Since the citation sets match exactly and the backbone is the same, the classification is P (Perfect match).

### 1.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct AD equal to AB on AC using I.3, join BD, establish that angle ADB equals angle ABD (isosceles triangle), apply the exterior angle theorem I.16 to show angle ADB is greater than angle ACB, and conclude that angle ABC is greater than angle ACB since it contains angle ABD. The AI's three extra citations (1.5, CN5, P1) are all explicit references to results that Heath uses implicitly: Heath says 'let BD be joined' without citing P1, invokes the isosceles base angle equality without citing I.5, and uses the whole-greater-than-part principle via the phrase 'much greater' without citing CN5. Since heath_only is empty and all ai_only items are over-citations of implicitly used facts, this is Case A of Q2: same backbone with different citation depth.

### 1.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof are structurally identical proof-by-elimination arguments. Both establish the same two key intermediate conclusions in the same order: (1) AC is not equal to AB, eliminated via I.5 (isosceles triangle base angles equal, yielding contradiction), and (2) AC is not less than AB, eliminated via I.18 (greater side subtends greater angle, yielding contradiction). The citation sets are identical at {1.5, 1.18} with Jaccard similarity 1.0, and the logical backbones match exactly, satisfying the perfect match check.

### 1.20
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: extend BA to D with DA = AC, use I.5 to show the base angles of isosceles triangle ACD are equal, apply CN5 to conclude angle BCD > angle ADC, invoke I.19 to get DB > BC, and substitute DA = AC to reach BA + AC > BC. The only citation difference is that the AI explicitly cites the construction steps (1.3 for cutting off equal segments, P1 for joining points, P2 for extending a line) that Heath performs without explicit citation. Since heath_only is empty and the ai_only items are all construction propositions and postulates whose underlying operations appear at the same logical positions in both proofs, this is a citation-depth difference under Case A of Q2, yielding G.

### 1.21
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: extend BD to meet AC at E, apply I.20 twice to establish BA + AC > BE + EC > BD + DC for the length inequality, and apply I.16 twice to establish angle BDC > angle CED > angle BAC for the angle inequality. The key intermediate conclusions are the same in both proofs. The only difference is citation depth: the AI explicitly cites CN2 (for adding equal magnitudes to both sides of an inequality), P1, and P2 (for extending BD to meet AC), whereas Heath invokes these implicitly. Since ai_only contains only postulates and common notions and heath_only is empty, this is a clear case of over-citation by the AI with no backbone divergence, yielding Granularity difference (G).

### 1.22
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share identical key intermediate conclusions: setting out line DE with segments DF=A, FG=B, GH=C via I.3; describing two circles centered at F and G; establishing that the circles intersect (justified by the triangle inequality condition, citing I.20); joining KF and KG at intersection point K; then showing FK=FD=A (radii), GK=GH=C (radii), and FG=B by construction, concluding that triangle KFG has sides equal to A, B, C. The AI proof cites the same substantive propositions as Heath (1.3 and 1.20) and adds only foundational references: CN1 (common notion for transitivity of equality), D1.15 (definition of circle for radii equality), and postulates P1 (joining lines), P2 (extending lines), P3 (describing circles). These are all axioms, definitions, and postulates that Heath uses implicitly. The heath_only set is empty, confirming no substantive propositions are missing from the AI proof. This is a clear Case A in Q2: same logical backbone with the AI providing finer citation depth for foundational steps.

### 1.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take arbitrary points D and E on the rays of the given angle, join DE, construct triangle AFG with sides equal to CD, CE, and DE, then apply I.8 (SSS) to conclude the constructed angle equals the given angle. The AI proof cites three additional references beyond Heath's sole citation of I.8: P1 (for joining DE), 1.22 (for constructing the triangle from three given segments), and 1.20 (for verifying the triangle inequality prerequisite of 1.22). All three ai_only items are construction-level or foundational citations that Heath uses implicitly without explicit reference. Since heath_only is empty and all ai_only items represent over-citation of steps present in both proofs, this is Case A of Q2: same backbone with different citation depth, yielding a Granularity difference (G).

### 1.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct angle EDG equal to BAC, make DG equal to AC/DF, join EG and FG, then establish BC = EG via I.4, show triangle DFG is isosceles so angle DGF = angle DFG via I.5, derive angle EFG > angle EGF through angle inequalities, conclude EG > EF via I.19, and substitute BC = EG to get BC > EF. The AI proof is more explicit in its angle inequality chain (Steps 5-8) and cites construction-level and axiomatic references that Heath leaves implicit: I.3 for cutting a line equal to another, P1 for joining lines, CN1 for transitivity of equality, and CN5 for the whole-greater-than-part principle. Since heath_only is empty and all ai_only items (1.3, CN1, CN5, P1) are construction propositions, postulates, or common notions representing over-citation rather than a different logical path, this is a granularity difference (G).

### 1.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical structures: both use proof by elimination via trichotomy, first showing angle BAC cannot equal angle EDF (contradiction via I.4, since equal angles with equal sides would give equal bases), then showing angle BAC cannot be less than angle EDF (contradiction via I.24, since the lesser angle with equal sides would give a lesser base), and concluding angle BAC must be greater than angle EDF. The citation sets are exactly equal (both use 1.4 and 1.24 only), the key intermediate conclusions are the same, and the argumentative structure matches perfectly, satisfying the perfect match check.

### 1.26
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same two-case structure: Case 1 (ASA) uses reductio by assuming AB unequal to DE, constructing BG = DE, applying I.4 for congruence of triangles GBC and DEF, and deriving a contradiction from angle GCB equaling angle BCA; Case 2 (AAS) uses a similar reductio with I.4 and I.16 to derive an exterior-angle contradiction. The key intermediate conclusions and logical backbone are identical in both proofs. The AI's extra citations (1.3 for cutting segments, P1 for joining lines, CN5 for the part-whole axiom) correspond to construction and axiomatic steps that Heath performs implicitly without explicit citation. Heath_only is empty, confirming that every substantive step Heath cites is also cited by the AI. The ai_only set consists entirely of construction propositions, postulates, and common notions, which are hallmarks of over-citation at a finer granularity rather than a genuinely different proof path.

### 1.27
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 1.27 follow identical logical backbones: both proceed by contradiction, assuming AB and CD are not parallel, then forming a triangle at the meeting point G, applying I.16 (exterior angle theorem) to derive that the alternate angle AEF is greater than angle EFG (which equals EFD), contradicting the hypothesis of equal alternate angles. Both proofs handle the symmetric case (meeting on the other side) and conclude via D1.23 (definition of parallel lines). The citation sets are exactly equal (1.16 and D1.23), with empty ai_only and heath_only sets and Jaccard similarity of 1.0. Since the key intermediate conclusions and citations match perfectly, this is classified as P (Perfect match).

### 1.28
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs address the same two cases and argue through identical key intermediate conclusions: in Case 1, EGB = AGH (by I.15), then AGH = GHD, yielding parallelism by I.27; in Case 2, AGH + BGH = two right angles (by I.13), combined with BGH + GHD = two right angles, subtracting BGH to get AGH = GHD, then parallelism by I.27. The only difference is that the AI explicitly cites CN1 (transitivity of equality) and CN3 (subtraction of equals) for steps that Heath performs without citing the underlying common notions. Since heath_only is empty and ai_only contains only common notions, this is a clear case of the AI providing greater citation depth for the same logical backbone, which is Case A under Q2 — granularity difference.

### 1.29
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: a reductio argument establishing alternate angles equality (using I.13 and Post.5), then deriving the exterior angle equality via vertical angles (I.15, CN1), and finally the supplementary interior angles result (I.13, CN2). The only citation difference is that the AI explicitly cites D1.23 (definition of parallel lines) in Step 7 where Heath implicitly invokes the same fact by stating the lines 'do not meet, because they are by hypothesis parallel.' Since heath_only is empty and ai_only contains only a definition, this is a pure citation-depth difference with the same key intermediate conclusions, satisfying Case A of Q2.

### 1.30
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: draw a transversal across all three parallel lines, apply I.29 twice to establish two angle equalities (one from AB parallel to EF, one from EF parallel to CD), then use CN1 transitivity to conclude the alternate angles formed by the transversal on AB and CD are equal, therefore AB is parallel to CD. The only difference is that the AI explicitly cites 1.27 (equal alternate angles imply parallel lines) in the final step, while Heath states the conclusion without an explicit citation, relying implicitly on the same result. Since heath_only is empty and ai_only contains only 1.27, which is the proposition Heath uses implicitly, this is a citation-depth difference with identical key intermediate conclusions, yielding category G.

### 1.31
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: taking point D on BC, joining AD, constructing angle DAE equal to angle ADC via I.23, producing line EA to F, and concluding EF is parallel to BC by I.27 (alternate angles). The AI proof cites P1 (to join AD) and P2 (to produce EA to F), which are basic construction postulates that Heath uses implicitly without citation. The ai_only set contains only postulates (P1, P2) and heath_only is empty, confirming this is a citation-depth difference where the AI over-cites construction axioms. The logical backbone is the same in both proofs, making this a granularity difference.

### 1.32
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: constructing CE parallel to AB via 1.31, establishing BAC = ACE and ECD = ABC via two applications of 1.29, combining these to show the exterior angle ACD equals the two interior and opposite angles, then adding ACB to both sides and using 1.13 to conclude the three interior angles equal two right angles. The AI proof explicitly cites CN1 and CN2 for the addition and substitution steps that Heath performs implicitly without citing axioms. Since the key intermediate conclusions are the same and the only difference is the AI's explicit citation of Common Notions that Heath uses tacitly, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 1.33
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: The AI proof and Heath's proof share identical key intermediate conclusions: (1) alternate angles ABC=BCD via I.29, (2) triangle congruence ABC=DCB via SAS (I.4) yielding AC=BD and equal alternate angles ACB=CBD, and (3) AC parallel to BD via I.27. The only citation difference is that the AI explicitly cites Postulate 1 for joining line BC, while Heath performs the same construction without an explicit postulate citation. Since heath_only is empty and ai_only contains only P1 (a construction postulate), this is a pure citation-depth difference with the AI over-citing a construction step. Q2 Case A holds, yielding G.

### 1.34
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing alternate angles via I.29 (twice), proving triangle congruence via I.26 (ASA), deriving equal opposite sides and angles, combining angles via CN2 for the remaining pair of opposite angles, and concluding the diameter bisects the area from triangle equality. The only citation differences are that the AI over-cites P1 for drawing the diagonal (a construction postulate Heath uses implicitly) and that Heath re-derives triangle equality for the bisection part using I.4 (SAS), while the AI simply re-uses the triangle equality already established via I.26. Since both proofs reach every key intermediate conclusion through the same logical steps and the citation differences reflect depth of citation rather than different reasoning paths, this is a granularity difference (G).

### 1.35
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of 1.35 and Heath's proof share identical citation sets (1.29, 1.34, 1.4, CN1, CN2, CN3) with Jaccard similarity 1.0. Both proofs establish the same key intermediate conclusions: AD = EF via I.34 and CN1, AE = DF via CN2, AB = DC via I.34, angle EAB = angle FDC via I.29, and triangle EAB = triangle FDC via I.4. The final area argument uses CN3 for subtraction and CN2 for addition in both proofs. The AI proof explicitly handles two sub-cases for the relative positions of points on line AF, while Heath presents one specific configuration with intersection point G, but this is a presentational difference rather than a backbone divergence. Since the citation sets are exactly equal and the key intermediate conclusions match, the classification is P (Perfect match).

### 1.36
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: both construct parallelogram EBCH by joining BE and CH, establish BC = EH via transitivity (CN1), use I.33 to show EBCH is a parallelogram, apply I.35 twice to show ABCD = EBCH and EFGH = EBCH, and conclude ABCD = EFGH by CN1. The citation sets are exactly equal (1.33, 1.34, 1.35, CN1) with Jaccard similarity 1.0, and since both proofs argue through the same key intermediate conclusions with the same citations, this is a perfect match.

### 1.37
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing parallelograms EBCA and DBCF, proving their equality via I.35, showing each triangle is half its respective parallelogram via I.34, and concluding the triangles are equal. The AI's ai_only citations (CN2, CN3, P2) are all foundational axioms and postulates that Heath leaves implicit: P2 for producing line AD, and CN2/CN3 for the principle that halves of equal things are equal. Heath invokes this last principle in brackets without formal citation. Since the logical backbone is the same and the citation differences are purely a matter of explicit vs. implicit foundational references, this is a granularity difference (G).

### 1.38
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: both construct parallelograms on the equal bases (using 1.31), show those parallelograms are equal by 1.36, show each triangle is half its respective parallelogram by 1.34, and conclude by the principle that halves of equal things are equal. The citation sets are identical (1.31, 1.34, 1.36) with Jaccard similarity 1.0, and the key intermediate conclusions match exactly. The only superficial difference is vertex labeling (Heath uses DEFH while the AI uses DEKF for the second parallelogram), which is immaterial. Since both the logical backbone and the citation sets match perfectly, this is classified as P (Perfect match).

### 1.39
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs use identical proof-by-contradiction backbones: assume AD is not parallel to BC, draw AE parallel to BC via I.31, join EC, apply I.37 to show triangle ABC equals triangle EBC, then use CN1 to derive the contradiction that DBC equals EBC when one is greater than the other. The AI proof explicitly cites P1 for joining EC and CN5 for the whole-is-greater-than-the-part principle, whereas Heath performs these same steps implicitly without formal citation. Since ai_only contains only P1 (a postulate) and CN5 (a common notion), and heath_only is empty, the proofs share the same key intermediate conclusions with the AI simply citing at a finer granularity level. This is Case A of Q2: same backbone, different citation depth.

### 1.40
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy: join AD, assume it is not parallel to the base line, draw a parallel through A via 1.31, form a new triangle equal to ABC via 1.38, derive a contradiction using CN1 when comparing the new triangle to the given equal triangle. The key intermediate conclusions are identical in both proofs. The AI adds CN5 (whole is greater than the part) to explicitly justify the contradiction that Heath leaves as 'the greater to the less: which is impossible,' and cites P1 for joining points where Heath does so implicitly. Both ai_only items are axiom-level citations (a Common Notion and a Postulate), representing over-citation rather than a different proof path. Since the backbones match and the citation differences are purely depth-of-citation differences, this is a Granularity difference (G).

### 1.41
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same two key intermediate conclusions: (1) the diagonal AC bisects parallelogram ABCD, making it double triangle ABC (by 1.34), and (2) triangle ABC equals triangle EBC because they share base BC and lie in the same parallels (by 1.37). These are then combined to conclude ABCD is double EBC. The AI proof presents these steps in reversed order compared to Heath but the logical backbone is identical. The ai_only citations (CN1 and P1) are a common notion and a postulate that Heath uses implicitly without explicit citation: Heath says 'let AC be joined' without citing P1, and writes 'so that the parallelogram ABCD is also double of the triangle EBC' without citing CN1. Since heath_only is empty and the ai_only items are purely axiomatic over-citations, this is a clear Case A same-backbone, different-depth granularity difference.

### 1.42
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs construct parallelogram FECG equal to triangle ABC using identical key intermediate conclusions: (1) FECG is a parallelogram by construction, (2) triangle ABE equals triangle AEC by I.38, (3) triangle ABC is double of triangle AEC, (4) parallelogram FECG is double of triangle AEC by I.41, and (5) therefore FECG equals triangle ABC. The logical backbones are the same. The AI's extra citations (1.10 for bisecting BC, P1 for joining AE, CN1 and CN2 for the common notions justifying the doubling and equality conclusions) are all construction-level or axiom-level over-citations that make explicit what Heath leaves implicit. Heath cites no propositions that the AI omits (heath_only is empty). This is Case A of Q2: same backbone, different citation depth, yielding classification G.

### 1.43
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 1.43 follow identical logical backbones and cite exactly the same propositions. Both proofs establish the same five key intermediate conclusions in the same order: (1) triangle ABC equals triangle ACD by 1.34, (2) triangle AEK equals triangle AHK by 1.34, (3) triangle KFC equals triangle KGC by 1.34, (4) the sum AEK + KGC equals AHK + KFC by CN2, and (5) complement BK equals complement KD by CN3. The citation sets are identical (ai_used = heath_refs = {1.34, CN2, CN3}), with Jaccard similarity of 1.0, empty ai_only and empty heath_only. Since Q1 found no logical errors, Q2 confirmed the same backbone, and the citation sets match exactly, this is a perfect match (P).

### 1.44
**Category**: Granularity difference
**Jaccard**: 0.700
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing parallelogram BEFG equal to triangle C with the required angle (I.42), showing lines HB and FE meet at K via angle arguments (I.29, Post. 5), establishing HLKF as a parallelogram with HK as its diagonal, applying I.43 to equate the complements LB and BF, concluding LB equals C via CN1, and using vertical angles (I.15) to show angle ABM equals D. The AI proof adds explicit citations to I.34 (for properties of parallelogram BEFG such as opposite sides being parallel and opposite angles being equal), P1 (to join HB), and P2 (to produce lines), all of which Heath invokes implicitly without citation. Since heath_only is empty and ai_only contains only over-citations of foundational/construction results that support the same backbone, this is a clear Case A granularity difference.

### 1.45
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: divide the rectilineal figure into triangles via diagonals, construct a parallelogram equal to the first triangle using I.42, apply parallelograms equal to subsequent triangles using I.44, prove collinearity of adjacent sides using I.14 and I.29, establish that the result is a single parallelogram, and sum the areas using CN1 and CN2. The ai_only citation P1 is a postulate used for drawing diagonals, which is simple over-citation. The heath_only citation 1.33 reflects a different low-level justification for establishing the final parallelogram: Heath uses I.33 (lines joining equal and parallel lines are equal and parallel) while the AI uses I.34, I.29, and I.30 to argue the parallelism directly, reaching the same intermediate conclusion that the composite figure is a parallelogram. Since both proofs establish the same key intermediate conclusions with only citation-depth differences, this is Case A of Q2.

### 1.46
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: construct parallelogram ADEB via right angle (1.11) and parallel lines (1.31), show it is equilateral by combining opposite-side equality (1.34) with the construction AD=AB, then show it is right-angled by applying 1.29 to a pair of parallel sides with a transversal and using opposite-angle equality (1.34) to extend the right angle to all four corners. The AI uses a slightly different pair of parallels for the 1.29 step (AD parallel to BE with transversal AB, versus Heath's AB parallel to DE with transversal AD), but the logical structure is identical. The ai_only set consists entirely of over-citations: 1.3 (construction prop for cutting off equal lengths, used implicitly by Heath), CN1 (common notion for transitivity of equality), CN3 (common notion for the angle subtraction), and D1.22 (definition of square). Heath uses all of these implicitly without citing them by name. The heath_only set is empty. This is a clear Case A granularity difference.

### 1.47
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification as G. Both proofs share identical key intermediate conclusions: establishing collinearity of CA with AG and BA with AH via I.14, proving triangle congruence ABD = FBC via I.4, using the parallelogram-triangle doubling relation via I.41 to show each rectangular sub-region of the large square equals the corresponding smaller square, and combining via CN2. The AI proof follows Heath's exact logical backbone for the Pythagorean theorem proof. The ai_only set consists entirely of over-citations: 1.31 (for drawing a parallel line, a construction step), P1 (for joining lines), P4 (for right angles being equal), and CN1 (for doubles of equals being equal). These are all construction-level propositions, postulates, or common notions that Heath uses implicitly without formal citation. The heath_only set is empty, confirming the AI cites everything Heath cites plus additional foundational references. This is a clear Case A granularity difference with the same backbone and different citation depth.

### 1.48
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: construct AD perpendicular to AC and equal to AB, join DC, show DA^2 + AC^2 = BA^2 + AC^2 by adding AC^2 to both sides, apply I.47 to get DC^2 = DA^2 + AC^2, use the hypothesis to get BC^2 = BA^2 + AC^2, conclude DC = BC, then apply I.8 (SSS congruence) to show angle DAC = angle BAC, and since DAC is right, BAC is right. The AI cites six additional items (1.11, 1.3, P1, CN1, CN2, D1.10) that Heath leaves implicit: these are construction propositions (1.11 for perpendicular, 1.3 for equal length), a postulate (P1 for joining), common notions (CN1, CN2 for equality reasoning), and a definition (D1.10 for right angle). All appear at the same logical positions in both proofs, representing over-citation by the AI rather than any structural divergence. Heath's citation set is a proper subset of the AI's.


## Book 2

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 4 |
| Path difference (D) | 10 |
| AI proof error (E) | 0 |

**Total**: 14 propositions

### 2.1
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct rectangle BH from the uncut line A and the full segment BC using perpendiculars and parallels, then identify each sub-rectangle (BK, DL, EH) as rectangle(A, segment) by showing the relevant side equals A via I.34, and conclude by equating BH to the sum of the sub-rectangles. The AI proof cites the same four propositions as Heath (1.11, 1.3, 1.31, 1.34) plus three additional references: 1.29 to explicitly justify right angles in the sub-rectangles, CN2 to explicitly justify the additive combination, and D2.1 to cite the definition of rectangle. All three ai_only items are over-citations making explicit what Heath leaves implicit. Since heath_only is empty and the key intermediate conclusions are identical in both proofs, this is a granularity difference where the AI provides greater citation depth than Heath.

### 2.2
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification. Heath proves 2.2 by direct geometric construction: he builds the square ADEB on AB, draws CF parallel to AD/BE through C (I.31), decomposes the square into sub-rectangles AF and CE, and identifies each as rect(BA,AC) and rect(AB,BC) respectively. The AI instead reduces 2.2 to a special case of Proposition 2.1 by treating both 'two straight lines' as AB itself, with one copy cut at C into segments AC and CB. By 2.1, rect(AB,AB) = rect(AB,AC) + rect(AB,CB), and since sq(AB) = rect(AB,AB) by definition, the result follows. These are genuinely different logical backbones: Heath uses a geometric decomposition of the square via parallel lines, while the AI uses an algebraic reduction to an earlier theorem. Although 1.31 (Heath's only unique citation) appears inside Heath's proof of 2.1 (which the AI cites), this is not a containment scenario because Heath does not cite 2.1 at all in his proof of 2.2; he performs an independent direct argument. The AI's path is logically valid and complete, so Q3 yields D.

### 2.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 2.3 constructs a square CDEB on CB (I.46) and draws a parallel (I.31) to create a geometric figure whose sub-areas are identified as the rectangle AB,BC, the rectangle AC,CB, and the square on BC. The AI instead applies the previously proved Proposition 2.1 algebraically, treating BC as the uncut line and AB as the line cut into segments AC and CB, to obtain rectangle(AB,BC) = rectangle(BC,AC) + rectangle(BC,CB), then identifies rectangle(BC,CB) as the square on BC by definition. These are fundamentally different backbones: Heath uses geometric area decomposition via construction, while the AI uses an algebraic identity from a prior theorem. The proof-tree containment test confirms this is not mere granularity difference: Heath's proof of 2.1 contains I.31 but not I.46, so the heath_only citations are not fully subsumed by the AI's cited proposition. The AI's different path is logically valid under Q3, so the classification is D (path difference).

### 2.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof of 2.4 decomposes the square on AB geometrically by constructing the square ADEB, drawing parallels, and then identifying sub-regions as squares on AC and CB and rectangles equal to rect(AC,CB), using Book 1 geometric propositions (I.5, I.6, I.29, I.31, I.34, I.46). The AI proof takes an entirely different algebraic route: it applies Proposition 2.2 to express sq(AB) as the sum of two rectangles, then applies Proposition 2.3 twice to expand each rectangle into a square-plus-rectangle, and finally combines terms using commutativity and CN2. The Jaccard similarity is 0.0 with completely disjoint citation sets. The proof-tree containment test confirms this is not a granularity difference: Heath's proofs of 2.2 and 2.3 use only I.46 and I.31, whereas Heath's proof of 2.4 additionally uses I.29, I.5, I.6, and I.34 for geometric reasoning not present in or subsumed by the 2.2/2.3 proofs. The AI's algebraic chain is logically sound and complete, running from established prior results to the desired conclusion, so Q3 confirms the path is valid.

### 2.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof of 2.5 uses a geometric dissection approach: constructing a square on CB, drawing parallels (1.31), using complement equality (1.43), equal parallelograms on equal bases (1.36), and square construction (1.46) to show that the rectangle AD,DB plus square on CD equals the gnomon NOP plus LG, which is the whole square on CB. The AI proof takes an entirely different algebraic route, decomposing rect(AD,DB) via 2.1 into rect(CB,DB) + rect(CD,DB), then expanding rect(CB,DB) via 2.3, substituting to get 2*rect(CD,DB) + sq(DB), adding sq(CD), and recognizing the result as sq(CB) by 2.4. The key intermediate conclusions are completely different: Heath argues through area complements and gnomons in a geometric figure, while the AI argues through algebraic rectangle and square identities from earlier Book 2 propositions. This is Case B (different backbone) in Q2. Q3 confirms the AI path is valid: all citations are prior propositions applied correctly, and the logical chain from premises to conclusion is complete. The Jaccard similarity of 0.0 reflects the completely disjoint citation sets, confirming a genuine path difference.

### 2.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 2.6 using a geometric construction approach: he builds a square on CD, draws parallels, and argues through parallelogram complements (I.36, I.43) and gnomon areas to establish the rectangle-plus-square identity. The AI instead takes a purely algebraic route, decomposing rect(AD, DB) via the distributive law (2.1), expanding rect(CD, DB) via 2.3, and expressing sq(CD) via 2.4, then substituting to reach the conclusion. The key intermediate conclusions are entirely different: Heath works through geometric area equalities (AL = CH, CH = HF, AM = gnomon NOP), while the AI works through algebraic rectangle/square identities (rect(AD,DB) = 2*rect(CB,BD) + sq(BD), sq(CD) = sq(CB) + sq(BD) + 2*rect(CB,BD)). The citation sets are completely disjoint (Jaccard = 0.0), reflecting genuinely different proof strategies rather than mere citation-depth differences. The AI proof is logically complete, with each step correctly applying the cited proposition, so this is a valid alternative path.

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof is geometric: it constructs a square on AB (I.46), uses complements about the diagonal (I.43) to establish equality of regions, then manipulates gnomons to reach the conclusion. The AI's proof is algebraic: it applies the identity from 2.4 (square on whole equals squares on segments plus twice rectangle on segments), adds sq(CB) to both sides, then uses the identity from 2.3 (rectangle on whole and segment equals rectangle on segments plus square on segment) to express 2*rect(AB,BC) in terms matching the other equation, concluding by CN1. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different -- Heath reasons through geometric complements and gnomons while the AI reasons through algebraic identities from earlier Book 2 propositions. This is a genuine path difference with a valid alternative chain from premises to conclusion.

### 2.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof uses a geometric construction approach with a square on AD, identifying equal parallelogram complements (1.43) and equal parallelograms on equal bases (1.36) to build a gnomon that equals four times the rectangle, then adds the square on AC. The AI proof takes an entirely different algebraic path, applying Proposition 2.4 (square on sum of segments) to AD cut at B, then Proposition 2.7 (relating square on whole plus square on segment to twice rectangle plus square on other segment) to AB cut at C, and combining these through algebraic substitution to reach the same conclusion. The key intermediate conclusions are fundamentally different: Heath argues through geometric area relationships (quadruples of specific rectangular areas, gnomon composition), while the AI argues through algebraic identities from earlier Book 2 propositions. The zero Jaccard similarity (completely disjoint citation sets) confirms the entirely different proof strategies. The AI proof is logically complete and valid, establishing each step through properly cited prior results.

### 2.9
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof constructs a geometric figure with perpendiculars and parallels, then uses angle-chasing (I.32, I.29), isosceles triangle properties (I.6), parallelogram properties (I.34), and three applications of the Pythagorean theorem (I.47) to establish the result through geometric reasoning. The AI proof takes an entirely different algebraic route: it applies Proposition 2.4 (square of a sum) to expand sq(AD) and Proposition 2.7 (an algebraic identity) to express sq(DB), then adds the results and simplifies using the fact that AC = CB, with rectangle terms canceling via Common Notions. The two proofs share no key intermediate conclusions -- the Jaccard similarity is 0.0 with completely disjoint citation sets. The AI's algebraic path is logically complete: each step follows validly from cited propositions or common notions, and the chain runs from premises to conclusion without gaps. This is a genuine path difference (D).

### 2.10
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3. Heath's proof is entirely geometric: it constructs auxiliary points and triangles (CE perpendicular and equal to AC, parallelogram ECFG, triangle AEG), establishes angle properties via I.5, I.15, I.29, I.32, derives segment equalities via I.6, and applies the Pythagorean theorem (I.47) three times to relate sq(EA), sq(EG), and sq(AG) to the desired quantities. The AI proof takes a fundamentally different algebraic route, using three Book 2 identities directly: 2.7 to express sq(AD)+sq(DB) in terms of rect(AD,DB) and sq(AB), 2.4 to expand sq(AB) as 4*sq(AC), and 2.6 to express rect(AD,DB) as sq(CD)-sq(AC), then substituting to reach the conclusion. The two proofs share zero citations (Jaccard=0.0) and have completely different key intermediate conclusions: Heath argues through isosceles right triangles and repeated Pythagorean applications, while the AI argues through rectangular area identities and algebraic substitution. This is a genuine path difference (Case B at Q2). The AI's algebraic chain is logically complete and each cited proposition is correctly applied, so Q3 confirms validity, yielding category D.

### 2.11
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Both proofs share the same construction and the same critical first-half intermediate conclusion: rect(CF,FA) = sq(AB), derived via II.6, the construction EF=EB, and I.47. However, the proofs diverge in how they pass from this intermediate result to the final conclusion rect(AB,BH) = sq(AH). Heath uses geometric figure identification within the constructed diagram (FK=AD, subtract AK to get FH=HD, then identify HD and FH with their algebraic equivalents). The AI instead takes an algebraic decomposition route, using II.1 to decompose rect(CF,AH) into sq(AH) + rect(AH,AB), and II.2 to partition sq(AB) into rect(AB,AH) + rect(AB,HB), then equates and subtracts to reach the result. The use of II.1 and II.2 constitutes a genuinely different logical backbone for the second half of the proof, not merely a difference in citation depth. Since Q2 Case B applies (different backbone) and Q3 confirms the AI's alternative path is valid, the classification is D.

### 2.12
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G. Both proofs follow the same logical backbone: apply II.4 to expand the square on the extended line segment, apply I.47 twice to the two right triangles formed by the perpendicular, then substitute to reach the conclusion. The AI uses a different vertex labeling (obtuse angle at B rather than A) but the geometric argument is structurally identical. The ai_only citations (1.12 for constructing the perpendicular, D1.11 for the definition of obtuse angle, CN2 for the substitution step) are all construction, definition, and common notion items that Heath leaves implicit, representing over-citation rather than a different proof path. Heath_only is empty, confirming that the AI covers all of Heath's cited dependencies. This is Case A of Q2: same backbone, different citation depth.

### 2.13
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: apply II.7 to BC cut at D to get sq(CB)+sq(BD)=2*rect(CB,BD)+sq(DC), add sq(DA) to both sides, apply I.47 twice to substitute sq(AB)=sq(BD)+sq(DA) and sq(AC)=sq(CD)+sq(DA), then conclude sq(CB)+sq(AB)=2*rect(CB,BD)+sq(AC). The AI proof adds explicit citations for the construction of the perpendicular (1.12), the definitions of right angle, acute angle, and acute-angled triangle (D1.10, D1.12, D1.21), and the common notions justifying algebraic operations (CN1, CN2). These are all foundational or constructive references that Heath uses implicitly without citing. Since heath_only is empty and all ai_only items are over-citations of definitions, common notions, and construction propositions, Case A of Q2 holds, yielding a granularity difference classification.

### 2.14
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs argue through identical key intermediate conclusions: construct a rectangular parallelogram equal to the given figure (I.45), apply II.5 to obtain rect(BE,EF) + sq(GE) = sq(GF), establish GF = GH as radii, apply I.47 to the right triangle GEH, subtract sq(GE) from both sides to conclude rect(BE,EF) = sq(EH), and finally equate sq(EH) to the original figure. The AI proof cites the same three substantive propositions as Heath (1.45, 1.47, 2.5) and adds explicit citations for postulates (P1, P2, P3), definitions (D1.15, D1.17, D1.22), common notions (CN3), and basic constructions (1.3, 1.10, 1.46) that Heath invokes implicitly. Since heath_only is empty and all ai_only items are construction-level or foundational citations, this is a clear case of same backbone with different citation depth, yielding G.


## Book 3

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 24 |
| Path difference (D) | 13 |
| AI proof error (E) | 0 |

**Total**: 37 propositions

### 3.1
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct a chord AB, bisect it, draw a perpendicular, bisect the resulting diameter, then prove by contradiction that the midpoint of the diameter is the centre using SSS congruence (I.8) to show that an assumed alternative centre would force two right angles at the same point to be equal when one is a proper part of the other. The AI proof cites eight additional foundational items (1.10, 1.11, CN5, D1.15, D1.16, P1, P2, P4) that Heath leaves implicit, all of which are construction propositions, postulates, definitions, or common notions rather than substantive theorems introducing a different proof path. Heath's citation set is a proper subset of the AI's, with heath_only empty. This is a clear case of over-citation at the foundational level, not a different argumentative route.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate geometric conclusions: equal base angles of the isosceles triangle formed by two radii (I.5), the exterior angle inequality at the arbitrary point on the chord (I.16), combining these to get a strict angle inequality, and then applying I.19 to conclude the side opposite the larger angle is greater, yielding that the distance from center to the arbitrary point is less than the radius. The structural difference (Heath uses proof by contradiction assuming the line falls outside; the AI uses a direct proof taking an arbitrary point on the segment) does not change the geometric backbone. The citation difference is entirely non-substantive: the AI explicitly cites D1.15 (definition of circle) and P1 (postulate for joining lines) where Heath uses them implicitly. heath_only is empty, confirming the AI covers all of Heath's cited results. This is Case A of Q2: same backbone, different citation depth.

### 3.3
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs handle the two cases of the biconditional. Case 1 (bisection implies right angles) uses the same backbone in both proofs: SSS congruence via I.8 followed by the definition of right angles. However, Case 2 (right angles implies bisection) diverges fundamentally. Heath argues through I.5 (isosceles base angles) and I.26 (AAS triangle congruence) to establish AF=FB, while the AI uses I.47 (the Pythagorean theorem) to set up equations on the squares of the sides, then applies CN1 and CN3 to algebraically derive that the square on AE equals the square on EB, concluding AE=EB. These are genuinely different key intermediate conclusions: Heath's path goes through angle equality and triangle congruence, while the AI's path goes through the Pythagorean relation and algebraic subtraction of squares. The AI's path is logically valid, making this a path difference (D).

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: assuming the two chords bisect each other at E, finding center F, joining FE, showing FE perpendicular to AC (so angle FEA is right) and FE perpendicular to BD (so angle FEB is right) via 3.3, then deriving the contradiction that the two right angles are equal yet one is a proper part of the other. The AI proof cites CN5 (whole greater than part), P1 (drawing FE), and P4 (all right angles are equal), which are axioms and postulates that Heath uses implicitly without citation. Since heath_only is empty and ai_only consists entirely of foundational axioms/postulates/common notions, this is a clear case of the AI over-citing at a finer granularity while following the same logical backbone. Case A of Q2 applies: same backbone, different citation depth.

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs follow identical logical backbones: assume the two intersecting circles share a centre E, establish EC = EF (from E being centre of circle ABC) and EC = EG (from E being centre of circle CDG), derive EF = EG, then note that F lies between E and G so EG > EF, reaching a contradiction. The key intermediate conclusions are the same in both proofs at the same logical positions. The ai_only set consists entirely of CN1, CN5, P1, and P2 -- all common notions and postulates that Heath uses implicitly but the AI cites explicitly. CN1 justifies the transitive equality step, CN5 justifies the 'less to the greater' inequality, and P1/P2 justify the line constructions. Heath's proof performs the same steps without citing these foundational axioms. The empty heath_only set confirms there are no substantive propositions the AI omits. This is a clear case of over-citation by the AI, fitting Case A (same backbone, different citation depth).

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume a common centre F for circles ABC and CDE touching at C, join FC and draw line FEB, establish FC = FB (F is centre of ABC) and FC = FE (F is centre of CDE), derive FE = FB by transitivity, then note FE < FB since E lies between F and B, reaching a contradiction. The key intermediate conclusions are the same in both proofs. The citation difference arises because the AI explicitly cites foundational items (CN1, CN5, D1.15, D1.16, D3.3, P1, P2) that Heath leaves implicit. Heath cites no prior propositions at all, and the AI also cites no prior propositions — its ai_only set consists entirely of definitions, common notions, and postulates. This is a classic over-citation pattern representing a difference in citation granularity, not a difference in proof strategy.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions through the same logical backbone: (1) FA is greatest via the triangle inequality (1.20) and radii equality, (2) FD is least via the triangle inequality and subtraction, (3) nearer lines are greater than more remote lines via the SAS inequality (1.24) with equal radii and unequal included angles, and (4) exactly two equal lines exist via angle construction (1.23), SAS congruence (1.4), and a uniqueness argument by contradiction. The AI's additional citations (CN3, D1.15, D1.16, P1, P3) are all foundational items -- a common notion for subtraction, definitions justifying radii equality, and postulates for line-drawing constructions -- that Heath invokes implicitly. Heath_only is empty, confirming that the AI covers everything Heath cites. This is a classic over-citation pattern where the AI makes explicit the foundational steps that Heath leaves tacit, with no difference in the logical backbone.

### 3.8
**Category**: Path difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. While both proofs establish the same overall conclusions (ordering on concave circumference, ordering on convex circumference, uniqueness of equal lines), the logical paths diverge in two substantive ways. First, for the convex circumference ordering, Heath uses 1.21 (lines constructed within a triangle are less than the remaining two sides) to show DK < DL, while the AI uses 1.24 (SAS inequality) with an angle comparison argument noting that B lies between A and M, making the angle at M directly comparable. Second, for the uniqueness argument, Heath constructs the equal angle directly and uses 1.4, then argues by contradiction citing the earlier ordering result, while the AI uses 1.23 to construct the angle, 1.4 for SAS congruence, and then 1.8 (SSS) in the contradiction argument. These are genuinely different intermediate reasoning steps (not merely different citation depth), confirmed by the fact that heath_only items (1.21, 3.1) are not subsumed by any higher-level proposition the AI cites. The AI's alternative path is logically valid throughout, so the classification is D rather than E.

### 3.9
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3. Heath proves 3.9 constructively by joining chords, bisecting them, and using triangle congruence (I.8) to show the bisectors are perpendicular, then applying III.1 to conclude the center lies on each perpendicular bisector, with their unique intersection at D establishing D as the center. The AI instead uses proof by contradiction: assuming D is not the center and invoking Proposition 3.7, which states that from a non-center interior point only two equal straight lines can fall on the circle, directly contradicting the hypothesis that more than two equal lines fall from D. These are fundamentally different logical backbones — constructive perpendicular-bisector argument versus indirect argument via 3.7 — making this a genuine path difference. The AI's contradiction proof is logically complete and valid, so Q3 yields D.

### 3.10
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Classification was decided at Q2/Q3. Heath's proof uses perpendicular bisectors of chords connecting intersection points to show that both circles share the same center (contradicting III.5), citing only III.1 and III.5. The AI proof takes a fundamentally different approach: it finds the center K of one circle via III.1, observes that three equal radii KB=KG=KF fall from K onto the second circle (by D1.15), then performs an exhaustive case analysis on K's position relative to the second circle — inside (contradicted by III.9 implying K is also center of circle 2, violating III.5), outside (contradicted by III.8 allowing at most two equal lines), or on the circumference (contradicted by III.7 allowing at most two equal lines from a non-center point on the diameter). These are genuinely different logical backbones: Heath derives a shared center via perpendicular bisector geometry, while the AI derives contradictions via equal-line-count propositions III.7/III.8/III.9. The AI's path is logically complete — every step is supported by valid citations and the case analysis is exhaustive — so Q3(b) holds, yielding D.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs use identical logical backbones: a proof by contradiction assuming the line joining the centres does not pass through the point of contact, applying the triangle inequality to derive that a radius of one circle exceeds a radius of the other (or a segment that should be larger), yielding a contradiction. Heath's proof cites no explicit references (heath_refs is empty), while the AI explicitly cites 1.20 (triangle inequality), CN5 (whole greater than part), D1.15 (definition of circle/centre), and P1 (joining lines) -- all foundational items that Heath uses implicitly without citation. The key intermediate conclusions are the same in both proofs: the contradiction setup, the triangle inequality application, the radii equalities, and the final contradiction. The only difference is that the AI over-cites foundational references that Heath leaves implicit, which is a classic citation-depth difference (Case A of Q2).

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Both proofs use the same proof-by-contradiction strategy: assume the line joining the centres does not pass through the point of contact, form a triangle with the centres and the contact point, apply I.20 (triangle inequality), and derive a contradiction by comparing the sum of radii to the centre-to-centre distance. The key intermediate conclusions are the same backbone: radii from each centre to the contact point equal radii to points where the centre line meets each circle, and I.20 provides the contradicting inequality. The AI proof explicitly cites D1.15 (definition of circle/centre), D3.3 (definition of externally tangent circles), CN5 (whole greater than part), and P1 (joining points by a line), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only consists entirely of definitions, common notions, and a postulate, this is a clear Case A in Q2: same backbone with different citation depth, classifying as G.

### 3.13
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 reveals different backbones in both cases. For the internal tangency case, Heath derives a metric contradiction by comparing radii directly (BG = GD implies BG > HD, but BH = HD gives BH much greater than HD, contradiction), while the AI argues that collinearity plus equal radii forces both centers to be the midpoint of the segment between contact points, so the centers coincide, contradicting 3.6. For the external tangency case, Heath uses 3.2 (a chord falls within each circle) combined with D3.3 (external tangency means the chord falls outside one circle) to reach contradiction, while the AI uses 3.12 (line through centers passes through contact point) and the same midpoint-coincidence argument with 3.6. These are genuinely different logical paths: Heath never invokes 3.6, 3.12, or the midpoint argument, and the AI never invokes 3.2 or the metric inequality. Both paths are logically complete, so the classification is D.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions in both directions of the biconditional: perpendiculars from the center bisect the chords (III.3), halves of equal chords are equal, radii are equal, the Pythagorean theorem (I.47) yields squared equalities on the perpendicular distances, and subtraction of equals yields the result. The citation differences are purely at the granularity level: the AI over-cites foundational items (CN1, CN2, CN3 for arithmetic on equals, D1.15 for the definition of radius, P1 for drawing lines) that Heath uses implicitly, while Heath explicitly cites III.1 to find the center of the circle, which the AI assumes as given without citation. All ai_only items are common notions, definitions, or postulates (over-citation), and the single heath_only item (3.1) is a construction proposition for locating the center, which the AI handles by simply positing the center without formal citation. The logical backbone is the same throughout.

### 3.15
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 determined the classification. Both proofs establish the same two-part conclusion (diameter is greatest; nearer chord is greater) but through fundamentally different backbones. For Part 1, Heath constructs an auxiliary chord MN equal to BC using 3.14 and then applies the triangle inequality (1.20), while the AI directly applies the triangle inequality to the triangle formed by the center and the chord endpoints, noting BC equals the sum of two radii. For Part 2, Heath uses the SAS inequality theorem (1.24) on triangles with equal sides but unequal included angles, while the AI uses perpendicular bisection of chords (3.3) combined with the Pythagorean theorem (1.47) and algebraic manipulation of squares to compare half-chord lengths. The key intermediate conclusions differ in both parts: Heath's proof pivots on 3.14 and 1.24 (neither cited by the AI), while the AI's proof pivots on 1.47 and 3.3 (neither cited by Heath). The AI's path is logically valid throughout, satisfying Q3, so the classification is D.

### 3.16
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same three-part structure with identical key intermediate conclusions: (i) the tangent falls outside the circle by contradiction via an isosceles triangle (I.5) yielding two right angles in a triangle (contradicting I.17); (ii) no line can be interposed between the tangent and circumference, shown by dropping a perpendicular from the center to the supposed interposed line and using I.19 to show the foot of the perpendicular lies inside the circle, forcing the interposed line to cross the circumference; (iii) the angle of the semicircle exceeds any acute rectilineal angle and the horn angle is less, by showing any such angle would require an interposed line contradicting part (ii). The AI cites all three of Heath's references (1.5, 1.17, 1.19) plus ten additional items: definitions (D1.10, D1.12, D1.15, D1.17, D3.7), postulates (P1, P4), a construction proposition (1.12), and two substantive propositions (3.2, 3.7) that make explicit the reasoning Heath leaves implicit about points inside the circle and chords crossing the circumference. Since heath_only is empty and all ai_only items represent over-citation of steps that Heath performs without explicit reference, this is a citation-depth difference with the same logical backbone.

### 3.17
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 decides the classification as D (Path difference). Heath's proof constructs an auxiliary circle centered at E with radius EA, draws a perpendicular DF to EA, and uses triangle congruence (I.4) to show that angle EBA equals the right angle EDF, concluding tangency by III.16. The AI proof uses a fundamentally different construction: it bisects AE at midpoint M, draws a Thales circle with center M and radius MA, finds the intersection B with the given circle, and then proves angle ABE is a right angle through an elaborate but valid argument using isosceles triangle properties (I.5), supplementary angles (I.13), and angle sum in triangles (I.32). The key intermediate conclusions differ in both construction and logical method — Heath relies on SAS congruence while the AI relies on Thales circle properties proved via angle arithmetic. Additionally, the AI covers an extra case (point on the circle) not explicitly treated by Heath. The AI's path is logically complete and valid, satisfying Q3.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Both proofs use the same proof-by-contradiction structure: assume FC is not perpendicular to DE, draw FG perpendicular to DE, establish that angle FGC is right and angle FCG is acute (I.17), then conclude FC > FG (I.19). The key intermediate conclusions through step 3 are identical in both proofs. The proofs diverge only in how they articulate the final contradiction: Heath compresses it into FC = FB (radii) so FB > FG which is impossible, while the AI expands it by explicitly arguing that G lies inside the circle (D1.15), so DE cuts the circle (3.2, 3.16), contradicting tangency (D3.2). This divergence is a matter of citation depth, not a different logical backbone. The AI over-cites by including construction references (1.12), definitions (D1.10, D1.15, D3.2), a postulate (P1), and substantive propositions (3.2, 3.16) that merely expand the contradiction step Heath handles tersely. Since heath_only is empty, every Heath citation appears in the AI set, confirming no substantive step is missing. Q2 Case A applies: same backbone, different depth. Classification is G.

### 3.19
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction assuming the centre F lies off the perpendicular line CA, using III.18 to show FC is also perpendicular to the tangent DE, yielding two right angles at the point of contact where one is part of the other, which is impossible. The AI proof adds explicit citations to foundational items (P4 for equality of right angles, CN5 for whole-greater-than-part, D1.10 for right angle definition, D3.2 for tangent definition) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, common notions, and postulates, this is a clear case of over-citation at a deeper foundational level, making this a granularity difference.

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions using the identical logical backbone: (1) radii are equal so base angles of the isosceles triangle are equal (I.5), (2) the exterior angle of the triangle equals the sum of the two remote interior angles (I.32), giving the doubling relationship for each sub-angle, and (3) combining via addition or subtraction for the different cases. The AI proof covers three explicit cases (center on a side, center inside the angle, center outside the angle) while Heath covers two, but the underlying reasoning is the same. The ai_only set consists entirely of definitions (D1.15, D1.16, D3.8, D3.9), common notions (CN2, CN3), and postulates (P1, P2) — all foundational items that Heath uses implicitly without citation. The heath_only set is empty. This is a classic over-citation pattern where the AI explicitly cites construction and axiomatic foundations that Heath leaves implicit, constituting a citation-depth difference with the same backbone (Case A of Q2).

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: find the center of the circle, apply III.20 twice to show that the central angle subtending the chord is double each of the two inscribed angles in the same segment, then conclude the inscribed angles are equal. The AI proof cites additional items (3.1 for finding the center, P1 for joining lines, CN1 for the equality inference, D1.15 and D3.8 for definitions) that Heath leaves implicit, but these are all construction steps, postulates, common notions, and definitions — classic over-citation of non-substantive steps. Since heath_only is empty and the ai_only items are entirely non-substantive, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 3.22
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof joins the diagonals AC and BD, forms triangle ABC, uses I.32 (triangle angle sum equals two right angles) and III.21 (angles in the same segment are equal) to show that angle ADC equals the sum of angles BAC and ACB, then adds angle ABC to both sides to conclude that ABC + ADC = two right angles. The AI takes a fundamentally different approach: it finds the center O, applies III.20 (central angle is double the inscribed angle) to show that the two central angles at O corresponding to the two opposite inscribed angles are each double those inscribed angles, then argues that these two central angles partition the full revolution around O (four right angles, via I.13), so the two inscribed angles sum to two right angles. The key intermediate conclusions are entirely different -- Heath never uses the center or central angles, and the AI never uses diagonals, triangles, or the inscribed-angles-in-same-segment theorem. This is a genuine path difference with a valid alternative proof strategy, yielding classification D.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: assume two similar unequal segments ACB and ADB on the same side of AB, establish that a line from A through a point D on the outer arc crosses the inner arc at C, form a triangle BCD, and derive a contradiction by showing that the angle at C (exterior angle) must be both greater than (by I.16) and equal to (by Def. 3.11, similarity) the angle at D. The AI proof is more explicit in its construction and justification, citing D3.6 (definition of segment), D3.8 (definition of angle in a segment), and P1 (postulate for drawing lines), none of which Heath cites because he uses them implicitly. The heath_only set is empty, confirming that the AI covers all of Heath's reasoning. The difference is purely one of citation depth, not logical path.

### 3.24
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Both proofs use superposition: they apply segment AEB onto CFD, note that B coincides with D because AB equals CD, and then argue by contradiction that the segments must coincide. However, the key intermediate conclusion establishing the contradiction differs. Heath argues that if the segments do not coincide, a circle cuts a circle at more than two points, which is impossible by 3.10. The AI instead argues that non-coincidence would produce two similar and unequal segments on the same side of the same straight line, which is impossible by 3.23. Since 3.23 and 3.10 are substantive propositions establishing different geometric facts (3.23 concerns similar unequal segments on the same side of a line; 3.10 concerns circles cutting at more than two points), the backbones genuinely diverge at the contradiction step, making this Case B. The AI's path via 3.23 is logically valid since the superposed segment is similar to CFD by hypothesis and unequal by assumption, directly triggering 3.23's impossibility result. Q3 confirms the AI's different path is sound, yielding classification D.

### 3.25
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G. Both proofs share the same backbone: bisect AC at D, draw DB perpendicular to AC, split into three cases based on whether angle ABD is greater than, equal to, or less than angle BAD, in each case construct point E so that EA = EB = EC, then invoke 3.9 to identify E as the center and describe the complete circle. The AI proof cites every construction step explicitly (1.10, 1.11, 1.23, P1, P3, P4, D1.15, D3.6) and adds an explicit justification that E lies inside the circle via 3.2 before applying 3.9, whereas Heath leaves these constructions and the interior condition implicit. Since heath_only is empty and all ai_only items are either postulates, definitions, construction propositions, or an explicit justification of a premise Heath takes as obvious, this is Case A: same backbone, different citation depth.

### 3.26
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. For the centres case, Heath establishes arc equality by showing BC = EF via I.4, then arguing that segments BAC and EDF are similar (Def. 11), applying III.24 to conclude the similar segments on equal lines are equal, and finally subtracting the equal segments from the equal whole circles to get equal remaining circumferences. The AI instead uses a superposition method: after establishing BC = EF via I.4, it places one circle on the other so that centres, radii, and points coincide, then invokes CN4 (things that coincide are equal) to conclude the arcs are equal. For the circumferences case, Heath handles it through similar segments and III.24 as part of a unified argument, while the AI uses III.20 (central angle is double the inscribed angle) and CN2 to reduce the circumferences case to the already-proved centres case. The key intermediate conclusions differ substantively: Heath's backbone runs through similar segments and III.24, while the AI's runs through superposition (centres case) and III.20 with angle-doubling (circumferences case). Both paths are logically complete, so this is a genuine path difference.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: a proof by contradiction showing the central angles must be equal (assuming inequality, constructing an equal angle via I.23, applying III.26 to get equal arcs, deriving a contradiction), then using III.20 to transfer the result to inscribed angles. The AI proof explicitly cites CN1 (transitivity of equality for arcs BK and BC both equaling EF) and CN5 (whole is greater than part, for the contradiction) at the same logical positions where Heath uses these Common Notions implicitly. Since the key intermediate conclusions are identical and the only differences are the AI's explicit citation of foundational axioms that Heath leaves tacit, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs follow the same logical backbone: establish that radii of equal circles are equal, form two triangles with equal sides (two radii and the given equal chord), apply I.8 (SSS) to show the central angles are equal, invoke III.26 to conclude the minor arcs are equal, then subtract from the whole equal circles to conclude the major arcs are equal. The ai_only set {3.1, CN3, D3.1, P1} consists entirely of a construction proposition (3.1 for finding the center), a common notion (CN3 for subtracting equals), a definition (D3.1 for equal circles having equal radii), and a postulate (P1 for joining lines) — all of which Heath uses implicitly but does not cite explicitly. The heath_only set is empty, confirming the AI covers everything Heath cites. This is a classic Case A same-backbone situation with the AI providing finer citation granularity.

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) equal circumferences in equal circles yield equal central angles via III.27, (2) equal circles have equal radii, and (3) SAS congruence via I.4 gives BC = EF. The AI proof adds three over-citations not in Heath: 3.1 (finding centers), P1 (joining lines), and D3.1 (definition of equal circles), all of which are construction-level or definitional references whose underlying facts Heath states but does not formally cite. Since heath_only is empty and all ai_only items are construction/axiomatic over-citations with the same backbone present in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 3.30
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: bisecting AB at C, drawing CD perpendicular to AB, proving AD = DB by SAS (I.4), and concluding arc AD = arc DB via III.28 (equal chords cut off equal arcs). The ai_only citations (1.10, 1.11, P1, D1.10, D3.1) are exclusively construction propositions (bisecting a line, drawing a perpendicular), a postulate (joining points), and definitions (right angle, equal circles) that Heath leaves implicit. The heath_only set is empty, confirming no substantive step is missing from the AI proof. The AI's Step 8 explicitly justifying that a circle is equal to itself (via D3.1) to satisfy III.28's hypothesis about equal circles is an extra granularity step, not a different logical path. Since the backbones match and all differences are citation-depth matters, this is a granularity difference.

### 3.31
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: The classification is decided at Q2/Q3. Both proofs share the same backbone for the semicircle-right-angle case (I.5 twice for isosceles triangles, then I.32 and D1.10) and for the lesser-segment-obtuse case (III.22). However, for the greater-segment-acute case, the proofs diverge substantively: Heath uses I.17 (two angles of a triangle are less than two right angles) to conclude directly that angle ABC is less than a right angle given that BAC is right, while the AI uses III.20 (the inscribed angle theorem relating central and inscribed angles) to show that the inscribed angle standing on the minor arc must be less than a right angle. Since I.17 does not appear inside the proof of III.20, this is a genuinely different logical path, not a containment/granularity difference. Additionally, for the angle-of-segment parts (4 and 5), the AI explicitly invokes III.16 where Heath treats the result as manifest. The AI's alternative path via III.20 is logically valid, so Q3(b) holds, yielding classification D.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: (1) BA is a diameter and angle ABF is right, (2) angle ADB is right by 3.31, (3) angles ABD + BAD equal one right angle by 1.32, (4) angle DBF equals angle BAD by subtraction, (5) opposite angles of inscribed quadrilateral ABCD sum to two right angles by 3.22, and (6) angle DBE equals angle BCD by subtraction. The sole heath_only citation 3.19 (perpendicular to tangent passes through center) and the AI's citation of 3.18 (line from center to tangent point is perpendicular) are converses used to establish the same geometric fact. Indeed, Heath's proof of 3.19 itself relies on 3.18, so the AI is citing the more fundamental result directly. The remaining ai_only items (1.13, 3.21, D1.17, D3.2, D3.8, P1) are explicit citations of supplementary angle facts, angle-in-segment equality, definitions, and postulates that Heath leaves implicit. This is a clear case of same backbone with different citation depth.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions across all three cases (acute, right, obtuse): bisecting AB and using I.4 to show the circle passes through both endpoints, invoking III.16 to establish tangency of AD, and applying III.32 to equate the constructed angle with the angle in the alternate segment (with III.31 handling the right-angle case via semicircle). The AI proof's backbone matches Heath's exactly. The citation difference is entirely due to over-citation: the AI explicitly cites construction propositions (1.10, 1.11, 1.23), definitions (D1.15, D1.17, D1.18, D3.6, D3.8), and postulates (P1, P3) that Heath uses implicitly without formal citation. Heath_only is empty, confirming the AI captures all of Heath's cited steps. This is a same-backbone, different-depth situation (Case A in Q2), yielding Granularity difference.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct a tangent to the circle at a point B, construct angle FBC equal to the given angle D using I.23, then apply the alternate segment theorem III.32 to conclude that the angle in segment BAC equals angle D. The AI proof's additional citations (1.11, 3.1, 3.16, P1) all pertain to the explicit construction of the tangent line, which Heath handles implicitly with 'Let EF be drawn touching ABC at the point B.' The heath_only set is empty, confirming that Heath cites nothing beyond what the AI also cites. The ai_only items are purely construction and foundational references (finding center, drawing a line, erecting a perpendicular, tangent characterization), representing over-citation of construction details rather than any difference in logical path. This is a clear Case A in Q2: same backbone, different citation depth.

### 3.35
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: The AI proof uses a fundamentally different case structure from Heath's proof. Heath divides into two cases (both chords through the centre; neither through the centre), while the AI divides into three cases (both through centre; exactly one through centre; neither through centre) and reduces Case 3 to Case 2 by constructing a diameter through the intersection point E. In Heath's main case, perpendiculars are drawn from the centre to both chords, both are bisected by III.3, and II.5 plus I.47 are applied symmetrically to both chords. In the AI's Case 2, one chord is the diameter itself so II.5 is applied differently (the diameter is bisected at the centre rather than by a perpendicular), producing a distinct chain of intermediate conclusions. The AI's Case 3 reduction via a constructed diameter is an entirely different strategy from Heath's direct argument. Since the key intermediate conclusions and case organization differ but the AI's chain is logically sound throughout, this is classified as D (path difference) at Q2/Q3.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs address the same two cases (secant through the center, secant not through the center) and establish identical key intermediate conclusions in each case: angle at tangent point is right (III.18), the chord is bisected (by the center in Case 1, by perpendicular from center in Case 2 via III.3), application of II.6 to get the rectangle plus a square equals another square, repeated applications of I.47 (Pythagorean theorem) to replace sums of squares, equality of radii, and subtraction to reach the final result. The ai_only set consists entirely of over-citations: construction propositions (1.12, P1), common notions (CN1, CN2, CN3), and definitions (D1.15, D1.17) that Heath uses implicitly. The heath_only set is empty, confirming no substantive citation divergence. This is Case A of Q2: same backbone, different citation depth.

### 3.37
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct a tangent DE from the external point D, apply III.36 to establish rect(AD,DC) = sq(DE), combine with the hypothesis rect(AD,DC) = sq(DB) to get DE = DB, then use triangle congruence (I.8) with radii FE = FB and common side FD to show angle DBF = angle DEF, conclude angle DBF is right since angle DEF is right (III.18), and finally invoke III.16 to conclude DB is tangent. The ai_only set consists entirely of construction propositions (3.1, 3.17), a common notion (CN1), a definition (D1.15), and a postulate (P1) that Heath uses implicitly without citation. The heath_only set is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.


## Book 4

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 16 |
| Path difference (D) | 0 |
| AI proof error (E) | 0 |

**Total**: 16 propositions

### 4.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: draw a diameter of the circle, handle the trivial case where the diameter equals the given line, and in the main case construct a segment equal to the given line from an endpoint of the diameter, draw a circle with that segment as radius centered at the endpoint, and show that the chord from the endpoint to the intersection point equals the given line via the definition of a circle. The AI proof explicitly cites elementary constructions and definitions (3.1 for finding the center, 1.3 for cutting off a segment, P1 and P3 for joining lines and drawing circles, D1.15 for the circle definition, D1.17 for diameter, D4.7 for fitting, and CN1 for transitivity of equality) while Heath's proof performs the same constructions and reasoning without explicit citations. Since heath_refs is empty, all AI citations appear in ai_only, but these are all construction propositions, postulates, definitions, and common notions representing over-citation of elementary steps rather than a different proof strategy. The backbones are identical, making this a granularity difference.

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct a tangent at a point on the circle (III.16), construct two angles equal to the given triangle's angles (I.23), join the chord, apply the alternate segment theorem (III.32) twice to establish two angle equalities, then use the angle sum property (I.32) to derive the third. The ai_only set consists entirely of common notions (CN1, CN3), a definition (D4.3), and a postulate (P1), which are foundational items Heath leaves implicit. The heath_only set is empty. Since the key intermediate conclusions are identical and the citation differences consist only of the AI over-citing axiomatic and definitional foundations, this is a granularity difference.

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct angles at center K equal to the exterior angles of the given triangle, draw tangent lines at the resulting points on the circle, then use quadrilateral angle sums and supplementary angle relationships (I.13) to show each vertex angle of the circumscribed triangle equals the corresponding angle of the given triangle, with I.32 closing the third angle. The heath_only citations (3.1 and 3.18) reflect citation-depth differences rather than backbone divergence: Heath explicitly cites III.1 to find the center while the AI takes the center as given, and Heath uses III.18 (radius perpendicular to tangent) after constructing tangents via III.16, whereas the AI reverses the approach by first constructing perpendiculars to radii via I.11 then citing III.16 to establish tangency. Both routes establish the same intermediate fact (right angles between radii and tangent lines). The ai_only citations (1.11, CN1, CN3, D4.4, P1, P2) are all construction steps, common notions, a definition, and postulates representing over-citation by the AI. The key intermediate conclusions are identical in both proofs.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: bisect two angles of the triangle (I.9), drop perpendiculars from the intersection point to the three sides, use triangle congruence (I.26) to show all three perpendicular distances are equal, construct the circle, and invoke III.16 to establish tangency. The AI proof explicitly cites I.12 (perpendicular construction), P4 (right angles are equal), CN1 (transitivity of equality), and P3 (circle construction), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only construction propositions, postulates, and common notions, this is a clear Case A granularity difference where the AI over-cites foundational steps that Heath takes as understood.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect two sides of the triangle, erect perpendicular bisectors at the midpoints, show via SAS congruence (I.4) that the intersection point F is equidistant from all three vertices, and conclude the circle centered at F passes through all vertices. The AI bisects AB and BC (rather than Heath's AB and AC), but this is merely a choice of which two sides to use and does not alter the logical structure. The ai_only set consists entirely of construction propositions (1.11), an additional justification for why perpendiculars meet (1.28), common notions (CN1), definitions (D1.15, D4.6), and postulates (P1, P3, P4) -- all items that Heath leaves implicit. The heath_only set is empty. The AI also provides a single unified argument rather than Heath's three separate cases, but both approaches validly establish FA=FB=FC. This is a clear case of same backbone with different citation depth.

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification. Both proofs establish the same two key intermediate conclusions: (1) quadrilateral ABCD is equilateral and (2) ABCD is right-angled, then conclude it is a square by definition. Heath proves equilateral first using I.4 and right-angled second using III.31; the AI reverses the order but uses the same propositions for the same purposes. The ai_only set consists entirely of construction and foundational citations (1.11 for drawing the perpendicular, D1.15 and D1.17 for definitions of circle/diameter, P1 and P4 for postulates, CN1 for common notion, D4.3 for inscribed definition) that make the AI proof more explicit without changing the logical backbone. Heath_only is empty, confirming the AI cites a strict superset. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: drawing two perpendicular diameters, constructing tangent lines through the endpoints to form quadrilateral FGHK, establishing parallelism of opposite sides, proving the quadrilateral is equilateral, proving all angles are right, and concluding FGHK is a circumscribed square. The heath_only citations (1.30, 3.18) reflect minor route differences at the same logical positions: Heath uses 3.18 to derive perpendicularity from tangency while the AI constructs perpendiculars first via 1.11 and verifies tangency via 3.16, and Heath uses 1.30 for transitivity of parallels while the AI proves both parallel pairs directly via 1.28. The ai_only citations (1.11, 1.32, CN1, CN2, D1.15, D1.22, D4.4) are construction steps, definitions, common notions, and a detailed angle calculation that represent greater citation explicitness rather than a different logical path. The same key geometric facts are established at the same logical positions in both proofs, differing only in citation depth.

### 4.8
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: bisect two sides of the square, draw parallels through the midpoints to locate the center, use parallelogram properties (I.34) to show the four distances from the center to the midpoints are equal, construct the circle, and then invoke III.16 to show the circle touches rather than cuts each side. The key intermediate conclusions are identical in both proofs. The heath_only set is empty, meaning every citation Heath uses also appears in the AI proof. The ai_only set consists entirely of definitions (D1.22, D4.5), common notions (CN1), postulates (P1, P3, P4), and one additional proposition (1.29, used to explicitly justify perpendicularity of radii to sides via parallel lines). These are all instances of the AI citing foundational results that Heath leaves implicit, which is a citation-depth difference rather than a structural divergence.

### 4.9
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: join diagonals AC and BD at point E, use I.8 to show the diagonals bisect the corner angles of the square, then use I.6 to show all four segments EA, EB, EC, ED are equal (since the base angles in each sub-triangle are equal), and finally describe a circle with center E passing through all four vertices. The AI proof adds explicit citations for definitions (D1.22 for the square, D4.6 for circumscription), postulates (P1 for drawing lines, P3 for describing the circle), and a common notion (CN1 for transitivity of equality), all of which Heath leaves implicit. Since heath_only is empty and ai_only consists entirely of foundational items (definitions, postulates, common notions), this is a clear Case A: same backbone with the AI citing at greater depth.

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decides this as G (granularity difference). Both proofs share the same logical backbone: cutting AB at C via II.11, fitting BD = CA in circle BDE, circumscribing circle ACD, establishing BD is tangent to circle ACD, using the alternate segment theorem (III.32) to get angle BDC = angle DAC, then using angle sums (I.32), isosceles triangle properties (I.5), and I.6 to show each base angle of triangle ABD is double the vertex angle. The ai_only citations (4.1, P1, P3) are construction postulates and propositions that Heath uses implicitly. The AI cites 3.36 instead of Heath's 3.37, but the AI explicitly writes 'by the converse of the tangent-secant theorem,' demonstrating correct logical reasoning with merely a wrong proposition number label. Under the lenience rule this is not an error but a citation-depth difference. All key intermediate conclusions appear in both proofs at the same logical positions, making this Case A of Q2.
**Audit Record**: CANDIDATE E — 4.10
  violated_claim : BD touches circle ACD at D
  failure_mode   : invalid_inference
  missing_is     : expansion
  evidence       : AI Step 7 cites [3.36] but says 'by the converse of the tangent-secant theorem' - 3.36 is the direct theorem, 3.37 is the converse. The AI uses the correct logical direction but cites the wrong number.
  why_not_terse  : The cited proposition 3.36 is the forward direction, not the converse needed here. However, the AI text explicitly invokes the converse, making this a citation numbering error not a logical gap.
VERDICT: NOT-E. missing_is = expansion. The AI demonstrates correct reasoning (invoking the converse) but mislabels the proposition. Lenience rule applies: compressed-but-sound. Reclassified to G.

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct isosceles triangle FGH with base angles double the vertex angle (IV.10), inscribe an equiangular triangle ACD in the circle (IV.2), bisect the double angles (I.9) to obtain five equal inscribed angles, derive equal arcs (III.26), equal chords (III.29) for equilateral, and equal combined arcs yielding equal interior angles (III.27) for equiangular. The only citation difference is that the AI adds D4.3 (the definition of a polygon inscribed in a circle) to explicitly justify the final conclusion, while Heath leaves this implicit. Since heath_only is empty and ai_only contains only a definition, this is a classic over-citation granularity difference with identical backbone structure.

### 4.12
**Category**: Granularity difference
**Jaccard**: 0.467
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same logical backbone: inscribe a regular pentagon (IV.11), draw tangents at each vertex (III.16/III.18), establish equal tangent segments from each external point using the Pythagorean theorem (I.47) and SSS congruence (I.8), prove congruence of triangles at adjacent vertices via AAS (I.26), and conclude the circumscribed pentagon is equilateral and equiangular. The citation differences are all matters of depth: the AI explicitly cites foundational items (CN1, CN2, D1.15, D4.4, P1) that Heath uses implicitly; the AI adds 3.28 (equal chords yield equal arcs) as an explicit intermediate step before applying 3.27, whereas Heath proceeds directly from the equal arcs established by IV.11; the AI uses 1.32 (angle sum of a triangle) for the equiangular conclusion where Heath achieves the same result through I.26 alone; and Heath cites 3.1 to find the center of the circle while the AI simply names the center and invokes D1.15 for equal radii. All key intermediate conclusions are present in both proofs at the same logical positions, making this a Case A granularity difference.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs share the same backbone: bisect angles BCD and CDE to locate center F, show all five perpendiculars from F to the sides are equal via I.26 triangle congruences, and use III.16 to establish that the circle with center F is inscribed. The AI proof over-cites by explicitly referencing construction propositions (I.9 for angle bisection, I.12 for perpendicular dropping), common notions (CN1, CN3), definitions (D1.10, D4.5), and a postulate (P3) that Heath leaves implicit. The one substantive ai_only citation, I.6, is used to explicitly establish FC = FD from equal base angles in triangle FCD, whereas Heath establishes the same fact implicitly through the I.4 congruence of triangles BCF and DCF. Heath_only is empty, confirming the AI cites a strict superset. All key intermediate conclusions are the same in both proofs, making this a citation-depth difference rather than a path difference.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect angles BCD and CDE to find center F, show FC = FD via I.6 from equal base angles, extend to prove all five distances FA = FB = FC = FD = FE are equal, then circumscribe the circle. The AI proof explicitly works through each congruence step using I.4 (SAS) where Heath abbreviates with 'similarly it can be proved.' The ai_only set consists entirely of construction propositions (1.9), postulates (P1, P3), definitions (D1.15, D4.6), common notions (CN1), and the SAS congruence theorem (1.4) that Heath leaves implicit. The heath_only set is empty, confirming that the AI covers all of Heath's cited material. This is a clear Case A: same key intermediate conclusions with the AI providing finer-grained citation depth.

### 4.15
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they construct the hexagon by drawing a circle with center D and radius DG, prove that certain triangles at the center are equilateral, establish that all six central angles equal one-third of two right angles, then use III.26 (equal central angles yield equal arcs), III.29 (equal arcs yield equal chords) for equilateral, and III.27 (equal arcs yield equal inscribed angles) for equiangular. The sole substantive difference is that Heath uses I.15 (vertical angles) to obtain three of the six central angles at once, while the AI instead applies I.13 (supplementary angles) repeatedly to derive each remaining central angle individually. The key intermediate conclusions are identical in both proofs; the difference is only in citation depth. The ai_only set consists of over-citations (definitions D1.15, D1.20, D4.3; postulates P1, P3; common notion CN2; construction step 3.1) plus 1.13 as a mechanical substitute for 1.15, all consistent with granularity rather than path divergence.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: inscribe a side of the equilateral triangle (subtending 5/15 of the circumference) and a side of the regular pentagon (subtending 3/15), compute the remaining arc BC as 2/15, bisect it at E using 3.30 to obtain arcs of 1/15, then fit equal chords around the circle to produce the 15-gon. Heath's proof cites only 3.30 and leaves all other justifications implicit, while the AI explicitly cites 1.1, 4.2, 4.11, 3.28, 3.29, 3.30, 4.1, 3.27, and P1 — all of which are construction steps, supporting lemmas, or axioms that Heath uses implicitly. The heath_only set is empty, confirming no citations are missing from the AI. The AI also adds an explicit equiangularity argument (Step 10 via 3.27) that Heath simply asserts. This is a same-backbone, different-depth scenario: the AI over-cites by making explicit what Heath leaves implicit, yielding a granularity difference.


## Book 5

| Category | Count |
|---|---|
| Perfect match (P) | 4 |
| Granularity difference (G) | 16 |
| Path difference (D) | 5 |
| AI proof error (E) | 0 |

**Total**: 25 propositions

### 5.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: decomposing the equimultiples into their constituent equal parts and then working pairwise with those parts to reach the conclusion. Heath's proof uses no explicit citations (heath_refs is empty), relying implicitly on the definition of multiple and basic common notions. The AI proof follows the same structural approach but explicitly cites the foundational items it invokes: D5.1 and D5.2 (definitions of part and multiple) and CN2 and CN3 (common notions about adding and subtracting equals). Since ai_only contains only definitions and common notions (no substantive propositions) and heath_only is empty, this is a Case A situation under Q2: same logical backbone with different citation depth. The AI over-cites foundational axioms and definitions that Heath leaves implicit, which is a granularity difference.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that AB contains as many parts equal to C as DE contains parts equal to F (by the definition of equimultiple), likewise for BG and EH, then combine these counts to conclude that the total AG has as many parts equal to C as DH has equal to F. The AI proof explicitly cites D5.2 (definition of equimultiple) and CN2 (common notion on addition) at each step, while Heath's proof uses these same foundational items implicitly without formal citation. Since heath_refs is empty and ai_only contains only a common notion and a definition, the difference is purely one of citation depth for foundational items, not a difference in the logical path. Case A of Q2 holds, yielding Granularity difference (G).

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decompose the equimultiples into constituent parts equal to A and C respectively, observe that each part preserves the equimultiple relationship with B and D (since A=m*B and C=m*D), then apply Proposition 5.2 to combine these parts and conclude that the total sum maintains the equimultiple relationship. The only citation difference is that the AI explicitly cites Definition 5.2 (the definition of equimultiple) where Heath leaves this implicit. Since D5.2 is a definition rather than a substantive proposition, and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference falling under Case A of Q2, yielding a Granularity difference classification.

### 5.4
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 5.4 follow identical logical backbones: both take arbitrary equimultiples K, L of E, F and M, N of G, H, apply Proposition 5.3 to show K, L are equimultiples of A, C and M, N are equimultiples of B, D, then invoke Definition 5.5 twice -- first with the hypothesis A:B :: C:D to obtain the three-way excess/equal/less comparison, and second to conclude E:G :: F:H. The citation sets are identical (5.3 and D5.5) with Jaccard similarity 1.0, ai_only and heath_only are both empty, and the key intermediate conclusions match exactly, satisfying the perfect match criterion.

### 5.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use Proposition 5.1 to relate equimultiples of the component magnitudes, then apply subtraction to isolate the remainder and conclude it is the required multiple of the remainder. Heath constructs EB as a multiple of a new magnitude CG and uses 5.1 to combine equimultiples, while the AI decomposes each of the n copies of CD into CF and FD and uses 5.1 to recombine. The key intermediate conclusions are equivalent: both establish via 5.1 that the sum of equimultiples relates to the whole, and both subtract the known part to find the remainder. The ai_only set consists entirely of common notions (CN1, CN3) and definitions (D5.1, D5.2), which are foundational items the AI explicitly cites but Heath leaves implicit. The heath_only set is empty, confirming no substantive proposition is missing from the AI proof. This is Case A of Q2: same backbone with different citation depth, yielding Granularity difference (G).

### 5.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they use Proposition 5.2 to relate equimultiples and their parts, then show the remainders after subtraction are determined by the difference of the multipliers. Heath proves this with geometric construction (making CK equal to F) and explicit case separation, while the AI uses algebraic notation (m, n) for a unified argument but reaches the same key intermediate conclusions. The ai_only citations (CN3, D5.2) are a common notion and a definition that Heath uses implicitly without explicit citation. Heath_only is empty. This pattern of the AI over-citing foundational axioms and definitions while following the same proof strategy is a citation-depth difference, not a path difference.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: (1) establish that equimultiples of equal magnitudes are equal (mA = mB from A = B), (2) infer that equal equimultiples bear the same order relation to any multiple of C, then apply Definition 5.5 to conclude A:C = B:C, and (3) repeat the argument with reversed positions to conclude C:A = C:B. The only difference is citation depth: the AI explicitly cites CN1 (equals bear the same relations), CN2 (adding equals yields equals), and D5.2 (definition of equimultiple), while Heath uses these foundational facts implicitly without citing them by name. Since heath_only is empty and all ai_only items are common notions and definitions rather than substantive propositions, this is a clear case of over-citation at the axiomatic level with no backbone divergence, yielding a Granularity difference (G).

### 5.8
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they construct equimultiples of the original magnitudes (mA and mC), find a suitable comparison multiple (nB), and demonstrate the inequality pair required by D5.7 (mA > nB while mC does not exceed nB). The AI takes a more streamlined algebraic approach using the excess E = A - C directly rather than Heath's geometric construction with labeled points, but the logical backbone is identical. Heath's two geometric cases (AE < EB vs AE > EB) are absorbed by the AI's single general argument, which is valid because it does not depend on which part of the excess is smaller. The only citation difference is that the AI explicitly cites CN5 (the whole is greater than the part) in Case 2 of Part (ii), where Heath simply says the demonstration follows the same pattern as before. Since heath_only is empty and ai_only contains only the common notion CN5, this is a citation-depth difference with the same backbone, yielding G.

### 5.9
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs of 5.9 follow identical logical structure: two cases proved by contradiction using only Proposition 5.8. Case 1 shows that if A:C = B:C then A = B (since assuming A != B leads to A:C != B:C by 5.8, contradicting the hypothesis). Case 2 shows that if C:A = C:B then A = B (since assuming A != B leads to C:A != C:B by 5.8, contradicting the hypothesis). The citation sets are exactly equal (both cite only 5.8), the key intermediate conclusions are identical, and the logical backbone is the same. The AI proof is more verbose, spelling out the contradiction in greater detail, but this does not affect the classification. Since ai_used equals heath_refs exactly and the backbones match, this is a perfect match.

### 5.10
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both the AI and Heath proofs follow the identical logical backbone: a two-case proof by contradiction. In each case, equality is ruled out via 5.7 and the wrong inequality is ruled out via 5.8, leaving the desired conclusion. The key intermediate conclusions are the same in both proofs in the same order. The only citation difference is that the AI additionally cites D5.7 (the definition of greater ratio), which Heath uses implicitly without explicit citation. Since ai_only contains only this definition and heath_only is empty, this is a classic over-citation of a definitional item, constituting a citation-depth difference rather than a path difference. The citation sets are not identical (ai_used includes D5.7), so Perfect match (P) does not apply.

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: (1) take equimultiples of A, C, E and of B, D, F; (2) apply Definition 5.5 to A:B :: C:D to get that the comparison of multiples of A and B determines the comparison of multiples of C and D; (3) apply Definition 5.5 to C:D :: E:F to get the analogous result for C, D and E, F; (4) chain these two results so that the comparison of multiples of A and B determines the comparison of multiples of E and F; (5) conclude A:B :: E:F by Definition 5.5. The only difference is that the AI explicitly cites D5.5 while Heath's proof uses the definition implicitly without a formal citation. Since heath_refs is empty and ai_only contains only a definition (D5.5), this is a same-backbone, different-citation-depth situation (Case A), yielding G.

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they take equimultiples, use the definition of proportion (D5.5) to extract simultaneous comparisons from the given proportionality, aggregate those comparisons across all pairs by adding inequalities and equalities, use V.1 to relate individual equimultiples to equimultiples of the sums, and conclude by D5.5. The AI over-cites definitions (D5.1-D5.4) and Common Notion 2 that Heath leaves implicit, but these are axiom-level over-citations, not substantive path differences. With heath_only empty and ai_only consisting entirely of definitions and a common notion, and the key intermediate conclusions matching between both proofs, this is a clear Case A granularity difference.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 5.13 follow identical logical backbones and cite exactly the same references. Both proofs (1) invoke Definition 5.7 to obtain equimultiples of C,E and D,F such that the multiple of C exceeds the multiple of D while the multiple of E does not exceed the multiple of F; (2) form the corresponding equimultiples of A and B using the same multipliers; (3) apply Definition 5.5 (the definition of same ratio for A:B :: C:D) to transfer the excess relationship; and (4) apply Definition 5.7 again to conclude A:B > E:F. The citation sets are identical (D5.5, D5.7) with Jaccard similarity 1.0, and since both the key intermediate conclusions and the citation sets match exactly, the classification is P (Perfect match).

### 5.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Heath's proof explicitly works out only the case A > C (using 5.8, 5.13, 5.10) and abbreviates the remaining two cases with 'similarly we can prove.' The AI proof uses the identical logical backbone for Case 1 (A > C): 5.8 yields A:B > C:B, 5.13 with the hypothesis yields C:D > C:B, and 5.10 concludes D < B. The AI then explicitly proves Case 2 (A = C) using 5.7, 5.11, 5.9 and Case 3 (A < C) using 5.8, 5.13, 5.10, which are the cases Heath leaves to the reader. All ai_only citations (5.7, 5.9, 5.11, D5.5) serve these elaborated cases or reference the definition of same ratio. Since the key intermediate conclusions match for the shared explicit case, and the extra AI citations arise solely from spelling out what Heath abbreviates, this is a citation-depth difference, yielding G.

### 5.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof divides the multiples into unit parts equal to the original magnitudes, then uses V.7 (equal magnitudes have the same ratio) to establish ratios between corresponding parts, and V.12 (antecedent-to-consequent ratio equals all-antecedents-to-all-consequents) to combine them. The AI proof takes a fundamentally different approach: it appeals directly to Definition 5.5 (the equimultiple definition of ratio), uses Proposition 5.3 to establish that a multiple of a multiple equals a higher multiple of the original, and then shows via CN2 that ordering is preserved. The two proofs share zero citations (Jaccard = 0.0), and the containment test confirms that heath_only items 5.7 and 5.12 do not appear in the proof tree of any AI-cited proposition. The key intermediate conclusions differ entirely: Heath works through decomposition and recombination of multiples, while the AI works through the definitional characterization of ratio and algebraic properties of multiples. The AI's path is logically valid under the hardened 1(b) standard, yielding D.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) equimultiples of the first pair preserve the ratio (by 5.15), (2) equimultiples of the second pair preserve their ratio (by 5.15), (3) transitivity chains these proportions together (by 5.11), (4) the trichotomy comparison follows (by 5.14), and (5) the definition of proportion (D5.5) yields the alternate proportion. The only citation difference is that the AI explicitly cites D5.12 (the definition of alternate ratio) when setting up the problem in Step 1, while Heath does not cite this definition. Since D5.12 is a definition rather than a substantive proposition, this is a classic over-citation at the definitional level, constituting a citation-depth difference under Case A of Q2.

### 5.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) construct equimultiples of the compound magnitudes using 5.1, (2) construct combined equimultiples of the parts using 5.2, (3) apply the proportion hypothesis to obtain the trichotomy for compound multiples, (4) subtract common terms to reduce to a trichotomy on the separated multiples, and (5) conclude by the definition of proportion. The ai_only set consists entirely of definitions (D5.5, D5.14, D5.15) and common notions (CN2, CN3, CN5) that Heath uses implicitly but does not cite. For example, Heath writes 'if HK be subtracted from each' which is exactly CN3, and Heath implicitly invokes the definition of proportion (D5.5) when applying the equimultiple criterion. The heath_only set is empty. This is a clear Case A: same backbone, different citation depth, classifying as G.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as D (path difference). Heath proves 5.18 by reductio ad absurdum: assuming AB:BE equals CD:DG for DG less than DF, applying 5.17 (separando) to get AE:EB = CG:GD, then using 5.11 (transitivity of ratios) and 5.14 (ordering from ratios) to derive the contradiction GD > FD. The AI instead gives a direct proof from the definition of proportion (D5.5), showing that for arbitrary equimultiples m and n, the threefold condition transfers from the separando ratios to the componendo ratios by algebraic decomposition (AB = AE + EB implies m*AB = m*AE + m*EB), splitting into three sub-cases (n > m, n = m, n < m). The AI uses no prior theorems at all, working entirely from definitions (D5.5, D5.14, D5.15) and common notions (CN2, CN3, CN5), resulting in zero citation overlap (Jaccard = 0.0). These are fundamentally different proof strategies with no shared key intermediate conclusions, constituting a genuine path difference. The AI proof is logically complete under the Q1(b) hardened standard.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow the identical logical backbone: given AB:CD = AE:CF, both apply alternando (5.16) to obtain AB:AE = CD:CF, then separando (5.17) to derive EB:AE = FD:CF, then alternando (5.16) again to reach EB:FD = AE:CF, and finally transitivity of ratios (5.11) to conclude EB:FD = AB:CD. The citation sets are identical (ai_used = heath_refs = {5.11, 5.16, 5.17}) with Jaccard similarity 1.0, and the key intermediate conclusions match at every stage. Since the proofs share the same backbone and the same citation set, this is a perfect match.

### 5.20
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: for the A > C case, they establish A:B > C:B via 5.8, then use 5.13 to derive D:E > F:E via the given and inverse ratios, and conclude D > F via 5.10. Heath handles the A = C and A < C cases with 'similarly we can prove,' while the AI spells them out explicitly, citing 5.7, 5.9, and 5.11 for the equality case and reusing 5.8, 5.13, 5.10 for the less-than case. The AI also explicitly cites D5.5 to justify the inverse ratio step that Heath performs implicitly. Since heath_only is empty and all ai_only items (5.7, 5.9, 5.11, D5.5) represent either explicit treatment of cases Heath leaves as exercises or more granular citation of implicit steps, the proofs reach the same key intermediate conclusions at different citation depths, yielding a granularity difference.

### 5.21
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path (D). Heath's proof of the A > C case operates at the level of ratio comparisons: it uses 5.8 to get A:B > C:B, then 5.13 to transfer the greater-ratio through the hypotheses to get E:F > E:D, and finally 5.10 to conclude F < D. The AI proof instead works directly from the definitions of ratio (D5.5 and D5.7), unpacking 'greater ratio' into specific multiples m and n, then using D5.5 to transfer the multiple-inequalities through the ratio hypotheses, and assembling D > F from arithmetic on multiples without ever establishing ratio-comparison intermediate conclusions. The key intermediate conclusions differ: Heath reasons about ratio orderings (E:F > E:D) while the AI reasons about specific multiples (mE > nF, nD > mE). Furthermore, for Case 2 (A = C), the AI uses proof by contradiction while Heath merely says 'similarly we can prove.' The proof-tree containment test shows that 5.10 and 5.13 (heath_only) are not inside the proof of any proposition the AI cites as a unit; rather, the AI re-derives their substance from definitions, constituting a genuinely different proof strategy. The AI's path is logically complete and valid under the hardened 1(b) standard.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they take equimultiples of the outer terms, establish that equimultiples of the first pair maintain the same ratio, establish that equimultiples of the second pair maintain the same ratio, apply 5.20 for the ordering result on three pairs, and conclude via D5.5. The difference is purely in citation depth: Heath applies 5.4 directly to get G:K = H:L, while the AI breaks this down into 5.15 (parts have the same ratio as multiples) and 5.11 (transitivity of ratios) to reach the equivalent conclusion mA:mB = mD:mE. The AI also cites D5.17 (definition of ex aequali) for context. All ai_only items (5.11, 5.15, D5.17) represent finer-grained citation of the same underlying reasoning, and heath_only is empty, confirming this is a granularity difference rather than a path divergence.

### 5.23
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 determined the classification. Both proofs establish a perturbed proportion among equimultiples and then apply 5.21, but they reach the critical second ratio relationship by genuinely different methods. Heath uses alternation (5.16) on the hypothesis B:C = D:E to get B:D = C:E, then builds equimultiple ratios through repeated 5.15/5.11 applications. The AI instead applies 5.4 directly to B:C = D:E to obtain mB:nC = mD:nE in a single step. The proof-tree containment test confirms these are independent routes: 5.16 does not appear in Heath's proof of 5.4 (which uses 5.3 and D5.5). Since the backbone differs but the AI's path is logically sound under the hardened 1(b) standard, the classification is D.

### 5.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: (1) invert a given proportion, (2) apply ex aequali (5.22) to obtain a ratio between the first and fifth magnitudes, (3) apply componendo/separando (5.18) to compose the magnitudes, and (4) apply ex aequali (5.22) again to reach the final conclusion. The only difference is that the AI explicitly cites definitions D5.5 and D5.13 to justify the inversion step, whereas Heath performs the same inversion implicitly without citing these definitions. Since heath_only is empty and ai_only contains only definitions (not substantive propositions), this is a clear case of over-citation at different granularity with the same underlying logical structure.

### 5.25
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof constructs auxiliary segments AG=E and CH=F, then applies V.19 (remainder proportionality) to establish GB:HD :: AB:CD, from which GB > HD follows since AB > CD, and combines this with AG+F = CH+E to reach the conclusion. The AI instead uses alternando (5.16) and 5.14 to establish ordering relationships (C > D, B > D), then applies separando (5.17) followed by alternando and 5.14 again to establish A-B > C-D, and finally uses arithmetic (CN2, CN5) to conclude A+D > B+C. The key intermediate conclusions are fundamentally different: Heath pivots on remainder proportionality (5.19), while the AI pivots on the difference inequality A-B > C-D obtained through separando and alternando. The citation sets are completely disjoint (Jaccard = 0.0), confirming the different logical routes. Under Q3, the AI's chain is logically complete: each step validly applies its cited proposition, and the conclusion follows. Therefore the classification is D (path difference).


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
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: construct equimultiples of the bases by extending BD in both directions, use I.38 to show the equimultiple triangles equal the corresponding multiples of the original triangles, apply the three-way comparison (greater/equal/less) to satisfy V.Def.5 and conclude BC:CD = triangle ABC:triangle ACD, then use I.41 to show the parallelograms are double the triangles and V.15 to transfer the ratio. The ai_only items P1 and P2 are construction postulates (over-citation), and the heath_only item 5.11 (transitivity of ratios) is used verbally by the AI in Step 10 without explicit citation (under-citation). All key intermediate conclusions appear in both proofs at the same logical positions, making this a citation-depth difference rather than a path difference.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions in both the direct and converse parts: (1) triangles BDE and CDE are equal in area, (2) the ratios of triangles sharing a common height equal the ratios of their bases via VI.1, (3) V.7 links the equal triangles to equal ratios, (4) V.11 yields the proportionality conclusion, and for the converse, (5) V.9 recovers the triangle equality from equal ratios, and (6) I.39 gives the parallelism. The only citation differences are that the AI uses I.37 (same base) where Heath uses I.38 (equal bases) for the same geometric fact that BDE equals CDE, and the AI explicitly cites Postulate 1 for joining lines while Heath does not. Since I.37 and I.38 license the same conclusion in this context (the triangles share the literal same base DE), this is an alternative citation at the same logical position, not a different path. The extra P1 citation is standard over-citation of a construction postulate. Both backbones are identical, so this is Case A of Q2.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification. Both proofs (AI and Heath) establish the same key intermediate conclusions in both directions of the biconditional: constructing CE parallel to DA, establishing angle equalities via I.29, deriving AE = AC via I.6 (forward) or I.5 (converse), applying VI.2 for the proportion, and using V.9/V.11/V.7 for ratio arithmetic. The backbones are identical. The ai_only set consists entirely of over-citations: I.31 (construction of parallel line that Heath leaves implicit), V.7 (explicit ratio substitution that Heath performs without citation), CN1 (common notion cited explicitly), P2 and P5 (postulates for extending lines and guaranteeing intersection). Heath_only is empty, confirming that the AI cites everything Heath does plus additional construction-level and axiomatic references. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 6.4
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 determined the classification. Heath constructs an external figure by placing BC in a straight line with CE, extending BA and ED to meet at F, forming parallelogram FACD, and then applying VI.2 to the larger triangle FBE with substitutions from the parallelogram equalities, using V.16 (alternando) and V.22 (ex aequali) for proportion manipulation. The AI takes a fundamentally different approach: it constructs an internal congruent copy of the smaller triangle inside the larger by cutting off BG = EF on BC (I.3), drawing GH parallel to AC (I.31), proving triangle BGH congruent to triangle DEF via I.26 (ASA), then using 5.7 (invertendo), 5.18 (componendo), and 5.11 (transitivity of ratios) to establish the three-way proportion. The geometric constructions are entirely different (external extension vs. internal congruent copy), the key intermediate conclusions differ (parallelogram FACD with FA=DC, AC=FD vs. congruence BGH=DEF with BH=DE, GH=DF and parallelogram GHKC), and the proportion tools differ (V.16+V.22 vs. 5.7+5.18+5.11). The only shared citations are 1.34 and 6.2. The AI proof is logically complete and valid throughout, constituting a genuine path difference.

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct an auxiliary triangle equiangular to ABC on a side of triangle DEF (Heath constructs GEF on EF; the AI constructs DEG on DE), use VI.4 to get proportional sides, then use V.11 and V.9 to establish equal sides, and finally use triangle congruence (I.8/I.4) to transfer angle equalities. The only citation difference is that Heath explicitly cites both I.8 (SSS for the included angle) and I.4 (SAS for full congruence and remaining angles), while the AI cites only I.8 and attributes all angle equalities to it. This is a citation-depth difference, not a logical gap: the AI has established all three side equalities and compresses the two-step I.8-then-I.4 inference into one citation. The missing I.4 is an expansion of a supported step. Since the backbones match and the sole heath_only item (1.4) represents under-citation rather than a different logical path, this is Granularity difference (G).

### 6.6
**Category**: Path difference
**Jaccard**: 0.231
**Analysis**: Q2 determined this classification. Heath constructs an auxiliary triangle DGF that is equiangular to ABC by copying angles with I.23, then uses VI.4 to derive proportional sides, deduces ED=GD via V.9, and applies SAS (I.4) to show triangle DEF congruent to DGF. The AI instead constructs an auxiliary triangle DGH congruent to ABC by cutting off segments DG=AB and DH=AC and applying SAS (I.4), then uses proportional reasoning (5.16, 5.19, 5.11) to establish DG:GE = DH:HF, invokes the converse of 6.2 to conclude GH is parallel to EF, and applies I.29 to transfer angles. The key intermediate conclusions differ fundamentally: Heath's backbone runs through equiangular-auxiliary-triangle to proportional-sides to side-equality to SAS, while the AI's backbone runs through congruent-auxiliary-triangle to proportional-side-cuts to parallelism to equal-alternate-angles. The AI's different path is logically complete with every step properly cited and all cases addressed, satisfying Q3, yielding category D.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: indirect proof assuming angle ABC is not equal to angle DEF, constructing angle ABG equal to angle DEF via I.23, showing triangles ABG and DEF are equiangular via I.32, deriving BG = BC via proportions and V.9, using the isosceles triangle property I.5, and reaching contradictions in both cases. The differences are in citation depth rather than key conclusions. The AI avoids V.11 by arranging the given proportions as AB:DE = BC:EF rather than AB:BC = DE:EF, so the 6.4 result AB:DE = BG:EF lines up directly without needing transitivity. In Case 2, the AI uses a longer route through angle-sum arguments (I.32) instead of Heath's direct appeal to I.17, but both reach the same structural contradiction from BG = BC. The ai_only item P1 is a postulate (over-citation consistent with G). The heath_only items (1.17 used in Case 2, 5.11 used for ratio transitivity) reflect the AI taking slightly different but equivalent sub-paths to reach the same key intermediate conclusions.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs establish the same three key intermediate conclusions: (1) triangle ABD is similar to whole triangle ABC via equiangularity, (2) triangle ADC is similar to whole triangle ABC via equiangularity, and (3) triangles ABD and ADC are similar to each other. The logical backbone is identical in both proofs. The AI's citation set is a strict superset of Heath's: heath_only is empty, while ai_only consists entirely of foundational items (CN1, CN3, D1.10, P4) that Heath uses implicitly without explicit citation. The AI explicitly cites Postulate 4 for the equality of right angles, Definition 1.10 for the perpendicular construction, and Common Notions 1 and 3 for equality reasoning that Heath leaves tacit. This is a classic over-citation pattern representing different citation depth on the same logical path.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs follow the same backbone: construct equal segments on a line from A at an angle to AB, join the far endpoint to B, draw a parallel through an intermediate point to apply VI.2/6.2, obtain a proportion, and conclude the prescribed part has been cut off. Heath's proof and the AI proof establish identical key intermediate conclusions: the ratio between segments on the auxiliary line equals the ratio between segments on AB (via the parallel and VI.2/6.2), and the prescribed fraction results. The AI's additional citations (5.18 for componendo, CN1, CN2, D5.5 for definitions and common notions, P1 for drawing lines) are all over-citations that formalize steps Heath handles informally. Heath_only is empty, confirming the AI covers all of Heath's reasoning. This is Case A: same backbone, different citation depth.

### 6.10
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 determined the classification. Both proofs solve the construction problem of cutting a line similarly to a given cut line, and both use VI.2 as a core tool, but through fundamentally different geometric constructions. Heath constructs parallelograms (using I.31 and I.34) to establish segment equalities (DH=FG, HK=GB), then applies VI.2 in the resulting triangles and substitutes equals directly. The AI instead transfers the segment lengths onto a new line using I.2, joins endpoints, draws parallels to the joining line (I.31, I.30), applies VI.2 in the resulting triangles, and then derives the required proportions through ratio algebra (componendo via 5.18, alternando via 5.16, and transitivity via CN1). The key intermediate conclusions differ: Heath's backbone relies on parallelogram segment equalities (I.34) while the AI's backbone relies on ratio manipulation (5.16, 5.18). Since the backbones differ (Case B in Q2), Q3 was applied, and the AI's different path is logically complete and valid, yielding classification D.

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct BD equal to AC, draw DE parallel to BC, apply VI.2/6.2 to obtain AB:BD = AC:CE, then substitute BD = AC to conclude AB:AC = AC:CE. The AI proof cites four additional items not in Heath (5.7, CN1, P1, P2), all of which are over-citations of steps Heath performs implicitly. Proposition 5.7 explicitly justifies that equal magnitudes have the same ratio, which Heath handles by simple substitution. CN1 makes the equality-of-ratios combination explicit. P1 and P2 are postulate-level construction steps (joining and extending lines) that Heath leaves tacit. Heath cites nothing the AI omits (heath_only is empty). Since the key intermediate conclusions are identical and the citation differences are purely a matter of depth, this is Case A of Q2: same backbone, different citation depth, yielding a Granularity difference (G).

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the identical backbone: construct triangle DEF with DG=A, GE=B, DH=C on its sides, draw EF through E parallel to GH, apply VI.2 to obtain DG:GE = DH:HF, then substitute to get A:B = C:HF. The ai_only set {1.3, P1, CN1, D5.6} consists entirely of construction propositions (1.3 for cutting off equal segments), postulates (P1 for drawing lines), common notions (CN1 for substitution), and definitions (D5.6 for proportion) that Heath uses implicitly without citation. The heath_only set is empty. Since the key intermediate conclusions are the same and the citation differences are purely a matter of explicit versus implicit citation of foundational tools, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs follow the same backbone: place AB, BC in a straight line, describe a semicircle on AC, draw BD perpendicular to AC, establish that angle ADC is right by III.31, and conclude that DB is a mean proportional between AB and BC via VI.8. The AI proof adds explicit construction citations (P1, P2, P3, 1.10, 1.11), definitions (D1.17, D1.18, D5.8, D6.1), and 6.4 (proportionality of sides of similar triangles). The proof-tree containment test confirms that 6.4 appears inside Heath's proof of 6.8, so the AI is simply making explicit a sub-step that Heath invokes implicitly through 6.8. The heath_only set is empty, meaning Heath cites nothing the AI does not. All ai_only items are postulates, definitions, construction lemmas, or a sub-result contained within 6.8, confirming this is a citation-depth difference rather than a path difference.

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish reciprocal proportionality of sides by expressing each original parallelogram's area ratio to a reference parallelogram in terms of side ratios using 6.1, connecting these via the given equality of the parallelograms, and concluding with 5.11; the converse reverses the argument using 5.9. The AI uses a more elaborate construction (citing 1.13, 1.30, 1.31, 1.34 for setup steps that Heath's simpler arrangement avoids), and the AI omits citing 5.7 which Heath uses to formally justify that equal magnitudes have the same ratio to the same magnitude, though the AI uses this fact implicitly in Step 9. The ai_only items are all Book 1 construction propositions reflecting the AI's different geometric setup, and the heath_only item 5.7 is used implicitly by the AI without citation. These are citation-depth differences around the same key intermediate conclusions, not backbone differences.

### 6.15
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions for both the forward direction and the converse: they place the triangles so that CA and AD are collinear and BA and AE are collinear, join BD, use VI.1 twice to express triangle ratios as base ratios, apply V.7 (equal magnitudes have the same ratio to the same) and V.11 (transitivity of proportions), and for the converse use V.9 (same ratio to the same implies equality). The AI proof adds 1.13 for a more explicit justification of the collinearity step (Heath cites only I.14), cites P1 for joining BD (Heath omits the postulate citation), and uses 5.16 (alternando) to rearrange the final proportion into the desired form. All three ai_only items (1.13, 5.16, P1) represent additional citation depth rather than a different logical path. heath_only is empty, confirming that the AI covers all of Heath's reasoning. This is Case A: same backbone, different citation depth.

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct equiangular parallelograms (rectangles) whose sides equal the given line segments, then apply Proposition 6.14 in both directions to establish the biconditional. The AI proof covers both the forward direction (Steps 1-6) and the converse (Steps 7-9), matching Heath's two-part structure. The only difference is citation depth: the AI explicitly cites construction propositions (1.3, 1.11, 1.31, 1.34), Postulate 1, and Definition 6.2 for steps that Heath performs without explicit citation. The heath_only set is empty, confirming that the AI omits nothing Heath uses. The ai_only set consists entirely of construction tools, a postulate, and a definition, which are over-citations of elementary construction steps. This is a classic Case A granularity difference.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: viewing three proportional lines A, B, C as four proportional lines (A, B, B, C in the AI; A, B, D, C with D=B in Heath), applying 6.16 to equate the rectangle of the extremes with the rectangle of the means, and then identifying the rectangle of the means with the square on B. The converse follows the same pattern in both proofs. The only difference is that Heath explicitly constructs an auxiliary line D equal to B and substitutes, while the AI directly treats B, B as the two mean terms. The AI additionally cites definitions D1.22 and D2.1 to justify that rect(B,B) = sq(B), which Heath treats as self-evident from B = D. Since the ai_only items are purely definitional over-citations and heath_only is empty, this is a same-backbone, different-depth situation classifying as G.

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same backbone: decompose the given rectilinear figure into triangles, construct equiangular triangles on the given line using I.23, establish equiangularity via I.32, derive proportionality of corresponding sides via VI.4/6.4, chain the proportions across triangle pairs, and conclude similarity via VI.Def.1/D6.1. The AI's extra citations (5.11 for transitivity of ratios, CN2 for angle addition, CN3 for the remaining-angle deduction, and P1 for joining lines) are all explicit citations of steps that Heath performs implicitly without naming the underlying result. The heath_only set is empty, confirming no missing steps in the AI proof. This is a clear Case A under Q2: same key intermediate conclusions at every logical position, with the AI citing at a finer granularity than Heath.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct a third proportional BG to BC and EF via 6.11, establish that AB:DE = EF:BG, apply 6.15 to show triangle ABG equals triangle DEF, use D5.9 for the duplicate ratio of BC to BG, apply 6.1 for the ratio of triangles ABC and ABG, and substitute to reach the conclusion. The differences are purely in citation granularity: Heath uses 5.16 (alternation) to rearrange AB:BC = DE:EF into AB:DE = BC:EF before combining with 5.11, while the AI reads BC:EF = AB:DE directly from the similarity definition D6.1, bypassing the need for alternation. The AI also explicitly cites 5.7 (equal magnitudes have the same ratio) for the substitution of triangle DEF for the equal triangle ABG, a step Heath performs without explicit citation. Heath cites D5.11 (corresponding magnitudes) where the AI cites D6.1 (similar figures definition), both definitional references. All key intermediate conclusions are identical in both proofs.

### 6.20
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Both proofs share the same first part: triangulating the similar polygons and proving the component triangles are similar (using 6.6, 6.4, 5.22, D6.1). However, for the second part (proving the component triangles are proportional and the polygon ratio is duplicate of the side ratio), the proofs follow genuinely different backbones. Heath draws auxiliary diagonals AC and FH, identifies intersection points M and N, proves auxiliary triangles equiangular using 1.32, and then uses 6.1 (triangles under the same height are as their bases) to establish the proportionality chain. The AI instead leverages 6.19 directly on each pair of similar triangles to obtain duplicate ratios of shared corresponding sides (BE:GL for the first two pairs, EC:LH for the second two), then uses 5.11 (transitivity of ratio equality) to chain them together. This is a valid alternative path that reaches the same final conclusion through different key intermediate reasoning, making Q2 Case B. The AI's path is logically complete (Q3b holds), so the classification is D.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: unpack the two given similarities (A~C and B~C) using Definition 6.1 to obtain equiangularity and proportional sides with C, then conclude that A is similar to B. Heath's proof reaches the conclusion directly and tersely from these two similarity statements, citing only D6.1. The AI proof spells out the intermediate deductions more explicitly, using CN1 to show that angles of A equal angles of B (since both equal the same angles of C), and using 5.16 (inverse proportion) and 5.22 (ex aequali) to chain the proportional sides from A:C and C:B into A:B. These ai_only citations (CN1, 5.16, 5.22) provide granular justification for steps Heath considers self-evident, but both proofs establish the same key intermediate conclusions at the same logical positions. Heath_only is empty, confirming the AI covers all of Heath's reasoning and simply adds depth.

### 6.22
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same two-part structure for this biconditional: (Part 1) construct third proportionals via 6.11, apply ex aequali via 5.22, relate the ratio of similar figures to the ratio of lines to their third proportionals, and conclude by transitivity via 5.11; (Part 2) construct a line in the same ratio via 6.12, build a similar figure on it via 6.18, apply Part 1, use 5.11 and 5.9 to deduce equality of figures and hence of sides. The key intermediate conclusions match exactly in both order and substance. The only substantive citation difference is that Heath uses 6.19 (similar triangles in duplicate ratio) while the AI uses 6.20 (similar polygons in duplicate ratio). Since 6.19 is cited within Heath's own proof of 6.20, the proof-tree containment test confirms this is a citation-depth difference: the AI cites the higher-level result 6.20 as a unit, while Heath effectively re-derives its content via the more specific 6.19. The AI's additional citations of CN1 and D5.9 are axiom/definition-level over-citations consistent with a granularity difference.

### 6.23
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determines the classification. Heath's proof constructs auxiliary magnitudes K, L, M using 6.12, sets up K:L = BC:CG and L:M = DC:CE, then uses 5.11 (ratio transitivity) to link these auxiliary ratios to the parallelogram ratios AC:CH and CH:CF established by 6.1, before applying ex aequali to conclude K:M = AC:CF. The AI proof takes a fundamentally different path: it directly uses the intermediate parallelogram DCGH as the bridge, applying 6.1 twice to get ABCD:DCGH = BC:CG and DCGH:CEFG = DC:CE, then invokes the definition of compounded ratio (D6.5) and ex aequali (5.22) to conclude immediately. The AI avoids the auxiliary construction (6.12) and ratio transitivity (5.11) entirely, yielding a different backbone. The AI also explicitly justifies the collinearity of DC and CE via 1.13 and 1.14, which Heath states without citation. The AI's path is logically sound and complete, establishing the conclusion through valid but different key intermediate conclusions.

### 6.24
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 reveals genuinely different backbones, leading to classification D at Q3. Heath establishes proportionality of sides about the common angle by applying VI.2 to get BE:EA = CF:FA and CF:FA = DG:GA, then using V.18 (componendo) and V.16 (alternando) to derive BA:AD = EA:AG, and finally V.22 (ex aequali) for the remaining proportion DC:CB = GF:FE. The AI takes a fundamentally different route: it applies VI.2 directly to get AE/AB = AF/AC and AG/AD = AF/AC, then uses CN1 (transitivity) to conclude AE/AB = AG/AD, avoiding all Book V proportion-manipulation theorems. The AI establishes equiangularity through I.29 (alternate angles from parallels) and I.34 (opposite angles in parallelograms) rather than through triangle equiangularity, and uses I.34 (opposite sides equal) to substitute sides and establish all needed proportions without ex aequali. The heath_only set (5.16, 5.18, 5.22) represents the proportion-manipulation machinery that the AI replaces entirely with parallelogram properties (1.29, 1.34, CN1). This is not a depth difference but a genuinely different logical path. The AI's path is logically complete and sound, so Q3 yields D.

### 6.25
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: construct parallelograms BE equal to ABC and CM equal to D, find a mean proportional GH between BC and CF, describe figure KGH similar to ABC on GH, establish that BC:CF equals both the ratio of the similar figures and the ratio of the parallelograms, then conclude KGH equals D. The heath_only citations (1.44, 5.16, 6.19) reflect citation-depth differences rather than backbone divergence. Heath cites 1.44 for the first parallelogram application while the AI uses the more general 1.45 for both; Heath cites 6.19 (duplicate ratio for similar triangles) while the AI cites 6.20 (duplicate ratio for similar polygons), and 6.19 appears inside Heath's proof of 6.20, satisfying the proof-tree containment test; Heath uses V.16 (alternation) for the final deduction while the AI uses 5.9 (equal ratios to same imply equality), which is a minor variation in the concluding step but does not alter the key intermediate conclusions. The ai_only items (D5.9, D6.1, CN1) are definitions and common notions representing over-citation typical of granularity differences.

### 6.26
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: assume the smaller parallelogram is not about the same diameter, construct a parallelogram about the assumed diameter using I.31, apply VI.24 to establish similarity of the constructed parallelogram with the whole, use the given similarity hypothesis to derive that two unequal segments must be equal (AE = AK), and reach a contradiction. Heath's proof is concise, using V.11 and V.9 directly to collapse the proportion GA:AK = GA:AE into AE = AK. The AI proof is far more verbose (30 steps) but reaches the same key intermediate conclusions through additional elaboration: it explicitly invokes 6.21 for transitivity of similarity, 5.16 for alternation of proportions, 6.16 for rectangles of proportionals, 6.20 for duplicate ratios of areas, and foundational items (CN1, CN5, D6.1, P1). All of these are over-citations that expand on steps Heath leaves implicit. Since heath_only is empty (the AI cites every proposition Heath does), and the additional AI citations represent deeper elaboration of the same argument rather than a different path, this is a same-backbone, different-depth case.

### 6.27
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the use of 6.26 (similar parallelograms about the same diameter) and 1.43 (equality of complements), but they diverge in key intermediate conclusions. Heath establishes specific equalities (CF=FE via I.43, CH=CG via I.36 since AC=CB) and performs algebraic manipulation to show AF equals the gnomon LMN, concluding AD > AF. The AI instead uses a case-based geometric decomposition argument (E between A and C, or E between C and B), reasoning about containment of parallelograms about the diameter and how the gnomon difference arises structurally, concluding via CN5 that the whole is greater than the part. Heath's use of I.36 (parallelograms on equal bases between same parallels are equal) is a substantive step absent from the AI proof, and the AI's case-analysis approach with explicit decomposition reasoning is absent from Heath. Since the backbones differ and the AI's path is logically valid under Q3, this is classified as D.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: bisect AB at E, construct a parallelogram EBFG similar to D on the half-line (6.18), handle the trivial case, construct a parallelogram equal to the excess and similar to D (6.25), show it is similar to EBFG (6.21), place it about the same diameter (6.26), identify the gnomon as equal to C by subtraction, and then show the gnomon corresponds to the applied parallelogram on AB with the defect similar to D. The ai_only citations 1.10 (bisection) and CN3 (subtraction) are explicit over-citations of construction and common notion steps that Heath performs implicitly. The AI uses 1.43 (complements about the diameter are equal) and 6.24 (parallelograms about a diameter are similar to the whole) where Heath uses 1.36 (parallelograms on equal bases in same parallels are equal), but both serve the same purpose: establishing that the relevant parallelogram regions are equal and that the defect is similar to D. The key intermediate conclusions are identical in both proofs; only the citation depth differs.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect AB at E, describe a parallelogram on EB similar to D, construct a larger parallelogram equal to the sum of that parallelogram and C using VI.25, show the two parallelograms share a diameter (VI.21, VI.26), show the gnomon equals C, use AE=EB with I.36 and I.43 to equate the applied parallelogram with the gnomon (hence with C), and show the excess is similar to D via VI.24. Every key intermediate conclusion in Heath's proof appears in the AI proof at the same logical position. The ai_only set consists entirely of construction propositions (1.10, 6.18, 1.45), postulates (P1, P2), common notions (CN3, CN5), and a definition (D6.1), all of which are auxiliary references that Heath treats as implicit. The heath_only set is empty. This is a clear Case A: same backbone with different citation depth, yielding Granularity difference (G).

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determines the classification. Heath's proof constructs a square on AB, applies a parallelogram equal to it exceeding by a similar figure (6.29), then uses reciprocal proportionality of equiangular parallelograms (6.14) to derive BA:AE = AE:EB. The AI takes a fundamentally different path: it invokes 2.11 to cut AB so that rect(AB,CB) = sq(AC), then applies 6.17 (the converse: if the rectangle of the extremes equals the square on the mean, the three lines are proportional) to conclude AB:AC = AC:CB, which is the definition of extreme and mean ratio (D6.3). The citation sets are completely disjoint (Jaccard = 0.0), and the proof-tree containment test confirms that Heath's citations (6.14, 6.29) do not appear inside the proof trees of the AI's citations (2.11, 6.17). Both proofs are logically complete but argue through entirely different intermediate conclusions, making this a genuine path difference.

### 6.31
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same backbone: draw AD perpendicular from the right angle to the hypotenuse BC, invoke 6.8 to obtain similar triangles, extract the proportion BC:BA = BA:BD from similarity, establish that the ratio of figures on BC and BA equals the ratio BC:BD, apply the same reasoning to the other side, and conclude from BD+DC=BC that the figure on BC equals the sum of the similar figures on BA and CA. The key difference is citation depth: Heath cites 6.19 directly (similar triangles are in duplicate ratio of corresponding sides) to link the figure ratio to the segment ratio, while the AI cites the more general 6.20 (similar polygons in duplicate ratio) and also explicitly invokes D5.9 (definition of duplicate ratio) to build the same link in more detail. The proof-tree containment test confirms that 6.19 appears inside Heath's proof of 6.20, so the AI citing 6.20 instead of 6.19 is a citation-depth difference, not a path difference. The AI also makes explicit the proportion algebra that Heath leaves implicit, citing 5.7 (invertendo), 5.24 (combining ratios), and 5.9 (equality from equal ratios), all of which are valid steps that Heath compresses. D6.1 in heath_only is a definition used to extract proportions from similarity, which the AI handles via the theorem 6.4 instead. These are all granularity differences with the same underlying logical backbone.

### 6.32
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Both proofs follow the same logical backbone: (1) use I.29 to establish equal alternate angles from parallel lines, (2) apply VI.6 to conclude the two triangles are equiangular, (3) show that adjacent angles at the shared vertex C sum to two right angles, and (4) conclude collinearity of the remaining sides via I.14. The AI sets up a different (but equivalent) configuration, proving CA and CD collinear rather than BC and CE as in Heath, but the key intermediate conclusions are structurally identical. The citation difference is purely one of depth: Heath cites I.32 (angle sum of a triangle equals two right angles) to establish the supplementary angle relationship, while the AI cites I.13 (supplementary angles on a straight line) directly — and I.32's own proof relies on I.13, confirming this is a citation-depth difference rather than a different path. The AI's additional citation of CN1 for an explicit substitution step is standard over-citation. Q2 Case A applies: same backbone, different citation depth, yielding G.

### 6.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G. Both proofs follow the same logical backbone: they construct equimultiples of circumferences and central angles, verify the three conditions of the equimultiple criterion (V. Def. 5), and then extend the result from central angles to inscribed angles. The AI proof cites the same propositions as Heath (3.27 and D5.5) plus additional ones (1.23 for angle construction, 3.26 as the converse of 3.27, 3.20 for the inscribed-angle-is-half-central-angle fact, 5.15 for ratio transfer to halves, and D3.1). Since heath_only is empty, every step Heath cites is also cited by the AI. The ai_only items represent greater citation explicitness for steps that Heath handles implicitly or without formal citation, making this a same-backbone, different-depth case.


## Book 7

| Category | Count |
|---|---|
| Perfect match (P) | 1 |
| Granularity difference (G) | 27 |
| Path difference (D) | 11 |
| AI proof error (E) | 0 |

**Total**: 39 propositions

### 7.1
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume for contradiction that a number greater than one measures both given numbers, trace the common measure through every remainder of the Euclidean algorithm (successive subtraction), reach the conclusion that it must measure the final unit remainder, and derive a contradiction since a number greater than one cannot measure a unit. The AI proof cites seven additional foundational items (CN3, CN5, D7.1, D7.14, D7.15, D7.3, D7.5) that are all definitions and common notions -- precisely the kind of implicit background that Heath uses without explicit citation. With heath_only empty and all ai_only items being axioms/definitions rather than substantive theorems, this is a clear Case A (same backbone, different citation depth), yielding Granularity difference.

### 7.2
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone of the Euclidean algorithm: (1) trivial case where CD measures AB, (2) successive subtraction (antenaresis) that terminates because reaching a unit would contradict the hypothesis via 7.1, (3) the last remainder is shown to be a common measure by chaining divisibility up through the algorithm, and (4) it is shown to be the greatest common measure by proving any larger common measure would have to measure the last remainder (a contradiction). The AI and Heath establish the same key intermediate conclusions in the same logical order. The only difference is citation depth: the AI explicitly cites CN3, CN5, D7.12, and D7.2 (common notions and definitions) that Heath invokes implicitly without citation. Since heath_only is empty and ai_only consists entirely of definitions and common notions, this is a clear Case A granularity difference.

### 7.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: find D = gcd(A,B) via 7.2, then split into two cases depending on whether D measures C. In Case 1, D is shown to be the gcd by proving every common measure divides D. In Case 2, D and C are shown not to be coprime, E = gcd(D,C) is found via 7.2, E is shown to measure A,B,C, and every common measure is shown to divide E. The key intermediate conclusions are identical in both proofs. The only citation difference is that the AI explicitly cites D7.12 (definition of numbers prime to one another) where Heath uses the concept without citing the definition. Since D7.12 is a definition and the backbones match, this is a citation-depth difference, yielding G.

### 7.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof is constructive: it splits into cases based on whether the numbers are prime to one another, and in the non-trivial case uses VII.2 to find the GCD, then divides the smaller number into segments equal to the GCD to show each segment is a part of the greater. The AI proof takes a fundamentally different, purely definitional approach: it splits on whether A measures B or not, then directly invokes Definition 7.3 (a number is a part when it measures the greater) and Definition 7.4 (a number is parts when it does not measure the greater) to conclude that A is either a part or parts of B. The key intermediate conclusions differ entirely — Heath constructs the decomposition explicitly while the AI appeals directly to definitions with no construction. Under Q1(b) the AI proof is logically valid since D7.3 and D7.4 directly license the two cases, making this a different but valid path (D) rather than an error.

### 7.5
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification as Granularity difference (G). Both proofs establish the same key intermediate conclusions: they identify that A measures B some number n of times, that C measures D the same n times, and then show that A+C measures B+D exactly n times. Heath uses a constructive decomposition (dividing BC into parts BG, GC equal to A and EF into parts EH, HF equal to D, then pairing corresponding parts), while the AI uses algebraic notation (B = n*A, D = n*C, adding to get B+D = n*(A+C)). The logical backbone is identical. Heath cites no external references at all, while the AI explicitly cites definitions D7.3, D7.5, D7.15 and Common Notion CN2 that Heath uses implicitly. All ai_only items are definitions or common notions, and heath_only is empty, confirming this is a citation-depth difference rather than a path difference.

### 7.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: divide AB into parts AG, GB of C and DE into parts DH, HE of F; apply Proposition 7.5 to each corresponding pair (AG with DH, GB with HE) to show each sum is the same part of C+F; then reassemble to conclude AB+DE is the same parts of C+F that AB is of C. The only difference is that the AI explicitly cites definitions D7.3 and D7.4 to justify the decomposition into parts, while Heath leaves this implicit. Since the ai_only items are definitions (non-substantive) and heath_only is empty, this is a pure citation-depth difference with the same backbone, yielding Granularity difference (G).

### 7.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary number CG such that EB is the same part of CG as AE is of CF, then applies Proposition 7.5 (summation of parts) to conclude AB is that part of GF, equates GF with CD, and substitutes back. The AI proof takes a fundamentally different route: it expresses the 'part' relationship as 1/n using Definitions 7.3 and 7.5, decomposes BC into n copies of A and E into n copies of D, then subtracts pairwise using Common Notion 3 to show BC minus E equals n copies of (A minus D), concluding directly from the definition of 'part'. These represent genuinely different logical backbones -- Heath relies on the additive lemma 7.5 with an auxiliary construction, while the AI uses direct decomposition and pairwise subtraction without any auxiliary number or appeal to 7.5. The AI's path is logically complete and valid (Q3 satisfied), making this a path difference.

### 7.8
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: divide the whole and subtracted numbers into equal numbers of parts, apply Proposition 7.7 twice to show each partial remainder is the same part of the total remainder as the corresponding whole part is of the whole, then combine the partial remainders. The AI proof explicitly cites definitions D7.3 and D7.4 to justify the decomposition into parts, while Heath uses these definitions implicitly without citation. Since the ai_only items are purely definitional (D7.3, D7.4) and heath_only is empty, this is a clear Case A in Q2: same backbone with different citation depth, yielding a Granularity difference.

### 7.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: decompose the first number into n copies of a unit part and the second number into n copies of a corresponding unit part, note the multitudes are equal, then apply VII.5 (for the 'part' case) and VII.6 (for the 'parts' case) to combine the sums and conclude that the totals bear the same part/parts relation. The AI proof adds explicit definitional citations (D7.3, D7.4, D7.5, D7.20) that Heath treats as understood, but these are all definitions providing justification for steps present in both proofs. Since heath_only is empty and ai_only contains only definitions, this is a clear case of over-citation at the definitional level with no backbone divergence.

### 7.10
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: divide AB into parts AG, GB of C and DE into parts DH, HE of F; note equal multitude; apply 7.9 to each pair (AG/DH and GB/HE) to establish the alternation for each component part; then combine via 7.5 and 7.6 to reach the conclusion for the whole. The only difference is that the AI additionally cites definitions D7.3 and D7.4, which are implicit in Heath's proof but explicitly referenced by the AI. Since these are definitional citations (not substantive propositions) and the logical backbone is identical, this is a citation-depth difference under Q2 Case A, yielding G.

### 7.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) translate the given proportion AB:CD = AE:CF into part/parts language via D7.20, (2) apply 7.7 and 7.8 to conclude the remainder EB is the same part/parts of FD that AB is of CD, and (3) convert back to proportional language via D7.20. The AI proof makes the case split between 'part' and 'parts' explicit by citing 7.4 (any number is either a part or parts of another), D7.3 (definition of part), and D7.4 (definition of parts), while Heath handles the same dichotomy implicitly in a single sentence ('whatever part or parts'). Since the key intermediate conclusions are identical and the ai_only citations (7.4, D7.3, D7.4) merely provide explicit definitional grounding for a step Heath treats as obvious, this is a same-backbone, different-depth scenario — Case A in Q2 — yielding classification G.

### 7.12
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that numbers in proportion have the same part-or-parts relationship (via D7.20), then use 7.5 and 7.6 to show the sums preserve this relationship, and conclude by D7.20 that the ratio of the sums equals the original ratio. The only difference is that the AI explicitly cites 7.4 to justify the case split into 'part' versus 'parts', whereas Heath handles this implicitly with the phrase 'whatever part or parts.' This is a citation-depth difference, not a structural divergence in the proof strategy, so it falls under Case A of Q2.

### 7.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same key intermediate conclusion: from the proportionality A:B :: C:D (unpacked via D7.20), they derive the alternated relation A:C :: B:D by applying the alternation results (7.9/7.10) and then re-invoking D7.20. Heath gives a single-chain argument citing only 7.10 for the alternation step, using the phrase 'part or parts' to cover all sub-cases at once. The AI splits into three explicit cases (part, parts, multiple) and applies 7.9 for the 'part' case and 7.10 for the 'parts' case, with Case III reducing the 'multiple' case to a 'part' case via D7.5 and D7.3 before applying 7.9. The backbone is the same in both proofs; the AI simply provides more fine-grained case analysis and cites additional propositions and definitions (7.9, D7.3, D7.5) that Heath subsumes under a single invocation of 7.10. Since heath_only is empty and ai_only consists of over-citations providing extra granularity, this is a citation-depth difference fitting Case A of Q2.

### 7.14
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone for the core three-number case: alternation (7.13) applied to each given ratio to obtain A:D = B:E and B:E = C:F, then chaining these to get A:D = C:F, and a final alternation to conclude A:C = D:F. The AI proof matches all four of Heath's key intermediate conclusions in the same logical order. The ai_only items (CN1, D5.17, D7.20) are a common notion and two definitions, representing over-citation of foundational items that Heath uses implicitly. The AI also adds an explicit inductive argument (Steps 7-10) generalizing from three numbers to n numbers, which Heath leaves implicit. Since the backbones are identical and the differences are purely in citation depth and explicitness of the general case, this is a granularity difference.

### 7.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 7.15 by decomposing BC into its constituent units and EF into copies of D, then applying 7.12 (as one antecedent is to one consequent, so are all antecedents to all consequents) to directly establish A:D = BC:EF. The AI takes a fundamentally different route: it uses definitions (D7.3, D7.20) to first establish the proportion A:BC = D:EF (since both A and D are n-th parts of their respective numbers), then applies 7.13 (alternate proportion) to derive A:D = BC:EF. The key intermediate conclusions differ: Heath's backbone passes through unit-decomposition and sum-of-ratios (7.12), while the AI's backbone passes through a direct proportionality A:BC = D:EF and alternation (7.13). The proof-tree containment test confirms this is a genuine path difference, since 7.12 does not appear in the proof of 7.13. The AI's path is logically complete and valid, so the classification is D.

### 7.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: (1) from A*B=C, the unit measures A the same number of times B measures C; (2) by alternation via 7.15, the unit measures B the same number of times A measures C; (3) from B*A=D, the unit measures B the same number of times A measures D; (4) combining, A measures both C and D the same number of times, so C=D. The only difference is that the AI explicitly cites D7.15 (the definition of multiplication) to justify the measurement relationships arising from multiplication, while Heath applies the same concept implicitly without a formal citation. This is a citation-depth difference with identical logical backbones, yielding Case A of Q2 and classification G.

### 7.17
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof works by establishing that the unit F is to A as B is to D (and likewise as C is to E) via D7.20, then concludes B:D = C:E and applies alternation (7.13) to get B:C = D:E. The AI proof takes a fundamentally different route: it interprets multiplication as repeated addition via D7.15, recognizes that D is A copies of B and E is A copies of C, then applies 7.12 (the ratio of one antecedent to one consequent equals the ratio of all antecedents to all consequents) to conclude B:C = D:E directly without needing alternation. The key intermediates differ -- Heath pivots on the unit-to-multiplier ratio (F:A = B:D = C:E), while the AI pivots on the repeated-sum structure and the summing-of-proportionals property. Both paths are logically complete, making this a genuine path difference.

### 7.18
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs follow identical logical backbones: (1) establish via 7.16 that A times C equals C times A and B times C equals C times B, swapping the order of multiplication; (2) apply 7.17 to conclude that since C multiplying A produces D and C multiplying B produces E, the ratio D:E equals A:B. The AI's only additional citations are definitions D7.15 (definition of multiplication) and D7.20 (definition of proportionality), which Heath leaves implicit. Since the key intermediate conclusions are the same and the citation difference consists entirely of definitions the AI made explicit, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 7.19
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 determined the classification. Both proofs establish the biconditional (A:B::C:D iff A*D=B*C) and both cite 7.17 and 7.18, but they argue through different key intermediate conclusions. Heath introduces an auxiliary product G=A*C and reasons through ratios involving G, using Book 5 results (5.9 to infer equality from same ratio to the same, and 5.7 to infer same ratio from equal magnitudes). The AI instead uses B*D as a common denominator, shows both A*D and B*C bear the same ratio to B*D, and infers equality directly via Definition 7.20. In the converse, Heath again uses G and 5.7, while the AI substitutes A*D for B*C directly. These are genuinely different logical backbones rather than the same argument at different granularity levels, so the classification is D.

### 7.20
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Heath's proof argues by assuming CD is 'parts' (not a single part) of A, divides CD and EF into equal sub-parts, then uses 7.12 (antecedents to consequents) to show these sub-parts form a smaller pair in the same ratio, contradicting minimality, and concludes via 7.4 that CD is a part of A. The AI proof takes a fundamentally different approach: it uses the division algorithm to write A = qC + R, employs 7.19 (cross-multiplication) to establish CB = DA, then algebraically derives that R and S = B - qD satisfy R:S = C:D via 7.19 converse and 7.13, with R < C and S < D, again contradicting minimality. The key intermediate conclusions differ — Heath works through the 'parts' concept and ratio of sums (7.12), while the AI works through the division algorithm and cross-multiplication products (7.19). This constitutes a genuine path difference. The AI's path is logically complete and valid under Q3, confirming category D.

### 7.21
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume A, B (coprime) are not the least in their ratio, use VII.20 to establish that a number measures both A and B the same number of times, deduce that a common measure of A and B exists, and reach a contradiction with their coprimality via D7.12. The only difference is that Heath uses VII.16 (commutativity of multiplication) to swap the measurement relationship (from 'C measures A according to E' to 'E measures A according to C'), while the AI sets up the algebra as A = mE from the start, making m directly a divisor of A without needing the commutativity step. The heath_only citation 7.16 reflects this under-citation by the AI, which is a citation-depth difference rather than a different logical path. Since the key intermediate conclusions are identical and only the granularity of citation differs, this is classified as G.

### 7.22
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume A, B (least numbers in a ratio) are not coprime, introduce a common measure C, define D and E such that C*D=A and C*E=B, apply 7.17 to conclude D:E=A:B, note D<A and E<B, and derive a contradiction with the minimality of A, B. The ai_only set consists entirely of definitions and common notions (CN5, D7.12, D7.3) that the AI cites explicitly where Heath leaves them implicit, and heath_only is empty. This is a clear Case A in Q2: same backbone with different citation depth, classifying as G.

### 7.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume C and B are not prime to one another, derive that some D measures both C and B, show D also measures A (since D measures C and C measures A), reach a contradiction with A and B being prime to one another, and conclude C and B must be prime to one another. The AI proof cites three additional definitions (D7.3, D7.14, D7.15) that Heath leaves implicit, spelling out explicitly what it means for one number to measure another and why the common measure D is greater than a unit. Since ai_only contains only definitions and heath_only is empty, this is a clear case of the AI over-citing foundational definitions at a finer granularity than Heath, with no difference in the logical backbone.

### 7.24
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume for contradiction that a common factor measures both the product A*B and C, apply 7.23 to establish that this factor is prime to A, set up a proportion via 7.19, use 7.21 and 7.20 to derive that the factor must measure B, then reach a contradiction. The AI applies 7.23 an extra time (to B as well as A), which produces a slightly more direct contradiction (the factor measures B yet is prime to B) compared to Heath's contradiction (the factor measures both B and C which are prime to each other), but this is a surface-level variation in the same argument. The citation differences reflect granularity: ai_only contains D7.1 (an over-citation of the definition of unit in the contradiction setup), and heath_only contains 7.16 (the commutativity/measurement step that the AI bypasses by directly invoking the definition of divisibility). Since the key intermediate conclusions and the logical chain are the same, this is a granularity difference.

### 7.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Both proofs follow the same logical backbone: recognizing that A appears twice as a factor in A*A, that each instance of A is prime to B, and then applying 7.24 to conclude that the product A*A is prime to B. Heath introduces an auxiliary variable D equal to A to make the 'two numbers' explicit, while the AI simply refers to A twice directly. The only citation difference is that the AI explicitly cites Definition 7.12 (the definition of 'prime to one another'), which Heath leaves implicit. Since the key intermediate conclusions are identical and the citation difference is limited to an explicit definition reference, Q2 Case A applies, yielding a Granularity difference (G).

### 7.26
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Heath's proof groups the four pairwise coprimality conditions by the target factor: first showing that A and B are each prime to C, hence AB is prime to C (by 7.24), then similarly AB is prime to D, and finally since C and D are each prime to AB, CD is prime to AB. The AI proof instead groups by the source factor: since A is prime to both C and D, CD is prime to A (by 7.24), then similarly CD is prime to B, and finally since A and B are both prime to CD, AB is prime to CD. Both proofs apply 7.24 three times, but the key intermediate conclusions differ — Heath establishes 'AB is prime to C' and 'AB is prime to D' while the AI establishes 'CD is prime to A' and 'CD is prime to B'. This constitutes a genuinely different logical backbone (Case B in Q2), and since the AI's path is logically valid (Q3), the classification is D.

### 7.27
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate passes since 7.25 and 7.26 are both prior to 7.27. Q1 finds no logical errors: the AI proof is complete, correctly applying 7.25 and 7.26 to establish coprimality of both squares and cubes. Q2 identifies the same key intermediate conclusions in both proofs: (1) squares of coprime numbers are coprime, and (2) cubes of coprime numbers are coprime, both established through applications of 7.25 and 7.26. Although the AI uses a slightly different arrangement for the squares sub-proof (applying 7.26 directly to pairs (A,A) and (B,B) rather than chaining two applications of 7.25 as Heath does), the variable naming difference accounts for the apparent divergence, and the overall backbone and citation sets are identical. Since ai_used equals heath_refs exactly ({7.25, 7.26}), the perfect match check yields P.

### 7.28
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined the classification. In Part (i) of the proof, Heath and the AI use different key intermediate conclusions. Heath assumes D measures both the sum CA and AB, deduces D measures the remainder BC, and immediately contradicts the primality of AB and BC via D7.12. The AI instead invokes Proposition 7.23 to establish that C (which measures A) must be prime to B, then shows arithmetically that C also measures B, deriving a contradiction between C measuring B and being prime to B. This constitutes a genuinely different logical backbone: Heath contradicts the primality of the original pair directly, while the AI routes through 7.23 to get a different type of contradiction. Part (ii) is essentially the same in both proofs. Since Part (i) represents a major portion of the proof and uses a substantive proposition (7.23) absent from Heath, the overall classification is path difference. The AI's path is logically valid throughout.

### 7.29
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Both proofs use the same proof-by-contradiction structure: assume the prime p and number A are not prime to one another, derive that some common measure must exist, then show this common measure leads to a contradiction with the definition of primality. Heath argues that the common measure C cannot be the same as A (since A does not measure B but C does), and then notes C measures the prime A while being distinct from it, which is impossible. The AI argues more directly that since any measure of a prime must be a unit (D7.11), the common measure c must be a unit, contradicting the requirement that c be greater than a unit. These reach the same key intermediate conclusion through the same backbone. The ai_only citations D7.11 and D7.12 are definitions that Heath uses implicitly without citing, making this a citation-depth difference (Q2 Case A), which yields G.

### 7.30
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume the prime P does not measure A, conclude via 7.29 that P and A are prime to one another, use 7.21 to establish they are the least in their ratio, derive proportionality from the product equality via 7.19, and apply 7.20 to conclude P measures B. The only citation difference is that the AI explicitly cites D7.11 (the definition of a prime number) when noting that P is prime, whereas Heath uses this fact implicitly. Since the backbones are identical and the sole ai_only item is a definition (over-citation), this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 7.31
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: (1) A is composite so some number B measures it; (2) if B is prime, done; if composite, find C measuring B; (3) transitivity of divisibility gives C measures A; (4) iterate this process to produce a descending sequence; (5) an infinite descending sequence of positive integers is impossible; (6) therefore a prime measuring A must be found. The AI proof explicitly cites definitions D7.13, D7.5, D7.2, D7.11 and common notion CN5 to justify steps that Heath leaves implicit with no explicit citations (heath_refs is empty). Since the key intermediate conclusions are identical and the only difference is that the AI over-cites foundational definitions and axioms that Heath uses without attribution, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 7.32
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a two-case exhaustion where (1) if A is prime, the theorem holds immediately, and (2) if A is composite, Proposition 7.31 guarantees a prime divisor. The AI proof explicitly cites definitions D7.11 (prime) and D7.13 (composite) to justify the case split, while Heath invokes these concepts without formal citation. Since heath_only is empty and ai_only contains only definitions, the symmetric difference reflects over-citation of definitional steps rather than any structural divergence. The key intermediate conclusions are identical in both proofs, making this a citation-depth difference.

### 7.33
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 identifies different logical backbones, leading to Q3 which confirms a valid different path (D). Both proofs divide by the GCD to obtain reduced numbers and establish ratio equality, but they diverge substantially in how they prove minimality. Heath proves minimality by direct contradiction: assuming smaller proportional numbers exist, he constructs a number M and uses 7.19 (cross-multiplication proportion) to show E:H = M:D, concluding M > D contradicts D being the GCD. The AI instead first proves that E, F, G are coprime (by showing any common measure would yield a common measure of A, B, C larger than D, using CN5), then leverages 7.20 (least numbers measure proportionals) extensively to show that any numbers in the same ratio must be multiples of E, F, G, and since E, F, G are coprime the multiplier must be at least 1, ensuring minimality. Even the ratio-establishment step differs: Heath uses 7.16 (commutativity of multiplication) while the AI uses 7.17 (a number multiplying two numbers produces proportional results). These constitute genuinely different intermediate conclusions and proof strategies, both logically sound.

### 7.34
**Category**: Path difference
**Jaccard**: 0.444
**Analysis**: Q2 reveals a different backbone between the two proofs. Heath treats two cases (A,B prime vs. not prime) and uses 7.17 to transfer divisibility in the minimality contradiction (from E|G to C|D via proportionality). The AI unifies both cases by applying 7.33 directly to find the least ratio pair, bypassing the need for 7.21 (primes are least) and 7.16 (commutativity). More significantly, the AI replaces Heath's 7.17-based proportionality transfer with a magnitude argument: since D measures q, q is at least D, so F = q*A is at least D*A = E, contradicting F < E. This is a genuinely different logical mechanism for reaching the contradiction, not merely a difference in citation depth. Q3 confirms the AI's path is valid: the construction via 7.19 is correct, the unification of cases through 7.33 is sound, and the magnitude-based contradiction argument is logically complete. Therefore the classification is D.

### 7.35
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish that any remainder obtained by subtracting (multiples of) the LCM from the target number is measured by both A and B, and by the minimality of the LCM, such a remainder cannot be less than the LCM, which forces the LCM to divide the target number exactly. Heath's proof accomplishes this in a single contradiction step (assuming E does not measure CD yields a remainder CF < E that is measured by A and B, contradicting minimality), while the AI's proof is more constructive, iteratively subtracting L and arguing at each step that the remainder cannot be less than L. The citation difference arises because Heath cites no explicit propositions, while the AI explicitly cites 7.34 (existence of the LCM) and D7.5 (definition of divisibility), making explicit what Heath leaves implicit. Since heath_only is empty and ai_only contains only an existence reference and a definition, this is a citation-depth difference with the same backbone.

### 7.36
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct D = LCM(A, B) via 7.34, then E = LCM(D, C) via 7.34, show A, B, C all measure E because A and B measure D and D measures E, and prove minimality by contradiction using 7.35 twice (first to show D measures any common multiple of A and B, then to show E measures any common multiple of D and C). The AI omits Heath's first case (where C already measures D) but its general argument covers it since LCM(D, C) = D when C measures D. The only citation difference is that the AI explicitly cites D7.5 to justify why E measuring F contradicts F < E, whereas Heath simply states this as obvious. This is a citation-depth difference on the same backbone, yielding G.

### 7.37
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing that the unit measures one number the same number of times as the measuring number measures the measured number, applying alternation via Proposition 7.15, and concluding that the quotient is a part named after the measuring number. The AI swaps the variable names (A measures B instead of Heath's B measures A) but the argument structure is identical. The ai_only set contains only definitions (D7.15, D7.2, D7.3) that Heath invokes implicitly but does not list as explicit citations, while heath_only is empty. This is a classic citation-depth difference with the AI over-citing foundational definitions, placing this squarely in Case A of Q2 as a granularity difference.

### 7.38
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same starting point (the part definition establishing that unit measures C the same number of times B measures A), but they diverge in how they reach the conclusion that C measures A. Heath applies VII.15 (alternation of unit measure) to directly swap the measuring relationship, concluding that C measures A. The AI instead converts the measuring relationship into a multiplication (B times C equals A), then applies VII.16 (commutativity of multiplication) to get C times B equals A, and infers from this that C measures A. These represent genuinely different logical backbones: alternation of ratios versus commutativity of multiplication. The AI's path is logically sound throughout, with each step properly justified by cited definitions and propositions, so Q3 confirms validity, yielding category D.

### 7.39
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) find the LCM of the numbers corresponding to the given parts using 7.36, (2) show via 7.37 that the LCM has all the given parts, (3) prove minimality by contradiction using 7.38 to show that any smaller number with the parts would be measured by those numbers, contradicting the LCM's minimality. The AI proof adds explicit citations of 7.34 and 7.35 (which are internal to Heath's proof of 7.36) and definitions D7.3 and D7.5, and uses 7.35 explicitly in the contradiction step where Heath relies on the direct definition of LCM. Since heath_only is empty and all ai_only items are either definitions or propositions that appear inside Heath's proof of 7.36, this is over-citation at a finer granularity level, making G the appropriate classification.


## Book 8

| Category | Count |
|---|---|
| Perfect match (P) | 4 |
| Granularity difference (G) | 13 |
| Path difference (D) | 9 |
| AI proof error (E) | 1 |

**Total**: 27 propositions

### 8.1
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification. Heath proves 8.1 by contradiction: assuming smaller numbers in the same ratio, he uses ex aequali (7.14) to get A:D = E:H, then invokes 7.21 (primes are least) and 7.20 (least measure same-ratio numbers) to show A measures E, contradicting E < A. The AI takes a fundamentally different direct approach: it uses 7.33 to find the least numbers B1,...,Bn in the same ratio, then applies 7.20 to consecutive pairs to show all Ai = m*Bi for a common multiplier m, and finally uses coprimality of the extremes (D7.12) to force m = 1, concluding Ai = Bi. These are genuinely different logical backbones — contradiction via extremes versus direct construction with consecutive-pair chaining — but both are logically complete and valid, yielding a path difference (D).

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct terms by successive multiplication, show consecutive ratios equal A:B using VII.17/VII.18, establish that extremes are coprime via VII.22 and VII.27, and conclude the terms are least in continued proportion by VIII.1. The AI generalizes to arbitrary n via induction while Heath demonstrates the case n=4, but the key intermediate conclusions are identical. The citation differences are explained by granularity: ai_only items 7.33 (reducing to least terms) and D7.15 (definition of multiplication) are over-citations of preliminary steps Heath leaves implicit; 7.20 is used where 7.17 or 7.18 would be more precise but the underlying claim is sound. The heath_only item 7.18 reflects Heath's use of the symmetric companion to 7.17 for the case of two numbers multiplying one number, while the AI uses 7.17 throughout. The E candidate for miscitation of 7.20 was considered but rejected under the lenience rule since the mathematical claim is correct and licensable by 7.17 (which the AI cites), making it a matter of imprecise citation rather than a logical gap.
**Audit Record**: CANDIDATE E — 8.2
  violated_claim : a*c_{n-1} : b*c_{n-1} = a : b justified by 7.20
  failure_mode   : invalid_inference
  missing_is     : expansion — the claim is sound and could be licensed by 7.17 or 7.18 (which the AI cites)
  evidence       : Step 7: "a*c_{n-1} : b*c_{n-1} = a : b [7.20], since c_{n-1} is a common factor"
  why_not_terse  : 7.20 is about measurement of proportionals by least numbers, not about ratios of products with a common factor; however the claim itself is mathematically correct and supportable by 7.17
  VERDICT: NOT-E — missing_is = expansion; lenience rule applies (sound inference, imprecise citation)

### 8.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 8.3 follow the same logical backbone: both find the two least numbers in the given ratio (VII.33), establish their coprimality (VII.22), use VIII.2 to construct the least continued proportion with the required number of terms, identify the given sequence with the constructed one (since both are least), and conclude coprimality of the extremes via VII.27. The citation sets are identical (7.22, 7.27, 7.33, 8.2) with Jaccard similarity 1.0. No forward dependencies, no logical errors, no missing cases. The AI proof is slightly more explicit about expressing the extremes as powers (e^(n-1) and f^(n-1)) but this is a presentational difference, not a structural one. Since the key intermediate conclusions match and the citation sets are exactly equal, the classification is P (Perfect match).

### 8.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: construct the continued proportion using LCM (7.34), establish proportionality of the constructed terms, and prove minimality via 7.20 and 7.35. The key citation difference is that Heath uses 7.13 (alternate proportion) and D7.20 (definition of proportional) to establish the ratio relationships, while the AI uses 7.17 (multiplication preserves ratios) as a higher-level result. The proof-tree containment test confirms that 7.13 appears inside Heath's own proof of 7.17, so the AI is citing 7.17 as a unit while Heath re-derives its internals inline. The remaining differences (D7.15, D7.2, D7.5 in ai_only; D7.20 in heath_only) are all definitions reflecting different but equivalent definitional grounding. The AI's approach of using a single general LCM-based construction rather than Heath's two separate cases (E measures K vs E does not measure K) is a presentational choice that does not alter the backbone. This is a same-backbone, different-depth situation characteristic of G.

### 8.5
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 determines the classification as D (Path difference). Heath's proof constructs least numbers in continued proportion via 8.4, then uses ex aequali (7.14) to show the ratio A:B equals the compounded ratio G:K. The AI takes a fundamentally different approach: it constructs a single intermediate number E = a*d, uses 7.17 to establish A:E = b:d, uses 7.18 to establish E:C = a:c, and then directly applies the definition of compounded ratio (D6.5) to conclude. The two proofs share only 7.17 in common (Jaccard 0.167). The heath_only propositions 7.14 and 8.4 are substantive results central to Heath's strategy but entirely absent from the AI's approach, which avoids them through a more direct construction. This is a genuine backbone difference (Case B), and the AI's alternative path is logically sound, so Q3 yields D.

### 8.6
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: The proofs have different logical backbones, leading to classification D. Heath's proof takes the least numbers F, G, H in the same ratio as A, B, C via VII.33, applies ex aequali (VII.14), uses VIII.3 to show the extremes are prime, and concludes non-measurement via the definition D7.20. The AI instead takes the least pair p:q in the basic ratio (7.33), constructs the least continued proportion via 8.2, invokes primality of extremes (logically 8.3 content, though labeled as 8.1), then uses 7.21 and 7.20 to set up a measurement-based contradiction showing e_1 = 1 implies p = 1 implies A_1 measures A_2. The AI's use of 8.1 in the direction of 8.3 was considered as a potential E (invalid inference), but under the lenience rule the conclusion is mathematically sound and follows from the converse proposition 8.3, making this a citation label error rather than a logical gap (missing_is = expansion). The key structural difference is that Heath uses 8.3 directly for prime-extremes, while the AI decomposes through 8.2 and 8.1 and relies on measurement theory (7.20, 7.21, 7.22) to reach the contradiction, constituting a genuinely different valid path.
**Audit Record**: CANDIDATE E — 8.6
  violated_claim : "By 8.1, since e_1...are the least numbers in continued proportion, the extremes e_1 and e_{j-i+1} are prime to one another"
  failure_mode   : invalid_inference
  missing_is     : expansion — the conclusion is correct and follows from 8.3 (the converse of the cited 8.1); this is a citation label error, not a logical gap
  evidence       : Step 5 cites 8.1 ("extremes prime to one another implies numbers are least") but uses it in the converse direction ("numbers are least implies extremes are prime"), which is 8.3
  why_not_terse  : The wrong proposition is cited, but the conclusion is mathematically correct via 8.3; the logical chain is sound with the correct reference
VERDICT: NOT-E (missing_is = expansion; lenience rule applies)

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both proofs use identical proof-by-contradiction structure: assume the first number does not measure the second, apply 8.6 to conclude no term measures any other, then note this contradicts the hypothesis that the first measures the last. The citation sets are exactly equal (both cite only 8.6), the key intermediate conclusions are the same, and there are no ai_only or heath_only differences. Since the backbone and citation set match perfectly, the classification is P.

### 8.8
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided this classification. Both proofs share the same backbone of key intermediate conclusions: (1) obtain the least numbers in continued proportion, (2) show their extremes are prime via 8.3, (3) apply ex aequali via 7.14 to equate the ratio of extremes with A:B, (4) use 7.21 and 7.20 to show the least numbers measure D and E equally, and (5) multiply all terms by the same factor to construct the desired continued proportion. The AI's extra citations (8.2, 7.17, CN1) represent over-citation at the same logical positions: 8.2 explicitly constructs the least continued proportion where Heath handles this implicitly through 7.33, 7.17 explicitly justifies ratio-preservation under multiplication where Heath cites D7.20, and CN1 is a common notion for transitivity. Heath's sole extra citation D7.20 is a definition replaced by the AI's more explicit 7.17. Since the backbones match and all citation differences are depth-level, this is Case A in Q2, yielding G.

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same key intermediate conclusions: (1) the sequence A, C1, ..., Cn, B constitutes the least numbers in continued proportion with the given ratio (via 8.1), (2) the terms are identified as powers of the ratio's base terms (via 8.2), and (3) the geometric sequence from the unit to A (and to B) is constructed in continued proportion. The AI adds 7.22 and 7.33 to explicitly reduce the ratio to least terms and prove coprimality, steps that Heath handles implicitly by directly taking F, G as the least in the ratio via 8.2. Heath cites D7.20 to establish proportionality from the multiplication relationships (e.g., F*F=H implies E:F::F:H), while the AI achieves the same through its algebraic power notation. These differences are purely in citation depth and expositional style, not in the logical backbone.

### 8.10
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path (D). Heath's proof constructs specific intermediate numbers H=D*F, K=D*H, L=F*H and builds the continued proportion A,K,L,B by establishing individual ratio equalities (E:H, H:G, A:K, K:L, L:B all equal D:F) using repeated applications of 7.17 and 7.18. The AI takes a fundamentally different algebraic approach, representing A=c^(k+1) and B=d^(k+1) as powers and constructing the general interpolating sequence c^(k+1-j)*d^j. It then gives a uniform proof that all consecutive pairs share the ratio c:d by factoring each pair as c^(k-j)*d^j*c and c^(k-j)*d^j*d and applying 7.17. This general parametric construction versus Heath's specific stepwise construction constitutes genuinely different key intermediate conclusions. The AI's path is logically complete: 7.16 (commutativity) justifies the rearrangement, 7.17 provides the ratio conclusion, and D7.15/D7.20 supply definitional grounding. Heath's use of 7.18 is subsumed by the AI's direct use of 7.16+7.17 (since 7.18 is proved from exactly those two propositions), but the overall proof architecture differs enough to be a path difference rather than a granularity difference.

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct E as the product of the two sides, use VII.17 and VII.18 to establish that the square-to-E ratio and E-to-square ratio both equal the side-to-side ratio, conclude E is the mean proportional, then apply V.Def.9 for the duplicate ratio. The AI proof uses different variable naming (sides are A,B; squares are C,D) compared to Heath (squares are A,B; sides are C,D), but the key intermediate conclusions are identical. The ai_only citations CN1 and D7.18 are over-citations of foundational axioms and definitions that Heath uses implicitly: CN1 for the transitivity step combining equal ratios, and D7.18 for the definition of square numbers. Since heath_only is empty and the ai_only items are purely axiom/definition-level citation depth differences, Case A of Q2 holds, yielding G.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Both proofs establish the same backbone: constructing two mean proportionals between the cubes and showing that the four numbers form a continued proportion with common ratio equal to the side-to-side ratio, then concluding with the triplicate ratio property via V.Def.10. The AI differs only in citation depth: Heath alternates between VII.17 (one number multiplying two numbers) and VII.18 (two numbers multiplying one number) depending on how each product is factored, while the AI restructures the algebra so every ratio comparison fits the VII.18 pattern. The proof-tree containment test confirms that VII.17 appears inside Heath's proof of VII.18, so the AI's exclusive citation of VII.18 is a higher-level citation that implicitly subsumes VII.17. The ai_only items D7.15 and D7.19 are definitions (multiplication and cube number) that Heath leaves implicit. Since the key intermediate conclusions are identical and all citation differences reduce to depth, the classification is G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct auxiliary intermediate products to form continued proportional sequences sharing the common ratio A:B (= B:C), then apply ex aequali (7.14) to conclude D:E = E:F and G:H = H:K. Heath's proof refers to the method of the preceding proposition (8.12) with 'in manner similar to the foregoing,' implicitly using 7.17 and 7.18 which are the explicit citations in 8.12's proof. The AI instead cites 7.17 and 7.18 directly, spelling out each application to establish the intermediate proportions. This satisfies the proof-tree containment test: the AI's extra theorem citations (7.17, 7.18) appear inside the proof of the method Heath invokes implicitly, making this a citation-depth difference rather than a path difference. The AI's additional definition citations (D7.15, D7.18, D7.20) are standard over-citation of foundational definitions. The heath_only set is empty, confirming no substantive steps are missing from the AI proof.

### 8.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: establishing a continued proportion via 8.11, using 8.7 for measure propagation through the continued proportion in the first direction, and applying D7.20 for the measure-ratio connection in both directions. The AI proof adds explicit citations for sub-level arithmetic facts (7.17, 7.18 for ratio-from-multiplication relationships, 7.16 for composing measure relationships, and D7.3 as a definition) that Heath leaves implicit. Since heath_only is empty and the ai_only items are all finer-grained expansions of steps present in both proofs, this is a clear Case A same-backbone scenario with different citation depth.

### 8.15
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: construct a continued proportion between the two cubes using 8.12, apply 8.7 to transfer divisibility along the proportion, then use D7.20 to conclude divisibility of the sides (Part I), and reverse the argument for Part II. Heath additionally cites 8.11 for a separate square-number proportionality (E, F, G), which the AI omits by working directly with 8.12's explicit formulas for the mean proportionals (C=a^2*b, D=a*b^2). The AI's extra citations (D7.3, D7.15, D7.19) are definitions providing explicit grounding, and 7.17 is used for transitivity of divisibility in Part II where Heath uses D7.20 symmetrically. Since 8.11 is not contained within Heath's proof of 8.12, Heath's use of it represents a sub-construction (proportionality of squares) that the AI handles through direct computation rather than a separate theorem, but both proofs reach the same key intermediate conclusions at the same logical positions. This is a citation-depth difference, not a backbone difference.

### 8.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 8.16 are structurally identical. Both establish a biconditional by proving each direction via proof by contradiction using Proposition 8.14 as the sole cited result. In Part 1, both assume the side C measures the side D, invoke 8.14 to conclude the square A measures the square B, reach a contradiction with the hypothesis, and conclude C does not measure D. In Part 2, both assume A measures B, invoke 8.14 to conclude C measures D, reach a contradiction, and conclude A does not measure B. The citation sets are identical (ai_used = heath_refs = {8.14}), giving Jaccard = 1.0. Since the key intermediate conclusions are the same and the citation sets match exactly, this is a perfect match (P).

### 8.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 8.17 are structurally identical. Both prove the two contrapositives of 8.15 by contradiction: (1) if the cube does not measure the cube, assume the side does measure the side, then by 8.15 the cube measures the cube, contradiction; (2) if the side does not measure the side, assume the cube does measure the cube, then by 8.15 the side measures the side, contradiction. The citation sets are identical (both cite only 8.15), the logical backbone is the same, and the Jaccard similarity is 1.0. Since Q1 finds no error, Q2 confirms the same key intermediate conclusions, and the citation sets match exactly, this is a perfect match.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G. Both proofs establish the same key intermediate conclusions: (1) the sides of similar plane numbers are proportional, (2) a mean proportional G is constructed as the product of one side from each number, (3) two applications of 7.17 establish A:G and G:B as equal ratios, (4) A,G,B are in continued proportion, and (5) V.Def.9 yields the duplicate ratio. The difference lies in citation depth: Heath uses 7.13 (alternation) to convert the initial proportion C:D=E:F into C:E=D:F, while the AI reads D7.21 as directly giving c:e=d:f and uses 7.19 (products of extremes equal products of means) plus CN1 to achieve the equivalent construction. The ai_only items (7.19, CN1, D7.16) represent over-citation of definitions and common notions plus an alternative but equivalent route to the same construction, while the heath_only item (7.13) is an alternation step the AI absorbs into its reading of the definition. Since the backbone conclusions are identical and only the citation granularity differs, this is a granularity difference.

### 8.19
**Category**: Path difference
**Jaccard**: 0.571
**Analysis**: Q2 reveals different backbones: Heath constructs similar plane numbers K=C*D and L=F*G, invokes 8.18 to find their mean proportional M, uses 7.13 (alternation) to rewrite the side proportionalities, then builds N=E*M and O=H*M to obtain four numbers in continued proportion. The AI instead directly constructs the two mean proportionals as d*e*k and d*h*k by substituting one side factor at a time from A=d*e*f to B=g*h*k, showing each consecutive ratio equals f:k using 7.17 and 7.18. This avoids 8.18 and 7.13 entirely, representing a genuinely different algebraic strategy. The AI's path is logically complete under Q3(b): every step is supported by cited propositions and the chain runs from premises to conclusion without gaps, so the classification is D.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Both proofs share the same logical backbone: (1) take D,E as the least numbers in ratio A:C via 7.33, (2) use 7.20 to factor A = D*F, C = E*F and C = D*G, B = E*G, establishing A and B as plane numbers, (3) show the sides are proportional (D:E = F:G), and (4) conclude A,B are similar plane numbers. The only divergence is in how step (3) is derived: Heath uses 7.17 twice to establish ratio chains and then 7.13 for alternation, while the AI uses the algebraic equality E*F = D*G, coprimality of D,E via 7.22, and the converse of 7.19 to derive D:E = F:G directly. Since the key intermediate conclusions are identical and only the sub-step justifications differ, Q2 Case A applies, yielding G. The ai_only definitions D7.16 and D7.21 are explicit citations of definitions Heath uses implicitly, confirming a citation-depth difference. The heath_only proposition 7.17 appears inside Heath's own proof of 7.19 (which the AI cites), supporting the containment interpretation for that item.

### 8.21
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Classification was decided at Q2/Q3. The proofs have fundamentally different backbones: Heath decomposes the least numbers (three terms E,F,G) as similar plane numbers via VIII.20, then builds solid numbers using the plane sides and a multiplier, proving similarity through the ratio relationships established by VII.18. The AI instead takes four least terms E,F,G,H via VIII.2, uses VIII.9 to show the prime extremes E and H are perfect cubes (by finding mean proportionals between each and the unit), then constructs solid factorizations of A and D as multiples of these cubes, yielding sides of the form (mp,p,p) and (mr,r,r). The key intermediate conclusions differ entirely: Heath's central step is that E,G are similar plane numbers (VIII.20), while the AI's central step is that E,H are cubes (VIII.9). Neither conclusion appears in the other proof. The AI's path is logically valid throughout, with each step properly supported by cited propositions, so Q3(b) yields D.

### 8.22
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Both proofs share the same logical backbone: they establish that A and C are similar plane numbers via 8.20, then conclude that since A is square, C must also be square. Heath treats the final step as obvious, while the AI expands it by explicitly invoking the definition of similar plane numbers (D7.21) to show sides are proportional, the definition of square (D7.18), and propositions 7.17 and 7.19 to formally derive that equal sides of A force equal sides of C. Since heath_only is empty and all ai_only items (7.17, 7.19, D7.18, D7.21) are sub-steps expanding Heath's implicit reasoning at the same logical position, this is a same-backbone, different-depth situation decided at Q2 Case A as Granularity difference.

### 8.23
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof is extremely concise, relying on a single high-level lemma (8.21, similar solid numbers) to conclude that since A and D have two mean proportionals between them, they are similar solid numbers, and since A is cube, D must also be cube. The AI takes a fundamentally different route: it reduces the ratio to least terms (7.33, 7.22), constructs the least four numbers in continued proportion (8.2) as e^3, e^2f, ef^2, f^3, establishes that A = k*e^3 and D = k*f^3 via divisibility (7.20), uses 8.15 to show e divides a (the cube root of A), derives that k = m^3, and concludes D = (mf)^3 is a cube. The logical backbones are entirely different: Heath argues via the concept of similar solid numbers, while the AI argues via the algebraic structure of least terms in continued proportion and cube root extraction. Both paths are logically complete and valid, yielding a path difference (D).

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that one mean proportional exists between the two given square numbers, (2) transfer that mean proportional to A and B via 8.8, and (3) conclude B is square via 8.22. The only difference is citation depth at step (1): Heath observes that squares are similar plane numbers and applies 8.18 (between similar plane numbers there is one mean proportional), while the AI applies 8.11 (between two square numbers there is one mean proportional) directly. Proposition 8.11 is a more specific result that applies directly to square numbers, whereas 8.18 is the more general version for similar plane numbers. Both reach the identical intermediate conclusion, so this is Case A of Q2 -- same backbone with different citation depth, yielding G.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that two mean proportionals exist between the two given cube numbers, (2) apply 8.8 to transfer that continued proportion to A and B, and (3) apply 8.23 to conclude B is cube. The only difference is that Heath cites 8.19 (between similar solid numbers there are two mean proportionals), first noting cubes are similar solids, while the AI cites 8.12 (between cube numbers there are two mean proportionals) directly. Since 8.12 is the cube-specific version of the same fact that 8.19 establishes for similar solids generally, the key intermediate conclusion is identical in both proofs. This is a citation-depth difference (the AI uses a more specific, directly applicable proposition), not a backbone difference, yielding G.

### 8.26
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined the classification. Both proofs use 8.18 to establish a mean proportional between the similar plane numbers, and both use 7.33 to find least numbers in a ratio. However, their key intermediate conclusions diverge: Heath uses 8.2 to find the least numbers D, E, F in the continued proportion A, C, B and deduces that the extremes D, F are square, concluding directly that A:B has the ratio of a square to a square. The AI instead works through duplicate ratios, using 8.18 to establish that A:B is the duplicate ratio of the sides, then invoking 8.11 to show that e-squared to f-squared (where e, f are the least numbers in the ratio of the sides) is also that duplicate ratio, thereby identifying A:B with the ratio of two square numbers. The proof-tree containment test confirms this is a genuine path difference: 8.2 does not appear inside the proof of 8.11, so the heath_only citation represents an independent logical route rather than a citation-depth difference. The AI's path is logically complete and valid, so Q3 yields D.

### 8.27
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as Case B (different backbone), leading to Q3 which confirmed D. Heath's proof works by finding two mean proportionals between A and B via 8.19, then reducing to least numbers in the same ratio (7.33/8.2) and showing the extremes are cubes (8.2), so A:B equals a cube-to-cube ratio. The AI takes a fundamentally different route: it uses 8.19 to establish that A:B is the triplicate ratio of a:d, then uses 8.12 to show that the ratio of the cubes a^3:d^3 is also the triplicate ratio of a:d, and applies 5.11 (transitivity of ratio equality) to conclude A:B = a^3:d^3. Since a^3 and d^3 are cube numbers by D7.19, the result follows. The AI's path is logically complete and valid but argues through entirely different intermediate conclusions than Heath's, making this a genuine path difference.


## Book 9

| Category | Count |
|---|---|
| Perfect match (P) | 3 |
| Granularity difference (G) | 17 |
| Path difference (D) | 16 |
| AI proof error (E) | 0 |

**Total**: 36 propositions

### 9.1
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof constructs D = A*A, establishes that A:B = D:C via VII.17, transfers the mean proportional from between A,B to between D,C via VIII.8, then concludes C is square because D is square and three numbers in continued proportion starting from a square end at a square (VIII.22). The AI proof instead identifies D as the mean proportional between A and B from VIII.18, then applies VII.19 (product of extremes equals product of means) to conclude A*B = D*D directly, so C = D*D is square by definition (D7.18). The two proofs have entirely different constructions of the intermediate quantity D and use different logical chains: Heath works through ratio transfer and the properties of continued proportions (8.8, 8.22), while the AI works through the product-of-means relationship (7.19). Both paths are logically complete, yielding a valid path difference.

### 9.2
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as D (path difference). Both proofs ultimately establish that one mean proportional falls between A and B and then apply 8.20 to conclude A and B are similar plane numbers. However, the routes to establishing that mean proportional are fundamentally different. Heath constructs D = A*A, establishes D:C = A:B via 7.17, observes that D and C are both square (hence similar plane numbers), uses 8.18 to place a mean proportional between D and C, then transfers this via 8.8 to A and B. The AI instead decomposes the square S into C*C using D7.18, applies the converse of 7.19 to A*B = C*C to directly obtain A:C = C:B, immediately identifying C as the mean proportional between A and B. The AI's path bypasses the intermediate construction of D = A^2 and the chain through 8.18 and 8.8 entirely, constituting a genuinely different logical backbone. The AI's path is logically complete and valid, with each step properly supported by cited propositions.

### 9.3
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof establishes two mean proportionals between the unit and A (using VII. Def. 20), then uses VIII.8 to transfer those mean proportionals to between A and B, and finally applies VIII.23. The AI instead constructs six numbers a, c, A, D, E, F in continued proportion by repeated application of 7.17, then uses 7.19 to prove that F equals B, and applies 8.23 to the sub-chain A, D, E, F to conclude B is cube. The key intermediate conclusions differ fundamentally: Heath's backbone relies on mean proportionals via the unit and the transfer theorem VIII.8, while the AI's backbone relies on direct construction of a continued proportion chain and algebraic identification of F with B via 7.19. Both paths are logically complete and valid, but they argue through genuinely different intermediate conclusions.

### 9.4
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determined the classification. Heath's proof establishes that D=A*A is cube via 9.3, then uses the ratio A:B=D:C (VII.17), the existence of two mean proportionals between similar solid numbers A and B (VIII.19), the transfer of mean proportionals to D and C (VIII.8), and concludes C is cube via VIII.23. The AI takes a fundamentally different path: it explicitly constructs the two mean proportionals between A and C=A*B by repeatedly multiplying by b (the cube root of B), yielding the continued proportion A, Ab, Ab^2, Ab^3=C, using basic arithmetic propositions VII.17, VII.18, VII.19, and VII.16 to establish the ratios and product identities. Both proofs arrive at VIII.23 for the final conclusion, but their logical backbones differ: Heath invokes existence theorems for mean proportionals (VIII.19, VIII.8) and the subsidiary result 9.3, while the AI constructs the intermediates directly from the cube root. The AI's path is logically complete and valid, constituting a genuine path difference.

### 9.5
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: establish that A-squared is cube, use 7.17 to get the ratio A-squared:C = A:B, and then conclude B is cube from the fact that A is cube and the ratio A:B equals a cube-to-cube ratio. The AI operates at a higher level of abstraction throughout: it cites 9.4 (product of two cubes is cube) where Heath cites the lower-level 9.3 (cube times itself is cube), and the AI cites 8.25 (mislabeled as 8.24) directly where Heath re-derives 8.25's internals using 8.19, 8.8, and 8.23. The proof-tree containment test confirms that all heath_only items (8.19, 8.8, 8.23) appear inside Heath's proof of 8.25, and 9.3 appears inside the proof of 9.4. The AI's miscitation of 8.24 (about squares) instead of 8.25 (about cubes) was considered as a potential E under the invalid inference mode, but the AI's text correctly describes the cube-number reasoning matching 8.25, making this a citation label error rather than a logical gap; under the lenience rule the verdict defaults to NOT-E. D7.19 in ai_only is a definition (over-citation). All divergences reduce to citation-depth differences.
**Audit Record**: CANDIDATE E — 9.5
  violated_claim : "by Proposition 8.24 the second number B is also cube"
  failure_mode   : invalid_inference
  missing_is     : expansion — the AI correctly describes the reasoning of 8.25 (cube-to-cube ratio, first cube implies second cube) but mislabels it as 8.24 (which is about squares); the logical support for the conclusion exists in the text, only the citation number is wrong
  evidence       : AI Step 5: "Since two numbers A and B have to one another the ratio which a cube number has to a cube number, and the first of them A is cube, therefore by Proposition 8.24 the second number B is also cube [8.24]" — 8.24 is about square numbers, not cube numbers; the correct proposition is 8.25
  why_not_terse  : CANNOT COMPLETE — this is not a genuine logical gap but a citation labeling error; the described reasoning is sound and matches 8.25. Under the lenience rule, verdict defaults to NOT-E.

### 9.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 9.6 establishes a proportionality chain (unit:A = A:B = B:C), then uses 8.19 (mean proportionals between similar solids), 8.8 (transferring continued proportion), and 8.23 (first of four continued proportionals is cube implies fourth is cube) to conclude A is cube. The AI takes a fundamentally different path: it directly computes B*A = (A*A)*A = A^3, which is cube by definitions D7.17 and D7.19, and then invokes Proposition 9.5 (if a cube number multiplied by any number makes a cube, the multiplied number is also cube) to conclude A is cube. Although the containment test shows that the heath_only items (8.19, 8.8, 8.23) appear inside Heath's proof of 9.5, the AI's backbone introduces a novel key intermediate conclusion not present in Heath (that B*A equals A^3 and is therefore cube by definition) and reduces the problem to an entirely different prior result (9.5). The AI's proof is logically complete and valid but follows a genuinely different logical strategy, warranting classification as D.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same logical backbone: decompose the composite number A into two factors using D7.13 and D7.15, then observe that the product of A with another number equals the product of three numbers, hence is solid. The AI proof explicitly cites D7.16 (definition of plane number) to name the intermediate result that A is plane, and D7.17 (definition of solid number) to formally justify calling the final product solid. Heath makes exactly the same argument but does not explicitly cite these definitions, relying on the reader's implicit understanding of what 'solid' means. Since the ai_only items are both definitions that the AI cites for explicitness while Heath leaves them implicit, and the key intermediate conclusions (factor decomposition, three-number product) are identical in both proofs, this is a citation-depth difference, not a backbone difference.

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish the third term from the unit is square, (2) use 8.22 to extend squareness to all terms leaving out one, (3) establish the fourth term is cube, (4) use 8.23 to extend cubeness to all terms leaving out two, (5) combine to show the seventh is both cube and square. The citation difference lies entirely in how the initial square and cube properties are justified: Heath uses D7.20 (definition of proportional numbers) to show that the unit measures A the same number of times A measures B, and then concludes A multiplied by itself makes B (square) and A multiplied by B makes C (cube). The AI instead directly recognizes that A3 = r times r satisfies D7.18 (definition of square) and A4 = r times r times r satisfies D7.19 (definition of cube). These are definitional-level differences in justifying the same intermediate conclusions, making this a citation-depth difference rather than a backbone difference.

### 9.9
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decides the classification. Heath's proof of the square case uses a two-phase strategy: first invoking 9.8 to establish that every other term (the third, fifth, etc.) is square, then applying 8.22 to fill in the remaining terms. The AI proof takes a fundamentally different approach: it establishes that the unit itself is square (via D7.18), then applies 8.22 sequentially starting from the unit through every consecutive triple, covering all terms by direct induction without needing 9.8 at all. This constitutes a different logical backbone (Case B in Q2). The AI's path is logically valid under Q3: the unit is indeed square, and repeated application of 8.22 to consecutive triples correctly propagates the square property through all terms. Additionally, Heath's proof covers both the square and cube cases (using 8.23 and 9.3 for the cube case), but the statement given to the AI only specifies the square case, so the AI's omission of the cube case is not an error. The heath_only citations 8.23, 9.3 are exclusively for the cube case, while 9.8 is replaced by the AI's inductive approach from the unit.

### 9.10
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decides the classification. Heath's proof of the square part argues by contradiction through ratios: if an even-positioned term C is square and the adjacent odd-positioned term B is square (by 9.8), then B:C = A:B gives A,B the ratio of square to square, so by 8.26 (converse) A is square, contradicting the hypothesis. The AI instead uses 8.22 (in contrapositive/inverse form): for three consecutive terms in continued proportion, if the first is not square then the third is not square, and extends this by induction across all even-positioned terms. These are genuinely different logical backbones -- Heath reasons via ratios and similar plane numbers (8.26), while the AI reasons via properties of squares in continued proportion (8.22). The proof-tree containment test confirms 8.26 does not appear inside Heath's proof of 8.22 (which uses 8.20), so the routes are independent. Additionally, Heath's proof includes a cube part using 8.25 and 9.6 that the AI omits since the proposition statement concerns only squares. The AI's mislabeling of the inverse of 8.22 as 'the contrapositive' was considered as a candidate E (invalid inference), but the underlying mathematical result is sound in the geometric-sequence context, and under the lenience rule this is compressed-but-sound rather than a genuine logical gap. The AI's path is valid, yielding D.
**Audit Record**: CANDIDATE E — 9.10
  violated_claim : "if the first A2 is not square, then the third A4 cannot be square" — AI calls this the contrapositive of 8.22 but it is actually the inverse
  failure_mode   : invalid_inference
  missing_is     : expansion — the mathematical result is true in the geometric-sequence context; the AI compresses the justification by mislabeling the logical operation
  evidence       : AI Step 5: "8.22 states that if three numbers are in continued proportion and the first is square, then the third is square. We use the contrapositive: if the first A2 is not square, then the third A4 cannot be square." The actual contrapositive of 8.22 is "if third NOT square then first NOT square", not "if first NOT square then third NOT square."
  why_not_terse  : Cannot complete convincingly — while the labeling is incorrect, the underlying inference is sound in this context (for r^(k-1), r^k, r^(k+1) in geometric sequence, squareness of first and third are equivalent). This is compressed-but-sound, not a genuine logical gap. Reclassified to NOT-E per lenience rule.

### 9.11
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses a single key move: applying 7.15 (alternation for unit measures) to convert the proportion unit:B = D:E into the statement that B measures E according to the units in D, yielding the result directly. The AI proof takes a fundamentally different path, converting proportional relationships into multiplication statements via 7.19 (product equality from proportions), then establishing each term as a product of earlier terms (B = A*A, C = A*B, D = A*C), and using definitions D7.15 and D7.3 to translate multiplicative relationships into divisibility. The two proofs share zero citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different: Heath reasons through alternation of ratios and unit-counting, while the AI reasons through products and factors. Since the backbones differ (Case B in Q2), Q3 was applied: the AI's multiplication-based chain is logically complete from premises to conclusion, so the classification is D (path difference).

### 9.12
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determined this classification. Heath's proof uses proof by contradiction with iterative application of proportion theory (7.29 to establish coprimality, then 7.19/7.21/7.20 to show the prime must measure each successive term in the sequence, reaching a contradiction). The AI proof takes an entirely different approach: it uses 7.30 (a prime dividing a product must divide one of its factors) combined with direct finite descent. The AI establishes that An = A2 * A(n-1) from the continued proportion, applies 7.30 to conclude p divides A2 or A(n-1), and descends through shorter sequences until reaching the base case A3 = A2^2 where 7.30 yields p divides A2. The key intermediate conclusions differ completely: Heath's backbone involves coprimality assumptions, proportion equalities, and least-ratio arguments, while the AI's backbone involves product decomposition and the prime factor property. This is a genuine path difference. The AI's path is logically complete and valid, so Q3 confirms classification as D.

### 9.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Classification was decided at Q2 (Case A: same backbone, different citation depth). Both proofs follow the same descent argument: assume E measures D but is not among the proportional numbers, show E is not prime and that A is the only prime dividing E, so A measures E, then repeatedly divide out factors showing each quotient is also divisible only by A, descending through the proportional numbers until reaching a contradiction. The key intermediate conclusions are identical in both proofs. The citation differences are all depth-related: the AI cites 7.17 where Heath cites 7.19, but 7.17 appears inside Heath's proof of 7.19 (containment test satisfied), so the AI simply cites a sub-lemma rather than the composite result. Heath cites 9.8 to establish A*A = B while the AI derives this directly from the continued proportion. The AI's additional citations of D7.11, D7.15, and D7.3 are definitions cited explicitly by the AI but used implicitly by Heath. All differences are citation-depth variations on the same logical backbone.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: (1) assume a new prime measures A, yielding a factorization; (2) apply VII.30 to conclude the original primes must divide one of the factors; (3) rule out the new prime factor since it is prime and distinct; (4) conclude the original primes all divide the remaining factor; (5) derive a contradiction since that factor is less than A. The AI's ai_only citations (CN5, D7.11, D7.15, D7.2, D7.3, D7.5) are exclusively definitions and a common notion that Heath leaves implicit, representing over-citation of foundational material rather than any structural difference. Since the backbones are identical and the citation difference is purely one of depth, this is a granularity difference (G).

### 9.15
**Category**: Path difference
**Jaccard**: 0.556
**Analysis**: The forward dependency gate passed (all citations are from Books 7-8, prior to 9.15). Q1 found no logical errors: all three cases are addressed and each step is valid. Q2 revealed that while cases 1 (A+B prime to C) and 2 (B+C prime to A) share the same backbone in both proofs, case 3 (A+C prime to B) follows genuinely different intermediate conclusions. Heath uses algebraic identities II.3 and II.4 to expand DF^2 and then applies separando twice to strip away terms, establishing that A+C is prime to B. The AI instead uses VII.26 to show A is prime to C, then VII.28 to get A+C prime to both A and C, then first-principles divisibility arguments to show A+C is prime to each of p and q individually, and finally VII.24 to conclude A+C is prime to pq=B. These are substantively different logical paths through different intermediate conclusions, so Case B (different backbone) applies. Q3 confirms the AI path is logically valid: each step is properly justified and the chain runs from premises to conclusion without gaps. Classification is D (path difference).

### 9.16
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: assume for contradiction that A:B = B:C, apply 7.21 to establish A and B are the least numbers in their ratio, apply 7.20 to conclude A measures B, then derive a contradiction from A being a common measure of coprime numbers A and B. The AI proof cites three additional definitions (D7.1, D7.12, D7.2) that Heath uses implicitly without citation. Since ai_only contains only definitions and heath_only is empty, and the key intermediate conclusions are identical in both proofs, this is a same-backbone, different-citation-depth case, yielding Granularity difference (G).

### 9.17
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 9.17 by direct contradiction: assuming D:E = A:B, he uses alternation (7.13) to get A:D = B:E, then applies 7.21 and 7.20 to show A measures B, chains through the continued proportion to show A measures D, and derives a contradiction with A and D being prime. The AI takes a fundamentally different route: it uses 8.1 to establish the numbers are least in that ratio, 7.22 to show consecutive terms are prime, and then reduces the problem to 9.16 (if two numbers are prime to one another, the second is not to any other as the first is to the second), applied to the last two terms. The citation sets are completely disjoint (Jaccard = 0.0), and the key intermediate conclusions differ — Heath's backbone involves alternation and chaining divisibility through the proportion, while the AI's backbone involves establishing consecutive terms are prime and reducing to the previous proposition. This is a genuine path difference with a valid alternative proof strategy.

### 9.18
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof first separates the case where A and B are prime to one another, citing 9.16 to establish that no third proportional exists in that case, then handles the non-prime case with a sub-dichotomy on whether A measures B-squared. The AI proof instead uses a single exhaustive dichotomy (A measures B-squared or A does not measure B-squared) that subsumes the prime case without needing 9.16 at all. This represents a genuinely different logical backbone: Heath's three-branch structure (prime, non-prime with divisibility, non-prime without) versus the AI's two-branch structure (divisibility, non-divisibility). Both proofs share the use of 7.19 for the proportionality step and the contradiction argument for the impossibility case, but the overall organizational strategy differs. The AI's path is logically valid since its dichotomy is exhaustive and each branch is soundly argued, yielding classification D.

### 9.19
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath's proof organizes the investigation into four cases based on whether the three numbers are in continued proportion and whether their extremes are coprime, using propositions 9.17, 7.14, 7.21, and 7.20 as key tools across the different cases. The AI proof takes a fundamentally different and more direct approach: it reduces the entire question to a single divisibility criterion, proving that a fourth proportional D to A, B, C exists if and only if A measures the product B*C. The AI uses only 7.19 (products of extremes and means in a proportion are equal, and conversely) to establish both directions. Since the two proofs have entirely different key intermediate conclusions and logical backbones — Heath's multi-case analysis via primality and continued proportion versus the AI's unified divisibility argument — but the AI's path is logically complete and valid, the classification is D (path difference).

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share identical key intermediate conclusions: forming DE as the least number measured by the assigned primes, constructing EF = DE + 1, splitting into two cases (EF prime or not), and in the composite case using 7.31 to find a prime factor G that cannot equal any assigned prime (via the contradiction that it would measure the unit). The AI proof cites six additional foundational items (CN5, D7.1, D7.3, D7.11, D7.13, D7.15) that are all definitions and a common notion which Heath uses implicitly without citation. The heath_only set is empty, confirming the AI omits nothing. This is a clear Case A: same backbone with the AI providing greater citation depth for foundational definitions and axioms.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: each even summand has a half part, so the whole sum also has a half part, making it even by Definition 7.6. The AI proof explicitly invokes Common Notion 2 (if equals be added to equals, the wholes are equal) to justify that combining the half-parts of each summand yields two equal groups, while Heath simply states that 'the whole AE also has a half part' without citing CN2. The underlying logical backbone is identical; the AI merely makes explicit an axiom-level step that Heath treats as obvious. Since ai_only contains only CN2 (a common notion, not a substantive theorem) and heath_only is empty, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 9.22
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decides the classification. Both proofs follow the same logical backbone: decompose each odd number into an even number plus a unit (D7.7), sum the even parts and show the result is even (9.21), note the sum of units equals the even multitude and is therefore even, then conclude the whole sum is even as the sum of two even numbers (9.21). The AI proof explicitly cites CN2 for the algebraic regrouping step and D7.6 for the definition of even number, both of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only foundational axioms/definitions that represent over-citation of steps Heath leaves implicit, this is a same-backbone, different-depth scenario classifying as G.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 9.23 follow the same logical backbone and cite exactly the same propositions. Both proofs subtract one odd number from the collection (leaving an even count of odd numbers), apply 9.22 to conclude the partial sum is even, decompose the remaining odd number into an even number plus a unit via D7.7, combine the even quantities using 9.21, and conclude the total is odd by D7.7. The citation sets are identical (Jaccard 1.0) with no ai_only or heath_only items. Since the key intermediate conclusions match and the citation sets are equal, this is a perfect match under the protocol's final check.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that AB and BC each have half parts (by D7.6, since both are even), then conclude that the remainder AC also has a half part and is therefore even. The only difference is that the AI explicitly cites CN3 (if equals be subtracted from equals, the remainders are equal) to justify the subtraction of the halves, whereas Heath performs this same step implicitly without citing the underlying axiom. Since ai_only contains only CN3 (a Common Notion / axiom) and heath_only is empty, this is a clear case of the AI over-citing at a finer axiomatic level while following the identical argumentative path, which is a citation-depth difference characteristic of Granularity difference (G).

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 9.25 use exactly the same citation set {9.24, D7.7} and establish the same key intermediate conclusions. Both proofs decompose the odd number BC into an even part and a unit using D7.7, apply Proposition 9.24 to conclude that a difference of two even numbers is even, and then use D7.7 again to conclude that the remainder differs from an even number by a unit and is therefore odd. The only difference is in the labeling of segments (Heath uses CD as the unit and DB as the even part, while the AI uses BD as the unit and DC as the even part), but the logical backbone and citation set are identical. Since ai_used equals heath_refs exactly and the key intermediate conclusions match, this is classified as a Perfect match (P).

### 9.26
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical structure: both subtract a unit from each odd number to obtain two even numbers, citing D7.7, then apply 9.24 to conclude the remainder is even. The key intermediate conclusions (AD is even, DC/CD is even, AC/CA is even) are the same in both proofs, and the citation sets are exactly equal (ai_used = heath_refs = {9.24, D7.7}, Jaccard = 1.0). Since Q2 confirms the same backbone and the citation sets match perfectly, the classification is P (Perfect match).

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Classification was decided at Q2/Q3. Heath proves the proposition directly by subtracting a unit from the odd number AB to get even DB, then using 9.24 (even minus even is even) to show that the intermediate segment CD is even, and finally applying Def. 7.7 to conclude the remainder CA is odd. The AI instead uses proof by contradiction: assuming the remainder C is even, it applies 9.21 (sum of even numbers is even) to B + C to derive that A would be even, contradicting the hypothesis. These represent fundamentally different logical backbones -- Heath uses direct decomposition via unit subtraction and even-minus-even (9.24), while the AI uses reductio ad absurdum with sum-of-evens (9.21). The AI's contradictory path is logically complete and valid, so this is a path difference (D).

### 9.28
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) express the product C as a sum of A copies of B via Definition 7.15, (2) observe that each summand B is even, (3) apply Proposition 9.21 to conclude that the sum of even numbers is even, hence C is even. The only citation difference is that the AI explicitly cites Definition 7.6 (the definition of even number) when noting that B is even, whereas Heath simply states 'And B is even' without referencing the definition. This is a straightforward over-citation of a definition, which is a citation-depth difference, not a backbone difference. Since the key intermediate conclusions are identical and the citation difference is purely granular, the classification is G.

### 9.29
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use the definition of multiplication (D7.15) to express the product C as a sum of A copies of B, observe that each term is odd and the multitude of terms is odd, then apply Proposition 9.23 to conclude the sum is odd. The only difference is that the AI explicitly cites Definition 7.7 (the definition of an odd number) when noting that B is odd, while Heath simply states the oddness of A and B without citing a definition. Since ai_only contains only a definition [D7.7] and heath_only is empty, and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference falling under Case A of Q2, yielding Granularity difference (G).

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) let the odd number A measure the even number B some number of times, (2) show by contradiction that this multiplier cannot be odd (since odd times odd yields odd, contradicting B being even), (3) conclude the multiplier is even, and (4) deduce that A therefore measures the half of B. The sole substantive citation difference is that Heath uses 9.23 (sum of odd-many odd numbers is odd) while the AI uses 9.29 (odd times odd is odd). The proof-tree containment test confirms this is a depth difference: Heath's own proof of 9.29 directly cites 9.23, so the AI is citing 9.29 as a packaged unit while Heath works at the more granular level of 9.23. The remaining ai_only items (CN1, CN5, D7.15, D7.3, D7.6, D7.7) are all definitions and common notions representing over-citation of foundational material, a hallmark of granularity difference.

### 9.31
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath proves 9.31 by contradiction: assuming A and 2B share a common factor D, D must be odd (since it divides odd A), and by 9.30 an odd divisor of the even number 2B must also divide B, yielding a contradiction with A and B being coprime. The AI takes a completely different direct approach: since A is odd, 2 does not measure A, and since 2 is prime, 7.29 gives that 2 and A are coprime; combined with the given that B is coprime to A, 7.24 yields that the product 2B is coprime to A. The key intermediate conclusions are entirely different (Heath: odd divisor of even number measures its half; AI: 2 is coprime to A, then multiplicative property of coprimality), constituting a genuine path difference. The AI's chain is logically complete with every step supported by valid citations, so Q3 confirms validity.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing that the sequence of doubled numbers forms a continued proportion from the unit with 2 (a prime) as the second term, applying 9.13 to show the number is measured only by the proportional numbers, observing that all those proportional numbers (other than the unit) are even, and concluding that the number is even-times even only via D7.8. The AI proof adds explicit citations to definitions D7.11 (prime), D7.6 (even number), and D7.9 (even-times odd), and includes an explicit proof by contradiction that the number is not even-times odd, whereas Heath treats this as immediate from the structure of the argument. Since heath_only is empty and ai_only contains only definitions, this is a clear Case A (same backbone, different citation depth), yielding G.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish that the number is even-times odd via D7.9, (2) assume for contradiction that it is also even-times even (D7.8), (3) derive that the half would be measured by an even number and hence be even, contradicting the hypothesis that the half is odd. The AI proof elaborates this same argument with substantially more detail, explicitly citing definitions (D7.3, D7.6, D7.15) and propositions (7.16 commutativity, 9.28 odd times even is even) to justify steps that Heath handles implicitly in a single sentence. The heath_only set is empty, confirming that the AI covers everything Heath references. All ai_only citations are either definitions or propositions that fill in sub-steps of the same reasoning chain, making this a citation-depth difference rather than a path difference.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: first establishing the number is even-times even because its half is not odd (via Definition 7.8), then establishing it is even-times odd through a halving/bisection argument showing that since the number is not among those continually doubled from a dyad, repeated halving must eventually reach an odd number. The AI proof adds explicit citations to definitions (D7.6, D7.7, D7.9, D7.2) that Heath uses implicitly, and cites Proposition 9.32 to formally characterize the numbers continually doubled from a dyad, whereas Heath references this concept directly from the hypothesis without citing a specific proposition. The heath_only set is empty, confirming no substantive steps are missing from the AI proof. All ai_only items represent citation-depth differences rather than backbone divergence.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) apply separando to the continued proportion to derive equal ratios of successive differences to their respective terms, (2) apply VII.12 to sum the antecedents and consequents, (3) simplify the telescoping sum to reach the conclusion. The only substantive difference is which proposition licenses the separando step: Heath uses VII.11 (separando for numbers) together with VII.13 (alternation for numbers), while the AI uses V.17 (separando for magnitudes, the more general Book V result). The AI's additional citations (CN2, CN3, D5.8, D7.20) are common notions and definitions that reflect over-citation rather than a different proof path. Since both proofs establish the same key intermediate conclusions through the same logical structure, differing only in the specific propositions cited to justify the separando step, this is a citation-depth difference (Case A of Q2), yielding G.

### 9.36
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 reveals genuinely different backbones. Heath's proof uses proportional reasoning (7.14 ex aequali, 7.19 product-proportion) to establish the geometric series relationships, then employs an elaborate uniqueness argument via the 'least numbers' chain (7.21 primes-are-least, 7.20 least-measure-proportionals) to show no other number can divide FG. The AI takes a structurally different approach: it uses 9.35 to derive the closed-form sum S = 2*A_n - 1, enumerates divisors of A_n via 9.13 and 9.11, then determines divisors of P = S*A_n directly using 7.29 (prime-to-non-multiple) and 7.30 (prime dividing product divides factor). While both proofs share 9.13, 9.35, 7.29, and D7.22, the key intermediate conclusions differ: Heath reasons through proportional sequences and the least-numbers argument, while the AI reasons through direct divisor enumeration and algebraic summation. The proof-tree containment test shows that 7.19, 7.20, 7.21 do appear inside Heath's proof of 7.30, but in Heath's 9.36 proof these propositions are used independently in a different logical chain (not re-deriving 7.30), so this is genuine path divergence rather than citation-depth difference. The AI's path is logically valid under Q3, yielding classification D.


## Book 10

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 75 |
| Path difference (D) | 37 |
| AI proof error (E) | 3 |

**Total**: 115 propositions

### 10.1
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) use the Archimedean property (D5.4) to find a multiple DE of C exceeding AB, (2) divide DE into parts equal to C, (3) set up parallel subtractions removing more than half from AB-remainders and exactly one copy of C from DE-remainders, (4) show at each stage the DE-remainder exceeds the AB-remainder, and (5) conclude that when the DE-remainder reaches C the AB-remainder must be less than C. The AI proof cites CN5 (whole is greater than part) and D5.2 (definition of multiple) in addition to D5.4, while Heath cites only D5.4. These ai_only items are axiom-level over-citations that Heath invokes implicitly, representing a citation-depth difference with the same backbone, which is Case A of Q2, yielding G.

### 10.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume commensurability implies a common measure exists, show that this common measure must measure every successive remainder in the anthyphairesis process, argue that a remainder smaller than the common measure must eventually appear, and derive a contradiction since the common measure cannot measure a magnitude smaller than itself. The AI proof explicitly cites 10.1 for the existence of a remainder smaller than the common measure, and cites definitions (D10.1.1, D5.1, D5.2) and common notions (CN3, CN5) for supporting reasoning, while Heath's proof makes exactly the same arguments without recorded formal citations. Since heath_only is empty and all ai_only items are either definitions, common notions, or a proposition (10.1) that Heath uses implicitly, this is a citation-depth difference with the same logical backbone, yielding G.

### 10.3
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) handle the trivial case where one magnitude measures the other, (2) apply anthyphairesis (successive subtraction), (3) invoke Proposition 10.2 to guarantee termination since the magnitudes are commensurable, (4) work backwards through the chain of remainders to show the last remainder is a common measure of both original magnitudes, and (5) prove it is the greatest common measure via a reductio or equivalent argument. The AI proof explicitly cites Common Notions (CN2, CN3, CN5) and Definitions (D10.1.1, D5.1, D5.2) that Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are foundational axioms and definitions rather than substantive propositions, this is a clear case of over-citation at a different granularity level, not a path difference.

### 10.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs share the same logical backbone: find D = GCM(A, B) via 10.3, split into two cases (D measures C or not), and in Case 2 find the GCM of C and D to obtain the overall GCM. The key intermediate conclusions are identical in both proofs: establishing commensurability of C and D, showing the GCM candidate measures all three magnitudes, and proving maximality by showing any common measure of A, B, C must divide the candidate. The only difference is that the AI explicitly cites definitions D10.1.1 (commensurability) and D5.1 that Heath uses implicitly without citation. Since ai_only contains only definitions (not substantive propositions) and heath_only is empty, this is a citation-depth difference with the same backbone, yielding G.

### 10.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 reveals fundamentally different logical backbones: Heath establishes intermediate ratios C:A = unit:D and C:B = unit:E using D7.20, inverts via V.7, then composes via ex aequali (V.22) to obtain A:B = D:E. The AI instead expresses A = mC and B = nC directly, then proves A:B = m:n by constructing arbitrary equimultiples pA = (pm)C and qB = (qn)C using Proposition 5.3, comparing them via CN5, and applying the equimultiple definition of same ratio (D5.5). Since the key intermediate conclusions differ entirely (intermediate unit-ratios and ex aequali composition vs. direct equimultiple construction and comparison), Q2 yields Case B (different backbone). Q3 confirms the AI path is logically complete: every step from commensurability through to the D5.5 criterion is supported by cited propositions and definitions, so the classification is D.

### 10.6
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Both proofs share the same high-level strategy: divide A into m equal parts C, construct a magnitude equal to n copies of C, prove the ratio of A to this constructed magnitude equals m:n, then use 5.9 to conclude B equals the constructed magnitude, and hence C measures both A and B. However, the method by which the crucial intermediate ratio is established differs substantially. Heath establishes ratios via D7.20 (number-to-unit proportionality), then chains them using 5.7 (inverse ratios), 5.22 (ex aequali), and 5.11 (transitivity of ratios). The AI instead proves A:D = m:n directly from first principles using D5.5 (the definition of same ratio) and 5.3 (equimultiple arithmetic), bypassing the entire chain of Book 5 proportion theorems. Since the AI replaces three substantive Heath propositions (5.7, 5.11, 5.22) with a direct definitional proof rather than merely citing at different depth, this constitutes a genuinely different logical path. Q3 confirms the AI's path is valid: the chain from premises to conclusion is complete and logically sound.

### 10.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Both proofs share the same logical backbone: assume A has to B the ratio of a number to a number, apply Proposition 10.6 to conclude A and B are commensurable, then derive a contradiction with the hypothesis that A and B are incommensurable. The only citation difference is that the AI explicitly cites Definition D10.1.1 (definition of incommensurable magnitudes) where Heath uses the concept implicitly without a formal citation. Since heath_only is empty and ai_only contains only a definition (D10.1.1), this is a straightforward over-citation at the definitional level with identical intermediate conclusions, placing it squarely in Granularity difference (G).

### 10.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use identical logical backbones: a proof by contradiction that assumes A and B are commensurable, applies 10.5 to derive that they have a ratio of number to number, contradicts the hypothesis, and concludes incommensurability. The only citation difference is that the AI explicitly cites D10.1.1 (the definition of commensurable/incommensurable magnitudes), which Heath leaves implicit. Since D10.1.1 is a definition rather than a substantive proposition, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 10.9
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same four-part structure and the same key intermediate conclusions: (1) commensurable lengths imply a number ratio via 10.5, (2) squares stand in the duplicate ratio of sides via 6.20, (3) between square numbers the duplicate ratio relationship holds via 8.11, and (4) from a number ratio back to commensurability via 10.6, with parts 3 and 4 proved by contradiction from parts 1 and 2. The only difference is that the AI explicitly cites D5.9 (definition of duplicate ratio) in Step 9 and D7.18 (definition of square number) in Step 5, whereas Heath treats these definitional facts as implicit. Since the ai_only set consists entirely of definitions and heath_only is empty, this is a straightforward over-citation case with identical logical backbone, placing it squarely in Case A of Q2 as a granularity difference.

### 10.10
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) construct a line whose square is commensurable with the assigned line's square but which is incommensurable in length, using non-square-number ratios via 10.6 and 10.9; (2) take a mean proportional to get the second line; (3) show the second line is incommensurable in square with the assigned line. The difference lies in citation depth and technique for establishing step (3). Heath cites 10.11 (proportional transfer of incommensurability) as a single unit, while the AI cites 10.7 and 10.8, which are the internal components of 10.11's proof — satisfying the proof-tree containment test for a granularity difference. Similarly, Heath uses D5.9 (duplicate ratio definition) to establish the proportion sq(A):sq(E) = A:D, while the AI uses 6.17 and 6.1 to establish the equivalent proportion sq(A):sq(C) = A:B, reaching the same intermediate conclusion by a slightly different technical route. Since the key geometric conclusions are identical and the citation differences reflect depth rather than backbone divergence, this is a granularity difference.

### 10.11
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions across both cases: in Case 1, that A having a numeric ratio to B transfers to C having a numeric ratio to D via proportion (10.5, 10.6); in Case 2, that the absence of a numeric ratio for A:B transfers to C:D (10.7, 10.8). The AI proof differs from Heath only in citation depth: it explicitly cites 5.11 (transitivity of ratios) for the ratio-transfer step that Heath performs implicitly, and adds definitions D10.1.1 and D5.6 as over-citations. The AI's use of proof by contradiction in Case 2 (rather than Heath's direct argument) is a structural variant of the same logical content, reaching the same conclusions through the same propositions. Since heath_only is empty and ai_only contains only an explicit-citation of an implicit step (5.11) plus definitions, this is a same-backbone, different-depth scenario.

### 10.12
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 reveals different backbones, leading to Q3. Heath's proof constructs numbers in continued proportion via 8.4 and uses transitivity of ratio equality (5.11) to chain A:C and C:B through intermediate numbers H, K, L before applying ex aequali (5.22). The AI proof instead directly scales the numerical ratios using multiplication (7.17) so that A:C = qm:qn and C:B = nq:np, uses inversion (5.7) to orient the second ratio correctly, then applies ex aequali (5.22) with the matching middle terms qn = nq to conclude A:B = qm:np. Both reach the same final conclusion via 10.6, but the intermediate mechanisms differ substantially: Heath relies on a proportional construction (8.4) and ratio transitivity (5.11), while the AI relies on arithmetic scaling (7.17) and ratio inversion (5.7). The AI's path is logically complete and valid, so Q3 yields D.

### 10.13
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: assume B is commensurable with C for contradiction, apply Proposition 10.12 (transitivity of commensurability) to conclude A is commensurable with C, then note this contradicts the hypothesis that A is incommensurable with C, thereby establishing B must be incommensurable with C. The only citation difference is that the AI additionally cites Definition D10.1.1 (the definition of commensurability/incommensurability) when setting up and concluding the proof, while Heath leaves this implicit. Since the key intermediate conclusions are identical and the only difference is the AI's explicit citation of a definition, this is a Case A granularity difference.

### 10.14
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Heath's proof derives the linear proportion A:E :: C:F via separando (5.17) and ex aequali (5.22), then applies 10.11 to transfer commensurability between magnitudes. The AI proof takes a fundamentally different route: it uses alternando (5.16) on the squares proportion to get sq(A):sq(C) :: sq(B):sq(D), then applies the remainder theorem (5.19) to obtain sq(E):sq(F) :: sq(A):sq(C), applies alternando again to get sq(E):sq(A) :: sq(F):sq(C), and transfers commensurability via the square-number ratio characterization of 10.9 rather than the magnitude-level commensurability transfer of 10.11. The key intermediate conclusions differ: Heath works through E:B :: F:D and A:E :: C:F (linear ratios), while the AI works through sq(E):sq(F) :: sq(A):sq(C) and sq(E):sq(A) :: sq(F):sq(C) (square ratios). Both paths are logically complete, making this a valid path difference.

### 10.15
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs establish the same two-part biconditional through identical key intermediate conclusions: (1) a common measure D of AB and BC also measures the whole AC, making AC commensurable with each part; (2) conversely, a common measure of AC and AB also measures the remainder BC, making AB and BC commensurable. The AI proof follows the exact same logical backbone as Heath but explicitly cites foundational axioms and definitions (CN2 for addition, CN3 for subtraction, CN5 for whole greater than part, D5.1 and D5.2 for the definition of measurement) that Heath leaves implicit. The heath_only set is empty and the ai_only set consists entirely of common notions and definitions, confirming this is a citation-depth difference rather than a path divergence.

### 10.16
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Heath's proof works by introducing an explicit common measure D and showing that if D measures both CA and AB then it must also measure the remainder BC, leading to a contradiction with the incommensurability hypothesis. The AI's proof takes a fundamentally different approach: it recognizes that Proposition 10.16 is the contrapositive of Proposition 10.15 and applies 10.15 directly as a black box to derive contradictions without ever introducing a common measure. Since the key intermediate conclusions differ (Heath: explicit common measure argument; AI: direct application of 10.15's contrapositive), this is Case B in Q2. The AI's path is logically valid under Q3 since 10.15 properly licenses all the inferences made, yielding a sound chain from premises to conclusion.

### 10.17
**Category**: Path difference
**Jaccard**: 0.083
**Analysis**: Both proofs share the same algebraic backbone for establishing that the square on the greater exceeds the square on the less by the square on a specific line (using II.5 and quadrupling), but they diverge fundamentally in the commensurability reasoning. Heath uses a chain of X.15 (commensurability of sums and remainders), X.6 (equal magnitudes are commensurable), and X.12 (transitivity of commensurability) to transfer commensurability through the constructed segments. The AI takes a different path: in the forward direction it argues directly from D10.1.1 that a common measure of AE and EB also measures their sum and difference, and in the converse direction it uses 5.15 (equimultiples preserve ratios) and 10.11 (proportional transfer of commensurability) to establish the result through a ratio-based argument. These are genuinely different logical approaches that do not reduce to citation-depth differences. The proof-tree containment test confirms that heath_only items 10.12 and 10.15 do not appear inside the proof of the AI's cited 10.11, establishing an independent logical route. Q3 confirms the AI's path is valid, yielding classification D.

### 10.18
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determines this classification. Heath's proof works directly through a chain of commensurability/incommensurability relations using 10.6, 10.13, and 10.16 to propagate incommensurability through the segments BD, DC, BF+DC, and FD in both directions of the biconditional. The AI proof takes a fundamentally different approach: it introduces the ratio BC:FG = BE:DE and uses 10.11 to transfer commensurability/incommensurability between these pairs, then employs indirect proof (contradiction) via 10.15 and 10.12 in the forward direction, and directly invokes 10.17 as a lemma for contradiction in the converse direction. The key intermediate conclusions differ: Heath chains direct incommensurability relations through segments, while the AI routes through proportionality and contradiction. Both proofs are logically complete and sound, so Q3 confirms D.

### 10.19
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: (1) establish that the square on one of the given rational lines is rational, (2) use VI.1 to set up a proportion between the rectangle and the square, (3) conclude the rectangle is commensurable with the square, and (4) deduce the rectangle is rational by definition. The sole heath_only citation, 10.11, is a proposition whose own proof internally uses 10.5 and 10.6 (both in ai_only), confirming via the proof-tree containment test that the AI is expanding what Heath cites compactly as 10.11 into its constituent steps. The AI also adds explicit transitivity via 10.12 and an explicit definition D10.1.3, both of which are citation-depth additions rather than backbone differences. This is Case A of Q2: same key intermediate conclusions, different citation granularity.

### 10.20
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 reveals genuinely different backbones. Heath's proof works by constructing the square AD on AB, establishing that DA is commensurable with AC (both rational), forming the proportion DA:AC = DB:BC via VI.1, and then applying X.11 to transfer commensurability through that proportion (DB comm. BC, hence AB comm. BC). The AI proof takes a fundamentally different route: it introduces the assigned rational straight line rho explicitly, establishes that both S and the square on A are each commensurable with the square on rho (Steps 2-3), uses transitivity of commensurability (10.12) to conclude S is commensurable with the square on A (Step 4), then converts through the ratio-of-numbers pathway (6.1 to get the proportion, 10.5 to extract a numeric ratio, 10.6 to convert back to commensurability in length). Although Heath's 10.11 internally uses 10.5 and 10.6, the AI does not replicate 10.11's framework of transferring commensurability through a proportion; instead it establishes commensurability via a transitivity argument through rho, which is a different logical backbone. The AI proof is logically complete under the hardened Q1(b) standard, so Q3 confirms a valid different path, yielding category D.

### 10.21
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G. Both proofs establish the same key intermediate conclusions: the square on A is rational, A and B are incommensurable in length, the rectangle is to the square as B is to A (via 6.1), the rectangle is incommensurable with the square, and therefore the rectangle is irrational. The sole substantive citation difference is that Heath cites 10.11 (if four magnitudes are proportional and the first is incommensurable with the second, the third is incommensurable with the fourth) while the AI directly applies 10.7 and 10.8, which are the internal components of 10.11's incommensurable case. The proof-tree containment test confirms this: Heath's proof of 10.11 explicitly uses 10.7 and 10.8 for the incommensurable direction, so the AI is inlining the internals of 10.11 rather than citing it as a unit. The remaining ai_only items (D10.1.2, D10.1.3) are definitional over-citations. This is a citation-depth difference with identical logical backbone.

### 10.22
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: The forward dependency gate passed. Q1 found no logical errors in the AI proof. Q2 revealed that while both proofs share the same backbone for establishing the rationality of C (reciprocal proportionality leading to commensurability of squares, hence rationality), the incommensurability arguments follow genuinely different paths. Heath establishes that EF^2 is incommensurable with rect(FE,EG) via a Lemma and X.11, then uses 10.13 (transfer of incommensurability through commensurable magnitudes) to conclude CD^2 is incommensurable with rect(DC,CB). The AI instead argues directly that B*C = A^2 is irrational (medial) and hence incommensurable with the rational area B^2, then uses 6.1 to express the ratio B*C:B^2 = C:B and applies 10.11 to conclude incommensurability. This substitution of 10.13's indirect incommensurability transfer with a direct irrationality argument via 6.1 constitutes a different logical backbone, not merely a citation depth difference. Q3 confirmed the AI's alternative path is logically complete and sound, yielding classification D.

### 10.23
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: set out a rational line CD, apply rectangles equal to A-squared and B-squared, show the breadths are commensurable (via 6.1 and 10.11), deduce DF is rational and incommensurable with CD (via 10.13), and conclude B is medial via 10.21. The AI adds three citations not in Heath (10.9, 10.6, 10.12) but these are sub-steps that Heath compresses: Heath states that commensurable lines have commensurable squares without citing 10.9 and 10.6 explicitly, and deduces DF is rational by direct appeal to Definition 10.1.3 rather than going through 10.12 (transitivity of commensurability). The key intermediate conclusions are identical in both proofs, making this a same-backbone, different-depth case (Case A of Q2), hence G.

### 10.24
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: establish that the square on one of the medial lines is medial, show the rectangle is commensurable with that square, then conclude the rectangle is medial via 10.23. The key difference is citation depth in establishing commensurability: Heath cites 10.11 as a single unit to transfer commensurability through a proportion, while the AI explicitly deploys 10.5 and 10.6 (the internal steps of 10.11's proof, as verified by the containment test). The remaining ai_only items (10.21, 2.14, D10.1.2, D10.1.4) are definitions or foundational constructions representing over-citation of background details. Since the backbones match and the citation differences reduce to depth of exposition, this is a granularity difference.

### 10.25
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs follow the same logical backbone: apply squares on the two medial lines to a rational straight line, obtain rational breadths that are commensurable in length with each other, establish a mean proportional, use VI.17 to equate the rectangle of the outer breadths with the square on the middle breadth, conclude the middle breadth is rational, and then split into two cases (commensurable or incommensurable in length with the rational line) yielding a rational or medial area. The citation differences are purely depth-related: the AI explicitly cites definitions D10.1.2, D10.1.3, and D10.1.4 that Heath uses implicitly, while Heath explicitly cites 5.11 (transitivity of ratios) which the AI uses implicitly in Step 8 when combining two ratio equalities. No logical error was found; the proofs share the same key intermediate conclusions at every stage.

### 10.26
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 reveals genuinely different backbones after the shared initial setup (applying medial areas to a rational line and deducing properties of the breadths via 10.22 and 10.20). Heath derives a contradiction by showing EH is both rational and irrational, working through ratio-based incommensurability propagation (10.11, 10.13) and the square-sum identity II.4 with 10.16. The AI instead uses difference-of-squares factoring via 2.1 and transitivity of commensurability (10.12, 10.15) to show that FH+FG and then FH itself must be commensurable in length with EF, directly contradicting the earlier result from 10.22. These are different key intermediate conclusions: Heath's pivotal step is that sq(EH) is irrational via 10.16, while the AI's pivotal step is that FH is commensurable with EF via algebraic manipulation of the sum and difference of breadths. The AI's alternative path is logically complete with every step properly cited and sound, so Q3 confirms D.

### 10.27
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decides the classification. Heath constructs medial lines C and D where C is the mean proportional of two rational lines A,B (via 6.13) and D is a fourth proportional satisfying A:B = C:D (via 6.12), then uses 10.11 to transfer commensurability-in-square-only from A,B to C,D, and alternando (5.16) to show rect(C,D) = sq(B) is rational. The AI constructs a different pair: C as the same mean proportional, but E as the third proportional to C and A (via 6.11), then proves rect(C,E) = sq(A) directly from the third-proportional relation, and establishes commensurability-in-square-only of C,E through an elaborate ratio argument using 6.1, 6.22, and 10.12 rather than 10.11. The two constructions produce genuinely different pairs of medial lines through different intermediate conclusions, constituting a valid alternative path confirmed under Q3's hardened standard.

### 10.28
**Category**: Path difference
**Jaccard**: 0.353
**Analysis**: Q2 determined the classification. Heath's proof starts with three rational straight lines A, B, C commensurable in square only, takes D as a mean proportional between A and B, sets E via a proportion B:C = D:E, then uses X.11 to transfer commensurability and X.23 to establish E as medial, finally showing rect(D,E) = rect(A,C) is medial. The AI proof takes a fundamentally different constructive approach: it begins with one rational line and three numbers with specific ratio properties (p=2, q=3, r=12), constructs lines B and D via 6.12 using number-theoretic commensurability criteria (10.6, 10.9), forms medial lines C and E as mean proportionals, then introduces an auxiliary rational line G as the mean proportional of B and D. The AI shows rect(C,E) = rect(A,G) through a complex proportional argument using 6.1, 6.22, and 6.16, and concludes the rectangle is medial since A,G are rational commensurable in square only. The key intermediate conclusions differ substantially: Heath transfers commensurability via X.11 and mediality via X.23, while the AI builds commensurability from number ratios via 10.6/10.9 and mediality of the rectangle through the auxiliary line G. The AI's path is logically valid and complete, yielding a genuine path difference.

### 10.29
**Category**: Path difference
**Jaccard**: 0.176
**Analysis**: Q2 decided the classification. Heath's proof uses a semicircle construction with arbitrary square numbers CD and DE (where CE is not square), applies 3.31 (angle in semicircle is right) and 5.19 (convertendo) to derive the commensurability of the excess. The AI proof takes a fundamentally different approach: it bisects A to get C = A/2, uses 2.4 to compute sq(A) = 4*sq(C), constructs B via a right angle at a point (1.11) and the Pythagorean theorem (1.47) to get sq(B) = 3*sq(C), then derives the 4:3 ratio directly by arithmetic. The key intermediate conclusions differ in construction method (semicircle vs direct right-angle construction) and in how the excess commensurability is established (convertendo vs direct arithmetic). Both paths are logically complete, making this a valid path difference.

### 10.30
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 determines the classification. Heath's proof constructs a semicircle on the rational line AB, uses III.31 (angle in semicircle is right) and I.47 (Pythagorean theorem) to establish the relationship sq(AB) = sq(AF) + sq(BF), then applies convertendo (V.19) to obtain the ratio CD:DE :: sq(AB):sq(BF), from which incommensurability of AB and BF follows via X.9. The AI proof avoids the semicircle construction entirely, instead working purely within proportion theory: it applies separando (V.17) directly to the given proportion DF:DE :: sq(A):sq(FG) to derive EF:DE :: sq(H):sq(FG), then uses ex aequali (V.22) to obtain EF:DF :: sq(H):sq(A), concluding H is incommensurable with A via X.9. These are genuinely different logical backbones -- Heath's route goes through geometric construction (semicircle, right angle, Pythagorean theorem) while the AI's route is purely ratio-theoretic (separando, ex aequali). Neither subsumes the other, so the proof-tree containment test confirms this is Case B (different backbone). The AI's path is logically complete and valid, yielding classification D.

### 10.31
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: starting from two rational lines A, B commensurable in square only with commensurable excess (10.29), constructing C with sq(C) = rect(A,B) to get a medial line (10.21), establishing the proportion A:B = C:D, concluding C and D are commensurable in square only (10.11), D is medial (10.23), rect(C,D) is rational (equal to sq(B)), and sq(C) > sq(D) by a commensurable line (10.14). The AI proof reaches every key intermediate conclusion that Heath's proof does. The ai_only items (5.16, 6.12, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4) are all construction propositions, proportion lemmas, and definitions that the AI cites explicitly where Heath leaves them implicit. The heath_only item (10.30) appears only in Heath's supplementary 'similarly' remark about the incommensurable case, which is not part of the stated proposition. This is a same-backbone, different-depth scenario, yielding G.

### 10.32
**Category**: Path difference
**Jaccard**: 0.263
**Analysis**: Q2 determined the classification. Heath's proof starts with three rational lines A, B, C from 10.29, defines D via sq(D) = rect(A,B) and E via rect(D,E) = rect(B,C), then derives the proportion A:C = D:E to establish all required properties. The AI proof takes a fundamentally different constructive approach: it starts with only two rational lines A, B from 10.29, independently constructs a third rational line E using number-theoretic arguments (10.6, 10.9, D10.1.3), defines M via sq(M) = rect(A,E), and obtains G as the fourth proportional (6.12) so that A:B = M:G. The central proportions differ (Heath: A:C = D:E; AI: A:B = M:G), the auxiliary constructions differ (Heath: rectangle equalities; AI: fourth proportional and independent rational line), and the route to showing the rectangle is medial differs (Heath: rect(D,E) = rect(B,C) which is directly medial; AI: rect(M,G) = rect(B,E) via ratio manipulations with 5.7, 5.9, 6.1). The AI's different path is logically complete and valid throughout, with each step properly justified by cited propositions. The large symmetric difference (Jaccard 0.263) and the presence of substantive ai_only propositions (6.12, 6.22, 5.7, 5.9) as well as substantive heath_only propositions (6.16, 6.17, 6.4, 6.8 from the Lemma; 10.30 from the secondary case remark) confirm a genuine path difference rather than mere granularity variation.

### 10.33
**Category**: Granularity difference
**Jaccard**: 0.208
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same six key intermediate conclusions: (1) AE incommensurable with EB via 10.18, (2) sum of squares on AF and BF equals the rational square on AB via I.47, (3) EF equals BD, (4) rect(AF,FB) equals rect(AB,EF), (5) rect(AF,FB) is medial, and (6) AF and BF are incommensurable in square. The AI proof is far more explicit in its citations, spelling out construction steps (1.10, 1.11, P1, P3), definitions (D1.17, D1.18, D10.1.2, D10.1.3, D10.1.4), the semicircle angle theorem (3.31), similar triangle results (6.8, 6.17), and the incommensurability chain (6.1, 10.7, 10.8) that Heath leaves implicit. The sole heath_only citation, 10.23 (commensurable with medial is medial), is used by Heath to transfer mediality from rect(AB,BC) to rect(AB,EF); the AI bypasses 10.23 by directly showing that AB and EF are rational and commensurable in square only, then applying 10.21 to rect(AB,EF) without going through rect(AB,BC). This is a minor sub-path variation within the same overall backbone, not a genuine path difference, making this a granularity difference.

### 10.34
**Category**: Granularity difference
**Jaccard**: 0.25
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish two medial straight lines commensurable in square only containing a rational rectangle with incommensurable excess, (2) use a semicircle construction with area application via 6.28, (3) derive incommensurable segments via 10.18, (4) show the sum of squares on the resulting lines is medial via 3.31 and 1.47, (5) show the rectangle is rational via 10.6, and (6) show the lines are incommensurable in square. The sole heath_only citation (10.31) is accounted for by containment: Heath cites 10.31 directly to obtain the medial lines, while the AI re-derives the same content from primitive propositions in Steps 1-6 (using 10.30, 6.13, 6.17, 10.21, 6.11, etc.). Similarly, AI-only citations in the semicircle portion (6.8, 6.16, 10.7, 10.8) are finer-grained steps for what Heath accomplishes with the Lemma and 10.11. Every key intermediate conclusion appears in both proofs at the same logical position, confirming Case A of Q2.

### 10.35
**Category**: Path difference
**Jaccard**: 0.161
**Analysis**: Q2 decided the classification. Heath's proof starts from 10.32 which directly provides two medial lines commensurable in square only containing a medial rectangle with the desired excess property, then applies the semicircle/perpendicular construction to obtain the final lines. The AI proof instead starts from 10.30 (rational lines commensurable in square only), constructs an auxiliary line GH via 6.12, builds mean proportionals KL and MN using 6.13, proves KL and MN are medial and commensurable in square only with a medial rectangle and the needed excess property (Steps 1-7), and only then applies the semicircle construction (Steps 8-14). The AI's construction of the starting medial lines through mean proportionals and Book 6 techniques is fundamentally different from Heath's direct use of 10.32, making this a different backbone (Case B). The proof-tree containment test confirms this: the AI does not re-derive 10.32 inline but rather constructs different geometric objects via an independent route using 6.12, 6.13, and 6.16. Under Q3, the AI's different path is logically complete, with each step properly cited and the chain running soundly from premises to conclusion.

### 10.36
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Both proofs establish the same key backbone: the sum of squares on AB and BC is rational, twice the rectangle AB,BC is incommensurable with that sum, and therefore the square on AC (which equals the sum of squares plus twice the rectangle by 2.4) is incommensurable with a rational area and hence irrational. The difference lies in how the incommensurability of twice the rectangle with the sum of squares is established. Heath uses 10.11 (proportionality transfers incommensurability) directly on the proportion AB:BC = rect(AB,BC):sq(BC) to get that the rectangle is incommensurable with sq(BC), then chains through 10.6 and 10.13. The AI instead cites 10.21 (the rectangle of rationals commensurable in square only is medial/irrational) to characterize the rectangle as irrational, then reasons that twice an irrational area remains irrational and hence incommensurable with the rational sum of squares. Since 10.11 (the sole heath_only item) appears inside Heath's own proof of 10.21, the proof-tree containment test is satisfied: the AI cites 10.21 as a unit while Heath re-derives one of 10.21's internal steps inline. The ai_only items 10.12, D10.1.2, and D10.1.3 are over-citations making explicit what is implicit in the definition of rational lines and in the direct application of 10.15. This is a citation-depth difference, not a path difference, so the classification is G.

### 10.37
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determines the classification. Heath's proof uses a direct argument: referencing the reasoning pattern from 10.36, it establishes that the squares on AB, BC are incommensurable with twice the rectangle AB, BC, then applies componendo with 10.16 to conclude that the square on AC is incommensurable with the rational rectangle AB, BC, hence irrational. The AI proof takes a fundamentally different path: it separately establishes that the sum of squares on AB, BC is medial (irrational) via 10.15 and 10.13, that twice the rectangle is rational via 10.6, and then uses a proof by contradiction to show the square on AC cannot be rational (and further argues it cannot be medial, citing 10.26). The backbones differ -- Heath uses direct incommensurability reasoning with 10.16 while the AI uses contradiction via the rational/irrational dichotomy. The proof-tree containment test confirms this is not a mere depth difference: although several ai_only citations (10.13, 10.15, 10.6) appear inside Heath's proof of 10.36, the AI does not cite 10.36 as a unit and instead follows a structurally different contradiction-based argument that avoids 10.16 entirely. Under Q3, the AI's different path is logically complete and valid, yielding classification D.

### 10.38
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) the squares on AB, BC and twice the rectangle AB, BC are medial areas; (2) the sum of squares is incommensurable with twice the rectangle via X.11, X.15, X.6, X.13; (3) applying these to a rational line yields rational breadths incommensurable with it (X.22); (4) the breadths are incommensurable in length with each other; (5) their sum is irrational by X.36; (6) therefore AC is irrational. The ai_only citations (10.12, 10.23, D10.1.1, D10.1.3) are over-citations providing extra granularity: 10.12 explicitly justifies that the breadths are commensurable in square, 10.23 explicitly justifies that 2*AB*BC is medial, and D10.1.1/D10.1.3 are definitional references. The heath_only citations (1.44, 6.1) are construction and proportionality propositions that the AI handles implicitly or absorbs into its application of X.11. The logical backbone is identical; only the citation depth differs.

### 10.39
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) twice the rectangle AB,BC is medial, (2) the rational sum of squares on AB,BC is incommensurable with the medial twice-rectangle, (3) the square on AC equals the sum of squares plus twice the rectangle, (4) the square on AC is incommensurable with the rational sum of squares, and (5) therefore AC is irrational. The citation differences are all depth-related: Heath cites 10.33 for the existence of the configuration and 10.6 alongside 10.23 to justify that twice a medial area is medial, while the AI omits 10.33 (simply stating the conditions) and uses 10.23 with definitions instead of 10.6. Conversely, the AI explicitly cites 2.4 for the algebraic identity and 10.13 for transitivity of incommensurability, steps Heath performs implicitly or more directly. D10.1.3 is an additional definitional citation by the AI. Since the key intermediate conclusions are identical and the differences are limited to citation granularity, the classification is G.

### 10.40
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) the sum of squares on AB, BC is incommensurable with twice the rectangle AB, BC, (2) sq(AC) is incommensurable with twice the rectangle via 10.16, (3) sq(AC) is irrational, and (4) AC is irrational. The AI proof is more granular, explicitly citing 2.4 for the algebraic expansion of sq(AC), using 10.6 and 10.12 to prove that twice the rectangle is rational, invoking 10.21 to characterize medial areas, and applying 10.13 for transitivity of incommensurability. Heath compresses all of these into briefer reasoning. The heath_only citation 10.34 is merely a reference to the construction producing the given conditions, which the AI states directly as hypotheses. All ai_only citations (2.4, 10.6, 10.12, 10.13, 10.21) provide finer-grained justification for the same logical backbone, making this a citation-depth difference rather than a path difference.

### 10.41
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: set up a rational line DE, apply the two medial areas as rectangles on DE, show via X.22/10.22 that both breadths are rational and incommensurable with DE, show the breadths are incommensurable with each other, conclude via X.36/10.36 that their sum is binomial (irrational), and hence sq(AC) is irrational so AC is irrational. The heath_only citations (10.35, 6.1) reflect reference-level differences: 10.35 is merely the construction proposition for the setup conditions which the AI states directly, and 6.1 is used by Heath alongside X.11 for the step from area incommensurability to breadth incommensurability, which the AI handles with 10.11 alone. The ai_only citations (10.6, 10.23, 10.13, 10.12, 10.20) represent finer-grained explicit justifications for steps Heath handles more tersely: showing 2*rect(AB,BC) is medial via 10.6 and 10.23, deriving incommensurability via 10.13, establishing commensurability in square via 10.12, and using 10.20 for an indirect irrationality argument. All key intermediate conclusions appear in both proofs at the same logical positions, making this a citation-depth difference.

### 10.42
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined this classification. Both proofs share the core strategy of using II.4 to equate two decompositions of the square on AB, then contrasting the rational nature of sums of squares with the medial nature of rectangles. However, the proofs diverge in how they ensure completeness. Heath first establishes that AC cannot equal DB and that C, D are not equidistant from the midpoint, then uses the II.4 argument to derive a rational-equals-medial-difference contradiction (X.26), concluding immediately. The AI omits Heath's preliminary distinctness arguments and instead splits into two sub-cases after the II.4 setup: if the difference is nonzero, the same rational-vs-medial contradiction applies (10.26); if the difference is zero, a separate argument using bisection (1.10) and II.5 shows C must equal D, contradicting the assumption. This case-split approach with the bisection/II.5 branch constitutes a genuinely different backbone from Heath's preliminary-distinctness approach, making this a path difference. The AI's path is logically valid throughout.

### 10.43
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: assume AB is divided at two points C and D as a first bimedial, observe that twice the rectangles AC.CB and AD.DB are both rational so their difference is rational, observe that the sums of squares AC^2+CB^2 and AD^2+DB^2 are both medial, note that the algebraic identity (via II.4) forces the difference of the sums of squares to equal the rational difference of the rectangles, then invoke X.26 to reach a contradiction since a medial area cannot exceed a medial area by a rational area. The AI proof cites this same chain explicitly through 10.15, 10.23, 10.26, 10.37, 2.4, CN1, CN2, CN3, and D10.1.4, providing granular justification for steps Heath leaves implicit, and adds an extended argument (Steps 12-20 using 2.5) showing C=D directly, which goes beyond Heath but does not change the backbone. Heath's recorded references are empty in the data though the text clearly cites X.26; the AI's additional citations are all either definitions, common notions, algebraic identities, or properties of medial areas that support the same key conclusions at greater depth, making this a citation-depth difference rather than a path difference.

### 10.44
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Both proofs follow the same backbone: assume two division points C and D for the second bimedial AB, apply the resulting areas to a rational straight line, show the breadths are rational and incommensurable in length with the rational line, establish incommensurability between the sums of squares and twice the rectangles, conclude the breadths form a binomial straight line, and use the uniqueness of binomial division (10.42) to reach a contradiction forcing C = D. The citation differences are granularity-level: Heath uses 10.6, 10.13, and 6.1 in a detailed chain to establish incommensurability of the sums of squares with twice the rectangles and to convert area incommensurability to length incommensurability, while the AI compresses some of these steps (citing 10.38 broadly in Step 9, using 10.11 alone instead of 6.1+10.11). The AI adds explicit citations for establishing mediality (10.15, 10.23), explicitly cites 10.42 (which Heath uses implicitly), and includes extra detail via 2.5, CN1, and CN3. Q2 Case A holds: same key intermediate conclusions at different citation depth, yielding G.

### 10.45
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume two different divisions of a major straight line, show that the difference between the sums of squares (rational minus rational) equals the difference between twice the rectangles (medial minus medial), and derive a contradiction via 10.26 since a medial area cannot exceed a medial area by a rational area. The AI proof cites 2.4 and CN3 to explicitly derive the algebraic identity that Heath states directly, and cites 10.12 and 10.15 to explicitly justify that the difference of two rational areas is rational, which Heath simply asserts. The AI also adds Steps 8-10 showing the pairs must be identical, going beyond Heath's level of detail. Since heath_only is empty and all ai_only citations (10.12, 10.15, 2.4, CN3) are sub-level foundational results making explicit what Heath leaves implicit, this is a clear Case A same-backbone granularity difference.

### 10.46
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: assume AB is divided at C per 10.40, suppose also divided at D, show that the difference of the twice-rectangles equals the difference of the sums of squares, note that the twice-rectangles are rational so their difference is rational, but the sums of squares are medial so a medial area would exceed a medial area by a rational amount, contradicting 10.26. The AI proof adds extra steps (10-16) that algebraically show C=D after the contradiction, which are unnecessary but not erroneous. All ai_only citations (10.12, 10.15, 2.4, 2.7, CN1, CN2, CN3, D10.1.4) are over-citations providing granular justification for steps Heath performs implicitly: definitions and propositions for commensurability of rational areas, algebraic identities for squares and rectangles, and common notions for equality operations. Heath_only is empty, confirming the AI covers all of Heath's reasoning at finer granularity.

### 10.47
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same backbone: assume AB is divided at two points satisfying the conditions of 10.41, apply the resulting areas to a rational straight line, show the breadths are rational and commensurable in square only (via 10.22), conclude they form a binomial (10.36), and derive a contradiction from the uniqueness of binomial division (10.42). The heath_only set is empty, confirming every Heath citation appears in the AI proof. The ai_only set consists entirely of over-citations: definitions (D10.1.3, D10.1.4), common notions (CN1, CN2, CN3), the defining proposition 10.41, intermediate lemmas Heath uses implicitly (10.6, 10.13, 10.23), and 2.7 used in an additional explicit derivation showing AC=AD and CB=DB that Heath handles by simply declaring the contradiction absurd. These are all citation-depth differences, not backbone differences.

### 10.48
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they construct two rational straight lines commensurable in square only, conclude their sum is binomial via 10.36, then verify the first binomial conditions by showing the greater term's square exceeds the lesser's by the square on a line commensurable in length with the greater term, and the greater term is commensurable in length with the set-out rational line. The heath_only citations (10.28 for the Lemma providing suitable numbers, and 5.19 convertendo for deriving the ratio of the excess square) reflect Heath's more general approach, while the AI provides specific numbers (3, 1, 4) instead of citing the Lemma and computes the excess directly rather than using convertendo. The AI's ai_only items are predominantly over-citations: common notions (CN1, CN3, CN5), definitions (D10.1.3, D10.1.4, D10.2.1), and 5.22 (ex aequali) used to combine ratios where Heath handles this implicitly. The proposition 10.13 appears in the AI's USED list but is not visibly invoked in the proof text. All differences are citation-depth variations around the same key intermediate conclusions, placing this squarely in Case A of Q2.

### 10.49
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs construct the second binomial straight line through identical logical backbones: setting up numbers with the required ratio properties, establishing a rational line commensurable with D, using X.6 to create the square ratio, X.9 for incommensurability in length, X.36 for the binomial conclusion, V.19 (convertendo) for the square-difference property, and X.9 again for commensurability of the difference line. The AI proof differs only in citation depth: it explicitly cites definitions D10.1.3 and D10.2.2, common notion CN3, and proposition 10.13 (to explicitly show the greater term is incommensurable with D), all of which Heath leaves implicit. The heath_only set is empty, confirming the AI covers all of Heath's cited material. The ai_only items are all over-citations (definitions, a common notion, and one additional explicit verification step), making this a clear Case A granularity difference.

### 10.50
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: constructing rational lines incommensurable in length with the given rational line, showing they are commensurable in square only so their sum is binomial, proving the square on the greater exceeds the square on the lesser by the square on a line commensurable in length with the greater, and concluding that neither term is commensurable in length with the rational line, hence the sum is a third binomial. The only substantive citation difference is that Heath uses convertendo (5.19) directly to derive the excess-square ratio, while the AI expands this into separando (5.17), invertendo (D5.5), and ex aequali (5.22). The proof-tree containment test confirms this is a depth difference: 5.17 appears inside Heath's proof of 5.19, so the AI is re-deriving 5.19's internals rather than citing it as a unit. The remaining ai_only items (1.47, D10.1.3, D10.2.3, D5.5) are construction-step and definition citations representing standard over-citation. Since the logical backbone is identical and the differences are purely in citation depth, this is a granularity difference.

### 10.51
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: two rational straight lines commensurable in square only, the square on the greater exceeding the square on the lesser by a square incommensurable in length with the greater, and the greater term commensurable in length with the reference rational line, thereby forming a fourth binomial. The difference is citation depth. Heath builds the construction from lower-level propositions (10.6 for commensurability from number ratios, 10.9 for incommensurability from non-square ratios, 5.19 for convertendo), while the AI packages the same construction into the higher-level result 10.30 and uses 10.36 to conclude binomial status. The proof-tree containment test confirms this: all three heath_only citations (10.6, 10.9, 5.19) appear inside Heath's own proof of 10.30, which the AI cites as a unit. The AI also over-cites definitions (D10.1.3, D10.2.1-D10.2.4) that Heath applies implicitly. The Jaccard of 0.0 reflects this complete divergence in citation granularity, not a divergence in logical backbone.

### 10.52
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: (1) set up numbers whose ratio is not square-to-square, (2) establish two rational lines commensurable in square only via 10.6 and 10.9, yielding a binomial by 10.36, (3) use convertendo (5.19) to show the greater term's square exceeds the lesser's by the square on a line incommensurable in length with the greater term, and (4) note the lesser term is commensurable with the rational line set out, concluding a fifth binomial. The AI uses specific numbers (3 and 1) rather than Heath's general numbers, but every key intermediate conclusion appears in both proofs at the same logical position. The only citation difference is that the AI explicitly cites five definitions (D7.18, D10.1.2, D10.1.3, D10.2.4, D10.2.5) that Heath invokes implicitly, with no heath_only items. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.53
**Category**: Path difference
**Jaccard**: 0.444
**Analysis**: Both proofs share the same overall backbone: constructing rational straight lines that are commensurable in square only, showing their sum is binomial via 10.36, using ex aequali (5.22) to establish incommensurability of both terms with the rational line, and verifying the sixth binomial conditions. The decisive difference arises in Q2 when establishing that the square on the greater term exceeds the square on the lesser by the square on a line incommensurable with the greater. Heath uses convertendo (5.19) to convert the ratio AB:BC = sq(FG):sq(K), then applies 10.9 to get the incommensurability. The AI instead invokes 10.18 (the parallelogram criterion for incommensurable excess), combined with a number-theoretic argument using 7.19 about the ratio (F-G):G not being a square-number ratio. Since 5.19 does not appear inside the proof tree of 10.18, the proof-tree containment test fails, confirming a genuine path difference rather than a citation-depth difference. The AI's path through 10.18 is logically valid under Q3, as it correctly applies the parallelogram-based criterion to reach the same conclusion by a different method.

### 10.54
**Category**: Granularity difference
**Jaccard**: 0.643
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: dividing the first binomial AD at E, bisecting ED at F, applying a parallelogram to AE to obtain commensurable parts AG and GE (via 10.17), constructing two lines whose squares equal AB times AG and AB times GE respectively, showing these lines are rational and commensurable in square but incommensurable in length, and concluding binomial by 10.36. The AI cites 6.28 for the application construction and D10.1.3/D10.1.4 as definitions for rationality (over-citation), while Heath cites 6.17 for the mean proportional relationship and 10.13 for transferring incommensurability. The AI achieves the equivalent of Heath's 6.17 step through direct algebraic computation of rect(H,K) = AB times EF, and replaces Heath's 10.13 incommensurability transfer with a proof by contradiction using 10.12 and 10.15. These are differences in the depth and method of justifying individual steps, not differences in the key intermediate conclusions, making this a same-backbone, different-depth case (G).

### 10.55
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: dividing the second binomial into its terms, applying 10.17 to get commensurable parts, showing the resulting straight lines are medial and commensurable in square only, proving their rectangle is rational, and concluding by 10.37 that the side is a first bimedial. The AI's proof is a superset citation-wise (heath_only is empty), with ai_only items consisting of construction propositions (1.10), algebraic lemmas (2.1, 2.5), a mean proportional reference (6.17), additional commensurability results used for detail (10.23, 10.25), and definitions (D10.1.2, D10.1.4). These represent over-citation of the same logical steps rather than a different path. The key intermediate conclusions are identical in both proofs, making this a granularity difference.

### 10.56
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: the third binomial is decomposed per D10.2.3, the construction from 10.54 is applied, MN and NO are shown to be medial straight lines commensurable in square only, the rectangle MN,NO is shown to be medial, and therefore MO is a second bimedial by 10.38. Heath abbreviates the bulk of the argument with 'in manner similar to the foregoing' and 'let the same construction be made as before,' citing only 4 propositions (10.13, 10.21, 10.38, D10.2.3). The AI spells out the full construction and commensurability chain explicitly, citing 17 propositions including all of Heath's 4 plus 13 additional sub-step references (1.31, 2.1, 2.5, 6.1, 10.9, 10.11, 10.12, 10.15, 10.17, 10.54, D10.1.2, D10.1.3, D10.1.4). The heath_only set is empty, confirming the AI covers everything Heath cites. The ai_only items are all construction propositions, algebraic lemmas, commensurability machinery, and definitions that Heath subsumes under his abbreviations. This is Case A of Q2: same backbone, different citation depth.

### 10.57
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) the segments produced by the construction are incommensurable in length (via 10.18), (2) MN and NO/NX are incommensurable in square (via 6.1 and 10.11), (3) the sum of squares on MN and NO/NX is rational (via 10.19), (4) the rectangle MN by NO/NX is medial (via 10.13 and 10.21), and (5) therefore the whole line is major by 10.39. The AI proof is significantly more verbose and includes a false start in Steps 8-9 where it reconsiders its approach, but the final argument follows the same logical backbone as Heath. The ai_only citations (1.10, 10.36, 2.1, 2.4, 2.5, D10.1.3, D10.1.4) are all over-citations: explicit references to bisection, the definition of binomial, algebraic identities, and definitions of rational/medial that Heath uses implicitly. Heath_only is empty, confirming the AI cites a strict superset of Heath's references. This is Case A of Q2: same backbone, different citation depth.

### 10.58
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that the relevant pair of lines are incommensurable in square, that the sum of their squares is medial (via 10.21), and that the rectangle contained by them is rational (via 10.19), concluding by 10.40 that the side is the side of a rational plus a medial area. The single heath_only citation (10.13) is used by Heath to directly conclude that AB is incommensurable with AE, while the AI reaches the identical conclusion in Step 9 through a proof by contradiction using 10.12 and 10.36 -- a micro-level difference in how the same intermediate fact is established. The large ai_only set consists mostly of construction and algebraic identity propositions (1.10, 2.1, 2.4, 2.5, 6.28, D10.1.2) that the AI cites explicitly where Heath takes them as understood, plus 10.22, 10.26, and 10.36 which appear in the AI's more elaborate but equivalent argument chain. All key intermediate conclusions are the same in both proofs, making this a citation-depth difference rather than a path difference.

### 10.59
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) MN and NO are incommensurable in square, (2) the sum of the squares on MN and NO is medial (via 10.21, since AE is incommensurable in length with AB), (3) the rectangle MN by NO is medial (via 10.21, since ED is incommensurable in length with AB), (4) the sum of the squares is incommensurable with the rectangle (via 6.1 and 10.11), and (5) the conclusion follows by 10.41. The AI proof explicitly cites construction propositions (1.12, 1.31), algebraic identities (2.4, 2.5), foundational commensurability results (10.7, 10.18), a classification result (10.36), and definitions (D10.1.4, D10.2.6) that Heath's proof leaves implicit or abbreviates as 'same construction as before shown.' The heath_only set is empty, confirming the AI covers all of Heath's citations. This is a citation-depth difference with an identical logical backbone, yielding G.

### 10.60
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same backbone through the first five key intermediate conclusions: establishing that the two terms are rational commensurable in square only, that the sum-of-squares breadth is rational and commensurable with the given rational line, that the double-rectangle breadth is rational and incommensurable with it, and that the full breadth is therefore binomial. However, for the crucial sixth conclusion — that the square on the greater breadth exceeds the square on the lesser by a square commensurable with the greater — the proofs diverge substantially. Heath uses a geometric mean proportional argument (Lemma after 10.53, 6.17) to set up a rectangle equal to a fourth-part square, then invokes 10.17 to conclude commensurability. The AI instead takes an algebraic route: it uses 10.5 to express the ratio of squares as a ratio of numbers, 10.6 to establish commensurability of the sum and difference of squares, and the algebraic identity 2.5 to directly compute that EG^2 - GF^2 equals the square on a line commensurable with EG. This is a genuinely different logical backbone for the final portion of the proof, not merely a difference in citation depth. The AI's alternative path is logically sound and complete, so Q3 yields D.

### 10.61
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish identical key intermediate conclusions: (1) AC, CB are medial and commensurable in square only with rational rectangle (10.37), (2) sum of squares on AC, CB is medial, (3) the breadth DM/DH is rational and incommensurable with DE (10.22), (4) the breadth MG/HG is rational and commensurable with DE (10.20), (5) DG is binomial (10.36), (6) DM/DH > MG/HG, (7) square on DM/DH exceeds square on MG/HG by square on a line commensurable with DM/DH (10.17), and (8) the lesser term is commensurable with DE, giving a second binomial (D10.2.2). The citation differences are entirely depth-related: the AI explicitly cites construction (1.44), algebraic identities (2.4, 2.5), definitions (D10.1.2, D10.1.4), and transitivity (10.12), while Heath leaves these implicit or uses higher-level results. Heath's use of 10.21 is subsumed by the AI's citation of 10.22 (which uses 10.21 internally) and D10.1.4. Heath's use of 6.1 for parallelogram proportionality is replaced by the AI's algebraic approach reaching the same conclusions. The logical backbone is the same throughout.

### 10.62
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) AC, CB are medial and commensurable in square only with medial rectangle; (2) the sum of squares on AC, CB is medial; (3) DM is rational and incommensurable in length with DE; (4) MG/KF is rational and incommensurable in length with DE; (5) DM is incommensurable with MG/KF; (6) DG/DF is binomial; (7) sq(DM) exceeds sq(MG/KF) by the square on a line commensurable with DM; (8) neither DM nor MG/KF is commensurable with DE; (9) therefore third binomial. The ai_only citations (10.44, 10.5, 10.6, 2.4, D10.1.2, D10.1.4) are over-citations where the AI explicitly names definitions, algebraic identities, and commensurability lemmas that Heath handles implicitly or compactly. The heath_only citations (10.12, 10.23) reflect places where the AI reaches the same conclusion by a slightly different sub-route: using 10.13 twice instead of 10.12 for transitivity, and using 10.15 plus the definition of medial instead of citing the 10.23 Porism. These are citation-depth differences, not backbone differences, so the classification is G.

### 10.63
**Category**: Granularity difference
**Jaccard**: 0.615
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same key intermediate conclusions: (1) the sum of the squares on AC, CB is rational, so the corresponding breadth (DM in Heath, DH+HL in AI) is rational and commensurable with DE via 10.20; (2) twice the rectangle AC,CB is medial, so the other breadth (MG in Heath, MN in AI) is rational and incommensurable with DE via 10.22; (3) the two breadths are incommensurable with each other; (4) DG is binomial via 10.36; (5) the relevant sub-segments are incommensurable, leading via 10.18 to the square on the greater exceeding the square on the lesser by the square on a line incommensurable with the greater; (6) the greater term is commensurable with DE, yielding a fourth binomial via D10.2.4. The only substantive difference is at step 3: Heath derives DM incommensurable with MG using 10.13 (transitivity of incommensurability), while the AI derives DH+HL incommensurable with MN via 10.26 (rational area incommensurable with medial area) combined with 6.1 and 10.11. The AI's additional citations (2.4, 10.45, D10.1.3) are explicit citations of steps Heath handles implicitly or with back-references. These are citation-depth differences on the same logical backbone, not path differences.

### 10.64
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: (1) the segment corresponding to the sum of squares is rational and incommensurable with DE, (2) the segment corresponding to twice the rectangle is rational and commensurable with DE, (3) these segments are incommensurable with each other so the breadth is binomial, and (4) the square on the greater exceeds the square on the lesser by the square on a line incommensurable with the greater, with the lesser commensurable with DE, making it a fifth binomial. The AI proof explicitly works through the steps that Heath abbreviates as 'it can be proved similarly' and adds citations for algebraic identities (2.4, 2.5, 2.7), a ratio proposition (6.1), an incommensurability result (10.11), and definitions (D10.1.2, D10.2.4, D10.2.5). Heath's citation set is a proper subset of the AI's, with heath_only empty, confirming that the difference is purely one of citation depth rather than logical path.

### 10.65
**Category**: Granularity difference
**Jaccard**: 0.385
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish properties of the side of the sum of two medial areas via 10.41, (2) apply the medial areas to a rational line to get rational breadths incommensurable with the rational line via 10.22, (3) show the breadths are incommensurable with each other via 6.1 and 10.11, (4) conclude the result is binomial via 10.36, (5) show the square on the greater exceeds the square on the lesser by the square on a line incommensurable with the greater, and (6) conclude it is a sixth binomial. The heath_only set is empty, meaning the AI cites every proposition Heath does. The ai_only set contains eight additional citations (10.13, 10.18, 10.23, 10.24, 2.4, D10.1.3, D10.1.4, D10.2.6) which are all over-citations providing explicit detail for steps Heath handles implicitly or by phrases like 'similarly' and 'for the same reason.' This is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.66
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Both proofs establish identical key intermediate conclusions: (1) proportional division of the second line into terms matching the ratio of the binomial's terms, (2) commensurability in length of corresponding terms, (3) rationality of the new terms, (4) commensurability in square only of the new terms (hence binomial), (5) transfer of the excess property via 10.14, and (6) systematic verification across all six binomial orders using the same definitions D10.2.1-D10.2.6. The citation differences reflect granularity: the AI cites 10.5, 10.6, and 10.9 for explicit number-ratio and commensurability-in-square arguments where Heath uses 10.11 more directly; the AI cites 5.22 for ex aequali ratio composition where Heath uses 5.11 for ratio transitivity; the AI explicitly cites definitions D10.1.2 and D10.1.3 that Heath invokes implicitly; and for the third/sixth binomial cases, the AI uses proof by contradiction via 10.12 where Heath cites 10.13 directly. Heath cites 5.19 for the remainder-to-remainder step which the AI handles as part of the proportional division construction via 6.12. All differences are in citation depth or minor alternative justifications for the same conclusions within the same logical backbone, making this a granularity difference.

### 10.67
**Category**: Granularity difference
**Jaccard**: 0.385
**Analysis**: Q2 decided the classification as G. Both proofs share the same backbone of key intermediate conclusions: (1) dividing the bimedial AB at E and setting up the proportion CF:AE = FD:EB = CD:AB via 5.19, (2) showing CF and FD are each medial via 10.23, (3) showing CF and FD are commensurable in square only, (4) showing the rectangle CF.FD is commensurable with rectangle AE.EB, and (5) performing the same case analysis for first vs second bimedial using 10.37 and 10.38. The citation differences reflect different depths of justification for the same geometric facts: where Heath uses 5.11 (transitivity of ratios) and 5.16 (alternation of proportions) to establish the commensurability of the rectangles, the AI uses 10.5/10.6 (commensurability via number ratios), 10.12 (transitivity of commensurability), 6.23 (duplicate ratios), and 8.11 (duplicate of number-to-number ratio). The AI also explicitly cites D10.1.4 as a definition. These are all lower-level or alternative-level tools used to reach the identical key conclusions, making this a citation-depth difference rather than a path difference.

### 10.68
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same backbone of key intermediate conclusions: (1) AE, EB are incommensurable in square with sum of squares rational and rectangle medial; (2) CD is divided at F proportionally; (3) AE is commensurable with CF and EB with FD; (4) sum of squares on CF, FD is rational; (5) rectangle CF*FD is medial; (6) CF, FD are incommensurable in square; (7) CD is major by 10.39. The difference lies in the technical route used to establish these shared conclusions: Heath works through V.16 (alternation), V.18 (componendo), and VI.20 (duplicate ratio) to connect squares via ratio manipulation, while the AI uses a more direct approach via 10.11 (commensurability of sides implies commensurability of squares), 10.15/10.12 (commensurability of sums), and 6.16 (rectangle-square relationship). The ai_only citations (10.12, 10.15, 5.12, 6.12, 6.16, D10.1.3, D10.1.4) represent more explicit granularity and definitions, while the heath_only citations (5.18, 6.20) represent Heath's specific ratio-manipulation path. Since both proofs reach the same key intermediate conclusions through slightly different but parallel technical lemmas, this is a citation-depth difference rather than a path difference.

### 10.69
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) the original line decomposes into parts incommensurable in square with medial sum of squares and rational rectangle (via 10.40), (2) the commensurable line is divided proportionally, (3) the corresponding parts are commensurable, (4) the sum of squares on the new parts is commensurable with (and hence also medial as) the original sum, (5) the rectangle of the new parts is commensurable with (and hence also rational as) the original rectangle, and (6) the new parts are incommensurable in square. The only difference is citation depth: Heath summarizes the argument with 'We can then prove similarly' citing only 10.40, while the AI explicitly cites each sub-step (10.11, 10.12, 10.13, 10.15, 10.22, 10.23, 6.12, 6.16, 6.22, D10.1.4). The heath_only set is empty, confirming that the AI covers everything Heath does and more. This is a classic Case A granularity difference.

### 10.70
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same key intermediate conclusions: CF and FD are incommensurable in square, the sum of squares on CF and FD is medial (via commensurability with the sum on AE and EB), the rectangle CF by FD is medial (via commensurability with rectangle AE by EB), and the sum of squares on CF and FD is incommensurable with the rectangle CF by FD. Heath abbreviates the entire derivation with 'let the same construction be made as before' and 'we can then prove similarly,' citing only 10.41, while the AI spells out every step explicitly, citing the individual propositions used in that derivation (6.12 for proportional division, 10.11 for commensurability transfer, 6.22 for square ratios, 10.12 and 10.15 for combining commensurable magnitudes, 10.23 for mediality transfer, 6.16 for rectangle ratios, and 10.13 for incommensurability transfer). The ai_only set consists entirely of these finer-grained tools that flesh out the abbreviated argument, and heath_only is empty. This is a classic same-backbone, different-depth scenario.

### 10.71
**Category**: Granularity difference
**Jaccard**: 0.647
**Analysis**: Q2 decides this as Granularity difference (G). Both proofs share the same logical backbone: apply the rational and medial areas to a rational line EF to produce breadths, show those breadths are rational but incommensurable in length, conclude the combined line is binomial (via 10.36), then classify into four sub-cases (first/second/fourth/fifth binomial) yielding the four irrational types via 10.54/55/57/58. The only substantive difference is how incommensurability of the two breadths is established: Heath uses 6.1 (proportion of areas to breadths) and 10.11 (transfer of incommensurability through proportion), while the AI uses 10.12 (transitivity of commensurability via contradiction). Both reach the identical intermediate conclusion. The AI's additional citations of 10.9 (rational lines commensurable in square) and D10.2.3/D10.2.6 (ruling out third and sixth binomial types explicitly) are over-citations providing justification Heath leaves implicit. Since all key intermediate conclusions match and only citation depth differs, this is Case A of Q2.

### 10.72
**Category**: Granularity difference
**Jaccard**: 0.438
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: applying medial areas to a rational line to get rational breadths incommensurable with it (10.22), showing the breadths are incommensurable with each other (Heath via 6.1 then 10.11, AI via 10.11 directly), concluding the sum is binomial (10.36), narrowing to third or sixth binomial, and then applying 10.56 or 10.59 for the two cases. The AI's ai_only citations fall into two categories: (1) D10.2.1, D10.2.2, D10.2.4, D10.2.5 are explicit definition citations used to eliminate binomial types that Heath eliminates without citing the definitions, which is over-citation at a finer granularity; (2) 10.28, 10.35, 10.38, 10.41 are existence propositions used in the AI's Step 11 to argue that both cases actually arise, which is supplementary content not part of the core deductive backbone. Heath's sole unique citation 6.1 provides the proportion step (rectangles on the same base are as their breadths) that the AI handles implicitly when applying 10.11. All key intermediate conclusions match; the differences are purely in citation depth and supplementary argumentation.

### 10.73
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Q2 reveals genuinely different proof backbones, leading to classification D at Q3. Heath proves AC irrational by a direct commensurability chain: he shows sq(AB) is incommensurable with rect(AB,BC) via 10.11, establishes commensurability of sq(AB)+sq(BC) with sq(AB) via 10.15 and of 2*rect(AB,BC) with rect(AB,BC) via 10.6, then uses II.7 with 10.13 and 10.16 to conclude sq(AB)+sq(BC) is incommensurable with sq(AC), hence AC is irrational. The AI takes a fundamentally different path: it uses 10.21 to directly establish that rect(AB,BC) is medial (irrational), then employs a proof by contradiction assuming AC is rational, which would make the difference of two rational quantities (the sum of squares and sq(AC)) rational, contradicting the mediality of twice the rectangle. The key intermediate conclusions differ: Heath's backbone centers on incommensurability propagation (10.11, 10.6, 10.13, 10.16), while the AI's centers on the mediality result (10.21) and reductio. Both paths are logically complete and valid, satisfying Q3(b).

### 10.74
**Category**: Path difference
**Jaccard**: 0.133
**Analysis**: Q2 determines the classification. Heath's proof works directly with area commensurability: since sq(AB) and sq(BC) are medial while 2*rect(AB,BC) is rational, these are incommensurable, and by II.7 and X.16 the square on AC is incommensurable with the rational 2*rect(AB,BC), hence irrational. The AI takes a fundamentally different approach by introducing an auxiliary rational line rho, applying sq(AB), sq(BC), and 2*rect(AB,BC) to it to produce breadths p1, p2, and q, then showing p1+p2 and q are rational lines commensurable in square only, and applying 10.73 (the apotome proposition) to conclude the breadth (p1+p2)-q is irrational, which makes sq(AC) irrational when applied to the rational line rho. The key intermediate conclusions differ entirely: Heath never introduces an auxiliary rational line or uses apotome theory (10.73), while the AI never uses the direct incommensurability argument via X.16. This is a genuine path difference with a valid alternative proof strategy well-grounded in Book X techniques.

### 10.75
**Category**: Granularity difference
**Jaccard**: 0.471
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same backbone: set out a rational line DI, apply the sum of squares on the two medial lines to get a medial area whose breadth is rational and incommensurable with DI (via 10.22), apply twice the rectangle to get another such breadth, show the two areas are incommensurable (via the chain 10.11/10.15/10.6/10.13), conclude the breadths are incommensurable, then conclude the difference of breadths is an apotome making the remainder irrational. The AI proof is verbose with false starts but establishes all the same key intermediate conclusions as Heath. The ai_only items are definitions (D10.1.2, D10.1.3, D10.1.4), a construction proposition (2.4), an extra minor step (10.19), and a mis-citation of 10.36 (binomial) where 10.73 (apotome) was intended, though the AI correctly identifies the result as an apotome. The heath_only items (10.28 for construction reference, 10.20 for the final deduction, 10.73 for the apotome conclusion) are either handled informally by the AI or replaced by the wrong citation number while making the correct logical deduction. Since the backbones match and differences are at the citation depth level, this is a granularity difference.

### 10.76
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same key intermediate conclusions: (1) sq(AB)+sq(BC) is rational while 2*rect(AB,BC) is medial, so they are incommensurable; (2) sq(AC) is incommensurable with sq(AB)+sq(BC); (3) therefore sq(AC) is irrational and AC is irrational. The difference lies in citation depth: Heath uses 10.16 directly (incommensurable magnitudes added together give a whole incommensurable with each) with a concise 'convertendo' argument, while the AI uses 10.15 (the commensurable counterpart) in a proof by contradiction to reach the same conclusion, and also explicitly derives the mediality of 2*rect(AB,BC) via 10.6 and 10.13. The AI also cites D10.1.4 explicitly for the definition of irrational, and uses 10.12 for commensurability transitivity. These are all expansions at a finer granularity of the same logical backbone rather than a fundamentally different proof path. Heath's 10.33 is merely a construction reference cited in the setup, not a substantive proof step.

### 10.77
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: The classification is decided at Q2/Q3. Heath's proof works directly: it observes that the sum of squares on AB, BC (medial) is incommensurable with twice rect(AB,BC) (rational), then applies II.7 and X.16 to conclude that sq(AC) is also incommensurable with twice rect(AB,BC), and since twice rect(AB,BC) is rational, sq(AC) must be irrational. The AI proof takes a fundamentally different indirect approach: after establishing sq(AC) = sq(AB)+sq(BC) - 2*rect(AB,BC) via II.7, it uses proof by contradiction twice — first assuming sq(AC) is rational (deriving contradiction via 10.12 and 10.15 that the sum of squares would be rational, not medial), then assuming sq(AC) is medial (deriving contradiction via 10.26 that a medial area cannot exceed a medial area by a rational area). These are different key intermediate conclusions (direct incommensurability argument vs. elimination-by-contradiction of rational and medial cases), constituting a genuine path difference. The AI's indirect path is logically sound throughout, so the classification is D.

### 10.78
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Both proofs share the same backbone through four key intermediate conclusions: setting up areas on a rational line DI, establishing that the breadths DG and DH (or DF) are rational and incommensurable in length with DI (via X.22), showing DG is incommensurable with DH/DF (via VI.1 and X.11), and concluding that the difference HG/FG is an apotome (via X.73). However, the proofs diverge at the final step of establishing irrationality. Heath directly applies a deduction from X.20 (that the rectangle of a rational line and an apotome is irrational) to conclude AC is irrational. The AI instead takes an independent indirect route in Steps 10-14, proving by contradiction that the square on AC is neither rational (using 10.26, that a medial area does not exceed a medial area by a rational area) nor medial (using 10.36, that the sum of two rational lines commensurable in square only is a binomial, which contradicts DG being rational). These additional intermediate conclusions (square on AC is not rational, square on AC is not medial) are substantive facts argued by the AI but entirely absent from Heath, causing Case A of Q2 to fail. Under Q3, the AI's different path is logically valid, so the classification is D.

### 10.79
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: The classification is decided at Q2 (Case A). Both proofs share the same logical backbone: they set up the apotome AB with annex BC, assume a second annex BD, apply II.7 to both decompositions to show that the difference of the sums of squares on the two pairs equals the difference of the doubled rectangles, note that the sums of squares are rational while the doubled rectangles are medial (by 10.21), and reach a contradiction via 10.26 (a medial area cannot exceed a medial area by a rational area). The AI proof then adds an extended argument (Steps 11-18) showing CB = DB directly by forcing both sides of the equation to zero and using 2.1 to derive an algebraic contradiction, but this is supplementary elaboration beyond the shared core contradiction argument. Heath_only is empty, confirming the AI covers all of Heath's citations. The ai_only items (10.12, 10.13, 10.15, 10.23, 10.6, 2.1, common notions, and definitions) represent explicit expansion of steps Heath handles more tersely, plus the additional algebraic argument. The shared backbone and the nature of the extra citations as depth expansions yield a granularity difference.

### 10.80
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this classification as G (Granularity difference). Both proofs share the same logical backbone: they assume a second annex DB exists, apply II.7 (2.7) to equate the excess of sums of squares with the excess of twice the rectangles, show the rectangle side is rational and the sum-of-squares side is medial, then invoke 10.26 (medial cannot exceed medial by rational) to reach a contradiction. The citation differences are attributable to depth: Heath cites 10.23 to establish that the sums of squares are medial, while the AI derives the same conclusion via 10.13 and 10.15; the AI also explicitly cites common notions (CN1, CN2, CN3), a definition (D10.1.4), and 10.12 which Heath leaves implicit. The AI additionally extends the proof beyond the contradiction (Steps 11-14, using 2.4) to explicitly derive BC=BD, but this does not change the core backbone. All ai_only items are either over-citations of implicit steps or sub-lemmas reaching the same intermediate conclusions as Heath, confirming Case A of Q2.

### 10.81
**Category**: Path difference
**Jaccard**: 0.350
**Analysis**: Q2 revealed genuinely different backbones, leading to classification via Q3. Heath's proof reduces the uniqueness problem to the structure of apotomes: after setting up rectangles on a rational line EF, Heath shows EM and HM are rational and commensurable in square only, concluding EH is an apotome (10.73) with HM as annex, then similarly shows HN is also an annex, contradicting the uniqueness of apotome annexes (10.79). The AI takes a fundamentally different algebraic approach: after the same initial setup, it equates the two decompositions of sq(AB) via II.7, then uses 10.26 (a medial area does not exceed a medial area by a rational area) combined with the incommensurability of the sum-of-squares and twice-rectangle medial areas to force the difference of the two decompositions to be zero, and then algebraically deduces AC=AD and CB=DB using identities involving 6.17. The heath_only propositions 10.73 and 10.79 are central to Heath's apotome-based strategy and have no counterpart in the AI proof; conversely, the AI's use of 10.26 and 6.17 for direct algebraic equality has no counterpart in Heath. The AI's path is logically valid under Q3(b), making this a path difference.

### 10.82
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: assume a second annex BD exists with the same properties as BC, show that the excess of the sums of squares on AD,DB over AC,CB equals the excess of twice the rectangles, conclude the excess is rational (since both sums of squares are rational), then derive a contradiction via 10.26 because both double-rectangles are medial and a medial area cannot exceed a medial area by a rational area. The AI proof takes a more algebraically explicit route, expanding expressions using 2.3 and 2.4, and justifying that the difference of two rational areas is rational using 10.12, 10.15, D10.1.3, and CN3. Heath states these same facts more concisely without citing these supporting propositions. All ai_only citations (2.3, 2.4, 10.12, 10.15, CN3, D10.1.3) are over-citations that fill in details Heath leaves implicit, while heath_only is empty. The key intermediate conclusions are identical in both proofs, making this a citation-depth difference.

### 10.83
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath's proof derives the contradiction in a few lines: the excess of the sums of squares equals the excess of the double rectangles; the latter difference is rational (both are rational), so the former is rational; but both sums of squares are medial, and by 10.26 a medial area cannot exceed a medial area by a rational area. The AI proof shares the setup (10.77) and does invoke 10.26 to note that medial areas cannot differ by a rational amount, but instead of directly equating the two excesses (as Heath does by reference to preceding cases), the AI embarks on a 30-step detour analyzing commensurability relationships using 2.7, 2.5, 2.6, 10.11, 10.12, 10.13, 10.15, 10.19, 10.20, 10.21, and 10.23, ultimately reaching a contradiction through 10.19 and 10.21 (that the rectangle on AB and BC-BD cannot be rational regardless of whether the lines are commensurable in length or in square only). The key intermediate conclusions forming the backbone are fundamentally different: Heath uses a direct algebraic identity relating the two excesses, while the AI constructs an elaborate commensurability argument through multiple intermediate results. Both proofs are logically complete, so this is a valid different path (D).

### 10.84
**Category**: Path difference
**Jaccard**: 0.667
**Analysis**: Both proofs share the same initial backbone: assuming two annexes BC and BD satisfying 10.78 conditions, constructing areas on a rational line EF, establishing that the relevant breadths are rational and incommensurable in length with EF (10.22), that corresponding breadths are incommensurable with each other (6.1, 10.11), and that the resulting breadths form apotomes (10.73). The divergence occurs at the final contradiction step. Heath identifies EH as an apotome with two different rational annexes HM and HN, then invokes 10.79 (to an apotome only one rational line can be annexed commensurable in square only) for the contradiction. The AI instead takes a longer route through Steps 11-22, using 10.26 (a medial area does not exceed a medial area by a rational area) and 10.47 (the side of the sum of two medial areas is divided at one point only, invoked as a structural analogy for the subtractive case) to argue that sq(AC) must equal sq(AD), forcing BC = BD. This is a genuinely different logical path to the same conclusion -- the AI replaces Heath's single-step apotome-uniqueness argument (10.79) with an extended area-difference argument using different propositions (10.26, 10.47). Q2 Case B applies since the final contradiction mechanism constitutes a different backbone conclusion, and Q3 confirms the AI's path is valid under the hardened standard.

### 10.85
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). The AI proof invokes Proposition 10.29 as a single unit to obtain two rational straight lines BG and GC that are commensurable in square only, with the square on BG greater than the square on GC by the square on a line commensurable in length with BG. Heath's proof constructs these lines from scratch using square numbers and explicitly applies 10.6 (twice for commensurability from number ratios), 10.9 (for incommensurability in length and commensurability via square-number ratios), and 5.19 (convertendo). The proof-tree containment test confirms that all three heath_only items (10.6, 10.9, 5.19) appear inside Heath's own proof of 10.29, meaning the AI is citing a higher-level result as a package while Heath re-derives its internals inline. Both proofs reach the same key intermediate conclusions (BC is an apotome via 10.73, BG commensurable in length with A, and the first apotome conditions of D10.3.1 are satisfied), differing only in the depth at which the construction is cited.

### 10.86
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they construct two rational straight lines commensurable in square only, apply 10.73 to obtain an apotome, show that the square on the larger exceeds the square on the smaller by the square on a line commensurable in length with the larger, and verify that the annex is commensurable with the given rational line to conclude it is a second apotome. The sole substantive citation difference is that Heath uses 5.19 (convertendo) to derive that sq(BG):sq(H) = DE:EF, while the AI reaches the same conclusion through direct arithmetic with specific numbers (4k - 3k = k, so sq(FG):sq(L) = 4:1), citing 1.47 and CN3 instead. The ai_only items (1.3, 1.47, CN3, CN5, D10.1.3, D10.1.4, P1) are construction steps, common notions, and definitions that Heath leaves implicit, confirming a citation-depth difference rather than a path divergence.

### 10.87
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) FG is rational and incommensurable in length with A, (2) GH is rational and incommensurable in length with FG, (3) FG and GH are commensurable in square only so FH is an apotome via 10.73, (4) A is incommensurable in length with GH via ex aequali (5.22), and (5) the square on FG exceeds the square on GH by the square on a line commensurable with FG. The citation differences are all citation-depth matters: the AI explicitly cites 10.12 for transitivity of commensurability (Heath uses the same reasoning implicitly), D10.1.3 for the definition of rational (Heath invokes the concept without citing the definition), and 5.17 (separando) combined with inversion and 5.22 instead of Heath's direct use of 5.19 (convertendo). Since 5.17 appears inside Heath's proof of 5.19, the AI is effectively re-deriving convertendo from its components rather than citing the composite result. All backbone conclusions match, making this Case A under Q2: same backbone, different citation depth.

### 10.88
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same key intermediate conclusions: (1) BG is rational and commensurable in length with A, (2) BG and GC are rational and commensurable in square only, (3) BC is an apotome by 10.73, (4) the square on BG exceeds the square on GC by the square on a line incommensurable with BG, and (5) BC is therefore a fourth apotome by D10.3.4. The divergence lies entirely in citation depth: the AI invokes 10.30 as a single high-level proposition to construct BG and GC with the needed properties, whereas Heath re-derives those properties inline using 10.6 (ratio-to-commensurability), 10.9 (square ratio to length incommensurability), and 5.19 (convertendo). The proof-tree containment test confirms that all three heath_only items (10.6, 10.9, 5.19) appear inside Heath's own proof of 10.30, so the AI is citing 10.30 as a unit while Heath unpacks its internals. The AI's additional citations of D10.1.3 and 10.13 are minor over-citations that do not alter the logical backbone.

### 10.89
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: they set out a rational line A with CG commensurable in length with A, construct numbers DF and FE such that DE has not to either the ratio of a square number to a square number, establish the ratio FE:ED = sq(CG):sq(BG), prove BG is rational and incommensurable in length with GC (making BC an apotome via 10.73), then use convertendo reasoning to show the square on BG exceeds the square on GC by a square incommensurable in length with BG, and finally classify the result as a fifth apotome since the annex CG is commensurable with A. The sole heath_only citation 5.19 (convertendo) is explicitly invoked by the AI in Step 6 using the word 'convertendo' and the same algebraic manipulation, but the AI cites 5.16 (alternando) instead. The ai_only items are definitions (D10.1.3, D10.1.4, D10.3.4), a common notion (CN5), and elaborating propositions (10.11, 10.13, 10.30, 5.16) that make explicit what Heath leaves implicit. This is a clear case of same backbone with different citation depth.

### 10.90
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determines the classification. Heath constructs FG and GH from number ratios using 10.6, then establishes their properties (rationality, incommensurability) step by step using 10.9, derives chain results via ex aequali (5.22) and convertendo (5.19), and finally classifies the apotome. The AI takes a fundamentally different approach: it invokes 10.30 directly to obtain two rational lines commensurable in square only with the required square-difference property, uses 10.10 to ensure both are incommensurable in length with A, and then verifies the sixth apotome conditions from D10.3.6. While three of the four heath_only citations (10.6, 10.9, 5.19) appear inside Heath's proof of 10.30, the AI also introduces 10.10 (not used by Heath) and bypasses the ex aequali argument (5.22) entirely because the construction via 10.30+10.10 yields the incommensurability properties directly. This constitutes a genuinely different logical backbone rather than a mere citation-depth difference. The AI's path is logically complete under Q3: every step from construction through classification follows validly.

### 10.91
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decides this classification as Case B (different backbone), leading to Q3 which confirms a valid different path (D). Both proofs begin identically by setting up the first apotome AD with annex DG and applying a parallelogram construction via 10.17. However, the proofs diverge fundamentally in how they construct the 'side' of the area. Heath constructs auxiliary squares LM and NO about the same diameter (using 6.26), then uses a mean proportional argument (Lemma after 10.53, 5.11) to show LN is the side and an apotome. The AI instead works directly with lines p and q defined by p^2 = AC*AH and q^2 = AC*HG, uses algebraic identities (2.5, 2.7) to show p^2+q^2 is rational and 2pq is medial, proves p and q are rational and commensurable in square only via a contradiction argument, and shows (p-q)^2 = AB via 2.7. The heath_only citations (10.53/Lemma, 5.11, 6.26) belong entirely to Heath's geometric square construction which the AI avoids completely, while the ai_only citations (2.5, 2.7, 10.20, 10.26, 10.9, 6.28, D10.1.3, D10.1.4) support the AI's more algebraic approach. The AI's chain from premises to conclusion is logically complete under Q3(b).

### 10.92
**Category**: Granularity difference
**Jaccard**: 0.348
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they set up the second apotome AD with annex DG using D10.3.2, bisect DG at E, apply 10.17 to obtain commensurable segments AF and FG, establish that the sub-rectangles with AC are medial (10.21), show that the cross-product rectangle is rational (10.19), and conclude via 10.74 that the side is a first apotome of a medial straight line. The citation differences reflect different construction techniques rather than different logical paths: Heath uses a geometric square-and-gnomon construction (6.26, 6.17, 5.11) while the AI uses algebraic identities (2.1, 2.5) and a proof by contradiction for incommensurability in length (10.24, 10.26). Heath cites 10.73 for the apotome definition where the AI uses D10.3.2 directly, and Heath uses 10.13 for commensurability transfer where the AI cites 10.12 and related results. Since the key intermediate conclusions are the same in both proofs and only the depth and method of establishing them differ, this is a granularity difference.

### 10.93
**Category**: Granularity difference
**Jaccard**: 0.368
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they set up the third apotome AD with whole AG and annex GD, bisect GD, apply 10.17 to obtain commensurable parts, establish that the resulting rectangular areas (formed with the rational line AC) are medial, show the components are medial lines commensurable in square only that contain a medial rectangle, and conclude via 10.75 that the side is a second apotome of a medial straight line. The AI avoids Heath's explicit geometric construction of squares LM and NO sharing a diameter (which requires 6.26) and the mean proportional chain (requiring 5.11 and 6.17), instead working algebraically with r and s where r-squared equals AC times AH and s-squared equals AC times HG. The AI cites 10.5, 10.6, 6.28, and several definitions (D10.1.2, D10.1.3, D10.1.4) that Heath does not, while Heath cites 10.13, 5.11, 6.17, and 6.26 that the AI does not. These differences reflect citation depth and constructive technique rather than different key intermediate conclusions, placing this squarely in the granularity-difference category.

### 10.94
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish the properties of the fourth apotome AD with annex DG, show AF is incommensurable with FG via 10.18, prove rect(AC,AG) is rational via 10.19 and rect(AC,DG) is medial via 10.21, then construct two quantities whose squares sum to a rational area, whose double rectangle is medial, and which are incommensurable in square, concluding by 10.76 that the side is minor. The difference lies in citation depth: Heath uses a geometric construction with squares LM and NO about the same diameter (6.26), the gnomon, and a mean proportional chain (5.11) to establish the area relationships, while the AI uses an algebraic approach with lines p and q, direct area computation via 6.17, and the identities 2.5 and 2.7. The AI also over-cites with 10.13, 6.28, D10.1.3, and D10.1.4. The heath_only citation 6.26 is contained within the proof of 6.28 which the AI cites, and 5.11 is bypassed by the AI's direct algebraic proportional reasoning. All key intermediate conclusions are the same in both proofs, making this a granularity difference rather than a path difference.

### 10.95
**Category**: Path difference
**Jaccard**: 0.227
**Analysis**: Q2 determined the classification. Both proofs start from the definition of the fifth apotome (D10.3.5) and ultimately establish the same final conditions for invoking 10.77: the two component straight lines are incommensurable in square, their sum of squares is medial, and twice their rectangle is rational. However, the intermediate paths diverge significantly. Heath uses the standard rectangle construction with bisection (10.18), establishes that AK is medial (10.21) and DK is rational (10.19), constructs squares about the same diameter (6.26), and directly reads off the properties. The AI instead uses algebraic decomposition (2.7, 2.1) to break down the areas, applies them to the rational line AC to get breadths SN and NQ, establishes their properties using 10.15, 10.20, 10.22, 10.23, 10.26, and then invokes the semicircle construction method (referencing 10.94 and 2.14) to find the component straight lines. The AI's use of the semicircle method and algebraic area decomposition replaces Heath's parallelogram-about-the-same-diameter construction (6.26), representing a genuinely different backbone. The proof-tree containment test confirms this: 6.26 (heath_only) is not subsumed by any single AI citation but rather replaced by an entirely different construction approach. Under Q3, the AI's path is logically sound though terse in Steps 10-12, satisfying the lenience rule.

### 10.96
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G. Both proofs establish the same key intermediate conclusions: (1) the sixth apotome's whole and annex are rational and commensurable in square only, (2) the parallelogram construction via 10.18 divides the whole into incommensurable parts, (3) two constructed straight lines are produced whose squares sum to AC times AE, (4) the sum of those squares is medial via 10.21, (5) twice the rectangle of those lines is medial via 10.21, (6) the sum of squares is incommensurable with twice the rectangle, (7) the lines are incommensurable in square, and (8) 10.78 yields the final classification. The difference lies in construction method: Heath uses 6.26 (squares about the same diameter) for a geometric construction, while the AI constructs the lines algebraically using 2.5, 2.7, 3.31, 6.8, and makes explicit use of 10.7 and definitions D10.1.3, D10.1.4. These ai_only items are construction-level or definitional references that serve the same logical purpose as Heath's geometric approach, making this a citation-depth difference rather than a backbone difference.

### 10.97
**Category**: Granularity difference
**Jaccard**: 0.280
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: they decompose the square on the apotome into rational and medial areas applied to the rational line CD, show the resulting breadth is an apotome (via X.73), then verify the first apotome conditions (D10.3.1) through a mean proportional argument and commensurability of parts. The key intermediate conclusions match at every stage. The two heath_only citations (10.11 and 10.17) represent citation-depth differences rather than backbone divergences: where Heath uses 10.11 to transfer incommensurability through a proportion, the AI uses 10.13 to reach the same conclusion (CG incommensurable with GE) via a different sub-step; where Heath invokes 10.17 as a single unit to conclude sq(CM) > sq(MF) by a commensurable square, the AI re-derives the same conclusion directly in Steps 10-16 using ratio-of-numbers arguments (5.17, 5.18, 10.5, 10.6, 2.4). The large ai_only set (16 items) consists predominantly of definitions (D10.1.2, D10.1.3, D10.1.4), common notions (CN5), and sub-lemma propositions (10.12, 10.15, 10.21, 10.23, 10.5, 10.6, 2.14, 2.4, 5.17, 5.18, 6.20) that the AI cites explicitly where Heath leaves them implicit, confirming a granularity difference.

### 10.98
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) decompose sq(AB) into areas applied to the rational line CD, (2) show the whole breadth (CM/CL+FL) is rational and incommensurable with CD, (3) show the annex breadth (FM/MN) is rational and commensurable with CD, (4) conclude these are rational commensurable in square only so the result is an apotome by 10.73, (5) verify the second-apotome conditions (sq on whole > sq on annex by commensurable square, annex commensurable with CD). The citation differences reflect different technical tools used at the same logical positions: the AI uses 10.13 (transitivity of incommensurability) where Heath uses 6.1 and 10.11 to establish the incommensurability between whole and annex; the AI uses 10.14 (transfer of commensurability through proportion) to verify the greater-by-commensurable-square condition, while Heath explicitly constructs a mean proportional using 5.11 and 6.17; Heath uses 10.23 to establish that the sum of squares is medial while the AI handles individual medial areas. The proof-tree containment test shows 5.11 and 6.17 are not inside 10.14, but both sets of tools serve to establish the identical sub-conclusion about the second-apotome condition, making this a same-backbone difference in citation depth and technique, not a different logical path.

### 10.99
**Category**: Granularity difference
**Jaccard**: 0.643
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they apply the square on the second apotome of a medial to a rational line, decompose it into breadths corresponding to the squares on the components and twice their rectangle, establish that these breadths are rational and incommensurable with the rational line, show they are incommensurable with each other to conclude the result is an apotome, and then determine it is specifically a third apotome by verifying the commensurability condition on the excess and that neither breadth is commensurable with the rational line. The citation differences (ai_only: 10.14, D10.1.3; heath_only: 10.17, 10.23, 5.11) reflect different tools used to reach the same intermediate conclusions at the same logical positions. Heath uses a mean-proportional argument (5.11) and parallelogram application (10.17) to establish that sq(CM) > sq(MF) by the square on a commensurable line, while the AI uses 10.14 (transfer of commensurability across proportionals) for the same conclusion. D10.1.3 is mere over-citation of a definition, and 10.23 is a supporting result Heath uses for establishing mediality that the AI handles more tersely. All key intermediate conclusions are present in both proofs, satisfying Case A of Q2.

### 10.100
**Category**: Granularity difference
**Jaccard**: 0.381
**Analysis**: Both proofs share the same backbone of key intermediate conclusions: (1) decompose the minor into AG, GB with properties from 10.76, (2) apply the sum of squares and twice the rectangle to the rational line CD to obtain rational segments CM/DK and FM/KE with the appropriate commensurability and incommensurability properties via 10.20 and 10.22, (3) conclude the breadth is an apotome via 10.73, (4) establish the fourth apotome condition that the square on the whole exceeds the square on the annex by a square on a line incommensurable with the whole via 10.18, and (5) conclude fourth apotome by D10.3.4. The citation differences are all at the sub-step level: Heath uses 10.11 for proportionality transfer of incommensurability where the AI uses 10.13 for transitivity of incommensurability; Heath uses the geometric mean proportional approach (5.11, 6.17) to set up the application of 10.18, while the AI uses an algebraic identity approach (2.5, 2.6, 5.15); and the AI over-cites definitions (D10.1.1, D10.1.4) and auxiliary results (10.23, 10.6, CN1). Since all key intermediate conclusions are the same and the differences are in citation granularity and alternative sub-routes to identical intermediate results, Q2 Case A applies, yielding G.

### 10.101
**Category**: Granularity difference
**Jaccard**: 0.727
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that AG, GB are incommensurable in square with medial sum of squares and rational twice-rectangle (10.77), construct rectangles on CD to get breadths CL and FL, show CL is rational and incommensurable with CD (10.22) while FL is rational and commensurable with CD (10.20), deduce CL is incommensurable with FL making CF an apotome (10.73), then show CH is incommensurable with KL leading via 10.18 to the conclusion that CF is specifically a fifth apotome (D10.3.5). The citation differences are purely about how intermediate steps are justified: Heath uses VI.1 (6.1) to convert area relationships to length ratios and then X.11 for incommensurability transfer, while the AI uses 10.13 (transitivity of incommensurability) directly to reach the same conclusion that CL is incommensurable with FL. The AI also explicitly cites 10.9 for the square-number ratio argument that Heath leaves implicit. These are citation-depth differences for identical key intermediate conclusions, placing this squarely in Case A of Q2 as a granularity difference.

### 10.102
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Heath's proof directly decomposes the squares on AG and GB and twice their rectangle, applies them to CD, uses 10.73 to establish CF as an apotome, then verifies the sixth apotome conditions via 10.18 and D10.3.6. The AI takes a fundamentally different path: it first applies sq(BG) to CD to obtain a sixth binomial CF via 10.65, then decomposes this binomial to show that the breadth CE for sq(AB) satisfies the conditions of a sixth apotome (D10.3.6). The AI's route through the sixth binomial (10.65) and related results (10.84, 10.96, 10.42) represents a genuinely different backbone from Heath's direct approach via 10.73 and 2.7. The heath_only citations (10.73, 2.7) are not contained in any single higher-level AI citation but represent independent logical steps in Heath's alternative route. The AI proof, while verbose and meandering through 33 steps with multiple reorganizations, does establish a complete logical chain from premises to conclusion and passes the Q3 validity check under the hardened 1(b) standard.

### 10.103
**Category**: Granularity difference
**Jaccard**: 0.412
**Analysis**: Q2 decided this classification. Both proofs establish the same key intermediate conclusions: (1) setting up a proportion to construct corresponding parts of the new apotome, (2) showing CF and FD are rational and commensurable in square only, (3) transferring the excess-of-squares condition via 10.14, and (4) transferring the commensurability-with-rational-line condition via 10.12/10.13. The difference lies in construction direction: Heath starts from the annex (BE:DF = AB:CD) and extends to the whole using 5.12, while the AI starts from the whole (AG:CF = AB:CD) and derives the annex using 5.19 (separando) and 5.11 (transitivity). This is a minor variation in how the same proportionality is established, not a different logical backbone. The AI's additional citations of definitions D10.1.3 and D10.3.1-D10.3.6 are explicit references to what Heath leaves implicit. Since the backbone conclusions are identical and the citation differences reflect construction-direction variation and explicit definition citation, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.104
**Category**: Path difference
**Jaccard**: 0.214
**Analysis**: Q2 determines the classification. Heath's proof works directly with the annex segments of the apotome of a medial straight line, using ratio properties (6.12, 5.12, 5.16) and commensurability transfers (10.11, 10.13, 10.23) to show that the commensurable line CD has components that are medial and commensurable in square only, then uses the rational-vs-medial rectangle distinction (D10.1.4) to establish same order. The AI proof takes a fundamentally different approach: it introduces an auxiliary rational line, applies the squares of both lines to it as areas, uses 10.98/10.99 to convert apotomes of medial into plain apotomes (second or third), uses 10.103 to transfer the apotome type via commensurability, then uses 10.92/10.93 to convert back. The key intermediate conclusions are entirely different -- Heath never applies areas to a rational line and the AI never works with the annex segments directly. The Jaccard similarity of 0.214 with five substantive AI-only citations and six substantive Heath-only citations confirms the divergence. The AI's path is logically complete and valid in both cases (first and second apotome of medial), so Q3 yields D.

### 10.105
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decides this classification as G (Granularity difference). Both proofs establish the same four key intermediate conclusions: (1) CF, FD are incommensurable in square, (2) the sum of squares on CF, FD is rational, (3) the rectangle CF.FD is medial, and (4) CD is minor by 10.76. The citation differences reflect depth rather than path divergence. Heath uses 10.13 to transfer incommensurability, but 10.13 itself depends on 10.12 (which the AI cites directly), making this a citation-depth difference. Heath uses 5.16 (alternation) to set up ratios, while the AI uses 6.12 (fourth proportional construction) and 6.16 (rectangle-proportion equivalence) to achieve the same proportional relationships. The AI additionally cites 10.82 (uniqueness of decomposition) and 10.6, which are over-citations not present in Heath but do not change the logical backbone. Since both proofs reach the same intermediate conclusions through arguments of different granularity, this is a granularity difference.

### 10.106
**Category**: Granularity difference
**Jaccard**: 0.083
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs establish the same key intermediate conclusions: dividing CD in the same ratio as the components of AB, proving the new components are incommensurable in square, proving the sum of their squares is medial, and proving their rectangle is rational. Heath's proof accomplishes this by saying 'in manner similar to the foregoing' and citing only 10.77, while the AI proof explicitly spells out every sub-step with detailed citations (10.5, 10.6, 10.11, 10.12, 10.13, 10.15, 10.23, 10.83, 6.16, D10.1.2, D10.1.4). The heath_only set is empty and all ai_only items are sub-steps supporting the same backbone conclusions, making this a clear case of different citation depth with identical logical structure.

### 10.107
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3. Heath's proof works directly with the geometric decomposition: it decomposes AB into AE and EB (characterized by 10.78), transfers the three defining properties (sum of squares medial, rectangle medial, sum of squares incommensurable with rectangle) to the corresponding parts CF, FD of CD via commensurability, and reassembles to conclude CD produces with a medial area a medial whole. The AI proof takes an entirely different indirect route via apotome classification: it applies the square on AB to a rational line to obtain a sixth apotome (10.102), shows the corresponding breadth for CD is commensurable and hence also a sixth apotome (10.103), then reverses via 10.96 to conclude CD has the desired property. The Jaccard similarity is 0.0, reflecting completely disjoint citation sets. The key intermediate conclusions differ fundamentally (Heath: transfer of three geometric properties between decomposed parts; AI: classification and transfer of apotome order), confirming Case B (different backbone) at Q2. The AI's path is logically complete under Q3, with each step properly supported by cited propositions, yielding classification D.

### 10.108
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: apply the rational and medial areas to a rational straight line to obtain breadths p and q (rational, commensurable and incommensurable in length with the rational line respectively), establish their incommensurability in length via 10.13, conclude they are rational commensurable in square only so p-q is an apotome by 10.73, then split into two cases (first apotome yielding an apotome side via D10.3.1 and 10.91, fourth apotome yielding a minor side via D10.3.4 and 10.94). The AI proof is strictly a superset in citations, adding 10.12, 10.21, D10.1.3, and D10.1.4 as explicit justifications for steps Heath leaves implicit (transitivity of commensurability, the definition of medial area, and the definition of rational lines). Since heath_only is empty and the ai_only items are all foundational or definitional over-citations that do not alter the logical backbone, this is a granularity difference.

### 10.109
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: apply the medial and rational areas to a rational straight line, establish that the resulting breadths are rational and commensurable in square only, conclude the difference is an apotome (10.73), then split into two cases based on whether the excess of squares is by a commensurable or incommensurable line, yielding a second apotome (leading to a first apotome of a medial via 10.92) or a fifth apotome (leading to a line producing with a rational area a medial whole via 10.95). The AI proof cites 10.20 and 10.22 explicitly to justify why the breadths have their commensurability properties, and cites definitions D10.1.3 and D10.1.4, whereas Heath states these properties as immediate consequences without explicit citation. Since heath_only is empty and all ai_only items (10.20, 10.22, D10.1.3, D10.1.4) are supporting citations for steps present in both proofs at the same logical position, this is a citation-depth difference under Q2 Case A, yielding G.

### 10.110
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establishing that the breadths obtained by applying medial areas to a rational line are rational and incommensurable with that line (via 10.22), (2) showing these breadths are incommensurable with each other (from incommensurability of the areas), (3) concluding the breadths are rational and commensurable in square only so their difference is an apotome (10.73), and (4) splitting into two cases based on whether the excess square is commensurable or incommensurable, yielding a third apotome leading to a second apotome of a medial (10.93) or a sixth apotome leading to a line producing with a medial area a medial whole (10.96). The citation differences are granularity-level: Heath cites 6.1 and 10.11 to transfer incommensurability from areas to breadths, while the AI handles this via a direct proportion argument and instead adds 10.12 and 10.21 for extra detail; the AI also cites additional definitions (D10.1.3, D10.3.1, D10.3.2, D10.3.4, D10.3.5) to explicitly eliminate non-applicable apotome orders, which is extra rigor not present in Heath but does not alter the backbone.

### 10.111
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 decided this classification. Heath's proof applies the square on AB to a rational line DC, producing a breadth DE that is simultaneously a first apotome (by 10.97) and a first binomial (by 10.60), then uses the definitional properties (D10.2.1, D10.3.1) and commensurability results (10.12, 10.15, 10.13) to show a segment EG would be both an apotome and rational, a contradiction. The AI takes a fundamentally different path: it decomposes AB directly as a sum (binomial via 10.36) and a difference (apotome via 10.73) of rational lines, expands sq(AB) two ways using algebraic identities (2.4, 2.7), shows the resulting equation forces a sum of two medial areas (established via 10.21, 10.6) to equal a rational area, applies these areas to a rational line to produce breadths (using 10.20, 10.22), and derives contradictions in both exhaustive sub-cases about the commensurability properties of those breadths. The two proofs share no key intermediate conclusions: Heath works through first apotome/binomial classification of the applied breadth, while the AI works through algebraic expansion and medial-versus-rational area analysis. Both approaches are logically complete, making this a genuine path difference.

### 10.112
**Category**: Path difference
**Jaccard**: 0.139
**Analysis**: The AI proof takes a fundamentally different path from Heath's. Heath constructs an elaborate proportion-based argument using segments HK, KF, KE and Book V proportion results (5.11, 5.12, 5.14, 5.16, 5.17) along with VI.16, VI.22, and X.11 to directly establish that EF is an apotome with the required properties. The AI instead uses an algebraic identity approach: it shows that sq(AC) - sq(CB) is rational via 10.12/10.15, establishes AC - CB is an apotome via 10.73, proves FG is commensurable in length with AC - CB through 2.1, 6.1, 10.5, and 10.6, then leverages 10.103 (a line commensurable with an apotome is an apotome of the same order) to transfer the apotome classification and order to FG. The backbones differ at Q2: Heath's key intermediates are proportion-derived segment properties while the AI's key intermediate is commensurability of FG with the apotome AC - CB. Both paths are logically valid, so Q3 yields D.

### 10.113
**Category**: Path difference
**Jaccard**: 0.242
**Analysis**: Q2 decided the classification. Heath constructs the binomial directly through a geometric proportion construction: setting up G via BC*G = A^2, making KE = G, using convertendo (5.19) to derive BC:CD = KH:HE, then constructing point F via the proportion KH:HE = HF:FE, and through a chain of proportion results (5.11, 5.16, V.Def.9) establishing that KF and FH are rational commensurable in square only, yielding KH as binomial. The AI takes a fundamentally different approach: it defines p and q by rho^2 = a*p and rho^2 = b*q, shows they are rational and commensurable in square only (via 10.13 and 10.20), establishes q+p as binomial (10.36), then crucially uses 10.112 (the converse proposition, which applies a rational square to a binomial to produce an apotome) to identify w = q+p by showing that applying rho^2 to the binomial q+p produces exactly the apotome AB. The AI also uses 10.112 for order matching rather than Heath's direct argument via 10.14. The AI never constructs Heath's key intermediate point F or uses the convertendo-based proportion chain. These constitute genuinely different logical backbones, making this a path difference. The AI's path is logically valid: 10.112 is a previously proved proposition, and the uniqueness argument for w = q+p is sound.

### 10.114
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) construct an apotome F/KL via 10.112 whose terms are commensurable with the binomial's terms, (2) establish ratio equalities among the terms, (3) derive that AB is commensurable with F/KL, (4) use 6.1 to relate the rectangle areas, (5) conclude commensurability with a rational square, hence the side is rational. The heath_only citation 5.19 passes the proof-tree containment test: the AI cites 5.17 and 5.11, both of which appear inside Heath's proof of 5.19, meaning the AI re-derives 5.19's internals inline rather than citing it as a unit. The ai_only citations 10.5 and 10.6 provide a more explicit route to commensurability propagation where Heath uses 10.11 directly; CN1 and D10.1.4 are over-citations of a common notion and definition. All differences are matters of citation depth, not different logical paths.

### 10.115
**Category**: Path difference
**Jaccard**: 0.028
**Analysis**: Q2 determined the classification. Heath's proof generates infinitely many irrationals by a simple iterative construction: given medial A and rational B, form C where C^2 = B*A (making C irrational by Def.4 and deduction from 10.20), then D where D^2 = B*C, and so on ad infinitum. The AI takes a fundamentally different approach: it systematically constructs all 13 types of irrational lines from Book 10 (binomial, apotome, first bimedial, second bimedial, major, minor, etc.) from the medial line A, proves they are mutually distinct using propositions 10.42-10.47, 10.79-10.84, and 10.111, and then argues the process can be repeated from each new irrational to generate infinitely many. These are entirely different logical backbones: Heath never constructs binomials, bimedials, or apotomes, and the AI never uses Heath's iterative rectangle construction. The AI's path is logically valid under the hardened 1(b) standard, making this a genuine path difference (D).


## Book 11

| Category | Count |
|---|---|
| Perfect match (P) | 1 |
| Granularity difference (G) | 26 |
| Path difference (D) | 11 |
| AI proof error (E) | 1 |

**Total**: 39 propositions

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
**Category**: Granularity difference
**Jaccard**: 0.4167
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: CD perpendicular to BD via I.29 and alternate interior angles, ED perpendicular to AD (the crucial step), ED perpendicular to the plane through BD and DA via XI.4, CD perpendicular to DE via XI.2 and D11.3, and finally CD perpendicular to the reference plane via XI.4 again. The only difference is the technique for establishing ED perpendicular to AD: Heath uses implicit triangle congruence (SAS via I.4 and SSS via I.8, neither explicitly cited), while the AI uses three applications of the Pythagorean theorem (1.47) and its converse (1.48) with algebraic manipulation (CN1, CN2). Since heath_only is empty (all Heath citations appear in the AI set), and the ai_only items consist entirely of construction-level propositions (P1, 1.3, 1.11), common notions (CN1, CN2), and the Pythagorean tools (1.47, 1.48), Q2 Case A holds: same backbone of key conclusions, different citation depth.

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
**Category**: Granularity difference
**Jaccard**: 0.75
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) construct an auxiliary parallelepiped with standing edges matching the target solid on the given base, establishing equality by 11.29/11.30; (2) use 1.23 to adjust the angle of the second base and 1.35 to show the adjusted parallelogram equals the original; (3) construct and cut two auxiliary parallelepipeds using 11.25 to produce proportions relating each solid to a common mediating solid; (4) apply the proportion chain 5.7, 5.11, 5.9 to conclude equality of the two solids. The citation differences are purely at the depth level: the AI explicitly cites CN1 and 1.34 where Heath leaves them implicit, and Heath cites D11.10 where the AI achieves the same step through 11.24 and 11.29/11.30. The AI handles Heath's two-case structure (right-angle vs oblique standing edges) in a unified argument by deferring to 11.29 or 11.30 as appropriate, which is a presentation choice rather than a structural divergence. Same backbone with different citation depth yields G.

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


## Book 12

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 9 |
| Path difference (D) | 8 |
| AI proof error (E) | 1 |

**Total**: 18 propositions

### 12.1
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: from the similarity of the inscribed polygons, they derive equiangular triangles (BAE/GFL via VI.6), then use inscribed angle theorems to transfer angle equalities to triangles involving the diameters (ABM/FGN), establish equiangularity of those triangles via the right angle from III.31 and the angle sum from I.32, extract the proportionality BM:GN = BA:GF via VI.4, and conclude using duplicate ratios from VI.20. The key citation difference is that the AI cites 3.21 (angles in the same segment are equal) where Heath cites 3.27 (angles on equal circumferences in equal circles are equal) for the same logical step; both justify the equality of inscribed angles in a single circle, making this a citation-level rather than backbone-level difference. The remaining ai_only items (5.11, CN1, D5.9, P4) are auxiliary citations that Heath leaves implicit, representing over-citation at a finer granularity. Since the key intermediate conclusions are identical and only the citation depth differs, this is a granularity difference.

### 12.2
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: a double reductio ad absurdum using the method of exhaustion. In Case I (S < circle EFGH), both inscribe successively refined polygons to exhaust the gap between the circle and S (using 10.1), invoke 12.1 to relate similar inscribed polygons as squares on diameters, then derive a contradiction showing S is simultaneously greater than and less than the polygon. In Case II (S > circle EFGH), both reduce to Case I by inverting the ratio. The sole heath_only citation, 5.16 (alternando), is used by Heath to rearrange the proportion before concluding the contradiction, while the AI instead applies 5.14 directly to the unrearranged proportion to reach the same contradiction — an equivalent proportional reasoning step yielding the same key intermediate conclusion. The ai_only citations (1.41, 10.1, 4.6, 5.14, 5.7, CN1, CN5, D5.13) are explicit citations of foundational steps that Heath employs implicitly: 4.6 for inscribing the square, 10.1 for the exhaustion principle, 1.41 for the area comparison, and various Book 5 results and common notions for proportional reasoning. This is a citation-depth difference within the same logical backbone.

### 12.3
**Category**: Path difference
**Jaccard**: 0.278
**Analysis**: Q2 decides the classification. Both proofs establish the same key intermediate conclusions: the two sub-pyramids are equal, similar to each other, and similar to the whole; the remainder consists of two equal prisms; and the two prisms exceed half the whole pyramid. However, they reach the face-congruence and similarity conclusions by substantively different subsidiary methods. Heath uses XI.10 (equal angles from parallel lines in different planes) and I.4 (SAS congruence) to prove triangle congruences, while the AI uses VI.2 to establish that all six edges of each sub-pyramid are half the corresponding edges of the original, then applies I.8 (SSS congruence) to prove face congruences directly. The heath_only proposition XI.10 is not contained in the proof tree of any AI-cited proposition and represents a genuinely different geometric technique (angle-based vs. edge-length-based), so Case A of Q2 fails for this item, pushing to Case B and Q3. Under Q3, the AI's SSS-based path is fully valid, yielding classification D.

### 12.4
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determined the classification. Heath's proof establishes the prism ratio through proportionality of similar figures on proportional lines (6.22) followed by alternando (5.16) to derive that base_1 : base_2 equals the sub-triangle ratio. The AI's proof takes a genuinely different path: it argues that prisms of equal height are proportional to their bases (via 11.28, 11.32, 11.39), then computes that each prism base is one-fourth of the original triangle base using 6.19 directly, and uses 5.15 to conclude the ratio of prisms equals the ratio of original bases. The heath_only citations 5.16 and 6.22 are substantive backbone propositions in Heath's approach that are not merely compressed but entirely absent from the AI's logical chain, which substitutes a direct area-computation route. Both paths are logically complete and valid, yielding classification D.

### 12.5
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs follow the same double reductio ad absurdum structure: they assume the ratio of pyramids to bases fails, subdivide one pyramid using XII.3, apply the exhaustion principle (X.1), establish prism ratios via XII.4, derive a contradiction using Book V proportion results, then reduce the second case (W greater) to the first (W less). The key geometric intermediate conclusions are identical in both proofs. The differences lie entirely in which Book V proportion lemmas are invoked: Heath uses V.16 (alternation) and the XII.2 Lemma to manipulate the proportions and handle the second case, while the AI uses 5.14 (ratio comparison), 5.7 (inversion), 5.11 (transitivity), and 5.9 (equality from equal ratios). These are alternative proportion tools applied at the same logical junctures to reach the same geometric conclusions, making this a citation-depth difference rather than a path difference.

### 12.6
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 reveals genuinely different logical backbones. Heath builds up the polygonal base ratio incrementally using componendo (5.18): he adds one triangle at a time to the polygon, alternating between 5.18 and ex aequali (5.22) to progressively enlarge the base. The AI instead adopts a common-denominator strategy, comparing every sub-pyramid of both polygonal pyramids to a single reference pyramid (L-GHI) using 12.5, then summing all the ratios at once via 5.24 (addition of ratios with a common second term), and finally chaining with invertendo (5.7) and ex aequali (5.22). The key intermediate conclusions differ: Heath's intermediates are cumulative partial-polygon ratios (ABCD:ACD, ABCDE:ADE), while the AI's intermediates are whole-polygon-to-single-triangle ratios (P1:L-GHI, P2:L-GHI). Both paths are logically complete, so the classification is D.

### 12.7
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Heath decomposes the prism ABCDEF into three pyramids by drawing diagonals BD, EC, CD and argues equality via parallelogram faces ABED (diagonal BD) and FCBE (diagonal CE), using a same-planes identification to link the first two pyramids. The AI instead decomposes the prism by drawing diagonal AC and cutting planes through ACE and ACD, producing a different set of three pyramids (T1=ABCE, T2=ACDE, T3=ACEF). The AI argues equality by pairing pyramids whose bases are the two triangles formed by the diagonal of a parallelogram face (ABED with diagonal AE for T1=T2, ADFC with diagonal AC for T2=T3), applying XII.5 in each case. Because the decompositions use different cutting diagonals and yield different intermediate pyramids with different key intermediate conclusions (different parallelogram faces, different equal-triangle pairs), this is Case B (different backbone). The AI's alternative path is logically complete and valid, so this is classified as D.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: construct parallelepipeds around the similar pyramids, show the parallelepipeds are similar, apply XI.33 for the triplicate ratio of corresponding sides, establish that each pyramid is one-sixth of its parallelepiped via XI.28 and XII.7, and conclude the pyramids are in the triplicate ratio. The citation differences are all matters of depth: Heath cites XI.24 (opposite faces of a parallelepiped are equal and parallelogrammic) to help establish similarity of the solids, while the AI omits this and argues directly from the definition of similar solids (D11.9). The AI's additional citations (5.15 for the ratio step, D11.9, D5.10, D6.1 as definitions) make explicit what Heath leaves implicit or handles without explicit citation. No logical gap or error was identified in the AI proof.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: complete parallelepipedal solids from the given pyramids, apply 11.34 to establish reciprocal proportionality of the parallelepiped bases and heights, then convert the parallelogram base ratio to a triangle base ratio using proportion theory (5.11). The difference is purely in citation depth. Heath goes directly from pyramids to parallelepipeds (citing 1.34 to relate parallelogram bases to triangle bases), while the AI takes more explicit intermediate steps through prisms (12.7: prism = 3x pyramid), then constructs parallelepipeds from them (1.42 to build double-parallelogram bases, 11.39 to equate parallelepiped and prism), and uses 5.15 and CN1 for the equimultiple and equality reasoning. The ai_only items (12.7, 11.39, 1.42, 5.15, CN1) represent finer-grained construction steps, and the heath_only item (1.34) is replaced by the AI's equivalent use of 1.42 plus 5.15 at the same logical position. The key intermediate conclusions are identical in both proofs.

### 12.10
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Q2 reveals a genuinely different backbone in Case 2 of this double-reductio proof. Both proofs share the same structure for Case 1 (cylinder > 3*cone): inscribe a polygon, build prisms, apply exhaustion via X.1, use XII.7 to relate prism and pyramid, and derive a contradiction from the inscribed pyramid being both greater than and less than the cone. However, for Case 2 (cylinder < 3*cone), Heath exhausts the cone with inscribed pyramids, showing the inscribed pyramid exceeds one-third of the cylinder while the corresponding prism (inscribed in the cylinder) must be less than the cylinder. The AI instead switches to circumscribed figures: it circumscribes a polygon about the base circle, builds a circumscribed prism and pyramid, and derives a contradiction from the circumscribed pyramid being simultaneously greater than the cone (by containment) and less than the cone (from the exhaustion bound). This is a valid alternative approach with different key intermediate conclusions. Additionally, the AI uses I.41 (parallelogram-triangle area relation) to justify the greater-than-half lemma where Heath references XII.2, and the AI explicitly cites CN5 and definitions D11.18 and D11.21 that Heath leaves implicit. Q3 confirms the AI's circumscribed-figure path is logically sound, yielding classification D.

### 12.11
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 identified a genuine backbone difference between the two proofs, leading to classification D via Q3. Heath proves the result for cones first using inscribed pyramids and the exhaustion method, then extends to cylinders via XII.10 (cone = 1/3 cylinder). The AI reverses this order: it proves the result for cylinders first using inscribed prisms (justified via XII.7 reducing prisms to pyramids, then XII.6 for proportionality of pyramids to bases), establishes the cylinder ratio directly, and then derives the cone result from the cylinder result using XII.10 and V.15. Additionally, the proportion-manipulation techniques differ: Heath uses V.16 (alternation) to reach the contradiction, while the AI uses V.14 (comparison via proportion) and V.7 (inversion) for corresponding steps. These constitute substantive differences in both the order of key intermediate conclusions and the specific logical tools employed, placing this firmly in path-difference territory. Q3 confirms the AI's alternative path is logically valid.

### 12.12
**Category**: Path difference
**Jaccard**: 0.150
**Analysis**: Q2 determined the classification. Heath proves this proposition using the method of exhaustion (double reductio ad absurdum): he assumes the triplicate ratio maps to a solid less than (then greater than) the second cone, inscribes polygons in the circular bases, builds similar pyramids with the same vertex as the cones, applies 12.8 (similar pyramids in triplicate ratio of corresponding sides) and 10.1 (exhaustion principle) to derive a contradiction. The AI takes a fundamentally different direct approach: it introduces an intermediate cone sharing the first cone's base and the second cone's height, then shows (1) the intermediate cone to the second cone is in the duplicate ratio of the diameters via 12.11 and 12.2, and (2) the first cone to the intermediate cone is as the ratio of diameters (via an informal argument about cones on the same base being as their heights, using 12.10, 11.25, and 6.1). The AI then compounds these ratios via 5.22 to obtain the triplicate ratio. The key intermediate conclusions are entirely different: Heath's backbone involves inscribed similar pyramids and exhaustion, while the AI's backbone involves ratio composition through an intermediate cone. E was considered for Step 6 where the AI cites 12.11 for a claim about cones on the same base being as their heights (12.11 actually proves the converse), but the audit record shows missing_is = expansion since the AI provides informal reasoning through 12.10 and 11.25 that could be expanded, so the lenience rule applies and the verdict is NOT-E. Since the backbones differ and the AI's path is valid under the hardened standard, the classification is D.
**Audit Record**: CANDIDATE E — 12.12
  violated_claim : "the first cone is to the intermediate cone as KL is to MN" (cones on the same base are to one another as their heights)
  failure_mode   : invalid_inference
  missing_is     : expansion (the AI provides informal reasoning via 12.10, 11.25, 6.1 that could be expanded to a full proof of this claim)
  evidence       : Step 6: "By 12.11, cones on the same base (which is a special case of equal bases) are to one another as their heights... we apply 11.25 and the general principle: by 12.10, cone = (1/3) cylinder, and cylinders on the same base are as their heights (since a cylinder on a given base with height h equals the base times h, by the reasoning underlying 12.11 and 6.1)"
  why_not_terse  : 12.11 proves cones of same height are as their bases, not the converse; the informal chain through 11.25 is about parallelepipeds not cylinders. However, missing_is = expansion because the reasoning chain (12.10 reducing cones to cylinders, 11.25 giving proportionality for parallelepipeds, extending to cylinders) is an expansion of a supported step rather than an entirely missing support relation. Lenience rule applies: NOT-E.

### 12.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Both proofs follow the same equimultiple strategy to establish the proportion between cylinder segments and axis segments via V. Def. 5 (D5.5). The key intermediate conclusions are identical: (1) cross-sections cut by parallel planes are equal circles, (2) cylinders on equal axis segments with equal bases are equal, establishing the equimultiple relationship, (3) the equimultiple comparison transfers between axes and cylinders, and (4) the definition of proportion yields the result. The difference is purely in citation depth: Heath invokes 12.11 (cylinders of the same height are as their bases) to formally justify that cylinders on equal segments are equal, while the AI argues this directly from definitions of cylinders (D11.21, D11.22, D11.23) and 11.14 (planes perpendicular to the same line are parallel). The AI goes to a lower level of justification rather than citing the composite theorem. Since the backbone is the same and the difference is only in what level of the dependency tree each proof cites, this is a granularity difference (G).

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: construct a cylinder with the same base and matching height, use 12.11 to establish equality of cylinders on equal bases with equal heights, use 12.13 to establish that cutting a cylinder by a parallel plane yields cylinders proportional to their axes, substitute the equal cylinder to obtain the height ratio, then use 12.10 to extend the result from cylinders to cones. The AI adds explicit citations to 5.15 (parts have the same ratio as multiples) and 5.11 (transitivity of equal ratios) when deriving the cone case from the cylinder case, whereas Heath handles this ratio reasoning implicitly. Since heath_only is empty and ai_only contains only Book 5 ratio-algebra lemmas supporting the same logical step Heath performs without citation, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they construct an auxiliary cone or cylinder sharing one base and one height from the two originals, establish a ratio via equal heights using 12.11, establish a ratio via equal bases (Heath uses 12.13 on a cut cylinder; the AI uses the higher-level 12.14), apply 5.7 from the equality of the original solids, and combine ratios via 5.11 to reach the reciprocal proportionality. The converse directions are similarly parallel. The proof-tree containment test confirms that heath_only item 12.13 appears inside Heath's proof of 12.14, so the AI is citing 12.14 as a packaged unit while Heath re-derives its internals inline. The ai_only item D5.13 is a definition (inverse ratio) representing over-citation. The AI also unifies Heath's two sub-cases (equal and unequal heights) into a single general argument, which is a presentational difference rather than a backbone difference. All key intermediate conclusions match, with only citation depth differing.

### 12.16
**Category**: Path difference
**Jaccard**: 0.062
**Analysis**: Q2 reveals different backbones: Heath's proof constructs a tangent to the lesser circle (3.16), then repeatedly bisects the circumference (10.1) to produce a chord LN parallel to that tangent, concluding via parallelism that LN cannot touch the lesser circle, and uses 3.3 and 1.4 to show LD = DN. The AI proof instead inscribes a square (using 1.11 and 3.29), then repeatedly bisects arcs (3.30) while tracking perpendicular distances from the center to each side via 3.15, showing that these distances strictly increase with each bisection, and applies 10.1 to conclude that after sufficiently many bisections the perpendicular distance exceeds the lesser circle's radius. The key intermediate conclusions differ: Heath relies on tangent-parallelism, while the AI relies on perpendicular-distance monotonicity and 3.15. Under Q3, the AI's alternative path is logically complete — each step is supported by valid citations (3.15 for the distance comparison, 10.1 for the exhaustion argument, 3.30 for arc bisection), and no unsupported assertions, circular citations, or invalid inferences are present under the hardened 1(b) standard.

### 12.17
**Category**: Path difference
**Jaccard**: 0.148
**Analysis**: Q2 determined the classification. Heath proves the polyhedron does not touch the lesser sphere by dropping a perpendicular AX from centre A to the plane of each face and algebraically showing AX > AG (the lesser sphere radius) through comparisons of squares (I.47, III.31, VI.8). The AI proof takes a fundamentally different approach: it uses a cross-sectional argument, showing that for any point on any face, the plane perpendicular to the axis BD at that height cuts the polyhedron in a polygon lying entirely outside the lesser sphere's cross-section circle. The AI establishes this at latitude levels by construction (12.16) and at intermediate heights by interpolation (11.17, 6.2, 11.16). These are genuinely different key intermediate conclusions -- Heath never considers cross-sections perpendicular to the axis, and the AI never drops a perpendicular to a face plane or compares squares. The large symmetric difference in citations (Jaccard 0.148) with substantive propositions on both sides confirms the path divergence. The AI's cross-sectional chain is logically complete under the hardened Q1(b) standard, so Q3(b) holds and the classification is D.

### 12.18
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Both proofs follow the same double reductio ad absurdum backbone: assume the spheres do not have the triplicate ratio of diameters, derive a contradiction for the less-than case by inscribing polyhedra (via 12.17) whose triplicate ratio equals the assumed ratio, then using alternando (5.16) to show the inner sphere must be both greater and less than the inscribed polyhedron, then handle the greater-than case to complete the exhaustion. The key intermediate conclusions are identical in both proofs. The citation differences are granularity-level: the AI explicitly cites 12.8 for the triplicate ratio of similar pyramids (which Heath subsumes under 12.17), and the AI enumerates Book 5 ratio propositions (5.11, 5.13, 5.14, 5.22) plus definitions and common notions (CN1, CN5, D11.14, D11.17, D5.10) that Heath leaves implicit. The sole heath_only citation, 12.2 (its Lemma), is used by Heath to formally justify that if a greater sphere has a certain ratio to a third sphere, then the original sphere has that ratio to something smaller; the AI handles this same step by inversion (5.13) and appeal to symmetry of the argument, which is a different justification mechanism for the same conclusion rather than a different backbone. Since Q2 Case A holds with the same key intermediate conclusions throughout, the classification is G.


## Book 13

| Category | Count |
|---|---|
| Perfect match (P) | 0 |
| Granularity difference (G) | 6 |
| Path difference (D) | 11 |
| AI proof error (E) | 1 |

**Total**: 18 propositions

### 13.1
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: The classification is decided at Q2/Q3 as a path difference. Both proofs share the same starting point (rect(AB,BC) = sq(AC) via D6.3 and 6.17) and the same conclusion (sq(CD) = 5*sq(DA)), but they reach the conclusion through fundamentally different methods. Heath uses a geometric approach based on gnomons and proportional areas, relying on VI.1 to establish proportional relationships among rectangles within constructed squares. The AI instead takes an algebraic route through Book 2 identities: it uses 2.1 (distributive property of rectangles) to decompose sq(AB) into rect(AB,AC) + rect(AB,CB), applies 2.4 to expand both sq(AB) = 4*sq(AD) and sq(AC+AD), and then combines these algebraic results to reach 5*sq(AD). The AI's proof introduces constructions (bisection via 1.10, point construction via 1.3 and P2) and algebraic propositions (2.1, 2.4) that Heath does not use, while Heath's gnomon-based geometric reasoning through VI.1 is entirely absent from the AI's proof. The backbones are genuinely different, and the AI's algebraic path is logically complete and valid.

### 13.2
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof uses geometric constructions (squares AF and CG, gnomons, and area reasoning) with a single citation of VI.1 to establish that rect(CD, DB) = sq(CB), then concludes via proportion. The AI proof takes an entirely different algebraic route using Book 2 identities (2.1, 2.2, 2.4) to derive sq(AC) = rect(CD, CD-AC), then applies 6.17 to establish the extreme and mean ratio proportion. The key intermediate conclusions differ fundamentally: Heath reasons through gnomon MNO = CG and remainder HF = BG via geometric figure manipulation, while the AI reasons through algebraic expansions of squares and rectangles. The proof-tree containment test confirms this is genuine path divergence since 6.1 (Heath's only citation) does not appear in the proof trees of any AI-cited proposition. The AI's algebraic path is logically complete and valid, satisfying Q3(b), yielding classification D.

### 13.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) rect(AB,BC) = sq(AC) from the extreme and mean ratio property, (2) sq(AC) = 4*sq(DC) because AC = 2DC, and (3) combining these to get sq(BD) = 5*sq(DC). Heath uses geometric area manipulations through a constructed square figure with gnomons, while the AI uses explicit algebraic identities (2.6 for the binomial square relationship, 2.4 to expand sq(AC), 6.17 for the EMR rectangle-square equivalence). The logical backbone is identical in both proofs. The difference is purely in citation depth: Heath's recorded references are empty while the AI explicitly cites the propositions justifying each step. Since the key conclusions align and only the citation granularity differs, this is classified as G.

### 13.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish that rect(AB,CB) = sq(AC) from the golden ratio definition (D6.3, 6.17), (2) derive that sq(AB) + sq(CB) = 2*rect(AB,CB) + sq(AC), and (3) substitute to conclude sq(AB) + sq(CB) = 3*sq(AC). The sole difference is citation depth: Heath re-derives the identity of Proposition 2.7 inline through gnomon geometry (constructing square ADEB and manipulating areas with gnomon LMN and squares CK, HG), while the AI cites Proposition 2.7 directly as a packaged result. Checking Heath's proof of 2.7 confirms it uses the identical gnomon construction that appears in Heath's 13.4 proof, satisfying the proof-tree containment test. The AI's additional citations of CN1 and CN2 are over-citations for basic arithmetic combining steps. Heath_only is empty, confirming no independent reasoning strand is missing from the AI proof.

### 13.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) AB is cut in extreme and mean ratio so AB*BC = AC^2, (2) the rectangle BD*DA equals the square AB^2, (3) the proportion DB:AB = AB:DA follows by 6.17, and (4) AB is the greater segment. The proofs differ in technique for establishing BD*DA = AB^2: Heath uses a geometric area argument with constructed squares and rectangles in a diagram, while the AI uses algebraic distribution via 2.1, expanding both AB^2 and DB*DA to show both equal AC^2 + AB*AC. For the greater-segment conclusion, Heath invokes 5.14 (a proportion theorem: if a:b = c:d and a > c then b > d), while the AI uses the more elementary CN5 (whole > part) and CN1 (equals substitution). The ai_only items (1.3, P2, 2.1, CN1, CN5) are construction props, a computational identity, and common notions -- all consistent with over-citation or different granularity rather than a different logical path. The single heath_only item (5.14) is replaced by a more direct elementary argument reaching the same conclusion. Since all key intermediates align and the differences are in citation depth and technique rather than backbone, this is a granularity difference.

### 13.6
**Category**: Path difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs agree on the method for proving AC is an apotome (using 13.1 to establish sq(CD)=5*sq(DA), then 10.6 and 10.9 to show CD and DA are rational and commensurable in square only, and 10.73 to conclude AC is an apotome). However, the proofs diverge fundamentally on how they prove CB is an apotome. Heath uses the extreme-and-mean-ratio property via 6.17 to establish rect(AB,BC)=sq(AC), then applies 10.97 to conclude CB is specifically a first apotome. The AI instead takes a direct algebraic approach: expressing CB = 3*AD - E, showing that 3*AD and E are rational and commensurable in square only (via the ratio 9:5 and propositions 10.6 and 10.9), and then applying 10.73 to conclude CB is an apotome. These are genuinely different key intermediate conclusions for the CB segment, constituting Case B (different backbone) in Q2. The AI's different path is logically valid and complete (Q3 holds), so the classification is D.

### 13.7
**Category**: Path difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs handle the two required cases (consecutive and non-consecutive equal angles), so Q1 is satisfied. However, the key intermediate conclusions differ substantially. In Case 1, Heath works through the intersection point F of diagonals AC and BE, using I.6 (converse isosceles triangle theorem) to establish AF = BF, then subtracting to get FC = FE, and applying I.8 to triangles FCD and FED. The AI avoids the intersection point entirely and instead establishes BE = BD via I.4 on triangles ABE and BCD, uses I.5 on isosceles triangle BDE for angle BDE = angle BED, and proceeds through a different chain of triangle congruences (including I.8 on triangles CEA and DAB) to show all angles equal. In Case 2, Heath works directly with the given non-consecutive angles (A, C, D), while the AI relabels to (A, B, D) and reduces to Case 1 by showing angle E equals the given equal angles. The AI's omission of I.6 is not an under-citation but reflects a genuinely different logical backbone that avoids needing the converse of the isosceles triangle theorem. Both paths are logically complete and valid, confirming a path difference.

### 13.8
**Category**: Granularity difference
**Jaccard**: 0.438
**Analysis**: Q2 decides: both proofs share the same key intermediate conclusions (angle BAC = angle ABE, HE = EA = side of pentagon via I.6, triangle similarity yielding the proportion BE:HE = HE:HB, and HE being the greater segment) but differ in citation depth and supporting arguments. Heath uses VI.33 (angles proportional to arcs) combined with III.28 to establish that angle EAC is double angle BAC, while the AI uses III.27 (equal arcs yield equal inscribed angles) and explicit interior-angle computation to reach the same conclusion. Heath uses V.14 to establish HE > HB from the proportion, while the AI uses I.19. The AI additionally cites 6.17 to convert the proportion into a rectangle-square equality, and explicitly invokes D6.3 for the definition of extreme and mean ratio. Since 3.27 appears inside Heath's proof of 6.33, the AI is partly citing at a lower level, but also takes a genuinely different computational route through explicit angle values rather than arc proportionality. The ai_only items (1.19, 3.27, 6.17, CN1, CN3, D6.3, P1) are a mix of lower-level citations and alternative support for the same backbone conclusions, while the heath_only items (5.14, 6.33) represent Heath's alternative supporting propositions for those same conclusions. The backbone is the same; only the depth and choice of supporting lemmas differs, yielding G.

### 13.9
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: The forward dependency gate passed (all AI citations are backward). Q1 found no logical defect: the AI proof is complete, correctly applying 4.15 to identify the hexagon side as the radius, 2.11 and 4.10 to identify the decagon side as the greater segment of the radius cut in extreme and mean ratio, and 13.5 to conclude that adding the greater segment to the EMR-cut line produces a new EMR cut with the original line as the greater segment. Q2 identified fundamentally different backbones: Heath uses angle chasing via arc-angle correspondence (6.33), isosceles triangle properties (1.5, 1.32), and similar triangle proportionality (6.4) to derive BD:DC = DC:CB directly; the AI instead identifies the decagon side as the EMR greater segment of the radius and applies the higher-level result 13.5 about extending EMR-cut lines. With only 4.15 shared and entirely different intermediate conclusions, this is Case B (different backbone). Q3 confirmed the AI's different path is logically complete and valid, yielding classification D.

### 13.10
**Category**: Path difference
**Jaccard**: 0.130
**Analysis**: Q2 determined the classification. Heath's proof establishes the result through similar triangles: it identifies AK as the decagon side, proves triangles ABF and BFN equiangular to get rect(AB,BN) = sq(BF), proves triangles KBA and KNA equiangular to get rect(BA,AN) = sq(AK), then applies II.2 to combine these into sq(BA) = sq(BF) + sq(AK). The AI takes a fundamentally different path: it identifies BG as the decagon side via arc midpoint, uses the angle-in-semicircle theorem (3.31) and the Pythagorean theorem (1.47) to get 4r^2 = d^2 + q^2, invokes 13.9 for the golden ratio property of hexagon and decagon sides, applies the intersecting chords theorem (3.35), and then proceeds through extensive algebraic manipulation to derive sq(p) = sq(r) + sq(d). The key intermediate conclusions are entirely different -- Heath uses proportion from equiangular triangles while the AI uses metric relations from the Pythagorean theorem and intersecting chords combined with the golden ratio. The very low Jaccard similarity of 0.13 (only 3 shared citations out of 23 total) confirms the massive divergence. The AI proof is logically complete under the hardened Q1(b) standard, with each step properly justified, so Q3 yields a valid different path.

### 13.11
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 determined the classification. Heath's proof works directly within the pentagon geometry, using similar triangles (ACL ~ AMF via I.32) and proportion manipulation (V.18, V.19) to establish that sq(MK) = 5*sq(KF), then uses XIII.8 and XIII.1 to derive the five-times relation, and shows MB is a fourth apotome via X.15 and X.12. The AI takes a fundamentally different path: it decomposes side_pent^2 via XIII.10 into r^2 + side_dec^2, uses the extreme-and-mean ratio properties (XIII.9, XIII.5) and algebra (VI.17, II.1) to express side_pent^2 = r*(2r - side_dec), then constructs N = 2r - side_dec as P - Q using the II.11 construction and I.47, showing N is a fourth apotome through ratio analysis with X.6 and X.9. The key intermediate conclusions differ entirely: Heath's backbone involves similar triangles within the pentagon and the segments MK, KF, BK, while the AI's backbone involves the hexagon-decagon decomposition and explicit algebraic manipulation of the radius. With only 4 shared citations out of 26 total (Jaccard 0.154), this is a genuine path difference with a valid alternative route confirmed in Q3.

### 13.12
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Classification was decided at Q2 (Case A). Both proofs follow the same logical backbone: inscribe the equilateral triangle in the circle, identify a chord subtending one-sixth of the circumference as equal to the radius (via the hexagon property, IV.15), establish a right angle in a semicircle (III.31), apply the Pythagorean theorem (I.47), and conclude by arithmetic that the square on the side equals three times the square on the radius. The AI's proof adds explicit citations for intermediate steps that Heath leaves implicit: 3.28 (equal chords cut equal arcs) and 3.29 (equal arcs are subtended by equal chords) to justify the arc and chord equalities, plus definitions (D1.15, D1.17, D1.20, D4.3), common notions (CN1, CN3), and a postulate (P1). Heath's citation set {1.47, 3.31, 4.15} is a strict subset of the AI's, and heath_only is empty, confirming this is pure over-citation at greater granularity rather than a different proof path.

### 13.13
**Category**: Path difference
**Jaccard**: 0.318
**Analysis**: Q2 determines the classification. Heath constructs the tetrahedron with vertex K erected perpendicular above center H of the inscribed equilateral triangle base EFG (in a separate circle), proves edge equality via SAS congruence (I.4), and inscribes in the sphere by showing a semicircle on KL passes through E, F, G. The AI instead uses endpoint A of the diameter as the vertex, places the equilateral triangle FGH in a circle centered at C on the diameter in a perpendicular plane, proves edge equality via the Pythagorean theorem (I.47) applied to right triangles, and inscribes in the sphere by computing distances from center O. These represent genuinely different construction layouts and proof methods -- different key intermediate conclusions (I.47-based coordinate-style computation vs I.4-based SAS congruence; direct distance computation from sphere center vs semicircle rotation argument). The AI proof is logically complete and valid under Q3, so the classification is D.

### 13.14
**Category**: Path difference
**Jaccard**: 0.118
**Analysis**: The AI proof uses a fundamentally different construction from Heath's. Heath constructs a square EFGH with diagonals meeting at K, erects perpendiculars KL and KM equal to KE, then uses I.4 (SAS congruence) and III.31 (angle in semicircle is right) to prove the octahedron is inscribed in the given sphere and that the diameter squared is double the side squared. The AI instead places the center C at the midpoint of diameter AB, constructs four points D, E, F, G in a plane perpendicular to AB through C, all at distance CA from C, forming a 6-vertex octahedron directly. The AI proves edge equality via I.47 applied to right triangles with equal legs, proves inscription by noting all vertices are equidistant from C, and proves the diameter-to-side ratio by direct arithmetic (AB squared = 4 AC squared = 2 times side squared). The different constructions lead to different key intermediate conclusions and different citation sets (heath_only contains I.4 and III.31 which are not needed in the AI's approach; ai_only contains constructions, definitions, and 2.4 reflecting the AI's direct algebraic approach). Since the AI's different path is logically complete and valid, Q3 yields category D.

### 13.15
**Category**: Path difference
**Jaccard**: 0.056
**Analysis**: Q2 decided this classification. Both proofs construct the cube identically and reach the same numerical conclusions (EG^2 = 2*EF^2, space-diagonal^2 = 3*EF^2, AB^2 = 3*BD^2), but they diverge in two key ways. First, the AI uses an explicit similar-triangles approach (6.8, 6.4, 6.17) to establish BD^2 = BC*BA, while Heath uses an implicit proportion argument. More significantly, the proofs take genuinely different paths for the inscribability sub-problem: Heath uses a semicircle rotation argument with D11.3 (the definition of perpendicular to a plane) to show the semicircle on KG passes through all vertices, while the AI proves inscribability by showing all space diagonals bisect at a common center O and all vertices are equidistant from O (using parallelogram properties 1.33, 1.34 and the perpendicularity result 11.6). This center-equidistance method is a substantively different logical route from Heath's semicircle rotation strategy, constituting a backbone difference (Case B). Q3 confirms the AI's path is valid: every step is supported by cited propositions and the chain runs completely from premises to conclusion.

### 13.16
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: AB squared equals 5 times DB squared from the semicircle construction, two pentagonal rings inscribed in circles of radius DB, the decagon side identity s_10 = (AB - DB)/2 via 13.9 and 13.3, all 30 edge lengths verified via 13.10 (pentagon side squared = hexagon side squared + decagon side squared), all 12 vertices on the sphere of diameter AB, and the side classified as minor via 13.11. The AI proof is more explicit in citing construction steps (1.10, 1.11, 3.30, 4.11, 11.12), the Pythagorean theorem (1.47), commensurability (10.6), and axioms/definitions (CN1, D10.1.3, D11.27, P1), while Heath leaves these implicit. The sole heath_only citation D5.9 is a definition, not substantive. This is Case A: same backbone, different citation depth.

### 13.17
**Category**: Path difference
**Jaccard**: 0.161
**Analysis**: Q2 determines the classification. Both proofs construct a dodecahedron from a cube by bisecting edges and cutting half-edges in extreme and mean ratio, then prove the resulting pentagons are equilateral, equiangular, and coplanar, that the dodecahedron is comprehended in the given sphere, and that its side is an apotome. However, the detailed intermediate arguments differ substantially (Jaccard 0.161). Heath uses 13.4 and 13.5 as the core EMR results for proving equilateral sides, equiangularity, and sphere comprehension, while the AI uses 13.1, 13.2, and 13.3 — algebraically related but distinct EMR propositions. Heath proves coplanarity explicitly via 6.32 (triangles with proportional parallel sides yield collinear remaining sides), 11.6 (lines perpendicular to the same plane are parallel), and 11.1 (a line cannot be partly in one plane and partly in another), whereas the AI asserts coplanarity from symmetry without comparable geometric detail. Heath uses 5.15 for the ratio doubling argument showing NO is cut in EMR, while the AI omits this entirely. These differences in the choice of supporting propositions and the level of geometric argument constitute a genuine path difference rather than mere granularity variation, as the AI employs a different set of EMR lemmas and omits the solid-geometry coplanarity proof in favor of a symmetry-based approach.

### 13.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: the squared relationships between the diameter and each of the five solid sides (pyramid = 2/3, octahedron = 1/2, cube = 1/3 of the squared diameter), the identification of icosahedron and dodecahedron sides as minor and apotome irrationals respectively, the rational ratios among the first three (4:3, 3:2, 2:1), and the ordering including icosahedron side > dodecahedron side. The difference lies in citation depth: Heath performs detailed geometric constructions within 13.18 using lower-level tools (VI.8, VI.4, V.Def.9, IV.15, XIII.9, VI.20) to re-derive intermediate relationships, while the AI directly cites the higher-level results of XIII.13-17 and performs arithmetic comparisons. The proof-tree containment test confirms that many heath_only citations (4.15, 13.9, 6.8, D5.9) appear inside Heath's proofs of XIII.13, XIII.16, and XIII.17 — the very propositions the AI cites as units. The AI's additional citations (1.47, 13.12, 13.8) are over-citations for steps that Heath handles through different lower-level tools. The logical backbone is the same in both proofs; only the granularity of citation differs.
