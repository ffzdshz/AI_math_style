# Book 6 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 28 | 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 6.11, 6.12, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18, 6.19, 6.21, 6.24, 6.25, 6.26, 6.27, 6.28, 6.29, 6.32, 6.33 |
| Path difference (D) | 5 | 6.20, 6.22, 6.23, 6.30, 6.31 |
| AI proof error (E) | 0 |  |

**Total**: 33 propositions

## Per-Proposition Analysis

### 6.1
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: constructing equimultiples of the bases by extending the base line and marking equal segments, establishing equal triangles on equal bases via I.38, showing equimultiple correspondence between bases and triangles, verifying the three cases (equal, excess, less) for the definition of proportion (V. Def. 5), then extending to parallelograms via I.41, transferring the ratio via V.15, and concluding by transitivity via V.11. The AI proof cites six additional foundational references that Heath uses implicitly without citation: postulates P1 and P2 for joining and extending lines, proposition 1.3 for cutting off equal segments, common notion CN5 for the whole being greater than the part, and definitions D5.2 and D6.4 for equimultiples and height respectively. Since heath_only is empty and all ai_only items are postulates, common notions, definitions, or a basic construction proposition present implicitly in both proofs, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decided the classification. Both proofs follow identical two-part structures with the same key intermediate conclusions in the same order: in Part I, establishing BDE = CDE, deriving equal ratios to ADE, converting triangle ratios to segment ratios via VI.1/6.1, and concluding BD:DA = CE:EA via V.11/5.11; in Part II, reversing the argument through VI.1/6.1, V.11/5.11, V.9/5.9, and I.39/1.39. The only citation differences are that the AI uses I.37 (triangles on the same base in the same parallels are equal) where Heath uses I.38 (triangles on equal bases in the same parallels are equal) — both valid for the same logical fact since the triangles share the literal same base DE — and the AI over-cites D6.4 (definition of height) and P1 (postulate for joining lines). These are citation-depth differences at the same logical positions, making this Case A in Q2: same backbone, different granularity.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs are biconditional and prove both directions using the identical construction (draw a line through C parallel to DA, extend BA to meet it at E). The key intermediate conclusions are the same in both parts: establishing angle equalities via I.29, deducing AE = AC via I.6 (part 1) or I.5 (part 2), applying VI.2 for the proportionality, and substituting equals. The AI's seven extra citations (1.17, 1.31, 5.7, CN1, P1, P2, P5) are all construction-level postulates, common notions, or lower-level propositions that Heath uses implicitly. heath_only is empty, confirming that the AI cites everything Heath does and more. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 6.4
**Category**: Granularity difference
**Jaccard**: 0.636
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: placing BC in line with CE, producing BA and ED to meet at F, establishing BF parallel to CD and AC parallel to FE via I.28, obtaining parallelogram FACD with FA equal to CD and AC equal to FD via I.34, then applying VI.2 twice to derive proportions, substituting equal sides, using alternando (V.16), and concluding with ex aequali (V.22). The AI proof adds four over-citations not in Heath: 5.7 and 5.11 to make the ratio substitution steps explicit (where Heath simply says 'But AF is equal to CD; therefore...'), P2 for producing lines, and D5.11 for the definition of corresponding sides. Since heath_only is empty and all ai_only items are granularity-level elaborations of steps Heath performs implicitly, this is Case A of Q2: same backbone, different citation depth.

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.700
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: construct triangle GEF on EF with angles equal to those of ABC (I.23), deduce remaining angle equality (I.32), apply VI.4 to obtain proportionality in the equiangular triangles, use V.11 and V.9 to show DE=GE and DF=GF, then apply I.8 and I.4 to establish congruence of triangles DEF and GEF, and chain the angle equalities to conclude. The AI's three additional citations (1.17, P5, CN1) are all over-citations providing explicit justification for steps Heath leaves implicit: 1.17 and P5 justify that the lines constructed at E and F actually meet to form triangle GEF, while CN1 makes the transitivity of angle equality explicit. Since the key intermediate conclusions are identical and the citation difference is purely one of depth, this is a granularity difference.

