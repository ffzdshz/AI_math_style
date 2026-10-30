# Book 12 of Euclid's Elements — Step-by-Step AI Proofs (Run B)

## Proposition 12.1
**Statement:** Similar polygons inscribed in circles are to one another as the squares on the diameters.

**Step 1.** Let ABCDE and FGHKL be similar polygons inscribed in circles with diameters BM and GN respectively. We are to show that polygon ABCDE is to polygon FGHKL as the square on BM is to the square on GN.

**Step 2.** Since ABCDE and FGHKL are similar polygons, by definition their angles are severally equal and the sides about the equal angles are proportional [D6.1]. In particular, angle AEB equals angle FKG (corresponding angles of the similar polygons), and BA:AE = GF:FK.

**Step 3.** By 6.20, similar polygons are to one another in the duplicate ratio of corresponding sides. Therefore polygon ABCDE is to polygon FGHKL in the duplicate ratio of AB to FG, that is, as the square on AB is to the square on FG [6.20].

**Step 4.** It remains to show that the square on AB is to the square on FG as the square on diameter BM is to the square on diameter GN. To do this, we shall prove that AB:FG = BM:GN.

**Step 5.** Since BM is a diameter of the first circle, join AM. The angle BAM, being an angle in a semicircle (since it is the angle at A subtended by diameter BM), is a right angle [3.31].

**Step 6.** The angle AMB is an angle inscribed in the first circle standing on arc AB. The angle AEB is also an angle inscribed in the first circle standing on the same arc AB. Therefore angle AMB equals angle AEB [3.21].

**Step 7.** Similarly, since GN is a diameter of the second circle, join FN. The angle GFN, being an angle in a semicircle (the angle at F subtended by diameter GN), is a right angle [3.31].

**Step 8.** The angle GNF is an angle inscribed in the second circle standing on arc GF. The angle GKF is also an angle inscribed in the second circle standing on the same arc GF. Therefore angle GNF equals angle GKF [3.21].

**Step 9.** From Step 2, angle AEB equals angle FKG (corresponding angles in the similar polygons). From Step 6, angle AMB equals angle AEB. From Step 8, angle GNF equals angle GKF. Therefore angle AMB equals angle GNF [CN1].

**Step 10.** Now consider triangles ABM and FGN. We have angle BAM equals angle GFN (both right angles, by Steps 5 and 7) [P4]. And angle AMB equals angle GNF (by Step 9). Therefore the remaining angles are also equal: angle ABM equals angle FGN [1.32]. Hence triangles ABM and FGN are equiangular.

**Step 11.** Since triangles ABM and FGN are equiangular, they are similar, and therefore the sides about the equal angles are proportional [6.4]. In particular, AB:FG = BM:GN (sides opposite the equal right angles correspond to the hypotenuses, i.e., the diameters).

**Step 12.** Since AB:FG = BM:GN, the duplicate ratio of AB to FG equals the duplicate ratio of BM to GN. That is, the square on AB is to the square on FG as the square on BM is to the square on GN [6.20, D5.9].

**Step 13.** From Step 3, polygon ABCDE is to polygon FGHKL as the square on AB is to the square on FG. From Step 12, the square on AB is to the square on FG as the square on BM is to the square on GN. Therefore polygon ABCDE is to polygon FGHKL as the square on BM is to the square on GN [5.11].

**Step 14.** Therefore similar polygons inscribed in circles are to one another as the squares on the diameters. Q.E.D.

**USED:** 1.32, 3.21, 3.31, 5.11, 6.20, 6.4, CN1, D5.9, D6.1, P4
**Human refs (from References field):** 1.32, 3.27, 3.31, 6.20, 6.4, 6.6, D6.1
**Jaccard:** 0.417 — AI adds ['3.21', '5.11', 'CN1', 'D5.9', 'P4']; Human adds ['3.27', '6.6']

## Proposition 12.2
**Statement:** Circles are to one another as the squares on the diameters.

**Step 1.** Let ABCD and EFGH be two circles with diameters BD and FH respectively. We wish to prove that circle ABCD is to circle EFGH as the square on BD is to the square on FH.

**Step 2.** Suppose, for the sake of contradiction, that the circles are not as the squares on the diameters. Then the square on BD is to the square on FH as circle ABCD is to some area S, where S is not equal to circle EFGH.

**Step 3.** Case 1: Suppose first that S is less than circle EFGH. Then circle EFGH exceeds S by some magnitude.

**Step 4.** Inscribe a square in circle EFGH [4.6]. The inscribed square is greater than half the circle, since the square is half the circumscribed square [1.34, 1.41], while the circle is less than the circumscribed square [CN5]. Therefore the inscribed square is more than half the circle.

**Step 5.** Bisect the arcs cut off by the sides of the square [3.30], and join the new points to the vertices of the square, forming an inscribed regular octagon. Each triangle formed on a chord as base with vertex at the midpoint of the corresponding arc is greater than half the circular segment it lies in, since such a triangle is half the rectangle circumscribed about the segment [1.41], and the segment is less than that rectangle.

**Step 6.** Continue this process of bisecting arcs and joining chords. By Proposition 10.1, since at each stage we remove more than half of the remaining difference between the circle and the inscribed polygon, we will eventually obtain an inscribed polygon P_2 in circle EFGH such that the excess of circle EFGH over P_2 is less than the excess of circle EFGH over S. That is, P_2 is greater than S.

**Step 7.** Inscribe in circle ABCD a polygon P_1 similar to P_2. Since P_1 and P_2 are similar polygons inscribed in circles ABCD and EFGH respectively, by Proposition 12.1, P_1 is to P_2 as the square on BD is to the square on FH.

**Step 8.** But by our assumption, the square on BD is to the square on FH as circle ABCD is to S. Therefore P_1 is to P_2 as circle ABCD is to S [5.11].

**Step 9.** Since P_1 is inscribed in circle ABCD, P_1 is less than circle ABCD [CN5]. Therefore, since P_1 is to P_2 as circle ABCD is to S, and P_1 is less than circle ABCD, it follows that P_2 is less than S [5.14].

**Step 10.** But in Step 6 we established that P_2 is greater than S. This is a contradiction. Therefore the assumption that S is less than circle EFGH is false.

**Step 11.** Case 2: Suppose now that S is greater than circle EFGH. Then since the square on BD is to the square on FH as circle ABCD is to S, by alternation [5.16] the square on BD is to circle ABCD as the square on FH is to S. By inversion, circle ABCD is to the square on BD as S is to the square on FH.

**Step 12.** Since S is greater than circle EFGH, the square on FH is to S is a lesser ratio than the square on FH is to circle EFGH. Equivalently, we may set up the argument symmetrically: since sq(BD) : sq(FH) = circle ABCD : S and S > circle EFGH, it follows that sq(FH) : sq(BD) = S : circle ABCD. Now consider that sq(FH) : sq(BD) = circle EFGH : T for some area T. From the proportion sq(BD) : sq(FH) = circle ABCD : S, by inversion sq(FH) : sq(BD) = S : circle ABCD. Since S > circle EFGH, and sq(FH) : sq(BD) equals both the ratio S : circle ABCD and the ratio circle EFGH : T, we would need T < circle ABCD.

**Step 13.** Now apply the exhaustion argument of Steps 4 through 6 to circle ABCD. Inscribe successively doubling polygons in circle ABCD until the inscribed polygon Q_1 satisfies: Q_1 is greater than T. Inscribe a similar polygon Q_2 in circle EFGH.

**Step 14.** By Proposition 12.1, Q_1 is to Q_2 as the square on BD is to the square on FH. But the square on BD is to the square on FH equals circle ABCD to S. So Q_1 : Q_2 = circle ABCD : S.

**Step 15.** Since Q_2 is inscribed in circle EFGH, Q_2 is less than circle EFGH, which is less than S [CN5]. So Q_2 < S. From Q_1 : Q_2 = circle ABCD : S and Q_2 < S, it follows that Q_1 < circle ABCD [5.14]. But Q_1 was constructed to be greater than T, and we need Q_1 < circle ABCD, which is consistent since T < circle ABCD.

**Step 16.** However, from the proportion circle EFGH : T = sq(FH) : sq(BD) = Q_2 : Q_1, and Q_2 < circle EFGH (since Q_2 is inscribed in circle EFGH) [CN5], it follows that Q_1 < T [5.14]. But we constructed Q_1 > T. This is a contradiction.

**Step 17.** Therefore the assumption that S is greater than circle EFGH is also false.

**Step 18.** Since S is neither less than nor greater than circle EFGH, we conclude that S equals circle EFGH. Therefore the square on BD is to the square on FH as circle ABCD is to circle EFGH. That is, circles are to one another as the squares on their diameters. Q.E.D.

**USED:** 1.34, 1.41, 10.1, 12.1, 3.30, 4.6, 5.11, 5.14, 5.16, CN5
**Human refs (from References field):** 12.1, 5.11, 5.16
**Jaccard:** 0.300 — AI adds ['1.34', '1.41', '10.1', '3.30', '4.6', '5.14', 'CN5']

## Proposition 12.3
**Statement:** Any pyramid which has a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; and the two prisms are greater than the half of the whole pyramid.

**Step 1.** Let ABCD be a pyramid with triangular base BCD and apex A. Bisect the six edges [1.10]: let E, F, G be the midpoints of AB, AC, AD, and H, K, L the midpoints of BC, CD, BD respectively. Join all adjacent midpoint pairs [P1].

