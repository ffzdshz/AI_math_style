# Book 12 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 10 | 12.1, 12.2, 12.5, 12.7, 12.8, 12.9, 12.13, 12.14, 12.15, 12.18 |
| Path difference (D) | 8 | 12.3, 12.4, 12.6, 12.10, 12.11, 12.12, 12.16, 12.17 |
| AI proof error (E) | 0 |  |

**Total**: 18 propositions

## Per-Proposition Analysis

### 12.1
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: (1) establish triangles ABE and FGL as equiangular via VI.6, (2) show inscribed angles AEB=AMB and FLG=FNG, (3) deduce triangles ABM and FGN are equiangular via I.32, (4) derive BM:GN=BA:GF via VI.4, and (5) conclude via duplicate ratios from VI.20. The sole heath_only citation is 3.27 (angles in equal circles on equal circumferences are equal), which the AI replaces with 3.21 (angles in the same segment are equal). Since each inscribed-angle step operates within a single circle, 3.21 is actually the more directly applicable proposition; Heath's choice of 3.27 works but is more general than necessary. The ai_only items (CN1, P4, D5.9, 5.11) are all axioms, definitions, and common notions that Heath leaves implicit. Since all key intermediate conclusions are identical and the citation differences reflect only depth of explicit citation and choice of equivalent foundational proposition, this is a granularity difference.

### 12.2
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs follow the identical exhaustion structure: assume the ratio of squares on diameters equals the ratio of one circle to an area S different from the other circle, then derive contradictions for both S < circle EFGH and S > circle EFGH using inscribed polygons, the exhaustion principle (10.1), similar polygon ratios (12.1), and proportion theory (5.11, 5.16). The AI proof's key intermediate conclusions match Heath's exactly in the same logical order. The ai_only citations (1.41, 10.1, 4.6, 5.14, CN5) are all over-citations making explicit what Heath uses implicitly: 10.1 is mentioned by name in Heath's text but not bracket-cited, 4.6 is a construction step for inscribing the square, 1.41 justifies the triangle-parallelogram area relationship, 5.14 licenses the inference from the polygon being less than the circle, and CN5 is a common notion invoked for the containment relationship. Heath_only is empty, confirming the AI cites a strict superset. This is a clear Case A granularity difference.

### 12.3
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 reveals genuinely different backbones, leading to classification via Q3. Heath proves face congruences using I.4 (SAS) and establishes similarity to the whole via XI.10 (equal angles from parallel lines in different planes) and VI.Def.1, then proves prism equality via XI.39 (prisms with parallelogram base double of triangle base are equal). The AI instead proves face congruences via edge-length ratios from VI.2 and I.8 (SSS), establishes similarity via VI.4 and Def.XI.9, and proves prism equality through an entirely different route using XI.28, XI.32, and XI.34 (parallelepiped volume theory — completing each prism to a parallelepiped and comparing via reciprocally proportional bases and heights). These are substantively different logical routes: SSS vs SAS for congruence, edge-ratio similarity vs angle-based similarity, and parallelepiped volume comparison vs direct prism equality. The heath_only citations (I.4, XI.10, XI.39, Def.VI.1) represent genuine alternative machinery, not mere depth differences. Q3 confirms the AI's path is logically valid and complete, so the classification is D.

### 12.4
**Category**: Path difference
**Jaccard**: 0.273
**Analysis**: Q2 decided the classification. Heath's proof establishes the key proportionality ABC:DEF :: prisms:prisms by using VI.22 (similar rectilinear figures on proportional lines are proportional) and V.16 (alternando) to transfer the similarity relation between sub-triangles into a proportion between the original bases. The AI takes a fundamentally different route: it uses VI.19 (similar triangles have areas in duplicate ratio of sides) to compute that each prism base is exactly one-fourth of the original triangle's area, then applies V.15 (parts have same ratio as same multiples) to conclude that the ratio of prism bases equals the ratio of original bases. These are different key intermediate conclusions -- Heath works through similarity-based proportion transfer (6.22 + 5.16), while the AI works through area-fraction computation (6.19 + 5.15). The proof-tree containment test confirms these are independent routes: 5.16 and 6.22 are not sub-steps of any AI-cited proposition used for the same purpose. The AI's path is logically complete and valid, with each step properly cited, yielding a path difference (D).

