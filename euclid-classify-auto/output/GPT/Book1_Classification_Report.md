# Book 1 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 3 | 1.3, 1.19, 1.25 |
| Granularity difference (G) | 43 | 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.20, 1.21, 1.22, 1.23, 1.26, 1.27, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48 |
| Path difference (D) | 2 | 1.24, 1.40 |
| AI proof error (E) | 0 |  |

**Total**: 48 propositions

## Per-Proposition Analysis

### 1.1
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct two circles centered at A and B, join the intersection point C to both endpoints, use Def. 15 twice to establish AC=AB and BC=BA, then chain these equalities to conclude all three sides are equal and the triangle is equilateral. The AI proof adds citations for CN4 (things equal to themselves), D1.19 (definition of trilateral figure), and D1.20 (definition of equilateral triangle), which Heath uses implicitly without explicit citation. The AI's commentary about the intersection issue is a well-known foundational observation about Euclid's proof, not a logical defect in the AI's own reasoning. Since heath_only is empty and ai_only contains only definitions and common notions, this is a citation-depth difference with the same backbone, yielding G.

### 1.2
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing equilateral triangle DAB on the join AB, drawing a circle with center B through C to establish BG = BC, drawing a circle with center D through G to establish DL = DG, subtracting the equal segments DA = DB to obtain AL = BG via CN3, and concluding AL = BC by transitivity via CN1. The AI's three additional citations (CN5, D1.15, D1.20) are all definitions and common notions that make implicit steps explicit: D1.15 justifies radii equality from the definition of a circle, D1.20 justifies DA = DB from the definition of an equilateral triangle, and CN5 justifies the ordering of points along produced lines. Since heath_only is empty and the ai_only items are purely foundational over-citations rather than substantive propositions, and since both proofs establish the same key intermediate conclusions in the same order, Q2 Case A holds, yielding G.

### 1.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate found no issues (1.2 is prior, CN1/D1.15/P3 are never forward). Q1 confirmed the AI proof is logically complete: each step is explicitly supported by a cited proposition, definition, postulate, or common notion, with no gaps. Q2 confirmed both proofs share the same backbone of key intermediate conclusions: place a segment equal to the lesser line at the endpoint of the greater (1.2), draw a circle (P3), equate the cut-off segment to the radius (D1.15), and conclude equality by transitivity (CN1). Since the citation sets are identical (ai_used = heath_refs = {1.2, CN1, D1.15, P3}, Jaccard = 1.0) and the backbones match, the perfect-match check assigns category P.

### 1.4
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs use the method of superposition and establish identical key intermediate conclusions in the same order: placing vertex A on D and side AB along DE so that B coincides with E (by equality of AB and DE), then using the equality of the included angles to force AC along DF, then using AC = DF to make C coincide with F, and finally concluding that the bases, triangles, and remaining angles are equal. The only difference is citation depth: the AI explicitly cites foundational definitions (D1.4, D1.8, D1.9, D1.14, D1.19) and Common Notion 5 that Heath leaves entirely implicit. Since all ai_only items are definitions and common notions (no substantive propositions) and heath_only is empty, this is a clear Case A granularity difference.

### 1.5
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: construct F on the extension of AB and G on the extension of AC with AF = AG (via I.3), prove triangles AFC and AGB congruent (via I.4), derive BF = CG as remainders, prove triangles BFC and CGB congruent (via I.4), and obtain both the base angles and under-base angles. The AI proof explicitly cites Common Notions (CN1, CN3, CN4, CN5) and a Definition (D1.20) that Heath invokes implicitly without citation. Since heath_only is empty and ai_only contains only axiom-level items, this is a clear case of over-citation at the same logical depth, satisfying Case A of Q2 for Granularity difference.

### 1.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume AB > AC, cut DB equal to AC, apply SAS to obtain triangle DBC equal to triangle ACB, note that the part equals the whole (absurd), and conclude AB = AC. The key intermediate conclusions are identical in both proofs. The AI simply cites explicitly (1.3, 1.4, CN1, CN4, CN5, P1) what Heath uses without naming references. Since heath_refs is empty (no citations extracted) while the AI provides six explicit citations for the same logical steps, this is a citation-depth difference, not a path difference. Classification is G (granularity difference).

