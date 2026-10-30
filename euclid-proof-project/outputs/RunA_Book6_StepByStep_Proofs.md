# Book 6 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 6.1
**Statement:** Triangles and parallelograms which are under the same height are to one another as their bases.

**Step 1.** Let ABC be a triangle and BCGF be a parallelogram, both having the same base BC and under the same height, that is, lying between the same parallel lines. We must show that for any triangle and any parallelogram under the same height, each is to the other as their respective bases. More precisely, let there be any triangle ABC with base BC and any parallelogram BCGF with base BC, both under the same height. We wish to show: triangle ABC is to triangle ACD as BC is to CD, and parallelogram BCGF is to parallelogram CDHE as BC is to CD, where ACD is another triangle and CDHE another parallelogram, both under the same height.

**Step 2.** Let ABC be a triangle with base BC, and let ACD be a triangle with base CD, where B, C, D are collinear, and both triangles have vertex A at the same height above line BD. Similarly, let BCGF and CDHE be parallelograms on bases BC and CD respectively, under the same height. We shall prove that triangle ABC is to triangle ACD as BC is to CD, and that parallelogram BCGF is to parallelogram CDHE as BC is to CD.

**Step 3.** Produce BD in both directions. Along the direction from B away from D, take any number of segments BH, HK each equal to BC, by repeated application of P1 and P2 to extend the line, and 1.3 to cut off equal lengths. Along the direction from D away from B, take any number of segments DL, LM each equal to CD, again by P1, P2, and 1.3.

**Step 4.** Join A to each of the points H, K, L, M by P1, forming triangles AHB, ABK (on base HK through B), and triangles ADL, ALM.

**Step 5.** Since KB, BH, and BC are all equal to one another, the triangles AKB, ABH, and ABC are triangles on equal bases and under the same height (since A is at the same distance above line KD). By 1.38, triangles on equal bases and between the same parallels are equal. Therefore triangle AKC (which consists of triangles AKB, ABH, and ABC) is triple the triangle ABC. In general, the triangle on base KC equals the triangle ABC taken as many times as BC is contained in KC.

**Step 6.** Similarly, since CD, DL, and LM are all equal to one another, by 1.38 the triangles ACD, ADL, and ALM are all equal. Therefore triangle ACM (which consists of triangles ACD, ADL, and ALM) is triple triangle ACD. In general, the triangle on base CM equals triangle ACD taken as many times as CD is contained in CM.

**Step 7.** Thus if we take m copies of BC along one direction giving base KC = m times BC, the triangle AKC equals m times triangle ABC. And if we take n copies of CD along the other direction giving base CM = n times CD, the triangle ACM equals n times triangle ACD. That is, the equimultiple of triangle ABC corresponds to the triangle on the equimultiple of BC, and the equimultiple of triangle ACD corresponds to the triangle on the equimultiple of CD.

**Step 8.** Now, if KC > CM (that is, m times BC > n times CD), then triangle AKC > triangle ACM, because the triangle on the greater base with the same height is greater, by 1.38 applied together with CN5; if KC = CM, then triangle AKC = triangle ACM, by 1.38; and if KC < CM, then triangle AKC < triangle ACM.

**Step 9.** But triangle AKC is m times triangle ABC, and triangle ACM is n times triangle ACD; and KC is m times BC, and CM is n times CD. Therefore: if m times BC > n times CD, then m times triangle ABC > n times triangle ACD; if m times BC = n times CD, then m times triangle ABC = n times triangle ACD; and if m times BC < n times CD, then m times triangle ABC < n times triangle ACD.

**Step 10.** Since this holds for arbitrary positive integers m and n, by D5.5 (the definition of proportion), triangle ABC is to triangle ACD as BC is to CD. This establishes the result for triangles under the same height.

**Step 11.** Now consider the parallelograms BCGF and CDHE under the same height. By 1.41, parallelogram BCGF is double triangle ABC (since they share base BC and are between the same parallels). Likewise, parallelogram CDHE is double triangle ACD.

**Step 12.** Since parallelogram BCGF is double triangle ABC and parallelogram CDHE is double triangle ACD, and since triangle ABC is to triangle ACD as BC is to CD (proved in Step 10), by 5.15 (or more precisely by 5.11, which states that ratios equal to the same ratio are equal to one another, combined with the observation that doubling both terms of a ratio preserves it), the parallelogram BCGF is to parallelogram CDHE as BC is to CD. More directly, since BCGF = 2 times triangle ABC and CDHE = 2 times triangle ACD, taking the same multiple of both antecedent and consequent preserves the ratio by D5.5 and 5.15. Specifically, by 5.15, if four magnitudes are proportional, equimultiples of the first and third will also be proportional to the same equimultiples of the second and fourth. Here we apply the fact that the doubles stand in the same ratio, which follows from the definition of equal ratios (D5.5) since the equimultiple conditions are inherited.

**Step 13.** Therefore, triangles and parallelograms which are under the same height are to one another as their bases. Q.E.F.

**USED:** 1.3, 1.38, 1.41, 5.15, CN5, D5.5, P1, P2
**Human refs (from References field):** 1.38, 1.41, 5.11, 5.15, D5.5
**Jaccard:** 0.444 — AI adds ['1.3', 'CN5', 'P1', 'P2']; Human adds ['5.11']

## Proposition 6.2
**Statement:** If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section will be parallel to the remaining side of the triangle.

**Step 1.** Let ABC be a triangle, and let DE be drawn parallel to BC, with D on AB and E on AC. Join BE and CD [P1].

**Step 2.** Consider triangles BDE and CDE. They share the same base DE, and their vertices B and C lie on the line BC, which is parallel to DE. Therefore triangles BDE and CDE are equal in area, since they are on the same base DE and between the same parallels DE and BC [1.38].

**Step 3.** Triangles ADE and BDE have the same height (the perpendicular from E to line AB), and their bases along AB are AD and DB respectively. By 6.1 (triangles under the same height are as their bases), triangle ADE : triangle BDE = AD : DB [6.1].

**Step 4.** Triangles ADE and CDE have the same height (the perpendicular from D to line AC), and their bases along AC are AE and EC respectively. By 6.1, triangle ADE : triangle CDE = AE : EC [6.1].

**Step 5.** Since triangle BDE equals triangle CDE (Step 2), the same magnitude triangle ADE has the same ratio to each of these equal magnitudes. By 5.7 (the same magnitude has to equal magnitudes the same ratio), triangle ADE : triangle BDE = triangle ADE : triangle CDE [5.7].

**Step 6.** From Step 3, triangle ADE : triangle BDE = AD : DB. From Step 4, triangle ADE : triangle CDE = AE : EC. From Step 5, triangle ADE : triangle BDE = triangle ADE : triangle CDE. Therefore AD : DB = AE : EC, since ratios which are the same with the same ratio are the same with one another [5.11].

**Step 7.** This completes the first part: if DE is parallel to BC, then AD : DB = AE : EC.

**Step 8.** For the converse, suppose the sides of triangle ABC are cut proportionally, so that AD : DB = AE : EC, where D is on AB and E is on AC. Join BE and CD [P1].

**Step 9.** By 6.1, triangle ADE : triangle BDE = AD : DB (same height from E to AB) [6.1].

**Step 10.** By 6.1, triangle ADE : triangle CDE = AE : EC (same height from D to AC) [6.1].

**Step 11.** Since AD : DB = AE : EC (hypothesis), from Steps 9 and 10 we have triangle ADE : triangle BDE = triangle ADE : triangle CDE (by transitivity: each ratio equals AD : DB = AE : EC) [5.11].

**Step 12.** Since the same magnitude triangle ADE has the same ratio to triangle BDE and to triangle CDE, by 5.9 (magnitudes to which the same magnitude has the same ratio are equal), triangle BDE = triangle CDE [5.9].

**Step 13.** Now triangles BDE and CDE are equal in area, lie on the same base DE, and are on the same side of DE. By 1.39 (equal triangles on the same base and on the same side are between the same parallels), DE is parallel to BC [1.39].

**Step 14.** Therefore, if the sides of the triangle are cut proportionally, the line joining the points of section is parallel to the remaining side. Q.E.D.

**USED:** 1.38, 1.39, 5.11, 5.7, 5.9, 6.1, P1
**Human refs (from References field):** 1.38, 1.39, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.857 — AI adds ['P1']

## Proposition 6.3
**Statement:** If an angle of a triangle be bisected and the straight line cutting the angle cut the base also, the segments of the base will have the same ratio as the remaining sides of the triangle; and, if the segments of the base have the same ratio as the remaining sides of the triangle, the straight line joined from the vertex to the point of section will bisect the angle of the triangle.

**Part I (Forward direction):** If in triangle ABC the angle BAC is bisected by AD, where D lies on BC, then BD is to DC as BA is to AC.

**Step 1.** Let triangle ABC be given, and let the angle BAC be bisected by the straight line AD, so that angle BAD equals angle DAC. We must show that BD is to DC as BA is to AC. [Setup from hypothesis]

**Step 2.** Through C, draw CE parallel to DA, and let BA be produced to meet CE at E. [By 1.31, through any point not on a given line we can draw a line parallel to it; by P2, BA can be produced; since DA and CE are parallel and BA is a transversal that is not parallel to them, BA produced meets CE at some point E by P5.]

**Step 3.** Since AD is parallel to EC, and AC is a transversal cutting them, the alternate angles DAC and ACE are equal. [By 1.29]

**Step 4.** Since AD is parallel to EC, and BAE is a transversal cutting them, the corresponding angles BAD and AEC are equal. [By 1.29]

**Step 5.** But angle BAD equals angle DAC by hypothesis. Therefore angle ACE equals angle AEC, since both are equal to one of the bisected angles. [By CN1]

**Step 6.** Since in triangle ACE the angles ACE and AEC are equal, the side AE equals the side AC. [By 1.6, if two angles of a triangle are equal, the sides opposite them are equal.]

**Step 7.** Now in triangle BCE, since DA is parallel to CE and DA cuts the sides BC and BE, by the property of a line drawn parallel to one side of a triangle, the sides are cut proportionally. That is, BD is to DC as BA is to AE. [By 6.2]

**Step 8.** But AE equals AC (from Step 6). Therefore BD is to DC as BA is to AC. [By 5.7, since AE equals AC, the ratio BA to AE equals the ratio BA to AC.]

**Part II (Converse direction):** If BD is to DC as BA is to AC, then AD bisects angle BAC.

**Step 9.** Suppose that BD is to DC as BA is to AC. We must show that angle BAD equals angle DAC. Using the same construction as before, through C draw CE parallel to DA, and produce BA to meet CE at E. [By 1.31 and P2, with the meeting guaranteed by P5 as before.]

**Step 10.** Since DA is parallel to CE, in triangle BCE the line DA is parallel to one side CE and cuts the other two sides. Therefore BD is to DC as BA is to AE. [By 6.2]

**Step 11.** But by hypothesis, BD is to DC as BA is to AC. Therefore BA is to AE equals BA is to AC. [By CN1 and 5.11, since both ratios equal BD to DC]

**Step 12.** Since BA is to AE as BA is to AC, it follows that AE equals AC. [By 5.9, if the same magnitude has the same ratio to two magnitudes, those magnitudes are equal.]

**Step 13.** Since AE equals AC in triangle ACE, the angles ACE and AEC are equal. [By 1.5]

**Step 14.** But angle AEC equals angle BAD, since DA is parallel to EC and BAE is a transversal, giving equal corresponding angles. [By 1.29]

**Step 15.** And angle ACE equals angle DAC, since DA is parallel to EC and AC is a transversal, giving equal alternate angles. [By 1.29]

**Step 16.** Therefore angle BAD equals angle DAC, since angle BAD equals angle AEC (Step 14), angle AEC equals angle ACE (Step 13), and angle ACE equals angle DAC (Step 15). [By CN1]

**Step 17.** Therefore AD bisects the angle BAC. This completes the proof in both directions. Q.E.F.

**USED:** 1.29, 1.31, 1.5, 1.6, 5.11, 5.7, 5.9, 6.2, CN1, P2, P5
**Human refs (from References field):** 1.29, 1.5, 1.6, 5.11, 5.9, 6.2
**Jaccard:** 0.545 — AI adds ['1.31', '5.7', 'CN1', 'P2', 'P5']

## Proposition 6.4
**Statement:** In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

**Step 1.** Let ABC and DCE be equiangular triangles with angle ABC = angle DCE, angle BAC = angle CDE, and angle ACB = angle DEC. We wish to show that the sides about the equal angles are proportional, with corresponding sides being those that subtend equal angles.

**Step 2.** Place the triangles so that BC is in a straight line with CE, with C between B and E, so that BCE is a straight line.

**Step 3.** Since the angles of triangle ABC satisfy angle ABC + angle ACB < two right angles [1.17], and angle ACB = angle DEC by hypothesis, we have angle ABC + angle DEC < two right angles. Produce BA beyond A and ED beyond D [P2]. Since the interior angles angle ABC and angle DEC on the same side of transversal BE sum to less than two right angles, the lines BA produced and ED produced must meet on that side [P5]. Let them meet at F, forming triangle BFE with C on side BE.

**Step 4.** We now show BF is parallel to CD. Since BCE is a straight line, angle BCD + angle DCE = two right angles [1.13]. Since angle ABC = angle DCE by hypothesis, angle FBC = angle ABC (as F lies on BA produced), and so angle FBC + angle BCD = angle DCE + angle BCD = two right angles. Since the co-interior angles FBC and BCD on transversal BE sum to two right angles, BF is parallel to CD [1.28].

**Step 5.** We now show AC is parallel to FE. Since BCE is a straight line, angle ACB + angle ACE = two right angles [1.13]. Since angle ACB = angle DEC by hypothesis, and angle FEC = angle DEC (as F lies on ED produced), we have angle ACE + angle FEC = two right angles. Since the co-interior angles ACE and FEC on transversal BE sum to two right angles, AC is parallel to FE [1.28].

