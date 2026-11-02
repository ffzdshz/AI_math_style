# AI Proof Error Summary

Errors identified across three independent proving runs (A, B, C) of all 465 propositions in Euclid's Elements. Includes E-class errors (logical defects found by classification) and geometry-check FAILs (spatial configuration contradictions found by geometry consistency audit).

---

## Part 1: E-Class Errors (Classification)

### 3.26 — Unsupported assertion (Run A)

The reductio argument for the central angles case (Steps 4–8) contains an unsupported assertion in Step 6: "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF." This claim that equal arcs in equal circles yield equal central angles is precisely the content of Proposition 3.27, the converse of the theorem being proved (3.26). No citation is given, and no earlier proposition in Euclid establishes this result. The inference relies on the converse of the theorem under proof (circular reasoning) or the forward proposition 3.27.

**Audit record:**
- **Violated claim**: "Since circumference BMC equals circumference ELF in equal circles, we would have angle BGM equal to angle EHF" (Step 6)
- **Failure mode**: Unsupported assertion
- **Evidence**: No citation is provided. The needed result is 3.27 (equal arcs → equal angles in equal circles), which is the next proposition (forward).

---

### 7.33 — Invalid inference (Run A)

Step 8 claims that E and F are pairwise coprime because "any common measure of E and F would also measure G," but this is false in general. Group coprimality (gcd(E,F,G)=1, established in Steps 5–7) does not entail pairwise coprimality. Counterexample: with A=6, B=10, C=15, D=gcd=1, we get E=6, F=10, G=15 where gcd(6,10)=2 but 2 does not divide 15, yet gcd(6,10,15)=1. The proof then applies Proposition 7.21 (numbers prime to one another are least in their ratio) to the pair E, F, but 7.21 requires pairwise coprimality which was not validly established.

**Audit record:**
- **Violated claim**: "E and F are prime to one another (from Step 7, any common measure of E and F would also measure G, giving a common measure of all three greater than one, which was shown impossible)"
- **Failure mode**: Invalid inference
- **Evidence**: Step 8 claims pairwise coprimality of E, F from group coprimality of E, F, G. The justification is stated without proof and is false in general.

---

### 8.8 — Invalid inference (Run C)

Step 4 claims "by 8.1 the extremes F0 and F(n+1) are prime to one another." However, 8.1 states the converse: "If numbers in continued proportion have extremes prime to one another, then they are the least of those in the same ratio." The AI needs the direction "if they are the least, then the extremes are prime," which is 8.3, not 8.1. The cited proposition literally states the opposite implication from what is needed.

**Audit record:**
- **Violated claim**: "by 8.1 the extremes F0 and F(n+1) are prime to one another" (Step 4)
- **Failure mode**: Invalid inference
- **Evidence**: 8.1 goes from prime extremes to least numbers; the AI has least numbers and infers prime extremes. The correct proposition is 8.3.

---

### 9.9 — Missing case (Run A)

Proposition 9.9 contains two cases: (1) if the number after the unit is square, all the rest are square, and (2) if the number after the unit is cube, all the rest are cube. The AI proof only addresses the square case (Steps 1–8) and never mentions cubes at all. The cube case is entirely absent from the proof, not merely compressed or terse.

**Audit record:**
- **Violated claim**: The cube case: "if the number after the unit be cube, all the rest will also be cube"
- **Failure mode**: Missing case
- **Evidence**: The AI proof text only addresses the square case (Steps 1–8) and concludes "This is what was to be proved" without any mention of cubes.

---

### 9.10 — Invalid inference (Run A) / Missing case (Run B)

**Run A**: The AI cites Proposition 8.25 to conclude that a number is square (Steps 3, 4, 5), but 8.25 states "If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube" — it concerns cubes, not squares. The correct proposition for the square case is 8.24.

**Run B**: The AI proof addresses only the square part (Steps 1–12) and concludes "This is what was to be proved" without any mention of cubes. The cube case is an entirely separate assertion with its own hypothesis and conclusion, not a mere expansion of the square case.

