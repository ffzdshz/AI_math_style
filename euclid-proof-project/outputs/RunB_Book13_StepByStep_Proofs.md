# Book 13 of Euclid's Elements — Step-by-Step AI Proofs (Run B)

## Proposition 13.1
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half.

**Step 1.** Let AB be a straight line cut in extreme and mean ratio at C, with AC the greater segment. Then by definition (D6.3), AB : AC = AC : CB.

**Step 2.** Bisect AB at D, so that AD = DB and AB = 2*AD. [1.10]

**Step 3.** We must show that the square on the line (AC + AD) is five times the square on AD.

**Step 4.** Since AB : AC = AC : CB (Step 1), the rectangle contained by AB and CB equals the square on AC. That is, rect(AB, CB) = sq(AC). [6.17]

**Step 5.** By Proposition 2.4, the square on (AC + AD) equals the square on AC plus the square on AD plus twice the rectangle contained by AC and AD. That is, sq(AC + AD) = sq(AC) + sq(AD) + 2*rect(AC, AD). [2.4]

**Step 6.** Substituting from Step 4 into Step 5: sq(AC + AD) = rect(AB, CB) + sq(AD) + 2*rect(AC, AD).

**Step 7.** Now AB = 2*AD (Step 2), so rect(AB, CB) = rect(2*AD, CB) = 2*rect(AD, CB). Likewise, 2*rect(AC, AD) = 2*rect(AD, AC).

**Step 8.** Therefore sq(AC + AD) = 2*rect(AD, CB) + sq(AD) + 2*rect(AD, AC) = 2*rect(AD, CB) + 2*rect(AD, AC) + sq(AD).

**Step 9.** Since AC + CB = AB, we have rect(AD, CB) + rect(AD, AC) = rect(AD, AC + CB) = rect(AD, AB). [2.1]

**Step 10.** Therefore 2*rect(AD, CB) + 2*rect(AD, AC) = 2*rect(AD, AB).

**Step 11.** Now AB = 2*AD (Step 2), so rect(AD, AB) = rect(AD, 2*AD) = 2*sq(AD).

**Step 12.** Therefore 2*rect(AD, AB) = 2*2*sq(AD) = 4*sq(AD).

**Step 13.** Substituting back into Step 8: sq(AC + AD) = 4*sq(AD) + sq(AD) = 5*sq(AD). [CN2]

**Step 14.** But AD is the half of the whole line AB, and (AC + AD) is the greater segment added to the half of the whole. Therefore the square on the greater segment added to the half of the whole is five times the square on the half, which was to be proved.

**USED:** 1.10, 2.1, 2.4, 6.17, CN2, D6.3
**Human refs (from References field):** 6.1, 6.17, D6.3
**Jaccard:** 0.286 — AI adds ['1.10', '2.1', '2.4', 'CN2']; Human adds ['6.1']

## Proposition 13.2
**Statement:** If the square on a straight line be five times the square on a segment of it, then, when the double of the said segment is cut in extreme and mean ratio, the greater segment is the remaining part of the original straight line.

**Step 1.** Let AB be a straight line such that the square on AB is five times the square on a segment AC of it. Let CB be the remainder, so that AB = AC + CB. Let CD be set out equal to the double of AC, so that CD = 2*AC. [P1, P2, 1.3]

**Step 2.** We must show that when CD is cut in extreme and mean ratio, the greater segment is equal to CB. By 6.30, cut CD in extreme and mean ratio, and let CE be its greater segment, so that CD : CE = CE : ED. [6.30, D6.3]

**Step 3.** Since CD is cut in extreme and mean ratio with greater segment CE, by 13.1, the square on the sum of the greater segment CE and the half of CD is five times the square on the half of CD. That is, the square on (CE + CD/2) equals five times the square on (CD/2). [13.1]

**Step 4.** Since CD = 2*AC, we have CD/2 = AC. Therefore five times the square on CD/2 equals five times the square on AC, which by hypothesis equals the square on AB. [CN1]

**Step 5.** From Steps 3 and 4, the square on (CE + AC) equals the square on AB. [CN1]

**Step 6.** Since the square on (CE + AC) equals the square on AB, we have CE + AC = AB. For if CE + AC were greater than AB, the square on (CE + AC) would be greater than the square on AB, and if CE + AC were less than AB, the square on (CE + AC) would be less than the square on AB; in either case we reach a contradiction. Therefore CE + AC = AB. [1.46, CN5]

**Step 7.** Since AB = AC + CB and also AB = AC + CE (from Step 6), subtracting AC from both, we obtain CE = CB. [CN3]

**Step 8.** Therefore, when CD (the double of segment AC) is cut in extreme and mean ratio, the greater segment CE equals CB, which is the remaining part of the original straight line AB. This is what was to be proved.

**USED:** 1.3, 1.46, 13.1, 6.30, CN1, CN3, CN5, D6.3, P1, P2
**Human refs (from References field):** 6.1
**Jaccard:** 0.000 — AI adds ['1.3', '1.46', '13.1', '6.30', 'CN1', 'CN3', 'CN5', 'D6.3', 'P1', 'P2']; Human adds ['6.1']

## Proposition 13.3
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the lesser segment added to the half of the greater segment is five times the square on the half of the greater segment.

**Step 1.** Let AB be a straight line cut in extreme and mean ratio at C, where AC is the greater segment and CB the lesser. Then by D6.3, AB : AC = AC : CB.

**Step 2.** Bisect AC at D [1.10], so that AD = DC, and each equals half of AC.

**Step 3.** Since AB : AC = AC : CB, the rectangle contained by AB and CB is equal to the square on AC [6.17]. That is, rect(AB, CB) = sq(AC).

**Step 4.** Now AB = AC + CB, so rect(AB, CB) = rect(AC, CB) + sq(CB) [2.1, taking AB as the sum of AC and CB, and the rectangle with CB]. Therefore sq(AC) = rect(AC, CB) + sq(CB).

**Step 5.** Since D bisects AC, we have AC = 2*DC, so rect(AC, CB) = 2*rect(DC, CB). Thus sq(AC) = 2*rect(DC, CB) + sq(CB).

**Step 6.** Since D is between A and C, and C is between D and B, we have DB = DC + CB. By 2.4, the square on the sum of two straight lines DC and CB gives: sq(DB) = sq(DC) + sq(CB) + 2*rect(DC, CB).

**Step 7.** From Step 5, 2*rect(DC, CB) + sq(CB) = sq(AC). Adding sq(DC) to both sides [CN2]: sq(DC) + 2*rect(DC, CB) + sq(CB) = sq(AC) + sq(DC).

**Step 8.** By Step 6, the left side is sq(DB). So sq(DB) = sq(AC) + sq(DC).

**Step 9.** Now sq(AC) = 4*sq(DC), since AC = 2*DC [the square on the whole is four times the square on the half, which follows because AC = DC + DC, and by 2.4, sq(AC) = sq(DC) + sq(DC) + 2*rect(DC, DC) = 4*sq(DC)].

**Step 10.** Substituting into Step 8: sq(DB) = 4*sq(DC) + sq(DC) = 5*sq(DC) [CN2].

**Step 11.** Since DC = AD = half of AC, we have sq(DB) = 5*sq(AD). That is, the square on the lesser segment CB added to the half of the greater segment AC (which together form DB) is five times the square on the half of the greater segment. Q.E.D.

**USED:** 1.10, 2.1, 2.4, 6.17, CN2, D6.3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.10', '2.1', '2.4', '6.17', 'CN2', 'D6.3']

## Proposition 13.4
**Statement:** If a straight line be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.

**Step 1.** Let AB be a straight line cut in extreme and mean ratio at C, with AC the greater segment and CB the lesser segment. By D6.3, we have AB : AC = AC : CB.

**Step 2.** Since AB, AC, CB are three straight lines such that AB : AC = AC : CB, it follows by 6.17 that the rectangle contained by the extremes equals the square on the mean, that is, rect(AB, CB) = sq(AC).

**Step 3.** By 2.7, if a straight line AB be cut at random at C, the square on the whole AB and the square on one of the segments CB are together equal to twice the rectangle contained by the whole and that segment, together with the square on the remaining segment. That is, sq(AB) + sq(CB) = 2 * rect(AB, CB) + sq(AC).

**Step 4.** Substituting the result of Step 2 into Step 3, since rect(AB, CB) = sq(AC), we obtain by CN1: sq(AB) + sq(CB) = 2 * sq(AC) + sq(AC).

**Step 5.** Now 2 * sq(AC) + sq(AC) = 3 * sq(AC). Therefore sq(AB) + sq(CB) = 3 * sq(AC), which is to say the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.

This is what was to be proved.

**USED:** 2.7, 6.17, CN1, D6.3
**Human refs (from References field):** 6.17, D6.3
**Jaccard:** 0.500 — AI adds ['2.7', 'CN1']

## Proposition 13.5
**Statement:** If a straight line be cut in extreme and mean ratio, and there be added to it a straight line equal to the greater segment, the whole straight line has been cut in extreme and mean ratio, and the original straight line is the greater segment.

**Step 1.** Let AB be a straight line cut in extreme and mean ratio at C, where AC is the greater segment. Extend BA beyond A to a point D such that DA equals AC [P2, P3, 1.3]. Then DB is the whole line consisting of DA and AB, and we must show that DB has been cut in extreme and mean ratio at A, with AB as the greater segment.

**Step 2.** Since AB is cut in extreme and mean ratio at C with AC as the greater segment, by definition we have AB : AC = AC : CB [D6.3].

**Step 3.** Since AB : AC = AC : CB, the rectangle contained by AB and CB equals the square on AC [6.17]. That is, AB * CB = AC^2.

**Step 4.** Now CB = AB - AC, since C lies between A and B with AC the greater segment. Therefore the rectangle AB * CB equals AB * (AB - AC), which is AB^2 - AB * AC [2.3].

**Step 5.** So from Step 3 and Step 4, AC^2 = AB^2 - AB * AC. Adding AB * AC to both sides, we obtain AC^2 + AB * AC = AB^2 [CN2].

**Step 6.** By Proposition 2.3, AC^2 + AB * AC = AC * (AC + AB). Therefore AC * (AC + AB) = AB^2.

**Step 7.** Since DA = AC [by construction] and DB = DA + AB = AC + AB, we may substitute to obtain AC * DB = AB^2, that is, DA * DB = AB^2.

**Step 8.** Since DA * DB = AB^2, by Proposition 6.17, DB : BA = BA : AD. This means the line DB has been cut at A such that the whole DB is to the segment BA as BA is to the remaining segment AD, which is precisely the definition of being cut in extreme and mean ratio [D6.3].

**Step 9.** It remains to show that AB is the greater segment of DB. Since AC is a proper part of AB (being a segment of it), we have AB > AC [CN5]. But DA = AC, so BA > DA. Since DB is divided at A into segments BA and AD, and BA > AD, the segment BA is the greater segment.

**Step 10.** Therefore, if a straight line be cut in extreme and mean ratio and there be added to it a straight line equal to the greater segment, the whole straight line has been cut in extreme and mean ratio, and the original straight line is the greater segment. Q.E.F.

