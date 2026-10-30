# Book 1 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 1.1
**Statement:** On a given finite straight line to construct an equilateral triangle.

**Step 1.** Let AB be the given finite straight line. It is required to construct an equilateral triangle on AB.

**Step 2.** With centre A and distance AB, let the circle BCD be described. [P3]

**Step 3.** With centre B and distance BA, let the circle ACE be described. [P3]

**Step 4.** From the point C, in which the circles cut one another, draw the straight lines CA and CB to the points A and B respectively. [P1]

**Step 5.** Now, since the point A is the centre of circle BCD, the segment AC is equal to AB. [D1.15]

**Step 6.** Since the point B is the centre of circle ACE, the segment BC is equal to BA. [D1.15]

**Step 7.** But CA was shown equal to AB in Step 5. Therefore each of the straight lines CA and CB is equal to AB. [Steps 5 and 6]

**Step 8.** Things which are equal to the same thing are also equal to one another. Since CA equals AB and CB equals AB, it follows that CA equals CB. [CN1]

**Step 9.** Therefore the three straight lines CA, AB, and BC are equal to one another, and the triangle ABC is equilateral. [D1.20]

**Step 10.** Thus, on the given finite straight line AB, an equilateral triangle ABC has been constructed, which is what was required.

**USED:** CN1, D1.15, D1.20, P1, P3
**Human refs (from References field):** CN1, D1.15, P1, P3
**Jaccard:** 0.800 — AI adds ['D1.20']

## Proposition 1.2
**Statement:** To place at a given point (as an extremity) a straight line equal to a given straight line.

**Step 1.** Let A be the given point and BC the given straight line. We must place at point A a straight line equal to BC.

**Step 2.** Join the point A to the point B by the straight line AB. [P1]

**Step 3.** On the straight line AB, construct an equilateral triangle DAB. [1.1]

**Step 4.** Produce the straight lines DA and DB in a straight line to E and F respectively. [P2]

**Step 5.** With centre B and radius BC, describe the circle CGH. [P3]

**Step 6.** The straight line BG, being a radius of circle CGH, is equal to BC, since all straight lines drawn from the centre B to the circumference of circle CGH are equal. [D1.15]

**Step 7.** With centre D and radius DG, describe the circle GKL. [P3]

**Step 8.** The straight line DL, being a radius of circle GKL, is equal to DG, since all straight lines drawn from the centre D to the circumference of circle GKL are equal. [D1.15]

**Step 9.** Since the triangle DAB is equilateral, DA is equal to DB. [D1.20]

**Step 10.** Since DL equals DG, and DA equals DB, subtracting equals from equals, the remainder AL is equal to the remainder BG. [CN3]

**Step 11.** Since BG was shown equal to BC, and AL was shown equal to BG, therefore AL is equal to BC. [CN1]

**Step 12.** Therefore at the given point A, the straight line AL has been placed, equal to the given straight line BC, which is what was required to be done.

**USED:** 1.1, CN1, CN3, D1.15, D1.20, P1, P2, P3
**Human refs (from References field):** 1.1, CN1, CN3, P1, P2, P3
**Jaccard:** 0.750 — AI adds ['D1.15', 'D1.20']

## Proposition 1.3
**Statement:** Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

**Step 1.** Let AB be the greater straight line and C be the less. We are required to cut off from AB a straight line equal to C.

**Step 2.** By Proposition 1.2, place at the point A a straight line AD equal to C, so that AD = C.

**Step 3.** With centre A and distance AD, describe the circle DEF (Postulate 3).

**Step 4.** Since A is the centre of the circle DEF, and both AD and AE are straight lines from the centre A to the circumference, we have AE = AD (Definition 1.15: all straight lines falling from the centre upon the circumference of a circle are equal to one another).

**Step 5.** But AD = C (Step 2). Therefore AE = C (Common Notion 1: things equal to the same thing are equal to one another).

**Step 6.** Therefore, given the two unequal straight lines AB and C, from AB the greater the straight line AE has been cut off equal to C the less. This is what was required to be done.

**USED:** 1.2, CN1, D1.15, P3
**Human refs (from References field):** 1.2, CN1, D1.15, P3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.4
**Statement:** If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base, the triangle will be equal to the triangle, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend.

**Step 1.** Let ABC and DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively, namely AB equal to DE and AC equal to DF, and the angle BAC equal to the angle EDF. We are to show that the base BC equals the base EF, that the triangle ABC equals the triangle DEF, and that the remaining angles equal the remaining angles respectively, namely angle ABC equals angle DEF and angle ACB equals angle DFE.

**Step 2.** Apply the triangle ABC to the triangle DEF by placing the point A on the point D and the straight line AB along the straight line DE. Since the straight line AB is equal to the straight line DE, the point B will coincide with the point E [CN4, since equal lengths laid along the same line from the same point must end at the same point].

**Step 3.** Since AB coincides with DE, and the angle BAC is equal to the angle EDF, the straight line AC will also coincide with the straight line DF. For if AC, when placed on DF, fell to one side of it (say as DG), then the angle BAC, which equals the angle EDG, would not equal the angle EDF, contradicting the hypothesis that angle BAC equals angle EDF.

**Step 4.** Since AC coincides with DF, and AC is equal to DF, the point C will coincide with the point F [CN4, since equal lengths laid along the same line from the same point must end at the same point].

**Step 5.** But B has already coincided with E (Step 2). Therefore, since B coincides with E and C coincides with F, the base BC coincides with the base EF. For if B coincides with E and C with F, yet BC does not coincide with EF, then two distinct straight lines would enclose a space, which is impossible [P1, since there is exactly one straight line from any point to any point].

**Step 6.** Since BC coincides with EF, BC is equal to EF [CN4].

**Step 7.** Since the three sides of triangle ABC coincide respectively with the three sides of triangle DEF, the whole triangle ABC coincides with the whole triangle DEF, and therefore triangle ABC is equal to triangle DEF [CN4].

**Step 8.** Since the triangles coincide, the remaining angles also coincide with and are therefore equal to the remaining angles: angle ABC equals angle DEF, and angle ACB equals angle DFE [CN4].

**USED:** CN4, P1
**Human refs (from References field):** CN4
**Jaccard:** 0.500 — AI adds ['P1']

## Proposition 1.5
**Statement:** In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

**Step 1.** Let ABC be an isosceles triangle in which AB = AC. Produce AB beyond B to a point D, and produce AC beyond C to a point E [P2]. We are to show that angle ABC = angle ACB, and that angle DBC = angle ECB.

**Step 2.** Take an arbitrary point F on BD. From CE, cut off AG equal to AF [1.3]. (Since AF > AC, and AE extends beyond C, the point G falls on CE beyond C.)

**Step 3.** Join FC and GB [P1].

**Step 4.** Consider triangles AFC and AGB. We have AF = AG (by construction), AC = AB (given, since AB = AC), and the angle FAC is common to both triangles (angle FAC = angle GAB, being the same angle at vertex A). Therefore, by the side-angle-side criterion [1.4], triangle AFC is equal to triangle AGB, and hence: the base FC = the base GB, angle ACF = angle ABG, and angle AFC = angle AGB.

**Step 5.** Since AF = AG (construction) and AB = AC (given), subtracting equals from equals gives BF = CG [CN3].

**Step 6.** Consider triangles BFC and CGB. We have BF = CG (Step 5), FC = GB (Step 4), and angle BFC = angle CGB (Step 4, since angle AFC = angle AGB, and these are the same angles). Therefore, by the side-angle-side criterion [1.4], triangle BFC is equal to triangle CGB, and hence: angle FBC = angle GCB, and angle BCF = angle CBG.

**Step 7.** From Step 4, angle ABG = angle ACF. From Step 6, angle CBG = angle BCF. Subtracting the lesser from the greater in each case: angle ABG - angle CBG = angle ACF - angle BCF, that is, angle ABC = angle ACB [CN3]. These are the angles at the base of the isosceles triangle, and they are equal.

**Step 8.** From Step 6, angle FBC = angle GCB. Since F lies on BD and G lies on CE, these are the angles under the base, namely angle DBC = angle ECB, and they are equal.

**Step 9.** Therefore, in isosceles triangles the angles at the base are equal to one another, and if the equal straight lines be produced further, the angles under the base are equal to one another. Q.E.D.

**USED:** 1.3, 1.4, CN3, P1, P2
**Human refs (from References field):** 1.3, 1.4, P1, P2
**Jaccard:** 0.800 — AI adds ['CN3']

## Proposition 1.6
**Statement:** If in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another.

**Step 1.** Let ABC be a triangle having the angle ABC equal to the angle ACB. I say that the side AB is also equal to the side AC.

**Step 2.** For suppose AB is not equal to AC. Then one of them is greater. Let AB be greater than AC.

**Step 3.** From AB the greater, cut off DB equal to AC the less [1.3].

**Step 4.** Join DC [P1].

**Step 5.** Now in the triangles DBC and ACB, we have DB equal to AC (by construction), BC is common to both triangles, and the angle DBC is equal to the angle ACB (since angle DBC is the same as the given angle ABC, which equals angle ACB by hypothesis).

**Step 6.** Therefore, by the side-angle-side congruence criterion, triangle DBC is equal to triangle ACB [1.4].

**Step 7.** But triangle DBC is a part of triangle ABC, while triangle ACB is the whole triangle ABC. Therefore the part would equal the whole, which is impossible [CN5].

**Step 8.** Therefore AB is not unequal to AC; hence AB equals AC.

**Step 9.** Therefore, if in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another. Q.E.D.

**USED:** 1.3, 1.4, CN5, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.3', '1.4', 'CN5', 'P1']

## Proposition 1.7
**Statement:** Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities), and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively, namely each to that which has the same extremity with it.

**Step 1.** Let AB be the given straight line, and let AC, BC be two straight lines constructed from its extremities A, B and meeting at point C. Suppose, for the sake of contradiction, that two other straight lines AD, BD can be constructed from A, B on the same side of AB, meeting at a different point D, with AC = AD and BC = BD.

**Step 2.** Join CD [P1].

**Step 3.** Since AC = AD, triangle ACD is isosceles. Therefore the base angles are equal: angle ACD = angle ADC [1.5].

**Step 4.** Now since D is a point distinct from C on the same side of AB with lines from A and B meeting at both, consider the configuration at vertex C. The angle ACD is greater than the angle BCD, since angle ACD contains angle BCD as a part [CN5].

**Step 5.** Since angle ACD = angle ADC (Step 3) and angle ACD > angle BCD (Step 4), it follows that angle ADC > angle BCD.

**Step 6.** Since BC = BD, triangle BCD is isosceles. Therefore the base angles are equal: angle BCD = angle BDC [1.5].

**Step 7.** From Step 5, angle ADC > angle BCD. Since angle BCD = angle BDC (Step 6), it follows that angle ADC > angle BDC.

**Step 8.** But at vertex D, the angle BDC contains the angle ADC as a part, so angle BDC > angle ADC [CN5].

**Step 9.** Steps 7 and 8 are contradictory: we cannot have both angle ADC > angle BDC and angle BDC > angle ADC. Therefore the assumption that two such distinct points C and D exist is false.

**Step 10.** Hence, given two straight lines constructed on a straight line from its extremities and meeting in a point, there cannot be constructed on the same straight line, from its extremities, and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively. Q.E.D.

**USED:** 1.5, CN5, P1
**Human refs (from References field):** 1.5
**Jaccard:** 0.333 — AI adds ['CN5', 'P1']

## Proposition 1.8
**Statement:** If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines.

