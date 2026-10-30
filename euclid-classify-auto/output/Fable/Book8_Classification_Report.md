# Book 8 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 3 | 8.3, 8.7, 8.16 |
| Granularity difference (G) | 21 | 8.1, 8.2, 8.4, 8.6, 8.8, 8.9, 8.10, 8.11, 8.12, 8.13, 8.14, 8.15, 8.17, 8.18, 8.19, 8.20, 8.23, 8.24, 8.25, 8.26, 8.27 |
| Path difference (D) | 3 | 8.5, 8.21, 8.22 |
| AI proof error (E) | 0 |  |

**Total**: 27 propositions

## Per-Proposition Analysis

### 8.1
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume for contradiction that smaller numbers E, F, G, H exist in the same ratio as A, B, C, D; apply ex aequali (7.14) to obtain A:D = E:H; invoke the fact that prime numbers are least (7.21); conclude via 7.20 that A measures E, contradicting E < A. The AI proof adds explicit citations to definitions D7.12 (prime to one another) and D7.3 (part/measure), which Heath uses implicitly without citation. Since the key intermediate conclusions are identical and the only differences are additional definition citations by the AI, this is a citation-depth difference under Q2 Case A, yielding G.

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: they construct the same products (C, D, E, F, G, H, K) from A and B, establish each consecutive ratio equals A:B using VII.17 and VII.18 in the same logical positions, and prove minimality through the same chain (A,B coprime by VII.22, extremes coprime by VII.27, least by VIII.1). The AI proof adds two over-citations not in Heath: 7.33 to explicitly justify finding A, B as the least numbers in the given ratio (Heath simply assumes this), and D7.15 to cite the definition of multiplication for the construction steps (Heath takes this as implicit). Since the backbones match and the only differences are additional citation depth in the AI proof, Case A of Q2 holds, yielding G.

### 8.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (all citations 7.22, 7.27, 7.33, 8.2 precede 8.3). Q1 found the AI proof logically complete with no defects. Q2 confirmed both proofs share the same key intermediate conclusions: taking the least pair E, F in the common ratio via 7.33, establishing their coprimality via 7.22, building up sequences of least numbers via 8.2, cascading coprimality of extremes via 7.27, and concluding via uniqueness of least sets that A=L and D=O. The citation sets are identical (ai_used = heath_refs = {7.22, 7.27, 7.33, 8.2}), yielding Jaccard 1.0, so the perfect match check assigns category P.

### 8.4
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same two-case structure (E measures K vs. E does not measure K) and the same logical backbone: construct G as LCM(B,C) via 7.34, establish the ratio equalities A:B = H:G and C:D = G:K, extend by one more ratio, then prove minimality by contradiction showing G must measure a number smaller than itself. The AI's two extra citations (7.17 and D7.3) reflect citation-depth differences, not backbone divergence: the AI uses 7.17 directly to establish ratio equalities where Heath uses the combination of VII. Def. 20 and VII. 13, and the AI explicitly cites definition D7.3 for divisibility claims that Heath leaves implicit. Since heath_only is empty and the key intermediate conclusions are identical, this is Case A of Q2, yielding G. The citation sets are not identical (ai_used is a proper superset of heath_refs), so P does not apply.

### 8.5
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs construct L = D*E and establish the same two key intermediate ratio equalities (C:E = A:L and D:F = L:B), but they diverge in how they combine these into the compound ratio conclusion. Heath introduces auxiliary least numbers G, H, K via 8.4 and uses ex aequali (7.14) to establish G:K = A:B before concluding the compound ratio. The AI avoids this auxiliary construction entirely and instead directly applies the definition of compound ratio (D6.5) to the chain A, L, B. Since the heath_only propositions 7.14 and 8.4 are substantive theorems absent from the AI proof and not contained within any proposition the AI cites, Case A of Q2 fails. This yields Case B (different backbone), and Q3 confirms the AI path is logically complete (7.17 and 7.18 correctly establish the ratio equalities, and D6.5 validly concludes the compound ratio), giving classification D.

