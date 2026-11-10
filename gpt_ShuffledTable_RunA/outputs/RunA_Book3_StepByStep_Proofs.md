# Book 3 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 3.1
**Statement:** To find the centre of a given circle.

**Step 1.** Choose two distinct points A and B on the given circumference and join AB. Bisect AB at D, and draw through D the straight line ℓ perpendicular to AB. We use the perpendicular-bisector route: the equality of three corresponding sides will allow I.8 to locate the centre on ℓ. [P1, 1.10, 1.11]

**Step 2.** Let O denote a centre whose existence is part of the definition of the given circle; its position is not assumed known. Then OA = OB. If O lies on AB, it must be D: outside the segment AB one of OA and OB properly contains the other, while within AB any point other than its midpoint has unequal distances from A and B. Thus, in this case, O already lies on ℓ. [D1.15, D1.16, CN5]

**Step 3.** Suppose instead that O does not lie on AB. Join OA, OB and OD. In triangles ADO and BDO, AD = DB, DO is common, and OA = OB. Hence ∠ADO = ∠BDO by I.8. These are adjacent angles on the straight line AB, so both are right angles. Consequently DO lies along ℓ: otherwise, taking the ray of ℓ on the same side of AB as O, one of the angles made by that ray and DO with DA would properly contain the other. Both angles are right and therefore equal, contradicting that the whole is greater than the part. Thus O lies on ℓ in every case. [P1, 1.8, D1.10, P4, CN5]

**Step 4.** Produce ℓ in both directions to meet the circumference at C and E. Since ℓ passes through the interior point O, these intersections lie on opposite sides of O. By the definition of the circle, OC = OE. Bisect CE at F. This completes the construction, using only the given circumference, the chord AB and its perpendicular bisector. [P2, D1.15, D1.16, 1.10]

**Step 5.** We have CF = FE and OC = OE, with both F and O between C and E. They cannot be distinct. Indeed, if their order were C, F, O, E, then OC > CF = FE > OE, contradicting OC = OE. If their order were C, O, F, E, then CF > OC = OE > FE, contradicting CF = FE. Therefore F = O. Hence the constructed point F is the centre of the given circle, as required. [CN5]

**USED:** 1.10, 1.11, 1.8, CN5, D1.10, D1.15, D1.16, P1, P2, P4
**Human refs (from References field):** 1.8, D1.10
**Jaccard:** 0.200 — AI adds ['1.10', '1.11', 'CN5', 'D1.15', 'D1.16', 'P1', 'P2', 'P4']

## Proposition 3.2
**Statement:** If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

**Step 1.** Let A and B be distinct points on the circumference, and join AB. Let O be the centre, and join OA and OB. By the definition of a circle, O lies inside it and OA = OB. [P1, D1.15, D1.16]

**Step 2.** First consider the case in which O lies on the straight line AB. Since OA = OB, O must lie between A and B; otherwise one of these equal segments would properly contain the other, contrary to the whole being greater than the part. Every point C strictly between A and B, other than O itself, therefore lies on one of the radius segments and satisfies OC < OA. [D1.15, CN5]

**Step 3.** Now suppose O does not lie on AB. Take any point C strictly between A and B, and join OC. Since OA = OB, the base angles of triangle OAB are equal: ∠OAB = ∠OBA. [P1, 1.5]

**Step 4.** In triangle OCB, produce BC through C to A. The exterior angle ∠OCA is greater than the opposite interior angle ∠OBC. Because C lies between A and B, ∠OBC = ∠OBA and ∠OAC = ∠OAB. Hence, using the equal base angles, ∠OCA > ∠OAC. [1.16, 1.5]

**Step 5.** In triangle OAC, the side opposite ∠OCA is OA, and the side opposite ∠OAC is OC. Therefore OA > OC. This is the direct angle-to-side route: Proposition 1.19 applies immediately to the angle comparison just obtained. [1.19]

**Step 6.** Thus, in either case, every point C strictly between A and B, other than O, satisfies OC < OA. Extend the ray from O through C to its first meeting D with the circumference. By the definition of a circle, OD = OA, so OC < OD. Consequently C lies before that first boundary point and is inside the circle. If C = O, it is inside by the same definition. Therefore every point of the joining segment AB except its endpoints lies within the circle, as required. [P2, D1.15]

**USED:** 1.16, 1.19, 1.5, CN5, D1.15, D1.16, P1, P2
**Human refs (from References field):** 1.16, 1.19, 1.5, 3.1
**Jaccard:** 0.333 — AI adds ['CN5', 'D1.15', 'D1.16', 'P1', 'P2']; Human adds ['3.1']

## Proposition 3.3
**Statement:** If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

**Step 1.** Let AB be a chord of a circle with centre O, and let a straight line through O meet AB at D. Suppose AB does not pass through O, so O and D are distinct. Join OA and OB [P1]. Since they are radii of the same circle, OA = OB [D1.15].

**Step 2.** First suppose that AD = DB. Use the three-side comparison directly, since the assumed bisection supplies the required equality of sides. In triangles ADO and BDO, AD = BD, DO is common, and AO = BO. Therefore ∠ADO = ∠BDO [1.8].

**Step 3.** These are adjacent angles on the straight line AB. Since they are equal, each is a right angle, and OD is perpendicular to AB [D1.10]. Thus the straight line through the centre that bisects AB also cuts it at right angles.

**Step 4.** Conversely, suppose the straight line through O cuts AB at right angles. Then ∠ADO and ∠BDO are right angles [D1.10], and hence are equal [P4]. For this direction, use the isosceles base angles to obtain a second equal angle-pair: since OA = OB, ∠OAB = ∠OBA [1.5]. As D lies between A and B, these are respectively ∠OAD and ∠OBD.

**Step 5.** The triangles ADO and BDO therefore have equal angles at A and B respectively, equal angles at D, and the equal sides AO and BO opposite their equal angles at D. The angle–angle–side case gives AD = BD [1.26]. Thus the straight line through the centre that cuts AB at right angles also bisects it. Both assertions are proved.

**USED:** 1.26, 1.5, 1.8, D1.10, D1.15, P1, P4
**Human refs (from References field):** 1.26, 1.5, 1.8, D1.10
**Jaccard:** 0.571 — AI adds ['D1.15', 'P1', 'P4']

## Proposition 3.4
**Statement:** If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.

**Step 1.** Let the distinct chords AB and CD intersect at E, neither passing through the centre. Suppose, for contradiction, that they bisect one another, so AE = EB and CE = ED. Find the centre O of the circle. Since neither chord passes through O, we have O ≠ E. [3.1]

**Step 2.** Join OE. Use the midpoint-to-perpendicular direction of 3.3, since E is the assumed midpoint of each chord: the straight line through O and E cuts both AB and CD at right angles. [P1, 3.3]

**Step 3.** Label the endpoints so that A and C lie on the same side of the straight line OE. The rays EA and EC are distinct. Interchanging the names of the chords if necessary, EC lies inside angle OEA. Thus angle OEC is a proper part of angle OEA, and consequently angle OEA is greater than angle OEC. [CN5]

**Step 4.** But both angle OEA and angle OEC are right angles by Step 2, and all right angles are equal. This contradicts the strict inequality in Step 3. Therefore the two intersecting straight lines, neither passing through the centre, do not bisect one another. [3.3, P4, CN5]

**USED:** 3.1, 3.3, CN5, P1, P4
**Human refs (from References field):** 3.1, 3.3
**Jaccard:** 0.400 — AI adds ['CN5', 'P1', 'P4']

## Proposition 3.5
**Statement:** If two circles cut one another, they will not have the same centre.

**Step 1.** Let two circles cut one another at A, and suppose, for a contradiction, that they have the same centre O. We use the defining equality of radii directly, rather than a chord theorem. The point O lies inside each circle. [D1.15, D1.16]

**Step 2.** Since the circles cut one another, choose a point B on the circumference of the first circle strictly inside the second. Draw OA and OB, and produce OB until it meets the circumference of the second circle at C beyond B. Thus B lies strictly between O and C. [P1, P2]

**Step 3.** Since A and B lie on the first circle and O is its centre, OA = OB. Since A and C lie on the second circle and O is also its centre, OA = OC. Consequently OB = OC. [D1.15, D1.16, CN1]

**Step 4.** But OB is a proper part of OC, so OC is greater than OB, contradicting their equality. Therefore the two circles cannot have the same centre. [CN5]

**USED:** CN1, CN5, D1.15, D1.16, P1, P2
**Human refs (from References field):** D1.15
**Jaccard:** 0.167 — AI adds ['CN1', 'CN5', 'D1.16', 'P1', 'P2']

## Proposition 3.6
**Statement:** If two circles touch one another, they will not have the same centre.

**Step 1.** Let two distinct circles touch at A, so that A belongs to both circumferences (D3.3). Suppose, for a contradiction, that they have the same centre O. Then O lies inside both circles (D1.15, D1.16). We compare radii directly; no separate treatment of internal and external touching is needed.

**Step 2.** Since the circumferences are distinct, choose a point on one which is not on the other. Draw the straight line from O through this point and produce it as necessary to meet the other circumference. Because O is inside both circles, the two intersections lie on the same ray from O. Denote the nearer intersection by B and the farther by C, so that O, B, C occur in that order. Also join OA (P1, P2, D1.15, D1.16).

**Step 3.** In the circle through B, OA and OB are radii, so OA = OB. In the circle through C, OA and OC are radii, so OA = OC (D1.15, D1.16). Therefore OB = OC, since things equal to the same thing are equal to one another (CN1).

**Step 4.** But OB is a proper part of OC, so OC is greater than OB (CN5). This contradicts Step 3. Therefore two circles which touch one another cannot have the same centre.

