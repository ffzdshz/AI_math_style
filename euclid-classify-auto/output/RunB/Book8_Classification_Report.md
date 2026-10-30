# Book 8 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 1 | 8.7 |
| Granularity difference (G) | 15 | 8.2, 8.3, 8.4, 8.8, 8.9, 8.11, 8.12, 8.13, 8.14, 8.16, 8.17, 8.18, 8.20, 8.24, 8.25 |
| Path difference (D) | 11 | 8.1, 8.5, 8.6, 8.10, 8.15, 8.19, 8.21, 8.22, 8.23, 8.26, 8.27 |
| AI proof error (E) | 0 |  |

**Total**: 27 propositions

## Per-Proposition Analysis

### 8.1
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof works by assuming a smaller set in the same ratio, applying ex aequali (7.14) to reduce to the ratio of extremes A:D = E:H, invoking 7.21 to conclude A,D are the least in that ratio, then using 7.20 to derive that A measures E, which contradicts E < A. The AI proof takes a fundamentally different approach: it invokes 7.33 to guarantee the existence of a least set B with the same ratios, then applies 7.20 to show that the least set measures the original with a common multiplier m (so A_i = m*B_i for all i), then uses D7.12 (definition of coprimality) to conclude m must be a unit since it is a common measure of the coprime extremes, yielding A_i = B_i, which contradicts the assumption that the A's are not the least. The key intermediates differ: Heath establishes a ratio equality of extremes and uses the 'primes are least' theorem, while the AI establishes a uniform multiplier relationship and uses the definition of coprimality directly. Both paths are logically valid but arrive at the contradiction through genuinely different intermediate conclusions.

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing terms as products of powers of A and B, showing consecutive terms have ratio A:B, establishing the extremes are prime to each other via 7.22 and 7.27, and concluding minimality via 8.1. The citation differences are all depth-level: the AI's ai_only items (7.33 for reducing to least terms, 7.29 as extra primality support, D7.15 as a definition citation) are over-citations that do not alter the logical structure. Heath's sole heath_only item (7.18) is subsumed by the AI's use of 7.17 alone, since 7.18 reduces to 7.17 via commutativity of multiplication (7.16), and the AI simply reformulates the ratio arguments so that only 7.17 is needed. The key intermediate conclusions are identical in both proofs, making this a same-backbone, different-depth case.

### 8.3
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decides this classification as G (granularity difference). Both proofs share the same logical backbone: (1) identify the two-term least ratio pair and establish coprimality via 7.22, (2) construct the n-term continued proportion via 8.2, (3) show the constructed sequence equals the given sequence (both being least with the same multitude), and (4) conclude coprimality of extremes via 7.27. The citation differences are matters of depth, not path. Heath cites 7.33 to explicitly find the least pair in the ratio, while the AI takes the existence of such a pair for granted (an under-citation). The AI cites 7.20 to argue mutual measurement implies equality of the two least sequences, while Heath states this equality more directly without invoking 7.20. These are citation-depth variations around the same key intermediate conclusions, not different logical routes.

### 8.4
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs share the same key intermediate conclusions: (1) finding LCMs via 7.34 to bridge consecutive ratio pairs, (2) establishing proportional relationships through multiplication, (3) proving minimality via 7.20 and 7.35. The AI cites 7.17 where Heath cites 7.13 and D7.20; the proof-tree containment test confirms this is a depth difference, since Heath's proof of 7.17 explicitly uses 7.13 internally. The AI's additional citation of 7.22 (coprimality of least-ratio pairs) is an over-citation of a fact Heath treats as implicit from the ratios being 'in least numbers.' The AI organizes the proof iteratively (handle two ratios, then extend) rather than Heath's case-based split (E measures K vs. E does not measure K), but this is a presentational choice: the AI's general method (always taking LCM of the last term with the next antecedent) subsumes both of Heath's cases, and the underlying logical backbone of LCM construction, ratio preservation, and minimality proof is the same.

### 8.5
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof constructs least numbers in continued proportion via 8.4, then uses ex aequali (7.14) to link the ratio A:B to the compounded ratio G:K. The AI instead constructs a single intermediate product F = a*d, uses 7.17 and 7.18 to establish A:F = b:d and F:C = a:c respectively, then applies the definition of compounded ratio (D6.5) directly. These represent genuinely different logical backbones: Heath works through least numbers in continued proportion and ex aequali reasoning, while the AI takes a more direct algebraic route through an auxiliary product and the definition of compounded ratio. Both paths are logically complete and valid, making this a path difference.