### 8.6
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: taking least numbers in the same ratio via VII.33, establishing coprimality of extremes via VIII.3, applying ex aequali via VII.14, and transferring the 'not measuring' relation via Def. 20 to reach the conclusion. The AI proof is more explicit, separately handling consecutive and non-consecutive cases and citing definitions (D7.3 for 'part', D7.12 for coprimality, D7.2 for number) that Heath leaves implicit. Since heath_only is empty and ai_only contains only definitions, the AI over-cites at the definitional level while following the identical argumentative path, making this a clear Case A granularity difference.

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (8.6 < 8.7). Both proofs employ an identical proof-by-contradiction strategy: assume A does not measure B, invoke 8.6 to conclude that no number in the continued proportion measures any other, then note the contradiction with the hypothesis that A measures D. The AI and Heath citation sets are identical ({8.6}), yielding Jaccard 1.0, and the key intermediate conclusions match exactly, so the perfect match check assigns category P.

### 8.8
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take the least numbers G, H, K, L in the same ratio as A, C, D, B (7.33), establish that the extremes G, L are prime to one another (8.3), apply ex aequali to get A:B = G:L (7.14), equate G:L = E:F, use the leastness of G, L (7.21) and the measurement property (7.20) to find that G and L measure E and F the same number of times, construct intermediates M and N by applying that same multiplicity to H and K, and conclude that E, M, N, F are in continued proportion. The citation differences are purely at the level of definitional and low-level justification: the AI explicitly cites 7.17 (ratio preservation under multiplication) and D7.15 (definition of multiplication) to justify the ratio equalities in the construction step, whereas Heath invokes D7.20 (definition of proportionality) for the same purpose. These are different ways of articulating the same underlying reasoning at the same logical position, making this a granularity difference rather than a path difference.

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: they take the least numbers F, G in the common ratio, construct four numbers M, N, O, P in continued proportion via VIII.2, show these equal A, C, D, B respectively using VIII.1, then build the proportion chains E:F = F:H = H:A and E:G = G:L = L:B using the definition of multiplication and VII Def 20. The AI's three extra citations (7.33 for explicitly finding the least ratio pair, D7.15 for the definition of multiplication, D7.2 for the definition of unit) all represent over-citation: the AI makes explicit definitional and foundational steps that Heath leaves implicit. Heath's proof contains no citations absent from the AI (heath_only is empty). Since the key intermediate conclusions are identical and only citation depth differs, this is a granularity difference.

### 8.10
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share an identical logical backbone: they construct E=D*D, A=D*E, G=F*F, B=F*G, then H=D*F, K=D*H, L=F*H, and use VII.17 and VII.18 repeatedly to show that all ratios A:K, K:L, L:B equal D:F, establishing A, K, L, B in continued proportion. The AI proof adds explicit citations of D7.15 (definition of multiplication) and D7.2 (definition of number as composed of units), which Heath invokes implicitly without naming. Since the key intermediate conclusions are identical and the only difference is the AI's additional definitional citations, this is a granularity difference (Case A of Q2).

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing E as the product of sides C and D, establishing A:E = C:D via 7.17, E:B = C:D via 7.18, deriving transitivity to get A:E = E:B, and applying D5.9 for the duplicate ratio. The AI adds two over-citations not in Heath: 5.11 (transitivity of equal ratios, which Heath applies without explicit citation) and D7.18 (definition of square number, which Heath invokes implicitly). Since heath_only is empty and both ai_only items are explicit citations for steps present in both proofs, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs construct the same intermediate numbers E, F, G, H, K from the sides C, D of cubes A, B, and establish the identical chain of proportions (C:D = E:F, C:D = F:G, A:H = C:D, H:K = C:D, K:B = C:D) using VII.17 and VII.18, concluding that A, H, K, B are in continued proportion and that A:B is the triplicate ratio of C:D via V. Def. 10. The key intermediate conclusions are identical in both proofs. The AI over-cites by explicitly invoking 5.11 for transitivity of equal ratios (which Heath applies implicitly in substitution steps) and D7.19 for the definition of cube number (which Heath uses without citation). Since heath_only is empty and the ai_only items are a definition and a transitivity lemma that Heath applies without citation, this is a citation-depth difference with the same backbone, yielding G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing intermediate products between the original numbers and their squares/cubes, establishing that consecutive sequences are in continued proportion in the ratio A:B or B:C, and then applying ex aequali (7.14) to conclude that the squares and cubes are each in continued proportion. The AI proof explicitly cites 7.17 and 7.18 at each step to justify ratio relationships, while Heath uses these same results implicitly under the phrase 'in manner similar to the foregoing, we can prove' without explicit citation. Since heath_only is empty and ai_only contains only 7.17 and 7.18 (propositions that Heath applies but does not cite), this is a citation-depth difference with the same backbone, yielding G.

