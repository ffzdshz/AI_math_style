# Book 5 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 5.13, 5.19 |
| Granularity difference (G) | 17 | 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.9, 5.10, 5.11, 5.12, 5.14, 5.16, 5.17, 5.21, 5.22, 5.24 |
| Path difference (D) | 6 | 5.8, 5.15, 5.18, 5.20, 5.23, 5.25 |
| AI proof error (E) | 0 |  |

**Total**: 25 propositions

## Per-Proposition Analysis

### 5.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification as G (Granularity difference). Heath's proof of 5.1 cites no references (heath_refs is empty), working entirely from first principles and the definition of equimultiples. The AI proof establishes the same type of result using the same fundamental method -- decomposing multiples into unit parts and manipulating them -- but explicitly cites CN2 (equals added to equals), CN3 (equals subtracted from equals), D5.1, and D5.2 (definition of multiple). These are all common notions and definitions that Heath invokes implicitly without formal citation. The ai_only set contains exclusively axioms and definitions (CN2, CN3, D5.1, D5.2) with no substantive propositions, which is the hallmark of over-citation at a finer granularity. No forward dependencies were found. No logical errors were identified in the AI proof under the hardened 1(b) standard. The Jaccard similarity is 0.0 because Heath has no citations while the AI has four, but this reflects citation-depth difference rather than a genuine path divergence.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: decompose the first pair of equimultiples into equal parts, decompose the second pair into equal parts, then combine them to show the sums contain the same count of equal parts. The AI's key intermediate conclusions match Heath's exactly. The only difference is citation depth: Heath's proof uses no explicit citations (his reference list is empty), while the AI explicitly cites D5.2 (definition of equimultiple) and CN2 (Common Notion 2, addition of equals). Both of these are foundational items (a definition and a common notion) that Heath uses implicitly. This is a textbook Case A granularity difference: same backbone, the AI is simply more explicit about its definitional and axiomatic foundations.

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: decompose the equimultiples into parts equal to A and C respectively, observe that each part is the same multiple of B (or D) by hypothesis, then apply Proposition 5.2 to combine the parts and conclude that the total equimultiples are equimultiples of B and D. The only citation difference is that the AI explicitly cites Definition 5.2 (D5.2) when establishing the equimultiple relationships, while Heath uses the concept implicitly without citing the definition. This is a citation-depth difference (over-citation of a definition), not a backbone difference, placing this squarely in Case A of Q2.

### 5.4
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take arbitrary equimultiples of the given equimultiples, use Proposition 5.3 to collapse double equimultiples into single equimultiples of the original magnitudes, apply Definition 5.5 to the hypothesis A:B :: C:D with these collapsed equimultiples to obtain the three-way exceed/equal/less-than comparison, then apply Definition 5.5 a second time to conclude the desired ratio. The only citation difference is that the AI explicitly cites D5.2 (the definition of equimultiple), which Heath leaves implicit. Since D5.2 is a non-substantive definition and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference under Q2 Case A, yielding G.

### 5.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they use Proposition 5.1 as the central tool to combine multiples, then use algebraic manipulation (subtraction of equal parts) to isolate the remainder EB and show it is the same multiple of FD as AB is of CD. The AI's ai_only citations (CN1, CN3, D5.2) are exclusively common notions and a definition that Heath uses implicitly without citing. Heath implicitly applies CN3 when subtracting CF from both GF and CD, implicitly uses CN1 when equating magnitudes that are both equal to the same multiple, and implicitly relies on D5.2 (the definition of equimultiple) without citing it. The AI merely makes these implicit steps explicit, which is a citation-depth difference, not a path difference. The heath_only set is empty, confirming no substantive proposition is missing from the AI proof.

### 5.6
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: they show that the subtracted equimultiple plus the remainder equals the original equimultiple (using 5.2), then subtract to isolate the remainder, and finally split into two cases (remainder equals the magnitude, or remainder is a proper equimultiple). The AI uses algebraic multiplier notation while Heath uses geometric construction with named magnitudes, but the logical backbone is identical. The ai_only set consists entirely of common notions (CN3, CN5) and a definition (D5.2), which are axiom-level items that Heath uses implicitly without citing. Since heath_only is empty and all ai_only items are non-substantive over-citations, this is a citation-depth difference with the same backbone, yielding G.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: for each of the two parts (A:C=B:C and C:A=C:B), they take equimultiples, derive equality of the equimultiples from A=B, apply the trichotomy comparison, and conclude via Definition 5.5. The AI proof explicitly cites CN1 (equals compared to the same yield the same relation), CN2 (equals added to equals yield equals, used to justify that equimultiples of equal magnitudes are equal), and D5.2 (definition of equimultiple), all of which Heath uses implicitly without citation. The heath_only set is empty, confirming no substantive divergence. This is a clear case of same backbone with different citation depth, classifying as G.

