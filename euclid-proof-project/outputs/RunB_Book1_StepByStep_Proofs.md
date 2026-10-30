# Book 1 of Euclid's Elements — Step-by-Step AI Proofs (Run B)

## Proposition 1.1
**Statement:** On a given finite straight line to construct an equilateral triangle.

**Step 1.** Let AB be the given finite straight line. It is required to construct an equilateral triangle on the straight line AB.

**Step 2.** With centre A and distance AB let the circle BCD be described [P3].

**Step 3.** Again, with centre B and distance BA let the circle ACE be described [P3].

**Step 4.** From the point C, in which the two circles cut one another, draw the straight lines CA and CB to the points A and B [P1].

**Step 5.** Now, since the point A is the centre of the circle CDB, the straight line AC is equal to the straight line AB, both being radii of that circle [D1.15].

**Step 6.** Again, since the point B is the centre of the circle CAE, the straight line BC is equal to the straight line BA, both being radii of that circle [D1.15].

**Step 7.** But CA was also shown equal to AB; therefore each of the straight lines CA and CB is equal to AB.

**Step 8.** And things which are equal to the same thing are also equal to one another; therefore CA is also equal to CB [CN1].

**Step 9.** Therefore the three straight lines CA, AB, and BC are equal to one another, so that the triangle ABC has its three sides equal; hence it is equilateral [D1.20], and it has been constructed on the given finite straight line AB.

**USED:** CN1, D1.15, D1.20, P1, P3
**Human refs (from References field):** CN1, D1.15, P1, P3
**Jaccard:** 0.800 — AI adds ['D1.20']

## Proposition 1.2
**Statement:** To place at a given point (as an extremity) a straight line equal to a given straight line.

**Step 1.** Let A be the given point, and BC the given straight line. It is required to place at the point A a straight line equal to BC.

**Step 2.** From the point A to the point B draw the straight line AB [P1].

**Step 3.** On AB construct the equilateral triangle DAB, so that DA = DB = AB [1.1].

**Step 4.** Produce the straight lines DA and DB in straight lines to E and F respectively [P2].

**Step 5.** With centre B and distance BC describe the circle CGH, and let it cut DF (the production of DB) at the point G [P3].

**Step 6.** With centre D and distance DG describe the circle GKL, and let it cut DE (the production of DA) at the point L [P3].

**Step 7.** Since the point B is the centre of the circle CGH, and BC and BG are straight lines from the centre B to the circumference, BC is equal to BG [D1.15].

**Step 8.** Since the point D is the centre of the circle GKL, and DL and DG are straight lines from the centre D to the circumference, DL is equal to DG [D1.15].

**Step 9.** But DA is equal to DB, since DAB is an equilateral triangle [from Step 3].

**Step 10.** Therefore the remainder AL is equal to the remainder BG, for equals (DA, DB) have been subtracted from equals (DL, DG) [CN3].

**Step 11.** But BG was shown to be equal to BC. Therefore AL and BC are each equal to BG, and so AL is equal to BC [CN1].

**Step 12.** Therefore at the given point A the straight line AL has been placed equal to the given straight line BC. Q.E.F.

**USED:** 1.1, CN1, CN3, D1.15, P1, P2, P3
**Human refs (from References field):** 1.1, CN1, CN3, P1, P2, P3
**Jaccard:** 0.857 — AI adds ['D1.15']

## Proposition 1.3
**Statement:** Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

**Step 1.** Let AB and C be the two given unequal straight lines, of which AB is the greater. It is required to cut off from AB the greater a straight line equal to C the less.

**Step 2.** At the point A let there be placed a straight line AD equal to the given straight line C [1.2].

**Step 3.** With centre A and distance AD let the circle DEF be described [P3].

**Step 4.** Since the point A is the centre of the circle DEF, the straight line AE is equal to the straight line AD, both being radii drawn from the centre to the circumference [D1.15].

**Step 5.** But C is also equal to AD, by the construction in Step 2.

**Step 6.** Therefore each of the straight lines AE and C is equal to AD; hence AE is also equal to C [CN1].

**Step 7.** Therefore, given the two unequal straight lines AB and C, from AB the greater there has been cut off AE equal to C the less. Q.E.F.

**USED:** 1.2, CN1, D1.15, P3
**Human refs (from References field):** 1.2, CN1, D1.15, P3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.4
**Statement:** If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base, the triangle will be equal to the triangle, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend.

**Step 1.** Let ABC and DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively, namely AB to DE and AC to DF, and the angle BAC equal to the angle EDF. I say that the base BC is equal to the base EF, the triangle ABC is equal to the triangle DEF, and the remaining angles are equal to the remaining angles respectively, namely angle ABC to angle DEF and angle ACB to angle DFE.

**Step 2.** Apply the triangle ABC to the triangle DEF, placing the point A on the point D and the straight line AB on the straight line DE. Then the point B coincides with the point E, because AB is equal to DE.

**Step 3.** AB coinciding with DE, the straight line AC also coincides with DF, because the angle BAC is equal to the angle EDF; hence the point C also coincides with the point F, because AC is again equal to DF.

**Step 4.** But B coincided with E (Step 2); therefore the base BC coincides with the base EF. For if, while B coincides with E and C with F, the base BC does not coincide with the base EF, then two straight lines would enclose a space, which is impossible (the two points B and C are joined by the single straight line BC, by the nature of a straight line as that which lies evenly with the points on itself, D1.4). Therefore the base BC coincides with EF and is equal to it (CN4).

**Step 5.** Thus the whole triangle ABC coincides with the whole triangle DEF and is equal to it (CN4).

**Step 6.** And the remaining angles coincide with the remaining angles and are equal to them (CN4), namely the angle ABC to the angle DEF, and the angle ACB to the angle DFE.

**Step 7.** Therefore the base BC is equal to the base EF, the triangle ABC is equal to the triangle DEF, and the remaining angles are equal to the remaining angles respectively. Q.E.D.

**USED:** CN4, D1.4
**Human refs (from References field):** CN4
**Jaccard:** 0.500 — AI adds ['D1.4']

## Proposition 1.5
**Statement:** In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

**Step 1.** Let ABC be an isosceles triangle having the side AB equal to the side AC; and let the straight lines BD, CE be produced further in a straight line with AB, AC (P2). I say that the angle ABC is equal to the angle ACB, and the angle CBD is equal to the angle BCE.

**Step 2.** Take an arbitrary point F on BD. Since AE is greater than AF, cut off from AE the greater the straight line AG equal to AF the less (1.3).

**Step 3.** Join FC and GB (P1).

**Step 4.** Now consider the triangles AFC and AGB. We have AF equal to AG (by construction, Step 2) and AC equal to AB (by hypothesis). Thus the two sides FA, AC are equal to the two sides GA, AB respectively; and they contain a common angle, the angle FAG. Therefore, by the congruence of triangles, the base FC is equal to the base GB, the triangle AFC is equal to the triangle AGB, and the remaining angles are equal to the remaining angles respectively, namely those which the equal sides subtend; that is, the angle ACF is equal to the angle ABG, and the angle AFC is equal to the angle AGB (1.4).

**Step 5.** And, since the whole AF is equal to the whole AG, and in these AB is equal to AC, the remainder BF is equal to the remainder CG (CN3).

**Step 6.** But FC was also proved equal to GB (Step 4). Therefore the two sides BF, FC are equal to the two sides CG, GB respectively; and the angle BFC is equal to the angle CGB (the angle AFC equal to the angle AGB, Step 4), while the base BC is common to them. Therefore the triangle BFC is also equal to the triangle CGB, and the remaining angles are equal to the remaining angles respectively, namely those which the equal sides subtend; therefore the angle FBC is equal to the angle GCB, and the angle BCF is equal to the angle CBG (1.4).

**Step 7.** Accordingly, since the whole angle ABG was proved equal to the whole angle ACF, and in these the angle CBG is equal to the angle BCF, the remaining angle ABC is equal to the remaining angle ACB (CN3); and they are at the base of the triangle ABC.

**Step 8.** But the angle FBC was also proved equal to the angle GCB (Step 6); and these are under the base. Therefore in isosceles triangles the angles at the base are equal to one another, and, the equal straight lines being produced further, the angles under the base are equal to one another. Q.E.D.

**USED:** 1.3, 1.4, CN3, P1, P2
**Human refs (from References field):** 1.3, 1.4, P1, P2
**Jaccard:** 0.800 — AI adds ['CN3']

## Proposition 1.6
**Statement:** If in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another.

**Step 1.** Let ABC be a triangle having the angle ABC equal to the angle ACB. I say that the side AB is also equal to the side AC.

**Step 2.** For, if AB is unequal to AC, one of them is greater. Let AB be the greater; then, since AB is greater than AC, we can cut off from AB the greater a straight line DB equal to AC the less [1.3].

**Step 3.** Let DC be joined, the straight line from D to C [P1].

**Step 4.** Now consider the two triangles DBC and ACB. Since DB is equal to AC (by the construction in Step 2) and BC is common to both, the two sides DB, BC are equal to the two sides AC, CB respectively.

**Step 5.** And the angle DBC is equal to the angle ACB; for the angle DBC is the same as the angle ABC, which was assumed equal to the angle ACB.

**Step 6.** Therefore, since the two sides DB, BC are equal to the two sides AC, CB respectively, and the angle DBC contained by the equal straight lines is equal to the angle ACB likewise contained by them, the base DC is equal to the base AB, and the triangle DBC is equal to the triangle ACB [1.4].

**Step 7.** Thus the triangle DBC, which is a part of the triangle ACB, is equal to the triangle ACB, the whole. But this is impossible, since the whole is greater than the part [CN5].

**Step 8.** Therefore AB is not unequal to AC; it is therefore equal to it. Hence in the triangle ABC, the sides AB and AC which subtend the equal angles ABC and ACB are equal to one another. Q.E.D.

**USED:** 1.3, 1.4, CN5, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.3', '1.4', 'CN5', 'P1']

## Proposition 1.7
**Statement:** Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities), and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively, namely each to that which has the same extremity with it.

**Step 1.** Let AB be the given straight line, and suppose, on the same side of AB, two pairs of straight lines are constructed from the extremities A and B meeting in points. From A and B let AC, CB be drawn meeting at C, with AC having extremity A and CB having extremity B. Suppose, contrary to the proposition, that there can also be constructed two other straight lines AD, DB meeting at a different point D on the same side of AB, such that AD is equal to AC (the lines sharing extremity A) and DB is equal to CB (the lines sharing extremity B).

**Step 2.** Since D is a point distinct from C lying on the same side of AB as C, the point D either lies inside the triangle ACB, or outside it, or upon one of its sides AC or CB. (Consider first the principal case in which D falls outside the triangle ACB.) Join CD by a straight line (P1).

**Step 3.** Since AC is equal to AD (by hypothesis), the triangle ACD is isosceles; therefore by 1.5 the angles at the base CD are equal to one another, that is, the angle ACD is equal to the angle ADC.

**Step 4.** Now the angle ACD is greater than the angle BCD, because the whole is greater than the part (CN5): the straight line CB lies, in this configuration, within the angle ACD, so the angle BCD is a part of the angle ACD. Therefore the angle ADC is much greater than the angle BCD; that is, the angle ADC is greater than the angle BCD.

**Step 5.** Again, since CB is equal to DB (by hypothesis), the triangle BCD is isosceles; therefore by 1.5 the angles at the base CD are equal to one another, that is, the angle BCD is equal to the angle BDC.

**Step 6.** But it was shown that the angle ADC is greater than the angle BCD. Since the angle BDC is equal to the angle BCD, the angle ADC is greater than the angle BDC.

**Step 7.** Yet the angle ADC is also a part of the angle BDC: for in this configuration the straight line DC falls within the angle BDA, so that the angle ADC is less than the angle BDC by CN5 (the whole BDC being greater than its part ADC). Thus the angle ADC is at once greater than and less than the angle BDC, which is impossible.

