# Book 3 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 3.1
**Statement:** To find the centre of a given circle.

**Step 1.** Let ABC be the given circle. Draw any chord AB within the circle by taking two points A and B on the circumference and joining them [P1].

**Step 2.** Bisect AB at the point D [1.10].

**Step 3.** From D, draw DC at right angles to AB [1.11], and produce it in both directions to meet the circumference of the circle at points E and F [P2].

**Step 4.** Bisect EF at the point G [1.10]. I claim that G is the centre of circle ABC.

**Step 5.** Suppose, for the sake of contradiction, that G is not the centre. Let some other point H be the centre. Join HA, HD, and HB [P1].

**Step 6.** Since H is the centre of the circle, HA equals HB, for all straight lines from the centre to the circumference are equal [D1.15, D1.16].

**Step 7.** Since D is the midpoint of AB (by Step 2), DA equals DB.

**Step 8.** HD is common to triangles HDA and HDB.

**Step 9.** Therefore, in triangles HDA and HDB, we have HA equal to HB, DA equal to DB, and HD common. By the SSS congruence theorem, triangle HDA is congruent to triangle HDB, and in particular angle HDA equals angle HDB [1.8].

**Step 10.** Since the straight line HD standing on the straight line AB makes the adjacent angles HDA and HDB equal to one another, each of the angles HDA and HDB is a right angle [D1.10].

**Step 11.** But by construction (Step 3), angle GDA is also a right angle, since DC (and hence GD, which lies along EF) was drawn perpendicular to AB at D.

**Step 12.** Since angle HDA is a right angle and angle GDA is a right angle, angle HDA equals angle GDA, for all right angles are equal to one another [P4].

**Step 13.** But H and G are assumed to be distinct points. Therefore one of the angles HDA and GDA is a proper part of the other: either GDA is part of HDA or HDA is part of GDA. Hence they cannot be equal, for the whole is greater than the part [CN5].

**Step 14.** This contradicts the conclusion of Step 12. Therefore the assumption that the centre is some point other than G is false.

**Step 15.** Hence G is the centre of the given circle ABC, and it has been found by the given construction. Q.E.F.

**USED:** 1.10, 1.11, 1.8, CN5, D1.10, D1.15, D1.16, P1, P2, P4
**Human refs (from References field):** 1.8, D1.10
**Jaccard:** 0.200 — AI adds ['1.10', '1.11', 'CN5', 'D1.15', 'D1.16', 'P1', 'P2', 'P4']

## Proposition 3.2
**Statement:** If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

**Step 1.** Let ABC be a circle, and let B and C be two points taken on its circumference. Join BC [P1]. We must show that the straight line BC falls within the circle.

**Step 2.** Find the centre D of circle ABC [3.1]. Join DB and DC [P1].

**Step 3.** Take an arbitrary point F on the line segment BC, between B and C. Join DF [P1].

**Step 4.** Since DB and DC are both radii of circle ABC, we have DB = DC [D1.15].

**Step 5.** Since in triangle DBC the side DB equals the side DC, the angle DBC equals the angle DCB [1.5].

**Step 6.** Consider triangle DFC. The angle BFD is an exterior angle of triangle DFC (since F lies between B and C, so BF is the side of triangle DFC produced beyond F to B). Therefore angle BFD is greater than the interior and opposite angle DCF [1.16]. But angle DCF is the same as angle DCB.

**Step 7.** From Steps 5 and 6, angle BFD is greater than angle DCB, which equals angle DBC. But angle DBC is the same as angle DBF (since F lies on BC between B and C). Therefore angle BFD is greater than angle DBF.

**Step 8.** In triangle DBF, since angle BFD is greater than angle DBF, the side opposite the greater angle is greater than the side opposite the lesser angle [1.19]. Therefore DB is greater than DF.

**Step 9.** Since DB is a radius of circle ABC, and DF is less than DB, the point F is at a distance from the centre D that is less than the radius. Therefore F lies within the circle [D1.15].

**Step 10.** Since F was an arbitrary point on BC between B and C, every such point lies within the circle. The endpoints B and C lie on the circumference. Therefore the straight line BC falls within the circle [D1.15].

**Step 11.** Therefore, if on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle. Q.E.F.

**USED:** 1.16, 1.19, 1.5, 3.1, D1.15, P1
**Human refs (from References field):** 1.16, 1.19, 1.5, 3.1
**Jaccard:** 0.667 — AI adds ['D1.15', 'P1']

## Proposition 3.3
**Statement:** If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

**Step 1.** Let ABC be a circle, and let CD be a straight line through the centre which bisects the straight line AB not through the centre at the point E. We must first prove that CD cuts AB at right angles.

**Step 2.** Find the centre F of the circle ABC [3.1]. Join FA and FB [P1].

**Step 3.** Since F is the centre of the circle, FA equals FB [D1.15].

**Step 4.** Since CD bisects AB at E, AE equals EB [given].

**Step 5.** And FE is common to triangles FEA and FEB.

**Step 6.** Therefore the three sides of triangle FEA are equal respectively to the three sides of triangle FEB: FA equals FB, AE equals EB, and FE is common.

**Step 7.** Therefore angle FEA equals angle FEB [1.8].

**Step 8.** But when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right [D1.10].

**Step 9.** Therefore each of the angles FEA and FEB is a right angle. Hence CD cuts AB at right angles.

**Step 10.** Now conversely, let CD cut AB at right angles at E. We must prove that CD also bisects AB, that is, that AE equals EB.

**Step 11.** With the same construction, let F be the centre of the circle, and join FA and FB [3.1, P1].

**Step 12.** Since F is the centre of the circle, FA equals FB [D1.15].

**Step 13.** Since CD cuts AB at right angles at E, angle FEA is a right angle and angle FEB is a right angle.

**Step 14.** Now in the right-angled triangle FEA, by the Pythagorean theorem, the square on FA equals the sum of the squares on FE and AE [1.47].

**Step 15.** Likewise in the right-angled triangle FEB, the square on FB equals the sum of the squares on FE and EB [1.47].

**Step 16.** Since FA equals FB [Step 12], the square on FA equals the square on FB.

**Step 17.** Therefore the sum of the squares on FE and AE equals the sum of the squares on FE and EB [CN1].

**Step 18.** Subtracting the square on FE from each, the square on AE equals the square on EB [CN3].

**Step 19.** Therefore AE equals EB. Hence CD bisects AB. Q.E.D.

**USED:** 1.47, 1.8, 3.1, CN1, CN3, D1.10, D1.15, P1
**Human refs (from References field):** 1.26, 1.5, 1.8, D1.10
**Jaccard:** 0.200 — AI adds ['1.47', '3.1', 'CN1', 'CN3', 'D1.15', 'P1']; Human adds ['1.26', '1.5']

## Proposition 3.4
**Statement:** If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.

**Step 1.** Let ABCD be a circle, and let AC and BD be two straight lines in it which cut one another at the point E, and which are not through the centre. I say that they do not bisect one another.

**Step 2.** For suppose, if possible, that they do bisect one another, so that AE equals EC and BE equals ED.

**Step 3.** Find the centre F of the circle ABCD [3.1]. Draw the straight line FE from F to E [P1].

**Step 4.** Since the straight line FE passes through the centre F and bisects the chord AC at E (for AE equals EC by assumption), by 3.3, FE cuts AC at right angles. Therefore angle FEA is a right angle.

**Step 5.** Again, since the straight line FE passes through the centre F and bisects the chord BD at E (for BE equals ED by assumption), by 3.3, FE cuts BD at right angles. Therefore angle FEB is a right angle.

**Step 6.** But the angle FEA was shown to be a right angle, and the angle FEB was shown to be a right angle. Since all right angles are equal to one another [P4], angle FEA equals angle FEB.

**Step 7.** Now AC and BD are distinct straight lines (neither passes through the centre), so the rays EA and EB from E point in different directions. Therefore one of the angles FEA and FEB is a proper part of the other; that is, the lesser is contained within the greater.

**Step 8.** But the whole is greater than the part [CN5], so angle FEA cannot equal angle FEB. This contradicts Step 6.

**Step 9.** Therefore the assumption in Step 2 is false: AC and BD do not bisect one another. This is what was to be proved.

**USED:** 3.1, 3.3, CN5, P1, P4
**Human refs (from References field):** 3.1, 3.3
**Jaccard:** 0.400 — AI adds ['CN5', 'P1', 'P4']

## Proposition 3.5
**Statement:** If two circles cut one another, they will not have the same centre.

**Step 1.** Let circles ABC and CDG cut one another at the point C. Suppose, for the sake of contradiction, that they have the same centre; call it E.

**Step 2.** Since the two circles cut one another, there exists a point F on the circumference of circle ABC that lies within circle CDG. Draw the straight line EFC from E through F to C by P1, and extend EF beyond F to meet the circumference of circle CDG at a point G by P2, so that E, F, G lie on a straight line with F between E and G.

**Step 3.** Since E is the centre of circle ABC, and both F and C lie on the circumference of circle ABC, we have EC = EF by D1.15.

**Step 4.** Since E is the centre of circle CDG, and both C and G lie on the circumference of circle CDG, we have EC = EG by D1.15.

**Step 5.** From Steps 3 and 4, since EC = EF and EC = EG, we conclude EF = EG by CN1.

**Step 6.** But F lies between E and G on the straight line EFG, so EF is a part of EG. Therefore EG is greater than EF by CN5.

**Step 7.** This contradicts Step 5, which states that EF = EG. The assumption that the two circles have the same centre is therefore false.

**Step 8.** Therefore, if two circles cut one another, they do not have the same centre. Q.E.F.

**USED:** CN1, CN5, D1.15, P1, P2
**Human refs (from References field):** D1.15
**Jaccard:** 0.200 — AI adds ['CN1', 'CN5', 'P1', 'P2']

## Proposition 3.6
**Statement:** If two circles touch one another, they will not have the same centre.

**Step 1.** Let circles ABC and CDE touch one another at the point C. I say they do not have the same centre.

**Step 2.** Suppose, for the sake of contradiction, that they do have the same centre. Let it be F.

**Step 3.** Join FC [P1], and draw any other straight line FEB through F, meeting circle ABC at B and circle CDE at E [P1, P2].

**Step 4.** Since F is the centre of circle ABC, we have FC = FB [D1.15, D1.16].

**Step 5.** Since F is the centre of circle CDE, we have FC = FE [D1.15, D1.16].

**Step 6.** Since FC = FB and FC = FE, it follows that FE = FB [CN1].

**Step 7.** But FE is less than FB, since E lies between F and B on line FEB, so FE is a part of FB. Therefore the whole FB is greater than the part FE [CN5].

**Step 8.** This contradicts Step 6, which states FE = FB. The assumption that the two circles have the same centre leads to a contradiction.

**Step 9.** Therefore, if two circles touch one another, they will not have the same centre. Q.E.D.

**USED:** CN1, CN5, D1.15, D1.16, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN1', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1', 'P2']

## Proposition 3.7
**Statement:** If on the diameter of a circle a point be taken which is not the centre of the circle, and from the point straight lines fall upon the circle, that will be greatest on which the centre is, the remainder of the same diameter will be least, and of the rest  the nearer to the straight line through the centre is always greater than the more remote, and only two equal straight lines will fall from the point on the circle, one on each side of the least straight line.

**Step 1.** Let ABCD be a circle with center E. Let AD be a diameter and let F be a point on AD different from E. From F, let straight lines FB, FC be drawn to the circumference, where B is nearer to the straight line FA than C is along the arc on the same side. Join EB and EC [P1].

**Step 2.** Since E is the center of the circle, we have EA = EB = EC = ED, for all are radii of the circle [D1.15, D1.16].

**Step 3.** (FA is greatest.) In triangle BEF, the sum of two sides EB + EF is greater than the remaining side BF [1.20]. Since EB = EA [Step 2], it follows that EA + EF > BF. But A, E, F all lie on the diameter in that order, so EA + EF = FA. Therefore FA > FB. The same argument applies to any straight line drawn from F to the circumference. Hence FA is the greatest of all such lines.

**Step 4.** (FD is least.) In triangle BEF, the sum of two sides BF + FE is greater than the remaining side BE [1.20]. Since BE = DE [Step 2], we have BF + FE > DE. Now F lies on diameter AD between E and D (or between A and E), so in either case DE = DF + FE. Therefore BF + FE > DF + FE. Subtracting FE from both sides, BF > DF [CN3]. The same argument applies to any straight line drawn from F to the circumference. Hence FD is the least of all such lines.

