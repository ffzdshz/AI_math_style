# Book 3 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 3.1
**Statement:** To find the centre of a given circle.

**Step 1.** Use the perpendicular bisector of one chord to obtain a diameter, then bisect that diameter. Choose distinct points A and B on the given circumference and join AB (P1). Bisect AB at M (1.10), and draw through M a straight line l perpendicular to AB, producing it in both directions as necessary (1.11, P2, D1.10).

**Step 2.** By the definition of a circle, there exists an interior point O from which all straight lines to the circumference are equal; this point is a centre (D1.15, D1.16). Introduce O only to verify the construction, without assuming its position is known. In particular, OA = OB (D1.15).

**Step 3.** If O lies on the straight line AB, then O = M. Indeed, outside the segment AB, one of OA and OB would be a proper part of the other. Inside AB but away from M, one would be greater than AM and the other less than BM, or conversely; since AM = BM, they could not be equal. Both alternatives contradict OA = OB by the whole being greater than the part (CN5). Thus, in this case, O already lies on l.

**Step 4.** Suppose instead that O does not lie on AB. Join OA, OB, and OM (P1). In triangles AMO and BMO, AM = BM by construction, AO = BO by Step 2, and MO is common (CN4). Therefore ∠AMO = ∠BMO (1.8). Proposition 1.8 is the natural choice here because all three pairs of corresponding sides are already equal. Since MA and MB are opposite rays, these equal adjacent angles are right angles (D1.10).

**Step 5.** Let MX be the ray of l on the side of AB opposite O. The angles ∠OMA and ∠AMX are both right, by Step 4 and the construction of l (D1.10). Their sum is therefore two right angles (P4). Since MO and MX lie on opposite sides of AB, they form one straight line by 1.14. Hence O lies on l in this case also.

**Step 6.** Produce l as necessary to meet the circumference at C and D (P2). Because l passes through the interior centre O, these endpoints lie on opposite sides of O, and OC = OD (D1.15). Thus CD is a diameter (D1.17). Bisect CD at E, so that CE = ED (1.10).

**Step 7.** The point O must coincide with E. Otherwise, since both lie between C and D, one of OC and OD would be greater than the corresponding half CE or ED, and the other would be less. This contradicts OC = OD and CE = ED (CN5). Consequently E = O, so the constructed point E is the centre of the given circle (D1.16).

**USED:** 1.10, 1.11, 1.14, 1.8, CN4, CN5, D1.10, D1.15, D1.16, D1.17, P1, P2, P4
**Human refs (from References field):** 1.8, D1.10
**Jaccard:** 0.154 — AI adds ['1.10', '1.11', '1.14', 'CN4', 'CN5', 'D1.15', 'D1.16', 'D1.17', 'P1', 'P2', 'P4']

## Proposition 3.2
**Statement:** If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

**Step 1.** Let A and B be distinct points on the circumference. Draw AB, find the centre O, and join OA and OB. Then OA = OB, since both terminate on the circumference from the centre. [P1, 3.1, D1.15]

**Step 2.** Let X be any point strictly between A and B. If X = O, then X is inside the circle by the definition of its centre. Otherwise join OX. We shall show that OX < OB and thereby exclude X from being on or outside the circle. [D1.15, P1]

**Step 3.** First suppose O, A, and B are collinear. O must lie between A and B: otherwise one of the equal lengths OA and OB would be a proper part of the other, which is impossible. Since X is strictly between A and B and differs from O, OX is a proper part of either OA or OB. Thus OX < OB. [CN5, D1.15]

**Step 4.** Now suppose O, A, and B are not collinear. Since OA = OB, the base angles of triangle OAB are equal. Because X lies between A and B, this gives ∠OAX = ∠OBX. [1.5]

**Step 5.** In triangle OAX, the side AX is produced to B. Its exterior angle ∠OXB is therefore greater than the opposite interior angle ∠OAX. Hence ∠OXB > ∠OBX. The direct path here is the exterior-angle inequality, since only an inequality—not an angle-sum calculation—is needed. [1.16; equality from Step 4]

**Step 6.** In triangle OXB, the greater angle ∠OXB is opposite OB, while the smaller angle ∠OBX is opposite OX. Therefore OB > OX. Thus OX < OB in both the collinear and noncollinear cases. [1.19; Step 3]

**Step 7.** Suppose X were on or outside the circle. Since O is inside, the segment OX would meet the bounding circumference at some point C either equal to X or between O and X. Consequently OC ≤ OX. But OC = OB because C is on the circumference, contradicting OX < OB. Therefore X is inside the circle. Since X was arbitrary, every point of AB other than its endpoints lies within the circle, as required. [D1.15, CN5; Steps 3 and 6]

**USED:** 1.16, 1.19, 1.5, 3.1, CN5, D1.15, P1
**Human refs (from References field):** 1.16, 1.19, 1.5, 3.1
**Jaccard:** 0.571 — AI adds ['CN5', 'D1.15', 'P1']

## Proposition 3.3
**Statement:** If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

**Step 1.** Let the circle have centre O, let AB be a chord not passing through O, and let the given straight line through O cut AB at D. Thus D lies between A and B, and O is distinct from D. Join OA and OB (P1). Since they are radii of the same circle, OA = OB (D1.15, D1.16).

**Step 2.** First suppose that the given line bisects AB, so that AD = DB. In triangles ADO and BDO, AD = BD, DO is common (CN4), and AO = BO by Step 1. Therefore ∠ADO = ∠BDO (1.8). Path choice: 1.8 applies directly because all three corresponding sides are equal.

**Step 3.** Since DA and DB are opposite rays of the straight line AB, the equal angles ∠ADO and ∠BDO are adjacent angles made by DO standing on AB. Each is therefore right, and the given line through O cuts AB at right angles (D1.10).

**Step 4.** Conversely, suppose that the given line through O cuts AB at right angles. Then ∠ADO and ∠BDO are right angles and hence equal (P4).

**Step 5.** Since OA = OB, the base angles ∠OAB and ∠OBA of triangle OAB are equal (1.5). Because D lies between A and B, these are respectively ∠OAD and ∠OBD. Thus ∠OAD = ∠OBD (1.5).

**Step 6.** Triangles ADO and BDO therefore have two corresponding angles equal, by Steps 4–5, and the corresponding sides AO and BO, opposite the equal angles at D, are equal by Step 1. Hence AD = BD (1.26), so the given line bisects AB. Path choice: the two-angle-and-corresponding-side case of 1.26 applies immediately, without any auxiliary construction. Together with Step 3, this proves both assertions.

**USED:** 1.26, 1.5, 1.8, CN4, D1.10, D1.15, D1.16, P1, P4
**Human refs (from References field):** 1.26, 1.5, 1.8, D1.10
**Jaccard:** 0.444 — AI adds ['CN4', 'D1.15', 'D1.16', 'P1', 'P4']

## Proposition 3.4
**Statement:** If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.

**Step 1.** Let the distinct chords AB and CD cut one another at E, neither straight line passing through the centre. Suppose, for a contradiction, that they bisect one another: AE = EB and CE = ED. (Hypothesis; supposition for contradiction.)

**Step 2.** Find the centre O of the circle by 3.1, and join OE by P1. Since neither chord passes through O, the point O is distinct from E and lies on neither chord. (3.1, P1; hypothesis.)

**Step 3.** The straight line OE passes through the centre and bisects both AB and CD. Therefore it cuts both at right angles. We use the bisection-to-perpendicular implication of 3.3, since the assumed bisections give its hypotheses directly. (3.3.)

**Step 4.** Interchange the names C and D if necessary so that the rays EA and EC lie on opposite sides of the straight line OE. The angles AEO and OEC are both right angles, and hence together equal two right angles. Therefore EA and EC lie in one straight line, by 1.14. This directly supplies the required collinearity without a separate uniqueness-of-perpendicular argument. (D1.10, 1.14.)

**Step 5.** Consequently AB and CD lie on the same straight line, contrary to the hypothesis that they are distinct straight lines cutting one another. The supposition of mutual bisection is therefore false: two such straight lines not through the centre do not bisect one another. (Step 4; hypothesis; contradiction.)

**USED:** 1.14, 3.1, 3.3, D1.10, P1
**Human refs (from References field):** 3.1, 3.3
**Jaccard:** 0.400 — AI adds ['1.14', 'D1.10', 'P1']

## Proposition 3.5
**Statement:** If two circles cut one another, they will not have the same centre.

**Step 1.** Let the circles Γ and Δ cut one another at A. Since they cut, choose a point B on the circumference of Γ strictly inside Δ. We take the direct route of comparing radii and obtaining a whole–part contradiction. (Hypothesis that the circles cut.)

**Step 2.** Suppose, for a contradiction, that O is the centre of both circles. Then O lies inside both circles. [D1.15, D1.16]

**Step 3.** Join OA and OB, and produce OB to meet the circumference of Δ at C beyond B. Here B lies between O and C, since O is the centre of Δ and B lies strictly inside it. [P1, P2, D1.15, D1.16]

**Step 4.** Since A and B lie on Γ and O is its centre, OA = OB. Since A and C lie on Δ and O is its centre, OA = OC. Therefore OB = OC, being equal to the same straight line OA. [D1.15, D1.16, CN1]

**Step 5.** But OB is a proper part of OC, so OC is greater than OB, contrary to Step 4. [CN5] Thus the supposition of a common centre is impossible: if two circles cut one another, they do not have the same centre.

**USED:** CN1, CN5, D1.15, D1.16, P1, P2
**Human refs (from References field):** D1.15
**Jaccard:** 0.167 — AI adds ['CN1', 'CN5', 'D1.16', 'P1', 'P2']

## Proposition 3.6
**Statement:** If two circles touch one another, they will not have the same centre.

**Step 1.** Let the two distinct circles Γ and Δ touch at A. Thus A lies on both circumferences (D3.3). We argue by contradiction using equal radii; this route treats internal and external contact alike.

**Step 2.** Suppose that O is their common centre. Then O lies inside both circles (D1.15, D1.16). Join OA (P1).

**Step 3.** Since the circles are distinct, their bounding circumferences are distinct (D1.15). Interchanging their names if necessary, choose B on Γ but not on Δ. Draw OB and produce the straight line as necessary (P1, P2). Let C be the endpoint of the diameter of Δ in the direction from O through B (D1.17). Thus B and C lie on the same side of O on this straight line, and B ≠ C because C belongs to Δ whereas B does not.

**Step 4.** Since O is the centre of Γ and A and B lie on Γ, OB = OA (D1.15). Likewise, since A and C lie on Δ, OC = OA (D1.15). Therefore OB = OC (CN1).

**Step 5.** But B and C are distinct points on the same straight line and on the same side of O. Hence one of OB and OC is a proper part of the other, so the whole is greater than the part (CN5). This contradicts their equality in Step 4. Therefore the two touching circles cannot have the same centre.

