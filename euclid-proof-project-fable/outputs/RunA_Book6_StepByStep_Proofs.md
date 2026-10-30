# Book 6 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 6.1
**Statement:** Triangles and parallelograms which are under the same height are to one another as their bases.

## Proposition 6.1
**Statement:** Triangles and parallelograms which are under the same height are to one another as their bases.

**Step 1.** (Setting out.) Let ABC, ACD be triangles and EC, CF parallelograms under the same height, the height of a figure being the perpendicular drawn from the vertex to the base (D6.4). Place them so that the bases BC, CD lie in one straight line BD, the two triangles have the common vertex A, and the parallelograms EC (= EBCA) and CF (= ACDF) stand on the bases BC, CD with their sides EA, AF opposite the bases lying in one straight line EF through A. Since EA is the side of the parallelogram EC opposite to BC, EA is parallel to BC; hence EF is parallel to BD, and each of the four figures has for its height the same perpendicular from EF to BD (D6.4). I say that, as the base BC is to the base CD, so is the triangle ABC to the triangle ACD, and so is the parallelogram EC to the parallelogram CF.

**Step 2.** (Construction.) Produce BD in both directions to points H and L (P2). On the side of B set off, one after another, any number of straight lines BG, GH each equal to the base BC, and on the side of D any number of straight lines DK, KL each equal to the base CD (1.3). Join AG, AH, AK, AL (P1).

**Step 3.** Since CB, BG, GH are equal to one another, and the triangles ABC, AGB, AHG stand on these equal bases in the straight line HL and have their common vertex A on the straight line EF parallel to HL, these triangles are on equal bases and in the same parallels HL, EF; therefore the triangles ABC, AGB, AHG are equal to one another (1.38). For the same reason the triangles ACD, AKD, ALK are equal to one another (1.38).

**Step 4.** The base HC is made up of the segments HG, GB, BC, each equal to BC, so that HC is measured by BC as many times as there are such segments; and the triangle AHC is made up of the triangles AHG, AGB, ABC, each equal to the triangle ABC (Step 3), so that the triangle AHC is measured by the triangle ABC the same number of times. Hence, whatever multiple the base HC is of the base BC, the same multiple is the triangle AHC of the triangle ABC (D5.2). For the same reason, whatever multiple the base LC is of the base CD, the same multiple is the triangle ALC of the triangle ACD (D5.2). Since the number of segments set off on each side in Step 2 was arbitrary, HC and AHC are any equimultiples whatever of BC and ABC, and CL and ACL are any equimultiples whatever of CD and ACD.

**Step 5.** I say next that the triangle AHC exceeds, is equal to, or falls short of the triangle ACL according as the base HC exceeds, is equal to, or falls short of the base CL. (a) If HC is equal to CL, the triangles AHC, ACL stand on equal bases HC, CL and are in the same parallels HL, EF; therefore the triangle AHC is equal to the triangle ACL (1.38). (b) If HC is greater than CL, cut off from HC the straight line CM equal to CL (1.3), M lying between H and C. Then the triangles AMC, ACL stand on equal bases MC, CL in the same parallels HL, EF, so the triangle AMC is equal to the triangle ACL (1.38); but the triangle AHC is greater than the triangle AMC, the whole being greater than the part (CN5); therefore the triangle AHC is greater than the triangle ACL. (c) If HC is less than CL, then, interchanging the roles of HC and CL in (b), the triangle ACL is greater than the triangle AHC, that is, the triangle AHC is less than the triangle ACL.

**Step 6.** There are thus four magnitudes, the two bases BC, CD and the two triangles ABC, ACD; equimultiples HC, AHC have been taken of the first and third, namely of the base BC and the triangle ABC, and other, arbitrary equimultiples CL, ACL of the second and fourth, namely of the base CD and the triangle ACD (Step 4); and it has been proved that, if the multiple HC exceeds the multiple CL, the multiple AHC exceeds the multiple ACL, if equal, equal, and if less, less (Step 5). Therefore, by the definition of magnitudes in the same ratio, as the base BC is to the base CD, so is the triangle ABC to the triangle ACD (D5.5).

**Step 7.** Next, the parallelogram EC has the same base BC with the triangle ABC and is in the same parallels BC, EA; therefore the parallelogram EC is double of the triangle ABC (1.41). Likewise the parallelogram CF has the same base CD with the triangle ACD and is in the same parallels CD, AF; therefore the parallelogram CF is double of the triangle ACD (1.41).

**Step 8.** Since the parallelograms EC, CF are the same multiples (doubles) of the triangles ABC, ACD respectively, taken in corresponding order, and parts have the same ratio as the same multiples of them, as the triangle ABC is to the triangle ACD, so is the parallelogram EC to the parallelogram CF (5.15).

**Step 9.** But as the base BC is to the base CD, so is the triangle ABC to the triangle ACD (Step 6); and ratios which are the same with the same ratio are also the same with one another; therefore, as the base BC is to the base CD, so is the parallelogram EC to the parallelogram CF (5.11).

**Step 10.** Therefore triangles and parallelograms which are under the same height are to one another as their bases. Q.E.D.

*Path note:* In Step 5 the "greater" and "less" cases are established by cutting off a part equal to the smaller base (1.3), applying 1.38 to the part, and using CN5, rather than by asserting them as evident; this is the most direct route from the equal-base case already in hand. The figures are placed in the same parallels in Step 1 because, by D6.4, this is exactly what having the same height amounts to once the bases are laid in one straight line.

**USED:** P1, P2, CN5, D5.2, D5.5, D6.4, 1.3, 1.38, 1.41, 5.11, 5.15

**USED:** 1.3, 1.38, 1.41, 5.11, 5.15, CN5, D5.2, D5.5, D6.4, P1, P2
**Human refs (from References field):** 1.38, 1.41, 5.11, 5.15, D5.5
**Jaccard:** 0.455 — AI adds ['1.3', 'CN5', 'D5.2', 'D6.4', 'P1', 'P2']

## Proposition 6.2
**Statement:** If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section will be parallel to the remaining side of the triangle.

## Proposition 6.2
**Statement:** If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section will be parallel to the remaining side of the triangle.

*Part I.* Let ABC be a triangle, and let DE be drawn parallel to BC, one of its sides, with D on AB and E on AC. I say that BD : DA = CE : EA.

**Step 1.** Join BE and CD [P1].

**Step 2.** The triangles BDE and CDE stand on the same base DE and lie in the same parallels DE, BC, since DE is parallel to BC by hypothesis. Therefore triangle BDE is equal to triangle CDE [1.37].

**Step 3.** ADE is another triangle. Since BDE and CDE are equal, each has the same ratio to ADE; that is, BDE : ADE = CDE : ADE [5.7].

**Step 4.** Triangles BDE and ADE have the common vertex E, and their bases BD and DA lie on the same straight line AB; hence they are under the same height, namely the perpendicular drawn from E to AB [D6.4]. Triangles under the same height are to one another as their bases; therefore BDE : ADE = BD : DA [6.1].

**Step 5.** Likewise triangles CDE and ADE have the common vertex D, and their bases CE and EA lie on the same straight line AC; hence they are under the same height, the perpendicular drawn from D to AC [D6.4]. Therefore CDE : ADE = CE : EA [6.1].

**Step 6.** From Steps 3, 4 and 5, BD : DA = BDE : ADE = CDE : ADE = CE : EA. Ratios which are the same with the same ratio are also the same with one another [5.11]; therefore BD : DA = CE : EA. Thus DE cuts the sides AB and AC of the triangle proportionally.

*Part II.* Now let the sides AB and AC of the triangle ABC be cut proportionally at D and E, so that BD : DA = CE : EA, and let DE be joined. I say that DE is parallel to BC.

**Step 7.** Join DE, and also BE and CD [P1].

**Step 8.** As in Steps 4 and 5, triangles BDE and ADE are under the same height (the perpendicular from E to AB) with bases BD, DA on the one straight line AB, and triangles CDE and ADE are under the same height (the perpendicular from D to AC) with bases CE, EA on the one straight line AC [D6.4]. Therefore BD : DA = BDE : ADE and CE : EA = CDE : ADE [6.1].

**Step 9.** By hypothesis BD : DA = CE : EA. Hence BDE : ADE and CDE : ADE are each the same as this ratio, and so BDE : ADE = CDE : ADE [5.11].

**Step 10.** Magnitudes which have the same ratio to the same magnitude are equal to one another; therefore triangle BDE is equal to triangle CDE [5.9].

**Step 11.** The triangles BDE and CDE are equal, stand on the same base DE, and lie on the same side of it, since B and C both lie on the side of DE remote from A. Equal triangles on the same base and on the same side are in the same parallels [1.39]; therefore DE is parallel to BC.

**Step 12.** Therefore, if a straight line be drawn parallel to one of the sides of a triangle, it cuts the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section is parallel to the remaining side of the triangle. Q.E.D.

**USED:** P1, D6.4, 1.37, 1.39, 5.7, 5.9, 5.11, 6.1

**USED:** 1.37, 1.39, 5.11, 5.7, 5.9, 6.1, D6.4, P1
**Human refs (from References field):** 1.38, 1.39, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.556 — AI adds ['1.37', 'D6.4', 'P1']; Human adds ['1.38']

## Proposition 6.3
**Statement:** If an angle of a triangle be bisected and the straight line cutting the angle cut the base also, the segments of the base will have the same ratio as the remaining sides of the triangle; and, if the segments of the base have the same ratio as the remaining sides of the triangle, the straight line joined from the vertex to the point of section will bisect the angle of the triangle.

**Step 1.** Let ABC be a triangle, and let D be a point of the base BC lying between B and C. First suppose that the straight line AD bisects the angle BAC, so that the angle BAD is equal to the angle DAC. We show that BD : DC = BA : AC.

**Step 2.** Through C draw the straight line CF parallel to DA [1.31], taking F on the same side of BC as A.

**Step 3.** Since the straight line BC falls on the parallels DA and CF, the exterior angle ADB is equal to the interior and opposite angle DCF [1.29].

**Step 4.** In the triangle ABD, the two angles ABD and ADB together are less than two right angles [1.17]. Replacing ADB by the equal angle DCF, the angles ABC and BCF together are less than two right angles.

**Step 5.** Thus the straight line BC, falling on the two straight lines BA and CF, makes the interior angles on the same side (the side of A and F) less than two right angles; therefore BA and CF, produced indefinitely, meet on that side [P5]. Produce BA beyond A [P2] and let it meet CF at the point E. Then A lies between B and E, and E lies on the parallel through C, so that AD is parallel to EC.

**Step 6.** Since the straight line AC falls on the parallels AD and EC, the alternate angles DAC and ACE are equal [1.29].

**Step 7.** Since the straight line BE falls on the parallels AD and EC, the exterior angle BAD is equal to the interior and opposite angle AEC [1.29].

**Step 8.** By hypothesis the angle BAD is equal to the angle DAC. Therefore the angle AEC is equal to the angle ACE, each being equal to the same angle [CN1].

**Step 9.** In the triangle ACE the angles AEC and ACE are equal; the sides subtending them, AC and AE, are therefore equal [1.6].

**Step 10.** In the triangle BCE the straight line AD has been drawn parallel to the side EC, cutting BE at A and BC at D. Therefore it cuts the sides proportionally: BD : DC = BA : AE [6.2].

**Step 11.** Since AE is equal to AC, the same straight line BA has the same ratio to each of them: BA : AE = BA : AC [5.7].

**Step 12.** Therefore, since BD : DC = BA : AE and BA : AE = BA : AC, we have BD : DC = BA : AC [5.11]. This proves the first part.

**Step 13.** Conversely, let the segments of the base be proportional to the remaining sides, BD : DC = BA : AC, and join AD [P1]. We show that AD bisects the angle BAC.

**Step 14.** Make the same construction: through C draw CF parallel to DA [1.31], and produce BA [P2] to meet CF at E. The argument of Steps 3–5 did not use the bisection hypothesis, so it applies unchanged [1.29, 1.17, P5]: BA produced meets CF at a point E with A between B and E, and AD is parallel to EC.

**Step 15.** In the triangle BCE, AD is parallel to the side EC; therefore BD : DC = BA : AE [6.2].

**Step 16.** But by hypothesis BD : DC = BA : AC. Ratios which are the same with the same ratio are the same with one another; therefore BA : AC = BA : AE [5.11].

**Step 17.** Magnitudes to which the same magnitude has the same ratio are equal; therefore AC is equal to AE [5.9].

**Step 18.** In the isosceles triangle ACE, with AC equal to AE, the angles at the base, AEC and ACE, are equal [1.5].

**Step 19.** As in Step 7, the exterior angle BAD is equal to the interior and opposite angle AEC [1.29]; and as in Step 6, the alternate angles DAC and ACE are equal [1.29].

**Step 20.** Therefore the angle BAD is equal to the angle DAC, each being equal to one of two equal angles [CN1]. Hence the straight line AD bisects the angle BAC. This proves the second part, and the proposition is established.

**USED:** 1.17, 1.29, 1.31, 1.5, 1.6, 5.11, 5.7, 5.9, 6.2, CN1, P1, P2, P5
**Human refs (from References field):** 1.29, 1.5, 1.6, 5.11, 5.9, 6.2
**Jaccard:** 0.462 — AI adds ['1.17', '1.31', '5.7', 'CN1', 'P1', 'P2', 'P5']

## Proposition 6.4
**Statement:** In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

## Proposition 6.4
**Statement:** In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

**Step 1.** Let ABC and DCE be equiangular triangles having the angle ABC equal to the angle DCE, the angle BAC equal to the angle CDE, and the angle ACB equal to the angle CED. I say that in the triangles ABC, DCE the sides about the equal angles are proportional, and that the sides subtending the equal angles are the corresponding sides.

**Step 2.** Since both the hypothesis and the conclusion concern only the angles and the sides of the two triangles, let the triangles be so placed that BC and CE lie in one straight line BE, the vertex C being common, and A and D lying on the same side of BE.

**Step 3.** In the triangle ABC the two angles ABC, ACB are together less than two right angles [1.17]. But the angle ACB is equal to the angle CED (hypothesis); therefore the angles ABC, CED are together less than two right angles.

**Step 4.** Now the straight line BE falls on the two straight lines BA, ED, and the interior angles on the same side, namely the angle ABE (which is the angle ABC, since C lies on BE) and the angle BED (which is the angle CED), are together less than two right angles. Therefore BA and ED, if produced [P2], meet on the side on which A and D lie [P5]. Let them be produced and let them meet at F.

**Step 5.** Since the angle DCE is equal to the angle ABC (hypothesis), the straight line BE falling on the two straight lines BF, CD makes the exterior angle DCE equal to the interior and opposite angle ABC on the same side; therefore BF is parallel to CD [1.28].

**Step 6.** Again, since the angle ACB is equal to the angle CED, that is, to the angle FEC (F lying on ED produced), the straight line BE falling on the two straight lines AC, FE makes the exterior angle ACB equal to the interior and opposite angle FEC on the same side; therefore AC is parallel to FE [1.28].

**Step 7.** Therefore FACD is a parallelogram, its opposite sides FA, CD being parallel (Step 5) and its opposite sides AC, FD being parallel (Step 6); hence the opposite sides are equal: FA is equal to CD, and AC is equal to FD [1.34].

**Step 8.** Since AC is parallel to FE, one of the sides of the triangle FBE, and cuts the sides BF, BE at A and C, it cuts them proportionally: as BA is to AF, so is BC to CE [6.2].

**Step 9.** But AF is equal to CD (Step 7); therefore the same magnitude BA has the same ratio to the equal magnitudes AF, CD, that is, as BA is to AF, so is BA to CD [5.7]. And as BA is to AF, so is BC to CE (Step 8); therefore, ratios which are the same with the same ratio being the same with one another, as BA is to CD, so is BC to CE [5.11].

**Step 10.** Therefore, alternately, as AB is to BC, so is DC to CE [5.16].

**Step 11.** Again, since CD is parallel to BF, one of the sides of the triangle FBE, and cuts the sides EB, EF at C and D, it cuts them proportionally: as BC is to CE, so is FD to DE [6.2].

**Step 12.** But FD is equal to AC (Step 7); therefore the equal magnitudes FD, AC have the same ratio to the same magnitude DE, that is, as FD is to DE, so is AC to DE [5.7]. And as BC is to CE, so is FD to DE (Step 11); therefore as BC is to CE, so is AC to DE [5.11].

