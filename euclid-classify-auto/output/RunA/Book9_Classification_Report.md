# Book 9 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 3 | 9.23, 9.25, 9.26 |
| Granularity difference (G) | 15 | 9.4, 9.7, 9.8, 9.14, 9.20, 9.21, 9.24, 9.28, 9.29, 9.30, 9.32, 9.33, 9.34, 9.35, 9.36 |
| Path difference (D) | 16 | 9.1, 9.2, 9.3, 9.5, 9.6, 9.11, 9.12, 9.13, 9.15, 9.16, 9.17, 9.18, 9.19, 9.22, 9.27, 9.31 |
| AI proof error (E) | 2 | 9.9, 9.10 |

**Total**: 36 propositions

## Error Details

| Proposition | Error type | Details |
|---|---|---|
| 9.9 | Missing case | CANDIDATE E — 9.9   violated_claim : The cube case: 'if the number after the unit be cube, all the rest will also be cube'   failure_mode   : missing_case   missing_is     : support   evidence       : |
| 9.10 | Invalid inference | CANDIDATE E -- 9.10   violated_claim : "by 8.25, A is also square" (Step 3, and repeated in Steps 4-5)   failure_mode   : invalid_inference   missing_is     : support -- 8.25 is about cubes; the AI ne |

## Per-Proposition Analysis

### 9.1
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Heath's proof constructs D = A*A (square), establishes the ratio A:B = D:C via 7.17, transfers the mean proportional from A,B to D,C via 8.8, then applies 8.22 (if three numbers in continued proportion and the first is square, the third is also square). The AI takes a fundamentally different and more direct route: after obtaining mean proportional G between A and B via 8.18 (the one shared citation), it uses 7.19 to conclude that A*B = G*G (since A:G :: G:B implies the product of extremes equals the product of means), and then C = G*G is square by definition. The key intermediate conclusions differ entirely: Heath works through an auxiliary square D and ratio transfer, while the AI directly identifies C as a product of equal factors. Both paths are logically complete, making this a valid path difference (D).

### 9.2
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof introduces D = A*A, establishes A:B = D:C via 7.17, argues D and C are similar plane numbers (both square), uses 8.18 to get a mean proportional between D and C, then transfers that mean proportional to A and B via 8.8, and finally applies 8.20. The AI takes a fundamentally different path: it decomposes C = k*k by the definition of square number (D7.18), observes A*B = k*k, and directly applies the converse of 7.19 to conclude A:k = k:B, establishing k as a mean proportional between A and B without the intermediate auxiliary square D or the transfer via 8.8. Both proofs share only 8.20 as the final step. The AI's path is logically sound — 7.19's converse validly yields proportionality from equal products — but the key intermediate conclusions differ entirely, making this a genuine path difference.

### 9.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof establishes two mean proportionals between the unit and A (using VII. Def. 20), then uses VIII.8 to transfer those mean proportionals to the interval between A and B, and finally applies VIII.23 (if four numbers are in continued proportion and the first is cube, the fourth is also cube) to conclude B is cube. The AI proof takes a fundamentally different route: it uses the elementary proportion results 7.17 and 7.19 to build the continued proportion C:D = D:A = A:E directly, then algebraically derives that B = E*D = D^2*D = D^3, concluding B is cube by definition D7.19. The Jaccard similarity is 0.0 with completely disjoint citation sets, reflecting genuinely different logical backbones. The AI's path is logically valid throughout, with each step correctly following from the cited propositions, so Q3 confirms a valid different path yielding classification D.

### 9.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) A*A = D is cube by 9.3, (2) A:B = D:C by 7.17, (3) two mean proportionals exist between A and B, (4) therefore two mean proportionals exist between D and C by 8.8, (5) D is cube so C is cube by 8.23. The only substantive citation difference is that Heath uses 8.19 (between two similar solid numbers there are two mean proportionals) while the AI uses 8.12 (between two cube numbers there are two mean proportionals). Since cube numbers are similar solid numbers, both propositions yield the same intermediate conclusion at the same logical position — the AI simply chose the more specific result. The AI's additional citations of D7.15 and D7.19 are explicit definition references (over-citation). All key intermediate conclusions are identical, making this a same-backbone, different-citation-depth case (Case A of Q2).

