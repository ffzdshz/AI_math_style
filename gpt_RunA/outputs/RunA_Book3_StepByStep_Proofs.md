# Book 3 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 3.1
**Statement:** To find the centre of a given circle.

**Step 1.** Choose two distinct points A and B on the circumference of the given circle. Join AB and bisect it at M, so that AM = MB. [P1, 1.10]

**Step 2.** At M construct a straight line ℓ perpendicular to AB, and produce it in both directions. The construction will find the centre by bisecting the diameter on this line, rather than by constructing a second perpendicular bisector. [1.11, P2, D1.10]

**Step 3.** Let O denote a centre whose existence is part of the definition of the given circle; its position is not assumed known. Then OA = OB. If O lies on the straight line AB, it must be M. Indeed, if O lies outside the segment AB, one of OA and OB contains the other as a proper part, so they are unequal. If O lies inside AB but differs from M, one of OA and OB is greater than AM = MB and the other is less. The endpoints A and B are excluded because the centre is within the circle. Thus, in this case, O = M and O lies on ℓ. [D1.15, D1.16, CN5]

**Step 4.** Suppose instead that O does not lie on the straight line AB. Join OA, OB, and OM. In triangles AMO and BMO, AM = BM, MO is common, and OA = OB. Since the three corresponding sides are already equal, apply 1.8 directly: angle AMO equals angle BMO. These are adjacent angles on the straight line AB, so both are right angles. [P1, CN4, 1.8, D1.10]

**Step 5.** Take a point X on the ray of ℓ from M lying on the same side of AB as O. Angles AMX and AMO are both right angles and hence equal. If rays MX and MO were distinct, one of these angles would be a proper part of the other, contradicting their equality. Therefore MO lies on ℓ. Together with Step 3, this proves that O lies on ℓ in every case. [P4, CN5]

**Step 6.** Produce ℓ to the circumference in both directions, obtaining C and D on opposite sides of O. Thus CD is a diameter. Bisect CD at K, so CK = KD. Since O is a centre, CO = OD. If K differed from O, then, after interchanging C and D if necessary, their order would be C, K, O, D. Consequently CO > CK = KD > OD, contrary to CO = OD. Hence K = O. Therefore the constructed point K is the centre of the given circle, as required. [P2, D1.15, D1.17, 1.10, CN5, D1.16]

**USED:** 1.10, 1.11, 1.8, CN4, CN5, D1.10, D1.15, D1.16, D1.17, P1, P2, P4
**Human refs (from References field):** 1.8, D1.10
**Jaccard:** 0.167 — AI adds ['1.10', '1.11', 'CN4', 'CN5', 'D1.15', 'D1.16', 'D1.17', 'P1', 'P2', 'P4']

## Proposition 3.2
**Statement:** If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

**Step 1.** Let A and B be two distinct points on the circumference of the given circle, and draw AB. Find the centre O and join OA and OB. Since these are radii, OA = OB. [P1, 3.1, D1.15]

**Step 2.** Let C be any point strictly between A and B. If C coincides with O, it is inside the circle, since the centre lies within it. Otherwise join OC. Our route is to show OC < OA, separating the collinear case from the triangular case. [D1.15, P1]

**Step 3.** Suppose first that O lies on the straight line AB. Then O must lie between A and B; otherwise one of the equal radii OA and OB would be a proper part of the other, contrary to the whole being greater than its part. Since C is strictly between A and B and differs from O, OC is a proper part of either OA or OB. Hence OC < OA. [D1.15, CN5]

**Step 4.** Now suppose that O does not lie on the straight line AB. Since OA = OB, the base angles of triangle OAB are equal: ∠OAB = ∠OBA. Because C lies between A and B, these are respectively ∠OAC and ∠OBC. Thus ∠OAC = ∠OBC. [1.5]

**Step 5.** In triangle AOC, ∠OCB is an exterior angle, and therefore ∠OCB > ∠OAC. The exterior-angle theorem is the direct choice here because CB already continues AC. By Step 4, ∠OCB > ∠OBC. Consequently, in triangle OBC, the side OB opposite the greater angle is greater than OC. Thus OC < OB = OA. [1.16, 1.19, D1.15]

**Step 6.** In either case, OC < OA. Therefore C cannot be on the circumference, since its distance from O would then equal OA. Nor can C be outside the circle: since O is inside and the circumference bounds the figure, the segment OC would meet that boundary at a point D strictly between O and C. Then OD = OA, while OC > OD, contradicting OC < OA. Hence C is inside the circle. Since C was any point strictly between A and B, the straight line joining A and B lies within the circle, except for its endpoints on the circumference. [D1.15, CN5]

**USED:** 1.16, 1.19, 1.5, 3.1, CN5, D1.15, P1
**Human refs (from References field):** 1.16, 1.19, 1.5, 3.1
**Jaccard:** 0.571 — AI adds ['CN5', 'D1.15', 'P1']

## Proposition 3.3
**Statement:** If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

**Step 1.** Let AB have its endpoints on the circumference of a circle with centre O, and suppose AB does not pass through O. Let a straight line through O cut AB at D, between A and B. Thus O and D are distinct. Join OA and OB (P1). Since they are radii of the same circle, OA = OB (D1.15).

**Step 2.** First suppose that the line through O bisects AB, so AD = DB. In triangles ADO and BDO, AD = BD by hypothesis, DO = DO because it is common (CN4), and AO = BO by Step 1. Apply 1.8 directly to these three side equalities: the angles contained by AD, DO and BD, DO are equal. Hence ∠ADO = ∠BDO. This is the direct side-equality route, requiring no auxiliary construction (1.8).

**Step 3.** Since A, D, B lie on one straight line, ∠ADO and ∠BDO are adjacent angles made by OD standing on AB. Their equality makes each a right angle, and OD is perpendicular to AB (D1.10). Thus the straight line through the centre that bisects AB also cuts it at right angles.

**Step 4.** Conversely, suppose the straight line through O cuts AB at right angles at D. Then ∠ADO and ∠BDO are right angles, and therefore are equal (P4).

**Step 5.** Since OA = OB, the base angles of triangle OAB are equal: ∠OAB = ∠ABO (1.5). Because D lies between A and B, these are respectively ∠OAD and ∠DBO. Hence ∠OAD = ∠DBO.

**Step 6.** Triangles ADO and BDO therefore have two corresponding angles equal by Steps 4–5, and AO = BO by Step 1. These equal sides are opposite the equal angles at D. Consequently AD = BD by the side-opposite-an-equal-angle case of 1.26. This case is the direct choice because all its hypotheses are already established. Thus the straight line through the centre that cuts AB at right angles also bisects it, completing both assertions.

**USED:** 1.26, 1.5, 1.8, CN4, D1.10, D1.15, P1, P4
**Human refs (from References field):** 1.26, 1.5, 1.8, D1.10
**Jaccard:** 0.500 — AI adds ['CN4', 'D1.15', 'P1', 'P4']

## Proposition 3.4
**Statement:** If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.

**Step 1.** Let the distinct chords AB and CD intersect at E, and suppose neither passes through the centre. Assume, for contradiction, that they bisect one another: AE = EB and CE = ED. [Hypothesis; supposition for contradiction.]

**Step 2.** Find the centre O of the circle. [3.1] Since neither chord passes through O, O is distinct from E and lies on neither chord. Join OE. [P1]

**Step 3.** Path choice: apply the forward implication of 3.3, since the assumed bisections are precisely its hypotheses. The straight line OE passes through the centre and bisects each of AB and CD; therefore it cuts both at right angles. In particular, ∠OEA, ∠OEB, ∠OEC, and ∠OED are right angles. [3.3]

**Step 4.** Relabel the endpoints if necessary so that A and C lie on the same side of the straight line OE. This is possible because E lies between the endpoints of each chord, and neither chord lies along OE. The rays EA and EC are distinct because the chords are distinct. Thus, on this same side of OE, one of ∠OEA and ∠OEC is a proper part of the other. Consequently these angles are unequal, since the whole is greater than the part. [CN5]

**Step 5.** But ∠OEA and ∠OEC are both right angles by Step 3, so they are equal. [P4] This contradicts Step 4. Hence the two chords cannot bisect one another. Therefore, if two straight lines in a circle cut one another and neither passes through the centre, they do not bisect one another. [Reductio from Steps 1–4.]

**USED:** 3.1, 3.3, CN5, P1, P4
**Human refs (from References field):** 3.1, 3.3
**Jaccard:** 0.400 — AI adds ['CN5', 'P1', 'P4']

## Proposition 3.5
**Statement:** If two circles cut one another, they will not have the same centre.

**Step 1.** Let two circles cut one another at A. Suppose, for contradiction, that they have the same centre O. Then O lies inside both circles. We use the direct route of comparing equal radii with a whole and its proper part. (Hypothesis; D1.15, D1.16.)

**Step 2.** Since the circles cut one another, choose a point B on the first circumference strictly inside the second circle. Join OA and OB, and produce OB beyond B until it meets the second circumference at C. Since O and B are inside the second circle, the points occur in the order O, B, C; hence OB is a proper part of OC. (Cutting hypothesis; P1, P2; D1.15, D1.16.)

**Step 3.** Since O is the centre of the first circle and A and B lie on its circumference, OA = OB. Since O is also the centre of the second circle and A and C lie on its circumference, OA = OC. Therefore OB = OC. (D1.15; CN1.)

**Step 4.** But OC is greater than its proper part OB, contradicting Step 3. The supposition of a common centre is therefore impossible. Thus, if two circles cut one another, they will not have the same centre. (CN5; Steps 2–3, proof by contradiction.)

**USED:** CN1, CN5, D1.15, D1.16, P1, P2
**Human refs (from References field):** D1.15
**Jaccard:** 0.167 — AI adds ['CN1', 'CN5', 'D1.16', 'P1', 'P2']

## Proposition 3.6
**Statement:** If two circles touch one another, they will not have the same centre.

**Step 1.** Let two distinct circles touch at A. Then A belongs to both circumferences (D3.3). Suppose, for a contradiction, that they have the same centre O, which therefore lies within both circles (D1.15, D1.16). We use the direct radius-comparison route: the common point A supplies a radius of each circle.

**Step 2.** Since the circles are distinct, their circumferences do not coincide (D1.15). Interchanging their names if necessary, choose B on the circumference of the first circle but not on that of the second.

**Step 3.** Join OA and OB (P1). Along the ray from O through B, producing OB if necessary, let C be where that ray meets the circumference of the second circle (P2; D1.15, D1.16, since O lies within that circle). Since B is not on this circumference, B and C are distinct.

**Step 4.** In the first circle, OB = OA; in the second circle, OC = OA, because straight lines from a circle's centre to its circumference are equal (D1.15, D1.16). Therefore OB = OC (CN1).

**Step 5.** But B and C are distinct points on the same ray from O, so one of OB and OC is a proper part of the other. The whole is greater than the part (CN5), contradicting their equality in Step 4. Therefore two circles which touch one another cannot have the same centre.

**USED:** CN1, CN5, D1.15, D1.16, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN1', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1', 'P2']

## Proposition 3.7
**Statement:** If on the diameter of a circle a point be taken which is not the centre of the circle, and from the point straight lines fall upon the circle, that will be greatest on which the centre is, the remainder of the same diameter will be least, and of the rest  the nearer to the straight line through the centre is always greater than the more remote, and only two equal straight lines will fall from the point on the circle, one on each side of the least straight line.