**Step 8.** Therefore the assumption that D falls outside the triangle leads to a contradiction. The remaining case, in which D falls within the triangle ACB, is treated in the same manner: producing AC to E through C and AD to F through D (P2), and applying 1.5 to the isosceles triangles ACD and BCD on the bases below the produced lines, we obtain that the exterior angle ECD equals the angle FDC, while CN5 again forces these equal angles into the relation greater-than-less-than, a contradiction. (The case where D lies on a side of the triangle is excluded immediately, since then AD and AC, sharing extremity A and being equal, would terminate at the same point, making D coincide with C.)

**Step 9.** In every case the supposition that a second point D exists, distinct from C and on the same side of AB, with AD equal to AC and DB equal to CB, is impossible. Therefore there cannot be constructed on the same straight line, from its extremities and on the same side, two other straight lines meeting in another point and equal to the former two respectively, each to that which has the same extremity with it. Q.E.D.

**USED:** 1.5, CN5, P1, P2
**Human refs (from References field):** 1.5
**Jaccard:** 0.250 — AI adds ['CN5', 'P1', 'P2']

## Proposition 1.8
**Statement:** If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines.

**Step 1.** Let ABC and DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively, namely AB to DE and AC to DF; and let them have the base BC equal to the base EF. I say that the angle BAC is equal to the angle EDF.

**Step 2.** Apply the triangle ABC to the triangle DEF, placing the point B on the point E and the straight line BC on the straight line EF. Then the point C also coincides with the point F, because BC is equal to EF (given), and these are placed coincident from the start; so the base BC coincides with and is equal to the base EF (CN4).

**Step 3.** Thus, with BC applied along EF, the side BA falls along some straight line from E, and the side CA falls along some straight line from F. Suppose, for contradiction, that while the bases BC, EF coincide, the sides BA, CA do not coincide with the sides ED, FD but fall in a different position, so that the apex A falls at a point G distinct from D. Then on the straight line EF, from its extremities E and F and on the same side of it, there would be constructed two pairs of straight lines: namely ED, FD meeting at D, and EG (the image of BA), FG (the image of CA) meeting at G.

**Step 4.** But EG equals ED and FG equals FD, since EG is the image of BA, which equals DE, and FG is the image of CA, which equals DF, and equals of the same things are equal (the transferred lines BA, CA retain their lengths AB = DE and AC = DF). Hence on the same straight line EF, from its extremities and on the same side, two straight lines EG, FG meeting at G would be respectively equal to two straight lines ED, FD meeting at another point D, each to that which has the same extremity with it. This is impossible (1.7).

**Step 5.** Therefore it is not possible that the apex A falls at a point distinct from D. Consequently, when the base BC is applied to the base EF, the sides BA, AC necessarily coincide with the sides ED, DF.

**Step 6.** Since BA coincides with ED and AC coincides with DF, the angle BAC coincides with the angle EDF, and therefore is equal to it (CN4).

**Step 7.** Therefore, if two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines, namely the angle BAC equal to the angle EDF. Q.E.D.

**USED:** 1.7, CN4
**Human refs (from References field):** 1.7
**Jaccard:** 0.500 — AI adds ['CN4']

## Proposition 1.9
**Statement:** To bisect a given rectilineal angle.

**Step 1.** Let the angle BAC be the given rectilineal angle; it is required to bisect it.

**Step 2.** Take any point D at random on the straight line AB.

**Step 3.** Since AC is greater than or equal to AD (or by the same construction applied to the lesser), cut off from AC the straight line AE equal to AD [1.3], so that AD = AE.

**Step 4.** Join DE [P1].

**Step 5.** On the straight line DE construct the equilateral triangle DEF [1.1], so that DF = EF and DE = EF = FD.

**Step 6.** Join AF [P1]. I say that the straight line AF bisects the angle BAC.

**Step 7.** Now consider the two triangles ADF and AEF. AD = AE [Step 3], and AF is common to both triangles; therefore the two sides AD, AF are equal to the two sides AE, AF respectively.

**Step 8.** Also DF = EF, since the triangle DEF is equilateral [1.1, D1.20]; thus the base DF is equal to the base EF.

**Step 9.** Therefore, the two triangles ADF and AEF have the two sides equal to the two sides respectively and the base equal to the base; hence the angle DAF is equal to the angle EAF [1.8].

**Step 10.** Therefore the straight line AF bisects the given rectilineal angle BAC. Q.E.F.

**USED:** 1.1, 1.3, 1.8, D1.20, P1
**Human refs (from References field):** 1.3, 1.8
**Jaccard:** 0.400 — AI adds ['1.1', 'D1.20', 'P1']

## Proposition 1.10
**Statement:** To bisect a given finite straight line.

**Step 1.** Let AB be the given finite straight line; it is required to bisect it.

**Step 2.** On the straight line AB construct an equilateral triangle ABC (1.1), so that the three sides AC, CB, AB are equal to one another.

**Step 3.** Since triangle ABC is equilateral, its sides CA and CB are equal to one another (by D1.20, an equilateral triangle is that which has its three sides equal).

**Step 4.** Bisect the angle ACB by the straight line CD, letting CD meet AB at the point D (1.9). Then the angle ACD is equal to the angle BCD.

**Step 5.** Now in the two triangles ACD and BCD: the side CA is equal to the side CB (Step 3), the side CD is common to both triangles, and these two sides contain equal angles, namely the angle ACD equal to the angle BCD (Step 4).

**Step 6.** Therefore, since two sides of triangle ACD are equal to two sides of triangle BCD respectively, and the angles contained by the equal sides are equal, the base AD is equal to the base BD (1.4).

**Step 7.** Therefore the given finite straight line AB has been bisected at the point D, since AD is equal to DB (CN1). Q.E.F.

**USED:** 1.1, 1.4, 1.9, CN1, D1.20
**Human refs (from References field):** 1.1, 1.4, 1.9
**Jaccard:** 0.600 — AI adds ['CN1', 'D1.20']

## Proposition 1.11
**Statement:** To draw a straight line at right angles to a given straight line from a given point on it.

**Step 1.** Let AB be the given straight line, and C the given point on it. It is required to draw from the point C a straight line at right angles to AB.

**Step 2.** Take a point D taken at random on CA (between C and A). Then on CB, cut off CE equal to CD [1.3], so that the two segments CD and CE on opposite sides of C along the line AB are equal to one another.

**Step 3.** On the straight line DE construct the equilateral triangle FDE [1.1], so that FD, DE, and EF are all equal to one another.

**Step 4.** Join FC [P1].

**Step 5.** I say that the straight line FC has been drawn at right angles to the given straight line AB. For consider the two triangles FDC and FEC. Since DC equals CE (Step 2), and CF is common to both triangles, the two sides DC, CF are equal to the two sides EC, CF respectively; and the base FD equals the base FE (Step 3, as sides of the equilateral triangle). Therefore the angle DCF equals the angle ECF [1.8].

**Step 6.** Now the angles DCF and ECF are adjacent angles, made by the straight line FC standing on the straight line AB (since D lies on CA and E lies on CB, so that DCE forms the line AB). And when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is called a perpendicular to it [D1.10]. Therefore each of the angles DCF and ECF is right, and FC is at right angles to AB.

**Step 7.** Therefore the straight line FC has been drawn at right angles to the given straight line AB from the given point C on it. Q.E.F.

**USED:** 1.1, 1.3, 1.8, D1.10, P1
**Human refs (from References field):** 1.1, 1.3, 1.8, D1.10
**Jaccard:** 0.800 — AI adds ['P1']

## Proposition 1.12
**Statement:** To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

**Step 1.** Let AB be the given infinite straight line, and C the given point which is not on it. It is required to draw from C a straight line perpendicular to AB.

**Step 2.** Take any point D on the other side of the straight line AB (that is, on the side opposite to C). With centre C and distance CD, describe a circle EFG [P3]. Since C lies on one side of AB and D on the other side, the line AB lies between them, and the circle, passing through D, will cut the straight line AB in two points; let it cut AB at G and H.

**Step 3.** Bisect GH at the point E [1.10], and join the straight lines CG, CE, CH [P1].

**Step 4.** Now compare the triangles CGE and CHE. Since E is the midpoint of GH, GE is equal to EH. The side CE is common to both triangles. And the base CG is equal to the base CH, since G and H both lie on the circle of which C is the centre, so CG and CH are radii of one and the same circle [D1.15].

**Step 5.** Therefore in the two triangles CGE and CHE, the two sides GE, EC are equal to the two sides HE, EC respectively, and the base CG is equal to the base CH. Hence the angle CEG is equal to the angle CEH [1.8].

**Step 6.** But CEG and CEH are adjacent angles, and a straight line CE set up on the straight line GH (a part of AB) has been shown to make the adjacent angles equal to one another. When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the line standing on the other is called a perpendicular to it [D1.10].

**Step 7.** Therefore CE has been drawn perpendicular to the given infinite straight line AB from the given point C which is not on it. Q.E.F.

**USED:** 1.10, 1.8, D1.10, D1.15, P1, P3
**Human refs (from References field):** 1.10, 1.8, D1.10, P1, P3
**Jaccard:** 0.833 — AI adds ['D1.15']

## Proposition 1.13
**Statement:** If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

**Step 1.** Let the straight line AB be set up on the straight line CD, making the angles CBA and ABD. I say that the angles CBA, ABD are either two right angles or equal to two right angles.

**Step 2.** First, if the angle CBA is equal to the angle ABD, then, since AB standing on CD makes the adjacent angles CBA, ABD equal to one another, each of them is by definition right [D1.10]. In this case the two angles CBA, ABD are two right angles, and the proposition holds.

**Step 3.** But if the angle CBA is not equal to the angle ABD, draw from the point B the straight line BE at right angles to CD [1.11]. Then the angles CBE and EBD are each right angles, by the construction.

**Step 4.** Now the angle CBE is composed of the two angles CBA and ABE; for BA lies between BC and BE. Therefore, adding the angle EBD to each, the angle CBE together with the angle EBD equals the three angles CBA, ABE, EBD [CN2].

**Step 5.** Again, the angle DBA is composed of the two angles DBE and EBA; for BE lies between BD and BA. Therefore, adding the angle ABC to each, the angle DBA together with the angle ABC equals the three angles DBE, EBA, ABC [CN2].

**Step 6.** But the two angles CBE, EBD were also shown to equal the same three angles CBA, ABE, EBD. Now things which are equal to the same thing are also equal to one another [CN1]; therefore the angles CBE, EBD together are equal to the angles DBA, ABC together.

**Step 7.** But the angles CBE, EBD are two right angles [D1.10, by the construction of BE]. Therefore the angles DBA, ABC are also equal to two right angles [CN1].

**Step 8.** Therefore in either case the angles which the straight line AB, set up on the straight line CD, makes are either two right angles or equal to two right angles. Q.E.D.

**USED:** 1.11, CN1, CN2, D1.10
**Human refs (from References field):** 1.11, CN1, CN2, D1.10
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.14
**Statement:** If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

**Step 1.** Let AB be the given straight line, and at the point B on it let the two straight lines BC and BD, not lying on the same side of AB, make the adjacent angles ABC and ABD together equal to two right angles. I say that BD is in a straight line with CB.

**Step 2.** For, if BD is not in a straight line with BC, suppose that BE is in a straight line with CB; that is, produce the straight line CB in a straight line beyond B to a point E (P2).

**Step 3.** Then, since the straight line AB stands on the straight line CBE, the adjacent angles ABC and ABE are together equal to two right angles (1.13).

**Step 4.** But the angles ABC and ABD are also together equal to two right angles, by hypothesis. All right angles are equal to one another (P4), so the two right angles in Step 3 are equal to the two right angles of the hypothesis; hence the sum of the angles ABC and ABE is equal to the sum of the angles ABC and ABD (CN1).

