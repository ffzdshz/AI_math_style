# Book 9 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 9.23, 9.25 |
| Granularity difference (G) | 21 | 9.5, 9.6, 9.7, 9.8, 9.9, 9.13, 9.14, 9.18, 9.20, 9.21, 9.24, 9.26, 9.28, 9.29, 9.30, 9.31, 9.32, 9.33, 9.34, 9.35, 9.36 |
| Path difference (D) | 12 | 9.1, 9.2, 9.3, 9.4, 9.11, 9.12, 9.15, 9.16, 9.17, 9.19, 9.22, 9.27 |
| AI proof error (E) | 1 | 9.10 |

**Total**: 36 propositions

## Error Details

| Proposition | Error type | Details |
|---|---|---|
| 9.10 | Missing case | CANDIDATE E — 9.10   violated_claim : The second part of the proposition — 'if the number after the unit be not cube, neither will any other be cube except the fourth from the unit and all those which |

## Per-Proposition Analysis

### 9.1
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification. Heath's proof constructs D = A*A (square), establishes A:B = D:C via 7.17, transfers the mean proportional from (A,B) to (D,C) via 8.8, then applies 8.22 (if three numbers in continued proportion and the first is square, the third is square). The AI takes a fundamentally different route: it finds the mean proportional G between A and B via 8.18, then directly applies 7.19 to conclude A*B = G*G from the proportion A:G = G:B, making C = G^2 a square by definition. The AI never introduces D = A^2, never uses the ratio transfer (7.17, 8.8), and never invokes 8.22. These are genuinely different logical backbones producing different key intermediate conclusions, and the AI's path is logically sound at every step.

### 9.2
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided this classification. Heath's proof constructs D=A*A (a square), establishes A:B = D:C via 7.17, then uses the fact that D and C are both similar plane numbers (squares) to find a mean proportional between D and C (8.18), transfers this to A and B via the same-ratio result 8.8, and finally applies 8.20. The AI takes a fundamentally different route: it directly extracts N from S=N*N (by D7.18), applies the converse of 7.19 to A*B=N*N to immediately establish A:N=N:B, and then applies 8.20. The AI bypasses Heath's entire intermediate construction involving D=A^2 and the chain 7.17/8.18/8.8. The proof-tree containment test confirms this is not a depth difference: while 7.19 does cite 7.17, the heath_only items 8.18 and 8.8 do not appear inside the proof of 7.19, so the AI is using a genuinely independent argumentative route. Both proofs are logically complete and arrive at the same conclusion via valid but different intermediate steps.

### 9.3
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decides the classification as D (path difference). Heath's proof establishes two mean proportionals between the unit and A (via VII.Def.20), then uses VIII.8 to transfer the continued proportion structure to the pair (A, B), and finally applies VIII.23. The AI proof takes a fundamentally different route: it decomposes A into a*a*a using D7.19, directly constructs four numbers A, A*a, A*(a*a), A*A in continued proportion using VII.17 and VII.18, and then applies VIII.23 to conclude A*A = B is cube. The AI never works with the unit or uses VIII.8 to transfer proportions; instead it explicitly builds the required continued proportion chain through multiplication properties. These represent genuinely different logical backbones — Heath argues by proportion transfer while the AI argues by direct construction — making this a path difference rather than a granularity difference.

### 9.4
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) D = A*A is cube by 9.3, (2) two mean proportionals exist between D and C, and (3) C is cube by 8.23. However, the route to establishing the mean proportionals between D and C differs substantively. Heath uses 8.19 (between similar solid numbers fall two mean proportionals) to get mean proportionals between A and B, then 8.8 to transfer those mean proportionals to D and C via the ratio A:B :: D:C. The AI instead uses 8.12 (between two cube numbers there are two mean proportionals) to get mean proportionals between A and B, then explicitly constructs the mean proportionals between D and C through three applications of 7.17 rather than using 8.8. Since 8.12 does not contain 8.19 in its proof tree (they are independent parallel results for cubes vs. similar solids), and 8.8 is replaced by explicit construction, the proof-tree containment test fails for both heath_only items, so Case A does not hold. Under Q3, the AI's different path is logically valid: 8.12 correctly provides mean proportionals for cubes, and the 7.17 construction soundly establishes the continued proportion D, G, H, C.