**USED:** CN1, CN5, D1.15, D1.16, D1.17, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN1', 'CN5', 'D1.15', 'D1.16', 'D1.17', 'D3.3', 'P1', 'P2']

## Proposition 3.7
**Statement:** If on the diameter of a circle a point be taken which is not the centre of the circle, and from the point straight lines fall upon the circle, that will be greatest on which the centre is, the remainder of the same diameter will be least, and of the rest  the nearer to the straight line through the centre is always greater than the more remote, and only two equal straight lines will fall from the point on the circle, one on each side of the least straight line.

**Step 1.** Let AB be the diameter, O the centre, and P the given point on the diameter, distinct from O. Name the endpoints so that their order is A, O, P, B. Thus PA is the segment passing through the centre, and PB is the remainder of the diameter (D1.17). Join P and O to any other points of the circumference under consideration (P1).

**Step 2.** Let X be any point of the circumference other than A and B. In triangle POX, the two sides PO and OX together exceed PX (1.20). Since OX = OA, being radii (D1.15),
PX < PO + OX = PO + OA = PA
(CN2). Also PA > OA = OB > PB, because PA contains OA as a proper part and PB is a proper part of OB (D1.15; CN5). Therefore PA is strictly the greatest of all the segments from P to the circumference.

**Step 3.** In the same triangle, PO + PX > OX (1.20). But OX = OB = OP + PB (D1.15 and the order O, P, B). Removing the common length OP gives PX > PB (CN3; CN5). Together with PA > PB from Step 2, this proves that PB is strictly the least segment.

**Step 4.** Consider two non-diametral segments PX and PY on the same side of AB, with PX nearer to PA than PY. Their endpoints occur in the order A, X, Y, B along that semicircle. Consequently OY lies inside angle POX, and
∠POX > ∠POY
(CN5). In triangles POX and POY, OP is common and OX = OY, being radii (D1.15). Their included angles are ordered as just shown; hence PX > PY (1.24). The direct route here is 1.24: the equal radii and common side already supply precisely the two pairs of equal sides it requires. Thus, on either side of the diameter, the nearer segment is always greater than the more remote.

**Step 5.** For any non-diametral segment PX, construct on the opposite side of AB a ray from O making with OP an angle equal to ∠POX (1.23), and produce it to meet the circumference at Y (P2). Thus ∠POY = ∠POX. Since OY = OX (D1.15) and OP is common, triangles POY and POX have two sides and their included angle respectively equal. Therefore PY = PX, and ∠OPY = ∠OPX (1.4). This is the natural use of 1.4 because the construction supplies the included-angle equality directly. Since PA and PO are the same ray, PY and PX also make equal angles with PA. By construction they lie on opposite sides of AB, hence one on each side of the least segment PB.

**Step 6.** The ordering proved in Step 4 also applies when the two segments being compared lie on opposite sides of AB: replace one by its counterpart from Step 5 on the same side as the other. This replacement preserves both its length and its angle with PA, by 1.4. Step 4 then shows that the segment nearer to PA is greater, regardless of which sides the original segments occupy.

**Step 7.** No two distinct non-diametral segments on the same side of AB can be equal, since Step 4 makes one strictly greater than the other. Consequently the equal counterpart constructed in Step 5 is unique: any further segment equal to PX would share a side of AB with either PX or PY and contradict Step 4. Neither PA nor PB can have a distinct equal counterpart, by the strict inequalities of Steps 2 and 3. Therefore the segment through the centre is greatest, the remaining part of the diameter is least, the nearer of the other segments is always greater than the more remote, and each non-diametral segment has exactly one equal counterpart, one on each side of the least segment. This proves the proposition.