**Step 13.** Therefore, alternately, as BC is to CA, so is CE to ED [5.16].

**Step 14.** Now there are three magnitudes AB, BC, CA, and three others DC, CE, ED equal to them in multitude, which taken two and two are in the same ratio: as AB is to BC, so is DC to CE (Step 10), and as BC is to CA, so is CE to ED (Step 13). Therefore, ex aequali, as BA is to AC, so is DC to DE [5.22].

**Step 15.** Thus the sides about the equal angles are proportional: about the equal angles ABC, DCE, as AB is to BC, so is DC to CE (Step 10); about the equal angles ACB, CED, as BC is to CA, so is CE to ED (Step 13); and about the equal angles BAC, CDE, as BA is to AC, so is DC to DE (Step 14).

**Step 16.** Moreover, in these proportions the corresponding sides, antecedent answering to antecedent and consequent to consequent [D5.11], are AB and DC, BC and CE, CA and ED. Now AB subtends the angle ACB and DC subtends the equal angle CED; BC subtends the angle BAC and CE subtends the equal angle CDE; CA subtends the angle ABC and ED subtends the equal angle DCE. Therefore the corresponding sides are precisely those which subtend the equal angles.

Therefore, in equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles. Q.E.D.

**USED:** P2, P5, D5.11, 1.17, 1.28, 1.34, 5.7, 5.11, 5.16, 5.22, 6.2

**USED:** 1.17, 1.28, 1.34, 5.11, 5.16, 5.22, 5.7, 6.2, D5.11, P2, P5
**Human refs (from References field):** 1.17, 1.28, 1.34, 5.16, 5.22, 6.2, P5
**Jaccard:** 0.636 — AI adds ['5.11', '5.7', 'D5.11', 'P2']

## Proposition 6.5
**Statement:** If two triangles have their sides proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let ABC, DEF be two triangles having their sides proportional, so that AB : BC = DE : EF, BC : CA = EF : FD, and BA : AC = ED : DF. I say that triangle ABC is equiangular with triangle DEF, and that angle ABC = angle DEF, angle BCA = angle EFD, and angle BAC = angle EDF, these being the angles subtended by the corresponding sides AC and DF, AB and DE, BC and EF respectively.

**Step 2.** On the straight line EF, at the point E on it, construct the angle FEG equal to the angle ABC, and at the point F on it construct the angle EFG equal to the angle ACB, both on the same side of EF [1.23].

**Step 3.** Since ABC, ACB are two angles of the triangle ABC, they are together less than two right angles [1.17]; hence the angles FEG, EFG, which are equal to them, are together less than two right angles, and therefore the straight lines drawn from E and F, if produced, meet on the side of EF on which these angles lie [P5]. Let them meet at G, so that GEF is a triangle.

**Step 4.** In the triangles ABC, GEF, the angle ABC equals the angle GEF and the angle ACB equals the angle GFE (Step 2); and the three angles of each triangle are together equal to two right angles [1.32]; therefore the remaining angle BAC equals the remaining angle EGF. Hence the triangle ABC is equiangular with the triangle GEF.

**Step 5.** In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles [6.4]. Therefore AB : BC = GE : EF (the sides about the equal angles ABC, GEF), and BC : CA = EF : FG (the sides about the equal angles BCA, EFG).

**Step 6.** By hypothesis AB : BC = DE : EF, and by Step 5 AB : BC = GE : EF. Ratios which are the same with the same ratio are also the same with one another [5.11]; therefore DE : EF = GE : EF. But magnitudes which have the same ratio to the same magnitude are equal to one another [5.9]; therefore DE = GE.

**Step 7.** By hypothesis BC : CA = EF : FD, and by Step 5 BC : CA = EF : FG; therefore EF : FD = EF : FG [5.11]. But magnitudes to which the same magnitude has the same ratio are equal to one another [5.9]; therefore FD = FG.

**Step 8.** In the triangles DEF, GEF, the two sides DE, EF are equal to the two sides GE, EF respectively (DE = GE by Step 6, and EF is common), and the base DF is equal to the base GF (Step 7). Therefore the angle DEF, contained by the equal sides DE, EF, is equal to the angle GEF, contained by the equal sides GE, EF [1.8].

**Step 9.** Since DE = GE, EF is common, and the angle DEF equals the angle GEF (Step 8), the triangle DEF is equal to the triangle GEF, and the remaining angles are equal to the remaining angles, namely those which the equal sides subtend [1.4]: the angle EDF equals the angle EGF, and the angle DFE equals the angle GFE.

**Step 10.** Now the angle DEF equals the angle GEF (Step 8), and the angle GEF equals the angle ABC (Step 2); therefore the angle DEF equals the angle ABC [CN1]. Again, the angle DFE equals the angle GFE (Step 9), and the angle GFE equals the angle ACB (Step 2); therefore the angle DFE equals the angle ACB [CN1]. Lastly, the angle EDF equals the angle EGF (Step 9), and the angle EGF equals the angle BAC (Step 4); therefore the angle EDF equals the angle BAC [CN1].

**Step 11.** Therefore the triangle ABC is equiangular with the triangle DEF. Moreover, the angle BAC, subtended by BC, equals the angle EDF, subtended by the corresponding side EF; the angle ABC, subtended by AC, equals the angle DEF, subtended by the corresponding side DF; and the angle ACB, subtended by AB, equals the angle DFE, subtended by the corresponding side DE. Thus the triangles have those angles equal which the corresponding sides subtend. Q.E.D.

**USED:** 1.17, 1.23, 1.32, 1.4, 1.8, 5.11, 5.9, 6.4, CN1, P5
**Human refs (from References field):** 1.23, 1.32, 1.4, 1.8, 5.11, 5.9, 6.4
**Jaccard:** 0.700 — AI adds ['1.17', 'CN1', 'P5']

## Proposition 6.6
**Statement:** If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let ABC, DEF be two triangles having the angle BAC equal to the angle EDF, and the sides about the equal angles proportional, so that BA : AC = ED : DF. We must show that triangle ABC is equiangular with triangle DEF, having the angle ABC equal to the angle DEF and the angle ACB equal to the angle DFE.

**Step 2.** On the straight line DF, at the point D on it, construct the angle FDG equal to the angle BAC, and at the point F on it construct the angle DFG equal to the angle ACB [1.23], the straight lines DG, FG being drawn on the same side of DF and meeting at G. Thus DGF is a triangle.

**Step 3.** Since the angle BAC equals the angle FDG and the angle ACB equals the angle DFG, the remaining angle ABC of triangle ABC equals the remaining angle DGF of triangle DGF [1.32]. Hence triangle ABC is equiangular with triangle DGF.

**Step 4.** In the equiangular triangles ABC, DGF the sides about the equal angles are proportional, and the corresponding sides are those which subtend the equal angles [6.4]. Now BA subtends the angle ACB and GD subtends the equal angle DFG; AC subtends the angle ABC and DF subtends the equal angle DGF. Therefore BA : AC = GD : DF.

**Step 5.** But by hypothesis BA : AC = ED : DF. Since each of the ratios ED : DF and GD : DF is the same as the ratio BA : AC, they are the same as one another: ED : DF = GD : DF [5.11].

**Step 6.** Magnitudes which have the same ratio to the same magnitude are equal; therefore ED = DG [5.9].

**Step 7.** The angle FDG was constructed equal to the angle BAC, and the angle BAC equals the angle EDF by hypothesis; therefore the angle EDF equals the angle GDF [CN1].

**Step 8.** In the triangles DEF, DGF the two sides ED, DF are equal to the two sides GD, DF respectively, and the included angle EDF equals the included angle GDF; therefore the remaining angles equal the remaining angles respectively, namely those which the equal sides subtend [1.4]. Thus the angle DFE, subtended by DE, equals the angle DFG, subtended by the equal side DG; and the angle DEF, subtended by DF, equals the angle DGF, subtended by DF.

**Step 9.** Now the angle DFG equals the angle ACB by construction, and the angle DFG equals the angle DFE by Step 8; therefore the angle ACB equals the angle DFE [CN1].

**Step 10.** Likewise the angle DGF equals the angle ABC by Step 3, and the angle DGF equals the angle DEF by Step 8; therefore the angle ABC equals the angle DEF [CN1].

**Step 11.** Therefore the triangle ABC is equiangular with the triangle DEF: the angle BAC equals the angle EDF (by hypothesis), the angle ABC equals the angle DEF, and the angle ACB equals the angle DFE. Moreover the equal angles are those which the corresponding sides subtend: BC and EF subtend the equal angles at A and D, AC and DF subtend the equal angles at B and E, and AB and DE subtend the equal angles at C and F. Q.E.D.

**USED:** 1.23, 1.32, 1.4, 5.11, 5.9, 6.4, CN1
**Human refs (from References field):** 1.23, 1.32, 1.4, 5.11, 5.9, 6.4
**Jaccard:** 0.857 — AI adds ['CN1']

## Proposition 6.7
**Statement:** If two triangles have one angle equal to one angle, the sides about other angles proportional, and the remaining angles either both less or both not less than a right angle, the triangles will be equiangular and will have those angles equal, the sides about which are proportional.

**Step 1.** Let ABC, DEF be two triangles having the angle BAC equal to the angle EDF, having the sides about the angles ABC, DEF proportional, so that as AB is to BC, so is DE to EF, and having the remaining angles ACB, DFE either both less than a right angle or both not less than a right angle. I say that the angle ABC is equal to the angle DEF, the angle ACB to the angle DFE, and hence that the triangles are equiangular.

**Step 2.** Suppose the angle ABC is not equal to the angle DEF; then one of them is greater. Let the angle ABC be the greater.

**Step 3.** On the straight line AB, and at the point B on it, construct the angle ABG equal to the angle DEF [1.23]. Since the angle DEF, and therefore the angle ABG, is less than the angle ABC, the straight line BG falls within the angle ABC and so meets AC; let it meet AC at G, so that G lies between A and C.

**Step 4.** In the triangles ABG, DEF the angle BAG is equal to the angle EDF by hypothesis, and the angle ABG is equal to the angle DEF by construction. The three angles of each triangle are together equal to two right angles [1.32]; subtracting the equal pairs of angles from these equal sums, the remaining angle AGB is equal to the remaining angle DFE [CN3]. Therefore the triangle ABG is equiangular with the triangle DEF.

**Step 5.** Since the triangles ABG, DEF are equiangular, the sides about the equal angles ABG, DEF are proportional, the corresponding sides being those which subtend the equal angles (AB, DE subtend the equal angles AGB, DFE; BG, EF subtend the equal angles BAG, EDF): therefore as AB is to BG, so is DE to EF [6.4].

**Step 6.** But by hypothesis, as AB is to BC, so is DE to EF. Ratios which are the same with the same ratio are the same with one another; therefore as AB is to BG, so is AB to BC [5.11].

**Step 7.** Since the magnitude AB has the same ratio to each of BG, BC, those magnitudes are equal: therefore BG is equal to BC [5.9].

**Step 8.** Hence in the triangle BGC, since the side BG is equal to the side BC, the angle BGC is equal to the angle BCG [1.5].

**Step 9.** First case: let the angles ACB, DFE be both less than a right angle. Then the angle BCG, which is the angle ACB, is less than a right angle; therefore the angle BGC, being equal to it (Step 8), is also less than a right angle.

**Step 10.** The straight line BG stands on the straight line AC at the point G, so the adjacent angles AGB, BGC are together equal to two right angles [1.13]. Since the angle BGC is less than a right angle, the remaining angle AGB is greater than a right angle.

**Step 11.** But the angle AGB is equal to the angle DFE (Step 4), and the angle DFE is less than a right angle by hypothesis; therefore the angle AGB is less than a right angle. Thus the angle AGB is both greater than and less than a right angle, which is impossible.

**Step 12.** Second case: let the angles ACB, DFE be both not less than a right angle. Then the angle BCG is not less than a right angle; therefore the angle BGC, being equal to it (Step 8), is also not less than a right angle. Hence in the triangle BGC the two angles BGC, BCG are together not less than two right angles. But in any triangle two angles taken together are less than two right angles [1.17]. This is impossible.

**Step 13.** In either case the supposition of Step 2 leads to an impossibility; and if the angle DEF had been supposed the greater, the same construction and argument applied to the triangle DEF would lead to the same impossibility. Therefore the angle ABC is not unequal to the angle DEF; hence it is equal to it.

**Step 14.** Since the angle BAC is equal to the angle EDF and the angle ABC is equal to the angle DEF, and the three angles of each triangle are together equal to two right angles [1.32], the remaining angle ACB is equal to the remaining angle DFE [CN3].

**Step 15.** Therefore the triangles ABC, DEF are equiangular, and they have equal the angles ABC, DEF about which the sides are proportional. Q.E.D.

**USED:** 1.23, 1.32, CN3, 6.4, 5.11, 5.9, 1.5, 1.13, 1.17

**USED:** 1.13, 1.17, 1.23, 1.32, 1.5, 5.11, 5.9, 6.4, CN3
**Human refs (from References field):** 1.13, 1.17, 1.23, 1.32, 1.5, 5.11, 5.9, 6.4
**Jaccard:** 0.889 — AI adds ['CN3']

## Proposition 6.8
**Statement:** If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.

**Step 1.** Let ABC be a right-angled triangle having the angle BAC right, and let AD be the perpendicular drawn from A to the base BC, meeting BC at D. Since AD is perpendicular to BC, each of the adjacent angles ADB, ADC is a right angle (D1.10). I say that each of the triangles ABD, ADC is similar to the whole triangle ABC, and that they are similar to one another.

**Step 2.** First, D lies between B and C. Since the angle BAC is right, each of the angles ABC, ACB is less than a right angle, because any two angles of a triangle are together less than two right angles (1.17). If D coincided with B, then AB itself would be perpendicular to BC and the angle ABC would be right (D1.10), which is impossible. If D fell on CB produced beyond B, then the angle ABD would be an exterior angle of the triangle ABC and so greater than the interior and opposite angle BAC (1.16), that is, greater than a right angle; then the triangle ABD would contain the right angle ADB together with the angle ABD greater than a right angle, two angles together greater than two right angles, contrary to 1.17. In the same way D neither coincides with C nor falls beyond C. Therefore D lies between B and C, and AD divides the triangle ABC into the two triangles ABD, ADC adjoining the perpendicular, the angle ABD being the angle ABC and the angle ACD being the angle ACB.

**Step 3.** Triangle ABC is equiangular with triangle ABD. The angle BAC is equal to the angle ADB, since both are right angles (P4). The angle ABC is common to the two triangles, being the angle ABD. Now the three angles of the triangle ABC are together equal to two right angles, and so are the three angles of the triangle ABD (1.32); subtracting the equal angles BAC, ADB and the common angle at B, the remaining angle ACB is equal to the remaining angle BAD (CN3). Therefore the triangle ABC is equiangular with the triangle ABD, the angles BAC, ABC, ACB being equal respectively to the angles ADB, ABD, BAD.

**Step 4.** In equiangular triangles the sides about the equal angles are proportional, the corresponding sides being those which subtend the equal angles (6.4). In triangle ABC the side BC subtends the right angle BAC, the side AC subtends the angle ABC, and the side AB subtends the angle ACB; in triangle ABD the side BA subtends the right angle ADB, the side AD subtends the angle ABD, and the side BD subtends the angle BAD. Therefore as BC is to BA, so is AC to AD, and so is AB to BD.

**Step 5.** Thus the triangles ABC, ABD have their angles severally equal and the sides about the equal angles proportional; therefore the triangle ABC is similar to the triangle ABD (D6.1).

**Step 6.** Triangle ABC is equiangular with triangle ADC. The angle BAC is equal to the angle ADC, both being right (P4). The angle ACB is common to the two triangles, being the angle ACD. The three angles of each of the triangles ABC, ADC are together equal to two right angles (1.32); subtracting the equal angles BAC, ADC and the common angle at C, the remaining angle ABC is equal to the remaining angle DAC (CN3). Therefore the triangle ABC is equiangular with the triangle ADC, the angles BAC, ACB, ABC being equal respectively to the angles ADC, ACD, DAC.