### 9.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same initial backbone: establishing D = A*A is cube via 9.3, then deriving the ratio A:B = D:C via 7.17. They diverge in how they conclude B is cube: Heath re-derives the internals of 8.25 inline by going through mean proportionals (8.19 to show two mean proportionals fall between cubes D and C, 8.8 to transfer this to A and B, then 8.23 to conclude B is cube from four numbers in continued proportion), while the AI directly cites 8.25 which packages exactly those three steps. The proof-tree containment test confirms this: all three heath_only citations (8.19, 8.8, 8.23) appear inside Heath's own proof of 8.25, so the AI is citing at a higher level of abstraction rather than taking a genuinely different path. The ai_only definitions D7.15 and D7.19 are simple over-citation of definitions, a hallmark of granularity difference.

### 9.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this classification as G (granularity difference) via the proof-tree containment test. The AI proof reduces 9.6 to 9.5 by showing that B = A*A is cube (hypothesis), B*A = A^3 is cube (by D7.19), and then applying 9.5 (if a cube times a number gives a cube, that number is cube) to conclude A is cube. Heath's proof instead re-derives the internal machinery of 9.5 inline, establishing proportion chains (unit:A = A:B = B:C via D7.20), invoking 8.19 for mean proportionals between similar solid cubes, transferring via 8.8, and concluding via 8.23. All three substantive heath_only propositions (8.19, 8.8, 8.23) appear inside Heath's own proof of 9.5, satisfying the containment test: the AI cites 9.5 as a single higher-level unit while Heath re-derives 9.5's internals. This is a citation-depth difference, not a backbone difference.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) since A is composite, it is measured by some number (D7.13); (2) express A as a product of two factors using the definition of multiplication (D7.15); (3) the final product is therefore the product of three numbers, making it solid. The AI proof explicitly cites D7.16 (plane number definition) and D7.17 (solid number definition) to formally label A as plane and the result as solid, while Heath applies these same concepts implicitly without citing the definition numbers. The ai_only set contains only definitions (D7.16, D7.17), and heath_only is empty, confirming this is a citation-depth difference rather than a path difference. This is Case A in Q2: same backbone, different citation depth, yielding G.

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this as G (granularity difference). Both proofs share the same logical backbone: (1) show the third term from unit is square because A*A = B, (2) extend to all odd-indexed terms via VIII.22, (3) show the fourth term is cube because A*A*A = C, (4) extend to all terms leaving out two via VIII.23, (5) conclude the seventh term is both cube and square. The only difference is in which definitions are explicitly cited: the AI cites D7.15 (multiplication), D7.18 (square), and D7.19 (cube) while Heath cites D7.20 (proportional numbers). Both proofs use 8.22 and 8.23 as the key propositions. Since all ai_only and heath_only items are definitions used at the same logical positions within the same argumentative structure, this is a citation-depth difference, not a path difference.

### 9.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification as G (Granularity difference). The AI proof and Heath's proof share the same logical backbone for the square case stated in the proposition: both establish that B (the third from the unit) is square via 9.8, then use 8.22 iteratively on consecutive triples to show C, D, E, etc. are all square. The heath_only citations (8.23, 9.3) appear exclusively in Heath's proof of the cube extension case, which goes beyond the stated proposition; they do not represent a different backbone for the square case. The ai_only citation (D7.18) is a definition reference (square number), representing an over-citation of foundational definitions. Since both proofs argue through identical key intermediate conclusions for the proposition as stated, with differences only in citation depth and scope of coverage, this is a granularity difference.

