# Book 12 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 11 | 12.1, 12.2, 12.5, 12.6, 12.7, 12.8, 12.9, 12.13, 12.14, 12.15, 12.18 |
| Path difference (D) | 6 | 12.3, 12.4, 12.10, 12.11, 12.12, 12.16 |
| AI proof error (E) | 1 | 12.17 |

**Total**: 18 propositions

## Error Details

| Proposition | Error type | Details |
|---|---|---|
| 12.17 | Unsupported assertion | CANDIDATE E — 12.17   violated_claim : In Steps 10-11, the AI asserts 'the perpendicular from A to that face is at least as great as the perpendicular from A to the corresponding chord in the original |

## Per-Proposition Analysis

### 12.1
**Category**: Granularity difference
**Jaccard**: 0.417
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: they establish that triangles ABM and FGN (formed by joining polygon vertices to the endpoints of the diameters) are equiangular, derive the proportion BM:GN = BA:GF via VI.4, and then use the duplicate ratio (VI.20) to connect the polygon ratio to the ratio of squares on the diameters. The difference lies in how each proof obtains the key angle equality feeding into the triangle equiangularity. Heath uses VI.6 to first prove triangles ABE and FGL equiangular (from one equal angle and proportional sides in the similar polygons), then extracts the angle equality, and applies III.27 for inscribed angles on equal circumferences. The AI instead reads the corresponding angle equality directly from the definition of similar polygons (D6.1), bypasses VI.6 entirely, and uses III.21 (angles in the same segment) rather than III.27 for the inscribed angle step. The AI's additional citations (5.11, CN1, D5.9, P4) are axiom/definition-level over-citations making explicit what Heath leaves implicit. Since the key intermediate conclusions (equiangularity of the diameter-triangles, the side proportion, and the duplicate ratio conclusion) are the same in both proofs, the difference is one of citation depth rather than a fundamentally different proof path.

### 12.2
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same double reductio ad absurdum backbone using the method of exhaustion: assume circles are not as the squares on their diameters, then derive contradictions for both S < circle EFGH and S > circle EFGH, concluding S = circle EFGH. The key intermediate conclusions are identical in both proofs: the exhaustion process yields an inscribed polygon exceeding S, similar polygons relate as squares on diameters (12.1), proportion reasoning (5.11, 5.16) produces the contradiction. The ai_only set (1.34, 1.41, 10.1, 3.30, 4.6, 5.14, CN5) consists entirely of construction steps, auxiliary results, and common notions that Heath uses implicitly but does not cite explicitly — the inscribed square construction (4.6), arc bisection (3.30), the exhaustion lemma (10.1), area relationships (1.34, 1.41), proportion reasoning (5.14), and the whole-greater-than-part axiom (CN5). heath_only is empty, confirming the AI cites a strict superset of Heath's references. This is a clear case of the AI providing greater citation depth for the same logical backbone.

### 12.3
**Category**: Path difference
**Jaccard**: 0.263
**Analysis**: Q2 decides the classification. Heath's proof establishes the equality of the two sub-pyramids via SAS congruence (I.4) applied to corresponding face triangles, using XI.10 to establish angle equality between lines in different planes, and proves the prisms exceed half the whole pyramid by geometric containment (showing each prism contains a pyramid equal to one of the sub-pyramids). The AI's proof takes a fundamentally different path: it establishes similarity of the sub-pyramids by directly computing all six edge lengths as half the corresponding edges of the original (using 6.2 midline properties), proves equality via SSS congruence (1.8 instead of I.4), identifies the prisms through parallelogram structures (1.33), and argues the prisms exceed half the whole via a volume-ratio calculation (claiming each sub-pyramid is 1/8 of the original using 11.33 and 6.19). The backbones differ in both the congruence method and the approach to the prisms-greater-than-half conclusion. E was considered for the AI's application of 11.33 (similar parallelepipeds) to pyramids, but under the lenience rule, the underlying mathematical inference is sound (similar pyramids do have volumes in the cube of the linear ratio), making this an informal-but-sound inference rather than an invalid one. The different logical backbone (SSS vs SAS, direct edge computation vs angle-based congruence, volume ratios vs geometric containment) constitutes a genuine path difference.
**Audit Record**: CANDIDATE E — 12.3
  violated_claim : "each similar pyramid has all linear dimensions halved, so each has volume (1/2)^3 = 1/8 of the original [the ratio of similar solids is the cube of the linear ratio, following from 11.33 and 6.19]"
  failure_mode   : invalid_inference
  missing_is     : expansion
  evidence       : AI Step 11 cites 11.33 (similar parallelepipeds in triplicate ratio) and 6.19 (similar triangles in duplicate ratio) to justify that similar pyramids have volumes in the cube of the linear ratio. 11.33 applies to parallelepipeds, not pyramids. The correct result for pyramids is 12.8 (forward from 12.3).
  why_not_terse  : Cannot complete convincingly — the mathematical inference is sound (similar pyramids do have volumes in cubic ratio), the AI merely cited the wrong covering proposition. Under lenience rule, this is informal-but-sound, not invalid. Reclassified to NOT-E (D).

