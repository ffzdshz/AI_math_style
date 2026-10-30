# Book 9 — Classification Report (GPT)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 9.28, 9.29 |
| Granularity difference (G) | 16 | 9.4, 9.6, 9.7, 9.14, 9.16, 9.17, 9.20, 9.21, 9.22, 9.23, 9.24, 9.30, 9.31, 9.33, 9.34, 9.35 |
| Path difference (D) | 18 | 9.1, 9.2, 9.3, 9.5, 9.8, 9.9, 9.10, 9.11, 9.12, 9.13, 9.15, 9.18, 9.19, 9.25, 9.26, 9.27, 9.32, 9.36 |
| AI proof error (E) | 0 |  |

**Total**: 36 propositions

## Per-Proposition Analysis

### 9.1
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath proves that the product C is square by introducing an auxiliary square D = A*A, establishing the ratio A:B = D:C via VII.17, transferring the mean proportional count from A,B to D,C via VIII.8, and concluding via VIII.22 (if the first of three continued proportionals is square, the third is too). The AI takes a fundamentally different path: it obtains the mean proportional M between A and B via 8.18, then directly applies 7.19 (product of extremes equals product of means in a proportion) to conclude A*B = M*M, yielding squareness immediately. The AI never introduces the auxiliary square D, never uses ratio transfer (VII.17), never invokes VIII.8 or VIII.22. These are different key intermediate conclusions (Case B in Q2). Under Q3, the AI's chain is logically complete: every step from premises to conclusion is supported by a valid citation, so the different path is valid, yielding D.

### 9.2
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Heath's proof constructs an auxiliary square D = A squared, establishes the ratio A:B = D:C via VII.17, observes that D and C are both square (hence similar plane numbers), uses VIII.18 to find a mean proportional between D and C, then transfers that mean proportional to A and B via VIII.8, and finally applies VIII.20. The AI takes a fundamentally different and more direct route: from the definition of square number (D7.18) it writes A times B = C times C, then applies the converse of VII.19 (if the product of the first and fourth equals the product of the second and third, the four numbers are proportional) to the four numbers A, C, C, B to obtain A:C = C:B directly, making C the mean proportional between A and B without any auxiliary construction, and concludes via VIII.20. The key intermediate conclusions differ entirely: Heath routes through D, the ratio D:C, and a chain of three propositions (VII.17, VIII.18, VIII.8), while the AI bypasses all of this with a single application of VII.19. The AI's path is logically valid and complete, yielding a genuine path difference.

### 9.3
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof works through the theory of mean proportionals: it establishes two mean proportionals between the unit and A (via VII.Def.20), extends this to two mean proportionals between A and B using VIII.8, and then applies VIII.23 to conclude B is cube. The AI proof takes a fundamentally different, more elementary approach: it directly decomposes the cube A as a*b (where b = a*a), builds proportions a:b = b:A and a:b = A:c (where c = b*b) using Book 7 multiplication and ratio propositions (7.16, 7.17), derives b*c = A*A = N via 7.19, and concludes N = b*b*b is cube by definition. The two proofs share zero citations (Jaccard = 0.0) and argue through entirely different key intermediate conclusions, making this a clear path difference. The AI proof is logically complete: each step follows validly from its predecessors using the cited propositions.

### 9.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: define D = A*A as cube by 9.3, establish D:C = A:B by 7.17, then conclude C is cube because D is cube and the ratio D:C is a cube-to-cube ratio. The difference lies entirely in citation depth for the final step. Heath re-derives the internals of this reasoning inline using three propositions (8.19 to get mean proportionals between similar solids A and B, 8.8 to transfer those mean proportionals to D and C, and 8.23 to conclude from four numbers in continued proportion with the first being cube). The AI instead cites 8.25 as a single unit, which packages exactly that chain — Heath's own proof of 8.25 uses precisely 8.19, 8.8, and 8.23. The proof-tree containment test confirms all heath_only items appear inside Heath's proof of the AI's cited proposition 8.25, establishing this as a citation-depth difference rather than a path difference.

### 9.5
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2 (Case B) leading to Q3. The two proofs have completely different logical backbones with zero citation overlap (Jaccard = 0.0). Heath's proof works through proportionality theory: forming D = A squared (a cube by 9.3), establishing the ratio A:B = D:C via 7.17, then using the theory of similar solids (8.19) and mean proportionals (8.8, 8.23) to conclude B is cube. The AI's proof instead uses a direct construction approach: exploiting 8.15 to establish that the cube root of A measures the cube root of C, constructing D = d cubed from the measurement quotient, showing AD = C via commutativity (7.16), and cancelling to get B = D (hence B is cube). Both paths are logically complete under the hardened Q1(b) standard, yielding category D.

