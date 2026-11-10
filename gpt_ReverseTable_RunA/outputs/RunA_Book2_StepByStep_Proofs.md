# Book 2 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 2.1
**Statement:** If there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments.

**Step 1.** Let UV be the uncut straight line, and let the other straight line AB be divided, in order, at A = X₀, X₁, …, Xₙ = B. We choose a direct subdivision into rectangles, constructing the required pieces themselves. At A draw a perpendicular to AB; produce it sufficiently far and cut off AD equal to UV. [1.11, P2, 1.3]

**Step 2.** Through D draw a straight line parallel to AB. Through each Xᵢ, for i = 1, …, n, draw a straight line parallel to AD, meeting the parallel through D at Yᵢ. Put Y₀ = D and Yₙ = E. [1.31]

**Step 3.** The straight lines XᵢYᵢ are mutually parallel, since they are parallel to AD. Moreover, since AD is perpendicular to AB, the angle relations for parallel lines show that the angles formed by these lines with AB and DE are right angles. Thus ABED is a rectangle, as is every strip Xᵢ₋₁XᵢYᵢYᵢ₋₁. [1.30, 1.29]

**Step 4.** For each i ≥ 1, AXᵢYᵢD is a parallelogram, so its opposite sides XᵢYᵢ and AD are equal. Consequently every strip has its perpendicular side equal to AD, which was constructed equal to UV. [1.34]

**Step 5.** The whole rectangle ABED is therefore the rectangle contained by AB and UV. Likewise, each strip Xᵢ₋₁XᵢYᵢYᵢ₋₁ is the rectangle contained by the segment Xᵢ₋₁Xᵢ and UV: these are the lengths of its two sides containing a right angle. [D2.1]

**Step 6.** Because the division points occur successively on AB and the parallel dividing lines do not meet, the strips have no overlapping interiors and together fill exactly ABED. Their aggregate therefore coincides with, and is equal to, the whole rectangle. Substituting the identifications in Step 5, the rectangle contained by the two given straight lines equals all the rectangles contained by the uncut straight line and the several segments of the cut straight line, taken together. This is the required conclusion. [D1.23, CN4]

**USED:** 1.11, 1.29, 1.3, 1.30, 1.31, 1.34, CN4, D1.23, D2.1, P2
**Human refs (from References field):** 1.11, 1.3, 1.31, 1.34
**Jaccard:** 0.400 — AI adds ['1.29', '1.30', 'CN4', 'D1.23', 'D2.1', 'P2']

## Proposition 2.2
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and both of the segments is equal to the square on the whole.

**Step 1.** Let the straight line AB be cut at any point C between A and B. Describe the square ABDE on AB [1.46]. Its adjacent sides AE and AB are equal and contain a right angle [D1.22]; hence this square is the rectangle contained by AE and AB [D2.1].

**Step 2.** Use the direct specialization of Proposition 2.1, since it applies immediately to the cut line AB and the uncut line AE. It gives that the rectangle contained by AE and AB is equal to the rectangles contained by AE and AC, and by AE and CB, taken together [2.1].

**Step 3.** Since AE equals AB, the two latter rectangles are respectively the rectangles contained by AB and AC, and by AB and CB [D1.22, D2.1]. The rectangle contained by AE and AB is the square on AB, as established in Step 1. Therefore the rectangles contained by the whole AB and each of its two segments, taken together, are equal to the square on the whole AB [2.1]. This is the required conclusion.

**USED:** 1.46, 2.1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.200 — AI adds ['2.1', 'D1.22', 'D2.1']; Human adds ['1.31']

## Proposition 2.3
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and one of the segments is equal to the rectangle contained by the segments and the square on the aforesaid segment.

**Step 1.** Let the straight line AB be cut at an arbitrary point C, and let BC be the aforesaid segment. Denote by R(x,y) the rectangle contained by the straight lines x and y; the order of these two containing sides is immaterial. [D2.1]

**Step 2.** Use the two-segment case of Proposition 2.1 directly, since it already decomposes the required rectangle. Apply it to the straight lines BC and AB, with AB cut into AC and CB. It gives
R(AB,BC) = R(AC,BC) + R(BC,BC). [2.1]

**Step 3.** The square on BC is precisely the rectangle contained by BC and BC. Hence the preceding equality says that the rectangle contained by the whole AB and the segment BC equals the rectangle contained by the two segments AC and BC together with the square on BC. The chosen segment was arbitrary, so this proves the proposition. [D1.22, D2.1]

