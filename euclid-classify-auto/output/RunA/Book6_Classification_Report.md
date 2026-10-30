# Book 6 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 25 | 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 6.8, 6.9, 6.11, 6.12, 6.13, 6.14, 6.16, 6.17, 6.18, 6.19, 6.21, 6.22, 6.24, 6.25, 6.27, 6.28, 6.29, 6.31, 6.33 |
| Path difference (D) | 8 | 6.6, 6.10, 6.15, 6.20, 6.23, 6.26, 6.30, 6.32 |
| AI proof error (E) | 0 |  |

**Total**: 33 propositions

## Per-Proposition Analysis

### 6.1
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing equimultiples of the bases by extending the line, joining the vertex to new points, using I.38 to show triangles on equal bases are equal, applying V.Def.5 to establish BC:CD = triangle ABC:triangle ACD, then using I.41 to relate parallelograms to triangles and chaining the ratios. The ai_only citations (1.3, CN5, P1, P2) are all construction propositions, postulates, and common notions representing over-citation of construction steps that Heath leaves implicit. The heath_only citation (5.11, transitivity of ratios) represents a step that is logically present in both proofs at the same position: the AI actually mentions 5.11 in its Step 12 text but does not formally list it, instead handling the ratio-chaining through 5.15 and D5.5. Since the key intermediate conclusions are identical and the citation differences reflect depth of citation rather than different logical paths, this is a granularity difference.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both the AI and Heath proofs establish the same key intermediate conclusions in both parts of this biconditional proposition: (1) triangles BDE and CDE are equal by I.38, (2) triangle-to-segment ratios via VI.1, (3) ratio equality via V.7, and (4) transitivity via V.11 for the forward direction; and symmetrically for the converse using VI.1, V.11, V.9, and I.39. The only citation difference is that the AI explicitly cites Postulate 1 for joining lines BE and CD, which Heath uses implicitly without citation. Since P1 is a construction postulate and the logical backbone is identical, this is a classic granularity (citation-depth) difference, not a path difference.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided this classification. Both proofs (AI and Heath) establish identical key intermediate conclusions in both directions of this biconditional proposition: in Part I, both construct CE parallel to DA, establish angle equalities via I.29, deduce AE = AC via I.6, then apply VI.2 to get the proportionality; in Part II, both use VI.2, V.11, V.9 to deduce AE = AC, then I.5 and I.29 to establish the angle bisection. The AI's additional citations (1.31, 5.7, CN1, P2, P5) are all over-citations of construction steps, postulates, and common notions that Heath uses implicitly without explicit citation. Since heath_only is empty and ai_only consists entirely of construction/axiom-level references, this is a clear Case A: same backbone, different citation depth.

### 6.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share an identical geometric backbone: placing BC in line with CE, producing BA and ED to meet at F, establishing BF parallel to CD and AC parallel to FE (both via 1.28), forming parallelogram ACDF with AF=CD and AC=FD (via 1.34), and applying 6.2 twice to triangle BFE to extract the base proportions BA:AF=BC:CE and BC:CE=FD:DE. The only divergence is in the final proportion-manipulation stage: Heath uses alternando (5.16) to rearrange ratios and ex aequali (5.22) to derive the third pair BA:AC=CD:DE, while the AI uses transitivity of ratios (5.11) to show BA:CD=BC:CE=AC:DE directly. The ai_only items 1.13 and P2 are over-citations of construction steps that Heath leaves implicit. Since the key intermediate geometric conclusions are the same in both proofs and only the algebraic manipulation technique for the final proportions differs, this is a granularity/depth difference (Case A of Q2), not a path difference.

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the identical backbone: construct an auxiliary triangle equiangular with ABC (Heath on EF, AI on DE), prove proportionality of sides via VI.4, deduce side equalities via V.9, establish congruence with DEF via I.8, and transfer angle equalities back to conclude ABC is equiangular with DEF. The citation differences are purely depth-related: the AI cites CN1 for ratio transitivity where Heath cites V.11, and the AI attributes all angle equalities from congruence directly to I.8 where Heath explicitly invokes I.4 after I.8 to obtain remaining angle equalities. These are citation-depth differences on the same logical backbone, not different proof paths.

