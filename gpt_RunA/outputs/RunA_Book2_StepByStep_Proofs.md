# Book 2 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 2.1
**Statement:** If there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments.

**Step 1.** Let UV be the uncut straight line, and let the other straight line A₀Aₙ be divided at A₁, …, Aₙ₋₁ into any finite number n of consecutive segments. By D2.1, a rectangle is contained by its two adjacent sides. Our path is direct dissection: construct one rectangle and divide it into rectangles corresponding to the given segments. [D2.1]

**Step 2.** At A₀ erect a perpendicular to A₀Aₙ, producing the base through A₀ if necessary. On this perpendicular take A₀B₀ equal to UV, first producing the perpendicular sufficiently far and then cutting off the required length. Thus angle B₀A₀Aₙ is right and A₀B₀ = UV. [P2, 1.11, 1.3, D1.10]

**Step 3.** Through B₀ draw a straight line h parallel to A₀Aₙ. Through each Aᵢ, for i = 1, …, n, draw a straight line parallel to A₀B₀, meeting h at Bᵢ. These intersections exist: otherwise one of these lines would be parallel to h, and, being also parallel to A₀B₀, would imply that h and A₀B₀ are parallel, although they meet at B₀. [1.31, D1.23, 1.30]

**Step 4.** The outer quadrilateral A₀AₙBₙB₀ has both pairs of opposite sides parallel. The same is true of every strip Aᵢ₋₁AᵢBᵢBᵢ₋₁, since its two transverse sides are parallel to A₀B₀ and therefore parallel to one another. Because A₀B₀ is perpendicular to the base, the angle relations for parallel lines show that all the angles of the outer quadrilateral and of every strip are right. Hence they are rectangular parallelograms. [1.30, 1.29, D1.10]

**Step 5.** For each i = 1, …, n, the quadrilateral A₀AᵢBᵢB₀ is a parallelogram. Its opposite sides are equal, so AᵢBᵢ = A₀B₀ = UV. Together with the constructed equality A₀B₀ = UV, this shows that every strip has its transverse side equal to UV. Opposite-side equality is the natural tool here because the required sides already belong to the constructed parallelograms. [1.34, CN1]

**Step 6.** Consequently, the outer rectangle is the rectangle contained by UV and A₀Aₙ. For each i, the strip Aᵢ₋₁AᵢBᵢBᵢ₋₁ is the rectangle contained by UV and Aᵢ₋₁Aᵢ. [D2.1; Steps 2 and 5]

**Step 7.** The parallel dividing lines do not meet one another. Thus the consecutive strips have disjoint interiors and together coincide exactly with the outer rectangle. The outer rectangle therefore equals these strips taken together; replacing each strip by its identification in Step 6 and adding the equal areas gives

rectangle(UV, A₀Aₙ) = rectangle(UV, A₀A₁) + rectangle(UV, A₁A₂) + ⋯ + rectangle(UV, Aₙ₋₁Aₙ).

Since the number and positions of the divisions were arbitrary, the rectangle contained by the two given straight lines equals the rectangles contained by the uncut straight line and each of the segments, taken together. [D1.23, CN4, CN2]

**USED:** 1.11, 1.29, 1.3, 1.30, 1.31, 1.34, CN1, CN2, CN4, D1.10, D1.23, D2.1, P2
**Human refs (from References field):** 1.11, 1.3, 1.31, 1.34
**Jaccard:** 0.308 — AI adds ['1.29', '1.30', 'CN1', 'CN2', 'CN4', 'D1.10', 'D1.23', 'D2.1', 'P2']

## Proposition 2.2
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and both of the segments is equal to the square on the whole.

**Step 1.** Let the straight line AB be cut at an arbitrary interior point C. Construct the square ABDE on AB [1.46]. Its adjacent sides AB and AE are equal, and its angles are right angles [D1.22].