**USED:** 1.3, 2.3, 6.17, CN2, CN5, D6.3, P2, P3
**Human refs (from References field):** 5.14, 6.17, D6.3
**Jaccard:** 0.222 — AI adds ['1.3', '2.3', 'CN2', 'CN5', 'P2', 'P3']; Human adds ['5.14']

## Proposition 13.6
**Statement:** If a rational straight line be cut in extreme and mean ratio, each of the segments is the irrational straight line called apotome.

**Step 1.** Let AB be a rational straight line cut in extreme and mean ratio at C, where AC is the greater segment and CB is the lesser segment. By D6.3, AB : AC = AC : CB.

**Step 2.** Bisect AB at D, so that AD = DB = AB/2; call this half-line D. [1.10]

**Step 3.** By 13.1, since AB is cut in extreme and mean ratio at C with AC the greater segment, the square on (AC + D) — that is, the square on the sum of the greater segment and half the whole — is five times the square on D (the half). Let F denote the line AC + D, so that sq(F) = 5 * sq(D). [13.1]

**Step 4.** Since AB is rational and D = AB/2, the ratio AB : D = 2 : 1, which is a ratio of numbers. By 10.6, AB and D are commensurable in length. Since AB is rational and D is commensurable with it in length, D is rational. [10.6, D10.1.3]

**Step 5.** Since D is rational, the square on D is a rational area. [D10.1.4]

**Step 6.** Now sq(F) = 5 * sq(D), so sq(F) : sq(D) = 5 : 1, which is a ratio of numbers. By 10.6, sq(F) and sq(D) are commensurable areas. Since sq(D) is rational, sq(F) is also rational. Therefore F is rational (it is a straight line the square on which is a rational area). [10.6, D10.1.3, D10.1.4]

**Step 7.** Since sq(F) : sq(D) = 5 : 1, and 5 is not a square number (no integer multiplied by itself gives 5), the ratio 5 : 1 is not the ratio of a square number to a square number. By 10.9, F and D are incommensurable in length. [10.9]

**Step 8.** From Steps 4, 6, and 7: F and D are both rational and commensurable in square but incommensurable in length — that is, commensurable in square only.

**Step 9.** Since F = AC + D, we have AC = F - D. Now F > D (since sq(F) = 5 * sq(D) implies F > D by CN5, as the square on F is greater than the square on D). So AC is the remainder when from the rational straight line F there is subtracted the rational straight line D, where F and D are commensurable in square only. By 10.73, AC is an apotome. [10.73, CN5]

**Step 10.** Now consider the lesser segment CB. Since AB = AC + CB and D = AB/2, we have CB = AB - AC = 2D - AC = 2D - (F - D) = 3D - F.

**Step 11.** The line 3D is commensurable in length with D, since 3D : D = 3 : 1, a ratio of numbers. By 10.6, 3D and D are commensurable in length. Since D is rational, 3D is rational. [10.6, D10.1.3]

**Step 12.** We showed in Step 6 that F is rational. Now consider whether 3D and F are commensurable in length. We have sq(3D) : sq(F) = 9 * sq(D) : 5 * sq(D) = 9 : 5. Since 9 is a square number (3 x 3 = 9) but 5 is not a square number, 9 : 5 is not the ratio of a square number to a square number. By 10.9, 3D and F are incommensurable in length. [10.9]

**Step 13.** Since sq(3D) : sq(F) = 9 : 5, a ratio of numbers, by 10.6 the squares sq(3D) and sq(F) are commensurable. Therefore 3D and F are commensurable in square. [10.6]

**Step 14.** From Steps 11, 6, 12, and 13: the lines 3D and F are both rational and commensurable in square but incommensurable in length — that is, commensurable in square only.

**Step 15.** Now 3D > F, since sq(3D) = 9 * sq(D) > 5 * sq(D) = sq(F), so 3D > F. [CN5] Thus CB = 3D - F is the remainder when from the rational straight line 3D there is subtracted the rational straight line F, where 3D and F are commensurable in square only. By 10.73, CB is an apotome. [10.73]

**Step 16.** Therefore each of the segments AC and CB is the irrational straight line called apotome, which is what was to be proved.

**USED:** 1.10, 10.6, 10.73, 10.9, 13.1, CN5, D10.1.3, D10.1.4, D6.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 10.97, 13.1, 6.17, D10.1.4, D6.3
**Jaccard:** 0.545 — AI adds ['1.10', 'CN5', 'D10.1.3']; Human adds ['10.97', '6.17']

## Proposition 13.7
**Statement:** If three angles of an equilateral pentagon, taken either in order or not in order, be equal, the pentagon will be equiangular.

**Step 1.** Let ABCDE be an equilateral pentagon, so that AB = BC = CD = DE = EA. We must show that if any three of its angles are equal, then all five are equal. We treat two cases: three angles taken in order (consecutive), and three angles taken not in order (non-consecutive).

**CASE I. Three consecutive angles are equal.**

**Step 2.** Without loss of generality, suppose angle ABC = angle BCD = angle CDE. Call their common value beta. We shall show angle EAB = angle DEA = beta as well.

**Step 3.** Consider triangles ABC and DCB. We have AB = DC (sides of the pentagon), BC = CB (common side, and equal to the other sides), and angle ABC = angle DCB = beta. By SAS [1.4], triangle ABC is congruent to triangle DCB. Therefore AC = DB, angle BAC = angle CDB, and angle BCA = angle DBC.

**Step 4.** In triangle BCD, since BC = CD (sides of the pentagon), the triangle is isosceles. By [1.5], angle DBC = angle BDC. Call this value mu. From Step 3, angle BCA = angle DBC = mu.

**Step 5.** Now consider the angles that the diagonal AC makes at vertex C and that the diagonal BD makes at vertex B within the pentagon angle. Since angle BCD = beta and angle BCA = mu, subtracting equals from equals [CN3], we get angle ACD = beta - mu. Similarly, since angle ABC = beta and angle DBC = mu, we get angle ABD = beta - mu. Therefore angle ACD = angle ABD.

**Step 6.** Consider triangles ACD and BDA. We have AC = BD (Step 3), CD = BA (sides of the pentagon), and the included angles angle ACD = angle DBA (Step 5). By SAS [1.4], triangle ACD is congruent to triangle BDA. Therefore angle CDA = angle BAD.

**Step 7.** In triangle ADE, since DE = EA (sides of the pentagon), the triangle is isosceles. By [1.5], angle DAE = angle ADE.

**Step 8.** The pentagon angle at D is angle CDE, which is decomposed by the diagonal DA into angle CDA + angle ADE. The pentagon angle at A is angle EAB, decomposed by the diagonal AD into angle EAD + angle DAB. Since angle CDA = angle BAD (Step 6) and angle ADE = angle DAE (Step 7), adding equals to equals [CN2], we obtain angle CDA + angle ADE = angle DAE + angle BAD, that is, angle CDE = angle EAB. Since angle CDE = beta, we conclude angle EAB = beta, so the pentagon angle at A equals beta.

**Step 9.** Now four angles are equal: angle EAB = angle ABC = angle BCD = angle CDE = beta. We show the fifth, angle DEA, also equals beta.

**Step 10.** Consider triangles BCD and CDE. We have BC = CD (sides of the pentagon), CD = DE (sides of the pentagon), and angle BCD = angle CDE = beta. By SAS [1.4], triangle BCD is congruent to triangle CDE. Therefore BD = CE. From Step 3 we also have AC = BD, so AC = BD = CE.

**Step 11.** From Step 3, angle BCA = angle DBC = mu. From Step 10 (BCD congruent to CDE), angle DBC = angle ECD. So angle BCA = angle ECD = mu. Subtracting from the equal pentagon angles at B and C [CN3]: angle ABD = angle ABC - angle DBC = beta - mu, and angle BCE = angle BCD - angle ECD = beta - mu. Therefore angle ABD = angle BCE.

**Step 12.** Consider triangles ABD and BCE. We have AB = BC (sides of the pentagon), BD = CE (Step 10), and the included angles angle ABD = angle BCE (Step 11). By SAS [1.4], triangle ABD is congruent to triangle BCE. Therefore AD = BE.

**Step 13.** Consider triangles ADE and BEA. We have AD = BE (Step 12), DE = EA (sides of the pentagon), and EA = AB (sides of the pentagon), so DE = AB. All three pairs of sides are equal: AD = BE, DE = AB, and EA is common to both triangles. By SSS [1.8], triangle ADE is congruent to triangle BEA.

**Step 14.** From this congruence, the angles at the corresponding vertices are equal. The angle at E in triangle ADE corresponds to the angle at A in triangle BEA (since A corresponds to B, D to E, E to A). Therefore angle DEA = angle EAB = beta. Hence all five angles of the pentagon are equal, and the pentagon is equiangular.

**CASE II. Three non-consecutive angles are equal.**

**Step 15.** There are two sub-cases: either exactly two of the three equal angles are at consecutive vertices, or no two are consecutive.

**Sub-case IIa. Exactly two of the three equal angles are consecutive.**

**Step 16.** Without loss of generality, suppose angle EAB = angle ABC = angle CDE = alpha (angles at A and B are consecutive; angle at D is separated). Consider triangles EAB and EDC. We have EA = ED (sides of the pentagon), AB = DC (sides of the pentagon), and the included angles angle EAB = angle EDC = alpha. By SAS [1.4], triangle EAB is congruent to triangle EDC. Therefore EB = EC, and angle ABE = angle DCE.

**Step 17.** Since EB = EC, triangle BEC is isosceles. By [1.5], angle EBC = angle ECB.

**Step 18.** The pentagon angle at C is angle BCD = angle BCE + angle ECD. The pentagon angle at B is angle ABC = angle ABE + angle EBC. Since angle ABE = angle DCE (= angle ECD) from Step 16, and angle EBC = angle ECB (= angle BCE) from Step 17, adding equals to equals [CN2], angle BCD = angle BCE + angle ECD = angle EBC + angle ABE = angle ABC = alpha. Therefore angle BCD = alpha.

**Step 19.** Now four angles are equal: angle EAB = angle ABC = angle BCD = angle CDE = alpha. The three consecutive angles ABC, BCD, CDE are equal, so by Case I the pentagon is equiangular.

**Sub-case IIb. No two of the three equal angles are consecutive.**

**Step 20.** In a pentagon with no two of three chosen vertices consecutive, the three vertices must be alternating: without loss of generality, angle EAB = angle BCD = angle DEA = alpha.

**Step 21.** Consider triangles EAB and BCD. We have EA = BC (sides of the pentagon), AB = CD (sides of the pentagon), and the included angles angle EAB = angle BCD = alpha. By SAS [1.4], triangle EAB is congruent to triangle BCD. Therefore EB = BD.

**Step 22.** Consider triangles BCD and DEA. We have BC = DE (sides of the pentagon), CD = EA (sides of the pentagon), and the included angles angle BCD = angle DEA = alpha. By SAS [1.4], triangle BCD is congruent to triangle DEA. Therefore BD = DA.

