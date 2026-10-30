# GPT (GPT-6-Astra) — Classification Report (All Books)

## Overall Summary

| Book | P | G | D | E | Total |
|---|---|---|---|---|---|
| 1 | 3 | 43 | 2 | 0 | 48 |
| 2 | 0 | 5 | 9 | 0 | 14 |
| 3 | 0 | 25 | 12 | 0 | 37 |
| 4 | 0 | 12 | 4 | 0 | 16 |
| 5 | 2 | 19 | 4 | 0 | 25 |
| 6 | 0 | 21 | 12 | 0 | 33 |
| 7 | 0 | 29 | 10 | 0 | 39 |
| 8 | 2 | 17 | 8 | 0 | 27 |
| 9 | 2 | 16 | 18 | 0 | 36 |
| 10 | 0 | 68 | 47 | 0 | 115 |
| 11 | 0 | 24 | 15 | 0 | 39 |
| 12 | 0 | 7 | 11 | 0 | 18 |
| 13 | 0 | 9 | 9 | 0 | 18 |
| **Total** | **9** | **295** | **161** | **0** | **465** |

---

## Book 1 — Classification Report (GPT)

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


---

## Book 2 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 5 | 2.1, 2.11, 2.12, 2.13, 2.14 |
| Path difference (D) | 9 | 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10 |
| AI proof error (E) | 0 |  |

**Total**: 14 propositions

## Per-Proposition Analysis

### 2.1
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a rectangle with one side equal to the uncut line using a perpendicular and equal-length construction, divide it into sub-rectangles by drawing parallels through each division point, show each sub-rectangle has a side equal to the uncut line via I.34, and conclude the whole rectangle equals the sum of the sub-rectangles. The AI proof is more explicit, citing definitions (D1.10, D1.23, D2.1), common notions (CN1, CN2, CN4), a postulate (P2), and intermediate parallel-line results (1.29, 1.30) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations of foundational material supporting the same construction, this is Case A of Q2: same backbone, different citation depth.

### 2.2
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves 2.2 by constructing a parallel line CF through C (using I.31) to decompose the square ADEB into two sub-rectangles AF and CE, then directly identifying each as the required rectangle. The AI instead applies Proposition 2.1 (the distributive law for rectangles) with AE as the uncut line and AB as the line cut at C, yielding R(AE,AB) = R(AE,AC) + R(AE,CB), and then substitutes AE = AB to reach the conclusion. These are genuinely different key intermediate conclusions: Heath's backbone is geometric decomposition via parallel lines, while the AI's backbone is algebraic application of the preceding proposition. The AI's path is logically complete and valid, so the classification is D.

### 2.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 2.3 by geometric construction: building a square on CB (I.46), drawing a parallel (I.31), then visually decomposing the resulting figure into rectangles and a square. The AI takes a fundamentally different path, invoking Proposition 2.1 directly as an algebraic decomposition theorem applied to BC (uncut) and AB (cut at C), yielding R(AB,BC) = R(AC,BC) + R(BC,BC), then identifying R(BC,BC) as the square on BC via 1.34 and D1.22. The two backbones share no key intermediate conclusions: Heath never uses 2.1 and the AI never constructs the geometric figure. The containment test confirms that while 1.31 appears in Heath's proof of 2.1, 1.46 does not, and the overall logical strategies are genuinely distinct. Q3 confirms the AI's path is valid: the application of 2.1 is correct, the square identification is sound, and the chain from premises to conclusion is complete.

### 2.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 2.4 by geometric construction: building a square ADEB on AB, drawing parallels, and using Book 1 propositions (I.29, I.5, I.6, I.34, I.46, I.31) to identify sub-regions as squares on the segments and rectangles. The AI takes a fundamentally different algebraic path, applying 2.2 to decompose S(AB) into R(AB,AC) + R(AB,CB), then applying 2.3 twice to expand each rectangle into a square plus a rectangle on the segments, yielding S(AC) + S(CB) + 2R(AC,CB). The proof-tree containment test confirms genuine divergence: Heath's proofs of 2.2 and 2.3 cite only I.46 and I.31, so the remaining heath_only items (1.29, 1.34, 1.5, 1.6) are not contained within those proofs. The Jaccard similarity is 0.0 with zero citation overlap, and the key intermediate conclusions differ entirely (geometric sub-region identification vs algebraic decomposition via earlier Book 2 results). Q3 confirms the AI's path is valid: each step correctly applies the cited proposition, and the chain runs soundly from premises to conclusion.

### 2.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs a square on CB with parallel lines, then reasons through complement equality (I.43), equal parallelograms on equal bases (I.36), and gnomon area relations to reach the conclusion. The AI proof takes a fundamentally different algebraic approach, applying Proposition 2.1 (rectangle distribution) three times to decompose both S(CB) and R(AD,DB) into matching sums of rectangles and squares. The proof-tree containment test fails because the heath_only propositions 1.36, 1.43, and 1.46 do not appear inside Heath's proof of 2.1, confirming these are independent routes rather than different citation depths of the same argument. The AI's algebraic path is logically complete: each application of 2.1 is correct, substitutions using AC = CB are valid, and the final combination via common notions CN1 and CN2 is sound. Since the backbones differ and the AI's path is valid, the classification is D.

### 2.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 2.6 via geometric construction: he builds a square on CD, draws parallel lines to form a grid, and uses parallelogram properties (I.36, I.43) with gnomon decomposition to reach the conclusion. The AI instead takes a purely algebraic route, applying 2.1 (rectangle distribution over segments) and 2.4 (square of a sum) to decompose and recombine areas arithmetically. The two backbones share no key intermediate conclusions -- Heath's pivots on AL = CH and CH = HF via parallelogram complements, while the AI's pivots on distributing R(AD,BD) via 2.1 and expressing S(CD) via 2.4. The citation sets are completely disjoint (Jaccard = 0.0), reflecting genuinely different proof strategies rather than mere granularity variation. The AI proof is logically complete: each step correctly applies the cited proposition, and the chain from premises to conclusion is sound.

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs a square on AB and uses geometric properties of complements about the diagonal (I.43) and gnomon manipulations to establish the identity, with key intermediate conclusions involving the equality of complementary parallelogram areas AG = GE and the gnomon-rectangle correspondence. The AI proof takes a fundamentally different algebraic path, applying the prior identities 2.3 (rectangle decomposition) and 2.4 (square on a whole line) directly and combining them via Common Notions to reach the conclusion without any geometric construction or gnomon reasoning. The zero Jaccard similarity and completely disjoint citation sets reflect this genuine path divergence. The AI's chain is logically complete: 2.4 decomposes S(AB), 2.3 identifies R(AB,AC) = S(AC) + R(AC,CB), and algebraic combination via CN1 and CN2 yields the result. Since the backbones are different and the AI proof is valid, the classification is D.

### 2.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 2.8 by geometric construction: building a square on AD, identifying equal sub-areas via complements (I.43) and equal parallelograms (I.36), assembling a gnomon equal to four times the rectangle AB,BD, and adding the square on AC to complete the full square on AD. The AI takes a fundamentally different algebraic route, applying proposition 2.4 to expand the square on AD and proposition 2.7 to relate the sum of squares on AB and BC to the rectangle and remaining segment, then combining these algebraically via CN1 and CN2 to obtain 4R(AB,BC) + S(AC) = S(AD). The key intermediate conclusions differ entirely: Heath works with geometric regions and complements, while the AI chains prior algebraic identities. The zero Jaccard similarity (no shared citations) confirms the complete divergence in method. The AI's path is logically valid since 2.4 and 2.7 are correctly applied and the algebraic steps are sound, yielding category D.

### 2.9
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof is entirely geometric: it constructs CE perpendicular to AB with CE equal to AC, draws parallels, and applies the Pythagorean theorem (I.47) three times along with angle-chasing (I.29, I.32), equal-angle side equality (I.6), and parallelogram properties (I.34) to build the result through right isosceles triangles. The AI takes a fundamentally different, purely algebraic path: it applies proposition 2.4 twice (once at the equal cut, once at the unequal cut) and proposition 2.5 once, then reaches the conclusion through arithmetic substitution using common notions, with no geometric construction at all. The two proofs share zero citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different -- Heath establishes angle equalities, side equalities EG = GF and FD = DB, and three Pythagorean applications, while the AI establishes Q(AB) = 4Q(AC) and R + Q(CD) = Q(AC) as its pivotal intermediates. Since the backbones differ (Case B in Q2), Q3 was applied: the AI's algebraic chain is logically complete and sound at every step, yielding category D.

### 2.10
**Category**: Path difference
**Jaccard**: 0.105
**Analysis**: The AI proof takes a fundamentally different path from Heath's by reducing Proposition 2.10 to Proposition 2.9. Heath constructs perpendiculars and parallels, performs extensive angle-chasing with isosceles triangles (I.5, I.6), and applies the Pythagorean theorem (I.47) four times to build the result from Book I foundations. The AI instead extends BA beyond A, takes E with AE = BD, shows that C bisects ED, and applies 2.9 directly to the line ED cut unequally at A, yielding the result after a single substitution of equals. Q2 identifies different backbones (Case B): Heath's key intermediates are angle equalities, side equalities from isosceles triangles, and iterated Pythagorean applications, while the AI's key intermediate is the single observation that ED is bisected at C and cut unequally at A, enabling direct invocation of 2.9. Q3 confirms the AI's alternative path is logically complete and valid, giving classification D.

### 2.11
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: they construct the same figure (square on AB, bisect a side at E, extend to F with EF=EB), apply II.6 to obtain rect(CF,FA)+sq(AE)=sq(EF), apply I.47 to obtain sq(EB)=sq(EA)+sq(AB), and subtract to derive the central intermediate rect(CF,FA)=sq(AB). The proofs differ only in how they bridge from this intermediate to the final result rect(AB,BH)=sq(AH): Heath uses direct geometric identification of named rectangles in the constructed figure (FK=AD, subtract AK, FH=HD), while the AI uses II.1 twice as an algebraic distribution rule. This is a difference in citation depth and algebraic method, not in backbone conclusions. The AI additionally over-cites foundational results (postulates, definitions, common notions, construction propositions) and adds triangle inequality justifications (1.17, 1.19, 1.20) for the construction that Heath leaves implicit. Since heath_only is empty and all ai_only items represent either foundational over-citation or an alternative algebraic technique for the same logical step, Case A of Q2 holds.

### 2.12
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: drop a perpendicular from a vertex to the opposite side produced beyond the obtuse angle, apply 2.4 to the resulting segment cut at the triangle vertex to obtain the twice-rectangle term, apply 1.47 twice to the two right triangles formed by the perpendicular, then combine algebraically to reach the conclusion. The only difference is labeling (Heath places the obtuse angle at A, the AI at B) and citation depth: the AI explicitly cites definitions (D1.10, D1.11, D1.21, D1.22, D2.1), common notions (CN1, CN2, CN5), postulates (P2), and construction propositions (1.12, 1.17) that Heath leaves implicit. Since heath_only is empty and all ai_only items are foundational or construction citations, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 2.13
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: drop perpendicular AD from A to BC, apply 2.7 to the line BC cut at D, apply 1.47 (Pythagorean theorem) to both right triangles ABD and ACD, then combine algebraically to conclude that the square on AC is less than the squares on CB and BA by twice the rectangle CB, BD. The AI proof is substantially more explicit, citing definitions (D1.10, D1.12, D1.21, D1.22, D2.1), common notions (CN1, CN2, CN3, CN5), construction references (1.12, P2), and adding a dedicated argument using 1.16 to prove that the perpendicular foot D lies strictly between B and C, which Heath takes as implicit. Since heath_only is empty and all ai_only items are over-citations or auxiliary arguments rather than substantive path differences, this is Case A of Q2: same backbone, different citation depth.

### 2.14
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a rectangle equal to the given figure (I.45), apply II.5 to obtain a rectangle-plus-square equals a square relation, apply I.47 (Pythagorean theorem) to obtain another square decomposition, subtract the common square to show the rectangle equals the square on a constructed segment, and conclude. The AI proof handles both cases (already a square vs. main construction) just as Heath does. The ai_only set contains 18 items, but all are construction sub-steps (1.3, 1.10, 1.11), parallelogram properties cited explicitly (1.29, 1.34), definitions (D1.10, D1.15, D1.22, D2.1), common notions (CN1, CN3, CN4, CN5), postulates (P1, P2, P3, P4), and the final square construction (1.46) -- all steps Heath performs implicitly or without explicit citation. heath_only is empty, confirming the AI cites everything Heath does and more. This is a clear case of same backbone with different citation depth.


---

## Book 3 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 25 | 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.11, 3.12, 3.14, 3.17, 3.18, 3.20, 3.21, 3.22, 3.23, 3.26, 3.27, 3.28, 3.29, 3.31, 3.32, 3.33, 3.34, 3.35, 3.36 |
| Path difference (D) | 12 | 3.1, 3.8, 3.9, 3.10, 3.13, 3.15, 3.16, 3.19, 3.24, 3.25, 3.30, 3.37 |
| AI proof error (E) | 0 |  |

**Total**: 37 propositions

## Per-Proposition Analysis

### 3.1
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 determined the classification. Heath's proof uses reductio ad absurdum: it constructs the midpoint F of a perpendicular chord CE, assumes some other point G is the centre, and derives a contradiction via I.8 (angle GDB would be right but angle FDB is already right, yielding greater equals less). The AI proof instead takes a direct constructive approach with case analysis: it proves the centre must lie on the perpendicular bisector of chord AB (handling O on AB and O not on AB separately, using I.8 in the latter case), then locates the centre by bisecting the resulting diameter. These are genuinely different key intermediate conclusions and different logical architectures (reductio vs. direct construction with cases), so the backbones differ (Case B). Q3 confirms the AI's path is valid: every step is properly supported by citations and sound reasoning, with no gaps under the hardened 1(b) standard.

### 3.2
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: finding the center and establishing equal radii (via 3.1), deriving equal base angles (via I.5), applying the exterior angle theorem (I.16) to obtain an angle inequality, and converting that to a side inequality (via I.19) to show every point on the chord is closer to the center than the radius. The AI uses a direct proof rather than Heath's contradiction, and adds an explicit sub-case for the center lying on line AB, but the core geometric mechanism and key intermediate conclusions are identical. The ai_only set consists entirely of axiom-level over-citations (CN5, D1.15, P1) that Heath leaves implicit, and heath_only is empty. This is a clear Case A in Q2: same backbone, different citation depth.

### 3.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same biconditional through identical key intermediate conclusions: in the first direction, SSS congruence (I.8) yields equal adjacent angles, which are then right by definition (D1.10); in the second direction, equal radii give equal base angles (I.5), equal right angles and a shared side give triangle congruence (I.26), yielding equal segments. The AI proof cites four additional foundational items (CN4, D1.15, P1, P4) that Heath leaves implicit, all of which are common notions, definitions, or postulates rather than substantive propositions. Since heath_only is empty and the ai_only items are purely axiom-level over-citations, the backbones match and the difference is one of citation depth, yielding G.

### 3.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume for contradiction that two non-diametral chords bisect each other at E, find the centre, join it to E, apply 3.3 twice to conclude that two angles at E are both right, then observe that one angle is a proper part of the other, yielding a contradiction. The AI proof explicitly cites CN5 (whole greater than part), P1 (joining a line), and P4 (right angles are equal), which Heath invokes implicitly. Since heath_only is empty and all ai_only items are axiom-level citations (common notions and postulates) representing the same reasoning at greater depth, Case A of Q2 holds: same key intermediate conclusions, different citation depth.

### 3.5
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume a common centre, then show via the definition of centre (D1.15) that two radii force two geometrically unequal segments to be equal, yielding a contradiction. Heath's proof uses segments EC=EF and EC=EG along a random line EFG; the AI's proof uses OA=OB and OA=OC along a line from O through B to C. The key intermediate conclusion is identical in both: two segments, one a proper part of the other, are shown equal through the centre definition, producing a contradiction. The AI simply cites more foundational references explicitly (CN1 for transitivity, CN5 for the whole-greater-than-part axiom, D1.16 for the circle definition, P1 and P2 for line constructions), while Heath leaves these implicit. With heath_only empty and ai_only consisting entirely of common notions, definitions, and postulates, this is a clear case of over-citation at the same backbone, giving Granularity difference (G).

### 3.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use proof by contradiction assuming a common centre, then show that equal radii from that centre to points on each circle yield a contradiction with unequal distances. Heath draws a random line FEB through the supposed centre F to get FC = FB (first circle) and FC = FE (second circle), deriving FE = FB which contradicts FE < FB. The AI uses the touch point A and a chosen point B on the first circle (not on the second), finding C on the second circle along ray OB, to get OB = OA and OC = OA, deriving OB = OC which contradicts CN5 since B and C are distinct on the same ray. The key intermediate conclusions are the same: radii from the common centre are forced equal but the geometry makes them unequal. The entire ai_only set (CN1, CN5, D1.15, D1.16, D3.3, P1, P2) consists of definitions, common notions, and postulates that Heath uses implicitly without explicit citation. Heath has no explicit citations at all, so the Jaccard is 0.0, but this reflects only that the AI is more explicit about foundational references, not a path divergence.

### 3.7
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: the triangle inequality (I.20) with radii equality establishes the greatest and least lines, the SAS inequality (I.24) with equal radii, common side, and angle comparison establishes the ordering of intermediate lines, and angle construction (I.23) combined with SAS congruence (I.4) proves that exactly two equal lines exist. The ai_only set consists entirely of common notions (CN2, CN3, CN5), definitions (D1.15, D1.17), and postulates (P1, P2), which are foundational items Heath uses implicitly but the AI cites explicitly. Since heath_only is empty and all key intermediate conclusions appear in both proofs at the same logical positions, this is Case A of Q2: same backbone, different citation depth.

### 3.8
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined the classification. Heath uses 1.21 (lines constructed within a triangle from its extremities are shorter than the remaining two sides) for the convex circumference ordering, while the AI employs angle comparison arguments and the hinge theorem (1.24) uniformly for both concave and convex cases. Since 1.21 does not appear inside the proof of 1.24 (containment test fails), this constitutes a genuine backbone difference rather than a citation-depth variation. The AI also takes a distinct approach to uniqueness, applying 1.7 directly to show at most one circumference point on each side of the least segment can yield a given distance, instead of Heath's construction-plus-contradiction method using 1.4 and previously proved ordering results. Both alternative paths are logically sound, so Q3 confirms the classification as D.

### 3.9
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification. Heath proves 3.9 directly by bisecting two chords (AB and BC), using I.8 to show the bisecting lines are perpendicular, invoking III.1 to conclude each perpendicular bisector passes through the center, and noting their unique intersection is D. The AI instead proves 3.9 by contradiction: assuming the point P is not the center, it finds the actual center O via 3.1, constructs the diameter through O and P, and applies 3.7 to conclude that at most two equal straight lines can fall from P on the circle, contradicting the hypothesis of three. These are fundamentally different logical backbones — direct construction versus proof by contradiction via a different theorem — placing this squarely in Case B of Q2. The AI's chain is logically complete under Q3(b), so the classification is D.

### 3.10
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath proves 3.10 by contradiction using the perpendicular-bisector method: assuming four intersection points, he bisects chords between them and draws perpendiculars that, by 3.1, must pass through the center, forcing both circles to share a single center in contradiction to 3.5. The AI takes a fundamentally different route: assuming three intersection points A, B, C, it notes that the center T of the second circle sends three equal radii TA = TB = TC to the circumference of the first circle, then invokes 3.7 (interior point) and 3.8 (exterior point) to show that at most two equal lines can fall from any point to a circle, yielding a contradiction in every case. The two backbones share no key intermediate conclusion: Heath never invokes 3.7 or 3.8, and the AI never constructs perpendicular bisectors. The AI's path is logically complete under Q3, so the classification is D.

### 3.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy: assume the line through the two centers does not pass through the point of internal tangency, form a triangle with the two centers and the contact point, apply the triangle inequality, substitute equal radii, and derive a length contradiction. The key intermediate conclusions (triangle inequality on the centers-contact triangle, radii substitutions, length contradiction) are identical in both proofs. The only difference is citation depth: Heath leaves all references implicit (heath_refs is empty), while the AI explicitly cites 1.20 for the triangle inequality, 3.6 for the distinctness of centers, definitions D1.15, D1.16, D3.3, common notions CN1, CN2, CN5, and postulates P1, P2. Since the logical backbone is the same and the citation differences reflect only explicitness of referencing, this is a granularity difference.

### 3.12
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish a relationship between the center-to-center distance and the sum of the two radii to the contact point, then invoke I.20 (the triangle inequality) to derive a contradiction with the assumption that the centers and the contact point are not collinear. Heath's proof assumes the line FG does not pass through A and shows FG > FA + AG from the path FCDG while I.20 gives FA + AG > FG; the AI proof shows OP >= OT + PT from radii equalities and then applies I.20 to get OT + TP > OP if not collinear. The ai_only set consists entirely of definitions (D1.15, D1.16, D3.3), common notions (CN2, CN5), a postulate (P1), and one foundational result (3.6, that touching circles have distinct centers) -- all items Heath uses implicitly without citation. heath_only is empty. This is Case A: same backbone with different citation depth, yielding G.

### 3.13
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves the internal case by placing the contact points on the centre-line (3.11) and deriving a distance-domination contradiction (BG > HD implies BH much greater than HD, yet BH = HD), and the external case by an entirely separate argument using 3.2 (a chord falls inside a circle) to show the joining line is simultaneously inside one circle and outside the other. The AI instead unifies both cases: it applies 3.11 and 3.12 individually to each supposed contact point to establish that both contact points and both centres are collinear, then shows each centre must lie strictly between the two contact points (by equal radii and CN5), and derives AO < AQ = QB < OB = AO, a single contradiction covering both internal and external tangency. The backbones differ in structure (Heath separates cases with different methods; the AI merges them via betweenness), and the containment test confirms independence: 3.2 (heath_only) does not appear in Heath's proof of 3.12 (ai_only). The AI's chain is logically complete under the hardened 1(b) standard, so Q3 yields D.

### 3.14
**Category**: Granularity difference
**Jaccard**: 0.158
**Analysis**: Q2 decides the classification. Both proofs follow the same logical backbone: drop perpendiculars from the centre to the two chords, note that these perpendiculars bisect the chords (3.3), apply the Pythagorean theorem (1.47) to the resulting right triangles, and use the equality of radii to equate the sums of squares, then subtract equal terms to obtain the desired conclusion in each direction of the biconditional. The AI's sole heath_only gap (3.1, finding the centre) is a construction step the AI handles implicitly by assuming the centre exists. The AI's large ai_only set consists primarily of over-citations: definitions (D1.10, D1.15, D1.17, D1.22), common notions (CN1-CN5), postulates (P1, P4), and basic constructions (1.10, 1.3). The substantive ai_only propositions (2.4, 1.20) appear in ancillary arguments -- a lemma about equal squares having equal sides in Step 2, and the diameter special case in Step 7 -- that supplement the shared backbone without altering it. Since the key intermediate conclusions are the same and the differences are in citation depth and supplementary elaboration, this is a granularity difference.

### 3.15
**Category**: Path difference
**Jaccard**: 0.118
**Analysis**: Q2 revealed genuinely different backbones, and Q3 confirmed the AI's alternative path is valid, yielding category D. Heath's proof constructs an auxiliary chord MN at the same distance from the center as BC, uses 3.14 to establish MN = BC, then compares triangles by unequal included angles via 1.24 to show MN > FG. The AI's proof takes an entirely different route: it bisects the chords, obtains perpendicular distances via 3.3, applies the Pythagorean theorem (1.47) to right triangles formed by the radii and half-chords, then uses algebraic manipulation of squares (2.4) to show the half-chord of the nearer chord exceeds that of the more remote chord. The two proofs share almost no substantive citations (Jaccard 0.118), with heath_only containing 1.24 and 3.14 and ai_only containing 1.47, 2.4, 3.3 among others. Neither the containment test nor any logical defect applies; the AI's Pythagorean-algebraic chain is complete and sound.

### 3.16
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. The two proofs establish the same three assertions (tangent outside, no interposition, angle comparisons) but through genuinely different key intermediate conclusions at every stage. For Part 1, Heath uses the isosceles triangle theorem (I.5) in a contradiction proof, while the AI uses a direct distance comparison via I.17 and I.19. For Part 2, Heath drops a perpendicular from the center to the interposed line and derives a contradiction from radius vs perpendicular-distance inequality, whereas the AI constructs a symmetric point across a perpendicular foot using SAS congruence (I.4) and then invokes chord containment (3.2) to show every ray inside the angle immediately enters the circle. For Part 3, Heath argues indirectly from part 2, while the AI directly constructs rays at any given acute angle using I.23. These different backbones, confirmed by the very low Jaccard similarity (0.1) and the large set of substantive ai_only propositions (1.4, 1.12, 1.16, 1.23, 3.2), constitute a genuine path difference. The AI proof is logically complete under the hardened Q1(b) standard, so Q3(b) confirms a valid alternative path.

### 3.17
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct an auxiliary circle with the given point's distance as radius, use a perpendicular construction to create a right angle, apply SAS congruence (I.4) to transfer that right angle to the tangent point, and conclude tangency via III.16. The AI's ai_only set consists entirely of postulates (P1, P2, P3), common notions (CN4, CN5), definitions (D1.10, D1.15, D1.17, D3.2), and one construction proposition (1.11) that Heath uses implicitly without citing. Heath_only is empty. The AI also adds an extra case (point on the circumference), but the core argument for the main case matches Heath's backbone exactly, making this a citation-depth difference rather than a path difference.

### 3.18
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: a contradiction argument assuming the radius to the point of contact is not perpendicular to the tangent, drawing a perpendicular from the center instead, and deriving two contradictory inequalities about the perpendicular distance versus the radius using I.17 and I.19. The AI proof elaborates steps that Heath leaves implicit, explicitly citing 1.12 for the perpendicular construction, 3.2 and D3.2 to justify the perpendicular foot lies outside the circle, CN5 for the whole-greater-than-part inference, and various definitions and postulates. Since heath_only is empty and all ai_only items are over-citations or explicit supporting details for the same logical backbone, this is Case A of Q2: same key intermediate conclusions, different citation depth.

### 3.19
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves 3.19 by contradiction: assuming the centre F is not on the perpendicular AC, he derives via 3.18 that FC is perpendicular to the tangent, yielding angle FCE equal to angle ACE (the less to the greater), a contradiction. The AI instead gives a direct proof: it establishes via 3.18 that OT is perpendicular to the tangent, notes the drawn line n is also perpendicular to the tangent at T, shows the adjacent angles sum to two right angles, and applies 1.14 to conclude OT and n are collinear, so the centre lies on n. The key intermediate conclusions differ fundamentally — Heath's pivotal step is an angle-inequality contradiction under the assumption the centre is off the perpendicular, while the AI's pivotal step is a collinearity argument via 1.14. This constitutes a genuine path difference. The AI's direct proof is logically complete and sound, so Q3 confirms D.

### 3.20
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: forming isosceles triangles from radii and applying I.5, then using the exterior angle theorem I.32 to establish the doubling relationship for each sub-angle, and finally combining results by addition (center inside the inscribed angle) or subtraction (center outside). The AI proof is more explicit about case enumeration (diameter, interior, exterior) and explicitly cites definitions (D1.15, D1.17, D3.9, D3.10), common notions (CN2, CN3, CN4), and postulates (P1, P2) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, common notions, and postulates rather than substantive theorems, this is a clear case of over-citation with identical backbone, yielding G.

### 3.21
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: find the center, apply 3.20 twice to show the central angle is double each inscribed angle, then conclude the inscribed angles are equal. The AI proof adds substantial over-citation (3.1 for finding the center, definitions D1.17/D3.6/D3.8/D3.9, postulates P1/P2, and common notions CN1/CN2/CN5) and an extra case analysis for arcs larger than a semicircle, but these are citation-depth elaborations, not backbone differences. heath_only is empty, confirming no missing steps. Since the backbones match but citation sets differ, this is a granularity difference.

### 3.22
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: drawing diagonals AC and BD, using the inscribed angle theorem (III.21) to equate angles in the same segment, and applying the triangle angle sum (I.32) to conclude that opposite angles of the cyclic quadrilateral sum to two right angles. The AI proof is more explicit, providing a full argument for both pairs of opposite angles rather than Heath's 'similarly' for the second pair, and citing foundational items (CN1, CN2, CN4, D3.8, D4.3, P1) that Heath leaves implicit. Since the key intermediate conclusions are identical and the citation differences are purely at the axiom and definition level, this is a granularity difference.

### 3.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs argue by contradiction through the same backbone: assume two similar unequal segments on the same side of AB, construct a line through points on both arcs meeting at B, establish angle equality from the definition of similar segments (D3.11), then derive a contradiction via the exterior angle theorem (I.16). The AI proof adds explicit citations for the geometric configuration (3.10 to justify nesting of segments, definitions D3.6 and D3.8 for segment terminology, postulates P1 and P2 for line constructions, and CN4 for equality reasoning), but these elaborate on the same logical steps rather than introducing different key intermediate conclusions. With heath_only empty and ai_only consisting entirely of foundational items plus one configurational proposition, this is a clear Case A: same backbone at different citation depth.

### 3.24
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Both proofs use superposition to bring one segment onto the other's baseline, but the key reasoning step diverges. Heath argues by contradiction: if the segments do not coincide after superposition, one falls 'awry', meaning a circle cuts another circle at more than two points, contradicting III.10. The AI instead directly invokes III.23 (similar and unequal segments cannot be constructed on the same side of the same line) after superposition places both segments on the same base and same side. The proof-tree containment test confirms this is a genuine path difference: III.10 (heath_only) does not appear in Heath's proof of III.23 (which uses only Def. 11 and I.16), so these represent independent logical routes rather than citation-depth variation. The AI's path is valid, as III.23 directly yields equality once both segments share the same base and side. Q2 Case B leads to Q3, and Q3(b) holds, giving classification D.

### 3.25
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof proceeds by bisecting chord AC, drawing a perpendicular from the midpoint, then splitting into three cases based on whether angle ABD is greater than, equal to, or less than angle BAD, using I.6 (isosceles triangle theorem) and III.9 (circle through three equidistant points) to locate the center. The AI takes an entirely different path: it selects a third point C on the arc, constructs perpendicular bisectors of two chords AB and AC using I.10 and I.11, then applies III.3 (the perpendicular bisector of a chord passes through the center) to show the center lies on both perpendicular bisectors, with I.28 used to prove the two bisectors are distinct lines that must intersect at a unique point. This yields Jaccard 0.0 with completely disjoint citation sets, confirming different logical backbones. The AI's perpendicular-bisector method is logically complete and avoids the three-case structure entirely through a single general argument, making this a valid path difference.

### 3.26
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) equal radii from equal circles, (2) SAS (I.4) yields equal chords, (3) equal circumferential angles yield similar segments (D3.11), (4) similar segments on equal bases are equal (III.24), (5) subtracting equal segments from equal circles gives equal remaining circumferences. The AI proof adds explicit citations for definitions, common notions, and postulates that Heath leaves implicit, plus two substantive theorems (III.20 to unify the central and circumferential angle cases, I.13 for reflex angle handling) that elaborate on steps Heath treats more concisely. Since heath_only is empty and all ai_only items are either foundational over-citations or elaborations of the same logical steps, this is Case A of Q2: same backbone, different citation depth.

### 3.27
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs use an identical contradiction strategy to establish one type of angle equality (construct an equal angle with I.23, apply III.26 to obtain arc equality, reach contradiction), then derive the other type via III.20. Heath proves central angles first and derives circumference angles by halving; the AI reverses this order, proving circumference angles first and deriving central angles by doubling. The key intermediate conclusions are the same in both proofs. The ai_only citations (CN1, CN2, CN5, D3.9, P1, P2) are exclusively common notions, definitions, and postulates that Heath uses implicitly, representing over-citation of foundational items rather than a substantive path difference.

### 3.28
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: establishing that radii of equal circles are equal, applying SSS (I.8) to show the central angles are equal, invoking III.26 to conclude the lesser arcs are equal, and subtracting from equal whole circumferences to obtain equal greater arcs. The AI proof adds an explicit diameter sub-case (using 3.15) and over-cites by listing definitions (D1.15, D1.17, D1.18, D3.1, D3.9), common notions (CN1, CN3, CN4), a postulate (P1), and a construction proposition (3.1) that Heath leaves implicit. Since heath_only is empty and all ai_only items are supplementary citations or an extra sub-case rather than different key intermediate conclusions, this is Case A of Q2: same backbone, different citation depth.

### 3.29
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: equal arcs yield equal central angles via 3.27, radii of equal circles are equal, and SAS (1.4) gives equal chords. The AI adds explicit case analysis distinguishing semicircular, minor, and major arcs (Steps 2-3) and cites many foundational items (definitions D1.15, D1.17, D3.1, common notions CN3-CN5, postulate P1, and construction proposition 3.1) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, common notions, postulates, or a construction tool, this is classic over-citation with the same underlying argument, placing it squarely in Case A of Q2.

### 3.30
**Category**: Path difference
**Jaccard**: 0.083
**Analysis**: The classification is decided at Q2-Q3. Both proofs construct a perpendicular from the midpoint of chord AB to the arc and use I.4 (SAS) to establish triangle congruence. However, they extract different conclusions from the congruence and employ different bridge propositions to reach arc equality: Heath extracts chord equality (AD = DB) and applies III.28 (equal chords cut off equal arcs), while the AI extracts inscribed angle equality (angle BAC = angle ABC) and applies III.26 (equal inscribed angles stand on equal arcs). Since III.28 does not appear in the proof tree of III.26, the containment test confirms these are independent logical routes rather than a depth difference. The AI's path through inscribed angles is logically complete and valid, yielding a genuine path difference (D).

### 3.31
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: The forward dependency gate passes (all AI theorem citations precede 3.31). Q1 finds no logical errors: all five parts of this multi-case proposition are addressed, and every step is supported by cited propositions or sound reasoning. Q2 reveals that both proofs share the same backbone of key intermediate conclusions: both use I.5 on isosceles triangles formed by radii to decompose the inscribed angle, both apply I.32 (exterior angle theorem) to establish the angle in a semicircle is right via D1.10, both conclude the angle in the greater segment is less than a right angle, both use III.22 on a cyclic quadrilateral to show the angle in the less segment is greater than a right angle, and both handle the angles of the segments. The single heath_only citation (I.17) is replaced by a logically equivalent micro-argument: the AI derives angle ABC < R directly from angle ABC + angle ACB = R and CN5, whereas Heath invokes I.17 to reach the same conclusion. The 17 ai_only items consist overwhelmingly of definitions, common notions, postulates, and construction propositions that Heath leaves implicit, representing over-citation rather than a different proof path. Q2 Case A (same backbone, different citation depth) applies, yielding G.

### 3.32
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Both proofs follow the same logical backbone: establishing that the tangent is perpendicular to a diameter through the point of contact, using the angle in a semicircle (3.31), decomposing a right angle via the triangle angle sum (1.32), subtracting to obtain the first tangent-chord angle equality, and applying the cyclic quadrilateral property (3.22) for the second. The AI uses 3.18 (radius to contact point is perpendicular to tangent) where Heath uses its converse 3.19 (line perpendicular to tangent at contact passes through center); since 3.19 itself depends on 3.18, they establish the identical geometric fact at slightly different citation depth. The AI additionally cites 3.21 (angles in the same segment are equal) to generalize from a specific inscribed angle to all such angles, and explicitly lists construction steps (3.1, 3.2), definitions, common notions, and postulates that Heath leaves implicit. These are citation-depth differences, not backbone differences. Q2 Case A holds, yielding G.

### 3.33
**Category**: Granularity difference
**Jaccard**: 0.130
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct the given angle at one endpoint of the line, locate the circle center on the perpendicular bisector of AB, show the circle passes through both endpoints via I.4, establish tangency via III.16, and conclude that the angle in the appropriate segment equals the given angle via the tangent-chord relationship. The AI gives a unified argument covering all three angle types (acute, right, obtuse) through III.32 alone, while Heath separates into three explicit cases and uses III.31 for the right-angle case; this is a presentation choice, not a backbone difference, since III.32 subsumes the right-angle result of III.31. The large ai_only set (19 items) consists entirely of definitions, common notions, postulates, and construction propositions that Heath leaves implicit, confirming over-citation rather than path divergence. The sole heath_only item (3.31) is subsumed by the AI's uniform application of III.32. Same key intermediate conclusions at different citation depth yields G.

### 3.34
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs follow an identical backbone: draw a tangent to the circle, construct an angle between the tangent and a chord equal to the given angle using I.23, then apply the alternate segment theorem III.32 to conclude the angle in the alternate segment equals the given angle. The AI's seven extra citations (ai_only: 3.17, 3.2, CN1, D3.6, D3.8, P1, P2) are all over-citations of construction propositions, definitions, common notions, and postulates that Heath invokes implicitly without explicit reference. Heath cites nothing the AI omits (heath_only is empty). This is Case A of Q2: same key intermediate conclusions with different citation depth, yielding Granularity difference.

