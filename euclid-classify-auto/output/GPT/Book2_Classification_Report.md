# Book 2 — Classification Report (GPT)

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
