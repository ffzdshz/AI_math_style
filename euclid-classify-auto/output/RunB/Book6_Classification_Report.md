# Book 6 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 27 | 6.1, 6.2, 6.3, 6.5, 6.7, 6.8, 6.9, 6.11, 6.12, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18, 6.19, 6.21, 6.22, 6.24, 6.25, 6.26, 6.27, 6.28, 6.29, 6.31, 6.32, 6.33 |
| Path difference (D) | 6 | 6.4, 6.6, 6.10, 6.20, 6.23, 6.30 |
| AI proof error (E) | 0 |  |

**Total**: 33 propositions

## Per-Proposition Analysis

### 6.1
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: construct equimultiples of bases and triangles, use I.38 to show the equimultiple relationship preserves between bases and triangles, apply V. Def. 5 to conclude the proportion for triangles, then extend to parallelograms via I.41 and V.15. The ai_only set {1.3, 1.39, CN2, P1, P2} consists entirely of construction propositions, postulates, and common notions reflecting the AI's more detailed citation of constructive steps. The heath_only set {5.11} reflects Heath's explicit citation of ratio transitivity, which the AI handles implicitly by chaining equalities in Step 10 without a separate citation. Since the key intermediate conclusions are identical and all citation differences are matters of depth rather than substance, this is a granularity difference.

### 6.2
**Category**: Granularity difference
**Jaccard**: 0.625
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: in Part I, they establish the equality of triangles BDE and CDE (via same base DE between same parallels), derive triangle-to-triangle ratios using VI.1, and conclude proportionality via V.11; in Part II, they reverse the argument using V.9 and I.39. The only citation difference is that the AI cites I.37 (triangles on the same base in the same parallels are equal) where Heath cites I.38 (triangles on equal bases in the same parallels are equal). Since triangles BDE and CDE share the literally same base DE, both propositions apply and establish the identical geometric fact. The AI also adds the construction postulate P1 for joining lines, which is an over-citation. These are citation-depth differences with identical key intermediate conclusions, yielding G.

### 6.3
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs establish the angle bisector proportion theorem and its converse through identical key intermediate conclusions: constructing CE parallel to DA, establishing angle equalities via I.29, deriving that AE equals AC via the isosceles triangle theorem (I.6 forward, I.5 converse), applying proportionality with parallel lines (VI.2), and using ratio properties (V.11, V.9) for the converse. The AI's additional citations (1.31 for parallel construction, P2 for line extension, CN1 for transitivity of equality, and 5.7 for substituting equal magnitudes in a ratio) are all explicit statements of construction steps and axioms that Heath applies implicitly. The heath_only set is empty, confirming this is pure over-citation by the AI. Since the logical backbones are the same and the citation differences reflect only depth of explicit justification, this is a granularity difference.

### 6.4
**Category**: Path difference
**Jaccard**: 0.182
**Analysis**: Q2 determines the classification. Heath constructs a parallelogram by placing BC in line with CE, extending BA and ED to meet at F, establishing FACD as a parallelogram (using I.17, Post.5, I.28, I.34), then derives proportions via VI.2 with alternation (V.16) and ex aequali (V.22). The AI uses a fundamentally different superposition approach: it places triangle DEF onto ABC twice (once at vertex B, once at vertex A), each time establishing a parallel line via I.28, applying VI.2 for proportional segments, then using componendo (5.18) with ratio definitions (D5.13, D5.5) to obtain the desired ratios, and finally combining results via ratio transitivity (5.11). The key intermediate conclusions differ entirely: Heath's backbone runs through parallelogram construction and properties (I.34) with alternation and ex aequali, while the AI's backbone runs through double superposition with componendo and transitivity. Both paths are logically complete and valid, yielding a path difference (D).

