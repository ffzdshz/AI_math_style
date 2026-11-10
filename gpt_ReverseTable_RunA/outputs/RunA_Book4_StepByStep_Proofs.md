# Book 4 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 4.1
**Statement:** Into a given circle to fit a straight line equal to a given straight line which is not greater than the diameter of the circle.

**Step 1.** Let Γ be the given circle and let ℓ be the given straight line, not greater than its diameter. Find the centre O of Γ, and draw through O a straight line terminating at A and B on the circumference. Thus AB is a diameter. [3.1, P1, P2, D1.17]

**Step 2.** If ℓ equals AB, take AB itself: it has the required length and both its extremities lie on Γ, so it is fitted into the circle. [D4.7]

**Step 3.** Otherwise ℓ is less than AB. From AB cut off AE equal to ℓ, with E between A and B. This uses the direct cutting-off construction, since the greater straight line AB is already available. [1.3]

**Step 4.** Describe a circle with centre A and radius AE. It meets Γ: A is inside this auxiliary circle, whereas B is outside it because AB is greater than AE, so the circumference of Γ passes from inside to outside it. Let C be a point where the two circumferences meet, and join AC. [P3, P1]

**Step 5.** Since E and C lie on the circle with centre A, AC equals AE. But AE equals ℓ; therefore AC equals ℓ. Moreover, A and C both lie on Γ, so AC is fitted into Γ. Thus a straight line equal to the given straight line has been fitted into the given circle, as required. [D1.15, CN1, D4.7]

**USED:** 1.3, 3.1, CN1, D1.15, D1.17, D4.7, P1, P2, P3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.3', '3.1', 'CN1', 'D1.15', 'D1.17', 'D4.7', 'P1', 'P2', 'P3']

## Proposition 4.2
**Statement:** In a given circle to inscribe a triangle equiangular with a given triangle.

**Step 1.** Let the given circle be κ and the given triangle be DEF. Choose a point A on κ and draw the tangent at A, producing it in both directions to points X and Y, with A between them. We choose the tangent–chord route because it directly converts constructed angles at A into angles of an inscribed triangle. [3.17, P2]

**Step 2.** The angles DEF and DFE together are less than two right angles, since the three angles of triangle DEF equal two right angles. [1.32, CN5] On the side of XY containing the circle, construct a ray AC such that ∠XAC = ∠DEF. Since ∠XAC and ∠CAY together equal two right angles, ∠DFE is less than ∠CAY. Therefore construct a ray AB within ∠CAY such that ∠YAB = ∠DFE. Produce the rays to meet the circle again at C and B, respectively. Their order on this side of the tangent is AY, AB, AC, AX, so B and C are distinct. [1.23, 1.13, P2]

**Step 3.** Join B to C. Thus ABC is a triangle whose vertices lie on κ. [P1]

**Step 4.** Apply the tangent–chord theorem to AC and the tangent ray AX. The point B lies in the alternate segment, so ∠ABC = ∠XAC. Apply the same theorem to AB and the tangent ray AY. The point C lies in the alternate segment, so ∠ACB = ∠YAB. Consequently, by the constructed equalities, ∠ABC = ∠DEF and ∠ACB = ∠DFE. [3.32, CN1]

**Step 5.** The angles of each of triangles ABC and DEF sum to two right angles. The sums ∠ABC + ∠ACB and ∠DEF + ∠DFE are equal. Subtracting these equal sums from the equal totals gives ∠BAC = ∠EDF. Thus ABC is equiangular with DEF. [1.32, CN2, CN3]

**Step 6.** Since A, B, and C all lie on the circumference of κ, triangle ABC is inscribed in κ. It is therefore the required inscribed triangle equiangular with the given triangle DEF. [D4.3]

**USED:** 1.13, 1.23, 1.32, 3.17, 3.32, CN1, CN2, CN3, CN5, D4.3, P1, P2
**Human refs (from References field):** 1.23, 1.32, 3.16, 3.32
**Jaccard:** 0.231 — AI adds ['1.13', '3.17', 'CN1', 'CN2', 'CN3', 'CN5', 'D4.3', 'P1', 'P2']; Human adds ['3.16']

## Proposition 4.3
**Statement:** About a given circle to circumscribe a triangle equiangular with a given triangle.

**Step 1.** Let the given triangle be DEF, with angles α, β, γ at D, E, F respectively, and let R denote a right angle. We take the direct route: copy exterior angles at the centre of the circle, then draw perpendicular tangents. Produce a side at D and a side at F. The resulting exterior angles are 2R−α and 2R−γ. Also α+β+γ=2R, so each of α, β, γ, and each of these exterior angles, lies strictly between zero and 2R. [P2, P4, 1.13, 1.32, CN3]

**Step 2.** Find the centre O of the given circle, choose A on its circumference, and join OA. On opposite sides of OA construct angles AOB=2R−α and AOC=2R−γ, taking B and C where the constructed rays meet the circumference. Since the angles about O total 4R, the remaining sector BOC, not containing OA, equals
4R−(2R−α)−(2R−γ)=α+γ=2R−β.
Thus the successive central sectors AOB, BOC, COA have angles 2R−α, 2R−β, 2R−γ; each is less than 2R. [3.1, P1, 1.23, 1.13, P4, 1.32, CN2, CN3]

**Step 3.** Produce the radii to diameters and draw lines t_A, t_B, t_C through A, B, C perpendicular to OA, OB, OC respectively. Each perpendicular falls outside the circle and therefore touches it at its designated point. This perpendicular construction is the natural choice because the contact points have already been fixed. [P2, 1.11, 3.16, D3.2]