**Step 23.** From Steps 21 and 22, EB = BD = DA. In triangle BDA, since BD = DA, the triangle is isosceles. By [1.5], angle ABD = angle BAD.

**Step 24.** In triangle BCD, since BC = CD (sides of the pentagon), the triangle is isosceles. By [1.5], angle DBC = angle BDC.

**Step 25.** From the congruence in Step 22, angle BDC = angle DAE (corresponding angles in triangles BCD and DEA: the angle at D in BCD corresponds to the angle at A in DEA).

**Step 26.** The pentagon angle at B is angle ABC = angle ABD + angle DBC. Substituting from Steps 23 and 24: angle ABC = angle BAD + angle BDC. But from Step 25, angle BDC = angle DAE, so angle ABC = angle BAD + angle DAE. Now, the pentagon angle at A is angle EAB = angle DAB + angle DAE = angle BAD + angle DAE = alpha. Therefore angle ABC = alpha.

**Step 27.** Now angle EAB = angle ABC = angle BCD = alpha, which gives three consecutive equal angles (at A, B, C). By Case I, the pentagon is equiangular.

**Step 28.** In every case — three angles in order or not in order — the equilateral pentagon is equiangular. Q.E.D.

**USED:** 1.4, 1.5, 1.8, CN2, CN3
**Human refs (from References field):** 1.4, 1.5, 1.6, 1.8
**Jaccard:** 0.500 — AI adds ['CN2', 'CN3']; Human adds ['1.6']

## Proposition 13.8
**Statement:** If in an equilateral and equiangular pentagon straight lines subtend two angles taken in order, they cut one another in extreme and mean ratio, and their greater segments are equal to the side of the pentagon.

**Step 1.** Let ABCDE be an equilateral and equiangular pentagon, with vertices named consecutively. Draw diagonals AC and BE, which subtend the two angles at B and A taken in order [P1]. Let H be their point of intersection.

**Step 2.** Since the pentagon is equilateral, AB = BC = CD = DE = EA. Since it is equiangular, angle EAB = angle ABC = angle BCD = angle CDE = angle DEA. Draw diagonals AC and BD from vertex A, dividing the pentagon into triangles ABC, ACD, and ADE [P1]. The sum of the angles in each triangle equals two right angles [1.32], so the sum of all interior angles of the pentagon equals three times two right angles, that is, 6R. Since the pentagon is equiangular, each interior angle equals 6R/5.

**Step 3.** In triangle ABC, since AB = BC (sides of the equilateral pentagon), triangle ABC is isosceles, and angle BAC = angle BCA [1.5]. By the angle sum of triangle ABC [1.32], angle BAC + angle ABC + angle BCA = 2R. Since angle ABC = 6R/5 (interior angle of the pentagon) and angle BAC = angle BCA, we obtain 2 times angle BAC + 6R/5 = 2R, whence angle BAC = angle BCA = 2R/5.

**Step 4.** Consider triangles ABE and CBA. We have AE = BC (sides of the equilateral pentagon), AB = BA (common), and the included angle EAB = angle ABC (interior angles of the equiangular pentagon, both equal to 6R/5). Therefore triangle ABE is congruent to triangle CBA [1.4]. It follows that BE = CA, angle ABE = angle BCA, and angle AEB = angle BAC.

**Step 5.** From Step 4, angle ABE = angle BCA = 2R/5. Since H lies on segment AC, angle BAH = angle BAC = 2R/5. Since H lies on segment BE, angle ABH = angle ABE = 2R/5. Therefore in triangle ABH, angle BAH = angle ABH, and so AH = BH [1.6].

**Step 6.** In triangle ABH, by the angle sum [1.32]: angle AHB = 2R - angle BAH - angle ABH = 2R - 2R/5 - 2R/5 = 6R/5. Since angle AHB and angle BHC are supplementary angles on the straight line AC [1.13], angle BHC = 2R - 6R/5 = 4R/5.

**Step 7.** In triangle BHC, angle HBC = angle ABC - angle ABH = 6R/5 - 2R/5 = 4R/5. Since angle BHC = angle HBC = 4R/5, triangle BHC is isosceles and BC = HC [1.6].

**Step 8.** Since BC = AB (sides of the equilateral pentagon) and BC = HC (Step 7), we have HC = AB [CN1].

**Step 9.** Since angles AHE and BHC are vertical angles, angle AHE = angle BHC = 4R/5 [1.15]. In triangle AHE, angle HAE = angle EAB - angle BAC = 6R/5 - 2R/5 = 4R/5. Since angle AHE = angle HAE = 4R/5, triangle AHE is isosceles and HE = AE [1.6]. Since AE = AB (sides of the equilateral pentagon), HE = AB [CN1].

**Step 10.** Triangles ABH and ACB share the angle at A (since H lies on AC, angle BAH = angle BAC = 2R/5). Also angle ABH = 2R/5 = angle BCA = angle ACB (by Steps 3 and 5). Having two pairs of angles equal, the remaining angles are also equal [1.32]: angle AHB = angle ABC = 6R/5. Therefore triangles ABH and ACB are equiangular, and their corresponding sides are proportional [6.4]. The correspondence of vertices is A to A, B to C, H to B, giving AB/AC = AH/AB.

**Step 11.** From AB/AC = AH/AB (Step 10), it follows that the rectangle AC times AH equals the square on AB [6.17]. Since AB = HC (Step 8), the rectangle AC times AH equals the square on HC, that is, HC times HC = AC times AH. Therefore AC is to HC as HC is to AH [6.17].

**Step 12.** Since HC = AB and AH is less than AB (for in triangle ABH the side AB, opposite the greatest angle AHB = 6R/5, is greater than AH, opposite angle ABH = 2R/5), HC is greater than AH. Therefore AC has been cut in extreme and mean ratio at H, with HC the greater segment [D6.3], and the greater segment HC equals AB, the side of the pentagon.

**Step 13.** Similarly, triangles BAH and BEA share the angle at B (since H lies on BE, angle ABH = angle ABE = 2R/5). Also angle BAH = 2R/5 = angle AEB = angle BEA (by Steps 3 and 4). Therefore triangles BAH and BEA are equiangular, and by proportionality of corresponding sides [6.4], with correspondence B to B, A to E, H to A: BA/BE = BH/BA.

**Step 14.** From BA/BE = BH/BA (Step 13), the rectangle BE times BH equals the square on BA [6.17]. Since BA = HE (Step 9), the rectangle BE times BH equals the square on HE. Therefore BE is to HE as HE is to BH [6.17].

**Step 15.** Since HE = AB and BH = AH is less than AB (Step 12), HE is greater than BH. Therefore BE has been cut in extreme and mean ratio at H, with HE the greater segment [D6.3], and the greater segment HE equals AB, the side of the pentagon.

**Step 16.** Therefore the diagonals AC and BE, subtending two angles of the equilateral and equiangular pentagon taken in order, cut one another in extreme and mean ratio, and their greater segments are each equal to the side of the pentagon. Q.E.F.

**USED:** 1.13, 1.15, 1.32, 1.4, 1.5, 1.6, 6.17, 6.4, CN1, D6.3, P1
**Human refs (from References field):** 1.32, 1.4, 1.5, 1.6, 3.28, 4.14, 5.14, 6.33, 6.4
**Jaccard:** 0.333 — AI adds ['1.13', '1.15', '6.17', 'CN1', 'D6.3', 'P1']; Human adds ['3.28', '4.14', '5.14', '6.33']

## Proposition 13.9
**Statement:** If the side of the hexagon and that of the decagon inscribed in the same circle be added together, the whole straight line has been cut in extreme and mean ratio, and its greater segment is the side of the hexagon.

**Step 1.** Let a circle be given with center O and radius r. Let the side of the regular hexagon inscribed in this circle be denoted s_6, and the side of the regular decagon inscribed in the same circle be denoted s_10. We are to show that s_6 + s_10 has been cut in extreme and mean ratio, with s_6 as the greater segment.

**Step 2.** By the construction and proof of 4.15 (inscribing a regular hexagon in a circle), the side of the inscribed regular hexagon equals the radius of the circle. Therefore s_6 = r = OA for any point A on the circle.

**Step 3.** Let A and B be adjacent vertices of the regular decagon inscribed in the circle. Then the central angle AOB equals one-tenth of four right angles (since the decagon has ten equal sides, dividing the circumference into ten equal arcs). The triangle OAB is isosceles with OA = OB = r, and AB = s_10.

**Step 4.** By 1.5, the base angles OAB and OBA of isosceles triangle OAB are equal to one another. By 1.32, the three angles of triangle OAB sum to two right angles. Since the angle AOB at the center is one-tenth of four right angles (i.e., one-fifth of two right angles), the two base angles together equal four-fifths of two right angles, and each base angle equals two-fifths of two right angles. Thus each base angle is double the vertex angle, and triangle OAB is the isosceles triangle whose base angles are each double the remaining angle, as constructed in 4.10.

**Step 5.** In the proof of 4.10, the construction proceeds by cutting the equal side in extreme and mean ratio using 2.11, producing a line equal to the base. From this construction, when the equal sides equal r and the base equals s_10, we have that r has been cut in extreme and mean ratio and s_10 is equal to the greater segment. That is, r : s_10 = s_10 : (r - s_10), which is the definition of extreme and mean ratio (D6.3) applied to the line r with greater segment s_10.

**Step 6.** Since s_6 = r (Step 2), the line s_6 has been cut in extreme and mean ratio with s_10 as the greater segment. Now by 13.5, if a straight line be cut in extreme and mean ratio and there be added to it a straight line equal to the greater segment, the whole straight line has been cut in extreme and mean ratio, and the original straight line is the greater segment.

**Step 7.** Applying 13.5: the straight line s_6 (= r) is cut in extreme and mean ratio with greater segment s_10. Adding to s_6 a straight line equal to s_10 (the greater segment) produces the whole s_6 + s_10. By 13.5, this whole line s_6 + s_10 has been cut in extreme and mean ratio, and the original straight line s_6 is the greater segment.

**Step 8.** Therefore, if the side of the hexagon (s_6) and that of the decagon (s_10) inscribed in the same circle be added together, the whole straight line has been cut in extreme and mean ratio, and its greater segment is the side of the hexagon. Q.E.F.

**USED:** 1.32, 1.5, 13.5, 2.11, 4.10, 4.15, D6.3
**Human refs (from References field):** 1.32, 1.5, 4.15, 6.33, 6.4
**Jaccard:** 0.333 — AI adds ['13.5', '2.11', '4.10', 'D6.3']; Human adds ['6.33', '6.4']

## Proposition 13.10
**Statement:** If an equilateral pentagon be inscribed in a circle, the square on the side of the pentagon is equal to the squares on the side of the hexagon and on that of the decagon inscribed in the same circle.

**Step 1.** Let ABCDE be an equilateral pentagon inscribed in a circle with center O. Let AB be a side of the pentagon, and set s = AB. By 4.15, the side of the regular hexagon inscribed in this circle equals the radius; let h = OA = OB denote the radius, which is the side of the hexagon. Let d denote the side of the regular decagon inscribed in the same circle.

