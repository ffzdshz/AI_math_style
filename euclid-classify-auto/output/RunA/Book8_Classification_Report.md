# Book 8 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 8.7, 8.17 |
| Granularity difference (G) | 16 | 8.1, 8.2, 8.3, 8.6, 8.9, 8.11, 8.12, 8.13, 8.15, 8.16, 8.18, 8.20, 8.22, 8.23, 8.24, 8.25 |
| Path difference (D) | 9 | 8.4, 8.5, 8.8, 8.10, 8.14, 8.19, 8.21, 8.26, 8.27 |
| AI proof error (E) | 0 |  |

**Total**: 27 propositions

## Per-Proposition Analysis

### 8.1
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume smaller numbers in the same continued proportion, derive via ex aequali (7.14) that the ratio of extremes is the same, apply 7.21 to conclude the original extremes are least in that ratio, then use 7.20 to show the first extreme measures the corresponding smaller number, yielding a contradiction. The AI proof extends the argument further by showing all terms must be equal (Steps 7-8), but this is additional detail atop the same backbone. The only citation difference is D7.20 (a definition of proportionality) in ai_only, which the AI cites explicitly in Step 8 when Heath leaves it implicit. Since the key intermediate conclusions are identical and the citation difference is a single definition, this is a same-backbone, different-depth case — Granularity difference (G).

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing a sequence of products, showing each consecutive pair has ratio A:B via 7.17 and 7.18, establishing that A and B are prime to one another via 7.22, using 7.27 to show the extremes of the sequence are prime to one another, and concluding by 8.1 that the sequence is the least in continued proportion with the given ratio. The only citation difference is that the AI explicitly cites 7.33 to justify obtaining A and B as the least numbers in the given ratio, whereas Heath simply states this as the setup without citation. This is a classic over-citation at the construction/setup level, making this a Case A same-backbone granularity difference. The AI also generalizes to n terms using algebraic notation rather than Heath's specific four-term example, but this is a presentational difference rather than a backbone difference.

### 8.3
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: The forward dependency gate passed (all citations are from Book 7 or earlier in Book 8). Q1 found no logical errors: the AI proof follows a clear chain from taking e,f as the least numbers in the ratio (7.33), showing they are prime (7.22), building the least continued proportion via 8.2 to get extremes e^(n-1) and f^(n-1), applying 7.27 to show these powers are prime, and identifying them with the original extremes by uniqueness. Q2 determined that both proofs share the same backbone of key intermediate conclusions: (1) take the least pair in the ratio, (2) show that pair is coprime, (3) build up to the full sequence via 8.2, (4) show the extremes are coprime via 7.27, (5) identify with the original sequence by uniqueness. The only citation difference is that the AI additionally cites definitions D7.12 and D7.20, which are non-substantive over-citations of definitions. Since the backbones match but the citation sets differ by these extra definitions, this is a granularity difference (G).

### 8.4
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Heath's proof constructs the continued proportion using LCM (7.34) as the linking mechanism between consecutive ratios, establishing proportionality via 7.13 and D7.20, and requires a two-case split (whether E measures K or not), with minimality proved via 7.20 and 7.35. The AI proof takes a fundamentally different approach: it constructs intermediate sequences by forming products of terms (using 7.17 and 7.18 for ratio properties of products) and then reduces to least terms using 7.33, avoiding the case split entirely. The AI's construction via multiplication followed by reduction to least numbers is a genuinely different logical backbone from Heath's LCM-based construction. Since both proofs are logically complete but argue through different key intermediate conclusions, the classification is D (path difference).

### 8.5
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 determined the classification. Heath's proof uses 8.4 to construct least numbers G, H, K in continued proportion with the given ratios, introduces an auxiliary product L = D*E, establishes A:L = C:E and L:B = D:F via VII.17, and then combines them via ex aequali (VII.14) to reach A:B = G:K. The AI proof takes a fundamentally different route: it directly constructs an intermediate number E = c*b, shows A:E = a:c via 7.18 and E:C = b:d via 7.17, and then invokes the definition of compounded ratio (D6.5) to conclude. The AI never needs least numbers in continued proportion (8.4) or ex aequali (7.14); Heath never uses 7.18 or the definition of compounded ratio explicitly. These are genuinely different logical backbones, not merely different citation depths of the same argument. The AI's path is logically valid under Q3, so the classification is D.