### 9.6
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification via the proof-tree containment test. The AI proof establishes that C = A^3 is cube by definition, then applies 9.5 ('If a cube number by multiplying any number make a cube number, the multiplied number will also be cube') to conclude A is cube. Heath's proof reaches the same conclusion but re-derives the internals of 9.5 inline, setting up the proportion A:B = B:C via VII.Def.20, then using VIII.19 (similar solid numbers have two mean proportionals), VIII.8 (transferring mean proportionals across equal ratios), and VIII.23 (concluding a number with two mean proportionals to a cube is itself cube). All three substantive heath_only items (8.19, 8.8, 8.23) appear inside Heath's own proof of 9.5, confirming the AI cites 9.5 as a unit while Heath expands its internals. This is a citation-depth difference, not a backbone difference.

### 9.7
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 Case A decided the classification. Both proofs share the same logical backbone: decompose composite number A into factors D and E (via D7.13 and D7.15), establish that E times D equals A, then conclude that C equals D times E times B and is therefore solid. The AI proof differs only in explicitly citing D7.2 (definition of number) to justify that E is a number and D7.17 (definition of solid number) to justify the final conclusion, both of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions, this is purely a citation-depth difference with identical key intermediate conclusions.

### 9.8
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification. Heath proves the first term is square directly (A*A = B via Def. 20), then propagates squareness and cubeness along continued proportions using 8.22 and 8.23 respectively. The AI instead derives a general index-addition law u_{r+s} = u_s * u_r using 7.18 (ratio preservation under multiplication by a common number), then specializes: u_{2r} = u_r^2 is square, u_{3r} = u_r^3 is cube, and u_{6r} is both. The containment test confirms these are genuinely different paths: 8.22 relies on 8.20 (similar plane numbers) and 8.23 relies on 8.21 (similar solid numbers), neither of which appears in the proof tree of 7.18. The AI's chain is logically complete under the 1(b) standard, running from the continued proportion hypothesis through the index-addition law to all three assertions, so Q3 confirms a valid different path.

### 9.9
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Scope correction applied: Prop 9.9 statement asks only about the square case. Heath's cube-case extension and its citations (8.23, 9.3) excluded from comparison. The AI proves only the square case, which is the full scope of the proposition. Forward-dependency gate: 9.1 (b=9, n=1 < 9) not forward; D7.x definitions never forward. Gate passes. Q1(a): No multi-case structure in the square-case statement; AI addresses it fully. Q1(b): Each step is sound. Step 2 derives A_{i+1} = A_1 * A_i from the proportion relation. Step 3 correctly identifies two squares as similar plane numbers (equal-sided rectangles with proportional sides). Step 4 correctly applies 9.1 (product of similar plane numbers is square). Step 5 completes the induction. NOT-E. Q2: Different backbones. Heath uses IX.8 (alternate terms are square) then VIII.22 (in three continued-proportion numbers, first square implies third square) applied to consecutive triples (A,B,C), (B,C,D), etc. AI uses an inductive scheme through 9.1 (product of similar plane numbers is square), showing each A_i and A_1 are similar plane numbers. VIII.22 and 9.1 are independent propositions; no containment (9.1 is in Book IX, cannot appear inside VIII.22's proof). Case B. Q3: Gate passed (positional validity). AI chain from premises to conclusion is complete and logically sound. Path difference (D).

### 9.10
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: SCOPE CORRECTION: Proposition 9.10's statement concerns only the square case. Heath's proof includes the cube case as a bonus extension after completing the square case proof. The AI proves only the square case, which is the full scope of the proposition statement. Citations 8.25 and 9.6 are excluded from Heath's effective set as cube-case-only. Effective Heath citations for the square case: 8.26, 9.8. Forward-dependency gate: all AI citations (7.14, 8.22, 9.8, D7.20) are prior to 9.10 — pass. Q1: The AI proof is logically complete. It correctly uses 9.8 to establish that even-indexed terms are square, then shows by contradiction (via 7.14 and 8.22) that no odd-indexed term can be square. No E triggers. Q2: The backbones differ. Heath argues through the ratio of consecutive terms being square-to-square and uses 8.26 (converse) to identify similar plane numbers. The AI establishes a non-consecutive three-term proportion via 7.14 and propagates squareness directly via 8.22. Different key intermediate conclusions — Case B. Q3: The AI's chain from premises to conclusion is complete and sound. Path difference (D).

