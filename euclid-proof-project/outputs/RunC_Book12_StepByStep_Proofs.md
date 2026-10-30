# Book 12 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 12.1
**Statement:** Similar polygons inscribed in circles are to one another as the squares on the diameters.

**Step 1.** Let ABCDE and FGHKL be similar polygons inscribed in circles with diameters BM and GN respectively. We are to show that polygon ABCDE is to polygon FGHKL as the square on BM is to the square on GN.

**Step 2.** Join BE and GL. Since the polygons ABCDE and FGHKL are similar, their corresponding angles are equal and the sides about the equal angles are proportional [D6.1]. In particular, angle BAE equals angle GFL, and BA is to AE as GF is to FL.

**Step 3.** Since in triangles BAE and GFL the angle BAE equals the angle GFL and the sides about these equal angles are proportional (BA:AE = GF:FL), the triangles BAE and GFL are equiangular [6.6]. Therefore angle AEB equals angle FLG.

**Step 4.** Now angle AEB is an angle in the circle on the arc AB, and angle AMB is also an angle in the same segment (both stand on arc AB). Therefore angle AEB equals angle AMB [3.21]. Similarly, angle FLG equals angle FNG [3.21].

**Step 5.** Since angle AEB equals angle AMB [Step 4] and angle AEB equals angle FLG [Step 3], it follows that angle AMB equals angle FNG [CN1].

**Step 6.** Since BM is a diameter of the circle, the angle BAM is an angle in a semicircle, and therefore angle BAM is a right angle [3.31]. Similarly, since GN is a diameter, angle GFN is a right angle [3.31].

**Step 7.** Therefore angle BAM equals angle GFN (both being right angles) [P4].

**Step 8.** In triangles ABM and FGN, angle BAM equals angle GFN [Step 7] and angle AMB equals angle FNG [Step 5]. Therefore the remaining angle ABM equals the remaining angle FGN [1.32], and so triangles ABM and FGN are equiangular.

**Step 9.** Since triangles ABM and FGN are equiangular, their corresponding sides are proportional [6.4]. Therefore BA is to GF as BM is to GN.

**Step 10.** Since similar polygons are to one another in the duplicate ratio of corresponding sides [6.20], polygon ABCDE is to polygon FGHKL in the duplicate ratio of BA to GF.

**Step 11.** Since BA is to GF as BM is to GN [Step 9], the duplicate ratio of BA to GF is the same as the duplicate ratio of BM to GN [D5.9, 5.11].

**Step 12.** But the duplicate ratio of BM to GN is the ratio of the square on BM to the square on GN [6.20 porism, i.e., the square on BM is to the square on GN in the duplicate ratio of BM to GN].

**Step 13.** Therefore polygon ABCDE is to polygon FGHKL as the square on BM is to the square on GN [5.11, CN1].

**Step 14.** Therefore similar polygons inscribed in circles are to one another as the squares on the diameters, which is the required result. Q.E.D.

**USED:** 1.32, 3.21, 3.31, 5.11, 6.20, 6.4, 6.6, CN1, D5.9, D6.1, P4
**Human refs (from References field):** 1.32, 3.27, 3.31, 6.20, 6.4, 6.6, D6.1
**Jaccard:** 0.500 — AI adds ['3.21', '5.11', 'CN1', 'D5.9', 'P4']; Human adds ['3.27']

## Proposition 12.2
**Statement:** Circles are to one another as the squares on the diameters.

**Step 1.** Let ABCD and EFGH be two circles with diameters AC and EG respectively. We claim that circle ABCD is to circle EFGH as the square on AC is to the square on EG. That is, circle ABCD : circle EFGH = sq(AC) : sq(EG).

**Step 2.** Suppose, for contradiction, that circle ABCD is to circle EFGH not as sq(AC) is to sq(EG). Then sq(AC) is to sq(EG) as circle ABCD is to some area S, where S is either less than or greater than circle EFGH [5.11 — ratios of the same magnitudes must stand in some proportion].

**Step 3.** Case I: Assume first that S is less than circle EFGH. Then circle EFGH exceeds S by some magnitude, say circle EFGH - S = Delta, where Delta is a positive magnitude.

**Step 4.** Inscribe a square in circle EFGH [4.6]. This square is greater than half the circle EFGH, since the square consists of four triangles each having as base a side of the square and as height the radius from the center perpendicular to that side, and these triangles together cover more than half the circle's area. Thus the remainder, circle EFGH minus the inscribed square, is less than half of circle EFGH.

**Step 5.** By successively bisecting the arcs and joining the new vertices to form regular inscribed polygons of 8, 16, 32, ... sides, at each stage the newly added triangular segments each exceed half the circular segment they replace [since each triangle on a chord is more than half the corresponding circular segment, by 1.41 and the properties of the circle]. Hence at each doubling, more than half of the remaining difference between the circle and the inscribed polygon is removed.

**Step 6.** By the principle of exhaustion [10.1], after sufficiently many doublings we obtain a polygon P_EFGH inscribed in circle EFGH such that the difference (circle EFGH - P_EFGH) is less than Delta. Therefore P_EFGH is greater than S.

**Step 7.** Inscribe a similar polygon P_ABCD in circle ABCD, with the same number of sides as P_EFGH. Since both polygons are similar and inscribed in their respective circles, by 12.1 we have P_ABCD : P_EFGH = sq(AC) : sq(EG).

**Step 8.** But by our supposition, sq(AC) : sq(EG) = circle ABCD : S. Therefore P_ABCD : P_EFGH = circle ABCD : S [5.11, CN1].

**Step 9.** Since P_ABCD is inscribed in circle ABCD, we have P_ABCD < circle ABCD [CN5]. From the proportion P_ABCD : P_EFGH = circle ABCD : S, since P_ABCD < circle ABCD, it follows that P_EFGH < S [5.14].

**Step 10.** But in Step 6 we established that P_EFGH > S. This is a contradiction. Therefore S is not less than circle EFGH.

**Step 11.** Case II: Assume now that S is greater than circle EFGH. Then sq(AC) : sq(EG) = circle ABCD : S with S > circle EFGH. By inversion [5.7, D5.13], sq(EG) : sq(AC) = S : circle ABCD. Since S > circle EFGH, we can find a magnitude S' such that sq(EG) : sq(AC) = circle EFGH : S', and then S' < circle ABCD [5.14].

**Step 12.** That is, we now have sq(EG) : sq(AC) = circle EFGH : S', where S' is less than circle ABCD. But this places us exactly in the situation of Case I with the roles of the two circles interchanged: circle EFGH is to some area S' less than circle ABCD as the square on EG is to the square on AC.

**Step 13.** Applying the same exhaustion argument as in Steps 4 through 10 but now working in circle ABCD, we inscribe polygons of sufficiently many sides in circle ABCD so that the inscribed polygon exceeds S', and inscribe a similar polygon in circle EFGH. By 12.1, these similar inscribed polygons are as the squares on the diameters. The same chain of proportional reasoning produces the contradiction that the polygon inscribed in ABCD is both greater than and less than S'.

**Step 14.** Therefore S is not greater than circle EFGH either.

**Step 15.** Since S is neither less than nor greater than circle EFGH, we conclude S equals circle EFGH. Therefore circle ABCD : circle EFGH = sq(AC) : sq(EG). Circles are to one another as the squares on the diameters. Q.E.D.

**USED:** 1.41, 10.1, 12.1, 4.6, 5.11, 5.14, 5.7, CN1, CN5, D5.13
**Human refs (from References field):** 12.1, 5.11, 5.16
**Jaccard:** 0.182 — AI adds ['1.41', '10.1', '4.6', '5.14', '5.7', 'CN1', 'CN5', 'D5.13']; Human adds ['5.16']

## Proposition 12.3
**Statement:** Any pyramid which has a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; and the two prisms are greater than the half of the whole pyramid.

**Step 1.** Let ABCD be a pyramid with triangular base BCD and apex A. Bisect AB at E, AC at F, AD at G, BC at H, CD at K, and BD at L [1.10]. Join EF, EG, EH, EL, FG, FH, FK, GH, GK, GL, HK, HL, KL [P1].

**Step 2.** Since E and F are midpoints of sides AB and AC of triangle ABC, EF is parallel to BC and EF equals half of BC [6.2]. Similarly, EH is parallel to AC and equals half of AC, and FH is parallel to AB and equals half of AB. Likewise in triangle ABD, EG is parallel to BD and equals BD/2, EL is parallel to AD and equals AD/2, and GL is parallel to AB and equals AB/2. In triangle ACD, FG is parallel to CD and equals CD/2, FK is parallel to AD and equals AD/2, and GK is parallel to AC and equals AC/2. In triangle BCD, HK is parallel to BD and equals BD/2, HL is parallel to CD and equals CD/2, and KL is parallel to BC and equals BC/2 [6.2].

**Step 3.** Consider pyramid AEFG. Its six edges are AE = AB/2, AF = AC/2, AG = AD/2, EF = BC/2, EG = BD/2, and FG = CD/2. Since each edge of AEFG is half the corresponding edge of ABCD, the four triangular faces of AEFG are respectively similar to the four faces of ABCD with the same ratio [6.2, D6.1]. Hence AEFG is similar to ABCD [D11.9].

**Step 4.** Consider pyramid DGKL. Its six edges are DG = AD/2, DK = CD/2, DL = BD/2, GK = AC/2, GL = AB/2, and KL = BC/2. Each edge equals half of a corresponding edge of ABCD, so pyramid DGKL is also similar to ABCD by the same reasoning [6.2, D6.1, D11.9].