### 8.6
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) take the least numbers in the same ratio as the continued proportion, (2) show the first of these least numbers is not a unit (since A does not measure B), (3) use VIII.3 to establish coprimality of the extremes of the least continued proportion, (4) apply VII.14 (ex aequali) to transfer the ratio, and (5) derive a contradiction by showing the first least number would have to be 1. The AI proof is more explicit, separately handling consecutive and non-consecutive terms and citing auxiliary results (7.20, 7.21, 7.22 for properties of least ratios and coprimality, 8.2 for constructing the least continued proportion, and D7.3 for the definition of measurement direction) that Heath either uses implicitly or covers with 'similarly we can prove.' Heath_only is empty, confirming that the AI includes all of Heath's citations. The ai_only items are all depth-expansions of the same underlying logical steps, not evidence of a different proof path.

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs establish 8.7 by an identical proof by contradiction: assume the first number does not measure the second, apply 8.6 to conclude no number in the continued proportion measures any other, derive a contradiction with the hypothesis that the first measures the last, and conclude the first must measure the second. The citation sets are identical (both cite only 8.6), the key intermediate conclusions are the same, and the logical structure matches exactly, yielding a perfect match classification.

### 8.8
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Heath's proof works by applying VII.33 to the entire continued proportion sequence (all four numbers A,C,D,B) to find the least numbers G,H,K,L in the same ratio, then uses ex aequali (VII.14) to derive that the extreme ratio G:L equals A:B and hence E:F, followed by VII.21 and VII.20 to establish the measuring relationship. The AI takes a fundamentally different path: it applies VII.33 only to the two-number ratio A:B to find the least pair F,G, then explicitly constructs the full continued proportion via VIII.2, uses VIII.1 and VIII.3 to confirm these are least with prime extremes, applies VII.20 to get the measuring relationship, and finally uses VII.17 to show that multiplying by a common factor preserves the ratios. The backbones differ in their key intermediate conclusions: Heath's pivot is the ex aequali step connecting the full-sequence least numbers to the extreme ratio, while the AI's pivot is the explicit construction of the continued proportion via VIII.2 and ratio preservation via VII.17. Both paths are logically complete, making this a genuine path difference (D).

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they use 8.1 to establish the given sequence as the least in its ratio, then 8.2 to construct the power sequences, and finally exhibit the continued proportions from the unit to A and from the unit to B. The AI's two extra citations (ai_only: 7.22 and D7.15) represent citation-depth differences rather than path divergences. Specifically, 7.22 (the least numbers in a ratio are coprime) appears inside Heath's own proof of 8.2, confirmed by the proof-tree containment test, so the AI is citing an internal ingredient of a shared proposition. D7.15 is a definition used to justify the multiplication/exponent notation, which is standard over-citation. With heath_only empty and both proofs reaching the same key intermediate conclusions through the same logical route, this is a granularity difference in citation depth, not a different proof path.