**Step 1.** Let AB be the diameter, O its centre, and P the given point. Name the endpoints so that their order is A, O, P, B. Thus PA passes through the centre, while PB is the remainder of the diameter. Join O to any circumference points used below. All such radii are equal to OA and OB. (D1.17, P1, D1.15.)

**Step 2.** First prove the greatest-line assertion directly by the triangle inequality. For any circumference point X other than A or B, triangle OPX gives
OP + OX > PX. (1.20.)
Since OX = OA, it follows that
PA = PO + OA = PO + OX > PX. (D1.15, CN2.)
Also PA > OA = OB > PB, because each whole segment exceeds its indicated part. Therefore PA is strictly greater than every other line from P to the circumference. (D1.15, CN5.)

**Step 3.** In the same triangle,
OP + PX > OX = OB = OP + PB. (1.20, D1.15.)
Removing the common segment OP gives PX > PB. Together with PA > PB from Step 2, this proves that PB is strictly the least of all the lines. (CN3, CN5.)

**Step 4.** Take two points X and Y on either open semicircle, occurring in the order A, X, Y, B along its circumference. This is the order in which PX is nearer to PA than PY: within that half-plane, PX makes the smaller angle with PA. Since OP points towards B, the angle XOP contains the angle YOP as a proper part; hence ∠XOP > ∠YOP. (D1.17, CN5.) In triangles XOP and YOP, OX = OY and OP is common. Therefore PX > PY by the comparison of the sides opposite unequal included angles. (D1.15, 1.24.) This is the direct comparison to use, since the equal radii and the common side already supply its hypotheses.

**Step 5.** Let X be any circumference point off AB. On the opposite side of AB construct a ray OX′ such that ∠POX′ = ∠POX, and produce it to meet the circumference at X′. (1.23, P2.) Now OX′ = OX, OP is common, and the included angles at O are equal. Consequently triangles OPX′ and OPX have PX′ = PX and ∠OPX′ = ∠OPX. (D1.15, 1.4.) Since PO and PA are the same ray, PX and PX′ also make equal angles with PA. They lie on opposite sides of the line containing PB.

**Step 6.** The comparison in Step 4 also covers lines on opposite sides of AB. Indeed, replace either line by its equal partner from Step 5 on the side of the other. Both its length and its angle with PA are preserved. Step 4 then shows that the line making the smaller angle with PA is greater. Thus, among the non-diametral lines, the nearer to PA is always greater than the more remote. (Steps 4–5.)

**Step 7.** Finally, Step 4 shows that no two distinct lines ending on the same open semicircle can be equal. Step 5 supplies, for each non-diametral line, an equal line ending on the opposite semicircle. There can be no third equal line, since two of three would end on the same semicircle; nor can either diametral line belong to such an equal pair, by their strict extremality in Steps 2–3. Hence each non-diametral line has exactly one distinct equal partner, one on each side of the least line PB. Together with Steps 2, 3, and 6, this proves every assertion. (Steps 2–6.)

**USED:** 1.20, 1.23, 1.24, 1.4, CN2, CN3, CN5, D1.15, D1.17, P1, P2
**Human refs (from References field):** 1.20, 1.23, 1.24, 1.4
**Jaccard:** 0.364 — AI adds ['CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'P1', 'P2']

## Proposition 3.8
**Statement:** If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest   the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

**Step 1.** Find the centre O of the circle, and draw and produce PO, where P is the given exterior point (3.1, P1, P2). Let its intersections with the circumference be A and B, in the order P, A, O, B; thus AB is a diameter (D1.17). Along any other secant from P, call its first intersection the convex endpoint and its second intersection the concave endpoint. Nearness to the central straight line means smaller inclination to PO at P. All radii of the circle are equal (D1.15).

**Step 2.** Let W be any circumference point other than A and B, and join OW and PW (P1). In triangle POW, the triangle inequality and equality of radii give
PW < PO + OW = PO + OB = PB,
and
PO < PW + OW = PW + OA
(1.20, D1.15, CN2). Subtracting OA from the latter comparison gives PA < PW (CN3). Also PA < PB because PA is a proper part of PB (CN5). Consequently PB is uniquely greatest and PA uniquely least among all the segments from P to the circumference.

**Step 3.** Consider two non-diametral secants on the same side of PO, with intersections in the orders P, U, X and P, V, Y. Suppose PX is nearer PO than PY, so that ∠OPX < ∠OPY. Thus U and V are convex endpoints, while X and Y are concave endpoints. Join OU, OX, OV and OY (P1).

**Step 4.** By this order of the rays, O lies on one side of the straight line PX, while V and Y lie on the other. Hence the segments OV and OY cross PX, at S and T respectively. Each radius lies within the circle: produce it through O to complete a diameter and apply the theorem that the join of two circumference points lies within the circle (P2, D1.17, 3.2). Since S and T are interior points of these radii, they lie inside the circle and therefore strictly between U and X on the nearer secant. Thus the relevant orders are P, U, S, X and P, U, T, X.

**Step 5.** In triangle POS, U lies strictly between P and S, so OU divides ∠POS into two angles. Since OS is the same ray as OV, it follows that ∠POV > ∠POU. Likewise, T lies strictly between P and X, so OT divides ∠POX; since OT is the same ray as OY, ∠POX > ∠POY. Both inequalities follow because the whole angle is greater than its proper part (CN5).

**Step 6.** For these comparisons, the direct choice is the hinge theorem, 1.24: the triangles already have the common side OP and equal radii as their other corresponding sides. In triangles POX and POY, OX = OY and ∠POX > ∠POY; hence PX > PY. In triangles POV and POU, OV = OU and ∠POV > ∠POU; hence PV > PU (D1.15, 1.24). Therefore, on the concave circumference the nearer secant is greater, whereas on the convex circumference the nearer segment is less.

**Step 7.** Let Q be any circumference point off the diameter AB. On the opposite side of PO construct at O a ray making with OP an angle equal to ∠POQ, and let Q′ be its intersection with the circumference (1.23, P2). Since OQ = OQ′, OP is common, and the included angles are equal, triangles POQ and POQ′ have PQ = PQ′ and ∠OPQ = ∠OPQ′ (D1.15, 1.4). Thus every non-diametral segment has an equal companion on the opposite side of PA, with the same inclination to PO.

**Step 8.** Apply the construction of Step 7 to both endpoints of a secant. Their companions lie on the same opposite ray from P, because their angles with PO are equal (1.4, CN1). Their distances from P are preserved, so the nearer endpoint remains nearer and the farther endpoint remains farther (CN5). Thus this construction preserves both the inclination of the secant and its convex or concave endpoint classification. Consequently the comparisons in Step 6 also apply when the two original secants lie on opposite sides of PO: transfer one to the side of the other and use the unchanged lengths and inclinations.

**Step 9.** For uniqueness, use 1.7 directly, since its same-base, same-side hypotheses are precisely those available here. If distinct circumference points Q and R on the same side of PO satisfied PQ = PR, then also OQ = OR, since both are radii (D1.15). The two triangles on the same base PO would therefore have their corresponding sides from P and O equal while their vertices were distinct and on the same side of the base, contrary to 1.7. Hence at most one endpoint on each side can give any prescribed length. Together with Step 7, this proves that every non-diametral segment has exactly one equal companion, on the opposite side of the least segment PA, and that no third equal segment exists. Step 2 excludes either extreme segment from such a pair.

**Step 10.** Therefore the segment PB through the centre is greatest; among the other segments to the concave circumference, the nearer to PB is greater. The segment PA between P and the diameter is least; among the other segments to the convex circumference, the nearer to PA is less. Apart from the unique extreme segments PA and PB, equal segments occur in pairs only, one on each side of PA. These are all the required assertions (Steps 2, 6, 8 and 9).

**USED:** 1.20, 1.23, 1.24, 1.4, 1.7, 3.1, 3.2, CN1, CN2, CN3, CN5, D1.15, D1.17, P1, P2
**Human refs (from References field):** 1.20, 1.21, 1.24, 1.4, 3.1
**Jaccard:** 0.250 — AI adds ['1.23', '1.7', '3.2', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'P1', 'P2']; Human adds ['1.21']

## Proposition 3.9
**Statement:** If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

**Step 1.** Let P be the given point within the circle. Choose three of the equal straight lines, PA, PB, and PC, with distinct endpoints A, B, and C on the circumference. Thus PA = PB = PC. [Hypothesis]

**Step 2.** Find the centre O of the circle. If P = O, the conclusion already holds; suppose, therefore, that P is not O. [3.1]

**Step 3.** Join O to P and produce this straight line in both directions to meet the circumference at D and E. Since DE passes through the centre and terminates on the circumference in both directions, it is a diameter, and the interior point P lies on it. [P1, P2, D1.17]

**Step 4.** We choose the equal-line conclusion of 3.7, since it applies directly to a point on a diameter which is not the centre. By that conclusion, no more than two equal straight lines can fall from P upon the circumference. [3.7]

**Step 5.** This contradicts the three distinct equal straight lines PA, PB, and PC of Step 1. Therefore the supposition that P is not O is false. Hence P is the centre of the circle, as required. [Steps 1–4]

**USED:** 3.1, 3.7, D1.17, P1, P2
**Human refs (from References field):** 1.8, 3.1, D1.10
**Jaccard:** 0.143 — AI adds ['3.7', 'D1.17', 'P1', 'P2']; Human adds ['1.8', 'D1.10']

## Proposition 3.10
**Statement:** A circle does not cut a circle at more points than two.

**Step 1.** Suppose, for a contradiction, that two circles Γ and Δ cut one another at three distinct points A, B, and C. Find their centres O and T respectively. Since the circles cut one another, O and T are distinct. [3.1, 3.5]

**Step 2.** Join TA, TB, TC, and OT. Because A, B, and C lie on the circumference of Δ and T is its centre, TA = TB = TC. The direct path is therefore to apply the bounds on the number of equal straight lines drawn from a point to a circle, distinguishing the position of T relative to Γ. [P1, D1.15]

**Step 3.** First suppose that T lies within or on the circumference of Γ. Produce the straight line OT to obtain a diameter of Γ; T lies on this diameter and is not its centre O. Proposition 3.7 applies to a point on a diameter other than the centre, including the endpoint case in its stated hypothesis, and permits at most two equal straight lines from that point to the circumference. The three distinct straight lines TA, TB, and TC contradict this bound. [P2, D1.17, 3.7; Step 2]

**Step 4.** Alternatively, suppose that T lies outside Γ. Produce TO through Γ, giving a straight line through its centre, and produce the other straight lines through the circle as necessary. Proposition 3.8 permits at most two equal straight lines from an exterior point to the circumference. Again, the three equal straight lines TA, TB, and TC contradict this bound. [P2, 3.8; Step 2]

**Step 5.** Every possible position of T relative to Γ has led to a contradiction. Thus two circles cannot cut one another at three distinct points, and consequently a circle does not cut a circle at more points than two. [Steps 3–4]

**USED:** 3.1, 3.5, 3.7, 3.8, D1.15, D1.17, P1, P2
**Human refs (from References field):** 3.1, 3.5
**Jaccard:** 0.250 — AI adds ['3.7', '3.8', 'D1.15', 'D1.17', 'P1', 'P2']

## Proposition 3.11
**Statement:** If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.

**Step 1.** Let the outer circle Γ and the inner circle γ touch internally at T, and let their centres be O and C respectively. Thus T belongs to both circumferences, and γ lies within Γ. The centres O and C are distinct. [Hypothesis; D3.3; 3.6]

**Step 2.** Join OC and produce it beyond C. Let this ray meet the circumference of γ at B beyond C, and the circumference of Γ at A beyond C. These intersections are taken in the indicated direction from C, which lies within both circles. [P1; P2; D1.15; D1.16; internal-containment hypothesis]

**Step 3.** Since γ lies within Γ, B cannot lie beyond A on this ray. Consequently OB ≤ OA: if B precedes A, OB is a proper part of OA; if B = A, the lengths are equal. [Internal-containment hypothesis; CN5]

**Step 4.** Suppose that T does not lie on the straight line OC. Join OT and CT. Then OCT is a triangle, and
OC + CT > OT.
The direct path is the triangle inequality, since the assumed non-collinearity immediately supplies this triangle. [P1; 1.20]

**Step 5.** The radii of γ give CT = CB, and the radii of Γ give OT = OA. Adding OC to the first equality, and observing that C lies between O and B, gives
OC + CT = OC + CB = OB. [D1.15; CN2]

**Step 6.** Substituting the equal lengths from Step 5 into the inequality of Step 4 yields OB > OA, contradicting Step 3. Therefore T lies on the straight line joining O and C. Hence the straight line joining the centres, produced if necessary, passes through the point of contact. [Steps 3–5; CN1]

**USED:** 1.20, 3.6, CN1, CN2, CN5, D1.15, D1.16, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.20', '3.6', 'CN1', 'CN2', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1', 'P2']