### 12.4
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 reveals different logical backbones. Heath establishes the key ratio (prisms from one pyramid to prisms from the other as base to base) through a chain involving similarity of triangles (ABC~LOC, DEF~RVF), Proposition 6.22 (similar figures on proportional lines are proportional), 5.16 (alternation), the Lemma following 12.3, and 11.39 (relating parallelogram-based and triangle-based prisms). The AI instead uses Proposition 6.1 (triangles of the same height are as their bases) applied directly to the prism bases, arguing that the equal-height condition and uniform midpoint scaling make 6.1 sufficient to establish the same ratio. This is a genuinely different geometric argument — not a matter of citation depth but of which geometric facts drive the proof. The AI's path is logically valid: 6.1 does apply to the prism bases given the equal height of the original pyramids, and the combination via 5.12 and recursive application are sound. Q3 confirms validity, yielding classification D.

### 12.5
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Both proofs follow the same exhaustion-by-contradiction backbone: assume the ratio base:base equals pyramid:W where W is not the second pyramid, handle Case 1 (W less than the second pyramid) via successive subdivision by XII.3, exhaustion by X.1, and prism ratio by XII.4 to derive a contradiction, then handle Case 2 (W greater) by reducing to Case 1 via inversion. The key intermediate geometric conclusions are identical. The differences lie entirely in which Book V ratio-manipulation propositions are cited for the algebraic steps: the AI uses 5.11 (transitivity), 5.14 (ordering of proportionals), CN5 (whole greater than part), and D5.13 (definition of inverse ratio) where Heath uses V.11/V.16 (alternation) and XII.2 Lemma. The AI's use of 5.14 plus CN5 to derive the contradiction is a valid alternative to Heath's alternation step via 5.16, and the AI's use of D5.13 for inversion replaces Heath's reference to the XII.2 Lemma. These are citation-depth differences in the ratio algebra, not backbone differences, making this a granularity difference.

### 12.6
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: decompose polygonal bases into triangles via diagonals, apply XII.5 to compare triangular pyramids of equal height, then recombine the ratios to obtain the final proportion. The key difference is the recombination mechanism: Heath uses V.18 (componendo) sequentially to build up the polygon ratio one triangle at a time, while the AI uses V.24 (ratio addition with a common second term) to aggregate all triangular sub-pyramid ratios simultaneously. The proof-tree containment test confirms this is a depth difference rather than a path difference: V.18 appears inside Heath's own proof of V.24, so the AI is citing a higher-level result (5.24) that internally relies on the step Heath applies directly (5.18). The remaining ai_only items (P1 for drawing diagonals, D5.5 for ratio inversion) are construction and definitional over-citations consistent with granularity difference.