### 6.6
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: construct triangle DGF on DF with angles matching those of ABC (I.23), show ABC equiangular with DGF via the angle-sum property (I.32), apply proportionality of equiangular triangles (VI.4) to obtain GD:DF = BA:AC, combine with the hypothesis through V.11 to get ED:DF = GD:DF, conclude ED = DG (V.9), then use SAS congruence (I.4) to show DEF congruent to DGF and derive all angle equalities. The only citation difference is that the AI explicitly invokes CN1 (Common Notion 1, transitivity of equality) for the angle equality chains in Steps 7, 9, and 10, while Heath applies these substitutions implicitly without citation. Since CN1 is a common notion (axiom-level reference) and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference under Case A of Q2, yielding G.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.889
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assuming angle ABC is not equal to angle DEF, constructing angle ABG equal to DEF via I.23, showing triangle ABG equiangular with DEF via I.32, deriving AB:BG = DE:EF via VI.4, combining with the hypothesis via V.11 to get BC = BG via V.9, applying I.5 for the base angles, and then reaching a contradiction in each of the two cases (angles less than a right angle via I.13, angles not less via I.17). The AI proof addresses both cases explicitly and completely. The only citation difference is that the AI explicitly cites CN3 (Common Notion 3, equals subtracted from equals) in Steps 4 and 14, where Heath leaves the same reasoning implicit when invoking I.32 to conclude that remaining angles are equal. Since CN3 is a common notion (axiom) and not a substantive proposition, this is a straightforward over-citation, confirming Case A of Q2: same backbone, different citation depth.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing equiangularity of each sub-triangle with the whole triangle (right angles equal, one angle common, third angle equal by I.32), deriving proportional sides via VI.4, and concluding similarity via VI.Def.1, then proving mutual similarity of the two sub-triangles by the same method. The AI proof is more explicit, writing out both sub-triangle cases in full rather than using Heath's 'similarly,' and adding Step 2 (proving D lies between B and C using 1.16, 1.17). The ai_only set {1.16, 1.17, CN3, D1.10, P4} consists entirely of foundational over-citations: postulates, common notions, definitions, and basic Book 1 propositions used for construction details or implicit steps that Heath leaves uncited. The heath_only set is empty, confirming the AI covers everything Heath does at greater granular depth. This is Case A of Q2: same backbone, different citation depth.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) DF is drawn parallel to BC, (2) CD:DA = BF:FA by VI.2, (3) CD being double DA implies BF is double FA, (4) BA is triple of AF. The AI proof cites the same three substantive propositions as Heath (1.3, 1.31, 6.2) but adds five foundational items (CN2, D5.1, D5.5, P1, P2) that Heath leaves implicit. Since the backbones match and the citation difference consists entirely of postulates, definitions, and common notions that the AI makes explicit, this is a same-backbone, different-depth case under Q2 Case A, yielding G.

### 6.10
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: constructing parallels DF and EG to BC and DHK to AB, identifying parallelograms FGHD and GBKH to obtain DH=FG and HK=GB via I.34, then applying VI.2 twice in triangles DKC and AGE to derive the two required proportions CE:ED=BG:GF and ED:DA=GF:FA. The four ai_only citations (1.30, 5.7, 5.11, P1) are all explicit references for steps Heath performs implicitly: 1.30 for transitivity of parallelism, 5.7 and 5.11 for ratio substitution of equal magnitudes, and P1 for joining line BC. Heath_only is empty, confirming the AI cites a strict superset. Since the key intermediate conclusions are the same and only citation depth differs, this is Case A of Q2, yielding G.

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct BD equal to AC, join BC, draw DE parallel to BC through D, apply 6.2 to obtain AB:BD = AC:CE, then substitute BD = AC to conclude AB:AC = AC:CE. The AI proof over-cites by explicitly invoking P1 and P2 for basic constructions and 5.7 and 5.11 to spell out the ratio substitution that Heath performs implicitly in a single sentence. Since heath_only is empty and all ai_only items (P1, P2, 5.7, 5.11) represent finer-grained citations of steps Heath takes without explicit reference, this is a citation-depth difference with the same backbone, yielding G.

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct two lines DE, DF at any angle, mark off segments DG=A, GE=B, DH=C, join GH, draw EF parallel to GH through E, then apply 6.2 to obtain DG:GE = DH:HF, and substitute to conclude A:B = C:HF. The AI proof cites five additional references (P1, P2, 1.3, 5.7, 5.11) that Heath uses implicitly without citation. P1 and P2 justify setting out and producing lines, 1.3 justifies cutting off equal segments, and 5.7 and 5.11 justify the ratio substitution steps. Heath's proof has no citations absent from the AI proof (heath_only is empty). Since the key intermediate conclusions are identical and the citation differences reflect only the depth at which construction and ratio-substitution steps are made explicit, this is a granularity difference.

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: place AB and BC in a straight line, construct a semicircle on AC, draw BD perpendicular to AC, establish that angle ADC is right by III.31, and conclude that DB is a mean proportional by VI.8. The AI proof is far more explicit, citing construction postulates (P1, P2, P3), construction propositions (1.3, 1.10, 1.11), definitions (D1.15, D1.17, D1.18, D1.21, D6.1), and 6.4 to unpack the proportionality that Heath derives in a single step from VI.8. Since heath_only is empty and all ai_only items are construction citations, definitions, or an elaboration of VI.8's conclusion, this is Case A: same backbone with different citation depth, yielding Granularity difference (G).

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: placing the parallelograms so DB and BE are collinear, showing FB and BG are collinear via I.14, completing parallelogram FE, then using VI.1 twice with V.7 and V.11 for the forward direction, and VI.1 twice with V.11 and V.9 for the converse. The AI's six extra citations (1.13, 1.31, CN1, CN2, D6.2, D6.4) are all construction propositions, common notions, and definitions that Heath uses implicitly. The AI explicitly justifies the collinearity of FB and BG through supplementary angles (1.13, CN1, CN2) before invoking I.14, explicitly cites 1.31 for drawing parallels to complete FE, and references definitions D6.2 and D6.4 for clarity. Since heath_only is empty and all ai_only items represent over-citation of construction and foundational steps, this is Case A of Q2: same backbone, different citation depth.

