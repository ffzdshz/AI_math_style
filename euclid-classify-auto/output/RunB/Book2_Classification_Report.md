# Book 2 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 6 | 2.1, 2.6, 2.9, 2.12, 2.13, 2.14 |
| Path difference (D) | 8 | 2.2, 2.3, 2.4, 2.5, 2.7, 2.8, 2.10, 2.11 |
| AI proof error (E) | 0 |  |

**Total**: 14 propositions

## Per-Proposition Analysis

### 2.1
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct rectangle BGHC with BG equal to A, then identify each sub-rectangle (BGKD, DKLE, ELCH) as the rectangle contained by A and the corresponding segment (BD, DE, EC), using I.34 to show the vertical sides equal BG and hence equal A. The AI proof adds three explicit citations not in Heath: I.29 (to justify that DK is perpendicular to BC because it is parallel to BG which is perpendicular to BC), CN2 (to justify summing the sub-rectangles), and D2.1 (the definition of rectangle, to formally identify each parallelogram as a rectangle). Heath leaves all three implicit. Since heath_only is empty and the ai_only items are all over-citations providing finer justification for steps that appear in both proofs at the same logical position, this is Case A of Q2: same backbone, different citation depth.

### 2.2
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof decomposes the square on AB geometrically by drawing a parallel line CF through C (using I.31), splitting the square ADEB into two rectangles AF and CE, then identifying each as rect(BA, AC) and rect(AB, BC) respectively. The AI takes a fundamentally different approach: it invokes Proposition 2.1 (the distributive property of rectangles over line segments) with both lines set equal to AB, obtaining rect(AB, AB) = rect(AB, AC) + rect(AB, CB), then identifies rect(AB, AB) with sq(AB) by definition. The key intermediate conclusions differ entirely -- Heath's central step is the geometric decomposition via a parallel line, while the AI's central step is the algebraic application of 2.1. Since these represent genuinely different logical backbones (Case B in Q2), Q3 was applied: the AI's path is logically complete and valid, so the classification is D.

### 2.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as D (path difference). Heath's proof constructs a square CDEB on CB (I.46), draws a parallel line AF (I.31), and then decomposes the resulting rectangle AE into sub-rectangles AD and CE, identifying each with the required terms. The AI takes a fundamentally different approach by recognizing 2.3 as a direct corollary of Proposition 2.1: it treats AB and BC as two straight lines where AB is cut at C, applies 2.1 to get rect(AB,BC) = rect(AC,BC) + rect(CB,BC), and then identifies rect(CB,BC) as the square on BC by definition. The proof-tree containment test was applied since the AI cites 2.1 as a higher-level proposition and heath_only contains {1.31, 1.46}. While 1.31 appears in Heath's proof of 2.1, 1.46 does not, so containment fails. The key intermediate conclusions differ: Heath's backbone is geometric area decomposition of a constructed figure, while the AI's backbone is algebraic application of 2.1. The AI's path is logically valid (2.1 is correctly applied, the identification of rect(CB,BC) with sq(BC) is sound), yielding a valid different path.

### 2.4
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs the square ADEB on AB, draws parallels, and geometrically decomposes it into four areas (two smaller squares HF and KC on segments AC and CB, plus two rectangles AG and GE each equal to rect(AC,CB)), using Book 1 propositions about parallel lines, angle equality, and parallelograms (1.29, 1.31, 1.34, 1.46, 1.5, 1.6). The AI proof takes a completely different algebraic path: it applies Proposition 2.3 twice (once for each segment) to get rect(AB,AC) = rect(AC,CB) + sq(AC) and rect(AB,CB) = rect(CB,AC) + sq(CB), adds these equations via CN2, then substitutes using 2.2 (which states rect(AB,AC) + rect(AB,CB) = sq(AB)) via CN1 to reach the conclusion. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different: Heath identifies geometric sub-regions within a constructed figure, while the AI manipulates algebraic identities from earlier Book 2 propositions. Both paths are logically complete and valid, making this a genuine path difference.