### 9.5
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Heath's proof works by forming D = A*A (cube by 9.3), establishing A:B = D:C via 7.17, using 8.19 to get two mean proportionals between the cubes D and C, transferring those proportionals to A and B via 8.8, then concluding B is cube via 8.23. The AI proof takes a fundamentally different route: it uses 8.12 to place two mean proportionals D, E directly between the cubes A and C, then uses 8.7 to show A measures D, constructs a factor f such that D = A*f, and through ratio arithmetic (7.17, 5.11, 5.9) establishes E = D*f and C = E*f, yielding B = f*f*f, hence B is cube by D7.19. The key intermediate conclusions differ — Heath's backbone pivots on transferring mean proportionals from D,C to A,B and applying 8.23, while the AI explicitly constructs the cube root of B. The only shared citation is 7.17. The AI's path is logically complete with every step properly cited, so this is a valid path difference.

### 9.6
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof works through proportional number theory, establishing the chain of ratios 1:A = A:B = B:C, then using the similarity of cube numbers (VIII.19) and transfer of mean proportionals (VIII.8) to conclude A is cube via VIII.23. The AI takes a completely different path: it observes that C = A*A is cube by hypothesis, then shows A*A*A is cube by the definition of cube (D7.19), and finally applies Proposition 9.5 (if a cube multiplied by a number produces a cube, then that number is cube) to conclude A is cube. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different -- Heath's intermediates concern proportional relationships and mean proportionals, while the AI's sole intermediate is that A^3 is a cube number. The AI's path is logically valid and complete, making this a genuine path difference (D).

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) the composite number A is measured by some number (D7.13), (2) A can be expressed as a product of two numbers (D7.15), and (3) the final product equals three numbers multiplied together, making it solid. The only difference is that the AI explicitly cites D7.17 (the definition of a solid number) when concluding that the product of three numbers is solid, while Heath simply states the conclusion without citing the definition. Since D7.17 is a definition rather than a substantive proposition, this is a straightforward case of over-citation at the definitional level — the AI is more explicit about which definition warrants the final step. The backbones are identical, and the citation difference is purely one of depth, making this Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: they establish that the 3rd term from the unit is square (by showing the ratio from the unit implies the term equals itself multiplied by itself), the 4th term is cube (by extending the multiplication argument), then use VIII.22 to propagate squareness every two terms, VIII.23 to propagate cubeness every three terms, and combine both results at the 7th term. The only difference is in which definitions are cited: the AI cites D7.18 (definition of square number) and D7.19 (definition of cube number) when concluding terms are square or cube, while Heath cites D7.20 (definition of proportional numbers) when setting up the proportional reasoning. Since the entire symmetric difference consists of definitions rather than substantive propositions, and the key intermediate conclusions and logical structure are identical, this is a citation-depth difference falling under Case A of Q2.

### 9.9
**Category**: AI proof error
**Jaccard**: 0.400
**Analysis**: Proposition 9.9 as proved by Heath contains two cases: (1) if the number after the unit is square, all the rest are square, and (2) if the number after the unit is cube, all the rest are cube. Heath's proof explicitly addresses both cases, using 9.8 and 8.22 for the square case, and 9.8, 9.3, and 8.23 for the cube case. The AI proof only addresses the square case (Steps 1-8) and never mentions cubes at all. This is a genuine missing case under Q1(a): the cube case is entirely absent from the AI proof, not merely compressed or terse. The audit record completes convincingly since the omission is unambiguous — there is no general argument or reference in the AI proof that could cover the cube case.
**Audit Record**: CANDIDATE E — 9.9
  violated_claim : The cube case: 'if the number after the unit be cube, all the rest will also be cube'
  failure_mode   : missing_case
  missing_is     : support
  evidence       : Heath's proof explicitly addresses two cases: 'let A, the number after the unit, be square' and 'Next, let A be cube'. The AI proof text only addresses the square case (Steps 1-8) and never mentions cubes. The heath_only citations 8.23 and 9.3 are precisely the propositions used in the cube case.
  why_not_terse  : This is not brevity — the entire second case (cube) is absent from the AI proof. There is no general argument or reference that covers the cube case.