**Step 1.** Let ABC and DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively, namely AB equal to DE and AC equal to DF, and let the base BC be equal to the base EF. I say that the angle BAC is equal to the angle EDF.

**Step 2.** Apply the triangle ABC to the triangle DEF so that the point B is placed on the point E and the straight line BC is placed along the straight line EF. Then the point C will coincide with the point F, because BC is equal to EF.

**Step 3.** BC coinciding with EF, the sides BA and AC will also coincide with ED and DF respectively. For if the base BC coincides with the base EF but the sides BA, AC do not coincide with the sides ED, DF, but take a different position such as EG, GF, then given two straight lines constructed on a straight line from its extremities and meeting in a point, there will have been constructed on the same straight line from its extremities, and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively, namely each to that which has the same extremity with it. But this is impossible by Proposition 1.7.

**Step 4.** Therefore the side BA does coincide with ED and the side AC with DF. It follows that the angle BAC coincides with the angle EDF.

**Step 5.** Things which coincide with one another are equal to one another, by Common Notion 4. Therefore the angle BAC is equal to the angle EDF.

**USED:** 1.7, CN4
**Human refs (from References field):** 1.7
**Jaccard:** 0.500 — AI adds ['CN4']

## Proposition 1.9
**Statement:** To bisect a given rectilineal angle.

**Step 1.** Let the angle BAC be the given rectilineal angle. It is required to bisect it.

**Step 2.** Take an arbitrary point D on the ray AB.

**Step 3.** Using Proposition 1.3, cut off from AC a straight line AE equal to AD, so that AE = AD.

**Step 4.** Join D to E by Postulate 1, forming the straight line DE.

**Step 5.** On the straight line DE, construct an equilateral triangle DEF on the side of DE that is away from A, by Proposition 1.1.

**Step 6.** Join A to F by Postulate 1, forming the straight line AF.

**Step 7.** Now consider triangles ADF and AEF. We have: AD = AE (by construction in Step 3); DF = EF (since triangle DEF is equilateral, all its sides are equal by Definition 1.20, so DF = DE = EF, and in particular DF = EF); and AF is common to both triangles.

**Step 8.** Since the two triangles ADF and AEF have three sides equal to three sides respectively (AD = AE, DF = EF, AF = AF), by Proposition 1.8 (SSS congruence) the angles contained by the equal sides are equal. In particular, angle DAF equals angle EAF.

**Step 9.** Since angle DAF equals angle EAF, the straight line AF bisects the given rectilineal angle BAC. Therefore the angle BAC has been bisected by the straight line AF, which is what was required to do.

**USED:** 1.1, 1.3, 1.8, D1.20, P1
**Human refs (from References field):** 1.3, 1.8
**Jaccard:** 0.400 — AI adds ['1.1', 'D1.20', 'P1']

## Proposition 1.10
**Statement:** To bisect a given finite straight line.

**Step 1.** Let AB be the given finite straight line. It is required to bisect it.

**Step 2.** Construct an equilateral triangle ACB on AB [1.1]. Since triangle ACB is equilateral, we have AC = CB [D1.20].

**Step 3.** Bisect the angle ACB by the straight line CD, where D lies on AB [1.9].

**Step 4.** In triangles ACD and BCD, we have AC = BC (from Step 2), CD is common to both triangles, and angle ACD = angle BCD (since CD bisects angle ACB, from Step 3).

**Step 5.** Therefore, by the side-angle-side congruence, triangle ACD is equal to triangle BCD, and the remaining corresponding parts are equal. In particular, AD = DB [1.4].

**Step 6.** Therefore the given finite straight line AB has been bisected at the point D, which is what was required to do.

**USED:** 1.1, 1.4, 1.9, D1.20
**Human refs (from References field):** 1.1, 1.4, 1.9
**Jaccard:** 0.750 — AI adds ['D1.20']

## Proposition 1.11
**Statement:** To draw a straight line at right angles to a given straight line from a given point on it.

**Step 1.** Let AB be the given straight line and C the given point on it. We must draw a straight line from C at right angles to AB.

**Step 2.** Take an arbitrary point D on the segment AC (that is, on the line AB on one side of C).

**Step 3.** Using Proposition 1.3, cut off from CB a segment CE equal to CD, so that CD = CE. [1.3]

**Step 4.** On the segment DE, construct an equilateral triangle DEF using Proposition 1.1. [1.1]

**Step 5.** Join FC by Postulate 1. [P1]

**Step 6.** Now consider triangles DCF and ECF. We have DC = EC (by construction in Step 3), CF is common to both triangles, and DF = EF (since triangle DEF is equilateral, by Step 4).

**Step 7.** Therefore, by Proposition 1.8 (SSS congruence), since the two triangles DCF and ECF have three sides equal to three sides respectively, the angle DCF equals the angle ECF. [1.8]

**Step 8.** But angles DCF and ECF are adjacent angles formed by the straight line FC standing on the straight line DE (which lies along AB). Since these adjacent angles are equal to one another, each of them is a right angle, and the straight line CF is perpendicular to AB, by Definition 1.10. [D1.10]

**Step 9.** Therefore, the straight line FC has been drawn at right angles to the given straight line AB from the given point C on it, which is what was required to do.

**USED:** 1.1, 1.3, 1.8, D1.10, P1
**Human refs (from References field):** 1.1, 1.3, 1.8, D1.10
**Jaccard:** 0.800 — AI adds ['P1']

## Proposition 1.12
**Statement:** To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

**Step 1.** Let AB be the given infinite straight line and C the given point not on it. We must draw from C a straight line perpendicular to AB.

**Step 2.** Take an arbitrary point D on the opposite side of line AB from C. With center C and radius CD, describe a circle [P3]. Since C is not on AB and D is on the other side of AB from C, this circle intersects the straight line AB at two points. Let these points of intersection be G and E.

**Step 3.** Bisect the straight line GE at the point H [1.10].

**Step 4.** Join CG, CH, and CE [P1].

**Step 5.** Since G and E are both on the circle with center C, we have CG = CE [D1.15].

**Step 6.** Since H is the midpoint of GE, we have GH = HE [1.10].

**Step 7.** The side CH is common to triangles CHG and CHE.

**Step 8.** Therefore, triangles CHG and CHE have three sides equal to three sides respectively: CG = CE, GH = HE, and CH = CH. By the side-side-side congruence theorem, the angle CHG equals the angle CHE [1.8].

**Step 9.** Since the straight line CH standing on the straight line AB makes the adjacent angles CHG and CHE equal to one another, each of these equal angles is a right angle, and the straight line CH is perpendicular to AB [D1.10].

**Step 10.** Therefore, from the given point C, which is not on the given infinite straight line AB, a perpendicular CH has been drawn to AB, which is what was required to do.

**USED:** 1.10, 1.8, D1.10, D1.15, P1, P3
**Human refs (from References field):** 1.10, 1.8, D1.10, P1, P3
**Jaccard:** 0.833 — AI adds ['D1.15']

## Proposition 1.13
**Statement:** If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

**Step 1.** Let the straight line AB be set up on the straight line CD, making angles CBA and ABD. I say that the angles CBA and ABD are either two right angles or equal to two right angles.

**Step 2.** First, suppose angle CBA is equal to angle ABD. Since the straight line AB standing on CD makes the adjacent angles CBA and ABD equal to one another, each of them is a right angle [D1.10]. Thus in this case AB makes two right angles with CD.

**Step 3.** Now suppose angle CBA is not equal to angle ABD. Draw BE from the point B at right angles to CD [1.11]. Then each of the angles CBE and EBD is a right angle [D1.10].

**Step 4.** Since the angle CBE is composed of the angles CBA and ABE, we have angle CBE equals angle CBA plus angle ABE. Adding angle EBD to each side, the sum angle CBE plus angle EBD equals angle CBA plus angle ABE plus angle EBD [CN2].

**Step 5.** Again, since the angle DBA is composed of the angles DBE and EBA, we have angle DBA equals angle DBE plus angle EBA. Adding angle ABC to each side, the sum angle ABC plus angle DBA equals angle ABC plus angle DBE plus angle EBA [CN2].

**Step 6.** But it has been shown that the sum angle CBE plus angle EBD also equals angle CBA plus angle ABE plus angle EBD. Since the right-hand sides are the same three angles (angle CBA is the same as angle ABC, angle ABE is the same as angle EBA, and angle DBE is the same as angle EBD), the sums angle CBE plus angle EBD and angle ABC plus angle DBA are equal to one another [CN1].

**Step 7.** But angles CBE and EBD are both right angles. Therefore the angles ABC and ABD are together equal to two right angles.

**Step 8.** Therefore, if a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles. Q.E.D.

**USED:** 1.11, CN1, CN2, D1.10
**Human refs (from References field):** 1.11, CN1, CN2, D1.10
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.14
**Statement:** If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

**Step 1.** Let AB be a straight line, and let BC and BD be two straight lines not lying on the same side of AB, drawn from the point B on AB, such that the adjacent angles ABC and ABD are together equal to two right angles.

**Step 2.** We claim that BD is in a straight line with BC. Suppose, for the sake of contradiction, that BD is not in a straight line with BC.

**Step 3.** Since BD is assumed not to be in a straight line with BC, produce CB in a straight line to a point E on the other side of AB [P2]. Then BE is in a straight line with BC.

**Step 4.** Since the straight line AB stands on the straight line CBE, the angles ABC and ABE together equal two right angles [1.13].

**Step 5.** But by hypothesis, the angles ABC and ABD together equal two right angles.

**Step 6.** Therefore the angles ABC and ABE together equal the angles ABC and ABD together [CN1], since both sums equal two right angles.

**Step 7.** Subtract the angle ABC from each sum. Then angle ABE equals angle ABD [CN3].

**Step 8.** But angle ABE is only a part of angle ABD (since BD is not the same line as BE, and E lies beyond D from the perspective of the produced line, making ABE a proper part of ABD, or vice versa). Therefore the lesser equals the greater, which is impossible [CN5].

**Step 9.** Therefore the assumption that BD is not in a straight line with BC is false. Hence BD is in a straight line with BC, which was to be proved. Q.E.D.

**USED:** 1.13, CN1, CN3, CN5, P2
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.500 — AI adds ['CN5', 'P2']; Human adds ['P4']

## Proposition 1.15
**Statement:** If two straight lines cut one another, they make the vertical angles equal to one another.

**Step 1.** Let the two straight lines AB and CD cut one another at the point E. We must prove that the vertical angles are equal, namely that angle AEC equals angle DEB, and angle CEB equals angle AED.

**Step 2.** Since CE stands on the straight line AB, by Proposition 1.13 the angles AEC and CEB together equal two right angles.

**Step 3.** Since BE stands on the straight line CD, by Proposition 1.13 the angles CEB and BED together equal two right angles.

**Step 4.** From Steps 2 and 3, the sum angle AEC + angle CEB equals the sum angle CEB + angle BED, since both are equal to two right angles (CN1).

**Step 5.** Subtracting the common angle CEB from both sums (CN3), we conclude that angle AEC equals angle BED.

**Step 6.** Now, since DE stands on the straight line AB, by Proposition 1.13 the angles AED and DEB together equal two right angles.

**Step 7.** From Steps 3 and 6, the sum angle CEB + angle BED equals the sum angle AED + angle DEB, since both are equal to two right angles (CN1).

**Step 8.** Subtracting the common angle BED from both sums (CN3), we conclude that angle CEB equals angle AED.

**Step 9.** Therefore, if two straight lines cut one another, they make the vertical angles equal to one another, which was to be proved.

