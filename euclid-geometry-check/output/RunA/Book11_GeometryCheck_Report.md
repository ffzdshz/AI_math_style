# Book 11 — Geometry Configuration Check (RunA)

## Summary

**Total propositions checked**: 8

| Verdict | Count | Propositions |
|---|---|---|
| PASS | 6 | 11.7, 11.18, 11.26, 11.33, 11.36, 11.38 |
| FAIL | 2 | 11.29, 11.35 |
| SKIP | 0 |  |

## Detected Contradictions

### Proposition 11.29

**Contradictory steps**: Step 1, Step 3, Step 6

**Spatial claim 1** (Step 1): E, E', H, H' all lie on one straight line. This is the proposition's given condition: the extremities of the standing edges lie on two straight lines, and the proof assigns E, E', H, H' to one of them.
  - Required by: Setup of the proposition's geometric condition

**Spatial claim 2** (Step 3 and Step 6): EE'H'H is a parallelogram (Step 3), and the solid E,F,G,H,E',F',G',H' is a parallelepiped with all six faces being parallelograms (Step 6). Both claims require E,E',H,H' to be non-collinear so they form a proper 2D quadrilateral face.
  - Required by: Steps 3-4 use I.34 on these 'parallelograms'; Step 6 classifies the solid as a parallelepiped; Step 8 applies XI.28 (bisection by diagonal plane) to this 'parallelepiped'

**Contradiction**: The proof establishes in Step 1 that E, E', H, H' are collinear (all on one straight line), as required by the proposition's condition. In a parallelepiped, standing edges are translates of a single vector, so E=A+v1, H=D+v1, E'=A+v2, H'=D+v2. The collinearity condition forces v1-v2 to be parallel to D-A, placing all four points on one line. But four collinear points cannot form a parallelogram (which requires a 2D quadrilateral). Therefore EE'H'H is a degenerate line segment with zero area, not a parallelogram. Similarly FF'G'G is degenerate. Consequently, the solid in Step 6 has two degenerate 'faces' (zero-area line segments) and cannot be a parallelepiped, invalidating the application of XI.28 in Step 8. The proof conflates a degenerate configuration with a proper parallelepiped.

**Fixable**: True
  - Heath's proof avoids this error entirely by never constructing the auxiliary parallelepiped. Instead, Heath directly shows that the complementary prisms (triangular prisms formed by the difference between the two solids) are equal, using I.8, I.4, I.34, and I.36. The AI proof could be repaired by following this direct prism decomposition approach, or alternatively by correcting the point grouping so that the two straight lines contain {E,F,E',F'} and {H,G,H',G'} respectively (tops from adjacent base vertices on the same line), which would make EE'H'H a proper non-degenerate parallelogram.

### Proposition 11.35

