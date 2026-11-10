# Book 2 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 2.1
**Statement:** If there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments.

**Step 1.** Let the uncut straight line have length a, and let the other straight line be divided at the ordered points B₀, B₁, …, Bₙ into any finite number of segments. We use direct subdivision of one rectangle. At B₀ erect a perpendicular to B₀Bₙ, produce it sufficiently far, and cut off B₀C₀ equal to a. [1.11, P2, 1.3]

**Step 2.** Through C₀ draw a straight line parallel to B₀Bₙ. Through each Bᵢ, for 1 ≤ i ≤ n, draw a straight line parallel to B₀C₀, meeting the line through C₀ at Cᵢ. These upright lines are mutually parallel, since they are parallel to the same straight line. The angles made with the two horizontal lines are right angles. Thus B₀BₙCₙC₀ and every strip Bᵢ₋₁BᵢCᵢCᵢ₋₁ are rectangular parallelograms. [1.31, 1.30, 1.29]

**Step 3.** For each i ≥ 1, B₀BᵢCᵢC₀ is a parallelogram. Its opposite sides BᵢCᵢ and B₀C₀ are equal. Consequently every upright side has length a, including B₀C₀ itself. [1.34, CN1]

**Step 4.** Write R(u,v) for the rectangular area contained by straight lines of lengths u and v. By the definition of a rectangle contained by two straight lines, the whole rectangle B₀BₙCₙC₀ is R(a,B₀Bₙ), and, for each i, the strip Bᵢ₋₁BᵢCᵢCᵢ₋₁ is R(a,Bᵢ₋₁Bᵢ). [D2.1]

**Step 5.** The cuts through the ordered division points partition the whole rectangle into exactly these strips: the parallel cuts do not meet, and consecutive strips share only their boundary sides. Hence the strips together coincide with the whole rectangle. Adding their identified areas therefore gives

R(a,B₀Bₙ) = R(a,B₀B₁) + R(a,B₁B₂) + ··· + R(a,Bₙ₋₁Bₙ).

Thus the rectangle contained by the two original straight lines equals the rectangles contained by the uncut straight line and each segment of the divided straight line, as required. [D1.23, CN4, CN2]

**USED:** 1.11, 1.29, 1.3, 1.30, 1.31, 1.34, CN1, CN2, CN4, D1.23, D2.1, P2
**Human refs (from References field):** 1.11, 1.3, 1.31, 1.34
**Jaccard:** 0.333 — AI adds ['1.29', '1.30', 'CN1', 'CN2', 'CN4', 'D1.23', 'D2.1', 'P2']

## Proposition 2.2
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and both of the segments is equal to the square on the whole.

**Step 1.** Let the straight line AB be cut at an arbitrary interior point C. Apply Proposition 2.1 with both whole lengths equal to AB, dividing one of them into AC and CB. It gives: the rectangle contained by AB and AB is equal to the rectangles contained by AB and AC, and by AB and CB, taken together. This direct specialization is the natural route because Proposition 2.1 already supplies exactly the required division into two rectangles. [2.1]

**Step 2.** The square on AB is equilateral and right-angled; its two sides containing a right angle are therefore both equal to AB. Thus it is the rectangle contained by AB and AB. Substituting this identification into Step 1, the rectangles contained by the whole AB and each of its segments AC and CB, taken together, are equal to the square on AB, as required. [D1.22, D2.1]

**USED:** 2.1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', 'D1.22', 'D2.1']; Human adds ['1.31', '1.46']

## Proposition 2.3
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and one of the segments is equal to the rectangle contained by the segments and the square on the aforesaid segment.

**Step 1.** Let the straight line AB be cut at an arbitrary point C, and take BC as the aforesaid segment. Write R(u,v) for the rectangle contained by straight lines u and v, namely the rectangular parallelogram having those adjacent sides. [D2.1]

**Step 2.** Choose the direct distribution route: II.1 is the earliest applicable rectangle-distribution proposition. Apply it to the uncut straight line BC and the straight line AB cut into AC and CB. It gives
R(AB,BC) = R(AC,BC) + R(BC,BC). [2.1]

**Step 3.** The rectangle contained by BC and BC is the square on BC. Thus the equality in Step 2 says that the rectangle contained by the whole AB and the chosen segment BC equals the rectangle contained by the two segments AC, BC together with the square on BC. This is the required conclusion. [D1.22, D2.1]