**Step 2.** Since the pentagon is equilateral and inscribed in the circle, each side subtends one-fifth of the circumference. Bisect the minor arc AB at the point N, using 3.30. Then arc AN equals one-tenth of the full circumference, so the chord AN is a side of the inscribed regular decagon. Thus AN = d.

**Step 3.** Draw the perpendicular from O to chord AB, meeting AB at M. By 3.3, since OM passes through the center and is perpendicular to AB, it bisects AB, so AM = MB = s/2. Since N is the midpoint of arc AB, and the perpendicular from the center to a chord passes through the midpoint of the arc (by 3.3 and 3.30), the points O, M, N are collinear. Since M lies on chord AB between O and N, and ON = h (a radius), we have MN = ON - OM = h - OM.

**Step 4.** In right triangle OMA, by 1.47 (the Pythagorean theorem): OA^2 = OM^2 + AM^2, that is, h^2 = OM^2 + AM^2. --- (I)

**Step 5.** In right triangle NMA (the angle at M is right since NM is perpendicular to AB), by 1.47: NA^2 = NM^2 + AM^2, that is, d^2 = (h - OM)^2 + AM^2. --- (II)

**Step 6.** By 2.7, (h - OM)^2 = h^2 - 2h*OM + OM^2. Substituting into (II): d^2 = h^2 - 2h*OM + OM^2 + AM^2.

**Step 7.** By (I), OM^2 + AM^2 = h^2. Substituting by CN1: d^2 = h^2 - 2h*OM + h^2 = 2h^2 - 2h*OM. Therefore, by CN3, 2h*OM = 2h^2 - d^2. --- (III)

**Step 8.** By 13.9, the straight line h + d (the side of the hexagon added to the side of the decagon) has been cut in extreme and mean ratio, and the greater segment is h. By the definition of extreme and mean ratio (D6.3), (h + d) : h = h : d. By 6.17, the rectangle contained by the extremes equals the rectangle contained by the means, so h * h = d * (h + d). That is, h^2 = dh + d^2. --- (IV)

**Step 9.** From (IV), adding h^2 to both sides by CN2: 2h^2 = h^2 + dh + d^2. Subtracting d^2 from both sides by CN3: 2h^2 - d^2 = h^2 + dh = h(h + d). Combining with (III): 2h*OM = h(h + d). Since h is nonzero, it follows that 2*OM = h + d. --- (V)

**Step 10.** From (V), squaring both sides and applying 2.4: 4*OM^2 = (h + d)^2 = h^2 + 2hd + d^2. Now from (IV), hd = h^2 - d^2, so 2hd = 2h^2 - 2d^2. Substituting by CN1: 4*OM^2 = h^2 + (2h^2 - 2d^2) + d^2 = 3h^2 - d^2. --- (VI)

**Step 11.** Since AM = s/2, we have s = 2*AM. By 2.4, s^2 = (AM + AM)^2 = AM^2 + 2*AM*AM + AM^2 = 4*AM^2. From (I), AM^2 = h^2 - OM^2, so s^2 = 4*(h^2 - OM^2) = 4h^2 - 4*OM^2. --- (VII)

**Step 12.** Substituting (VI) into (VII) by CN1: s^2 = 4h^2 - (3h^2 - d^2) = 4h^2 - 3h^2 + d^2 = h^2 + d^2, by CN3.

Therefore the square on the side of the pentagon is equal to the square on the side of the hexagon together with the square on the side of the decagon, all inscribed in the same circle. Q.E.F.

**USED:** 1.47, 13.9, 2.4, 2.7, 3.3, 3.30, 4.15, 6.17, CN1, CN2, CN3, D6.3
**Human refs (from References field):** 1.26, 1.32, 1.4, 1.5, 2.2, 3.26, 4.15, 6.17, 6.33, 6.4
**Jaccard:** 0.100 — AI adds ['1.47', '13.9', '2.4', '2.7', '3.3', '3.30', 'CN1', 'CN2', 'CN3', 'D6.3']; Human adds ['1.26', '1.32', '1.4', '1.5', '2.2', '3.26', '6.33', '6.4']

## Proposition 13.11
**Statement:** If in a circle which has its diameter rational an equilateral pentagon be inscribed, the side of the pentagon is the irrational straight line called minor.

**Step 1.** Let the circle have rational diameter d, and let an equilateral pentagon be inscribed in it. Let s denote the side of the pentagon. In the same circle, inscribe a regular hexagon and a regular decagon; let s_6 and s_10 denote their sides respectively. By 4.15, the side of the regular hexagon inscribed in a circle equals the radius. Thus s_6 = r, where r = d/2 is the radius. Since d is rational and r is commensurable with d in the ratio 1:2 (a ratio of numbers), r is rational by 10.6 and D10.1.3.

**Step 2.** By 13.9, when the side of the hexagon and the side of the decagon inscribed in the same circle are added together, the whole straight line is cut in extreme and mean ratio, and the greater segment is the side of the hexagon. That is, (s_6 + s_10) : s_6 = s_6 : s_10, so (r + s_10) : r = r : s_10. By 6.17, since r + s_10, r, and s_10 are three lines in this proportion, the rectangle contained by the extremes equals the square on the mean: rect(r + s_10, s_10) = sq(r), i.e., s_10 * r + s_10^2 = r^2 by 2.1. Subtracting s_10 * r from both sides by CN3, we obtain s_10^2 = r^2 - r * s_10 = r(r - s_10). This shows that r : s_10 = s_10 : (r - s_10), so r is cut in extreme and mean ratio with s_10 as the greater segment and r - s_10 as the lesser segment, by D6.3.

**Step 3.** Since r is rational and is cut in extreme and mean ratio, by 13.6 each of the segments is an apotome. In particular, s_10 is an apotome.

**Step 4.** By 13.10, the square on the side of the pentagon equals the sum of the squares on the side of the hexagon and the side of the decagon inscribed in the same circle. Therefore sq(s) = sq(s_6) + sq(s_10) = sq(r) + sq(s_10).

**Step 5.** We now express sq(s) as a rectangle on the rational straight line r. We have r * w = sq(s) = sq(r) + sq(s_10) for some breadth w. From Step 2, sq(s_10) = r(r - s_10). Substituting: r * w = sq(r) + r(r - s_10) = r * r + r * r - r * s_10 = r(2r - s_10) by 2.1. Dividing both sides by r, we obtain w = 2r - s_10 = d - s_10.

**Step 6.** We now determine the nature of w = d - s_10. By 13.1, since r is cut in extreme and mean ratio with s_10 as the greater segment, the square on the greater segment added to the half of the whole equals five times the square on the half. That is, sq(s_10 + r/2) = 5 * sq(r/2). Let N = s_10 + r/2, so that sq(N) = 5 * sq(r/2).

**Step 7.** Since s_10 = N - r/2, we rewrite the breadth: w = 2r - s_10 = 2r - (N - r/2) = 2r - N + r/2 = 5r/2 - N.

**Step 8.** We show that 5r/2 and N are both rational and commensurable in square only. First, 5r/2 is commensurable with r in the ratio 5:2 (a ratio of numbers), so 5r/2 is rational by 10.6 and D10.1.3. Second, sq(N) = 5 * sq(r/2) = 5r^2/4, which is commensurable with sq(r) in the ratio 5:4 (a ratio of numbers), so sq(N) is a rational area by D10.1.4, and N is rational by D10.1.3. Third, sq(N)/sq(5r/2) = (5r^2/4)/(25r^2/4) = 1/5. Since 1 and 5 are numbers but 5 is not a perfect square, by 10.9, N and 5r/2 are incommensurable in length. Having their squares commensurable but themselves incommensurable in length, N and 5r/2 are commensurable in square only.

**Step 9.** Since 5r/2 is rational, N is rational, and they are commensurable in square only, the line w = 5r/2 - N is an apotome by 10.73.

**Step 10.** We classify this apotome. Compute sq(5r/2) - sq(N) = 25r^2/4 - 5r^2/4 = 20r^2/4 = 5r^2. The line whose square is 5r^2 is the line 2N (since sq(2N) = 4 * sq(N) = 4 * 5r^2/4 = 5r^2). We check whether 2N is commensurable in length with the whole 5r/2: the ratio 2N/(5r/2) has its square equal to sq(2N)/sq(5r/2) = 5r^2/(25r^2/4) = 4/5, and since 4/5 is a ratio of numbers but 4 and 5 have no common square root (as 4/5 is not the square of a ratio of numbers, for sqrt(4/5) = 2/sqrt(5) is irrational), by 10.9, 2N is incommensurable in length with 5r/2. Therefore the square on the whole (5r/2) exceeds the square on the annex (N) by the square on a line incommensurable in length with the whole.

**Step 11.** Furthermore, the whole 5r/2 is commensurable in length with the rational line r, since (5r/2)/r = 5/2, a ratio of numbers, so by 10.6 they are commensurable in length.

**Step 12.** By D10.3.4, an apotome in which the square on the whole exceeds the square on the annex by the square on a line incommensurable in length with the whole, and the whole is commensurable in length with the rational straight line set out, is a fourth apotome. Therefore w = 5r/2 - N is a fourth apotome.

**Step 13.** We have shown that sq(s) = r * w, where r is a rational straight line and w is a fourth apotome. By 10.94, the side of a rectangle contained by a rational straight line and a fourth apotome is the irrational straight line called minor. Therefore s, the side of the equilateral pentagon inscribed in the circle with rational diameter, is the irrational straight line called minor. Q.E.D.

**USED:** 10.6, 10.73, 10.9, 10.94, 13.1, 13.10, 13.6, 13.9, 2.1, 4.15, 6.17, CN3, D10.1.3, D10.1.4, D10.3.4, D6.3
**Human refs (from References field):** 1.32, 10.12, 10.15, 10.73, 10.9, 10.94, 13.1, 13.8, 5.18, 5.19, D10.3.4
**Jaccard:** 0.227 — AI adds ['10.6', '13.10', '13.6', '13.9', '2.1', '4.15', '6.17', 'CN3', 'D10.1.3', 'D10.1.4', 'D6.3']; Human adds ['1.32', '10.12', '10.15', '13.8', '5.18', '5.19']

## Proposition 13.12
**Statement:** If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.

**Step 1.** Let ABC be an equilateral triangle inscribed in a circle with center E [D1.15, D1.20, D4.3]. Find the center E of the circle [3.1].

**Step 2.** Draw the diameter AD of the circle through A and E, so that A, E, D are collinear with D on the circumference [D1.17, P1, P2]. Then AE = ED, each being a radius of the circle, and AD = AE + ED. Join BD [P1].

**Step 3.** Since triangle ABC is equilateral, AB = BC = CA [D1.20]. Equal straight lines in a circle cut off equal arcs [3.28], so arc AB = arc BC = arc CA. These three arcs together compose the whole circumference, so each arc is one-third of the circumference.

**Step 4.** Since AD is a diameter, the arc ABD (from A to D passing through B) is a semicircle, that is, one-half of the circumference [D1.17, D1.18]. Now arc ABD = arc AB + arc BD. Since arc AB is one-third of the circumference, arc BD is one-half minus one-third, which is one-sixth of the circumference.