### 9.10
**Category**: AI proof error
**Jaccard**: 0.143
**Analysis**: Proposition 9.10 is a compound proposition with two independent parts: (1) if the number after the unit is not square, then no other term besides the third from the unit and those leaving out one is square; and (2) if the number after the unit is not cube, then no other term besides the fourth from the unit and those leaving out two is cube. Heath's proof addresses both parts fully: the square case via contradiction using 9.8 and 8.26 converse, and the cube case via contradiction using 9.8, 8.25, and 9.6. The AI proof (Steps 1-12) addresses only the square part, proving that no odd power of A is square, and concludes 'This is what was to be proved' without any mention of cubes whatsoever. The cube case is an entirely separate assertion with its own hypothesis and conclusion, not a mere expansion or restatement of the square case. This constitutes a genuinely missing case under Q1(a), warranting classification E.
**Audit Record**: CANDIDATE E — 9.10
  violated_claim : The second part of the proposition — 'if the number after the unit be not cube, neither will any other be cube except the fourth from the unit and all those which leave out two' — is entirely unaddressed by the AI proof.
  failure_mode   : missing_case
  missing_is     : support   # The cube case is an independent part of the proposition, not an expansion of the square case.
  evidence       : The AI proof text covers Steps 1-12 dealing only with squares (odd vs even powers of A) and concludes 'This is what was to be proved' without any mention of cubes. Heath's proof has a second section beginning 'Next, let A not be cube' that proves the cube case using 9.8, 8.25, and 9.6.
  why_not_terse  : This is not a brevity issue — the cube case is an entirely separate assertion of the proposition with its own hypothesis ('let A not be cube') and its own conclusion ('neither will any other be cube except the fourth from the unit'), and the AI proof contains zero text addressing it.

### 9.11
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath's proof uses a specific proportional relationship (A:B = D:E from the continued proportion) and then applies alternation via 7.15 to conclude that the unit measures D the same number of times as B measures E, thereby establishing the measurement result. The AI proof takes a fundamentally different algebraic approach: it represents each term Ak in the geometric sequence as A2^(k-1), then shows that Aj = Ai times Aj-i+1 by direct computation of powers, concluding that Ai measures Aj according to the proportional number Aj-i+1. These are genuinely different logical backbones — Heath relies on the alternation property of proportions while the AI relies on the explicit multiplicative/power structure of the geometric sequence. The AI's path is logically valid under Q3, as the chain from premises to conclusion is sound, yielding classification D.

### 9.12
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determined the classification. Heath proves 9.12 by contradiction: assuming the prime E does not measure A, he uses coprimality (7.29), least ratio properties (7.21, 7.20), and proportionality (7.19) to descend through the geometric sequence and derive a contradiction. The AI instead gives a direct proof by descent using 7.30 (if a prime measures a product it measures one of the factors): from E = A*D it applies 7.30 to get p|A or p|D, and if p|D then D = A*C yields p|A or p|C, continuing until reaching B = A*A where 7.30 forces p|A. The two proofs have fundamentally different logical backbones -- Heath relies on the coprimality/ratio chain (7.29, 7.21, 7.20) while the AI relies on the prime product divisibility theorem (7.30). The AI's approach is mathematically valid, constituting a sound alternative path to the same conclusion, so the classification is D.

### 9.13
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: proof by contradiction assuming a divisor E not among the proportional numbers, showing E cannot be prime (via 9.12), that E must be divisible by A (the number after unity) using 7.31 and 9.12, then performing a descent through the sequence terms until reaching the prime A itself, yielding a contradiction. The citation differences are purely about depth: the AI uses 7.17 (equal products imply same ratio when multiplied by same number) where Heath uses 7.19 (the proportion-from-equal-products result) for the same logical step of concluding that quotients measure earlier terms. Heath explicitly cites 9.8 for the fact that A multiplied by itself makes B (the square property of the third term), while the AI handles this implicitly through the general descent argument recognizing proportional numbers as powers of A_2. The AI's additional citations of definitions (D7.3, D7.11, D7.15) and 7.20 (transitivity of measurement) represent over-citation of foundational facts that Heath leaves implicit. All key intermediate conclusions are established in both proofs at the same logical positions, making this a citation-depth difference rather than a path difference.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: assume a new prime measures A, express A as a product of that prime and a cofactor, apply 7.30 to conclude the original primes must measure the cofactor, and derive a contradiction with minimality. The AI proof adds explicit intermediate steps that Heath leaves implicit: it cites 7.29 to establish that each original prime is coprime to the new prime before applying 7.30, and explicitly invokes definitions (D7.11, D7.15, D7.3) and CN5 for steps Heath handles without citation. All ai_only items (7.29, CN5, D7.11, D7.15, D7.3) represent over-citation of definitions, common notions, and a sub-lemma that Heath subsumes into the direct application of 7.30. The heath_only set is empty, confirming the AI covers all of Heath's cited material. This is a clear Case A: same backbone, different citation depth.