## Proposition 3.12
**Statement:** If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

**Step 1.** Let the two circles touch externally at T, and let their centres be O and P. Their interiors are disjoint by the external-contact hypothesis: they meet without cutting one another (D3.3). Their centres are distinct (3.6). Join OP, OT, and PT (P1).

**Step 2.** Let X be the point where the segment from O towards P leaves the circle with centre O, and let Y be the point where the segment from P towards O leaves the circle with centre P. Each centre is inside its own circle and outside the other, so X and Y lie between O and P (D1.15, D1.16; external-contact hypothesis). Their order must be O, X, Y, P, allowing X = Y: otherwise points between Y and X would be inside both circles, contrary to external contact.

**Step 3.** If X = Y, then OP = OX + YP; otherwise the intervening segment XY makes OP greater than OX + YP (CN5). Thus OP ≥ OX + YP. But OX = OT and YP = PT, since these are radii of their respective circles (D1.15). Adding these equalities gives OX + YP = OT + PT (CN2). Consequently,
OP ≥ OT + PT.

**Step 4.** Suppose O, T, and P are not collinear. Apply the triangle inequality, the direct choice because the two sides OT and TP are precisely the radii compared in Step 3. In triangle OTP it gives OT + TP > OP (1.20), contradicting Step 3. Hence O, T, and P are collinear.

**Step 5.** T cannot lie beyond either centre. If O lay between P and T, then PT > OP; if P lay between O and T, then OT > OP (CN5). Either case would give OT + PT > OP, again contradicting Step 3. Nor can T coincide with either centre, since T is on each circumference whereas a centre is inside its circle (D1.15, D1.16). Therefore T lies between O and P, and the straight line joining the centres passes through the point of contact.