### 6.6
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decides the classification. Heath's proof constructs a triangle DGF equiangular to ABC on line DF using I.23, derives via VI.4 that BA:AC = GD:DF, combines with the hypothesis via V.11 to get ED:DF = GD:DF, concludes ED = GD by V.9, then applies I.4 (SAS) to prove DEF congruent to DGF and thereby transfers the angles. The AI proof takes a fundamentally different approach: it constructs points G on DE and H on DF with DG = AB and DH = AC (using I.3), then through a chain of ratio manipulations (5.7, 5.11, 5.16, 5.17) shows the sides DE and DF are cut proportionally at G and H, invokes the converse of 6.2 to establish GH parallel to EF, uses 1.29 for alternate angle equalities, and applies I.4 (SAS) to show triangle ABC congruent to DGH rather than to a separate equiangular construction. The key intermediate conclusions differ: Heath's backbone runs through equiangularity of a constructed triangle and equality of segments (V.9), while the AI's runs through proportional side-cutting, parallelism (6.2), and alternate angles (1.29). Both paths are logically complete and valid, but they establish different intermediate geometric facts, constituting a genuine path difference.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.875
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume angle ABC is not equal to angle DEF, construct an auxiliary triangle equiangular with one given triangle (Heath at point B, AI at point E), derive segment equality via proportionality (VI.4, V.11, V.9), establish an isosceles triangle (I.5), then derive contradictions in both cases (angles less than a right angle, angles not less than a right angle). The only citation difference is that Heath cites I.17 (any two angles of a triangle are less than two right angles) for the Case 2 contradiction, while the AI derives the equivalent result from I.32 (angle sum equals two right angles) by showing that if two angles account for two right angles the third angle would be zero, which is impossible. This is a citation-depth difference: the AI derives inline what Heath cites as a ready-made theorem. The key intermediate conclusions are identical, placing this firmly in Case A of Q2 as a granularity difference.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both the AI and Heath proofs follow the same logical backbone: they establish equiangularity of each sub-triangle (ABD and ACD) with the whole triangle ABC by noting that two angles are equal (one right angle and one common angle) and deducing the third angle equality via I.32 (angle sum), then apply VI.4 for proportionality and VI.Def.1 for similarity, and finally prove the two sub-triangles similar to each other by combining previously established angle equalities. The ai_only set consists entirely of axioms, definitions, and postulates (CN3, D1.10, D1.21, P4) that Heath invokes implicitly but the AI cites explicitly. The heath_only set is empty. This is a pure citation-depth difference with no backbone divergence, confirming Case A of Q2.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct three equal segments along an auxiliary line from one endpoint, draw a parallel through the first division point to the line joining the last division point to the other endpoint, and apply VI.2 to establish a proportion that yields the prescribed 1/n part. The AI proof cites 5.18 (componendo) to formally derive AG:AB = 1:3 from AD1:D1D3 = AG:GB, whereas Heath performs the equivalent ratio reasoning informally without citing a specific proposition. The remaining ai_only items (D5.1, D5.2, D5.5, P1) are definitions and a postulate that Heath leaves implicit. Heath_only is empty. Since the key intermediate conclusions are identical and the citation differences reflect only depth of explicit reference, this is a granularity difference (G).