### 3.35
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a trivial case when the intersection is at the centre (equal radii yield equal rectangles), followed by establishing for each chord the identity rect(segments) + sq(distance-to-centre) = sq(radius) using III.3 for bisection, II.5 for the rectangle identity, and I.47 for the Pythagorean theorem, then combining via equal radii and subtracting the common square. The AI proof is more granular, handling additional sub-cases explicitly and citing foundational items (definitions D1.15, D1.22, D2.1; common notions CN1-CN4; postulate P1; construction propositions 1.10 and 3.1) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations of foundational elements, Case A of Q2 holds: same backbone, different citation depth.

### 3.36
**Category**: Granularity difference
**Jaccard**: 0.267
**Analysis**: Q2 decided the classification. Both proofs handle the same two cases (secant through the centre, secant not through the centre) and argue through identical key intermediate conclusions: tangent perpendicularity via III.18, bisection of the chord (implicit or via III.3), application of II.6 to the bisected-and-extended chord, Pythagorean theorem I.47 on right triangles, and cancellation using equal radii. The ai_only set consists entirely of over-cited foundational items (1.10 for bisection construction, 3.1 for finding the centre, common notions CN1-CN4, definitions D1.15/D1.17/D1.22/D2.1, and postulate P1) that Heath leaves implicit, while heath_only is empty. Since the logical backbones coincide and the citation difference reflects only citation depth, this is a granularity difference.

### 3.37
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decides this classification as D. Both proofs share the opening strategy of constructing a tangent and applying III.36 to equate squares, but their key intermediate conclusions diverge thereafter. Heath uses triangle congruence (I.8): he shows DE = DB, then with FE = FB and FD common concludes triangles DEF and DBF are congruent, transferring the known right angle at E to B. The AI instead uses the Pythagorean theorem and its converse (I.47, I.48): after establishing AT squared equals AD squared, it applies I.47 to the right triangle OAT to get OA squared = OT squared + AT squared, substitutes equal radii and equal squares to obtain OA squared = OD squared + AD squared, then invokes I.48 to conclude angle ODA is right. The containment test was checked since heath_only contains 1.8 which appears inside the proof of AI-cited I.48, but Heath is not re-deriving I.48 inline; rather Heath uses I.8 in an entirely independent congruence-based route that never reconstructs the Pythagorean converse argument. These are genuinely different logical backbones yielding a valid path difference.


---

## Book 4 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 12 | 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.9, 4.10, 4.11, 4.13, 4.14, 4.16 |
| Path difference (D) | 4 | 4.1, 4.8, 4.12, 4.15 |
| AI proof error (E) | 0 |  |

**Total**: 16 propositions

## Per-Proposition Analysis

### 4.1
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof inscribes the chord by cutting the diameter to the desired length and drawing an auxiliary circle to locate the endpoint on the given circle, a simple circle-intersection construction. The AI instead finds the center, verifies that the two radii and the desired length satisfy the triangle inequality, and constructs a triangle with those three sides via 1.22, deducing that the third vertex lies on the circle because its distance from the center equals the radius. These are genuinely different construction methods with different logical backbones, and the AI's path is logically complete, so the classification is D.

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs follow the same tangent-chord strategy: draw a tangent to the circle at a point A, construct angles between the tangent and two chords equal to two angles of the given triangle (I.23), apply the tangent-chord theorem (III.32) to show the inscribed triangle's angles equal those of the given triangle, and use the angle-sum property (I.32) for the remaining angle. The AI proof adds explicit citations for construction existence (3.17), postulates (P1, P2), common notions (CN1, CN2, CN3), a definition (D4.3), and auxiliary ordering lemmas (1.13, 1.17), all of which Heath uses implicitly. Since heath_only is empty and the ai_only items are entirely over-citations of construction steps and axioms, the backbone is identical at different citation depths, giving Granularity difference (G).

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share the same backbone: construct central angles equal to the exterior angles of the given triangle, draw tangent lines at the three determined points on the circle, establish that these tangent lines are perpendicular to the radii at the contact points, and then show each angle of the circumscribed triangle equals the corresponding angle of the given triangle. The single heath_only citation (3.18, tangent-radius perpendicularity) is addressed by the AI through reversed construction order: the AI constructs perpendiculars to the radii using 1.11 and then confirms tangency via 3.16, achieving the identical geometric fact that Heath obtains by drawing tangents first and citing 3.18 for perpendicularity. The AI's angle computation uses isosceles triangle base angles (1.5) and 1.32 on sub-triangles rather than Heath's quadrilateral angle sum approach, but both arrive at the same key conclusion that each vertex angle of the circumscribed triangle equals the corresponding angle of the given triangle. The fourteen ai_only items consist of definitions, common notions, postulates, and explicit construction steps (1.11, 1.5) that represent over-citation and additional detail rather than a different logical path.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.211
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: bisect two interior angles of the triangle, find their intersection point, drop perpendiculars to the three sides, use I.26 to show the three perpendicular distances are equal, draw a circle through the three feet, and argue tangency via III.16 to conclude the circle is inscribed (IV.Def.5). The AI bisects angles at A and B rather than B and C, which is immaterial. All 15 ai_only items are over-citations reflecting greater explicitness rather than a different proof strategy: construction propositions (1.12), postulates (P1-P5), definitions (D1.10, D1.12, D1.15, D1.17, D3.2), common notions (CN1, CN5), and subsidiary results (1.16, 1.17) used to justify steps that Heath leaves implicit, such as proving the bisectors meet and that the perpendicular feet lie on the sides. The heath_only set is empty, confirming that the AI covers all of Heath's reasoning. Case A of Q2 holds: same backbone, different citation depth.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect two sides of the triangle at their midpoints, draw perpendiculars at those midpoints, show the intersection point is equidistant from all three vertices using I.4, and conclude the circle centered there circumscribes the triangle. The AI proof adds an explicit proof by contradiction (using 1.14, 1.29, 1.30, 1.31) that the perpendicular bisectors must meet, whereas Heath addresses this by enumerating three cases of where the intersection might lie. The AI also over-cites by including construction references (1.11, P1, P2, P3), definitions (D1.10, D1.15, D1.23, D4.6), common notions (CN1, CN4), and a postulate (P4) that Heath leaves implicit. Since heath_only is empty and all key intermediate conclusions are the same in both proofs, this is a granularity difference where the AI provides greater citation depth than Heath.

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct two perpendicular diameters in the circle, join their endpoints to form quadrilateral ABCD, prove ABCD equilateral using I.4 (congruent triangles from equal radii and equal angles at the center), prove ABCD right-angled using III.31 (angles in semicircles are right), and conclude ABCD is a square by definition. The AI proof over-cites by explicitly listing construction propositions (1.11, 3.1), definitions (D1.10, D1.15, D1.17, D4.3), postulates (P1, P2, P4), a common notion (CN1), and vertical angles (1.15), all of which Heath's proof invokes implicitly. Since heath_only is empty and all ai_only items are construction-level or foundational references, this is Case A of Q2: same backbone, different citation depth.

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct two perpendicular diameters, establish tangent lines at the four endpoints that are perpendicular to the radii, show opposite tangent lines are parallel (1.28, 1.30), form parallelograms, prove the circumscribed quadrilateral has right angles and equal sides via parallelogram properties (1.34), and conclude it is a square. The only substantive citation difference is that Heath uses 3.18 (radius to point of tangency is perpendicular to the tangent) after constructing tangent lines via 3.16, while the AI reverses the logical direction by first constructing perpendicular lines at the diameter endpoints (1.11) and then using 3.16 to show these perpendiculars are tangent. The key intermediate conclusion -- that the tangent lines are perpendicular to the radii at the points of contact -- is established in both proofs, just from opposite directions. All other ai_only items are definitions, common notions, postulates, and construction propositions, representing over-citation rather than path divergence. This is Case A of Q2: same backbone, different citation depth.

### 4.8
**Category**: Path difference
**Jaccard**: 0.056
**Analysis**: Q2 decided the classification. Both proofs establish the same final conclusions (equal perpendicular distances from center to all four sides, tangency via III.16), but they reach these conclusions through fundamentally different methods. Heath bisects two sides (I.10), draws parallels through the midpoints (I.31), forms parallelograms, and uses I.34 to show equal opposite sides, thereby establishing equal distances from center G to the four sides. The AI instead joins the diagonals to find center O, uses SAS (I.4) to prove the diagonals bisect the square's angles, drops perpendiculars from O to each side (I.12), and applies AAS (I.26) to prove all four perpendicular distances are equal. The heath_only propositions (I.10, I.31, I.34) represent substantive geometric constructions and facts that are entirely absent from the AI proof, which never bisects a side, draws a parallel, or invokes parallelogram properties. Case A of Q2 therefore fails, yielding Case B (different backbone). Under Q3, the AI's alternative path is logically complete with every step explicitly justified, so the classification is D.

### 4.9
**Category**: Granularity difference
**Jaccard**: 0.091
**Analysis**: Both proofs follow the same logical backbone: join the diagonals of the given square, establish triangle congruence at adjacent vertices to show that the corresponding angles are equal, apply I.6 to conclude that the four distances from the diagonal intersection to the vertices are all equal, and then describe the circumscribed circle. The sole substantive divergence is that Heath invokes I.8 (SSS congruence) while the AI invokes I.4 (SAS congruence) to establish the triangle congruence at each pair of adjacent vertices -- both are valid congruence criteria reaching the identical intermediate conclusion (angle equality). The remaining ai_only items (CN1, CN4, D1.15, D1.22, D4.6, P1, P3, P4) are definitions, common notions, and postulates that Heath uses implicitly without citation. Q2 Case A holds: the key intermediate conclusions are identical, and the citation differences reflect granularity rather than a different proof path.

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.467
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: golden section construction (2.11), tangency to circumscribed circle (3.37), tangent-chord angle theorem (3.32), exterior angle theorem (1.32), and isosceles triangle properties (1.5, 1.6) leading to the conclusion that each base angle is double the vertex angle. The AI uses a different construction method (1.22 for three-side triangle construction instead of Heath's IV.1 chord-fitting approach) and adds explicit citations for common notions (CN1, CN2, CN4, CN5), a postulate (P1), a definition (D1.20), and 3.2 (to justify B lying outside the circumscribed circle), but these are all construction-level or axiom-level over-citations that do not alter the key intermediate conclusions. Since heath_only is empty and every ai_only item is either a construction proposition, common notion, postulate, definition, or supporting lemma, this is Case A: same backbone with different citation depth.

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: construct a special isosceles triangle with base angles double the vertex angle (4.10), inscribe an equiangular triangle ACD in the circle (4.2), bisect the two base angles to locate points E and B on the circle (1.9), deduce five equal inscribed angles and hence five equal arcs (3.26), five equal chords (3.29) for equilateral, then show interior angles stand on equal composite arcs and are therefore equal (3.27) for equiangular. The AI cites the same six substantive propositions as Heath; its ai_only set consists entirely of common notions (CN1, CN2, CN5), definitions (D3.9, D4.3), and postulates (P1, P2) that Heath leaves implicit. Heath_only is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding G.

### 4.12
**Category**: Path difference
**Jaccard**: 0.087
**Analysis**: Q2 determined the classification. Heath's proof works through the centre of the circle, using perpendicularity of radii to tangent lines (III.18), the Pythagorean theorem (I.47) to establish BK = CK, SSS congruence (I.8) to bisect angles at the centre, and equal arcs yielding equal central angles (III.27) to prove triangle congruences via ASA (I.26). The AI proof takes a fundamentally different route: it avoids the centre entirely, instead joining diagonals to establish an inscribed-angle beta via SAS (I.4) and isosceles base angles (I.5), then applying the tangent-chord theorem (III.32) to show each tangent makes angle beta with the adjacent pentagon side. Meeting of tangent rays is proved through angle-sum arguments (I.32, P5), and congruence of all five exterior triangles follows from the isosceles converse (I.6) and ASA (I.26). The key intermediate conclusions differ at every stage: centre-based perpendicularity and Pythagorean reasoning versus tangent-chord angles and isosceles-triangle theory. The AI's chain is logically complete under the hardened Q1(b) standard, so the different backbone yields D.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.150
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect two interior angles of the regular pentagon to locate the incenter, show all five vertex angles are bisected by lines from that center (via I.4 and symmetry), drop perpendiculars to all five sides and prove them equal by AAS (I.26), then construct the inscribed circle and establish tangency via III.16. The AI adds supplementary reasoning -- computing the interior angle sum via 1.32, invoking P5 to justify the intersection of bisectors, and citing 1.16 to verify perpendicular feet lie on the side segments -- but these do not alter the backbone. The ai_only set consists entirely of over-citations: postulates (P1-P5), common notions (CN1, CN2, CN3, CN5), definitions (D1.10, D1.15, D3.2, D4.5), and construction or auxiliary propositions (1.9, 1.12, 1.16, 1.32) that Heath leaves implicit. The empty heath_only set confirms that every proposition Heath cites is also cited by the AI, with no substantive divergence.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: bisect two adjacent interior angles of the regular pentagon, find their intersection as the center, prove all five distances from center to vertices are equal, and circumscribe the circle. Heath compresses the equidistance argument with I.6 and repeated 'similarly' clauses, while the AI spells out each equality explicitly, using I.6 for one pair (OB = OC) and I.4 (SAS) for the remaining pairs. The ai_only set consists entirely of over-citations: postulates (P1, P2, P3, P5), the bisection construction (I.9), common notions (CN1, CN2, CN3, CN5), definitions (D1.15, D4.6), and the substantive but supporting citations I.17 (angle sum bound ensuring bisectors meet) and I.4 (SAS as an alternative route to the same equidistance conclusion). Heath_only is empty. The key intermediate conclusions appear at the same logical positions in both proofs, making this a same-backbone, different-depth case.

### 4.15
**Category**: Path difference
**Jaccard**: 0.150
**Analysis**: Q2 identified a genuine backbone divergence in the second half of the proof. Both proofs establish that all six central angles equal one-third of two right angles using the same method (equilateral triangle properties via I.5 and I.32, then supplementary and vertical angles). However, they diverge on how they conclude the hexagon is equilateral and equiangular. Heath routes through arc theory: equal central angles imply equal arcs (III.26), equal arcs imply equal chords (III.29) for the equilateral claim, and equal arcs imply equal inscribed angles (III.27) for the equiangular claim. The AI instead uses triangle congruence: equal radii and equal central angles give SAS-congruent radial triangles (I.4), yielding equal bases (equilateral) and equal base angles whose pairwise sums give equal interior angles (equiangular). The key intermediate 'equal arcs' in Heath is entirely absent from the AI proof, and the key intermediate 'congruent radial triangles via SAS' in the AI is absent from Heath. Since the AI's path is logically complete and valid, the classification is D.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.062
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: inscribe an equilateral triangle side (1/3 = 5/15 of the circumference) and an equilateral pentagon side (1/5 = 3/15), observe the difference arc is 2/15, bisect it with III.30 to obtain 1/15, then fit equal chords in contiguity to complete the 15-gon. Heath's proof is extremely terse, explicitly citing only 3.30, while implicitly relying on 4.2 (inscribed triangle), 4.11 (inscribed pentagon), 4.1 (fitting equal chords), 3.26/3.28 (equal arcs from equal chords/angles), and 3.27 (equal angles on equal arcs). The AI proof makes all of these implicit dependencies explicit, along with supporting axioms (CN1, CN2, CN3, CN5), postulates (P1), definitions (D4.3), and lower-level construction results (1.1, 1.5, 3.15). Since heath_only is empty and every ai_only item is either an implicit dependency Heath uses without citation or a foundational axiom/definition, this is a clear Case A granularity difference: same backbone, different citation depth.


---

## Book 5 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 5.13, 5.19 |
| Granularity difference (G) | 19 | 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 5.8, 5.9, 5.11, 5.12, 5.14, 5.15, 5.16, 5.17, 5.20, 5.22, 5.23, 5.24, 5.25 |
| Path difference (D) | 4 | 5.6, 5.10, 5.18, 5.21 |
| AI proof error (E) | 0 |  |

**Total**: 25 propositions

## Per-Proposition Analysis

### 5.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same fundamental approach: decomposing equimultiples into their constituent equal parts, operating on corresponding parts, and reassembling to establish the conclusion. Heath's proof cites no theorems explicitly, while the AI proof explicitly cites CN1, CN2, CN3, and D5.2 (all common notions and a definition). The ai_only set contains only axiom-level citations with no substantive theorem divergence, and heath_only is empty, confirming that the AI over-cites foundational axioms that Heath uses implicitly. The key intermediate conclusions (decomposition into copies, pairing of corresponding parts, reassembly preserving multiplicity) are the same in both proofs. Case A of Q2 holds: same backbone, different citation depth, yielding G.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Both proofs establish the same key intermediate conclusions: decomposing each magnitude into counted equal parts of the measuring magnitude, combining the counts by addition, and concluding the sums share the same multiplicity. The AI proof explicitly cites CN2 (addition of equals to equals) and D5.2 (definition of equimultiple), which Heath's proof uses implicitly without formal citation. Since heath_only is empty and ai_only contains only a common notion and a definition (foundational-level items rather than substantive propositions), this is a clear case of the AI over-citing axiom-level references while following the identical logical backbone, producing a granularity difference rather than a path difference.

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: decomposing the equimultiples into parts equal to A and C, establishing that each corresponding pair maintains the equimultiple relationship with B and D, and then applying V.2 to recombine the parts into the final conclusion. The AI presents this argument in an explicitly iterative/inductive style (defining partial sums S_k, T_k and applying 5.2 successively), while Heath presents a more condensed Euclidean version (dividing EF into EK, KF and GH into GL, LH, then applying V.2 once). The only citation difference is that the AI adds D5.2 (Definition 5.2, the definition of equimultiple), which Heath uses implicitly without citation. Since D5.2 is a definition rather than a substantive proposition, this is a citation-depth difference, not a path difference.

### 5.4
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take arbitrary test multiples of the given equimultiples, apply 5.3 to show these test multiples are equimultiples of the original magnitudes, then invoke D5.5 twice (once with the ratio hypothesis A:B=C:D to obtain the comparison, once to conclude the new ratio). The only citation difference is the AI's additional reference to D5.2 (the definition of equimultiple), which Heath takes as understood. Since heath_only is empty and ai_only contains only a definition, this is a clear case of over-citation with identical backbone, yielding Granularity difference.

### 5.5
**Category**: Granularity difference
**Jaccard**: 1.000
**Analysis**: Q1 considered E because the AI mischaracterizes 5.1 as directly stating the subtraction/remainder result, when 5.1 actually proves the additive property of equimultiples. However, under the lenience rule, this is compressed-but-sound rather than invalid inference: 5.1 is the correct and sole tool needed (Heath uses only 5.1 and common notions), and the missing intermediate steps are expansions of a supported step, not a missing support relation. Q2 finds both proofs use the same backbone (5.1 as the sole citation) with the AI presenting a highly compressed version that omits the auxiliary construction and intermediate algebraic deductions Heath works through. Case A (same backbone, different depth) applies, yielding G.
**Audit Record**: CANDIDATE E -- 5.5
  violated_claim : Applied to the wholes A, B and the subtracted parts C, D, [5.1] establishes that R is the same multiple of S that A is of B
  failure_mode   : invalid_inference
  missing_is     : expansion (5.1 is the correct tool used by Heath; the intermediate construction and algebraic steps are expansions of the 5.1 application, not independent support)
  evidence       : AI text: "Choose the direct application of 5.1, whose statement as supplied has exactly these hypotheses. Applied to the wholes A, B and the subtracted parts C, D, it establishes that R is the same multiple of S that A is of B." Heath proof of 5.1 shows it proves the additive combination of equimultiples, not the subtraction result.
  why_not_terse  : RETRACTED -- missing_is = expansion; 5.1 is the key tool and the omitted steps are algebraic expansions using common notions, not an independent logical gap. Reclassified as NOT-E.

### 5.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof relies on Proposition 5.2 (adding equimultiples yields equimultiples) as its key mechanism: it constructs KH via V.2, shows KH equals CD, then subtracts to reach the conclusion. The AI proof takes a fundamentally different path, working directly from the definition of multiples (D5.2) and common notions through a copy-counting decomposition: it establishes that m < n (the number of copies subtracted is less than the total), decomposes each magnitude into its subtracted part and remainder, applies CN3 to identify the remainders, and concludes by counting the remaining copies. The AI never invokes the additive equimultiple property (5.2) and cites no theorems at all, only axioms and definitions. The containment test does not apply since the AI cites no higher-level proposition that could subsume 5.2. These constitute genuinely different logical backbones. Under Q3, the AI's alternative path is logically complete and sound, so the classification is D.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that equimultiples of equal magnitudes are equal, then apply Definition 5.5 twice to conclude A:C = B:C and C:A = C:B. The AI proof explicitly cites CN2 (to justify that adding equal magnitudes preserves equality) and D5.2 (the definition of multiple), which Heath leaves implicit. Since heath_only is empty and the ai_only items are a common notion and a definition rather than substantive propositions, this is a clear case of over-citation at a finer granularity, not a different proof path. The backbone is identical, making this a granularity difference.

### 5.8
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decompose the greater magnitude into two parts, use the Archimedean property (D5.4) on the lesser part to find a multiplier m, construct equimultiples of both magnitudes, locate a critical multiple of the common magnitude between those equimultiples, and apply D5.7 twice for both halves of the statement. The sole substantive heath_only citation, 5.1, is used by Heath to conclude that equimultiples of parts yield an equimultiple of the whole; the AI derives this same fact inline ('adding m copies of A=B+E gives mA=mB+mE') from definitions and common notions (D5.2, CN2, CN5). The ai_only items are all common notions and definitions that support this inline derivation, confirming a citation-depth difference rather than a path divergence. The AI also elegantly collapses Heath's two cases into one general argument by taking the minimum of the two parts, but the key intermediate conclusions remain the same.

### 5.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Both proofs establish the same two cases (A:C = B:C implies A = B, and C:A = C:B implies A = B) by the same method of contradiction via 5.8: if the magnitudes were unequal, 5.8 would yield differing ratios, contradicting the hypothesis of sameness. The ai_only items (D5.5, D5.7) are definitions that the AI cites to spell out why a greater ratio is incompatible with sameness of ratio, while Heath leaves this implicit in the single citation of 5.8. Since the key intermediate conclusions are identical and the citation difference consists entirely of definitions added for explicitness, Q2 Case A applies, yielding G.

### 5.10
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves both parts of the proposition by contradiction using two previously established comparison theorems: 5.7 (equal magnitudes have the same ratio) and 5.8 (the greater magnitude has the greater ratio). The AI takes a fundamentally different route by going directly to Definition 5.7 (the definition of greater ratio via equimultiples), extracting specific multiples m and n satisfying mA > nC and mB <= nC, deducing mA > mB from transitivity, and then deriving contradictions for A = B and A < B using Common Notions 2 and 5. The key intermediate conclusions differ: Heath's backbone rests on applying proved ratio-comparison theorems, while the AI's backbone rests on unpacking the definition to obtain a direct magnitude inequality between equimultiples. The proof-tree containment test does not apply because D5.7 is a definition, not a higher-level theorem encompassing 5.7 and 5.8. Since the AI's different path is logically sound and complete, the classification is D.

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs establish the transitivity of equal ratios using the same logical backbone: taking equimultiples, applying the equimultiple criterion from both proportion hypotheses to obtain matching comparison results, chaining through the shared middle pair, and concluding by the definition of same ratio. The AI proof is a straightforward relabeling of Heath's argument. The sole citation difference is that the AI explicitly cites Definition 5.5 (the equimultiple criterion for same ratio) while Heath applies it implicitly without formal citation, yielding ai_only = {D5.5} and heath_only = {}. Since the key intermediate conclusions are identical and only the citation depth differs, this is a granularity difference. It cannot be P because the citation sets are not equal.

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decides the classification as G. Both proofs share the same logical backbone: they establish that equimultiple comparisons agree across all pairs from the equal-ratio hypothesis, show that equimultiples distribute over sums, aggregate individual comparisons to the sums, and conclude via Definition 5.5. The sole difference is citation depth at the distributivity step: Heath cites Proposition 5.1 as a unit to establish that combined equimultiples are equimultiples of the combined magnitudes, while the AI re-derives this same fact from first principles using Definition 5.2 and Common Notion 2. The ai_only items (CN2, CN5, D5.2, D5.4, D5.6) are all definitions and common notions that serve as the foundational components of what Heath accomplishes with the single citation of 5.1. The underlying geometric fact is present in both proofs at the same logical position, making this a same-backbone, different-depth case.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate found no issues since both citations (D5.5, D5.7) are definitions. Q1 confirmed the AI proof is logically complete: it obtains witnessing equimultiples via D5.7, transfers the comparison via D5.5, and concludes via D5.7 again, with every step properly justified. Q2 confirmed identical key intermediate conclusions in both proofs. The perfect-match check then determined the classification: ai_used equals heath_refs exactly ({D5.5, D5.7}), yielding Jaccard 1.0 and category P.

### 5.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. For the explicitly proved case (A > C), both Heath and the AI share the identical logical backbone: establish a ratio inequality via 5.8, transfer it via 5.13, then compare magnitudes via 5.10. Heath then abbreviates the remaining two cases (A = C, A < C) with 'similarly we can prove,' while the AI proves all three cases explicitly, introducing citations 5.7, 5.9, and 5.11 for the A = C case. Since heath_only is empty and the AI's extra citations serve only to spell out what Heath leaves to the reader, this is a same-backbone, different-depth scenario constituting a granularity difference (G).

### 5.15
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decompose the multiples into equal parts, show each corresponding pair has the same ratio via 5.7, aggregate via 5.12, and conclude the parts have the same ratio as the multiples. The AI proof cites definitions D5.1 and D5.2 explicitly where Heath leaves them implicit, and uses 5.11 (transitivity of equal ratios) explicitly where Heath handles the substitution AG=C, DK=F without naming a proposition. Since heath_only is empty and all ai_only items (5.11, D5.1, D5.2) represent over-citation of definitions and auxiliary results rather than a different argumentative path, this is a same-backbone, different-depth scenario -- granularity difference.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: take equimultiples of A,B and C,D, apply V.15 to show equimultiple ratios equal original ratios, chain equalities via V.11, apply V.14 trichotomy, and conclude by V.Def.5. The AI proof cites the identical theorem set (5.11, 5.14, 5.15) and the same definitional anchor (D5.5) as Heath. The ai_only set consists entirely of definitions (D5.2, D5.3, D5.6, D5.12) that the AI cites explicitly where Heath uses them implicitly, and heath_only is empty. This is a straightforward over-citation of definitional foundations with no change to the logical backbone, placing the proof squarely in Case A of Q2 as a granularity difference.

### 5.17
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct equimultiples of the component magnitudes, establish distributive properties of multiples over addition, apply the given proportion through the equimultiple criterion (Definition 5.5), subtract common parts to transfer the excess/equal/less comparison, and conclude by the definition of proportion. The sole difference is citation depth: Heath cites propositions 5.1 and 5.2 for the distributive properties of equimultiples (that m times A plus m times B equals m times (A+B), and that m-fold plus n-fold of the same magnitude equals (m+n)-fold), while the AI re-derives these same facts directly from Common Notion 2 (equals added to equals) and Definition 5.2 (equimultiple definition). All ai_only items are definitions and common notions (lower-level axioms), and all heath_only items are propositions whose substance the AI re-derives from those axioms. This is a same-backbone, different-depth scenario yielding G.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3. Heath proves 5.18 by reductio ad absurdum, assuming the contrary and deriving a contradiction through V.17 (separando), V.11 (transitivity of proportions), and V.14 (comparison of terms in a proportion). The AI instead proves the result directly from the equimultiple definition of proportion (D5.5), decomposing the magnitudes into their separando parts, forming arbitrary multiples, and showing through case analysis (n <= m and n > m) that the required comparison holds for all multiples. The two proofs share no key intermediate conclusions and have zero citation overlap (Jaccard = 0.0). The AI's direct proof from definitions is logically complete, establishing each step from common notions and definitions without invoking any prior theorems. This constitutes a genuine path difference.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate passed (all citations 5.11, 5.16, 5.17 are prior to 5.19). Q1 found no logical defect: the AI proof proceeds by alternation (5.16), separation (5.17), alternation again (5.16), and transitivity (5.11), with every step properly cited. Q2 confirmed that both proofs share the same logical backbone: both start from the hypothesis that whole:whole = part:part, apply alternation, then separation, then alternation again, and conclude by transitivity of equal ratios. The citation sets are identical (ai_used = heath_refs = {5.11, 5.16, 5.17}), yielding Jaccard 1.0 and a Perfect match classification.

### 5.20
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: for the primary case A > C, both establish A:B > C:B via 5.8, transfer the ratio inequality through the given proportions to obtain D:E > F:E, and conclude D > F via 5.10. The sole heath_only citation, 5.13, packages the transfer of ratio inequalities through proportion equalities; Heath's own proof of 5.13 uses V.Def.5 and V.Def.7, which are exactly the definitions (D5.5, D5.7) the AI cites directly to perform the same transfer step. The AI thus re-derives 5.13's internals from definitions rather than citing the packaged result, a citation-depth difference. The additional ai_only propositions (5.7, 5.9, 5.11) serve the A = C case that Heath dismisses with 'similarly we can prove,' representing explicit citation of a case Heath treats implicitly. Since the key intermediate conclusions are identical and all differences reduce to citation depth, Case A of Q2 holds, yielding G.

### 5.21
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: The classification is decided at Q2 (Case B). Heath's proof of the A > C case uses V.8 to establish A:B > C:B, then applies V.13 to transfer this inequality to E:F > E:D, and concludes D > F via V.10. The AI instead inverts A:B = E:F to obtain B:A = F:E (via Definition V.5), then uses V.8 in its alternate form to get B:C > B:A, and works through Definition V.7 (the definition of greater ratio) to transfer the inequality to D:E > F:E, concluding D > F via V.10. The intermediate ratio comparisons differ structurally: Heath compares ratios with common antecedent E (E:F > E:D), while the AI compares ratios with common consequent E (D:E > F:E). The transfer mechanism is fundamentally different: Heath uses the composed result V.13 (ratio inequality transitivity), while the AI works at the definitional level using D5.5 and D5.7. Additionally, the AI explicitly treats all three cases with distinct propositions (using 5.7, 5.9, 5.11 for the equality case), whereas Heath proves only the A > C case and asserts the rest follow similarly. Since the AI's path is logically valid (Q3 confirmed), the classification is D.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided this classification. Both proofs argue through the same key intermediate conclusions: applying V.4 to transform the given proportions into equimultiple form, applying V.20 for the ex aequali comparison of equimultiples, and concluding via V.Def.5. The AI's three-term proof (Steps 2-4) follows Heath's backbone exactly. The AI adds an explicit inductive extension to n terms (Step 5) and cites D5.17 (the definition of ex aequali ratio), which Heath uses implicitly without citing. Since ai_only contains only a definition (D5.17) and heath_only is empty, the proofs share the same backbone with the AI providing slightly more explicit citation depth, satisfying Case A of Q2.

### 5.23
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) establish the first perturbed proportion among equimultiples via 5.15 and 5.11, (2) establish the second perturbed proportion among equimultiples, (3) apply 5.21 to the perturbed triples, and (4) conclude by the definition of proportion. The sole substantive divergence is in step (2): the AI uses 5.4 in a single step to derive mB:nC = mD:nE directly from B:C = D:E, while Heath uses a six-step chain involving 5.16 (alternation twice), 5.15 (equimultiple transfer), and 5.11 (transitivity) to reach the equivalent H:L = K:M. Although the containment test shows 5.16 is not inside the proof of 5.4, the underlying geometric fact at this logical position -- the second perturbed proportion among the equimultiples needed for 5.21 -- is identical in both proofs. The ai_only definitions (D5.2, D5.5, D5.17, D5.18) are standard explicit definitional citations that do not alter the logical backbone. This is a citation-depth difference, not a path difference.

### 5.24
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: invert one of the given ratios, apply ex aequali (5.22) to relate the first and fifth magnitudes, apply componendo/composition (5.18) to obtain the sum-ratio, then apply ex aequali (5.22) again to reach the conclusion. The key intermediate conclusions match exactly across both proofs despite different notation conventions. The sole difference is that the AI explicitly cites Definition 5.5 for the inversion step, whereas Heath simply states 'inversely' without formal citation. Since ai_only contains only the definition D5.5 and heath_only is empty, this is a Case A granularity difference: same backbone, different citation depth.

### 5.25
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they apply 5.19 (separando) to obtain a remainder ratio equal to the whole ratio, derive the inequality of remainders from the inequality of wholes, then combine these results to show greatest plus least exceeds the remaining two. The AI over-cites by explicitly invoking 5.14 (to establish that B > D from the proportion and A > C), definitions D5.5 and D5.6, and common notions CN2 and CN5, all of which Heath leaves implicit. The empty heath_only set confirms that the AI covers every step Heath uses. Since the key intermediate conclusions are identical and only citation depth differs, this is a granularity difference.


---

## Book 6 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 21 | 6.1, 6.2, 6.3, 6.5, 6.6, 6.7, 6.8, 6.9, 6.11, 6.12, 6.13, 6.14, 6.16, 6.17, 6.18, 6.19, 6.21, 6.23, 6.27, 6.28, 6.29 |
| Path difference (D) | 12 | 6.4, 6.10, 6.15, 6.20, 6.22, 6.24, 6.25, 6.26, 6.30, 6.31, 6.32, 6.33 |
| AI proof error (E) | 0 |  |

**Total**: 33 propositions

## Per-Proposition Analysis

### 6.1
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing equimultiples of the bases, using I.38 to show triangles on equal bases between the same parallels are equal, establishing the three-way equimultiple comparison, applying V.Def.5 to conclude the triangle ratio equals the base ratio, then showing each parallelogram is double a triangle with the same base and height and using V.15 and V.11 for the parallelogram ratio. The sole heath_only item (1.41) is resolved by the proof-tree containment test: Heath's proof of 1.41 internally uses 1.34, which is the proposition the AI cites directly. The AI goes one level deeper into the proof tree by citing the internal machinery of 1.41 rather than 1.41 as a unit. The remaining ai_only items (1.14, 1.3, 1.31, CN2, CN4, CN5, D5.2, D6.4, P1, P2) are all construction steps, postulates, common notions, and definitions that Heath leaves implicit. This is a citation-depth difference, not a backbone difference, yielding G.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for this biconditional proposition: in the forward direction, both establish that triangles BDE and CDE are equal (same base DE, same parallels), then use VI.1 to express area ratios as segment ratios, V.7 to equate ratios of equal magnitudes, and V.11 to conclude proportionality; in the converse, both reverse the argument using V.11, V.9, and I.39. The sole substantive citation difference is that the AI cites I.37 (triangles on the same base in the same parallels are equal) where Heath cites I.38 (triangles on equal bases in the same parallels are equal). Since triangles BDE and CDE share the exact same base DE, I.37 is actually the more precise reference, and I.38 works only because same base implies equal bases. The remaining ai_only items (D5.6, D6.4, P1) are definitional and axiomatic over-citations that do not alter the proof structure. This is Case A of Q2: same backbone, different citation depth.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions through an identical logical backbone: constructing CE parallel to DA, deriving angle equalities via I.29, obtaining AE = AC (via I.6 forward, I.5 converse), applying VI.2 for proportional segments, and using V.11/V.9 for ratio manipulation in the converse. The heath_only set is empty, meaning the AI cites every reference Heath uses. The ai_only items (1.13, 1.31, 5.7, CN1, CN5, P1, P2, P5) are exclusively construction propositions, postulates, common notions, and one additional ratio step (5.7), all representing over-citation of lower-level details rather than a different proof path. This is Case A of Q2: same backbone, different citation depth.

### 6.4
**Category**: Path difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Heath constructs an external point F by extending sides BA and ED until they meet, forms parallelogram FACD, and uses parallelogram equalities (FA=DC, AC=FD) together with VI.2 applied to triangle FBE, V.16 alternation, and V.22 ex aequali to derive all three proportion pairs. The AI instead works entirely within one triangle: it cuts AP=DE on side AB, draws PQ parallel to BC, proves triangle APQ congruent to triangle DEF via I.26 to obtain AQ=DF, applies VI.2 to the internal parallel cut, and uses V.12 (ratio of sums) to reach AB:AC=DE:DF, then repeats for other vertex pairs by relabeling. The key intermediates are fundamentally different (external parallelogram vs. internal congruent triangle), yielding Case B in Q2. Q3 confirms the AI path is logically complete: every step is properly justified, and the chain runs soundly from premises to conclusion.

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct auxiliary triangle GEF on EF equiangular with ABC using I.23, show the remaining angle equal via I.32, apply VI.4 to obtain proportionality of sides in the equiangular triangles, compare with the hypothesis via V.11 to deduce equal ratios, apply V.9 to conclude DE=GE and DF=FG, establish all angle equalities between DEF and GEF, and transfer these equalities to conclude ABC is equiangular with DEF. The citation differences are purely at the granularity level: the AI over-cites by making explicit foundational justifications (I.17 and P5 for why the construction arms meet, CN1-CN3 for the subtraction argument on angle sums, D5.6 for the definition of proportion), while Heath leaves these implicit. The single heath_only item, I.4, reflects a different but equivalent mechanism for the same intermediate conclusion: Heath uses I.8 once then I.4 (SAS) for full congruence, whereas the AI applies I.8 at each corresponding vertex to obtain all three angle equalities directly. Both reach the same conclusion at the same logical position, making this a citation-depth difference rather than a path difference.