**Contradictory steps**: Step 2 (H is projection of G onto P1, implicitly determining H's position), Step 9 (claims H is in interior of angle BAC and ray JI lies in interior of angle HJA)

**Spatial claim 1** (Step 2): H is the orthogonal projection of G onto plane P1. For asymmetric angle configurations (e.g., angle BAG=70, angle CAG=20, angle BAC=60), the direction AH in the plane makes angle ~69 degrees with AB, placing H outside angle BAC (past line AC).
  - Required by: Construction of the perpendicular foot, used throughout Steps 3-13

**Spatial claim 2** (Step 9): Both H and I are in the interior of angle BAC on the same side of line AB, and ray JI lies in the interior of the right angle HJA, so angle HJA = angle HJI + angle IJA.
  - Required by: Derivation of angle HJI = 90 - angle AJI, leading to angle HJI = angle KLN in Step 9, and triangle congruence in Step 11

**Contradiction**: For valid asymmetric configurations (e.g., angle BAC=60, angle BAG=70, angle CAG=20, which satisfies the spherical triangle inequality |70-20|=50 <= 60 <= 90), coordinate analysis shows: (1) H falls at angle 69 degrees from AB, which is OUTSIDE angle BAC (past line AC at 60 degrees), falsifying the claim that H is in the interior of angle BAC. (2) At point J, the ray JI is at 81 degrees, JH is at 90 degrees, and JA is at 180 degrees from the positive x-axis. Since JI (81) is on the opposite side of JH (90) from JA (180), ray JI does NOT lie in the interior of angle HJA. The correct decomposition is angle IJA = angle IJH + angle HJA (not angle HJA = angle HJI + angle IJA). Additionally, I lies ON line AC (not in the interior of angle BAC as claimed). The step's conclusion (angle HJI = angle KLN) happens to survive because the same configuration issue applies symmetrically to both angle systems, but the stated reasoning and spatial claims are invalid.

**Fixable**: True
  - Heath's proof avoids this issue entirely by using Proposition I.8 (SSS triangle congruence) for the final step rather than angle decomposition, never requiring H to lie inside angle BAC or ray JI to lie inside angle HJA. Alternatively, the AI proof could be fixed by: (1) handling both cases (JI inside or outside angle HJA) separately, noting that either way angle HJI = |90 - angle AJI|, and by symmetry the same formula applies to angle KLN; or (2) replacing the angle decomposition approach in Steps 9-11 with a direct distance-based argument using I.47 and I.8 as Heath does.

## Passed Propositions

- **11.7**: All spatial claims are mutually consistent. Every object (lines AB, CD, points E, F, line EF) is placed in the same plane P, and no claim contradicts any other. The proof involves no angle decompositions, no inside/outside arguments, and no competing plane assignments. The difference from Heath (using 11.1 instead of 11.3) is a logical strategy choice, not a spatial configuration contradiction.
- **11.18**: All spatial claims are mutually consistent. The proof correctly uses AB perpendicular to P to derive perpendicularity of AB to both CE and AG (lines in P through A). It then correctly applies 11.4 to conclude AG is perpendicular to Q (since AG is perpendicular to two intersecting lines in Q). Finally D11.4 is correctly applied to conclude P perpendicular to Q. No angle decomposition issues arise; the proof uses only right-angle perpendicularity relationships. The unused point F is a minor style issue but introduces no spatial contradiction.
- **11.26**: All spatial claims are mutually consistent. The three face angles KAH = EDC, KAL = EDF, and HAL = CDF can coexist simultaneously at vertex A: H is placed in the plane of AB, and L is placed in a different half-plane through AK with dihedral freedom allowing angle HAL to equal angle CDF. The conditions of 11.23 (any two face angles greater than the third, sum less than four right angles) are inherited from the original solid angle at D via 11.20 and 11.21. The triangle congruences (I.4, I.8) establishing edge equalities are straightforward SAS/SSS results with no conflicting spatial requirements. The solid angle is correctly positioned at A with edge AK along AB.
- **11.33**: All spatial constructions are mutually consistent. The auxiliary solid CD-prime is well-defined with base equal to that of CD and height edge AH preserving the vertex angles. The equal-height claim for AB and CD-prime is justified by the similarity of AB and CD (equal vertex angles ensure equal perpendicular heights when both have edge AH). The ratio chain through XI.25, XI.32, VI.22, and V.22 is sound. The unused constructions S1 and S2 are inelegant but introduce no spatial contradictions. No angle decomposition issues, no inside/outside contradictions, and no plane membership conflicts are present.
- **11.36**: The proof is primarily proportional/ratio-based reasoning about equiangular parallelepipeds. While Steps 3 and 6 contain imprecise metric claims (Step 3 gives a muddled justification for the same-height condition, Step 6 equates edge lengths with perpendicular heights), these are errors in individual step explanations rather than spatial configuration contradictions between steps. All ratio conclusions are correct: base(S):base(T) = A:B via areas, height(T):height(S) = B:C via the common sin factor canceling. No two spatial claims about the same geometric entity are mutually inconsistent. The application of 11.34 (converse) to equiangular solids with reciprocally proportional bases and heights is valid.
- **11.38**: All spatial claims are mutually consistent. The cube labeling, midpoint positions, collinearity arguments (K-S-M and L-S-N via midline theorem), plane membership claims (S and T on both cutting planes), the identification of ST as common section, the construction of parallelogram ACGE, the sub-parallelogram ASGT, and the diagonal bisection of AG and ST are all verified to be geometrically correct and pairwise compatible. Coordinate verification confirms every claim: the two cutting planes are x=0.5 and y=0.5 respectively, their common section is ST, and the diagonals AG and ST of parallelogram ASGT meet at (0.5,0.5,0.5), bisecting each other.