**Step 7.** By 6.4 the sides about these equal angles are proportional. In triangle ABC the side BC subtends the right angle BAC, the side AB subtends the angle ACB, and the side AC subtends the angle ABC; in triangle ADC the side CA subtends the right angle ADC, the side AD subtends the angle ACD, and the side DC subtends the angle DAC. Therefore as BC is to CA, so is BA to AD, and so is CA to CD.

**Step 8.** Thus the triangles ABC, ADC have their angles severally equal and the sides about the equal angles proportional; therefore the triangle ABC is similar to the triangle ADC (D6.1).

**Step 9.** Triangle ABD is equiangular with triangle ADC. The angle ADB is equal to the angle ADC, both being right (P4). The angle BAD is equal to the angle ACB (Step 3), which is the angle ACD of the triangle ADC. The angle DAC is equal to the angle ABC (Step 6), which is the angle ABD of the triangle ABD. Therefore the triangle ABD is equiangular with the triangle ADC, the angles ADB, ABD, BAD being equal respectively to the angles ADC, DAC, ACD.

**Step 10.** By 6.4 the sides about these equal angles are proportional. In triangle ABD the side AB subtends the right angle ADB, the side AD subtends the angle ABD, and the side BD subtends the angle BAD; in triangle ADC the side AC subtends the right angle ADC, the side DC subtends the angle DAC, and the side AD subtends the angle ACD. Therefore as BA is to AC, so is AD to DC, and so is BD to DA; that is, as BD is to DA, so is DA to DC, and so is BA to AC.

**Step 11.** Thus the triangles ABD, ADC have their angles severally equal and the sides about the equal angles proportional; therefore the triangle ABD is similar to the triangle ADC (D6.1). Hence, in a right-angled triangle, when a perpendicular is drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole triangle and to one another. Q.E.D.

**USED:** 1.16, 1.17, 1.32, 6.4, CN3, D1.10, D6.1, P4
**Human refs (from References field):** 1.32, 6.4, D6.1
**Jaccard:** 0.375 — AI adds ['1.16', '1.17', 'CN3', 'D1.10', 'P4']

## Proposition 6.9
**Statement:** From a given straight line to cut off a prescribed part.

**Step 1.** Let AB be the given straight line, and let the prescribed part be a third part (for any other part the argument is the same, only the number of equal segments laid off in Step 2 changes). From A draw a straight line AG making with AB any angle [P1], and take a point D at random on AG.

**Step 2.** Produce AD beyond D as far as required [P2], and on the produced line cut off DE equal to AD and then EC equal to AD [1.3]. Then DC is made up of DE and EC, each of which is equal to AD; hence DC is double of DA, and AC is triple of AD.

**Step 3.** Join BC [P1], and through D draw DF parallel to BC, meeting AB at F [1.31].

**Step 4.** Since DF has been drawn parallel to BC, one of the sides of the triangle ABC, and cuts the remaining sides AC and AB at D and F, it cuts them proportionally: as CD is to DA, so is BF to FA [6.2].

**Step 5.** In this proportion take of the first and third terms, CD and BF, the same multiple (once each), and of the second and fourth terms, DA and FA, the same multiple (twice each). Since CD is equal to twice DA, the corresponding equimultiples of the third and fourth terms must likewise be equal, that is, BF is equal to twice FA [D5.5]. Therefore BF is double of FA.

**Step 6.** Now AB is made up of AF and FB. Adding AF to each side of the equality FB = twice AF, the whole AB is equal to three times AF [CN2]; that is, AB is triple of AF.

**Step 7.** Hence AF measures AB, being contained in it exactly three times, so AF is a part of AB [D5.1], namely its third part. Therefore from the given straight line AB the prescribed third part AF has been cut off. Q.E.F.

**Step 8.** In general, to cut off the n-th part, lay off along AG n segments AD, DE, ... each equal to AD, so that the last endpoint C makes CD equal to (n−1) times DA; the same reasoning of Steps 3–7 gives BF equal to (n−1) times FA, whence AB is n times AF and AF is the prescribed n-th part.

**USED:** 1.3, 1.31, 6.2, CN2, D5.1, D5.5, P1, P2
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.375 — AI adds ['CN2', 'D5.1', 'D5.5', 'P1', 'P2']

## Proposition 6.10
**Statement:** To cut a given uncut straight line similarly to a given cut straight line.

## Proposition 6.10
**Statement:** To cut a given uncut straight line similarly to a given cut straight line.

**Step 1.** Let AB be the given uncut straight line, and let AC be the given straight line cut at the points D and E; and let AB and AC be so placed as to contain the angle BAC at their common extremity A. It is required to cut AB similarly to AC, that is, into segments proportional to AD, DE, EC.

**Step 2.** Join BC. [P1]

**Step 3.** Through the points D and E draw DF and EG parallel to BC, meeting AB at F and G respectively; and through D draw DHK parallel to AB, meeting EG at H and BC at K. [1.31]

**Step 4.** Since each of DF and EG is parallel to the same straight line BC, DF is parallel to EG; hence FD is parallel to GH, and HE is parallel to KC. [1.30]

**Step 5.** Therefore FGHD is a parallelogram, for FG is parallel to DH (DK being parallel to AB by construction) and FD is parallel to GH (Step 4). Likewise GBKH is a parallelogram, for GB is parallel to HK (DK being parallel to AB) and GH is parallel to BK (EG being parallel to BC by construction).

**Step 6.** In a parallelogram the opposite sides are equal to one another; therefore in FGHD, DH is equal to FG, and in GBKH, HK is equal to GB. [1.34]

**Step 7.** In the triangle DKC the straight line HE has been drawn parallel to the side KC (Step 4); therefore it cuts the sides DK and DC proportionally, so that, as CE is to ED, so is KH to HD. [6.2]

**Step 8.** Since KH is equal to BG (Step 6), the equal magnitudes KH and BG have the same ratio to HD, so that, as KH is to HD, so is BG to HD; and since HD is equal to GF (Step 6), BG has the same ratio to the equal magnitudes HD and GF, so that, as BG is to HD, so is BG to GF. [5.7]

**Step 9.** Ratios which are the same with the same ratio are the same with one another; therefore, as CE is to ED, so is BG to GF. [5.11]

**Step 10.** Again, in the triangle AGE the straight line FD has been drawn parallel to the side GE (Step 4); therefore it cuts the sides AG and AE proportionally, so that, as ED is to DA, so is GF to FA. [6.2]

**Step 11.** Hence, as CE is to ED, so is BG to GF (Step 9), and as ED is to DA, so is GF to FA (Step 10); that is, the segments AF, FG, GB of AB are respectively proportional to the segments AD, DE, EC of AC. Therefore the given uncut straight line AB has been cut at F and G similarly to the given cut straight line AC cut at D and E. Q.E.F.

*Path note:* An alternative route omits the third parallel DHK, applying 6.2 in the triangles ABC and AGE and then combining the two proportions by composition (5.18) and ex aequali (5.22). The parallelogram route above is more direct, obtaining each required proportion by a single application of 6.2 with substitution of equal sides, so it was chosen.

**USED:** P1, 1.30, 1.31, 1.34, 5.7, 5.11, 6.2

**USED:** 1.30, 1.31, 1.34, 5.11, 5.7, 6.2, P1
**Human refs (from References field):** 1.31, 1.34, 6.2
**Jaccard:** 0.429 — AI adds ['1.30', '5.11', '5.7', 'P1']

## Proposition 6.11
**Statement:** To two given straight lines to find a third proportional.

**Step 1.** Let AB and AC be the two given straight lines, and let them be placed so as to contain any angle BAC at the point A (drawing a straight line from A to any point not on AB by P1, and cutting off on it AC equal to the second given straight line by 1.3). It is required to find a third proportional to AB, AC.

**Step 2.** Produce AB in a straight line beyond B to D (P2), and cut off BD equal to AC (1.3).

**Step 3.** Join BC (P1).

**Step 4.** Through the point D draw DE parallel to BC (1.31), and produce AC beyond C to meet DE at the point E (P2). Then ADE is a triangle, and BC has been drawn parallel to DE, one of its sides, cutting the side AD at B and the side AE at C.

**Step 5.** Since BC is parallel to DE, one of the sides of the triangle ADE, it cuts the remaining sides AD, AE proportionally; therefore, as AB is to BD, so is AC to CE (6.2).

**Step 6.** But BD is equal to AC (Step 2), and the same magnitude has the same ratio to equal magnitudes; therefore, as AB is to BD, so is AB to AC (5.7).

**Step 7.** Now the ratio of AB to AC is the same as the ratio of AB to BD (Step 6), and the ratio of AB to BD is the same as the ratio of AC to CE (Step 5); ratios which are the same with the same ratio are also the same with one another; therefore, as AB is to AC, so is AC to CE (5.11).

**Step 8.** Therefore to the two given straight lines AB, AC a third proportional CE has been found, such that as AB is to AC, so is AC to CE. Q.E.F.

**USED:** 1.3, 1.31, 5.11, 5.7, 6.2, P1, P2
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.429 — AI adds ['5.11', '5.7', 'P1', 'P2']

## Proposition 6.12
**Statement:** To three given straight lines to find a fourth proportional.

**Step 1.** Let A, B, C be the three given straight lines. It is required to find a fourth proportional to A, B, C, that is, a straight line X such that, as A is to B, so is C to X.

**Step 2.** Let two straight lines DE, DF be set out from a point D containing any angle EDF (P1), and let each be produced as far as may be necessary (P2).

**Step 3.** On DE cut off DG equal to A, and from G along the same line cut off GE equal to B; on DF cut off DH equal to C (1.3).

**Step 4.** Join GH (P1), and through the point E draw EF parallel to GH (1.31), meeting DF produced at the point F.

**Step 5.** Since GH has been drawn parallel to EF, one of the sides of the triangle DEF, it cuts the remaining sides DE, DF proportionally; therefore, as DG is to GE, so is DH to HF (6.2).

**Step 6.** But DG is equal to A and GE is equal to B; and equal magnitudes have the same ratio to the same magnitude, and the same magnitude has the same ratio to equal magnitudes (5.7); therefore, as DG is to GE, so is A to B. Likewise, since DH is equal to C, as DH is to HF, so is C to HF (5.7).

**Step 7.** Therefore the ratio of A to B is the same as the ratio of DG to GE, which is the same as the ratio of DH to HF, which in turn is the same as the ratio of C to HF; and ratios which are the same with the same ratio are also the same with one another (5.11). Therefore, as A is to B, so is C to HF.

**Step 8.** Therefore to the three given straight lines A, B, C a fourth proportional HF has been found. Q.E.F.

**USED:** 1.3, 1.31, 5.11, 5.7, 6.2, P1, P2
**Human refs (from References field):** 1.31, 6.2
**Jaccard:** 0.286 — AI adds ['1.3', '5.11', '5.7', 'P1', 'P2']

## Proposition 6.13
**Statement:** To two given straight lines to find a mean proportional.

**Step 1.** Let the two given straight lines be AB and G. Produce AB in a straight line beyond B (P2), and from the produced part cut off BC equal to G (1.3). Then the two given straight lines are AB and BC, placed in one straight line AC with B between A and C; it is required to find a mean proportional between AB and BC.

**Step 2.** Bisect AC at the point E (1.10), and with centre E and distance EA describe a circle (P3). Since EC is equal to EA, the point C lies on the circumference (D1.15); and AC, passing through the centre E and terminated at both ends by the circumference, is a diameter of the circle (D1.17). Let ADC be the semicircle on the diameter AC (D1.18).

**Step 3.** From the point B draw BD at right angles to AC (1.11), and let it meet the circumference of the semicircle at D. Join AD and DC (P1).

**Step 4.** Since the angle ADC is an angle in the semicircle ADC, the angle ADC is right (3.31). Therefore the triangle ADC is right-angled at D (D1.21).

**Step 5.** In the right-angled triangle ADC the straight line DB has been drawn from the right angle at D perpendicular to the base AC. Therefore, by 6.8, the triangles ABD and DBC adjoining the perpendicular are similar to one another, the right angle ABD corresponding to the right angle DBC, the angle BAD to the angle BDC, and the angle ADB to the angle DCB.

**Step 6.** Since the triangles ABD and DBC are similar, they are equiangular and have the sides about the equal angles proportional (D6.1); and in equiangular triangles the corresponding sides are those which subtend the equal angles (6.4). About the equal right angles ABD and DBC, the side AB subtends the angle ADB and the side DB subtends the equal angle DCB, while the side BD subtends the angle BAD and the side BC subtends the equal angle BDC. Therefore, as AB is to BD, so is DB to BC (6.4).

**Step 7.** Therefore the three straight lines AB, DB, BC are in continued proportion, AB being to DB as DB is to BC; that is, DB has been found a mean proportional between the two given straight lines AB and BC (the latter equal to G). Q.E.F.

**USED:** 1.10, 1.11, 1.3, 3.31, 6.4, 6.8, D1.15, D1.17, D1.18, D1.21, D6.1, P1, P2, P3
**Human refs (from References field):** 3.31, 6.8
**Jaccard:** 0.143 — AI adds ['1.10', '1.11', '1.3', '6.4', 'D1.15', 'D1.17', 'D1.18', 'D1.21', 'D6.1', 'P1', 'P2', 'P3']

## Proposition 6.14
**Statement:** In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal.

## Proposition 6.14
**Statement:** In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal.

**Step 1.** Let AB and BC be equiangular parallelograms, the sides of AB about the angle at B being DB, BF and the sides of BC about the angle at B being BE, BG, with the angle DBF equal to the angle EBG. Place the two parallelograms so that DB and BE lie in one straight line with B between D and E, and so that F and G lie on opposite sides of the straight line DE.

**Step 2.** Since the straight line BF stands on the straight line DE at the point B, the adjacent angles DBF, FBE are together equal to two right angles [1.13].

**Step 3.** The angle DBF is equal to the angle EBG (hypothesis). Adding the angle FBE to each, the angles FBE, EBG together are equal to the angles FBE, DBF together [CN2], and therefore to two right angles [CN1].

**Step 4.** Hence, with the straight line BE and at the point B on it, the two straight lines BF, BG, not lying on the same side of BE, make the adjacent angles FBE, EBG equal to two right angles; therefore FB is in a straight line with BG [1.14].

**Step 5.** Complete the parallelogram FE on the sides BF, BE: through E draw a straight line parallel to BF and through F draw a straight line parallel to BE [1.31], meeting at H; then FBEH is a parallelogram.

**Step 6.** The parallelograms AB and FE have their bases DB and BE on the same straight line DE and have the common vertex F; the perpendicular drawn from F to DE is the height of each [D6.4], so they are under the same height. Therefore, as the parallelogram AB is to the parallelogram FE, so is the base DB to the base BE [6.1].

**Step 7.** Likewise the parallelograms BC and FE have their bases BG and BF on the same straight line FG (Step 4) and have the common vertex E; the perpendicular drawn from E to FG is the height of each [D6.4], so they are under the same height. Therefore, as the parallelogram BC is to the parallelogram FE, so is the base GB to the base BF [6.1].

**Step 8.** First, let the parallelograms AB and BC be equal. Since equal magnitudes have the same ratio to the same magnitude, as AB is to FE, so is BC to FE [5.7].

**Step 9.** Now as DB is to BE, so is AB to FE (Step 6); as AB is to FE, so is BC to FE (Step 8); and as BC is to FE, so is GB to BF (Step 7). Ratios which are the same with the same ratio are the same with one another; therefore as DB is to BE, so is GB to BF [5.11].

**Step 10.** Thus in the equal and equiangular parallelograms AB, BC the sides about the equal angles at B are reciprocally proportional: the side DB of AB is to the side BE of BC as the side GB of BC is to the side BF of AB [D6.2]. This proves the first part.

**Step 11.** Conversely, let AB and BC be equiangular parallelograms in which the sides about the equal angles are reciprocally proportional, so that as DB is to BE, so is GB to BF. Make the same placement and construction as in Steps 1 to 5, so that Steps 6 and 7 again hold.

**Step 12.** Then as AB is to FE, so is DB to BE (Step 6); as DB is to BE, so is GB to BF (hypothesis); and as GB is to BF, so is BC to FE (Step 7). Therefore as AB is to FE, so is BC to FE [5.11].

**Step 13.** But magnitudes which have the same ratio to the same magnitude are equal to one another; therefore the parallelogram AB is equal to the parallelogram BC [5.9]. This proves the second part.