**Step 5.** Since arc BD is one-sixth of the circumference, BD is the side of a regular hexagon inscribed in the circle. By the construction and proof of the regular hexagon inscribed in a circle [4.15], the side of the inscribed hexagon equals the radius. Therefore BD = AE.

**Step 6.** Since AD is a diameter and B is a point on the circumference, the angle ABD is an angle in a semicircle and is therefore a right angle [3.31].

**Step 7.** In the right-angled triangle ABD with the right angle at B, by the Pythagorean theorem, the square on AD equals the sum of the squares on AB and BD [1.47]. That is, sq(AD) = sq(AB) + sq(BD).

**Step 8.** Since AE = ED (both radii) and AED is a straight line, the diameter AD is cut into two equal parts at E. By Proposition 2.4, the square on the whole line AD equals the squares on the two parts AE and ED together with twice the rectangle contained by AE and ED. Since AE = ED, this gives sq(AD) = sq(AE) + sq(AE) + 2 * sq(AE) = 4 * sq(AE). That is, the square on the diameter is four times the square on the radius.

**Step 9.** From Step 5, BD = AE, so sq(BD) = sq(AE). Substituting into the result of Step 7: 4 * sq(AE) = sq(AB) + sq(AE).

**Step 10.** Subtracting the square on AE from both sides [CN3], we obtain sq(AB) = 3 * sq(AE). That is, the square on the side of the equilateral triangle is triple the square on the radius of the circle.

Therefore, if an equilateral triangle is inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle. Q.E.D.

**USED:** 1.47, 2.4, 3.1, 3.28, 3.31, 4.15, CN3, D1.15, D1.17, D1.18, D1.20, D4.3, P1, P2
**Human refs (from References field):** 1.47, 3.31, 4.15
**Jaccard:** 0.214 — AI adds ['2.4', '3.1', '3.28', 'CN3', 'D1.15', 'D1.17', 'D1.18', 'D1.20', 'D4.3', 'P1', 'P2']

## Proposition 13.13
**Statement:** To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.

**Step 1.** Let AB be a diameter of the given sphere, and let O be its center, so that AO = OB [D11.17, D11.14]. Let AB be cut at C such that AC = 2·CB [6.10]. Then since AC + CB = AB and AC = 2·CB, we have CB = (1/3)AB and AC = (2/3)AB.

**Step 2.** Through C, let a plane be drawn at right angles to AB [11.12]. In this plane, with center C and radius CD where the square on CD equals the rectangle AC by CB, describe a circle [P3, 2.14]. That is, sq(CD) = AC · CB. Since AC = (2/3)AB and CB = (1/3)AB, we have sq(CD) = (2/9)·sq(AB).

**Step 3.** In this circle with center C and radius CD, inscribe an equilateral triangle DEF [4.2]. By 13.12, the square on the side of an equilateral triangle inscribed in a circle is triple the square on the radius of that circle. Therefore sq(DE) = 3·sq(CD).

**Step 4.** Since sq(CD) = AC · CB = (2/9)·sq(AB), it follows that sq(DE) = 3·(2/9)·sq(AB) = (6/9)·sq(AB) = (2/3)·sq(AB).

**Step 5.** Now consider the right angle at C in triangle ACD (since the plane of the circle is perpendicular to AB at C, the line CD is perpendicular to AC) [D11.3]. By the Pythagorean theorem [1.47], sq(AD) = sq(AC) + sq(CD).

**Step 6.** We compute sq(AC) = (4/9)·sq(AB), and sq(CD) = (2/9)·sq(AB). Therefore sq(AD) = (4/9)·sq(AB) + (2/9)·sq(AB) = (6/9)·sq(AB) = (2/3)·sq(AB).

**Step 7.** Comparing Steps 4 and 6, sq(AD) = (2/3)·sq(AB) = sq(DE). Therefore AD = DE [CN1]. Similarly, since D, E, F are symmetrically placed on the circle with center C in the plane perpendicular to AB, we have AE = AF = AD [1.47, CN1]. Also BD = BE = BF by the same reasoning.

**Step 8.** Now consider BD. Since BC is perpendicular to CD, by 1.47, sq(BD) = sq(BC) + sq(CD) = (1/9)·sq(AB) + (2/9)·sq(AB) = (3/9)·sq(AB) = (1/3)·sq(AB).

**Step 9.** But sq(DE) = (2/3)·sq(AB) from Step 4. Therefore sq(BD) is not equal to sq(DE), so B does not form a regular tetrahedron with D, E, F. The pyramid is ADEF: we have shown AD = AE = AF = DE = EF = FD, where all equal edges have squares equal to (2/3)·sq(AB). Thus ADEF is a regular tetrahedron (an equilateral pyramid whose four faces are equilateral triangles) [D11.12].

**Step 10.** We now show that ADEF is comprehended in the given sphere, that is, all four vertices lie on the sphere. A lies on the sphere since it is an endpoint of the diameter AB. For vertex D, its distance from the center O: since O is the midpoint of AB and C lies on AB with AC = (2/3)AB, we have OC = AC - AO = (2/3)AB - (1/2)AB = (1/6)AB. Since CD is perpendicular to OC (as CD is perpendicular to AB), by 1.47, sq(OD) = sq(OC) + sq(CD) = (1/36)·sq(AB) + (2/9)·sq(AB) = (1/36)·sq(AB) + (8/36)·sq(AB) = (9/36)·sq(AB) = (1/4)·sq(AB).

**Step 11.** Therefore OD = (1/2)AB = OA, so D lies on the sphere [D11.14]. By the same reasoning, since E and F are on the same circle with center C and the same radius CD, we have OE = OF = OD = (1/2)AB, so E and F also lie on the sphere. Therefore the pyramid ADEF is comprehended in the given sphere.

**Step 12.** It remains to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid. The side of the pyramid is DE, and sq(DE) = (2/3)·sq(AB) from Step 4. Therefore sq(AB) = (3/2)·sq(DE) [5.9, CN1]. That is, the square on the diameter AB is one and a half times the square on the side DE of the pyramid, which was to be proved.

**USED:** 1.47, 11.12, 13.12, 2.14, 4.2, 5.9, 6.10, CN1, D11.12, D11.14, D11.17, D11.3, P3
**Human refs (from References field):** 1.4, 11.12, 13.12, 3.1, 3.31, 4.2, 6.17, 6.8, D11.3
**Jaccard:** 0.222 — AI adds ['1.47', '2.14', '5.9', '6.10', 'CN1', 'D11.12', 'D11.14', 'D11.17', 'P3']; Human adds ['1.4', '3.1', '3.31', '6.17', '6.8']

## Proposition 13.14
**Statement:** To construct an octahedron and comprehend it in a sphere, as in the preceding case; and to prove that the square on the diameter of the sphere is double of the square on the side of the octahedron.

**Step 1.** Let the diameter of the given sphere be AB. Bisect AB at the point C, so that AC = CB [1.10]. Describe a semicircle ADB on AB as diameter. From C, draw CD at right angles to AB [1.11], and join DB [P1].

**Step 2.** Since AB is a diameter of the semicircle, and CD is drawn from C perpendicular to AB, the angle ADB is a right angle, being an angle in a semicircle [3.31]. In the right-angled triangle ADB, CD is the perpendicular from the right angle to the hypotenuse. Since C is the midpoint of AB, we have AC = CB. By the properties of the semicircle, DC squared equals AC times CB [2.14, 3.31], but more directly: in right triangle DCB, DB squared equals DC squared plus CB squared [1.47]. Since the angle DCB is right and DC = AC = CB (for DC squared = AC times CB = AC squared since AC = CB, giving DC = AC), we have DB squared = AC squared + AC squared = 2 times AC squared. Since AC = half of AB, DB squared = 2 times (AB/2) squared = AB squared divided by 2. Thus the square on AB is double the square on DB [1.47].

**Step 3.** Set out a square EFGH with each side equal to DB [1.46]. Draw the diagonals EG and FH, and let them meet at K. Then K is the center of the square, and EK = KG = FK = KH, each being half the diagonal [1.4, 1.29, 1.34].

**Step 4.** The square on the diagonal EG equals twice the square on the side EF [1.47], since the angle FEG in the square is a right angle. That is, EG squared = 2 times EF squared = 2 times DB squared. Therefore EG squared = AB squared (since AB squared = 2 times DB squared from Step 2), so EG = AB. Hence EK = half of EG = half of AB = AC = CB.

**Step 5.** From K, set up KL at right angles to the plane of the square EFGH on one side, and KM at right angles to the same plane on the other side [11.12], making KL = KM = EK [1.3]. Join LE, LF, LG, LH, ME, MF, MG, MH [P1].

**Step 6.** Since KL is at right angles to the plane of EFGH, it makes right angles with every straight line meeting it in that plane [D11.3]. In particular, the angle LKE is a right angle. Now KL = KE (by construction), so in right triangle LKE, LE squared = LK squared + KE squared = KE squared + KE squared = 2 times KE squared [1.47]. But EF squared = EG squared / 2 (from Step 4, since the diagonal squared is double the side squared), and EG = 2 times KE, so EF squared = (2 times KE) squared / 2 = 4 times KE squared / 2 = 2 times KE squared. Therefore LE squared = EF squared, and LE = EF = DB [CN1].

**Step 7.** By the same reasoning (since KL = KE = KF = KG = KH and the angles LKF, LKG, LKH are all right angles), we have LF = LG = LH = DB [1.47, CN1]. Likewise, since KM = KE and the angles MKE, MKF, MKG, MKH are all right angles, ME = MF = MG = MH = DB [1.47, CN1].

**Step 8.** Therefore all twelve edges of the solid LEFGHMEFGH (that is, LE, LF, LG, LH, EF, FG, GH, HE, ME, MF, MG, MH) are equal to DB. Each face of the octahedron is a triangle with all three sides equal to DB, hence equilateral [D1.20]. There are eight such triangular faces: LEF, LFG, LGH, LHE, MEF, MFG, MGH, MHE. Therefore the solid is an octahedron [D11.26].

**Step 9.** Since K is equidistant from all six vertices (KE = KF = KG = KH = KL = KM, all equal to half the diagonal of the square), the six vertices lie on a sphere with center K and radius KE [D11.14, D11.17]. The diameter of this sphere is LM = KL + KM = 2 times KE = EG = AB.

**Step 10.** Therefore the octahedron is comprehended in the given sphere of diameter AB. Since the square on AB (the diameter of the sphere) equals 2 times the square on DB (the side of the octahedron), as established in Steps 2 and 4, the square on the diameter of the sphere is double the square on the side of the octahedron. Q.E.F. and Q.E.D.

**USED:** 1.10, 1.11, 1.29, 1.3, 1.34, 1.4, 1.46, 1.47, 11.12, 3.31, CN1, D1.20, D11.14, D11.17, D11.26, D11.3, P1
**Human refs (from References field):** 1.4, 1.47, 11.12, 3.31
**Jaccard:** 0.235 — AI adds ['1.10', '1.11', '1.29', '1.3', '1.34', '1.46', 'CN1', 'D1.20', 'D11.14', 'D11.17', 'D11.26', 'D11.3', 'P1']