### 5.8
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof constructs equimultiples of AB and C (via splitting AB into AE and EB with BE=C) compared against successive multiples of an arbitrary third magnitude D, requiring two cases depending on whether AE is less or greater than EB. The AI proof takes a fundamentally different approach: it defines D as the excess A minus B, chooses m so that mD exceeds C via the Archimedean property (D5.4), then uses 5.1 to express mA as mB plus mD, and selects n as the greatest integer with nC not exceeding mB. This single unified construction avoids case analysis entirely and directly produces multipliers satisfying D5.7 for both parts of the proposition. The key intermediate conclusions differ structurally: Heath establishes that FH exceeds N while K does not exceed N (where FH and K are equimultiples of AB and C, and N is a multiple of D), whereas the AI establishes that mA exceeds (n+1)C while mB does not exceed (n+1)C. Both paths are logically complete but arrive at the D5.7 application through genuinely different constructions and intermediate facts.

### 5.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the identical logical backbone: a two-case proof by contradiction, where each case assumes A is not equal to B and derives a contradiction using Proposition 5.8, which states that the greater magnitude has a greater ratio. The AI proof and Heath's proof establish the same key intermediate conclusions in the same order for both parts of the proposition. The only difference is that the AI explicitly cites Definition 5.5 (same ratio) and Definition 5.7 (greater ratio) to clarify the notions being used, whereas Heath invokes these definitions implicitly. Since ai_only contains only definitions (D5.5, D5.7) and heath_only is empty, this is a case of over-citation by the AI at the definitional level, which is a citation-depth difference rather than a path difference.

### 5.10
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decides: both proofs argue through identical key intermediate conclusions across both required parts of this two-case proposition. Part 1 (A:C > B:C implies A > B) and Part 2 (C:B > C:A implies B < A) each proceed by proof by contradiction, eliminating the equality case via V.7/5.7 and the wrong-inequality case via V.8/5.8. The logical backbone is the same in both proofs. The only citation difference is that the AI explicitly cites D5.7 (the definition of greater ratio) when setting up its hypotheses, while Heath uses the concept implicitly. Since D5.7 is a definition and the ai_only set contains only this definitional over-citation with an empty heath_only set, this is a citation-depth difference under Case A of Q2, yielding Granularity difference (G).

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical logical backbone: take equimultiples of A, C, E by the same multiplier and equimultiples of B, D, F by the same multiplier; from A:B :: C:D deduce that the comparison of mA vs nB determines the comparison of mC vs nD; from C:D :: E:F deduce that the comparison of mC vs nD determines the comparison of mE vs nF; chain these to conclude that mA vs nB determines mE vs nF; and conclude A:B :: E:F by the definition of proportionality. The only citation difference is that the AI explicitly cites D5.5 (Definition V.5 of equal ratios) while Heath applies the same definition implicitly without a formal citation. This is a classic over-citation of a foundational definition, making the proofs identical in substance but different in citation depth.

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: take equimultiples G, H, K of the antecedents A, C, E and equimultiples L, M, N of the consequents B, D, F; use the proportionality hypothesis with D5.5 to establish that G, H, K simultaneously exceed, equal, or fall short of L, M, N; combine these to show G+H+K simultaneously exceeds, equals, or falls short of L+M+N; establish that G+H+K is the same multiple of A+C+E as G is of A (and similarly for the consequents); then conclude by D5.5. The only difference is citation depth: Heath cites 5.1 as a packaged result for the step that combines equimultiples into a single multiple of the sum, while the AI derives this same fact inline using CN2 (addition axiom) and D5.2 (definition of equimultiples). The ai_only items (CN2, D5.2, D5.6) are all definitions and common notions, not substantive theorems, confirming this is a depth-of-citation difference rather than a different proof path.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: Both the AI and Heath proofs establish the same key intermediate conclusions using the same citation set {D5.5, D5.7}. The logical backbone is identical: (1) apply D5.7 to obtain equimultiples of C,E and D,F where the multiple of C exceeds the multiple of D but the multiple of E does not exceed the multiple of F; (2) form corresponding equimultiples of A and B; (3) apply D5.5 to conclude that since A:B :: C:D and the multiple of C exceeds the multiple of D, the multiple of A exceeds the multiple of B; (4) apply D5.7 to conclude A:B > E:F. Since both the key conclusions and the citation sets are identical, this is a perfect match.

