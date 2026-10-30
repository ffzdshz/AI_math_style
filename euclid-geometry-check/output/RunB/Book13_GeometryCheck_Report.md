# Book 13 — Geometry Configuration Check (RunB)

## Summary

**Total propositions checked**: 12

| Verdict | Count | Propositions |
|---|---|---|
| PASS | 10 | 13.1, 13.2, 13.6, 13.7, 13.8, 13.9, 13.10, 13.11, 13.13, 13.18 |
| FAIL | 2 | 13.16, 13.17 |
| SKIP | 0 |  |

## Detected Contradictions

### Proposition 13.16

**Contradictory steps**: Step 12, Step 13, Step 22

**Spatial claim 1** (Step 12 and Step 13): The separation between the two pentagonal planes equals s₁₀, the side of the decagon inscribed in a circle of radius r
  - Required by: Step 12's assertion that lateral edges equal s₅ with this plane separation

**Spatial claim 2** (Step 22): The separation between the two pentagonal planes d = r, the radius of the circle in which the pentagons are inscribed
  - Required by: The circumsphere condition derived in Step 20 (s₁₀² + s₁₀·d = r²) combined with the golden ratio property from Prop. 13.9 (s₁₀² + s₁₀·r = r²)

**Contradiction**: Steps 12-13 assert the inter-plane distance d = s₁₀ (the decagon side), while Step 22 derives d = r (the circle radius). Since s₁₀ = r(√5-1)/2 ≈ 0.618r, these values are not equal. Moreover, Step 12's claim that d = s₁₀ produces equilateral lateral triangles is false: with d = s₁₀ the lateral edge² = s₁₀² + s₁₀² = 2s₁₀², but the required value is s₅² = r² + s₁₀² (by Prop. 13.10), and 2s₁₀² ≠ r² + s₁₀² since r ≠ s₁₀. Only d = r gives the correct lateral edge length. The proof asserts two mutually inconsistent positions for the pentagonal planes.

**Fixable**: True
  - Remove the incorrect claim in Steps 12-13 that d = s₁₀. The correct derivation in Steps 20-22 showing d = r should be retained and presented as the initial determination of the plane separation, not as a post-hoc correction. Heath's proof avoids this issue entirely by constructing perpendiculars of length r (= radius = hexagon side) from each pentagon vertex, which directly establishes the inter-plane distance as r.

### Proposition 13.17

**Contradictory steps**: Steps 11-12, Step 16

**Spatial claim 1** (Steps 11-12): The 12 non-cube-vertex vertices of the dodecahedron are golden-section division points located ON the edges of the cube (between midpoints and vertices of cube edges)
  - Required by: The entire construction in Steps 2-8 which places all dodecahedron vertices on cube edges or at cube vertices

**Spatial claim 2** (Step 16): All 20 vertices including the 12 golden-section edge points are equidistant from center O at distance d/2, lying on the circumscribing sphere
  - Required by: The conclusion in Step 16 that the dodecahedron is comprehended in the sphere

**Contradiction**: If a point K lies on an edge of the cube (between two cube vertices), it is strictly closer to the center O than the cube vertices are. Direct computation: for K on edge AB at the golden-section position, OK^2 = (s/2 - g)^2 + (s/2)^2 + (s/2)^2. Since 0 < g < s/2, we have (s/2 - g)^2 < (s/2)^2, so OK^2 < 3(s/2)^2 = d^2/4. Therefore K lies strictly inside the circumsphere, contradicting the claim that OK = d/2. The proof's assertion in Step 16 that OK^2 = (s/2)^2 + (s/2)^2 + (s/2)^2 is false -- it silently replaces (s/2 - g) with s/2 in the first coordinate. The fundamental error is that the construction places all vertices on the cube's edges, but a dodecahedron inscribed in the same sphere as the cube necessarily has vertices OUTSIDE the cube (raised above its faces).

**Fixable**: True
  - Heath's construction avoids this by erecting perpendicular segments from the cube faces outward (RU, SV, TW at right angles to the planes of the cube towards the outside), placing the 12 additional vertices outside the cube rather than on its edges. This is the correct geometric construction: the dodecahedron vertices that are not cube vertices must be raised above the cube faces, not confined to its edges.

## Passed Propositions