**USED:** 2.1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', 'D1.22', 'D2.1']; Human adds ['1.31', '1.46']

## Proposition 2.4
**Statement:** If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.

**Step 1.** Let AB be cut at any point C between A and B. Write S for the square on AB, X and Y for the squares on AC and CB, and R for the rectangle contained by AC and CB. Write U and V for the rectangles contained by AB and AC, and by AB and CB, respectively. Choose the square-specific decomposition, since it applies directly to the whole line and its two segments: S = U + V. Here addition denotes the sum of areas. [2.2]

**Step 2.** Apply the whole-by-segment identity to AB cut at C, first taking AC as the selected segment and then taking CB. It gives U = R + X and V = R + Y. The rectangle contained by the two segments is R in both applications. [2.3]

**Step 3.** Adding these equalities, U + V equals the squares X and Y together with two copies of R; that is, U + V = X + Y + 2R. [CN2]

**Step 4.** Since S = U + V, it follows that S = X + Y + 2R. Thus the square on the whole AB is equal to the squares on AC and CB and twice the rectangle contained by AC and CB, as required. [CN1]

**USED:** 2.2, 2.3, CN1, CN2
**Human refs (from References field):** 1.29, 1.31, 1.34, 1.46, 1.5, 1.6
**Jaccard:** 0.000 — AI adds ['2.2', '2.3', 'CN1', 'CN2']; Human adds ['1.29', '1.31', '1.34', '1.46', '1.5', '1.6']

## Proposition 2.5
**Statement:** If a straight line be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the straight line between the points of section is equal to the square on the half.

**Step 1.** Let AB be cut equally at C and unequally at D. Interchanging the names A and B if necessary, take the order to be A, C, D, B. Thus AC = CB. Write R(X,Y) for the rectangle contained by the lengths X and Y, and S(X) for the square on X. By the definitions, S(X) = R(X,X); reversing the order of the containing sides or replacing them by equal lengths gives coincident, hence equal, rectangles. [D2.1, D1.22, CN4]

**Step 2.** Choose the direct rectangle-decomposition route: proposition 2.1 is the earliest applicable rule and supplies all the required decompositions. Apply it to AD cut at C, with DB as the uncut straight line:
R(AD,DB) = R(AC,DB) + R(CD,DB).
Since AC = CB, this gives
R(AD,DB) = R(CB,DB) + R(CD,DB). [2.1, CN4]

**Step 3.** Apply the same rule to CB cut at D, with CD as the uncut straight line:
R(CB,CD) = R(CD,CD) + R(DB,CD)
= S(CD) + R(CD,DB). [2.1, D1.22, CN4]

**Step 4.** Apply the rule once more to CB cut at D, now with a straight line equal to CB as the uncut straight line:
S(CB) = R(CB,CD) + R(CB,DB).
Substituting the equality from Step 3 yields
S(CB) = S(CD) + R(CD,DB) + R(CB,DB). [2.1, D1.22, CN2, CN1]

**Step 5.** By Step 2, the last two rectangles together equal R(AD,DB). Therefore
S(CB) = S(CD) + R(AD,DB).
Here AD and DB are the unequal segments of the whole, CD is the straight line between the points of section, and CB is the half. Thus the rectangle contained by the unequal segments, together with the square on the straight line between the points of section, equals the square on the half, as required. [CN2, CN1]

**USED:** 2.1, CN1, CN2, CN4, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', 'CN1', 'CN2', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.6
**Statement:** If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

**Step 1.** Let AB be bisected at C, and let BD be added in the same straight line beyond B, so that A, C, B, D occur in this order and AC = CB. Write R(XY, ZW) for the rectangle contained by XY and ZW, and S(XY) for the square on XY. These symbols denote areas, not numerical products. [D2.1, D1.22]

**Step 2.** Choose the direct decomposition of AD at C and B: its pieces will match those in the expansion of the square on CD. By II.1, with BD as the uncut straight line,
R(AD, BD) = R(AC, BD) + R(CB, BD) + R(BD, BD). [2.1]

**Step 3.** Since AC = CB, the rectangles R(AC, BD) and R(CB, BD) have equal corresponding sides and coincide when superposed, so they are equal. Also, the rectangle contained by BD and BD is the square on BD. Consequently,
R(AD, BD) = 2R(CB, BD) + S(BD). [CN4, D1.22, CN2]