**Step 5.** The set of six edge lengths of AEFG is {AB/2, AC/2, AD/2, BC/2, BD/2, CD/2}, and the set of six edge lengths of DGKL is {AD/2, CD/2, BD/2, AC/2, AB/2, BC/2}. These are the same six lengths. Therefore the four faces of AEFG are respectively congruent to the four faces of DGKL [1.8], and the two pyramids are equal and similar to one another [D11.10].

**Step 6.** We now show the remainder of pyramid ABCD, after removing pyramids AEFG and DGKL, consists of two equal prisms. Consider the quadrilateral EHKG. From Step 2, EH is parallel to GK and EH = GK (both parallel to AC and equal to AC/2), and EG is parallel to HK and EG = HK (both parallel to BD and equal to BD/2) [CN1]. Since both pairs of opposite sides are equal and parallel, EHKG is a parallelogram [1.33, 1.34].

**Step 7.** The plane of parallelogram EHKG divides the remaining solid into two parts. One part lies on the side containing F and C; the other lies on the side containing L and B.

**Step 8.** Consider the solid on the side of F and C, with vertices E, F, G, H, K, C. Its faces are as follows. Triangle EFG is the face exposed by removing pyramid AEFG. In face ABC, since EF is parallel to HC (both parallel to BC, each equal to BC/2) and EH is parallel to CF (both parallel to AC, each equal to AC/2), the quadrilateral EHCF is a parallelogram [1.33]. In face ACD, since FG is parallel to CK (both parallel to CD, each equal to CD/2) and GK is parallel to CF (both parallel to AC, each equal to AC/2), the quadrilateral FGKC is a parallelogram [1.33]. In face BCD, the triangle HCK has sides HC = BC/2, CK = CD/2, and HK = BD/2. The fifth face is the parallelogram EHKG.

**Step 9.** The solid EFGHCK has two triangular faces EFG and HCK, and three parallelogram faces EHCF, EHKG, and FGKC. The triangles EFG and HCK are congruent, since EF = HC = BC/2, FG = CK = CD/2, and EG = HK = BD/2 [1.8]. They are parallel, since EF is parallel to HC, FG is parallel to CK, and EG is parallel to HK [Step 2]. Therefore this solid is a prism [D11.13].

**Step 10.** Consider the solid on the side of L and B, with vertices E, G, H, K, L, B. Its faces are as follows. In face ABC, the triangle EBH has sides EB = AB/2, BH = BC/2, and EH = AC/2. In face ABD, since EB is parallel to LG (both parallel to AB, each equal to AB/2) and BL is parallel to EG (both parallel to BD, each equal to BD/2), the quadrilateral EBLG is a parallelogram [1.33]. In face BCD, since BH is parallel to KL (both parallel to BC, each equal to BC/2) and BL is parallel to HK (both parallel to BD, each equal to BD/2), the quadrilateral BHKL is a parallelogram [1.33]. Triangle GKL is the face exposed by removing pyramid DGKL, with sides GK = AC/2, GL = AB/2, and KL = BC/2. The fifth face is the parallelogram EHKG.

**Step 11.** The solid EBHGKL has two triangular faces EBH and GKL, and three parallelogram faces EBLG, BHKL, and EHKG. The triangles EBH and GKL are congruent, since EB = GL = AB/2, BH = KL = BC/2, and EH = GK = AC/2 [1.8]. They are parallel, since EB is parallel to GL, BH is parallel to KL, and EH is parallel to GK [Step 2]. Therefore this solid is also a prism [D11.13].

**Step 12.** We now show the two prisms are equal. The corner pyramid at C is CFHK, with edges CF = AC/2, CH = BC/2, CK = CD/2, FH = AB/2, FK = AD/2, HK = BD/2, which are the same six edge lengths as AEFG and DGKL. Similarly the corner pyramid at B is BEHL, with edges BE = AB/2, BH = BC/2, BL = BD/2, EH = AC/2, EL = AD/2, HL = CD/2, again the same six lengths. So all four corner pyramids are equal to one another [1.8, D11.10]. Now, Prism 1 (EFGHCK) contains corner pyramid CFHK as a proper part, and Prism 2 (EBHGKL) contains corner pyramid BEHL as a proper part. The remaining portion of Prism 1 after removing CFHK, and the remaining portion of Prism 2 after removing BEHL, are each bounded on one side by the parallelogram EHKG and on the other by a triangular face of the respective corner pyramid. These two remaining portions are pyramids with the common base EHKG and with apices F and L respectively, lying on opposite sides. Since EL is parallel to FK (both parallel to AD, both equal to AD/2), and EF is parallel to KL (both parallel to BC, both equal to BC/2), and the distances from F and from L to the plane of EHKG are equal, these two pyramids on base EHKG are equal [11.39, 1.34]. Adding back the equal corner pyramids CFHK and BEHL respectively, the two prisms are equal [CN2].

**Step 13.** Finally, we show the two prisms together are greater than half the whole pyramid. Prism 1 contains the corner pyramid CFHK, which is equal to the removed pyramid AEFG [Step 12, Step 5]. Since the prism properly contains this corner pyramid, Prism 1 is greater than CFHK, and hence greater than AEFG [CN5]. Similarly, Prism 2 properly contains corner pyramid BEHL, which is equal to the removed pyramid DGKL, so Prism 2 is greater than DGKL [CN5]. Therefore the two prisms together are greater than the two removed pyramids together [CN2 applied to inequalities]. Since the whole pyramid equals the two removed pyramids plus the two prisms, and the two prisms exceed the two removed pyramids, the two prisms are greater than half of the whole pyramid [CN3, CN5].

**Step 14.** Therefore any pyramid with a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; and the two prisms are greater than the half of the whole pyramid. Q.E.D.

**USED:** 1.10, 1.33, 1.34, 1.8, 11.39, 6.2, CN1, CN2, CN3, CN5, D11.10, D11.13, D11.9, D6.1, P1
**Human refs (from References field):** 1.29, 1.34, 1.4, 11.10, 11.39, 6.2, D11.10, D6.1
**Jaccard:** 0.278 — AI adds ['1.10', '1.33', '1.8', 'CN1', 'CN2', 'CN3', 'CN5', 'D11.13', 'D11.9', 'P1']; Human adds ['1.29', '1.4', '11.10']

## Proposition 12.4
**Statement:** If there be two pyramids of the same height which have triangular bases, and cach of them be divided into two pyramids equal to one another and similar to the whole, and into two equal prisms, then, as the base of the one pyramid is to the base of the other pyramid, so will all the prisms in the one pyramid be to all the prisms, being equal in multitude, in the other pyramid.

**Step 1.** Let there be two pyramids of the same height with triangular bases, namely pyramid ABCD with base ABC and vertex D, and pyramid EFGH with base EFG and vertex H, where both pyramids have the same height. We are to show that as triangle ABC is to triangle EFG, so are all the prisms arising from repeated subdivision of ABCD to all the prisms, equal in multitude, arising from the same repeated subdivision of EFGH. [D11.12]

**Step 2.** By 12.3, divide pyramid ABCD into two pyramids equal to one another and similar to the whole, and into two equal prisms. Likewise divide pyramid EFGH into two pyramids equal to one another and similar to the whole, and into two equal prisms. [12.3]

**Step 3.** In the division of 12.3, the midpoints of the edges of ABCD are taken. Let K, L, M be the midpoints of AB, AC, AD respectively, and let N, O, P be the midpoints of BC, BD, CD respectively. The two prisms produced from ABCD have triangular cross-sections determined by these midpoints. Similarly, let the corresponding midpoints for EFGH be taken, producing two prisms from EFGH. [1.10]

**Step 4.** The two prisms arising from the subdivision of ABCD each have the same height as the two prisms arising from the subdivision of EFGH, because the original pyramids ABCD and EFGH have the same height, and the subdivision bisects the height in the same manner for both. [12.3, CN1]

**Step 5.** Consider one of the two prisms from ABCD and the corresponding prism from EFGH. These are prisms of equal height. A prism on a triangular base equals half the parallelepiped on the same base and height, and parallelepipeds of the same height are to one another as their bases. Therefore prisms of equal height are to one another as their bases. [11.28, 11.32, 11.39]

**Step 6.** The base of the prism from ABCD is a triangle formed by joining midpoints of sides of triangle ABC, which by 6.19 has area one-fourth that of triangle ABC. Similarly, the base of the corresponding prism from EFGH is one-fourth of triangle EFG. Since the prisms of equal height are as their bases, the prism from ABCD is to the corresponding prism from EFGH as one-fourth of ABC is to one-fourth of EFG, that is, as triangle ABC is to triangle EFG. [6.19, 5.15]

**Step 7.** Since the two prisms from ABCD are equal to one another (by 12.3), and the two prisms from EFGH are equal to one another (by 12.3), the sum of the two prisms from ABCD is to the sum of the two prisms from EFGH as one prism from ABCD is to one prism from EFGH, that is, as triangle ABC is to triangle EFG. [12.3, 5.12]

**Step 8.** Now the two smaller pyramids produced from ABCD are equal and similar to one another and similar to ABCD, and likewise the two smaller pyramids from EFGH are equal and similar to one another and similar to EFGH. Each pair of corresponding smaller pyramids (one from ABCD, one from EFGH) again has the same height as each other, since the original pyramids had the same height and the subdivision halves the height uniformly. [12.3]

**Step 9.** Apply 12.3 again to each of the smaller pyramids, subdividing each into two still-smaller pyramids and two equal prisms. For each corresponding pair of smaller pyramids (one descended from ABCD, one descended from EFGH), the prisms produced are again prisms of equal height. By the same reasoning as in Steps 5-6, these prisms are to one another as the bases of the smaller pyramids from which they arise. [12.3, 11.39]

