# Book 13 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 13.1
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half.

**Step 1.** Let AB be cut at C in extreme and mean ratio, with AC the greater segment. Write w = AB, a = AC, and b = CB, so w = a + b. Bisect AB and denote its half by h; thus w = h + h. This bisection is supplied by 1.10. Write S(x) for the square on a length x, and R(x,y) for the rectangle contained by lengths x and y.

**Step 2.** By the definition of extreme and mean ratio, w : a = a : b (D6.3). Apply 6.17, which directly concerns these three proportional straight lines, to obtain
S(a) = R(w,b).

**Step 3.** We use 2.4 because the side of the required square is the sum a + h. It gives
S(a+h) = S(a) + S(h) + 2R(a,h).
Since w consists of two halves equal to h, 2.1 gives R(w,a) = 2R(a,h). Therefore
S(a+h) = S(a) + R(w,a) + S(h).
[2.4, 2.1, CN1]

**Step 4.** Substitute the equality from Step 2. Since w is cut into a and b, 2.2 gives R(w,a) + R(w,b) = S(w). Consequently,
S(a+h) = R(w,b) + R(w,a) + S(h) = S(w) + S(h).
[2.2, CN2, CN1]

**Step 5.** Apply 2.4 to the whole w cut into its two equal halves h. The rectangle contained by h and h is the square on h, so
S(w) = S(h) + S(h) + 2S(h) = 4S(h).
[2.4]

**Step 6.** Adding S(h) to this equality and using Step 4 gives
S(a+h) = 4S(h) + S(h) = 5S(h).
Thus the square on the greater segment added to half the whole is five times the square on half the whole, as required. [CN2, CN1]

**USED:** 1.10, 2.1, 2.2, 2.4, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 6.1, 6.17, D6.3
**Jaccard:** 0.222 — AI adds ['1.10', '2.1', '2.2', '2.4', 'CN1', 'CN2']; Human adds ['6.1']

## Proposition 13.2
**Statement:** If the square on a straight line be five times the square on a segment of it, then, when the double of the said segment is cut in extreme and mean ratio, the greater segment is the remaining part of the original straight line.

**Step 1.** Let the original straight line have length a, the specified segment length b, and the remaining part length r. Thus a=b+r, and by hypothesis a²=5b². Consider the prescribed division of a line of length 2b in extreme and mean ratio, and let its greater segment have length x. Its half has length b, so XIII.1 gives (x+b)²=5b². This is the direct route: XIII.1 supplies exactly the fivefold square appearing in the hypothesis. [13.1]

**Step 2.** Since a² and (x+b)² are both equal to 5b², they are equal to one another. [CN1]

**Step 3.** Therefore a=x+b. For if either of these two lengths exceeded the other by a positive length d, II.4 would make the square on the longer equal to the square on the shorter together with the square on d and twice the rectangle contained by the shorter and d. The square on the longer would consequently be greater, contrary to Step 2. [2.4, CN5]

**Step 4.** Subtract b from the equal lengths a and x+b. The remainders are equal; since a−b=r, we obtain r=x. Thus the greater segment of the double of the specified segment, when cut in extreme and mean ratio, is the remaining part of the original straight line, as required. [CN3]

**USED:** 13.1, 2.4, CN1, CN3, CN5
**Human refs (from References field):** 6.1
**Jaccard:** 0.000 — AI adds ['13.1', '2.4', 'CN1', 'CN3', 'CN5']; Human adds ['6.1']

## Proposition 13.3
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the lesser segment added to the half of the greater segment is five times the square on the half of the greater segment.