### 6.15
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in both directions of the biconditional: placing the triangles so that CA is collinear with AD and EA with AB (via I.14), joining BD, using V.7 to establish equal ratios of the equal triangles to the common triangle BAD, converting triangle ratios to side ratios via VI.1, and concluding with V.11; the converse reverses the chain using VI.1, V.11, and V.9. The AI proof is strictly more explicit, adding 1.13, CN1, and CN2 to justify the collinearity step that Heath handles implicitly with I.14 alone, citing P1 for the join construction, and referencing D6.2 for the definition of reciprocal proportionality. All ai_only items (1.13, CN1, CN2, D6.2, P1) are construction props, axioms, or definitions representing over-citation, and heath_only is empty. The identical logical backbone with differing citation depth yields G.

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone for both directions of the biconditional: construct perpendiculars AG=F and CH=E, complete parallelograms BG and DH, derive the reciprocal proportion AB:CD=CH:AG from the hypothesis, then apply 6.14 to conclude equality of the parallelograms (and hence of the rectangles). The converse uses the same construction and applies 6.14 in reverse. The AI proof is substantially more verbose, explicitly citing 1.11 for perpendicular construction, 1.3 for cutting equal lengths, 1.31 for completing parallelograms, 1.29 for angle properties of parallels, 5.7 and 5.11 for proportion substitution steps, D2.1 for the definition of a rectangle, and P4 for equality of right angles, all of which Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are construction propositions, proportion lemmas, definitions, and postulates, this is a clear case of same backbone with different citation depth.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone for each direction of the biconditional: construct D equal to B, establish the four-term proportion A:B::D:C, apply 6.16 to equate rect(A,C) with rect(B,D), and identify rect(B,D) as sq(B) since B equals D, with the converse reversing this chain. The ai_only citations (1.2, 5.7, 5.11, D1.22, D2.1) are all over-citations that make explicit what Heath leaves implicit: the construction step (1.2), the ratio substitution when B equals D (5.7), transitivity of ratios (5.11), and the definitions identifying a rectangle and square (D1.22, D2.1). With heath_only empty and the logical backbone matching, this is Case A: same key intermediate conclusions at different citation depth, yielding G.

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: divide the given rectilineal figure into triangles by joining a diagonal, construct equiangular triangles on the given line AB using I.23 and I.32, establish proportional sides via VI.4, combine the proportions to show the whole figures have equal corresponding angles and proportional sides, and conclude similarity by VI.Def.1. The AI proof is strictly more explicit than Heath's, citing 1.17 and P5 to justify that constructed lines will meet, CN2 and CN3 for angle addition and subtraction, P1 for joining lines, and 5.22 for the ex aequali step combining proportions. All of these are foundational steps that Heath performs implicitly. Since heath_only is empty and all ai_only items represent deeper citation of the same reasoning rather than different intermediate conclusions, Case A of Q2 holds, yielding G.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing a third proportional BG via VI.11, using alternation (V.16) and transitivity (V.11) to establish AB:DE = EF:BG, applying VI.15 to show triangle ABG equals triangle DEF, invoking V.Def.9 for the duplicate ratio, and using VI.1 to relate the triangles by their bases. The ai_only set consists entirely of construction propositions (1.3, P1, P2), definitions (D6.1, D6.2), and ratio substitution (5.7), all reflecting more explicit citation of steps that Heath performs implicitly. The heath_only item D5.11 (definition of corresponding sides) is a definitional reference that the AI addresses through D6.1 instead. Since the logical backbone is the same and the citation differences are purely a matter of depth, this is a granularity difference.