### 12.5
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Both proofs follow the same method-of-exhaustion backbone: assume the ratio of pyramids to bases yields a solid W less than the second pyramid, divide using 12.3 repeatedly, apply 10.1 to get small remainders, use 12.4 to establish the ratio of prisms, then derive a contradiction where W must be both greater and less than the sum of prisms. Both also handle the greater-than case by reducing it to the less-than case. The difference lies in which Book 5 proportion tools are used to reach the same intermediate conclusions: Heath uses 5.16 (alternando) and 5.11 (transitivity of ratios) to derive the contradiction, while the AI uses 5.14 (comparison of magnitudes in proportions) and CN1. For the second case, Heath invokes the 12.2 Lemma while the AI uses inversion (D5.13) and symmetry. These are different citation-depth choices for the same logical steps, not different proof paths. The ai_only items are predominantly definitions and common notions (D11.12, D5.13, D5.5, CN1, CN5) indicating over-citation, plus 5.14 as an alternative proportion tool. Q2 Case A applies: same backbone, different citation depth, yielding G.

### 12.6
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: Q2 decides this classification. Heath's proof builds up the polygonal pyramid ratio incrementally, adding one triangle at a time using componendo (5.18) and ex aequali (5.22) in alternation. The AI proof takes a fundamentally different approach: it establishes individual triangular pyramid ratios via 12.5 relative to a common reference pyramid (FGHN), then aggregates all ratios simultaneously using a summation principle (cited as 5.12, though 5.12's preconditions of equal ratios are not strictly met -- the result the AI claims is nevertheless mathematically correct as a property of ratios with a common consequent). The AI then uses inversion and 5.22 to combine the two aggregated ratios into the final result. Since Heath uses 5.18 (componendo) as a core structural element while the AI never uses componendo and instead relies on direct summation of ratios, these constitute genuinely different logical backbones (Case B in Q2). Under Q3, the AI's different path is logically sound -- the mis-citation of 5.12 is an imprecise reference rather than an invalid inference, as the conclusion drawn is correct -- so the classification is D.

### 12.7
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: join diagonals BD, EC, and CD to divide the prism into three pyramids, then use I.34 twice to show the diagonals of parallelograms ABED and BCFE bisect them into equal triangles, apply XII.5 twice to equate pairs of pyramids with equal bases and the same height, and conclude by transitivity that all three pyramids are equal. The AI's only additional citations are CN1 (used explicitly for transitivity, which Heath invokes implicitly), D11.12, and D11.13 (definitions of pyramid and prism that Heath uses without citation). Since heath_only is empty and all ai_only items are axiom-level over-citations (a common notion and two definitions), the proofs share the same backbone at different citation depths, yielding a Granularity difference.

### 12.8
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: complete parallelepipeds on the two similar pyramids, show the parallelepipeds are similar, apply 11.33 for the triplicate ratio of similar parallelepipeds, then use 11.28 and 12.7 to establish that each pyramid is one-sixth of its parallelepiped, and conclude that the pyramids are in triplicate ratio of corresponding sides. The sole heath_only citation, 11.24 (opposite planes of a parallelepiped are equal and parallelogrammic), is replaced in the AI proof by its internal component 1.34 (opposite sides of a parallelogram are equal), which appears inside Heath's own proof of 11.24, satisfying the proof-tree containment test. The ai_only items consist of construction propositions (1.31), lower-level results (1.34, 5.15), and definitions (D11.9, D5.10, D6.1) that the AI cites explicitly where Heath leaves them implicit. All key intermediate conclusions are the same in both proofs, making this a citation-depth difference rather than a path difference.

### 12.9
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: complete triangular bases to parallelograms, construct parallelepipeds, establish the 6x pyramid-to-parallelepiped relationship, apply XI.34 for reciprocal proportionality of parallelepipeds, then convert back to triangular bases using I.34. The AI's additional citations (11.28, 12.7) explicitly derive the 1/6 relationship that Heath treats as established, while CN1, CN2, CN3 are over-citations of common notions. The AI uses 5.15 for a ratio step where Heath uses V.11 (5.11), but both achieve the same logical transition at the same position in the argument. The heath_only item 5.11 (transitivity of ratios) corresponds to a step the AI handles with CN1 at the same logical juncture. All differences are citation-depth rather than backbone differences.