### 1.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction that applies I.5 to the two pairs of equal sides (AC=AD and CB=DB) to establish equal base angles, then derives a contradiction through angle inequalities showing an angle is simultaneously greater than and equal to another. The AI proof is more thorough, explicitly handling exterior and nested geometric configurations and citing P1, P2, and CN5 for constructions and axiom invocations that Heath leaves implicit, but these are postulates and common notions representing over-citation at a different granularity level rather than a different proof strategy. Since heath_only is empty and ai_only contains only postulates and common notions, this is Case A of Q2: same backbone with different citation depth.

### 1.8
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the identical superposition backbone: apply triangle ABC to DEF by placing B on E and BC on EF so that C coincides with F; argue by contradiction using I.7 that the sides must also coincide; conclude that the contained angles coincide and are therefore equal. The AI proof explicitly cites the common notions it invokes (CN4 for superposition and coincidence, CN5 for the base equality argument, CN1 for transitivity of side equalities), while Heath leaves these implicit. Since heath_only is empty and ai_only contains only common notions, this is a clear case of the AI providing finer citation granularity for the same logical path, yielding G.

### 1.9
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: cut off AE equal to AD on AC (I.3), construct equilateral triangle DEF on DE giving DF = EF, then apply SSS congruence (I.8) to conclude angle DAF equals angle EAF, thereby bisecting the given angle. The AI proof is more explicit, citing I.1 for the equilateral triangle construction, P1 for joining lines, CN4 for the common side and angle coincidence, CN5 for an ordering argument, and definitions D1.9 and D1.20, all of which Heath leaves implicit. Since heath_only is empty and all ai_only items are construction propositions, postulates, common notions, or definitions that represent citation-depth differences rather than backbone divergences, Case A of Q2 holds, yielding G.

### 1.10
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct an equilateral triangle ABC on AB (I.1), bisect angle ACB with line CD (I.9), then apply SAS (I.4) using AC=CB, CD common, and angle ACD = angle BCD to conclude AD=BD. The AI's three extra citations (D1.20 for the definition of equilateral triangle justifying AC=BC, CN4 for the common side CD=CD, and P2 for extending the angle bisector to meet AB) are all foundational items — a definition, a common notion, and a postulate — that Heath leaves implicit. Since heath_only is empty and ai_only contains only non-substantive over-citations, this is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 1.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: taking a point D on the line and making CE equal to CD, constructing an equilateral triangle on DE to obtain DF = EF, joining CF, proving triangles DCF and ECF congruent by SSS (I.8), and concluding that the adjacent equal angles are right angles by Def. 10. The AI proof cites additional foundational items (P1, P2, CN4, D1.20) that Heath uses implicitly but does not cite, while heath_only is empty. Since the logical backbone is the same and the citation difference consists entirely of postulates, definitions, and common notions, this is a citation-depth difference under Case A of Q2, yielding G.

### 1.12
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct a circle centered at the given point C with radius reaching past the line, identify the two intersection points of the circle with the line, bisect the resulting chord at H, then apply I.8 using the three side equalities (radii, bisection, common side CH) to conclude the adjacent angles at H are equal, and invoke Def. 10 to establish perpendicularity. The AI proof explicitly cites CN4 (things equal to the same are equal), CN5 (the whole is greater than the part, used to show O lies inside the circle), D1.15 (definition of circle, used to justify equal radii), and P2 (to produce a line), all of which Heath uses implicitly without citation. With heath_only empty and ai_only containing only axioms, definitions, and postulates, this is a clear case of over-citation at a finer granularity, not a different proof path.