### 9.11
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves the proposition by extracting one ratio directly from the continued proportion (A:B = D:E) and then applying alternation (7.15) to convert the unit-measure relationship into the required divisibility result. The AI takes a fundamentally different route: it constructs two parallel chains of equal length with matching consecutive ratios and applies ex aequali (7.14) to obtain the proportion a0:a_d = ai:aj directly, then derives divisibility from the unit-measure property. The proof-tree containment test confirms these are independent paths: 7.15 does not appear inside Heath's proof of 7.14 (which uses 7.13 instead). Since the backbones differ and the AI's chain via ex aequali is logically sound and complete from premises to conclusion, the classification is D.

### 9.12
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof uses proof by contradiction with proportion theory: assuming the prime E does not measure A, he repeatedly applies VII.19 (proportion from product equality), VII.21 (primes are least), and VII.20 (least numbers measure proportionals) to descend from D through C and B, reaching a contradiction when E is shown to measure A. The AI instead takes a direct approach using VII.30 (Euclid's Lemma: if a prime divides a product, it divides one factor). The AI establishes that each term aⱼ equals a₁ times aⱼ₋₁ from the continued proportion, then applies VII.30 backward from aₙ to a₂ = a₁ squared, forcing the prime to divide a₁. These are fundamentally different proof strategies with different key intermediates: Heath works through ratios and coprimality, while the AI works through prime divisibility of products. The AI's path is logically complete and valid, so the classification is D.

### 9.13
**Category**: Path difference
**Jaccard**: 0.071
**Analysis**: Q2 decided this classification. Heath's proof descends through explicit quotients E, F, G, H using product identities (9.11, 9.8) and proportions (7.19) to eventually reach a contradiction with A being prime. The AI proof takes a structurally different approach: it selects a_k, the listed term with greatest index that divides d, shows that any prime dividing the quotient q = d/a_k must equal p (via 7.32 and 9.12), and concludes that a_{k+1} also divides d, contradicting the maximality of k. The only shared citation is 9.12; the remaining citations reflect entirely different proof mechanisms. The AI's index-based maximal element argument is logically complete and valid but follows a genuinely different logical backbone from Heath's explicit descent through proportions, yielding a path difference.

### 9.14
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs argue by contradiction: assume an extra prime q divides the least number N measured by given primes, write N = M*q, apply 7.30 to conclude each given prime divides M, and derive a contradiction from M < N. The key intermediate conclusions are identical. The AI's extra citations (D7.2, D7.5, D7.11, D7.15, CN5) are all definitions and a common notion that Heath leaves implicit, representing over-citation of foundational concepts rather than a different proof path. This is Case A of Q2: same backbone, different citation depth.

### 9.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath decomposes A, B, C into squares and products of a least ratio pair DE, EF (via VIII.2), establishes DE and EF are prime (VII.22), then uses composition-of-primality results (VII.24, VII.25, VII.28) together with algebraic identities (II.3, II.4) to derive the coprimality of each pair-sum with the remaining number. The AI takes a fundamentally different path: it applies VIII.3 directly to establish that the extremes A and C are prime, uses VII.19 to obtain the product identity AC = B^2, and then proves all three cases by contradiction, showing that any hypothetical prime common factor of a pair-sum and the remaining number would force a common factor of A and C, violating their coprimality (using VII.30 and VII.32). The Jaccard similarity is 0.0 with completely disjoint citation sets, and the key intermediate conclusions differ entirely: Heath works through the ratio-pair decomposition and algebraic identities, while the AI works through direct extremal primality and contradiction via prime divisors. The AI proof is logically complete and valid, establishing a genuine path difference.

### 9.16
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume A:B = B:C for contradiction, apply 7.21 (primes are least in their ratio), apply 7.20 (least numbers measure those with same ratio) to deduce A measures B, note A also measures itself so A is a common measure of A and B, and conclude this contradicts their being prime to one another. The AI proof explicitly cites definitions D7.1, D7.2, and D7.12 to spell out that A is a number (not a unit) and what it means for numbers to be prime to one another, whereas Heath leaves these definitional facts implicit. Since the backbones are identical and the only citation differences are these explicit definitions, Case A of Q2 holds, yielding G.

### 9.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: assume for contradiction that the last term is to some number as the first to the second, derive a proportion linking the coprime extremes to adjacent terms, invoke VII.21 (primes are least) and VII.20 (least measure proportionals) to conclude the first term divides the second, then chain divisibility through the continued proportion to show the first divides the last, contradicting coprimality. The sole substantive citation difference is that Heath uses alternation (7.13) directly on the assumed proportion while the AI uses ex aequali (7.14) on two shifted sequences to reach the same intermediate proportion. The proof-tree containment test confirms this is a depth difference: 7.13 appears inside Heath's proof of 7.14, so the AI cites 7.14 as a unit where Heath deploys 7.13 at a lower level. The remaining ai_only items (D7.2, D7.12, D7.15, D7.20) are definitions that Heath uses implicitly, representing over-citation rather than structural divergence.

### 9.18
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification. Heath's proof first distinguishes whether A and B are coprime, citing 9.16 to handle that case separately, then tests whether A measures B-squared for the non-coprime case. The AI proof bypasses the coprime distinction entirely, instead applying a unified measurement test (repeated subtraction of A from B-squared) that directly determines whether a third proportional exists. The proof-tree containment test confirms this as a genuine path difference: 9.16 does not appear inside the proof of 7.19, the AI's only substantive citation. The AI's unified approach is logically complete under the hardened standard: the measurement test correctly handles all sub-cases including the edge case where the quotient equals one (a unit, not a number per D7.1 and D7.2), and 7.19 correctly establishes the proportionality when the quotient is at least two. Q3 confirms the AI's different path is valid, yielding D.

### 9.19
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 decided the classification. Heath organizes the investigation into four cases based on whether the three numbers are in continued proportion and whether the extremes are coprime, using 9.17 for the continued-proportion-with-coprime case, ex aequali (7.14) with primes-are-least (7.21) and least-measure (7.20) for the non-continued-proportion-with-coprime case, and a divisibility test for the remaining cases. The AI instead gives a single unified criterion: form P = BC and test whether A divides P by repeated subtraction, justifying the equivalence entirely through 7.19 (proportion iff product equality) and 7.16 (commutativity of multiplication). Because the key intermediate conclusions differ fundamentally -- Heath reasons through coprimality and continued proportion while the AI reduces everything to a single divisibility test -- the backbones are different (Case B in Q2). Q3 confirms the AI path is logically valid: the chain from premises to conclusion is sound, yielding D.

### 9.20
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a common multiple of the assigned primes, add a unit to obtain a new number, then consider whether it is prime or not. If prime, a new prime is found directly; if not, any prime factor of the new number cannot equal any assigned prime (since it would then measure both the common multiple and the new number, hence the unit, a contradiction). The AI cites 7.32 where Heath cites 7.31; the proof-tree containment test confirms that 7.31 appears inside Heath's proof of 7.32, so the AI simply invokes the higher-level result as a unit while Heath applies the component lemma directly. The remaining ai_only items (7.34 for constructing the common multiple, plus definitions D7.1, D7.2, D7.5, D7.15 and common notions CN3, CN5) are explicit over-citations of construction steps, definitions, and axioms that Heath leaves implicit. The key intermediate conclusions are identical in both proofs, making this a granularity difference.

### 9.21
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: each even number is split into two equal halves (D7.6), those halves are combined so the whole sum also has a half, and therefore the whole is even (D7.6). The AI explicitly cites CN2 (equals added to equals are equal) to justify the step of combining the individual halves into a total, whereas Heath treats this inference as implicit. Since the ai_only item CN2 is a Common Notion (an axiom-level over-citation) and heath_only is empty, this is a straightforward Case A granularity difference: same backbone, different citation depth.

### 9.22
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: subtract one unit from each odd number to obtain even remainders (D7.7), sum the even remainders to get an even total (9.21), note the sum of the removed units equals the multitude which is even by hypothesis, then combine the two even sums to conclude the whole is even (9.21). The AI's extra citations CN2 (Common Notion 2 for the addition step) and D7.2 (definition of number to justify that the sum of n units is n) are foundational items that Heath uses implicitly without citing. Since heath_only is empty and the ai_only items are purely axiomatic/definitional over-citations, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 9.23
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) separating the odd-multitude sum so that an even count of odd numbers remains, whose sum is even by 9.22; (2) subtracting a unit from one odd number to obtain an even remainder by D7.7; (3) combining the two even quantities via 9.21; and (4) concluding the total equals that even sum plus a unit, hence odd by D7.7. The only citation difference is that the AI explicitly invokes CN2 (Common Notion 2) for an algebraic substitution step that Heath leaves implicit. Since CN2 is an axiom and the key intermediate conclusions are identical, this is a citation-depth difference, placing the proof in category G.