**USED:** 1.13, CN1, CN3
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.750 — Human adds ['P4']

## Proposition 1.16
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

**Step 1.** Let ABC be a triangle, and let the side BC be produced to D. We shall show that the exterior angle ACD is greater than each of the interior and opposite angles BAC and ABC.

**Step 2.** Bisect AC at E [1.10], so that AE = EC.

**Step 3.** Join B to E by a straight line [P1], and produce BE in a straight line to F [P2].

**Step 4.** Cut off EF equal to BE on the produced segment [1.3].

**Step 5.** Join F to C by a straight line [P1].

**Step 6.** Since AE = EC (Step 2), BE = EF (Step 4), and angle AEB equals angle CEF (for they are vertical angles formed by the straight lines AC and BF cutting one another at E) [1.15], the two triangles AEB and CEF have two sides equal to two sides respectively and the included angles equal.

**Step 7.** Therefore, by the side-angle-side congruence, triangle AEB is congruent to triangle CEF, and in particular angle BAE = angle ECF [1.4].

**Step 8.** Now angle ACD is the whole, and angle ECF is a part of it (since E lies on CA, the ray CF falls within the angle ACD). Therefore angle ACD is greater than angle ECF [CN5].

**Step 9.** But angle ECF = angle BAE (Step 7), and angle BAE is the same as angle BAC. Therefore angle ACD is greater than angle BAC [CN5].

**Step 10.** Next, to show that angle ACD is also greater than angle ABC, bisect BC at M [1.10], so that BM = MC.

**Step 11.** Join A to M by a straight line [P1], and produce AM in a straight line to N [P2].

**Step 12.** Cut off MN equal to MA on the produced segment [1.3].

**Step 13.** Join N to C by a straight line [P1].

**Step 14.** Since BM = MC (Step 10), AM = MN (Step 12), and angle AMB equals angle NMC (for they are vertical angles formed by the straight lines BC and AN cutting one another at M) [1.15], the two triangles AMB and NMC have two sides equal to two sides respectively and the included angles equal.

**Step 15.** Therefore, by the side-angle-side congruence, triangle AMB is congruent to triangle NMC, and in particular angle ABM = angle NCM [1.4].

**Step 16.** Now angle ABM is the same as angle ABC. The ray CN falls within the angle ACD (since M lies on BC and N is on the opposite side of line BC from A, placing the ray CN between the rays CA and CD). Therefore angle ACD is greater than angle NCM [CN5].

**Step 17.** But angle NCM = angle ABM = angle ABC (Step 15). Therefore angle ACD is greater than angle ABC.

**Step 18.** Hence the exterior angle ACD is greater than each of the interior and opposite angles BAC and ABC. Q.E.D.

**USED:** 1.10, 1.15, 1.3, 1.4, CN5, P1, P2
**Human refs (from References field):** 1.10, 1.15, 1.3, 1.4, CN5, P1, P2
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.17
**Statement:** In any triangle two angles taken together in any manner are less than two right angles.

**Step 1.** Let ABC be any triangle. We shall prove that any two of its angles taken together are less than two right angles.

**Step 2.** Produce side BC to point D [P2]. Then angle ACD is an exterior angle of triangle ABC.

**Step 3.** By Proposition 1.16, the exterior angle ACD is greater than the interior and opposite angle ABC. That is, angle ACD > angle ABC.

**Step 4.** By Proposition 1.13, since the straight line AC stands on line BD, the angles ACB and ACD together equal two right angles. That is, angle ACB + angle ACD = two right angles.

**Step 5.** Since angle ACD > angle ABC (Step 3), replacing angle ACD with the smaller angle ABC yields a lesser sum. Therefore angle ACB + angle ABC < angle ACB + angle ACD = two right angles. Hence angles ACB and ABC together are less than two right angles.

**Step 6.** Now produce side AB to point E [P2]. Then angle CBE is an exterior angle of triangle ABC at vertex B.

**Step 7.** By Proposition 1.16, the exterior angle CBE is greater than the interior and opposite angle BAC. That is, angle CBE > angle BAC.

**Step 8.** By Proposition 1.13, since the straight line BC stands on line AE, the angles ABC and CBE together equal two right angles. That is, angle ABC + angle CBE = two right angles.

**Step 9.** Since angle CBE > angle BAC (Step 7), replacing angle CBE with the smaller angle BAC yields a lesser sum. Therefore angle ABC + angle BAC < angle ABC + angle CBE = two right angles. Hence angles ABC and BAC together are less than two right angles.

**Step 10.** Finally, produce side AC to point F [P2]. Then angle BAF is an exterior angle of triangle ABC at vertex A, formed by producing side CA beyond A. Wait -- let us instead produce BC to D as before and apply 1.16 differently. Actually, produce BA to point G [P2]. Then angle CAG is an exterior angle of triangle ABC at vertex A.

**Step 11.** By Proposition 1.16, the exterior angle CAG is greater than the interior and opposite angle ACB. That is, angle CAG > angle ACB.

**Step 12.** By Proposition 1.13, since the straight line AC stands on line BG, the angles BAC and CAG together equal two right angles. That is, angle BAC + angle CAG = two right angles.

**Step 13.** Since angle CAG > angle ACB (Step 11), replacing angle CAG with the smaller angle ACB yields a lesser sum. Therefore angle BAC + angle ACB < angle BAC + angle CAG = two right angles. Hence angles BAC and ACB together are less than two right angles.

**Step 14.** We have now shown that each pair of angles of triangle ABC -- namely angles ABC and ACB (Step 5), angles ABC and BAC (Step 9), and angles BAC and ACB (Step 13) -- taken together are less than two right angles. Therefore, in any triangle, two angles taken together in any manner are less than two right angles. Q.E.D.

**USED:** 1.13, 1.16, P2
**Human refs (from References field):** 1.13, 1.16, P2
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.18
**Statement:** In any triangle the greater side subtends the greater angle.

**Step 1.** Let ABC be a triangle in which side AC is greater than side AB. We must show that angle ABC (subtended by the greater side AC) is greater than angle ACB (subtended by the lesser side AB).

**Step 2.** Since AC is greater than AB, by Proposition 1.3 we may cut off from AC a straight line AD equal to AB, where D lies on AC between A and C.

**Step 3.** Join B to D by Postulate P1.

**Step 4.** In triangle ABD, since AB equals AD (by construction in Step 2), triangle ABD is isosceles. Therefore by Proposition 1.5, angle ABD equals angle ADB.

**Step 5.** Now consider triangle BDC. Since D lies between A and C, the angle ADB is an exterior angle of triangle BDC formed by producing side CD beyond D to A. By Proposition 1.16, the exterior angle ADB of triangle BDC is greater than the interior and opposite angle DCB, that is, angle ADB is greater than angle ACB.

**Step 6.** Since D lies between A and C, the ray BD falls within angle ABC, and therefore angle ABD is a part of angle ABC. By Common Notion CN5 (the whole is greater than the part), angle ABC is greater than angle ABD.

**Step 7.** From Step 4, angle ABD equals angle ADB. From Step 5, angle ADB is greater than angle ACB. Therefore angle ABD is greater than angle ACB. Combining with Step 6, since angle ABC is greater than angle ABD, and angle ABD is greater than angle ACB, it follows that angle ABC is greater than angle ACB.

**Step 8.** Therefore in triangle ABC the greater side AC subtends the greater angle ABC, which is what was to be proved.

**USED:** 1.16, 1.3, 1.5, CN5, P1
**Human refs (from References field):** 1.16, 1.3
**Jaccard:** 0.400 — AI adds ['1.5', 'CN5', 'P1']

## Proposition 1.19
**Statement:** In any triangle the greater angle is subtended by the greater side.

**Step 1.** Let ABC be a triangle in which angle ABC is greater than angle BCA. We claim that side AC (which subtends angle ABC) is greater than side AB (which subtends angle BCA).

**Step 2.** There are three exhaustive possibilities for the relationship between AC and AB: either AC equals AB, or AC is less than AB, or AC is greater than AB.

**Step 3.** Suppose AC equals AB. Then triangle ABC is isosceles with two equal sides AC and AB. By Proposition 1.5, the base angles are equal, so angle ABC equals angle BCA. But this contradicts our hypothesis that angle ABC is greater than angle BCA. Therefore AC does not equal AB.

**Step 4.** Suppose AC is less than AB. Then AB is the greater side of triangle ABC. By Proposition 1.18, the greater side subtends the greater angle, so the angle subtended by AB (namely angle BCA) is greater than the angle subtended by AC (namely angle ABC). That is, angle BCA is greater than angle ABC. But this contradicts our hypothesis that angle ABC is greater than angle BCA. Therefore AC is not less than AB.

**Step 5.** Since AC is neither equal to AB nor less than AB, the remaining possibility is that AC is greater than AB.

**Step 6.** Therefore the side AC, which subtends the greater angle ABC, is greater than the side AB, which subtends the lesser angle BCA. Hence in any triangle the greater angle is subtended by the greater side, which is what was to be proved.

**USED:** 1.18, 1.5
**Human refs (from References field):** 1.18, 1.5
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.20
**Statement:** In any triangle two sides taken together in any manner are greater than the remaining one.

**Step 1.** Let ABC be any triangle. We shall prove that any two sides taken together are greater than the remaining side. It suffices to show that BA + AC > BC; the other two inequalities follow by an identical argument applied to the other pairs of sides.

**Step 2.** Produce the straight line BA beyond A to a point D such that AD = AC. This is accomplished by first extending BA beyond A [P2], then cutting off from the extended ray AD equal to AC [1.3].

**Step 3.** Join D to C [P1]. Now in triangle ACD, we have DA = AC by construction. Therefore triangle ACD is isosceles with DA = AC, and so the base angles are equal: angle ACD = angle ADC [1.5].

**Step 4.** Observe that angle BCD is the whole of which angle ACD is a part, since A lies between B and D, and C is not on line BD. Therefore angle BCD > angle ACD [CN5].

**Step 5.** Since angle ACD = angle ADC (Step 3) and angle BCD > angle ACD (Step 4), we conclude angle BCD > angle ADC. But angle ADC is the same angle as angle BDC (since B, A, D are collinear with A between B and D, so D sees C at the same angle from line BD). Thus angle BCD > angle BDC.

**Step 6.** In triangle BDC, angle BCD > angle BDC. Therefore the side opposite the greater angle is greater than the side opposite the lesser angle: BD > BC [1.19].

**Step 7.** Now BD = BA + AD (since A lies between B and D), and AD = AC (by construction in Step 2). Therefore BD = BA + AC.

**Step 8.** Since BD > BC (Step 6) and BD = BA + AC (Step 7), we conclude BA + AC > BC.

**Step 9.** By applying the same construction and argument starting from the other vertices, we obtain similarly that AB + BC > AC and that AC + CB > AB. Therefore, in triangle ABC, any two sides taken together are greater than the remaining one.

**USED:** 1.19, 1.3, 1.5, CN5, P1, P2
**Human refs (from References field):** 1.19, 1.5, CN5
**Jaccard:** 0.500 — AI adds ['1.3', 'P1', 'P2']

## Proposition 1.21
**Statement:** If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greaterangle.

**Step 1.** Let ABC be a triangle, and from the extremities B and C of side BC, let two straight lines BD and CD be constructed meeting at a point D within the triangle. We are to prove that BD + DC < BA + AC, and that angle BDC > angle BAC.

**Step 2.** Produce BD beyond D to meet AC at a point E [P2, P1]. Such a point E exists because D is inside triangle ABC, so the ray from B through D must cross side AC.