### 6.5
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow identical backbones: construct triangle GEF on EF equiangular with ABC (I.23, I.32), use VI.4 for proportionality, then V.11 and V.9 to show DE=GE and DF=GF, and finally SSS congruence to conclude DEF is congruent to GEF and transfer angles. The only citation difference is that Heath uses I.4 alongside I.8 to establish full triangle congruence (I.8 for one angle from three equal sides, then I.4 for the remaining angles and triangle equality), while the AI attributes full SSS congruence to I.8 alone. This is a citation depth difference: the same geometric conclusion (full congruence of DEF and GEF with all corresponding angles equal) appears at the same logical position in both proofs, but the AI compresses the two-step I.8+I.4 inference into a single citation of I.8.

### 6.6
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Heath's proof constructs a triangle DGF equiangular with ABC by copying angles (I.23), then uses VI.4 to derive a proportion, and V.11/V.9 to show ED = DG, leading to congruence of DEF and DGF via I.4. The AI instead constructs a triangle DGH congruent to ABC by marking off equal segments on DE and DF (I.3), then uses the converse of 6.2 to show GH is parallel to EF from the proportional cutting, and I.29 to transfer alternate angles. These are fundamentally different backbones: Heath works through angle-copying, proportional similarity (VI.4), and proportion algebra (V.11, V.9), while the AI works through side-copying, proportional cutting (6.2 converse), and parallel-line angle transfer (I.29). Both paths are logically complete and valid, yielding classification D.

### 6.7
**Category**: Granularity difference
**Jaccard**: 0.778
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: assume angle ABC is not equal to angle DEF, construct angle ABG equal to DEF via I.23, show triangles ABG and DEF are equiangular via I.32, derive the proportion AB:BG = DE:EF via VI.4, conclude BG = BC via V.11 and V.9, establish the isosceles triangle via I.5, and reach contradictions in both the less-than-right-angle and not-less-than-right-angle cases. The citation difference is purely one of depth: Heath cites I.17 directly for the Case 2 contradiction (two angles in a triangle are less than two right angles), while the AI derives the same contradiction by working through the angle sums using I.32 and I.13, which are the constituent parts of I.17. The AI additionally cites Postulate 5 to justify that ray BG meets line AC, which is an explicit construction detail Heath leaves implicit. Since the key intermediate conclusions are identical and the differences are limited to citation depth, this is a granularity difference.

### 6.8
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: they establish equiangularity of sub-triangles ABD and ADC with the whole triangle ABC using I.32 (angle sum), then derive proportionality of sides via VI.4 and similarity via VI.Def.1, and finally prove mutual similarity of ABD and ADC. The AI proof is more explicit than Heath in two respects: it fully works out the ADC case where Heath says 'similarly we can prove,' and it explicitly cites foundational items (CN1 for transitivity of equality, CN3 for subtraction of equals, D1.10 for the definition of a right angle, and P4 for right angle equality) that Heath uses implicitly. The ai_only set consists entirely of common notions, definitions, and a postulate, which are classic over-citations indicating a granularity difference rather than a path difference. Heath_only is empty, confirming the AI covers all of Heath's reasoning.

### 6.9
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a line AC at an angle from A with three equal segments AD=DE=EC, draw a parallel to BC through D, apply VI.2 (6.2) to obtain the proportionality, then use the 2:1 ratio of CD to DA to conclude that the prescribed third part has been cut off. The AI proof cites the same three substantive propositions as Heath (1.3, 1.31, 6.2) and adds only axiom-level items (CN1, CN2, D5.1, P1) that make explicit what Heath leaves implicit. With heath_only empty and ai_only consisting entirely of common notions, a definition, and a postulate, this is a clear case of over-citation at the same backbone, yielding a granularity difference.

### 6.10
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 determined this classification. Heath's proof constructs a parallelogram by drawing DHK parallel to AB through D, then uses I.34 to establish segment equalities (DH=FG, HK=GB) before applying VI.2 to triangles DKC and AGE. The AI proof takes a fundamentally different approach: it draws only lines parallel to BC (no parallelogram construction), applies VI.2 to triangles AEG and ABC, then uses ratio algebra (5.18 componendo, 5.16 alternando, and CN1 transitivity) to derive the required proportionalities. The key intermediate conclusions differ substantially -- Heath relies on parallelogram equalities while the AI relies on ratio manipulation chains. The AI's path is logically complete and valid, with each step properly justified, so Q3 confirms a valid path difference (D).