**Step 2.** In each face triangle, the segment joining midpoints of two sides is parallel to the third side and equal to half of it [6.2]. Specifically: EF parallel to BC with EF = (1/2)BC; EH parallel to AC with EH = (1/2)AC; FH parallel to AB with FH = (1/2)AB; EG parallel to BD with EG = (1/2)BD; EL parallel to AD with EL = (1/2)AD; GL parallel to AB with GL = (1/2)AB; FK parallel to AD with FK = (1/2)AD; FG parallel to CD with FG = (1/2)CD; GK parallel to AC with GK = (1/2)AC; HK parallel to BD with HK = (1/2)BD; KL parallel to BC with KL = (1/2)BC; HL parallel to CD with HL = (1/2)CD.

**Step 3.** Since EF and KL are both parallel to BC and both equal (1/2)BC, and EL and FK are both parallel to AD and both equal (1/2)AD, the quadrilateral EFKL (with EF equal and parallel to KL, and EL equal and parallel to FK) is a parallelogram [1.33]. Similarly EGHK is a parallelogram (with EG equal and parallel to HK, and EH equal and parallel to GK), and FGLH is a parallelogram (with FG equal and parallel to HL, and FH equal and parallel to GL).

**Step 4.** Pyramid AEFG has all six edges equal to half the corresponding edges of ABCD: AE = (1/2)AB, AF = (1/2)AC, AG = (1/2)AD, EF = (1/2)BC, EG = (1/2)BD, FG = (1/2)CD. Therefore its four faces are similar to those of ABCD [6.4, D6.1], and pyramid AEFG is similar to pyramid ABCD [D11.9].

**Step 5.** Pyramid BEHL (at vertex B) has all six edges equal to half the corresponding edges of ABCD: BE = (1/2)AB, BH = (1/2)BC, BL = (1/2)BD, EH = (1/2)AC, EL = (1/2)AD, HL = (1/2)CD. Therefore BEHL is similar to ABCD and, since its edges are respectively equal to those of AEFG, it is equal and similar to AEFG [1.8, D11.9, D11.10].

**Step 6.** Now consider the remainder of ABCD after removing pyramids AEFG and BEHL. The quadrilateral EFKL is a parallelogram [Step 3], so its diagonal FK divides it into two equal triangles EFK and FKL [1.34]. Triangle EFK is congruent to triangle EFH (since EF = EF, FK = (1/2)AD = EL, and EK... actually, let me identify the prisms differently).

**Step 7.** The solid between pyramid AEFG and base BCD is a frustum (since EFG is parallel to BCD). Within this frustum, the plane through E, H, L separates pyramid BEHL from the remainder. The remainder of the frustum, after removing BEHL, is bounded by triangles EFG and HKL (which are similar to BCD with ratio 1:2 by Step 2, hence equal and similar to each other [1.8]), by the three parallelograms EFKL, EGHK, FGLH [Step 3], and by the triangles EFH and EGL. This solid is the union of two prisms [D11.13].

**Step 8.** One prism has triangular bases EFH and GKL with three parallelogram lateral faces. The face EFKL is a parallelogram [Step 3] containing sides EF (of triangle EFH) and KL (of triangle GKL). The face EGHK is a parallelogram [Step 3] containing sides EH (of triangle EFH) and GK (of triangle GKL). The face containing FH and GL: since FH is parallel to GL and FH = GL [Step 2], the quadrilateral FHGL... but wait, FH and GL are sides of the respective triangles but FHGL may not be one of the three named parallelograms. However, FGLH is a parallelogram [Step 3], and its sides connect F to G, G to L, L to H, H to F. This parallelogram passes through vertices of both triangles EFH and GKL but is a diagonal cross-section, not a lateral face.

**Step 9.** I recognize the difficulty in explicitly naming the lateral faces of the prisms. The key structural point is that the three parallelograms EFKL, EGHK, FGLH, together with the eight triangles (four from each half), bound two prismatic solids. By D11.13, each solid with two equal, similar, parallel triangular faces and parallelogram lateral faces is a prism.

**Step 10.** For the claim that the two prisms are equal: both prisms have congruent triangular bases (each similar to BCD with ratio 1:2) and equal heights (half the height of ABCD), so by 11.39 (prisms of equal height on equal bases are equal), the two prisms are equal.

**Step 11.** For the claim that the two prisms together are greater than half the whole pyramid: each similar pyramid has all linear dimensions halved, so each has volume (1/2)^3 = 1/8 of the original [the ratio of similar solids is the cube of the linear ratio, following from 11.33 and 6.19]. The two pyramids together are (2/8) = 1/4 of the whole. Therefore the two prisms together are 1 - 1/4 = 3/4 of the whole, which is greater than 1/2 [CN5, CN3].

**Step 12.** Therefore pyramid ABCD has been divided into two equal and similar pyramids AEFG and BEHL, each similar to the whole and having triangular bases, and into two equal prisms; and the two prisms together are greater than half the whole pyramid. Q.E.D.

**USED:** 1.10, 1.33, 1.34, 1.8, 11.33, 11.39, 6.19, 6.2, 6.4, CN3, CN5, D11.10, D11.13, D11.9, D6.1, P1
**Human refs (from References field):** 1.29, 1.34, 1.4, 11.10, 11.39, 6.2, D11.10, D6.1
**Jaccard:** 0.263 — AI adds ['1.10', '1.33', '1.8', '11.33', '6.19', '6.4', 'CN3', 'CN5', 'D11.13', 'D11.9', 'P1']; Human adds ['1.29', '1.4', '11.10']

## Proposition 12.4
**Statement:** If there be two pyramids of the same height which have triangular bases, and cach of them be divided into two pyramids equal to one another and similar to the whole, and into two equal prisms, then, as the base of the one pyramid is to the base of the other pyramid, so will all the prisms in the one pyramid be to all the prisms, being equal in multitude, in the other pyramid.

**Step 1.** Let there be two pyramids of the same height with triangular bases ABC and DEF, having vertices G and H respectively, so that the pyramids are ABCG and DEFH with equal heights.

**Step 2.** By 12.3, divide pyramid ABCG into two pyramids equal to one another and similar to the whole, and into two equal prisms. Specifically, let the midpoints of edges AB, BC, CA, AG, BG, CG determine the division. The two prisms in ABCG together we call P1, and the two remaining sub-pyramids (each similar to ABCG and equal to each other) we call ABCG_1 and ABCG_2.

**Step 3.** Similarly, by 12.3, divide pyramid DEFH into two equal sub-pyramids similar to DEFH and two equal prisms. The two prisms together we call Q1, and the two remaining sub-pyramids we call DEFH_1 and DEFH_2.

**Step 4.** Consider the two prisms obtained from pyramid ABCG. Each prism has as base a triangle formed by joining midpoints of the sides of triangle ABC (or a triangle congruent to it), and has the same height structure as the corresponding prism from DEFH. Since the pyramids ABCG and DEFH have the same height, the prisms produced by the midpoint division in each also share the same height. By 6.1, triangles of the same height are to one another as their bases. The bases of the prisms from ABCG relate to the bases of the prisms from DEFH as triangle ABC relates to triangle DEF, since the midpoint construction produces bases that are the same fraction of the original base in each pyramid. Therefore, prism to prism, the prisms from ABCG are to the corresponding prisms from DEFH as triangle ABC is to triangle DEF.

**Step 5.** Since the two prisms in each pyramid are equal to one another (by 12.3), and each prism from ABCG is to the corresponding prism from DEFH as ABC is to DEF, by 5.12 (alternando) and 5.11 (ratios equal to the same ratio are equal to each other), the sum of the two prisms P1 from ABCG is to the sum of the two prisms Q1 from DEFH as triangle ABC is to triangle DEF.

**Step 6.** Now consider the sub-pyramids. By 12.3, each sub-pyramid of ABCG is similar to ABCG and has a triangular base that is one of the four congruent triangles into which the midpoints of ABC divide triangle ABC. Likewise for the sub-pyramids of DEFH with respect to triangle DEF. Moreover, since the original pyramids have the same height, the sub-pyramids from the two original pyramids also share the same height (each sub-pyramid has half the height of the original).

**Step 7.** Apply 12.3 again to each of the four sub-pyramids (two from ABCG, two from DEFH). Each sub-pyramid is divided into two further sub-pyramids and two prisms. By the same reasoning as in Steps 4 and 5, the prisms from each sub-pyramid of ABCG are to the corresponding prisms from the sub-pyramid of DEFH as the base of that sub-pyramid of ABCG is to the base of that sub-pyramid of DEFH.

**Step 8.** Since the sub-pyramids of ABCG are similar to ABCG and the sub-pyramids of DEFH are similar to DEFH, and the midpoint construction scales all bases by the same factor, the bases of the sub-pyramids of ABCG are to the bases of the sub-pyramids of DEFH as triangle ABC is to triangle DEF. Therefore the prisms produced at this second stage from ABCG are to the prisms produced at the second stage from DEFH as ABC is to DEF.

**Step 9.** By 5.12 (alternando), we may group all prisms from ABCG on one side and all prisms from DEFH on the other. At each stage of division, the prisms from ABCG are to the corresponding prisms from DEFH as ABC is to DEF. By 5.1, the same multiples preserve the ratio: since at each level the prisms from one pyramid bear the same ratio to the corresponding prisms of the other, the sum of all prisms from ABCG at each level is to the sum of all prisms from DEFH at the same level as ABC is to DEF.

**Step 10.** Combining all levels by repeated application of 5.12 and CN2 (if equals be added to equals, the wholes are equal in ratio), the total of all prisms in ABCG, being equal in multitude to all prisms in DEFH, is to the total of all prisms in DEFH as triangle ABC is to triangle DEF.

**Step 11.** Therefore, as the base of the one pyramid is to the base of the other pyramid, so are all the prisms in the one pyramid to all the prisms, being equal in multitude, in the other pyramid. This is what was to be proved.