### 6.6
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct an auxiliary triangle equiangular with ABC, apply VI.4 to obtain proportionality of sides, use V.11 and V.9 to establish a segment equality, and conclude that the original triangles are equiangular. The only structural difference is in the closing mechanism: Heath uses I.4 (SAS congruence) to show triangle DEF is congruent to the auxiliary triangle DGF, while the AI shows that the auxiliary point G coincides with F since both lie on the same ray from D at equal distance, making SAS unnecessary. The ai_only set consists entirely of over-citations (common notions CN1-CN5, postulates P2 and P5, and proposition 1.17 used to justify the construction), which are explicit justifications of steps Heath leaves implicit. The single heath_only item (I.4) is replaced by the AI's point-coincidence argument, which achieves the same logical transition through a simpler mechanism rather than a fundamentally different path. Since the key intermediate conclusions are the same and the citation differences reflect depth of justification rather than path divergence, this is a granularity difference.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct angle ABG equal to angle DEF, establish triangle ABG equiangular with triangle DEF via I.32, derive AB:BG = DE:EF via VI.4, conclude BC = BG via V.11 and V.9, then use the isosceles triangle property (I.5) and supplementary angles (I.13) to reach a contradiction. The AI handles both cases (remaining angles both less than, or both not less than, a right angle) in a single unified argument rather than separately as Heath does, but the key intermediate conclusions are identical. The ai_only set consists entirely of Common Notions (CN2, CN3, CN4, CN5) and Postulates (P4, P5) that Heath invokes implicitly, while heath_only is empty. This is a citation-depth difference with no divergence in the geometric reasoning, placing this squarely in Case A of Q2.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: establishing angle equalities via I.32 (angle sums in triangles) to show each sub-triangle is equiangular with the whole, applying VI.4 for proportionality of sides, and invoking VI.Def.1 to conclude similarity, then repeating this chain to show the two sub-triangles are similar to each other. The AI proof covers all three required parts (DBA similar to ABC, DAC similar to ABC, DBA similar to DAC) with the same key intermediate conclusions as Heath. The only difference is citation depth: the AI explicitly cites foundational items (CN1, CN3, CN4 for equality manipulations; D1.10 for the definition of right angle; P4 for all right angles being equal) that Heath invokes implicitly. With heath_only empty and ai_only consisting entirely of common notions, a definition, and a postulate, this is a clear Case A granularity difference.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Both proofs share the same logical backbone: construct equal segments on an auxiliary line from A, draw a parallel to the join with B to establish proportionality via 6.2, and use the known ratio on the auxiliary line to conclude the corresponding ratio on AB. Heath proves the specific third-part case using I.3 for equal segments and direct informal reasoning for the ratio transfer (CD is double DA, so BF is double FA, so BA is triple AF). The AI generalizes to the nth part, uses postulates and definitions (P1, P2, P3, D1.15) for the equal-segment construction instead of I.3, and makes the ratio composition step explicit via 5.18. Q2 Case A applies: the ai_only items are either definitions, axioms, and postulates (over-citation) or 5.18, which formalizes a step Heath performs informally; the single heath_only item (1.3) is replaced by lower-level construction steps. Same key intermediate conclusions at different citation depth yields G.

### 6.10
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof constructs parallelograms FH and HB, uses I.34 to establish equal sides (DH=FG, HK=GB), then applies VI.2 twice in triangles DKC and AGE to derive the segment proportions directly. The AI proof takes a fundamentally different approach: it constructs auxiliary points on a separate line AX with segments equal to the given cut line's segments (via I.3), draws parallels in a single triangle APnB, and then uses extensive Book 5 proportion theory (5.18, 5.16, 5.19, 5.11, 5.7) to manipulate the resulting ratios into the required cross-proportionality. The key intermediates differ: Heath relies on parallelogram equalities (I.34) that the AI never establishes, while the AI relies on terminal-segment ratio equalities and Book 5 algebraic manipulation that Heath never uses. This constitutes a genuine backbone difference (Q2 Case B). The AI's path is logically complete under Q3, with each step properly cited and the chain running soundly from construction to conclusion.

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a triangle with one side length equal to the second given line, draw a parallel to create proportional segments, apply VI.2 to obtain a proportion, then substitute the equal lengths to derive the continuous proportion. The AI proof uses the identical strategy as Heath (parallel line in a triangle plus 6.2) but over-cites construction foundations (1.2, P1, P2), the argument that the parallel meets the second ray (1.17, 1.29, P5), and explicit definitions (D1.23, D5.5, D5.6), all of which Heath leaves implicit. Since heath_only is empty and all ai_only items are expansions of steps present in both proofs, this is Case A: same backbone, different citation depth.

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct two rays at an angle, mark segments equal to the three given lines on those rays, draw a parallel line (I.31), and apply VI.2 to obtain the required proportionality. The AI proof adds extensive lower-level detail that Heath leaves implicit: postulates P1 and P2 for producing rays, P5 for establishing that the parallel meets the second ray, I.3 for cutting off equal segments, I.17 and I.29 for proving the lines must intersect, D1.23 for the definition of parallel lines, and D5.6 for the definition of proportion. Since heath_only is empty and all ai_only items are postulates, definitions, or construction-level propositions, this is a clear case of the same backbone argued at different depths of citation, yielding Granularity difference (G).

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: place the two given lines in a straight line, describe a semicircle on the combined segment, draw a perpendicular from the junction point to meet the semicircle, then apply III.31 (angle in a semicircle is right) and VI.8 (altitude from the right angle to the hypotenuse is a mean proportional between the segments of the base). The AI proof cites the same two substantive propositions as Heath (3.31 and 6.8) but additionally cites twelve construction-level items: propositions for placing the lines and constructing the perpendicular (1.3, 1.10, 1.11), postulates (P1, P2, P3), and definitions (D1.10, D1.15, D1.17, D5.5, D5.6, D6.1). Heath leaves all of these implicit. Since heath_only is empty and all ai_only items are construction propositions, postulates, or definitions, this is a clear case of over-citation at the same backbone, yielding G.

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they each construct an auxiliary parallelogram, use VI.1 (6.1) to express the ratio of each given parallelogram to the auxiliary in terms of the relevant sides, then combine the ratios via V.7 (5.7) and V.11 (5.11) for the forward direction and via V.11 (5.11) and V.9 (5.9) for the converse. The differences lie only in the geometric setup (Heath uses I.14 for collinearity, the AI uses a vertex-coincident placement justified by 1.30) and in the AI's explicit citation of definitions, axioms, and postulates (CN4, D1.23, D6.2, P2) that Heath leaves implicit. Since the logical backbone is identical and the citation differences reflect construction details and over-citation rather than a different proof path, this is a granularity difference.

### 6.15
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Heath positions both triangles at a shared vertex with sides collinear (using I.14) and creates triangle BAD as the common comparison triangle, then applies V.7 to the equal areas and VI.1 to convert area ratios to side ratios. The AI instead constructs a congruent copy AGH of triangle DEF inside triangle ABC using I.3 and I.4 (SAS), then uses the intermediate triangle AGC as the comparison triangle with VI.1 applied to two pairs of common-height triangles. The congruence step (I.4) is a key intermediate conclusion in the AI proof with no counterpart in Heath, and the collinearity step (I.14) is a key intermediate in Heath with no counterpart in the AI. These different auxiliary constructions produce genuinely different intermediate geometric conclusions, constituting a different logical backbone (Case B). Q3 confirmed the AI path is valid: the construction is sound, VI.1 is correctly applied, and the Book V proportionality chain (V.7, V.11, V.9) correctly completes both directions of the biconditional.

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: define the two rectangles as equiangular parallelograms, establish that reciprocal proportionality of their sides about the equal angles is equivalent to the given proportion of the four lines, and then apply 6.14 in both directions to connect equality of the parallelograms with that reciprocal proportionality. Heath constructs explicit auxiliary parallelograms (BG, DH with AG=F, CH=E) while the AI works directly with the rectangles, but the key intermediate conclusions are identical. The ai_only set consists entirely of definitions (D2.1, D5.6, D6.2) and a postulate (P4), which are explicit citations of concepts Heath uses implicitly, and heath_only is empty. This is a clear case of same backbone with different citation depth, yielding G.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs establish the same biconditional through the same key intermediate conclusions: identifying that three proportional lines yield four proportional entries, applying 6.16 to equate the rectangle of the extremes with the rectangle of the means, and recognizing that the rectangle of the means equals the square on the mean. Heath constructs an auxiliary line D equal to B to make four explicit lines, while the AI directly uses b,b as the two middle entries; this is a presentational difference, not a backbone difference. The ai_only set consists entirely of definitions (D1.22, D2.1, D5.6) that the AI cites explicitly but Heath leaves implicit, and heath_only is empty. This is Case A: same backbone, different citation depth, yielding G.

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: triangulate the given polygon, copy angles at the endpoints of each corresponding side using I.23, deduce remaining angles equal by I.32, establish proportionality of corresponding triangle sides by VI.4, chain the proportions to show all sides about equal angles are proportional, sum triangular angles to show whole angles are equal, and conclude similarity by VI. Def. 1. The AI generalizes Heath's specific pentagon to an arbitrary n-gon but follows the identical argumentative structure. Every ai_only citation is an over-citation making explicit what Heath leaves implicit: 1.17 and P5 justify that constructed lines meet, 5.22 names the ex aequali principle Heath applies verbally when chaining proportions, CN2 and CN3 name common notions for adding and subtracting angles, and P1 cites the postulate for drawing diagonals. With heath_only empty and all extra citations being depth-level elaborations of steps present in both proofs, this is Case A of Q2: same backbone, different citation depth.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: they establish AB:DE = BC:EF by alternation (5.16), construct a third proportional BG so that BC:EF = EF:BG (6.11), derive AB:DE = EF:BG by transitivity (5.11), conclude triangle ABG equals triangle DEF by reciprocal proportionality (6.15), relate triangle ABC to triangle ABG via their bases (6.1), and finally obtain the duplicate ratio result via D5.9. The citation differences are purely depth-related: the AI explicitly cites postulates (P1, P2, P3), common notions (CN1, CN4), the ratio substitution proposition (5.7), and specific definitions (D6.1, D6.4) for steps Heath leaves implicit or covers with the broader definition D5.11. Since the key intermediate conclusions are identical and only the citation granularity differs, this is a granularity difference.

### 6.20
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same approach for establishing that corresponding triangles are similar (using 6.6, 6.4, and 5.22 for ex aequali), but they diverge in how they prove the ratio relationship between corresponding triangles. Heath constructs auxiliary diagonals AC and FH, creates medial points M and N, uses 1.32 to prove auxiliary triangles ABM and FGN equiangular, and then uses 6.1 (triangles as their bases) to relate segment ratios AM:MC to triangle area ratios. The AI takes a genuinely different path: it directly applies 6.19 to each pair of similar triangles, observing that adjacent pairs share a diagonal as corresponding sides, so all pairs yield the same duplicate ratio, which it chains using 5.11. The containment test does not resolve this because Heath uses 1.32 for an auxiliary construction that has no counterpart in the AI proof. Under Q3, the AI's alternative route is logically valid and complete, yielding classification D.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the identical logical backbone: unpack the definition of similarity (D6.1) for each figure relative to the common figure, then conclude similarity of the two figures by transitivity of angle equality and proportionality of sides. Heath performs the transitivity step implicitly in a single sentence, while the AI makes it explicit by citing CN1 (things equal to the same thing are equal, for angle transitivity) and 5.11 (ratios equal to the same ratio are equal, for proportionality transitivity). The ai_only set {5.11, CN1} consists entirely of underlying justifications for the same logical step Heath leaves implicit, and heath_only is empty, confirming this is a citation-depth difference with no backbone divergence.

### 6.22
**Category**: Path difference
**Jaccard**: 0.357
**Analysis**: The forward direction of both proofs shares the same backbone (construct third proportionals, express figure ratios as duplicate ratios, apply ex aequali), differing only in citation depth (AI uses 6.20 for general polygons while Heath uses 6.19 for triangles, and 6.19 appears inside 6.20's proof). However, the converse directions follow genuinely different paths: Heath uses a reductio ad absurdum approach, constructing a similar figure via 6.18 on a fourth proportional line, applying the forward direction to derive a contradiction; the AI instead gives a direct proof using a fourth proportional and third proportional construction, then applies perturbed ex aequali (5.23) to show that d:e = e:d, forcing d = e. The AI's use of 5.23 represents a substantively different logical tool not present in Heath's argument, and the key intermediate conclusions of the converse differ entirely, making this a path difference (D) under Q2 Case B. The AI's different path was verified as logically sound under Q3.

### 6.23
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct an intermediate parallelogram sharing one pair of sides with each original, apply VI.1 twice to express area ratios in terms of side ratios, and then compose these ratios via ex aequali to obtain the compound ratio. Heath mediates through auxiliary straight lines K, L, M while the AI uses the intermediate parallelogram's area directly as the middle term, but the sequence of key geometric conclusions is identical. The AI's additional citations (1.31 for parallel construction, 5.22 for ex aequali, CN4 for congruence preservation, D6.5 for the definition of compound ratio) are all over-citations of construction steps, definitions, and common notions that Heath leaves implicit. Since heath_only is empty and both proofs establish the same key intermediate facts in the same logical order, this is a granularity difference.

### 6.24
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath establishes proportionality via 6.2 (parallel lines cut sides proportionally) applied directly to triangles ABC and ACD, then manipulates the resulting ratios with componendo (5.18) and alternando (5.16) to obtain full-side proportions, and uses ex aequali (5.22) for composite ratios. The AI instead establishes equiangularity of sub-triangles AEO/ABC and OFC/ABC via parallel lines, then applies 6.4 (equiangular triangles have proportional sides) to obtain proportions directly, extending them to all parallelogram sides via opposite-sides equality (1.34). The proof-tree containment test for 6.4 captures three of four heath_only items (6.2, 5.16, 5.22 appear inside 6.4's proof) but not 5.18 (componendo), which Heath uses in the main proof as part of a ratio-algebraic strategy absent from the AI's approach. The proofs work with different triangle pairs and employ fundamentally different strategies — ratio algebra from segment proportions (Heath) versus direct application of triangle similarity (AI) — constituting a genuine path difference. The AI's path is logically valid throughout.

### 6.25
**Category**: Path difference
**Jaccard**: 0.067
**Analysis**: Q2 decided the classification. Heath's proof constructs parallelograms equal to the given figures (I.44, I.45), takes a mean proportional (VI.13), and uses the duplicate ratio property of similar triangles (VI.19) together with proportional areas on equal bases (VI.1) and alternando (V.16) to transfer the area equality. The AI proof takes an entirely different route: it constructs squares equal to the given figures (2.14), finds a fourth proportional line (6.12), builds the similar figure on that line (6.18), and then applies VI.22 (similar figures on four proportional lines are proportional) to transfer the ratio, concluding via V.9 that the constructed figure equals the target. The only shared citation is 6.18. The key intermediates differ fundamentally — parallelogram application and mean proportionals versus square construction and direct ratio-transfer — confirmed by the proof-tree containment test showing that Heath's citations 1.44, 1.45, 5.16, 6.1, 6.13 do not appear inside the proof of VI.22. The AI's chain is logically complete and sound, so Q3 yields D.

### 6.26
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 6.26 by contradiction: assuming the diagonal does not pass through F, he constructs an auxiliary parallelogram on the assumed diagonal, uses 6.24 to establish a ratio equality, then applies 5.11 (transitivity of ratios) and 5.9 (equal ratios imply equal magnitudes) to derive AE = AK, a contradiction. The AI takes an entirely different direct approach: it extracts the similarity conditions (AE:EF = AB:BC and angle AEF = angle ABC) from D6.1, applies 6.6 (SAS similarity for triangles) to triangles AEF and ABC to show them equiangular, deduces angle BAF = angle BAC, and concludes that A, F, C are collinear by CN5. The Jaccard similarity is 0.0 with completely disjoint citation sets, reflecting genuinely different proof strategies rather than mere citation-depth differences. The AI proof is logically sound at every step, so Q3 confirms D.

### 6.27
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: establishing that similar parallelograms share a diameter (VI.26), using equality of complements (I.43) and parallelograms on equal bases between parallels (I.36) to perform an area dissection showing the parallelogram applied to the half exceeds any other admissible application. The AI proof explicitly cites construction steps (I.10, I.29, I.30, I.31, I.34), common notions (CN1, CN2, CN4, CN5), a definition (D6.1), a postulate (P2), and a ratio result (5.14) that Heath leaves implicit. With heath_only empty and ai_only consisting entirely of construction, axiom, and auxiliary citations, Q2 Case A applies: same backbone, different citation depth.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.217
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: bisect AB, construct a similar parallelogram on the half-line (6.18), handle the equality case, construct an excess parallelogram similar to the defect (6.25), establish similarity (6.21) and the same-diameter property (6.26), use complement equality and equal-base parallelograms (I.36) to conclude the required area. The heath_only set is empty, meaning every citation Heath makes also appears in the AI proof. The 18 ai_only items consist entirely of explicit construction citations (1.10, 1.3, 1.30, 1.31), postulates (P1, P2), common notions (CN2-CN5), definitions (D1.19, D6.1), sub-argument propositions (1.4, 1.34, 5.14, 1.43) that Heath uses implicitly, and additional Book 6 propositions (6.24 for similarity of opposite parallelogram about the diameter, 6.27 for the upper bound condition) that Heath handles without explicit citation. This is a clear case of the AI providing finer-grained justification for the same proof steps, yielding a granularity difference.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.261
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect the given line, construct a parallelogram similar to the given one on the half, use VI.25 to build a larger similar parallelogram equal to the first plus the given figure, show the two similar parallelograms are about the same diagonal (VI.26), invoke equal complements (I.43) and equal parallelograms on equal bases (I.36) to derive that the applied parallelogram equals the given figure, and finally show the excess is similar to the given parallelogram (VI.24). The heath_only set is empty, confirming the AI covers every citation Heath makes. The ai_only set consists entirely of construction propositions (1.10, 1.3, 1.29, 1.30, 1.31, 1.34, 1.4, 1.45, 6.18), common notions (CN1, CN2, CN3, CN5), postulates (P1, P2), a definition (D6.1), and one ratio result (5.14) that Heath leaves implicit. This is a clear case of the AI being more explicit about foundational steps while following the identical logical path.

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof works through area application (6.29) to construct a parallelogram equal to the square on AB, then uses reciprocal proportionality of equiangular parallelograms (6.14) to derive the extreme-and-mean-ratio proportion. The AI takes a fundamentally different route: it invokes 2.11 to cut AB at C so that rect(AB,CB) = sq(AC), then applies the converse of 6.17 to convert that rectangle-square equality directly into the proportion AB:AC = AC:CB, and finishes with 5.14 to establish AC > CB. The two proofs share zero citations (Jaccard = 0.0) and their key intermediates differ — Heath's pivots on area equality of parallelograms and reciprocal proportionality, while the AI's pivots on the algebraic cutting lemma and the rectangle-proportion equivalence. Neither path subsumes the other. The AI's chain is logically complete and valid, so Q3 confirms D.

### 6.31
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Heath's proof draws an altitude from the right angle to the hypotenuse, invokes 6.8 to establish that the sub-triangles are similar to the whole triangle, then applies 6.19 (duplicate ratio of similar triangles) to derive the figure proportions, and concludes by summing the segments. The AI takes a fundamentally different path: it constructs squares on all three sides (1.46), uses 6.20 (duplicate ratio of similar polygons) to show that the ratios of the arbitrary similar figures equal the corresponding ratios of the squares, links these via 5.11, adds the proportions with 5.24, and then applies the Pythagorean theorem (1.47) to conclude that the sum of the figures on the legs equals the figure on the hypotenuse. The only shared citation is D6.1, yielding a Jaccard of 0.091. The proof-tree containment test confirms Case B: while 6.19 does appear inside the proof of 6.20, the other heath_only item 6.8 does not, reflecting Heath's reliance on an altitude-based similar-triangle strategy that is entirely absent from the AI proof. The AI's chain is logically complete and valid under the hardened Q1(b) standard, so Q3 yields D.

### 6.32
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the initial key conclusions: establishing equal angles BAC = CDE via two applications of I.29, and deriving equiangular triangles via VI.6 to obtain ABC = DCE. However, the proofs diverge in how they reach the final collinearity conclusion. Heath uses I.32 (angle sum in a triangle) and angle addition to show that ACE + ACB equals two right angles, then applies I.14 with reference line AC. The AI instead applies I.29 a second time to derive co-interior angles (ABC + BCD = two right angles from parallels AB and DC with transversal BC), substitutes using the established equality ABC = DCE to get DCE + BCD = two right angles, and applies I.14 with reference line CD. This constitutes a genuinely different logical backbone: the AI avoids I.32 entirely by exploiting the co-interior angle property of parallel lines, which is an independent geometric argument that does not contain or subsume I.32. The AI proof is logically complete and valid, warranting classification as D.

### 6.33
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Heath uses 3.27 (equal arcs produce equal angles) to build equimultiples by laying off consecutive equal arcs and deriving equimultiple central angles, then applies V. Def. 5. The AI instead uses the converse proposition 3.26 (equal angles produce equal arcs) and constructs equimultiples through a fundamentally different mechanism: bisecting the original angles into k equal parts (1.9), obtaining equal arcs from those equal small angles (3.26), and then building equimultiples of the small pieces to satisfy the equimultiple criterion (D5.5). The containment test confirms that 3.27 does not appear inside Heath's proof of 3.26, which uses I.4, III.Def.11, and III.24 instead, establishing that these are independent routes rather than a citation-depth difference. Under Q3, the AI's chain from angle subdivision through the angle-arc order correspondence to the equimultiple criterion is logically complete, yielding D.


---

## Book 7 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 29 | 7.1, 7.2, 7.3, 7.5, 7.9, 7.11, 7.12, 7.13, 7.14, 7.16, 7.17, 7.18, 7.19, 7.20, 7.21, 7.22, 7.23, 7.24, 7.25, 7.26, 7.28, 7.29, 7.32, 7.34, 7.35, 7.36, 7.37, 7.38, 7.39 |
| Path difference (D) | 10 | 7.4, 7.6, 7.7, 7.8, 7.10, 7.15, 7.27, 7.30, 7.31, 7.33 |
| AI proof error (E) | 0 |  |

**Total**: 39 propositions

## Per-Proposition Analysis

### 7.1
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs use identical proof-by-contradiction structure: assume a number d measures both given numbers, trace d through each successive remainder of the Euclidean algorithm to show d must measure the final unit, then derive a contradiction since a number cannot measure a unit. The key intermediate conclusions (common measure propagates through subtraction, common measure must divide the unit, contradiction) are the same in both proofs. The AI's additional citations (CN2, CN3, CN5, D7.1, D7.2, D7.5) are all common notions and definitions that Heath invokes implicitly but does not cite, while heath_only is empty. This is a citation-depth difference with identical logical backbone, yielding G.

### 7.2
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they handle the trivial case (divisor measures the other number), apply successive subtraction with termination guaranteed by 7.1 (the process cannot reduce to a unit without contradicting the hypothesis that the numbers are not prime to one another), trace divisibility backward through the chain of remainders to show the terminal remainder divides both original numbers, and then prove maximality. The AI proof is more explicit in citing foundational items (definitions D7.2, D7.3, D7.12 and common notions CN2, CN3, CN5) that Heath invokes implicitly, while heath_only is empty. Since the key intermediate conclusions are identical and the only difference is citation depth, this is a granularity difference.

### 7.3
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: find GCM of the first two numbers (A,B), then find GCM of that result and the third number (C), and show the final result is GCM(A,B,C). Heath cites 7.2 as a unit for the first step and handles two explicit cases (D measures C vs. D does not measure C). The AI re-derives the Euclidean algorithm (antanairesis) inline for the pair A,B in Steps 2-4 rather than citing 7.2, adding definitions (D7.2, D7.5, D7.12) and common notions (CN2, CN3, CN5) that Heath leaves implicit, then applies 7.2 to D and C and collapses the two cases into a single application. Since the ai_only citations are entirely definitions and common notions used in the inline expansion, and heath_only is empty, this is a citation-depth difference with the same logical backbone, yielding G.

### 7.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof constructs the parts explicitly: for the prime case, it decomposes into units; for the non-prime, non-measuring case, it invokes 7.2 to find the GCD and then shows each segment of the decomposition is a part of the greater number. The AI takes a fundamentally different route, arguing purely from definitions: D7.3 defines 'part' as the case when the lesser measures the greater, and D7.4 defines 'parts' as the case when it does not, so the dichotomy (measures or not) yields the conclusion directly. The backbones are entirely different -- Heath's is constructive (GCD-based decomposition) while the AI's is definitional (direct application of D7.3 and D7.4). Under the hardened standard, the AI's definitional argument is terse but supported: each step cites a definition that licenses the claim, so Q1 does not trigger E. Since the backbones differ (Q2 Case B) and the AI's path is logically complete under Q3, the classification is D.

### 7.5
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: partition the two larger numbers into equal parts corresponding to the smaller numbers, note the equal multitude of parts, pair corresponding parts to show each pair sums to the same value, and conclude that the sum of the smaller numbers is the same part of the sum of the larger numbers. The AI proof explicitly cites Common Notions (CN2, CN4, CN5) and Definitions (D7.2, D7.3) that Heath uses implicitly without citation, producing a Jaccard of 0.0 despite identical logical structure. Since all ai_only items are foundational axioms and definitions rather than substantive propositions, and heath_only is empty, this is a citation-depth difference under Case A of Q2, yielding G.

### 7.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof applies Proposition 7.5 (the single-part version) iteratively to each pair of corresponding individual parts: it divides AB into parts AG, GB and DE into parts DH, HE, then uses 7.5 to conclude that each paired sum (AG+DH, GB+HE) is the same part of C+F. The AI takes a fundamentally different approach, working entirely from definitions (D7.1-D7.4) and common notions (CN2, CN4, CN5) without citing any theorem. It represents numbers as counts of unit groups (A=r*u, B=s*u, C=r*v, D=s*v), defines w=u+v, and directly shows A+C=r*w and B+D=s*w through regrouping. The citation sets are completely disjoint (Jaccard=0.0), and the proof-tree containment test does not apply because the AI cites no higher-level proposition that could subsume 7.5; instead it derives the result from a more foundational level. The AI also includes an additional step proving A+C is 'parts' (not 'part') of B+D, which Heath omits. These constitute different logical backbones (Q2 Case B), and Q3 confirms the AI's path is logically valid and complete, yielding classification D.

### 7.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Heath's proof constructs an auxiliary number CG, applies Proposition 7.5 (the sum-of-parts theorem) to establish that AB is the same part of GF as AE is of CF, then derives GF = CD and GC = FD by subtraction before substituting back to reach the conclusion. The AI proof takes a genuinely different route: it works directly from Definition 7.3, expressing the part relationship as a multiplicity count k (B = kA, D = kC), algebraically decomposes each copy of A into C + R, sums over k copies to get B = D + kR, and subtracts D to obtain S = kR, yielding the conclusion without any auxiliary construction or appeal to 7.5. The key intermediate conclusions differ: Heath's backbone pivots on GF = CD (via 7.5), while the AI's backbone pivots on B = D + kR (via direct algebraic decomposition from the definition). No containment test applies since the AI cites no higher-level proposition covering 7.5. The AI's chain is logically complete under the hardened Q1(b) standard, so the classification is D rather than E.

### 7.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof reduces 7.8 (the 'parts' case) to 7.7 (the single 'part' case) by splitting the composite parts into individual part-components, applying 7.7 to each pair, and summing the remainders. The AI instead works directly from definitions and common notions: it decomposes the numbers into multiples of measuring units (A=r*u, B=s*u, C=r*v, D=s*v), subtracts corresponding pieces to obtain E=r*w and F=s*w where w=u-v, and concludes that E bears the same parts-relation to F as A does to B. The AI explicitly states it takes 'the direct common-notion route, without introducing proportionality theorems,' bypassing 7.7 entirely. The two proofs have genuinely different backbones: Heath's iterative reduction to 7.7 versus the AI's direct algebraic manipulation from definitions. The AI's path is logically valid, with each step soundly justified, so Q3 yields D.

### 7.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decomposing the given numbers into equal copies and then using propositions 7.5 and 7.6 to show that the aggregated sums preserve the part/parts relationship under alternation. Heath divides BC and EF into equal segments and directly applies 7.5/7.6 to the sums, while the AI frames the decomposition using definitions D7.2 and D7.3, cites 7.4 to justify the exhaustive case split into part vs. parts, and then applies 7.5 and 7.6 case by case. The ai_only items (D7.2, D7.3, 7.4) are all definitional or foundational citations that Heath uses implicitly, and heath_only is empty, confirming that the AI over-cites at a finer granularity without introducing a different proof path. This is Case A of Q2: same key intermediate conclusions, different citation depth.

### 7.10
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Heath's proof divides the given numbers into individual parts, applies 7.9 to each part-pair to get alternation, then combines the results using 7.5 and 7.6 (addition of same parts). The AI takes a fundamentally different approach: it represents the numbers algebraically as r and s copies of unit pieces u and v, doubles everything to ensure all terms are genuine numbers, applies 7.9 four times on the doubled quantities and again to undo the doubling, and chains the results by transitivity (CN1). The AI never divides into parts and never uses 7.5 or 7.6. These are genuinely different backbones (Case B). Under Q3, the AI's doubling strategy and multiple applications of 7.9 form a logically valid chain from premises to conclusion, so the classification is D.

### 7.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: unpack the ratio hypothesis via D7.20 into a part-or-parts relationship, apply 7.7 and 7.8 to establish the same relationship for the remainders, then invoke D7.20 again to restate the conclusion as a ratio. The AI proof is more explicit, separating into four cases (equality, part, parts, multiple) where Heath handles them together, and the AI cites additional foundational items (CN3 for the equality case, D7.3 and D7.5 for the multiple case) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions or common notions rather than substantive propositions, this is a clear case of over-citation at the same backbone -- granularity difference.

### 7.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: convert the proportion into a part-or-parts relationship via D7.20, show that addition preserves that relationship using 7.5 and 7.6, then invoke D7.20 again to re-establish the proportion for the sums. The AI proof adds an explicit treatment of the 'same multiple' case (Step 4), citing CN2 and D7.15, which Heath omits. Since heath_only is empty and ai_only contains only a Common Notion (CN2) and a Definition (D7.15) used for this additional sub-case, the difference is one of citation depth and case granularity rather than a different proof path. This is Case A of Q2: same backbone, different depth.

### 7.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: unpack the given proportion A:B = C:D via Def. 7.20, apply alternation results to obtain A:C = B:D, and conclude via Def. 7.20. Heath handles the alternation in a single step citing only VII.10, while the AI explicitly separates into three cases distinguished by Def. 7.20 (part via 7.9, parts via 7.10, multiple via substitution and 7.9) and cites additional definitions (D5.12, D7.3, D7.5). The ai_only items are either definitions (over-citation) or proposition 7.9, which is the single-part companion to Heath's cited 7.10 and covers the same logical ground at finer granularity. Since heath_only is empty and the key intermediate conclusion -- that the alternation of the part-or-parts relationship holds -- is the same in both proofs, the difference lies only in citation depth, making this a granularity difference.

### 7.14
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: alternate the given proportions using VII.13, chain the resulting ratios by transitivity, and alternate back to reach the desired ex aequali conclusion. The AI generalizes to n numbers rather than Heath's three specific numbers, but this is a presentational choice that does not change the proof structure. The ai_only items (CN1, D5.17, D7.20) are all definitions and common notions that Heath uses implicitly: CN1 licenses the transitivity step Heath performs without citation, D5.17 names the ex aequali definition cited in framing the hypothesis, and D7.20 names the definition of numerical proportion underlying the transitivity chain. Since all key intermediate conclusions match and the citation differences reflect only the depth at which definitions and common notions are made explicit, this is a granularity difference.

### 7.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves alternation of measurement by decomposing both numbers into equal parts, establishing a chain of equal ratios, and then applying VII.12 (as one antecedent is to one consequent, so are all antecedents to all consequents) to conclude the proportion. The AI instead uses a direct combinatorial rearrangement argument: it arranges the units of C in an r-by-s grid (r copies of B, each consisting of s units), then reads the grid by columns rather than rows to show each column equals A and there are s columns, so A measures C exactly s times. These are genuinely different backbones: Heath works through ratio theory while the AI works through unit-grid commutativity. The AI's path is logically complete and sound, so Q3 yields D.

### 7.16
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that the unit measures A the same number of times as B measures C (by definition of multiplication), then apply VII.15 to alternate this relation, repeat the argument for the second product B times A, and combine to conclude C equals D. The AI proof explicitly cites the definition of multiplication (D7.15) and Common Notion 2 (CN2) where Heath uses them implicitly. Since ai_only contains only foundational items (a definition and a common notion) and heath_only is empty, the proofs differ only in citation depth, not in their key intermediate conclusions. Case A of Q2 holds, yielding G.

### 7.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that multiplying a number by two factors produces equal multiples of those factors, express this proportional relationship via Definition 20, then apply alternation (7.13) to obtain the desired ratio. The AI's extra citations D7.15 (definition of multiplication) and D7.5 (definition of measure/multiple) are definitions that Heath invokes implicitly without explicit citation. Since the key intermediate conclusions are identical and the only differences are citation depth for definitional items, this is a granularity difference (G).

### 7.18
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: rewriting A*C=D as C*A=D and B*C=E as C*B=E via commutativity of multiplication (7.16), then applying 7.17 to conclude that D:E = A:B. The only citation difference is the AI's additional reference to Definition 7.15 (the definition of multiplication) in the setup step, which Heath leaves implicit. Since the key intermediate conclusions are identical and the sole ai_only item is a definition providing extra citation depth rather than a substantive divergence, Q2 Case A applies, yielding G.

### 7.19
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs establish the biconditional through the same logical backbone: constructing an auxiliary product, using VII.17 and VII.18 to establish two ratio identities connecting the original proportion to ratios of products, and then combining these identities to reach the conclusion in both directions. The AI uses G=BD as its auxiliary while Heath uses G=AC, but the structural logic is identical. The ai_only citations (5.11, D7.15, D7.20) are all over-citations: 5.11 (transitivity of ratio equality) is used implicitly by Heath when chaining ratio equalities, and D7.15 and D7.20 are definitions Heath invokes without explicit citation. With heath_only empty and the backbones matching, this is Case A of Q2, a granularity difference.

### 7.20
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: assume the least number is 'parts' of the given number, unpack into equal component parts, derive that these components form a ratio equal to the original least numbers' ratio, reach a contradiction with leastness, and conclude the least number is a 'part' that measures the given number. The sole substantive citation difference is that Heath uses 7.12 (antecedents-to-consequents ratio combination) to establish the key ratio equality, while the AI uses alternation via 7.13 to achieve the same intermediate conclusion. The ai_only items (CN5, D7.3, D7.4) are all definitions and common notions that Heath leaves implicit, representing over-citation. Since all key intermediate conclusions are identical and the citation differences reflect depth rather than route, this is a granularity difference.

### 7.21
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: assume for contradiction that smaller numbers C, D exist in the same ratio as coprime A, B; apply 7.20 to establish that C measures A and D measures B the same number of times E; derive that E measures both A and B; reach a contradiction with coprimality via D7.12. The only difference is in how the step 'E measures A' is justified: Heath cites 7.16 (commutativity of multiplication), while the AI cites 7.15 (alternation of measurement) directly. Since Heath's own proof of 7.16 internally relies on 7.15, the AI is simply citing the more fundamental proposition rather than the derived one, a pure citation-depth difference. The additional AI citation D7.2 is a definitional reference with no structural significance. Same backbone, different citation depth yields G.

### 7.22
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow identical proof-by-contradiction backbones: assume A, B (least in their ratio) share a common measure C, define quotient counts, show the quotients have the same ratio as A:B, note the quotients are smaller, and reach a contradiction with leastness. The sole substantive citation difference is that Heath cites 7.17 (one number multiplying two numbers preserves ratio) while the AI cites 7.18 (two numbers multiplying one number preserves ratio). The proof-tree containment test confirms that 7.17 appears inside Heath's proof of 7.18, so the AI cites 7.18 as a higher-level unit while Heath uses its internal component 7.17 directly. The AI's additional citations (CN5, D7.12, D7.2) are a common notion and definitions that make explicit what Heath leaves implicit. All differences are citation-depth differences with identical key intermediate conclusions, yielding G.

### 7.23
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs follow an identical logical backbone: assume for contradiction that C and B are not prime to one another, derive that some D measures both C and B, use transitivity of divisibility (D measures C and C measures A, so D measures A) to show D measures both A and B, contradicting their being prime. The only difference is citation depth: the AI explicitly cites D7.5 (definition of 'measures') and CN2 (common notion) for the transitivity step, which Heath performs without explicit citation. Since ai_only contains only a common notion and a definition (axiomatic-level items) and heath_only is empty, this is a clear case of over-citation with the same backbone, yielding Granularity difference (G).

### 7.24
**Category**: Granularity difference
**Jaccard**: 0.778
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume a common divisor d of C and the product AB, apply 7.23 to get d and A prime, introduce a quotient so that d times the quotient equals the product, use 7.19 to set up a proportion, then 7.21 and 7.20 to conclude d measures B, reaching a contradiction with B and C being prime. The AI proof adds two extra citations (CN1 for the equality of products and D7.2 for the definition of number as a multitude of units) that Heath treats as implicit. Since the key intermediate conclusions are identical and the only differences are citation depth, this is a granularity difference.

### 7.25
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: that both factors of A*A are each prime to B, which by 7.24 yields that the product is prime to B. Heath introduces an auxiliary D equal to A as a formal device to satisfy the 'each of two numbers' language in 7.24, while the AI more directly observes that 7.24 does not require distinct factors and applies it with both factors being A. The logical backbone is identical. The ai_only items (D7.12, D7.15) are definitions the AI explicitly cites but Heath leaves implicit, representing over-citation at the definition level. Since the backbones match and only citation depth differs, this is a granularity difference.

### 7.26
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) E=A*B is prime to C via 7.24, (2) E is prime to D via 7.24, (3) C and D are each prime to E, and (4) F=C*D is prime to E via 7.24. The AI proof follows Heath's logical backbone exactly but explicitly cites two definitions that Heath uses implicitly: D7.12 (symmetry of the coprimality relation) and D7.15 (definition of product/multiplication). Since heath_only is empty and ai_only contains only definitions, this is a clear Case A granularity difference where the AI over-cites at the definitional level while establishing the same substantive chain of reasoning.

### 7.27
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decides the classification. Heath proves squares coprime using 7.25 (squaring preserves coprimality) and then cubes coprime by combining four pairwise coprimality relations via 7.26 (products of pairwise coprime numbers are coprime). The AI instead uses 7.24 (the product rule) directly in a general inductive argument: first establishing that all powers of B are coprime to A by repeated application of 7.24, then for a fixed power B^n, building up A, A^2, ..., A^n each coprime to B^n by the same rule. While both 7.25 and 7.26 are proved from 7.24, the AI does not merely re-derive them inline; it applies 7.24 in a structurally different inductive pattern that entirely avoids the pairwise-product principle of 7.26. For the cubes result, Heath's intermediates are A^3 coprime to B and A^3 coprime to B^2 (inside 7.26's logic), while the AI's intermediates are A coprime to B^3 and A^2 coprime to B^3 — a genuinely different sequence of key conclusions. Since the backbones diverge (Q2 Case B) and the AI's inductive path is logically valid (Q3), the classification is D.