**Step 4.** Join AB, BC, CA. We verify that the tangent lines form a triangle whose sides contain the contact points. In triangle OAB, the radii OA and OB are equal, so its base angles are equal; call each u. If θ=∠AOB, then 2u+θ=2R, whence u<R. On the side of AB opposite O, the tangents at A and B consequently make angles R−u with AB. Their sum is 2R−2u=θ<2R; therefore the tangents meet on that side. Call their intersection X. Apply the same reasoning to BC and CA, obtaining Y=t_B∩t_C and Z=t_C∩t_A.

These meetings use the tangent rays directed into the respective central sectors. Since the three sectors are consecutive and each is less than 2R, the meetings belonging to the two sectors adjacent to any radius lie on opposite rays of its tangent. Consequently A lies between Z and X, B between X and Y, and C between Y and Z. Thus X, Y, Z form a triangle with the three contact points on its sides. [P1, D1.15, 1.5, 1.32, CN3, P5]

**Step 5.** In triangle AXB, the angles at A and B have sum θ=2R−α, as established above. Its angle at X therefore equals α. The same argument in triangles BYC and CZA gives angles β at Y and γ at Z. Because A, B, C lie between the corresponding vertices, these are precisely the interior angles of triangle XYZ. Hence XYZ is equiangular with DEF. [1.32, CN3]

**Step 6.** The sides XZ, XY, YZ touch the given circle at A, B, C respectively. Therefore triangle XYZ is circumscribed about the circle and, by Step 5, is equiangular with the given triangle DEF. The required construction is complete. [D4.4]

**USED:** 1.11, 1.13, 1.23, 1.32, 1.5, 3.1, 3.16, CN2, CN3, D1.15, D3.2, D4.4, P1, P2, P4, P5
**Human refs (from References field):** 1.13, 1.23, 1.32, 3.1, 3.16, 3.18
**Jaccard:** 0.294 — AI adds ['1.11', '1.5', 'CN2', 'CN3', 'D1.15', 'D3.2', 'D4.4', 'P1', 'P2', 'P4', 'P5']; Human adds ['3.18']

## Proposition 4.4
**Statement:** In a given triangle to inscribe a circle.

**Step 1.** Let ABC be the given triangle. Use the route of two internal angle bisectors: bisect ∠ABC and ∠BCA. Their halves together are less than two right angles, since the original two angles are already less than two right angles. Hence the bisector rays meet, by the parallel postulate, at a point I on the same side of BC as A. Since both rays lie inside their respective vertex angles, I is inside triangle ABC. [1.9, 1.17, P5]

**Step 2.** From I draw perpendiculars IE, IF, IG to the straight lines AB, BC, CA, respectively. The feet E and F lie on the rays BA and BC, and the feet F and G lie on the rays CB and CA. Indeed, each bisector makes an acute angle with either bounding ray; a foot on the opposite ray would therefore give a right triangle with an obtuse angle at the vertex, contradicting the fact that two angles of a triangle are less than two right angles. For now, the feet need not be assumed to lie on the finite sides. [1.12, 1.13, 1.17]

**Step 3.** Compare triangles BIE and BIF. Their angles at B are equal because BI bisects ∠ABC; their angles at E and F are right and therefore equal; and BI is common. Apply 1.26, the direct fit to these two equal angles and the common side. It follows that IE = IF. [1.9, P4, 1.26]

**Step 4.** Similarly, triangles CIF and CIG have equal angles at C, equal right angles at F and G, and the common side CI. Thus IF = IG. Consequently IE = IF = IG. [1.9, P4, 1.26, CN1]

**Step 5.** Describe the circle with centre I and distance IE. Since IE, IF, and IG are equal, this circle passes through E, F, and G. [P3, D1.15]

**Step 6.** The lines AB, BC, and CA are perpendicular at E, F, and G to the respective radii. Each radius lies along a diameter, so 3.16 applies directly: a perpendicular at the extremity of a diameter falls outside the circle. Thus each of these three lines meets the circle at its indicated point without cutting it, and therefore touches it. This is the direct tangency criterion supplied by the constructed perpendiculars. [3.16, D3.2]

**Step 7.** The circle lies on the same side of each tangent line as its centre I. Since I is inside ABC, these are precisely the three inward half-planes whose intersection is the triangle. Hence the circle lies within ABC; in particular, E, F, and G lie on the finite sides AB, BC, and CA. Its circumference therefore touches every side of the triangle, so the circle is inscribed in ABC, as required. [3.16, D4.5]

**USED:** 1.12, 1.13, 1.17, 1.26, 1.9, 3.16, CN1, D1.15, D3.2, D4.5, P3, P4, P5
**Human refs (from References field):** 1.26, 1.9, 3.16, D4.5
**Jaccard:** 0.308 — AI adds ['1.12', '1.13', '1.17', 'CN1', 'D1.15', 'D3.2', 'P3', 'P4', 'P5']

## Proposition 4.5
**Statement:** About a given triangle to circumscribe a circle.

**Step 1.** Let ABC be the given triangle. We take the direct route of constructing the perpendicular bisectors of two sides. Bisect AB at D and AC at E, so that AD = DB and AE = EC. [1.10]

**Step 2.** Through D draw a straight line p perpendicular to AB, and through E draw a straight line q perpendicular to AC. Produce these lines in both directions as necessary. [1.11, P2, D1.10]