**USED:** 1.13, 1.14, 1.31, 5.7, 5.9, 5.11, 6.1, CN1, CN2, D6.2, D6.4

**USED:** 1.13, 1.14, 1.31, 5.11, 5.7, 5.9, 6.1, CN1, CN2, D6.2, D6.4
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.455 — AI adds ['1.13', '1.31', 'CN1', 'CN2', 'D6.2', 'D6.4']

## Proposition 6.15
**Statement:** In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal.

**Step 1.** Let ABC and ADE be two equal triangles having the angle BAC equal to the angle DAE. Place the triangles so that the vertices of the equal angles coincide at A, CA lies in a straight line with AD, and the points B and E lie on opposite sides of the straight line CD.

**Step 2.** Since the straight line BA stands upon the straight line CAD, the adjacent angles CAB and BAD are together equal to two right angles (1.13).

**Step 3.** The angle CAB is equal to the angle DAE by hypothesis; adding the angle BAD to each, the angles BAD, DAE together are equal to the angles BAD, CAB together (CN2), and these latter are two right angles, so the angles BAD, DAE together are equal to two right angles (CN1).

**Step 4.** Thus the two straight lines BA and AE, lying on opposite sides of AD at the point A, make the adjacent angles BAD, DAE with AD equal to two right angles; therefore BA is in a straight line with AE (1.14).

**Step 5.** Join BD (P1).

**Step 6.** Since the triangle ABC is equal to the triangle ADE, and BAD is another triangle, equal magnitudes have the same ratio to the same magnitude; therefore the triangle CAB is to the triangle BAD as the triangle EAD is to the triangle BAD (5.7).

**Step 7.** The triangles CAB and BAD have the common vertex B and their bases CA, AD lie on the one straight line CD, so they are under the same height; therefore the triangle CAB is to the triangle BAD as the base CA is to the base AD (6.1).

**Step 8.** Likewise the triangles EAD and BAD have the common vertex D and their bases EA, AB lie on the one straight line EB, so they are under the same height; therefore the triangle EAD is to the triangle BAD as the base EA is to the base AB (6.1).

**Step 9.** From Steps 6, 7 and 8, ratios which are the same as the same ratio are the same as one another; therefore as CA is to AD, so is EA to AB (5.11). Hence in the equal triangles ABC, ADE the sides about the equal angles at A are reciprocally proportional (D6.2), which proves the first part.

**Step 10.** Conversely, let the triangles ABC and ADE have the angle BAC equal to the angle DAE, and let the sides about these angles be reciprocally proportional, namely as CA is to AD, so let EA be to AB. Place the triangles as in Step 1; then by Steps 2 to 4 BAE and CAD are straight lines, and join BD as in Step 5.

**Step 11.** As in Step 7, CA is to AD as the triangle CAB is to the triangle BAD (6.1); and as in Step 8, EA is to AB as the triangle EAD is to the triangle BAD (6.1).

**Step 12.** Since CA is to AD as EA is to AB, the triangle CAB is to the triangle BAD as the triangle EAD is to the triangle BAD (5.11).

**Step 13.** Magnitudes which have the same ratio to the same magnitude are equal; therefore the triangle ABC is equal to the triangle ADE (5.9). This proves the second part.

Therefore, in equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal.

**USED:** 1.13, 1.14, 5.11, 5.7, 5.9, 6.1, CN1, CN2, D6.2, P1
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.500 — AI adds ['1.13', 'CN1', 'CN2', 'D6.2', 'P1']

## Proposition 6.16
**Statement:** If four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes be equal to the rectangle contained by the means, the four straight lines will be proportional.

**Step 1.** Let AB, CD, E, F be four straight lines which are proportional, so that, as AB is to CD, so is E to F. The extremes are AB and F, and the means are CD and E. I say that the rectangle contained by AB, F is equal to the rectangle contained by CD, E.

**Step 2.** From the point A draw AG at right angles to the straight line AB, and from the point C draw CH at right angles to the straight line CD [1.11].

**Step 3.** Make AG equal to F, and CH equal to E [1.3].

**Step 4.** Let the parallelogram BG be completed by drawing through G the straight line GK parallel to AB and through B the straight line BK parallel to AG, K being the vertex opposite A; and likewise let the parallelogram DH be completed by drawing through H the straight line HL parallel to CD and through D the straight line DL parallel to CH, L being the vertex opposite C [1.31]. Thus BG (that is, ABKG) and DH (that is, CDLH) are parallelograms, their opposite sides being parallel by construction.

**Step 5.** Since AG is parallel to BK and the straight line AB falls upon them, the interior angles BAG, ABK on the same side are together equal to two right angles [1.29]; but the angle BAG is right (Step 2); therefore the angle ABK is also right. In the same way, since AB is parallel to GK and AG falls upon them, the angle AGK is right; and since AG is parallel to BK and GK falls upon them, the angle GKB is right [1.29]. Therefore all the angles of the parallelogram BG are right, so that BG is a rectangular parallelogram, namely the rectangle contained by the two straight lines AB, AG which contain its right angle at A [D2.1]. By the same reasoning DH is a rectangular parallelogram, namely the rectangle contained by CD, CH [D2.1].

**Step 6.** But AG is equal to F, and CH is equal to E (Step 3). Therefore BG is the rectangle contained by AB, F, and DH is the rectangle contained by CD, E.

**Step 7.** Since the angles BAG, DCH are both right, they are equal to one another [P4]; and all the remaining angles of BG and of DH are also right (Step 5), and so are likewise equal to one another [P4]. Hence the parallelograms BG, DH are equiangular.

**Step 8.** Now, by hypothesis, as AB is to CD, so is E to F. But E is equal to CH, and equal magnitudes have to the same the same ratio; therefore, as E is to F, so is CH to F [5.7]. Again, F is equal to AG, and the same has to equal magnitudes the same ratio; therefore, as CH is to F, so is CH to AG [5.7]. Since ratios which are the same with the same ratio are also the same with one another, as E is to F, so is CH to AG [5.11]; and consequently, as AB is to CD, so is CH to AG [5.11].

**Step 9.** Thus in the equiangular parallelograms BG, DH the sides about the equal angles BAG, DCH are reciprocally proportional: as AB, a side of BG, is to CD, a side of DH, so is CH, the other side of DH, to AG, the other side of BG. But equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal [6.14]. Therefore the parallelogram BG is equal to the parallelogram DH.

**Step 10.** And BG is the rectangle contained by AB, F, while DH is the rectangle contained by CD, E (Step 6). Therefore the rectangle contained by AB, F is equal to the rectangle contained by CD, E; that is, the rectangle contained by the extremes is equal to the rectangle contained by the means.

**Step 11.** Next, let the rectangle contained by AB, F be equal to the rectangle contained by CD, E. I say that, as AB is to CD, so is E to F.

**Step 12.** With the same construction (Steps 2 to 4), BG is the rectangle contained by AB, F, and DH is the rectangle contained by CD, E (Steps 5 and 6). Since by hypothesis the rectangle contained by AB, F is equal to the rectangle contained by CD, E, the parallelogram BG is equal to the parallelogram DH.

**Step 13.** Moreover BG, DH are equiangular (Step 7). But in equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional [6.14]; therefore, as AB is to CD, so is CH to AG.

**Step 14.** But CH is equal to E, so that, as CH is to AG, so is E to AG [5.7]; and AG is equal to F, so that, as E is to AG, so is E to F [5.7]; therefore, as CH is to AG, so is E to F [5.11]. Hence, as AB is to CD, so is E to F [5.11]; that is, the four straight lines AB, CD, E, F are proportional.

**Step 15.** Therefore, if four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes be equal to the rectangle contained by the means, the four straight lines will be proportional. Q.E.D.

**USED:** 1.11, 1.29, 1.3, 1.31, 5.11, 5.7, 6.14, D2.1, P4
**Human refs (from References field):** 6.14
**Jaccard:** 0.111 — AI adds ['1.11', '1.29', '1.3', '1.31', '5.11', '5.7', 'D2.1', 'P4']

## Proposition 6.17
**Statement:** If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to the square on the mean, the three straight lines will be proportional.

**Statement:** If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to the square on the mean, the three straight lines will be proportional.

**Step 1.** Let A, B, C be three straight lines which are proportional, so that, as A is to B, so is B to C. I say that the rectangle contained by A, C is equal to the square on B.

**Step 2.** At any point let a straight line D be placed equal to B [1.2].

**Step 3.** Since B is equal to D, and equal magnitudes have the same ratio to the same magnitude, as B is to C, so is D to C [5.7].

**Step 4.** But, by hypothesis, as A is to B, so is B to C; and ratios which are the same with the same ratio are the same with one another; therefore, as A is to B, so is D to C [5.11].

**Step 5.** Thus the four straight lines A, B, D, C are proportional, A and C being the extremes and B, D the means. Therefore the rectangle contained by the extremes A, C is equal to the rectangle contained by the means B, D [6.16].

**Step 6.** Now the rectangle contained by B, D is the rectangular parallelogram whose adjacent sides are B and D [D2.1]; and since D is equal to B, this figure is both equilateral and right-angled, that is, it is the square described on B [D1.22]. Therefore the rectangle contained by A, C is equal to the square on B.

**Step 7.** Next, let the rectangle contained by A, C be equal to the square on B. I say that, as A is to B, so is B to C.

**Step 8.** With D equal to B as before, the square on B is the rectangle contained by B, D, exactly as in Step 6 [D2.1, D1.22]. Therefore the rectangle contained by A, C is equal to the rectangle contained by B, D.

**Step 9.** Since the rectangle contained by the extremes A, C is equal to the rectangle contained by the means B, D, the four straight lines A, B, D, C are proportional: as A is to B, so is D to C [6.16].

**Step 10.** But D is equal to B; therefore, as D is to C, so is B to C [5.7]; and hence, as A is to B, so is B to C [5.11].

**Step 11.** Therefore, if three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to the square on the mean, the three straight lines are proportional. Q.E.D.

**USED:** 1.2, 5.7, 5.11, 6.16, D2.1, D1.22

*Note on tool choice:* the auxiliary line D equal to B (Step 2) is obtained by 1.2 rather than 1.3, because D is placed freely at a point and is not cut off from a given greater straight line.

**USED:** 1.2, 5.11, 5.7, 6.16, D1.22, D2.1
**Human refs (from References field):** 6.16
**Jaccard:** 0.167 — AI adds ['1.2', '5.11', '5.7', 'D1.22', 'D2.1']

## Proposition 6.18
**Statement:** On a given straight line to describe a rectilineal figure similar and similarly situated to a given rectilineal figure.

**Step 1.** Let AB be the given straight line and let CDEF be the given rectilineal figure, a quadrilateral with vertices C, D, E, F taken in order (the method below applies to a figure with any number of sides). It is required to describe on AB a rectilineal figure similar and similarly situated to CDEF.

**Step 2.** Join DF (P1). The quadrilateral CDEF is thereby divided into the two triangles DCF and DFE.

**Step 3.** On the straight line AB, at the point A, construct the angle GAB equal to the angle DCF, and at the point B construct the angle ABG equal to the angle CDF, both angles being placed on the same side of AB (1.23).

**Step 4.** In the triangle DCF the two angles DCF and CDF are together less than two right angles (1.17). Since the angles GAB and ABG are equal respectively to DCF and CDF, their sum equals the sum of DCF and CDF (CN2) and is therefore less than two right angles. Hence, by P5, the straight lines drawn from A and B at these angles, if produced, meet on the side of AB on which the angles lie; let them meet at G. Thus a triangle ABG stands on AB.

**Step 5.** In the triangles ABG and CDF, the angle GAB equals the angle DCF and the angle ABG equals the angle CDF (Step 3). The three angles of each triangle are together equal to two right angles (1.32), so the remaining angle AGB equals the remaining angle CFD (CN3). Therefore the triangle ABG is equiangular with the triangle CDF, with A corresponding to C, B to D, and G to F.

**Step 6.** Since the triangles ABG and CDF are equiangular, the sides about their equal angles are proportional (6.4): about the equal angles at B and D, AB : BG = CD : DF; about the equal angles at G and F, GA : GB = FC : FD; about the equal angles at A and C, GA : AB = FC : CD.

**Step 7.** On the straight line BG, at the point G, construct the angle BGH equal to the angle DFE, and at the point B construct the angle GBH equal to the angle FDE, both angles being placed on the side of BG remote from A (1.23).

**Step 8.** In the triangle DFE the angles DFE and FDE are together less than two right angles (1.17); hence the angles BGH and GBH, being equal to them respectively, are together less than two right angles (CN2). By P5 the straight lines drawn from G and B at these angles meet on the side of BG remote from A; let them meet at H. Thus a triangle BGH stands on BG.

**Step 9.** In the triangles BGH and DFE, the angle BGH equals the angle DFE and the angle GBH equals the angle FDE (Step 7). Since the three angles of each triangle equal two right angles (1.32), the remaining angle BHG equals the remaining angle DEF (CN3). Therefore the triangle BGH is equiangular with the triangle DFE, with B corresponding to D, G to F, and H to E.

**Step 10.** Since the triangles BGH and DFE are equiangular, the sides about their equal angles are proportional (6.4): about the equal angles at B and D, BG : BH = DF : DE; about the equal angles at G and F, GB : GH = FD : FE; about the equal angles at H and E, BH : HG = DE : EF.

**Step 11.** The figure ABHG is equiangular with the figure CDEF. For the angle GAB equals the angle DCF (Step 3); the angle BHG equals the angle DEF (Step 9); the angle ABH, being made up of the angles ABG and GBH, equals the angle CDE, which is made up of the equal angles CDF and FDE (CN2); and the angle AGH, being made up of the angles AGB and BGH, equals the angle CFE, which is made up of the equal angles CFD and DFE (CN2).

**Step 12.** The sides about the equal angles of the two figures are proportional. About the angles at A and C, GA : AB = FC : CD (Step 6). About the angles at H and E, BH : HG = DE : EF (Step 10). About the angles at B and D: since AB : BG = CD : DF (Step 6) and BG : BH = DF : DE (Step 10), therefore, ex aequali, AB : BH = CD : DE (5.22). About the angles at G and F: since GA : GB = FC : FD (Step 6) and GB : GH = FD : FE (Step 10), therefore, ex aequali, GA : GH = FC : FE (5.22).

**Step 13.** Since the figures ABHG and CDEF have their angles severally equal (Step 11) and the sides about the equal angles proportional (Step 12), the figure ABHG is similar to the figure CDEF (D6.1). Moreover, the vertices A, B, H, G correspond in order to the vertices C, D, E, F, the given straight line AB corresponding to the side CD, so that the figure ABHG is also similarly situated to CDEF.

**Step 14.** If the given figure has more than four sides, join further straight lines from the vertex F to the remaining vertices (P1), dividing the figure into triangles; then on the side last obtained (here GH) construct, as in Steps 7 to 10, a triangle equiangular with the next triangle of the given figure, and continue until all the triangles have been used. Each new triangle is equiangular with its corresponding triangle (1.23, 1.17, P5, 1.32, CN3), its sides are proportional to those of that triangle (6.4), the angles at the common vertices combine by addition (CN2), and the ratios of the sides about those angles combine ex aequali (5.22); hence the whole figure so described is similar and similarly situated to the given figure (D6.1).

Therefore on the given straight line AB the rectilineal figure ABHG has been described similar and similarly situated to the given rectilineal figure CDEF. Q.E.F.

**USED:** 1.17, 1.23, 1.32, 5.22, 6.4, CN2, CN3, D6.1, P1, P5
**Human refs (from References field):** 1.23, 1.32, 6.4, D6.1
**Jaccard:** 0.400 — AI adds ['1.17', '5.22', 'CN2', 'CN3', 'P1', 'P5']

## Proposition 6.19
**Statement:** Similar triangles are to one another in the duplicate ratio of the corresponding sides.

**Statement:** Similar triangles are to one another in the duplicate ratio of the corresponding sides.

**Step 1.** Let ABC, DEF be similar triangles having the angle at B equal to the angle at E, and such that, as AB is to BC, so is DE to EF, so that BC corresponds to EF (D6.1: similar rectilineal figures have their angles severally equal and the sides about the equal angles proportional). It is to be proved that the triangle ABC has to the triangle DEF the duplicate ratio of that which BC has to EF.