**USED:** CN1, CN5, D1.15, D1.16, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN1', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1', 'P2']

## Proposition 3.7
**Statement:** If on the diameter of a circle a point be taken which is not the centre of the circle, and from the point straight lines fall upon the circle, that will be greatest on which the centre is, the remainder of the same diameter will be least, and of the rest  the nearer to the straight line through the centre is always greater than the more remote, and only two equal straight lines will fall from the point on the circle, one on each side of the least straight line.

**Step 1.** Let AB be the diameter, O the centre, and P the given point, distinct from O. Name the endpoints so that their order is A, O, P, B. Thus PA passes through the centre and PB is the remainder of the diameter. The diameter divides the circle into two semicircles, and all radii are equal. Join the points required below. [D1.15, D1.16, D1.17, D1.18, P1]

**Step 2.** We use the triangle inequality directly for the greatest and least lines. Let X be any point of the circumference other than A or B. In triangle POX,
PX < PO + OX = PO + OA = PA.
Thus PA exceeds every line not lying on the diameter. Moreover, OA = OB = OP + PB, so PA = PO + OP + PB > PB. Consequently PA is the greatest of all the lines. [1.20, D1.15, CN2, CN5]

**Step 3.** In the same triangle,
PO + PX > OX = OB = OP + PB.
Subtracting the common length OP gives PX > PB. Together with PA > PB, this proves that PB is the least of all the lines. [1.20, D1.15, CN3, CN5]

**Step 4.** Take X and Y in the same semicircle, in the order A, X, Y, B along its circumference; thus PX is nearer to PA than PY is. The ray OY lies within angle POX, so angle POX is greater than angle POY. Triangles POX and POY have OP common and OX = OY. The included-angle comparison is therefore the direct applicable result: by I.24, PX > PY. Hence, on either side of the diameter, the nearer line to PA is always greater than the more remote. [CN5, D1.15, 1.24]

**Step 5.** For any X off the diameter, construct at O, on the opposite side of AB, a ray OY such that angle POY equals angle POX, and produce it to meet the circumference at Y. This choice of construction makes the included angles equal. Since OP is common and OX = OY, triangles POX and POY are congruent by I.4. Therefore PX = PY, and angle OPX equals angle OPY. Since PO has the direction of PA, these equal lines also have equal inclinations to PA, on opposite sides of the diameter. [1.23, P2, D1.15, 1.4]

**Step 6.** The comparison also holds for lines on opposite sides of the diameter. Replace one of them by its equal mate from Step 5 on the side of the other. This preserves both its length and its inclination to PA, so the comparison in Step 4 applies. Thus, wherever the two lines lie, the one nearer to the line through the centre is greater than the more remote. [1.4, 1.24]

**Step 7.** No two distinct lines ending in the same open semicircle can be equal, by Step 4. Neither PA nor PB equals any other line, by Steps 2 and 3. But every line not on the diameter has an equal mate in the opposite semicircle by Step 5. Hence each such line has exactly one equal mate, and no three of the lines can be equal. The equal pair lies one on each side of PB, the least line. Therefore the line through the centre is greatest, the remainder of the diameter is least, the nearer of the other lines is greater than the more remote, and equal lines occur only in pairs, one on each side of the least line. [1.20, 1.24, 1.4]

**USED:** 1.20, 1.23, 1.24, 1.4, CN2, CN3, CN5, D1.15, D1.16, D1.17, D1.18, P1, P2
**Human refs (from References field):** 1.20, 1.23, 1.24, 1.4
**Jaccard:** 0.308 — AI adds ['CN2', 'CN3', 'CN5', 'D1.15', 'D1.16', 'D1.17', 'D1.18', 'P1', 'P2']

## Proposition 3.8
**Statement:** If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest   the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

**Step 1.** Find the centre O of the circle, and draw and produce PO, where P is the given exterior point. Let this line meet the circle first at B and then at A; thus P, B, O, A occur in that order. All radii drawn below are equal. For any secant from P, call its first intersection the near, or convex, intersection, and its second the far, or concave, intersection. We shall compare the extreme lengths by the triangle inequality, far intersections by included angles, and near intersections by an interior broken-line comparison. [3.1, P1, P2, D1.17, D1.15]

**Step 2.** Let Q be any point of the circle other than A or B, and join OQ. In triangle POQ, the triangle inequality gives
PQ < PO + OQ = PO + OA = PA.
It also gives
PO < PQ + OQ.
Since PO = PB + BO and OQ = BO, cancellation gives PB < PQ. Consequently PA is greater than every other line from P to the circle, and PB is less than every other such line. [P1, 1.20, D1.15, CN3, CN5]

**Step 3.** Consider two secants on the same side of PO, meeting the circle in the orders P, X, U and P, Y, V, respectively. Suppose the first is nearer to PO, so that ∠OPU < ∠OPV. Join OU and OV.

The ray PU lies inside ∠OPV and therefore meets the opposite side OV of triangle POV at an interior point T. This point is inside the circle: it lies in the interior of the diameter through V, and a chord lies within the circle. Hence the far intersection U lies beyond T on the ray PU. It follows that OU lies beyond OV, away from OP, and therefore ∠POU > ∠POV.

Triangles POU and POV have PO common and OU = OV. Their included angles are now ordered, so the direct included-angle comparison gives PU > PV. Thus, among the far intersections on either side, the line nearer to the central line is greater. [P1, P2, D1.17, 3.2, CN5, D1.15, 1.24]

**Step 4.** For the same two secants, join OX and OY. The ray PX lies inside ∠OPY and meets OY at an interior point S. As in Step 3, S is inside the circle. Therefore the first intersection X lies between P and S, and hence strictly inside triangle POY.

Apply the interior broken-line comparison directly to triangle POY, taking PO as its base and X as its interior point. It gives
PX + XO < PY + YO.
Since XO = YO, cancellation yields PX < PY. Thus, among the near intersections on either side, the line nearer to PB is less. [P1, P2, D1.17, 3.2, 1.21, D1.15, CN3, CN5]

**Step 5.** Let Q be any point of the circle off the diameter AB. At O, on the opposite side of OP, construct a ray OR such that ∠POR = ∠POQ, and extend it to meet the circle at R. Since OP is common, OQ = OR, and the included angles are equal, the triangles POQ and POR are congruent. Therefore PQ = PR, and also ∠OPQ = ∠OPR. Thus an equal line exists on the opposite side of PB. [1.23, P2, D1.15, 1.4]

Applying this construction to both intersections of a secant places their counterparts on the same opposite ray, because the corresponding angles at P are equal. Their distances from P, and hence their order, are preserved. Thus the construction preserves both inclination to PO and the near/far designation. Consequently the comparisons in Steps 3 and 4 also hold when the two lines being compared lie on opposite sides of PO. [1.4, CN5]

**Step 6.** There cannot be two distinct equal lines from P whose endpoints Q and R lie on the same side of AB. Indeed, their central rays OQ and OR must be distinct: otherwise the equality of their radii would contradict the whole being greater than its part. Hence one of ∠POQ and ∠POR is greater than the other. Since OP is common and OQ = OR, the included-angle comparison makes one of PQ and PR strictly greater than the other. [D1.15, CN5, 1.24]

Every non-diametral line therefore has exactly one equal counterpart, on the opposite side of PB, and no third equal line is possible. The diametral lines PA and PB have no equal counterparts, by Step 2. Together with Steps 2–5, this proves that the central line is greatest on the concave circumference, that nearer lines there are greater, that PB is least on the convex circumference, that nearer lines there are less, and that equal lines occur only in pairs, one on each side of the least. ∎

