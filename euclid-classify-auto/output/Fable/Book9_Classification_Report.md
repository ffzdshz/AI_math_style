# Book 9 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 8 | 9.9, 9.22, 9.23, 9.25, 9.26, 9.27, 9.28, 9.29 |
| Granularity difference (G) | 26 | 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.10, 9.12, 9.13, 9.14, 9.15, 9.16, 9.17, 9.18, 9.20, 9.21, 9.24, 9.30, 9.31, 9.32, 9.33, 9.34, 9.35, 9.36 |
| Path difference (D) | 2 | 9.11, 9.19 |
| AI proof error (E) | 0 |  |

**Total**: 36 propositions

## Per-Proposition Analysis

### 9.1
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) D = A*A is square, (2) A:B = D:C by VII.17, (3) one mean proportional between A and B by VIII.18, (4) one mean proportional between D and C by VIII.8, (5) D square implies C square by VIII.22. The only difference is that the AI explicitly cites Definition 7.18 to justify that a number multiplied by itself is square, whereas Heath states this without citation. This is a classic over-citation of a definition, placing the proofs in Case A of Q2: same backbone, different citation depth, yielding category G.

### 9.2
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification. Both proofs follow the identical backbone: construct D = A*A, establish A:B = D:C via VII.17, observe that D and C are both square and therefore similar plane numbers, find a mean proportional between D and C via VIII.18, transfer the mean proportional to A and B via VIII.8, and conclude that A and B are similar plane numbers via VIII.20. The only difference is that the AI explicitly cites definitions D7.16 (plane number), D7.18 (square number), and D7.21 (similar plane numbers) to justify steps that Heath leaves implicit. Since heath_only is empty and ai_only contains only definitional citations, this is a straightforward citation-depth difference with the same logical backbone, yielding G.

### 9.3
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: decomposing cube A via its side C to establish the continued proportion unit:C = C:D = D:A, then deriving unit:A = A:B from A multiplying itself, applying VIII.8 to obtain two mean proportionals between A and B, and concluding via VIII.23 that B is cube. The only difference is that the AI explicitly cites definitions D7.15 (multiplication as repeated addition) and D7.19 (cube number definition) at each step, whereas Heath invokes these concepts implicitly without formal citation. Since heath_only is empty and ai_only contains only definitions, this is a clear case of over-citation at the definitional level with no change in the proof's logical structure, yielding a granularity difference.

### 9.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification via the proof-tree containment test. Both proofs share the same backbone: construct D = A*A so D is cube (9.3), establish A:B = D:C (7.17), then conclude C is cube from D being cube and the ratio being cube-to-cube. The sole difference is citation depth at the final step: Heath re-derives the internals of 8.25 inline by showing A,B are similar solid numbers with two mean proportionals between them (8.19), transferring those mean proportionals to D,C (8.8), and concluding via 8.23; the AI instead cites 8.25 directly, which is exactly the proposition whose proof uses 8.19, 8.8, and 8.23. Since all three heath_only items appear inside Heath's proof of 8.25, this is a citation-depth difference under Case A of Q2, yielding G.

### 9.5
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: A multiplied by itself gives cube D (9.3), the ratio A:B equals D:C (7.17), D and C are similar solid numbers so two mean proportionals fall between them (8.19), two mean proportionals therefore fall between A and B (8.8), and since A is cube B must be cube (8.23). The AI proof adds explicit citations to Definitions 7.19 and 7.21 to justify why cube numbers are similar solid numbers, a step Heath states without citing the definitions. Since ai_only contains only definitions and heath_only is empty, and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference under Case A of Q2, yielding G.