### 2.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof is geometric-constructive: it builds a square on CB (1.46), draws parallels (1.31), uses the complement theorem (1.43) and area equivalence (1.36) to establish the identity through gnomons and area rearrangement. The AI proof is algebraic: it applies 2.4 to expand sq(CB), uses 2.3 and 2.1 to decompose rect(AD, DB), then combines these results through substitution and Common Notions to reach the same conclusion. The two proofs share zero citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different — Heath argues through complements and gnomons while the AI argues through algebraic identities from earlier Book 2 propositions. This is a clear Case B (different backbone) in Q2. The AI's algebraic chain is logically complete and sound (Q3(b) holds), so the classification is D.

### 2.6
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: constructing square CEFD on CD, drawing parallels, establishing AL = CH (I.36), CH = HF (I.43), deriving AL = HF by transitivity, identifying the gnomon as equal to rect(AD,DB), and adding sq(CB) to both sides to reach the conclusion. The ai_only set {CN1, CN2, P1} consists entirely of common notions and a postulate that Heath uses implicitly but the AI cites explicitly: CN1 for the transitive step AL = HF, CN2 for the addition step, and P1 for drawing the diagonal. The heath_only set is empty. This is Case A of Q2 -- same backbone with different citation depth, where the AI over-cites foundational axioms that Heath leaves implicit.

### 2.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 2.7 uses a geometric gnomon approach: constructing square ADEB on AB (I.46), applying I.43 (complements about the diagonal are equal) to establish AG = GE, then working through the gnomon KLM and square areas to reach the conclusion. The AI proof takes a fundamentally different algebraic path: it applies 2.4 to expand sq(AB) into sq(AC) + sq(CB) + 2*rect(AC,CB), then applies 2.3 to show rect(AB,CB) = rect(AC,CB) + sq(CB), and combines these via CN1 and CN2 to reach the same conclusion. The key intermediate conclusions are entirely different — Heath argues through gnomons and area complements while the AI argues through algebraic identities from earlier Book 2 propositions. The proof-tree containment test confirms this is not mere citation-depth difference: I.43, which is central to Heath's proof, does not appear inside the proofs of either 2.3 or 2.4, so the AI's route is genuinely independent. The AI's algebraic chain is logically complete and valid (Q3(b) holds), so the classification is D.

### 2.8
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 2.8 works geometrically by constructing a square on AD, then using properties of parallelogram complements (I.43) and parallelograms on equal bases (I.36) to show that eight sub-areas forming a gnomon are quadruple of the rectangle AK, then adding the square on AC to obtain the full square on AD. The AI proof takes an entirely different algebraic route: it applies 2.4 twice to expand sq(AD) and sq(CD), uses 2.1 to decompose rect(AC,CD), then applies 2.3 to relate rect(AB,CB) to rect(AC,CB) + sq(CB), combining these to reach the same conclusion. The key intermediate conclusions are completely different — Heath passes through gnomon areas and complement equalities, while the AI passes through algebraic decomposition identities from earlier Book 2 propositions. The citation sets are fully disjoint (Jaccard = 0.0), confirming genuinely different proof strategies. The AI proof is logically complete and sound throughout, so Q3(b) holds, yielding category D.

### 2.9
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct CE perpendicular to AB and equal to AC/CB, join lines, draw parallels, establish half-right-angle properties in isosceles right triangles ACE and ECB, show EG=GF via I.6 in triangle EGF, show FD=DB via I.6, identify GF=CD via I.34, then apply the Pythagorean theorem (I.47) three times to conclude sq(AE)=2*sq(AC), sq(EF)=2*sq(CD), and combine via sq(AF) expressed two ways. The AI proof is a superset of Heath's citations: heath_only is empty, and ai_only consists entirely of construction propositions (1.11, 1.3, 1.31), foundational references (1.13, 1.5, CN1, P1) that Heath uses implicitly without citing. This is a clear Case A granularity difference where the AI over-cites construction and axiomatic steps.