### 8.10
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Heath's proof constructs the intermediate numbers explicitly by multiplying the geometric-sequence bases (D*F=H, D*H=K, F*H=L) and then establishes the continued proportion A:K=K:L=L:B step-by-step using 7.17 and 7.18 to relate ratios. The AI takes a fundamentally different high-level approach: it expresses A and B as powers of their respective bases, reduces the ratio of bases to least terms via 7.33, establishes coprimality via 7.22, uses 8.2 to find least numbers in continued proportion between the relevant powers, and then applies 8.8 to transfer the continued proportion to A and B. The backbones are genuinely different -- Heath works constructively with explicit products while the AI packages the argument through higher-level results (8.2, 8.8). The AI's path is logically complete, with each step supported by valid citations, so Q3 confirms a valid different path, yielding D.

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing the product of the two sides as a mean proportional, establishing two ratio equalities via VII.17 and VII.18, combining them to show the mean proportional, and then applying V.Def.9 for the duplicate ratio. The AI proof adds three explicit citations not in Heath (5.11 for transitivity of ratios, D7.15 for the definition of multiplication, and D7.18 for the definition of square number), but all three correspond to steps that Heath uses implicitly. Since heath_only is empty and the ai_only items are all definitions or an explicit transitivity citation that Heath applies without naming, this is a same-backbone, different-depth situation characteristic of granularity difference.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they construct mean proportionals (A-squared-B and A-B-squared) between two cube numbers, build a continued proportion chain showing the ratio between consecutive terms equals the ratio of the sides, and conclude via V. Def. 10 that the cube-to-cube ratio is triplicate of the side-to-side ratio. The logical backbone is identical. The AI's extra citations (7.16 for commutativity of multiplication, and definitions D7.16, D7.18, D7.19) are over-citations that make explicit what Heath leaves implicit. Heath's proof relies on the same arithmetic facts but does not cite commutativity or the definitions of square and cube numbers explicitly. Since heath_only is empty and the ai_only items are all basic properties or definitions, this is a citation-depth difference with the same backbone, yielding G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: constructing auxiliary mean proportional numbers between the squares and cubes, establishing that the intermediate ratio chains are all in the same ratio (since A:B = B:C), and then applying ex aequali (7.14) to conclude D:E = E:F and G:H = H:K. The AI explicitly cites 7.17 and 7.18 to justify each ratio step, while Heath compresses these steps into the phrase 'in manner similar to the foregoing' (referring to 8.12, whose proof uses 7.17 and 7.18 explicitly). The AI also cites CN1 for equality transitivity. Since heath_only is empty and ai_only contains {7.17, 7.18, CN1} which are the propositions Heath invokes implicitly via the reference to 8.12's method, this is a citation-depth difference with the same backbone, yielding G.

### 8.14
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. While the forward direction (if A^2 measures B^2 then A measures B) follows the same backbone in both proofs — establishing a continued proportion via 8.11, applying 8.7 to deduce measurement of the middle term, then concluding via D7.20 — the converse direction diverges. Heath's converse mirrors the forward direction, using the same continued proportion and D7.20 to transfer measurement from sides to squares. The AI instead takes a fundamentally different path for the converse: it applies 7.17 twice to establish that A^2 measures AB (from A:B = A^2:AB) and AB measures B^2 (from A:B = AB:B^2), then concludes by transitivity of divisibility that A^2 measures B^2. This is a valid but structurally different logical backbone that does not pass through the continued proportion reasoning Heath employs, constituting a genuine path difference.

### 8.15
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish a continued proportion between the cube numbers with ratio equal to the sides' ratio (via 8.12), apply 8.7 to show the first term measures the second, then use D7.20 to transfer divisibility from cubes to sides (Part I), with the reverse for Part II. The citation differences are all at the granularity level: the AI adds D7.19 (definition of cube, used for notation setup) and D7.3 (definition of measurement, used to make transitivity of divisibility explicit), while Heath adds 8.11 (the square analogue cited alongside 8.12, but unnecessary since the proposition concerns cubes and 8.12 alone suffices). These are citation-depth differences, not backbone differences, placing this squarely in Case A of Q2.

### 8.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same two-part contrapositive result using identical logical backbones: each part is proved by contradiction via Proposition 8.14. The AI proof (Steps 2 and 3) mirrors Heath's structure exactly, assuming the negation of the desired conclusion, applying 8.14 to derive the contradicted hypothesis, and concluding. The only citation difference is that the AI adds Definition 7.18 (ai_only = [D7.18]) when introducing the notion that square numbers are 'equal multiplied by equal,' which Heath leaves implicit. Since D7.18 is a definitional over-citation and heath_only is empty, this is a pure citation-depth difference with the same key intermediate conclusions, satisfying Case A of Q2.