### 9.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: The forward dependency gate passes (9.5 precedes 9.6; D7.19 is a definition). Q1 finds no logical defect: the AI correctly establishes C = A^3 is cube by D7.19, then correctly applies 9.5 (if a cube multiplied by a number yields a cube, that number is cube) to conclude A is cube. Q2 applies the proof-tree containment test to the three substantive heath_only propositions (8.19, 8.8, 8.23): all three appear inside Heath's own proof of 9.5, which the AI cites as a single higher-level unit. Heath re-derives the internals of 9.5 inline in his proof of 9.6 (establishing proportions via VII.Def.20, finding mean proportionals via VIII.19/VIII.8, concluding via VIII.23), while the AI packages that entire argument by citing 9.5 directly. The remaining differences (D7.19 vs D7.20) are definitional. Since the containment test passes for all substantive heath_only items, this is Case A -- same logical backbone at different citation depth -- yielding G.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: The forward dependency gate found no issues since all AI citations (D7.13, D7.15, D7.17) are definitions, which are never forward. Q1 confirmed the AI proof is logically complete with no errors: every step is supported by a citation or follows from prior steps. Q2 revealed that both proofs share identical key intermediate conclusions -- decomposing the composite number A into factors D and E via D7.13 and D7.15, then showing that D x E x B = C makes C a solid number. The sole difference is that the AI explicitly cites Definition 7.17 (the definition of a solid number) to justify the final conclusion, while Heath applies the same concept without a formal citation. Since D7.17 is a definition rather than a substantive proposition, this is over-citation at the definitional level, placing this squarely in Case A of Q2: same backbone, different citation depth. The classification is therefore G.

### 9.8
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that A multiplied by itself produces the square B (via VII Def 20), extend squareness along the geometric progression using VIII.22, show that A multiplied by B produces the cube C, and extend cubeness using VIII.23, then combine both results for the seventh term. The AI proof explicitly cites three definitions (D7.15 for multiplication, D7.18 for square, D7.19 for cube) that Heath invokes implicitly without formal citation. Since heath_only is empty and the ai_only items are all definitions providing finer citation granularity for the same reasoning steps, this is Case A of Q2: same backbone, different citation depth.

### 9.9
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Scope correction applied: Proposition 9.9's statement asks only about the square case. Heath's proof includes the cube case as a bonus extension after completing the square case, but the cube case is not part of the proposition statement. Citations 8.23 and 9.3 are excluded as cube-case-only. After this correction, the effective Heath citations for the square case are {8.22, 9.8}, matching the AI citations exactly. Forward-dependency gate: 8.22 (book 8 < 9) and 9.8 (n=8 < 9) are both backward; no forward dependencies. Q1(a): Single-case proposition (square case only). The AI addresses the square case fully; no missing case. Q1(b): The AI proof is logically complete — Step 2 uses 9.8 to establish odd-position numbers are square, Steps 3–4 use 8.22 to cascade the square property through even-position numbers via consecutive triples, and Step 5 generalizes the induction. No E triggers. Q2: Both proofs share the same backbone: (1) odd-position numbers are square by 9.8, (2) even-position numbers are shown square by applying 8.22 to consecutive triples. Case A holds. Perfect match check: AI citations {8.22, 9.8} equal the scope-corrected Heath citations {8.22, 9.8}. Classification: P.

### 9.10
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Scope correction applied: the proposition statement concerns only the square case. Heath's proof includes a cube case extension (using 8.25 and 9.6) that goes beyond the proposition statement; these citations are excluded from comparison. Effective Heath citations for the square case: 8.26, 9.8. Forward dependency gate passes (8.24 in Book 8, 9.8 precedes 9.10, D7.20 is a definition). Q1(a): only the square case is required; the AI addresses it completely. Q1(b): every step is supported by citation or prior steps — 9.8 licenses B being square, D7.20 licenses the proportion inversion, 8.24 licenses the conclusion that A is square from ratio of square to square and B being square. NOT-E. Q2: both proofs share the same backbone for the square case — (1) B is square [9.8], (2) assume C square, (3) establish that A and B have ratio of square to square, (4) conclude A is square (contradiction), (5) C not square, (6) extend to subsequent terms. The citation difference is at step (4): the AI uses D7.20 to invert the proportion and 8.24 directly (ratio of sq:sq + first is square implies second is square), while Heath uses 8.26 converse (ratio of sq:sq implies similar plane numbers, then similar to a square is square). D7.20 is an explicit definition citation left implicit by Heath. Same backbone, different citation depth — G.

