# Book 5 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 3 | 5.4, 5.13, 5.19 |
| Granularity difference (G) | 20 | 5.2, 5.3, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11, 5.12, 5.14, 5.15, 5.16, 5.17, 5.20, 5.21, 5.22, 5.23, 5.24, 5.25 |
| Path difference (D) | 2 | 5.1, 5.18 |
| AI proof error (E) | 0 |  |

**Total**: 25 propositions

## Per-Proposition Analysis

### 5.1
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The forward-dependency gate passes since all AI citations (CN1, CN2, CN3, CN5, D5.2) are Common Notions and Definitions. Q1 finds no logical defects: the AI proof is a thorough, step-by-step demonstration with every claim properly supported by cited Common Notions and the definition of multiples. Q2 reveals completely different backbones: the Heath proof establishes that equimultiples of magnitudes sum to equimultiples of the sum, while the AI proof establishes that if the whole and the subtracted part are equimultiples, then the remainders are also equimultiples. Since the two proofs argue through entirely different key intermediate conclusions (Case B), Q3 applies. The AI's path is logically complete and valid -- every step is justified by cited axioms or definitions, and the chain runs from premises to conclusion without gaps -- yielding a D classification.

### 5.2
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decides this classification. Both proofs establish identical key intermediate conclusions: decomposing the first and fifth magnitudes into counted parts equal to the second magnitude, decomposing the third and sixth into counted parts equal to the fourth, then combining to show the sums are the same multiple. The AI explicitly cites Definition 5.2 (definition of multiple) at each step while Heath applies the same definition implicitly without formal citation. Since heath_only is empty and ai_only contains only a definition (D5.2), this is a citation-depth difference (Case A of Q2), yielding G.

### 5.3
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: dividing the equimultiples EF and GH into parts equal to A and C respectively, establishing that each part of EF is the same multiple of B as the corresponding part of GH is of D, and then applying V.2 to conclude that the sums maintain this equimultiple relationship. The only citation difference is that the AI explicitly invokes Definition 5.2 (the definition of equimultiple) where Heath leaves this implicit. Since D5.2 is a definition rather than a substantive proposition, this represents a citation-depth difference with no change to the logical backbone. This is Case A of Q2, yielding G.

### 5.4
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (5.3 is prior to 5.4 and D5.5 is a definition). Both proofs follow the identical logical backbone: after setting up the equimultiples E, F of A, C and G, H of B, D, both take further equimultiples K, L of E, F and M, N of G, H; both invoke 5.3 to show K, L are equimultiples of A, C and M, N are equimultiples of B, D; both apply Definition 5.5 to obtain the trichotomy and then again to conclude E:G :: F:H. The citation sets are identical (ai_used = heath_refs = {5.3, D5.5}), the Jaccard similarity is 1.0, and the key intermediate conclusions match exactly, yielding a Perfect match classification.

### 5.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct an auxiliary magnitude as the same multiple (Heath uses CG, the AI uses FD directly), apply V.1/5.1 to sum equimultiples, invoke the hypothesis to establish equality with AB, subtract to identify the auxiliary with the remainder EB, and conclude that EB is the desired multiple of FD. The ai_only set consists entirely of common notions (CN1, CN2, CN3) and a definition (D5.2) that Heath employs implicitly without citation, while heath_only is empty. This is a textbook over-citation pattern: the AI makes explicit the foundational axioms that Heath leaves tacit, producing a citation-depth difference with no divergence in the argumentative backbone.

### 5.6
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct CK equal to F (or the appropriate multiple of F), apply 5.2 to show AB is the same multiple of E that KH is of F, conclude KH equals CD since both are the same multiple of F, subtract the common magnitude CH to get KC equals HD, and then conclude HD equals F (Case 1) or HD is the same multiple of F as GB is of E (Case 2). The AI proof explicitly handles both cases while Heath dispatches Case 2 with 'similarly,' but the underlying argument structure is identical. The ai_only citations (CN1, CN3, CN5, D5.2) are all Common Notions and a Definition that Heath invokes implicitly at the same logical positions, representing over-citation rather than a different proof path. This is Case A of Q2: same backbone, different citation depth.