**Step 3.** The lines p and q must meet. For suppose they do not; they are then parallel. If AC were parallel to p, it would also be parallel to q, since straight lines parallel to the same straight line are parallel to one another. But AC meets q at E. Thus AC is not parallel to p and, when produced if necessary, meets p at a point F. Since AC is perpendicular to q and p is parallel to q, the equality of angles made by a transversal of parallel lines shows that AC is perpendicular to p at F. Now F is distinct from A and D, and triangle ADF has right angles at both D and F. This contradicts the fact that any two angles of a triangle are together less than two right angles. Therefore p and q meet; call an intersection O. [D1.23, 1.30, P2, 1.29, D1.10, 1.17]

**Step 4.** Join OA, OB, and OC. If O = D, then OA = OB immediately from AD = DB. Otherwise, in triangles ODA and ODB, OD is common, AD = DB, and the included angles ODA and ODB are right angles and hence equal. Consequently OA = OB by side–angle–side. This is the natural comparison: the midpoint equalities and the common perpendicular already give the two sides and their included angle. [P1, 1.10, D1.10, P4, 1.4]

**Step 5.** Likewise, if O = E, then OA = OC from AE = EC. Otherwise, triangles OEA and OEC have OE common, AE = EC, and equal included right angles at E. Side–angle–side therefore gives OA = OC. [1.10, D1.10, P4, 1.4]

**Step 6.** Describe the circle with centre O and distance OA. Since OB = OA and OC = OA, its circumference passes through A, B, and C. It is therefore circumscribed about triangle ABC, as required. [P3, D1.15, D4.6]

**USED:** 1.10, 1.11, 1.17, 1.29, 1.30, 1.4, D1.10, D1.15, D1.23, D4.6, P1, P2, P3, P4
**Human refs (from References field):** 1.10, 1.4
**Jaccard:** 0.143 — AI adds ['1.11', '1.17', '1.29', '1.30', 'D1.10', 'D1.15', 'D1.23', 'D4.6', 'P1', 'P2', 'P3', 'P4']

## Proposition 4.6
**Statement:** In a given circle to inscribe a square.

**Step 1.** Let the given circle have centre O, found by 3.1. Choose A on its circumference, join AO, and produce it through O to meet the circumference again at C. Thus AC is a diameter. [3.1, P1, P2, D1.17]

**Step 2.** At O draw a perpendicular to AC, meeting the circumference at B, and produce BO through O to meet the circumference again at D. Then BD is another diameter. The angles AOB and BOC are right by the perpendicular construction; their vertically opposite angles COD and DOA are also right. Consequently all four central angles are equal. The points A, B, C, D occur successively around the circle. [1.11, P2, D1.17, D1.10, 1.15, P4]

**Step 3.** Join AB, BC, CD, and DA. Since O is the centre, OA, OB, OC, and OD are equal. Choose the direct side-angle-side route: the central triangles already have equal pairs of radial sides and equal included right angles. Applying 1.4 to triangle AOB and each of triangles BOC, COD, and DOA gives AB = BC, AB = CD, and AB = DA. Hence ABCD is equilateral. [P1, D1.15, D1.16, 1.4, CN1]

**Step 4.** Since AC is a diameter, angles ABC and ADC are angles in semicircles, and therefore are right. Since BD is a diameter, angles BAD and BCD likewise are right. Thus ABCD is right-angled. [D1.17, D1.18, 3.31]

**Step 5.** The quadrilateral ABCD is both equilateral and right-angled, so it is a square. Its four vertices lie on the circumference of the given circle, so it is inscribed in that circle. Therefore a square has been inscribed in the given circle, as required. [D1.22, D4.3]

**USED:** 1.11, 1.15, 1.4, 3.1, 3.31, CN1, D1.10, D1.15, D1.16, D1.17, D1.18, D1.22, D4.3, P1, P2, P4
**Human refs (from References field):** 1.4, 3.31, D1.22
**Jaccard:** 0.188 — AI adds ['1.11', '1.15', '3.1', 'CN1', 'D1.10', 'D1.15', 'D1.16', 'D1.17', 'D1.18', 'D4.3', 'P1', 'P2', 'P4']

## Proposition 4.7
**Statement:** About a given circle to circumscribe a square.

**Step 1.** Let the given circle have centre O, found by 3.1. Choose A on its circumference, join AO, and produce it through O to meet the circle again at C. Through O draw the perpendicular to AC, meeting the circle at B and D, with A, B, C, D in cyclic order. Thus AC and BD are perpendicular diameters. [3.1, P1, P2, 1.11]

**Step 2.** At A and C draw straight lines a and c perpendicular to AC; at B and D draw straight lines b and d perpendicular to BD. Each such line meets the circle at its designated endpoint and otherwise falls outside it, so each touches the circle there. We use the perpendicular-at-a-diameter-endpoint route directly, since 3.16 is the first applicable tangency result for these already chosen points. [1.11, 3.16, D3.2]

**Step 3.** Since all right angles are equal, 1.28 gives a ∥ BD and c ∥ BD, and likewise b ∥ AC and d ∥ AC. Hence a ∥ c and b ∥ d. No line of the first pair can be parallel to a line of the second pair: otherwise transitivity of parallelism would make AC parallel to BD, although they meet at O. Consequently adjacent tangents intersect. Set E = a ∩ b, F = b ∩ c, G = c ∩ d, and H = d ∩ a. These form a parallelogram EFGH. The opposite tangent pairs lie on opposite sides of O, so A, B, C, D lie respectively on the side segments HE, EF, FG, GH. [P4, 1.28, 1.30, D1.23]

