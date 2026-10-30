# Book 4 — Classification Report (RunC)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 16 | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13, 4.14, 4.15, 4.16 |
| Path difference (D) | 0 |  |
| AI proof error (E) | 0 |  |

**Total**: 16 propositions

## Per-Proposition Analysis

### 4.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: draw a diameter of the circle, handle the trivial case where the diameter equals the given line, and in the main case construct a segment equal to the given line from an endpoint of the diameter, draw a circle with that segment as radius centered at the endpoint, and show that the chord from the endpoint to the intersection point equals the given line via the definition of a circle. The AI proof explicitly cites elementary constructions and definitions (3.1 for finding the center, 1.3 for cutting off a segment, P1 and P3 for joining lines and drawing circles, D1.15 for the circle definition, D1.17 for diameter, D4.7 for fitting, and CN1 for transitivity of equality) while Heath's proof performs the same constructions and reasoning without explicit citations. Since heath_refs is empty, all AI citations appear in ai_only, but these are all construction propositions, postulates, definitions, and common notions representing over-citation of elementary steps rather than a different proof strategy. The backbones are identical, making this a granularity difference.

### 4.2
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: construct a tangent at a point on the circle (III.16), construct two angles equal to the given triangle's angles (I.23), join the chord, apply the alternate segment theorem (III.32) twice to establish two angle equalities, then use the angle sum property (I.32) to derive the third. The ai_only set consists entirely of common notions (CN1, CN3), a definition (D4.3), and a postulate (P1), which are foundational items Heath leaves implicit. The heath_only set is empty. Since the key intermediate conclusions are identical and the citation differences consist only of the AI over-citing axiomatic and definitional foundations, this is a granularity difference.

### 4.3
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct angles at center K equal to the exterior angles of the given triangle, draw tangent lines at the resulting points on the circle, then use quadrilateral angle sums and supplementary angle relationships (I.13) to show each vertex angle of the circumscribed triangle equals the corresponding angle of the given triangle, with I.32 closing the third angle. The heath_only citations (3.1 and 3.18) reflect citation-depth differences rather than backbone divergence: Heath explicitly cites III.1 to find the center while the AI takes the center as given, and Heath uses III.18 (radius perpendicular to tangent) after constructing tangents via III.16, whereas the AI reverses the approach by first constructing perpendiculars to radii via I.11 then citing III.16 to establish tangency. Both routes establish the same intermediate fact (right angles between radii and tangent lines). The ai_only citations (1.11, CN1, CN3, D4.4, P1, P2) are all construction steps, common notions, a definition, and postulates representing over-citation by the AI. The key intermediate conclusions are identical in both proofs.

### 4.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: bisect two angles of the triangle (I.9), drop perpendiculars from the intersection point to the three sides, use triangle congruence (I.26) to show all three perpendicular distances are equal, construct the circle, and invoke III.16 to establish tangency. The AI proof explicitly cites I.12 (perpendicular construction), P4 (right angles are equal), CN1 (transitivity of equality), and P3 (circle construction), all of which Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only construction propositions, postulates, and common notions, this is a clear Case A granularity difference where the AI over-cites foundational steps that Heath takes as understood.

