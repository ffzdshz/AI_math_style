# Book 4 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 4.1
**Statement:** Into a given circle to fit a straight line equal to a given straight line which is not greater than the diameter of the circle.

**Step 1.** Let ABC be the given circle and let E be the given straight line, which is not greater than the diameter of the circle. It is required to fit into the circle ABC a straight line equal to E.

**Step 2.** Find the center D of circle ABC [3.1], and draw a diameter BC through D [P1, D1.17].

**Step 3.** Now E is not greater than the diameter BC. If BC equals E, then BC has been fitted into the circle ABC (since B and C lie on the circumference) equal to E, and the problem is solved [D4.7].

**Step 4.** If BC does not equal E, then since E is not greater than BC, we have BC greater than E. Using Proposition 1.3, cut off from BC a straight line CF equal to E, so that CF is less than or equal to BC [1.3].

**Step 5.** With center C and radius CF, describe a circle FGH [P3]. Since C is a point on the circumference of circle ABC and CF is not greater than the radius of circle ABC (for CF is not greater than the diameter BC, and in fact CF, being at most the diameter, when used as radius from the circumference point C, will meet the circle), let G be a point where circle FGH meets circle ABC.

**Step 6.** Join CG [P1].

**Step 7.** Since C is the center of circle FGH, the straight lines CG and CF are both radii of circle FGH. Therefore CG equals CF [D1.15].

**Step 8.** But CF was made equal to E [Step 4]. Therefore CG equals E [CN1].

**Step 9.** Now both C and G lie on the circumference of circle ABC, so CG has been fitted into circle ABC [D4.7].

**Step 10.** Therefore, into the given circle ABC, a straight line CG has been fitted equal to the given straight line E. Q.E.F.

**USED:** 1.3, 3.1, CN1, D1.15, D1.17, D4.7, P1, P3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.3', '3.1', 'CN1', 'D1.15', 'D1.17', 'D4.7', 'P1', 'P3']

## Proposition 4.2
**Statement:** In a given circle to inscribe a triangle equiangular with a given triangle.

**Step 1.** Let ABC be the given circle and let DEF be the given triangle. It is required to inscribe in circle ABC a triangle equiangular with triangle DEF.

**Step 2.** Let A be any point on the circumference of circle ABC. Draw the straight line GH tangent to the circle at A [3.16]. Here GH touches circle ABC at A and, being produced, does not cut the circle.

**Step 3.** On the straight line AH at the point A, construct the angle HAC equal to the angle DEF [1.23], where C is a point on the circumference of circle ABC.

**Step 4.** On the straight line AG at the point A, construct the angle GAB equal to the angle DFE [1.23], where B is a point on the circumference of circle ABC.

**Step 5.** Join BC [P1]. Triangle ABC is now inscribed in circle ABC, since its three vertices A, B, C lie on the circumference [D4.3].

**Step 6.** Since GH is tangent to circle ABC at A, and AC is a chord drawn from the point of tangency, the angle HAC is equal to the angle ABC in the alternate segment [3.32]. But angle HAC was constructed equal to angle DEF [Step 3]. Therefore angle ABC is equal to angle DEF [CN1].

**Step 7.** Similarly, since GH is tangent to circle ABC at A, and AB is a chord drawn from the point of tangency, the angle GAB is equal to the angle ACB in the alternate segment [3.32]. But angle GAB was constructed equal to angle DFE [Step 4]. Therefore angle ACB is equal to angle DFE [CN1].

**Step 8.** Since the three angles of any triangle are together equal to two right angles [1.32], the angles of triangle ABC (namely angle BAC, angle ABC, and angle ACB) are together equal to two right angles, and the angles of triangle DEF (namely angle EDF, angle DEF, and angle DFE) are together equal to two right angles.

**Step 9.** Therefore the sum of the three angles of triangle ABC equals the sum of the three angles of triangle DEF [CN1]. Since angle ABC equals angle DEF [Step 6] and angle ACB equals angle DFE [Step 7], subtracting these equals from the equal sums, the remaining angle BAC equals the remaining angle EDF [CN3].

**Step 10.** Therefore triangle ABC, inscribed in circle ABC, is equiangular with triangle DEF, having angle BAC equal to angle EDF, angle ABC equal to angle DEF, and angle ACB equal to angle DFE. Thus in the given circle a triangle equiangular with the given triangle has been inscribed, which is what was required to do.

**USED:** 1.23, 1.32, 3.16, 3.32, CN1, CN3, D4.3, P1
**Human refs (from References field):** 1.23, 1.32, 3.16, 3.32
**Jaccard:** 0.500 — AI adds ['CN1', 'CN3', 'D4.3', 'P1']

## Proposition 4.3
**Statement:** About a given circle to circumscribe a triangle equiangular with a given triangle.

**Step 1.** Let ABC be the given circle with center K, and let DEF be the given triangle. We must circumscribe about circle ABC a triangle equiangular with triangle DEF.

**Step 2.** Produce side EF in both directions to points G and H, so that GEF and EFH are straight lines [P2].

**Step 3.** Take any point A on the circumference of circle ABC. Draw the straight line KA from the center K to A [P1].

**Step 4.** At the point K on the straight line KA, construct angle AKB equal to angle DEG on one side, and angle AKC equal to angle DFH on the other side, where B and C are the points at which the newly drawn lines from K meet the circumference of the circle [1.23].

**Step 5.** Through A, draw the straight line LAM at right angles to KA; through B, draw the straight line LBN at right angles to KB; through C, draw the straight line MCN at right angles to KC [1.11].

**Step 6.** Since each of these lines is drawn at right angles to a diameter of the circle at its extremity, each line touches the circle at its respective point [3.16]. Therefore LA M touches at A, LBN touches at B, and MCN touches at C.

**Step 7.** Let L be the intersection of the tangents at A and B, let M be the intersection of the tangents at A and C, and let N be the intersection of the tangents at B and C. Then triangle LMN is circumscribed about circle ABC, since each of its sides touches the circle [D4.4].

**Step 8.** Now consider the quadrilateral AKBL. The angle KAL is a right angle and the angle KBL is a right angle, since they are the angles between the radii and the tangent lines [3.16]. The quadrilateral AKBL is composed of two triangles whose angle sums each equal two right angles [1.32], so the sum of the four angles of quadrilateral AKBL equals four right angles.

**Step 9.** Since angle KAL and angle KBL are each right angles, their sum equals two right angles. Therefore the sum of the remaining two angles, angle AKB and angle ALB, also equals two right angles.

**Step 10.** By construction, angle AKB equals angle DEG [Step 4]. Since GE is produced from EF, angle DEG and angle DEF together equal two right angles [1.13].

**Step 11.** Therefore angle AKB and angle DEF together equal two right angles. But angle AKB and angle ALB together also equal two right angles [Step 9]. Hence angle ALB equals angle DEF [CN1].