### 5.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: constructing equimultiples D, E of A, B and an arbitrary multiple F of C, proving D=E from the equality A=B, applying the three-way size comparison of D/E against F, and invoking Definition 5.5 to conclude first that A:C = B:C and then symmetrically that C:A = C:B. The AI proof explicitly cites CN1 (equals to the same are equal), CN2 (equals added to equals yield equals), and D5.2 (definition of equimultiple), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only common notions and a definition, the difference is purely one of citation depth with the same logical backbone, yielding G.

### 5.8
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: constructing equimultiples FH and K of AB and C via 5.1, showing GH equals K because EB equals C, finding the first multiple N of D exceeding K, proving FH exceeds N, and applying Definition 5.7 to conclude both ratio inequalities. The AI avoids Heath's two-case distinction (AE less than EB vs AE greater than EB) by always multiplying AE, handling the sub-case in Step 7, but this structural difference does not change the logical backbone. The ai_only citations CN2 and CN5 are Common Notions that Heath uses implicitly but the AI cites explicitly, confirming over-citation rather than a path difference. With the same backbone and different citation depth, this is a granularity difference.

### 5.9
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for both cases of the proposition: assume equal ratios, suppose the magnitudes are unequal, invoke 5.8 to derive that the ratios would in fact be unequal, reaching a contradiction. The AI proof explicitly cites definitions D5.5 (equal ratio) and D5.7 (greater ratio) to unpack what 5.8 yields, while Heath leaves these definitions implicit. Since heath_only is empty and ai_only contains only definitions, this is a citation-depth difference with an identical backbone, yielding G.

### 5.10
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided this classification. Both proofs argue through exactly the same key intermediate conclusions using the same reductio ad absurdum structure: for each of the two parts of the proposition, they show the magnitudes are not equal (via 5.7) and that the wrong inequality is impossible (via 5.8), then conclude by exhaustion. The AI proof explicitly cites definitions D5.5 and D5.7 that Heath invokes implicitly, resulting in a pure citation-depth difference with no change to the logical backbone. Since heath_only is empty and ai_only contains only definitions, this is Case A of Q2, yielding Granularity difference.

### 5.11
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: setting up equimultiples G, H, K of A, C, E and L, M, N of B, D, F; deriving the equimultiple trichotomy from each given ratio equality (A:B = C:D and C:D = E:F); chaining the two trichotomies; and concluding A:B = E:F by the definition of same ratio. The only difference is that the AI explicitly cites Definition V.5 (D5.5) at each application of the definition of same ratio, whereas Heath applies the same definition without a formal citation. This is a citation-depth difference with the same logical backbone, placing the proof in Case A of Q2, yielding Granularity difference (G).

### 5.12
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: take equimultiples of the antecedents and consequents, apply D5.5 to establish ordering relationships between individual equimultiples, conclude the same ordering holds for the sums, invoke 5.1 to show those sums are themselves equimultiples of the totals, and finish by D5.5. The AI proof adds two axiom-level over-citations not found in Heath: CN2 (common notion justifying addition of equals in Step 5) and D5.6 (definition of proportional magnitudes in Step 1). Heath uses both facts implicitly without citing them. Since the backbones are identical and the ai_only items are purely axiom-level elaborations, Case A of Q2 holds, yielding G.

### 5.13
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues since both AI citations (D5.5, D5.7) are definitions. Q1 confirmed the AI proof is logically complete: it correctly invokes D5.7 to obtain equimultiples witnessing the greater ratio C:D > E:F, constructs corresponding equimultiples of A and B, applies D5.5 (same ratio definition) to transfer the inequality, and concludes via D5.7. Q2 confirmed both proofs share the same key intermediate conclusions in the same logical order. The citation sets are identical (ai_used = heath_refs = {D5.5, D5.7}) with Jaccard 1.0, yielding a perfect match.