### 5.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Heath's proof of 5.14 explicitly proves only Case 1 (A > C) using 5.8, 5.13, and 5.10, then handles Cases 2 (A = C) and 3 (A < C) with 'similarly we can prove.' The AI proof establishes the identical backbone for Case 1 — A:B > C:B by 5.8, then C:D > C:B by 5.13, then D < B by 5.10 — but goes further by explicitly proving the other two cases: Case 2 uses 5.7, 5.11, and 5.9, and Case 3 mirrors Case 1 with 5.8, 5.13, and 5.10. The ai_only citations (5.7, 5.9, 5.11, D5.5) are entirely attributable to the AI's greater explicitness in proving cases Heath leaves implicit and citing the definition for the ratio hypothesis. With heath_only empty and the key logical backbone identical for the explicitly proved case, this is a same-backbone, different-depth situation characteristic of G.

### 5.15
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof divides the multiples AB and DE into parts equal to C and F respectively, then uses V.7 (equal magnitudes have the same ratio) to establish proportionality among corresponding parts, and V.12 (as one antecedent to one consequent, so all antecedents to all consequents) to recombine. The AI proof takes a fundamentally different approach: it goes directly to Definition 5.5's criterion for ratio equality, uses V.5.3 to show commutativity of iterated multiples (nC = m(nA) and pD = m(pB)), then verifies all three order cases using CN2 and CN5. The proof-tree containment test confirms the divergence: neither 5.7 nor 5.12 (Heath's key citations) appears in the proof tree of any AI-cited proposition. The backbones are entirely different, making this Case B. Q3 confirms the AI's path is logically valid and complete, yielding classification D.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: take equimultiples of A,B and C,D, use V.15 to relate each pair's ratio to the original ratio, chain via V.11 with the hypothesis to equate the equimultiple ratios, apply V.14 for trichotomy, and conclude by D5.5. The AI's only extra citation is D5.12 (a definition about magnitudes of the same kind), which is a purely definitional over-citation that Heath leaves implicit. Since the key intermediate conclusions are the same in both proofs and the citation difference is limited to a single definition, this is a granularity difference (Case A of Q2).

### 5.17
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) construct equimultiples and use 5.1 to form multiples of the composite magnitudes AB and CD, (2) use 5.2 to form combined equimultiples of EB and FD, (3) apply the proportion hypothesis to get the excess/equal/less trichotomy, (4) subtract common quantities to transfer the condition to the component parts AE vs EB and CF vs FD, and (5) conclude by the definition of proportion. The ai_only citations CN3, D5.14, D5.15, and D5.5 are all definitions and common notions that Heath uses implicitly without explicit citation. The AI makes these foundational references explicit, which is a citation-depth difference, not a structural divergence. Since heath_only is empty and all ai_only items are axiom-level over-citations, this is a clear Case A granularity difference.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this classification as D (path difference). Heath proves 5.18 by contradiction: assuming the componendo proportion fails, he applies 5.17 (the converse, separando from componendo), then 5.11 (transitivity of ratios) and 5.14 (order-preserving property of equal ratios) to derive a contradiction. The AI proof takes an entirely different approach, working directly from the equimultiple definition of proportion (D5.5). It uses 5.1 to distribute multiples over sums, then breaks into cases based on whether n > m or n <= m, verifying the equimultiple condition in each case using the hypothesis and common notions. The two proofs share zero citations (Jaccard = 0.0) and have completely different logical backbones: Heath's contradiction via the converse versus the AI's direct definitional verification. The AI's path is logically sound and complete, satisfying Q3, so the classification is D.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: both start from the hypothesis AB:CD = AE:CF, apply alternation (5.16) to obtain AB:AE = CD:CF, then apply separando (5.17) to get EB:AE = FD:CF, then alternate again (5.16) to obtain EB:FD = AE:CF, and finally use transitivity (5.11) to conclude EB:FD = AB:CD. The citation sets are exactly identical at {5.11, 5.16, 5.17} with Jaccard similarity 1.0, and the key intermediate conclusions match at every stage, satisfying the perfect match criteria.