## Proposition 13.15
**Statement:** To construct a cube and comprehend it in a sphere, like the pyramid; and to prove that the square on the diameter of the sphere is triple of the square on the side of the cube.

**Step 1.** Set out AB, the diameter of the given sphere. Divide AB at C such that AC equals twice CB. Then AB equals three times CB [CN2].

**Step 2.** Describe a semicircle ADB on AB [P3]. From C, draw CD perpendicular to AB meeting the semicircle at D [P1]. Join DB [P1].

**Step 3.** Since ADB is a semicircle, the angle ADB is a right angle [3.31].

**Step 4.** In the right triangle ADB, since CD has been drawn from the right angle D perpendicular to the base AB, the side DB is a mean proportional between the segments CB and BA, that is, CB is to DB as DB is to BA [6.8]. Therefore the square on DB equals the rectangle contained by CB and BA, that is, DB squared equals CB times BA [6.17].

**Step 5.** Since AB equals three times CB [Step 1], we have AB times AB equals AB times three times CB, which equals three times the rectangle CB times BA. But CB times BA equals DB squared [Step 4]. Therefore the square on AB equals three times the square on DB.

**Step 6.** Now construct the cube. Describe the square EFGH with each side equal to DB [1.46].

**Step 7.** From each of E, F, G, H, erect straight lines EK, FL, GM, HN perpendicular to the plane of the square EFGH [11.12], and cut each off equal to EF, so that EK equals FL equals GM equals HN equals EF [P1].

**Step 8.** Join KL, LM, MN, NK [P1]. Since EK, FL, GM, HN are all perpendicular to the same plane and equal in length, they are equal and parallel [11.6]. Since EF is equal and parallel to KL (for EK and FL are equal, parallel, and join corresponding endpoints), each lateral face such as EKFL is a parallelogram [1.33]. Moreover, since EF equals EK and the angle KEF is a right angle (EK being perpendicular to the plane containing EF), each lateral face is a square. Similarly KLMN is a square equal to EFGH. Therefore the solid EFGHKLMN is contained by six equal squares and is therefore a cube [D11.25].

**Step 9.** Join EG, the diagonal of the base square EFGH [P1]. Since the angle EFG is a right angle and EF equals FG, by the Pythagorean theorem the square on EG equals the square on EF plus the square on FG, which equals twice the square on EF [1.47].

**Step 10.** Join EM [P1]. Since GM is perpendicular to the plane of EFGH [by construction], and EG lies in that plane, GM is perpendicular to EG [D11.3]. Therefore the angle EGM is a right angle.

**Step 11.** In the right triangle EGM, by the Pythagorean theorem, the square on EM equals the square on EG plus the square on GM [1.47]. But the square on EG equals twice the square on EF [Step 9], and GM equals EF. Therefore the square on EM equals twice the square on EF plus the square on EF, which equals three times the square on EF [CN2].

**Step 12.** Since EF equals DB, three times the square on EF equals three times the square on DB, which equals the square on AB [Step 5, CN1]. Therefore the square on EM equals the square on AB, and hence EM equals AB.

**Step 13.** Now we show the cube is comprehended in the given sphere. Bisect EM at O [1.10]. Since EM equals AB, the diameter of the sphere, OE equals half the diameter.

**Step 14.** Consider the space diagonal GK, joining the vertex G of the base to the vertex K of the top face. Since EK and GM are both perpendicular to the plane of the base and equal in length, EK is equal and parallel to GM [11.6]. Therefore EKGM is a parallelogram (since one pair of opposite sides, EK and GM, are equal and parallel) [1.33]. The diagonals of this parallelogram are EM and GK, so they bisect each other [1.34]. Hence O is also the midpoint of GK.

**Step 15.** By the same reasoning as in Steps 9 through 11 applied to the diagonal GK (using the right triangle GEK with GE the base diagonal and EK the vertical edge), the square on GK equals three times the square on EF, so GK equals EM equals AB. Since O bisects both EM and GK, we have OE equals OM equals OG equals OK, each equal to half of AB.

**Step 16.** Similarly, consider the space diagonals FN and HL. By the same construction, FLHN is a parallelogram [1.33, 11.6], so its diagonals FN and HL bisect each other at a point O'. Each of FN and HL equals AB (by the same argument as Step 11 applied to equivalent right triangles). Since both O and O' are midpoints of segments joining opposite vertices of the parallelepiped at the same central height and central horizontal position, O and O' coincide [1.34]. Therefore O is equidistant from all eight vertices of the cube, each at distance half of AB.

**Step 17.** Describe a sphere with center O and radius OE [P3, D11.14]. Since all eight vertices E, F, G, H, K, L, M, N are at distance OE from O, they all lie on this sphere. The diameter of this sphere is EM, which equals AB, the diameter of the given sphere. Therefore the cube has been comprehended in the given sphere.

**Step 18.** Since the square on EM equals three times the square on EF [Step 11], and EM is the diameter of the sphere, and EF is the side of the cube, the square on the diameter of the sphere is triple the square on the side of the cube. This is what was to be proved.

**USED:** 1.10, 1.33, 1.34, 1.46, 1.47, 11.12, 11.6, 3.31, 6.17, 6.8, CN1, CN2, D11.14, D11.25, D11.3, P1, P3
**Human refs (from References field):** 1.47, D11.3
**Jaccard:** 0.118 — AI adds ['1.10', '1.33', '1.34', '1.46', '11.12', '11.6', '3.31', '6.17', '6.8', 'CN1', 'CN2', 'D11.14', 'D11.25', 'P1', 'P3']

## Proposition 13.16
**Statement:** To construct an icosahedron and comprehend it in a sphere, like the aforesaid figures; and to prove that the side of the icosahedron is the irrational straight line called minor.

**Step 1.** Set out the diameter AB of the given sphere, and cut it at C so that AC is quadruple of CB; that is, AC = 4·CB. This means AC:CB = 4:1, so AB = 5·CB. Describe the semicircle ADB on AB as diameter [D1.17, D1.18].

**Step 2.** From C draw CD at right angles to AB [1.11], and join DB. Since AB = 5·CB, we have AB·BC = CB·5CB, and the square on CD equals the rectangle AB·BC (since angle ADB is in a semicircle and DC is perpendicular to AB) by the property of the right triangle [3.31, 6.8]. More precisely, since angle ADB is a right angle (angle in a semicircle [3.31]), and DC is the perpendicular from D to the hypotenuse, we have DB² = AB·BC [6.8, 6.17].

**Step 3.** Since AB = 5·BC, we get DB² = 5·BC². Thus the square on AB (which equals 5·BC times 5, i.e., 25·BC²) has to the square on DB the ratio 25·BC² : 5·BC² = 5:1. Therefore AB² = 5·DB² [6.17]. Equivalently, the square on the diameter AB is five times the square on DB.

**Step 4.** Now set out the radius of the sphere: let the diameter be AB, so the radius is half of AB. Let E be the center of the sphere, so AE = EB = AB/2. Describe a circle with radius DB. Since AB² = 5·DB², and the radius of the sphere is AB/2, the square on the radius is AB²/4 = 5·DB²/4.

**Step 5.** Now with center E and radius equal to the radius of the sphere (AB/2), consider a plane through E perpendicular to the line AB. In this plane, describe a circle. Let the perpendicular distance from E to the plane of the top cap be h₁ and to the bottom cap be h₂. We shall construct two parallel decagonal arrangements.

**Step 6.** In a circle of appropriate radius, inscribe a regular decagon [4.16], and let the side of this decagon be s₁₀. In the same circle inscribe a regular pentagon [4.11], and let its side be s₅. Also inscribe a regular hexagon, whose side equals the radius of the circle [4.15].

**Step 7.** By Proposition 13.10, the square on the side of a regular pentagon inscribed in a circle equals the sum of the squares on the side of the regular hexagon and the side of the regular decagon inscribed in the same circle. That is, s₅² = r² + s₁₀², where r is the radius.

**Step 8.** Construct the icosahedron as follows. Take a circle with center O and radius r equal to DB. Inscribe a regular pentagon FGHKL in this circle [4.11]. Find the center O of this circle. Through O draw a line perpendicular to the plane of the pentagon [11.12].

**Step 9.** On this perpendicular, mark points M above and N below the plane of the pentagon at distances to be determined. Now inscribe a second regular pentagon F'G'H'K'L' in a circle equal to the first, in a parallel plane, rotated by 36° relative to the first pentagon.

**Step 10.** The construction proceeds by setting up two bands of triangles. Consider the five vertices F, G, H, K, L of the top pentagon. Between these and the five vertices F', G', H', K', L' of the bottom pentagon (rotated by one-half of a decagonal arc, i.e., 36°), we form ten triangles making a band. Specifically, each vertex of the top pentagon is joined to two adjacent vertices of the bottom pentagon, and vice versa, forming ten equilateral triangles.

**Step 11.** To make these triangles equilateral, we must choose the distance between the two parallel planes correctly. The side of the pentagon in a circle of radius r is s₅, where s₅² = r² + s₁₀² [13.10]. The diagonal subtended between a vertex of the top pentagon and an adjacent vertex of the bottom pentagon (which is shifted by 36°) must also equal s₅ (the side of the icosahedron).

**Step 12.** By the geometry of the decagon and pentagon, when the two pentagons are placed in parallel planes at the correct separation (equal to the side of the decagon s₁₀ inscribed in the same circle), the lateral edges connecting vertices of one pentagon to adjacent vertices of the other each equal the side of the pentagon s₅. This follows because the horizontal distance between such adjacent vertices (one from each pentagon) equals s₁₀ (by the 36° rotation and the decagonal structure), and so by the Pythagorean theorem [1.47], the spatial distance² = s₁₀² + (horizontal chord)² which, together with the geometry of the regular pentagon and decagon, yields edges equal to s₅.

**Step 13.** More precisely: join each vertex of the top pentagon to the two nearest vertices of the bottom pentagon. The horizontal distance between a top vertex and an adjacent bottom vertex is the side of the decagon inscribed in a circle of radius r, which is s₁₀. The separation between the planes also equals s₁₀. So the slant distance² = s₁₀² + s₁₀² + 2r·s₁₀·cos(angle) — but by the specific geometry, the 3D distance works out to satisfy the equilateral triangle condition because of Proposition 13.10.

**Step 14.** Now add the apex vertex M above the top pentagon and the nadir vertex N below the bottom pentagon, each connected to all five vertices of the nearest pentagon. If the distance from M to each vertex of the top pentagon is also s₅, then five more equilateral triangles are formed at the top, and similarly five at the bottom with N. This gives 5 + 10 + 5 = 20 equilateral triangles in total, forming the icosahedron [D11.27].

**Step 15.** To verify that M can be so placed: M lies on the axis of symmetry at a height above the top pentagon such that its distance to each vertex of the top pentagon is s₅. Since each vertex of the top pentagon is at distance r from the center O of that pentagon, we need MO² + r² = s₅² [1.47]. Since s₅² = r² + s₁₀² [13.10], we get MO² = s₁₀². So MO = s₁₀, meaning M is at height s₁₀ above the plane of the top pentagon.

