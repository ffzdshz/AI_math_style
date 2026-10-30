# Book 9 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 3 | 9.23, 9.25, 9.26 |
| Granularity difference (G) | 17 | 9.5, 9.7, 9.8, 9.13, 9.14, 9.16, 9.20, 9.21, 9.22, 9.24, 9.28, 9.29, 9.30, 9.32, 9.33, 9.34, 9.35 |
| Path difference (D) | 16 | 9.1, 9.2, 9.3, 9.4, 9.6, 9.9, 9.10, 9.11, 9.12, 9.15, 9.17, 9.18, 9.19, 9.27, 9.31, 9.36 |
| AI proof error (E) | 0 |  |

**Total**: 36 propositions

## Per-Proposition Analysis

### 9.1
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof constructs D = A*A, establishes that A:B = D:C via VII.17, transfers the mean proportional from between A,B to between D,C via VIII.8, then concludes C is square because D is square and three numbers in continued proportion starting from a square end at a square (VIII.22). The AI proof instead identifies D as the mean proportional between A and B from VIII.18, then applies VII.19 (product of extremes equals product of means) to conclude A*B = D*D directly, so C = D*D is square by definition (D7.18). The two proofs have entirely different constructions of the intermediate quantity D and use different logical chains: Heath works through ratio transfer and the properties of continued proportions (8.8, 8.22), while the AI works through the product-of-means relationship (7.19). Both paths are logically complete, yielding a valid path difference.

### 9.2
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as D (path difference). Both proofs ultimately establish that one mean proportional falls between A and B and then apply 8.20 to conclude A and B are similar plane numbers. However, the routes to establishing that mean proportional are fundamentally different. Heath constructs D = A*A, establishes D:C = A:B via 7.17, observes that D and C are both square (hence similar plane numbers), uses 8.18 to place a mean proportional between D and C, then transfers this via 8.8 to A and B. The AI instead decomposes the square S into C*C using D7.18, applies the converse of 7.19 to A*B = C*C to directly obtain A:C = C:B, immediately identifying C as the mean proportional between A and B. The AI's path bypasses the intermediate construction of D = A^2 and the chain through 8.18 and 8.8 entirely, constituting a genuinely different logical backbone. The AI's path is logically complete and valid, with each step properly supported by cited propositions.

### 9.3
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof establishes two mean proportionals between the unit and A (using VII. Def. 20), then uses VIII.8 to transfer those mean proportionals to between A and B, and finally applies VIII.23. The AI instead constructs six numbers a, c, A, D, E, F in continued proportion by repeated application of 7.17, then uses 7.19 to prove that F equals B, and applies 8.23 to the sub-chain A, D, E, F to conclude B is cube. The key intermediate conclusions differ fundamentally: Heath's backbone relies on mean proportionals via the unit and the transfer theorem VIII.8, while the AI's backbone relies on direct construction of a continued proportion chain and algebraic identification of F with B via 7.19. Both paths are logically complete and valid, but they argue through genuinely different intermediate conclusions.

### 9.4
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determined the classification. Heath's proof establishes that D=A*A is cube via 9.3, then uses the ratio A:B=D:C (VII.17), the existence of two mean proportionals between similar solid numbers A and B (VIII.19), the transfer of mean proportionals to D and C (VIII.8), and concludes C is cube via VIII.23. The AI takes a fundamentally different path: it explicitly constructs the two mean proportionals between A and C=A*B by repeatedly multiplying by b (the cube root of B), yielding the continued proportion A, Ab, Ab^2, Ab^3=C, using basic arithmetic propositions VII.17, VII.18, VII.19, and VII.16 to establish the ratios and product identities. Both proofs arrive at VIII.23 for the final conclusion, but their logical backbones differ: Heath invokes existence theorems for mean proportionals (VIII.19, VIII.8) and the subsidiary result 9.3, while the AI constructs the intermediates directly from the cube root. The AI's path is logically complete and valid, constituting a genuine path difference.

