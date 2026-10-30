# Book 8 — Classification Report (GPT)

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