**USED:** 1.20, 1.21, 1.23, 1.24, 1.4, 3.1, 3.2, CN3, CN5, D1.15, D1.17, P1, P2
**Human refs (from References field):** 1.20, 1.21, 1.24, 1.4, 3.1
**Jaccard:** 0.385 — AI adds ['1.23', '3.2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'P1', 'P2']

## Proposition 3.9
**Statement:** If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

**Step 1.** Let P be the given point within the circle, from which more than two distinct equal straight lines fall upon the circumference. Find the centre O of the circle. Suppose, for a contradiction, that P is not O. [3.1]

**Step 2.** Join O to P and produce this straight line in both directions to meet the circumference at A and B. Since AB passes through the centre and terminates at the circumference in both directions, AB is a diameter, and P lies on it. [P1, P2, D1.17]

**Step 3.** Apply III.7 directly: it is the natural route because it already limits the number of equal straight lines from a noncentral point on a diameter to the circumference. Since P is on the diameter AB and is assumed not to be the centre, no more than two such straight lines can be equal. This contradicts the hypothesis. Therefore P is O, and the point taken is the centre of the circle. [3.7]

**USED:** 3.1, 3.7, D1.17, P1, P2
**Human refs (from References field):** 1.8, 3.1, D1.10
**Jaccard:** 0.143 — AI adds ['3.7', 'D1.17', 'P1', 'P2']; Human adds ['1.8', 'D1.10']

## Proposition 3.10
**Statement:** A circle does not cut a circle at more points than two.

**Step 1.** Suppose two circles cut one another at three distinct points A, B, C. Join AB, BC, and AC. These points are not collinear: otherwise one would lie between the other two, whereas the interior of a chord lies within the circle, not on its circumference. We use bisected common chords, since III.3 directly relates their midpoints to the centres. [P1, 3.2]

**Step 2.** Find the centres O and P of the two circles. Since the circles cut one another, O and P are distinct. Draw the straight line OP and produce it as necessary; call this line ℓ. [3.1, 3.5, P1, P2]

**Step 3.** Bisect AB at D and BC at E. Each centre is equidistant from the endpoints of either chord. Consequently, if a centre lies on the supporting line of a chord, it must be that chord’s midpoint: any other point on that line has unequal distances from the endpoints. Thus each centre is either D or off the line AB, and either E or off the line BC. [1.10, D1.15, CN5]

**Step 4.** Join D to each centre different from D. Each resulting line passes through a centre and bisects the chord AB, which does not pass through that centre; hence it is perpendicular to AB. There is only one perpendicular line to AB through D: two distinct such lines would give, on the same side of AB, right angles one of which is a proper part of the other, contrary to the equality of right angles. Therefore both O and P lie on that perpendicular. Since O and P are distinct, ℓ passes through D and is perpendicular to AB. [P1, 3.3, D1.10, P4, CN5]

**Step 5.** Apply the same argument to the common chord BC and its midpoint E. Both centres lie on the perpendicular to BC through E. Hence ℓ also passes through E and is perpendicular to BC. [P1, 3.3, D1.10, P4, CN5]

**Step 6.** Because A, B, C are not collinear, B, D, E form a triangle. Its side DE lies on ℓ, so both ∠BDE and ∠BED are right angles. But any two angles of a triangle are together less than two right angles, a contradiction. Therefore a circle does not cut a circle at more points than two. [D1.10, 1.17]

**USED:** 1.10, 1.17, 3.1, 3.2, 3.3, 3.5, CN5, D1.10, D1.15, P1, P2, P4
**Human refs (from References field):** 3.1, 3.5
**Jaccard:** 0.167 — AI adds ['1.10', '1.17', '3.2', '3.3', 'CN5', 'D1.10', 'D1.15', 'P1', 'P2', 'P4']

## Proposition 3.11
**Statement:** If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.

**Step 1.** Let the inner circle touch the outer circle at A, and let their centres be I and O respectively. Thus A belongs to both circumferences, and the inner circle lies within the outer circle. The centres O and I are distinct, since touching circles cannot have the same centre. [D3.3, 3.6]

**Step 2.** Join OI and produce it beyond I. Since each centre lies inside its circle, this ray meets the inner circumference at D beyond I and the outer circumference at B beyond I. Internal containment implies that D lies between I and B, or coincides with B. Consequently OD ≤ OB: in the first case OD is a proper part of OB, and in the second they are equal. [P1, P2, D1.15, D1.16, CN5]

**Step 3.** Suppose that A does not lie on the straight line OI. Join OA and IA. Since A and B lie on the outer circumference, OA = OB; since A and D lie on the inner circumference, IA = ID. [P1, D1.15]

**Step 4.** Use the triangle inequality directly, since it compares the distance between the centres together with the inner radius against the outer radius. In triangle OIA,
OI + IA > OA.
Substituting the equal radii from Step 3 gives
OI + ID > OB.
But O, I, D lie in that order on a straight line, so OI + ID = OD. Hence OD > OB, contrary to Step 2. Therefore A lies on the straight line joining O and I, produced if necessary. Thus the line joining the centres falls on the point of contact, as required. [1.20, CN2]

**USED:** 1.20, 3.6, CN2, CN5, D1.15, D1.16, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.20', '3.6', 'CN2', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1', 'P2']

## Proposition 3.12
**Statement:** If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

**Step 1.** Let the circles have centres O and P and touch externally at A. Draw OP, OA, and PA (P1). Suppose that A does not lie on the straight line OP. Then OAP is a triangle; the natural direct comparison is the triangle inequality of 1.20.

**Step 2.** Let OP leave the circle with centre O at X and enter the circle with centre P at Y. Since the contact is external, the interiors of the circles are disjoint. Consequently the points occur in the order O, X, Y, P, allowing X and Y to coincide. Thus OX + YP ≤ OP: there is equality if X = Y, and otherwise OP additionally contains the positive intervening segment XY (external-contact hypothesis; D3.3; CN5).

**Step 3.** Since OA and OX are radii of the first circle, and PA and PY are radii of the second, OA = OX and PA = PY (D1.15, D1.16). Adding equals gives OA + PA = OX + YP, so OA + PA ≤ OP (CN2; Step 2).

**Step 4.** But in triangle OAP, the two sides OA and PA together are greater than OP (1.20), contradicting Step 3. Therefore A lies on the straight line OP. Moreover, A lies between the centres: otherwise the radial segments OA and PA would have a common nonzero portion immediately next to A lying inside both circles, contrary to external contact (D1.15; D3.3; the hypothesis). Hence the straight line joining the centres passes through the point of contact.

