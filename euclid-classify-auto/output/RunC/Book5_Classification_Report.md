# Book 5 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 4 | 5.4, 5.9, 5.13, 5.19 |
| Granularity difference (G) | 16 | 5.1, 5.2, 5.3, 5.5, 5.6, 5.7, 5.8, 5.10, 5.11, 5.12, 5.14, 5.16, 5.17, 5.20, 5.22, 5.24 |
| Path difference (D) | 5 | 5.15, 5.18, 5.21, 5.23, 5.25 |
| AI proof error (E) | 0 |  |

**Total**: 25 propositions

## Per-Proposition Analysis

### 5.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusion: decomposing the equimultiples into their constituent equal parts and then working pairwise with those parts to reach the conclusion. Heath's proof uses no explicit citations (heath_refs is empty), relying implicitly on the definition of multiple and basic common notions. The AI proof follows the same structural approach but explicitly cites the foundational items it invokes: D5.1 and D5.2 (definitions of part and multiple) and CN2 and CN3 (common notions about adding and subtracting equals). Since ai_only contains only definitions and common notions (no substantive propositions) and heath_only is empty, this is a Case A situation under Q2: same logical backbone with different citation depth. The AI over-cites foundational axioms and definitions that Heath leaves implicit, which is a granularity difference.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that AB contains as many parts equal to C as DE contains parts equal to F (by the definition of equimultiple), likewise for BG and EH, then combine these counts to conclude that the total AG has as many parts equal to C as DH has equal to F. The AI proof explicitly cites D5.2 (definition of equimultiple) and CN2 (common notion on addition) at each step, while Heath's proof uses these same foundational items implicitly without formal citation. Since heath_refs is empty and ai_only contains only a common notion and a definition, the difference is purely one of citation depth for foundational items, not a difference in the logical path. Case A of Q2 holds, yielding Granularity difference (G).

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: decompose the equimultiples into constituent parts equal to A and C respectively, observe that each part preserves the equimultiple relationship with B and D (since A=m*B and C=m*D), then apply Proposition 5.2 to combine these parts and conclude that the total sum maintains the equimultiple relationship. The only citation difference is that the AI explicitly cites Definition 5.2 (the definition of equimultiple) where Heath leaves this implicit. Since D5.2 is a definition rather than a substantive proposition, and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference falling under Case A of Q2, yielding a Granularity difference classification.

### 5.4
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 5.4 follow identical logical backbones: both take arbitrary equimultiples K, L of E, F and M, N of G, H, apply Proposition 5.3 to show K, L are equimultiples of A, C and M, N are equimultiples of B, D, then invoke Definition 5.5 twice -- first with the hypothesis A:B :: C:D to obtain the three-way excess/equal/less comparison, and second to conclude E:G :: F:H. The citation sets are identical (5.3 and D5.5) with Jaccard similarity 1.0, ai_only and heath_only are both empty, and the key intermediate conclusions match exactly, satisfying the perfect match criterion.

### 5.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use Proposition 5.1 to relate equimultiples of the component magnitudes, then apply subtraction to isolate the remainder and conclude it is the required multiple of the remainder. Heath constructs EB as a multiple of a new magnitude CG and uses 5.1 to combine equimultiples, while the AI decomposes each of the n copies of CD into CF and FD and uses 5.1 to recombine. The key intermediate conclusions are equivalent: both establish via 5.1 that the sum of equimultiples relates to the whole, and both subtract the known part to find the remainder. The ai_only set consists entirely of common notions (CN1, CN3) and definitions (D5.1, D5.2), which are foundational items the AI explicitly cites but Heath leaves implicit. The heath_only set is empty, confirming no substantive proposition is missing from the AI proof. This is Case A of Q2: same backbone with different citation depth, yielding Granularity difference (G).

### 5.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they use Proposition 5.2 to relate equimultiples and their parts, then show the remainders after subtraction are determined by the difference of the multipliers. Heath proves this with geometric construction (making CK equal to F) and explicit case separation, while the AI uses algebraic notation (m, n) for a unified argument but reaches the same key intermediate conclusions. The ai_only citations (CN3, D5.2) are a common notion and a definition that Heath uses implicitly without explicit citation. Heath_only is empty. This pattern of the AI over-citing foundational axioms and definitions while following the same proof strategy is a citation-depth difference, not a path difference.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: (1) establish that equimultiples of equal magnitudes are equal (mA = mB from A = B), (2) infer that equal equimultiples bear the same order relation to any multiple of C, then apply Definition 5.5 to conclude A:C = B:C, and (3) repeat the argument with reversed positions to conclude C:A = C:B. The only difference is citation depth: the AI explicitly cites CN1 (equals bear the same relations), CN2 (adding equals yields equals), and D5.2 (definition of equimultiple), while Heath uses these foundational facts implicitly without citing them by name. Since heath_only is empty and all ai_only items are common notions and definitions rather than substantive propositions, this is a clear case of over-citation at the axiomatic level with no backbone divergence, yielding a Granularity difference (G).

