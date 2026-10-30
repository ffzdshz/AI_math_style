# Book 2 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 12 | 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.9, 2.10, 2.11, 2.12, 2.13, 2.14 |
| Path difference (D) | 2 | 2.7, 2.8 |
| AI proof error (E) | 0 |  |

**Total**: 14 propositions

## Per-Proposition Analysis

### 2.1
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical geometric argument: construct rectangle BH with BG equal to A, then identify each sub-rectangle (BK, DL, EH) with the corresponding rect(A, segment) using I.34, and conclude BH equals their sum. The key intermediate conclusions are the same in both proofs. The AI proof explicitly cites 1.29 (to show right angles via parallel lines), 1.30 (transitivity of parallelism), CN1 (transitivity of equality), and D2.1 (definition of rectangle), whereas Heath uses these facts implicitly without citation. Since heath_only is empty and all ai_only items are foundational elaborations of steps present in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 2.2
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow identical backbones: construct square ADEB on AB, draw CF through C parallel to AD to divide the square into two rectangles AF and CE, identify AF as rect(AB,AC) since DA equals AB and CE as rect(AB,BC) since BE equals AB, and conclude their sum equals the square on AB. The AI proof cites 1.34 (opposite angles in parallelograms are equal), D1.22 (definition of square), and D2.1 (definition of rectangle) as additional justifications for the same intermediate steps that Heath handles implicitly. Since heath_only is empty and ai_only consists entirely of over-citations (two definitions and one supporting theorem applied to the same conclusions), this is a clear granularity difference.

### 2.3
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct square CDEB on CB, draw AF parallel to CD/BE through A, decompose figure AE into AD and CE, then identify AE as the rectangle contained by AB and BC, AD as the rectangle contained by AC and CB, and CE as the square on CB. The AI proof adds explicit citations for foundational steps that Heath leaves implicit -- 1.28 and 1.29 for proving parallelism via interior angles, 1.30 for transitivity of parallelism, D1.22 for the definition of a square, D2.1 for the definition of a rectangle, and P2 for producing a line segment. Since heath_only is empty and all ai_only items are over-citations supporting the same intermediate conclusions at greater depth, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 2.4
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same geometric argument: constructing a square on the whole line, subdividing it with parallels through the cut point, showing the resulting sub-figures are squares on the segments and rectangles equal to the product of the segments, then summing the parts. The key intermediate conclusions are identical in both proofs: CGKB is equilateral and right-angled hence a square on CB, HF/HDFG is a square on AC, AG equals the rectangle contained by AC and CB, AG equals GE as complements about the diameter, and the four regions sum to the whole square ADEB. The AI's eight additional citations (1.28, 1.30, 1.43, CN1, CN2, D1.22, D2.1, P1) represent over-citation of construction propositions (1.28, 1.30), a complement theorem Heath uses without citing (1.43), definitions, common notions, and a postulate that Heath invokes implicitly, constituting a citation-depth difference rather than a substantive path divergence.

### 2.5
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions through the same logical backbone: construct square CEFB on CB, show CH=HF by I.43, derive CM=DF by adding DM, show AL=CM by I.36 (since AC=CB), deduce AH=gnomon NOP, identify AH as rect(AD,DB) since DH=DB, and conclude rect(AD,DB)+sq(CD)=sq(CB). The AI proof is far more verbose, explicitly citing definitions (D1.22, D2.1, D2.2), common notions (CN1, CN2), a postulate (P1), and supporting propositions (1.34 for opposite sides of a parallelogram, 2.4 Porism for parallelograms about a diameter being squares) that Heath leaves implicit. Since heath_only is empty and all ai_only items are over-citations making explicit what Heath uses tacitly, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 2.6
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct square CEFD on CD, draw parallels through B, H, and A, establish AL = CH (I.36), CH = HF (I.43), combine to show AM equals the gnomon NOP which equals the rectangle AD,DB, then add LG (the square on BC) to reach the conclusion. The AI proof follows this identical chain in its Steps 5-12, matching every key intermediate conclusion of Heath's proof. The ai_only set (1.29, 1.30, 1.34, 2.4, CN1, CN2, D1.22, D2.1, D2.2, P1) consists entirely of additional explicit citations for steps Heath leaves implicit: common notions for equals-added-to-equals, definitions for rectangles and gnomons, parallelism transitivity, a postulate for joining lines, and the porism to 2.4 for identifying sub-squares. Heath_only is empty, confirming Heath's references are a strict subset of the AI's. This is a clear Case A in Q2: same backbone with the AI providing greater citation depth.

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3 (path difference). The AI proof uses an algebraic approach, combining the decomposition identity 2.4 (square on a line equals squares on segments plus twice the rectangle) with the rectangle identity 2.3 (rectangle on whole and segment equals rectangle on segments plus square on segment), then uses arithmetic operations (doubling and addition, justified by CN2) and transitivity (CN1) to derive the desired equality. Heath's proof takes a direct geometric approach: constructing the square on AB (I.46), using the complement theorem (I.43) to establish equality of areas about the diagonal, then manipulating the gnomon and squares. The key intermediate conclusions are entirely different -- Heath works with gnomons, complements about the diagonal, and geometric area decomposition, while the AI works with previously proved algebraic identities from 2.3 and 2.4. The proof-tree containment test confirms genuine divergence: I.43, which is central to Heath's proof of 2.7, does not appear in Heath's proofs of 2.3 or 2.4, so the AI's route is not merely a higher-level packaging of the same geometric argument. The AI's algebraic chain is logically complete and valid, so the classification is D.