**Step 3.** Consider triangle ABE. By Proposition 1.20, the two sides BA and AE are together greater than the remaining side BE. That is, BA + AE > BE.

**Step 4.** Add EC to both sides of this inequality. Then BA + AE + EC > BE + EC [CN2]. Since E lies on segment AC, we have AE + EC = AC. Therefore BA + AC > BE + EC.

**Step 5.** Now consider triangle DEC. By Proposition 1.20, the two sides DE and EC are together greater than the remaining side DC. That is, DE + EC > DC.

**Step 6.** Add BD to both sides of this inequality. Then BD + DE + EC > BD + DC [CN2]. Since D lies on segment BE, we have BD + DE = BE. Therefore BE + EC > BD + DC.

**Step 7.** From Step 4 we have BA + AC > BE + EC, and from Step 6 we have BE + EC > BD + DC. Therefore BA + AC > BD + DC. Equivalently, BD + DC < BA + AC, which is the first part of what was to be proved.

**Step 8.** For the angle: in triangle DEC, the angle BDC is an exterior angle (formed by producing side ED of the triangle beyond D to B). By Proposition 1.16, the exterior angle BDC is greater than the interior and opposite angle DEC. That is, angle BDC > angle DEC.

**Step 9.** Similarly, in triangle ABE, the angle DEC (which is the same as angle AEB) is an exterior angle (formed by producing side AE of the triangle beyond E, since BE produced meets AC at E, making angle AEB an exterior angle at vertex E when side BE is produced to D — more precisely, angle BEA is exterior to triangle ABE when we consider that E lies on AC and BE crosses from inside). Let us state this more carefully: in triangle ABE, side BE meets vertex E, and the line EC is the production of AE beyond E. Thus angle BEC is an exterior angle of triangle ABE at vertex E. By Proposition 1.16, angle BEC > angle BAE, that is, angle DEC > angle BAC.

**Step 10.** From Step 8 we have angle BDC > angle DEC, and from Step 9 we have angle DEC > angle BAC. Therefore angle BDC > angle BAC, which is the second part of what was to be proved.

**Step 11.** Therefore, if on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed are less than the remaining two sides of the triangle, but contain a greater angle. Q.E.F.

**USED:** 1.16, 1.20, CN2, P1, P2
**Human refs (from References field):** 1.16, 1.20
**Jaccard:** 0.400 — AI adds ['CN2', 'P1', 'P2']

## Proposition 1.22
**Statement:** Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manner should be greater than the remaining one.

**Step 1.** Let A, B, C be three given straight lines such that any two taken together in any manner are greater than the remaining one. It is required to construct a triangle out of straight lines equal to A, B, C.

**Step 2.** Set out a straight line DE, terminated at D but infinite in the direction of E [P2]. Using Proposition 1.3, cut off DF equal to A, FG equal to B, and GH equal to C from the line DE [1.3].

**Step 3.** With center F and distance FD, describe the circle DKL [P3]. With center G and distance GH, describe the circle KLH [P3].

**Step 4.** We must show these two circles intersect. Since any two of A, B, C are greater than the remaining one, we have in particular B + C > A, i.e., FG + GH > FD. Thus GH > FD - FG. Also A + C > B, i.e., FD + GH > FG, so FD + GH > FG, meaning the distance FG between the centers is less than the sum of the two radii FD and GH. And B < A + C gives FG < FD + GH. Also A < B + C gives FD < FG + GH, so FG > FD - GH, meaning the distance between centers exceeds the absolute difference of the radii. Therefore the circles meet; let them intersect at the point K. [1.20]

**Step 5.** Join KF and KG [P1].

**Step 6.** Since F is the center of circle DKL, and FD and FK are both radii, we have FK = FD [D1.15]. But FD = A [Step 2]. Therefore FK = A [CN1].

**Step 7.** Since G is the center of circle KLH, and GH and GK are both radii, we have GK = GH [D1.15]. But GH = C [Step 2]. Therefore GK = C [CN1].

**Step 8.** And FG = B by construction [Step 2].

**Step 9.** Therefore the triangle KFG has its three sides FK, FG, GK equal to the three given straight lines A, B, C respectively. Thus out of three straight lines FK, FG, GK, which are equal to the three given straight lines A, B, C, a triangle KFG has been constructed. Q.E.F.

**USED:** 1.20, 1.3, CN1, D1.15, P1, P2, P3
**Human refs (from References field):** 1.20, 1.3
**Jaccard:** 0.286 — AI adds ['CN1', 'D1.15', 'P1', 'P2', 'P3']

## Proposition 1.23
**Statement:** On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

**Step 1.** Let the given straight line be AB, let A be the given point on it, and let angle DCE be the given rectilineal angle.

**Step 2.** Take arbitrary points D and E on the rays CD and CE respectively, so that D and E are distinct from C.

**Step 3.** Join D to E [P1], forming triangle CDE.

**Step 4.** On the straight line AB, construct triangle AFG out of three straight lines equal to CD, CE, and DE, such that AF equals CD, AG equals CE, and FG equals DE [1.22]. This construction is valid because CD, CE, and DE are sides of an existing triangle, so any two of them taken together are greater than the remaining one [the necessary condition stated in 1.22 is satisfied, as verified by 1.20 applied to triangle CDE].

**Step 5.** Since AF equals CD, AG equals CE, and FG equals DE, the two triangles AFG and CDE have their three sides respectively equal to one another.

**Step 6.** Therefore, by the Side-Side-Side congruence criterion, angle FAG equals angle DCE [1.8].

**Step 7.** Thus, on the given straight line AB and at the point A on it, the rectilineal angle FAG has been constructed equal to the given rectilineal angle DCE, which is what was required.

**USED:** 1.20, 1.22, 1.8, P1
**Human refs (from References field):** 1.8
**Jaccard:** 0.250 — AI adds ['1.20', '1.22', 'P1']

## Proposition 1.24
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

**Step 1.** Let ABC and DEF be two triangles having AB equal to DE and AC equal to DF, and let the angle BAC be greater than the angle EDF. I say that the base BC is also greater than the base EF.

**Step 2.** At the point D on the straight line DE, construct the angle EDG equal to the angle BAC, on the same side of DE as F [1.23]. Make DG equal to AC (which also equals DF) [1.3]. Join EG and FG [P1].

**Step 3.** Since AB equals DE, and AC equals DG (by construction), and the angle BAC equals the angle EDG (by construction), therefore the base BC equals the base EG, and triangle ABC is congruent to triangle DEG [1.4].

**Step 4.** Since DF equals DG (for DF equals AC and DG was made equal to AC, hence DF equals DG by CN1), the triangle DFG is isosceles. Therefore the angle DGF equals the angle DFG [1.5].

**Step 5.** Since the angle EDG is greater than the angle EDF (because angle EDG equals angle BAC, which is greater than angle EDF by hypothesis), the ray DF falls within the angle EDG. Consequently, F lies on the opposite side of line EG from D, so the angle DGF is the sum of the angles DGE and EGF. Therefore the angle DGF is greater than the angle EGF [CN5, the whole is greater than the part].

**Step 6.** Since the angle DFG equals the angle DGF [Step 4], and the angle DGF is greater than the angle EGF [Step 5], therefore the angle DFG is greater than the angle EGF.

**Step 7.** From the point F, the ray FD falls within the angle EFG (since D lies between E and G as seen from F). Therefore the angle EFG is greater than the angle DFG [CN5, the whole is greater than the part].

**Step 8.** Since the angle EFG is greater than the angle DFG [Step 7], and the angle DFG is greater than the angle EGF [Step 6], therefore the angle EFG is greater than the angle EGF.

**Step 9.** In triangle EFG, since the angle EFG (at vertex F) is greater than the angle EGF (at vertex G), the side EG, which subtends the greater angle, is greater than the side EF, which subtends the lesser angle [1.19].

**Step 10.** But BC equals EG [Step 3]. Therefore BC is greater than EF. This is what was to be proved.

**USED:** 1.19, 1.23, 1.3, 1.4, 1.5, CN1, CN5, P1
**Human refs (from References field):** 1.19, 1.23, 1.4, 1.5
**Jaccard:** 0.500 — AI adds ['1.3', 'CN1', 'CN5', 'P1']

## Proposition 1.25
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.

**Step 1.** Let ABC and DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively, that is, AB equal to DE and AC equal to DF, but having the base BC greater than the base EF. I say that the angle BAC is greater than the angle EDF.

**Step 2.** The angle BAC is either equal to the angle EDF, or less than it, or greater than it. We shall show it must be greater.

**Step 3.** Suppose, for the sake of contradiction, that angle BAC is equal to angle EDF. Then since AB equals DE, AC equals DF, and angle BAC equals angle EDF, by Proposition 1.4 (the side-angle-side congruence theorem), the base BC would equal the base EF.

**Step 4.** But BC is given as greater than EF, so BC cannot equal EF. This is a contradiction. Therefore angle BAC is not equal to angle EDF.

**Step 5.** Now suppose that angle BAC is less than angle EDF. Then since DE equals AB, DF equals AC, and the angle EDF (contained by the equal sides DE, DF) is greater than the angle BAC (contained by the equal sides AB, AC), by Proposition 1.24 (if two triangles have two sides equal to two sides but the contained angle of one is greater, then the base of that triangle is greater), the base EF would be greater than the base BC.

**Step 6.** But BC is given as greater than EF, so EF cannot be greater than BC. This is a contradiction. Therefore angle BAC is not less than angle EDF.

**Step 7.** Since angle BAC is neither equal to angle EDF nor less than angle EDF, it remains that angle BAC is greater than angle EDF.

**Step 8.** Therefore, if two triangles have two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other. Q.E.F.

**USED:** 1.24, 1.4
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.26
**Statement:** If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of the equal angles, they will also have the remaining sides equal tothe remaining sides and the remaining angle to the remaining angle.

**Step 1.** Let ABC and DEF be two triangles. The proposition has two cases. In Case 1 (ASA), suppose angle ABC equals angle DEF, angle BCA equals angle EFD, and BC equals EF (the side adjoining the equal angles). In Case 2 (AAS), suppose angle ABC equals angle DEF, angle BAC equals angle EDF, and BC equals EF (the side subtending one of the equal angles).

**Step 2.** [Case 1: ASA] Suppose AB is not equal to DE. Then one of them is greater. Without loss of generality, let AB be greater than DE. By 1.3, cut off from AB a segment BG equal to DE, so that BG = DE. Join GC by P1.

**Step 3.** Now in triangles GBC and DEF we have BG = DE (by construction), BC = EF (given), and angle GBC = angle DEF (given, since angle GBC is the same as angle ABC). Therefore by 1.4, triangle GBC is congruent to triangle DEF, and in particular angle GCB = angle DFE.

**Step 4.** But angle BCA = angle EFD (given), so angle GCB = angle BCA. However, angle GCB is a part of angle BCA (since G lies between A and B, the ray CG falls between rays CA and CB). This means a part equals the whole, contradicting CN5.

**Step 5.** Therefore the assumption that AB is not equal to DE is false, so AB = DE.

**Step 6.** Now we have AB = DE, BC = EF, and angle ABC = angle DEF. By 1.4, triangle ABC is congruent to triangle DEF. Therefore AC = DF, and angle BAC = angle EDF. This completes Case 1.

**Step 7.** [Case 2: AAS] Now suppose angle ABC = angle DEF, angle BAC = angle EDF, and BC = EF (the side opposite one of the equal angles). Suppose AB is not equal to DE. Without loss of generality, let AB be greater than DE. By 1.3, cut off from AB a segment BG equal to DE, so that BG = DE. Join GC by P1.