### 6.20
**Category**: Path difference
**Jaccard**: 0.462
**Analysis**: The forward-dependency gate passes cleanly. Q1 finds no logical defect: the AI proof is complete and every step is properly supported by cited propositions. Q2 reveals that while the first part of the proof (dividing similar polygons into similar triangles, Steps 1-11) shares the same backbone as Heath — both use VI.6, VI.4, angle subtraction, and V.22 ex aequali in the same sequence — the second part (proving the triangles are in the same ratio as the wholes) follows a fundamentally different route. Heath joins the further diagonals AC and FH, uses I.32 to show partial triangles equiangular, and compares the component triangles through their bases using VI.1 and V.12 with alternation. The AI instead applies VI.19 to the shared corresponding sides (BE:GL and EC:LH) of adjacent similar triangle pairs, constructs third proportionals via 6.11, identifies the duplicate ratio via D5.9, equates the triangle ratios via 5.11, and sums via V.12. The heath_only references 1.32 and 6.1 belong entirely to Heath's diagonal-based approach and are not subsumed by any proposition the AI cites; conversely, the ai_only references 5.11, 6.11, and D5.9 belong to the AI's duplicate-ratio approach. This constitutes a genuine path divergence (Case B). Q3 confirms the AI's alternative chain is logically valid, running soundly from premises to conclusion, so the classification is D.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they unpack the similarity of A to C and B to C using Definition 6.1, then conclude that A must be equiangular with B and have proportional sides, hence A is similar to B. The AI proof makes two implicit transitivity steps explicit by citing CN1 (things equal to the same thing are equal to one another, for angle equality) and 5.11 (ratios the same with the same ratio are the same with one another, for side proportionality), while Heath performs these same logical moves without explicit citation. Since heath_only is empty and the ai_only items (CN1, 5.11) merely supply deeper justification for steps that both proofs share, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 6.22
**Category**: Path difference
**Jaccard**: 0.462
**Analysis**: Q2 decided the classification. Part I of both proofs shares the same backbone: taking third proportionals, applying ex aequali (5.22), and linking figure ratios to line ratios via 6.19. However, Part II (the converse) follows a fundamentally different logical path. Heath constructs a line QR such that AB:CD = EF:QR, then uses 6.18 to build a similar figure SR on QR, applies the forward direction to get MF:SR = MF:NH, deduces NH = SR, and concludes GH = QR from the equal and similar figures. The AI instead constructs a fourth proportional X and a third proportional Y, derives through ratio arithmetic that P = Y and EF:X = X:P, then proves X = GH by a contradiction argument using ratio inequality propositions (5.8, 5.10, 5.13). The AI never constructs a similar figure and works entirely within Book V ratio theory for the converse, making the key intermediate conclusions genuinely different. Both paths are logically valid, so the classification is D.

### 6.23
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: The forward-dependency gate passes (all AI citations are from Books 1 and 6 with no forward references). Q1 finds the AI proof logically complete: it correctly constructs the intermediate parallelogram CH, establishes two ratio equalities via 6.1, and applies the definition of compound ratio (D6.5) directly to conclude. Q2 reveals Case B (different backbone): while both proofs share the same geometric core (constructing CH and using 6.1 twice to get AC:CH = BC:CG and CH:CF = DC:CE), Heath's proof introduces auxiliary magnitudes K, L, M via 6.12 (fourth proportional construction) and transfers ratios via 5.11 (transitivity), then combines via ex aequali. This auxiliary-line method is entirely absent from the AI proof, which instead bypasses the construction by directly applying D6.5 to the parallelogram chain AC, CH, CF. Since 5.11 and 6.12 are substantive propositions argued in Heath but absent from the AI proof (and not contained in any proposition the AI cites), Case A fails. At Q3, the AI's different path is logically complete and valid, yielding classification D.