**Step 12.** By the same reasoning applied to quadrilateral AKCM: angle KAM is a right angle and angle KCM is a right angle [3.16], so the sum of the four angles of AKCM equals four right angles [1.32]. Since angle KAM and angle KCM are each right angles, the sum of angle AKC and angle AMC equals two right angles.

**Step 13.** By construction, angle AKC equals angle DFH [Step 4]. Since FH is produced from EF, angle DFH and angle DFE together equal two right angles [1.13].

**Step 14.** Therefore angle AKC and angle DFE together equal two right angles. But angle AKC and angle AMC together also equal two right angles [Step 12]. Hence angle AMC equals angle DFE [CN1].

**Step 15.** Since the three angles of triangle LMN sum to two right angles [1.32], and the three angles of triangle DEF also sum to two right angles [1.32], and since angle ALB (that is, angle L) equals angle DEF and angle AMC (that is, angle M) equals angle DFE, the remaining angle N of triangle LMN equals the remaining angle EDF of triangle DEF [CN3].

**Step 16.** Therefore triangle LMN has been circumscribed about the given circle ABC, and it is equiangular with the given triangle DEF. This is what was required to do.

**USED:** 1.11, 1.13, 1.23, 1.32, 3.16, CN1, CN3, D4.4, P1, P2
**Human refs (from References field):** 1.13, 1.23, 1.32, 3.1, 3.16, 3.18
**Jaccard:** 0.333 — AI adds ['1.11', 'CN1', 'CN3', 'D4.4', 'P1', 'P2']; Human adds ['3.1', '3.18']

## Proposition 4.4
**Statement:** In a given triangle to inscribe a circle.

**Step 1.** Let ABC be the given triangle. We wish to inscribe a circle in it.

**Step 2.** Bisect angle ABC by the straight line BD, and bisect angle BCA by the straight line CD [1.9]. Let these bisectors meet at the point D inside the triangle.

**Step 3.** From D, draw DE perpendicular to AB, DF perpendicular to BC, and DG perpendicular to AC [1.12]. Thus angles DEB, DFB, DFC, and DGC are all right angles.

**Step 4.** Consider triangles DBE and DBF. Angle DBE equals angle DBF, since BD bisects angle ABC [Step 2]. Angle DEB and angle DFB are both right angles [Step 3], so they are equal [P4]. The side BD is common. Therefore triangle DBE is congruent to triangle DBF [1.26], and so DE equals DF.

**Step 5.** Consider triangles DCF and DCG. Angle DCF equals angle DCG, since CD bisects angle BCA [Step 2]. Angle DFC and angle DGC are both right angles [Step 3], so they are equal [P4]. The side DC is common. Therefore triangle DCF is congruent to triangle DCG [1.26], and so DF equals DG.

**Step 6.** From Steps 4 and 5, DE equals DF and DF equals DG. Therefore DE equals DG [CN1]. Hence DE, DF, and DG are all equal to one another.

**Step 7.** With center D and radius DE, describe a circle EFG [P3]. Since DE equals DF equals DG, this circle passes through E, F, and G.

**Step 8.** Since DE is perpendicular to AB at E, and DE is a radius of circle EFG, the line AB touches the circle at E and does not cut it [3.16]. Similarly, since DF is perpendicular to BC at F, the line BC touches the circle at F. And since DG is perpendicular to AC at G, the line AC touches the circle at G.

**Step 9.** Therefore the circle EFG touches each of the three sides AB, BC, and AC of triangle ABC. Hence the circle EFG is inscribed in triangle ABC [D4.5].

Therefore, in the given triangle ABC, a circle has been inscribed, which is what was required to do.

**USED:** 1.12, 1.26, 1.9, 3.16, CN1, D4.5, P3, P4
**Human refs (from References field):** 1.26, 1.9, 3.16, D4.5
**Jaccard:** 0.500 — AI adds ['1.12', 'CN1', 'P3', 'P4']

## Proposition 4.5
**Statement:** About a given triangle to circumscribe a circle.

**Step 1.** Let ABC be the given triangle. We are to circumscribe a circle about it, that is, to find a circle whose circumference passes through each vertex A, B, C.

**Step 2.** Bisect AB at D and BC at E [1.10].

**Step 3.** From D, draw DF at right angles to AB, and from E, draw EF at right angles to BC [1.11]. These perpendiculars must meet, for if they were parallel then, since DF is perpendicular to AB and EF is perpendicular to BC, the lines AB and BC would also have to be parallel [1.28]; but AB and BC meet at B, so they are not parallel, and therefore DF and EF are not parallel. They meet at some point F, which lies either inside the triangle, on side AC, or outside the triangle.

**Step 4.** Join FA, FB, and FC [P1].

**Step 5.** Since AD equals DB [Step 2], DF is common to triangles ADF and BDF, and angle ADF equals angle BDF (both being right angles) [P4], therefore triangle ADF is congruent to triangle BDF [1.4]. Hence FA equals FB.

**Step 6.** Since BE equals EC [Step 2], EF is common to triangles BEF and CEF, and angle BEF equals angle CEF (both being right angles) [P4], therefore triangle BEF is congruent to triangle CEF [1.4]. Hence FB equals FC.

**Step 7.** From Steps 5 and 6, FA equals FB and FB equals FC. Therefore FA equals FC [CN1]. Thus all three distances FA, FB, FC are equal to one another.

**Step 8.** Describe a circle with center F and radius FA [P3]. Since FA equals FB and FA equals FC, the points B and C also lie on this circle, for all straight lines from F to the circumference are equal [D1.15], and FB and FC are each equal to FA.

**Step 9.** Therefore the circle passes through all three vertices A, B, and C. Since the circumference of the circle passes through each angle of the triangle, the circle has been circumscribed about triangle ABC [D4.6].

**Step 10.** Therefore, about the given triangle ABC, a circle has been circumscribed, which is what was required to do.

**USED:** 1.10, 1.11, 1.28, 1.4, CN1, D1.15, D4.6, P1, P3, P4
**Human refs (from References field):** 1.10, 1.4
**Jaccard:** 0.200 — AI adds ['1.11', '1.28', 'CN1', 'D1.15', 'D4.6', 'P1', 'P3', 'P4']

## Proposition 4.6
**Statement:** In a given circle to inscribe a square.

**Step 1.** Let the given circle be ABCD with center E. Draw a diameter AC through E [D1.17]. Through E, draw a straight line BD at right angles to AC [1.11], and let B and D be the points where this perpendicular meets the circumference of the circle. Then BD is also a diameter [D1.17].

**Step 2.** Join AB, BC, CD, and DA [P1]. I say that ABCD is a square inscribed in the circle.

**Step 3.** Since AC is a diameter, the arc ABC is a semicircle, and the angle ADC, being an angle in that semicircle, is a right angle [3.31]. Similarly, the arc ADC is a semicircle, and the angle ABC is a right angle [3.31].

**Step 4.** Since BD is a diameter, the arc BAD is a semicircle, and the angle BCD, being an angle in that semicircle, is a right angle [3.31]. Similarly, the arc BCD is a semicircle, and the angle BAD is a right angle [3.31].

