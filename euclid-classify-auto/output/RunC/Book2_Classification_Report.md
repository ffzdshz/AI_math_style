# Book 2 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 4 | 2.1, 2.12, 2.13, 2.14 |
| Path difference (D) | 10 | 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11 |
| AI proof error (E) | 0 |  |

**Total**: 14 propositions

## Per-Proposition Analysis

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