### 12.7
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this classification. Both the AI and Heath proofs argue through identical key intermediate conclusions: (1) diagonal BD bisects parallelogram ABED so triangle ABD equals triangle BDE (I.34), (2) pyramids with equal triangular bases and the same height are equal (XII.5), yielding pyramid ABCD = pyramid BCDE, (3) diagonal CE bisects parallelogram BCFE so triangle BCE equals triangle CEF (I.34), (4) again by XII.5 pyramid BCDE = pyramid CDEF, and (5) therefore all three pyramids are equal. The AI proof adds explicit citations to definitions D11.12 and D11.13 (for prism and related solid geometry terms) and CN1 (transitivity of equality), which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only definitions and a common notion, this is a clear case of over-citation at the same logical backbone, making it a granularity difference.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.308
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: complete parallelepipedal solids on the similar pyramids, show the parallelepipeds are similar (XI.24), apply XI.33 to get the triplicate ratio of corresponding sides, then relate pyramid to parallelepiped via prism = half parallelepiped (XI.28) and prism = triple pyramid (XII.7), yielding the pyramid ratio equals the triplicate ratio. The AI cites all four of Heath's references (11.24, 11.28, 11.33, 12.7) and adds nine further citations (11.31, 5.11, 5.15, 6.4, CN1, D11.9, D5.10, D6.1, P1) which are definitions, common notions, postulates, and lower-level propositions supporting the same steps at finer granularity. heath_only is empty, confirming the AI misses nothing Heath uses. The key intermediate conclusions are identical in both proofs, making this a citation-depth difference, not a path difference.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decides this as G (granularity difference, Case A). Both proofs share the same logical backbone: construct parallelepipeds from the given pyramids, apply XI.34 to obtain reciprocal proportionality of parallelogram bases and heights, then use I.34 to relate triangular bases to parallelogram bases, and chain the proportions. The difference is purely in citation depth and which specific lemmas are invoked for equivalent steps. Heath goes directly from pyramid to parallelepiped (factor of 6) and uses V.11 to chain proportions, while the AI takes a more explicit two-step route through prisms (XII.7 for pyramid-to-prism, XI.28 for prism-to-parallelepiped) and uses V.15 instead of V.11 for the proportion chaining. The ai_only items (XII.7, XI.28, CN2, CN3) are construction-level and common-notion citations that spell out what Heath does more concisely, and V.15 replaces V.11 for an equivalent logical step. The heath_only item V.11 is a proportion-transitivity result that the AI replaces with V.15 (parts have the same ratio as their multiples), achieving the same intermediate conclusion. The key geometric facts established are identical in both proofs.

### 12.10
**Category**: Path difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification. In Case 1 (cylinder > 3 times cone), both proofs follow essentially the same exhaustion argument: inscribe polygons, show the prism on the polygon exceeds 3 times the cone, invoke 12.7 to get the pyramid exceeds the cone, contradicting containment. However, in Case 2 (cylinder < 3 times cone), the backbones diverge. Heath inscribes pyramids within the cone, exhausts the cone from the inside, and shows the inscribed pyramid exceeds a third of the cylinder, yielding a prism exceeding the cylinder while being contained in it. The AI instead circumscribes a polygon about the circle, constructs a prism and pyramid that contain the cylinder and cone respectively, and derives a contradiction from the circumscribed pyramid exceeding the cone while the corresponding prism is less than 3 times the cone. This circumscribed-polygon strategy in Case 2 is a genuinely different logical path from Heath's inscribed-pyramid approach, producing different key intermediate conclusions. Q3 confirms the AI's path is logically valid: the exhaustion principle applies to circumscribed polygons, 12.7 gives prism = 3 times pyramid for any polygon, and the containment and contradiction arguments are sound.

### 12.11
**Category**: Path difference
**Jaccard**: 0.400
**Analysis**: Q2 identified genuinely different backbones between the two proofs, leading to classification under Q3. Heath proves the result for cones first using an exhaustion argument with inscribed pyramids, applies alternando (5.16) as a key ratio step, and then extends to cylinders via 12.10. The AI reverses the order entirely: it proves the result for cylinders first using an exhaustion argument with inscribed prisms (justified by decomposing prisms into pyramids via 12.7 and applying 12.5/12.6), uses ratio comparison properties (5.8, 5.10) instead of alternando (5.16), and then derives the cone result from the cylinder result via 12.10 and 5.15. These structural differences -- proving cylinders before cones, using prisms rather than pyramids as the primary exhaustion objects, and substituting different ratio-manipulation propositions -- constitute a different logical path. The AI's path is logically valid throughout: the exhaustion argument is properly structured, the prism-to-pyramid decomposition is sound, and the derivation of the cone result from the cylinder result is correct.