### 8.6
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 reveals different logical backbones, leading to classification via Q3. Heath's proof takes the least numbers in the same ratio as a subsequence (e.g., A, B, C mapped to F, G, H via VII.33), then uses ex aequali (VII.14) to relate the ratio of non-adjacent terms (A:C = F:H), transfers the non-measuring property via D7.20, and concludes from VIII.3 that F, H are coprime. The AI takes a fundamentally different path: it first extracts the basic ratio e:f (VII.33), proves e is not unity via VII.20 and D7.3, then for any subsequence A_i through A_j uses VIII.2 to explicitly construct the least continued proportion, applies VIII.3 to show the extremes e^(j-i) and f^(j-i) are coprime, uses VII.20 to express A_i and A_j as coprime-coefficient multiples of a common factor m, and derives a contradiction from assuming divisibility. The AI's path through 8.2 (constructing least continued proportions) and its explicit power-based argument replaces Heath's ex aequali approach entirely. Both proofs are logically complete, so Q3 confirms D.

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs use identical proof-by-contradiction structures relying solely on Proposition 8.6. The key intermediate conclusion in both is that if the first number does not measure the second, then by 8.6 no number in the sequence measures any other, which contradicts the hypothesis that the first measures the last. The citation sets are identical (both cite only 8.6), giving Jaccard similarity of 1.0, and the logical backbones match exactly, satisfying the perfect match criteria.

### 8.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs share the same backbone of key intermediate conclusions: (1) find least numbers in continued proportion with the given ratio, (2) show extremes are prime via 8.3, (3) use 7.21 and 7.20 to establish that the extremes measure D and E the same number of times, (4) construct intermediate terms by multiplying the least proportionals by that common factor, and (5) verify the resulting sequence is in continued proportion. The citation differences reflect substitutions at the same logical positions: the AI uses 8.2 to explicitly construct least continued proportionals where Heath uses VII.33 on the full sequence, the AI uses 7.17 to show multiplication preserves ratios where Heath invokes D7.20, and the AI reasons directly about extreme ratios of continued proportions where Heath cites VII.14 (ex aequali). These are citation-depth differences for the same underlying logical steps, not different proof paths.

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification as Granularity difference (G). Both proofs share the same logical backbone: reduce the ratio A:C1 to least terms, use 8.2 to construct the least numbers in continued proportion as powers of those least terms, identify A and B with the extreme powers via uniqueness of least numbers (8.1), then construct the geometric sequences 1, p, p^2, ..., p^(k+1)=A and similarly for B. The AI explicitly cites 7.33 (to find least terms), 7.22 (to show they are prime), and 8.3 (to confirm extremes of least sequence are prime), while Heath handles these steps implicitly or within the internal proofs of 8.2 (which itself uses 7.22). The proof-tree containment test confirms that 7.22 appears inside Heath's proof of 8.2, and both 7.33 and 7.22 appear inside Heath's proof of 8.3. Heath's sole unique citation D7.20 is a definition used to justify proportionality statements that the AI handles through explicit power notation without citing the definition. The key intermediate conclusions are identical in both proofs, differing only in citation depth.