**Step 2.** Write R(X,Y) for the rectangle contained by the straight lines X and Y [D2.1]. Choose the direct specialization of 2.1: take AE as the uncut straight line and AB as the straight line cut into AC and CB. This gives
R(AE,AB) = R(AE,AC) + R(AE,CB) [2.1],
where the sum denotes the two rectangular areas taken together. This route applies the preceding proposition directly, without a further dissection.

**Step 3.** The rectangle R(AE,AB) is the square ABDE, since AE and AB are its adjacent sides. Moreover, AE = AB, so R(AE,AC) and R(AE,CB) are respectively the rectangles contained by AB, AC and by AB, CB [D2.1; D1.22]. Thus the equality in Step 2 says that the rectangles contained by the whole AB and each of its two segments, taken together, equal the square on AB. This is the required conclusion [2.1].

**USED:** 1.46, 2.1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.200 — AI adds ['2.1', 'D1.22', 'D2.1']; Human adds ['1.31']

## Proposition 2.3
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and one of the segments is equal to the rectangle contained by the segments and the square on the aforesaid segment.

**Step 1.** Let AB be cut at an arbitrary interior point C, and take BC as the aforesaid segment. Write R(X,Y) for the area of the rectangle contained by X and Y; naming these two adjacent sides in the opposite order names the same rectangle [D2.1]. Path choice: apply 2.1 directly, since it already gives the required division into rectangles, with BC as the uncut straight line [2.1].

**Step 2.** Apply 2.1 to the straight lines BC and AB, the latter being cut at C. It gives
R(AB,BC) = R(AC,BC) + R(BC,BC),
where the sum denotes the two areas taken together [2.1, D2.1].

**Step 3.** In R(BC,BC), the two sides containing a right angle both equal BC [D2.1]. The opposite sides of this parallelogram are respectively equal, so all four sides equal BC [1.34]. Being equilateral and right-angled, this rectangle is a square on BC. Thus, writing S(BC) for the area of that square, R(BC,BC) = S(BC) [D1.22].

**Step 4.** Add R(AC,BC) to both sides of the equality in Step 3 [CN2], and combine the resulting equality with Step 2 [CN1]. Therefore
R(AB,BC) = R(AC,BC) + S(BC).
Hence the rectangle contained by the whole and the chosen segment equals the rectangle contained by the two segments together with the square on the chosen segment, as required.