**Step 6.** Since D lies on segment FE (as F is on line ED produced beyond D) and A lies on segment BF (as F is on line BA produced beyond A), we apply Proposition 6.2 to triangle BFE. Line CD is parallel to side BF and meets side BE at C and side FE at D. By 6.2, BC : CE = FD : DE.

**Step 7.** Again in triangle BFE, line AC is parallel to side FE and meets side BF at A and side BE at C. By 6.2, BA : AF = BC : CE.

**Step 8.** From Steps 6 and 7, the ratios BA : AF and FD : DE are each equal to BC : CE. Therefore BA : AF = FD : DE [5.11].

**Step 9.** Now, since AC is parallel to FD (Step 5, as FD is part of line FE) and AF is parallel to CD (Step 4, as AF is part of line BF), the quadrilateral ACDF has both pairs of opposite sides parallel, forming a parallelogram. By 1.34, the opposite sides are equal: AF = CD and AC = FD.

**Step 10.** Substituting the equalities from Step 9 into the proportions: since BA : AF = BC : CE and AF = CD, we obtain BA : CD = BC : CE. Since FD : DE = BC : CE and FD = AC, we obtain AC : DE = BC : CE.

**Step 11.** Therefore BA : CD = BC : CE = AC : DE. That is, in the equiangular triangles ABC and DCE, the sides about the equal angles are proportional. Moreover, the corresponding sides which subtend equal angles are proportional: BC and CE subtend the equal angles BAC and CDE; BA and CD subtend the equal angles ACB and DEC; and AC and DE subtend the equal angles ABC and DCE. This is what was to be proved.

**USED:** 1.13, 1.17, 1.28, 1.34, 5.11, 6.2, P2, P5
**Human refs (from References field):** 1.17, 1.28, 1.34, 5.16, 5.22, 6.2, P5
**Jaccard:** 0.500 — AI adds ['1.13', '5.11', 'P2']; Human adds ['5.16', '5.22']

## Proposition 6.5
**Statement:** If two triangles have their sides proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let ABC and DEF be two triangles having their sides proportional, so that AB is to DE as BC is to EF, and as AC is to DF. We must prove that the triangles are equiangular, with equal angles subtended by the corresponding sides, namely angle A equals angle D, angle B equals angle E, and angle C equals angle F.

**Step 2.** At the points D and E on the straight line DE, construct angle EDG equal to angle BAC and angle DEG equal to angle ABC [1.23].

**Step 3.** Since the three angles of a triangle are equal to two right angles [1.32], and angle EDG equals angle BAC and angle DEG equals angle ABC, the remaining angle DGE equals the remaining angle BCA.

**Step 4.** Therefore triangle ABC is equiangular with triangle DEG. Hence by Proposition 6.4, the sides about the equal angles are proportional: AB is to DE as BC is to EG, and as AC is to DG [6.4].

**Step 5.** But by hypothesis, AB is to DE as BC is to EF. Since AB is to DE as BC is to EG (from Step 4) and AB is to DE as BC is to EF (by hypothesis), we have BC is to EG as BC is to EF [CN1]. Therefore EG equals EF [5.9].

**Step 6.** Similarly, by hypothesis AB is to DE as AC is to DF, and from Step 4, AB is to DE as AC is to DG. Therefore AC is to DG as AC is to DF [CN1], and hence DG equals DF [5.9].

**Step 7.** Now in triangles DEG and DEF, DE is common, EG equals EF (Step 5), and DG equals DF (Step 6). Therefore by Proposition 1.8 (SSS congruence), triangle DEG is congruent to triangle DEF. In particular, angle DEG equals angle DEF, angle EDG equals angle EDF, and angle DGE equals angle DFE [1.8].

**Step 8.** But angle DEG was constructed equal to angle ABC (Step 2), so angle DEF equals angle ABC. And angle EDG was constructed equal to angle BAC (Step 2), so angle EDF equals angle BAC. And angle DGE equals angle BCA (Step 3), so angle DFE equals angle BCA.

**Step 9.** Therefore triangle ABC is equiangular with triangle DEF, and the equal angles are those subtended by the corresponding (proportional) sides: angle A equals angle D (subtended by BC and EF), angle B equals angle E (subtended by AC and DF), and angle C equals angle F (subtended by AB and DE). This is what was to be proved.

**USED:** 1.23, 1.32, 1.8, 5.9, 6.4, CN1
**Human refs (from References field):** 1.23, 1.32, 1.4, 1.8, 5.11, 5.9, 6.4
**Jaccard:** 0.625 — AI adds ['CN1']; Human adds ['1.4', '5.11']

## Proposition 6.6
**Statement:** If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

Let triangles ABC and DEF have angle BAC equal to angle EDF, and let the sides about the equal angles be proportional, so that AB is to AC as DE is to DF.

**Step 1.** On DE, mark off DG equal to AB, and on DF, mark off DH equal to AC. This is possible since we can cut off from the greater (or equal) a length equal to the lesser, by 1.3.

**Step 2.** Join GH, by P1.

**Step 3.** Since DG equals AB and DH equals AC, we have DG is to DH as AB is to AC, by 5.7 (equal magnitudes have to equal magnitudes the same ratio). But AB is to AC as DE is to DF, by hypothesis. Therefore DG is to DH as DE is to DF, by 5.11 (ratios equal to the same ratio are equal to one another).

**Step 4.** By alternando (5.16), DG is to DE as DH is to DF.

**Step 5.** By invertendo, which follows from 5.7 (Corollary), DE is to DG as DF is to DH.

**Step 6.** By separando (5.17), since DE is to DG as DF is to DH, we obtain GE is to DG as HF is to DH, where GE equals DE minus DG and HF equals DF minus DH.

**Step 7.** By invertendo (5.7 Corollary) again, DG is to GE as DH is to HF.

**Step 8.** Since the sides DE and DF of triangle DEF are cut proportionally at G and H respectively (that is, DG is to GE as DH is to HF), the line GH is parallel to the remaining side EF, by the converse part of 6.2.

**Step 9.** Since GH is parallel to EF, and the straight line DE falls on them, the alternate angles DGH and DEF are equal; and since the straight line DF falls on GH and EF, the alternate angles DHG and DFE are equal, by 1.29.

**Step 10.** Now consider triangles ABC and DGH. We have AB equal to DG (by construction), AC equal to DH (by construction), and angle BAC equal to angle GDH (since angle GDH is the same as angle EDF, which equals angle BAC by hypothesis). Therefore, by 1.4 (side-angle-side), triangle ABC is congruent to triangle DGH, and the remaining angles are respectively equal: angle ABC equals angle DGH, and angle ACB equals angle DHG.

**Step 11.** But angle DGH equals angle DEF, and angle DHG equals angle DFE (from Step 9). Therefore angle ABC equals angle DEF, and angle ACB equals angle DFE, by CN1 (things equal to the same thing are equal to one another).

**Step 12.** Together with angle BAC equal to angle EDF (given), the triangles ABC and DEF are equiangular, and the equal angles are those subtended by the corresponding sides: angle BAC equals angle EDF (subtended by BC and EF respectively), angle ABC equals angle DEF (subtended by AC and DF respectively), and angle ACB equals angle DFE (subtended by AB and DE respectively).

Therefore, if two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles are equiangular and have those angles equal which the corresponding sides subtend. Q.E.D.

**USED:** 1.29, 1.3, 1.4, 5.11, 5.16, 5.17, 5.7, 6.2, CN1, P1
**Human refs (from References field):** 1.23, 1.32, 1.4, 5.11, 5.9, 6.4
**Jaccard:** 0.143 — AI adds ['1.29', '1.3', '5.16', '5.17', '5.7', '6.2', 'CN1', 'P1']; Human adds ['1.23', '1.32', '5.9', '6.4']

## Proposition 6.7
**Statement:** If two triangles have one angle equal to one angle, the sides about other angles proportional, and the remaining angles either both less or both not less than a right angle, the triangles will be equiangular and will have those angles equal, the sides about which are proportional.

**Step 1.** Let ABC and DEF be two triangles having angle BAC equal to angle EDF, the sides about angles ABC and DEF proportional so that AB is to DE as BC is to EF, and the remaining angles ACB and DFE either both less than a right angle or both not less than a right angle. We must show the triangles are equiangular with angle ABC equal to angle DEF.

**Step 2.** Suppose angle ABC is not equal to angle DEF. At point E on straight line EF, construct angle DEG equal to angle ABC, with G on the same side of EF as D [1.23].

**Step 3.** Since in triangles ABC and DEG we have angle BAC equal to angle EDF (given) and angle ABC equal to angle DEG (construction), the remaining angle ACB equals angle DGE, because the three angles of each triangle sum to two right angles [1.32].

**Step 4.** Therefore triangles ABC and DEG are equiangular. By Proposition 6.4, the sides about the equal angles are proportional, so AB is to DE as BC is to EG [6.4].

**Step 5.** But AB is to DE as BC is to EF (given). Since AB to DE equals BC to EG, and AB to DE equals BC to EF, we conclude BC is to EG as BC is to EF [5.11]. Therefore EG equals EF [5.9].

**Step 6.** Since EG equals EF, if G is not the same point as F, then triangle EGF is isosceles, and angle EGF equals angle EFG [1.5].

**Step 7.** Now in triangle DEG, we showed angle GDE plus angle DEG plus angle DGE equals two right angles [1.32]. So angle GDE equals two right angles minus angle ABC minus angle ACB. But in triangle ABC, angle BAC plus angle ABC plus angle ACB equals two right angles [1.32], so angle BAC equals two right angles minus angle ABC minus angle ACB. Therefore angle GDE equals angle BAC. Since angle BAC equals angle EDF (given), we have angle GDE equals angle EDF.

**Step 8.** Since angle GDE equals angle EDF, and both angles are measured from ray DE at point D, ray DG coincides with ray DF. Therefore G lies on the straight line DF.

**Step 9.** Since G lies on line DF and G is not F (our assumption), either G lies between D and F, or F lies between D and G.

**Step 10.** Case 1: Suppose both angle ACB and angle DFE are less than a right angle. Consider first that G lies between D and F. Then angles DGE and EGF are supplementary, summing to two right angles [1.13]. Since angle DGE equals angle ACB, which is less than a right angle, angle EGF is greater than a right angle. Since angle EGF equals angle EFG [Step 6], angle EFG is also greater than a right angle. But then in triangle EGF the two angles EGF and EFG together already exceed two right angles, which is impossible since the sum of all three angles of a triangle equals two right angles [1.32]. This is a contradiction.

**Step 11.** Still in Case 1, consider that F lies between D and G. Then angles DFE and EFG are supplementary, summing to two right angles [1.13]. Since angle DFE is less than a right angle, angle EFG is greater than a right angle. Since angle EFG equals angle EGF [Step 6], angle EGF is also greater than a right angle. At point G, since D, F, G are collinear with F between D and G, the ray GD passes through F, so angle DGE equals angle EGF. Thus angle ACB equals angle EGF, which is greater than a right angle. But angle ACB is less than a right angle by hypothesis. This is a contradiction.

**Step 12.** Case 2: Suppose both angle ACB and angle DFE are not less than a right angle. Consider first that G lies between D and F. Then angles DGE and EGF sum to two right angles [1.13]. Since angle DGE equals angle ACB, which is not less than a right angle, angle EGF is at most a right angle. Since angle EGF equals angle EFG [Step 6], angle EFG is at most a right angle. Now since G is between D and F, the ray from F toward G is the same as the ray from F toward D, so angle EFG equals angle EFD, that is, angle DFE. Hence angle DFE is at most a right angle. But angle DGE equals angle ACB is not less than a right angle, so angle EGF equals two right angles minus angle ACB, which is at most a right angle. If angle ACB is strictly greater than a right angle, angle EGF is strictly less, so angle EFG is strictly less than a right angle, making angle DFE strictly less than a right angle, contradicting the hypothesis. If angle ACB equals a right angle exactly, then angle EGF equals a right angle, so angle EFG equals a right angle, and in triangle EGF the angles EGF and EFG sum to two right angles, leaving angle GEF equal to zero [1.32], which is impossible for a triangle. This is a contradiction in all sub-cases.

**Step 13.** Still in Case 2, consider that F lies between D and G. Then angles DFE and EFG sum to two right angles [1.13]. Since angle DFE is not less than a right angle, angle EFG is at most a right angle. Since angle EFG equals angle EGF [Step 6], angle EGF is at most a right angle. At point G, since F lies between D and G, angle DGE equals angle EGF (the ray GD passes through F). So angle ACB equals angle EGF, which is at most a right angle. If angle DFE is strictly greater than a right angle, then angle EFG is strictly less than a right angle, so angle EGF is strictly less, hence angle ACB is strictly less than a right angle, contradicting the hypothesis that angle ACB is not less than a right angle. If angle DFE equals a right angle exactly, then angle EFG equals a right angle, so angle EGF equals a right angle, and in triangle EGF the two base angles sum to two right angles, forcing angle GEF to equal zero [1.32], which is impossible. This is a contradiction in all sub-cases.

**Step 14.** Since the assumption that angle ABC is not equal to angle DEF leads to a contradiction in every case, we conclude angle ABC equals angle DEF.

**Step 15.** Since angle BAC equals angle EDF (given) and angle ABC equals angle DEF (proved), the remaining angles are also equal: angle ACB equals angle DFE [1.32]. Therefore the triangles ABC and DEF are equiangular, and they have those angles equal (namely ABC and DEF) about which the sides are proportional.

**USED:** 1.13, 1.23, 1.32, 1.5, 5.11, 5.9, 6.4
**Human refs (from References field):** 1.13, 1.17, 1.23, 1.32, 1.5, 5.11, 5.9, 6.4
**Jaccard:** 0.875 — Human adds ['1.17']

## Proposition 6.8
**Statement:** If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.

**Step 1.** Let triangle ABC have a right angle at A (so angle BAC is a right angle), and let AD be drawn from A perpendicular to the base BC. Then angle ADB and angle ADC are each right angles [D1.10].

**Step 2.** Consider triangle ABD and triangle ABC. Angle ADB is a right angle and angle BAC is a right angle, so angle ADB equals angle BAC [P4]. Furthermore, angle ABD is the same angle as angle ABC, since B is common to both triangles.