### 8.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 8.17 are structurally identical and cite exactly the same proposition (8.15). Both proofs establish the biconditional by proving each direction via proof by contradiction: in part 1, assuming the side measures the side leads via 8.15 to the cube measuring the cube, contradicting the hypothesis; in part 2, assuming the cube measures the cube leads via 8.15 to the side measuring the side, contradicting the hypothesis. The citation sets are identical (ai_used = heath_refs = {8.15}), the Jaccard similarity is 1.0, and the key intermediate conclusions match exactly, so this is a perfect match.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish proportionality of corresponding sides from the definition of similar plane numbers, (2) construct a mean proportional by multiplying a side of one number by a non-corresponding side of the other, (3) use properties of multiplication and proportion to show the three numbers are in continued proportion, and (4) conclude the duplicate ratio via V. Def. 9. The citation differences are granularity-level: Heath uses 7.13 (alternation) to rearrange the proportion from C:D::E:F to C:E::D:F, then applies 7.17 twice; the AI extracts the corresponding-sides proportion a:c::b:d directly from the similarity definition and uses 7.17 once and 7.18 once (7.18 being the dual of 7.17 with multipliers swapped). The AI's additional citations (7.19 for verification, CN1, D7.16) are axiom/definition-level over-citations. The key intermediate conclusions — the mean proportional, the continued proportion, and the duplicate ratio — are identical in both proofs.

### 8.19
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 reveals different backbones: Heath constructs plane numbers K=C*D and L=F*G, invokes 8.18 to find a mean proportional M between them, then builds the four-term continued proportion A, N, O, B using additional multiplications by E and H. The AI takes a direct route, constructing C1=a*e*c and C2=d*e*c as explicit mean proportionals, then proving each consecutive ratio equals the common side ratio using 7.17, 7.18, and 7.16 (commutativity). The two constructions produce different intermediate numbers and follow different logical chains: Heath's proof pivots on 8.18 and 7.13 (alternation), while the AI uses 7.19 and 7.16 instead. Since the key intermediates differ and the AI's path is logically valid (Q3 confirmed), this is classified as D.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: they establish the two target numbers as plane numbers with specific sides (D,F and E,G) via 7.33 and 7.20, then prove the sides are proportional (D:E = F:G), and conclude similarity. The difference lies in citation depth for the proportionality step. Heath uses 7.17 twice (to derive D:E = A:C = C:B and F:G = C:B) and then 7.13 (alternation to get D:F = E:G), while the AI derives E*F = D*G from the equalities and applies 7.19 (cross-multiplication converse) to get D:E = F:G directly. The proof-tree containment test confirms this is a depth difference: 7.17 (a heath_only item) appears inside Heath's own proof of 7.19 (an ai_only item), meaning the AI cites 7.19 as a unit while Heath re-derives its internals inline. The AI's additional citations of D7.16 and D7.21 are explicit definitions that Heath uses implicitly. Heath's use of 7.13 is an additional step to restate the proportionality in alternate form, which the AI bypasses by working with D:E = F:G directly for the similarity conclusion. All differences are citation-depth variations around the same logical backbone.

### 8.21
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path. Heath's proof works through VIII.20 (similar plane numbers) by taking the least triple E, F, G in ratio with A, C, D, showing E and G are prime (VIII.3) and hence similar plane numbers, then building up solid number structure from plane number sides using VII.14 (ex aequali), VII.21, VII.18 and VII.20. The AI proof takes a fundamentally different algebraic approach: it repeatedly applies VII.19 and VII.20 to decompose the continued proportion A:C:D:B = p:q step by step, ultimately deriving A = t*p^3 and B = t*q^3, then factors these as products of three numbers to establish solidity and uses VII.17 to show all three pairs of corresponding sides share ratio p:q. The AI never establishes similar plane numbers as an intermediate result and does not use VIII.20, VIII.3, VIII.2, VII.14, VII.18, or VII.21 at all. The AI's chain is logically complete and sound, running from premises to conclusion via a valid but distinct algebraic decomposition route, warranting classification as D.

