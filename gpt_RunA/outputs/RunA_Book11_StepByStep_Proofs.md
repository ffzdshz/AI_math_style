# Book 11 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 11.1
**Statement:** A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 1.** We use contradiction, comparing straight continuations rather than introducing angles or perpendiculars. Suppose that a straight line ABC has its part AB in the reference plane Π, but its continuation BC elevated above Π. Thus AB and BC are assumed to form one straight line, lying evenly with its points. [D1.4]

**Step 2.** Produce AB beyond B continuously in a straight line within Π, and call this in-plane continuation r. The production is permitted by P2, made in the reference plane, which lies evenly with the straight lines on itself. [P2, D1.7]

**Step 3.** Both r and BC are straight continuations of the same nonzero segment AB beyond the same endpoint B. They therefore cannot diverge: a continuation departing from the alignment fixed by A and B would not lie evenly with the points of the original segment and its continuation. Hence BC coincides with the corresponding part of r. [D1.4]

**Step 4.** Since r lies in Π, this coincidence puts BC in Π also, contrary to the supposition that BC is elevated above Π. Therefore a part of a straight line cannot be in the plane of reference and another part in a plane more elevated. [Steps 1–3]

**USED:** D1.4, D1.7, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D1.4', 'D1.7', 'P2']

## Proposition 11.2
**Statement:** If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

**Step 1.** Let the distinct straight lines ℓ and m cut one another at O. Choose A on m, different from O and therefore not on ℓ. Through A draw a straight line n parallel to ℓ. [1.31] This is the chosen route because the definition of parallel lines explicitly supplies a common plane. [D1.23]

**Step 2.** Since ℓ and n are parallel, they lie in one plane Π. Thus O belongs to Π because it is on ℓ, and A belongs to Π because it is on n. [D1.23]

**Step 3.** Join O to A in Π. The straight segment OA lies in Π and is a part of m. [P1, D1.7] A straight line cannot have one part in a plane and another part elevated from it; consequently the whole of m lies in Π. [11.1] Hence the two intersecting straight lines ℓ and m lie in one plane.

**Step 4.** Now let ABC be any triangle. Its sides AB and AC meet at A, so the argument of Steps 1–3 places them in one plane Σ. In particular, A, B, and C belong to Σ. [Steps 1–3]

**Step 5.** Since B and C belong to Σ, their straight join BC also lies in Σ. [P1, D1.7] Thus all three sides, and the triangular figure bounded by them, lie in Σ. [D1.19] Therefore two straight lines which cut one another are in one plane, and every triangle is in one plane.

**USED:** 1.31, 11.1, D1.19, D1.23, D1.7, P1
**Human refs (from References field):** 11.1
**Jaccard:** 0.167 — AI adds ['1.31', 'D1.19', 'D1.23', 'D1.7', 'P1']

## Proposition 11.3
**Statement:** If two planes cut one another, their common section is a straight line.

**Step 1.** Let the distinct planes Π and Σ cut one another, and let s be their common section. Choose two distinct points A and B on s, draw AB, and produce it to the straight line ℓ [P1, P2]. Our route is to use 11.1 to exclude any common point outside ℓ: a straight line cannot have a segment in a plane and then leave that plane.

**Step 2.** Since A and B belong to both planes, the segment AB lies in each plane, by the defining straightness property of a plane [D1.7]. Its straight continuation cannot leave either plane [11.1]. Consequently, ℓ is contained in the common section s.

**Step 3.** Suppose there is a point C of s outside ℓ. Join CA and CB [P1]. These segments lie in both planes [D1.7]. Moreover, for every point D on the segment AB, the joining segment CD lies in both planes [P1, D1.7]. These segments fill the triangular region ABC, so that entire region is common to the two planes. Because C is outside AB, this is a nondegenerate triangular region, with interior points in each plane [D1.19].

**Step 4.** Since Π and Σ are distinct, some point X belongs to one but not the other; interchange their names if necessary so that X belongs to Π but not Σ. Choose an interior point O of the common triangle and join OX in Π [P1, D1.7]. Since O is interior to the triangle, a nonzero initial segment of OX lies within that triangle and therefore in Σ [Step 3]. But X is outside Σ. Thus the straight line OX has a part in Σ and another part outside it, contrary to 11.1.

**Step 5.** Therefore no point of s lies outside ℓ [Steps 3–4]. Conversely, ℓ lies in s [Step 2]. Hence the common section is exactly the straight line ℓ. Thus, if two planes cut one another, their common section is a straight line.

**USED:** 11.1, D1.19, D1.7, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['11.1', 'D1.19', 'D1.7', 'P1', 'P2']

## Proposition 11.4
**Statement:** If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

**Step 1.** Let the distinct straight lines a and b meet at O, and let r be perpendicular to both at O. Let π be a plane containing a and b; such a plane exists by 11.2. The line r cannot lie in π: otherwise, rays of a and b chosen on opposite sides of r would make two adjacent right angles with a ray of r, and hence would form one straight line by 1.14, contradicting the distinctness of a and b. Moreover, r meets π only at O: a second common point would place the intervening segment in π, and then the whole line r in π (D1.7, 11.1).

**Step 2.** Let t be any straight line in π through O, distinct from a and b. Choose rays of a and b enclosing one ray of t, and take points B and C on those respective rays. Join BC (P1); it lies in π (D1.7). The chosen ray of t makes with OB an angle smaller than ∠BOC (CN5). Since ∠BOC together with ∠OBC is less than two right angles (1.17), the angle between OB and that ray of t, together with ∠OBC, is also less than two right angles. Consequently, t meets the ray BC at a point X on the chosen side of OB (P5). In particular, X ≠ O, and BX and BC are the same ray.

**Step 3.** Choose A on r, distinct from O, and produce AO through O to A′ so that OA′ = OA (P2, 1.3). Join AB, AC, A′B, A′C, AX, and A′X (P1). Every triangle used below is planar by 11.2. Our path is to compare triangles using these equal opposite segments on r, ultimately obtaining equal adjacent angles at O.

**Step 4.** The angles AOB, A′OB, AOC, and A′OC are right angles, by the hypotheses, the definition of perpendicularity, and equality of vertically opposite angles (D1.10, 1.15). They are therefore equal (P4). In triangles AOB and A′OB, OA = OA′ and OB is common (CN4), so AB = A′B by 1.4. Likewise, applying 1.4 to triangles AOC and A′OC gives AC = A′C.

**Step 5.** Triangles ABC and A′BC have AB = A′B, AC = A′C, and BC common (CN4). Their three corresponding sides are therefore equal, so ∠ABC = ∠A′BC by 1.8. This is the natural congruence criterion here because all three side equalities are already available.

**Step 6.** Since BX and BC are the same ray, ∠ABX = ∠ABC and ∠A′BX = ∠A′BC (CN4). Thus ∠ABX = ∠A′BX (CN1). Now AB = A′B and BX is common (CN4); hence triangles ABX and A′BX give AX = A′X by 1.4.

**Step 7.** In triangles AOX and A′OX, OA = OA′ by construction, AX = A′X by Step 6, and OX is common (CN4). Therefore ∠AOX = ∠A′OX by 1.8. Since OA and OA′ are opposite rays, these are equal adjacent angles; consequently each is right, and r is perpendicular to t (D1.10).

**Step 8.** The line t was arbitrary among the lines of π through O other than a and b, and r is perpendicular to a and b by hypothesis. Since O is the only point where r meets π, r therefore makes right angles with every straight line in π that meets it. Thus r is at right angles to π, the plane through the two given lines (D11.3).

**USED:** 1.14, 1.15, 1.17, 1.3, 1.4, 1.8, 11.1, 11.2, CN1, CN4, CN5, D1.10, D1.7, D11.3, P1, P2, P4, P5
**Human refs (from References field):** 1.15, 1.26, 1.4, 1.8, D11.3
**Jaccard:** 0.211 — AI adds ['1.14', '1.17', '1.3', '11.1', '11.2', 'CN1', 'CN4', 'CN5', 'D1.10', 'D1.7', 'P1', 'P2', 'P4', 'P5']; Human adds ['1.26']

## Proposition 11.5
**Statement:** If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

**Step 1.** Let a, b, and c be the three straight lines meeting at O, and let n be perpendicular to each at O. The intersecting lines a and b lie in a plane Π. [Hypothesis; 11.2]

**Step 2.** Since n is perpendicular to both a and b at their intersection, n is perpendicular to Π. We choose 11.4 because it applies immediately to two of the given lines. [11.4]

**Step 3.** Suppose, for a contradiction, that c does not lie in Π. The intersecting lines n and c lie in a plane Σ, which is distinct from Π because it contains c. [11.2; supposition]

**Step 4.** The planes Π and Σ meet at O, and their common section is a straight line d through O. Since d lies in Π and meets n at O, n is perpendicular to d. [11.3; Step 2; D11.3]

**Step 5.** Extend c and d through O, and in Σ choose points C on c and D on d on opposite sides of n. Choose N distinct from O on n. The adjacent angles CON and NOD are both right: the first by hypothesis and the second by Step 4. Their sum is therefore two right angles, so OC and OD lie in one straight line. We use 1.14 because its opposite-side and two-right-angle conditions are exactly those obtained here. [P2; hypothesis; Step 4; 1.14]

**Step 6.** Consequently c is the same straight line as d and therefore lies in Π, contradicting Step 3. Hence c lies in Π together with a and b: the three straight lines are in one plane. [Steps 1, 3–5]

**USED:** 1.14, 11.2, 11.3, 11.4, D11.3, P2
**Human refs (from References field):** 11.3, 11.4, D11.3
**Jaccard:** 0.500 — AI adds ['1.14', '11.2', 'P2']

## Proposition 11.6
**Statement:** If two straight lines be at right angles to the same plane, the straight lines will be parallel.

**Step 1.** Let l and m be distinct straight lines perpendicular to a plane Π, meeting it at A and B respectively (D11.3). The feet A and B are distinct. For if both were O, the intersecting lines l and m would lie in a plane Σ (11.2), different from Π. The common section of Σ and Π would be a straight line t through O (11.3). Both l and m would be perpendicular to t (D11.3). Taking their rays on opposite sides of t, the adjacent angles they make with a ray of t would together equal two right angles; hence those rays would form one straight line (1.14), contrary to l and m being distinct.

**Step 2.** Join AB; it lies in Π (P1, D1.7). In Π construct a straight line through B perpendicular to AB (1.11). Produce it in both directions and take points C and D on opposite sides of B such that BC = BD (P2, 1.3). Choose X on l outside Π and off m, and join AC, AD, XC, XD, and XB (P1).

**Step 3.** In triangles ABC and ABD, AB is common, BC = BD, and the included angles ABC and ABD are right angles, hence equal (P4). Therefore AC = AD by side-angle-side congruence (1.4).

**Step 4.** The triangles XAC and XAD are each planar (11.2). Since l is perpendicular to Π, the angles XAC and XAD are right angles (D11.3), and therefore equal (P4). Together with the common side XA and AC = AD, side-angle-side congruence gives XC = XD (1.4).

**Step 5.** The triangles XBC and XBD have XB common, BC = BD, and XC = XD. Hence their angles at B are equal by side-side-side congruence (1.8). The intersecting straight lines XB and CD lie in one plane (11.2). Since BC and BD are opposite rays, these equal angles are adjacent angles on CD; thus XB is perpendicular to CD (D1.10).

**Step 6.** At B, the straight line CD is perpendicular to BA by construction, to BX by Step 5, and to m because CD lies in Π (D11.3). Consequently BA, BX, and m lie in one plane Σ (11.5). Both A and X belong to Σ, so AX lies in Σ (D1.7), and the whole straight line l lies there (11.1). Thus l and m are coplanar. This establishes the necessary spatial condition before applying a planar parallelism criterion.

**Step 7.** In Σ, the transversal AB makes right angles with both l and m (D11.3). Their two interior angles on the same side of AB therefore equal two right angles. This directly supplies the criterion of 1.28, so l and m are parallel. Therefore two straight lines perpendicular to the same plane are parallel.

**USED:** 1.11, 1.14, 1.28, 1.3, 1.4, 1.8, 11.1, 11.2, 11.3, 11.5, D1.10, D1.7, D11.3, P1, P2, P4
**Human refs (from References field):** 1.28, 1.4, 1.8, 11.2, 11.5, D11.3
**Jaccard:** 0.375 — AI adds ['1.11', '1.14', '1.3', '11.1', '11.3', 'D1.10', 'D1.7', 'P1', 'P2', 'P4']

## Proposition 11.7
**Statement:** If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

**Step 1.** Let ℓ and m be the given parallel straight lines, and let A on ℓ and B on m be arbitrary points. By the definition of parallels, ℓ and m lie in a common plane Π and do not meet, even when produced indefinitely. Thus B does not lie on ℓ. [D1.23]

**Step 2.** Join A to B by the straight line AB. [P1] Since AB and ℓ meet at A and are distinct, they lie in a plane Σ. [11.2] This is the intersecting-lines route: 11.2 applies immediately to the joining line and one given line.

**Step 3.** Suppose Σ were different from Π. Since both planes contain ℓ, they intersect, and their common section is a straight line. [11.3] That section contains ℓ and therefore lies along ℓ. But B also belongs to both planes: it belongs to Σ because it is on AB, and to Π because it is on m. Consequently B lies on ℓ, produced if necessary. Thus the parallel lines ℓ and m meet at B, contrary to their definition. [D1.23]

**Step 4.** Therefore Σ is Π. Since AB lies in Σ, it lies in the same plane Π as both given parallel straight lines. The chosen points were arbitrary, so the required conclusion follows. [Steps 1–3]