### 9.5
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: establish that A-squared is cube, use 7.17 to get the ratio A-squared:C = A:B, and then conclude B is cube from the fact that A is cube and the ratio A:B equals a cube-to-cube ratio. The AI operates at a higher level of abstraction throughout: it cites 9.4 (product of two cubes is cube) where Heath cites the lower-level 9.3 (cube times itself is cube), and the AI cites 8.25 (mislabeled as 8.24) directly where Heath re-derives 8.25's internals using 8.19, 8.8, and 8.23. The proof-tree containment test confirms that all heath_only items (8.19, 8.8, 8.23) appear inside Heath's proof of 8.25, and 9.3 appears inside the proof of 9.4. The AI's miscitation of 8.24 (about squares) instead of 8.25 (about cubes) was considered as a potential E under the invalid inference mode, but the AI's text correctly describes the cube-number reasoning matching 8.25, making this a citation label error rather than a logical gap; under the lenience rule the verdict defaults to NOT-E. D7.19 in ai_only is a definition (over-citation). All divergences reduce to citation-depth differences.
**Audit Record**: CANDIDATE E — 9.5
  violated_claim : "by Proposition 8.24 the second number B is also cube"
  failure_mode   : invalid_inference
  missing_is     : expansion — the AI correctly describes the reasoning of 8.25 (cube-to-cube ratio, first cube implies second cube) but mislabels it as 8.24 (which is about squares); the logical support for the conclusion exists in the text, only the citation number is wrong
  evidence       : AI Step 5: "Since two numbers A and B have to one another the ratio which a cube number has to a cube number, and the first of them A is cube, therefore by Proposition 8.24 the second number B is also cube [8.24]" — 8.24 is about square numbers, not cube numbers; the correct proposition is 8.25
  why_not_terse  : CANNOT COMPLETE — this is not a genuine logical gap but a citation labeling error; the described reasoning is sound and matches 8.25. Under the lenience rule, verdict defaults to NOT-E.

### 9.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 9.6 establishes a proportionality chain (unit:A = A:B = B:C), then uses 8.19 (mean proportionals between similar solids), 8.8 (transferring continued proportion), and 8.23 (first of four continued proportionals is cube implies fourth is cube) to conclude A is cube. The AI takes a fundamentally different path: it directly computes B*A = (A*A)*A = A^3, which is cube by definitions D7.17 and D7.19, and then invokes Proposition 9.5 (if a cube number multiplied by any number makes a cube, the multiplied number is also cube) to conclude A is cube. Although the containment test shows that the heath_only items (8.19, 8.8, 8.23) appear inside Heath's proof of 9.5, the AI's backbone introduces a novel key intermediate conclusion not present in Heath (that B*A equals A^3 and is therefore cube by definition) and reduces the problem to an entirely different prior result (9.5). The AI's proof is logically complete and valid but follows a genuinely different logical strategy, warranting classification as D.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same logical backbone: decompose the composite number A into two factors using D7.13 and D7.15, then observe that the product of A with another number equals the product of three numbers, hence is solid. The AI proof explicitly cites D7.16 (definition of plane number) to name the intermediate result that A is plane, and D7.17 (definition of solid number) to formally justify calling the final product solid. Heath makes exactly the same argument but does not explicitly cite these definitions, relying on the reader's implicit understanding of what 'solid' means. Since the ai_only items are both definitions that the AI cites for explicitness while Heath leaves them implicit, and the key intermediate conclusions (factor decomposition, three-number product) are identical in both proofs, this is a citation-depth difference, not a backbone difference.

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: (1) establish the third term from the unit is square, (2) use 8.22 to extend squareness to all terms leaving out one, (3) establish the fourth term is cube, (4) use 8.23 to extend cubeness to all terms leaving out two, (5) combine to show the seventh is both cube and square. The citation difference lies entirely in how the initial square and cube properties are justified: Heath uses D7.20 (definition of proportional numbers) to show that the unit measures A the same number of times A measures B, and then concludes A multiplied by itself makes B (square) and A multiplied by B makes C (cube). The AI instead directly recognizes that A3 = r times r satisfies D7.18 (definition of square) and A4 = r times r times r satisfies D7.19 (definition of cube). These are definitional-level differences in justifying the same intermediate conclusions, making this a citation-depth difference rather than a backbone difference.

