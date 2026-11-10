# Book 4 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 4.1
**Statement:** Into a given circle to fit a straight line equal to a given straight line which is not greater than the diameter of the circle.

**Step 1.** Let Γ be the given circle and s the length of the given straight line. Find the centre O of Γ, choose A on its circumference, and join AO and produce it through O to meet the circumference again at B. Then AB is a diameter. [3.1, P1, P2, D1.17]

**Step 2.** If s = AB, the diameter AB itself is the required straight line: it has the prescribed length and both extremities are on Γ. Hence suppose s < AB. [Hypothesis, D4.7]

**Step 3.** The radii OA and OB are equal, so AB = OA + OB = OA + OA. Consequently s < OA + OA. Also OA + s > OA, since the whole is greater than its part. Thus the three lengths OA, OA, s satisfy every strict triangle inequality. [D1.15, CN2, CN5]

**Step 4.** Apply the triangle construction of 1.22 with OA as one side and with the other two prescribed lengths OA and s. Let the third vertex be C, with OC = OA and AC = s. This route uses 1.22 directly because Step 3 establishes precisely its required inequalities. [1.22]

**Step 5.** Since OC = OA, C lies on the circle with centre O and radius OA, namely Γ. Thus A and C both lie on Γ, so AC is fitted into Γ; and AC equals the given straight line. Together with the equality case in Step 2, this completes the construction. [D1.15, D4.7]

**USED:** 1.22, 3.1, CN2, CN5, D1.15, D1.17, D4.7, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.22', '3.1', 'CN2', 'CN5', 'D1.15', 'D1.17', 'D4.7', 'P1', 'P2']

## Proposition 4.2
**Statement:** In a given circle to inscribe a triangle equiangular with a given triangle.

**Step 1.** Let the given circle be Γ and the given triangle be DEF. Choose a point A on Γ, and construct a tangent at A by 3.17. Produce it in both directions, taking points X and Y so that X, A, Y lie in that order (P2). Path choice: use the ready-made tangent construction, then apply the tangent–chord theorem 3.32 directly to obtain the required angles on the circumference.

**Step 2.** On the side of XY containing the circle, construct rays AB and AC such that ∠XAB = ∠DFE and ∠CAY = ∠DEF (1.23). Produce these rays to their second intersections B and C with Γ (P2). The two copied angles together are less than two right angles (1.17), whereas the adjacent angles across the circle-side of the straight line XAY total two right angles (1.13). Consequently the rays occur in the order AX, AB, AC, AY on that side; in particular, B and C are distinct. Join BC (P1).

**Step 3.** For the chord AB, C lies in the segment opposite the tangent–chord angle XAB. Therefore ∠ACB = ∠XAB by 3.32. Since ∠XAB was constructed equal to ∠DFE, we obtain ∠ACB = ∠DFE (CN1).

**Step 4.** For the chord AC, B lies in the segment opposite the tangent–chord angle CAY. Therefore ∠ABC = ∠CAY by 3.32. Since ∠CAY was constructed equal to ∠DEF, we obtain ∠ABC = ∠DEF (CN1).

**Step 5.** The three angles of ABC and the three angles of DEF each equal two right angles (1.32), so their sums are equal (CN1). The sums ∠ABC + ∠ACB and ∠DEF + ∠DFE are equal by Steps 3–4 and CN2. Subtracting these equal sums leaves ∠BAC = ∠EDF (CN3). Thus the triangles are equiangular.

**Step 6.** Since A, B, and C all lie on Γ, triangle ABC is inscribed in the given circle (D4.3). It is equiangular with the given triangle DEF, as required.

**USED:** 1.13, 1.17, 1.23, 1.32, 3.17, 3.32, CN1, CN2, CN3, D4.3, P1, P2
**Human refs (from References field):** 1.23, 1.32, 3.16, 3.32
**Jaccard:** 0.231 — AI adds ['1.13', '1.17', '3.17', 'CN1', 'CN2', 'CN3', 'D4.3', 'P1', 'P2']; Human adds ['3.16']

## Proposition 4.3
**Statement:** About a given circle to circumscribe a triangle equiangular with a given triangle.

**Step 1.** Let the given circle be Γ and the given triangle be ABC. Write α = ∠BAC, β = ∠ABC, and γ = ∠ACB, and denote the common magnitude of a right angle by R (P4). Then α + β + γ = 2R (1.32), so each of α, β, γ is less than 2R (CN5). We shall prescribe their supplements as successive central angles and draw tangents at the resulting points.

**Step 2.** Produce suitable sides of ABC to obtain exterior angles a and c supplementary to α and γ respectively; thus a + α = 2R and c + γ = 2R (P2, 1.13). Find the centre O of Γ (3.1), choose U on its circumference, and join OU (P1). At O construct ∠UOV = a and ∠UOW = c on opposite sides of OU, taking V and W where the constructed rays meet Γ (1.23, P2).

**Step 3.** The angles about O together equal 4R, by applying 1.13 on both sides of a straight line and adding (P4, CN2). Since α + β + γ = 2R, we have a + c = 2R + β; hence the remaining sector between OV and OW, not containing OU, equals 2R − β (CN2, CN3). Consequently U, V, W occur cyclically with successive central angles
∠UOV = 2R − α,  ∠VOW = 2R − β,  ∠WOU = 2R − γ.
Each of these angles is strictly between zero and 2R, by Step 1 and the supplementary-angle equalities (CN5).

**Step 4.** At U, V, and W draw straight lines perpendicular to OU, OV, and OW respectively, producing the radii as necessary (P2, 1.11). These perpendiculars meet the circle without cutting it (3.16), and therefore are tangents, denoted tU, tV, and tW (D3.2). Path choice: the perpendicular-tangent criterion is used here because the radii and points of contact are already prescribed.