### 8.10
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Heath's proof explicitly constructs intermediate numbers H=D*F, K=D*H, L=F*H and directly verifies the continued proportion A, K, L, B using VII.17 and VII.18 in a computational, step-by-step manner. The AI proof takes a fundamentally different route: it characterizes A and B as (m+1)-th powers of their respective geometric-progression bases C1 and D1, then invokes 8.2 to find least numbers in continued proportion with ratio C1:D1, and applies 8.8 to transfer the existence of m intermediate terms to A and B. These are genuinely different logical backbones — Heath builds the intermediates by hand while the AI leverages higher-level existence results (8.2, 8.8). The AI's path is logically valid: 8.2 correctly produces continued proportions whose extremes are powers of the base ratio elements, and 8.8 legitimately transfers the count of intermediates to numbers in the same ratio. Under Q3, the AI's different path passes the hardened 1(b) standard with no unsupported assertions, circular citations, or invalid inferences, yielding classification D.

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct the product of the two sides of the square numbers, use 7.17 to establish the ratio of the first square to the product equals the ratio of the sides, use 7.18 to establish the ratio of the product to the second square equals the same ratio of the sides, conclude the product is a mean proportional, then apply D5.9 for the duplicate ratio. The AI proof additionally cites CN1 (to explicitly justify equating the two ratio expressions), D7.15 (definition of multiplication), and D7.18 (definition of square number), all of which are foundational items Heath uses implicitly. Since heath_only is empty and ai_only contains only Common Notions and Definitions, this is a clear Case A granularity difference with the AI over-citing foundational material.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) the ratio of the sides equals the ratio between corresponding products (a^2:ab = ab:b^2), (2) the four numbers a^3, a^2b, ab^2, b^3 are in continued proportion, and (3) the triplicate ratio follows from V.Def.10. The AI reaches conclusion (1) by citing 8.11 as a packaged result, while Heath derives it inline using VII.17 and VII.18 directly; the underlying geometric fact is identical. The ai_only set consists of definitions (D7.15, D7.18, D7.19), a common notion (CN1), commutativity (7.16), and 8.11 — all representing either over-citation of foundational items or a different citation depth for the same logical step. Since heath_only is empty, every citation Heath uses is also used by the AI. The backbones match with differing granularity, yielding G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing intermediate terms to form continued proportions among the squares and cubes, showing these continued proportions share a common ratio (since A:B = B:C), and applying ex aequali (7.14) to conclude D:E = E:F and G:H = H:K. The ai_only citations 7.17 and 7.18 are the explicit multiplication-proportion results that Heath uses implicitly through his phrase 'in manner similar to the foregoing' (referring back to 8.12, where 7.17 and 7.18 are cited explicitly). The AI spells out each application of 7.17 and 7.18 step by step, while Heath compresses these into a back-reference. Since heath_only is empty and the ai_only items represent over-citation of the same underlying reasoning, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 8.14
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same backbone: they establish a continued proportion via 8.11, apply 8.7 to derive divisibility of the mean term, and then use the ratio relationship to conclude divisibility of the sides (forward direction) or squares (converse). The citation differences reflect depth, not path: Heath cites D7.20 (definition of proportional numbers) to move directly from a ratio equality and a divisibility to the conclusion, while the AI explicitly cites 7.17 (products of a number multiplying two numbers have the same ratio as the multiplied numbers) and 7.20 (least numbers in ratio measure proportional numbers equally) to spell out the same inferential step at a finer grain. The AI's additional citation of D7.3 is likewise a definitional over-citation. The key intermediate conclusions are identical in both proofs at every logical position, making this a same-backbone, different-depth case.

### 8.15
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determines the classification. While Part (i) of the AI proof follows a similar backbone to Heath (using 8.12 for mean proportionals, 8.7 for divisibility in continued proportion, then establishing the ratio to conclude side divisibility), Part (ii) takes a fundamentally different path. Heath re-uses the same continued proportion construction (A, H, K, B in ratio C:D) for both directions, applying the converse reasoning with D7.20. The AI instead invokes 8.14 (the square analogue) to establish that a^2 measures b^2, then builds a divisibility chain using 7.17 and 7.20: first showing a^3 measures a^2*b (from a measuring b), then showing a^2*b measures b^3 (from a^2 measuring b^2), and concluding by transitivity that a^3 measures b^3. This is a genuinely different logical backbone for the converse direction, yielding different key intermediate conclusions (using the square result as a stepping stone rather than the continued proportion). The AI's path is logically complete and valid under Q3, so the classification is D.

### 8.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Both the AI and Heath proofs establish the same two-part contrapositive argument: (1) if the square does not measure the square, assume the side measures the side, then by 8.14 the square measures the square, contradiction; (2) if the side does not measure the side, assume the square measures the square, then by 8.14 the side measures the side, contradiction. The key intermediate conclusions and logical backbone are identical. The only citation difference is that the AI explicitly cites D7.18 (the definition of square numbers) in its setup, while Heath leaves this implicit. Since ai_used and heath_refs differ only by this definitional over-citation, this is a granularity difference (G) rather than a perfect match (P) or a path difference (D).