**Step 5.** Let the common angle ABC be subtracted from each; then the remaining angle ABE is equal to the remaining angle ABD (CN3).

**Step 6.** But this is impossible: for the straight line BE, lying on the same side of AB as BD, falls within the angle ABD, so that the angle ABE is a part of the angle ABD, and the whole is greater than the part (CN5); that is, the angle ABD is greater than the angle ABE, which contradicts Step 5.

**Step 7.** Therefore BE is not in a straight line with CB. Similarly it can be proved that no straight line other than BD is so; therefore BD is in a straight line with CB.

**Step 8.** Therefore, if with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines are in a straight line with one another. Q.E.D.

**USED:** 1.13, CN1, CN3, CN5, P2, P4
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.667 — AI adds ['CN5', 'P2']

## Proposition 1.15
**Statement:** If two straight lines cut one another, they make the vertical angles equal to one another.

**Step 1.** Let the two straight lines AB and CD cut one another at the point E, so that the angles formed are AEC, CEB, BED, and DEA. It is to be shown that the vertical angles are equal, namely angle AEC equals angle DEB, and angle CEB equals angle AED.

**Step 2.** Since the straight line AE stands upon the straight line CD at the point E, it makes the adjacent angles CEA and AED. By 1.13, the angles CEA and AED, which AE makes with CD, are together equal to two right angles.

**Step 3.** Again, since the straight line CE stands upon the straight line AB at the point E, it makes the adjacent angles AEC and CEB. By 1.13, the angles AEC and CEB, which CE makes with AB, are together equal to two right angles.

**Step 4.** But the angles CEA and AED were also shown to be equal to two right angles. Therefore the sum of the angles AEC and CEB is equal to the sum of the angles CEA and AED, since each sum is equal to two right angles (CN1).

**Step 5.** Let the common angle AEC be subtracted from each. Then the remaining angle CEB is equal to the remaining angle AED (CN3).

**Step 6.** Similarly, since the straight line DE stands upon the straight line AB at E, the angles AED and DEB are together equal to two right angles (1.13); and from Step 2 the angles CEA and AED are together equal to two right angles. Hence the sum of the angles AED and DEB equals the sum of the angles CEA and AED, each being two right angles (CN1). Subtracting the common angle AED from each, the remaining angle DEB is equal to the remaining angle AEC (CN3).

**Step 7.** Therefore the vertical angles AEC and DEB are equal to one another, and the vertical angles CEB and AED are equal to one another. Hence, if two straight lines cut one another, they make the vertical angles equal to one another, which was to be proved.

**USED:** 1.13, CN1, CN3
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.750 — Human adds ['P4']

## Proposition 1.16
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

**Step 1.** Let ABC be a triangle, and let one side BC be produced to D, so that the exterior angle ACD is formed (by P2, BC may be produced continuously in a straight line). We must prove that the exterior angle ACD is greater than each of the interior and opposite angles BAC and ABC.

**Step 2.** Bisect AC at the point E (by 1.10, to bisect a given finite straight line).

**Step 3.** Join BE (by P1, to draw a straight line from B to E), and produce BE in a straight line to a point F (by P2). On the produced part cut off EF equal to BE (by 1.3, given two unequal straight lines, to cut off from the greater a straight line equal to the less); thus BE = EF. Join FC (by P1).

**Step 4.** Now consider the two triangles AEB and CEF. Since E bisects AC, we have AE = CE (by the construction in Step 2). Also BE = EF by construction (Step 3).

**Step 5.** The angle AEB and the angle CEF are vertical angles, formed by the two straight lines AC and BF cutting one another at E; therefore angle AEB = angle CEF (by 1.15, if two straight lines cut one another they make the vertical angles equal).

**Step 6.** Thus in triangles AEB and CEF the two sides AE, EB are equal to the two sides CE, EF respectively, and the angle AEB contained by them is equal to the angle CEF contained by them. Therefore the base AB = base CF, the triangles are equal, and the remaining angles are equal to the remaining angles respectively, namely those which the equal sides subtend (by 1.4). In particular, angle BAE = angle ECF.

**Step 7.** But the angle BAE is the same as the angle BAC, and the angle ECF is part of the angle ACD. Therefore the whole angle ACD is greater than the part angle ECF (by CN5, the whole is greater than the part), and since angle ECF = angle BAC (from Step 6), it follows that angle ACD is greater than angle BAC.

**Step 8.** Similarly, if AC is bisected and BC is produced — equivalently, if the angle BCG vertical to angle ACD is considered — the angle BCG can be shown by the same construction to be greater than angle ABC. Concretely: bisect BC, join AC's analogue and proceed as before; the exterior angle BCG equal to angle ACD (by 1.15, vertical angles) is greater than the interior and opposite angle ABC by the same argument (Steps 2–7 applied to side BC). Therefore angle ACD, being equal to angle BCG, is also greater than angle ABC.

**Step 9.** Therefore the exterior angle ACD is greater than each of the interior and opposite angles BAC and ABC. Therefore in any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles, which was to be proved.

**USED:** 1.10, 1.15, 1.3, 1.4, CN5, P1, P2
**Human refs (from References field):** 1.10, 1.15, 1.3, 1.4, CN5, P1, P2
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.17
**Statement:** In any triangle two angles taken together in any manner are less than two right angles.

**Step 1.** Let ABC be the given triangle. I say that two of its angles taken together in any manner are less than two right angles.

**Step 2.** Let the side BC be produced to D (P2), so that B, C, D lie on one straight line.

**Step 3.** Since the straight line BC has been produced to D, the angle ACD is an exterior angle of the triangle ABC; hence by 1.16 the exterior angle ACD is greater than the interior and opposite angle ABC.

**Step 4.** Let the angle ACB be added to each. Then the angle ACD together with the angle ACB is greater than the angle ABC together with the angle ACB (CN2 applied to the inequality of Step 3, adding the equal angle ACB to each side).

**Step 5.** Now the straight line AC stands on the straight line BD, making the adjacent angles ACD and ACB; therefore by 1.13 the angles ACD and ACB are together equal to two right angles.

**Step 6.** But the angles ACD and ACB together were shown greater than the angles ABC and ACB together (Step 4). Therefore the angles ABC and ACB together are less than two right angles (CN1, substituting the two right angles of Step 5 for the equal sum ACD plus ACB).

**Step 7.** Similarly, by producing AB and by producing CA, it can be proved in the same manner that the angles BAC and ACB together, and likewise the angles BAC and ABC together, are each less than two right angles.

**Step 8.** Therefore in the triangle ABC any two angles taken together in any manner are less than two right angles, which was to be proved.

**USED:** 1.13, 1.16, CN1, CN2, P2
**Human refs (from References field):** 1.13, 1.16, P2
**Jaccard:** 0.600 — AI adds ['CN1', 'CN2']

## Proposition 1.18
**Statement:** In any triangle the greater side subtends the greater angle.

**Step 1.** Let ABC be a triangle having the side AC greater than the side AB. I say that the angle ABC is also greater than the angle BCA.

**Step 2.** Since AC is greater than AB, let AD be made equal to AB by cutting off from the greater straight line AC a straight line equal to the less AB [1.3]; and let BD be joined [P1].

**Step 3.** Since AD was cut off from AC, the point D lies on AC between A and C, so that the straight line BD falls within the triangle ABC and the angle ABC is composed of the angle ABD together with the angle DBC. Hence the angle ABC is greater than the angle ABD, since the whole is greater than the part [CN5].

**Step 4.** Now in the triangle ABD, since AB is equal to AD, the triangle ABD is isosceles; therefore the angle ABD is equal to the angle ADB, the angles at the base of an isosceles triangle being equal to one another [1.5].

**Step 5.** Next, the angle ADB is an exterior angle of the triangle BDC, formed by producing the side CD to A; therefore the angle ADB is greater than the interior and opposite angle DCB, that is, than the angle BCA [1.16].

**Step 6.** But the angle ABD was proved equal to the angle ADB [Step 4]; therefore the angle ABD is likewise greater than the angle BCA.

**Step 7.** And the angle ABC was proved greater than the angle ABD [Step 3]; therefore the angle ABC is much greater than the angle BCA.

**Step 8.** Therefore in any triangle the greater side subtends the greater angle. Q.E.D.

**USED:** 1.16, 1.3, 1.5, CN5, P1
**Human refs (from References field):** 1.16, 1.3
**Jaccard:** 0.400 — AI adds ['1.5', 'CN5', 'P1']

## Proposition 1.19
**Statement:** In any triangle the greater angle is subtended by the greater side.

**Step 1.** Let ABC be a triangle having the angle ABC greater than the angle BCA. I say that the side AC is also greater than the side AB (that is, the greater angle ABC is subtended by the greater side AC).

**Step 2.** For if not, AC is either equal to AB or less than AB. These are the only remaining possibilities, since of two magnitudes one is either greater than, equal to, or less than the other.

**Step 3.** First, suppose AC were equal to AB. Then the triangle ABC would be isosceles, having AB equal to AC. But in isosceles triangles the angles at the base are equal to one another [1.5]; hence the angle ABC would be equal to the angle BCA.

**Step 4.** But, by hypothesis, the angle ABC is greater than the angle BCA, so it is not equal to it. Therefore AC is not equal to AB.

**Step 5.** Next, suppose AC were less than AB. Then AB would be the greater side, and AB subtends the angle BCA, while AC subtends the angle ABC. But in any triangle the greater side subtends the greater angle [1.18]; hence the angle BCA, being subtended by the greater side AB, would be greater than the angle ABC, which is subtended by the lesser side AC.

**Step 6.** But, by hypothesis, the angle ABC is greater than the angle BCA, so the angle BCA is not greater than the angle ABC. Therefore AC is not less than AB.

**Step 7.** Since AC is neither equal to AB nor less than AB, it follows that AC is greater than AB.

**Step 8.** Therefore in any triangle the greater angle is subtended by the greater side. Q.E.D.

**USED:** 1.18, 1.5
**Human refs (from References field):** 1.18, 1.5
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.20
**Statement:** In any triangle two sides taken together in any manner are greater than the remaining one.

**Step 1.** Let ABC be the given triangle. I say that in triangle ABC the two sides taken together in any manner are greater than the remaining one, namely BA, AC greater than BC; AB, BC greater than CA; and BC, CA greater than AB. It suffices to prove one case, say that BA together with AC is greater than BC; the other cases follow by the same argument applied to the corresponding sides.

**Step 2.** Produce the side BA in a straight line to a point D (by P2), and let AD be made equal to CA (by P3, describing a circle with centre A and distance AC, and taking the point D where this circle meets the produced line; or equivalently by 1.3 the segment AD equal to the given line CA can be cut off). Join DC (by P1).

**Step 3.** Since AD is equal to AC, the triangle ADC is isosceles. Therefore, by 1.5, the angle ADC at the base is equal to the angle ACD at the base.

**Step 4.** Now the whole angle BCD is composed of the angle ACD together with the angle ACB. Hence the angle BCD is greater than the angle ACD (by CN5, the whole is greater than the part).

**Step 5.** Since the angle BCD is greater than the angle ACD, and the angle ACD is equal to the angle ADC (from Step 3), the angle BCD is greater than the angle ADC, which is the same as the angle BDC.

**Step 6.** Consider the triangle BDC. Since in this triangle the angle BCD is greater than the angle BDC, the side opposite the greater angle is greater than the side opposite the lesser angle; that is, by 1.19, the side BD is greater than the side BC.

**Step 7.** But BD is equal to BA together with AD, since D lies on BA produced. And AD was made equal to AC. Therefore BD is equal to BA together with AC.

**Step 8.** Therefore BA together with AC is greater than BC. Similarly it may be shown that AB together with BC is greater than CA, and that BC together with CA is greater than AB. Therefore in any triangle two sides taken together in any manner are greater than the remaining one.