### 6.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: using VI.2 on the two triangles formed by the diameter to establish proportions, combining via transitivity, composition, and alternation to show sides about the common angle are proportional, establishing equiangularity of the relevant triangles through parallel lines and common angles, deriving all proportional side ratios with ex aequali (V.22), and concluding similarity by VI.Def.1. The AI's six extra citations (1.29, 1.30, 1.34, 5.11, 6.4, CN1) all explicitly name propositions that Heath uses implicitly at the same logical positions: 1.29 for angle equalities from parallel lines, 1.30 for transitivity of parallelism, 1.34 for opposite angles of parallelograms, 5.11 for transitivity of proportions, 6.4 for proportional sides in equiangular triangles, and CN1 for equality of equals. Heath's proof leaves all of these implicit. With heath_only empty and all ai_only items being over-citations at the same logical steps, this is a clear Case A granularity difference.

### 6.25
**Category**: Granularity difference
**Jaccard**: 0.353
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: they construct the same parallelograms BE (equal to ABC) and CM (equal to D), establish collinearity of BC with CF and LE with EM, take GH as a mean proportional of BC and CF, construct KGH similar to ABC on GH, establish the core ratio BC:CF = ABC:KGH = BE:CM, and conclude KGH = D. The AI proof is significantly more explicit, citing sub-step propositions (1.14, 1.29, 1.34, CN1, CN2) for the collinearity arguments that Heath states without justification, and citing D5.9, 5.11, and 6.20 for steps Heath leaves implicit or handles with the triangle-specific 6.19 alone. The only substantive algebraic difference is that Heath uses V.16 (alternately) for the final deduction while the AI uses V.7 and V.9 instead, but both start from the same proportion (ABC:KGH = BE:CM) and the same equality (ABC = BE) and reach the same conclusion (KGH = CM = D). This is the same backbone argued at different citation depth, making it a granularity difference.

### 6.26
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs use the same proof-by-contradiction strategy with identical key intermediate conclusions: assume the inner parallelogram is not about the same diameter, produce GF to meet the diameter at H, draw HK through H parallel to AD (1.31), establish that parallelogram AKHG is similar to ABCD (6.24), derive DA:AB = GA:AK and DA:AB = GA:AE from the two similarity relations, conclude GA:AK = GA:AE by 5.11, hence AK = AE by 5.9, contradicting the fact that one is a proper part of the other. The AI proof adds extensive foundational citations (1.30, CN5, D1.23, D6.1, P1, P2) that Heath leaves implicit, but these are entirely postulates, definitions, common notions, and a basic proposition about parallel lines. The heath_only set is empty. This is Case A: same backbone, different citation depth, yielding G.