### 1.13
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the same two-case structure and establish identical key intermediate conclusions: (1) if the adjacent angles are equal, each is a right angle by D1.10; (2) if unequal, construct BE perpendicular to CD via I.11, decompose the angles into parts, apply CN2 twice to show both sums equal the same three angles, then apply CN1 for transitivity to conclude CBA+ABD equals two right angles. The only difference is that the AI explicitly cites CN4 (things which coincide with one another are equal) for the angle-decomposition step in Step 4, where Heath performs the same decomposition without an explicit common-notion citation. Since ai_only contains only CN4 (a common notion, indicating over-citation) and heath_only is empty, this is a citation-depth difference with the same logical backbone, yielding G.

### 1.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: applying I.13 to establish a supplementary angle pair, equating the two angle sums via CN1, subtracting the common angle via CN3 to conclude that two specific angles are equal, and then using that equality to force the two lines to coincide. The AI takes a constructive approach (extending BO to D via P2, then arguing coincidence of rays via CN5) while Heath uses proof by contradiction (assuming a different line BE and deriving an impossibility via Post.4). The symmetric difference consists entirely of axiom-level items: ai_only holds CN5 and P2 (a Common Notion and a Postulate used for the constructive framing), while heath_only holds P4 (a Postulate used to equate the fixed value of two right angles). Since the key intermediate conclusions are identical and only the citation depth differs, this is a granularity difference.

### 1.15
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: applying I.13 to show that adjacent angle pairs formed by two intersecting lines each sum to two right angles, then equating these sums and subtracting the common angle via CN3 to establish equality of vertical angles. The AI's only extra citation is CN2 (if equals be added to equals, the wholes are equal), which it uses to make explicit the step where two sums each equal to two right angles are equated. Heath handles this same step with just P4 and CN1. Since CN2 is a common notion (axiom-level), its inclusion reflects greater explicitness in the justification chain rather than a different proof strategy. The AI also proves both pairs of vertical angles explicitly rather than deferring one to 'similarly,' but the underlying reasoning is identical. This is a same-backbone, different-depth scenario under Q2 Case A.

### 1.16
**Category**: Granularity difference
**Jaccard**: 0.875
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect a side of the triangle, extend the join to construct a segment of equal length, apply SAS congruence (I.4) using vertical angles (I.15) to establish equal angles, then invoke the part-whole inequality (CN5) to conclude the exterior angle exceeds the interior opposite angle. The AI explicitly carries out the second case (ACD > ABC) that Heath handles with 'similarly,' but the key intermediate conclusions are identical. The only citation difference is that the AI adds CN4 (a Common Notion about coincidence implying equality), which Heath leaves implicit. With an empty heath_only set and the same proof strategy in both texts, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 1.17
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: produce a side to create an exterior angle, invoke I.16 to establish that the exterior angle exceeds the remote interior angle, invoke I.13 to note that the supplementary angles equal two right angles, and conclude that the two selected interior angles sum to less than two right angles. The only difference is citation depth: the AI explicitly cites CN2 (equals added to unequals) and CN5 (the whole is greater than the part) to justify the algebraic inequality step, whereas Heath leaves these common-notion invocations implicit. Since heath_only is empty and ai_only contains only Common Notions (axioms), this is a clear Case A granularity difference with the AI over-citing at a finer axiomatic grain.

### 1.18
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct D on AC with AD = AB (I.3), join BD, establish the isosceles angle equality (angle ABD = angle BDA), apply the exterior angle theorem (I.16) to get angle BDA > angle BCA, note that angle ABC > angle ABD (whole greater than part), and chain the inequalities to conclude angle ABC > angle BCA. The AI proof explicitly cites I.5 for the isosceles result, CN4 for angle identification, CN5 for the whole-greater-than-part step, and P1 for joining BD, while Heath uses all of these implicitly without citation. Since heath_only is empty and all ai_only items are foundational results that Heath invokes without naming, this is a pure citation-depth difference with identical backbone, yielding G.

