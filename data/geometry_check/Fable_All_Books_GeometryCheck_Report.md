# Fable — Geometry Configuration Check Report (All Books)

## Overall Summary

**Total propositions checked**: 34  
**Run**: Fable (Claude Fable 5.1)

| Verdict | Count | Propositions |
|---|---|---|
| PASS | 23 | 2.7, 2.8, 3.9, 3.16, 4.9, 4.12, 4.14, 6.20, 6.22, 6.23, 6.30, 6.31, 10.29, 10.48, 10.113, 11.37, 12.16, 13.1, 13.2, 13.4, 13.5, 13.7, 13.12 |
| FAIL | 0 | — |
| SKIP | 11 | 5.1, 5.18, 7.27, 7.33, 8.5, 8.21, 8.22, 9.11, 9.19, 10.39, 10.91 |

**No geometric configuration contradictions detected.**

## Per-Book Summary

| Book | Total | PASS | FAIL | SKIP |
|---|---|---|---|---|
| 2 | 2 | 2 | 0 | 0 |
| 3 | 2 | 2 | 0 | 0 |
| 4 | 3 | 3 | 0 | 0 |
| 5 | 2 | 0 | 0 | 2 |
| 6 | 5 | 5 | 0 | 0 |
| 7 | 2 | 0 | 0 | 2 |
| 8 | 3 | 0 | 0 | 3 |
| 9 | 2 | 0 | 0 | 2 |
| 10 | 5 | 3 | 0 | 2 |
| 11 | 1 | 1 | 0 | 0 |
| 12 | 1 | 1 | 0 | 0 |
| 13 | 6 | 6 | 0 | 0 |
| **Total** | **34** | **23** | **0** | **11** |

## Detected Contradictions

None.

---

## Book 2 (2 propositions: PASS 2, FAIL 0, SKIP 0)

- **2.7** — PASS: The proof is purely algebraic, manipulating area equalities from previously proven propositions (2.3 and 2.4) via Common Notions. It makes no spatial configuration claims beyond the given premise (C on AB). With no geometric constructions, no angle decompositions, no inside/outside claims, and no ray orderings, there is nothing that could produce a spatial contradiction.
- **2.8** — PASS: The proof's spatial claims are limited to collinear point positions on a single line (A-C-B-D with BD=CB), all trivially and mutually consistent. The core reasoning is purely algebraic manipulation of area identities from Propositions 2.4 and 2.7, with no angle decompositions, no inside/outside claims, no ray orderings, and no opportunity for spatial configuration contradictions.

## Book 3 (2 propositions: PASS 2, FAIL 0, SKIP 0)

- **3.9** — PASS: All spatial claims are mutually consistent. D is inside the circle and on diameter FG (since line DE through the centre is extended to the circumference). The application of 3.7 to point D on diameter FG (not the centre) is geometrically valid. The reductio correctly derives a contradiction between 3.7's conclusion (at most two equal lines from D to the circle) and the hypothesis (three equal lines). No angle decompositions, no interior/exterior conflicts, no conflicting point positions.
- **3.16** — PASS: All spatial claims are mutually consistent. The proof carefully tracks point positions relative to the circle (D inside, G outside, H on circumference between D and G) and angle orderings (DAF < right, DAG < right, AGD = right). The Step 8 argument correctly establishes G on ray FA rather than beyond A. Contradictions arising in the reductio arguments (Parts 1 and 2) are intentional consequences of the false assumptions, not proof errors. The Part 3 direct argument using I.23 and 3.2 is a legitimate alternative to Heath's reductio approach, with sound spatial reasoning throughout.

## Book 4 (3 propositions: PASS 3, FAIL 0, SKIP 0)

