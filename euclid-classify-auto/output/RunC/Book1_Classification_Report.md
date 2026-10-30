# Book 1 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 11 | 1.3, 1.13, 1.16, 1.17, 1.19, 1.25, 1.27, 1.35, 1.36, 1.38, 1.43 |
| Granularity difference (G) | 37 | 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.14, 1.15, 1.18, 1.20, 1.21, 1.22, 1.23, 1.24, 1.26, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.37, 1.39, 1.40, 1.41, 1.42, 1.44, 1.45, 1.46, 1.47, 1.48 |
| Path difference (D) | 0 |  |
| AI proof error (E) | 0 |  |

**Total**: 48 propositions

## Per-Proposition Analysis

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