### 4.5
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect two sides of the triangle, erect perpendicular bisectors at the midpoints, show via SAS congruence (I.4) that the intersection point F is equidistant from all three vertices, and conclude the circle centered at F passes through all vertices. The AI bisects AB and BC (rather than Heath's AB and AC), but this is merely a choice of which two sides to use and does not alter the logical structure. The ai_only set consists entirely of construction propositions (1.11), an additional justification for why perpendiculars meet (1.28), common notions (CN1), definitions (D1.15, D4.6), and postulates (P1, P3, P4) -- all items that Heath leaves implicit. The heath_only set is empty. The AI also provides a single unified argument rather than Heath's three separate cases, but both approaches validly establish FA=FB=FC. This is a clear case of same backbone with different citation depth.

### 4.6
**Category**: Granularity difference
**Jaccard**: 0.300
**Analysis**: Q2 decided the classification. Both proofs establish the same two key intermediate conclusions: (1) quadrilateral ABCD is equilateral and (2) ABCD is right-angled, then conclude it is a square by definition. Heath proves equilateral first using I.4 and right-angled second using III.31; the AI reverses the order but uses the same propositions for the same purposes. The ai_only set consists entirely of construction and foundational citations (1.11 for drawing the perpendicular, D1.15 and D1.17 for definitions of circle/diameter, P1 and P4 for postulates, CN1 for common notion, D4.3 for inscribed definition) that make the AI proof more explicit without changing the logical backbone. Heath_only is empty, confirming the AI cites a strict superset. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 4.7
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: drawing two perpendicular diameters, constructing tangent lines through the endpoints to form quadrilateral FGHK, establishing parallelism of opposite sides, proving the quadrilateral is equilateral, proving all angles are right, and concluding FGHK is a circumscribed square. The heath_only citations (1.30, 3.18) reflect minor route differences at the same logical positions: Heath uses 3.18 to derive perpendicularity from tangency while the AI constructs perpendiculars first via 1.11 and verifies tangency via 3.16, and Heath uses 1.30 for transitivity of parallels while the AI proves both parallel pairs directly via 1.28. The ai_only citations (1.11, 1.32, CN1, CN2, D1.15, D1.22, D4.4) are construction steps, definitions, common notions, and a detailed angle calculation that represent greater citation explicitness rather than a different logical path. The same key geometric facts are established at the same logical positions in both proofs, differing only in citation depth.

### 4.8
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: bisect two sides of the square, draw parallels through the midpoints to locate the center, use parallelogram properties (I.34) to show the four distances from the center to the midpoints are equal, construct the circle, and then invoke III.16 to show the circle touches rather than cuts each side. The key intermediate conclusions are identical in both proofs. The heath_only set is empty, meaning every citation Heath uses also appears in the AI proof. The ai_only set consists entirely of definitions (D1.22, D4.5), common notions (CN1), postulates (P1, P3, P4), and one additional proposition (1.29, used to explicitly justify perpendicularity of radii to sides via parallel lines). These are all instances of the AI citing foundational results that Heath leaves implicit, which is a citation-depth difference rather than a structural divergence.

### 4.9
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: join diagonals AC and BD at point E, use I.8 to show the diagonals bisect the corner angles of the square, then use I.6 to show all four segments EA, EB, EC, ED are equal (since the base angles in each sub-triangle are equal), and finally describe a circle with center E passing through all four vertices. The AI proof adds explicit citations for definitions (D1.22 for the square, D4.6 for circumscription), postulates (P1 for drawing lines, P3 for describing the circle), and a common notion (CN1 for transitivity of equality), all of which Heath leaves implicit. Since heath_only is empty and ai_only consists entirely of foundational items (definitions, postulates, common notions), this is a clear Case A: same backbone with the AI citing at greater depth.

### 4.10
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decides this as G (granularity difference). Both proofs share the same logical backbone: cutting AB at C via II.11, fitting BD = CA in circle BDE, circumscribing circle ACD, establishing BD is tangent to circle ACD, using the alternate segment theorem (III.32) to get angle BDC = angle DAC, then using angle sums (I.32), isosceles triangle properties (I.5), and I.6 to show each base angle of triangle ABD is double the vertex angle. The ai_only citations (4.1, P1, P3) are construction postulates and propositions that Heath uses implicitly. The AI cites 3.36 instead of Heath's 3.37, but the AI explicitly writes 'by the converse of the tangent-secant theorem,' demonstrating correct logical reasoning with merely a wrong proposition number label. Under the lenience rule this is not an error but a citation-depth difference. All key intermediate conclusions appear in both proofs at the same logical positions, making this Case A of Q2.
**Audit Record**: CANDIDATE E — 4.10
  violated_claim : BD touches circle ACD at D
  failure_mode   : invalid_inference
  missing_is     : expansion
  evidence       : AI Step 7 cites [3.36] but says 'by the converse of the tangent-secant theorem' - 3.36 is the direct theorem, 3.37 is the converse. The AI uses the correct logical direction but cites the wrong number.
  why_not_terse  : The cited proposition 3.36 is the forward direction, not the converse needed here. However, the AI text explicitly invokes the converse, making this a citation numbering error not a logical gap.
VERDICT: NOT-E. missing_is = expansion. The AI demonstrates correct reasoning (invoking the converse) but mislabels the proposition. Lenience rule applies: compressed-but-sound. Reclassified to G.

### 4.11
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct isosceles triangle FGH with base angles double the vertex angle (IV.10), inscribe an equiangular triangle ACD in the circle (IV.2), bisect the double angles (I.9) to obtain five equal inscribed angles, derive equal arcs (III.26), equal chords (III.29) for equilateral, and equal combined arcs yielding equal interior angles (III.27) for equiangular. The only citation difference is that the AI adds D4.3 (the definition of a polygon inscribed in a circle) to explicitly justify the final conclusion, while Heath leaves this implicit. Since heath_only is empty and ai_only contains only a definition, this is a classic over-citation granularity difference with identical backbone structure.

### 4.12
**Category**: Granularity difference
**Jaccard**: 0.467
**Analysis**: Q2 decided the classification as Granularity difference (G). Both proofs follow the same logical backbone: inscribe a regular pentagon (IV.11), draw tangents at each vertex (III.16/III.18), establish equal tangent segments from each external point using the Pythagorean theorem (I.47) and SSS congruence (I.8), prove congruence of triangles at adjacent vertices via AAS (I.26), and conclude the circumscribed pentagon is equilateral and equiangular. The citation differences are all matters of depth: the AI explicitly cites foundational items (CN1, CN2, D1.15, D4.4, P1) that Heath uses implicitly; the AI adds 3.28 (equal chords yield equal arcs) as an explicit intermediate step before applying 3.27, whereas Heath proceeds directly from the equal arcs established by IV.11; the AI uses 1.32 (angle sum of a triangle) for the equiangular conclusion where Heath achieves the same result through I.26 alone; and Heath cites 3.1 to find the center of the circle while the AI simply names the center and invokes D1.15 for equal radii. All key intermediate conclusions are present in both proofs at the same logical positions, making this a Case A granularity difference.

### 4.13
**Category**: Granularity difference
**Jaccard**: 0.273
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs share the same backbone: bisect angles BCD and CDE to locate center F, show all five perpendiculars from F to the sides are equal via I.26 triangle congruences, and use III.16 to establish that the circle with center F is inscribed. The AI proof over-cites by explicitly referencing construction propositions (I.9 for angle bisection, I.12 for perpendicular dropping), common notions (CN1, CN3), definitions (D1.10, D4.5), and a postulate (P3) that Heath leaves implicit. The one substantive ai_only citation, I.6, is used to explicitly establish FC = FD from equal base angles in triangle FCD, whereas Heath establishes the same fact implicitly through the I.4 congruence of triangles BCF and DCF. Heath_only is empty, confirming the AI cites a strict superset. All key intermediate conclusions are the same in both proofs, making this a citation-depth difference rather than a path difference.

### 4.14
**Category**: Granularity difference
**Jaccard**: 0.125
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: bisect angles BCD and CDE to find center F, show FC = FD via I.6 from equal base angles, extend to prove all five distances FA = FB = FC = FD = FE are equal, then circumscribe the circle. The AI proof explicitly works through each congruence step using I.4 (SAS) where Heath abbreviates with 'similarly it can be proved.' The ai_only set consists entirely of construction propositions (1.9), postulates (P1, P3), definitions (D1.15, D4.6), common notions (CN1), and the SAS congruence theorem (1.4) that Heath leaves implicit. The heath_only set is empty, confirming that the AI covers all of Heath's cited material. This is a clear Case A: same key intermediate conclusions with the AI providing finer-grained citation depth.

### 4.15
**Category**: Granularity difference
**Jaccard**: 0.357
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they construct the hexagon by drawing a circle with center D and radius DG, prove that certain triangles at the center are equilateral, establish that all six central angles equal one-third of two right angles, then use III.26 (equal central angles yield equal arcs), III.29 (equal arcs yield equal chords) for equilateral, and III.27 (equal arcs yield equal inscribed angles) for equiangular. The sole substantive difference is that Heath uses I.15 (vertical angles) to obtain three of the six central angles at once, while the AI instead applies I.13 (supplementary angles) repeatedly to derive each remaining central angle individually. The key intermediate conclusions are identical in both proofs; the difference is only in citation depth. The ai_only set consists of over-citations (definitions D1.15, D1.20, D4.3; postulates P1, P3; common notion CN2; construction step 3.1) plus 1.13 as a mechanical substitute for 1.15, all consistent with granularity rather than path divergence.

### 4.16
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: inscribe a side of the equilateral triangle (subtending 5/15 of the circumference) and a side of the regular pentagon (subtending 3/15), compute the remaining arc BC as 2/15, bisect it at E using 3.30 to obtain arcs of 1/15, then fit equal chords around the circle to produce the 15-gon. Heath's proof cites only 3.30 and leaves all other justifications implicit, while the AI explicitly cites 1.1, 4.2, 4.11, 3.28, 3.29, 3.30, 4.1, 3.27, and P1 — all of which are construction steps, supporting lemmas, or axioms that Heath uses implicitly. The heath_only set is empty, confirming no citations are missing from the AI. The AI also adds an explicit equiangularity argument (Step 10 via 3.27) that Heath simply asserts. This is a same-backbone, different-depth scenario: the AI over-cites by making explicit what Heath leaves implicit, yielding a granularity difference.