**Step 5.** Therefore the quadrilateral ABCD has all four of its angles right angles.

**Step 6.** Now, since AE and BE are both radii of the circle, AE = BE [D1.15]. Similarly, BE = DE, since both are radii [D1.15]. The angle AEB and angle AED are both right angles (since BD is perpendicular to AC), so angle AEB equals angle AED [P4]. In triangles AEB and AED, AE is common, BE = DE, and angle AEB = angle AED. Therefore triangle AEB is congruent to triangle AED [1.4], and so AB = AD.

**Step 7.** In triangles AEB and CEB, BE is common, AE = CE (both radii) [D1.15], and angle AEB = angle CEB (both right angles) [P4]. Therefore triangle AEB is congruent to triangle CEB [1.4], and so AB = BC.

**Step 8.** In triangles CEB and CED, CE is common, BE = DE (both radii) [D1.15], and angle CEB = angle CED (both right angles) [P4]. Therefore triangle CEB is congruent to triangle CED [1.4], and so BC = CD.

**Step 9.** Therefore AB = BC = CD = DA, and the quadrilateral ABCD is equilateral [CN1].

**Step 10.** Since ABCD is both equilateral and right-angled, it is a square by definition [D1.22].

**Step 11.** Each vertex A, B, C, D lies on the circumference of the circle, so the square ABCD is inscribed in the circle [D4.3].

**Step 12.** Therefore, in the given circle ABCD, a square has been inscribed. Q.E.F.

**USED:** 1.11, 1.4, 3.31, CN1, D1.15, D1.17, D1.22, D4.3, P1, P4
**Human refs (from References field):** 1.4, 3.31, D1.22
**Jaccard:** 0.300 — AI adds ['1.11', 'CN1', 'D1.15', 'D1.17', 'D4.3', 'P1', 'P4']

## Proposition 4.7
**Statement:** About a given circle to circumscribe a square.

**Step 1.** Let ABCD be the given circle with center E. Draw diameter AC through E, and draw diameter BD through E perpendicular to AC, using 1.11 to erect a perpendicular to AC at E. Then angle AEB is a right angle.

**Step 2.** Through A, draw line FG perpendicular to EA (1.11). Through B, draw line GH perpendicular to EB (1.11). Through C, draw line HK perpendicular to EC (1.11). Through D, draw line FK perpendicular to ED (1.11). Let F be the intersection of the line through A and the line through D, G the intersection of the line through A and the line through B, H the intersection of the line through B and the line through C, and K the intersection of the line through C and the line through D.

**Step 3.** Since FG is perpendicular to EA and HK is perpendicular to EC, and A, E, C are collinear (AC being a diameter), FG and HK each make right angles with line AC. Thus the interior angles on the same side of transversal AC sum to two right angles, so FG is parallel to HK (1.28). Similarly, since GH is perpendicular to EB and FK is perpendicular to ED, and B, E, D are collinear (BD being a diameter), GH is parallel to FK (1.28).

**Step 4.** Since FG is parallel to HK and GH is parallel to FK, quadrilateral FGHK is a parallelogram. By 1.34, opposite sides are equal: FG = HK and GH = FK.

**Step 5.** Consider quadrilateral AGBE. By construction, angle GAE is right (FG perpendicular to AE), angle AEB is right (BD perpendicular to AC), and angle EBG is right (GH perpendicular to EB). Draw diagonal AB. In triangle ABE, the angles sum to two right angles (1.32), and angle AEB is right, so angle BAE + angle ABE equals one right angle. In triangle ABG, the angles sum to two right angles (1.32). Now angle GAB = angle GAE minus angle BAE = one right angle minus angle BAE, and angle GBA = angle GBE minus angle ABE = one right angle minus angle ABE. So angle GAB + angle GBA = two right angles minus (angle BAE + angle ABE) = two right angles minus one right angle = one right angle. Therefore angle AGB = two right angles minus one right angle = one right angle (1.32).

**Step 6.** By an identical argument applied to quadrilateral BECH (with angle EBH right, angle BEC right, angle ECH right), angle BHC is right. Similarly, applied to quadrilateral CEDK, angle CKD is right, and applied to quadrilateral DEAF, angle DFA is right. Thus all four angles of FGHK are right angles.

**Step 7.** Since AGBE has all four angles right (angles at A, E, B each right by construction, and angle G right by Step 5), and its opposite sides are parallel (AG parallel to EB since both perpendicular to AE, and AE parallel to BG since both perpendicular to EB, by 1.28), AGBE is a parallelogram. By 1.34, AG = EB and BG = AE. Since AE and EB are both radii of circle ABCD, AE = EB (D1.15). By CN1, AG = AE = EB = BG.

**Step 8.** Similarly, in parallelogram AFED (all right angles, opposite sides parallel by 1.28), AF = ED and FD = AE (1.34). Since ED is a radius and AE is a radius, AE = ED (D1.15), so AF = AE (CN1). Likewise, in parallelogram BECH, BH = EC and CH = BE (1.34), and since BE = EC (D1.15), BH = BE (CN1). In parallelogram CEDK, CK = ED and DK = CE (1.34), and since CE = ED (D1.15), CK = CE (CN1).

**Step 9.** Now FG = FA + AG (F, A, G being collinear on the tangent through A). We have FA = AE and AG = AE (from Steps 7 and 8), so FG = AE + AE (CN2). Similarly, GH = GB + BH = BE + BE (CN2), HK = KC + CH = CE + CE (CN2), and KF = KD + DF = ED + ED (CN2). Since AE = BE = CE = DE (all radii, D1.15 and CN1), we conclude FG = GH = HK = KF (CN1).

**Step 10.** FGHK is equilateral (all sides equal by Step 9) and right-angled (all angles right by Step 6). Therefore FGHK is a square (D1.22).

**Step 11.** Each side of FGHK touches the circle at exactly one point: FG touches at A, GH touches at B, HK touches at C, and FK touches at D. This is because each side is perpendicular to the radius at the point where it meets the circle, so by 3.16, each side is tangent to the circle. Therefore the square FGHK is circumscribed about the given circle (D4.4).

**Step 12.** Therefore, about the given circle, a square has been circumscribed, which is what was required to do. Q.E.F.

**USED:** 1.11, 1.28, 1.32, 1.34, 3.16, CN1, CN2, D1.15, D1.22, D4.4
**Human refs (from References field):** 1.28, 1.30, 1.34, 3.16, 3.18
**Jaccard:** 0.250 — AI adds ['1.11', '1.32', 'CN1', 'CN2', 'D1.15', 'D1.22', 'D4.4']; Human adds ['1.30', '3.18']

## Proposition 4.8
**Statement:** In a given square to inscribe a circle.

**Step 1.** Let ABCD be the given square, with vertices labeled so that AB, BC, CD, DA are its sides. By D1.22, ABCD is equilateral and right-angled, so AB = BC = CD = DA, and each interior angle is a right angle.

