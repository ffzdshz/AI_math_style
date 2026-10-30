# Book 6 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 6.1
**Statement:** Triangles and parallelograms which are under the same height are to one another as their bases.

**Step 1.** Let triangle ABC have base BC, and let triangle ACD have base CD, and let both triangles be under the same height, that is, let the perpendicular drawn from A to the line BD be the same for both triangles. Similarly, let parallelogram EC be on base BC and parallelogram CF be on base CD, both under the same height as the triangles. We are to prove that triangle ABC is to triangle ACD as BC is to CD, and that parallelogram EC is to parallelogram CF as BC is to CD.

**Step 2.** Produce BD in both directions. Along the direction from C through B, mark off any number of segments equal to BC: let BG = BC, and GH = BC. Along the direction from C through D, mark off any number of segments equal to CD: let DK = CD, and KL = CD. Join AG, AH, AK, and AL. [P1, P2]

**Step 3.** Since HC = HG + GB + BC and HG = GB = BC, we have HC = 3 times BC. Similarly, since GC = GB + BC and GB = BC, we have GC = 2 times BC. In general, by producing as many equal segments as we wish, the base HC is any desired multiple of BC. Likewise, CL = CD + DK + KL = 3 times CD, and CK = CD + DK = 2 times CD, so CL is any desired multiple of CD.

**Step 4.** Now, since GB = BC, triangles AGB and ABC are on equal bases GB and BC and are between the same parallels (since A is at the same height above both), so triangle AGB equals triangle ABC [1.38]. Similarly, since HG = BC = GB, triangle AHG equals triangle AGB, which equals triangle ABC [1.38]. Therefore triangle AHC = triangle AHG + triangle AGB + triangle ABC = 3 times triangle ABC. By the same reasoning, for any number m of equal segments marked off, the triangle on base equal to m times BC equals m times triangle ABC.

**Step 5.** By the same argument on the other side, since DK = CD, triangle ADK equals triangle ACD [1.38]. And since KL = CD, triangle AKL equals triangle ACD [1.38]. Therefore triangle ACL = triangle ACD + triangle ADK + triangle AKL = 3 times triangle ACD. In general, for any number n of equal segments marked off, the triangle on base equal to n times CD equals n times triangle ACD.

**Step 6.** Now let m and n be any positive integers whatsoever. Then triangle AHC (where HC = m times BC) equals m times triangle ABC, and triangle ACL (where CL = n times CD) equals n times triangle ACD, as established in Steps 4 and 5.

**Step 7.** If HC = m times BC is equal to CL = n times CD, then triangle AHC equals triangle ACL, since they are triangles on equal bases between the same parallels [1.38]. If HC is greater than CL, then triangle AHC is greater than triangle ACL, since a triangle on a greater base between the same parallels is greater. If HC is less than CL, then triangle AHC is less than triangle ACL.

**Step 8.** Therefore, whatever equimultiples m and n are taken, if m times BC is greater than, equal to, or less than n times CD, then correspondingly m times triangle ABC is greater than, equal to, or less than n times triangle ACD. By the definition of proportion [D5.5], triangle ABC is to triangle ACD as BC is to CD.

**Step 9.** Now, parallelogram EC on base BC and between the same parallels is double triangle ABC [1.41]. Similarly, parallelogram CF on base CD and between the same parallels is double triangle ACD [1.41].

**Step 10.** Since triangle ABC is to triangle ACD as BC is to CD (Step 8), and parallelogram EC is double triangle ABC while parallelogram CF is double triangle ACD, the ratio of parallelogram EC to parallelogram CF equals the ratio of their halves, that is, of triangle ABC to triangle ACD [5.15]. Therefore parallelogram EC is to parallelogram CF as BC is to CD.

**Step 11.** Therefore, triangles and parallelograms which are under the same height are to one another as their bases. Q.E.D.

**USED:** 1.38, 1.41, 5.15, D5.5, P1, P2
**Human refs (from References field):** 1.38, 1.41, 5.11, 5.15, D5.5
**Jaccard:** 0.571 — AI adds ['P1', 'P2']; Human adds ['5.11']

## Proposition 6.2
**Statement:** If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section will be parallel to the remaining side of the triangle.

**Step 1.** Let ABC be a triangle, and let DE be drawn parallel to BC, with D on AB and E on AC. We prove first that AD:DB = AE:EC.

**Step 2.** Join BE and CD [P1].

**Step 3.** Triangles BDE and CDE are on the same base DE and between the same parallels DE and BC. Therefore triangle BDE equals triangle CDE in area [1.37].

**Step 4.** Triangles ADE and BDE have the same height (the perpendicular from E to line AB), and their bases are AD and DB respectively. Therefore triangle ADE is to triangle BDE as AD is to DB [6.1].

**Step 5.** Triangles ADE and CDE have the same height (the perpendicular from D to line AC), and their bases are AE and EC respectively. Therefore triangle ADE is to triangle CDE as AE is to EC [6.1].

**Step 6.** Since triangle BDE equals triangle CDE (Step 3), the same magnitude triangle ADE has to equal magnitudes the same ratio. Therefore triangle ADE is to triangle BDE as triangle ADE is to triangle CDE [5.7].

**Step 7.** But triangle ADE is to triangle BDE as AD is to DB (Step 4), and triangle ADE is to triangle CDE as AE is to EC (Step 5). Since both ratios equal the ratio triangle ADE to triangle BDE, they are the same as one another. Therefore AD:DB = AE:EC [5.11].

**Step 8.** Now we prove the converse. Suppose the sides of triangle ABC are cut proportionally, so that AD:DB = AE:EC, with D on AB and E on AC. We prove that DE is parallel to BC.

**Step 9.** Join BE and CD [P1].

**Step 10.** Since triangle ADE and triangle BDE have the same height from E, triangle ADE is to triangle BDE as AD is to DB [6.1].

**Step 11.** Since triangle ADE and triangle CDE have the same height from D, triangle ADE is to triangle CDE as AE is to EC [6.1].

**Step 12.** Since AD:DB = AE:EC (by hypothesis), and triangle ADE is to triangle BDE as AD is to DB (Step 10), and triangle ADE is to triangle CDE as AE is to EC (Step 11), it follows that triangle ADE is to triangle BDE as triangle ADE is to triangle CDE [5.11].

**Step 13.** Since triangle ADE has the same ratio to triangle BDE as it has to triangle CDE, therefore triangle BDE equals triangle CDE [5.9].

**Step 14.** But triangles BDE and CDE are on the same base DE and on the same side of it. Triangles that are equal in area, on the same base, and on the same side are between the same parallels. Therefore DE is parallel to BC [1.39].

**Step 15.** Therefore, if a straight line is drawn parallel to one of the sides of a triangle, it cuts the sides proportionally; and if the sides are cut proportionally, the line joining the points of section is parallel to the remaining side. Q.E.D.

**USED:** 1.37, 1.39, 5.11, 5.7, 5.9, 6.1, P1
**Human refs (from References field):** 1.38, 1.39, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.625 — AI adds ['1.37', 'P1']; Human adds ['1.38']

## Proposition 6.3
**Statement:** If an angle of a triangle be bisected and the straight line cutting the angle cut the base also, the segments of the base will have the same ratio as the remaining sides of the triangle; and, if the segments of the base have the same ratio as the remaining sides of the triangle, the straight line joined from the vertex to the point of section will bisect the angle of the triangle.

Let triangle ABC be given, with the angle BAC bisected by the straight line AD, which meets BC at D. We prove both directions.

**PART I (Forward):** If AD bisects angle BAC, then BD:DC = BA:AC.

**Step 1.** Through C, draw CE parallel to DA [1.31], and produce BA to meet CE at E [P2, P5]. (Since DA and CE are parallel, and BA is a transversal that meets DA, when BA is produced it must meet CE, for the interior angles on the side of E are less than two right angles.)

**Step 2.** Since AC is a transversal falling on the parallel lines AD and EC, the alternate angles DAC and ACE are equal [1.29].

**Step 3.** Since BAE is a transversal falling on the parallel lines AD and EC, the exterior angle BAD equals the interior and opposite angle AEC on the same side [1.29].

**Step 4.** Since AD bisects angle BAC, angle BAD equals angle DAC [by hypothesis].

**Step 5.** From Steps 2, 3, and 4: angle ACE equals angle DAC equals angle BAD equals angle AEC. Therefore angle ACE equals angle AEC [CN1].

**Step 6.** Since in triangle ACE the angle ACE equals the angle AEC, the side AE equals the side AC [1.6].

**Step 7.** In triangle BCE, the line DA is parallel to CE (one side of the triangle), and DA cuts the other two sides (or their extensions): it cuts BE at A and BC at D. Therefore BD:DC = BA:AE [6.2].

**Step 8.** Since AE equals AC (Step 6), we substitute to obtain BD:DC = BA:AC [5.7].

**PART II (Converse):** If BD:DC = BA:AC, then AD bisects angle BAC.

**Step 9.** Using the same construction as before, draw CE through C parallel to DA [1.31], and let BA produced meet CE at E [P2].

**Step 10.** Since DA is parallel to CE, by the same reasoning as in Step 7 (applying 6.2 to triangle BCE with line DA parallel to side CE), we have BD:DC = BA:AE [6.2].

**Step 11.** By hypothesis, BD:DC = BA:AC. From Step 10, BD:DC = BA:AE. Therefore BA:AC = BA:AE [CN1, 5.11].

**Step 12.** Since BA:AC = BA:AE, we conclude AC = AE [5.9].

**Step 13.** Since in triangle ACE, AE equals AC, the angles opposite these equal sides are equal: angle AEC equals angle ACE [1.5].

**Step 14.** Since AD is parallel to EC: the angle BAD equals the angle AEC (corresponding angles with transversal BE) [1.29], and the angle DAC equals the angle ACE (alternate angles with transversal AC) [1.29].

**Step 15.** From Steps 13 and 14: angle BAD equals angle AEC equals angle ACE equals angle DAC. Therefore angle BAD equals angle DAC [CN1], so AD bisects angle BAC.

Therefore, if an angle of a triangle is bisected and the straight line cutting the angle cuts the base, the segments of the base have the same ratio as the remaining sides; and conversely, if the segments of the base have the same ratio as the remaining sides, the straight line from the vertex to the point of section bisects the angle. Q.E.F.

**USED:** 1.29, 1.31, 1.5, 1.6, 5.11, 5.7, 5.9, 6.2, CN1, P2, P5
**Human refs (from References field):** 1.29, 1.5, 1.6, 5.11, 5.9, 6.2
**Jaccard:** 0.545 — AI adds ['1.31', '5.7', 'CN1', 'P2', 'P5']

## Proposition 6.4
**Statement:** In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

**Step 1.** Let triangles ABC and DEF be equiangular, with angle ABC = angle DEF, angle BCA = angle EFD, and angle BAC = angle EDF. We are to show that the sides about the equal angles are proportional, namely BC:EF = BA:DE = CA:DF, where corresponding sides are those subtending equal angles.

**Step 2.** Since BC and EF are straight lines, either BC > EF, BC = EF, or BC < EF. If BC = EF, then since angle ABC = angle DEF and angle BCA = angle EFD, the triangles are congruent by 1.26, and the sides about the equal angles are trivially proportional in equal ratios. Suppose BC > EF (the case BC < EF follows by interchanging the roles of the two triangles).

**Step 3.** Since BC > EF, cut off BG from BC equal to EF, using 1.3. Through G, draw GH parallel to AC, meeting BA at H, using 1.31.

**Step 4.** Since GH is parallel to AC in triangle ABC, by 6.2 the parallel line cuts the sides proportionally: BG:GC = BH:HA.

**Step 5.** Since GH is parallel to AC and both are cut by transversal BC, the corresponding angles are equal by 1.29: angle BGH = angle BCA. Similarly, since GH is parallel to AC and both are cut by transversal BA, by 1.29: angle BHG = angle BAC.

**Step 6.** In triangle BGH, we now have angle GBH = angle ABC (since they are the same angle), angle BGH = angle BCA (Step 5), and angle BHG = angle BAC (Step 5). Since the triangles are equiangular, angle ABC = angle DEF, angle BCA = angle EFD, and angle BAC = angle EDF. Therefore angle GBH = angle DEF, angle BGH = angle EFD, and BG = EF (by construction). By 1.26, triangle BGH is congruent to triangle DEF, so BH = DE and GH = DF.

**Step 7.** From Step 4, BG:GC = BH:HA. By the porism of 5.7 (invertendo), GC:BG = HA:BH. By 5.18 (componendo), (GC + BG):BG = (HA + BH):BH, that is, BC:BG = BA:BH.

**Step 8.** Through H, draw HK parallel to BC, meeting AC at K, using 1.31. Since HK is parallel to BC in triangle ABC, by 6.2 the parallel line cuts the sides proportionally: BH:HA = CK:KA.

**Step 9.** Now GH is parallel to AC (by construction) and HK is parallel to BC (Step 8). In quadrilateral GHKC, GH is parallel to KC (since GH is parallel to AC and KC is a segment of AC), and HK is parallel to GC (since HK is parallel to BC and GC is a segment of BC). Therefore GHKC is a parallelogram. By 1.34, opposite sides of a parallelogram are equal, so GH = KC.

**Step 10.** From Step 8, BH:HA = CK:KA. Since GH = KC (Step 9), we have BH:HA = GH:KA. By the porism of 5.7 (invertendo), HA:BH = KA:GH. By 5.18 (componendo), (HA + BH):BH = (KA + GH):GH, that is, BA:BH = AC:GH.

**Step 11.** From Step 7, BC:BG = BA:BH. From Step 10, BA:BH = AC:GH. By 5.11, ratios that are each equal to the same ratio are equal to one another, so BC:BG = BA:BH = AC:GH.

**Step 12.** Since BG = EF, BH = DE, and GH = DF (Step 6), substituting into the proportion of Step 11 gives BC:EF = BA:DE = AC:DF. These are the sides about the equal angles, and those which subtend the equal angles are the corresponding sides: BC and EF subtend the equal angles BAC and EDF respectively, BA and DE subtend the equal angles BCA and EFD, and AC and DF subtend the equal angles ABC and DEF.

**Step 13.** Therefore, in equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles. Q.E.D.