**USED:** 1.20, 1.23, 1.24, 1.4, CN2, CN3, CN5, D1.15, D1.17, P1, P2
**Human refs (from References field):** 1.20, 1.23, 1.24, 1.4
**Jaccard:** 0.364 — AI adds ['CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'P1', 'P2']

## Proposition 3.8
**Statement:** If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest   the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

**Step 1.** Let P be the exterior point and O the centre. Draw PO and continue it through the circle, meeting the circumference first at A and then at B; thus P, A, O, B occur in this order, and AB is a diameter. Join O to the other circumference points used below. All these radii are equal. For a secant from P, call its first intersection the convex endpoint and its second intersection the concave endpoint. [P1, P2, D1.15, D1.17]

**Step 2.** The central lines give the strict extremes. For any circumference point X other than A and B, the triangle inequality in triangle POX gives
PX < PO + OX = PO + OB = PB.
The same inequality also gives
PO < PX + OX.
Since PO = PA + OA and OA = OX, subtraction yields PA < PX. Thus PB is greatest among all the lines from P to the circumference, and PA is least. [1.20, D1.15, CN2, CN3]

**Step 3.** Consider two noncentral secants on the same side of PO. Write their points in the orders P, C, D and P, E, F, with C and E their convex endpoints and D and F their concave endpoints. Suppose the ray PCD is nearer to PO than the ray PEF: it lies strictly inside the angle OPE. It therefore meets the opposite sides OE and OF of triangles POE and POF; call these intersections K and L respectively. Both intersections lie in the interiors of those radii. Each open radius lies inside the circle, since it is part of a diameter and a chord lies inside the circle. Consequently K and L lie between the entry C and the exit D of the first secant. [P2, D1.17, 3.2]

**Step 4.** Because C lies between P and K, OC lies inside angle POK; because O, K, E are collinear, this gives
∠POC < ∠POE.
Likewise, L lies between P and D, so OL lies inside angle POD; since O, L, F are collinear,
∠POF < ∠POD. [CN5]
Now triangles POC and POE have PO common and OC = OE, while triangles POF and POD have PO common and OF = OD. Proposition 1.24 therefore gives
PC < PE and PF < PD.
Thus the nearer secant has the shorter convex line and the longer concave line. The chosen comparison is 1.24 because joining the endpoints to the centre immediately supplies its two equal side-pairs and the required included-angle inequalities. The argument applies on either side of PO. [D1.15, 1.24]

**Step 5.** Every noncentral line has an equal counterpart on the other side. Let X be any circumference point not on AB. At O construct, on the opposite side of OP, an angle POY equal to POX, taking Y where its second arm meets the circle. Join PY. Then PO is common, OX = OY, and the included angles are equal. Hence triangles POX and POY are congruent: PX = PY and ∠OPX = ∠OPY. [1.23, P1, D1.15, 1.4]

**Step 6.** This construction also completes the comparisons for lines lying on opposite sides of PO. Apply Step 5 to both endpoints of a secant. Their counterparts lie on the same opposite ray, because each makes the same angle with PO as the original secant; their distances from P are preserved. Hence the convex endpoint remains the nearer endpoint and the concave endpoint remains the farther endpoint. Reflecting one of two secants on opposite sides therefore reduces their comparison to Step 4, without changing either its inclination to PO or its two lengths. Thus, on either side or across the two sides, nearer to the central line means greater for the concave lines and less for the convex lines. [1.4, CN5, 1.24]

**Step 7.** Finally, there cannot be two distinct circumference points X and Z on the same side of PO with PX = PZ. For OX = OZ as radii, so such points would give two distinct triangles on the same base PO and on the same side, with their corresponding sides from P and O equal. This is precisely what 1.7 forbids; it is the direct uniqueness proposition for these two prescribed distances. Consequently the counterpart constructed in Step 5 is the only equal partner of PX. The axial lines PA and PB have no equal partners, by the strict inequalities of Step 2. Therefore no three lines from P to the circle can be equal, and every noncentral line has exactly one equal partner, on the opposite side of the least line PA. Together with Steps 2, 4, and 6, this proves all the assertions. [D1.15, 1.7, 1.4, 1.20, 1.24]

**USED:** 1.20, 1.23, 1.24, 1.4, 1.7, 3.2, CN2, CN3, CN5, D1.15, D1.17, P1, P2
**Human refs (from References field):** 1.20, 1.21, 1.24, 1.4, 3.1
**Jaccard:** 0.200 — AI adds ['1.23', '1.7', '3.2', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'P1', 'P2']; Human adds ['1.21', '3.1']

## Proposition 3.9
**Statement:** If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

**Step 1.** Let P be the given point within the circle. Choose three of the given equal straight lines PA, PB, PC, with A, B, C distinct points on the circumference; thus PA = PB = PC. (Hypothesis.) Find the centre O of the circle. [3.1]

**Step 2.** Suppose, for a contradiction, that P is not O. Join O to P and produce this straight line in both directions to meet the circumference at X and Y. [P1, P2] Since XY passes through the centre and terminates at the circumference in both directions, it is a diameter, and P lies on it. [D1.17]

**Step 3.** Apply 3.7 directly: it is the preceding theorem that addresses precisely a noncentral point on a diameter. It states that at most two equal straight lines can fall from such a point to the circumference. [3.7] This contradicts the three distinct equal straight lines PA, PB, PC of Step 1. Therefore P is O, and the given point is the centre of the circle.

**USED:** 3.1, 3.7, D1.17, P1, P2
**Human refs (from References field):** 1.8, 3.1, D1.10
**Jaccard:** 0.143 — AI adds ['3.7', 'D1.17', 'P1', 'P2']; Human adds ['1.8', 'D1.10']

## Proposition 3.10
**Statement:** A circle does not cut a circle at more points than two.

**Step 1.** Suppose, for a contradiction, that two circles cut one another at three distinct points A, B, C. Join AB, AC, and BC (P1). These points are not collinear: otherwise the middle point would lie within either circle, being an interior point of the chord joining the other two, whereas it lies on the circumference (3.2).

**Step 2.** Find the centres O and Q of the two circles (3.1). Since the circles cut one another, O and Q are distinct (3.5). Moreover, OA = OB = OC and QA = QB = QC, because these are radii of their respective circles (D1.15). We use the common-chord perpendicular-bisector route through 3.3, which requires no assumption about either centre lying inside the other circle.

**Step 3.** Bisect AB at M and AC at N (1.10). Erect perpendiculars ℓ and m to AB and AC at M and N respectively, and produce them as necessary (1.11, P2). The points M and N are distinct: otherwise the distinct lines AB and AC would share both A and their common midpoint, contrary to their being distinct straight lines (D1.4).

**Step 4.** Both centres lie on each of these perpendiculars. Indeed, consider either common chord, let T be its midpoint, and let X be either centre. If X lies on the chord’s supporting line, its equal distances from the endpoints force it to be T: an exterior point has unequal distances, and an interior point other than the midpoint likewise has unequal distances, by the whole being greater than the part (D1.15, CN5). If X does not lie on that line, join XT (P1). Since XT passes through the centre and bisects a chord not through the centre, it is perpendicular to the chord (3.3). It therefore coincides with the perpendicular already erected at T, by uniqueness of the perpendicular at a point, which follows from 1.14 and P4. Consequently, both O and Q lie on ℓ, and both lie on m.

**Step 5.** Since O and Q are distinct, the straight lines ℓ and m, passing through both, coincide (D1.4). Thus AB and AC are perpendicular to the same straight line at the distinct points M and N. Their alternate angles with that line are right angles and hence equal (D1.10, P4). Apply 1.27, naturally using these equal alternate angles: AB and AC are parallel. But they meet at A, contradicting the definition of parallel straight lines (D1.23).

**Step 6.** The supposition of three distinct points of intersection has therefore led to a contradiction. Hence a circle does not cut a circle at more points than two (Steps 1–5).

**USED:** 1.10, 1.11, 1.14, 1.27, 3.1, 3.2, 3.3, 3.5, CN5, D1.10, D1.15, D1.23, D1.4, P1, P2, P4
**Human refs (from References field):** 3.1, 3.5
**Jaccard:** 0.125 — AI adds ['1.10', '1.11', '1.14', '1.27', '3.2', '3.3', 'CN5', 'D1.10', 'D1.15', 'D1.23', 'D1.4', 'P1', 'P2', 'P4']

## Proposition 3.11
**Statement:** If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.

**Step 1.** Let the inner circle, with centre I, touch the outer circle, with centre O, at T. Thus T lies on both circumferences, and the inner circle is contained in the outer circle. Since I lies within the inner circle, it also lies within the outer circle. Moreover, O and I are distinct. [Internal-contact hypothesis; D3.3; D1.16; 3.6.]

**Step 2.** Draw OI and produce it in both directions to form a diameter of the outer circle. Let A be its endpoint in the direction from O through I, so that O, I, A occur in that order. Let B be the intersection of the ray from I towards A with the inner circumference, and join IT. [P1; P2; D1.17.]

**Step 3.** Because the inner circle is contained in the outer circle, B cannot lie beyond A on this ray. Thus either B = A or B lies between I and A. Consequently IB ≤ IA, with strict inequality in the latter case because IA is then the whole and IB a part. [Internal-contact hypothesis; CN5.]

**Step 4.** Since B and T lie on the inner circumference, IB = IT. Substitution in the comparison of Step 3 therefore gives IT ≤ IA. [D1.15; Step 3.]

**Step 5.** Path choice: apply the already proved least-distance assertion of 3.7 directly to I, an interior point of an outer diameter distinct from its centre O. The segment IA is the remainder of that diameter in the direction away from O, and hence is strictly shorter than every other segment from I to the outer circumference. Therefore, if T ≠ A, then IA < IT, contradicting Step 4. Thus T = A. [3.7; Steps 1–2 and 4.]

**Step 6.** Since A lies on OI produced beyond I and T = A, the straight line joining the centres, when produced, passes through the point of contact, as required. [Steps 2 and 5.]

**USED:** 3.6, 3.7, CN5, D1.15, D1.16, D1.17, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['3.6', '3.7', 'CN5', 'D1.15', 'D1.16', 'D1.17', 'D3.3', 'P1', 'P2']

## Proposition 3.12
**Statement:** If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

**Step 1.** Let the two circles, with centres A and B, touch externally at C. Their centres are distinct by 3.6. Join AB. (3.6; P1.)

**Step 2.** Suppose that C does not lie on the straight line AB, and join AC and BC. Path choice: the triangle inequality applies immediately to triangle ACB, so no auxiliary perpendicular or tangent is needed. It gives AC + BC > AB. (P1; 1.20.)

**Step 3.** Since the circles touch externally, their interiors are disjoint, and each centre is outside the other circle. Let X be the point where the segment AB leaves the circle centred at A, and Y the point where it enters the circle centred at B. The order is A, X, Y, B, allowing X = Y: if Y preceded X, points between Y and X would be inside both circles, contrary to external contact. (External-contact hypothesis; D3.3; D1.15.)

**Step 4.** Consequently AX + YB ≤ AB. Indeed, if X = Y, these two segments together constitute AB; otherwise AB also contains the positive intervening segment XY and is greater than their sum. (Step 3; CN5.)

**Step 5.** Because C and X lie on the circle centred at A, AC = AX; similarly, BC = BY. Adding these equalities gives AC + BC = AX + BY ≤ AB, contradicting Step 2. Thus C lies on the straight line through A and B. (D1.15; CN2; Steps 2 and 4.)

**Step 6.** Moreover, C lies between the centres. Otherwise one centre would lie in the interior of the radius joining the other centre to C, and hence inside the other circle, contrary to external contact. Therefore the straight line joining the centres passes through the point of contact. (D1.15; external-contact hypothesis; Step 5.)

**USED:** 1.20, 3.6, CN2, CN5, D1.15, D3.3, P1
**Human refs (from References field):** 1.20
**Jaccard:** 0.143 — AI adds ['3.6', 'CN2', 'CN5', 'D1.15', 'D3.3', 'P1']

## Proposition 3.13
**Statement:** A circle does not touch a circle at more points than one, whether it touch it internally or externally.

**Step 1.** Suppose, for a contradiction, that two circles touch one another, internally or externally, at two distinct points A and B. Find their centres O and P by 3.1. Since the circles touch, their centres are distinct by 3.6.

**Step 2.** Draw OP and produce it as necessary (P1, P2). We use the centre-line route because the preceding contact theorems apply directly: in the internal case, 3.11 places each of A and B on the straight line OP; in the external case, 3.12 does so. Thus A, B, O, and P are collinear in either case.

**Step 3.** Join each centre to A and B (P1). Radii of the same circle are equal, so OA = OB and PA = PB (D1.15). Each centre is inside its circle and therefore differs from A and B (D1.15). If O were not between A and B, one of OA and OB would contain the other together with the nonzero segment AB, contradicting their equality because the whole is greater than the part (CN5). Hence O lies between A and B. The same argument shows that P also lies between A and B.

**Step 4.** Since O and P are distinct, interchange their names if necessary so that the order is A, O, P, B. Then AP > AO and OB > PB, because in each comparison the first segment contains the second as a proper part (CN5). Using the radial equalities from Step 3 gives AP > AO = OB > PB, contradicting AP = PB (D1.15). The supposition of two distinct contact points is therefore impossible in both cases established in Step 2. Consequently, a circle does not touch another circle at more points than one, whether internally or externally.

**USED:** 3.1, 3.11, 3.12, 3.6, CN5, D1.15, P1, P2
**Human refs (from References field):** 3.11, 3.2, D3.3
**Jaccard:** 0.100 — AI adds ['3.1', '3.12', '3.6', 'CN5', 'D1.15', 'P1', 'P2']; Human adds ['3.2', 'D3.3']

## Proposition 3.14
**Statement:** In a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another.

**Step 1.** Let AB and CD be chords of a circle with centre O. First dispose of chords through O. Such chords are diameters and are equal, since each consists of two radii (D1.15, D1.17, CN2). A chord not through O is shorter than a diameter: the two radii to its endpoints together exceed it by 1.20. Moreover, a diameter has zero distance from O, whereas a chord not through O has a positive perpendicular distance. Thus both assertions hold in cases involving diameters. Henceforth suppose neither chord passes through O (D3.4).

**Step 2.** Draw OE perpendicular to AB and OF perpendicular to CD (1.12). By 3.3 these perpendiculars bisect the chords, so AE = EB and CF = FD. Join OA and OC (P1); then OA = OC, since they are radii of the same circle (D1.15). Path choice: use the chord-bisection result 3.3 followed by 1.47, since the same two right-triangle identities will establish both directions.

**Step 3.** Write S(XY) for the area of the square on XY. We use the elementary square-comparison rule: equal segments have equal squares, and equal squares have equal sides. Indeed, squares on equal sides coincide when corresponding sides are fitted together; if the sides were unequal, fitting a corner and its adjacent sides would place the smaller square as a proper part of the larger, so the squares could not be equal (D1.22, P4, CN4, CN5).

**Step 4.** Applying 1.47 to the right-angled triangles OEA and OFC gives
S(OA) = S(OE) + S(AE),
S(OC) = S(OF) + S(CF).
Since OA = OC, their squares are equal by Step 3. Consequently,
S(OE) + S(AE) = S(OF) + S(CF) (CN1).

**Step 5.** Suppose first that AB = CD. Since E and F bisect these chords, AE = CF: otherwise the chord consisting of two copies of the greater half would exceed the other chord, contrary to their equality (CN2, CN5). Hence S(AE) = S(CF) by Step 3. Subtracting these equal squares from the equal sums in Step 4 gives S(OE) = S(OF) (CN3), and therefore OE = OF by Step 3. The perpendiculars from the centre are thus equal, so AB and CD are equally distant from the centre (D3.4).

**Step 6.** Conversely, suppose AB and CD are equally distant from the centre. Then OE = OF by D3.4, and hence S(OE) = S(OF) by Step 3. Subtracting these equal squares from the equal sums in Step 4 gives S(AE) = S(CF) (CN3). Thus AE = CF by Step 3. Since AE = EB and CF = FD by Step 2, adding the corresponding equal halves yields AB = CD (CN1, CN2).

**Step 7.** Therefore equal straight lines in a circle are equally distant from its centre, and straight lines equally distant from its centre are equal to one another, as established in Steps 1, 5, and 6 (D3.4).

**USED:** 1.12, 1.20, 1.47, 3.3, CN1, CN2, CN3, CN4, CN5, D1.15, D1.17, D1.22, D3.4, P1, P4
**Human refs (from References field):** 1.47, 3.1, 3.3, D3.4
**Jaccard:** 0.188 — AI adds ['1.12', '1.20', 'CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.17', 'D1.22', 'P1', 'P4']; Human adds ['3.1']

## Proposition 3.15
**Statement:** Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

**Step 1.** Let O be the centre of the circle, XY any diameter, and AB any chord not passing through O. Join OA and OB (P1). Since all radii are equal, OX = OA and OY = OB; therefore XY = OA + OB (D1.15, D1.17, CN2).

**Step 2.** In triangle OAB, OA + OB > AB (1.20). Hence XY > AB. Since AB was arbitrary, every diameter is greater than every non-diametral chord. Moreover, all diameters are equal, each being the sum of two radii (D1.15, D1.17, CN2).

**Step 3.** Now let AB and CD be non-diametral chords, with AB nearer to O than CD. Bisect AB at M and CD at N (1.10), and join OM, ON, and OC (P1). Thus AM = MB and CN = ND. The lines from the centre bisecting these chords are perpendicular to them (3.3). Consequently OM < ON, by the meaning of greater distance from the centre (D3.5).

**Step 4.** Path choice: apply 1.47 directly to the right triangles formed by the perpendiculars and half-chords, since their hypotenuses are equal radii. Writing s² for the square on a segment s, we have
OM² + AM² = OA²,
and ON² + CN² = OC² (1.47).
Since OA = OC (D1.15), it follows that
OM² + AM² = ON² + CN² (CN1).

**Step 5.** Cut off OT = OM from ON, so that T lies strictly between O and N (1.3). By 2.4, the square on ON equals the square on OT together with the square on TN and twice the rectangle contained by OT and TN. These additional areas are positive; hence ON² > OT² = OM² (CN5).

**Step 6.** Subtract OM² from the equal totals in Step 4. Thus AM² equals CN² together with the positive excess of ON² over OM², and therefore AM² > CN² (CN3, CN5). It follows that AM > CN: equality would give equal squares, while AM < CN would give AM² < CN² by the same application of 2.4 and CN5 used in Step 5.

**Step 7.** Since AB consists of two parts each equal to AM, and CD consists of two parts each equal to CN, the inequality AM > CN gives AB > CD (CN2, CN5). Thus, of the straight lines in a circle, the diameter is greatest, and among the remaining chords the nearer to the centre is always greater than the more remote.

**USED:** 1.10, 1.20, 1.3, 1.47, 2.4, 3.3, CN1, CN2, CN3, CN5, D1.15, D1.17, D3.5, P1
**Human refs (from References field):** 1.20, 1.24, 3.14, D3.5
**Jaccard:** 0.125 — AI adds ['1.10', '1.3', '1.47', '2.4', '3.3', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'P1']; Human adds ['1.24', '3.14']

## Proposition 3.16
**Statement:** The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

**Step 1.** Let AB be a diameter of the circle, O its centre, and t the straight line through A perpendicular to AB. Choose a point T on either ray of t, and consider the semicircle on the same side of AB as T. Since AO lies along AB, ∠OAT is right. (D1.17, D1.18, D1.10)

**Step 2.** Let P be any point of t other than A, and join OP. In triangle OAP, the angle at A is right; therefore ∠OPA is less than a right angle, and consequently OP > OA. Here the two-angle inequality is the first sufficient angle result, and the side–angle comparison gives the required inequality directly. (P1, 1.17, 1.19)

If P were on the circumference, OP would equal OA. If P were inside the circle, producing OP to the circumference at Q beyond P would give OP < OQ = OA. Both contradict OP > OA. Thus every point of t other than A lies outside the circle. (P2, D1.15, CN5)

**Step 3.** For the remaining assertions, we shall construct a chord along every ray strictly inside ∠OAT and then apply the established chord-containment theorem. Let AX be any such ray. Its angle with AO is acute, since it is a proper part of the right angle OAT. Draw OH perpendicular to the complete straight line AX. (CN5, D1.12, 1.12)

The foot H lies on the ray AX. Indeed, H cannot equal A, since ∠OAX is acute. If H lay on the opposite ray, ∠OAH would be supplementary to the acute angle OAX and hence greater than a right angle. Together with the right angle OHA, this would contradict the two-angle inequality for triangle OAH. (D1.10, D1.12, 1.13, 1.17)

**Step 4.** Produce AH beyond H to K, taking HK equal to HA, and join OK. The triangles AHO and KHO have AH = HK, the side OH common, and their included angles at H equal, since both are right. Therefore OK = OA by side–angle–side congruence. Hence K lies on the circumference; because K lies on AX, it belongs to the chosen semicircle. (P2, 1.3, P1, D1.10, P4, 1.4, D1.15, D1.18)

**Step 5.** Since A and K are on the circumference, the chord AK, except for its endpoints, lies within the circle. Thus every ray strictly between AO and AT has an initial segment lying inside the chosen semicircle. This invokes 3.2 directly rather than re-establishing chord containment. (3.2; Steps 3–4)

An alleged straight ray interposed at A between AT and the semicircular circumference would lie strictly between AO and AT, but would have to remain outside the semicircle immediately after A. The preceding conclusion makes this impossible. Therefore no straight line can be interposed in that space. (Steps 1–5)

**Step 6.** Denote by S the angle of the semicircle at A, contained by AO and the semicircular circumference, and by R the remaining angle between that circumference and AT. These are plane angles, and S is the angle of the segment whose base is the diameter. (D1.8, D1.18, D3.7)

For every ray AX strictly inside ∠OAT, Step 5 places its initial segment strictly inside the semicircle. Consequently, at A, ∠OAX is a proper part of S, while R is a proper part of ∠XAT. Hence
S > ∠OAX, and R < ∠XAT.
These comparisons are comparisons of the angles at A, using the circumference adjacent to A. (Step 5, CN5)

**Step 7.** Let α be any acute rectilineal angle. At A, on AO and toward AT, construct a ray AX such that ∠OAX = α. Since α is less than a right angle, AX lies strictly inside ∠OAT. Applying Step 6 gives S > α. Thus the angle of the semicircle is greater than every acute rectilineal angle. (1.23, D1.12, P4; Step 6)

**Step 8.** Again let α be any acute rectilineal angle. At A, on AT and toward AO, construct a ray AY such that ∠YAT = α. This ray also lies strictly inside ∠OAT. Applying Step 6 to AY gives R < α. Thus the remaining angle is less than every acute rectilineal angle. (1.23, D1.12, P4; Step 6)

**Step 9.** The perpendicular t therefore lies outside the circle except at A; no straight line can be interposed between it and the circumference at A; the angle of the semicircle is greater than every acute rectilineal angle; and the remaining angle is less than every such angle. Since either ray of t could have been chosen in Step 1, the argument applies on either side of the diameter. This proves all the assertions. (Steps 2, 5, 7–8)

**USED:** 1.12, 1.13, 1.17, 1.19, 1.23, 1.3, 1.4, 3.2, CN5, D1.10, D1.12, D1.15, D1.17, D1.18, D1.8, D3.7, P1, P2, P4
**Human refs (from References field):** 1.17, 1.19, 1.5
**Jaccard:** 0.100 — AI adds ['1.12', '1.13', '1.23', '1.3', '1.4', '3.2', 'CN5', 'D1.10', 'D1.12', 'D1.15', 'D1.17', 'D1.18', 'D1.8', 'D3.7', 'P1', 'P2', 'P4']; Human adds ['1.5']

## Proposition 3.17
**Statement:** From a given point to draw a straight line touching a given circle.

**Step 1.** Let Γ be the given circle, and first let the given point A lie outside it. Find its centre O, and join OA, meeting Γ at B between O and A. [3.1, P1]

**Step 2.** Describe an auxiliary circle Σ with centre O and radius OA. Since OB is a proper part of OA, OB < OA, so B lies inside Σ. [P3, CN5, D1.15]

**Step 3.** At B draw a perpendicular to OA, and produce it to meet Σ at C. Join OC, meeting Γ at T between O and C, and join AT. Thus ∠OBC is right. [1.11, P2, P1, D1.10]

**Step 4.** We have OB = OT, since both are radii of Γ, and OC = OA, since both are radii of Σ. Moreover, rays OB and OA coincide, as do rays OC and OT; hence ∠BOC = ∠TOA. [D1.15, CN4]

**Step 5.** Therefore triangles OBC and OTA have two sides respectively equal and the included angles equal. By 1.4, their corresponding angles ∠OBC and ∠OTA are equal. Consequently ∠OTA is right. The natural choice here is 1.4: the two side equalities and their included-angle equality are already available. [1.4, D1.10]

**Step 6.** Produce TO through O to the opposite circumference of Γ, obtaining a diameter with endpoint T. The straight line AT is perpendicular to this diameter at T; therefore it falls outside Γ by 3.16. Since it meets Γ at T without cutting it, AT touches Γ. This applies the preceding proposition directly to establish touching. [P2, D1.17, 3.16, D3.2]

**Step 7.** If instead A lies on Γ, join OA and produce it through O to form a diameter with endpoint A. At A erect a perpendicular to that diameter. By 3.16 this perpendicular falls outside Γ and therefore touches Γ at A. Thus, from the given point, whether outside the circle or on its circumference, a straight line touching the circle has been drawn. An interior point is excluded, since a straight line through it cuts the circle rather than touching it. [P1, P2, D1.17, 1.11, 3.16, D3.2]

**USED:** 1.11, 1.4, 3.1, 3.16, CN4, CN5, D1.10, D1.15, D1.17, D3.2, P1, P2, P3
**Human refs (from References field):** 1.4, 3.1, 3.16
**Jaccard:** 0.231 — AI adds ['1.11', 'CN4', 'CN5', 'D1.10', 'D1.15', 'D1.17', 'D3.2', 'P1', 'P2', 'P3']

## Proposition 3.18
**Statement:** If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.

**Step 1.** Let the straight line \(t\) touch the circle at \(A\), and let \(O\) be its centre. Thus \(O\) is inside the circle, while \(t\) meets but does not cut it. Produce \(AO\) through \(O\) to meet the circumference again at \(B\); then \(AB\) is a diameter. [D1.15, D1.16, D3.2, P2, D1.17]

**Step 2.** Draw the straight line \(p\) through \(A\) perpendicular to \(AB\). [1.11] Apply 3.16 to each of the two semicircles on \(AB\): \(p\) falls outside the circle, and no straight line from \(A\) can be interposed between \(p\) and either semicircumference. **Path choice:** use this non-interposition assertion directly to exclude any other direction for the tangent. [3.16]

**Step 3.** Suppose that \(t\) is distinct from \(p\). One ray of \(t\) from \(A\) then points into the half-plane bounded by \(p\) that contains \(O\). If this ray follows \(AB\), it passes through the interior point \(O\), contrary to tangency. Otherwise it lies between \(AB\) and one of the rays of \(p\). Since \(t\) does not cut the circle, this ray cannot enter the corresponding semicircle; it would therefore be interposed, at \(A\), between that semicircumference and \(p\). This contradicts the non-interposition assertion of Step 2. Hence \(t=p\). [D1.15, D1.16, D3.2, 3.16]

**Step 4.** By construction, \(p\) makes right angles with the diameter \(AB\) at \(A\). Since \(t=p\) and \(AO\) lies along \(AB\), the adjacent angles made by \(AO\) with \(t\) are right angles. Therefore \(OA\) is perpendicular to the tangent \(t\), as required. [Step 2, Step 3, D1.10]

**USED:** 1.11, 3.16, D1.10, D1.15, D1.16, D1.17, D3.2, P2
**Human refs (from References field):** 1.17, 1.19
**Jaccard:** 0.000 — AI adds ['1.11', '3.16', 'D1.10', 'D1.15', 'D1.16', 'D1.17', 'D3.2', 'P2']; Human adds ['1.17', '1.19']

## Proposition 3.19
**Statement:** If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so drawn.

**Step 1.** Let the straight line t touch the circle at T, and let n be the given straight line through T perpendicular to t. Let O be the centre of the circle, and join OT. [Hypotheses; P1]

**Step 2.** Since t touches the circle at T, the straight line OT is perpendicular to t. This is the direct route: 3.18 applies immediately to the given tangent and the radius to its point of contact. [3.18]

**Step 3.** Take A distinct from T on t. Choose C distinct from T on n, on the opposite side of t from O, producing n through T if necessary. The angles OTA and ATC are both right angles, because OT and n are perpendicular to t. Thus these adjacent angles together equal two right angles. [P2; D1.10; Step 2 and the hypothesis]

**Step 4.** The rays TO and TC lie on opposite sides of t and make with TA adjacent angles equal to two right angles. Therefore TO and TC lie in one straight line, by the straight-line criterion 1.14, whose hypotheses are exactly those just established. Since TC lies on n, the centre O lies on n. Hence the centre lies on the straight line drawn through the point of contact at right angles to the tangent. [1.14]

**USED:** 1.14, 3.18, D1.10, P1, P2
**Human refs (from References field):** 3.18
**Jaccard:** 0.200 — AI adds ['1.14', 'D1.10', 'P1', 'P2']

## Proposition 3.20
**Statement:** In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.

**Step 1.** Let O be the centre of the circle, and let A, B, C be distinct points on its circumference. Let Γ be the arc AB not containing C, and let Θ be the central angular magnitude standing on Γ. We must prove Θ = 2∠ACB. The central magnitude is taken toward Γ; for a semicircular or larger arc, it is understood as the sum of its adjacent ordinary angles. [D3.9, D3.10]

**Step 2.** Join OA, OB, OC, CA and CB, and produce CO beyond O to meet the circumference at D. Thus CD is a diameter, O lies between C and D, and the rays CO and CD coincide. [P1, P2, D1.17]

**Step 3.** For either X = A or X = B, provided X ≠ D, the radii OX and OC are equal. Hence, in triangle OCX, ∠XCO = ∠CXO. Since OD is the continuation of CO, the exterior-angle theorem gives
∠XOD = ∠XCO + ∠CXO = 2∠XCO = 2∠XCD.
Here the last equality uses the coincident rays CO and CD. This is the direct path: use the exterior-angle statement of 1.32 because the equal radii make its two opposite interior angles equal. [D1.15, 1.5, 1.32, CN2, CN4]

**Step 4.** Suppose first that D is an endpoint of Γ, so D = A or D = B. Let X be the other endpoint. Then Θ is precisely ∠XOD, and ∠ACB is precisely ∠XCD. Step 3 therefore gives Θ = 2∠ACB. [Step 3; D3.9, D3.10, CN4]

**Step 5.** Suppose next that D lies in the interior of Γ. The diameter CD divides Γ into the arcs AD and DB lying in its two semicircles. Accordingly, CD lies inside ∠ACB, and OD divides the central angular region standing on Γ. Thus
∠ACB = ∠ACD + ∠DCB,
and
Θ = ∠AOD + ∠DOB.
Adding the two identities supplied by Step 3 gives
Θ = 2∠ACD + 2∠DCB = 2∠ACB.
This addition also applies when the central region is semicircular or reflex. [D1.17, D3.9, D3.10; Step 3; CN2]

**Step 6.** Finally, suppose D lies outside Γ and is not an endpoint. Then A and B lie in the same semicircle determined by CD. Interchange their names if necessary so that B lies between A and D along that semicircle. The corresponding angular regions are nested, giving
∠ACD = ∠ACB + ∠BCD,
and
∠AOD = Θ + ∠BOD.
Subtracting the identity ∠BOD = 2∠BCD from the identity ∠AOD = 2∠ACD established in Step 3 yields
Θ = 2∠ACD − 2∠BCD = 2∠ACB.
The last equality follows by subtracting the two copies of ∠BCD from the two copies of ∠ACD. [D1.17, D3.9, D3.10; Step 3; CN2, CN3]

**Step 7.** The point D either is an endpoint of Γ, lies in its interior, or lies outside it. Steps 4–6 therefore establish in every case that the angle at the centre is double the angle at the circumference standing on the same arc. [Steps 4–6; D3.9, D3.10]

**USED:** 1.32, 1.5, CN2, CN3, CN4, D1.15, D1.17, D3.10, D3.9, P1, P2
**Human refs (from References field):** 1.32, 1.5
**Jaccard:** 0.182 — AI adds ['CN2', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D3.10', 'D3.9', 'P1', 'P2']

## Proposition 3.21
**Statement:** In a circle the angles in the same segment are equal to one another.

**Step 1.** Let AB be the base of a segment of a circle, and let C and D be any two points on its circumference, distinct from A and B. Join AC, BC, AD, and BD. The angles ACB and ADB are angles in the given segment, and both stand upon the same arc AB opposite that segment. Denote this common arc by Γ. [P1, D3.6, D3.8, D3.9]

**Step 2.** Find the centre O of the circle and join OA and OB. Let Θ be the central angular magnitude subtending Γ, taking the angular magnitude towards Γ, whether smaller than, equal to, or greater than two right angles. The direct route is to apply 3.20: it compares each given angle with the central angular magnitude having precisely its arc as base. [3.1, P1, 3.20]

**Step 3.** Since Θ and angle ACB have Γ as their common base, Θ is double angle ACB. Likewise, Θ is double angle ADB. Consequently, the doubles of angles ACB and ADB are equal. [3.20, CN1]

**Step 4.** Therefore angle ACB equals angle ADB. Indeed, if either angle exceeded the other by a nonzero angular part, its double would equal the other's double together with two copies of that part, and so would be greater, contradicting Step 3. Since C and D were arbitrary, the angles in the same segment are equal to one another. [CN2, CN5, D3.8]

**USED:** 3.1, 3.20, CN1, CN2, CN5, D3.6, D3.8, D3.9, P1
**Human refs (from References field):** 3.20
**Jaccard:** 0.111 — AI adds ['3.1', 'CN1', 'CN2', 'CN5', 'D3.6', 'D3.8', 'D3.9', 'P1']

## Proposition 3.22
**Statement:** The opposite angles of quadrilaterals in circles are equal to two right angles.

**Step 1.** Let ABCD be a quadrilateral inscribed in a circle, with its vertices in that order around the circumference [D4.3]. Join AC and BD [P1]. We shall prove that each pair of opposite interior angles is together equal to two right angles.

**Step 2.** Path choice: the diagonals give angles in the same segment directly, so use 3.21 without introducing the centre. Since C and D lie in the same segment on AB, and A and D lie in the same segment on BC,
∠ADB = ∠ACB and ∠BDC = ∠BAC [3.21].

**Step 3.** The diagonal DB divides the interior angle ADC into ∠ADB and ∠BDC. Adding the equalities of Step 2 therefore gives
∠ADC = ∠ADB + ∠BDC = ∠ACB + ∠BAC [CN2].

**Step 4.** In triangle ABC,
∠ABC + ∠ACB + ∠BAC = two right angles [1.32].
Adding ∠ABC to the equality in Step 3 and comparing with this triangle-angle sum gives
∠ABC + ∠ADC = two right angles [CN2, CN1].

**Step 5.** Since B and C lie in the same segment on AD, ∠ABD = ∠ACD [3.21]. Also, ∠ADB = ∠ACB by Step 2. The diagonal CA divides the interior angle BCD into ∠ACB and ∠ACD; hence, adding these equalities,
∠BCD = ∠ACB + ∠ACD = ∠ADB + ∠ABD [CN2].

**Step 6.** In triangle ABD,
∠BAD + ∠ADB + ∠ABD = two right angles [1.32].
Adding ∠BAD to the equality in Step 5 and comparing with this triangle-angle sum gives
∠BAD + ∠BCD = two right angles [CN2, CN1].
Thus each pair of opposite angles of a quadrilateral inscribed in a circle is together equal to two right angles.

**USED:** 1.32, 3.21, CN1, CN2, D4.3, P1
**Human refs (from References field):** 1.32, 3.21
**Jaccard:** 0.333 — AI adds ['CN1', 'CN2', 'D4.3', 'P1']

## Proposition 3.23
**Statement:** On the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.

**Step 1.** Suppose, for contradiction, that two similar but unequal circular segments are constructed on the same base AB and on the same side of it. Their supporting circles must be distinct: otherwise the chord AB and the arc on the specified side would bound the same figure, making the segments equal (D3.6, CN4).

**Step 2.** The two circles already have A and B in common, so their arcs cannot intersect again (3.10). Consequently, the segments on the specified side of AB are nested. Call the inner segment S and the outer segment T. Since they are unequal, choose a point C, other than A or B, on the arc of S strictly inside T (D3.6).

**Step 3.** Join AC and produce it beyond C to meet the arc of T at D; join BC and BD (P1, P2). Thus A, C, D occur in that order on one straight line. This construction selects the exterior-angle route: the two segment angles will be an exterior angle and a remote interior angle of triangle BCD.

**Step 4.** The angles ACB and ADB are angles in S and T respectively (D3.8). Since these segments are similar, ∠ACB = ∠ADB (D3.11).

**Step 5.** In triangle BCD, the side DC is produced through C to A. Therefore its exterior angle ACB is greater than its remote interior angle CDB (1.16, which applies directly to this construction). But the rays DC and DA coincide, so ∠CDB is precisely ∠ADB. Hence ∠ACB > ∠ADB, contradicting Step 4. Therefore two similar and unequal circular segments cannot be constructed on the same straight line and on the same side.

**USED:** 1.16, 3.10, CN4, D3.11, D3.6, D3.8, P1, P2
**Human refs (from References field):** 1.16, D3.11
**Jaccard:** 0.250 — AI adds ['3.10', 'CN4', 'D3.6', 'D3.8', 'P1', 'P2']

## Proposition 3.24
**Statement:** Similar segments of circles on equal straight lines are equal to one another.

**Step 1.** Let the given similar circular segments be S and T, standing on the equal straight lines AB and CD respectively. Their angles in the segments are equal, by the definition of similar segments (D3.11).

**Step 2.** Choose superposition to bring the equal bases into the common-base configuration. Place S upon the plane of T so that A coincides with C, B with D, and both segments lie on the same side of CD. This placement is possible because AB = CD. Denote the placed segment by S′; it retains the magnitude and angles of S (superposition; CN4).

**Step 3.** Thus S′ and T are similar segments on the same straight line CD and on the same side of it (D3.11). By 3.23, two such segments cannot be unequal. Hence S′ = T. This uses the preceding common-base proposition directly.

**Step 4.** Since S = S′ and T = S′, we have S = T (CN1). Therefore similar segments of circles on equal straight lines are equal to one another.

**USED:** 3.23, CN1, CN4, D3.11
**Human refs (from References field):** 3.10
**Jaccard:** 0.000 — AI adds ['3.23', 'CN1', 'CN4', 'D3.11']; Human adds ['3.10']

## Proposition 3.25
**Statement:** Given a segment of a circle, to describe the complete circle of which it is a segment.

**Step 1.** Let AB be the straight boundary of the given segment, and choose C on its circular boundary, distinct from A and B and not on AB (D3.6). Join AC (P1). Path choice: use the perpendicular bisectors of the two chords AB and AC. The centre will be located by 3.3, which applies directly to chord-midpoints and avoids distinguishing segments smaller or greater than a semicircle.

**Step 2.** Bisect AB at M and AC at N (1.10). Construct the straight line ℓ perpendicular to AB at M, and the straight line m perpendicular to AC at N (1.11).

**Step 3.** For verification only, let Γ denote the circle to which the given circular boundary belongs, and let S denote its centre. Such a circle and centre exist by the meaning of a circular segment and a circle (D3.6, D1.15, D1.16). Neither Γ nor S is assumed to have been constructed.

**Step 4.** We show that S lies on each constructed perpendicular. Consider either chord AB or AC, writing its endpoints as X, Y and its midpoint as T. Its radii satisfy SX = SY (D1.15). If S lies on the straight line XY, it must lie between X and Y: otherwise one of SX, SY would properly contain the other, contradicting their equality (CN5). Thus S is the midpoint T and lies on the perpendicular at T. If S does not lie on XY, join ST (P1). This line passes through the centre and bisects a chord not through the centre; therefore ST is perpendicular to XY (3.3). Perpendicular straight lines at the same point of a given straight line coincide, by 1.14. Hence S again lies on the constructed perpendicular at T. Applying this to both chords gives S on both ℓ and m.

**Step 5.** The lines ℓ and m are distinct. Indeed, A, M, N are non-collinear, since M and N lie respectively on the non-collinear chords AB and AC. If ℓ and m coincided, triangle AMN would have right angles at both M and N, contrary to 1.17. Since the two distinct constructed lines both contain S, they meet. Produce them as necessary and take their intersection O (P2). By Step 4, O is S.

**Step 6.** Describe the circle with centre O and radius OA (P3). Since O = S and A lies on Γ, this is the circle with the centre and radius of Γ, and therefore it is Γ itself (D1.15, D1.16). Its circumference consequently contains the whole given circular boundary; together with AB, that boundary encloses the given segment (D3.6). Thus the complete circle of which the given figure is a segment has been described.

**USED:** 1.10, 1.11, 1.14, 1.17, 3.3, CN5, D1.15, D1.16, D3.6, P1, P2, P3
**Human refs (from References field):** 1.6, 3.9
**Jaccard:** 0.000 — AI adds ['1.10', '1.11', '1.14', '1.17', '3.3', 'CN5', 'D1.15', 'D1.16', 'D3.6', 'P1', 'P2', 'P3']; Human adds ['1.6', '3.9']

## Proposition 3.26
**Statement:** In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

**Step 1.** Let two equal circles have centres O and U, and let the circumferences to be compared be the arcs AB and DE. Choose P on the complementary arc from A to B and Q on the complementary arc from D to E, taking P and Q to be the given vertices when the equal angles are at the circumferences. Thus ∠APB and ∠DQE stand on the arcs being compared (D3.8, D3.9).

**Step 2.** Join OA, OB, UD, UE and the chords AB, DE (P1). Since the circles are equal, their radii are equal; hence OA = UD and OB = UE (D1.15, D3.1). Denote the central angular magnitudes standing on the selected arcs by α and β, respectively; for a major arc, use the reflex angular magnitude.

**Step 3.** By 3.20, α is double ∠APB, and β is double ∠DQE. Consequently, whether the given equality is α = β or ∠APB = ∠DQE, both equalities hold. Equal angles have equal doubles by CN2; conversely, unequal angles would have unequal doubles, since the double of the larger would contain the double of the smaller as a proper part (CN2, CN5).

**Step 4.** We obtain AB = DE. Indeed, if α and β are less than two right angles, the triangles AOB and DUE have two corresponding sides and their included angles equal, so their bases are equal by 1.4. If α and β are reflex, the ordinary included angles of these triangles are their remainders from four right angles and are therefore equal; 1.4 again applies (1.13, P4, CN2, CN3). If α and β are two right angles, AB and DE are diameters and are equal by D1.17 and D3.1.

**Step 5.** Consider the segments bounded by chord AB and arc APB, and by chord DE and arc DQE. The equal angles ∠APB and ∠DQE are angles in these segments. Therefore the segments are similar (D3.6, D3.8, D3.11).

**Step 6.** These similar segments stand on the equal straight lines AB and DE. By 3.24 they are equal, and their corresponding circular boundaries, the arcs APB and DQE, are consequently equal (D3.6). This is the direct application of 3.24: equal bases and similar segments have already been established.

**Step 7.** The whole circumferences of the two circles are equal. For, when their centres and a pair of equal radii are superposed, their circumferences coincide, since both circles have the same radius (D1.15, D3.1); coincident magnitudes are equal (CN4).

**Step 8.** Subtract the equal arcs APB and DQE from the equal whole circumferences. The remaining arcs AB and DE—the arcs on which the given angles stand—are equal (CN3). Therefore, in equal circles, equal angles stand on equal circumferences, whether the angles are at the centres or at the circumferences.

**USED:** 1.13, 1.4, 3.20, 3.24, CN2, CN3, CN4, CN5, D1.15, D1.17, D3.1, D3.11, D3.6, D3.8, D3.9, P1, P4
**Human refs (from References field):** 1.4, 3.24, D3.11
**Jaccard:** 0.176 — AI adds ['1.13', '3.20', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.17', 'D3.1', 'D3.6', 'D3.8', 'D3.9', 'P1', 'P4']

## Proposition 3.27
**Statement:** In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.

**Step 1.** Let two equal circles have equal circumferences (arcs) AB and DE. Let ∠AXB and ∠DYE stand on these arcs, with X and Y either both centres or both points on the respective circumferences. We prove equality in either case by the same argument. [D3.9]

**Step 2.** Choose the direct route through 3.26, whose two cases match precisely the two cases here. Suppose the angles are unequal; after interchanging the circles if necessary, let ∠AXB be the greater. At X construct, strictly inside ∠AXB, an angle ∠AXZ equal to ∠DYE, and extend its second side to meet the first circle at Z. Because this side lies strictly inside ∠AXB, Z lies strictly between A and B on the intercepted arc AB. Thus the intercepted arc AZ is a proper part of arc AB. [1.23, P2, D3.9]

**Step 3.** The equal angles ∠AXZ and ∠DYE stand in equal circles and are of the same kind—both central or both circumferential. Therefore their intercepted arcs AZ and DE are equal. But arc DE equals arc AB by hypothesis; hence arc AZ equals arc AB. [3.26, CN1]

**Step 4.** This is impossible: arc AB is greater than its proper part AZ. Consequently the angles cannot be unequal, and ∠AXB = ∠DYE. Since the argument applies to either choice of vertices, angles standing on equal circumferences in equal circles are equal, whether they stand at the centres or at the circumferences. [CN5]

**USED:** 1.23, 3.26, CN1, CN5, D3.9, P2
**Human refs (from References field):** 1.23, 3.20, 3.26
**Jaccard:** 0.286 — AI adds ['CN1', 'CN5', 'D3.9', 'P2']; Human adds ['3.20']

## Proposition 3.28
**Statement:** In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

**Step 1.** Let AB and CD be equal chords of equal circles Γ and Δ. Find their centres O and P, respectively, and join OA, OB, PC, and PD (3.1, P1). The radii within each circle are equal, and the radii of the two equal circles are equal; hence OA = PC and OB = PD (D1.15, D3.1).

**Step 2.** The whole circumferences of Γ and Δ are equal. Indeed, on superposing their centres, their equal radii make their circumferences coincide; coincident magnitudes are equal (D1.15, D3.1, CN4).

**Step 3.** If either chord is a diameter, the other is also a diameter: the diameters of the two circles are equal, whereas every non-diameter chord is less than a diameter (D3.1, 3.15, CN1). In this case the arcs cut off are semicircumferences, and corresponding semicircumferences coincide when the centres and diameters are superposed; thus they are equal (D1.17, CN4). It remains to consider the case in which neither chord is a diameter.

**Step 4.** In triangles AOB and CPD, we have OA = PC, OB = PD, and AB = CD. Therefore ∠AOB = ∠CPD by 1.8. We use central rather than inscribed angles because the two radius triangles give their equality directly.

**Step 5.** These ordinary central angles stand on the respective lesser arcs cut off by AB and CD (D3.9). Equal angles at the centres of equal circles stand on equal circumferences; therefore the lesser arc cut off by AB equals the lesser arc cut off by CD (3.26).

**Step 6.** Subtract these equal lesser arcs from the equal whole circumferences established in Step 2. The remaining greater arcs are equal (CN3). Consequently, in equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

**USED:** 1.8, 3.1, 3.15, 3.26, CN1, CN3, CN4, D1.15, D1.17, D3.1, D3.9, P1
**Human refs (from References field):** 1.8, 3.26
**Jaccard:** 0.167 — AI adds ['3.1', '3.15', 'CN1', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D3.1', 'D3.9', 'P1']

## Proposition 3.29
**Statement:** In equal circles equal circumferences are subtended by equal straight lines.

**Step 1.** Let two equal circles have equal arcs with endpoints A, B and C, D respectively. Join AB and CD; these are the straight lines subtending the given arcs. We must prove AB = CD. [P1]

**Step 2.** We may reduce to arcs less than semicircles. Indeed, equal circles have equal complete circumferences and equal semicircumferences: their equal radii allow their circular boundaries, and corresponding halves bounded by diameters, to coincide on superposition. [D3.1, D1.15, D1.17, CN4] Thus, if the given equal arcs are greater than semicircles, their complementary arcs are equal and have the same subtending straight lines. [CN3] If they are semicircles, AB and CD are diameters and therefore are equal, proving the result in that case. [D1.18, D3.1] Henceforth take the equal arcs to be less than semicircles.

**Step 3.** Find the centres O and Q of the respective circles, and join OA, OB, QC, and QD. [3.1, P1]

**Step 4.** Since the circles are equal, their radii are equal; in particular, OA = QC and OB = QD. [D1.15, D3.1]

**Step 5.** The angles AOB and CQD stand at the centres on the equal arcs. Therefore ∠AOB = ∠CQD. [3.27] We choose the centre-angle form of this proposition because it directly supplies the included angles between the equal radii.

**Step 6.** The triangles AOB and CQD have two sides respectively equal and the included angles equal. Therefore their bases AB and CD are equal by side–angle–side. [1.4] Consequently, in equal circles equal circumferences are subtended by equal straight lines.

**USED:** 1.4, 3.1, 3.27, CN3, CN4, D1.15, D1.17, D1.18, D3.1, P1
**Human refs (from References field):** 1.4, 3.27
**Jaccard:** 0.200 — AI adds ['3.1', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D1.18', 'D3.1', 'P1']

## Proposition 3.30
**Statement:** To bisect a given circumference.

**Step 1.** Let the given circumference be the arc Γ with endpoints A and B. Join AB (P1). The chord AB and Γ bound a segment of a circle (D3.6); describe the complete circle of which it is a segment (3.25).

**Step 2.** Choose a point C on the complementary arc, and join CA and CB (P1). Bisect the angle ACB by a ray from C (1.9). We use the angle-to-arc route, since this construction supplies equal angles at the circumference directly.

**Step 3.** The bisecting ray lies inside the angle ACB and therefore crosses the opposite side AB of triangle ACB at an interior point E (1.9). Since AB lies within the circle, E is inside the circle (3.2). Continue the ray beyond E until it meets the circumference at D (P2). This intersection is on the side of AB opposite C, and hence on the given arc Γ, between A and B (D3.6).

**Step 4.** By construction, ∠ACD = ∠DCB (1.9). These angles stand respectively on the subarcs AD and DB of Γ (D3.9). Equal angles at the circumference stand on equal circumferences, applying 3.26 within the same circle. Therefore arc AD equals arc DB, and D bisects the given circumference Γ, as required.

**USED:** 1.9, 3.2, 3.25, 3.26, D3.6, D3.9, P1, P2
**Human refs (from References field):** 1.4, 3.28
**Jaccard:** 0.000 — AI adds ['1.9', '3.2', '3.25', '3.26', 'D3.6', 'D3.9', 'P1', 'P2']; Human adds ['1.4', '3.28']

## Proposition 3.31
**Statement:** In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

**Step 1.** Find the centre O of the given circle. Choose A on its circumference and produce AO to meet the circumference again at C, so that AC is a diameter. Take any other point B on the circumference, and join AB, BC, and BO. Thus ABC is an angle in a semicircle. [3.1, P1, P2, D1.17, D1.18, D3.8]

**Step 2.** The radii OA, OB, and OC are equal. Hence, in the isosceles triangles AOB and BOC, ∠ABO = ∠BAO and ∠OBC = ∠BCO. Since O lies between A and C, these give ∠ABO = ∠BAC and ∠OBC = ∠BCA. Adding, we obtain ∠ABC = ∠BAC + ∠BCA. [D1.15, 1.5, CN2]

**Step 3.** Produce AB through B to F. We use the exterior-angle form of the triangle theorem, since it directly supplies an angle adjacent to ∠ABC: ∠CBF = ∠BAC + ∠BCA. Consequently ∠CBF = ∠ABC. These are equal adjacent angles made by BC standing on the straight line ABF, so each is right. Because B was arbitrary, every angle in a semicircle is right. Write R for a right angle; all right angles are equal. [P2, 1.32, CN1, D1.10, D3.8, P4]

**Step 4.** The chord AB is an arbitrary chord which is not a diameter. The segment bounded by AB and the arc AB not containing C is properly contained in one semicircle on AC; the complementary segment properly contains the opposite semicircle. These are therefore the less and greater segments, respectively, and C lies on the arc of the greater segment. [3.2, D1.17, D1.18, D3.6, CN5]
Using the triangle-angle sum already available from 1.32, together with ∠ABC = R, we have ∠BAC + ∠BCA = R. Thus ∠BCA < R. Every angle in the greater segment equals ∠BCA, and is therefore less than a right angle. [1.32, CN3, CN5, 3.21, D3.8]

**Step 5.** Take any point Q on the arc of the less segment and join QA and QB. The points A, Q, B, C, in that order, form a quadrilateral in the circle. The cyclic-quadrilateral theorem is the direct choice here, because it gives the supplement of the angle just bounded: ∠AQB + ∠ACB = 2R. Since ∠ACB < R, its supplement ∠AQB is greater than R. As Q was arbitrary, every angle in the less segment is greater than a right angle. [P1, 3.22, CN3, CN5, D3.8]

**Step 6.** Consider now the angle **of** the greater segment at B: its boundaries are BA and the arc leaving B towards C. The chord BC lies inside the circle and within this greater segment. Hence the rectilineal angle ABC is a proper part of that curvilinear segment-angle. Since ∠ABC = R by Step 3, the angle of the greater segment is greater than a right angle. [3.2, D3.6, D3.7, CN5]

**Step 7.** Produce CB through B to E. The adjacent angles ABC and ABE together equal two right angles; therefore ∠ABE = R. [P2, 1.13, CN3]
The arc BA of the less segment lies on the side of AB opposite C, and on the side of BC containing A. Indeed, it cannot cross BC: any third circumference point on that line would make one circumference point an interior point of a chord, contrary to 3.2. Thus this arc lies within the angle ABE. The angle of the less segment at B, bounded by BA and that arc, is consequently a proper part of ∠ABE, and is less than a right angle. [3.2, D3.6, D3.7, CN5]

**Step 8.** The chord AB was arbitrary, and its endpoints may be interchanged, so Steps 6–7 apply at either endpoint. Together, Steps 3–7 establish all the required distinctions: the angle in a semicircle is right; the angle in a greater segment is less than a right angle; the angle in a less segment is greater than a right angle; while the angle of the greater segment is greater than a right angle, and the angle of the less segment is less than a right angle. [D3.7, D3.8]

**USED:** 1.13, 1.32, 1.5, 3.1, 3.2, 3.21, 3.22, CN1, CN2, CN3, CN5, D1.10, D1.15, D1.17, D1.18, D3.6, D3.7, D3.8, P1, P2, P4
**Human refs (from References field):** 1.17, 1.32, 1.5, 3.22, D1.10
**Jaccard:** 0.182 — AI adds ['1.13', '3.1', '3.2', '3.21', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'D1.18', 'D3.6', 'D3.7', 'D3.8', 'P1', 'P2', 'P4']; Human adds ['1.17']

## Proposition 3.32
**Statement:** If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

**Step 1.** Let the straight line XAY touch the circle at A, and let AB be the chord drawn from A (D3.2). At A erect a perpendicular to XY and produce it into the circle to meet the circumference again at C (1.11, P2). The centre lies on this perpendicular, so AC is a diameter (3.19, D1.17). Both ∠XAC and ∠CAY are right angles (D1.10). **Path choice:** constructing the perpendicular naturally invokes 3.19 and supplies a diameter, allowing direct use of the semicircle theorem 3.31.

**Step 2.** If B = C, both angles between AB and the tangent are right. Every angle in either segment cut off by the diameter AB is also right, by 3.31. Hence the required equalities hold in this case (P4).

**Step 3.** Suppose B ≠ C. Interchange the names X and Y if necessary so that AB lies inside ∠XAC. The segment with base AB containing C is then on the opposite side of AB from X; the other segment is on the opposite side from Y (D3.6). Join BC (P1). Since AC is a diameter, ∠ABC is right (3.31).

**Step 4.** The three angles of triangle ABC equal two right angles (1.32). Subtracting the right angle ∠ABC gives
∠BAC + ∠ACB = one right angle
(P4, CN3).
But AB divides the right angle XAC, so
∠XAB + ∠BAC = one right angle
(D1.10, P4).
Subtracting the common angle BAC therefore gives
∠XAB = ∠ACB
(CN3).

**Step 5.** Let P be any point, other than A and B, on the circumference of the segment containing C, and join PA and PB (P1). If P = C, Step 4 already applies; otherwise, angles in the same segment give ∠APB = ∠ACB (3.21). Consequently ∠APB = ∠XAB (CN1). Thus the angle between AX and AB equals every angle in its alternate segment (D3.8). Here 3.21 is the natural choice because the two angles lie in the very same segment.

**Step 6.** Let Q be any point, other than A and B, on the circumference of the other segment, and join QA and QB (P1). The quadrilateral AQBC has its vertices on the circle, so its opposite angles satisfy
∠AQB + ∠ACB = two right angles
(3.22).
Since AX and AY are opposite rays,
∠XAB + ∠BAY = two right angles
(1.13).
By Step 4, ∠XAB = ∠ACB. Subtracting these equal angles from the equal sums yields
∠BAY = ∠AQB
(P4, CN3).
This is the angle in the segment opposite AY across AB, hence the alternate segment for ∠BAY (D3.8).

**Step 7.** Since P and Q were arbitrary, each angle made by the chord with the tangent equals the angles in its alternate segment, as required (Steps 5–6, D3.8).

**USED:** 1.11, 1.13, 1.32, 3.19, 3.21, 3.22, 3.31, CN1, CN3, D1.10, D1.17, D3.2, D3.6, D3.8, P1, P2, P4
**Human refs (from References field):** 1.32, 3.19, 3.22, 3.31
**Jaccard:** 0.235 — AI adds ['1.11', '1.13', '3.21', 'CN1', 'CN3', 'D1.10', 'D1.17', 'D3.2', 'D3.6', 'D3.8', 'P1', 'P2', 'P4']

## Proposition 3.33
**Statement:** On a given straight line to describe a segment of a circle admitting an angle equal to a given rectilineal angle.

**Step 1.** Let AB be the given straight line and θ the given rectilineal angle. At A construct a ray AT such that ∠BAT = θ (1.23). We choose the tangent–chord route: construct a circle through A and B tangent to AT at A, and then apply 3.32 directly, rather than introduce angles at the centre.

**Step 2.** Bisect AB at M (1.10). Write R for a right angle. If θ = R, take O = M; then AO is perpendicular to AT (D1.10). The next two steps construct O when θ is not right.

**Step 3.** Suppose θ ≠ R. Draw a perpendicular to AT at A (1.11), choosing its ray AU as follows. If θ < R, take AU on the opposite side of AB from T; then, putting β = ∠BAU, we have β + θ = R. If θ > R, take AU on the same side of AB as T; then β + R = θ. These angle decompositions follow from the constructed perpendicular (D1.10). Moreover, θ is less than two right angles, since its adjacent supplementary angle completes two right angles (P2, 1.13). Consequently, in either case, 0 < β < R (CN3, CN5).

**Step 4.** At M erect a perpendicular to AB, taking its ray on the same side of AB as AU (1.11). With AM as transversal, the interior angles on that side are β and a right angle (D1.10, P4). Their sum is less than two right angles, so this perpendicular and AU, produced if necessary, meet on that side; call their intersection O (P2, P5). Thus, in the non-right case, OM is perpendicular to AB and AO is perpendicular to AT.

**Step 5.** We have OA = OB. Indeed, if O = M, this is the bisection of AB from Step 2. Otherwise, join OB (P1). The triangles OMA and OMB have AM = MB, OM common, and equal included right angles at M (D1.10); hence OA = OB by 1.4. Describe the circle with centre O and radius OA (P3). It passes through both A and B because OA = OB (D1.15).

**Step 6.** Produce AO through O to meet the circumference again at E, so that AE is a diameter (P2, D1.17). In every case AT is perpendicular to AE at A. Therefore AT lies outside the circle except at A, by 3.16, and consequently touches the circle there (D3.2). Here 3.16 applies directly because the perpendicular to the diameter has already been constructed.

**Step 7.** Take the segment bounded by AB and the arc lying on the opposite side of AB from T (D3.6). Let C be any point of that arc other than A or B, and join CA and CB (P1). The angle ACB is an angle in this segment (D3.8). Since AT touches the circle at A and AB cuts across it, the tangent–chord theorem gives ∠ACB = ∠BAT: this is precisely the alternate segment for the angle BAT (3.32). But ∠BAT = θ by construction, so ∠ACB = θ (CN1). Thus the constructed segment on the given straight line AB admits an angle equal to the given rectilineal angle, as required.

**USED:** 1.10, 1.11, 1.13, 1.23, 1.4, 3.16, 3.32, CN1, CN3, CN5, D1.10, D1.15, D1.17, D3.2, D3.6, D3.8, P1, P2, P3, P4, P5
**Human refs (from References field):** 1.4, 3.16, 3.31, 3.32
**Jaccard:** 0.136 — AI adds ['1.10', '1.11', '1.13', '1.23', 'CN1', 'CN3', 'CN5', 'D1.10', 'D1.15', 'D1.17', 'D3.2', 'D3.6', 'D3.8', 'P1', 'P2', 'P3', 'P4', 'P5']; Human adds ['3.31']

## Proposition 3.34
**Statement:** From a given circle to cut off a segment admitting an angle equal to a given rectilineal angle.

**Step 1.** Let Γ be the given circle and α the given rectilineal angle. Choose a point A on Γ and draw the tangent t at A; choose a point T on t distinct from A. This tangent is constructible by 3.17. We use the tangent–chord route because it gives the required angle directly in the given circle.

**Step 2.** At A construct, on the side of t containing the circle, a ray making with AT an angle equal to α (1.23). The tangent is perpendicular to the radius ending at A (3.18), so the no-interposition assertion of 3.16 applies: this inward ray, distinct from the tangent, enters the circle. Produce it to meet the circumference again at B (P2). Thus ∠TAB = α.

**Step 3.** Select the segment S bounded by AB and the arc AB lying on the side of the line AB opposite T (D3.6). Take any point C on this arc other than A and B, and join CA and CB (P1). Then ∠ACB is an angle in S (D3.8).

**Step 4.** Since t touches Γ at A and AB cuts the circle, the angle between AT and AB equals the angle in the alternate segment S; therefore ∠ACB = ∠TAB (3.32). This theorem is the direct choice because it applies immediately to the tangent and chord just constructed. Since ∠TAB = α, we obtain ∠ACB = α (CN1). As C was arbitrary, the segment S admits an angle equal to the given rectilineal angle (D3.8). Thus the required segment has been cut off from the given circle.

**USED:** 1.23, 3.16, 3.17, 3.18, 3.32, CN1, D3.6, D3.8, P1, P2
**Human refs (from References field):** 1.23, 3.32
**Jaccard:** 0.200 — AI adds ['3.16', '3.17', '3.18', 'CN1', 'D3.6', 'D3.8', 'P1', 'P2']

## Proposition 3.35
**Statement:** If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.

**Step 1.** Let the chords AB and CD intersect at E inside the circle. Find the centre O, and join OA and OC. Write S(UV) for the square on UV, and R(UV,WZ) for the rectangle contained by UV and WZ. We must prove R(AE,EB) = R(CE,ED). [3.1, P1, D1.22, D2.1]

**Step 2.** If E coincides with O, then AE, EB, CE, and ED are equal radii. Consequently the two rectangles are equal squares, and the conclusion follows. Henceforth suppose E differs from O, and join OE. [D1.15, D1.22, D2.1, CN4, P1]

**Step 3.** Take XY to denote either AB or CD. We shall show that
R(XE,EY) + S(OE) = S(OX).
The path chosen is the internal-cut identity of 2.5, since E lies between the endpoints of each chord; where necessary, 1.47 will connect the relevant squares. First, if XY passes through O, then OX = OY, so XY is cut equally at O and unequally at E. Therefore
R(XE,EY) + S(OE) = S(OX).
[D1.15, 2.5]

**Step 4.** Now suppose XY does not pass through O. Bisect XY at M and join OM. Since a straight line through the centre bisects the chord, OM cuts XY at right angles. Thus, in the right-angled triangle OMX,
S(MX) + S(OM) = S(OX).
[1.10, P1, 3.3, 1.47]

**Step 5.** If E coincides with M, then XE = EY = MX, so R(XE,EY) = S(MX), while OE is OM. Substitution in the equality of Step 4 gives
R(XE,EY) + S(OE) = S(OX).
[D1.22, D2.1, CN4, CN1]

**Step 6.** If E differs from M, then XY is cut equally at M and unequally at E. Hence
R(XE,EY) + S(ME) = S(MX).
Adding S(OM) to both sides and using Step 4 gives
R(XE,EY) + S(ME) + S(OM) = S(OX).
[2.5, CN2, CN1]

**Step 7.** Triangle OME is right-angled at M, so
S(ME) + S(OM) = S(OE).
Substituting this into Step 6 yields
R(XE,EY) + S(OE) = S(OX).
Together with Steps 3 and 5, this establishes the equality for either chord in every case. [3.3, 1.47, CN1]

**Step 8.** Applying the established equality to AB and CD gives
R(AE,EB) + S(OE) = S(OA),
R(CE,ED) + S(OE) = S(OC).
Since OA and OC are radii, their squares are equal. The left-hand sums are therefore equal; subtracting their common square S(OE) gives
R(AE,EB) = R(CE,ED).
Thus the rectangle contained by the segments of one straight line equals the rectangle contained by the segments of the other. [D1.15, CN4, CN1, CN3]

**USED:** 1.10, 1.47, 2.5, 3.1, 3.3, CN1, CN2, CN3, CN4, D1.15, D1.22, D2.1, P1
**Human refs (from References field):** 1.47, 2.5, 3.3
**Jaccard:** 0.231 — AI adds ['1.10', '3.1', 'CN1', 'CN2', 'CN3', 'CN4', 'D1.15', 'D1.22', 'D2.1', 'P1']

## Proposition 3.36
**Statement:** If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the circle and the other touch it, the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference will be equal to the square on the tangent.

**Step 1.** Let P be the exterior point, let the secant meet the circle first at A and then at B, and let PT touch the circle at T. Write R for the rectangle contained by PB and PA, and XY² for the square on XY. Find the centre O of the circle, bisect AB at M, and join OP, OA, and OT (3.1, 1.10, P1).

**Step 2.** Since O is the centre and T is the point of contact, OT is perpendicular to PT (3.18). Therefore, in the right-angled triangle OTP,
PO² = PT² + OT² (1.47).
Also OA = OT, being radii of the same circle (D1.15).

**Step 3.** The straight line AB is bisected at M and produced beyond A to P. Thus 2.6 applies directly—the relevant path choice is the bisected-and-produced-line identity—and gives
R + AM² = PM² (2.6).

**Step 4.** First suppose the secant passes through O. The equal radii OA and OB then make O the midpoint M of AB (D1.15). Hence PM = PO and AM = OA = OT. Substituting in Step 3 gives
R + OT² = PO² (CN1).

**Step 5.** Now suppose the secant does not pass through O. Join OM (P1). Since the straight line through the centre O bisects the chord AB at M, it is perpendicular to AB (3.3). Consequently the triangles OMP and OMA are right-angled at M, and
PO² = PM² + OM²,
OA² = AM² + OM² (1.47).

**Step 6.** Add OM² to both sides of the equality in Step 3 (CN2):
R + AM² + OM² = PM² + OM².
Using the two equalities in Step 5, this becomes
R + OA² = PO² (CN1).
Since OA = OT, it follows that
R + OT² = PO² (D1.15, CN1).

**Step 7.** In either case, therefore, R + OT² = PO². But Step 2 gives PT² + OT² = PO². Equating these two expressions and subtracting the common square OT² yields R = PT² (CN1, CN3). Thus the rectangle contained by the whole secant PB and its exterior portion PA equals the square on the tangent PT, as required.

**USED:** 1.10, 1.47, 2.6, 3.1, 3.18, 3.3, CN1, CN2, CN3, D1.15, P1
**Human refs (from References field):** 1.47, 2.6, 3.18, 3.3
**Jaccard:** 0.364 — AI adds ['1.10', '3.1', 'CN1', 'CN2', 'CN3', 'D1.15', 'P1']

## Proposition 3.37
**Statement:** If a point be taken outside a circle and from the point there fall on the circle two straight lines, if one of them cut the circle, and the other fall on it, and if further the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference be equal to the square on the straight line which falls on the circle, the straight line which falls on it will touch the circle.

**Step 1.** Let P be outside the given circle, let the secant meet it at A and B in the order P, A, B, and let C be the point on the circumference at which the other straight line PC falls. By hypothesis, the rectangle contained by PB and PA equals the square on PC. We must prove that PC touches the circle.

**Step 2.** Draw a tangent PT from P, touching the circle at T (3.17). If T coincides with C, the conclusion already holds. Otherwise, by 3.36, the rectangle contained by PB and PA equals the square on PT. Hence the squares on PT and PC are equal (hypothesis; CN1). This comparison with a constructed tangent is our chosen route.

**Step 3.** Therefore PT = PC. Indeed, if either segment were greater, 2.4, applied to the greater segment divided into a segment equal to the lesser and the remaining segment, would express its square as the square on the lesser together with the square on the remainder and twice the rectangle contained by the lesser and the remainder. Its square would consequently be greater, contrary to their equality (2.4; CN5).

**Step 4.** Find the centre O of the circle and join OP, OT, and OC (3.1; P1). The radii OT and OC are equal (D1.15), and OP is common (CN4). Since PT touches the circle at T, angle PTO is right (3.18).

**Step 5.** The points P, C, O are not collinear: otherwise one of PC, CO, OP would equal the sum of the other two, contradicting the strict triangle inequalities for the equal corresponding sides PT, TO, OP of triangle PTO (1.20). Thus triangles PTO and PCO have their three sides respectively equal, and angle PCO equals angle PTO (1.8). We use 1.8 because the comparison has supplied the three side equalities directly. Consequently angle PCO is right (Step 4).

**Step 6.** Produce CO through O to meet the circumference again at D (P2). Then CD is a diameter (D1.17), and PC makes a right angle with it at its extremity C. By 3.16, the straight line PC falls outside the circle. It therefore meets the circle at C without cutting it, even when produced, and hence touches the circle by D3.2. This proves the proposition.

**USED:** 1.20, 1.8, 2.4, 3.1, 3.16, 3.17, 3.18, 3.36, CN1, CN4, CN5, D1.15, D1.17, D3.2, P1, P2
**Human refs (from References field):** 1.8, 3.16, 3.18, 3.36
**Jaccard:** 0.250 — AI adds ['1.20', '2.4', '3.1', '3.17', 'CN1', 'CN4', 'CN5', 'D1.15', 'D1.17', 'D3.2', 'P1', 'P2']