### 9.24
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: each splits the even minuend and even subtrahend into two equal halves (by Definition 7.6), then concludes that the remainder likewise splits into two equal halves and is therefore even. The AI proof makes the intermediate arithmetic explicit by citing Common Notions (CN2 for adding/subtracting magnitudes, CN3 for equals subtracted from equals, CN5 for the whole being greater than the part), whereas Heath leaves these inferential steps implicit. Since ai_only contains only Common Notions and heath_only is empty, the difference is purely one of citation depth, not of proof strategy. This is Case A of Q2: same backbone, different granularity.

### 9.25
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Heath proves the result directly by constructing an auxiliary even number: subtracting a unit from the odd subtrahend BC to obtain an even number DB, applying 9.24 to show that AB minus DB (i.e., AD) is even, and then concluding that CA is odd because it is one less than the even number AD. The AI instead uses proof by contradiction, assuming the remainder R is even, applying 9.24 to show that A minus R would be even, using CN3 to identify A minus R with B, and deriving a contradiction since B is odd. These represent genuinely different logical backbones -- direct construction versus reductio ad absurdum -- so the proof is classified as D (path difference). The AI's contradiction argument is logically complete and valid.

### 9.26
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof is direct: it subtracts a unit from both the odd minuend and the odd subtrahend to obtain two even numbers (AD and CD), then applies 9.24 (even minus even is even) to conclude the remainder CA is even. The AI proof takes a fundamentally different route via proof by contradiction: it assumes the remainder R is odd, observes that two odd numbers (B and R) constitute an even multitude, and applies 9.22 (the sum of an even count of odd numbers is even) to derive that A = B + R would be even, contradicting the hypothesis that A is odd. These are different logical backbones (Q2 Case B). Under Q3, the AI's proof by contradiction is logically complete and valid, with every step properly supported by citations, so the classification is D.