**USED:** 1.26, 1.29, 1.3, 1.31, 1.34, 5.11, 5.18, 5.7, 6.2
**Human refs (from References field):** 1.17, 1.28, 1.34, 5.16, 5.22, 6.2, P5
**Jaccard:** 0.143 — AI adds ['1.26', '1.29', '1.3', '1.31', '5.11', '5.18', '5.7']; Human adds ['1.17', '1.28', '5.16', '5.22', 'P5']

## Proposition 6.5
**Statement:** If two triangles have their sides proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let ABC and DEF be two triangles having their sides proportional, so that AB is to DE as BC is to EF, and as AC is to DF.

**Step 2.** At the point D on the straight line DE, construct the angle EDG equal to the angle BAC, and at the point E on the straight line DE, construct the angle DEG equal to the angle ABC [1.23]. Then the remaining angle DGE equals the remaining angle ACB, since the three angles of each triangle are equal to two right angles [1.32].

**Step 3.** Triangle ABC is therefore equiangular with triangle DEG. By Proposition 6.4, the sides about the equal angles are proportional: AB is to DE as BC is to EG, and as AC is to DG.

**Step 4.** But AB is to DE as BC is to EF (given). Since AB is to DE as BC is to EG (Step 3) and AB is to DE as BC is to EF (given), we have BC is to EG as BC is to EF [5.11]. Therefore EG equals EF [5.9].

**Step 5.** Similarly, AB is to DE as AC is to DG (Step 3) and AB is to DE as AC is to DF (given), so AC is to DG as AC is to DF [5.11]. Therefore DG equals DF [5.9].

**Step 6.** Now in triangles DEF and DEG, the side DE is common, EF equals EG (Step 4), and DF equals DG (Step 5). Therefore triangle DEF is congruent to triangle DEG, and the angles contained by the equal sides are equal: angle EDF equals angle EDG, angle DEF equals angle DEG, and angle DFE equals angle DGE [1.8].

**Step 7.** But angle EDG equals angle BAC and angle DEG equals angle ABC (by construction), and angle DGE equals angle ACB (Step 2). Therefore angle EDF equals angle BAC, angle DEF equals angle ABC, and angle DFE equals angle ACB.

**Step 8.** Hence triangle ABC is equiangular with triangle DEF, and the equal angles are those which the corresponding (proportional) sides subtend. Q.E.D.

**USED:** 1.23, 1.32, 1.8, 5.11, 5.9, 6.4
**Human refs (from References field):** 1.23, 1.32, 1.4, 1.8, 5.11, 5.9, 6.4
**Jaccard:** 0.857 — Human adds ['1.4']

## Proposition 6.6
**Statement:** If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let triangles ABC and DEF have angle BAC equal to angle EDF, and let BA be to AC as ED is to DF. We are to show the triangles are equiangular with equal angles subtending corresponding sides.

**Step 2.** On ray DE, cut off DG equal to AB (1.3). On ray DF, cut off DH equal to AC (1.3). Join GH (P1).

**Step 3.** In triangles ABC and DGH, we have AB equal to DG (construction), AC equal to DH (construction), and angle BAC equal to angle GDH (since angle GDH is the same angle as angle EDF, which equals angle BAC by hypothesis). Therefore by 1.4 (SAS congruence), triangle ABC is congruent to triangle DGH. Hence BC equals GH, angle ABC equals angle DGH, and angle ACB equals angle DHG.

**Step 4.** Since BA is to AC as ED is to DF (given), and DG equals BA while DH equals AC (construction), we have DG is to DH as ED is to DF (CN1, substituting equals).

**Step 5.** By alternando (5.16), DG is to ED as DH is to DF.

**Step 6.** Case 1: Suppose DG equals DE. Then from Step 5, since DG is to ED as DH is to DF, and DG equals ED, we have ED is to ED as DH is to DF. By 5.9, since ED has the same ratio to ED as it has to DF through DH, we conclude DH equals DF. Therefore triangle DGH coincides with triangle DEF, and since triangle ABC is congruent to triangle DGH (Step 3), the triangles ABC and DEF are equiangular: angle BAC equals angle EDF, angle ABC equals angle DEF, and angle ACB equals angle DFE.

**Step 7.** Case 2: Suppose DG is not equal to DE. Since DG is to DH as ED is to DF (Step 4), if DG is less than DE then DH is less than DF, so G lies between D and E while H lies between D and F.

**Step 8.** From Step 4, DG is to DH as ED is to DF. Equivalently, ED is to DF as DG is to DH (5.11, symmetry of equal ratios). Since DG is less than DE and DH is less than DF, by 5.19 the remainder GE is to the remainder HF as DE is to DF. That is, GE is to HF as DE is to DF.

**Step 9.** Since DG is to DH as DE is to DF (Step 4) and GE is to HF as DE is to DF (Step 8), by 5.11 we have DG is to DH as GE is to HF. Applying alternando (5.16), DG is to GE as DH is to HF.

**Step 10.** In triangle DEF, the point G lies on side DE and the point H lies on side DF, with DG being to GE as DH is to HF (Step 9). By the converse part of 6.2, the straight line GH is parallel to the remaining side EF.

**Step 11.** Since GH is parallel to EF, and the straight line DE falls upon them, angle DGH equals angle DEF (1.29, alternate angles or corresponding angles with parallel lines). Similarly, since the straight line DF falls upon GH and EF, angle DHG equals angle DFE (1.29).

**Step 12.** From Step 3, angle ABC equals angle DGH and angle ACB equals angle DHG. Combined with Step 11, angle ABC equals angle DEF and angle ACB equals angle DFE. Together with angle BAC equal to angle EDF (given), the two triangles ABC and DEF are equiangular, and the equal angles are precisely those which the corresponding sides subtend.

**Step 13.** The case where DG is greater than DE is handled analogously: G falls on DE produced beyond E and H on DF produced beyond F, and the same proportional argument yields GH parallel to EF, leading to the same conclusion by 1.29.

**Step 14.** Therefore, if two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles are equiangular and have those angles equal which the corresponding sides subtend. Q.E.F.

**USED:** 1.29, 1.3, 1.4, 5.11, 5.16, 5.19, 5.9, 6.2, CN1, P1
**Human refs (from References field):** 1.23, 1.32, 1.4, 5.11, 5.9, 6.4
**Jaccard:** 0.231 — AI adds ['1.29', '1.3', '5.16', '5.19', '6.2', 'CN1', 'P1']; Human adds ['1.23', '1.32', '6.4']

## Proposition 6.7
**Statement:** If two triangles have one angle equal to one angle, the sides about other angles proportional, and the remaining angles either both less or both not less than a right angle, the triangles will be equiangular and will have those angles equal, the sides about which are proportional.

**Step 1.** Let ABC and DEF be two triangles having angle BAC equal to angle EDF, the sides about angles ABC and DEF proportional so that AB is to DE as BC is to EF, and the remaining angles ACB and DFE either both less than a right angle or both not less than a right angle. We must show the triangles are equiangular with angle ABC equal to angle DEF and angle ACB equal to angle DFE.

**Step 2.** Suppose angle ABC is not equal to angle DEF. Then one of them is greater. Without loss of generality, assume angle ABC is greater than angle DEF.

**Step 3.** At point B on line BA, construct angle ABG equal to angle DEF, with G on segment AC [1.23, P1]. Since angle ABG is less than angle ABC, the ray BG falls between rays BA and BC, so G lies on AC between A and C.

**Step 4.** In triangles ABG and DEF, angle BAG equals angle EDF (given, since angle BAG is the same as angle BAC) and angle ABG equals angle DEF (by construction). Therefore by the angle-sum property, angle AGB equals angle DFE [1.32].

**Step 5.** Since triangles ABG and DEF are equiangular, the sides about the equal angles are proportional. In particular, AB is to DE as BG is to EF [6.4].

**Step 6.** But it is given that AB is to DE as BC is to EF. Therefore BG is to EF as BC is to EF. Since BG and BC have the same ratio to EF, it follows that BG equals BC [5.9].

**Step 7.** Since BG equals BC, triangle BGC is isosceles, and therefore angle BGC equals angle BCG [1.5].

**Step 8.** Case 1: Suppose angles ACB and DFE are both less than a right angle. Since G lies between A and C on line AC, angles AGB and BGC are supplementary and sum to two right angles [1.13]. From Step 4, angle AGB equals angle DFE, which is less than a right angle (since angle DFE and angle ACB are both less than a right angle by hypothesis). Therefore angle BGC is greater than a right angle. But angle BGC equals angle BCG (Step 7), so angle BCG is greater than a right angle. Since G lies between A and C, angle BCG is the same angle as angle BCA. Hence angle ACB is greater than a right angle. This contradicts the hypothesis that angle ACB is less than a right angle.

**Step 9.** Case 2: Suppose angles ACB and DFE are both not less than a right angle. From Step 4, angle AGB equals angle DFE, which is not less than a right angle. Since angles AGB and BGC are supplementary [1.13], angle BGC is not greater than a right angle. By Step 7, angle BGC equals angle BCG, so angle BCG is not greater than a right angle. Since G lies between A and C, angle BCG equals angle ACB, so angle ACB is not greater than a right angle. Combined with the hypothesis that angle ACB is not less than a right angle, we conclude angle ACB is exactly a right angle. Then angle BCG is a right angle, so angle BGC is a right angle (Step 7), and therefore angle AGB is a right angle (supplementary to BGC by 1.13). Hence angle DFE is a right angle (Step 4). Now in triangle ABG, the angle sum gives angle ABG plus angle BAG plus angle AGB equals two right angles [1.32], so angle ABG plus angle BAG equals one right angle. In triangle ABC, angle ABC plus angle BAC plus angle ACB equals two right angles [1.32], so angle ABC plus angle BAC equals one right angle. Since angle BAG equals angle BAC, we obtain angle ABG equals angle ABC. But we assumed angle ABC is greater than angle ABG (since angle ABG equals angle DEF and angle ABC was assumed greater than angle DEF). This is a contradiction.

**Step 10.** Since both cases lead to contradictions, the assumption that angle ABC is not equal to angle DEF is false. Therefore angle ABC equals angle DEF.

**Step 11.** Since angle BAC equals angle EDF (given) and angle ABC equals angle DEF (Step 10), the remaining angles satisfy angle ACB equals angle DFE [1.32]. Therefore the triangles ABC and DEF are equiangular and have those angles equal, the sides about which are proportional.

**USED:** 1.13, 1.23, 1.32, 1.5, 5.9, 6.4, P1
**Human refs (from References field):** 1.13, 1.17, 1.23, 1.32, 1.5, 5.11, 5.9, 6.4
**Jaccard:** 0.667 — AI adds ['P1']; Human adds ['1.17', '5.11']

## Proposition 6.8
**Statement:** If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.

**Step 1.** Let triangle ABC have the right angle BAC, and let AD be drawn from A perpendicular to BC [D1.10]. We must show that triangles ABD and ADC are each similar to the whole triangle ABC, and also similar to one another.

**Step 2.** Consider triangles ABD and ABC. Since AD is perpendicular to BC, angle ADB is a right angle [D1.10]. But angle BAC is also a right angle by hypothesis. Therefore angle ADB equals angle BAC [P4, since all right angles are equal to one another].

**Step 3.** The angle ABD is common to both triangle ABD and triangle ABC, that is, angle ABD equals angle ABC.

**Step 4.** Since the sum of the angles in any triangle equals two right angles [1.32], and two angles of triangle ABD (namely angle ADB and angle ABD) are respectively equal to two angles of triangle ABC (namely angle BAC and angle ABC), the remaining angles must also be equal: angle BAD equals angle BCA [CN3, subtracting equals from the equal sums].

**Step 5.** Therefore triangles ABD and ABC are equiangular. Since they are equiangular, the sides about the equal angles are proportional [6.4], so triangle ABD is similar to triangle ABC [D6.1].

**Step 6.** Now consider triangles ADC and ABC. Since AD is perpendicular to BC, angle ADC is a right angle [D1.10]. But angle BAC is also a right angle by hypothesis. Therefore angle ADC equals angle BAC [P4].

**Step 7.** The angle ACD is common to both triangle ADC and triangle ABC, that is, angle ACD equals angle ACB.

**Step 8.** Since the sum of the angles in any triangle equals two right angles [1.32], and two angles of triangle ADC (namely angle ADC and angle ACD) are respectively equal to two angles of triangle ABC (namely angle BAC and angle ACB), the remaining angles must also be equal: angle DAC equals angle ABC [CN3].

**Step 9.** Therefore triangles ADC and ABC are equiangular. Since they are equiangular, the sides about the equal angles are proportional [6.4], so triangle ADC is similar to triangle ABC [D6.1].

**Step 10.** Since triangle ABD is similar to triangle ABC (Step 5) and triangle ADC is also similar to triangle ABC (Step 9), the two smaller triangles are equiangular with the same triangle and hence equiangular with each other: angle BAD equals angle ACD and angle ABD equals angle DAC and angle ADB equals angle ADC [CN1, since things equal to the same thing are equal to one another]. Therefore by the proportionality of sides about equal angles [6.4], triangle ABD is similar to triangle ADC [D6.1].

**Step 11.** Therefore, if in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another. Q.E.D.

**USED:** 1.32, 6.4, CN1, CN3, D1.10, D6.1, P4
**Human refs (from References field):** 1.32, 6.4, D6.1
**Jaccard:** 0.429 — AI adds ['CN1', 'CN3', 'D1.10', 'P4']

## Proposition 6.9
**Statement:** From a given straight line to cut off a prescribed part.

**Step 1.** Let AB be the given straight line, and let the prescribed part to be cut off be one-third (the method works for any prescribed part 1/n by taking n equal segments instead of three).

**Step 2.** From point A, draw a straight line AC making any angle with AB. [P1]

**Step 3.** On AC, take an arbitrary point D. [P1]

**Step 4.** Using D as a distance, construct DE equal to AD along AC, and then EF equal to AD along AC, so that AD = DE = EF. Thus AC contains three equal segments from A, and F lies on AC with AF composed of these three equal parts. [1.3]

**Step 5.** Join F to B. [P1]

**Step 6.** Through D, draw DG parallel to FB, meeting AB at G. [1.31]

**Step 7.** In triangle ABF, since DG is drawn parallel to the side BF, by Proposition 6.2 the line DG cuts the sides of the triangle proportionally. Therefore AD : DF = AG : GB. [6.2]

**Step 8.** Now AD is one segment and DF = DE + EF = AD + AD = 2*AD, so AD : DF = 1 : 2. Therefore AG : GB = 1 : 2. [CN1]