**Step 3.** Since in triangle ABC the three angles sum to two right angles [1.32], and in triangle ABD the three angles also sum to two right angles [1.32], and two of the angles are respectively equal (angle ADB = angle BAC, and angle ABD = angle ABC), the remaining angles must be equal: angle BAD equals angle ACB [CN3].

**Step 4.** Since triangle ABD and triangle ABC have all three angles respectively equal (angle ADB = angle BAC, angle ABD = angle ABC, angle BAD = angle ACB), they are equiangular. Therefore the sides about the equal angles are proportional [6.4], and hence triangle ABD is similar to triangle ABC [D6.1].

**Step 5.** Now consider triangle ACD and triangle ABC. Angle ADC is a right angle and angle BAC is a right angle, so angle ADC equals angle BAC [P4]. Furthermore, angle ACD is the same angle as angle ACB, since C is common to both triangles.

**Step 6.** Since in triangle ACD the three angles sum to two right angles [1.32], and in triangle ABC the three angles also sum to two right angles [1.32], and two of the angles are respectively equal (angle ADC = angle BAC, and angle ACD = angle ACB), the remaining angles must be equal: angle DAC equals angle ABC [CN3].

**Step 7.** Since triangle ACD and triangle ABC have all three angles respectively equal (angle ADC = angle BAC, angle ACD = angle ACB, angle DAC = angle ABC), they are equiangular. Therefore the sides about the equal angles are proportional [6.4], and hence triangle ACD is similar to triangle ABC [D6.1].

**Step 8.** It remains to show that triangle ABD is similar to triangle ACD. From Steps 3 and 6, we have: angle BAD equals angle ACB (Step 3), and angle DAC equals angle ABC (Step 6). Also angle ADB equals angle ADC, both being right angles [P4]. Since angle ACB equals angle DAC (both equal angle ABC by Step 6 giving DAC = ABC, and from triangle ABC we can compare), let us verify directly: in triangle ABD, the angles are angle ABD, angle BAD, angle ADB; in triangle ACD, the angles are angle ACD, angle DAC, angle ADC.

**Step 9.** From Step 3: angle BAD = angle ACB = angle ACD. From Step 6: angle DAC = angle ABC = angle ABD. And angle ADB = angle ADC [P4]. Therefore triangle ABD and triangle ACD have all three angles respectively equal, so they are equiangular. By the proportionality of sides about equal angles [6.4], triangle ABD is similar to triangle ACD [D6.1].

**Step 10.** Therefore the triangles adjoining the perpendicular (triangles ABD and ACD) are similar both to the whole triangle ABC and to one another. Q.E.F.

**USED:** 1.32, 6.4, CN3, D1.10, D1.21, D6.1, P4
**Human refs (from References field):** 1.32, 6.4, D6.1
**Jaccard:** 0.429 — AI adds ['CN3', 'D1.10', 'D1.21', 'P4']

## Proposition 6.9
**Statement:** From a given straight line to cut off a prescribed part.

**Step 1.** Let AB be the given straight line, and let the prescribed part be one-third (the argument works for any part 1/n; we illustrate with one-third). We must cut off one-third of AB from the endpoint A.

**Step 2.** From A, draw a straight line AC making any angle with AB. [P1]

**Step 3.** On AC, take an arbitrary point D. [P1]

**Step 4.** Using Proposition 1.3, lay off on AC from A three successive segments equal to AD: let AE = AD, and EF = AD, and let the third endpoint be D itself — that is, choose points D1, D2, D3 on AC such that AD1 = D1D2 = D2D3, where D3 lies further from A. More precisely: take any point D1 on AC. Then by 1.3, cut off D1D2 equal to AD1 on the ray from D1 away from A, and similarly cut off D2D3 equal to AD1. So AD1 = D1D2 = D2D3, and we have three equal segments from A along AC. [1.3]

**Step 5.** Join D3 to B by a straight line. [P1]

**Step 6.** Through D1, draw a straight line D1G parallel to D3B, meeting AB at G. [1.31]

**Step 7.** Since in triangle AD3B, the straight line D1G is drawn parallel to the side D3B, by Proposition 6.2 (if a straight line is drawn parallel to one side of a triangle, it cuts the other two sides proportionally), we have: AD1 : D1D3 = AG : GB. [6.2]

**Step 8.** Now AD1 is one segment, and D1D3 = D1D2 + D2D3 = AD1 + AD1 = 2·AD1, since D1D2 = D2D3 = AD1 by construction. Therefore AD1 : D1D3 = AD1 : 2·AD1.

**Step 9.** By the definition of proportion (D5.5) and the properties of multiples (5.15 — separation of a ratio), since AD3 = AD1 + D1D3 = AD1 + 2·AD1 = 3·AD1, we have the ratio AD1 : AD3 = 1 : 3. Applying composition of ratio to AD1 : D1D3 = AG : GB, we get AD1 : AD3 = AG : AB (by Proposition 5.18 — ex aequali in perturbed proportion — or more directly by the addendo form). Specifically, since AD1 : D1D3 = AG : GB, then by adding antecedents and consequents: (AD1 + D1D3) : D1D3 = (AG + GB) : GB, i.e., AD3 : D1D3 = AB : GB. But we need the other composition: AD1 : (AD1 + D1D3) = AG : (AG + GB), i.e., AD1 : AD3 = AG : AB. This follows from the proportion AD1 : D1D3 = AG : GB by Proposition 5.18 (componendo in the form: if a : b = c : d, then a : (a+b) = c : (c+d)). [5.18]

**Step 10.** Since AD1 : AD3 = 1 : 3 (as AD3 is the triple of AD1, being composed of three equal segments each equal to AD1), we conclude AG : AB = 1 : 3. [D5.1, D5.2]

**Step 11.** Therefore AG is one-third of AB (D5.1 — AD1 is a part of AD3 since it measures it, and the same ratio holds for AG to AB), and the prescribed third part has been cut off from the given straight line AB.

**Step 12.** The same construction generalizes: to cut off a 1/n part, lay off n equal segments on AC and draw a parallel through the first point to the line joining the nth point to B. By the same reasoning using 6.2 and 5.18, the intercepted segment on AB will be the prescribed 1/n part of AB. Q.E.F. [6.2, 5.18]

**USED:** 1.3, 1.31, 5.18, 6.2, D5.1, D5.2, D5.5, P1
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.375 — AI adds ['5.18', 'D5.1', 'D5.2', 'D5.5', 'P1']

## Proposition 6.10
**Statement:** To cut a given uncut straight line similarly to a given cut straight line.

**Step 1.** Let AC be the given cut straight line, cut at points D and E (so that A, D, E, C lie in order along the line), and let AB be the given uncut straight line. We are required to cut AB similarly to AC.

**Step 2.** Place AB and AC so that they contain any angle at A. Join B to C by a straight line [P1].

**Step 3.** Through D, draw DF parallel to BC, meeting AB at F [1.31]. Through E, draw EG parallel to BC, meeting AB at G [1.31].

**Step 4.** Since DF and EG are each parallel to BC, they are parallel to one another [1.30].

**Step 5.** In triangle ABC, since DF is parallel to side BC and meets sides AC and AB at D and F respectively, by Proposition 6.2 the sides are cut proportionally: AD:DC = AF:FB.

**Step 6.** In triangle ABC, since EG is parallel to side BC and meets sides AC and AB at E and G respectively, by Proposition 6.2: AE:EC = AG:GB.

**Step 7.** Now consider triangle AEG. The point D lies on side AE, and the point F lies on side AG, and DF is parallel to EG [Step 4]. Therefore, by Proposition 6.2 applied to triangle AEG: AD:DE = AF:FG.

**Step 8.** Since AD:DE = AF:FG [Step 7], by Proposition 5.18 (componendo from separando): AE:DE = AG:FG, where AE = AD + DE and AG = AF + FG.

**Step 9.** From Step 8, by inversion: DE:AE = FG:AG. From Step 6 we have AE:EC = AG:GB. Applying ex aequali [5.22] to the chain DE:AE and AE:EC on one side, and FG:AG and AG:GB on the other (since DE:AE = FG:AG and AE:EC = AG:GB), we obtain DE:EC = FG:GB.

**Step 10.** We have now established AD:DE = AF:FG [Step 7] and DE:EC = FG:GB [Step 9]. Therefore AB has been cut at F and G similarly to how AC is cut at D and E: the segments AF, FG, GB of line AB are in the same ratios as the segments AD, DE, EC of line AC.

**Step 11.** Therefore the given uncut straight line AB has been cut similarly to the given cut straight line AC, which is what was required to be done. Q.E.F.

**USED:** 1.30, 1.31, 5.18, 5.22, 6.2, P1
**Human refs (from References field):** 1.31, 1.34, 6.2
**Jaccard:** 0.286 — AI adds ['1.30', '5.18', '5.22', 'P1']; Human adds ['1.34']

## Proposition 6.11
**Statement:** To two given straight lines to find a third proportional.

**Step 1.** Let AB and AC be the two given straight lines. It is required to find a third proportional to AB and AC, that is, to find a straight line such that AB : AC :: AC : (that line).

**Step 2.** Place AB and AC so as to contain any angle at A. [P1, for setting up the configuration.]

**Step 3.** Produce AB to D, and produce AC to E. [P2.]

**Step 4.** Cut off BD equal to AC on the extension of AB beyond B. [1.3.]

**Step 5.** Join B to C. [P1.]

**Step 6.** Through D, draw DE parallel to BC, meeting AC produced at E. [1.31.]

**Step 7.** Now in triangle ADE, the straight line BC is parallel to DE (since DE was drawn parallel to BC). By Proposition 6.2, a straight line drawn parallel to one side of a triangle cuts the other two sides proportionally. Therefore AB : BD :: AC : CE. [6.2.]

**Step 8.** But BD was made equal to AC (Step 4). Since BD = AC, and AB : BD :: AC : CE, by Proposition 5.7 (equal magnitudes have to the same magnitude the same ratio, and the same magnitude has to equal magnitudes the same ratio), we may substitute AC for BD in the proportion, yielding AB : AC :: AC : CE. [5.7, CN1.]

**Step 9.** Therefore CE is a third proportional to AB and AC. That is, AB : AC :: AC : CE, which is what was required to find. Q.E.F.

**USED:** 1.3, 1.31, 5.7, 6.2, CN1, P1, P2
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.429 — AI adds ['5.7', 'CN1', 'P1', 'P2']

## Proposition 6.12
**Statement:** To three given straight lines to find a fourth proportional.

**Step 1.** Let A, B, C be the three given straight lines. It is required to find a fourth straight line D such that A : B :: C : D.

**Step 2.** Set out two straight lines DE, DF containing any angle EDF [P1].

**Step 3.** On DE, cut off DG equal to A and GE equal to B [1.3]. On DF, cut off DH equal to C [1.3].

**Step 4.** Join G to H [P1].

**Step 5.** Through E, draw EF parallel to GH [1.31], where F is the point at which this parallel meets DF (produced if necessary by P2).

**Step 6.** Since GH is parallel to EF, a side of triangle DEF, by Proposition 6.2 the line GH cuts the sides of triangle DEF proportionally. Therefore DG : GE :: DH : HF.

**Step 7.** But DG = A, GE = B, and DH = C by construction. Therefore A : B :: C : HF.

**Step 8.** Thus HF is the fourth proportional to the three given straight lines A, B, C. Q.E.F.

**USED:** 1.3, 1.31, 6.2, P1, P2
**Human refs (from References field):** 1.31, 6.2
**Jaccard:** 0.400 — AI adds ['1.3', 'P1', 'P2']

## Proposition 6.13
**Statement:** To two given straight lines to find a mean proportional.

**Step 1.** Let AB and BC be the two given straight lines. It is required to find a mean proportional to AB and BC.

**Step 2.** Place AB and BC in a straight line so that they form the continuous segment AC, with B lying between A and C [P1, P2].

**Step 3.** Describe the semicircle ADC on AC as diameter [P3, D1.17, D1.18]. That is, find the midpoint of AC, and with that midpoint as centre and half of AC as radius, describe the semicircle on the side chosen.

**Step 4.** From B, draw BD at right angles to AC, meeting the semicircle at D [1.11]. Since AC is the diameter and BD is erected perpendicular to it at a point between A and C, BD must meet the circumference at some point D (because B lies between A and C and is therefore interior to the semicircle, and a line from an interior point perpendicular to the diameter reaches the circumference).

**Step 5.** Join AD and DC [P1].

**Step 6.** Now the angle ADC is an angle in a semicircle, since A and C are the endpoints of the diameter AC and D lies on the circumference. Therefore angle ADC is a right angle [3.31].

**Step 7.** In the right-angled triangle ADC, the angle at D is a right angle, and BD has been drawn from the right angle perpendicular to the base AC. By 6.8, the triangles ABD and BDC adjoining the perpendicular are similar both to the whole triangle ADC and to one another.

**Step 8.** Since triangle ABD is similar to triangle DBC (by Step 7), the sides about their equal angles are proportional [D6.1]. In particular, the sides adjacent to the right angles at B correspond: AB in triangle ABD corresponds to DB in triangle DBC, and BD in triangle ABD corresponds to BC in triangle DBC. Therefore AB is to BD as BD is to BC.

**Step 9.** Thus BD is a mean proportional between the two given straight lines AB and BC.

Therefore, to the two given straight lines a mean proportional has been found, namely BD. Q.E.F.

**USED:** 1.11, 3.31, 6.8, D1.17, D1.18, D6.1, P1, P2, P3
**Human refs (from References field):** 3.31, 6.8
**Jaccard:** 0.222 — AI adds ['1.11', 'D1.17', 'D1.18', 'D6.1', 'P1', 'P2', 'P3']

## Proposition 6.14
**Statement:** In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal.

**Step 1.** Let ABCD and EBFG be equal and equiangular parallelograms with the equal angles at B, so that angle ABC equals angle EBF. We must show that the sides about the equal angles are reciprocally proportional, that is, AB : BE = BF : BC.