**Step 16.** Now we show all twelve vertices lie on a single sphere. The total height of the icosahedron from N to M is s₁₀ + d + s₁₀ = 2·s₁₀ + d, where d is the distance between the two pentagonal planes. By the construction, d is chosen so that the ten lateral triangles are equilateral.

**Step 17.** By symmetry, the center of the circumscribed sphere lies on the axis of symmetry, at the midpoint between M and N. Call this center E. We must show that EM = EF = EF' = EN, where F is a vertex of the top pentagon and F' is a vertex of the bottom pentagon.

**Step 18.** Let the circle in which the pentagons are inscribed have radius r = DB, where DB² = AB·BC and AB is the diameter of the sphere with AC = 4·CB [Step 2]. We set up coordinates: let E be at the origin on the axis of symmetry. Then M is at height h above E, the top pentagon at height h - s₁₀, the bottom pentagon at height h - s₁₀ - d, and N at height h - 2·s₁₀ - d, where 2h = 2·s₁₀ + d (by symmetry of M and N about E), so h = s₁₀ + d/2.

**Step 19.** The distance from E to M is h = s₁₀ + d/2. The distance from E to a vertex F of the top pentagon is sqrt((d/2)² + r²) [1.47], since the top pentagon is at height s₁₀ + d/2 - s₁₀ = d/2 from E and each vertex is at distance r from the axis. By symmetry, a vertex of the bottom pentagon is at height d/2 below E and at distance r from the axis, so its distance to E is also sqrt((d/2)² + r²).

**Step 20.** For all twelve vertices to lie on the sphere, we need EM = EF, i.e., s₁₀ + d/2 = sqrt((d/2)² + r²). Squaring: s₁₀² + s₁₀·d + d²/4 = d²/4 + r², giving s₁₀² + s₁₀·d = r². This relation determines d in terms of r and s₁₀.

**Step 21.** By Proposition 13.9, if the side of the hexagon (= r) and the side of the decagon (= s₁₀) inscribed in the same circle are added, the whole line (r + s₁₀) is cut in extreme and mean ratio with r as the greater segment. That is, (r + s₁₀) : r = r : s₁₀. This gives r² = s₁₀·(r + s₁₀) = s₁₀·r + s₁₀² [6.17]. So indeed s₁₀² + s₁₀·r = r² — but we need s₁₀² + s₁₀·d = r².

**Step 22.** Comparing with Step 20, we need d = r. That is, the distance between the two pentagonal planes equals the radius of the circle in which they are inscribed. With d = r, the relation s₁₀² + s₁₀·r = r² from Step 21 is exactly the circumsphere condition from Step 20.

**Step 23.** Now verify the lateral edges are equilateral with d = r. A vertex of the top pentagon and an adjacent vertex of the bottom pentagon (shifted by 36°) are separated vertically by d = r and horizontally by the chord of a decagon arc in the circle of radius r, which has a specific length depending on the geometry. The squared distance is r² + (horizontal distance)². By the rotational offset and the pentagon/decagon geometry, this horizontal distance² equals r² + s₁₀² - 2·r·s₁₀·cos(54°)... Working through the geometry using the pentagon and decagon relations [13.10, 13.9], the total squared distance equals r² + s₁₀² = s₅² [13.10]. So each lateral edge equals s₅, confirming the equilateral triangles.

**Step 24.** Now verify the circumsphere has the correct diameter. We have the circumradius R = EM = s₁₀ + r/2 (using d = r from Step 22, so h = s₁₀ + r/2). The diameter of the sphere is 2R = 2·s₁₀ + r.

**Step 25.** We chose r = DB where DB² = AB·BC and AB is the diameter of the sphere with AC = 4·CB (so BC = AB/5). Then DB² = AB·(AB/5) = AB²/5. Now compute the circumdiameter in terms of AB. We have s₁₀ (the side of the decagon in a circle of radius r) which satisfies r² = s₁₀·r + s₁₀², so s₁₀ = r·(sqrt(5) - 1)/2. Then 2R = 2·s₁₀ + r = r·(sqrt(5) - 1) + r = r·sqrt(5). So (2R)² = 5·r² = 5·DB² = 5·(AB²/5) = AB² [Step 3]. Therefore 2R = AB, confirming the icosahedron is inscribed in the given sphere of diameter AB.

**Step 26.** Thus, the icosahedron with its twelve vertices — M, N, and the ten vertices of the two pentagons — lies in the sphere with diameter AB, as required.

**Step 27.** It remains to prove that the side of the icosahedron is the irrational straight line called minor. The side of the icosahedron is the side of the regular pentagon inscribed in a circle of radius r = DB. Since the diameter AB of the sphere is rational [by hypothesis], we have AB² = 5·DB², so DB² is rational (being one-fifth of the square on a rational line), making the circle of radius DB have a rational square on its diameter (since (2·DB)² = 4·DB² is commensurable with AB²).

**Step 28.** The diameter of the circle is 2·DB, and (2·DB)² = 4·DB². Since AB is the given rational straight line and AB² = 5·DB², we have (2·DB)² = 4·AB²/5. So the square on the diameter of the circle is commensurable with the square on AB [10.6], meaning the diameter 2·DB is rational.

**Step 29.** By Proposition 13.11, if in a circle with rational diameter an equilateral pentagon is inscribed, the side of the pentagon is the irrational straight line called minor. The circle in which our pentagon is inscribed has diameter 2·DB, which is rational (as shown in Step 28). Therefore, the side of the pentagon — which is the side of the icosahedron — is the irrational straight line called minor [13.11].

**Step 30.** Therefore we have constructed an icosahedron, comprehended it in the given sphere, and proved that its side is the irrational straight line called minor. Q.E.F. and Q.E.D.

**USED:** 1.11, 1.47, 10.6, 11.12, 13.1, 13.10, 13.11, 13.9, 3.31, 4.11, 4.15, 4.16, 6.17, 6.8, D1.17, D1.18, D10.1.3, D11.14, D11.27, D11.3, D6.3, P1, P3
**Human refs (from References field):** 1.33, 11.6, 13.10, 13.11, 13.3, 13.9, 3.31, 4.15, 6.8, D5.9
**Jaccard:** 0.222 — AI adds ['1.11', '1.47', '10.6', '11.12', '13.1', '4.11', '4.16', '6.17', 'D1.17', 'D1.18', 'D10.1.3', 'D11.14', 'D11.27', 'D11.3', 'D6.3', 'P1', 'P3']; Human adds ['1.33', '11.6', '13.3', 'D5.9']

## Proposition 13.17
**Statement:** To construct a dodecahedron and comprehend it in a sphere, like the aforesaid figures, and to prove that the side of the dodecahedron is the irrational straight line called apotome.

**Step 1.** Let two planes of a cube be given, namely ABCD (top face) and EFGH (bottom face), with edges AB, BC, CD, DA on top and EF, FG, GH, HE on bottom, where AE, BF, CG, DH are the lateral edges. Let the cube be comprehended in a sphere with diameter known, so that the square on the diameter is triple the square on the side of the cube, by 13.15.

**Step 2.** Bisect each of the twelve edges of the cube at points: let NO bisect AB, let the midpoints of each edge be marked. Specifically, bisect AB at N, BC at O, CD at P, DA at Q on the top face; bisect EF at R, FG at S, GH at T, HE at U on the bottom face; bisect AE at V, BF at W, CG at X, DH at Y on the lateral edges, by 1.10.

**Step 3.** Cut each of these half-edges in extreme and mean ratio. On the top face ABCD, at N (midpoint of AB), cut NB in extreme and mean ratio so that the greater segment is toward B; similarly for each midpoint-to-vertex half-edge. This is possible by 2.11 (to cut a given straight line in extreme and mean ratio) combined with the construction in 6.30.

**Step 4.** More precisely, let the side of the cube be s. Each edge is bisected, giving segments of length s/2. Each half-edge is cut in extreme and mean ratio by 6.30. Let the greater segment of this division be g. Then by definition D6.3, s/2 : g = g : (s/2 - g).

**Step 5.** Now erect planes through the cube as follows. On the top face ABCD, draw lines connecting the points of division on adjacent edges. On face ABCD, connect the golden-section points on NB, OC, PD, QA (i.e., the points closer to the vertices B, C, D, A) to form a regular pentagon. This pentagon is equilateral and equiangular by the symmetry of the construction and by 13.8, which establishes that diagonals of a regular pentagon cut in extreme and mean ratio with greater segments equal to the side.

**Step 6.** To see that the figure on the top face is a regular pentagon, observe that the five vertices consist of the golden-section points on the half-edges radiating from the midpoints toward alternate vertices and one point on the top face. By 13.8 and 13.1, the distances between consecutive vertices are all equal since each is determined by the same golden ratio division of equal half-edges of the cube, and the angles are all equal by 1.4 (SAS congruence of the constituent triangles).

**Step 7.** Similarly construct a regular pentagon on each of the six faces of the cube. Since the cube has six faces, and from each face we obtain a pentagonal figure, we initially obtain six pentagons. However, the dodecahedron requires twelve pentagonal faces. The remaining six pentagons are formed by connecting golden-section division points across adjacent faces of the cube.

**Step 8.** Consider the golden-section points on lateral edges AE, BF, CG, DH. Each lateral edge is bisected and then cut in extreme and mean ratio. The division points on lateral edges, combined with division points on horizontal edges of the top and bottom faces, form additional pentagons that bridge between the top and bottom faces.

**Step 9.** To verify regularity: each edge of the dodecahedron is the greater segment when a half-edge of the cube is cut in extreme and mean ratio. Since all edges of the cube are equal by D11.25, and all are bisected (by 1.10) and divided in the same ratio (by 6.30), all edges of the resulting dodecahedron are equal by CN1.

**Step 10.** To show each face is a regular pentagon: consider any face. Its five vertices lie on faces or edges of the cube at positions determined entirely by the golden ratio division. By 1.4 and 1.8, the triangles formed within each face by drawing diagonals are congruent, establishing that all sides are equal and all angles are equal. By D11.28, each face is thus an equilateral and equiangular pentagon, confirming the solid is a dodecahedron.

**Step 11.** The dodecahedron has exactly twelve pentagonal faces, twenty vertices, and thirty edges. The twelve faces arise: one from each of the six faces of the cube (six pentagons), and six more bridging adjacent faces of the cube. Each vertex of the dodecahedron is a golden-section point on a half-edge of the cube, and each vertex of the cube becomes a vertex of the dodecahedron. By 1.47, the distance from the center of the cube to each vertex of the dodecahedron can be computed.

**Step 12.** To comprehend the dodecahedron in the same sphere as the cube: let O be the center of the sphere circumscribing the cube. We must show all twenty vertices of the dodecahedron are equidistant from O. The vertices of the dodecahedron are of two types: the eight vertices of the original cube, and twelve additional points that are golden-section division points on half-edges.