**Audit record (Run A):**
- **Violated claim**: "by 8.25, A is also square" (Step 3, repeated in Steps 4–5)
- **Failure mode**: Invalid inference
- **Evidence**: 8.25 concerns cubes exclusively and cannot justify any conclusion about square numbers. The correct warrant is 8.24.

**Audit record (Run B):**
- **Violated claim**: The cube case is entirely unaddressed
- **Failure mode**: Missing case
- **Evidence**: The AI proof covers Steps 1–12 dealing only with squares and concludes without mentioning cubes.

---

### 10.12 — Invalid inference (Run A)

The AI commits an invalid inference when applying 5.22 (ex aequali) in Step 8. The AI establishes A:C :: pm:np and C:B :: nq:np, then claims that 5.22 yields A:B :: pm:nq. However, 5.22 requires matching middle terms — the second term of the first ratio must equal the first term of the second ratio. Here np ≠ nq (since p ≠ q in general), so 5.22 is inapplicable. Moreover, the claimed result A:B = pm:nq is arithmetically incorrect (the correct ratio would be mq:np).

**Audit record:**
- **Violated claim**: A:B :: pm:nq (Step 8)
- **Failure mode**: Invalid inference
- **Evidence**: 5.22 requires matching middle terms. Here the middle terms are np (from A:C) and nq (from C:B), which are unequal when p ≠ q.

---

### 10.34 — Invalid inference (Run C)

The AI uses 10.27 to obtain two medial straight lines A, B that are "commensurable in square only," meaning their squares are commensurable but the lines are incommensurable in length. However, the proposition requires finding lines "incommensurable in square," meaning their squares cannot have any common measure. In Step 6, the AI explicitly claims these commensurable-in-square-only lines are "incommensurable in square," redefining the term to mean "not commensurable in length, only in square." This directly contradicts Definition 10.1.2. The conclusion directly contradicts the premise of the construction.

**Audit record:**
- **Violated claim**: "They are therefore two straight lines incommensurable in square" (Step 6)
- **Failure mode**: Invalid inference
- **Evidence**: The AI claims A, B are "incommensurable in square" but A, B from 10.27 are commensurable in square only. By D10.1.2, "incommensurable in square" means squares have no common measure — the opposite of what the construction produces.

---

### 10.44 — Invalid inference (Run B)

Step 20 claims that decompositions of sq(AB) into two incommensurable medial parts must be unique, citing "the reasoning of 10.42 applied to medial areas and 10.26." However, 10.42's proof technique exploits the rational/medial dichotomy: in 10.42, the sums of squares are rational while the doubled rectangles are medial, so a contradiction arises. In 10.44, both the sums of squares and the doubled rectangles are medial, so both sides of the difference equation are medial-minus-medial, and no rational/medial contradiction arises. The analogy to 10.42 is structurally invalid.

**Audit record:**
- **Violated claim**: "these decompositions of sq(AB) into incommensurable medial parts must be the same decomposition (by the reasoning of 10.42 applied to medial areas and 10.26)" (Step 20)
- **Failure mode**: Invalid inference
- **Evidence**: 10.42's proof mechanism depends on the rational/medial dichotomy that does not exist in 10.44's all-medial setting. "The reasoning of 10.42 applied to medial areas" is an invalid analogy.

---

### 10.47 — Unsupported assertion (Run B)

The crux of the contradiction (Steps 19–20) is the claim that the difference sq(MC) − sq(MD) is rational, where M is the midpoint of AB, because "MC and MD are expressible in terms of the segments and their differences are commensurable." This claim is unsupported: MC = AB/2 − AC and MD = AB/2 − AD, but AC and CB are incommensurable in square (by hypothesis), and no cited proposition establishes MC and MD as commensurable or their difference of squares as rational.

**Audit record:**
- **Violated claim**: "The square on MC minus the square on MD is a difference of squares on segments that are commensurable. This difference of squares is rational." (Steps 19–20)
- **Failure mode**: Unsupported assertion
- **Evidence**: No citation supports this. The segments MC, MD involve incommensurable magnitudes, and no proposition licenses the rationality claim.