### 9.10
**Category**: AI proof error
**Jaccard**: 0.500
**Analysis**: The AI proof of 9.10 cites proposition 8.25 to conclude that a number is square (Steps 3, 4, and 5), but 8.25 states 'If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube' -- it concerns cubes, not squares. The correct proposition for the square case is 8.24 ('If two numbers have to one another the ratio which a square number has to a square number, and the first be square, the second will also be square'). Since the AI explicitly cites 8.25 as its warrant and 8.25 does not entail any conclusion about square numbers, this is an invalid inference under Q1(b). The audit record completes convincingly: the missing element is support (not mere expansion), the cited proposition genuinely does not entail the conclusion, and this is not a matter of terseness or compression but of citing the wrong proposition entirely. Heath correctly uses 8.25 only in the cube case and uses 8.26 (converse) for the square case.
**Audit Record**: CANDIDATE E -- 9.10
  violated_claim : "by 8.25, A is also square" (Step 3, and repeated in Steps 4-5)
  failure_mode   : invalid_inference
  missing_is     : support -- 8.25 is about cubes; the AI needs 8.24 (squares) but cites 8.25 (cubes)
  evidence       : AI Step 3: "Since B is square and A has to B the ratio of a square number to a square number, by 8.25, A is also square." Proposition 8.25: "If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube." The AI applies 8.25 to a square-ratio context where it does not apply.
  why_not_terse  : The AI explicitly names 8.25 as the warrant for its conclusion about squares. 8.25 concerns cubes exclusively and cannot justify any conclusion about square numbers. The correct warrant is 8.24, which the AI does not cite.

### 9.11
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof of 9.11 relies on a single key mechanism: alternation of ratios via 7.15, directly converting the fact that the unit measures D into the conclusion that B measures E according to D. The AI proof takes a fundamentally different path, using the multiplicative structure of geometric sequences beginning from unity. It builds up from showing A multiplied by each term yields the next term (via definitions D7.15 and D7.20), then generalizes to show that for any two terms T_i and T_j with i < j, T_i multiplied by T_{j-i+1} equals T_j, using propositions 7.14 (ex aequali), 7.16 (commutativity of multiplication), 7.17 (ratio preservation), and 8.7. The key intermediate conclusions differ entirely: Heath uses ratio alternation while the AI uses recursive multiplication properties. Since the AI's multiplicative approach is mathematically sound and reaches the correct conclusion through validly cited propositions, this is a valid different path, yielding classification D.

### 9.12
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 determined this classification. Heath's proof uses proof by contradiction, assuming the prime E does not measure A, then descending through the specific chain D to C to B to A-squared using ratio and proportion arguments (7.19, 7.20, 7.21) combined with the coprimality result (7.29), ultimately reaching a contradiction. The AI proof takes a fundamentally different approach: it uses induction on the number of terms in the continued proportion, applying 7.30 (if a prime divides a product it divides a factor) at each step. The AI decomposes L = A*K via 7.19 from the proportion 1:A = K:L, then uses 7.30 to conclude p|A or p|K, descending to shorter sequences until the base case of three terms where B = A*A and 7.30 gives p|A. The key intermediate conclusions differ entirely: Heath establishes E|C, then E|B, then E|A via contradiction; the AI establishes a descent through 7.30 at each level. The proof-tree containment test confirms this is genuine path divergence rather than citation-depth difference: while 7.30 does subsume 7.29, 7.21, and 7.20 from heath_only, the remaining heath_only items 9.11 and 9.8 are not inside Heath's proof of 7.30, and more importantly the overall proof architecture (contradiction vs induction) is different. The AI proof is logically complete under the hardened 1(b) standard, so Q3 confirms category D.