### 6.10
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification as D (path difference). Heath's proof constructs a line through D parallel to AB, creating parallelograms FH and HB, then uses I.34 (opposite sides of a parallelogram are equal) to establish segment equalities DH=FG and HK=GB, followed by two applications of VI.2 to triangles DKC and AGE. The AI proof takes a fundamentally different geometric approach: it draws DF and EG both parallel to BC (rather than creating a parallelogram), establishes DF parallel to EG via I.30, then applies VI.2 three times (to triangle ABC twice and to triangle AEG), and uses ratio-theoretic machinery from Book 5 (5.18 componendo and 5.22 ex aequali) to derive the required proportions. The AI avoids parallelogram construction entirely, substituting ratio algebra for geometric segment equality. Since the key intermediate conclusions differ -- Heath works through parallelogram side equalities while the AI works through a chain of three proportion applications combined with Book 5 ratio operations -- this is Case B (different backbone). The AI's path is logically valid at Q3, with each step properly justified, so the classification is D.

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: place lines BA, AC at any angle, produce them, set BD equal to AC via I.3, join BC and draw DE parallel to BC via I.31, apply VI.2 to obtain AB:BD = AC:CE, then substitute AC for BD to conclude AB:AC = AC:CE. The AI's extra citations (P1, P2 for construction lines, CN1 for equals substitution, and 5.7 for the formal justification of replacing BD with AC in the proportion) are all over-citations that make explicit what Heath leaves implicit. Heath's proof performs the same substitution step without citing any supporting proposition. Since the key intermediate conclusions are identical and the citation differences reflect only depth of justification, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct triangle DEF with DG=A, GE=B, DH=C, draw EF parallel to GH via I.31, apply VI.2 to obtain DG:GE::DH:HF, then substitute equals to conclude A:B::C:HF. The AI proof cites three additional items (1.3, P1, P2) that Heath leaves implicit, all of which are construction propositions or postulates justifying the explicit construction steps (cutting off equal segments, drawing and joining lines, extending lines). Since heath_only is empty and ai_only consists entirely of construction-level over-citations, the proofs share the same key intermediate conclusions at different citation depths, yielding a granularity difference.

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: they construct a semicircle on AC, draw BD perpendicular to the diameter, and establish two key intermediate conclusions in the same order: (1) angle ADC is a right angle by III.31, and (2) DB is a mean proportional between AB and BC by VI.8. The AI proof cites the same core propositions as Heath (3.31 and 6.8) but additionally cites postulates P1, P2, P3 for construction steps, definitions D1.17 and D1.18 for the semicircle, definition D6.1 for similarity, and proposition 1.11 for the perpendicular construction. These are all foundational items that Heath leaves implicit, representing over-citation rather than a different proof strategy. Heath_only is empty, confirming no substantive steps are missing. This is Case A of Q2: same backbone, different citation depth.

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.556
**Analysis**: Q2 decides: both proofs follow the same backbone. They place the equal and equiangular parallelograms with equal angles adjacent, complete a third reference parallelogram (Heath calls it FE, the AI constructs BCHF), then use VI.1 to express area ratios as side ratios, V.7 to exploit the equality of the original parallelograms, V.11 for transitivity, and V.9 for the converse direction. The AI's four extra citations (1.13, 1.30, 1.31, 5.16) all make explicit construction or algebraic steps that Heath leaves implicit: 1.31 for constructing the reference parallelogram, 1.13 and 1.30 for establishing collinearity of sides, and 5.16 for alternation of the proportion. Since heath_only is empty and the ai_only items are all over-citations of construction and supplementary steps with no change to the logical backbone, this is Case A of Q2, a granularity difference.