**USED:** 11.2, 11.3, D1.23, P1
**Human refs (from References field):** 11.3
**Jaccard:** 0.250 — AI adds ['11.2', 'D1.23', 'P1']

## Proposition 11.8
**Statement:** If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

**Step 1.** Let the straight lines l and m be parallel, and let l be at right angles to a plane Π at O. The parallel lines lie in one plane Σ (D1.23). Since l is perpendicular to Π, Σ is different from Π (D11.3). Their common section is therefore a straight line s through O (11.3).

**Step 2.** The line m meets s. For otherwise, since both lie in Σ, m would be parallel to s (D1.23). Then l and s, being parallel to m in the same plane, would be parallel to one another (1.30), contrary to their meeting at O. Let B be the intersection of m and s. Since l and m do not meet, B is different from O (D1.23).

**Step 3.** Since s lies in Π and passes through O, l is at right angles to s (D11.3). The transversal s cuts the parallel lines l and m; hence the corresponding angle at B is also right, and m is at right angles to s (1.29).

**Step 4.** In Π draw BE at right angles to s at B, taking E different from B (1.11). Take A on l, different from O, and join OE, AE, and AB (P1). The line OE lies in Π (D1.7), and AB lies in Σ because its endpoints lie on the parallel lines l and m (11.7). Triangle AOE is also planar (11.2). Path choice: the right triangles now available allow 1.47 and its converse 1.48 to establish an auxiliary right angle, after which the two-line criterion 11.4 applies directly.

**Step 5.** The angles AOE and AOB are right because l is perpendicular to Π (D11.3), and OBE is right by construction. Thus, writing XY² for the square on XY, application of 1.47 to triangles AOE, OBE, and AOB gives respectively
AE² = AO² + OE²,
OE² = OB² + BE²,
and AB² = AO² + OB².

**Step 6.** Substituting the second equality into the first, and then using the third, gives
AE² = AO² + OB² + BE² = AB² + BE² (CN1, CN2).
Therefore the angle ABE is right, by the converse of the square-on-the-hypotenuse theorem (1.48).

**Step 7.** Consequently BE makes right angles with both BA and BO at their common point B. These are two distinct intersecting straight lines in Σ, so BE is at right angles to Σ (11.4). Since m lies in Σ and passes through B, BE is at right angles to m (D11.3).

**Step 8.** The line m therefore makes right angles with both BO, by Step 3, and BE, by Step 7. These two straight lines intersect at B and lie in Π. Hence m is at right angles to Π (11.4). Thus, if two straight lines are parallel and one is at right angles to a plane, the remaining one is also at right angles to that plane.

**USED:** 1.11, 1.29, 1.30, 1.47, 1.48, 11.2, 11.3, 11.4, 11.7, CN1, CN2, D1.23, D1.7, D11.3, P1
**Human refs (from References field):** 1.29, 11.2, 11.4, 11.7, D11.3
**Jaccard:** 0.333 — AI adds ['1.11', '1.30', '1.47', '1.48', '11.3', 'CN1', 'CN2', 'D1.23', 'D1.7', 'P1']

## Proposition 11.9
**Statement:** Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

**Step 1.** Let a and b each be parallel to c, with the three lines not all in one plane. By the definition of parallel lines, a and c lie in a plane α, and b and c lie in a plane β; these planes are distinct by hypothesis. [D1.23] Path choice: we shall make a and b perpendicular to a common plane, allowing their parallelism to follow without assuming their coplanarity.

**Step 2.** Since α and β both contain c, they intersect, and their common section is precisely the straight line c. [11.3]

**Step 3.** Choose a point O on c. In α draw a straight line p through O at right angles to c; in β draw a straight line q through O at right angles to c. [1.11] The lines p and q are distinct: otherwise their common line would belong to both α and β and hence would be c, whereas each was constructed perpendicular to c. [11.3, 1.11]

**Step 4.** The intersecting lines p and q lie in one plane, say Σ. [11.2] Since c makes right angles with both at their common point O, c is perpendicular to Σ. [11.4]

**Step 5.** Since a is parallel to c and c is perpendicular to Σ, a is perpendicular to Σ. Likewise, since b is parallel to c, b is perpendicular to Σ. [11.8]

**Step 6.** The straight lines a and b are therefore perpendicular to the same plane Σ, so they are parallel to one another, as required. [11.6]

**USED:** 1.11, 11.2, 11.3, 11.4, 11.6, 11.8, D1.23
**Human refs (from References field):** 11.4, 11.6, 11.8
**Jaccard:** 0.429 — AI adds ['1.11', '11.2', '11.3', 'D1.23']

## Proposition 11.10
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.

**Step 1.** Let the first two straight lines meet at A and the second two at D. Join AD [P1]. Each pair of corresponding parallel lines lies in a plane [D1.23], and AD lies in each of these planes [11.7]. Label corresponding rays AB, AC and DE, DF, with AB parallel to DE and AC parallel to DF: choose B and E on the same side of AD in the first parallel-pair plane, and C and F on the same side of AD in the second. The corresponding angles to be compared are ∠BAC and ∠EDF.

**Step 2.** Choose the endpoints on these rays so that AB = DE and AC = DF, cutting down the longer of each pair of initially chosen segments when necessary [1.3]. Join BE, CF, BC and EF [P1].

**Step 3.** The joins AD and BE lie in the plane of AB and DE, and the joins AD and CF lie in the plane of AC and DF [11.7]. Since AB and DE are equal and parallel, and AD and BE join their corresponding ends in the same direction, AD and BE are equal and parallel [1.33]. Likewise, since AC and DF are equal and parallel, AD and CF are equal and parallel [1.33]. Consequently BE = CF, since each equals AD [CN1].

**Step 4.** The three straight lines AD, BE and CF cannot all lie in one plane. Such a plane would contain all six endpoints and therefore the original four straight lines, contrary to the hypothesis [D1.7, 11.1]. Since BE and CF are both parallel to AD and are not all coplanar with it, BE is parallel to CF [11.9].

**Step 5.** The equal parallel segments BE and CF have the same corresponding direction: in the two applications of 1.33 in Step 3, B and C correspond to A, while E and F correspond to D. Thus BC and EF join their corresponding ends in the same direction. These joins lie in the plane of BE and CF [11.7]. Applying the equal-and-parallel joining theorem once more gives BC = EF [1.33].

**Step 6.** In triangles ABC and DEF, we have AB = DE and AC = DF by Step 2, and BC = EF by Step 5. The direct path is therefore the three-side criterion: all three corresponding side equalities are already established. By 1.8, the angles contained by AB, AC and by DE, DF are equal; that is, ∠BAC = ∠EDF. Hence the given pairs of meeting parallel straight lines contain equal corresponding angles.

**USED:** 1.3, 1.33, 1.8, 11.1, 11.7, 11.9, CN1, D1.23, D1.7, P1
**Human refs (from References field):** 1.33, 1.8, 11.9
**Jaccard:** 0.300 — AI adds ['1.3', '11.1', '11.7', 'CN1', 'D1.23', 'D1.7', 'P1']

## Proposition 11.11
**Statement:** From a given elevated point to draw a straight line perpendicular to a given plane.

**Step 1.** Let A be the given point outside the given plane Π. Draw a straight line ℓ in Π, producing it as necessary. Join A to two distinct points of ℓ. The resulting triangle lies in a plane, which therefore contains A and ℓ; the produced line remains in that plane. [P1, P2, 11.2, 11.1]

**Step 2.** In the plane containing A and ℓ, draw AB perpendicular to ℓ, with B on ℓ. In Π, draw the straight line m through B perpendicular to ℓ. Thus AB and m are both perpendicular to ℓ at B. [1.12, 1.11]

**Step 3.** If AB is also perpendicular to m, then AB is perpendicular to the two intersecting lines ℓ and m in Π, and consequently AB is perpendicular to Π. This completes the construction in this case. For the remaining case, suppose AB is not perpendicular to m. [11.4]

**Step 4.** The intersecting lines AB and m lie in a plane Σ. Since ℓ is perpendicular to both at their intersection B, ℓ is perpendicular to Σ. Within Σ, draw AH perpendicular to m, with H on m. Here H differs from B, since otherwise AB would be perpendicular to m, contrary to the remaining case. [11.2, 11.4, 1.12]

**Step 5.** Through H draw, in Π, a straight line n parallel to ℓ. Since ℓ is perpendicular to Σ, n is also perpendicular to Σ. Hence n is perpendicular to AH, which lies in Σ and meets n at H. The direct path here is to use 11.8: it transfers the perpendicularity already established for ℓ to its parallel n. [1.31, 11.8, D11.3]

**Step 6.** The lines m and n are distinct: m meets ℓ at B, whereas n, being parallel to ℓ, does not meet ℓ. Both lie in Π and meet at H. Since AH is perpendicular to m by construction and to n by Step 5, AH is perpendicular to Π. Thus, in either case, a straight line perpendicular to the given plane has been drawn from the given elevated point A. [D1.23, 11.4]

**USED:** 1.11, 1.12, 1.31, 11.1, 11.2, 11.4, 11.8, D1.23, D11.3, P1, P2
**Human refs (from References field):** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3
**Jaccard:** 0.545 — AI adds ['11.1', '11.2', 'D1.23', 'P1', 'P2']

## Proposition 11.12
**Statement:** To set up a straight line at right angles to a given plane from a given point in it.

**Step 1.** Let Π be the given plane and A the given point in it. Choose a point B outside Π. By 11.11, draw BC perpendicular to Π, meeting Π at C.

**Step 2.** If A lies on BC, then BC is already the required perpendicular through A, by its construction in Step 1 (11.11). Otherwise, join AB (P1). Since AB and BC intersect at B, they lie in one plane Σ, which therefore contains A and BC (11.2).

**Step 3.** In the plane Σ, draw through A a straight line AD parallel to BC (1.31).

**Step 4.** Since BC is perpendicular to Π and AD is parallel to BC, AD is also perpendicular to Π (11.8). This is the direct criterion naturally supplied by the parallel construction; no separate verification against intersecting lines in Π is needed. Thus AD is the required straight line set up at right angles to the given plane from its given point A.

**USED:** 1.31, 11.11, 11.2, 11.8, P1
**Human refs (from References field):** 1.31, 11.11, 11.8
**Jaccard:** 0.600 — AI adds ['11.2', 'P1']

## Proposition 11.13
**Statement:** From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

**Step 1.** Suppose, for a contradiction, that from a point A of a plane Π two distinct rays AB and AC are set up perpendicular to Π on the same side. Their supporting straight lines are distinct: otherwise the rays from A on that same side would coincide. (Contrary hypothesis.)

**Step 2.** Since these two straight lines are perpendicular to the same plane Π, they are parallel by **11.6**. This is the direct path: 11.6 applies immediately to the assumed perpendicularities, without an auxiliary construction.

**Step 3.** By **D1.23**, parallel straight lines do not meet in either direction. But the two lines both pass through A, a contradiction. Therefore, from the same point two distinct straight lines cannot be set up at right angles to the same plane on the same side.

**USED:** 11.6, D1.23
**Human refs (from References field):** 11.3, D11.3
**Jaccard:** 0.000 — AI adds ['11.6', 'D1.23']; Human adds ['11.3', 'D11.3']

## Proposition 11.14
**Statement:** Planes to which the same straight line is at right angles will be parallel.

**Step 1.** Let α and β be distinct planes, and let the same straight line ℓ be at right angles to α at A and to β at B. Thus ℓ makes right angles with every straight line in either plane through its respective foot [D11.3].

**Step 2.** The feet A and B are distinct. Otherwise, at their common point O choose two distinct straight lines r and s in α and a straight line t in β not contained in α. Since ℓ is at right angles to all three, they lie in one plane γ [D11.3, 11.5]. Necessarily γ = α: otherwise the common section of γ and α would contain both r and s, whereas the common section of two distinct intersecting planes is a single straight line [11.3]. This would put t in α, a contradiction.

**Step 3.** Suppose, for contradiction, that α and β meet, and take a point C common to them. A straight line through two points of a plane lies wholly in that plane [D1.7, 11.1]. Consequently C cannot lie on ℓ: since A ≠ B, this would put ℓ wholly in at least one of the planes, contrary to its being perpendicular to that plane [D11.3].

**Step 4.** Join AC and BC [P1]. These straight lines lie in α and β respectively [D1.7, 11.1]. Since C is not on AB, the three points form a triangle, which lies in one plane [11.2]. As AB lies on ℓ, both ∠CAB and ∠CBA are right angles [D11.3].

**Step 5.** Use the direct two-angle bound, since no information about the third angle is needed: in any triangle, any two angles together are less than two right angles [1.17]. Applied to triangle ABC, this contradicts the fact that ∠CAB and ∠CBA are themselves two right angles.

**Step 6.** Therefore α and β do not meet. Planes which do not meet are parallel; hence planes to which the same straight line is at right angles are parallel [D11.8].

**USED:** 1.17, 11.1, 11.2, 11.3, 11.5, D1.7, D11.3, D11.8, P1
**Human refs (from References field):** 1.17, 11.3, D11.3, D11.8
**Jaccard:** 0.444 — AI adds ['11.1', '11.2', '11.5', 'D1.7', 'P1']

## Proposition 11.15
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

**Step 1.** Let the straight lines a and b meet at A, and let c and d meet at B, with a parallel to c and b parallel to d. Let α and β be the planes through the respective pairs (11.2). By hypothesis, α and β are distinct.

**Step 2.** The point B is outside α. For suppose B belonged to α. Since a and c are parallel, they lie in a plane γ, and B, being on c, is not on a (D1.23). Thus α and γ would contain both a and the point B outside a. By 11.3, distinct planes cannot have such a common section; hence γ = α, so c lies in α. The same argument with b and d shows that d lies in α. Then α and β contain the two intersecting lines c and d, and 11.3 again forces α = β, contrary to the hypothesis.