### 1.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate passed (both 1.5 and 1.18 precede 1.19). Q1 found no logical defect: the AI proof correctly uses I.5 to eliminate AC = AB and I.18 to eliminate AC < AB, concluding AC > AB by exhaustion, exactly mirroring Heath's elimination structure. Q2 confirmed the same backbone: both proofs establish the same two key intermediate conclusions (AC is not equal to AB, AC is not less than AB) via the same citations in the same logical positions. Since the citation sets are identical (ai_used = heath_refs = {1.5, 1.18}, Jaccard = 1.0) and the backbones match, the classification is P (Perfect match).

### 1.20
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct D on BA produced so that DA equals CA, use I.5 to establish base angle equality in the isosceles triangle ACD, apply CN5 to show angle BCD exceeds angle ADC, invoke I.19 to conclude DB exceeds BC, and then decompose BD into BA plus AC to reach the inequality. The AI proof cites the same three substantive references as Heath (1.19, 1.5, CN5) and adds six over-citations (1.3, CN1, CN2, CN4, P1, P2) that merely make explicit the construction postulates and common notions Heath leaves implicit. With an empty heath_only set and all ai_only items being construction or axiomatic references, this is a clear Case A: same backbone, different citation depth, yielding G.

### 1.21
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: extending BD to a point E, applying I.20 twice (on triangles ABE and CED/DEC) with additions to establish that BA+AC > BD+DC, then applying I.16 twice (on triangles CDE and ABE) to chain exterior angle inequalities and conclude that angle BDC > angle BAC. The ai_only set consists entirely of common notions (CN2, CN4, CN5) and a postulate (P2) that Heath uses implicitly without citation, while heath_only is empty. This is a clear Case A in Q2: same key intermediate conclusions at every logical position, differing only in citation depth where the AI explicitly cites axioms that Heath leaves implicit.

### 1.22
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same backbone construction: lay out one side of the triangle, draw two circles from its endpoints with radii equal to the other two given lengths, and take the intersection point as the third vertex. Heath places FG=B and draws circles centered at F (radius A) and G (radius C); the AI places AB=a and draws circles centered at A (radius b) and B (radius c). The core geometric argument is identical. The AI proof adds two elements of additional depth: an explicit proof that the triangle inequality is necessary (via 1.20) and a detailed justification for why the two circles must intersect (by showing one has a point inside and outside the other). All ai_only items are definitions, common notions, and postulates (CN1, CN2, CN3, CN5, D1.13, D1.15, D1.17, D1.18, D1.19, P1, P2, P3) that Heath uses implicitly but does not cite, and heath_only is empty. This is a clear case of same backbone with different citation depth, yielding G.

### 1.23
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: construct a triangle AFG with sides equal to the sides of triangle CDE (AF=CD, AG=CE, FG=DE), then apply SSS congruence (1.8) to conclude that angle FAG equals angle DCE. The AI proof adds explicit verification of the triangle inequality (1.20) to justify the construction, explicitly cites the construction proposition (1.22), and references definitions (D1.8, D1.9) and a postulate (P1) that Heath takes as understood. Since heath_only is empty and all ai_only items are construction-level or foundational references, this is a citation-depth difference with the same logical backbone, yielding G.

### 1.24
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof constructs angle EDG equal to angle BAC at point D, uses SAS (I.4) to establish BC = EG, then invokes isosceles triangle properties (I.5) and the angle-side relationship (I.19) to conclude EG > EF, hence BC > EF. The AI takes a fundamentally different route: it constructs a ray inside angle BAC with angle BAX = angle EDF and AX = AC, uses SAS to get BX = EF, then bisects angle XAC (I.9) to obtain XM = CM via a second SAS application, and finally applies the triangle inequality (I.20) to show BM + MX > BX, yielding BC > EF. The key intermediate conclusions differ entirely: Heath argues through angle comparison (I.5 and I.19), while the AI argues through an angle bisector and the triangle inequality (I.9 and I.20). Both proofs are logically complete, so this is a valid different path.