### 6.15
**Category**: Path difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. The AI proof uses a different auxiliary construction from Heath: it joins BE to create intermediate triangle ABE, whereas Heath joins BD to create intermediate triangle BAD. This leads to different key intermediate conclusions: the AI establishes ratios ABC:ABE = CA:AE and ABE:ADE = BA:AD via VI.1, then uses alternando (V.16) to rearrange to the desired reciprocal proportion CA:AD = AE:BA, while Heath establishes CAB:BAD = CA:AD and EAD:BAD = EA:AB via VI.1, obtaining the result directly through transitivity of ratios (V.11). The different auxiliary line produces genuinely different intermediate geometric facts, not merely a difference in citation depth. The AI's path is logically valid throughout both directions of the biconditional, correctly applying V.16 where Heath uses V.11, and V.7/V.9 as Heath does. This constitutes a genuine path difference (D).

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: construct two equiangular parallelograms (rectangles) representing the rectangles of the extremes and means, establish that the sides about the equal angles are reciprocally proportional, and apply 6.14 to conclude equality of the parallelograms (and hence the rectangles). The converse direction is handled identically in both proofs by reversing the application of 6.14. The ai_only set consists entirely of construction propositions (1.3, 1.11, 1.31), postulates (P1, P4), and a definition (D2.1) that Heath uses implicitly but does not cite. The heath_only set is empty. This is a classic case of the AI over-citing foundational construction steps that Heath leaves tacit, with no difference in the logical backbone.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: converting the three-line proportion into a four-line proportion context and applying 6.16 in both the forward and converse directions. Heath introduces an explicit auxiliary line D equal to B to set up the four-line proportion, while the AI directly observes that A, B, B, C constitute four proportional lines without needing an auxiliary construction. The key intermediate conclusions are identical in both proofs. The ai_only set consists entirely of definitions (D1.22, D2.1, D5.6, D5.8) that the AI cites explicitly where Heath leaves them implicit, and heath_only is empty. This is a classic Case A same-backbone-different-depth scenario.

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the identical backbone: decompose the given rectilineal figure into triangles by joining diagonals, construct equiangular counterpart triangles on the given line using I.23, show remaining angles equal by I.32, establish proportional sides by VI.4, chain the proportional ratios to show all corresponding sides are in the same ratio, show all corresponding angles equal by construction and addition, and conclude similarity by VI. Def. 1. The AI proof generalizes to a pentagon while Heath uses a quadrilateral, but the method is the same iterative triangle-matching procedure. The ai_only citations (5.11, CN2, P1) are all over-citations of basic infrastructure: 5.11 for ratio transitivity that Heath uses implicitly when chaining proportions, CN2 for adding angles that Heath performs without naming the common notion, and P1 for joining diagonals. The heath_only set is empty, confirming that every substantive citation in Heath also appears in the AI proof. This is Case A of Q2: same backbone, different citation depth.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: constructing a third proportional BG to BC and EF via 6.11, establishing that AB:DE = EF:BG via transitivity (5.11), proving triangle ABG equals triangle DEF via reciprocally proportional sides about equal angles (6.15), using 6.1 to relate triangle ABC : triangle ABG to the base ratio BC:BG, and concluding that triangle ABC has to triangle DEF the duplicate ratio of BC:EF via D5.9. The citation differences are purely granularity: the AI cites 6.4 (equiangular triangles have proportional sides) to obtain AB:DE = BC:EF directly, whereas Heath derives this same proportion by applying 5.16 (alternation) to the given ratio AB:BC = DE:EF. The proof-tree containment test confirms that 5.16 appears inside Heath's proof of 6.4, so the AI is citing at a higher level while Heath re-derives the internals inline. The AI also explicitly cites 5.7 (equal magnitudes have the same ratio) for the substitution of equal triangles ABG and DEF, which Heath performs without explicit citation, and cites D6.1 (definition of similar figures) where Heath cites D5.11 (definition of corresponding magnitudes). These are all citation-depth differences with identical key intermediate conclusions.

### 6.20
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs establish that similar polygons decompose into similar triangles in the same ratio, but they use genuinely different logical backbones. Heath triangulates from vertex E (diagonals BE, EC) and establishes the ratio part through an elaborate sub-triangle argument using I.32 (angle sums), VI.1 (triangles as their bases), and VI.4 (equiangular triangles have proportional sides), constructing additional diagonals AC and FH to create intermediate points M and N. The AI triangulates from vertex A (diagonals AC, AD) and takes a more direct path for the ratio argument: it applies 6.19 directly to each pair of similar triangles to obtain duplicate ratios, observes these duplicate ratios are all equal because the polygon side ratios are equal, and sums them via 5.12. The heath_only citations (1.32, 6.1, 6.4) are not subsumed by any AI-cited proposition — they reflect genuinely different intermediate steps, not mere citation depth differences. The AI's different path is logically complete and valid, with each step properly justified.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: unpack the similarity of A and B to C via Definition 6.1 (equiangular with proportional sides), then conclude A is similar to B. Heath compresses the final inference into a single 'therefore' step, while the AI proof explicitly cites CN1 for transitivity of angle equality and uses Propositions 5.16 (inverse ratios) and 5.22 (ex aequali) to rigorously derive the proportionality of sides between A and B. The ai_only set {5.16, 5.22, CN1} consists entirely of ratio machinery and a common notion that flesh out steps Heath handles implicitly. The heath_only set is empty. This is a clear Case A in Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 6.22
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone in both parts: the forward direction constructs third proportionals via 6.11, applies ex aequali (5.22) to obtain a key ratio, invokes the duplicate-ratio property of similar figures, and chains ratios via 5.11; the converse constructs a fourth proportional (6.12), builds a similar figure (6.18), applies the forward direction, then uses 5.11 and 5.9. The only citation differences are that the AI cites 6.20 (similar polygons are in duplicate ratio of corresponding sides) where Heath cites 6.19 (similar triangles are in duplicate ratio), and the AI explicitly cites D5.9 (definition of duplicate ratio) which Heath uses implicitly. Since 6.19 appears inside Heath's proof of 6.20, the proof-tree containment test confirms the AI is citing 6.20 as a higher-level unit while Heath uses its sub-result 6.19 directly, making this a citation-depth difference rather than a path difference. D5.9 is a definition and represents over-citation. The key intermediate conclusions are identical in both proofs.