### 9.15
**Category**: Path difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. For the first two sub-cases (A+B prime to C, and B+C prime to A), both proofs share the same backbone: establish a,b coprime (7.22), their sum coprime to each (7.28), then use 7.25 and 7.24 to show the result. The AI omits the explicit citation of II.3 for the factoring but achieves the same intermediate conclusion, which alone would be a granularity difference. However, for the third sub-case (A+C prime to B), the proofs take genuinely different paths. Heath uses II.4 to expand (DE+EF)^2, establishes that this square is coprime to DE*EF, then applies separando twice to conclude that DE^2+EF^2 is coprime to DE*EF. The AI instead uses a direct divisibility argument: assuming d divides both a^2+b^2 and a, it shows d must divide b^2, but since b^2 is coprime to a (by 7.25) and d divides a, d must be unity. This proves a^2+b^2 is coprime to a (and symmetrically to b), then invokes 7.24 to get coprimality with ab. This is a valid but structurally different logical path that does not pass through II.4 or the separando steps at all, constituting a genuine path difference under Q2 Case B, confirmed valid under Q3.

### 9.16
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof reaches contradiction via the ratio-minimality route: since A and B are prime they are the least numbers in that ratio (7.21), so A measures B (7.20), contradicting coprimality. The AI proof takes a fundamentally different path through product arithmetic: from A:B = B:C it derives A*C = B*B (7.19), then uses the fact that B*B is prime to A (7.25) to show A must be the unit, contradicting A being a number. The key intermediate conclusions are entirely different — Heath's backbone is 'least ratio implies measuring' while the AI's backbone is 'product equality plus coprimality of square implies A is a unit.' The citation sets are completely disjoint (Jaccard = 0.0), and the proof-tree containment test confirms neither AI-cited proposition subsumes the Heath-cited ones. Both proofs are logically complete, so Q3 confirms the AI's different path as valid, yielding category D.

### 9.17
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof uses alternation (7.13) to convert the assumed proportion into A:D = B:E, then applies 7.21 (primes are least in their ratio) and 7.20 to conclude A measures B, and cascades through the continued proportion to show A measures D, contradicting coprimality. The AI proof takes a fundamentally different route: it uses 7.33 to find the least numbers F,G in the ratio A_1:A_2, applies 7.20 to show F divides both A_1 and A_n, uses coprimality (D7.12) to conclude F is a unit, then derives the multiplicative structure A_k = G^{k-1}*A_1 to show A_1 divides A_n, and uses D7.2 to establish A_1 is not a unit, reaching a contradiction. The key intermediate conclusions differ: Heath argues through alternation and a divisibility cascade (A|B, then A|C, then A|D), while the AI argues through least-ratio representatives and multiplicative structure (F=unit, then A_1|A_n directly). Both paths are logically complete, making this a genuine path difference.

### 9.18
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: compute B squared, check whether A measures it, and if so use 7.19 to establish the proportionality A:B = B:D, otherwise prove impossibility by contradiction. Heath separately handles the case where A and B are prime to one another by citing 9.16 before proceeding to the general case, while the AI subsumes this under its general criterion (A measures B squared or not), which is exhaustive and implicitly covers the prime case. The ai_only items D7.15 and D7.3 are definitions the AI cites for explicitness that Heath uses implicitly. The heath_only item 9.16 is not evidence of a different path but rather of Heath citing a previously proven special case that the AI handles through its more direct general argument. The key intermediate conclusions (third proportional exists iff A measures B squared, established via 7.19 and contradiction) are identical in both proofs, making this a citation-depth difference rather than a path difference.