**Step 5.** (Nearer to FA is greater than more remote.) Consider triangles EFB and EFC with B nearer to A than C along the circumference. We have EF = EF (common side), and EB = EC (both radii) [Step 2]. Since B is nearer to A along the arc, the angle BEF is greater than the angle CEF. This is because EB, being directed toward B which is closer to A, makes a larger angle with EF (which points from E toward D, away from A) than EC does. Therefore, since in the two triangles EFB and EFC the two sides EF, EB equal the two sides EF, EC respectively, and the included angle BEF is greater than the included angle CEF, the base FB is greater than the base FC [1.24]. Hence of the remaining straight lines, the nearer to FA is always greater than the more remote.

**Step 6.** (Only two equal lines from F, one on each side of FD.) On the straight line EF, at the point E, construct the angle FEH on the opposite side of the diameter from B, equal to the angle FEB [1.23]. Let H be the point where the second arm of this angle meets the circle [P3]. Join FH [P1].

**Step 7.** In triangles FEB and FEH, we have EF = EF (common), EB = EH (both radii) [Step 2], and angle FEB = angle FEH (by construction) [Step 6]. Therefore triangle FEB is congruent to triangle FEH, and in particular FB = FH [1.4].

**Step 8.** We now show no other straight line from F to the circumference equals FB apart from FH. Suppose FK is another line from F to the circle with FK = FB, and K lies on the same side of the diameter as B. If K is nearer to A than B, then FK > FB by Step 5, contradicting FK = FB. If K is more remote from A than B, then FK < FB by Step 5, again contradicting FK = FB. So on the side of B, no other line equals FB. By the same reasoning on the other side, no line other than FH equals FB. Therefore exactly two equal straight lines fall from F on the circle, one on each side of the least line FD.

**Step 9.** Therefore, if on the diameter of a circle a point be taken which is not the centre of the circle, the straight line on which the centre lies (FA) is greatest, the remainder of the diameter (FD) is least, of the rest the nearer to FA is always greater than the more remote, and only two equal straight lines fall from the point on the circle, one on each side of the least straight line. Q.E.F.

**USED:** 1.20, 1.23, 1.24, 1.4, CN3, D1.15, D1.16, P1, P3
**Human refs (from References field):** 1.20, 1.23, 1.24, 1.4
**Jaccard:** 0.444 — AI adds ['CN3', 'D1.15', 'D1.16', 'P1', 'P3']

## Proposition 3.8
**Statement:** If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest   the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

**Step 1.** Let there be a circle with centre M, and let a point A be taken outside the circle. Draw a straight line from A through M, meeting the circle at points B (on the near side, the convex circumference) and D (on the far side, the concave circumference), so that ABD is a diameter extended through A [P1]. Let other straight lines AE, AF, AG be drawn from A through to the circle at random, meeting the concave circumference at E, F, G and the convex circumference at corresponding points, arranged so that E is nearer to D than F, and F is nearer to D than G, on the concave circumference. Also let AH be drawn meeting the convex circumference at H on the other side of B from the other lines. We must show the required ordering properties.

**Step 2.** Join ME, MF, MG, MH [P1]. Since M is the centre, we have MD = ME = MF = MG = MH = MB, all being radii of the circle [D1.15].

**Step 3.** (AD is greatest among lines to the concave circumference.) Consider triangle AME. By 1.20 (any two sides of a triangle are together greater than the remaining side), AM + ME > AE. But ME = MD (radii), so AM + MD > AE, that is, AD > AE [CN5, since AD = AM + MD]. Hence AD is greater than AE. The same argument applies to AF, AG, and any other line from A to the concave circumference. Therefore AD, the line through the centre, is the greatest among lines falling on the concave circumference.

**Step 4.** (AE > AF, i.e., the nearer to AD is greater than the more remote on the concave circumference.) In triangles AME and AMF, we have ME = MF (radii), AM is common, and angle AME > angle AMF, since E is nearer to D than F on the concave circumference, meaning E is closer to the line AD, so the angle AME (measured at M between MA and ME) is less than angle AMF. Wait — we must be more careful about angles. Since E is nearer to D than F, the angle DME < angle DMF. Now angle AME = 180 degrees minus angle DME (since A, M, D are collinear and E is on the far side), so angle AME > angle AMF. By 1.24 (if two triangles have two sides equal to two sides respectively, and the included angle of the first is greater than the included angle of the second, then the base of the first is greater than the base of the second), in triangles AME and AMF, since AM = AM, ME = MF, and angle AME > angle AMF, we conclude AE > AF.

**Step 5.** By the same reasoning, since angle AMF > angle AMG (because F is nearer to D than G, so angle DMF < angle DMG, hence angle AMF = supplement of angle DMF > supplement of angle DMG = angle AMG), applying 1.24 to triangles AMF and AMG gives AF > AG. This establishes that of lines to the concave circumference, the nearer to AD is always greater than the more remote.

**Step 6.** (AB is least among lines to the convex circumference.) Consider any line from A to the convex circumference, say the line meeting it at K. Join MK. In triangle AMK, by 1.20, AK + KM > AM. Since KM = MB (radii), AK + MB > AM, so AK > AM - MB = AB. Therefore AB < AK. Since K was arbitrary on the convex circumference (other than B), AB is the least line from A to the convex circumference.

**Step 7.** (Ordering on the convex circumference: AH < AK when H is nearer to B than K.) Let H and K be points on the convex circumference with H nearer to B than K. Join MH, MK. Since H is nearer to B, the angle BMH < angle BMK. Now in triangles AMH and AMK, AM is common, MH = MK (radii). The angle AMH = angle AMB + angle BMH (since H is on the same side), but we must consider: A, M, B are collinear (B is on segment AM since A is outside and B is the near intersection). Actually, since A is outside the circle and B is between A and M (the near intersection point on the diameter), M is beyond B from A. So angle AMH is the angle at M in triangle AMH, and angle AMK is the angle at M in triangle AMK. Since H is nearer to B than K, the angle BMH < angle BMK. Because B lies on segment AM (between A and M), the angles AMH and BMH are the same angle. Thus angle AMH < angle AMK. By 1.24, in triangles AMH and AMK with AM common, MH = MK, and angle AMH < angle AMK, we get AH < AK. This shows the nearer to AB is less than the more remote on the convex circumference.

**Step 8.** (Only two equal lines from A to the circle, one on each side of the least line AB.) At point M, on the line MA, construct angle AML equal to angle AMH on the other side of line MA [1.23], with ML equal to MH (i.e., ML is a radius) [P3]. Then L is on the circle. In triangles AMH and AML, AM is common, MH = ML (radii), and angle AMH = angle AML (by construction). By 1.4 (SAS), triangles AMH and AML are congruent, so AH = AL. Thus there exists one line on each side of AB equal to AH.

**Step 9.** We must show that no other line from A to the circle equals AH. Suppose AN is another line from A to the circle on the same side as AH, with AN = AH. Join MN. Then MN = MH (radii), AM is common, and AN = AH. By 1.8 (SSS), triangles AMN and AMH are congruent, so angle AMN = angle AMH. But if N is different from H, the angle AMN differs from angle AMH (since different points on the circle on the same side of the diameter yield different angles at M, as each radius to a distinct point makes a distinct angle with MA — for if two distinct radii made equal angles with MA on the same side, by 1.4 the endpoints would coincide, contradicting their distinctness). This is a contradiction. Therefore, on each side of the diameter, there is exactly one line from A equal to AH, giving exactly two equal lines total, one on each side of AB.

**Step 10.** Therefore, of the straight lines falling on the concave circumference from the external point, that through the centre is greatest, and the nearer to it is always greater than the more remote; of those falling on the convex circumference, that between the point and the diameter is least, and the nearer to the least is always less than the more remote; and only two equal straight lines fall on the circle from the point, one on each side of the least. Q.E.D.

**USED:** 1.20, 1.23, 1.24, 1.4, 1.8, CN5, D1.15, P1, P3
**Human refs (from References field):** 1.20, 1.21, 1.24, 1.4, 3.1
**Jaccard:** 0.273 — AI adds ['1.23', '1.8', 'CN5', 'D1.15', 'P1', 'P3']; Human adds ['1.21', '3.1']

## Proposition 3.9
**Statement:** If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

**Step 1.** Let the given circle be ABC, and let D be a point taken within it such that more than two equal straight lines fall from D on the circle. We must prove that D is the centre of circle ABC.

**Step 2.** Suppose, for the sake of contradiction, that D is not the centre of the circle.

**Step 3.** Since D is a point within circle ABC and D is not the centre, by Proposition 3.7, of all straight lines falling from D upon the circle, the greatest is that on which the centre lies, the least is the remainder of that same diameter, and of the rest, the nearer to the line through the centre is always greater than the more remote. Moreover, only two equal straight lines fall from D on the circle, one on each side of the least straight line [3.7].

**Step 4.** But by hypothesis, more than two equal straight lines fall from D on the circle, which contradicts the conclusion of 3.7 that only two equal straight lines can fall from D on the circle when D is not the centre.

**Step 5.** Therefore the assumption that D is not the centre is false. Hence D is the centre of circle ABC.

**Step 6.** Therefore, if a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle. Q.E.D.

**USED:** 3.7
**Human refs (from References field):** 1.8, 3.1, D1.10
**Jaccard:** 0.000 — AI adds ['3.7']; Human adds ['1.8', '3.1', 'D1.10']

## Proposition 3.10
**Statement:** A circle does not cut a circle at more points than two.

**Step 1.** Suppose, for the sake of contradiction, that two circles cut one another at more than two points. Let circle 1 and circle 2 cut one another at the distinct points B, G, and F (three or more common points).

**Step 2.** Find the center K of circle 1. [3.1]

**Step 3.** Join KB, KG, and KF. [P1]

**Step 4.** Since K is the center of circle 1, and B, G, F all lie on the circumference of circle 1, we have KB = KG = KF. [D1.15]

**Step 5.** Now B, G, F also lie on circle 2. Therefore three equal straight lines KB, KG, KF fall from the point K upon circle 2.

**Step 6.** Consider where K lies relative to circle 2. There are three cases: K lies within circle 2, K lies outside circle 2, or K lies on the circumference of circle 2.

**Step 7.** Case 1: Suppose K lies within circle 2. Since more than two equal straight lines (namely KB, KG, KF) fall from the point K upon circle 2, by Proposition 3.9, the point K is the center of circle 2. But then circles 1 and 2 have the same center K, and yet they cut one another. This contradicts Proposition 3.5, which states that if two circles cut one another, they do not have the same center. [3.9, 3.5]

**Step 8.** Case 2: Suppose K lies outside circle 2. By Proposition 3.8, if a point is taken outside a circle, only two equal straight lines can fall from the point on the circle. But three equal straight lines KB, KG, KF fall from K upon circle 2. This is a contradiction. [3.8]

**Step 9.** Case 3: Suppose K lies on the circumference of circle 2. Then K is itself a point on circle 2. Draw the diameter of circle 2 through K; that is, draw the line through K and the center of circle 2, meeting circle 2 again at the opposite point. Then K is a point on this diameter, and K is not the center of circle 2 (for if K were the center of circle 2 as well as the center of circle 1, this would contradict Proposition 3.5, since the circles cut one another). By Proposition 3.7, from a point on the diameter of a circle that is not the center, only two equal straight lines fall from the point on the circle. But three equal straight lines KB, KG, KF fall from K upon circle 2. This is a contradiction. [3.7, 3.5]

**Step 10.** In every case we have reached a contradiction. Therefore our assumption is false, and a circle does not cut a circle at more than two points. Q.E.D.

**USED:** 3.1, 3.5, 3.7, 3.8, 3.9, D1.15, P1
**Human refs (from References field):** 3.1, 3.5
**Jaccard:** 0.286 — AI adds ['3.7', '3.8', '3.9', 'D1.15', 'P1']

## Proposition 3.11
**Statement:** If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.

**Step 1.** Let two circles ABC (the larger) and ADE (the smaller) touch one another internally at the point A. Let G be the center of circle ABC, and H be the center of circle ADE. We must show that the straight line GH, produced, passes through A.

**Step 2.** Suppose, for the sake of contradiction, that the line GH produced does not pass through A. Join GA and HA by P1.

**Step 3.** The line from G through H, when produced, meets the circumference of the smaller circle ADE at some point D (on the far side of H from G), and meets the circumference of the larger circle ABC at some point B (beyond D from G). Since H is between G and D on this line, we have GD = GH + HD.

**Step 4.** Since G is the center of circle ABC, we have GA = GB, both being radii of circle ABC (by D1.15).

**Step 5.** Since H is the center of circle ADE, we have HA = HD, both being radii of circle ADE (by D1.15).

