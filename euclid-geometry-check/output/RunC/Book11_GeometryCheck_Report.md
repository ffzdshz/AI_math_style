# Book 11 — Geometry Configuration Check (RunC)

## Summary

**Total propositions checked**: 11

| Verdict | Count | Propositions |
|---|---|---|
| PASS | 10 | 11.7, 11.18, 11.19, 11.23, 11.32, 11.33, 11.35, 11.36, 11.37, 11.38 |
| FAIL | 1 | 11.31 |
| SKIP | 0 |  |

## Detected Contradictions

### Proposition 11.31

**Contradictory steps**: Step 3 (first collinearity claim), Step 3 (second collinearity claim), Step 6, Step 7

**Spatial claim 1** (Step 3): E, F, K, L are collinear (EF and KL on the same straight line), with E and K as distinct points (vertices of different parallelogram bases)
  - Required by: Steps 6-7: construction of combined parallelogram EKNT and connecting region FKLG

**Spatial claim 2** (Step 3): E, H, K, N are collinear (EH and KN on the same straight line), with EFGH a non-degenerate parallelogram (so EF and EH are not parallel, meaning the two lines l1 and l2 are distinct)
  - Required by: Steps 6-7: construction of combined parallelogram EKNT spanning both bases

**Contradiction**: Since EFGH is a non-degenerate parallelogram, its adjacent sides EF and EH are not parallel, so line l1 (through E,F,K,L) is distinct from line l2 (through E,H,K,N). Two distinct lines in a plane intersect in at most one point. E lies on both lines, making E the unique intersection. K is also claimed to lie on both lines, forcing K = E. With K = E: (1) the combined parallelogram EKNT degenerates (two vertices coincide); (2) the connecting region FKLG = FELG is not a parallelogram since FE is along l1 while FG is parallel to EH along l2; (3) the entire complement technique of Steps 6-8 breaks down. The double-collinearity configuration is geometrically impossible for distinct non-degenerate parallelogram bases.

**Fixable**: False
  - The AI proof's additive/subtractive complement technique inherently requires both pairs of adjacent sides to be collinear, which is impossible. Heath's proof avoids this by placing only one pair of sides collinear, constructing the second direction via angle construction (I.23), and using proportion theory (V.7, V.9, V.11 combined with XI.25) instead of the complement technique. The proof would need to be fundamentally restructured to follow Heath's proportion-based approach rather than the impossible complement-based approach.

## Passed Propositions

- **11.7**: All spatial claims in the proof concern plane membership and are mutually consistent. The chain of reasoning (parallel lines share a plane P; points on those lines are in P; a line with both endpoints in P lies entirely in P by 11.1) involves no contradictory geometric configurations. There are no angle decompositions, interior/exterior point arguments, or complex constructions that could introduce inconsistency.
- **11.18**: All spatial claims are mutually consistent. The configuration of a line AB perpendicular to plane P at foot A, a plane Q through AB intersecting P along line CE through A, and the perpendicularity of AB to CE is geometrically coherent. No angle decompositions, no interior/exterior conflicts, no betweenness issues arise. The proof directly applies D11.4 using AB itself as the witness line, which is spatially valid since AB lies in Q, is perpendicular to CE, and is perpendicular to P.
- **11.19**: All spatial claims are mutually consistent. The proof constructively shows that the unique perpendicular EK to plane P from E must lie in both planes AB and CD (via D11.4 and 11.13 applied independently), and therefore coincides with their common section EF. No angle decomposition, no inside/outside claims, and no ray-betweenness issues arise. Each geometric object maintains a consistent position across all steps.
- **11.23**: All spatial claims are mutually consistent. The proof does not perform any problematic angle decomposition -- the key relationship (angles around O summing to 360 degrees) is a fundamental property of angles around a point, not a decomposition of a single angle. The construction of R above the plane is geometrically valid: OR perpendicular to the plane ensures right angles with all radii, making the Pythagorean theorem applications correct. The SSS congruences (I.8) establishing the face angles are sound given RL = RM = RN = AB and the matching bases. The contradiction argument proving OL less than AB is logically valid. All three cases for O's position are addressed without spatial contradictions.
- **11.32**: The proof is a standard Eudoxian proportion argument (D5.5 method) with straightforward spatial content: juxtaposition of parallelogram bases, construction of parallelepipeds of the same height, and cutting by planes parallel to opposite faces. All spatial claims are mutually consistent. There are no angle decompositions, no interior/exterior point claims, and no betweenness claims that could conflict. The geometric heavy lifting is correctly delegated to 11.25 and 11.31.
- **11.33**: The proof makes no angle decomposition claims, no interior/exterior point claims, and no betweenness claims that could conflict. All spatial content involves constructing parallelepipeds with specific edge lengths (preserving edge directions) and comparing volumes by varying one dimension at a time. Applications of 11.25 (same base, ratio of heights) and 11.32 (same height, ratio of bases) are each applied to pairs of solids that genuinely share the required common element with the same edge directions. The identification AO = AB in Step 21 is valid because both are similar and similarly situated to CD on the same edge AE with the same solid angle. No pairwise contradiction exists among the spatial claims.
- **11.35**: All spatial claims are mutually consistent. The proof makes extensive perpendicularity and point-position claims in 3D, but each is compatible with the others. The 11.4 application (deriving HK perp AB and HJ perp AC from the perpendicularity of GH to the plane) is geometrically valid. The determination of H as the unique point satisfying two perpendicular conditions is correct. The chain of triangle congruences (AKG to DLM, AJG to DQM, AKJ to DLQ, GAH to MDN) is internally consistent, with no contradictory positional requirements on any point. No angle decomposition issues arise since the proof relies entirely on triangle congruences and Pythagorean relations rather than angle sums.
- **11.36**: The proof is primarily algebraic/proportional, comparing parallelepipeds through edge ratios, base area ratios, and volume ratios. All spatial claims are mutually consistent: both solids share the same solid angle, the base/height decomposition uses corresponding edge positions in both solids, the height equality follows from equal edge lengths in the same angular direction, and all cited propositions (11.26, 11.31, 11.32, 6.1, 6.16) are applied in configurations consistent with their requirements. No spatial configuration contradiction exists.
- **11.37**: The proof is a proportion/ratio argument throughout. Parallelepipedal solids appear but are treated purely through their ratio properties via 11.33 (triplicate ratio) and 11.27 (construction of similar solids). No spatial configuration claims are made — no point positions, angle decompositions, betweenness claims, plane memberships, or inside/outside assertions. All claims (solid similarity, ratio relationships, solid equality) are mutually consistent.
- **11.38**: All spatial claims are mutually consistent. The cube configuration, midpoint positions, parallelogram formations (KOQM and LPRN), plane intersections, and the key claim that the common section ST and diagonal AG bisect each other at the cube's center (0.5,0.5,0.5) are all verified to be geometrically correct. Coordinate verification confirms every parallelism, equality, bisection, and plane membership claim. The proof is verbose in Steps 20-22 but contains no spatial contradictions.