**Step 3.** From B draw BH perpendicular to α, with H in α (11.11). We use the common-perpendicular route: once BH is also perpendicular to β, 11.14 gives the required conclusion directly.

**Step 4.** If H is not on a, draw through H in α a straight line r parallel to a; if H is on a, take r to be a itself. Likewise, draw through H in α a straight line s parallel to b, taking s to be b itself when H lies on b (1.31).

**Step 5.** We have r parallel to c and s parallel to d. Indeed, if r = a, the first assertion is given. Otherwise r and c are both parallel to a: apply 1.30 when these three lines are coplanar, and 11.9 when they are not. Thus the earlier planar result is used wherever it applies, and the spatial result only where needed. The identical argument with s, b, and d proves the second assertion.

**Step 6.** Since BH is perpendicular to α, it makes right angles with r and s at H (D11.3). Moreover, BH lies in the plane of the parallel lines r and c, because it joins H on r to B on c; likewise it lies in the plane of s and d (11.7). Applying 1.29 in each of these planes, with BH as transversal, shows that the angles BH makes with c and d at B are right. Hence BH is perpendicular to both c and d (D1.10).

**Step 7.** Since c and d meet at B, their common perpendicular BH is perpendicular to their plane β (11.4). Thus the same straight line BH is perpendicular to both α and β. Therefore α and β are parallel (11.14), as required.

**USED:** 1.29, 1.30, 1.31, 11.11, 11.14, 11.2, 11.3, 11.4, 11.7, 11.9, D1.10, D1.23, D11.3
**Human refs (from References field):** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Jaccard:** 0.538 — AI adds ['1.30', '11.2', '11.3', '11.7', 'D1.10', 'D1.23']

## Proposition 11.16
**Statement:** If two parallel planes be cut by any plane, their common sections are parallel.

**Step 1.** Let the parallel planes Π and Σ be cut by a plane Ω, and let their common sections with Ω be a and b respectively. By 11.3, a and b are straight lines. Both lie in Ω, since they are sections of that plane. [11.3]

**Step 2.** Produce a and b indefinitely in both directions. Their productions remain in Π and Σ respectively, and both remain in Ω, because a straight line cannot lie partly in a plane and partly outside it. [P2, 11.1]

**Step 3.** If a and b met in either direction at a point X, then X would belong to both Π and Σ, by Step 2. Thus Π and Σ would meet. But parallel planes do not meet, so this contradicts the hypothesis that Π and Σ are parallel. Therefore a and b do not meet in either direction, however far produced. [D11.8]

**Step 4.** The straight lines a and b lie in the same plane Ω and, when produced indefinitely in both directions, do not meet. Hence they are parallel by D1.23. This definition gives the direct route to the conclusion, since coplanarity and nonintersection have both been established. Therefore the common sections of two parallel planes with any cutting plane are parallel. [D1.23]

**USED:** 11.1, 11.3, D1.23, D11.8, P2
**Human refs (from References field):** 11.1, D1.23
**Jaccard:** 0.400 — AI adds ['11.3', 'D11.8', 'P2']

## Proposition 11.17
**Statement:** If two straight lines be cut by parallel planes, they will be cut in the same ratios.

**Step 1.** Let three parallel planes Π₁, Π₂, Π₃ cut the two distinct straight lines at A, B, C and D, E, F, respectively, with Π₂ the middle plane and the points on each line in the indicated order. The planes do not meet one another (D11.8). We must prove AB:BC = DE:EF. Our route is to obtain parallel lines in triangular sections and apply the direct proportional-cutting theorem 6.2.

**Step 2.** First suppose A ≠ D and C ≠ F. Join AF, AD, and CF (P1), and let AF meet the middle plane Π₂ at G. The triangles ACF and FAD each lie in a plane (11.2). Moreover, AD lies in Π₁ and CF lies in Π₃, since their endpoints lie in those respective planes (11.1).

**Step 3.** In the plane of triangle ACF, the common sections with Π₂ and Π₃ are the straight lines BG and CF (11.3). Since Π₂ and Π₃ are parallel, BG is parallel to CF (11.16). Likewise, in the plane of triangle FAD, the common sections with Π₂ and Π₁ are GE and AD (11.3); hence GE is parallel to AD (11.16).

**Step 4.** In triangle ACF, the parallel BG cuts the sides AC and AF proportionally, so AB:BC = AG:GF (6.2). In triangle FAD, the parallel GE cuts the sides FA and FD proportionally; taking corresponding segments in the same order gives AG:GF = DE:EF (6.2).

**Step 5.** Ratios equal to the same ratio are equal to one another. Therefore AB:BC = DE:EF (5.11).

**Step 6.** If an outer intersection is shared, only one triangular section is needed. If A = D, form triangle ACF; if C = F, form triangle CAD (P1; 11.2). In the first case BE and CF, and in the second case BE and AD, are the straight common sections of the triangle's plane with two of the parallel planes (11.1; 11.3). They are therefore parallel (11.16). Applying 6.2 in the respective triangle gives AB:BC = DE:EF directly. Thus the result holds also in these cases. Since the three parallel planes were arbitrary, the two straight lines are cut in the same ratios, as required.

**USED:** 11.1, 11.16, 11.2, 11.3, 5.11, 6.2, D11.8, P1
**Human refs (from References field):** 11.16, 5.11, 6.2
**Jaccard:** 0.375 — AI adds ['11.1', '11.2', '11.3', 'D11.8', 'P1']

## Proposition 11.18
**Statement:** If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

**Step 1.** Let AB be perpendicular to a plane α at B, and let β be any plane containing AB. The common section of α and β is a straight line d through B (11.3).

**Step 2.** Since d lies in α and meets AB at B, AB is perpendicular to d (D11.3). We take the direct route through D11.4: we shall show that every straight line in β perpendicular to d is perpendicular to α.

**Step 3.** Let m be any straight line in β perpendicular to d, meeting d at C. If C = B, then m coincides with AB. Indeed, their rays on the same side of d make right angles with a fixed ray of d (D1.10). If those rays were distinct, one of these right angles would be a proper part of the other, contradicting the equality of all right angles and the principle that the whole is greater than the part (P4, CN5). Thus, in this case, m is perpendicular to α by the hypothesis on AB.

**Step 4.** Suppose instead that C differs from B. The lines AB and m lie in β, and d cuts them at B and C. Their interior angles on the same side of d are both right angles (D1.10). Hence AB and m are parallel (1.28). We use this criterion because the two same-side interior angles are immediately known to sum to two right angles.

**Step 5.** Since m is parallel to AB, and AB is perpendicular to α, m is also perpendicular to α (11.8).

**Step 6.** Therefore every straight line drawn in β at right angles to the common section d is perpendicular to α. By D11.4, β is perpendicular to α. Since β was any plane through AB, every plane through AB is perpendicular to α, as required.

**USED:** 1.28, 11.3, 11.8, CN5, D1.10, D11.3, D11.4, P4
**Human refs (from References field):** 1.11, 1.28, 11.8, D11.3, D11.4
**Jaccard:** 0.444 — AI adds ['11.3', 'CN5', 'D1.10', 'P4']; Human adds ['1.11']

## Proposition 11.19
**Statement:** If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

**Step 1.** Let the intersecting planes α and β each be at right angles to the plane Π. Denote their common section by s, and their respective sections with Π by a and b. These common sections are straight lines. [11.3]

**Step 2.** Choose any point A on s. Within α construct a straight line p through A perpendicular to a, and within β construct a straight line q through A perpendicular to b. If A lies in Π, then A lies on both a and b, so erect these perpendiculars at A. [1.11] If A does not lie in Π, then A lies outside both traces, so drop the perpendiculars from A to them in the respective planes. [1.12] This construction avoids assuming beforehand that s meets Π.

**Step 3.** Since α is at right angles to Π, the line p, drawn in α perpendicular to their common section a, is perpendicular to Π. Likewise, since β is at right angles to Π, q is perpendicular to Π. [D11.4]

**Step 4.** Use the parallelism of perpendiculars to a plane, since it applies whether A lies in Π or outside it. If p and q were distinct, they would be parallel, both being perpendicular to Π. [11.6] But they both pass through A, whereas parallel straight lines do not meet. [D1.23] Therefore p and q coincide.

**Step 5.** This coincident straight line lies in both α and β, and therefore is their common section s. [11.3] By Step 3 it is perpendicular to Π. Hence the common section of the two given planes is at right angles to the same plane, as required.

**USED:** 1.11, 1.12, 11.3, 11.6, D1.23, D11.4
**Human refs (from References field):** 11.13, D11.4
**Jaccard:** 0.143 — AI adds ['1.11', '1.12', '11.3', '11.6', 'D1.23']; Human adds ['11.13']

## Proposition 11.20
**Statement:** If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

**Step 1.** Let O be the vertex, and denote the three edge rays by OA, OB, OC, with points on these rays to be chosen below. These rays are not coplanar (D11.11). Write α = ∠AOB, β = ∠AOC, and γ = ∠BOC, relabelling so that α is greatest. The inequalities α + β > γ and α + γ > β follow immediately because each sum exceeds its summand α (CN5). It remains to prove β + γ > α.

**Step 2.** If α = β, then β + γ > α by CN5. Suppose therefore that α > β. In the plane of OA and OB, construct a ray OD strictly inside ∠AOB such that ∠AOD = β (1.23). This is the chosen route: splitting the greatest face angle will reduce the required inequality to a comparison of two triangles.

**Step 3.** Choose A and B on their respective edge rays and join AB; let the interior ray OD meet AB at D, so that D lies between A and B (P1). Choose C on the third edge ray so that OC = OD, producing that edge if necessary (P2, 1.3). Join AC and BC (P1). Since the three edge rays are noncoplanar, C is not on AB, so ABC is a genuine triangle (D11.11). Every triangle used below lies in a plane (11.2).

**Step 4.** In triangles AOD and AOC, AO is common, OD = OC, and ∠AOD = ∠AOC by construction. Hence their bases are equal: AD = AC (1.4).

**Step 5.** In triangle ABC, the two sides AC and CB together exceed AB:
AC + CB > AB (1.20).

**Step 6.** Since D lies between A and B, AB = AD + DB. Substituting AD = AC into Step 5 and removing the equal common parts gives CB > DB (CN3, CN5).

**Step 7.** Compare triangles COB and DOB. They have CO = DO and OB common, while their bases satisfy CB > DB. Therefore ∠COB > ∠DOB (1.25). This proposition applies directly because equality of the corresponding pairs of sides and inequality of the bases have already been established.

**Step 8.** Add ∠AOC = ∠AOD to the inequality in Step 7. Since OD lies inside ∠AOB, this gives
∠AOC + ∠COB > ∠AOD + ∠DOB = ∠AOB
(CN2, CN5). Thus β + γ > α. Together with the other two inequalities established in Step 1, this proves that any two of the three plane angles, taken together, are greater than the remaining one.

**USED:** 1.20, 1.23, 1.25, 1.3, 1.4, 11.2, CN2, CN3, CN5, D11.11, P1, P2
**Human refs (from References field):** 1.20, 1.25, 1.4
**Jaccard:** 0.250 — AI adds ['1.23', '1.3', '11.2', 'CN2', 'CN3', 'CN5', 'D11.11', 'P1', 'P2']

## Proposition 11.21
**Statement:** Any solid angle is contained by plane angles less than four right angles.

**Step 1.** Use a plane section, so that all numbers of containing angles are treated together. Let O be the vertex of the given solid angle, understood in the usual Euclidean convex sense. Cut its bounding edges by a plane not through O, obtaining a convex polygon A₁A₂…Aₙ, with n ≥ 3. The sections of consecutive faces are its straight sides. Indices below are cyclic: A₀ = Aₙ and Aₙ₊₁ = A₁. The angles whose sum is required are αᵢ = ∠AᵢOAᵢ₊₁. [D11.11, 11.3]

**Step 2.** At each vertex Aᵢ of the section, put φᵢ = ∠Aᵢ₋₁AᵢAᵢ₊₁ and θᵢ = ∠Aᵢ₋₁AᵢO + ∠OAᵢAᵢ₊₁. Since O is outside the section plane, the three rays AᵢAᵢ₋₁, AᵢO, and AᵢAᵢ₊₁ form a solid angle contained by three plane angles. Therefore θᵢ > φᵢ. This is the natural application of 11.20: the two angles belonging to the lateral triangles together exceed the angle of the section. [11.2, 11.20]

**Step 3.** Let B be the sum of all θᵢ and C the sum of all φᵢ. Write θᵢ = φᵢ + εᵢ, where each εᵢ is a positive angular excess. Adding these equalities gives B = C + E, where E is the sum of the positive excesses and is itself positive. [CN2, CN5]

**Step 4.** Let R denote the common magnitude of a right angle. Draw the diagonals from A₁ to A₃, …, Aₙ₋₁. These divide the convex section into n − 2 triangles. Their angles together constitute exactly the interior angles of the polygon. Since each triangle has its three angles equal to two right angles, C = 2(n − 2)R. Consequently B = 2(n − 2)R + E. [P4, P1, 1.32, CN2]

**Step 5.** Each of the n lateral triangles OAᵢAᵢ₊₁ is planar and has angle sum 2R. On adding their angle sums, their angles at O contribute A = α₁ + ⋯ + αₙ. Their remaining angles contribute exactly B, because at each Aᵢ the two adjacent lateral triangles contribute θᵢ. Hence A + B = 2nR. [11.2, 1.32, CN2]