**Step 6.** Now consider triangle GHA. Since by our assumption G, H, and A are not collinear, this is a genuine triangle. By 1.20 (in any triangle, the sum of any two sides is greater than the remaining side), we have GH + HA > GA.

**Step 7.** Since HA = HD (Step 5), substituting gives GH + HD > GA. But GH + HD = GD (Step 3), so GD > GA.

**Step 8.** Since GA = GB (Step 4), we conclude GD > GB.

**Step 9.** Now, since the circles touch internally, the smaller circle ADE lies within the larger circle ABC. The point D lies on circle ADE, and D is not the point of tangency A (because by our assumption the line GH produced does not pass through A). Therefore D lies strictly inside circle ABC.

**Step 10.** Since D is inside circle ABC and B is on circle ABC, and the points G, D, B are collinear (all on the line through G and H produced), with D between G and B, the segment GD is a part of the segment GB. Therefore by CN5 (the whole is greater than the part), GB > GD.

**Step 11.** But Step 8 established GD > GB, which contradicts Step 10. This contradiction arises from our assumption that GH produced does not pass through A.

**Step 12.** Therefore the straight line joining the centres G and H, when produced, falls on the point of contact A. Q.E.D.

**USED:** 1.20, CN5, D1.15, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.20', 'CN5', 'D1.15', 'P1']

## Proposition 3.12
**Statement:** If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

**Step 1.** Let two circles touch one another externally at the point C, let F be the centre of the first circle, and let G be the centre of the second circle. I say that the straight line FG passes through C.

**Step 2.** Suppose, for the sake of contradiction, that FG does not pass through C. Then join FC and GC [P1]. Since F, C, G are not collinear by assumption, the points F, C, G form a triangle.

**Step 3.** In triangle FCG, the sum of the two sides FC and CG is greater than the remaining side FG [1.20]. That is, FC + CG > FG.

**Step 4.** Now since F is the centre of the first circle and C is a point on the first circle, FC is a radius of the first circle [D1.15]. Since the circles touch externally, the second circle lies entirely outside the first circle (for if any part of it fell inside, the circles would cut one another, contradicting D3.3). Therefore G, the centre of the second circle, lies outside the first circle, and the straight line FG, going from F (inside the first circle) to G (outside it), must meet the first circle at some point H between F and G.

**Step 5.** Since F is the centre of the first circle and H is on the first circle, FH is a radius of the first circle [D1.15]. Therefore FH equals FC [D1.15].

**Step 6.** Similarly, since G is the centre of the second circle and C is on the second circle, GC is a radius of the second circle [D1.15]. Since the first circle lies entirely outside the second circle, F lies outside the second circle. Therefore the line GF, going from G (inside the second circle) to F (outside it), must meet the second circle at some point K between G and F.

**Step 7.** Since G is the centre of the second circle and K is on the second circle, GK is a radius of the second circle [D1.15]. Therefore GK equals GC [D1.15].

**Step 8.** Since the circles touch externally and do not cut one another [D3.3], each circle lies outside the other. Therefore H (on the first circle) lies outside the second circle, and K (on the second circle) lies outside the first circle. The order of points along the line segment FG is F, H, K, G, so that FG equals FH plus HK plus KG.

**Step 9.** Since HK is a segment of the whole FG, HK is greater than or equal to zero, and FG equals FH + HK + KG [CN5]. Therefore FG is greater than or equal to FH + KG, that is, FG is greater than or equal to FC + GC (since FH = FC from Step 5 and GK = GC from Step 7).

**Step 10.** But from Step 3, FC + CG is greater than FG. This contradicts Step 9, which establishes that FG is greater than or equal to FC + GC.

**Step 11.** Therefore the assumption that FG does not pass through C is false. Hence the straight line joining the centres F and G passes through the point of contact C. Q.E.D.

**USED:** 1.20, CN5, D1.15, D3.3, P1
**Human refs (from References field):** 1.20
**Jaccard:** 0.200 — AI adds ['CN5', 'D1.15', 'D3.3', 'P1']

## Proposition 3.13
**Statement:** A circle does not touch a circle at more points than one, whether it touch it internally or externally.

**Step 1.** Suppose, for the sake of contradiction, that two circles touch one another at more than one point. We consider the two cases: internal tangency and external tangency.

**Step 2.** Case 1: Suppose circle ABDC with center G and circle ABEC with center H touch one another internally at two distinct points A and B.

**Step 3.** By Proposition 3.11, the straight line joining the centers G and H, when produced, falls on the point of contact. Since the circles touch at A, the line GH produced passes through A. Since the circles also touch at B, the line GH produced passes through B. Therefore G, H, A, and B are all collinear, lying on the single straight line through G and H [P1].

**Step 4.** Since G is the center of one circle and A, B lie on its circumference, GA equals GB [D1.15]. Since H is the center of the other circle and A, B lie on its circumference, HA equals HB [D1.15].

**Step 5.** Since A and B are distinct points on the line through G, and GA equals GB, the points A and B are equidistant from G on opposite sides of G. Hence G is the midpoint of segment AB.

**Step 6.** Since HA equals HB and A, B are distinct points on the same line, by the same reasoning H is the midpoint of segment AB.

**Step 7.** Since both G and H are the midpoint of segment AB, G coincides with H, meaning the two circles have the same center.

**Step 8.** But by Proposition 3.6, if two circles touch one another, they do not have the same center. This is a contradiction. Therefore two circles cannot touch internally at more than one point.

**Step 9.** Case 2: Suppose circle AKC with center G and circle ALC with center H touch one another externally at two distinct points A and C.

**Step 10.** By Proposition 3.12, the straight line joining the centers G and H passes through the point of contact. Since the circles touch at A, the line GH passes through A. Since the circles also touch at C, the line GH passes through C. Therefore G, H, A, and C are all collinear [P1].

**Step 11.** Since G is the center of one circle and A, C lie on its circumference, GA equals GC [D1.15]. Since H is the center of the other circle and A, C lie on its circumference, HA equals HC [D1.15].

**Step 12.** Since A and C are distinct points on the line through G, and GA equals GC, the points A and C are equidistant from G on opposite sides of G. Hence G is the midpoint of segment AC.

**Step 13.** Since HA equals HC and A, C are distinct points on the same line, H is likewise the midpoint of segment AC.

**Step 14.** Since both G and H are the midpoint of segment AC, G coincides with H, meaning the two circles have the same center.

**Step 15.** But by Proposition 3.6, if two circles touch one another, they do not have the same center. This is a contradiction. Therefore two circles cannot touch externally at more than one point.

**Step 16.** Since in both cases — internal and external tangency — the assumption that the circles touch at more than one point leads to a contradiction, a circle does not touch a circle at more points than one, whether it touch it internally or externally. Q.E.F.

**USED:** 3.11, 3.12, 3.6, D1.15, D3.3, P1
**Human refs (from References field):** 3.11, 3.2, D3.3
**Jaccard:** 0.286 — AI adds ['3.12', '3.6', 'D1.15', 'P1']; Human adds ['3.2']

## Proposition 3.14
**Statement:** In a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another.

**Step 1.** Let ABCD be a circle with centre E, and let AB and CD be equal straight lines in the circle. I say that AB and CD are equally distant from the centre. Conversely, let AB and CD be equally distant from the centre. I say that AB equals CD.

**Step 2.** Draw EF from E perpendicular to AB, and EG from E perpendicular to CD [P1]. Join EA and EC [P1].

**Step 3.** Since the straight line EF through the centre is perpendicular to AB, it bisects AB [3.3]. Therefore AF equals FB, and AB is double AF. Similarly, since EG through the centre is perpendicular to CD, it bisects CD [3.3]. Therefore CG equals GD, and CD is double CG.

**Step 4.** Since AB equals CD, and AB is double AF while CD is double CG, AF equals CG [CN1].

**Step 5.** Now EA and EC are radii of the circle, so EA equals EC [D1.15].

**Step 6.** In the right-angled triangle AEF, the square on EA equals the sum of the squares on EF and AF [1.47]. In the right-angled triangle CEG, the square on EC equals the sum of the squares on EG and CG [1.47].

**Step 7.** Since EA equals EC, the square on EA equals the square on EC. Since AF equals CG, the square on AF equals the square on CG. Therefore, subtracting equals from equals, the square on EF equals the square on EG [CN3]. Hence EF equals EG.

**Step 8.** But EF and EG are the perpendiculars drawn from the centre to AB and CD respectively. Therefore AB and CD are equally distant from the centre [D3.4].

**Step 9.** Now conversely, let AB and CD be equally distant from the centre, so that EF equals EG [D3.4]. I say that AB equals CD.

**Step 10.** With the same construction, EA and EC are radii of the circle, so EA equals EC [D1.15]. Therefore the square on EA equals the square on EC.

**Step 11.** In the right-angled triangle AEF, the square on EA equals the sum of the squares on EF and AF [1.47]. In the right-angled triangle CEG, the square on EC equals the sum of the squares on EG and CG [1.47].

**Step 12.** Since the square on EA equals the square on EC, the sum of the squares on EF and AF equals the sum of the squares on EG and CG. Since EF equals EG, the square on EF equals the square on EG. Therefore, subtracting equals from equals, the square on AF equals the square on CG [CN3]. Hence AF equals CG.

**Step 13.** Since AF equals FB, AB is double AF. Since CG equals GD, CD is double CG. Since AF equals CG, AB is double AF and CD is double CG, so AB equals CD [CN2].

**Step 14.** Therefore in a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another. Q.E.D.

**USED:** 1.47, 3.3, CN1, CN2, CN3, D1.15, D3.4, P1
**Human refs (from References field):** 1.47, 3.1, 3.3, D3.4
**Jaccard:** 0.333 — AI adds ['CN1', 'CN2', 'CN3', 'D1.15', 'P1']; Human adds ['3.1']

## Proposition 3.15
**Statement:** Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

**Step 1.** Let ABDC be a circle with center E, and let BC be a diameter. Let AD be any chord that is not a diameter. We are to show first that BC is greater than AD, and second that among non-diameter chords, the one nearer to the center is greater than the one more remote.

**Step 2.** Since E is the center of the circle, join EA and ED [P1]. Since E is the center, EA, EB, EC, and ED are all radii, so EA = EB and ED = EC [D1.15].

**Step 3.** Since AD is not a diameter, it does not pass through E [D1.17], so E, A, D form a triangle. By the triangle inequality, EA + ED > AD [1.20].

**Step 4.** Since E lies on the diameter BC between B and C, we have BC = BE + EC. But BE = EA and EC = ED [D1.15, CN1]. Therefore BC = EA + ED.

**Step 5.** Since EA + ED > AD [Step 3] and BC = EA + ED [Step 4], we conclude BC > AD. Thus the diameter is the greatest straight line in the circle.

**Step 6.** Now for the second part, let AD and FG be two chords neither of which is a diameter, with AD nearer to the center than FG. Draw EH perpendicular to AD and EK perpendicular to FG from center E [1.12, P1].

**Step 7.** Since EH is drawn from the center perpendicular to chord AD, it bisects AD, so AH = HD [3.3]. Similarly, since EK is drawn from the center perpendicular to chord FG, it bisects FG, so FK = KG [3.3].

**Step 8.** Since AD is nearer to the center than FG, the perpendicular EH is less than the perpendicular EK, that is, EH < EK [D3.4, D3.5].

**Step 9.** Since angle EHA is a right angle, triangle EHA is right-angled at H. By the Pythagorean theorem, the square on AE equals the sum of the squares on AH and HE, that is, AE^2 = AH^2 + HE^2 [1.47].

**Step 10.** Since angle EKF is a right angle, triangle EKF is right-angled at K. By the Pythagorean theorem, EF^2 = FK^2 + KE^2 [1.47].

**Step 11.** Since AE and EF are both radii of the circle, AE = EF [D1.15, CN1]. Therefore AE^2 = EF^2, and so AH^2 + HE^2 = FK^2 + KE^2 [CN1].

**Step 12.** Since EH < EK [Step 8], the square on EH is less than the square on EK, that is, HE^2 < KE^2. From the equality AH^2 + HE^2 = FK^2 + KE^2 [Step 11], since HE^2 < KE^2, it follows that AH^2 > FK^2, and therefore AH > FK.

**Step 13.** Since AH = HD [Step 7], we have AD = AH + HD = AH + AH. Since FK = KG [Step 7], we have FG = FK + KG = FK + FK. Since AH > FK [Step 12], adding equals to equals (AH > FK added to AH > FK), we obtain AH + AH > FK + FK [CN2], that is, AD > FG.

**Step 14.** Therefore, of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote. Q.E.F.