### 6.11
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct BD equal to AC, join BC, draw DE parallel to BC, apply VI.2 to obtain AB:BD = AC:CE, then substitute BD = AC to conclude AB:AC = AC:CE. The AI makes the substitution step more explicit by citing 5.7 (equal magnitudes have the same ratio) and 5.11 (transitivity of ratios), whereas Heath performs this substitution informally in a single sentence. The ai_only items P1 and P2 are postulates cited for construction steps (over-citation). Since heath_only is empty and the ai_only items all represent deeper citation of the same reasoning steps rather than a different proof path, this is Case A of Q2: same backbone, different citation depth.

### 6.12
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct lines DE, DF at an angle, mark DG=A, GE=B, DH=C, join GH, draw EF parallel to GH through E (via I.31), apply VI.2/6.2 to conclude DG:GE::DH:HF, then substitute to get A:B::C:HF. The AI's three extra citations (1.3, P1, P2) are all construction-level references and postulates that make explicit the tools used for setting out lines and cutting off equal segments, which Heath leaves implicit. With heath_only empty and ai_only containing only construction/postulate items, this is a clear Case A in Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 6.13
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: place the two lines AB, BC in a straight line, describe a semicircle on AC, draw BD perpendicular to AC, then conclude that angle ADC is right by III.31 and that BD is a mean proportional between AB and BC by VI.8. The AI proof is more explicit in its construction steps (citing 1.10 for bisection, 1.11 for perpendicular construction, P1/P2/P3 for postulates, D1.18 for semicircle definition) and expands the final proportionality step by explicitly citing 6.4 for the proportionality of sides in similar triangles. The proof-tree containment test confirms that 6.4 appears inside Heath's proof of 6.8, so the AI is merely unpacking what Heath cites as a single unit. The heath_only set is empty, meaning Heath cites nothing that the AI does not also cite. All ai_only items are construction propositions, postulates, a definition, or a proposition contained within a cited result, confirming a citation-depth difference rather than a path difference.

### 6.14
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: arranging the equiangular parallelograms so that sides are collinear, completing an auxiliary parallelogram, using VI.1/6.1 to express area ratios as base ratios, applying V.7/5.7 for equal areas having the same ratio to a third magnitude, and using V.11/5.11 for transitivity of ratios, with the converse using V.9/5.9 to conclude equality from equal ratios to the same magnitude. The ai_only set consists entirely of construction and foundational propositions (1.13, 1.30, 1.31, 1.34) and common notions (CN1, CN2) that Heath leaves implicit. For instance, Heath simply states 'let the parallelogram FE be completed' without citing 1.31 or 1.34, and notes collinearity citing only I.14 while the AI explicitly invokes I.13 and I.30 for the supplementary angle and parallel-line arguments. The heath_only set is empty, confirming the AI cites a strict superset of Heath's references. This is a clear Case A: same backbone, different citation depth.

### 6.15
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same logical backbone: arrange the two equal triangles so that CA is collinear with AD and EA is collinear with AB, join BD, use VI.1 to establish ratio relationships between the triangles and their sides, then combine these ratios to reach the conclusion (forward direction: reciprocal proportionality; converse: equality via V.9). The citation differences are purely about depth of justification for identical logical steps. The AI over-cites by including 1.13 (supplementary angles) to explicitly justify the collinearity before applying 1.14, where Heath simply invokes I.14 directly. For the ratio-combining step, Heath uses V.11 (transitivity of ratios) while the AI uses V.7 (equal magnitudes have the same ratio to the same) with informal inversion, but both reach the same intermediate conclusion at the same logical position. Neither 5.11 nor 5.7 contains the other in its proof tree, but both serve the identical role of combining established ratio equalities, making this a citation-depth difference rather than a path difference.