---

### 10.52 — Invalid inference (Run C)

After correctly computing in Steps 7–8 that sq(E):sq(F) = 3:2, the AI asserts in Step 9 that "Equivalently, the square on E is to the square on F as CD:CG = 4:3." The claim that 3:2 equals 4:3 is a mathematical falsehood. The AI explicitly writes two contradictory numerical ratios (3:2 in Step 8, then 4:3 in Step 9) and calls them "equivalent."

**Audit record:**
- **Violated claim**: "the square on E is to the square on F as CD:CG = 4:3" (Step 9), after computing the ratio as 3:2 in Step 8
- **Failure mode**: Invalid inference
- **Evidence**: With CD=4 and CG=3, CD:CG = 4:3 ≠ 3:2. The correct convertendo relationship gives sq(E):sq(F) = 3:2, not 4:3.

---

### 10.86 — Invalid inference (Run B)

Step 2 asserts that Proposition 10.29 can find two rational straight lines FG and GH such that "GH is commensurable in length with the rational straight line A." However, 10.29 guarantees no relationship between either output line and any external rational line. If one sets the starting line commensurable with A, then the lesser line (GH) would be incommensurable in length with A — the opposite of what the AI claims. The AI positively attributes to 10.29 a property it does not entail.

**Audit record:**
- **Violated claim**: Step 2 asserts that 10.29 can find FG, GH such that "GH is commensurable in length with the rational straight line A"
- **Failure mode**: Invalid inference
- **Evidence**: 10.29 guarantees no commensurability with an external line. The lesser line produced by 10.29 is commensurable in square only with the greater.

---

### 10.87 — Invalid inference (Run C)

The AI stipulates that BC:CD IS a square-to-square ratio (Step 1), whereas the proposition requires that BC:CD is NOT a square-to-square ratio. With the AI's setup, Step 5 correctly derives that FG is commensurable in LENGTH with GH. But 10.73, which the AI cites to establish FH as an apotome, requires "commensurable in square only." The AI acknowledges the contradiction in Steps 9 and 12 but never resolves it. With FG and GH commensurable in length and both rational, FH = FG − GH would be rational, not an apotome.

**Audit record:**
- **Violated claim**: FH is an apotome (cited as following from 10.73 in Steps 9 and 12)
- **Failure mode**: Invalid inference
- **Evidence**: AI Step 1 sets BC:CD as a square-to-square ratio. AI Step 5 derives FG commensurable in length with GH. 10.73 requires "commensurable in square only." The AI explicitly notes the problem but never resolves it.

---

### 11.8 — Invalid inference (Run C)

Step 4 claims "apply 1.29 to obtain that the alternate angles angle ADB and angle DBC are also equal." Proposition 1.29, applied to parallel lines AB and CD with transversal BD, yields the alternate interior angles ABD = BDC (correctly used in Step 3), but does NOT yield angle ADB = angle DBC. The angles ADB and DBC are not alternate angles under 1.29. This invalid angle equality is used in Step 5 via AAS (1.26) to conclude AB = CD, a result that is not generally true for the given configuration. The false conclusion propagates through Steps 6, 9, 10, and 12.

**Audit record:**
- **Violated claim**: "angle ADB equals angle DBC" derived from 1.29 in Step 4
- **Failure mode**: Invalid inference
- **Evidence**: 1.29 applied to parallels AB‖CD with transversal BD yields angle ABD = angle BDC, not angle ADB = angle DBC. The latter are not alternate interior angles.

---

### 11.31 — Invalid inference (Run A)

The AI constructs a comparison solid RS on base FGPQ (equal to LMNO via I.45) and then claims in Step 5 that solids AB (on base FGHK) and RS (on base FGPQ) are "on the same base (sharing the side FG in the base plane)" and applies 11.29 or 11.30 to conclude AB equals RS. However, 11.29 and 11.30 both require the solids to be on THE SAME base — meaning the identical base parallelogram — not merely on equal bases that share one edge. FGHK and FGPQ are different parallelograms (equal in area but geometrically distinct), so the hypothesis of 11.29/11.30 is not satisfied.