**USED:** 1.12, 1.20, 1.47, 3.3, CN1, CN2, D1.15, D1.17, D3.4, D3.5, P1
**Human refs (from References field):** 1.20, 1.24, 3.14, D3.5
**Jaccard:** 0.154 — AI adds ['1.12', '1.47', '3.3', 'CN1', 'CN2', 'D1.15', 'D1.17', 'D3.4', 'P1']; Human adds ['1.24', '3.14']

## Proposition 3.16
**Statement:** The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

**Step 1.** Let there be a circle with center F and diameter AB. From A, draw the straight line AE at right angles to AB [D1.10]. We must show three things: (i) AE falls outside the circle, (ii) no straight line can be interposed between AE and the circumference, and (iii) the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

**Step 2.** (Part i) Suppose AE does not fall outside the circle. Then it either falls on the circumference or inside it. Suppose AE, produced, meets the circumference at some point C. Join FC [P1].

**Step 3.** Since F is the center and A, C are on the circumference, FA = FC [D1.15]. Therefore triangle FAC is isosceles, and so angle FAC = angle FCA [1.5].

**Step 4.** But angle FAC is a right angle by construction [D1.10]. Therefore angle FCA is also a right angle. This means triangle FAC has two angles equal to two right angles.

**Step 5.** But in any triangle, the sum of any two angles is less than two right angles [1.17]. This is a contradiction. Therefore AE cannot meet the circumference at any point C, and so AE falls entirely outside the circle.

**Step 6.** (Part ii) We now show that no straight line can be interposed between the straight line AE and the circumference. Suppose, for the sake of contradiction, that some straight line AH can be drawn from A in the space between AE and the circumference without meeting the circumference.

**Step 7.** From F, draw FG perpendicular to AH [1.12], meeting AH at G. Then angle FGA is a right angle [D1.10].

**Step 8.** Since AH lies between AE and the circumference, angle FAH is less than angle FAE. But angle FAE is a right angle, so angle FAH is acute [D1.12].

**Step 9.** In triangle FAG, angle FGA is a right angle and angle FAG is acute. Since angle FGA is greater than angle FAG, the side opposite the greater angle is greater than the side opposite the lesser angle, so FA > FG [1.19].

**Step 10.** But FA is a radius of the circle [D1.15, D1.17]. Since FG < FA, the point G lies within the circle [3.7, noting that a point closer to the center than the radius lies inside the circle].

**Step 11.** But G is a point on line AH, and since it is inside the circle while A is on the circle, the line from A through G, when produced, must meet the circumference [3.2, since a chord joining two points on a circle falls within it, points inside the circle connect to the circumference]. More precisely, since AH passes from A on the circumference through G inside the circle, AH must cross the circumference again. This contradicts the assumption that AH does not meet the circumference. Therefore no straight line can be interposed between AE and the circumference.

**Step 12.** (Part iii — the angle of the semicircle) Consider the angle of the semicircle, which is the angle at A contained by the diameter BA and the arc of the semicircle [D3.7]. We claim this angle is greater than any acute rectilineal angle.

**Step 13.** Suppose there exists an acute rectilineal angle less than or equal to the angle of the semicircle. Let angle BAK be any acute rectilineal angle at A that is less than a right angle, with AK on the side of BA toward the semicircle. Since angle BAK is less than the right angle BAE [D1.12, P4], the line AK falls between AE and the diameter BA.

**Step 14.** By Part ii (Step 11), since AK lies between AE and the circumference, it must meet the circumference. Therefore AK falls within the angle of the semicircle, and angle BAK is less than the angle of the semicircle. Since this holds for every acute rectilineal angle, the angle of the semicircle is greater than any acute rectilineal angle.

**Step 15.** (Part iii — the remaining horn angle) Now consider the remaining angle, the angle at A between AE and the circumference on the side of the semicircle (the so-called horn angle or hornlike angle) [D3.7].

**Step 16.** We claim this horn angle is less than any acute rectilineal angle. Let angle EAK be any acute rectilineal angle at A with AK between AE and AB (on the side toward the circumference). Then angle BAK = angle BAE minus angle EAK. Since angle BAE is a right angle and angle EAK is acute, angle BAK is acute [D1.12].

**Step 17.** By Part ii, the line AK must meet the circumference, say at a point. Therefore AK passes between AE and the circumference, and the horn angle between AE and the circumference is less than angle EAK. Since angle EAK was an arbitrary acute rectilineal angle, the horn angle is less than any acute rectilineal angle.

**Step 18.** Therefore: (i) the straight line drawn at right angles to the diameter from its extremity falls outside the circle; (ii) between it and the circumference no straight line can be interposed; (iii) the angle of the semicircle is greater than any acute rectilineal angle, and the remaining horn angle is less than any acute rectilineal angle. Q.E.F.

**USED:** 1.12, 1.17, 1.19, 1.5, 3.2, 3.7, D1.10, D1.12, D1.15, D1.17, D3.7, P1, P4
**Human refs (from References field):** 1.17, 1.19, 1.5
**Jaccard:** 0.231 — AI adds ['1.12', '3.2', '3.7', 'D1.10', 'D1.12', 'D1.15', 'D1.17', 'D3.7', 'P1', 'P4']

## Proposition 3.17
**Statement:** From a given point to draw a straight line touching a given circle.

**Step 1.** Let A be the given point and let the given circle have circumference BCD. We consider two cases: either A lies on the circle, or A lies outside the circle.

**Step 2.** Case 1: Suppose A lies on the circumference of circle BCD. Find the centre E of circle BCD [3.1]. Join AE [P1].

**Step 3.** At point A on line AE, draw the straight line AF at right angles to AE [1.11].

**Step 4.** Since AE is a radius of the circle and AF is drawn at right angles to it at the extremity A on the circumference, by 3.16 the line AF falls outside the circle and touches circle BCD at A. Thus AF is the required tangent in this case.

**Step 5.** Case 2: Suppose A lies outside circle BCD. Find the centre E of the circle [3.1]. Join AE [P1], and let AE meet the circumference at D.

**Step 6.** Bisect AE at the point M [1.10]. With centre M and radius MA, describe circle ABF [P3]. Since A is outside the given circle, AE is greater than the radius ED, so the circle with centre M and radius MA (equal to half of AE) intersects the given circle. Let B be a point of intersection of circle ABF with circle BCD.

**Step 7.** Join AB and EB [P1].

**Step 8.** Since M is the midpoint of AE, we have MA = ME. And since B lies on circle ABF (centre M, radius MA), we have MB = MA. Therefore MA = MB = ME.

**Step 9.** In triangle MAB, since MA = MB, the angles opposite these equal sides are equal, so angle MAB = angle MBA [1.5].

**Step 10.** In triangle MEB, since ME = MB, the angles opposite these equal sides are equal, so angle MEB = angle MBE [1.5].

**Step 11.** Since A, M, E are collinear and B does not lie on line AE, angles AMB and EMB are supplementary, that is, angle AMB + angle EMB = two right angles [1.13].

**Step 12.** In triangle MAB, the sum of the interior angles equals two right angles [1.32], so angle MAB + angle MBA + angle AMB = two right angles, and since angle MAB = angle MBA (Step 9), we obtain 2 times angle MAB + angle AMB = two right angles.

**Step 13.** In triangle MEB, the sum of the interior angles equals two right angles [1.32], so angle MEB + angle MBE + angle EMB = two right angles, and since angle MEB = angle MBE (Step 10), we obtain 2 times angle MEB + angle EMB = two right angles.

**Step 14.** Adding the results of Steps 12 and 13: 2 times angle MAB + angle AMB + 2 times angle MEB + angle EMB = four right angles. By Step 11, angle AMB + angle EMB = two right angles, so substituting: 2 times angle MAB + 2 times angle MEB + two right angles = four right angles. Therefore 2 times angle MAB + 2 times angle MEB = two right angles, whence angle MAB + angle MEB = one right angle.

**Step 15.** In triangle ABE, the sum of the interior angles equals two right angles [1.32], so angle BAE + angle ABE + angle AEB = two right angles. Now angle BAE = angle MAB and angle AEB = angle MEB, so angle MAB + angle ABE + angle MEB = two right angles.

**Step 16.** By Step 14, angle MAB + angle MEB = one right angle. Substituting into Step 15: one right angle + angle ABE = two right angles. Therefore angle ABE = one right angle.

**Step 17.** Since angle ABE is a right angle, EB is perpendicular to AB at B. Since B lies on circle BCD and EB is a radius of circle BCD, the line AB is at right angles to the radius EB at the point B on the circumference. By 3.16, the line AB falls outside the circle and touches circle BCD at B [D3.2].

**Step 18.** Therefore in both cases, from the given point A a straight line has been drawn touching the given circle. Q.E.F.

**USED:** 1.10, 1.11, 1.13, 1.32, 1.5, 3.1, 3.16, D3.2, P1, P3
**Human refs (from References field):** 1.4, 3.1, 3.16
**Jaccard:** 0.182 — AI adds ['1.10', '1.11', '1.13', '1.32', '1.5', 'D3.2', 'P1', 'P3']; Human adds ['1.4']

## Proposition 3.18
**Statement:** If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.

**Step 1.** Let the straight line DE touch the circle ABC at the point C, and let F be the centre of the circle. Join FC. We must show that FC is perpendicular to DE. [D3.2, P1]

**Step 2.** Suppose, for the sake of contradiction, that FC is not perpendicular to DE. Then from F draw FG perpendicular to DE, meeting DE at some point G distinct from C. [1.12]

**Step 3.** Since angle FGC is a right angle (by construction), consider triangle FGC. By 1.17, the sum of any two angles in a triangle is less than two right angles. Since angle FGC is already a right angle, angle FCG must be less than a right angle, i.e., angle FCG is acute. [1.17]

**Step 4.** Since angle FGC (a right angle) is greater than angle FCG (an acute angle), the side opposite the greater angle is greater than the side opposite the lesser angle. Therefore FC, which subtends the right angle FGC, is greater than FG, which subtends the acute angle FCG. That is, FG < FC. [1.19]

**Step 5.** Now FC is a radius of the circle, since F is the centre and C is on the circumference. Since FG < FC, the distance from the centre F to the point G is less than the radius. Therefore G lies within the circle. [D1.15]

**Step 6.** But G lies on the line DE. Since G is within the circle and C is on the circle, the line DE passes through a point inside the circle. A straight line passing through a point inside a circle must meet the circumference in two points, and therefore cuts the circle. Hence DE cuts the circle. [3.2, 3.16]

**Step 7.** But DE is tangent to the circle at C, which means by definition it meets the circle and, being produced, does not cut the circle. This contradicts the conclusion of Step 6. [D3.2]

**Step 8.** Therefore the supposition is false, and FC is perpendicular to DE. That is, the straight line joined from the centre to the point of contact is perpendicular to the tangent. [D1.10]

Q.E.F.

**USED:** 1.12, 1.17, 1.19, 3.16, 3.2, D1.10, D1.15, D3.2, P1
**Human refs (from References field):** 1.17, 1.19
**Jaccard:** 0.222 — AI adds ['1.12', '3.16', '3.2', 'D1.10', 'D1.15', 'D3.2', 'P1']

## Proposition 3.19
**Statement:** If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so drawn.

**Step 1.** Let the straight line DE touch the circle ABC at the point C, and from C let CA be drawn at right angles to DE. I say that the centre of the circle is on CA.

**Step 2.** For suppose it is not, but, if possible, let the centre be at a point F not on CA. Join FC.

**Step 3.** Since DE touches the circle ABC at C, and FC has been joined from the centre F to the point of contact C, by Proposition 3.18 the line FC is perpendicular to DE. Therefore the angle FCD is a right angle.

**Step 4.** But the angle ACD is also a right angle, since CA was drawn at right angles to DE (by construction and Definition D1.10).

**Step 5.** Therefore angle FCD equals angle ACD, since all right angles are equal to one another (Postulate P4).

**Step 6.** But angle FCD is a part of angle ACD, since F is not on CA. Therefore a part equals the whole, which is impossible (Common Notion CN5: the whole is greater than the part).

**Step 7.** Therefore the centre of the circle is not at any point F off the line CA. Hence the centre lies on CA, which was to be proved.

**USED:** 3.18, CN5, D1.10, D3.2, P4
**Human refs (from References field):** 3.18
**Jaccard:** 0.200 — AI adds ['CN5', 'D1.10', 'D3.2', 'P4']

## Proposition 3.20
**Statement:** In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.

**Step 1.** Let ABC be a circle with center F [D1.15, D1.16]. Let angle BFC be an angle at the center and angle BAC be an angle at the circumference, where both angles stand on the same arc BC [D3.8, D3.9].