### 6.23
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 determined the classification. Both proofs share the initial setup (placing parallelograms so BC is collinear with CG, proving DC collinear with CE, completing an intermediate parallelogram) and both apply 6.1 twice to establish the ratios of the parallelograms to the intermediate parallelogram in terms of the ratios of their sides. However, the mechanism for combining these ratios into the compounded ratio differs fundamentally. Heath constructs explicit auxiliary magnitudes K, L, M via 6.12 (fourth proportional), uses 5.11 (transitivity of ratio equality) to link these to the parallelogram ratios, and applies ex aequali to conclude. The AI bypasses this entire apparatus by directly invoking D6.5 (definition of compounded ratio) with the intermediate parallelogram DCGK as the linking magnitude, concluding immediately that ABCD:CEFG is compounded of the two side-ratios. The AI also provides more explicit detail for the collinearity argument (citing 1.13, 1.14) and the construction (citing 1.31), which Heath leaves implicit. Since the key intermediate conclusions about the auxiliary magnitudes K, L, M and the ex aequali step form the backbone of Heath's proof but are entirely absent from the AI proof, which follows a logically valid but structurally different path, this is a genuine path difference.

### 6.24
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) establishing equiangularity of the sub-parallelogram with the whole, (2) establishing proportionality of sides about equal angles, (3) concluding similarity by D6.1, and (4) using 6.21 for mutual similarity. The critical difference is citation depth. The AI cites 6.4 (equiangular triangles have proportional sides) to obtain all proportional relationships directly from equiangular sub-triangles, while Heath re-derives the internals of 6.4 inline using 6.2 (proportional intercepts), 5.16 (alternately), 5.18 (componendo), and 5.22 (ex aequali). The proof-tree containment test confirms that three of the four heath_only items (6.2, 5.16, 5.22) appear inside Heath's own proof of 6.4, indicating the AI cites 6.4 as a unit while Heath unpacks its internals. The remaining heath_only item 5.18 (componendo) is avoided by the AI because 6.4 applied to appropriate sub-triangles gives the proportionality of sides about common angles directly, without needing the ratio manipulation step. The AI's additional citations (1.29, 1.32, 1.34, CN1) are foundational angle and parallelogram theorems used to set up the equiangular triangles, consistent with over-citation at a finer granularity level.

### 6.25
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone: construct parallelograms BE equal to ABC and CM equal to D, take GH as a mean proportional to BC and CF, construct KGH similar to ABC on GH, establish that the ratio of the parallelogram areas equals the ratio of the similar figures via the duplicate ratio property, and conclude by the equality chain that KGH equals D. The citation differences are all citation-depth variations: the AI cites 6.20 (similar polygons in duplicate ratio) where Heath cites 6.19 (similar triangles in duplicate ratio), and 6.19 appears inside Heath's proof of 6.20, satisfying the proof-tree containment test. Similarly, the AI cites 1.45 for both parallelogram constructions where Heath distinguishes 1.44 and 1.45, and 1.44 is used inside the proof of 1.45. The AI's use of 5.11 and 5.14 instead of Heath's 5.16 represents a minor algebraic variation in ratio manipulation (transitivity plus equal-ratios-imply-equality vs alternando) that achieves the same proportional conclusion. The additional AI citations of 1.14, 1.29, CN1, and D5.9 are over-citations of construction details, common notions, and definitions that Heath leaves implicit.