**Step 5.** We verify that these tangents meet in the required directions. Take any consecutive pair (S,T) among (U,V), (V,W), and (W,U), and put θ = ∠SOT. Join ST (P1). Since OS = OT (D1.15), the base angles ε = ∠OST and ζ = ∠OTS are equal (1.5). Also ε + ζ = 2R − θ (1.32); consequently both are less than R (CN5).
Choose the tangent ray at S on the side of OS containing T, and the tangent ray at T on the side of OT containing S. These rays lie on the side of ST opposite O. By their perpendicularity to the radii, their interior angles with ST are R − ε and R − ζ. Their sum is θ, which is less than 2R (CN2, CN3; Step 3). Thus the rays meet on that side of ST (P5). Denote the intersections for (U,V), (V,W), and (W,U) by X, Y, and Z respectively.

**Step 6.** Because all three successive central angles are less than 2R, the other two contact points lie on opposite sides of the line through O and any one contact point (Step 3). Accordingly, the two tangent rays chosen there in Step 5 are opposite rays. Thus U lies between Z and X, V lies between X and Y, and W lies between Y and Z. The three tangent segments therefore form triangle XYZ, and its sides ZX, XY, and YZ touch Γ at U, V, and W respectively. Hence XYZ is circumscribed about Γ (D4.4).

**Step 7.** For the pair S,T and its tangent intersection K in Step 5, the two base angles of triangle SKT sum to θ. Therefore ∠SKT = 2R − θ (1.32, CN3). Applying this to the three pairs, using the central angles in Step 3 and the betweenness relations in Step 6, gives
∠ZXY = α,  ∠XYZ = β,  ∠YZX = γ
(CN1, CN3). Thus XYZ is equiangular with ABC and is circumscribed about the given circle, as required.