**Step 2.** Join AF and produce it to a point E on the circumference [P1, P2].

**Step 3.** [Case 1: F lies on AC.] Since FA and FB are both radii of circle ABC, FA equals FB [D1.15]. Therefore triangle FAB is isosceles, and by 1.5, angle FAB equals angle FBA.

**Step 4.** Since BFC is an exterior angle of triangle ABF, by 1.32 angle BFC equals the sum of angles FAB and FBA. Since angle FAB equals angle FBA, angle BFC equals twice angle FAB, that is, twice angle BAC. This concludes Case 1.

**Step 5.** [Case 2: F lies within angle BAC.] Since FE and FB are both radii, FE equals FB [D1.15]. Triangle BEF is isosceles, so by 1.5 angle FEB equals angle FBE.

**Step 6.** Since BFE is an exterior angle of triangle ABF, by 1.32 angle BFE equals the sum of angles FAB and FBA. But FA equals FB (both radii), so by 1.5 angle FAB equals angle FBA. Therefore angle BFE equals twice angle FAB, that is, twice angle BAE.

**Step 7.** Similarly, since FE and FC are both radii, FE equals FC [D1.15]. Triangle CEF is isosceles, so by 1.5 angle FEC equals angle FCE. Since CFE is an exterior angle of triangle ACF, by 1.32 angle CFE equals the sum of angles FAC and FCA. But FA equals FC (both radii), so by 1.5 angle FAC equals angle FCA. Therefore angle CFE equals twice angle FAC, that is, twice angle CAE.

**Step 8.** Adding, angle BFE plus angle CFE equals twice angle BAE plus twice angle CAE [CN2]. That is, the whole angle BFC equals twice the whole angle BAC. This concludes Case 2.

**Step 9.** [Case 3: F lies outside angle BAC, on the opposite side of AB from C.] As in Steps 5-6, since FA equals FB (both radii), by 1.5 angle FAB equals angle FBA. Then by 1.32 angle BFE equals twice angle BAE.

**Step 10.** Similarly, as in Step 7, since FA equals FC (both radii), by 1.5 angle FAC equals angle FCA. Then by 1.32 angle CFE equals twice angle CAE.

**Step 11.** Subtracting angle CFE from angle BFE: angle BFE minus angle CFE equals twice angle BAE minus twice angle CAE [CN3]. That is, the remaining angle BFC equals twice the remaining angle BAC. This concludes Case 3.

**Step 12.** Therefore, in all cases, the angle BFC at the center is double the angle BAC at the circumference, when both stand on the same arc BC. Q.E.D.

**USED:** 1.32, 1.5, CN2, CN3, D1.15, D1.16, D3.8, D3.9, P1, P2
**Human refs (from References field):** 1.32, 1.5
**Jaccard:** 0.200 — AI adds ['CN2', 'CN3', 'D1.15', 'D1.16', 'D3.8', 'D3.9', 'P1', 'P2']

## Proposition 3.21
**Statement:** In a circle the angles in the same segment are equal to one another.

**Step 1.** Let ABCD be a circle, and let angles BAC and BDC be angles in the same segment BADC, that is, let A and D be points on the same arc such that both angles subtend the chord BC from the same side. We must show that angle BAC equals angle BDC. [D1.15, D3.8]

**Step 2.** Find the center E of circle ABCD. [3.1]

**Step 3.** Join BE and CE. [P1]

**Step 4.** The angle BEC at the center and the angle BAC at the circumference have the same arc BC as base. Therefore, by Proposition 3.20, angle BEC is double angle BAC. [3.20]

**Step 5.** Likewise, the angle BEC at the center and the angle BDC at the circumference have the same arc BC as base. Therefore, by Proposition 3.20, angle BEC is double angle BDC. [3.20]

**Step 6.** Since angle BEC is double angle BAC, and angle BEC is double angle BDC, it follows that the double of angle BAC equals the double of angle BDC. Therefore angle BAC equals angle BDC. [CN1]

**Step 7.** Therefore, in a circle the angles in the same segment are equal to one another. Q.E.F.

**USED:** 3.1, 3.20, CN1, D1.15, D3.8, P1
**Human refs (from References field):** 3.20
**Jaccard:** 0.167 — AI adds ['3.1', 'CN1', 'D1.15', 'D3.8', 'P1']

## Proposition 3.22
**Statement:** The opposite angles of quadrilaterals in circles are equal to two right angles.

**Step 1.** Let ABCD be a quadrilateral inscribed in a circle, so that all four vertices A, B, C, D lie on the circumference [D4.3]. We are to show that the opposite angles, namely angle BAD + angle BCD, and angle ABC + angle ADC, each equal two right angles.

**Step 2.** Let O be the centre of the circle [3.1]. Join OB and OD [P1].

**Step 3.** The angle BAD is an angle at the circumference standing on the arc BCD (the arc from B to D that does not contain A). The angle BOD on the same side as A — that is, the angle BOD that faces arc BCD — is the angle at the centre standing on the same arc BCD. By Proposition 3.20, the angle BOD (reflex or non-reflex as appropriate) standing on arc BCD is double the angle BAD.

**Step 4.** Similarly, the angle BCD is an angle at the circumference standing on the arc BAD (the arc from B to D that contains A). The angle BOD on the same side as C — that is, the remaining angle BOD that faces arc BAD — is the angle at the centre standing on the same arc BAD. By Proposition 3.20, this angle BOD standing on arc BAD is double the angle BCD.

**Step 5.** Let the angle at the centre standing on arc BCD be called alpha, and the angle at the centre standing on arc BAD be called beta. Then alpha = 2 * angle BAD, and beta = 2 * angle BCD [Steps 3-4, by 3.20].

**Step 6.** Now alpha and beta together constitute the full angle around the centre O formed by the two rays OB and OD. Since OB and OD are two straight lines meeting at O, the angles on one side of line BD through O and the angles on the other side each sum to two right angles by Proposition 1.13. More precisely, the total of all angles around O formed by OB and OD equals four right angles: the angles on one side of the line through B, O, D (if it is a straight line) sum to two right angles, or if BOD is not a straight line, we apply 1.15 and 1.13 to see that the pair of angles alpha and beta (which together go all the way around O) sum to four right angles. Formally: draw the diameter from B through O; the angles on each side of this diameter sum to two right angles [1.13], giving four right angles total around O. The angles alpha and beta partition this full revolution, so alpha + beta = four right angles.

**Step 7.** Since alpha + beta = four right angles, and alpha = 2 * angle BAD and beta = 2 * angle BCD, we have 2 * angle BAD + 2 * angle BCD = four right angles. Halving both sides (which follows from CN1 and the properties of equal magnitudes), angle BAD + angle BCD = two right angles.

**Step 8.** By the same argument applied to the diagonal AC: join OA and OC [P1]. The angle ABC stands on arc ADC, and the angle at the centre AOC on arc ADC is double angle ABC [3.20]. The angle ADC stands on arc ABC, and the angle at the centre AOC on arc ABC is double angle ADC [3.20]. The two central angles around O (formed by OA and OC) again sum to four right angles [1.13]. Therefore 2 * angle ABC + 2 * angle ADC = four right angles, whence angle ABC + angle ADC = two right angles.

**Step 9.** Therefore the opposite angles of the quadrilateral ABCD inscribed in the circle are together equal to two right angles. Q.E.F.

**USED:** 1.13, 3.1, 3.20, CN1, D4.3, P1
**Human refs (from References field):** 1.32, 3.21
**Jaccard:** 0.000 — AI adds ['1.13', '3.1', '3.20', 'CN1', 'D4.3', 'P1']; Human adds ['1.32', '3.21']

## Proposition 3.23
**Statement:** On the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.

**Step 1.** Suppose, for the sake of contradiction, that on the same straight line AB, two similar and unequal segments of circles can be constructed on the same side. Let these be segments ACB and ADB, where segment ADB is the larger and contains segment ACB, with both arcs on the same side of AB. [D3.6, D3.11]

**Step 2.** Since segment ADB is larger and both share the base AB on the same side, the arc ADB lies further from AB than the arc ACB. Take a point D on the arc of segment ADB. Draw the straight line DA. [P1]

**Step 3.** Since the arc ACB lies between AB and the arc ADB, the straight line DA must cross the arc ACB at some point. Let this intersection point be C, so that C lies on the arc ACB and on the line segment AD, with A, C, D in that order. [3.2, since the chord from A toward D enters the region of the inner circle]

**Step 4.** Join DB and CB. [P1]

**Step 5.** Now consider triangle BCD with vertices B, C, D. The angle BCA is an exterior angle of triangle BCD at vertex C, since A, C, D are collinear and A is on the opposite side of C from D. By Proposition 1.16, the exterior angle of a triangle is greater than either of the non-adjacent interior angles. Therefore angle BCA is greater than angle BDC. [1.16]

**Step 6.** Since A, C, D are collinear (with C between A and D), angle BDC is the same as angle BDA, which is the angle in segment ADB (the angle at D subtended by base AB in segment ADB). [D3.8]

**Step 7.** Similarly, angle BCA is the angle in segment ACB (the angle at C subtended by base AB in segment ACB). [D3.8]

**Step 8.** Since segments ACB and ADB are similar, by Definition 3.11 they admit equal angles. Therefore the angle in segment ACB equals the angle in segment ADB; that is, angle BCA equals angle BDA. [D3.11]

**Step 9.** But from Step 5, angle BCA is greater than angle BDC, which equals angle BDA (Step 6). So angle BCA is greater than angle BDA. This contradicts Step 8, which asserts they are equal.

**Step 10.** Therefore the assumption is false, and on the same straight line there cannot be constructed two similar and unequal segments of circles on the same side. Q.E.D.

**USED:** 1.16, D3.11, D3.6, D3.8, P1
**Human refs (from References field):** 1.16, D3.11
**Jaccard:** 0.400 — AI adds ['D3.6', 'D3.8', 'P1']

## Proposition 3.24
**Statement:** Similar segments of circles on equal straight lines are equal to one another.

**Step 1.** Let AEB and CFD be similar segments of circles on equal straight lines AB and CD respectively. We must show that segment AEB is equal to segment CFD.

**Step 2.** Since AB is equal to CD, if the segment AEB is applied to the segment CFD so that the point A is placed on C and the straight line AB is placed on CD, then the point B will coincide with the point D, because AB is equal to CD [CN4].

**Step 3.** With AB coinciding with CD, suppose the segment AEB does not coincide with the segment CFD. Then it must fall otherwise, as segment CGD (say), so that on the same straight line CD there would be two segments of circles, CFD and CGD, on the same side, which are similar but unequal.

**Step 4.** But on the same straight line there cannot be constructed two similar and unequal segments of circles on the same side [3.23].

**Step 5.** Therefore the segment AEB, when applied to segment CFD, cannot fail to coincide with it. Hence segment AEB coincides with segment CFD and is therefore equal to it [CN4].

**Step 6.** Therefore similar segments of circles on equal straight lines are equal to one another. Q.E.D.

**USED:** 3.23, CN4, D3.11, D3.6
**Human refs (from References field):** 3.10
**Jaccard:** 0.000 — AI adds ['3.23', 'CN4', 'D3.11', 'D3.6']; Human adds ['3.10']

## Proposition 3.25
**Statement:** Given a segment of a circle, to describe the complete circle of which it is a segment.

**Step 1.** Let ABC be the given segment of a circle, with base AC and arc ABC, where B is any point on the arc. We are to describe the complete circle of which this segment is a part. [D3.6]

**Step 2.** Bisect AC at D. [1.10]

**Step 3.** From D, draw DB at right angles to AC, where B is on the arc of the segment, and produce DB in both directions as needed. [1.11]

**Step 4.** Join AB. [P1]

**Step 5.** Now consider the angles ABD and BAD. Exactly one of three cases holds: (i) angle ABD equals angle BAD, (ii) angle ABD is greater than angle BAD, or (iii) angle ABD is less than angle BAD.

**Step 6.** Case (i): Suppose angle ABD equals angle BAD. Then in triangle ABD, since the base angles are equal, the sides opposite them are equal, so BD = DA. [1.6] But DA = DC since D bisects AC. Therefore BD = DA = DC. Let E coincide with D. Then EA = EB = EC, and E is equidistant from A, B, and C.

**Step 7.** Case (ii): Suppose angle ABD is greater than angle BAD. At point A on the straight line AB, construct angle BAE equal to angle ABD, with E on the line BD between D and B. [1.23, P1] In triangle ABE, since angle BAE equals angle ABE, the sides opposite them are equal, so AE = BE. [1.6]