- **4.9** — PASS: The proof makes straightforward spatial claims about the intersection of diagonals of a square and uses SAS congruence (I.4) and isosceles triangle properties (I.6) in a standard, correct manner. No angle decomposition is performed, avoiding the primary error pattern. All spatial claims — E on both diagonals, the SAS congruences of adjacent triangles, the angle re-labelings, and the equal distance conclusions — are mutually consistent throughout.
- **4.12** — PASS: All spatial claims are mutually consistent. The tangent-chord angle theorem (III.32) is correctly applied at each vertex: the alternate segments are correctly identified (the segment on the far side of the chord from the external tangent intersection point, containing the appropriate inscribed pentagon vertices). Equal arcs from the regular inscribed pentagon correctly yield equal inscribed angles via III.27/III.21. The ASA congruences chain correctly to establish all ten half-segments equal. No angle decomposition errors or point position contradictions exist.
- **4.14** — PASS: All spatial claims are mutually consistent. F inside the pentagon is geometrically correct for the intersection of adjacent angle bisectors. Each angle decomposition (at vertices B and E in Steps 4 and 6) correctly relies on the ray to F being interior to the vertex angle, which follows from F being inside the pentagon. All four SAS congruences are properly set up. The chain of radius equalities is valid.

## Book 5 (2 propositions: PASS 0, FAIL 0, SKIP 2)

- **5.1** — SKIP: Book 5 is proportions theory. Proposition 5.1 proves that if AB = n*CD and AE = n*CF, then the remainder EB = n*(remainder FD). The proof is purely algebraic, manipulating abstract magnitudes via Common Notions and Definition 5.2 (multiples). No geometric spatial claims are made.
- **5.18** — SKIP: Book 5 proposition dealing entirely with proportions theory. The proof reasons about abstract magnitudes and their equimultiples using Definition 5.5, with no geometric spatial claims.

## Book 6 (5 propositions: PASS 5, FAIL 0, SKIP 0)

- **6.20** — PASS: All spatial claims are mutually consistent. The diagonal decompositions from a single vertex of each convex polygon are standard constructions. The angle subtractions at B, C (and correspondingly G, H) are valid because the diagonals lie within the respective interior angles of the convex polygons. The ratio arguments in Steps 12-16 are purely proportional with correctly identified corresponding sides in the similar triangles. No configuration contradiction exists.
- **6.22** — PASS: The proof is entirely ratio-theoretic, using Book V proportion theory (5.7-5.13, 5.22) and previously established results about duplicate ratios of similar figures (6.19, 6.20, D5.9). No spatial configuration claims are made.
- **6.23** — PASS: All spatial claims are mutually consistent. The construction is a standard placement of equiangular parallelograms at a shared vertex C, with sides BC-CG made collinear and D-C-E proved collinear via supplementary angles and I.14. The bridging parallelogram DCGH correctly shares a base line and height with each original parallelogram, enabling two valid applications of VI.1. No angle decompositions, no inside/outside point-position claims, and no betweenness contradictions arise.
- **6.30** — PASS: The proof makes only trivial spatial claims (C lies on segment AB) and proceeds entirely through algebraic/proportional reasoning (2.11 for construction, 6.17 for proportion, 5.14 for magnitude comparison, CN5 for part-whole). No angle decompositions, no inside/outside claims, no ray orderings, no circle arguments.
- **6.31** — PASS: All spatial claims are mutually consistent. The proof uses a single standard construction (altitude from right-angle vertex to hypotenuse) producing an unambiguous configuration. The similarity relationships, corresponding-side identifications, and area decomposition all follow correctly. No angle decompositions, no inside/outside ambiguities, and no conflicting point positions arise.

## Book 7 (2 propositions: PASS 0, FAIL 0, SKIP 2)

- **7.27** — SKIP: Book 7 is number theory with no spatial configuration. Proposition 7.27 is purely about coprimality of products of numbers.
- **7.33** — SKIP: Book 7 is number theory. Proposition 7.33 (finding least numbers in the same ratio) is purely arithmetic.

## Book 8 (3 propositions: PASS 0, FAIL 0, SKIP 3)

- **8.5** — SKIP: Book 8 is number theory with no spatial configuration. Proposition 8.5 concerns plane numbers and the ratio compounded of the ratios of their sides.
- **8.21** — SKIP: Book 8 is number theory. Proposition 8.21 proves that numbers with two mean proportionals are similar solid numbers.
- **8.22** — SKIP: Book 8 is number theory. Proposition 8.22 proves that if three numbers are in continued proportion and the first is square, the third is also square.