### 9.19
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided this classification. Heath's proof is a multi-case argument that distinguishes four scenarios based on whether the three numbers are in continued proportion and whether the extremes are prime to one another, using 9.17 for the continued-proportion-with-primes case, 7.14/7.21/7.20 for the non-continued-proportion-with-primes case, and 7.19 for the remaining cases where A measures B*C. The AI proof takes a fundamentally different path: it gives a single unified criterion that a fourth proportional exists if and only if A measures B*C, proved entirely via 7.19 and definitions. The AI avoids all case-splitting by primality or continued proportion, instead reducing the problem to a single divisibility condition. This constitutes a genuinely different logical backbone (Q2 Case B). Under Q3, the AI's path is logically valid: the forward direction constructs D from the divisibility, and the reverse direction uses contradiction via 7.19's product-proportion equivalence. The proof is complete and sound, yielding classification D.

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a number divisible by all given primes (Heath uses the LCM, the AI uses the product), add a unit, then consider two cases -- if the result is prime, it is a new prime; if not, by 7.31 some prime divides it, and that prime cannot be any of the given primes because it would then have to divide the unit, a contradiction. The key intermediate conclusions are identical in both proofs. The AI's ai_only citations (CN5, D7.11, D7.13, D7.15, D7.3, D7.5) are all definitions and common notions that Heath invokes implicitly without citation, representing over-citation rather than a substantive path difference. With heath_only empty and the backbones matching, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 9.21
**Category**: Granularity difference
**Jaccard**: 1.000
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusion: each even number has a half part (by D7.6), therefore the whole sum also has a half part, therefore the whole is even. The citation sets are identical (both cite only D7.6), with Jaccard 1.0 and empty ai_only and heath_only sets. The difference is purely one of exposition depth: Heath states directly that since each part has a half, the whole has a half; the AI proof elaborates this with an explicit inductive argument showing the base case (sum of two even numbers) and the inductive extension. This additional detail constitutes a granularity difference (Case A of Q2) rather than a path difference, since the underlying logical backbone and citations are the same.

### 9.22
**Category**: Path difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Heath's proof decomposes each odd number individually by subtracting a unit (D7.7), sums the even remainders via 9.21, notes the multitude of units is even, and adds the two even sums via 9.21 again. The AI proof takes a fundamentally different approach: it pairs the odd numbers (since their multitude is even, via D7.6), shows each pair of odd numbers sums to an even number using D7.7 and algebra, then sums all the even pair-sums via 9.21. The key intermediate conclusions differ — Heath's backbone has 'sum of remainders is even AND sum of units is even' while the AI's backbone has 'each pair of odd numbers sums to even.' Since these are different backbones (Case B in Q2), the proof proceeds to Q3 where the AI's alternative path is verified as logically complete, yielding classification D.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof cite the identical set {9.21, 9.22, D7.7} (Jaccard 1.0) and argue through the same key intermediate conclusions: separating the odd-count collection into an even-count subcollection whose sum is even (9.22) plus one remaining odd number, decomposing that odd number into an even part plus a unit (D7.7), combining the two even parts via 9.21, and concluding the total is odd by D7.7. No forward dependencies, no logical errors, no missing cases, and no citation differences exist. The perfect-match check at the end of the protocol confirms category P.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) AB is even so it has a half part, (2) BC is even so it has a half part, (3) the remainder CA therefore also has a half part and is even. The AI makes the subtraction step explicit by citing CN3 (equals subtracted from equals leave equal remainders) and introduces named quantities D and E as the halves, while Heath leaves the subtraction implicit and simply states the remainder also has a half part. The single ai_only item CN3 is a Common Notion (axiom) that justifies a step Heath performs without explicit citation, making this a citation-depth difference rather than a backbone difference. Case A of Q2 holds, yielding Granularity difference (G).

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow the identical logical backbone with the identical citation set. Both proofs (1) subtract the unit CD from odd BC to obtain even BD/DB via Definition VII.7, (2) conclude that the remainder AD is even since both AB and BD are even by Proposition IX.24, and (3) deduce that AC/CA is odd because it differs from the even number AD by the unit CD, again invoking Definition VII.7. The citation sets are exactly equal (ai_used = heath_refs = {9.24, D7.7}), yielding Jaccard 1.0, and the key intermediate conclusions match at every stage. Since both the logical backbone and the citation sets are identical, the classification is P (Perfect match).