### 9.27
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Heath's proof is direct: it subtracts a unit from the odd number to obtain an even remainder, applies 9.24 (even minus even is even) to show an intermediate quantity is even, then restores the unit to conclude oddness via Def. 7.7. The AI proof takes a fundamentally different path via proof by contradiction: it assumes the remainder is even, then uses 9.21 (sum of even numbers is even) to show the original odd number would be even, reaching a contradiction. Since the key intermediate conclusions differ — Heath works through even-minus-even (9.24) while the AI works through even-plus-even (9.21) yielding a contradiction — the backbones are different (Q2 Case B). The AI's contradiction chain is logically complete under Q3, so the classification is D.

### 9.28
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.21 is prior and D7.15 is a definition). Both proofs follow an identical logical backbone: express the product C as a repeated sum of the even number B using Definition VII.15, observe that every summand is even, then apply Proposition IX.21 (sum of even numbers is even) to conclude C is even. The AI citation set {9.21, D7.15} equals the Heath citation set {9.21, D7.15} exactly, yielding Jaccard 1.0. Since Q1 found no logical errors, Q2 confirmed the same key intermediate conclusions, and the citation sets match perfectly, the classification is P (Perfect match).

### 9.29
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (9.23 is prior to 9.29 and D7.15 is a definition). Q1 confirmed the AI proof is logically complete: it correctly establishes that C equals A copies of B by the definition of multiplication (D7.15), observes each summand is odd and their count is odd, then applies 9.23 to conclude the sum is odd. Q2 confirmed the same backbone in both proofs. Since ai_used equals heath_refs exactly ({9.23, D7.15}), the classification is P (Perfect match).

### 9.30
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: express B as a multiple of A, show the multiplier must be even by contradiction (if odd, B would be odd), and conclude A measures half of B. The sole substantive citation difference is that the AI cites 9.29 (product of two odd numbers is odd) where Heath cites 9.23 (sum of an odd multitude of odd numbers is odd). The proof-tree containment test confirms that 9.23 appears directly inside Heath's proof of 9.29, so the AI is citing a higher-level packaging of the same underlying fact. The remaining ai_only items (CN2, D7.5, D7.6, D7.7, D7.15) are all definitions and common notions representing over-citation of implicit axioms. This is a citation-depth difference with the same backbone, yielding G.