**Step 6.** Substitute the expression for B to obtain A + 2(n − 2)R + E = 2nR. Subtracting 2(n − 2)R from both sides gives A + E = 4R. Since E is positive, A is less than 4R. Thus the plane angles containing the given solid angle are together less than four right angles. [CN3, CN5, D11.11]

**USED:** 1.32, 11.2, 11.20, 11.3, CN2, CN3, CN5, D11.11, P1, P4
**Human refs (from References field):** 1.32, 11.20
**Jaccard:** 0.200 — AI adds ['11.2', '11.3', 'CN2', 'CN3', 'CN5', 'D11.11', 'P1', 'P4']

## Proposition 11.22
**Statement:** If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

**Step 1.** Denote the three given angles, in increasing order, by α ≤ β ≤ γ. Let the common length of their six containing straight lines be r, and join their respective extremities; denote the resulting straight lines by a, b, c, opposite α, β, γ respectively (P1). By hypothesis, α + β > γ. **Path choice:** establish the triangle inequalities for a, b, c and then apply 1.22; no construction of a solid angle is needed.

**Step 2.** Since the two sides containing each angle equal r, comparison of the included angles gives a ≤ b ≤ c: a strict angle inequality gives the corresponding strict base inequality by 1.24, while equal angles give equal bases by 1.4. We use 1.24 because the known angle comparison directly supplies the required side comparison.

**Step 3.** If α = γ, all three angles are equal, and consequently a = b = c by 1.4. Hence a + b > c, since the whole exceeds either part (CN5). It remains to establish this same inequality when α < γ.

**Step 4.** In that case, name the vertex and extremities of the given angle γ as O, A, B, so that ∠AOB = γ, OA = OB = r, and AB = c. Describe the circle with centre O and radius r (P3). Within ∠AOB construct a ray making an angle α with OA, and let C be its intersection with the circle (1.23). Then OC = OA = OB by D1.15. Since 0 < α < γ, the points A, C, B are distinct. Join AC and BC (P1). These three points are noncollinear: otherwise one would lie between the other two, whereas the straight line joining two points of a circle lies within the circle (3.2). Thus ACB is a triangle.

**Step 5.** Since ∠AOC = α and OA = OC = r, comparison with the original triangle having vertex angle α gives AC = a (1.4). Put δ = ∠COB. The construction gives γ = α + δ. Consequently δ < β, since otherwise adding α would contradict the hypothesis α + β > γ (CN2, CN5). Comparing the triangle COB with the original triangle having vertex angle β, their two containing sides are respectively equal, but δ < β; therefore CB < b (1.24).

**Step 6.** In triangle ACB, the two sides AC and CB together exceed AB (1.20). Since AC = a, CB < b, and AB = c, it follows that
 a + b > AC + CB > AB = c
(CN2, CN5). Thus a + b > c in both cases considered.

**Step 7.** From c ≥ b and c ≥ a, already established in Step 2, we also have a + c > b and b + c > a, since each sum exceeds its positive summand c (CN5). Therefore any two of a, b, c together exceed the remaining one. By 1.22, a triangle can be constructed with sides equal to a, b, c. These are precisely the straight lines joining the extremities of the equal straight lines containing the three given angles. Hence the required triangle can be constructed.

**USED:** 1.20, 1.22, 1.23, 1.24, 1.4, 3.2, CN2, CN5, D1.15, P1, P3
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 0.182 — AI adds ['1.20', '1.22', '1.23', '3.2', 'CN2', 'CN5', 'D1.15', 'P1', 'P3']

## Proposition 11.23
**Statement:** To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

**Step 1.** Let the given plane angles be α, β, γ, and write R for a right angle. Thus each given angle is positive and less than 2R. Suppose that α + β > γ, β + γ > α, γ + α > β, and that α + β + γ < 4R. The last restriction is necessary by 11.21. Path choice: retain α in a fixed plane and construct the third edge by a perpendicular lift, obtaining the lifting height directly from intersecting chords.

**Step 2.** In a plane Π describe a circle Ω with centre O and radius r, and choose A on it. Construct B on Ω so that ∠AOB = α. Fix a positive direction around the circle. Construct C₊ and C₋ on Ω by copying β from OA in the positive and negative directions respectively. Likewise construct E₊ and E₋ by copying γ from OB in the positive and negative directions respectively. These constructions use P3, 1.23 and P2. All the segments from O to these circumference points equal r by D1.15.

**Step 3.** A complete turn is 4R by 1.13. Measured positively from OC₋, the angular positions of E₋, C₊ and E₊ are respectively α + β − γ, 2β and α + β + γ. The hypotheses give
0 < α + β − γ < 2β < α + β + γ < 4R.
Consequently the cyclic order is C₋, E₋, C₊, E₊. Join C₋C₊ and E₋E₊ by P1. Their endpoints alternate, so the endpoints of either chord lie on opposite sides of the other chord. The chords therefore meet at a point D strictly interior to both; their segments lie within Ω by 3.2.

**Step 4.** The triangles AOC₊ and AOC₋ have OA common, OC₊ = OC₋, and equal included angles β. Hence AC₊ = AC₋ by 1.4. Similarly, BE₊ = BE₋ by 1.4. Describe a circle ΩA with centre A and radius AC₊, and a circle ΩB with centre B and radius BE₊ (P3). Thus C₋C₊ is a chord of both Ω and ΩA, while E₋E₊ is a chord of both Ω and ΩB. Since D is internal to these chords, it lies inside all three circles by 3.2.

**Step 5.** Write products of lengths for their contained rectangles, and squared lengths for the squares on them. Set k = DC₊·DC₋. Applying 3.35 to the intersecting chords in Ω gives
k = DC₊·DC₋ = DE₊·DE₋.
All four chord portions are positive, since D is strictly interior to both chords.

**Step 6.** Draw the diameters through D in the three circles, using P1 and P2. For a circle with centre X and radius ρ, let UV be its diameter through D. Since X bisects UV and D lies between U and V, 2.5 gives
DU·DV + XD² = ρ².
By 3.35, DU·DV equals the product of the portions of any other chord through D. If that chord is itself UV, the equality of products is immediate. Applying this argument to Ω, ΩA and ΩB, and using Step 5, gives
r² = OD² + k,
AC₊² = AD² + k,
BE₊² = BD² + k.
If D = O, use any diameter of Ω: 3.35 gives k = r² directly, so the first equality still holds with OD² = 0.

**Step 7.** Construct a mean proportional h between DC₊ and DC₋ by 6.13. Then h² = DC₊·DC₋ = k by 6.17, and h is positive. Set up a perpendicular to Π at D by 11.12, and on it take P with DP = h, producing the line and cutting off the required length by P2 and 1.3. Since DP is positive, P is outside Π. Join P to O, A and B by P1.

**Step 8.** The triangles ODP, ADP and BDP lie in planes by 11.2 and, when nondegenerate, are right-angled at D by D11.3. Therefore 1.47, together with the equalities in Steps 6 and 7, gives
OP² = OD² + DP² = OD² + k = r²,
AP² = AD² + DP² = AD² + k = AC₊²,
BP² = BD² + DP² = BD² + k = BE₊²
(CN1, CN2). If D = O, the first equality follows instead immediately from OP = DP = h and h² = r². Hence OP = r, AP = AC₊ and BP = BE₊. Here equal squares have equal sides, since 2.4 and CN5 imply that a strictly greater side has a strictly greater square.

**Step 9.** The side equalities now make 1.8 the direct applicable congruence proposition. In triangles AOP and AOC₊, OA is common, OP = OC₊ = r, and AP = AC₊. Thus ∠AOP = ∠AOC₊ = β by 1.8. Likewise, triangles BOP and BOE₊ have their three sides respectively equal, so ∠BOP = ∠BOE₊ = γ by 1.8. The remaining angle ∠AOB is α by construction.

**Step 10.** The rays OA and OB are distinct and noncollinear, and P is outside their plane Π. Thus OA, OB and OP cannot lie in one plane: otherwise that plane and Π would have two intersecting straight lines in common, contrary to 11.3. By D11.11, the three rays therefore constitute a solid angle, whose three plane angles are precisely α, β and γ by Step 9. The required solid angle has been constructed.

**USED:** 1.13, 1.23, 1.3, 1.4, 1.47, 1.8, 11.12, 11.2, 11.21, 11.3, 2.4, 2.5, 3.2, 3.35, 6.13, 6.17, CN1, CN2, CN5, D1.15, D11.11, D11.3, P1, P2, P3
**Human refs (from References field):** 1.25, 1.29, 1.4, 1.47, 1.8, 11.12, 11.22, 5.16, 6.2, 6.4
**Jaccard:** 0.129 — AI adds ['1.13', '1.23', '1.3', '11.2', '11.21', '11.3', '2.4', '2.5', '3.2', '3.35', '6.13', '6.17', 'CN1', 'CN2', 'CN5', 'D1.15', 'D11.11', 'D11.3', 'P1', 'P2', 'P3']; Human adds ['1.25', '1.29', '11.22', '5.16', '6.2', '6.4']

## Proposition 11.24
**Statement:** If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

**Step 1.** Label the solid so that its opposite face-pairs are ABCD and EFGH, ABFE and DCGH, and BCGF and ADHE; the planes of each pair are parallel by hypothesis. The edges are straight lines, being common sections of the bounding planes [11.3]. We shall prove equality for the opposite pair ABCD, EFGH, chosen arbitrarily.

**Step 2.** Use the theorem on sections of parallel planes, since it directly determines the directions of the edges. The plane ABCD cuts the parallel planes ABFE and DCGH in AB and DC, so AB is parallel to DC. It cuts the parallel planes ADHE and BCGF in AD and BC, so AD is parallel to BC [11.16]. Thus ABCD is a parallelogram. Likewise, the plane of every other face cuts the other two pairs of parallel bounding planes in its opposite sides; these sides are therefore parallel [11.16]. Consequently all six faces are parallelogrammic.

**Step 3.** In the parallelogram ABFE, opposite sides AB and EF are equal. In the parallelogram ADHE, opposite sides AD and EH are equal [1.34]. Thus AB = EF and AD = EH.

**Step 4.** Also AB is parallel to EF, and AD is parallel to EH, by Step 2. These corresponding sides, taken from A and E respectively, contain equal angles: ∠BAD = ∠FEH [11.10]. This is the applicable angle theorem because the two pairs of intersecting lines lie in different planes.

**Step 5.** Join BD and FH [P1]. The triangles BAD and FEH have two sides respectively equal and their included angles equal, by Steps 3–4. Therefore these triangles are equal [1.4]. Side-angle-side is the direct choice, since precisely its hypotheses have already been established.

**Step 6.** The diagonal BD bisects the parallelogram ABCD, so triangle BAD equals triangle BCD. Likewise FH bisects EFGH, so triangle FEH equals triangle FGH [1.34]. Together with Step 5, these equalities give triangle BCD equal to triangle FGH [CN1]. Adding the equal triangles in corresponding pairs, the whole parallelogram ABCD equals the whole parallelogram EFGH [CN2].

**Step 7.** The opposite pair chosen in Step 1 was arbitrary, so Steps 3–6 establish equality for each opposite pair. Step 2 establishes that every face is parallelogrammic. Therefore the opposite planes of the solid are equal and parallelogrammic.

**USED:** 1.34, 1.4, 11.10, 11.16, 11.3, CN1, CN2, P1
**Human refs (from References field):** 1.34, 1.4, 11.10, 11.16
**Jaccard:** 0.500 — AI adds ['11.3', 'CN1', 'CN2', 'P1']

## Proposition 11.25
**Statement:** If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.

**Step 1.** Let the opposite end faces of the parallelepiped be ABCD and A′B′C′D′, with joining edges AA′, BB′, CC′, DD′. Let the cutting plane, parallel to these end faces, meet those edges at E, F, G, H respectively. Denote the two resulting solids by S₁ and S₂. Taking ABB′A′ as the base of the original solid, denote its two parts ABFE and EFB′A′ by b₁ and b₂. The intersections with the cutting plane are parallel to the corresponding end-face edges, and each resulting solid has parallelogrammic faces. [11.16, 11.24]

**Step 2.** We use the equimultiple criterion directly: the same construction will realize multiples of each base and its solid together. [D5.5] Produce the four joining edges indefinitely in the direction from ABCD towards A′B′C′D′. Through any point P other than A on the ray AA′, draw, in the two lateral planes through AA′, lines parallel respectively to AB and AD. These intersecting lines determine a plane parallel to ABCD. Use ABCD itself as the section at A. The defining lines of any two such sections are parallel in their respective lateral planes, so their section planes are also parallel to one another. Their intersections with the four fixed lateral planes therefore bound parallelogrammic sections and parallelepipedal slabs. [P2, 1.31, 11.2, 11.15, 1.30, 11.16, 11.24]

**Step 3.** Two slabs in this extension whose intercepts on AA′ are equal have equal chosen bases and are equal solids. To see this, apply the equality of opposite sides of a parallelogram to the lateral faces: every section has corresponding side lengths equal to those of ABCD, and the four joining edges of any slab equal its intercept on AA′. Corresponding lateral-face angles are equal by the properties of parallel lines, and corresponding section-face angles are equal because their sides are respectively parallel. Thus, for slabs with equal intercepts, corresponding faces have equal adjacent sides and equal included angles. Applying side-angle-side to the triangles constituting these parallelograms shows that corresponding faces are congruent, hence equal and similar. Their chosen bases are consequently equal, and the solids are equal and similar because their six corresponding faces are equal and similar. [1.34, 1.29, 11.10, 1.4, CN4, D6.1, D11.10]

