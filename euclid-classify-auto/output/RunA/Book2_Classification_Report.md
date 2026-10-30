# Book 2 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 5 | 2.1, 2.9, 2.12, 2.13, 2.14 |
| Path difference (D) | 9 | 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.10, 2.11 |
| AI proof error (E) | 0 |  |

**Total**: 14 propositions

## Per-Proposition Analysis

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