**Step 2.** Bisect AD at E and bisect AB at G [1.10]. Then AE = ED and AG = GB.

**Step 3.** Through E, draw line EF parallel to AB, meeting BC at F [1.31, P1]. Through G, draw line GH parallel to AD, meeting DC at H [1.31, P1].

**Step 4.** Let K be the intersection of EF and GH. Since EF is parallel to AB (and hence to CD), and GH is parallel to AD (and hence to BC), the figure AEKG has AE parallel to GK and AG parallel to EK.

**Step 5.** Therefore AEKG is a parallelogram, so AE = GK and AG = EK [1.34]. Since ABCD is a square, AD = AB, and since AE is half of AD and AG is half of AB, we have AE = AG [CN1]. Therefore EK = GK = AE = AG.

**Step 6.** Similarly, EBFK is a parallelogram (EB parallel to KF, EK parallel to BF), so KF = EB = AE [1.34, CN1]. And GKHD is a parallelogram, so KH = GD. Now GD = AG (since AG = GB = half of AB, and similarly DH = half of DC = half of AB = AG; but GD is not a side — let me proceed differently). GKHD is a parallelogram with GK parallel to DH and GD parallel to KH, so KH = GD [1.34]. Since DC = AB and DH = half of DC (by the parallel construction from the midpoint G, the line GH meets DC at H with DH = AG), we have KH = AG = AE [CN1].

**Step 7.** Thus KE = KG = KF = KH, all equal to half the side of the square.

**Step 8.** With center K and radius KE, describe circle EGFH [P3]. Since KE = KF = KG = KH, the circle passes through E, F, G, and H, the midpoints of the four sides.

**Step 9.** Now consider side AD. The line EK (part of EF) is parallel to AB, so EK is perpendicular to AD, since angle DAB is a right angle and EK is parallel to AB [1.29, P4]. Thus KE meets AD at right angles at the point E, which lies on the circle. By 3.16, since KE is a radius drawn to the point E on the circle and KE is perpendicular to AD, the line AD touches the circle at E and does not cut it. Therefore side AD is tangent to the circle at E.

**Step 10.** By the same reasoning, side AB is perpendicular to GK at G (since GK is parallel to AD and angle DAB is right), so AB touches the circle at G [3.16, 1.29, P4]. Side BC is perpendicular to KF at F (since KF is parallel to AB and angle ABC is right), so BC touches the circle at F [3.16, 1.29, P4]. Side CD is perpendicular to KH at H (since KH is parallel to AD and angle ADC is right), so CD touches the circle at H [3.16, 1.29, P4].

**Step 11.** Since each side of square ABCD touches the circle at exactly one point, the circle with center K and radius KE is inscribed in the square ABCD [D4.5].

**Step 12.** Therefore, in the given square a circle has been inscribed, which is what was required to do.

**USED:** 1.10, 1.29, 1.31, 1.34, 3.16, CN1, D1.22, D4.5, P1, P3, P4
**Human refs (from References field):** 1.10, 1.31, 1.34, 3.16
**Jaccard:** 0.364 — AI adds ['1.29', 'CN1', 'D1.22', 'D4.5', 'P1', 'P3', 'P4']

## Proposition 4.9
**Statement:** About a given square to circumscribe a circle.

**Step 1.** Let ABCD be the given square, with right angles at each vertex and all sides equal [D1.22].

**Step 2.** Draw the diagonals AC and BD [P1], and let them intersect at point E.

**Step 3.** Since ABCD is a square, AB = AD and BC = DC [D1.22]. In triangles ABC and ADC, we have AB = AD, BC = DC, and AC is common. Therefore triangle ABC is congruent to triangle ADC [1.8], and so angle BAC = angle DAC.

**Step 4.** Since angle BAD is a right angle [D1.22] and angle BAC = angle DAC, each of these equals half a right angle.

**Step 5.** Similarly, since AB = CB and AD = CD, in triangles ABD and CBD we have AB = CB, AD = CD, and BD is common. Therefore triangle ABD is congruent to triangle CBD [1.8], and so angle ABD = angle CBD.

**Step 6.** Since angle ABC is a right angle [D1.22] and angle ABD = angle CBD, each of these equals half a right angle.

**Step 7.** Now consider triangle ABE. We have angle BAE = half a right angle [Step 4] and angle ABE = half a right angle [Step 6]. Since the two base angles are equal, the sides opposite them are equal, so EA = EB [1.6].

**Step 8.** By the same reasoning in triangle BCE: angle CBE = half a right angle [Step 6] and angle BCE = half a right angle (since angle BCA = angle BAC = half a right angle, from Step 3 applied to the congruence of triangles ABC and ADC, noting angle BCA corresponds to angle BAC in the congruent pair). Therefore EB = EC [1.6].

**Step 9.** Similarly in triangle CDE: angle DCE = angle DAC = half a right angle (since angle DCA = angle BAC by the congruence in Step 3, and angle BCA = angle BAC, so angle DCA = half a right angle). And angle CDE = half a right angle (by an argument symmetric to Step 6, from the congruence of triangles ACD and BCD giving angle ADC bisected by diagonal, so angle CDE = half a right angle). Therefore EC = ED [1.6].

**Step 10.** From Steps 7, 8, and 9, we have EA = EB = EC = ED [CN1].

**Step 11.** With centre E and radius EA, describe a circle [P3]. Since EA = EB = EC = ED, the circle passes through all four vertices A, B, C, and D.

**Step 12.** Therefore the circle is circumscribed about the square ABCD [D4.6], which is what was required.

**USED:** 1.6, 1.8, CN1, D1.22, D4.6, P1, P3
**Human refs (from References field):** 1.6, 1.8
**Jaccard:** 0.286 — AI adds ['CN1', 'D1.22', 'D4.6', 'P1', 'P3']

## Proposition 4.10
**Statement:** To construct an isosceles triangle having each of the angles at the base double of the remaining one.

**Step 1.** Let AB be any given straight line. Cut AB at the point C so that the rectangle AB times BC equals the square on CA [2.11]. That is, AB * BC = CA^2.

**Step 2.** With center A and radius AB, describe the circle BDE [P3]. Since A is the center and AB is the radius, every point on this circle is at distance AB from A.

**Step 3.** In circle BDE, fit the chord BD equal to CA [4.1]. This is possible because CA is less than AB (since C lies between A and B and AB * BC = CA^2 implies CA < AB), and AB is a radius, so CA is less than the diameter of circle BDE.

**Step 4.** Join AD and DC [P1].

**Step 5.** Circumscribe a circle about triangle ACD [4.5]. Call this the circle ACD.

**Step 6.** Since AB * BC = CA^2 (from Step 1) and BD = CA (from Step 3), we have AB * BC = BD^2. Since AB = BA, this gives BD^2 = BC * BA.

