# Book 8 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 4 | 8.3, 8.7, 8.16, 8.17 |
| Granularity difference (G) | 13 | 8.2, 8.4, 8.9, 8.11, 8.12, 8.13, 8.14, 8.15, 8.18, 8.20, 8.22, 8.24, 8.25 |
| Path difference (D) | 9 | 8.1, 8.5, 8.6, 8.10, 8.19, 8.21, 8.23, 8.26, 8.27 |
| AI proof error (E) | 1 | 8.8 |

**Total**: 27 propositions

## Error Details

| Proposition | Error type | Details |
|---|---|---|
| 8.8 | Invalid inference | CANDIDATE E — 8.8   violated_claim : 'by 8.1 the extremes F0 and F(n+1) are prime to one another' (Step 4)   failure_mode   : invalid_inference   missing_is     : support — 8.1 states the converse of  |

## Per-Proposition Analysis

### 8.1
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided this classification. Heath proves 8.1 by contradiction: assuming smaller numbers in the same ratio, he uses ex aequali (7.14) to get A:D = E:H, then invokes 7.21 (primes are least) and 7.20 (least measure same-ratio numbers) to show A measures E, contradicting E < A. The AI takes a fundamentally different direct approach: it uses 7.33 to find the least numbers B1,...,Bn in the same ratio, then applies 7.20 to consecutive pairs to show all Ai = m*Bi for a common multiplier m, and finally uses coprimality of the extremes (D7.12) to force m = 1, concluding Ai = Bi. These are genuinely different logical backbones — contradiction via extremes versus direct construction with consecutive-pair chaining — but both are logically complete and valid, yielding a path difference (D).

### 8.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct terms by successive multiplication, show consecutive ratios equal A:B using VII.17/VII.18, establish that extremes are coprime via VII.22 and VII.27, and conclude the terms are least in continued proportion by VIII.1. The AI generalizes to arbitrary n via induction while Heath demonstrates the case n=4, but the key intermediate conclusions are identical. The citation differences are explained by granularity: ai_only items 7.33 (reducing to least terms) and D7.15 (definition of multiplication) are over-citations of preliminary steps Heath leaves implicit; 7.20 is used where 7.17 or 7.18 would be more precise but the underlying claim is sound. The heath_only item 7.18 reflects Heath's use of the symmetric companion to 7.17 for the case of two numbers multiplying one number, while the AI uses 7.17 throughout. The E candidate for miscitation of 7.20 was considered but rejected under the lenience rule since the mathematical claim is correct and licensable by 7.17 (which the AI cites), making it a matter of imprecise citation rather than a logical gap.
**Audit Record**: CANDIDATE E — 8.2
  violated_claim : a*c_{n-1} : b*c_{n-1} = a : b justified by 7.20
  failure_mode   : invalid_inference
  missing_is     : expansion — the claim is sound and could be licensed by 7.17 or 7.18 (which the AI cites)
  evidence       : Step 7: "a*c_{n-1} : b*c_{n-1} = a : b [7.20], since c_{n-1} is a common factor"
  why_not_terse  : 7.20 is about measurement of proportionals by least numbers, not about ratios of products with a common factor; however the claim itself is mathematically correct and supportable by 7.17
  VERDICT: NOT-E — missing_is = expansion; lenience rule applies (sound inference, imprecise citation)

### 8.3
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 8.3 follow the same logical backbone: both find the two least numbers in the given ratio (VII.33), establish their coprimality (VII.22), use VIII.2 to construct the least continued proportion with the required number of terms, identify the given sequence with the constructed one (since both are least), and conclude coprimality of the extremes via VII.27. The citation sets are identical (7.22, 7.27, 7.33, 8.2) with Jaccard similarity 1.0. No forward dependencies, no logical errors, no missing cases. The AI proof is slightly more explicit about expressing the extremes as powers (e^(n-1) and f^(n-1)) but this is a presentational difference, not a structural one. Since the key intermediate conclusions match and the citation sets are exactly equal, the classification is P (Perfect match).