### 8.22
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: they use 8.20 to establish that A and C are similar plane numbers, then conclude that since A is square, C must also be square. Heath's proof accomplishes this in two sentences, treating the final inference as obvious. The AI proof expands this same inference over six additional steps (Steps 4-8), explicitly citing definitions D7.16, D7.18, D7.21 and lower-level Book 7 propositions 7.16, 7.17, 7.19 to unpack what it means for similar plane numbers with one being square to force the other to be square. All six ai_only citations are sub-steps that elaborate the same conclusion Heath reaches implicitly. With heath_only empty, every citation Heath uses is also present in the AI proof. This is a clear Case A: same backbone, different citation depth.

### 8.23
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish that B and C are two mean proportionals between A and D, apply 8.21 to conclude A and D are similar solid numbers, and then conclude D is cube because A is cube. Heath's proof leaves the final inference implicit ('But A is cube; therefore D is also cube'), while the AI explicitly unpacks why a similar solid to a cube must itself be a cube, citing D7.21 (similar solids have proportional sides), 7.13 (alternation of proportion), and D7.20 to show all three sides of D are equal, then D7.19 (definition of cube). These ai_only citations (7.13, D7.19, D7.20, D7.21) represent over-citation of definitions and an elaboration of a step Heath treats as obvious, not a different proof path. heath_only is empty, confirming the AI covers all of Heath's reasoning and more. This is Case A: same backbone, different citation depth.

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish one mean proportional between the two given square numbers, (2) transfer that mean proportional to A and B via 8.8, and (3) conclude B is square via 8.22. The only difference is the citation used in step 1: Heath cites 8.18 (between two similar plane numbers there is one mean proportional) while the AI cites 8.11 (between two square numbers there is one mean proportional). These are two different propositions that both validly establish the same intermediate conclusion for this case, since square numbers are similar plane numbers. The AI chose the more specific result (8.11, tailored to squares) while Heath chose the more general result (8.18, for similar plane numbers). Since the key intermediate conclusions are identical and the difference is only in which valid prior result is cited to justify the same step, this is a citation-depth difference under Case A of Q2.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish that two mean proportionals exist between the given cube numbers in the ratio, (2) use 8.8 to transfer those mean proportionals to A and B, (3) conclude B is cube via 8.23. The only difference is in how step (1) is justified: Heath notes that cubes are similar solid numbers and invokes 8.19 (the general theorem for similar solids), while the AI directly invokes 8.12 (the specific theorem for cubes). These are parallel results that yield exactly the same intermediate conclusion. Since the key intermediate conclusions are identical and only the citation depth differs at a single step, this is a granularity difference. The AI's additional citation of D7.19 (definition of similar solid numbers) is harmless over-citation consistent with G.

### 8.26
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decides this classification. Heath's proof finds the least numbers D, E, F in the same ratio as A, C, B (using 7.33/8.2), shows the extremes D, F are square (8.2), and concludes from D:F = A:B. The AI takes a fundamentally different path: it decomposes the similar plane numbers into their sides (a,b and c,d), establishes the mean proportional via 8.18, uses 8.11 to find the mean proportional between the square numbers a^2 and c^2, then applies 5.11 (transitivity of ratios) and 7.14 (ex aequali) to conclude A:B = a^2:c^2. The two backbones differ in their key intermediate conclusions — Heath works through least numbers in ratio while the AI works through the sides' squares directly. Both paths are logically complete, so the classification is D.

### 8.27
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Heath's proof directly applies VIII.2 to find the least numbers in the continued proportion A, C, D, B and notes that the extremes are cubes, concluding immediately that A:B is a ratio of cubes. The AI proof takes a structurally different path: it extracts the side ratio in least terms p:q (7.33), explicitly constructs cube numbers p^3 and q^3 (D7.19), invokes 8.12 to establish that between these cubes there are two mean proportionals with the same common ratio p:q, then uses 8.2 to find the least four-term continued proportion with ratio p:q, and finally applies CN1 to equate A:B with p^3:q^3. The introduction of 8.12 (between two cube numbers there are two mean proportional numbers) as a key intermediate conclusion is absent from Heath's proof and constitutes a genuinely different logical backbone, not merely a difference in citation depth. The AI's path is logically valid and complete, so Q3(b) holds, yielding classification D.