### 9.13
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 reveals fundamentally different backbones. Heath's proof uses an intricate descent argument: assuming E measures D and is not among A, B, C, Heath shows E is composite (via 9.12 and 7.31), that A measures E, then introduces quotient F, proves F is not among A, B, C, and repeats the argument, descending through F, G, H using proportionality (7.19) and 9.11, ultimately reaching a contradiction via 9.8 when H measures A (prime). The AI takes a markedly different path: it shows directly that every prime factor of any divisor C of A_n must equal A_2 (using 9.12 and transitivity via 7.20), concludes C is a power of A_2, observes the proportional numbers are exactly the successive powers of A_2, and applies 9.11 to conclude C must be among them, reaching contradiction immediately. The AI's argument is logically sound throughout: the step from 'only prime factor is A_2' to 'C is a power of A_2' is terse but valid, and the identification of proportional terms as powers of A_2 follows from the definition of continued proportion. This constitutes a genuinely different valid path, not merely a granularity difference, since the key intermediate conclusions (prime-factor characterization vs. descent through quotients) are structurally distinct.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same contradiction structure: assume a prime E distinct from B, C, D measures the least number A measured by B, C, D; deduce A = E*F; apply 7.30 to show B, C, D each measure E or F; eliminate E (since E is prime and distinct); conclude B, C, D measure F; derive contradiction since F < A. The AI proof works through B, C, D individually (Steps 3-7) rather than collectively as Heath does, and explicitly cites definitions (D7.1, D7.3, D7.11, D7.15) and a common notion (CN5) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions and common notions representing over-citation of foundational items, this is Case A (same backbone, different citation depth), yielding G.

### 9.15
**Category**: Path difference
**Jaccard**: 0.556
**Analysis**: Q2 reveals a different backbone between the two proofs. For the first two cases (A+B prime to C and B+C prime to A), Heath uses II.3 to decompose the product FD*DE into the sum DE^2 + DE*EF, whereas the AI directly factors A+B as p*(p+q) without needing any algebraic identity proposition. For the third case (A+C prime to B), Heath uses II.4 to expand DF^2, then applies separando twice to establish that DE^2 + EF^2 is prime to DE*EF, whereas the AI uses proof by contradiction to show p^2+q^2 is prime to p and to q separately, then combines via VII.24. Both approaches are logically complete, but the AI avoids the Book II algebraic identities entirely, substituting direct factoring and proof by contradiction. This constitutes a genuine path difference, not merely a granularity difference, since the key intermediate conclusions differ in structure.

### 9.16
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works entirely within ratio theory: since A,B are coprime they are the least in their ratio (7.21), and least numbers measure proportional numbers equally (7.20), so A measures B, contradicting coprimality. The AI proof takes a fundamentally different route via products: it converts the proportion A:B=B:C into A*C=B^2 using 7.19, then invokes 7.25 to show A and B^2 are coprime, which contradicts A dividing B^2 (forcing A to be a unit). The key intermediate conclusions are entirely different — Heath reasons about least ratios and measuring, while the AI reasons about products, divisibility, and coprimality of squares. This is a genuine backbone difference (Case B). The AI's alternative path is logically complete under Q3, with each step properly supported by cited propositions, so the classification is D.

### 9.17
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof uses alternation (7.13) to get A:D = B:E, then the coprimality/least-ratio facts (7.21, 7.20) to conclude A measures B, and chains divisibility through the continued proportion (A|B, B|C implies A|C, then A|D) to reach a contradiction with gcd(A,D)=1. The AI takes an entirely different route: it invokes 8.1 to establish the terms are the least in their ratio, then uses 8.2 to express the first and last terms as powers of the base ratio p:q (A_1 = p^(n-1), A_n = q^(n-1)), sets up a cross-multiplication via 7.19, and derives that p divides q^n. Since 7.27 guarantees p^n and q^n are coprime, p must be a unit, making A_1 a unit and contradicting it being a number. The two proofs share zero citations (Jaccard = 0.0) and their key intermediate conclusions are completely different: Heath argues through a divisibility chain along the terms, while the AI argues through the explicit power structure of the least continued proportion. Although the heath_only items 7.20 and 7.21 appear inside Heath's proof of 8.1 (which the AI cites), the AI does not merely subsume Heath's argument under 8.1; rather, 8.1 serves as the launching point for a fundamentally different algebraic strategy. This is a genuine path difference.