**Step 8.** In triangles GBC and DEF we have BG = DE (by construction), BC = EF (given), and angle GBC = angle DEF (given). Therefore by 1.4, triangle GBC is congruent to triangle DEF, and in particular angle BGC = angle EDF.

**Step 9.** But angle BAC = angle EDF (given), so angle BGC = angle BAC. Now since G lies on segment AB between A and B, the line segment GC lies inside triangle ABC. Consider triangle AGC: the angle BGC is an exterior angle of triangle AGC (being supplementary to angle AGC on the other side of the line AG at point G, or equivalently, since G is between A and B, angle BGC is the exterior angle of triangle AGC formed by producing side AG to B). By 1.16, this exterior angle BGC must be greater than the interior and opposite angle GAC, which is the same as angle BAC. But we derived that angle BGC = angle BAC, a contradiction.

**Step 10.** Therefore the assumption that AB is not equal to DE is false, so AB = DE.

**Step 11.** Now we have AB = DE, BC = EF, and angle ABC = angle DEF. By 1.4, triangle ABC is congruent to triangle DEF. Therefore AC = DF, and angle BCA = angle EFD. This completes Case 2.

**Step 12.** In both cases, the two triangles have the remaining sides equal to the remaining sides and the remaining angle equal to the remaining angle, which is what was to be proved.

**USED:** 1.16, 1.3, 1.4, CN5, P1
**Human refs (from References field):** 1.16, 1.4
**Jaccard:** 0.400 — AI adds ['1.3', 'CN5', 'P1']

## Proposition 1.27
**Statement:** If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

**Step 1.** Let the straight line EF, falling on the two straight lines AB and CD, make the alternate angles AEF and EFD equal to one another. I say that AB is parallel to CD.

**Step 2.** Suppose AB is not parallel to CD. Then, by the definition of parallel lines (D1.23), AB and CD, when produced, will meet in some direction. Suppose they meet, when produced, at a point G on the side of B and D. Then EFG is a triangle.

**Step 3.** In triangle EFG, the angle AEF is an exterior angle, since G lies on the ray from E through B, making AEF the angle formed between the side EF and the extension of side EG beyond E toward A. The angle EFG is an interior angle of the triangle opposite to vertex E.

**Step 4.** By Proposition 1.16, the exterior angle of any triangle is greater than either of the interior and opposite angles. Therefore angle AEF is greater than angle EFG.

**Step 5.** But angle EFG is the same as angle EFD (since G lies on ray FD). Therefore angle AEF is greater than angle EFD.

**Step 6.** This contradicts the hypothesis that angle AEF equals angle EFD.

**Step 7.** Similarly, if AB and CD are supposed to meet on the side of A and C when produced, triangle EFG is formed on that side, and angle EFD becomes an exterior angle of the triangle while angle FEG (which is the same as angle FEA, i.e., angle AEF) is an interior and opposite angle. By 1.16, angle EFD would be greater than angle AEF, again contradicting the hypothesis.

**Step 8.** Since AB and CD cannot meet on either side, they do not meet when produced indefinitely in both directions. Therefore, by D1.23, AB is parallel to CD.

**USED:** 1.16, D1.23

**USED:** 1.16, D1.23
**Human refs (from References field):** 1.16, D1.23
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.28
**Statement:** If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to two right angles, the straight lines will be parallel to one another.

**Step 1.** Let the straight line EF fall on the two straight lines AB and CD. We must prove two cases: (a) if the exterior angle EGB equals the interior and opposite angle GHD on the same side, then AB is parallel to CD; and (b) if the interior angles on the same side, BGH and GHD, are together equal to two right angles, then AB is parallel to CD.

**Step 2.** (Case a) Suppose the exterior angle EGB equals the interior and opposite angle GHD. Now angle EGB is a vertical angle to angle AGH, since the lines EF and AB cut one another at G. By 1.15, angle EGB equals angle AGH.

**Step 3.** Since angle EGB equals angle GHD (given), and angle EGB equals angle AGH (Step 2), it follows by CN1 that angle AGH equals angle GHD.

**Step 4.** But angles AGH and GHD are alternate angles formed by the transversal EF falling on the two straight lines AB and CD. Since these alternate angles are equal, by 1.27 the straight lines AB and CD are parallel to one another.

**Step 5.** (Case b) Suppose the interior angles on the same side, BGH and GHD, are together equal to two right angles.

**Step 6.** Since the straight line EF stands on the straight line AB at G, by 1.13 the angles AGH and BGH together equal two right angles.

**Step 7.** But the angles BGH and GHD together also equal two right angles (given, Step 5). Therefore by CN1, angles AGH and BGH together equal angles BGH and GHD together.

**Step 8.** Subtracting the common angle BGH from each side, by CN3 angle AGH equals angle GHD.

**Step 9.** But angles AGH and GHD are alternate angles. Since they are equal, by 1.27 the straight lines AB and CD are parallel to one another.

**Step 10.** Therefore, in both cases, if a straight line falling on two straight lines makes the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to two right angles, the straight lines are parallel to one another. Q.E.D.

**USED:** 1.13, 1.15, 1.27, CN1, CN3
**Human refs (from References field):** 1.13, 1.15, 1.27
**Jaccard:** 0.600 — AI adds ['CN1', 'CN3']

## Proposition 1.29
**Statement:** A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

**Step 1.** Let the straight line EF fall on the parallel straight lines AB and CD, meeting AB at G and CD at H. We must show: (i) the alternate angles AGH and GHD are equal, (ii) the exterior angle EGB equals the interior and opposite angle GHD, and (iii) the interior angles on the same side BGH and GHD together equal two right angles.

**Step 2.** (Proof of (i) by reductio.) Suppose the alternate angles AGH and GHD are not equal. Then one of them is greater. Suppose angle AGH is greater than angle GHD.

**Step 3.** Add angle BGH to each. Then angle AGH together with angle BGH is greater than angle GHD together with angle BGH [CN2 and the properties of inequality].

**Step 4.** But since EF stands on the straight line AB at G, the angles AGH and BGH together equal two right angles [1.13].

**Step 5.** Therefore the angles BGH and GHD together are less than two right angles.

**Step 6.** But straight lines which are met by a transversal making the interior angles on one side less than two right angles, if produced indefinitely, meet on that side [P5]. Therefore AB and CD, if produced, meet on the side of B and D.

**Step 7.** But AB and CD are parallel, and parallel lines are lines in the same plane which, produced indefinitely in both directions, do not meet one another in either direction [D1.23]. This is a contradiction.

**Step 8.** Therefore angle AGH is not greater than angle GHD. By the same argument (interchanging the roles of the two angles), angle GHD is not greater than angle AGH. Therefore the alternate angles AGH and GHD are equal.

**Step 9.** (Proof of (ii).) Since the straight lines AB and EF cut one another at G, the vertical angles EGB and AGH are equal [1.15].

**Step 10.** But angle AGH was shown equal to angle GHD [Step 8]. Therefore angle EGB equals angle GHD [CN1]. That is, the exterior angle equals the interior and opposite angle.

**Step 11.** (Proof of (iii).) Since angle AGH equals angle GHD [Step 8], add angle BGH to each. Then angle AGH together with angle BGH equals angle GHD together with angle BGH [CN2].

**Step 12.** But angle AGH together with angle BGH equals two right angles [1.13, since EF stands on AB]. Therefore angle GHD together with angle BGH equals two right angles [CN1].

**Step 13.** Therefore a straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles. Q.E.F.

**USED:** 1.13, 1.15, CN1, CN2, D1.23, P5
**Human refs (from References field):** 1.13, 1.15, CN1, CN2, P5
**Jaccard:** 0.833 — AI adds ['D1.23']

## Proposition 1.30
**Statement:** Straight lines parallel to the same straight line are also parallel to one another.

**Step 1.** Let AB and CD be straight lines, each parallel to the straight line EF.

**Step 2.** Let the straight line GHK fall upon all three lines, cutting AB at G, EF at H, and CD at K.

**Step 3.** Since AB is parallel to EF, and the straight line GHK falls upon them, the alternate angles AGH and GHF are equal to one another. [1.29]

**Step 4.** Since EF is parallel to CD, and the straight line GHK falls upon them, the exterior angle GHF is equal to the interior and opposite angle HKD. [1.29]

**Step 5.** It was shown that angle AGH equals angle GHF (Step 3), and that angle GHF equals angle HKD (Step 4). Therefore angle AGH equals angle HKD. [CN1]

**Step 6.** But angles AGH and HKD are alternate angles formed by the straight line GHK falling on lines AB and CD.

**Step 7.** Since the straight line GHK falling on the two straight lines AB and CD makes the alternate angles AGH and HKD equal to one another, AB is parallel to CD. [1.27]

**Step 8.** Therefore straight lines parallel to the same straight line are also parallel to one another. Q.E.D.

**USED:** 1.27, 1.29, CN1
**Human refs (from References field):** 1.29, CN1
**Jaccard:** 0.667 — AI adds ['1.27']

## Proposition 1.31
**Statement:** Through a given point to draw a straight line parallel to a given straight line.

**Step 1.** Let A be the given point and BC the given straight line. It is required to draw through A a straight line parallel to BC.

**Step 2.** Let a point D be taken at random on BC, and let AD be joined. [P1]

**Step 3.** On the straight line DA, at the point A on it, construct the angle DAE equal to the angle ADC on the opposite side of DA from the angle ADC. [1.23]

**Step 4.** Produce the straight line EA in a straight line to F. [P2]

**Step 5.** Since the straight line AD falls on the two straight lines EF and BC, and makes the alternate angles EAD and ADC equal to one another, therefore EF is parallel to BC. [1.27]

**Step 6.** Therefore through the given point A the straight line EAF has been drawn parallel to the given straight line BC, which is what was required to do.

**USED:** 1.23, 1.27, P1, P2
**Human refs (from References field):** 1.23, 1.27
**Jaccard:** 0.500 — AI adds ['P1', 'P2']

## Proposition 1.32
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

**Step 1.** Let ABC be a triangle, and let the side BC be produced to D. I say that the exterior angle ACD is equal to the two interior and opposite angles CAB and ABC, and that the three interior angles of the triangle, namely ABC, BCA, and BAC, are together equal to two right angles.

**Step 2.** Through the point C, draw CE parallel to the straight line BA. [1.31]

**Step 3.** Since AB is parallel to CE, and AC falls upon them as a transversal, the alternate angles BAC and ACE are equal to one another. [1.29]

**Step 4.** Again, since AB is parallel to CE, and the straight line BD falls upon them, the exterior angle ECD is equal to the interior and opposite angle ABC. [1.29]

**Step 5.** But the angle ACE was shown equal to the angle BAC. Therefore the whole angle ACD is equal to the two interior and opposite angles BAC and ABC, since angle ACD is the sum of angles ACE and ECD. [CN2]

**Step 6.** Now add the angle ACB to each side. Then the angles ACD and ACB together are equal to the three angles ABC, BAC, and ACB. [CN2]

**Step 7.** But the angles ACD and ACB are equal to two right angles, since the straight line AC stands on the straight line BD making adjacent angles. [1.13]

**Step 8.** Therefore the three interior angles ABC, BAC, and ACB are also equal to two right angles. [CN1]

**Step 9.** Therefore, in any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles. Q.E.D.

**USED:** 1.13, 1.29, 1.31, CN1, CN2
**Human refs (from References field):** 1.13, 1.29, 1.31
**Jaccard:** 0.600 — AI adds ['CN1', 'CN2']