**Step 4.** The lines a and c are perpendicular to AC, while b and d are parallel to AC. Applying 1.29 to these parallels shows that the angles at E, F, G, and H are all right angles. Thus EFGH is right-angled. [1.29]

**Step 5.** The radii OA, OB, OC, and OD are equal. Adding OA = OB to OC = OD gives OA + OC = OB + OD; therefore AC = BD. [D1.15, CN2]

**Step 6.** The quadrilateral AEFC is a parallelogram: AE ∥ FC because a ∥ c, and EF ∥ AC because b ∥ AC. Its opposite sides therefore give EF = AC. Similarly, BFGD is a parallelogram because BF ∥ GD and FG ∥ BD, so FG = BD. Since AC = BD, it follows that EF = FG. Finally, opposite sides of the parallelogram EFGH are equal, so EF = GH and FG = HE. Hence all four sides of EFGH are equal. [1.34, CN1]

**Step 7.** The quadrilateral EFGH is both equilateral and right-angled, and therefore is a square. Its four sides touch the given circle at A, B, C, and D respectively; hence it is circumscribed about that circle. Thus a square has been circumscribed about the given circle, as required. [D1.22, D4.4]

**USED:** 1.11, 1.28, 1.29, 1.30, 1.34, 3.1, 3.16, CN1, CN2, D1.15, D1.22, D1.23, D3.2, D4.4, P1, P2, P4
**Human refs (from References field):** 1.28, 1.30, 1.34, 3.16, 3.18
**Jaccard:** 0.222 — AI adds ['1.11', '1.29', '3.1', 'CN1', 'CN2', 'D1.15', 'D1.22', 'D1.23', 'D3.2', 'D4.4', 'P1', 'P2', 'P4']; Human adds ['3.18']

## Proposition 4.8
**Statement:** In a given square to inscribe a circle.

**Step 1.** Let ABCD be the given square, with vertices in order. Its sides are equal and its angles are right angles. Consequently AB is parallel to CD, and AD is parallel to BC, since the corresponding interior angles sum to two right angles. [D1.22, 1.28]

**Step 2.** We use midpoints and parallels, because this construction gives four equal perpendicular distances to the sides directly. Bisect AB at E and AD at F. Since AB = AD, their halves are equal, so
AE = EB = AF = FD.
Indeed, if either half were greater than the other, the sum of its two equal halves would also be greater, contradicting AB = AD. [1.10, D1.22, CN1, CN2, CN5]

**Step 3.** Through E draw EH parallel to AD, meeting CD at H. Through F draw FK parallel to AB, meeting BC at K. Let G be the intersection of EH and FK inside the square. Since straight lines parallel to the same straight line are parallel to one another, AEGF, EBKG, and FDHG are parallelograms. [1.31, 1.30]

**Step 4.** Opposite sides of these parallelograms are equal. From AEGF we obtain GE = AF and GF = AE; from EBKG, GK = EB; and from FDHG, GH = FD. Hence
GE = GF = GK = GH.
Moreover, the parallels and the right angles of the square give GE perpendicular to AB, GF perpendicular to AD, GK perpendicular to BC, and GH perpendicular to CD. [1.34, CN1, 1.29]

**Step 5.** Describe the circle with centre G and radius GE. The equalities just established show that F, K, and H also lie on its circumference. Since E, G, H are collinear and F, G, K are collinear, EH and FK are diameters of this circle. [P3, D1.15, D1.17]

**Step 6.** Apply the diameter-endpoint criterion directly: a straight line perpendicular to a diameter at its extremity falls outside the circle. Thus AB, AD, BC, and CD meet the circle respectively at E, F, K, and H without cutting it; each therefore touches the circle. The circle lies within the square and touches all four sides, so it is inscribed in ABCD, as required. [3.16, D3.2, D4.5]

**USED:** 1.10, 1.28, 1.29, 1.30, 1.31, 1.34, 3.16, CN1, CN2, CN5, D1.15, D1.17, D1.22, D3.2, D4.5, P3
**Human refs (from References field):** 1.10, 1.31, 1.34, 3.16
**Jaccard:** 0.250 — AI adds ['1.28', '1.29', '1.30', 'CN1', 'CN2', 'CN5', 'D1.15', 'D1.17', 'D1.22', 'D3.2', 'D4.5', 'P3']

## Proposition 4.9
**Statement:** About a given square to circumscribe a circle.

**Step 1.** Let ABCD be the given square, with its vertices in order. Its four sides are equal and its four angles are right angles. Join the diagonals AC and BD, and let E be their intersection. We take E as the prospective centre and use side–angle–side comparisons, since the square directly supplies equal sides and equal included right angles. [D1.22, P1]

**Step 2.** Compare triangles ABC and BAD. The side AB is common, BC equals AD, and the included angles ABC and BAD are equal, being right angles. Therefore, by side–angle–side, ∠BAC = ∠ABD. Since E lies on AC and BD, this gives ∠EAB = ∠ABE. [P4, 1.4]

**Step 3.** Likewise, compare triangles BCD and CBA: BC is common, CD equals BA, and their included angles are right angles. Hence ∠CBD = ∠BCA, so ∠EBC = ∠ECB. Finally, compare triangles CDA and DCB: CD is common, DA equals CB, and their included angles are right angles. Hence ∠DCA = ∠CDB, so ∠ECD = ∠EDC. [P4, 1.4]