**USED:** 1.11, 1.13, 1.23, 1.32, 1.5, 3.1, 3.16, CN1, CN2, CN3, CN5, D1.15, D3.2, D4.4, P1, P2, P4, P5
**Human refs (from References field):** 1.13, 1.23, 1.32, 3.1, 3.16, 3.18
**Jaccard:** 0.263 — AI adds ['1.11', '1.5', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.15', 'D3.2', 'D4.4', 'P1', 'P2', 'P4', 'P5']; Human adds ['3.18']

## Proposition 4.4
**Statement:** In a given triangle to inscribe a circle.

**Step 1.** Let ABC be the given triangle. Bisect the internal angles BAC and ABC [1.9]. Their halves have sum less than two right angles [1.17, CN5], so the bisecting rays meet at a point O on the side of AB containing C [P5]. Their common point lies inside both vertex angles, and therefore inside triangle ABC. We use these two bisectors; no theorem concerning concurrence of three bisectors is needed.

**Step 2.** Produce the side-lines as necessary [P2], and draw OE, OF, and OG perpendicular to the lines AB, AC, and BC respectively [1.12]. The half-angles at A and B are acute [1.17]. Hence E and F lie on the rays AB and AC, while E and G lie on the rays BA and BC. Indeed, a foot at its vertex would make the corresponding half-angle right; a foot on the opposite ray would make the angle at that vertex obtuse [1.13], which is impossible in a right-angled triangle [1.17]. In particular, E lies between A and B.

**Step 3.** In triangles AEO and AFO, the angles AEO and AFO are equal, being right angles [P4]; the angles EAO and FAO are equal by the bisection at A [1.9]; and AO is common. Therefore OE = OF [1.26]. This is the natural congruence proposition here: two angles and the side opposite the right angle are already equal.

**Step 4.** Likewise, in triangles BEO and BGO, the right angles BEO and BGO are equal [P4], the angles EBO and GBO are equal by the bisection at B [1.9], and BO is common. Thus OE = OG [1.26]. Consequently OE, OF, and OG are all equal [CN1].

**Step 5.** Describe the circle with centre O and radius OE [P3]. Since OF and OG equal OE, the points E, F, and G all lie on its circumference [D1.15].

**Step 6.** Each of the lines AB, AC, and BC is perpendicular to a radius at its endpoint on the circumference. Each therefore touches the circle, respectively at E, F, and G [3.16]. We use 3.16 directly because the perpendicular radii have already been constructed.

**Step 7.** A tangent does not cut the circle [D3.2], so the circle lies entirely on the side of each tangent line containing its centre O. Since O is inside ABC, these are precisely the three inward sides of the lines bounding the triangle. Thus the circle is contained in ABC, and its contact points E, F, and G belong to the actual side segments, not merely their extensions. Its circumference therefore touches each side of the triangle: the circle is inscribed in ABC [D4.5], as required.

**USED:** 1.12, 1.13, 1.17, 1.26, 1.9, 3.16, CN1, CN5, D1.15, D3.2, D4.5, P2, P3, P4, P5
**Human refs (from References field):** 1.26, 1.9, 3.16, D4.5
**Jaccard:** 0.267 — AI adds ['1.12', '1.13', '1.17', 'CN1', 'CN5', 'D1.15', 'D3.2', 'P2', 'P3', 'P4', 'P5']

## Proposition 4.5
**Statement:** About a given triangle to circumscribe a circle.

**Step 1.** Let ABC be the given triangle. We use the perpendicular bisectors of two sides; this construction does not require separate cases according to the angles of the triangle. Bisect AB at D and AC at E, so that AD = DB and AE = EC (1.10).

**Step 2.** At D erect a straight line ℓ perpendicular to AB, and at E erect a straight line m perpendicular to AC (1.11). Produce these lines as necessary in both directions (P2). The angles they make with the respective sides are right angles (D1.10).

**Step 3.** We show that ℓ and m meet. Suppose that they do not; then they are parallel (D1.23). The straight line AB must meet m: otherwise AB would also be parallel to m, and hence parallel to ℓ by 1.30, although AB meets ℓ at D. Let F be the intersection of AB, produced if necessary, with m (P2).

**Step 4.** Since m is perpendicular to AC at E, it cannot also contain A; hence F ≠ A (D1.10). Moreover, E does not lie on AB, so AEF is a triangle. Its angle AEF is right because m is perpendicular to AC (D1.10). Its angle AFE is also right, since the transversal AB cuts the supposed parallels ℓ and m and is perpendicular to ℓ (1.29). This contradicts 1.17, according to which any two angles of a triangle together are less than two right angles. Therefore ℓ and m meet; call their intersection O. Join O to A, B, and C (P1).

**Step 5.** If O = D, then OA = OB because AD = DB. Otherwise, in triangles ADO and BDO, AD = DB, OD is common (CN4), and the included angles ADO and BDO are right and therefore equal (D1.10, P4). Thus OA = OB by 1.4. Side–angle–side is the natural choice here because its hypotheses are already supplied by the construction; no calculation with squares is needed.

**Step 6.** Similarly, if O = E, then OA = OC because AE = EC. Otherwise, triangles AEO and CEO have AE = EC, the common side EO (CN4), and equal included right angles AEO and CEO (D1.10, P4). Hence OA = OC by 1.4. Together with Step 5, this gives OA = OB = OC (CN1).

**Step 7.** Since A is not on the perpendicular ℓ through D, O ≠ A (D1.10). Describe the circle with centre O and radius OA (P3). The equalities OA = OB = OC show that its circumference passes through A, B, and C (D1.15). Consequently this circle is circumscribed about triangle ABC (D4.6), as required.

**USED:** 1.10, 1.11, 1.17, 1.29, 1.30, 1.4, CN1, CN4, D1.10, D1.15, D1.23, D4.6, P1, P2, P3, P4
**Human refs (from References field):** 1.10, 1.4
**Jaccard:** 0.125 — AI adds ['1.11', '1.17', '1.29', '1.30', 'CN1', 'CN4', 'D1.10', 'D1.15', 'D1.23', 'D4.6', 'P1', 'P2', 'P3', 'P4']

## Proposition 4.6
**Statement:** In a given circle to inscribe a square.

**Step 1.** Let Γ be the given circle. Find its centre O by 3.1. Choose A on its circumference, join AO, and produce AO through O to meet the circumference again at C (P1, P2). Then AC is a diameter (D1.17).

**Step 2.** At O construct a perpendicular to AC, and extend it in both directions to meet Γ at B and D, naming the points so that A, B, C, D occur successively around the circumference (1.11, P2). Since BD passes through O, it too is a diameter (D1.17). Join AB, BC, CD, and DA (P1).

**Step 3.** The angles AOB and BOC are right because BO is perpendicular to AC (D1.10). Their vertically opposite angles COD and DOA are equal to them, respectively (1.15). Thus all four central angles are right and equal to one another (P4). Also OA = OB = OC = OD, since these are radii of Γ (D1.15).

**Step 4.** Apply 1.4 successively to the pairs of triangles AOB and BOC, BOC and COD, and COD and DOA: in each pair, two corresponding sides are equal radii and the included angles are equal by Step 3. Hence AB = BC, BC = CD, and CD = DA, so all four sides of ABCD are equal (CN1). This direct SAS route is chosen because its hypotheses are already supplied by the perpendicular radii; no intermediate comparison of arcs is needed.

**Step 5.** Since AC is a diameter, the angles ABC and ADC are angles in semicircles and therefore right (3.31). Since BD is a diameter, the angles BAD and BCD are likewise right (3.31). Thus ABCD is right-angled.

**Step 6.** The quadrilateral ABCD is both equilateral and right-angled, so it is a square (D1.22). Its four vertices lie on Γ, so it is inscribed in Γ (D4.3). Therefore a square has been inscribed in the given circle, as required.

**USED:** 1.11, 1.15, 1.4, 3.1, 3.31, CN1, D1.10, D1.15, D1.17, D1.22, D4.3, P1, P2, P4
**Human refs (from References field):** 1.4, 3.31, D1.22
**Jaccard:** 0.214 — AI adds ['1.11', '1.15', '3.1', 'CN1', 'D1.10', 'D1.15', 'D1.17', 'D4.3', 'P1', 'P2', 'P4']

## Proposition 4.7
**Statement:** About a given circle to circumscribe a square.

**Step 1.** Find the centre O of the given circle [3.1]. Draw a diameter AC and, through O, a diameter BD perpendicular to AC, naming the endpoints A, B, C, D consecutively around the circle [P1, P2, 1.11, D1.17].

**Step 2.** At A and C draw straight lines perpendicular to AC, and at B and D draw straight lines perpendicular to BD; denote these lines by t_A, t_B, t_C, t_D respectively [P2, 1.11]. Each touches the circle at its named endpoint, by the perpendicular-at-an-extremity consequence of 3.16. This is the direct path: the diameters already supply the perpendiculars needed for tangency, so no separate tangent construction is required [3.16].

**Step 3.** Adjacent tangents meet on the required sides as follows. For any consecutive pair U, V among A, B, C, D, join UV [P1]. Triangle OUV is right-angled at O, so its angles at U and V together equal one right angle [1.32, P4, CN3]. At U take the tangent ray directed toward the side of OU containing V, and at V take the tangent ray directed toward the side of OV containing U. The angles these rays make with UV, on the side opposite O, are complementary to the angles of triangle OUV at U and V. Their sum is therefore one right angle [P4, CN2, CN3]. Consequently these tangent rays meet on that side [P5]. Name the intersections E = t_A ∩ t_B, F = t_B ∩ t_C, G = t_C ∩ t_D, and H = t_D ∩ t_A. The two intersections on each tangent lie on opposite rays from its contact point; hence A, B, C, D lie within the segments HE, EF, FG, GH respectively.

**Step 4.** In each triangle formed by two consecutive contact points and their tangent intersection, the two angles at the contact points together equal one right angle, as established in Step 3. Its angle at the tangent intersection is therefore right [1.32, P4, CN3]. Thus all four interior angles of EFGH are right. Moreover, the perpendiculars to AC at A, O, C are parallel to one another, and the perpendiculars to BD at B, O, D are parallel to one another [1.28, P4]. Consequently t_A and t_C are parallel to BD, while t_B and t_D are parallel to AC; opposite sides of EFGH are parallel.

**Step 5.** The quadrilateral AEFC is a parallelogram: AE is parallel to FC, and EF is parallel to CA, by Step 4. Its opposite sides are therefore equal, giving EF = AC [1.34]. Likewise BFGD is a parallelogram, since BF is parallel to GD and FG is parallel to DB; hence FG = BD [1.34].

**Step 6.** The radii OA, OB, OC, OD are equal [D1.15]. Adding equal radii gives AC = BD [CN2]. Together with Step 5, this yields EF = FG [CN1]. Since EFGH is a parallelogram, EF = GH and FG = HE [1.34]. Therefore all four sides of EFGH are equal [CN1].

**Step 7.** EFGH is equilateral by Step 6 and right-angled by Step 4, so it is a square [D1.22]. Its four sides touch the given circle at A, B, C, D respectively, with each contact point on its corresponding side, by Steps 2–3. Hence EFGH is a square circumscribed about the given circle [D4.4].

**USED:** 1.11, 1.28, 1.32, 1.34, 3.1, 3.16, CN1, CN2, CN3, D1.15, D1.17, D1.22, D4.4, P1, P2, P4, P5
**Human refs (from References field):** 1.28, 1.30, 1.34, 3.16, 3.18
**Jaccard:** 0.158 — AI adds ['1.11', '1.32', '3.1', 'CN1', 'CN2', 'CN3', 'D1.15', 'D1.17', 'D1.22', 'D4.4', 'P1', 'P2', 'P4', 'P5']; Human adds ['1.30', '3.18']

## Proposition 4.8
**Statement:** In a given square to inscribe a circle.

**Step 1.** Let ABCD be the given square, with vertices in order. Its four sides are equal and its four angles are right angles (D1.22). Draw the diagonals AC and BD, and let their intersection inside the square be O (P1).

**Step 2.** Triangles BAC and DAC have their three corresponding sides equal: BA = DA, BC = DC, and AC is common. Therefore ∠BAC = ∠DAC and ∠BCA = ∠DCA (1.8). Likewise, comparing triangles ABD and CBD gives ∠ABD = ∠CBD and ∠ADB = ∠CDB (1.8). Thus the diagonals bisect the square’s angles. This is the chosen route: the side equalities make 1.8 immediately applicable, and the resulting angle-bisectors will give equal perpendicular distances from O to the sides.

**Step 3.** From O draw OE, OF, OG, and OH perpendicular to AB, BC, CD, and DA respectively (1.12). The angles at these feet are right angles (D1.10). Each foot lies strictly within its corresponding side. Indeed, at either endpoint of a side, the segment joining that endpoint to O lies strictly inside the square’s right angle, so its angle with the side is less than a right angle (Step 2; CN5). A foot at the endpoint would contradict this. A foot beyond an endpoint would make the angle between the segment to O and the segment to the foot greater than a right angle (1.13; P4), giving a triangle with a right angle and an angle greater than a right angle, contrary to 1.17.

**Step 4.** Compare triangles OAE and OAH. Their angles at A are equal by Step 2, their angles at E and H are equal right angles (P4), and OA is their common side opposite those right angles. Hence OE = OH (1.26). Similarly, triangles OBE and OBF give OE = OF, and triangles OCF and OCG give OF = OG (1.26). Consequently OE = OF = OG = OH (CN1).

**Step 5.** Describe the circle with centre O and radius OE (P3). Since OF, OG, and OH equal OE, the circle passes through E, F, G, and H (D1.15).

**Step 6.** Each side of the square is perpendicular to a radius at its endpoint on the circle. By 3.16, each such side-line lies outside the circle apart from that point, and therefore touches the circle (D3.2). Here 3.16 supplies precisely the needed direction, from perpendicularity to tangency. Since O lies inside the square and none of its side-lines cuts the circle, the circle lies within the square and touches its four sides at E, F, G, and H. It is therefore inscribed in ABCD (D4.5). Thus, in the given square, a circle has been inscribed.

**USED:** 1.12, 1.13, 1.17, 1.26, 1.8, 3.16, CN1, CN5, D1.10, D1.15, D1.22, D3.2, D4.5, P1, P3, P4
**Human refs (from References field):** 1.10, 1.31, 1.34, 3.16
**Jaccard:** 0.053 — AI adds ['1.12', '1.13', '1.17', '1.26', '1.8', 'CN1', 'CN5', 'D1.10', 'D1.15', 'D1.22', 'D3.2', 'D4.5', 'P1', 'P3', 'P4']; Human adds ['1.10', '1.31', '1.34']

## Proposition 4.9
**Statement:** About a given square to circumscribe a circle.

**Step 1.** Let ABCD be the given square, with its vertices in order. Its sides are equal and its angles are right angles (D1.22). Join AC (P1).

**Step 2.** Circumscribe a circle about triangle ABC, and let O be its centre (4.5). Path choice: use the previously established triangle-circumcircle construction, then identify its diameter by the angle classification in 3.31.

**Step 3.** Since ∠ABC is right, AC must be a diameter of this circle. Indeed, otherwise the circular segment bounded by AC and the arc through B would be either greater or less than a semicircle; 3.31 would then make ∠ABC respectively less or greater than a right angle, contrary to Step 1. Thus O lies on AC, between A and C (3.31, D1.17).

**Step 4.** In triangles ABC and ADC, AB = AD and BC = DC because ABCD is a square, while AC is common. Therefore ∠BCA = ∠DCA by 1.8. SSS is the natural choice here because all three corresponding sides are already known equal (D1.22, 1.8).

**Step 5.** Join OB and OD (P1). Since O lies between A and C, Step 4 gives ∠BCO = ∠DCO. In triangles BCO and DCO, BC = DC, CO is common, and these included angles are equal. Hence OB = OD by 1.4 (D1.22, 1.4).

**Step 6.** B lies on the constructed circle, so OB is its radius. Since OD = OB, D also lies on that circle (D1.15). Its circumference therefore passes through all four vertices A, B, C, D. Consequently it is circumscribed about the given square, as required (D4.6).

**USED:** 1.4, 1.8, 3.31, 4.5, D1.15, D1.17, D1.22, D4.6, P1
**Human refs (from References field):** 1.6, 1.8
**Jaccard:** 0.100 — AI adds ['1.4', '3.31', '4.5', 'D1.15', 'D1.17', 'D1.22', 'D4.6', 'P1']; Human adds ['1.6']

## Proposition 4.10
**Statement:** To construct an isosceles triangle having each of the angles at the base double of the remaining one.

**Step 1.** Let AB be a given straight-line segment. By 2.11, cut AB at an interior point D so that the rectangle contained by AB and BD equals the square on AD. Since D is interior, AD < AB (CN5).

**Step 2.** Construct on AB a triangle ABC with AC = AB and BC = AD (1.22). The required triangle inequalities hold: AB + AD > AB, and AB + AB > AD, since AD is a positive proper part of AB (CN5). Because AB = AC, the base angles satisfy ∠ABC = ∠ACB (1.5).

**Step 3.** Join CD (P1), and circumscribe a circle about triangle ACD (4.5). Since A, D, B occur in that order on their straight line, B is outside this circle, and its secant BA meets the circle first at D and then at A. By Step 1 and BC = AD, the rectangle contained by BA and BD equals the square on BC (CN1). Therefore BC touches the circle at C (3.37). **Path choice:** 3.37 applies directly because the constructed rectangle–square equality is precisely its hypothesis.

**Step 4.** Apply the tangent–chord theorem to the tangent CB and chord CD. Since A and B lie on opposite sides of CD, it gives ∠BCD = ∠CAD (3.32). As AD lies along AB, ∠CAD is the apex angle ∠CAB.

**Step 5.** In triangle ACD, DB extends AD beyond D. Hence its exterior angle satisfies
∠CDB = ∠CAD + ∠ACD (1.32).
Replacing ∠CAD by ∠BCD from Step 4 gives
∠CDB = ∠BCD + ∠ACD = ∠ACB (CN2).
But ∠ACB = ∠ABC by Step 2, and ∠ABC is the same angle as ∠CBD. Thus ∠CDB = ∠CBD (CN1). Consequently, in triangle BCD, BC = CD (1.6). Together with BC = AD, this gives AD = CD (CN1).

**Step 6.** Since AD = CD, triangle ACD has ∠ACD = ∠CAD (1.5). Step 4 also gives ∠BCD = ∠CAD. Therefore
∠ACB = ∠ACD + ∠DCB = ∠CAD + ∠CAD = 2∠CAB (CN2).
Since ∠ABC = ∠ACB, it follows that ∠ABC = 2∠CAB as well (CN1). Finally, AB = AC while BC = AD < AB, so ABC is an isosceles triangle with base BC (D1.20), and each angle at its base is double the remaining angle, as required.

**USED:** 1.22, 1.32, 1.5, 1.6, 2.11, 3.32, 3.37, 4.5, CN1, CN2, CN5, D1.20, P1
**Human refs (from References field):** 1.32, 1.5, 1.6, 2.11, 3.32, 3.37, 4.5
**Jaccard:** 0.538 — AI adds ['1.22', 'CN1', 'CN2', 'CN5', 'D1.20', 'P1']

## Proposition 4.11
**Statement:** In a given circle to inscribe an equilateral and equiangular pentagon.

**Step 1.** Let Γ be the given circle. Construct an isosceles triangle XYZ whose angles at Y and Z are each double its angle at X [4.10]. This is the direct starting construction, since it supplies the required double-angle relation without rebuilding it from elementary constructions.

**Step 2.** Inscribe in Γ a triangle ACD equiangular with XYZ, with A corresponding to X, C to Y, and D to Z [4.2]. Write θ = ∠CAD. Then ∠ACD and ∠CDA are each equal to θ + θ [4.10, 4.2, CN1].

**Step 3.** Bisect ∠ACD and ∠CDA, and produce their internal bisectors to meet Γ again at E and B, respectively [1.9, P2]. Thus E lies on the arc DA not containing C, and B lies on the arc AC not containing D; the five points consequently occur around Γ in the order A, B, C, D, E. The bisections and the double-angle relations give
∠ACE = ∠ECD = ∠CDB = ∠BDA = ∠CAD = θ.
Indeed, each pair of equal halves has sum θ + θ, so each half equals θ: a greater or smaller half would give a greater or smaller double [CN1, CN2, CN5].

**Step 4.** Hereafter, an arc between consecutive named vertices means the arc containing none of the other vertices. The equal angles ∠CAD, ∠CDB, ∠BDA, ∠ACE, and ∠ECD stand respectively upon the arcs CD, CB, BA, AE, and ED [D3.9]. Equal angles at the circumference cut off equal arcs; hence
arc AB = arc BC = arc CD = arc DE = arc EA [3.26].
This passage from angles to arcs is the natural next step, because the resulting arc equalities establish both required properties.

**Step 5.** Join AB, BC, DE, and EA, retaining CD as the fifth side [P1]. Equal arcs in the same circle are subtended by equal straight lines [3.29]. Therefore
AB = BC = CD = DE = EA,
so ABCDE is equilateral.

**Step 6.** The arcs BCDE, CDEA, DEAB, EABC, and ABCD each consist of three consecutive arcs from the five equal arcs established in Step 4. They are therefore equal by addition of equals [CN2]. The interior angles EAB, ABC, BCD, CDE, and DEA stand respectively upon these five arcs [D3.9]. Angles at the circumference standing upon equal arcs are equal [3.27]. Consequently all five interior angles of ABCDE are equal, so the pentagon is equiangular.

**Step 7.** All five vertices of ABCDE lie on Γ by construction; hence the pentagon is inscribed in Γ [D4.3]. Together with Steps 5 and 6, this proves that an equilateral and equiangular pentagon has been inscribed in the given circle.

**USED:** 1.9, 3.26, 3.27, 3.29, 4.10, 4.2, CN1, CN2, CN5, D3.9, D4.3, P1, P2
**Human refs (from References field):** 1.9, 3.26, 3.27, 3.29, 4.10, 4.2
**Jaccard:** 0.462 — AI adds ['CN1', 'CN2', 'CN5', 'D3.9', 'D4.3', 'P1', 'P2']

## Proposition 4.12
**Statement:** About a given circle to circumscribe an equilateral and equiangular pentagon.

**Step 1.** Let Γ be the given circle. Inscribe in it an equilateral and equiangular pentagon A₀A₁A₂A₃A₄, with the vertices named in their cyclic order [4.11]. Throughout, subscripts are taken modulo five. Join the diagonals needed to form the triangles Aᵢ₋₁AᵢAᵢ₊₁ [P1]. Write β for the common interior angle of the pentagon. **Path choice:** use this already constructed inscribed pentagon and draw tangents at its vertices; the tangent–chord theorem will supply the angles needed to compare the exterior triangles directly.

**Step 2.** The five triangles Aᵢ₋₁AᵢAᵢ₊₁ have two corresponding sides equal and their included angles equal to β. Hence their corresponding angles are equal by 1.4, which applies directly to the given side–angle–side data. Each triangle is isosceles, so its two base angles are equal [1.5]. Thus all these base angles have one common value, α. The two base angles together are less than two right angles [1.17], and the angle sum of any one of these triangles gives α + β + α equal to two right angles [1.32].

**Step 3.** Draw the tangent tᵢ to Γ at each Aᵢ [3.17]. Consider the consecutive tangents tᵢ and tᵢ₊₁, with the chord AᵢAᵢ₊₁ as transversal. On the side of this chord opposite the other vertices, the angles made by the tangents with the chord are both equal to ∠AᵢAᵢ₊₂Aᵢ₊₁, by the tangent–chord theorem [3.32]. This inscribed angle is α by Step 2. Since the two angles together are less than two right angles, the tangents, produced as necessary, meet on that side [P2, P5]. Call their intersection Xᵢ. Consequently, triangle AᵢXᵢAᵢ₊₁ has both base angles equal to α.

**Step 4.** At Aᵢ, the rays toward Xᵢ₋₁ and Xᵢ lie outside the interior angle ∠Aᵢ₋₁AᵢAᵢ₊₁ on its two respective sides. The successive angles from AᵢXᵢ₋₁ through the two chords to AᵢXᵢ are α, β, and α. Their sum is two right angles by Step 2; therefore the two tangent rays are opposite [1.14]. Thus Aᵢ lies between Xᵢ₋₁ and Xᵢ. In their cyclic order, the five tangent segments therefore form the outer pentagon X₀X₁X₂X₃X₄, with Aᵢ on its side Xᵢ₋₁Xᵢ.

**Step 5.** Since the base angles of each triangle AᵢXᵢAᵢ₊₁ are equal, its two tangent sides are equal: XᵢAᵢ = XᵢAᵢ₊₁ [1.6]. Moreover, all five such triangles have equal bases, by Step 1, and equal angles at both ends of their bases, by Step 3. Apply 1.26: the known equal side lies between the known equal angles, so this is the direct comparison. Their corresponding remaining sides and their vertex angles are equal. Together with the equality within each triangle, this shows that all ten tangent segments XᵢAᵢ and XᵢAᵢ₊₁ have one common length, and all angles ∠AᵢXᵢAᵢ₊₁ are equal [1.26, CN1].

**Step 6.** Each side Xᵢ₋₁Xᵢ is the sum of the two tangent segments Xᵢ₋₁Aᵢ and AᵢXᵢ. Since all these segments are equal, all five sides of the outer pentagon are equal [CN2]. By the betweenness established in Step 4, its interior angle at Xᵢ is precisely ∠AᵢXᵢAᵢ₊₁; hence its five interior angles are equal by Step 5. Finally, every side Xᵢ₋₁Xᵢ touches Γ at Aᵢ, so the pentagon is circumscribed about Γ [D4.4]. Therefore an equilateral and equiangular pentagon has been circumscribed about the given circle.

**USED:** 1.14, 1.17, 1.26, 1.32, 1.4, 1.5, 1.6, 3.17, 3.32, 4.11, CN1, CN2, D4.4, P1, P2, P5
**Human refs (from References field):** 1.26, 1.47, 1.8, 3.1, 3.16, 3.18, 3.27, 4.11
**Jaccard:** 0.091 — AI adds ['1.14', '1.17', '1.32', '1.4', '1.5', '1.6', '3.17', '3.32', 'CN1', 'CN2', 'D4.4', 'P1', 'P2', 'P5']; Human adds ['1.47', '1.8', '3.1', '3.16', '3.18', '3.27']

## Proposition 4.13
**Statement:** In a given pentagon, which is equilateral and equiangular, to inscribe a circle.

**Step 1.** Let ABCDE be the given equilateral and equiangular pentagon, with vertices named in boundary order, and denote each interior angle by 2h. Draw AC and AD (P1). Adding the angle sums of triangles ABC, ACD, and ADE shows that the pentagon’s five interior angles together equal six right angles (1.32, CN2). Hence 2h is less than two right angles, and h is less than one right angle. Our route is to intersect adjacent internal angle bisectors, then establish equal perpendicular distances from their intersection to the five sides.

**Step 2.** Bisect angles ABC and BCD (1.9), and produce the bisecting lines as necessary (P2). Their angles with BC, on its interior side, are h and h. Since their sum is less than two right angles, the bisecting rays meet on that side at a point O (P5). Thus ∠ABO = ∠OBC = ∠BCO = ∠OCD = h. In particular, O lies on the interior side of each of AB, BC, and CD.

**Step 3.** Join OA and OD (P1). In triangles ABO and CBO, AB = CB, BO is common, and ∠ABO = ∠CBO. Therefore ∠BAO = ∠BCO = h (1.4). Since O lies on the interior side of AB, AO lies within angle BAE; subtracting ∠BAO from that angle gives ∠OAE = h (CN3). Similarly, triangles DCO and BCO have DC = BC, CO common, and ∠DCO = ∠BCO. Hence ∠CDO = ∠CBO = h (1.4). Since O lies on the interior side of CD, DO lies within angle CDE, and ∠ODE = h (CN3). Thus AO and DO bisect the angles at A and D. These facts also place O on the interior sides of EA and DE; consequently O is inside the pentagon.

**Step 4.** Join OE (P1). Triangles EAO and BAO have EA = BA, AO common, and ∠EAO = ∠BAO = h. Therefore ∠AEO = ∠ABO = h (1.4). Since O is inside the pentagon, EO lies within angle AED; subtracting ∠AEO from that angle gives ∠OED = h (CN3). Thus the lines from O to the vertices bisect all five interior angles.

**Step 5.** Draw OF, OG, OH, OI, and OJ perpendicular to the lines AB, BC, CD, DE, and EA respectively (1.12). Each foot lies strictly within its corresponding side segment. Indeed, both base angles of the triangle formed by O and the endpoints of any side equal h, which is less than a right angle. If the perpendicular foot were an endpoint, that base angle would be right (D1.10). If it lay beyond an endpoint, the base angle there would be an exterior angle of a right triangle and therefore greater than its opposite right angle (1.16). Both possibilities are impossible.

**Step 6.** Triangles OBF and OBG have equal angles h at B, equal right angles at F and G (P4), and the common side OB opposite those right angles. Hence OF = OG (1.26). Applying the same proposition to triangles OCG and OCH, to ODH and ODI, and to OAF and OAJ gives, respectively, OG = OH, OH = OI, and OF = OJ (1.26). Consequently OF = OG = OH = OI = OJ (CN1).

**Step 7.** Describe the circle with centre O and radius OF (P3). By the established equalities, it passes through F, G, H, I, and J (D1.15). Each corresponding side is perpendicular to the radius at that point. Therefore AB, BC, CD, DE, and EA touch the circle at F, G, H, I, and J respectively (3.16). The perpendicular-to-radius tangency conclusion of 3.16 applies directly here, since perpendicularity has already been established.

**Step 8.** The constructed circle touches all five sides at points lying on the side segments. It is therefore inscribed in the given equilateral and equiangular pentagon (D4.5), as required.

**USED:** 1.12, 1.16, 1.26, 1.32, 1.4, 1.9, 3.16, CN1, CN2, CN3, D1.10, D1.15, D4.5, P1, P2, P3, P4, P5
**Human refs (from References field):** 1.26, 1.4, 3.16
**Jaccard:** 0.167 — AI adds ['1.12', '1.16', '1.32', '1.9', 'CN1', 'CN2', 'CN3', 'D1.10', 'D1.15', 'D4.5', 'P1', 'P2', 'P3', 'P4', 'P5']

## Proposition 4.14
**Statement:** About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.

**Step 1.** Let ABCDE be the given equilateral and equiangular pentagon, with its vertices in order. By 4.13, inscribe a circle in it, touching AB, BC, CD, DE, EA at X, Y, Z, U, V respectively; find its centre O by 3.1. We choose this route because the inscribed circle supplies equal perpendicular distances to all five sides, avoiding a fresh construction of a centre.

**Step 2.** Join O to the five vertices and to the five points of contact [P1]. Since OX, OY, OZ, OU, OV are radii of the inscribed circle, they are equal [D1.15]. Each is perpendicular to the corresponding side at its point of contact [3.18].

**Step 3.** The right triangles OXA and OVA have the common hypotenuse OA and equal legs OX and OV. By 1.47,
OA² = OX² + AX² and OA² = OV² + AV².
Subtracting the equal squares on the radii gives AX² = AV², and hence AX = AV [CN3]. Applying the same argument at B, C, D, E gives BX = BY, CY = CZ, DZ = DU, and EU = EV [1.47, CN3]. Write these equal tangent lengths as
AX = AV = a, BX = BY = b, CY = CZ = c, DZ = DU = d, EU = EV = e.

**Step 4.** The five side lengths are therefore a + b, b + c, c + d, d + e, e + a. Since the pentagon is equilateral, AB = BC gives a = c; BC = CD gives b = d; CD = DE gives c = e; and DE = EA gives d = a, in each case by cancelling the common segment [CN3]. Consequently a = b = c = d = e [CN1]. In particular, AX = BY = CZ = DU = EV.

**Step 5.** Compare the right triangles OXA, OYB, OZC, OUD, OVE. Their respective radius legs are equal by Step 2, and their respective legs along the pentagon's sides are equal by Step 4. The included right angles are equal [P4]. Thus these triangles are congruent by the side-angle-side proposition 1.4, and their hypotenuses satisfy OA = OB = OC = OD = OE [CN1].

**Step 6.** Describe the circle with centre O and radius OA [P3]. Because all five distances OA, OB, OC, OD, OE are equal, its circumference passes through A, B, C, D, E [D1.15]. It is therefore circumscribed about the given pentagon [D4.6], as required.

**USED:** 1.4, 1.47, 3.1, 3.18, 4.13, CN1, CN3, D1.15, D4.6, P1, P3, P4
**Human refs (from References field):** 1.6
**Jaccard:** 0.000 — AI adds ['1.4', '1.47', '3.1', '3.18', '4.13', 'CN1', 'CN3', 'D1.15', 'D4.6', 'P1', 'P3', 'P4']; Human adds ['1.6']

## Proposition 4.15
**Statement:** In a given circle to inscribe an equilateral and equiangular hexagon.

**Step 1.** Choose the route of inscribing an equiangular triangle and bisecting its three intervening arcs. On an auxiliary segment construct an equilateral triangle XYZ by 1.1. Its three angles are equal by 1.5 and CN1.

**Step 2.** In the given circle inscribe a triangle ACE equiangular with XYZ by 4.2. Thus ∠ACE, ∠CEA, and ∠EAC are equal (CN1).

**Step 3.** Let arc AC mean the arc not containing E, arc CE the arc not containing A, and arc EA the arc not containing C. These three arcs are equal because the equal angles ∠AEC, ∠CAE, and ∠ECA stand upon them (3.26). This angle-to-arc proposition applies directly to the equality supplied by Step 2, without an intermediate comparison of chords.

**Step 4.** Bisect these arcs at B, D, and F respectively (3.30). The six points therefore occur in the order A, B, C, D, E, F around the circumference. Since the three original arcs are equal and each has been divided into two equal parts, their six halves are equal:
arc AB = arc BC = arc CD = arc DE = arc EF = arc FA.
Indeed, unequal halves would, upon addition to their respective equal partners, give unequal wholes, contrary to Step 3 (CN2, CN5; CN1).

**Step 5.** Join AB, BC, CD, DE, EF, and FA (P1). Equal arcs in the same circle are subtended by equal straight lines (3.29). Hence AB = BC = CD = DE = EF = FA, so the hexagon ABCDEF is equilateral.

**Step 6.** Each interior angle of this hexagon stands upon the arc between its neighbouring vertices that does not contain its own vertex (D3.9). For example, ∠FAB stands upon arc BCDEF. Each such intercepted arc consists of four of the six equal arcs from Step 4; consequently all six intercepted arcs are equal (CN2, CN1). Angles standing upon equal arcs in the same circle are equal (3.27). Therefore the six interior angles of ABCDEF are equal, and the hexagon is equiangular.

**Step 7.** All six vertices lie on the given circumference, so ABCDEF is inscribed in the given circle (D4.3). By Steps 5 and 6, it is equilateral and equiangular. Thus the required hexagon has been constructed.

**USED:** 1.1, 1.5, 3.26, 3.27, 3.29, 3.30, 4.2, CN1, CN2, CN5, D3.9, D4.3, P1
**Human refs (from References field):** 1.15, 1.32, 1.5, 3.26, 3.27, 3.29
**Jaccard:** 0.267 — AI adds ['1.1', '3.30', '4.2', 'CN1', 'CN2', 'CN5', 'D3.9', 'D4.3', 'P1']; Human adds ['1.15', '1.32']

## Proposition 4.16
**Statement:** In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular.

**Step 1.** Let the given circle have circumference S. Inscribe an equilateral and equiangular pentagon and an equilateral and equiangular hexagon, starting both constructions at a chosen point A (4.11, 4.15). Fix one direction around the circle. Let B be the next pentagon vertex after A, and C the second hexagon vertex after A. Our path choice is to use two adjacent hexagon arcs to obtain a third of the circumference, thereby avoiding a separate auxiliary triangle construction.

**Step 2.** Equal chords cut off equal minor arcs (3.28). Thus the pentagon divides the circumference into five equal successive arcs, and the hexagon divides it into six equal successive arcs. Write p for the pentagon arc AB and t for the arc AC consisting of two successive hexagon arcs. By addition of equal arcs,
S = 5p = 3t (CN2).
Consequently t is greater than p: otherwise 3t would be at most 3p, which is less than 5p (CN2, CN5). Therefore B lies between A and C on the chosen arc AC.

**Step 3.** Bisect the remaining arc BC at D (3.30), and write s for each of the equal arcs BD and DC. Then t = p + 2s. Hence
3p + 6s = 3t = S = 5p,
so subtracting 3p gives 6s = 2p (CN2, CN3). Therefore 3s = p: if either were greater, its double would also be greater, contrary to the preceding equality (CN2, CN5). It follows that
S = 5p = 15s (CN2).
Thus fifteen copies of arc BD exactly constitute the circumference.

**Step 4.** Join BD (P1), and call its length q. Since BD is a chord of the given circle, q is not greater than its diameter (3.15). Beginning with X₀ = B and X₁ = D, successively fit chords of length q into the circle, taking each preceding endpoint as the next starting point and proceeding in the fixed direction along minor arcs (4.1). Continue until fifteen chords have been fitted, with successive endpoints X₀, X₁, …, X₁₅.

**Step 5.** Each successive minor arc equals arc BD, because its chord equals BD (3.28). Each is therefore s. Since S = 15s, fewer than fifteen such arcs cannot complete the circumference, whereas fifteen complete it exactly (CN2, CN5). Consequently X₀, …, X₁₄ are distinct and X₁₅ = X₀. The resulting closed polygon has fifteen sides, all equal to q and therefore equal to one another (4.1, CN1).

**Step 6.** At any vertex Xᵢ, with indices read cyclically, the interior angle stands upon the arc from Xᵢ₋₁ to Xᵢ₊₁ which does not contain Xᵢ (D3.9). That arc consists of the other thirteen successive arcs. All such intercepted arcs are therefore equal, each being the sum of thirteen arcs equal to s (CN2). Angles standing upon equal arcs of the same circle are equal (3.27). Hence all fifteen interior angles of the polygon are equal.

**Step 7.** Every vertex of the constructed polygon lies on the circumference of the given circle, so the polygon is inscribed in it (D4.3). By Steps 5 and 6 it is both equilateral and equiangular. Thus the required fifteen-angled figure has been inscribed.

**USED:** 3.15, 3.27, 3.28, 3.30, 4.1, 4.11, 4.15, CN1, CN2, CN3, CN5, D3.9, D4.3, P1
**Human refs (from References field):** 3.30
**Jaccard:** 0.071 — AI adds ['3.15', '3.27', '3.28', '4.1', '4.11', '4.15', 'CN1', 'CN2', 'CN3', 'CN5', 'D3.9', 'D4.3', 'P1']