## Book 9 (2 propositions: PASS 0, FAIL 0, SKIP 2)

- **9.11** — SKIP: Book 9 is number theory with no spatial configuration. Proposition 9.11 is purely arithmetic, concerning measurement relationships among numbers in continued proportion.
- **9.19** — SKIP: Book 9 is number theory. Proposition 9.19 is purely about numerical proportions and divisibility.

## Book 10 (5 propositions: PASS 3, FAIL 0, SKIP 2)

- **10.29** — PASS: The proof's geometric content is limited to a single right triangle ABF with the right angle at B. The perpendicularity claim and the Pythagorean theorem application are mutually consistent and standard. All remaining reasoning is algebraic ratio manipulation and number-theoretic arguments about commensurability. No angle decompositions, no inside/outside claims, no betweenness claims, and no conflicting spatial configurations exist.
- **10.48** — PASS: The proof is fundamentally algebraic/proportional, constructing a binomial line by transferring commensurability properties through a fourth proportional. The only spatial element is the trivial collinear arrangement E-F-G, which is used consistently throughout.
- **10.113** — PASS: All spatial claims are mutually consistent. The geometry is limited to collinear point arrangements whose relative positions are straightforward and never conflict. The core argument is algebraic/proportional, with no angle decompositions, no interior/exterior claims, and no complex spatial configurations.
- **10.39** — SKIP: Purely algebraic proof about commensurability of magnitudes. No geometric configuration reasoning is involved beyond trivial collinearity.
- **10.91** — SKIP: The proof is purely algebraic/proportional, dealing with commensurability relations. All spatial claims are trivial collinear point placements on line segments.

## Book 11 (1 proposition: PASS 1, FAIL 0, SKIP 0)

- **11.37** — PASS: The proof is overwhelmingly proportional/algebraic. Its few spatial claims (similarity of parallelepipedal solids, corresponding sides, construction of a similar solid via 11.27, transitivity of face similarity via 6.21) are all mutually consistent. No angle decompositions, interior/exterior arguments, betweenness claims, or point-position claims are present.

## Book 12 (1 proposition: PASS 1, FAIL 0, SKIP 0)

- **12.16** — PASS: All spatial claims are mutually consistent. The proof carefully tracks point positions (G between K and D, G between A and C, L on arc AD between A and D), correctly establishes ray orderings (KL within angle AKD, KD within angle AKC), properly applies the hinge theorem (1.24) to deduce LD less than AC, and correctly derives the distance inequality KO greater than KG ensuring every point of the inscribed polygon lies outside the lesser circle. No angle decomposition errors or point position contradictions are present.

## Book 13 (6 propositions: PASS 6, FAIL 0, SKIP 0)

- **13.1** — PASS: The proof is essentially algebraic, using Book II area identities applied to segments on a single straight line. The only spatial claims concern the collinear ordering of points and segment equalities, all of which are mutually consistent. No angle decompositions, no inside/outside claims, no triangle or circle constructions are involved.
- **13.2** — PASS: The proof operates on points along a single line with a simple ordering A-C-E-B-D. All spatial claims concern collinearity and betweenness, and they are mutually consistent. The critical betweenness claim is formally proved before being used.
- **13.4** — PASS: The proof is almost entirely algebraic, working with segment identities and a proportional relationship applied to a single line AB cut at point C. The only spatial configuration is used consistently and without contradiction throughout all steps.
- **13.5** — PASS: The proof is a chain of Book 5 proportion manipulations applied to segments on a single line. The only spatial claims are trivial collinearity and betweenness facts that are given in the setup and mutually consistent.
- **13.7** — PASS: All spatial claims are mutually consistent. The six angle decomposition claims each assert that a diagonal falls within an interior angle of the convex pentagon, which is guaranteed by convexity. The ray orderings at each vertex confirm every additive decomposition is valid. All triangle congruences use correct side-angle correspondences.
- **13.12** — PASS: All spatial claims are mutually consistent. The proof establishes BE = DE through a valid chain of angle calculations. No angle decomposition errors or point position contradictions are present.