**Step 4.** Applying the theorem that equal angles in a triangle subtend equal sides to triangles EAB, EBC, and ECD respectively, we obtain EA = EB, EB = EC, and EC = ED. Thus EA = EB = EC = ED. [1.6, CN1]

**Step 5.** Describe the circle with centre E and distance EA. Because B, C, and D are each at the same distance from E as A, this circle passes through all four vertices of the square. It is therefore circumscribed about ABCD, as required. [P3, D1.15, D4.6]

**USED:** 1.4, 1.6, CN1, D1.15, D1.22, D4.6, P1, P3, P4
**Human refs (from References field):** 1.6, 1.8
**Jaccard:** 0.100 — AI adds ['1.4', 'CN1', 'D1.15', 'D1.22', 'D4.6', 'P1', 'P3', 'P4']; Human adds ['1.8']

## Proposition 4.10
**Statement:** To construct an isosceles triangle having each of the angles at the base double of the remaining one.

**Step 1.** Take a straight line AB. By 2.11, cut it at C so that the rectangle contained by AB and BC equals the square on AC:
AB·BC = AC².
Here C lies between A and B, and AC < AB. [2.11, CN5]

**Step 2.** Describe the circle with centre A and radius AB. Since AC is less than AB, and therefore less than the diameter, fit in this circle a chord BD equal to AC. Join AD and CD. The radii AB and AD are equal, so
∠ABD = ∠BDA.
[P3, D1.17, CN5, 4.1, P1, D1.15, 1.5]

**Step 3.** Circumscribe a circle Γ about triangle ACD. Since A, C, B occur in that order on a straight line, B is outside Γ; the secant from B meets Γ first at C and then at A. Now
BA·BC = AC² = BD².
Consequently BD touches Γ at D, by the converse tangent criterion. This is the direct criterion to use because the rectangle–square equality is already known and tangency is required. [4.5, CN1, 3.37]

**Step 4.** Apply the tangent–chord theorem to the tangent DB and chord DC of Γ. It gives
∠BDC = ∠CAD.
Since C lies on the side AB of triangle ABD, DC divides its angle at D. Hence
∠BDA = ∠BDC + ∠CDA = ∠CAD + ∠CDA.
[3.32, CN2]

**Step 5.** Because AC is extended through C to B, the exterior-angle clause of 1.32 applies directly to triangle ACD:
∠BCD = ∠CAD + ∠CDA.
Thus ∠BCD = ∠BDA. Also, by Step 2 and the coincidence of rays BC and BA,
∠CBD = ∠ABD = ∠BDA.
Therefore ∠BCD = ∠CBD, and their opposite sides in triangle BCD are equal: BD = CD. [1.32, 1.5, CN1, 1.6]

**Step 6.** Since BD = AC by construction and CD = BD, we have CD = AC. Triangle ACD is therefore isosceles, and
∠CDA = ∠CAD.
[CN1, 1.5]

**Step 7.** Substituting this equality into Step 4 gives
∠BDA = ∠CAD + ∠CAD = 2∠BAD,
since rays AC and AB coincide. Step 2 then gives ∠ABD = 2∠BAD as well. Finally, AB = AD, while BD = AC < AB. Thus ABD is an isosceles triangle having each angle at its base BD double the remaining angle at A, as required. [CN2, CN1, 1.5, D1.20]

**USED:** 1.32, 1.5, 1.6, 2.11, 3.32, 3.37, 4.1, 4.5, CN1, CN2, CN5, D1.15, D1.17, D1.20, P1, P3
**Human refs (from References field):** 1.32, 1.5, 1.6, 2.11, 3.32, 3.37, 4.5
**Jaccard:** 0.438 — AI adds ['4.1', 'CN1', 'CN2', 'CN5', 'D1.15', 'D1.17', 'D1.20', 'P1', 'P3']

## Proposition 4.11
**Statement:** In a given circle to inscribe an equilateral and equiangular pentagon.

**Step 1.** Choose the direct angle-construction route, since 4.10 supplies the required angle ratio. Construct an isosceles triangle whose base angles are each double its remaining angle, and inscribe in the given circle a triangle ACD equiangular with it. Label it so that, writing α = ∠CAD, we have ∠ACD = ∠CDA = 2α. [4.10, 4.2]

**Step 2.** Bisect ∠CDA and ∠ACD internally. Extend their bisectors to meet the circle again at B and E, respectively. Thus B lies on the arc AC not containing D, and E lies on the arc AD not containing C; the cyclic order is A, B, C, D, E. Join AB, BC, DE, and EA. By the bisections and the angle relations of Step 1,
∠ADB = ∠BDC = ∠CAD = ∠DCE = ∠ECA = α. [1.9, P2, P1, CN1]

**Step 3.** These five equal angles stand, respectively, on the consecutive arcs AB, BC, CD, DE, and EA. Equal angles at the circumference stand on equal arcs; hence these five arcs are equal. This uses the angle-to-arc result directly, because the construction has already supplied equal angles. [3.26, CN1]

**Step 4.** Equal arcs are subtended by equal straight lines. Consequently AB = BC = CD = DE = EA, so the pentagon ABCDE is equilateral. [3.29]