### 9.11
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath proves only that B (the first term after the unit) measures the last term E, using a single application of 7.15 (alternation). The AI proves the fully general case that any earlier term M measures any later term N, by first establishing (like Heath) that B measures each later term Q according to its predecessor P via 7.15, and then extending to arbitrary pairs M, N through an ex aequali argument using 7.14. The ex aequali step is an indispensable key intermediate conclusion in the AI proof that is entirely absent from Heath's proof, making this Case B (different backbone). The AI's generalized path is logically sound (Q3 confirmed), yielding D.

### 9.12
**Category**: Granularity difference
**Jaccard**: 0.714
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: a proof by contradiction assuming prime E does not measure A (the term next to the unit), followed by a descent chain showing E|D implies E|C implies E|B implies E|A, yielding a contradiction. The two heath_only citations (9.8 and D7.14) reflect citation-depth differences, not backbone divergence. Heath cites 9.8 explicitly for the fact that A squared equals B, while the AI derives the same fact from 9.11 and its Porism (since A measures B according to the term in the same position from B as A is from the unit, which is A itself). Heath cites D7.14 (definition of composite numbers) in the final argument step, while the AI proceeds directly from the contradiction to the conclusion, omitting the definitional intermediary. The ai_only set is empty, confirming the AI uses a subset of Heath's citations. Since the key intermediate conclusions are identical and the citation differences are purely matters of depth, this is Case A in Q2, yielding G.

### 9.13
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow the same descent argument: assuming a number E not among the proportional numbers measures the greatest term D, they show E is composite and measured by A (via 9.12 and 7.31), introduce F with E*F=D and F not among the proportional numbers (via 9.11), then use proportionality (7.19) to descend through F measuring C, G measuring B, and finally H measuring A, contradicting A being prime. The key intermediate conclusions are identical. The sole heath_only citation, 9.8 (A multiplied by itself makes B), is re-derived inline by the AI from definitions D7.20 and D7.15, which appear inside Heath's own proof of 9.8 — satisfying the proof-tree containment test. All ai_only items are definitions (D7.2, D7.3, D7.11, D7.13, D7.15, D7.20) and the commutativity result 7.16, representing over-citation of foundational material. This is a same-backbone, different-citation-depth case.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume a prime E different from B, C, D measures A, derive E times F = A, apply VII.30 to conclude B, C, D each measure E or F, rule out E because it is prime and distinct, so they measure F, and reach a contradiction since F is less than A. The AI proof cites exactly the same key proposition (7.30) as Heath and adds explicit references to definitions (D7.11 for prime, D7.15 for multiplication, D7.3 for part), a common notion (CN5), and the commutativity of multiplication (7.16), all of which Heath uses implicitly. Since heath_only is empty and all ai_only items are over-citations of definitions and basic results, this is Case A in Q2: same backbone, different citation depth, yielding G.

### 9.15
**Category**: Granularity difference
**Jaccard**: 0.875
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: they take DE, EF as the least numbers with the given ratio via VIII.2, establish A=DE^2, B=DE*EF, C=EF^2, prove DE and EF coprime (VII.22), prove DF coprime to each (VII.28), then demonstrate all three coprimality results (A+B prime to C, B+C prime to A, A+C prime to B) using the same chain of VII.24, VII.25, II.3, and II.4. The AI proof additionally cites VII.33 for finding the least numbers with a given ratio, a construction step that Heath subsumes under VIII.2 alone. Since heath_only is empty and ai_only contains only this construction-level over-citation, the backbones are identical and the difference is purely one of citation depth, placing this squarely in Case A of Q2 as a granularity difference.

### 9.16
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs follow the same backbone: assume for contradiction that A:B = B:C, invoke 7.21 to establish that A and B are the least numbers in their ratio, then apply 7.20 to conclude that A measures B, and since A measures itself, A measures both A and B, contradicting their being prime to one another. The AI proof adds explicit citations to D7.2 (definition of number, to show A is not a unit) and D7.12 (definition of prime to one another) to spell out the final contradiction step that Heath leaves implicit. Since heath_only is empty and ai_only contains only definitions, this is a clear case of over-citation at the same logical backbone, yielding a granularity difference.