**Step 9.** Since AG : GB = 1 : 2, by composition of the ratio (componendo), AG + GB : GB = 1 + 2 : 2, that is, AB : GB = 3 : 2. [5.18]

**Step 10.** Since AG : GB = 1 : 2 and AB : GB = 3 : 2, we have AG : AB = 1 : 3 by the definition of proportional magnitudes, for AG is one part and AB is three such parts. Equivalently, since AB = AG + GB and GB = 2*AG, we have AB = 3*AG, so AG is one-third of AB. [CN2, D5.5]

**Step 11.** Therefore AG has been cut off from the given straight line AB, and AG is the prescribed third part of AB. The same construction works for any prescribed part 1/n by marking n equal segments on AC instead of three, joining the last to B, and drawing through the first point a line parallel to this join. Q.E.F.

**USED:** 1.3, 1.31, 5.18, 6.2, CN1, CN2, D5.5, P1
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.375 — AI adds ['5.18', 'CN1', 'CN2', 'D5.5', 'P1']

## Proposition 6.10
**Statement:** To cut a given uncut straight line similarly to a given cut straight line.

**Step 1.** Let AB be the given straight line cut at points C and D, so that the segments are AC, CD, and DB. Let EF be the given uncut straight line. It is required to cut EF similarly to AB.

**Step 2.** From E, draw a straight line at any angle to EF [P1]. On this line, place EH equal to AC, HK equal to CD, and KG equal to DB, so that EG is divided at H and K exactly as AB is divided at C and D [1.2].

**Step 3.** Join G to F [P1].

**Step 4.** Through H, draw HL parallel to GF, meeting EF at L [1.31]. Through K, draw KM parallel to GF, meeting EF at M [1.31].

**Step 5.** Since HL and KM are each parallel to GF, they are parallel to one another [1.30]. Now in triangle EKM, the line HL is parallel to side KM and meets sides EK and EM at H and L respectively. Therefore, by Proposition 6.2, EH : HK = EL : LM.

**Step 6.** In triangle EGF, the line KM is parallel to side GF and meets sides EG and EF at K and M respectively. Therefore, by Proposition 6.2, EK : KG = EM : MF.

**Step 7.** From Step 5, since EH : HK = EL : LM, by componendo [5.18], (EH + HK) : HK = (EL + LM) : LM, that is, EK : HK = EM : LM.

**Step 8.** Since EK : HK = EM : LM, and all four magnitudes are straight lines, by alternando [5.16], EK : EM = HK : LM.

**Step 9.** From Step 6, since EK : KG = EM : MF, by alternando [5.16], EK : EM = KG : MF.

**Step 10.** From Steps 8 and 9, EK : EM = HK : LM and EK : EM = KG : MF. Therefore HK : LM = KG : MF [CN1].

**Step 11.** By alternando [5.16], HK : KG = LM : MF.

**Step 12.** We now have EH : HK = EL : LM (Step 5) and HK : KG = LM : MF (Step 11). Since by construction EH = AC, HK = CD, and KG = DB, it follows that AC : CD = EL : LM and CD : DB = LM : MF. Therefore the straight line EF has been cut at L and M similarly to the given cut straight line AB.

Q.E.D.

**USED:** 1.2, 1.30, 1.31, 5.16, 5.18, 6.2, CN1, P1
**Human refs (from References field):** 1.31, 1.34, 6.2
**Jaccard:** 0.222 — AI adds ['1.2', '1.30', '5.16', '5.18', 'CN1', 'P1']; Human adds ['1.34']

## Proposition 6.11
**Statement:** To two given straight lines to find a third proportional.

**Step 1.** Let BA and AC be the two given straight lines. It is required to find a third proportional to BA and AC, that is, a line such that BA : AC = AC : that line.

**Step 2.** Place BA and AC so that they contain any angle at A. Produce BA in the direction of A to D. [P2]

**Step 3.** Set BD equal to AC. [1.3]

**Step 4.** Join B to C. [P1]

**Step 5.** Through D, draw DE parallel to BC, meeting AC produced at E. [1.31, P2]

**Step 6.** Since BC is parallel to a side DE in triangle ADE, and the line BC cuts the sides AD and AE, by Proposition 6.2, AB : BD = AC : CE.

**Step 7.** But BD was made equal to AC (Step 3). Since BD = AC, by Proposition 5.7 (equal magnitudes have to the same magnitude the same ratio, and the same magnitude has to equal magnitudes the same ratio), AB : BD = AB : AC.

**Step 8.** Therefore AB : AC = AC : CE. [CN1, combining Steps 6 and 7: AB : BD = AC : CE and AB : BD = AB : AC, so AB : AC = AC : CE]

**Step 9.** Thus CE is a third proportional to the two given straight lines BA and AC, which is what was required to find.

**USED:** 1.3, 1.31, 5.7, 6.2, CN1, P1, P2
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.429 — AI adds ['5.7', 'CN1', 'P1', 'P2']

## Proposition 6.12
**Statement:** To three given straight lines to find a fourth proportional.

**Step 1.** Let A, B, C be the three given straight lines. It is required to find a fourth proportional, that is, to find a straight line D such that A is to B as C is to D.

**Step 2.** Set out two straight lines DE and DF containing any angle EDF. [P1]

**Step 3.** On DE, cut off DG equal to A, and GE equal to B, so that DG = A and GE = B. [1.3]

**Step 4.** On DF, cut off DH equal to C, so that DH = C. [1.3]

**Step 5.** Join GH. [P1]

**Step 6.** Through E, draw EF parallel to GH. [1.31]

**Step 7.** Since GH is parallel to EF, a side of triangle DEF, by Proposition 6.2 the parallel line GH cuts the sides of triangle DEF proportionally. Therefore DG is to GE as DH is to HF. [6.2]

**Step 8.** But DG = A, GE = B, and DH = C. Therefore A is to B as C is to HF. [D5.6, CN1]

**Step 9.** Therefore to the three given straight lines A, B, C a fourth proportional HF has been found. Q.E.F.

**USED:** 1.3, 1.31, 6.2, CN1, D5.6, P1
**Human refs (from References field):** 1.31, 6.2
**Jaccard:** 0.333 — AI adds ['1.3', 'CN1', 'D5.6', 'P1']

## Proposition 6.13
**Statement:** To two given straight lines to find a mean proportional.

**Step 1.** Let AB and BC be the two given straight lines. Place them in a straight line so that A, B, C are collinear with B between A and C. [P1]

**Step 2.** Bisect AC at its midpoint E. [1.10]

**Step 3.** With centre E and radius EA (equal to EC), describe a semicircle ADC on the diameter AC. [P3, D1.17, D1.18]

**Step 4.** From B, draw BD at right angles to AC, meeting the semicircle at D. [1.11, P2]

**Step 5.** Join AD and DC. [P1]

**Step 6.** The angle ADC is an angle in a semicircle on diameter AC, so angle ADC is a right angle. [3.31]

**Step 7.** In the right-angled triangle ADC, BD has been drawn from D perpendicular to the base AC (since BD is at right angles to AC by construction). The angle ADB plus angle BDC equals angle ADC, which is a right angle. By 6.8, the triangles ABD and DBC adjoining the perpendicular are similar both to the whole triangle ADC and to one another. [6.8]

**Step 8.** Since triangle ABD is similar to triangle DBC, the sides about their equal angles are proportional. In triangle ABD, the side AB subtends angle ADB; in triangle DBC, the side BD subtends the equal angle BDC (equal because each triangle is similar to the whole and the angles at B are both right angles). Likewise BD subtends angle ADB in triangle ABD, and BC subtends the corresponding angle BDC in triangle DBC. Therefore AB is to BD as BD is to BC. [6.4, D6.1]

**Step 9.** Therefore BD is a mean proportional between the two given straight lines AB and BC. [D5.8]

Q.E.F.

**USED:** 1.10, 1.11, 3.31, 6.4, 6.8, D1.17, D1.18, D5.8, D6.1, P1, P2, P3
**Human refs (from References field):** 3.31, 6.8
**Jaccard:** 0.167 — AI adds ['1.10', '1.11', '6.4', 'D1.17', 'D1.18', 'D5.8', 'D6.1', 'P1', 'P2', 'P3']

## Proposition 6.14
**Statement:** In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal.

**Step 1.** Let ABCD and CEFG be two equal and equiangular parallelograms, with angle BCD equal to angle ECG. We must show that the sides about the equal angles are reciprocally proportional, that is, BC : CG = EC : CD.

**Step 2.** Place the parallelograms so that the sides BC and CG about the equal angles are in a straight line, with C between B and G. Since BCG is a straight line, angle BCD + angle DCG equals two right angles [1.13].

**Step 3.** Since angle BCD equals angle ECG (given), substituting yields angle ECG + angle DCG equals two right angles. Therefore DC and CE are in a straight line [1.14]. Call this straight line DE.

**Step 4.** Through D, draw DH parallel to CG, and through G, draw GH parallel to CD, completing parallelogram DCHG [1.31].

**Step 5.** Since ABCD is a parallelogram, AD is parallel to BC, that is, AD is parallel to BG [1.34]. Since DCHG is a parallelogram, DH is parallel to CG, that is, DH is parallel to BG [1.34]. Both AD and DH pass through point D and are each parallel to BG. If AD and DH were distinct lines, they would be two different lines through D both parallel to BG; but lines parallel to the same line are parallel to one another [1.30], so AD would be parallel to DH, which is impossible since they share the point D. Therefore A, D, and H are collinear, and the parallelograms ABCD and DCHG lie between the same parallels, namely line BG and line ADH.

**Step 6.** Similarly, since CEFG is a parallelogram, GF is parallel to CE, that is, GF is parallel to DE [1.34]. Since DCHG is a parallelogram, GH is parallel to DC, that is, GH is parallel to DE [1.34]. Both GF and GH pass through point G and are each parallel to DE. By the same reasoning as in Step 5 using [1.30], F, G, and H are collinear, and the parallelograms CEFG and DCHG lie between the same parallels, namely line DE and line FGH.

**Step 7.** Since parallelograms ABCD and DCHG are between the same parallels (line BG and line ADH) and have their bases BC and CG on the same line BG, by [6.1] we have ABCD : DCHG = BC : CG.

**Step 8.** Since parallelograms CEFG and DCHG are between the same parallels (line DE and line FGH) and have their bases CE and CD on the same line DE, by [6.1] we have CEFG : DCHG = CE : CD.

**Step 9.** Now since ABCD equals CEFG (given), we have ABCD : DCHG = CEFG : DCHG. From Steps 7 and 8, BC : CG = ABCD : DCHG and CE : CD = CEFG : DCHG. Since BC : CG and CE : CD are each equal to the same ratio (namely the ratio of ABCD to DCHG, which equals the ratio of CEFG to DCHG), we conclude BC : CG = CE : CD [5.11]. This completes the first part: the sides about the equal angles are reciprocally proportional.

**Step 10.** Conversely, let ABCD and CEFG be equiangular parallelograms with angle BCD equal to angle ECG, and suppose BC : CG = EC : CD. We must show that ABCD equals CEFG.

**Step 11.** Arrange the parallelograms and complete parallelogram DCHG exactly as in Steps 2 through 6.

**Step 12.** By [6.1], as before, ABCD : DCHG = BC : CG, and CEFG : DCHG = CE : CD.

**Step 13.** Since BC : CG = EC : CD (given), and ABCD : DCHG = BC : CG while CEFG : DCHG = CE : CD, it follows that ABCD : DCHG = CEFG : DCHG [5.11].

**Step 14.** Since ABCD and CEFG have the same ratio to DCHG, we conclude ABCD equals CEFG [5.9]. This completes the converse.

**Step 15.** Therefore, in equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal. Q.E.D.

**USED:** 1.13, 1.14, 1.30, 1.31, 1.34, 5.11, 5.9, 6.1
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.444 — AI adds ['1.13', '1.30', '1.31', '1.34']; Human adds ['5.7']

## Proposition 6.15
**Statement:** In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal.

**Step 1.** Let triangles ABC and ADE be equal in area, with angle BAC equal to angle DAE. We must show that the sides about the equal angles are reciprocally proportional, that is, BA : AD = EA : AC.

**Step 2.** Place the triangles so that vertex A is common and the sides CA and AD lie along the same straight line, with C and D on opposite sides of A. Since CAD is a straight line, by 1.13 the angles on one side sum to two right angles: angle BAC + angle BAD = two right angles.

**Step 3.** Since angle BAC = angle DAE (given), substituting yields angle DAE + angle BAD = two right angles. But angle DAE + angle BAD = angle BAE (since D lies on the ray from A opposite to C, and E is on the same side). Therefore the angles which BA and AE make with line CAD on the same side sum to two right angles, so by 1.14, the points B, A, E are collinear, that is, BA and AE lie in a straight line.

**Step 4.** Join BD [P1].

**Step 5.** Consider triangles ABD and ABC. They share the same vertex B, and their bases AD and AC lie along the same straight line CAD. Therefore they are under the same height (the perpendicular from B to line CAD). By 6.1, triangle ABD : triangle ABC = AD : AC.

**Step 6.** Consider triangles ABD and ADE. They share the same vertex D, and their bases AB and AE lie along the same straight line BAE. Therefore they are under the same height (the perpendicular from D to line BAE). By 6.1, triangle ABD : triangle ADE = AB : AE.

**Step 7.** Since triangle ABC = triangle ADE (given, equal in area), the magnitude triangle ABD has the same ratio to each of these equal magnitudes. By 5.7, triangle ABD : triangle ABC = triangle ABD : triangle ADE.

**Step 8.** From Steps 5 and 7: triangle ABD : triangle ABC = AD : AC and triangle ABD : triangle ABC = triangle ABD : triangle ADE. From Step 6: triangle ABD : triangle ADE = AB : AE. Therefore, by 5.11, AD : AC = AB : AE.

**Step 9.** Since AB : AE = AD : AC (rewriting the same proportion), by 5.16 (alternando), AB : AD = AE : AC. That is, BA : AD = EA : AC, which is the reciprocal proportionality of the sides about the equal angles.

**Step 10.** Now for the converse. Let triangles ABC and ADE have angle BAC equal to angle DAE, and let the sides about the equal angles be reciprocally proportional: BA : AD = EA : AC. We must show that triangle ABC = triangle ADE.