**USED:** 1.19, 1.3, 1.5, CN5, P1, P2, P3
**Human refs (from References field):** 1.19, 1.5, CN5
**Jaccard:** 0.429 — AI adds ['1.3', 'P1', 'P2', 'P3']

## Proposition 1.21
**Statement:** If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greaterangle.

**Step 1.** Let ABC be a triangle, and on BC, one of its sides, from the extremities B and C let the two straight lines BD and DC be constructed meeting within the triangle at the point D. I say that BD, DC are less than the remaining two sides BA, AC of the triangle, but contain an angle BDC greater than the angle BAC.

**Step 2.** Let BD be produced through D to meet the side AC at the point E (by P2, producing the finite line BD continuously; since D lies within the triangle, the produced line meets the side AC at a point E lying between A and C).

**Step 3.** Consider the triangle ABE. By 1.20, in any triangle two sides taken together are greater than the remaining one; hence the two sides BA, AE are greater than the remaining side BE, that is, BA + AE > BE.

**Step 4.** Let EC be added to each side of this inequality. Then BA + AE + EC > BE + EC (by CN2, adding the equal magnitude EC to the greater and to the less preserves the inequality). But AE + EC = AC, since E lies on AC between A and C. Therefore BA + AC > BE + EC.

**Step 5.** Consider the triangle DEC. By 1.20, the two sides DE, EC are greater than the remaining side DC, that is, DE + EC > DC.

**Step 6.** Let BD be added to each side of this inequality. Then BD + DE + EC > BD + DC (by CN2). But BD + DE = BE, since E lies on the line BD produced, with D between B and E. Therefore BE + EC > BD + DC.

**Step 7.** From Step 4, BA + AC > BE + EC, and from Step 6, BE + EC > BD + DC. Therefore BA + AC > BD + DC; that is, the two constructed straight lines BD, DC are less than the remaining two sides BA, AC of the triangle. This proves the first part.

**Step 8.** Now consider the angle BDC. In the triangle DEC, the side ED has been produced to B, so the angle BDC is an exterior angle of the triangle DEC. By 1.16, in any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles; hence the exterior angle BDC is greater than the interior and opposite angle DEC, that is, angle BDC > angle DEC.

**Step 9.** Again consider the triangle ABE. The side AE has been produced to C, so the angle DEC (which is the angle BEC) is an exterior angle of the triangle ABE. By 1.16, the exterior angle DEC is greater than the interior and opposite angle BAE; and the angle BAE is the same as the angle BAC, since E lies on AC. Therefore angle DEC > angle BAC.

**Step 10.** From Step 8, angle BDC > angle DEC, and from Step 9, angle DEC > angle BAC. Therefore angle BDC > angle BAC; that is, the constructed lines contain an angle greater than the angle contained by the remaining two sides. Thus the two constructed straight lines are less than the remaining two sides of the triangle, but contain a greater angle. Q.E.D.

**USED:** 1.16, 1.20, CN2, P2
**Human refs (from References field):** 1.16, 1.20
**Jaccard:** 0.500 — AI adds ['CN2', 'P2']

## Proposition 1.22
**Statement:** Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manner should be greater than the remaining one.

**Step 1.** Let the three given straight lines be A, B, C, such that two of them taken together in any manner are greater than the remaining one — namely A, B greater than C; A, C greater than B; and B, C greater than A. It is required to construct a triangle out of straight lines equal to A, B, C.

**Step 2.** Set out a straight line DE, terminated at D but unlimited in the direction of E (P2).

**Step 3.** On DE, by means of 1.3, cut off DF equal to A, FG equal to B, and GH equal to C.

**Step 4.** With centre F and distance FD describe the circle DKL (P3). Then, since F is the centre, FD is equal to FK for whatever point K of the circle is taken (D1.15).

**Step 5.** With centre G and distance GH describe the circle KLH (P3). Then, since G is the centre, GH is equal to GK for whatever point K of this circle is taken (D1.15).

**Step 6.** The two circles meet in a point. For the circle DKL has the point D on the segment DH (since FD = A), and the circle KLH has the point H on the segment DH (since GH = C); and the condition that any two of A, B, C taken together exceed the remaining one guarantees that neither circle lies wholly outside the other nor wholly within it, so they cut one another. Let K be a point in which they meet.

**Step 7.** Join FK and KG (P1).

**Step 8.** Now since the point F is the centre of the circle DKL, FD is equal to FK (D1.15); but FD is equal to A (Step 3); therefore FK is also equal to A (CN1).

**Step 9.** Again, since the point G is the centre of the circle KLH, GH is equal to GK (D1.15); but GH is equal to C (Step 3); therefore GK is also equal to C (CN1).

**Step 10.** And FG is also equal to B (Step 3).

**Step 11.** Therefore the three straight lines FK, FG, GK are equal to the three straight lines A, B, C respectively.

**Step 12.** Therefore out of the three straight lines FK, FG, GK, which are equal to the three given straight lines A, B, C, the triangle KFG has been constructed. Being so contained by three straight lines, KFG is a triangle (D1.19).

**USED:** 1.3, CN1, D1.15, D1.19, P1, P2, P3
**Human refs (from References field):** 1.20, 1.3
**Jaccard:** 0.125 — AI adds ['CN1', 'D1.15', 'D1.19', 'P1', 'P2', 'P3']; Human adds ['1.20']

## Proposition 1.23
**Statement:** On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

**Step 1.** Let AB be the given straight line, A the point on it, and let DCE be the given rectilineal angle (contained by the straight lines CD and CE meeting at C). It is required to construct on the straight line AB, at the point A, a rectilineal angle equal to the given angle DCE.

**Step 2.** On the straight lines CD and CE take arbitrary points D and E, and join DE by P1. There are thus formed three straight lines CD, DE, EC, which are the three sides of triangle CDE.

**Step 3.** Out of three straight lines equal to the three straight lines CD, DE, EC construct a triangle AFG, so placed that CD corresponds to AF, CE to AG, and DE to FG, with A as the common point of AF and AG (1.22). This construction is possible because, since CD, DE, EC are the three sides of the actual triangle CDE, any two of them taken together are greater than the remaining one (1.20), which is the condition required by 1.22; and one of the constructed sides, namely AF, is laid down along the given line AB.

**Step 4.** Then in the two triangles CDE, AFG the two sides DC, CE are respectively equal to the two sides FA, AG (by construction: DC = FA and CE = AG), and the base DE is equal to the base FG (by construction). Therefore the angle DCE contained by DC, CE is equal to the angle FAG contained by FA, AG (1.8).

**Step 5.** Therefore on the given straight line AB, and at the point A on it, the rectilineal angle FAG has been constructed equal to the given rectilineal angle DCE. Q.E.F.

**USED:** 1.20, 1.22, 1.8, P1
**Human refs (from References field):** 1.8
**Jaccard:** 0.250 — AI adds ['1.20', '1.22', 'P1']

## Proposition 1.24
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

**Step 1.** Let ABC and DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively, namely AB to DE and AC to DF, and let the angle BAC be greater than the angle EDF. I say that the base BC is greater than the base EF. Suppose AB is the side not greater than AC (if it were greater, the roles of the two pairs of sides may be interchanged, since the construction below is to be made on the side that is not greater).

**Step 2.** On the straight line DE, and at the point D on it, construct the angle EDG equal to the angle BAC [1.23]; let DG lie on the same side of DE as DF.

**Step 3.** From the straight line DG, since DG may be produced as far as required, cut off DG equal to AC, that is, equal to DF [1.3]; and join EG and FG [P1].

**Step 4.** Now in the triangles ABC and DEG, the side AB is equal to DE and the side AC is equal to DG (for DG was made equal to AC), and the angle BAC is equal to the angle EDG by construction. Therefore the base BC is equal to the base EG [1.4].

**Step 5.** Again, since DF is equal to DG (each being equal to AC) [CN1], the triangle DFG is isosceles, and therefore the angle DGF is equal to the angle DFG [1.5].

**Step 6.** Now the angle DFG is greater than the angle EFG, since the angle DFG contains the angle EFG and the whole is greater than the part [CN5]. (That F and the line DF lie so that EFG is part of DFG follows because DG was set on the same side of DE as DF and DG = DF ≥ DE, so G lies beyond EF as seen from the construction; thus FG falls within the angle DFE... ) Therefore the angle DGF is much greater than the angle EFG, since the angle DGF is equal to the angle DFG and the angle DFG is greater than the angle EFG [CN5].

**Step 7.** And since the angle EGF is less than the angle DGF, while the angle DGF is equal to the angle DFG, and the angle DFG is greater than the angle EFG, it follows that the angle EGF is less than the angle EFG [CN1].

**Step 8.** Then, in the triangle EFG, since the angle EFG is greater than the angle EGF, and the greater angle is subtended by the greater side, the side EG opposite the greater angle EFG is greater than the side EF opposite the lesser angle EGF [1.19].

**Step 9.** But EG was proved equal to BC [Step 4]. Therefore BC is also greater than EF [CN1]. Therefore, if two triangles have the two sides equal to two sides respectively, but have the angle contained by the equal straight lines of the one greater than that of the other, they have also the base greater than the base.

**USED:** 1.19, 1.23, 1.3, 1.4, 1.5, CN1, CN5, P1
**Human refs (from References field):** 1.19, 1.23, 1.4, 1.5
**Jaccard:** 0.500 — AI adds ['1.3', 'CN1', 'CN5', 'P1']

## Proposition 1.25
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.

**Step 1.** Let ABC and DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively, namely AB to DE and AC to DF, but having the base BC greater than the base EF. I say that the angle BAC is also greater than the angle EDF.

**Step 2.** For, if the angle BAC be not greater than the angle EDF, it is either equal to it or less than it.

**Step 3.** Suppose first that the angle BAC is equal to the angle EDF. Then, since AB is equal to DE and AC to DF, and the angle BAC is equal to the angle EDF, the two sides AB, AC equal the two sides DE, DF respectively and contain equal angles; therefore by 1.4 the base BC is equal to the base EF. But, by hypothesis, BC is greater than EF; this is a contradiction. Therefore the angle BAC is not equal to the angle EDF.

**Step 4.** Suppose next that the angle BAC is less than the angle EDF. Then the two triangles have the two sides AB, AC equal to the two sides DE, DF respectively, but have the angle DEF (that is, the angle EDF) contained by the equal straight lines greater than the angle BAC. Therefore by 1.24 the base EF is greater than the base BC, that is, BC is less than EF. But, by hypothesis, BC is greater than EF; this is a contradiction. Therefore the angle BAC is not less than the angle EDF.

**Step 5.** But it was also proved that it is not equal to it. Therefore the angle BAC is greater than the angle EDF.

**Step 6.** Therefore, if two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they also have the one of the angles contained by the equal straight lines greater than the other. Q.E.D.

**USED:** 1.24, 1.4
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.26
**Statement:** If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of the equal angles, they will also have the remaining sides equal tothe remaining sides and the remaining angle to the remaining angle.

**Step 1.** Let ABC and DEF be two triangles having the two angles ABC, BCA equal to the two angles DEF, EFD respectively, namely the angle ABC to the angle DEF and the angle BCA to the angle EFD. I say first the case in which the equal sides adjoin the equal angles, that is, BC is equal to EF. I claim that the remaining sides equal the remaining sides, namely AB to DE and AC to DF, and the remaining angle BAC equals the remaining angle EDF.

**Step 2.** For, if AB is unequal to DE, one of them is greater. Let AB be the greater, and from it cut off BG equal to DE (by 1.3, since two unequal straight lines being given, a straight line equal to the less may be cut off from the greater). Join GC (by P1).

