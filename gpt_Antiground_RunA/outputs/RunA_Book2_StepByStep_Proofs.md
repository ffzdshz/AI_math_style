# Book 2 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 2.1
**Statement:** If there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments.

**Step 1.** Let the uncut straight line be a, and let the other straight line A₀Aₙ be divided at the successive points A₁, …, Aₙ₋₁ into any finite number n of segments. Choose the direct dissection route: construct one rectangle and divide it along the given cuts. Produce the base as necessary, erect a perpendicular at A₀, and, producing that perpendicular sufficiently, cut off A₀B₀ equal to a. [P2, 1.11, 1.3]

**Step 2.** Through B₀ draw a straight line parallel to A₀Aₙ. Through each Aᵢ, for i = 1, …, n, draw a straight line parallel to A₀B₀, meeting the line through B₀ at Bᵢ. The transverse lines A₀B₀, A₁B₁, …, AₙBₙ are mutually parallel. [1.31, 1.30]

**Step 3.** The whole parallelogram A₀AₙBₙB₀ and every strip Aᵢ₋₁AᵢBᵢBᵢ₋₁ are rectangular: the parallel-line angle relations carry the original right angle at A₀ to their angles. Moreover, in each parallelogram A₀AᵢBᵢB₀, opposite sides are equal, so AᵢBᵢ = A₀B₀ = a. Thus every transverse side equals a. Here 1.34 is used directly for the side equality supplied by the construction, rather than introducing an area-comparison theorem. [1.29, 1.34, CN1]

**Step 4.** Denote the whole rectangle by R and the successive strips by R₁, …, Rₙ. By the definition of a rectangle contained by two straight lines, R is the rectangle contained by a and A₀Aₙ, while Rᵢ is the rectangle contained by a and Aᵢ₋₁Aᵢ: these are its two adjacent sides containing a right angle. [D2.1]

**Step 5.** The transverse dividing lines cannot meet one another, since they are parallel. Consequently, the strips, taken in the order of the given segments, fill R exactly, with no overlapping interiors and no gaps. Their assembled figure therefore coincides with R and is equal to it. [D1.23, CN4]

**Step 6.** Replace each strip by the rectangle identified with it in Step 4, adding these equalities. The equality of the assembled strips with R gives
Rect(a, A₀Aₙ) = Rect(a, A₀A₁) + Rect(a, A₁A₂) + ⋯ + Rect(a, Aₙ₋₁Aₙ),
where the sum denotes the rectangles taken together. Since the number and positions of the cuts were arbitrary, the rectangle contained by the two given straight lines equals the rectangles contained by the uncut straight line and each segment of the cut straight line. [CN2, CN1]

**USED:** 1.11, 1.29, 1.3, 1.30, 1.31, 1.34, CN1, CN2, CN4, D1.23, D2.1, P2
**Human refs (from References field):** 1.11, 1.3, 1.31, 1.34
**Jaccard:** 0.333 — AI adds ['1.29', '1.30', 'CN1', 'CN2', 'CN4', 'D1.23', 'D2.1', 'P2']

## Proposition 2.2
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and both of the segments is equal to the square on the whole.

**Step 1.** Let the straight line AB be cut at an arbitrary interior point C. Apply 2.1 with both whole straight lines equal to AB, taking the segments of the cut line to be AC and CB. The rectangle contained by AB and AB is therefore equal to the sum of the rectangles contained by AB and AC, and by AB and CB (2.1). **Path choice:** specialize 2.1 directly, since it already provides exactly the required two-part decomposition.

**Step 2.** The rectangle contained by AB and AB is a rectangular parallelogram whose two adjacent sides are each equal to AB (D2.1). Its opposite sides are equal (1.34); hence all four sides are equal. Being both equilateral and right-angled, it is the square on AB (D1.22).

**Step 3.** The two rectangles from Step 1, taken together, and the square on AB are thus equal to the same rectangle. Therefore the rectangles contained by the whole AB and each of its segments AC and CB, taken together, are equal to the square on the whole AB (CN1). This proves the proposition.

**USED:** 1.34, 2.1, CN1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.000 — AI adds ['1.34', '2.1', 'CN1', 'D1.22', 'D2.1']; Human adds ['1.31', '1.46']