### 6.26
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Both proofs are by contradiction: they assume the smaller parallelogram is not about the same diameter as the whole, construct a parallelogram about the diameter using I.31, and apply VI.24 to establish similarity. However, the mechanism for deriving the contradiction differs substantially. Heath uses the proportionality DA:AB = GA:AK (from VI.24) and DA:AB = GA:AE (from similarity of the given parallelograms), then via V.11 gets GA:AK = GA:AE, and by V.9 concludes AE = AK, which is impossible. The AI instead uses VI.21 (transitive similarity) to conclude AEFG is similar to AKHL, then employs an elaborate argument using D6.1 for proportional sides, V.16 (alternando), and VI.2 (parallel lines cutting triangle sides proportionally) to show that vertex F must lie on the diagonal AC, contradicting the assumption. Since the key intermediate conclusions and the contradiction mechanism are different (V.9-based magnitude equality vs. VI.2-based positional argument), and the AI's path is logically valid throughout, this is classified as a path difference (D).

### 6.27
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect AB at C, use 6.26 to establish that the similar deficient parallelograms are about the same diagonal, and use 1.43 to identify equal complements about that diagonal. The difference lies in how each proof concludes the inequality. Heath uses 1.36 (parallelograms on equal bases in same parallels are equal) to establish CH = CG from AC = CB, then derives the gnomon relationship to show AD > AF. The AI omits 1.36 and instead argues more directly from the geometric containment of KF within CF (since KF is similar to CF but on a shorter base), concluding CE > AF by CN5 (whole greater than part). The ai_only item CN5 is a common notion that Heath uses implicitly, and the heath_only item 1.36 is an intermediate step the AI compresses away through its containment argument. These represent different levels of citation depth on the same backbone, not a fundamentally different proof path.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: bisect AB, construct a similar parallelogram EBFG on the half, handle two cases (C equals EBFG, or C is less), construct the excess parallelogram similar to D, show it is about the same diameter as EBFG via VI.21 and VI.26, establish that the gnomon equals C, and then use area equalities to show the applied parallelogram TS equals C. The AI proof cites many additional construction-level propositions (1.10, 1.3, 1.31, P1) and axioms (CN3) that Heath leaves implicit, which are standard over-citations. The substantive citation difference is that the AI uses 1.43 (complements about the diameter are equal) where Heath uses 1.36 (parallelograms on equal bases in same parallels are equal) to establish the same area equality leading to TS = gnomon = C. The AI also cites 6.24 and 6.27 which Heath omits, but these support the same conclusions Heath reaches by other means. Since the key intermediate conclusions are identical and only the citation granularity differs, this is a granularity difference.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same backbone: bisect AB at E, construct a parallelogram on EB similar to D, use VI.25 to build a larger parallelogram equal to the first plus C and similar to D, show the two parallelograms are about the same diameter via VI.26, demonstrate the gnomon equals C, and conclude the applied parallelogram equals C with the excess similar to D via VI.24. The AI's eight ai_only citations (1.10, 6.18, 6.22, CN3, CN5, D6.1, P1, P2) are all construction propositions, common notions, definitions, or postulates that provide finer granularity to steps Heath treats as self-evident. The single heath_only citation (1.36, parallelograms on equal bases in same parallels are equal) is used at the same logical position in both proofs — Heath cites it explicitly to show AN = NB, while the AI makes the same argument more tersely without the explicit citation. This is a citation-depth difference at the same backbone, not a structural divergence.

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs a square on AB, applies a parallelogram equal to it exceeding by a similar figure (6.29), then uses reciprocal proportionality of equiangular parallelograms (6.14) to derive BA:AE = AE:EB. The AI takes an entirely different path: it uses 2.11 to cut AB so that rect(AB,BC) = sq(AC), then applies the converse of 6.17 to convert this rectangle-equals-square relation into the proportion AB:AC = AC:BC, and invokes D6.3 to conclude the extreme and mean ratio. The Jaccard similarity is 0.0 with completely disjoint citation sets, and the proof-tree containment test confirms the AI citations (2.11, 6.17) do not appear inside Heath's cited propositions (6.29, 6.14). Both proofs are logically complete but argue through fundamentally different intermediate conclusions, making this a genuine path difference.

