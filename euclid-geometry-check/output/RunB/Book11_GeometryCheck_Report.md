# Book 11 — Geometry Configuration Check (RunB)

## Summary

**Total propositions checked**: 10

| Verdict | Count | Propositions |
|---|---|---|
| PASS | 9 | 11.6, 11.7, 11.26, 11.31, 11.33, 11.34, 11.35, 11.36, 11.38 |
| FAIL | 1 | 11.29 |
| SKIP | 0 |  |

## Detected Contradictions

### Proposition 11.29

**Contradictory steps**: Step 1, Step 17

**Spatial claim 1** (Step 1): CM and CN are general parallelepipeds on base ABCD satisfying the collinearity condition. Their translation vectors v and w satisfy w = v + t*AB but are NOT required to be parallel (v not parallel to w in general).
  - Required by: The hypothesis of the proposition; establishes the generality of the configuration

**Spatial claim 2** (Step 17): The solid ABCD-EF'G'H (with standing edges AE from CM and BF' from CN) is a parallelepiped. This implicitly requires AE || BF', i.e., v || w.
  - Required by: Application of Proposition 11.28 in Step 18 to decompose the auxiliary solid into prisms, which is essential for the chain CM = auxiliary solid = CN in Steps 29-31

**Contradiction**: The auxiliary solid ABCD-EF'G'H has standing edges AE = v (from CM) and BF' = w (from CN). For it to be a parallelepiped, all six faces must be parallelograms, which requires AE || BF' (i.e., v || w). But the hypothesis only constrains w = v + t*AB (from collinearity), which does NOT imply v || w unless v happens to be parallel to AB (a degenerate case). In a general oblique parallelepiped, v is not parallel to AB, so AE is not parallel to BF', face ABF'E is not a parallelogram, and the auxiliary solid is not a parallelepiped. A concrete counterexample with v=(0.5,0,1) and w=(0.8,0,1) confirms this: both parallelepipeds satisfy all hypotheses but ABF'E has non-parallel opposite sides.

**Fixable**: True
  - Heath's proof avoids this entirely by using a direct subtraction/addition approach: showing triangles DCE = HBK (by I.8, I.4), parallelograms DG = HN (by I.36), and then adding equal prisms to reach CM = CN. The AI's strategy of constructing an auxiliary parallelepiped is fundamentally flawed because the solid ABCD-EF'G'H is not a parallelepiped in general. A correct proof must use Heath's approach or an equivalent one that does not require this false intermediate construction.

## Passed Propositions

- **11.6**: All spatial claims are mutually consistent. The perpendicularity relationships, plane memberships, and the Pythagorean derivation chain are geometrically valid. The identification of angles ABD and BDC as alternate angles is valid for the configuration where A and C are on opposite sides of plane P (a legitimate case for the proposition). Even if interpreted as co-interior angles (same side), both equal 90 degrees and parallelism follows. No spatial configuration contradiction exists.
- **11.7**: All spatial claims concern plane membership and are mutually consistent. The key argument (P = Q via shared non-collinear points H, E, F) is valid. There are no angle decompositions, no interior/exterior point arguments, and no contradictory betweenness or ray-ordering claims. The abandoned contradiction attempt in Steps 3-5 introduces no binding claims used in the final proof.
- **11.26**: All spatial claims are mutually consistent. The proof constructs point P in plane BAL as the counterpart of G in plane DFC, using perpendicular feet and distance equalities. The key spatial requirements (G in interior of angle FDC, P in interior of angle BAL, correct perpendicularity relationships for the plane-to-plane arguments) are all satisfied. The angle decomposition in Step 10 is valid because the projection G of interior edge DE onto the base plane falls inside angle FDC, ensuring ray AP falls between AL and AB. All subsequent congruence arguments (Steps 13-18) correctly use the established perpendicularity and distance relationships without contradiction.
- **11.31**: The proof reduces both parallelepipeds to rectangular boxes via valid re-orientation and 11.30, then uses proportions (11.25, 6.1, 6.16, 5.22) to show the boxes are equal. All spatial claims (perpendicularity, re-orientation heights, plane sections) are mutually consistent. No angle decompositions, no interior/exterior point arguments, and no betweenness claims that could generate contradictions. The height d1 correctly equals the altitude of the base parallelogram, and R3 is consistently dimensioned across its two uses.
- **11.33**: All spatial claims are mutually consistent. The proof constructs a chain of intermediate parallelepipeds at vertex E, each sharing a common face with the next and differing in exactly one edge length. Each application of XI.25 is valid: Steps 9 and 10 involve cutting a larger solid at a specified height (EY is a sub-solid of AB, EX is a sub-solid of EY). Step 11 involves the combined solid from A to M being cut at E into EX and EP. The directions and positions of all constructed solids are compatible throughout.
- **11.34**: The proof is primarily proportional/algebraic, using Book 5 proportion theory to combine two ratio relationships. The spatial claims are limited and mutually consistent: (1) FO shares base EH with AB, (2) FO shares height CN with CD. These two claims are independent and non-contradictory. The construction of FO as a bridge solid linking AB and CD through shared dimensions is a standard and valid technique. No angle decompositions, betweenness claims, or interior/exterior claims are made that could generate spatial contradictions.
- **11.35**: All spatial claims are mutually consistent. The Pythagorean decomposition of 3D altitudes into vertical and horizontal components is geometrically valid (verified by coordinate analysis). The claim that H lies inside triangle ABC for large enough B,C is correct since the projection of the elevated line falls within angle BAC. The area-based contradiction argument is sound: equal altitudes with different perpendicular heights force unequal total areas, contradicting the established area equality. No configuration contradiction exists between any pair of spatial claims.
- **11.36**: All spatial claims about shared solid angles, equal heights, and parallelogram base comparisons are mutually consistent. The perpendicular heights are correctly determined by shared edges and the common solid angle. The proportional argument (via 11.32, 6.1, and ex aequali) is geometrically grounded in valid parallelepiped geometry with no configuration contradictions.
- **11.38**: All spatial claims are mutually consistent when verified with coordinates. The midpoints, planes, intersection points, parallelism claims, and the key parallelogram ASGT are all geometrically valid. The notation ASTG for the parallelogram is unconventional (boundary order is A-S-G-T) but the proof correctly identifies AG and ST as diagonals and the bisection conclusion follows validly from the parallelogram diagonal property.