**Step 2.** Place the parallelograms so that the sides CB and BE about the equal angles are in a straight line, that is, C, B, E are collinear. Since C, B, E are collinear, angle ABC + angle ABE equals two right angles [1.13].

**Step 3.** Since angle ABC equals angle EBF (given), substituting yields angle EBF + angle ABE equals two right angles. Therefore A, B, F are in a straight line [1.14].

**Step 4.** Through C draw a line parallel to BF, and through F draw a line parallel to BC [1.31]. Let these lines meet at H. Then BCHF is a parallelogram with BC and BF as adjacent sides at B, CH parallel to BF, and FH parallel to BC.

**Step 5.** In parallelogram ABCD, the side DC is parallel to AB and hence parallel to the line ABF. In parallelogram BCHF, the side CH is parallel to BF and hence parallel to the line ABF. Since both DC and CH pass through C and are each parallel to ABF, they must lie on the same straight line, so D, C, H are collinear [1.30].

**Step 6.** In parallelogram EBFG, the side GF is parallel to EB and hence parallel to the line CBE. In parallelogram BCHF, the side HF is parallel to BC and hence parallel to the line CBE. Since both GF and HF pass through F and are each parallel to CBE, they must lie on the same straight line, so H, F, G are collinear [1.30].

**Step 7.** Now parallelograms ABCD and BCHF have their bases AB and BF on the same straight line ABF, and their opposite sides lie on the same straight line DCH (by Step 5). Therefore they are under the same height, and by 6.1, ABCD : BCHF = AB : BF.

**Step 8.** Similarly, parallelograms BCHF and EBFG have their bases BC and BE on the same straight line CBE, and their opposite sides lie on the same straight line HFG (by Step 6). Therefore they are under the same height, and by 6.1, BCHF : EBFG = BC : BE. Equivalently, EBFG : BCHF = BE : BC.

**Step 9.** (Forward direction) Since parallelogram ABCD equals parallelogram EBFG (given), they have the same ratio to BCHF [5.7]. Therefore EBFG : BCHF = AB : BF (from Step 7). But also EBFG : BCHF = BE : BC (from Step 8). Hence AB : BF = BE : BC [5.11].

**Step 10.** By alternation, AB : BE = BF : BC [5.16]. This is the reciprocal proportion of the sides about the equal angles, which was to be proved.

**Step 11.** (Converse direction) Now let ABCD and EBFG be equiangular parallelograms with equal angles at B and with the sides about the equal angles reciprocally proportional, so that AB : BE = BF : BC. We must show that parallelogram ABCD equals parallelogram EBFG.

**Step 12.** Using the same arrangement as before (Steps 2 through 8), we again have ABCD : BCHF = AB : BF (Step 7) and BCHF : EBFG = BC : BE (Step 8).

**Step 13.** From the hypothesis AB : BE = BF : BC, by alternation AB : BF = BE : BC [5.16].

**Step 14.** From Step 7, ABCD : BCHF = AB : BF = BE : BC (by Step 13). From Step 8, EBFG : BCHF = BE : BC. Therefore ABCD : BCHF = EBFG : BCHF [5.11].

**Step 15.** Since ABCD and EBFG have the same ratio to the same magnitude BCHF, it follows that ABCD equals EBFG [5.9]. This is what was to be proved.

**USED:** 1.13, 1.14, 1.30, 1.31, 5.11, 5.16, 5.7, 5.9, 6.1
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.556 — AI adds ['1.13', '1.30', '1.31', '5.16']

## Proposition 6.15
**Statement:** In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal.

**Step 1.** Let ABC and ADE be two equal triangles having angle BAC equal to angle DAE. We are to show that the sides about the equal angles are reciprocally proportional, namely that CA:AD = EA:AB; and conversely.

**Step 2.** Place the two triangles so that CA and AD are in a straight line, with the equal angles at vertex A. Since angle BAC equals angle DAE and CA, AD are in a straight line, we have angle BAC + angle CAD equal to two right angles by [1.13]. Therefore angle DAE + angle CAD also equals two right angles, and so EA and AC are in a straight line by [1.14].

**Step 3.** Join BE by [P1].

**Step 4.** Triangles ABC and ABE share vertex B, and their bases CA and AE lie on the same straight line CE. Hence they are under the same height. By [6.1], triangle ABC is to triangle ABE as CA is to AE.

**Step 5.** Triangles ABE and ADE share vertex E, and their bases BA and AD lie on the same straight line BD. Hence they are under the same height. By [6.1], triangle ABE is to triangle ADE as BA is to AD.

**Step 6.** Since triangle ABC equals triangle ADE (given), triangle ABC has to triangle ABE the same ratio that triangle ADE has to triangle ABE by [5.7].

**Step 7.** From Step 4, triangle ABC : triangle ABE = CA : AE. From Steps 5 and 6, triangle ADE : triangle ABE = BA : AD, so triangle ABC : triangle ABE = BA : AD. But triangle ABC : triangle ABE = CA : AE from Step 4. Therefore CA : AE = BA : AD.

**Step 8.** By alternando [5.16], CA : BA = AE : AD, which rearranged gives CA : AD = AE : BA. Thus the sides about the equal angles are reciprocally proportional.

**Step 9.** [Converse] Now let triangles ABC and ADE have angle BAC equal to angle DAE, and let the sides about the equal angles be reciprocally proportional, so that CA : AD = EA : AB. We are to show that triangle ABC equals triangle ADE.

**Step 10.** Place the triangles as before so that CA and AD are in a straight line and EA and AC are in a straight line (by the same reasoning from Steps 1-2 using [1.13] and [1.14]). Join BE by [P1].

**Step 11.** Since CA : AD = EA : AB (given), and also CA : AE = triangle ABC : triangle ABE by [6.1] (Step 4), and BA : AD = triangle ABE : triangle ADE by [6.1] (Step 5), we need to connect these.

**Step 12.** From the given proportion CA : AD = EA : AB, by alternando [5.16] we get CA : EA = AD : AB, that is, CA : AE = AD : BA. Inverting the second ratio by [5.7], CA : AE = AD : BA means CA : AE = AD : BA.

**Step 13.** From Step 4, CA : AE = triangle ABC : triangle ABE. From Step 5, BA : AD = triangle ABE : triangle ADE, so by inversion [5.7], AD : BA = triangle ADE : triangle ABE. Since CA : AE = AD : BA (Step 12), we have triangle ABC : triangle ABE = triangle ADE : triangle ABE.

**Step 14.** Since triangles ABC and ADE have the same ratio to triangle ABE, triangle ABC equals triangle ADE by [5.9].

**Step 15.** Therefore, in equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle and in which the sides about the equal angles are reciprocally proportional are equal. Q.E.D.

**USED:** 1.13, 1.14, 5.16, 5.7, 5.9, 6.1, P1
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.500 — AI adds ['1.13', '5.16', 'P1']; Human adds ['5.11']

## Proposition 6.16
**Statement:** If four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes be equal to the rectangle contained by the means, the four straight lines will be proportional.

**Step 1.** Let A, B, C, D be four straight lines such that A : B :: C : D. We wish to show that the rectangle contained by A and D equals the rectangle contained by B and C.

**Step 2.** Set out a point E and draw a straight line from E, and on it cut off EF equal to B and EG equal to A, where G is on the same ray from E as F, with EG along EF (by 1.3). At E, draw EH at right angles to EG (by 1.11).

**Step 3.** On EH, cut off EK equal to C and EL equal to D, where K and L lie on the same ray from E along EH (by 1.3).

**Step 4.** Through G draw a line parallel to EH, and through L draw a line parallel to EG, and let them meet at M. Then EGLM is a parallelogram (rectangle) contained by EG and EL, that is, by A and D (by 1.31, P1, D2.1).

**Step 5.** Similarly, through F draw a line parallel to EH, and through K draw a line parallel to EF, and let them meet at N. Then EFKN is a parallelogram (rectangle) contained by EF and EK, that is, by B and C (by 1.31, P1, D2.1).

**Step 6.** The rectangles EGLM and EFKN both have a right angle at E, since EH is perpendicular to EG by construction. Since all right angles are equal (P4), the two rectangles are equiangular.

**Step 7.** Now the sides about the equal angles at E are: EG = A and EL = D in rectangle EGLM, and EF = B and EK = C in rectangle EFKN. Since A : B :: C : D (given), we have EG : EF :: EK : EL. That is, the sides about the equal angles are reciprocally proportional.

**Step 8.** Therefore, by 6.14, since the two equiangular parallelograms have the sides about the equal angles reciprocally proportional, the parallelograms are equal. That is, the rectangle contained by A and D equals the rectangle contained by B and C.

**Step 9.** Now suppose conversely that the rectangle contained by A and D equals the rectangle contained by B and C. We wish to show that A : B :: C : D.

**Step 10.** Construct the same rectangles EGLM (contained by A and D) and EFKN (contained by B and C) as in Steps 2 through 5, sharing the right angle at E.

**Step 11.** Since the rectangle contained by A and D equals the rectangle contained by B and C, the parallelograms EGLM and EFKN are equal. They are also equiangular, sharing the right angle at E (by P4).

**Step 12.** Therefore, by 6.14, in equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional. Hence EG : EF :: EK : EL, that is, A : B :: C : D.

**Step 13.** Therefore, if four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and if the rectangle contained by the extremes be equal to the rectangle contained by the means, the four straight lines will be proportional. Q.E.F.

**USED:** 1.11, 1.3, 1.31, 6.14, D2.1, P1, P4
**Human refs (from References field):** 6.14
**Jaccard:** 0.143 — AI adds ['1.11', '1.3', '1.31', 'D2.1', 'P1', 'P4']

## Proposition 6.17
**Statement:** If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to the square on the mean, the three straight lines will be proportional.

**Step 1.** Let A, B, C be three straight lines that are proportional, so that A is to B as B is to C [D5.6, D5.8].

**Step 2.** Since A : B = B : C, we may regard A, B, B, C as four straight lines in proportion: the first (A) is to the second (B) as the third (B) is to the fourth (C).

**Step 3.** By 6.16 (forward part), if four straight lines are proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means. Therefore the rectangle contained by A and C equals the rectangle contained by B and B [6.16].

**Step 4.** But the rectangle contained by B and B is the square on B [D1.22, D2.1]. Therefore the rectangle contained by A and C (the extremes) is equal to the square on B (the mean).

**Step 5.** Now suppose conversely that the rectangle contained by A and C is equal to the square on B.

**Step 6.** The square on B is the rectangle contained by B and B [D1.22, D2.1]. Therefore the rectangle contained by A and C (the extremes) is equal to the rectangle contained by B and B (the means).

**Step 7.** By 6.16 (converse part), if the rectangle contained by the extremes is equal to the rectangle contained by the means, then the four straight lines are proportional. Therefore A is to B as B is to C [6.16].

**Step 8.** Hence the three straight lines A, B, C are proportional [D5.6].

**Step 9.** Therefore, if three straight lines are proportional, the rectangle contained by the extremes equals the square on the mean; and if the rectangle contained by the extremes equals the square on the mean, the three straight lines are proportional. Q.E.D.

**USED:** 6.16, D1.22, D2.1, D5.6, D5.8
**Human refs (from References field):** 6.16
**Jaccard:** 0.200 — AI adds ['D1.22', 'D2.1', 'D5.6', 'D5.8']

## Proposition 6.18
**Statement:** On a given straight line to describe a rectilineal figure similar and similarly situated to a given rectilineal figure.

**Step 1.** Let ABCDE be the given rectilineal figure and FG the given straight line. It is required to describe on FG a rectilineal figure similar and similarly situated to ABCDE, with FG corresponding to side AB.

**Step 2.** Join the diagonals AC and AD of the figure ABCDE, decomposing it into the triangles ABC, ACD, and ADE [P1]. (If the figure has more or fewer sides, the same procedure applies with the appropriate number of triangles.)

**Step 3.** At the point F on the line FG, construct the angle GFH equal to the angle BAC, and at the point G, construct the angle FGH equal to the angle ABC [1.23].

**Step 4.** Since the angles GFH and FGH are respectively equal to the angles BAC and ABC, and the sum of the angles in any triangle equals two right angles [1.32], the remaining angle FHG equals the remaining angle ACB. Therefore triangle FGH is equiangular with triangle ABC.

**Step 5.** Since triangles FGH and ABC are equiangular, the sides about the equal angles are proportional [6.4]. In particular, FG is to AB as FH is to AC, and as GH is to BC.

**Step 6.** At the point F on the line FH, construct the angle HFK equal to the angle CAD, and at the point H, construct the angle FHK equal to the angle ACD [1.23].

**Step 7.** Since the angles HFK and FHK are respectively equal to the angles CAD and ACD, the remaining angle FKH equals the remaining angle ADC [1.32]. Therefore triangle FHK is equiangular with triangle ACD.

**Step 8.** Since triangles FHK and ACD are equiangular, the sides about the equal angles are proportional [6.4]. In particular, FH is to AC as FK is to AD, and as HK is to CD.

**Step 9.** At the point F on the line FK, construct the angle KFL equal to the angle DAE, and at the point K, construct the angle FKL equal to the angle ADE [1.23].

**Step 10.** Since the angles KFL and FKL are respectively equal to the angles DAE and ADE, the remaining angle FLK equals the remaining angle AED [1.32]. Therefore triangle FKL is equiangular with triangle ADE.

**Step 11.** Since triangles FKL and ADE are equiangular, the sides about the equal angles are proportional [6.4]. In particular, FK is to AD as KL is to DE, and as FL is to AE.

**Step 12.** Now from Step 5, FG : AB = FH : AC. From Step 8, FH : AC = HK : CD. Since FG : AB = FH : AC and FH : AC = HK : CD, it follows that FG : AB = HK : CD [5.11]. Similarly, from Step 8, FH : AC = FK : AD, so FG : AB = FK : AD [5.11].

**Step 13.** From Step 11, FK : AD = KL : DE, and since FG : AB = FK : AD (Step 12), it follows that FG : AB = KL : DE [5.11]. Likewise, FK : AD = FL : AE (Step 11), so FG : AB = FL : AE [5.11].