**Step 11.** Place the triangles as before so that CA and AD are in a straight line. By the same reasoning as in Steps 2 and 3 (using 1.13 and 1.14), BA and AE are also in a straight line. Join BD [P1].

**Step 12.** By 6.1 (as in Step 5), triangle ABD : triangle ABC = AD : AC. By 6.1 (as in Step 6), triangle ABD : triangle ADE = AB : AE.

**Step 13.** From the given proportion BA : AD = EA : AC, that is AB : AD = AE : AC, by 5.16 (alternando) we obtain AB : AE = AD : AC.

**Step 14.** From Step 12, triangle ABD : triangle ADE = AB : AE = AD : AC (by Step 13). Also from Step 12, triangle ABD : triangle ABC = AD : AC. Therefore by 5.11, triangle ABD : triangle ADE = triangle ABD : triangle ABC.

**Step 15.** Since triangle ABD has the same ratio to both triangle ADE and triangle ABC, by 5.9, triangle ABC = triangle ADE. Therefore the triangles are equal in area.

**Step 16.** Therefore, in equal triangles which have one angle equal to one angle, the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal. Q.E.D.

**USED:** 1.13, 1.14, 5.11, 5.16, 5.7, 5.9, 6.1, P1
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.625 — AI adds ['1.13', '5.16', 'P1']

## Proposition 6.16
**Statement:** If four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes be equal to the rectangle contained by the means, the four straight lines will be proportional.

**Step 1.** Let A, B, C, D be four straight lines such that A : B :: C : D. We must show that the rectangle contained by A and D equals the rectangle contained by B and C.

**Step 2.** Set out a point E. From E, draw a straight line EF equal to A and a straight line EG equal to D, making the angle FEG a right angle [P1, 1.3, 1.11]. Complete the rectangle (parallelogram) EFHG with sides EF = A and EG = D [1.31, 1.34]. This rectangle is the rectangle contained by A and D.

**Step 3.** Similarly, from E draw EK equal to B along the same line as EF (or its extension), and EL equal to C along the same line as EG (or its extension), again making a right angle at E [P1, 1.3, 1.11]. Complete the rectangle EKLM with sides EK = B and EL = C [1.31, 1.34]. This rectangle is the rectangle contained by B and C.

**Step 4.** Now the rectangles EFHG and EKLM are equiangular parallelograms, since each has a right angle at E. The sides about the equal right angles are: EF (= A) and EG (= D) for the first rectangle, and EK (= B) and EL (= C) for the second rectangle.

**Step 5.** By hypothesis, A : B :: C : D, that is, EF : EK :: EL : EG. This is precisely the condition that the sides about the equal angles are reciprocally proportional [D6.2].

**Step 6.** Therefore, by the converse part of Proposition 6.14, the two equiangular parallelograms EFHG and EKLM are equal. That is, the rectangle contained by A and D equals the rectangle contained by B and C.

**Step 7.** Now conversely, suppose the rectangle contained by A and D equals the rectangle contained by B and C. Construct the same rectangles EFHG and EKLM as before, with EF = A, EG = D, EK = B, EL = C, each having a right angle at E.

**Step 8.** Since the rectangles are equal equiangular parallelograms (each having a right angle at E), by the forward part of Proposition 6.14, the sides about the equal angles are reciprocally proportional. That is, EF : EK :: EL : EG, which gives A : B :: C : D.

**Step 9.** Therefore the four straight lines A, B, C, D are proportional. This completes both directions, and the proposition is proved. Q.E.F.

**USED:** 1.11, 1.3, 1.31, 1.34, 6.14, D6.2, P1
**Human refs (from References field):** 6.14
**Jaccard:** 0.143 — AI adds ['1.11', '1.3', '1.31', '1.34', 'D6.2', 'P1']

## Proposition 6.17
**Statement:** If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to the square on the mean, the three straight lines will be proportional.

**Step 1.** Let A, B, C be three straight lines in proportion, so that A is to B as B is to C. We must show that the rectangle contained by A and C is equal to the square on B.

**Step 2.** Since A is to B as B is to C, we have four straight lines A, B, B, C that are proportional, with the first to the second as the third to the fourth (the two means being equal).

**Step 3.** By Proposition 6.16, if four straight lines are proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means. Therefore the rectangle contained by A and C is equal to the rectangle contained by B and B.

**Step 4.** But the rectangle contained by B and B is the square on B, since the square on a straight line is the rectangle contained by that line with itself (D2.1, D1.22). Therefore the rectangle contained by A and C is equal to the square on B.

**Step 5.** Now suppose conversely that the rectangle contained by A and C is equal to the square on B. We must show that A is to B as B is to C.

**Step 6.** The square on B is equal to the rectangle contained by B and B (D2.1, D1.22). Therefore the rectangle contained by A and C is equal to the rectangle contained by B and B.

**Step 7.** By the converse part of Proposition 6.16, if the rectangle contained by the extremes is equal to the rectangle contained by the means, the four straight lines are proportional. Therefore A is to B as B is to C, and the three lines are proportional.

**Step 8.** Therefore, if three straight lines are proportional, the rectangle contained by the extremes equals the square on the mean; and if the rectangle contained by the extremes equals the square on the mean, the three lines are proportional. Q.E.D.

**USED:** 6.16, D1.22, D2.1
**Human refs (from References field):** 6.16
**Jaccard:** 0.333 — AI adds ['D1.22', 'D2.1']

## Proposition 6.18
**Statement:** On a given straight line to describe a rectilineal figure similar and similarly situated to a given rectilineal figure.

**Step 1.** Let the given straight line be FG, and let the given rectilineal figure be the polygon ABCDE (the argument applies to any polygon with four or more sides; the triangular case is handled directly by 6.4 and 1.23). We are to construct on FG a rectilineal figure similar and similarly situated to ABCDE.

**Step 2.** Join BD and BE, thereby decomposing the polygon ABCDE into the triangles ABE, EBD, and BDC [P1].

**Step 3.** On the straight line FG, construct a triangle FHG equiangular with triangle ABE as follows: at F, construct angle GFH equal to angle ABE, and at G, construct angle FGH equal to angle AEB [1.23]. Since the angles of triangle ABE sum to two right angles [1.32], and angle GFH equals angle ABE and angle FGH equals angle AEB, the remaining angle FHG equals the remaining angle BAE [1.32, CN3]. Therefore triangle FHG is equiangular with triangle ABE.

**Step 4.** On the straight line HG, construct a triangle HKG equiangular with triangle EBD: at H, construct angle GHK equal to angle EBD, and at G, construct angle HGK equal to angle BED [1.23]. By the same reasoning as in Step 3, triangle HKG is equiangular with triangle EBD [1.32, CN3].

**Step 5.** On the straight line KG, construct a triangle KLG equiangular with triangle BDC: at K, construct angle GKL equal to angle DBC, and at G, construct angle KGL equal to angle BDC [1.23]. By the same reasoning, triangle KLG is equiangular with triangle BDC [1.32, CN3].

**Step 6.** The figure FHKLG has been constructed on FG. We now prove it is similar and similarly situated to ABCDE [D6.1]. First we show the corresponding angles are equal.

**Step 7.** Angle HFG equals angle BAE, since these are the angles FHG... rather, angle GFH was constructed equal to angle ABE, and angle FHG equals angle BAE (from Step 3). Wait — to clarify: in triangle FHG, angle at F (that is, angle HFG) was constructed equal to angle ABE. But the angle of the polygon at A is angle BAE = angle of triangle ABE at A, which equals angle FHG. The angle of the polygon FHKLG at F is angle HFG, which equals angle ABE. Actually, let me re-identify: the polygon ABCDE has angle at A = angle EAB, which corresponds to angle at the vertex of FHG at the position corresponding to A. Since the triangles ABE and FHG are equiangular with angle BAE = angle HFG... Let me re-establish the correspondence. Triangle ABE has vertices A, B, E. Triangle FHG has vertices F, H, G with angle at F equal to angle at A (= angle BAE), angle at H equal to angle at B (= angle ABE), angle at G equal to angle at E (= angle AEB). So vertex A corresponds to F, B corresponds to H, E corresponds to G. Thus the polygon vertex A corresponds to polygon vertex F, and angle EAB = angle GFH. This is angle of the figure at F.

**Step 8.** The angle of figure ABCDE at B is angle ABC = angle ABE + angle EBD + angle DBC. The angle of figure FHKLG at H is angle FHK = angle FHG + angle GHK. Now angle FHG = angle ABE (Step 3 correspondence: angle at H = angle at B), and angle GHK = angle EBD (Step 4). But we also need angle DBC. Actually, checking the triangle count: ABCDE is a pentagon decomposed into 3 triangles (ABE, EBD, BDC), and the angle at B involves all three triangles. However, in figure FHKLG, vertex H is shared by triangles FHG and HKG only, and vertex K is shared by triangles HKG and KLG. The angle at H in the figure is angle FHK = angle FHG + angle GHK = angle ABE + angle EBD. This does not include angle DBC. Let me reconsider the vertex correspondence.

Actually, the correct correspondence for the polygon FHKLG to ABCDE should be re-examined. The decomposition of ABCDE from vertex B gives triangles ABE (with side AE as part of the polygon boundary), EBD (with side ED as boundary), BDC (with side DC as boundary). The sides of the polygon are AB, BC, CD, DE, EA.

In the reconstruction on FG (which corresponds to AE), the first triangle FHG corresponds to ABE with F↔A, H↔B, G↔E. The second triangle HKG corresponds to EBD with H↔B, K↔D, G↔E. The third triangle KLG corresponds to BDC with K↔D, L↔C, G↔B.

So the polygon FHKLG corresponds to ABDCA... no. Let me reconsider. The polygon ABCDE has boundary vertices A, B, C, D, E in order. From vertex B, diagonals go to D and E. The triangles are: ABE (boundary sides AB, AE), BDE (boundary side DE), BCD (boundary sides BC, CD). The polygon vertices not at B are A, C, D, E. In the reconstruction: A↔F, E↔G (from first triangle). D↔K (from second triangle). C↔L (from third triangle). B is an internal vertex in the decomposition, corresponding to H and also to G in different triangles. But H corresponds to B in the first two triangles, and G corresponds to E in the first two but to B in the third. This creates a contradiction in the simple approach.

Let me restart with the classical construction more carefully. The standard approach in Euclid decomposes the given figure from one vertex and reconstructs on the given line.

OK — let me use the construction as Euclid actually does it, decomposing from a single vertex of the given figure, not an interior vertex.

**REVISED CLEAN PROOF:**

**Step 1.** Let the given straight line be AB, and let the given rectilineal figure be CDEFG (a pentagon; the argument generalizes to any polygon). We must describe on AB a figure similar and similarly situated to CDEFG.

**Step 2.** Join DF and DG, decomposing CDEFG into the triangles FCD, FDE, and DGF... no, let me decompose from vertex C. Join CE, decomposing CDEFG into triangles CDE, CEF (wait, that only works for specific polygons). Let me use a quadrilateral for simplicity, as Euclid does, then note the generalization.

Let the given rectilineal figure be the quadrilateral ABCD (renaming for clarity), and let the given straight line be EF. Join AC, decomposing ABCD into triangles ABC and ACD.

**Step 3.** On EF, construct triangle EGF equiangular with triangle ABC: at E construct angle FEG equal to angle BAC, and at F construct angle EFG equal to angle ABC [1.23]. Then angle EGF equals angle ACB [1.32, CN3], and triangle EGF is equiangular with triangle ABC, hence similar to it [6.4].

**Step 4.** On EG (corresponding to AC), construct triangle EHG equiangular with triangle ACD: at E construct angle GEH equal to angle CAD, and at G construct angle EGH equal to angle ACD [1.23]. Then triangle EHG is equiangular with triangle ACD, hence similar to it [1.32, CN3, 6.4].

**Step 5.** The figure EFGH has been constructed on EF. We show it is similar and similarly situated to ABCD.

**Step 6.** (Angles are equal.) The angle at E in figure EFGH is angle FEH = angle FEG + angle GEH = angle BAC + angle CAD = angle BAD [CN2], which is the angle at A in figure ABCD.

**Step 7.** The angle at G in figure EFGH is angle FGH = angle FGE + angle EGH = angle BCA + angle ACD = angle BCD [CN2], which is the angle at C in ABCD.

**Step 8.** The angle at F in EFGH equals angle ABC (from Step 3, since triangle EGF is equiangular with triangle ABC and angle EFG = angle ABC). The angle at H in EFGH equals angle ADC (from Step 4, since triangle EHG is equiangular with triangle ACD and angle EHG = angle ADC). Thus all four corresponding angles are equal.

**Step 9.** (Sides are proportional.) Since triangles ABC and EGF are similar [6.4], we have AB:EF = BC:FG = AC:EG.

**Step 10.** Since triangles ACD and EGH are similar [6.4], we have AC:EG = CD:GH = DA:HE.

**Step 11.** Since AB:EF = AC:EG (Step 9) and AC:EG = CD:GH (Step 10), by transitivity of ratios [5.11] we have AB:EF = CD:GH. Likewise AB:EF = DA:HE. Combined with AB:EF = BC:FG from Step 9, the sides about the equal angles are proportional: AB:EF = BC:FG = CD:GH = DA:HE.

**Step 12.** Since the figures ABCD and EFGH have their angles severally equal (Steps 6-8) and the sides about the equal angles proportional (Step 11), they are similar rectilineal figures [D6.1], and they are similarly situated since corresponding vertices appear in the same order.

**Step 13.** The construction generalizes to any polygon with more than four sides: decompose the given polygon into triangles by joining successive diagonals from one vertex, then on the given line construct a sequence of similar triangles sharing sides that correspond to those diagonals, using 1.23 to construct equal angles. At each stage, 6.4 gives the similarity of each pair of triangles, and 5.11 chains the proportions across successive triangle pairs. The angles of the constructed figure equal the corresponding angles of the given figure by addition of the triangle angles [CN2], and the sides about equal angles are proportional by the chain of equal ratios.

**Step 14.** Therefore, on the given straight line AB, the rectilineal figure EFGH (or its generalization) has been described similar and similarly situated to the given rectilineal figure ABCD. Q.E.F.

**USED:** 1.23, 1.32, 5.11, 6.4, CN2, CN3, D6.1, P1
**Human refs (from References field):** 1.23, 1.32, 6.4, D6.1
**Jaccard:** 0.500 — AI adds ['5.11', 'CN2', 'CN3', 'P1']