### 6.16
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification as G (Granularity difference). Both Heath and the AI prove the biconditional in two parts using the same logical backbone: construct equiangular parallelograms (rectangles) whose sides equal the given lines, establish that the sides about equal angles are reciprocally proportional from the hypothesis, then apply 6.14 to conclude equality of the parallelograms (forward direction) or reciprocal proportionality of sides (converse direction). The ai_only set consists entirely of construction propositions (1.11 for right angles, 1.31 for parallel lines), a definition (D2.1), and postulates (P1, P4) that Heath leaves implicit. Heath cites only 6.14, which the AI also cites. The empty heath_only set confirms no substantive step is missing from the AI proof. This is a clear Case A in Q2: same backbone, different citation depth.

### 6.17
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they reduce the three-line proportion to four proportional lines, apply 6.16 to equate the rectangle of the extremes with the rectangle of the means, then identify the rectangle of the means with the square on the middle line. The only difference is that the AI explicitly cites definitions D1.22 and D2.1 to justify that rect(B,B) = sq(B), whereas Heath leaves this step implicit (noting 'the rectangle B, D is the square on B, for B is equal to D' without citing definitions). The AI also skips Heath's formal construction of an auxiliary line D = B, instead directly treating B, B as both means, which is a presentational variation rather than a structural divergence. Since the key intermediate conclusions are the same and the ai_only items are purely definitional over-citations, this is a same-backbone, different-depth case yielding Granularity difference (G).

### 6.18
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decides the classification as G (granularity difference). Both proofs follow the same logical backbone: decompose the given rectilineal figure into triangles by joining diagonals, construct corresponding equiangular triangles on the given line segment using I.23 and I.32, establish proportionality of sides via VI.4, show composite angles are equal by angle addition, chain the proportions to cover all corresponding sides, and conclude similarity by VI. Def. 1. The AI uses a pentagon (3 triangles) where Heath uses a quadrilateral (2 triangles), but this is a difference in illustrative complexity, not logical method. The ai_only citations (P1, CN2, 5.22) reflect over-citation: P1 is a postulate for joining diagonals, CN2 makes explicit the angle addition Heath uses implicitly, and 5.22 (ex aequali) explicitly chains proportions across three triangle pairs where Heath's simpler two-triangle decomposition chains them through a directly shared ratio. Heath_only is empty, confirming the AI covers all of Heath's cited ground. The key intermediate conclusions are the same in both proofs, just expressed at different levels of citation granularity.

### 6.19
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decides the classification as G (Granularity difference). Both proofs share the same logical backbone: construct BG as third proportional to BC and EF via 6.11, establish that AB:DE = EF:BG through ratio manipulation, conclude triangle ABG equals triangle DEF via 6.15 (reciprocal proportionality), relate triangle ABC to triangle ABG via 6.1 (same height), substitute DEF for ABG, and apply the duplicate ratio definition D5.9. The citation differences are all depth-related: the AI cites 6.4 directly to establish proportional sides in similar triangles, while Heath derives the same proportion inline using the similarity condition plus alternando (5.16) — and 5.16 appears inside Heath's own proof of 6.4, satisfying the proof-tree containment test. The AI's additional citations of 5.7 (for substitution of equal magnitudes in ratio), CN1, and D6.1 are over-citations of axiom/definition-level steps that Heath performs without explicit citation. Heath's additional D5.11 (definition of corresponding magnitudes) is similarly a definition-level difference. Since all key intermediate conclusions match and all citation differences reduce to depth rather than substance, this is a granularity difference.