## Proposition 1.33
**Statement:** The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.

**Step 1.** Let AB and CD be equal and parallel straight lines, and let AC and BD join them at the extremities which are in the same directions respectively. We are to prove that AC and BD are themselves equal and parallel.

**Step 2.** Join BC [P1].

**Step 3.** Since AB is parallel to CD, and the straight line BC falls on them, the alternate angles ABC and BCD are equal to one another [1.29].

**Step 4.** Now in triangles ABC and DCB, we have: AB equals DC (given), BC is common to both triangles, and the contained angle ABC equals the contained angle DCB (Step 3).

**Step 5.** Therefore, by the side-angle-side criterion, triangle ABC is congruent to triangle DCB. In particular, the base AC equals the base BD, and the remaining angles are equal, so angle ACB equals angle DBC [1.4].

**Step 6.** Since the straight line BC falls on the two straight lines AC and BD, and the alternate angles ACB and DBC are equal to one another (Step 5), AC is parallel to BD [1.27].

**Step 7.** Therefore AC and BD have been proved both equal (Step 5) and parallel (Step 6), which is what was to be demonstrated.

**USED:** 1.27, 1.29, 1.4, P1
**Human refs (from References field):** 1.27, 1.29, 1.4
**Jaccard:** 0.750 — AI adds ['P1']

## Proposition 1.34
**Statement:** In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.

**Step 1.** Let ABCD be a parallelogrammic area (parallelogram), so that AB is parallel to CD, and AD is parallel to BC. Let AC be a diameter (diagonal) of the parallelogram, drawn by P1.

**Step 2.** Since AB is parallel to CD, and the straight line AC falls on them, the alternate angles BAC and DCA are equal to one another (1.29).

**Step 3.** Since AD is parallel to BC, and the straight line AC falls on them, the alternate angles DAC and BCA are equal to one another (1.29).

**Step 4.** Now consider triangles ABC and CDA. We have angle BAC equal to angle DCA (Step 2), angle BCA equal to angle DAC (Step 3), and the side AC is common to both triangles.

**Step 5.** Therefore, by 1.26 (ASA congruence), triangle ABC is equal to triangle CDA, and the remaining sides equal the remaining sides respectively: AB equals CD, and BC equals DA. Also the remaining angle ABC equals the remaining angle CDA.

**Step 6.** Since angle BAC equals angle DCA (Step 2) and angle DAC equals angle BCA (Step 3), adding these pairs, angle BAC together with angle DAC equals angle DCA together with angle BCA (CN2). But angle BAC together with angle DAC is the whole angle BAD, and angle DCA together with angle BCA is the whole angle BCD. Therefore angle BAD equals angle BCD.

**Step 7.** Thus the opposite sides of the parallelogram are equal (AB equals CD, and AD equals BC), and the opposite angles are equal (angle ABC equals angle CDA, and angle BAD equals angle BCD).

**Step 8.** Since triangle ABC is equal to triangle CDA (Step 5), the diameter AC bisects the parallelogrammic area ABCD. Q.E.D.

**USED:** 1.26, 1.29, CN2, P1
**Human refs (from References field):** 1.26, 1.29, 1.4, CN2
**Jaccard:** 0.600 — AI adds ['P1']; Human adds ['1.4']

## Proposition 1.35
**Statement:** Parallelograms which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EBCF be two parallelograms on the same base BC and between the same parallels BC and AF, so that A, D, E, F all lie on the line AF.

**Step 2.** Since ABCD is a parallelogram, by 1.34, its opposite sides are equal: AD = BC and AB = DC. Also AB is parallel to DC.

**Step 3.** Since EBCF is a parallelogram, by 1.34, its opposite sides are equal: EF = BC and EB = FC.

**Step 4.** Since AD = BC and EF = BC (Steps 2 and 3), we have AD = EF by CN1.

**Step 5.** Adding DE to both AD and EF, we obtain AE = DF by CN2.

**Step 6.** Since AB is parallel to DC (Step 2) and line AF is a transversal falling on these parallel lines, by 1.29 the alternate interior angles are equal: angle DAB = angle FDC. Since A, E, D are collinear with E between A and D (or D between A and E), the ray from A toward E coincides with the ray from A toward D, so angle EAB = angle DAB. Therefore angle EAB = angle FDC.

**Step 7.** In triangles EAB and FDC, we have EA = FD (Step 5), angle EAB = angle FDC (Step 6), and AB = DC (Step 2). Therefore, by 1.4, triangle EAB is equal to triangle FDC.

**Step 8.** Case 1: Suppose E lies between A and D on line AF. Then parallelogram ABCD is composed of triangle ABE and quadrilateral EBCD, while parallelogram EBCF is composed of triangle DCF and the same quadrilateral EBCD. Since triangle ABE equals triangle DCF (Step 7), adding the common quadrilateral EBCD to each yields parallelogram ABCD equal to parallelogram EBCF, by CN2.

**Step 9.** Case 2: Suppose D lies between A and E on line AF. Then quadrilateral ABCF is composed of parallelogram ABCD together with triangle DCF, and also of parallelogram EBCF together with triangle ABE. Since triangle ABE equals triangle DCF (Step 7), subtracting these equal triangles from the common quadrilateral ABCF yields parallelogram ABCD equal to parallelogram EBCF, by CN3.

**Step 10.** Therefore, in all cases, parallelograms which are on the same base and in the same parallels are equal to one another.

**USED:** 1.29, 1.34, 1.4, CN1, CN2, CN3
**Human refs (from References field):** 1.29, 1.34, 1.4, CN1, CN2, CN3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.36
**Statement:** Parallelograms which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EFGH be parallelograms on equal bases BC and FG respectively, and in the same parallels, so that A, D, E, H lie on one parallel line and B, C, F, G lie on the other.

**Step 2.** Since EFGH is a parallelogram, EH is equal to FG [1.34, opposite sides of a parallelogram are equal].

**Step 3.** But BC is equal to FG [given, equal bases]. Therefore BC is equal to EH [CN1].

**Step 4.** Now BC and EH are also parallel, since they each lie in the two parallel lines (BC on the line through B, C, F, G and EH on the line through A, D, E, H).

**Step 5.** Join BE and CH. Since BC and EH are equal and parallel, the straight lines BE and CH joining their extremities in the same directions are themselves equal and parallel [1.33]. Therefore EBCH is a parallelogram.

**Step 6.** The parallelograms ABCD and EBCH are on the same base BC and in the same parallels (the line through B, C and the line through A, D, E, H). Therefore ABCD is equal to EBCH [1.35].

**Step 7.** The parallelograms EFGH and EBCH are on the same base EH and in the same parallels (the line through E, H and the line through B, C, F, G). Therefore EFGH is equal to EBCH [1.35].

**Step 8.** Since ABCD and EFGH are each equal to EBCH, ABCD is equal to EFGH [CN1].

**Step 9.** Therefore parallelograms which are on equal bases and in the same parallels are equal to one another. Q.E.D.

**USED:** 1.33, 1.34, 1.35, CN1
**Human refs (from References field):** 1.33, 1.34, 1.35, CN1
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.37
**Statement:** Triangles which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let triangles ABC and DBC be on the same base BC and in the same parallels BC and AD. We must show that triangle ABC equals triangle DBC.

**Step 2.** Produce line AD in both directions [P2]. Through B, draw BE parallel to CA [1.31]. Through C, draw CF parallel to BD [1.31].

**Step 3.** Then EBCA is a parallelogram, since BE is parallel to CA and BC joins them, while BA joins the other pair of sides, and EB is parallel to AC by construction. Likewise DBCF is a parallelogram, since BD is parallel to CF by construction.

**Step 4.** Now E, A, D, and F all lie on the line through A and D (or its production). Since BE is parallel to CA and CF is parallel to BD, the figures EBCA and DBCF are both parallelograms on the same base BC and in the same parallels BC and EF.

**Step 5.** Therefore parallelogram EBCA equals parallelogram DBCF [1.35].

**Step 6.** By 1.34, the diagonal BC bisects parallelogram EBCA, so triangle ABC equals triangle BEC. Hence parallelogram EBCA is double triangle ABC.

**Step 7.** By 1.34, the diagonal BC bisects parallelogram DBCF, so triangle DBC equals triangle BFC. Hence parallelogram DBCF is double triangle DBC.

**Step 8.** Since parallelogram EBCA equals parallelogram DBCF [Step 5], and parallelogram EBCA is double triangle ABC [Step 6], and parallelogram DBCF is double triangle DBC [Step 7], triangle ABC equals triangle DBC. For the doubles of triangle ABC and triangle DBC are equal to one another; therefore the halves are themselves equal, since if equals be added to equals the wholes are equal [CN2], and conversely, things that are double the same or equal things are equal [CN3].

**Step 9.** Therefore triangles which are on the same base and in the same parallels are equal to one another. Q.E.D.

**USED:** 1.31, 1.34, 1.35, CN2, CN3, P2
**Human refs (from References field):** 1.31, 1.34, 1.35
**Jaccard:** 0.500 — AI adds ['CN2', 'CN3', 'P2']

## Proposition 1.38
**Statement:** Triangles which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let ABC and DEF be triangles on equal bases BC and EF respectively, and let them lie in the same parallels, so that the line through B, C, E, F is one parallel and the line through A and D is the other.

**Step 2.** Through A, draw AG parallel to CB, and through A draw AH parallel to CD (by extending as needed). More precisely: produce BA to G and draw CG through C parallel to BA [1.31], so that GBCA is a parallelogram. Similarly, produce ED to K and draw FK through F parallel to DE [1.31], so that DEKF is a parallelogram.

**Step 3.** Now GBCA and DEKF are parallelograms on equal bases BC and EF (since BC = EF by hypothesis), and they are in the same parallels BF and GK (the line through G, A, D, K lies along the same parallel to BF since GA is parallel to BC and DK is parallel to EF, and A and D both lie on the parallel to BF). Therefore parallelogram GBCA equals parallelogram DEKF [1.36].

**Step 4.** The diagonal AC of parallelogram GBCA bisects it, so triangle ABC is half of parallelogram GBCA [1.34].

**Step 5.** The diagonal DF of parallelogram DEKF bisects it, so triangle DEF is half of parallelogram DEKF [1.34].

**Step 6.** Since parallelogram GBCA equals parallelogram DEKF (Step 3), and triangle ABC is half of GBCA (Step 4), and triangle DEF is half of DEKF (Step 5), the halves of equal things are equal to one another. Therefore triangle ABC equals triangle DEF.

**Step 7.** Therefore, triangles which are on equal bases and in the same parallels are equal to one another. Q.E.D.

**USED:** 1.31, 1.34, 1.36
**Human refs (from References field):** 1.31, 1.34, 1.36
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.39
**Statement:** Equal triangles which are on the same base and on the same side are also in the same parallels.

**Step 1.** Let ABC and DBC be equal triangles on the same base BC and on the same side of it. I say that they are in the same parallels, that is, that the line AD is parallel to BC.

**Step 2.** Suppose AD is not parallel to BC. Through A, draw the straight line AE parallel to BC, meeting BD (or BD produced) at a point E distinct from D [1.31].

**Step 3.** Join EC [P1].

**Step 4.** Since triangles ABC and EBC are on the same base BC and in the same parallels BC and AE, triangle ABC is equal to triangle EBC [1.37].

**Step 5.** But triangle ABC is equal to triangle DBC (by hypothesis). Therefore triangle EBC is equal to triangle DBC [CN1].

**Step 6.** But this is impossible, for triangle DBC is a part of triangle EBC (since E lies on BD or BD produced, and D is distinct from E), and the whole is greater than the part [CN5].