### 2.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 2.8 by the gnomon method: constructing the square on AD, dissecting it into squares and complements using I.36 (parallelograms on equal bases) and I.43 (complements), and showing the gnomon STU equals four times rect(AB,BD). The AI instead takes an algebraic route, applying 2.4 to expand sq(AD) into sq(AB)+sq(BD)+2*rect(AB,BD), substituting BD=CB, then using 2.7 to relate sq(AB)+sq(CB) to 2*rect(AB,CB)+sq(AC), and combining these identities to reach 4*rect(AB,CB)+sq(AC)=sq(AD). The key intermediates are entirely different: Heath's backbone is geometric decomposition of the gnomon into eight equal rectangular areas, while the AI's backbone is algebraic combination of two prior quadratic identities. The citation sets are completely disjoint (Jaccard=0.0), confirming genuinely different paths. The AI's chain is logically complete, each step justified by cited propositions or common notions, so Q3 confirms validity, yielding D.

### 2.9
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing CE perpendicular to AB and equal to AC/CB, establishing half-right angles in triangles ACE and ECB, proving angle AEB is right, showing EG=GF and FD=DB via angle arguments and I.6, then chaining Pythagorean applications (I.47) to conclude that the squares on AD and DB are double the squares on AC and CD. The AI proof cites the same core propositions as Heath (1.29, 1.32, 1.34, 1.47, 1.6) and additionally cites construction steps (1.11, 1.3, 1.31), the isosceles base-angle theorem (1.5), supplementary angles (1.13), common notions (CN1, CN2, CN3), a definition (D1.10), and postulates (P1, P2) that Heath leaves implicit. With heath_only empty and all ai_only items being construction propositions, axioms, or postulates, this is a clear Case A same-backbone, different-depth scenario warranting G.

### 2.10
**Category**: Granularity difference
**Jaccard**: 0.706
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: constructing CE perpendicular to AB at C equal to AC, joining EA and EB, drawing parallels EF and FD, producing EB and FD to meet at G, then establishing half-right-angle arguments in isosceles triangles ACE, BCE, and BDG, proving BD=GD and GF=EF, and applying the Pythagorean theorem (I.47) three times to derive that the squares on AD and DB together are double the squares on AC and CD. The AI proof explicitly cites Common Notions CN2, CN3, CN5 and Postulates P1, P2 that Heath leaves implicit, constituting over-citation of basic axioms rather than any structural divergence. With heath_only empty and ai_only consisting entirely of foundational axioms and postulates, this is a clear case of same backbone with different citation depth.

### 2.11
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: construct square ABDC, bisect AC at E, join BE, extend CA to F with EF equal to BE, construct square AFGH on AF, extend GH to K, then apply II.6 to obtain rect(CF,FA)+sq(AE)=sq(EF), substitute EF=EB, apply I.47 at the right angle, subtract sq(AE), identify FK=AD, subtract AK, and conclude rect(AB,BH)=sq(AH). The AI proof cites every construction step, postulate, common notion, and definition explicitly (1.10, 1.13, 1.3, CN1, CN3, D1.22, D2.1, P1, P2) where Heath leaves these implicit. The heath_only set is empty, confirming that the AI omits nothing Heath cites. This is Case A of Q2: same backbone, different citation depth.

### 2.12
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: applying 2.4 to the line CD cut at point A to express sq(DC) in terms of sq(CA), sq(AD), and 2*rect(CA,AD); adding sq(DB) to both sides; applying 1.47 twice to replace sq(CD)+sq(DB) with sq(CB) and sq(AD)+sq(DB) with sq(AB); and substituting to reach the conclusion. The AI's additional citations (1.12, 1.17, P2, D1.10, D1.11, CN1, CN2) are all over-citations of construction steps, postulates, definitions, and common notions that Heath leaves implicit. Since heath_only is empty and all ai_only items are foundational-level references, the proofs differ only in citation depth, not in their key intermediate conclusions.

### 2.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: apply 2.7 to the line CB cut at D, add the square on DA to both sides, apply 1.47 twice to the right triangles ABD and ACD, substitute to obtain CB^2 + BA^2 = AC^2 + 2*rect(CB,BD), and conclude. The AI proof adds an explicit verification that D lies within BC (Step 2, using 1.16) and cites definitions (D1.10, D1.12, D1.21), common notions (CN1, CN2, CN3), postulates (P2, P4), and a construction proposition (1.12) that Heath leaves implicit. The heath_only set is empty, confirming the AI covers everything Heath does. All ai_only items are foundational references cited at a finer granularity, not substantive divergences, so Case A of Q2 holds and the classification is G.

### 2.14
**Category**: Granularity difference
**Jaccard**: 0.188
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct rectangular parallelogram BD equal to A via I.45, handle the trivial BE=ED case, then for the non-trivial case produce BE to F with EF=ED, bisect BF at G, draw semicircle BHF, apply II.5 to obtain rect(BE,EF)+sq(EG)=sq(GF), substitute GH for GF as radii, apply I.47 to get sq(HE)+sq(EG)=sq(GH), subtract sq(EG) to conclude rect(BE,EF)=sq(HE), and finally substitute to reach A=sq(HE). The key intermediate conclusions are identical in both proofs. The AI proof differs only in citation depth: it explicitly cites every construction step (1.3, 1.10, 1.11, 1.46), definitions (D1.15, D1.22, D2.1), common notions (CN1, CN3), postulates (P1, P2, P3), and a basic result (1.34) that Heath leaves implicit. The empty heath_only set confirms that the AI covers all of Heath's cited material. This is Case A of Q2: same backbone, different citation depth.
