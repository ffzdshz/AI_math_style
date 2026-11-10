# Book 13 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 13.1
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half.

**Step 1.** Let the whole line have length a, its greater segment g, and its lesser segment s. Bisect the whole by I.10, and denote its half by h. Thus a = g + s = h + h. By the definition of extreme and mean ratio, a : g = g : s. Write Q(x) for the square on x and R(x,y) for the rectangle contained by x and y. [1.10, D6.3]

**Step 2.** Since a, g, s are proportional, VI.17 gives Q(g) = R(a,s). Dividing the side a into its two equal halves, II.1 gives R(a,s) = 2R(h,s). Hence Q(g) = 2R(h,s). [6.17, 2.1, CN1]

**Step 3.** The required square is on the sum g + h, so take the direct square-of-a-sum route using II.4. It gives
Q(g + h) = Q(g) + Q(h) + 2R(g,h).
Substituting the equality from Step 2, we obtain
Q(g + h) = 2R(h,s) + 2R(h,g) + Q(h). [2.4, CN2, CN1]

**Step 4.** By II.1, since s + g = a and a consists of two halves h,
R(h,s) + R(h,g) = R(h,a) = 2Q(h).
Adding this equality to itself and then adding Q(h), Step 3 therefore yields
Q(g + h) = 4Q(h) + Q(h) = 5Q(h).
Thus the square on the greater segment together with half the whole is five times the square on the half, as required. [2.1, CN2, CN1]

**USED:** 1.10, 2.1, 2.4, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 6.1, 6.17, D6.3
**Jaccard:** 0.250 — AI adds ['1.10', '2.1', '2.4', 'CN1', 'CN2']; Human adds ['6.1']

## Proposition 13.2
**Statement:** If the square on a straight line be five times the square on a segment of it, then, when the double of the said segment is cut in extreme and mean ratio, the greater segment is the remaining part of the original straight line.

**Step 1.** Let C lie between A and B, and suppose that the square on AB is five times the square on AC. Let DE be twice AC, and cut DE at F in extreme and mean ratio, DF being the greater segment. Such a division is possible by 6.30. Thus AC is half of DE. [6.30]

**Step 2.** Apply 13.1 directly to this division: this is the natural route because the half of DE is precisely the given segment AC. The square on DF + AC is therefore five times the square on AC. By the hypothesis, the square on AB is equal to that same area. Consequently, the square on DF + AC equals the square on AB. [13.1, CN1]

**Step 3.** Hence DF + AC = AB. For if these lengths were unequal, apply 2.4 to the longer, divided into a part equal to the shorter and the positive excess. Its square would equal the square on the shorter together with the square on the excess and twice the rectangle contained by the shorter and the excess. It would therefore be greater than the square on the shorter, contradicting Step 2. [2.4, CN5]

**Step 4.** Subtract AC from the equal lengths DF + AC and AB. The remainders are equal, so DF = CB. Thus, when the double of the given segment is cut in extreme and mean ratio, its greater segment is the remaining part of the original straight line. [CN3]

**USED:** 13.1, 2.4, 6.30, CN1, CN3, CN5
**Human refs (from References field):** 6.1
**Jaccard:** 0.000 — AI adds ['13.1', '2.4', '6.30', 'CN1', 'CN3', 'CN5']; Human adds ['6.1']

## Proposition 13.3
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the lesser segment added to the half of the greater segment is five times the square on the half of the greater segment.

**Step 1.** Let AB be cut in extreme and mean ratio at C, with AC the greater segment and CB the lesser. Bisect AC at D, so that AD = DC. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. [1.10]

**Step 2.** By the definition of extreme and mean ratio,
AB : AC = AC : CB.
Thus R(AB,CB) = S(AC). We use the three-proportional-lines theorem directly, since the defining proportion already has this form. [D6.3, 6.17]

**Step 3.** Apply the bisection-and-extension identity to AC, bisected at D and extended by CB. This route directly supplies the square on DB, the sum of the lesser segment and half the greater segment:
S(DB) = R(AB,CB) + S(DC). [2.6]

**Step 4.** Applying the square-of-a-divided-line identity to AC gives
S(AC) = S(AD) + S(DC) + 2R(AD,DC).
Since AD = DC, each of S(AD) and R(AD,DC) is S(DC). Hence
S(AC) = 4S(DC). [2.4]

**Step 5.** Combining Steps 2 and 4 yields R(AB,CB) = 4S(DC). Adding S(DC) to both sides and using Step 3, we obtain
S(DB) = 5S(DC).
But DB is CB added to DC, and DC is half the greater segment AC. Therefore the square on the lesser segment added to half the greater segment is five times the square on half the greater segment, as required. [CN1, CN2]

**USED:** 1.10, 2.4, 2.6, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.10', '2.4', '2.6', '6.17', 'CN1', 'CN2', 'D6.3']

## Proposition 13.4
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.

**Step 1.** Let AB be cut in extreme and mean ratio at C, with AC the greater segment and CB the lesser. By the definition of extreme and mean ratio,
AB : AC = AC : CB. [D6.3]

**Step 2.** These three straight lines are proportional; therefore the rectangle contained by AB and CB equals the square on AC. [6.17]

**Step 3.** Apply II.7 to AB cut at C, taking CB as the specified segment. This is the direct route because the proposition gives exactly the required pair of squares: the square on AB and the square on CB together equal twice the rectangle contained by AB and CB together with the square on AC. [2.7]

**Step 4.** By Step 2, adding that rectangle to itself gives an area equal to two squares on AC; adding the square on AC to both gives three squares on AC. Thus the equality in Step 3 shows that the square on AB and the square on CB together are triple the square on AC. Hence the squares on the whole and the lesser segment together are triple the square on the greater segment, as required. [CN2, CN1]

**USED:** 2.7, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 6.17, D6.3
**Jaccard:** 0.400 — AI adds ['2.7', 'CN1', 'CN2']

## Proposition 13.5
**Statement:** If a straight line be cut in extreme and mean ratio, and there be added to it a straight line equal to the greater segment, the whole straight line has been cut in extreme and mean ratio, and the original straight line is the greater segment.

**Step 1.** Let the greater and lesser segments of the original straight line have lengths a and b, respectively, and let its whole length be s = a + b. Since it is cut in extreme and mean ratio, s : a = a : b. Add a straight line of length a to the original line, making the new whole of length t = s + a. [D6.3]

**Step 2.** Use the direct sum-of-antecedents and sum-of-consequents rule, since these sums are precisely the new whole and the original line. Applied to s : a = a : b, it gives
(s + a) : (a + b) = s : a.
Thus t : s = s : a. [5.12]

**Step 3.** The original whole s is greater than its part a. Hence the new whole t has segments s and a, with s the greater; and the proportion t : s = s : a shows that it is cut in extreme and mean ratio. Therefore the original straight line is the greater segment of the new whole, as required. [CN5, D6.3]

**USED:** 5.12, CN5, D6.3
**Human refs (from References field):** 5.14, 6.17, D6.3
**Jaccard:** 0.200 — AI adds ['5.12', 'CN5']; Human adds ['5.14', '6.17']

## Proposition 13.6
**Statement:** If a rational straight line be cut in extreme and mean ratio, each of the segments is the irrational straight line called apotome.

**Step 1.** Let the rational straight line have length L, and let its greater and lesser segments in extreme and mean ratio have lengths a and b. Thus L = a + b. Bisect L, and denote its half by h. Put t = a + h and u = L + h = 3h. [1.10]

**Step 2.** Use XIII.1 directly, because it relates an auxiliary square to the square on half the given rational whole. It gives t² = 5h². Also, since squares have the duplicate ratio of their sides, L² = 4h² and u² = 9h². Consequently the squares on h, t, u, and L have h² as a common measure. Since L is rational, its square is commensurable with the square on the assigned rational straight line; transitivity of commensurability therefore shows that h, t, and u are all rational straight lines. [13.1, 6.20, D10.1.2, 10.12, D10.1.3]