**Step 3.** Then in the two triangles GBC and DEF, the two sides GB, BC are equal to the two sides DE, EF respectively (BG equal to DE by construction, BC equal to EF by hypothesis), and the angle GBC equals the angle DEF (since the angle ABC equals the angle DEF by hypothesis, and GBC is the angle ABC). Therefore, by 1.4, the base GC equals the base DF, the triangle GBC equals the triangle DEF, and the remaining angles equal the remaining angles, namely those which the equal sides subtend; thus the angle GCB equals the angle DFE.

**Step 4.** But the angle DFE was assumed equal to the angle BCA. Therefore the angle GCB equals the angle BCA (by CN1), the less to the greater: which is impossible (by CN5, the whole is greater than the part, since G lies inside, making angle GCB part of angle BCA). Therefore AB is not unequal to DE, and so it is equal to it.

**Step 5.** But BC is also equal to EF. So the two sides AB, BC are equal to the two sides DE, EF respectively, and the angle ABC equals the angle DEF. Therefore, by 1.4, the base AC equals the base DF, and the remaining angle BAC equals the remaining angle EDF. This proves the first case.

**Step 6.** Now let the equal sides subtend equal angles, that is, let AB be equal to DE, the side subtending one of the equal angles (AB subtends angle BCA, and DE subtends angle EFD, and angle BCA equals angle EFD). I say again that the remaining sides equal the remaining sides, namely BC to EF and AC to DF, and the remaining angle BAC equals the remaining angle EDF.

**Step 7.** For, if BC is unequal to EF, one of them is greater. Let BC be the greater, and from it cut off BH equal to EF (by 1.3). Join AH (by P1).

**Step 8.** Then in the two triangles ABH and DEF, the two sides AB, BH are equal to the two sides DE, EF respectively (AB equal to DE by hypothesis, BH equal to EF by construction), and the angle ABH equals the angle DEF (since the angle ABC equals the angle DEF by hypothesis, and ABH is the angle ABC). Therefore, by 1.4, the remaining angles equal the remaining angles which the equal sides subtend; thus the angle AHB equals the angle DFE.

**Step 9.** But the angle DFE equals the angle ACB (= angle BCA) by hypothesis. Therefore the angle AHB equals the angle ACB (by CN1). Now in the triangle AHC, the side BC has been produced beyond H to C, so AHB is an exterior angle of the triangle AHC and ACB (that is, AHC) is the interior and opposite angle. By 1.16, the exterior angle AHB is greater than the interior and opposite angle ACH: which contradicts their being equal. Therefore BC is not unequal to EF, and so it is equal to it.

**Step 10.** But AB is also equal to DE. So the two sides AB, BC are equal to the two sides DE, EF respectively, and they contain the equal angles ABC, DEF. Therefore, by 1.4, the base AC equals the base DF, and the remaining angle BAC equals the remaining angle EDF. Thus in both cases the remaining sides equal the remaining sides and the remaining angle equals the remaining angle, which was to be proved.

**USED:** 1.16, 1.3, 1.4, CN1, CN5, P1
**Human refs (from References field):** 1.16, 1.4
**Jaccard:** 0.333 — AI adds ['1.3', 'CN1', 'CN5', 'P1']

## Proposition 1.27
**Statement:** If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

**Step 1.** Let the straight line EF fall on the two straight lines AB, CD, meeting AB at E and CD at F, and let it make the alternate angles AEF and EFD equal to one another. I say that AB is parallel to CD.

**Step 2.** For, if not, then AB and CD, being produced, will meet either in the direction of B, D or in the direction of A, C. Let them be produced and meet, in the direction of B, D, at the point G.

**Step 3.** Then GEF is a triangle, having EF as one side and the point G as the vertex opposite to it, with EG lying along AB and FG lying along CD.

**Step 4.** In the triangle GEF the side EG has been produced to A, so that the angle AEF is the exterior angle of the triangle, and the angle EFG (which is the angle EFD) is one of the interior and opposite angles. But in any triangle the exterior angle is greater than either of the interior and opposite angles [1.16]; therefore the angle AEF is greater than the angle EFG, that is, greater than the angle EFD.

**Step 5.** But the angle AEF was assumed equal to the angle EFD; therefore AEF is at once equal to and greater than EFD, which is impossible. Therefore AB and CD, when produced, do not meet in the direction of B, D.

**Step 6.** Similarly it can be proved that neither do they meet in the direction of A, C: for then the angle EFD would be the exterior angle of the resulting triangle and AEF one of the interior and opposite angles, so that EFD would be greater than AEF, again contradicting their assumed equality [1.16].

**Step 7.** But straight lines which do not meet in either direction, being in the same plane and produced indefinitely, are parallel [D1.23]. Therefore AB is parallel to CD. Q.E.D.

**USED:** 1.16, D1.23
**Human refs (from References field):** 1.16, D1.23
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.28
**Statement:** If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to two right angles, the straight lines will be parallel to one another.

**Step 1.** Let the straight line EF fall on the two straight lines AB and CD. Let G be the point where EF meets AB, and H the point where EF meets CD, with E on the side of AB away from CD and F on the side of CD away from AB. Thus along EF the order of points is E, G, H, F.

**Step 2.** *First case:* suppose the exterior angle EGB is equal to the interior and opposite angle GHD on the same side.

**Step 3.** The straight lines AB and EF cut one another at G; hence by 1.15 the vertical angles EGB and AGH are equal to one another.

**Step 4.** But the angle EGB was assumed equal to the angle GHD. Therefore, since the angle AGH equals the angle EGB (Step 3) and the angle EGB equals the angle GHD (Step 2), the angle AGH equals the angle GHD by CN1.

**Step 5.** Now AGH and GHD are the alternate angles made by the straight line EF (i.e. GH) falling on the two straight lines AB and CD; and they have been shown equal. Therefore by 1.27 AB is parallel to CD.

**Step 6.** *Second case:* suppose instead that the interior angles on the same side, namely BGH and GHD, are together equal to two right angles.

**Step 7.** The straight line AB is a straight line, and EF (the part GE) is set up on it at the point G, making the adjacent angles AGH and BGH. Hence by 1.13 the angles AGH and BGH are together equal to two right angles.

**Step 8.** Therefore the angles AGH and BGH together (Step 7) are equal to the angles BGH and GHD together (Step 6), each pair being equal to two right angles, by P4 and CN1.

**Step 9.** Let the common angle BGH be subtracted from each pair. Then by CN3 the remaining angle AGH is equal to the remaining angle GHD.

**Step 10.** But AGH and GHD are the alternate angles made by EF (i.e. GH) falling on AB and CD; and they have been shown equal. Therefore by 1.27 AB is parallel to CD.

**Step 11.** Hence in each case the two straight lines AB and CD are parallel to one another, which was to be proved.

**USED:** 1.13, 1.15, 1.27, CN1, CN3, P4
**Human refs (from References field):** 1.13, 1.15, 1.27
**Jaccard:** 0.500 — AI adds ['CN1', 'CN3', 'P4']

## Proposition 1.29
**Statement:** A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

**Step 1.** Let the straight line EF fall on the parallel straight lines AB, CD, meeting AB at the point G and CD at the point H. I say that it makes the alternate angles AGH, GHD equal; the exterior angle EGB equal to the interior and opposite angle GHD; and the interior angles on the same side, BGH, GHD, equal to two right angles.

**Step 2.** First I show the alternate angles AGH, GHD are equal. For if they are not equal, one of them is greater; let AGH be the greater. Add the angle BGH to each. Then the angles AGH, BGH are greater than the angles BGH, GHD (CN: if to unequals equals be added, the wholes are unequal — applied as the natural extension; more precisely, since AGH is greater than GHD, by adding BGH to both, AGH together with BGH is greater than GHD together with BGH).

**Step 3.** But the angles AGH, BGH are equal to two right angles, since EF stands on the straight line AB at G [1.13]. Therefore the angles BGH, GHD are less than two right angles.

**Step 4.** But straight lines produced indefinitely from angles less than two right angles meet [P5]; therefore AB, CD, if produced indefinitely, will meet on the side of B, D. But they do not meet, because they are by hypothesis parallel [D1.23]. Therefore the angle AGH is not unequal to the angle GHD; therefore it is equal to it.

**Step 5.** Next, the angle AGH is equal to the angle EGB, for these are vertical angles formed by the two straight lines EF and AB cutting one another at G [1.15]. Since AGH was shown equal to GHD, and AGH is equal to EGB, therefore the exterior angle EGB is also equal to the interior and opposite angle GHD [CN1].

**Step 6.** Finally, let the angle BGH be added to each of the equals EGB, GHD. Then the angles EGB, BGH are equal to the angles BGH, GHD [CN2]. But the angles EGB, BGH are equal to two right angles, since EF stands on the straight line AB at G [1.13]. Therefore the angles BGH, GHD are also equal to two right angles [CN1].

**Step 7.** Therefore a straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles. Q.E.D.

**USED:** 1.13, 1.15, CN1, CN2, D1.23, P5
**Human refs (from References field):** 1.13, 1.15, CN1, CN2, P5
**Jaccard:** 0.833 — AI adds ['D1.23']

## Proposition 1.30
**Statement:** Straight lines parallel to the same straight line are also parallel to one another.

**Step 1.** Let the straight lines AB and CD each be parallel to the straight line EF. I say that AB is also parallel to CD.

**Step 2.** Let the straight line GHK fall across the three lines, cutting AB at G, EF at H, and CD at K (P1, P2 supply such a transversal, and the configuration is taken with AB and CD on opposite sides of EF).

**Step 3.** Since the straight line GK falls on the parallel straight lines AB and EF, by 1.29 the alternate angles are equal; hence the angle AGH (at G) is equal to the angle GHF (the interior angle that EF makes with the transversal at H).

**Step 4.** Again, since the straight line GK falls on the parallel straight lines EF and CD, by 1.29 the exterior angle equals the interior and opposite angle on the same side; hence the angle GHF (at H) is equal to the angle GKD (at K).

**Step 5.** Therefore the angle AGH is equal to the angle GHF, and the angle GHF is equal to the angle GKD; consequently, by CN1, the angle AGH is equal to the angle GKD.

**Step 6.** But these are alternate angles made by the straight line GK falling on the two straight lines AB and CD. Since the alternate angles are equal, by 1.27 the straight lines AB and CD are parallel to one another.

**Step 7.** Therefore straight lines parallel to the same straight line are also parallel to one another. Q.E.D.

**USED:** 1.27, 1.29, CN1, P1, P2
**Human refs (from References field):** 1.29, CN1
**Jaccard:** 0.400 — AI adds ['1.27', 'P1', 'P2']

## Proposition 1.31
**Statement:** Through a given point to draw a straight line parallel to a given straight line.

**Step 1.** Let A be the given point and BC the given straight line; it is required to draw through A a straight line parallel to BC.

**Step 2.** Take a point D at random on BC, and join AD (P1).

**Step 3.** On the straight line DA, and at the point A on it, construct the angle DAE equal to the angle ADC (1.23).

**Step 4.** Produce the straight line EA in a straight line to F (P2), so that EAF is one straight line through A.

**Step 5.** Now the straight line AD falls on the two straight lines EF and BC, and by the construction of Step 3 it makes the alternate angles EAD and ADC equal to one another.

**Step 6.** But when a straight line falling on two straight lines makes the alternate angles equal to one another, the two straight lines are parallel to one another (1.27). Therefore EF is parallel to BC.

**Step 7.** Thus through the given point A the straight line EAF has been drawn parallel to the given straight line BC. Q.E.F.

**USED:** 1.23, 1.27, P1, P2
**Human refs (from References field):** 1.23, 1.27
**Jaccard:** 0.500 — AI adds ['P1', 'P2']

## Proposition 1.32
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

**Step 1.** Let ABC be a triangle, and let one of its sides BC be produced in a straight line to D (P2), so that the exterior angle ACD is formed.

**Step 2.** Through the point C draw the straight line CE parallel to the side AB (1.31).