**USED:** 1.34, 2.1, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.000 — AI adds ['1.34', '2.1', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.31', '1.46']

## Proposition 2.4
**Statement:** If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.

**Step 1.** Let the straight line AB be cut at an arbitrary interior point C. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW. The order of the two containing sides does not change the rectangle: R(XY,ZW) = R(ZW,XY). [D1.22, D2.1]

**Step 2.** By 2.2, the square on AB equals the rectangles contained by AB and each of its segments:
S(AB) = R(AB,AC) + R(AB,CB).
Path choice: use 2.2 because it directly decomposes the square required in the conclusion, then use 2.3 on each resulting rectangle. [2.2]

**Step 3.** Apply 2.3 to AB cut at C, taking AC as the specified segment. Then
R(AB,AC) = S(AC) + R(AC,CB). [2.3]

**Step 4.** Apply 2.3 to the same cut, now taking CB as the specified segment. Then
R(AB,CB) = S(CB) + R(CB,AC) = S(CB) + R(AC,CB). [2.3, D2.1]

**Step 5.** Add the equalities of Steps 3 and 4, and use Step 2. Thus
S(AB) = S(AC) + S(CB) + R(AC,CB) + R(AC,CB).
Consequently, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments, as required. [CN2, CN1]

**USED:** 2.2, 2.3, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.29, 1.31, 1.34, 1.46, 1.5, 1.6
**Jaccard:** 0.000 — AI adds ['2.2', '2.3', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.29', '1.31', '1.34', '1.46', '1.5', '1.6']

## Proposition 2.5
**Statement:** If a straight line be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the straight line between the points of section is equal to the square on the half.

**Step 1.** Let AB be cut equally at C and unequally at D, so AC = CB. Interchanging the names of the endpoints if necessary, suppose the points occur in the order A, C, D, B. Write R(p,q) for the rectangle contained by segments p and q, and S(p) for the square on p. Thus R(p,p) = S(p); the containing sides may be interchanged, and equal segments give equal corresponding rectangles by coincidence. (D1.22, D2.1, CN4.)

**Step 2.** Path choice: use 2.1, the earliest applicable rectangle-distribution result, throughout, treating the square as a rectangle with equal sides. Apply it with the uncut segment CB and with CB cut at D. We obtain
S(CB) = R(CB,CD) + R(CB,DB).
(2.1, D1.22, D2.1.)

**Step 3.** Apply the same distribution result with the uncut segment CD and with CB cut at D. Then
R(CB,CD) = R(CD,CD) + R(DB,CD)
= S(CD) + R(CD,DB).
(2.1, D1.22, D2.1, CN4.)

**Step 4.** Add R(CB,DB) to the equality in Step 3 and use Step 2. It follows that
S(CB) = S(CD) + R(CD,DB) + R(CB,DB).
(CN2, CN1.)

**Step 5.** Apply rectangle distribution with the uncut segment DB and with AD cut at C. Since AC = CB,
R(AD,DB) = R(AC,DB) + R(CD,DB)
= R(CB,DB) + R(CD,DB).
(2.1; the hypothesis AC = CB; CN4, CN2.)

**Step 6.** Add S(CD) to the equality in Step 5. The resulting sum is exactly the sum equal to S(CB) in Step 4. Therefore
R(AD,DB) + S(CD) = S(CB).
(CN2, CN1.) Here AD and DB are the unequal segments, CD is the straight line between the points of section, and CB is half of AB. Hence the rectangle contained by the unequal segments, together with the square on the line between the points of section, equals the square on the half, as required.

**USED:** 2.1, CN1, CN2, CN4, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', 'CN1', 'CN2', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.6
**Statement:** If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

**Step 1.** Let AB be bisected at C, and let BD be added in the same straight line beyond B. Thus A, C, B, D occur in that order, and AC = CB by hypothesis. Write R(X,Y) for the area of the rectangle contained by X and Y, and S(X) for the area of the square on X (D2.1, D1.22). Sums and doublings below refer to areas.

**Step 2.** Choose the direct three-part dissection: the given points divide AD into AC, CB, and BD, so 2.1 applies without any auxiliary construction. Applying it with BD as the uncut straight line gives
R(AD,BD) = R(AC,BD) + R(CB,BD) + S(BD),
where the rectangle contained by BD and BD is the square on BD (2.1, D1.22).

**Step 3.** Since AC = CB, the rectangles contained by AC, BD and by CB, BD coincide upon superposition and are equal (CN4). Substituting these equal areas in Step 2 therefore gives
R(AD,BD) = 2R(CB,BD) + S(BD)
(CN2).

**Step 4.** The straight line CD is cut at B into CB and BD. Hence
S(CD) = S(CB) + S(BD) + 2R(CB,BD)
by 2.4.

**Step 5.** Add S(CB) to both sides of the equality in Step 3 (CN2). Its right-hand side is precisely the sum of areas equal to S(CD) in Step 4. Consequently,
R(AD,BD) + S(CB) = S(CD)
(CN1). Here AD is the whole with the added straight line, BD is the added straight line, CB is the half, and CD consists of that half together with the added straight line. This is the required conclusion.

**USED:** 2.1, 2.4, CN1, CN2, CN4, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', '2.4', 'CN1', 'CN2', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.7
**Statement:** If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

**Step 1.** Let AB be cut at an arbitrary interior point C, and let AC be the specified segment. Write S(X) for the square on a segment X and R(X,Y) for the rectangle contained by segments X and Y, regarding these figures as areas; write 2T for T + T. [D1.22, D2.1] Path choice: use 2.4 to decompose the square on the whole, then 2.3 to identify the square-and-rectangle pair. The latter directly matches the required rectangle, without a further subdivision construction.

**Step 2.** By 2.4,
S(AB) = S(AC) + S(CB) + 2R(AC,CB).
Add S(AC) to both sides. Grouping the resulting areas into two identical pairs gives
S(AB) + S(AC) = S(CB) + [S(AC) + R(AC,CB)] + [S(AC) + R(AC,CB)]. [2.4, CN2]

**Step 3.** Applied to the same cut and the specified segment AC, 2.3 gives
R(AB,AC) = S(AC) + R(AC,CB).
Adding this equality to itself therefore gives
2R(AB,AC) = [S(AC) + R(AC,CB)] + [S(AC) + R(AC,CB)]. [2.3, CN2]

**Step 4.** Add S(CB) to both sides of the equality in Step 3. Its right-hand side is now the same collection of areas as the right-hand side in Step 2. Hence
S(AB) + S(AC) = 2R(AB,AC) + S(CB). [CN2, CN1]
Thus the square on the whole and the square on the specified segment together equal twice the rectangle contained by the whole and that segment, together with the square on the remaining segment. Since the specified segment was arbitrary, the proposition is proved.

**USED:** 2.3, 2.4, CN1, CN2, D1.22, D2.1
**Human refs (from References field):** 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.3', '2.4', 'CN1', 'CN2', 'D1.22', 'D2.1']; Human adds ['1.43', '1.46']

## Proposition 2.8
**Statement:** If a straight line be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one straight line.

**Step 1.** Let AB be cut at an arbitrary interior point C, and designate BC as the aforesaid segment; AC is the remaining segment. For straight-line lengths x and y, write S(x) for the square on x and R(x,y) for the rectangle contained by x and y. Multiples of areas mean repeated sums. [D1.22, D2.1]

**Step 2.** Produce AB sufficiently beyond B, and cut off BD equal to BC on the produced part. Thus AD consists of the whole AB and the designated segment BC placed together on one straight line. [P2, 1.3]

**Step 3.** Apply 2.4 to AD cut at B. Since BD equals BC,
S(AD) = S(AB) + S(BC) + 2R(AB,BC).
This is the direct path choice: expanding the required square first produces exactly the pair of squares to which the relation for the original cut will apply. [2.4]

**Step 4.** Apply 2.7 to AB cut at C, taking BC as the specified segment. It gives
S(AB) + S(BC) = 2R(AB,BC) + S(AC). [2.7]

**Step 5.** Add 2R(AB,BC) to both sides of the equality in Step 4. Then
S(AB) + S(BC) + 2R(AB,BC) = 4R(AB,BC) + S(AC). [CN2]
Comparing with Step 3 yields
4R(AB,BC) + S(AC) = S(AD). [CN1]
Since AD is the whole AB together with BC on one straight line, four times the rectangle contained by the whole and the designated segment, together with the square on the remaining segment, equals the square on the whole and the designated segment taken as one straight line, as required.

**USED:** 1.3, 2.4, 2.7, CN1, CN2, D1.22, D2.1, P2
**Human refs (from References field):** 1.36, 1.43
**Jaccard:** 0.000 — AI adds ['1.3', '2.4', '2.7', 'CN1', 'CN2', 'D1.22', 'D2.1', 'P2']; Human adds ['1.36', '1.43']

## Proposition 2.9
**Statement:** If a straight line be cut into equal and unequal segments, the squares on the unequal segments of the whole are double of the square on the half and of the square on the straight line between the points of section.

**Step 1.** Let AB be cut equally at C and unequally at D, so AC = CB. Write Q(XY) for the area of the square on XY, and R for the area of the rectangle contained by AD and DB; numerical multiples denote repeated addition (D1.22, D2.1). We use 2.4 to decompose the square on AB at each cut, and 2.5 because it applies directly to the given equal and unequal cuts, without auxiliary construction.

**Step 2.** Since AC = CB, the squares on AC and CB are equal, and the rectangle contained by AC and CB equals the square on AC (D1.22, D2.1, CN4). Applying 2.4 to AB cut at C therefore gives
Q(AB) = Q(AC) + Q(CB) + 2Q(AC) = 4Q(AC).
(Citations: 2.4, CN2.)

**Step 3.** Applying 2.4 to AB cut at D gives
Q(AD) + Q(DB) + 2R = Q(AB).
Together with Step 2, this yields
Q(AD) + Q(DB) + 2R = 4Q(AC).
(Citations: 2.4, CN1.)

**Step 4.** Since C and D are respectively the equal and unequal points of section, 2.5 gives
R + Q(CD) = Q(AC).
Adding this equality to itself yields
2R + 2Q(CD) = 2Q(AC).
(Citations: 2.5, CN2.)

**Step 5.** Add 2Q(CD) to both sides of the equality in Step 3. Replacing 2R + 2Q(CD) by its equal from Step 4 gives
Q(AD) + Q(DB) + 2Q(AC) = 4Q(AC) + 2Q(CD).
(Citations: CN2, CN1.)

**Step 6.** Subtract 2Q(AC) from both sides. Then
Q(AD) + Q(DB) = 2Q(AC) + 2Q(CD).
Thus the squares on the unequal segments together are double the square on the half together with the square on the straight line between the points of section, as required. (Citation: CN3.)

**USED:** 2.4, 2.5, CN1, CN2, CN3, CN4, D1.22, D2.1
**Human refs (from References field):** 1.29, 1.32, 1.34, 1.47, 1.6
**Jaccard:** 0.000 — AI adds ['2.4', '2.5', 'CN1', 'CN2', 'CN3', 'CN4', 'D1.22', 'D2.1']; Human adds ['1.29', '1.32', '1.34', '1.47', '1.6']

## Proposition 2.10
**Statement:** If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

**Step 1.** Let AB be bisected at C, and let BD be added beyond B in the same straight line. Thus A, C, B, D occur in this order and AC = CB (hypothesis). Write S(XY) for the square on XY. Our path is to use **2.9**, since an extension at the opposite end will make the required squares correspond to the unequal segments of a bisected line.

**Step 2.** Produce BA beyond A and take E on this extension so that AE = BD. The points therefore occur in the order E, A, C, B, D. This construction is permitted by **P2** and **1.3**.

**Step 3.** Since AE = BD and AC = CB, adding equals gives
EC = EA + AC = BD + CB = CD (**CN2**).
Hence ED is bisected at C. Moreover, AD is greater than its part BD, and BD = EA; therefore AD is greater than EA (**CN5**). Thus A cuts ED into unequal segments EA and AD.

**Step 4.** Apply **2.9** to ED, bisected at C and cut unequally at A. The straight line between its points of section is AC, so
S(EA) + S(AD) = 2S(EC) + 2S(AC).

**Step 5.** Squares on equal straight lines coincide upon superposition: their sides are equal and their corresponding right angles are equal (**D1.22**, **P4**); consequently their areas are equal (**CN4**). Since EA = BD and EC = CD, substitute these equal squares in Step 4 (**CN1**, **CN2**) to obtain
S(AD) + S(BD) = 2S(CD) + 2S(AC).
Here AD is the whole AB together with the added line BD, while CD is the half CB together with BD. Thus the squares on the whole with the added line and on the added line are together double the squares on the half and on the half together with the added line, as required.

**USED:** 1.3, 2.9, CN1, CN2, CN4, CN5, D1.22, P2, P4
**Human refs (from References field):** 1.11, 1.15, 1.29, 1.3, 1.31, 1.32, 1.34, 1.47, 1.5, 1.6, CN1, P5
**Jaccard:** 0.105 — AI adds ['2.9', 'CN2', 'CN4', 'CN5', 'D1.22', 'P2', 'P4']; Human adds ['1.11', '1.15', '1.29', '1.31', '1.32', '1.34', '1.47', '1.5', '1.6', 'P5']

## Proposition 2.11
**Statement:** To cut a given straight line so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.

**Step 1.** Let AB be the given straight line. Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW, regarding these as areas [D1.22, D2.1]. Construct the square ABCD, bisect AD at E, and join EB. Then AD = AB, AE = ED, and angle EAB is right [1.46, D1.22, 1.10, P1].

**Step 2.** In triangle EAB, the angles at A and B together are less than two right angles. Since the angle at A is right, the angle at B is smaller than it; consequently EB > EA [1.17, P4, 1.19]. Also, the triangle inequality gives EB < EA + AB [1.20].

**Step 3.** Produce DA beyond A. Describe the circle with centre E and radius EB, and let F be its intersection with the ray from E through A. Since EB > EA, F lies beyond A, and EF = EB [P2, P3, D1.15]. Thus EF = EA + AF. Moreover, AF < AB: otherwise adding EA would give EF ≥ EA + AB, contrary to Step 2 [CN2, CN5]. Cut off AH equal to AF from AB; H therefore lies strictly between A and B [1.3].

**Step 4.** The straight line DA is bisected at E and extended by AF. Hence
R(DF,AF) + S(EA) = S(EF)
[2.6]. This is the direct path: the construction gives precisely a bisected line with an added straight line, the configuration of 2.6.

**Step 5.** Since triangle EAB is right-angled at A,
S(EB) = S(EA) + S(AB)
[1.47]. Because EF = EB, their squares are equal by superposition [P4, CN4]. Comparing this equality with Step 4 and subtracting S(EA) gives
R(DF,AF) = S(AB)
[CN1, CN3].

**Step 6.** Apply 2.1 to the uncut line AF and the line DF cut at A. It gives
R(DF,AF) = R(AD,AF) + S(AF)
[2.1, D1.22, D2.1]. We choose 2.1 as the first available distribution rule: it directly separates the rectangle at A. Since AD = AB and AF = AH, the corresponding rectangles and squares are equal by superposition [P4, CN4]. Therefore Step 5 becomes
R(AB,AH) + S(AH) = S(AB)
[CN1].

**Step 7.** Apply the same distribution rule to AB and its division at H. The rectangle contained by AB and itself is its square, so
R(AB,AH) + R(AB,HB) = S(AB)
[2.1, D1.22, D2.1].

**Step 8.** The sums in Steps 6 and 7 are equal to the same square. Subtracting their common rectangle R(AB,AH), we obtain
R(AB,HB) = S(AH)
[CN1, CN3]. Thus AB has been cut at H so that the rectangle contained by the whole AB and the segment HB equals the square on the remaining segment AH, as required.

**USED:** 1.10, 1.17, 1.19, 1.20, 1.3, 1.46, 1.47, 2.1, 2.6, CN1, CN2, CN3, CN4, CN5, D1.15, D1.22, D2.1, P1, P2, P3, P4
**Human refs (from References field):** 1.46, 1.47, 2.6
**Jaccard:** 0.143 — AI adds ['1.10', '1.17', '1.19', '1.20', '1.3', '2.1', 'CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.15', 'D1.22', 'D2.1', 'P1', 'P2', 'P3', 'P4']

## Proposition 2.12
**Statement:** In obtuse-angled triangles the square on the side subtending the obtuse angle is greater than the squares on the sides containing the obtuse angle by twice the rectangle contained by one of the sides about the obtuse angle, namely that on which the   perpendicular falls, and the straight line cut off outside by the perpendicular towards the obtuse angle.

**Step 1.** Let ABC be a triangle whose angle ABC is obtuse, so that AC subtends the obtuse angle (D1.21, D1.11). Write S(XY) for the square on XY and R(XY,ZW) for the rectangle contained by XY and ZW, regarding these figures as areas (D1.22, D2.1).

**Step 2.** Produce AB as necessary, and from C draw CD perpendicular to the straight line AB, meeting it at D (P2, 1.12).

**Step 3.** The point D lies beyond B, so that A, B, D occur in that order. For D cannot coincide with B, since then ABC would be right rather than obtuse (D1.10, D1.11). Nor can D lie on the ray from B through A: in that case angle CBD would be the given obtuse angle, while angle CDB would be right, contrary to 1.17, which says that any two angles of a triangle are together less than two right angles (D1.10, D1.11, 1.17). Thus B lies between A and D.

**Step 4.** Direct path choice: apply 2.4 to AD cut at B, since this immediately supplies the required twice-rectangle term. It gives
S(AD) = S(AB) + S(BD) + 2R(AB,BD).
(2.4.)

**Step 5.** Since CD is perpendicular to AD, triangles ACD and BCD are right-angled at D (D1.10). Therefore
S(AC) = S(AD) + S(CD),
and
S(BC) = S(BD) + S(CD).
(1.47.)

**Step 6.** Add S(CD) to both sides of the equality in Step 4 (CN2). Substituting the two equalities from Step 5 gives
S(AC) = S(AB) + S(BC) + 2R(AB,BD).
(CN1, CN2.)

**Step 7.** Hence the square on AC is greater than the squares on AB and BC together by precisely twice the rectangle contained by AB and BD (CN5, D2.1). Here AB is the side containing the obtuse angle on whose continuation the perpendicular falls, and BD is the straight line cut off outside that side towards the obtuse vertex B, as established in Step 3. This is the required conclusion.

**USED:** 1.12, 1.17, 1.47, 2.4, CN1, CN2, CN5, D1.10, D1.11, D1.21, D1.22, D2.1, P2
**Human refs (from References field):** 1.47, 2.4
**Jaccard:** 0.154 — AI adds ['1.12', '1.17', 'CN1', 'CN2', 'CN5', 'D1.10', 'D1.11', 'D1.21', 'D1.22', 'D2.1', 'P2']

## Proposition 2.13
**Statement:** In acute-angled triangles the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle by twice the rectangle contained by one of the sides about the acute angle, namely that on which the perpendicular falls, and the straight line cut off within by the perpendicular towards the acute angle.

**Step 1.** Let ABC be an acute-angled triangle, and take ABC as the acute angle under consideration; its opposite side is AC (D1.21). Write S(XY) for the area of the square on XY, and R(XY,ZW) for the area of the rectangle contained by XY and ZW (D1.22, D2.1).

**Step 2.** Produce BC in both directions and draw from A the perpendicular AD to this straight line, with foot D (P2, 1.12). The angles made by AD with the straight line BC at D are right angles (D1.10).

**Step 3.** The point D lies strictly between B and C. Indeed, if D lay beyond B, then angle ABC would be an exterior angle of triangle ABD and would be greater than its opposite interior right angle ADB (1.16), contradicting the acuteness of angle ABC (D1.12). If D lay beyond C, then angle ACB would similarly be an exterior angle of triangle ACD greater than its opposite interior right angle ADC (1.16), again contradicting acuteness (D1.12). Finally, D cannot coincide with B or C, since the corresponding angle of ABC would then be right, not acute (D1.10, D1.12). Thus BC is cut internally at D.

**Step 4.** Apply 2.7 to BC cut at D, taking BD as the specified segment. It gives
S(BC) + S(BD) = 2R(BC,BD) + S(DC).
This is the direct choice of identity because it already contains the rectangle formed by the whole side BC and the segment BD required in the conclusion (2.7).

**Step 5.** Applying the theorem on the square opposite a right angle to triangles ADB and ADC gives, respectively,
S(AB) = S(AD) + S(BD),
and
S(AC) = S(AD) + S(DC) (1.47).

**Step 6.** Add S(AD) to both sides of the equality in Step 4 (CN2). Using the two equalities in Step 5 to replace the corresponding sums by equal squares, we obtain
S(AB) + S(BC) = S(AC) + 2R(BC,BD) (CN1, CN2).

**Step 7.** Subtracting S(AC) from these equal totals shows that the squares on AB and BC together exceed the square on AC by exactly 2R(BC,BD) (CN3). Since D lies strictly between B and C, this rectangle has positive area, so the square on AC is strictly less than those two squares together (CN5). Here BC is the side containing the chosen acute angle on which the perpendicular falls, and BD is the segment cut off within it towards that angle. This is the required conclusion.

**USED:** 1.12, 1.16, 1.47, 2.7, CN1, CN2, CN3, CN5, D1.10, D1.12, D1.21, D1.22, D2.1, P2
**Human refs (from References field):** 1.47, 2.7
**Jaccard:** 0.143 — AI adds ['1.12', '1.16', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.10', 'D1.12', 'D1.21', 'D1.22', 'D2.1', 'P2']

## Proposition 2.14
**Statement:** To construct a square equal to a given rectilineal figure.

**Step 1.** Let Q be the given rectilineal figure. Construct a right angle by 1.11, and construct a parallelogram ABCD equal in area to Q with angle ABC equal to that right angle by 1.45. Opposite angles of a parallelogram are equal, and adjacent angles together equal two right angles (1.34, 1.29). Consequently, all four angles are right (P4, CN3), so ABCD is a rectangle.

**Step 2.** If AB equals BC, the opposite-side equalities of 1.34 make all four sides equal. Thus ABCD itself is the required square (D1.22). Otherwise, relabel the vertices if necessary so that AB is greater than BC; this is possible because opposite sides are equal (1.34).

**Step 3.** Produce AB sufficiently beyond B and cut off BE equal to BC (P2, 1.3). Bisect AE at F (1.10). Since AB is greater than BE, the midpoint F lies between A and B: if F were at B or beyond B, then AB would be no greater than AF, while BE would be no less than FE, contradicting AF = FE and AB > BE (CN5). Hence FB is a proper part of FE, and FB < FE (CN5).

**Step 4.** Describe the circle with centre F and radius FE (P3). At B draw a perpendicular to AE and extend it to meet the circumference at H (1.11, P2). Here B is inside the circle because FB < FE, so the perpendicular ray meets the circumference. Join FH (P1). The angle FBH is right (D1.10), and FH = FE because they are radii of the same circle (D1.15).

**Step 5.** The straight line AE is cut equally at F and unequally at B. Therefore the rectangle contained by AB and BE, together with the square on FB, equals the square on FE (2.5). This is the direct path choice: placing the rectangle’s two side lengths consecutively and bisecting their combined line gives exactly the equal-and-unequal division required by 2.5.

**Step 6.** In the right-angled triangle FBH, the square on FH equals the squares on FB and BH together (1.47). Since FH = FE, the squares on these equal straight lines coincide when superposed and are equal (CN4). Thus the square on FE also equals the squares on FB and BH together (CN1).

**Step 7.** Comparing Steps 5 and 6, the rectangle contained by AB and BE together with the square on FB equals the squares on FB and BH together (CN1). Subtract the common square on FB: the rectangle contained by AB and BE equals the square on BH (CN3). Since BE = BC, that rectangle equals ABCD, the rectangle contained by AB and BC (D2.1, CN4). But ABCD equals Q; hence the square on BH equals Q (CN1). Construct that square by 1.46. The required square equal to the given rectilineal figure has therefore been constructed.

**USED:** 1.10, 1.11, 1.29, 1.3, 1.34, 1.45, 1.46, 1.47, 2.5, CN1, CN3, CN4, CN5, D1.10, D1.15, D1.22, D2.1, P1, P2, P3, P4
**Human refs (from References field):** 1.45, 1.47, 2.5
**Jaccard:** 0.143 — AI adds ['1.10', '1.11', '1.29', '1.3', '1.34', '1.46', 'CN1', 'CN3', 'CN4', 'CN5', 'D1.10', 'D1.15', 'D1.22', 'D2.1', 'P1', 'P2', 'P3', 'P4']