### 8.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs share the same logical backbone: a two-part contrapositive argument where each direction is proved by contradiction using 8.15. In Part 1, both assume the side measures the side, derive via 8.15 that the cube measures the cube, and reach a contradiction. In Part 2, both assume the cube measures the cube, derive via 8.15 that the side measures the side, and reach a contradiction. The only difference is that the AI explicitly cites D7.19 (definition of cube number) when setting up notation, while Heath does not cite any definition. Since D7.19 is a definitional citation representing over-citation rather than a substantive intermediate conclusion, this is a citation-depth difference with the same backbone, yielding G. The citation sets are not identical (ai_used includes D7.19 while heath_refs does not), so P is ruled out.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they set up similar plane numbers with proportional sides, construct a mean proportional number (Heath constructs G = D*E; the AI constructs M = c*f and uses 7.19 to show c*f = d*e, which is the same number), apply 7.17 twice to establish the continued proportion A:mean::mean:B, and then invoke V.Def.9 for the duplicate ratio. The difference lies in how a sub-step is justified: Heath uses 7.13 (alternation) to rearrange the proportion c:d = e:f into c:e = d:f, while the AI uses 7.19 (cross-multiplication property) to establish c*f = d*e directly, bypassing the need for alternation. The ai_only citation D7.16 is simply the definition of plane number (over-citation). Since the key intermediate conclusions are identical and only the justification technique for one sub-step differs, this is a same-backbone, different-depth case under Q2 Case A.

### 8.19
**Category**: Path difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Heath's proof constructs intermediate numbers K=CD and L=FG as similar plane numbers, applies 8.18 to find their mean proportional M=DF, uses 7.13 for alternation, then builds N=EM and O=HM to establish the continued proportion A,N,O,B. The AI proof takes a genuinely different path: it directly constructs P=a*e*c and Q=d*e*c, then uses 7.17 and 7.18 to show A:P=b:e, P:Q=a:d, and Q:B=c:f. Since the sides are proportional by similarity (D7.21), all three ratios are equal, giving continued proportion A,P,Q,B immediately without invoking 8.18 or 7.13. The key intermediate conclusions differ substantially: Heath routes through similar plane numbers and their mean proportional, while the AI constructs entirely different intermediates that avoid the plane-number machinery. Both paths are logically valid, making this a path difference.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they take D, E as the least numbers in the ratio A:C via 7.33, use 7.20 to decompose A and B into products (A = F*D, B = G*E), establish that A and B are plane numbers, and then show that D:E = F:G to conclude the sides are proportional and hence A, B are similar plane numbers. The citation difference arises because the AI uses 7.19 (product equality implies proportionality) to establish D:E = F:G directly from F*E = G*D, whereas Heath uses 7.17 twice to establish D:E = A:C and F:G = C:B, then chains these and applies 7.13 (alternation). Since 7.17 appears inside Heath's own proof of 7.19, this satisfies the proof-tree containment test: the AI cites 7.19 as a unit while Heath re-derives its internals inline. The AI's additional citations of 7.22, D7.16, and D7.21 are either explicit statements of facts Heath uses implicitly or supporting lemmas not strictly needed. This is a citation-depth difference with the same backbone, yielding G.

### 8.21
**Category**: Path difference
**Jaccard**: 0.308
**Analysis**: Q2 determined the classification. Heath's proof works through three least numbers in continued proportion (VIII.2), proves their extremes are prime (VIII.3), applies VIII.20 to conclude the extremes are similar plane numbers with identifiable sides, then uses ex aequali (VII.14) and VII.21 to establish the measurement relations, finally building the solid decomposition from plane-number sides. The AI takes a fundamentally different route: it works with the least four numbers in continued proportion e^3, e^2f, ef^2, f^3 (VIII.1, VIII.2), directly deduces A = ke^3 and B = kf^3 via VII.20, and factors these into sides (e, e, ke) and (f, f, kf) to show both are solid numbers with proportional sides. The backbones differ substantially: Heath relies on VIII.20 (similar plane numbers from one mean proportional), VIII.3 (prime extremes), VII.14 (ex aequali), and VII.21 (primes are least), none of which the AI uses. The AI instead relies on VIII.1 (least in continued proportion), VII.15, VII.17, and the explicit cubic structure. Since the AI's different path is logically complete and valid, this is a path difference.