### 7.28
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: the forward direction assumes a common measure of the sum and one summand, deduces it must also measure the other summand (the difference), and derives a contradiction with coprimality; the converse assumes a common measure of both summands, deduces it must measure their sum, and derives a contradiction. The AI proof cites CN2, CN3, CN5, D7.2, and D7.5 in addition to D7.12, while Heath cites only D7.12. All ai_only items are Common Notions and Definitions that Heath uses implicitly but does not cite explicitly, representing a pure citation-depth difference with no change in the argumentative backbone.

### 7.29
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs use the identical contradiction strategy: assume a common measure C exists for prime A and number B (which A does not measure), conclude by primality that C must equal A, then derive the contradiction that A measures B. The key intermediate conclusions are the same in both proofs. The only citation difference is that the AI explicitly cites definitions D7.11 (prime), D7.12 (prime to one another), and D7.2 (unit/number) that Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions, this is a straightforward Case A granularity difference where the AI over-cites foundational definitions relative to Heath's more concise style.

### 7.30
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determines the classification. Heath proves 7.30 by a direct argument: assuming D does not measure A, he derives coprimality via 7.29, constructs a proportion D:A = B:E via 7.19, invokes 7.21 to establish D and A are least in that ratio, and applies 7.20 to conclude D measures B. The AI instead uses proof by contradiction, assuming the prime p measures neither A nor B, obtaining coprimality of both A and B with p via 7.29, then applying 7.24 (if two numbers are each prime to a number, their product is also prime to it) to conclude C = AB is prime to p, contradicting p|C. The key intermediate conclusions differ fundamentally: Heath's backbone runs through proportions (7.19, 7.20, 7.21), while the AI's backbone runs through product coprimality (7.24). This is a genuine path difference with a logically complete alternative chain, yielding D.

### 7.31
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves that any composite number is measured by a prime using an iterative infinite-descent argument: repeatedly factor until a prime is reached, with termination guaranteed by the impossibility of an infinite decreasing sequence of numbers. The AI instead uses a minimality/well-ordering argument: select the least numerical measure of A by finite inspection, then prove by contradiction that this least measure must be prime (if it were composite, a smaller measure of A would exist, contradicting minimality). These are genuinely different proof strategies with different key intermediate conclusions -- Heath's backbone rests on iterative factoring and descent termination, while the AI's backbone rests on the existence and primality of a minimal measure. Both are logically complete and valid, so Q3 confirms the classification as D.

### 7.32
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: (1) consider whether A is prime or composite, (2) if prime, the result holds immediately, (3) if composite, apply 7.31 to conclude a prime number measures A. The AI proof adds explicit citations to definitions D7.11 (prime) and D7.13 (composite) where Heath uses these terms without citation. Since heath_only is empty and ai_only contains only definitions, the difference is purely one of citation depth, not of logical backbone. Case A of Q2 holds, yielding G.

### 7.33
**Category**: Path difference
**Jaccard**: 0.188
**Analysis**: Q2 decided the classification. Both proofs share the high-level strategy of dividing by the GCD and proving minimality by contradiction, but the logical backbones of the minimality arguments diverge fundamentally. Heath introduces a counting number M, establishes a product equality (ED = HM), and applies 7.19 (proportionality from equal products) to conclude M > D, contradicting D being the GCD. The AI instead uses alternation (7.13) to establish a uniform ratio across all index pairs, reduces a representative pair to coprime form via 7.2, then invokes 7.21 (coprime numbers are least in their ratio) and 7.20 (least numbers measure any in the same ratio) to derive that p > 1 measures all the reduced quotients, contradicting their established coprimality. The heath_only citations (7.3, 7.16, 7.19) are not subsumed by any single AI citation under the proof-tree containment test; they belong to a genuinely independent logical chain. The AI's path is logically complete under the hardened 1(b) standard, so Q3 confirms D.

### 7.34
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: The forward dependency gate is clear. Q1: The AI proof is logically complete; it handles trivial cases (equal, one measures the other) and the general case with a valid unified argument through 7.33, which demonstrably covers both Heath's coprime and non-coprime cases. Q2 decides the classification. Both proofs share the same backbone of key intermediate conclusions: (1) construct the LCM candidate as a product, (2) show both numbers measure it, (3) assume a smaller common multiple exists, (4) express it as multiples of A and B, (5) derive a ratio equality among multipliers via 7.19, (6) use the least-ratio property (7.20) to establish divisibility of multipliers, and (7) derive a contradiction. The heath_only citation 7.21 appears inside Heath's proof of 7.33, which the AI cites, satisfying the proof-tree containment test. The other heath_only citation 7.17 is used by Heath to convert multiplier divisibility into product divisibility, while the AI achieves the same contradiction through direct comparison of multiples of A, a difference in citation depth rather than backbone. The ai_only items (CN1, CN2, CN5, D7.5) are all common notions and definitions, representing over-citation typical of granularity differences.

### 7.35
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish the LCM of A and B, show that if it does not divide the given number then a remainder smaller than the LCM is also measured by both numbers, and derive a contradiction with minimality. Heath performs this in a single step (E measuring DF leaves CF less than E, and A, B measure CF), while the AI formalizes the process via explicit repeated subtraction and tracks the divisibility property through each step. The AI explicitly cites 7.34 for the existence of the LCM, definitions D7.2, D7.5, D7.15 for measuring and number concepts, and common notions CN2, CN3, CN5 for the arithmetic reasoning, all of which Heath uses implicitly without citation. Since the key intermediate conclusions are the same and all citation differences reflect depth rather than substance, this is a granularity difference (G).

### 7.36
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: find D = LCM(A,B) via 7.34, then compute LCM(D,C), show all three numbers measure the result, and prove minimality using 7.35. Heath splits into two cases depending on whether C measures D, while the AI gives a single unified argument that subsumes both cases (when C measures D, LCM(D,C) = D). The key intermediate conclusions are identical in both proofs. The ai_only citations (CN2, D7.5, D7.15) are all definitions and common notions that the AI cites explicitly in Step 3 to justify that A and B measure E, whereas Heath treats this transitivity of divisibility as obvious. This is classic over-citation with no change to the logical path, yielding a granularity difference.

### 7.37
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that the unit measures the quotient the same number of times as the divisor measures the dividend, (2) apply VII.15 to obtain the alternate proportion, and (3) conclude the quotient is a part of the dividend named after the divisor. The ai_only set consists entirely of definitions (D7.1, D7.2, D7.3, D7.5) and a common notion (CN5) that Heath uses implicitly without citation. The heath_only set is empty. This is a pure citation-depth difference where the AI over-cites foundational items, yielding G.

### 7.38
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that the unit measures the naming number the same number of times the part measures the whole (from the definition of 'part'), then apply VII.15 (alternation) to conclude that the naming number measures the whole. The AI proof adds an unnecessary but valid case split (B is a unit vs B is a number) and explicitly cites foundational definitions (D7.1, D7.2, D7.3) and a common notion (CN2) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions and common notions, this is strictly over-citation at a finer granularity level, not a path difference. Case A of Q2 holds: same backbone, different citation depth.

### 7.39
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct the least common multiple of the numbers corresponding to the given parts, show the LCM has all the given parts (via 7.37), and prove minimality by showing any number with all the parts is measured by all the corresponding numbers (via 7.38) and hence by the LCM. The difference is citation depth: Heath cites 7.36 (find the LCM of three numbers) as a single unit, while the AI re-derives the LCM construction iteratively using 7.34 (two-number LCM) and proves minimality using 7.35 (if two numbers measure a third, their LCM does too). The proof-tree containment test confirms this: Heath's own proof of 7.36 uses exactly 7.34 and 7.35, the substantive ai_only items. The remaining ai_only citations (CN2, CN5, D7.5) are common notions and a definition, consistent with over-citation at finer granularity.


---

## Book 8 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 8.7, 8.17 |
| Granularity difference (G) | 17 | 8.1, 8.2, 8.3, 8.5, 8.6, 8.8, 8.9, 8.11, 8.12, 8.13, 8.14, 8.15, 8.16, 8.18, 8.20, 8.24, 8.25 |
| Path difference (D) | 8 | 8.4, 8.10, 8.19, 8.21, 8.22, 8.23, 8.26, 8.27 |
| AI proof error (E) | 0 |  |

**Total**: 27 propositions

## Per-Proposition Analysis

### 8.1
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same mathematical backbone: ex aequali (7.14) yields the ratio of extremes, coprimality implies the extremes are least in their ratio (7.21), and the measurement property (7.20) establishes divisibility at the extremes. Heath completes the argument by contradiction (A measures E but E < A), while the AI takes a direct approach, using alternando (7.13) to extend the measurement relation from the extremes to all intermediate terms and citing CN5 for the inequality. The ai_only set consists of two definitions (D7.12, D7.20), a common notion (CN5), and one theorem (7.13) used for an elaboration step on the same backbone. With heath_only empty, the AI's citations are a strict superset of Heath's. This is a same-backbone, different-depth situation: the AI explicitly cites foundational items Heath leaves implicit and adds one intermediate step to handle all terms directly rather than by contradiction.

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct terms by multiplication so each successive ratio equals A:B (using VII.17 and VII.18), show A and B are prime to each other (VII.22), show the extremes of the sequence are prime to each other (VII.27), and conclude the constructed numbers are the least in continued proportion (VIII.1). The AI proof generalizes to n terms using an iterative construction while Heath works a concrete four-term example, but the key intermediate conclusions are identical. The ai_only citations (5.11, 7.33, D7.15) are over-citations: 5.11 makes ratio transitivity explicit where Heath leaves it implicit, 7.33 explicitly reduces to least terms where Heath assumes it, and D7.15 cites the definition of multiplication Heath uses without naming. With heath_only empty and the backbones matching, this is Case A of Q2: same backbone, different citation depth.

### 8.3
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) take the least pair in the given ratio and show they are prime to each other (VII.33, VII.22); (2) construct a comparison sequence in continued proportion whose extremes are powers of that pair, hence prime to each other (VII.27); (3) show the comparison sequence is least, so it equals the original sequence, transferring the primality of the extremes. The difference is citation depth: Heath cites VIII.2 as a single unit to construct the comparison sequence and establish its leastness, while the AI re-derives VIII.2's construction explicitly (citing the lower-level 7.16, 7.17, D7.15 for the ratio-preserving multiplication steps) and directly invokes VIII.1 to establish leastness. Since VIII.1 appears inside Heath's proof of VIII.2, the proof-tree containment test confirms this is a citation-depth difference rather than a path divergence. The additional AI citations (D7.12, D7.15, 7.16, 7.17) are definitions and basic arithmetic facts that Heath uses implicitly through the VIII.2 package. This is Case A of Q2: same backbone, different granularity.

### 8.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. The two proofs have entirely different backbones (Jaccard 0.0 with zero citation overlap). Heath constructs the continued proportion iteratively using LCM (7.34), scales terms proportionally via 7.13 and Def. 20, handles two sub-cases depending on whether E measures K, and proves minimality by contradiction using divisibility properties (7.20, 7.35). The AI instead builds an arbitrary chain with the correct successive ratios by iterated multiplication (using 7.16 and 7.17), then applies 7.33 (find least numbers in the same ratio via GCD) as a global minimization step, and proves minimality by showing any competing chain falls within the class minimized by 7.33. The key intermediate conclusions differ fundamentally: Heath relies on LCM-based pairwise joining and divisibility-based contradiction, while the AI relies on multiplication-based chain construction and GCD-based global reduction. Since the AI's path is logically complete under Q3 — every step is supported by a cited proposition (7.17 for ratio preservation, 7.33 for minimization, 7.14 for ex aequali, 5.11 for transitivity of ratios) — the classification is D.

### 8.5
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct an intermediate product number, establish that the ratio from A to the intermediate equals one side ratio and the ratio from the intermediate to B equals the other side ratio, then combine these to conclude A:B is the compound of the side ratios. Heath uses 7.17 twice for the ratio steps, then 8.4 (least numbers in compound ratio) and 7.14 (ex aequali) for the formal combination. The AI uses 7.18 (the dual of 7.17) for one ratio step and 7.17 for the other, then directly invokes D6.5 (definition of compound ratio) to combine. The key intermediate conclusions are identical; the differences lie only in citation depth at the combination step and in whether 7.17 or its dual 7.18 is cited for one of the ratio establishments.

### 8.6
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: given a continued proportion where the first term does not measure the second, they choose a pair of terms, construct the least numbers in the same continued ratio, show the first of these least numbers is not a unit, establish that the extremes are coprime (both citing 8.3), apply ex aequali (both citing 7.14), and derive a contradiction from the assumption of divisibility. The sole substantive citation difference is that Heath uses 7.33 (find least numbers in a given ratio for any set of numbers) while the AI uses 8.2 (find least numbers in continued proportion), but both achieve the identical intermediate conclusion of obtaining least numbers to work with. The AI's additional citations of definitions D7.2, D7.3, and D7.12 are explicit over-citations of foundational definitions that Heath leaves implicit. Since the key intermediate conclusions are the same and the citation differences reflect depth rather than path, this is Case A in Q2, yielding G.

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both proofs establish proposition 8.7 through an identical proof by contradiction using only proposition 8.6. The logical backbone is the same: assume the first number does not measure the second, apply 8.6 to conclude that no number in the sequence measures any other, observe the contradiction with the hypothesis that the first measures the last, and conclude. The citation sets are identical (ai_used = heath_refs = {8.6}), yielding Jaccard similarity 1.0, and the key intermediate conclusion (the contrapositive application of 8.6) is the same in both proofs. Since the backbone and citation sets match exactly, this is a perfect match (P).

### 8.8
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) obtain a least sequence of numbers in continued proportion, (2) show the extremes are coprime via 8.3, (3) connect the ratio of extremes to the target ratio via ex aequali (7.14), (4) show the extremes measure the target numbers equally via 7.20 and 7.21, (5) scale all intermediate terms by the common multiplier, and (6) conclude the scaled sequence is in continued proportion. The only difference is that Heath uses 7.33 (general method for finding least numbers in a given ratio) while the AI uses 8.2 (specialized construction for least numbers in continued proportion) to produce the minimal sequence — both reach the same intermediate conclusion. The AI additionally cites 7.17 for ratio preservation under multiplication and D7.15 for the definition of multiples, making explicit steps that Heath leaves implicit. These are citation-depth differences, not backbone differences, yielding Case A of Q2 and classification G.

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: establish that the given progression is the least (via VIII.1/8.1), show the endpoints are perfect n-th powers of coprime bases, and then construct geometric sequences from each endpoint to the unit. The key difference is citation depth: Heath cites VIII.2 to construct the least chains of increasing length from the base ratio, while the AI re-derives this construction inline using Book 7 propositions (7.16, 7.17, 7.22, 7.24, 7.33). Heath's proof of VIII.2 itself uses VII.17, VII.22, VII.27, and VIII.1, several of which appear among the AI's citations, confirming that the AI is performing 8.2's work at a lower level of abstraction rather than taking a genuinely different path. The definitions in ai_only (D7.1, D7.12, D7.15) are over-citation. Since the key intermediate conclusions are the same and the difference is only in the depth at which supporting steps are cited, this is a granularity difference.

### 8.10
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 determined the classification. Heath's proof works with a specific illustrative case (m=2), constructing named intermediates H=D*F, K=D*H, L=F*H and chaining ratio equalities via both 7.17 (common first factor) and 7.18 (common second factor) to establish A:K=K:L=L:B. The AI takes a structurally different approach: it proves the general case directly by constructing a parametric family C_j = p^{n-j} * q^j, factors each pair as R_j*p and R_j*q, and applies only 7.17 to obtain a uniform ratio C_j:C_{j+1} = p:q across all consecutive pairs. The AI avoids 7.18 entirely by using 7.16 (commutativity) to rearrange factors so the common multiplier is always first, effectively inlining 7.18's proof. These constitute different backbones: different constructions, different intermediate conclusions, and a different generalization strategy. The AI's path is logically complete under the Q3 check, yielding D.

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct the product of the two sides as the candidate mean proportional, establish two proportions (first-to-mean and mean-to-second equal to side-to-side), conclude the mean proportional exists, then derive the duplicate ratio via V.Def.9. The only difference is citation depth: Heath invokes 7.18 directly for the second proportion (two numbers multiplying one number), while the AI instead uses 7.16 (commutativity of multiplication) plus 7.17 to achieve the same result. The remaining ai_only items are definitional over-citations (D7.15, D7.18, D7.20) and an explicit transitivity step (5.11) that Heath leaves implicit. Since the key intermediate conclusions are identical and the citation differences reflect depth rather than route, this is a granularity difference.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct intermediate numbers as products of the cube sides, show all consecutive ratios equal the ratio of the sides using VII.17 and VII.18, conclude the intermediate numbers are mean proportionals between the two cubes, and apply the definition of triplicate ratio (V.Def.10). The AI's three extra citations (5.11, D7.15, D7.19) are over-citations representing greater explicitness rather than a different proof path: 5.11 explicitly chains proportions that Heath performs verbally, while D7.15 and D7.19 are definitions of multiplication and cube number that Heath invokes without citation. With heath_only empty and the backbones identical, Case A of Q2 holds, yielding G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish mean proportionals between consecutive squares and cubes, observe that the continued proportion of the original numbers gives equal successive ratios in these chains, then apply ex aequali (7.14) to conclude that the squares and cubes are themselves in continued proportion. Heath constructs the intermediate products inline and refers to the method of the foregoing propositions, while the AI explicitly cites 8.11 and 8.12 as established results for the mean proportionals, 5.11 for equal ratios, and various definitions. Since heath_only is empty and all ai_only items represent finer citation depth for the same logical steps, this is Case A: same backbone, different citation depth, yielding G.

### 8.14
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: (1) establish a continued proportion between the two square numbers via a mean proportional, (2) in the forward direction, use 8.7 to show the first extreme measures the mean, then D7.20 to transfer measurement to the sides, (3) in the converse, use D7.20 to transfer side-measurement to the proportion terms, then conclude the square measures the square. The sole substantive citation difference is that Heath cites 8.11 as a unit to establish the continued proportion, while the AI re-derives 8.11's content at a lower level using 7.17 and 7.18 directly. The proof-tree containment test confirms this: Heath's own proof of 8.11 uses 7.17 and 7.18 internally. The remaining ai_only items (D7.5, D7.15, D7.18) are definitions the AI cites explicitly where Heath leaves them implicit. This is a citation-depth difference with the same backbone, yielding G.

### 8.15
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a continued proportion A:M:N:B (Heath uses A:H:K:B) in the ratio of side to side, then apply 8.7 to show the extreme-measuring relation implies the second-term relation, and D7.20 to transfer the ratio to a measurement relation between the sides; the converse reverses this chain. The only difference is citation depth in establishing the continued proportion: Heath cites 8.12 (and 8.11) as a unit, while the AI re-derives the same result inline using 7.17 and 7.18, which are the elementary propositions appearing inside Heath's own proof of 8.12. The AI's additional citations of D7.15, D7.19, and D7.3 are definitions that Heath uses implicitly without citing. The proof-tree containment test confirms this is a citation-depth difference, not a path difference, yielding G.

### 8.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: each direction of the biconditional is proved by contradiction using Proposition 8.14. The AI proof (Steps 2 and 3) mirrors Heath's two-part structure exactly, establishing the same key intermediate conclusions in the same order. The only citation difference is that the AI explicitly cites Definition 7.18 (defining square numbers as products of their sides) when introducing the setup, while Heath leaves this implicit. Since D7.18 is a definitional citation and the logical backbone is identical, this is a citation-depth difference, yielding Granularity difference (G).

### 8.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof both establish two contrapositive results using proposition 8.15 by contradiction. Part 1: assuming cube A does not measure cube B, if side C measured side D then by 8.15 A would measure B, contradiction. Part 2: assuming side C does not measure side D, if A measured B then by 8.15 C would measure D, contradiction. The logical backbone is identical in both proofs, and the citation sets match exactly (both cite only 8.15), yielding Jaccard 1.0. Since ai_used equals heath_refs and the key intermediate conclusions are the same, the classification is P (Perfect match).

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish side proportionality from the definition of similar plane numbers, apply alternation (7.13), construct a cross-product of one side from each number, use VII.17 twice to establish the two ratios flanking the mean proportional, conclude the continued proportion, and derive the duplicate ratio via V.Def.9. The heath_only set is empty, and the ai_only set consists entirely of over-citations: 5.11 (transitivity of proportion, used explicitly by the AI where Heath leaves it implicit), 7.16 (commutativity of multiplication), and definitions D7.15 and D7.16 (multiplication and plane number). Since the backbones are identical and the citation difference is purely one of explicitness, this is Case A of Q2, yielding G.

### 8.19
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification. Heath's proof routes through similar plane numbers K=CD and L=FG, invokes 8.18 to find one mean proportional M between them, uses 7.13 (alternation) to establish that corresponding side ratios are equal, then builds the solid chain A,N,O,B. The AI instead constructs its two means M=(db)c and N=(de)c directly from the sides, then applies 7.17 and 7.18 factor-by-factor to establish A:M=a:d, M:N=b:e, and N:B=c:f, bypassing both 8.18 and alternation entirely. The resulting intermediate numbers differ (the AI's second mean EFG versus Heath's DFH), and the logical backbone is genuinely different: Heath reduces to the plane-number case while the AI works at the individual-factor level throughout. Q3 confirms the AI's path is valid, as each step is properly justified by cited propositions.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 Case A decided the classification. Both proofs share the same key intermediate conclusions: that both numbers are plane (expressible as products of two factors found via VII.33 and VII.20) and that their sides are proportional. The citation differences arise from the AI explicitly citing definitions (D7.15, D7.16, D7.20, D7.21) and a common notion (CN1) that Heath leaves implicit, and from the AI using VII.19 (the equal-products-to-proportionality equivalence) as a single higher-level step where Heath uses VII.17 twice and VII.13 (alternando) as lower-level components. The proof-tree containment test confirms that VII.17 appears within Heath's proof of VII.19, establishing a citation-depth difference for that component. VII.13 is not needed in the AI's proof because its algebraic setup (equating two expressions for the mean proportional) directly produces the sides proportion in the required form without alternation. Since the backbone conclusions are identical, Q2 Case A holds, yielding G.

### 8.21
**Category**: Path difference
**Jaccard**: 0.118
**Analysis**: Q2 decided the classification. Heath's proof works through three-term least proportionals (E, F, G in ratio A:C:D) and pivots on VIII.20 to establish that E and G are similar plane numbers, then builds solid representations using four distinct plane sides (H, K and L, M). The AI takes a fundamentally different route: it reduces A:B to two least coprime terms E:F, uses 8.8 to transfer the two mean proportionals from A,B to E,F, then applies 8.9 to get two mean proportionals between each of E,F and unity, deducing that E and F are perfect cubes (E=r^3, F=s^3). The solid representations A=(kr,r,r) and B=(ks,s,s) with two repeated sides differ structurally from Heath's (H,K,N) and (L,M,O). Since the key intermediate conclusions differ (similar plane numbers vs. cubes) and the AI's chain is logically complete with every step properly cited, this is a valid different path.

### 8.22
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof relies on 8.20 to establish that A and C are similar plane numbers, then concludes C is square because A is square with equal sides and similar plane numbers have proportional sides. The AI proof takes a fundamentally different route: it uses 7.19 to derive A*C = B^2 from the continued proportion, applies 8.14 to conclude that s (the side of A) divides B, constructs t = B/s and T = t^2, then uses ratio arithmetic (7.17, 5.11, 5.9) to show C = T = t^2. The two proofs share zero citations (Jaccard = 0.0) and argue through entirely different key intermediate conclusions: Heath through similar plane numbers, the AI through square divisibility and ratio manipulation. The containment test confirms the divergence is genuine, since the AI's cited propositions (8.14, 7.19, 5.11, 5.9) do not appear inside Heath's proof of 8.20, which uses VII.33, VII.20, VII.17, and VII.13. The AI proof is logically complete and sound, so Q3 yields D.

### 8.23
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof argues through the concept of similar solid numbers via 8.21: since A and D have two mean proportionals between them, they are similar solid numbers, and since A is cube, D must also be cube. The AI takes a fundamentally different algebraic path, deriving B^3 = A^2*D = s^3*D from the continued proportion (where s = a^2 and A = a^3), then applying 8.15 (cube divisibility) to conclude s divides B, writing B = st, and finally showing D = t^3. The citation sets are completely disjoint (Jaccard = 0.0), and the key intermediate conclusions differ entirely: Heath uses similar solid numbers while the AI uses algebraic manipulation and cube divisibility. The AI proof is logically complete under the hardened 1(b) standard, with every step properly supported by citations, so Q3 confirms the different path is valid.

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that one mean proportional falls between the square numbers C and D, (2) transfer this via 8.8 to obtain one mean proportional between A and B, and (3) conclude B is square by 8.22. The sole difference is the citation used for step (1): the AI invokes 8.11, which states directly that between two square numbers there is one mean proportional, while Heath invokes 8.18, the more general result that between two similar plane numbers there is one mean proportional (noting first that squares are similar plane numbers). Since 8.11 and 8.18 establish the identical intermediate conclusion at the same logical position, differing only in generality, this is Case A of Q2 — same backbone, different citation depth — yielding G.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) two mean proportionals fall between the cube numbers C and D, (2) by 8.8 two mean proportionals fall between A and B, and (3) by 8.23 B is cube. The sole difference is that Heath justifies step (1) by observing that cubes are similar solid numbers and invoking 8.19 (the general result for similar solid numbers), while the AI directly invokes 8.12 (the specific result for cube numbers). Since 8.12 and 8.19 establish the same fact for this case at different levels of generality, and the underlying conclusion is present in both proofs at the same logical position, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 8.26
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Heath proves 8.26 by finding a mean proportional between the similar plane numbers (8.18), reducing to the least numbers in the same ratio (7.33 or 8.2), and showing the extremes are square (8.2). The AI takes a fundamentally different path: it uses the second half of 8.18's statement to establish that A:B is the duplicate ratio of the corresponding sides a:c, then constructs explicit squares S=a^2 and T=c^2, applies 8.11 to show S:T is also the duplicate ratio of a:c, and concludes A:B = S:T by the transitivity of ratios (5.11). The two proofs share no key intermediate conclusions: Heath never constructs squares of the sides, and the AI never reduces to least terms. At Q3 the AI's chain is logically complete, each step supported by a valid citation, so the classification is D.

### 8.27
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 decided this classification. Heath's proof works by finding two mean proportionals between A and B (8.19), reducing to least terms in the same ratio (7.33/8.2), and showing the extremes are cubes (8.2), so A:B equals a cube-to-cube ratio. The AI takes a fundamentally different path: it constructs explicit cubes C=a^3 and D=b^3 from the corresponding sides, establishes that A:B is triplicate of a:b (8.19) and C:D is triplicate of a:b (8.12), then uses 5.11 (ratios equal to the same ratio are equal) to equate corresponding terms and 7.14 (ex aequali) to conclude A:B=C:D. The two proofs share only 8.19; the remaining citations are entirely disjoint and reflect genuinely different logical strategies rather than mere depth differences. The AI's chain is logically complete under Q1/Q3, so this is a valid different path.


---

## Book 9 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 9.28, 9.29 |
| Granularity difference (G) | 16 | 9.4, 9.6, 9.7, 9.14, 9.16, 9.17, 9.20, 9.21, 9.22, 9.23, 9.24, 9.30, 9.31, 9.33, 9.34, 9.35 |
| Path difference (D) | 18 | 9.1, 9.2, 9.3, 9.5, 9.8, 9.9, 9.10, 9.11, 9.12, 9.13, 9.15, 9.18, 9.19, 9.25, 9.26, 9.27, 9.32, 9.36 |
| AI proof error (E) | 0 |  |

**Total**: 36 propositions

## Per-Proposition Analysis

### 9.1
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath proves that the product C is square by introducing an auxiliary square D = A*A, establishing the ratio A:B = D:C via VII.17, transferring the mean proportional count from A,B to D,C via VIII.8, and concluding via VIII.22 (if the first of three continued proportionals is square, the third is too). The AI takes a fundamentally different path: it obtains the mean proportional M between A and B via 8.18, then directly applies 7.19 (product of extremes equals product of means in a proportion) to conclude A*B = M*M, yielding squareness immediately. The AI never introduces the auxiliary square D, never uses ratio transfer (VII.17), never invokes VIII.8 or VIII.22. These are different key intermediate conclusions (Case B in Q2). Under Q3, the AI's chain is logically complete: every step from premises to conclusion is supported by a valid citation, so the different path is valid, yielding D.

### 9.2
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary square D = A squared, establishes the ratio A:B = D:C via VII.17, observes that D and C are both square (hence similar plane numbers), uses VIII.18 to find a mean proportional between D and C, then transfers that mean proportional to A and B via VIII.8, and finally applies VIII.20. The AI takes a fundamentally different and more direct route: from the definition of square number (D7.18) it writes A times B = C times C, then applies the converse of VII.19 (if the product of the first and fourth equals the product of the second and third, the four numbers are proportional) to the four numbers A, C, C, B to obtain A:C = C:B directly, making C the mean proportional between A and B without any auxiliary construction, and concludes via VIII.20. The key intermediate conclusions differ entirely: Heath routes through D, the ratio D:C, and a chain of three propositions (VII.17, VIII.18, VIII.8), while the AI bypasses all of this with a single application of VII.19. The AI's path is logically valid and complete, yielding a genuine path difference.

### 9.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works through the theory of mean proportionals: it establishes two mean proportionals between the unit and A (via VII.Def.20), extends this to two mean proportionals between A and B using VIII.8, and then applies VIII.23 to conclude B is cube. The AI proof takes a fundamentally different, more elementary approach: it directly decomposes the cube A as a*b (where b = a*a), builds proportions a:b = b:A and a:b = A:c (where c = b*b) using Book 7 multiplication and ratio propositions (7.16, 7.17), derives b*c = A*A = N via 7.19, and concludes N = b*b*b is cube by definition. The two proofs share zero citations (Jaccard = 0.0) and argue through entirely different key intermediate conclusions, making this a clear path difference. The AI proof is logically complete: each step follows validly from its predecessors using the cited propositions.

### 9.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: define D = A*A as cube by 9.3, establish D:C = A:B by 7.17, then conclude C is cube because D is cube and the ratio D:C is a cube-to-cube ratio. The difference lies entirely in citation depth for the final step. Heath re-derives the internals of this reasoning inline using three propositions (8.19 to get mean proportionals between similar solids A and B, 8.8 to transfer those mean proportionals to D and C, and 8.23 to conclude from four numbers in continued proportion with the first being cube). The AI instead cites 8.25 as a single unit, which packages exactly that chain — Heath's own proof of 8.25 uses precisely 8.19, 8.8, and 8.23. The proof-tree containment test confirms all heath_only items appear inside Heath's proof of the AI's cited proposition 8.25, establishing this as a citation-depth difference rather than a path difference.

### 9.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2 (Case B) leading to Q3. The two proofs have completely different logical backbones with zero citation overlap (Jaccard = 0.0). Heath's proof works through proportionality theory: forming D = A squared (a cube by 9.3), establishing the ratio A:B = D:C via 7.17, then using the theory of similar solids (8.19) and mean proportionals (8.8, 8.23) to conclude B is cube. The AI's proof instead uses a direct construction approach: exploiting 8.15 to establish that the cube root of A measures the cube root of C, constructing D = d cubed from the measurement quotient, showing AD = C via commutativity (7.16), and cancelling to get B = D (hence B is cube). Both paths are logically complete under the hardened Q1(b) standard, yielding category D.

### 9.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification via the proof-tree containment test. The AI proof establishes that C = A^3 is cube by definition, then applies 9.5 ('If a cube number by multiplying any number make a cube number, the multiplied number will also be cube') to conclude A is cube. Heath's proof reaches the same conclusion but re-derives the internals of 9.5 inline, setting up the proportion A:B = B:C via VII.Def.20, then using VIII.19 (similar solid numbers have two mean proportionals), VIII.8 (transferring mean proportionals across equal ratios), and VIII.23 (concluding a number with two mean proportionals to a cube is itself cube). All three substantive heath_only items (8.19, 8.8, 8.23) appear inside Heath's own proof of 9.5, confirming the AI cites 9.5 as a unit while Heath expands its internals. This is a citation-depth difference, not a backbone difference.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 Case A decided the classification. Both proofs share the same logical backbone: decompose composite number A into factors D and E (via D7.13 and D7.15), establish that E times D equals A, then conclude that C equals D times E times B and is therefore solid. The AI proof differs only in explicitly citing D7.2 (definition of number) to justify that E is a number and D7.17 (definition of solid number) to justify the final conclusion, both of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions, this is purely a citation-depth difference with identical key intermediate conclusions.

### 9.8
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Heath proves the first term is square directly (A*A = B via Def. 20), then propagates squareness and cubeness along continued proportions using 8.22 and 8.23 respectively. The AI instead derives a general index-addition law u_{r+s} = u_s * u_r using 7.18 (ratio preservation under multiplication by a common number), then specializes: u_{2r} = u_r^2 is square, u_{3r} = u_r^3 is cube, and u_{6r} is both. The containment test confirms these are genuinely different paths: 8.22 relies on 8.20 (similar plane numbers) and 8.23 relies on 8.21 (similar solid numbers), neither of which appears in the proof tree of 7.18. The AI's chain is logically complete under the 1(b) standard, running from the continued proportion hypothesis through the index-addition law to all three assertions, so Q3 confirms a valid different path.

### 9.9
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Scope correction applied: Prop 9.9 statement asks only about the square case. Heath's cube-case extension and its citations (8.23, 9.3) excluded from comparison. The AI proves only the square case, which is the full scope of the proposition. Forward-dependency gate: 9.1 (b=9, n=1 < 9) not forward; D7.x definitions never forward. Gate passes. Q1(a): No multi-case structure in the square-case statement; AI addresses it fully. Q1(b): Each step is sound. Step 2 derives A_{i+1} = A_1 * A_i from the proportion relation. Step 3 correctly identifies two squares as similar plane numbers (equal-sided rectangles with proportional sides). Step 4 correctly applies 9.1 (product of similar plane numbers is square). Step 5 completes the induction. NOT-E. Q2: Different backbones. Heath uses IX.8 (alternate terms are square) then VIII.22 (in three continued-proportion numbers, first square implies third square) applied to consecutive triples (A,B,C), (B,C,D), etc. AI uses an inductive scheme through 9.1 (product of similar plane numbers is square), showing each A_i and A_1 are similar plane numbers. VIII.22 and 9.1 are independent propositions; no containment (9.1 is in Book IX, cannot appear inside VIII.22's proof). Case B. Q3: Gate passed (positional validity). AI chain from premises to conclusion is complete and logically sound. Path difference (D).