**USED:** 2.1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', 'D1.22', 'D2.1']; Human adds ['1.31', '1.46']

## Proposition 2.4
**Statement:** If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.

**Step 1.** Let the straight line AB be cut at an arbitrary interior point C. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW; sums below mean sums of areas. The order of the two containing sides does not change the rectangle. [D1.22, D2.1]

**Step 2.** Use II.2 directly, since it gives precisely the decomposition of the square on the whole into rectangles involving the two segments:
S(AB) = R(AB,AC) + R(AB,CB). [2.2]

**Step 3.** Apply II.3 to the same cut, first taking AC as the chosen segment and then taking CB. Thus
R(AB,AC) = S(AC) + R(AC,CB),
and
R(AB,CB) = S(CB) + R(AC,CB). [2.3, D2.1]

**Step 4.** Adding these equalities, equals being added to equals, gives
R(AB,AC) + R(AB,CB) = S(AC) + S(CB) + 2R(AC,CB). [CN2]

**Step 5.** The equality in Step 2 and that in Step 4 have the same sum of rectangles. Therefore
S(AB) = S(AC) + S(CB) + 2R(AC,CB).
Hence the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments, as required. [CN1]

**USED:** 2.2, 2.3, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.29, 1.31, 1.34, 1.46, 1.5, 1.6
**Jaccard:** 0.000 — AI adds ['2.2', '2.3', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.29', '1.31', '1.34', '1.46', '1.5', '1.6']

## Proposition 2.5
**Statement:** If a straight line be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the straight line between the points of section is equal to the square on the half.

**Step 1.** Let AB be cut equally at C and unequally at D. By interchanging the names A and B if necessary, take the order to be A, C, D, B. Thus AC = CB. Write R(X,Y) for the rectangle contained by the lengths X and Y, and S(X) for the square on X. The two containing sides may be exchanged, and R(X,X) = S(X). Rectangles with the same containing lengths coincide upon superposition, so equal lengths may be substituted. [D2.1, D1.22, CN4]

**Step 2.** Choose the direct rectangle-decomposition route: II.1 applies to each required partition, including a rectangle whose equal sides make it a square. Apply it to AC and CB, with CB cut at D. Since AC = CB, this gives
S(CB) = R(AC,CD) + R(AC,DB). [2.1, D1.22, CN4]

**Step 3.** Since AC = CB, the rectangle R(AC,CD) equals R(CB,CD). Apply II.1 to CD and CB, again cutting CB at D. Consequently,
R(AC,CD) = R(CD,CD) + R(DB,CD)
= S(CD) + R(CD,DB). [2.1, D2.1, D1.22, CN4, CN1]

**Step 4.** Apply II.1 to DB and AD, with AD cut at C. It follows that
R(AD,DB) = R(AC,DB) + R(CD,DB). [2.1, D2.1]

**Step 5.** Add R(AC,DB) to the equality in Step 3 and use Steps 2 and 4. By addition of equals and equality to the same magnitude,
S(CB) = S(CD) + R(CD,DB) + R(AC,DB)
= S(CD) + R(AD,DB).
Here AD and DB are the unequal segments of AB, CD is the straight line between the points of section, and CB is the half of AB. Therefore the rectangle contained by the unequal segments, together with the square on the straight line between the points of section, equals the square on the half. [CN2, CN1]

**USED:** 2.1, CN1, CN2, CN4, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', 'CN1', 'CN2', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.6
**Statement:** If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

**Step 1.** Let AB be bisected at C, and let BD be added in the same straight line beyond B, so that A, C, B, D occur in this order and AC = CB. Write R(x,y) for the rectangle contained by lengths x,y, and S(x) for the square on length x; in particular, R(x,x) = S(x). We must prove R(AD,BD) + S(CB) = S(CD). [D2.1, D1.22]

**Step 2.** Apply II.1 to AD, divided at C and B, and the uncut line BD. This is the direct choice because the required three-part division is already given. Thus
R(AD,BD) = R(AC,BD) + R(CB,BD) + R(BD,BD).
Since AC = CB, this becomes
R(AD,BD) = 2R(CB,BD) + S(BD). [2.1, D1.22]

**Step 3.** Apply II.4 to CD, cut at B. It gives
S(CD) = S(CB) + S(BD) + 2R(CB,BD). [2.4]

**Step 4.** Add S(CB) to both sides of the equality in Step 2. The resulting right-hand side is exactly the sum equal to S(CD) in Step 3. Hence
R(AD,BD) + S(CB) = S(CD).
Therefore the rectangle contained by the whole with the added line and the added line, together with the square on the half, equals the square on the half together with the added line, as required. [CN2, CN1]

**USED:** 2.1, 2.4, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', '2.4', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.7
**Statement:** If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

**Step 1.** Let AB be cut at C, and let AC be the chosen segment. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. We use II.4 to decompose the square on the whole, followed by II.3 to identify the rectangle involving the chosen segment; these directly match the magnitudes in the claim. By II.4,
S(AB) = S(AC) + S(CB) + 2R(AC,CB). [2.4]

**Step 2.** Add S(AC) to both sides. Then
S(AB) + S(AC) = 2S(AC) + 2R(AC,CB) + S(CB). [CN2]

**Step 3.** By II.3, applied to the same cut and the chosen segment AC,
R(AB,AC) = R(AC,CB) + S(AC).
Adding this equality to itself gives
2R(AB,AC) = 2R(AC,CB) + 2S(AC). [2.3, CN2]

**Step 4.** Add S(CB) to both sides of the last equality and compare with Step 2. Things equal to the same magnitude are equal; hence
S(AB) + S(AC) = 2R(AB,AC) + S(CB).
Thus the square on the whole and the square on the chosen segment together equal twice the rectangle contained by the whole and that segment, together with the square on the remaining segment, as required. [CN2, CN1]

**USED:** 2.3, 2.4, CN1, CN2
**Human refs (from References field):** 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.3', '2.4', 'CN1', 'CN2']; Human adds ['1.43', '1.46']

## Proposition 2.8
**Statement:** If a straight line be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one straight line.

**Step 1.** Let the straight line AB be cut at any point C, and let AC be the chosen segment, so that CB is the remaining segment. Produce AB beyond B and cut off BD equal to AC. Thus AD is the whole AB and the chosen segment AC taken as one straight line. This construction uses P2 and 1.3. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW; multiples denote repeated addition of areas. [P2, 1.3]

**Step 2.** Apply 2.4 to AD cut at B. This is the direct starting point because its two segments are precisely the original whole and a copy of the chosen segment. Since BD = AC,
S(AD) = S(AB) + S(AC) + 2R(AB,AC). [2.4]

**Step 3.** The paired squares on the right are exactly the combination addressed by 2.7. Apply that proposition to AB cut at C, with AC as the chosen segment:
S(AB) + S(AC) = 2R(AB,AC) + S(CB). [2.7]

**Step 4.** Add 2R(AB,AC) to both sides of the equality in Step 3. By CN2,
S(AB) + S(AC) + 2R(AB,AC) = 4R(AB,AC) + S(CB).
Comparing this with Step 2, CN1 gives
S(AD) = 4R(AB,AC) + S(CB).
Thus four times the rectangle contained by the whole and the chosen segment, together with the square on the remaining segment, equals the square on the whole and the chosen segment taken as one straight line, as required. [CN2, CN1]

**USED:** 1.3, 2.4, 2.7, CN1, CN2, P2
**Human refs (from References field):** 1.36, 1.43
**Jaccard:** 0.000 — AI adds ['1.3', '2.4', '2.7', 'CN1', 'CN2', 'P2']; Human adds ['1.36', '1.43']

## Proposition 2.9
**Statement:** If a straight line be cut into equal and unequal segments, the squares on the unequal segments of the whole are double of the square on the half and of the square on the straight line between the points of section.

**Step 1.** Let AB be cut equally at C and unequally at D. Interchanging the names A and B if necessary, take the points in the order A, C, D, B. Write S(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW; sums below are sums of areas. [D1.22, D2.1]

**Step 2.** Since AC = CB, the squares on AC and CB coincide upon superposition, as do the rectangles contained respectively by AC, CD and by CB, CD. Hence
S(AC) = S(CB), and R(AC, CD) = R(CB, CD). [CN4]

**Step 3.** Apply II.4 to AD cut at C. It gives
S(AD) = S(AC) + S(CD) + 2R(AC, CD).
This directly expresses the square on the longer unequal segment using the half and the distance between the points of section. [2.4]

**Step 4.** Apply II.7 to CB cut at D, choosing CD as the specified segment. This route places the same rectangle together with the square on DB, ready for substitution:
S(CB) + S(CD) = 2R(CB, CD) + S(DB).
Using the equalities of Step 2, this becomes
S(AC) + S(CD) = 2R(AC, CD) + S(DB). [2.7, CN2, CN1]

**Step 5.** Add S(DB) to both sides of the equality in Step 3, and then substitute the equality in Step 4. Thus
S(AD) + S(DB)
= S(AC) + S(CD) + [2R(AC, CD) + S(DB)]
= [S(AC) + S(CD)] + [S(AC) + S(CD)]
= 2S(AC) + 2S(CD). [CN2, CN1]
Therefore the squares on the unequal segments AD and DB are together double the square on the half AC and the square on CD, the straight line between the points of section. This proves the proposition.

**USED:** 2.4, 2.7, CN1, CN2, CN4, D1.22, D2.1
**Human refs (from References field):** 1.29, 1.32, 1.34, 1.47, 1.6
**Jaccard:** 0.000 — AI adds ['2.4', '2.7', 'CN1', 'CN2', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.29', '1.32', '1.34', '1.47', '1.6']

## Proposition 2.10
**Statement:** If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

**Step 1.** Let AB be bisected at C, and let BD be added in the same straight line beyond B. Thus A, C, B, D occur in that order, and AC = CB. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. Squares on equal lengths, and rectangles with equal corresponding dimensions, coincide and are therefore equal. Consequently S(AC) = S(CB) and R(AC,CD) = R(CD,CB). [CN4]

**Step 2.** Apply II.4 to AD cut at C. This expansion directly exposes the squares on the half AC and on the combined length CD:
S(AD) = S(AC) + S(CD) + 2R(AC,CD). [2.4]

**Step 3.** Apply II.7 to CD cut at B, taking CB as the specified segment:
S(CD) + S(CB) = 2R(CD,CB) + S(BD).
This proposition is used because its rectangle term is exactly the one obtained in Step 2. By the equalities in Step 1, we therefore have
2R(AC,CD) + S(BD) = S(CD) + S(AC). [2.7, CN1]

**Step 4.** Add S(BD) to both sides of the equality in Step 2, and substitute the equality from Step 3. Then
S(AD) + S(BD)
= S(AC) + S(CD) + [2R(AC,CD) + S(BD)]
= S(AC) + S(CD) + S(CD) + S(AC)
= 2S(AC) + 2S(CD). [CN2, CN1]
Since AD is the whole with the added straight line, AC is the half, and CD consists of the half CB together with the added straight line BD, this is precisely the required conclusion.

**USED:** 2.4, 2.7, CN1, CN2, CN4
**Human refs (from References field):** 1.11, 1.15, 1.29, 1.3, 1.31, 1.32, 1.34, 1.47, 1.5, 1.6, CN1, P5
**Jaccard:** 0.062 — AI adds ['2.4', '2.7', 'CN2', 'CN4']; Human adds ['1.11', '1.15', '1.29', '1.3', '1.31', '1.32', '1.34', '1.47', '1.5', '1.6', 'P5']

## Proposition 2.11
**Statement:** To cut a given straight line so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.

**Step 1.** Let AB be the given straight line. Construct the square ABCD, so that AD = AB and angle DAB is right. Bisect AD at E, and join EB. Thus AE = ED and AB = AE + ED. [1.46, D1.22, 1.10, P1]

**Step 2.** In triangle AEB, the triangle inequality gives EB + AE > AB = AE + AE, and also EB < AE + AB. Consequently,
AE < EB < AE + AB. [1.20]

**Step 3.** Produce EA beyond A sufficiently far, and cut off EF equal to EB on this ray. Since EB > EA, the point F lies beyond A. Moreover, EA + AF = EF = EB < EA + AB, so AF < AB. Therefore cut off AH equal to AF from AB; H lies strictly between A and B. [P2, 1.3]

**Step 4.** Write S(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW. Use the bisected-and-extended-line proposition, since AD is bisected at E and extended beyond A by AF. It gives
R(DF, AF) + S(AE) = S(EF). [D2.1, 2.6]

**Step 5.** Since triangle EAB is right-angled at A,
S(EB) = S(AE) + S(AB).
But EF = EB. Comparing this equality with that in Step 4 and subtracting S(AE), we obtain
R(DF, AF) = S(AB). [1.47, CN1, CN3]

**Step 6.** Apply the whole-and-segment rectangle proposition to DF cut at A, choosing AF as the segment. It gives
R(DF, AF) = R(DA, AF) + S(AF).
Since DA = AB and AF = AH, Step 5 therefore yields
S(AB) = R(AB, AH) + S(AH). [2.3, CN1]

**Step 7.** Applying the rectangle decomposition for a line cut into two segments to AB cut at H gives
S(AB) = R(AB, AH) + R(AB, HB). [2.2]

**Step 8.** The right-hand sides in Steps 6 and 7 are equal. Subtracting their common rectangle R(AB, AH), we obtain
S(AH) = R(AB, HB).
Thus AB has been cut at H so that the rectangle contained by the whole AB and the segment HB equals the square on the remaining segment AH, as required. [CN1, CN3]

**USED:** 1.10, 1.20, 1.3, 1.46, 1.47, 2.2, 2.3, 2.6, CN1, CN3, D1.22, D2.1, P1, P2
**Human refs (from References field):** 1.46, 1.47, 2.6
**Jaccard:** 0.214 — AI adds ['1.10', '1.20', '1.3', '2.2', '2.3', 'CN1', 'CN3', 'D1.22', 'D2.1', 'P1', 'P2']

## Proposition 2.12
**Statement:** In obtuse-angled triangles the square on the side subtending the obtuse angle is greater than the squares on the sides containing the obtuse angle by twice the rectangle contained by one of the sides about the obtuse angle, namely that on which the   perpendicular falls, and the straight line cut off outside by the perpendicular towards the obtuse angle.

**Step 1.** Let ABC be a triangle with obtuse angle BAC. Choose AB as the side containing the obtuse angle on whose extended line the perpendicular is to fall. Produce its line and draw CD perpendicular to it, with foot D. Write XY² for the square on XY, and R(XY, ZW) for the rectangle contained by XY and ZW. [P2, 1.12]

**Step 2.** The point D lies beyond A, so the order is B, A, D. Indeed, D cannot equal A, since then BAC would be right. Nor can D lie on the ray AB away from A: in that case triangle ACD would have the obtuse angle CAD and the right angle ADC, contrary to the fact that any two angles of a triangle together are less than two right angles. Thus AD is precisely the straight line cut off outside towards the obtuse angle. [D1.10, D1.11, 1.17]

**Step 3.** Apply the square-of-a-divided-line proposition to BD cut at A:
BD² = AB² + AD² + 2R(AB, AD).
This is the natural expansion to choose, since the segments AB and AD are exactly those required in the rectangle of the conclusion. [2.4]

**Step 4.** Since CD is perpendicular to BD, triangles BDC and ADC are right-angled at D. Hence
BC² = BD² + CD²,
and
AC² = AD² + CD². [D1.10, 1.47]

**Step 5.** Add CD² to both sides of the equality in Step 3, and substitute the equalities from Step 4. This gives
BC² = AB² + AC² + 2R(AB, AD). [CN2, CN1]

**Step 6.** Since AB and AD are nonzero, the twice-rectangle is a positive area. Therefore the square on BC, the side subtending the obtuse angle, is greater than the squares on AB and AC by twice the rectangle contained by AB and the external segment AD cut off by the perpendicular towards that angle. This is the required conclusion. [CN5]

**USED:** 1.12, 1.17, 1.47, 2.4, CN1, CN2, CN5, D1.10, D1.11, P2
**Human refs (from References field):** 1.47, 2.4
**Jaccard:** 0.200 — AI adds ['1.12', '1.17', 'CN1', 'CN2', 'CN5', 'D1.10', 'D1.11', 'P2']

## Proposition 2.13
**Statement:** In acute-angled triangles the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle by twice the rectangle contained by one of the sides about the acute angle, namely that on which the perpendicular falls, and the straight line cut off within by the perpendicular towards the acute angle.

**Step 1.** Let ABC be an acute-angled triangle, and choose the acute angle ABC. Its opposite side is AC, and its containing sides are AB and BC. All three angles are less than a right angle. Write X² for the square on a segment X, and R(X,Y) for the rectangle contained by segments X and Y. [D1.21, D1.12]

**Step 2.** Draw AD perpendicular to the straight line BC, with foot D. The point D lies strictly between B and C. Indeed, if D coincided with B or C, the corresponding angle of ABC would be right. If D lay beyond B, angle ABC would be an exterior angle of triangle ABD and hence greater than its right angle ADB. If D lay beyond C, angle ACB would similarly be greater than the right angle ADC. Each possibility contradicts the acuteness of ABC. Thus BD is the segment cut off within BC towards the chosen angle B. [1.12, D1.10, 1.16, D1.12]

**Step 3.** Use II.7 directly: its whole-and-segment rectangle is exactly the rectangle required here. Since BC is cut at D,
BC² + BD² = 2R(BC,BD) + CD². [2.7]

**Step 4.** Applying the theorem on the square of the hypotenuse to the right-angled triangles ADB and ADC gives
AB² = AD² + BD²,
AC² = AD² + CD². [1.47]

**Step 5.** Add AD² to both sides of the equality in Step 3, and substitute the equal areas from Step 4. Therefore
AB² + BC² = AC² + 2R(BC,BD). [CN2, CN1]

**Step 6.** Subtracting AC² shows that the excess of AB² + BC² over AC² is exactly 2R(BC,BD). This rectangle has nonzero sides, since D lies strictly between B and C; hence the sum of the two squares is greater than AC². Thus the square on the side subtending the chosen acute angle is less than the squares on its containing sides by twice the rectangle contained by BC, the side on which the perpendicular falls, and BD, the segment cut off within it towards that angle. Since the chosen angle was arbitrary, the proposition follows. [CN3, CN5]

**USED:** 1.12, 1.16, 1.47, 2.7, CN1, CN2, CN3, CN5, D1.10, D1.12, D1.21
**Human refs (from References field):** 1.47, 2.7
**Jaccard:** 0.182 — AI adds ['1.12', '1.16', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.10', 'D1.12', 'D1.21']

## Proposition 2.14
**Statement:** To construct a square equal to a given rectilineal figure.

**Step 1.** Let the given rectilineal figure be F. Construct a right angle, and in that angle construct a parallelogram ABCD equal to F (1.11, 1.45). Its remaining angles are also right angles, by the properties of parallel lines and opposite angles of a parallelogram (1.29, 1.34). Thus ABCD is the rectangle contained by AB and AD (D2.1).

**Step 2.** If AB equals AD, the opposite sides are equal as well, so ABCD is equilateral and right-angled: it is already the required square (1.34, D1.22). Otherwise, relabel the rectangle if necessary so that AB is greater than AD. We shall convert this unequal-sided rectangle into a square.

**Step 3.** Produce AB beyond B and cut off BE equal to AD (P2, 1.3). Bisect AE at O (1.10). Since AB is greater than BE, O lies between A and B. Thus AE is cut equally at O and unequally at B.

**Step 4.** Describe the circle with centre O and radius OA (P3). Since OA equals OE, this circle passes through A and E (D1.15). At B draw a perpendicular to AE and produce it to meet the circle at H (1.11, P2). Here B is inside the circle, since OB is less than OE, so the perpendicular reaches its circumference. Join OH (P1). The angle OBH is right, and OH equals OA because they are radii of the same circle (D1.15).

**Step 5.** Write S(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW. Apply 2.5 to AE, cut equally at O and unequally at B. This is the directly matching proposition because the construction supplies precisely its two kinds of division. It gives
R(AB, BE) + S(OB) = S(OA).

**Step 6.** In the right-angled triangle OBH, the square on the hypotenuse equals the squares on the other two sides (1.47):
S(OH) = S(OB) + S(BH).
Since OH equals OA, the right-hand total here equals the total in Step 5 (CN1). Subtracting the common square S(OB) gives
R(AB, BE) = S(BH) (CN3).
But BE equals AD, so R(AB, BE) is equal to the rectangle ABCD, which is contained by AB and AD (D2.1). Consequently S(BH) equals ABCD and hence the given figure F (CN1).

**Step 7.** Construct a square on BH (1.46). By Step 6 this square is equal to the given rectilineal figure. Therefore a square equal to the given rectilineal figure has been constructed.

**USED:** 1.10, 1.11, 1.29, 1.3, 1.34, 1.45, 1.46, 1.47, 2.5, CN1, CN3, D1.15, D1.22, D2.1, P1, P2, P3
**Human refs (from References field):** 1.45, 1.47, 2.5
**Jaccard:** 0.176 — AI adds ['1.10', '1.11', '1.29', '1.3', '1.34', '1.46', 'CN1', 'CN3', 'D1.15', 'D1.22', 'D2.1', 'P1', 'P2', 'P3']