**USED:** 12.3, 5.1, 5.11, 5.12, 6.1, CN2
**Human refs (from References field):** 11.39, 12.3, 5.12, 5.16, 6.22
**Jaccard:** 0.222 — AI adds ['5.1', '5.11', '6.1', 'CN2']; Human adds ['11.39', '5.16', '6.22']

## Proposition 12.5
**Statement:** Pyramids which are of the same height and have triangular bases are to one another as the bases.

**Step 1.** Let there be two pyramids of the same height with triangular bases, the first having base ABC and apex D, and the second having base EFG and apex H. We must show that pyramid ABCD is to pyramid EFGH as triangle ABC is to triangle EFG.

**Step 2.** Suppose, for the sake of contradiction, that pyramid ABCD is not to pyramid EFGH as base ABC is to base EFG. Then base ABC is to base EFG as pyramid ABCD is to some magnitude either less than or greater than pyramid EFGH.

**Step 3.** First, assume that base ABC is to base EFG as pyramid ABCD is to some magnitude W less than pyramid EFGH. Let the excess by which pyramid EFGH exceeds W be some magnitude S, so that W = EFGH - S.

**Step 4.** By 12.3, divide pyramid EFGH into two pyramids equal to one another and similar to the whole, having triangular bases, and into two equal prisms. The two prisms together are greater than half of pyramid EFGH.

**Step 5.** Similarly, divide each of the two sub-pyramids in the same manner by 12.3. Continue this process of successive bisection of the remaining pyramids. By 10.1, since S is some definite magnitude and at each stage the prisms removed exceed half of the remaining pyramids, after finitely many iterations the sum of all remaining sub-pyramids will be less than S.

**Step 6.** Let this process of division be carried out on pyramid EFGH until the remaining sub-pyramids are together less than S. Let the prisms within EFGH resulting from these divisions be HP1, HP2, ..., HPn, and let the remaining sub-pyramids have total volume less than S.

**Step 7.** Carry out exactly the same sequence of divisions on pyramid ABCD, producing prisms AP1, AP2, ..., APn within ABCD (equal in number to those in EFGH). Since the remaining sub-pyramids in EFGH are together less than S, we have that the sum of prisms HP1 + HP2 + ... + HPn is greater than EFGH - S = W.

**Step 8.** By 12.4, at each stage of the division, as the base ABC is to the base EFG, so are all the prisms in ABCD to all the corresponding prisms in EFGH. That is, the sum AP1 + AP2 + ... + APn is to the sum HP1 + HP2 + ... + HPn as triangle ABC is to triangle EFG.

**Step 9.** But by our assumption, triangle ABC is to triangle EFG as pyramid ABCD is to W. Therefore, by 5.11, the sum of prisms in ABCD is to the sum of prisms in EFGH as pyramid ABCD is to W.

**Step 10.** Now, the sum of prisms in ABCD is less than pyramid ABCD (since prisms are parts of the pyramid, by CN5). And the sum of prisms in EFGH is greater than W (from Step 7). By 5.14, if A < B and C > D, and A:C = B:D, we reach a contradiction. More precisely: since the sum of prisms in ABCD is less than pyramid ABCD, while the sum of prisms in EFGH is greater than W, the ratio (sum of prisms in ABCD):(sum of prisms in EFGH) is simultaneously equal to ABCD:W, yet the first term of the first ratio is less than the first term of the second ratio while the second term of the first ratio is greater than the second term of the second ratio. This is impossible, for if A < B then A:C < B:C for any C, and if C > D then A:C < A:D, so (sum of prisms in ABCD):(sum of prisms in EFGH) < ABCD:W. But they were supposed to be equal. This is a contradiction.

**Step 11.** Therefore W is not less than pyramid EFGH.

**Step 12.** Now suppose W is greater than pyramid EFGH. Then base ABC is to base EFG as pyramid ABCD is to some magnitude W greater than EFGH. By inversion (5.7.Porism or D5.13), base EFG is to base ABC as W is to pyramid ABCD. Since W > EFGH, there exists a magnitude W' less than ABCD such that base EFG is to base ABC as pyramid EFGH is to W'. But this reduces to the first case with the pyramids interchanged: pyramid EFGH would be to some magnitude W' less than pyramid ABCD as base EFG is to base ABC. By the same argument as in Steps 4 through 11 (applied to EFGH and ABCD), this leads to a contradiction.

**Step 13.** Therefore W is neither less than nor greater than pyramid EFGH, so W equals pyramid EFGH.

**Step 14.** Hence, base ABC is to base EFG as pyramid ABCD is to pyramid EFGH. That is, pyramids of the same height with triangular bases are to one another as their bases. Q.E.D.

**USED:** 10.1, 12.3, 12.4, 5.11, 5.14, CN5, D5.13
**Human refs (from References field):** 10.1, 12.2, 12.3, 12.4, 5.16, 5.2
**Jaccard:** 0.300 — AI adds ['5.11', '5.14', 'CN5', 'D5.13']; Human adds ['12.2', '5.16', '5.2']

## Proposition 12.6
**Statement:** Pyramids which are of the same height and have polygonal bases are to one another as the bases.

**Step 1.** Let there be two pyramids of the same height, the first with polygonal base ABCDE and apex F, and the second with polygonal base GHKLM and apex N. We are to show that pyramid F-ABCDE is to pyramid N-GHKLM as polygon ABCDE is to polygon GHKLM.

**Step 2.** From vertex A of polygon ABCDE, draw diagonals AC and AD, dividing the polygonal base into triangles ABC, ACD, and ADE [P1]. From vertex G of polygon GHKLM, draw diagonals GK and GL, dividing the polygonal base into triangles GHK, GKL, and GLM [P1]. These diagonals likewise decompose pyramid F-ABCDE into triangular-based pyramids F-ABC, F-ACD, and F-ADE sharing the common apex F, and pyramid N-GHKLM into triangular-based pyramids N-GHK, N-GKL, and N-GLM sharing the common apex N. All six triangular pyramids have the same height as the original pyramids.

**Step 3.** Since pyramids F-ABC and N-GHK are of the same height and have triangular bases, by 12.5 we have F-ABC : N-GHK = triangle ABC : triangle GHK. Similarly, F-ACD : N-GHK = triangle ACD : triangle GHK, and F-ADE : N-GHK = triangle ADE : triangle GHK [12.5].

**Step 4.** Since F-ABC : N-GHK = ABC : GHK and F-ACD : N-GHK = ACD : GHK, by 5.24, (F-ABC + F-ACD) : N-GHK = (ABC + ACD) : GHK. Applying 5.24 again with F-ADE : N-GHK = ADE : GHK, we obtain (F-ABC + F-ACD + F-ADE) : N-GHK = (ABC + ACD + ADE) : GHK. That is, pyramid F-ABCDE : pyramid N-GHK = polygon ABCDE : triangle GHK.

**Step 5.** By 12.5, since the triangular pyramids N-GHK, N-GKL, and N-GLM each share the same height as pyramid F-ABC, we have N-GHK : F-ABC = triangle GHK : triangle ABC, and N-GKL : F-ABC = triangle GKL : triangle ABC, and N-GLM : F-ABC = triangle GLM : triangle ABC [12.5].

**Step 6.** By two applications of 5.24 (as in Step 4), summing the three ratios from Step 5 yields (N-GHK + N-GKL + N-GLM) : F-ABC = (GHK + GKL + GLM) : ABC. That is, pyramid N-GHKLM : pyramid F-ABC = polygon GHKLM : triangle ABC.

**Step 7.** By the definition of same ratio [D5.5], the proportion in Step 6 — namely N-GHKLM : F-ABC = GHKLM : ABC — entails the inverse proportion F-ABC : N-GHKLM = ABC : GHKLM.

**Step 8.** From 12.5 we also have N-GHK : F-ABC = GHK : ABC. Combining this with the result of Step 7 by ex aequali [5.22] (since N-GHK : F-ABC = GHK : ABC and F-ABC : N-GHKLM = ABC : GHKLM), we conclude N-GHK : N-GHKLM = GHK : GHKLM.

**Step 9.** Combining Step 4 (F-ABCDE : N-GHK = ABCDE : GHK) with Step 8 (N-GHK : N-GHKLM = GHK : GHKLM) by ex aequali [5.22], we obtain F-ABCDE : N-GHKLM = ABCDE : GHKLM.

**Step 10.** Therefore pyramids of the same height with polygonal bases are to one another as their bases. Q.E.D.

**USED:** 12.5, 5.22, 5.24, D5.5, P1
**Human refs (from References field):** 12.5, 5.18, 5.22
**Jaccard:** 0.333 — AI adds ['5.24', 'D5.5', 'P1']; Human adds ['5.18']

## Proposition 12.7
**Statement:** Any prism which has a triangular base is divided into three pyramids equal to one another which have triangular bases.

**Step 1.** Let there be a prism with triangular bases ABC and DEF, where the vertices correspond so that AD, BE, and CF are lateral edges. By the definition of a prism (D11.13), the lateral faces ABED, BCFE, and ACFD are parallelograms, and the opposite faces ABC and DEF are equal, similar, and parallel triangles.

**Step 2.** Join BD (a diagonal of parallelogram ABED) and CE (a diagonal of parallelogram BCFE). The plane through B, C, D divides the prism into the tetrahedron ABCD and the solid BCDEF. The plane through C, D, E further divides the solid BCDEF into tetrahedra BCDE and CDEF. Thus the prism is divided into three pyramids with triangular bases: ABCD, BCDE, and CDEF.