### 9.10
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: SCOPE CORRECTION: Proposition 9.10's statement concerns only the square case. Heath's proof includes the cube case as a bonus extension after completing the square case proof. The AI proves only the square case, which is the full scope of the proposition statement. Citations 8.25 and 9.6 are excluded from Heath's effective set as cube-case-only. Effective Heath citations for the square case: 8.26, 9.8. Forward-dependency gate: all AI citations (7.14, 8.22, 9.8, D7.20) are prior to 9.10 — pass. Q1: The AI proof is logically complete. It correctly uses 9.8 to establish that even-indexed terms are square, then shows by contradiction (via 7.14 and 8.22) that no odd-indexed term can be square. No E triggers. Q2: The backbones differ. Heath argues through the ratio of consecutive terms being square-to-square and uses 8.26 (converse) to identify similar plane numbers. The AI establishes a non-consecutive three-term proportion via 7.14 and propagates squareness directly via 8.22. Different key intermediate conclusions — Case B. Q3: The AI's chain from premises to conclusion is complete and sound. Path difference (D).

### 9.11
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves the proposition by extracting one ratio directly from the continued proportion (A:B = D:E) and then applying alternation (7.15) to convert the unit-measure relationship into the required divisibility result. The AI takes a fundamentally different route: it constructs two parallel chains of equal length with matching consecutive ratios and applies ex aequali (7.14) to obtain the proportion a0:a_d = ai:aj directly, then derives divisibility from the unit-measure property. The proof-tree containment test confirms these are independent paths: 7.15 does not appear inside Heath's proof of 7.14 (which uses 7.13 instead). Since the backbones differ and the AI's chain via ex aequali is logically sound and complete from premises to conclusion, the classification is D.

### 9.12
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof uses proof by contradiction with proportion theory: assuming the prime E does not measure A, he repeatedly applies VII.19 (proportion from product equality), VII.21 (primes are least), and VII.20 (least numbers measure proportionals) to descend from D through C and B, reaching a contradiction when E is shown to measure A. The AI instead takes a direct approach using VII.30 (Euclid's Lemma: if a prime divides a product, it divides one factor). The AI establishes that each term aⱼ equals a₁ times aⱼ₋₁ from the continued proportion, then applies VII.30 backward from aₙ to a₂ = a₁ squared, forcing the prime to divide a₁. These are fundamentally different proof strategies with different key intermediates: Heath works through ratios and coprimality, while the AI works through prime divisibility of products. The AI's path is logically complete and valid, so the classification is D.

### 9.13
**Category**: Path difference
**Jaccard**: 0.071
**Analysis**: Q2 decided this classification. Heath's proof descends through explicit quotients E, F, G, H using product identities (9.11, 9.8) and proportions (7.19) to eventually reach a contradiction with A being prime. The AI proof takes a structurally different approach: it selects a_k, the listed term with greatest index that divides d, shows that any prime dividing the quotient q = d/a_k must equal p (via 7.32 and 9.12), and concludes that a_{k+1} also divides d, contradicting the maximality of k. The only shared citation is 9.12; the remaining citations reflect entirely different proof mechanisms. The AI's index-based maximal element argument is logically complete and valid but follows a genuinely different logical backbone from Heath's explicit descent through proportions, yielding a path difference.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction: assume an extra prime q divides the least number N measured by given primes, write N = M*q, apply 7.30 to conclude each given prime divides M, and derive a contradiction from M < N. The key intermediate conclusions are identical. The AI's extra citations (D7.2, D7.5, D7.11, D7.15, CN5) are all definitions and a common notion that Heath leaves implicit, representing over-citation of foundational concepts rather than a different proof path. This is Case A of Q2: same backbone, different citation depth.

### 9.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath decomposes A, B, C into squares and products of a least ratio pair DE, EF (via VIII.2), establishes DE and EF are prime (VII.22), then uses composition-of-primality results (VII.24, VII.25, VII.28) together with algebraic identities (II.3, II.4) to derive the coprimality of each pair-sum with the remaining number. The AI takes a fundamentally different path: it applies VIII.3 directly to establish that the extremes A and C are prime, uses VII.19 to obtain the product identity AC = B^2, and then proves all three cases by contradiction, showing that any hypothetical prime common factor of a pair-sum and the remaining number would force a common factor of A and C, violating their coprimality (using VII.30 and VII.32). The Jaccard similarity is 0.0 with completely disjoint citation sets, and the key intermediate conclusions differ entirely: Heath works through the ratio-pair decomposition and algebraic identities, while the AI works through direct extremal primality and contradiction via prime divisors. The AI proof is logically complete and valid, establishing a genuine path difference.

### 9.16
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume A:B = B:C for contradiction, apply 7.21 (primes are least in their ratio), apply 7.20 (least numbers measure those with same ratio) to deduce A measures B, note A also measures itself so A is a common measure of A and B, and conclude this contradicts their being prime to one another. The AI proof explicitly cites definitions D7.1, D7.2, and D7.12 to spell out that A is a number (not a unit) and what it means for numbers to be prime to one another, whereas Heath leaves these definitional facts implicit. Since the backbones are identical and the only citation differences are these explicit definitions, Case A of Q2 holds, yielding G.

### 9.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: assume for contradiction that the last term is to some number as the first to the second, derive a proportion linking the coprime extremes to adjacent terms, invoke VII.21 (primes are least) and VII.20 (least measure proportionals) to conclude the first term divides the second, then chain divisibility through the continued proportion to show the first divides the last, contradicting coprimality. The sole substantive citation difference is that Heath uses alternation (7.13) directly on the assumed proportion while the AI uses ex aequali (7.14) on two shifted sequences to reach the same intermediate proportion. The proof-tree containment test confirms this is a depth difference: 7.13 appears inside Heath's proof of 7.14, so the AI cites 7.14 as a unit where Heath deploys 7.13 at a lower level. The remaining ai_only items (D7.2, D7.12, D7.15, D7.20) are definitions that Heath uses implicitly, representing over-citation rather than structural divergence.

### 9.18
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof first distinguishes whether A and B are coprime, citing 9.16 to handle that case separately, then tests whether A measures B-squared for the non-coprime case. The AI proof bypasses the coprime distinction entirely, instead applying a unified measurement test (repeated subtraction of A from B-squared) that directly determines whether a third proportional exists. The proof-tree containment test confirms this as a genuine path difference: 9.16 does not appear inside the proof of 7.19, the AI's only substantive citation. The AI's unified approach is logically complete under the hardened standard: the measurement test correctly handles all sub-cases including the edge case where the quotient equals one (a unit, not a number per D7.1 and D7.2), and 7.19 correctly establishes the proportionality when the quotient is at least two. Q3 confirms the AI's different path is valid, yielding D.

### 9.19
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Heath organizes the investigation into four cases based on whether the three numbers are in continued proportion and whether the extremes are coprime, using 9.17 for the continued-proportion-with-coprime case, ex aequali (7.14) with primes-are-least (7.21) and least-measure (7.20) for the non-continued-proportion-with-coprime case, and a divisibility test for the remaining cases. The AI instead gives a single unified criterion: form P = BC and test whether A divides P by repeated subtraction, justifying the equivalence entirely through 7.19 (proportion iff product equality) and 7.16 (commutativity of multiplication). Because the key intermediate conclusions differ fundamentally -- Heath reasons through coprimality and continued proportion while the AI reduces everything to a single divisibility test -- the backbones are different (Case B in Q2). Q3 confirms the AI path is logically valid: the chain from premises to conclusion is sound, yielding D.

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a common multiple of the assigned primes, add a unit to obtain a new number, then consider whether it is prime or not. If prime, a new prime is found directly; if not, any prime factor of the new number cannot equal any assigned prime (since it would then measure both the common multiple and the new number, hence the unit, a contradiction). The AI cites 7.32 where Heath cites 7.31; the proof-tree containment test confirms that 7.31 appears inside Heath's proof of 7.32, so the AI simply invokes the higher-level result as a unit while Heath applies the component lemma directly. The remaining ai_only items (7.34 for constructing the common multiple, plus definitions D7.1, D7.2, D7.5, D7.15 and common notions CN3, CN5) are explicit over-citations of construction steps, definitions, and axioms that Heath leaves implicit. The key intermediate conclusions are identical in both proofs, making this a granularity difference.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: each even number is split into two equal halves (D7.6), those halves are combined so the whole sum also has a half, and therefore the whole is even (D7.6). The AI explicitly cites CN2 (equals added to equals are equal) to justify the step of combining the individual halves into a total, whereas Heath treats this inference as implicit. Since the ai_only item CN2 is a Common Notion (an axiom-level over-citation) and heath_only is empty, this is a straightforward Case A granularity difference: same backbone, different citation depth.

### 9.22
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: subtract one unit from each odd number to obtain even remainders (D7.7), sum the even remainders to get an even total (9.21), note the sum of the removed units equals the multitude which is even by hypothesis, then combine the two even sums to conclude the whole is even (9.21). The AI's extra citations CN2 (Common Notion 2 for the addition step) and D7.2 (definition of number to justify that the sum of n units is n) are foundational items that Heath uses implicitly without citing. Since heath_only is empty and the ai_only items are purely axiomatic/definitional over-citations, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 9.23
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) separating the odd-multitude sum so that an even count of odd numbers remains, whose sum is even by 9.22; (2) subtracting a unit from one odd number to obtain an even remainder by D7.7; (3) combining the two even quantities via 9.21; and (4) concluding the total equals that even sum plus a unit, hence odd by D7.7. The only citation difference is that the AI explicitly invokes CN2 (Common Notion 2) for an algebraic substitution step that Heath leaves implicit. Since CN2 is an axiom and the key intermediate conclusions are identical, this is a citation-depth difference, placing the proof in category G.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: each splits the even minuend and even subtrahend into two equal halves (by Definition 7.6), then concludes that the remainder likewise splits into two equal halves and is therefore even. The AI proof makes the intermediate arithmetic explicit by citing Common Notions (CN2 for adding/subtracting magnitudes, CN3 for equals subtracted from equals, CN5 for the whole being greater than the part), whereas Heath leaves these inferential steps implicit. Since ai_only contains only Common Notions and heath_only is empty, the difference is purely one of citation depth, not of proof strategy. This is Case A of Q2: same backbone, different granularity.

### 9.25
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Heath proves the result directly by constructing an auxiliary even number: subtracting a unit from the odd subtrahend BC to obtain an even number DB, applying 9.24 to show that AB minus DB (i.e., AD) is even, and then concluding that CA is odd because it is one less than the even number AD. The AI instead uses proof by contradiction, assuming the remainder R is even, applying 9.24 to show that A minus R would be even, using CN3 to identify A minus R with B, and deriving a contradiction since B is odd. These represent genuinely different logical backbones -- direct construction versus reductio ad absurdum -- so the proof is classified as D (path difference). The AI's contradiction argument is logically complete and valid.

### 9.26
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof is direct: it subtracts a unit from both the odd minuend and the odd subtrahend to obtain two even numbers (AD and CD), then applies 9.24 (even minus even is even) to conclude the remainder CA is even. The AI proof takes a fundamentally different route via proof by contradiction: it assumes the remainder R is odd, observes that two odd numbers (B and R) constitute an even multitude, and applies 9.22 (the sum of an even count of odd numbers is even) to derive that A = B + R would be even, contradicting the hypothesis that A is odd. These are different logical backbones (Q2 Case B). Under Q3, the AI's proof by contradiction is logically complete and valid, with every step properly supported by citations, so the classification is D.

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof is direct: it subtracts a unit from the odd number to obtain an even remainder, applies 9.24 (even minus even is even) to show an intermediate quantity is even, then restores the unit to conclude oddness via Def. 7.7. The AI proof takes a fundamentally different path via proof by contradiction: it assumes the remainder is even, then uses 9.21 (sum of even numbers is even) to show the original odd number would be even, reaching a contradiction. Since the key intermediate conclusions differ — Heath works through even-minus-even (9.24) while the AI works through even-plus-even (9.21) yielding a contradiction — the backbones are different (Q2 Case B). The AI's contradiction chain is logically complete under Q3, so the classification is D.

### 9.28
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21 is prior and D7.15 is a definition). Both proofs follow an identical logical backbone: express the product C as a repeated sum of the even number B using Definition VII.15, observe that every summand is even, then apply Proposition IX.21 (sum of even numbers is even) to conclude C is even. The AI citation set {9.21, D7.15} equals the Heath citation set {9.21, D7.15} exactly, yielding Jaccard 1.0. Since Q1 found no logical errors, Q2 confirmed the same key intermediate conclusions, and the citation sets match perfectly, the classification is P (Perfect match).

### 9.29
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.23 is prior to 9.29 and D7.15 is a definition). Q1 confirmed the AI proof is logically complete: it correctly establishes that C equals A copies of B by the definition of multiplication (D7.15), observes each summand is odd and their count is odd, then applies 9.23 to conclude the sum is odd. Q2 confirmed the same backbone in both proofs. Since ai_used equals heath_refs exactly ({9.23, D7.15}), the classification is P (Perfect match).

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: express B as a multiple of A, show the multiplier must be even by contradiction (if odd, B would be odd), and conclude A measures half of B. The sole substantive citation difference is that the AI cites 9.29 (product of two odd numbers is odd) where Heath cites 9.23 (sum of an odd multitude of odd numbers is odd). The proof-tree containment test confirms that 9.23 appears directly inside Heath's proof of 9.29, so the AI is citing a higher-level packaging of the same underlying fact. The remaining ai_only items (CN2, D7.5, D7.6, D7.7, D7.15) are all definitions and common notions representing over-citation of implicit axioms. This is a citation-depth difference with the same backbone, yielding G.

### 9.31
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume some D > 1 measures both A and C (the double of B), conclude D must be odd because it divides odd A, apply 9.30 to show odd D measuring even C must also measure its half B, then derive a contradiction with A and B being prime to one another. The key intermediate conclusions are identical in both proofs. The ai_only set consists entirely of definitions (D7.5, D7.6, D7.7, D7.12) and one substantive proposition (9.21) cited explicitly to justify why D must be odd, a step Heath states without formal citation. The heath_only set is empty. This is classic over-citation at a finer granularity with no change to the logical backbone, placing the proof squarely in Case A of Q2.

### 9.32
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: The classification is decided at Q2 (Case B) and confirmed at Q3. Heath proves the exclusivity of even-times even by invoking 9.13, which establishes that the only divisors of the last term in a geometric progression starting from unity with a prime ratio are the preceding terms in the chain; since all chain members are even, every factorization yields even factors. The AI takes a fundamentally different route: it uses 9.30 in a descent argument to show that no odd number can divide any member of the doubling chain (an odd divisor would propagate down through successive halves until it measured the unit, a contradiction), then invokes 7.16 (commutativity of multiplication) to convert any hypothetical even-times-odd decomposition into an odd divisor, contradicting the descent result. These are genuinely different key intermediate conclusions -- 'measured only by proportional chain members' (Heath via 9.13) versus 'no odd divisor exists' (AI via 9.30) -- constituting different backbones at Q2. The AI's path is logically complete at Q3, yielding category D.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that the number is even-times odd (because its odd half measures it an even number of times), then assume for contradiction that it is also even-times even, derive that the half would need to be even, and conclude by contradiction. The AI proof adds explicit citations for definitions (D7.6, D7.7, D7.15) and propositions (7.16 for commutativity, 9.21 for the sum-of-evens result) that Heath leaves implicit or states without citation. The empty heath_only set confirms Heath cites nothing the AI lacks. Since the key intermediate conclusions are identical and the differences are purely in citation depth, this is a granularity difference.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) A is even-times even because its half is not odd, by Definition VII.8; (2) successive bisection of A must terminate at an odd number (by reductio: reaching a dyad would make A one of those continually doubled from a dyad, contradicting the hypothesis), and this odd number measures A according to an even number, making A even-times odd. The AI proof elaborates each step by explicitly citing definitions (D7.2, D7.6, D7.7, D7.9, D7.15), common notions (CN2, CN5), and Proposition 7.16 (commutativity of multiplication), all of which Heath leaves implicit. Since heath_only is empty and ai_only consists entirely of definitions, common notions, and one minor theorem that merely makes explicit what Heath takes for granted, this is Case A: same backbone, different citation depth.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they connect the continued proportion's individual term ratios to aggregate sums via VII.12, then derive the excess ratios using separando (VII.11) and alternando (VII.13). The order of operations differs slightly (Heath applies separando to the chain of equal ratios first then sums; the AI sums first via VII.12 then applies separando), but the logical backbone is identical. The ai_only items CN2 and D7.20 are a Common Notion and a Definition that Heath uses implicitly, representing over-citation by the AI rather than a substantive path difference. heath_only is empty, confirming no missing citations. This is Case A of Q2: same backbone, different citation depth.

### 9.36
**Category**: Path difference
**Jaccard**: 0.105
**Analysis**: Q2 decided the classification. Heath's proof and the AI proof have fundamentally different logical backbones. Heath relies on proportional reasoning (7.14 ex aequali, 7.19 product-proportion equivalence) and the geometric series summation formula 9.35 to show that FG equals the sum of all terms, then proves uniqueness of divisors through the chain 9.13, 7.29, 7.21, 7.20 (prime-to-one-another and least-number arguments). The AI instead derives a summation identity A = 1 + B directly from the doubling property, characterizes all divisors of A via 9.11 and 9.13, constructs two disjoint families of proper divisors, and proves their completeness using 7.30 (Euclid's lemma: if a prime divides a product it divides one of the factors). These represent genuinely different argumentative strategies, not merely different citation depths for the same intermediate conclusions. The AI's path is logically valid under Q3(b): every step is supported by cited propositions and the inference chain from premises to the conclusion that N is perfect is complete and sound.


---

## Book 10 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 68 | 10.2, 10.3, 10.4, 10.7, 10.8, 10.9, 10.12, 10.13, 10.14, 10.15, 10.16, 10.17, 10.19, 10.20, 10.21, 10.25, 10.36, 10.37, 10.38, 10.39, 10.40, 10.41, 10.42, 10.44, 10.45, 10.46, 10.47, 10.49, 10.54, 10.55, 10.56, 10.57, 10.58, 10.59, 10.60, 10.61, 10.62, 10.63, 10.64, 10.65, 10.66, 10.71, 10.72, 10.74, 10.76, 10.77, 10.79, 10.80, 10.81, 10.82, 10.83, 10.84, 10.85, 10.89, 10.90, 10.92, 10.93, 10.94, 10.96, 10.97, 10.98, 10.99, 10.101, 10.102, 10.103, 10.108, 10.109, 10.110 |
| Path difference (D) | 47 | 10.1, 10.5, 10.6, 10.10, 10.11, 10.18, 10.22, 10.23, 10.24, 10.26, 10.27, 10.28, 10.29, 10.30, 10.31, 10.32, 10.33, 10.34, 10.35, 10.43, 10.48, 10.50, 10.51, 10.52, 10.53, 10.67, 10.68, 10.69, 10.70, 10.73, 10.75, 10.78, 10.86, 10.87, 10.88, 10.91, 10.95, 10.100, 10.104, 10.105, 10.106, 10.107, 10.111, 10.112, 10.113, 10.114, 10.115 |
| AI proof error (E) | 0 |  |

**Total**: 115 propositions

## Per-Proposition Analysis

### 10.1
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath proves 10.1 by direct step-by-step comparison, showing that at each stage the remainder in the original magnitude is dominated by the corresponding segment of a multiple of the lesser magnitude (DF=C > AK). The AI proof instead uses a proof by contradiction: assuming all first n remainders are at least B, it shows the total subtracted exceeds nB (which exceeds A by D5.4), contradicting that A bounds the sum of all subtractions plus the final remainder. These are different logical backbones (Case B in Q2), and the AI's indirect argument is logically sound with no gaps (Q3(b) holds), yielding a path difference.

### 10.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume for contradiction that the magnitudes are commensurable, so some magnitude E measures both; then E measures every remainder produced by the alternating subtraction process; eventually a remainder falls below E; but E measures it, so it must be at least E, yielding a contradiction. The AI explicitly invokes 10.1 (repeated more-than-half removal) to justify that a remainder eventually drops below E, whereas Heath asserts this directly from the finiteness of the subtraction process without citing any proposition. The AI also makes explicit the definitions (D5.2, D10.1.1) and common notions (CN2, CN3, CN5) that Heath leaves entirely implicit. Since Heath cites nothing at all while the AI over-cites, and both proofs establish the same key intermediate conclusions in the same logical order, this is Case A of Q2: same backbone, different citation depth.

### 10.3
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they handle the trivial case where the smaller magnitude measures the larger, then apply the anthyphairesis (Euclidean algorithm) process with termination justified by 10.2, show the terminal remainder is a common measure by reversing the subtraction chain, and prove it is the greatest common measure. The only difference is citation depth: the AI explicitly cites definitions (D5.2, D10.1.1) and common notions (CN2, CN3, CN5) that Heath uses implicitly without citation. The heath_only set is empty, confirming that the AI covers all of Heath's cited references. This is a pure granularity difference in citation practice, not a difference in proof strategy.

### 10.4
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: The forward dependency gate passes (all AI citations precede 10.4). Q1 finds no logical error: the AI proof is complete, covering both of Heath's cases through a unified approach that always applies 10.3 to find GCM(D,C) rather than splitting into separate cases. Q2 determines the classification: both proofs share the same backbone of finding the GCM of the first two magnitudes (D), then finding the GCM of D with the third magnitude (E), and showing E is the overall GCM. The AI differs only in granularity, explicitly re-deriving the anthyphairesis process for finding D (citing 10.2 for termination, plus definitions D5.2, D10.1.1 and common notions CN2, CN3) where Heath simply invokes 10.3 as a black box. Since heath_only is empty and all ai_only items represent over-citation of foundational material or re-derivation of what 10.3 already provides, the classification is G.

### 10.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof chains ratio identities via V.7 (inverse ratio) and V.22 (ex aequali) to conclude A:B = D:E, working through intermediate conclusions C:A = unit:D and C:B = unit:E. The AI proof bypasses all ratio-manipulation propositions entirely, instead constructing numbers M and N (using a two-unit base T to satisfy D7.1/D7.2) and directly verifying the equimultiple condition of D5.5 by showing that for arbitrary multiples r and s, the ordering of rA vs sB always matches the ordering of rM vs sN. These are genuinely different logical backbones: Heath uses established proportion theorems while the AI works from the foundational definition of equal ratio. Q3 confirmed the AI's path is logically valid and complete, yielding D.

### 10.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 10.6 by direct construction: dividing A into D equal parts, forming F from E copies of that part, then chaining ratio results (V.7, V.22, V.11, V.9) to show B equals F, so both magnitudes share a common measure C. The AI instead uses an antanairesis (iterative subtraction) approach: repeatedly applying separando (5.17) to reduce the numerical ratio to equality, arguing termination by finite descent, then reversing the subtractions to show both magnitudes are multiples of a common residual E. The two backbones are entirely different, with zero citation overlap (Jaccard 0.0). The AI's chain is logically complete: separando is correctly applied, the termination argument is sound, and the reversal validly establishes the common measure. This is a genuine path difference.

### 10.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use identical logical backbones: assume A:B equals a ratio of numbers, apply 10.6 to conclude commensurability, then derive a contradiction with the hypothesis of incommensurability. The only citation difference is that the AI explicitly cites D10.1.1 (the definition of incommensurable magnitudes) to unpack what incommensurability means, whereas Heath invokes that definition implicitly. Since D10.1.1 is a definition and not a substantive proposition, this is a citation-depth difference under Case A of Q2, yielding G.

### 10.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the same proof by contradiction: assume A and B are commensurable, apply 10.5 to derive that A:B equals a ratio of numbers, note the contradiction with the hypothesis, and conclude incommensurability. The key intermediate conclusions are identical in both proofs. The only citation difference is that the AI explicitly cites D10.1.1 (the definition of commensurable magnitudes) whereas Heath invokes this concept implicitly. Since D10.1.1 is a definition rather than a substantive proposition, this is a case of over-citation at the definitional level, fitting Case A of Q2: same backbone, different citation depth.

### 10.9
**Category**: Granularity difference
**Jaccard**: 0.235
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: converting commensurability to a number ratio via X.5, establishing that the square ratio is the duplicate of the line ratio via VI.20, that the square-number ratio is the duplicate of the side ratio via VIII.11, and then equating these to conclude the first assertion; for the converse, reversing the duplicate ratio argument and applying X.6; and handling the incommensurable cases by contradiction. The AI proof adds substantial over-citation in the form of definitions (D1.22, D5.5, D5.9, D6.1, D7.18, D10.1.1), postulates (P2, P3, P4), a construction proposition (1.46), intermediate ratio results (5.11, 5.22), and the explicit converse proposition 6.22 where Heath simply reuses VI.20 in both directions. Since heath_only is empty and all 13 ai_only items are either definitions, postulates, or finer-grained citations for steps already present in Heath's proof, this is a clear case of same backbone with different citation depth.

### 10.10
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 decides the classification. Heath establishes the square-incommensurable line by taking a mean proportional E between A and D, then applying X.11 (if four magnitudes are proportional and the first is incommensurable with the second, the third is incommensurable with the fourth) to transfer the length-incommensurability of A,D into the square-incommensurability of A,E. The AI takes a genuinely different path: it constructs two mean proportionals b and c using VI.13, derives Q(a):Q(c) = a:b via VI.17/VI.1/V.11, then uses X.7 (incommensurable magnitudes do not have a numerical ratio) and X.8 (magnitudes without a numerical ratio are incommensurable) to establish the square-incommensurability of a and c. This is not a depth difference but a different logical mechanism: Heath transfers incommensurability via a proportionality rule (X.11), while the AI converts incommensurability into a statement about non-numerical ratios (X.7) and re-applies that characterization (X.8). The AI also differs in its construction, choosing the specific ratio 2:3 and building lines explicitly via bisection (I.10) and postulates, whereas Heath uses any abstract non-square ratio and the general construction of X.6. The proof is logically complete under the hardened standard, so the valid different backbone yields D.

### 10.11
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. For the commensurable case, both proofs share the same backbone: apply 10.5 to get a numerical ratio, transfer it to C:D, then apply 10.6 to conclude commensurability. However, for the incommensurable case the backbones diverge. Heath uses a direct argument via 10.7 (incommensurable magnitudes do not have a numerical ratio) and 10.8 (magnitudes without a numerical ratio are incommensurable). The AI instead proves this case by contradiction: assuming C is commensurable with D, it applies 10.5 to obtain a numerical ratio for C:D, uses 5.11 (ratio transitivity) to transfer that ratio to A:B, then applies 10.6 to conclude A is commensurable with B, contradicting the hypothesis. This is a genuinely different logical path that avoids 10.7 and 10.8 entirely, substituting a valid reductio argument that reuses the commensurable-case machinery. The contradiction argument is logically complete and sound, so Q3 confirms D.

### 10.12
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: express A:C and C:B as numerical ratios via 10.5, construct three numbers with a common middle term preserving both ratios, chain the proportions via 5.11, apply ex aequali (5.22) to obtain A:B as a numerical ratio, and conclude commensurability via 10.6. The only difference lies in how the three intermediate numbers are constructed. Heath invokes 8.4, which finds the least numbers in continued proportion in given ratios, while the AI directly constructs the numbers by multiplication (X=mp, Y=np, Z=nq) and justifies the resulting ratios using the basic arithmetic propositions 7.17 and 7.18. The key intermediate conclusion -- that three numbers exist with the required ratio relationships -- is identical in both proofs, making this a citation-depth difference rather than a path difference.

### 10.13
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy with identical key intermediate conclusions: assume B is commensurable with C, apply 10.12 (transitivity of commensurability) to deduce A is commensurable with C, reach a contradiction with the hypothesis that A is incommensurable with C, and conclude B is incommensurable with C. The only difference is that the AI explicitly cites definition D10.1.1 (definition of commensurability) three times to justify references to common measures, while Heath leaves this definitional invocation implicit. Since heath_only is empty and ai_only contains only a definition, this is a pure over-citation case with no backbone divergence, placing it squarely in Q2 Case A as a granularity difference.

### 10.14
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 Case A decides the classification. Both proofs share the same key intermediate conclusions: (1) the proportion of squares S(a):S(b) = S(c):S(d) via 6.22, (2) the proportion a:e = c:f, and (3) the commensurability/incommensurability transfer via 10.11. The difference lies in the proportion manipulation route: Heath uses separando (5.17) and ex aequali (5.22) to derive A:E = C:F, while the AI uses alternando (5.16) and the remainder proportion (5.19) to reach the same conclusion through a different algebraic path. Additionally, the AI over-cites construction steps (1.46 for constructing squares, 2.14 for constructing f from the excess) and an ordering result (5.14) that Heath leaves implicit. These are citation-depth differences in how proportion algebra is conducted, not backbone differences, since the key geometric facts and logical structure are identical.

### 10.15
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: in the forward direction, a common measure of the two summands is shown to measure the whole; in the converse direction, a common measure of the whole and one summand is shown to measure the remainder. The AI proof explicitly cites axiom-level items (CN2, CN3, CN5, D5.2) that Heath invokes implicitly, while heath_only is empty, indicating the AI omits nothing but over-cites foundational axioms. This is a citation-depth difference with identical key intermediate conclusions, yielding G.

### 10.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same two contrapositives by contradiction: (1) if A and B are incommensurable, then assuming A+B commensurable with one summand leads to A and B being commensurable, a contradiction; (2) if A+B is incommensurable with one summand, then assuming A and B commensurable leads to A+B being commensurable with that summand, a contradiction. The key intermediate conclusions are identical. The only difference is that the AI cites 10.15 (the commensurable analogue of 10.16) as a unit to license the critical inference in each direction, whereas Heath re-derives the same common-measure argument inline. Since heath_only is empty and the AI's additional citation 10.15 packages exactly the reasoning Heath spells out directly, this is a citation-depth difference, not a path difference.

### 10.17
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs establish the same biconditional with identical key intermediate conclusions: (1) the algebraic identity a-squared equals b-squared plus d-squared, and (2) the equivalence between commensurability of the application parts and commensurability of a with d. The difference lies entirely in citation depth. For the algebraic step, Heath uses II.5 with a midpoint construction then quadruples, while the AI uses II.8 directly to obtain the same identity without a midpoint. For the commensurability chain, Heath cites X.15 (componendo/separando), X.6 (equal magnitudes commensurable), and X.12 (transitivity), while the AI re-derives these results from the definition of commensurability (D10.1.1) using common notions and arithmetic. The zero Jaccard similarity reflects this systematic granularity shift: the AI works at a lower level of abstraction, citing definitions, common notions, and basic Book 1-2 propositions where Heath cites established Book 10 theorems. Since the backbone conclusions are the same and only the depth of justification differs, this is Case A under Q2, yielding G.

### 10.18
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Heath proves both directions of this biconditional by a direct chain of commensurability and incommensurability lemmas (10.16, 10.6, 10.13), propagating incommensurability through sums and differences of the segments. The AI instead proves both directions by contradiction using 10.17, the commensurable counterpart of 10.18: if the incommensurability conclusion were false, 10.17 would yield commensurate parts (or a commensurate excess line), contradicting the hypothesis. The proof-tree containment test confirms that heath_only items (10.13, 10.16) are not inside Heath's proof of 10.17 (which uses 10.15 and 10.12), so the AI's contradiction strategy is a genuinely independent route, not a higher-level packaging of the same steps. Both proofs are logically complete, but they argue through entirely different key intermediate conclusions, making this a path difference.

### 10.19
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: they use VI.1 (6.1) to establish a proportion between the rectangle and a square constructed on one of the given lines, then apply X.11 (10.11) to convert the commensurability in length of the two given lines into commensurability of the rectangle with that square, and conclude rationality of the rectangle. The AI proof adds an explicit transitivity step (10.12) to connect the rectangle to the square on the assigned rational line u, whereas Heath connects directly to the square on AB, which is already rational. The ai_only items are all definitions (D2.1, D10.1.2, D10.1.3), a construction proposition (1.46), and a transitivity lemma (10.12), representing deeper citation depth rather than a different logical path. With heath_only empty, the AI covers all of Heath's reasoning at finer granularity, placing this squarely in Case A of Q2.

### 10.20
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that the square on the given line is commensurable with the rational area, apply VI.1 to obtain the ratio between the line and the breadth, then use X.11 to transfer commensurability in length, and finally conclude that the breadth is rational. The AI proof elaborates this backbone by introducing an explicit reference rational line u, constructing squares via 1.46, invoking transitivity of commensurability (10.12) explicitly, and citing the definitions of rationality (D10.1.2, D10.1.3, D2.1) that Heath leaves implicit. All ai_only items are construction propositions, definitions, or explicit transitivity steps; heath_only is empty. This is Case A of Q2: same key intermediate conclusions at different citation depth, yielding G.

### 10.21
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification. Both proofs establish the same key intermediate conclusion: the rectangle contained by two rational lines commensurable in square only is irrational because, were it rational, the two lines would be commensurable in length, contradicting the hypothesis. Heath demonstrates this explicitly by constructing the proportion DB:BC = AD:AC via 6.1, then transferring incommensurability via 10.11. The AI achieves the same result by citing 10.20 directly in a proof by contradiction. The proof-tree containment test confirms that the heath_only items (10.11 and 6.1) both appear inside Heath's own proof of 10.20, so the AI is citing 10.20 as a unit while Heath re-derives its internals inline. This is a citation-depth difference, yielding G.

### 10.22
**Category**: Path difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. The first half of both proofs shares the same backbone: both invoke 10.21 to express the square on the medial line as a rectangle of rational lines commensurable in square only, derive a proportion from the equal rectangles (Heath via 6.14, AI via 6.16), apply 6.22 to obtain a proportion of squares, and use 10.11 to transfer commensurability and conclude rationality of the breadth. However, the second half -- establishing that the breadth is incommensurable in length with the base -- follows a genuinely different logical path. Heath builds a chain of commensurability and incommensurability transfers using 10.13, showing that sq(CD) is incommensurable with rect(DC,CB) and converting via a Lemma. The AI instead uses a proof by contradiction via 10.19: if the two rational lines were commensurable in length, their rectangle would be rational, contradicting the irrationality of the medial area established by 10.21. Since the key intermediate conclusions for the incommensurability argument differ (Case B in Q2), and the AI's contradiction argument is logically valid (Q3), the classification is D.

### 10.23
**Category**: Path difference
**Jaccard**: 0.417
**Analysis**: Q2 decides the classification. Heath's proof applies the squares on A and B as rectangles on a newly set-out rational line CD, then uses 10.22 to characterize the breadth ED as rational and incommensurable in length with CD, and transfers these properties to DF via 10.13. The AI proof instead starts from the medial definition (10.21) to express Q(m) as a rectangle of rational lines r, s commensurable in square only, then constructs a third proportional t via 6.11 and 6.17 so that Q(n) = rect(r,t), and separately establishes that t is rational through a chain of commensurability results (10.9, 10.6, 10.12) and that t is incommensurable in length with r via 10.13. These constitute genuinely different backbones: Heath relies on the area-application technique pivoting on 10.22, while the AI uses third proportionals and builds rationality from scratch. The heath_only citation 10.22 does not appear inside the proof tree of any AI-cited proposition, confirming that the AI takes a different route rather than merely citing at different granularity. Both paths are logically complete, so the classification is D.

### 10.24
**Category**: Path difference
**Jaccard**: 0.133
**Analysis**: Q2 decided the classification. Heath's proof works through direct commensurability: it constructs the square on AB (which is medial), shows the square DA is commensurable with rectangle AC via VI.1 and X.11, and concludes AC is medial by X.23 (an area commensurable with a medial area is medial). The AI proof takes a fundamentally different approach: it introduces a rational straight line r, constructs fourth proportionals u and v so that the areas a-squared and [a,b] equal [r,u] and [r,v] respectively, then uses X.22 to characterize u as rational and incommensurable in length with r, transfers the commensurability of a and b to u and v, deduces that v is rational and commensurable in square only with r via X.9, X.6, X.12, and X.13, and concludes via X.21 that [r,v] is medial. These are genuinely different backbones with different key intermediate conclusions, and the AI's chain is logically complete, so the classification is D.

### 10.25
**Category**: Granularity difference
**Jaccard**: 0.438
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they reduce the rectangle contained by two medial straight lines (commensurable in square only) to a rectangle of two rational lines applied to an assigned rational line, then case-split on whether those rational lines are commensurable in length (yielding a rational area) or commensurable in square only (yielding a medial area via X.21). The AI uses third and fourth proportional constructions (6.11, 6.12) rather than Heath's direct application of areas to a single rational line, but the key intermediate conclusions are the same: a rational breadth is obtained from applying the medial square, the original rectangle is shown equal to a rectangle of two rational lines, and the two exhaustive cases are handled identically. Since heath_only is empty, the AI captures all of Heath's logical content; the ai_only items consist entirely of definitions (D2.1, D10.1.1, D10.1.2, D10.1.3), construction propositions (6.11, 6.12), and auxiliary ratio results (5.9, 6.22, 10.12) that Heath leaves implicit. This is a citation-depth difference, not a path difference.