**Step 4.** Let m and n be arbitrary positive integers. Starting at A on the ray AA′, mark m successive intervals each equal to AE, ending at M. Independently, starting at the same A, mark n successive intervals each equal to EA′, ending at N. These intervals can be laid off by repeatedly cutting the required length from a sufficiently produced straight line. Draw the sections of Step 2 through all the marked points. [P2, 1.3; Step 2]

**Step 5.** Every slab in the first partition equals S₁, and its chosen base equals b₁, by Step 3. Therefore the entire slab from A to M is mS₁, and its base is mb₁. Likewise, the entire slab from A to N is nS₂, and its base is nb₂. These equalities follow by adding the equal constituent magnitudes; they are precisely multiples in the sense of the definition. [Step 3, CN2, D5.2]

**Step 6.** Compare M and N on their common ray. If M lies beyond N, the slab ending at N is a proper part of the slab ending at M, and its base is likewise a proper part of the other base. Hence mb₁ > nb₂ and mS₁ > nS₂. If M = N, both slabs and both bases coincide, so both comparisons are equalities. If N lies beyond M, the proper-part comparisons are reversed, giving mb₁ < nb₂ and mS₁ < nS₂. Thus the corresponding equimultiples always alike exceed, are alike equal to, or alike fall short of one another. [CN5, CN4]

**Step 7.** Since m and n were arbitrary, the definition of equality of ratios gives b₁ : b₂ = S₁ : S₂. Therefore, as the base is to the base, so is the solid to the solid. [D5.5]

**USED:** 1.29, 1.3, 1.30, 1.31, 1.34, 1.4, 11.10, 11.15, 11.16, 11.2, 11.24, CN2, CN4, CN5, D11.10, D5.2, D5.5, D6.1, P2
**Human refs (from References field):** 11.24, D5.5
**Jaccard:** 0.105 — AI adds ['1.29', '1.3', '1.30', '1.31', '1.34', '1.4', '11.10', '11.15', '11.16', '11.2', 'CN2', 'CN4', 'CN5', 'D11.10', 'D5.2', 'D6.1', 'P2']

## Proposition 11.26
**Statement:** On a given straight line, and at a given point on it, to construct a solid angle equal to a given solid angle.

**Step 1.** Let ℓ be the given straight line and A the given point on it. Let the given solid angle have vertex O and bounding rays OX₁, …, OXₙ. Choose points Xᵢ distinct from O on these rays, with O, X₁, X₂ non-collinear, and let π be their plane. Choose a ray of ℓ starting at A and a plane π′ through ℓ. Such planes are determined by intersecting straight lines. [D11.11, P1, 11.2] We shall copy the configuration in π and then reproduce its perpendicular offsets; this fixes the prescribed edge from the outset.

**Step 2.** For every Xᵢ outside π, draw XᵢHᵢ perpendicular to π, meeting it at Hᵢ. For every Xᵢ already in π, put Hᵢ = Xᵢ. In particular, H₁ = X₁ and H₂ = X₂. [11.11]

**Step 3.** On the chosen ray of ℓ mark B so that AB = OX₁. In π′ construct the ray AC so that ∠BAC = ∠X₁OX₂, and mark C so that AC = OX₂, producing the rays as necessary. Join BC and X₁X₂. [P2, 1.3, 1.23, P1] The triangles ABC and OX₁X₂ are congruent by the two sides and their included angle. [1.4] This is the direct congruence criterion here because precisely those data were copied. Fix a fitting of these triangles with O corresponding to A, X₁ to B, and X₂ to C; use this fitting to specify corresponding sides of their planes.

**Step 4.** Copy every foot Hᵢ into π′ as follows. If Hᵢ = O, put Hᵢ′ = A. If Hᵢ lies on the line OX₁, mark Hᵢ′ on the corresponding ray of the line AB with AHᵢ′ = OHᵢ. Otherwise construct ∠BAHᵢ′ = ∠X₁OHᵢ and mark AHᵢ′ = OHᵢ, choosing the side of AB according as Hᵢ lies on the same side of OX₁ as X₂ or on the opposite side. [P2, 1.3, 1.23] In this last case, triangles ABHᵢ′ and OX₁Hᵢ are congruent by two sides and their included angle. [1.4] Thus, under the fixed fitting of the base triangles, every Hᵢ coincides with Hᵢ′; the cases on the line or at the vertex follow directly from their construction. [CN4]

**Step 5.** For each Xᵢ outside π, erect at Hᵢ′ a perpendicular to π′, on the side corresponding to the side of π containing Xᵢ. On it mark Xᵢ′ so that Hᵢ′Xᵢ′ = HᵢXᵢ. [11.12, P2, 1.3] For each Xᵢ in π, put Xᵢ′ = Hᵢ′. Draw all the rays AXᵢ′. In particular, X₁′ = B and X₂′ = C. [P1, P2]

**Step 6.** Apply the original configuration by the fixed fitting of its base triangle. Each Hᵢ then coincides with Hᵢ′. Each perpendicular HᵢXᵢ becomes a perpendicular to π′ at Hᵢ′, since its right angles with the lines of the base plane are preserved under coincidence. [D11.3, CN4] It is on the same side of π′ as the constructed perpendicular Hᵢ′Xᵢ′. These perpendicular rays therefore coincide. [11.13] Their lengths are equal by construction, so their endpoints also coincide: otherwise one segment would be a proper part of the other and hence smaller. [CN5] Consequently every Xᵢ coincides with Xᵢ′, including those already in the base plane.

**Step 7.** Hence all the bounding rays and plane angles of the given solid angle coincide, in their corresponding arrangement, with those constructed at A. The two solid angles are therefore equal. [D11.11, CN4] At least one original ray lies outside π, and its copy lies outside π′, so the constructed angle is indeed solid. Its edge AB lies on the given straight line ℓ and its vertex is the prescribed point A. Thus the required solid angle has been constructed.

**USED:** 1.23, 1.3, 1.4, 11.11, 11.12, 11.13, 11.2, CN4, CN5, D11.11, D11.3, P1, P2
**Human refs (from References field):** 1.23, 1.4, 1.8, 11.11, 11.12, D11.3
**Jaccard:** 0.357 — AI adds ['1.3', '11.13', '11.2', 'CN4', 'CN5', 'D11.11', 'P1', 'P2']; Human adds ['1.8']

## Proposition 11.27
**Statement:** On a given straight line to describe a parallelepipedal solid similar and similarly situated to a given parallelepipedal solid.

**Step 1.** Let AB be the given straight line, and let OU, OV, OW be the three edges issuing from a vertex O of the given parallelepiped S. At A, on AB, construct a solid angle equal to the solid angle at O, with AB corresponding to OU and the other two edge-rays corresponding, in order, to OV and OW [11.26]. Denote these rays by AC and AD, leaving the distances AC and AD to be fixed below. Thus ∠BAC = ∠UOV, ∠CAD = ∠VOW, and ∠DAB = ∠WOU. The three rays are not coplanar [D11.11]. This direct copying of the given solid angle is the chosen route, rather than reconstructing it from its separate plane angles.

**Step 2.** Construct a fourth proportional x to OU, OV, AB, and then a fourth proportional y to OV, OW, x [6.12]. On the corresponding rays mark C and D so that AC = x and AD = y, transferring the lengths to A and marking their endpoints by circles, with the drawn lines produced if necessary [1.2, P3, P2]. Consequently,
OU:OV = AB:AC,
and
OV:OW = AC:AD.

**Step 3.** From these two proportions, ex aequali,
OU:OW = AB:AD [5.22].
Hence each pair among the three original edges is proportional to the corresponding pair among AB, AC, AD. These are precisely the three proportions needed for the three faces meeting at A.

**Step 4.** Through B draw a plane parallel to ACD; through C draw a plane parallel to ABD; and through D draw a plane parallel to ABC. Each construction is obtained by drawing through the designated point two lines respectively parallel to the two intersecting edge-lines in the corresponding plane [1.31], taking the plane through the constructed lines [11.2], and applying the criterion for parallel planes [11.15]. Together with ABC, ABD, ACD, these planes complete a parallelepiped T whose edges at A are AB, AC, AD.

**Step 5.** The faces of S and T are parallelograms [11.24]. Pair the faces containing OU, OV with those containing AB, AC; those containing OV, OW with those containing AC, AD; and those containing OW, OU with those containing AD, AB. In each pair, the angles at O and A are equal by Step 1. Opposite angles of a parallelogram are equal [1.34], and adjacent angles sum to two right angles [1.29]; therefore the remaining corresponding angles are also equal, since all right angles are equal and subtraction of equals leaves equals [P4, CN3]. Opposite sides of each parallelogram are equal [1.34], so the proportions in Steps 2–3 give proportional sides about every pair of corresponding equal angles. Thus these three pairs of faces are similar [D6.1].

**Step 6.** In either S or T, consider two opposite faces, matching their vertices along the edges joining them. Their corresponding sides are parallel, because the two parallel face-planes are cut by the intervening face-planes [11.16]. Their corresponding sides are also equal, being opposite sides of the intervening parallelograms [1.34]. Their corresponding angles are equal because their containing sides are respectively parallel [11.10]. Hence each face is similar to its opposite face [D6.1].

**Step 7.** Each of the three pairs of faces established as similar in Step 5 has a pair of opposite faces. By Step 6 and the transitivity of similarity of rectilineal figures, these opposite faces are likewise similar in their corresponding pairs [6.21]. Thus S and T are contained by six faces respectively similar to one another. Therefore S and T are similar solids [D11.9].

**Step 8.** The correspondence preserves the order of the three faces at the equal solid angles O and A [11.26], while the remaining faces are their corresponding parallel opposites by the construction in Step 4 [11.15]. Thus T is similarly situated to S. Therefore, on the given straight line AB, a parallelepipedal solid similar and similarly situated to the given parallelepipedal solid has been described.

**USED:** 1.2, 1.29, 1.31, 1.34, 11.10, 11.15, 11.16, 11.2, 11.24, 11.26, 5.22, 6.12, 6.21, CN3, D11.11, D11.9, D6.1, P2, P3, P4
**Human refs (from References field):** 5.22, 6.12, D11.9
**Jaccard:** 0.150 — AI adds ['1.2', '1.29', '1.31', '1.34', '11.10', '11.15', '11.16', '11.2', '11.24', '11.26', '6.21', 'CN3', 'D11.11', 'D6.1', 'P2', 'P3', 'P4']

## Proposition 11.28
**Statement:** If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid will be bisected by the plane.

**Step 1.** Label the parallelepiped ABCD–EFGH, with joining edges AE, BF, CG, DH, so that the given cutting plane passes through the diagonals AC and EG of the opposite faces ABCD and EFGH. These diagonals are parallel, being the intersections of parallel planes with the cutting plane (11.16). All six faces are parallelograms, and opposite faces are equal (11.24).

**Step 2.** The cutting plane contains AE and CG because it contains their endpoints (D1.7). Its intersections with the face planes are straight lines (11.3), so its section through the solid is the quadrilateral ACGE. Consequently, the two resulting parts have the following bounding faces:
• First part: ABC, EFG, ABFE, BCGF, ACGE.
• Second part: CDA, GHE, CDHG, DAEH, ACGE.
These are the surfaces bounding the two parts (D11.2).

**Step 3.** Opposite faces are not only equal but similar. Indeed, their corresponding sides are equal, since each such pair consists of opposite sides of a connecting parallelogram face (1.34). Their corresponding angles are equal, since the sides forming them are respectively parallel and similarly directed (11.10). Their corresponding sides are therefore proportional and their corresponding angles equal, which establishes similarity (D6.1). Their equality was established in Step 1 (11.24).

**Step 4.** The equalities of corresponding sides and angles of opposite faces from Step 3, together with the equalities of opposite sides and angles within each parallelogram (1.34), give
AB = GH, BC = HE, and ∠ABC = ∠GHE;
and also
EF = CD, FG = DA, and ∠EFG = ∠CDA
(CN1).
Thus triangle ABC is equal to triangle GHE, and triangle EFG is equal to triangle CDA, with their remaining corresponding sides and angles also equal (1.4). Each pair is consequently similar as well (D6.1). Here the side–angle–side route is chosen because the two sides and their included angle are already known.

**Step 5.** Pair the remaining bounding faces as follows: ABFE with CDHG, BCGF with DAEH, and ACGE with itself. The first two pairs are opposite faces of the original parallelepiped and hence are equal and similar by Step 3 (11.24; D6.1). The last face is common to both parts and is equal and similar to itself (CN4; D6.1).

**Step 6.** Each part is therefore contained by five faces, respectively equal and similar to the five faces bounding the other part. By D11.10, the two parts are equal and similar solids, and in particular they are equal. Since they are precisely the two parts into which the given plane cuts the parallelepiped, that plane bisects the solid.

**USED:** 1.34, 1.4, 11.10, 11.16, 11.24, 11.3, CN1, CN4, D1.7, D11.10, D11.2, D6.1
**Human refs (from References field):** 1.34, D11.10
**Jaccard:** 0.167 — AI adds ['1.4', '11.10', '11.16', '11.24', '11.3', 'CN1', 'CN4', 'D1.7', 'D11.2', 'D6.1']

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let the common base be the parallelogram ABCD, and let the upper faces of the two solids P and Q be EFGH and KLMN respectively, with standing edges AE, BF, CG, DH and AK, BL, CM, DN. Label the vertices so that E, F, K, L lie on one straight line and H, G, N, M on the other straight line specified in the hypothesis. All faces of either solid are parallelograms (11.24). We shall compare two end solids and subtract them from one common enclosing solid; this route does not require the upper edges to overlap.