**Step 7.** Therefore the assumption that AD is not parallel to BC is false. Hence AD is parallel to BC, and the triangles ABC and DBC are in the same parallels, namely BC and AD. Q.E.D.

**USED:** 1.31, 1.37, CN1, CN5, P1
**Human refs (from References field):** 1.31, 1.37, CN1
**Jaccard:** 0.600 — AI adds ['CN5', 'P1']

## Proposition 1.40
**Statement:** Equal triangles which are on equal bases and on the same side are also in the same parallels.

**Step 1.** Let ABC and DEF be equal triangles on equal bases BC and EF respectively, both bases lying on the same straight line BF, and both triangles on the same side of BF. We are to show that AD is parallel to BF, that is, that the triangles are in the same parallels.

**Step 2.** Join AD. Suppose, for the sake of contradiction, that AD is not parallel to BF.

**Step 3.** Through A, draw AG parallel to BF [1.31]. Since AD is not parallel to BF by assumption, but AG is, the point G is distinct from D.

**Step 4.** Join GF. Now consider triangle GEF. It has base EF on the line BF, and its vertex G lies on the line AG, which is parallel to BF.

**Step 5.** Triangle ABC has base BC on the line BF, and its vertex A lies on the line AG (since AG was drawn through A parallel to BF). Thus triangles ABC and GEF are on equal bases BC and EF (given that BC equals EF) and in the same parallels BF and AG.

**Step 6.** By 1.38, triangle ABC equals triangle GEF.

**Step 7.** But triangle ABC equals triangle DEF (given). Therefore, by CN1, triangle GEF equals triangle DEF.

**Step 8.** But G is distinct from D (Step 3), so triangles GEF and DEF are different triangles sharing the same base EF and on the same side of it. One of them is a part of the other or they overlap, so a part would equal the whole. This contradicts CN5, which states that the whole is greater than the part.

**Step 9.** Therefore the assumption that AD is not parallel to BF is false. Hence AD is parallel to BF, and the equal triangles ABC and DEF on equal bases BC and EF and on the same side are in the same parallels. Q.E.F.

**USED:** 1.31, 1.38, CN1, CN5, P1
**Human refs (from References field):** 1.31, 1.38, CN1
**Jaccard:** 0.600 — AI adds ['CN5', 'P1']

## Proposition 1.41
**Statement:** If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.

**Step 1.** Let parallelogram ABCD and triangle EBC share the same base BC and lie between the same parallels BC and AE. We must show that parallelogram ABCD is double triangle EBC.

**Step 2.** Join AC, the diagonal of parallelogram ABCD. [P1]

**Step 3.** Since ABCD is a parallelogram and AC is its diagonal, by 1.34 the diagonal bisects the parallelogram. Therefore triangle ABC is equal to triangle ACD, and each is half of parallelogram ABCD. In particular, parallelogram ABCD is double triangle ABC. [1.34]

**Step 4.** Now triangles ABC and EBC are on the same base BC. Since A lies on line AE (the parallel to BC through A and D) and E also lies on the same line AE, both triangles have their vertices on the line AE, which is parallel to BC. Therefore triangles ABC and EBC are on the same base BC and in the same parallels BC and AE. By 1.37, triangle ABC equals triangle EBC. [1.37]

**Step 5.** Since parallelogram ABCD is double triangle ABC (Step 3), and triangle ABC equals triangle EBC (Step 4), it follows that parallelogram ABCD is double triangle EBC. [CN1]

**Step 6.** Therefore, if a parallelogram has the same base with a triangle and they are in the same parallels, the parallelogram is double the triangle. Q.E.F.

**USED:** 1.34, 1.37, CN1, P1
**Human refs (from References field):** 1.34, 1.37
**Jaccard:** 0.500 — AI adds ['CN1', 'P1']

## Proposition 1.42
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let ABC be the given triangle and D the given rectilineal angle. We are required to construct a parallelogram equal to triangle ABC having one angle equal to angle D.

**Step 2.** Bisect BC at E [1.10], and join AE [P1].

**Step 3.** At point E on the straight line EC, construct angle CEF equal to angle D [1.23].

**Step 4.** Through A, draw a line parallel to EC [1.31]; through C, draw a line parallel to EF [1.31]. Let these two lines meet at G, and let the line through A parallel to EC meet the ray EF at F. Then FECG is a parallelogram, since EF is parallel to CG and FG is parallel to EC, both by construction.

**Step 5.** Since E is the midpoint of BC, we have BE equal to EC. Triangles ABE and AEC share the common vertex A, and their bases BE and EC are equal segments on the same line BC. Therefore triangles ABE and AEC are on equal bases and in the same parallels (namely BC and the line through A parallel to BC). By [1.38], triangle ABE is equal to triangle AEC.

**Step 6.** Since triangle ABC is composed of triangles ABE and AEC, and triangle ABE equals triangle AEC, it follows that triangle ABC is double of triangle AEC [CN2].

**Step 7.** Now, parallelogram FECG and triangle AEC are on the same base EC. Furthermore, they are in the same parallels, since EC is one parallel and FG (the line through A parallel to EC) is the other, and vertex A of triangle AEC lies on line FG. Therefore by [1.41], parallelogram FECG is double of triangle AEC.

**Step 8.** Since parallelogram FECG is double of triangle AEC (Step 7), and triangle ABC is also double of triangle AEC (Step 6), parallelogram FECG is equal to triangle ABC [CN1].

**Step 9.** Moreover, angle FEC was constructed equal to angle D [1.23].

**Step 10.** Therefore the parallelogram FECG has been constructed equal to the given triangle ABC, in the given angle D, which is what was required to do.

**USED:** 1.10, 1.23, 1.31, 1.38, 1.41, CN1, CN2, P1
**Human refs (from References field):** 1.23, 1.31, 1.38, 1.41
**Jaccard:** 0.500 — AI adds ['1.10', 'CN1', 'CN2', 'P1']

## Proposition 1.43
**Statement:** In any parallelogram the complements of the parallelograms about the diameter are equal to one another.

**Step 1.** Let ABCD be a parallelogram with diameter AC. Let K be any point on AC, and through K let lines be drawn parallel to AB and BC, meeting the sides of the parallelogram. This creates parallelograms EKHA and KGCF about the diameter AC, and two complementary parallelograms EBFK and HKGD filling the remainder of ABCD.

**Step 2.** Since ABCD is a parallelogram and AC is its diameter, by 1.34 the diameter bisects the parallelogram, so triangle ABC equals triangle ACD.

**Step 3.** Since AEKH is a parallelogram about the diameter (with AK as a segment of the diameter AC), by 1.34 the diagonal AK bisects it, so triangle AEK equals triangle AHK.

**Step 4.** Similarly, since KGCF is a parallelogram about the diameter (with KC as a segment of the diameter AC), by 1.34 the diagonal KC bisects it, so triangle KFC equals triangle KGC.

**Step 5.** Now, triangle ABC is composed of triangle AEK, triangle KFC, and the complement EBFK. Therefore, triangle ABC equals triangle AEK plus triangle KFC plus complement EBFK.

**Step 6.** Similarly, triangle ACD is composed of triangle AHK, triangle KGC, and the complement HKGD. Therefore, triangle ACD equals triangle AHK plus triangle KGC plus complement HKGD.

**Step 7.** From Step 2, triangle ABC equals triangle ACD. From Steps 3 and 4, triangle AEK equals triangle AHK and triangle KFC equals triangle KGC. Therefore the sum triangle AEK plus triangle KFC equals the sum triangle AHK plus triangle KGC, by CN2.

**Step 8.** Since triangle ABC equals triangle ACD (Step 2), and triangle AEK plus triangle KFC equals triangle AHK plus triangle KGC (Step 7), by subtracting equals from equals (CN3), complement EBFK equals complement HKGD.

**Step 9.** Therefore, in any parallelogram the complements of the parallelograms about the diameter are equal to one another. Q.E.F.

**USED:** 1.34, CN2, CN3
**Human refs (from References field):** 1.34, CN2, CN3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.44
**Statement:** To a given straight line to apply, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let AB be the given straight line, C the given triangle, and D the given rectilineal angle. By 1.42, construct the parallelogram BEFG equal to triangle C, with angle EBG equal to D. Place BEFG so that BE is in a straight line with AB, with B between A and E.

**Step 2.** Produce the side GF of parallelogram BEFG to H, so that H is on the side of A (that is, H is on line GF produced beyond G). Through A draw AH parallel to BG by 1.31. Then AH is also parallel to EF, since in parallelogram BEFG the sides BG and EF are parallel (by 1.34). Since GF is parallel to BE (opposite sides of parallelogram BEFG, by 1.34), and ABE is a straight line, the line HGF is parallel to line ABE.

**Step 3.** Join HB by P1. Since HGF is parallel to ABE, the transversal HB falling on these parallels makes the interior angles BHG and HBE. By 1.29, angle BHG plus angle HBE equals two right angles... but we need to consider HB and FE on the same side. Consider instead the two lines HB and FE, both meeting the parallel lines HGF and ABE. The transversal HGF crosses these lines at H and F. At H, the angle GHB is the angle between HG (going toward F along the upper parallel) and HB (going down toward B). At F, the angle GFE is the angle between FG (going toward H along the upper parallel) and FE (going down toward E). In parallelogram BEFG, angle GFE equals angle GBE (opposite angles are equal by 1.34), so angle GFE equals D. Now in parallelogram AHGB (which is a parallelogram since AH is parallel to BG and HG is parallel to AB), the diagonal HB lies strictly between sides HA and HG, so angle GHB is strictly less than angle GHA. Since AHGB is a parallelogram, angle GHA equals angle ABG (opposite angles, by 1.34), and angle ABG equals pi minus D (since angle ABG is supplementary to angle EBG on the straight line AE). Therefore angle GHB is strictly less than pi minus D. Thus angle GHB plus angle GFE is strictly less than (pi minus D) plus D, which equals two right angles. By Postulate 5, the lines HB and FE, when produced on the side of B and E, will meet. Call their meeting point K.

**Step 4.** Through K draw KL parallel to AE by 1.31. Produce the line HA beyond A until it meets KL; call this meeting point L. Produce the line FE beyond E (through K, which is already on this line). Now FHLK is a parallelogram: FH is parallel to LK since FH lies along line HGF which is parallel to ABE, and KL is parallel to AE (which lies on ABE), so FH is parallel to KL. Also HL is parallel to FK since HL lies along the line HAL and FK lies along the line FEK, and AH is parallel to EF (established in Step 2), so their extensions HL and FK are parallel. Therefore FHLK is a parallelogram.

**Step 5.** Now HK is a diagonal of parallelogram FHLK, and B lies on HK (since H, B, K are collinear by construction: K lies on HB produced). Through B, draw lines parallel to each pair of opposite sides of FHLK. The line through B parallel to FH (that is, parallel to HGF) is the line ABE, which meets side HL at A and side FK at E. The line through B parallel to HL (that is, parallel to AH, which is parallel to BG) is the line GBM, where G is on side FH and M is the point where BG produced meets side LK. These two lines through B, both passing through the point B on diagonal HK, divide parallelogram FHLK into four parallelograms. The two parallelograms about the diameter HK are HABG (containing vertex H of the diagonal) and BMKE (containing vertex K of the diagonal). The two complements are GFEB and ALMB.

**Step 6.** By 1.43, the complements of the parallelograms about the diameter are equal. Therefore parallelogram GFEB equals parallelogram ALMB. But GFEB is the same as parallelogram BEFG, which was constructed equal to triangle C. Therefore parallelogram ALMB equals triangle C (by CN1).