## Proposition 6.19
**Statement:** Similar triangles are to one another in the duplicate ratio of the corresponding sides.

**Step 1.** Let ABC and DEF be similar triangles, with angle ABC equal to angle DEF, and let BC and EF be corresponding sides (subtending equal angles BAC and EDF respectively). By the definition of similar rectilineal figures (D6.1), the angles of the triangles are severally equal and the sides about the equal angles are proportional.

**Step 2.** Since triangles ABC and DEF are similar with angle ABC equal to angle DEF, the sides about these equal angles are proportional (D6.1), so that BC is to EF as AB is to DE.

**Step 3.** Using 6.11, find a third proportional BG to BC and EF, so that BC is to EF as EF is to BG. Place BG along the ray from B through C (or its extension) so that A and G are on the same side, and join AG.

**Step 4.** Since BC, EF, BG are three magnitudes in continued proportion (BC:EF = EF:BG), by D5.9, BC has to BG the duplicate ratio of that which BC has to EF.

**Step 5.** Since triangles ABC and ABG share the same vertex A and have their bases BC and BG on the same straight line, they are under the same height. Therefore by 6.1, triangle ABC is to triangle ABG as BC is to BG.

**Step 6.** From Step 2, BC is to EF as AB is to DE. From Step 3, BC is to EF as EF is to BG. Therefore by 5.11 (ratios equal to the same ratio are equal to one another), AB is to DE as EF is to BG.

**Step 7.** Now consider triangles ABG and DEF. We have angle ABG equal to angle DEF (since angle ABG is the same as angle ABC, which equals angle DEF). The sides about these equal angles satisfy: AB is to DE as EF is to BG (from Step 6). That is, the sides about the equal angles are reciprocally proportional (AB and BG about angle B in triangle ABG correspond reciprocally to DE and EF about angle E in triangle DEF).

**Step 8.** By the converse part of 6.15, since triangles ABG and DEF have one angle equal to one angle (angle ABG equals angle DEF) and the sides about the equal angles are reciprocally proportional, triangle ABG is equal to triangle DEF.

**Step 9.** Since triangle ABG equals triangle DEF, by 5.7 (equal magnitudes have the same ratio to the same magnitude), triangle ABC is to triangle ABG as triangle ABC is to triangle DEF.

**Step 10.** From Step 5, triangle ABC is to triangle ABG as BC is to BG. From Step 9, triangle ABC is to triangle ABG as triangle ABC is to triangle DEF. Therefore by 5.11, triangle ABC is to triangle DEF as BC is to BG.

**Step 11.** But BC has to BG the duplicate ratio of that which BC has to EF (Step 4). Therefore triangle ABC has to triangle DEF the duplicate ratio of that which side BC has to the corresponding side EF.

**Step 12.** Therefore similar triangles are to one another in the duplicate ratio of the corresponding sides. Q.E.D.

**USED:** 5.11, 5.7, 6.1, 6.11, 6.15, D5.9, D6.1
**Human refs (from References field):** 5.11, 5.16, 6.1, 6.11, 6.15, D5.11, D5.9
**Jaccard:** 0.556 — AI adds ['5.7', 'D6.1']; Human adds ['5.16', 'D5.11']

## Proposition 6.20
**Statement:** Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate of that which the corresponding side has to the corresponding  side.

**Step 1.** Let ABCDE and FGHKL be similar polygons, and let AB correspond to FG. We must show that these polygons are divided into similar triangles equal in multitude and in the same ratio as the wholes, and that polygon ABCDE has to polygon FGHKL a ratio duplicate of that which AB has to FG.

**Step 2.** Join BE, EC in polygon ABCDE, and GL, LH in polygon FGHKL, drawing diagonals from one vertex to all non-adjacent vertices. This divides ABCDE into triangles ABE, BCE, CDE, and FGHKL into triangles FGL, GHL, HKL. Both polygons are divided into the same number of triangles, namely three (and in general, for an n-sided polygon, n-2 triangles). [P1]

**Step 3.** Since ABCDE and FGHKL are similar polygons, angle A equals angle F, and the sides about the equal angles are proportional, so BA is to AE as GF is to FL. [D6.1]

**Step 4.** Since angle A equals angle F and the sides about these equal angles are proportional (BA:AE = GF:FL), triangle ABE is equiangular with triangle FGL. [6.6]

**Step 5.** Therefore angle ABE equals angle FGL, and angle AEB equals angle FLG. [6.6]

**Step 6.** Since the polygons are similar, the whole angle ABC equals the whole angle FGH. [D6.1]

**Step 7.** Since angle ABE equals angle FGL (Step 5), the remaining angle EBC equals the remaining angle LGH. [CN3]

**Step 8.** Since triangles ABE and FGL are equiangular (Step 4), we have EB:BA = LG:GF. [6.4]

**Step 9.** Since the polygons are similar, AB:BC = FG:GH. [D6.1]

**Step 10.** Therefore, by the equality of ratios (ex aequali), EB:BC = LG:GH. [5.22]

**Step 11.** The sides about the equal angles EBC and LGH are thus proportional (EB:BC = LG:GH). Since angle EBC equals angle LGH (Step 7) and the sides about these equal angles are proportional, triangle EBC is equiangular with triangle LGH. [6.6]

**Step 12.** By the same reasoning, since triangle EBC is equiangular with triangle LGH, angle BEC equals angle GLH, and angle BCE equals angle GHL. [6.6]

**Step 13.** Since the polygons are similar, the whole angle BCD equals the whole angle GHK. [D6.1]

**Step 14.** Since angle BCE equals angle GHL (Step 12), the remaining angle ECD equals the remaining angle LHK. [CN3]

**Step 15.** From triangle EBC equiangular with triangle LGH, we have EC:CB = LH:HG. [6.4]

**Step 16.** Since the polygons are similar, BC:CD = GH:HK. [D6.1]

**Step 17.** Therefore, by the equality of ratios, EC:CD = LH:HK. [5.22]

**Step 18.** Since angle ECD equals angle LHK (Step 14) and the sides about these equal angles are proportional (EC:CD = LH:HK), triangle ECD is equiangular with triangle LHK. [6.6]

**Step 19.** Therefore the similar polygons ABCDE and FGHKL have been divided into similar triangles (ABE similar to FGL, BCE similar to GLH, CDE similar to LHK), and into triangles equal in multitude, namely three each. [D6.1]

**Step 20.** We now show the triangles are in the same ratio as the wholes. Since triangle ABE is similar to triangle FGL, triangle ABE has to triangle FGL the duplicate ratio of that which BE has to GL. [6.19]

**Step 21.** Similarly, since triangle EBC is similar to triangle LGH, triangle EBC has to triangle LGH the duplicate ratio of that which BE has to GL (since EB:LG is a pair of corresponding sides). [6.19]

**Step 22.** Therefore triangle ABE is to triangle FGL as triangle EBC is to triangle LGH, since both ratios are duplicate of the same ratio BE:GL. [5.11]

**Step 23.** Similarly, since triangle EBC is similar to triangle LGH, triangle EBC has to triangle LGH the duplicate ratio of that which EC has to LH. [6.19]

**Step 24.** And since triangle ECD is similar to triangle LHK, triangle ECD has to triangle LHK the duplicate ratio of that which EC has to LH. [6.19]

**Step 25.** Therefore triangle EBC is to triangle LGH as triangle ECD is to triangle LHK, since both ratios are duplicate of the same ratio EC:LH. [5.11]

**Step 26.** From Steps 22 and 25, triangle ABE is to triangle FGL as triangle EBC is to triangle LGH, and as triangle ECD is to triangle LHK. [5.11]

**Step 27.** Since triangle ABE is to triangle FGL as triangle EBC is to triangle LGH as triangle ECD is to triangle LHK, it follows that the sum ABE + EBC + ECD is to the sum FGL + LGH + LHK in the same ratio as each component. That is, polygon ABCDE is to polygon FGHKL as triangle ABE is to triangle FGL. [5.12]

**Step 28.** But triangle ABE has to triangle FGL the duplicate ratio of that which side AB has to side FG, since triangle ABE is similar to triangle FGL and AB, FG are corresponding sides. [6.19]

**Step 29.** Therefore polygon ABCDE has to polygon FGHKL the duplicate ratio of that which the corresponding side AB has to the corresponding side FG. [5.11]

**Step 30.** Therefore similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate of that which the corresponding side has to the corresponding side. Q.E.D.

**USED:** 5.11, 5.12, 5.22, 6.19, 6.4, 6.6, CN3, D5.9, D6.1, P1
**Human refs (from References field):** 1.32, 5.12, 5.22, 6.1, 6.19, 6.4, 6.6, D6.1
**Jaccard:** 0.500 — AI adds ['5.11', 'CN3', 'D5.9', 'P1']; Human adds ['1.32', '6.1']

## Proposition 6.21
**Statement:** Figures which are similar to the same rectilineal figure are also similar to one another.

**Step 1.** Let A and B be two rectilineal figures, each similar to the same rectilineal figure C. We must show that A is similar to B.

**Step 2.** Since A is similar to C, by Definition D6.1, the angles of A are severally equal to the corresponding angles of C, and the sides of A about the equal angles are proportional to the corresponding sides of C.

**Step 3.** Since B is similar to C, by Definition D6.1, the angles of B are severally equal to the corresponding angles of C, and the sides of B about the equal angles are proportional to the corresponding sides of C.

**Step 4.** Consider any angle of A that equals a corresponding angle of C (Step 2), and the corresponding angle of B that also equals that same angle of C (Step 3). By CN1, since both the angle of A and the angle of B are equal to the same angle of C, the angle of A is equal to the corresponding angle of B. This holds for every pair of corresponding angles, so A and B have their angles severally equal.

**Step 5.** Now consider the sides about any pair of equal angles. From Step 2, the sides of A about an angle are proportional to the corresponding sides of C about the equal angle; that is, the ratio of a side of A to the corresponding side of C equals the ratio of another side of A about that angle to the corresponding side of C about that angle. From Step 3, the sides of B about the equal angle of C are likewise proportional to the sides of C; that is, the ratio of a side of C to the corresponding side of B equals the ratio of another side of C about that angle to the corresponding side of B about that angle.

**Step 6.** More precisely, let the sides about equal angles in A, C, and B be as follows. From the similarity of A to C: as side a1 of A is to the corresponding side c1 of C, so is side a2 of A to the corresponding side c2 of C. From the similarity of B to C: as side b1 of B is to the corresponding side c1 of C, so is side b2 of B to the corresponding side c2 of C. By 5.16 (inverse proportion), as c1 is to b1, so is c2 to b2.

**Step 7.** From Step 6 we have a1 : c1 :: a2 : c2 (from A similar to C) and c1 : b1 :: c2 : b2 (from B similar to C, inverted by 5.16). Applying 5.22 (ex aequali), since a1 : c1 :: a2 : c2 and c1 : b1 :: c2 : b2, we conclude a1 : b1 :: a2 : b2. Thus the sides of A about each angle are proportional to the corresponding sides of B about the equal angle.

**Step 8.** Since (by Step 4) the angles of A are severally equal to the corresponding angles of B, and (by Step 7) the sides about the equal angles are proportional, by Definition D6.1, figure A is similar to figure B.

**Step 9.** Therefore, figures which are similar to the same rectilineal figure are also similar to one another. Q.E.D.

**USED:** 5.16, 5.22, CN1, D6.1
**Human refs (from References field):** D6.1
**Jaccard:** 0.250 — AI adds ['5.16', '5.22', 'CN1']

## Proposition 6.22
**Statement:** If four straight lines be proportional, the rectilineal figures similar and similarly described upon them will also be proportional; and, if the rectilineal figures similar and similarly described upon them be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let AB, CD, EF, GH be four straight lines such that AB:CD :: EF:GH. Let P and Q be similar and similarly described rectilineal figures on AB and CD respectively, and let R and S be similar and similarly described rectilineal figures on EF and GH respectively. We must show P:Q :: R:S.

**Step 2.** By 6.11, find a third proportional M to AB and CD, so that AB:CD :: CD:M. Then AB has to M the duplicate ratio of that which AB has to CD [D5.9].

**Step 3.** Similarly, by 6.11, find a third proportional N to EF and GH, so that EF:GH :: GH:N. Then EF has to N the duplicate ratio of that which EF has to GH [D5.9].

**Step 4.** By 6.20, since P and Q are similar polygons described on AB and CD, P:Q is the duplicate ratio of AB to CD, that is, P:Q :: AB:M.

**Step 5.** By 6.20, since R and S are similar polygons described on EF and GH, R:S is the duplicate ratio of EF to GH, that is, R:S :: EF:N.

**Step 6.** Since AB:CD :: EF:GH (given), and AB:CD :: CD:M (Step 2), and EF:GH :: GH:N (Step 3), it follows that CD:M :: GH:N [5.11].

**Step 7.** From AB:CD :: EF:GH and CD:M :: GH:N, by the ex aequali rule [5.22], AB:M :: EF:N.

**Step 8.** Since P:Q :: AB:M (Step 4) and AB:M :: EF:N (Step 7) and EF:N :: R:S (Step 5), we conclude P:Q :: R:S [5.11]. This completes the first part of the proposition.

**Step 9.** Conversely, suppose P:Q :: R:S, where P, Q are similar and similarly described rectilineal figures on AB, CD, and R, S are similar and similarly described on EF, GH. We must show AB:CD :: EF:GH.

**Step 10.** By 6.12, find a line X such that AB:CD :: EF:X.

**Step 11.** By 6.18, on X describe a rectilineal figure T similar and similarly situated to S (and therefore also similar to R, since R and S are similar).

**Step 12.** Since AB:CD :: EF:X (Step 10), and P, Q are similar figures on AB, CD while R, T are similar figures on EF, X, by the first part of this proposition (Steps 1-8), P:Q :: R:T.

**Step 13.** But P:Q :: R:S (given). Therefore R:T :: R:S [5.11].

**Step 14.** Since R:T :: R:S, it follows that T = S [5.9].

**Step 15.** Since T and S are similar and similarly described rectilineal figures, and T = S (equal in area), and T is described on X while S is described on GH, we conclude X = GH. For if X were not equal to GH, then the similar figures described on them could not be equal, since by 6.20 similar polygons are in the duplicate ratio of corresponding sides, and unequal sides yield unequal duplicate ratios, hence unequal figures.