**Step 8.** Now in triangles ADE and CDE: AD = DC (since D bisects AC), DE is common, and angle ADE = angle CDE (both are right angles, since DB is perpendicular to AC). Therefore by the side-angle-side criterion, triangles ADE and CDE are congruent, and in particular AE = CE. [1.4]

**Step 9.** Thus in Case (ii), AE = BE = CE, so E is equidistant from A, B, and C.

**Step 10.** Case (iii): Suppose angle ABD is less than angle BAD. At point A on the straight line AB, construct angle BAE equal to angle ABD, with E on the line BD produced beyond D (on the opposite side of AC from B). [1.23, P1] In triangle ABE, since angle BAE equals angle ABE, the sides opposite them are equal, so AE = BE. [1.6]

**Step 11.** In triangles ADE and CDE: AD = DC (since D bisects AC), DE is common, and angle ADE = angle CDE (both are right angles, since the line through D perpendicular to AC makes right angles on both sides). Therefore by the side-angle-side criterion, triangles ADE and CDE are congruent, and AE = CE. [1.4]

**Step 12.** Thus in Case (iii), AE = BE = CE, so E is equidistant from A, B, and C.

**Step 13.** In all three cases, we have found a point E such that EA = EB = EC. With centre E and radius EA, describe a circle. [P3] Since EA = EB = EC, this circle passes through all three points A, B, and C. [D1.15]

**Step 14.** Now the given segment ABC is part of some circle; call it the original circle. The original circle passes through A and C (the endpoints of the base of the segment) and through B (a point on the arc). The newly constructed circle with centre E and radius EA also passes through A, B, and C.

**Step 15.** If the constructed circle were different from the original circle, then two distinct circles would have three common points A, B, and C. But a circle does not cut another circle at more than two points. [3.10] Since the two circles share three points, they cannot be distinct. Therefore the constructed circle is the same as the original circle.

**Step 16.** Therefore the circle with centre E and radius EA is the complete circle of which the given segment ABC is a segment. The complete circle has been described from the given segment, which is what was required to do.

**USED:** 1.10, 1.11, 1.23, 1.4, 1.6, 3.10, D1.15, D3.6, P1, P3
**Human refs (from References field):** 1.6, 3.9
**Jaccard:** 0.091 — AI adds ['1.10', '1.11', '1.23', '1.4', '3.10', 'D1.15', 'D3.6', 'P1', 'P3']; Human adds ['3.9']

## Proposition 3.26
**Statement:** In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

**Step 1.** Let ABC and DEF be equal circles, and let G and H be their centres respectively. First, suppose that the angles at the centres are equal: angle BGC = angle EHF. We must show that arc BC = arc EF.

**Step 2.** Since circles ABC and DEF are equal, their radii are equal by definition (D3.1). Therefore BG = EH and GC = HF.

**Step 3.** In triangles BGC and EHF, we have BG = EH, GC = HF (Step 2), and angle BGC = angle EHF (given). Therefore by the Side-Angle-Side criterion (1.4), triangle BGC is congruent to triangle EHF, and in particular BC = EF.

**Step 4.** Since the circles are equal, if circle ABC is applied to circle DEF so that centre G is placed on centre H, the circumferences coincide (D3.1). Since BG = EH (Step 2), place the radius GB along HE so that B falls on E. Since angle BGC = angle EHF (given) and GC = HF (Step 2), the radius GC falls along HF and the point C falls on F.

**Step 5.** Since B coincides with E and C coincides with F, and the circumferences of the two circles coincide, the arc BC coincides with the arc EF. Things which coincide with one another are equal (CN4). Therefore arc BC = arc EF.

**Step 6.** This completes the proof for the case of equal angles at the centres. Now suppose the angles at the circumferences are equal: angle BAC = angle EDF, where A is a point on the circumference of circle ABC and D is a point on the circumference of circle DEF.

**Step 7.** By Proposition 3.20, the angle at the centre is double the angle at the circumference when both stand on the same arc. Therefore angle BGC = 2 * angle BAC and angle EHF = 2 * angle EDF.

**Step 8.** Since angle BAC = angle EDF (given), their doubles are also equal: angle BGC = angle EHF (CN2, adding equals to equals, since angle BAC + angle BAC = angle EDF + angle EDF).

**Step 9.** But angle BGC and angle EHF are angles at the centres of equal circles, and they are equal (Step 8). Therefore by the case already proved (Steps 1-5), arc BC = arc EF.

**Step 10.** Therefore, in equal circles, equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences. Q.E.D.

**USED:** 1.4, 3.20, CN2, CN4, D3.1
**Human refs (from References field):** 1.4, 3.24, D3.11
**Jaccard:** 0.143 — AI adds ['3.20', 'CN2', 'CN4', 'D3.1']; Human adds ['3.24', 'D3.11']

## Proposition 3.27
**Statement:** In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.

**Step 1.** Let ABC and DEF be equal circles, and let arcs BC and EF be equal circumferences in them. Let G be the centre of circle ABC and H be the centre of circle DEF. Let angles BGC and EHF stand on arcs BC and EF at the centres, and let angles BAC and EDF stand on the same arcs at the circumferences. We must show that angle BGC equals angle EHF, and angle BAC equals angle EDF.

**Step 2.** First we prove the result for angles at the centres. Suppose angle BGC is not equal to angle EHF. Then one of them is greater. Without loss of generality, let angle BGC be greater than angle EHF.

**Step 3.** At the point G on the straight line BG, construct angle BGK equal to angle EHF, where K falls on the arc BC between B and C, using Proposition 1.23.

**Step 4.** Since circles ABC and DEF are equal, and angle BGK at the centre G equals angle EHF at the centre H, then by Proposition 3.26, arc BK equals arc EF.

**Step 5.** But arc BC equals arc EF by hypothesis. Therefore arc BK equals arc BC, by Common Notion 1.

**Step 6.** However, since angle BGK is less than angle BGC (as angle BGC is greater than angle EHF and angle BGK equals angle EHF), the ray GK falls between rays GB and GC. Hence arc BK is a proper part of arc BC.

**Step 7.** By Common Notion 5, the whole arc BC is greater than its part arc BK, so arc BK is not equal to arc BC. This contradicts Step 5.

**Step 8.** Therefore the assumption that angle BGC is not equal to angle EHF is false. Hence angle BGC equals angle EHF. This proves the result for angles at the centres.

**Step 9.** Now we prove the result for angles at the circumferences. By Proposition 3.20, since angle BAC is an angle at the circumference and angle BGC is the angle at the centre, both standing on the same arc BC, the central angle BGC is double the inscribed angle BAC.

**Step 10.** Similarly, by Proposition 3.20, the central angle EHF is double the inscribed angle EDF.

**Step 11.** Since angle BGC equals angle EHF (proved in Step 8), and angle BGC is double angle BAC, and angle EHF is double angle EDF, therefore double of angle BAC equals double of angle EDF. Hence angle BAC equals angle EDF, since halves of equals are equal.

**Step 12.** Therefore, in equal circles, angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences. Q.E.D.

**USED:** 1.23, 3.20, 3.26, CN1, CN5
**Human refs (from References field):** 1.23, 3.20, 3.26
**Jaccard:** 0.600 — AI adds ['CN1', 'CN5']

## Proposition 3.28
**Statement:** In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

**Step 1.** Let ABC and DEF be equal circles, and let BC and EF be equal straight lines in them cutting off the circumferences BAC, BGC in circle ABC and EDF, EHF in circle DEF, where BGC and EHF are the minor arcs and BAC and EDF are the major arcs. We must show that the major circumference BAC equals the major circumference EDF, and the minor circumference BGC equals the minor circumference EHF.

**Step 2.** Find the centre K of circle ABC and the centre L of circle DEF [3.1]. Join BK, KC, EL, and LF [P1].

**Step 3.** Since circles ABC and DEF are equal, their radii are equal [D3.1]. Therefore BK equals EL, and KC equals LF.

**Step 4.** Since BC equals EF (given), BK equals EL, and KC equals LF (Step 3), the two triangles BKC and ELF have three sides respectively equal. Therefore angle BKC equals angle ELF [1.8].

**Step 5.** Since angle BKC and angle ELF are equal central angles in equal circles, the circumferences on which they stand are equal [3.26]. That is, the minor circumference BGC equals the minor circumference EHF.

**Step 6.** Since circles ABC and DEF are equal, the whole circumference of circle ABC equals the whole circumference of circle DEF. Since the minor circumference BGC equals the minor circumference EHF (Step 5), subtracting equals from equals, the remaining major circumference BAC equals the remaining major circumference EDF [CN3].

**Step 7.** Therefore in equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less. Q.E.D.

**USED:** 1.8, 3.1, 3.26, CN3, D3.1, P1
**Human refs (from References field):** 1.8, 3.26
**Jaccard:** 0.333 — AI adds ['3.1', 'CN3', 'D3.1', 'P1']

## Proposition 3.29
**Statement:** In equal circles equal circumferences are subtended by equal straight lines.

**Step 1.** Let ABC and DEF be equal circles, and let the circumference BGC in circle ABC be equal to the circumference EHF in circle DEF. Let BC be the straight line subtending arc BGC and let EF be the straight line subtending arc EHF. I say that BC equals EF.

**Step 2.** Find the centre K of circle ABC and the centre L of circle DEF. [3.1]

**Step 3.** Join KB, KC, LE, and LF. [P1]

**Step 4.** Since the circumference BGC is equal to the circumference EHF, and these circumferences lie in equal circles, the angle BKC at the centre of circle ABC is equal to the angle ELF at the centre of circle DEF. [3.27]

**Step 5.** Since circles ABC and DEF are equal, their radii are equal. [D3.1] Therefore KB equals LE, and KC equals LF.

**Step 6.** In triangles BKC and ELF, KB equals LE, KC equals LF, and angle BKC equals angle ELF. Therefore, by the side-angle-side congruence criterion, triangle BKC is equal to triangle ELF, and the base BC equals the base EF. [1.4]

**Step 7.** Therefore in equal circles equal circumferences are subtended by equal straight lines. Q.E.D.

**USED:** 1.4, 3.1, 3.27, D3.1, P1
**Human refs (from References field):** 1.4, 3.27
**Jaccard:** 0.400 — AI adds ['3.1', 'D3.1', 'P1']

## Proposition 3.30
**Statement:** To bisect a given circumference.

**Step 1.** Let ADB be the given circumference (arc) of a circle, and let A and B be its endpoints. It is required to bisect the arc ADB.

**Step 2.** Join AB [P1].

**Step 3.** Bisect AB at C [1.10], so that AC equals CB.

**Step 4.** From C, draw CD at right angles to AB [1.11], and let D be the point where CD meets the arc ADB.

**Step 5.** Join AD and DB [P1].

**Step 6.** In triangles ACD and BCD: AC equals CB (by construction in Step 3); CD is common to both triangles; and angle ACD equals angle BCD, since each is a right angle (by construction in Step 4) [D1.10].

**Step 7.** Therefore triangle ACD is congruent to triangle BCD, and in particular AD equals DB [1.4].

**Step 8.** Now AD and DB are equal straight lines in the same circle. A circle is equal to itself, since its diameter (or radius) equals itself [D3.1].

**Step 9.** Therefore, since in equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less, the arc AD (which is part of arc ADB) equals the arc DB (which is the remaining part of arc ADB) [3.28].

**Step 10.** Therefore the given circumference ADB has been bisected at D. Q.E.F.

**USED:** 1.10, 1.11, 1.4, 3.28, D1.10, D3.1, P1
**Human refs (from References field):** 1.4, 3.28
**Jaccard:** 0.286 — AI adds ['1.10', '1.11', 'D1.10', 'D3.1', 'P1']

## Proposition 3.31
**Statement:** In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

**Step 1.** Let ABCD be a circle with diameter BC, and let E be its centre. Take any point A on the semicircle BAC and join BA and AC. We shall first show that angle BAC is a right angle.

**Step 2.** Join AE. Since EB equals EA (radii of the circle, by D1.15), triangle ABE is isosceles. Therefore angle EAB equals angle EBA (by 1.5).

**Step 3.** Since EA equals EC (radii of the circle, by D1.15), triangle AEC is isosceles. Therefore angle EAC equals angle ECA (by 1.5).

**Step 4.** Now angle BAC equals the sum of angles EAB and EAC. In triangle ABC, the sum of angles ABC, BCA, and BAC equals two right angles (by 1.32).

**Step 5.** That is, angle EBA + angle ECA + angle EAB + angle EAC = two right angles. Since angle EAB = angle EBA and angle EAC = angle ECA (from Steps 2 and 3), we have angle EAB + angle EAC + angle EAB + angle EAC = two right angles, i.e., 2*(angle EAB + angle EAC) = two right angles.