### 12.10
**Category**: Path difference
**Jaccard**: 0.211
**Analysis**: Q2 decides the classification. Both proofs use double reductio ad absurdum with the method of exhaustion, and Case 1 (cylinder > 3*cone) follows essentially the same backbone in both proofs: inscribe polygons, exhaust segments via 10.1, relate prism to pyramid via 12.7, derive contradiction from pyramid being inscribed in cone. However, Case 2 (cylinder < 3*cone) reveals a genuine path difference. Heath inscribes polygons in the circle and sets up pyramids, deriving a contradiction when the prism on the inscribed polygon exceeds the cylinder despite being inscribed in it. The AI instead circumscribes polygons about the circle (citing 3.16 and 1.12 for tangent constructions), deriving a contradiction when the pyramid on the circumscribed polygon is less than the cone despite the cone being inscribed in it. These are different intermediate constructions yielding different key intermediate conclusions, constituting Case B in Q2. Q3 confirms the AI's circumscribed-polygon approach is logically valid, with a sound chain from premises to conclusion.

### 12.11
**Category**: Path difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs use the same overall strategy of double reductio ad absurdum combined with the method of exhaustion (X.1) and proportionality of inscribed polygons to circles (XII.1, XII.2). However, the key intermediate conclusions differ in two substantive ways. First, Heath works with pyramids on inscribed polygons and cites XII.6 (pyramids of same height with polygonal bases are as their bases) to establish the ratio of the solid figures, while the AI works with prisms on inscribed polygons and re-derives an analogous result for prisms using XII.7 (triangular prism equals three pyramids), XII.5 (pyramids with triangular bases are as their bases), and V.24 (summing proportions). Second, Heath reaches the contradiction via V.16 (alternation of proportions), while the AI uses V.14 (if A:B=C:D and A<C then B<D). Additionally, Heath proves the result for cones first and extends to cylinders via XII.10, whereas the AI proves for cylinders first and extends to cones. These constitute genuinely different intermediate conclusions and logical paths, not merely different citation depth, so the classification is D. The AI's path was verified as logically valid in Q3.

### 12.12
**Category**: Path difference
**Jaccard**: 0.158
**Analysis**: Q2 determines the classification. Heath's proof uses a double reductio (exhaustion) approach: inscribing polygons in circles, building pyramids approximating the cones, proving individual pyramids are similar via triangle similarity (VI.5, VI.6, V.16, V.22), applying XII.8 for the triplicate ratio of similar pyramids, summing via V.12, and completing the exhaustion argument via X.1. The AI takes a fundamentally different direct ratio approach: constructing a continued proportion via 6.11 to define the triplicate ratio (D5.10), introducing an intermediate cone/cylinder C of mixed dimensions, showing A:C via 12.11 and 12.2 (same height, different bases), proving C:B by establishing from D5.5 that cylinders on the same base are proportional to their heights (with 12.10 reducing cones to cylinders), and chaining via ex aequali (5.22). The key intermediate conclusions are entirely different -- Heath's backbone rests on pyramid similarity and exhaustion, while the AI's rests on direct ratio composition through an auxiliary solid. Both paths are logically complete, so this is a valid path difference (D).

### 12.13
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the identical Eudoxean proportion backbone: they cut the cylinder by a parallel plane, take arbitrary equimultiples of the two sub-axes, construct corresponding equimultiple cylinders using XII.11 (since bases are equal, cylinders on equal axes are equal), verify the equimultiple criterion (greater/equal/less holds simultaneously for axes and cylinders), and conclude by V. Def. 5. The ai_only set consists entirely of definitions (D11.21, D11.23), common notions (CN2, CN5), and a geometric construction proposition (11.16) that the AI cites explicitly to justify that the cross-section is a circle equal to the bases, while Heath treats this as obvious from the setup. heath_only is empty. Since the key intermediate conclusions are the same and the citation differences reflect only the depth of explicit justification, this is a granularity difference.

### 12.14
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same logical backbone: construct or identify a cylinder equal to one of the given cylinders (using equal bases and same height via XII.11), apply XII.13 to establish the ratio between cylinders and their axes, substitute the equal cylinder to obtain the desired proportion, and then extend the result to cones via XII.10. The AI proof adds explicit citations for steps Heath performs implicitly: 5.7 for the substitution of equal magnitudes, 5.15 for transferring the cylinder ratio to cones (as one-third submultiples), CN1 and D5.5 for establishing cylinder equality, and D11.21 for the definition of cylinder. Since heath_only is empty and all ai_only items are definitions, common notions, or ratio-manipulation propositions that support the same intermediate conclusions Heath reaches without citation, this is a citation-depth difference rather than a path difference.