### 5.20
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 determines the classification. Heath's proof of the A>C case establishes D:E > F:E by combining both given proportions with 5.13 (using the inverse), then concludes D > F via 5.10 (greater ratio to the same implies greater magnitude). The AI proof instead uses 5.13 only to get D:E > C:B, then drops to definition-level equimultiple reasoning (D5.7, D5.5) to establish D > F directly without ever forming the comparison D:E > F:E or citing 5.10. The heath_only citation 5.10 does not appear inside Heath's proofs of any AI-cited proposition, so the proof-tree containment test fails and this is not a granularity difference. Furthermore, for the A=C case, Heath says 'similarly we can prove' while the AI uses an entirely different proof by contradiction approach via 5.7 and 5.11. These constitute genuinely different logical backbones. The AI's path is logically complete and valid throughout all three cases, so Q3 yields D.

### 5.21
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone for Case I (A > C): deriving A:B > C:B from A > C via 5.8, obtaining E:F > E:D via 5.13 and the inverse ratio, then concluding D > F via 5.10. Heath dismisses Cases II and III with 'similarly,' while the AI proves all three cases explicitly, which accounts for the ai_only propositions 5.7, 5.9, and 5.11 (used in the equal and less-than cases). The remaining ai_only items are definitions (D5.5, D5.13, D5.18) that the AI cites explicitly where Heath leaves them implicit. Since heath_only is empty and all divergences are explained by the AI's greater explicitness rather than a different proof strategy, this is a citation-depth difference, not a path difference.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions for the three-magnitude case: (1) applying V.4 twice to derive ratio relationships among equimultiples, (2) applying V.20 to conclude the ex aequali ordering, and (3) applying V. Def. 5 to conclude A:C = D:F. The AI proof has the same logical backbone as Heath's. The only citation difference is that the AI explicitly cites D5.17 (the definition of ex aequali ratio), which Heath uses implicitly without citation. Since D5.17 is a definition and not a substantive proposition, this is a citation-depth difference. The AI also extends the proof to the general case via induction (Steps 8-12), which Heath omits, but this is additional granularity rather than a different path. Case A of Q2 holds, yielding G.

### 5.23
**Category**: Path difference
**Jaccard**: 0.375
**Analysis**: Q2 decides the classification as D (path difference). The two proofs use fundamentally different equimultiple groupings: Heath takes G, H as equimultiples of A, B and K of D (first group), with L, M of C, E and N of F (second group), then uses alternation (5.16) twice as a key technique to establish H:L = K:M. The AI instead takes G, H, K as equimultiples of A, D, E and L, M, N of B, C, F, then uses 5.4 to directly derive G:L = K:N from A:B = E:F across the two multiplier groups. This leads to different intermediate conclusions: Heath establishes G:H = M:N and H:L = K:M before applying 5.21, while the AI establishes G:L = K:N and L:M = H:K before applying 5.21 to a differently-constituted set of six magnitudes. The containment test confirms this is genuine path divergence since 5.16 (heath_only) does not appear inside Heath's proof of 5.4 (ai_only). The AI's alternative path is logically valid throughout, with each step properly justified by cited propositions.

### 5.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: (1) invert one given ratio, (2) apply ex aequali (5.22) to combine with the other given ratio, (3) apply componendo (5.18), and (4) apply ex aequali (5.22) again to reach the final conclusion. The AI's only extra citations are D5.5 and D5.13, which are definitions used to explicitly justify the inversion step that Heath performs without citing a definitional basis. Since heath_only is empty and the ai_only items are purely definitional over-citations, this is a clear Case A granularity difference with the same backbone at different citation depth.

### 5.25
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs auxiliary magnitudes AG=E and CH=F, then applies V.19 (the remainder proposition) to establish GB:HD :: AB:CD, deducing GB > HD from AB > CD, and finally combines the equalities AG+F = CH+E with GB > HD to reach AB+F > CD+E. The AI takes a fundamentally different route: it establishes ordering relations (A > B, B > D, C > D) using 5.14 and 5.16, then applies 5.17 (separando) directly to the original proportion to get (A-B):B :: (C-D):D, uses 5.14 to show A-B > C-D, and adds B+D to both sides via CN2. Although 5.16 and 5.17 appear inside Heath's proof of 5.19, the AI does not cite 5.19 and uses these propositions in entirely different logical roles — the AI's key intermediates (establishing G > H where G=A-B, H=C-D) differ from Heath's (establishing GB:HD proportionality via the remainder theorem). This constitutes a genuinely different backbone, confirmed as logically valid at Q3.