### 1.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow an identical logical structure: proof by elimination of two cases for the angle relationship. Both proofs assume first that angle BAC equals angle EDF and derive a contradiction via I.4 (yielding BC = EF, contradicting BC > EF), then assume angle BAC is less than angle EDF and derive a contradiction via I.24 (yielding EF > BC or BC < EF, again contradicting BC > EF), and conclude that angle BAC must be greater than angle EDF. The citation sets are identical (1.4 and 1.24), the Jaccard similarity is 1.0, and both ai_only and heath_only are empty. Since the key intermediate conclusions and the citation sets match exactly, this is a perfect match (P).

### 1.26
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share identical logical backbones across both required cases: Case 1 (side adjoining equal angles) uses proof by contradiction via SAS (I.4) to establish the unknown side equality, then SAS again for the remaining elements; Case 2 (side subtending equal angles) uses the same contradiction structure augmented by the exterior angle theorem (I.16). The ai_only set consists entirely of construction propositions (1.3), common notions (CN1, CN4, CN5), and a postulate (P1) that Heath employs implicitly without citation. Heath_only is empty. Every ai_only item corresponds to an underlying fact present in Heath's proof at the same logical position, confirming Case A of Q2: same backbone, different citation depth.

### 1.27
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction that assumes the two lines meet on each side of the transversal, applies I.16 (the exterior angle theorem) to derive a contradiction in each case, and concludes the lines are parallel by Def. 23. The AI proof explicitly works out both cases (Steps 2 and 3) while Heath handles the second with 'Similarly,' and the AI additionally cites Postulate 2 for producing the lines, which Heath invokes implicitly. Since ai_only contains only P2 (a construction postulate representing over-citation) and heath_only is empty, both proofs reach the same key intermediate conclusions at slightly different citation depths, satisfying Case A of Q2.

### 1.28
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs handle the two cases (exterior angle equals interior opposite angle; interior angles on same side sum to two right angles) through identical key intermediate conclusions: in case 1, vertical angles (1.15) yield equal alternate angles leading to parallelism via 1.27; in case 2, supplementary angles on a line (1.13) allow subtraction of the common angle to obtain equal alternate angles and again parallelism via 1.27. The AI proof cites the same three substantive propositions as Heath (1.13, 1.15, 1.27) and additionally makes explicit the foundational axioms and postulates (CN1, CN2, CN3, P2, P4) that Heath invokes implicitly. Since heath_only is empty and ai_only contains only common notions and postulates, this is a citation-depth difference with identical logical backbone, yielding G.

### 1.29
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing alternate angle equality through a reductio ad absurdum argument invoking Postulate 5 (parallel lines cannot meet), then deriving exterior angle equality via I.15 (vertical angles) and the interior angle sum via I.13 (supplementary angles). The AI proof is more explicit, handling both inequality directions separately (alpha > delta and alpha < delta) where Heath uses a single-direction contradiction, and citing foundational items (CN3 for subtraction, CN5 for whole-greater-than-part, D1.23 for the definition of parallels, P2 for line extension, P4 for right angle equality) that Heath employs implicitly. Since heath_only is empty and every ai_only item is a common notion, definition, or postulate rather than a substantive theorem, the difference is purely one of citation depth, not proof strategy. This is Case A of Q2: same backbone, different granularity.

### 1.30
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: draw a transversal across the three lines, apply I.29 twice to establish angle equalities with the middle line, then use CN1 (transitivity) to equate the angles at the two outer lines, and conclude parallelism. The ai_only citations P1 and P2 are construction postulates for the transversal (over-citation), and 1.28 is the AI's explicit citation for the final parallelism conclusion where Heath implicitly invokes I.27 via alternate angles. The key intermediate conclusions are identical in both proofs; only citation depth differs.

### 1.31
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: connect A to a point on BC, construct equal alternate angles at A using I.23, extend the line, and conclude parallelism via I.27. The only construction-level difference is that Heath joins A to a random point D on BC while the AI joins A to endpoint B, but this does not change the key intermediate conclusion (equal alternate angles imply parallelism). The ai_only set consists entirely of a definition (D1.23) and postulates (P1, P2), which the AI cites explicitly for basic construction and definitional steps that Heath leaves implicit. With heath_only empty and ai_only containing only non-substantive items, this is a clear citation-depth difference under Case A of Q2, yielding G.