**Step 10.** The bases of the smaller pyramids from ABCD are similar to triangle ABC and equal to one-fourth of the triangle from which they were subdivided, and likewise for those from EFGH. Since similar triangles are to one another as the squares on corresponding sides (6.19), and the subdivision produces bases that maintain the same ratio throughout, each pair of corresponding prisms at this second level of subdivision is again in the ratio of triangle ABC to triangle EFG. [6.19, 6.20]

**Step 11.** At each stage of subdivision, we obtain twice as many prisms from each pyramid as at the previous stage. At every stage, the prisms from ABCD taken together are to the prisms from EFGH taken together as triangle ABC is to triangle EFG. This is because at each stage, every individual pair of corresponding prisms is in the ratio ABC to EFG (by Steps 5-6 applied to the sub-pyramids at that level), and when several magnitudes are each in the same ratio to corresponding magnitudes, the sums are also in that ratio. [5.12]

**Step 12.** Therefore, after any number of equal subdivisions applied to both pyramids, the sum of all the prisms in pyramid ABCD is to the sum of all the prisms, being equal in multitude, in pyramid EFGH, as the base ABC of the one pyramid is to the base EFG of the other pyramid. [5.12, CN2]

**Step 13.** Therefore, if there be two pyramids of the same height which have triangular bases, and each of them be divided into two pyramids equal to one another and similar to the whole, and into two equal prisms, then as the base of the one pyramid is to the base of the other pyramid, so will all the prisms in the one pyramid be to all the prisms, being equal in multitude, in the other pyramid. Q.E.D.

**USED:** 1.10, 11.28, 11.32, 11.39, 12.3, 5.12, 5.15, 6.19, 6.20, CN1, CN2, D11.12, D11.13
**Human refs (from References field):** 11.39, 12.3, 5.12, 5.16, 6.22
**Jaccard:** 0.200 — AI adds ['1.10', '11.28', '11.32', '5.15', '6.19', '6.20', 'CN1', 'CN2', 'D11.12', 'D11.13']; Human adds ['5.16', '6.22']

## Proposition 12.5
**Statement:** Pyramids which are of the same height and have triangular bases are to one another as the bases.

**Step 1.** Let there be two pyramids of the same height with triangular bases, the first having base ABC and apex D, and the second having base EFG and apex H. We must prove that pyramid ABCD is to pyramid EFGH as triangle ABC is to triangle EFG.

**Step 2.** Suppose, for the sake of contradiction, that the pyramids are not as the bases. Then as triangle ABC is to triangle EFG, so is pyramid ABCD to some solid W, where W is either less than or greater than pyramid EFGH.

**Step 3.** First suppose W is less than pyramid EFGH. By 12.3, divide pyramid EFGH into two pyramids equal to one another and similar to the whole, and into two equal prisms. The two prisms together are greater than half of pyramid EFGH [12.3].

**Step 4.** Again by 12.3, divide each of the two sub-pyramids in the same manner into two smaller pyramids and two prisms. The prisms obtained at this stage are again greater than half of the respective sub-pyramids [12.3].

**Step 5.** Continue this process of successive division. Since pyramid EFGH exceeds W, and at each stage the prisms removed are greater than half of the remaining pyramidal portions, by repeated application we eventually reach a stage where the sum of the remaining pyramidal portions (the leftover sub-pyramids not yet resolved into prisms) is less than the excess of pyramid EFGH over W [10.1]. That is, the remaining sub-pyramids in EFGH together have total volume less than (pyramid EFGH - W).

**Step 6.** Let the total of all the prisms accumulated in pyramid EFGH at this stage be called S_E. Then since the remaining sub-pyramids are less than (pyramid EFGH - W), we have pyramid EFGH - S_E < pyramid EFGH - W, so S_E > W.

**Step 7.** Now perform exactly the same number of divisions on pyramid ABCD, obtaining prisms at each corresponding stage. Let the total of all accumulated prisms in ABCD be S_A.

**Step 8.** By 12.4, at each stage of division, as triangle ABC is to triangle EFG, so are all the prisms in pyramid ABCD to all the prisms (equal in multitude) in pyramid EFGH. Therefore S_A is to S_E as triangle ABC is to triangle EFG [12.4].

**Step 9.** But by our supposition, as triangle ABC is to triangle EFG, so is pyramid ABCD to W. Therefore S_A is to S_E as pyramid ABCD is to W [5.11].

**Step 10.** Now S_A, being a sum of prisms contained within pyramid ABCD, is less than pyramid ABCD, so S_A < pyramid ABCD. Since S_A : S_E = pyramid ABCD : W, and S_A < pyramid ABCD, it follows that S_E < W [5.14].

**Step 11.** But in Step 6 we showed S_E > W. This is a contradiction. Therefore W is not less than pyramid EFGH.

**Step 12.** Now suppose W is greater than pyramid EFGH. Then as triangle ABC is to triangle EFG, so is pyramid ABCD to W with W > pyramid EFGH. By inversion, as triangle EFG is to triangle ABC, so is W to pyramid ABCD [5.7.corollary, i.e., from the proportion we derive the inverse].

**Step 13.** Since W > pyramid EFGH, we have that W is to pyramid ABCD in a certain ratio. There exists some solid W' such that as triangle EFG is to triangle ABC, so is pyramid EFGH to W'. Since W > pyramid EFGH, and both are in proportion with the same terms, it follows that W' < pyramid ABCD [5.14].

**Step 14.** But now we have: as triangle EFG is to triangle ABC, so is pyramid EFGH to W', with W' less than pyramid ABCD. This is exactly the first case again (with the two pyramids interchanged), which we have already shown leads to a contradiction in Steps 3-11.

**Step 15.** Therefore W is neither less than nor greater than pyramid EFGH, so W equals pyramid EFGH. That is, as triangle ABC is to triangle EFG, so is pyramid ABCD to pyramid EFGH [5.9, from the definition of proportionality].

**Step 16.** Therefore pyramids which are of the same height and have triangular bases are to one another as the bases. Q.E.D.

**USED:** 10.1, 12.3, 12.4, 5.11, 5.14, 5.7, 5.9, CN5
**Human refs (from References field):** 10.1, 12.2, 12.3, 12.4, 5.16, 5.2
**Jaccard:** 0.273 — AI adds ['5.11', '5.14', '5.7', '5.9', 'CN5']; Human adds ['12.2', '5.16', '5.2']

## Proposition 12.6
**Statement:** Pyramids which are of the same height and have polygonal bases are to one another as the bases.

**Step 1.** Let the two pyramids be P1 with polygonal base ABCDE and apex F, and P2 with polygonal base GHIJK and apex L, both having the same height. We are to prove that P1 is to P2 as polygon ABCDE is to polygon GHIJK.

**Step 2.** From vertex A, draw diagonals AC and AD in the base polygon ABCDE, dividing it into triangles ABC, ACD, and ADE. These diagonals, together with the apex F, divide pyramid P1 into three pyramids F-ABC, F-ACD, and F-ADE, each having the same height as P1 and having triangular bases.

**Step 3.** Similarly, from vertex G, draw diagonals GI and GJ in polygon GHIJK, dividing it into triangles GHI, GIJ, and GJK. These diagonals, together with the apex L, divide pyramid P2 into three pyramids L-GHI, L-GIJ, and L-GJK of the same height.

**Step 4.** Since pyramids F-ABC and L-GHI have the same height and triangular bases, by 12.5, pyramid F-ABC is to pyramid L-GHI as triangle ABC is to triangle GHI.

**Step 5.** Since pyramids F-ACD and L-GHI have the same height and triangular bases, by 12.5, pyramid F-ACD is to pyramid L-GHI as triangle ACD is to triangle GHI.

**Step 6.** From Steps 4 and 5, since F-ABC is to L-GHI as ABC is to GHI, and F-ACD is to L-GHI as ACD is to GHI, by 5.24 the sum (F-ABC together with F-ACD) is to L-GHI as the sum (triangle ABC together with triangle ACD) is to triangle GHI.

**Step 7.** Since pyramids F-ADE and L-GHI have the same height and triangular bases, by 12.5, pyramid F-ADE is to pyramid L-GHI as triangle ADE is to triangle GHI.

**Step 8.** From Steps 6 and 7, by 5.24 again, the sum (F-ABC together with F-ACD together with F-ADE) is to pyramid L-GHI as the sum (triangle ABC together with triangle ACD together with triangle ADE) is to triangle GHI. But the sum of pyramids F-ABC, F-ACD, and F-ADE equals pyramid P1, and the sum of triangles ABC, ACD, and ADE equals polygon ABCDE. Therefore pyramid P1 is to pyramid L-GHI as polygon ABCDE is to triangle GHI.

**Step 9.** By the same reasoning applied to the sub-pyramids of P2: since L-GIJ and L-GHI have the same height with triangular bases, by 12.5, L-GIJ is to L-GHI as triangle GIJ is to triangle GHI. Likewise by 12.5, L-GJK is to L-GHI as triangle GJK is to triangle GHI. Applying 5.24 twice, the sum (L-GHI together with L-GIJ together with L-GJK) is to pyramid L-GHI as the sum (triangle GHI together with triangle GIJ together with triangle GJK) is to triangle GHI. That is, pyramid P2 is to pyramid L-GHI as polygon GHIJK is to triangle GHI.

**Step 10.** From Step 9, by the porism of 5.7 (invertendo), pyramid L-GHI is to pyramid P2 as triangle GHI is to polygon GHIJK.

**Step 11.** From Step 8 we have P1 is to L-GHI as polygon ABCDE is to triangle GHI, and from Step 10 we have L-GHI is to P2 as triangle GHI is to polygon GHIJK. Therefore by 5.22 (ex aequali), pyramid P1 is to pyramid P2 as polygon ABCDE is to polygon GHIJK.