**Step 2.** To the two straight lines BC, EF take a third proportional (6.11); on the straight line BC, produced beyond C if necessary (P2), cut off from B a segment BG equal to this third proportional (1.3). Then, as BC is to EF, so is EF to BG, and G lies on the straight line BC on the same side of B as C.

**Step 3.** Join AG (P1).

**Step 4.** Since, as AB is to BC, so is DE to EF, therefore alternately, as AB is to DE, so is BC to EF (5.16).

**Step 5.** But, as BC is to EF, so is EF to BG (Step 2). Therefore, as AB is to DE, so is EF to BG (5.11).

**Step 6.** Since G lies on the straight line BC on the same side of B as C, the angle ABG is the same as the angle ABC, and so the angle ABG is equal to the angle DEF (Step 1). Thus the triangles ABG, DEF have one angle equal to one angle, and the sides about the equal angles, namely AB, BG and DE, EF, are reciprocally proportional, for AB is to DE as EF is to BG (Step 5; D6.2). Therefore the triangle ABG is equal to the triangle DEF (6.15).

**Step 7.** Since the three straight lines BC, EF, BG are proportional (Step 2), BC has to BG the duplicate ratio of that which BC has to EF (D5.9).

**Step 8.** The triangles ABC, ABG have the same vertex A and their bases BC, BG lie on the same straight line, so they are under the same height; therefore, as BC is to BG, so is the triangle ABC to the triangle ABG (6.1).

**Step 9.** Hence the triangle ABC has to the triangle ABG the duplicate ratio of that which BC has to EF (Steps 7 and 8).

**Step 10.** But the triangle ABG is equal to the triangle DEF (Step 6); therefore, as the triangle ABC is to the triangle ABG, so is the triangle ABC to the triangle DEF (5.7).

**Step 11.** Therefore the triangle ABC has to the triangle DEF the duplicate ratio of that which BC has to EF, where BC, EF are corresponding sides. Therefore similar triangles are to one another in the duplicate ratio of the corresponding sides. Q.E.D.

**USED:** D6.1, 6.11, P2, 1.3, P1, 5.16, 5.11, D6.2, 6.15, D5.9, 6.1, 5.7

**USED:** 1.3, 5.11, 5.16, 5.7, 6.1, 6.11, 6.15, D5.9, D6.1, D6.2, P1, P2
**Human refs (from References field):** 5.11, 5.16, 6.1, 6.11, 6.15, D5.11, D5.9
**Jaccard:** 0.462 — AI adds ['1.3', '5.7', 'D6.1', 'D6.2', 'P1', 'P2']; Human adds ['D5.11']

## Proposition 6.20
**Statement:** Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate of that which the corresponding side has to the corresponding  side.

**Step 1.** Let ABCDE and FGHKL be the two similar polygons, with AB the side corresponding to FG, so that the vertices correspond in order A–F, B–G, C–H, D–K, E–L. By D6.1 the polygons have their angles severally equal — angle BAE = angle GFL, angle ABC = angle FGH, angle BCD = angle GHK, angle CDE = angle HKL, angle DEA = angle KLF — and the sides about the equal angles are proportional: BA : AE = GF : FL, AB : BC = FG : GH, BC : CD = GH : HK, and so on round the figure. Since the angles correspond one to one, the two polygons have the same number of sides.

**Step 2.** Join BE and EC (P1), and join GL and LH (P1). These diagonals drawn from the corresponding vertices E and L divide polygon ABCDE into the three triangles ABE, EBC, ECD and polygon FGHKL into the three triangles FGL, LGH, LHK; the two sets of triangles are therefore equal in multitude (in general the diagonals from one vertex divide a polygon of n sides into n − 2 triangles, and both polygons have the same n).

**Step 3.** In triangles ABE, FGL: angle BAE = angle GFL and BA : AE = GF : FL (Step 1). Thus they have one angle equal to one angle and the sides about the equal angles proportional; by 6.6 the triangles are equiangular, with angle ABE = angle FGL (each subtended by AE, FL respectively) and angle AEB = angle FLG (each subtended by AB, FG respectively).

**Step 4.** Since triangles ABE, FGL are equiangular, by 6.4 the sides about their equal angles are proportional, the corresponding sides being those which subtend the equal angles. Hence triangle ABE is similar to triangle FGL (D6.1). In particular, taking the sides about the equal angles ABE, FGL: EB : BA = LG : GF.

**Step 5.** The whole angle ABC equals the whole angle FGH (Step 1), and the part angle ABE equals the part angle FGL (Step 3). Therefore the remaining angle EBC equals the remaining angle LGH (CN3).

**Step 6.** EB : BA = LG : GF (Step 4) and BA : BC = GF : GH (Step 1). Hence, ex aequali (5.22), EB : BC = LG : GH.

**Step 7.** In triangles EBC, LGH: angle EBC = angle LGH (Step 5) and EB : BC = LG : GH (Step 6). By 6.6 they are equiangular, with angle BEC = angle GLH (subtended by BC, GH) and angle BCE = angle GHL (subtended by EB, LG). By 6.4 the sides about the equal angles are proportional, so triangle EBC is similar to triangle LGH (D6.1). In particular, taking the sides about the equal angles BCE, GHL: EC : CB = LH : HG.

**Step 8.** The whole angle BCD equals the whole angle GHK (Step 1), and the part angle BCE equals the part angle GHL (Step 7); therefore the remaining angle ECD equals the remaining angle LHK (CN3).

**Step 9.** EC : CB = LH : HG (Step 7) and CB : CD = HG : HK (Step 1); hence, ex aequali (5.22), EC : CD = LH : HK.

**Step 10.** In triangles ECD, LHK: angle ECD = angle LHK (Step 8) and EC : CD = LH : HK (Step 9). By 6.6 they are equiangular, and by 6.4 the sides about the equal angles are proportional; therefore triangle ECD is similar to triangle LHK (D6.1). For polygons with more sides the same pattern — subtract the angle already used (CN3), apply ex aequali (5.22), then 6.6 and 6.4 — is repeated round the polygon.

**Step 11.** Thus the similar polygons have been divided into similar triangles, ABE similar to FGL, EBC to LGH, ECD to LHK, and these triangles are equal in multitude. This proves the first part.

**Step 12.** In the similar triangles ABE, FGL the side BE corresponds to GL (both subtend the equal angles BAE, GFL). By 6.19, triangle ABE has to triangle FGL the ratio duplicate of that which BE has to GL. In the similar triangles EBC, LGH the side EB likewise corresponds to LG (both subtend the equal angles BCE, GHL); by 6.19, triangle EBC has to triangle LGH the ratio duplicate of that which EB has to LG.

**Step 13.** Take X a third proportional to BE, GL (6.11), so that BE : GL = GL : X. By D5.9 the ratio duplicate of BE : GL is the ratio BE : X. Hence triangle ABE : triangle FGL = BE : X and triangle EBC : triangle LGH = BE : X; therefore, by 5.11, triangle ABE : triangle FGL = triangle EBC : triangle LGH.

**Step 14.** In the same way, EC corresponds to LH both in the similar triangles EBC, LGH (EC, LH subtending the equal angles EBC, LGH) and in the similar triangles ECD, LHK (EC, LH subtending the equal angles EDC, LKH); by 6.19 each of the ratios triangle EBC : triangle LGH and triangle ECD : triangle LHK is the duplicate of EC : LH. Taking a third proportional to EC, LH (6.11) and arguing exactly as in Step 13 (D5.9, 5.11), triangle EBC : triangle LGH = triangle ECD : triangle LHK.

**Step 15.** Therefore triangle ABE : triangle FGL = triangle EBC : triangle LGH = triangle ECD : triangle LHK. By 5.12, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents: triangle ABE : triangle FGL = (ABE + EBC + ECD) : (FGL + LGH + LHK) = polygon ABCDE : polygon FGHKL. Hence the triangles are in the same ratio as the wholes. This proves the second part.

**Step 16.** Finally, in the similar triangles ABE, FGL the side AB corresponds to FG (both subtend the equal angles AEB, FLG); by 6.19, triangle ABE has to triangle FGL the ratio duplicate of that which AB has to FG. Take Y a third proportional to AB, FG (6.11), so that AB : FG = FG : Y; then by D5.9, triangle ABE : triangle FGL = AB : Y. But polygon ABCDE : polygon FGHKL = triangle ABE : triangle FGL (Step 15); therefore, by 5.11, polygon ABCDE : polygon FGHKL = AB : Y. Since AB, FG, Y are three magnitudes in continued proportion, the polygon ABCDE has to the polygon FGHKL the ratio duplicate of that which the corresponding side AB has to the corresponding side FG (D5.9). QED.

*Path note (flagged per protocol).* For the second part, an alternative route joins the further diagonals AC, FH, proves the partial triangles cut off on them equiangular via 1.32, and compares the component triangles through their bases on AC, FH using 6.1 and 5.12 with alternation. Because 6.19 is already available, the route through the duplicate ratios of the shared corresponding sides BE : GL and EC : LH is shorter, so it was chosen.

**USED:** 5.11, 5.12, 5.22, 6.11, 6.19, 6.4, 6.6, CN3, D5.9, D6.1, P1
**Human refs (from References field):** 1.32, 5.12, 5.22, 6.1, 6.19, 6.4, 6.6, D6.1
**Jaccard:** 0.462 — AI adds ['5.11', '6.11', 'CN3', 'D5.9', 'P1']; Human adds ['1.32', '6.1']

## Proposition 6.21
**Statement:** Figures which are similar to the same rectilineal figure are also similar to one another.

**Step 1.** Let A and B be rectilineal figures each of which is similar to the same rectilineal figure C. I say that A is also similar to B.

**Step 2.** Since A is similar to C, by D6.1 the angles of A are severally equal to the angles of C, and the sides about the equal angles are proportional; that is, for any angle of A and the angle of C equal to it, the two sides of A containing the one are to one another as the corresponding two sides of C containing the other.

**Step 3.** Again, since B is similar to C, by D6.1 the angles of B are severally equal to the angles of C, and the sides about the equal angles are proportional in the same manner.

**Step 4.** Take any angle of A. It is equal to an angle of C (Step 2), and that angle of C is equal to an angle of B (Step 3). Things which are equal to the same thing are also equal to one another [CN1]; therefore the angle of A is equal to the angle of B. Since this holds for every angle, the figures A and B have their angles severally equal, corresponding angles being those which are equal to the same angle of C.

**Step 5.** Now let a1, a2 be the sides of A about one of its angles, let c1, c2 be the corresponding sides of C about the angle of C equal to it, and let b1, b2 be the corresponding sides of B about the angle of B equal to the same angle of C. By Step 2, a1 : a2 = c1 : c2; by Step 3, b1 : b2 = c1 : c2.

**Step 6.** Ratios which are the same with the same ratio are also the same with one another [5.11]; therefore a1 : a2 = b1 : b2. Since this holds for the sides about every pair of equal angles, the sides of A and B about the equal angles are proportional.

**Step 7.** Therefore A and B have their angles severally equal (Step 4) and the sides about the equal angles proportional (Step 6); hence by D6.1, A is similar to B.

**Step 8.** Therefore figures which are similar to the same rectilineal figure are also similar to one another. Q.E.D.

**USED:** 5.11, CN1, D6.1
**Human refs (from References field):** D6.1
**Jaccard:** 0.333 — AI adds ['5.11', 'CN1']

## Proposition 6.22
**Statement:** If four straight lines be proportional, the rectilineal figures similar and similarly described upon them will also be proportional; and, if the rectilineal figures similar and similarly described upon them be proportional, the straight lines will themselves also be proportional.

## Proposition 6.22
**Statement:** If four straight lines be proportional, the rectilineal figures similar and similarly described upon them will also be proportional; and, if the rectilineal figures similar and similarly described upon them be proportional, the straight lines will themselves also be proportional.

Let AB, CD, EF, GH be four straight lines, and let similar and similarly situated rectilineal figures KAB, LCD be described on AB, CD, and similar and similarly situated rectilineal figures MF, NH on EF, GH.

**Part I.** Let AB : CD = EF : GH; to prove KAB : LCD = MF : NH.

**Step 1.** Take a third proportional O to AB, CD, and a third proportional P to EF, GH [6.11], so that AB : CD = CD : O and EF : GH = GH : P.

**Step 2.** Since CD : O = AB : CD, AB : CD = EF : GH (hypothesis), and EF : GH = GH : P, we have CD : O = GH : P [5.11]. Thus the three lines AB, CD, O and the three lines EF, GH, P are proportional taken two and two (AB : CD = EF : GH and CD : O = GH : P); therefore, ex aequali, AB : O = EF : P [5.22].

**Step 3.** Since AB, CD, O are three proportional straight lines, AB has to O the ratio duplicate of that which AB has to CD [D5.9]. But the similar and similarly situated figures KAB, LCD are to one another in the ratio duplicate of that of the corresponding sides AB, CD [6.20; 6.19 when the figures are triangles]. Hence KAB : LCD = AB : O; that is, as the first of three proportional lines is to the third, so is the figure on the first to the similar and similarly described figure on the second (the porism of 6.19 and 6.20).

**Step 4.** In the same way, since EF, GH, P are three proportional straight lines, MF : NH = EF : P [D5.9, 6.19, 6.20].

**Step 5.** By Step 2, AB : O = EF : P; therefore, by Steps 3 and 4, KAB : LCD = MF : NH [5.11]. This proves the first part.

**Part II.** Conversely, let KAB : LCD = MF : NH; to prove AB : CD = EF : GH.

**Step 6.** With O, P taken as in Step 1 [6.11], Steps 3 and 4 give KAB : LCD = AB : O and MF : NH = EF : P. Since KAB : LCD = MF : NH by hypothesis, AB : O = EF : P [5.11].

**Step 7.** Take a fourth proportional X to the three straight lines AB, CD, EF [6.12], so that AB : CD = EF : X, and a third proportional Y to EF, X [6.11], so that EF : X = X : Y.

**Step 8.** Since CD : O = AB : CD = EF : X = X : Y [5.11], the lines AB, CD, O and the lines EF, X, Y are proportional taken two and two (AB : CD = EF : X and CD : O = X : Y); therefore, ex aequali, AB : O = EF : Y [5.22].

**Step 9.** From Steps 6 and 8, EF : P = EF : Y [5.11]; and magnitudes to which the same has the same ratio are equal, so P = Y [5.9]. Consequently X has to the equal lines Y, P the same ratio, X : Y = X : P [5.7], and therefore EF : X = X : P [5.11].

**Step 10.** I say that X = GH. For if not, one of them is greater. First let X > GH. Then the same line EF has to the less, GH, a greater ratio than to the greater, X: EF : GH > EF : X [5.8]. But EF : GH = GH : P (Step 1) and EF : X = X : P (Step 9); therefore GH : P > X : P [5.13]. Hence, of magnitudes having a ratio to the same P, that which has the greater ratio is greater: GH > X [5.10], which contradicts X > GH. Next let GH > X. Then EF : X > EF : GH [5.8]; therefore X : P > GH : P [5.13], so X > GH [5.10], which contradicts GH > X. Therefore X = GH.

**Step 11.** Since X = GH, the same line EF has to X and to GH the same ratio: EF : X = EF : GH [5.7]. But AB : CD = EF : X (Step 7); therefore AB : CD = EF : GH [5.11]. This proves the second part.

Therefore, if four straight lines be proportional, the rectilineal figures similar and similarly described upon them are also proportional; and if the figures be proportional, the straight lines are themselves proportional.

**Path note.** The converse is settled by comparing the fourth proportional X with GH directly through the Book V ratio inequalities (Step 10), rather than by describing on X a figure similar to MF and then appealing to a separate lemma that equal and similar figures have equal corresponding sides; the direct route needs no such lemma and reuses only the third-proportional machinery already set up in Part I.

**USED:** D5.9, 5.7, 5.8, 5.9, 5.10, 5.11, 5.13, 5.22, 6.11, 6.12, 6.19, 6.20

**USED:** 5.10, 5.11, 5.13, 5.22, 5.7, 5.8, 5.9, 6.11, 6.12, 6.19, 6.20, D5.9
**Human refs (from References field):** 5.11, 5.22, 5.9, 6.11, 6.12, 6.18, 6.19
**Jaccard:** 0.462 — AI adds ['5.10', '5.13', '5.7', '5.8', '6.20', 'D5.9']; Human adds ['6.18']