### 9.18
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Classification was decided at Q2/Q3. Heath's proof first distinguishes whether A and B are prime to one another, invoking 9.16 to dismiss that case, then handles the non-prime situation by checking whether A measures B-squared. The AI proof omits the prime/not-prime distinction entirely and uses a single exhaustive dichotomy: either A measures B-squared or it does not. This is a genuinely different logical backbone -- Heath has a three-branch structure (prime, not-prime-and-measures, not-prime-and-does-not-measure) while the AI has a two-branch structure (measures, does-not-measure). The AI's approach is valid because the measure/not-measure dichotomy is exhaustive and the prime case is subsumed under the not-measuring case. Both proofs share the core use of 7.19 for the positive case and contradiction for the negative case, but the structural difference in case organization and the AI's omission of 9.16 constitute a different path rather than mere granularity difference. The AI's path is logically complete and sound, yielding classification D.

### 9.19
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof uses a four-case analysis based on whether the three numbers are in continued proportion and whether their extremes are prime to one another, employing 9.17, 7.14, 7.21, and 7.20 to establish impossibility in the prime-extremes cases and 7.19 for the constructive cases. The AI proof takes an entirely different structural approach: it bypasses the case analysis altogether and provides a single unified criterion that a fourth proportional to A, B, C exists if and only if A measures the product B times C. The AI's backbone relies solely on the biconditional in 7.19 (proportionality iff product equality) combined with definitions D7.15 and D7.3 for the measuring relation. Since the key intermediate conclusions differ fundamentally — Heath argues through prime number properties and continued proportion cases while the AI argues through a direct divisibility criterion — this is Case B (different backbone) at Q2, leading to Q3. At Q3, the AI's path is logically complete: each step follows validly, the biconditional is correctly established, and the impossibility direction is proved by clean contradiction. Therefore the classification is D (path difference).

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: take the LCM (or any common multiple) of the assigned primes, add a unit to form a new number, then split into two cases (new number is prime, or new number is composite and measured by some prime G via 7.31). In both cases a contradiction argument shows the new prime cannot equal any of the assigned primes. The AI proof's only divergence from Heath is the explicit citation of six definitions (D5.1, D7.1, D7.11, D7.13, D7.15, D7.3) that Heath leaves implicit. Since heath_only is empty and all ai_only items are definitions, this is a clear case of over-citation at finer granularity with no backbone difference, yielding G.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusion: each even summand has a half part, and the collection of all half parts yields a half of the whole sum, making it even by Definition 7.6. The AI proof makes the 'adding equals to equals' step explicit by citing CN2, while Heath's proof performs the same reasoning implicitly ('so that the whole AE also has a half part'). The sole ai_only citation CN2 is a Common Notion (not a substantive proposition), representing over-citation of a foundational axiom rather than a different logical path. Since the backbones align and the citation difference is purely one of depth, this is a granularity difference.

### 9.22
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Heath's proof decomposes each odd number by subtracting a unit, sums the even remainders (9.21), notes the even count of units, then adds those two even quantities (9.21) to get an even total. The AI proof instead pairs the odd numbers (since their multitude is even, by D7.6), shows each pair of odd numbers sums to an even number (decomposing via D7.7, adding via CN2, concluding evenness via 9.21), then sums the even pair-sums (9.21). These represent genuinely different logical backbones: Heath works by subtract-units-then-recombine while the AI works by pair-then-sum. The ai_only items (CN2, D7.6) are not mere over-citations but reflect the AI's distinct pairing strategy. Since the different path is logically complete under the hardened 1(b) standard, the classification is D.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21, 9.22, and D7.7 are all prior to 9.23). Q1 found no logical defects: the AI proof correctly separates the last odd number from the rest, shows the remaining even-count sum is even via 9.22, decomposes the last odd number into an even number plus a unit via D7.7, combines the even parts via 9.21, and concludes oddness by D7.7. Q2 confirmed both proofs share the same logical backbone: isolate the last odd number, show the partial sum is even, then show adding the last odd number produces an odd total. The citation sets are identical (ai_used = heath_refs = {9.21, 9.22, D7.7}, Jaccard = 1.0), and the key intermediate conclusions match, so the perfect match check assigns category P.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: (1) AB is even so it has a half part, (2) BC is even so it has a half part, (3) the remainder AC therefore also has a half part and is even. The AI proof explicitly cites CN3 (if equals be subtracted from equals, the remainders are equal) to justify deriving that AC consists of two equal parts, while Heath's proof simply states that the remainder also has a half part without citing any common notion. The ai_only set contains only CN3, a Common Notion (axiom-level citation), and heath_only is empty. This is a classic over-citation pattern where the AI makes explicit an axiom that Heath uses implicitly, with no difference in the key intermediate conclusions or logical path.

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 9.25 use identical citation sets (9.24 and D7.7) and argue through the same key intermediate conclusions: decomposing the odd subtrahend into an even number plus a unit via D7.7, applying 9.24 to show that subtracting the even part from the original even number yields an even remainder, and then observing that the final result differs from that even remainder by a unit and is therefore odd by D7.7. Since the logical backbones match and the citation sets are identical (Jaccard 1.0, with empty ai_only and heath_only), this is a perfect match under the protocol's final check.