### 9.26
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: subtract a unit from each odd number to obtain two even numbers (by D7.7), then apply 9.24 (even minus even is even) to conclude the remainder is even. The AI's only additional citation is CN3, a common notion used to explicitly justify the algebraic step of canceling the equal units (BD = BE) when showing AC = AD - CE. Heath performs the same reasoning but treats the cancellation as implicit. Since heath_only is empty and ai_only contains only a common notion (axiom-level over-citation), this is a citation-depth difference with the same key intermediate conclusions, yielding Granularity difference (G).

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath proves 9.27 directly: he subtracts a unit from the odd number to obtain an even number, then applies 9.24 (even minus even is even) to show an intermediate remainder is even, and concludes via D7.7 that the target remainder is odd. The AI instead uses proof by contradiction: it assumes the remainder is even, then applies 9.21 (sum of even numbers is even) to show the original odd number would be even, reaching a contradiction. These are fundamentally different proof strategies with different key intermediate conclusions -- Heath's backbone relies on unit subtraction and 9.24, while the AI's backbone relies on the contrapositive reasoning via 9.21. Since the AI's contradictory path is logically sound and complete, this is a valid path difference (D).

### 9.28
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) C is made up of as many copies of B as there are units in A (by D7.15), (2) since B is even, all summands are even, and (3) by 9.21, the sum of even numbers is even, so C is even. The only citation difference is that the AI explicitly cites D7.6 (definition of even number) when noting B is even, while Heath simply states the fact without citing the definition. This is a classic over-citation of a definition, a citation-depth difference that does not alter the logical backbone. Since the key intermediate conclusions are identical and the difference is purely in citation granularity, the classification is G. The citation sets are not identical (ai_only contains D7.6), so P does not apply.

### 9.29
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: (1) by the definition of multiplication (D7.15/VII.Def.15), the product C equals A copies of B; (2) since each copy B is odd and the number of copies A is odd, we have an odd multitude of odd numbers; (3) by 9.23/IX.23, the sum of an odd number of odd addends is odd, so C is odd. The only citation difference is that the AI explicitly cites D7.7 (the definition of odd number) when identifying A and B as odd, whereas Heath treats oddness as directly given by hypothesis without citing the definition. This is a shallow over-citation of a definition, not a path divergence, placing the proof squarely in the granularity-difference category.

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) A (odd) measures B (even) so B = A times some multiplier, (2) proof by contradiction that the multiplier cannot be odd because that would make B odd, contradicting B being even, (3) the multiplier is therefore even, (4) A therefore measures the half of B. The only difference is citation depth. Heath cites 9.23 directly (sum of an odd count of odd numbers is odd) to establish that the product of two odd numbers is odd, while the AI cites 9.29 (product of two odd numbers is odd), which itself uses 9.23 in its proof per the proof-tree containment test. The AI's remaining ai_only citations (7.5, CN3, D7.15, D7.3, D7.6, D7.7) are definitions, common notions, and basic propositions that make explicit what Heath leaves implicit in the final steps. This is a citation-depth difference with identical backbone, confirming Case A of Q2.