### 8.22
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof pivots on a single structural result (8.20) that if one mean proportional falls between two numbers then they are similar plane numbers, and since A is square, C must also be square. The AI instead takes a direct algebraic route: using 7.19 to establish A*C = B*B from the continued proportion, then applying 8.14 to conclude that a (the side of the square A) divides B, and finally algebraically deriving C = c*c. The key intermediate conclusions are entirely different: Heath argues through 'A and C are similar plane numbers' while the AI argues through 'A*C = B*B' and 'a divides B'. The citation sets are completely disjoint (Jaccard = 0.0), confirming the path divergence. The AI's alternative route is logically sound and complete, so the classification is D (path difference).

### 8.23
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof has a two-step backbone: (1) since A and D have two mean proportionals between them, they are similar solid numbers by 8.21, and (2) since A is a cube and similar solid numbers to a cube are cubes, D is also cube. The AI proof takes a fundamentally different path: it finds the least numbers p, q in the ratio A:D (7.33, 7.22), uses 8.8 and 8.9 to show that continued proportions from unit to p and from unit to q exist, proves p and q are each cubes via arithmetic on those proportions, then uses 7.20 to establish that p measures A and q measures D the same number of times, applies 8.15 to show the cube root relationship transfers, derives that the common multiplier m is itself a cube, and concludes D = m*q is a product of two cubes and hence a cube. The Jaccard similarity of 0.0 (zero overlap between citation sets) reflects this genuine path divergence. The AI's proof is logically complete and valid throughout, establishing the conclusion through a longer but sound chain of number-theoretic reasoning rather than Heath's concise appeal to similar solid numbers.

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish that one mean proportional falls between the two given square numbers, (2) apply 8.8 to transfer the mean proportional relationship to A and B, (3) apply 8.22 to conclude B is square since A is square and A, E, B are in continued proportion. The sole difference is that Heath cites 8.18 (between two similar plane numbers there is one mean proportional) after noting that squares are similar plane numbers, while the AI cites 8.11 (between two square numbers there is one mean proportional), which is the specialization of 8.18 to square numbers. The AI also cites D7.18 (a definition), which Heath leaves implicit. These are citation-depth differences, not backbone differences, since the key intermediate conclusion — that a mean proportional exists between the two square numbers — is identical in both proofs.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that two mean proportionals exist between the given cube numbers C and D, (2) apply 8.8 to transfer those mean proportionals to A and B which have the same ratio, and (3) apply 8.23 to conclude B is cube since A is cube and four numbers are in continued proportion. The sole difference is how step (1) is justified: Heath cites 8.19 (mean proportionals between similar solid numbers) after noting that cube numbers are similar solids, while the AI cites 8.12 (mean proportionals between cube numbers) which applies directly. These are two independent propositions reaching the same intermediate conclusion, with 8.12 being a more specialized result for cubes and 8.19 being the general result for similar solids. Since the key intermediate conclusions are identical at every logical position and only the citation supporting one step differs, this is a citation-depth difference (Case A in Q2), yielding classification G.

### 8.26
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Heath's proof finds the least numbers D, E, F in the same ratio as A, C, B (using 7.33/8.2), then observes the extremes D, F are square (8.2), so A:B is a ratio of squares. The AI takes a fundamentally different route: it extracts the sides a, b from the similar plane numbers, constructs the explicit squares a^2 and b^2, uses 8.11 to establish a continued proportion a^2:(a*b):(b^2), then applies ex aequali (7.14) to conclude A:B = a^2:b^2. These are genuinely different backbones — Heath works with abstract least numbers in ratio while the AI works with concrete side-derived squares — so Q2 Case B applies. The AI's path is logically complete under Q3, with every step properly cited and sound, yielding category D.

### 8.27
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs share the initial step of using 8.19 to establish two mean proportionals between the similar solid numbers A and B, but they diverge completely after that. Heath's proof finds the least numbers in the same ratio (via 7.33/8.2) and shows their extremes are cubes (via 8.2), concluding that A:B equals a cube-to-cube ratio. The AI proof instead constructs explicit cube numbers a^3 and d^3 from the sides of the similar solid numbers, uses 8.12 to establish that between these cubes also fall two mean proportionals with the same common ratio a:d, then applies ex aequali (5.22) to conclude A:B = a^3:d^3, which is directly a cube-to-cube ratio. These are genuinely different logical backbones: Heath works through reduction to least numbers, while the AI works through explicit construction of cubes with matching continued proportions. The AI's path is logically complete and valid, yielding classification D.