**Step 5.** Each interior angle of the pentagon stands on the arc between its adjacent vertices that does not contain its own vertex. These arcs are:
• for ∠EAB: BC + CD + DE;
• for ∠ABC: CD + DE + EA;
• for ∠BCD: DE + EA + AB;
• for ∠CDE: EA + AB + BC;
• for ∠DEA: AB + BC + CD.
Since the five elementary arcs are equal, these sums of three arcs are equal. Angles at the circumference standing on equal arcs are equal, so all five interior angles of ABCDE are equal. [CN2, 3.27]

**Step 6.** All five vertices lie on the given circumference, so ABCDE is inscribed in the circle. By Steps 4 and 5 it is equilateral and equiangular. Thus an equilateral and equiangular pentagon has been inscribed in the given circle, as required. [D4.3]

**USED:** 1.9, 3.26, 3.27, 3.29, 4.10, 4.2, CN1, CN2, D4.3, P1, P2
**Human refs (from References field):** 1.9, 3.26, 3.27, 3.29, 4.10, 4.2
**Jaccard:** 0.545 — AI adds ['CN1', 'CN2', 'D4.3', 'P1', 'P2']

## Proposition 4.12
**Statement:** About a given circle to circumscribe an equilateral and equiangular pentagon.

**Step 1.** In the given circle inscribe an equilateral and equiangular pentagon ABCDE, with its vertices in circular order (4.11). Join AC, BD, CE, DA, and EB (P1). We use the direct tangent–chord route: the inscribed pentagon supplies equal chords, and the tangent–chord theorem will supply the angles needed to compare the exterior triangles.

**Step 2.** Write θ for the common interior angle of ABCDE. The triangles ABC, BCD, CDE, DEA, and EAB have two corresponding sides equal and their included angles equal, so their corresponding angles are equal (1.4). Moreover, AB = BC, so the two base angles of ABC are equal (1.5). Consequently, all the base angles of these five triangles have one common value, β. By the angle sum of triangle ABC,
θ + β + β = two right angles (1.32).
In particular, β + β is less than two right angles (CN5).

**Step 3.** Draw tangents to the circle at A, B, C, D, and E (3.17). For each consecutive chord, take the rays of its endpoint tangents lying on the side of that chord opposite the other vertices of the inscribed pentagon. By the tangent–chord theorem, the two angles these rays make with the chord equal an angle standing on that chord in the alternate segment (3.32). For AB use ∠ACB; for BC use ∠BDC; for CD use ∠CED; for DE use ∠DAE; and for EA use ∠EBA. Step 2 shows that each of these angles is β. Thus, for every consecutive chord, both exterior tangent–chord angles are β.

**Step 4.** Produce the tangent rays as necessary (P2). Since their two interior angles with each consecutive chord total β + β, less than two right angles, the tangents meet on the chosen exterior side (P5). Denote their intersections by P for AB, Q for BC, R for CD, S for DE, and T for EA.
At A, the successive angles from AT through AE and AB to AP total β + θ + β, which is two right angles. Hence AT and AP are opposite rays (1.14). The same argument applies at every contact point. Therefore the orders on the five tangent sides are T–A–P, P–B–Q, Q–C–R, R–D–S, and S–E–T. These sides form the surrounding pentagon PQRST, with each contact point lying on its corresponding side.

**Step 5.** Each of the triangles PAB, QBC, RCD, SDE, and TEA has both base angles equal to β, so its two tangent sides are equal (1.6). Their bases AB, BC, CD, DE, and EA are also equal. Apply 1.26 to these triangles: this is the natural comparison because a base and its two adjacent angles are already known equal. Their corresponding tangent sides and their vertex angles are therefore equal. Combining these equalities, all ten tangent segments PA, PB, QB, QC, RC, RD, SD, SE, TE, and TA are equal (CN1).

**Step 6.** Each side of PQRST is the sum of two of those equal tangent segments:
PQ = PB + BQ, QR = QC + CR, RS = RD + DS, ST = SE + ET, and TP = TA + AP.
Hence all five sides are equal (CN2). Its interior angles are respectively the vertex angles of PAB, QBC, RCD, SDE, and TEA, since the contact points lie between consecutive vertices. These angles are equal by Step 5 (1.26). Thus PQRST is equilateral and equiangular. Each of its sides touches the given circle, so it is circumscribed about that circle (D4.4). Therefore an equilateral and equiangular pentagon has been circumscribed about the given circle, as required.

**USED:** 1.14, 1.26, 1.32, 1.4, 1.5, 1.6, 3.17, 3.32, 4.11, CN1, CN2, CN5, D4.4, P1, P2, P5
**Human refs (from References field):** 1.26, 1.47, 1.8, 3.1, 3.16, 3.18, 3.27, 4.11
**Jaccard:** 0.091 — AI adds ['1.14', '1.32', '1.4', '1.5', '1.6', '3.17', '3.32', 'CN1', 'CN2', 'CN5', 'D4.4', 'P1', 'P2', 'P5']; Human adds ['1.47', '1.8', '3.1', '3.16', '3.18', '3.27']

## Proposition 4.13
**Statement:** In a given pentagon, which is equilateral and equiangular, to inscribe a circle.

**Step 1.** Let ABCDE be the given equilateral and equiangular pentagon, with vertices in order, and let α denote half its common interior angle. Choose the direct angle-bisector construction, which will provide equal perpendicular distances to the sides. Bisect ∠ABC and ∠BCD by inward rays meeting at O (1.9). These rays meet on the interior side of BC because their angles with BC sum to one interior angle of the pentagon, less than two right angles (P5). Join OA, OD, and OE (P1).