**Step 6.** Therefore angle EAB + angle EAC = one right angle. But angle EAB + angle EAC equals angle BAC. Hence angle BAC is a right angle (by D1.10).

**Step 7.** This holds for any point A on the semicircle, so the angle in a semicircle is right.

**Step 8.** Now for the angle in a greater segment. Let ABC be a greater segment of the circle with base AC, and let D be a point on the circumference of the greater segment. The angle ADC is an angle in the greater segment. Draw the diameter from A through the centre, meeting the circle at some point, and consider the semicircle. Since ABC is a greater segment, the arc ABC is greater than a semicircle, so the arc ADC (the remaining arc from A to C not through B) is less than a semicircle.

**Step 9.** Instead, proceed directly: let ABCD be a circle with diameter BC and centre E. Let F be any point on the arc BAC (the semicircle). Take a point A on the arc BC that is on the same side as F, forming a greater segment. Join AB and AC. Since angle BAC is in the semicircle, angle BAC is right (Step 7). Now consider angle ABC in triangle ABC: since angle BAC is right, angles ABC and ACB together equal one right angle (by 1.32, the three angles sum to two right angles, and angle BAC is one right angle, so the remaining two sum to one right angle). Therefore angle ABC is less than a right angle, i.e., it is acute.

**Step 10.** But observe that angle ABC is an angle in the segment ABC. The segment on BC containing A is a greater segment (since BC is a diameter, the segment on one side is a semicircle; for a chord not through the centre, the segment containing the centre is the greater segment). More precisely: let the circle ABCD have any chord AC (not a diameter). This chord divides the circle into two segments. Let B be a point in the greater segment. Consider the quadrilateral ABCD inscribed in the circle where D is in the lesser segment.

**Step 11.** By 3.22, the opposite angles of a cyclic quadrilateral sum to two right angles. So angle ABC + angle ADC = two right angles.

**Step 12.** Now, since AC is not a diameter and B lies in the greater segment, the arc ADC (on which angle ABC stands at the circumference, by D3.9) is the minor arc, and the arc ABC is the major arc. The angle at the centre standing on arc ADC is less than two right angles (since arc ADC is less than a semicircle). By 3.20, the angle at the centre is double the angle at the circumference, so angle ABC, which stands on arc ADC, satisfies: the central angle on arc ADC is double angle ABC.

**Step 13.** Since the arc of the greater segment (arc ABC containing B) is greater than a semicircle, the arc ADC (on which angle ABC stands from the circumference) is less than a semicircle. The central angle subtended by arc ADC is less than two right angles. By 3.20, the central angle equals twice angle ABC. Since the greater segment's arc is greater than a semicircle, the central angle on the minor arc ADC is less than two right angles, meaning angle ABC is less than a right angle.

**Step 14.** Alternatively and more directly: take the circle with chord AC (not a diameter), B in the greater segment, and let M be the midpoint of arc AC (greater arc) so that AM is a diameter. Join BM. Then angle ABM is in a semicircle with diameter AM, but this introduces extra construction. We use the cleaner approach via 3.22 and the semicircle result.

**Step 15.** Clean argument for the greater segment: Let AC be a chord of circle ABCD, B a point on the major arc (greater segment), and D a point on the minor arc (lesser segment). Draw diameter AE through the centre. Join EC, EB, and BC. Angle AEC is in the semicircle on diameter AE... 

**Step 16.** Let us use the most direct approach. In circle ABCD, let AC be a chord (not a diameter). Let B be on the major arc and D on the minor arc. The angle in the greater segment is angle ABC (D3.8). The angle in the lesser segment is angle ADC (D3.8). By 3.22, angle ABC + angle ADC = two right angles.

**Step 17.** Now draw a diameter through A, say AF, where F is the diametrically opposite point. F lies on the minor arc (the arc AC not containing B), since the major arc contains B and is more than a semicircle. Join BF and CF. The angle BCF is in the semicircle on diameter BF... this overcomplicates. Instead:

**Step 18.** Direct proof using 3.20 and the semicircle result: The angle in the greater segment is angle ABC where B is on the major arc. The inscribed angle ABC subtends the minor arc ADC (by D3.9). Let O be the centre. The central angle AOC on the minor arc is less than two right angles (since the minor arc is less than a semicircle, the central angle facing it is less than a straight angle). By 3.20, central angle AOC = 2 * angle ABC. Since the minor arc is less than a semicircle, central angle AOC < two right angles, so angle ABC < one right angle. Thus the angle in the greater segment is acute (D1.12).

**Step 19.** The angle in the lesser segment is angle ADC where D is on the minor arc. By 3.22, angle ABC + angle ADC = two right angles. Since angle ABC < one right angle (Step 18), angle ADC > one right angle (by CN5 and the fact that if one part is less, the other must be greater to maintain the sum). Thus the angle in the lesser segment is obtuse (D1.11).

**Step 20.** For the angle of the greater segment: by D3.7, the angle of a segment is the angle between the chord and the arc. The angle of the greater segment is contained by the straight line AC and the major arc. Since the angle in the semicircle (angle BAC with B on the semicircular arc of diameter AC) is right, and the greater segment's arc is larger than a semicircle, the angle of the greater segment (between chord AC and the major arc) is greater than the angle of the semicircle (between the diameter and the semicircular arc). By 3.16, the angle of the semicircle (between the diameter and the circumference) is greater than any acute rectilineal angle. Therefore the angle of the greater segment, being a mixed angle between a chord and an arc that is greater than a semicircular arc, is greater than a right angle.

**Step 21.** More precisely for the angle of the greater segment: consider the angle of the greater segment at endpoint A of chord AC, formed between AC and the major arc ABC. Draw the diameter AD through the centre from A. Then AD passes through the interior of the greater segment (since the greater segment contains the centre). The angle DAC is an angle in the semicircle on the other side, and by the semicircle result (Step 7) the angle in that semicircle is right. The angle of the semicircle at A (between diameter AD and the arc) is itself greater than any acute rectilineal angle by 3.16. Now the angle of the greater segment at A (between chord AC and the major arc) contains both the rectilineal angle DAC and the angle of the semicircle between AD and the arc on the side of the greater segment. Since angle DAC is part of the angle of the greater segment, and angle DAC equals a right angle (being the angle in a semicircle from Step 7 applied to the semicircle on one side of AD), the angle of the greater segment is greater than a right angle.

**Step 22.** For the angle of the less segment: the angle of the lesser segment at A is between chord AC and the minor arc. This is contained within the angle of the semicircle at A on that side (between diameter AD and the arc). By 3.16, the angle of the semicircle is less than any right rectilineal angle. Therefore the angle of the lesser segment, being less than the angle of the semicircle (which is itself less than a right angle), is less than a right angle.

**Step 23.** Therefore: (1) the angle in the semicircle is right, (2) the angle in a greater segment is less than a right angle, (3) the angle in a less segment is greater than a right angle, (4) the angle of the greater segment is greater than a right angle, and (5) the angle of the less segment is less than a right angle. Q.E.D.

**USED:** 1.32, 1.5, 3.16, 3.20, 3.22, D1.10, D1.11, D1.12, D1.15, D1.17, D1.18, D3.7, D3.8, D3.9, P1
**Human refs (from References field):** 1.17, 1.32, 1.5, 3.22, D1.10
**Jaccard:** 0.250 — AI adds ['3.16', '3.20', 'D1.11', 'D1.12', 'D1.15', 'D1.17', 'D1.18', 'D3.7', 'D3.8', 'D3.9', 'P1']; Human adds ['1.17']

## Proposition 3.32
**Statement:** If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

**Step 1.** Let the straight line EF touch the circle ABCD at the point B, and from B let the straight line BD be drawn across the circle, cutting it. The chord BD divides the circle into two segments. We must show that angle DBF equals the angle in the alternate segment BAD, and that angle DBE equals the angle in the alternate segment BCD.

**Step 2.** Draw BA as a diameter of the circle [D1.17], and join AD and DC [P1].

**Step 3.** Since EF is a tangent to the circle at B [D3.2], and BA is a straight line drawn from the centre to the point of contact, angle ABF is a right angle [3.18].

**Step 4.** Since BA is a diameter of the circle, the angle ADB is an angle in a semicircle, and therefore angle ADB is a right angle [3.31].

**Step 5.** In triangle ABD, the three interior angles sum to two right angles [1.32]. Since angle ADB is a right angle, the remaining two angles satisfy angle ABD + angle DAB = one right angle.

**Step 6.** Since angle ABF is a right angle, and angle ABF = angle ABD + angle DBF, we have angle DBF = angle ABF - angle ABD = one right angle minus angle ABD.

**Step 7.** From Step 5, angle DAB = one right angle minus angle ABD. Therefore angle DBF = angle DAB.

**Step 8.** Now angle DAB is an angle in the segment BAD [D3.8], which is the alternate segment with respect to the angle DBF. Moreover, any other angle inscribed in segment BAD stands on the same arc BD and is therefore equal to angle DAB [3.21]. Hence angle DBF equals the angle in the alternate segment.

**Step 9.** Since B lies on the straight line EF, angles DBF and DBE are supplementary, that is, angle DBE + angle DBF = two right angles [1.13].

**Step 10.** The quadrilateral ABCD is inscribed in the circle, so its opposite angles satisfy angle BAD + angle BCD = two right angles [3.22].

**Step 11.** From Step 7, angle DBF = angle BAD. Substituting into the equation from Step 9: angle DBE = two right angles minus angle BAD. From Step 10: angle BCD = two right angles minus angle BAD. Therefore angle DBE = angle BCD.

**Step 12.** Now angle BCD is an angle in the segment BCD [D3.8], which is the alternate segment with respect to the angle DBE. Any other angle inscribed in segment BCD is equal to angle BCD [3.21]. Hence angle DBE equals the angle in the alternate segment.

**Step 13.** Therefore, if a straight line touches a circle, and from the point of contact a straight line is drawn across the circle cutting it, the angles which it makes with the tangent are equal to the angles in the alternate segments of the circle. Q.E.F.

**USED:** 1.13, 1.32, 3.18, 3.21, 3.22, 3.31, D1.17, D3.2, D3.8, P1
**Human refs (from References field):** 1.32, 3.19, 3.22, 3.31
**Jaccard:** 0.273 — AI adds ['1.13', '3.18', '3.21', 'D1.17', 'D3.2', 'D3.8', 'P1']; Human adds ['3.19']

## Proposition 3.33
**Statement:** On a given straight line to describe a segment of a circle admitting an angle equal to a given rectilineal angle.

**Step 1.** Let AB be the given straight line and C the given rectilineal angle. We wish to describe on AB a segment of a circle admitting an angle equal to angle C. There are three cases according as angle C is right, acute, or obtuse.

**Step 2.** Case 1: Suppose angle C is a right angle. Bisect AB at F [1.10]. With center F and radius FA, describe the semicircle AHB [P3, D1.15]. Then AB is a diameter of the circle [D1.17], and AHB is a semicircle [D1.18]. By 3.31, the angle in a semicircle is right. Therefore the segment AHB admits an angle equal to the right angle C, and the construction is done for this case.

**Step 3.** Case 2: Suppose angle C is acute. At the point A on the line AB, construct angle BAD equal to angle C [1.23]. From A, draw AE at right angles to AD [1.11]. Bisect AB at F [1.10]. From F, draw FG at right angles to AB [1.11]. Join GB [P1].

**Step 4.** Since AF equals FB (by bisection), and FG is common, and angle AFG equals angle BFG (each being a right angle), by 1.4 triangle AFG is congruent to triangle BFG. Therefore GA equals GB.

**Step 5.** Since GA equals GB, the circle described with center G and radius GA also passes through B [D1.15, P3]. Let this circle be AHB. Since AB is a chord of the circle and G is the center, consider the diameter of the circle through A and G. The line AD is perpendicular to GA at A, because GA lies along AE (since G lies on the line AE erected perpendicular to AD at A), and angle GAD is therefore a right angle.

**Step 6.** Since GA is a radius and the straight line AD is drawn at right angles to the diameter through A at the endpoint A, by 3.16 the line AD falls outside the circle and therefore touches the circle at A.

**Step 7.** Since the straight line AD touches the circle at A, and AB is drawn from the point of contact A across the circle, by 3.32 the angle DAB equals the angle in the alternate segment AHB [D3.6, D3.8]. But angle DAB was constructed equal to angle C. Therefore the angle in the segment AHB equals angle C. Thus the segment AHB on the given straight line AB admits an angle equal to the given angle C.