### 9.17
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction through identical key intermediate conclusions: assuming D:E = A:B, applying alternation (7.13) to get A:D = B:E, invoking the primality-implies-least result (7.21), using the least-numbers measuring property (7.20) to show A measures B, then propagating divisibility through the continued proportion to show A measures D, contradicting the premise that A and D are prime to one another. The AI proof cites four additional definitions (D7.3, D7.20, D7.12, D7.2) that Heath leaves implicit, but these are purely citation-depth differences: the underlying logical steps and key conclusions are identical in both proofs. Case A of Q2 holds, yielding G.

### 9.18
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 (Case A) decided the classification. Both proofs establish identical key intermediate conclusions through the same logical backbone: both divide into three cases (A,B prime to one another; A,B not prime and A measures B-squared; A,B not prime and A does not measure B-squared), invoke 9.16 for the prime case, and use 7.19 for the proportionality argument in the remaining cases, with a proof by contradiction for the non-measuring sub-case. The AI proof explicitly cites CN1 (for equality transitivity, e.g., A*D = B*B) and D7.15 (for the definition of multiplication), both of which Heath uses implicitly without citation. Since ai_only contains only a common notion and a definition while heath_only is empty, and the logical backbones are identical, this is a citation-depth difference yielding category G.

### 9.19
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Heath's proof treats four separate cases, with Case 2 (not in continued proportion, extremes prime to one another) proved impossible through a dedicated chain using 7.14 (ex aequali), 7.21 (primes are least), and 7.20 (least numbers measure those with same ratio). The AI proof bypasses this entire argument by providing a unified criterion for all cases except the 9.17 case: form D = B*C and check whether A measures D. The AI's two-branch structure (9.17 case vs. unified A|B*C criterion) constitutes a genuinely different logical backbone from Heath's four-case treatment. The proof-tree containment test confirms these heath_only propositions are not subsumed by any higher-level proposition the AI cites; the AI simply takes a different route. Q3 confirms the AI's path is valid: the A|B*C criterion is correctly proved in both directions using 7.19, with no logical gaps.

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct DE as the least common multiple of the assigned primes, add a unit to obtain EF, then consider two cases. In Case 1 (EF prime), both proofs conclude that EF is a new prime different from the assigned ones. In Case 2 (EF not prime), both proofs show EF is measured by some prime G and then prove by contradiction that G cannot equal any of the assigned primes, since G would then measure the unit. The only differences are in citation depth: the AI cites 7.32 (any number is either prime or measured by some prime) where Heath cites 7.31 (any composite number is measured by some prime), and the proof-tree containment test confirms that 7.31 appears inside Heath's proof of 7.32, so the AI simply cites the higher-level result. The remaining ai_only items (7.36 for finding the LCM, CN5, D7.2, D7.3) are foundational or construction citations that Heath invokes implicitly without explicit reference. This is Case A of Q2: same backbone, different citation depth.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: the sum AE is divisible into two equal parts (has a half part), and therefore AE is even. Heath's proof states this concisely by noting each summand has a half part so the whole does too. The AI proof spells out the same argument in greater detail, explicitly constructing the grouped halves F and G', invoking CN2 (equals added to equals yield equals) to show F = G', and then concluding AE = F + G'. The only citation difference is that the AI explicitly cites CN2 where Heath leaves the inference implicit. Since CN2 is a Common Notion (axiom-level), this is over-citation at the axiom level, a classic granularity difference. The logical backbones are identical, so this is Case A of Q2.

### 9.22
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21 is prior and D7.7 is a definition). Q1 confirmed the AI proof is logically complete: each step is supported by a citation or the hypothesis. Q2 confirmed both proofs share the same key intermediate conclusions -- subtract a unit from each odd number to get even remainders (D7.7), sum the even remainders (9.21), note the units form an even number, and conclude AE is even (9.21). The citation sets are identical (ai_used = heath_refs = {9.21, D7.7}, Jaccard = 1.0), so the perfect match check assigns category P.