### 6.27
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: establishing that DB and FB are about the same diameter via VI.26, using complements CF = FE via I.43, building the equality chain CH = KE and CG = CH via I.36, and concluding that AF equals only a portion of DB so AD > AF. The AI proof is more detailed, explicitly handling two cases and citing construction steps (1.10), postulates (P1, P2), and common notions (CN1, CN2, CN3, CN5) that Heath uses implicitly. Since heath_only is empty and all ai_only items are axioms, postulates, or construction references, this is a clear case of overcitation at the same backbone — a granularity difference.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: bisect AB at E, construct EBFG on EB similar to D (6.18), complete the parallelogram AG, handle the trivial case AG = C, then for the main case construct KM equal to the excess of GB over C and similar to D (6.25), show KM is similar to GB (6.21), prove GE > KL and GF > LM, cut off GO = KL and GP = LM to construct OGPQ, establish OGPQ is about the same diameter as EBFG (6.26), derive that the gnomon equals C, use complement equality and equal-base parallelogram results to conclude TS = C. The heath_only set is empty, confirming every Heath citation appears in the AI set. The 15 ai_only items are all construction propositions (1.10, 1.3, 1.31), foundational results (1.4, 1.34, 1.43), common notions (CN1-CN5), postulates (P1, P2), a definition (D6.1), 5.14 for inequality reasoning, and 6.24 for explicitly establishing similarity of parallelograms about the diameter, all of which are sub-steps Heath leaves implicit. This is a clear case of the same backbone argued at different citation depth.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect AB, construct BF similar to D on EB, construct GH equal to BF+C and similar to D via 6.25, build MN equal and similar to GH, invoke 6.26 for the common diameter, extract the gnomon equal to C, and use I.36 and I.43 to show the applied parallelogram equals C with the excess similar to D via 6.24. The heath_only set is empty, confirming every Heath citation appears in the AI's set. The 16 ai_only items are all elaborations of steps Heath leaves implicit: construction propositions (1.10, 1.3, 1.30, 1.31, 6.18), basic results used to prove sub-steps in detail (1.4, 1.34 for triangle congruence to establish MN=GH; 5.14 for the inequality FM>FL), common notions (CN1, CN2, CN3, CN5), definitions (D2.2, D6.1), and postulates (P1, P2). The AI's path note explicitly states it chose 5.14 over 6.20 and 1.4+1.34 over 6.14 for sub-arguments, but the key intermediate conclusions remain identical. This is Case A of Q2: same backbone, different citation depth.

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs the golden section via parallelogram application (6.29) and derives the proportion through reciprocal proportionality of equiangular parallelograms (6.14). The AI takes an entirely different route: it uses 2.11 to cut AB so that the rectangle contained by the whole and one segment equals the square on the other, then applies the converse of 6.17 to convert that rectangle-equals-square condition directly into the required proportion, and finally uses CN5 and 5.14 to establish the ordering of segments. The two proofs share zero citations (Jaccard = 0.0) and have fundamentally different key intermediate conclusions -- Heath argues through area subtraction and reciprocal proportionality while the AI argues through the mean proportional theorem. The AI proof is logically complete: each step is correctly justified by the cited proposition, and the chain runs soundly from premises to conclusion. The AI itself explicitly acknowledges Heath's route and explains why it chose the alternative path through 2.11 and 6.17.

### 6.31
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same construction (perpendicular from vertex to hypotenuse, yielding similar sub-triangles via 6.8), but their key intermediate conclusions diverge. Heath derives the continued proportion CB:BA = BA:BD from similarity and then applies 6.19 (similar triangles are in duplicate ratio of corresponding sides) to directly relate figure ratios to line-segment ratios. The AI takes a genuinely different route: it establishes the sub-triangles DBA and DAC as similar figures similarly described on the relevant sides (via D6.1), then uses 6.22 (proportional lines yield proportional similar figures) to set up Q:P = DBA:ABC and R:P = DAC:ABC, and finishes by combining these ratios with 5.24 and concluding via 5.16 and 5.9. Although 6.19 appears in Heath's proof of 6.22 (satisfying the containment test), the proofs' key intermediates are structurally different: Heath reasons through line-to-figure ratios via duplicate ratio, while the AI reasons through area-to-area ratios using sub-triangles as mediating similar figures. The AI itself acknowledges this is an alternative route chosen deliberately. Since the backbones differ (Case B) and the AI's chain is logically complete under Q3, the classification is D.

### 6.32
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: parallel lines yield equal alternate angles via I.29 applied twice, transitivity gives angle BAC equal to angle CDE, VI.6 establishes equiangular triangles so angle ABC equals angle DCE, the angle sum at C is shown equal to two right angles via I.32, and collinearity of BC and CE follows from I.14. The AI proof explicitly cites Common Notions CN1 and CN2 for transitivity of equality and addition of equals, whereas Heath applies these same axioms implicitly without citation. Since heath_only is empty and ai_only contains only Common Notions (axioms, not substantive propositions), this is a citation-depth difference with the same backbone, satisfying Case A of Q2.

### 6.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same Eudoxean equimultiple method: constructing equimultiple circumferences, establishing that the corresponding central angles are the same multiples (via III.27), verifying the triple comparison, applying V. Def. 5 to conclude the ratio of circumferences equals the ratio of central angles, and then extending to inscribed angles via the doubling relationship. The key intermediate conclusions are identical in both proofs. The AI simply cites more explicitly what Heath leaves implicit: P1 for joining lines, CN5 for the whole-greater-than-part comparison, III.20 for the inscribed angle theorem (Heath writes 'they are doubles respectively' without citation), V.15 for the ratio of halves, and V.11 for transitivity of ratios. With heath_only empty and all ai_only items being over-citations of construction details, axioms, and propositions that Heath invokes implicitly, this is a clear Case A granularity difference.