**Step 14.** Combining Steps 5, 12, and 13, all corresponding sides are in the same ratio: FG : AB = GH : BC = HK : CD = KL : DE = FL : AE.

**Step 15.** Now consider the angles. The angle at G in figure FGHKL is angle FGH, which equals angle ABC by construction (Step 3). The angle at H in figure FGHKL is the sum angle FHG + angle FHK. From Step 4, angle FHG = angle ACB, and from Step 7, angle FHK = angle ACD. Therefore the angle at H equals angle ACB + angle ACD = angle BCD in figure ABCDE [CN2]. Similarly, the angle at K in figure FGHKL is the sum angle FKH + angle FKL. From Step 7, angle FKH = angle ADC, and from Step 10, angle FKL = angle ADE. Therefore the angle at K equals angle ADC + angle ADE = angle CDE [CN2].

**Step 16.** The angle at L in figure FGHKL is angle FLK, which equals angle AED by Step 10. The angle at F in figure FGHKL is the sum angle GFH + angle HFK + angle KFL. By construction, these equal angle BAC + angle CAD + angle DAE = angle BAE [CN2].

**Step 17.** Therefore all corresponding angles of FGHKL and ABCDE are severally equal, and the sides about those equal angles are proportional (Step 14). By the definition of similar rectilineal figures [D6.1], figure FGHKL is similar and similarly situated to figure ABCDE.

**Step 18.** Therefore, on the given straight line FG, a rectilineal figure FGHKL has been described similar and similarly situated to the given rectilineal figure ABCDE. Q.E.F.

**USED:** 1.23, 1.32, 5.11, 6.4, CN2, D6.1, P1
**Human refs (from References field):** 1.23, 1.32, 6.4, D6.1
**Jaccard:** 0.571 — AI adds ['5.11', 'CN2', 'P1']

## Proposition 6.19
**Statement:** Similar triangles are to one another in the duplicate ratio of the corresponding sides.

**Step 1.** Let ABC and DEF be similar triangles, with angle ABC equal to angle DEF, and let BC and EF be corresponding sides. Since ABC and DEF are similar, their angles are severally equal and the sides about the equal angles are proportional [D6.1].

**Step 2.** By 6.4, since the triangles are equiangular (having equal angles), the sides about the equal angles are proportional. In particular, AB:DE = BC:EF, where AB, BC are sides about angle ABC and DE, EF are sides about the equal angle DEF [6.4].

**Step 3.** Using 6.11, find a third proportional BG to BC and EF, so that BC:EF = EF:BG [6.11].

**Step 4.** Since BC, EF, BG are three magnitudes in continued proportion (BC:EF = EF:BG), by Definition 5.9 the ratio BC:BG is the duplicate ratio of BC:EF [D5.9].

**Step 5.** From Step 2, AB:DE = BC:EF. From Step 3, BC:EF = EF:BG. Therefore AB:DE = EF:BG, since ratios which are the same with the same ratio are also the same with one another [5.11].

**Step 6.** Now consider triangles ABG and DEF. We have angle ABG equal to angle DEF (since angle ABG is the same as angle ABC, and angle ABC equals angle DEF by similarity). The sides about these equal angles are reciprocally proportional: AB:DE = EF:BG (from Step 5). Therefore, by 6.15, triangle ABG is equal in area to triangle DEF [6.15].

**Step 7.** Triangles ABC and ABG share the same vertex A, and their bases BC and BG lie on the same straight line. Therefore they have the same height from A to line BG. By 6.1, triangle ABC is to triangle ABG as BC is to BG [6.1].

**Step 8.** Since triangle ABG equals triangle DEF (Step 6), triangle ABC has to triangle DEF the same ratio that triangle ABC has to triangle ABG [5.7]. That is, triangle ABC : triangle DEF = triangle ABC : triangle ABG.

**Step 9.** Combining Steps 7 and 8: triangle ABC : triangle DEF = BC : BG. But BC:BG is the duplicate ratio of BC:EF (Step 4). Therefore triangle ABC is to triangle DEF in the duplicate ratio of the corresponding side BC to EF [5.11].

**Step 10.** Hence similar triangles are to one another in the duplicate ratio of the corresponding sides. Q.E.D.

**USED:** 5.11, 5.7, 6.1, 6.11, 6.15, 6.4, D5.9, D6.1
**Human refs (from References field):** 5.11, 5.16, 6.1, 6.11, 6.15, D5.11, D5.9
**Jaccard:** 0.500 — AI adds ['5.7', '6.4', 'D6.1']; Human adds ['5.16', 'D5.11']

## Proposition 6.20
**Statement:** Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate of that which the corresponding side has to the corresponding  side.

**Step 1.** Let ABCDE and FGHKL be similar polygons, and let AB correspond to FG. Since the polygons are similar, by D6.1 their angles are severally equal and the sides about the equal angles are proportional. Thus angle A = angle F, angle B = angle G, angle C = angle H, angle D = angle K, angle E = angle L, and AB:FG = BC:GH = CD:HK = DE:KL = EA:LF.

**Step 2.** Join AC, AD in polygon ABCDE and FH, FK in polygon FGHKL. These diagonals divide ABCDE into triangles ABC, ACD, ADE and FGHKL into triangles FGH, FHK, FKL. Thus each polygon is divided into three triangles, equal in multitude.

**Step 3.** We show triangle ABC is similar to triangle FGH. Since the polygons are similar, angle ABC = angle FGH, and AB:BC = FG:GH. Therefore by 6.6, triangle ABC is equiangular with triangle FGH, and hence similar.

**Step 4.** Since triangle ABC is similar to triangle FGH, angle BCA = angle GHF and BC:CA = GH:HF by D6.1.

**Step 5.** We show triangle ACD is similar to triangle FHK. Since angle BCD = angle GHK (from the similar polygons) and angle BCA = angle GHF (Step 4), subtracting by CN3 gives angle ACD = angle FHK.

**Step 6.** From the similar polygons, BC:CD = GH:HK. From the similar triangles ABC and FGH, BC:CA = GH:HF (Step 4). Therefore by 5.22 (ex aequali), CA:CD = HF:HK.

**Step 7.** Since angle ACD = angle FHK (Step 5) and CA:CD = HF:HK (Step 6), by 6.6 triangle ACD is similar to triangle FHK.

**Step 8.** Since triangle ACD is similar to triangle FHK, angle CDA = angle HKF and CD:DA = HK:KF by D6.1.

**Step 9.** We show triangle ADE is similar to triangle FKL. Since angle CDE = angle HKL (from the similar polygons) and angle CDA = angle HKF (Step 8), subtracting by CN3 gives angle ADE = angle FKL.

**Step 10.** From the similar polygons, CD:DE = HK:KL. From the similar triangles ACD and FHK, CD:DA = HK:KF (Step 8). Therefore by 5.22 (ex aequali), DA:DE = KF:KL.

**Step 11.** Since angle ADE = angle FKL (Step 9) and DA:DE = KF:KL (Step 10), by 6.6 triangle ADE is similar to triangle FKL.

**Step 12.** Thus the similar polygons ABCDE and FGHKL have been divided into similar triangles (ABC ~ FGH, ACD ~ FHK, ADE ~ FKL) equal in multitude (three each).

**Step 13.** We now show the triangles are in the same ratio as the wholes. Since triangle ABC is similar to triangle FGH, by 6.19 triangle ABC : triangle FGH is the duplicate ratio of BC:GH.

**Step 14.** Since triangle ACD is similar to triangle FHK, by 6.19 triangle ACD : triangle FHK is the duplicate ratio of CD:HK.

**Step 15.** Since the polygons are similar, BC:GH = CD:HK. Therefore the duplicate ratio of BC:GH equals the duplicate ratio of CD:HK, so triangle ABC : triangle FGH = triangle ACD : triangle FHK.

**Step 16.** Since triangle ADE is similar to triangle FKL, by 6.19 triangle ADE : triangle FKL is the duplicate ratio of DE:KL.

**Step 17.** Since the polygons are similar, BC:GH = DE:KL. Therefore the duplicate ratio of BC:GH equals the duplicate ratio of DE:KL, so triangle ABC : triangle FGH = triangle ADE : triangle FKL.

**Step 18.** From Steps 15 and 17, triangle ABC : triangle FGH = triangle ACD : triangle FHK = triangle ADE : triangle FKL. Since the three ratios are all equal, by 5.12 (alternando) we can also express this as: triangle ABC : triangle ACD = triangle FGH : triangle FHK, and similarly for the other pairs.

**Step 19.** Since triangle ABC : triangle FGH = triangle ACD : triangle FHK = triangle ADE : triangle FKL, by 5.12 we have that as one antecedent is to its consequent, so is the sum of the antecedents to the sum of the consequents. That is, triangle ABC : triangle FGH = (triangle ABC + triangle ACD + triangle ADE) : (triangle FGH + triangle FHK + triangle FKL), by 5.12 combined with the repeated application of equal ratios. More precisely, since all three ratios are equal, by applying 5.12 and then the additive property of equal ratios, as one of the triangles is to the corresponding triangle, so is the whole polygon to the whole polygon.

**Step 20.** But triangle ABC + triangle ACD + triangle ADE = polygon ABCDE, and triangle FGH + triangle FHK + triangle FKL = polygon FGHKL. Therefore triangle ABC : triangle FGH = polygon ABCDE : polygon FGHKL. This shows the triangles are in the same ratio as the wholes.

**Step 21.** Finally, we show the polygon has to the polygon the duplicate ratio of corresponding sides. From Step 13, triangle ABC : triangle FGH is the duplicate ratio of BC:GH. From Step 20, polygon ABCDE : polygon FGHKL = triangle ABC : triangle FGH. Therefore polygon ABCDE : polygon FGHKL is the duplicate ratio of BC:GH, by CN1.

**Step 22.** Since BC:GH = AB:FG (from the similar polygons), the duplicate ratio of BC:GH equals the duplicate ratio of AB:FG. Therefore polygon ABCDE : polygon FGHKL is the duplicate ratio of the corresponding side AB to the corresponding side FG.

**Step 23.** Therefore similar polygons are divided into similar triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate of that which the corresponding side has to the corresponding side. Q.E.F.

**USED:** 5.12, 5.22, 6.19, 6.6, CN1, CN3, D5.9, D6.1
**Human refs (from References field):** 1.32, 5.12, 5.22, 6.1, 6.19, 6.4, 6.6, D6.1
**Jaccard:** 0.455 — AI adds ['CN1', 'CN3', 'D5.9']; Human adds ['1.32', '6.1', '6.4']

## Proposition 6.21
**Statement:** Figures which are similar to the same rectilineal figure are also similar to one another.

**Step 1.** Let A and B be two rectilineal figures, each similar to the same rectilineal figure C. We must show that A is similar to B.

**Step 2.** Since A is similar to C, by D6.1 the angles of A are severally equal to the corresponding angles of C, and the sides about the equal angles are proportional. That is, the angles of A equal the corresponding angles of C, and for each pair of corresponding sides, the ratio of a side of A to the corresponding side of C is the same.

**Step 3.** Since B is similar to C, by D6.1 the angles of B are severally equal to the corresponding angles of C, and the sides about the equal angles are proportional.

**Step 4.** Now consider any angle of A that equals a corresponding angle of C (from Step 2), and the same angle of C equals the corresponding angle of B (from Step 3). By CN1, the angle of A equals the corresponding angle of B. This holds for every pair of corresponding angles, so A and B have their angles severally equal.

**Step 5.** It remains to show that the sides of A about the equal angles are proportional to the corresponding sides of B. Consider any pair of corresponding sides. From the similarity of A to C, the ratio of a side of A about a given angle to the corresponding side of C about the equal angle is a definite ratio. From the similarity of B to C, the ratio of the corresponding side of B to the corresponding side of C is also a definite ratio.

**Step 6.** From the similarity A ~ C, for sides a1, a2 of A about an angle and corresponding sides c1, c2 of C about the equal angle, we have a1 : c1 :: a2 : c2 (D6.1). From the similarity B ~ C, for corresponding sides b1, b2 of B and the same sides c1, c2 of C, we have b1 : c1 :: b2 : c2 (D6.1).

**Step 7.** From Step 6, a1 : c1 :: a2 : c2. By 5.16 (inverse ratio / alternando — taking the inverse), we obtain c1 : b1 :: c2 : b2 from the proportion b1 : c1 :: b2 : c2 by inversion. That is, c1 : b1 :: c2 : b2.

**Step 8.** We now have a1 : c1 :: a2 : c2 (from A ~ C) and c1 : b1 :: c2 : b2 (from Step 7). By 5.22 (ratio ex aequali), combining these two proportions, a1 : b1 :: a2 : b2.

**Step 9.** The argument in Steps 5 through 8 applies to every set of corresponding sides about equal angles in A and B. Therefore the sides of A about the equal angles are proportional to the corresponding sides of B.

**Step 10.** Since A and B have their angles severally equal (Step 4) and the sides about the equal angles proportional (Step 9), A is similar to B by D6.1. Therefore figures which are similar to the same rectilineal figure are also similar to one another. Q.E.D.

**USED:** 5.16, 5.22, CN1, D6.1
**Human refs (from References field):** D6.1
**Jaccard:** 0.250 — AI adds ['5.16', '5.22', 'CN1']

## Proposition 6.22
**Statement:** If four straight lines be proportional, the rectilineal figures similar and similarly described upon them will also be proportional; and, if the rectilineal figures similar and similarly described upon them be proportional, the straight lines will themselves also be proportional.

**Part I (Forward direction): If four straight lines are proportional, the similar and similarly described figures upon them are also proportional.**

**Step 1.** Let AB, CD, EF, GH be four straight lines such that AB : CD :: EF : GH. Let S be the rectilineal figure described on AB similar and similarly situated to that on CD, and let S' be the rectilineal figure described on EF similar and similarly situated to that on GH. All four figures are similar and similarly described. We must show that S(AB) : S(CD) :: S(EF) : S(GH).