### 10.26
**Category**: Path difference
**Jaccard**: 0.235
**Analysis**: Q2 reveals genuinely different proof backbones, leading to classification D at Q3. Both proofs proceed by contradiction from the assumption that a medial area exceeds another by a rational area, and both apply the areas to a rational line to obtain breadths. However, Heath's key chain works through incommensurability transfer: he shows EG is incommensurable with GH (10.13), derives that sq(EG) is incommensurable with rect(EG,GH) via a proportion (10.11), uses 10.6 and 10.13 to show the sum of squares is incommensurable with twice the rectangle, and applies 10.16 to conclude sq(EH) is incommensurable with the sum of squares, making EH irrational — contradicting its rationality. The AI instead works through commensurability transitivity: it shows all squares on the rational breadths are commensurable with the reference square U (10.12), uses 10.15 (converse) to derive that the rectangle T = rect(y,z) is rational, then applies 10.20 to conclude y is commensurable with z and hence with r — contradicting that y is incommensurable with r. The contradiction targets differ (EH irrational vs. y commensurable with r), the intermediate conclusions differ (incommensurability chain vs. commensurability chain), and the cited tools differ (10.11/10.13/10.16/10.6 vs. 10.12/10.15). The AI's path is logically sound, so Q3(b) yields D.

### 10.27
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Heath constructs the two medial lines by taking a mean proportional C between two given rational lines A, B commensurable in square only, then building a fourth proportional D via VI.12, showing D medial through X.23 (commensurability with a medial line preserves mediality), and proving the rectangle rational via alternando (V.16). The AI takes a fundamentally different construction: it starts from a single rational line r, constructs s commensurable in square only with r via 10.10, forms a third proportional t via 6.11 such that st = r^2, shows t rational and commensurable in length with s via 10.20, then takes two separate mean proportionals x (of r,s) and y (of r,t), proving both medial directly via 10.21. The AI establishes commensurability in square only through ratio chains using 6.1, 10.11, 5.11, and 6.22, and proves the rectangle rational via the converse of 6.22. The key intermediates differ in substance: Heath uses fourth proportional plus mediality transfer (10.23), while the AI uses third proportional plus two mean proportionals with direct mediality. The heath_only citations (10.23, 5.16, 6.12) are not subsumed by any single AI citation but reflect genuinely different proof steps. The AI proof is logically complete with every claim properly supported by cited propositions, constituting a valid alternative path.

### 10.28
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 determined the classification. Heath's proof works abstractly: starting from three arbitrary rational lines commensurable in square only, it constructs D and E via mean proportionals and proportional arrangement, uses X.11 to transfer commensurability in square only, X.23 addition to show E is medial, and V.16 alternation with VI.16 to equate rectangles. The AI proof takes a fundamentally different constructive path: it builds specific numerical lines (a=2r, b=3r, c=5r), proves that ratios 2:3, 4:5, 5:6 are not ratios of square numbers using arithmetic propositions 8.11 and 8.8, constructs medial lines x and y as mean proportionals, and establishes xy = pq through a chain of proportional equalities (6.1, 5.11, 6.22, 6.16) rather than Heath's alternation approach. The key intermediate conclusions differ: Heath uses X.11 and X.23 addition (neither cited by the AI), while the AI uses 10.9, 10.6, and number-theoretic arguments absent from Heath. Both paths are logically complete, yielding a valid path difference.

### 10.29
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Heath constructs his pair of lines using a semicircle on AB and a ratio DC:CE of square numbers whose difference is not square, deriving AF via X.6 and the excess line BF via convertendo (V.19, III.31). The AI instead constructs an equilateral triangle on AB, bisects it, and uses the altitude CD to obtain the specific ratio Q(AB):Q(CD) = 4:3, then shows via number theory (8.11, 8.8) that this ratio is not square-to-square. The constructions, the intermediate lines (AF/BF vs CD/AD), the ratio arguments, and the excess lines are all different, placing these proofs on genuinely different backbones. The AI's chain is logically complete: every step from the equilateral triangle construction through the Pythagorean theorem, the number-theoretic argument, and the application of X.9 to the final conclusion is sound and supported by citations.

### 10.30
**Category**: Path difference
**Jaccard**: 0.118
**Analysis**: Q2 determined this classification. Heath's proof uses a semicircle construction with carefully chosen square numbers CE, ED whose sum CD is not square, applying 10.6 to set up a ratio DC:CE = BA^2:AF^2, then convertendo (5.19) and III.31/I.47 to derive the incommensurability of AB with BF via 10.9. The AI proof takes a fundamentally different approach: it constructs a square on the rational line AB and considers its diagonal AC, proving AC^2 = 2*AB^2 by the Pythagorean theorem, then shows AB and AC are incommensurable in length by a direct arithmetic contradiction (if m^2 = 2n^2, then by 8.14 n divides m, forcing m^2 >= 4n^2, a contradiction). The key intermediate conclusions differ entirely: Heath works through number-theoretic ratio conditions on auxiliary square numbers, while the AI exploits the irrationality of the diagonal of a square. Both paths are logically complete and valid, yielding classification D.

### 10.31
**Category**: Path difference
**Jaccard**: 0.190
**Analysis**: Q2 decided the classification. Heath constructs medial lines C and D via area equations (sq(C)=rect(A,B) and rect(C,D)=sq(B)), then shows D is medial through X.23 (commensurability with a medial line). The AI instead constructs a third proportional c to a and b, then takes mean proportionals m and n between a,b and b,c respectively, showing each is medial directly via 10.21 applied to distinct pairs of rational lines commensurable in square only. The key intermediate conclusions differ: Heath relies on the proportion A:B = sq(C):rect(C,D) = C:D derived from the area constructions, while the AI derives m:n = a:b through a ratio chain m^2:n^2 = ab:bc = a:c = a^2:b^2. The heath_only citations (10.23 for showing D medial via commensurability with C, and 10.30 for the incommensurable variant) are not contained in the AI's approach, which uses fundamentally different constructions. The AI's path is logically complete and valid, establishing all required properties (mediality, commensurability in square only, rational rectangle, square-difference condition) through a sound chain of reasoning.

### 10.32
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof starts from three rational straight lines (via 10.29) and uses rectangle-equality constructions with proportionality transfer (10.14, 6.4, 6.8, 6.16) to derive medial lines D, E with the required properties. The AI proof takes a fundamentally different approach: it starts from two medial lines already containing a medial rectangle (via 10.28), constructs a third proportional, and then uses the bisection-gnomon identity (2.5) to build a new line d such that d squared equals b squared plus e squared, establishing the square-difference condition directly through commensurability arithmetic (10.6, 10.9, 10.12). The backbones differ in starting objects (rational vs medial), key constructions (rectangle-equality vs bisection), and transfer mechanisms (10.14 vs direct computation). The extremely low Jaccard of 0.143 reflects this genuine path divergence. The AI proof is logically complete under the Q1 hardened standard, with each step validly supported by cited propositions.

### 10.33
**Category**: Path difference
**Jaccard**: 0.077
**Analysis**: The forward-dependency gate passed (all AI citations precede 10.33). Q1 found no logical defects: the AI proof constructs sum-difference segments p=a+c, q=a-c from the 10.30 lines, proves pq=b^2 via 2.5, shows p and q incommensurable by indirect argument using 10.15 and 10.12, constructs mean proportionals x and y via 6.13 so that x^2=ap and y^2=aq, derives x^2+y^2=2a^2 (rational) by 2.1, establishes x^2 and y^2 incommensurable via 10.11, and proves xy=ab (medial) through a proportion chain using 5.11, 6.22, and 6.16. Q2 determined that the backbones differ fundamentally: Heath uses a semicircle construction with area application (6.28), the Pythagorean theorem (1.47), and incommensurability from 10.18, while the AI uses sum-difference segments, mean proportionals, and proportion theory from Books 2, 5, and 6. These are entirely different geometric techniques with no shared key intermediate conclusions beyond the common starting point (10.30) and final medial step (10.21). Q3 confirmed the AI's different path is valid, yielding classification D.

### 10.34
**Category**: Path difference
**Jaccard**: 0.115
**Analysis**: The proofs diverge fundamentally at the construction level. Heath begins with two medial straight lines obtained from X.31 and uses a semicircle construction (III.31, I.47) to produce the target lines AD and DB, deriving the medial sum of squares from the medial square on AB and the rational rectangle from the doubling relation with BC via X.6. The AI instead begins with two rational straight lines from X.30 and constructs the target lines through mean and fourth proportionals (VI.12, VI.13), deriving the medial sum from the product ba being medial by X.21 and the rational rectangle from half of b-squared being commensurable with b-squared via X.12. The classification is decided at Q2 (Case B): the key intermediate conclusions differ in starting lines (medial vs rational), geometric construction method (semicircle vs proportionals), and paths to establishing each of the three required properties. Since the AI alternative chain is logically complete under the hardened Q1(b) standard, the classification is D (Path difference).

### 10.35
**Category**: Path difference
**Jaccard**: 0.033
**Analysis**: Q2 decided the classification. Heath's proof uses the semicircle construction from X.32, deriving AD and DB as perpendicular segments in a semicircle and establishing mediality through III.31, I.47, X.18, and X.32. The AI proof takes a fundamentally different algebraic-arithmetic route: it proves that certain ratios are not ratios of square numbers using Book 7 number theory, constructs auxiliary lines e, f, t with specified square relationships, applies the sum-and-difference identity from 2.5, then builds the final lines x and y as mean proportionals via Book 6 proportion theory. The two proofs share only 10.11 among their citations (Jaccard 0.033), and their key intermediate conclusions are entirely different in both method and substance. The AI proof is logically complete, with every step from construction through verification of all four required properties (incommensurability in square, medial sum of squares, medial rectangle, mutual incommensurability) fully justified.

### 10.36
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: the sum of squares on the two lines is rational, the rectangle (or twice it) is incommensurable with the rational standard, and therefore the square on the whole is irrational. The difference lies in citation depth. The AI uses 10.21 directly to establish that the rectangle of two rational lines commensurable in square only is irrational, packaging the step that Heath derives inline using 10.11 (proportionality-commensurability transfer) and VI.1; the proof-tree containment test confirms that 10.11 appears inside Heath's proof of 10.21, so this is citation-depth, not path divergence. Similarly, the AI cites D10.1.1 (definition of commensurability) instead of 10.6 to justify that R and 2R are commensurable, and adds 10.12 (transitivity) and additional definitions (D10.1.2, D10.1.3) as explicit citations for facts Heath leaves implicit. These are all granularity differences: the same geometric argument at different levels of detail.

### 10.37
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that the sum of the squares on the two medial lines is incommensurable with twice their rectangle, (2) apply II.4 and X.16 to conclude the square on the whole is incommensurable with a rational area, (3) conclude irrationality. Heath obtains step (1) by cross-referencing the argument from X.36 lines 9-20, while the AI re-derives it explicitly using 10.15, 10.21, and 10.13. The proof-tree containment test confirms this: heath_only contains only 10.36, and Heath's own proof of 10.36 uses 10.13 and 10.15, which are the substantive items in ai_only. The remaining ai_only items (D10.1.1, D10.1.2) are definitions representing over-citation. This is Case A in Q2: same backbone at different citation depth, yielding G.

### 10.38
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs argue through the same key intermediate conclusions: applying the relevant areas (squares on the medial lines and twice their rectangle) to a rational line to obtain breadths, showing those breadths are rational via X.22, proving the sum of squares is incommensurable with twice the rectangle via X.11/X.15/X.6/X.13, concluding the breadths are rational commensurable in square only, and applying X.36 to establish irrationality of the total breadth, from which the irrationality of the whole line follows. The citation differences are purely at the construction and detail level: Heath uses I.44 for area application while the AI uses 6.12/6.16 for fourth proportionals to achieve the same construction; the AI additionally cites definitions D10.1.2 and D10.1.3 explicitly, lemmas 10.9 and 10.12 for commensurability of squares, and 2.1 for distribution of a rectangle over parts. These are all citation-depth differences, not backbone differences, so Q2 Case A holds and the classification is G.

### 10.39
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) twice the rectangle is incommensurable with the sum of squares, (2) the square on the whole equals the sum of squares plus twice the rectangle, (3) by 10.16 the square on the whole is incommensurable with the sum of squares, and (4) therefore the square on the whole is irrational. The difference lies only in the sub-lemma chains used to establish step 1: Heath goes through 10.6 and 10.23 to show twice the medial rectangle is itself medial and hence incommensurable with the rational sum, while the AI introduces the unit square and uses transitivity of incommensurability (10.13) together with 10.21 and D10.1.1 to reach the same conclusion. The AI also makes the algebraic identity (2.4) explicit where Heath leaves it implicit. Since the key intermediate conclusions are identical and only the citation depth differs, this is a granularity difference.

### 10.40
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: given that the sum of the squares on the two lines is medial and twice the rectangle is rational, they establish that these two areas are incommensurable, then apply 10.16 to show the square on the whole line is incommensurable with twice the rectangle, and conclude irrationality via Def 4. The AI proof is more explicit, citing 2.4 for the algebraic identity, 10.21 for the step from medial to irrational, 10.13 for transitivity of incommensurability, and D10.1.1 for the definition of rational areas. Heath compresses all of these into a terse narrative. The sole heath_only citation, 10.34, is a setup reference to the construction proposition that produces the required lines, which the AI simply takes as hypothesis. All differences are citation-depth differences with identical key intermediate conclusions, yielding Case A of Q2.

### 10.41
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: apply the two medial areas to a rational line to obtain rational breadths, show those breadths are incommensurable in length (from the incommensurability of the original areas), conclude the breadths are rational and commensurable in square only, invoke X.36 to establish their sum is irrational (binomial), and deduce the original line is irrational. The AI applies S and R separately (getting breadths u and v) rather than applying S and 2R directly as Heath does, which introduces extra sub-steps (10.12, 10.13, definitions) to prove 2v is rational, but this does not alter the backbone. The large ai_only set consists entirely of construction propositions (1.44), transitivity lemmas (10.12, 10.13), a subsidiary result (10.20), distribution (2.1), a common notion (CN2), and definitions (D10.1.1-D10.1.3) that Heath uses implicitly. The sole heath_only item (10.35) is a condition reference the AI states directly. Case A of Q2 holds: same backbone, different citation depth.

### 10.42
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification. Both proofs follow the same reductio structure: assume two distinct divisions of the binomial AB, establish that the rectangles contained by each pair of terms are medial areas (via 10.21), establish that the sums of squares on each pair are rational, apply II.4 (2.4) to both divisions to derive the identity linking the differences of the square-sums and the double-rectangles, then conclude that a medial area exceeds another medial by a rational area, contradicting 10.26. The AI proof adds granular citations not in Heath's extracted references -- definitions (D2.1, D10.1.1, D10.1.3, D10.1.4), common notions (CN1, CN3, CN5), and intermediate propositions for commensurability reasoning (10.12, 10.15) and algebraic distribution (2.1) -- but these all provide more explicit justification for the same logical steps that Heath takes implicitly. With heath_only empty and ai_only consisting entirely of lower-level supporting citations, this is a clear case of same backbone with different citation depth.

### 10.43
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Both proofs use the algebraic identity AB^2 = (sum of squares) + 2*(rational rectangle) for each division and invoke 10.26 (a medial area does not exceed a medial area by a rational area) as the core contradiction tool. However, the logical backbones diverge. Heath derives the contradiction in one direct step: the difference of the sums of squares equals the difference of twice the rational rectangles, which is rational, so medial areas differ by a rational area, contradicting 10.26. The AI proof instead uses 10.26 to establish an intermediate result (R = S, that the two rational rectangles must be equal), then deploys a completely separate geometric argument in Step 6: from R = S and distinct division points, distributivity yields DC*CB = AD*DC, which implies CB = AD, contradicting the established ordering AD > DB > CB. This second-stage rectangle-equality argument is a key intermediate conclusion entirely absent from Heath, making the backbone genuinely different. The AI's chain is logically complete and sound throughout, so Q3 confirms a valid different path.

### 10.44
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume two divisions of the second bimedial, apply areas to a rational straight line, show the resulting lengths are rational and commensurable in square only (forming a binomial), then invoke binomial uniqueness (10.42) to derive a contradiction or force equality of the original terms. The AI proof makes every supporting step explicit, citing 10.42 (binomial uniqueness), intermediate commensurability results (10.12, 10.15, 10.9), algebraic identities (2.1, 2.7), proportionality constructions (6.12, 6.16), definitions, and common notions, all of which Heath uses implicitly without citing. Since heath_only is empty and all ai_only items are lower-level supporting results or axioms that Heath employs without citation, the proofs have the same key intermediate conclusions at different citation depths, giving Granularity difference (G).

### 10.45
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction from the same setup (10.39): assuming a major line AB can be divided at two points C and D, both establish that the sums of squares on the parts are rational and the rectangles are medial, then show the difference of the sums of squares equals the difference of twice the rectangles, conclude this difference is rational, and derive a contradiction via 10.26 (a medial area cannot exceed a medial area by a rational area). The AI proof adds a midpoint construction (1.10), explicit algebraic identities (2.4, 2.5), commensurability lemmas (10.12, 10.15), definitions (D10.1.1, D10.1.4), and common notions (CN2, CN3, CN5) to justify steps that Heath performs implicitly. Since the key intermediate conclusions are identical and the extra citations provide finer granularity for the same logical backbone, this is a granularity difference.

### 10.46
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs use the same contradiction strategy: assume two divisions of AB, show the difference of the twice-rectangles equals the difference of the sums-of-squares, establish that this difference is rational while the sums-of-squares are medial, and reach a contradiction via 10.26. The AI proof spells out every sub-step explicitly, citing algebraic identities (2.1, 2.4), commensurability results (10.12, 10.15), common notions (CN1, CN2, CN3, CN5), and definitions (D10.1.1, D10.1.4) that Heath leaves implicit. Since heath_only is empty and all ai_only items are supporting sub-steps within the same logical backbone, this is Case A of Q2: same key intermediate conclusions at different citation depth, yielding G.

### 10.47
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume two divisions of AB, apply the resulting medial areas to a rational straight line, show the breadths are rational and incommensurable via 10.22 and 6.1/10.11, construct a binomial via 10.36, and derive contradiction through the uniqueness of binomial division (10.42). The AI proof adds substantial extra citation granularity (10.41 for the defining properties, 10.12 and 10.13 for commensurability lemmas, 2.1 and 2.7 for algebraic identities, 5.9 for proportionality, 6.11 and 6.17 for geometric constructions, plus definitions D10.1.1-3 and common notion CN5) but establishes the same key intermediate conclusions in the same logical order. The heath_only set is empty, confirming no cited steps are missing from the AI proof. This is Case A of Q2: same backbone with different citation depth, yielding G.

### 10.48
**Category**: Path difference
**Jaccard**: 0.059
**Analysis**: Q2 decided this classification. Heath's proof constructs the first binomial by setting up numbers with specific ratio properties (Lemma I after X.28), then building segments via X.6, establishing incommensurability via X.9, and using convertendo (V.19) for the square-excess condition. The AI proof takes a fundamentally different approach: it invokes X.29 to directly obtain two rational lines with the needed properties, then transfers all properties to the assigned rational line through fourth proportionals (6.12), using 10.11 for commensurability transfer and 10.14 for the square-excess transfer. The backbones diverge in method, not just citation depth -- Heath uses a number-theoretic setup while the AI uses an existence theorem and proportion-transfer technique. The AI's chain is logically complete: every step from 10.29 through 6.12, 10.11, 6.22, 10.14, and 10.36 is supported by valid citations, and the inferences are sound. This is a valid alternative path to the same conclusion.

### 10.49
**Category**: Granularity difference
**Jaccard**: 0.056
**Analysis**: The forward-dependency gate found no violations. Q1 confirmed the AI proof is logically complete: it constructs the second binomial by invoking 10.29 to obtain rational lines commensurable in square only with the right square-difference property, then uses proportional transfer (10.14, 10.11) to adapt these lines so the lesser term equals the assigned rational line. Q2 determined the classification: both proofs establish the same key intermediate conclusions -- two rational lines commensurable in square only, the square on the greater exceeding the square on the lesser by a commensurable square, and the lesser term commensurable with the assigned rational line -- confirming the same logical backbone. The proof-tree containment test shows that all three heath_only citations (10.6, 10.9, 5.19) appear inside Heath's proof of 10.29, meaning the AI cites 10.29 as a unit while Heath re-derives its internals inline. The AI's additional citations (10.11, 10.14, 6.12, 6.22) are proportional-transfer machinery needed to adapt 10.29's output rather than independent backbone conclusions. This is a citation-depth difference yielding G.

### 10.50
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Both proofs must verify the same defining conditions of a third binomial straight line (rational terms commensurable in square only, neither commensurable in length with the assigned rational, excess of squares commensurable with the greater term), but they reach these conditions by fundamentally different constructions and mathematical tools. Heath uses an abstract number-theoretic ratio setup with carefully chosen numbers AC, CB, D, relying on ratio-manipulation theorems from Books 5 and 10 (10.6 for commensurability via number ratios, 5.22 ex aequali for transitive ratio chains, 5.19 convertendo for the excess condition). The AI instead constructs explicit lines as multiples of the assigned rational (u=2r, v=3r) and uses mean proportionals from Book 6 (6.13, 6.17), area algebra from Book 2 (2.1, 2.4), and number theory from Book 8 (8.24) to establish the required properties through direct algebraic computation. The heath_only propositions (10.6, 5.19, 5.22) do not appear inside the proofs of any AI-cited proposition, confirming these are independent routes from different mathematical domains rather than depth differences. The AI proof is logically complete with no defects under the hardened Q1(b) standard.

### 10.51
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The two proofs have completely different logical backbones (Jaccard = 0.0, zero shared citations). Heath constructs the fourth binomial by setting out numbers with non-square ratios, using X.6 to relate those ratios to squares on lines, and X.9 to derive incommensurability, building the construction from number-theoretic conditions and convertendo (V.19). The AI instead leverages the pre-established result 10.30 to obtain auxiliary rational lines commensurable in square only with the needed excess property, then uses a fourth proportional (6.12) and the transfer result 10.14 to move those properties onto lines related to the assigned rational, before assembling the binomial via 10.36. Q1 finds no logical error: each AI step is supported by correctly cited propositions (10.30 supplies the construction, 10.14 transfers the excess property, 10.11 transfers commensurability through proportions, 10.36 classifies the sum as binomial). Q2 identifies fundamentally different key intermediate conclusions (Case B): Heath reasons through number ratios and X.6/X.9, while the AI reasons through pre-built constructions and proportion transfers. Q3 confirms the AI path is logically complete, yielding classification D.

### 10.52
**Category**: Path difference
**Jaccard**: 0.059
**Analysis**: Q2 reveals different backbones. Although the heath_only items (10.6, 10.9, 5.19) all appear inside Heath's proof of 10.30 (which the AI cites), the AI does not merely cite 10.30 as a packaged version of Heath's inline work. The AI uses 10.30 to obtain generic lines with the required commensurability and excess properties, then employs a proportional scaling strategy (6.12, 5.16, 10.11, 6.22) and 10.14 to transfer those properties to lines matched to the assigned rational. This scaling-and-transfer approach, involving substantive propositions 10.30, 10.14, and 10.11 as a coordinated strategy, is entirely absent from Heath's proof, which constructs lines directly from numerical conditions using X.6 and X.9 without any proportional scaling. Since the AI introduces substantive intermediate steps not present in Heath's backbone, Case A fails and Q3 applies. The AI's different path is logically valid: every step is supported by cited propositions, with 10.14 correctly transferring the excess property through the established proportion, yielding classification D.

### 10.53
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decides the classification. Both proofs establish the same structural conclusions needed for a sixth binomial straight line (two rational lines commensurable in square only, binomial sum, both incommensurable with the assigned rational, square excess incommensurable with the greater term). However, the constructions are fundamentally different: Heath uses X.6 to produce lines from numbers with specific non-square-ratio properties and applies ratio manipulation (V.19 convertendo, V.22 ex aequali), while the AI constructs explicit mean proportionals via 6.13 giving a-squared equal to 3r-squared and b-squared equal to 2r-squared, then uses direct arithmetic computation and Book 7-8 number theory to establish the required incommensurabilities. The AI construction is a genuinely different path, not a higher-level subsumption of Heath steps but an entirely independent approach using different mathematical machinery (mean proportionals and specific numerical ratios vs. general number-theoretic ratios via X.6). The very low Jaccard similarity of 0.10 reflects this deep divergence. The AI proof is logically complete under the hardened 1(b) standard, so Q3 confirms it as a valid different path, yielding D.

### 10.54
**Category**: Granularity difference
**Jaccard**: 0.391
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: the parts of the first binomial (after bisection and rectangle application) are commensurable in length via 10.17; the constructed square-root lines are rational and commensurable in square; those lines are incommensurable in length; and their sum squares to the given area, making it binomial by 10.36. The ai_only citations (1.10, 2.1, 2.4, 5.11, 5.9, 6.28, CN2, D10.1.1-D10.1.4) are construction steps, algebraic identities, proportion basics, and definitions that Heath leaves implicit — standard over-citation. The AI substitutes 6.22 for Heath's 6.17 and uses an indirect argument via 10.12 instead of Heath's 10.13, but these sub-step variations reach the same intermediate conclusions. Case A of Q2 holds: same backbone, different citation depth.

### 10.55
**Category**: Granularity difference
**Jaccard**: 0.345
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: dividing the second binomial into its terms, bisecting the lesser term, applying a rectangle deficient by a square to get commensurable parts (via 10.17), constructing two lines whose squares equal the rectangles formed with the rational line, showing those lines are medial and commensurable in square only, demonstrating their product is a rational rectangle (via 10.19), and concluding the sum is a first bimedial (via 10.37). The AI uses algebraic notation (x, y, h, u, v) where Heath uses geometric labels (AG, GE, MN, NO), but every key intermediate conclusion maps one-to-one. The heath_only set is empty, meaning the AI cites every proposition Heath cites plus 19 additional references -- construction steps (1.10, 2.14, 6.28), algebraic identities (2.1, 2.4), proportion manipulations (5.11, 5.16, 6.16, 6.17, 6.22), commensurability lemmas (10.6, 10.9, 10.36), and definitions/common notions that Heath leaves implicit. This is a clear Case A: same backbone with the AI providing finer citation granularity.

### 10.56
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that the side of the area contained by a rational line and the third binomial consists of two medial straight lines commensurable in square only whose rectangle is medial, concluding it is a second bimedial by 10.38. Heath's proof is extremely condensed, referencing 'manner similar to the foregoing' (i.e., proofs of 10.54/10.55) for the bulk of the argument, and citing only 10.13, 10.21, 10.38, and Def. II.3. The AI proof works through every step explicitly, constructing u and v from scratch and citing 26 propositions at a much finer granularity. The heath_only set is empty, confirming that every Heath citation appears in the AI's set; the 22 ai_only citations are all foundational results (definitions, common notions, proportion theory, construction lemmas) that Heath subsumes under his terse 'similar to the foregoing' reference. This is Case A of Q2: same backbone, different citation depth.

### 10.57
**Category**: Granularity difference
**Jaccard**: 0.320
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish the defining properties of the fourth binomial, apply an area to obtain incommensurable parts (via 10.18), show the constructed lines are incommensurable in square (via 6.1 and 10.11), prove the sum of squares is rational (via 10.19), prove the rectangle is medial (via 10.13 and 10.21), and conclude by 10.39 that the whole is the major irrational. The heath_only set is empty, confirming the AI cites every reference Heath uses. The 17 ai_only items are all lower-level or auxiliary results (construction steps like 1.10 and 2.14, algebraic identities like 2.1 and 2.4, proportion lemmas like 5.11, 6.16, 6.17, 6.22, 6.28, the definition reference 10.36, definitions D10.1.1-D10.1.4, and common notions CN1-CN2) that Heath invokes implicitly. This is a clear case of over-citation at the same backbone, yielding a granularity difference.

### 10.58
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs establish the same three key intermediate conclusions before applying 10.40: (1) the two component lines are incommensurable in square, (2) the sum of their squares is medial, and (3) their rectangle is rational. Heath compresses the construction into 'the same construction as before shown' and cites only the main propositions at each logical step, while the AI spells out every construction step (1.10, 6.13, 6.28), algebraic identity (2.1, 2.4), proportion lemma (5.11, 5.16, 6.16, 6.17, 6.22), common notion (CN1, CN2), and definition (D10.1.1-D10.1.4, D10.2.4) explicitly. The empty heath_only set confirms that no element of Heath's reasoning is absent from the AI proof; the AI simply operates at finer citation granularity.

### 10.59
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions through the same logical backbone: (1) two lines incommensurable in square, (2) the sum of their squares is medial via 10.21, (3) their rectangle is medial via 10.21, (4) the sum of squares and rectangle are incommensurable via 6.1 and 10.11, and (5) the conclusion follows from 10.41. The AI proof uses algebraic notation (u, v, r, a, b) where Heath uses geometric labels (MN, NO, AK, EL), but the logical structure is identical. The large ai_only set (20 items) consists entirely of definitions, common notions, construction propositions, and foundational results that Heath implicitly uses but does not cite, particularly because Heath abbreviates the construction as 'the same construction as before shown.' The empty heath_only set confirms that the AI covers all of Heath's cited propositions. This is a clear Case A granularity difference: same backbone, different citation depth.

### 10.60
**Category**: Granularity difference
**Jaccard**: 0.360
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: (1) the sum of squares on the binomial terms is rational, so the corresponding breadth segment is rational and commensurable in length with the given rational line; (2) twice the rectangle of the terms is medial, so its breadth segment is rational and incommensurable in length with the given rational line; (3) these two breadth segments are incommensurable with each other and both rational, so their sum is binomial; (4) a mean proportional relation yields a commensurable partition enabling application of 10.17; (5) the sum of squares exceeds twice the rectangle, giving the needed inequality; (6) the resulting binomial satisfies the definition of first binomial. The citation differences are entirely at the level of auxiliary propositions: the AI uses 10.12 (transitivity of commensurability) where Heath uses 10.11 (proportional commensurability transfer), 6.16 (four-line rectangle equality) where Heath uses 6.17 (three-line version), and derives the mean-proportional lemma (cited by Heath as the Lemma after 10.53) directly from 6.1 and 5.11. The AI also over-cites foundational material (definitions D10.1.1-D10.1.4, algebraic identities 2.1/2.4/2.7, CN5). All differences are citation-depth substitutions with no change to the logical backbone.

### 10.61
**Category**: Granularity difference
**Jaccard**: 0.310
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: the first bimedial decomposition yields a breadth with two rational terms, one commensurable and one incommensurable with the given rational line, commensurable in square only (hence binomial via 10.36), with the greater term's square exceeding the lesser's by a square on a commensurable line, and the lesser term commensurable with the rational line (hence second binomial via D10.2.2). The heath_only citations (10.17, 10.21, 10.23) are all re-derived by the AI at lower granularity: 10.17's criterion for excess by a commensurable square is established through explicit algebraic steps using 2.7, proportion theory (5.11, 6.16), and the relation pq = t^2; 10.21 and 10.23 are bypassed because the AI works directly with fourth proportionals rather than through mediality of areas. The large ai_only set consists of definitions, common notions, algebraic identities, and proportion theory that support the same logical backbone at finer detail. This is Case A: same backbone, different citation depth.

### 10.62
**Category**: Granularity difference
**Jaccard**: 0.409
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: the breadth of the applied rectangle decomposes into two rational segments each incommensurable in length with the given rational line, those two segments are mutually incommensurable in length, hence the breadth is binomial (10.36), and the square on the greater exceeds the square on the lesser by the square on a line commensurable with the greater while neither segment is commensurable with the rational line, yielding the third binomial (Def. 10.2.3). The single heath_only item 10.23 (Porism) is used by Heath to conclude that the sum of squares on the medial components is medial; the AI unpacks this same fact through its constituent results (10.15, 10.6, 10.9, 10.12). The twelve ai_only items are all over-citations of definitions (D10.1.1, D10.1.2, D10.1.3, D10.2.1), elementary arithmetic identities (2.1, 2.4, 2.5), proportionality results (6.12, 6.16), and commensurability sub-steps (10.6, 10.9, 10.17) that Heath leaves implicit or compresses. The logical backbone is identical, so Case A of Q2 holds and the classification is G.

### 10.63
**Category**: Granularity difference
**Jaccard**: 0.409
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: the greater term (DM/x) is rational and commensurable in length with the given rational line (via 10.20), the lesser term (MG/y) is rational and incommensurable in length with it (via 10.22 and 10.13), the two terms are commensurable in square only so their sum is binomial (via 10.36), the greater term exceeds the lesser, the sub-segments of the application are incommensurable (via 6.1 and 10.11), and by 10.18 the square on the greater exceeds the square on the lesser by a square incommensurable with the greater, yielding the fourth binomial classification (D10.2.4). The AI proof cites all nine of Heath's references plus thirteen additional items -- definitions (D10.1.1-D10.1.4), common notions (CN5), algebraic identities (2.1, 2.4, 2.7), proportion results (5.11, 5.14), and construction propositions (6.12, 6.16, 10.12) -- all of which are foundational results Heath applies implicitly. The empty heath_only set confirms the AI omits nothing Heath cites. This is a clear Case A: same logical backbone with the AI providing finer citation granularity.

### 10.64
**Category**: Granularity difference
**Jaccard**: 0.261
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decompose via 10.40, show the sum-of-squares component is rational and incommensurable with the given line (10.22), show the rectangle component is rational and commensurable with it (10.20), derive their mutual incommensurability (10.13), conclude binomial (10.36), and verify the fifth binomial conditions via 10.18. heath_only is empty, meaning every proposition Heath cites also appears in the AI citation set. The 17 ai_only items are all over-citations at lower levels of granularity: definitions (D2.1, D10.1.1-4, D10.2.4-5), a common notion (CN5), construction and proportion propositions (6.1, 6.12, 6.16, 5.11), algebraic identities (2.1, 2.4, 2.7), and commensurability transfer results (10.11, 10.12). This is Case A of Q2: same backbone, different citation depth.

### 10.65
**Category**: Granularity difference
**Jaccard**: 0.238
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: starting from the X.41 properties of the side of the sum of two medial areas, they apply the resulting medial rectangles to a rational straight line, show the resulting lines are rational and incommensurable in length with that rational line (X.22), establish that they are commensurable in square only and hence form a binomial (X.36), and then verify the three sixth binomial conditions. The heath_only set is empty, meaning every Heath citation appears in the AI set. The 16 ai_only items are all finer-grained references: definitions (D10.1.1, D10.1.2, D10.1.3, D10.2.6, D5.5), common notions (CN5), algebraic identities (2.1, 2.4, 2.7), and auxiliary propositions (5.11, 6.12, 6.16, 6.17, 10.12, 10.13, 10.18) that Heath either subsumes or leaves implicit. This is a clear Case A under Q2: same backbone, different citation depth.

### 10.66
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: dividing the commensurable line proportionally to match the binomial's terms, showing each new term is commensurable in length with the corresponding original term, establishing that the new terms are rational and commensurable in square only (hence the sum is binomial), and then systematically verifying that both the length-commensurability condition and the excess-square condition are preserved across all six binomial orders. The citation differences are entirely in which Book 5/6 proportion lemmas are used for the proportional construction (AI uses 6.10, 5.12, 5.14 where Heath uses 6.12, 5.19, 5.11) and in the AI's additional explicit citation of definitions (D10.1.2, D10.1.3) and lower-level commensurability results (10.6, 10.9). Since the key conclusions and their logical positions are identical, this is a citation-depth difference, not a path difference.

### 10.67
**Category**: Path difference
**Jaccard**: 0.059
**Analysis**: Q2 decided this classification. Heath's proof works by directly dividing the bimedial into its medial components and showing the corresponding parts of CD inherit mediality and commensurability in square only, then comparing rectangles for same-order determination using Book V proportions (5.11, 5.16, 5.19) and Book X mediality results (10.23, 10.37, 10.38). The AI proof takes an entirely different route: it applies the squares of L and M to a rational straight line r, producing breadths x and y, then converts the bimedial classification into a binomial classification of these breadths (10.61, 10.62), uses the binomial order-preservation theorem (10.66) to show y has the same binomial order as x, and finally extracts the bimedial classification of M from the binomial classification of y (10.55, 10.56). The two backbones share essentially no intermediate conclusions, with a Jaccard similarity of only 0.059 and only one shared citation (10.11). The AI's application-of-areas method is logically complete and valid, producing a genuine path difference.

### 10.68
**Category**: Path difference
**Jaccard**: 0.062
**Analysis**: Q2 decides the classification. Heath proves the proposition by directly dividing both lines proportionally and transferring the rationality of the sum of squares and the mediality of the rectangle through ratio manipulations (V.11, V.16, V.18, VI.20, X.23, X.39). The AI takes an entirely different route: it applies the squares of both lines to a rational straight line, shows the breadth for A is a fourth binomial (10.63), transfers the binomial order to B's breadth via commensurability in length (10.66), and concludes B is major because the side of a rectangle contained by a rational line and a fourth binomial is major (10.57). The two proofs share only 10.11 out of their combined citation sets (Jaccard 0.062), and their key intermediate conclusions are completely different: Heath works with the parts of the major line and their commensurability properties, while the AI works with binomial characterizations obtained through area application. This is a genuine path difference with a valid alternative proof.