### 5.8
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they construct equimultiples of the original magnitudes (mA and mC), find a suitable comparison multiple (nB), and demonstrate the inequality pair required by D5.7 (mA > nB while mC does not exceed nB). The AI takes a more streamlined algebraic approach using the excess E = A - C directly rather than Heath's geometric construction with labeled points, but the logical backbone is identical. Heath's two geometric cases (AE < EB vs AE > EB) are absorbed by the AI's single general argument, which is valid because it does not depend on which part of the excess is smaller. The only citation difference is that the AI explicitly cites CN5 (the whole is greater than the part) in Case 2 of Part (ii), where Heath simply says the demonstration follows the same pattern as before. Since heath_only is empty and ai_only contains only the common notion CN5, this is a citation-depth difference with the same backbone, yielding G.

### 5.9
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs of 5.9 follow identical logical structure: two cases proved by contradiction using only Proposition 5.8. Case 1 shows that if A:C = B:C then A = B (since assuming A != B leads to A:C != B:C by 5.8, contradicting the hypothesis). Case 2 shows that if C:A = C:B then A = B (since assuming A != B leads to C:A != C:B by 5.8, contradicting the hypothesis). The citation sets are exactly equal (both cite only 5.8), the key intermediate conclusions are identical, and the logical backbone is the same. The AI proof is more verbose, spelling out the contradiction in greater detail, but this does not affect the classification. Since ai_used equals heath_refs exactly and the backbones match, this is a perfect match.

### 5.10
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both the AI and Heath proofs follow the identical logical backbone: a two-case proof by contradiction. In each case, equality is ruled out via 5.7 and the wrong inequality is ruled out via 5.8, leaving the desired conclusion. The key intermediate conclusions are the same in both proofs in the same order. The only citation difference is that the AI additionally cites D5.7 (the definition of greater ratio), which Heath uses implicitly without explicit citation. Since ai_only contains only this definition and heath_only is empty, this is a classic over-citation of a definitional item, constituting a citation-depth difference rather than a path difference. The citation sets are not identical (ai_used includes D5.7), so Perfect match (P) does not apply.

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: (1) take equimultiples of A, C, E and of B, D, F; (2) apply Definition 5.5 to A:B :: C:D to get that the comparison of multiples of A and B determines the comparison of multiples of C and D; (3) apply Definition 5.5 to C:D :: E:F to get the analogous result for C, D and E, F; (4) chain these two results so that the comparison of multiples of A and B determines the comparison of multiples of E and F; (5) conclude A:B :: E:F by Definition 5.5. The only difference is that the AI explicitly cites D5.5 while Heath's proof uses the definition implicitly without a formal citation. Since heath_refs is empty and ai_only contains only a definition (D5.5), this is a same-backbone, different-citation-depth situation (Case A), yielding G.

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they take equimultiples, use the definition of proportion (D5.5) to extract simultaneous comparisons from the given proportionality, aggregate those comparisons across all pairs by adding inequalities and equalities, use V.1 to relate individual equimultiples to equimultiples of the sums, and conclude by D5.5. The AI over-cites definitions (D5.1-D5.4) and Common Notion 2 that Heath leaves implicit, but these are axiom-level over-citations, not substantive path differences. With heath_only empty and ai_only consisting entirely of definitions and a common notion, and the key intermediate conclusions matching between both proofs, this is a clear Case A granularity difference.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of Proposition 5.13 follow identical logical backbones and cite exactly the same references. Both proofs (1) invoke Definition 5.7 to obtain equimultiples of C,E and D,F such that the multiple of C exceeds the multiple of D while the multiple of E does not exceed the multiple of F; (2) form the corresponding equimultiples of A and B using the same multipliers; (3) apply Definition 5.5 (the definition of same ratio for A:B :: C:D) to transfer the excess relationship; and (4) apply Definition 5.7 again to conclude A:B > E:F. The citation sets are identical (D5.5, D5.7) with Jaccard similarity 1.0, and since both the key intermediate conclusions and the citation sets match exactly, the classification is P (Perfect match).