**Step 7.** Now B lies outside circle ACD (since the line from B through C to A is a secant of circle ACD, with C and A on the circle, and B beyond C). The line BCA is a secant from B cutting circle ACD at C and A, and BD meets circle ACD at D. Since BD^2 = BC * BA, by the converse of the tangent-secant theorem, BD touches circle ACD at the point D [3.36].

**Step 8.** Since BD is tangent to circle ACD at D, and DC is a chord of circle ACD drawn from the point of tangency D, the angle BDC (between the tangent BD and the chord DC) equals the angle in the alternate segment, which is angle DAC [3.32].

**Step 9.** Since A is the center of circle BDE and both B and D lie on circle BDE, we have AB = AD. Therefore triangle ABD is isosceles, and angle ABD = angle ADB [1.5].

**Step 10.** Since C lies between A and B on segment AB, the ray from B toward C is the same as the ray from B toward A. Therefore angle DBC = angle ABD.

**Step 11.** In triangle BDC, the sum of angles is two right angles: angle BDC + angle DCB + angle DBC = two right angles [1.32].

**Step 12.** In triangle ABD, the sum of angles is two right angles: angle DAB + angle ABD + angle ADB = two right angles [1.32]. Since angle ABD = angle ADB (Step 9), this gives angle DAB + 2 * angle ABD = two right angles, so angle DAB = two right angles minus 2 * angle ABD.

**Step 13.** Since C lies on ray AB from A, we have angle DAC = angle DAB. From Step 8, angle BDC = angle DAC = angle DAB. Substituting into the equation from Step 11: angle DAB + angle DCB + angle DBC = two right angles. Using angle DBC = angle ABD (Step 10), this gives angle DAB + angle DCB + angle ABD = two right angles.

**Step 14.** From Step 12, angle DAB = two right angles minus 2 * angle ABD. Substituting into the result of Step 13: (two right angles minus 2 * angle ABD) + angle DCB + angle ABD = two right angles. Simplifying: angle DCB - angle ABD = 0, so angle DCB = angle ABD.

**Step 15.** In triangle BDC, angle DBC = angle ABD (Step 10) and angle DCB = angle ABD (Step 14), so angle DBC = angle DCB. Since the angles at the base BC of triangle BDC are equal, the sides opposite them are equal: BD = DC [1.6].

**Step 16.** Since BD = CA (Step 3) and BD = DC (Step 15), we have DC = CA.

**Step 17.** In triangle DCA, since DC = CA, triangle DCA is isosceles, and the base angles are equal: angle CDA = angle DAC [1.5].

**Step 18.** From Step 8, angle BDC = angle DAC. From Step 17, angle CDA = angle DAC. Therefore angle BDC = angle CDA.

**Step 19.** Since ray DC lies between rays DA and DB at vertex D (because C lies between A and B on segment AB, and the tangent BD at D to circle ACD ensures that B is on the opposite side of chord DA from C within the circle), we have angle ADB = angle ADC + angle CDB = angle CDA + angle BDC = angle DAC + angle DAC = 2 * angle DAC.

**Step 20.** Since angle DAC = angle DAB (Step 13) and angle ABD = angle ADB (Step 9), we conclude angle ABD = angle ADB = 2 * angle DAB. Thus in triangle ABD, which is isosceles with AB = AD, each of the base angles ABD and ADB is double the remaining angle DAB.

**Step 21.** Therefore the isosceles triangle ABD has been constructed such that each of the angles at the base BD is double the remaining angle at vertex A, which is what was required.

**USED:** 1.32, 1.5, 1.6, 2.11, 3.32, 3.36, 4.1, 4.5, P1, P3
**Human refs (from References field):** 1.32, 1.5, 1.6, 2.11, 3.32, 3.37, 4.5
**Jaccard:** 0.545 — AI adds ['3.36', '4.1', 'P1', 'P3']; Human adds ['3.37']

## Proposition 4.11
**Statement:** In a given circle to inscribe an equilateral and equiangular pentagon.

**Step 1.** Let the given circle be ABCDE. By Proposition 4.10, construct an isosceles triangle FGH such that each of the angles at G and H (the base angles) is double the remaining angle at F (the vertex angle). Thus angle GFH = 36 degrees, and angles FGH = FHG = 72 degrees.

**Step 2.** By Proposition 4.2, inscribe in circle ABCDE a triangle ACD equiangular with triangle FGH, so that angle CAD equals angle GFH, angle ACD equals angle FGH, and angle ADC equals angle FHG. Then angle CAD = 36 degrees, angle ACD = 72 degrees, and angle ADC = 72 degrees, with A, C, D on the circumference.

**Step 3.** By Proposition 1.9, bisect angle ACD by the line CB, so that angle ACB = angle BCD = 36 degrees. Likewise, by Proposition 1.9, bisect angle ADC by the line DE, so that angle ADE = angle EDC = 36 degrees. Let B and E be the points where these bisecting lines meet the circumference of circle ABCDE.

**Step 4.** Now the five inscribed angles ACB, BCD, CAD, ADE, and EDC are each equal to 36 degrees. Since these are angles at the circumference, by Proposition 3.26, equal angles at the circumference stand on equal arcs in the same circle. Therefore arc AB = arc BC = arc CD = arc DE = arc EA.

**Step 5.** Since arcs AB, BC, CD, DE, and EA are all equal, by Proposition 3.29, the chords subtending equal arcs in the same circle are equal. Therefore AB = BC = CD = DE = EA, and the pentagon ABCDE is equilateral.

**Step 6.** It remains to show the pentagon is equiangular. Each interior angle of pentagon ABCDE is an inscribed angle in the circle. The interior angle at A, namely angle EAB, stands on the arc from E to B passing through C and D (that is, arc EDCB on the far side), which comprises arcs BC, CD, and DE, three of the five equal arcs. Similarly, the interior angle at B, namely angle ABC, stands on arc AED (comprising arcs CD, DE, and EA), again three of the five equal arcs. The same holds for each vertex: each interior angle stands on an arc equal to three-fifths of the circumference. By Proposition 3.27, angles standing on equal arcs in the same circle are equal. Therefore all five interior angles of pentagon ABCDE are equal, and the pentagon is equiangular.

**Step 7.** Since pentagon ABCDE is both equilateral and equiangular, and each of its vertices lies on the circumference of circle ABCDE, by Definition D4.3 it is inscribed in the circle. Therefore, in the given circle an equilateral and equiangular pentagon has been inscribed, which is what was required.

**USED:** 1.9, 3.26, 3.27, 3.29, 4.10, 4.2, D4.3
**Human refs (from References field):** 1.9, 3.26, 3.27, 3.29, 4.10, 4.2
**Jaccard:** 0.857 — AI adds ['D4.3']

## Proposition 4.12
**Statement:** About a given circle to circumscribe an equilateral and equiangular pentagon.

**Step 1.** Let the given circle have center O. By Proposition 4.11, inscribe an equilateral and equiangular pentagon ABCDE in the circle, so that AB = BC = CD = DE = EA and all interior angles of the pentagon are equal.