### 6.31
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: drawing the perpendicular AD from the right angle to BC, establishing similarity of sub-triangles ABD and ACD to the whole triangle ABC via 6.8, deriving the proportional relationships CB:BA = BA:BD and BC:CA = CA:CD, connecting these to the ratios of similar figures on the sides, and concluding via BD+DC=BC that the figure on BC equals the sum of the figures on BA and AC. The key citation difference is that Heath uses 6.19 (similar triangles are in duplicate ratio of corresponding sides) to establish the figure-ratio step, while the AI uses 6.20 (similar polygons in duplicate ratio of corresponding sides) along with explicit Book V ratio manipulations (D5.9, 5.24, 5.9). The proof-tree containment test confirms that 6.19 appears explicitly within Heath's proof of 6.20, so the AI is citing the higher-level result as a unit while Heath uses the more specific sub-result directly. The remaining ai_only items (1.12 for the perpendicular construction, D5.9 for the duplicate ratio definition, 5.24 for ratio addition, 5.9 for ratio equality) represent over-citation of construction steps and ratio arithmetic that Heath leaves implicit.

### 6.32
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: The AI proof takes a fundamentally different geometric approach from Heath's proof. Heath establishes angle equalities via I.29, uses VI.6 to show the triangles are equiangular, then combines angle sums with I.32 and applies I.14 (adjacent angles equal to two right angles imply collinearity). The AI instead introduces an auxiliary intersection point G where line AE crosses line BD, establishes equiangularity of triangles ABG and EDG via I.29, I.15, and I.32, uses 6.4 for proportional sides, then applies ratio manipulation (5.17/5.9) to show G coincides with C, concluding collinearity. The key intermediate conclusions are entirely different: Heath argues through angle sums at vertex C, while the AI argues through proportional segments and point coincidence. Q2 Case B applies (different backbone). Under Q3, the AI's chain is logically complete despite misciting 5.17 where 5.18 is needed — under the lenience rule, the mathematical inference is sound (informal but sound), so this is NOT-E. Classification is D (path difference).
**Audit Record**: CANDIDATE E — 6.32
  violated_claim : "by 5.17 (composition of a ratio) we obtain (BG + GD)/GD = (BC + CD)/CD"
  failure_mode   : invalid_inference
  missing_is     : expansion — the correct proposition 5.18 would justify this step; it is a citation number error, not a logical gap
  evidence       : AI Step 8 cites 5.17 for going from BG/GD = BC/CD to (BG+GD)/GD = (BC+CD)/CD, but 5.17 is separando (componendo to separando), not componendo (separando to componendo, which is 5.18)
  why_not_terse  : This is a miscitation of proposition number, not a logical gap. The mathematical step is sound via 5.18.
VERDICT: NOT-E — missing_is = expansion; the inference is mathematically sound, just incorrectly numbered. Reclassified as D.

### 6.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow identical logical backbones: constructing equimultiple arcs and corresponding central angles, applying the Eudoxian definition of proportion (V. Def. 5 / D5.5) via the equimultiple comparison, and then extending the ratio to inscribed angles using the central-angle-is-double-inscribed-angle relationship. The AI proof cites exactly the same propositions as Heath (3.27 and D5.5) plus six additional references (3.20, 5.15, CN2, D3.1, P1, P3) that Heath leaves implicit. Among these, P1 and P3 are construction postulates, CN2 is a common notion, and D3.1 is a definition, all representing standard over-citation. The substantive additions 3.20 (inscribed angle theorem, which Heath invokes implicitly as 'they are doubles respectively') and 5.15 (halves in same ratio) make explicit what Heath states without citation. With heath_only empty and all ai_only items corresponding to the same underlying reasoning at finer granularity, this is a clear Case A same-backbone-different-depth scenario.