**USED:** 1.20, 3.6, CN2, CN5, D1.15, D1.16, D3.3, P1
**Human refs (from References field):** 1.20
**Jaccard:** 0.125 — AI adds ['3.6', 'CN2', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1']

## Proposition 3.13
**Statement:** A circle does not touch a circle at more points than one, whether it touch it internally or externally.

**Step 1.** Suppose, for a contradiction, that two circles touch one another at two distinct points A and B. Thus A and B lie on both circumferences (D3.3). Find their centres O and Q (3.1). Since the circles touch, O and Q are distinct (3.6).

**Step 2.** Join OQ and produce it as necessary (P1, P2). We use the centre-line route, since the preceding contact propositions apply directly: for internal contact, 3.11 places each of A and B on the produced line OQ; for external contact, 3.12 places each on OQ itself. Hence, in either case, A, B, O, and Q are collinear (3.11, 3.12).

**Step 3.** The radii of each circle are equal, so OA = OB and QA = QB. Moreover, neither centre is on its own circumference (D1.15). Therefore O lies strictly between A and B: otherwise one of OA and OB would contain the other as a proper part, contradicting their equality (CN5). The same reasoning shows that Q lies strictly between A and B (D1.15, CN5).

**Step 4.** Since the centres are distinct, interchange the names A and B if necessary so that their order is A, O, Q, B. Then AO is a proper part of AQ, and QB is a proper part of OB. Consequently AO < AQ and QB < OB (CN5). But AQ = QB and OB = AO, being radii of the respective circles (D1.15). Thus AO < AQ = QB < OB = AO, which is impossible.

**Step 5.** The supposition of two distinct points of contact is therefore false in both cases. A circle cannot touch another circle at more than one point, whether internally or externally; and, since touching circles meet, they have exactly one point of contact (D3.3).

**USED:** 3.1, 3.11, 3.12, 3.6, CN5, D1.15, D3.3, P1, P2
**Human refs (from References field):** 3.11, 3.2, D3.3
**Jaccard:** 0.200 — AI adds ['3.1', '3.12', '3.6', 'CN5', 'D1.15', 'P1', 'P2']; Human adds ['3.2']

## Proposition 3.14
**Statement:** In a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another.

**Step 1.** Let O be the centre of the circle, and first let AB and CD be chords neither of which passes through O. Bisect AB at M and CD at N (1.10), and join OM, ON, OA, and OC (P1). Since the lines through the centre bisect the chords, OM is perpendicular to AB and ON is perpendicular to CD (3.3). Thus OMA and ONC are right angles (D1.10), while OA = OC because they are radii (D1.15). Path choice: bisecting first ensures that the perpendicular feet lie on the chords; 3.3 then supplies exactly the right triangles needed for 1.47.

**Step 2.** Write S(XY) for the square on the segment XY. Squares on equal segments are equal: their equal sides and equal right angles allow them to coincide upon superposition (D1.22, P4, CN4). Conversely, equal squares have equal sides. Indeed, if one side were greater, cut off from it a segment equal to the smaller side (1.3). By 2.4, the square on the greater side equals the square on the smaller side together with the square on the positive remainder and twice the rectangle contained by the smaller side and that remainder. It therefore exceeds the smaller square, contrary to their equality (CN5).

**Step 3.** Applying 1.47 to the two right-angled triangles gives
S(OA) = S(OM) + S(AM),
and
S(OC) = S(ON) + S(CN).
Since OA = OC, Step 2 gives S(OA) = S(OC). Consequently,
S(OM) + S(AM) = S(ON) + S(CN) (CN1).

**Step 4.** Suppose first that AB = CD. Since M and N bisect these chords, AB consists of two copies of AM and CD of two copies of CN. Therefore AM = CN: if either half were greater, its two copies would together exceed the two copies of the other half, contradicting AB = CD (CN2, CN5). Hence S(AM) = S(CN) by Step 2.

**Step 5.** Subtract these equal squares from the equal sums in Step 3. The remaining squares S(OM) and S(ON) are equal (CN3), and therefore OM = ON by Step 2. Since OM and ON are the perpendiculars from the centre to the chords, AB and CD are equally distant from the centre (D3.4).

**Step 6.** Conversely, suppose that AB and CD are equally distant from O. Their perpendiculars OM and ON are then equal (D3.4), so S(OM) = S(ON) by Step 2. Subtracting these from the equality in Step 3 gives S(AM) = S(CN) (CN3), and hence AM = CN by Step 2. Since MB = AM and ND = CN, adding the equal halves gives AB = CD (CN1, CN2).

**Step 7.** The case of chords through the centre also satisfies both conclusions. Such chords are diameters (D1.17); each consists of two radii, so all are equal (D1.15, CN2), and each has zero distance from the centre. A chord XY not through O has positive perpendicular distance, and it is shorter than any diameter: in triangle OXY, XY < OX + OY (1.20), while OX + OY equals a diameter (D1.15, D1.17, CN2). Thus a diameter and a non-diametral chord are neither equal nor equally distant from the centre; two diameters are both equal and equally distant (D3.4).

**Step 8.** Therefore, in a circle, equal straight lines are equally distant from the centre, and straight lines equally distant from the centre are equal to one another (Steps 5–7; D3.4).

**USED:** 1.10, 1.20, 1.3, 1.47, 2.4, 3.3, CN1, CN2, CN3, CN4, CN5, D1.10, D1.15, D1.17, D1.22, D3.4, P1, P4
**Human refs (from References field):** 1.47, 3.1, 3.3, D3.4
**Jaccard:** 0.158 — AI adds ['1.10', '1.20', '1.3', '2.4', 'CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.10', 'D1.15', 'D1.17', 'D1.22', 'P1', 'P4']; Human adds ['3.1']

## Proposition 3.15
**Statement:** Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

**Step 1.** Let O be the centre of the circle, AB any diameter, and CD and EF two non-diametral chords, with CD nearer to the centre than EF. Join OC, OD, and OE. Thus O lies between A and B, while neither CD nor EF passes through O. (P1, D1.17.)

**Step 2.** For the diameter, the direct path is the triangle inequality. Since all radii are equal, AO + OB = OC + OD; and in triangle COD, OC + OD > CD. Therefore AB > CD. The same argument applies to every non-diametral chord. Moreover, all diameters are equal, since each consists of two radii. Hence every diameter is greatest among the chords. (D1.15, D1.17, CN2, 1.20.)

**Step 3.** Bisect CD at M and EF at N, and join OM and ON. By 3.3, OM is perpendicular to CD, and ON is perpendicular to EF. Since CD is nearer to the centre than EF, OM < ON. The chosen path is to bisect first: 3.3 then immediately supplies the perpendicular distances, and the resulting right triangles permit a direct comparison by 1.47. (1.10, P1, 3.3, D3.5.)

**Step 4.** Write □XY for the area of the square on XY. Applying 1.47 to the right triangles OMC and ONE gives
□OM + □MC = □OC,
□ON + □NE = □OE.
The radii OC and OE are equal, so their squares are equal by superposition. Consequently,
□OM + □MC = □ON + □NE. (1.47, D1.15, CN4, CN1.)

**Step 5.** Cut off OT equal to OM from the greater segment ON. Then T lies between O and N. By 2.4,
□ON = □OT + □TN + twice the rectangle contained by OT and TN.
Since □OT = □OM, this says □ON = □OM + K, where K is the positive area consisting of □TN together with that doubled rectangle. Substitute this expression into Step 4 and subtract □OM from the equal wholes. The result is
□MC = □NE + K,
so □MC > □NE. (1.3, 2.4, CN4, CN1, CN3, CN5.)

**Step 6.** Therefore MC > NE. Indeed, if MC = NE, their squares would be equal by superposition. If MC < NE, cutting from NE a part equal to MC and applying 2.4 to that part and the positive remainder would give □NE > □MC. Both alternatives contradict Step 5. (CN4, 1.3, 2.4, CN5.)

**Step 7.** Since M and N are the midpoints, CD is twice MC and EF is twice NE. Doubling MC > NE therefore gives CD > EF: the two positive excesses together remain an excess. Thus, of the non-diametral chords, the nearer to the centre is greater than the more remote; and, by Step 2, the diameter is greatest of all. (1.10, CN2, CN5.)

**USED:** 1.10, 1.20, 1.3, 1.47, 2.4, 3.3, CN1, CN2, CN3, CN4, CN5, D1.15, D1.17, D3.5, P1
**Human refs (from References field):** 1.20, 1.24, 3.14, D3.5
**Jaccard:** 0.118 — AI adds ['1.10', '1.3', '1.47', '2.4', '3.3', 'CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.17', 'P1']; Human adds ['1.24', '3.14']

## Proposition 3.16
**Statement:** The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

**Step 1.** Let AB be a diameter of the circle, with centre O, and let t be the straight line through A perpendicular to AB. Choose either semicircle, and let AT be the ray of t on its side of AB. Then ∠OAT is right. Denote by S the angle of the semicircle at A, bounded by AB and the circumference, and by H the remaining angle between that circumference and AT. [D1.17, D1.18, D1.10, D3.7, D1.8]

**Step 2.** Take any point X on t other than A, and join OX. In triangle OAX, ∠OAX is right. The two-angle inequality gives ∠OXA less than a right angle; hence ∠OAX > ∠OXA, and therefore OX > OA. The direct choice here is the two-angle inequality, since it gives exactly the comparison required without a full angle-sum calculation. [P1, 1.17, P4, 1.19]

**Step 3.** Every point of the circumference has distance OA from O. Every interior point other than O has smaller distance: produce the segment from O through that point to the circumference, and the original segment is a proper part of a radius. Thus OX > OA shows that X is neither on nor inside the circle. Since X was arbitrary on either side of A, the whole perpendicular t, except for A itself, lies outside the circle. [D1.15, P2, CN5; Step 2]

**Step 4.** For the remaining assertions, the chosen route is to construct a chord along every ray strictly inside ∠OAT. Let AR be any such ray. Then ∠OAR is acute, being a proper part of a right angle. Draw OF perpendicular to the straight line containing AR. The foot F is not A, for that would make ∠OAR right. Nor can F lie on the opposite ray from A: in that case ∠OAR would be an exterior angle of triangle OFA and would exceed its right interior angle OFA. Consequently F lies on the ray AR beyond A. [CN5, D1.12, 1.12, D1.10, 1.16]

**Step 5.** Produce AF through F, and take C on this continuation so that FC = FA; join OC. In triangles AFO and CFO, AF = CF, OF is common, and ∠AFO and ∠CFO are equal right angles. Therefore OA = OC by side-angle-side congruence. Hence C is on the given circumference. [P2, 1.3, P1, D1.10, P4, 1.4, D1.15]

**Step 6.** Since A and C are on the circumference, the chord AC, apart from its endpoints, lies inside the circle. Moreover, it lies in the chosen semicircle because its ray AR is on that side of AB. Thus every ray strictly inside ∠OAT enters the semicircle immediately from A. Any straight line interposed at A between AT and the circumference would have to issue along such a ray, yet remain outside the semicircle. This is impossible. Therefore no straight line can be interposed in the stated space. [3.2, D1.18; Steps 4–5]

**Step 7.** Let α be any acute rectilineal angle. At A, on AO and toward AT, construct a ray AR such that ∠OAR = α. Since α is acute, this ray lies strictly inside ∠OAT. By Steps 4–6 it contains a chord AC whose interior lies inside the semicircle. At A, therefore, the rectilineal angle OAC is a proper part of the angle S bounded by the diameter and the circumference. Hence S > ∠OAC = α. The angle of the semicircle is consequently greater than every acute rectilineal angle. [1.23, D1.12, D3.7, 3.2, CN5]

**Step 8.** Again let α be any acute rectilineal angle. This time construct AR from AT toward AO so that ∠TAR = α. This ray also lies strictly inside ∠OAT and, by Steps 4–6, contains an interior chord AC. At A the circumference lies between AT and this interior chord, so H is a proper part of the rectilineal angle TAC. Therefore H < ∠TAC = α. Thus the remaining angle is less than every acute rectilineal angle. Since either semicircle could have been chosen, this conclusion, together with Steps 3 and 6, proves all the assertions. [1.23, D1.12, D1.8, 3.2, CN5]

**USED:** 1.12, 1.16, 1.17, 1.19, 1.23, 1.3, 1.4, 3.2, CN5, D1.10, D1.12, D1.15, D1.17, D1.18, D1.8, D3.7, P1, P2, P4
**Human refs (from References field):** 1.17, 1.19, 1.5
**Jaccard:** 0.100 — AI adds ['1.12', '1.16', '1.23', '1.3', '1.4', '3.2', 'CN5', 'D1.10', 'D1.12', 'D1.15', 'D1.17', 'D1.18', 'D1.8', 'D3.7', 'P1', 'P2', 'P4']; Human adds ['1.5']

## Proposition 3.17
**Statement:** From a given point to draw a straight line touching a given circle.

**Step 1.** Let Γ be the given circle and A the given point. The admissible cases are that A lies outside Γ or on its circumference: a straight line through an interior point cuts the circle and therefore cannot touch it (D3.2). Find the centre O of Γ (3.1).

**Step 2.** First suppose A lies outside Γ. Join OA, and let B be its intersection with Γ between O and A (P1). Describe the auxiliary circle Σ with centre O and radius OA (P3). Since OB is a proper part of OA, OB < OA; thus B lies inside Σ (CN5, D1.15).

**Step 3.** At B draw a perpendicular to OA, and produce it to meet Σ at C (1.11, P2). Join OC, let D be its intersection with Γ between O and C, and join AD (P1).

**Step 4.** We have OB = OD, since both are radii of Γ, and OC = OA, since both are radii of Σ (D1.15). Moreover, ∠BOC = ∠DOA: these angles coincide because the rays OB and OA coincide, as do the rays OC and OD (CN4). Consequently, triangles OBC and ODA have two corresponding sides and their included angles equal, so ∠OBC = ∠ODA (1.4). This is the chosen path: the included central angle is already common, making the side–angle–side criterion 1.4 the directly applicable congruence proposition.

**Step 5.** Since BC is perpendicular to OA, ∠OBC is right; hence the equal angle ODA is right, and AD is perpendicular to OD (D1.10). Produce DO through O to the opposite circumference of Γ, thereby completing a diameter with extremity D (P2, D1.17). The straight line AD is perpendicular to this diameter at D, so it falls outside Γ except at D (3.16). Therefore AD touches Γ at D (D3.2).

**Step 6.** If instead A lies on the circumference of Γ, join OA and extend its straight line as needed; the segment it cuts off in Γ is a diameter with extremity A (P1, P2, D1.17). Draw through A a perpendicular to this diameter (1.11). This perpendicular falls outside Γ except at A, and therefore touches Γ at A (3.16, D3.2). Thus, in either admissible case, a straight line touching the given circle has been drawn from the given point.

**USED:** 1.11, 1.4, 3.1, 3.16, CN4, CN5, D1.10, D1.15, D1.17, D3.2, P1, P2, P3
**Human refs (from References field):** 1.4, 3.1, 3.16
**Jaccard:** 0.231 — AI adds ['1.11', 'CN4', 'CN5', 'D1.10', 'D1.15', 'D1.17', 'D3.2', 'P1', 'P2', 'P3']

## Proposition 3.18
**Statement:** If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.

**Step 1.** Let the straight line ℓ touch the circle at A, and let O be the centre. Join OA (P1). The centre O is within the circle (D1.15, D1.16), whereas a tangent does not enter its interior, since it meets but does not cut the circle (D3.2). Thus O is not on ℓ.

**Step 2.** Suppose that OA is not perpendicular to ℓ. Draw OF perpendicular to ℓ, with F on ℓ (1.12). Then F is different from A, and ∠OFA is right (D1.10). Our chosen route is to compare sides of this right triangle.

**Step 3.** The point F cannot lie within the circle, because ℓ does not cut it (D3.2). Nor can F lie on its circumference: otherwise the segment AF would lie within the circle (3.2), again contradicting tangency (D3.2). Therefore F lies outside the circle.

**Step 4.** Since O is inside and F outside, let C be the point where the segment OF meets the circumference on passing out of the circle; thus C lies between O and F (D1.15, D1.16). Consequently OF is greater than OC (CN5). But OC equals OA, since both are drawn from the centre to the circumference (D1.15). Hence OF is greater than OA.

**Step 5.** In triangle OAF, the angles OFA and OAF together are less than two right angles (1.17). Since ∠OFA is right, ∠OAF is less than ∠OFA (P4). Here 1.17 is the natural choice because only these two angles need comparison, rather than the full triangle-angle sum. The side opposite the greater angle is greater (1.19); therefore OA is greater than OF.

**Step 6.** Steps 4 and 5 contradict one another. Thus the supposition in Step 2 is false: OA is perpendicular to ℓ. Therefore the straight line joined from the centre to the point of contact is perpendicular to the tangent (D1.10).

**USED:** 1.12, 1.17, 1.19, 3.2, CN5, D1.10, D1.15, D1.16, D3.2, P1, P4
**Human refs (from References field):** 1.17, 1.19
**Jaccard:** 0.182 — AI adds ['1.12', '3.2', 'CN5', 'D1.10', 'D1.15', 'D1.16', 'D3.2', 'P1', 'P4']

## Proposition 3.19
**Statement:** If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so drawn.

**Step 1.** Let the straight line t touch the circle at T, let n be the given straight line through T perpendicular to t, and let O be the centre. The angles made by the given perpendicular with t are right angles (hypothesis; D1.10).

**Step 2.** Join OT (P1). Since t touches the circle at T, OT is perpendicular to t (3.18). This is the direct path: 3.18 applies immediately to the given tangent, leaving only collinearity to establish.

**Step 3.** Produce the given perpendicular through T (P2), and choose B on it on the opposite side of t from O. Choose A on t distinct from T. Both ∠OTA and ∠ATB are right angles, since OT and n are perpendicular to t (D1.10). Thus these adjacent angles together equal two right angles, and TO and TB lie on opposite sides of the straight line TA.

**Step 4.** Apply 1.14, whose straight-line criterion is exactly the configuration just obtained: TO and TB lie in one straight line. Since TB lies on n, O also lies on n. Therefore the centre of the circle lies on the straight line drawn from the point of contact at right angles to the tangent.

**USED:** 1.14, 3.18, D1.10, P1, P2
**Human refs (from References field):** 3.18
**Jaccard:** 0.200 — AI adds ['1.14', 'D1.10', 'P1', 'P2']

## Proposition 3.20
**Statement:** In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.

**Step 1.** Let O be the centre of the circle, let A and B be the endpoints of the common base arc Γ, and let C lie on the other arc AB. Write φ = ∠ACB, and let θ be the angle at O standing on Γ, taking its opening toward that arc. We must prove θ = 2φ, where twice an angle means that angle added to itself. [D3.9, D3.10]

**Step 2.** Join OA, OB, OC, CA, and CB. Produce CO through O to meet the circumference again at D; thus CD is a diameter and C, O, D occur in that order. The chosen route is to use this diameter to obtain an exact doubling from an exterior angle, and then combine the resulting equalities by addition or subtraction. [P1, P2, D1.17]

**Step 3.** Take X to be either A or B, provided X ≠ D. Since OC = OX, the base angles of triangle OCX are equal: ∠OCX = ∠CXO. [D1.15, 1.5] Because OD is the continuation of CO, the exterior-angle equality gives
∠XOD = ∠OCX + ∠CXO = 2∠OCX = 2∠XCD.
Here the last equality holds because CO and CD are the same ray from C. The exterior-angle form of 1.32 is the direct choice because the required side has already been produced. [1.32, CN2, CN4]

**Step 4.** If D coincides with A, apply Step 3 with X = B. The angle ∠BOD is precisely θ, and ∠BCD is precisely φ; hence θ = 2φ. If D coincides with B, the same conclusion follows by taking X = A. [Step 3, D3.9, D3.10, CN4]

**Step 5.** Suppose D lies strictly within Γ. Then CD divides the circumference angle into ∠ACD and ∠DCB, while OD divides the central opening standing on Γ into ∠AOD and ∠DOB. Thus
φ = ∠ACD + ∠DCB,
θ = ∠AOD + ∠DOB.
These are the corresponding angle decompositions along the two subarcs AD and DB of Γ. [D3.9, D3.10] Adding the two equalities obtained in Step 3 therefore gives
θ = 2∠ACD + 2∠DCB = 2φ. [Step 3, CN2]

**Step 6.** Finally, suppose D lies outside Γ and is distinct from A and B. Interchange the names A and B if necessary so that, on the arc from D to B which avoids C, A lies between D and B. At C, the angle ∠DCA is then a part of ∠DCB, with remainder φ; at O, the angle ∠DOA is a part of ∠DOB, with remainder θ. Consequently,
φ = ∠DCB − ∠DCA,
θ = ∠DOB − ∠DOA. [D3.9, D3.10]
By Step 3, ∠DOB = 2∠DCB and ∠DOA = 2∠DCA. Subtracting gives
θ = 2∠DCB − 2∠DCA = 2φ. [Step 3, CN2, CN3]

**Step 7.** The endpoint, interior, and exterior positions of D exhaust the possibilities. In every case θ = 2φ. Therefore, in a circle, the angle at the centre is double the angle at the circumference when they stand on the same circumference as base. [Steps 4–6]

**USED:** 1.32, 1.5, CN2, CN3, CN4, D1.15, D1.17, D3.10, D3.9, P1, P2
**Human refs (from References field):** 1.32, 1.5
**Jaccard:** 0.182 — AI adds ['CN2', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D3.10', 'D3.9', 'P1', 'P2']

## Proposition 3.21
**Statement:** In a circle the angles in the same segment are equal to one another.

**Step 1.** Let AB be the base of a segment of a circle, and let C and D be any two points, other than A and B, on the circumference bounding that segment. Join AC, BC, AD, and BD. The angles to be compared are ∠ACB and ∠ADB. [D3.6, D3.8, P1]

**Step 2.** Let Γ be the other arc from A to B, namely the arc not containing C or D. Both ∠ACB and ∠ADB stand upon Γ. We therefore choose the direct route through 3.20: compare both angles with the central angular magnitude over their common arc. [D3.9, 3.20]

**Step 3.** Find the centre O and join OA and OB. If Γ is smaller than a semicircle, let Θ be the central angle over Γ. Otherwise, draw two distinct diameters through O and divide Γ at their endpoints lying on it; each resulting subarc is smaller than a semicircle. Join its endpoints to O, C, and D, and let Θ be the sum of the central angles over these subarcs. This subdivision avoids treating a straight or reflex angular magnitude as a single rectilineal angle. [3.1, P1, P2, D1.17]

**Step 4.** By 3.20, the central angle over Γ, or over each of its subarcs, is double the angle at C standing upon that same arc, and also double the corresponding angle at D. In the subdivided case, the component angles at C together constitute ∠ACB, and those at D together constitute ∠ADB. Adding the equalities therefore gives, in either case,
Θ = ∠ACB + ∠ACB,
Θ = ∠ADB + ∠ADB.
Consequently, ∠ACB + ∠ACB = ∠ADB + ∠ADB. [D3.9, 3.20, CN2, CN1]

**Step 5.** These equal doubles have equal halves. Indeed, if either original angle exceeded the other by a positive angular magnitude, its double would equal the other's double together with two copies of that excess, and so would be greater, contrary to Step 4. Hence ∠ACB = ∠ADB. Since C and D were arbitrary, the angles in the same segment of a circle are equal to one another. [CN2, CN5, D3.8]

**USED:** 3.1, 3.20, CN1, CN2, CN5, D1.17, D3.6, D3.8, D3.9, P1, P2
**Human refs (from References field):** 3.20
**Jaccard:** 0.091 — AI adds ['3.1', 'CN1', 'CN2', 'CN5', 'D1.17', 'D3.6', 'D3.8', 'D3.9', 'P1', 'P2']

## Proposition 3.22
**Statement:** The opposite angles of quadrilaterals in circles are equal to two right angles.

**Step 1.** Let ABCD be a quadrilateral inscribed in a circle, with its vertices named in their order around the circumference. Join AC and BD. [D4.3; P1]

**Step 2.** The direct route is to use angles in the same segment, since the diagonals immediately supply such angle pairs without requiring a centre construction. The angles BAC and BDC lie in the same segment on chord BC, and the angles BCA and BDA lie in the same segment on chord BA. Hence
∠BAC = ∠BDC,
∠BCA = ∠BDA. [D3.8; 3.21]

**Step 3.** Adding these equalities gives
∠BAC + ∠BCA = ∠BDC + ∠BDA.
Since BD divides the interior angle ADC, the two angles on the right together coincide with ∠ADC. Thus
∠BAC + ∠BCA = ∠ADC. [CN2; CN4]

**Step 4.** In triangle ABC,
∠ABC + ∠BAC + ∠BCA = two right angles. [1.32]
Adding ∠ABC to the equality in Step 3 and comparing with this triangle-angle sum yields
∠ABC + ∠ADC = two right angles. [CN2; CN1]

**Step 5.** The angles CBD and CAD lie in the same segment on chord CD, so ∠CBD = ∠CAD. [D3.8; 3.21]
Together with ∠BDC = ∠BAC from Step 2, this gives
∠CBD + ∠BDC = ∠CAD + ∠BAC = ∠BAD,
because AC divides the interior angle BAD. [CN2; CN4]

**Step 6.** In triangle BCD,
∠BCD + ∠CBD + ∠BDC = two right angles. [1.32]
Adding ∠BCD to the equality in Step 5 therefore gives
∠BCD + ∠BAD = two right angles. [CN2; CN1]
Thus each pair of opposite angles of the inscribed quadrilateral is together equal to two right angles, as required.

**USED:** 1.32, 3.21, CN1, CN2, CN4, D3.8, D4.3, P1
**Human refs (from References field):** 1.32, 3.21
**Jaccard:** 0.250 — AI adds ['CN1', 'CN2', 'CN4', 'D3.8', 'D4.3', 'P1']

## Proposition 3.23
**Statement:** On the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.

**Step 1.** Suppose, for a contradiction, that two similar but unequal segments of circles are constructed on the same straight line AB and on the same side of it. Each segment is bounded by AB and a circular arc (D3.6). Their circles must be distinct: otherwise the arcs on the specified side, and hence the segments, would coincide and be equal (D3.6, CN4).

**Step 2.** The circles already have A and B in common, so their arcs cannot cross at any further point (3.10). Consequently, the segments on the specified side of AB are nested. Relabel them as the inner and outer segments. Since they are unequal, choose a point D, other than A and B, on the inner arc and strictly inside the outer segment (D3.6).

**Step 3.** Join AD and produce it beyond D until it meets the outer arc at C; join DB and CB (P1, P2). Thus A, D, C lie on one straight line in that order. This secant construction makes an exterior-angle comparison directly available.

**Step 4.** The angle ADB is an angle in the inner segment, and ACB is an angle in the outer segment (D3.8). Since the two segments are similar, ∠ADB = ∠ACB (D3.11).

**Step 5.** In triangle DBC, the side CD is produced through D to A. Therefore its exterior angle ADB is greater than its interior opposite angle DCB (1.16, the direct choice because the construction supplies an exterior angle). But the rays CD and CA coincide, so ∠DCB = ∠ACB (CN4). Hence ∠ADB > ∠ACB, contradicting Step 4. Therefore, on the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.

**USED:** 1.16, 3.10, CN4, D3.11, D3.6, D3.8, P1, P2
**Human refs (from References field):** 1.16, D3.11
**Jaccard:** 0.250 — AI adds ['3.10', 'CN4', 'D3.6', 'D3.8', 'P1', 'P2']

## Proposition 3.24
**Statement:** Similar segments of circles on equal straight lines are equal to one another.

**Step 1.** Let S and T be similar segments of circles on the equal straight lines AB and DE, respectively. Their boundaries consist of their bases and the corresponding circular arcs, and the angles in the two segments are equal. We use superposition to bring their bases together, making 3.23 directly applicable. [D3.6, D3.11]

**Step 2.** Superpose T so that D falls on A and DE lies along AB, with the segment on the same side of AB as S. Since DE = AB, E falls on B. Call the placed segment T′. Superposition leaves the figure and its angles unchanged; thus T′ equals T and remains similar to S. [CN4, D3.11]

**Step 3.** The segments S and T′ are now similar segments on the same straight line AB and on the same side of it. They cannot be unequal, since two similar and unequal segments cannot be constructed on the same straight line and on the same side. Therefore S equals T′. [3.23]

**Step 4.** Since S equals T′ and T′ equals T, S equals T. Therefore similar segments of circles on equal straight lines are equal to one another. [CN1]

**USED:** 3.23, CN1, CN4, D3.11, D3.6
**Human refs (from References field):** 3.10
**Jaccard:** 0.000 — AI adds ['3.23', 'CN1', 'CN4', 'D3.11', 'D3.6']; Human adds ['3.10']

## Proposition 3.25
**Statement:** Given a segment of a circle, to describe the complete circle of which it is a segment.

**Step 1.** Let AB be the straight boundary of the given segment, and choose a third point C on its circular boundary. By D3.6, that boundary belongs to some circle Γ; this circle is used only to verify the construction, not as an already constructed figure. The points A, B, C are not collinear: otherwise the middle one would lie within Γ by 3.2 applied to the outer two, although it lies on the circumference. **Path choice:** use the centre–chord theorem 3.3, which applies directly to perpendicular bisectors and avoids separate cases for different sizes of segment. [D3.6, 3.2]

**Step 2.** Join AC. Bisect AB at M and AC at N. Through M draw the straight line ℓ perpendicular to AB, and through N draw the straight line m perpendicular to AC, producing these lines as necessary. These constructions use only points and straight lines available from the given segment. [P1, 1.10, 1.11, P2]

**Step 3.** Let O denote the centre of Γ. We show that O lies on ℓ. If O lies on AB, the equal radii OA and OB imply that O is its midpoint M: O cannot lie beyond either endpoint, since then one radius would properly contain the other. Thus O lies on ℓ. [D1.15, D1.16, CN5]

If O does not lie on AB, join OM. This line passes through the centre and bisects the chord AB, so it is perpendicular to AB by 3.3. Therefore it coincides with ℓ. Indeed, distinct perpendiculars at M would, on the same side of AB, give two right angles one properly containing the other, contrary to the equality of all right angles and the whole being greater than its part. Thus again O lies on ℓ. Applying exactly the same argument to AC and its midpoint N shows that O also lies on m. [P1, 3.3, D1.10, P4, CN5]

**Step 4.** The midpoints M and N are distinct, since otherwise the straight lines AB and AC would have both A and their midpoint in common, contrary to the noncollinearity of A, B, C. The lines ℓ and m are also distinct: if they coincided, AB and AC would both be perpendicular to the same transversal at distinct points, and hence would be parallel by 1.28; but they meet at A. [D1.4, 1.28, D1.23]

Since ℓ and m are distinct and both contain O, they meet at that point. Produce them to their intersection X. Their intersection is unique, so X = O. The centre has therefore been constructed from the given segment alone. [P2, D1.4]

**Step 5.** With centre X and distance XA describe a circle. Since X = O and A lies on Γ, this circle has precisely the centre and radius of Γ and is therefore the complete circle whose circumference contains the given arc. Together with AB, that arc bounds the original segment. Thus the complete circle of which the given figure is a segment has been described. [P3, D1.15, D1.16, D3.6]

**USED:** 1.10, 1.11, 1.28, 3.2, 3.3, CN5, D1.10, D1.15, D1.16, D1.23, D1.4, D3.6, P1, P2, P3, P4
**Human refs (from References field):** 1.6, 3.9
**Jaccard:** 0.000 — AI adds ['1.10', '1.11', '1.28', '3.2', '3.3', 'CN5', 'D1.10', 'D1.15', 'D1.16', 'D1.23', 'D1.4', 'D3.6', 'P1', 'P2', 'P3', 'P4']; Human adds ['1.6', '3.9']

## Proposition 3.26
**Statement:** In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

**Step 1.** Let the equal circles have centres O and P, and let Γ and Δ be the circumferences intercepted by the angles under comparison, with endpoints A, B and D, E respectively. If the given angles are at the circumferences, call their vertices C and F. If the given angles are at the centres, choose C and F on the arcs complementary to Γ and Δ. Draw the chords AB, DE, the radii OA, OB, PD, PE, and the lines CA, CB, FD, FE (P1). Thus α = ∠ACB and β = ∠DFE stand on Γ and Δ respectively (D3.8, D3.9).

**Step 2.** Write Φ and Ψ for the central openings standing on Γ and Δ respectively, taking the opening towards the specified arc, including the reflex opening when that arc is greater than a semicircle. By 3.20, Φ is double α and Ψ is double β. Consequently, either hypothesis of the proposition gives both Φ = Ψ and α = β. Equal inscribed angles give equal doubles by CN2; equal central openings give equal halves, since otherwise doubling the greater half would give a greater whole, contrary to their equality (CN2, CN5).

**Step 3.** Since the circles are equal, their radii are equal; in particular OA = PD and OB = PE (D1.15, D3.1). We shall use these two pairs of equal sides and the equal included angles to obtain equal chords by SAS. This is the direct route because the central-angle equality is already available.

**Step 4.** If Φ and Ψ are not straight openings, the ordinary included angles of triangles OAB and PDE are equal. Indeed, for openings smaller than a straight angle they are Φ and Ψ themselves; for reflex openings they are the respective remainders from a full turn. These full turns are equal: producing the radii through the centres (P2) and applying 1.13 on both sides gives four right angles at either centre, equal by P4 and CN2. Subtracting Φ = Ψ therefore gives equal remaining angles (CN3). Hence AB = DE by SAS (1.4). If Φ and Ψ are straight openings, AB and DE pass through their centres and are diameters, so again AB = DE (D1.17, D3.1).

**Step 5.** Consider the circular segments bounded by AB and the arc through C, and by DE and the arc through F (D3.6). Their angles α and β are equal by Step 2, so these segments are similar (D3.8, D3.11). Their bases are equal by Step 4; therefore the segments are equal by 3.24. Their corresponding circular boundaries—the arcs through C and F—accordingly coincide upon superposition and are equal (CN4). We compare these segments because their similarity follows directly from the equal circumferential angles.

**Step 6.** The complete circumferences of the two equal circles are equal: their centres can be superposed, and their equal radii then make their circular boundaries coincide (D3.1, D1.15, CN4). Subtract the equal arcs through C and F established in Step 5. The remaining circumferences Γ and Δ are equal (CN3). These are precisely the circumferences on which the angles under comparison stand (D3.9). Thus, in equal circles, equal angles stand on equal circumferences, whether the angles are at the centres or at the circumferences.

**USED:** 1.13, 1.4, 3.20, 3.24, CN2, CN3, CN4, CN5, D1.15, D1.17, D3.1, D3.11, D3.6, D3.8, D3.9, P1, P2, P4
**Human refs (from References field):** 1.4, 3.24, D3.11
**Jaccard:** 0.167 — AI adds ['1.13', '3.20', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.17', 'D3.1', 'D3.6', 'D3.8', 'D3.9', 'P1', 'P2', 'P4']

## Proposition 3.27
**Statement:** In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.

**Step 1.** Let two equal circles have equal specified arcs AB and CD. Take arbitrary points P and Q on their respective complementary arcs, and join PA, PB, QC, and QD [P1]. Thus ∠APB and ∠CQD stand on the given equal arcs [D3.9]. Path choice: use the immediately preceding implication, 3.26, by contradiction at the circumferences; then obtain the central case by doubling with 3.20, avoiding a separate argument about halves.

**Step 2.** Suppose ∠APB and ∠CQD are unequal. Interchanging the names of the circles if necessary, suppose ∠APB is greater. At P construct an angle equal to ∠CQD with PA as one side and its other side strictly inside ∠APB [1.23]. Extend this other side to meet the specified arc AB at E [P2]. Since this ray lies strictly between PA and PB, E lies strictly between A and B on that arc. Consequently, the arc AE cut off by ∠APE is a proper part of the specified arc AB [D3.9].

**Step 3.** By construction, ∠APE = ∠CQD. These are angles at the circumferences of equal circles; therefore the arcs AE and CD on which they stand are equal [3.26].

**Step 4.** But arc AB equals arc CD by hypothesis. Hence arc AE equals arc AB [CN1], although arc AE is a proper part of arc AB. This contradicts the fact that the whole is greater than the part [CN5]. Therefore ∠APB = ∠CQD. Since P and Q were arbitrary, the required equality holds for angles at the circumferences.

**Step 5.** Let O and R be the respective centres, and join OA, OB, RC, and RD [P1]. Denote by θ and φ the central angles standing on the specified arcs AB and CD, respectively. Since each central angle and its corresponding circumferential angle stand on the same arc, θ is double ∠APB, and φ is double ∠CQD [3.20].

**Step 6.** Adding the equal angles established in Step 4 to themselves gives ∠APB + ∠APB = ∠CQD + ∠CQD [CN2]. Thus θ = φ [CN1]. Therefore, in equal circles, angles standing on equal circumferences are equal to one another, both at the centres and at the circumferences.

**USED:** 1.23, 3.20, 3.26, CN1, CN2, CN5, D3.9, P1, P2
**Human refs (from References field):** 1.23, 3.20, 3.26
**Jaccard:** 0.333 — AI adds ['CN1', 'CN2', 'CN5', 'D3.9', 'P1', 'P2']

## Proposition 3.28
**Statement:** In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

**Step 1.** Let AB and CD be equal chords of two equal circles. Find their centres O and P (3.1). Equal circles have equal radii; consequently, when their centres are superposed, their circumferences coincide. Their complete circumferences are therefore equal (D3.1, D1.15, CN4).

**Step 2.** First dispose of the diameter case. If AB is a diameter, then CD equals a diameter of its own circle, because the circles have equal diameters (D3.1, CN1). Since every nondiameter chord is less than a diameter, CD must also be a diameter (3.15). The same reasoning applies if CD is initially a diameter. The arcs cut off are then semicircumferences (D1.17, D1.18), and superposing the circles with their diameters aligned makes corresponding semicircumferences coincide; hence they are equal (D1.15, CN4). Thus this case is settled. Assume henceforth that neither chord is a diameter.

**Step 3.** Join OA, OB, PC, and PD (P1). Since these are radii of equal circles, OA = PC and OB = PD (D1.15, D3.1). Also AB = CD by hypothesis.

**Step 4.** The triangles OAB and PCD therefore have their three corresponding sides equal. Hence ∠AOB = ∠CPD (1.8). We choose the central-angle route because these equal angles follow immediately from the three side equalities.

**Step 5.** These central angles stand on the respective lesser arcs cut off by AB and CD (D3.9). In equal circles equal central angles stand on equal circumferences; therefore the lesser arc AB equals the lesser arc CD (3.26).

**Step 6.** Subtract these equal lesser arcs from the equal complete circumferences established in Step 1. The remaining greater arcs are equal (CN3). Thus equal straight lines in equal circles cut off equal circumferences, the greater equal to the greater and the less to the less.

**USED:** 1.8, 3.1, 3.15, 3.26, CN1, CN3, CN4, D1.15, D1.17, D1.18, D3.1, D3.9, P1
**Human refs (from References field):** 1.8, 3.26
**Jaccard:** 0.154 — AI adds ['3.1', '3.15', 'CN1', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D1.18', 'D3.1', 'D3.9', 'P1']

## Proposition 3.29
**Statement:** In equal circles equal circumferences are subtended by equal straight lines.

**Step 1.** Let equal arcs with endpoints A, B and C, D be given in two equal circles. Draw the subtending straight lines AB and CD, and find the centres O and Q of the respective circles. We must prove AB = CD. [P1; 3.1]

**Step 2.** The whole circumferences of the two circles are equal, as are their semicircumferences: when the centres and corresponding radii are superposed, the respective circumferences and semicircumferences coincide, since the radii are equal. Consequently, the given equal arcs are either both semicircular, both less than semicircumferences, or both greater than semicircumferences; otherwise one would equal a proper part of the other after superposition. [D3.1; D1.15; D1.17; CN4; CN5]

**Step 3.** If the given arcs are semicircumferences, AB and CD are diameters and hence are equal. If the given arcs are greater than semicircumferences, subtract them from the equal whole circumferences: the remaining minor arcs are equal and have the same endpoints, so their subtending straight lines are still AB and CD. It therefore remains only to prove the result for equal minor arcs. [D1.17; D3.1; CN3]

**Step 4.** Join OA, OB, QC, and QD. These are radii of the equal circles, so OA = QC and OB = QD. [P1; D1.15; D3.1]

**Step 5.** The angles AOB and CQD stand at the centres upon the equal minor arcs. Therefore ∠AOB = ∠CQD. This is the direct path: the centre form of 3.27 supplies precisely the included-angle equality needed between the equal pairs of radii. [3.27]

**Step 6.** In triangles AOB and CQD, the two sides OA, OB equal QC, QD respectively, and their included angles are equal. Hence their bases AB and CD are equal by side–angle–side. Together with Step 3, this proves that in equal circles equal circumferences are subtended by equal straight lines. [1.4]

**USED:** 1.4, 3.1, 3.27, CN3, CN4, CN5, D1.15, D1.17, D3.1, P1
**Human refs (from References field):** 1.4, 3.27
**Jaccard:** 0.200 — AI adds ['3.1', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.17', 'D3.1', 'P1']

## Proposition 3.30
**Statement:** To bisect a given circumference.

**Step 1.** Let the given circumference be an arc with extremities A and B. Join AB and bisect it at D, so that AD = DB. Since AB lies within the circle, D is an interior point. [P1, 1.10, 3.2]

**Step 2.** At D draw a perpendicular to AB toward the given arc, producing it if necessary to meet that arc at C. Join AC and BC. [1.11, P2, P1]

**Step 3.** In triangles ADC and BDC, AD = DB, DC is common, and the angles ADC and BDC are right angles and therefore equal. Hence the triangles have two sides and their included angles respectively equal, so ∠DAC = ∠DBC. [Step 1, CN4, D1.10, P4, 1.4]

**Step 4.** Since D lies between A and B, ∠DAC coincides with ∠BAC, and ∠DBC coincides with ∠ABC. Thus ∠BAC = ∠ABC. The former stands upon the portion BC of the given arc, and the latter upon its portion AC. [Step 3, CN4, D3.9]

**Step 5.** Apply 3.26 to these equal angles at the circumference of the same circle, which is equal to itself. The equal-angle route is the direct choice because the triangle comparison already supplies its hypothesis, without a further chord-to-arc inference. Therefore the portions BC and AC of the given circumference are equal. Consequently C bisects the given circumference, as required. [CN4, 3.26]

**USED:** 1.10, 1.11, 1.4, 3.2, 3.26, CN4, D1.10, D3.9, P1, P2, P4
**Human refs (from References field):** 1.4, 3.28
**Jaccard:** 0.083 — AI adds ['1.10', '1.11', '3.2', '3.26', 'CN4', 'D1.10', 'D3.9', 'P1', 'P2', 'P4']; Human adds ['3.28']

## Proposition 3.31
**Statement:** In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

**Step 1.** Let AC be any chord of the given circle which is not a diameter. Find the centre O, and produce CO through O to meet the circumference at B; thus BC is a diameter and O lies between B and C. Join AB and AO, and produce BA beyond A to E. (3.1, P1, P2, D1.17.)

**Step 2.** The radii OA, OB, and OC are equal. Therefore the isosceles triangles AOB and AOC give ∠BAO = ∠ABO and ∠OAC = ∠ACO. Since O lies between B and C, these base angles coincide respectively with ∠ABC and ∠ACB. Also AO divides ∠BAC. Adding the equal angles therefore gives
∠BAC = ∠ABC + ∠ACB.
(D1.15, 1.5, CN4, CN2.)

**Step 3.** Use the exterior-angle theorem here because the extension AE supplies an adjacent angle directly: in triangle ABC, ∠CAE = ∠ABC + ∠ACB. Hence ∠CAE = ∠BAC. These are equal adjacent angles made by AC standing on the straight line BAE, so both are right angles. Write R for a right angle. Since BC may be any diameter and A any point on either semicircular circumference other than its endpoints, every angle in a semicircle is right. (1.32, CN1, D1.10, P4, D1.18, D3.8.)

**Step 4.** Let S be the segment bounded by AC and the arc AC which does not contain B, and let G be the complementary segment. That arc AC is a proper part of the semicircular arc from C to B through A. Thus S is properly contained in that semicircle, whereas G properly contains the opposite semicircle. Consequently S is the less segment and G the greater segment. (D1.17, D1.18, D3.6, CN5.)

**Step 5.** For the greater segment, the equality already obtained in Steps 2–3 gives ∠ABC + ∠ACB = R. Hence ∠ABC < R. This is an angle in G, and every other angle in G equals it. Therefore every angle in the greater segment is less than a right angle. (CN5, D3.8, 3.21.)

**Step 6.** Take any point D on the arc AC bounding S, other than its endpoints, and join AD and CD. The quadrilateral ABCD is inscribed in the circle, so its opposite angles satisfy ∠ABC + ∠ADC = 2R. Since ∠ABC < R, subtraction gives ∠ADC = R + (R − ∠ABC) > R. Since D was arbitrary, every angle in the less segment is greater than a right angle. (P1, 3.22, CN3, CN5, D3.8.)

**Step 7.** Now consider the angle *of* G at A, namely the angle contained by AC and the circumference proceeding from A towards B. The chord AB, apart from its endpoints, lies inside the circle and on the G-side of AC. Thus AB lies inside this segment angle, and the rectilineal angle CAB is a proper part of it. But ∠CAB = R by Step 3. Therefore the angle of the greater segment is greater than a right angle. (3.2, D3.7, CN5.)

**Step 8.** The arc AC bounding S lies on the side of AC opposite B. Apart from A, it also lies on the C-side of AB: it cannot cross AB, since it avoids B, and any third intersection of AB with the circumference would place a circumference point in the interior of a chord, contrary to 3.2. These two sides of the lines bound precisely the angular region CAE. Consequently the angle of S at A, contained by AC and this arc, is a proper part of ∠CAE. Since ∠CAE = R by Step 3, the angle of the less segment is less than a right angle. (3.2, D3.6, D3.7, CN5.)

**Step 9.** The chord AC was arbitrary, and either endpoint could have been named A, so the segment-angle comparisons hold at either endpoint of every nondiametral chord. Together, Steps 3, 5, 6, 7, and 8 establish all the assertions: the angle in a semicircle is right; an angle in a greater segment is less than a right angle; an angle in a less segment is greater than a right angle; the angle of a greater segment is greater than a right angle; and the angle of a less segment is less than a right angle. (D3.7, D3.8.)

**USED:** 1.32, 1.5, 3.1, 3.2, 3.21, 3.22, CN1, CN2, CN3, CN4, CN5, D1.10, D1.15, D1.17, D1.18, D3.6, D3.7, D3.8, P1, P2, P4
**Human refs (from References field):** 1.17, 1.32, 1.5, 3.22, D1.10
**Jaccard:** 0.182 — AI adds ['3.1', '3.2', '3.21', 'CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.17', 'D1.18', 'D3.6', 'D3.7', 'D3.8', 'P1', 'P2', 'P4']; Human adds ['1.17']

## Proposition 3.32
**Statement:** If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

**Step 1.** Let the straight line XAY touch the circle at A, and let AB be the straight line drawn from A across the circle to B. Find the centre O, join AO, and produce AO beyond O to meet the circumference at C (3.1; P1; P2). Then AC is a diameter (D1.17). Since OA is perpendicular to the tangent, both ∠XAC and ∠CAY are right angles (3.18; D1.10). **Path choice:** the radius already drawn makes 3.18 directly applicable, and the resulting diameter allows us to use the angle in a semicircle.

**Step 2.** If B = C, both angles made by AB with the tangent are right by Step 1. Every angle in either semicircle with base AB is also right (3.31). Hence the required equalities hold in this case (P4). Henceforth suppose B ≠ C.

**Step 3.** Interchange the names X and Y, if necessary, so that AB lies inside the right angle XAC. This is possible because the chords AB and AC lie within the circle, whereas the tangent does not cut it (3.2; D3.2). Thus X and C lie on opposite sides of AB, while Y and C lie on the same side. Join BC (P1). Since AC is a diameter, ∠ABC is an angle in a semicircle and is therefore right (3.31).

**Step 4.** The three angles of triangle ABC equal two right angles (1.32). Subtracting the right angle ABC shows that ∠BAC + ∠ACB equals one right angle (P4; CN3). Also, ∠XAB + ∠BAC is the right angle XAC. Subtracting the common angle BAC from these equal right angles gives
∠XAB = ∠ACB.
(P4; CN3.)

**Step 5.** Every angle ADB whose vertex D lies on the arc AB containing C equals ∠ACB, because these are angles in the same segment (3.21). Consequently,
∠XAB = ∠ADB
(CN1). This is the required equality for the tangent ray AX: the segment containing C lies on the opposite side of AB from X, and ∠ADB is an angle in that segment (Step 3; D3.8).

**Step 6.** Take any point E on the other arc AB, and join AE and BE (P1). The quadrilateral AEBC is inscribed in the circle. Its opposite angles therefore satisfy
∠AEB + ∠ACB = two right angles
(3.22).

**Step 7.** Since AX and AY are opposite rays of the tangent,
∠XAB + ∠BAY = two right angles
(1.13). Comparing this equality with Step 6 and subtracting the equal angles ∠XAB and ∠ACB established in Step 4 gives
∠BAY = ∠AEB
(P4; CN3). Since E was arbitrary, this holds for every angle in the segment on the opposite side of AB from Y (Step 3; D3.8). Together with Step 5 and the diameter case in Step 2, this proves that the angles made by the chord with the tangent equal the angles in the alternate segments.

**USED:** 1.13, 1.32, 3.1, 3.18, 3.2, 3.21, 3.22, 3.31, CN1, CN3, D1.10, D1.17, D3.2, D3.8, P1, P2, P4
**Human refs (from References field):** 1.32, 3.19, 3.22, 3.31
**Jaccard:** 0.167 — AI adds ['1.13', '3.1', '3.18', '3.2', '3.21', 'CN1', 'CN3', 'D1.10', 'D1.17', 'D3.2', 'D3.8', 'P1', 'P2', 'P4']; Human adds ['3.19']

## Proposition 3.33
**Statement:** On a given straight line to describe a segment of a circle admitting an angle equal to a given rectilineal angle.

**Step 1.** Let AB be the given straight line and α the given rectilineal angle. Choose the tangent–chord construction, since 3.32 directly turns a prescribed tangent–chord angle into an angle in the alternate segment. Construct a ray AT such that ∠TAB = α, and produce it into the full straight line t (1.23, P2). The lines t and AB are distinct, since they contain a rectilineal angle (D1.8).

**Step 2.** Bisect AB at M (1.10). Draw the straight line m through M perpendicular to AB, and the straight line ℓ through A perpendicular to t, producing both as necessary (1.11, P2, D1.10).

**Step 3.** The lines ℓ and m meet. Indeed, if ℓ is the line AB, they meet at M. Otherwise, suppose they do not meet. They would then be parallel (D1.23), and AB, meeting them at A and M, would make equal corresponding angles with them (1.29). Thus AB would be perpendicular to ℓ at A, just as it is perpendicular to m at M (P4, D1.10). But t is also perpendicular to ℓ at A. Taking rays of AB and t on opposite sides of ℓ, their adjacent angles with a ray of ℓ are both right; hence those rays form one straight line (1.14). This would make t the line AB, contrary to Step 1. Therefore ℓ and m meet; call their intersection O.

**Step 4.** We have OA = OB. If O = M, this is the equality MA = MB from the bisection (1.10). Otherwise, join OA and OB (P1). In triangles OMA and OMB, MA = MB, OM is common (CN4), and ∠OMA and ∠OMB are equal right angles (D1.10, P4). Therefore OA = OB by side–angle–side congruence (1.4).

**Step 5.** Describe the circle Γ with centre O and radius OA (P3). Since OB = OA, both A and B lie on its circumference (D1.15).

**Step 6.** The diameter of Γ through A lies on ℓ, since O and A lie on ℓ (P2, D1.17). The line t is perpendicular to this diameter at A. Consequently t falls outside Γ except at A, by 3.16, and therefore touches Γ at A (D3.2). Here 3.16 supplies tangency directly from the constructed perpendicular diameter.

**Step 7.** Take the segment S bounded by AB and the arc of Γ lying on the side of AB opposite T—the alternate segment to ∠TAB (D3.6). Let X be any point of that arc other than A and B, and join XA and XB (P1). Since t touches Γ at A and AB cuts the circle, the tangent–chord theorem gives ∠AXB = ∠TAB (3.32). But ∠TAB = α, so ∠AXB = α (CN1). By D3.8, ∠AXB is an angle in S. Thus the segment S has been described on the given straight line AB and admits an angle equal to the given rectilineal angle, as required.

**USED:** 1.10, 1.11, 1.14, 1.23, 1.29, 1.4, 3.16, 3.32, CN1, CN4, D1.10, D1.15, D1.17, D1.23, D1.8, D3.2, D3.6, D3.8, P1, P2, P3, P4
**Human refs (from References field):** 1.4, 3.16, 3.31, 3.32
**Jaccard:** 0.130 — AI adds ['1.10', '1.11', '1.14', '1.23', '1.29', 'CN1', 'CN4', 'D1.10', 'D1.15', 'D1.17', 'D1.23', 'D1.8', 'D3.2', 'D3.6', 'D3.8', 'P1', 'P2', 'P3', 'P4']; Human adds ['3.31']

## Proposition 3.34
**Statement:** From a given circle to cut off a segment admitting an angle equal to a given rectilineal angle.

**Step 1.** Let the given circle be Γ and the given rectilineal angle be α. Choose a point A on Γ and draw a tangent AT at A (3.17). We choose the tangent–chord route because the alternate-segment theorem applies directly to the given circle, without constructing another circle.

**Step 2.** At A, on the side of AT containing the circle, construct a ray AX such that ∠TAX = α (1.23). Let this inward ray meet the circumference again at B, producing it as necessary (P2). Thus ∠TAB = α.

**Step 3.** The chord AB lies within the circle (3.2). Let S be the segment bounded by AB and the arc AB lying on the opposite side of AB from T (D3.6). This is the alternate segment corresponding to ∠TAB. Take any point C on that arc, distinct from A and B, and join CA and CB (P1). Then ∠ACB is an angle in S (D3.8).

**Step 4.** Since AT touches the circle at A and AB cuts it, the angle between AT and AB equals the angle in the alternate segment: ∠ACB = ∠TAB (3.32). But ∠TAB = α, so ∠ACB = α (CN1). Since C was arbitrary, the segment S cut off from the given circle admits an angle equal to the given rectilineal angle, as required.

**USED:** 1.23, 3.17, 3.2, 3.32, CN1, D3.6, D3.8, P1, P2
**Human refs (from References field):** 1.23, 3.32
**Jaccard:** 0.222 — AI adds ['3.17', '3.2', 'CN1', 'D3.6', 'D3.8', 'P1', 'P2']

## Proposition 3.35
**Statement:** If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.

**Step 1.** Let the chords AB and CD intersect at P inside the circle. Find its centre O (3.1). Write R(UV,WX) for the rectangle contained by UV and WX, and S(UV) for the square on UV (D2.1, D1.22). We must prove R(AP,PB) = R(CP,PD).

**Step 2.** If P = O, then AP, PB, CP, and PD are equal radii (D1.15). Consequently the two rectangles are squares on equal straight lines and are equal by coincidence (D1.22, CN4). Henceforth suppose P ≠ O, and join OP (P1).

**Step 3.** Consider each of the two chords in turn, writing XY for AB or CD, and join OX (P1). We compare their rectangles by establishing
R(XP,PY) + S(OP) = S(OX).
The chosen route uses the internal-division identity 2.5, since P lies between the endpoints of each chord, together with the right-triangle identity 1.47. The following cases include chords through the centre and intersections at chord midpoints.

**Step 4.** Suppose XY passes through O. Since OX = OY, O bisects XY (D1.15). Because P ≠ O, XY is cut equally at O and unequally at P. Therefore
R(XP,PY) + S(OP) = S(OX)
by 2.5.

**Step 5.** Suppose XY does not pass through O. Bisect XY at M (1.10), and join OM (P1). Since the midpoint has been constructed first, use the bisecting-implies-perpendicular direction of 3.3: OM is perpendicular to XY. Thus, in the right-angled triangle OMX,
S(XM) + S(OM) = S(OX) (1.47).
If P = M, then XP = PY = XM, so R(XP,PY) = S(XM), while OP is OM (D1.22, CN4). Substitution gives
R(XP,PY) + S(OP) = S(OX) (CN1).

**Step 6.** In the remaining case, XY does not pass through O and P ≠ M. Since XY is cut equally at M and unequally at P,
R(XP,PY) + S(MP) = S(XM) (2.5).
Also, OM is perpendicular to MP, so the right-angled triangle OMP gives
S(MP) + S(OM) = S(OP) (1.47).
Add S(OM) to both sides of the first equality (CN2). Substituting the last equality and the equality from triangle OMX in Step 5 yields
R(XP,PY) + S(OP) = S(OX) (CN1).

**Step 7.** Applying these cases to AB and CD gives
R(AP,PB) + S(OP) = S(OA),
R(CP,PD) + S(OP) = S(OC).
The radii OA and OC are equal, and hence their squares are equal (D1.15, CN4). Therefore the two left-hand sums are equal (CN1). Subtracting the common square S(OP) gives
R(AP,PB) = R(CP,PD) (CN3).
Thus the rectangle contained by the segments of one straight line equals the rectangle contained by the segments of the other.

**USED:** 1.10, 1.47, 2.5, 3.1, 3.3, CN1, CN2, CN3, CN4, D1.15, D1.22, D2.1, P1
**Human refs (from References field):** 1.47, 2.5, 3.3
**Jaccard:** 0.231 — AI adds ['1.10', '3.1', 'CN1', 'CN2', 'CN3', 'CN4', 'D1.15', 'D1.22', 'D2.1', 'P1']

## Proposition 3.36
**Statement:** If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the circle and the other touch it, the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference will be equal to the square on the tangent.

**Step 1.** Let P be the exterior point, let the secant meet the circle first at A and then at B, and let PT touch the circle at T. Write S(x) for the square on a segment x and R(x,y) for the rectangle contained by segments x and y (D1.22, D2.1). Find the centre O and join OP, OT, and OB (3.1, P1).

**Step 2.** The radius OT is perpendicular to the tangent PT (3.18). Consequently, in the right-angled triangle OTP,
S(OP) = S(OT) + S(PT) (1.47).
Here 3.18 is the direct choice because the centre and the radius to the point of contact are already available.

**Step 3.** Bisect AB at M (1.10). The points lie in the order B, M, A, P. Apply 2.6 to AB, bisected at M and produced beyond A to P. Since MA = MB, it gives
R(PB,PA) + S(MB) = S(PM) (2.6, CN4).
The relevant path choice is the midpoint-and-squares route: 2.6 applies directly to this externally extended, bisected chord. We distinguish whether the secant passes through O.

**Step 4.** Suppose first that the secant passes through O. Then AB is a diameter, and OA = OB because they are radii (D1.17, D1.15). Thus O is its midpoint M. The identity in Step 3 therefore becomes
R(PB,PA) + S(OB) = S(OP) (CN4).

**Step 5.** Suppose instead that the secant does not pass through O. Join OM (P1). Since the straight line through O bisects the chord AB at M, it is perpendicular to AB (3.3). Applying 1.47 to the right-angled triangles OMB and OMP gives
S(OB) = S(OM) + S(MB),
and
S(OP) = S(OM) + S(PM).

**Step 6.** Add S(OM) to both sides of the identity in Step 3 (CN2):
R(PB,PA) + S(MB) + S(OM) = S(PM) + S(OM).
Substituting the equal areas established in Step 5 yields
R(PB,PA) + S(OB) = S(OP) (CN1).
Together with Step 4, this establishes the same identity in both cases.

**Step 7.** Since OB and OT are radii, OB = OT, and hence S(OB) = S(OT) (D1.15, CN4). Combining this equality with Steps 2, 4, and 6 gives
R(PB,PA) + S(OB) = S(PT) + S(OB) (CN2, CN1).
Subtract the common square S(OB) (CN3). Therefore
R(PB,PA) = S(PT).
Thus the rectangle contained by the whole secant PB and its exterior portion PA equals the square on the tangent PT, as required.

**USED:** 1.10, 1.47, 2.6, 3.1, 3.18, 3.3, CN1, CN2, CN3, CN4, D1.15, D1.17, D1.22, D2.1, P1
**Human refs (from References field):** 1.47, 2.6, 3.18, 3.3
**Jaccard:** 0.267 — AI adds ['1.10', '3.1', 'CN1', 'CN2', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D1.22', 'D2.1', 'P1']

## Proposition 3.37
**Statement:** If a point be taken outside a circle and from the point there fall on the circle two straight lines, if one of them cut the circle, and the other fall on it, and if further the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference be equal to the square on the straight line which falls on the circle, the straight line which falls on it will touch the circle.

**Step 1.** Let A be the point outside the circle, and let the secant meet the circumference first at B and then at C. Let D be the point on the circumference at which the other straight line AD falls. The hypothesis is that the rectangle contained by AC and AB equals the square on AD. Write XY² for the square on a segment XY. (Hypothesis.)

**Step 2.** Draw a tangent AT from A to the circle, touching it at T (3.17). Find the centre O (3.1), and join OA, OT, and OD (P1). Path choice: compare the given square with the square on this actual tangent, retaining an equality of squares so that the converse right-angle theorem can be applied directly.

**Step 3.** Since AC cuts the circle and AT touches it, the rectangle contained by AC and AB equals AT² (3.36). The same rectangle equals AD² by hypothesis; therefore AT² = AD² (CN1).

**Step 4.** The radii OT and OD are equal (D1.15), so their squares are equal (CN4). Because AT touches the circle at T, OT is perpendicular to AT (3.18). Thus, by the theorem on the square opposite a right angle,
OA² = OT² + AT² (1.47).
Substituting the equal squares just established gives
OA² = OD² + AD² (CN2, CN1).

**Step 5.** The points O, A, and D are not collinear. Indeed, all three segments between them are nonzero. If the points were collinear, one segment would be the sum of the other two, and its square would exceed the sum of their squares (2.4, CN5). If that segment were OA, this would contradict Step 4 directly. If it were OD or AD, its square would exceed OA², whereas Step 4 makes OA² greater than each of OD² and AD² (CN5). Hence OAD is a triangle.

**Step 6.** In triangle OAD, the square on OA equals the sum of the squares on OD and AD. Therefore the angle ODA is right (1.48).

**Step 7.** Produce DO through O to the opposite circumference (P2); the resulting straight line is a diameter ending at D (D1.17). By Step 6, AD is at right angles to this diameter at its extremity. Consequently the straight line AD falls outside the circle (3.16). Since it meets the circle at D but does not cut it, it touches the circle at D (D3.2). Thus the straight line specified in the proposition is a tangent.

**USED:** 1.47, 1.48, 2.4, 3.1, 3.16, 3.17, 3.18, 3.36, CN1, CN2, CN4, CN5, D1.15, D1.17, D3.2, P1, P2
**Human refs (from References field):** 1.8, 3.16, 3.18, 3.36
**Jaccard:** 0.167 — AI adds ['1.47', '1.48', '2.4', '3.1', '3.17', 'CN1', 'CN2', 'CN4', 'CN5', 'D1.15', 'D1.17', 'D3.2', 'P1', 'P2']; Human adds ['1.8']