### 9.9
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decides the classification. Heath's proof of the square case uses a two-phase strategy: first invoking 9.8 to establish that every other term (the third, fifth, etc.) is square, then applying 8.22 to fill in the remaining terms. The AI proof takes a fundamentally different approach: it establishes that the unit itself is square (via D7.18), then applies 8.22 sequentially starting from the unit through every consecutive triple, covering all terms by direct induction without needing 9.8 at all. This constitutes a different logical backbone (Case B in Q2). The AI's path is logically valid under Q3: the unit is indeed square, and repeated application of 8.22 to consecutive triples correctly propagates the square property through all terms. Additionally, Heath's proof covers both the square and cube cases (using 8.23 and 9.3 for the cube case), but the statement given to the AI only specifies the square case, so the AI's omission of the cube case is not an error. The heath_only citations 8.23, 9.3 are exclusively for the cube case, while 9.8 is replaced by the AI's inductive approach from the unit.

### 9.10
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decides the classification. Heath's proof of the square part argues by contradiction through ratios: if an even-positioned term C is square and the adjacent odd-positioned term B is square (by 9.8), then B:C = A:B gives A,B the ratio of square to square, so by 8.26 (converse) A is square, contradicting the hypothesis. The AI instead uses 8.22 (in contrapositive/inverse form): for three consecutive terms in continued proportion, if the first is not square then the third is not square, and extends this by induction across all even-positioned terms. These are genuinely different logical backbones -- Heath reasons via ratios and similar plane numbers (8.26), while the AI reasons via properties of squares in continued proportion (8.22). The proof-tree containment test confirms 8.26 does not appear inside Heath's proof of 8.22 (which uses 8.20), so the routes are independent. Additionally, Heath's proof includes a cube part using 8.25 and 9.6 that the AI omits since the proposition statement concerns only squares. The AI's mislabeling of the inverse of 8.22 as 'the contrapositive' was considered as a candidate E (invalid inference), but the underlying mathematical result is sound in the geometric-sequence context, and under the lenience rule this is compressed-but-sound rather than a genuine logical gap. The AI's path is valid, yielding D.
**Audit Record**: CANDIDATE E — 9.10
  violated_claim : "if the first A2 is not square, then the third A4 cannot be square" — AI calls this the contrapositive of 8.22 but it is actually the inverse
  failure_mode   : invalid_inference
  missing_is     : expansion — the mathematical result is true in the geometric-sequence context; the AI compresses the justification by mislabeling the logical operation
  evidence       : AI Step 5: "8.22 states that if three numbers are in continued proportion and the first is square, then the third is square. We use the contrapositive: if the first A2 is not square, then the third A4 cannot be square." The actual contrapositive of 8.22 is "if third NOT square then first NOT square", not "if first NOT square then third NOT square."
  why_not_terse  : Cannot complete convincingly — while the labeling is incorrect, the underlying inference is sound in this context (for r^(k-1), r^k, r^(k+1) in geometric sequence, squareness of first and third are equivalent). This is compressed-but-sound, not a genuine logical gap. Reclassified to NOT-E per lenience rule.

### 9.11
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses a single key move: applying 7.15 (alternation for unit measures) to convert the proportion unit:B = D:E into the statement that B measures E according to the units in D, yielding the result directly. The AI proof takes a fundamentally different path, converting proportional relationships into multiplication statements via 7.19 (product equality from proportions), then establishing each term as a product of earlier terms (B = A*A, C = A*B, D = A*C), and using definitions D7.15 and D7.3 to translate multiplicative relationships into divisibility. The two proofs share zero citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different: Heath reasons through alternation of ratios and unit-counting, while the AI reasons through products and factors. Since the backbones differ (Case B in Q2), Q3 was applied: the AI's multiplication-based chain is logically complete from premises to conclusion, so the classification is D (path difference).