### 1.32
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical path: construct CE parallel to AB via I.31, establish BAC = ACE by alternate angles (I.29), establish ECD = ABC by the exterior-angle property of parallels (I.29), combine to show ACD = BAC + ABC, then add ACB to reach the angle-sum result using I.13. The key intermediate conclusions are the same in both proofs. The only difference is that the AI explicitly cites CN1 (equals to equals), CN2 (addition of equals), and P2 (line production) where Heath leaves these foundational axioms and postulates implicit. Since ai_only contains only common notions and a postulate, and heath_only is empty, this is a clear case of over-citation with identical backbone, yielding G.

### 1.33
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same three key intermediate conclusions: (1) alternate angles ABC and BCD are equal via I.29 from the given parallels and transversal BC, (2) triangles ABC and DCB are congruent by SAS via I.4, yielding AC = BD and angle ACB = angle CBD, and (3) AC is parallel to BD via I.27 from those alternate angles. The AI proof adds CN4 (to justify BC = BC as a common side) and P1 (to justify joining the lines), both of which Heath uses implicitly without citation. Since the logical backbones are identical and the only differences are over-citations of foundational axioms, this is a granularity difference.

### 1.34
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: two applications of I.29 to establish alternate angles, I.26 (ASA) to conclude opposite sides and one pair of opposite angles are equal, CN2 to add angles for the second pair of opposite angles, and I.4 (SAS) to prove triangle equality for the diameter bisection. The AI's extra citations CN4 (self-equality of the common side) and P1 (drawing the diameter) are axiomatic over-citations of facts Heath uses implicitly, and heath_only is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 1.35
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish AD = EF via I.34 and CN1, (2) derive AE = DF, (3) prove triangle congruence by SAS via I.4 using two equal sides and the angle from I.29, and (4) conclude parallelogram equality by piece-wise subtraction/addition of equal triangles and common regions. The citation differences are entirely at the axiom level: the AI uses CN3/CN4 where Heath uses CN2 to establish AE = DF, and the AI adds CN5 and P2 for an explicit coincidence-case discussion and line extension that Heath leaves implicit. Since all ai_only items (CN4, CN5, P2) are common notions or postulates representing over-citation, and the sole heath_only item (CN2) is a common notion replaced by equivalent axiom-level reasoning, this is a same-backbone, different-depth scenario characteristic of G.

### 1.36
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the identical strategy of constructing an auxiliary parallelogram that shares a base with each of the two given parallelograms, applying I.35 twice, and concluding by transitivity via CN1. The AI constructs EFCD while Heath constructs EBCH, but these serve the same structural role and yield the same key intermediate conclusions. The only citation difference is that the AI explicitly cites Postulate 1 for joining points to form the auxiliary parallelogram, while Heath performs the same construction without citing P1. Since P1 is a construction postulate rather than a substantive proposition, this constitutes over-citation at the construction level, making this a granularity difference rather than a path difference.

### 1.37
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: construct two parallelograms on base BC using I.31, establish their equality via I.35, show each triangle is half its parallelogram via I.34, and conclude from the equality of the halves. The AI proof adds foundational citations (1.30 for parallel transitivity in the construction argument, D1.23 for the definition of parallel lines, P2 for line extension, and CN2/CN5 to explicitly justify that halves of equal things are equal) that Heath treats as understood. Since heath_only is empty and all ai_only items are definitional, axiomatic, or foundational elaborations of steps present in both proofs, this is Case A: same backbone with different citation depth, yielding G.

