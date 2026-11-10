# Book 13 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 13.1
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half.

**Step 1.** Let AB be cut at C in extreme and mean ratio, with AC the greater segment. Put w = AB, g = AC, and l = CB. Bisect AB at D, and put h = AD = DB [1.10]. Thus w = g + l = h + h, and w:g = g:l [D6.3]. Write S(u) for the area of the square on u, and R(u,v) for the area of the rectangle with adjacent sides u and v; thus R(u,v) = R(v,u) and R(u,u) = S(u) [D2.1, D1.22].

**Step 2.** Since w, g, l are continuously proportional, the rectangle contained by the extremes equals the square on the mean:
S(g) = R(w,l) [6.17].
Path choice: 6.17 applies directly to the three proportional lengths, without reformulating them as a four-term proportion.

**Step 3.** Applying the rectangle-distribution theorem to w = g + l gives
S(w) = R(w,g) + R(w,l) [2.1].
Applying it to w = h + h gives
R(w,g) = 2R(g,h) [2.1].
Substituting these equalities and Step 2 therefore gives
S(w) = 2R(g,h) + S(g) [CN1, CN2].

**Step 4.** The square on the sum of g and h satisfies
S(g + h) = S(g) + S(h) + 2R(g,h) [2.4].
By Step 3, the first and third areas together equal S(w). Hence
S(g + h) = S(w) + S(h) [CN1, CN2].

**Step 5.** Applying the same square-of-a-sum theorem to w = h + h yields
S(w) = S(h) + S(h) + 2R(h,h) = 4S(h) [2.4, D1.22, D2.1, CN2].
Substitution into Step 4 gives
S(g + h) = 4S(h) + S(h) = 5S(h) [CN1, CN2].
Therefore the square on the greater segment added to half the whole is five times the square on that half, as required.