### 9.23
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21, 9.22, and D7.7 are all prior to 9.23). Q1 confirmed the AI proof is logically complete: each step is properly justified with appropriate citations. Q2 confirmed both proofs share the same key intermediate conclusions -- subtracting a unit from the last odd number to obtain an even remainder, establishing that the sum of the remaining odd numbers is even via 9.22, combining the two even parts via 9.21, and concluding the whole is odd by D7.7. The citation sets are identical (ai_used = heath_refs = {9.21, 9.22, D7.7}), yielding Jaccard 1.0 and classification P.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same chain of key intermediate conclusions: AB has a half part (by D7.6), BC has a half part (by D7.6), the remainder AC also has a half part, and therefore AC is even. The AI proof takes a more formally detailed route by invoking Definition 7.3 to define what a 'part' is and Proposition 7.7 to formally justify that if D is the half of AB and E is the half of BC, then D minus E is the half of AC. Heath treats this final step as immediately obvious from the definition of even numbers. Since the key conclusions are identical and the extra AI citations (7.7, D7.3) provide additional depth of justification rather than a different logical route, this is a granularity difference.

### 9.25
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow the same logical backbone with identical citations. Both subtract a unit from the odd number BC to obtain the even number DB (by D7.7), then subtract the even DB from the even AB to conclude AD is even (by 9.24), and finally observe that the remainder CA differs from the even AD by exactly one unit, making CA odd (by D7.7). The citation sets are identical (9.24, D7.7), yielding a Jaccard similarity of 1.0. Since Q1 found no logical defect, Q2 confirmed the same key intermediate conclusions, and the citation sets match exactly, the perfect-match check assigns category P.

### 9.26
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.24 is prior and D7.7 is a definition). Both proofs follow an identical logical chain: subtract a unit BD from the odd number AB to get even remainder AD (by Definition VII.7), observe that CD is also even by the same reasoning, then conclude that CA is even because an even number subtracted from an even number leaves an even remainder (by IX.24). The citation sets are identical (9.24 and D7.7), yielding Jaccard 1.0. Since the key intermediate conclusions and citations match exactly, this is a perfect match.

### 9.27
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 9.27 follow the same logical backbone: subtract the unit AD from odd number AB to obtain even DB (by Def. 7.7), then since both DB and BC are even, their difference CD is even (by 9.24), and finally CA equals CD plus the unit DA, making CA odd (by Def. 7.7). The citation sets are identical ({9.24, D7.7} = {9.24, D7.7}, Jaccard = 1.0), and the key intermediate conclusions match exactly, so the perfect-match check at the end of the protocol assigns category P.

### 9.28
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21 is prior and D7.15 is a definition). Both proofs follow the identical logical chain: by the definition of multiplication (D7.15), C is made up of as many copies of B as there are units in A; since B is even, C is a sum of even numbers; by 9.21, the sum of even numbers is even, so C is even. The citation sets are exactly equal (ai_used = heath_refs = {9.21, D7.15}), with Jaccard similarity 1.0 and empty ai_only and heath_only sets. Since no category was assigned by Q1-Q3 and the citation sets match exactly, the classification is P (Perfect match).

### 9.29
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward-dependency gate found no issues (9.23 is prior and D7.15 is a definition). Both proofs follow the same logical backbone: applying VII. Def. 15 to express the product C as a sum of A copies of B, noting each summand is odd and their count is odd, then invoking IX. 23 to conclude C is odd. The AI proof is logically complete with no defects under Q1. Since the citation sets are exactly equal ({9.23, D7.15} = {9.23, D7.15}) and the key intermediate conclusions match, the classification is P (Perfect match).

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they set up A times C equals B, prove by contradiction that C cannot be odd (which would make B odd, contradicting the hypothesis that B is even), conclude C is even, and derive that A measures the half of B. The sole substantive divergence is the citation used in the contradiction step: Heath cites 9.23 directly (a sum of odd numbers taken an odd number of times is odd), while the AI cites 9.29 (the product of two odd numbers is odd). The proof-tree containment test confirms that 9.23 appears inside Heath's own proof of 9.29, so the AI is citing 9.29 as a unit while Heath re-derives its internals inline. The remaining ai_only items (D7.15, D7.6, D7.7) are definitions reflecting over-citation at a finer granularity. This is Case A of Q2: same backbone, different citation depth.

### 9.31
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as G. Both proofs follow the same backbone: assume by contradiction that A (odd, prime to B) is not prime to C = 2B, derive that some D measures both A and C, show D must be odd, apply 9.30 to conclude D measures half of C which is B, and reach a contradiction since D then measures both A and B which are coprime. The AI proof adds explicit definitional citations (D7.5, D7.6, D7.7, D7.12) and proposition 9.21 to justify steps that Heath states without citation, such as the step that D is odd because it divides the odd number A. Since heath_only is empty, the AI covers every step Heath uses. The difference is purely citation depth — the AI over-cites definitions and a supporting lemma — placing this firmly in Case A of Q2.