### 1.38
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct parallelograms on the equal bases between the same parallels (I.31), show the parallelograms are equal (I.36), show each triangle is half its respective parallelogram via the diagonal (I.34), and conclude the triangles are equal as halves of equals. The AI proof adds five over-citations not in Heath (1.30, D1.23, CN1, CN2, CN5) that make explicit what Heath leaves implicit: D1.23 and 1.30 justify why the constructed parallels meet the bounding line, and CN1, CN2, CN5 spell out the common-notion reasoning behind the halves-of-equals step that Heath states in brackets without citation. Since heath_only is empty and all ai_only items are foundational over-citations rather than substantive path divergences, this is Case A of Q2: same backbone at different citation depth, yielding G.

### 1.39
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs use the same reductio ad absurdum backbone: construct an auxiliary point via a parallel line (I.31), form a comparison triangle equal to the original using I.37, derive a contradiction using the given equality and CN1, and conclude that the line joining the vertices is parallel to the base. The AI's construction differs superficially (drawing the parallel through vertex C rather than through vertex A as Heath does), but the key intermediate conclusions are identical. Heath's citation set is a proper subset of the AI's, and all ai_only items are either explicit citations of steps Heath leaves implicit (CN5 for the greater-to-less contradiction, P1 and P2 for construction postulates, D1.23 for the definition of parallels) or a subsidiary construction step (1.30, used to show two lines must intersect). No item in ai_only represents a genuinely different key geometric fact, confirming a citation-depth difference rather than a path divergence.

### 1.40
**Category**: Path difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Heath proves 1.40 by reductio ad absurdum: assuming AD is not parallel to BE, constructing AF parallel to BE via I.31, deriving triangle ABC = triangle FCE by I.38, then reaching a contradiction (DCE = FCE, greater to less) via CN1. The AI instead gives a direct proof: it constructs a line m through A parallel to the base line (I.31), shows ABC = AEF by I.38 on equal bases between parallels, derives AEF = DEF by CN1, and then invokes I.39 (the same-base converse: equal triangles on the same base and same side are in the same parallels) to conclude that A and D lie on the same parallel to the base line. The key intermediate conclusions differ fundamentally — Heath's backbone is a contradiction argument while the AI's is a direct chain through I.39. The AI's path is logically valid: I.39 properly applies to triangles AEF and DEF which share base EF, are equal, and lie on the same side.

### 1.41
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: use the diagonal AC to split the parallelogram into two equal triangles via 1.34, show one constituent triangle equals the external triangle via 1.37, and conclude the parallelogram is double the external triangle. The AI proof makes explicit the common notions (CN1 for transitivity, CN2 for addition) and the postulate (P1 for joining AC) that Heath uses implicitly, yielding ai_only = {CN1, CN2, P1} with an empty heath_only. This is Case A of Q2: same backbone with different citation depth, classifying as G.

### 1.42
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect BC to obtain equal segments, construct a parallelogram with the given angle on one half of BC, show the two sub-triangles are equal in area via I.38 (equal bases, same parallels), conclude the original triangle is double one sub-triangle, then apply I.41 to show the parallelogram is also double that sub-triangle, yielding equality. The AI's extra citations (1.10 for bisection, 1.30 and D1.23 for parallel-line intersection arguments, CN1 and CN2 for equality reasoning, P1 and P2 for constructive postulates) make explicit what Heath leaves implicit but do not alter the logical backbone. Heath cites nothing that the AI omits. This is a same-backbone, different-depth scenario, hence G.

### 1.43
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that the diagonal bisects the whole parallelogram (I.34), that the diagonals of the two sub-parallelograms about the diameter bisect those sub-parallelograms (I.34), combine the resulting equal triangle pairs (CN2), and subtract equals from equals to conclude the complements are equal (CN3). The only citation difference is the AI's inclusion of Postulate 1 for drawing the diameter, a construction step that Heath leaves implicit. Since the key intermediate conclusions are identical and the citation difference is limited to a construction postulate, this is a granularity difference.