**Step 3.** The ratio t² : h² = 5 : 1 is not the ratio of a square number to a square number. Indeed, if m² = 5n² for relatively prime positive integers m and n, VII.30 would imply that 5 divides m; writing m = 5k then gives n² = 5k², so VII.30 would also imply that 5 divides n, a contradiction. Hence X.9 shows that t and h are incommensurable in length. Together with Step 2, this says that they are commensurable in square only. [7.30, 10.9, D10.1.2]

**Step 4.** Now a = t − h > 0. Thus the greater segment is obtained by subtracting from the rational straight line t the rational straight line h, which is commensurable with t in square only. By X.73, a is irrational and is called an apotome. [10.73]

**Step 5.** Since u = 3h, the lines u and h are commensurable in length, h being a common measure. Since h is incommensurable in length with t, X.13 implies that u is also incommensurable in length with t. Their squares, however, are commensurable by Step 2. Thus the rational straight lines u and t are commensurable in square only. [D10.1.1, 10.13, D10.1.2]

**Step 6.** Subtracting t = a + h from u = L + h leaves L − a = b. Therefore b = u − t > 0. The lesser segment is consequently also the remainder after subtracting from a rational straight line a rational straight line commensurable with it in square only. By X.73, b is irrational and is called an apotome. Hence each segment of the given rational straight line is the irrational straight line called apotome. [CN3, 10.73]