### 8.14
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct E = C*D, establish that A, E, B are in continued proportion with ratio C:D, then for Part 1 use 8.7 to show A measures E and the ratio relationship to conclude C measures D, and for Part 2 reverse the argument. The sole substantive divergence is citation depth: Heath cites 8.11 as a unit to establish the continued proportion, while the AI re-derives it from 7.17 and 7.18, which are the internal components of Heath's own proof of 8.11 (proof-tree containment test satisfied). The additional ai_only items D7.18 and D7.3 are definitional over-citations. Since the key intermediate conclusions are identical and only citation granularity differs, the classification is G.

### 8.15
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they construct the same products (E, F, G, H, K), establish that A, H, K, B are in continued proportion with common ratio C:D, then for the first direction apply 8.7 to get A|H from A|B and use the proportion (D7.20) to conclude C|D, and for the second direction reverse the argument through the proportion chain. The only difference is citation depth: Heath cites 8.11 and 8.12 as packaged results to establish the continued proportion, while the AI re-derives the same proportion directly from the more primitive 7.17 and 7.18, which are exactly the propositions used inside Heath's proofs of 8.11 and 8.12. The remaining ai_only items (D7.19, D7.3) are definitions that the AI cites explicitly where Heath leaves them implicit. This satisfies the proof-tree containment test for Case A, yielding G.

### 8.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (8.14 < 8.16). Both proofs handle the two required cases of this biconditional contrapositive proposition identically: each case proceeds by contradiction, assuming the negation and applying 8.14 to derive a contradiction. The AI proof covers case 1 (A not measuring B implies C not measuring D) in Steps 2-4 and case 2 (C not measuring D implies A not measuring B) in Steps 5-7, matching Heath's structure exactly. The citation sets are identical (both cite only 8.14), giving Jaccard similarity of 1.0, and the key intermediate conclusions are the same, so this is a perfect match.

### 8.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same two contrapositive cases: (1) if cube A does not measure cube B then side C does not measure side D, and (2) if side C does not measure side D then cube A does not measure cube B. Both use proof by contradiction invoking 8.15 in each case. The key intermediate conclusions are identical. The only citation difference is that the AI explicitly cites D7.19 (the definition of cube numbers) while Heath does not, which is a minor over-citation of a definition. This is Case A in Q2: same backbone, different citation depth, yielding G.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: they establish similarity via D7.21, apply alternation via 7.13, construct G = D*E, use 7.17 twice to derive the continued proportion A:G :: G:B, and conclude with the duplicate ratio via D5.9. The AI's two extra citations (5.11 and D7.16) are over-citations that make explicit what Heath leaves implicit: 5.11 formalizes the transitivity of equal ratios where Heath simply writes 'therefore also,' and D7.16 cites the definition of plane number where Heath invokes it without citation. Since the key intermediate conclusions are identical and the only differences are in citation depth, this is a granularity difference.

### 8.19
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: the equality of corresponding side ratios (C:F=D:G=E:H), the continuous proportion K,M,L in ratio C:F, the construction of N=E*M and O=H*M yielding A,N,O,B continuously proportional, and the triplicate ratio conclusion. The sole substantive citation difference is that Heath invokes 8.18 to obtain the mean proportional M between similar plane numbers K and L, while the AI constructs M=F*D directly and proves K:M=M:L inline using 7.17 and 7.18. The proof-tree containment test confirms that 8.18's own proof uses VII.17 and VII.13 to establish exactly the same result, so the AI is re-deriving 8.18's internals rather than taking a different path. The ai_only item D7.17 is a definition (minor over-citation). This is Case A of Q2: same backbone, different citation depth.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: A is plane with sides D and F, B is plane with sides E and G, and the sides are proportional, so A and B are similar plane numbers. The substantive citation difference is that the AI uses 7.19 (if products from first-fourth and second-third are equal, the four numbers are proportional) to establish F:G = D:E in one step, whereas Heath derives the same proportionality via 7.17 (twice) and 7.13 (alternation). The proof-tree containment test confirms this is a depth difference: Heath's proof of 7.19 cites 7.17, and Heath's proof of 7.17 cites 7.13, so both heath_only items (7.13, 7.17) lie inside the proof tree of the AI's citation 7.19. The AI additionally cites definitions D7.15, D7.16, D7.20, and D7.21 that Heath invokes implicitly, which is over-citation. Since the backbone is the same and all citation differences reduce to depth, this is Granularity difference (G).