### 2.10
**Category**: Path difference
**Jaccard**: 0.053
**Analysis**: Q2 decided the classification. Heath's proof constructs a geometric figure with perpendiculars (I.11), parallels (I.31), and uses isosceles triangle properties (I.5, I.6) and the Pythagorean theorem (I.47) four times to establish the result through geometric relationships in a constructed figure. The AI proof takes an entirely different algebraic route, applying three earlier Book 2 identities (2.7, 2.6, 2.4) and combining them via algebraic manipulation with common notions to reach the same conclusion. The key intermediate conclusions are completely different: Heath establishes that sq(EA) = 2*sq(AC) and sq(EG) = 2*sq(CD) via right triangles, while the AI establishes rect(AD,DB) = sq(CD) - sq(AC) and sq(AB) = 4*sq(AC) via rectangle identities. The Jaccard similarity of 0.053 (only CN1 shared) reflects this fundamental divergence in proof strategy. The AI proof is logically complete and valid, with each step correctly applying its cited proposition.

### 2.11
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Both proofs share the same construction and the same first four key intermediate conclusions through rect(CF,FA) = sq(AB), established via 2.6, I.47, and subtraction. However, the proofs diverge fundamentally after this point. Heath completes the proof by geometric rectangle identification within the diagram (FK = AD, subtracting AK to get FH = HD, then identifying HD = rect(AB,BH) and FH = sq(AH)). The AI instead takes an algebraic route: it uses 2.3 to decompose rect(CF,FA) into rect(AB,AH) + sq(AH), and 2.2 to decompose sq(AB) into rect(AB,AH) + rect(AB,HB), then equates and subtracts to reach sq(AH) = rect(AB,HB). These are genuinely different backbones from step 4 onward — the AI never establishes Heath's key intermediates FK = AD or FH = HD, and Heath never invokes 2.2 or 2.3. Q2 Case B applies, and Q3 confirms the AI's algebraic path is logically complete and valid, yielding classification D.

### 2.12
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: apply II.4 to the line composed of two segments (one side and the external segment cut off by the perpendicular), add the square on the perpendicular to both sides, then use I.47 twice on the two right triangles formed by the perpendicular to substitute and reach the conclusion. The key intermediate conclusions are identical in both proofs despite different vertex labeling. The AI's extra citations (1.12 for drawing the perpendicular, D1.11 for the obtuse angle definition, P2 for producing a line, CN1 and CN2 for equality operations) are all construction-level, definitional, or common-notion citations that Heath uses implicitly but does not cite explicitly. Since heath_only is empty and ai_only contains only over-citations at a finer granularity level, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 2.13
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification. Both proofs follow the same logical backbone: drop a perpendicular from vertex A to the opposite side BC, apply II.7 to the line BC cut at the foot D, apply I.47 twice to the two right triangles formed (ADB and ADC), then combine via addition and substitution to reach the conclusion. The AI proof differs only in explicitly citing construction references (1.12 for drawing the perpendicular), common notions (CN1, CN2, CN3 for equality manipulations), and definitions (D1.10, D1.11, D1.12, D1.21 for right angles, obtuse angles, acute angles, and acute-angled triangles) that Heath leaves implicit. Since heath_only is empty and all ai_only items are construction props, common notions, and definitions, this is a clear Case A (same backbone, different citation depth), yielding G.

### 2.14
**Category**: Granularity difference
**Jaccard**: 0.214
**Analysis**: Q2 decided this classification. Both proofs follow the identical logical backbone: construct a rectangle equal to the given figure (I.45), extend one side and bisect (creating the semicircle construction), apply II.5 to relate the rectangle to squares, use I.47 (Pythagorean theorem) on triangle GEH, and subtract the common square on GE to conclude that the rectangle equals the square on EH. The AI proof cites 14 references while Heath cites only 3, but the ai_only set consists entirely of construction propositions (1.3, 1.10, 1.46), postulates (P1, P2, P3), common notions (CN1, CN3), and definitions (D1.15, D1.17, D2.1) — all foundational-level citations that Heath uses implicitly without explicit reference. The heath_only set is empty, confirming that the AI covers everything Heath does and more. Since the key intermediate conclusions are identical and the citation difference is purely one of depth (over-citation by the AI of foundational steps), this is a granularity difference.