**Step 16.** Since X = GH and AB:CD :: EF:X (Step 10), we have AB:CD :: EF:GH [CN1]. This completes the converse, and the proposition is proved.

**USED:** 5.11, 5.22, 5.9, 6.11, 6.12, 6.18, 6.20, CN1, D5.9
**Human refs (from References field):** 5.11, 5.22, 5.9, 6.11, 6.12, 6.18, 6.19
**Jaccard:** 0.600 — AI adds ['6.20', 'CN1', 'D5.9']; Human adds ['6.19']

## Proposition 6.23
**Statement:** Equiangular parallelograms have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let ABCD and CEFG be two equiangular parallelograms, with angle BCD equal to angle GCE. We are to show that parallelogram ABCD has to parallelogram CEFG the ratio compounded of the ratios of their sides, namely the ratio compounded of BC to CG and DC to CE.

**Step 2.** Place the parallelograms so that BC is in a straight line with CG. Since angle BCD equals angle GCE, and angle BCD together with angle DCG equals two right angles (because BCG is a straight line, by 1.13), it follows that angle GCE together with angle DCG also equals two right angles. Therefore DC is in a straight line with CE, by 1.14.

**Step 3.** Through G draw GH parallel to DC (equivalently to CE) by 1.31, and complete the parallelogram DCGH. By P1 we join any required segments.

**Step 4.** Now the parallelograms ABCD and DCGH are under the same height (between the parallel lines BG and AD, HF extended), and share the base line BG. By 6.1, parallelogram ABCD is to parallelogram DCGH as the base BC is to the base CG.

**Step 5.** Similarly, the parallelograms DCGH and CEFG are under the same height (between the parallel lines DE and GF extended), and share the base line DE. By 6.1, parallelogram DCGH is to parallelogram CEFG as the base DC is to the base CE.

**Step 6.** Since ABCD : DCGH = BC : CG, and DCGH : CEFG = DC : CE, there are three magnitudes ABCD, DCGH, CEFG and three magnitudes BC, CG (with ratio BC:CG) and DC, CE (with ratio DC:CE) such that the ratio of the first to the third is compounded of the ratio of the first to the second and the ratio of the second to the third. By the definition of compounded ratio (D6.5) and by ex aequali (5.22), ABCD : CEFG is the ratio compounded of ABCD : DCGH and DCGH : CEFG, which is the ratio compounded of BC : CG and DC : CE.

**Step 7.** Therefore equiangular parallelograms have to one another the ratio compounded of the ratios of their sides. Q.E.F.

**USED:** 1.13, 1.14, 1.31, 1.34, 5.22, 6.1, D6.5, P1
**Human refs (from References field):** 5.11, 6.1, 6.12
**Jaccard:** 0.100 — AI adds ['1.13', '1.14', '1.31', '1.34', '5.22', 'D6.5', 'P1']; Human adds ['5.11', '6.12']

## Proposition 6.24
**Statement:** In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.

**Step 1.** Let ABCD be a parallelogram with diameter (diagonal) AC, and let AEFG and FHCK be parallelograms about the diameter, where E is on AB, G is on AD, K is on DC, H is on BC, and F is the point where the diameter AC passes through these inner parallelograms. We must show that AEFG and FHCK are each similar to ABCD, and hence similar to one another.

**Step 2.** Since ABCD is a parallelogram, AB is parallel to DC and AD is parallel to BC, and opposite sides are equal: AB = DC and AD = BC [1.34].

**Step 3.** Since AEFG is a parallelogram about the diameter AC, the diagonal AF of AEFG lies along AC. In parallelogram AEFG, EF is parallel to AG (which lies along AD), so EF is parallel to AD and hence parallel to BC. Likewise, GF is parallel to AE (which lies along AB), so GF is parallel to AB and hence parallel to DC.

**Step 4.** In triangle ABC, since EF is parallel to BC (established in Step 3), with E on AB and F on AC, by the property of a line drawn parallel to one side of a triangle, AE/AB = AF/AC [6.2].

**Step 5.** In triangle ACD, since GF is parallel to DC (established in Step 3), with G on AD and F on AC, by the same reasoning, AG/AD = AF/AC [6.2].

**Step 6.** Therefore AE/AB = AG/AD, since both equal AF/AC [CN1].

**Step 7.** Now consider the angles. The angle GAE in parallelogram AEFG is the same angle as angle DAB in parallelogram ABCD, since E lies on AB and G lies on AD. So angle GAE equals angle DAB.

**Step 8.** Since AEFG is a parallelogram, angle AEF is supplementary to angle GAE, meaning angle GAE + angle AEF equals two right angles [1.34, 1.29]. Similarly in parallelogram ABCD, angle DAB + angle ABC equals two right angles [1.34, 1.29]. Since angle GAE = angle DAB, it follows that angle AEF = angle ABC.

**Step 9.** By 1.34, the opposite angles in each parallelogram are equal: in AEFG, angle EFG = angle GAE and angle FGA = angle AEF; in ABCD, angle BCD = angle DAB and angle CDA = angle ABC. Therefore all four angles of AEFG are severally equal to the corresponding four angles of ABCD.

**Step 10.** In parallelogram AEFG, EF = AG and GF = AE [1.34]. In parallelogram ABCD, BC = AD and DC = AB [1.34]. From Step 6, AE/AB = AG/AD. Therefore GF/DC = AE/AB = AG/AD = EF/BC. Thus the sides about the equal angles are proportional.

**Step 11.** Since AEFG and ABCD are equiangular (Step 9) and have the sides about the equal angles proportional (Step 10), AEFG is similar to ABCD [D6.1].

**Step 12.** Now consider parallelogram FHCK about the diameter. The diagonal FC of FHCK lies along AC. In parallelogram FHCK, FH is parallel to CK (which lies along DC), so FH is parallel to DC and hence parallel to AB. Likewise, FK is parallel to HC (which lies along BC), so FK is parallel to BC and hence parallel to AD.

**Step 13.** In triangle ABC, since FH is parallel to AB (established in Step 12), with F on AC and H on BC, we have CF/CA = CH/CB [6.2].

**Step 14.** In triangle ACD, since FK is parallel to AD (established in Step 12), with F on AC and K on CD, we have CF/CA = CK/CD [6.2].

**Step 15.** Therefore CH/CB = CK/CD, since both equal CF/CA [CN1].

**Step 16.** The angle KCH in parallelogram FHCK is the same angle as angle DCB in parallelogram ABCD, since K lies on DC and H lies on BC. So angle KCH equals angle DCB.

**Step 17.** Since FHCK is a parallelogram, angle KCH + angle CHF equals two right angles [1.34, 1.29]. In parallelogram ABCD, angle DCB + angle CBA equals two right angles [1.34, 1.29]. Since angle KCH = angle DCB, it follows that angle CHF = angle CBA. By 1.34, the opposite angles in each parallelogram are equal, so all four angles of FHCK are severally equal to the corresponding four angles of ABCD.

**Step 18.** In parallelogram FHCK, FH = CK and FK = CH [1.34]. From Step 15, CK/CD = CH/CB. Therefore FH/DC = CK/CD = CH/CB = FK/AD. Since DC = AB and AD = BC [1.34], we also have FH/AB = FK/BC. Thus the sides about the equal angles are proportional.

**Step 19.** Since FHCK and ABCD are equiangular (Step 17) and have the sides about the equal angles proportional (Step 18), FHCK is similar to ABCD [D6.1].

**Step 20.** Since AEFG is similar to ABCD (Step 11) and FHCK is similar to ABCD (Step 19), AEFG is similar to FHCK [6.21].

**Step 21.** Therefore, in any parallelogram, the parallelograms about the diameter are similar both to the whole and to one another. Q.E.D.

**USED:** 1.29, 1.34, 6.2, 6.21, CN1, D6.1
**Human refs (from References field):** 5.16, 5.18, 5.22, 6.2, 6.21, D6.1
**Jaccard:** 0.333 — AI adds ['1.29', '1.34', 'CN1']; Human adds ['5.16', '5.18', '5.22']

## Proposition 6.25
**Statement:** To construct one and the same figure similar to a given rectilineal figure and equal to another given rectilineal figure.

**Step 1.** Let ABC be the given rectilineal figure to which the constructed figure must be similar, and let D be the given rectilineal figure to which the constructed figure must be equal in area.

**Step 2.** On the straight line BC, apply the parallelogram BE equal to the rectilineal figure ABC [1.45], and on the straight line CE, apply the parallelogram CM equal to D in the angle FCE equal to the angle CBL [1.45]. Then BC and CF are in a straight line, and LE and EM are in a straight line.

**Step 3.** Find GH a mean proportional between BC and CF [6.13], so that BC : GH = GH : CF.

**Step 4.** On GH describe the rectilineal figure KGH similar and similarly situated to the rectilineal figure ABC [6.18], so that BC corresponds to GH.

**Step 5.** Since BC : GH = GH : CF, it follows that BC : CF is the duplicate ratio of BC : GH [D5.9].

**Step 6.** Since ABC and KGH are similar rectilineal figures, and BC and GH are corresponding sides, the ratio ABC : KGH is the duplicate ratio of BC : GH [6.20].

**Step 7.** Therefore ABC : KGH = BC : CF [Steps 5 and 6; CN1].

**Step 8.** Since BE and CM are parallelograms on the bases BC and CF respectively, and they are between the same parallels (that is, they have the same height), BE : CM = BC : CF [6.1].

**Step 9.** But BE equals the rectilineal figure ABC, and CM equals D, by construction. Therefore ABC : D = BC : CF.

**Step 10.** From Steps 7 and 9, ABC : KGH = ABC : D [CN1].

**Step 11.** Therefore KGH equals D [5.9].

**Step 12.** And KGH is similar to ABC by construction [Step 4].

**Step 13.** Therefore KGH is the required rectilineal figure: it is similar to the given figure ABC and equal to the given figure D. Q.E.F.

**USED:** 1.45, 5.9, 6.1, 6.13, 6.18, 6.20, CN1, D5.9, D6.1
**Human refs (from References field):** 1.44, 1.45, 5.16, 6.1, 6.13, 6.18, 6.19
**Jaccard:** 0.333 — AI adds ['5.9', '6.20', 'CN1', 'D5.9', 'D6.1']; Human adds ['1.44', '5.16', '6.19']

## Proposition 6.26
**Statement:** If from a parallelogram there be taken away a parallelogram similar and similarly situated to the whole and having a common angle with it, it is about the same diameter with the whole.

**Step 1.** Let ABCD be a parallelogram, and let AEFG be a parallelogram taken away from it, similar and similarly situated to the whole ABCD, and having angle GAE common with angle DAB. We must prove that AEFG is about the same diameter with ABCD.

**Step 2.** Suppose, for the sake of contradiction, that AEFG is not about the same diameter with ABCD. Let AHC be a diameter of ABCD, and suppose this diameter does not pass through the vertex of AEFG opposite to A (that is, through the point where EF and GF meet).

**Step 3.** Draw the diameter AHC of parallelogram ABCD [P1]. Since the diameter AHC does not pass through the corner of AEFG opposite to A, let the diameter AHC intersect side EF (or EF produced) at some point K, and intersect side GF (or GF produced) at some point H.

**Step 4.** Through K, draw KL parallel to AD meeting the diameter and sides of ABCD, and through H, draw HM parallel to AB meeting the diameter and sides of ABCD, so that AKHM is a parallelogram about the diameter AHC of ABCD [1.31].

**Step 5.** Since AKHM is a parallelogram about the diameter of ABCD, by Proposition 6.24, AKHM is similar and similarly situated to ABCD [6.24].

**Step 6.** But AEFG is also similar and similarly situated to ABCD, by hypothesis.

**Step 7.** Since both AKHM and AEFG are similar to ABCD, by Proposition 6.21, AKHM is similar to AEFG [6.21].

**Step 8.** Since AEFG and AKHM are similar and similarly situated parallelograms sharing the common angle at A, and they are similar to each other, the sides about the common angle A must be proportional. That is, AE is to AK as AG is to AH [D6.1].

**Step 9.** Since AKHM is similar to AEFG, and they share angle A and are similarly situated, we have AK : AE = AH : AG (the sides about the equal angle at A are proportional) [D6.1].

**Step 10.** But AKHM contains AEFG (or AEFG contains AKHM) since they share vertex A and lie within ABCD. In either case, suppose AK is not equal to AE. If AK is less than AE, then since AK : AE = AH : AG, we would have AH less than AG [5.14]. But then AKHM would be contained within AEFG. Conversely, if AK is greater than AE, then AH is greater than AG, and AEFG would be contained within AKHM.

**Step 11.** Consider the case where AK is not equal to AE. From the proportion AK : AE = AH : AG, by Proposition 5.9 (and properties of proportions), AK and AE are in a definite ratio. Since AKHM is similar to AEFG, the ratio AK : AH equals AE : AG [D6.1]. Therefore AK : AE = AH : AG [5.16].

**Step 12.** Now since both parallelograms share side directions from A and are similarly situated, one must contain the other. Suppose AK is not equal to AE. Then the side AK is either greater or less than AE. But since AK : AH = AE : AG (from similarity of AKHM and AEFG), if AK > AE then AH > AG, meaning AEFG lies entirely inside AKHM. In this case AEFG is a part of AKHM, so AEFG is less than AKHM [CN5].

**Step 13.** But since AKHM is similar to AEFG, the ratio of their areas is the duplicate ratio of corresponding sides [6.20]. Specifically, AKHM : AEFG is the duplicate ratio of AK : AE. Since AEFG is part of AKHM, AKHM is greater than AEFG, so AK is greater than AE.

**Step 14.** However, from the similar positioning, AE lies along AB and AK also lies along AB (since K is on EF, and the diameter meets EF at K, while EF is parallel to AB or to a side). In fact, since both AEFG and AKHM share the angle at A and are similarly situated to ABCD, the sides AE and AK both lie along the same ray from A (along AB), and AG, AH both lie along the same ray from A (along AD).

**Step 15.** From the proportion AE : AG = AK : AH (both ratios equal to the ratio of corresponding sides of ABCD, since both parallelograms are similar to ABCD), we get AE : AK = AG : AH [5.16]. If AK is not equal to AE, say AK > AE, then AG < AH cannot hold simultaneously with the required similarity, because from ABCD's own side ratio AB : AD, we need AE : AG = AK : AH = AB : AD. This gives AE/AK = AG/AH. But if AK > AE, then AE/AK < 1, so AG/AH < 1, meaning AG < AH.