**Step 2.** Opposite sides of the parallelogram faces are equal and parallel (1.34). In particular, EF = KL = AB, while EH, FG, KN, LM are equal and parallel to AD. If E = K, these relations make all corresponding upper vertices coincide, and P = Q by CN4. Otherwise, interchange the solids if necessary so that K lies beyond E in the direction from E to F. Since EF and KL are equal and have the same direction, L then lies beyond F, and EK = FL, by addition or subtraction of the intervening segments (CN2, CN3). Moreover, EH is parallel to KN, and FG to LM (11.9), so EKNH and FLMG are parallelograms. Consequently EK = HN and FL = GM (1.34), and therefore HN = GM (CN1).

**Step 3.** The points A, B, E, F, K, L lie in one side-face plane, and D, C, H, G, N, M lie in its parallel opposite side-face plane: the straight lines EF and HG remain in those respective planes when extended (11.1). Form the end solid U with triangular faces AEK and DHN and lateral faces ADHE, ADNK, EKNH. Form V with triangular faces BFL and CGM and lateral faces BCGF, BCML, FLMG. The necessary joins may be drawn by P1; all the listed faces are planar, being either triangles or the parallelograms already identified.

**Step 4.** We have AE = BF and DH = CG (1.34), and EK = FL and HN = GM by Step 2. Since AE is parallel to BF and their upper endpoints lie on the same straight line, angle AEK equals angle BFL (1.29). Likewise angle DHN equals angle CGM (1.29). Thus triangles AEK and BFL are congruent, as are triangles DHN and CGM, by 1.4. Here 1.4 is the natural first congruence test: two equal sides and their included angle are already available. In particular, the corresponding triangular faces are equal and similar (D6.1).

**Step 5.** The lateral faces also correspond in equal, similar pairs. For ADHE and BCGF, the adjacent sides AD, AE equal BC, BF respectively (1.34), and angle DAE equals angle CBF because their respective sides are parallel (11.10). For ADNK and BCML, similarly AD = BC, AK = BL, and angle DAK equals angle CBL (1.34, 11.10). Finally, for EKNH and FLMG, we have EK = FL and EH = FG, while angle KEH equals angle LFG by 1.29. In each pair, draw the corresponding diagonals (P1). Applying 1.4 and the parallelogram properties in 1.34 gives corresponding congruent triangular halves. Hence the whole parallelograms are equal and similar (CN2, D6.1).

**Step 6.** Thus U and V are contained by corresponding similar faces equal in number and magnitude. They are therefore equal solid figures by D11.10: U = V.

**Step 7.** Take the enclosing solid W whose end faces are ABLE and DCMH and whose remaining faces are ABCD, ELMH, ADHE, and BCML. These faces lie in the side, base, and upper planes already identified. The plane BCGF cuts W into P and V: its traces on the two end faces are BF and CG. The plane ADNK cuts W into Q and U: its corresponding traces are AK and DN (11.3). Thus the two dissections give W = P + V and W = Q + U (CN2). Both dissections are valid whether K precedes, coincides with, or follows F on their common straight line.

**Step 8.** Subtract the equal solids V and U from the same enclosing solid W. The remainders P and Q are equal by CN3. Therefore the given parallelepipedal solids are equal to one another.

**USED:** 1.29, 1.34, 1.4, 11.1, 11.10, 11.24, 11.3, 11.9, CN1, CN2, CN3, CN4, D11.10, D6.1, P1
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.118 — AI adds ['1.29', '11.1', '11.10', '11.24', '11.3', '11.9', 'CN1', 'CN2', 'CN3', 'CN4', 'D11.10', 'D6.1', 'P1']; Human adds ['1.36', '1.8']

## Proposition 11.30
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another.

**Step 1.** Let the two solids have the common base ABCD and opposite faces EFGH and E′F′G′H′, respectively, with corresponding vertices listed in the same order. Their faces are parallelograms. Thus EF and HG are parallel to AB, while E′H′ and F′G′ are parallel to AD. The opposite face-planes of each solid are parallel. [11.24]

**Step 2.** Both upper faces lie in one plane Π parallel to the base plane. Indeed, section the upper planes and the base plane by planes containing a perpendicular to the base. Their section-lines are parallel, and the chosen perpendicular is perpendicular to the base section-line. Moreover, the perpendicular separation of two parallel planes is constant: perpendiculars to the base are parallel, and in the plane containing two such perpendiculars the intercepted segments are opposite sides of a parallelogram, hence equal. Therefore the equal heights put the two upper section-lines at the same point of the perpendicular, on the same side of the base. They consequently coincide in every such section, so the upper planes coincide. [11.16, D11.3, 11.6, 1.34, D6.4]

**Step 3.** We construct an intermediate solid so that 11.29 applies first along one direction of the base and then along the other; this directly reduces the present configuration to the preceding proposition. In Π produce the sides as necessary and define
I = EF ∩ E′H′,
J = EF ∩ F′G′,
K = HG ∩ F′G′,
L = HG ∩ E′H′.
These intersections exist: EF and HG form one pair of parallel lines, and E′H′ and F′G′ another; their directions are those of the intersecting base sides AB and AD, so a line of one pair is not parallel to a line of the other. Thus IJKL is a parallelogram. [P2, 11.9, 1.30, D1.23]

**Step 4.** Join AI, BJ, CK and DL. The faces ABJI and DCKL lie in the opposite lateral planes ABFE and DCGH of the first solid. The faces ADLI and BCKJ lie in the opposite lateral planes ADH′E′ and BCG′F′ of the second solid. Each of these two pairs of planes is parallel; the remaining pair consists of the base plane and Π. Consequently these six planes bound a parallelepipedal solid U = ABCD–IJKL, whose faces are parallelograms. Its base is ABCD and its height is the common height of the original solids. [P1, 11.24, D6.4]

**Step 5.** Compare the first solid with U. They have the same base and height. Furthermore, E, F, I and J lie on the straight line EF, while H, G, L and K lie on the straight line HG. Their upper extremities therefore satisfy exactly the same-straight-lines condition of 11.29. Hence the first solid equals U. [11.29]

**Step 6.** Compare the second solid with U, now using the other direction of the base. Again their bases and heights are the same. The points E′, H′, I and L lie on E′H′, while F′, G′, J and K lie on F′G′. Thus the same-straight-lines condition is again satisfied, and the second solid equals U. [11.29]

**Step 7.** Since both original solids equal U, they equal one another. Therefore parallelepipedal solids on the same base and of the same height, whose upper extremities are not on the same straight lines, are equal. [CN1]

**USED:** 1.30, 1.34, 11.16, 11.24, 11.29, 11.6, 11.9, CN1, D1.23, D11.3, D6.4, P1, P2
**Human refs (from References field):** 11.29
**Jaccard:** 0.077 — AI adds ['1.30', '1.34', '11.16', '11.24', '11.6', '11.9', 'CN1', 'D1.23', 'D11.3', 'D6.4', 'P1', 'P2']

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let S₁ and S₂ be parallelepipedal solids on equal bases K₁ and K₂, with common perpendicular height h. Their bases are parallelograms [11.24; D6.4]. We shall first replace each solid by an equal rectangular box, preserving its base area and height, and then compare the boxes as parts cut from one containing box.

**Step 2.** On each Kᵢ construct a right parallelepiped Uᵢ of height h: erect perpendiculars to its plane at the four vertices and mark equal lengths h on the same side [11.12; P3]. These perpendiculars are parallel; joining their endpoints gives parallelogram faces and an upper face parallel to Kᵢ [11.6; 1.33; 11.15]. Thus Sᵢ and Uᵢ have the same base and height, so Sᵢ = Uᵢ. Here use 11.29 when the upper endpoints lie on the same straight lines specified there, and 11.30 otherwise. This chooses the earlier, special same-base result whenever its additional condition holds [11.29; 11.30].

**Step 3.** Consider either Uᵢ, writing its lower base as ABCD and its corresponding upper vertices as A′, B′, C′, D′. Draw through A a perpendicular to AB meeting the line DC, produced if necessary, at E; through B draw a parallel to AE meeting that same line at F [1.11; 1.31; P2]. Then ABFE is a rectangle [1.29]. Moreover, ABCD and ABFE are on the same base AB and between the same parallels AB and DC, so their areas are equal. The same-base proposition 1.35 is the directly applicable planar result [1.35].

**Step 4.** In the plane DCC′D′, draw through E and F parallels to DD′, meeting the line D′C′, produced if necessary, at E′ and F′ [1.31; P2]. The resulting parallelograms show that EE′ = FF′ = DD′ = h [1.34]. Also EE′ and FF′ are perpendicular to the lower base plane, since they are parallel to DD′ [11.8]. Consequently the vertices A, B, F, E and A′, B′, F′, E′ bound a rectangular box Bᵢ of height h on ABFE [1.33; 11.15].

**Step 5.** Regard Uᵢ and Bᵢ as standing instead on their common lateral face ABB′A′. The line AE is perpendicular to AB by construction, and to AA′ because AA′ is perpendicular to the original base plane [D11.3]. Hence AE is perpendicular to the plane ABB′A′ [11.4]. The opposite faces of both solids lie in the plane DCC′D′, which contains E; thus both have height AE relative to this common base. Their standing-edge endpoints lie on the same two straight lines: D, C, E, F lie on DC, and D′, C′, E′, F′ lie on D′C′. Therefore Uᵢ = Bᵢ by precisely the aligned-endpoint case 11.29 [11.29].

**Step 6.** Apply Steps 3–5 to both U₁ and U₂. We obtain rectangular boxes B₁ and B₂ of height h whose base rectangles r₁ and r₂ are equal in area, and S₁ = B₁, S₂ = B₂ [1.35; CN1]. It remains to prove B₁ = B₂.

**Step 7.** By superposition, place the boxes with a common lower vertex and their three corresponding perpendicular edge directions agreeing [P4; CN4]. If their base rectangles coincide, the boxes also coincide because their heights are equal, and hence B₁ = B₂ [CN4]. Otherwise, neither base rectangle can contain the other, since they are equal in area and a whole is greater than a proper part [CN5]. Consequently, after interchanging the labels if necessary, their two horizontal edge lengths may be written as a, b and c, d, with a > c and b < d.

**Step 8.** Construct the containing rectangular box W with horizontal edge lengths a, d and height h, using the same perpendicular and parallel constructions as above [11.12; 1.31; 11.15]. A plane parallel to its appropriate opposite faces cuts W into B₁ and a remaining box T₁; another such plane cuts W into B₂ and a remaining box T₂. Both remainders are nonzero because b < d and c < a. If w is the lower base of W and t₁, t₂ are the lower bases of T₁, T₂, then w consists respectively of r₁ together with t₁ and of r₂ together with t₂. Since r₁ = r₂, subtraction gives t₁ = t₂ [CN3].

**Step 9.** Apply 11.25 to the two cuts of W. It gives
B₁ : T₁ = r₁ : t₁,
and
B₂ : T₂ = r₂ : t₂.
Since r₁ = r₂ and t₁ = t₂, these base ratios are equal, and therefore B₁ : T₁ = B₂ : T₂ [11.25; 5.7; 5.11].

**Step 10.** By composition,
(B₁ + T₁) : T₁ = (B₂ + T₂) : T₂ [5.18].
Both sums are W, so W : T₁ = W : T₂. Magnitudes to which the same magnitude has the same ratio are equal; hence T₁ = T₂ [5.9]. Subtracting these equal remainders from W gives B₁ = B₂ [CN3].

**Step 11.** Since S₁ = B₁ and S₂ = B₂, it follows that S₁ = S₂ [CN1]. Therefore parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**USED:** 1.11, 1.29, 1.31, 1.33, 1.34, 1.35, 11.12, 11.15, 11.24, 11.25, 11.29, 11.30, 11.4, 11.6, 11.8, 5.11, 5.18, 5.7, 5.9, CN1, CN3, CN4, CN5, D11.3, D6.4, P2, P3, P4
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.267 — AI adds ['1.11', '1.29', '1.31', '1.33', '1.34', '11.12', '11.15', '11.4', '11.6', '11.8', '5.18', 'CN1', 'CN3', 'CN4', 'CN5', 'D11.3', 'D6.4', 'P2', 'P3', 'P4']; Human adds ['1.23', 'D11.10']

## Proposition 11.32
**Statement:** Parallelepipedal solids which are of the same height are to one another as their bases.

**Step 1.** Let S and T be parallelepipedal solids of the same height, with bases ABCD and EFGH respectively. Their bases are parallelograms (11.24). Denote their areas by P and Q. We must prove S:T = P:Q.

**Step 2.** Draw the diagonal EG of the second base, dividing it into triangles EFG and EGH (P1). Produce AB beyond B and DC beyond C (P2). Apply to BC a parallelogram BLKC equal to triangle EFG, choosing its angle at B so that BL lies along AB produced (1.44). Next apply to LK a parallelogram LNMK equal to triangle EGH, choosing its angle at L so that LN continues BL (1.44).

**Step 3.** In this construction A, B, L, N lie on one straight line, and D, C, K, M lie on the parallel straight line. Also BC, LK, and NM are parallel. Consequently BNMC and ANMD are parallelograms (1.30). Let R be the area of BNMC. Since its two constituent parallelograms equal the two constituent triangles of EFGH, addition gives R = Q (CN2).

**Step 4.** Complete a larger parallelepiped W over ANMD by extending S in the direction AB, retaining its original bottom and top planes. Specifically, draw through N a line parallel to the rising edge at B, and take the plane through this line and NM. This plane is parallel to the face of S through BC, since their two intersecting generating lines are respectively parallel (1.31; 11.15). Produce the original side faces to this new end plane (P2). Thus W consists of S and an adjacent parallelepiped U with base BNMC. The face separating S and U is parallel to the two outer end faces, and U has the same height as S because their bottom and top planes are the same.