### 5.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Heath's proof explicitly works out only the case A > C (using 5.8, 5.13, 5.10) and abbreviates the remaining two cases with 'similarly we can prove.' The AI proof uses the identical logical backbone for Case 1 (A > C): 5.8 yields A:B > C:B, 5.13 with the hypothesis yields C:D > C:B, and 5.10 concludes D < B. The AI then explicitly proves Case 2 (A = C) using 5.7, 5.11, 5.9 and Case 3 (A < C) using 5.8, 5.13, 5.10, which are the cases Heath leaves to the reader. All ai_only citations (5.7, 5.9, 5.11, D5.5) serve these elaborated cases or reference the definition of same ratio. Since the key intermediate conclusions match for the shared explicit case, and the extra AI citations arise solely from spelling out what Heath abbreviates, this is a citation-depth difference, yielding G.

### 5.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof divides the multiples into unit parts equal to the original magnitudes, then uses V.7 (equal magnitudes have the same ratio) to establish ratios between corresponding parts, and V.12 (antecedent-to-consequent ratio equals all-antecedents-to-all-consequents) to combine them. The AI proof takes a fundamentally different approach: it appeals directly to Definition 5.5 (the equimultiple definition of ratio), uses Proposition 5.3 to establish that a multiple of a multiple equals a higher multiple of the original, and then shows via CN2 that ordering is preserved. The two proofs share zero citations (Jaccard = 0.0), and the containment test confirms that heath_only items 5.7 and 5.12 do not appear in the proof tree of any AI-cited proposition. The key intermediate conclusions differ entirely: Heath works through decomposition and recombination of multiples, while the AI works through the definitional characterization of ratio and algebraic properties of multiples. The AI's path is logically valid under the hardened 1(b) standard, yielding D.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) equimultiples of the first pair preserve the ratio (by 5.15), (2) equimultiples of the second pair preserve their ratio (by 5.15), (3) transitivity chains these proportions together (by 5.11), (4) the trichotomy comparison follows (by 5.14), and (5) the definition of proportion (D5.5) yields the alternate proportion. The only citation difference is that the AI explicitly cites D5.12 (the definition of alternate ratio) when setting up the problem in Step 1, while Heath does not cite this definition. Since D5.12 is a definition rather than a substantive proposition, this is a classic over-citation at the definitional level, constituting a citation-depth difference under Case A of Q2.

### 5.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: (1) construct equimultiples of the compound magnitudes using 5.1, (2) construct combined equimultiples of the parts using 5.2, (3) apply the proportion hypothesis to obtain the trichotomy for compound multiples, (4) subtract common terms to reduce to a trichotomy on the separated multiples, and (5) conclude by the definition of proportion. The ai_only set consists entirely of definitions (D5.5, D5.14, D5.15) and common notions (CN2, CN3, CN5) that Heath uses implicitly but does not cite. For example, Heath writes 'if HK be subtracted from each' which is exactly CN3, and Heath implicitly invokes the definition of proportion (D5.5) when applying the equimultiple criterion. The heath_only set is empty. This is a clear Case A: same backbone, different citation depth, classifying as G.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as D (path difference). Heath proves 5.18 by reductio ad absurdum: assuming AB:BE equals CD:DG for DG less than DF, applying 5.17 (separando) to get AE:EB = CG:GD, then using 5.11 (transitivity of ratios) and 5.14 (ordering from ratios) to derive the contradiction GD > FD. The AI instead gives a direct proof from the definition of proportion (D5.5), showing that for arbitrary equimultiples m and n, the threefold condition transfers from the separando ratios to the componendo ratios by algebraic decomposition (AB = AE + EB implies m*AB = m*AE + m*EB), splitting into three sub-cases (n > m, n = m, n < m). The AI uses no prior theorems at all, working entirely from definitions (D5.5, D5.14, D5.15) and common notions (CN2, CN3, CN5), resulting in zero citation overlap (Jaccard = 0.0). These are fundamentally different proof strategies with no shared key intermediate conclusions, constituting a genuine path difference. The AI proof is logically complete under the Q1(b) hardened standard.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow the identical logical backbone: given AB:CD = AE:CF, both apply alternando (5.16) to obtain AB:AE = CD:CF, then separando (5.17) to derive EB:AE = FD:CF, then alternando (5.16) again to reach EB:FD = AE:CF, and finally transitivity of ratios (5.11) to conclude EB:FD = AB:CD. The citation sets are identical (ai_used = heath_refs = {5.11, 5.16, 5.17}) with Jaccard similarity 1.0, and the key intermediate conclusions match at every stage. Since the proofs share the same backbone and the same citation set, this is a perfect match.