**Step 16.** Now the point K lies on the diameter AHC and on line EF. The point H lies on the diameter and on line GF. Since AEFG has its opposite vertex (the intersection of EF and GF) not on the diameter by our assumption, we have constructed a different parallelogram AKHM about the diameter. But AKHM is similar to AEFG with AK along the same line as AE and AH along the same line as AG, with AE : AG = AK : AH. This means AE/AK = AG/AH, call this ratio r. If r is not equal to 1, then AEFG is a scaled version of AKHM from vertex A.

**Step 17.** Since AEFG is similar to ABCD and AKHM is similar to ABCD, and both share angle A with sides along the same directions, the ratio AE : AB = AG : AD and AK : AB = AH : AD [D6.1]. From these: AE : AK = (AE/AB) / (AK/AB) = (AG/AD) / (AH/AD) = AG : AH. So AE * AH = AK * AG [6.16].

**Step 18.** But also, since AEFG is similar to AKHM (both being similar to ABCD), AE : AK = AG : AH [D6.1, 6.21]. This means AE * AH = AG * AK [6.16], confirming the relationship. Now if AK is not equal to AE, the parallelogram AKHM is distinct from AEFG. Since they share vertex A and lie along the same directions, one contains the other strictly, making the contained one a proper part of the other [CN5].

**Step 19.** Since AEFG is similar to AKHM with ratio of similarity r (where r is not 1), AEFG has area r^2 times the area of AKHM [6.20]. But if AEFG is a proper part of AKHM (when r < 1), the area ratio would be less than 1, consistent with r < 1. However, in the original construction, both AEFG and AKHM are sub-parallelograms of ABCD about the same vertex A.

**Step 20.** The key contradiction arises as follows. Since AKHM is about the diameter of ABCD, by 6.24 it is the unique parallelogram about that diameter at vertex A that is similar to ABCD. Since AEFG is also similar to ABCD and similarly situated at vertex A, if AEFG is not about the same diameter, then AEFG is different from AKHM. But then one contains the other as a proper part while both are similar to each other, which means the part is similar to the whole. The ratio of similarity gives AE : AK = AG : AH with the ratio not equal to 1.

**Step 21.** From AEFG similar to ABCD: AE : AG = AB : AD. From AKHM similar to ABCD: AK : AH = AB : AD. Therefore AE : AG = AK : AH [CN1, 5.11]. Since E lies on AB and K lies on AB (between A and E, or between E and B), and G lies on AD and H lies on AD, we have both AE : AG and AK : AH equal to the same ratio AB : AD.

**Step 22.** From AE : AG = AK : AH, alternating gives AE : AK = AG : AH [5.16]. Suppose AE is not equal to AK. Then the ratio AE : AK is not 1 : 1. But since E is on segment AB and K is also on segment AB (as K lies on line EF, which is parallel to AD and meets the diagonal), we have two distinct points E and K on AB, with AE and AK being different lengths.

**Step 23.** Since AEFG is similar to ABCD, by D6.1, all corresponding angles are equal and sides are proportional. Similarly for AKHM. The angle at A is the same for both. The sides from A lie along AB and AD respectively. With AE : AG = AK : AH, and AE distinct from AK, the point F (intersection of the line through E parallel to AD and the line through G parallel to AB) is distinct from the point determined by K and H. But AKHM is about the diameter, meaning its opposite vertex lies on AHC.

**Step 24.** For AEFG not to be about the diameter means the opposite vertex of AEFG does not lie on diagonal AC. Yet AEFG is similar and similarly situated to ABCD with the same angle at A. By the construction in Step 4, AKHM is the unique such parallelogram about the diameter. Since AEFG is similar to ABCD and similarly situated, and AKHM is the unique such parallelogram about the diameter that is similar to ABCD, if AEFG is different from AKHM, then one is a proper part of the other.

**Step 25.** If AEFG is a proper part of AKHM (AE < AK), then since AEFG is similar to AKHM, the area of AEFG is less than the area of AKHM. But AEFG has sides AE and AG, while AKHM has sides AK and AH, with AE < AK and AG < AH. The parallelogram AEFG lies entirely within AKHM. Now the complement of AEFG within AKHM is a gnomon, which has positive area. But this contradicts nothing yet directly.

**Step 26.** The contradiction is obtained as follows. Since AE : AG = AK : AH = AB : AD, and AE is not equal to AK, let AE < AK (the case AE > AK is symmetric). Then AG < AH. Point E lies between A and K on line AB, and point G lies between A and H on line AD. Draw EF parallel to AD and GF parallel to AB so that F is the vertex of AEFG opposite A. Since AKHM is about the diameter AC, the diagonal AC passes through the vertex M of AKHM (the point opposite A). The line EF is parallel to AD and the line through K parallel to AD is the same line (both pass through points on AB at distance AE and AK respectively from A, both parallel to AD). But AE < AK, so EF and the line through K are different parallel lines. The diagonal AC crosses the line through K (at M, since AKHM is about the diameter), but AC also must cross EF at some point since it goes from A to C.

**Step 27.** Let the diagonal AC meet EF at point N. Then N lies on EF between E and F (or on EF produced). Consider the parallelogram AENG', where G' is on AD such that this parallelogram is about the diameter. By 6.24, this parallelogram is similar to ABCD. Its side along AB is AE, and by similarity to ABCD, AE : AG' = AB : AD. But from AEFG similar to ABCD, AE : AG = AB : AD. Therefore AG' = AG [5.9, 5.11]. This means G' coincides with G, and N lies on line GF (since the parallelogram about the diameter with side AE along AB has its opposite vertex on the diagonal, and its side along AD is AG = AG').

**Step 28.** Therefore the opposite vertex of the parallelogram with sides AE and AG that is similar to ABCD and about the diameter must have its opposite vertex at F, where EF meets GF. This means F lies on the diagonal AC. But this contradicts our assumption that AEFG is not about the diameter of ABCD.

**Step 29.** The case AE > AK leads to the same contradiction by symmetric reasoning.

**Step 30.** Therefore the assumption that AEFG is not about the same diameter as ABCD is false. Hence AEFG is about the same diameter with ABCD. Q.E.D.

**USED:** 1.31, 5.11, 5.16, 5.9, 6.16, 6.20, 6.21, 6.24, CN1, CN5, D6.1, P1
**Human refs (from References field):** 1.31, 5.11, 5.9, 6.24
**Jaccard:** 0.333 — AI adds ['5.16', '6.16', '6.20', '6.21', 'CN1', 'CN5', 'D6.1', 'P1']

## Proposition 6.27
**Statement:** Of all the parallelograms applied to the same straight line and deficient by parallelogrammic figures similar and similarly situated to that described on the half of the straight line, that parallelogram is greatest which is applied to the half of the straight line and is similar to the defect.

**Step 1.** Let AB be a given straight line, bisected at the point C [1.10]. On CB describe a parallelogrammic figure CF. Complete the whole parallelogram on AB by extending CF to form the parallelogram AO on AB, with CF about the diameter. Then the complement AD (the parallelogram applied to AC, the half of AB) has CF as its defect. We claim AD is the greatest of all parallelograms applied to AB and deficient by figures similar and similarly situated to CF.

**Step 2.** Let there be applied to AB any other parallelogram AG, on a segment AE (where E is on AB and E differs from C), deficient by a parallelogrammic figure EG that is similar and similarly situated to CF [D6.1].

**Step 3.** Since EG is similar and similarly situated to CF and they share a common angle (at B), by Proposition 6.26, the parallelogram EG is about the same diameter as CF. Let the common diameter be drawn; call it DB.

**Step 4.** In the whole parallelogram on AB with diameter DB, both CF (on CB) and EG (on EB) are parallelograms about the diameter. The complement AD corresponds to CF, and the complement AG corresponds to EG, where by 1.43 each complement equals the complement on the opposite side of its respective parallelogram about the diameter.

**Step 5.** Since C is the midpoint of AB and E is different from C, we have EB not equal to CB. Therefore EG, being similar and similarly situated to CF but described on a different segment, is not equal to CF. One of these parallelograms about the diameter properly contains the other.

**Step 6.** If E lies between A and C, then EB > CB, so EG (on EB) properly contains CF (on CB), since both are about the same diameter and EG extends further along the diameter. In this case, EG consists of CF together with the gnomon-shaped region that is the difference EG minus CF. The complement AG together with this gnomon equals the complement AD: for the whole parallelogram decomposes into the parallelograms about the diameter and the two complements, and replacing CF by the larger EG forces the complement to shrink from AD to AG by exactly the gnomon.

**Step 7.** If E lies between C and B, then EB < CB, so CF properly contains EG. In this case, CF consists of EG together with the gnomon-shaped region that is the difference CF minus EG. The complement AD consists of the complement AG together with this gnomon: for replacing EG by the larger CF as the parallelogram about the diameter, the complement grows from AG to AD by exactly the gnomon.

**Step 8.** In both cases, the complement AD equals the complement AG plus a gnomon (a positive region). By CN5 (the whole is greater than the part), AD is greater than AG.

**Step 9.** Since AG was an arbitrary parallelogram applied to AB and deficient by a parallelogrammic figure similar and similarly situated to CF, the parallelogram AD applied to the half AC is the greatest of all such parallelograms.

**Step 10.** Therefore, of all the parallelograms applied to the same straight line and deficient by parallelogrammic figures similar and similarly situated to that described on the half of the straight line, that parallelogram is greatest which is applied to the half of the straight line and is similar to the defect. Q.E.D.

**USED:** 1.10, 1.43, 6.26, CN5, D6.1
**Human refs (from References field):** 1.36, 1.43, 6.26
**Jaccard:** 0.333 — AI adds ['1.10', 'CN5', 'D6.1']; Human adds ['1.36']

## Proposition 6.28
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and deficient by a parallelogrammic figure similar to a given one: thus the given rectilineal figure must not be greater than the parallelogram described on the half of the straight line and similar to the defect.

**Step 1.** Let AB be the given straight line, C the given rectilineal figure to which the applied parallelogram must be equal, and D the given parallelogrammic figure to which the defect must be similar. It is required to apply to AB a parallelogram equal to C and deficient by a parallelogram similar to D. The given figure C is assumed not greater than the parallelogram described on the half of AB and similar to D.

**Step 2.** Bisect AB at E [1.10]. On EB, describe the parallelogram EBFG similar and similarly situated to D [6.18]. Then EBFG is the parallelogram described on the half of AB and similar to D.

**Step 3.** If EBFG is equal to C, then EBFG has been applied to the straight line AB equal to C and deficient by the parallelogram EBFG which is similar to D, and the construction is done.

**Step 4.** If not, then EBFG is greater than C (since C is not greater than EBFG by hypothesis, and they are not equal). Let EBFG exceed C by the rectilineal figure K, so that EBFG equals C together with K [CN3].

**Step 5.** Construct a parallelogram LMNO equal to K and similar and similarly situated to D [6.25]. Since EBFG is similar to D [by construction], and LMNO is similar to D [by construction], therefore LMNO is similar to EBFG [6.21].

**Step 6.** Since LMNO is similar to EBFG and LMNO equals K which is less than EBFG, LMNO is less than EBFG. Let LMNO be so placed that the parallelogram LMNO is similar and similarly situated to EBFG, sharing the angle at B (that is, placed at the corner corresponding to angle EBG). Since LMNO and EBFG are similar and LMNO is less than EBFG, with LMNO placed about the same angle, LMNO lies within EBFG and is about the same diameter [6.26].

**Step 7.** Let GEB be the diameter of EBFG, and let the same line be the diameter of LMNO. Complete the figure. Let GEB be the diameter and let the parallelogram LMNO be placed so that its sides lie along the sides of EBFG emanating from B. Denote the configuration so that EBFG is divided by LMNO into the smaller parallelogram LMNO (about the diameter), and two complements.

**Step 8.** Since the parallelogram EBFG equals C together with K [Step 4], and LMNO equals K [Step 5], subtracting LMNO from EBFG and K from (C + K), the gnomon (that is, the remainder EBFG minus LMNO) equals C [CN3].

**Step 9.** Now, since AE equals EB [Step 2, bisection], the parallelogram AN (the parallelogram applied to AE sharing a side with the complement along the diameter) equals the complement on the other side of the diameter by the property that in any parallelogram the complements about the diameter are equal [1.43].

**Step 10.** The gnomon of EBFG about LMNO consists of the two complements and the parallelogram LMNO is excluded. The complement on the side of AE together with the complement on the side of EB makes up the gnomon. By the equality of complements about the diameter of the larger parallelogram constructed on AB [1.43], and the relationship between the pieces, the gnomon equals the parallelogram applied to AB deficient by the parallelogram similar to D at the end.

**Step 11.** More precisely, extend the construction to the full line AB. Since AE = EB, construct on AB the full parallelogram ABFP (extending EBFG to the full line). The parallelogram about the diameter on the AE side is the complement, and it equals the complement on the EB side [1.43]. The parallelogram applied to AB is the figure on the AE side together with the complement, which equals the gnomon, which equals C [Step 8].

**Step 12.** The defect (the part by which the applied parallelogram falls short of the parallelogram on the whole line AB) is the parallelogram remaining at the end, which is similar to LMNO and hence similar to D [6.24], since parallelograms about the diameter of a parallelogram are similar to the whole and to one another.

**Step 13.** Therefore, to the given straight line AB there has been applied the parallelogram (the gnomon region) equal to the given rectilineal figure C, deficient by a parallelogrammic figure similar to the given parallelogram D. Q.E.F.

**USED:** 1.10, 1.43, 6.18, 6.21, 6.24, 6.25, 6.26, CN3
**Human refs (from References field):** 1.36, 6.18, 6.21, 6.25, 6.26
**Jaccard:** 0.444 — AI adds ['1.10', '1.43', '6.24', 'CN3']; Human adds ['1.36']

## Proposition 6.29
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and exceeding by a parallelogrammic figure similar to a given one.

**Step 1.** Let AB be the given straight line, C the given rectilineal figure, and D the given parallelogram to which the excess is to be similar. It is required to apply to AB a parallelogram equal to C and exceeding by a parallelogrammic figure similar to D.

**Step 2.** Bisect AB at E [1.10].

**Step 3.** On EB, describe the parallelogram BFGE similar and similarly situated to D [6.18]. Let BFGE be the parallelogram on EB similar to D, where GE is along EB.