**USED:** 1.10, 2.1, 2.4, 6.17, CN1, CN2, D1.22, D2.1, D6.3
**Human refs (from References field):** 6.1, 6.17, D6.3
**Jaccard:** 0.200 — AI adds ['1.10', '2.1', '2.4', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['6.1']

## Proposition 13.2
**Statement:** If the square on a straight line be five times the square on a segment of it, then, when the double of the said segment is cut in extreme and mean ratio, the greater segment is the remaining part of the original straight line.

**Step 1.** Let AB be the original straight line, and let C lie between A and B, with the square on AB equal to five times the square on AC. Produce CA beyond A to D, taking AD equal to AC [P2, 1.3]. Then CD is double AC, and AC is its half.

**Step 2.** Cut CD in extreme and mean ratio at E, with CE the greater segment [6.30]. We apply 13.1 directly because its fivefold-square conclusion matches the hypothesis. Since AC is half of CD, the square on the length CE + AC is five times the square on AC [13.1].

**Step 3.** By hypothesis, the square on AB is also five times the square on AC. Therefore the square on CE + AC equals the square on AB [CN1].

**Step 4.** Consequently CE + AC equals AB. Indeed, if these lengths were unequal, cut off from the longer a length equal to the shorter [1.3]. By 2.4, the square on the longer would equal the square on the shorter together with the square on the positive remainder and twice the rectangle contained by the shorter and the remainder. Thus the square on the longer would be greater than the square on the shorter [CN5], contradicting Step 3.

**Step 5.** Since AB equals AC + CB, the equality CE + AC = AB gives CE + AC = CB + AC. Subtracting AC yields CE = CB [CN3]. Therefore, when the double of the specified segment AC is cut in extreme and mean ratio, its greater segment equals CB, the remaining part of the original straight line. This proves the proposition.

**USED:** 1.3, 13.1, 2.4, 6.30, CN1, CN3, CN5, P2
**Human refs (from References field):** 6.1
**Jaccard:** 0.000 — AI adds ['1.3', '13.1', '2.4', '6.30', 'CN1', 'CN3', 'CN5', 'P2']; Human adds ['6.1']

## Proposition 13.3
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the lesser segment added to the half of the greater segment is five times the square on the half of the greater segment.

**Step 1.** Let AB be cut in extreme and mean ratio at C, with AC the greater segment and CB the lesser. Then AB : AC = AC : CB. [D6.3]

**Step 2.** The rectangle contained by AB and CB therefore equals the square on AC. We use the three-term proportion theorem directly, since AC is the mean proportional between AB and CB. [6.17]

**Step 3.** Bisect AC at D, so that AD = DC. The points lie in the order A, D, C, B; hence DB consists of the lesser segment CB together with DC, half the greater segment. [1.10]

**Step 4.** Apply the bisected-and-extended-line identity to AC, bisected at D and extended by CB. It gives: the rectangle contained by AB and CB, together with the square on DC, equals the square on DB. This is the direct path because the bisection and extension are already present. [2.6]

**Step 5.** Applied to AC cut at D, the square-of-a-sum identity says that the square on AC equals the squares on AD and DC together with twice the rectangle contained by AD and DC. Since AD = DC, this is four times the square on DC. [2.4]

**Step 6.** Add the square on DC to the equal areas in Step 2 and use Steps 4 and 5. Thus the square on DB equals the square on AC together with the square on DC, and therefore equals five times the square on DC. Since DB is the lesser segment added to half the greater, the required conclusion follows. [CN2, CN1]

**USED:** 1.10, 2.4, 2.6, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.10', '2.4', '2.6', '6.17', 'CN1', 'CN2', 'D6.3']

## Proposition 13.4
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.

**Step 1.** Let AB be cut at C in extreme and mean ratio, with AC the greater segment and CB the lesser. By the definition of extreme and mean ratio,
AB : AC = AC : CB. [D6.3]

**Step 2.** Since AB, AC, CB are three proportional straight lines, the rectangle contained by AB and CB equals the square on AC. [6.17] This theorem applies directly to the three-term proportion, without requiring a four-term reformulation.

**Step 3.** Apply Proposition 2.7 to AB cut at C, taking CB as the designated segment. The squares on AB and CB together equal twice the rectangle contained by AB and CB together with the square on AC. [2.7] This identity is chosen because its left-hand side is exactly the sum required in the conclusion.

**Step 4.** By Step 2, each of the two rectangles in Step 3 equals the square on AC. Adding these equalities and then adding the square on AC shows that twice that rectangle together with the square on AC equals three times the square on AC. [CN2] Consequently, by Step 3, the square on AB and the square on CB together are triple of the square on AC: the squares on the whole and the lesser segment together are triple of the square on the greater segment. [CN1]

**USED:** 2.7, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 6.17, D6.3
**Jaccard:** 0.400 — AI adds ['2.7', 'CN1', 'CN2']

## Proposition 13.5
**Statement:** If a straight line be cut in extreme and mean ratio, and there be added to it a straight line equal to the greater segment, the whole straight line has been cut in extreme and mean ratio, and the original straight line is the greater segment.

**Step 1.** Let AB be cut in extreme and mean ratio at C, with AC the greater segment. Let BD be the given addition beyond B, equal to AC, so that AD is the enlarged straight line. By the definition of extreme and mean ratio,
AB : AC = AC : CB. [D6.3]

**Step 2.** Apply the theorem on sums of antecedents and consequents to this proportion:
(AB + AC) : (AC + CB) = AB : AC. [5.12]
This is the direct ratio route: the two sums give precisely the enlarged line and the original line, without introducing squares or auxiliary constructions.

**Step 3.** Since AC = BD, adding AB to both gives AB + AC = AB + BD = AD. [CN2] Also, AC + CB = AB, because C lies between A and B. Substituting these equal magnitudes, and BD for AC, in the proportion of Step 2 gives
AD : AB = AB : BD. Such substitution preserves the ratio by its defining comparison of equimultiples. [D5.5]

**Step 4.** The original line AB is greater than its part AC, and therefore greater than BD, which equals AC. [CN5] Thus AD is divided at B into the greater segment AB and the lesser segment BD, with the whole to the greater as the greater to the lesser. By definition, AD has been cut in extreme and mean ratio, and the original straight line AB is its greater segment. [D6.3]

**USED:** 5.12, CN2, CN5, D5.5, D6.3
**Human refs (from References field):** 5.14, 6.17, D6.3
**Jaccard:** 0.143 — AI adds ['5.12', 'CN2', 'CN5', 'D5.5']; Human adds ['5.14', '6.17']

## Proposition 13.6
**Statement:** If a rational straight line be cut in extreme and mean ratio, each of the segments is the irrational straight line called apotome.

**Step 1.** Let the rational straight line AB be cut in extreme and mean ratio at C, with AC the greater segment. Bisect AB at M [1.10], and produce BA beyond A to D so that AD = AM [P2, 1.3]. The points are in the order D, A, C, B. Write h = AD, t = DC, and u = DB. Thus AB = 2h, u = 3h, AC = t − h, and CB = u − t [CN2, CN3]. Throughout, x² denotes the square on the straight line x.

**Step 2.** The straight line h measures AB twice and u three times. Consequently h, AB, and u are commensurable in length [D10.1.1], and their squares are commensurable [10.9]. Since AB is rational, h and u are also rational: their squares are commensurable with the square on the assigned rational straight line, by transitivity of commensurability [10.12, D10.1.3].

**Step 3.** Choose 13.1, the first preceding square identity, because it applies directly to the greater segment together with the rational half of the whole. Since t = AC + h and h is half of AB, it gives t² = 5h² [13.1]. Therefore t and h are commensurable in square [D10.1.2]. Since h is rational, t is rational as well [10.12, D10.1.3].

**Step 4.** The ratio 5:1 cannot be a ratio of square numbers. Indeed, suppose it were, and take the least numbers m, n in the ratio of the sides of those squares. The original sides are equimultiples of m, n [7.20], so m² = 5n²; moreover, m and n are prime to one another [7.22]. Since 5 is prime and measures m², it measures m [7.30]. Writing m = 5k gives n² = 5k², so 5 also measures n [7.30], a contradiction. Thus t²:h² = 5:1 is not a ratio of square numbers, and t and h are incommensurable in length [10.9].

**Step 5.** Since DC contains DA as a proper part, t > h [CN5]. Hence AC = t − h is obtained by subtracting from the rational straight line t the rational straight line h, commensurable with it in square only. By 10.73, AC is irrational and is an apotome.

**Step 6.** The straight lines u and h are commensurable in length, since u = 3h [D10.1.1]. If u and t were commensurable in length, then h and t would also be commensurable in length [10.12], contrary to Step 4. Thus u and t are incommensurable in length. But u² is commensurable with h² [10.9], and t² is commensurable with h² by Step 3; therefore u² and t² are commensurable [10.12]. The rational straight lines u and t are consequently commensurable in square only.

**Step 7.** Since DB contains DC as a proper part, u > t [CN5]. Thus CB = u − t is likewise obtained by subtracting from one rational straight line another rational straight line commensurable with it in square only. By 10.73, CB is irrational and is an apotome. Therefore each segment of the given rational straight line is the irrational straight line called apotome.

**USED:** 1.10, 1.3, 10.12, 10.73, 10.9, 13.1, 7.20, 7.22, 7.30, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, P2
**Human refs (from References field):** 10.6, 10.73, 10.9, 10.97, 13.1, 6.17, D10.1.4, D6.3
**Jaccard:** 0.143 — AI adds ['1.10', '1.3', '10.12', '7.20', '7.22', '7.30', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'P2']; Human adds ['10.6', '10.97', '6.17', 'D10.1.4', 'D6.3']

## Proposition 13.7
**Statement:** If three angles of an equilateral pentagon, taken either in order or not in order, be equal, the pentagon will be equiangular.

**Step 1.** Let ABCDE be the equilateral pentagon, with vertices named in boundary order; write A, B, C, D, E also for its interior angles. Up to relabelling, the three equal angles are either B, C, D (consecutive) or A, B, D (nonconsecutive). In both cases B = D. Join AC and CE. [Hypothesis; P1]

**Step 2.** In triangles ABC and EDC, AB = ED and BC = DC because the pentagon is equilateral, while ∠ABC = ∠EDC because B = D. Therefore AC = EC and ∠BAC = ∠DEC. We use SAS here because the given equal angles are precisely those included between the equal sides. [1.4]

**Step 3.** Since AC = EC, the base angles of triangle ACE satisfy ∠CAE = ∠CEA. Adding this equality to ∠BAC = ∠DEC gives
∠BAE = ∠DEA.
Thus A = E in both arrangements of the three given equal angles. [1.5; CN2]

**Step 4.** First suppose that the three consecutive angles B, C, D are equal. Join BD and AD. In triangles ABC and BCD, AB = BC, BC = CD, and ∠ABC = ∠BCD. Hence AC = BD. [P1; 1.4]

**Step 5.** Compare triangles BAD and CDA. We have BA = CD, BD = CA by Step 4, and AD is common. Thus ∠BAD = ∠CDA by SSS, which is now the direct choice because all three corresponding sides are equal. Also, AE = DE, so triangle ADE has ∠DAE = ∠ADE. [1.8; 1.5]

**Step 6.** Adding the two angle equalities in Step 5 gives
∠BAE = ∠CDE,
so A = D. Step 3 gives E = A, while B = C = D by hypothesis. Therefore all five angles are equal in the consecutive case. [CN2; CN1]

**Step 7.** Now suppose that the given equal angles are the nonconsecutive angles A, B, D. By Step 3, E = A; hence E, A, B are three equal consecutive angles. The consecutive case established in Steps 2–6 applies after cyclic relabelling, and therefore all five angles are again equal. Thus, in either arrangement, the equilateral pentagon is equiangular. [CN1; Steps 2–6]

**USED:** 1.4, 1.5, 1.8, CN1, CN2, P1
**Human refs (from References field):** 1.4, 1.5, 1.6, 1.8
**Jaccard:** 0.429 — AI adds ['CN1', 'CN2', 'P1']; Human adds ['1.6']

## Proposition 13.8
**Statement:** If in an equilateral and equiangular pentagon straight lines subtend two angles taken in order, they cut one another in extreme and mean ratio, and their greater segments are equal to the side of the pentagon.

**Step 1.** Let ABCDE be the equilateral and equiangular pentagon, with its vertices in order. Draw AC and BD, subtending the consecutive angles ABC and BCD, and let their interior intersection be F. Also draw AD. [P1]

**Step 2.** Write R for a right angle and put θ = 2R/5. The triangles ABC, ACD, and ADE together contain all the interior angles of the pentagon. Their angle sums therefore give six right angles in all. Since the five angles of the pentagon are equal, each equals 6R/5 = 3θ; the angle sum of any triangle is 2R = 5θ. [1.32, CN2]

**Step 3.** Since AB = BC, the base angles BAC and BCA are equal. Their sum is 5θ − 3θ = 2θ, so each equals θ. Similarly, since BC = CD, the angles CBD and BDC each equal θ. [1.5, 1.32, CN3]

**Step 4.** In triangle ABF, the angle BAF equals BAC, hence equals θ. Moreover, angle ABF is the remainder after angle CBD is subtracted from angle ABC, so it equals 3θ − θ = 2θ. Consequently angle AFB also equals 2θ. The equal angles ABF and AFB give AF = AB, and therefore AF = BC. [CN3, 1.32, 1.6, CN1]

**Step 5.** In triangle BCF, angle CBF equals CBD and angle BCF equals BCA, so both equal θ. Thus BF = CF, while angle BFC equals 3θ. Since angle BFC is greater than angle CBF, its opposite side BC is greater than CF. Together with Step 4, this gives AF > CF. [1.6, 1.32, 1.19]

**Step 6.** The triangles ABC and BCD have AB = BC, BC = CD, and the included angles ABC and BCD equal. Hence AC = BD. Subtracting the equal segments CF and BF from these equal diagonals gives AF = DF. Therefore DF = BC, and, by Step 5, DF > BF. [1.4, CN3, CN1]

**Step 7.** The triangles ABC and BFC are equiangular: their corresponding angles, in the displayed order, are θ, 3θ, θ. We choose the equiangular-triangle proportionality theorem directly, since these angle equalities are already established. It gives AC : BC = BC : FC. Substituting AF = BC from Step 4 yields AC : AF = AF : FC. [6.4, D5.5]

**Step 8.** By Steps 5 and 6, BD = AC, DF = AF, and FB = FC. Substitution in the preceding proportion therefore gives BD : DF = DF : FB. Since AF > FC and DF > FB, these two proportions say precisely that AC and BD are each cut at F in extreme and mean ratio. Their greater segments are AF and DF, both equal to the side BC of the pentagon. Thus the proposition is proved. [D5.5, D6.3]

**USED:** 1.19, 1.32, 1.4, 1.5, 1.6, 6.4, CN1, CN2, CN3, D5.5, D6.3, P1
**Human refs (from References field):** 1.32, 1.4, 1.5, 1.6, 3.28, 4.14, 5.14, 6.33, 6.4
**Jaccard:** 0.312 — AI adds ['1.19', 'CN1', 'CN2', 'CN3', 'D5.5', 'D6.3', 'P1']; Human adds ['3.28', '4.14', '5.14', '6.33']

## Proposition 13.9
**Statement:** If the side of the hexagon and that of the decagon inscribed in the same circle be added together, the whole straight line has been cut in extreme and mean ratio, and its greater segment is the side of the hexagon.

**Step 1.** Let O be the centre of the given circle, and let AB be a side of its inscribed regular decagon. Join OA and OB (P1). The radii OA and OB are equal (D1.15), and each equals the side of the inscribed regular hexagon, by the radius–side equality in 4.15. We shall identify AB as the greater segment of a radius cut in extreme and mean ratio; 13.5 will then give the required addition directly.

**Step 2.** Join O to the remaining vertices of the decagon (P1). The ten triangles so formed have equal radii and equal bases, so their angles at O are equal (D1.15, 1.8). Put θ = ∠AOB. Since the angles about O total four right angles (1.13), five angles θ equal two right angles. Also, OA = OB, so ∠OAB = ∠ABO (1.5). The angle sum of triangle OAB therefore gives ∠OAB = ∠ABO = 2θ (1.32).

**Step 3.** Bisect ∠OAB by AD, meeting OB at D (1.9). Thus ∠OAD = ∠DAB = θ. In triangle OAD, ∠AOD = ∠OAD = θ, whence OD = AD (1.6). In triangle ADB, the angles at A and B are θ and 2θ; its remaining angle ∠ADB is consequently 2θ (1.32). Hence AD = AB (1.6), and therefore OD = AD = AB (CN1).

**Step 4.** In triangle ADB, ∠ABD = 2θ is greater than ∠BAD = θ (CN5). The side opposite the greater angle is greater, so AD > DB (1.19). Since OD = AD, it follows that OD > DB: OD is the greater segment of OB.

**Step 5.** Because AD bisects ∠OAB, the angle-bisector theorem gives OA : AB = OD : DB (6.3). This theorem is the direct choice here because the constructed bisector supplies precisely the required proportion. Substituting OA = OB and AB = OD gives OB : OD = OD : DB. Together with OD > DB, this says that OB is cut at D in extreme and mean ratio, with greater segment OD equal to the decagon side AB (D6.3).

**Step 6.** Produce OB beyond B to C, taking BC = BA by intersecting the produced line with the circle of centre B and distance BA (P2, P3, D1.15). Thus BC = OD (CN1). Since OB is cut in extreme and mean ratio and a line equal to its greater segment has been added to it, 13.5 shows that OC is cut at B in extreme and mean ratio, with OB its greater segment. In particular, OC : OB = OB : BC (D6.3). But OB is the hexagon side and BC is the decagon side, so OC is their sum. Therefore their sum is cut in extreme and mean ratio, and its greater segment is the side of the hexagon, as required.

**USED:** 1.13, 1.19, 1.32, 1.5, 1.6, 1.8, 1.9, 13.5, 4.15, 6.3, CN1, CN5, D1.15, D6.3, P1, P2, P3
**Human refs (from References field):** 1.32, 1.5, 4.15, 6.33, 6.4
**Jaccard:** 0.158 — AI adds ['1.13', '1.19', '1.6', '1.8', '1.9', '13.5', '6.3', 'CN1', 'CN5', 'D1.15', 'D6.3', 'P1', 'P2', 'P3']; Human adds ['6.33', '6.4']

## Proposition 13.10
**Statement:** If an equilateral pentagon be inscribed in a circle, the square on the side of the pentagon is equal to the squares on the side of the hexagon and on that of the decagon inscribed in the same circle.

**Step 1.** Let ABCDE be the given equilateral pentagon, with its vertices in cyclic order. Find the centre O, join the required points, and produce AO through O to meet the circle again at F [3.1, P1, P2]. Thus AF is a diameter [D1.17]. Put AB = p and OA = r. All the radii equal r [D1.15], and r is the side of the inscribed regular hexagon [4.15]. Our route is to determine BF and then apply the theorem on the square of the hypotenuse to triangle ABF.

**Step 2.** The equal sides of the pentagon subtend equal minor arcs [3.28]. The five successive arcs must all be minor: a major one would leave its complementary minor arc containing the other four successive arcs, each at least as large as that complementary arc, which is impossible [CN5]. Consequently the five successive arcs are equal, and ∠AOB = 72° [3.27, 1.13]. Bisect each of these arcs [3.30]. The resulting ten equal arcs determine an equilateral and equiangular inscribed decagon [3.29, 3.27]. Let M be the midpoint of arc AB, and put AM = d. Thus d is the decagon side and ∠AOM = 36° [3.27, 1.13].

**Step 3.** Since OA and OF are opposite rays, ∠BOF = 108° [1.13]. Since OB = OF, the base angles ∠OBF and ∠BFO are equal and therefore each is 36° [D1.15, 1.5, 1.32]. The side BF, opposite the greater angle, is greater than BO [1.19].

**Step 4.** Cut off BT = BO on BF, with T between B and F [1.3]. In the isosceles triangle BOT, the angle at B is 36°, so ∠BOT = ∠OTB = 72° [1.5, 1.32]. Hence ∠TOF = 108° − 72° = 36° [CN3]. Also ∠OFT = ∠OFB = 36°. Therefore TF = OT [1.6].

**Step 5.** In triangles BOT and OAM, BO = OA and BT = OM, while their included angles ∠OBT and ∠AOM both equal 36° [D1.15, CN1]. Side–angle–side therefore gives OT = AM = d [1.4]. Together with Step 4 this gives TF = d, and consequently BF = BT + TF = r + d [CN1, CN2].

**Step 6.** Write x² for the square on x, and xy for the rectangle contained by x and y [D2.1]. By the preceding hexagon–decagon proposition, r + d is cut in extreme and mean ratio with greater segment r; hence (r + d) : r = r : d [13.9, D6.3]. The three-term result applies directly to this continuous proportion, giving r² = (r + d)d [6.17]. Expanding this rectangle gives
r² = rd + d² [2.3].

**Step 7.** Since AF is a diameter, ∠ABF is right [3.31]. Also AF = AO + OF = 2r [D1.15, CN2]. Therefore the theorem on the square of the hypotenuse gives
p² + (r + d)² = (2r)² [1.47].
Expanding the squares, we obtain
p² + r² + 2rd + d² = 4r² [2.4].

**Step 8.** Add d² to both sides of the last equality. Twice the equality in Step 6 gives 2rd + 2d² = 2r²; substituting this yields
p² + 3r² = 4r² + d² [CN1, CN2].
Subtracting 3r² gives
p² = r² + d² [CN3].
Thus the square on the pentagon side equals the squares on the hexagon side and the decagon side inscribed in the same circle, as required.

**USED:** 1.13, 1.19, 1.3, 1.32, 1.4, 1.47, 1.5, 1.6, 13.9, 2.3, 2.4, 3.1, 3.27, 3.28, 3.29, 3.30, 3.31, 4.15, 6.17, CN1, CN2, CN3, CN5, D1.15, D1.17, D2.1, D6.3, P1, P2
**Human refs (from References field):** 1.26, 1.32, 1.4, 1.5, 2.2, 3.26, 4.15, 6.17, 6.33, 6.4
**Jaccard:** 0.147 — AI adds ['1.13', '1.19', '1.3', '1.47', '1.6', '13.9', '2.3', '2.4', '3.1', '3.27', '3.28', '3.29', '3.30', '3.31', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.17', 'D2.1', 'D6.3', 'P1', 'P2']; Human adds ['1.26', '2.2', '3.26', '6.33', '6.4']

## Proposition 13.11
**Statement:** If in a circle which has its diameter rational an equilateral pentagon be inscribed, the side of the pentagon is the irrational straight line called minor.

**Step 1.** Let d be the rational diameter of the circle, and p the side of the given equilateral pentagon. Let h and t be the sides of the equilateral hexagon and decagon inscribed in the same circle. The hexagon side equals the radius, so h = d/2 (4.15). Put u = h/2, so d = 4u. Throughout, x² denotes the square on x, and xy the rectangle contained by x and y.

**Step 2.** By 13.9, h + t is cut in extreme and mean ratio, with greater segment h and lesser segment t. Thus (h + t):h = h:t (D6.3), and consequently
h² = (h + t)t = ht + t²
by 6.17 and 2.3. In particular, h > t.

**Step 3.** By 13.10, p² = h² + t². Combining this with Step 2 gives
p² = 2h² − ht = h(2h − t)
(CN2, CN3, 2.1). The breadth 2h − t is positive because h > t. Our path is to identify this breadth as a fourth apotome, so that the side of this rectangle can be classified directly by 10.94.

**Step 4.** Set b = t + u and a = 5u. Since u is half the greater segment h in the division of Step 2, the directly applicable identity is 13.3, which gives
b² = (t + u)² = 5u².
Moreover,
a − b = 5u − (t + u) = 4u − t = 2h − t.
Write e = a − b. Thus e > 0 and p² = he.

**Step 5.** Since d = 4u, h = 2u, and a = 5u, distributivity of rectangles gives
d² = 16u²,  h² = 4u²,  a² = 25u²,
while b² = 5u² (2.1; Step 4). Hence h, a, and b are rational: their squares are commensurable with the square on the given rational diameter (D10.1.2, D10.1.3). Also, a and h are commensurable in length, since u measures both (D10.1.1).

**Step 6.** The squares on a and b have ratio 25:5, that is, 5:1. This is not a ratio of square numbers. Indeed, if it were, its square roots could be represented by relatively prime integers m and n (7.33, 7.22), with m² = 5n². Since 5 is prime, 7.30 would give 5 dividing m. Writing m = 5k then gives n² = 5k², so 7.30 also gives 5 dividing n, a contradiction. Therefore a and b are incommensurable in length by 10.9. Their squares are nevertheless commensurable by Step 5, so they are commensurable in square only.

**Step 7.** Thus e = a − b is obtained by subtracting from a rational straight line another rational straight line commensurable with it in square only. Accordingly, e is an apotome (10.73).

**Step 8.** The excess of the square on its whole a over the square on its annex b is
a² − b² = 25u² − 5u² = 20u² = 4b² = (2b)²
(2.1, CN3). The line 2b is commensurable in length with b (D10.1.1), and therefore is incommensurable in length with a, by Step 6 and 10.13. Since a is commensurable in length with the rational line h, the apotome e is a fourth apotome relative to h (D10.3.4).

**Step 9.** By Steps 3–4, the square on the pentagon side p equals the rectangle contained by the rational straight line h and the fourth apotome e. By 10.94, the side of such an area is the irrational straight line called minor. Therefore the side of the inscribed equilateral pentagon is minor, as required.

**USED:** 10.13, 10.73, 10.9, 10.94, 13.10, 13.3, 13.9, 2.1, 2.3, 4.15, 6.17, 7.22, 7.30, 7.33, CN2, CN3, D10.1.1, D10.1.2, D10.1.3, D10.3.4, D6.3
**Human refs (from References field):** 1.32, 10.12, 10.15, 10.73, 10.9, 10.94, 13.1, 13.8, 5.18, 5.19, D10.3.4
**Jaccard:** 0.143 — AI adds ['10.13', '13.10', '13.3', '13.9', '2.1', '2.3', '4.15', '6.17', '7.22', '7.30', '7.33', 'CN2', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D6.3']; Human adds ['1.32', '10.12', '10.15', '13.1', '13.8', '5.18', '5.19']

## Proposition 13.12
**Statement:** If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.

**Step 1.** Let ABC be the inscribed equilateral triangle, so AB = BC = CA and A, B, C lie on the circumference [D1.20, D4.3]. Find the centre O [3.1]. The three angles of ABC are equal [1.5]; denote each by θ. Their sum is two right angles, so 3θ equals two right angles and θ is acute [1.32]. Write x² for the area of the square on a segment of length x.

**Step 2.** Draw AO and produce it through O to meet the circumference again at D; join OB and BD [P1, P2]. Thus AD is a diameter [D1.17]. Put r = AO. Since radii of the same circle are equal, AO = OB = OD = r [D1.15]. Moreover, D is not B: otherwise AB would be a diameter and ∠ACB would be right, contrary to Step 1 [3.31].

**Step 3.** The angle at the centre standing on the arc AB not containing C is twice ∠ACB, and therefore equals 2θ [3.20]. Since 2θ is less than two right angles, this is the ordinary angle AOB. Because OA and OD are opposite rays, ∠AOB and ∠BOD together equal two right angles [1.13]. Subtracting 2θ from 3θ gives ∠BOD = θ [CN3].

**Step 4.** In triangle OBD, OB = OD, so ∠OBD = ∠BDO [1.5]. Since ∠BOD = θ and the three angles sum to 3θ, the two equal remaining angles are each θ [1.32, CN3]. Consequently ∠BOD = ∠OBD, and their opposite sides are equal: BD = OD = r [1.6].

**Step 5.** Since AD is a diameter, ∠ABD is right [3.31]. Path choice: the diameter has supplied a right triangle, so apply the square-on-the-hypotenuse theorem directly rather than introduce proportions. It gives AB² + BD² = AD² [1.47].

**Step 6.** Apply the square-of-a-divided-line theorem to AD divided at O. The square on AD equals the squares on AO and OD together with twice the rectangle contained by AO and OD [2.4]. Since AO = OD = r, that rectangle is a square on r, and the squares on these equal segments are equal [D2.1, D1.22, CN4]. Hence AD² = r² + r² + 2r² = 4r² [CN2].

**Step 7.** Since BD = r, its square equals r² [CN4]. Substituting in the equality from Step 5 gives AB² + r² = 4r². Subtracting r² yields AB² = 3r² [CN3]. Therefore the square on the side of the inscribed equilateral triangle is triple the square on the radius of the circle.

**USED:** 1.13, 1.32, 1.47, 1.5, 1.6, 2.4, 3.1, 3.20, 3.31, CN2, CN3, CN4, D1.15, D1.17, D1.20, D1.22, D2.1, D4.3, P1, P2
**Human refs (from References field):** 1.47, 3.31, 4.15
**Jaccard:** 0.095 — AI adds ['1.13', '1.32', '1.5', '1.6', '2.4', '3.1', '3.20', 'CN2', 'CN3', 'CN4', 'D1.15', 'D1.17', 'D1.20', 'D1.22', 'D2.1', 'D4.3', 'P1', 'P2']; Human adds ['4.15']

## Proposition 13.13
**Statement:** To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.

**Step 1.** Choose a generating semicircle of the given sphere, with diameter AB and plane Π. Thus AB is also a diameter of the sphere [D11.14, D11.16, D11.17]. Trisect AB, and take the division point C for which AC = 2CB [6.9]. Write CB = t, so AC = 2t and AB = 3t. Our construction will use an equilateral triangle in a circular section perpendicular to AB; the directly applicable side–radius relation is 13.12.

**Step 2.** In Π erect CD perpendicular to AB, meeting the generating semicircle at D, and join AD and BD [1.11, P1]. The angle ADB is right, since it stands in a semicircle [3.31]. The perpendicular DC to the hypotenuse therefore gives AC : CD = CD : CB [6.8]. Consequently,
CD² = AC·CB = 2t²
[6.17, 2.1]. Here XY² denotes the square on XY, and XY·ZW the rectangle contained by those segments.

**Step 3.** At C erect a straight line ℓ perpendicular to Π [11.12], and let Σ be the plane containing the intersecting lines ℓ and CD [11.2]. Since AB lies in Π, it is perpendicular to ℓ; it is also perpendicular to CD [D11.3; Step 2]. Hence AB is perpendicular to Σ [11.4]. In Σ describe the circle Γ with centre C and radius CD [P3].

**Step 4.** The whole circumference of Γ lies on the given sphere. Indeed, when the generating semicircle revolves about AB, CD retains its length and remains perpendicular to AB. Every position of CD lies in Σ: AB is perpendicular to ℓ, to the original CD, and to that position, so these three lines are coplanar [11.5]. During the complete revolution, D therefore traces precisely the circle with centre C and radius CD, namely Γ [D1.15]. This trace belongs to the surface of the given sphere, and the fixed endpoint A also belongs to that surface [D11.14].

**Step 5.** Construct an equilateral triangle [1.1]; its angles are equal [1.5]. Using it as the given triangle in 4.2, inscribe an equiangular triangle DEF in Γ, taking D as one vertex [4.2]. Its equal angles imply equal opposite sides, so DEF is equilateral [1.6].

**Step 6.** Apply 13.12 to the equilateral triangle DEF and its circumcircle Γ. Each base edge consequently satisfies
DE² = EF² = FD² = 3CD² = 6t²
[13.12; Step 2; CN1]. This uses the preceding side–radius theorem directly, rather than deriving that relation afresh.

**Step 7.** Join A to E and F, and C to E and F [P1]. For each X among D, E, and F, the angle ACX is right because AB is perpendicular to Σ [D11.3]. Also CX = CD, since these are radii of Γ [D1.15]. Thus the theorem on the square opposite a right angle gives
AX² = AC² + CX² = (2t)² + 2t² = 6t²
[1.47, 2.4, CN2]. Therefore AD² = AE² = AF² = 6t².

**Step 8.** By Steps 6 and 7, the squares on all six edges AD, AE, AF, DE, EF, and FD are equal [CN1]. The edges themselves are therefore equal: if one were greater than another, 2.4 would express its square as the smaller square together with additional positive areas, contradicting equality [2.4, CN5]. Hence the four triangular faces are equilateral [D1.20]. Since A is outside Σ, these faces bound the pyramid ADEF, constructed from the base DEF to the point A [D11.12]. All four vertices lie on the given sphere by Step 4, so the pyramid is comprehended in that sphere [D11.14].

**Step 9.** Let s be the common edge of the pyramid. We have s² = 6t², whereas AB = 3t gives AB² = 9t² [Steps 1, 6; 2.1, 2.4]. Consequently,
AB² = 9t² = 6t² + 3t² = s² + ½s²
[CN1, CN2]. Thus the square on the diameter of the given sphere is one and a half times the square on the side of the constructed pyramid, as required.

**USED:** 1.1, 1.11, 1.47, 1.5, 1.6, 11.12, 11.2, 11.4, 11.5, 13.12, 2.1, 2.4, 3.31, 4.2, 6.17, 6.8, 6.9, CN1, CN2, CN5, D1.15, D1.20, D11.12, D11.14, D11.16, D11.17, D11.3, P1, P3
**Human refs (from References field):** 1.4, 11.12, 13.12, 3.1, 3.31, 4.2, 6.17, 6.8, D11.3
**Jaccard:** 0.226 — AI adds ['1.1', '1.11', '1.47', '1.5', '1.6', '11.2', '11.4', '11.5', '2.1', '2.4', '6.9', 'CN1', 'CN2', 'CN5', 'D1.15', 'D1.20', 'D11.12', 'D11.14', 'D11.16', 'D11.17', 'P1', 'P3']; Human adds ['1.4', '3.1']

## Proposition 13.14
**Statement:** To construct an octahedron and comprehend it in a sphere, as in the preceding case; and to prove that the square on the diameter of the sphere is double of the square on the side of the octahedron.

**Step 1.** Choose the construction consisting of an equatorial square and two opposite poles. Let AC be the prescribed diameter of the sphere. Bisect AC at O (1.10), and in a plane Π describe the circle with centre O and radius OA (P3). Draw through O the perpendicular to AC, producing it to meet the circle at B and D on opposite sides of AC (1.11, P2). Thus AC and BD are perpendicular diameters, and OA = OB = OC = OD (D1.15, D1.17). Join AB, BC, CD, and DA (P1).

**Step 2.** The two angles on one side of AC at O are right by construction, and their vertically opposite angles are right by 1.15. Consequently the triangles AOB, BOC, COD, and DOA have corresponding equal sides enclosing equal right angles (P4). Side–angle–side is the natural first comparison because these equalities are supplied directly by the construction; applying 1.4 gives AB = BC = CD = DA. Moreover, each angle of ABCD stands in a semicircle and is therefore right (3.31). Hence ABCD is a square (D1.22).

**Step 3.** Set up at O a straight line perpendicular to Π, and produce it in both directions (11.12, P2). This line and AC lie in one plane (11.2). In that plane describe a second circle with centre O and radius OA, meeting the perpendicular at E and F on opposite sides of Π (P3). Then OE = OF = OA, and this circle also passes through A (D1.15). Since E, O, and F are collinear, EF is its diameter (D1.17).

**Step 4.** Join each of E and F to each of A, B, C, and D (P1). For any vertex X of the square, the angles EOX and FOX are right, since EF is perpendicular to Π (D11.3). The triangles EOX and FOX therefore each have two sides equal respectively to OA and OB, enclosing an angle equal to AOB (P4). Applying 1.4 gives EX = AB and FX = AB. Thus all eight segments from the poles to the square's vertices equal the four sides of the square (CN1).

**Step 5.** Form the pyramids with common base ABCD and respective vertices E and F (D11.12). They lie on opposite sides of Π, so their common base is internal to their union, whose boundary consists of exactly the eight triangles EAB, EBC, ECD, EDA, FAB, FBC, FCD, and FDA. Every side of every one of these triangles equals AB, so they are equilateral (D1.20). Their corresponding angles are equal by 1.8, and the triangles themselves are equal by 1.4. Their union is therefore a solid contained by eight equal equilateral triangles: an octahedron (D11.26).

**Step 6.** Take the semicircle of the second circle with diameter EF and passing through A (D1.18). Revolve it about EF; the solid so comprehended is a sphere (D11.14). Since OA is perpendicular to EF, during this revolution A describes the circle in Π with centre O and radius OA, namely the original circle through A, B, C, and D (D11.3, D1.15). Hence all four square vertices lie on the sphere's surface. The fixed endpoints E and F also lie on its surface. Thus the constructed octahedron is comprehended in this sphere, with all six vertices on its surface.

**Step 7.** The sphere has centre O, the centre of the generating semicircle (D11.16), and EF is a diameter of it (D11.17). Since OE = OA and OF = OC, adding equals gives EF = OE + OF = OA + OC = AC (CN1, CN2). The sphere therefore has the prescribed diameter.

**Step 8.** The angle ABC is right and AB = BC, because ABCD is a square. Therefore the square on AC equals the squares on AB and BC together (1.47), and hence equals twice the square on AB (CN2). Since EF = AC, the square on the sphere's diameter EF is likewise twice the square on AB (CN1). But AB is a side of the constructed octahedron. The required octahedron has therefore been constructed and comprehended in the sphere, and the square on the sphere's diameter is double the square on its side.

**USED:** 1.10, 1.11, 1.15, 1.4, 1.47, 1.8, 11.12, 11.2, 3.31, CN1, CN2, D1.15, D1.17, D1.18, D1.20, D1.22, D11.12, D11.14, D11.16, D11.17, D11.26, D11.3, P1, P2, P3, P4
**Human refs (from References field):** 1.4, 1.47, 11.12, 3.31
**Jaccard:** 0.154 — AI adds ['1.10', '1.11', '1.15', '1.8', '11.2', 'CN1', 'CN2', 'D1.15', 'D1.17', 'D1.18', 'D1.20', 'D1.22', 'D11.12', 'D11.14', 'D11.16', 'D11.17', 'D11.26', 'D11.3', 'P1', 'P2', 'P3', 'P4']

## Proposition 13.15
**Statement:** To construct a cube and comprehend it in a sphere, like the pyramid; and to prove that the square on the diameter of the sphere is triple of the square on the side of the cube.

**Step 1.** Let d be the prescribed diameter of the sphere, and write x² for the square on a length x. We choose the square-base construction: a face diagonal and then a solid diagonal give two successive applications of 1.47, without requiring another regular-solid construction. Cut off a third t of d (6.9), and construct a mean proportional a between d and t (6.13). Then a² equals the rectangle contained by d and t (6.17). Since d consists of three lengths equal to t, the square on d consists of three such rectangles (2.1). Consequently,

d² = 3a².

**Step 2.** Construct a square ABCD with side a (1.46). Its opposite sides are parallel, because the interior angles on the same side of each transversal together equal two right angles (1.28). At A, B, C, and D erect perpendiculars to the plane of the square, all on the same side of that plane (11.12). Produce them as necessary and cut off AA′ = BB′ = CC′ = DD′ = a (P2, 1.3). Join A′B′, B′C′, C′D′, and D′A′, and join the four solid diagonals AC′, BD′, CA′, and DB′ (P1).

**Step 3.** The four erected perpendiculars are parallel to one another (11.6). Since AA′ and BB′ are equal and parallel in the same direction, AB and A′B′ are also equal and parallel (1.33). The same argument applies to each successive pair of erected perpendiculars. Thus ABB′A′, BCC′B′, CDD′C′, and DAA′D′ are parallelograms, each having all four sides equal to a. Their angles at the base are right angles, since the erected lines are perpendicular to the base plane (D11.3); their opposite angles are equal to these (1.34). These four faces are therefore squares (D1.22).

**Step 4.** From the parallelisms already established, A′B′ and D′C′ are parallel to the same base direction and hence parallel to one another (11.9). They therefore lie in one plane, which contains all four upper vertices (D1.23). Each upper side equals a, and the two sides at each upper vertex are respectively parallel to the corresponding sides of ABCD. Their included angles consequently equal the corresponding right angles of ABCD (11.10). Hence A′B′C′D′ is also a square (D1.22). All six faces are equal squares: dividing each by a diagonal gives corresponding triangles with two equal sides and an equal included right angle (P4, 1.4), and adding the equal triangles gives equal squares (CN2). The solid bounded by these six faces is therefore a cube (D11.25).

**Step 5.** Apply 1.47 to the right-angled triangles ABC and BAD. Since every base side equals a,

AC² = BD² = 2a².

Also, CC′ is perpendicular to AC, DD′ to BD, AA′ to CA, and BB′ to DB, because each erected line is perpendicular to the base plane (D11.3). Applying 1.47 to ACC′, BDD′, CAA′, and DBB′ therefore gives

AC′² = BD′² = CA′² = DB′² = 2a² + a² = 3a² = d²

(CN1, CN2, Step 1). Equal squares have equal sides: otherwise the square on the shorter side could be placed strictly within the square on the longer side, contradicting their equality (CN5). Thus all four solid diagonals have length d.

**Step 6.** AB and D′C′ are equal and parallel, as are AD and B′C′, and also AA′ and CC′ (Steps 2–4; 11.9). Each such pair lies in one plane (D1.23), and joining its corresponding endpoints gives a parallelogram (1.33). Consequently ABC′D′, ADC′B′, and ACC′A′ are parallelograms. Their diagonals bisect one another (1.34). Each has AC′ as one diagonal, while its other diagonal is respectively BD′, DB′, or CA′. Therefore all four solid diagonals pass through the same midpoint O of AC′ and are bisected there. Since their lengths are all d, the distances from O to all eight vertices are equal to d/2 (CN1).

**Step 7.** Describe the circle with centre O and radius OA (P3). Since O is the midpoint of AC′, that line is a diameter of the circle (D1.17). Rotate either semicircle on AC′ about AC′ (D1.18). The resulting solid is a sphere with centre O (D11.14, D11.16), and AC′ is a diameter of that sphere (D11.17). Every vertex of the cube lies on its surface: in the half-plane through the axis and that vertex, the rotating semicircle has centre O and radius OA, equal to the distance of the vertex from O (D1.15, D11.14, Step 6). The sphere thus has the prescribed diameter d.

**Step 8.** The cube is contained in this sphere, not merely incident with it at its vertices. Indeed, in a plane through O, the sphere has a circular disk as its section (D11.14). Any segment joining points of that disk lies within it: extend the segment to the circumference and apply 3.2 (P2). Thus every segment between points of the spherical solid stays within it. It follows successively that the cube’s edges, the squares filled by segments between those edges, and the solid filled by segments between opposite squares all lie within the sphere. We have therefore constructed a cube and comprehended it in a sphere of diameter d; and, since its side is a, Step 1 proves that the square on the diameter is triple the square on the side:

d² = 3a².

**USED:** 1.28, 1.3, 1.33, 1.34, 1.4, 1.46, 1.47, 11.10, 11.12, 11.6, 11.9, 2.1, 3.2, 6.13, 6.17, 6.9, CN1, CN2, CN5, D1.15, D1.17, D1.18, D1.22, D1.23, D11.14, D11.16, D11.17, D11.25, D11.3, P1, P2, P3, P4
**Human refs (from References field):** 1.47, D11.3
**Jaccard:** 0.061 — AI adds ['1.28', '1.3', '1.33', '1.34', '1.4', '1.46', '11.10', '11.12', '11.6', '11.9', '2.1', '3.2', '6.13', '6.17', '6.9', 'CN1', 'CN2', 'CN5', 'D1.15', 'D1.17', 'D1.18', 'D1.22', 'D1.23', 'D11.14', 'D11.16', 'D11.17', 'D11.25', 'P1', 'P2', 'P3', 'P4']

## Proposition 13.16
**Statement:** To construct an icosahedron and comprehend it in a sphere, like the aforesaid figures; and to prove that the side of the icosahedron is the irrational straight line called minor.

**Step 1.** Let D be the prescribed diameter of the sphere. We shall use two staggered pentagonal rings, preserving the side of a pentagon as the edge of the solid; this makes the subsequent irrationality classification direct. Cut off e equal to one fifth of D, and construct r as a mean proportional between D and e (6.9, 6.13). Then r² = D·e, and consequently D² = 5r² (6.16, 2.1).

**Step 2.** Describe a circle γ with centre H and radius r, and inscribe in it an equilateral and equiangular pentagon A_0A_1A_2A_3A_4 (P3, 4.11). Its five successive minor arcs are equal (3.28). Bisect each of these arcs at C_i, so that the cyclic order of the ten points is A_0, C_0, A_1, C_1, …, A_4, C_4 (3.30). The ten consecutive chords are equal; denote their common length by d. Denote the pentagon side by s. Equal arcs also give C_iC_{i+1} = A_iA_{i+1} = s (3.29). Throughout, indices are read modulo five.

**Step 3.** The side of the regular hexagon inscribed in γ equals r (4.15). Therefore
s² = r² + d²
by 13.10. Moreover, r + d is cut in extreme and mean ratio with greater segment r and lesser segment d (13.9). Apply 13.3: this is the direct choice because it concerns precisely the lesser segment together with half the greater. It gives
(d + r/2)² = 5(r/2)² = 5r²/4,
where the last equality follows from 2.4.

**Step 4.** Let π be the plane of γ. Erect at H a straight line ℓ perpendicular to π, and take K on it with HK = r (11.12, P2, 1.3). Through K construct two intersecting lines parallel respectively to two intersecting diameters of γ; their plane π′ is parallel to π (1.31, 11.15).

Through each C_i draw the parallel to ℓ, meeting π′ at B_i (1.31). These parallels are perpendicular to π (11.8). In the plane HKC_i, the intersections HC_i and KB_i with the parallel planes π and π′ are parallel (11.16). Thus HC_iB_iK is a rectangle, and
C_iB_i = HK = r,  KB_i = HC_i = r;
also KB_i is perpendicular to ℓ (D11.3, 1.34). Join consecutive B_i. Since C_iB_i and C_{i+1}B_{i+1} are equal and parallel in the same direction, B_iB_{i+1} = C_iC_{i+1} = s (P1, 1.33).

**Step 5.** On ℓ take P beyond H, away from K, with HP = d; take Q beyond K, away from H, with KQ = d (P2, 1.3). Make the joins required for the following four families of triangles, five in each family (P1):
P A_i A_{i+1};
Q B_i B_{i+1};
A_i A_{i+1} B_i;
B_i B_{i+1} A_{i+1}.
These are the proposed twenty faces.

**Step 6.** The triangles PHA_i and QKB_i are right-angled. Hence
PA_i² = HP² + HA_i² = d² + r² = s²,
and similarly QB_i² = s² (1.47; Step 3). Therefore PA_i = QB_i = s for every i. Since both pentagonal rings also have side s, the five triangles at P and the five at Q are equilateral (D1.20).

**Step 7.** Since C_iB_i is perpendicular to π, the triangles A_iC_iB_i and A_{i+1}C_iB_i are right-angled. Their horizontal sides A_iC_i and A_{i+1}C_i both equal d. Thus
A_iB_i² = d² + r² = s²,
and
A_{i+1}B_i² = d² + r² = s²
(1.47; Steps 2–4). These are all the sloping edges used in the remaining ten faces. Consequently those faces also are equilateral, and all twenty triangles are equal by the equality of their three sides (D1.20, 1.8).

**Step 8.** We verify that these triangles bound a solid without crossing. A plane parallel to π and strictly between π and π′ cuts each of the ten sloping edges A_iB_i and A_{i+1}B_i at an interior point. Their perpendicular projections onto π lie, one on each side and in cyclic order, on the ten sides A_iC_i and C_iA_{i+1} of the inscribed decagon. The sections of the ten intervening triangles join consecutive such points (11.16, 6.2). These joins form a simple convex decagon: each join cuts off only the intervening corner of the original convex decagon, leaving all the other section points on the other side.

Thus the ten intervening triangles form an uncrossed band with the two pentagons as its boundaries. The five triangles at P close its upper end as a pentagonal pyramid, and the five at Q close its lower end in the same manner (D11.12). Equivalently, the filled intermediate section polygons, together with these two pyramids, form a solid whose entire boundary consists of the twenty triangles listed in Step 5. Since these triangles are equal and equilateral, the solid is an icosahedron (D11.27).

**Step 9.** Bisect HK at O (1.10). Then
OP = OQ = d + r/2.
Also, by the right triangles OHA_i and OKB_i,
OA_i² = OB_i² = r² + (r/2)² = 5r²/4
(1.47, 2.4). By Step 3 this equals OP². Thus all twelve vertices are equally distant from O. Furthermore,
PQ² = 4OP² = 5r² = D²,
so PQ = D (2.4; Step 1).

Describe the semicircle on diameter PQ and turn it about PQ. It produces a sphere with centre O and diameter D, on which all twelve vertices lie (P3, D11.14, D11.16, D11.17). Every edge is a chord of a circular section through O and therefore lies inside the sphere (3.2). A plane perpendicular to PQ cuts the sphere in a disk, as follows from 1.47; the vertices of each polygonal section of our solid lie on edges already inside the sphere. Those disks are convex by 3.2, so they contain the filled polygonal sections as well. Hence the entire icosahedron is comprehended in this sphere.

**Step 10.** Finally, take D as the assigned rational straight line of Book X (D10.1.3). The diameter of γ is 2r, and
(2r)² = 4r²,  D² = 5r²
(2.4; Step 1). Thus r² measures both squares, so 2r is commensurable in square with D and is therefore rational (D10.1.2, D10.1.3). The common edge s of the icosahedron is exactly the side of the equilateral pentagon inscribed in γ. Since γ has rational diameter, 13.11 applies directly: s is the irrational straight line called minor. Therefore the required icosahedron has been constructed, comprehended in a sphere of the prescribed diameter, and its side proved to be minor.

**USED:** 1.10, 1.3, 1.31, 1.33, 1.34, 1.47, 1.8, 11.12, 11.15, 11.16, 11.8, 13.10, 13.11, 13.3, 13.9, 2.1, 2.4, 3.2, 3.28, 3.29, 3.30, 4.11, 4.15, 6.13, 6.16, 6.2, 6.9, D1.20, D10.1.2, D10.1.3, D11.12, D11.14, D11.16, D11.17, D11.27, D11.3, P1, P2, P3
**Human refs (from References field):** 1.33, 11.6, 13.10, 13.11, 13.3, 13.9, 3.31, 4.15, 6.8, D5.9
**Jaccard:** 0.140 — AI adds ['1.10', '1.3', '1.31', '1.34', '1.47', '1.8', '11.12', '11.15', '11.16', '11.8', '2.1', '2.4', '3.2', '3.28', '3.29', '3.30', '4.11', '6.13', '6.16', '6.2', '6.9', 'D1.20', 'D10.1.2', 'D10.1.3', 'D11.12', 'D11.14', 'D11.16', 'D11.17', 'D11.27', 'D11.3', 'P1', 'P2', 'P3']; Human adds ['11.6', '3.31', '6.8', 'D5.9']

## Proposition 13.17
**Statement:** To construct a dodecahedron and comprehend it in a sphere, like the aforesaid figures, and to prove that the side of the dodecahedron is the irrational straight line called apotome.

**Step 1.** Let Δ be the prescribed diameter of the sphere, and take Δ as the assigned rational straight line [D10.1.3]. Construct a cube of side s such that Δ² = 3s² [13.15]. We choose the cube-and-caps construction: its advantage is that the eventual dodecahedron edge will be exactly the greater segment of the cube edge cut in extreme and mean ratio.

**Step 2.** Cut s in extreme and mean ratio into its greater segment e and lesser segment f [6.30]. Bisect these lengths and s, putting a = s/2, b = e/2, and d = f/2 [1.10]. Then a = b + d and a:b = b:d [D6.3; 5.15], whence ad = b² [6.16]. In particular, 0 < d < b < a. Put c = a + b. Applied to the division of a into b and d, Proposition 13.4 gives

a² + d² = 3b².

Furthermore, c is cut in extreme and mean ratio into its greater segment a and lesser segment b [13.5]. Applying 13.4 again gives

c² + b² = 3a².

These two square identities will establish the face lengths and the common circumsphere respectively.

**Step 3.** Let O be the centre of the cube. Use through O the three directions parallel to the three edges meeting at a cube vertex; midpoints and parallels construct these reference lines [1.10; 1.31; 6.2]. Describe positions by triples of signed lengths in these directions. Thus the eight cube vertices are

(±a, ±a, ±a).

These triples are only bookkeeping for perpendicular constructions. A reference direction is perpendicular to the plane of the other two, and its parallels retain that perpendicularity [11.4; 11.8]. Consequently, a segment with perpendicular component lengths u, v, w has square u² + v² + w², by two applications of 1.47. All distance computations below use this rule.

**Step 4.** On each cube face construct an outward cap as follows. From its centre erect a perpendicular of length b; through its endpoint draw a ridge, parallel to a selected pair of opposite edges, extending a distance b on either side. These constructions use perpendiculars, the transfer of lengths, and parallels [11.12; 1.3; 1.31]. Select the ridge directions cyclically: on the two faces perpendicular to the second reference direction, use the first direction; on the two faces perpendicular to the third, use the second; on the two faces perpendicular to the first, use the third.

The twelve ridge endpoints are therefore

(±b, ±c, 0),     (0, ±b, ±c),     (±c, 0, ±b),

with independent signs in each group. Join the ridge endpoints to the appropriate corners of their square bases [P1].

**Step 5.** We specify the caps and their assembly explicitly. On the face whose second coordinate is a, write

A = (a,a,a),   D = (−a,a,a),   F = (−a,a,−a),   G = (a,a,−a),
B = (b,c,0),   C = (−b,c,0).

The cap has square base ADFG, two trapezoidal outer faces ABCD and GBCF, and two triangular outer faces ABG and DCF. The trapezoids are planar because their bases are parallel [11.9; D1.23]. The cap can also be subdivided into the three triangular pyramids with vertex sets ADFC, AFGB, and AFCB [D11.12]. The other five caps have the identical construction.

Since b < a, each cap lies outside its cube face but within the perpendicular prism erected on that square. Indeed, sections parallel to the square interpolate between the square and the shorter, centrally placed ridge, as follows from similar triangles [6.2]. Hence distinct cap interiors do not overlap: caps on adjacent faces meet only along their common cube edge, and caps on opposite faces are disjoint. Attaching all six caps to the cube therefore gives a solid whose outer boundary consists of twelve trapezoids and twelve triangles. By the cyclic choice of ridge directions, at every cube edge exactly one of these trapezoids and one of these triangles meet.

**Step 6.** We prove that the two boundary pieces at each cube edge form one planar, convex pentagon. It suffices to examine the edge AD. The adjacent cap on the face whose third coordinate is a has the ridge endpoint

E = (0,b,c).

Its triangle ADE meets the trapezoid ABCD along AD. Let

M = (0,a,a),     N = (0,c,0),

the midpoints of AD and BC. In the plane perpendicular to AD through M, the perpendicular components of MN have lengths b and a, whereas those of ME have lengths d and b, with both directions reversed. Since ad = b², these pairs of legs are proportional. The corresponding right triangles are therefore similar [6.6], and MN and ME are opposite rays of one straight line [1.14]. Thus E lies on the line MN, and hence in the plane of ABCD [11.1].

Moreover, M lies between N and E, so the triangle and trapezoid lie on opposite sides of AD. Their union has boundary ABCDE. At A and D, each of the two angles being joined is acute: the perpendicular projections of B and C onto AD lie between A and D because b < a, and the perpendicular from E meets AD at M. These assertions follow from the perpendicular constructions and the angle sum in a right triangle [11.4; 1.32]. Their sums are therefore less than two right angles. The other vertices are already convex vertices of the trapezoid or triangle. Consequently ABCDE is a convex planar pentagon. Reversing signs or cyclically relabelling the three directions proves the same assertion at every cube edge.

**Step 7.** We now prove that this pentagon is equilateral and equiangular. By the perpendicular-distance computation of Step 3,

AB² = CD² = DE² = EA² = a² + b² + d².

The first identity of Step 2 therefore gives

AB² = CD² = DE² = EA² = 4b².

Also BC = 2b. Since the square on twice a length is four times its square, all five sides equal 2b = e [1.47; 13.4; 2.4; CN2].

The five diagonals satisfy

AD² = 4a²,
AC² = BD² = BE² = CE² = a² + b² + c² = 4a²,

using the second identity of Step 2 [1.47; 13.4; 2.4; CN2]. Thus every diagonal equals 2a. Each triangle formed by three consecutive pentagon vertices consequently has sides 2b, 2b, 2a. By side-side-side congruence, their angles at the middle vertices are equal [1.8]. These are precisely the five interior angles, since the pentagon is convex. Hence ABCDE is equilateral and equiangular. Here side-side-side is the direct choice: the distance calculation has already supplied every diagonal.

**Step 8.** A cube has twelve edges, and Step 6 combines the boundary pieces at each such edge into one pentagon. Thus the boundary of the constructed solid consists of twelve pentagons. The calculations in Step 7 are unchanged by the sign reversals and cyclic relabellings that describe the other faces. The pentagons are therefore all equilateral and equiangular, with identical corresponding sides and diagonals; triangulating each from a corresponding vertex proves them equal by 1.8. The solid is consequently a dodecahedron [D11.28]. Its vertices are the eight original cube vertices and the twelve ridge endpoints.

**Step 9.** We next verify the sphere. Every original cube vertex has squared distance 3a² from O [1.47]. Every added vertex has squared distance

b² + c² = 3a²

from O, by Step 2 [1.47; 13.4]. All twenty vertices therefore lie on the sphere centred at O with radius R satisfying R² = 3a² [D11.14; D11.16]. Since s = 2a and Δ² = 3s², this sphere has diameter Δ [2.4; 13.15].

The whole solid, not merely its vertices, is contained in this sphere. Subdivide the cube into triangular pyramids by joining O to triangulated cube faces; subdivide each cap into the triangular pyramids specified in Step 5 [P1; D11.12]. Every vertex of these pyramids is on or inside the sphere. A segment between two points on or inside the sphere remains inside it: take a plane through the two points and O and apply the fact that a circle contains its chords [3.2; D11.14]. Applying this first to segments, then to triangles, and then to pyramids proves the required containment. Thus the dodecahedron is comprehended in the sphere of diameter Δ.

**Step 10.** Finally, Δ² = 3s² shows that s is commensurable in square with the assigned rational line Δ; hence s is rational [D10.1.2; D10.1.3]. Its division into e and f was constructed in extreme and mean ratio, and the dodecahedron edge is exactly e, its greater segment. Therefore that edge is the irrational straight line called apotome [13.6]. This uses the golden division already present in the construction, without any additional classification of irrationals. The dodecahedron has been constructed, comprehended in the prescribed sphere, and its side proved to be an apotome.

**USED:** 1.10, 1.14, 1.3, 1.31, 1.32, 1.47, 1.8, 11.1, 11.12, 11.4, 11.8, 11.9, 13.15, 13.4, 13.5, 13.6, 2.4, 3.2, 5.15, 6.16, 6.2, 6.30, 6.6, CN2, D1.23, D10.1.2, D10.1.3, D11.12, D11.14, D11.16, D11.28, D6.3, P1
**Human refs (from References field):** 1.47, 1.8, 11.1, 11.38, 11.6, 13.15, 13.4, 13.5, 13.6, 13.7, 5.15, 6.32
**Jaccard:** 0.216 — AI adds ['1.10', '1.14', '1.3', '1.31', '1.32', '11.12', '11.4', '11.8', '11.9', '2.4', '3.2', '6.16', '6.2', '6.30', '6.6', 'CN2', 'D1.23', 'D10.1.2', 'D10.1.3', 'D11.12', 'D11.14', 'D11.16', 'D11.28', 'D6.3', 'P1']; Human adds ['11.38', '11.6', '13.7', '6.32']

## Proposition 13.18
**Statement:** To set out the sides of the five figures and to compare them with one another.

**Step 1.** Fix a sphere with diameter D. Let t, o, c, i, and d denote respectively the sides of the pyramid (tetrahedron), octahedron, cube, icosahedron, and dodecahedron constructed in this sphere by 13.13, 13.14, 13.15, 13.16, and 13.17. Write a² for the square on a line a, and ab for the rectangle contained by a and b. Our path is to retain the auxiliary pentagons and cube of these constructions and compare square areas, rather than classify irrational lines. Squares placed at a common corner show that their order is exactly the order of their sides (1.46, CN5).

**Step 2.** The first three constructions give
D² = (3/2)t²,  D² = 2o²,  D² = 3c²
(13.13, 13.14, 13.15). Consequently,
t² = (2/3)D²,  o² = (1/2)D²,  c² = (1/3)D².
Thus t² : o² : c² = 4 : 3 : 2, and in particular t > o > c (CN5 and Step 1).

**Step 3.** Retain the two auxiliary regular pentagons in the construction of the icosahedron in 13.16. Their planes are parallel, their centres lie on a common perpendicular axis through the sphere's centre, and their planes are equally distant from that centre. Their vertices alternate when projected onto one plane: one pentagon is turned through half a pentagon's central angle relative to the other. Let r be their common circumradius, h the distance between their planes, and x the side of the regular decagon formed by those ten projected vertices. Each pentagon has side i (13.16). The hexagon inscribed in its circumcircle has side r (4.15); hence
i² = r² + x²
by 13.10. This is the immediate square relation for the pentagonal auxiliary figure.

**Step 4.** An edge joining neighbouring vertices in different pentagonal planes has perpendicular components h and x: its projection joins adjacent vertices of the projected decagon. Therefore
i² = h² + x²
(13.16, D11.3, 1.47). Comparison with Step 3 gives h² = r², and hence h = r (CN3 and Step 1). A radius from the sphere's centre to a pentagon vertex has perpendicular components r and h/2. Thus
(D/2)² = r² + (h/2)²,
and consequently
D² = 4r² + h² = 5r²
(1.47, 2.4).

**Step 5.** Retain also the cube used in the construction of the dodecahedron in 13.17. It is inscribed in the same sphere, and therefore its side is c (13.15). Its edges are diagonals of the pentagonal faces of the dodecahedron (13.17). The diagonal relation makes 13.8 the natural next tool: intersecting diagonals of a regular pentagon divide one another in extreme and mean ratio, with the greater segment equal to the pentagon's side. Hence
c : d = d : (c − d),  with d > c − d.
Thus d is the greater segment of c cut in extreme and mean ratio, and
d² = c(c − d)
(D6.3, 6.17).

**Step 6.** The five sides can now be set out by plane constructions alone. Obtain the thirds, half, and fifth of D by 6.9. Construct mean proportionals between D and, respectively, 2D/3, D/2, D/3, and D/5 by 6.13. Their squares are respectively (2/3)D², (1/2)D², (1/3)D², and (1/5)D² (6.17, 6.1); therefore they give t, o, c, and r by Steps 2 and 4. Describe a circle of radius r and inscribe a regular pentagon in it (P3, 4.11). Its side is i: its centre-and-side triangles are congruent to those of the auxiliary pentagon in Step 3 (1.4). Finally, cut c in extreme and mean ratio by 6.30 and take the greater segment; this is d by Step 5. Indeed, the equation u² = c(c − u) admits at most one positive segment u, since increasing u increases its square and decreases the rectangle on the right (6.1, CN5). Thus all five sides have been set out.

**Step 7.** To compare the icosahedral side with the others, apply 13.9 to the hexagon and decagon in the circle of radius r. It gives
(r + x) : r = r : x,
so
r² = x(r + x) = rx + x²
(6.17, 2.1). In particular r² > x², whence r > x (CN5 and Step 1). Therefore rx > x² (6.1), and the displayed equality yields r² > 2x². Using Step 3, we obtain
r² < i² < (3/2)r².
Since D² = 5r², this is
(1/5)D² < i² < (3/10)D².

**Step 8.** From d > c − d in Step 5, the smaller segment c − d is less than half of c. Hence
 d² = c(c − d) < (1/2)c² = (1/6)D²
(6.1, CN5, and Step 2).

**Step 9.** Since (1/6)D² < (1/5)D² and (3/10)D² < (1/3)D², Steps 7 and 8 give
 d² < i² < c².
Combining this with Step 2 and passing from squares to their sides gives
 t > o > c > i > d
(CN5 and Step 1). Therefore, for the same circumscribed sphere, the pyramid has the greatest side, next the octahedron, next the cube, next the icosahedron, and last the dodecahedron. The sides of all five figures have thus been set out and compared.

**USED:** 1.4, 1.46, 1.47, 13.10, 13.13, 13.14, 13.15, 13.16, 13.17, 13.8, 13.9, 2.1, 2.4, 4.11, 4.15, 6.1, 6.13, 6.17, 6.30, 6.9, CN3, CN5, D11.3, D6.3, P3
**Human refs (from References field):** 13.10, 13.13, 13.14, 13.15, 13.16, 13.17, 13.9, 4.15, 6.20, 6.4, 6.8, D5.9
**Jaccard:** 0.276 — AI adds ['1.4', '1.46', '1.47', '13.8', '2.1', '2.4', '4.11', '6.1', '6.13', '6.17', '6.30', '6.9', 'CN3', 'CN5', 'D11.3', 'D6.3', 'P3']; Human adds ['6.20', '6.4', '6.8', 'D5.9']