### 10.69
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 10.69 by direct construction: dividing the commensurable line at a corresponding point and showing that its parts satisfy the definition from 10.40 (sum of squares medial, rectangle rational). The AI takes an entirely different route through binomial classification theory: it applies the squares of both lines to a rational line r via fourth proportionals (6.12, 6.17), identifies the resulting breadth u as a fifth binomial (10.64), shows u and v are commensurable in length (10.9, 10.6, 6.1, 10.11), concludes v is also a fifth binomial (10.66), and then applies 10.58 to recover that y is the side of a rational plus a medial area. The key intermediate conclusions are completely different: Heath works with incommensurability of parts and commensurability of sums-of-squares and rectangles, while the AI works with binomial orders of breadths and application-of-areas machinery. The Jaccard similarity is 0.0, reflecting zero overlap in citations. The AI proof is logically complete with every step justified by a cited proposition, so no E was considered.

### 10.70
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works by direct construction: dividing AB at E, showing AE and EB satisfy the conditions of 10.41 (incommensurable in square, medial sum of squares, medial rectangle, sum incommensurable with rectangle), then transferring these properties to CF and FD via commensurability. The AI proof takes an entirely different route through binomial representations: it applies the squares on a and b to a rational straight line r to obtain breadths x and y (6.12, 6.17), identifies x as a sixth binomial via 10.65, shows y is commensurable in length with x (6.1, 10.11) and therefore also a sixth binomial (10.66), then invokes 10.59 to conclude that b is the side of the sum of two medial areas. The two backbones share no key intermediate conclusions, establishing Case B (different backbone). Under Q3 the AI's path is logically complete: every step is properly cited with sound inferences from premise to conclusion, so the classification is D.

### 10.71
**Category**: Granularity difference
**Jaccard**: 0.407
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: they apply the rational and medial areas to a rational line to obtain two breadths that are rational and commensurable in square only, conclude the sum is a binomial (10.36), then split into four exhaustive sub-cases based on which breadth is greater and whether the excess square is commensurable or incommensurable, yielding binomial (10.54), first bimedial (10.55), major (10.57), and side of rational plus medial (10.58). The AI reaches the incommensurability of the two breadths through a contradiction argument using 10.12 (transitivity of commensurability) rather than Heath's proportion-based route via 6.1 and 10.11, but both arrive at the same key intermediate conclusion. The large ai_only set consists of over-cited construction steps (2.1, 2.14, 6.12, 6.17), definitions (D10.1.1, D10.1.2, D10.1.3), and an additional realizability argument in Step 8 citing 10.19, 10.21, 10.48, 10.49, 10.51, 10.52. These are citation-depth differences, not backbone differences, so the classification is G.

### 10.72
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: apply two incommensurable medial areas to a rational straight line to obtain rational breadths incommensurable with it (10.22), show the breadths are incommensurable with each other (6.1, 10.11), conclude their sum is binomial (10.36), then split into two cases based on whether the excess of squares is commensurable or incommensurable with the greater term, yielding a third binomial and second bimedial (D10.2.3, 10.56) or a sixth binomial and side of the sum of two medial areas (D10.2.6, 10.59). The AI proof cites all of Heath's references plus six additional items (10.12, 2.1, 2.14, D10.1.1, D10.1.2, D10.1.3) that are definitions and construction propositions Heath leaves implicit, and heath_only is empty. This is a pure over-citation pattern with identical key intermediate conclusions, making it a granularity difference.

### 10.73
**Category**: Path difference
**Jaccard**: 0.083
**Analysis**: Q2 decided the classification. Heath proves the irrationality of the remainder directly by manipulating squares and rectangles: using the proportionality transfer (10.11) to establish incommensurability between sq(AB) and rect(AB,BC), the algebraic identity sq(AB)+sq(BC) = 2*rect(AB,BC)+sq(AC) from II.7, and commensurability/incommensurability propagation rules (10.6, 10.13, 10.16) to conclude sq(AC) is incommensurable with the rational sum sq(AB)+sq(BC). The AI instead uses proof by contradiction: it assumes the remainder CB is rational, derives that AC and CB are commensurable in square only (via 10.12 and definitions), then invokes the previously proved 10.36 (the binomial theorem) to conclude their sum AB would be irrational, contradicting the hypothesis. These are fundamentally different proof strategies with entirely different key intermediate conclusions -- Heath's direct area-based argument versus the AI's indirect reduction to 10.36. The Jaccard similarity of 0.083 (only 10.15 in common) reflects this deep structural divergence. The AI proof is logically valid and complete, so the classification is D.

### 10.74
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: they establish that the squares on the two medial lines are medial (hence incommensurable with the rational reference), that twice the rectangle is rational, apply the II.7 identity to connect the sum of squares with twice the rectangle and the square on the remainder, then use X.16 to conclude the square on the remainder is incommensurable with the rational quantity, and hence irrational. The AI proof spells out each intermediate commensurability and incommensurability step with explicit citations (10.12 for transitivity of commensurability, 10.13 for mixed transitivity, 10.15 for sums of commensurable magnitudes, 10.21 for the rationality characterization, and definitions D10.1.1 and D10.1.2), whereas Heath applies these results implicitly. The empty heath_only set confirms the AI cites everything Heath does and more. This is a same-backbone, different-depth scenario, yielding G.

### 10.75
**Category**: Path difference
**Jaccard**: 0.176
**Analysis**: The AI proof takes a fundamentally different path from Heath. Heath applies the areas a^2+b^2 and 2ab to a rational line DI, shows the resulting breadths DG and DF are rational and incommensurable with DI, proves they are incommensurable with each other via X.11/X.15/X.6/X.13, concludes FG is an apotome by X.73, and derives irrationality from X.20. The AI instead shows both S=a^2+b^2 and 2R=2ab are medial areas, then directly invokes 10.26 (a medial area does not exceed a medial area by a rational area) to conclude c^2=S-2R is irrational, hence c is irrational. The AI never constructs a rational line, never applies areas, never forms an apotome, and never uses X.73 or the many intermediate commensurability results Heath requires. This is a genuinely different and valid proof strategy, decided at Q2 (different backbone) and confirmed valid at Q3.

### 10.76
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) the sum of squares on AB and BC is rational while twice the rectangle is medial, making them incommensurable; (2) by II.7 and X.16 (convertendo), the sum of squares is incommensurable with the square on AC; (3) since the sum of squares is rational, the square on AC is irrational and therefore AC is irrational. The AI's additional citations (10.13 for transitivity of incommensurability, 10.21 for medial-implies-irrational, and definitions D10.1.1 and D10.1.4) make explicit what Heath leaves implicit, representing over-citation at finer granularity. Heath's sole extra citation, 10.33, is a construction cross-reference for the existence of lines satisfying the hypothesis, not a deductive step in the proof chain. Since the backbones match and all citation differences reflect depth rather than path, this is a granularity difference.

### 10.77
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) the sum of squares on AB and BC is incommensurable with twice the rectangle AB,BC because the former is medial and the latter rational; (2) by II.7 the sum of squares equals twice the rectangle plus the square on AC, so by X.16 the square on AC is incommensurable with twice the rectangle; (3) since twice the rectangle is rational, the square on AC is irrational and AC is irrational. The AI adds lower-level citations (10.13 for transitivity of incommensurability, 10.21 for the definition of medial, D10.1.4 for definitions) that Heath handles implicitly, while Heath cites 10.34 as a setup reference for the existence of lines satisfying the conditions. These are citation-depth differences, not structural divergences, so the classification is G.

### 10.78
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: The forward dependency gate is clear (all AI citations precede 10.78). Q1 finds no logical defect: the AI correctly invokes 10.26, which states that a medial area does not exceed a medial area by a rational area, and applies it to the hypothesis that both S (sum of squares on AB, BC) and T (twice the rectangle AB, BC) are medial; since S = T + square on AC by 2.7, and S > T by CN5, the square on AC equals S minus T and is therefore not rational, hence irrational, making AC irrational. At Q2, the proofs have fundamentally different backbones: Heath constructs auxiliary rectangles on a rational line DI, establishes that DG and DF are rational and incommensurable in length with DI (via 10.22), uses 6.1 and 10.11 to show DG incommensurable with DF, concludes FG is an apotome (10.73), and deduces irrationality from the rectangle of a rational line and an apotome (deduction from 10.20); the AI instead directly applies 10.26 to the two medial areas to conclude their difference is not rational. Since the key intermediates differ entirely (apotome construction vs. direct application of 10.26), this is Case B (different backbone). Q3 confirms the AI path is logically complete: the chain runs from premises through 10.26 to the conclusion without gaps, yielding classification D.

### 10.79
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification. Both proofs use the same contradiction strategy: they set up two representations of the apotome from rational lines commensurable in square only, apply II.7/2.7 to express the sums of squares in terms of the rectangles, show the difference of rectangle areas must be rational (since the sums of squares are rational), then invoke X.21 to establish both rectangles are medial and X.26 to derive the contradiction that a medial area cannot exceed a medial by a rational area. The logical backbones are identical. The AI proof explicitly cites definitions (D10.1.1-D10.1.4), common notions (CN2, CN3, CN5), and intermediate commensurability results (10.12, 10.15) plus 2.1 for rectangle computation, all of which Heath uses implicitly without citation. Since heath_only is empty, the AI covers every step Heath uses, and the ai_only items are all foundational or supporting citations, this is a clear Case A granularity difference.

### 10.80
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction, assuming two valid annexes to a first apotome of a medial straight line. Both establish the same key intermediate conclusions: (1) the sums of squares on each pair of whole-and-annex are medial areas, (2) by II.7, the difference of these medial areas equals the difference of twice the rational rectangles, which is rational, (3) this contradicts X.26 (a medial area cannot exceed a medial by a rational area). The AI proof takes a more elaborate route through Book 6 proportions (6.1, 6.12, 6.17) and additional Book 10 commensurability results (10.11, 10.12, 10.24) to establish that the sums of squares are medial, whereas Heath invokes X.15 and X.23 more directly. The AI also explicitly cites definitions (D10.1.1, D10.1.2, D10.1.4), common notions (CN2, CN3, CN5), and 2.1, all of which Heath leaves implicit. Since heath_only is empty and all ai_only items represent additional citation depth for the same logical backbone, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 10.81
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they assume two annexes to a second apotome of a medial straight line, apply the relevant areas (squares and double-rectangles) to a rational line, show the resulting breadths are rational and incommensurable in length with the rational line via 10.22, establish that the two breadths are incommensurable in length with each other through the chain involving 10.11 and 10.13, conclude that an apotome is formed via 10.73 with the breadths as rational annexes commensurable in square only, and invoke 10.79 for the uniqueness contradiction. The citation differences are all at the granularity level: the AI over-cites definitions (D10.1.1-3), common notions (CN4, CN5), and basic construction and proportion propositions (6.12, 6.16, 2.1, 10.9, 10.12), while Heath's sole unique citation 10.23 (a line commensurable with a medial line is medial) is functionally replaced by the AI's use of 10.21 and 10.22 to reach the same intermediate conclusion. This is Case A of Q2: same backbone, different citation depth.

### 10.82
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs employ the same contradiction strategy for uniqueness of the annex to a minor straight line: they assume two distinct annexes, show the difference of the two rational square-sums is itself rational, establish that this rational difference equals the difference of the two medial double-rectangles, and then invoke 10.26 to obtain a contradiction (a medial area cannot exceed a medial area by a rational area). The AI proof elaborates every implicit step Heath takes for granted: it uses 2.7 to derive the algebraic identity equating the square-sum difference with the double-rectangle difference, invokes 10.12 and 10.15 to justify that the difference of two rational areas is rational, and adds a Step 2 proving 2ab is medial via 10.21, 10.23, and 10.24 (a fact already given by the definition in 10.76). The empty heath_only set confirms that Heath uses no proposition the AI omits. All 14 ai_only items are definitions, common notions, algebraic identities, or commensurability lemmas that fill in steps Heath leaves implicit, making this a clear Case A granularity difference.

### 10.83
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs establish uniqueness of the annex by contradiction: they assume a second annex exists satisfying the conditions of X.77, show that the difference of the two medial sums-of-squares equals the difference of the two rational twice-rectangles, conclude that difference is rational, and invoke X.26 to derive a contradiction (a medial area cannot exceed a medial area by a rational amount). The logical backbones are identical. The AI proof cites additional intermediate steps that Heath leaves implicit: II.7 for the algebraic identity expressing each sum-of-squares in terms of the twice-rectangle and the square on a, propositions 10.12 and 10.15 for the commensurability reasoning showing the difference of rational areas is rational, common notions CN2/CN3/CN5 for arithmetic comparisons, and definition D10.1.4 for rationality. Since heath_only is empty, every Heath citation appears in the AI set. This is a clear case of same backbone at different citation depth, yielding G.

### 10.84
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume two annexes exist (10.78), apply II.7 to express the square on the given line, apply the resulting medial areas to a rational straight line to obtain rational breadths (10.22), show those breadths are incommensurable in length via VI.1 and X.11, conclude they are rational and commensurable in square only so the difference is an apotome (10.73), then invoke uniqueness of the annex (10.79) for the contradiction. The AI's extra citations (1.44, 10.12, 2.1, CN4, CN5, D10.1.2, D10.1.3) are all construction steps, transitivity lemmas, common notions, and definitions that Heath invokes implicitly. Since heath_only is empty and all ai_only items are sub-step-level citations, Q2 Case A applies: same backbone, different citation depth.

### 10.85
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs establish the same key geometric facts: two rational straight lines commensurable in square only whose difference is an apotome, with the square on the greater exceeding the square on the lesser by the square on a line commensurable in length with the greater, and the greater commensurable in length with the assigned rational line, thereby satisfying the definition of a first apotome. The AI achieves this by invoking 10.48 (to find the first binomial) as a packaged unit and then subtracting one term from the other via 10.73, while Heath re-derives the same construction inline using 10.6, 10.9, and 5.19. The proof-tree containment test confirms that all three heath_only propositions (10.6, 10.9, 5.19) appear inside Heath's proof of 10.48, so the AI is citing at a higher level of granularity rather than taking a genuinely different path.

### 10.86
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decides the classification. Heath constructs the second apotome directly from scratch by setting out square numbers with a non-square difference, using 10.6 to arrange ratios, 10.9 to establish commensurability and incommensurability in length, and 5.19 (convertendo) to show the excess is by a commensurable line. The AI takes a fundamentally different route: it invokes 10.49 to construct a second binomial, extracts the properties of its terms from the binomial definitions (D10.2.1, D10.2.2), then subtracts the lesser term from the greater using 1.3 to form an apotome via 10.73, and verifies the second apotome conditions via D10.3.2. Although the heath_only items (10.6, 10.9, 5.19) do appear inside Heath's proof of 10.49, the AI is not merely compressing the same construction at a higher level; it is constructing a different intermediate object (a binomial rather than directly building the apotome) and converting it, which constitutes a genuinely different proof backbone. The AI's chain is logically complete and valid, so Q3 confirms path difference D.

### 10.87
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Heath directly constructs a third apotome from scratch using number ratios with specific properties, establishing commensurability and incommensurability through 10.6, 10.9, and proportion results 5.22 (ex aequali) and 5.19 (convertendo). The AI takes a genuinely different path: it first constructs a third binomial via 10.50, identifies the binomial's terms as rational straight lines commensurable in square only (via 10.36 and definitions D10.2.1, D10.2.3), then subtracts the lesser term from the greater (1.3) to produce an apotome (10.73), and finally classifies it as a third apotome by D10.3.3. Although all four heath_only items (10.6, 10.9, 5.19, 5.22) appear in Heath's proof of 10.50, the containment test does not apply because 10.50 constructs a third binomial, not a third apotome — these are different objects, and the AI's strategy of constructing a binomial and converting it to an apotome by subtraction constitutes a genuinely different logical backbone from Heath's direct construction. The AI's path is valid at Q3: each step is properly supported by citations and the inference chain is sound.

### 10.88
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Heath constructs the fourth apotome directly using number ratios and proportions (10.6, 10.9, 5.19) to establish two rational lines commensurable in square only with the required square-excess property. The AI takes a fundamentally different path: it first constructs a fourth binomial via 10.51, then observes that the same pair of terms, when subtracted rather than added, yield a fourth apotome. The key intermediate conclusion 'we have a fourth binomial' appears only in the AI proof and has no counterpart in Heath's proof, making the backbone different (Q2 Case B). Under Q3, the AI's path is logically sound: the definitional conditions for a fourth binomial (D10.2.4) and fourth apotome (D10.3.4) impose the same requirements on the terms (whole commensurable in length with the rational, square excess incommensurable with the whole), so constructing the binomial and then forming the apotome from its terms is a valid chain from premises to conclusion.

### 10.89
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: two rational lines commensurable in square only, their difference is an apotome (via 10.73), the square on the whole exceeds the square on the annex by a square incommensurable with the whole, and the annex is commensurable with the assigned rational line. The difference lies in citation depth. Heath constructs directly from number ratios, using 10.6 (commensurability from number ratios), 10.9 (incommensurability from non-square ratios), and 5.19 (convertendo) to build up the required properties step by step. The AI instead cites 10.52 (construction of a fifth binomial) as a unit, then derives the fifth apotome from the binomial's definitional properties. The proof-tree containment test confirms this is a citation-depth difference: all three heath_only items (10.6, 10.9, 5.19) appear inside Heath's proof of 10.52, meaning the AI cites the higher-level result while Heath re-derives its internals inline.

### 10.90
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification. Both proofs establish the same key intermediate conclusions: the two terms are rational and commensurable in square only, neither is commensurable in length with the given rational line, and the square on the whole exceeds the square on the annex by the square on a line incommensurable with the whole. Heath derives these properties from scratch using number-ratio constructions with 10.6, 10.9, 5.22, and 5.19, while the AI obtains them by citing 10.53 (sixth binomial construction) as a unit and extracting the properties from the binomial definitions (D10.2.4, D10.2.6). The proof-tree containment test confirms the granularity diagnosis: all four heath_only items (10.6, 10.9, 5.19, 5.22) appear inside Heath's proof of 10.53, so the AI is packaging Heath's inline derivation into a single higher-level citation. The backbone is the same; only the citation depth differs.

### 10.91
**Category**: Path difference
**Jaccard**: 0.310
**Analysis**: Q2 decided the classification. Heath's proof uses a geometric gnomon construction: it builds squares LM and NO about the same diameter (6.26), establishes that certain rectangles are medial (10.21, 10.13), and applies the mean proportional lemma after 10.53 to show MN equals EK, ultimately deriving the side LN via a gnomon argument. The AI instead constructs explicit square roots u and v with u-squared equal to rx and v-squared equal to ry (using 2.14), establishes proportional relationships via 6.22, proves uv equals rh through 6.16 and 6.17, shows u and v are incommensurable by contradiction, and then uses the algebraic identity from 2.7 to derive w-squared equals r times the apotome a minus b. These represent genuinely different constructive strategies with different key intermediate conclusions, explaining the low Jaccard similarity of 0.31 and the substantial symmetric difference in citations. The AI's path is logically complete and valid, so the classification is D.

### 10.92
**Category**: Granularity difference
**Jaccard**: 0.367
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: decomposing the second apotome via 10.73, bisecting the annex and applying the rectangle construction of 10.17 to obtain commensurable parts, establishing those parts as rational and incommensurable with the given rational line, showing the resulting rectangular areas are medial (10.21) and the constructed side-lengths are medial lines commensurable in square, proving their product is a rational area, establishing their incommensurability in length, deriving that the square on their difference equals the given area, and concluding via 10.74 that the difference is a first apotome of a medial straight line. The AI replaces Heath's geometric square construction (6.26) and mean proportional argument (6.17) with an algebraic proportion chain using 6.22, 6.16, and 6.1 to reach the same intermediate conclusion that xy is rational. The large ai_only set consists primarily of over-cited definitions (D10.1.1-D10.1.4), common notions (CN3), foundational arithmetic propositions (2.1, 2.4, 2.7, 2.14), and commensurability lemmas (10.6, 10.9, 10.12), reflecting greater citation granularity rather than a different logical path.

### 10.93
**Category**: Granularity difference
**Jaccard**: 0.310
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decomposing the third apotome via bisection of the annex and parallelogram application to obtain commensurable segments, showing the resulting rectangles are medial, establishing that the constructed lines are medial and commensurable in square only while containing a medial rectangle, concluding via 10.75 that the result is a second apotome of a medial straight line, and verifying the square equals the given area. The heath_only items (6.17 and 6.26) reflect Heath's geometric gnomon construction approach: 6.17 converts a rectangle-square equality into a proportion, while 6.26 establishes that parallelograms share a diameter. The AI replaces these with algebraic equivalents (6.1 for proportions, 2.7 for algebraic expansion), arriving at the same conclusions. The large ai_only set consists of over-cited foundational results (definitions D10.1.1-D10.1.4, common notions CN3/CN5, algebraic propositions 2.1/2.4/2.7/2.14, and commensurability lemmas 10.6/10.9/10.12) plus 10.73 which characterizes the third apotome explicitly rather than citing D10.3.3 alone. This is Case A of Q2: same backbone, different citation depth.

### 10.94
**Category**: Granularity difference
**Jaccard**: 0.360
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: decompose the fourth apotome using 10.18 to get incommensurable segments, show the sum of corresponding squares is rational (10.19), the product or double rectangle is medial (10.21), and the squares are incommensurable (6.1, 10.11), then apply 10.76 to conclude the side is minor. The AI proof adds explicit citations for definitions (D10.1.1-D10.1.4), common notions (CN3), algebraic identities (2.1, 2.4, 2.7), construction propositions (1.10, 2.14, 6.28), and intermediate commensurability results (10.12, 10.13, 10.73) that Heath invokes implicitly. The sole heath_only citation (6.26, squares about same diameter) is a geometric construction step that the AI replaces with algebraic notation while reaching the same conclusions. This is a citation-depth difference, not a path difference.

### 10.95
**Category**: Path difference
**Jaccard**: 0.190
**Analysis**: Q2 decided the classification. Heath proves 10.95 by direct geometric construction: applying 10.18 to divide a segment into incommensurable parts, constructing squares about a common diameter via 6.26, and showing the resulting side has the required properties via 10.77. The AI instead uses a fundamentally different algebraic strategy: it forms the sum a+b (identifying it as a fifth binomial via 10.36 and D10.2.5), obtains the side x+y of r(a+b) via 10.58/10.40, then proves that x^2+y^2 equals the medial area ra and 2xy equals the rational area rb using 10.26 (a medial area cannot exceed a medial area by a rational area), and finally derives (x-y)^2 = r(a-b) by the algebraic identity from 2.7. The two proofs share only the final step citing 10.77, while their intermediate conclusions and methods are entirely different. The AI's path is logically sound with every step properly supported by cited propositions, so this is a valid path difference rather than an error.

### 10.96
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same logical order: (1) the parts from bisection and application of areas are incommensurable via 10.18, (2) the rectangle on the rational line and the whole is medial via 10.21, (3) the rectangle on the rational line and the annex is medial via 10.21, (4) these two rectangles are incommensurable, (5) the component squares are incommensurable, and (6) the side satisfies the conditions of 10.78. The AI's 15 ai_only citations are overwhelmingly over-citations: construction props (1.10, 6.28), algebraic identities (2.1, 2.7, 2.14), proportion lemmas (5.9, 5.11, 6.22), definitions (D10.1.2, D10.1.3, D10.3.4), common notions (CN2, CN3), and intermediate Book 10 results (10.12, 10.73) that Heath leaves implicit or compresses via 'in manner similar to the above.' The sole heath_only item 6.26 reflects a construction technique difference (geometric square construction vs. algebraic extraction) rather than a backbone divergence. Same backbone, different citation depth yields G.

### 10.97
**Category**: Granularity difference
**Jaccard**: 0.292
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: decomposing the apotome via 10.73, showing the sum-of-squares breadth is rational and commensurable with the rational line (10.20), showing the double-rectangle breadth is rational and incommensurable with it, establishing the two breadths are incommensurable with each other, concluding the result is an apotome (10.73), then applying 10.17 to establish the first apotome condition. The two heath_only citations (10.22, 6.17) are accounted for by citation-depth differences: the AI establishes 10.22's conclusion through more granular sub-steps (10.19, 10.13, 10.11) at the same logical position, and uses 6.16 in place of its direct corollary 6.17. The large ai_only set consists entirely of definitions, common notions, transitivity lemmas, and sub-propositions that Heath leaves implicit. Case A of Q2 holds, yielding G.

### 10.98
**Category**: Granularity difference
**Jaccard**: 0.423
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decomposing the first apotome of a medial straight line via 10.74, applying the resulting squares and rectangles to a rational line, showing the two breadth components are rational and commensurable in square only (yielding an apotome by 10.73), using the algebraic identity II.7 for the remainder, establishing a continuous proportion to obtain the fourth-part-of-square condition, applying 10.17 for the square excess, and concluding second apotome via D10.3.2. The ai_only set consists entirely of over-citations: definitions (D10.1.1-4, D2.1), common notions (CN3, CN5), and lower-level construction or commensurability lemmas (6.12, 6.16, 10.12, 10.13, 2.1, 2.4). The heath_only citations 10.23 (medial commensurability) and 5.11 (proportion transitivity) correspond to intermediate steps that the AI handles through equivalent alternative citations (10.15 plus definitions for 10.23; 6.1 and 6.17 for 5.11). Since the key intermediate conclusions are identical and only citation depth differs, this is Case A of Q2, yielding granularity difference.

### 10.99
**Category**: Granularity difference
**Jaccard**: 0.458
**Analysis**: Both proofs follow the same logical backbone: decomposing the second apotome of a medial straight line via 10.75, applying squares and rectangles to a rational line to obtain breadths, showing these breadths are rational and commensurable in square only (hence forming an apotome via 10.73), then verifying the deficient-rectangle criterion of 10.17 to classify the result as a third apotome (D10.3.3). The classification is decided at Q2 (Case A): the proofs share the same key intermediate conclusions with differences only in citation depth. The AI's 12 extra citations are definitions (D10.1.1, D10.1.2, D10.1.3), common notions (CN3, CN5), construction propositions (6.12, 6.16), and supporting commensurability lemmas (10.6, 10.9, 10.12, 2.1, 2.4) that Heath uses implicitly. Heath's sole extra citation, 10.23 (a line commensurable with a medial line is medial), reflects an intermediate step where Heath establishes the mediality of the sum-of-squares area before deriving the breadth, while the AI works directly with the breadths, bypassing this step but reaching the same key result.

### 10.100
**Category**: Path difference
**Jaccard**: 0.259
**Analysis**: The proofs share the same initial structure: decomposing the minor via 10.76, establishing that U (or CM) is rational and commensurable with the rational line (10.20), and that V (or FM) is rational and incommensurable with it (10.22), then concluding the breadth is an apotome (10.73). However, they diverge fundamentally on how they establish that the apotome is specifically a fourth apotome. Heath directly constructs the mean proportional relationship (6.17) and applies 10.18 to show the square-excess is incommensurable. The AI instead leverages the binomial-apotome duality: it shows a+b is major (10.39), applies 10.63 to get that U+V is a fourth binomial, then uses the uniqueness of binomial division (10.42) to transfer the square-excess property from the fourth binomial definition (D10.2.4). This indirect transfer argument through binomials constitutes a genuinely different logical backbone from Heath's direct computation, resolved at Q2 as Case B and confirmed valid at Q3, yielding classification D.

### 10.101
**Category**: Granularity difference
**Jaccard**: 0.450
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: decompose the given irrational line via X.77, apply the squares and twice-the-rectangle to a rational line, show one breadth is rational and incommensurable (X.22) while the other is rational and commensurable (X.20), conclude an apotome (X.73), establish incommensurability of the two parts of the whole, show the product of those parts equals one-fourth the annex squared, apply X.18 to derive the excess-square incommensurability, and conclude fifth apotome by Def. X.III.5. The AI proof uses algebraic notation with fourth proportionals but reaches every key intermediate conclusion at the same logical position as Heath. The eleven ai_only citations (10.12, 10.13, 2.1, 2.4, 5.11, 6.12, 6.16, CN3, CN5, D10.1.2, D10.1.3) are all definitions, common notions, construction sub-steps, or commensurability-transitivity lemmas that Heath invokes implicitly. heath_only is empty, confirming the AI cites everything Heath does plus additional sub-steps. This is a clear Case A granularity difference.

### 10.102
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decomposition via X.78, application of areas to a rational line to obtain rational breadths incommensurable with it (X.22), showing those breadths are incommensurable with each other and hence form an apotome (X.73), establishing the mean proportional relationship among the sub-breadths, applying X.18 to determine the square-excess condition, and concluding sixth apotome by definition D10.3.6. The heath_only set is empty, meaning every citation Heath uses also appears in the AI's set. The eight ai_only items (1.44, 10.12, 2.1, 2.4, 6.17, CN3, D10.1.2, D10.1.3) are all construction propositions, auxiliary commensurability results, algebraic identities, definitions, and common notions that make explicit steps Heath leaves implicit. This is a clear Case A under Q2: same backbone, different citation depth.

### 10.103
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: decompose the apotome into rational components commensurable in square only (10.73), construct proportional counterparts for the commensurable line (6.12, 5.12), transfer commensurability to the components (10.11), establish the new components are rational commensurable in square only (10.13), use alternation to relate the ratios (5.16), transfer the square-difference condition via 10.14, and transfer the order-determining commensurability status via 10.12 and 10.13. The heath_only set is empty, meaning the AI cites every proposition Heath cites. The ai_only set consists of two subsidiary propositions (10.6, 10.9) that the AI uses to elaborate how the new components inherit rationality, plus eight definitions (D10.1.2, D10.1.3, D10.3.1-D10.3.6) that Heath leaves implicit. This is classic over-citation with the same key intermediate conclusions, placing it squarely in Case A of Q2 as a granularity difference.

### 10.104
**Category**: Path difference
**Jaccard**: 0.105
**Analysis**: The AI proof takes a fundamentally different path from Heath's. Heath works directly with the annex decomposition: he constructs a proportional so that AB:CD = BE:DF, shows the parts CF and FD are medial and commensurable in square only (using 10.23, 10.13), and then compares the rectangles AE*EB and CF*FD to determine same order. The AI instead uses an application-of-areas technique: it applies the squares on a and b to a rational line r, obtaining breadths c and d that are commensurable in length, then converts from apotome-of-medial types to ordinary apotome types via 10.98/10.99, transfers the order via 10.103, and converts back via 10.92/10.93. The key intermediate conclusions are entirely different -- Heath's backbone involves the annex pair being medial and commensurable in square only, while the AI's backbone involves ordinary apotomes as intermediaries. The AI's path is logically sound: each step is correctly supported by its cited propositions, and both cases (first and second apotome of medial) are explicitly addressed. Q2 identifies Case B (different backbone), and Q3 confirms validity, yielding D.

### 10.105
**Category**: Path difference
**Jaccard**: 0.056
**Analysis**: Q2 determines the classification. Heath proves 10.105 by directly working with the definition of a minor line: he transfers the ratio AE:EB to CF:FD, then shows CF and FD are incommensurable in square, the sum of their squares is rational, and their rectangle is medial, concluding CD is minor by definition (10.76). The AI takes an entirely different route via the apotome characterization: it applies the squares of x and y to a rational line r, shows the breadth a is a fourth apotome (10.100), proves breadth b is commensurable with a and hence also a fourth apotome (10.103), then invokes 10.94 to conclude y is minor. The two backbones share no key intermediate conclusions, giving Case B (different backbone). Q3 confirms the AI path is valid: every step is supported by a correctly cited prior result, and the chain runs from premises to conclusion without gaps.

### 10.106
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works by direct annex-transfer: decomposing AB into AE and EB (its annex), establishing that AE and EB are incommensurable in square with medial sum of squares and rational rectangle (via 10.77), then transferring these properties proportionally to CF and FD on the commensurable line CD. The AI takes a completely different route via apotome classification: it applies the square of each line to a fixed rational line r, shows the first application yields a fifth apotome (10.101), proves the two breadths are commensurable in length (via 10.9, 10.6, 6.1, 10.11), concludes the second breadth is also a fifth apotome (10.103), and then invokes 10.95 to recover the desired line type. The key intermediate conclusions are entirely different -- Heath's backbone is the preservation of annex properties, while the AI's backbone is the preservation of apotome order under commensurability. This is Case B (different backbone). Q3 confirms the AI's path is logically valid: each step is supported by a correctly cited prior result, and the chain from premises to conclusion is complete.

### 10.107
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works directly with the components (annex) of the lines, transferring the three characteristic properties (incommensurability in square, medial sum of squares, medial rectangle, and their mutual incommensurability) from AE,EB to CF,FD via commensurability, then invoking the definition 10.78. The AI instead uses the apotome classification route: applying the square on A to a rational line r to obtain a sixth apotome breadth (10.102), showing the breadths are commensurable via commensurability of the squares (10.9, 10.6, 6.1, 10.11), transferring the apotome order (10.103), and recovering the line type from the sixth apotome classification (10.96). These are fundamentally different backbones with zero citation overlap (Jaccard 0.0). The AI's chain is logically complete, with every step supported by a cited proposition, so Q3 confirms a valid different path.

### 10.108
**Category**: Granularity difference
**Jaccard**: 0.350
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: applying both areas to a rational line, establishing that one breadth is commensurable and the other incommensurable in length with that line, concluding the two breadths are incommensurable with each other and thus rational commensurable in square only, deriving that their difference is an apotome, and then splitting into two cases (first apotome yielding an apotome side via 10.91, fourth apotome yielding a minor side via 10.94). The sole heath_only citation (10.13) and the AI's substitute (10.12 used by contrapositive) serve the same logical function at the same position: both derive the incommensurability of the two breadths. The ai_only items are over-citations of construction propositions (1.45, 6.1, 6.12, 6.16), algebraic identities (2.1, 2.14), definitions (D10.1.1, D10.1.2, D10.1.3), a common notion (CN3), and 10.76 (confirming irrationality of a minor). Since the key conclusions and logical structure are identical and only citation depth differs, this is a granularity difference.

### 10.109
**Category**: Granularity difference
**Jaccard**: 0.316
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: the breadths of the medial and rational areas applied to a rational reference line are rational and commensurable in square only (one commensurable in length with the reference, the other incommensurable), their difference is an apotome, and the two exhaustive cases (second apotome yielding a first apotome of a medial, fifth apotome yielding a line producing with a rational area a medial whole) are handled identically. The heath_only set is empty, confirming that every Heath citation appears in the AI set. The 13 ai_only items are all lower-level supporting results that Heath invokes implicitly: foundational commensurability propositions (10.12, 10.20, 10.22), construction and algebraic props (1.44, 2.1, 2.14, 6.1), irrationality confirmations (10.74, 10.77), definitions (D10.1.1, D10.1.2, D10.1.3), and a common notion (CN3). This is a classic over-citation pattern where the AI spells out every sub-step that Heath leaves tacit, constituting a citation-depth difference with the same logical backbone.

### 10.110
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: the breadths of the applied medial areas are rational and incommensurable in length with the assigned rational line, they are incommensurable with each other, hence commensurable in square only, so their difference is an apotome (10.73). Both then split into the same two exhaustive cases based on whether the excess is commensurable or incommensurable with the whole, yielding a third apotome (second apotome of medial via 10.93) or a sixth apotome (line producing with medial area a medial whole via 10.96). The AI's additional citations (1.44, 10.12, 2.1, 2.14, CN3, D10.1.1, D10.1.2, D10.1.3) are all construction steps, algebraic lemmas, definitions, and common notions that Heath leaves implicit, while heath_only is empty. This is a clear Case A: same backbone with different citation depth.

### 10.111
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 reveals different logical backbones. Heath derives the contradiction by showing that the segment EG (between the binomial division point G and the apotome annex point F, extended to E) must be both an apotome (via 10.73, after using 10.13 to establish that GF is incommensurable in length with EF) and rational, which is impossible. The AI instead works algebraically with the terms of the two decompositions: it defines e = c - a = b + d, shows e is rational, then applies 10.36 to conclude that b and d must be commensurable in length (otherwise their sum would be irrational), and from this derives that a and b are commensurable in length, contradicting the binomial definition. The pivotal tool 10.36 (sum of rational lines commensurable in square only is irrational) is absent from Heath, while Heath's pivotal tool 10.13 (transitivity of incommensurability) is absent from the AI proof. Both paths are logically valid, yielding classification D.

### 10.112
**Category**: Path difference
**Jaccard**: 0.205
**Analysis**: Q2 determined the classification. Heath's proof works through a geometric construction using VI.16 to relate rectangles to proportions, V.17 for separando, V.12/V.11 to derive segment proportions, VI.22 for square commensurability, and X.20 to establish rationality of the breadth. The AI instead uses II.5 to establish the algebraic identity (a+b)(a-b) + b^2 = a^2, derives commensurability of c and x via VI.1 and X.11, then constructs a fourth proportional u via VI.12 and uses V.19/V.16 to obtain a:b = u:v. These are fundamentally different intermediate routes: Heath places proportional segments on a geometric figure and uses rectangle-proportion machinery (VI.16, VI.22, X.20), while the AI uses a product identity (II.5) and fourth-proportional construction (VI.12, V.19). The key intermediate conclusions differ in substance, not merely in citation depth. The AI's path is logically complete and sound, yielding a valid different proof.