### 12.12
**Category**: Path difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Heath's proof uses the method of exhaustion with inscribed polygons and pyramids: it inscribes polygons in the base circles, erects pyramids, proves these pyramids are similar (via VI.6, V.16, V.22, VI.5), applies XII.8 (similar pyramids in triplicate ratio), sums them with V.12, and obtains the result by double reductio ad absurdum. The AI takes a fundamentally different path: it introduces an intermediate solid C sharing A's base and B's height, decomposes the ratio A:B into A:C (height ratio, established via prisms and exhaustion) and C:B (base ratio squared, via XII.11 and XII.2), then compounds these via V.22 ex aequali to obtain the triplicate ratio. The backbones are entirely different -- Heath works through similar pyramids and exhaustion while the AI works through ratio decomposition via an intermediate solid. The AI's Step 4 mis-cites XI.32 (same height implies ratio of bases) for the converse claim (same base implies ratio of heights), but the underlying mathematical fact is correct and provable in Euclid's system; under the lenience rule this is not an error but a citation issue. The AI's proof path is logically complete and valid, yielding classification D.
**Audit Record**: CANDIDATE E — 12.12
  violated_claim : "These prisms, being parallelepipedal solids on equal bases, are to one another as their heights h_A and h_B by 11.32"
  failure_mode   : invalid_inference
  missing_is     : expansion — XI.32 establishes same-height-as-bases; the AI needs same-base-as-heights which is the converse, but the mathematical fact is correct and derivable; this is a citation error not a logical gap
  evidence       : AI Step 4 cites XI.32 ("Parallelepipedal solids which are of the same height are to one another as their bases") but applies it to prisms on equal bases to conclude they are as their heights — the converse
  why_not_terse  : Cannot complete convincingly — the underlying mathematical claim is true and the AI's broader argument is sound; the error is in citing the wrong proposition number, not in the logical structure. Reclassify as NOT-E.

### 12.13
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided the classification. Both proofs follow the identical equimultiple strategy mandated by Definition V.5: they construct arbitrary multiples of the two axis segments, erect corresponding cylinders by cutting with parallel planes, use XII.11 to show that the small cylinders with equal bases and equal heights are equal, establish that the m-fold and n-fold composite cylinders are equimultiples of the respective segment cylinders, verify the trichotomy (excess, equal, less) between the composite cylinders tracks the trichotomy between the composite axes, and conclude by V. Def. 5 that the ratio of cylinders equals the ratio of axes. The key intermediate conclusions are identical in both proofs. The only difference is citation depth: the AI explicitly cites common notions (CN1, CN2, CN5), definitions (D11.21, D11.22, D11.23, D11.8, D5.2), and postulates (P1, P2) that Heath leaves implicit. Since heath_only is empty and all ai_only items are foundational (no substantive theorems), this is a clear Case A granularity difference.

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: construct an auxiliary cylinder sharing one parameter (base or height) with each of the two original cylinders, use XII.11 (cylinders of same height are as their bases) to show the auxiliary equals one original, use XII.13 (cutting a cylinder by a parallel plane gives proportional axes) to establish the proportion with the other, then extend to cones via XII.10. The AI explicitly cites Book 5 proportion-theory results (5.7 for substituting equals in ratios, 5.15 for parts having the same ratio as multiples, 5.11 for transitivity of ratios) that Heath applies implicitly without citation. Since heath_only is empty and ai_only contains only proportion-manipulation lemmas that justify steps Heath performs without explicit citation, this is a classic over-citation granularity difference.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.571
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs follow the same biconditional structure: forward direction with two cases (equal heights and unequal heights) and the converse. The key intermediate conclusions are identical in both proofs: in the unequal-heights case, both construct an auxiliary solid sharing one base with one original and the height of the other, then establish two ratio equalities (one from equal-height comparison via 12.11, one from equal-base/height comparison) and combine them via 5.11. The only substantive citation difference is that the AI uses 12.14 (cones/cylinders on equal bases are as their heights) where Heath uses 12.13 (cylinder cut by parallel plane gives ratio equal to ratio of axes). The proof-tree containment test confirms that 12.13 appears inside Heath's proof of 12.14, so the AI is citing a higher-level result as a unit while Heath effectively re-derives its internals inline. The AI's additional citation of CN1 is a common notion (over-citation). This is a citation-depth difference with the same logical backbone.