**Step 2.** By Definition D1.15, since A, B, C, D, E lie on the circle, OA = OB = OC = OD = OE (all are radii of the given circle).

**Step 3.** At each of the five vertices A, B, C, D, E, draw the straight line tangent to the circle at that point (by Proposition 3.16, the line drawn perpendicular to the radius at a point on the circle does not cut the circle, i.e., is tangent to it). By Proposition 3.18, each tangent is perpendicular to the radius drawn to the point of tangency. Thus OA is perpendicular to the tangent at A, OB is perpendicular to the tangent at B, and so on.

**Step 4.** Let the tangent at A and the tangent at B meet at point G; the tangent at B and the tangent at C meet at H; the tangent at C and the tangent at D meet at K; the tangent at D and the tangent at E meet at L; and the tangent at E and the tangent at A meet at M. Then GHKLM is a pentagon circumscribed about the circle, since each of its five sides (being a segment of a tangent line) touches the circle (Definition D4.4). By Postulate P1, join OG, OH, OK, OL, OM.

**Step 5.** Since the five chords AB, BC, CD, DE, EA of the inscribed pentagon are all equal (Step 1), by Proposition 3.28 the arcs AB, BC, CD, DE, EA are all equal. Then by Proposition 3.27, the central angles subtended by these equal arcs are equal: angle AOB = angle BOC = angle COD = angle DOE = angle EOA.

**Step 6.** Consider the right triangle OAG (right angle at A, since OA is perpendicular to the tangent at A by Step 3) and the right triangle OBG (right angle at B, since OB is perpendicular to the tangent at B). We have OA = OB (radii, Step 2) and OG is common. By Proposition 1.47, OG^2 = OA^2 + AG^2 and OG^2 = OB^2 + BG^2. Since OA = OB, it follows that AG^2 = BG^2, and therefore AG = BG. Moreover, the right triangles OAG and OBG share hypotenuse OG with equal legs OA = OB and equal legs AG = BG, so by Proposition 1.8 (SSS), these triangles are congruent, giving angle AOG = angle BOG. Therefore OG bisects angle AOB.

**Step 7.** By the same reasoning applied at each external point: from H, the tangent segments HB = HC and angle BOH = angle COH; from K, KC = KD and angle COK = angle DOK; from L, LD = LE and angle DOL = angle EOL; and from M, ME = MA and angle EOM = angle AOM.

**Step 8.** Since angle AOB = angle BOC (Step 5), and OG bisects angle AOB while OH bisects angle BOC (Steps 6 and 7), we have angle BOG = (1/2) angle AOB = (1/2) angle BOC = angle BOH. Now consider the right triangles OBG and OBH: they share leg OB, have equal right angles at B (by Step 3), and have equal angles BOG = BOH at vertex O. By Proposition 1.26 (AAS), triangle OBG is congruent to triangle OBH. Therefore BG = BH.

**Step 9.** Since G, B, H all lie on the tangent line at B (G and H are defined as the intersections of adjacent tangents with the tangent at B), and B lies between G and H, we have GH = GB + BH (Common Notion CN2). Similarly, HK = HC + CK, KL = KD + DL, LM = LE + EM, and MG = MA + AG.

**Step 10.** From Step 8, BG = BH. By the same argument applied at each vertex: at C, using angle BOC = angle COD and the bisection by OH and OK, we obtain CH = CK. At D, DK = DL. At E, EL = EM. At A, AM = AG.

**Step 11.** From Step 7, HB = HC (tangent segments from H). Combined with Step 8 (BG = BH) and Step 10 (CH = CK), we have BG = BH = HC = CK (since BG = BH and BH = HC by tangent segments, and HC = CK by Step 10). By the same chain of equalities: CK = DK, DK = DL, DL = EL, EL = EM, EM = AM, AM = AG, and AG = BG (by CN1, transitivity).

**Step 12.** Therefore GH = GB + BH = BH + HC = HK (by Step 9 and the equalities from Step 11). Similarly, HK = HC + CK = CK + KD = KL, and KL = KD + DL = DL + LE = LM, and LM = LE + EM = EM + MA = MG. Hence GH = HK = KL = LM = MG, and the pentagon GHKLM is equilateral.

**Step 13.** It remains to show the pentagon is equiangular. Consider angle GHK at vertex H. In right triangle OBH, angle OBH = 90 degrees and angle BOH = (1/2) angle BOC (Step 8), so angle BHO = 90 - (1/2) angle BOC (by Proposition 1.32, the angle sum of a triangle equals two right angles). Similarly, in right triangle OCH, angle OCH = 90 degrees and angle COH = (1/2) angle BOC, so angle CHO = 90 - (1/2) angle BOC.

**Step 14.** Therefore angle GHK = angle BHC = angle BHO + angle CHO = [90 - (1/2) angle BOC] + [90 - (1/2) angle BOC] = 180 - angle BOC (by CN2).

**Step 15.** By the same reasoning at each vertex: angle HKL = 180 - angle COD, angle KLM = 180 - angle DOE, angle LMG = 180 - angle EOA, and angle MGH = 180 - angle AOB. Since angle AOB = angle BOC = angle COD = angle DOE = angle EOA (Step 5), all five angles of pentagon GHKLM are equal.

**Step 16.** Therefore GHKLM is an equilateral and equiangular pentagon circumscribed about the given circle, which is what was required.

**USED:** 1.26, 1.32, 1.47, 1.8, 3.16, 3.18, 3.27, 3.28, 4.11, CN1, CN2, D1.15, D4.4, P1
**Human refs (from References field):** 1.26, 1.47, 1.8, 3.1, 3.16, 3.18, 3.27, 4.11
**Jaccard:** 0.467 — AI adds ['1.32', '3.28', 'CN1', 'CN2', 'D1.15', 'D4.4', 'P1']; Human adds ['3.1']

## Proposition 4.13
**Statement:** In a given pentagon, which is equilateral and equiangular, to inscribe a circle.

**Step 1.** Let ABCDE be the given equilateral and equiangular pentagon. Bisect angle BCD by the straight line CF and angle CDE by the straight line DF [1.9], and let CF and DF meet at the point F within the pentagon.

**Step 2.** From F, draw FG perpendicular to AB, FH perpendicular to BC, FK perpendicular to CD, FL perpendicular to DE, and FM perpendicular to EA [1.12].

**Step 3.** Since the pentagon is equiangular, angle BCD equals angle CDE. Because CF bisects angle BCD, angle FCB equals half of angle BCD. Because DF bisects angle CDE, angle FDC equals half of angle CDE. Since angle BCD equals angle CDE, it follows that angle FCD equals angle FDC [CN1].

**Step 4.** In triangle FCD, since angle FCD equals angle FDC, the side FC equals the side FD [1.6].

**Step 5.** Now consider triangles FHC and FKC. Angle FHC and angle FKC are both right angles [D1.10]. Angle FCH equals angle FCK since CF bisects angle BCD. The side FC is common. Therefore triangle FHC is congruent to triangle FKC [1.26], and so FH equals FK.