**Step 2.** By 6.11, find a third proportional X to AB and CD, so that AB : CD :: CD : X. Then by D5.9, AB has to X the duplicate ratio of that which AB has to CD.

**Step 3.** By 6.11, find a third proportional Y to EF and GH, so that EF : GH :: GH : Y. Then by D5.9, EF has to Y the duplicate ratio of that which EF has to GH.

**Step 4.** Since AB : CD :: EF : GH (given), and AB : CD :: CD : X (Step 2), and EF : GH :: GH : Y (Step 3), it follows by 5.11 that CD : X :: GH : Y.

**Step 5.** We now have AB : CD :: EF : GH (given) and CD : X :: GH : Y (Step 4). Therefore, by 5.22 (ex aequali), AB : X :: EF : Y.

**Step 6.** By 6.20, since the figures on AB and CD are similar, S(AB) : S(CD) is the duplicate ratio of AB to CD, which is the ratio AB : X (Steps 2 and D5.9). Therefore S(AB) : S(CD) :: AB : X.

**Step 7.** By 6.20, since the figures on EF and GH are similar, S(EF) : S(GH) is the duplicate ratio of EF to GH, which is the ratio EF : Y (Steps 3 and D5.9). Therefore S(EF) : S(GH) :: EF : Y.

**Step 8.** Since S(AB) : S(CD) :: AB : X (Step 6), and AB : X :: EF : Y (Step 5), by 5.11, S(AB) : S(CD) :: EF : Y. Since EF : Y :: S(EF) : S(GH) (Step 7), by 5.11 again, S(AB) : S(CD) :: S(EF) : S(GH). This completes Part I.

**Part II (Converse): If the similar and similarly described figures upon four straight lines are proportional, the straight lines are themselves proportional.**

**Step 9.** Let AB, CD, EF, GH be four straight lines with similar and similarly described rectilineal figures upon them, and suppose S(AB) : S(CD) :: S(EF) : S(GH). We must show AB : CD :: EF : GH.

**Step 10.** By 6.12, find a fourth proportional GH' to AB, CD, EF, so that AB : CD :: EF : GH'.

**Step 11.** On GH', describe a rectilineal figure S(GH') similar and similarly situated to S(GH) (which is possible by 6.18). Since AB : CD :: EF : GH' (Step 10), by Part I (Steps 1-8), S(AB) : S(CD) :: S(EF) : S(GH').

**Step 12.** But S(AB) : S(CD) :: S(EF) : S(GH) by hypothesis (Step 9). Therefore by 5.11, S(EF) : S(GH) :: S(EF) : S(GH'). By 5.9, S(GH) = S(GH').

**Step 13.** Now S(GH) and S(GH') are similar rectilineal figures (both being similar and similarly described to the same figure), and they are equal (Step 12). By 6.20, S(GH) : S(GH') is the duplicate ratio of GH : GH'. Since S(GH) = S(GH'), this duplicate ratio is the ratio of equality. By 6.11, take the third proportional Z to GH and GH', so GH : GH' :: GH' : Z, and the duplicate ratio of GH to GH' is GH : Z (D5.9). Since this ratio equals the ratio of equality, GH = Z. But GH : GH' :: GH' : GH (substituting GH for Z), and so by 5.9, GH = GH'.

**Step 14.** Since GH = GH', and AB : CD :: EF : GH' (Step 10), we conclude AB : CD :: EF : GH. This completes Part II.

Therefore, if four straight lines are proportional, the rectilineal figures similar and similarly described upon them are also proportional; and if the similar figures are proportional, the straight lines are themselves proportional. Q.E.D.

**USED:** 5.11, 5.22, 5.9, 6.11, 6.12, 6.18, 6.20, D5.9
**Human refs (from References field):** 5.11, 5.22, 5.9, 6.11, 6.12, 6.18, 6.19
**Jaccard:** 0.667 — AI adds ['6.20', 'D5.9']; Human adds ['6.19']

## Proposition 6.23
**Statement:** Equiangular parallelograms have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let ABCD and CEFG be equiangular parallelograms, with angle BCD equal to angle ECG. We wish to show that parallelogram ABCD has to parallelogram CEFG the ratio compounded of the ratios of the sides, that is, the ratio compounded of BC to CG and DC to CE.

**Step 2.** Place the parallelograms so that BC is in a straight line with CG. Since angle BCD equals angle ECG, add angle DCE to each. Then angle BCD plus angle DCE equals angle ECG plus angle DCE. Now since BCG is a straight line, angle BCD plus angle DCG equals two right angles [1.13]. Therefore angle ECG plus angle DCE equals angle BCD plus angle DCE equals angle DCG, and so angle DCE plus angle ECG equals two right angles. By 1.14, since the angles DCE and ECG on either side of C at point C on line CG sum to two right angles, the lines DC and CE are in a straight line.

**Step 3.** Complete the parallelogram DCGK, by drawing through G a line parallel to DC [1.31] and through D a line parallel to CG [1.31], letting these lines meet at K. Then DCGK is a parallelogram with sides DC and CG.

**Step 4.** The parallelograms ABCD and DCGK are between the same parallels, namely the line through B, C, G and the line through A, D, K (since AD is parallel to BC by definition of parallelogram ABCD, and DK is parallel to CG by construction, and BC and CG are in a straight line, so AD and DK lie along the same straight line, meaning A, D, K are collinear and the line through them is parallel to BCG). They have the same height, the perpendicular distance between these parallels. By 6.1, parallelogram ABCD is to parallelogram DCGK as their bases BC is to CG. That is, ABCD : DCGK = BC : CG.

**Step 5.** The parallelograms DCGK and CEFG are between the same parallels, namely the line through C, G and the line through D, K and E, F (since DC and CE are in a straight line by Step 2, and KG is parallel to DC by construction of parallelogram DCGK, and GF is parallel to CE by definition of parallelogram CEFG; since DC and CE are in a straight line, KG and GF are both parallel to the same line DCE, so K, G, F... but more precisely: DCGK has base DC and CEFG has base CE, both measured along the line DCE, and both parallelograms have their opposite sides KG and GF respectively along the parallel through G). By 6.1, parallelogram DCGK is to parallelogram CEFG as DC is to CE. That is, DCGK : CEFG = DC : CE.

**Step 6.** Now the ratio ABCD : CEFG is compounded of the ratios ABCD : DCGK and DCGK : CEFG, since DCGK is the intermediate magnitude [D6.5]. From Step 4, ABCD : DCGK = BC : CG, and from Step 5, DCGK : CEFG = DC : CE. Therefore the ratio ABCD : CEFG is compounded of the ratios BC : CG and DC : CE [D6.5].

**Step 7.** But BC : CG and DC : CE are the ratios of the sides of the equiangular parallelograms ABCD and CEFG about the equal angles. Therefore equiangular parallelograms have to one another the ratio compounded of the ratios of their sides. Q.E.D.

**USED:** 1.13, 1.14, 1.29, 1.31, 1.34, 6.1, D6.5
**Human refs (from References field):** 5.11, 6.1, 6.12
**Jaccard:** 0.111 — AI adds ['1.13', '1.14', '1.29', '1.31', '1.34', 'D6.5']; Human adds ['5.11', '6.12']

## Proposition 6.24
**Statement:** In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.

**Step 1.** Let ABCD be a parallelogram with diameter (diagonal) AC, and let AEKH and KFCG be parallelograms about the diameter, so that EK and HK lie along directions parallel to BC and CD respectively, with K on AC, and similarly GK and FK are parallel to sides of ABCD. We must show that AEKH and KFCG are each similar to ABCD and to one another.

**Step 2.** Since ABCD is a parallelogram, AB is parallel to DC and AD is parallel to BC [D1.22, 1.34].

**Step 3.** Since AEKH is a parallelogram about the diameter AC, its sides AH and EK are parallel to AD and BC respectively, and its sides AE and HK are parallel to AB and DC respectively. This follows from the construction of parallelograms about the diameter.

**Step 4.** Since AE is parallel to HK and both lie along the line AB and DC respectively, and AH is parallel to EK and both lie along AD and BC respectively, the angles of AEKH equal the corresponding angles of ABCD. Specifically, since AB is parallel to DC, and AE lies along AB while HK is parallel to AB, we have by 1.29 that angle EAH equals angle BAD (they are the same angle, since E lies on AB and H lies on AD). Likewise angle AEK equals angle ABC, since AE lies on AB and EK is parallel to BC, so the transversal BE (along AB) cutting the parallels EK and BC gives angle AEK equal to angle ABC by 1.29. Similarly angle EKH equals angle BCD and angle KHA equals angle CDA by the same reasoning.

**Step 5.** Thus AEKH is equiangular with ABCD; that is, their angles taken in order are severally equal.

**Step 6.** Now consider triangles AEK and ABC. Since EK is parallel to BC, and both are cut by transversal AB (through A and B with E on AB) and by transversal AC (the diameter), triangle AEK is equiangular with triangle ABC. For angle EAK equals angle BAC (they are the same angle), angle AEK equals angle ABC by 1.29 (since EK is parallel to BC and AB is a transversal), and therefore angle AKE equals angle ACB by 1.32.

**Step 7.** Since triangles AEK and ABC are equiangular, by 6.4 the sides about the equal angles are proportional: AE/AB = AK/AC = EK/BC.

**Step 8.** Similarly, consider triangles AHK and ADC. Since HK is parallel to DC (both being parallel to AB and DC respectively — more precisely, since AEKH is a parallelogram about the diameter, HK is parallel to DC), and AH lies along AD, triangle AHK is equiangular with triangle ADC. By 6.4, AH/AD = AK/AC = HK/DC.

**Step 9.** From Steps 7 and 8, we have AE/AB = AK/AC and AH/AD = AK/AC. Therefore AE/AB = AH/AD by CN1 (both equal AK/AC). Also EK/BC = AK/AC = HK/DC, so EK/BC = HK/DC.

**Step 10.** Since ABCD is a parallelogram, AB = CD and BC = AD by 1.34. Since AEKH is a parallelogram, AE = HK and AH = EK by 1.34. From AE/AB = AK/AC = EK/BC (Step 7), we get AE/AB = EK/BC. Since HK = AE and DC = AB, we also have HK/DC = AE/AB. And since EK = AH and AD = BC, we get AH/AD = EK/BC. Thus the sides of AEKH about each angle are proportional to the corresponding sides of ABCD about the equal angle.

**Step 11.** Specifically, assembling the ratios: AE/AB = AH/AD (the sides about the equal angles DAB and HAE); AE/AB = EK/BC (the sides about angles ABC and AEK); and the remaining pairs follow from the parallelogram equalities. Therefore the sides about the equal angles of AEKH and ABCD are proportional.

**Step 12.** Since AEKH and ABCD are equiangular (Step 5) and the sides about the equal angles are proportional (Step 11), AEKH is similar to ABCD by D6.1.

**Step 13.** By entirely analogous reasoning applied to parallelogram KFCG about the diameter: since KF is parallel to AB and KG is parallel to AD, the angles of KFCG are severally equal to the corresponding angles of ABCD by 1.29. Considering triangles KFC and ABC (where KF is parallel to AB, giving triangle KFC equiangular with triangle BAC by 1.29 and 1.32), and triangles KGC and ADC (where KG is parallel to AD), we obtain by 6.4 that CF/CB = CK/CA = KF/AB and CG/CD = CK/CA = KG/AD. The same argument as in Steps 9 through 11 shows the sides of KFCG about each equal angle are proportional to the corresponding sides of ABCD.

**Step 14.** Therefore KFCG is similar to ABCD by D6.1.

**Step 15.** Since AEKH is similar to ABCD (Step 12) and KFCG is similar to ABCD (Step 14), AEKH is similar to KFCG by 6.21.

**Step 16.** Therefore, in any parallelogram the parallelograms about the diameter are similar both to the whole and to one another. Q.E.F.

**USED:** 1.29, 1.32, 1.34, 6.21, 6.4, CN1, D6.1
**Human refs (from References field):** 5.16, 5.18, 5.22, 6.2, 6.21, D6.1
**Jaccard:** 0.182 — AI adds ['1.29', '1.32', '1.34', '6.4', 'CN1']; Human adds ['5.16', '5.18', '5.22', '6.2']

## Proposition 6.25
**Statement:** To construct one and the same figure similar to a given rectilineal figure and equal to another given rectilineal figure.

**Step 1.** Let ABC be the given rectilineal figure to which the figure to be constructed must be similar, and let D be the given rectilineal figure to which it must be equal. Let BC be a side of ABC.

**Step 2.** On BC, apply the parallelogram BE equal to the rectilineal figure ABC [1.45], and on CE, apply the parallelogram CM equal to D in the angle FCE equal to the angle CBL [1.45]. Then BC and CF are in a straight line, and also LE and EM are in a straight line [1.14, 1.29].

**Step 3.** Take GH as a mean proportional between BC and CF [6.13].

**Step 4.** On GH, describe the rectilineal figure KGH similar and similarly situated to the rectilineal figure ABC [6.18].

**Step 5.** Since BC : GH = GH : CF, it follows that BC has to CF the duplicate ratio of that which BC has to GH [D5.9].

**Step 6.** But the ratio of BC to CF equals the ratio of the parallelogram BE to the parallelogram CM, since BE and CM have the same height [6.1].

**Step 7.** Therefore the parallelogram BE has to the parallelogram CM the duplicate ratio of that which BC has to GH.

**Step 8.** But the ratio of the rectilineal figure ABC to the rectilineal figure KGH is the duplicate ratio of BC to GH, since similar rectilineal figures are to one another in the duplicate ratio of their corresponding sides [6.20].

**Step 9.** Therefore the parallelogram BE is to the parallelogram CM as the rectilineal figure ABC is to the rectilineal figure KGH [5.11].

**Step 10.** But the parallelogram BE is equal to the rectilineal figure ABC [Step 2]. Therefore the parallelogram CM is equal to the rectilineal figure KGH [5.14].

**Step 11.** But the parallelogram CM is equal to D [Step 2]. Therefore the rectilineal figure KGH is also equal to D [CN1].