**Step 4.** Apply II.4 to CD cut at B. It gives
S(CD) = S(CB) + S(BD) + 2R(CB, BD). [2.4]

**Step 5.** Add S(CB) to both sides of the equality in Step 3. The resulting right-hand side consists of exactly the areas equal to S(CD) in Step 4. Hence
R(AD, BD) + S(CB) = S(CD).
Here AD is the whole original line together with the added line, BD is the added line, CB is the half, and CD is the half together with the added line. This is the required conclusion. [CN2, CN1]

**USED:** 2.1, 2.4, CN1, CN2, CN4, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', '2.4', 'CN1', 'CN2', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.7
**Statement:** If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

**Step 1.** Let AB be cut at an arbitrary point C, and take AC as the specified segment. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. Choose the direct decomposition given by 2.4, since it immediately expresses the square on the whole in terms of the segments:
S(AB) = S(AC) + S(CB) + 2R(AC,CB). [2.4]

**Step 2.** Add S(AC) to both sides. Then
S(AB) + S(AC) = 2S(AC) + S(CB) + 2R(AC,CB). [CN2]

**Step 3.** Applied to the same cut, 2.3 gives
R(AB,AC) = R(AC,CB) + S(AC).
Add this equality to itself, and then add S(CB) to both sides:
2R(AB,AC) + S(CB) = 2R(AC,CB) + 2S(AC) + S(CB). [2.3, CN2]

**Step 4.** The right-hand sides in Steps 2 and 3 are the same sum of areas. Therefore
S(AB) + S(AC) = 2R(AB,AC) + S(CB).
Thus the square on the whole and the square on the specified segment together equal twice the rectangle contained by the whole and that segment, together with the square on the remaining segment, as required. [CN1]

**USED:** 2.3, 2.4, CN1, CN2
**Human refs (from References field):** 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.3', '2.4', 'CN1', 'CN2']; Human adds ['1.43', '1.46']

## Proposition 2.8
**Statement:** If a straight line be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one straight line.

**Step 1.** Let AB be cut at an arbitrary point C, and let AC be the aforesaid segment, so that CB is the remaining segment. Produce AB beyond B sufficiently far, and cut off BD equal to AC. Thus AD consists of the whole AB and the segment AC placed together on one straight line. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. [P2, 1.3]

**Step 2.** Apply II.4 to AD cut at B. Since BD equals AC, it gives
S(AD) = S(AB) + S(AC) + 2R(AB,AC).
This decomposition reduces the proof to replacing the first two squares. [2.4]

**Step 3.** Apply II.7 to AB cut at C, taking AC as the selected segment. This proposition directly supplies the two-square sum occurring in Step 2:
S(AB) + S(AC) = 2R(AB,AC) + S(CB). [2.7]

**Step 4.** Add 2R(AB,AC) to both sides of the equality in Step 3 and combine it with Step 2. Then
S(AD) = 4R(AB,AC) + S(CB).
Since AD is AB and AC taken as one straight line, four times the rectangle contained by the whole and the aforesaid segment, together with the square on the remaining segment, equals the square on the whole and the aforesaid segment taken as one straight line. This is the required conclusion. [CN2, CN1]

**USED:** 1.3, 2.4, 2.7, CN1, CN2, P2
**Human refs (from References field):** 1.36, 1.43
**Jaccard:** 0.000 — AI adds ['1.3', '2.4', '2.7', 'CN1', 'CN2', 'P2']; Human adds ['1.36', '1.43']

## Proposition 2.9
**Statement:** If a straight line be cut into equal and unequal segments, the squares on the unequal segments of the whole are double of the square on the half and of the square on the straight line between the points of section.