**Step 6.** Similarly, consider triangles FKD and FLD. Angle FKD and angle FLD are both right angles. Angle FDK equals angle FDL since DF bisects angle CDE. The side FD is common. Therefore triangle FKD is congruent to triangle FLD [1.26], and so FK equals FL.

**Step 7.** Since the pentagon is equilateral, BC equals ED; and since it is equiangular, angle FCB equals angle FDE (both being half of equal angles as shown in Step 3). Also FC equals FD [Step 4]. Therefore, by SAS, triangle BCF is congruent to triangle EDF [1.4]. Hence BF equals EF and angle FBC equals angle FED.

**Step 8.** Since angle ABC equals angle DEA (equiangular pentagon) and angle FBC equals angle FED [Step 7], subtracting equals from equals gives angle ABF equals angle AEF [CN3]. Therefore BF bisects angle ABC and EF bisects angle DEA.

**Step 9.** Consider triangles FGB and FHB. Angle FGB and angle FHB are both right angles. Angle FBG equals angle FBH since BF bisects angle ABC [Step 8]. The side BF is common. Therefore triangle FGB is congruent to triangle FHB [1.26], and so FG equals FH.

**Step 10.** Similarly, consider triangles FLE and FME. Angle FLE and angle FME are both right angles. Angle FEL equals angle FEM since EF bisects angle DEA [Step 8]. The side FE is common. Therefore triangle FLE is congruent to triangle FME [1.26], and so FL equals FM.

**Step 11.** From Steps 5, 6, 9, and 10 we have FG equals FH, FH equals FK, FK equals FL, and FL equals FM. Therefore FG equals FH equals FK equals FL equals FM; that is, all five perpendicular distances from F to the sides of the pentagon are equal [CN1].

**Step 12.** With centre F and radius FG, describe the circle GHKLM [P3]. Since FG, FH, FK, FL, FM are all equal to the radius and each is perpendicular to its respective side, each side of the pentagon touches the circle at the foot of the perpendicular. For the straight line drawn at right angles to a radius at its extremity touches the circle [3.16].

**Step 13.** Therefore the circle GHKLM is inscribed in the pentagon ABCDE, since each side of the pentagon touches the circumference of the circle [D4.5]. This is what was required to do.

**USED:** 1.12, 1.26, 1.4, 1.6, 1.9, 3.16, CN1, CN3, D1.10, D4.5, P3
**Human refs (from References field):** 1.26, 1.4, 3.16
**Jaccard:** 0.273 — AI adds ['1.12', '1.6', '1.9', 'CN1', 'CN3', 'D1.10', 'D4.5', 'P3']

## Proposition 4.14
**Statement:** About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.

**Step 1.** Let ABCDE be the given equilateral and equiangular pentagon. We must circumscribe a circle about it, that is, find a circle whose circumference passes through each vertex A, B, C, D, E [D4.6].

**Step 2.** Bisect angle BCD by the line CF, and bisect angle CDE by the line DF [1.9]. Let F be the point at which CF and DF meet [P1].

**Step 3.** Since the pentagon is equiangular, angle BCD equals angle CDE. Since CF bisects angle BCD, angle FCD equals half of angle BCD. Since DF bisects angle CDE, angle FDC equals half of angle CDE. Because angle BCD equals angle CDE, it follows that angle FCD equals angle FDC.

**Step 4.** In triangle FCD, since angle FCD equals angle FDC, the side FC equals the side FD [1.6].

**Step 5.** Now consider triangles BCF and DCF. We have BC equals DC (the pentagon is equilateral), CF is common to both triangles, and angle BCF equals angle DCF (since CF bisects angle BCD). Therefore by the side-angle-side criterion, triangle BCF is congruent to triangle DCF [1.4]. Hence FB equals FD.

**Step 6.** Since FC equals FD (Step 4) and FB equals FD (Step 5), it follows that FB equals FC [CN1].

**Step 7.** Consider triangles BCF and EDF. We have BC equals ED (equilateral pentagon), FC equals FD (Step 4), and angle BCF equals angle EDF (since angle BCF is half of angle BCD, angle EDF is half of angle CDE, and angle BCD equals angle CDE). Therefore by the side-angle-side criterion, triangle BCF is congruent to triangle EDF [1.4]. Hence FB equals FE.

**Step 8.** From the congruence in Step 5, angle FBC equals angle FDC. Since angle FDC is half of angle CDE (because DF bisects angle CDE) and angle CDE equals angle ABC (equiangular pentagon), angle FBC equals half of angle ABC. Therefore angle ABF, which equals angle ABC minus angle FBC, equals half of angle ABC. Hence angle ABF equals angle FBC, and BF bisects angle ABC.

**Step 9.** Consider triangles ABF and CBF. We have AB equals CB (equilateral pentagon), BF is common, and angle ABF equals angle CBF (since BF bisects angle ABC, as shown in Step 8). Therefore by the side-angle-side criterion, triangle ABF is congruent to triangle CBF [1.4]. Hence FA equals FC.

**Step 10.** From Steps 4, 5, 6, 7, and 9, we have FA equals FC, FC equals FD, FB equals FC, and FB equals FE. Therefore FA equals FB equals FC equals FD equals FE [CN1].

**Step 11.** Describe the circle with center F and radius FA [P3, D1.15]. Since FA equals FB equals FC equals FD equals FE, this circle passes through all five vertices A, B, C, D, E.

**Step 12.** Therefore about the given equilateral and equiangular pentagon ABCDE, a circle has been circumscribed [D4.6]. Q.E.F.

**USED:** 1.4, 1.6, 1.9, CN1, D1.15, D4.6, P1, P3
**Human refs (from References field):** 1.6
**Jaccard:** 0.125 — AI adds ['1.4', '1.9', 'CN1', 'D1.15', 'D4.6', 'P1', 'P3']

## Proposition 4.15
**Statement:** In a given circle to inscribe an equilateral and equiangular hexagon.

**Step 1.** Let the given circle have center G, found by 3.1, and let a diameter AD be drawn through G [P1].

**Step 2.** With center D and radius DG, describe a circle [P3]. Let this circle meet the given circle at points C and E, where C and E lie on opposite sides of the line AD.

**Step 3.** Join CG, GE, CD, DE, and produce CG to B and EG to F, where B and F are the second intersections of these lines with the given circle [P1].

**Step 4.** Since GD and GC are both radii of the given circle, GD equals GC [D1.15]. Since DC is a radius of the circle with center D and radius DG, DC equals DG. Therefore GD equals GC equals DC, and triangle GCD is equilateral [D1.20].

**Step 5.** Similarly, since GD and GE are radii of the given circle, GD equals GE [D1.15]. Since DE is a radius of the circle with center D and radius DG, DE equals DG. Therefore GD equals GE equals DE, and triangle GDE is equilateral [D1.20].