**Step 12.** And KGH is also similar to ABC [Step 4].

**Step 13.** Therefore one and the same figure KGH has been constructed similar to the given rectilineal figure ABC and equal to the other given rectilineal figure D. Q.E.F.

**USED:** 1.14, 1.29, 1.45, 5.11, 5.14, 6.1, 6.13, 6.18, 6.20, CN1, D5.9
**Human refs (from References field):** 1.44, 1.45, 5.16, 6.1, 6.13, 6.18, 6.19
**Jaccard:** 0.286 — AI adds ['1.14', '1.29', '5.11', '5.14', '6.20', 'CN1', 'D5.9']; Human adds ['1.44', '5.16', '6.19']

## Proposition 6.26
**Statement:** If from a parallelogram there be taken away a parallelogram similar and similarly situated to the whole and having a common angle with it, it is about the same diameter with the whole.

**Step 1.** Let ABCD be a parallelogram, and let AEFG be a parallelogram similar and similarly situated to ABCD, having the common angle at A with it, where E lies on AB and G lies on AD. We are to prove that AEFG is about the same diameter as ABCD.

**Step 2.** Draw the diagonal AC of parallelogram ABCD [P1]. Suppose, for the sake of contradiction, that AEFG is not about the diameter AC, that is, the vertex F (opposite to A in AEFG) does not lie on AC.

**Step 3.** Since AC is the diagonal of ABCD, and E lies on AB between A and B, and G lies on AD between A and D, the line AC passes through the interior of the region bounded by AE, EF, GF, and AG. Let AC meet one of the sides EF or GF, and through a point on AC lying within this region, draw lines parallel to AB and AD [1.31], thereby constructing a parallelogram AKHL about the diameter AC, where K lies on AB, H lies on AD, and the vertex L (opposite to A) lies on the diagonal AC.

**Step 4.** By Proposition 6.24, since AKHL is a parallelogram about the diameter of ABCD, AKHL is similar to ABCD [6.24].

**Step 5.** But AEFG is also similar to ABCD (given). Therefore AEFG is similar to AKHL [6.21], since figures similar to the same rectilineal figure are also similar to one another.

**Step 6.** Since AEFG is similar to ABCD and they share angle A, the sides about the equal angle are proportional [D6.1]: AE : AB = AG : AD.

**Step 7.** Since AKHL is similar to ABCD (Step 4) and they share angle A, similarly [D6.1]: AK : AB = AH : AD.

**Step 8.** From Steps 6 and 7, AE : AB = AG : AD and AK : AB = AH : AD. By alternando [5.16] applied to AE : AB = AG : AD, we obtain AE : AG = AB : AD. Similarly from AK : AB = AH : AD, we obtain AK : AH = AB : AD. Therefore AE : AG = AK : AH [5.11, CN1], and by alternando again [5.16], AE : AK = AG : AH.

**Step 9.** Now consider triangle AKL, where K is on AB and L is on AC. The line through E (which lies on ray AK, since both K and E are on AB) drawn parallel to KL meets AL at a point; call it F'. Since EF' is parallel to KL and E lies on AK (or AK produced), by Proposition 6.2, the sides of triangle AKL are cut proportionally: AE : AK = AF' : AL.

**Step 10.** Similarly, consider triangle AHL, where H is on AD and L is on AC. The line through G (which lies on ray AH, since both H and G are on AD) drawn parallel to HL meets AL at a point; call it F''. Since GF'' is parallel to HL and G lies on AH (or AH produced), by Proposition 6.2: AG : AH = AF'' : AL.

**Step 11.** From Step 8, AE : AK = AG : AH. From Step 9, AE : AK = AF' : AL. From Step 10, AG : AH = AF'' : AL. Since AE : AK = AG : AH [Step 8], it follows that AF' : AL = AF'' : AL [5.11, CN1]. Therefore AF' = AF'', which means F' and F'' are the same point on line AL.

**Step 12.** Now, the line through E parallel to AD (which is the same as the line through E parallel to KL, since KL is parallel to AH which lies along AD) meets AL at F'. And the line through G parallel to AB (which is the same as the line through G parallel to HL, since HL is parallel to AK which lies along AB) meets AL at F''. Since F' = F'' (Step 11), call this common point F*.

**Step 13.** But in parallelogram AEFG, the vertex F is determined as the intersection of the line through E parallel to AG (i.e., parallel to AD) and the line through G parallel to AE (i.e., parallel to AB). These are precisely the same two lines identified in Step 12. Therefore F = F*, and F lies on line AL, which is part of line AC.

**Step 14.** This means F lies on the diagonal AC, so AEFG is about the diameter AC. This contradicts our assumption in Step 2 that AEFG is not about the diameter AC.

**Step 15.** Therefore the assumption is false, and the parallelogram AEFG is about the same diameter as the parallelogram ABCD. Q.E.D.

**USED:** 1.31, 5.11, 5.16, 6.2, 6.21, 6.24, CN1, D6.1, P1
**Human refs (from References field):** 1.31, 5.11, 5.9, 6.24
**Jaccard:** 0.300 — AI adds ['5.16', '6.2', '6.21', 'CN1', 'D6.1', 'P1']; Human adds ['5.9']

## Proposition 6.27
**Statement:** Of all the parallelograms applied to the same straight line and deficient by parallelogrammic figures similar and similarly situated to that described on the half of the straight line, that parallelogram is greatest which is applied to the half of the straight line and is similar to the defect.

**Step 1.** Let AB be the given straight line, and let it be bisected at the point C. On CB let the parallelogram CE be described, so that CE is the parallelogram applied to the half of the straight line. The defect of CE (the parallelogrammic figure by which the applied parallelogram falls short of the whole line AB) is the parallelogram on the remaining part; call it the parallelogram CF, which is similar and similarly situated to CE by construction on the half.

**Step 2.** Let any other parallelogram AF be applied to the straight line AB, deficient by a parallelogram KF that is similar and similarly situated to CF. Since AF is applied to a part of AB different from the half CB, the point of division for AF is at some point other than C.

**Step 3.** Since CF is a parallelogram described on CB and KF is similar and similarly situated to CF, and moreover CF and KF share a common angle (both being on the same side and similarly situated), by Proposition 6.26, the parallelograms CF and KF are about the same diagonal. Let this diagonal be drawn and call it CG.

**Step 4.** The diagonal CG determines a larger parallelogram, call it ADGB, of which CF and KF are parallelograms about the diagonal. By Proposition 1.43, in any parallelogram the complements of the parallelograms about the diagonal are equal to one another.

**Step 5.** Now in the parallelogram ADGB about the diagonal CG, the parallelogram CF has a complement that is the parallelogram CE (the parallelogram applied to the half CB). The parallelogram KF, being also about the diagonal CG but smaller than CF (since KF is similar to CF but has a shorter corresponding side), has a complement that is the parallelogram AF.

**Step 6.** Since KF is contained within CF (being similar and similarly situated to CF, sharing a common angle, and lying about the same diagonal, but on a shorter base), the complement of KF in the whole parallelogram ADGB includes the complement of CF plus additional area. That is, AF (the complement of KF) together with KF makes up the same region as CE (the complement of CF) together with CF only if they coincide, which they do not since AF is not applied to the half.

**Step 7.** More precisely, the complement of CF is CE, and the complement of KF is AF. The gnomon formed by removing KF from CF, together with AF, makes up CE together with the difference. Since CF is larger than KF (CF contains KF as a proper part, because KF is similar to CF but on a strictly shorter base), and by Proposition 1.43 the complement of CF equals CE while the complement of KF equals AF, we observe that CE contains AF as a part: the region CE includes AF plus the gnomon region that is the difference between CF and KF transferred via the complement structure.

**Step 8.** Specifically, the whole parallelogram ADGB equals CF plus CE plus the two complements' shared boundary regions. Equally, the whole parallelogram ADGB equals KF plus AF plus the remaining complements. Since CF contains KF (CF is the larger, KF the smaller, both about the diagonal), the complement AF is contained within the complement CE together with the gnomon. Therefore CE is greater than AF by Common Notion 5, since the whole is greater than the part.

**Step 9.** Therefore, of all the parallelograms applied to the same straight line AB and deficient by parallelogrammic figures similar and similarly situated to that described on the half of the straight line, the parallelogram CE applied to the half CB is greatest. Q.E.D.

**USED:** 1.43, 6.26, CN5
**Human refs (from References field):** 1.36, 1.43, 6.26
**Jaccard:** 0.500 — AI adds ['CN5']; Human adds ['1.36']

## Proposition 6.28
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and deficient by a parallelogrammic figure similar to a given one: thus the given rectilineal figure must not be greater than the parallelogram described on the half of the straight line and similar to the defect.

**Step 1.** Let AB be the given straight line, C the given rectilineal figure to which the applied parallelogram must be equal, and D the given parallelogram to which the defect is to be similar. It is required to apply to AB a parallelogram equal to C and deficient by a parallelogrammic figure similar to D. The condition is that C must not be greater than the parallelogram described on the half of AB and similar to the defect D.

**Step 2.** Bisect AB at the point E [1.10]. On EB, describe the parallelogram EBFG similar and similarly situated to D [6.18]. Then by the hypothesis (the diorismos), the rectilineal figure C is not greater than the parallelogram EBFG.

**Step 3.** Case 1: If C is equal to the parallelogram EBFG, then the parallelogram EBFG has been applied to the half EB of the straight line AB, is equal to the given rectilineal figure C, and is deficient from the whole line AB by the parallelogram on the other half EA, which is similar to EBFG and hence similar to D (since a congruent copy on the equal segment EA is similar to D). Thus the problem is solved in this case.

**Step 4.** Case 2: Suppose C is less than the parallelogram EBFG. Then EBFG is greater than C.

**Step 5.** Construct a parallelogram KLMN equal to the excess by which EBFG exceeds C, and similar and similarly situated to D [6.25]. Since D is similar to EBFG [by construction in Step 2], KLMN is also similar to EBFG [6.21].

**Step 6.** Since EBFG is greater than KLMN (because EBFG exceeds C by exactly KLMN, and C is positive), EBFG is greater than KLMN. Therefore the side GE is greater than the corresponding side KL, and the side GF is greater than the corresponding side KM [since similar parallelograms with the greater having greater area must have greater corresponding sides].

**Step 7.** Make GO equal to KL and GP equal to KM [1.3], placing these along GE and GF respectively, so that GO falls on GE and GP falls on GF. Complete the parallelogram OGPQ [1.31, P1]. Then OGPQ is equal and similar to KLMN, since it has the same corresponding sides (GO = KL, GP = KM) and the same angles [by construction, OGPQ is similar and similarly situated to KLMN].

**Step 8.** But KLMN is similar to EBFG [Step 5], so OGPQ is similar to EBFG [6.21]. Therefore the parallelogram OGPQ is about the same diameter as EBFG [6.26].

**Step 9.** Let GQB be the diameter of both OGPQ and EBFG. Complete the figure. Since EBFG equals C plus KLMN [Step 5], and KLMN equals OGPQ [Step 7], we have EBFG equals C plus OGPQ. Subtracting OGPQ from both sides, the gnomon (that is, the L-shaped region of EBFG remaining after removing OGPQ) equals C [CN3].

**Step 10.** Now since the complement of a parallelogram about the diameter equals the other complement [1.43], the parallelogram TE (the complement on one side of the diameter) equals the parallelogram PQ-complement (the complement on the other side). Adding OGPQ to the complement on the PQ side, we see that the whole parallelogram TS (applied to the segment AE and extending along AB) relates to the gnomon. Specifically, the gnomon consisting of the region EBFG minus OGPQ equals the complement TE plus the region between, which together form the applied parallelogram on the portion of AB from A up to a certain point.

**Step 11.** More precisely, since the gnomon of EBFG around the interior parallelogram OGPQ equals C [Step 9], and the gnomon is composed of the two complements and OGPQ's supplementary regions, we use the property that the complement on one side of the diameter equals the complement on the other side [1.43]. The parallelogram applied to the segment AS of line AB (where S is determined by the construction) equals the gnomon, which equals C.

**Step 12.** The deficiency from the full line AB is the parallelogram on the remaining segment SB. This parallelogram on SB is similar to OGPQ [6.24, since the parallelograms about the diameter of EBFG are similar both to the whole and to one another], and OGPQ is similar to D [Steps 5 and 7, via 6.21]. Therefore the defect is similar to D.

**Step 13.** Thus we have applied to the given straight line AB a parallelogram (on segment AS) equal to the given rectilineal figure C, deficient by a parallelogrammic figure (on segment SB) similar to the given parallelogram D.

**Step 14.** Therefore, to a given straight line there has been applied a parallelogram equal to a given rectilineal figure and deficient by a parallelogrammic figure similar to a given one, subject to the necessary condition that the given figure not be greater than the parallelogram on the half of the line similar to the defect. Q.E.F.

**USED:** 1.10, 1.3, 1.31, 1.43, 6.18, 6.21, 6.24, 6.25, 6.26, 6.27, CN3, P1
**Human refs (from References field):** 1.36, 6.18, 6.21, 6.25, 6.26
**Jaccard:** 0.308 — AI adds ['1.10', '1.3', '1.31', '1.43', '6.24', '6.27', 'CN3', 'P1']; Human adds ['1.36']

## Proposition 6.29
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and exceeding by a parallelogrammic figure similar to a given one.

**Step 1.** Let AB be the given straight line, C the given rectilineal figure, and D the given parallelogram to which the excess is to be similar. It is required to apply to AB a parallelogram equal to C and exceeding by a parallelogrammic figure similar to D.

**Step 2.** Bisect AB at E [1.10]. On EB, describe the parallelogram EBFG similar and similarly situated to D [6.18].

**Step 3.** By 6.25, construct a parallelogram KH equal to the sum of EBFG and C, and similar to D. Since EBFG is similar to D, and KH is similar to D, it follows that KH is similar to EBFG [6.21].