**Step 1.** Let AB be bisected at C and cut unequally at D. Interchanging the names A and B if necessary, suppose the points occur in the order A, C, D, B. Write Q(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. Since AC = CB, their squares are equal, as are the rectangles contained by AC, CD and by CB, CD: the corresponding figures coincide by superposition. [CN4]

**Step 2.** Choose the direct square-expansion route: II.4 applies naturally first because AD consists of the half AC together with CD. Applied to AD cut at C, it gives
Q(AD) = Q(AC) + Q(CD) + 2R(AC,CD).
Using the equalities in Step 1, this becomes
Q(AD) = Q(CB) + Q(CD) + 2R(CB,CD). [2.4, CN1]

**Step 3.** Apply II.7 to CB cut at D, taking CD as the specified segment. This supplies exactly the rectangle term occurring in Step 2:
Q(CB) + Q(CD) = 2R(CB,CD) + Q(DB). [2.7]

**Step 4.** Add Q(DB) to both sides of the equality in Step 2 and use Step 3. Then
Q(AD) + Q(DB)
= Q(CB) + Q(CD) + 2R(CB,CD) + Q(DB)
= Q(CB) + Q(CD) + Q(CB) + Q(CD)
= 2Q(CB) + 2Q(CD). [CN2, CN1]
Thus the squares on the unequal segments AD and DB together are double the square on the half CB together with the square on CD, the straight line between the points of section. This is the required conclusion.

**USED:** 2.4, 2.7, CN1, CN2, CN4
**Human refs (from References field):** 1.29, 1.32, 1.34, 1.47, 1.6
**Jaccard:** 0.000 — AI adds ['2.4', '2.7', 'CN1', 'CN2', 'CN4']; Human adds ['1.29', '1.32', '1.34', '1.47', '1.6']

## Proposition 2.10
**Statement:** If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

**Step 1.** Let AB be bisected at C, and let BD be added in the same straight line beyond B. Write S(XY) for the square on XY. We shall apply 2.9, since an equal extension at the opposite end converts this configuration into a line cut into equal and unequal segments. [2.9]

**Step 2.** Produce BA beyond A sufficiently far, and cut off AE equal to BD. The points are therefore in the order E, A, C, B, D. [P2, 1.3]

**Step 3.** Since EA = BD and AC = CB, addition of equals gives
EC = EA + AC = BD + CB = CD.
Thus C bisects ED. Also AD is greater than its proper part BD, which equals EA; hence A cuts ED into unequal segments EA and AD. [CN2, CN5]

**Step 4.** Apply 2.9 to ED, bisected at C and cut unequally at A. Its unequal segments are EA and AD, one half is CD, and the straight line between the points of section is AC. Therefore
S(EA) + S(AD) = 2(S(CD) + S(AC)). [2.9]

**Step 5.** Since EA = BD, their squares coincide upon superposition and are equal. Substituting this equality in Step 4 gives
S(AD) + S(BD) = 2(S(AC) + S(CD)).
Here AD is the whole original line with the added line, AC is the half, and CD consists of the other equal half CB together with the added line BD. Thus the square on the whole with the added line and the square on the added line together are double the square on the half and the square on the half together with the added line, as required. [CN4, CN2, CN1]

**USED:** 1.3, 2.9, CN1, CN2, CN4, CN5, P2
**Human refs (from References field):** 1.11, 1.15, 1.29, 1.3, 1.31, 1.32, 1.34, 1.47, 1.5, 1.6, CN1, P5
**Jaccard:** 0.118 — AI adds ['2.9', 'CN2', 'CN4', 'CN5', 'P2']; Human adds ['1.11', '1.15', '1.29', '1.31', '1.32', '1.34', '1.47', '1.5', '1.6', 'P5']

## Proposition 2.11
**Statement:** To cut a given straight line so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.

**Step 1.** Let AB be the given straight line. Write R(u,v) for the rectangle contained by segments u and v, and Q(u) for the square on u, with equalities understood as equalities of areas. Construct the square ABCD, bisect AD at E, and join EB. Thus AD = AB, EA = ED, and angle EAB is right. [D2.1, D1.22, 1.46, 1.10, P1]

**Step 2.** In triangle EAB, the triangle inequalities give EB + EA > AB and EB < EA + AB. Since AB = AD = EA + EA, these imply
EA < EB < EA + AB. [1.20]

**Step 3.** Produce DA beyond A sufficiently far, and cut off EF equal to EB on the ray from E through A. Since EB > EA, F lies beyond A. Moreover, AF = EB − EA, so Step 2 gives 0 < AF < AB. Therefore cut off AH equal to AF from AB; H lies strictly between A and B. [P2, 1.3]

**Step 4.** We use 2.6 directly because DA has been bisected at E and extended by AF. It gives
R(DF,AF) + Q(EA) = Q(EF). [2.6]

**Step 5.** Since triangle EAB is right-angled at A,
Q(EB) = Q(EA) + Q(AB).
But EF = EB. Comparing this equality with Step 4 and subtracting Q(EA), we obtain
R(DF,AF) = Q(AB). [1.47, CN1, CN3]

**Step 6.** Apply the whole-and-segment identity directly to DF cut at A:
R(DF,AF) = R(DA,AF) + Q(AF).
Since DA = AB and AF = AH, Step 5 therefore becomes
Q(AB) = R(AB,AH) + Q(AH). [2.3, CN1]

**Step 7.** The square-partition identity applied to AB cut at H gives
Q(AB) = R(AB,AH) + R(AB,HB). [2.2]

**Step 8.** Compare Steps 6 and 7 and subtract the common rectangle R(AB,AH). The remainders are equal:
R(AB,HB) = Q(AH).
Thus AB has been cut at H so that the rectangle contained by the whole AB and one segment HB equals the square on the remaining segment AH, as required. [CN1, CN3]

**USED:** 1.10, 1.20, 1.3, 1.46, 1.47, 2.2, 2.3, 2.6, CN1, CN3, D1.22, D2.1, P1, P2
**Human refs (from References field):** 1.46, 1.47, 2.6
**Jaccard:** 0.214 — AI adds ['1.10', '1.20', '1.3', '2.2', '2.3', 'CN1', 'CN3', 'D1.22', 'D2.1', 'P1', 'P2']

## Proposition 2.12
**Statement:** In obtuse-angled triangles the square on the side subtending the obtuse angle is greater than the squares on the sides containing the obtuse angle by twice the rectangle contained by one of the sides about the obtuse angle, namely that on which the   perpendicular falls, and the straight line cut off outside by the perpendicular towards the obtuse angle.

**Step 1.** Let ABC be a triangle whose angle ACB is obtuse. Produce BC, and from A draw AD perpendicular to the straight line containing BC, meeting it at D. Write XY² for the square on XY and XY·ZW for the rectangle contained by XY and ZW. [P2, 1.12]

**Step 2.** The foot D lies beyond C, so that B, C, D occur in that order. Indeed, D cannot coincide with C, for then angle ACB would be right rather than obtuse. If D lay on the ray CB, triangle ACD would have an obtuse angle at C and a right angle at D. Since an obtuse angle exceeds a right angle and all right angles are equal, these two angles would exceed two right angles, contrary to I.17. Thus D lies on the opposite ray from CB. [D1.10, D1.11, P4, 1.17]

**Step 3.** Use II.4 directly: it is the whole-and-parts identity naturally applicable because C cuts BD into BC and CD. Hence
BD² = BC² + CD² + 2(BC·CD). [2.4]

**Step 4.** Since AD is perpendicular to BD, triangles ADB and ADC are right-angled at D. Applying I.47 to each gives
AB² = AD² + BD²,
AC² = AD² + CD². [D1.10, 1.47]

**Step 5.** Add AD² to both sides of the equality in Step 3, and substitute the equal quantities from Step 4. We obtain
AB² = AD² + BC² + CD² + 2(BC·CD)
     = AC² + BC² + 2(BC·CD). [CN2, CN1]

**Step 6.** Therefore the square on AB, the side subtending the obtuse angle, is greater than the squares on AC and BC by exactly twice the rectangle contained by BC and CD. Here BC is the side on whose produced line the perpendicular falls, and CD is the segment cut off outside the triangle between the perpendicular's foot and the obtuse vertex. The displayed equality gives the asserted excess, and the whole is greater than its part. This proves the proposition. [CN5]

**USED:** 1.12, 1.17, 1.47, 2.4, CN1, CN2, CN5, D1.10, D1.11, P2, P4
**Human refs (from References field):** 1.47, 2.4
**Jaccard:** 0.182 — AI adds ['1.12', '1.17', 'CN1', 'CN2', 'CN5', 'D1.10', 'D1.11', 'P2', 'P4']

## Proposition 2.13
**Statement:** In acute-angled triangles the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle by twice the rectangle contained by one of the sides about the acute angle, namely that on which the perpendicular falls, and the straight line cut off within by the perpendicular towards the acute angle.

**Step 1.** Let ABC be an acute-angled triangle, and take ABC as the acute angle in the assertion. Its opposite side is AC, and its containing sides are AB and BC. All three angles are less than a right angle. Produce BC as necessary and draw AD perpendicular to its straight line. [D1.21, D1.12, P2, 1.12]

**Step 2.** The foot D lies strictly between B and C. It cannot coincide with either endpoint, since then the triangle would have a right angle. If D lay beyond B, angle ABC would be an exterior angle of triangle ABD and hence greater than the right angle ADB, contrary to its being acute. If D lay beyond C, angle ACB would similarly be an exterior angle of triangle ACD and greater than the right angle ADC. Thus BC is cut internally at D, and BD is the segment towards the chosen acute angle at B. [D1.10, D1.12, 1.16]

**Step 3.** Write Q(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW. Apply II.7 directly to BC cut at D, taking BD as the selected segment; this gives precisely the rectangle involving the whole side and the segment towards B:

Q(BC) + Q(BD) = 2R(BC, BD) + Q(DC). [D2.1, 2.7]

**Step 4.** Since ADB and ADC are right angles, the squares on the hypotenuses of the two right-angled triangles give

Q(AB) = Q(AD) + Q(BD),

Q(AC) = Q(AD) + Q(DC). [1.47]

**Step 5.** Add Q(AD) to both sides of the equality in Step 3 and substitute the equal magnitudes from Step 4. We obtain

Q(AB) + Q(BC) = Q(AC) + 2R(BC, BD). [CN2, CN1]

Therefore the square on AC is less than the squares on AB and BC together by exactly twice the rectangle contained by BC, the side on which the perpendicular falls, and BD, the segment cut off within towards the acute angle ABC. The inequality is strict because the rectangle has positive area. This is the required conclusion. [CN5]

**USED:** 1.12, 1.16, 1.47, 2.7, CN1, CN2, CN5, D1.10, D1.12, D1.21, D2.1, P2
**Human refs (from References field):** 1.47, 2.7
**Jaccard:** 0.167 — AI adds ['1.12', '1.16', 'CN1', 'CN2', 'CN5', 'D1.10', 'D1.12', 'D1.21', 'D2.1', 'P2']

## Proposition 2.14
**Statement:** To construct a square equal to a given rectilineal figure.

**Step 1.** Let F be the given rectilineal figure. Construct a right angle, and in that angle construct a parallelogram ABCD equal to F. Its remaining angles are also right angles, since adjacent angles of a parallelogram equal two right angles and opposite angles are equal. Thus ABCD is a rectangle. This reduces the required construction directly to squaring a rectangle. [1.11, 1.45, 1.29, 1.34]

**Step 2.** If AB = AD, the opposite sides are also equal, so ABCD is equilateral and right-angled: it is already the required square. Otherwise, label the rectangle so that AB > AD. [1.34, D1.22]

**Step 3.** Produce AB beyond B sufficiently far, and cut off BE equal to AD. Bisect AE at M. Since AB > BE, M lies between A and B; the points therefore occur in the order A, M, B, E. [P2, 1.3, 1.10]

**Step 4.** Describe the circle with centre M and radius ME; it also passes through A. At B draw a perpendicular to AE, producing it to meet the circle at H, and join MH. Here MB < ME, so B is inside the circle. Since H and E lie on the circle, MH = ME. Construct a square K on BH. [P3, 1.11, P2, P1, D1.15, 1.46]

**Step 5.** Write R(x,y) for the rectangle contained by lengths x and y, and S(x) for the square on length x. The line AE is cut equally at M and unequally at B. Proposition 2.5 is the direct choice because these are precisely its hypotheses. It gives
R(AB,BE) + S(MB) = S(ME).
Since ME = MH, the squares on these equal lengths coincide upon superposition and hence are equal. Therefore
R(AB,BE) + S(MB) = S(MH). [D2.1, 2.5, CN4, CN1]

**Step 6.** Triangle MBH is right-angled at B. Consequently,
S(MH) = S(MB) + S(BH).
Combining this with Step 5 and subtracting the common square S(MB), we obtain
R(AB,BE) = S(BH). [1.47, CN1, CN3]

**Step 7.** Since BE = AD, the rectangle contained by AB and BE equals rectangle ABCD: their corresponding adjacent sides are equal, so the rectangles coincide upon superposition. But ABCD equals F, and S(BH) is the constructed square K. Hence K equals the given rectilineal figure F. Thus a square equal to the given rectilineal figure has been constructed. [D2.1, CN4, CN1]

**USED:** 1.10, 1.11, 1.29, 1.3, 1.34, 1.45, 1.46, 1.47, 2.5, CN1, CN3, CN4, D1.15, D1.22, D2.1, P1, P2, P3
**Human refs (from References field):** 1.45, 1.47, 2.5
**Jaccard:** 0.167 — AI adds ['1.10', '1.11', '1.29', '1.3', '1.34', '1.46', 'CN1', 'CN3', 'CN4', 'D1.15', 'D1.22', 'D2.1', 'P1', 'P2', 'P3']