**Step 8.** Case 3: Suppose angle C is obtuse. At the point A on the line AB, construct angle BAD equal to angle C [1.23]. From A, draw AE at right angles to AD [1.11]. Bisect AB at F [1.10]. From F, draw FG at right angles to AB [1.11]. Join GB [P1].

**Step 9.** Since AF equals FB, FG is common, and angle AFG equals angle BFG (each being right), by 1.4 triangle AFG is congruent to triangle BFG. Therefore GA equals GB.

**Step 10.** The circle described with center G and radius GA passes through B [D1.15, P3]. Let this circle be AHB. As in Case 2, G lies on the line AE (perpendicular to AD at A), so GA is perpendicular to AD at A. Since GA is a radius and AD is at right angles to the diameter through A at the endpoint A, by 3.16 the line AD touches the circle at A.

**Step 11.** Since AD touches the circle at A and AB is drawn from the point of contact across the circle, by 3.32 the angle DAB equals the angle in the alternate segment AHB. But angle DAB was constructed equal to angle C. Therefore the angle in the segment AHB equals the obtuse angle C. Thus the segment AHB on the given straight line AB admits an angle equal to the given angle C.

**Step 12.** Therefore in all three cases, on the given straight line AB a segment of a circle AHB has been described admitting an angle equal to the given rectilineal angle C. Q.E.F.

**USED:** 1.10, 1.11, 1.23, 1.4, 3.16, 3.31, 3.32, D1.15, D1.17, D1.18, D3.6, D3.8, P1, P3
**Human refs (from References field):** 1.4, 3.16, 3.31, 3.32
**Jaccard:** 0.286 — AI adds ['1.10', '1.11', '1.23', 'D1.15', 'D1.17', 'D1.18', 'D3.6', 'D3.8', 'P1', 'P3']

## Proposition 3.34
**Statement:** From a given circle to cut off a segment admitting an angle equal to a given rectilineal angle.

**Step 1.** Let ABC be the given circle, and let D be the given rectilineal angle. We are required to cut off from circle ABC a segment admitting an angle equal to angle D.

**Step 2.** Take any point B on the circumference of circle ABC. Find the centre of circle ABC [3.1], and draw the straight line from the centre to B [P1]. At the point B, erect a straight line EBF at right angles to the radius at B [1.11]. By 3.16, the straight line drawn at right angles to the diameter at its extremity touches the circle and does not cut it, so EBF is tangent to circle ABC at B.

**Step 3.** At the point B on the straight line BF, construct angle FBC equal to the given angle D, where the ray BC meets the circumference of the circle at C [1.23]. Since EBF is tangent to the circle at B, by 3.16 every other straight line through B besides the tangent falls within the circle; therefore BC cuts the circle and meets the circumference again at a point C distinct from B.

**Step 4.** The chord BC divides circle ABC into two segments. Consider the segment BAC on the side of BC opposite to the tangent direction BF. By 3.32, since the straight line EBF touches circle ABC at B, and from the point of contact B the straight line BC has been drawn across the circle cutting it, the angle FBC which BC makes with the tangent BF is equal to the angle in the alternate segment BAC.

**Step 5.** But angle FBC was constructed equal to angle D [Step 3]. Therefore the angle in segment BAC is equal to angle D.

**Step 6.** Therefore from the given circle ABC, the segment BAC has been cut off admitting an angle equal to the given rectilineal angle D. Q.E.F.

**USED:** 1.11, 1.23, 3.1, 3.16, 3.32, P1
**Human refs (from References field):** 1.23, 3.32
**Jaccard:** 0.333 — AI adds ['1.11', '3.1', '3.16', 'P1']

## Proposition 3.35
**Statement:** If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.

**Step 1.** Let ABCD be a circle, and let two straight lines AC and BD cut one another at the point E within the circle. I say that the rectangle AE by EC equals the rectangle DE by EB.

**Step 2.** Case 1: Suppose AC and BD each pass through the centre F of the circle. Then E is the centre F, so AE = EC and DE = EB, since each is a radius [D1.15]. Therefore the rectangle AE by EC equals the rectangle DE by EB, since AE = DE and EC = EB (all being radii).

**Step 3.** Case 2: Suppose AC passes through the centre F and BD does not pass through the centre. Draw the centre F [3.1]. Since AC passes through F, F lies on AC. Draw FG perpendicular from F to BD [1.12]. Then FG bisects BD, so DG = GB [3.3].

**Step 4.** Since the straight line AC is cut into equal parts at F and into unequal parts at E, the rectangle AE by EC together with the square on EF equals the square on FC [2.5].

**Step 5.** But FC is a radius, so FC = FB [D1.15]. Therefore the rectangle AE by EC plus the square on EF equals the square on FB.

**Step 6.** Now in the right-angled triangle FGE (right angle at G), the square on FE equals the square on FG plus the square on GE [1.47]. So the rectangle AE by EC plus the square on FG plus the square on GE equals the square on FB.

**Step 7.** In the right-angled triangle FGB (right angle at G), the square on FB equals the square on FG plus the square on GB [1.47]. So the rectangle AE by EC plus the square on FG plus the square on GE equals the square on FG plus the square on GB.

**Step 8.** Subtracting the square on FG from both sides, the rectangle AE by EC plus the square on GE equals the square on GB [CN3].

**Step 9.** Since the straight line BD is cut into equal parts at G and into unequal parts at E, the rectangle DE by EB plus the square on GE equals the square on GB [2.5].

**Step 10.** Therefore the rectangle AE by EC plus the square on GE equals the rectangle DE by EB plus the square on GE [CN1].

**Step 11.** Subtracting the square on GE from both sides, the rectangle AE by EC equals the rectangle DE by EB [CN3].

**Step 12.** Case 3: Suppose neither AC nor BD passes through the centre. Draw the centre F [3.1]. Draw the diameter FGEH through F and E [P1, P2]. (Here G is the intersection of the diameter with BD and H is arbitrary on the circle; the diameter passes through E since E is a point through which we draw the line from F.)

**Step 13.** Since FGEH is a diameter passing through the centre F and cutting chord AC at E, and also cutting chord BD, we apply the result of Case 2. Treating the diameter FH as the chord through the centre and AC as the chord not through the centre, the rectangle AE by EC equals the rectangle FE by EH (by Case 2 applied to chords FH and AC intersecting at E).

**Step 14.** Similarly, treating the diameter FH as the chord through the centre and BD as the chord not through the centre, the rectangle DE by EB equals the rectangle FE by EH (by Case 2 applied to chords FH and BD intersecting at E).

**Step 15.** Therefore the rectangle AE by EC equals the rectangle DE by EB, since both equal the rectangle FE by EH [CN1].

**Step 16.** Therefore, if in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other. Q.E.D.

**USED:** 1.12, 1.47, 2.5, 3.1, 3.3, CN1, CN3, D1.15, P1, P2
**Human refs (from References field):** 1.47, 2.5, 3.3
**Jaccard:** 0.300 — AI adds ['1.12', '3.1', 'CN1', 'CN3', 'D1.15', 'P1', 'P2']

## Proposition 3.36
**Statement:** If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the circle and the other touch it, the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference will be equal to the square on the tangent.

**Step 1.** Let the circle have center F, let D be a point outside it, let DCA be a straight line from D cutting the circle at C (on the convex circumference, nearer to D) and at A (on the far side), and let DB be a tangent to the circle touching it at B. We must show that the rectangle contained by DA and DC equals the square on DB.

**Step 2.** Join FB, FC, and FD [P1].

**Step 3.** Since DB touches the circle at B, and FB is joined from the center F to the point of contact B, angle FBD is a right angle [3.18].

**Step 4.** Case 1: Suppose the secant DCA passes through the center F, so that CA is a diameter. Then F is the midpoint of CA, meaning CF = FA [D1.15, D1.17]. The points lie in order D, C, F, A along the line.

**Step 5.** Since CA is bisected at F and extended to D, by Proposition 2.6: the rectangle DA times DC plus the square on CF equals the square on DF. That is, rect(DA, DC) + CF² = DF² [2.6].

**Step 6.** In right triangle DFB (right angle at B from Step 3), by the Pythagorean theorem: DF² = DB² + BF² [1.47].

**Step 7.** Since BF and CF are both radii of the circle, BF = CF [D1.15].

**Step 8.** From Steps 5 and 6: rect(DA, DC) + CF² = DB² + BF². Since CF = BF, subtracting CF² from both sides yields rect(DA, DC) = DB² [CN3].

**Step 9.** Case 2: Suppose the secant DCA does not pass through the center F. Draw FG perpendicular from F to chord CA, meeting CA at G [1.12].

**Step 10.** Since FG is drawn from the center perpendicular to chord CA, it bisects CA, so CG = GA [3.3].

**Step 11.** Since CA is bisected at G and extended to D, by Proposition 2.6: rect(DA, DC) + GC² = GD² [2.6].

**Step 12.** Add FG² to both sides: rect(DA, DC) + GC² + FG² = GD² + FG² [CN2].

**Step 13.** In right triangle FGC (right angle at G), by the Pythagorean theorem: FC² = FG² + GC² [1.47].

**Step 14.** In right triangle FGD (right angle at G), by the Pythagorean theorem: FD² = FG² + GD² [1.47].

**Step 15.** Substituting Steps 13 and 14 into Step 12: rect(DA, DC) + FC² = FD² [CN1].

**Step 16.** In right triangle FBD (right angle at B from Step 3), by the Pythagorean theorem: FD² = FB² + BD² [1.47].

**Step 17.** From Steps 15 and 16: rect(DA, DC) + FC² = FB² + BD² [CN1].

**Step 18.** Since FB and FC are both radii of the circle, FB = FC [D1.15], so FB² = FC².

**Step 19.** Subtracting FC² from both sides of Step 17: rect(DA, DC) = BD² [CN3].

**Step 20.** Therefore in both cases, the rectangle contained by the whole secant DA and the external segment DC equals the square on the tangent DB, which was to be proved.

**USED:** 1.12, 1.47, 2.6, 3.18, 3.3, CN1, CN2, CN3, D1.15, D1.17, P1
**Human refs (from References field):** 1.47, 2.6, 3.18, 3.3
**Jaccard:** 0.364 — AI adds ['1.12', 'CN1', 'CN2', 'CN3', 'D1.15', 'D1.17', 'P1']

## Proposition 3.37
**Statement:** If a point be taken outside a circle and from the point there fall on the circle two straight lines, if one of them cut the circle, and the other fall on it, and if further the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference be equal to the square on the straight line which falls on the circle, the straight line which falls on it will touch the circle.

**Step 1.** Let D be a point outside circle ABC, let DCA be a straight line cutting the circle at C and A (with C on the convex circumference nearer to D), and let DB fall on the circle at B. Suppose that the rectangle contained by DA and DC is equal to the square on DB. We must show that DB touches the circle.

**Step 2.** From D, draw the tangent DE to the circle (3.17). Let E be the point of tangency.

**Step 3.** Since DE touches the circle and DCA cuts it, by Proposition 3.36 the rectangle contained by DA and DC equals the square on DE. That is, rect(DA, DC) = DE^2.

**Step 4.** But by hypothesis, rect(DA, DC) = DB^2. Therefore DE^2 = DB^2 (CN1), and hence DE = DB.

**Step 5.** Find the center F of the circle (3.1). Join FB, FE, and FD (P1).

**Step 6.** Since F is the center and B and E are on the circle, FB = FE (D1.15).

**Step 7.** FD is common to triangles FBD and FED.

**Step 8.** We have FB = FE (Step 6), DB = DE (Step 4), and FD = FD (Step 7). Therefore triangle FBD is congruent to triangle FED, and angle FBD = angle FED (1.8).

**Step 9.** Since DE touches the circle at E, and FE is joined from the center F to the point of contact E, angle FED is a right angle (3.18).

**Step 10.** Therefore angle FBD is also a right angle (Step 8, Step 9).

**Step 11.** Since FB is a radius of the circle to the point B on the circumference, and DB makes a right angle with FB at B, the line DB touches the circle at B (3.16).

**Step 12.** Therefore, if a point be taken outside a circle and from the point there fall on the circle two straight lines, one cutting the circle and the other falling on it, and if the rectangle contained by the whole of the cutting line and the part intercepted outside between the point and the convex circumference equals the square on the line which falls on the circle, then that line touches the circle. Q.E.D.

**USED:** 1.8, 3.1, 3.16, 3.17, 3.18, 3.36, CN1, D1.15, P1
**Human refs (from References field):** 1.8, 3.16, 3.18, 3.36
**Jaccard:** 0.444 — AI adds ['3.1', '3.17', 'CN1', 'D1.15', 'P1']