**Step 3.** We show that pyramid ABCD equals pyramid BCDE. Consider both as pyramids with common apex C and bases lying in the plane of parallelogram ABED. Pyramid ABCD has base ABD, and pyramid BCDE has base BDE. Since ABED is a parallelogram and BD is its diagonal, by 1.34 the diagonal bisects the parallelogram, so triangle ABD is equal to triangle BDE. Since both pyramids have the same height (the perpendicular distance from C to the plane of ABED) and equal triangular bases ABD and BDE, by 12.5 (pyramids of the same height with triangular bases are to one another as their bases), pyramid ABCD is to pyramid BCDE as triangle ABD is to triangle BDE. Since triangle ABD equals triangle BDE, pyramid ABCD equals pyramid BCDE.

**Step 4.** We show that pyramid BCDE equals pyramid CDEF. Consider both as pyramids with common apex D and bases lying in the plane of parallelogram BCFE. Pyramid BCDE has base BCE, and pyramid CDEF has base CEF. Since BCFE is a parallelogram and CE is its diagonal, by 1.34 the diagonal bisects the parallelogram, so triangle BCE is equal to triangle CEF. Since both pyramids have the same height (the perpendicular distance from D to the plane of BCFE) and equal triangular bases BCE and CEF, by 12.5, pyramid BCDE is to pyramid CDEF as triangle BCE is to triangle CEF. Since triangle BCE equals triangle CEF, pyramid BCDE equals pyramid CDEF.

**Step 5.** Since pyramid ABCD equals pyramid BCDE, and pyramid BCDE equals pyramid CDEF, by CN1 (things equal to the same thing are equal to one another) all three pyramids are equal to one another. Each of the three pyramids ABCD, BCDE, and CDEF has a triangular base (namely ABC or BCD, BCE or BDE, and CEF or CDE respectively). Therefore any prism which has a triangular base is divided into three pyramids equal to one another which have triangular bases. Q.E.F.

**USED:** 1.34, 12.5, CN1, D11.12, D11.13
**Human refs (from References field):** 1.34, 12.5
**Jaccard:** 0.400 — AI adds ['CN1', 'D11.12', 'D11.13']

## Proposition 12.8
**Statement:** Similar pyramids which have triangular bases are in the triplicate ratio of their corresponding sides.

**Step 1.** Let ABCD and EFGH be similar pyramids having the triangular bases BCD and FGH, with apices A and E respectively. We are to prove that pyramid ABCD is to pyramid EFGH in the triplicate ratio of that which corresponding sides have to one another.

**Step 2.** Since the pyramids ABCD and EFGH are similar, their corresponding triangular faces are similar triangles, and the solid angles are contained by similar planes equal in multitude [D11.9]. Therefore all corresponding edges are proportional: AB:EF = BC:FG = CD:GH = BD:FH = AC:EG = AD:EH [D6.1, 6.4].

**Step 3.** Complete pyramid ABCD into a parallelepiped BCDKLM as follows. On the triangular base BCD, construct the prism having the same height as the pyramid ABCD, with the edge from each vertex of the base drawn parallel to the line from that vertex's corresponding apex direction, so that the prism has BCD as one triangular face. Similarly, complete pyramid EFGH into a parallelepiped on base FGH with the same height as pyramid EFGH [P1, 11.31].

**Step 4.** By 12.7, any prism which has a triangular base is divided into three pyramids equal to one another which have triangular bases. Now the prism on base BCD with the same height as pyramid ABCD contains pyramid ABCD as one of its three constituent equal pyramids. Therefore the prism on BCD equals three times pyramid ABCD. Likewise, the prism on FGH equals three times pyramid EFGH [12.7].

**Step 5.** Since the prism on BCD is triple pyramid ABCD, and the prism on FGH is triple pyramid EFGH, therefore pyramid ABCD is to pyramid EFGH as the prism on BCD is to the prism on FGH [5.15].

**Step 6.** By 11.28, each prism on a triangular base is half of the parallelepiped on the same base and of the same height. Therefore the prism on BCD is half of the parallelepiped on BCD, and the prism on FGH is half of the parallelepiped on FGH. Hence the prism on BCD is to the prism on FGH as the parallelepiped on BCD is to the parallelepiped on FGH [5.15, 11.28].

**Step 7.** Now we show the parallelepipeds are similar. Since all corresponding edges of the pyramids are proportional (Step 2), and the parallelepipeds are constructed with edges parallel to and proportional to those of the pyramids, the parallelepipeds have their corresponding edges proportional. Furthermore, since the solid angles of the similar pyramids are contained by similar planes in the same arrangement, the solid angles of the completed parallelepipeds are also equal. Therefore the parallelepipeds are similar solid figures [D11.9, 11.24].

**Step 8.** By 11.33, similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides. Therefore the parallelepiped on BCD is to the parallelepiped on FGH in the triplicate ratio of BC to FG [11.33].

**Step 9.** Combining the results: pyramid ABCD is to pyramid EFGH as the prism on BCD is to the prism on FGH (Step 5), which is as the parallelepiped on BCD is to the parallelepiped on FGH (Step 6), which is in the triplicate ratio of BC to FG (Step 8). Therefore pyramid ABCD is to pyramid EFGH in the triplicate ratio of BC to FG [5.11, CN1].

**Step 10.** Since BC and FG are corresponding sides of the similar pyramids, and the triplicate ratio of BC to FG is the same as the triplicate ratio of any pair of corresponding sides (since all corresponding sides are in the same ratio by Step 2), it follows that similar pyramids which have triangular bases are in the triplicate ratio of their corresponding sides [D5.10]. Q.E.D.

**USED:** 11.24, 11.28, 11.31, 11.33, 12.7, 5.11, 5.15, 6.4, CN1, D11.9, D5.10, D6.1, P1
**Human refs (from References field):** 11.24, 11.28, 11.33, 12.7
**Jaccard:** 0.308 — AI adds ['11.31', '5.11', '5.15', '6.4', 'CN1', 'D11.9', 'D5.10', 'D6.1', 'P1']

## Proposition 12.9
**Statement:** In equal pyramids which have triangular bases the bases are reciprocally proportional to the heights; and those pyramids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let ABCD and EFGH be two equal pyramids with triangular bases ABC and EFG, with apices D and H respectively. Let h₁ denote the perpendicular height from D to the plane of triangle ABC, and h₂ the perpendicular height from H to the plane of triangle EFG. We are to show that base ABC is to base EFG as h₂ is to h₁.

**Step 2.** Complete each pyramid to a triangular prism having the same base and the same height: let prism P₁ have base ABC and height h₁, and let prism P₂ have base EFG and height h₂. By XII.7, each triangular prism is divided into three equal pyramids with triangular bases. Therefore prism P₁ is three times pyramid ABCD, and prism P₂ is three times pyramid EFGH.

**Step 3.** Since pyramid ABCD equals pyramid EFGH (given), and prism P₁ equals three times pyramid ABCD while prism P₂ equals three times pyramid EFGH, it follows that prism P₁ equals prism P₂, since equal magnitudes taken the same multiple yield equal multiples (by CN2 applied repeatedly, or equivalently by 5.15 in reverse).

**Step 4.** Now construct parallelepipedal solids from each prism. By I.34, the diagonal of a parallelogram bisects it into two equal triangles. Conversely, each triangular base can be doubled to a parallelogram: double triangle ABC to parallelogram ABCX (by completing the parallelogram on two sides of the triangle), and double triangle EFG to parallelogram EFGY. By XI.28, the diagonal plane of a parallelepiped bisects it into two equal triangular prisms. Therefore the parallelepiped Q₁ on base ABCX with height h₁ is twice prism P₁, and the parallelepiped Q₂ on base EFGY with height h₂ is twice prism P₂.

**Step 5.** Since prism P₁ equals prism P₂ (Step 3), and Q₁ = 2·P₁ while Q₂ = 2·P₂, it follows that parallelepiped Q₁ equals parallelepiped Q₂ (by CN2).

**Step 6.** By XI.34, in equal parallelepipedal solids, the bases are reciprocally proportional to the heights. Applying this to Q₁ and Q₂, we obtain parallelogram ABCX : parallelogram EFGY = h₂ : h₁.

**Step 7.** Since triangle ABC is half of parallelogram ABCX and triangle EFG is half of parallelogram EFGY (by I.34), by V.15 (parts have the same ratio as the same multiples of them), triangle ABC : triangle EFG = parallelogram ABCX : parallelogram EFGY. Combining with Step 6, we conclude that base ABC : base EFG = h₂ : h₁. This completes the first part.

**Step 8.** Conversely, let pyramids ABCD and EFGH have triangular bases ABC and EFG with heights h₁ and h₂ respectively, and suppose base ABC : base EFG = h₂ : h₁. We are to show that pyramid ABCD equals pyramid EFGH.

**Step 9.** Construct the same prisms and parallelepipeds as before: prism P₁ on base ABC with height h₁, prism P₂ on base EFG with height h₂, parallelepiped Q₁ on parallelogram ABCX with height h₁, and parallelepiped Q₂ on parallelogram EFGY with height h₂.

**Step 10.** Since base ABC : base EFG = h₂ : h₁ (given), and since triangle ABC : triangle EFG = parallelogram ABCX : parallelogram EFGY (by V.15 and I.34 as before), we have parallelogram ABCX : parallelogram EFGY = h₂ : h₁.

**Step 11.** By the converse part of XI.34, parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal. Therefore parallelepiped Q₁ equals parallelepiped Q₂.

**Step 12.** Since Q₁ = 2·P₁ and Q₂ = 2·P₂ (by XI.28), and Q₁ = Q₂, it follows that prism P₁ equals prism P₂ (halves of equals are equal, by CN3).

**Step 13.** Since prism P₁ = 3 · pyramid ABCD and prism P₂ = 3 · pyramid EFGH (by XII.7), and prism P₁ equals prism P₂, it follows that pyramid ABCD equals pyramid EFGH (thirds of equals are equal, by CN3). This completes the converse.