**Step 2.** In triangles ABO and CBO, AB = CB, BO is common, and ∠ABO = ∠CBO. Hence, by 1.4, ∠BAO = ∠BCO = α. Since O is on the interior side of AB, AO lies within ∠BAE. Subtracting ∠BAO from that whole angle gives ∠OAE = α; thus AO bisects the angle at A (CN3).

**Step 3.** In triangles BCO and DCO, BC = DC, CO is common, and ∠BCO = ∠DCO. Hence ∠CDO = ∠CBO = α (1.4). Since O is on the interior side of CD, DO lies within ∠CDE, and subtraction gives ∠ODE = α (CN3). Thus DO bisects the angle at D. The original bisectors place O on the interior sides of AB, BC, and CD; the bisections just established place it on the interior sides of AE and DE also. Therefore O is inside the pentagon.

**Step 4.** In triangles BAO and EAO, BA = EA, AO is common, and ∠BAO = ∠EAO. Consequently ∠AEO = ∠ABO = α (1.4). Subtracting this from the whole angle AED gives ∠OED = α (CN3). Hence EO also bisects its vertex angle. Thus the lines from O to all five vertices bisect their respective interior angles.

**Step 5.** Draw OP, OQ, OR, OS, and OT perpendicular respectively to the straight lines AB, BC, CD, DE, and EA, producing those lines as necessary for the construction (P2, 1.12). Each foot lies strictly on its corresponding side segment. Indeed, both endpoint angles in each triangle formed by O and a side equal α and are acute. A foot beyond an endpoint would make the angle at that endpoint an exterior angle of a right triangle, hence greater than a right angle by 1.16. A foot at an endpoint would make that endpoint angle right. Both are impossible.

**Step 6.** Consider triangles OBP and OBQ. Their angles at P and Q are equal right angles (P4), their angles at B are equal because BO bisects ∠ABC, and OB is common. Apply 1.26, the natural criterion here because two equal angles and the common side opposite the right angles are already known. It gives OP = OQ. Applying the same proposition to triangles OCQ and OCR, ODR and ODS, and OES and OET gives OQ = OR, OR = OS, and OS = OT. Therefore OP = OQ = OR = OS = OT (CN1).

**Step 7.** Describe the circle with centre O and distance OP (P3). Since all five perpendicular distances are equal, this circle passes through P, Q, R, S, and T (D1.15).

**Step 8.** The diameter through each of these points is collinear with its radius from O (P2, D1.17). Each corresponding side of the pentagon is therefore perpendicular to a diameter at its extremity and, by 3.16, falls outside the circle apart from that point. Thus each side touches the circle (D3.2). Its circumference consequently touches all five sides of ABCDE, so it is inscribed in the given pentagon (D4.5), as required.

**USED:** 1.12, 1.16, 1.26, 1.4, 1.9, 3.16, CN1, CN3, D1.15, D1.17, D3.2, D4.5, P1, P2, P3, P4, P5
**Human refs (from References field):** 1.26, 1.4, 3.16
**Jaccard:** 0.176 — AI adds ['1.12', '1.16', '1.9', 'CN1', 'CN3', 'D1.15', 'D1.17', 'D3.2', 'D4.5', 'P1', 'P2', 'P3', 'P4', 'P5']

## Proposition 4.14
**Statement:** About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.

**Step 1.** Let ABCDE be the given equilateral and equiangular pentagon, with vertices in order, and let θ denote its common interior angle. Use adjacent internal angle bisectors, which supply the included angles for direct side–angle–side comparisons. Bisect ∠BCD and ∠CDE. Their half-angles adjoining CD sum to θ, less than two right angles; therefore the bisectors meet at F on the interior side of CD. Join FB, FA, and FE. (1.9, P5, P1)

**Step 2.** Since ∠FCD = θ/2 = ∠CDF, the sides opposite these equal angles in triangle CDF are equal. Hence FC = FD. (1.6)

**Step 3.** Compare triangles BCF and DCF. We have BC = DC, CF common, and ∠BCF = ∠DCF because CF bisects ∠BCD. Therefore BF = DF and ∠CBF = ∠CDF = θ/2. Together with Step 2, this gives BF = FC = FD. (1.4, CN1)

**Step 4.** Because CF is internal to ∠BCD, F lies on the same side of BC as A. Since ∠CBF = θ/2 while ∠ABC = θ, BF lies within ∠ABC, and subtraction gives ∠ABF = θ/2 = ∠CBF. Now triangles ABF and CBF have AB = CB, BF common, and equal included angles. Consequently AF = CF. (CN3, 1.4)

**Step 5.** Compare triangles CDF and EDF. We have CD = ED, DF common, and ∠CDF = ∠EDF because DF bisects ∠CDE. Therefore CF = EF. (1.4)

**Step 6.** Thus FA = FB = FC = FD = FE. Describe the circle with centre F and distance FC. All five vertices A, B, C, D, E lie on its circumference, since their distances from F equal its radius. Hence this circle is circumscribed about the given pentagon, as required. (CN1, P3, D1.15, D4.6)

**USED:** 1.4, 1.6, 1.9, CN1, CN3, D1.15, D4.6, P1, P3, P5
**Human refs (from References field):** 1.6
**Jaccard:** 0.100 — AI adds ['1.4', '1.9', 'CN1', 'CN3', 'D1.15', 'D4.6', 'P1', 'P3', 'P5']

## Proposition 4.15
**Statement:** In a given circle to inscribe an equilateral and equiangular hexagon.