**Audit record:**
- **Violated claim**: Step 5 applies 11.29/11.30 to solids on different (though equal) bases sharing only edge FG
- **Failure mode**: Invalid inference
- **Evidence**: 11.29 states "on the same base" meaning the identical parallelogram, not equal parallelograms sharing an edge. FGHK ≠ FGPQ.

---

### 12.17 — Unsupported assertion (Run B) / Invalid inference (Run C)

**Run B**: Steps 10–11 assert "the perpendicular from A to that face is at least as great as the perpendicular from A to the corresponding chord." This is the essential geometric claim of the entire proposition; no valid supporting chain is provided. The cited propositions (3.15, 11.38, 1.19, CN5) do not license the 3D perpendicular-distance claim. This is the core conclusion being asserted without valid justification.

**Run C**: Step 13 claims "the perpendicular distance from A to the plane of any face of the polyhedron is at least as great as the perpendicular distance from A to any edge of that face." This inequality is reversed: the perpendicular from a point to a plane is the MINIMUM distance to any point in the plane, so dist(A, plane) ≤ dist(A, edge), not ≥. The stated mathematical relationship is the exact opposite of the true one.

**Audit record (Run B):**
- **Violated claim**: "the perpendicular from A to that face is at least as great as the perpendicular from A to the corresponding chord" (Steps 10–11)
- **Failure mode**: Unsupported assertion
- **Evidence**: The cited refs (1.19, 11.38, 3.15, CN5) do not support this 3D perpendicular-distance claim.

**Audit record (Run C):**
- **Violated claim**: "perpendicular distance from A to plane ≥ perpendicular distance from A to edge" (Step 13)
- **Failure mode**: Invalid inference
- **Evidence**: The perpendicular from a point to a plane is the minimum distance; dist(A, plane) ≤ dist(A, edge). The AI's chain is backwards.

---

### 13.16 — Unsupported assertion (Run C)

The AI attempts to construct an icosahedron but its own calculations in Steps 17–18 and 26–27 explicitly demonstrate that the construction parameters do not yield equilateral triangular faces (Step 18: "the pentagon sides are not equal to the pole edges"; Step 27: "√5 = 5, which is false"). After these failed attempts, the AI vaguely restates the approach in Steps 28–35 but never identifies correct construction parameters. Nevertheless, Step 36 asserts "Therefore twenty equilateral triangles have been constructed." The AI showed its construction fails, attempted but could not fix it, and then asserted the conclusion without any valid supporting argument.

**Audit record:**
- **Violated claim**: "Therefore twenty equilateral triangles have been constructed, and all twelve vertices lie on the sphere of diameter AB" (Step 36)
- **Failure mode**: Unsupported assertion
- **Evidence**: Step 18: "So the pentagon sides are not equal to the pole edges." Step 27: "√5 = 5, which is false." The AI demonstrated its construction is wrong, never completed a working alternative, then asserted the conclusion.

---

## Part 2: Geometry-Check FAIL (Spatial Configuration Contradictions)

### 1.24 — Angle decomposition contradiction (Run A)

**Contradictory steps**: Step 6, Step 8

- **Claim 1** (Step 6): F lies inside triangle DEG, so the three angles DFE, EFG, GFD around F sum to 360°. Required by application of Proposition 1.21 in Step 7.
- **Claim 2** (Step 8): Ray FD falls between rays FE and FG, so angle EFG = angle EFD + angle DFG (additive decomposition). Required by angle inequality chain in Steps 8–10.

**Contradiction**: If F is inside triangle DEG, the three angles around F sum to 360°. The additive decomposition angle EFG = angle EFD + angle DFG forces angle EFG = 180°, meaning E, F, G are collinear — contradicting F being inside the triangle and triangle EFG being valid. Numerical verification confirms: from F, ray FD points away from the interior angle EFG; the opposite ray is what actually falls between FE and FG.