### 9.12
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determined this classification. Heath's proof uses proof by contradiction with iterative application of proportion theory (7.29 to establish coprimality, then 7.19/7.21/7.20 to show the prime must measure each successive term in the sequence, reaching a contradiction). The AI proof takes an entirely different approach: it uses 7.30 (a prime dividing a product must divide one of its factors) combined with direct finite descent. The AI establishes that An = A2 * A(n-1) from the continued proportion, applies 7.30 to conclude p divides A2 or A(n-1), and descends through shorter sequences until reaching the base case A3 = A2^2 where 7.30 yields p divides A2. The key intermediate conclusions differ completely: Heath's backbone involves coprimality assumptions, proportion equalities, and least-ratio arguments, while the AI's backbone involves product decomposition and the prime factor property. This is a genuine path difference. The AI's path is logically complete and valid, so Q3 confirms classification as D.

### 9.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Classification was decided at Q2 (Case A: same backbone, different citation depth). Both proofs follow the same descent argument: assume E measures D but is not among the proportional numbers, show E is not prime and that A is the only prime dividing E, so A measures E, then repeatedly divide out factors showing each quotient is also divisible only by A, descending through the proportional numbers until reaching a contradiction. The key intermediate conclusions are identical in both proofs. The citation differences are all depth-related: the AI cites 7.17 where Heath cites 7.19, but 7.17 appears inside Heath's proof of 7.19 (containment test satisfied), so the AI simply cites a sub-lemma rather than the composite result. Heath cites 9.8 to establish A*A = B while the AI derives this directly from the continued proportion. The AI's additional citations of D7.11, D7.15, and D7.3 are definitions cited explicitly by the AI but used implicitly by Heath. All differences are citation-depth variations on the same logical backbone.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: (1) assume a new prime measures A, yielding a factorization; (2) apply VII.30 to conclude the original primes must divide one of the factors; (3) rule out the new prime factor since it is prime and distinct; (4) conclude the original primes all divide the remaining factor; (5) derive a contradiction since that factor is less than A. The AI's ai_only citations (CN5, D7.11, D7.15, D7.2, D7.3, D7.5) are exclusively definitions and a common notion that Heath leaves implicit, representing over-citation of foundational material rather than any structural difference. Since the backbones are identical and the citation difference is purely one of depth, this is a granularity difference (G).

### 9.15
**Category**: Path difference
**Jaccard**: 0.556
**Analysis**: The forward dependency gate passed (all citations are from Books 7-8, prior to 9.15). Q1 found no logical errors: all three cases are addressed and each step is valid. Q2 revealed that while cases 1 (A+B prime to C) and 2 (B+C prime to A) share the same backbone in both proofs, case 3 (A+C prime to B) follows genuinely different intermediate conclusions. Heath uses algebraic identities II.3 and II.4 to expand DF^2 and then applies separando twice to strip away terms, establishing that A+C is prime to B. The AI instead uses VII.26 to show A is prime to C, then VII.28 to get A+C prime to both A and C, then first-principles divisibility arguments to show A+C is prime to each of p and q individually, and finally VII.24 to conclude A+C is prime to pq=B. These are substantively different logical paths through different intermediate conclusions, so Case B (different backbone) applies. Q3 confirms the AI path is logically valid: each step is properly justified and the chain runs from premises to conclusion without gaps. Classification is D (path difference).

### 9.16
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: assume for contradiction that A:B = B:C, apply 7.21 to establish A and B are the least numbers in their ratio, apply 7.20 to conclude A measures B, then derive a contradiction from A being a common measure of coprime numbers A and B. The AI proof cites three additional definitions (D7.1, D7.12, D7.2) that Heath uses implicitly without citation. Since ai_only contains only definitions and heath_only is empty, and the key intermediate conclusions are identical in both proofs, this is a same-backbone, different-citation-depth case, yielding Granularity difference (G).

### 9.17
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 9.17 by direct contradiction: assuming D:E = A:B, he uses alternation (7.13) to get A:D = B:E, then applies 7.21 and 7.20 to show A measures B, chains through the continued proportion to show A measures D, and derives a contradiction with A and D being prime. The AI takes a fundamentally different route: it uses 8.1 to establish the numbers are least in that ratio, 7.22 to show consecutive terms are prime, and then reduces the problem to 9.16 (if two numbers are prime to one another, the second is not to any other as the first is to the second), applied to the last two terms. The citation sets are completely disjoint (Jaccard = 0.0), and the key intermediate conclusions differ — Heath's backbone involves alternation and chaining divisibility through the proportion, while the AI's backbone involves establishing consecutive terms are prime and reducing to the previous proposition. This is a genuine path difference with a valid alternative proof strategy.