## Proposition 2.3
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and one of the segments is equal to the rectangle contained by the segments and the square on the aforesaid segment.

**Step 1.** Let AB be cut at an arbitrary interior point C, and take BC as the aforesaid segment. Write R(X,Y) for the rectangle contained by straight lines X and Y; their order does not change the rectangle designated. [D2.1]

**Step 2.** Path choice: use 2.1 directly, since its general decomposition of a rectangle applies immediately, without an auxiliary construction. Apply it to the straight lines BC and AB, with AB cut into AC and CB. It gives
R(BC,AB) = R(BC,AC) + R(BC,BC). [2.1]

**Step 3.** The rectangular parallelogram contained by BC and BC has two adjacent sides equal to BC. Its opposite sides are equal, so all four sides are equal. Since it is also right-angled, it is a square on BC. Thus R(BC,BC) is the square on BC. [1.34, D1.22, D2.1]

**Step 4.** Adding R(BC,AC) to the equality in Step 3 and combining with Step 2 yields
R(AB,BC) = R(AC,BC) + the square on BC. [CN2, CN1, D2.1]
Therefore the rectangle contained by the whole and the selected segment equals the rectangle contained by the two segments together with the square on the selected segment. Either segment may be selected by interchanging the names A and B. This proves the proposition.

**USED:** 1.34, 2.1, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.000 — AI adds ['1.34', '2.1', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.31', '1.46']

## Proposition 2.4
**Statement:** If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.

**Step 1.** Let the straight line AB be cut at an arbitrary interior point C. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW, regarding these figures as areas. The order of the two containing sides in R is immaterial: they name the same rectangle. [D1.22, D2.1]

**Step 2.** By 2.2, applied to AB cut at C,
S(AB) = R(AB,AC) + R(AB,CB).
Path choice: use 2.2 rather than the more general 2.1 because it directly decomposes the square on the whole into the two rectangles needed here. [2.2]

**Step 3.** Apply 2.3 to the same cut, taking AC as the specified segment. Then
R(AB,AC) = S(AC) + R(AC,CB). [2.3]

**Step 4.** Apply 2.3 again, now taking CB as the specified segment. Then
R(AB,CB) = S(CB) + R(AC,CB). [2.3, D2.1]

**Step 5.** Add the equal areas in Steps 3 and 4. Thus
R(AB,AC) + R(AB,CB) = S(AC) + S(CB) + 2R(AC,CB),
where 2R(AC,CB) means two copies of that rectangle. [CN2]

**Step 6.** Combining Steps 2 and 5 gives
S(AB) = S(AC) + S(CB) + 2R(AC,CB).
Therefore the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments, as required. [CN1]

**USED:** 2.2, 2.3, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.29, 1.31, 1.34, 1.46, 1.5, 1.6
**Jaccard:** 0.000 — AI adds ['2.2', '2.3', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.29', '1.31', '1.34', '1.46', '1.5', '1.6']

## Proposition 2.5
**Statement:** If a straight line be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the straight line between the points of section is equal to the square on the half.

**Step 1.** Let AB be bisected at C and cut unequally at D. Interchanging the names A and B if necessary, take the points in the order A, C, D, B; thus AC = CB. Write R(X,Y) for the rectangle contained by the lengths X and Y, and S(X) for the square on X; addition below means addition of areas. Interchanging the two containing sides names the same rectangle, and equal lengths may replace one another in these expressions. [D2.1, D1.22, CN4]

**Step 2.** Path choice: split the desired rectangle by 2.1, then use 2.3 to supply exactly the square on CD. Since AD is cut at C, applying 2.1 with DB as the uncut straight line gives
R(AD,DB) = R(AC,DB) + R(CD,DB).
Since AC = CB, this becomes
R(AD,DB) = R(CB,DB) + R(CD,DB). [2.1, CN4]

**Step 3.** Apply 2.3 to CB cut at D, choosing CD as the specified segment. The rectangle contained by the whole and CD equals the rectangle contained by the two segments together with the square on CD. Hence
R(CB,CD) = R(CD,DB) + S(CD). [2.3]

**Step 4.** Reuse 2.1 to split the square on CB: take one straight line equal to CB as uncut, and the other CB as cut at D. This is the natural choice because the same distributive rule already used in Step 2 gives the required decomposition directly. Since the rectangle contained by CB and CB is the square on CB,
S(CB) = R(CB,CD) + R(CB,DB). [2.1, D2.1, D1.22]

**Step 5.** Add S(CD) to both sides of the equality in Step 2, and substitute the equal areas from Steps 3 and 4. We obtain
R(AD,DB) + S(CD)
= R(CB,DB) + R(CD,DB) + S(CD)
= R(CB,DB) + R(CB,CD)
= S(CB). [CN2, CN1]
Thus the rectangle contained by the unequal segments AD and DB, together with the square on CD between the two points of section, equals the square on the half CB, as required.

**USED:** 2.1, 2.3, CN1, CN2, CN4, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', '2.3', 'CN1', 'CN2', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.6
**Statement:** If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

**Step 1.** Let AB be bisected at C, and let BD be added beyond B in the same straight line. Thus A, C, B, D occur in that order and AC = CB. We must prove that the rectangle contained by AD and BD, together with the square on AC, equals the square on CD. (Hypothesis.)

**Step 2.** Produce BA beyond A sufficiently far, and cut off AE equal to BD on the produced part. The points now occur in the order E, A, C, B, D. (P2, 1.3.) The chosen route is to apply 2.5: this equal extension will make C the midpoint of ED while A supplies its unequal division, giving the required rectangle directly.

**Step 3.** Since AC = CB and AE = BD, addition gives EC = CD. Hence ED is bisected at C. (CN2.) Moreover, AD is greater than its proper part BD, and BD = AE; therefore AD > AE, so A divides ED into unequal segments. (CN5.)

**Step 4.** Apply 2.5 to ED, divided equally at C and unequally at A. Its unequal segments are EA and AD, the straight line between the points of section is AC, and CD is half of ED. Consequently, the rectangle contained by EA and AD, together with the square on AC, equals the square on CD. (2.5.)

**Step 5.** Since EA = BD, the rectangle in Step 4 is a rectangle contained by AD and BD. (D2.1.) Therefore the rectangle contained by the whole extended line AD and the added line BD, together with the square on the half AC, equals the square on CD, which consists of the half CB and the added line BD. This is the required conclusion. (Step 4; hypothesis.)

**USED:** 1.3, 2.5, CN2, CN5, D2.1, P2
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['1.3', '2.5', 'CN2', 'CN5', 'D2.1', 'P2']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.7
**Statement:** If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

**Step 1.** Let AB be cut at C, and let AC be the selected segment. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. Sums denote areas taken together, and twice an area means two copies of it. [D1.22, D2.1]

**Step 2.** We choose the direct route through the established square decomposition, requiring no auxiliary construction. Applied to the given cut, it gives
S(AB) = S(AC) + S(CB) + 2R(AC,CB). [2.4]

**Step 3.** Add S(AC) to both sides. Thus
S(AB) + S(AC) = 2S(AC) + 2R(AC,CB) + S(CB). [CN2]

**Step 4.** The whole-and-segment identity applies directly to the selected segment, so we use it rather than derive another rectangle decomposition:
R(AB,AC) = S(AC) + R(AC,CB).
Adding this equality to itself gives
2R(AB,AC) = 2S(AC) + 2R(AC,CB). [2.3, CN2]

**Step 5.** Add S(CB) to both sides of the last equality. Its right-hand side is the same collection of areas as the right-hand side in Step 3. Consequently,
S(AB) + S(AC) = 2R(AB,AC) + S(CB).
Thus the squares on the whole and the selected segment together equal twice the rectangle contained by the whole and that segment together with the square on the remaining segment, as required. [CN2, CN1]

**USED:** 2.3, 2.4, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.3', '2.4', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.43', '1.46']

## Proposition 2.8
**Statement:** If a straight line be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one straight line.

**Step 1.** Let AB be cut at C, and take BC as the selected segment, so that AC is the remaining segment. Produce AB beyond B and mark D with BD equal to BC, using the circle with centre B and radius BC (P2, P3, D1.15). Thus AD is the whole AB together with BC laid in one straight line. Write S(XY) for the square on XY and R(XY,UV) for the rectangle contained by XY and UV; numerical coefficients denote repeated addition of areas (D1.22, D2.1).

**Step 2.** Path choice: apply 2.7 first to the given cut, since it supplies exactly the pair of squares that 2.4 will combine on the extended line. By 2.7, applied to AB cut at C with BC as the selected segment,
S(AB) + S(BC) = 2R(AB,BC) + S(AC).

**Step 3.** Apply 2.4 to AD cut at B:
S(AD) = S(AB) + S(BD) + 2R(AB,BD).
Since BD equals BC, the corresponding squares and rectangles are equal by coincidence (CN4). Consequently,
S(AD) = S(AB) + S(BC) + 2R(AB,BC) (CN1).

**Step 4.** Add 2R(AB,BC) to both sides of the equality in Step 2 (CN2):
S(AB) + S(BC) + 2R(AB,BC) = 4R(AB,BC) + S(AC).
Together with Step 3, this gives
S(AD) = 4R(AB,BC) + S(AC) (CN1).
Since AD consists of AB and a segment equal to BC laid in one straight line, four times the rectangle contained by the whole and the selected segment, together with the square on the remaining segment, equals the square on the whole and the selected segment taken as one straight line, as required.

**USED:** 2.4, 2.7, CN1, CN2, CN4, D1.15, D1.22, D2.1, P2, P3
**Human refs (from References field):** 1.36, 1.43
**Jaccard:** 0.000 — AI adds ['2.4', '2.7', 'CN1', 'CN2', 'CN4', 'D1.15', 'D1.22', 'D2.1', 'P2', 'P3']; Human adds ['1.36', '1.43']

## Proposition 2.9
**Statement:** If a straight line be cut into equal and unequal segments, the squares on the unequal segments of the whole are double of the square on the half and of the square on the straight line between the points of section.

**Step 1.** Let AB be bisected at C and cut unequally at D. Thus AC = CB. Write Q(XY) for the square on XY and R(XY,ZT) for the rectangle contained by XY and ZT, treating these as areas. A rectangle with equal adjacent sides is a square, and squares on equal segments are equal by coincidence. [Hypothesis; D1.22, D2.1, CN4]

**Step 2.** Apply 2.5, whose hypothesis matches exactly the two given cuts:
R(AD,DB) + Q(CD) = Q(AC).
Adding this equality to itself gives
2R(AD,DB) + 2Q(CD) = 2Q(AC).
This is the chosen route because it directly relates the rectangle contained by the unequal segments to the two squares required in the conclusion. [2.5, CN2]

**Step 3.** Use 2.4, the earliest available square-of-a-whole decomposition, on AB cut at C:
Q(AB) = Q(AC) + Q(CB) + 2R(AC,CB).
Since AC = CB, both Q(CB) and R(AC,CB) equal Q(AC). Hence
Q(AB) = 4Q(AC). [2.4, D1.22, D2.1, CN4, CN2]

**Step 4.** Apply 2.4 again, now to AB cut at D, and use Step 3:
Q(AD) + Q(DB) + 2R(AD,DB) = 4Q(AC).
Add 2Q(CD) to both sides. By Step 2, the resulting left side equals Q(AD) + Q(DB) + 2Q(AC). Therefore
Q(AD) + Q(DB) + 2Q(AC) = 4Q(AC) + 2Q(CD). [2.4, CN1, CN2]

**Step 5.** Subtract 2Q(AC) from both sides:
Q(AD) + Q(DB) = 2Q(AC) + 2Q(CD).
Thus the squares on the unequal segments are together double the square on the half and the square on the straight line between the points of section, as required. [CN3]

**USED:** 2.4, 2.5, CN1, CN2, CN3, CN4, D1.22, D2.1
**Human refs (from References field):** 1.29, 1.32, 1.34, 1.47, 1.6
**Jaccard:** 0.000 — AI adds ['2.4', '2.5', 'CN1', 'CN2', 'CN3', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.29', '1.32', '1.34', '1.47', '1.6']

## Proposition 2.10
**Statement:** If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

**Step 1.** Let AB be bisected at C, and let BD be added beyond B in the same straight line. Thus A, C, B, D occur in that order and AC = CB (hypothesis). Write S(XY) for the area of the square on XY; twice an area means its sum with itself [D1.22]. We must prove
S(AD) + S(BD) = 2S(AC) + 2S(CD).

**Step 2.** Path choice: use 2.9 by extending the line at the opposite end, so that its unequal segments become AD and a segment equal to BD. Produce BA beyond A sufficiently far, and cut off AE equal to BD on that production [P2, 1.3]. The points are therefore ordered E, A, C, B, D.

**Step 3.** Since EA = BD and AC = CB, addition of equals gives
EC = EA + AC = BD + CB = CD [CN2].
Hence C bisects ED. Moreover, AD is greater than its part BD, which equals EA; therefore AD > EA, and A divides ED into unequal segments [CN5].

**Step 4.** Apply 2.9 to ED, bisected at C and divided unequally at A. Its unequal segments are EA and AD, a half is CD, and the straight line between the points of section is AC. Consequently,
S(EA) + S(AD) = 2S(CD) + 2S(AC) [2.9].

**Step 5.** Since EA = BD, the squares on EA and BD coincide upon superposition and are equal [D1.22, CN4]. Adding S(AD) to these equal areas and using the equality in Step 4 gives
S(AD) + S(BD) = 2S(AC) + 2S(CD) [CN2, CN1].
Here AD is the original whole with the added straight line, AC is its original half, and CD consists of the other equal half CB together with BD. Thus the square on the whole with the addition and the square on the addition together are double the square on the half and the square on the half together with the addition, as required.

**USED:** 1.3, 2.9, CN1, CN2, CN4, CN5, D1.22, P2
**Human refs (from References field):** 1.11, 1.15, 1.29, 1.3, 1.31, 1.32, 1.34, 1.47, 1.5, 1.6, CN1, P5
**Jaccard:** 0.111 — AI adds ['2.9', 'CN2', 'CN4', 'CN5', 'D1.22', 'P2']; Human adds ['1.11', '1.15', '1.29', '1.31', '1.32', '1.34', '1.47', '1.5', '1.6', 'P5']

## Proposition 2.11
**Statement:** To cut a given straight line so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.

**Step 1.** Write S(XY) for the square on XY, and R(XY,ZW) for the rectangle contained by XY and ZW [D1.22, D2.1]. Bisect the given straight line AB at M [1.10]. Produce AB beyond B and erect a perpendicular at B; on this perpendicular, extended sufficiently, cut off BC equal to AB [P2, 1.11, 1.3]. Join MC [P1].

**Step 2.** Triangle MBC is right-angled at B. Its angle at C is less than a right angle [1.17], so MC, opposite the right angle, is greater than MB [1.19]. The triangle inequality also gives MC < MB + BC = MB + AB [1.20]. Thus MB < MC < MB + AB.

**Step 3.** On AB produced, take D so that MD = MC, extending the line sufficiently and cutting off the required length from M [P2, 1.3]. The inequalities in Step 2 ensure that D is beyond B and that 0 < BD < AB. Therefore cut off AH equal to BD from AB; H lies strictly between A and B [1.3].

**Step 4.** Path choice: use 2.6 because AB is bisected at M and extended by BD; this proposition gives the needed rectangle directly. It yields
R(AD,BD) + S(MB) = S(MD) [2.6].

**Step 5.** By the theorem on the square opposite the right angle in triangle MBC,
S(MC) = S(MB) + S(BC) [1.47].
Since MD = MC and BC = AB, the corresponding squares are equal by coincidence [CN4]. Combining this equality with Step 4 gives
R(AD,BD) + S(MB) = S(MB) + S(AB) [CN1].
Subtracting S(MB), we obtain
R(AD,BD) = S(AB) [CN3].

**Step 6.** Apply 2.3 to AD cut at B: it is the direct choice because it already separates off the square on BD. Thus
R(AD,BD) = R(AB,BD) + S(BD) [2.3].
Since AH = BD, substitution of equal sides in the corresponding rectangles and squares, followed by Step 5, gives
R(AB,AH) + S(AH) = S(AB) [CN4, CN1].

**Step 7.** Apply the square-of-the-whole decomposition to AB cut at H:
R(AB,AH) + R(AB,HB) = S(AB) [2.2].
Compare this with Step 6 and subtract the common rectangle R(AB,AH) [CN1, CN3]. The result is
R(AB,HB) = S(AH).
Therefore AB has been cut at H so that the rectangle contained by the whole AB and the segment HB equals the square on the remaining segment AH, as required.

**USED:** 1.10, 1.11, 1.17, 1.19, 1.20, 1.3, 1.47, 2.2, 2.3, 2.6, CN1, CN3, CN4, D1.22, D2.1, P1, P2
**Human refs (from References field):** 1.46, 1.47, 2.6
**Jaccard:** 0.111 — AI adds ['1.10', '1.11', '1.17', '1.19', '1.20', '1.3', '2.2', '2.3', 'CN1', 'CN3', 'CN4', 'D1.22', 'D2.1', 'P1', 'P2']; Human adds ['1.46']

## Proposition 2.12
**Statement:** In obtuse-angled triangles the square on the side subtending the obtuse angle is greater than the squares on the sides containing the obtuse angle by twice the rectangle contained by one of the sides about the obtuse angle, namely that on which the   perpendicular falls, and the straight line cut off outside by the perpendicular towards the obtuse angle.

**Step 1.** Let ABC be a triangle whose angle ABC is obtuse. Write Q(XY) for the square on XY and R(XY, ZW) for the rectangle contained by XY and ZW (D1.22, D2.1). Produce the straight line AB as necessary, and draw CD perpendicular to it, meeting it at D (P2, 1.12).

**Step 2.** The point D lies beyond B, so the order is A, B, D. For D cannot coincide with B, since angle ABC would then be right (D1.10), contrary to its being obtuse (D1.11). If D lay on the ray from B through A, angle CBD would be the obtuse angle CBA, while angle BDC would be right (D1.10). This contradicts 1.17, since two angles of a triangle are together less than two right angles, whereas an obtuse angle together with a right angle exceeds two right angles (D1.11). Thus BD is the segment cut off outside AB towards the obtuse angle.

**Step 3.** Apply 2.4 to the whole AD cut at B:
Q(AD) = Q(AB) + Q(BD) + 2R(AB, BD).
This is the direct path: 2.4 is the natural first choice because the whole AD is already divided into precisely the two segments required in the rectangle.

**Step 4.** Since CD is perpendicular to AD, triangles ACD and BCD are right-angled at D (D1.10). Therefore, by 1.47 applied to each triangle,
Q(AC) = Q(AD) + Q(CD),
and
Q(BC) = Q(BD) + Q(CD).

**Step 5.** Add Q(CD) to both sides of the equality in Step 3 (CN2):
Q(AD) + Q(CD) = Q(AB) + Q(BD) + Q(CD) + 2R(AB, BD).
Using the two equalities of Step 4 gives
Q(AC) = Q(AB) + Q(BC) + 2R(AB, BD)
(CN1, CN2).

**Step 6.** The rectangle contained by the nonzero segments AB and BD is a nonzero area. Hence the square on AC is greater than the squares on AB and BC together by exactly twice that rectangle (Step 5, CN5). Here AC subtends the obtuse angle, AB is the side containing that angle on whose produced line the perpendicular falls, and BD is the segment cut off outside towards the obtuse angle. This proves the proposition.

**USED:** 1.12, 1.17, 1.47, 2.4, CN1, CN2, CN5, D1.10, D1.11, D1.22, D2.1, P2
**Human refs (from References field):** 1.47, 2.4
**Jaccard:** 0.167 — AI adds ['1.12', '1.17', 'CN1', 'CN2', 'CN5', 'D1.10', 'D1.11', 'D1.22', 'D2.1', 'P2']

## Proposition 2.13
**Statement:** In acute-angled triangles the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle by twice the rectangle contained by one of the sides about the acute angle, namely that on which the perpendicular falls, and the straight line cut off within by the perpendicular towards the acute angle.

**Step 1.** Let ABC be an acute-angled triangle, and consider the angle BAC, opposite the side BC. All three angles are acute (D1.21). Write XY² for the square on XY, and R(XY, ZW) for the rectangle contained by XY and ZW (D1.22, D2.1).

**Step 2.** Produce AB as necessary and draw CD perpendicular to its straight line, meeting it at D (P2, 1.12). The point D lies strictly between A and B. Indeed, if D coincided with either endpoint, the angle of ABC at that endpoint would be right, contrary to its being acute (D1.10, D1.12). If D lay beyond A, then BAC would be an exterior angle of triangle CAD and hence greater than the right angle CDA (1.16). If D lay beyond B, then ABC would be an exterior angle of triangle CBD and hence greater than the right angle CDB (1.16). Both alternatives contradict acuteness (D1.12). Thus D is internal, and both CDA and CDB are right angles (D1.10).

**Step 3.** Apply 2.7 to AB cut at D, taking AD as the specified segment. It gives
AB² + AD² = 2R(AB, AD) + DB².
This is the direct choice because its rectangle already contains the whole side AB and the segment AD cut off toward the chosen angle (2.7).

**Step 4.** Apply the theorem on the square opposite a right angle to triangles ADC and BDC. We obtain
AC² = AD² + CD²,
and
BC² = DB² + CD² (1.47).

**Step 5.** Add CD² to both sides of the equality in Step 3 (CN2):
AB² + AD² + CD² = 2R(AB, AD) + DB² + CD².
Substituting the equal areas from Step 4 gives
AB² + AC² = 2R(AB, AD) + BC² (CN1).

**Step 6.** Since D lies strictly between A and B, the rectangle R(AB, AD) is a nonzero area. Therefore the square on BC is less than the squares on AB and AC together (CN5), and the equality in Step 5 shows that the deficiency is exactly twice the rectangle contained by AB and AD. Here AB is the side on which the perpendicular falls, and AD is the segment cut off within it toward the acute angle BAC. This proves the proposition.

**USED:** 1.12, 1.16, 1.47, 2.7, CN1, CN2, CN5, D1.10, D1.12, D1.21, D1.22, D2.1, P2
**Human refs (from References field):** 1.47, 2.7
**Jaccard:** 0.154 — AI adds ['1.12', '1.16', 'CN1', 'CN2', 'CN5', 'D1.10', 'D1.12', 'D1.21', 'D1.22', 'D2.1', 'P2']

## Proposition 2.14
**Statement:** To construct a square equal to a given rectilineal figure.

**Step 1.** Let G be the given rectilineal figure. Construct a right angle (1.11), and construct a parallelogram ABCD equal in area to G with that prescribed angle (1.45). Opposite angles of a parallelogram are equal, and adjacent angles together equal two right angles; hence all its angles are right (1.34, 1.29, CN3). Thus ABCD is a rectangle. This is the direct reduction supplied by 1.45.

**Step 2.** If AB = BC, the opposite sides are also equal (1.34), so ABCD is equilateral and right-angled, and therefore is the required square (D1.22). Otherwise, label the rectangle so that AB > BC.

**Step 3.** Produce AB beyond B to E, making BE = BC (P2, 1.3). Bisect AE at O (1.10). Since AB > BE and AO = OE, O lies between A and B. Thus the points occur in the order A, O, B, E.

**Step 4.** Describe the circle with centre O and radius OE (P3). At B erect a perpendicular to AE and produce it to meet the circle at F (1.11, P2). Here B is inside the circle, since OB < OE (CN5). Join OF (P1). The radii OF and OE are equal (D1.15), and angle OBF is right by the perpendicular construction (1.11).

**Step 5.** AE is divided equally at O and unequally at B. Therefore the rectangle contained by AB and BE, together with the square on OB, equals the square on OE (2.5). The equal and unequal divisions make 2.5 the natural identity to use directly.

**Step 6.** In the right-angled triangle OBF, the square on OF equals the squares on OB and BF together (1.47). Since OF = OE, the squares on them are equal (CN4). Consequently, the square on OE equals the squares on OB and BF together (CN1).

**Step 7.** Comparing Steps 5 and 6 and subtracting the common square on OB, the rectangle contained by AB and BE equals the square on BF (CN1, CN3). Because BE = BC, that rectangle equals ABCD (D2.1, CN4). Since ABCD equals G, the square on BF also equals G (CN1).

**Step 8.** Construct the square on BF (1.46). By Step 7 it is equal in area to the given rectilineal figure G. Thus the required square has been constructed.

**USED:** 1.10, 1.11, 1.29, 1.3, 1.34, 1.45, 1.46, 1.47, 2.5, CN1, CN3, CN4, CN5, D1.15, D1.22, D2.1, P1, P2, P3
**Human refs (from References field):** 1.45, 1.47, 2.5
**Jaccard:** 0.158 — AI adds ['1.10', '1.11', '1.29', '1.3', '1.34', '1.46', 'CN1', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.22', 'D2.1', 'P1', 'P2', 'P3']