### 9.32
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: establish that the doubled numbers are all even, set out a unit to form a continued proportion with A (the dyad) as the prime after the unit, apply 9.13 to show D is measured only by A, B, and C, and conclude that since all divisors are even, D is even-times even only. The AI proof cites nine additional items beyond Heath's two references (9.13, D7.8), but these are almost entirely definitions (D7.2, D7.3, D7.6, D7.7, D7.9, D7.11, D7.15, D7.20) that Heath invokes implicitly, plus one theorem (7.16) used in an explicit contradiction argument showing D is not even-times odd, which Heath derives more directly from D7.8. Since heath_only is empty and the ai_only items are all foundational definitions or a theorem used to spell out what Heath states concisely, this is Case A: same backbone, different citation depth.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) show A is even-times odd because its odd half measures it an even number of times, and (2) show A is not even-times even by contradiction, since assuming so forces the half to be even, contradicting its oddness. The AI proof is substantially more detailed, explicitly citing definitions (D7.6, D7.7, D7.15), a common notion (CN5), commutativity of multiplication (7.16), and a result on sums of even numbers (9.21) at steps that Heath leaves implicit. Heath cites only D7.8 and D7.9, and all of these appear in the AI's citation set as well (heath_only is empty). The six ai_only items are all foundational results and definitions used to flesh out sub-steps of the same argument, representing over-citation and greater explicitness rather than a different proof path. Case A of Q2 holds, yielding G.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Both proofs share the same two-part backbone: (1) A is even-times even because its half is not odd, justified by D7.8; (2) A is even-times odd because repeated bisection must terminate at an odd number (not a dyad, by contradiction with the hypothesis), and that odd number measures A according to an even number. The AI proof follows this identical logical path but makes explicit every definitional and auxiliary step that Heath leaves implicit, citing definitions D7.2, D7.3, D7.6, D7.7, D7.9, D7.15, common notion CN5, and propositions 7.16 (commutativity) and 9.29 (odd times odd is odd) to justify details Heath treats as obvious. Since heath_only is empty and all ai_only items are over-citations providing deeper justification for the same backbone conclusions, this is Case A of Q2: same key intermediate conclusions at different citation depth.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing FK=BC and FL=D within EF, establishing KH=GC by remainder equality, applying separando (7.11) and alternando (7.13) to obtain the chain of equal ratios EL:FL = LK:FK = KH:FH, then combining antecedents and consequents via 7.12 to reach the final proportion GC:A = EH:(D+BC+A). The AI proof adds explicit citations to common notions (CN1, CN3) and definitions (D7.3, D7.4, D7.20) that Heath uses implicitly without citation. Since heath_only is empty and all ai_only items are foundational axioms rather than substantive propositions, this is a clear Case A in Q2: same key intermediate conclusions with different citation depth.

### 9.36
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: establishing E, HK, L, M, FG in continuous double proportion, applying 9.35 to show OG equals the sum E+HK+L+M, demonstrating FG equals the sum of all its parts, showing each part measures FG, and proving by contradiction that no other number measures FG. The only difference is the sub-argument mechanism for the uniqueness step: the AI uses 7.30 (a prime dividing a product divides one factor) to split into two cases, while Heath re-derives the internals of 7.30 inline using 7.29 (prime not measuring a number is coprime to it), 7.21 (coprime numbers are least in ratio), and 7.20 (least numbers measure proportionals the same number of times). The proof-tree containment test confirms that all three heath_only propositions (7.29, 7.21, 7.20) appear inside Heath's own proof of 7.30, so the AI is citing 7.30 as a packaged unit while Heath unpacks it. The remaining ai_only items are definitions (D7.2, D7.3, D7.11, D7.15), common notions (CN1, CN2, CN5), and basic results (7.13, 7.16, 7.17) that represent explicit over-citation of steps Heath leaves implicit. This is a citation-depth difference, not a path difference.