### 10.113
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Heath builds the binomial KH directly through a chain of Book V ratio manipulations (convertendo, alternando) to construct the terms KF and FH, showing them rational and commensurable in square only, then invoking X.36. The AI takes a fundamentally different route: it introduces the conjugate binomial c = a+b, uses the algebraic identity II.5 to show R(t,c) is commensurable with r-squared, deduces that the breadth x is commensurable in length with c and hence binomial by X.66, then invokes the converse theorem 10.112 and the uniqueness-of-annex result 10.79 to establish that the binomial terms of x are commensurable with the apotome terms in the same ratio and order. These backbones share no key intermediate conclusions: Heath never uses a conjugate-binomial identity or the converse theorem, and the AI never constructs the binomial terms through proportion chains. Both paths are logically complete, so the classification is D.

### 10.114
**Category**: Path difference
**Jaccard**: 0.059
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary apotome KL by applying H-squared to CD (using 10.112), then chains ratios via V.19 and commensurability via 10.11/10.12 to show AB is commensurable with KL, transferring this to the rectangles via VI.1. The AI instead takes an algebraic expansion approach: it uses 6.16 to cancel cross-rectangles R(a,d)=R(b,c), expands the product R(a-b, c+d) via 2.1 to obtain S = R(a,c) - R(b,d), shows both component rectangles are rational by 10.19, and derives commensurability of S with the rational square through 10.15 and 10.12. These are genuinely different backbone strategies with entirely different key intermediate conclusions, and the AI's algebraic path is logically complete and valid, yielding D.

### 10.115
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof establishes irrationality of each new line directly via X.20 (the rectangle contained by an irrational and a rational is irrational) and argues distinctness from preceding irrationals by noting that applying each new line's square to a rational line produces a medial breadth, which no preceding irrational does. The AI proof takes a fundamentally different path: it constructs the sequence via mean proportionals using Book 6 results (6.11, 6.13, 6.17), establishes irrationality through incommensurability arguments (10.11), and then systematically excludes all twelve previously established irrational kinds by citing the application results 10.60-10.65 and 10.97-10.102. The two proofs share zero citations (Jaccard = 0.0), confirming the structural divergence. The AI's different path is logically complete and valid under Q3, with every step well-supported by citations, so the classification is D rather than E.


---

## Book 11 — Classification Report (GPT)

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


---

## Book 12 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 7 | 12.6, 12.7, 12.8, 12.9, 12.10, 12.14, 12.15 |
| Path difference (D) | 11 | 12.1, 12.2, 12.3, 12.4, 12.5, 12.11, 12.12, 12.13, 12.16, 12.17, 12.18 |
| AI proof error (E) | 0 |  |

**Total**: 18 propositions

## Per-Proposition Analysis

### 12.1
**Category**: Path difference
**Jaccard**: 0.227
**Analysis**: The forward dependency gate passes (all citations are from Books 1-6). Q1 finds no logical error: the AI proof is complete and valid, with each step properly supported by citations. Q2 compares the backbones. Both proofs share the same early intermediate conclusions: equiangular triangles from polygon similarity (6.6), inscribed angle transfer (AI uses 3.21 where Heath uses 3.27 for the same geometric fact), and equiangular diameter-triangles giving side-to-diameter proportionality (6.4). However, they diverge at the final step: Heath invokes the duplicate ratio concept via 6.20 (similar polygons have to each other a ratio duplicate of corresponding sides), while the AI explicitly constructs squares on the diameters, shows they are similar, and applies 6.22 (proportional lines yield proportional similar figures). Since 6.20 and 6.22 are independent propositions -- neither contains the other in its proof tree -- and the duplicate ratio intermediate conclusion is present in Heath but absent from the AI, Case A of Q2 fails. Under Q3, the AI's different path is positionally valid and logically complete, yielding category D.

### 12.2
**Category**: Path difference
**Jaccard**: 0.036
**Analysis**: Q2 determined the classification. Heath proves XII.2 by the classical double reductio ad absurdum: assuming the ratio of circles equals the ratio of diameter-squares to a lesser area S, he inscribes polygons using exhaustion (10.1), applies XII.1 for similar polygon ratios, and uses proportion manipulation theorems V.11 (transitivity) and V.16 (alternando) to derive a contradiction, then repeats the argument for a greater area. The AI proof takes a fundamentally different path, directly verifying the equimultiple definition of proportion (D5.5): it inscribes and refines polygons showing P_j : Q_j = S : T at every stage by XII.1, uses exhaustion to make remainders arbitrarily small, and then for arbitrary positive integers m and n demonstrates that mC vs nD matches mS vs nT, concluding C : D = S : T without any reductio. Because the key intermediate conclusions differ -- Heath argues through contradiction via proportion manipulation while the AI argues through direct equimultiple verification -- this is a genuine path difference, and Q3 confirms the AI's chain is logically complete.

### 12.3
**Category**: Path difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs establish the same final conclusions (sub-pyramids equal and similar to each other and the whole; two equal prisms greater than half the whole), but the intermediate reasoning differs in two substantive ways. First, Heath uses XI.10 (equal angles from parallel lines in different planes) to establish face congruence via SAS (I.4), while the AI avoids XI.10 entirely by using edge proportionality and SSS similarity (6.5). Second, Heath establishes prism equality directly via XI.39, while the AI constructs a parallelepiped Z, bisects it using XI.28, and shows both prisms are halves of it via superposition (CN4). The AI's parallelepiped construction is an intermediate geometric object absent from Heath's proof, and the AI's method differs even from XI.39's internal proof (which constructs two parallelepipeds and uses XI.31, not one parallelepiped with superposition). Since the containment test fails for both heath_only items and the AI employs genuinely different geometric methods, Case A (same backbone) fails, yielding Case B. Under Q3, the AI's different path is logically complete and valid, so the classification is D.

### 12.4
**Category**: Path difference
**Jaccard**: 0.087
**Analysis**: Q2 decided the classification. Heath's proof establishes the base-to-prism ratio through similar triangles (VI.22) and alternando (V.16), connecting triangle ratios to prism ratios via the Lemma following XII.3 and using XI.39 to equate prisms with parallelogram and triangular bases. The AI proof takes a fundamentally different route: it computes the base area relationship directly using equal-altitude triangles (VI.1) applied twice to show the pyramid base is four times the prism base, then completes prisms to parallelepipeds (I.31, XI.28) and compares them using XI.32 (equal-height parallelepipeds proportional to bases), reducing back to prism ratios via V.15 and V.11. The heath_only citations (6.22, 5.16, 11.39) are not subsumed by any higher-level AI citation but are replaced by an entirely different proof strategy, confirming Case B (different backbone). Q3 confirms the AI's path is logically valid, with every step properly supported by cited propositions, yielding D.

### 12.5
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as Case B (different backbone), confirmed valid in Q3. Heath's proof proceeds by double reductio ad absurdum: it assumes the ratio of pyramids to bases equals a ratio to a hypothetical solid W less than (then greater than) the second pyramid, subdivides via XII.3, compares prism collections via XII.4, and derives contradictions using alternando (V.16), the XII.2 Lemma, and V.2. The AI proof takes a fundamentally different path: it directly verifies all three conditions of Definition V.5 (the Eudoxian definition of equal ratios) by showing that for arbitrary positive integers m and n, the ordering of mP vs nQ matches that of mA vs nB. The AI uses the same core exhaustion machinery (XII.3, XII.4, X.1) but deploys it within a direct equimultiple framework, employing V.11 (transitivity of ratios), V.19 (subtraction of proportional parts), and common notions for the algebraic manipulations. This is a genuinely different logical strategy — direct verification versus indirect contradiction — and the AI's chain from premises to conclusion is logically complete and sound.

### 12.6
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same geometric backbone: triangulate the polygonal bases, apply XII.5 to compare triangular pyramids of equal height, aggregate the triangular ratios to relate full polygonal pyramids, and conclude via V.22 (ex aequali). The sole substantive citation difference is that Heath uses V.18 (componendo) iteratively to build up polygon-to-triangle ratios one step at a time, while the AI uses V.24 (addendo, which adds antecedents with a fixed consequent) to sum all ratios at once. The proof-tree containment test confirms that V.18 appears inside Heath's own proof of V.24, so the AI is citing V.24 as a unit while Heath re-derives its internals inline. The remaining ai_only items (11.2, CN2, D11.12, D5.5, D6.4, P1) are all definitions, common notions, postulates, or construction-level citations, representing over-citation rather than a path divergence. Since the key geometric conclusions are the same and the citation difference is one of depth, this is a granularity difference.

### 12.7
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decides the classification. Both proofs share the same logical backbone: decompose the prism into three triangular pyramids, then establish pairwise equality by showing base triangles are equal halves of parallelogram faces (I.34) and applying the pyramid ratio result (XII.5). Though the AI uses different cutting diagonals (AF, BF, AE vs. Heath's BD, EC, CD), the key intermediate conclusions are structurally identical in both proofs. The ai_only set (11.2, CN1, D11.12, D11.13, D5.5, D6.4, P1) consists entirely of definitions, common notions, postulates, and one foundational Book 11 proposition, all of which Heath takes as implicit. With heath_only empty and the backbone the same, this is a citation-depth difference classifying as G.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct parallelepipeds on the similar pyramids, show these parallelepipeds are similar, apply XI.33 for the triplicate ratio of similar parallelepipeds, then use XI.28 and XII.7 to establish that each pyramid is one-sixth of its parallelepiped, and transfer the ratio. The sole heath_only citation, XI.24 (opposite faces of a parallelepiped are equal and similar), is used by Heath to help establish the similarity of the two parallelepipeds. The AI reaches the same conclusion by citing lower-level results: I.34 for opposite sides of parallelograms, I.29 for supplementary angles, XI.10 for dihedral angles, and the definitions D6.1 and D11.9 for similarity of figures and solids. The ai_only set consists entirely of definitions, common notions, construction propositions, parallelogram properties, and ratio algebra propositions that support the same key conclusions Heath establishes more tersely. This is Case A of Q2: same backbone, different citation depth.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct parallelepipeds around the pyramids, establish that each parallelepiped is six times its pyramid, apply XI.34 for reciprocal proportionality of parallelepipeds, connect parallelepiped bases to triangular bases via I.34, and chain ratio equalities to reach the conclusion, with the converse proved by reversing the argument. The heath_only citation (5.11, transitivity of equal ratios) is used by Heath to chain ratio equalities; the AI achieves the identical logical step using 5.15 (equimultiples preserve ratios) and direct substitution. The large ai_only set consists almost entirely of construction details (1.31, 11.15, 11.28), the explicit pyramid-prism relation (12.7), definitions (D5.5, D6.4), and a common notion (CN2) that Heath leaves implicit. Since both proofs argue through the same key intermediate conclusions and differ only in citation depth, the classification is G.

### 12.10
**Category**: Granularity difference
**Jaccard**: 0.107
**Analysis**: Q2 decides this classification as G. Both proofs share the same logical backbone: a double reductio ad absurdum via exhaustion, inscribing successively refined polygons in the circular base, establishing that each refinement removes more than half of the remaining solid (conical or cylindrical), invoking X.1 (exhaustion), and using XII.7 to convert between prisms and pyramids (prism = 3 times pyramid). The AI addresses both required cases (cylinder > 3 times cone in Step 7, cylinder < 3 times cone in Step 8). The heath_only items (11.32, 12.2, 4.7) all correspond to facts present in the AI proof at the same logical position but argued at finer granularity or with different equivalent lemmas: Heath uses 11.32 (parallelepipeds of same height are as bases) for comparing prisms, while the AI uses 12.5 and 12.6 (pyramids of same height are as bases) for the analogous comparison; Heath references 12.2 for the more-than-half exhaustion technique, while the AI re-derives it explicitly using 1.41 and 3.16; Heath circumscribes a square (4.7) for the initial more-than-half argument, while the AI uses a rectangle containment argument instead. The large ai_only set consists overwhelmingly of definitions, common notions, postulates, and elementary construction propositions, indicating over-citation at a finer granularity level rather than a different proof path.

### 12.11
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification. Heath proves 12.11 by the classic double reductio ad absurdum: assuming the proportion between cones and bases fails, he inscribes exhausting polygonal pyramids, applies alternation of proportions (5.16) to derive a contradiction, then handles the greater-solid case by inversion. The AI instead gives a direct proof via the Eudoxian definition of equal ratios (D5.5): after constructing similar inscribed polygons and showing their pyramid ratios match the base ratios (12.1, 12.2, 12.6), the AI directly verifies all three comparison cases of the definition (mB1 = nB2, mB1 > nB2, mB1 < nB2) using gap-control arguments with 5.15 and 5.19 rather than alternation. These represent genuinely different logical backbones -- Heath's pivotal intermediate conclusion is the alternation step yielding cone:pyramid = O:pyramid, while the AI's pivotal conclusions are the direct gap-control inequalities in Steps 7-9. The AI's path is logically complete and valid under Q3.

### 12.12
**Category**: Path difference
**Jaccard**: 0.103
**Analysis**: Q2 determined the classification. Heath's proof uses the method of exhaustion: inscribing similar polygonal pyramids in the cones, applying X.1 to exhaust the gap, invoking XII.8 (similar pyramids in triplicate ratio of corresponding sides), aggregating via V.12, and reaching a double reductio ad absurdum (less-than and greater-than cases). The AI proof takes an entirely different route: it introduces an auxiliary cylinder T sharing the second cylinder's base but the first cylinder's height, proves T:C2 = h:k = a:b by a stacking argument from the definition of equal ratios (D5.5), then applies 12.11 (same-height cylinder comparison) and 12.2 (circles as squares on diameters) to build a chain of proportions, which it combines via ex aequali (5.22) to obtain the triplicate ratio for cylinders, transferring to cones via 12.10 and 5.15. The backbones share no key intermediate conclusions: Heath's pivots on pyramid similarity (XII.8) and exhaustion (X.1), while the AI's pivots on direct cylinder-ratio algebra (12.11, 12.2, 6.20). At Q3, the AI's chain is logically complete, with each step supported by cited propositions, so the verdict is D.

### 12.13
**Category**: Path difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification. Heath's proof relies on XII.11 (cones and cylinders of the same height are proportional to their bases, proved by exhaustion) to establish that cylinder segments with equal heights and equal bases are equal, then builds equimultiples and applies V. Def. 5. The AI proof takes a fundamentally different route, avoiding XII.11 entirely: it defines cylinders via generating rectangles, assembles congruent copies end-to-end to form equimultiples, and compares the assembled cylinders by geometric inclusion or coincidence of their generating rectangles. The proof-tree containment test confirms that XII.11 (the sole heath_only substantive proposition) is not subsumed by any AI-cited higher-level result; the AI's approach is an independent path from first principles using definitions (D11.21-D11.23), common notions (CN2, CN4, CN5), and low-level Book 1/11 propositions. Since the backbones differ (Case B) and the AI's chain is logically complete under the Q3 check, the classification is D.

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct an auxiliary cylinder by extending an axis, use XII.13 (cylinder cut by a parallel plane gives ratio equal to axis ratio) to establish the proportion between cylinders and their axes, use XII.11 (cylinders on equal bases with the same height are equal) to substitute the auxiliary cylinder for the target, and extend to cones via XII.10. The AI proof cites the same three core propositions as Heath (12.10, 12.11, 12.13) but additionally cites construction steps (1.3, P2), definitions (D11.21, D11.22, D11.23, D3.1, D5.5), a geometric lemma for parallel planes (11.14), and ratio manipulation propositions (5.7, 5.11, 5.15) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations of constructions, definitions, and ratio lemmas filling out steps present but implicit in Heath, this is Case A: same backbone with different citation depth, yielding G.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs construct an auxiliary solid sharing the base of one original solid and the height of the other, then establish that the ratio to the auxiliary equals the ratio of bases (via 12.11) and the ratio of heights (Heath via 12.13, AI via 12.14), combining with 5.11, 5.7, and 5.9 to reach the reciprocal proportion and its converse. The proof-tree containment test confirms that 12.13 appears inside Heath's own proof of 12.14, so the AI cites 12.14 as a single higher-level unit while Heath re-derives its internals inline. The remaining ai_only items D11.18 and D11.21 are definitions (overcitation). Heath case-splits the forward direction into equal and unequal heights, whereas the AI handles both uniformly through 12.14, which applies regardless; this is a presentational, not structural, difference. Same backbone, different citation depth: G.

### 12.16
**Category**: Path difference
**Jaccard**: 0.105
**Analysis**: Q2 decided the classification. Heath's proof argues through tangent-line and parallelism intermediates: AC is tangent to the inner circle (3.16), the perpendicular bisector yields LD = DN (3.3, 1.4), and LN parallel to the tangent AC therefore does not touch the inner circle. The AI proof instead argues through angle-chord comparison and distance inequalities: the hinge theorem (1.24) establishes that any polygon side UV is shorter than the reference chord BC, the chord-distance theorem (3.15) then shows the perpendicular from the center to UV exceeds r, and triangle properties (1.17, 1.19) extend this to every point on every side. These are fundamentally different key intermediate conclusions -- neither set is a refinement or compression of the other -- placing the proofs in Case B of Q2. Q3 confirms the AI path is logically complete: every step is justified by cited propositions, and the chain from premises to conclusion is sound.

### 12.17
**Category**: Path difference
**Jaccard**: 0.171
**Analysis**: Classification was decided at Q2/Q3. The two proofs share the high-level goal of inscribing a polyhedron in the greater sphere that avoids the lesser, but their key intermediate conclusions and distance arguments differ fundamentally. Heath inscribes the equilateral polygon so it does not touch the lesser circle directly, then analyzes the perpendicular distance from the center to each face through a specific chain of square comparisons (KB^2 > 2BX^2 via the circumscribed-circle property, KB^2 < 2KZ^2 via III.31 and VI.8), concluding AX > AZ > AG. The AI instead constructs a mean proportional s = sqrt(Rr) between the two radii (6.13, 6.17), inscribes the polygon so it does not touch a circle of radius s rather than r (explicitly citing 12.16), then uses a general projection-and-scaling argument to show every face point P satisfies OP >= ka = a^2/R > s^2/R = r. The constructions, the cited propositions, and the logical backbones are all different, yielding a Jaccard of only 0.171. The AI's path is logically complete under the hardened Q1(b) standard, so the classification is D.

### 12.18
**Category**: Path difference
**Jaccard**: 0.071
**Analysis**: Q2 decided the classification. Heath's proof uses the classic double reductio (method of exhaustion): assuming the ratio holds to a smaller sphere, inscribing a non-touching polyhedral solid (12.17), deriving a contradiction via alternation (5.16), then handling the greater sphere case via 12.2 Lemma. The AI proof takes a fundamentally different path: it introduces concentric cubes as intermediaries whose ratio is the triplicate of the diameters (11.33), subdivides inscribed polyhedra into similar triangular pyramids (12.8, 6.6, 6.4, 6.5), constructs cubical shell approximations controlled by 10.1, and directly verifies the equimultiple definition (D5.5) to establish the ratio without any reductio argument. These are clearly different backbones -- the AI avoids double reductio entirely and instead gives a direct equimultiple proof. Under Q3, the AI's different path is logically complete: each step is explicitly justified with cited propositions, the chain runs from premises to conclusion, and the mathematical strategy of using cubes as intermediaries with controlled approximation error is sound.


---

## Book 13 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 9 | 13.3, 13.4, 13.8, 13.12, 13.13, 13.14, 13.15, 13.16, 13.17 |
| Path difference (D) | 9 | 13.1, 13.2, 13.5, 13.6, 13.7, 13.9, 13.10, 13.11, 13.18 |
| AI proof error (E) | 0 |  |

**Total**: 18 propositions

## Per-Proposition Analysis

### 13.1
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves 13.1 through geometric constructions using gnomons and the proportionality theorem 6.1 to establish area relations within the constructed figure, ultimately showing that the square on CD equals five times the square on DA. The AI proof takes a fundamentally different algebraic route through Book 2 propositions: it uses 2.1 (rectangle distribution) and 2.4 (square-of-sum identity) to manipulate the area expressions algebraically, avoiding gnomon constructions and proportionality entirely. Both proofs share the starting point (6.17 for the extreme-and-mean-ratio rectangle-square equality) and the intermediate fact that the square on the whole equals four times the square on the half, but the logical backbone connecting these to the conclusion diverges: Heath's geometric proportionality path through 6.1 versus the AI's algebraic decomposition path through 2.1 and 2.4. The containment test confirms this is not a depth difference, since 6.1 does not appear inside Heath's proof of 6.17. Q3 confirms the AI's algebraic path is logically complete and valid.

### 13.2
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 13.2 entirely through area manipulation: constructing squares and gnomons, showing gnomon MNO equals CG (both quadruple AH), then by careful area subtraction establishing the rectangle CD,DB equals CB squared, which yields the extreme and mean ratio proportion DC:CB = CB:BD via 6.1. The AI takes a fundamentally different path by invoking proposition 13.1 directly: it cuts CD in extreme and mean ratio at E (via 6.30), applies 13.1 to conclude (CE + AC) squared equals 5 times AC squared, matches this with the hypothesis that AB squared equals 5 times AC squared, then proves CE + AC = AB by contradiction (using 2.4 and CN5), and subtracts AC to get CE = CB. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different: Heath works with area equalities and proportions while the AI leverages the converse-like relationship established in 13.1. The AI proof is logically complete and valid, so the classification is D.

### 13.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) rect(AB,CB) = AC^2 from the extreme and mean ratio property, (2) AC^2 = 4DC^2 from bisection, and (3) combining these to obtain DB^2 = 5DC^2. Heath achieves the combination through geometric gnomon manipulations in a constructed square figure without citing any propositions, while the AI uses an algebraic approach explicitly citing 2.6 (bisected-and-extended line identity), 2.4 (square of a sum), 6.17 (mean proportional rectangle equality), 1.10 (bisection), and common notions. Since heath_refs is empty and all AI citations formalize steps Heath performs without explicit citation, the identical backbone with different citation depth yields a granularity difference.

### 13.4
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establishing that rectangle AB·BC equals the square on AC via the golden ratio definition (D6.3) and Proposition 6.17, (2) showing that AB² + CB² equals twice rectangle AB·CB plus AC², and (3) substituting to obtain AB² + CB² = 3·AC². The difference is purely one of citation depth: Heath re-derives step (2) inline through a geometric construction involving gnomons and area manipulation on the square ADEB, while the AI cites Proposition 2.7, which proves exactly this algebraic identity. The ai_only items CN1 and CN2 are common notions that Heath uses implicitly. Since heath_only is empty and the AI's additional citations (2.7, CN1, CN2) reflect over-citation and packaging of inline reasoning rather than a different proof path, this is Case A of Q2: same backbone, different citation depth.

### 13.5
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 determined the classification. Heath's proof works through areas: it constructs a square on AB, establishes that rectangle AB*BC equals the square on AC (via VI.17), performs area manipulations to show rectangle BD*DA equals the square on AB, then converts back to a proportion via VI.17 and uses V.14 for ordering. The AI proof works entirely within proportions: starting from AB:AC = AC:CB, it applies V.12 (sum of antecedents to sum of consequents) to obtain (AB+AC):(AC+CB) = AB:AC, then substitutes AD = AB+AC and AB = AC+CB to reach AD:AB = AB:BD directly, using CN5 for the ordering. The key intermediate conclusions differ fundamentally -- Heath's backbone pivots on the area equality rect(BD,DA) = sq(AB), while the AI's backbone pivots on the ratio composition (AB+AC):(AC+CB) = AB:AC. Since the backbones are different (Q2 Case B) and the AI's ratio-based chain is logically complete (Q3), the classification is D.

### 13.6
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. For the first segment (AC is an apotome), both proofs share the same backbone: they use XIII.1 to establish CD squared equals five times DA squared, show CD is rational, prove CD and DA are incommensurable in length (since 5:1 is not a ratio of square numbers), and conclude AC is an apotome by X.73. However, for the second segment (CB), the proofs diverge fundamentally in their key intermediate conclusions. Heath uses the golden ratio rectangle property (AB times BC equals AC squared, via VI.Def.3 and VI.17) and then applies X.97 (square on an apotome applied to a rational line produces a first apotome) to conclude CB is a first apotome. The AI instead constructs DB = 3 times DA, proves DB and DC are rational and commensurable in square only through a transitivity argument using X.12, and then applies X.73 directly to conclude CB is an apotome. These are genuinely different logical paths with different key intermediates, not merely different citation depths for the same argument. The AI's alternative path is logically complete and valid (Q3 confirmed), yielding classification D.

### 13.7
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decides the classification. Heath's consecutive-angle case relies on the intersection point F of diagonals AC and BE, using I.6 (converse of the isosceles triangle theorem) to establish AF=BF, then subtracting to get FC=FE, and finally applying I.8 on triangles FCD and FED. The AI proof takes a fundamentally different geometric route: it never introduces the diagonal intersection point and never invokes I.6, instead applying I.4 to triangles ABC/EDC to get AC=EC, then I.5 on triangle ACE, and separately I.4 on ABC/BCD to get AC=BD followed by I.8 on triangles BAD/CDA with the common side AD. The AI also handles the non-consecutive case differently, reducing it to the consecutive case via the A=E result from Step 3, whereas Heath proves it directly. Since the key intermediate conclusions differ (Heath's chain passes through the intersection-point equalities AF=BF and FC=FE, which the AI's chain entirely avoids), this is Case B in Q2 — different backbone. Q3 confirms the AI's alternative path is logically valid throughout, yielding D.

### 13.8
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) establishing angle equalities in a triangle to show a segment equals the side of the pentagon via I.6, (2) proving equiangularity of two specific triangles, (3) applying VI.4 to derive the proportion, and (4) concluding extreme and mean ratio. The proofs differ in their sub-methods for reaching these shared conclusions: Heath circumscribes a circle about the pentagon (IV.14) and uses arc-angle theorems (III.28, VI.33) to establish angle equalities, while the AI computes angles directly from interior angle sums and isoceles triangle properties. Similarly, Heath uses V.14 for segment inequality while the AI uses I.19. For each heath_only citation, the underlying geometric fact is present in the AI proof at the same logical position, established by a different but equivalent method. The ai_only items are predominantly common notions, definitions, and a postulate (over-citation of basics), plus I.19 as a minor alternative to V.14. Since the backbone is the same and differences are in citation depth and sub-step methodology, this is Case A in Q2, yielding G.

### 13.9
**Category**: Path difference
**Jaccard**: 0.158
**Analysis**: Q2 decides the classification as D. Heath proves the result directly by showing triangles EBD and EBC are equiangular (using VI.33 for arc-angle proportionality and VI.4 for similar-triangle proportions), obtaining BD:DC = DC:CB in one step from the compound segment BD = BC + CD. The AI takes a fundamentally different route: it constructs an angle bisector in the isosceles triangle formed by two radii and the decagon side, uses angle chasing (I.5, I.6, I.32) to show the bisector foot D satisfies OD = AB (decagon side), applies the angle bisector theorem (VI.3) to establish OB:OD = OD:DB (i.e., the radius is cut in extreme and mean ratio with the decagon side as greater segment), and then invokes XIII.5 to derive that the sum of the hexagon and decagon sides is cut in extreme and mean ratio with the hexagon side as greater segment. The two proofs share no key intermediate conclusions: Heath never establishes that the radius is cut in EMR, and the AI never constructs equiangular triangles or uses arc-angle proportionality. The Jaccard similarity of 0.158 reflects this deep divergence. The AI proof is logically complete and sound throughout, so this is a valid different path.

### 13.10
**Category**: Path difference
**Jaccard**: 0.147
**Analysis**: Q2 decided the classification. Heath proves the result through proportion theory and similar triangles: he establishes that triangles ABF and BFN are equiangular (yielding AB*BN = BF^2 via VI.4/VI.17) and that triangles KBA and KNA are equiangular (yielding BA*AN = AK^2), then combines these via II.2 to get BA^2 = BF^2 + AK^2. The AI takes a fundamentally different route: it shows BF = r + d by an auxiliary construction with a cut-off point T on BF and SAS congruence, invokes XIII.9 (the extreme and mean ratio result for hexagon and decagon sides) to obtain r^2 = rd + d^2, applies the Pythagorean theorem (I.47) to the right triangle ABF inscribed in a semicircle (III.31), and arrives at p^2 = r^2 + d^2 by algebraic manipulation. These key intermediate conclusions are genuinely different, and both chains are logically complete, so the classification is D.

### 13.11
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 reveals fundamentally different backbones, sending classification to Q3. Heath's proof works by geometric construction within the circle (center, perpendiculars, similar triangles ACL and AMF) and bridges to the 5:1 ratio via XIII.8 (diagonal of pentagon cut in extreme and mean ratio, greater segment equals the side) and XIII.1 (square on greater segment plus half of whole equals five times the square on the half). The AI instead reframes the problem algebraically using the hexagon side h and decagon side t, invoking XIII.9 (h+t in extreme and mean ratio), XIII.10 (pentagon side squared equals sum of hexagon and decagon side squared), and XIII.3 (square on lesser segment plus half of greater equals five times square on half of greater) to establish the same 5:1 ratio structure through entirely different intermediate objects (a = 5u, b = t+u, e = a-b). The AI also introduces number theory (7.22, 7.30, 7.33) to prove 5:1 is not a ratio of square numbers, whereas Heath applies X.9 directly. Both proofs ultimately show the square on the pentagon side equals a rational line times a fourth apotome and apply X.94, but the routes to that conclusion are genuinely different. Under Q3, the AI's chain is logically complete with every step cited and sound, yielding classification D.

### 13.12
**Category**: Granularity difference
**Jaccard**: 0.095
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a diameter through a vertex of the inscribed equilateral triangle, establish that a segment from another vertex to the far endpoint of that diameter equals the radius, invoke the angle-in-a-semicircle result (III.31) to obtain a right triangle, apply the Pythagorean theorem (I.47), compute that the square on the diameter equals four times the square on the radius, and subtract to conclude that the square on the side equals three times the square on the radius. The sole heath_only citation, IV.15 (inscribing a regular hexagon), packages the fact that the hexagonal side equals the radius; the AI re-derives this same intermediate conclusion from more elementary propositions (III.20 for the central angle, I.5 and I.32 for the angle sum in the isosceles triangle OBD, and I.6 to conclude BD equals the radius). Similarly, Heath states directly that the square on the diameter is quadruple the square on the radius, while the AI cites II.4 for the same arithmetic. The large ai_only set consists of these lower-level derivation steps plus definitions, postulates, and common notions that Heath leaves implicit. Since both proofs establish the same key intermediate conclusions at the same logical positions and differ only in citation depth, Case A of Q2 holds, yielding G.

### 13.13
**Category**: Granularity difference
**Jaccard**: 0.226
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: cut the diameter AB so AC = 2CB, construct CD perpendicular in the semicircle, inscribe an equilateral triangle in a circle of radius CD (both cite 4.2), apply XIII.12 to obtain base edge squared equals three times the radius squared, show all six edges are equal, inscribe the pyramid in the sphere, and prove the diameter-to-side ratio. The proofs differ in citation depth and minor method choices: Heath uses I.4 (SAS congruence) to establish lateral edge equality while the AI uses I.47 (Pythagorean theorem) to compute the same edge lengths directly, and Heath cites III.1 to find the circle center while the AI's construction places the circle at the known center C, making III.1 unnecessary. The 22 ai_only items are overwhelmingly definitions (D1.15, D1.20, D11.12, D11.14, D11.16, D11.17), postulates (P1, P3), common notions (CN1, CN2, CN5), and foundational construction propositions that Heath takes as implicit, representing over-citation rather than path divergence. Since the key intermediate conclusions are the same at every logical position, this is Case A of Q2: same backbone, different citation granularity.

### 13.14
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a square from the sphere's diameter, erect perpendicular poles from the square's center at equal distance, prove all edges from poles to vertices equal the square's side (yielding eight equilateral triangles forming an octahedron), show all six vertices lie on a sphere of the given diameter, and conclude that the square on the diameter is double the square on the side via I.47. The heath_only set is empty, confirming the AI cites every proposition Heath cites. The 22 ai_only items consist entirely of construction propositions (1.10, 1.11), postulates (P1-P4), common notions (CN1, CN2), definitions (D1.15, D1.17, D1.18, D1.20, D1.22, D11.3, D11.12, D11.14, D11.16, D11.17, D11.26), and minor supporting theorems (1.15, 1.8, 11.2) that Heath uses implicitly. This is a classic over-citation pattern with the same backbone at different citation depth, yielding G.

### 13.15
**Category**: Granularity difference
**Jaccard**: 0.061
**Analysis**: Q2 Case A decided the classification. Both proofs establish the same key intermediate conclusions: (1) finding a side length a satisfying d-squared equals 3a-squared, (2) constructing the cube from that side, (3) proving all solid diagonals equal d via I.47, and (4) inscribing the cube in the sphere of diameter d. The AI uses an explicit mean proportional construction (6.13, 6.17, 6.9, 2.1) for step (1), while Heath uses an implicit semicircle construction achieving the same result without citing Book VI. The AI's 31 additional citations (ai_only) consist entirely of definitions (D1.15, D1.17, D1.18, D1.22, D1.23, D11.14, D11.16, D11.17, D11.25), postulates (P1-P4), common notions (CN1, CN2, CN5), and foundational propositions from Books I, II, III, VI, and XI that Heath leaves unstated. The empty heath_only set confirms every step present in Heath also appears in the AI proof. The very low Jaccard (0.061) reflects exhaustive over-citation of elementary steps, not a different proof strategy.

### 13.16
**Category**: Granularity difference
**Jaccard**: 0.140
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs construct the icosahedron by the same fundamental method: establishing a circle with radius r satisfying D^2 = 5r^2, inscribing an equilateral pentagon, bisecting arcs for decagonal points, constructing two staggered pentagonal rings plus two apex vertices to form the 12 vertices, using XIII.10 (pentagon^2 = hexagon^2 + decagon^2) as the key metric relation to show all edges equal, proving all 20 faces equilateral, demonstrating all vertices equidistant from a common center to establish comprehension in the sphere, and applying XIII.11 to classify the side as minor. The backbone of key intermediate conclusions is identical. The large citation difference (Jaccard 0.14) reflects citation depth, not structural divergence: the AI explicitly cites 33 additional elementary propositions (postulates, definitions, construction steps like I.47, I.33, I.3, II.4, III.28-30, IV.11, VI.9, VI.13, XI.12, XI.15, XI.16) that Heath leaves implicit. The four heath_only items (XI.6, III.31, VI.8, V.Def.9) are replaced by equivalent citations at different granularity: XI.6 (perpendiculars to same plane are parallel) is replaced by XI.8 plus XI.15/XI.16; III.31 and VI.8, used in Heath's proportion-and-semicircle argument for sphere comprehension, are replaced by the AI's direct distance computation via I.47 and II.4; and V.Def.9 is unnecessary in the AI's algebraic approach. In every case the underlying geometric fact is present in both proofs at the same logical position.

### 13.17
**Category**: Granularity difference
**Jaccard**: 0.216
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: constructing a dodecahedron from a cube, proving each face is an equilateral equiangular pentagon in one plane, verifying all twenty vertices lie on the circumsphere, and proving the side is an apotome. The differences lie entirely in subsidiary methods at each juncture. For coplanarity, Heath uses VI.32 and XI.6 while the AI uses proportional right triangles (VI.6) and supplementary angles (I.14) with XI.4 and XI.8. For equiangularity, Heath invokes XIII.7 (three equal angles of an equilateral pentagon imply equiangularity) while the AI proves all five angles equal directly via diagonal computation and SSS congruence (I.8), bypassing XIII.7 entirely. For the circumsphere, Heath uses XI.38 while the AI derives the same from its coordinate framework. The AI's very large ai_only set (25 items) reflects its more explicit citation style, including many definitions, postulates, common notions, and basic construction propositions, alongside alternative substantive lemmas used in place of Heath's shortcuts. The four heath_only items (XI.38, XI.6, XIII.7, VI.32) are propositions Heath uses as convenient tools whose underlying conclusions are nonetheless present in the AI proof, established by different means. Since the key intermediate conclusions are identical and the differences are in citation depth and subsidiary proof methods, this is a granularity difference.

### 13.18
**Category**: Path difference
**Jaccard**: 0.276
**Analysis**: Q1 found no logical defect in the AI proof: the algebraic bounding arguments for i and d are sound, with every step justified by a cited proposition or common notion. Q2 identified a genuinely different backbone in the comparison portion: Heath constructs all five sides as segments on the diameter using similar triangles (6.4, 6.8, D5.9, 6.20) and proves the icosahedron side exceeds the dodecahedron side through a direct geometric inequality chain (AD > FB, AL > FB, KL > NB, MB > NB), while the AI derives the icosahedron side via pentagonal auxiliary figures (i squared equals r squared plus x squared, D squared equals 5r squared) using 13.8 and 13.9, bounds i squared to the interval (1/5)D squared to (3/10)D squared, bounds d squared below (1/6)D squared, and concludes the full ordering t > o > c > i > d from these bounds. The two paths share the same starting ratios from 13.13-13.15 but diverge in the intermediate conclusions used for the comparison, making this Case B. Q3 confirmed the AI path is valid, yielding classification D.