**USED:** 1.10, 10.12, 10.13, 10.73, 10.9, 13.1, 6.20, 7.30, CN3, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 10.97, 13.1, 6.17, D10.1.4, D6.3
**Jaccard:** 0.176 — AI adds ['1.10', '10.12', '10.13', '6.20', '7.30', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.6', '10.97', '6.17', 'D10.1.4', 'D6.3']

## Proposition 13.7
**Statement:** If three angles of an equilateral pentagon, taken either in order or not in order, be equal, the pentagon will be equiangular.

**Step 1.** Let ABCDE be the pentagon, with AB = BC = CD = DE = EA. Join AC, BE, BD, and CE [P1]. Up to relabelling around the boundary, the three equal angles occur either at A, C, D or at A, B, C. We first treat the nonconsecutive arrangement; the consecutive arrangement will then reduce to it.

**Step 2.** Suppose ∠EAB = ∠BCD = ∠CDE. Apply side–angle–side to triangles EAB, BCD, and CDE: this is the natural congruence criterion because their equal included angles are given. Their corresponding sides and angles are equal [1.4]. Consequently BE = BD = CE. Moreover, their base angles are all equal, since each triangle is isosceles [1.5, CN1]. Denote this common base angle by α; thus
∠ABE = ∠BEA = ∠CBD = ∠BDC = ∠DCE = ∠CED = α.

**Step 3.** Since BE = BD, triangle BED gives ∠BED = ∠BDE [1.5]. Adding the equal angles ∠BEA and ∠BDC therefore gives
∠DEA = ∠BED + α = ∠BDE + α = ∠CDE [CN2].
Likewise, BE = CE gives ∠EBC = ∠BCE [1.5], and hence
∠ABC = α + ∠EBC = α + ∠BCE = ∠BCD [CN2].
Thus the angles at E and B equal the given equal angles at D and C respectively. All five angles are therefore equal in the nonconsecutive case [CN1].

**Step 4.** Now suppose ∠EAB = ∠ABC = ∠BCD. Triangles EAB and ABC have equal corresponding sides enclosing equal angles, so BE = AC and their corresponding base angles are equal [1.4]. Since they are also isosceles, write
∠EBA = ∠BEA = ∠BAC = ∠BCA = β [1.5, CN1].
Let F be the intersection of diagonals AC and BE.

**Step 5.** In triangle ABF, the angles BAF and ABF both equal β. Therefore AF = BF [1.6]. Subtracting these equal lengths from AC = BE yields FC = FE [CN3]. Triangle CFE is consequently isosceles, so ∠FCE = ∠CEF [1.5]. Because F lies on AC and BE, this says
∠ACE = ∠BEC.

**Step 6.** Since CD = DE, triangle CDE gives ∠ECD = ∠CED [1.5]. Adding this equality, the equality from Step 5, and ∠BCA = ∠BEA = β, we obtain
∠BCD = ∠BCA + ∠ACE + ∠ECD
= ∠BEA + ∠BEC + ∠CED
= ∠DEA [CN2].
Thus the angle at E equals the given equal angles at A, B, and C [CN1].

**Step 7.** In particular, the angles at B, C, and E are equal. These form the nonconsecutive arrangement already proved in Steps 2–3, so that case shows that all five angles are equal. Hence, whether the three given equal angles are taken in order or not in order, the equilateral pentagon is equiangular.

**USED:** 1.4, 1.5, 1.6, CN1, CN2, CN3, P1
**Human refs (from References field):** 1.4, 1.5, 1.6, 1.8
**Jaccard:** 0.375 — AI adds ['CN1', 'CN2', 'CN3', 'P1']; Human adds ['1.8']

## Proposition 13.8
**Statement:** If in an equilateral and equiangular pentagon straight lines subtend two angles taken in order, they cut one another in extreme and mean ratio, and their greater segments are equal to the side of the pentagon.

**Step 1.** Let ABCDE be the given equilateral and equiangular pentagon, with its vertices in order. Draw AC and BD, which subtend the consecutive angles at B and C, and let them meet at P. Also draw AD. Let u denote one fifth of two right angles. The triangles ABC, ACD, and ADE partition the pentagon, so its interior angles together equal six right angles, or 15u. Since its five angles are equal, each equals 3u. [P1, 1.32, CN2]

**Step 2.** Since AB = BC and BC = CD, the triangles ABC and BCD are isosceles. Their vertex angles at B and C respectively equal 3u, while each triangle has angle sum 5u. Consequently,
∠BAC = ∠BCA = ∠CBD = ∠BDC = u. [1.5, 1.32]

**Step 3.** Because P lies on AC and BD,
∠BAP = u and ∠ABP = ∠ABC − ∠CBD = 2u.
Thus ∠APB = 2u, and the equal angles at B and P in triangle ABP give AP = AB.
Similarly,
∠CDP = u and ∠PCD = ∠BCD − ∠BCA = 2u.
Thus ∠CPD = 2u, and the equal angles at C and P in triangle CDP give DP = CD. As all pentagon sides are equal, we have
AP = DP = BC. [CN3, 1.32, 1.6, CN1]

**Step 4.** In triangle BPC, the angles at B and C both equal u, so the angle at P equals 3u. The side opposite the greater angle is greater; hence BC > BP and BC > PC. Since AP = DP = BC, it follows that AP > PC and DP > PB. Therefore AP and DP are the greater segments of AC and BD respectively. [1.32, 1.19, CN1]

**Step 5.** Use equiangular-triangle proportionality directly, since the preceding angle equalities supply its hypotheses. Triangles ABC and BPC are equiangular, with A corresponding to B, B to P, and C to C. Their corresponding sides therefore give
AC : BC = BC : PC.
Likewise, triangles BCD and BPC are equiangular, with B corresponding to B, C to P, and D to C. Thus
BD : BC = BC : PB. [6.4]

**Step 6.** Substitute AP = BC into the first proportion and DP = BC into the second:
AC : AP = AP : PC,
BD : DP = DP : PB.
By Step 4, the middle terms are precisely the greater segments. Thus each diagonal is cut by the other in extreme and mean ratio. By Step 3, both greater segments equal a side of the pentagon. This proves the proposition. [CN1, D6.3]

**USED:** 1.19, 1.32, 1.5, 1.6, 6.4, CN1, CN2, CN3, D6.3, P1
**Human refs (from References field):** 1.32, 1.4, 1.5, 1.6, 3.28, 4.14, 5.14, 6.33, 6.4
**Jaccard:** 0.267 — AI adds ['1.19', 'CN1', 'CN2', 'CN3', 'D6.3', 'P1']; Human adds ['1.4', '3.28', '4.14', '5.14', '6.33']

## Proposition 13.9
**Statement:** If the side of the hexagon and that of the decagon inscribed in the same circle be added together, the whole straight line has been cut in extreme and mean ratio, and its greater segment is the side of the hexagon.

**Step 1.** Let O be the centre of the given circle, r its radius, h the side of its inscribed regular hexagon, and d the side of its inscribed regular decagon. Join O to the vertices [P1]. All these radii are equal [D1.15]. Equal sides cut off equal minor arcs, and equal arcs subtend equal angles at the centre [3.28, 3.27]. Since the angles about O together equal four right angles [1.13], consecutive vertices of the hexagon subtend 60° at O, and consecutive vertices of the decagon subtend 36°.

**Step 2.** Let UV be a side of the hexagon. In triangle OUV, OU = OV and ∠UOV = 60°. Its base angles are equal and together equal 120°, so each is 60° [1.5, 1.32]. Equal angles subtend equal sides; hence UV = OU, and therefore h = r [1.6].

**Step 3.** Let AB be a side of the decagon. In triangle OAB, OA = OB = r, AB = d, and ∠AOB = 36°. Thus ∠OAB = ∠ABO = 72° [1.5, 1.32]. Bisect ∠OAB by AD, meeting OB at D [1.9]. Then ∠OAD = ∠DAB = 36°.

**Step 4.** In triangle OAD, ∠AOD = ∠OAD = 36°, so OD = AD [1.6]. In triangle ADB, ∠DAB = 36° and ∠ABD = 72°; therefore ∠ADB = 72° [1.32], and AD = AB [1.6]. Consequently OD = AD = AB = d. Moreover, in triangle ADB the angle at B is greater than the angle at A, so AD > DB [1.19]. Thus OD > DB.

**Step 5.** Use the angle-bisector theorem here, since it directly gives the proportion between the two parts of the radius:
OD : DB = OA : AB [6.3].
As OA = OB and AB = OD, this is
OB : OD = OD : DB.
Since OD is the greater segment, OB has been cut at D in extreme and mean ratio, with its greater segment equal to d [D6.3].

**Step 6.** Apply 13.5: adjoining to a line cut in extreme and mean ratio a line equal to its greater segment produces another such division, whose greater segment is the original whole. Here the original whole is r and its greater segment is d. Hence r + d is cut in extreme and mean ratio into r and d, with r the greater segment [13.5]. Since h = r by Step 2, the sum h + d is cut in extreme and mean ratio, and its greater segment is the side h of the hexagon, as required.

**USED:** 1.13, 1.19, 1.32, 1.5, 1.6, 1.9, 13.5, 3.27, 3.28, 6.3, D1.15, D6.3, P1
**Human refs (from References field):** 1.32, 1.5, 4.15, 6.33, 6.4
**Jaccard:** 0.125 — AI adds ['1.13', '1.19', '1.6', '1.9', '13.5', '3.27', '3.28', '6.3', 'D1.15', 'D6.3', 'P1']; Human adds ['4.15', '6.33', '6.4']

## Proposition 13.10
**Statement:** If an equilateral pentagon be inscribed in a circle, the square on the side of the pentagon is equal to the squares on the side of the hexagon and on that of the decagon inscribed in the same circle.

**Step 1.** Let O be the centre of the circle, let r be its radius, and let p, h, d denote respectively the sides of the inscribed equilateral pentagon, hexagon, and decagon. Equal chords cut off equal corresponding arcs, so the successive arcs of each polygon are equal. The six hexagonal arcs therefore give six equal central angles. Each is one third of two right angles; and, since the two radii forming such an angle are equal, the other two angles of the triangle are equal and have that same magnitude. Thus its three sides are equal, and h = r. [3.28, 3.27, D1.15, 1.5, 1.32, 1.6]

**Step 2.** Take a pentagon side AB and bisect it at H. Join OH and extend it to meet the minor arc AB at C; join AC and BC. Since AB is not a diameter, the line through the centre bisecting AB is perpendicular to AB. Moreover, O, H, C occur in that order. Put AH = HB = x and OH = u. Thus p = 2x and HC = r − u. [1.10, P1, P2, 3.3]

**Step 3.** The right triangles AHC and BHC give AC² = AH² + HC² = BH² + HC² = BC². Hence AC = BC, and their corresponding arcs are equal. Together these arcs form the pentagonal arc AB, which is one fifth of the circumference; each is therefore one tenth. Consequently AC = BC = d, the side of the inscribed decagon. [1.47, 3.28, 3.29]

**Step 4.** Use XIII.9 directly, since it already relates the hexagon and decagon sides needed here. It says that r + d is cut in extreme and mean ratio with greater segment r. Thus (r + d):r = r:d, and consequently
r² = (r + d)d = rd + d².  (1)
Here and below, products denote rectangles and squares denote their areas. [13.9, D6.3, 6.17, 2.3]

**Step 5.** Applying the right-triangle theorem to OHA and CHA gives
r² = x² + u²,
d² = x² + (r − u)².  (2)
[1.47]

**Step 6.** Apply II.7 to the radius cut into u and r − u:
r² + u² = 2ru + (r − u)².
Adding x² to both sides and using (2) gives
2r² = 2ru + d².
Together with (1), this yields
2ru = r² + rd = r(r + d).
The left side is the rectangle r(2u). These equal rectangles have the same positive height r, so their bases are equal:
2u = r + d.  (3)
[2.7, CN2, CN3, 2.1, 2.3, 6.1]

**Step 7.** Multiply the first equality in (2) by four. Since 2x = p and, by (3), 2u = r + d, the square-of-a-sum identity gives
4r² = p² + (r + d)² = p² + r² + 2rd + d².
Add d² to both sides and use (1):
4r² + d² = p² + r² + 2(rd + d²) = p² + 3r².
Subtracting 3r² gives p² = r² + d². Since h = r, this is p² = h² + d²: the square on the pentagon side equals the squares on the hexagon and decagon sides inscribed in the same circle. [2.4, CN2, CN3]

**USED:** 1.10, 1.32, 1.47, 1.5, 1.6, 13.9, 2.1, 2.3, 2.4, 2.7, 3.27, 3.28, 3.29, 3.3, 6.1, 6.17, CN2, CN3, D1.15, D6.3, P1, P2
**Human refs (from References field):** 1.26, 1.32, 1.4, 1.5, 2.2, 3.26, 4.15, 6.17, 6.33, 6.4
**Jaccard:** 0.103 — AI adds ['1.10', '1.47', '1.6', '13.9', '2.1', '2.3', '2.4', '2.7', '3.27', '3.28', '3.29', '3.3', '6.1', 'CN2', 'CN3', 'D1.15', 'D6.3', 'P1', 'P2']; Human adds ['1.26', '1.4', '2.2', '3.26', '4.15', '6.33', '6.4']

## Proposition 13.11
**Statement:** If in a circle which has its diameter rational an equilateral pentagon be inscribed, the side of the pentagon is the irrational straight line called minor.

**Step 1.** Let D be the given rational diameter, r its half, and p the side of the inscribed equilateral pentagon. Set out D as the rational straight line of reference. Since r²:D² = 1:4, r is rational. [10.6, D10.1.3]

**Step 2.** Inscribe a regular hexagon in the circle. Its side equals r: joining its vertices to the centre gives six triangles whose corresponding sides are equal, since their two radial sides are equal and their bases are equal. Their central angles are therefore equal, each being two-thirds of a right angle. Each triangle is isosceles, and its angle sum is two right angles; consequently its base angles also equal two-thirds of a right angle. Thus each triangle is equilateral, proving that the hexagon’s side is r. [4.15, D1.15, 1.8, 1.5, 1.32, 1.6]

**Step 3.** Let d be the side of the regular decagon inscribed in the same circle. The line r+d is cut in extreme and mean ratio, with greater segment r and lesser segment d. Therefore, putting t = d+r/2, the square on the lesser segment together with half the greater segment satisfies

t² = 5(r/2)² = 5r²/4. [13.9, 13.3]

**Step 4.** We use the direct square identity for the pentagon’s side: p² = r²+d². Also, expanding the square on t gives

t² = d²+rd+r²/4.

Together with Step 3, this yields d²+rd = r². Hence, if u = 5r/2,

p² = r²+d² = 2r²−rd = r(2r−d) = r(u−t).

Thus the required square is a rectangle with rational side r; it remains to classify its other side u−t. [13.10, 2.4, 2.1]

**Step 5.** We have u² = 25r²/4 and t² = 5r²/4. Consequently u²:D² = 25:16 and t²:D² = 5:16, so u and t are rational straight lines. Their squares have ratio 5:1 and are therefore commensurable. But 5:1 is not the ratio of a square number to a square number, so u and t are incommensurable in length. Since u>t, their difference u−t is an apotome. [10.6, D10.1.3, 10.9, 10.73]

**Step 6.** Moreover,

u²−t² = 5r² = (2t)²,

and u²:(2t)² = 5:4. This is not a ratio of square numbers, so 2t is incommensurable in length with u. Meanwhile u:D = 5:4, so the whole u is commensurable in length with the rational line set out. The apotome u−t therefore meets exactly the definition of a fourth apotome: the excess of the square on its whole over the square on its annex is the square on a line incommensurable with the whole. [10.9, 10.6, D10.3.4]

**Step 7.** By Step 4, the square on p is the rectangle contained by the rational straight line r and the fourth apotome u−t. The direct classification theorem for such an area says that its square-side is minor. Therefore the side p of the inscribed equilateral pentagon is the irrational straight line called minor, as required. [10.94]

**USED:** 1.32, 1.5, 1.6, 1.8, 10.6, 10.73, 10.9, 10.94, 13.10, 13.3, 13.9, 2.1, 2.4, 4.15, D1.15, D10.1.3, D10.3.4
**Human refs (from References field):** 1.32, 10.12, 10.15, 10.73, 10.9, 10.94, 13.1, 13.8, 5.18, 5.19, D10.3.4
**Jaccard:** 0.217 — AI adds ['1.5', '1.6', '1.8', '10.6', '13.10', '13.3', '13.9', '2.1', '2.4', '4.15', 'D1.15', 'D10.1.3']; Human adds ['10.12', '10.15', '13.1', '13.8', '5.18', '5.19']

## Proposition 13.12
**Statement:** If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.

**Step 1.** Let ABC be an equilateral triangle inscribed in the given circle, and write R for a right angle. Since AB = BC = CA, the three angles of ABC are equal; since their sum is 2R, each is 2R/3. We use a diameter through A to obtain a right triangle directly. [1.5, 1.32]

**Step 2.** Find the centre O, draw AO, and produce it through O to meet the circle again at D. Join BD and BO. The radii satisfy AO = OB = OD, and AD is a diameter. [3.1, P1, P2, D1.15]

**Step 3.** The point D is distinct from B and C, since otherwise an angle of ABC would be right by the semicircle theorem, contrary to Step 1. Since AD is a diameter, ∠ABD = R, so ∠ADB is acute. The angle ACB is also acute. Thus, by the greater- and lesser-segment assertions of III.31, C and D lie in the same greater segment bounded by AB. The same-segment theorem is therefore the direct applicable theorem, giving
∠ADB = ∠ACB = 2R/3. [3.31, 1.32, 3.21]

**Step 4.** Because O lies between A and D, ∠ODB = ∠ADB = 2R/3. In triangle OBD, OB = OD, so ∠OBD = ∠ODB = 2R/3. Its remaining angle BOD is consequently also 2R/3. Equal angles have equal opposite sides; hence BD = OD. Thus BD equals a radius of the circle. [D1.15, 1.5, 1.32, 1.6]

**Step 5.** Write XY² for the square on XY. Since AO = OD, applying II.4 to AD cut at O gives
AD² = AO² + OD² + 2(AO · OD) = 4OD².
Here AO · OD denotes the rectangle contained by AO and OD, which is a square because those lengths are equal. [2.4, CN2]

**Step 6.** Applying the right-triangle theorem to ABD gives
AB² + BD² = AD².
Substituting BD = OD and the equality from Step 5 yields
AB² + OD² = 4OD².
Subtracting OD² gives AB² = 3OD². Since AB is a side of the equilateral triangle and OD is a radius, the square on the side is triple the square on the radius, as required. [1.47, CN3]

**USED:** 1.32, 1.47, 1.5, 1.6, 2.4, 3.1, 3.21, 3.31, CN2, CN3, D1.15, P1, P2
**Human refs (from References field):** 1.47, 3.31, 4.15
**Jaccard:** 0.143 — AI adds ['1.32', '1.5', '1.6', '2.4', '3.1', '3.21', 'CN2', 'CN3', 'D1.15', 'P1', 'P2']; Human adds ['4.15']

## Proposition 13.13
**Statement:** To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.

**Step 1.** Let AB be the diameter of a generating semicircle of the given sphere, and let O be its centre. Thus O is also the sphere’s centre, and OA = OB. Cut off CB equal to one third of AB, so that AC = 2CB. In the plane of the semicircle draw CD perpendicular to AB, meeting the semicircle at D. Write t = CB and r = CD; thus AC = 2t and AB = 3t. [D11.14, D11.16, D11.17, D1.15, 6.9, 1.11]

**Step 2.** Construct the plane of the base as follows. At C erect CT perpendicular to the plane of the semicircle. The intersecting lines CD and CT determine a plane Π. Since AB is perpendicular to both CD and CT, it is perpendicular to Π. In Π describe the circle k with centre C and radius CD. [11.12, D11.3, 11.2, 11.4, P3]

**Step 3.** Determine the radius of k. Since the sphere’s centre already bisects AB, II.5 applies directly to the equal division at O and the unequal division at C:

AC·CB + OC² = OA².

The right triangle OCD gives

CD² + OC² = OD².

But OA = OD, being radii of the generating circle. Subtracting OC² from these equal areas therefore gives

r² = CD² = AC·CB = 2t².

Here products denote rectangles and squared lengths denote the corresponding squares. [2.5, 1.47, D1.15, CN3]

**Step 4.** The circle k lies on the given sphere. Indeed, for any point X of k, CX = CD, and OC is perpendicular to CX. Consequently,

OX² = OC² + CX² = OC² + CD² = OD².

Thus every point of k is at the sphere’s radius from O. Equivalently, as the generating semicircle revolves about AB, D describes precisely this circle, whose centre is C and whose plane is perpendicular to AB. Hence k is on the given sphere. [D1.15, D11.3, 1.47, D11.14, D11.16]

**Step 5.** Construct an auxiliary equilateral triangle, and inscribe in k a triangle EFG equiangular with it. The auxiliary triangle has equal angles, and therefore EFG has equal sides. Join A to E, F, and G. Since A is outside Π, these joins and the base EFG form a triangular pyramid. All four vertices lie on the given sphere, so the pyramid is comprehended by it. [1.1, 1.5, 4.2, 1.6, P1, D11.12]

**Step 6.** We use XIII.12 for the base because its circumradius r has already been determined. It gives

EF² = FG² = GE² = 3r² = 6t².

Also, AC is perpendicular to the base plane, while CE = CF = CG = r. Applying the theorem on the square of the hypotenuse to each of the three right triangles with vertex C gives

AE² = AF² = AG² = AC² + r² = (2t)² + 2t² = 6t².

The expansion (2t)² = 4t² follows from II.4. Thus all six edges are equal: the constructed pyramid has four equilateral triangular faces. [13.12, D11.3, D1.15, 1.47, 2.4, CN1]

**Step 7.** Let s be any edge of the pyramid. We have proved s² = 6t². Since the sphere’s diameter is AB = 3t, successive application of II.4 gives AB² = 9t². Therefore

AB² = (3/2)s².

Hence an equilateral triangular pyramid has been constructed and comprehended in the given sphere, and the square on the sphere’s diameter is one and a half times the square on the side of the pyramid, as required. [2.4]

**USED:** 1.1, 1.11, 1.47, 1.5, 1.6, 11.12, 11.2, 11.4, 13.12, 2.4, 2.5, 4.2, 6.9, CN1, CN3, D1.15, D11.12, D11.14, D11.16, D11.17, D11.3, P1, P3
**Human refs (from References field):** 1.4, 11.12, 13.12, 3.1, 3.31, 4.2, 6.17, 6.8, D11.3
**Jaccard:** 0.143 — AI adds ['1.1', '1.11', '1.47', '1.5', '1.6', '11.2', '11.4', '2.4', '2.5', '6.9', 'CN1', 'CN3', 'D1.15', 'D11.12', 'D11.14', 'D11.16', 'D11.17', 'P1', 'P3']; Human adds ['1.4', '3.1', '3.31', '6.17', '6.8']

## Proposition 13.14
**Statement:** To construct an octahedron and comprehend it in a sphere, as in the preceding case; and to prove that the square on the diameter of the sphere is double of the square on the side of the octahedron.

**Step 1.** Let AC be the prescribed diameter of the sphere. We use the direct construction by three mutually perpendicular diameters. Bisect AC at O, and describe in a plane π the circle Γ with centre O and radius OA. Through O draw the perpendicular to AC in π, meeting Γ at B and D, so that A, B, C, D occur successively around the circle. Thus AC and BD are diameters, and OA = OB = OC = OD. [1.10, P3, 1.11, D1.15, D1.17]

**Step 2.** At O set up a straight line perpendicular to π. Produce it through O, and take E and F on its opposite sides such that OE = OF = OA. Join consecutive vertices of ABCD, and join each of E and F to each of A, B, C, D. Since EF is perpendicular to π, each of OE and OF makes a right angle with every equatorial radius OA, OB, OC, OD. [11.12, P2, 1.3, P1, D11.3]

**Step 3.** Consider the twelve triangles OAB, OBC, OCD, ODA, OEA, OEB, OEC, OED, OFA, OFB, OFC, OFD. In each, the two sides issuing from O equal OA, and their included angle is right. Consequently their opposite sides are all equal by side–angle–side. This is the natural criterion here because the equal radii and included right angles are already available. Hence
AB = BC = CD = DA = EA = EB = EC = ED = FA = FB = FC = FD. [P4, 1.4]

**Step 4.** Since AC and BD are diameters of Γ, all four angles of ABCD are angles in semicircles and therefore right. Together with the equality of its sides, this makes ABCD a square. The four triangles EAB, EBC, ECD, EDA form the boundary above this square, and FAB, FBC, FCD, FDA form the boundary below it; together they enclose a solid, with their common square base internal. Every one of these eight boundary triangles is equilateral by Step 3. Moreover, any two have their three sides respectively equal, so their corresponding angles are equal, and side–angle–side then gives equality of the triangles themselves. The solid is therefore contained by eight equal equilateral triangles: it is an octahedron. [3.31, D1.22, D1.20, 1.8, 1.4, D11.26]

**Step 5.** In the plane through AC and EF, describe the circle with centre O and radius OA. Its diameter is EF, and A lies on its circumference. Rotate the semicircle EAF about EF. By the definition of a sphere, this generates a sphere with centre O. The endpoints E and F remain on its surface, while A traces precisely Γ, the circle in π with centre O and radius OA. Thus A, B, C, D also lie on the spherical surface, and the sphere comprehends the constructed octahedron. Its diameter EF equals the prescribed AC, since
EF = EO + OF = AO + OC = AC. [P3, D1.18, D11.14, D11.16, D11.17, CN2]

**Step 6.** The angle ABC is right, being an angle in the semicircle on AC. Therefore the square on AC equals the sum of the squares on AB and BC. But AB = BC by Step 3, so the square on AC is double the square on AB. Since AC equals the sphere’s diameter and AB is a side of the octahedron, the square on the diameter of the sphere is double the square on the side of the octahedron. The required construction and proof are complete. [3.31, 1.47]

**USED:** 1.10, 1.11, 1.3, 1.4, 1.47, 1.8, 11.12, 3.31, CN2, D1.15, D1.17, D1.18, D1.20, D1.22, D11.14, D11.16, D11.17, D11.26, D11.3, P1, P2, P3, P4
**Human refs (from References field):** 1.4, 1.47, 11.12, 3.31
**Jaccard:** 0.174 — AI adds ['1.10', '1.11', '1.3', '1.8', 'CN2', 'D1.15', 'D1.17', 'D1.18', 'D1.20', 'D1.22', 'D11.14', 'D11.16', 'D11.17', 'D11.26', 'D11.3', 'P1', 'P2', 'P3', 'P4']

## Proposition 13.15
**Statement:** To construct a cube and comprehend it in a sphere, like the pyramid; and to prove that the square on the diameter of the sphere is triple of the square on the side of the cube.

**Step 1.** Let d be the prescribed diameter of the sphere. We first determine the cube’s edge by a mean proportional, since this directly constructs a square equal to one third of the square on d. Cut off t equal to one third of d, and construct a mean proportional s between d and t. Thus d:s = s:t, and the square on s equals the rectangle contained by d and t. Dividing the square on d into three such rectangles gives

d² = 3s².
[6.9, 6.13, 6.17, 2.1]

**Step 2.** Construct the square ABCD with side s. At A, B, C, and D erect perpendiculars to its plane, all on the same side. Extend them as necessary and cut off AA′ = BB′ = CC′ = DD′ = s. These four perpendiculars are parallel to one another. [1.46, 11.12, P2, 1.3, 11.6]

**Step 3.** Join A′B′, B′C′, C′D′, and D′A′. Since AA′ and BB′ are equal and parallel, AB and A′B′ are equal and parallel; the same reasoning applies to the other three pairs of corresponding edges. Consequently ABB′A′, BCC′B′, CDD′C′, and DAA′D′ are parallelograms whose sides all equal s. Each has right angles at its base, because the erected edges are perpendicular to the base plane; its remaining angles are right by the properties of parallel lines. Thus these four faces are squares. [P1, 1.33, D11.3, 1.29, D1.22]

**Step 4.** The opposite sides of ABCD are parallel, since its angles are right. Therefore, using the parallels established above, A′B′ and D′C′ are parallel. They consequently lie in one plane containing all four upper vertices. The angles of A′B′C′D′ equal the corresponding angles of ABCD, because their respective sides are parallel. Hence the upper face is also a square of side s. [1.28, 11.9, D1.23, 11.10, D1.22]

All six faces are equal: dividing each square by a diagonal gives two triangles having sides s, s and the included right angle, so the triangles, and therefore the squares, are equal. The constructed solid is consequently a cube. [1.4, CN2, D11.25]

**Step 5.** Join the face diagonals AC and BD and the four body diagonals AC′, BD′, CA′, and DB′. By the right-angled triangles in the base,

AC² = BD² = 2s².

Since CC′ is perpendicular to the base plane, triangle ACC′ is right-angled at C. Thus

AC′² = AC² + CC′² = 2s² + s² = 3s² = d².

The identical calculation, using the appropriate base diagonal and erected edge, applies to BD′, CA′, and DB′. Hence all four body diagonals have length d. [P1, D11.3, 1.47]

**Step 6.** To locate their common midpoint, use XI.38, which applies directly to the cube just constructed. Bisect the four sides of each of the opposite faces ABCD and A′B′C′D′. Carry one plane through the midpoints of AB, CD, A′B′, and C′D′, and another through the midpoints of BC, DA, B′C′, and D′A′. Let MN be their common section within the cube. [1.10]

Apply XI.38 to these same planes and each body diagonal: MN and that diagonal bisect one another. Thus all four body diagonals have the same midpoint O, namely the midpoint of MN. Since each diagonal has length d, the distances from O to all eight vertices are equal to d/2. [11.38]

**Step 7.** In the plane ACC′A′ describe the circle with centre O and radius OA, and take a semicircle with diameter AC′. Rotate this semicircle about AC′. It generates a sphere with centre O. [P3, D11.14, D11.16]

Every vertex lies on this sphere. Indeed, each is at distance OA from O; the plane through that vertex and the axis AC′ is a position of the rotating semicircle, whose circular boundary has precisely that radius. Thus the generated surface passes through all eight vertices, and the cube is comprehended in the sphere. [D1.15, D11.14]

The segment AC′ passes through O and terminates on the sphere, so it is a diameter. Its length is d, and Step 5 gives AC′² = 3s². Therefore the cube has been constructed and comprehended in a sphere of the prescribed diameter, and the square on that diameter is triple the square on the side of the cube. [D11.17, 1.47]

**USED:** 1.10, 1.28, 1.29, 1.3, 1.33, 1.4, 1.46, 1.47, 11.10, 11.12, 11.38, 11.6, 11.9, 2.1, 6.13, 6.17, 6.9, CN2, D1.15, D1.22, D1.23, D11.14, D11.16, D11.17, D11.25, D11.3, P1, P2, P3
**Human refs (from References field):** 1.47, D11.3
**Jaccard:** 0.069 — AI adds ['1.10', '1.28', '1.29', '1.3', '1.33', '1.4', '1.46', '11.10', '11.12', '11.38', '11.6', '11.9', '2.1', '6.13', '6.17', '6.9', 'CN2', 'D1.15', 'D1.22', 'D1.23', 'D11.14', 'D11.16', 'D11.17', 'D11.25', 'P1', 'P2', 'P3']

## Proposition 13.16
**Statement:** To construct an icosahedron and comprehend it in a sphere, like the aforesaid figures; and to prove that the side of the icosahedron is the irrational straight line called minor.

**Step 1.** Let D be the diameter of the required sphere, and take D as the assigned rational straight line for the irrationality assertion [D10.1.3]. Cut off D/5, and construct a mean proportional r between D and D/5 [6.9, 6.13]. Then
r² = D²/5,
by the relation between a mean proportional and the rectangle contained by its extremes [6.17]. Squares below denote the squares on the corresponding straight lines.

**Step 2.** Describe a circle with centre O and radius r, and inscribe a regular pentagon A₀A₁A₂A₃A₄ in it [P3, 4.11]. Let its side be a. Indices throughout are taken modulo five. Bisect each successive arc AᵢAᵢ₊₁ at Cᵢ [3.30]. Since equal chords cut off equal arcs, the ten points A₀,C₀,A₁,C₁,…,A₄,C₄ divide the circumference into ten equal arcs [3.28]. Consequently they form a regular decagon; write t for its side. Thus AᵢCᵢ = CᵢAᵢ₊₁ = t. Moreover, each arc CᵢCᵢ₊₁ equals an arc AᵢAᵢ₊₁, so CᵢCᵢ₊₁ = a [3.29].

**Step 3.** The side of a regular hexagon inscribed in this circle is r. Indeed, construct the hexagon by 4.15. Its equal arcs give six equal central angles [3.28, 3.27]; its isosceles central triangles therefore have all three angles equal, and hence are equilateral [1.5, 1.32, 1.6]. Applying 13.10 to our pentagon now gives
(1)  a² = r² + t².
This suggests the direct construction: two staggered pentagons separated by r, whose joining edges have perpendicular components r and t.

**Step 4.** By 13.9, the sum r+t is cut in extreme and mean ratio, with greater segment r and lesser segment t. Therefore 13.3 gives
(2)  (t+r/2)² = 5(r/2)² = D²/4.
Put h = t+r/2. Since lengths are positive, 2h = D. Here 13.3 is the directly applicable identity: the distance needed for each axial pole is the lesser segment plus half the greater.

**Step 5.** Erect OO′ perpendicular to the plane of the circle and make OO′ = r [11.12, P3]. Through each Cᵢ draw a parallel to OO′ and mark Bᵢ on the same side of the original plane, with CᵢBᵢ = r [1.31, P3]. Equal parallel displacements give
O′Bᵢ = OCᵢ = r,
BᵢBᵢ₊₁ = CᵢCᵢ₊₁ = a,
with the corresponding joins parallel [1.33]. Hence B₀,…,B₄ form the congruent pentagon in the plane through O′ parallel to the original plane [11.15]. The lifting lines are perpendicular to the original plane [11.8]. Also OO′ is perpendicular to the upper plane: it is perpendicular to two intersecting lines in that plane parallel to lines through O in the original plane [1.29, 11.4]. Thus the two pentagons have perpendicular separation r, and the projections of the upper vertices are precisely the intervening arc-midpoints Cᵢ.

**Step 6.** Produce the axis beyond O away from O′ to S, and beyond O′ away from O to T, taking OS = O′T = t [P2, P3]. Join S to every Aᵢ, T to every Bᵢ, and each Bᵢ to Aᵢ and Aᵢ₊₁ [P1]. Perpendicularity to the planes supplies the right angles in the following triangles [D11.3]. By 1.47,
AᵢBᵢ² = AᵢCᵢ² + CᵢBᵢ² = t²+r² = a²,
and likewise Aᵢ₊₁Bᵢ² = a². Also
SAᵢ² = SO² + OAᵢ² = t²+r² = a²,
TBᵢ² = TO′² + O′Bᵢ² = t²+r² = a².
Thus every joining edge, as well as every side of either pentagon, equals a, by (1).

**Step 7.** Take the following four families of triangular faces, each containing five triangles:
S Aᵢ Aᵢ₊₁;
Aᵢ Aᵢ₊₁ Bᵢ;
Aᵢ₊₁ Bᵢ Bᵢ₊₁;
T Bᵢ Bᵢ₊₁.
The middle ten form a nonintersecting belt between the pentagons. To see this explicitly, intersect the belt with any plane strictly between and parallel to their planes. Its section is a closed ten-sided polygon, with sides alternately parallel to the sides of the two pentagons [11.16]. In their cyclic order these directions turn successively through one-tenth of a full turn, always in the same sense; hence the section is a convex decagon. The belt therefore has no crossings. The first and last five triangles form the two caps, lying on opposite sides outside the slab, and close its two boundary pentagons. Consequently these twenty triangles enclose a solid.
By Step 6 each triangle is equilateral of side a. They are equal triangles, since their corresponding sides and included angles are equal [1.5, 1.32, 1.4]. The solid is therefore an icosahedron, according to the definition of a solid contained by twenty equal equilateral triangles [D11.27].

**Step 8.** Bisect OO′ at M [1.10]. Then
MS = MT = r/2+t = h = D/2.
For every lower vertex, the right triangle MOAᵢ gives
MAᵢ² = MO²+OAᵢ² = r²/4+r² = 5r²/4 = D²/4.
The upper right triangles MO′Bᵢ give the same result for MBᵢ [1.47]. Thus all twelve vertices S,T,A₀,…,A₄,B₀,…,B₄ are at distance D/2 from M. The sphere generated by rotating the semicircle with diameter ST has centre M and diameter D, and all these vertices lie on its surface [D11.14, D11.16, D11.17]. Hence the constructed icosahedron is comprehended in a sphere of the prescribed diameter.

**Step 9.** The diameter of the original pentagon's circle is 2r, and
(2r)² = 4D²/5.
The squares on 2r and D therefore have the common measure D²/5. Thus 2r is commensurable in square with the assigned rational line D, and is itself rational [D10.1.2, D10.1.3]. Proposition 13.11 now applies directly to the original inscribed pentagon: its side a is the irrational straight line called minor. Since a is also the side of the constructed icosahedron, the required construction, comprehension in the sphere, and classification of its side are complete.

**USED:** 1.10, 1.29, 1.31, 1.32, 1.33, 1.4, 1.47, 1.5, 1.6, 11.12, 11.15, 11.16, 11.4, 11.8, 13.10, 13.11, 13.3, 13.9, 3.27, 3.28, 3.29, 3.30, 4.11, 4.15, 6.13, 6.17, 6.9, D10.1.2, D10.1.3, D11.14, D11.16, D11.17, D11.27, D11.3, P1, P2, P3
**Human refs (from References field):** 1.33, 11.6, 13.10, 13.11, 13.3, 13.9, 3.31, 4.15, 6.8, D5.9
**Jaccard:** 0.146 — AI adds ['1.10', '1.29', '1.31', '1.32', '1.4', '1.47', '1.5', '1.6', '11.12', '11.15', '11.16', '11.4', '11.8', '3.27', '3.28', '3.29', '3.30', '4.11', '6.13', '6.17', '6.9', 'D10.1.2', 'D10.1.3', 'D11.14', 'D11.16', 'D11.17', 'D11.27', 'D11.3', 'P1', 'P2', 'P3']; Human adds ['11.6', '3.31', '6.8', 'D5.9']

## Proposition 13.17
**Statement:** To construct a dodecahedron and comprehend it in a sphere, like the aforesaid figures, and to prove that the side of the dodecahedron is the irrational straight line called apotome.

**Step 1.** Let D be the diameter of the given sphere, and take D as the assigned rational straight line. Choose the cube construction: it will make the required dodecahedral edge a golden-section segment of the cube’s edge, so that the apotome conclusion follows directly. By [13.15], construct a cube with edge s such that D² = 3s². Cut s in extreme and mean ratio by [6.30]. Bisect s and its greater segment, writing them respectively as 2a and 2b; thus 0 < b < a. Put c = a + b. These bisections are supplied by [1.10]. The choice of rational reference is that of [D10.1.3].

**Step 2.** By the definition of extreme and mean ratio and the invariance of a ratio under equal multiplication,
a : b = b : (a − b).
Since c = a + b, [13.5] gives
c : a = a : b,
and therefore bc = a² by [6.16]. Apply the golden-section square identity [13.4] first to a, whose greater segment is b, and then to c, whose greater segment is a. We obtain
(1) a² + (a − b)² = 3b²,
(2) c² + b² = 3a².
Also c − a = b and c − b = a. These are the identities needed below. [D6.3, 5.15, 13.5, 6.16, 13.4]

**Step 3.** At the centre O of the sphere choose three mutually perpendicular directions, using [1.11] and [11.12]. A triple (x,y,z) will denote signed perpendicular offsets in these directions; this is only notation for constructed lengths. Copy lengths and draw parallels by [1.2] and [1.31] to construct the following twenty points, with the signs independent:
• eight points (±a, ±a, ±a);
• four points (0, ±b, ±c);
• four points (±b, ±c, 0);
• four points (±c, 0, ±b).
The first eight are the vertices of a cube of edge 2a. For any two listed points, the square of their distance is the sum of the squares of the differences of their three offsets, by applying [1.47] twice.

**Step 4.** Attach a roof to each of the cube’s six faces. For the face z = a, its ridge is the segment joining (0,−b,c) to (0,b,c). The roof is filled by the straight joins between this ridge and the square base. Its boundary, apart from the base, consists of two triangular ends and two trapezoidal sides. The trapezoids are planar because their opposite sides lie on parallel straight lines. [11.2, 11.7]

For clarity, at proportional height t above the base, where 0 ≤ t ≤ 1, the roof’s section is the rectangle
z = a + tb,
|x| ≤ a(1 − t),
|y| ≤ a(1 − t) + bt.
These proportional sections follow from [6.2]. In particular, the roof lies in the outward prism over its base square, since both half-widths are at most a.

Use the analogous ridge on z = −a. On the faces y = ±a use the ridges joining (−b,±c,0) to (b,±c,0); on x = ±a use those joining (±c,0,−b) to (±c,0,b). Thus the ridge directions are chosen cyclically. The six roofs have disjoint interiors, since they lie in the respective outward face-prisms. Added to the cube, they form a solid whose exterior consists of twelve triangular and twelve trapezoidal panels.

**Step 5.** We show that these panels join in pairs into twelve plane pentagons. Consider
P = (0,b,c), Q = (a,a,a), R = (b,c,0), S = (−b,c,0), T = (−a,a,a).
The roof on z = a supplies triangle PQT, while the roof on y = a supplies trapezoid QRST. Their common side QT is an edge of the cube.

The plane through the parallel lines QT and RS has the perpendicular-offset equation
ay + bz = ac.
Indeed, in the section x = 0 its line joins (y,z) = (a,a) to (c,0), and the displayed relation is precisely the proportional-intercept relation of [6.2]. Parallel lines in the x-direction fill the same plane. [11.7]

The point P also belongs to this plane, since
ab + bc = ab + a² = ac.
Hence PQT and QRST are coplanar. They lie on opposite sides of QT: P has z = c > a, while R and S have z = 0 < a. Their union is the pentagon PQRST. Its outline is convex: P has greatest z, RS has least z, and Q and T are respectively its extreme positive and negative x-points.

At every cube edge the cyclic ridge choice similarly places one triangular panel beside one trapezoidal panel. Sign changes and cyclic permutation of the three directions repeat the preceding calculation at all twelve cube edges. Thus all twenty-four exterior panels pair into exactly twelve plane pentagons. Their planes are the twelve distinct planes ±ay ±bz = ac and their cyclic variants. [6.2, 11.7]

**Step 6.** Compute the sides and diagonals of PQRST by [1.47]. For four of its sides the squared length, with the terms possibly reordered, is
a² + (a − b)² + b² = 4b²
by identity (1); the remaining side RS is visibly 2b. Therefore all five sides equal 2b.

The diagonal QT is 2a. Each of the other four diagonals has squared length
c² + b² + a² = 4a²
by identity (2). For example,
PR² = b² + (c − b)² + c² = b² + a² + c²,
and
QS² = (a + b)² + (a − c)² + a² = c² + b² + a².
Consequently every diagonal is 2a. [1.47, 13.4]

**Step 7.** At each vertex of this convex pentagon, the two adjacent sides and the straight line joining their other endpoints form a triangle with sides 2b, 2b, 2a. By [1.8], all five interior angles are equal. Thus PQRST is equilateral and equiangular.

The sign changes and cyclic permutations used for the other eleven pentagons preserve all the lengths just computed. Triangulating corresponding pentagons therefore gives corresponding triangles with equal sides; [1.8] gives their equal included angles, and [1.4] gives equality of the triangles. Hence the twelve pentagons are equal as well as equilateral and equiangular. The constructed solid is therefore a dodecahedron by [D11.28].

**Step 8.** Every cube vertex has squared distance 3a² from O. Every added vertex has squared distance b² + c² = 3a², by identity (2). Since
D² = 3(2a)²,
we have 3a² = (D/2)². Thus all twenty vertices lie on the given sphere. [1.47, 13.4, D11.14, D11.16]

The sphere also contains the solid itself. A plane through O and a straight join cuts the sphere in a circle; chords lie inside that circle by [3.2]. Extending the joining line to the circumference gives the same conclusion when its endpoints are already inside. Hence every straight join filling the cube and its six roofs stays inside the sphere. The dodecahedron is therefore comprehended in the given sphere. [11.2, D11.14, 3.2]

**Step 9.** Finally, D² = 3s² shows that s is commensurable in square with the assigned rational diameter D. Hence s is rational in Euclid’s sense. [D10.1.2, D10.1.3] The dodecahedron’s edge is 2b, which by Step 1 is exactly the greater segment obtained by cutting s in extreme and mean ratio. By [13.6], this segment is the irrational straight line called apotome.

Thus a dodecahedron has been constructed and comprehended in the given sphere, and its side has been proved to be an apotome.

**USED:** 1.10, 1.11, 1.2, 1.31, 1.4, 1.47, 1.8, 11.12, 11.2, 11.7, 13.15, 13.4, 13.5, 13.6, 3.2, 5.15, 6.16, 6.2, 6.30, D10.1.2, D10.1.3, D11.14, D11.16, D11.28, D6.3
**Human refs (from References field):** 1.47, 1.8, 11.1, 11.38, 11.6, 13.15, 13.4, 13.5, 13.6, 13.7, 5.15, 6.32
**Jaccard:** 0.233 — AI adds ['1.10', '1.11', '1.2', '1.31', '1.4', '11.12', '11.2', '11.7', '3.2', '6.16', '6.2', '6.30', 'D10.1.2', 'D10.1.3', 'D11.14', 'D11.16', 'D11.28', 'D6.3']; Human adds ['11.1', '11.38', '11.6', '13.7', '6.32']

## Proposition 13.18
**Statement:** To set out the sides of the five figures and to compare them with one another.

**Step 1.** Let the given sphere have diameter AB, of length L. We use comparison of squares, since the diameter relations already established for the first three figures directly determine their sides; for the remaining two figures we obtain the needed relations from diametral sections. Write x² for the square on a segment x, and xy for the rectangle contained by x and y.

Draw a semicircle on AB. Bisect AB at M, and take C on AB with AC one third of AB. The perpendiculars at C and M meet the semicircle at P and Q respectively. Set t = BP, o = AQ, and c = AP. These constructions are available by P3, I.10, VI.9, and I.11. [P3, 1.10, 6.9, 1.11]

**Step 2.** The angles APB and AQB are right. Similarity of the triangles formed by their perpendiculars to AB gives
AP² = AB·AC, BP² = AB·BC, and AQ² = AB·AM.
Consequently,
3c² = L², 3t² = 2L², and 2o² = L².
By the diameter relations of XIII.13, XIII.14, and XIII.15, t, o, and c are respectively the sides of the pyramid, octahedron, and cube inscribed in the given sphere. [3.31, 6.8, 6.4, 6.17, 13.13, 13.14, 13.15]

**Step 3.** Take the fifth part of L and construct its mean proportional with L; call this mean r. Thus 5r² = L². In a circle of radius r inscribe an equilateral and equiangular pentagon, and call its side i. Also cut c in extreme and mean ratio, and call its greater segment d. We shall show that i and d are respectively the required icosahedral and dodecahedral sides. [6.9, 6.13, 6.17, P3, 4.11, 6.30, D6.3]

**Step 4.** For these two identifications, consider a vertex U on the sphere and any collection of vertices V at the same distance s from U. Let UW be the diameter through U, and drop VH perpendicular to UW. The section through U, W, V is a circle with diameter UW, so UVW is a right angle. Similar triangles give UW:UV = UV:UH, and therefore
L·UH = s².
Thus the foot H is the same for every such V. Their perpendiculars to UW lie in one plane, and, by the right-triangle theorem, all the lengths HV are equal. The vertices V therefore lie on a circle in that plane. If its radius is ρ and UH = h, we have
s² = ρ² + h² = Lh.
This is the diametral-section relation we need. [D11.14, D11.16, 1.12, 3.31, 6.8, 6.4, 6.17, 11.5, 1.47]

**Step 5.** Take the icosahedron constructed in XIII.16, and denote its side by e. The five neighbours of one vertex form an equilateral pentagon of side e. By Step 4 they lie on a circle; denote its radius by ρ and its decagon side by q. The hexagon side is ρ, as in the hexagon construction. XIII.9 and XIII.10 give
ρ² = q(ρ + q), with ρ > q,
and e² = ρ² + q².
Comparing the latter equality with e² = ρ² + h² from Step 4 gives h = q. Hence
Lq = e² = ρ² + q² = q(ρ + 2q),
so L = ρ + 2q. [13.16, 4.15, 13.9, 13.10, 1.47, 6.17]

**Step 6.** By XIII.9, the line ρ + q is cut in extreme and mean ratio with greater segment ρ. XIII.3 therefore gives
(q + ρ/2)² = 5(ρ/2)²,
and hence (ρ + 2q)² = 5ρ². Since L = ρ + 2q, we obtain L² = 5ρ². But L² = 5r² by construction, so ρ = r. Equilateral pentagons in equal circles have equal sides: their equal chords divide their circumferences into five equal arcs, and equal arcs have equal chords. Thus e = i, identifying the icosahedral side. [13.9, 13.3, 3.28, 3.29]

**Step 7.** Take the dodecahedron constructed in XIII.17. Let its side be a and a diagonal of one of its pentagonal faces be f. By XIII.8, f is cut in extreme and mean ratio with greater segment a. Put v = f − a. Then
a² = fv and f² + v² = 3a²,
the second equality being XIII.4.

At a vertex U, the three adjacent vertices are pairwise separated by face diagonals f, and so form an equilateral triangle. Let the radius of its circle be ρ. XIII.12 gives f² = 3ρ². Applying Step 4 with s = a gives
a² = ρ² + h² = Lh.
It follows that
3h² = 3a² − f² = v²,
while Lh = a² = fv. [13.17, 13.8, D6.3, 6.17, 13.4, 13.12, 1.47]

**Step 8.** From Lh = fv we have L:f = v:h. Squares have the duplicate ratio of their sides; since v² = 3h², it follows that L² = 3f². Step 2 gives L² = 3c², so f = c. Thus a is the greater segment of c cut in extreme and mean ratio, and therefore a = d.

This segment is unique: enlarging it increases its square while decreasing the rectangle contained by the whole and the remainder, whereas those two areas must be equal. The dodecahedral side has therefore also been identified. [6.16, 6.20, D6.3, 6.17, CN5]

**Step 9.** The relations in Step 2 give
t² = 2c² and o² = (3/2)c².
Therefore t² > o² > c², and hence t > o > c. Here and below, the order of squares is the order of their positive sides. [6.20, CN5]

**Step 10.** In the circle of radius r, let q be the decagon side. By XIII.9,
r² = q(r + q) > 2q²,
because r > q. By XIII.10, i² = r² + q². Consequently,
i² < (3/2)r² < (5/3)r² = c²,
where the last equality follows from 5r² = L² = 3c². Thus c > i. [4.15, 13.9, 13.10, 6.20, CN5]

Now put u = c − d. Since d is the greater segment, u < d. XIII.4 gives c² + u² = 3d², and therefore c² > 2d². Hence
d² < c²/2 = (5/6)r² < r² < i².
Thus i > d. [D6.3, 13.4, 13.10, 6.20, CN5]

**Step 11.** Transfer the five constructed segments to a common starting point if desired. They are the sides of the five figures inscribed in the same sphere, and their order is
pyramid side > octahedron side > cube side > icosahedron side > dodecahedron side.
Thus the sides of the five figures have been set out and compared with one another. [1.2]

**USED:** 1.10, 1.11, 1.12, 1.2, 1.47, 11.5, 13.10, 13.12, 13.13, 13.14, 13.15, 13.16, 13.17, 13.3, 13.4, 13.8, 13.9, 3.28, 3.29, 3.31, 4.11, 4.15, 6.13, 6.16, 6.17, 6.20, 6.30, 6.4, 6.8, 6.9, CN5, D11.14, D11.16, D6.3, P3
**Human refs (from References field):** 13.10, 13.13, 13.14, 13.15, 13.16, 13.17, 13.9, 4.15, 6.20, 6.4, 6.8, D5.9
**Jaccard:** 0.306 — AI adds ['1.10', '1.11', '1.12', '1.2', '1.47', '11.5', '13.12', '13.3', '13.4', '13.8', '3.28', '3.29', '3.31', '4.11', '6.13', '6.16', '6.17', '6.30', '6.9', 'CN5', 'D11.14', 'D11.16', 'D6.3', 'P3']; Human adds ['D5.9']