### 5.14
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for the primary case (A > C): establishing A:B > C:B via 5.8, deriving C:D > C:B via 5.13, and concluding D < B via 5.10. The AI's four extra citations (5.7, 5.9, 5.11, D5.5) all arise from explicitly proving the two subsidiary cases (A = C and A < C) that Heath abbreviates with 'Similarly we can prove.' Since heath_only is empty, every citation Heath uses also appears in the AI proof. The difference is purely one of citation depth: the AI spells out the analogous reasoning Heath leaves to the reader, requiring the additional propositions for the equality and less-than cases. This is Case A of Q2, same backbone with different granularity.

### 5.15
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided this classification. Both proofs share the same backbone: decompose the multiples into equal parts, establish that each pair of corresponding parts has the same ratio via 5.7, then apply 5.12 to aggregate one-antecedent-to-one-consequent into all-antecedents-to-all-consequents, and finally substitute back to obtain the desired ratio. The AI proof differs only in citation depth: it explicitly cites 5.11 (transitivity of equal ratios) for substitution steps that Heath performs implicitly, and it explicitly cites definitions D5.1, D5.2, and D5.6 that Heath uses without citation. Since heath_only is empty and all ai_only items (5.11, D5.1, D5.2, D5.6) represent over-citation of supporting lemmas and definitions rather than a different logical path, this is Case A of Q2: same key intermediate conclusions at different citation granularity.

### 5.16
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs establish the identical backbone of key intermediate conclusions: equimultiples E,F of A,B and G,H of C,D are taken; 5.15 gives A:B=E:F and C:D=G:H; 5.11 chains these to get E:F=G:H; 5.14 yields the ordering comparison; and D5.5 delivers the conclusion A:C=B:D. The AI proof adds explicit citations to definitions D5.6 (ratio) and D5.12 (alternate proportion) that Heath invokes implicitly, making ai_only consist entirely of definitions with heath_only empty. This is a straightforward citation-depth difference with identical logical structure, yielding G.

### 5.17
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing equimultiples GH, HK, LM, MN of AE, EB, CF, FD and other equimultiples KO, NP of EB, FD; using 5.1 to show GK and LN are equimultiples of AB and CD; using 5.2 to show HO and MP are equimultiples of EB and FD; applying the given proportion to obtain the excess/equal/less correspondence for GK vs HO and LN vs MP; then subtracting common parts to transfer the correspondence to GH vs KO and LM vs NP; and concluding AE:EB = CF:FD. The ai_only citations (CN2, CN5, D5.14, D5.15, D5.5, D5.6) are exclusively definitions and common notions that Heath uses implicitly without explicit citation, representing over-citation rather than a structural difference. The heath_only set is empty. This is a clear case of the same backbone argued at different citation depth.

### 5.18
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 5.18 by reductio ad absurdum, supposing AB:BE = CD:DG for DG less than FD, then applying 5.17 (componendo implies separando), 5.11 (transitivity of ratios), and 5.14 (ordering preservation) to derive a contradiction. The AI instead constructs a direct proof from D5.5 (the equimultiple definition of proportion), decomposing arbitrary equimultiples of the wholes into sums of equimultiples of the parts via 5.1 and 5.2, then performing exhaustive case analysis on the multiplier relationship to verify the equimultiple condition directly. The two proofs share no citations (Jaccard = 0.0) and their key intermediate conclusions are entirely different: Heath reasons through higher-level proportion theorems in a reductio framework, while the AI works at the definitional level with direct equimultiple arithmetic. Since the AI's chain is logically complete with every step justified, this is a valid different path.

### 5.19
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The forward dependency gate found no issues (all citations 5.11, 5.16, 5.17 precede 5.19). Both proofs follow an identical logical backbone: apply alternation (5.16) to the hypothesis AB:CD = AE:CF, then separando (5.17) to isolate the remainders, then alternation (5.16) again to obtain EB:FD = AE:CF, and finally transitivity (5.11) to conclude EB:FD = AB:CD. The citation sets are exactly equal with Jaccard 1.0, ai_only and heath_only are both empty, and the key intermediate conclusions match at every stage. The perfect match check at Step 6 confirms category P.