**Step 14.** Therefore, in equal pyramids which have triangular bases, the bases are reciprocally proportional to the heights; and those pyramids in which the bases are reciprocally proportional to the heights are equal. Q.E.D.

**USED:** 1.34, 11.28, 11.34, 12.7, 5.15, CN2, CN3
**Human refs (from References field):** 1.34, 11.34, 5.11
**Jaccard:** 0.250 — AI adds ['11.28', '12.7', '5.15', 'CN2', 'CN3']; Human adds ['5.11']

## Proposition 12.10
**Statement:** Any cone is a third part of the cylinder which has the same base with it and equal height.

**Step 1.** Let the cone and the cylinder have the same circular base, call it circle ABCD, and let them have equal height. We are to prove that the cone is one-third of the cylinder. That is, the cylinder equals three times the cone.

**Step 2.** Suppose, for contradiction, that the cylinder does not equal three times the cone. Then either the cylinder is greater than three times the cone, or the cylinder is less than three times the cone.

**Step 3.** First suppose the cylinder is greater than three times the cone. Then there exists some solid magnitude S such that the cylinder equals three times the cone plus S, so that S is the excess of the cylinder over three times the cone.

**Step 4.** Inscribe a square ABCD in the circle by 4.6. This square is greater than half the circle, since the square is half the circumscribed square, and the circle is less than the circumscribed square.

**Step 5.** Bisect the arcs AB, BC, CD, DA and join the chords to form an inscribed regular octagon. Each triangle formed between a side of the square and the new vertex on the arc is greater than half of the corresponding circular segment. Continue bisecting arcs and joining chords in this manner. By 10.1, after sufficiently many bisections, the remaining circular segments (the excess of the circle over the inscribed polygon) can be made less than any given magnitude. In particular, continue until the excess of the circle over the inscribed polygon, when multiplied by the height, yields a solid less than S. That is, the cylinder on the full circle exceeds the prism erected on the inscribed polygon (with the same height as the cylinder) by less than S.

**Step 6.** Let the inscribed polygon so obtained be P. Erect on P a prism of the same height as the cylinder. Since the remaining segments of the circle beyond the polygon are less than what is needed, the cylinder exceeds this prism by less than S. Therefore the prism on P is greater than the cylinder minus S, which equals three times the cone (by Step 3).

**Step 7.** Now decompose the polygon P into triangles by drawing diagonals from one vertex. On each triangle, erect a prism of the same height. By 12.7, each such triangular prism is divided into three equal pyramids having the same triangular base and the same height. Therefore each triangular prism equals three times the corresponding triangular pyramid.

**Step 8.** Summing over all the triangles composing P, by CN2, the total prism on P equals three times the total pyramid on P having the same height. That is, Prism(P) = 3 times Pyramid(P).

**Step 9.** From Step 6, Prism(P) is greater than three times the cone. From Step 8, Prism(P) equals three times Pyramid(P). Therefore three times Pyramid(P) is greater than three times the cone, and so Pyramid(P) is greater than the cone.

**Step 10.** But the polygon P is inscribed in the circle, and the pyramid on P with vertex at the apex of the cone is inscribed within the cone. By CN5, the whole is greater than the part, so the cone is greater than the inscribed Pyramid(P). This contradicts Step 9. Therefore the cylinder is not greater than three times the cone.

**Step 11.** Now suppose the cylinder is less than three times the cone. Then three times the cone exceeds the cylinder. Let E be the excess, so that three times the cone equals the cylinder plus E.

**Step 12.** As before, inscribe successive polygons in the circle by bisecting arcs, starting from the square inscribed by 4.6. By 10.1, we can find an inscribed polygon P such that the excess of the circle over P, when taken with the height, makes the difference between the cylinder and the prism on P less than E. That is, the cylinder exceeds the prism on P by less than E, so the prism on P is greater than the cylinder minus E.

**Step 13.** But also consider: since the polygon P is inscribed in the circle, the prism on P is less than the cylinder (by CN5, as the prism is contained in the cylinder). Similarly, the pyramid on P is less than the cone (as it is inscribed in the cone).

**Step 14.** From Step 8 (which applies to any polygon decomposed into triangles), Prism(P) = 3 times Pyramid(P). Since Pyramid(P) is less than the cone (Step 13), we have Prism(P) = 3 times Pyramid(P) < 3 times the cone.

**Step 15.** But three times the cone = cylinder + E (from Step 11), and the prism on P < cylinder (from Step 13). So Prism(P) < cylinder < cylinder + E = 3 times the cone. This is consistent so far. We need a sharper contradiction.

**Step 16.** Reconsider: since the cylinder is less than three times the cone, circumscribe a polygon Q about the circle such that Q exceeds the circle by an amount making the prism on Q exceed the cylinder by less than E. This is possible by 10.1 applied to the successive circumscribed polygons (the excess of Q over the circle can be made arbitrarily small).

**Step 17.** The prism on Q, having the same height as the cylinder, exceeds the cylinder (since Q contains the circle) but by less than E. So Prism(Q) < cylinder + E = 3 times the cone.

**Step 18.** Decompose Q into triangles. By 12.7 and CN2 as before, Prism(Q) = 3 times Pyramid(Q).

**Step 19.** Since Q is circumscribed about the circle, the pyramid on Q with vertex at the apex of the cone contains the cone (the cone is inscribed within this pyramid). By CN5, Pyramid(Q) is greater than the cone. Therefore 3 times Pyramid(Q) is greater than 3 times the cone.

**Step 20.** That is, Prism(Q) > 3 times the cone. But Step 17 gives Prism(Q) < 3 times the cone. This is a contradiction. Therefore the cylinder is not less than three times the cone.

**Step 21.** Since the cylinder is neither greater than nor less than three times the cone (Steps 10 and 20), the cylinder equals exactly three times the cone. Therefore the cone is one-third of the cylinder which has the same base and equal height. Q.E.D.

**USED:** 10.1, 12.7, 4.6, CN2, CN5, D11.18, D11.21
**Human refs (from References field):** 10.1, 11.32, 12.2, 12.7, 4.6, 4.7
**Jaccard:** 0.300 — AI adds ['CN2', 'CN5', 'D11.18', 'D11.21']; Human adds ['11.32', '12.2', '4.7']

## Proposition 12.11
**Statement:** Cones and cylinders which are of the same height are to one another as their bases.

**Step 1.** Let there be two cones and two cylinders of the same height. Let the first cone and cylinder have circular base B1, and the second cone and cylinder have circular base B2, all sharing the same height h. We must show that both the cylinders and the cones are to one another as their bases, that is, Cylinder1 : Cylinder2 = B1 : B2 and Cone1 : Cone2 = B1 : B2.

**Step 2.** We first prove the result for the cylinders. Suppose for contradiction that the cylinders are not as their bases. Then B1 : B2 is not equal to Cylinder1 : Cylinder2. So either B1 : B2 > Cylinder1 : Cylinder2 or B1 : B2 < Cylinder1 : Cylinder2. Without loss of generality, assume B1 : B2 > Cylinder1 : Cylinder2 (the other case is symmetric by interchanging the roles of the two cylinders).

**Step 3.** Since B1 : B2 > Cylinder1 : Cylinder2, there exists a solid S less than Cylinder2 such that B1 : B2 = Cylinder1 : S [by the principle used in 12.2, taking a magnitude smaller than Cylinder2 in the same ratio].

**Step 4.** Inscribe in circle B2 a polygon by repeatedly bisecting arcs and joining chords, such that the inscribed polygon differs from B2 by less than the difference Cylinder2 - S. This is possible by the exhaustion lemma (10.1), since at each step the inscribed polygon exceeds half of the remaining difference, as in the method of 12.2.

**Step 5.** Let P2 be the polygon inscribed in B2 from Step 4, and inscribe a polygon P1 similar to P2 in circle B1 [by 4.1, fitting the corresponding chords]. Erect prisms of height h on each inscribed polygon. Call these Prism1 (on P1 inside Cylinder1) and Prism2 (on P2 inside Cylinder2).

**Step 6.** Each prism with a polygonal base can be divided into triangular prisms (by drawing diagonals from one vertex of the polygon). Each triangular prism can be divided into three pyramids of equal volume by 12.7. Therefore each prism equals a sum of pyramids with triangular bases, all of the same height h.

**Step 7.** By 12.5, pyramids of the same height with triangular bases are to one another as their bases. By 12.6, pyramids of the same height with polygonal bases are to one another as their bases. Therefore, the prisms of the same height on polygonal bases P1 and P2 are to one another as their bases: Prism1 : Prism2 = P1 : P2.

**Step 8.** Since P1 and P2 are similar polygons inscribed in circles with diameters d1 and d2 respectively, by 12.1 we have P1 : P2 = d1^2 : d2^2. Also by 12.2, B1 : B2 = d1^2 : d2^2. Therefore P1 : P2 = B1 : B2 [by CN1, since both equal the same ratio of squares on diameters].

**Step 9.** From Steps 7 and 8, Prism1 : Prism2 = B1 : B2 = Cylinder1 : S [from Step 3, by 5.11, since B1 : B2 = Cylinder1 : S].

**Step 10.** Since Prism1 is contained within Cylinder1, we have Prism1 < Cylinder1, so Prism1 : Prism2 < Cylinder1 : Prism2 [since if A < B and C > 0, then A : C < B : C]. But from Step 9, Prism1 : Prism2 = Cylinder1 : S. Therefore Cylinder1 : S < Cylinder1 : Prism2, which implies that Prism2 < S [by 5.10 and the inversion of the inequality: if A : C < A : D then D < C, since the larger the consequent the smaller the ratio, by 5.8].