**Step 12.** The same argument applies to polygonal bases with any number of sides, since any polygon can be divided into triangles by diagonals drawn from one vertex, and 5.24 can be applied as many times as needed. Therefore pyramids of the same height with polygonal bases are to one another as their bases.

**USED:** 12.5, 5.22, 5.24, 5.7
**Human refs (from References field):** 12.5, 5.18, 5.22
**Jaccard:** 0.400 — AI adds ['5.24', '5.7']; Human adds ['5.18']

## Proposition 12.7
**Statement:** Any prism which has a triangular base is divided into three pyramids equal to one another which have triangular bases.

**Step 1.** Let there be a prism with triangular base ABC and opposite triangular face DEF, where A corresponds to D, B to E, and C to F, so that ABED, BEFC, and ADFC are the parallelogram lateral faces [D11.13].

**Step 2.** Join AC and draw the planes through A, C, E and through A, C, D. These two planes, together with the faces of the prism, divide the prism into three pyramids with triangular bases [D11.12]: pyramid T1 = ABCE (base ABC, apex E), pyramid T2 = ACDE (base ACD, apex E, equivalently base ACE, apex D), and pyramid T3 = ACEF (base ACF, apex E, equivalently base ACE, apex F).

**Step 3.** We show T1 = T2. Since ABED is a parallelogram (lateral face of the prism), its diagonal AE divides it into two equal triangles ABE and ADE [1.34]. Now consider T1 as the pyramid with base ABE and apex C, and T2 as the pyramid with base ADE and apex C. Both pyramids have the same apex C, and their bases ABE and ADE lie in the same plane, namely the plane of parallelogram ABED. Therefore both pyramids have the same height, namely the perpendicular distance from C to the plane ABED. Since their triangular bases are equal and they have the same height, by XII.5 they are equal [12.5]. Thus T1 = T2.

**Step 4.** We show T2 = T3. Since ADFC is a parallelogram (lateral face of the prism), its diagonal AC divides it into two equal triangles ACD and ACF [1.34]. Now consider T2 as the pyramid with base ACD and apex E, and T3 as the pyramid with base ACF and apex E. Both pyramids have the same apex E, and their bases ACD and ACF lie in the same plane, namely the plane of parallelogram ADFC. Therefore both pyramids have the same height, namely the perpendicular distance from E to the plane ADFC. Since their triangular bases are equal and they have the same height, by XII.5 they are equal [12.5]. Thus T2 = T3.

**Step 5.** Since T1 = T2 and T2 = T3, it follows that T1 = T2 = T3 [CN1]. Therefore the prism with triangular base ABC has been divided into three pyramids equal to one another which have triangular bases, which is what was to be proved.

**USED:** 1.34, 12.5, CN1, D11.12, D11.13
**Human refs (from References field):** 1.34, 12.5
**Jaccard:** 0.400 — AI adds ['CN1', 'D11.12', 'D11.13']

## Proposition 12.8
**Statement:** Similar pyramids which have triangular bases are in the triplicate ratio of their corresponding sides.

**Step 1.** Let ABCD and EFGH be similar pyramids with triangular bases ABC and EFG respectively, where D and H are the respective apices. Since the pyramids are similar, by D11.9, they are contained by similar planes equal in multitude. Therefore the four triangular faces of ABCD are respectively similar to the four triangular faces of EFGH, and by D6.1 the sides about equal angles are proportional. In particular, all corresponding edges are proportional: AB:EF = BC:FG = CA:GE = DA:HE = DB:HF = DC:HG.

**Step 2.** Complete pyramid ABCD to a parallelepiped as follows. Through each edge of the tetrahedron, draw a plane parallel to the opposite edge. The six planes so drawn enclose a parallelepiped, call it S1, in which ABCD is inscribed so that each edge of ABCD lies along a diagonal of a face of S1. Similarly, complete pyramid EFGH to a parallelepiped S2.

**Step 3.** We show that S1 and S2 are similar parallelepipeds. Each face of S1 is a parallelogram whose diagonals are a pair of opposite edges of ABCD. Since corresponding edges of the two pyramids are proportional (Step 1) and the angles between corresponding edges are equal (the faces being similar triangles, and the solid angles at corresponding vertices being contained by equal plane angles in the same arrangement), the corresponding faces of S1 and S2 are similar parallelograms arranged in the same order. Therefore, by D11.9, the parallelepipeds S1 and S2 are similar.

**Step 4.** Since S1 and S2 are similar parallelepipeds, by 11.33, S1 is to S2 in the triplicate ratio of any corresponding pair of edges. Taking the edges corresponding to AB and EF, we have S1:S2 in the triplicate ratio of AB:EF.

**Step 5.** We now establish that S1 = 6 times pyramid ABCD. The diagonal plane through two opposite edges of S1 divides S1 into two equal triangular prisms, by 11.28. Each of these prisms has a triangular base, so by 12.7, each prism is divided into three pyramids equal to one another which have triangular bases. Thus S1 is divided into 2 times 3 = 6 equal pyramids with triangular bases. Since the two prisms are equal (11.28) and each yields three equal pyramids (12.7), all six pyramids are equal to one another.

**Step 6.** Pyramid ABCD is one of these six equal pyramids. To see this: one of the two prisms produced in Step 5 has triangle ABC as its base and its apex edge passes through D. By 12.7, this prism decomposes into three equal pyramids, one of which is the pyramid on base ABC with apex at D, namely pyramid ABCD itself. Therefore pyramid ABCD is exactly one-sixth of S1, that is, S1 is the same multiple (sixfold) of pyramid ABCD. By the same construction and reasoning, S2 is the sixfold multiple of pyramid EFGH.

**Step 7.** Since S1 = 6 times pyramid ABCD and S2 = 6 times pyramid EFGH, by 5.15 (parts have the same ratio as the same multiples of them), pyramid ABCD is to pyramid EFGH as S1 is to S2.

**Step 8.** Combining Steps 4 and 7: pyramid ABCD is to pyramid EFGH in the triplicate ratio of AB to EF. Since AB and EF are corresponding sides of the similar pyramids, the similar pyramids which have triangular bases are in the triplicate ratio of their corresponding sides, by D5.10. This is what was to be proved.

**USED:** 11.28, 11.33, 12.7, 5.15, D11.9, D5.10, D6.1
**Human refs (from References field):** 11.24, 11.28, 11.33, 12.7
**Jaccard:** 0.375 — AI adds ['5.15', 'D11.9', 'D5.10', 'D6.1']; Human adds ['11.24']

## Proposition 12.9
**Statement:** In equal pyramids which have triangular bases the bases are reciprocally proportional to the heights; and those pyramids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let ABCD and EFGH be equal pyramids with triangular bases ABC and EFG respectively, where D and H are the apices. Let the perpendicular from D to the plane of ABC have length h1, and the perpendicular from H to the plane of EFG have length h2. We must show that triangle ABC is to triangle EFG as h2 is to h1.

**Step 2.** Complete each pyramid to the prism having the same triangular base and the same height: let prism P1 have base ABC and height h1, and prism P2 have base EFG and height h2. By 12.7, each prism with a triangular base is divided into three equal pyramids with triangular bases; therefore prism P1 is triple pyramid ABCD, and prism P2 is triple pyramid EFGH.

**Step 3.** Since pyramid ABCD equals pyramid EFGH (given), and prism P1 is triple pyramid ABCD while prism P2 is triple pyramid EFGH, we conclude that prism P1 equals prism P2, for equimultiples of equal magnitudes are equal [5.15].

**Step 4.** On triangle ABC, construct the parallelogram ABCL that is double triangle ABC, lying in the same plane, by producing side BC and completing the parallelogram [1.42]. Similarly, on triangle EFG, construct the parallelogram EFGM that is double triangle EFG. Erect the parallelepipedal solid S1 on parallelogram ABCL with height h1, and the parallelepipedal solid S2 on parallelogram EFGM with height h2.

**Step 5.** By 11.39, since S1 is a parallelepiped of height h1 with parallelogram base ABCL (which is double triangle ABC), and P1 is a prism of the same height h1 with triangular base ABC, the parallelepiped S1 equals prism P1. Likewise, parallelepiped S2 equals prism P2.

**Step 6.** Since prism P1 equals prism P2 (Step 3), and S1 equals P1 while S2 equals P2, we have S1 equals S2 [CN1].

**Step 7.** By 11.34, in equal parallelepipedal solids the bases are reciprocally proportional to the heights. Since S1 and S2 are equal parallelepipeds, we have: parallelogram ABCL is to parallelogram EFGM as h2 is to h1.

**Step 8.** Since parallelogram ABCL is double triangle ABC and parallelogram EFGM is double triangle EFG, the ratio ABCL : EFGM equals the ratio ABC : EFG [5.15]. Therefore triangle ABC is to triangle EFG as h2 is to h1 [5.11]. This completes the first part: in equal pyramids with triangular bases, the bases are reciprocally proportional to the heights.

**Step 9.** Now for the converse. Let pyramids ABCD and EFGH have triangular bases ABC and EFG with heights h1 and h2 respectively, and suppose triangle ABC is to triangle EFG as h2 is to h1. We must show the pyramids are equal.

**Step 10.** Using the same constructions as before, form prisms P1 and P2 on the same bases and heights as the pyramids, and parallelepipeds S1 and S2 on parallelogram bases ABCL (double ABC) and EFGM (double EFG) with the same heights.

**Step 11.** Since triangle ABC is to triangle EFG as h2 is to h1 (given), and ABCL is double ABC while EFGM is double EFG, we have ABCL is to EFGM as h2 is to h1 [5.15].