### 5.20
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same key intermediate conclusions for the principal case (A > C): establishing A:B > C:B via 5.8, deriving D:E > F:E, and concluding D > F via 5.10. The AI proof is a strict superset of Heath's citations, with heath_only empty. The five ai_only items (5.7, 5.9, 5.11, D5.5, D5.7) are all explicitations of steps Heath leaves implicit: 5.7 for the inversion Heath performs without citation, 5.9 and 5.11 for the equal-magnitudes case Heath covers with 'similarly we can prove,' and D5.5/D5.7 for definitional expansions of ratio comparisons that Heath handles with a single application of 5.13. The backbone is identical across all three cases; the AI simply provides greater citation depth.

### 5.21
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone for the principal case (A > C): establishing A:B > C:B via 5.8, deriving E:F > E:D via 5.13 and the proportion hypotheses, then concluding D > F via 5.10. The AI proof differs only in depth: it explicitly proves all three cases (A > C, A = C, A < C) where Heath says 'similarly we can prove,' and it cites definitions (D5.5, D5.7, D5.13, D5.17, D5.18) and additional propositions (5.7, 5.9, 5.11) needed for the equal and less cases. The AI also works through definition-level arguments rather than relying solely on 5.13 for ratio substitution. Since heath_only is empty and all AI-only citations represent either explicit definitions or propositions for cases Heath handles summarily, this is a granularity difference rather than a path difference.

### 5.22
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone for the three-magnitude case: take equimultiples G,H of A,D; K,L of B,E; M,N of C,F; apply 5.4 twice to get G:K=H:L and K:M=L:N; invoke 5.20 for the ex aequali comparison on equimultiples; then conclude A:C=D:F by Definition 5.5. The AI proof adds an explicit citation to D5.17 (the definition of ex aequali ratio) and an inductive extension to more than three magnitudes (Step 7), neither of which changes the backbone. Since the key intermediate conclusions are identical and the only citation difference is the AI's additional definition reference D5.17, this is Case A of Q2: same backbone, different citation depth, yielding G. The citation sets are not identical (ai_used includes D5.17), so P does not apply.

### 5.23
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided this classification. Both proofs share an identical logical backbone: taking equimultiples G,H,K of A,B,D and L,M,N of C,E,F; using V.15 and V.11 to establish G:H = M:N; using V.16, V.15, and V.11 to derive H:K = C:E then H:K = L:M; alternating to get H:L = K:M; applying V.21 to the resulting perturbed proportion among multiples; and concluding A:C = D:F. The AI cites the same four theorems as Heath (5.11, 5.15, 5.16, 5.21) and additionally cites three definitions (D5.5, D5.17, D5.18) that Heath invokes implicitly without explicit citation. Since the key intermediate conclusions are identical and the only citation differences are definitional over-citations by the AI, this is Case A of Q2: same backbone, different citation depth, yielding G.

### 5.24
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: inverting BG:C = EH:F to C:BG = F:EH, applying ex aequali (5.22) to obtain AB:BG = DE:EH, using componendo (5.18) to get AG:GB = DH:HE, and a final ex aequali (5.22) to reach AG:C = DH:F. The AI proof adds explicit citations for definitions (D5.5, D5.13, D5.14, D5.15, D5.17) and the inversion proposition (5.7) that Heath uses without explicit citation. Since heath_only is empty and all ai_only items are definitions or the inversion result underlying a step Heath performs implicitly, this is a citation-depth difference with the same logical backbone, yielding G.

### 5.25
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: substituting AG=E and CH=F, applying V.19 to obtain GB:HD = AB:CD, deducing GB > HD from AB > CD, noting AG+F = CH+E, and combining these to conclude AB+F > CD+E. The AI proof cites the same key proposition (5.19) as Heath but adds explicit citations for steps Heath performs implicitly: 1.3 for cutting off equal segments, 5.7 and 5.11 for the ratio substitution justifying AB:CD = AG:CH, 5.16 (alternando) and 5.14 for deducing the inequality GB > HD from the proportion, and CN2 and CN5 for combining the final results. Since heath_only is empty and all ai_only items are deeper-level citations for the same logical steps, this is Case A of Q2: same backbone, different citation depth, yielding G.