## Proposition 6.23
**Statement:** Equiangular parallelograms have to one another the ratio compounded of the ratios of their sides.

## Proposition 6.23
**Statement:** Equiangular parallelograms have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let AC and CF be equiangular parallelograms — AC the parallelogram ABCD and CF the parallelogram CEFG — having the angle BCD equal to the angle ECG. I say that AC has to CF the ratio compounded of the ratio of BC to CG and the ratio of DC to CE, the sides about the equal angles.

**Step 2.** Let the parallelograms be placed so that BC and CG lie in one straight line BG, C falling between B and G, and so that D and E lie on opposite sides of BG.

**Step 3.** Since the straight line DC stands on the straight line BG at C, the adjacent angles BCD, DCG are together equal to two right angles [1.13].

**Step 4.** The angle ECG is equal to the angle BCD; let the angle DCG be added to each. Then the angles ECG, DCG are together equal to the angles BCD, DCG [CN2], and therefore are together equal to two right angles [CN1].

**Step 5.** Hence at the point C on the straight line CG, the two straight lines CD, CE, not lying on the same side of CG, make the adjacent angles DCG, GCE together equal to two right angles; therefore CE is in a straight line with DC [1.14]. Call this straight line DE.

**Step 6.** Through D draw DH parallel to CG, and through G draw GH parallel to CD [1.31]; let them meet at H, so that DCGH is a parallelogram, which call CH. It has the side DC in common with AC and the side CG in common with CF.

**Step 7.** The parallelograms AC and CH have their bases BC, CG in the one straight line BG and share the side DC, so that the perpendicular from D to BG is the height of each [D6.4]; they are therefore under the same height. Hence, as BC is to CG, so is the parallelogram AC to the parallelogram CH [6.1].

**Step 8.** Again, the parallelograms CH and CF have their bases DC, CE in the one straight line DE and share the side CG, so that the perpendicular from G to DE is the height of each [D6.4]; they are therefore under the same height. Hence, as DC is to CE, so is the parallelogram CH to the parallelogram CF [6.1].

**Step 9.** Now the three parallelograms AC, CH, CF form a chain in which AC has a ratio to CH and CH has a ratio to CF; the ratio of the extremes, AC to CF, is by definition the ratio compounded of the ratio of AC to CH and the ratio of CH to CF [D6.5].

**Step 10.** But the ratio of AC to CH is the same as the ratio of BC to CG, and the ratio of CH to CF is the same as the ratio of DC to CE (Steps 7 and 8). Therefore the ratio of AC to CF is compounded of the ratio of BC to CG and the ratio of DC to CE, that is, of the ratios of the sides about the equal angles [D6.5].

Therefore equiangular parallelograms have to one another the ratio compounded of the ratios of their sides. Q.E.D.

*Path note.* An equivalent route first embodies the compound ratio in three auxiliary straight lines K, L, M by taking fourth proportionals to the sides, and then carries it over to the parallelograms by the equality of ratios and the ex aequali theorem; it rests on the same two applications of 6.1. The route above is chosen as the more direct, because the chain AC, CH, CF already exhibits the compound ratio without auxiliary lines.

**USED:** CN1, CN2, D6.4, D6.5, 1.13, 1.14, 1.31, 6.1

**USED:** 1.13, 1.14, 1.31, 6.1, CN1, CN2, D6.4, D6.5
**Human refs (from References field):** 5.11, 6.1, 6.12
**Jaccard:** 0.100 — AI adds ['1.13', '1.14', '1.31', 'CN1', 'CN2', 'D6.4', 'D6.5']; Human adds ['5.11', '6.12']

## Proposition 6.24
**Statement:** In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.

**Step 1.** Let ABCD be a parallelogram and AC its diameter. Let F be a point on AC, and let AEFG and FHCK be the parallelograms about the diameter AC, E lying on AB, G on AD, H on DC and K on BC, so that EF, FH are in one straight line EH and GF, FK are in one straight line GK. Since AEFG is a parallelogram, EF is parallel to AG, that is, to AD, and GF is parallel to AE, that is, to AB. But AD is parallel to BC and AB is parallel to DC; therefore EF is parallel to BC, and GF is parallel to DC [1.30].

**Step 2.** Since GF is parallel to DC, one of the sides of the triangle ADC, and cuts AD in G and AC in F, therefore DG : GA = CF : FA [6.2].

**Step 3.** Since EF is parallel to BC, one of the sides of the triangle ABC, and cuts AB in E and AC in F, therefore CF : FA = BE : EA [6.2].

**Step 4.** Therefore DG : GA = BE : EA [5.11].

**Step 5.** Componendo, DA : AG = BA : AE [5.18].

**Step 6.** Alternately, DA : AB = GA : AE [5.16]. Thus in the parallelograms ABCD and AEFG the sides about the common angle BAD are proportional.

**Step 7.** Since GF is parallel to DC and the straight line AC falls upon them, the exterior angle AFG is equal to the interior and opposite angle ACD; and since the straight line AD falls upon them, the exterior angle AGF is equal to the interior and opposite angle ADC [1.29]. The angle DAC is common to the two triangles ADC, AGF. Therefore the triangle ADC is equiangular with the triangle AGF.

**Step 8.** Hence in the triangles ADC, AGF the sides about the equal angles are proportional [6.4]: AD : DC = AG : GF, and DC : CA = GF : FA.

**Step 9.** Similarly, since EF is parallel to BC and the straight lines AC, AB fall upon them, the angle AFE is equal to the angle ACB and the angle AEF is equal to the angle ABC [1.29], while the angle BAC is common; therefore the triangle ABC is equiangular with the triangle AEF, and [6.4] CB : BA = FE : EA, and AC : CB = AF : FE.

**Step 10.** Since DC : CA = GF : FA (Step 8) and CA : CB = FA : FE (Step 9), therefore ex aequali DC : CB = GF : FE [5.22].

**Step 11.** Again, the angle EFG is equal to the opposite angle EAG of the parallelogram AEFG, and the angle BCD is equal to the opposite angle BAD of the parallelogram ABCD [1.34]; and the angle EAG is the same angle as the angle BAD; therefore the angle EFG is equal to the angle BCD [CN1]. Together with Steps 7 and 9, the parallelogram ABCD is therefore equiangular with the parallelogram AEFG: the angle BAD is the angle EAG, the angle ABC is equal to the angle AEF, the angle BCD is equal to the angle EFG, and the angle ADC is equal to the angle AGF.

**Step 12.** Moreover the sides about the equal angles are proportional: about the angles BAD, EAG, DA : AB = GA : AE (Step 6); about the angles ADC, AGF, AD : DC = AG : GF (Step 8); about the angles BCD, EFG, DC : CB = GF : FE (Step 10); and about the angles CBA, FEA, CB : BA = FE : EA (Step 9). Therefore the parallelogram ABCD is similar to the parallelogram AEFG [D6.1].

**Step 13.** In the same manner, since KF is parallel to BA, one of the sides of the triangle CBA, and HF is parallel to DA, one of the sides of the triangle CDA, we have BK : KC = AF : FC and DH : HC = AF : FC [6.2], so that BK : KC = DH : HC [5.11], whence componendo BC : CK = DC : CH [5.18] and alternately BC : DC = CK : CH [5.16]. The triangle CBA is equiangular with the triangle CKF and the triangle CDA with the triangle CHF, the angle at C being common and the remaining angles equal by parallels [1.29]; hence CB : BA = CK : KF, BA : AC = KF : FC, CD : DA = CH : HF and AC : AD = FC : FH [6.4], and ex aequali BA : AD = KF : FH [5.22]. Also the angle KFH is equal to the angle KCH, which is equal to the angle BAD [1.34, CN1]. Therefore the parallelogram ABCD is equiangular with the parallelogram FHCK and has the sides about the equal angles proportional, so that ABCD is similar to FHCK [D6.1].

**Step 14.** Therefore each of the parallelograms AEFG, FHCK is similar to the whole parallelogram ABCD. But figures which are similar to the same rectilineal figure are also similar to one another [6.21]; therefore the parallelogram AEFG is also similar to the parallelogram FHCK.

**Step 15.** Therefore in any parallelogram the parallelograms about the diameter are similar both to the whole and to one another. Q.E.D.

**USED:** 1.29, 1.30, 1.34, 5.11, 5.16, 5.18, 5.22, 6.2, 6.21, 6.4, CN1, D6.1
**Human refs (from References field):** 5.16, 5.18, 5.22, 6.2, 6.21, D6.1
**Jaccard:** 0.500 — AI adds ['1.29', '1.30', '1.34', '5.11', '6.4', 'CN1']

## Proposition 6.25
**Statement:** To construct one and the same figure similar to a given rectilineal figure and equal to another given rectilineal figure.

**Step 1.** Let ABC be the given rectilineal figure to which the required figure is to be similar, BC being one of its sides, and let D be the given rectilineal figure to which the required figure is to be equal.

**Step 2.** Apply to the straight line BC, in any angle CBL, the parallelogram BCEL (call it BE) equal to the figure ABC [1.44; if ABC is not a triangle, divide it into triangles and apply to BC parallelograms equal to them in succession in the same angle, as in 1.45, the result being a single parallelogram BE on BC equal to ABC].

**Step 3.** Apply to the straight line CE, in the angle FCE equal to the angle CBL, the parallelogram CFME (call it CM) equal to the figure D [1.44, 1.45 as in Step 2], F lying on the side of CE remote from B.

**Step 4.** Since BL is parallel to CE (opposite sides of the parallelogram BE) and BC falls upon them, the interior angles CBL, BCE on the same side are together equal to two right angles [1.29]. But the angle FCE is equal to the angle CBL (Step 3); therefore the angles FCE, BCE are together equal to two right angles [CN2, CN1]. Hence the straight line CE, standing at C on the two straight lines BC, CF, makes the adjacent angles together equal to two right angles, so that BC is in a straight line with CF [1.14].

**Step 5.** In the parallelogram BE the opposite angles CBL, CEL are equal [1.34]; and since CF is parallel to EM (opposite sides of the parallelogram CM) and CE falls upon them, the angles FCE, CEM are together equal to two right angles [1.29]. Since the angle CEL is equal to the angle CBL, that is, to the angle FCE, the angles CEL, CEM are together equal to two right angles [CN1, CN2]; hence LE is in a straight line with EM [1.14].

**Step 6.** Thus the parallelograms BE and CM have their bases BC, CF on the one straight line BF and their opposite sides LE, EM on the one straight line LM, which is parallel to BF; they are therefore under the same height, and so BE : CM = BC : CF [6.1].

**Step 7.** Take GH a mean proportional between BC and CF [6.13], so that BC : GH = GH : CF.

**Step 8.** On GH describe the rectilineal figure KGH similar and similarly situated to ABC, the side GH corresponding to the side BC [6.18].

**Step 9.** Since BC, GH, CF are three proportional straight lines, BC has to CF the ratio duplicate of that which BC has to GH [D5.9]. And the figure ABC has to the similar figure KGH the ratio duplicate of that which the corresponding side BC has to the corresponding side GH [6.20; when ABC is a triangle this is 6.19]. Therefore BC : CF = ABC : KGH.

**Step 10.** But BC : CF = BE : CM (Step 6). Therefore ABC : KGH = BE : CM [5.11].

**Step 11.** Now ABC is equal to BE (Step 2), and equal magnitudes have the same ratio to the same magnitude; therefore ABC : KGH = BE : KGH [5.7]. Hence BE : KGH = BE : CM [5.11].

**Step 12.** Magnitudes to which the same magnitude has the same ratio are equal; therefore KGH = CM [5.9].

**Step 13.** But CM is equal to D (Step 3); therefore KGH is equal to D [CN1]. And KGH is similar to ABC (Step 8). Hence one and the same figure KGH has been constructed similar to the given rectilineal figure ABC and equal to the other given rectilineal figure D. Q.E.F.

*Path note:* From ABC : KGH = BE : CM (Step 10) one could instead alternate [5.16] to ABC : BE = KGH : CM and conclude by 5.14; the route through 5.7 and 5.9 is the more direct and is the one taken.

**USED:** 1.14, 1.29, 1.34, 1.44, 1.45, 5.11, 5.7, 5.9, 6.1, 6.13, 6.18, 6.19, 6.20, CN1, CN2, D5.9
**Human refs (from References field):** 1.44, 1.45, 5.16, 6.1, 6.13, 6.18, 6.19
**Jaccard:** 0.353 — AI adds ['1.14', '1.29', '1.34', '5.11', '5.7', '5.9', '6.20', 'CN1', 'CN2', 'D5.9']; Human adds ['5.16']

## Proposition 6.26
**Statement:** If from a parallelogram there be taken away a parallelogram similar and similarly situated to the whole and having a common angle with it, it is about the same diameter with the whole.

**Step 1.** Let ABCD be a parallelogram, and from it let there be taken away the parallelogram AEFG, similar and similarly situated to ABCD and having the angle DAB common with it; so that E lies on AB, G lies on AD, the sides AE, AG of AEFG lie along the sides AB, AD of ABCD, and the vertex F falls within ABCD. Join AC, the diameter of the parallelogram ABCD [P1]. I say that AEFG is about the same diameter with ABCD, that is, that F lies on AC. Suppose, if possible, that F does not lie on AC.

**Step 2.** Since AEFG is a parallelogram, its opposite sides are parallel: GF is parallel to AE, that is, to AB, and EF is parallel to AG, that is, to AD. Produce GF [P2]. The straight line AC is not parallel to GF; for otherwise AB and AC, being each parallel to GF, would be parallel to one another [1.30] and so would never meet [D1.23], whereas they meet at A. Hence AC and GF produced meet. Moreover, since G lies between A and D, while DC is parallel to GF (each being parallel to AB [1.30]), the points A and C lie on opposite sides of the straight line GF; so the meeting point, call it H, lies on the diameter AC between A and C.

**Step 3.** Through H draw HK parallel to AD [1.31], and let it meet AB at K. (It does meet AB: AB and AD meet at A and so are not parallel, and a straight line parallel to AD cannot also be parallel to AB, for then AB and AD would be parallel to one another [1.30] and would not meet [D1.23].) Since H lies within the parallelogram ABCD and HK is parallel to AD, the point K lies on AB on the same side of A as B, and therefore on the same side of A as E.

**Step 4.** Then AKHG is a parallelogram, for AK is parallel to GH and AG is parallel to KH; and since its vertex H lies on the diameter AC, it is a parallelogram about the diameter AC of ABCD, having the angle DAB common with it. Therefore AKHG is similar to ABCD [6.24].

**Step 5.** Now K is not the same point as E. For if K coincided with E, then HK would be a straight line drawn through E parallel to AD; but EF is also a straight line drawn through E parallel to AD. If HK and EF were different straight lines, being each parallel to AD they would be parallel to one another [1.30] and would not meet [D1.23]; but they meet at E. Hence HK and EF would be one and the same straight line, so that H would lie on the straight line EF. But H lies also on the straight line GF; and EF, GF are different straight lines (they contain the angle EFG of the parallelogram AEFG), which cannot have two points in common without enclosing a space. Therefore H would coincide with F, and F would lie on the diameter AC, contrary to the supposition. Hence K is not E; and since K and E lie on AB on the same side of A, one of the straight lines AK, AE is a part of the other.

**Step 6.** Since AKHG is similar to ABCD, the angle at A being common and the sides GA, AK lying along DA, AB respectively, the sides about the common angle are proportional [D6.1]: as DA is to AB, so is GA to AK.

**Step 7.** Again, since AEFG is similar and similarly situated to ABCD, the angle at A being common and the sides GA, AE lying along DA, AB respectively, the sides about the common angle are proportional [D6.1]: as DA is to AB, so is GA to AE.

**Step 8.** Therefore, ratios which are the same with the same ratio being the same with one another [5.11], as GA is to AK, so is GA to AE. Thus the same magnitude GA has the same ratio to each of AK, AE; therefore AK is equal to AE [5.9].

**Step 9.** But by Step 5 one of AK, AE is a part of the other; so the part would be equal to the whole, which is impossible, since the whole is greater than the part [CN5].