**Step 5.** Apply 11.25 to W and its separating plane. It gives
S:U = P:R.
This is the direct ratio step: the auxiliary construction makes the two solids pieces of one parallelepiped cut parallel to opposite faces, exactly as required by 11.25.

**Step 6.** The bases of U and T are equal, since R = Q, and their heights are equal by Step 4 and the hypothesis. Therefore U = T (11.31). This equality theorem applies naturally here because the bases are equal in area, though they need not be the same figure.

**Step 7.** Equal magnitudes have the same ratio to any fixed magnitude, and a fixed magnitude has the same ratio to equal magnitudes. Hence S:T = S:U and P:R = P:Q (5.7). Combining these equalities with Step 5 gives S:T = P:Q (5.11). Therefore parallelepipedal solids of the same height are to one another as their bases.

**USED:** 1.30, 1.31, 1.44, 11.15, 11.24, 11.25, 11.31, 5.11, 5.7, CN2, P1, P2
**Human refs (from References field):** 1.45, 11.25, 11.31
**Jaccard:** 0.154 — AI adds ['1.30', '1.31', '1.44', '11.15', '11.24', '5.11', '5.7', 'CN2', 'P1', 'P2']; Human adds ['1.45']

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

**Step 1.** Let S and T be similar parallelepipedal solids. At corresponding vertices O and o, let their three incident edges be OA, OB, OC and oa, ob, oc, respectively. Choose OA and oa as any desired pair of corresponding sides. The corresponding faces are similar, so their corresponding angles are equal and their sides are proportional. Alternating the proportions in the faces gives
OA : oa = OB : ob = OC : oc.
[D11.9, D6.1, 5.16, 5.11]

**Step 2.** On the rays OA, OB, OC, produced if necessary, take A₁, B₁, C₁ such that OA₁ = oa, OB₁ = ob, and OC₁ = oc. These points can be obtained by circles centred at O with the respective given distances. [P2, P3]
Write Π(X,Y) for the parallelogram having adjacent sides OX and OY, and write P(X,Y,Z) for the parallelepiped having incident edges OX, OY, OZ. Complete these figures by parallels; the resulting opposite face-planes are parallel by 11.15. [1.31, 11.15]
Set
S₀ = P(A,B,C) = S,
S₁ = P(A₁,B,C),
S₂ = P(A₁,B₁,C),
S₃ = P(A₁,B₁,C₁).
Thus two intermediate solids have been inserted, and each consecutive pair differs in just one incident edge.

**Step 3.** The solid S₃ is equal and similar to T. Indeed, their three faces incident at O and o have equal corresponding adjacent sides by construction and equal included angles by Step 1. The same holds for their opposite faces: opposite edges of each parallelepiped are equal, and the angles formed by the corresponding parallel edges are equal. [1.34, 11.10, CN1]
Divide each corresponding parallelogram face by the diagonal joining the endpoints of those adjacent sides. The resulting corresponding triangles are congruent by the equality of two sides and their included angle; the other triangles have the same properties by 1.34. [1.4, 1.34]
Consequently, the corresponding faces are equal in area and similar. [CN2, D6.1] Since the two solids are contained by equal and similar corresponding faces, S₃ and T are equal and similar solids. [D11.10]

**Step 4.** We compare the completed solids directly by 11.32: it naturally applies because each consecutive pair has equal height after a suitable choice of base, without requiring a subdivision argument.
For S₀ and S₁, take the bases Π(A,B) and Π(A₁,B). Both bases lie in the plane OAB, and both opposite faces lie in the same parallel plane through C. Therefore
S₀ : S₁ = Π(A,B) : Π(A₁,B). [11.32]
The two base parallelograms have bases OA and OA₁ on the same straight line and their opposite sides on the same parallel through B. They therefore have equal height, and
Π(A,B) : Π(A₁,B) = OA : OA₁. [6.1]
Hence S₀ : S₁ = OA : OA₁. [5.11]

**Step 5.** For S₁ and S₂, take the bases Π(A₁,B) and Π(A₁,B₁). Their opposite faces again lie in the common parallel plane through C, so the solids have equal height. Thus
S₁ : S₂ = Π(A₁,B) : Π(A₁,B₁). [11.32]
Regard these parallelograms as having bases OB and OB₁. Their opposite sides lie on the same parallel through A₁, so their heights are equal. Consequently
Π(A₁,B) : Π(A₁,B₁) = OB : OB₁, [6.1]
and therefore S₁ : S₂ = OB : OB₁. [5.11]

**Step 6.** For S₂ and S₃, instead take the bases Π(B₁,C) and Π(B₁,C₁), lying in the plane OBC. Their opposite faces lie in the same parallel plane through A₁, so
S₂ : S₃ = Π(B₁,C) : Π(B₁,C₁). [11.32]
These base parallelograms, regarded as standing on OC and OC₁, have their opposite sides on the same parallel through B₁. Hence
Π(B₁,C) : Π(B₁,C₁) = OC : OC₁, [6.1]
and therefore S₂ : S₃ = OC : OC₁. [5.11]

**Step 7.** By Steps 1–2 and the three comparisons,
S₀ : S₁ = S₁ : S₂ = S₂ : S₃ = OA : oa. [5.11]
Thus S₀, S₁, S₂, S₃ are four continuously proportional magnitudes. By the definition of triplicate ratio, S₀ : S₃ is the triplicate ratio of S₀ : S₁, and therefore of OA : oa. [D5.10]
Since S₀ = S and S₃ = T, the ratio S : T is the triplicate ratio of OA : oa. The corresponding sides OA and oa were arbitrary. Therefore similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

**USED:** 1.31, 1.34, 1.4, 11.10, 11.15, 11.32, 5.11, 5.16, 6.1, CN1, CN2, D11.10, D11.9, D5.10, D6.1, P2, P3
**Human refs (from References field):** 11.24, 11.32, 6.1, D11.10, D5.10
**Jaccard:** 0.222 — AI adds ['1.31', '1.34', '1.4', '11.10', '11.15', '5.11', '5.16', 'CN1', 'CN2', 'D11.9', 'D6.1', 'P2', 'P3']; Human adds ['11.24']

## Proposition 11.34
**Statement:** In equal parallelepipedal solids the bases are reciprocally proportional to the heights; and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let the given parallelepipedal solids be S₁ and S₂, with bases F₁ and F₂ and perpendicular heights h₁ and h₂ respectively (D6.4). We must prove that S₁ = S₂ if and only if F₁ : F₂ = h₂ : h₁; this is the asserted reciprocal proportionality (D5.13).

**Step 2.** Write ABCD for the base F₁. At A erect a perpendicular to its plane (11.12), and on the same ray take AA₁ = h₁ and AA₂ = h₂, producing the ray as necessary (P2, 1.3). Complete by parallels two right parallelepipeds R₁ and R₂ on ABCD, with these upright edges and with their other upright edges lying on the same fixed lines through B, C, D (1.31, 11.15). These other upright edges are perpendicular to the base plane by 11.8 and equal to the corresponding AAᵢ by 1.34. Thus R₁ and R₂ have heights h₁ and h₂ respectively. Since R₁ and S₁ have equal bases and the same height, R₁ = S₁ by 11.31. This theorem applies irrespective of the inclination of the original solid’s edges.

**Step 3.** The solids R₂ and S₂ have the same height h₂. Therefore, by 11.32,
R₂ : S₂ = F₁ : F₂.

**Step 4.** Let L₁ = ABB₁A₁ and L₂ = ABB₂A₂ be the lateral faces of R₁ and R₂ along AB. Regard these faces as bases. Their planes coincide, and the planes of their respective opposite faces along CD also coincide; these two fixed planes are parallel by 11.15. Hence R₁ and R₂ have the same height in this new orientation (D6.4). The chosen route is to apply 11.32 again, now to lateral bases, obtaining
R₂ : R₁ = L₂ : L₁.

**Step 5.** In their common plane, regard AA₂ and AA₁ as the bases of the parallelograms L₂ and L₁. Both have height AB, since AB is perpendicular to the upright line through A (D11.3). Consequently, by 6.1,
L₂ : L₁ = AA₂ : AA₁ = h₂ : h₁.
Combining this with Step 4 gives
R₂ : R₁ = h₂ : h₁
by 5.11.

**Step 6.** First suppose S₁ = S₂. Since R₁ = S₁, we have R₁ = S₂ (CN1). Equal magnitudes have equal ratios to the same magnitude, and conversely as consequents, so R₂ : S₂ = R₂ : R₁ (5.7). Steps 3 and 5 therefore give
F₁ : F₂ = h₂ : h₁
by 5.11. Thus equal parallelepipedal solids have bases reciprocally proportional to their heights.

**Step 7.** Conversely, suppose F₁ : F₂ = h₂ : h₁. By Steps 3 and 5 and 5.11,
R₂ : S₂ = R₂ : R₁.
Magnitudes to which the same magnitude has the same ratio are equal; hence S₂ = R₁ (5.9). Since R₁ = S₁, it follows that S₁ = S₂ (CN1). Therefore parallelepipedal solids whose bases are reciprocally proportional to their heights are equal, completing both directions.

**USED:** 1.3, 1.31, 1.34, 11.12, 11.15, 11.31, 11.32, 11.8, 5.11, 5.7, 5.9, 6.1, CN1, D11.3, D5.13, D6.4, P2
**Human refs (from References field):** 11.25, 11.29, 11.30, 11.31, 11.32, 5.7, 5.9, 6.1
**Jaccard:** 0.250 — AI adds ['1.3', '1.31', '1.34', '11.12', '11.15', '11.8', '5.11', 'CN1', 'D11.3', 'D5.13', 'D6.4', 'P2']; Human adds ['11.25', '11.29', '11.30']

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

**Step 1.** Let the equal plane angles be ∠B₀AC₀ and ∠E₀DF₀, in planes α and β. Let X and Y be the arbitrary points on the elevated rays, so that ∠B₀AX = ∠E₀DY and ∠C₀AX = ∠F₀DY. Let XU and YV be their perpendiculars to α and β. Draw the joins required below by P1; every triangle used is planar by 11.2. We must prove ∠XAU = ∠YDV. If either elevated ray is perpendicular to its base plane, the given angle equalities and 11.4 make the other perpendicular also, and both inclinations are right (D11.3, P4). Thus consider the nonperpendicular case, in which U ≠ A and V ≠ D.

**Step 2.** Our route is to make the elevated segments equal and then compare triangles on a transversal through one perpendicular foot. By cutting the longer of AX and DY, choose G on AX and H on DY with AG = DH (1.3). In triangles AXU and DYV, draw GP parallel to XU and HQ parallel to YV, meeting AU and DV at P and Q respectively; retain the original perpendicular wherever the endpoint was not changed (1.31). These intersections lie on the corresponding segments, by the parallel-side construction and 6.2. Moreover, GP is perpendicular to α and HQ to β (11.8). Since the respective rays have not changed, ∠GAP = ∠XAU and ∠HDQ = ∠YDV (D1.9). It therefore suffices to prove ∠GAP = ∠HDQ.

**Step 3.** Through P draw a straight line in α which does not pass through A and is not parallel to either original arm. Let it meet the complete straight lines AB₀ and AC₀ at B and C respectively (P1, P2, D1.23). Thus A, B, C are not collinear. Interchange the names of the two arms in both configurations if necessary so that B ≠ P; this is possible because P ≠ A and the two arms meet only at A.

**Step 4.** On the corresponding complete lines DE₀ and DF₀ take E and F with DE = AB and DF = AC, choosing the original or opposite ray according as B and C lie on the original or opposite rays from A (P2, 1.3). We then have
∠BAC = ∠EDF,  ∠BAG = ∠EDH,  and  ∠CAG = ∠FDH.
Indeed, reversing an arm replaces the relevant angle by its supplement; doing so in both configurations preserves equality, since all right angles are equal and equal angles subtracted from two right angles leave equal remainders (1.13, P4, CN3).

**Step 5.** Apply 1.4 to triangles ABC and DEF, using AB = DE, AC = DF, and ∠BAC = ∠EDF. Thus BC = EF and ∠ABC = ∠DEF. Apply 1.4 also to triangles ABG and DEH, and to triangles ACG and DFH, using AG = DH and the corresponding equal angles from Step 4. This gives BG = EH and CG = FH.

**Step 6.** The three sides of triangle GBC are now respectively equal to those of triangle HEF. Therefore 1.8, naturally applicable because all three side equalities are known, gives ∠GBC = ∠HEF.

**Step 7.** On the complete line EF choose R with ER = BP. Choose R on the ray EF if P is on the ray BC, and on the opposite ray from E otherwise (P2, 1.3). Since B ≠ P, also E ≠ R. The angle equalities in Steps 5 and 6 now give
∠ABP = ∠DER  and  ∠GBP = ∠HER.
When P is on the ray BC these are the equalities already obtained; otherwise they are equal supplements of those angles (1.13, P4, CN3). This construction therefore covers an exterior perpendicular foot as well as an interior one.

**Step 8.** In triangles ABP and DER, we have AB = DE, BP = ER, and the equal included angles established in Step 7. Hence AP = DR (1.4). Similarly, triangles GBP and HER have GB = HE, BP = ER, and equal included angles; consequently GP = HR and ∠GPB = ∠HRE (1.4). Since GP is perpendicular to α and PB lies in α, ∠GPB is right (D11.3). Thus HR is perpendicular to EF.

**Step 9.** Compare triangles AGP and DHR. Their three corresponding sides are equal: AG = DH by construction, AP = DR by Step 8, and GP = HR by Step 8. Therefore ∠GPA = ∠HRD and ∠GAP = ∠HDR (1.8). But ∠GPA is right because GP is perpendicular to α (D11.3). Hence HR is perpendicular to DR also.