**Step 4.** Let the side KE of KH correspond to the side EF of EBFG, and let the side EH of KH correspond to the side EB of EBFG. Since KH equals the sum of EBFG and C, KH is greater than EBFG [CN5]. Therefore the side KE is greater than EF and the side EH is greater than EB [6.22, D6.1].

**Step 5.** Produce FE to L so that EL equals KE, and produce EB to M so that EM equals EH [P2, P1]. Complete the parallelogram LEMN. Then LEMN is similar to KH, since the corresponding sides are equal: LE = KE and EM = EH. Since KH is similar to D, LEMN is similar to D [6.21].

**Step 6.** Now since EF is part of EL and EB is part of EM, the parallelogram EBFG shares an angle at E with LEMN and has its sides along the same lines as LEMN. Since EBFG is similar to LEMN (both being similar to D), and shares the angle at E with LEMN, EBFG is about the same diameter with LEMN [6.26].

**Step 7.** Let the diameter of LEMN (and of EBFG) be drawn, and let the figure be completed. Since EBFG is the parallelogram about the diameter, let the complement parallelograms be identified. By 1.43, the complements of the parallelograms about the diameter in LEMN are equal to each other. The gnomon composed of EBFG together with these complements, when subtracted from LEMN, leaves the excess parallelogram on the extension of AB.

**Step 8.** More precisely, since LEMN is the whole parallelogram and EBFG is the parallelogram about the diameter, the gnomon formed around EBFG within LEMN equals LEMN minus EBFG. But LEMN equals KH (by construction, their corresponding sides are equal), and KH equals EBFG plus C [Step 3]. Therefore the gnomon equals C [CN3].

**Step 9.** Now, since AE equals EB [Step 2] and EBFG is on EB, the parallelogram on AB is obtained by extending the construction from E in both directions. The parallelogram AOPL applied to AB equals the gnomon plus EBFG minus EBFG composed appropriately. Specifically, the parallelogram applied to the whole line AB consists of the gnomon together with certain parts, and the excess beyond AB is the parallelogram BMNS, which is similar to D since it is the parallelogram about the diameter in LEMN, hence similar to LEMN [6.24], and LEMN is similar to D.

**Step 10.** Since AE equals EB, and the figure LEMN extends from E to M along EB produced, the total application to AB has the parallelogram on AB equal to the gnomon, which equals C [Step 8]. The excess parallelogram beyond B is similar to LEMN [6.24], hence similar to D [6.21].

**Step 11.** Therefore, to the given straight line AB there has been applied a parallelogram equal to the given rectilineal figure C and exceeding by a parallelogrammic figure similar to D. Q.E.F.

**USED:** 1.10, 1.43, 6.18, 6.21, 6.22, 6.24, 6.25, 6.26, CN3, CN5, D6.1, P1, P2
**Human refs (from References field):** 1.36, 1.43, 6.21, 6.24, 6.25, 6.26
**Jaccard:** 0.357 — AI adds ['1.10', '6.18', '6.22', 'CN3', 'CN5', 'D6.1', 'P1', 'P2']; Human adds ['1.36']

## Proposition 6.30
**Statement:** To cut a given finite straight line in extreme and mean ratio.

**Step 1.** Let AB be the given finite straight line. It is required to cut AB in extreme and mean ratio.

**Step 2.** Cut AB at C such that the rectangle contained by AB and BC is equal to the square on AC. This is possible by 2.11.

**Step 3.** Since the rectangle contained by AB and BC equals the square on AC, the three straight lines AB, AC, BC are proportional, that is, AB : AC = AC : BC. This follows by 6.17 (the converse part: if the rectangle contained by the extremes equals the square on the mean, then the three straight lines are proportional), where AB and BC are the extremes and AC is the mean.

**Step 4.** Since AB : AC = AC : BC, and C lies on AB with AC being the greater segment and BC the lesser, the line AB has been cut in extreme and mean ratio at C, according to Definition D6.3 (a straight line is cut in extreme and mean ratio when the whole is to the greater segment as the greater segment is to the less).

**Step 5.** Therefore the given finite straight line AB has been cut in extreme and mean ratio. Q.E.F.

**USED:** 2.11, 6.17, D6.3
**Human refs (from References field):** 6.14, 6.29
**Jaccard:** 0.000 — AI adds ['2.11', '6.17', 'D6.3']; Human adds ['6.14', '6.29']

## Proposition 6.31
**Statement:** In right - angled triangles the figure on the side subtending the right angle is equal to the similar and similarly described figures on the sides containing the right angle.

**Step 1.** Let ABC be a right-angled triangle having the angle BAC right, and let similar and similarly described rectilineal figures be drawn on BC, BA, and AC. We must show that the figure on BC is equal to the sum of the figures on BA and AC.

**Step 2.** From A draw AD perpendicular to BC [1.12]. Then in the right-angled triangle ABC, the perpendicular AD has been drawn from the right angle to the base BC.

**Step 3.** By 6.8, the triangles ABD and ADC are similar both to the whole triangle ABC and to one another. In particular, triangle ABC is similar to triangle ABD, and triangle ABC is similar to triangle ACD.

**Step 4.** Since triangle ABC is similar to triangle ABD, the sides about the equal angles are proportional [D6.1]. In particular, as BC (the side subtending the right angle in ABC) is to BA (the side subtending the right angle in ABD), so is BA to BD. That is, BC : BA = BA : BD.

**Step 5.** Since BC : BA = BA : BD, the line BA is a mean proportional between BC and BD. Therefore BC has to BD the duplicate ratio of that which BC has to BA [D5.9].

**Step 6.** Similarly, since triangle ABC is similar to triangle ACD, as BC is to CA, so is CA to CD. That is, BC : CA = CA : CD. Therefore BC has to CD the duplicate ratio of that which BC has to CA [D5.9].

**Step 7.** Now let the similar and similarly described figure on BC be F, the similar figure on BA be G, and the similar figure on AC be H. Since these are similar rectilineal figures described on BC, BA, and AC respectively, by 6.20 the figure F is to the figure G in the duplicate ratio of BC to BA, and the figure F is to the figure H in the duplicate ratio of BC to CA.

**Step 8.** From Step 5, the duplicate ratio of BC to BA is the ratio BC : BD. From Step 7, the figure F is to the figure G in the duplicate ratio of BC to BA. Therefore F : G = BC : BD.

**Step 9.** From Step 6, the duplicate ratio of BC to CA is the ratio BC : CD. From Step 7, the figure F is to the figure H in the duplicate ratio of BC to CA. Therefore F : H = BC : CD.

**Step 10.** From Step 8, F : G = BC : BD. By inversion [5.7 via contrapositive, or directly by 5.4], G : F = BD : BC. Similarly from Step 9, by inversion, H : F = CD : BC.

**Step 11.** Since G : F = BD : BC and H : F = CD : BC, by addition of ratios [5.24], (G + H) : F = (BD + CD) : BC.

**Step 12.** But D lies on BC between B and C (since AD is the perpendicular from A to BC), so BD + CD = BC. Therefore (BD + CD) : BC = BC : BC.

**Step 13.** Since BC : BC is the ratio of equal magnitudes, by 5.9 (equals have the same ratio), (G + H) : F = BC : BC, which is a ratio of equality.

**Step 14.** Therefore G + H = F [5.9]. That is, the figure on BA together with the figure on AC is equal to the figure on BC.

**Step 15.** Therefore, in right-angled triangles the figure on the side subtending the right angle is equal to the similar and similarly described figures on the sides containing the right angle. Q.E.D.

**USED:** 1.12, 5.24, 5.9, 6.20, 6.8, D5.9, D6.1
**Human refs (from References field):** 6.19, 6.8, D6.1
**Jaccard:** 0.250 — AI adds ['1.12', '5.24', '5.9', '6.20', 'D5.9']; Human adds ['6.19']

## Proposition 6.32
**Statement:** If two triangles having two sides proportional to two sides be placed together at one angle so that their corresponding sides are also parallel, the remaining sides of the triangles will be in a straight line.

**Step 1.** Let triangles ABC and DCE be placed together at vertex C such that B, C, D lie on a single straight line, AB is parallel to DE, and BC/CD = AB/DE. The triangles are arranged so that A and E lie on opposite sides of line BD, with the angle BCA in triangle ABC and the angle DCE in triangle DCE being vertical angles at C.

**Step 2.** Join A to E by P1. Since A and E lie on opposite sides of line BD, the straight line AE must cross line BD at some point; call this point G.

**Step 3.** Since AB is parallel to DE and line BD falls on these parallel lines, by 1.29 the alternate angles are equal: angle ABG equals angle EDG.

**Step 4.** At point G on line BD, angles AGB and EGD are vertical angles formed by the intersection of lines AE and BD. By 1.15, angle AGB equals angle EGD.

**Step 5.** In triangles ABG and EDG, we have angle ABG equal to angle EDG (Step 3) and angle AGB equal to angle EGD (Step 4). By 1.32, the three interior angles of any triangle sum to two right angles, so the remaining angles must also be equal: angle BAG equals angle DEG. Therefore triangles ABG and EDG are equiangular.

**Step 6.** Since triangles ABG and EDG are equiangular, by 6.4 the sides about the equal angles are proportional. In particular, the sides about the equal angles at G give the proportion AB/ED = BG/GD.

**Step 7.** We are given that BC/CD = AB/DE. From Step 6, AB/DE = BG/GD. Therefore BG/GD = BC/CD, since both ratios equal AB/DE (by CN1).

**Step 8.** Since BG/GD = BC/CD, by 5.17 (composition of a ratio) we obtain (BG + GD)/GD = (BC + CD)/CD. Now G lies on segment BD between B and D, so BG + GD = BD. Likewise BC + CD = BD. Therefore BD/GD = BD/CD.

**Step 9.** Since BD/GD = BD/CD, by 5.9 (magnitudes which have the same ratio to the same magnitude are equal to one another), GD = CD.

**Step 10.** Since GD = CD, and both G and C lie on segment BD at the same distance from D, the point G coincides with C. Therefore the straight line AE passes through C, which means that A, C, E are collinear. Hence the remaining sides CA and CE of the two triangles are in a straight line, which was to be proved.

**USED:** 1.15, 1.29, 1.32, 5.17, 5.9, 6.4, CN1, P1
**Human refs (from References field):** 1.14, 1.29, 1.32, 6.6
**Jaccard:** 0.200 — AI adds ['1.15', '5.17', '5.9', '6.4', 'CN1', 'P1']; Human adds ['1.14', '6.6']

## Proposition 6.33
**Statement:** In equal circles angles have the same ratio as the circumferences on which they stand, whether they stand at the centres or at the circumferences.

**Step 1.** Let there be equal circles ABC and DEF, and let angles BGC and EHF be angles at the centres G and H, and angles BAC and EDF be angles at the circumferences, standing on circumferences BC and EF respectively. I say that circumference BC is to circumference EF as angle BGC is to angle EHF, and as angle BAC is to angle EDF.

**Step 2.** Starting from B along circumference BC, place any number of consecutive arcs each equal to circumference BC. Specifically, let circumferences CK and KL each be made equal to circumference BC, so that we have arcs BC, CK, KL laid out consecutively. Similarly, starting from E along circumference EF in circle DEF, place any number of consecutive arcs each equal to circumference EF. Let circumferences FM and MN each be made equal to circumference EF. [P3, D3.1]

**Step 3.** Join GK and GL in circle ABC, and HM and HN in circle DEF. [P1]

**Step 4.** Since circumferences BC, CK, and KL are all equal to one another, the angles BGC, CGK, and KGL are also equal to one another, for in equal circles (here the same circle, which is equal to itself) equal circumferences are subtended by equal angles at the centre. [3.27]

**Step 5.** Therefore, whatever multiple circumference BL is of circumference BC, the angle BGL is the same multiple of angle BGC. That is, if BL = n times BC, then angle BGL = n times angle BGC. [CN2]

**Step 6.** Similarly, since circumferences EF, FM, and MN are all equal to one another, the angles EHF, FHM, and MHN are all equal to one another. [3.27]

**Step 7.** Therefore, whatever multiple circumference EN is of circumference EF, the angle EHN is the same multiple of angle EHF. [CN2]

**Step 8.** Now, if circumference BL is equal to circumference EN, then angle BGL is also equal to angle EHN, since in equal circles equal circumferences subtend equal angles at the centres. [3.27]

**Step 9.** If circumference BL is greater than circumference EN, then angle BGL is also greater than angle EHN. For a greater circumference in equal circles subtends a greater angle at the centre. [3.27]

**Step 10.** And if circumference BL is less than circumference EN, then angle BGL is less than angle EHN. [3.27]

**Step 11.** Thus there are four magnitudes: circumference BC (first), circumference EF (second), angle BGC (third), angle EHF (fourth). And we have taken equimultiples of the first and third, namely circumference BL and angle BGL, and equimultiples of the second and fourth, namely circumference EN and angle EHN. And we have shown that if the multiple of the first exceeds, equals, or falls short of the multiple of the second, then the multiple of the third likewise exceeds, equals, or falls short of the multiple of the fourth respectively.

**Step 12.** Therefore, by the definition of proportion, circumference BC is to circumference EF as angle BGC is to angle EHF. [D5.5]

**Step 13.** But the angle at the centre BGC is double the angle at the circumference BAC, and the angle at the centre EHF is double the angle at the circumference EDF, since in each circle the angle at the centre is double the angle at the circumference when both stand on the same arc. [3.20]

**Step 14.** Since angle BGC is double angle BAC and angle EHF is double angle EDF, and since angle BGC is to angle EHF as circumference BC is to circumference EF, it follows that angle BAC is to angle EDF as circumference BC is to circumference EF. For halves of magnitudes are in the same ratio as the magnitudes themselves. [5.15]

**Step 15.** Therefore, in equal circles, angles have the same ratio as the circumferences on which they stand, whether they stand at the centres or at the circumferences. Q.E.D.

**USED:** 3.20, 3.27, 5.15, CN2, D3.1, D5.5, P1, P3
**Human refs (from References field):** 3.27, D5.5
**Jaccard:** 0.250 — AI adds ['3.20', '5.15', 'CN2', 'D3.1', 'P1', 'P3']