### 9.18
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof first separates the case where A and B are prime to one another, citing 9.16 to establish that no third proportional exists in that case, then handles the non-prime case with a sub-dichotomy on whether A measures B-squared. The AI proof instead uses a single exhaustive dichotomy (A measures B-squared or A does not measure B-squared) that subsumes the prime case without needing 9.16 at all. This represents a genuinely different logical backbone: Heath's three-branch structure (prime, non-prime with divisibility, non-prime without) versus the AI's two-branch structure (divisibility, non-divisibility). Both proofs share the use of 7.19 for the proportionality step and the contradiction argument for the impossibility case, but the overall organizational strategy differs. The AI's path is logically valid since its dichotomy is exhaustive and each branch is soundly argued, yielding classification D.

### 9.19
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 determined the classification. Heath's proof organizes the investigation into four cases based on whether the three numbers are in continued proportion and whether their extremes are coprime, using propositions 9.17, 7.14, 7.21, and 7.20 as key tools across the different cases. The AI proof takes a fundamentally different and more direct approach: it reduces the entire question to a single divisibility criterion, proving that a fourth proportional D to A, B, C exists if and only if A measures the product B*C. The AI uses only 7.19 (products of extremes and means in a proportion are equal, and conversely) to establish both directions. Since the two proofs have entirely different key intermediate conclusions and logical backbones — Heath's multi-case analysis via primality and continued proportion versus the AI's unified divisibility argument — but the AI's path is logically complete and valid, the classification is D (path difference).

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share identical key intermediate conclusions: forming DE as the least number measured by the assigned primes, constructing EF = DE + 1, splitting into two cases (EF prime or not), and in the composite case using 7.31 to find a prime factor G that cannot equal any assigned prime (via the contradiction that it would measure the unit). The AI proof cites six additional foundational items (CN5, D7.1, D7.3, D7.11, D7.13, D7.15) that are all definitions and a common notion which Heath uses implicitly without citation. The heath_only set is empty, confirming the AI omits nothing. This is a clear Case A: same backbone with the AI providing greater citation depth for foundational definitions and axioms.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: each even summand has a half part, so the whole sum also has a half part, making it even by Definition 7.6. The AI proof explicitly invokes Common Notion 2 (if equals be added to equals, the wholes are equal) to justify that combining the half-parts of each summand yields two equal groups, while Heath simply states that 'the whole AE also has a half part' without citing CN2. The underlying logical backbone is identical; the AI merely makes explicit an axiom-level step that Heath treats as obvious. Since ai_only contains only CN2 (a common notion, not a substantive theorem) and heath_only is empty, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 9.22
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decides the classification. Both proofs follow the same logical backbone: decompose each odd number into an even number plus a unit (D7.7), sum the even parts and show the result is even (9.21), note the sum of units equals the even multitude and is therefore even, then conclude the whole sum is even as the sum of two even numbers (9.21). The AI proof explicitly cites CN2 for the algebraic regrouping step and D7.6 for the definition of even number, both of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only foundational axioms/definitions that represent over-citation of steps Heath leaves implicit, this is a same-backbone, different-depth scenario classifying as G.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 9.23 follow the same logical backbone and cite exactly the same propositions. Both proofs subtract one odd number from the collection (leaving an even count of odd numbers), apply 9.22 to conclude the partial sum is even, decompose the remaining odd number into an even number plus a unit via D7.7, combine the even quantities using 9.21, and conclude the total is odd by D7.7. The citation sets are identical (Jaccard 1.0) with no ai_only or heath_only items. Since the key intermediate conclusions match and the citation sets are equal, this is a perfect match under the protocol's final check.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that AB and BC each have half parts (by D7.6, since both are even), then conclude that the remainder AC also has a half part and is therefore even. The only difference is that the AI explicitly cites CN3 (if equals be subtracted from equals, the remainders are equal) to justify the subtraction of the halves, whereas Heath performs this same step implicitly without citing the underlying axiom. Since ai_only contains only CN3 (a Common Notion / axiom) and heath_only is empty, this is a clear case of the AI over-citing at a finer axiomatic level while following the identical argumentative path, which is a citation-depth difference characteristic of Granularity difference (G).

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 9.25 use exactly the same citation set {9.24, D7.7} and establish the same key intermediate conclusions. Both proofs decompose the odd number BC into an even part and a unit using D7.7, apply Proposition 9.24 to conclude that a difference of two even numbers is even, and then use D7.7 again to conclude that the remainder differs from an even number by a unit and is therefore odd. The only difference is in the labeling of segments (Heath uses CD as the unit and DB as the even part, while the AI uses BD as the unit and DC as the even part), but the logical backbone and citation set are identical. Since ai_used equals heath_refs exactly and the key intermediate conclusions match, this is classified as a Perfect match (P).