### 9.31
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: a proof by contradiction where one assumes the odd number A and the double of B share a common measure, shows that common measure must be odd, applies 9.30 to conclude it also measures B, and derives a contradiction with the coprimality of A and B. The only difference is in how the oddness of the common measure is established: Heath leaves it implicit (a measure of an odd number is odd), while the AI explicitly argues via 9.21 that if the common measure were even, A would be a sum of even numbers and hence even, contradicting the hypothesis. The AI also over-cites several definitions (D7.12, D7.3, D7.5, D7.6, D7.7) that Heath leaves implicit. Since heath_only is empty and all ai_only items are either definitions or a theorem used to make explicit a step Heath takes implicitly, this is a same-backbone, different-depth scenario — Case A of Q2.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they set up the sequence of powers of 2 as a continued proportion from unity with the prime number 2 after the unit, invoke Proposition 9.13 to establish that the only divisors are the powers of 2 in the sequence, observe that all these divisors (except unity) are even, and conclude even-times even only via Definition 7.8. The AI proof makes additional explicit steps (showing 2^k is not even-times odd by contradiction in Step 6) and cites three extra definitions (D7.11 for prime, D7.6 for even, D7.9 for even-times odd) that Heath leaves implicit. Since heath_only is empty and the ai_only items are all definitions providing explicit grounding for facts Heath treats as obvious, this is a clear case of same backbone with different citation depth.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Both proofs share the same logical backbone: (1) the half of the number is odd, so the number is even-times odd by D7.9; (2) assume for contradiction the number is also even-times even per D7.8; (3) then the half would be measured by an even number, making it even; (4) but the half is odd, contradiction; (5) therefore the number is even-times odd only. The AI proof is substantially more verbose, explicitly unpacking foundational definitions (D7.6 for even, D7.7 for odd, D7.15 for multiplication) and CN2 (adding equals to equals) that Heath treats as implicit. Since heath_only is empty and ai_only contains only definitions and a common notion, this is a clear case of the AI over-citing foundational items while following the identical argument structure. Q2 Case A applies: same backbone, different citation depth, yielding classification G.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decides this as Granularity difference (G). Both proofs establish the same two key intermediate conclusions: (1) the number is even-times even because its half is not odd, appealing to D7.8, and (2) the number is even-times odd via repeated bisection until an odd factor is reached, with a contradiction argument that otherwise the number would be among those continually doubled from a dyad. The AI proof makes these steps more explicit by citing D7.6 (definition of even), D7.9 (definition of even-times odd), and 9.32 (characterizing doubled-from-dyad numbers as even-times even only), while Heath leaves these definitional and propositional references implicit. The AI also lists 9.33 in its USED citations though it is not explicitly invoked in the proof steps. The heath_only set is empty, confirming no step present in Heath is missing from the AI. This is Case A of Q2: same logical backbone with different citation depth.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they apply separando (VII.11) to derive equal ratios among consecutive differences, then use the antecedents-to-consequents principle (VII.12) to aggregate the differences and terms, arriving at the conclusion that the excess of the last over the first is to the sum of all preceding terms as the excess of the second over the first is to the first. Heath also references VII.13 in a combined annotation with VII.11 for the separando step, which the AI makes more explicit as a separate alternando application. The only citations in ai_only are CN1, CN2, and CN3, which are common notions (basic axioms for equality and addition/subtraction) that Heath uses implicitly without citation. Since heath_only is empty, every substantive proposition Heath cites is also cited by the AI. The key intermediate conclusions are identical in both proofs, with the AI simply over-citing foundational axioms, making this a citation-depth difference rather than a path difference.

### 9.36
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions: (1) using 9.35 to establish the sum of the geometric series, (2) enumerating all divisors of the product P = S * A(n-1) using the primality of S and 9.13, (3) summing all proper divisors to show they equal P, and (4) concluding P is perfect by D7.22. The large symmetric difference (Jaccard 0.25) is explained by citation-depth differences: the AI cites 7.24 as a unit, while Heath re-derives the same reasoning inline using 7.19, 7.20, and 7.21 — all three of which appear inside Heath's own proof of 7.24, satisfying the proof-tree containment test. Similarly, Heath uses 7.14 (ex aequali) for proportion manipulation where the AI uses direct algebraic reasoning, and the AI cites 9.11, 7.16, and several definitions (D7.11, D7.15, D7.3, D7.5) that Heath leaves implicit. These are all citation-granularity differences, not backbone differences, yielding G.