### 8.4
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs share the same logical backbone: construct the continued proportion using LCM (7.34), establish proportionality of the constructed terms, and prove minimality via 7.20 and 7.35. The key citation difference is that Heath uses 7.13 (alternate proportion) and D7.20 (definition of proportional) to establish the ratio relationships, while the AI uses 7.17 (multiplication preserves ratios) as a higher-level result. The proof-tree containment test confirms that 7.13 appears inside Heath's own proof of 7.17, so the AI is citing 7.17 as a unit while Heath re-derives its internals inline. The remaining differences (D7.15, D7.2, D7.5 in ai_only; D7.20 in heath_only) are all definitions reflecting different but equivalent definitional grounding. The AI's approach of using a single general LCM-based construction rather than Heath's two separate cases (E measures K vs E does not measure K) is a presentational choice that does not alter the backbone. This is a same-backbone, different-depth situation characteristic of G.

### 8.5
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 determines the classification as D (Path difference). Heath's proof constructs least numbers in continued proportion via 8.4, then uses ex aequali (7.14) to show the ratio A:B equals the compounded ratio G:K. The AI takes a fundamentally different approach: it constructs a single intermediate number E = a*d, uses 7.17 to establish A:E = b:d, uses 7.18 to establish E:C = a:c, and then directly applies the definition of compounded ratio (D6.5) to conclude. The two proofs share only 7.17 in common (Jaccard 0.167). The heath_only propositions 7.14 and 8.4 are substantive results central to Heath's strategy but entirely absent from the AI's approach, which avoids them through a more direct construction. This is a genuine backbone difference (Case B), and the AI's alternative path is logically sound, so Q3 yields D.

### 8.6
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: The proofs have different logical backbones, leading to classification D. Heath's proof takes the least numbers F, G, H in the same ratio as A, B, C via VII.33, applies ex aequali (VII.14), uses VIII.3 to show the extremes are prime, and concludes non-measurement via the definition D7.20. The AI instead takes the least pair p:q in the basic ratio (7.33), constructs the least continued proportion via 8.2, invokes primality of extremes (logically 8.3 content, though labeled as 8.1), then uses 7.21 and 7.20 to set up a measurement-based contradiction showing e_1 = 1 implies p = 1 implies A_1 measures A_2. The AI's use of 8.1 in the direction of 8.3 was considered as a potential E (invalid inference), but under the lenience rule the conclusion is mathematically sound and follows from the converse proposition 8.3, making this a citation label error rather than a logical gap (missing_is = expansion). The key structural difference is that Heath uses 8.3 directly for prime-extremes, while the AI decomposes through 8.2 and 8.1 and relies on measurement theory (7.20, 7.21, 7.22) to reach the contradiction, constituting a genuinely different valid path.
**Audit Record**: CANDIDATE E — 8.6
  violated_claim : "By 8.1, since e_1...are the least numbers in continued proportion, the extremes e_1 and e_{j-i+1} are prime to one another"
  failure_mode   : invalid_inference
  missing_is     : expansion — the conclusion is correct and follows from 8.3 (the converse of the cited 8.1); this is a citation label error, not a logical gap
  evidence       : Step 5 cites 8.1 ("extremes prime to one another implies numbers are least") but uses it in the converse direction ("numbers are least implies extremes are prime"), which is 8.3
  why_not_terse  : The wrong proposition is cited, but the conclusion is mathematically correct via 8.3; the logical chain is sound with the correct reference
VERDICT: NOT-E (missing_is = expansion; lenience rule applies)

### 8.7
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both proofs use identical proof-by-contradiction structure: assume the first number does not measure the second, apply 8.6 to conclude no term measures any other, then note this contradicts the hypothesis that the first measures the last. The citation sets are exactly equal (both cite only 8.6), the key intermediate conclusions are the same, and there are no ai_only or heath_only differences. Since the backbone and citation set match perfectly, the classification is P.