### 9.26
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical structure: both subtract a unit from each odd number to obtain two even numbers, citing D7.7, then apply 9.24 to conclude the remainder is even. The key intermediate conclusions (AD is even, DC/CD is even, AC/CA is even) are the same in both proofs, and the citation sets are exactly equal (ai_used = heath_refs = {9.24, D7.7}, Jaccard = 1.0). Since Q2 confirms the same backbone and the citation sets match perfectly, the classification is P (Perfect match).

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Classification was decided at Q2/Q3. Heath proves the proposition directly by subtracting a unit from the odd number AB to get even DB, then using 9.24 (even minus even is even) to show that the intermediate segment CD is even, and finally applying Def. 7.7 to conclude the remainder CA is odd. The AI instead uses proof by contradiction: assuming the remainder C is even, it applies 9.21 (sum of even numbers is even) to B + C to derive that A would be even, contradicting the hypothesis. These represent fundamentally different logical backbones -- Heath uses direct decomposition via unit subtraction and even-minus-even (9.24), while the AI uses reductio ad absurdum with sum-of-evens (9.21). The AI's contradictory path is logically complete and valid, so this is a path difference (D).

### 9.28
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) express the product C as a sum of A copies of B via Definition 7.15, (2) observe that each summand B is even, (3) apply Proposition 9.21 to conclude that the sum of even numbers is even, hence C is even. The only citation difference is that the AI explicitly cites Definition 7.6 (the definition of even number) when noting that B is even, whereas Heath simply states 'And B is even' without referencing the definition. This is a straightforward over-citation of a definition, which is a citation-depth difference, not a backbone difference. Since the key intermediate conclusions are identical and the citation difference is purely granular, the classification is G.

### 9.29
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use the definition of multiplication (D7.15) to express the product C as a sum of A copies of B, observe that each term is odd and the multitude of terms is odd, then apply Proposition 9.23 to conclude the sum is odd. The only difference is that the AI explicitly cites Definition 7.7 (the definition of an odd number) when noting that B is odd, while Heath simply states the oddness of A and B without citing a definition. Since ai_only contains only a definition [D7.7] and heath_only is empty, and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference falling under Case A of Q2, yielding Granularity difference (G).

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) let the odd number A measure the even number B some number of times, (2) show by contradiction that this multiplier cannot be odd (since odd times odd yields odd, contradicting B being even), (3) conclude the multiplier is even, and (4) deduce that A therefore measures the half of B. The sole substantive citation difference is that Heath uses 9.23 (sum of odd-many odd numbers is odd) while the AI uses 9.29 (odd times odd is odd). The proof-tree containment test confirms this is a depth difference: Heath's own proof of 9.29 directly cites 9.23, so the AI is citing 9.29 as a packaged unit while Heath works at the more granular level of 9.23. The remaining ai_only items (CN1, CN5, D7.15, D7.3, D7.6, D7.7) are all definitions and common notions representing over-citation of foundational material, a hallmark of granularity difference.