**Step 1.** Let AB be cut in extreme and mean ratio at C, with AC the greater segment and CB the lesser. Bisect AC at D, so that AD = DC and the points occur in the order A, D, C, B. Thus DB is the lesser segment CB added to half the greater segment. Write S(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW. [1.10]

**Step 2.** By the definition of extreme and mean ratio, AB : AC = AC : CB. Hence the rectangle contained by the extremes equals the square on the mean:
R(AB, CB) = S(AC).
The three-proportional-lines theorem applies directly to the defining proportion. [D6.3, 6.17]

**Step 3.** Use the bisected-line identity directly, since its half-plus-added segment is precisely DB. The line AC is bisected at D and CB is added to it in a straight line; therefore
R(AB, CB) + S(DC) = S(DB). [2.6]

**Step 4.** Applying the square-of-a-divided-line identity to AC gives
S(AC) = S(AD) + S(DC) + 2R(AD, DC).
Since AD = DC, each square on the right equals S(DC), and R(AD, DC) is also the square on a length equal to DC. Consequently,
S(AC) = 4S(DC). [2.4]

**Step 5.** Adding S(DC) to the equality in Step 2 and using Steps 3 and 4 yields
S(DB) = S(AC) + S(DC) = 4S(DC) + S(DC) = 5S(DC).
Since DB is CB added to half of AC, the square on the lesser segment added to half the greater segment is five times the square on half the greater segment, as required. [CN2, CN1]

**USED:** 1.10, 2.4, 2.6, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.10', '2.4', '2.6', '6.17', 'CN1', 'CN2', 'D6.3']

## Proposition 13.4
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.

**Step 1.** Let AB be cut at C in extreme and mean ratio, with AC the greater segment and CB the lesser. By definition, AB : AC = AC : CB. Write S(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW. [D6.3]

**Step 2.** Use the three-proportional theorem directly, since AC is the mean between AB and CB. The rectangle contained by the extremes equals the square on the mean; hence R(AB, CB) = S(AC). [6.17]

**Step 3.** Apply the whole-and-segment identity to AB, choosing the lesser segment CB because this gives exactly the sum required in the proposition. Thus
S(AB) + S(CB) = 2R(AB, CB) + S(AC). [2.7]

**Step 4.** Adding the equality of Step 2 to itself, and then adding S(AC) to both sides, gives
2R(AB, CB) + S(AC) = 3S(AC). [CN2]
Combining this with Step 3 yields S(AB) + S(CB) = 3S(AC). Therefore the square on the whole and the square on the lesser segment together are triple the square on the greater segment. [CN1]

**USED:** 2.7, 6.17, CN1, CN2, D6.3
**Human refs (from References field):** 6.17, D6.3
**Jaccard:** 0.400 — AI adds ['2.7', 'CN1', 'CN2']

## Proposition 13.5
**Statement:** If a straight line be cut in extreme and mean ratio, and there be added to it a straight line equal to the greater segment, the whole straight line has been cut in extreme and mean ratio, and the original straight line is the greater segment.

**Step 1.** Let AB be cut at C in extreme and mean ratio, with AC the greater segment. Let the added straight line BD lie beyond B and equal AC, so that AD is the augmented line. By the definition of extreme and mean ratio,
AB : AC = AC : CB. [D6.3]

**Step 2.** Use the rule for summing antecedents and consequents directly, since these sums give the augmented line and the original line. Applied to the proportion in Step 1, it gives
(AB + AC) : (AC + CB) = AB : AC. [5.12]

**Step 3.** Since AC = BD, adding AB gives AB + AC = AB + BD = AD. Also AC + CB = AB. Substituting these equal lengths into the preceding proportion, and replacing AC by BD, yields
AD : AB = AB : BD. [CN2]

**Step 4.** The whole AB is greater than its part AC; since AC = BD, we have AB > BD. Thus the proportion in Step 3 says that the whole AD is to its greater segment AB as AB is to its lesser segment BD. Therefore AD is cut at B in extreme and mean ratio, and the original straight line AB is the greater segment. [CN5, D6.3]

**USED:** 5.12, CN2, CN5, D6.3
**Human refs (from References field):** 5.14, 6.17, D6.3
**Jaccard:** 0.167 — AI adds ['5.12', 'CN2', 'CN5']; Human adds ['5.14', '6.17']

## Proposition 13.6
**Statement:** If a rational straight line be cut in extreme and mean ratio, each of the segments is the irrational straight line called apotome.

**Step 1.** Let the rational straight line have length L, and let its greater and lesser segments in extreme and mean ratio have lengths a and b. Thus L = a + b. Bisect L, and write h = L/2. Set s = a + h and t = 3h. Here sums denote concatenated lengths, and x² denotes the square on length x. [1.10]

**Step 2.** The direct choice is XIII.1, because it uses half the given rational whole rather than half an as-yet-unclassified segment. It gives
s² = 5h².
Also, since squares have the duplicate ratio of their corresponding sides,
L² = 4h² and t² = 9h². [13.1; 6.20]

**Step 3.** The area h² therefore measures each of L², s², and t². Consequently h, s, and t are all commensurable in square with L, and s is commensurable in square with both h and t. Since L is rational, its square is commensurable with the square on the assigned rational straight line. Transitivity of commensurability shows that the same holds for the squares on h, s, and t; hence all three straight lines are rational. [D10.1.2; 10.12; D10.1.3]

**Step 4.** The ratio s²:h² is 5:1, which is not a ratio of a square number to a square number. Therefore s and h are incommensurable in length. But h measures t three times, so h and t are commensurable in length. It follows that s and t are likewise incommensurable in length. Together with Step 3, this proves that s and h, and also t and s, are commensurable in square only. [10.9; D10.1.1; 10.13]

**Step 5.** Since s = a + h, the greater segment is a = s − h. Thus it is the remainder when the rational straight line h is subtracted from the rational straight line s, the two being commensurable in square only. Therefore a is irrational and is an apotome. [10.73]

**Step 6.** Likewise,
t − s = 3h − (a + h) = 2h − a = L − a = b.
Since b is positive, this subtracts the lesser rational straight line s from the greater rational straight line t. These are commensurable in square only, so b too is irrational and is an apotome. Hence each segment of the rational straight line cut in extreme and mean ratio is the irrational straight line called apotome. [10.73]

**USED:** 1.10, 10.12, 10.13, 10.73, 10.9, 13.1, 6.20, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 10.97, 13.1, 6.17, D10.1.4, D6.3
**Jaccard:** 0.200 — AI adds ['1.10', '10.12', '10.13', '6.20', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.6', '10.97', '6.17', 'D10.1.4', 'D6.3']

## Proposition 13.7
**Statement:** If three angles of an equilateral pentagon, taken either in order or not in order, be equal, the pentagon will be equiangular.

**Step 1.** Let ABCDE be the given equilateral pentagon, with vertices in boundary order, and write AB = BC = CD = DE = EA = s. Up to cyclic relabelling and reversal, the three selected equal angles occur either at A, B, C or at A, C, D. We treat these two arrangements separately. Side-angle-side is the natural first comparison, since equal adjacent sides and their included angles are given. All diagonals used below are joined by [P1].

**Step 2.** First suppose the angles at A, B, C are equal, each being α. The triangles EAB, ABC, BCD have their two sides of length s and their included angles equal. Hence their bases are equal:
BE = AC = BD = d.
Their base angles are also all equal; denote each by β. In particular,
∠AEB = ∠CDB = ∠BCA = β. [1.4, 1.5, CN1]

**Step 3.** Since BE = BD, the base angles ∠BED and ∠BDE are equal. Adding the equal angles ∠AEB and ∠CDB shows that the pentagon’s angles at E and D are equal; denote each by δ. Put u = ∠ACD and v = ∠BDE. The diagonals divide the angles at C and D so that
α = β + u,   δ = β + v. [1.5, CN2]

**Step 4.** We now compare α and δ by [1.24], since each required triangle comparison already has two corresponding sides equal.

If α > δ, then u > v. In triangles ACD and BDE, AC = BD and CD = DE; therefore u > v gives AD > BE = d. But in triangles ABC and AED, AB = AE and BC = ED, while their included angles are α and δ. Thus α > δ gives AC > AD, or d > AD—a contradiction.

If α < δ, the same two comparisons give respectively AD < BE = d and AC < AD, or d < AD—again a contradiction.

Consequently α = δ. Thus all five angles are equal in the consecutive arrangement. [1.24, CN1]

**Step 5.** Now suppose the three equal angles are at A, C, D, each being α. The triangles EAB, BCD, CDE have two corresponding sides of length s and equal included angles. Therefore
BE = BD = CE,
and all their base angles are equal; call each β. In particular,
∠AEB = ∠CDB = ∠ABE = ∠ECD = β. [1.4, 1.5, CN1]

**Step 6.** In triangle BDE, BE = BD, so ∠BED = ∠BDE. Consequently
∠DEA = ∠BED + ∠BEA
= ∠BDE + ∠CDB
= ∠CDE = α.
Thus the angle at E equals the given angle at D. [1.5, CN2, CN1]

**Step 7.** In triangle BEC, BE = CE, so ∠EBC = ∠BCE. Hence
∠ABC = ∠ABE + ∠EBC
= ∠ECD + ∠BCE
= ∠BCD = α.
Thus the angle at B also equals α. Together with Step 6 and the three given equal angles, this proves that all five angles are equal in the nonconsecutive arrangement as well. The two possible arrangements are exhausted; therefore the equilateral pentagon is equiangular. [1.5, CN2, CN1]

**USED:** 1.24, 1.4, 1.5, CN1, CN2, P1
**Human refs (from References field):** 1.4, 1.5, 1.6, 1.8
**Jaccard:** 0.250 — AI adds ['1.24', 'CN1', 'CN2', 'P1']; Human adds ['1.6', '1.8']

## Proposition 13.8
**Statement:** If in an equilateral and equiangular pentagon straight lines subtend two angles taken in order, they cut one another in extreme and mean ratio, and their greater segments are equal to the side of the pentagon.

**Step 1.** Let ABCDE be the equilateral and equiangular pentagon, with its vertices in order. The straight lines subtending two consecutive angles may be named AC and BD; let their interior intersection be F. We use the direct angle-and-similarity route. Join AD. The triangles ABC, ACD, and ADE divide the pentagon, so its interior angles together equal six right angles. Let u be one fifth of two right angles. Each interior angle of the pentagon is therefore 3u, while the angles of any triangle sum to 5u. [P1, 1.32]

**Step 2.** Since AB = BC and BC = CD, the triangles ABC and BCD are isosceles. Their vertex angles at B and C respectively are 3u, so their base angles are u:
∠BAC = ∠BCA = ∠CBD = ∠BDC = u.
Consequently,
∠ABF = ∠ABC − ∠CBD = 2u,
and
∠FCD = ∠BCD − ∠BCA = 2u. [1.5, 1.32]

**Step 3.** In triangle ABF, the angles at A and B are u and 2u, so the angle at F is 2u. The equal angles at B and F therefore give AF = AB. Similarly, in triangle CDF, the angles at C and D are 2u and u, so its angle at F is 2u; hence DF = CD. Thus AF and DF both equal the side of the pentagon. [1.32, 1.6]

**Step 4.** In triangle BCF, the angles at B and C are both u, so BF = CF. Moreover, in triangle ABF, the angle at B is 2u and exceeds the angle u at A; therefore AF > BF. It follows that AF > CF and, since DF = AF, that DF > BF. Thus AF and DF are indeed the greater segments of AC and BD respectively. [1.6, 1.19]

**Step 5.** The angles of triangle BFC, at B, F, C respectively, are u, 3u, u. Thus triangles ABC and BFC are equiangular in the indicated order. Applying the proportionality theorem for equiangular triangles—the direct theorem for the angle equalities just established—gives
AC : BC = BC : FC.
Likewise, triangles BCD and CFB are equiangular in the indicated order, giving
BD : CD = CB : FB.
Since AF = BC = CD = DF, these proportions become
AC : AF = AF : FC,
and
BD : DF = DF : FB. [1.32, 6.4]

**Step 6.** Each whole diagonal is therefore to its greater segment as that greater segment is to its lesser segment. By the definition of extreme and mean ratio, AC and BD cut one another in extreme and mean ratio; and their greater segments AF and DF are each equal to the side of the pentagon, as required. [D6.3]

**USED:** 1.19, 1.32, 1.5, 1.6, 6.4, D6.3, P1
**Human refs (from References field):** 1.32, 1.4, 1.5, 1.6, 3.28, 4.14, 5.14, 6.33, 6.4
**Jaccard:** 0.333 — AI adds ['1.19', 'D6.3', 'P1']; Human adds ['1.4', '3.28', '4.14', '5.14', '6.33']

## Proposition 13.9
**Statement:** If the side of the hexagon and that of the decagon inscribed in the same circle be added together, the whole straight line has been cut in extreme and mean ratio, and its greater segment is the side of the hexagon.

**Step 1.** Let O be the centre of the common circle, and let h and d denote the sides of its inscribed regular hexagon and decagon respectively. Write R for a right angle. Join O to the vertices of each polygon. All these radii are equal (D1.15). Within each polygon, the triangles formed by consecutive radii have their three sides respectively equal, so their angles at O are equal (1.8). These angles together make four right angles (1.13). Hence each central angle of the hexagon is 2R/3, and each central angle of the decagon is 2R/5.

**Step 2.** Let HK be a side of the hexagon. Since OH = OK, the base angles of triangle OHK are equal (1.5); their sum is 2R − 2R/3, so each is 2R/3 (1.32). Thus the triangle is equiangular, and HK = OH (1.6). Consequently the radius equals h. Now let AB be a side of the decagon. In triangle OAB, OA = OB = h and AB = d. Its angle at O is 2R/5, so each base angle is 4R/5 (1.5, 1.32).

**Step 3.** Bisect angle OAB by AC, meeting OB at C (1.9). Then ∠OAC = ∠CAB = 2R/5. Since ∠AOC also equals 2R/5, triangle AOC gives AC = OC (1.6). In triangle ABC, the angles at A and B are respectively 2R/5 and 4R/5; therefore the angle at C is 4R/5 (1.32). Hence AC = AB (1.6). Thus OC = AC = AB = d.

**Step 4.** In triangle ABC, the angle at B is greater than the angle at A. Therefore AC > BC (1.19). Since AC = OC, it follows that OC > CB.

**Step 5.** Because AC bisects angle OAB, the angle-bisector theorem gives OC : CB = OA : AB (6.3). Substituting OA = OB and AB = OC yields OB : OC = OC : CB. Together with OC > CB, this says that OB has been cut at C in extreme and mean ratio, with OC its greater segment (D6.3).

**Step 6.** We now use 13.5 directly, since its hypothesis is exactly the subdivision just obtained: add to OB a straight line equal to its greater segment OC. The resulting whole is cut in extreme and mean ratio, and its greater segment is the original line OB (13.5). Since OB = h and OC = d, this whole is h + d, and (h + d) : h = h : d. Therefore the sum of the hexagon side and the decagon side is cut in extreme and mean ratio, with the hexagon side as its greater segment, as required.

**USED:** 1.13, 1.19, 1.32, 1.5, 1.6, 1.8, 1.9, 13.5, 6.3, D1.15, D6.3
**Human refs (from References field):** 1.32, 1.5, 4.15, 6.33, 6.4
**Jaccard:** 0.143 — AI adds ['1.13', '1.19', '1.6', '1.8', '1.9', '13.5', '6.3', 'D1.15', 'D6.3']; Human adds ['4.15', '6.33', '6.4']

## Proposition 13.10
**Statement:** If an equilateral pentagon be inscribed in a circle, the square on the side of the pentagon is equal to the squares on the side of the hexagon and on that of the decagon inscribed in the same circle.

**Step 1.** Let ABCDE be the given equilateral pentagon, O the centre of its circle, r the radius, and p = AB. Equal chords cut off equal arcs, so the five consecutive arcs are equal. Bisect arc AB at F. Bisecting all five arcs gives ten equal arcs and therefore equal chords; thus d = AF is the side of the inscribed decagon. The central angles AOF and FOB are each 36°. All radii are equal. [D1.15, 3.28, 3.30, 3.29, 3.27]

**Step 2.** The side of the inscribed equilateral hexagon equals r. Indeed, its six equal arcs give central angles of 60°. Each triangle formed by a hexagon side and the two radii to its endpoints is isosceles; its remaining angles are consequently also 60°, and its three sides are equal. It therefore suffices to prove p² = r² + d². [3.28, 3.27, 1.5, 1.32, 1.6]

**Step 3.** Let OF meet AB at H. Triangles OAH and OBH have OA = OB, OH common, and equal included angles. Hence AH = HB and their adjacent angles at H are equal, so both are right angles. Thus AB = 2AH and AH is perpendicular to OF. [1.4, D1.10]

**Step 4.** In the isosceles triangle OAF, the angle at O is 36°, so the angles OAF and AFO are each 72°. Bisect angle OAF by AP, meeting OF at P. Then angle OAP = angle AOP = 36°, whence OP = AP. Also angle PAF = 36° and angle AFP = 72°, so angle APF = 72° and AP = AF. Consequently OP = AP = AF = d. [1.5, 1.32, 1.9, 1.6]

**Step 5.** Apply the right-triangle square theorem to AHP and AHF. Since AP = AF and AH is common, subtraction gives HP² = HF², hence HP = HF. As P and F are distinct points on the line through H, H is the midpoint of PF. Therefore
2OH = 2OP + PF = OP + OF = d + r.
Thus the two legs of the right triangle OHA satisfy 2AH = p and 2OH = r + d. [1.47, CN3, CN2]

**Step 6.** By XIII.9, the sum r + d of the hexagon and decagon sides is cut in extreme and mean ratio, with greater segment r and lesser segment d. We use XIII.4 directly here because its square identity concerns exactly this whole and these two segments. It gives
(r + d)² + d² = 3r². [13.9, 13.4]

**Step 7.** In the right triangle OHA,
AH² + OH² = OA² = r².
The square on twice a segment is four times the square on that segment. Multiplying the preceding equality by four and using Step 5 therefore gives
p² + (r + d)² = 4r². [1.47, 2.4, CN2]

**Step 8.** Add d² to the equality in Step 7 and substitute the equality from Step 6:
p² + 3r² = 4r² + d².
Subtracting 3r² yields p² = r² + d². Since p, r, and d are respectively the pentagon, hexagon, and decagon sides in the same circle, the square on the pentagon side equals the squares on the hexagon and decagon sides together. [CN2, CN3]

**USED:** 1.32, 1.4, 1.47, 1.5, 1.6, 1.9, 13.4, 13.9, 2.4, 3.27, 3.28, 3.29, 3.30, CN2, CN3, D1.10, D1.15
**Human refs (from References field):** 1.26, 1.32, 1.4, 1.5, 2.2, 3.26, 4.15, 6.17, 6.33, 6.4
**Jaccard:** 0.125 — AI adds ['1.47', '1.6', '1.9', '13.4', '13.9', '2.4', '3.27', '3.28', '3.29', '3.30', 'CN2', 'CN3', 'D1.10', 'D1.15']; Human adds ['1.26', '2.2', '3.26', '4.15', '6.17', '6.33', '6.4']

## Proposition 13.11
**Statement:** If in a circle which has its diameter rational an equilateral pentagon be inscribed, the side of the pentagon is the irrational straight line called minor.

**Step 1.** Let D be the rational diameter of the given circle, and p the side of its inscribed equilateral pentagon. Inscribe a regular hexagon and denote its side by r [4.15]. Its six central angles are equal, since the radii are equal and the six corresponding chords are equal [D1.15, 1.8]. These angles together make four right angles [1.13]. Thus each central angle is one-third of two right angles. Each corresponding isosceles triangle consequently has all three angles equal [1.5, 1.32], and therefore all three sides equal [1.6]. Hence r is the radius, so r = D/2 and is rational [D10.1.3].

**Step 2.** Let d be the side of the regular decagon inscribed in the same circle. The line r + d is cut in extreme and mean ratio, with r its greater segment [13.9]. Put h = r/2 and t = d + h. Proposition 13.3 applies directly to the lesser segment together with half the greater segment, and gives
 t² = 5h².
This is the direct route we use: express p² as the rectangle contained by a rational line and a fourth apotome.

**Step 3.** Expanding the square on t = d + h gives
 d² + 2dh + h² = 5h²,
so, since r = 2h,
 d² + rd = r²
[2.4]. Also, the square on the pentagon side equals the squares on the hexagon and decagon sides together [13.10]. Consequently,
 p² = r² + d² = 2r² − rd = r(2r − d),
where the last equality is the distributive relation for rectangles [2.1].

**Step 4.** Set a = 5h and q = a − t. Because r is the greater segment in Step 2, d < r; therefore
 q = 5h − (d + h) = 2r − d > 0.
Moreover,
 a² = 25h²,   t² = 5h²,   r² = 4h².
Thus a and t are rational straight lines and are commensurable in square: their squares and the square on the rational line r are measured by h² [D10.1.2, D10.1.3].

**Step 5.** The ratio a²:t² is 25:5. This cannot be the ratio of a square number to a square number: otherwise, since 25 is square, 5 would also be square [8.24]. Hence a and t are incommensurable in length [10.9]. They are therefore rational straight lines commensurable in square only, and their difference q = a − t is an apotome [10.73].

**Step 6.** The difference between the squares on the whole a and its annex t is
 a² − t² = 20h² = (2t)².
Now a²:(2t)² = 25:20. Since 25 is square and 20 is not, this is not a ratio of square numbers [8.24]; therefore a and 2t are incommensurable in length [10.9]. On the other hand, a:r = 5:2, so the whole a is commensurable in length with the rational line r. Accordingly, taking r as the rational straight line set out, q is a fourth apotome [D10.3.4].

**Step 7.** Steps 3 and 4 give p² = rq. Thus the square on p is the rectangle contained by the rational straight line r and the fourth apotome q. The side of such an area is minor [10.94]. Therefore the side of the inscribed equilateral pentagon is the irrational straight line called minor, as required.

**USED:** 1.13, 1.32, 1.5, 1.6, 1.8, 10.73, 10.9, 10.94, 13.10, 13.3, 13.9, 2.1, 2.4, 4.15, 8.24, D1.15, D10.1.2, D10.1.3, D10.3.4
**Human refs (from References field):** 1.32, 10.12, 10.15, 10.73, 10.9, 10.94, 13.1, 13.8, 5.18, 5.19, D10.3.4
**Jaccard:** 0.200 — AI adds ['1.13', '1.5', '1.6', '1.8', '13.10', '13.3', '13.9', '2.1', '2.4', '4.15', '8.24', 'D1.15', 'D10.1.2', 'D10.1.3']; Human adds ['10.12', '10.15', '13.1', '13.8', '5.18', '5.19']

## Proposition 13.12
**Statement:** If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.

**Step 1.** Let ABC be an equilateral triangle inscribed in the given circle, and let q denote a right angle. Since AB = BC = CA, the angles of ABC are equal; their sum is 2q, so each is 2q/3. [D1.20, 1.5, 1.32]

**Step 2.** Find the centre O. Draw AO and produce it through O to meet the circle again at D; join BD and BO. We choose this diameter route because it directly supplies a right triangle for the square calculation. Write r for the radius. Then AO = BO = OD = r, and AD = 2r. [3.1, P1, P2, D1.15, D1.17]

**Step 3.** D is neither B nor C: otherwise the angle at the third vertex of ABC would be an angle in a semicircle and therefore right, contrary to Step 1. Since AD is a diameter, ∠ABD = q, and consequently ∠ADB is acute. The angle ∠ACB is also acute. Thus C and D both lie in the greater segment bounded by chord AB. Use the same-segment theorem here, since it directly compares the two angles subtending AB: ∠ADB = ∠ACB = 2q/3. The angle sum in triangle ABD therefore gives ∠BAD = q/3. [3.31, 3.21, 1.32]

**Step 4.** Because OA = OB, triangle AOB has ∠ABO = ∠BAO. Since O lies on AD, ∠BAO = ∠BAD = q/3. Moreover, O lies between A and D, so BO lies inside ∠ABD. Hence ∠OBD = q − q/3 = 2q/3. But ∠BDO = ∠BDA = 2q/3. The equal angles in triangle BOD therefore give BD = BO = r. [D1.15, 1.5, 1.6]

**Step 5.** In the right-angled triangle ABD, the square on AD equals the squares on AB and BD:
AD² = AB² + BD². [1.47]
Since AD is divided at O into two equal radii, the square-on-a-divided-line identity gives
AD² = AO² + OD² + 2(AO·OD) = 4r². [2.4]
Substituting BD² = r² and subtracting that square yields AB² = 3r². Thus the square on the side of the inscribed equilateral triangle is triple the square on the radius of the circle. [CN3]

**USED:** 1.32, 1.47, 1.5, 1.6, 2.4, 3.1, 3.21, 3.31, CN3, D1.15, D1.17, D1.20, P1, P2
**Human refs (from References field):** 1.47, 3.31, 4.15
**Jaccard:** 0.133 — AI adds ['1.32', '1.5', '1.6', '2.4', '3.1', '3.21', 'CN3', 'D1.15', 'D1.17', 'D1.20', 'P1', 'P2']; Human adds ['4.15']

## Proposition 13.13
**Statement:** To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.

**Step 1.** Let the given sphere be generated by a semicircle with diameter AB and centre O. Thus A and B are on the sphere, O is its centre, and OA = OB. Cut off HB equal to one third of AB, so that AH = 2HB. Then H lies between O and B. Writing t = OH, we have HB = 2t, OA = OB = 3t, AH = 4t, and AB = 6t. [D11.14, D11.16, D11.17, D1.15, 6.9]

**Step 2.** In the plane of the generating semicircle, draw HC perpendicular to AB, meeting the semicircular circumference at C. At H erect HK perpendicular to that plane. Consequently HK is perpendicular to AB. Since AB is perpendicular to both HC and HK at their intersection H, it is perpendicular to the plane Π through those two lines. [1.11, 11.12, D11.3, 11.4]

**Step 3.** In Π describe the circle Γ with centre H and radius HC. As the generating semicircle turns about AB, C describes precisely this circle: its distance from H remains HC, and HC turns in the plane perpendicular to AB at H. Therefore every point of Γ lies on the given sphere. This perpendicular circular section will provide the base of the pyramid. [P3, D11.14]

**Step 4.** Write XY² for the area of the square on XY. Squares have the duplicate ratio of their sides, so the square on a length nt is n² times the square on t. Join OC. Since OC is a radius of the generating circle, OC = OA = 3t. The triangle OHC is right-angled at H; hence
OC² = OH² + HC²,
and therefore
HC² = 9t² − t² = 8t². [6.20, P1, D1.15, 1.47, CN3]

**Step 5.** Construct an equilateral triangle as a model; its angles are equal. In Γ inscribe a triangle EFG equiangular with that model. Its equal angles give equal sides, so EFG is equilateral. For its side–radius relation, use XIII.12 directly, since it supplies exactly the required equality without an auxiliary chord construction:
EF² = FG² = GE² = 3HC² = 24t². [1.1, 1.5, 4.2, 1.6, 13.12]

**Step 6.** Join A to E, F, and G, and join H to those three points. Since AB is perpendicular to Π, each of AHE, AHF, and AHG is right-angled at H. Also HE = HF = HG = HC, since these are radii of Γ. Consequently
AE² = AH² + HE² = 16t² + 8t² = 24t²,
and likewise AF² = AG² = 24t². Comparing with Step 5, and using the duplicate-ratio property of squares, all six edges AE, AF, AG, EF, FG, and GE are equal. [P1, D11.3, D1.15, 1.47, 6.20, CN2]

**Step 7.** The triangle EFG and the three triangles AEF, AFG, and AGE therefore bound a pyramid with four equilateral faces. Its vertex A lies outside the base plane, and all four vertices lie on the given sphere; thus the pyramid is comprehended in that sphere. If s denotes its common edge, then s² = 24t², whereas the square on the sphere’s diameter is
AB² = (6t)² = 36t² = (3/2)·24t² = (3/2)s².
Hence the required pyramid has been constructed in the given sphere, and the square on the sphere’s diameter is one and a half times the square on the side of the pyramid. [D11.12, D11.14, 6.20]

**USED:** 1.1, 1.11, 1.47, 1.5, 1.6, 11.12, 11.4, 13.12, 4.2, 6.20, 6.9, CN2, CN3, D1.15, D11.12, D11.14, D11.16, D11.17, D11.3, P1, P3
**Human refs (from References field):** 1.4, 11.12, 13.12, 3.1, 3.31, 4.2, 6.17, 6.8, D11.3
**Jaccard:** 0.154 — AI adds ['1.1', '1.11', '1.47', '1.5', '1.6', '11.4', '6.20', '6.9', 'CN2', 'CN3', 'D1.15', 'D11.12', 'D11.14', 'D11.16', 'D11.17', 'P1', 'P3']; Human adds ['1.4', '3.1', '3.31', '6.17', '6.8']

## Proposition 13.14
**Statement:** To construct an octahedron and comprehend it in a sphere, as in the preceding case; and to prove that the square on the diameter of the sphere is double of the square on the side of the octahedron.

**Step 1.** Let AC be the prescribed diameter of the sphere. Bisect AC at O. In a plane π containing AC, describe the circle Γ with centre O and radius OA. Through O draw a straight line perpendicular to AC, meeting Γ at B and D, so that A, B, C, D occur successively around Γ. Thus AC and BD are diameters, and OA = OB = OC = OD. [1.10, 1.11, P2, P3, D1.15, D1.17]

**Step 2.** At O set up a straight line perpendicular to π, and produce it in both directions. This line and AC lie in one plane. In that plane describe another circle with centre O and radius OA, meeting the perpendicular at E and F on opposite sides of π. Consequently OE = OF = OA, and all six segments OA, OB, OC, OD, OE, OF are equal. [11.12, P2, 11.2, P3, D1.15]

**Step 3.** Join AB, BC, CD, DA, and join each of E and F to each of A, B, C, D. We compare these edges directly by side–angle–side, since the construction supplies equal radii and included right angles. Indeed, the four triangles OAB, OBC, OCD, ODA and the eight triangles OEA, OEB, OEC, OED, OFA, OFB, OFC, OFD each have two sides equal to OA and their included angle right. They are therefore equal by I.4, and their bases—the twelve proposed edges of the octahedron—are all equal. [P1, D11.3, P4, 1.4, CN1]

**Step 4.** Each angle of ABCD stands in a semicircle of Γ: the angles at B and D subtend diameter AC, and those at A and C subtend diameter BD. Hence all four angles are right. Together with the equalities established in Step 3, this makes ABCD a square, with O inside it. Form the pyramids with common base ABCD and vertices E and F. They lie on opposite sides of π; their common base is internal to their union. Their union is therefore bounded by precisely the eight triangles EAB, EBC, ECD, EDA, FAB, FBC, FCD, FDA. [3.31, D1.22, D11.12]

**Step 5.** Each of these eight triangles is equilateral, since its three sides are among the equal edges of Step 3. Moreover, any two have their three corresponding sides equal: I.8 gives equal corresponding included angles, and I.4 then gives equality of the triangles themselves. Thus the solid is contained by eight equal and equilateral triangles, and is an octahedron. [D1.20, 1.8, 1.4, D11.26]

**Step 6.** In the circle constructed in Step 2, take the semicircle with diameter EF passing through A, and revolve it about EF. It generates a sphere with centre O. Because OA is perpendicular to EF, the point A describes exactly Γ during the revolution. Thus A, B, C, D lie on the generated spherical surface, while E and F remain on that surface as the fixed endpoints of the diameter. The sphere therefore comprehends the constructed octahedron. Since AC passes through O and has both endpoints on its surface, AC is a diameter of this sphere, as prescribed. [D11.14, D11.16, D11.17]

**Step 7.** The angle ABC is right, so the square on AC equals the sum of the squares on AB and BC. Since AB = BC, this sum is twice the square on AB. But AC is the diameter of the sphere and AB is a side of the octahedron. Therefore the square on the diameter of the sphere is double the square on the side of the octahedron. The required construction and proof are complete. [3.31, 1.47, CN2]

**USED:** 1.10, 1.11, 1.4, 1.47, 1.8, 11.12, 11.2, 3.31, CN1, CN2, D1.15, D1.17, D1.20, D1.22, D11.12, D11.14, D11.16, D11.17, D11.26, D11.3, P1, P2, P3, P4
**Human refs (from References field):** 1.4, 1.47, 11.12, 3.31
**Jaccard:** 0.167 — AI adds ['1.10', '1.11', '1.8', '11.2', 'CN1', 'CN2', 'D1.15', 'D1.17', 'D1.20', 'D1.22', 'D11.12', 'D11.14', 'D11.16', 'D11.17', 'D11.26', 'D11.3', 'P1', 'P2', 'P3', 'P4']

## Proposition 13.15
**Statement:** To construct a cube and comprehend it in a sphere, like the pyramid; and to prove that the square on the diameter of the sphere is triple of the square on the side of the cube.

**Step 1.** Let d be the prescribed diameter of the sphere. Cut off a third part t of d, and construct a mean proportional s between d and t. Then d:s = s:t, so the square on s equals the rectangle contained by d and t. Since d consists of three parts equal to t, the square on d is three times that rectangle. Thus

d² = 3s².

The mean-proportional construction is the direct choice here because it produces the required square as a rectangle. [6.9, 6.13, 6.17, 2.1]

**Step 2.** Construct the square ABCD with side s. At A, B, C, and D erect perpendiculars to its plane, and on the same side of that plane take AE = BF = CG = DH = s. These perpendiculars are parallel to one another. Join EF, FG, GH, and HE. Since equal and parallel segments have their corresponding endpoints joined by equal and parallel segments, we obtain

EF ∥ AB, FG ∥ BC, GH ∥ CD, HE ∥ DA,

and every upper edge has length s. [1.46, 11.12, 1.3, 11.6, P1, 1.33]

**Step 3.** Verify that the constructed solid is a cube. Each lateral quadrilateral ABFE, BCGF, CDHG, and DAEH is a parallelogram. Its two angles at the lower face are right angles, because its upright edges are perpendicular to the plane ABCD; its opposite angles are equal, so all four angles are right angles. Its four sides have length s. Hence each lateral face is a square. [D11.3, 1.34, D1.22]

The opposite upper edges are parallel by the theorem on lines parallel to the same straight line. In particular, EF and GH lie in one plane, which contains E, F, G, and H. Each angle of EFGH equals the corresponding angle of ABCD, since their sides are respectively parallel and point in corresponding directions. Thus EFGH also is a square of side s. The solid is therefore contained by six equal squares and is a cube. [11.9, D1.23, 11.10, D1.22, D11.25]

**Step 4.** Join AC and AG. The triangle ABC is right-angled at B, and the triangle ACG is right-angled at C, since CG is perpendicular to the plane ABCD. Therefore

AC² = AB² + BC² = 2s²,

AG² = AC² + CG² = 3s² = d².

The same argument, using the appropriate lower-face diagonal and upright edge, gives

BH² = CE² = DF² = 3s².

Consequently all four body diagonals AG, BH, CE, and DF have length d. [P1, D11.3, 1.47]

**Step 5.** To locate the centre, use the cube-bisection theorem directly, since its hypothesis is precisely the cube just constructed. Bisect the sides of the opposite faces ABCD and EFGH. Carry one plane through the midpoints of AB, CD, EF, and GH, and another through the midpoints of BC, DA, FG, and HE. Let MN be the segment of their common section between the two opposite faces, and bisect MN at O. [1.10, 11.38]

By the cube-bisection theorem, MN and a body diagonal bisect one another. Applying it to each of AG, BH, CE, and DF, with the same two midpoint planes, shows that O is the midpoint of every body diagonal. Since those diagonals all have length d,

OA = OB = OC = OD = OE = OF = OG = OH = d/2. [11.38]

**Step 6.** In a plane through AG describe the circle with centre O and radius OA. Since O bisects AG, AG is a diameter of this circle. Rotate a semicircle on AG about AG: it generates a sphere with centre O and diameter AG = d. Its surface consists of the points at distance OA from O; hence all eight vertices of the cube lie on that surface. The constructed cube is therefore comprehended in a sphere of the prescribed diameter. [P3, D1.15, D11.14, D11.16, D11.17]

Finally, Step 4 gives AG² = 3AB². Thus the square on the diameter of the sphere is triple the square on the side of the cube, as required. [1.47]

**USED:** 1.10, 1.3, 1.33, 1.34, 1.46, 1.47, 11.10, 11.12, 11.38, 11.6, 11.9, 2.1, 6.13, 6.17, 6.9, D1.15, D1.22, D1.23, D11.14, D11.16, D11.17, D11.25, D11.3, P1, P3
**Human refs (from References field):** 1.47, D11.3
**Jaccard:** 0.080 — AI adds ['1.10', '1.3', '1.33', '1.34', '1.46', '11.10', '11.12', '11.38', '11.6', '11.9', '2.1', '6.13', '6.17', '6.9', 'D1.15', 'D1.22', 'D1.23', 'D11.14', 'D11.16', 'D11.17', 'D11.25', 'P1', 'P3']

## Proposition 13.16
**Statement:** To construct an icosahedron and comprehend it in a sphere, like the aforesaid figures; and to prove that the side of the icosahedron is the irrational straight line called minor.

**Step 1.** Let the given sphere have centre O and diameter D. For the assertion about irrationality, take D as the assigned rational straight line (D10.1.3). Cut off a fifth of D and construct r as the mean proportional between D and that fifth. Then
r² = D²/5.
Put h = r/2. In a plane through O describe the circle Γ with centre O and radius r. These constructions are justified by 6.9, 6.13, 6.17, and P3.

**Step 2.** Inscribe in Γ an equilateral and equiangular pentagon X₀X₁X₂X₃X₄ (4.11). Its five smaller intervening arcs are equal (3.28). Bisect each of them, calling the midpoint of the arc XᵢXᵢ₊₁ by Yᵢ; throughout, subscripts are taken modulo five (3.30). Thus the ten points occur alternately as X₀, Y₀, X₁, Y₁, and so on, and divide the circle into ten equal arcs. Their successive chords consequently have a common length t, the side of the inscribed regular decagon. The Yᵢ also form an equilateral pentagon whose side equals the side s of the X-pentagon. The corresponding central angles are equal as well (3.29, 3.27).

**Step 3.** The side of a regular hexagon inscribed in Γ equals r. Indeed, construct that hexagon by 4.15 and join its vertices to O. The six isosceles central triangles have equal central angles by 1.8; hence each central angle is one-third of two right angles. By 1.5 and 1.32, each base angle has that same magnitude. Their sides are therefore equal by 1.6, so each hexagon side equals its radius r.

**Step 4.** By 13.9, the straight line r + t is cut in extreme and mean ratio, with greater segment r and lesser segment t. For the required height, 13.3 is the direct choice, since this is exactly its hypothesis. It gives
(t + h)² = 5h² = D²/4,
and therefore
D/2 = t + h.
Moreover, applying 13.10 to Γ gives
s² = r² + t².
These are the two relations needed for the construction.

**Step 5.** Set up perpendiculars to the plane of Γ at O and at its ten marked points (11.12). These perpendiculars are parallel (11.6). Choose one side of the plane as upper. On the perpendicular through Xᵢ take Aᵢ at distance h above the plane; on that through Yᵢ take Bᵢ at distance h below it. Equal displacements along parallel lines preserve the lengths and parallelism of the joining segments (1.33). Thus the Aᵢ and Bᵢ form two equilateral pentagons of side s in parallel planes, separated by 2h = r; the parallelism of the planes follows from 11.15. On the perpendicular through O take N and S, respectively above and below O, with ON = OS = D/2.

**Step 6.** Join N to all the Aᵢ, S to all the Bᵢ, and each Bᵢ to Aᵢ and Aᵢ₊₁. The right angles used below follow from the original perpendiculars and parallel displacement (1.29).

The horizontal separation between N and Aᵢ is r, while their vertical separation is D/2 − h = t. Hence, by 1.47 and Step 4,
NAᵢ² = r² + t² = s².
Likewise SBᵢ = s.

The projections of Aᵢ and Bᵢ on the original plane are adjacent decagon vertices, as are the projections of Aᵢ₊₁ and Bᵢ. Each projected separation is therefore t, while the vertical separation is 2h = r. Again by 1.47,
AᵢBᵢ² = Aᵢ₊₁Bᵢ² = t² + r² = s².
Together with the sides of the two pentagons, every segment designated as an edge thus has length s.

**Step 7.** The ten triangles
AᵢAᵢ₊₁Bᵢ and Aᵢ₊₁BᵢBᵢ₊₁
form the lateral boundary between the two pentagons. To verify that they fit without crossing, consider the plane of AᵢAᵢ₊₁Bᵢ. It cuts the upper pentagonal plane along its side AᵢAᵢ₊₁, and the lower plane along the parallel line through Bᵢ (11.16). Because Yᵢ bisects the arc XᵢXᵢ₊₁, its radius bisects the corresponding chord, by congruence of the central half-triangles, and is perpendicular to it (1.4, 3.3). Consequently the lower intersection line is perpendicular to the radius of the lower circumcircle at Bᵢ and lies outside that circle (3.16). Thus the face plane supports both pentagons, all their remaining vertices being on its inward side. The identical argument with upper and lower interchanged applies to the other five lateral triangles.

These supporting triangles therefore form a non-self-intersecting belt: each connecting edge belongs to two adjacent triangles, and its boundary consists exactly of the two pentagons. Close the upper boundary with the five triangles NAᵢAᵢ₊₁ and the lower boundary with the five triangles SBᵢBᵢ₊₁. These two caps lie on opposite sides outside the intervening slab, so they introduce no intersections. The resulting closed solid has exactly twenty triangular faces.

**Step 8.** By Step 6, every one of these twenty faces is equilateral with side s. They are also equal triangles, by 1.8 followed by 1.4. The constructed solid is therefore an icosahedron, according to D11.27.

**Step 9.** For every upper or lower pentagonal vertex, the perpendicular to the original plane supplies a right triangle with legs r and h. Therefore, by 1.47,
OAᵢ² = OBᵢ² = r² + h² = 5r²/4 = D²/4.
Also ON = OS = D/2 by construction. All twelve vertices consequently lie on the sphere with centre O and diameter D, which is the given sphere (D11.14). Thus the constructed icosahedron is comprehended in that sphere.

**Step 10.** The diameter of Γ is 2r. Since
D² = 5r² and (2r)² = 4r²,
the squares on D and 2r have the common measure r². Hence 2r is commensurable in square with the assigned rational line D and is itself rational (D10.1.2, D10.1.3). The common edge s is already the side of the equilateral pentagon inscribed in Γ, so 13.11 applies directly: s is the irrational straight line called minor.

Therefore an icosahedron has been constructed and comprehended in the given sphere, and its side has been proved to be minor.

**USED:** 1.29, 1.32, 1.33, 1.4, 1.47, 1.5, 1.6, 1.8, 11.12, 11.15, 11.16, 11.6, 13.10, 13.11, 13.3, 13.9, 3.16, 3.27, 3.28, 3.29, 3.3, 3.30, 4.11, 4.15, 6.13, 6.17, 6.9, D10.1.2, D10.1.3, D11.14, D11.27, P3
**Human refs (from References field):** 1.33, 11.6, 13.10, 13.11, 13.3, 13.9, 3.31, 4.15, 6.8, D5.9
**Jaccard:** 0.200 — AI adds ['1.29', '1.32', '1.4', '1.47', '1.5', '1.6', '1.8', '11.12', '11.15', '11.16', '3.16', '3.27', '3.28', '3.29', '3.3', '3.30', '4.11', '6.13', '6.17', '6.9', 'D10.1.2', 'D10.1.3', 'D11.14', 'D11.27', 'P3']; Human adds ['3.31', '6.8', 'D5.9']

## Proposition 13.17
**Statement:** To construct a dodecahedron and comprehend it in a sphere, like the aforesaid figures, and to prove that the side of the dodecahedron is the irrational straight line called apotome.

**Step 1.** Use an inscribed cube as the scaffold: its side is already related to the diameter of the sphere, and the construction below will make the required side a greater extreme-and-mean segment of that cube side. Let the given sphere have centre O and diameter d. Construct in it a cube of side 2a, bisecting its side to obtain a. Then

d² = 3(2a)² = 12a². [13.15, 1.10]

**Step 2.** Cut a in extreme and mean ratio, and let b be its greater segment. Write t = b/a and h = 1+t. The definition of the division and the equality of the corresponding rectangles give

b² = a(a−b), hence t²+t = 1.

Consequently

0 < t < 1,  th = 1,  h−t = 1,  h²+t² = 3,

and

1+t²+(1−t)² = 4t².

The division is constructible by VI.30; the first equality follows from VI.16, and the subsequent identities are expansions and combinations of rectangles and squares. [6.30, D6.3, 6.16, 2.1, 2.4]

**Step 3.** Use O as origin and the three mutually perpendicular directions of the cube’s edges as reference directions. In the triples below, each entry records a signed perpendicular offset in units of a. Thus the cube’s eight vertices are

(±1, ±1, ±1).

Construct twelve further points:

(0, ±t, ±h),  (±h, 0, ±t),  (±t, ±h, 0),

with the signs chosen independently. These are ordinary constructions using the lengths a, b, and a+b, transferred and joined by parallels. [1.2, 1.31]

For this notation, the square of the distance between two points is a² times the sum of the squares of their three coordinate differences: apply I.47 first in a reference plane and then in the perpendicular right triangle. The required perpendicularity to that plane follows from XI.4. [11.4, 1.47]

**Step 4.** Construct the plane through

A = (0,t,h),  B = (0,−t,h),  D = (h,0,t).

These three non-collinear points lie in a plane. The midpoint (0,0,h) of AB and D lie in the reference plane with second coordinate zero. Since h−t = 1 and 1/h = t, proportional intercepts show that the plane ABD has equation

tx+z = h.

Here the equation merely expresses the ratios of the perpendicular offsets. [11.2, 6.2]

By changing signs and cyclically permuting the reference directions, construct the twelve planes

±tx ± z = h,  ±ty ± x = h,  ±tz ± y = h,

where each displayed pair of signs is independent. Take the common portion K on the O-side of all twelve planes. Equivalently, K is described by

t|x|+|z| ≤ h,
t|y|+|x| ≤ h,
t|z|+|y| ≤ h.

It contains the original cube, because t+1 = h, and it is bounded, because these inequalities imply |x|, |y|, |z| ≤ h. It is convex: proportional division along a segment preserves each of the twelve linear inequalities when both endpoints satisfy it. Thus this construction gives a bounded solid containing O in its interior. [6.2]

**Step 5.** Determine its face in the plane tx+z = h. The first inequality forces x,z ≥ 0. Substituting z = h−tx into the other two gives

0 ≤ x ≤ h,
|y| ≤ (h−x)/t,
|y| ≤ t+t²x.

The two upper bounds for |y| are equal at x = 1, where both equal 1. The second displayed bound is the smaller for 0 ≤ x ≤ 1, and the first is the smaller for 1 ≤ x ≤ h. These are precisely the straight-line intercept relations obtained by proportional division, simplified using the identities of Step 2. [6.2, 2.1]

Therefore this face is exactly the convex pentagon, in boundary order,

A = (0,t,h),
B = (0,−t,h),
C = (1,−1,1),
D = (h,0,t),
E = (1,1,1).

The defining inequalities are unchanged by independent sign changes and cyclic permutation of the coordinates. Hence every one of the twelve bounding planes has the same pentagonal vertex pattern. Moreover, every boundary point must satisfy at least one of the twelve plane equations: if all inequalities are strict, sufficiently small displacements still satisfy them. Thus these twelve pentagons constitute the entire boundary, with no additional faces. Their vertices are precisely the eight cube vertices and the twelve points constructed in Step 3.

**Step 6.** Calculate the sides and diagonals of ABCDE by the repeated application of I.47 described in Step 3. We obtain

AB² = 4a²t²,

BC² = CD² = DE² = EA²
= a²[1+t²+(1−t)²]
= 4a²t².

Also,

AC² = AD² = BD² = BE²
= a²(1+h²+t²)
= 4a²,

and CE² = 4a². [1.47, 2.4]

Thus all five sides equal 2at = 2b, and all five diagonals equal 2a. The side-and-diagonal comparison is the direct route to equiangularity here, since these lengths are already known: at every vertex, the two adjacent sides and the diagonal joining their other endpoints form a triangle with sides 2b, 2b, 2a. Therefore all five interior angles are equal by I.8. [1.8]

The same calculations apply to every face. Dividing corresponding faces by two diagonals from corresponding vertices gives three pairs of triangles with respectively equal sides. I.8 gives equal included angles, and I.4 then gives equal triangles. Hence the twelve pentagons are equal, equilateral, and equiangular. Accordingly K is a dodecahedron, and its side is 2b. [1.8, 1.4, D11.28]

**Step 7.** Every cube vertex has squared distance 3a² from O. Each of the twelve added vertices has squared distance

a²(t²+h²) = 3a².

But the given sphere has radius squared d²/4 = 3a². Thus all twenty vertices lie on its surface. [1.47, 13.15, D11.14]

To verify that the whole solid is comprehended in the sphere, drop OF perpendicular to the plane of any face. For every vertex V of that face, I.47 gives

FV² = OV²−OF² = 3a²−OF².

Hence its five vertices lie on one circle centred at F. The convex pentagon lies within that circle, since its triangles are filled by chords lying within the circle. Consequently every point X of the face satisfies OX² ≤ 3a². [11.11, 1.47, 3.2]

Finally, every point of K is between O and a boundary point: continue its ray from O until it meets one of the bounding planes. Such radial segments remain inside the sphere. Therefore the entire dodecahedron is comprehended in the given sphere. [D11.14]

**Step 8.** Take d as the assigned rational straight line. Since d² = 3(2a)², the square on the cube side 2a is commensurable with the square on d. Thus 2a is rational in the sense of Book X. [D10.1.2, D10.1.3]

Let e = 2b be the dodecahedron’s side. From b² = a(a−b),

e² = (2a)(2a−e).

Also b is the greater segment of a, so e is greater than 2a−e. Therefore 2a has been cut in extreme and mean ratio with greater segment e. [6.16, D6.3]

Apply XIII.6 directly to this rational cube side: its greater segment e is the irrational straight line called apotome. Thus the dodecahedron has been constructed and comprehended in the given sphere, and its side has been proved to be an apotome. [13.6]

**USED:** 1.10, 1.2, 1.31, 1.4, 1.47, 1.8, 11.11, 11.2, 11.4, 13.15, 13.6, 2.1, 2.4, 3.2, 6.16, 6.2, 6.30, D10.1.2, D10.1.3, D11.14, D11.28, D6.3
**Human refs (from References field):** 1.47, 1.8, 11.1, 11.38, 11.6, 13.15, 13.4, 13.5, 13.6, 13.7, 5.15, 6.32
**Jaccard:** 0.133 — AI adds ['1.10', '1.2', '1.31', '1.4', '11.11', '11.2', '11.4', '2.1', '2.4', '3.2', '6.16', '6.2', '6.30', 'D10.1.2', 'D10.1.3', 'D11.14', 'D11.28', 'D6.3']; Human adds ['11.1', '11.38', '11.6', '13.4', '13.5', '13.7', '5.15', '6.32']

## Proposition 13.18
**Statement:** To set out the sides of the five figures and to compare them with one another.

**Step 1.** Let the given sphere have diameter D. Construct in this same sphere the regular pyramid (tetrahedron), octahedron, cube, icosahedron, and dodecahedron, using the five preceding constructions. Denote their respective sides by t, o, c, i, and d. Copy these five lengths from a common point onto one ray, using equal-length constructions and circles about that point. This sets out the five sides. We choose to compare them by plane sections of the already-constructed solids, without repeating their solid constructions or using their irrationality classifications. Below, x² denotes the square on x, and xy the rectangle contained by x and y. [13.13, 13.14, 13.15, 13.16, 13.17, 1.2, P3]

**Step 2.** The first three constructions give
D² = (3/2)t² = 2o² = 3c².
Thus t² = 2c² and o² = (3/2)c². Consequently t > o > c. It remains to place i and d below c in their proper order. [13.13, 13.14, 13.15, CN5]

**Step 3.** We establish the plane-section relations needed for the last two figures. Let V be a vertex, let V′ be the opposite endpoint of the sphere's diameter through V, and let W be any adjacent vertex, with VW = e. The central section through V and W is a circle with diameter VV′ = D, so angle VWV′ is right. Draw WH perpendicular to VV′. Similarity of the right triangles gives VW² = VV′·VH. Hence, writing VH = h and HW = r,
e² = Dh, and r² = e² − h².
Since every neighbor W is at the same distance e from V, its perpendicular foot is the same point H. Their perpendiculars to VV′ lie in one plane, and their lengths r are equal. The neighboring vertices therefore lie on a circle of centre H and radius r. [D11.14, 3.31, 1.12, 6.8, 6.17, 1.47, 11.5]

**Step 4.** Apply Step 3 at a five-triangle vertex of the icosahedron constructed in 13.16. Its five neighboring vertices, taken in order, form an equilateral pentagon of side i in the section circle. Let its radius be r, and let k be the side of the regular decagon in that circle. The side of the regular hexagon in the same circle is r: its six central triangles are congruent and isosceles, their equal central angles divide four right angles into six parts, and the triangle-angle theorem makes their remaining angles equal to their central angles; hence they are equilateral. [13.16, D11.27, 4.15, 1.8, 1.5, 1.32, 1.6]

**Step 5.** The circle now supplies exactly the sides occurring in 13.9 and 13.10, so these are the direct propositions to use. They give
i² = r² + k²,
and say that r + k is cut in extreme and mean ratio with greater segment r. Thus r > k and
r² = k(r + k).
But Step 3 gives i² = r² + h². Therefore h = k, and the other identity from that step becomes
i² = Dk. [13.10, 13.9, D6.3, 6.17, 1.47]

**Step 6.** Since r > k, the identity r² = rk + k² first gives r² > 2k². Also k² < rk, so r² < 2rk and therefore r < 2k. Substituting this last inequality into r² = rk + k² gives r² < 3k². Consequently
3k² < i² < 4k².
Since i² = Dk, cancellation of the common positive factor k gives 3k < D < 4k. Multiplication by D, followed by substitution of Dk = i², yields
3i² < D² < 4i².
Now D² = 3c², so c > i; and D² < 4i² gives i > D/2. Thus c > i > D/2. All these are comparisons of squares and rectangles, not numerical approximations. [13.9, 13.10, 6.17, 6.1, 13.15, CN5]

**Step 7.** Next take a vertex V of the dodecahedron constructed in 13.17, and its three neighboring vertices A, B, C. Each pair of its incident edges belongs to a regular pentagonal face. Accordingly AB, BC, and CA are equal diagonals of such faces; denote their common length by b. By the pentagon-diagonal theorem, each diagonal is cut in extreme and mean ratio with greater segment equal to the pentagon's side d. Therefore, putting y = b − d,
b = d + y, d > y > 0, and d² = by. [13.17, D11.28, 13.8, D6.3, 6.17]

**Step 8.** Because y < d, we have b < 2d. Hence
d² = by < 2dy,
so d < 2y. Thus y > d/2 and consequently b = d + y > 3d/2. [6.1, CN5]

**Step 9.** Apply Step 3 to this dodecahedral vertex, now with e = d. The neighboring vertices A, B, C form an equilateral triangle of side b in the circle of radius r. Therefore b² = 3r². Since b > 3d/2, it follows that r² > 3d²/4. The section identity h² = d² − r² consequently gives h² < d²/4, and therefore h < d/2. Finally d² = Dh, so D > 2d. Thus d < D/2 < i.
Combining this with Steps 2 and 6, the five sides already set out satisfy
 t > o > c > i > d.
Therefore, for the same circumscribing sphere, the side of the pyramid is greatest, followed in order by those of the octahedron, cube, icosahedron, and dodecahedron. The five sides have been set out and compared, as required. [13.12, 1.47, 6.1, CN5]

**USED:** 1.12, 1.2, 1.32, 1.47, 1.5, 1.6, 1.8, 11.5, 13.10, 13.12, 13.13, 13.14, 13.15, 13.16, 13.17, 13.8, 13.9, 3.31, 4.15, 6.1, 6.17, 6.8, CN5, D11.14, D11.27, D11.28, D6.3, P3
**Human refs (from References field):** 13.10, 13.13, 13.14, 13.15, 13.16, 13.17, 13.9, 4.15, 6.20, 6.4, 6.8, D5.9
**Jaccard:** 0.290 — AI adds ['1.12', '1.2', '1.32', '1.47', '1.5', '1.6', '1.8', '11.5', '13.12', '13.8', '3.31', '6.1', '6.17', 'CN5', 'D11.14', 'D11.27', 'D11.28', 'D6.3', 'P3']; Human adds ['6.20', '6.4', 'D5.9']