### 8.8
**Category**: AI proof error
**Jaccard**: 0.200
**Analysis**: The classification is decided at Q1(b) by an invalid inference in Step 4 of the AI proof. The AI constructs the least numbers in continued proportion via 8.2, then claims 'by 8.1 the extremes F0 and F(n+1) are prime to one another.' However, 8.1 states the converse: 'If numbers in continued proportion have extremes prime to one another, then they are the least of those in the same ratio.' The AI needs the direction 'if they are the least, then the extremes are prime,' which is 8.3, not 8.1. This is not mere brevity or compression -- the cited proposition literally states the opposite implication from what is needed. The converse of a true implication is not logically guaranteed, so citing 8.1 does not license the conclusion that the extremes are prime. The audit record completes convincingly: the missing element is genuine logical support (not an expansion), as no reading of 8.1 yields the needed direction.
**Audit Record**: CANDIDATE E — 8.8
  violated_claim : 'by 8.1 the extremes F0 and F(n+1) are prime to one another' (Step 4)
  failure_mode   : invalid_inference
  missing_is     : support — 8.1 states the converse of what is needed; the AI needs 8.3 (if least then prime), not 8.1 (if prime then least)
  evidence       : AI Step 4: 'Since F0, F1, ..., F(n+1) are the least numbers in continued proportion in the ratio F:G, by 8.1 the extremes F0 and F(n+1) are prime to one another.' 8.1 states: 'If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio with them.' The AI has least numbers and infers prime extremes, but 8.1 goes from prime extremes to least numbers.
  why_not_terse  : This is not mere brevity — the cited proposition (8.1) literally states the converse implication. No amount of compression makes 8.1 yield 'least implies prime extremes'; that is 8.3's content.

### 8.9
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same key intermediate conclusions: (1) the sequence A, C1, ..., Cn, B constitutes the least numbers in continued proportion with the given ratio (via 8.1), (2) the terms are identified as powers of the ratio's base terms (via 8.2), and (3) the geometric sequence from the unit to A (and to B) is constructed in continued proportion. The AI adds 7.22 and 7.33 to explicitly reduce the ratio to least terms and prove coprimality, steps that Heath handles implicitly by directly taking F, G as the least in the ratio via 8.2. Heath cites D7.20 to establish proportionality from the multiplication relationships (e.g., F*F=H implies E:F::F:H), while the AI achieves the same through its algebraic power notation. These differences are purely in citation depth and expositional style, not in the logical backbone.

### 8.10
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path (D). Heath's proof constructs specific intermediate numbers H=D*F, K=D*H, L=F*H and builds the continued proportion A,K,L,B by establishing individual ratio equalities (E:H, H:G, A:K, K:L, L:B all equal D:F) using repeated applications of 7.17 and 7.18. The AI takes a fundamentally different algebraic approach, representing A=c^(k+1) and B=d^(k+1) as powers and constructing the general interpolating sequence c^(k+1-j)*d^j. It then gives a uniform proof that all consecutive pairs share the ratio c:d by factoring each pair as c^(k-j)*d^j*c and c^(k-j)*d^j*d and applying 7.17. This general parametric construction versus Heath's specific stepwise construction constitutes genuinely different key intermediate conclusions. The AI's path is logically complete: 7.16 (commutativity) justifies the rearrangement, 7.17 provides the ratio conclusion, and D7.15/D7.20 supply definitional grounding. Heath's use of 7.18 is subsumed by the AI's direct use of 7.16+7.17 (since 7.18 is proved from exactly those two propositions), but the overall proof architecture differs enough to be a path difference rather than a granularity difference.

### 8.11
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct E as the product of the two sides, use VII.17 and VII.18 to establish that the square-to-E ratio and E-to-square ratio both equal the side-to-side ratio, conclude E is the mean proportional, then apply V.Def.9 for the duplicate ratio. The AI proof uses different variable naming (sides are A,B; squares are C,D) compared to Heath (squares are A,B; sides are C,D), but the key intermediate conclusions are identical. The ai_only citations CN1 and D7.18 are over-citations of foundational axioms and definitions that Heath uses implicitly: CN1 for the transitivity step combining equal ratios, and D7.18 for the definition of square numbers. Since heath_only is empty and the ai_only items are purely axiom/definition-level citation depth differences, Case A of Q2 holds, yielding G.