### 9.31
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the same proof-by-contradiction backbone: assume some D > 1 measures both A and C (the double of B), conclude D must be odd because it divides odd A, apply 9.30 to show odd D measuring even C must also measure its half B, then derive a contradiction with A and B being prime to one another. The key intermediate conclusions are identical in both proofs. The ai_only set consists entirely of definitions (D7.5, D7.6, D7.7, D7.12) and one substantive proposition (9.21) cited explicitly to justify why D must be odd, a step Heath states without formal citation. The heath_only set is empty. This is classic over-citation at a finer granularity with no change to the logical backbone, placing the proof squarely in Case A of Q2.

### 9.32
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: The classification is decided at Q2 (Case B) and confirmed at Q3. Heath proves the exclusivity of even-times even by invoking 9.13, which establishes that the only divisors of the last term in a geometric progression starting from unity with a prime ratio are the preceding terms in the chain; since all chain members are even, every factorization yields even factors. The AI takes a fundamentally different route: it uses 9.30 in a descent argument to show that no odd number can divide any member of the doubling chain (an odd divisor would propagate down through successive halves until it measured the unit, a contradiction), then invokes 7.16 (commutativity of multiplication) to convert any hypothetical even-times-odd decomposition into an odd divisor, contradicting the descent result. These are genuinely different key intermediate conclusions -- 'measured only by proportional chain members' (Heath via 9.13) versus 'no odd divisor exists' (AI via 9.30) -- constituting different backbones at Q2. The AI's path is logically complete at Q3, yielding category D.

### 9.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: establish that the number is even-times odd (because its odd half measures it an even number of times), then assume for contradiction that it is also even-times even, derive that the half would need to be even, and conclude by contradiction. The AI proof adds explicit citations for definitions (D7.6, D7.7, D7.15) and propositions (7.16 for commutativity, 9.21 for the sum-of-evens result) that Heath leaves implicit or states without citation. The empty heath_only set confirms Heath cites nothing the AI lacks. Since the key intermediate conclusions are identical and the differences are purely in citation depth, this is a granularity difference.

### 9.34
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) A is even-times even because its half is not odd, by Definition VII.8; (2) successive bisection of A must terminate at an odd number (by reductio: reaching a dyad would make A one of those continually doubled from a dyad, contradicting the hypothesis), and this odd number measures A according to an even number, making A even-times odd. The AI proof elaborates each step by explicitly citing definitions (D7.2, D7.6, D7.7, D7.9, D7.15), common notions (CN2, CN5), and Proposition 7.16 (commutativity of multiplication), all of which Heath leaves implicit. Since heath_only is empty and ai_only consists entirely of definitions, common notions, and one minor theorem that merely makes explicit what Heath takes for granted, this is Case A: same backbone, different citation depth.

### 9.35
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they connect the continued proportion's individual term ratios to aggregate sums via VII.12, then derive the excess ratios using separando (VII.11) and alternando (VII.13). The order of operations differs slightly (Heath applies separando to the chain of equal ratios first then sums; the AI sums first via VII.12 then applies separando), but the logical backbone is identical. The ai_only items CN2 and D7.20 are a Common Notion and a Definition that Heath uses implicitly, representing over-citation by the AI rather than a substantive path difference. heath_only is empty, confirming no missing citations. This is Case A of Q2: same backbone, different citation depth.

### 9.36
**Category**: Path difference
**Jaccard**: 0.105
**Analysis**: Q2 decided the classification. Heath's proof and the AI proof have fundamentally different logical backbones. Heath relies on proportional reasoning (7.14 ex aequali, 7.19 product-proportion equivalence) and the geometric series summation formula 9.35 to show that FG equals the sum of all terms, then proves uniqueness of divisors through the chain 9.13, 7.29, 7.21, 7.20 (prime-to-one-another and least-number arguments). The AI instead derives a summation identity A = 1 + B directly from the doubling property, characterizes all divisors of A via 9.11 and 9.13, constructs two disjoint families of proper divisors, and proves their completeness using 7.30 (Euclid's lemma: if a prime divides a product it divides one of the factors). These represent genuinely different argumentative strategies, not merely different citation depths for the same intermediate conclusions. The AI's path is logically valid under Q3(b): every step is supported by cited propositions and the inference chain from premises to the conclusion that N is perfect is complete and sound.