**Step 6.** Since triangle GCD is equilateral, its three sides are equal, so by 1.5 the base angles are equal. By 1.32, the three angles of triangle GCD sum to two right angles. Since all three angles are equal, each angle is one-third of two right angles. In particular, angle CGD equals one-third of two right angles.

**Step 7.** By the same reasoning applied to equilateral triangle GDE, angle DGE equals one-third of two right angles.

**Step 8.** Since CGB is a straight line (CG produced to B), angle CGD and angle DGB together equal two right angles [1.13]. Since angle CGD equals one-third of two right angles, angle DGB equals two-thirds of two right angles.

**Step 9.** Since EGF is a straight line (EG produced to F), angle DGE and angle DGF together equal two right angles [1.13]. Since angle DGE equals one-third of two right angles, angle DGF equals two-thirds of two right angles.

**Step 10.** Since C and E are on opposite sides of diameter AD, and angle CGD equals one-third of two right angles and angle DGE equals one-third of two right angles, the angle CGE (containing D) equals angle CGD plus angle DGE, which is two-thirds of two right angles [CN2].

**Step 11.** Since CGB is a straight line, angles CGE and EGB together equal two right angles [1.13]. Since angle CGE equals two-thirds of two right angles, angle EGB equals one-third of two right angles.

**Step 12.** Since EGF is a straight line, angles CGE and CGF together equal two right angles [1.13]. Since angle CGE equals two-thirds of two right angles, angle CGF equals one-third of two right angles.

**Step 13.** Since AGD is a straight line (diameter), angle DGB and angle BGA together equal two right angles [1.13]. Since angle DGB equals two-thirds of two right angles, angle BGA equals one-third of two right angles.

**Step 14.** Since AGD is a straight line, angle DGF and angle FGA together equal two right angles [1.13]. Since angle DGF equals two-thirds of two right angles, angle FGA equals one-third of two right angles.

**Step 15.** Therefore the six angles at center G, namely CGD, DGE, EGB, BGA, AGF, and FGC, are each equal to one-third of two right angles.

**Step 16.** Since these six equal central angles stand at the center of the circle, the six arcs they subtend, namely arcs CD, DE, EB, BA, AF, and FC, are all equal to one another [3.26].

**Step 17.** Since the six arcs are all equal, the straight lines subtending them are equal [3.29]. Therefore CD equals DE equals EB equals BA equals AF equals FC, and hexagon ABCDEF is equilateral.

**Step 18.** Now consider any interior angle of the hexagon, say angle FCD at vertex C. This is an inscribed angle standing on arc FDEBAF, that is, the arc from D to F not passing through C. This arc is the sum of four of the six equal arcs (arcs DE, EB, BA, AF), hence equals four-sixths of the whole circumference.

**Step 19.** Similarly, each interior angle of the hexagon is an inscribed angle standing on an arc equal to four of the six equal arcs. Since all these arcs are equal to one another, the inscribed angles standing on them are equal to one another [3.27].

**Step 20.** Therefore hexagon ABCDEF is also equiangular.

**Step 21.** Thus in the given circle an equilateral and equiangular hexagon has been inscribed [D4.3]. Q.E.F.

**USED:** 1.13, 1.32, 1.5, 3.1, 3.26, 3.27, 3.29, CN2, D1.15, D1.20, D4.3, P1, P3
**Human refs (from References field):** 1.15, 1.32, 1.5, 3.26, 3.27, 3.29
**Jaccard:** 0.357 — AI adds ['1.13', '3.1', 'CN2', 'D1.15', 'D1.20', 'D4.3', 'P1', 'P3']; Human adds ['1.15']

## Proposition 4.16
**Statement:** In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular.

**Step 1.** Let ABCDE be the given circle. Construct an equilateral triangle [1.1], and by 4.2, inscribe in circle ABCDE a triangle equiangular with it, so that the inscribed triangle is equilateral. Let one side of this inscribed equilateral triangle be AC, with A and C on the circumference.

**Step 2.** By 4.11, inscribe a regular equilateral and equiangular pentagon in the same circle ABCDE. Let one side of this pentagon be AB, where A is the same vertex shared with the triangle side AC, and B lies on the circumference between A and C along the arc on which C lies.

**Step 3.** Since the inscribed equilateral triangle has three equal sides, by 3.28 (in equal circles, equal straight lines cut off equal arcs), the three arcs subtended by its sides are equal. Therefore each side of the equilateral triangle subtends one-third of the circumference. In particular, arc AC (the minor arc from A to C passing through B) is one-third of the whole circumference, that is, five-fifteenths of the circumference.

**Step 4.** Similarly, since the inscribed regular pentagon has five equal sides, by 3.28 the five arcs subtended by its sides are equal. Therefore each side of the pentagon subtends one-fifth of the circumference. In particular, arc AB is one-fifth of the whole circumference, that is, three-fifteenths of the circumference.

**Step 5.** The arc AC (from A to C through B) equals five-fifteenths of the circumference, and the arc AB equals three-fifteenths of the circumference. Since B lies on arc AC between A and C, the remaining arc BC equals arc AC minus arc AB, that is, five-fifteenths minus three-fifteenths, which is two-fifteenths of the circumference.

**Step 6.** By 3.30, bisect the arc BC at the point E. Then each of the arcs BE and EC equals one-fifteenth of the circumference.

**Step 7.** Join BE and EC as straight lines [P1]. Each of these chords subtends an arc equal to one-fifteenth of the circumference. Therefore BE and EC are equal chords in the circle, since by 3.29 (in equal circles, the straight lines subtending equal arcs are equal) equal arcs are subtended by equal straight lines.

**Step 8.** By 4.1, fit straight lines equal to BE (or EC) successively into the circle, proceeding around the entire circumference from E. Since the whole circumference is fifteen times the arc of one-fifteenth, exactly fifteen such equal chords can be fitted around the circle, producing the vertices of a fifteen-sided figure inscribed in the circle.

**Step 9.** The inscribed fifteen-angled figure is equilateral, since all fifteen sides are equal to BE, each subtending an arc of one-fifteenth of the circumference, and equal arcs in the same circle are subtended by equal chords [3.29].

**Step 10.** The inscribed fifteen-angled figure is equiangular. Each interior angle of the inscribed polygon is an angle in a segment, and each such angle stands on an arc equal to thirteen-fifteenths of the circumference (the whole circumference minus the one-fifteenth arc subtended by the opposite side). Since these arcs are all equal, by 3.27 (in equal circles, the angles standing on equal circumferences are equal, whether at the centres or at the circumferences), all the inscribed angles are equal to one another.

**Step 11.** Therefore in the given circle a fifteen-angled figure has been inscribed which is both equilateral and equiangular, which is what was required.

**USED:** 1.1, 3.27, 3.28, 3.29, 3.30, 4.1, 4.11, 4.2, P1
**Human refs (from References field):** 3.30
**Jaccard:** 0.111 — AI adds ['1.1', '3.27', '3.28', '3.29', '4.1', '4.11', '4.2', 'P1']