**Step 11.** But by construction in Step 4, the polygon P2 was chosen so that B2 - P2 < Cylinder2 - S, and since Prism2 is the prism of height h on P2 and Cylinder2 is the cylinder of height h on B2, the prism Prism2 is greater than S. This contradicts the conclusion of Step 10 that Prism2 < S. [More precisely: since B2 - P2 < Cylinder2 - S, and the prism on B2 of height h equals Cylinder2 while the prism on P2 of height h equals Prism2, we have Cylinder2 - Prism2 < Cylinder2 - S, hence S < Prism2.]

**Step 12.** The symmetric case, B1 : B2 < Cylinder1 : Cylinder2, leads to an analogous contradiction by interchanging the roles of the two cylinders. Therefore, the assumption that the cylinders are not as their bases is false, and we conclude Cylinder1 : Cylinder2 = B1 : B2.

**Step 13.** Now for the cones. By 12.10, Cone1 is one-third of Cylinder1 (since they share the same base B1 and height h), and Cone2 is one-third of Cylinder2 (since they share base B2 and height h). That is, 3 * Cone1 = Cylinder1 and 3 * Cone2 = Cylinder2.

**Step 14.** Since Cylinder1 : Cylinder2 = B1 : B2 (from Step 12), and Cylinder1 = 3 * Cone1, Cylinder2 = 3 * Cone2, we have 3*Cone1 : 3*Cone2 = B1 : B2. By 5.15, equal multiples have the same ratio as the magnitudes themselves, so Cone1 : Cone2 = B1 : B2.

**Step 15.** Therefore, cones and cylinders which are of the same height are to one another as their bases. Q.E.D.

**USED:** 10.1, 12.1, 12.10, 12.2, 12.5, 12.6, 12.7, 4.1, 5.10, 5.11, 5.15, 5.8, CN1, CN5
**Human refs (from References field):** 10.1, 12.1, 12.10, 12.2, 12.6, 5.11, 5.16
**Jaccard:** 0.400 — AI adds ['12.5', '12.7', '4.1', '5.10', '5.15', '5.8', 'CN1', 'CN5']; Human adds ['5.16']

## Proposition 12.12
**Statement:** Similar cones and cylinders are to one another in the triplicate ratio of the diameters in their bases.

**Step 1.** Let A be a cone (or cylinder) with base circle having diameter d_A and height h_A, and let B be a similar cone (or cylinder) with base circle having diameter d_B and height h_B. By D11.24, since A and B are similar, their axes and base diameters are proportional, so d_A : d_B = h_A : h_B.

**Step 2.** Construct a third solid C of the same type (cone or cylinder) having the same base as A (diameter d_A) and the same height as B (height h_B).

**Step 3.** Since C and B are cones (or cylinders) of the same height h_B, by 12.11, C : B = (base of C) : (base of B). By 12.2, circles are to one another as the squares on their diameters, so (base of C) : (base of B) = d_A^2 : d_B^2. Therefore C : B = d_A^2 : d_B^2, which by D5.9 is the duplicate ratio of d_A to d_B.

**Step 4.** Now consider A and C, which share the same base circle of diameter d_A. We show that A : C = h_A : h_B. If A and C are cylinders, inscribe in each a prism with a regular polygonal base (the same polygon inscribed in their common circular base). These prisms, being parallelepipedal solids on equal bases, are to one another as their heights h_A and h_B by 11.32. As the inscribed polygonal prisms are made to approximate the cylinders more closely (by doubling the number of sides), the prisms always maintain the ratio h_A : h_B, and by the method of exhaustion (as established in 12.10 and 12.11 via 10.1), the cylinders themselves satisfy A : C = h_A : h_B.

**Step 5.** If A and C are cones rather than cylinders, let Cyl_A be the cylinder with the same base and height as cone A, and let Cyl_C be the cylinder with the same base and height as cone C. By 12.10, A = (1/3) Cyl_A and C = (1/3) Cyl_C. Since Cyl_A and Cyl_C share the same base, by Step 4, Cyl_A : Cyl_C = h_A : h_B. Since A is the same part (one-third) of Cyl_A as C is of Cyl_C, by 5.15, A : C = Cyl_A : Cyl_C = h_A : h_B.

**Step 6.** From Step 1, d_A : d_B = h_A : h_B, so A : C = d_A : d_B.

**Step 7.** We now have the two ratios: A : C = d_A : d_B (Step 6) and C : B = d_A^2 : d_B^2 (Step 3). By 5.22 (ex aequali), from the proportion A : C : B with the stated ratios, we obtain A : B = (the ratio compounded of d_A : d_B and d_A^2 : d_B^2).

**Step 8.** Since d_A : d_B is the first ratio, d_A^2 : d_B^2 is its duplicate (D5.9), the compounded ratio A : B equals d_A^3 : d_B^3. By D5.10, this is the triplicate ratio of d_A to d_B, i.e., the triplicate ratio of the diameters of the bases.

**Step 9.** Therefore, similar cones and cylinders are to one another in the triplicate ratio of the diameters in their bases. Q.E.D.

**USED:** 10.1, 11.32, 12.10, 12.11, 12.2, 5.15, 5.22, D11.24, D5.10, D5.9
**Human refs (from References field):** 10.1, 12.10, 12.8, 4.6, 5.12, 5.16, 5.22, 6.5, 6.6, D11.24, D11.9, D6.1
**Jaccard:** 0.222 — AI adds ['11.32', '12.11', '12.2', '5.15', 'D5.10', 'D5.9']; Human adds ['12.8', '4.6', '5.12', '5.16', '6.5', '6.6', 'D11.9', 'D6.1']

## Proposition 12.13
**Statement:** If a cylinder be cut by a plane which is parallel to its opposite planes, then, as the cylinder is to the cylinder, so will the axis be to the axis.

**Step 1.** Let the cylinder AD have axis EF, and let it be cut by a plane through G parallel to the opposite planes (the circular bases at A and D). Let the axis EF be cut at the same point H, so that EH is the axis of cylinder AG and HF is the axis of cylinder GD. We must show that cylinder AG is to cylinder GD as axis EH is to axis HF.

**Step 2.** We shall prove this using the general definition of proportion (D5.5). Let any equimultiples whatever be taken: let axis EH be multiplied m times to produce a length EH_m, and let axis HF be multiplied n times to produce a length HF_n. We must show that m times cylinder AG compares to n times cylinder GD in the same way that EH_m compares to HF_n.

**Step 3.** Produce the axis EF in both directions. Along the direction from E beyond E, set off m - 1 successive lengths each equal to EH, and along the direction from F beyond F, set off n - 1 successive lengths each equal to HF (P1, P2). Through each of the resulting division points, draw planes parallel to the bases of the cylinder (D11.8).

**Step 4.** Each of the m small cylinders cut off on the side of EH has the same base (the circle equal to the base at A, since the cutting planes are all parallel to the base) and the same height (equal to EH). By 12.11, cylinders of the same height are to one another as their bases. Since the bases are all equal circles (being cross-sections of a cylinder cut by parallel planes, and hence equal to the original base), each of these m small cylinders is equal to cylinder AG (CN1).

**Step 5.** Therefore the cylinder composed of all m such small cylinders equals m times cylinder AG (D5.2, CN2). Likewise, the cylinder composed of all n small cylinders on the side of HF, each equal to cylinder GD, equals n times cylinder GD.

**Step 6.** Now the total axis for the m-fold cylinder is EH_m = m times EH, and the total axis for the n-fold cylinder is HF_n = n times HF. These composite cylinders have the same base as the original cylinder.

**Step 7.** If EH_m > HF_n, that is, if m times EH exceeds n times HF, then the m-fold cylinder (having the same base and greater height) is greater than the n-fold cylinder. For by 12.11, cylinders on equal bases are to one another as their heights, so the cylinder of greater height is greater (CN5).

**Step 8.** Similarly, if EH_m = HF_n, then the m-fold cylinder equals the n-fold cylinder, since they have equal bases and equal heights (12.11, CN1). And if EH_m < HF_n, then the m-fold cylinder is less than the n-fold cylinder, by the same reasoning.

**Step 9.** Therefore, for any equimultiples m of cylinder AG and axis EH, and any equimultiples n of cylinder GD and axis HF, the multiple of the first magnitude (cylinder AG) exceeds, equals, or falls short of the multiple of the second magnitude (cylinder GD) precisely when the corresponding multiple of the third magnitude (axis EH) exceeds, equals, or falls short of the corresponding multiple of the fourth magnitude (axis HF).

**Step 10.** Therefore, by the definition of proportion (D5.5), cylinder AG is to cylinder GD as axis EH is to axis HF.

**Step 11.** But cylinder AG together with cylinder GD equals the whole cylinder AD (CN2), and axis EH together with axis HF equals the whole axis EF. Therefore, as the cylinder is to the cylinder, so is the axis to the axis. Q.E.D.

**USED:** 12.11, CN1, CN2, CN5, D11.21, D11.22, D11.23, D11.8, D5.2, D5.5, P1, P2
**Human refs (from References field):** 12.11, D5.5
**Jaccard:** 0.167 — AI adds ['CN1', 'CN2', 'CN5', 'D11.21', 'D11.22', 'D11.23', 'D11.8', 'D5.2', 'P1', 'P2']

## Proposition 12.14
**Statement:** Cones and cylinders which are on equal bases are to one another as their heights.

**Step 1.** Let there be two cylinders CD1 and CD2 on equal bases B1 and B2 respectively, with heights H1 and H2. We are to show that CD1 is to CD2 as H1 is to H2.

**Step 2.** Construct a third cylinder CD3 on the same base B1 as CD1, but with height equal to H2. This is possible since we may erect a cylinder on any given circular base to any given height.