**Step 1.** Construct an equilateral triangle on any nonzero segment. Applying the isosceles-triangle theorem to its equal sides shows that its three angles are equal. [1.1, 1.5, CN1]

**Step 2.** In the given circle inscribe a triangle ACE equiangular with that triangle, naming its vertices in cyclic order. Thus the angles CAE, ACE, and CEA are equal. We choose this triangle-and-arc-bisection route because the equal inscribed angles give equal arcs directly, without first needing to establish equal chords. [4.2]

**Step 3.** Let the arc AC mean the arc not containing E, the arc CE the arc not containing A, and the arc EA the arc not containing C. These arcs are equal, since they are intercepted respectively by the equal angles AEC, CAE, and ACE in the same circle. [3.26]

**Step 4.** Bisect these three arcs at B, D, and F respectively. The six points consequently occur in the cyclic order A, B, C, D, E, F, and the six successive arcs AB, BC, CD, DE, EF, FA are equal. Indeed, each pair consists of equal halves of one of the equal arcs from Step 3; unequal halves would, when each was added to its equal fellow, give unequal wholes. [3.30, CN2, CN5]

**Step 5.** Join AB, BC, CD, DE, EF, and FA. Equal arcs in the same circle are subtended by equal straight lines; hence AB = BC = CD = DE = EF = FA. Therefore ABCDEF is equilateral. [P1, 3.29]

**Step 6.** Each interior angle of ABCDEF stands on the arc between its adjacent vertices which does not contain its own vertex. Every such arc consists of four of the six equal successive arcs: for example, angle FAB stands on BCDEF, while angle ABC stands on CDEFA. These intercepted arcs are therefore equal, by addition of equals. Angles at the circumference standing on equal arcs are equal, so all six interior angles of ABCDEF are equal. [CN2, 3.27]

**Step 7.** All six vertices lie on the circumference of the given circle, so ABCDEF is inscribed in it. By Steps 5 and 6 it is both equilateral and equiangular. Thus an equilateral and equiangular hexagon has been inscribed in the given circle, as required. [D4.3]

**USED:** 1.1, 1.5, 3.26, 3.27, 3.29, 3.30, 4.2, CN1, CN2, CN5, D4.3, P1
**Human refs (from References field):** 1.15, 1.32, 1.5, 3.26, 3.27, 3.29
**Jaccard:** 0.286 — AI adds ['1.1', '3.30', '4.2', 'CN1', 'CN2', 'CN5', 'D4.3', 'P1']; Human adds ['1.15', '1.32']

## Proposition 4.16
**Statement:** In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular.

**Step 1.** Let the given circle be Γ. Use the triangle–pentagon route, obtaining the triangle directly from the earlier triangle-inscription construction. Construct an equilateral triangle by 1.1; its angles are equal by 1.5. Inscribe in Γ a triangle equiangular with it by 4.2, and call one vertex A. Thus the inscribed triangle has three equal angles. [1.1, 1.5, 4.2]

**Step 2.** Inscribe an equilateral and equiangular pentagon in Γ, taking A as one of its vertices. Choose a direction around Γ; let B be the next triangle vertex and C the next pentagon vertex. The triangle’s equal angles stand on equal circumferences, so its three successive arcs are equal. The pentagon’s equal sides likewise cut off five equal successive arcs. Consequently, if L denotes the whole circumference, arc AB is L/3 and arc AC is L/5, measured in the chosen direction, and C lies between A and B. Here fractions denote equal parts of the same circumference. [4.11, 3.26, 3.28]

**Step 3.** Subtracting arc AC from arc AB gives
arc CB = L/3 − L/5 = 2L/15.
Bisect arc CB at D. Then each of arcs CD and DB is L/15. Join C to D. Thus CD is a constructed chord subtending exactly one fifteenth of the circumference. [CN2, CN3, 3.30, P1]

**Step 4.** Since CD is a chord, it is not greater than the diameter. Therefore, starting with C and D, fit chords equal to CD successively into Γ, always proceeding in the chosen direction and taking the minor arc at each fitting. This is the direct chord-fitting construction of 4.1. Equal chords cut off equal minor arcs, so every successive arc equals arc CD, namely L/15. Fifteen such arcs make the whole circumference; fewer than fifteen do not. Hence the fifteenth chord returns to C, and the preceding endpoints are fourteen distinct further vertices. These fifteen equal chords therefore form an equilateral fifteen-sided figure. [3.15, 4.1, 3.28, CN2]

**Step 5.** At each vertex of this figure, the interior angle stands on the arc between its two neighboring vertices which does not contain that vertex. This arc consists of thirteen of the fifteen equal elementary arcs: it is the whole circumference with the two adjacent elementary arcs removed. Such intercepted arcs are equal at every vertex, by addition and subtraction of equals. Angles standing at the circumference on equal circumferences are equal; therefore all fifteen interior angles are equal. [CN2, CN3, 3.27]

**Step 6.** Every vertex lies on Γ, so the figure is inscribed in the given circle. By Steps 4 and 5 it is both equilateral and equiangular. Thus the required fifteen-angled figure has been constructed. [D4.3]

**USED:** 1.1, 1.5, 3.15, 3.26, 3.27, 3.28, 3.30, 4.1, 4.11, 4.2, CN2, CN3, D4.3, P1
**Human refs (from References field):** 3.30
**Jaccard:** 0.071 — AI adds ['1.1', '1.5', '3.15', '3.26', '3.27', '3.28', '4.1', '4.11', '4.2', 'CN2', 'CN3', 'D4.3', 'P1']