### 8.21
**Category**: Path difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification. Heath's proof finds the least triple E, F, G via VIII.2, shows their extremes coprime via VIII.3, and then applies VIII.20 to decompose E, G as similar plane numbers with distinct sides H,K and L,M, yielding solids A = N*H*K and B = O*L*M. The AI takes a fundamentally different construction: it finds the least pair H, K in ratio A:C (7.33), builds E = H^2, F = HK, G = K^2 directly, proves coprimality of E, G through 7.22 and 7.27, and decomposes A and B as solids with sides (H, H, N) and (K, K, O). The AI bypasses 8.2, 8.3, and 8.20 entirely, replacing them with a direct square-based construction that avoids the similar-plane-numbers intermediate conclusion. Since these represent genuinely different key intermediate conclusions and the AI's chain from premises to conclusion is logically complete and sound, the classification is D.

### 8.22
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses VIII.20 to establish that A and C are similar plane numbers (since B is one mean proportional between them), then immediately concludes that since A is square, C must also be square. The AI takes a completely different route: it decomposes A as D*D, derives A*C = B*B from the continued proportion via 7.19, applies 8.14 to conclude D divides B, then constructs B = D*E and uses ratio manipulation (7.17, 7.18) and 5.9 to show C = E*E. The key intermediate conclusions differ entirely -- Heath's backbone pivots on similarity of plane numbers, while the AI's pivots on divisibility of sides and direct algebraic reconstruction. The Jaccard similarity is 0.0 with completely disjoint citation sets, confirming a genuine path divergence. The AI proof is logically complete with every step explicitly justified, so Q3(b) holds and the classification is D.

### 8.23
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: B and C are two mean proportionals between A and D, so by 8.21 A and D are similar solid numbers, and since A is cube D must also be cube. The AI proof explicitly cites definitions D7.19 (cube as product of three equal factors), D7.21 (similar solids have proportional sides), and D7.20 (equal ratios imply equal parts) to unpack the final inference that Heath leaves implicit in the single sentence 'But A is cube; therefore D is also cube.' Since ai_only consists entirely of definitions and heath_only is empty, this is a citation-depth difference with the same key intermediate conclusions, yielding G.

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) one mean proportional falls between the square numbers C and D, (2) since A:B = C:D, one mean proportional also falls between A and B (8.8), (3) since A is square and has a mean proportional to B, B is also square (8.22). The sole difference is the citation for step 1: Heath cites 8.18 (between two similar plane numbers there is one mean proportional) after noting squares are similar plane numbers, while the AI cites 8.11 (between two square numbers there is one mean proportional), which applies directly to squares without going through the more general similar-plane-numbers result. Since the underlying fact is the same at the same logical position and the proofs differ only in which proposition justifies that step, this is Case A of Q2, a citation-depth difference yielding G.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) two mean proportional numbers fall between the cube numbers C and D, (2) by 8.8, two mean proportionals also fall between A and B, and (3) by 8.23, since A, E, F, B are in continued proportion and A is cube, B is cube. The sole difference is the justification for step (1): Heath observes that cubes are similar solid numbers and invokes the general result 8.19, while the AI directly applies the cube-specific result 8.12. Since the underlying fact established at the same logical position is identical in both proofs, this is Case A of Q2, a citation-depth difference yielding G.

### 8.26
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish a mean proportional C between similar plane numbers A, B via 8.18, (2) find the least numbers D, E, F in continued proportion with the same ratio, (3) show D and F are square via 8.2, and (4) conclude A:B = D:F is a ratio of square numbers. The citation differences are purely about depth: Heath cites 7.33 for finding least numbers in a given ratio, while the AI uses 8.2 directly for least numbers in continued proportion; conversely, the AI explicitly cites 7.14 (ex aequali) to establish A:B = D:F, while Heath states that proportion without explicit citation. Since the key intermediate conclusions are identical and only the citation granularity differs, this is Case A of Q2, yielding G.

### 8.27
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) since A, B are similar solid numbers, two mean proportionals C, D fall between them by 8.19; (2) the least numbers in that continued proportion have cube extremes by 8.2; (3) the ratio of those cube extremes equals A:B, so A:B is a cube-to-cube ratio. The AI proof adds explicit citations for 7.14 (ex aequali reasoning that Heath leaves implicit) and D7.19 (definition of cube number), but these are over-citations making implicit steps explicit rather than introducing a different argumentative path. Heath_only is empty, confirming no substantive step is missing from the AI proof. This is Case A of Q2: same backbone, different citation depth.