### 12.16
**Category**: Path difference
**Jaccard**: 0.125
**Analysis**: Q2 reveals different backbones, leading to Q3 which confirms a valid different path (D). Heath's proof constructs a tangent line AC to the lesser circle (III.16), then bisects arcs until arc LD < AD, draws LM perpendicular to BD, shows LD = DN (III.3, I.4), and argues that since LN is parallel to AC and AC touches the lesser circle, LN does not touch it either — a parallelism-based argument. The AI proof instead argues through perpendicular distances: it uses the Pythagorean theorem (1.47) and III.14 to show that as arcs decrease through repeated bisection, the perpendicular distance from the center to each chord increases, and by X.1 this distance eventually exceeds the radius of the lesser circle, so no side touches it. These are genuinely different intermediate mechanisms — Heath uses tangent-parallelism while the AI uses perpendicular-distance comparison — producing different key intermediate conclusions with different supporting citations. The AI's perpendicular distance chain is logically sound and complete, satisfying Q3.

### 12.17
**Category**: AI proof error
**Jaccard**: 0.074
**Analysis**: The AI proof takes a fundamentally different constructive approach from Heath, erecting perpendicular planes through each side of the inscribed polygon and building the polyhedron from polygons in those planes. The critical question is Q1(b)/Q3(b): whether the AI's argument that the polyhedron does not touch the lesser sphere is logically complete. The AI's Steps 10-11 assert that the perpendicular from the centre A to any face of the solid exceeds the radius of the lesser sphere, claiming this follows because 'the face in the perpendicular plane lies on or beyond the chord relative to A.' This is the essential geometric claim of the entire proposition, and Heath devotes the majority of his proof to establishing it through an elaborate chain involving 3.27, 1.26, 6.2, 11.6, 1.33, 11.9, 11.7, 1.47, 3.31, and 6.8. The AI provides no valid supporting chain: the cited propositions 3.15 (chords nearer centre are greater), 11.38 (about bisecting cube faces, completely irrelevant), 1.19 (angle-side inequality in triangles), and CN5 (whole greater than part) do not license the 3D perpendicular-distance claim. This is not mere terseness but an unsupported assertion of the core conclusion, satisfying the hardened E standard.
**Audit Record**: CANDIDATE E — 12.17
  violated_claim : In Steps 10-11, the AI asserts 'the perpendicular from A to that face is at least as great as the perpendicular from A to the corresponding chord in the original plane, because the face in the perpendicular plane lies on or beyond the chord relative to A' and concludes the perpendicular from A to every face exceeds the radius of the lesser sphere.
  failure_mode   : unsupported_assertion
  missing_is     : support — this is the core geometric claim of the entire proposition, not an expansion of an already-supported step. Heath's proof requires an elaborate chain (3.27, 1.26, 6.2, 11.6, 1.33, 11.9, 11.7, 1.47, 3.31, 6.8) to establish the analogous result.
  evidence       : Step 10 cites 1.19 (angle-side inequality in triangles) and CN5 (whole > part); Step 11 cites 3.15 (diameter greatest chord) and 11.38 (bisecting cube faces). None of these propositions license the claim that the 3D perpendicular distance from A to a face in a perpendicular plane exceeds the perpendicular distance from A to the corresponding chord in the base plane. 11.38 is about cubes and is entirely irrelevant.
  why_not_terse  : This is not mere brevity — the claim is the essential geometric argument of the entire proposition. Heath devotes the bulk of his proof to exactly this argument, requiring detailed reasoning about equal perpendiculars, parallel lines, quadrilaterals in planes, inscribed quadrilaterals in circles, and Pythagorean relationships. The AI skips all of this, asserting the conclusion without any valid supporting chain.

### 12.18
**Category**: Granularity difference
**Jaccard**: 0.100
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same double reductio backbone: (1) assume the triplicate ratio holds to a sphere less than the target, inscribe similar polyhedral solids via 12.17, derive a contradiction where the lesser sphere must be both greater and less than the inscribed polyhedron; (2) handle the greater-than case by inversion reducing to the already-refuted case; (3) conclude. The AI's ai_only citations (12.8, 5.11, 5.12, CN5, D11.14, D11.17, D5.10) represent finer-grained detail: the AI explicitly breaks down why similar polyhedra have the triplicate ratio via 12.8 (similar pyramids in triplicate ratio of sides) and 5.12 (combining parts), while Heath cites 12.17 as a unit covering this. The definitions and CN5 are implicit in Heath. Heath's heath_only citations (12.2 Lemma for the greater-case reduction, 5.16 for alternando) correspond to steps the AI performs by direct reasoning or uses without listing: the AI applies alternando in Step 11 and handles the greater case by straightforward inversion rather than citing 12.2 Lemma. The key intermediate conclusions are identical at matching logical positions in both proofs, confirming Case A of Q2.