**Fixable**: Yes

---

### 3.25 — Cases ii/iii position swap (Run C)

**Contradictory steps**: Step 7, Step 10

- **Claim 1** (Step 7): In Case (ii) where angle ABD > angle BAD, E lies on line BD between D and B.
- **Claim 2** (Step 10): In Case (iii) where angle ABD < angle BAD, E lies on line BD produced beyond D.

**Contradiction**: The positions of E in Cases (ii) and (iii) are swapped. Coordinate verification with A=(0,0), C=(2,0), D=(1,0), B=(1,h): in Case (ii) (h<1), E is placed at (1,−0.75) — beyond D, not between D and B as claimed. In Case (iii) (h>1), E is at (1,0.75) — between D and B, not beyond D as claimed.

**Fixable**: Yes — swap the position descriptions between Cases (ii) and (iii).

---

### 4.15 — Incorrect angle sum across semicircle (Run A)

**Contradictory steps**: Steps 2–4 (construction), Step 5

- **Claim 1** (Steps 2–4): C and E are intersection points of the auxiliary circle with the main circle, placed symmetrically on opposite sides of diameter AD. C is above AD, E is below.
- **Claim 2** (Step 5): Angles AGC + CGD + DGE are all on one side of line AD and sum to 180° by I.13.

**Contradiction**: C is above diameter AD and E is below it. Angle AGC + angle CGD = 120° + 60° = 180° accounts for the entire upper side, while angle DGE = 60° is on the lower side. The three-angle sum is 240°, not 180°. The correct angle AGE is 120°, not 60°. (Note: this erroneous step is never used in subsequent steps — the proof's final result is correct despite this error.)

**Fixable**: Yes — Step 5 is unnecessary and should be removed.

---

### 6.15 — Incorrect collinearity claim (Run A)

**Contradictory steps**: Step 2, Step 5

- **Claim 1** (Step 2): EA and AC are in a straight line (E-A-C collinear). Combined with the construction C-A-D collinear, this forces E, C, A, D all onto one line, making triangle ADE degenerate (zero area).
- **Claim 2** (Step 5): BA and AD lie on the same straight line BD (B-A-D collinear). Combined with C-A-D collinear, this forces B onto line CD, making triangle ABC degenerate.

**Contradiction**: Step 2 incorrectly concludes EA and AC are in a straight line; the correct conclusion from I.13 and I.14 is that EA and AB are in a straight line. The wrong collinearity (E-A-C), combined with construction (C-A-D collinear), forces all of E, C, A, D onto one line, making triangle ADE degenerate. Both reference triangles become degenerate, making the entire proof strategy unsound.

**Fixable**: Yes — use the correct collinearity E-A-B from I.14.

---

### 10.29 — Circle centered at wrong point (Run C)

**Contradictory steps**: Step 5

- **Claim 1** (Step 5): Circle centered at vertex V with radius A meets the other arm at Q, making B = VQ = A.
- **Claim 2** (Step 5): In right triangle VPQ, sq(A) = sq(B) + sq(C) with C > 0, requiring B < A.

**Contradiction**: The construction forces B = A, but the Pythagorean relation with C = A/2 > 0 requires B = A·√3/2 < A. Substituting B = A gives sq(C) = 0, contradicting C = A/2 > 0. The circle should be centered at P (the endpoint of C on the arm), not at V (the vertex).

**Fixable**: Yes — center the circle at P instead of V.

---

### 11.29 — Collinear points treated as parallelogram (Run A, Run B)

**Run A — Contradictory steps**: Step 1, Step 3, Step 6

- **Claim 1** (Step 1): E, E', H, H' all lie on one straight line (the proposition's given condition).
- **Claim 2** (Steps 3, 6): EE'H'H is a parallelogram, and the solid is a parallelepiped with all six faces being parallelograms.

**Contradiction**: Four collinear points cannot form a parallelogram (which requires a 2D quadrilateral). EE'H'H is a degenerate line segment with zero area, not a parallelogram. The solid cannot be a parallelepiped, invalidating the application of XI.28.

**Run B — Contradictory steps**: Step 1, Step 17

- **Claim 1** (Step 1): CM and CN are general parallelepipeds with translation vectors v and w that are NOT required to be parallel.
- **Claim 2** (Step 17): The auxiliary solid ABCD-EF'G'H is a parallelepiped, implicitly requiring AE ‖ BF' (i.e., v ‖ w).

**Contradiction**: AE = v and BF' = w. For the auxiliary solid to be a parallelepiped, v must be parallel to w. But the hypothesis only constrains w = v + t·AB, which does NOT imply v ‖ w unless v happens to be parallel to AB (a degenerate case).

**Fixable**: Yes (both runs)

---

### 11.31 — Double-collinearity forces degenerate construction (Run C)

**Contradictory steps**: Step 3

- **Claim 1** (Step 3): E, F, K, L are collinear (line l₁).
- **Claim 2** (Step 3): E, H, K, N are collinear (line l₂), with EFGH a non-degenerate parallelogram (so l₁ ≠ l₂).

**Contradiction**: Two distinct lines intersect in at most one point. E lies on both lines, making E the unique intersection. K is also claimed to lie on both lines, forcing K = E. This makes the combined parallelogram EKNT degenerate. The complement technique of Steps 6–8 breaks down entirely.

**Fixable**: No — the AI's additive/subtractive complement technique inherently requires both pairs of adjacent sides to be collinear, which is geometrically impossible for distinct non-degenerate parallelogram bases. The proof would need to be fundamentally restructured.

---

### 11.35 — Projection falls outside angle (Run A)

**Contradictory steps**: Step 2, Step 9

- **Claim 1** (Step 2): H is the orthogonal projection of G onto plane P1. For asymmetric angle configurations (e.g., angle BAG=70°, angle CAG=20°, angle BAC=60°), H falls at ~69° from AB, placing it outside angle BAC.
- **Claim 2** (Step 9): H is in the interior of angle BAC, and ray JI lies in the interior of angle HJA, so angle HJA = angle HJI + angle IJA.

**Contradiction**: For valid asymmetric configurations, coordinate analysis shows: (1) H falls outside angle BAC (past line AC). (2) At point J, ray JI does NOT lie in the interior of angle HJA. The correct decomposition is angle IJA = angle IJH + angle HJA (not the stated form).

**Fixable**: Yes — handle both cases (JI inside or outside angle HJA) separately, or replace the angle decomposition with a distance-based argument.

---

### 13.16 — Inter-plane distance contradiction (Run B)

**Contradictory steps**: Steps 12–13, Step 22

- **Claim 1** (Steps 12–13): The separation between the two pentagonal planes equals s₁₀ (side of the inscribed decagon).
- **Claim 2** (Step 22): The separation equals r (the radius of the inscribing circle).

**Contradiction**: s₁₀ = r(√5−1)/2 ≈ 0.618r ≠ r. With d = s₁₀, the lateral edge² = 2s₁₀², but the required value is s₅² = r² + s₁₀². The proof asserts two mutually inconsistent positions for the pentagonal planes.

**Fixable**: Yes — remove the incorrect claim in Steps 12–13 that d = s₁₀.

---

### 13.17 — Dodecahedron vertices misplaced (Run B)

**Contradictory steps**: Steps 11–12, Step 16

- **Claim 1** (Steps 11–12): The 12 non-cube-vertex vertices are golden-section division points located ON the edges of the cube.
- **Claim 2** (Step 16): All 20 vertices are equidistant from center O at distance d/2, lying on the circumsphere.

**Contradiction**: A point K on an edge of the cube (between two vertices) is strictly closer to the center than the cube vertices are. Direct computation confirms OK² < d²/4. The proof silently replaces (s/2 − g) with s/2 in a coordinate. A dodecahedron inscribed in the same sphere as the cube necessarily has vertices OUTSIDE the cube (raised above its faces), not on its edges.

**Fixable**: Yes — the additional vertices must be erected outward from the cube faces, not confined to its edges.