### 6.20
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: The classification is decided at Q2/Q3. While both proofs share the same backbone for Part 1 (decomposing similar polygons into similar triangles via 6.6 with angle subtraction), they diverge significantly in Part 2 (establishing that the component triangles are in the same ratio as the whole polygons). Heath constructs auxiliary diagonals AC and FH, uses 1.32 to show auxiliary triangles are equiangular, applies 6.1 to relate triangle areas to their bases, and chains ratios via 5.22 (ex aequali). The AI takes a genuinely different path: it observes that adjacent pairs of similar triangles share a common side (BE/GL or EC/LH), applies 6.19 directly to obtain duplicate ratios of those shared sides, then uses 5.11 (ratio transitivity) to chain the equal ratios. The heath_only citations 1.32, 5.22, and 6.1 are not merely subsumed by an AI-cited higher-level proposition (only 6.1 appears inside 6.19's proof tree, but 1.32 and 5.22 do not), confirming this is a backbone-level divergence rather than a depth difference. The AI's alternative path is logically complete and valid, so Q3 yields D.

### 6.21
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish that A is similar to C and B is similar to C (unpacking the definition D6.1 to get equiangularity and proportional sides), then conclude that A must be similar to B. Heath treats the transitivity of angle equality and side proportionality as self-evident, citing only D6.1. The AI proof provides the same key intermediate conclusions but explicitly justifies the transitivity steps: CN1 for angle equality, and 5.16 (alternando) plus 5.22 (ex aequali) for chaining the side proportions, with 5.11 also mentioned for ratio transitivity. All four ai_only citations (5.11, 5.16, 5.22, CN1) are additional granularity filling in steps that Heath leaves implicit, not a different proof path. Since heath_only is empty, there is no missing content from the AI side. This is Case A of Q2: same backbone, different citation depth.

### 6.22
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided this as Granularity (G). Both proofs share the same logical backbone for both directions: in the forward direction, both find third proportionals, express figure ratios via duplicate ratios, apply ex aequali (5.22), and conclude via transitivity (5.11). In the converse, both construct a line via 6.12, describe a similar figure via 6.18, apply the forward direction, use 5.9 to conclude equality of figures, and derive equality of lines. The sole heath_only citation 6.19 (similar triangles in duplicate ratio of sides) is contained within Heath's proof of 6.20 (similar polygons in duplicate ratio of sides), which the AI cites instead. This passes the proof-tree containment test: 6.19 appears explicitly inside the proof of 6.20, so the AI cites 6.20 as a unit while Heath uses the triangle-specific 6.19. The ai_only items D5.9 and D6.1 are definitions (over-citation), and 5.8 provides extra explicitness in the converse about why equal similar figures imply equal sides, where Heath simply asserts this. All differences are citation-depth, not backbone.

### 6.23
**Category**: Path difference
**Jaccard**: 0.091
**Analysis**: Q2 determined the classification. Both proofs share the initial setup of placing equiangular parallelograms with collinear sides and completing an intermediate parallelogram, and both use VI.1 twice to establish that the ratios of adjacent parallelograms equal the ratios of the corresponding sides. However, the backbone diverges significantly in how the compound ratio is established. Heath introduces auxiliary magnitudes K, L, M via VI.12 (fourth proportional), transfers the parallelogram ratios to K:L and L:M using V.11, then applies ex aequali to the K:L:M sequence to reach the conclusion. The AI bypasses this entire auxiliary construction, instead directly applying D6.5 (definition of compound ratio) and V.22 (ex aequali) to the three-term parallelogram sequence ABCD:DCKH:CEFG. The heath_only items (5.11 and 6.12) are integral to Heath's auxiliary-magnitude strategy, not subsumed by any single AI citation; they represent an independent route. This constitutes a genuine path difference, and the AI's direct approach is logically sound.

### 6.24
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decides: both proofs establish the same key intermediate conclusions -- equiangularity of the sub-triangles (AEF with ACB, AKF with ADC) with the whole parallelogram's component triangles, proportionality of all corresponding sides about equal angles, similarity via D6.1, and transitivity via 6.21. The difference lies in the tools used to derive these shared conclusions. Heath uses 6.2 (parallel line cuts sides proportionally) to extract ratios, then manipulates them with 5.18 (componendo), 5.16 (alternando), and 5.22 (ex aequali). The AI instead establishes equiangularity first using 1.29 and 1.32, then applies 6.4 (equiangular triangles have proportional sides) to derive the needed ratios directly, combining them with 5.11. The proof-tree containment test confirms that three of the four heath_only items (6.2, 5.16, 5.22) appear inside Heath's proof of 6.4, meaning the AI cites 6.4 as a unit while Heath re-derives its internals inline. The fourth heath_only item (5.18) is not needed by the AI because its use of 6.4 naturally produces ratios in the required form, avoiding the separando-to-componendo conversion. The ai_only items (1.29, 1.32, 1.34, CN1) are over-citations of elementary facts that Heath uses implicitly. This is a citation-depth difference with the same logical backbone, yielding G.

### 6.25
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same geometric backbone: apply parallelograms equal to the two given figures, find a mean proportional, construct a similar figure on it, then use the duplicate ratio property and proportional reasoning to show the constructed figure equals the target. The key differences are citation-depth variations. Heath cites 1.44 for the first parallelogram application (to a triangle), while the AI uses the more general 1.45 for both. Heath cites 6.19 (similar triangles in duplicate ratio), while the AI cites 6.20 (similar polygons in duplicate ratio); since 6.19 appears explicitly inside Heath's proof of 6.20, the AI is citing a higher-level unit that subsumes it, satisfying the proof-tree containment test. For the final proportional arithmetic, Heath uses alternando (5.16), while the AI uses 5.7 (equal magnitudes have same ratio), 5.9 (same ratio implies equality), and 5.11 (transitivity), which are different Book V tools reaching the same conclusion. All differences are in citation granularity rather than in the logical backbone.

### 6.26
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same backbone: assume the inner parallelogram is not about the same diameter, construct a parallelogram about the diameter via I.31, use VI.24 to establish similarity/proportionality, derive that two segments must be equal via V.9, and reach a contradiction. The sole heath_only citation is 5.11 (transitivity of ratios), which the AI replaces with CN1 (transitivity of equality applied to ratio expressions) combined with 6.21 (transitivity of similarity) and D6.1 (definition of similar figures) to derive the same ratio equality. The ai_only items (P1, D6.1, CN1, 1.34, 6.21) are a mix of over-citation of constructions/definitions/axioms and alternative citation-depth for the ratio transitivity step. The key geometric conclusions are identical in both proofs, making this a same-backbone, different-citation-depth case.

### 6.27
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they bisect the line, take an arbitrary parallelogram applied to the line with a similar defect, use VI.26 to establish the parallelograms are about the same diameter, use I.43 to establish complement equality, construct the gnomon argument, and conclude the half-parallelogram is greatest. The heath_only citation {1.36} represents a citation-depth difference: Heath explicitly invokes I.36 to show that parallelograms on equal bases (the two halves of the bisected line) are equal, while the AI proof implicitly uses the same fact by noting AE = EB from the midpoint construction without formally citing I.36. The ai_only citations {1.10, CN5, D6.1, P1} are all construction steps (1.10 for bisection), definitions (D6.1 for similar figures), postulates (P1 for drawing), and common notions (CN5 for whole > part) that Heath leaves implicit. This is a symmetric over/under-citation pattern with the same key intermediate conclusions, characteristic of a granularity difference.

### 6.28
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same backbone: bisect AB, construct a similar parallelogram EBFG on the half-line EB, handle the trivial equality case, construct a parallelogram KLMN equal to the excess (EBFG minus C) and similar to D, show it is similar to EBFG via 6.21, construct an inner parallelogram (OGPQ/EOPQ) equal and similar to KLMN, establish it is about the same diameter as EBFG via 6.26, then show the gnomon equals C and the resulting parallelogram applied to AB satisfies the requirements. The AI's ai_only citations (1.10, 1.3, 1.43, 6.24, 6.27, CN3, D6.1) are all granularity-level differences: 1.10 and 1.3 are construction propositions cited explicitly, 1.43 is the complement equality that Heath uses implicitly, 6.24 and 6.27 are cited for intermediate similarity and the maximality condition, and CN3 and D6.1 are axiom/definition over-citations. Heath's sole unique citation 1.36 (parallelograms on equal bases are equal) is used in the step OB = TE since AE = EB, which the AI handles through its complement-based argument using 1.43 instead, representing a micro-level difference in how the same geometric fact is established rather than a different logical path.

### 6.29
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: bisect AB at E, construct a parallelogram on EB similar to D, use VI.25 to construct a larger parallelogram equal to the original plus C and similar to D, show the two parallelograms are about the same diameter via VI.26, establish via gnomon arithmetic that the gnomon equals C, and conclude the applied parallelogram equals C with the excess similar to D via VI.24. The AI's ai_only citations (1.10, 6.18, 5.14, 6.22, CN3, CN5) are construction steps, ratio lemmas, and common notions that Heath leaves implicit -- typical over-citation at a finer granularity. Heath's sole unique citation (1.36, parallelograms on equal bases are equal) is used to establish AN = NB; the AI handles this area relationship through a broader application of 1.43 (complements about a diameter) without explicitly citing 1.36. The key intermediate conclusions are identical in both proofs, making this a same-backbone, different-depth case (Case A) under Q2.

### 6.30
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath's proof constructs the golden section via area methods: applying a parallelogram equal to the square on AB and exceeding by a similar figure (6.29), then using reciprocal proportionality in equiangular parallelograms (6.14) to derive the proportion. The AI takes a fundamentally different route, invoking the Book 2 result (2.11) that directly cuts a line so that the rectangle of the whole and one segment equals the square on the other, then converting this area equality to a proportion via the converse of 6.17. The citation sets are completely disjoint (Jaccard 0.0), and the key intermediate conclusions differ: Heath's backbone passes through parallelogram constructions and reciprocal proportionality, while the AI's passes through the rectangle-square equality from 2.11 and the proportion-rectangle equivalence from 6.17. Both paths are logically complete and valid, making this a genuine path difference.

### 6.31
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: draw AD perpendicular to BC, establish similarity of triangles ABD and ACD to ABC via 6.8, derive the continued proportions BC:BA=BA:BD and BC:CA=CA:DC, show that figure ratios equal segment ratios (duplicate ratio argument), then sum and use BD+DC=BC to conclude equality. The sole heath_only citation is 6.19 (similar triangles in duplicate ratio of corresponding sides), while the AI cites the more general 6.20 (similar polygons in duplicate ratio of corresponding sides). The proof-tree containment test confirms that 6.19 appears inside Heath's proof of 6.20, so the AI is citing 6.20 as a unit while Heath uses the triangle-specific 6.19 that 6.20 subsumes. The ai_only citations (5.24, 5.7, 5.9, 6.4, D5.9) represent explicit lower-level steps that Heath's proof handles more tersely or implicitly. This is a citation-depth difference with identical key intermediate conclusions.

### 6.32
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: using I.29 to establish alternate angle equalities (BAC = ACD and ACD = CDE), deducing BAC = CDE by transitivity, applying VI.6 to conclude equiangular triangles from the proportional sides about equal angles, extracting the angle equality ABC = DCE, then summing angles at C to show BCA + ACE equals two right angles via I.32, and finally applying I.14 for collinearity. The only citation difference is that the AI explicitly cites CN1 (Common Notion 1) for the transitivity step where Heath leaves it implicit. Since CN1 is a common notion (not a substantive proposition) and the underlying logical step is present in both proofs at the same position, this is a same-backbone, different-depth situation (Case A of Q2), yielding a granularity difference classification.

### 6.33
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the identical logical backbone: construct equimultiples of arcs BC and EF, show via III.27 that the corresponding central angles are equimultiples of BGC and EHF, verify the equimultiple comparison tracks (greater/equal/less), invoke V.Def.5 to conclude BC:EF :: BGC:EHF, then use the doubling relationship (central angle = 2 * inscribed angle) to extend the proportion to inscribed angles. The heath_only set is empty, confirming that every Heath citation appears in the AI set. The ai_only items (3.20, 3.26, 5.11, 5.15, CN2, D3.1) are all explicit citations for steps that Heath handles implicitly: 3.20 for the doubling relationship, 3.26 used in an indirect argument for the comparison step, 5.15 and 5.11 for ratio manipulation, and CN2/D3.1 as foundational citations. This is classic over-citation at greater depth, placing the classification squarely in Case A of Q2.