- **13.1**: The proof is essentially algebraic, manipulating squares and rectangles of line segments using Propositions 2.1, 2.4, and 6.17. The only spatial claims are that C and D both lie on segment AB in the order A-D-C-B, which is trivially consistent. There are no angle decompositions, no interior/exterior point arguments, no ray orderings, and no circle arguments — nothing that could create a spatial configuration contradiction.
- **13.2**: The proof is essentially algebraic, working with equalities of squares of lengths. The spatial configuration is minimal: two line segments each with one interior point, with no complex geometric constructions, no angle decompositions, no interior/exterior arguments, and no circle-based reasoning. All spatial claims (two betweenness claims and one segment construction) are independently established, trivially consistent, and never interact in a way that could produce contradiction.
- **13.6**: The proof is essentially algebraic, working with lengths, squares of lengths, and commensurability relations from Book 10. The only spatial claims concern the positions of C and D on line AB and the positivity of constructed lengths, all of which are trivially consistent. There are no angle decompositions, no interior/exterior point arguments, no circle configurations, and no complex geometric constructions that could harbor hidden contradictions.
- **13.7**: All spatial claims are mutually consistent for a convex equilateral pentagon. The proof makes extensive use of angle decompositions by diagonals (AC, BD, DA, CE, BE), and in every case the diagonal passes through the pentagon interior, correctly entering the interior of the relevant angle at the vertex. Triangle congruences are properly set up with correct side-angle correspondences. No point is placed in contradictory positions across different steps, and no angle decomposition conflicts with any other. The proof handles both consecutive and non-consecutive cases with consistent geometry throughout.
- **13.8**: All spatial claims are mutually consistent. The two critical angle decompositions (Step 7: angle HBC = angle ABC - angle ABH; Step 9: angle HAE = angle EAB - angle BAC) are both valid because the dividing rays genuinely lie between the outer rays in the regular pentagon configuration. The vertical angle claim at H is correct since A-H-C and B-H-E are collinear triples. The four angles at H sum to 360 degrees. All distance relationships (AH = BH, HC = HE = AB) are consistent with each other and with the segment additions AC = AH + HC, BE = BH + HE. Coordinate verification confirms all angle values and the golden ratio division.
- **13.9**: The proof's spatial claims are minimal and mutually consistent. The only geometric construction is the standard isosceles triangle OAB (36-72-72) formed by the circle center and two adjacent decagon vertices, which is correctly identified as the 4.10 triangle. There are no interior/exterior point claims, no angle decompositions, and no betweenness claims. The bulk of the reasoning is algebraic, applying ratio properties (EMR from 4.10 and the extension property from 13.5). All spatial claims are standard results about inscribed regular polygons and are pairwise compatible.
- **13.10**: All spatial claims are mutually consistent. The collinearity of O, M, N with M between O and N is geometrically correct for the perpendicular bisector of a non-diametral chord. Both right angles at M are valid since OM and MN lie along the same perpendicular to AB. The application of 13.9 is correct. After establishing the geometric setup, the proof proceeds through valid algebraic manipulations to reach s^2 = h^2 + d^2.
- **13.11**: The proof makes only minimal spatial claims (three standard regular polygons inscribed in the same circle) which are mutually consistent. The bulk of the argument is algebraic: expressing the square on the pentagon side as a rectangle on a rational line, then classifying the breadth as a fourth apotome via Book 10 machinery. No angle decompositions, interior/exterior point claims, ray orderings, or betweenness claims are made. All cited geometric results (4.15, 13.1, 13.6, 13.9, 13.10) are standard and correctly applied. No spatial configuration contradiction exists.
- **13.13**: All spatial claims are mutually consistent. The proof's construction (perpendicular plane at C, circle in that plane, equilateral triangle DEF, apex A at diameter endpoint) is geometrically clean. Every perpendicularity claim derives from the single fact that the plane through C is perpendicular to AB. All distance computations (AD=DE, AE=AF=AD, OD=OA) follow correctly from right triangles at C. No angle decomposition issues arise since the proof uses no additive angle decompositions. No point is claimed to be in contradictory positions across different steps.
- **13.18**: The proof is predominantly algebraic/proportional. Its only spatial claims are trivial collinear point placements on the diameter AB (C at 2/3 from A, D at midpoint), which are mutually consistent. No angle decompositions, no interior/exterior claims, no ray orderings, and no complex spatial configurations appear. All substantive work is ratio arithmetic using results from 13.13-13.17.