### 8.12
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Both proofs establish the same backbone: constructing two mean proportionals between the cubes and showing that the four numbers form a continued proportion with common ratio equal to the side-to-side ratio, then concluding with the triplicate ratio property via V.Def.10. The AI differs only in citation depth: Heath alternates between VII.17 (one number multiplying two numbers) and VII.18 (two numbers multiplying one number) depending on how each product is factored, while the AI restructures the algebra so every ratio comparison fits the VII.18 pattern. The proof-tree containment test confirms that VII.17 appears inside Heath's proof of VII.18, so the AI's exclusive citation of VII.18 is a higher-level citation that implicitly subsumes VII.17. The ai_only items D7.15 and D7.19 are definitions (multiplication and cube number) that Heath leaves implicit. Since the key intermediate conclusions are identical and all citation differences reduce to depth, the classification is G.

### 8.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct auxiliary intermediate products to form continued proportional sequences sharing the common ratio A:B (= B:C), then apply ex aequali (7.14) to conclude D:E = E:F and G:H = H:K. Heath's proof refers to the method of the preceding proposition (8.12) with 'in manner similar to the foregoing,' implicitly using 7.17 and 7.18 which are the explicit citations in 8.12's proof. The AI instead cites 7.17 and 7.18 directly, spelling out each application to establish the intermediate proportions. This satisfies the proof-tree containment test: the AI's extra theorem citations (7.17, 7.18) appear inside the proof of the method Heath invokes implicitly, making this a citation-depth difference rather than a path difference. The AI's additional definition citations (D7.15, D7.18, D7.20) are standard over-citation of foundational definitions. The heath_only set is empty, confirming no substantive steps are missing from the AI proof.

### 8.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: establishing a continued proportion via 8.11, using 8.7 for measure propagation through the continued proportion in the first direction, and applying D7.20 for the measure-ratio connection in both directions. The AI proof adds explicit citations for sub-level arithmetic facts (7.17, 7.18 for ratio-from-multiplication relationships, 7.16 for composing measure relationships, and D7.3 as a definition) that Heath leaves implicit. Since heath_only is empty and the ai_only items are all finer-grained expansions of steps present in both proofs, this is a clear Case A same-backbone scenario with different citation depth.

### 8.15
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: construct a continued proportion between the two cubes using 8.12, apply 8.7 to transfer divisibility along the proportion, then use D7.20 to conclude divisibility of the sides (Part I), and reverse the argument for Part II. Heath additionally cites 8.11 for a separate square-number proportionality (E, F, G), which the AI omits by working directly with 8.12's explicit formulas for the mean proportionals (C=a^2*b, D=a*b^2). The AI's extra citations (D7.3, D7.15, D7.19) are definitions providing explicit grounding, and 7.17 is used for transitivity of divisibility in Part II where Heath uses D7.20 symmetrically. Since 8.11 is not contained within Heath's proof of 8.12, Heath's use of it represents a sub-construction (proportionality of squares) that the AI handles through direct computation rather than a separate theorem, but both proofs reach the same key intermediate conclusions at the same logical positions. This is a citation-depth difference, not a backbone difference.

### 8.16
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 8.16 are structurally identical. Both establish a biconditional by proving each direction via proof by contradiction using Proposition 8.14 as the sole cited result. In Part 1, both assume the side C measures the side D, invoke 8.14 to conclude the square A measures the square B, reach a contradiction with the hypothesis, and conclude C does not measure D. In Part 2, both assume A measures B, invoke 8.14 to conclude C measures D, reach a contradiction, and conclude A does not measure B. The citation sets are identical (ai_used = heath_refs = {8.14}), giving Jaccard = 1.0. Since the key intermediate conclusions are the same and the citation sets match exactly, this is a perfect match (P).

### 8.17
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of 8.17 are structurally identical. Both prove the two contrapositives of 8.15 by contradiction: (1) if the cube does not measure the cube, assume the side does measure the side, then by 8.15 the cube measures the cube, contradiction; (2) if the side does not measure the side, assume the cube does measure the cube, then by 8.15 the side measures the side, contradiction. The citation sets are identical (both cite only 8.15), the logical backbone is the same, and the Jaccard similarity is 1.0. Since Q1 finds no error, Q2 confirms the same key intermediate conclusions, and the citation sets match exactly, this is a perfect match.