**Step 3.** Since AB is parallel to CE, and the straight line AC falls upon them, the alternate angles BAC and ACE made by AC are equal to one another (1.29).

**Step 4.** Again, since AB is parallel to CE, and the straight line BD falls upon them, the exterior angle ECD is equal to the interior and opposite angle ABC on the same side (1.29).

**Step 5.** But the angle ACE was also proved equal to the angle BAC; therefore the whole angle ACD, which is composed of ACE and ECD, is equal to the sum of the two interior and opposite angles BAC and ABC (CN2). This proves the first assertion: the exterior angle is equal to the two interior and opposite angles.

**Step 6.** Let the angle ACB be added to each side of this equality. Then the sum of the angles ACD and ACB is equal to the sum of the three angles BAC, ABC, and ACB, that is, to the three interior angles of the triangle (CN2).

**Step 7.** But the angles ACD and ACB, which the straight line AC set up on the straight line BD makes, are together equal to two right angles (1.13).

**Step 8.** Therefore the three interior angles BAC, ABC, and ACB of the triangle are also equal to two right angles (CN1). This proves the second assertion.

**USED:** 1.13, 1.29, 1.31, CN1, CN2, P2
**Human refs (from References field):** 1.13, 1.29, 1.31
**Jaccard:** 0.500 — AI adds ['CN1', 'CN2', 'P2']

## Proposition 1.33
**Statement:** The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.

**Step 1.** Let AB and CD be equal and parallel straight lines, and let the straight lines AC and BD join them at their extremities in the same directions. I say that AC and BD are also equal and parallel.

**Step 2.** Join BC (P1).

**Step 3.** Since AB is parallel to CD, and the straight line BC has fallen upon them, the alternate angles ABC and BCD are equal to one another (1.29).

**Step 4.** Now consider the two triangles ABC and DCB. We have AB equal to DC (by hypothesis), the side BC common to both, and the included angle ABC equal to the included angle DCB (Step 3). Therefore the two sides AB, BC and the angle ABC are equal respectively to the two sides DC, CB and the angle DCB.

**Step 5.** Hence, by the congruence of two triangles having two sides and the included angle equal, the base AC is equal to the base DB, the triangle ABC equals the triangle DCB, and the remaining angles are equal to the remaining angles respectively, namely those subtended by the equal sides; in particular the angle ACB is equal to the angle DBC (1.4).

**Step 6.** Thus AC is equal to BD, which is the first part of the proposition.

**Step 7.** Furthermore, the straight line BC, falling on the two straight lines AC and BD, makes the alternate angles ACB and DBC equal to one another (Step 5). Therefore AC is parallel to BD (1.27).

**Step 8.** Therefore the straight lines AC and BD joining the equal and parallel straight lines AB and CD at their extremities in the same directions are themselves equal and parallel.

**USED:** 1.27, 1.29, 1.4, P1
**Human refs (from References field):** 1.27, 1.29, 1.4
**Jaccard:** 0.750 — AI adds ['P1']

## Proposition 1.34
**Statement:** In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.

**Step 1.** Let ACDB be a parallelogrammic area, having AB parallel to CD and AC parallel to BD (D1.22), and let BC be its diameter. It is to be shown that the opposite sides and angles of the parallelogram are equal to one another and that the diameter BC bisects it.

**Step 2.** Since AB is parallel to CD, and the straight line BC falls upon them, the alternate angles ABC, BCD are equal to one another (1.29).

**Step 3.** Again, since AC is parallel to BD, and the straight line BC falls upon them, the alternate angles ACB, CBD are equal to one another (1.29).

**Step 4.** Therefore the two triangles ABC, DCB have the two angles ABC, BCA equal to the two angles DCB, CBD respectively, namely ABC to DCB and BCA to CBD; and they have one side equal to one side, namely BC which is adjacent to the equal angles and common to both triangles. Therefore they have the remaining sides equal to the remaining sides respectively and the remaining angle to the remaining angle (1.26); so that AB is equal to CD, AC to BD, and further the angle BAC is equal to the angle CDB.

**Step 5.** Thus the opposite sides AB, CD and AC, BD are equal to one another, and one pair of opposite angles, BAC and CDB, is equal.

**Step 6.** For the remaining pair of opposite angles: since the angle ABC is equal to the angle BCD, and the angle CBD is equal to the angle ACB, the whole angle ABD, which is composed of the angles ABC and CBD, is equal to the whole angle ACD, which is composed of the angles BCD and ACB, equals being added to equals (CN2).

**Step 7.** Therefore in the parallelogram the opposite sides and the opposite angles are equal to one another.

**Step 8.** I say next that the diameter bisects the area. For since AB is equal to CD, and BC is common, the two sides AB, BC are equal to the two sides DC, CB respectively; and the angle ABC was proved equal to the angle DCB, which is contained by these sides. Therefore the base AC is equal to the base DB, and the triangle ABC is equal to the triangle DCB (1.4).

**Step 9.** Therefore the diameter BC bisects the parallelogram ACDB. Hence in parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas, which was to be proved.

**USED:** 1.26, 1.29, 1.4, CN2, D1.22
**Human refs (from References field):** 1.26, 1.29, 1.4, CN2
**Jaccard:** 0.800 — AI adds ['D1.22']

## Proposition 1.35
**Statement:** Parallelograms which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EBCF be parallelograms on the same base BC and in the same parallels BC, AF (so that A, D, E, F all lie on the straight line through A parallel to BC, and the points lie in the order A, D, E, F or A, E, D, F along that line). We must prove that the parallelogram ABCD is equal to the parallelogram EBCF.

**Step 2.** Since ABCD is a parallelogram, its opposite sides AD and BC are equal (1.34). Likewise, since EBCF is a parallelogram, its opposite sides EF and BC are equal (1.34).

**Step 3.** Since AD is equal to BC and EF is equal to BC, AD is equal to EF (CN1).

**Step 4.** Add (or subtract) the common segment DE to (from) each: in the case A, D, E, F, adding DE to AD gives AE, and adding DE to EF... more directly, since AD equals EF, adding the common part DE yields AE equal to DF; in the case A, E, D, F, subtracting the common part ED from each yields AE equal to DF (CN2 or CN3). In either configuration AE is equal to DF.

**Step 5.** Since ABCD is a parallelogram, its opposite side AB is equal to the opposite side DC (1.34).

**Step 6.** The straight line AF falls on the parallel straight lines AB and DC. Hence the exterior angle FDC is equal to the interior and opposite angle EAB (1.29).

**Step 7.** Now in the two triangles EAB and FDC: side EA is equal to side FD (Step 4), side AB is equal to side DC (Step 5), and the contained angle EAB is equal to the contained angle FDC (Step 6). Therefore the base EB is equal to the base FC, and the triangle EAB is equal to the triangle FDC (1.4).

**Step 8.** From the figure made up of triangle EAB together with the region DGEB... taking the whole figure ABED (the quadrilateral bounded by AB, BE-region) consider it as follows: from the triangle FDC subtract the triangle DGE, and from the triangle EAB subtract the same triangle DGE; the remainders are equal, namely the trapezium ABGD is equal to the trapezium EGCF (CN3), where G is the intersection of the diagonals BE and DC.

**Step 9.** To each of these equal trapezia add the common triangle GBC: then the whole parallelogram ABCD is equal to the whole parallelogram EBCF (CN2).

**Step 10.** Therefore parallelograms on the same base and in the same parallels are equal to one another. Q.E.D.

**USED:** 1.29, 1.34, 1.4, CN1, CN2, CN3
**Human refs (from References field):** 1.29, 1.34, 1.4, CN1, CN2, CN3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.36
**Statement:** Parallelograms which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EFGH be parallelograms which are on equal bases BC, FG and in the same parallels AH, BG; I say that the parallelogram ABCD is equal to the parallelogram EFGH.

**Step 2.** Join BE and CH (P1).

**Step 3.** Since BC equals FG (by hypothesis), and FG equals EH, because in the parallelogram EFGH the opposite sides EH and FG are equal (1.34), therefore BC also equals EH (CN1).

**Step 4.** Moreover, BC and EH are parallel: for AH and BG are the same parallels, EH lies along AH and BC lies along BG, so EH and BC are straight lines in these parallels and do not meet, hence they are parallel (D1.23).

**Step 5.** Now EB and HC join the straight lines BC and EH, which are equal (Step 3) and parallel (Step 4), at the extremities which are toward the same direction. Therefore EB and HC are themselves equal and parallel (1.33).

**Step 6.** Therefore EBCH is a parallelogram, since its opposite sides BC, EH are equal and parallel and its opposite sides EB, HC are equal and parallel.

**Step 7.** The parallelogram ABCD and the parallelogram EBCH are on the same base BC and in the same parallels BC, AH; therefore the parallelogram ABCD equals the parallelogram EBCH (1.35).

**Step 8.** For the same reason, the parallelogram EFGH and the parallelogram EBCH are on the same base EH and in the same parallels EH, BG; therefore the parallelogram EFGH also equals the parallelogram EBCH (1.35).

**Step 9.** Therefore the parallelogram ABCD also equals the parallelogram EFGH (CN1).

**Step 10.** Therefore parallelograms which are on equal bases and in the same parallels are equal to one another. Q.E.D.

**USED:** 1.33, 1.34, 1.35, CN1, D1.23, P1
**Human refs (from References field):** 1.33, 1.34, 1.35, CN1
**Jaccard:** 0.667 — AI adds ['D1.23', 'P1']

## Proposition 1.37
**Statement:** Triangles which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let ABC and DBC be triangles on the same base BC and in the same parallels AD, BC (so that A and D both lie on a straight line AD parallel to BC). It is to be proved that triangle ABC is equal to triangle DBC.

**Step 2.** Produce the straight line AD in both directions to points E and F (P2), so that E, A, D, F lie on one straight line which is parallel to BC.

**Step 3.** Through B draw BE parallel to CA, meeting the line EF at E (1.31).

**Step 4.** Through C draw CF parallel to BD, meeting the line EF at F (1.31).

**Step 5.** Then EBCA is a quadrilateral whose opposite sides are parallel: EA and BC lie in the same parallels, and EB is parallel to AC by construction. Hence EBCA is a parallelogram. Likewise DBCF has BC parallel to DF (they are in the same parallels) and BD parallel to CF by construction, so DBCF is a parallelogram (D1.23).

**Step 6.** The parallelograms EBCA and DBCF are on the same base BC and in the same parallels BC and EF; therefore EBCA is equal to DBCF (1.35).

**Step 7.** AB is a diameter of the parallelogram EBCA, and the diameter bisects the parallelogram; therefore triangle ABC is half of the parallelogram EBCA (1.34).

**Step 8.** Likewise DC is a diameter of the parallelogram DBCF, and the diameter bisects the parallelogram; therefore triangle DBC is half of the parallelogram DBCF (1.34).

**Step 9.** Now the parallelogram EBCA is equal to the parallelogram DBCF (Step 6), and triangle ABC is half of the one while triangle DBC is half of the other (Steps 7, 8). But the halves of equal things are equal to one another (CN1 applied to halves). Therefore triangle ABC is equal to triangle DBC.

**Step 10.** Therefore triangles which are on the same base and in the same parallels are equal to one another, which was to be proved.

**USED:** 1.31, 1.34, 1.35, CN1, D1.23, P2
**Human refs (from References field):** 1.31, 1.34, 1.35
**Jaccard:** 0.500 — AI adds ['CN1', 'D1.23', 'P2']

## Proposition 1.38
**Statement:** Triangles which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let ABC and DEF be triangles on equal bases BC and EF and in the same parallels BF and AD (so that A and D lie on a straight line parallel to BC and EF, and BC, EF lie on one straight line). It is to be proved that triangle ABC is equal to triangle DEF.

**Step 2.** Through the point B draw BG parallel to CA, and through the point F draw FH parallel to ED (1.31). Thus BGAC and EFHD are each parallelograms.