### 9.26
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI and Heath proofs of 9.26 follow the same logical backbone: subtract a unit from the odd number AB to get even remainder AD (D7.7), establish that CD is also even (D7.7), and conclude that the remainder CA is even by 9.24. The AI proof is more explicit in justifying why CD is even (showing that the unit subtracted from BC yields the same point as the unit subtracted from AB), but this is additional detail, not a different path. The citation sets are identical: both use exactly 9.24 and D7.7, yielding Jaccard 1.0. Since the key intermediate conclusions match and the citation sets are equal, this is a perfect match (P).

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification as D (Path difference). Heath proves 9.27 directly: from odd AB, subtract unit AD to get even DB, then since DB and BC are both even, their difference CD is even by 9.24, leaving CA odd by D7.7. The AI instead uses proof by contradiction: assuming the remainder C is even, it applies 9.21 (sum of even numbers is even) to conclude B+C=A would be even, contradicting A being odd. The key intermediate conclusions differ fundamentally — Heath's backbone relies on subtracting a unit and applying 9.24 (even minus even is even) to establish an even intermediate, while the AI's backbone relies on assuming evenness of the remainder and applying 9.21 (sum of evens is even) to derive a contradiction. Since the logical backbones are genuinely different and the AI's proof by contradiction is logically complete and sound, this is a valid different path.

### 9.28
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: (1) express the product C as B added to itself A times via D7.15, (2) observe that since B is even each summand is even, and (3) apply 9.21 to conclude the sum of even numbers is even. The AI additionally cites D7.6 (the definition of even number) when establishing that B and each summand are even, while Heath leaves this implicit. Since heath_only is empty and ai_only contains only a definition (D7.6), this is a straightforward case of over-citation at the definition level, which is a citation-depth difference under Case A of Q2.

### 9.29
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) C is the product of A and B and hence equals a sum of copies of one factor repeated as many times as the units in the other (by Definition 7.15), (2) each summand is odd and the count of summands is odd, and (3) therefore C is odd by Proposition 9.23. The only citation difference is that the AI explicitly cites D7.7 (definition of odd number) to justify calling A and B odd, whereas Heath simply states that A and B are odd without citing the definition. Since D7.7 is a foundational definition and not a substantive proposition, and the logical backbone is identical, this is a citation-depth difference under Case A of Q2, yielding G. The citation sets are not identical (ai_used includes D7.7 which heath_refs does not), so P is ruled out.

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: given odd A measures even B via C, they prove C must be even by contradiction (if C were odd, the product of two odd numbers would be odd, contradicting B being even), then conclude A measures B/2. The only substantive citation difference is that the AI uses 9.29 (product of two odds is odd) while Heath uses 9.23 (sum of an odd count of odds is odd). The proof-tree containment test confirms this is a depth difference: Heath's own proof of 9.29 cites 9.23 as its key step, so the AI is citing 9.29 as a packaged unit while Heath effectively re-derives the reasoning of 9.29 inline using 9.23. The remaining ai_only items (D7.3, D7.6, D7.7, D7.15) are all Book 7 definitions representing over-citation by the AI. This is a citation-depth difference with identical logical backbones, yielding G.