**Step 10.** Therefore the supposition is false, and F lies on the diameter AC. That is, the parallelogram AEFG taken away from ABCD is about the same diameter AC with the whole parallelogram ABCD. Q.E.D.

**USED:** 1.30, 1.31, 5.11, 5.9, 6.24, CN5, D1.23, D6.1, P1, P2
**Human refs (from References field):** 1.31, 5.11, 5.9, 6.24
**Jaccard:** 0.400 — AI adds ['1.30', 'CN5', 'D1.23', 'D6.1', 'P1', 'P2']

## Proposition 6.27
**Statement:** Of all the parallelograms applied to the same straight line and deficient by parallelogrammic figures similar and similarly situated to that described on the half of the straight line, that parallelogram is greatest which is applied to the half of the straight line and is similar to the defect.

**Step 1.** Let AB be the given straight line, and let it be bisected at C [1.10]. Let AD be the parallelogram applied to AB which is deficient by the parallelogram DB described on the half CB: AD stands on the base AC, DB stands on the base CB, CD is their common side, and together they make up the parallelogram AE on the whole of AB, whose sides AL, BE are parallel to CD and whose side LDE is one straight line parallel to AB. Thus AD is the parallelogram applied to the half AC and deficient by DB, the figure described on the other half. I say that AD is the greatest of all the parallelograms applied to AB and deficient by parallelogrammic figures similar and similarly situated to DB.

**Step 2.** Let AF be any other parallelogram applied to AB and deficient by a parallelogram FB similar and similarly situated to DB, and let K be the point of AB at which AF and FB meet: AF stands on AK, FB stands on KB, KF is their common side, and together they make up a parallelogram AH on the whole of AB. Because FB is similarly situated to DB, the angle at B is common to them, so that the side BH of FB lies along BE, the sides AG, KF of the figure are parallel to BE, that is, to CD, and GFH is one straight line parallel to AB. Since AF is other than AD, K is other than C, so that K lies either between C and B or between A and C.

**Step 3.** Join DB [P1]. The parallelograms DB and FB are similar and similarly situated and have the common angle at B, the lesser of them being taken away from the greater; therefore they are about the same diameter [6.26]. Hence F lies on the straight line DB: if K is between C and B, then F is between D and B; if K is between A and C, then D is between F and B.

**Step 4.** The parallelograms AD and DB are on the equal bases AC, CB and in the same parallels AB, LE; therefore AD = DB [1.36]. It remains to show that DB > AF.

*Case 1: K between C and B.*

**Step 5.** Here FB lies within DB. The straight line GFH cuts CD at a point N; let KF be produced to meet DE at R [P2]. Then in the parallelogram DB, whose diameter is DB, the parallelograms about the diameter are FB and DF (namely NFRD), and the complements are CF (namely CKFN) and FE (namely FHER).

**Step 6.** The complements are equal: CF = FE [1.43].

**Step 7.** Add the parallelogram FB to each; then CF together with FB is equal to FE together with FB [CN2]. But CF and FB together make up the parallelogram CH (namely CBHN), and FE and FB together make up the parallelogram KE (namely KBER). Therefore CH = KE.

**Step 8.** The parallelograms CG (namely ACNG) and CH are on the equal bases AC, CB and in the same parallels AB, GH; therefore CG = CH [1.36].

**Step 9.** Since CG = CH and CH = KE, CG = KE [CN1].

**Step 10.** Add the parallelogram CF to each; then CG together with CF is equal to KE together with CF [CN2]. But CG and CF together make up the parallelogram AF (namely AKFG); and KE together with CF is composed of FB, FE and CF, that is, it is the parallelogram DB with the parallelogram DF taken away. Therefore AF is equal to DB with DF taken away.

**Step 11.** But DB with DF taken away is a part of DB; therefore DB is greater than it [CN5], that is, DB > AF. Since AD = DB (Step 4), AD > AF.

*Case 2: K between A and C.*

**Step 12.** Here DB lies within FB, and D is on the diameter FB of the parallelogram FB. The side KF of FB cuts LD at a point Q; let CD be produced to meet GH at P [P2]. Then in the parallelogram FB, whose diameter is FB, the parallelograms about the diameter are DB and FD (namely QDPF), and the complements are KD (namely KCDQ) and DH (namely DEHP).

**Step 13.** The complements are equal: KD = DH [1.43].

**Step 14.** The parallelograms AP (namely ACPG) and CH (namely CBHP) are on the equal bases AC, CB and in the same parallels AB, GH; therefore AP = CH [1.36].

**Step 15.** Now AP is made up of the parallelogram AF (namely AKFG) and the parallelogram KP (namely KCPF), and KP is made up of the complement KD and the parallelogram FD; so AP is made up of AF, KD and FD together. And CH is made up of the parallelogram DB and the complement DH. Therefore AF, KD, FD together are equal to DB, DH together.

**Step 16.** Since KD = DH, take these equals away from those equals: AF together with FD is equal to DB [CN3].

**Step 17.** Therefore AF is a part of a figure equal to DB, so that DB > AF [CN5]. Since AD = DB (Step 4), AD > AF.

**Step 18.** Therefore in either case AD > AF. Hence, of all the parallelograms applied to AB and deficient by parallelogrammic figures similar and similarly situated to DB, the parallelogram AD, which is applied to the half AC and is similar to the defect DB, is the greatest. Q.E.D.

*Path note:* the gnomon argument of Case 1 (F between D and B) does not transfer verbatim to Case 2 (D between F and B), so Case 2 is proved separately with the same tools (1.43 and 1.36) rather than by an appeal to symmetry; both cases reduce to the identity "AF together with the parallelogram on DF equals DB".

**USED:** 1.10, 1.36, 1.43, 6.26, CN1, CN2, CN3, CN5, P1, P2
**Human refs (from References field):** 1.36, 1.43, 6.26
**Jaccard:** 0.300 — AI adds ['1.10', 'CN1', 'CN2', 'CN3', 'CN5', 'P1', 'P2']

## Proposition 6.28
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and deficient by a parallelogrammic figure similar to a given one: thus the given rectilineal figure must not be greater than the parallelogram described on the half of the straight line and similar to the defect.

## Proposition 6.28
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and deficient by a parallelogrammic figure similar to a given one: thus the given rectilineal figure must not be greater than the parallelogram described on the half of the straight line and similar to the defect.

Let AB be the given straight line, C the given rectilineal figure, and D the given parallelogram to which the defect is to be similar; and let C be not greater than the parallelogram described on the half of AB and similar to D.

**Step 1.** Bisect AB at E [1.10], so that AE = EB.

**Step 2.** On EB describe the parallelogram EBFG similar and similarly situated to D [6.18]. EBFG is the parallelogram described on the half EB of AB and similar to the defect D; hence, by hypothesis, C is not greater than EBFG. (Write GB for EBFG.)

**Step 3.** Through A draw AH parallel to EG [1.31], and produce FG to meet it at H [P2]. Since GF is parallel to EB, HG is parallel to AE; and AH is parallel to EG; therefore AEGH is a parallelogram (write AG for it).

**Step 4.** AEGH and EBFG are parallelograms on the equal bases AE, EB and in the same parallels AB, HF; therefore AEGH = EBFG [1.36]. Consequently C is not greater than AEGH: either AEGH = C, or AEGH > C.

**Step 5.** If AEGH = C, what was required is done: to AB there has been applied the parallelogram AEGH, standing on the part AE of AB, equal to C and deficient by the parallelogram EBFG on the remaining part EB, which is similar to D.

**Step 6.** Otherwise AEGH > C, and therefore, since EBFG = AEGH, EBFG > C. Construct [6.25] the parallelogram KLMN similar and similarly situated to D and equal to the excess by which EBFG is greater than C; thus EBFG is equal to C and KLMN together, and EBFG > KLMN [CN5]. (Write KM for KLMN.)

**Step 7.** KLMN is similar to D, and EBFG is similar to D; therefore KLMN is similar to EBFG [6.21]. Let KL correspond to GE and LM to GF; then the angle KLM is equal to the angle EGF, and KL : LM = GE : GF [D6.1].

**Step 8.** GE > KL and GF > LM. For suppose KL were not less than GE. Since KL : LM = GE : GF, LM would then not be less than GF [5.14]. Cut off LX = GE from LK and LY = GF from LM [1.3] (X, Y coinciding with K, M in case of equality) and complete the parallelogram XLYZ [1.31]. The two sides LX, LY and the included angle XLY are equal to the two sides GE, GF and the included angle EGF; hence the triangles XLY, EGF are equal [1.4], and the parallelograms XLYZ, EBFG, each double of its triangle [1.34], are equal. But XLYZ is a part of KLMN or the whole of it; so KLMN would not be less than EBFG [CN5], contrary to Step 6. Hence KL < GE, and therefore also LM < GF [5.14].

**Step 9.** On GE cut off GO = KL, and on GF cut off GP = LM [1.3], and complete the parallelogram OGPQ [1.31] (write GQ for it). The sides GO, GP and the included angle OGP are equal to KL, LM and the included angle KLM; hence, exactly as in Step 8, the triangles OGP, KLM are equal [1.4] and the parallelograms OGPQ, KLMN are equal [1.34]. Moreover all the sides and angles of OGPQ are equal to those of KLMN, so OGPQ is also similar to KLMN [D6.1].

**Step 10.** OGPQ is similar to KLMN, and KLMN to EBFG; therefore OGPQ is similar to EBFG [6.21]. Now OGPQ is a parallelogram taken away from EBFG, similar and similarly situated to it, and having the angle at G in common with it; therefore it is about the same diameter with EBFG [6.26]. Join GB [P1]; then Q lies on GB.

**Step 11.** Produce OQ in both directions to meet AH at T and BF at R, and produce PQ to meet AB at S [P2]. Then TR is parallel to AB and SQ to GE. In the parallelogram EBFG with diameter GB, OGPQ and QSBR are the two parallelograms about the diameter, and OESQ, PQRF are the complements. Write QB, OS, PR for QSBR, OESQ, PQRF, and TS, TE, OB, PB for the parallelograms TASQ, TAEO, OEBR, PFBS.

**Step 12.** QSBR, being a parallelogram about the diameter of EBFG, is similar to EBFG [6.24], and therefore to D [6.21].

**Step 13.** EBFG is equal to C and KM together (Step 6), and OGPQ = KM (Step 9). Taking away OGPQ from EBFG, the remainder, namely the gnomon made up of OS, QB and PR, is equal to C [CN3].

**Step 14.** The complements PR and OS are equal [1.43]. Add QB to each; then PB (= PR together with QB) is equal to OB (= OS together with QB) [CN2].

**Step 15.** OB and TE are parallelograms on the equal bases EB, AE and in the same parallels AB, TR; therefore OB = TE [1.36]. Hence TE = PB [CN1].

**Step 16.** Add OS to each: TE together with OS is the parallelogram TS, and PB together with OS is the gnomon. Therefore TS is equal to the gnomon [CN2]; and the gnomon was proved equal to C (Step 13); therefore TS = C [CN1].

**Step 17.** TS stands on the part AS of AB, and together with QB, which stands on the remaining part SB, it makes up the parallelogram TABR on the whole of AB. Thus to the given straight line AB there has been applied the parallelogram TS, equal to the given rectilineal figure C and deficient by the parallelogrammic figure QB, which is similar to D (Step 12). This is what was required. Q.E.F.

Path note: the parallelogram GQ is placed inside GB by cutting off its two sides GO, GP and completing it, after which 6.26 shows it lies about the diameter GB; the alternative of first drawing the diameter GB, locating Q on it and using 6.24 for the similarity was not taken, because the chosen route yields GQ = KM directly from the equal sides and included angle.

**USED:** P1, P2, CN1, CN2, CN3, CN5, D6.1, 1.3, 1.4, 1.10, 1.31, 1.34, 1.36, 1.43, 5.14, 6.18, 6.21, 6.24, 6.25, 6.26

**USED:** 1.10, 1.3, 1.31, 1.34, 1.36, 1.4, 1.43, 5.14, 6.18, 6.21, 6.24, 6.25, 6.26, CN1, CN2, CN3, CN5, D6.1, P1, P2
**Human refs (from References field):** 1.36, 6.18, 6.21, 6.25, 6.26
**Jaccard:** 0.250 — AI adds ['1.10', '1.3', '1.31', '1.34', '1.4', '1.43', '5.14', '6.24', 'CN1', 'CN2', 'CN3', 'CN5', 'D6.1', 'P1', 'P2']

## Proposition 6.29
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and exceeding by a parallelogrammic figure similar to a given one.

**Step 1.** Let AB be the given straight line, C the given rectilineal figure, and D the given parallelogram to which the excess is to be similar. Bisect AB at the point E [1.10].

**Step 2.** On EB describe the parallelogram EBLF similar and similarly situated to D [6.18]; call it BF. Its sides FL and FE meet at F, FL is parallel to EB, and BL is parallel to FE.

**Step 3.** Construct the parallelogram KHTG (call it GH; K and T are opposite vertices) similar and similarly situated to D and equal to the sum of BF and C [6.25]. Since BF and GH are each similar to D, they are similar to one another [6.21]; let the angle at K be the angle corresponding to the angle at F, so that KH corresponds to FL and KG to FE. Then the angle HKG is equal to the angle LFE [D6.1].

**Step 4.** Produce FL and FE [P2], and from F along these lines cut off FM equal to KH and FN equal to KG [1.3]. Through M draw MO parallel to FN, and through N draw NO parallel to FM [1.31], meeting at O. Then FMON is a parallelogram (call it MN); its sides FM, FN about the angle MFN are equal to KH, KG respectively, and the angle MFN is the angle LFE, which is equal to the angle HKG.

**Step 5.** Join the straight lines MN and HG [P1]. In the triangles FMN, KHG the sides FM, FN are equal to the sides KH, KG respectively and the included angles MFN, HKG are equal; hence the triangles are equal, the base MN is equal to the base HG, the angle FMN to the angle KHG, and the angle FNM to the angle KGH [1.4]. The diameter MN bisects the parallelogram FMON and the diameter HG bisects the parallelogram KHTG [1.34]; therefore the parallelogram FMON, being double the triangle FMN, is equal to the parallelogram KHTG, which is double the triangle KHG [CN2].

**Step 6.** Further, since in a parallelogram the opposite sides and angles are equal [1.34], OM = FN = KG = TH, ON = FM = KH = TG, and the angle MON = the angle MFN = the angle HKG = the angle HTG [CN1]. Hence the triangles OMN, THG likewise have two sides and the included angle equal, so that the angle OMN = the angle THG and the angle ONM = the angle TGH [1.4]. Adding, the angle FMO = the angle KHT and the angle FNO = the angle KGT [CN2]; together with the equalities of the angles at F and K and at O and T, this shows that the parallelograms MN and GH are equiangular, and their sides about the equal angles, being respectively equal, are proportional. Therefore MN is similar to GH [D6.1].

**Step 7.** Since MN is similar to GH, and BF is similar to GH (Step 3), MN is similar to BF [6.21], the angle at F of MN corresponding to the angle at F of BF, FM to FL, and FN to FE; hence FM : FN = FL : FE [D6.1]. Also MN = GH (Step 5) and GH = BF together with C (Step 3), so MN is equal to BF together with C [CN1]; hence MN is greater than BF [CN5].

**Step 8.** FM is greater than FL. For if FM = FL, then FN = FE [5.14]; M would coincide with L and N with E, and MN would be BF itself, so that MN = BF, contrary to Step 7. And if FM < FL, then FN < FE [5.14]; M would lie between F and L and N between F and E, and the parallelogram MN, having its sides FM, FN along FL, FE and shorter than them, would be a part of BF, so that MN < BF [CN5], again contrary to Step 7. Therefore FM > FL, and consequently FN > FE [5.14]; thus L lies between F and M, E lies between F and N, and BF lies within MN.

**Step 9.** Thus from the parallelogram MN there is taken away the parallelogram BF, similar and similarly situated to MN and having with it the common angle at F; therefore BF is about the same diameter as MN [6.26]. Join FO [P1]: FO is the diameter of MN, and the point B lies on it.