### 8.18
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G. Both proofs establish the same key intermediate conclusions: (1) the sides of similar plane numbers are proportional, (2) a mean proportional G is constructed as the product of one side from each number, (3) two applications of 7.17 establish A:G and G:B as equal ratios, (4) A,G,B are in continued proportion, and (5) V.Def.9 yields the duplicate ratio. The difference lies in citation depth: Heath uses 7.13 (alternation) to convert the initial proportion C:D=E:F into C:E=D:F, while the AI reads D7.21 as directly giving c:e=d:f and uses 7.19 (products of extremes equal products of means) plus CN1 to achieve the equivalent construction. The ai_only items (7.19, CN1, D7.16) represent over-citation of definitions and common notions plus an alternative but equivalent route to the same construction, while the heath_only item (7.13) is an alternation step the AI absorbs into its reading of the definition. Since the backbone conclusions are identical and only the citation granularity differs, this is a granularity difference.

### 8.19
**Category**: Path difference
**Jaccard**: 0.571
**Analysis**: Q2 reveals different backbones: Heath constructs similar plane numbers K=C*D and L=F*G, invokes 8.18 to find their mean proportional M, uses 7.13 (alternation) to rewrite the side proportionalities, then builds N=E*M and O=H*M to obtain four numbers in continued proportion. The AI instead directly constructs the two mean proportionals as d*e*k and d*h*k by substituting one side factor at a time from A=d*e*f to B=g*h*k, showing each consecutive ratio equals f:k using 7.17 and 7.18. This avoids 8.18 and 7.13 entirely, representing a genuinely different algebraic strategy. The AI's path is logically complete under Q3(b): every step is supported by cited propositions and the chain runs from premises to conclusion without gaps, so the classification is D.

### 8.20
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Both proofs share the same logical backbone: (1) take D,E as the least numbers in ratio A:C via 7.33, (2) use 7.20 to factor A = D*F, C = E*F and C = D*G, B = E*G, establishing A and B as plane numbers, (3) show the sides are proportional (D:E = F:G), and (4) conclude A,B are similar plane numbers. The only divergence is in how step (3) is derived: Heath uses 7.17 twice to establish ratio chains and then 7.13 for alternation, while the AI uses the algebraic equality E*F = D*G, coprimality of D,E via 7.22, and the converse of 7.19 to derive D:E = F:G directly. Since the key intermediate conclusions are identical and only the sub-step justifications differ, Q2 Case A applies, yielding G. The ai_only definitions D7.16 and D7.21 are explicit citations of definitions Heath uses implicitly, confirming a citation-depth difference. The heath_only proposition 7.17 appears inside Heath's own proof of 7.19 (which the AI cites), supporting the containment interpretation for that item.

### 8.21
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Classification was decided at Q2/Q3. The proofs have fundamentally different backbones: Heath decomposes the least numbers (three terms E,F,G) as similar plane numbers via VIII.20, then builds solid numbers using the plane sides and a multiplier, proving similarity through the ratio relationships established by VII.18. The AI instead takes four least terms E,F,G,H via VIII.2, uses VIII.9 to show the prime extremes E and H are perfect cubes (by finding mean proportionals between each and the unit), then constructs solid factorizations of A and D as multiples of these cubes, yielding sides of the form (mp,p,p) and (mr,r,r). The key intermediate conclusions differ entirely: Heath's central step is that E,G are similar plane numbers (VIII.20), while the AI's central step is that E,H are cubes (VIII.9). Neither conclusion appears in the other proof. The AI's path is logically valid throughout, with each step properly supported by cited propositions, so Q3(b) yields D.