### 5.20
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: for the A > C case, they establish A:B > C:B via 5.8, then use 5.13 to derive D:E > F:E via the given and inverse ratios, and conclude D > F via 5.10. Heath handles the A = C and A < C cases with 'similarly we can prove,' while the AI spells them out explicitly, citing 5.7, 5.9, and 5.11 for the equality case and reusing 5.8, 5.13, 5.10 for the less-than case. The AI also explicitly cites D5.5 to justify the inverse ratio step that Heath performs implicitly. Since heath_only is empty and all ai_only items (5.7, 5.9, 5.11, D5.5) represent either explicit treatment of cases Heath leaves as exercises or more granular citation of implicit steps, the proofs reach the same key intermediate conclusions at different citation depths, yielding a granularity difference.

### 5.21
**Category**: Path difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path (D). Heath's proof of the A > C case operates at the level of ratio comparisons: it uses 5.8 to get A:B > C:B, then 5.13 to transfer the greater-ratio through the hypotheses to get E:F > E:D, and finally 5.10 to conclude F < D. The AI proof instead works directly from the definitions of ratio (D5.5 and D5.7), unpacking 'greater ratio' into specific multiples m and n, then using D5.5 to transfer the multiple-inequalities through the ratio hypotheses, and assembling D > F from arithmetic on multiples without ever establishing ratio-comparison intermediate conclusions. The key intermediate conclusions differ: Heath reasons about ratio orderings (E:F > E:D) while the AI reasons about specific multiples (mE > nF, nD > mE). Furthermore, for Case 2 (A = C), the AI uses proof by contradiction while Heath merely says 'similarly we can prove.' The proof-tree containment test shows that 5.10 and 5.13 (heath_only) are not inside the proof of any proposition the AI cites as a unit; rather, the AI re-derives their substance from definitions, constituting a genuinely different proof strategy. The AI's path is logically complete and valid under the hardened 1(b) standard.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they take equimultiples of the outer terms, establish that equimultiples of the first pair maintain the same ratio, establish that equimultiples of the second pair maintain the same ratio, apply 5.20 for the ordering result on three pairs, and conclude via D5.5. The difference is purely in citation depth: Heath applies 5.4 directly to get G:K = H:L, while the AI breaks this down into 5.15 (parts have the same ratio as multiples) and 5.11 (transitivity of ratios) to reach the equivalent conclusion mA:mB = mD:mE. The AI also cites D5.17 (definition of ex aequali) for context. All ai_only items (5.11, 5.15, D5.17) represent finer-grained citation of the same underlying reasoning, and heath_only is empty, confirming this is a granularity difference rather than a path divergence.

### 5.23
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 determined the classification. Both proofs establish a perturbed proportion among equimultiples and then apply 5.21, but they reach the critical second ratio relationship by genuinely different methods. Heath uses alternation (5.16) on the hypothesis B:C = D:E to get B:D = C:E, then builds equimultiple ratios through repeated 5.15/5.11 applications. The AI instead applies 5.4 directly to B:C = D:E to obtain mB:nC = mD:nE in a single step. The proof-tree containment test confirms these are independent routes: 5.16 does not appear in Heath's proof of 5.4 (which uses 5.3 and D5.5). Since the backbone differs but the AI's path is logically sound under the hardened 1(b) standard, the classification is D.

### 5.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: (1) invert a given proportion, (2) apply ex aequali (5.22) to obtain a ratio between the first and fifth magnitudes, (3) apply componendo/separando (5.18) to compose the magnitudes, and (4) apply ex aequali (5.22) again to reach the final conclusion. The only difference is that the AI explicitly cites definitions D5.5 and D5.13 to justify the inversion step, whereas Heath performs the same inversion implicitly without citing these definitions. Since heath_only is empty and ai_only contains only definitions (not substantive propositions), this is a clear case of over-citation at different granularity with the same underlying logical structure.

### 5.25
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined the classification. Heath's proof constructs auxiliary segments AG=E and CH=F, then applies V.19 (remainder proportionality) to establish GB:HD :: AB:CD, from which GB > HD follows since AB > CD, and combines this with AG+F = CH+E to reach the conclusion. The AI instead uses alternando (5.16) and 5.14 to establish ordering relationships (C > D, B > D), then applies separando (5.17) followed by alternando and 5.14 again to establish A-B > C-D, and finally uses arithmetic (CN2, CN5) to conclude A+D > B+C. The key intermediate conclusions are fundamentally different: Heath pivots on remainder proportionality (5.19), while the AI pivots on the difference inequality A-B > C-D obtained through separando and alternando. The citation sets are completely disjoint (Jaccard = 0.0), confirming the different logical routes. Under Q3, the AI's chain is logically complete: each step validly applies its cited proposition, and the conclusion follows. Therefore the classification is D (path difference).