### 9.31
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as Case B (different backbone), leading to Q3. Heath proves 9.31 by contradiction: assuming some D measures both A and C=2B, D must be odd (since it divides odd A), and then by 9.30 an odd divisor of an even number also divides its half, so D divides B, contradicting A and B being coprime. The AI instead gives a direct proof: since A is odd, 2 does not divide A, so by 7.29 (a prime not dividing a number is coprime to it) 2 is coprime to A; since B is coprime to A by hypothesis, 7.24 (the product of two numbers each coprime to a third is coprime to that third) gives that 2B is coprime to A. These are fundamentally different proof strategies with completely disjoint citation sets (Jaccard 0.0), yet the AI's direct proof is logically sound at every step, so Q3(b) holds and the classification is D.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) each number in the doubled-from-dyad sequence is even-times even, (2) by 9.13, the only divisors of any number in the sequence are the preceding terms and the unit, (3) since all those terms are even, no odd number greater than 1 divides any term, so no term is even-times odd, hence each is even-times even only. The AI proof explicitly cites three definitions (D7.6 for even, D7.9 for even-times odd, D7.11 for prime) that Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are definitions providing extra citation depth for the same underlying reasoning, this is a clear Case A: same backbone, different citation depth.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decides this as G (granularity difference). Both proofs share the same logical backbone: (1) the half of the number is odd, so the number is even-times odd by D7.9; (2) if the number were also even-times even (D7.8), then the half would be measured by an even number, contradicting the half being odd; (3) therefore the number is even-times odd only. The AI proof adds an additional argument (Steps 8-10) ruling out odd-times-odd using 9.29, which Heath does not include, but this supplements rather than replaces the shared backbone. The ai_only set consists of definitions (D7.6, D7.7, D7.10) that Heath uses implicitly without citation, plus 9.29 for the supplementary odd-times-odd argument. The heath_only set is empty, confirming the AI covers all of Heath's reasoning. Since the core backbone is identical and the differences are extra explicit definition citations and an additional thoroughness argument, this is a same-backbone, different-depth situation classifying as G.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: (1) A is even-times even because its half is not odd (citing D7.8), and (2) A is even-times odd because repeated bisection must reach an odd number (proved by contradiction — if not, we reach a dyad and A would be in the doubling sequence from 2, contradicting the hypothesis). The AI proof explicitly cites definitions D7.6 (even), D7.7 (odd), and D7.9 (even-times odd) that Heath uses implicitly, and cites 9.32 to justify the contradiction step where Heath simply states 'A will be among those which are doubled from a dyad' without an explicit citation. All ai_only items (9.32, D7.6, D7.7, D7.9) represent over-citation at a finer granularity, not a different proof path, and heath_only is empty, confirming Case A of Q2.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: they apply separando (7.11) to the continued proportion to obtain differences of consecutive terms, use alternando (7.13) to rearrange and establish that all ratio pairs (A(k+1)-Ak):Ak are equal, then apply ratio summation (7.12) to combine all the equal ratios, and finally simplify the resulting telescoping sum to reach the conclusion. The AI proof explicitly cites CN2 and CN3 to justify the telescoping sum simplification, while Heath performs the same simplification by substituting named segments without citing these Common Notions. Since the key intermediate conclusions are identical and the only difference is that the AI over-cites Common Notions for added rigor, this is a granularity difference (G).

### 9.36
**Category**: Granularity difference
**Jaccard**: 0.312
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same backbone of key intermediate conclusions: (1) setting up a geometric series in double proportion from unity with prime sum S, (2) using 9.35 to relate the sum to a power of 2, (3) using 9.13 to identify that the divisors of D are exactly the terms of the geometric progression, (4) proving that all divisors of E = S*D are either divisors of D or S times a divisor of D, (5) summing proper divisors to show the total equals E, and (6) concluding perfection by D7.22. The citation differences reflect alternative paths to the same conclusions: Heath uses 7.14 (ex aequali) and 7.19 (proportional products) where the AI uses 7.17 and 7.18 (direct ratio preservation under multiplication), and Heath uses 7.19+7.21+7.20 for the divisor uniqueness argument where the AI uses 7.30 (prime divides product implies divides a factor) more directly. The ai_only definitions (D7.1, D7.3, D7.11, D7.15) are minor overcitations. The Jaccard of 0.312 reflects these citation-level differences rather than structural divergence.