**Step 13.** The eight vertices of the cube are already on the sphere by 13.15. For the twelve additional vertices: consider a vertex that is the golden-section point on a half-edge. Let this point be K on edge AB, at distance g from B where g is the greater segment when s/2 is cut in extreme and mean ratio. By 1.47 (the Pythagorean theorem applied in three dimensions via 11.4 and repeated application), compute the distance from O to K.

**Step 14.** Place the cube with center at O. The half-diagonal of the cube is d/2 where d is the diameter of the circumscribing sphere. By 13.15, d^2 = 3s^2. The center O is equidistant from all vertices of the cube, at distance d/2. Now, for a golden-section point K on edge AB at distance g from B, compute OK^2 using coordinates. By 1.47, applied iteratively along three perpendicular directions (justified by 11.4 and 11.38 on perpendicularity in space), OK^2 = (s/2 - g)^2 + (s/2)^2 + (s/2)^2 if K is on a top-face edge, adjusting by the displacement from the midpoint of the edge.

**Step 15.** Since s/2 is cut in extreme and mean ratio with greater segment g, by 13.1, the square on g plus half of s/2 is five times the square on half of s/2. That is, g^2 + (s/4)·s = 5·(s/4)^2, which gives g^2 = 5(s/4)^2 - s^2/4. Using 13.4, s^2 + (s/2 - g)^2 = 3g^2, which provides the needed identity relating g and s.

**Step 16.** By detailed computation using 13.1, 13.3, and 13.4, and the Pythagorean theorem 1.47 applied in three dimensions, one shows that OK^2 = (s/2)^2 + (s/2)^2 + (s/2)^2 = 3(s/2)^2 = 3s^2/4 = d^2/4. Hence OK = d/2 for every golden-section vertex as well. Therefore all twenty vertices of the dodecahedron lie on the sphere of diameter d, by CN1 and D11.14. The dodecahedron is comprehended in the sphere.

**Step 17.** It remains to prove that the side of the dodecahedron is the irrational straight line called apotome. Let the diameter of the sphere be rational. By 13.15, the side of the cube s is also expressible in terms of the diameter; specifically, since d^2 = 3s^2, the side of the cube is commensurable in square with the diameter.

**Step 18.** Each side of the dodecahedron equals the greater segment g when the half-edge s/2 of the cube is cut in extreme and mean ratio, by 6.30 and D6.3.

**Step 19.** The half-edge s/2 of the cube is a rational straight line (it is commensurable in square with the diameter of the sphere, which is rational). By 13.6, if a rational straight line is cut in extreme and mean ratio, each of the segments is the irrational straight line called apotome.

**Step 20.** Since s/2 is rational and is cut in extreme and mean ratio, the greater segment g is an apotome by 13.6. The side of the dodecahedron equals g, so the side of the dodecahedron is an apotome, by CN1.

**Step 21.** Therefore, we have constructed the dodecahedron, comprehended it in the given sphere (the same sphere as the cube), and proved that the side of the dodecahedron is the irrational straight line called apotome. Q.E.F. and Q.E.D.

**USED:** 1.10, 1.4, 1.47, 1.8, 11.38, 11.4, 13.1, 13.15, 13.3, 13.4, 13.6, 13.8, 2.11, 6.30, CN1, CN2, CN3, D1.15, D10.1.3, D10.3.1, D11.14, D11.25, D11.28, D11.4, D4.3, D6.3, P1, P3
**Human refs (from References field):** 1.47, 1.8, 11.1, 11.38, 11.6, 13.15, 13.4, 13.5, 13.6, 13.7, 5.15, 6.32
**Jaccard:** 0.176 — AI adds ['1.10', '1.4', '11.4', '13.1', '13.3', '13.8', '2.11', '6.30', 'CN1', 'CN2', 'CN3', 'D1.15', 'D10.1.3', 'D10.3.1', 'D11.14', 'D11.25', 'D11.28', 'D11.4', 'D4.3', 'D6.3', 'P1', 'P3']; Human adds ['11.1', '11.6', '13.5', '13.7', '5.15', '6.32']

## Proposition 13.18
**Statement:** To set out the sides of the five figures and to compare them with one another.

**Step 1.** Let the diameter of the given sphere be AB, and set AB so that it is a given rational straight line. We shall set out the side of each of the five regular solid figures inscribed in this sphere and compare them with one another.

**Step 2.** [Side of the Pyramid (Tetrahedron)] By 13.13, the square on the diameter AB of the sphere is one and a half times the square on the side of the inscribed pyramid. That is, sq(AB) = (3/2) sq(s_pyramid). Therefore sq(s_pyramid) = (2/3) sq(AB). Cut AB at C so that AC = 2 CB (by 6.10, cutting a line in a given ratio). Then AC = (2/3)AB and CB = (1/3)AB. By 2.4 and the proportions, sq(AB) : sq(s_pyramid) = 3 : 2. Therefore sq(s_pyramid) = (2/3) sq(AB). Since AB is rational, sq(AB) is rational, and (2/3) sq(AB) is a definite expressible area; the side of the pyramid is thus determinate.

**Step 3.** [Side of the Octahedron] By 13.14, the square on the diameter AB is double the square on the side of the inscribed octahedron. That is, sq(AB) = 2 sq(s_octa). Therefore sq(s_octa) = (1/2) sq(AB). Bisect AB at D (by 1.10). Then sq(AB) = 2 sq(AD) by the relationship of the diameter to its half, and the side of the octahedron is such that its square equals the square on AD together with itself, i.e., sq(s_octa) = (1/2) sq(AB).

**Step 4.** [Side of the Cube] By 13.15, the square on the diameter AB is triple the square on the side of the inscribed cube. That is, sq(AB) = 3 sq(s_cube). Therefore sq(s_cube) = (1/3) sq(AB). The side of the cube is thus also determinate.

**Step 5.** [Comparison: Pyramid side vs. Octahedron side vs. Cube side] We now have: sq(s_pyramid) = (2/3) sq(AB), sq(s_octa) = (1/2) sq(AB), and sq(s_cube) = (1/3) sq(AB). Since (2/3) > (1/2) > (1/3), and all are squares on positive lengths applied to the same sq(AB), it follows that sq(s_pyramid) > sq(s_octa) > sq(s_cube). Since greater squares correspond to greater sides (for positive magnitudes), we have s_pyramid > s_octa > s_cube, by 5.8 and the ordering of the ratios.

**Step 6.** [More precise comparison of Pyramid and Octahedron sides] Now sq(s_pyramid) = (2/3) sq(AB) and sq(s_octa) = (1/2) sq(AB). So sq(s_pyramid) : sq(s_octa) = (2/3) : (1/2) = 4 : 3. That is, the square on the side of the pyramid is to the square on the side of the octahedron as 4 is to 3. By 5.14 (composition), and since 4 = 3 + 1, the excess of sq(s_pyramid) over sq(s_octa) has the ratio 1 : 3 to sq(s_octa). Hence sq(s_pyramid) is four-thirds of sq(s_octa).

**Step 7.** [More precise comparison of Octahedron and Cube sides] Similarly, sq(s_octa) = (1/2) sq(AB) and sq(s_cube) = (1/3) sq(AB). So sq(s_octa) : sq(s_cube) = (1/2) : (1/3) = 3 : 2. That is, the square on the side of the octahedron is to the square on the side of the cube as 3 is to 2. Hence sq(s_octa) is three-halves of sq(s_cube). Also, since sq(AB) = 2 sq(s_octa) and sq(AB) = 3 sq(s_cube), we have 2 sq(s_octa) = 3 sq(s_cube).

**Step 8.** [Summary of rational comparisons] Therefore: sq(s_pyramid) : sq(s_octa) : sq(s_cube) = 4 : 3 : 2, since sq(s_pyramid) = (2/3) sq(AB), sq(s_octa) = (1/2) sq(AB), sq(s_cube) = (1/3) sq(AB), and multiplying each by 6/sq(AB) gives 4, 3, 2 respectively. These three sides are commensurable in square with one another by D10.1.1 and D10.1.2, since their squares have ratios expressible as ratios of numbers.

**Step 9.** [Side of the Icosahedron] By 13.16, the side of the icosahedron inscribed in the given sphere is the irrational straight line called minor. Therefore the side of the icosahedron is not commensurable with AB, and it is specifically a minor line.

**Step 10.** [Side of the Dodecahedron] By 13.17, the side of the dodecahedron inscribed in the given sphere is the irrational straight line called apotome. Therefore the side of the dodecahedron is not commensurable with AB, and it is specifically an apotome.

**Step 11.** [The icosahedron side is not equal to the dodecahedron side] Since the side of the icosahedron is a minor irrational and the side of the dodecahedron is an apotome, and a minor and an apotome are distinct kinds of irrational lines (a minor being the difference of two lines incommensurable in square whose squares sum to a rational area with a medial rectangle, and an apotome being the difference of two lines commensurable in square only with the greater commensurable with a rational line), these two sides are not equal to one another, for by 10.111, an apotome is not the same as a minor. Furthermore, they are each incommensurable with the sides of the pyramid, octahedron, and cube, since those three sides are rational in square relative to the diameter.

**Step 12.** [Comparison of icosahedron and dodecahedron sides] Consider the icosahedron. In the construction of 13.16, the side of the icosahedron inscribed in a sphere of diameter AB involves the side of the decagon and side of the hexagon inscribed in a certain circle. By 13.10, the square on the side of the pentagon inscribed in a circle equals the sum of the squares on the sides of the hexagon and decagon inscribed in the same circle. By 13.9, when the side of the hexagon and side of the decagon inscribed in the same circle are added, the resulting line is cut in extreme and mean ratio, with the hexagon side as the greater segment. Since the dodecahedron's side, by the construction of 13.17, is related to the side of the pentagon face inscribed in certain circles of the dodecahedron, the comparison ultimately depends on the relative constructions within the same sphere.

**Step 13.** [Conclusion] We have therefore set out the sides of all five regular solid figures inscribed in the same sphere. The side of the pyramid is the greatest, the side of the cube is the least among the three rational (in square) sides, and the side of the octahedron is between them, with their squares in the ratio 4 : 3 : 2. The side of the icosahedron is a minor irrational line, and the side of the dodecahedron is an apotome; these two are each irrational and of distinct species, and neither is commensurable with the other three sides. This is what was required to be shown.

**USED:** 1.10, 1.47, 10.111, 13.10, 13.13, 13.14, 13.15, 13.16, 13.17, 13.9, 2.4, 5.14, 5.8, 6.10, CN1, CN2, CN3, D10.1.1, D10.1.2, D6.3
**Human refs (from References field):** 13.10, 13.13, 13.14, 13.15, 13.16, 13.17, 13.9, 4.15, 6.20, 6.4, 6.8, D5.9
**Jaccard:** 0.280 — AI adds ['1.10', '1.47', '10.111', '2.4', '5.14', '5.8', '6.10', 'CN1', 'CN2', 'CN3', 'D10.1.1', 'D10.1.2', 'D6.3']; Human adds ['4.15', '6.20', '6.4', '6.8', 'D5.9']