### 9.31
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath proves 9.31 by contradiction: assuming A and 2B share a common factor D, D must be odd (since it divides odd A), and by 9.30 an odd divisor of the even number 2B must also divide B, yielding a contradiction with A and B being coprime. The AI takes a completely different direct approach: since A is odd, 2 does not measure A, and since 2 is prime, 7.29 gives that 2 and A are coprime; combined with the given that B is coprime to A, 7.24 yields that the product 2B is coprime to A. The key intermediate conclusions are entirely different (Heath: odd divisor of even number measures its half; AI: 2 is coprime to A, then multiplicative property of coprimality), constituting a genuine path difference. The AI's chain is logically complete with every step supported by valid citations, so Q3 confirms validity.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establishing that the sequence of doubled numbers forms a continued proportion from the unit with 2 (a prime) as the second term, applying 9.13 to show the number is measured only by the proportional numbers, observing that all those proportional numbers (other than the unit) are even, and concluding that the number is even-times even only via D7.8. The AI proof adds explicit citations to definitions D7.11 (prime), D7.6 (even number), and D7.9 (even-times odd), and includes an explicit proof by contradiction that the number is not even-times odd, whereas Heath treats this as immediate from the structure of the argument. Since heath_only is empty and ai_only contains only definitions, this is a clear Case A (same backbone, different citation depth), yielding G.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish that the number is even-times odd via D7.9, (2) assume for contradiction that it is also even-times even (D7.8), (3) derive that the half would be measured by an even number and hence be even, contradicting the hypothesis that the half is odd. The AI proof elaborates this same argument with substantially more detail, explicitly citing definitions (D7.3, D7.6, D7.15) and propositions (7.16 commutativity, 9.28 odd times even is even) to justify steps that Heath handles implicitly in a single sentence. The heath_only set is empty, confirming that the AI covers everything Heath references. All ai_only citations are either definitions or propositions that fill in sub-steps of the same reasoning chain, making this a citation-depth difference rather than a path difference.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: first establishing the number is even-times even because its half is not odd (via Definition 7.8), then establishing it is even-times odd through a halving/bisection argument showing that since the number is not among those continually doubled from a dyad, repeated halving must eventually reach an odd number. The AI proof adds explicit citations to definitions (D7.6, D7.7, D7.9, D7.2) that Heath uses implicitly, and cites Proposition 9.32 to formally characterize the numbers continually doubled from a dyad, whereas Heath references this concept directly from the hypothesis without citing a specific proposition. The heath_only set is empty, confirming no substantive steps are missing from the AI proof. All ai_only items represent citation-depth differences rather than backbone divergence.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) apply separando to the continued proportion to derive equal ratios of successive differences to their respective terms, (2) apply VII.12 to sum the antecedents and consequents, (3) simplify the telescoping sum to reach the conclusion. The only substantive difference is which proposition licenses the separando step: Heath uses VII.11 (separando for numbers) together with VII.13 (alternation for numbers), while the AI uses V.17 (separando for magnitudes, the more general Book V result). The AI's additional citations (CN2, CN3, D5.8, D7.20) are common notions and definitions that reflect over-citation rather than a different proof path. Since both proofs establish the same key intermediate conclusions through the same logical structure, differing only in the specific propositions cited to justify the separando step, this is a citation-depth difference (Case A of Q2), yielding G.

### 9.36
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 reveals genuinely different backbones. Heath's proof uses proportional reasoning (7.14 ex aequali, 7.19 product-proportion) to establish the geometric series relationships, then employs an elaborate uniqueness argument via the 'least numbers' chain (7.21 primes-are-least, 7.20 least-measure-proportionals) to show no other number can divide FG. The AI takes a structurally different approach: it uses 9.35 to derive the closed-form sum S = 2*A_n - 1, enumerates divisors of A_n via 9.13 and 9.11, then determines divisors of P = S*A_n directly using 7.29 (prime-to-non-multiple) and 7.30 (prime dividing product divides factor). While both proofs share 9.13, 9.35, 7.29, and D7.22, the key intermediate conclusions differ: Heath reasons through proportional sequences and the least-numbers argument, while the AI reasons through direct divisor enumeration and algebraic summation. The proof-tree containment test shows that 7.19, 7.20, 7.21 do appear inside Heath's proof of 7.30, but in Heath's 9.36 proof these propositions are used independently in a different logical chain (not re-deriving 7.30), so this is genuine path divergence rather than citation-depth difference. The AI's path is logically valid under Q3, yielding classification D.