### 8.22
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Both proofs share the same logical backbone: they establish that A and C are similar plane numbers via 8.20, then conclude that since A is square, C must also be square. Heath treats the final step as obvious, while the AI expands it by explicitly invoking the definition of similar plane numbers (D7.21) to show sides are proportional, the definition of square (D7.18), and propositions 7.17 and 7.19 to formally derive that equal sides of A force equal sides of C. Since heath_only is empty and all ai_only items (7.17, 7.19, D7.18, D7.21) are sub-steps expanding Heath's implicit reasoning at the same logical position, this is a same-backbone, different-depth situation decided at Q2 Case A as Granularity difference.

### 8.23
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof is extremely concise, relying on a single high-level lemma (8.21, similar solid numbers) to conclude that since A and D have two mean proportionals between them, they are similar solid numbers, and since A is cube, D must also be cube. The AI takes a fundamentally different route: it reduces the ratio to least terms (7.33, 7.22), constructs the least four numbers in continued proportion (8.2) as e^3, e^2f, ef^2, f^3, establishes that A = k*e^3 and D = k*f^3 via divisibility (7.20), uses 8.15 to show e divides a (the cube root of A), derives that k = m^3, and concludes D = (mf)^3 is a cube. The logical backbones are entirely different: Heath argues via the concept of similar solid numbers, while the AI argues via the algebraic structure of least terms in continued proportion and cube root extraction. Both paths are logically complete and valid, yielding a path difference (D).

### 8.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that one mean proportional exists between the two given square numbers, (2) transfer that mean proportional to A and B via 8.8, and (3) conclude B is square via 8.22. The only difference is citation depth at step (1): Heath observes that squares are similar plane numbers and applies 8.18 (between similar plane numbers there is one mean proportional), while the AI applies 8.11 (between two square numbers there is one mean proportional) directly. Proposition 8.11 is a more specific result that applies directly to square numbers, whereas 8.18 is the more general version for similar plane numbers. Both reach the identical intermediate conclusion, so this is Case A of Q2 -- same backbone with different citation depth, yielding G.

### 8.25
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish that two mean proportionals exist between the two given cube numbers, (2) apply 8.8 to transfer that continued proportion to A and B, and (3) apply 8.23 to conclude B is cube. The only difference is that Heath cites 8.19 (between similar solid numbers there are two mean proportionals), first noting cubes are similar solids, while the AI cites 8.12 (between cube numbers there are two mean proportionals) directly. Since 8.12 is the cube-specific version of the same fact that 8.19 establishes for similar solids generally, the key intermediate conclusion is identical in both proofs. This is a citation-depth difference (the AI uses a more specific, directly applicable proposition), not a backbone difference, yielding G.

### 8.26
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined the classification. Both proofs use 8.18 to establish a mean proportional between the similar plane numbers, and both use 7.33 to find least numbers in a ratio. However, their key intermediate conclusions diverge: Heath uses 8.2 to find the least numbers D, E, F in the continued proportion A, C, B and deduces that the extremes D, F are square, concluding directly that A:B has the ratio of a square to a square. The AI instead works through duplicate ratios, using 8.18 to establish that A:B is the duplicate ratio of the sides, then invoking 8.11 to show that e-squared to f-squared (where e, f are the least numbers in the ratio of the sides) is also that duplicate ratio, thereby identifying A:B with the ratio of two square numbers. The proof-tree containment test confirms this is a genuine path difference: 8.2 does not appear inside the proof of 8.11, so the heath_only citation represents an independent logical route rather than a citation-depth difference. The AI's path is logically complete and valid, so Q3 yields D.

### 8.27
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as Case B (different backbone), leading to Q3 which confirmed D. Heath's proof works by finding two mean proportionals between A and B via 8.19, then reducing to least numbers in the same ratio (7.33/8.2) and showing the extremes are cubes (8.2), so A:B equals a cube-to-cube ratio. The AI takes a fundamentally different route: it uses 8.19 to establish that A:B is the triplicate ratio of a:d, then uses 8.12 to show that the ratio of the cubes a^3:d^3 is also the triplicate ratio of a:d, and applies 5.11 (transitivity of ratio equality) to conclude A:B = a^3:d^3. Since a^3 and d^3 are cube numbers by D7.19, the result follows. The AI's path is logically complete and valid but argues through entirely different intermediate conclusions than Heath's, making this a genuine path difference.