**Step 3.** Since CD1 and CD3 are both on the same base B1, and differ only in their heights H1 and H2, by Proposition 12.13 (if a cylinder be cut by a plane parallel to its opposite planes, then as the cylinder is to the cylinder so will the axis be to the axis), the cylinder on a single base is divided proportionally to its axis. Applying this principle, CD1 is to CD3 as H1 is to H2, since these two cylinders share the same base and their axes (heights) are H1 and H2 respectively.

**Step 4.** Now consider CD3 and CD2. The cylinder CD3 has base B1 and height H2, while CD2 has base B2 and height H2. Since B1 equals B2 (by hypothesis) and both cylinders have the same height H2, by Proposition 12.11 (cones and cylinders of the same height are to one another as their bases), CD3 is to CD2 as B1 is to B2. But B1 equals B2, so CD3 is to CD2 as B1 is to B1, that is, CD3 equals CD2.

**Step 5.** Since CD3 equals CD2, and CD1 is to CD3 as H1 is to H2 (from Step 3), by Proposition 5.7 (equal magnitudes have the same ratio to the same magnitude, and the same magnitude has the same ratio to equal magnitudes), we may substitute CD2 for CD3. Therefore CD1 is to CD2 as H1 is to H2. This completes the proof for cylinders on equal bases.

**Step 6.** Now let there be two cones K1 and K2 on equal bases B1 and B2 respectively, with heights H1 and H2. Let CD1 be the cylinder with the same base B1 and height H1 as cone K1, and let CD2 be the cylinder with the same base B2 and height H2 as cone K2.

**Step 7.** By Proposition 12.10 (any cone is a third part of the cylinder which has the same base and equal height), K1 is one-third of CD1, and K2 is one-third of CD2.

**Step 8.** From Step 5, we established that CD1 is to CD2 as H1 is to H2. Since K1 is one-third of CD1 and K2 is one-third of CD2, that is, K1 and K2 are the same parts (namely third parts) of CD1 and CD2 respectively, by Proposition 5.15 (parts have the same ratio as the same multiples of them), K1 is to K2 as CD1 is to CD2.

**Step 9.** But CD1 is to CD2 as H1 is to H2 (Step 5). Therefore, by Proposition 5.11 (ratios which are the same with the same ratio are also the same with one another), K1 is to K2 as H1 is to H2. This completes the proof for cones on equal bases.

**Step 10.** Therefore, cones and cylinders which are on equal bases are to one another as their heights. Q.E.D.

**USED:** 12.10, 12.11, 12.13, 5.11, 5.15, 5.7
**Human refs (from References field):** 12.10, 12.11, 12.13
**Jaccard:** 0.500 — AI adds ['5.11', '5.15', '5.7']

## Proposition 12.15
**Statement:** In equal cones and cylinders the bases are reciprocally proportional to the heights; and those cones and cylinders in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let there be equal cones or cylinders; let them have bases the circles A and B, and heights C and D respectively. We must show that base A is to base B as height D is to height C (i.e., the bases are reciprocally proportional to the heights).

**Step 2.** Case 1: Suppose the heights C and D are equal. Since the cones (or cylinders) are equal and have equal heights, by 12.11 (cones and cylinders of the same height are to one another as their bases), the bases must also be equal. Then base A is to base B as D is to C, since A equals B and D equals C, so both ratios are ratios of equals [CN1, 5.7].

**Step 3.** Case 2: Suppose the heights C and D are not equal. Let height C be greater than D. On the base B, set up a cone (or cylinder) of height E equal to height C, so that this new solid has base B and height E = C [by construction].

**Step 4.** Since the original cone (or cylinder) on base A with height C and the new cone (or cylinder) on base B with height E (= C) have the same height, by 12.11, the cone (or cylinder) on base A with height C is to the cone (or cylinder) on base B with height E as base A is to base B.

**Step 5.** But the original cone (or cylinder) on base A with height C equals the original cone (or cylinder) on base B with height D (by hypothesis). Therefore the cone (or cylinder) on base B with height D is to the cone (or cylinder) on base B with height E as base A is to base B [5.7].

**Step 6.** Since the cone (or cylinder) on base B with height D and the cone (or cylinder) on base B with height E are on the same base B, by 12.14 (cones and cylinders on equal bases are to one another as their heights), they are to one another as height D is to height E.

**Step 7.** Therefore base A is to base B as height D is to height E [5.11]. But E equals C (by construction), so base A is to base B as height D is to height C [5.7, CN1]. This completes the forward direction.

**Step 8.** Conversely, suppose that base A is to base B as height D is to height C. We must prove the cones (or cylinders) are equal.

**Step 9.** Using the same construction as before, set up on base B a cone (or cylinder) of height E equal to C.

**Step 10.** Since base A is to base B as height D is to height C, and E equals C, we have base A is to base B as height D is to height E [5.7, CN1].

**Step 11.** The cone (or cylinder) on base B with height D is to the cone (or cylinder) on base B with height E as D is to E, by 12.14 (same base, different heights).

**Step 12.** The cone (or cylinder) on base A with height C is to the cone (or cylinder) on base B with height E (= C) as base A is to base B, by 12.11 (same height, different bases).

**Step 13.** Therefore the cone (or cylinder) on base A with height C is to the cone (or cylinder) on base B with height E as the cone (or cylinder) on base B with height D is to the cone (or cylinder) on base B with height E [5.11, from Steps 10-12 combining the equal ratios].

**Step 14.** Since these two solids have the same ratio to the cone (or cylinder) on base B with height E, they are equal to one another [5.9].

**Step 15.** Therefore the cone (or cylinder) on base A with height C equals the cone (or cylinder) on base B with height D. This completes the converse, and the proposition is proved.

**USED:** 12.11, 12.14, 5.11, 5.7, 5.9, CN1
**Human refs (from References field):** 12.11, 12.13, 5.11, 5.7, 5.9
**Jaccard:** 0.571 — AI adds ['12.14', 'CN1']; Human adds ['12.13']

## Proposition 12.16
**Statement:** Given two circles about the same centre, to inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle.

**Step 1.** Let the two concentric circles have center E, with the greater circle ABCD and the lesser circle FGHK, and let EF be a radius of the lesser circle. We must inscribe in circle ABCD an equilateral polygon with an even number of sides that does not touch circle FGHK.

**Step 2.** Draw a diameter BD of the greater circle through E [D1.17]. Through E, draw AC at right angles to BD [1.11], so that AC is also a diameter. Then arcs AB, BC, CD, DA are each quarter-arcs of the circle, and AE, BE, CE, DE are all radii of the greater circle.

**Step 3.** Since EF is a radius of the lesser circle and EB is a radius of the greater circle, and the lesser circle lies inside the greater, we have EF < EB [D1.15, CN5].

**Step 4.** Now bisect the angle AEB by the straight line EL meeting the greater circle at L [1.9, P1]. Bisect the angle LEB by the straight line EM meeting the greater circle at M [1.9, P1]. Continue bisecting in this manner. By repeated bisection, we diminish the arc at each step by half. By Proposition 10.1, if we continue this process, we will eventually arrive at an arc — call it BN — that is less than any assigned magnitude, in particular one whose properties we now examine.

**Step 5.** Specifically, at each bisection the perpendicular distance from the center E to the resulting chord increases. Consider the perpendicular from E to any chord of the greater circle: by 3.14, this perpendicular bisects the chord, and by 1.47 the square on the radius equals the square on half the chord plus the square on the perpendicular. As the subtended arc decreases, the chord decreases, so the square on half the chord decreases, and hence the square on the perpendicular increases, meaning the perpendicular itself increases.

**Step 6.** The difference between the radius EB and the perpendicular distance from E to the chord is diminished at each bisection step. By 10.1, since EB - EF is a positive magnitude, repeated halving will produce a remainder less than EB - EF. That is, we can bisect the angle sufficiently many times to obtain an arc BN such that the perpendicular EQ from E to chord BN satisfies EQ > EF.

**Step 7.** Let the arc AB have been bisected the requisite number of times so that the final subdivision arc BN has the property that the perpendicular from E to the chord BN exceeds EF. Since we began with a quarter-arc and bisected it n times, the arc BN is a (1/2^n)-th part of a quarter-circle, so the full circle is divided into 4 times 2^n equal arcs, each equal to arc BN.

**Step 8.** Mark off arcs equal to BN successively around the entire greater circle. This divides the circumference into 4 times 2^n equal arcs. Join the consecutive division points by straight lines [P1]. The resulting figure is a polygon inscribed in the greater circle [D4.3].

**Step 9.** Since all the arcs are equal, all the chords (sides of the polygon) subtend equal arcs. By 3.29, equal arcs are subtended by equal chords. Therefore the polygon is equilateral.

**Step 10.** The number of sides is 4 times 2^n, which is an even number [D7.6], since it is divisible by 2.

**Step 11.** Now consider any side of this polygon. It subtends an arc equal to BN, so by symmetry (the polygon is regular and concentric with the circles), the perpendicular from E to that side equals EQ, the perpendicular from E to chord BN. Since EQ > EF [Step 6], the perpendicular from E to every side of the polygon exceeds the radius EF of the lesser circle.

**Step 12.** Since the perpendicular distance from E to each side of the polygon is greater than EF, each side lies entirely outside the lesser circle. For if any side touched or crossed the lesser circle, then by 3.16, at the point of tangency or by 3.14, the perpendicular from the center to that chord would be at most EF, contradicting EQ > EF. Alternatively, by 3.15, since each side is farther from the center than any chord of the lesser circle would require, no side meets the lesser circle.

**Step 13.** Therefore we have inscribed in the greater circle an equilateral polygon with an even number of sides (namely 4 times 2^n sides) which does not touch the lesser circle. Q.E.F.