**USED:** 1.20, CN2, CN5, D1.15, D1.16, D3.3, P1
**Human refs (from References field):** 1.20
**Jaccard:** 0.143 — AI adds ['CN2', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1']

## Proposition 3.13
**Statement:** A circle does not touch a circle at more points than one, whether it touch it internally or externally.

**Step 1.** Suppose that two circles touch one another at two distinct points A and B. Find their centres O and P. Since touching circles do not have the same centre, O and P are distinct. [3.1, 3.6]

**Step 2.** Use the line of centres, since the preceding contact results apply directly to each alleged contact. If the circles touch internally, the line OP, produced, passes through A and also through B. If they touch externally, the line OP likewise passes through A and B. Thus, in either case, A, B, O, and P lie on one straight line. [3.11, 3.12]

**Step 3.** By the definition of a circle and its centre, OA = OB and PA = PB. Each centre must lie strictly between A and B: it is not on its own circumference, and if it lay outside the segment AB, one of its straight lines to A and B would contain the other as a proper part, contradicting their equality. [D1.15, D1.16, CN5]

**Step 4.** Since the centres are distinct and both lie between A and B, interchange their names if necessary so that their order is A, O, P, B. Then AO < AP and PB < OB, because a whole is greater than its proper part. But AO = OB and AP = PB, so substitution gives AO < AP = PB < OB = AO, an impossibility. Therefore two circles cannot touch at two distinct points, and hence cannot touch at more than one point, whether internally or externally. [CN5, D1.15, CN1]

**USED:** 3.1, 3.11, 3.12, 3.6, CN1, CN5, D1.15, D1.16
**Human refs (from References field):** 3.11, 3.2, D3.3
**Jaccard:** 0.100 — AI adds ['3.1', '3.12', '3.6', 'CN1', 'CN5', 'D1.15', 'D1.16']; Human adds ['3.2', 'D3.3']

## Proposition 3.14
**Statement:** In a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another.

**Step 1.** Let AB and CD be chords of a circle with centre O. Join OA and OC. These radii are equal: OA = OC. We first consider chords neither of which passes through O. [P1, D1.15]

**Step 2.** Draw OE perpendicular to AB and OF perpendicular to CD. By 3.3, these perpendiculars bisect the chords, so AE = EB and CF = FD. This is the direct route: the perpendiculars defining distance from the centre are also bisectors, after which 1.47 compares the resulting right triangles in both directions. [1.12, 3.3, D3.4]

**Step 3.** Applying 1.47 to the right triangles OEA and OFC gives
OA² = OE² + AE²,
OC² = OF² + CF².
Since OA = OC, it follows that
OE² + AE² = OF² + CF².
Here X² denotes the square on the straight line X. [1.47, D1.15, CN1]

**Step 4.** Suppose AB = CD. Their halves are therefore equal, so AE = CF. Subtracting the equal squares on these halves from the equality in Step 3 gives OE² = OF², and hence OE = OF. The perpendiculars from the centre to the chords are thus equal; consequently AB and CD are equally distant from the centre. [3.3, CN2, CN3, D3.4]

**Step 5.** Conversely, suppose AB and CD are equally distant from O. By definition, OE = OF. Subtracting their equal squares from the equality in Step 3 gives AE² = CF², and hence AE = CF. Since AE = EB and CF = FD, adding these equal halves gives AB = CD. [D3.4, CN3, 3.3, CN2]

**Step 6.** For completeness, a chord through O is a diameter and has distance zero from O. All diameters are equal, each consisting of two radii. Every chord XY not through O has positive distance from O and is shorter than a diameter: in triangle XOY, 1.20 gives XY < OX + OY, the latter being the length of a diameter. Thus a diameter can neither equal a non-diameter chord nor be equally distant from O with it, while two diameters satisfy both assertions. This covers the remaining cases. Therefore, in a circle equal straight lines are equally distant from the centre, and those equally distant from the centre are equal to one another. [D1.17, D1.15, CN2, 1.20, D3.4]

**USED:** 1.12, 1.20, 1.47, 3.3, CN1, CN2, CN3, D1.15, D1.17, D3.4, P1
**Human refs (from References field):** 1.47, 3.1, 3.3, D3.4
**Jaccard:** 0.250 — AI adds ['1.12', '1.20', 'CN1', 'CN2', 'CN3', 'D1.15', 'D1.17', 'P1']; Human adds ['3.1']

## Proposition 3.15
**Statement:** Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

**Step 1.** Let O be the centre of the circle, UV a diameter, and AB any chord not passing through O. Join OA and OB (P1). The radii OA, OB, OU, and OV are equal (D1.15), and UV = OU + OV (D1.17). Hence OA + OB = UV (CN2). But in triangle AOB, OA + OB > AB (1.20). Therefore UV > AB. Every diameter consists of two equal radii, so all diameters are equal and are greater than every non-diametral chord.

**Step 2.** Now let AB and CD be non-diametral chords, with AB nearer the centre than CD. Bisect AB at M and CD at N (1.10), and join OM, ON, and OC (P1). By 3.3, OM and ON are perpendicular to their respective chords. Thus OM < ON by D3.5. Choosing the midpoints first gives both the perpendicular distances and the half-chords directly.

**Step 3.** Write S(XY) for the area of the square on XY. Apply 1.47 to the right triangles OMA and ONC; this is the direct comparison because their hypotenuses are equal radii. We obtain
S(OM) + S(AM) = S(OA),
S(ON) + S(CN) = S(OC).
Since OA = OC (D1.15), these give
S(OM) + S(AM) = S(ON) + S(CN) (CN1).

**Step 4.** Since OM < ON, cut off OT = OM on ON, with T between O and N (1.3). By 2.4, the square on ON equals the square on OT together with the square on TN and twice the rectangle contained by OT and TN. Consequently S(ON) equals S(OM) together with a positive remainder, say R (CN5).

**Step 5.** Substitute this expression for S(ON) into the equality in Step 3 and subtract the common square S(OM) (CN3). Then
S(AM) = S(CN) + R.
Therefore S(AM) > S(CN) (CN5).

**Step 6.** Hence AM > CN. Indeed, equal segments have equal squares; and if AM were shorter than CN, cutting off a segment equal to AM on CN and applying 2.4 would make S(CN) greater than S(AM), contrary to Step 5 (1.3, 2.4, CN5). Since AB is twice AM and CD is twice CN, AB > CD (CN2, CN5).

Thus the diameter is greatest among straight lines in the circle, and, among the remaining chords, the nearer to the centre is always greater than the more remote.

**USED:** 1.10, 1.20, 1.3, 1.47, 2.4, 3.3, CN1, CN2, CN3, CN5, D1.15, D1.17, D3.5, P1
**Human refs (from References field):** 1.20, 1.24, 3.14, D3.5
**Jaccard:** 0.125 — AI adds ['1.10', '1.3', '1.47', '2.4', '3.3', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'P1']; Human adds ['1.24', '3.14']

## Proposition 3.16
**Statement:** The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

**Step 1.** Let AB be a diameter of the circle, O its centre, and ℓ the straight line through A perpendicular to AB. Choose one semicircle, and let AT be the ray of ℓ on its side of AB. Denote by S the angle between AB and this semicircle’s circumference at A, and by R the remaining angle between that circumference and AT. Thus S and R occupy the right angle OAT. [D1.17, D1.18, D1.10, D3.7]

**Step 2.** Take any point X of ℓ other than A, and join OX. In triangle OAX, the angle OAX is right. Therefore the angle OXA is less than a right angle, since two angles of a triangle are together less than two right angles. Consequently OX > OA, the greater angle being opposite the greater side. Since OA is a radius, X is outside the circle. This applies on both sides of A; hence ℓ, except for A itself, falls outside the circle. The direct route here is the right-triangle comparison: perpendicularity supplies the needed angle immediately. [P1, D1.10, 1.17, 1.19, D1.15]

**Step 3.** Now let AU be any ray strictly inside the right angle OAT. Draw OH perpendicular to the straight line containing AU. The foot H lies on the forward ray AU: it cannot equal A, since OAU is acute; and if it lay on the opposite ray, angle OAH would be greater than a right angle, while OHA would be right, contradicting the triangle-angle inequality. In the right triangle OAH, angle OAH is acute and OHA is right. Hence OA > OH. Thus H lies inside the circle. [1.12, D1.12, 1.13, 1.17, 1.19, D1.15]

**Step 4.** Produce AH beyond the interior point H until it meets the circumference again at K. Since A and K are on the circumference, the chord AK, apart from its endpoints, lies within the circle. Thus every ray strictly inside angle OAT enters the circle immediately after A. A straight line interposed between AT and the circumference would have to issue from A inside this right angle while remaining outside the circle, which is impossible. Therefore no straight line can be interposed between ℓ and the circumference at A. [P2, D1.15, 3.2; Steps 2–3]

**Step 5.** Let α be any acute rectilineal angle. At A, on AO and toward AT, construct a rectilineal angle OAU equal to α. Because α is less than a right angle, AU lies strictly inside angle OAT. By Step 4, AU lies inside the semicircle near A. Consequently angle OAU is a proper part of the angle S of the semicircle, so S > α. Thus the angle of the semicircle is greater than every acute rectilineal angle. [1.23, D1.12, P4, CN5; Step 4]

**Step 6.** Again, on AT and toward AO, construct an angle TAV equal to the same arbitrary acute angle α. The ray AV lies strictly inside angle OAT and, by Step 4, enters the circle immediately after A. Therefore the remaining angle R, between AT and the circumference, is a proper part of angle TAV. Hence R < α. Since α was arbitrary, the remaining angle is less than every acute rectilineal angle. Together with Steps 2 and 4, this proves all the assertions. [1.23, D1.12, P4, CN5; Steps 2, 4]

**USED:** 1.12, 1.13, 1.17, 1.19, 1.23, 3.2, CN5, D1.10, D1.12, D1.15, D1.17, D1.18, D3.7, P1, P2, P4
**Human refs (from References field):** 1.17, 1.19, 1.5
**Jaccard:** 0.118 — AI adds ['1.12', '1.13', '1.23', '3.2', 'CN5', 'D1.10', 'D1.12', 'D1.15', 'D1.17', 'D1.18', 'D3.7', 'P1', 'P2', 'P4']; Human adds ['1.5']

## Proposition 3.17
**Statement:** From a given point to draw a straight line touching a given circle.

**Step 1.** Let C be the given circle and A the given point, first supposed outside C. Find the centre O of C, and join OA, meeting C at D, with D between O and A. (3.1, P1)

**Step 2.** Describe the auxiliary circle K with centre O and radius OA. At D draw a perpendicular to OA, and produce it to meet K at E. Choose this concentric-circle route because it allows the constructed right angle to be transferred directly by side–angle–side. (P3, 1.11, P2)

**Step 3.** Join OE, meeting C at B, and join AB. Since OA and OE are radii of K, OA = OE; since OB and OD are radii of C, OB = OD. Moreover, the angle AOB equals the angle EOD: OD lies along OA, and OB lies along OE. (P1, D1.15)

**Step 4.** Thus triangles AOB and EOD have two corresponding sides equal and their included angles equal. By side–angle–side, angle ABO equals angle EDO. The latter is right by construction; therefore AB is perpendicular to OB. (1.4, 1.11, D1.10)

**Step 5.** Produce BO through O to the other circumference of C, obtaining a diameter with extremity B. The straight line AB is perpendicular to this diameter at B, so it falls outside C. Since it meets C at B without cutting it, AB touches C. It also passes through the given point A, as required. (P2, D1.17, 3.16, D3.2)

**Step 6.** If A is itself on C, join OA and produce it through O to form a diameter. Draw the perpendicular to this diameter at A. By the same perpendicular-at-an-extremity result, this line lies outside C and therefore touches C at A. Hence the required tangent has been constructed in both admissible cases. A point strictly inside C is necessarily excluded: a straight line through it cuts the circle rather than merely touching it. (P1, P2, D1.17, 1.11, 3.16, D3.2)

**USED:** 1.11, 1.4, 3.1, 3.16, D1.10, D1.15, D1.17, D3.2, P1, P2, P3
**Human refs (from References field):** 1.4, 3.1, 3.16
**Jaccard:** 0.273 — AI adds ['1.11', 'D1.10', 'D1.15', 'D1.17', 'D3.2', 'P1', 'P2', 'P3']

## Proposition 3.18
**Statement:** If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.

**Step 1.** Let the straight line ℓ touch a circle at A, and let O be its centre. The centre lies inside the circle, whereas a tangent does not pass through its interior; hence O is not on ℓ. We must prove that OA is perpendicular to ℓ. [D1.15, D1.16, D3.2]

**Step 2.** Suppose that OA is not perpendicular to ℓ. We proceed by comparing it with a perpendicular from O: draw OH perpendicular to ℓ, with H on ℓ. Then H differs from A, and angle OHA is right. [1.12, D1.10]

**Step 3.** In triangle OAH, angles OHA and OAH together are less than two right angles. Since OHA is right, OAH is less than a right angle and therefore less than OHA. The two-angle bound suffices here. The greater angle is subtended by the greater side, so OA > OH. [1.17, 1.19]

**Step 4.** Because H lies on the tangent, it cannot lie inside the circle. Thus the segment from the interior point O to H meets the circumference at a point E, either at H itself or between O and H. Since OA and OE are radii, OA = OE. If E = H, this gives OA = OH. If E lies between O and H, then OH > OE, since the whole is greater than the part, and consequently OH > OA. In either case, OA is not greater than OH. [D3.2, D1.15, CN5]

**Step 5.** This contradicts Step 3. Therefore OA is perpendicular to ℓ: the straight line joined from the centre to the point of contact is perpendicular to the tangent. [D1.10]

**USED:** 1.12, 1.17, 1.19, CN5, D1.10, D1.15, D1.16, D3.2
**Human refs (from References field):** 1.17, 1.19
**Jaccard:** 0.250 — AI adds ['1.12', 'CN5', 'D1.10', 'D1.15', 'D1.16', 'D3.2']

## Proposition 3.19
**Statement:** If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so drawn.

**Step 1.** Let the straight line AB touch the circle at T, let ℓ be the straight line drawn through T perpendicular to AB, and let O be the centre. Join OT. [P1]

**Step 2.** By 3.18, OT is perpendicular to AB. This is the direct route: the immediately preceding tangent–radius theorem supplies precisely the perpendicular needed. [3.18]

**Step 3.** Produce ℓ through T as necessary, and choose C on it on the side of AB opposite O. Choose B on the tangent, distinct from T. Since both OT and ℓ are perpendicular to AB, the adjacent angles OTB and BTC are each right angles; together they therefore equal two right angles. [P2, D1.10]

**Step 4.** The straight lines TO and TC lie on opposite sides of TB and make with it adjacent angles equal to two right angles. By 1.14, TO and TC are in a straight line with one another. Since TC lies on ℓ, the centre O lies on ℓ. Thus the centre lies on the straight line drawn at right angles to the tangent from the point of contact. [1.14]

**USED:** 1.14, 3.18, D1.10, P1, P2
**Human refs (from References field):** 3.18
**Jaccard:** 0.200 — AI adds ['1.14', 'D1.10', 'P1', 'P2']

## Proposition 3.20
**Statement:** In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.

**Step 1.** Let B and C be the endpoints of the common circumference, let A be the vertex on the circle, and let O be its centre. Write Θ for the angle at O standing on the arc BC which does not contain A. We must prove Θ = 2∠BAC; throughout, the central angle is taken over this specified arc, not the complementary arc. [D3.9]

**Step 2.** Join AB, AC, AO, BO, and CO, and produce AO beyond O to meet the circle again at D. Since O is the centre, OA = OB = OC. We distinguish whether D lies between B and C on the specified arc, coincides with an endpoint, or lies outside that arc. [P1, P2, D1.15, D1.16]

**Step 3.** Use the direct isosceles-triangle route: equal radii immediately supply the base-angle equality by I.5, and the exterior-angle theorem then supplies the doubling. Indeed, let X be either B or C, provided X ≠ D. In triangle AOX, OA = OX, so ∠OAX = ∠AXO. Since AO is produced to D, I.32 gives
∠XOD = ∠OAX + ∠AXO = 2∠OAX = 2∠XAD.
Thus each nondegenerate auxiliary central angle is double its corresponding angle at A. [1.5, 1.32, CN2]

**Step 4.** Suppose D lies strictly between B and C on the arc BC not containing A. Then AD divides ∠BAC, while OD divides the central angle over that same arc. Adding the two equalities from Step 3 gives
Θ = ∠BOD + ∠DOC
= 2∠BAD + 2∠DAC
= 2∠BAC.
The central sum is taken over the specified arc, including when that sum is a reflex angle. [D3.9, CN2]

**Step 5.** Suppose D coincides with an endpoint. If D = B, the equality in Step 3 for X = C gives
Θ = ∠COD = 2∠CAD = 2∠BAC.
If D = C, the equality for X = B gives the same conclusion. Thus the case in which AO lies along a side of the angle at A is also covered. [D3.9, 1.5, 1.32]

**Step 6.** Finally, suppose D lies outside the specified arc BC. Then B and C lie on the same side of the line AD. Interchanging B and C if necessary, their order is such that AC lies inside ∠BAD. Accordingly,
∠BAC = ∠BAD − ∠CAD,
and, taking the central angles over the corresponding arcs,
Θ = ∠BOD − ∠COD.
Subtracting the equalities from Step 3 therefore gives
Θ = 2∠BAD − 2∠CAD = 2∠BAC. [D3.9, CN3]

These cases exhaust the possible positions of D. Hence, in a circle, the angle at the centre is double the angle at the circumference when they have the same circumference as base.

**USED:** 1.32, 1.5, CN2, CN3, D1.15, D1.16, D3.9, P1, P2
**Human refs (from References field):** 1.32, 1.5
**Jaccard:** 0.222 — AI adds ['CN2', 'CN3', 'D1.15', 'D1.16', 'D3.9', 'P1', 'P2']

## Proposition 3.21
**Statement:** In a circle the angles in the same segment are equal to one another.

**Step 1.** Let AB be the chord bounding a segment of a circle, and let C and D be points on the circumference of that same segment. The angles in question are ∠ACB and ∠ADB. Both stand upon the same arc AB, namely the arc complementary to the circumference of their segment. [D3.6, D3.8, D3.9]

**Step 2.** Find the centre O of the circle and join OA and OB. Use the central-angle route: Proposition 3.20 directly compares both given angles with one common angle at the centre. [3.1, P1]

**Step 3.** Let Θ denote the angle at O corresponding to the common arc AB identified in Step 1, taking the central angle along that arc. Since Θ and ∠ACB have the same circumference as base, Θ is double ∠ACB. Likewise, Θ is double ∠ADB. Thus each of the two angles is half of Θ. [3.20]

**Step 4.** Since ∠ACB and ∠ADB are each equal to the same half of Θ, they are equal to one another. Therefore, in a circle, the angles in the same segment are equal to one another. [CN1]

**USED:** 3.1, 3.20, CN1, D3.6, D3.8, D3.9, P1
**Human refs (from References field):** 3.20
**Jaccard:** 0.143 — AI adds ['3.1', 'CN1', 'D3.6', 'D3.8', 'D3.9', 'P1']

## Proposition 3.22
**Statement:** The opposite angles of quadrilaterals in circles are equal to two right angles.

**Step 1.** Let ABCD be a quadrilateral inscribed in a circle, with its vertices in that order around the circumference. Join AC and BD. [P1] We use the same-segment route because these diagonals immediately furnish angles standing on the same chords.

**Step 2.** The angles BAC and BDC stand on chord BC in the same segment, and the angles CAD and CBD stand on chord CD in the same segment. Therefore
∠BAC = ∠BDC and ∠CAD = ∠CBD. [3.21]

**Step 3.** Since AC divides the interior angle BAD, adding the equalities gives
∠BAD = ∠BAC + ∠CAD = ∠BDC + ∠CBD.
Consequently,
∠BAD + ∠BCD = ∠BDC + ∠CBD + ∠BCD.
The latter sum comprises the three angles of triangle BCD and therefore equals two right angles. Thus ∠BAD + ∠BCD equals two right angles. [CN2, 1.32, CN1]

**Step 4.** Similarly, the angles ABD and ACD stand on chord AD in the same segment, while DBC and DAC stand on chord DC in the same segment. Hence ∠ABD = ∠ACD and ∠DBC = ∠DAC. [3.21] Since BD divides the interior angle ABC,
∠ABC + ∠CDA = ∠ABD + ∠DBC + ∠CDA = ∠ACD + ∠DAC + ∠CDA.
This is the sum of the three angles of triangle ACD, so it equals two right angles. [CN2, 1.32, CN1] Therefore each pair of opposite angles of a quadrilateral in a circle is together equal to two right angles.

**USED:** 1.32, 3.21, CN1, CN2, P1
**Human refs (from References field):** 1.32, 3.21
**Jaccard:** 0.400 — AI adds ['CN1', 'CN2', 'P1']

## Proposition 3.23
**Statement:** On the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.

**Step 1.** Suppose, contrary to the assertion, that two similar but unequal segments of circles are constructed on the same straight line AB and on the same side of it. Each segment is bounded by AB and an arc joining A to B. [D3.6]

**Step 2.** Their bounding circles are distinct, since the same circle and the same chord determine only one segment on a specified side. The circles already meet at A and B, so their arcs cannot cross elsewhere: otherwise the circles would cut at more than two points. Consequently one segment lies within the other; call them the inner and outer segments. [D3.6, 3.10]

**Step 3.** Choose a point D on the inner arc, other than A and B, lying inside the outer segment. Join AD and produce it until it meets the outer arc at C, so that A, D, C occur in that order. Join DB and CB. [P1, P2]

**Step 4.** The angles ADB and ACB are angles in the inner and outer segments respectively. Use the defining angle equality of similar segments directly: since the segments are similar, ∠ADB = ∠ACB. [D3.8, D3.11]

**Step 5.** In triangle DCB, the side CD is produced through D to A. Thus ∠ADB is an exterior angle and is greater than the opposite interior angle DCB. Since the rays CD and CA coincide, ∠DCB = ∠ACB. Hence ∠ADB > ∠ACB, contradicting Step 4. Therefore two similar and unequal segments of circles cannot be constructed on the same straight line and on the same side. [1.16, D3.11]

**USED:** 1.16, 3.10, D3.11, D3.6, D3.8, P1, P2
**Human refs (from References field):** 1.16, D3.11
**Jaccard:** 0.286 — AI adds ['3.10', 'D3.6', 'D3.8', 'P1', 'P2']

## Proposition 3.24
**Statement:** Similar segments of circles on equal straight lines are equal to one another.

**Step 1.** Let S and T be similar segments of circles on the equal straight lines AB and CD, respectively. By the definition of similar segments, the angles admitted by S and T are equal. [D3.11]

**Step 2.** Superpose T upon the plane of S, placing C at A and CD along AB, with the two segments on the same side of AB. Since CD equals AB, D falls on B. Denote the transported segment by T′. Superposition preserves its angles and magnitude: thus T′ remains similar to S, and T′ equals T. [D3.11, CN4]

**Step 3.** Now S and T′ are similar segments on the same straight line AB and on the same side. They cannot be unequal, because two similar and unequal segments cannot be constructed on the same straight line on the same side. Hence S equals T′. This is the direct same-base route supplied by III.23 after superposition. [3.23]

**Step 4.** Since S equals T′ and T equals T′, S equals T. Therefore similar segments of circles on equal straight lines are equal to one another. [CN1]

**USED:** 3.23, CN1, CN4, D3.11
**Human refs (from References field):** 3.10
**Jaccard:** 0.000 — AI adds ['3.23', 'CN1', 'CN4', 'D3.11']; Human adds ['3.10']

## Proposition 3.25
**Statement:** Given a segment of a circle, to describe the complete circle of which it is a segment.

**Step 1.** Let the given segment have straight boundary AB. Choose a point C on its circular boundary distinct from A and B. The points A, B, C are not collinear: otherwise one would lie between the other two, whereas the interior of the chord joining those two lies within the circle, not on its circumference. [D3.6, 3.2]

**Step 2.** Join AC. Bisect AB at M and AC at N. At M draw the straight line p perpendicular to AB, and at N draw the straight line q perpendicular to AC, producing these lines as necessary. We choose this route because two chord-bisectors locate the centre directly, without distinguishing different shapes of the given segment. [P1, 1.10, 1.11, P2]

**Step 3.** The lines p and q are distinct. For if they were the same line, MN would be perpendicular both to AM and to AN. The triangle AMN would then have two right angles, contrary to the fact that any two angles of a triangle are together less than two right angles. [1.17]

**Step 4.** For verification only, let O denote the centre of the circle of which the given figure is a segment; the construction does not assume that O is already known. Its radii OA, OB, OC are equal. If O lies on the straight line AB, equality of OA and OB forces O to be its midpoint M, so O lies on p. Indeed, an exterior position, or any position other than the midpoint, would make one of these distances greater than the other. [D3.6, D1.15, D1.16, CN5]

**Step 5.** If O does not lie on AB, join OM. Since this straight line passes through the centre and bisects the chord AB, it is perpendicular to AB. Thus OM lies on the constructed perpendicular p, and again O lies on p. Here III.3 applies directly because AB has already been bisected; the identification of the two perpendiculars follows from I.14. Applying the same argument to AC and its midpoint N shows that O also lies on q, including the case O = N. Consequently the two distinct constructed lines meet, and their intersection E is O. [P1, P2, 3.3, 1.14, D1.15, CN5]

**Step 6.** With centre E and distance EA describe a circle. Since E is the centre O of the original circle and EA is its radius, the circle described is precisely the complete circle to which the given segment belongs. Thus the required circle has been described. [P3, D1.15, D1.16]

**USED:** 1.10, 1.11, 1.14, 1.17, 3.2, 3.3, CN5, D1.15, D1.16, D3.6, P1, P2, P3
**Human refs (from References field):** 1.6, 3.9
**Jaccard:** 0.000 — AI adds ['1.10', '1.11', '1.14', '1.17', '3.2', '3.3', 'CN5', 'D1.15', 'D1.16', 'D3.6', 'P1', 'P2', 'P3']; Human adds ['1.6', '3.9']

## Proposition 3.26
**Statement:** In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

**Step 1.** Let the two equal circles have centres O and P, and let the circumferences to be compared be the arcs AB and CD. Draw the radii to their endpoints. The radii of the two circles are equal, so OA = PC and OB = PD. We take the direct route: first establish the centre case by superposition, then reduce the circumference case to it by doubling the given angles. [P1, D1.15, D3.1, D3.9]

**Step 2.** Suppose first that the central angles AOB and CPD standing on the specified arcs are equal. Superpose the first circle on the second, placing O on P and the ray OA along PC, with the equal angular openings corresponding. Since OA = PC, A coincides with C. Equality of the angles makes the ray OB coincide with PD; since OB = PD, B also coincides with D. Moreover, the entire circumferences coincide, because after this placement they have the same centre and radius. [D1.15, D3.1]

**Step 3.** Under this superposition, the specified arc AB coincides with the specified arc CD: their endpoints coincide, their circles coincide, and they belong to the corresponding angular openings, rather than to complementary openings. Things which coincide are equal. Thus equal angles at the centres stand on equal circumferences. [D3.9, CN4]

**Step 4.** Now suppose that equal angles AXB and CYD stand at the circumferences on the specified arcs AB and CD. By III.20, the central angle standing on AB is double angle AXB, and the central angle standing on CD is double angle CYD. Adding equals to equals gives equal doubles, so these central angles are equal. By Steps 2–3, their corresponding arcs AB and CD are therefore equal. Hence, in equal circles, equal angles stand on equal circumferences, whether the angles stand at the centres or at the circumferences. [3.20, CN2, D3.9, CN4]

**USED:** 3.20, CN2, CN4, D1.15, D3.1, D3.9, P1
**Human refs (from References field):** 1.4, 3.24, D3.11
**Jaccard:** 0.000 — AI adds ['3.20', 'CN2', 'CN4', 'D1.15', 'D3.1', 'D3.9', 'P1']; Human adds ['1.4', '3.24', 'D3.11']

## Proposition 3.27
**Statement:** In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.

**Step 1.** Let two equal circles have equal arcs AB and DE, and let angles AVB and DWE stand on these arcs. Take V and W either both at the centres or both on the respective complementary circumferences. Draw the sides of the angles as necessary (P1). We use the immediately preceding proposition, III.26, by a whole–part contradiction, since it applies directly to both kinds of angle (3.26).

**Step 2.** Suppose the angles are unequal. Interchanging the circles if necessary, let angle AVB be greater than angle DWE. At V, on VA and towards VB, construct an angle AVX equal to angle DWE (1.23). Since this angle is smaller than angle AVB, its second side lies strictly inside angle AVB. Produce that side to meet the circle at X (P2). Thus X lies strictly within the given arc AB, and arc AX is a proper part of arc AB. This holds whether V is the centre or lies on the complementary circumference.

**Step 3.** The equal angles AVX and DWE stand in equal circles, and their vertices are of the same kind. Therefore the arcs AX and DE on which they stand are equal (3.26). But arc DE equals arc AB by hypothesis. Hence arc AX equals arc AB (CN1).

**Step 4.** This is impossible: arc AX is a proper part of arc AB, and the whole is greater than the part (CN5). Consequently the original angles cannot be unequal. Therefore, in equal circles, angles standing on equal circumferences are equal to one another, whether both stand at the centres or both at the circumferences.

**USED:** 1.23, 3.26, CN1, CN5, P1, P2
**Human refs (from References field):** 1.23, 3.20, 3.26
**Jaccard:** 0.286 — AI adds ['CN1', 'CN5', 'P1', 'P2']; Human adds ['3.20']

## Proposition 3.28
**Statement:** In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

**Step 1.** Let AB and CD be equal chords in two equal circles. Find their centres O and P, and join OA, OB, PC, and PD. The corresponding radii are equal: OA = PC and OB = PD. (3.1, P1, D3.1)

**Step 2.** The complete circumferences of the two circles are equal. Indeed, when their centres are superposed, their equal radii make the circumferences coincide, since every point of either circumference is at the prescribed distance from its centre. Coincident magnitudes are equal. (D1.15, D3.1, CN4)

**Step 3.** First suppose neither chord is a diameter. In triangles AOB and CPD, the two corresponding sides are equal radii and the bases AB and CD are equal by hypothesis. Therefore ∠AOB = ∠CPD. We choose the central-angle route because the given chord equality completes precisely the three side equalities required here. (1.8)

**Step 4.** These equal, non-reflex central angles stand on the lesser circumferences cut off by AB and CD. In equal circles, equal angles at the centres stand on equal circumferences. Hence the lesser circumference cut off by AB equals the lesser circumference cut off by CD. (3.26)

**Step 5.** Subtract those equal lesser circumferences from the equal complete circumferences established in Step 2. The remainders, which are the greater circumferences cut off by the chords, are equal. Thus the greater equals the greater and the less equals the less. (CN3)

**Step 6.** For completeness, if either chord is a diameter, so is the other. A diameter consists of two radii, whereas a chord not passing through the centre is strictly shorter than the sum of its two endpoint radii, by the triangle inequality. Those sums are equal in the two equal circles, so equal chords cannot consist of one diameter and one non-diameter. Each diameter bisects its circle, and corresponding semicircumferences coincide when the equal circles and their diameters are superposed. Hence the cut-off circumferences are equal in this case also. Therefore, in equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less. (D1.17, 1.20, D3.1, CN2, CN4)

**USED:** 1.20, 1.8, 3.1, 3.26, CN2, CN3, CN4, D1.15, D1.17, D3.1, P1
**Human refs (from References field):** 1.8, 3.26
**Jaccard:** 0.182 — AI adds ['1.20', '3.1', 'CN2', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D3.1', 'P1']

## Proposition 3.29
**Statement:** In equal circles equal circumferences are subtended by equal straight lines.

**Step 1.** Let two equal circles have equal arcs AB and CD, subtended by the straight lines AB and CD. Find their centres O and P, and join OA, OB, PC, and PD, as well as the chords AB and CD. [3.1, P1]

**Step 2.** If the equal arcs are semicircles, their chords are diameters and therefore are equal, since the circles are equal. This gives the conclusion in that case. Otherwise, consider the triangles OAB and PCD. Their corresponding radii satisfy OA = PC and OB = PD. [D1.17, D3.1, D1.15]

**Step 3.** Since the circles are equal and the given arcs are equal, the angles AOB and CPD standing on those arcs at the centres are equal. We use the centre form of this proposition because it supplies directly the included angles of the two radius-triangles. [3.27]

**Step 4.** Thus triangles OAB and PCD have two sides respectively equal and the included angles equal. Their bases are consequently equal: AB = CD. Therefore, in equal circles, equal circumferences are subtended by equal straight lines. [1.4]

**USED:** 1.4, 3.1, 3.27, D1.15, D1.17, D3.1, P1
**Human refs (from References field):** 1.4, 3.27
**Jaccard:** 0.286 — AI adds ['3.1', 'D1.15', 'D1.17', 'D3.1', 'P1']

## Proposition 3.30
**Statement:** To bisect a given circumference.

**Step 1.** Let the given circumference be an arc with endpoints A and B. Join AB, and bisect the straight line AB at D. Thus AD = DB. [P1, 1.10]

**Step 2.** At D draw a perpendicular to AB, and produce it on the side of AB containing the given arc until it meets that arc at C. Join AC and BC. [1.11, P2, P1]

**Step 3.** In triangles ADC and BDC, AD = DB, DC is common, and the included angles ADC and BDC are equal, since both are right angles. Therefore AC = BC by side–angle–side. [P4, 1.4]

**Step 4.** Apply the equal-chord-to-equal-arc direction, since equality of the chords has just been established. By 3.28, AC and BC cut off equal lesser arcs and equal greater arcs in the same circle. The particular arcs AC and CB contained in the given arc must therefore be equal: otherwise one would be the greater and the other the lesser of these corresponding pairs, so together they would equal the entire circumference. But together they constitute only the given arc, a proper part of that circumference, which is impossible. Hence arc AC equals arc CB, and C bisects the given circumference. [3.28, CN2, CN5]

**USED:** 1.10, 1.11, 1.4, 3.28, CN2, CN5, P1, P2, P4
**Human refs (from References field):** 1.4, 3.28
**Jaccard:** 0.222 — AI adds ['1.10', '1.11', 'CN2', 'CN5', 'P1', 'P2', 'P4']

## Proposition 3.31
**Statement:** In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

**Step 1.** Let BC be a diameter of a circle with centre O, and let A be any point on either semicircle, distinct from B and C. Join AB, AC, and AO, and produce BA through A to F. We take the direct equal-radii and exterior-angle route for the semicircle case. [P1, P2, D1.17, D1.18]

**Step 2.** Since OA = OB, the base angles OAB and ABO are equal. Since OA = OC, the base angles OAC and ACO are equal. But O lies on BC, and AO divides angle BAC. Adding these equalities therefore gives
∠BAC = ∠ABC + ∠BCA.
[D1.15, 1.5, CN2]

**Step 3.** The exterior-angle theorem applied to triangle ABC gives
∠FAC = ∠ABC + ∠BCA.
Consequently ∠BAC = ∠FAC. These are adjacent angles made by AC standing on the straight line BAF, so each is right. Since A was arbitrary on either semicircle, the angle in a semicircle is right. [1.32, CN1, D1.10, D3.8]

**Step 4.** Write R for a right angle, all right angles being equal. The angle sum of triangle ABC, after subtracting ∠BAC = R, gives
∠ABC + ∠BCA = R.
Each of these two angles is therefore less than R. [P4, 1.32, CN3, CN5]

**Step 5.** Consider the chord AC. Its arc not containing B is a proper part of the semicircle BAC; let D be any point of this arc. Thus the segment bounded by AC and arc ADC is less than a semicircle, while the complementary segment bounded by AC and arc ABC is greater than a semicircle. Angle ABC is an angle in the greater segment and, by Step 4, is less than R. We now use equality of angles in the same segment—the direct way to transfer this comparison from B to every other vertex on arc ABC. Hence every angle in the greater segment is less than a right angle. [D1.17, D1.18, D3.6, D3.8, CN5, 3.21]

**Step 6.** Join AD and CD. In the cyclic quadrilateral ABCD, the opposite angles ABC and ADC sum to two right angles. Using Step 4 and subtracting equal angles gives
∠ADC = 2R − ∠ABC = R + ∠BCA > R.
Since D was arbitrary on the smaller arc AC, every angle in the less segment is greater than a right angle. [P1, 3.22, CN2, CN3, CN5, D3.8]

**Step 7.** It remains to compare the angles **of** the segments, namely the angles between their chord and their circumference. At A, the angle of the greater segment is bounded by AC and arc ABC. The chord AB, apart from its endpoints, lies inside the circle; it also lies on the side of AC occupied by the greater segment. Thus AB lies within this segment-angle, and the right angle BAC is a proper part of it. The angle of the greater segment is therefore greater than a right angle. [3.2, D3.6, D3.7, CN5]

**Step 8.** The minor arc ADC lies on the C-side of line AB. Indeed, it cannot cross AB again: three collinear points of the circumference would place the middle one inside a chord, contrary to the fact that the chord's interior lies inside the circle. The same arc lies on the side of AC opposite B, which is the F-side of AC. Consequently, at A, arc ADC lies strictly between the rays AC and AF. The angle of the less segment, bounded by AC and this arc, is therefore a proper part of ∠FAC, which is right by Step 3. It is thus less than a right angle. [3.2, D3.6, D3.7, CN5]

Every non-diametral chord can serve as AC by taking B to be the opposite endpoint of the diameter through C, and either endpoint can be named A. Therefore all the assertions hold generally: the angle in a semicircle is right; the angle in a greater segment is less than a right angle; the angle in a less segment is greater than a right angle; and the angles of the greater and less segments are respectively greater and less than a right angle.

**USED:** 1.32, 1.5, 3.2, 3.21, 3.22, CN1, CN2, CN3, CN5, D1.10, D1.15, D1.17, D1.18, D3.6, D3.7, D3.8, P1, P2, P4
**Human refs (from References field):** 1.17, 1.32, 1.5, 3.22, D1.10
**Jaccard:** 0.200 — AI adds ['3.2', '3.21', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'D1.18', 'D3.6', 'D3.7', 'D3.8', 'P1', 'P2', 'P4']; Human adds ['1.17']

## Proposition 3.32
**Statement:** If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

**Step 1.** Let a straight line touch the circle at A, and let AB be the chord drawn from A. Find the centre O, join AO, and produce it to meet the circle again at C; thus AC is a diameter. Join BC when B ≠ C. We use this diameter because the angle in a semicircle gives a direct right-angle comparison. [3.1, P1, P2, D1.17]

**Step 2.** The radius OA is perpendicular to the tangent, so AC is also perpendicular to it. If B = C, both angles between AB and the tangent are right angles, and every angle in either semicircle on AB is right. The required equalities therefore hold in this case. Henceforth suppose B ≠ C. Name the opposite tangent rays AT and AU so that AB lies within the right angle TAC. [3.18, 3.31, P4]

**Step 3.** Since AC is a diameter, ∠ABC is right. The angles of triangle ABC equal two right angles; subtracting ∠ABC gives
∠BAC + ∠ACB = one right angle.
Also, since ∠TAC is right and AB lies within it,
∠TAB + ∠BAC = one right angle.
Subtracting the common angle BAC from these equal right angles yields
∠TAB = ∠ACB. [3.31, 1.32, 3.18, P4, CN3]

**Step 4.** Let Y be any point, other than A and B, on the arc AB containing C. If Y ≠ C, the angles AYB and ACB are in the same segment and therefore equal; for Y = C this equality is immediate. Consequently
∠TAB = ∠AYB.
This is the required alternate segment for ∠TAB: C, and hence this arc, lies on the opposite side of AB from the tangent ray AT. [3.21, CN1]

**Step 5.** Let X be any point, other than A and B, on the other arc AB, and join AX and BX. The quadrilateral AXBC is inscribed in the circle, so its opposite angles satisfy
∠AXB + ∠ACB = two right angles.
Because AT and AU are opposite rays, we also have
∠TAB + ∠BAU = two right angles.
By Step 3, ∠ACB = ∠TAB. Subtracting these equal angles from the equal totals gives
∠AXB = ∠BAU.
The arc containing X lies on the opposite side of AB from AU, so this is the other required alternate segment. Thus each angle made by the chord with the tangent equals the angles in its alternate segment. [P1, 3.22, 1.13, P4, CN3]

**USED:** 1.13, 1.32, 3.1, 3.18, 3.21, 3.22, 3.31, CN1, CN3, D1.17, P1, P2, P4
**Human refs (from References field):** 1.32, 3.19, 3.22, 3.31
**Jaccard:** 0.214 — AI adds ['1.13', '3.1', '3.18', '3.21', 'CN1', 'CN3', 'D1.17', 'P1', 'P2', 'P4']; Human adds ['3.19']

## Proposition 3.33
**Statement:** On a given straight line to describe a segment of a circle admitting an angle equal to a given rectilineal angle.

**Step 1.** Let AB be the given straight line and α the given rectilineal angle. At A construct a ray AT such that ∠BAT = α [1.23]. We choose the tangent–chord route: making AT tangent to a circle through A and B will give the required angle directly, with the same concluding argument for acute, right, and obtuse angles [3.32].

**Step 2.** Bisect AB at M [1.10]. If α is right, take O = M; then AT is perpendicular to AO [D1.10]. If α is not right, draw the straight line p through M perpendicular to AB, and the straight line q through A perpendicular to AT [1.11].

**Step 3.** In the non-right case, p and q meet. Indeed, write R for a right angle. If α is acute, q has a ray on the side of AB opposite T making the acute angle R − α with AB. If α is obtuse, q has a ray on the same side of AB as T making the acute angle α − R with AB [D1.10, 1.13]. On the corresponding side of AB, the angle between MA and p is right. Thus the interior angles made by the transversal AM with q and p on that side are together less than two right angles. Produce the lines to meet at O on that side [P2, P5].

**Step 4.** We have OA = OB. In the right-angle case this is simply MA = MB. Otherwise join OB [P1]. In triangles AMO and BMO, AM = BM, MO is common, and the included angles at M are right and therefore equal [P4]. Consequently OA = OB by side–angle–side [1.4].

**Step 5.** Describe the circle with centre O and radius OA [P3]. Since OB = OA, this circle passes through both A and B [D1.15].

**Step 6.** The line AT touches this circle at A. For AO is perpendicular to AT: in the right-angle case AO lies along AB, and otherwise it lies on q. Produce AO through the centre to form the diameter through A [P2, D1.17]. The straight line through the extremity A perpendicular to this diameter falls outside the circle [3.16]. Since AT meets the circle at A but does not cut it, AT is a tangent [D3.2].

**Step 7.** The chord AB lies within the circle [3.2]. Select the segment bounded by AB and the arc lying on the side of AB opposite the ray AT [D3.6]. Let C be any point of that arc other than A or B, and join CA and CB [P1]. Then ∠ACB is an angle in the selected segment [D3.8].

**Step 8.** Since AT is tangent at A and AB is the chord from the point of contact, the angle ∠BAT equals the angle ∠ACB in the alternate segment [3.32]. But ∠BAT = α by construction; hence ∠ACB = α [CN1]. Therefore the selected segment on the given straight line AB admits an angle equal to the given rectilineal angle, as required.

**USED:** 1.10, 1.11, 1.13, 1.23, 1.4, 3.16, 3.2, 3.32, CN1, D1.10, D1.15, D1.17, D3.2, D3.6, D3.8, P1, P2, P3, P4, P5
**Human refs (from References field):** 1.4, 3.16, 3.31, 3.32
**Jaccard:** 0.143 — AI adds ['1.10', '1.11', '1.13', '1.23', '3.2', 'CN1', 'D1.10', 'D1.15', 'D1.17', 'D3.2', 'D3.6', 'D3.8', 'P1', 'P2', 'P3', 'P4', 'P5']; Human adds ['3.31']

## Proposition 3.34
**Statement:** From a given circle to cut off a segment admitting an angle equal to a given rectilineal angle.

**Step 1.** Let Γ be the given circle and α the given rectilineal angle. Choose a point A on Γ and draw a straight line touching Γ at A. Choose a point B on this tangent, distinct from A. [3.17]

**Step 2.** At A, on the straight line AB, construct an angle BAC equal to α, placing the ray AC on the side of the tangent containing the circle. Let C be its second intersection with Γ. The chord AC cuts off two segments of Γ; select the segment whose arc lies on the side of AC opposite B. [1.23, D3.6]

**Step 3.** Take any point D on the arc of the selected segment, other than A or C, and join DA and DC. Then ∠ADC is an angle in that segment. Use the tangent–chord theorem directly, since it relates the constructed angle to precisely the required alternate segment: as AB touches Γ and AC cuts it, ∠BAC = ∠ADC. [P1, D3.8, 3.32]

**Step 4.** Since ∠BAC = α by construction and ∠ADC = ∠BAC, it follows that ∠ADC = α. Thus the segment bounded by AC and the arc through D admits an angle equal to the given rectilineal angle, and is the required segment cut off from the given circle. [CN1]

**USED:** 1.23, 3.17, 3.32, CN1, D3.6, D3.8, P1
**Human refs (from References field):** 1.23, 3.32
**Jaccard:** 0.286 — AI adds ['3.17', 'CN1', 'D3.6', 'D3.8', 'P1']

## Proposition 3.35
**Statement:** If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.

**Step 1.** Let the chords AB and CD intersect at E inside the circle. Find its centre O, and bisect AB at M and CD at N. Join OA, OC, OE, OM, and ON whenever their endpoints are distinct. We take the midpoint-and-square route because each required rectangle arises from a chord cut at its midpoint and at E. [3.1, 1.10, P1]

**Step 2.** Write S(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW. Use S(XX)=0 merely as notation for an omitted term, not for a constructed square. By II.5,
R(AE, EB) + S(ME) = S(AM),
R(CE, ED) + S(NE) = S(CN).
If E=M, the first equality holds directly because AE=EB=AM, so the rectangle is the square on AM. Likewise, if E=N, the second equality holds directly. Thus these equalities include the cases in which E is a midpoint. [D2.1, D1.22, 2.5]

**Step 3.** If AB does not pass through O, then OM, joining the centre to the midpoint of AB, is perpendicular to AB. Applying I.47 to the right triangles OMA and OME gives
S(OA) = S(OM) + S(AM),
S(OE) = S(OM) + S(ME).
When E=M, the second equality is simply S(OE)=S(OM), so no degenerate triangle is used. If AB passes through O, its midpoint M is O, since OA=OB are radii; both displayed equalities then hold directly with the omitted zero terms.

Exactly the same reasoning for CD gives
S(OC) = S(ON) + S(CN),
S(OE) = S(ON) + S(NE),
again directly if E=N or if N=O. [3.3, 1.47, D1.15]

**Step 4.** Add S(OM) to both sides of the first equality in Step 2. Substituting the equalities from Step 3 yields
R(AE, EB) + S(OE) = S(OA).
Similarly, adding S(ON) to both sides of the second equality in Step 2 yields
R(CE, ED) + S(OE) = S(OC).
Here an omitted zero term requires no addition. [CN2, CN1]

**Step 5.** Since OA and OC are radii of the same circle, they are equal, and hence their squares are equal. Therefore
R(AE, EB) + S(OE) = R(CE, ED) + S(OE).
Subtracting the common square on OE gives
R(AE, EB) = R(CE, ED).
If E=O, that square was already omitted and the equality follows immediately. Thus the rectangle contained by the segments of one chord equals the rectangle contained by the segments of the other. [D1.15, CN1, CN3]

**USED:** 1.10, 1.47, 2.5, 3.1, 3.3, CN1, CN2, CN3, D1.15, D1.22, D2.1, P1
**Human refs (from References field):** 1.47, 2.5, 3.3
**Jaccard:** 0.250 — AI adds ['1.10', '3.1', 'CN1', 'CN2', 'CN3', 'D1.15', 'D1.22', 'D2.1', 'P1']

## Proposition 3.36
**Statement:** If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the circle and the other touch it, the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference will be equal to the square on the tangent.

**Step 1.** Let X be the exterior point, let the secant meet the circle first at A and then at B, and let XT touch the circle at T. Find the centre O and join OX, OA, OB, and OT. Write UV² for the square on UV and UV·WZ for the rectangle contained by UV and WZ. We use the direct route through the bisected-chord identity of 2.6, distinguishing whether the secant passes through O. [3.1, P1]

**Step 2.** Since OT is drawn from the centre to the point of contact, OT is perpendicular to XT. Hence, by the theorem on right-angled triangles,
OX² = OT² + XT².
The radii OT and OA are equal, so
OX² = OA² + XT². [3.18, 1.47, D1.15]

**Step 3.** Suppose first that the secant passes through O. Then O lies between A and B, and OA = OB, so AB is bisected at O. Proposition 2.6 applies naturally to this bisected chord with AX added beyond A, and gives
XB·XA + OA² = OX².
Comparing this with Step 2 and subtracting the common square OA² yields
XB·XA = XT².
Thus the proposition holds in this case. [D1.15, 2.6, CN1, CN3]

**Step 4.** Suppose now that the secant does not pass through O. Bisect AB at M and join OM. Since the straight line from the centre bisects the chord AB, which does not pass through the centre, OM is perpendicular to AB, and therefore also to MX. [1.10, P1, 3.3]

**Step 5.** Apply the same bisected-line identity to AB, bisected at M, with AX added beyond A. It gives
XB·XA + AM² = XM². [2.6]

**Step 6.** The triangles OMA and OMX are right-angled at M. Therefore
OA² = OM² + AM²,
and
OX² = OM² + XM².
Add OM² to both sides of the equality in Step 5. Substituting these two equalities gives
XB·XA + OA² = OX². [1.47, CN2, CN1]

**Step 7.** Comparing Step 6 with Step 2 and subtracting OA² gives
XB·XA = XT².
The two cases exhaust the possible positions of the secant. Consequently, the rectangle contained by the whole secant XB and its exterior part XA equals the square on the tangent XT, as required. [CN1, CN3]

**USED:** 1.10, 1.47, 2.6, 3.1, 3.18, 3.3, CN1, CN2, CN3, D1.15, P1
**Human refs (from References field):** 1.47, 2.6, 3.18, 3.3
**Jaccard:** 0.364 — AI adds ['1.10', '3.1', 'CN1', 'CN2', 'CN3', 'D1.15', 'P1']

## Proposition 3.37
**Statement:** If a point be taken outside a circle and from the point there fall on the circle two straight lines, if one of them cut the circle, and the other fall on it, and if further the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference be equal to the square on the straight line which falls on the circle, the straight line which falls on it will touch the circle.

**Step 1.** Let P be outside the circle, and let the secant meet it first at A and then at B. Let C be the point on the circle at which the other straight line PC falls. The hypothesis is that the rectangle PA·PB equals the square on PC. Draw a tangent PT to the circle (3.17). We choose comparison with this tangent because 3.36 concerns exactly the rectangle appearing in the hypothesis. If C = T, the conclusion already holds.

**Step 2.** By 3.36, the rectangle PA·PB equals the square on PT. Hence the squares on PC and PT are equal (CN1), and therefore PC = PT: otherwise the square on the shorter segment could be placed as a proper part of the square on the longer, contrary to CN5.

**Step 3.** Find the centre O of the circle and join OP, OC, and OT (3.1, P1). Since OC and OT are radii of the same circle, OC = OT (D1.15).

**Step 4.** Because PT touches the circle at T, OT is perpendicular to PT (3.18). Thus angle OTP is right (D1.10).

**Step 5.** The three lengths OP, OC, CP equal OP, OT, TP respectively. The points O, C, P cannot be collinear: otherwise one of their three distances would equal the sum of the other two, contradicting the strict triangle inequalities for triangle OTP (1.20). Thus triangles OCP and OTP have their three corresponding sides equal. By 1.8, angle OCP equals angle OTP, and so angle OCP is right.

**Step 6.** Produce CO through the centre to obtain the diameter having C as an extremity (P2). The straight line PC is perpendicular to this diameter at C. Therefore it falls outside the circle (3.16). Since it meets the circle at C but, when produced, does not cut it, PC touches the circle by D3.2. This is the required conclusion.

**USED:** 1.20, 1.8, 3.1, 3.16, 3.17, 3.18, 3.36, CN1, CN5, D1.10, D1.15, D3.2, P1, P2
**Human refs (from References field):** 1.8, 3.16, 3.18, 3.36
**Jaccard:** 0.286 — AI adds ['1.20', '3.1', '3.17', 'CN1', 'CN5', 'D1.10', 'D1.15', 'D3.2', 'P1', 'P2']