### 12.15
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they establish a biconditional by (1) constructing a third cone/cylinder sharing one dimension with each given solid, (2) using the same-height ratio (12.11) and a same-base ratio result to relate the constructed solid to each original, (3) combining via 5.7 and 5.11. The sole citation difference is that Heath uses 12.13 (cylinder cut by parallel plane gives axis ratio) to establish the height-ratio step, while the AI uses 12.14 (cones/cylinders on equal bases are as their heights). The proof-tree containment test confirms that 12.13 appears inside Heath's own proof of 12.14, so the AI is citing 12.14 as a packaged unit while Heath re-derives its content inline via 12.13. This is a citation-depth difference, not a path difference. The AI's general argument also validly covers both of Heath's sub-cases (heights equal and heights unequal) through a single construction that works regardless.

### 12.16
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Classification was decided at Q2/Q3 (different backbone, valid path). Heath's proof establishes the non-touching condition via a parallelism argument: AC is drawn tangent to the inner circle, then repeated arc bisection yields a chord LN parallel to AC, so LN also does not touch the inner circle. The AI proof instead takes a direct perpendicular-distance approach: it inscribes a square, then bisects arcs repeatedly (using 10.1 for convergence) until the perpendicular distance from the centre to each chord exceeds the inner circle's radius, citing 3.16 and 3.18 to conclude non-touching. The key intermediate conclusions differ fundamentally: Heath argues through tangent-parallel geometry and triangle congruence (1.4), while the AI argues through perpendicular distances and chord-arc relationships (3.14, 3.15, 3.29). Both paths are logically complete, so this is a genuine path difference.

### 12.17
**Category**: Path difference
**Jaccard**: 0.130
**Analysis**: Q2 determines this classification. The AI and Heath proofs have fundamentally different backbones. Heath constructs the polyhedron by drawing a perpendicular OA from center to sphere surface, creating planes through OA, inscribing arcs in the resulting semicircles, then establishing an intricate chain of parallel lines (WV parallel to KB via VI.2, PV parallel to SW via XI.6), showing KBPS is a quadrilateral in a circle (XI.7, XI.9, I.33), and using a detailed algebraic argument with squares and rectangles (III.31, VI.8) to prove AX > AZ > AG. The AI takes a rotational approach, explicitly citing 12.16 to inscribe the polygon, then rotating the construction around an axis by passing planes through AC, constructing the polyhedron from connected vertices in adjacent planes, and arguing that the perpendicular from center to each face exceeds the lesser sphere's radius using a Pythagorean framework (OT^2 + r^2 = R^2). E was considered for the terse assertion of OT >= OS in Step 16, but the audit record yields missing_is = expansion (the claim is stated with supporting structure, just not fully expanded), so the lenience rule applies and the verdict is NOT-E. The very low Jaccard (0.13) with 7 AI-only and 13 Heath-only citations confirms the substantial path divergence.
**Audit Record**: CANDIDATE E — 12.17
  violated_claim : OT >= OS (perpendicular from O to face plane >= perpendicular from O to polygon side)
  failure_mode   : unsupported_assertion
  missing_is     : expansion  # The AI states the claim and sketches why, but doesn't fully expand the argument
  evidence       : Step 16: "OT >= OS > OE" - asserted without detailed derivation; the AI provides OT^2 + r^2 = R^2 framework but does not rigorously derive the inequality
  why_not_terse  : Cannot complete convincingly - the AI provides structural reasoning (Pythagorean framework, angle subtension argument) that informally supports the claim, making this an expansion gap rather than a logical gap

### 12.18
**Category**: Granularity difference
**Jaccard**: 0.182
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same exhaustion backbone: assume the triplicate ratio holds to something less than the second sphere, inscribe a polyhedral solid in the second sphere not touching an inner sphere (12.17), inscribe a similar polyhedron in the first sphere, establish that similar polyhedra are in the triplicate ratio of diameters, use alternation (5.16) to derive a contradiction, then handle the greater case by inversion reducing to the less case. The ai_only citations (12.8, 5.11, 5.12, 5.14, CN5, D11.14, D11.17, D5.10) represent over-citation of proportion-theory lemmas, definitions, and common notions that Heath uses implicitly, plus an explicit derivation of the triplicate ratio of similar polyhedra via 12.8 and 5.12 where Heath cites 12.17's corollary as a unit. The heath_only citation (12.2) is a lemma Heath invokes in the greater case that the AI handles by direct parallel argument instead. These are all citation-depth differences on the same logical backbone, not path divergences.