**Step 12.** By 11.34 (converse part), parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal. Therefore S1 equals S2.

**Step 13.** Since S1 equals prism P1 and S2 equals prism P2 [11.39], we have prism P1 equals prism P2 [CN1].

**Step 14.** Since prism P1 is triple pyramid ABCD and prism P2 is triple pyramid EFGH [12.7], and the prisms are equal, the pyramids are equal, for the third parts of equal magnitudes are equal [5.15].

**Step 15.** Therefore, in equal pyramids which have triangular bases the bases are reciprocally proportional to the heights; and those pyramids in which the bases are reciprocally proportional to the heights are equal. Q.E.D.

**USED:** 1.42, 11.34, 11.39, 12.7, 5.11, 5.15, CN1
**Human refs (from References field):** 1.34, 11.34, 5.11
**Jaccard:** 0.250 — AI adds ['1.42', '11.39', '12.7', '5.15', 'CN1']; Human adds ['1.34']

## Proposition 12.10
**Statement:** Any cone is a third part of the cylinder which has the same base with it and equal height.

**Step 1.** Let there be a cone K with circular base having centre E, and let C be the cylinder on the same base with the same height. I say that K is one-third of C, that is, C = 3K.

**Step 2.** Suppose for contradiction that C is not equal to 3K. Then either C > 3K or C < 3K.

**Step 3.** Case 1: Suppose C > 3K. Let S = C - 3K, so S > 0. Inscribe a square in the base circle [4.6]. This square is greater than half the circle, since it is half of the circumscribed square which contains the circle. Bisect each arc cut off by the sides of the square, and join straight lines to the points of bisection, forming an octagon. Each triangle so formed between a side of the square and two new chords is greater than half the circular segment in which it lies [1.41, since the triangle has the same base as a parallelogram that contains the segment, and the triangle is half that parallelogram]. Continue bisecting arcs and joining chords.

**Step 4.** By repeatedly taking away more than half of the remaining circular segments, we eventually obtain an inscribed polygon Q such that the sum of the remaining segments (the excess of the circle over Q) is less than S, measured as volumes by multiplying areas by the common height [10.1]. That is, C - Pr(Q) < S, where Pr(Q) is the prism erected on Q with height equal to that of the cylinder.

**Step 5.** Divide Q into triangles by joining all vertices to the centre E. On each triangle erect a prism of the same height as the cylinder. Each such triangular prism can be divided into three pyramids of equal volume having the same triangular base and the same height [12.7]. Therefore the prism on each triangle equals three times the pyramid on that triangle with the same height.

**Step 6.** Summing over all the constituent triangles of Q, we obtain Pr(Q) = 3 times Pyr(Q), where Pyr(Q) is the pyramid inscribed in the cone on the polygonal base Q with the same apex as the cone [12.7].

**Step 7.** From Step 4, C - Pr(Q) < S = C - 3K. Therefore Pr(Q) > 3K, and by Step 6, 3 times Pyr(Q) > 3K, so Pyr(Q) > K.

**Step 8.** But Q is inscribed in the base circle of the cone, and the pyramid Pyr(Q) is contained within the cone K. Therefore Pyr(Q) is less than K [CN5, since the whole is greater than the part]. This contradicts Step 7. Hence C is not greater than 3K.

**Step 9.** Case 2: Suppose C < 3K. Then 3K > C, so S = 3K - C > 0.

**Step 10.** By the same exhaustion process as in Case 1, inscribe a polygon Q in the base circle such that the excess of the circle over Q, measured as volumes, is less than S [10.1, 4.6]. Erect on Q a prism Pr(Q) of the same height as the cylinder, and form the pyramid Pyr(Q) inscribed in the cone on base Q. As before, Pr(Q) = 3 times Pyr(Q) [12.7].

**Step 11.** Since Q is inscribed in the base circle, the prism Pr(Q) is contained within the cylinder C. Also, the inscribed pyramid Pyr(Q) is contained within the cone K. Therefore Pyr(Q) < K [CN5], so 3 times Pyr(Q) < 3K, i.e., Pr(Q) < 3K.

**Step 12.** Now, C - Pr(Q) < S = 3K - C, which gives Pr(Q) > 2C - 3K. We also know Pr(Q) < C (since the polygon is within the circle) and Pr(Q) < 3K (from Step 11). Since C < 3K by assumption, we have Pr(Q) < 3K, which is consistent but does not yield a contradiction directly from inscribed figures alone.

**Step 13.** We therefore argue Case 2 by considering circumscribed figures. Circumscribe a polygon Q' about the base circle such that Q' exceeds the circle by an area that, multiplied by the height, is less than S = 3K - C [10.1 applied to the successive halving of the excess of circumscribed polygons over the circle]. Erect on Q' a prism Pr(Q') of the same height.