**Step 3.** The parallelogram GBCA is on the base BC, and the parallelogram DEFH is on the base EF; the bases BC and EF are equal (by hypothesis), and both parallelograms lie in the same parallels BF and GH (since G, A, D, H all lie on the straight line through A and D parallel to BC, EF). Therefore the parallelogram GBCA is equal to the parallelogram DEFH (1.36).

**Step 4.** Now AB is a diameter of the parallelogram GBCA, so it bisects it; hence the triangle ABC is half of the parallelogram GBCA (1.34). Likewise DF is a diameter of the parallelogram DEFH, so it bisects it; hence the triangle DEF is half of the parallelogram DEFH (1.34).

**Step 5.** But the halves of equal things are equal to one another. Since the parallelogram GBCA is equal to the parallelogram DEFH, and the triangles ABC and DEF are their respective halves, the triangle ABC is equal to the triangle DEF (CN1).

**Step 6.** Therefore triangles which are on equal bases and in the same parallels are equal to one another. Q.E.D.

**USED:** 1.31, 1.34, 1.36, CN1
**Human refs (from References field):** 1.31, 1.34, 1.36
**Jaccard:** 0.750 — AI adds ['CN1']

## Proposition 1.39
**Statement:** Equal triangles which are on the same base and on the same side are also in the same parallels.

**Step 1.** Let ABC and DBC be equal triangles which are on the same base BC and on the same side of it. I say that they are also in the same parallels; that is, joining AD, AD is parallel to BC.

**Step 2.** Join AD. I assert that AD is parallel to BC. For, if it is not, then through the point A draw the straight line AE parallel to the straight line BC (1.31), and join EC, where E is the point in which AE meets DC (produced if necessary).

**Step 3.** Then, since AE is parallel to BC, and the triangles ABC and EBC are on the same base BC and in the same parallels AE, BC, the triangle ABC is equal to the triangle EBC (1.37).

**Step 4.** But the triangle ABC is equal to the triangle DBC by hypothesis; therefore the triangle DBC is also equal to the triangle EBC (CN1).

**Step 5.** Therefore the greater triangle DBC equals the lesser triangle EBC: which is impossible, since EBC is a part of DBC and the whole is greater than the part (CN5).

**Step 6.** Therefore AE is not parallel to BC. Similarly we can prove that neither is any other straight line through A except AD; therefore AD is parallel to BC.

**Step 7.** Therefore equal triangles which are on the same base and on the same side are also in the same parallels.

**USED:** 1.31, 1.37, CN1, CN5
**Human refs (from References field):** 1.31, 1.37, CN1
**Jaccard:** 0.750 — AI adds ['CN5']

## Proposition 1.40
**Statement:** Equal triangles which are on equal bases and on the same side are also in the same parallels.

**Step 1.** Let ABC and CDE be equal triangles standing on equal bases BC and CE which lie on the same straight line (so that BCE is one straight line, with B, C, E in order) and on the same side of it. I say that they are also in the same parallels; that is, joining AD, I say that AD is parallel to BE.

**Step 2.** Join AD (by P1, a straight line may be drawn from A to D).

**Step 3.** I say that AD is parallel to BE. For if it is not, draw through the point A a straight line AF parallel to the straight line BE (by 1.31), and join FE (by P1), where F is taken so that AF meets ED produced or lies in the configuration giving triangle FCE on base CE.

**Step 4.** Then the triangle ABC is on the base BC and the triangle FCE is on the base CE; the bases BC and CE are equal; and both triangles lie in the same parallels BE and AF (by construction AF is parallel to BE). Therefore the triangle ABC is equal to the triangle FCE (by 1.38).

**Step 5.** But the triangle ABC is equal to the triangle DCE by hypothesis. Therefore the triangle DCE is also equal to the triangle FCE (by CN1).

**Step 6.** This is impossible: for, since F is distinct from D, the one of the triangles DCE, FCE is a part of the other, and the whole is greater than the part (by CN5), so they cannot be equal. Therefore the line drawn through A parallel to BE cannot fail to pass through D.

**Step 7.** Similarly we can prove that no straight line through A other than AD is parallel to BE. Therefore AD is parallel to BE.

**Step 8.** Therefore equal triangles which are on equal bases and on the same side are also in the same parallels. Q.E.D.

**USED:** 1.31, 1.38, CN1, CN5, P1
**Human refs (from References field):** 1.31, 1.38, CN1
**Jaccard:** 0.600 — AI adds ['CN5', 'P1']

## Proposition 1.41
**Statement:** If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.

**Step 1.** Let ABCD be a parallelogram having the same base BC as the triangle EBC, and let them be in the same parallels BC and AE (so that the vertex E lies on the straight line AD produced, i.e. on the parallel through A and D).

**Step 2.** Join AC, the diameter of the parallelogram ABCD.

**Step 3.** The diameter AC bisects the parallelogram ABCD, so the triangle ABC is equal to the triangle ACD [1.34]. Hence the parallelogram ABCD is double of the triangle ABC.

**Step 4.** Now the triangle ABC and the triangle EBC are on the same base BC and in the same parallels BC and AE. Therefore the triangle ABC is equal to the triangle EBC [1.37].

**Step 5.** Since the parallelogram ABCD is double of the triangle ABC (Step 3), and the triangle ABC equals the triangle EBC (Step 4), the parallelogram ABCD is also double of the triangle EBC [CN1, applied to the doubles].

**Step 6.** Therefore, if a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle. Q.E.D.

**USED:** 1.34, 1.37, CN1, P1
**Human refs (from References field):** 1.34, 1.37
**Jaccard:** 0.500 — AI adds ['CN1', 'P1']

## Proposition 1.42
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let ABC be the given triangle and D the given rectilineal angle. It is required to construct, in the angle D, a parallelogram equal to the triangle ABC.

**Step 2.** Bisect BC at E [1.10], and join AE [P1]. Thus E is the midpoint of BC, so BE is equal to EC.

**Step 3.** On the straight line EC, and at the point E on it, construct the angle CEF equal to the given angle D [1.23].

**Step 4.** Through A draw AG parallel to EC (that is, to BC) [1.31], and let it be produced so that EF, when produced if necessary, meets it; specifically, draw EF up to its meeting with AG and let F be that point, so that EF lies along the side of the constructed angle and F is on AG.

**Step 5.** Through C draw CG parallel to EF [1.31], meeting AG at G.

**Step 6.** Then FE is parallel to GC (by construction, since CG was drawn parallel to EF) [1.31], and FG (lying along AG) is parallel to EC (since AG was drawn parallel to BC, and E, C lie on BC) [1.31]. Therefore FECG is a parallelogram [D1.23, D1.22 sense of a quadrilateral with both pairs of opposite sides parallel].

**Step 7.** Now join AE [P1, already drawn]. The triangles ABE and AEC are on the equal bases BE and EC and in the same parallels BC and AG; therefore the triangle ABE is equal to the triangle AEC [1.38]. Hence the whole triangle ABC is double of the triangle AEC [CN2: the two equal triangles ABE and AEC together make ABC, so ABC is double of AEC].

**Step 8.** The parallelogram FECG has the same base EC with the triangle AEC and is in the same parallels EC and AG; therefore the parallelogram FECG is double of the triangle AEC [1.41].

**Step 9.** But the triangle ABC was also proved double of the triangle AEC. Therefore the parallelogram FECG is equal to the triangle ABC [CN1: things which are equal to the same thing (here, doubles of the same triangle) are equal to one another].

**Step 10.** And the parallelogram FECG has the angle FEC equal to the given angle D, by construction [1.23]. Therefore the parallelogram FECG has been constructed equal to the given triangle ABC, in the angle FEC which is equal to the given angle D. Q.E.F.

**USED:** 1.10, 1.23, 1.31, 1.38, 1.41, CN1, CN2, D1.22, D1.23, P1
**Human refs (from References field):** 1.23, 1.31, 1.38, 1.41
**Jaccard:** 0.400 — AI adds ['1.10', 'CN1', 'CN2', 'D1.22', 'D1.23', 'P1']

## Proposition 1.43
**Statement:** In any parallelogram the complements of the parallelograms about the diameter are equal to one another.

**Step 1.** Let ABCD be a parallelogram with diameter AC. Let K be any point on AC. Through K let EKG be drawn parallel to the sides AD and BC, and let HKF be drawn parallel to the sides AB and DC (1.31 guarantees such parallels can be drawn). Here E lies on AB, G on DC, H on AD, and F on BC, so that AHKE and KFCG are the parallelograms about the diameter, while HDGK (call it BK... ) — naming the two complements as EBFK and HKGD, these are the complements of the parallelograms about the diameter. (The figures AHKE and KGCF are parallelograms because their opposite sides are parallel by construction, by D1.23 and the parallelism established.)

**Step 2.** Since ABCD is a parallelogram and AC is its diameter, the diameter bisects it; therefore the triangle ABC is equal to the triangle ACD (1.34).

**Step 3.** Again, since AHKE is a parallelogram and AK is its diameter (AK being part of the diameter AC), the diameter bisects it; therefore the triangle AEK is equal to the triangle AHK (1.34).

**Step 4.** For the same reason, since KFCG is a parallelogram and KC is its diameter (KC being part of the diameter AC), the diameter bisects it; therefore the triangle KFC is equal to the triangle KGC (1.34).

**Step 5.** Now the triangle AEK is equal to the triangle AHK, and the triangle KFC is equal to the triangle KGC; therefore the triangle AEK together with the triangle KFC is equal to the triangle AHK together with the triangle KGC (CN2).

**Step 6.** But the whole triangle ABC is equal to the whole triangle ACD (Step 2). Therefore, if from the triangle ABC there be subtracted the triangles AEK and KFC, and from the equal triangle ACD there be subtracted the equal triangles AHK and KGC, the remainders are equal (CN3).

**Step 7.** The remainder of triangle ABC after subtracting triangles AEK and KFC is the complement EBFK; and the remainder of triangle ACD after subtracting triangles AHK and KGC is the complement HKGD. Therefore the complement EBFK is equal to the complement HKGD (CN1, CN3).

**Step 8.** Hence in the parallelogram ABCD the complements of the parallelograms about the diameter are equal to one another, which was to be proved.

**USED:** 1.31, 1.34, CN1, CN2, CN3, D1.23
**Human refs (from References field):** 1.34, CN2, CN3
**Jaccard:** 0.500 — AI adds ['1.31', 'CN1', 'D1.23']

## Proposition 1.44
**Statement:** To a given straight line to apply, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let AB be the given straight line, C the given triangle, and D the given rectilineal angle. It is required to apply to the given straight line AB, in an angle equal to D, a parallelogram equal to the triangle C.

**Step 2.** By 1.42, construct the parallelogram BEFG equal to the triangle C, in the angle EBG which is equal to D, and so placed that BE is in a straight line with AB. (1.42 produces a parallelogram in a given angle equal to a given triangle on a line bisecting one side of the triangle; we take its base BE collinear with AB and the angle at B equal to D.) Produce FG to H.

**Step 3.** Through the point A draw AH parallel to either BG or EF, by 1.31, meeting the produced line FH at H. Join HB.

**Step 4.** Since the straight line HF falls upon the parallels AH and EF, the angles AHF and HFE are equal to two right angles, by 1.29. Therefore the angles BHG and GFE are less than two right angles (since they are parts of, or equal to less than, those two angles; specifically angle BHG is less than angle AHF, and GFE equals HFE).

**Step 5.** But straight lines produced indefinitely from angles less than two right angles meet, by P5. Therefore HB and FE, being produced in the direction of B and E, will meet. Let them be produced and meet at K.

**Step 6.** Through the point K draw KL parallel to either EA or FH, by 1.31. Produce HA and GB to the points L and M respectively. (Thus HLKF is a parallelogram, HK is its diameter, and AG, ME are parallelograms about HK, while LB and BF are the complements.)