**Step 10.** Produce EB to meet MO at P, and LB to meet NO at Q [P2]; through A draw AR parallel to FN, meeting NO produced beyond N at R [1.31, P2]. Now EB, that is the straight line AP, is parallel to FL (Step 2), and NO is parallel to FM (Step 4); hence AP is parallel to NO [1.30]. Likewise LB is parallel to FE (Step 2), while AR and MO are each parallel to FN; hence LQ, AR and MO are parallel to one another [1.30]. Consequently LMPB, BPOQ, EBQN, AENR, EPON and APOR are all parallelograms. In the parallelogram MN with diameter FO, the parallelograms FLBE (that is, BF) and BPOQ are the parallelograms about the diameter, and LMPB and EBQN are the complements.

**Step 11.** The whole parallelogram MN consists of BF together with the gnomon formed by the parallelogram BPOQ about the diameter and the two complements LMPB, EBQN [D2.2]. Since MN is equal to BF together with C (Step 7), subtracting BF from each, the gnomon is equal to C [CN3].

**Step 12.** Since AE = EB (Step 1), the parallelograms AENR and EBQN, being on the equal bases AE, EB and in the same parallels AP, RQ, are equal [1.36]. And EBQN is equal to LMPB, these being the complements about the diameter FO of the parallelogram MN [1.43]. Therefore AENR = LMPB [CN1].

**Step 13.** Add to each the parallelogram EPON, which is made up of EBQN and BPOQ. Then AENR together with EPON is the parallelogram APOR, while LMPB together with EPON is the gnomon (LMPB, BPOQ, EBQN); hence APOR is equal to the gnomon [CN2], and therefore APOR is equal to C [CN1].

**Step 14.** The parallelogram APOR is applied to the straight line AB: its side AP contains AB, and it exceeds the parallelogram ABQR standing on AB by the parallelogram BPOQ standing on BP. Since BPOQ and FLBE are the parallelograms about the diameter FO of MN, BPOQ is similar to FLBE, that is, to BF [6.24]; and BF is similar to D (Step 2); therefore BPOQ is similar to D [6.21].

**Step 15.** Therefore to the given straight line AB there has been applied the parallelogram APOR, equal to the given rectilineal figure C and exceeding by the parallelogram BPOQ, which is similar to the given parallelogram D. Q.E.F.

*Path note.* The inequality FM > FL (needed so that BF lies inside MN before 6.26 can be invoked) is established by fitting MN against BF at the common angle F using 5.14 and CN5, which is more direct here than the alternative route through the duplicate ratio of 6.20; and the equality of the parallelograms MN, GH is obtained from congruent triangles (1.4, 1.34) rather than from 6.14, whose reciprocal-proportion condition would require ratios of equal lines.

**USED:** 1.10, 1.3, 1.30, 1.31, 1.34, 1.36, 1.4, 1.43, 5.14, 6.18, 6.21, 6.24, 6.25, 6.26, CN1, CN2, CN3, CN5, D2.2, D6.1, P1, P2
**Human refs (from References field):** 1.36, 1.43, 6.21, 6.24, 6.25, 6.26
**Jaccard:** 0.273 — AI adds ['1.10', '1.3', '1.30', '1.31', '1.34', '1.4', '5.14', '6.18', 'CN1', 'CN2', 'CN3', 'CN5', 'D2.2', 'D6.1', 'P1', 'P2']

## Proposition 6.30
**Statement:** To cut a given finite straight line in extreme and mean ratio.

**Step 1.** Let AB be the given finite straight line. It is required to cut AB in extreme and mean ratio, that is, to find a point on AB such that, as the whole AB is to the greater segment, so is the greater segment to the less [D6.3].

**Step 2.** Cut AB at the point C so that the rectangle contained by the whole AB and the segment BC is equal to the square on the remaining segment AC [2.11].

**Step 3.** Consider the three straight lines AB, AC, CB. The rectangle contained by the extremes AB and CB is equal to the square on the mean AC (Step 2); therefore the three straight lines are proportional: as AB is to AC, so is AC to CB [6.17].

**Step 4.** Since AC is a part of the whole AB, AB is greater than AC [CN5].

**Step 5.** In the proportion AB : AC = AC : CB, the first magnitude AB is greater than the third magnitude AC; therefore the second magnitude AC is also greater than the fourth magnitude CB [5.14]. Hence AC is the greater segment of AB and CB the less.

**Step 6.** Therefore, as the whole AB is to the greater segment AC, so is the greater segment AC to the less segment CB; that is, AB has been cut in extreme and mean ratio at the point C, AC being the greater segment [D6.3]. Q.E.F.

*Path note:* An alternative route describes the square on AB [1.46], applies to a side of that square a parallelogram equal to the square and exceeding by a square [6.29], and then obtains the proportion from the equal, equiangular parallelograms by [6.14]. The route through [2.11] and [6.17] is chosen here as the most direct: by [6.17] the required proportion is equivalent to the rectangle-equals-square condition, which [2.11] constructs immediately.

**USED:** 2.11, 5.14, 6.17, CN5, D6.3
**Human refs (from References field):** 6.14, 6.29
**Jaccard:** 0.000 — AI adds ['2.11', '5.14', '6.17', 'CN5', 'D6.3']; Human adds ['6.14', '6.29']

## Proposition 6.31
**Statement:** In right - angled triangles the figure on the side subtending the right angle is equal to the similar and similarly described figures on the sides containing the right angle.

## Proposition 6.31
**Statement:** In right-angled triangles the figure on the side subtending the right angle is equal to the similar and similarly described figures on the sides containing the right angle.

Let ABC be a right-angled triangle having the angle BAC right. Let a rectilineal figure P be described on BC, and on BA and AC let figures Q and R be described similar and similarly described to P. I say that P is equal to Q and R together.

**Step 1.** From the point A let AD be drawn perpendicular to the straight line BC [1.12], meeting BC at D.

**Step 2.** Since ABC is a right-angled triangle and AD has been drawn from the right angle A perpendicular to the base BC, the triangles DBA, DAC adjoining the perpendicular are similar both to the whole triangle ABC and to one another [6.8].

**Step 3.** Since the triangle DBA is similar to the triangle ABC, their angles are severally equal [D6.1]: the angle DBA is the angle ABC itself, the angle BDA is equal to the right angle BAC, and the remaining angle BAD is equal to the remaining angle BCA. In the triangle DBA the side BA subtends the right angle BDA, and in the triangle ABC the side BC subtends the right angle BAC; hence BA and BC are corresponding sides, so that the triangles DBA, ABC are similar rectilineal figures similarly described upon BA and BC.

**Step 4.** Likewise, since the triangle DAC is similar to the triangle ABC, the angle DCA is the angle BCA itself, the angle ADC is equal to the right angle BAC, and the remaining angle DAC is equal to the remaining angle ABC [D6.1]. In the triangle DAC the side AC subtends the right angle ADC, and in the triangle ABC the side BC subtends the right angle BAC; hence AC and BC are corresponding sides, so that the triangles DAC, ABC are similar rectilineal figures similarly described upon AC and BC.

**Step 5.** Now Q and P are similar and similarly described upon BA and BC (by hypothesis), the triangles DBA and ABC are similar and similarly described upon BA and BC (Step 3), and the four straight lines BA, BC, BA, BC are proportional, since BA is to BC as BA is to BC. But if four straight lines be proportional, the rectilineal figures similar and similarly described upon them are also proportional [6.22]. Therefore, as Q is to P, so is the triangle DBA to the triangle ABC.

**Step 6.** Again, R and P are similar and similarly described upon AC and BC (by hypothesis), the triangles DAC and ABC are similar and similarly described upon AC and BC (Step 4), and AC is to BC as AC is to BC. Therefore [6.22], as R is to P, so is the triangle DAC to the triangle ABC.

**Step 7.** Since Q has to P the same ratio as the triangle DBA has to the triangle ABC, and R has to the same P the same ratio as the triangle DAC has to the same triangle ABC, therefore Q and R added together have to P the same ratio as the triangles DBA and DAC added together have to the triangle ABC [5.24].

**Step 8.** But D lies on BC, and the straight line AD divides the triangle ABC into the two triangles DBA and DAC; hence the triangles DBA and DAC added together are the whole triangle ABC. Therefore, as Q and R together are to P, so is the triangle ABC to the triangle ABC.

**Step 9.** These four magnitudes are all areas; therefore, alternately [5.16], as Q and R together are to the triangle ABC, so is P to the triangle ABC.

**Step 10.** But magnitudes which have the same ratio to the same are equal to one another [5.9]. Therefore Q and R together are equal to P; that is, the figure on BC, the side subtending the right angle, is equal to the similar and similarly described figures on BA and AC, the sides containing the right angle. Q.E.D.

**USED:** 1.12, 6.8, D6.1, 6.22, 5.24, 5.16, 5.9

Path note: an equivalent route obtains the continued proportion CB : BA = BA : BD from D6.1 and applies the porism to 6.19; the route above via 6.22 was chosen because it keeps every proportion among magnitudes of one kind (areas), so that the alternation in Step 9 is legitimate.

**USED:** 1.12, 5.16, 5.24, 5.9, 6.22, 6.8, D6.1
**Human refs (from References field):** 6.19, 6.8, D6.1
**Jaccard:** 0.250 — AI adds ['1.12', '5.16', '5.24', '5.9', '6.22']; Human adds ['6.19']

## Proposition 6.32
**Statement:** If two triangles having two sides proportional to two sides be placed together at one angle so that their corresponding sides are also parallel, the remaining sides of the triangles will be in a straight line.

## Proposition 6.32
**Statement:** If two triangles having two sides proportional to two sides be placed together at one angle so that their corresponding sides are also parallel, the remaining sides of the triangles will be in a straight line.

**Setting out.** Let ABC, DCE be two triangles having the two sides BA, AC proportional to the two sides DC, DE, so that, as BA is to AC, so is DC to DE; and let them be placed together at the point C so that the corresponding sides are parallel, namely AB parallel to DC and AC parallel to DE, the triangle DCE lying on the side of AC remote from B, with CD falling within the angle ACE. I say that BC is in a straight line with CE.

**Step 1.** Since AB is parallel to DC, and the straight line AC has fallen upon them, the alternate angles BAC, ACD are equal to one another [1.29].

**Step 2.** Again, since AC is parallel to DE, and the straight line DC has fallen upon them, the alternate angles ACD, CDE are equal to one another [1.29].

**Step 3.** Therefore, since each of the angles BAC, CDE is equal to the angle ACD, the angle BAC is equal to the angle CDE [CN1].

**Step 4.** Now the triangles ABC, DCE have one angle equal to one angle, namely the angle BAC equal to the angle CDE, and the sides about these equal angles proportional, for as BA is to AC, so is CD to DE. Therefore the triangle ABC is equiangular with the triangle DCE, and it has those angles equal which the corresponding sides subtend [6.6]; hence the angle ABC, which the side AC subtends, is equal to the angle DCE, which the corresponding side DE subtends.

**Step 5.** But the angle ACD was proved equal to the angle BAC (Step 1). Therefore the whole angle ACE, being made up of the angles ACD, DCE, is equal to the two angles BAC, ABC taken together [CN2].

**Step 6.** Let the angle ACB be added to each; therefore the angles ACE, ACB are together equal to the three angles BAC, ABC, ACB [CN2].

**Step 7.** But the three angles BAC, ABC, ACB of the triangle ABC are together equal to two right angles [1.32].

**Step 8.** Therefore the angles ACE, ACB are also together equal to two right angles [CN1].

**Step 9.** Thus with the straight line AC, and at the point C on it, the two straight lines CB, CE, not lying on the same side of AC, make the adjacent angles ACB, ACE equal to two right angles. Therefore BC is in a straight line with CE [1.14].

Therefore, if two triangles having two sides proportional to two sides be placed together at one angle so that their corresponding sides are also parallel, the remaining sides of the triangles will be in a straight line. Q.E.D.

**USED:** 1.29, CN1, 6.6, CN2, 1.32, 1.14

**Path note:** The route is direct and essentially forced: parallels give the equal angles at A and D (1.29 applied twice), the proportion then triggers 6.6, and the angle sum at C is closed off by 1.32 and 1.14. No equivalent alternative route was available at this stage of Book 6.

**USED:** 1.14, 1.29, 1.32, 6.6, CN1, CN2
**Human refs (from References field):** 1.14, 1.29, 1.32, 6.6
**Jaccard:** 0.667 — AI adds ['CN1', 'CN2']

## Proposition 6.33
**Statement:** In equal circles angles have the same ratio as the circumferences on which they stand, whether they stand at the centres or at the circumferences.

**Step 1.** Let ABC and DEF be equal circles with centres G and H. Let the angle BGC at the centre G and the angle BAC at the circumference both stand upon the circumference BC, and let the angle EHF at the centre H and the angle EDF at the circumference both stand upon the circumference EF. We must show that, as the circumference BC is to the circumference EF, so is the angle BGC to the angle EHF, and so also is the angle BAC to the angle EDF.

**Step 2.** On the circle ABC take any number of consecutive circumferences CK, KL, ... each equal to the circumference BC, proceeding from C in the direction away from B; and on the circle DEF take any number of consecutive circumferences FM, MN, ... each equal to the circumference EF, proceeding from F away from E. Join the straight lines GK, GL, HM, HN [P1].

**Step 3.** Since the circumferences BC, CK, KL are equal to one another in the same circle, the angles BGC, CGK, KGL which stand upon them at the centre are equal to one another [3.27]. The angle BGL is made up of these adjacent angles just as the circumference BL is made up of the circumferences BC, CK, KL; therefore, whatever multiple the circumference BL is of the circumference BC, the same multiple is the angle BGL of the angle BGC.

**Step 4.** In the same way, since the circumferences EF, FM, MN are equal, the angles EHF, FHM, MHN are equal to one another [3.27]; therefore, whatever multiple the circumference EN is of the circumference EF, the same multiple is the angle EHN of the angle EHF.

**Step 5.** Now compare the circumference BL with the circumference EN. (a) If the circumference BL is equal to the circumference EN, then, the circles being equal, the angle BGL is equal to the angle EHN [3.27]. (b) If the circumference BL is greater than the circumference EN, cut off from BL, beginning at B, a circumference BX equal to EN, so that X lies on the circumference BL between B and L, and join GX [P1]; then the angle BGX is equal to the angle EHN, since they stand upon equal circumferences in equal circles [3.27]; but the angle BGL is greater than the angle BGX, since BGX is a part of BGL [CN5]; therefore the angle BGL is greater than the angle EHN. (c) Similarly, if the circumference BL is less than the circumference EN, cutting off from EN a circumference equal to BL shows that the angle BGL is less than the angle EHN.

**Step 6.** We therefore have four magnitudes: the circumference BC, the circumference EF, the angle BGC, and the angle EHF. Of the first and third we have taken arbitrary equimultiples, the circumference BL and the angle BGL; of the second and fourth we have taken arbitrary equimultiples, the circumference EN and the angle EHN; and it has been shown that the circumference BL exceeds, equals, or falls short of the circumference EN according as the angle BGL exceeds, equals, or falls short of the angle EHN. Therefore, as the circumference BC is to the circumference EF, so is the angle BGC to the angle EHF [D5.5].

**Step 7.** Next, the angle BGC at the centre and the angle BAC at the circumference have the same circumference BC as base; therefore the angle BGC is double of the angle BAC [3.20]. Likewise the angle EHF is double of the angle EDF [3.20].

**Step 8.** Thus the angle BAC is half of the angle BGC and the angle EDF is half of the angle EHF, so that BGC and EHF are the same multiples (doubles) of BAC and EDF respectively. Since parts have the same ratio as the same multiples of them taken in corresponding order, as the angle BAC is to the angle EDF, so is the angle BGC to the angle EHF [5.15].

**Step 9.** But as the circumference BC is to the circumference EF, so is the angle BGC to the angle EHF (Step 6); and as the angle BGC is to the angle EHF, so is the angle BAC to the angle EDF (Step 8). Ratios which are the same with the same ratio are the same with one another; therefore, as the circumference BC is to the circumference EF, so is the angle BAC to the angle EDF [5.11]. Hence in equal circles the angles, whether at the centres or at the circumferences, have the same ratio as the circumferences on which they stand. Q.E.D.

**USED:** 3.20, 3.27, 5.11, 5.15, CN5, D5.5, P1
**Human refs (from References field):** 3.27, D5.5
**Jaccard:** 0.286 — AI adds ['3.20', '5.11', '5.15', 'CN5', 'P1']