**Step 4.** Construct a parallelogram KH equal to the sum of BFGE and C, and similar and similarly situated to D [6.25]. This is possible because 6.25 constructs a figure similar to one given figure and equal in area to another; here we need KH similar to D and equal to BFGE + C. (We first construct a parallelogram equal to BFGE + C by 1.45, then apply 6.25 to obtain KH similar to D and equal to that sum.)

**Step 5.** Since KH is similar to D and BFGE is similar to D, KH is similar to BFGE [6.21].

**Step 6.** Since KH equals BFGE + C, and C is a positive area, KH is greater than BFGE [CN5]. Because KH and BFGE are similar parallelograms and KH is greater, each side of KH is greater than the corresponding side of BFGE.

**Step 7.** Let GE and GF be the sides of parallelogram BFGE meeting at G. Since KH is similar to BFGE, let the sides of KH corresponding to GE and GF be greater. Produce GE to L and GF to M so that GL equals the side of KH corresponding to GE, and GM equals the side of KH corresponding to GF. Complete the parallelogram GLMN on sides GL and GM, similar and similarly situated to D [P1, P2]. Then GLMN is equal and similar to KH, since the corresponding sides are equal and the angles are equal (both being similar to D) [6.24, D6.1].

**Step 8.** Since GLMN is similar to BFGE, and BFGE is about the diameter of GLMN, the parallelogram BFGE is about the same diameter as GLMN [6.26]. Let that diameter be GB (extended to the opposite corner of GLMN).

**Step 9.** Since BFGE is a parallelogram about the diameter of GLMN, the gnomon composed of the remaining pieces of GLMN (that is, GLMN minus BFGE) equals the complement areas. Specifically, the gnomon equals GLMN minus BFGE [CN3]. But GLMN equals KH (Step 7), and KH equals BFGE + C (Step 4). Therefore the gnomon equals (BFGE + C) minus BFGE, which equals C [CN3].

**Step 10.** Now, since AE equals EB (Step 2), and BFGE is built on EB, consider the full figure. The parallelogram applied to the whole line AB in the same angular orientation is composed of the parallelogram on AE (which is the complement to BFGE about the diameter) together with BFGE and the remaining parts of GLMN. More precisely, since AE = EB and EG is a side of the parallelogram BFGE, produce the construction so that the parallelogram on the whole line AB (in the direction of GF) is the parallelogram AEMF (where M lies on GF produced). The gnomon — the region GLMN minus BFGE — can be rearranged as the parallelogram applied to AB. Specifically, the parallelogram applied to AB equals the gnomon [1.43, 1.36], which equals C (Step 9).

**Step 11.** The excess by which this applied parallelogram exceeds the line AB is the parallelogram on the extension of AB beyond B, which is part of GLMN. Since GLMN is similar to D [6.24], and the excess parallelogram is similar to the whole GLMN (being a parallelogram about the diameter of GLMN) [6.24], the excess is similar to D.

**Step 12.** Therefore, to the given straight line AB, a parallelogram has been applied equal to the given rectilineal figure C and exceeding by a parallelogrammic figure similar to the given parallelogram D. This is what was required to be done.

**USED:** 1.10, 1.36, 1.43, 1.45, 6.18, 6.21, 6.24, 6.25, 6.26, CN3, CN5, D6.1, P1, P2
**Human refs (from References field):** 1.36, 1.43, 6.21, 6.24, 6.25, 6.26
**Jaccard:** 0.429 — AI adds ['1.10', '1.45', '6.18', 'CN3', 'CN5', 'D6.1', 'P1', 'P2']

## Proposition 6.30
**Statement:** To cut a given finite straight line in extreme and mean ratio.

**Step 1.** Let AB be the given finite straight line. It is required to cut AB in extreme and mean ratio (D6.3).

**Step 2.** By Proposition 2.11, cut AB at a point C such that the rectangle contained by AB and CB is equal to the square on AC. That is, rect(AB, CB) = sq(AC).

**Step 3.** Since rect(AB, CB) = sq(AC), and AB, AC, CB are three straight lines such that the rectangle contained by the first (AB) and the third (CB) equals the square on the second (AC), by Proposition 6.17 (converse part: if the rectangle contained by the extremes is equal to the square on the mean, the three straight lines are proportional), we conclude that AB : AC = AC : CB.

**Step 4.** Since AB : AC = AC : CB, the whole line AB is to the greater segment AC as the greater segment AC is to the lesser segment CB. Therefore, by Definition D6.3, the straight line AB has been cut in extreme and mean ratio at C.

**Step 5.** Therefore, the given finite straight line AB has been cut in extreme and mean ratio, which is what was required to do. Q.E.F.

**USED:** 2.11, 6.17, D6.3
**Human refs (from References field):** 6.14, 6.29
**Jaccard:** 0.000 — AI adds ['2.11', '6.17', 'D6.3']; Human adds ['6.14', '6.29']

## Proposition 6.31
**Statement:** In right - angled triangles the figure on the side subtending the right angle is equal to the similar and similarly described figures on the sides containing the right angle.

**Step 1.** Let triangle ABC have a right angle at vertex A, with BC the side subtending the right angle (the hypotenuse). Let similar and similarly described rectilineal figures be constructed on BC, BA, and CA; call them F_BC, F_BA, and F_CA respectively. We are to prove that F_BC = F_BA + F_CA.

**Step 2.** From the right angle at A, draw AD perpendicular to BC. By 6.8, since triangle ABC is right-angled at A and AD is drawn from the right angle perpendicular to the base BC, the triangles ABD and ABC are similar, and likewise triangles ADC and ABC are similar.

**Step 3.** Since triangle ABD is similar to triangle ABC (by Step 2), corresponding sides are proportional (by 6.4), and in particular BC : BA = BA : BD. That is, BA is a mean proportional between BC and BD.

**Step 4.** Since BC : BA = BA : BD, three magnitudes BC, BA, BD are in continued proportion. Therefore, by D5.9, BC has to BD the duplicate ratio of that which BC has to BA.

**Step 5.** Since triangle ADC is similar to triangle ABC (by Step 2), corresponding sides are proportional (by 6.4), and in particular BC : CA = CA : DC. That is, CA is a mean proportional between BC and DC.

**Step 6.** Since BC : CA = CA : DC, three magnitudes BC, CA, DC are in continued proportion. Therefore, by D5.9, BC has to DC the duplicate ratio of that which BC has to CA.

**Step 7.** Now F_BC and F_BA are similar rectilineal figures described on BC and BA respectively. By 6.20, similar polygons have to one another the ratio duplicate of that which corresponding sides have to corresponding sides. Therefore F_BC : F_BA is the duplicate ratio of BC : BA.

**Step 8.** But from Step 4, BC : BD is also the duplicate ratio of BC : BA. Since two ratios that are each the duplicate of the same ratio are the same ratio, we conclude F_BC : F_BA = BC : BD.

**Step 9.** By 5.7 (invertendo), since F_BC : F_BA = BC : BD, we have F_BA : F_BC = BD : BC.

**Step 10.** Similarly, F_BC and F_CA are similar rectilineal figures described on BC and CA respectively. By 6.20, F_BC : F_CA is the duplicate ratio of BC : CA.

**Step 11.** From Step 6, BC : DC is also the duplicate ratio of BC : CA. Therefore F_BC : F_CA = BC : DC.

**Step 12.** By 5.7 (invertendo), since F_BC : F_CA = BC : DC, we have F_CA : F_BC = DC : BC.

**Step 13.** We now have F_BA : F_BC = BD : BC (Step 9) and F_CA : F_BC = DC : BC (Step 12). By 5.24, the sum of the antecedents has to the common consequent the same ratio as the sum of the corresponding antecedents to their common consequent. That is, (F_BA + F_CA) : F_BC = (BD + DC) : BC.

**Step 14.** But D is a point on BC between B and C (being the foot of the perpendicular from A), so BD + DC = BC. Therefore (BD + DC) : BC = BC : BC.

**Step 15.** Thus (F_BA + F_CA) : F_BC = BC : BC. By 5.9, if two magnitudes have the same ratio to the same magnitude, they are equal to one another. Therefore F_BA + F_CA = F_BC.

**Step 16.** Hence, in the right-angled triangle ABC, the figure on the hypotenuse BC is equal to the sum of the similar and similarly described figures on the two sides BA and CA containing the right angle. Q.E.D.

**USED:** 5.24, 5.7, 5.9, 6.20, 6.4, 6.8, D5.9
**Human refs (from References field):** 6.19, 6.8, D6.1
**Jaccard:** 0.111 — AI adds ['5.24', '5.7', '5.9', '6.20', '6.4', 'D5.9']; Human adds ['6.19', 'D6.1']

## Proposition 6.32
**Statement:** If two triangles having two sides proportional to two sides be placed together at one angle so that their corresponding sides are also parallel, the remaining sides of the triangles will be in a straight line.

**Step 1.** Let ABC and DCE be two triangles placed together at angle C, such that BC/CE = AB/DE (two sides proportional to two sides), with BC parallel to CE (so that B, C, E are collinear) and AB parallel to DE (corresponding sides parallel), and with A and D on opposite sides of line BE.

**Step 2.** Since AB is parallel to DE, and line BE is a transversal cutting these parallel lines, the alternate interior angles are equal: angle ABC = angle CED. [1.29]

**Step 3.** In triangles ABC and DCE, we have angle ABC = angle CED (Step 2), and the sides about these equal angles are proportional: BA/ED = BC/EC (given). Therefore, by Proposition 6.6, triangles ABC and DCE are equiangular. In particular, the angles at C correspond: angle BCA = angle DCE. [6.6]

**Step 4.** Since B, C, E are collinear and the straight line CA meets line BE at C, the angles on one side of CA at point C are supplementary: angle BCA + angle ACE equals two right angles. [1.13]

**Step 5.** Since angle BCA = angle DCE (Step 3), we may substitute: angle DCE + angle ACE equals two right angles. [CN1]

**Step 6.** At point C on line BE, the two straight lines CA and CD lie on opposite sides of BE, and the adjacent angles they make with BE satisfy angle ACE + angle DCE = two right angles (Step 5). Therefore, by Proposition 1.14, CA and CD are in a straight line. [1.14]

Therefore, the remaining sides CA and CD of the two triangles are in a straight line, which is what was to be proved.

**USED:** 1.13, 1.14, 1.29, 6.6, CN1
**Human refs (from References field):** 1.14, 1.29, 1.32, 6.6
**Jaccard:** 0.500 — AI adds ['1.13', 'CN1']; Human adds ['1.32']

## Proposition 6.33
**Statement:** In equal circles angles have the same ratio as the circumferences on which they stand, whether they stand at the centres or at the circumferences.

**Step 1.** Let there be equal circles with centres G and H respectively. Let angle BGC be a central angle in the first circle standing on circumference BC, and let angle EHF be a central angle in the second circle standing on circumference EF. We must show that angle BGC is to angle EHF as circumference BC is to circumference EF.

**Step 2.** Take any integer m. Starting from ray GB at centre G, lay off m consecutive angles each equal to angle BGC around the centre, producing rays GB, GC1, GC2, ..., GCm where C1 = C and each angle GCi to GC(i+1) equals angle BGC. This partitions the arc from B to Cm into m consecutive arcs. By Proposition 3.26, in equal circles equal central angles stand on equal circumferences, so each of these m arcs equals circumference BC. Therefore the total arc from B to Cm equals m times circumference BC, and the total angle at G equals m times angle BGC.

**Step 3.** Similarly, take any integer n and lay off n consecutive angles each equal to angle EHF at centre H, producing a total angle of n times angle EHF standing on a total circumference equal to n times circumference EF, again by Proposition 3.26.

**Step 4.** Now we apply the equimultiple criterion for proportion (Definition 5.5). We must show that for all positive integers m and n: m times angle BGC is greater than, equal to, or less than n times angle EHF according as m times circumference BC is greater than, equal to, or less than n times circumference EF.

**Step 5.** Suppose m times angle BGC equals n times angle EHF. These are central angles in equal circles, and since they are equal, by Proposition 3.26 they stand on equal circumferences. Therefore m times circumference BC equals n times circumference EF.

**Step 6.** Suppose m times angle BGC is greater than n times angle EHF. By Proposition 1.23, we can construct at centre G an angle equal to n times angle EHF within the angle of m times angle BGC. This constructed angle, being equal to n times angle EHF, stands on a circumference equal to n times circumference EF, by Propositions 3.26 and 3.27 (in equal circles, equal central angles stand on equal circumferences, and angles standing on equal circumferences are equal). Since m times angle BGC is greater than this constructed angle, the circumference on which m times angle BGC stands, namely m times circumference BC, is greater than the circumference on which the constructed angle stands, namely n times circumference EF. Therefore m times circumference BC is greater than n times circumference EF.

**Step 7.** Similarly, if m times angle BGC is less than n times angle EHF, then by the same reasoning (applying 3.26 and 3.27 with the roles exchanged), m times circumference BC is less than n times circumference EF.

**Step 8.** Since for all positive integers m and n, the m-fold of angle BGC and the m-fold of circumference BC simultaneously exceed, equal, or fall short of the n-fold of angle EHF and the n-fold of circumference EF respectively, by Definition 5.5 we conclude that angle BGC is to angle EHF as circumference BC is to circumference EF.

**Step 9.** Now consider angles at the circumferences. Let angle BAC be an inscribed angle in the first circle standing on circumference BC, and let angle EDF be an inscribed angle in the second circle standing on circumference EF. By Proposition 3.20, the central angle BGC is double the inscribed angle BAC, and the central angle EHF is double the inscribed angle EDF. Therefore angle BAC is half of angle BGC and angle EDF is half of angle EHF.

**Step 10.** By Proposition 5.15, since angle BGC is to angle EHF as circumference BC is to circumference EF (established in Step 8), and angle BAC is half of angle BGC while angle EDF is half of angle EHF, the halves are in the same ratio as the wholes. That is, angle BAC is to angle EDF as circumference BC is to circumference EF.

**Step 11.** Therefore, in equal circles, angles have the same ratio as the circumferences on which they stand, whether they stand at the centres or at the circumferences. Q.E.F.

**USED:** 1.23, 3.20, 3.26, 3.27, 5.15, D3.1, D5.5
**Human refs (from References field):** 3.27, D5.5
**Jaccard:** 0.286 — AI adds ['1.23', '3.20', '3.26', '5.15', 'D3.1']