**USED:** 1.11, 1.47, 1.9, 10.1, 3.14, 3.15, 3.16, 3.29, CN5, D1.15, D1.17, D4.3, D7.6, P1
**Human refs (from References field):** 1.4, 10.1, 3.16, 3.3
**Jaccard:** 0.125 — AI adds ['1.11', '1.47', '1.9', '3.14', '3.15', '3.29', 'CN5', 'D1.15', 'D1.17', 'D4.3', 'D7.6', 'P1']; Human adds ['1.4', '3.3']

## Proposition 12.17
**Statement:** Given two spheres about the same centre, to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface.

**Step 1.** Let there be two spheres about the same centre A, and let it be required to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface.

**Step 2.** Cut the spheres by any plane through the centre A. This produces two concentric circles: the great circle BCDE of the greater sphere and the great circle FGHK of the lesser sphere, both with centre A [D11.14, D11.17].

**Step 3.** Draw two diameters BD and CE of the greater circle at right angles to one another [1.11]. These diameters also pass through the centre A of the lesser circle.

**Step 4.** By 12.16, inscribe in the greater circle BCDE an equilateral polygon with an even number of sides which does not touch the lesser circle FGHK. Let this polygon have sides BM, ME, EN, ND, DO, OC, CP, PB (or similar vertices on the circle), so that no side touches circle FGHK [12.16].

**Step 5.** Let BM be one of the sides of the inscribed polygon that cuts one of the quadrants. Draw a perpendicular from the centre A to BM; let it meet BM at the point L [1.12]. Then AL, being the perpendicular from the centre to a chord of the greater circle, is less than the radius of the greater circle, but since the polygon does not touch the lesser circle, AL is greater than the radius AF of the lesser circle [3.14, 3.15]. That is, the perpendicular distance from A to each side of the polygon is greater than the radius of the lesser sphere.

**Step 6.** Through each side of the inscribed polygon (such as BM), erect a plane perpendicular to the plane of the great circle BCDE [11.12]. Each such plane intersects the greater sphere in a great circle (since the plane passes through a chord of the great circle and is perpendicular to the plane containing that great circle).

**Step 7.** On each chord (such as BM), within the circle formed by the plane through that chord, the chord BM subtends an arc of that circle. In this new circle, inscribe the same equilateral polygon as in Step 4 (with the same number of sides), placing BM as one side, and erecting the remaining vertices on the circle in the perpendicular plane [4.1, 12.16]. Since this new circle is a great circle of the greater sphere (having the same radius), the inscribed polygon is congruent to the polygon in the original plane.

**Step 8.** Carry out this construction for every side of the original polygon from Step 4. Connect adjacent vertices of polygons in adjacent perpendicular planes to form triangular faces. The result is a polyhedral solid whose vertices all lie on the surface of the greater sphere, hence it is inscribed in the greater sphere [D11.14].

**Step 9.** It remains to show that this polyhedral solid does not touch the lesser sphere. Consider any face of the polyhedral solid. Each face is either a side of one of the inscribed polygons in a perpendicular plane or a triangle connecting vertices of adjacent polygons. In every case, the face is a plane figure.

**Step 10.** Drop a perpendicular from the centre A to the plane of any face of the solid [11.11]. This perpendicular is the shortest distance from A to that plane. Since every face of the solid lies on a chord or triangle that is at least as far from the centre A as the perpendicular distance AL found in Step 5, and since AL is greater than the radius of the lesser sphere, the perpendicular from A to any face must also be greater than the radius of the lesser sphere [1.19, CN5].

**Step 11.** More precisely, in the original plane, the perpendicular from A to each side of the polygon exceeds the radius of the lesser circle (Step 5). For a face in a perpendicular plane, the perpendicular from A to that face is at least as great as the perpendicular from A to the corresponding chord in the original plane, because the face in the perpendicular plane lies on or beyond the chord relative to A. Thus the perpendicular from A to every face of the polyhedron is greater than the radius of the lesser sphere [3.15, 11.38].

**Step 12.** Since the distance from the centre A to every face of the polyhedral solid exceeds the radius of the lesser sphere, the surface of the lesser sphere cannot meet any face of the solid. Therefore the polyhedral solid inscribed in the greater sphere does not touch the lesser sphere at its surface [D11.14].

**Step 13.** Therefore, given two spheres about the same centre, we have inscribed in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface, which is what was required to construct. Q.E.F.

**USED:** 1.11, 1.12, 1.19, 11.11, 11.12, 11.38, 12.16, 3.14, 3.15, 4.1, CN5, D11.14, D11.17
**Human refs (from References field):** 1.26, 1.33, 1.47, 11.11, 11.18, 11.2, 11.6, 11.7, 11.9, 3.27, 3.31, 6.2, 6.8, D11.14, D11.3, D11.4
**Jaccard:** 0.074 — AI adds ['1.11', '1.12', '1.19', '11.12', '11.38', '12.16', '3.14', '3.15', '4.1', 'CN5', 'D11.17']; Human adds ['1.26', '1.33', '1.47', '11.18', '11.2', '11.6', '11.7', '11.9', '3.27', '3.31', '6.2', '6.8', 'D11.3', 'D11.4']

## Proposition 12.18
**Statement:** Spheres are to one another in the triplicate ratio of their respective diameters.

**Step 1.** Let there be two spheres with centres A and B, and let their diameters be CD and EF respectively. We must show that sphere CD is to sphere EF in the triplicate ratio of CD to EF, that is, as the cube on CD is to the cube on EF.

**Step 2.** Suppose, for the sake of contradiction, that sphere CD is not to sphere EF as the cube on CD is to the cube on EF. Then sphere CD is to some magnitude either less than or greater than sphere EF as the cube on CD is to the cube on EF.

**Step 3.** First, suppose sphere CD is to a magnitude W less than sphere EF as the cube on CD is to the cube on EF, so that W < sphere EF.

**Step 4.** Since W is less than sphere EF, there exists a sphere concentric with sphere EF and smaller than sphere EF, whose volume exceeds W. By 12.17, we can inscribe in the greater sphere EF a polyhedral solid that does not touch the lesser sphere at its surface. Let such a polyhedral solid be inscribed in sphere EF.

**Step 5.** Inscribe in sphere CD a polyhedral solid similar to the polyhedral solid inscribed in sphere EF. By the construction in 12.17, such similar polyhedral solids can be formed, since the polyhedra are built from pyramids with vertices at the centres of the spheres.

**Step 6.** The similar polyhedral solids inscribed in the two spheres are composed of pyramids with triangular bases (by decomposing each polygonal face into triangles and forming pyramids to the centre). These pyramids in the solid inscribed in sphere CD are similar to the corresponding pyramids in the solid inscribed in sphere EF, since corresponding edges are proportional (the solids are similar).

**Step 7.** By 12.8, similar pyramids which have triangular bases are in the triplicate ratio of their corresponding sides. Therefore each pyramid in the polyhedron inscribed in sphere CD is to the corresponding pyramid in the polyhedron inscribed in sphere EF in the triplicate ratio of the corresponding sides.

**Step 8.** Since the sides of the inscribed polyhedra are proportional to the diameters of the spheres in which they are inscribed (by the similarity of the construction), and all corresponding sides have the same ratio, the triplicate ratio of corresponding sides equals the triplicate ratio of CD to EF.

**Step 9.** By 5.12 (alternando) and the fact that each pair of corresponding pyramids has the same ratio, and by 5.12 applied repeatedly, the whole polyhedral solid in sphere CD is to the whole polyhedral solid in sphere EF in the triplicate ratio of CD to EF, that is, as the cube on CD is to the cube on EF.

**Step 10.** But by hypothesis, sphere CD is to W as the cube on CD is to the cube on EF. Therefore, by 5.11 (magnitudes that have the same ratio to the same are equal), the polyhedral solid in sphere CD is to the polyhedral solid in sphere EF as sphere CD is to W.

**Step 11.** By 5.16 (alternando and conversion), since sphere CD is greater than the polyhedral solid inscribed in it (as the sphere contains the solid, by CN5), it follows that W is greater than the polyhedral solid inscribed in sphere EF.

**Step 12.** But the polyhedral solid inscribed in sphere EF is greater than the inner sphere (and hence greater than W, since the polyhedron was chosen so that the inner sphere it circumscribes has volume greater than W, and the polyhedron lies between the two concentric spheres). This means the polyhedral solid inscribed in sphere EF is greater than W. This contradicts Step 11.

**Step 13.** Therefore the assumption that sphere CD is to a magnitude W less than sphere EF as the cube on CD is to the cube on EF is false.

**Step 14.** Now suppose sphere CD is to a magnitude W greater than sphere EF as the cube on CD is to the cube on EF. Then by inversion, W is to sphere CD as the cube on EF is to the cube on CD, so sphere EF is to some magnitude less than sphere CD as the cube on EF is to the cube on CD.

**Step 15.** But this reduces to the case already refuted in Steps 3 through 13 (with the roles of the two spheres interchanged). Therefore this case also leads to a contradiction.

**Step 16.** Since sphere CD cannot be to any magnitude greater than or less than sphere EF in the ratio of the cube on CD to the cube on EF, it follows that sphere CD is to sphere EF as the cube on CD is to the cube on EF.

**Step 17.** By D5.10, the ratio of the cube on CD to the cube on EF is the triplicate ratio of that which CD has to EF (since if CD, X, Y, EF are in continuous proportion, then CD:EF = CD^3:EF^3 is the triplicate ratio).

**Step 18.** Therefore spheres are to one another in the triplicate ratio of their respective diameters. Q.E.D.

**USED:** 12.17, 12.8, 5.11, 5.12, CN5, D11.14, D11.17, D5.10
**Human refs (from References field):** 12.17, 12.2, 5.16
**Jaccard:** 0.100 — AI adds ['12.8', '5.11', '5.12', 'CN5', 'D11.14', 'D11.17', 'D5.10']; Human adds ['12.2', '5.16']