### 1.44
**Category**: Granularity difference
**Jaccard**: 0.538
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct parallelogram BEFG equal to the given triangle in the given angle (I.42), draw a parallel through A (I.31), show lines HB and FE meet at K using the parallel postulate (Post.5), draw through K a parallel to AB forming the larger parallelogram (I.31), apply the complement theorem (I.43) to equate the result parallelogram with BEFG and hence with the given triangle, and establish the angle equality via vertical angles (I.15). The AI proof cites six additional items (1.17, 1.23, 1.30, CN2, P1, P2) that Heath uses implicitly or bundles within other references: 1.23 for angle construction (subsumed by Heath's I.42 reference), 1.17 for the angle-sum inequality, 1.30 for transitivity of parallelism, and postulates and common notions for elementary construction and arithmetic steps. Heath cites nothing the AI omits (heath_only is empty). Since the key intermediate conclusions are identical and the citation differences reflect only the depth of explicit justification, this is a granularity difference.

### 1.45
**Category**: Granularity difference
**Jaccard**: 0.467
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: triangulate the rectilineal figure, construct the first parallelogram in the given angle via I.42, iteratively adjoin each remaining triangle as a parallelogram via I.44, establish collinearity of the extended sides using I.29 and I.14, show the combined figure is a parallelogram, and conclude by area addition. The heath_only citations (I.33, I.34) are used by Heath to establish that the combined figure is a parallelogram (I.34 gives equal and parallel opposite sides, I.33 gives equal and parallel joining lines), while the AI reaches the same conclusion via I.30 (transitivity of parallelism) and D1.23 (definition of parallel lines). This is a citation-depth difference for the same intermediate conclusion, not a backbone divergence. The ai_only items (1.31, CN4, D1.19, D1.23, P1, P2) are construction propositions, definitions, common notions, and postulates reflecting the AI's more explicit triangulation procedure and alternative parallelism argument, all consistent with over-citation rather than path divergence.

### 1.46
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a parallelogram with one right angle and two adjacent equal sides, show all four sides equal via I.34 and the construction, show all four angles right via I.29 on co-interior angles and I.34 on opposite angles, then conclude the figure is a square. The AI proof cites all four of Heath's references (1.11, 1.29, 1.31, 1.34) and adds eight further citations (1.3, 1.30, CN1, CN3, D1.22, D1.23, P2, P4) that are construction steps, definitions, common notions, and postulates Heath invokes implicitly. Since heath_only is empty and every ai_only item is either a construction detail or an explicitly cited axiom/definition, the proofs establish the same key intermediate conclusions at different citation depths, yielding G.

### 1.47
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the identical logical backbone: construct squares on all three sides of the right triangle (I.46), draw a line through the right-angle vertex parallel to the sides of the hypotenuse square to divide it into two rectangles, establish collinearity of certain vertices (I.14), prove two pairs of congruent triangles via SAS (I.4), relate each triangle to a rectangle and a square using the double-area relationship (I.41), and sum to reach the Pythagorean conclusion (CN2). The heath_only set is empty, confirming the AI cites every proposition Heath does. The 13 ai_only items are all over-citations that make explicit what Heath leaves implicit: definitions (D1.10, D1.21, D1.22, D1.23), postulates (P1, P2, P4, P5), a common notion (CN1), the perpendicular-construction proposition (1.12), propositions used to prove the perpendicular foot lies between the hypotenuse endpoints (1.16, 1.17), and the proposition justifying parallelism from perpendicularity (1.28). The logical backbone is identical; only the citation depth differs.

### 1.48
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct point D with AD perpendicular to AC and AD equal to AB, apply the Pythagorean theorem (I.47) to right triangle DAC to obtain DC squared equals DA squared plus AC squared, combine with the hypothesis to deduce DC equals BC, then apply SSS congruence (I.8) to conclude angle DAC equals angle BAC and hence angle BAC is right. The heath_only set is empty, meaning the AI cites every proposition Heath does. The ai_only set consists entirely of construction propositions (1.11, 1.3, 1.46), postulates (P1, P2, P4), common notions (CN1, CN2, CN4, CN5), and definitions (D1.10, D1.22), all of which justify individual sub-steps that Heath leaves implicit. This is a clear Case A in Q2: same key intermediate conclusions at different citation depth.