**Step 14.** Since Q' is circumscribed about the base circle, the cylinder C is contained within the prism Pr(Q'), and the cone K is contained within the pyramid Pyr(Q') erected on Q' to the same apex. Therefore Pyr(Q') > K [CN5], so 3 times Pyr(Q') > 3K.

**Step 15.** Also Pr(Q') = 3 times Pyr(Q') [12.7, applied to the constituent triangles of Q']. Since Q' exceeds the circle by less than S in volume, Pr(Q') - C < S = 3K - C, hence Pr(Q') < 3K. Then 3 times Pyr(Q') < 3K, so Pyr(Q') < K.

**Step 16.** But from Step 14, Pyr(Q') > K. This contradicts Step 15. Hence C is not less than 3K.

**Step 17.** Since C is neither greater than nor less than 3K, we conclude C = 3K. Therefore the cone K is one-third of the cylinder C which has the same base and equal height. QED.

**USED:** 1.41, 10.1, 12.7, 4.6, CN5, D11.18, D11.21
**Human refs (from References field):** 10.1, 11.32, 12.2, 12.7, 4.6, 4.7
**Jaccard:** 0.300 — AI adds ['1.41', 'CN5', 'D11.18', 'D11.21']; Human adds ['11.32', '12.2', '4.7']

## Proposition 12.11
**Statement:** Cones and cylinders which are of the same height are to one another as their bases.

**Step 1.** Let there be two cones (or two cylinders) of the same height, with the cone (or cylinder) on base circle A having height h, and the cone (or cylinder) on base circle B having the same height h. We are to show that cone(A) : cone(B) = circle A : circle B, and likewise cylinder(A) : cylinder(B) = circle A : circle B.

**Step 2.** We first prove the result for cylinders. Suppose cylinder(A) : cylinder(B) is not equal to circle A : circle B. Then let circle A : circle B = cylinder(A) : S, where S is some solid not equal to cylinder(B) [D5.3, D5.5].

**Step 3.** Case 1: Suppose S < cylinder(B). Then cylinder(B) - S is some positive magnitude. Inscribe a regular polygon in circle B such that the difference between circle B and the inscribed polygon is less than the difference between cylinder(B) and S. This is possible by repeatedly bisecting the arcs and applying the principle that we can make the remainder less than any given magnitude [10.1, 12.2 method]. Inscribe the same regular polygon in circle A as well.

**Step 4.** Erect on each inscribed polygon a prism of height h. The prism inscribed in cylinder(A) is contained within cylinder(A), and the prism inscribed in cylinder(B) is contained within cylinder(B) [CN5].

**Step 5.** Since each inscribed polygon can be divided into triangles from the center, each prism can be divided into triangular prisms. By 12.7, each triangular prism equals three pyramids of equal triangular bases and equal height. By 12.6, pyramids of the same height with polygonal bases are to one another as their bases. Therefore the prisms of the same height erected on the two inscribed polygons are to one another as the polygonal bases [12.6, 12.7].

**Step 6.** Now the inscribed polygons, being similar regular polygons inscribed in their respective circles, are to one another as the squares on the diameters of those circles [12.1]. But circles are also to one another as the squares on their diameters [12.2]. Therefore the inscribed polygons are to one another as the circles A and B [5.11, 12.1, 12.2].

**Step 7.** Hence prism(A) : prism(B) = circle A : circle B = cylinder(A) : S [5.11].

**Step 8.** But prism(A) < cylinder(A), since the prism is inscribed in the cylinder [CN5]. Therefore prism(B) < S [5.14]. However, the inscribed polygon was chosen so that the difference between circle B and the polygon is small enough that cylinder(B) - prism(B) < cylinder(B) - S, which gives S < prism(B). This contradicts the conclusion that prism(B) < S. Therefore the case S < cylinder(B) is impossible.

**Step 9.** Case 2: Suppose S > cylinder(B). Then by inversion, circle B : circle A = S : cylinder(A) [5.7]. Since S > cylinder(B), we have cylinder(B) : cylinder(A) relates to circle B : circle A in a way that gives a solid S' < cylinder(A), reducing to Case 1 with the roles of A and B interchanged. By the same argument as above, this too is impossible.

**Step 10.** Since S can be neither less than nor greater than cylinder(B), we conclude S = cylinder(B). Therefore cylinder(A) : cylinder(B) = circle A : circle B [5.9, D5.5].

**Step 11.** Now for cones. By 12.10, cone(A) = (1/3) cylinder(A) and cone(B) = (1/3) cylinder(B). That is, cylinder(A) is triple of cone(A), and cylinder(B) is triple of cone(B), so cone(A) is the same part of cylinder(A) as cone(B) is of cylinder(B) [12.10].

**Step 12.** Since cylinder(A) : cylinder(B) = circle A : circle B (proved above), and cone(A) : cone(B) = cylinder(A) : cylinder(B) by 5.15 (parts of magnitudes in the same ratio are in that ratio), we conclude cone(A) : cone(B) = circle A : circle B [5.15, 5.11].

**Step 13.** Therefore cones and cylinders which are of the same height are to one another as their bases. Q.E.D.

**USED:** 10.1, 12.1, 12.10, 12.2, 12.6, 12.7, 5.11, 5.14, 5.15, 5.7, CN5, D5.3, D5.5
**Human refs (from References field):** 10.1, 12.1, 12.10, 12.2, 12.6, 5.11, 5.16
**Jaccard:** 0.429 — AI adds ['12.7', '5.14', '5.15', '5.7', 'CN5', 'D5.3', 'D5.5']; Human adds ['5.16']

## Proposition 12.12
**Statement:** Similar cones and cylinders are to one another in the triplicate ratio of the diameters in their bases.

**Step 1.** Let there be similar cones and cylinders. We treat the case of cones first; the case of cylinders follows by the same argument. Let the similar cones have bases the circles with diameters ABCD and EFGH, and let the axes (heights) of the cones be KL and MN respectively. Since the cones are similar, by D11.24 the axes and the diameters of the bases are proportional, so ABCD : EFGH :: KL : MN.

**Step 2.** We must show that the cone with base diameter ABCD and height KL is to the cone with base diameter EFGH and height MN in the triplicate ratio of ABCD to EFGH. By D5.10, the triplicate ratio of ABCD to EFGH is the ratio obtained when three ratios each equal to ABCD : EFGH are compounded.

**Step 3.** Let a third proportional O be taken such that ABCD : EFGH :: EFGH : O (by 6.11, a third proportional can be found). Then ABCD has to O the duplicate ratio of that which ABCD has to EFGH, by D5.9.

**Step 4.** Now construct a cylinder (or cone) with the same base as the first cone (circle on diameter ABCD) but with height equal to MN (the height of the second cone). Call this the intermediate cone. By 12.11, cones of the same height are to one another as their bases. The intermediate cone (base on ABCD, height MN) and the second cone (base on EFGH, height MN) have the same height MN. Therefore, the intermediate cone is to the second cone as the circle on ABCD is to the circle on EFGH.

**Step 5.** By 12.2, circles are to one another as the squares on the diameters. Therefore the circle on ABCD is to the circle on EFGH as the square on ABCD is to the square on EFGH. By 6.20 (or equivalently by the construction of D5.9), the square on ABCD is to the square on EFGH in the duplicate ratio of ABCD to EFGH. Hence the intermediate cone is to the second cone in the duplicate ratio of ABCD to EFGH.

**Step 6.** Now consider the first cone (base on ABCD, height KL) and the intermediate cone (base on ABCD, height MN). These two cones share the same base (the circle on ABCD). By 12.11, cones on the same base (which is a special case of equal bases) are to one another as their heights — more precisely, we use the fact that cones on equal bases are to one another as their heights. Since 12.11 gives cones of the same height are as their bases, we apply 11.25 and the general principle: by 12.10, cone = (1/3) cylinder, and cylinders on the same base are as their heights (since a cylinder on a given base with height h equals the base times h, by the reasoning underlying 12.11 and 6.1). Therefore, the first cone is to the intermediate cone as KL is to MN.

**Step 7.** But since the cones are similar, ABCD : EFGH :: KL : MN (by D11.24). Therefore the first cone is to the intermediate cone as ABCD to EFGH.

**Step 8.** We now compound the ratios. We have:
- First cone : Intermediate cone :: ABCD : EFGH (from Step 7)
- Intermediate cone : Second cone :: (ABCD : EFGH) in duplicate ratio (from Step 5)

By 5.22 (ex aequali), the first cone is to the second cone in the ratio compounded of ABCD : EFGH and the duplicate ratio of ABCD : EFGH. This compound is the triplicate ratio of ABCD to EFGH, by D5.10.

**Step 9.** Therefore the first cone is to the second cone in the triplicate ratio of ABCD to EFGH, that is, in the triplicate ratio of the diameters of their bases.

**Step 10.** For cylinders: let the similar cylinders have the same base diameters ABCD, EFGH and heights KL, MN as above (with D11.24 giving ABCD : EFGH :: KL : MN). By 12.10, each cone is one-third of the corresponding cylinder (same base and height). Therefore the first cylinder is triple the first cone, and the second cylinder is triple the second cone. By 5.15, the ratio of the first cylinder to the second cylinder equals the ratio of the first cone to the second cone. Since the first cone is to the second cone in the triplicate ratio of ABCD to EFGH (established above), the first cylinder is also to the second cylinder in the triplicate ratio of the diameters of their bases.

**Step 11.** Therefore, similar cones and cylinders are to one another in the triplicate ratio of the diameters in their bases. Q.E.D.

**USED:** 12.10, 12.11, 12.2, 5.15, 5.22, 6.1, 6.11, 6.20, D11.24, D5.10, D5.9
**Human refs (from References field):** 10.1, 12.10, 12.8, 4.6, 5.12, 5.16, 5.22, 6.5, 6.6, D11.24, D11.9, D6.1
**Jaccard:** 0.150 — AI adds ['12.11', '12.2', '5.15', '6.1', '6.11', '6.20', 'D5.10', 'D5.9']; Human adds ['10.1', '12.8', '4.6', '5.12', '5.16', '6.5', '6.6', 'D11.9', 'D6.1']

## Proposition 12.13
**Statement:** If a cylinder be cut by a plane which is parallel to its opposite planes, then, as the cylinder is to the cylinder, so will the axis be to the axis.

**Step 1.** Let the cylinder AD have axis EF, and let it be cut by the plane GH which is parallel to the opposite planes (the bases) through the circles AB and CD. Let the plane GH meet the axis at K. Then two cylinders are formed: AH with axis EK, and GD with axis KF. We must show that cylinder AH : cylinder GD = axis EK : axis KF.

**Step 2.** Since the plane GH is parallel to the base planes AB and CD, and the cylinder is generated by rotating a rectangle about its axis (D11.21), the cross-section at GH is a circle equal to each of the base circles AB and CD. This follows because the axis EF is perpendicular to both base planes (D11.22, 11.14), and the cutting plane GH, being parallel to these base planes, produces a circular cross-section of the same radius. Thus cylinder AH and cylinder GD stand on equal bases.

**Step 3.** Produce the axis EF in both directions. Along the extension beyond E, set off any number of segments each equal to EK, say EL and LM equal to EK. Along the extension beyond F, set off any number of segments each equal to KF, say FN, NP, and PQ each equal to KF. Through each of the points L, M, N, P, Q draw planes parallel to the base planes AB and CD, cutting out additional cylinders.

**Step 4.** Since EK = EL = LM, the cylinder on base AB with axis EK, the cylinder with axis EL, and the cylinder with axis LM all have equal bases (each cross-section being equal to circle AB by Step 2) and equal heights. Therefore these cylinders are all equal to one another. Thus the cylinder standing on the combined axis ME has height equal to the sum of three segments each equal to EK, and it equals three times cylinder AH. In general, whatever multiple the axis ME is of axis EK, the cylinder on axis ME is the same multiple of cylinder AH.

**Step 5.** Similarly, since KF = FN = NP = PQ, each of the cylinders on these equal axis segments has a base equal to circle CD and the same height KF. These cylinders are therefore all equal to cylinder GD. Thus the cylinder standing on the combined axis KQ has height equal to the sum of four segments each equal to KF, and it equals four times cylinder GD. In general, whatever multiple the axis KQ is of axis KF, the cylinder on axis KQ is the same multiple of cylinder GD.

**Step 6.** Now consider the cylinder on axis MQ (from M to Q through E, K, and F) compared with the cylinder on axis KQ. The cylinder on axis MQ stands on the same base as cylinder AH (equal to circle AB, hence also equal to circle CD), and has height MQ. The cylinder on axis KQ stands on the same base as cylinder GD (equal to circle CD), and has height KQ. But since all cross-sections are equal, both cylinders have equal bases.

**Step 7.** If the axis MK (= ME + EK = 3 EK, the multiple of EK) is equal to the axis KQ (= KF + FN + NP + PQ = 4 KF, the multiple of KF), then the two cylinders on these axes, having equal bases and equal heights, are equal (D11.21, 11.14). If axis MK is greater than axis KQ, then the cylinder on MK is greater than the cylinder on KQ, since it has the same base but greater height. And if axis MK is less, the cylinder on MK is less.

**Step 8.** We have shown: the cylinder on axis ME is an arbitrary equimultiple of cylinder AH, and the cylinder on axis KQ is an arbitrary equimultiple of cylinder GD. Furthermore, the axis ME is the same equimultiple of axis EK that the cylinder on ME is of cylinder AH, and the axis KQ is the same equimultiple of axis KF that the cylinder on KQ is of cylinder GD. And we showed that whichever of the equimultiples of the axes is greater, equal, or less, the corresponding equimultiples of the cylinders are likewise greater, equal, or less.

**Step 9.** Therefore, by the definition of proportion (D5.5), as cylinder AH is to cylinder GD, so is axis EK to axis KF.

**Step 10.** Therefore, if a cylinder be cut by a plane parallel to its opposite planes, then as the cylinder is to the cylinder, so is the axis to the axis. Q.E.D.

**USED:** 11.14, D11.21, D11.22, D11.23, D5.5
**Human refs (from References field):** 12.11, D5.5
**Jaccard:** 0.167 — AI adds ['11.14', 'D11.21', 'D11.22', 'D11.23']; Human adds ['12.11']

## Proposition 12.14
**Statement:** Cones and cylinders which are on equal bases are to one another as their heights.

**Step 1.** Let there be two cylinders, cylinder P on base A with height h and axis of length h, and cylinder Q on base B with height k and axis of length k, where base A is equal to base B. We are to prove that P : Q = h : k.

**Step 2.** Construct a cylinder on the same base A whose total height equals the sum h + k. The axis of this cylinder has length h + k. Cut this cylinder by a plane parallel to its base planes at a distance h from one end. This produces two sub-cylinders: one with base A and axis of length h, and another with base A and axis of length k. The first sub-cylinder is equal to P (same base, same height), and call the second sub-cylinder R, which has base A and axis of length k.

**Step 3.** By 12.13 (if a cylinder is cut by a plane parallel to its opposite planes, then cylinder is to cylinder as axis is to axis), we have P : R = h : k.

**Step 4.** Now R is a cylinder on base A with height k, and Q is a cylinder on base B with height k. Since base A equals base B, the cylinders R and Q are on equal bases and have the same height. By 12.11 (cones and cylinders of the same height are to one another as their bases), R : Q = A : B. Since A = B, we have R : Q = A : A, so R = Q.

**Step 5.** Since R = Q, we may substitute Q for R in the proportion from Step 3. Therefore P : Q = h : k. That is, the cylinders on equal bases are to one another as their heights.

**Step 6.** Now suppose the solids are cones instead of cylinders. Let cone P' stand on base A with height h, and cone Q' stand on base B with height k, where base A equals base B. By 12.10 (any cone is a third part of the cylinder which has the same base and equal height), cone P' is one-third of cylinder P, and cone Q' is one-third of cylinder Q.

**Step 7.** Since P' = (1/3)P and Q' = (1/3)Q, by 5.15 (parts have the same ratio as the same multiples of them), P' : Q' = P : Q. But from Step 5, P : Q = h : k. Therefore P' : Q' = h : k, by 5.11 (ratios equal to the same ratio are equal to one another).

**Step 8.** Therefore cones and cylinders which are on equal bases are to one another as their heights. Q.E.D.

**USED:** 12.10, 12.11, 12.13, 5.11, 5.15
**Human refs (from References field):** 12.10, 12.11, 12.13
**Jaccard:** 0.600 — AI adds ['5.11', '5.15']

## Proposition 12.15
**Statement:** In equal cones and cylinders the bases are reciprocally proportional to the heights; and those cones and cylinders in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let there be equal cones or equal cylinders. Let the first have base B1 and height H1, and the second have base B2 and height H2. We must show that B1 : B2 = H2 : H1. Conversely, given cones or cylinders (of the same kind) with B1 : B2 = H2 : H1, we must show they are equal.

**Step 2.** [Forward direction] Suppose the first cone or cylinder O1 (with base B1, height H1) equals the second cone or cylinder O2 (with base B2, height H2). Construct a third cone or cylinder O3 of the same kind, having base B2 and height H1.

**Step 3.** Since O1 and O3 are cones (or cylinders) of the same height H1, by 12.11 (cones and cylinders of the same height are as their bases), O1 : O3 = B1 : B2.

**Step 4.** Since O3 and O2 are cones (or cylinders) on the same base B2, by 12.14 (cones and cylinders on equal bases are as their heights), O3 : O2 = H1 : H2.

**Step 5.** Since O1 = O2 by hypothesis, O3 has the same ratio to each of them. That is, O3 : O1 = O3 : O2, by 5.7 (equal magnitudes have the same ratio to the same magnitude).

**Step 6.** From Step 4, O3 : O2 = H1 : H2. Combined with Step 5, we obtain O3 : O1 = H1 : H2.

**Step 7.** From Step 3, O1 : O3 = B1 : B2. By the definition of inverse ratio (D5.13), O3 : O1 = B2 : B1.

**Step 8.** From Steps 6 and 7, B2 : B1 = H1 : H2. By the definition of inverse ratio (D5.13) applied again, B1 : B2 = H2 : H1. This establishes that in equal cones or cylinders the bases are reciprocally proportional to the heights.

**Step 9.** [Converse direction] Now suppose that in cones or cylinders of the same kind, B1 : B2 = H2 : H1. We must show that O1 = O2. Again let O3 be a cone or cylinder of the same kind with base B2 and height H1.

**Step 10.** As in Step 3, by 12.11, O1 : O3 = B1 : B2.

**Step 11.** By hypothesis, B1 : B2 = H2 : H1. Therefore O1 : O3 = H2 : H1 (by 5.11, ratios equal to the same ratio are equal to each other).

**Step 12.** As in Step 4, by 12.14, O3 : O2 = H1 : H2. By the definition of inverse ratio (D5.13), O2 : O3 = H2 : H1.

**Step 13.** From Steps 11 and 12, O1 : O3 = O2 : O3 (both equal H2 : H1), by 5.11.

**Step 14.** Since O1 and O2 have the same ratio to O3, by 5.9 (magnitudes which have the same ratio to the same are equal), O1 = O2.

**Step 15.** Therefore in equal cones and cylinders the bases are reciprocally proportional to the heights, and cones and cylinders in which the bases are reciprocally proportional to the heights are equal. Q.E.D.

**USED:** 12.11, 12.14, 5.11, 5.7, 5.9, D5.13
**Human refs (from References field):** 12.11, 12.13, 5.11, 5.7, 5.9
**Jaccard:** 0.571 — AI adds ['12.14', 'D5.13']; Human adds ['12.13']

## Proposition 12.16
**Statement:** Given two circles about the same centre, to inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle.

**Step 1.** Let two circles be given about the same centre A, with BCDE being the greater circle and FGHK the lesser circle. We must inscribe in circle BCDE an equilateral polygon with an even number of sides which does not touch circle FGHK. [D1.15, D1.16]

**Step 2.** Draw a diameter BD of the greater circle BCDE through the centre A. [D1.17, P1]

**Step 3.** From A, draw the line AC at right angles to BD, and produce it to meet the circle at E on the opposite side, so that CE is also a diameter perpendicular to BD. [1.11, P2]

**Step 4.** Join BC, CD, DE, EB. Then BCDE is a square inscribed in the greater circle, since the four arcs BC, CD, DE, EB are equal (each being a quadrant), so the four chords are equal, making BCDE equilateral with four sides (an even number). [P1, 3.29]

**Step 5.** Now either the square BCDE does not touch the lesser circle FGHK, or it does. If the square does not touch the lesser circle, then we have inscribed in the greater circle an equilateral polygon with an even number of sides (namely four) that does not touch the lesser circle, and the construction is complete.

**Step 6.** Suppose then that side BC (and by symmetry each side) does touch or intersect the lesser circle FGHK. Let L be the point where the perpendicular from A meets BC, so that AL is perpendicular to BC. Then AL falls on or within the lesser circle, meaning AL is less than or equal to AF, the radius of the lesser circle. [1.12]

**Step 7.** Now bisect each of the arcs BC, CD, DE, EB at their midpoints, obtaining eight equal arcs. Join the consecutive endpoints to form a regular octagon inscribed in the greater circle. This octagon is equilateral with eight sides (an even number). [3.30, P1]

**Step 8.** Let BM be a side of this octagon (where M is the midpoint of arc BC). Draw the perpendicular AN from A to BM. Since the arc BM is half of arc BC, the chord BM subtends a smaller arc than BC does. By Proposition 3.15, a chord nearer to the centre is longer than one further from the centre, and conversely a shorter chord (subtending a smaller arc) is further from the centre. Therefore AN, the perpendicular distance from A to BM, is greater than AL, the perpendicular distance from A to BC. [3.15]

**Step 9.** If AN is greater than the radius AF of the lesser circle, then side BM does not touch the lesser circle, and by symmetry no side of the octagon touches the lesser circle. In that case, the regular octagon is the desired polygon and the construction is complete.

**Step 10.** If AN is still not greater than AF, continue bisecting: bisect each of the eight arcs to obtain sixteen equal arcs, forming a regular 16-gon inscribed in the greater circle. By the same reasoning as in Step 8, the perpendicular distance from A to each side of the 16-gon is greater than AN. Continue this process of successive bisection. [3.30]

**Step 11.** At each stage of bisection, we pass from a 2^k-gon to a 2^(k+1)-gon (always an even number of sides), and the perpendicular distance from A to each side strictly increases. The difference between the radius AB of the greater circle and the perpendicular distance from A to each side decreases at each step. By Proposition 10.1, if from a magnitude (here AB minus the perpendicular distance) there is subtracted more than its half (which each bisection achieves, since the perpendicular distance increases and the residual decreases by more than half), then by repeating the process we can make the remainder less than any assigned magnitude. [10.1, CN5]

**Step 12.** Take as the assigned magnitude the difference AB minus AF (i.e., the difference between the radius of the greater circle and the radius of the lesser circle; this is positive since BCDE is the greater circle). By 10.1, after sufficiently many bisections, the difference between AB and the perpendicular distance from A to a side becomes less than AB minus AF. Therefore the perpendicular distance from A to each side exceeds AF. [10.1]

**Step 13.** When the perpendicular distance from A to each side of the inscribed polygon exceeds AF (the radius of the lesser circle), no side of the polygon touches or intersects the lesser circle FGHK, since every point on a side is at distance from A at least equal to the perpendicular distance, which exceeds AF. [3.15]

**Step 14.** The resulting polygon is equilateral (all sides subtend equal arcs, hence are equal chords), has an even number of sides (being 4 times a power of 2), and is inscribed in the greater circle BCDE. It does not touch the lesser circle FGHK. [3.29, D4.3]

**Step 15.** Therefore, given two circles about the same centre, we have inscribed in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle. Q.E.F.

**USED:** 1.11, 1.12, 10.1, 3.15, 3.29, 3.30, CN5, D1.15, D1.16, D1.17, D4.3, P1, P2
**Human refs (from References field):** 1.4, 10.1, 3.16, 3.3
**Jaccard:** 0.062 — AI adds ['1.11', '1.12', '3.15', '3.29', '3.30', 'CN5', 'D1.15', 'D1.16', 'D1.17', 'D4.3', 'P1', 'P2']; Human adds ['1.4', '3.16', '3.3']

## Proposition 12.17
**Statement:** Given two spheres about the same centre, to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface.

**Step 1.** Let there be two spheres about the same centre A, and let it be required to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface. Let the spheres be cut by any plane through the centre A. The sections will be circles [D11.14], the greater circle being in the greater sphere and the lesser in the lesser sphere, since the centre of the sphere is also the centre of the circle [D11.16]. Let these circles have centre A.

**Step 2.** Draw two diameters of the greater circle, BC and DE, at right angles to one another [1.11]. These diameters also pass through A, the common centre of both spheres.

**Step 3.** By Proposition 12.16, inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle. Let the sides of this polygon in the quadrant BE be BF, FG, GH, HE, and let the corresponding sides be placed similarly in the other quadrants by symmetry.

**Step 4.** Since the polygon is equilateral with an even number of sides and is inscribed in the greater circle, and does not touch the lesser circle, the perpendicular from A to any side of the polygon is greater than the radius of the lesser sphere. In particular, let AK be the perpendicular from A to the side BF [1.12]. Then AK is greater than the radius of the lesser sphere.

**Step 5.** Now set up the construction in three dimensions. Let the plane of the circle BDCE be a base plane. Through the diameter BD, erect a plane perpendicular to the plane BDCE [11.12]. In this perpendicular plane, the great circle through BD will also have centre A and the same radius as circle BDCE [D11.17].

**Step 6.** In each great circle plane through the diameter BD that is perpendicular to the base, the same polygon can be inscribed with sides equal to those of the polygon in the base circle, since all great circles of the sphere have the same radius [D11.17, 12.16]. Thus we inscribe the same equilateral polygon in each such great circle.

**Step 7.** Now connect the vertices: the polygon in the base plane has vertices such as F, G, H on the semicircle BED. Through each of these vertices, pass a plane parallel to the plane of the circle through BD perpendicular to BE [11.15]. Each such plane cuts the sphere in a lesser circle.

**Step 8.** Consider the plane through F parallel to the equatorial plane containing DE. This plane cuts the sphere in a circle with centre on the line BA [11.17 applied via the geometry of the sphere]. Let this circle have centre N, where N lies on BA. The radius NF of this circle is the distance from N to F.

**Step 9.** On each of these lesser circles, the corresponding vertices of the polygons inscribed in the various great circles through BD all lie, forming a regular polygon inscribed in that lesser circle [1.4, 3.14]. Connect adjacent vertices on each such lesser circle, and connect corresponding vertices on adjacent parallel circles, forming triangular and quadrilateral faces.

**Step 10.** The resulting solid figure is bounded by polygonal faces (triangles and quadrilaterals) whose vertices all lie on the greater sphere. Therefore, the polyhedral solid is inscribed in the greater sphere [D11.1, D11.2].

**Step 11.** It remains to show that this polyhedral solid does not touch the lesser sphere. Consider any face of the polyhedron. Draw the perpendicular from the centre A to the plane of that face [11.11]. This perpendicular is the shortest distance from A to that plane [11.38].

**Step 12.** Consider a face on the side surface of the polyhedron, such as a quadrilateral face BFQP where Q and P are corresponding vertices in an adjacent great-circle plane. The perpendicular from A to this face falls within the face or its plane. Now BF is a side of the inscribed polygon, and the perpendicular from A to line BF has length AK [from Step 4].

**Step 13.** The perpendicular distance from A to the plane of any face of the polyhedron is at least as great as the perpendicular distance from A to any edge of that face, which in turn is at least AK [1.19, 11.38]. Since AK is greater than the radius of the lesser sphere [Step 4, from 12.16], the perpendicular from A to every face is greater than the radius of the lesser sphere.

**Step 14.** Since every face of the polyhedral solid has the property that the perpendicular distance from the centre A to the plane of that face exceeds the radius of the lesser sphere, no face can touch or intersect the surface of the lesser sphere [D11.3, 3.16 applied to the cross-sections]. The lesser sphere, being a surface of revolution at fixed distance from A, lies entirely within the interior of the polyhedron.

**Step 15.** Therefore, a polyhedral solid has been inscribed in the greater sphere which does not touch the lesser sphere at its surface, which is what was required to be done.

**USED:** 1.11, 1.12, 1.19, 1.4, 11.11, 11.12, 11.15, 11.17, 11.38, 12.16, 3.14, 3.16, D11.1, D11.14, D11.16, D11.17, D11.2, D11.3
**Human refs (from References field):** 1.26, 1.33, 1.47, 11.11, 11.18, 11.2, 11.6, 11.7, 11.9, 3.27, 3.31, 6.2, 6.8, D11.14, D11.3, D11.4
**Jaccard:** 0.097 — AI adds ['1.11', '1.12', '1.19', '1.4', '11.12', '11.15', '11.17', '11.38', '12.16', '3.14', '3.16', 'D11.1', 'D11.16', 'D11.17', 'D11.2']; Human adds ['1.26', '1.33', '1.47', '11.18', '11.2', '11.6', '11.7', '11.9', '3.27', '3.31', '6.2', '6.8', 'D11.4']

## Proposition 12.18
**Statement:** Spheres are to one another in the triplicate ratio of their respective diameters.

**Step 1.** Let there be two spheres with centres A and B, and let their diameters be CD and EF respectively. We must show that sphere CD is to sphere EF in the triplicate ratio of CD to EF.

**Step 2.** Suppose, for contradiction, that sphere CD is not to sphere EF in the triplicate ratio of CD to EF. Then sphere CD has to some magnitude either less than or greater than sphere EF the triplicate ratio of CD to EF. First, let it have that ratio to a magnitude G less than sphere EF.

**Step 3.** Let sphere EF be conceived as set about centre B. Then G is less than sphere EF. By 12.17, we can inscribe in sphere EF a polyhedral solid that does not touch the lesser sphere corresponding to magnitude G; that is, we inscribe a polyhedron in sphere EF such that the polyhedron is greater than G (since the polyhedron lies within sphere EF but outside the concentric sphere whose volume corresponds to G).

**Step 4.** Now inscribe in sphere CD a polyhedron similar to the polyhedron inscribed in sphere EF, using similar polygonal faces arranged similarly. By 12.17 and the construction, this is possible.

**Step 5.** The similar polyhedral solids inscribed in the two spheres are to one another in the triplicate ratio of their corresponding sides. Since the polyhedra are inscribed in the spheres, the corresponding sides are proportional to the diameters CD and EF of the respective spheres. Therefore the polyhedron in sphere CD is to the polyhedron in sphere EF in the triplicate ratio of CD to EF, by 12.8 (similar pyramids with triangular bases are in the triplicate ratio of corresponding sides), since each polyhedron can be decomposed into pyramids with triangular bases from the centre, and the pyramids in one solid are similar to the corresponding pyramids in the other, and by 12.8 each pair is in the triplicate ratio of corresponding sides, and by 5.12 (alternando) and 5.22 (ex aequali through ratios) the totals maintain the same ratio.

**Step 6.** But sphere CD is to G in the triplicate ratio of CD to EF, by our assumption. Therefore, as the polyhedron in sphere CD is to the polyhedron in sphere EF, so is sphere CD to G, by 5.11 (ratios that are the same as the same ratio are the same as one another, via the definition of triplicate ratio and CN1).

**Step 7.** By alternando (5.16), as sphere CD is to the polyhedron in sphere CD, so is G to the polyhedron in sphere EF.

**Step 8.** Now sphere CD is greater than the polyhedron inscribed in it (since the polyhedron is contained within the sphere), so by CN5 the sphere is greater than the inscribed polyhedron. Therefore G is greater than the polyhedron in sphere EF, by 5.14 (if the first is greater than the second, the third is also greater than the fourth when ratios are equal).

**Step 9.** But the polyhedron inscribed in sphere EF was constructed to be greater than G (Step 3). So G is both greater than the polyhedron and less than the polyhedron, which is impossible. Therefore the assumption that sphere CD has to a magnitude G less than sphere EF the triplicate ratio of CD to EF leads to contradiction.

**Step 10.** Now suppose sphere CD has to a magnitude G greater than sphere EF the triplicate ratio of CD to EF. Then by inversion (5.13), G is to sphere CD in the triplicate ratio of EF to CD. Since G is greater than sphere EF, apply the same argument with the roles of the spheres exchanged: sphere EF has to some magnitude less than sphere CD a ratio equal to the triplicate ratio of EF to CD.

**Step 11.** But by the same argument as in Steps 2 through 9, applied with the spheres interchanged, this leads to a contradiction. Therefore sphere CD cannot have to any magnitude greater than sphere EF the triplicate ratio of CD to EF.

**Step 12.** Since sphere CD has the triplicate ratio of CD to EF neither to a magnitude less than sphere EF nor to one greater, it must have it to sphere EF itself. That is, sphere CD is to sphere EF in the triplicate ratio of diameter CD to diameter EF.

**Step 13.** Therefore, spheres are to one another in the triplicate ratio of their respective diameters. Q.E.D.

**USED:** 12.17, 12.8, 5.11, 5.13, 5.14, 5.16, 5.22, CN1, CN5, D11.14, D11.17, D5.10
**Human refs (from References field):** 12.17, 12.2, 5.16
**Jaccard:** 0.154 — AI adds ['12.8', '5.11', '5.13', '5.14', '5.22', 'CN1', 'CN5', 'D11.14', 'D11.17', 'D5.10']; Human adds ['12.2']