**Step 7.** Then HLKF is a parallelogram, HK its diameter, and AG and ME are parallelograms about HK, while LB and BF are the complements about it. Therefore, by 1.43, the complement LB is equal to the complement BF.

**Step 8.** But BF is equal to the triangle C, by Step 2 and 1.42. Therefore LB is also equal to the triangle C, by CN1.

**Step 9.** Now since the angle GBE is equal to the angle ABM, by 1.15 (these are vertical angles formed by the lines HK... rather, by the straight lines AB, BE and GB, BM crossing at B); and the angle GBE is equal to the angle D; therefore the angle ABM is also equal to the angle D, by CN1.

**Step 10.** Therefore the parallelogram LB has been applied to the given straight line AB, in the angle ABM which is equal to the given angle D, and it is equal to the given triangle C. Therefore to the given straight line AB there has been applied, in the given rectilineal angle D, the parallelogram LB equal to the given triangle C. Q.E.F.

**USED:** 1.15, 1.29, 1.31, 1.42, 1.43, CN1, P5
**Human refs (from References field):** 1.15, 1.29, 1.31, 1.42, 1.43, CN1, P5
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.45
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.

**Step 1.** Let ABCD be the given rectilineal figure and E the given rectilineal angle. It is required to construct, in the angle equal to E, a parallelogram equal to the rectilineal figure ABCD. (For definiteness we treat ABCD as a quadrilateral; the same procedure, repeated, handles any rectilineal figure.)

**Step 2.** Join DB (P1). The figure ABCD is thereby divided into the two triangles ABD and DBC.

**Step 3.** Construct the parallelogram FH equal to the triangle ABD, in the angle HKF equal to the given angle E (1.42).

**Step 4.** To the straight line GH apply the parallelogram GM equal to the triangle DBC, in the angle GHM equal to the given angle E (1.44), placing it so that GM lies alongside FH on GH.

**Step 5.** Since each of the angles HKF and GHM was made equal to the same angle E, they are equal to one another (CN1).

**Step 6.** Add the angle KHG to each. Then the angles FKH, KHG are equal to the angles KHG, GHM (CN2).

**Step 7.** But FKH, KHG are equal to two right angles, since KF and HG are the opposite sides of the parallelogram FH and KH falls on the parallels KF, HG, making the interior angles on the same side equal to two right angles (1.34, 1.29). Therefore KHG, GHM are also equal to two right angles (CN1).

**Step 8.** Thus, with the straight line GH, and at the point H on it, the two straight lines KH and HM, not lying on the same side, make the adjacent angles KHG, GHM equal to two right angles. Therefore KH is in a straight line with HM (1.14).

**Step 9.** Since the straight line HG falls on the parallels KM and FG, the alternate angles MHG, HGF are equal to one another (1.29).

**Step 10.** Add the angle HGL to each. Then the angles MHG, HGL are equal to the angles HGF, HGL (CN2).

**Step 11.** But the angles MHG, HGL are equal to two right angles, since HM and GL are opposite sides of the parallelogram GM and HG falls on them, making the interior angles on the same side equal to two right angles (1.34, 1.29). Therefore the angles HGF, HGL are also equal to two right angles (CN1).

**Step 12.** Thus, with the straight line HG, and at the point G on it, the two straight lines FG and GL, not lying on the same side, make the adjacent angles HGF, HGL equal to two right angles. Therefore FG is in a straight line with GL (1.14).

**Step 13.** Now FK is parallel and equal to HG, since FH is a parallelogram (1.34); and HG is parallel and equal to ML, since GM is a parallelogram (1.34). Therefore KF is equal to ML and parallel to ML (CN1, 1.30).

**Step 14.** And the straight lines KM, FL join them at their extremities; therefore KM, FL are themselves also equal and parallel (1.33). Hence KFLM is a parallelogram.

**Step 15.** The parallelogram FH was constructed equal to the triangle ABD, and the parallelogram GM equal to the triangle DBC. Adding equals to equals, the whole parallelogram KFLM is equal to the whole figure ABCD (CN2).

**Step 16.** Therefore the parallelogram KFLM has been constructed equal to the given rectilineal figure ABCD, in the angle FKM which is equal to the given angle E. (Should the figure have more than four sides, divide it into further triangles and apply parallelograms to the side GL in succession in the same way, each new piece joining the previous one into a single parallelogram by the same argument.) Therefore the required parallelogram has been constructed. Q.E.F.

**USED:** 1.14, 1.29, 1.30, 1.33, 1.34, 1.42, 1.44, CN1, CN2, P1
**Human refs (from References field):** 1.14, 1.29, 1.30, 1.33, 1.34, 1.42, 1.44, CN1, CN2
**Jaccard:** 0.900 — AI adds ['P1']

## Proposition 1.46
**Statement:** On a given straight line to describe a square.

**Step 1.** Let AB be the given straight line; it is required to describe a square on AB.

**Step 2.** From the point A draw AC at right angles to the straight line AB from the point A on it [1.11], so that angle DAB is a right angle.

**Step 3.** On AC cut off AD equal to AB [1.3], so that AD = AB.

**Step 4.** Through the point D draw DE parallel to AB, and through the point B draw BE parallel to AD [1.31]; let them meet at E. Then ADEB is a parallelogram, since DE is parallel to AB and AD is parallel to BE.

**Step 5.** Therefore AB is equal to DE, and AD is equal to BE, for in a parallelogram the opposite sides are equal to one another [1.34].

**Step 6.** But AB was made equal to AD [Step 3]. Therefore the four straight lines BA, AD, DE, EB are equal to one another: AB = AD, AB = DE (since DE = AB), and AD = BE; hence by combining, BA = AD = DE = EB [CN1]. Therefore the parallelogram ADEB is equilateral.

**Step 7.** I say next that it is also right-angled. For, since the straight line AD falls upon the parallels AB, DE, the angles BAD, ADE are equal to two right angles [1.29].

**Step 8.** But the angle BAD is right [Step 2]; therefore the angle ADE is also right [CN3], subtracting the right angle BAD from the two right angles.

**Step 9.** And in parallelogrammic areas the opposite sides and angles are equal to one another [1.34]; therefore each of the opposite angles ABE, BED is also right: angle ABE equals angle ADE and angle BED equals angle BAD. Therefore all four angles BAD, ADE, DEB, EBA are right.

**Step 10.** Therefore the parallelogram ADEB is right-angled. And it was also proved equilateral [Step 6]. Therefore it is a square [D1.22], and it is described on the straight line AB. Q.E.F.

**USED:** 1.11, 1.29, 1.3, 1.31, 1.34, CN1, CN3, D1.22
**Human refs (from References field):** 1.11, 1.29, 1.31, 1.34
**Jaccard:** 0.500 — AI adds ['1.3', 'CN1', 'CN3', 'D1.22']

## Proposition 1.47
**Statement:** In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.

**Step 1.** Let ABC be a right-angled triangle having the angle BAC right; I say that the square on BC equals the sum of the squares on BA and AC.

**Step 2.** On BC describe the square BDEC, and on BA and AC describe the squares GB and HC respectively (1.46), so that BDEC is the square on the hypotenuse and GFBA, ACKH are the squares on the two sides containing the right angle.

**Step 3.** Since each of the angles BAC and BAG is right (the angle BAC by hypothesis, and BAG because GFBA is a square, by D1.22), the two straight lines AC and AG, drawn from the point A on opposite sides of the line BA, make the adjacent angles equal to two right angles. Therefore CA is in a straight line with AG (1.14). For the same reason BA is also in a straight line with AH.

**Step 4.** Through A draw AL parallel to BD (and to CE), meeting BC in M and DE in L (1.31). Join AD and FC (P1).

**Step 5.** Since each of the angles DBC and FBA is right (being angles of the squares BDEC and GFBA, by D1.22), add to each the angle ABC; then the whole angle DBA equals the whole angle FBC (P4, CN2).

**Step 6.** Now in the triangles ABD and FBC, the two sides DB, BA equal the two sides CB, BF respectively (DB equals CB as sides of the square BDEC, and BA equals BF as sides of the square GFBA, by D1.22), and the contained angle DBA equals the contained angle FBC (Step 5); therefore the base AD equals the base FC, and the triangle ABD equals the triangle FBC (1.4).

**Step 7.** The parallelogram BL (that is, BMLD) is double the triangle ABD, for they have the same base BD and are in the same parallels BD and AL (1.41).

**Step 8.** The square GB (that is, GFBA) is double the triangle FBC, for they have the same base FB and are in the same parallels FB and GC (since GFBA is a square, GC is parallel to FB by D1.22, and CA lies in line AG by Step 3, so C is on that parallel) (1.41).

**Step 9.** Since the triangle ABD equals the triangle FBC (Step 6), and the parallelogram BMLD is double the one while the square GFBA is double the other (Steps 7, 8), the parallelogram BMLD equals the square GFBA (CN1: doubles of equals are equal).

**Step 10.** Similarly, joining AE and BK, and since the angle ACE equals the angle BCK (each being the right angle ACB increased by the right angle of a square, by D1.22, P4, CN2), it is proved in the same way that the parallelogram MLEC equals the square ACKH (using P1, 1.4, 1.41, CN1 as in Steps 6–9).

**Step 11.** Therefore the whole square BDEC, being composed of the parallelogram BMLD and the parallelogram MLEC, equals the sum of the two squares GFBA and ACKH (CN2: adding equals to equals).

**Step 12.** But BDEC is the square on BC, while GFBA and ACKH are the squares on BA and AC. Therefore the square on the side BC subtending the right angle equals the sum of the squares on the sides BA and AC containing the right angle. Therefore in right-angled triangles the square on the side subtending the right angle equals the squares on the sides containing the right angle.

**USED:** 1.14, 1.31, 1.4, 1.41, 1.46, CN1, CN2, D1.22, P1, P4
**Human refs (from References field):** 1.14, 1.4, 1.41, 1.46, CN2
**Jaccard:** 0.500 — AI adds ['1.31', 'CN1', 'D1.22', 'P1', 'P4']

## Proposition 1.48
**Statement:** If in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right.

**Step 1.** Let ABC be a triangle such that the square on BC is equal to the squares on the sides BA, AC. I say that the angle BAC is right.

**Step 2.** From the point A draw AD at right angles to the straight line AC [1.11], and make AD equal to BA [1.3].

**Step 3.** Join DC [P1].

**Step 4.** Since DA is equal to AB, the square on DA is also equal to the square on AB [CN1, the squares on equal straight lines being equal].

**Step 5.** Let the square on AC be added to each. Then the squares on DA, AC are equal to the squares on BA, AC [CN2].

**Step 6.** But, since the angle DAC is right [by construction, Step 2], the square on DC is equal to the squares on DA, AC [1.47].

**Step 7.** And, by hypothesis, the square on BC is equal to the squares on BA, AC.

**Step 8.** Therefore the square on DC is equal to the square on BC, for each is equal to the squares on BA, AC [CN1, using Steps 5, 6, 7].

**Step 9.** Therefore the side DC is also equal to the side BC [for if DC and BC were unequal, the square on the greater would exceed the square on the less, contrary to Step 8].

**Step 10.** Now in the triangles DAC, BAC: DA is equal to AB [Step 2], AC is common to both, and the base DC is equal to the base BC [Step 9]; therefore the angle DAC is equal to the angle BAC [1.8].

**Step 11.** But the angle DAC is right [Step 2]; therefore the angle BAC is also right [CN1].

**Step 12.** Therefore, if in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right. Q.E.D.

**USED:** 1.11, 1.3, 1.47, 1.8, CN1, CN2, P1
**Human refs (from References field):** 1.47, 1.8
**Jaccard:** 0.286 — AI adds ['1.11', '1.3', 'CN1', 'CN2', 'P1']