**Step 7.** The parallelogram ALMB has AB as one of its sides. It remains to show that the angle of ALMB at B equals angle D. Since A, B, E are collinear and G, B, M are collinear (B being the intersection of these two lines), the angles EBG and ABM are vertical angles. By 1.15, angle ABM equals angle EBG. But angle EBG equals D by construction. Therefore angle ABM equals D.

**Step 8.** Therefore ALMB is a parallelogram applied to the given straight line AB, in the given angle D, equal to the given triangle C. This is what was required to be done.

**USED:** 1.15, 1.29, 1.31, 1.34, 1.42, 1.43, CN1, P1, P2, P5
**Human refs (from References field):** 1.15, 1.29, 1.31, 1.42, 1.43, CN1, P5
**Jaccard:** 0.700 — AI adds ['1.34', 'P1', 'P2']

## Proposition 1.45
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.

**Step 1.** Let ABCDE be the given rectilineal figure (illustrated as a polygon; the argument works for any number of sides) and let angle F be the given rectilineal angle. We must construct a parallelogram equal to ABCDE in angle F.

**Step 2.** Draw diagonals AC and AD from vertex A, dividing the figure ABCDE into triangles: triangle ABC, triangle ACD, and triangle ADE [P1].

**Step 3.** By Proposition 1.42, construct parallelogram GHKL equal to triangle ABC in the given angle F, so that GH is one of its sides. Then parallelogram GHKL equals triangle ABC [1.42].

**Step 4.** By Proposition 1.44, to the straight line HK, in the angle GHM which equals angle F, apply the parallelogram HKMN equal to triangle ACD. Since the angle at H in both parallelograms equals angle F, and GH and HN lie along the same direction, the side GH is in a straight line with HN [1.14, 1.29]. Likewise KL is in a straight line with KM, since KL is parallel to GH, and KM is parallel to HN, and GH is in a straight line with HN, so KL is in a straight line with KM [1.30, 1.14, 1.29].

**Step 5.** By Proposition 1.44 again, to the straight line KM (which is in a straight line with KL), in the angle MKP which equals angle F, apply the parallelogram KMPO equal to triangle ADE. By the same reasoning as in Step 4, HN is in a straight line with NO, and LM is in a straight line with MP [1.44, 1.14, 1.29, 1.30].

**Step 6.** Now GLPO is a parallelogram: GL and OP are parallel (since GL lies along the line through KL-KM-MP extended, and OP lies along the opposite side), and GP and LO are parallel (since they connect corresponding endpoints of parallel sides). Moreover, angle GLP equals angle F, since angle GLK equals angle F from the original construction, and KL-KM-MP form a single straight line, giving angle GLP equal to angle F [1.34, 1.29, 1.30].

**Step 7.** Now parallelogram GHKL equals triangle ABC [Step 3], parallelogram HKMN equals triangle ACD [Step 4], and parallelogram KMPO equals triangle ADE [Step 5].

**Step 8.** Therefore the whole parallelogram GLPO equals triangle ABC together with triangle ACD together with triangle ADE [CN2].

**Step 9.** But triangle ABC together with triangle ACD together with triangle ADE equals the rectilineal figure ABCDE, since these triangles exactly compose it [CN2].

**Step 10.** Therefore parallelogram GLPO equals the rectilineal figure ABCDE, and it has been constructed in the given angle F [CN1].

**Step 11.** Hence, in the given rectilineal angle, a parallelogram has been constructed equal to the given rectilineal figure, which is what was required to do. Q.E.F.

**USED:** 1.14, 1.29, 1.30, 1.34, 1.42, 1.44, CN1, CN2, P1
**Human refs (from References field):** 1.14, 1.29, 1.30, 1.33, 1.34, 1.42, 1.44, CN1, CN2
**Jaccard:** 0.800 — AI adds ['P1']; Human adds ['1.33']

## Proposition 1.46
**Statement:** On a given straight line to describe a square.

**Step 1.** Let AB be the given straight line. It is required to describe a square on AB.

**Step 2.** From the point A, draw AC at right angles to AB [1.11]. Cut off AD equal to AB from AC [1.3].

**Step 3.** Through D, draw DE parallel to AB [1.31]. Through B, draw BE parallel to AD [1.31]. Let E be the point at which DE and BE meet. Then ADEB is a parallelogram, since both pairs of opposite sides are parallel by construction.

**Step 4.** Since ADEB is a parallelogram, its opposite sides are equal [1.34]. Therefore AB = DE and AD = BE.

**Step 5.** But AD was made equal to AB [Step 2]. Therefore AB = AD = DE = BE [CN1]. Thus the parallelogram ADEB is equilateral.

**Step 6.** Now, since AD is parallel to BE and AB falls upon them, the interior angles DAB and ABE on the same side are together equal to two right angles [1.29].

**Step 7.** But angle DAB is a right angle, since AC was drawn at right angles to AB at A [Step 2, 1.11]. Therefore angle ABE is also a right angle [CN3, subtracting angle DAB from two right angles on each side].

**Step 8.** Since ADEB is a parallelogram, the opposite angles are equal [1.34]. Therefore angle ADE equals angle ABE, and angle DAB equals angle DEB.

**Step 9.** Since angle DAB is a right angle and angle DEB equals angle DAB, angle DEB is also a right angle. Since angle ABE is a right angle and angle ADE equals angle ABE, angle ADE is also a right angle.

**Step 10.** Therefore all four angles of ADEB are right angles. Combined with the equilateral property established in Step 5, ADEB is both equilateral and right-angled. By definition [D1.22], ADEB is a square.

**Step 11.** Therefore on the given straight line AB, a square ADEB has been described, which is what was required to do.

**USED:** 1.11, 1.29, 1.3, 1.31, 1.34, CN1, CN3, D1.22
**Human refs (from References field):** 1.11, 1.29, 1.31, 1.34
**Jaccard:** 0.500 — AI adds ['1.3', 'CN1', 'CN3', 'D1.22']

## Proposition 1.47
**Statement:** In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.

**Step 1.** Let ABC be a right-angled triangle having the right angle BAC. We are to show that the square on BC is equal to the sum of the squares on BA and AC.

**Step 2.** On BC, CA, and AB, describe squares BDEC, CKHA, and BAGF respectively [1.46].

**Step 3.** Through A, draw AL parallel to BD (or CE), and join AD and FC [P1, 1.31].

**Step 4.** Since angle BAC is a right angle (given) and angle BAG is also a right angle (being an angle of square BAGF), the two straight lines CA and AG, not lying on the same side of line BA, make the adjacent angles with BA equal to two right angles. Therefore CA is in a straight line with AG [1.14].

**Step 5.** By the same reasoning, since angle BAC is a right angle and angle CAH is a right angle (being an angle of square CKHA), BA is in a straight line with AH [1.14].

**Step 6.** Now, since angle DBC is a right angle (angle of square BDEC) and angle FBA is a right angle (angle of square BAGF), we have angle DBC equal to angle FBA [P4]. Adding angle ABC to each, angle DBA equals angle FBC [CN2].

**Step 7.** In triangles ABD and FBC: AB equals FB (sides of square BAGF), BD equals BC (sides of square BDEC), and angle ABD equals angle FBC (Step 6). Therefore triangle ABD is equal to triangle FBC [1.4].

**Step 8.** Now, the parallelogram BL (that is, rectangle BDLA) is double the triangle ABD, since they are on the same base BD and in the same parallels BD and AL [1.41].

**Step 9.** The square BAGF is double the triangle FBC, since they are on the same base FB and in the same parallels FB and GC. For since angle BAC is a right angle and BA is in a straight line with AH (Step 5), and since FB is parallel to GC (being opposite sides of square BAGF extended through the collinearity of C, A, H), the triangle FBC and the square BAGF share the base FB and lie in the same parallels [1.41].

**Step 10.** Since the parallelogram BL is double of triangle ABD and the square BAGF is double of triangle FBC, and triangle ABD equals triangle FBC (Step 7), the parallelogram BL equals the square BAGF [CN1].

**Step 11.** Next, join AE and BK [P1].

**Step 12.** Since angle ACE is a right angle (angle of square BDEC) and angle ACK is a right angle (angle of square CKHA), we have angle ACE equal to angle ACK [P4]. Adding angle ACB to each, angle BCE equals angle ACK (that is, angle BCK) [CN2].

**Step 13.** In triangles BCE and ACK: BC equals CE (sides of square BDEC), AC equals CK (sides of square CKHA), and angle BCE equals angle ACK (Step 12). Therefore triangle BCE is equal to triangle ACK [1.4].

**Step 14.** The parallelogram CL (that is, rectangle CELQ where Q is the intersection point on DE) is double the triangle BCE, since they are on the same base CE and in the same parallels CE and AL [1.41].

**Step 15.** The square CKHA is double the triangle ACK, since they are on the same base CK and in the same parallels CK and AH. For BA is in a straight line with AH (Step 5), so the parallels are CK and BH [1.41].

**Step 16.** Since the parallelogram CL is double of triangle BCE and the square CKHA is double of triangle ACK, and triangle BCE equals triangle ACK (Step 13), the parallelogram CL equals the square CKHA [CN1].

**Step 17.** The whole square BDEC is composed of the parallelograms BL and CL. Since BL equals the square BAGF (Step 10) and CL equals the square CKHA (Step 16), the square BDEC equals the sum of the squares BAGF and CKHA [CN2].

**Step 18.** Therefore, in the right-angled triangle ABC, the square on the side BC subtending the right angle is equal to the squares on the sides BA and AC containing the right angle. Q.E.D.

**USED:** 1.14, 1.31, 1.4, 1.41, 1.46, CN1, CN2, P1, P4
**Human refs (from References field):** 1.14, 1.4, 1.41, 1.46, CN2
**Jaccard:** 0.556 — AI adds ['1.31', 'CN1', 'P1', 'P4']

## Proposition 1.48
**Statement:** If in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right.

**Step 1.** Let ABC be a triangle in which the square on BC is equal to the squares on BA and AC together. I say that the angle BAC is right.

**Step 2.** From the point A, draw AD at right angles to AC [1.11], and make AD equal to AB [1.3].

**Step 3.** Join DC [P1].

**Step 4.** Since AD equals AB, the square on AD equals the square on AB. Adding the square on AC to each, the square on AD together with the square on AC equals the square on AB together with the square on AC [CN2].

**Step 5.** Now the angle DAC is right by construction. Therefore by the Pythagorean theorem, the square on DC is equal to the squares on DA and AC [1.47]. And by hypothesis, the square on BC is equal to the squares on BA and AC.

**Step 6.** Therefore the square on DC is equal to the square on BC [CN1]. Hence DC equals BC.

**Step 7.** Now in triangles DAC and BAC, we have DA equal to AB (by construction [1.3]), AC is common, and DC has been proved equal to BC. Therefore by the side-side-side congruence criterion, angle DAC equals angle BAC [1.8].

**Step 8.** But angle DAC is a right angle by construction [D1.10]. Therefore angle BAC is also a right angle.

**Step 9.** Therefore, if in a triangle the square on one of the sides is equal to the squares on the remaining two sides, the angle contained by those two sides is right. Q.E.D.

**USED:** 1.11, 1.3, 1.47, 1.8, CN1, CN2, D1.10, P1
**Human refs (from References field):** 1.47, 1.8
**Jaccard:** 0.250 — AI adds ['1.11', '1.3', 'CN1', 'CN2', 'D1.10', 'P1']