**Step 10.** The lines RE and RD are distinct intersecting lines in β: E and R lie on EF, whereas D does not. Since HR is perpendicular to both, it is perpendicular to β (11.4). The given auxiliary perpendicular HQ is also perpendicular to β. If R and Q were distinct, triangle HRQ would have right angles at both R and Q (D11.3), contradicting 1.17, which says that any two angles of a triangle are together less than two right angles. Therefore R = Q.

**Step 11.** Substituting R = Q in the equality from Step 9 yields ∠GAP = ∠HDQ. By Step 2 these are respectively ∠XAU and ∠YDV. Hence ∠XAU = ∠YDV (CN1): the joins from the perpendicular feet to the original vertices contain equal angles with the elevated straight lines, as required.

**USED:** 1.13, 1.17, 1.3, 1.31, 1.4, 1.8, 11.2, 11.4, 11.8, 6.2, CN1, CN3, D1.23, D1.9, D11.3, P1, P2, P4
**Human refs (from References field):** 1.26, 1.4, 1.47, 1.48, 1.8, 11.8
**Jaccard:** 0.143 — AI adds ['1.13', '1.17', '1.3', '1.31', '11.2', '11.4', '6.2', 'CN1', 'CN3', 'D1.23', 'D1.9', 'D11.3', 'P1', 'P2', 'P4']; Human adds ['1.26', '1.47', '1.48']

## Proposition 11.36
**Statement:** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

**Step 1.** Let the three given straight lines have lengths a, b, c, with a:b = b:c, and let S be the parallelepipedal solid formed from them. At a vertex O, denote its three edges by OA, OB, OC, where OA = a, OB = b, OC = c. The stated proportion is the hypothesis that the three lines are proportional [D5.6]. Choose the face with adjacent edges OA and OC as the base. This choice keeps the mean edge OB as the standing edge and leads directly to equality of bases by 6.14 and equality of solids by 11.31.

**Step 2.** On the rays OA and OC take points D and E respectively such that OD = OE = b, producing the edges if necessary [P2, 1.3]. Complete the parallelogram ODFE in the base plane by drawing parallels [1.31]. Its angle DOE is the same as the angle AOC of the original base, and
OA:OD = a:b = b:c = OE:OC.
Thus the sides about these equal angles are reciprocally proportional. Consequently the parallelogram ODFE is equal to the base of S [6.14].

**Step 3.** Complete a solid T on ODFE with OB as its standing edge, drawing its remaining edges parallel to OA, OC and OB [1.31]. The opposite face planes so obtained are parallel, since each contains two intersecting lines parallel to two intersecting lines in the corresponding opposite face [11.15]; hence T is a parallelepiped. Its opposite base through B lies in the opposite-base plane of S: the two edges from B in that face run along the same straight lines as the corresponding edges of S.

**Step 4.** The three edges OD, OE and OB of T are all equal to b. Every other edge equals one of these, by equality of opposite sides of the parallelogram faces; therefore T is equilateral [1.34]. Moreover, its three edge rays at O are precisely the corresponding edge rays of S, and its remaining corresponding edges are parallel and similarly directed. Thus the corresponding face angles are equal, using the angle properties of parallels in a plane and of pairs of parallel lines in space [1.29, 11.10]. Hence T is equiangular with S.

**Step 5.** The bases of S and T are equal by Step 2. By Step 3 their bases lie in the same plane and their opposite bases lie in the same parallel plane, so they have the same height. Parallelepipedal solids on equal bases and of the same height are equal [11.31]. Therefore S = T: the parallelepipedal solid formed from the three proportional straight lines equals the equilateral parallelepipedal solid on the mean which is equiangular with it.

**USED:** 1.29, 1.3, 1.31, 1.34, 11.10, 11.15, 11.31, 6.14, D5.6, P2
**Human refs (from References field):** 11.31, 11.35, 6.14
**Jaccard:** 0.182 — AI adds ['1.29', '1.3', '1.31', '1.34', '11.10', '11.15', 'D5.6', 'P2']; Human adds ['11.35']

## Proposition 11.37
**Statement:** If four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described will also be proportional; and, if the parallelepipedal solids on them which are similar and similarly described be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let a, b, c, d be the four straight lines, and let A, B, C, D be the respective parallelepipedal solids, similar and similarly described, with these lines as corresponding edges. We use 11.33 because it directly relates the ratios of these solids to those of their corresponding edges.

**Step 2.** By repeated application of 6.11, construct straight lines x, y, z, w such that

a:b = b:x = x:y, and c:d = d:z = z:w.

Thus a:y is the triplicate ratio of a:b, and c:w is the triplicate ratio of c:d [D5.10]. Consequently,

A:B = a:y, and C:D = c:w [11.33].

**Step 3.** First suppose that a:b = c:d. The corresponding successive ratios in the two chains of Step 2 are therefore equal. Hence, ex aequali, a:y = c:w [5.22]. Combining this with Step 2 gives A:B = C:D [5.11]. Thus the solids are proportional [D5.6].

**Step 4.** Conversely, suppose that A:B = C:D. Construct a fourth proportional e to a, b, c, so that a:b = c:e [6.12]. On e construct a parallelepipedal solid E similar and similarly described to C [11.27]. The corresponding faces of D and E are similar to the same faces of C, and hence are similar to one another [6.21]. Since their faces are also equal in multitude, D and E are similar solids [D11.9]. This construction reduces the converse to comparing the corresponding edges of two equal similar solids.

**Step 5.** Applying the forward implication proved in Steps 2–3 to a, b, c, e and their solids gives A:B = C:E. Together with the hypothesis A:B = C:D, this yields C:D = C:E [5.11]. Therefore D = E, since magnitudes to which the same magnitude has the same ratio are equal [5.9].

**Step 6.** Construct straight lines p, q such that d:e = e:p = p:q [6.11]. Since D and E are similar and d, e are their corresponding edges,

D:E = d:q [11.33, D5.10].

But D = E by Step 5. Taking each of the equimultiples in the definition of equal ratios to be the magnitude itself, the equality D = E therefore implies d = q [D5.5].

**Step 7.** If d were greater than e, then d:e = e:p would imply e > p, and e:p = p:q would imply p > q [5.14]. Hence d > e > p > q, contrary to d = q. If d were less than e, the same applications of 5.14 would give d < e < p < q, again contrary to d = q. Therefore d = e.

**Step 8.** Since d = e, we have c:d = c:e [5.7]. Combining this with the constructed proportion a:b = c:e gives a:b = c:d [5.11]. Thus the straight lines are proportional [D5.6]. Both implications are proved.

**USED:** 11.27, 11.33, 5.11, 5.14, 5.22, 5.7, 5.9, 6.11, 6.12, 6.21, D11.9, D5.10, D5.5, D5.6
**Human refs (from References field):** 11.33
**Jaccard:** 0.071 — AI adds ['11.27', '5.11', '5.14', '5.22', '5.7', '5.9', '6.11', '6.12', '6.21', 'D11.9', 'D5.10', 'D5.5', 'D5.6']

## Proposition 11.38
**Statement:** If the sides of the opposite planes of a cube be bisected, and planes be carried through the points of section, the common section of the planes and the diameter of the cube bisect one another.

**Step 1.** Let the opposite faces of the cube be ABCD and A'B'C'D', with AA', BB', CC', DD' the joining edges. Let M, N, P, Q bisect AB, BC, CD, DA respectively, and let M', N', P', Q' bisect the corresponding sides of A'B'C'D'. Denote the cutting planes MPP'M' and NQQ'N' by Π and Σ. The faces are squares, hence equilateral and right-angled. [D11.25, D1.22]

**Step 2.** Opposite sides of each square face are parallel. [1.28] Thus AA' ∥ BB' and BB' ∥ CC', whence AA' ∥ CC'. [11.9] Moreover, AA' = AB = BC = CC', so AA' = CC'. [D1.22, CN1] The joins AC and A'C' lie in the plane of the parallel edges AA', CC'; since these edges are equal and parallel, AC ∥ A'C'. Consequently ACC'A' is a parallelogram in one plane. [11.7, 1.33]

**Step 3.** Bisect AC, A'C', and the cube's diameter AC' at X, Y, and T respectively, and draw the joins used below. [1.10, P1] We take the planar midpoint route: divisions into equal halves have the same ratio, so the converse of 6.2 applies immediately to any two bisected sides of a triangle. This is the natural route from the given bisections, without comparing solids. [D5.5, 6.2]

**Step 4.** Apply the converse of 6.2 to triangles ABC, CDA, BCA, and DAC respectively. Since the relevant sides are bisected, it gives
MX ∥ BC, PX ∥ DA, NX ∥ BA, and QX ∥ DC. [6.2]
Since BC ∥ DA and BA ∥ DC, the lines MX and PX coincide, and the lines NX and QX coincide: distinct lines parallel to the same line cannot meet. Thus M, X, P are collinear, and N, X, Q are collinear. [1.30, D1.23]

**Step 5.** The identical applications in the upper square give M', Y, P' collinear and N', Y, Q' collinear. [6.2, 1.30, D1.23] Therefore both Π and Σ contain X and Y. [11.1] Their traces on ABCD are the distinct lines MP and NQ, so Π and Σ are distinct planes. Their common section is consequently the straight line XY; its portion within the cube is terminated at X and Y on the opposite faces. [11.3]

**Step 6.** In triangle ACC', X and T bisect AC and AC', so XT ∥ CC'. In triangle C'A'A, Y and T bisect C'A' and C'A, so YT ∥ A'A. [6.2] Since AA' ∥ CC', the lines XT and YT coincide. Hence X, T, Y are collinear. [1.30, D1.23] Moreover, T is between A and C', and therefore lies between the parallel sides AC and A'C' of the diagonal parallelogram. It is consequently between their intersections X and Y with this common line. Thus the common section XY meets the diameter AC' at T.

**Step 7.** Because AC ∥ A'C', the alternate angles XAT and YC'T are equal. [1.29] The vertical angles XTA and YTC' are also equal. [1.15] Together with AT = TC' from the construction, these equalities make triangles XAT and YC'T congruent by the equal-angle-and-included-side criterion; hence XT = TY. [1.10, 1.26] We therefore have both AT = TC' and XT = TY. Thus the diameter of the cube and the common section of the cutting planes bisect one another, as required.

**USED:** 1.10, 1.15, 1.26, 1.28, 1.29, 1.30, 1.33, 11.1, 11.3, 11.7, 11.9, 6.2, CN1, D1.22, D1.23, D11.25, D5.5, P1
**Human refs (from References field):** 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.9
**Jaccard:** 0.250 — AI adds ['1.10', '1.28', '1.30', '11.1', '11.3', '11.7', '6.2', 'CN1', 'D1.22', 'D1.23', 'D11.25', 'D5.5', 'P1']; Human adds ['1.14', '1.4']

## Proposition 11.39
**Statement:** If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms will be equal.

**Step 1.** Let the first prism P have triangular faces ABC and A′B′C′, and stand on its parallelogram face ABB′A′, with CC′ the opposite edge. Let the second prism Q have triangular base EFG and opposite triangular face E′F′G′. Thus the parallelogram base in the statement is a supporting face of the first triangular prism, not the base of a parallelepiped. Let their common perpendicular height be h. By hypothesis, ABB′A′ is double triangle EFG. (D11.13; D6.4; hypothesis.)

**Step 2.** Complete ABC and A′B′C′ to parallelograms ABCD and A′B′C′D′, and join DD′. Likewise complete EFG and E′F′G′ to parallelograms EFGH and E′F′G′H′, and join HH′. The parallels are constructed by 1.31 and the joining lines by P1. Corresponding new sides are equal by 1.34 and parallel by 11.9; consequently their joining faces are parallelograms by 1.33. The opposite face-planes are parallel by 11.15. We have therefore completed P and Q to parallelepipeds S and T respectively.

**Step 3.** Regard ABB′A′ as the base of S. Its opposite face CDD′C′ is parallel to that base and contains CC′, so S has the same height h as P. Regard EFGH as the base of T. Its base and opposite face lie in the same planes as the two triangular faces of Q, so T also has height h. Thus S and T have equal heights. (11.15; D6.4; hypothesis.)

**Step 4.** The diagonal EG bisects parallelogram EFGH; hence EFGH is double triangle EFG. But ABB′A′ is also double that triangle by hypothesis. Therefore the bases ABB′A′ and EFGH are equal. (1.34; CN1.)

**Step 5.** Consequently S and T are equal, since they are parallelepipeds on equal bases and of equal height. This is the direct comparison: equality of bases has already been obtained, so no general solid-ratio theorem is needed. (11.31.)

**Step 6.** The plane through AC and A′C′ passes through diagonals of opposite faces of S and separates P from the added prism. It therefore bisects S, so S is double P. Similarly, the plane through EG and E′G′ bisects T and separates Q from the added prism, so T is double Q. (11.28.)

**Step 7.** Since S is double P and T is double Q, S:P = T:Q: indeed, for arbitrary positive integers m and n, comparing mS with nP compares 2m copies of P with n copies, and comparing mT with nQ gives exactly the same comparison. (D5.5.) Since S = T by Step 5, the same magnitude has the same ratio to P and Q. Therefore P = Q. Thus the two prisms are equal. (5.9.)

**USED:** 1.31, 1.33, 1.34, 11.15, 11.28, 11.31, 11.9, 5.9, CN1, D11.13, D5.5, D6.4, P1
**Human refs (from References field):** 1.34, 11.28, 11.31
**Jaccard:** 0.231 — AI adds ['1.31', '1.33', '11.15', '11.9', '5.9', 'CN1', 'D11.13', 'D5.5', 'D6.4', 'P1']
