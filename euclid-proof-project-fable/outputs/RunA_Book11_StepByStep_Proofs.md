# Book 11 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 11.1
**Statement:** A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Statement:** A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 1.** Suppose, if possible, that of the straight line ABC the part AB lies in the plane of reference while the part BC lies in a plane more elevated, so that BC does not lie in the plane of reference.

**Step 2.** Since AB is a finite straight line lying in the plane of reference, produce it continuously in a straight line within the plane of reference to a point D [P2]. Then ABD is one straight line, and its part BD lies in the plane of reference.

**Step 3.** BD lies in the plane of reference, whereas BC does not; therefore BC and BD do not coincide. Hence ABC and ABD are two distinct straight lines having the segment AB in common.

**Step 4.** With centre B and distance BA describe a circle [P3]; since it is described with distance BA, the point A lies on its circumference. Let the circumference meet the straight line BC (produced if necessary) at E and the straight line BD (produced if necessary) at F. Because BC and BD are distinct straight lines drawn from B, the points E and F are distinct.

**Step 5.** ABE is a straight line drawn through the centre B and terminated in both directions, at A and at E, by the circumference; therefore AE is a diameter of the circle, and so it bisects the circle [D1.17]. In the same way ABF is a straight line through the centre terminated at A and F by the circumference; therefore AF is also a diameter and bisects the circle [D1.17].

**Step 6.** The three distinct points A, E, F divide the circumference into three circumferences AE, EF, FA, each named by its extremities and containing neither of the other named points. The two circumferences into which the diameter AE divides the circle are the circumference AE and the circumference AFE, the latter being composed of the circumferences AF and FE; since AE bisects the circle, the circumference AFE is equal to the circumference AE. Likewise the diameter AF divides the circle into the circumference AF and the circumference AEF, composed of the circumferences AE and EF; since AF bisects the circle, the circumference AF is equal to the circumference AEF.

**Step 7.** The circumference AEF is greater than its part, the circumference AE [CN5]; and the circumference AF is equal to the circumference AEF; therefore the circumference AF is greater than the circumference AE. Again, the circumference AFE is greater than its part, the circumference AF [CN5]; and the circumference AE is equal to the circumference AFE; therefore the circumference AE is greater than the circumference AF.

**Step 8.** Thus the circumference AF is at once greater and less than the circumference AE, which is impossible. Therefore two straight lines ABC, ABD cannot have the common segment AB, and the supposition of Step 1 cannot hold.

**Step 9.** Therefore a part of a straight line cannot be in the plane of reference and a part in a plane more elevated. Q.E.D.

**USED:** P2, P3, D1.17, CN5

**USED:** CN5, D1.17, P2, P3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN5', 'D1.17', 'P2', 'P3']

## Proposition 11.2
**Statement:** If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

**Step 1.** Let AB, CD be two straight lines cutting one another at the point E. I say that AB, CD are in one plane, and that every triangle is in one plane.

**Step 2.** Join CB [P1]. Then ECB is a triangle, being the figure contained by the three straight lines EC, CB, BE [D1.19].

**Step 3.** I say first that the triangle ECB is in one plane. For, if not, some part of the triangle is in one plane, which we call the plane of reference, while the remainder is in a plane more elevated. Take points F, G at random on EC, EB respectively, and points H, K at random on CB, and join FG, FH, GK [P1]. The part of the triangle lying in the plane of reference is cut off from the remainder by a straight line drawn across the triangle, and the two extremities of this cutting line lie on the boundary of the triangle. They cannot both be at vertices of the triangle, for then the cutting line would coincide with a side and would cut off nothing; hence at least one extremity lies within a side, and that side is divided at it. Thus, if the part in the plane of reference is a corner piece such as the triangle FHC, the side EC is divided at F; if it is a corner piece such as the triangle GBK, the side EB is divided at G; if it is a corner piece such as the triangle EFG, or a strip such as the quadrilateral FCBG lying between FG and CB, both EC and EB are divided, at F and G; and if it is a piece cut off by a line drawn from a vertex to a point of the opposite side, that opposite side is divided.

**Step 4.** Consequently at least one of the straight lines EC, CB, BE has one part in the plane of reference and the remaining part in a plane more elevated. But this is impossible [11.1]. Therefore the triangle ECB is in one plane.

**Step 5.** Now the triangle ECB is contained by the straight lines EC, CB, BE [D1.19]; hence in whatever plane the triangle ECB is, in that same plane are each of the straight lines EC, EB.

**Step 6.** But EC is a part of the straight line CD. If the remainder ED of CD were not in the plane of the triangle ECB, the straight line CD would have the part CE in that plane and a part in a plane more elevated, which is impossible [11.1]. Therefore the whole of CD is in the plane of the triangle ECB. In the same way, since EB is a part of the straight line AB, the whole of AB is in that plane [11.1].

**Step 7.** Therefore the straight lines AB, CD are in one plane.

**Step 8.** Finally, the reasoning of Steps 3 and 4 used nothing about ECB except that it is a triangle contained by three straight lines. Applied to any triangle whatever, it shows that a part of the triangle cannot be in one plane and the remainder in a plane more elevated without some side of the triangle being partly in the one plane and partly in the other, which is impossible [11.1]. Therefore every triangle is in one plane.

Therefore, if two straight lines cut one another, they are in one plane, and every triangle is in one plane. Q.E.D.

**USED:** P1, D1.19, 11.1

**USED:** 11.1, D1.19, P1
**Human refs (from References field):** 11.1
**Jaccard:** 0.333 — AI adds ['D1.19', 'P1']

## Proposition 11.3
**Statement:** If two planes cut one another, their common section is a straight line.

**Step 1.** Let the two planes AB and BC cut one another, and let the line DB be their common section, D and B being two points common to the two planes. I say that DB is a straight line.

**Step 2.** Suppose, if possible, that the common section DB is not a straight line. Since D and B are points of the plane AB, let the straight line DEB be drawn from D to B in the plane AB [P1]; because a plane surface lies evenly with the straight lines on itself, DEB lies wholly in the plane AB [D1.7].

**Step 3.** Again, since D and B are points of the plane BC, let the straight line DFB be drawn from D to B in the plane BC [P1]; for the same reason DFB lies wholly in the plane BC [D1.7].

**Step 4.** The straight line DEB does not lie in the plane BC. For, if it did, every point of DEB would be common to the planes AB and BC, so that DEB, which is a straight line, would be the common section of the two planes from D to B; but by supposition the common section DB is not a straight line. By the same argument DFB does not lie in the plane AB. Hence DEB and DFB are two different straight lines.

**Step 5.** But DEB and DFB have the same extremities D and B. Thus two different straight lines DEB, DFB drawn from D to B would enclose a space, which is impossible, since from the point D to the point B only one straight line can be drawn [P1].

**Step 6.** Therefore the supposition of Step 2 is false, and the common section DB of the planes AB and BC is a straight line. Hence, if two planes cut one another, their common section is a straight line. Q.E.D.

**USED:** D1.7, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D1.7', 'P1']

## Proposition 11.4
**Statement:** If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

## Proposition 11.4
**Statement:** If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

Let the two straight lines AB, CD cut one another at the point E, and let the straight line EF be set up at E at right angles to both AB and CD. I say that EF is also at right angles to the plane through AB, CD.

**Step 1.** Since AB and CD cut one another, they lie in one plane [11.2]. Call this the plane of reference; it is the plane through AB, CD.

**Step 2.** From E cut off the four straight lines EA, EB, EC, ED equal to one another [1.3], so that E bisects both AB and CD. Join AD and CB [P1].

**Step 3.** Let GH be any straight line in the plane of reference passing through E other than AB and CD themselves (for AB and CD the right angles at E hold by hypothesis). Since the four segments EA, EB, EC, ED are equal and the construction is symmetric about E, we may name the extremities so that GH meets AD at G and CB at H, G and H lying on opposite sides of E. Join FA, FG, FD, FC, FH, FB [P1].

**Step 4.** Since the straight lines AB and CD cut one another at E, the vertical angles AED and BEC are equal [1.15]. In the triangles AED, BEC the two sides AE, ED are equal to the two sides BE, EC respectively, and the angle AED is equal to the angle BEC; therefore the base AD is equal to the base BC, and the angle EAD is equal to the angle EBC [1.4].

**Step 5.** Since the straight lines AB and GH cut one another at E, the vertical angles AEG and BEH are equal [1.15]. In the triangles AEG, BEH the angle GAE is equal to the angle HBE (these are the angles EAD, EBC of Step 4, since G lies on AD and H on BC), the angle AEG is equal to the angle BEH, and the side AE adjoining the equal angles is equal to the side BE. Therefore the remaining sides are equal: GE is equal to HE and AG is equal to BH [1.26].

**Step 6.** Since EF is at right angles to AB, each of the angles FEA, FEB is right, so they are equal to one another [P4]. In the triangles FEA, FEB the side EA is equal to EB, EF is common, and the angle FEA is equal to the angle FEB; therefore the base FA is equal to the base FB [1.4]. In the same way, since EF is at right angles to CD, the angles FEC, FED are right and equal [P4], EC is equal to ED, and EF is common; therefore FC is equal to FD [1.4].

**Step 7.** In the triangles FAD, FBC the side FA is equal to FB (Step 6), AD is equal to BC (Step 4), and FD is equal to FC (Step 6). Therefore the angle FAD, contained by FA, AD, is equal to the angle FBC, contained by FB, BC [1.8].

**Step 8.** In the triangles FAG, FBH the side FA is equal to FB, AG is equal to BH (Step 5), and the angle FAG is equal to the angle FBH (these are the angles FAD, FBC of Step 7, since G lies on AD and H on BC). Therefore the base FG is equal to the base FH [1.4].

**Step 9.** In the triangles FEG, FEH the side GE is equal to HE (Step 5), EF is common, and the base FG is equal to the base FH (Step 8). Therefore the angle FEG is equal to the angle FEH [1.8].

**Step 10.** The straight line FE, set up on the straight line GH at E, makes the adjacent angles FEG, FEH equal to one another; therefore each of them is right, and FE is perpendicular to GH [D1.10].

**Step 11.** But GH was any straight line through E in the plane of reference. Hence FE makes right angles with every straight line which meets it and lies in the plane through AB, CD. Therefore FE is at right angles to that plane [D11.3]. Q.E.D.

Path note: the proof is a single congruence chain (1.15 → 1.4 → 1.26 → 1.8 → 1.4 → 1.8) closed by D1.10 and D11.3; no shorter route through later books exists, since only Book 1 congruence theorems are needed.

**USED:** P1, P4, 1.3, 1.4, 1.8, 1.15, 1.26, D1.10, D11.3, 11.2

**USED:** 1.15, 1.26, 1.3, 1.4, 1.8, 11.2, D1.10, D11.3, P1, P4
**Human refs (from References field):** 1.15, 1.26, 1.4, 1.8, D11.3
**Jaccard:** 0.500 — AI adds ['1.3', '11.2', 'D1.10', 'P1', 'P4']

## Proposition 11.5
**Statement:** If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

**Step 1.** Let the straight line AB be set up at right angles to the three straight lines BC, BD, BE at their common point of section B, so that each of the angles ABC, ABD, ABE is right. I say that BC, BD, BE are in one plane. Suppose, if possible, that they are not. Since BD and BE cut one another at B, they lie in one plane [11.2]; call this the plane of reference. Then, by supposition, BC does not lie in the plane of reference but is in a plane more elevated.

**Step 2.** Since AB and BC cut one another at B, they lie in one plane [11.2]. This plane contains the point B of the plane of reference, but it is not the same plane as the plane of reference, since BC lies in it and not in the plane of reference; therefore the two planes cut one another, and their common section is a straight line [11.3]. Let this common section be the straight line BF, drawn through B, and let F be taken on that side of AB on which C lies.

**Step 3.** Therefore the three straight lines AB, BC, BF are in one plane, namely the plane drawn through AB, BC, since BF is the common section of that plane with the plane of reference and so lies in it.

**Step 4.** Now, since AB is at right angles to each of the straight lines BD, BE, which cut one another at B, AB is at right angles to the plane through BD, BE [11.4]. But the plane through BD, BE is the plane of reference; therefore AB is at right angles to the plane of reference.

**Step 5.** Hence AB makes right angles with all the straight lines which meet it and are in the plane of reference [D11.3]. But BF is in the plane of reference and meets AB at B; therefore the angle ABF is right.

**Step 6.** But by hypothesis the angle ABC is also right; therefore the angle ABF is equal to the angle ABC [P4].

**Step 7.** But BF and BC are different straight lines, since BF lies in the plane of reference and BC does not; and they are drawn from the same point B, in the same plane through AB, BC, on the same side of AB. Therefore one of the angles ABF, ABC lies within the other and is a part of it; so the part would be equal to the whole, which is impossible, for the whole is greater than the part [CN5].

**Step 8.** Therefore BC is not in a plane more elevated than the plane of reference; that is, BC lies in the plane through BD, BE. Therefore the three straight lines BC, BD, BE are in one plane. Q.E.D.

**USED:** 11.2, 11.3, 11.4, D11.3, P4, CN5

**USED:** 11.2, 11.3, 11.4, CN5, D11.3, P4
**Human refs (from References field):** 11.3, 11.4, D11.3
**Jaccard:** 0.500 — AI adds ['11.2', 'CN5', 'P4']

## Proposition 11.6
**Statement:** If two straight lines be at right angles to the same plane, the straight lines will be parallel.

**Step 1.** Let AB and CD be two straight lines at right angles to the plane of reference, meeting it at the points B and D respectively. Join the straight line BD (P1).

**Step 2.** In the plane of reference draw DE at right angles to BD (1.11), and cut off DE equal to AB (1.3). Join BE, AE and AD (P1).

**Step 3.** Since AB is at right angles to the plane of reference, it makes right angles with every straight line which meets it and lies in that plane (D11.3). The straight lines BD and BE lie in the plane of reference and meet AB at B; therefore each of the angles ABD, ABE is right.

**Step 4.** For the same reason, since CD is at right angles to the plane of reference, and DB, DE lie in that plane and meet CD at D, each of the angles CDB, CDE is right (D11.3).

**Step 5.** The angles ABD and EDB are both right, so they are equal to one another (P4). In the triangles ABD, EDB the two sides AB, BD are equal to the two sides ED, DB respectively (AB = ED by construction, BD common), and the included angles ABD, EDB are equal; therefore the base AD is equal to the base EB (1.4).

**Step 6.** In the triangles ABE, EDA the side AB is equal to the side ED, the side BE is equal to the side DA (Step 5), and the base AE is common. Therefore the angle ABE, contained by AB, BE, is equal to the angle EDA, contained by ED, DA (1.8). But the angle ABE is right (Step 3); therefore the angle EDA is also right, so that ED is at right angles to DA.

**Step 7.** Thus ED is at right angles to DB (Step 2), to DA (Step 6) and to DC (Step 4). ED has therefore been set up at right angles to the three straight lines DB, DA, DC at their common point of section D; consequently DB, DA, DC are in one plane (11.5).

**Step 8.** DB and DA cut one another at D, so they lie in one plane, and the triangle ABD lies in that same plane (11.2); hence AB lies in the plane containing DB and DA. By Step 7, DC also lies in the plane containing DB and DA. Therefore AB and CD are in one plane.

**Step 9.** AB and CD are two straight lines in one plane, and the straight line BD falls on them making the interior angles ABD, BDC on the same side each right (Steps 3 and 4), so that together they are equal to two right angles. Therefore AB is parallel to CD (1.28).

**Step 10.** Therefore, if two straight lines be at right angles to the same plane, the straight lines will be parallel. Q.E.D.

**USED:** 1.11, 1.28, 1.3, 1.4, 1.8, 11.2, 11.5, D11.3, P1, P4
**Human refs (from References field):** 1.28, 1.4, 1.8, 11.2, 11.5, D11.3
**Jaccard:** 0.600 — AI adds ['1.11', '1.3', 'P1', 'P4']

## Proposition 11.7
**Statement:** If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

**Step 1.** Let AB and CD be two parallel straight lines, and let E be any point taken on AB and F any point taken on CD. Since AB and CD are parallel, they are straight lines lying in one plane (D1.23); call this plane the plane of reference. The points E and F, being points of AB and CD respectively, are therefore in the plane of reference.

**Step 2.** Join the straight line from E to F (P1). I say that the straight line joining E and F is in the plane of reference.

**Step 3.** For suppose it is not. Then the straight line joining E to F contains some point G which is not in the plane of reference, so that the line lies in a more elevated position; let it be denoted EGF.

**Step 4.** Through the straight line EGF let a plane be drawn. This plane is different from the plane of reference, since it contains the point G while the plane of reference does not; and the two planes cut one another, since they have the point E (and likewise the point F) in common. Therefore their common section is a straight line (11.3).

**Step 5.** The point E is in the plane of reference (Step 1) and also in the plane drawn through EGF (Step 4); hence E lies on the common section of the two planes. In the same way F lies on the common section. Therefore the common section is a straight line drawn from E to F lying wholly in the plane of reference; let it be EF.

**Step 6.** Thus EGF and EF are two straight lines each having the same extremities E and F, and they are distinct straight lines, since the point G lies on EGF but not on EF (every point of EF being in the plane of reference, whereas G is not). Consequently the two straight lines EGF and EF would enclose a space.

**Step 7.** But this is impossible: a straight line is a line which lies evenly with the points on itself (D1.4), so that the straight line drawn from the point E to the point F is one and the same (P1), and two distinct straight lines cannot have the same two extremities, that is, cannot enclose a space.

**Step 8.** Therefore the straight line joining E to F is not in a more elevated plane; hence it is in the plane of reference, that is, in the same plane with the parallel straight lines AB and CD. Q.E.D.

**USED:** 11.3, D1.23, D1.4, P1
**Human refs (from References field):** 11.3
**Jaccard:** 0.250 — AI adds ['D1.23', 'D1.4', 'P1']

## Proposition 11.8
**Statement:** If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

**Step 1.** Let AB, CD be two parallel straight lines, and let one of them, AB, be at right angles to the plane of reference; let AB, CD meet the plane of reference at the points B, D. I say that CD is also at right angles to the plane of reference.

**Step 2.** Join BD [P1]. Since B, D are points taken on the parallel straight lines AB, CD, the straight line BD lies in the same plane as AB, CD [11.7]; call this plane Π.

**Step 3.** In the plane of reference draw DE at right angles to BD at the point D [1.11], and cut off DE equal to AB [1.3]. Join BE, AE, AD [P1].

**Step 4.** Since AB is at right angles to the plane of reference, it makes right angles with all straight lines which meet it and lie in that plane [D11.3]. BD and BE meet AB at B and lie in the plane of reference; therefore each of the angles ABD, ABE is right.

**Step 5.** Since the straight line BD falls on the parallel straight lines AB, CD, the interior angles on the same side, ABD and CDB, are together equal to two right angles [1.29]. But the angle ABD is right; subtracting it from the sum, the remaining angle CDB is a right angle [CN3]. Therefore CD is at right angles to BD.

**Step 6.** In the triangles ABD, EDB, the side AB is equal to the side ED (Step 3), and BD is common to both; and the angle ABD is equal to the angle EDB, for both are right angles [P4]. Therefore the base AD is equal to the base BE [1.4].

**Step 7.** In the triangles ABE, EDA, the two sides AB, BE are equal to the two sides ED, DA respectively (AB = ED by Step 3, BE = DA by Step 6), and the base AE is common. Therefore the angle ABE, contained by AB, BE, is equal to the angle EDA, contained by ED, DA [1.8]. But the angle ABE is right (Step 4); therefore the angle EDA is right, and ED is at right angles to DA.

**Step 8.** ED is at right angles to DB (Step 3) and to DA (Step 7), and DB, DA cut one another at D. Therefore ED is at right angles to the plane through BD, DA [11.4], and hence ED makes right angles with every straight line which meets it and lies in that plane [D11.3].

**Step 9.** The triangle ABD lies in one plane [11.2], so AB and BD lie in the plane through BD, DA. But CD lies in the plane Π which contains AB and BD (Step 2). Since AB, BD cut one another at B, the plane through BD, DA and the plane Π are one and the same plane; therefore DC lies in the plane through BD, DA. DC meets ED at D; hence, by Step 8, the angle EDC is right, that is, CD is at right angles to DE.

**Step 10.** Thus CD is at right angles to each of the straight lines DE, DB (Steps 9 and 5), which cut one another at D. Therefore CD is at right angles to the plane through DE, DB [11.4]. But DE and DB both lie in the plane of reference, so the plane through DE, DB is the plane of reference.

**Step 11.** Therefore CD is at right angles to the plane of reference. Q.E.D.

**USED:** 1.11, 1.29, 1.3, 1.4, 1.8, 11.2, 11.4, 11.7, CN3, D11.3, P1, P4
**Human refs (from References field):** 1.29, 11.2, 11.4, 11.7, D11.3
**Jaccard:** 0.417 — AI adds ['1.11', '1.3', '1.4', '1.8', 'CN3', 'P1', 'P4']

## Proposition 11.9
**Statement:** Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

## Proposition 11.9
**Statement:** Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

**Step 1.** Let each of the straight lines AB, CD be parallel to the straight line EF, and let neither AB nor CD be in the same plane with EF. I say that AB is parallel to CD. Since AB is parallel to EF, the straight lines AB, EF lie in one plane [D1.23]; call it the plane through EF, AB. Likewise, since CD is parallel to EF, the straight lines CD, EF lie in one plane [D1.23]; call it the plane through EF, CD. By hypothesis these are two distinct planes.

**Step 2.** Let a point G be taken at random on EF. In the plane through EF, AB let GH be drawn from the point G at right angles to EF [1.11], and in the plane through EF, CD let GK be drawn from the point G at right angles to EF [1.11].

**Step 3.** The straight lines GH, GK are not in one straight line. For the two distinct planes through EF, AB and through EF, CD have the straight line EF in common, so they cut one another, and their common section is a straight line [11.3]; since this common section contains EF, it is the straight line EF itself. If GH, GK were in one straight line HK, then HK, lying in both planes, would lie in their common section EF; but GH makes a right angle with EF at G, so HK does not lie along EF. Therefore GH, GK are two straight lines which cut one another at G.

**Step 4.** Since the straight line EF is set up at right angles to the two straight lines GH, GK, which cut one another, at their common point of section G, EF is at right angles to the plane through GH, GK [11.4].

**Step 5.** Since EF and AB are parallel, and EF is at right angles to the plane through GH, GK, the remaining straight line AB is also at right angles to the plane through GH, GK [11.8]. For the same reason, since EF and CD are parallel, CD is also at right angles to the plane through GH, GK [11.8].

**Step 6.** Therefore each of the straight lines AB, CD is at right angles to the same plane, namely the plane through GH, GK. But if two straight lines are at right angles to the same plane, they are parallel [11.6]. Therefore AB is parallel to CD. Q.E.D.

**USED:** D1.23, 1.11, 11.3, 11.4, 11.6, 11.8

**USED:** 1.11, 11.3, 11.4, 11.6, 11.8, D1.23
**Human refs (from References field):** 11.4, 11.6, 11.8
**Jaccard:** 0.500 — AI adds ['1.11', '11.3', 'D1.23']

## Proposition 11.10
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.

**Step 1.** Let AB, BC be two straight lines meeting one another at B, and DE, EF two straight lines meeting one another at E, such that AB is parallel to DE and BC is parallel to EF, the pair AB, BC not being in the same plane as the pair DE, EF. It is required to prove that the angle ABC is equal to the angle DEF.

**Step 2.** Cut off BA equal to ED and BC equal to EF [1.3], the points being taken so that A and D lie towards the same parts of the parallels BA, ED, and C and F towards the same parts of the parallels BC, EF. Join AD, CF, BE, AC and DF [P1].

**Step 3.** Since BA is equal and parallel to ED, and AD, BE join their extremities in the same directions, AD is equal and parallel to BE [1.33].

**Step 4.** In the same way, since BC is equal and parallel to EF, and CF, BE join their extremities in the same directions, CF is equal and parallel to BE [1.33].

**Step 5.** The straight lines AD and CF are not in the same plane with BE. For AD is parallel to BE (Step 3), and A, B are points on AD, BE respectively, so AB lies in the plane of AD, BE; likewise D, E are points on AD, BE, so DE lies in that plane [11.7]. Again CF is parallel to BE (Step 4), and C, B and F, E are points on CF, BE respectively, so BC and EF lie in the plane of CF, BE [11.7]. Hence, if AD, CF and BE were in one plane, the straight lines AB, BC, DE, EF would all lie in that plane, contrary to the hypothesis that AB, BC and DE, EF are not in the same plane.

**Step 6.** Since AD and CF are each parallel to the same straight line BE, and are not in the same plane with it, AD is parallel to CF [11.9].

**Step 7.** Since AD is equal to BE and CF is equal to BE, AD is equal to CF [CN1].

**Step 8.** Thus AD, CF are equal and parallel, and AC, DF join their extremities in the same directions (A and C being the extremities on the side of B, D and F those on the side of E); therefore AC is equal and parallel to DF [1.33].

**Step 9.** In the triangles ABC, DEF, the two sides AB, BC are equal to the two sides DE, EF respectively (Step 2), and the base AC is equal to the base DF (Step 8); therefore the angle ABC is equal to the angle DEF [1.8].

**Step 10.** Therefore, if two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they contain equal angles. Q.E.D.

**USED:** 1.3, 1.33, 1.8, 11.7, 11.9, CN1, P1
**Human refs (from References field):** 1.33, 1.8, 11.9
**Jaccard:** 0.429 — AI adds ['1.3', '11.7', 'CN1', 'P1']

## Proposition 11.11
**Statement:** From a given elevated point to draw a straight line perpendicular to a given plane.

**Statement:** From a given elevated point to draw a straight line perpendicular to a given plane.

**Step 1.** Let A be the given elevated point and let the plane of reference be the given plane. Take any two points B, C in the plane of reference and join the straight line BC (P1); BC lies in the plane of reference. Since A is elevated above the plane, A is not on BC; so from A draw AD perpendicular to BC, meeting it at D (1.12). By D1.10 the angles ADB, ADC are right, so BC is at right angles to DA at D.

**Step 2.** If AD is at right angles to the plane of reference, the required straight line has been drawn and the construction is complete. Suppose then that AD is not at right angles to the plane of reference.

**Step 3.** In the plane of reference, from the point D on BC draw DE at right angles to BC (1.11). Then BC is at right angles to DE at D. From A draw AF perpendicular to DE, meeting it at F (1.12); by D1.10 the angle AFD is right, so AF is at right angles to DE at F. Finally, in the plane of reference, through F draw GH parallel to BC (1.31).

**Step 4.** The straight lines DA and DE cut one another at D, and BC is at right angles to each of them at that common point (Steps 1 and 3). Therefore BC is at right angles to the plane through DA, DE (11.4).

**Step 5.** GH is parallel to BC (Step 3), and BC is at right angles to the plane through DA, DE (Step 4). Therefore GH is also at right angles to the plane through DA, DE (11.8).

**Step 6.** Since GH is at right angles to the plane through DA, DE, it makes right angles with every straight line that meets it and lies in that plane (D11.3). Now AF was drawn from A, a point of that plane, to F, a point of DE, and so lies in the plane through DA, DE; and AF meets GH at F. Therefore GH makes a right angle with AF, that is, AF is at right angles to GH at F.

**Step 7.** AF is at right angles to DE at F (Step 3) and at right angles to GH at F (Step 6), and DE and GH cut one another at F. Therefore AF is at right angles to the plane through DE, GH (11.4).

**Step 8.** But DE and GH were both drawn in the plane of reference, so the plane through DE, GH is the plane of reference itself. Therefore AF is at right angles to the plane of reference, that is, AF makes right angles with every straight line meeting it in that plane (D11.3).

**Step 9.** Therefore from the given elevated point A the straight line AF has been drawn perpendicular to the given plane. Q.E.F.

**USED:** P1, D1.10, D11.3, 1.11, 1.12, 1.31, 11.4, 11.8

**USED:** 1.11, 1.12, 1.31, 11.4, 11.8, D1.10, D11.3, P1
**Human refs (from References field):** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3
**Jaccard:** 0.750 — AI adds ['D1.10', 'P1']

## Proposition 11.12
**Statement:** To set up a straight line at right angles to a given plane from a given point in it.

**Statement:** To set up a straight line at right angles to a given plane from a given point in it.

**Step 1.** Let the given plane be the plane of reference, and let A be the given point in it. It is required to set up from A a straight line at right angles to the plane of reference.

**Step 2.** Let any point B be conceived elevated above the plane of reference, that is, a point not lying in the plane.

**Step 3.** From the elevated point B draw the straight line BC perpendicular to the plane of reference, meeting the plane at the point C [11.11].

**Step 4.** If the point C coincides with A, then BC is itself a straight line set up from A at right angles to the plane of reference, and what was required has been done.

**Step 5.** Otherwise, C is a point of the plane distinct from A. Join AC [P1]. Since the straight lines AC and BC cut one another at C, they lie in one plane [11.2]; call this plane Π. The point A and the straight line BC are therefore both in Π.

**Step 6.** In the plane Π, through the point A draw the straight line AD parallel to BC [1.31].

**Step 7.** Now BC and AD are two parallel straight lines, and one of them, BC, is at right angles to the plane of reference (Step 3). Therefore the remaining one, AD, is also at right angles to the plane of reference [11.8].

**Step 8.** Therefore the straight line AD has been set up at right angles to the given plane from the given point A in it, which was required.

**USED:** P1, 1.31, 11.2, 11.8, 11.11

**USED:** 1.31, 11.11, 11.2, 11.8, P1
**Human refs (from References field):** 1.31, 11.11, 11.8
**Jaccard:** 0.600 — AI adds ['11.2', 'P1']

## Proposition 11.13
**Statement:** From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

**Step 1.** Let the plane of reference be given and let A be a point in it. Suppose, if possible, that from the point A two distinct straight lines AB and AC are set up at right angles to the plane of reference on the same side of it.

**Step 2.** Since AB and AC are two straight lines which meet one another at A, they lie in one plane [11.2]. Let this plane be called Π.

**Step 3.** Since AB is set up on one side of the plane of reference, it does not lie in that plane; hence Π is not the plane of reference. But both planes contain the point A, so they cut one another, and their common section is a straight line [11.3]. Let this straight line be DAE, with D and E points of it on either side of A.

**Step 4.** Since CA is at right angles to the plane of reference, it makes right angles with all the straight lines which meet it and lie in the plane of reference [D11.3]. Now AE meets CA at A and lies in the plane of reference, being part of the common section DAE. Therefore the angle CAE is right.

**Step 5.** For the same reason, since BA is at right angles to the plane of reference and AE meets it and lies in that plane, the angle BAE is also right [D11.3].

**Step 6.** Since the angles CAE and BAE are both right, they are equal to one another [P4].

**Step 7.** Now the straight lines AB, AC and DAE all lie in the one plane Π, and every point of Π which lies in the plane of reference lies on the common section DAE. Since AB and AC are on the same side of the plane of reference, they lie on the same side of the straight line DAE within Π. Thus AB and AC are two distinct straight lines drawn from A in the plane Π on the same side of AE; hence one of them falls within the angle contained by the other and AE. That is, either AB falls within the angle CAE, so that the angle BAE is a part of the angle CAE, or AC falls within the angle BAE, so that the angle CAE is a part of the angle BAE.

**Step 8.** In either case one of the two angles is a part of the other, and the whole is greater than the part [CN5]. Hence the angles CAE and BAE are unequal, which contradicts Step 6.

**Step 9.** Therefore the supposition is impossible. From the same point two straight lines cannot be set up at right angles to the same plane on the same side. Q.E.D.

**USED:** 11.2, 11.3, CN5, D11.3, P4
**Human refs (from References field):** 11.3, D11.3
**Jaccard:** 0.400 — AI adds ['11.2', 'CN5', 'P4']

## Proposition 11.14
**Statement:** Planes to which the same straight line is at right angles will be parallel.

**Step 1.** Let the straight line AB be at right angles to each of the planes CD and EF, meeting the plane CD at the point A and the plane EF at the point B. I say that the planes CD, EF are parallel.

**Step 2.** Suppose they are not parallel. Since parallel planes are those which do not meet (D11.8), the planes CD, EF, being not parallel, meet one another when produced.

**Step 3.** Since the two planes CD, EF cut one another, their common section is a straight line (11.3); let it be GH. The straight line GH lies in both of the planes CD and EF.

**Step 4.** Take a point K at random on GH, and join the straight lines AK, BK (P1). Since K is on GH, the point K lies in the plane CD and also in the plane EF.

**Step 5.** Since the points A and K are both in the plane CD, the straight line AK lies in the plane CD; and since the points B and K are both in the plane EF, the straight line BK lies in the plane EF.

**Step 6.** Now AB is at right angles to the plane EF; therefore it makes right angles with all the straight lines which meet it and are in the plane EF (D11.3). But BK meets AB at B and is in the plane EF; therefore the angle ABK is right.

**Step 7.** Again, AB is at right angles to the plane CD; therefore it makes right angles with all the straight lines which meet it and are in the plane CD (D11.3). But AK meets AB at A and is in the plane CD; therefore the angle BAK is right.

**Step 8.** Thus in the triangle ABK each of the two angles ABK, BAK is right, so that the two angles ABK, BAK taken together are equal to two right angles. But in any triangle two angles taken together in any manner are less than two right angles (1.17). This is impossible.

**Step 9.** Therefore the planes CD, EF do not meet one another when produced; hence, since parallel planes are those which do not meet (D11.8), the planes CD, EF are parallel.

Therefore planes to which the same straight line is at right angles are parallel. Q.E.D.

**USED:** 1.17, 11.3, D11.3, D11.8, P1
**Human refs (from References field):** 1.17, 11.3, D11.3, D11.8
**Jaccard:** 0.800 — AI adds ['P1']

## Proposition 11.15
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

**Statement.** If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

**Setup.** Let AB, BC be two straight lines meeting one another at B, and DE, EF two straight lines meeting one another at E; let AB be parallel to DE and BC parallel to EF, and let AB, BC not lie in the same plane as DE, EF. Call the plane through AB, BC the plane P, and the plane through DE, EF the plane Q. I say that plane P is parallel to plane Q.

**Step 1.** The point B does not lie in plane Q. For suppose it did. Since AB is parallel to DE, B is not on DE, because parallel straight lines do not meet [D1.23]; so through B, in the plane Q, draw BL parallel to DE [1.31]. Then AB and BL are both parallel to DE. If AB and BL were distinct straight lines, they would be parallel to one another — by 1.30 if they lie in one plane with DE, by 11.9 if they do not — and yet they meet at B, which is impossible for parallel straight lines [D1.23]. Hence AB coincides with BL and therefore lies in plane Q. In the same way BC lies in plane Q. But then AB, BC would be in the same plane as DE, EF, contrary to hypothesis. Therefore B is a point elevated above plane Q.

**Step 2.** From the elevated point B draw BG perpendicular to plane Q, meeting it at G [11.11].

**Step 3.** Through G draw, in plane Q, GH parallel to ED and GK parallel to EF [1.31]. (If G happens to lie on ED, let GH be ED itself; likewise, if G lies on EF, let GK be EF itself.)

**Step 4.** Since BG is at right angles to plane Q, it makes right angles with all the straight lines which meet it and lie in that plane [D11.3]. Now GH and GK lie in plane Q and meet BG at G; therefore each of the angles BGH, BGK is right.

**Step 5.** BA is parallel to GH. If GH is ED itself, this is the hypothesis. Otherwise BA and GH are both parallel to ED, and they are not in one plane with ED: for if BA, GH, ED lay in one plane R, then R would be distinct from Q (since B, and hence BA, is not in Q by Step 1), so the common section of R and Q would be a straight line [11.3]; but that common section contains both ED and GH, two distinct parallel straight lines which do not lie in one straight line — which is impossible. Hence BA and GH, being parallel to the same straight line ED and not in the same plane with it, are parallel to one another [11.9]. In the same way BC is parallel to GK.

**Step 6.** Since BA and GH are parallel, they lie in one plane [D1.23], and BG, which joins the point B on BA to the point G on GH, lies in that same plane [11.7]. Thus BG is a straight line falling on the parallel straight lines BA, GH, so the interior angles on the same side, ABG and BGH (A and H being taken on the same side of BG), are together equal to two right angles [1.29]. But the angle BGH is right (Step 4); subtracting it from both, the remaining angle ABG is right [CN3]. Therefore GB is at right angles to BA. In the same way, from the parallels BC, GK and the right angle BGK, the angle CBG is right, so that GB is at right angles to BC.

**Step 7.** GB has thus been set up at right angles to the two straight lines BA, BC, which cut one another at B, at their common point of section B; therefore GB is at right angles to the plane through BA, BC, that is, to plane P [11.4].

**Step 8.** The same straight line BG is at right angles to both plane P (Step 7) and plane Q (Step 2). Planes to which the same straight line is at right angles are parallel [11.14]. Therefore plane P is parallel to plane Q.

Therefore, if two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel. Q.E.D.

*Path note.* The route chosen drops a perpendicular BG from B to plane Q and shows it is also perpendicular to plane P, so that 11.14 applies directly; this is the most direct route. Step 1 is included because 11.11 requires an elevated point, and Step 5 supplies the "not in the same plane" condition required by 11.9.

**USED:** D1.23, 1.31, 1.30, 11.9, 11.11, D11.3, 11.3, 11.7, 1.29, CN3, 11.4, 11.14

**USED:** 1.29, 1.30, 1.31, 11.11, 11.14, 11.3, 11.4, 11.7, 11.9, CN3, D1.23, D11.3
**Human refs (from References field):** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Jaccard:** 0.583 — AI adds ['1.30', '11.3', '11.7', 'CN3', 'D1.23']

## Proposition 11.16
**Statement:** If two parallel planes be cut by any plane, their common sections are parallel.

**Step 1.** Let the two parallel planes AB, CD be cut by the plane EFGH, and let EF be the common section of the planes EFGH and AB, and GH the common section of the planes EFGH and CD. Since two planes which cut one another have a straight line as their common section [11.3], each of EF, GH is a straight line. I say that EF is parallel to GH.

**Step 2.** Since EF is the common section of the planes AB and EFGH, EF lies in the plane EFGH; and since GH is the common section of the planes CD and EFGH, GH also lies in the plane EFGH. Therefore EF and GH are straight lines lying in one plane, namely EFGH.

**Step 3.** Since the planes AB, CD are parallel, they do not meet [D11.8]. But EF lies in the plane AB and GH in the plane CD; therefore EF and GH have no point in common, so they are distinct straight lines.

**Step 4.** Suppose that EF is not parallel to GH. Since EF, GH are straight lines in one plane (Step 2), then by the definition of parallel straight lines [D1.23] they must, when produced indefinitely, meet one another in one direction or the other, that is, either in the direction of F, H or in the direction of E, G. Let them be produced [P2] and let them meet at a point K.

**Step 5.** The straight line EF lies in the plane AB, and when produced to K it forms the straight line EFK, of which the part EF is in the plane AB. But a part of a straight line cannot be in the plane of reference and a part in a plane more elevated [11.1]; therefore the whole straight line EFK is in the plane AB, and so every point of it, in particular K, is in the plane AB.

**Step 6.** In the same way, the straight line GH lies in the plane CD, and when produced to K it forms the straight line GHK, of which the part GH is in the plane CD; therefore, by [11.1], the whole straight line GHK is in the plane CD, and so the point K is in the plane CD.

**Step 7.** Therefore the point K is in both of the planes AB and CD, so that the planes AB, CD meet one another at K. But they do not meet, since by hypothesis they are parallel [D11.8]. This is impossible. Therefore EF, GH do not meet when produced in the direction of F, H; and by the same argument they do not meet when produced in the direction of E, G either.

**Step 8.** Thus EF and GH are straight lines which are in the same plane EFGH (Step 2) and which, being produced indefinitely in both directions, do not meet one another in either direction. Therefore, by the definition of parallel straight lines [D1.23], EF is parallel to GH. Therefore, if two parallel planes be cut by any plane, their common sections are parallel. Q.E.D.

**USED:** 11.1, 11.3, D1.23, D11.8, P2
**Human refs (from References field):** 11.1, D1.23
**Jaccard:** 0.400 — AI adds ['11.3', 'D11.8', 'P2']

## Proposition 11.17
**Statement:** If two straight lines be cut by parallel planes, they will be cut in the same ratios.

**Step 1.** Let the two straight lines AB, CD be cut by the parallel planes GH, KL, MN at the points A, E, B and C, F, D respectively, so that A and C lie in the plane GH, E and F in the plane KL, and B and D in the plane MN. I say that, as AE is to EB, so is CF to FD.

**Step 2.** Join AC, BD, AD [P1]. Since A is in the plane GH and D is in the plane MN, while the plane KL lies between these two planes, the straight line AD passes across the plane KL; let it meet the plane KL at the point O, and join EO, OF [P1].

**Step 3.** The straight lines AB, AD meet one another at A; therefore they are in one plane, and the whole triangle ABD is in one plane [11.2]. The points E, B lie on AB and the points O, D lie on AD; hence the straight lines EO, BD lie in the plane of the triangle ABD.

**Step 4.** The plane ABD cuts each of the parallel planes KL, MN. Its common section with the plane KL is a straight line [11.3]; this straight line contains the point E (which is in KL, since KL cuts AB at E) and the point O (which is in KL by construction), so it is the straight line EO. Likewise its common section with the plane MN is a straight line [11.3] containing the points B and D, namely the straight line BD.

**Step 5.** Since the two parallel planes KL, MN are cut by the plane ABD, their common sections EO, BD are parallel [11.16].

**Step 6.** Again, the straight lines AC, AD meet one another at A; therefore they are in one plane, and the whole triangle ACD, including its side CD, is in one plane [11.2]. The point F lies on CD and the point O on AD; hence the straight lines AC, OF lie in the plane of the triangle ACD.

**Step 7.** The plane ACD cuts each of the parallel planes GH, KL. Its common section with the plane GH is a straight line [11.3] containing the points A and C (both of which are in GH), so it is the straight line AC; its common section with the plane KL is a straight line [11.3] containing the points O and F (both of which are in KL), so it is the straight line OF.

**Step 8.** Since the two parallel planes GH, KL are cut by the plane ACD, their common sections AC, OF are parallel [11.16].

**Step 9.** In the triangle ABD the straight line EO has been drawn parallel to the side BD (Step 5); therefore it cuts the sides AB, AD proportionally, so that, as AE is to EB, so is AO to OD [6.2].

**Step 10.** In the triangle ACD the straight line OF has been drawn parallel to the side AC (Step 8); therefore it cuts the sides DA, DC proportionally, so that, as AO is to OD, so is CF to FD [6.2].

**Step 11.** The ratio of AE to EB and the ratio of CF to FD are each the same as the ratio of AO to OD (Steps 9 and 10); therefore, as AE is to EB, so is CF to FD [5.11]. Therefore, if two straight lines be cut by parallel planes, they are cut in the same ratios. Q.E.D.

**USED:** 11.16, 11.2, 11.3, 5.11, 6.2, P1
**Human refs (from References field):** 11.16, 5.11, 6.2
**Jaccard:** 0.500 — AI adds ['11.2', '11.3', 'P1']

## Proposition 11.18
**Statement:** If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

**Step 1.** Let the straight line AB be at right angles to the plane of reference, meeting it at the point B, and let DE be any plane drawn through AB. We must show that the plane DE is at right angles to the plane of reference.

**Step 2.** The plane DE contains the point B of the plane of reference, and it also contains the line AB, which does not lie in the plane of reference (AB stands at right angles to it); hence the planes DE and the plane of reference cut one another. Therefore their common section is a straight line [11.3]; let it be CE. Since B lies in both planes, B lies on CE.

**Step 3.** Take any point F on CE other than B, and from F draw, in the plane DE, the straight line FG at right angles to CE [1.11]; thus the angle GFB is right.

**Step 4.** Since AB is at right angles to the plane of reference, it makes right angles with all the straight lines which meet it and lie in that plane [D11.3]. Now CE lies in the plane of reference and meets AB at B; therefore the angle ABF is right.

**Step 5.** The straight lines AB and FG both lie in the one plane DE (AB by hypothesis, FG by construction), and the straight line BF falling on them makes the interior angles ABF, BFG on the same side equal to two right angles (each being right). Therefore AB is parallel to FG [1.28].

**Step 6.** But AB is at right angles to the plane of reference; and if two straight lines are parallel and one of them is at right angles to a plane, the other is also at right angles to the same plane [11.8]. Therefore FG is at right angles to the plane of reference.

**Step 7.** Now a plane is at right angles to a plane when the straight lines drawn, in one of the planes, at right angles to the common section of the planes are at right angles to the remaining plane [D11.4]. FG was any straight line drawn in the plane DE at right angles to the common section CE, and it has been shown to be at right angles to the plane of reference. Therefore the plane DE is at right angles to the plane of reference.

**Step 8.** The plane DE was any plane whatever drawn through AB. Therefore all the planes through AB are at right angles to the plane of reference. Q.E.D.

**USED:** 1.11, 1.28, 11.3, 11.8, D11.3, D11.4
**Human refs (from References field):** 1.11, 1.28, 11.8, D11.3, D11.4
**Jaccard:** 0.833 — AI adds ['11.3']

## Proposition 11.19
**Statement:** If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

## Proposition 11.19
**Statement:** If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

**Step 1.** Let the two planes AB and BC cut one another, let BD be their common section, and let each of the planes AB, BC be at right angles to the plane of reference. Let the straight line BD meet the plane of reference at the point D. Since the plane AB cuts the plane of reference, their common section is a straight line [11.3]; call it AD. Likewise the common section of the plane BC and the plane of reference is a straight line [11.3]; call it CD. The point D is in the plane AB and in the plane of reference, so it lies on AD; and D is in the plane BC and in the plane of reference, so it lies on CD.

**Step 2.** In the plane AB, at the point D on the straight line AD, draw DE at right angles to AD [1.11], taking E on the side of the plane of reference towards which the planes AB, BC are elevated. In the plane BC, at the point D on the straight line CD, draw DF at right angles to CD [1.11], taking F on that same side.

**Step 3.** Since the plane AB is at right angles to the plane of reference, and DE has been drawn in the plane AB at right angles to AD, the common section of these two planes, DE is at right angles to the plane of reference [D11.4].

**Step 4.** Similarly, since the plane BC is at right angles to the plane of reference, and DF has been drawn in the plane BC at right angles to CD, the common section of these two planes, DF is at right angles to the plane of reference [D11.4].

**Step 5.** Thus DE and DF are both set up from the same point D at right angles to the plane of reference, and on the same side of it. But from the same point two distinct straight lines cannot be set up at right angles to the same plane on the same side [11.13]. Therefore DE and DF are not distinct: they are one and the same straight line.

**Step 6.** This single straight line lies in the plane AB, because DE was drawn in the plane AB, and it lies in the plane BC, because DF was drawn in the plane BC. Hence every point of it is common to the two planes AB and BC. The points common to the planes AB and BC make up their common section, which is the straight line BD [11.3]. Therefore the straight line DE lies along the common section BD; and since DE and DB both pass through the point D, the straight line DB is the same straight line as DE.

**Step 7.** But DE is at right angles to the plane of reference (Step 3). Therefore BD, the common section of the planes AB and BC, is at right angles to the plane of reference.

Therefore, if two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane. Q.E.D.

*Path note:* the proof rests on the uniqueness of the perpendicular from a point to a plane (11.13); once the two perpendiculars DE, DF are forced to coincide, the fact that they lie in both planes identifies them with the common section BD via 11.3. No other route is needed.

**USED:** 11.3, 1.11, D11.4, 11.13

**USED:** 1.11, 11.13, 11.3, D11.4
**Human refs (from References field):** 11.13, D11.4
**Jaccard:** 0.500 — AI adds ['1.11', '11.3']

## Proposition 11.20
**Statement:** If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

## Proposition 11.20
**Statement:** If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

**Step 1.** Let the solid angle at A be contained by the three plane angles BAC, CAD, DAB. By D11.11 these three plane angles are not in the same plane; in particular the straight line AD does not lie in the plane through BA, AC, so the point D is not in that plane. Since the three required inequalities differ only by a renaming of the letters B, C, D, it suffices to prove that the angles DAB, DAC taken together are greater than the angle BAC.

**Step 2.** First suppose that the angle BAC is not greater than one of the angles DAB, DAC; say BAC is not greater than DAB. The angle DAB together with the angle DAC is a whole of which DAB is a part, so the two together are greater than DAB (CN5); and DAB is not less than BAC. Hence DAB together with DAC is greater than BAC. The same argument applies if BAC is not greater than DAC.

**Step 3.** Suppose now that BAC is greater than each of DAB and DAC. In the plane through BA, AC, on the straight line AB and at the point A on it, construct the angle BAE equal to the angle DAB (1.23), taking E on the same side of AB as C. Since the angle BAE equals DAB and DAB is less than BAC, the straight line AE falls within the angle BAC.

**Step 4.** Cut off AE equal to AD (1.3). Take a point B on AB, join BE (P1), and produce BE beyond E (P2); since AE lies within the angle BAC, the line BE produced meets AC at a point C. Thus E lies between B and C on the straight line BC, so that BC is equal to BE together with EC.

**Step 5.** Join DB and DC (P1).

**Step 6.** In the triangles DAB, EAB, the side DA is equal to the side AE, the side AB is common, and the angle DAB is equal to the angle BAE by construction. Therefore the base DB is equal to the base BE (1.4).

**Step 7.** Since D is not in the plane through BA, AC (Step 1), D is not on the straight line BC, so DBC is a triangle. Therefore the two sides DB, DC are together greater than the third side BC (1.20).

**Step 8.** Now BC is equal to BE together with EC, and BE is equal to DB (Step 6); so BC is equal to DB together with EC. Hence DB together with DC is greater than DB together with EC. Taking away the common DB from each, the remainder DC is greater than the remainder EC (CN3).

**Step 9.** In the triangles DAC, EAC, the side DA is equal to the side AE, the side AC is common, and the base DC is greater than the base EC. Therefore the angle DAC is greater than the angle EAC (1.25).

**Step 10.** Since the angle DAC is greater than the angle EAC, DAC is equal to EAC together with some further angle. Adding the equal angles DAB and BAE respectively (CN2), the angles DAB, DAC together are equal to the angles BAE, EAC together with that further angle, and so are greater than the angles BAE, EAC together (CN5).

**Step 11.** Since AE lies within the angle BAC, the angles BAE, EAC together make up the whole angle BAC. Therefore the angles DAB, DAC together are greater than the angle BAC.

**Step 12.** Combining Steps 2 and 11, in every case the angles DAB, DAC together are greater than the angle BAC; and by renaming the letters the same argument shows that BAC, DAB together are greater than DAC, and that BAC, DAC together are greater than DAB. Therefore, if a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

**USED:** D11.11, CN5, 1.23, 1.3, P1, P2, 1.4, 1.20, CN3, 1.25, CN2

**USED:** 1.20, 1.23, 1.25, 1.3, 1.4, CN2, CN3, CN5, D11.11, P1, P2
**Human refs (from References field):** 1.20, 1.25, 1.4
**Jaccard:** 0.273 — AI adds ['1.23', '1.3', 'CN2', 'CN3', 'CN5', 'D11.11', 'P1', 'P2']

## Proposition 11.21
**Statement:** Any solid angle is contained by plane angles less than four right angles.

## Proposition 11.21
**Statement:** Any solid angle is contained by plane angles less than four right angles.

**Step 1.** First let the solid angle at A be contained by three plane angles BAC, CAD, DAB. By D11.11 these plane angles are constructed to the one point A and are not in one plane. I say that the angles BAC, CAD, DAB are together less than four right angles.

**Step 2.** Take points B, C, D at random on the straight lines AB, AC, AD respectively, and join BC, CD, DB [P1].

**Step 3.** The points A, B, C, D are not in one plane; for a plane containing all four would contain the straight lines AB, AC, AD which join them, so that the angles BAC, CAD, DAB would lie in one plane and would not contain a solid angle [D11.11]. Consequently the straight lines BA, BC, BD are not in one plane, and the three plane angles CBA, ABD, CBD, constructed to the point B, contain a solid angle at B [D11.11]. In the same way the three plane angles BCA, ACD, BCD contain a solid angle at C, and the three plane angles CDA, ADB, CDB contain a solid angle at D.

**Step 4.** Since the solid angle at B is contained by the three plane angles CBA, ABD, CBD, any two of them taken together are greater than the remaining one [11.20]; therefore the angles CBA, ABD are together greater than the angle CBD.

**Step 5.** For the same reason [11.20], the angles BCA, ACD at the solid angle at C are together greater than the angle BCD, and the angles CDA, ADB at the solid angle at D are together greater than the angle CDB.

**Step 6.** Adding the three inequalities of Steps 4 and 5, the six angles CBA, ABD, BCA, ACD, CDA, ADB are together greater than the three angles CBD, BCD, CDB.

**Step 7.** But the angles CBD, BCD, CDB are the three angles of the triangle BCD, and are therefore together equal to two right angles [1.32]. Hence the six angles CBA, ABD, BCA, ACD, CDA, ADB are together greater than two right angles.

**Step 8.** Again, the three angles of each of the triangles ABC, ACD, ADB are together equal to two right angles [1.32]. Adding these three equalities [CN2], the nine angles of the three triangles, namely CBA, ACB, BAC, ACD, CDA, CAD, ADB, DBA, BAD, are together equal to six right angles.

**Step 9.** Of these nine angles, the six angles CBA, ACB, ACD, CDA, ADB, DBA are together greater than two right angles [Step 7]. Since the whole nine make six right angles and six of them exceed two right angles, the remaining three angles BAC, CAD, DAB, which contain the solid angle at A, are together less than four right angles. This proves the proposition for a solid angle contained by three plane angles.

**Step 10.** Next let the solid angle at A be contained by more than three plane angles, say by the n plane angles BAC, CAD, DAE, ..., JAK, KAB (n > 3) taken in order about A, with edges AB, AC, AD, ..., AJ, AK. Let a plane cut these edges, and let B, C, D, ..., J, K be the points of section; join BC, CD, ..., JK, KB [P1], so that BCD...K is a plane polygon of n sides. The point A is not in the plane of this polygon, for otherwise the edges AB, AC, ..., AK, and with them all the plane angles at A, would lie in one plane [D11.11].

**Step 11.** Hence at each vertex of the polygon the three straight lines drawn to A and to the two neighbouring vertices are not in one plane, and each vertex is the vertex of a solid angle contained by three plane angles [D11.11]: at B the angles ABK, ABC, KBC; at C the angles BCA, ACD, BCD; and so on, up to K with the angles JKA, AKB, JKB. Applying 11.20 at each vertex: the angles ABK, ABC are together greater than the angle KBC; the angles BCA, ACD are together greater than the angle BCD; ...; the angles JKA, AKB are together greater than the angle JKB.

**Step 12.** The angles on the left of these n inequalities are exactly the 2n angles which the n triangles ABC, ACD, ..., AJK, AKB have at the vertices B, C, ..., K of the polygon; the angles on the right are the n angles of the polygon. Adding the n inequalities, the 2n angles of the triangles at B, C, ..., K are together greater than the n angles of the polygon BCD...K.

**Step 13.** Join BD, BE, ..., BJ [P1], dividing the polygon BCD...K into the n − 2 triangles BCD, BDE, ..., BJK. The n angles of the polygon are made up of the angles of these n − 2 triangles, and each triangle has its three angles equal to two right angles [1.32]; therefore [CN2] the n angles of the polygon are together equal to 2(n − 2) right angles, that is, to 2n right angles diminished by four right angles.

**Step 14.** The n triangles ABC, ACD, ..., AJK, AKB have their angles together equal to 2n right angles [1.32, CN2]. These 3n angles consist of the n angles BAC, CAD, ..., KAB at A together with the 2n angles at B, C, ..., K; and by Steps 12 and 13 the latter are together greater than 2n right angles diminished by four right angles. Therefore the n angles BAC, CAD, ..., KAB, which contain the solid angle at A, are together less than four right angles.

**Step 15.** Therefore any solid angle is contained by plane angles less than four right angles. Q.E.D.

*Path note.* The argument requires the section of the solid angle to be a plane figure: for three plane angles the triangle BCD is necessarily plane, so nothing further is assumed; for more than three plane angles the proof takes a plane section BCD...K, which the proposition tacitly presupposes (the section polygon being convex, as used in Step 13). The angle sum of the polygon is obtained directly from 1.32 by diagonals from one vertex, the most direct route with the tools already in use.

**USED:** P1, CN2, D11.11, 1.32, 11.20

**USED:** 1.32, 11.20, CN2, D11.11, P1
**Human refs (from References field):** 1.32, 11.20
**Jaccard:** 0.400 — AI adds ['CN2', 'D11.11', 'P1']

## Proposition 11.22
**Statement:** If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

**Step 1.** Let the three given plane angles be ABC, DEF, GHK, contained by the equal straight lines AB, BC, DE, EF, GH, HK, so that AB = BC = DE = EF = GH = HK; and let any two of the angles ABC, DEF, GHK taken together in any manner be greater than the remaining one. Join AC, DF, GK (P1). It is required to construct a triangle out of straight lines equal to AC, DF, GK.

**Step 2.** By 1.22, a triangle can be constructed out of three given straight lines provided any two of them taken together in any manner are greater than the remaining one. It therefore suffices to prove that any two of AC, DF, GK taken together are greater than the third.

**Step 3.** Case 1: the angles ABC, DEF, GHK are equal to one another. In the triangles ABC, DEF the two sides AB, BC are equal to the two sides DE, EF respectively, and the angle ABC is equal to the angle DEF; therefore the base AC is equal to the base DF (1.4). In the same way AC is equal to GK. Hence AC, DF, GK are all equal to one another (CN1). Then DF and GK together are greater than DF alone, since the whole is greater than the part (CN5), and DF is equal to AC; therefore DF and GK together are greater than AC. In the same way AC and DF together are greater than GK, and AC and GK together are greater than DF.

**Step 4.** Case 2: the angles ABC, DEF, GHK are not all equal. Let ABC be an angle which is not less than either of the other two; and since the three are not all equal, one of the remaining two is less than ABC, and let that one be GHK. Thus the angle ABC is not less than the angle DEF, and the angle ABC is greater than the angle GHK.

**Step 5.** On the straight line AB and at the point B on it, and on the same side of AB as C, construct the angle ABL equal to the angle GHK (1.23). Since the angle ABL is equal to the angle GHK, which is less than the angle ABC, the straight line BL falls within the angle ABC, so that the whole angle ABC is made up of the angles ABL, LBC. Cut off BL equal to AB (1.3), and join AL, LC (P1).

**Step 6.** Since AB is equal to GH, and BL is equal to AB, which is equal to HK, BL is equal to HK (CN1); and the angle ABL is equal to the angle GHK. Therefore in the triangles ABL, GHK the two sides AB, BL are equal to the two sides GH, HK respectively, and the included angles are equal; hence the base AL is equal to the base GK (1.4).

**Step 7.** By hypothesis the angles DEF, GHK together are greater than the angle ABC. But the angle GHK is equal to the angle ABL, and the angle ABC is made up of the angles ABL, LBC (Step 5). Therefore the angles DEF, ABL together are greater than the angles ABL, LBC together; and taking away the common angle ABL, the remaining angle DEF is greater than the remaining angle LBC (CN3).

**Step 8.** In the triangles DEF, LBC, the side DE is equal to the side LB, since each is equal to AB (CN1), and the side EF is equal to the side BC; but the angle DEF contained by DE, EF is greater than the angle LBC contained by LB, BC. Therefore the base DF is greater than the base LC (1.24).

**Step 9.** In the triangle ALC the two sides AL, LC together are greater than the remaining side AC (1.20). But AL is equal to GK (Step 6), and DF is greater than LC (Step 8); therefore GK and DF together are greater than AL and LC together, which are greater than AC. Hence DF and GK together are greater than AC.

**Step 10.** Next, AC is not less than DF. For in the triangles ABC, DEF, AB is equal to DE and BC is equal to EF, and the angle ABC is not less than the angle DEF (Step 4): if the angles are equal, AC is equal to DF (1.4), and if the angle ABC is the greater, AC is greater than DF (1.24). Similarly, since the angle ABC is greater than the angle GHK and AB, BC are equal to GH, HK respectively, AC is greater than GK (1.24). Therefore AC and GK together are greater than AC (CN5), and AC is not less than DF; so AC and GK together are greater than DF. Likewise AC and DF together are greater than AC (CN5), and AC is greater than GK; so AC and DF together are greater than GK.

**Step 11.** Thus in both cases any two of the straight lines AC, DF, GK taken together in any manner are greater than the remaining one. Therefore by 1.22 a triangle can be constructed having its three sides equal to AC, DF, GK respectively; that is, a triangle can be constructed out of the straight lines joining the extremities of the equal straight lines. Q.E.F.

(Path note: in Case 1 an equilateral triangle on AC by 1.1 would also serve; 1.22 is used uniformly because the proposition's conclusion is exactly the conclusion of 1.22, so verifying its hypothesis is the most direct route in every case.)

**USED:** 1.20, 1.22, 1.23, 1.24, 1.3, 1.4, CN1, CN3, CN5, P1
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 0.200 — AI adds ['1.20', '1.22', '1.23', '1.3', 'CN1', 'CN3', 'CN5', 'P1']

## Proposition 11.23
**Statement:** To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

**Statement.** To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one; the three angles being (as they must be) less than four right angles.

Let the three given plane angles be ABC, DEF, GHK, any two of which are together greater than the third, and all three together less than four right angles. It is required to construct a solid angle out of three plane angles equal to ABC, DEF, GHK.

**Step 1.** Cut off AB, BC, DE, EF, GH, HK all equal to one another (1.3), and join AC, DF, GK (P1).

**Step 2.** The angles ABC, DEF, GHK are contained by equal straight lines and any two are together greater than the third; therefore, by 11.22, a triangle can be constructed out of straight lines equal to AC, DF, GK, i.e. any two of AC, DF, GK are together greater than the third. Construct the triangle LMN with LM = AC, MN = DF, NL = GK (1.22).

**Step 3.** Circumscribe the circle LMN about the triangle LMN (4.5); take its centre O (3.1) and join LO, MO, NO (P1). Then LO = MO = NO (D1.15).

**Step 4.** I say that AB is greater than LO. Two preliminary facts are established first. (i) If AB = LO, then, since AB = BC and LO = OM, the two sides AB, BC equal the two sides LO, OM, and the base AC equals the base LM; therefore angle ABC = angle LOM (1.8). Likewise angle DEF = angle MON and angle GHK = angle NOL.

**Step 5.** (ii) If AB < LO, cut off OP = AB on OL and OQ = BC on OM (1.3) and join PQ (P1). Since OP = OQ, the remainders PL, QM are equal (CN3); hence PQ is parallel to LM (6.2), so angle OPQ = angle OLM and angle OQP = angle OML (1.29) and the triangles OPQ, OLM are equiangular. Therefore OL : LM = OP : PQ (6.4), and alternately LO : OP = LM : PQ (5.16); but LO > OP, therefore LM > PQ (5.14), i.e. AC > PQ. Now the two sides AB, BC equal the two sides PO, OQ, while the base AC is greater than the base PQ; therefore angle ABC > angle POQ, that is, angle ABC > angle LOM (1.25). Likewise angle DEF > angle MON and angle GHK > angle NOL.

**Step 6.** Case 1: O lies within the triangle LMN. Produce LO through O to T (P2). Then angles LOM, MOT together equal two right angles, and angles LON, NOT together equal two right angles (1.13); adding (CN2), and observing that angles MOT, TON make up angle MON since OT falls within it, the three angles LOM, MON, NOL together equal four right angles. If AB = LO, then by Step 4 the angles ABC, DEF, GHK together equal LOM, MON, NOL, i.e. four right angles; if AB < LO, then by Step 5 they together exceed four right angles. Either conclusion contradicts the hypothesis; therefore AB > LO.

**Step 7.** Case 2: O lies on a side of the triangle, say on LM. Then LM is the sum of LO and OM. If AB were not greater than LO, then, since BC = AB and OM = LO, the sum of AB, BC would not exceed the sum of LO, OM, which is LM = AC; but in the triangle ABC the two sides AB, BC are together greater than AC (1.20). This is impossible; therefore AB > LO.

**Step 8.** Case 3: O lies outside the triangle, say O and N on opposite sides of LM. Then N lies on the arc cut off by LM on the side remote from the centre, so the segment LNM is less than a semicircle and the angle LNM is obtuse (3.31). Moreover ON falls within angle LOM, so that angle LOM is the sum of angles LON, NOM; and ON falls within angle LNM, so that angle LNM is the sum of angles ONL, ONM.

**Step 9.** In Case 3, AB is not equal to LO: for otherwise, by Step 4, angle ABC = angle LOM = angle LON + angle NOM = angle GHK + angle DEF, contrary to the hypothesis that DEF, GHK are together greater than ABC.

**Step 10.** In Case 3, suppose, if possible, AB < LO. By Step 5, angle ABC > angle LOM. Since angle LNM is obtuse, each of the angles NLM, NML is less than it (1.17), so LM > MN and LM > NL (1.19); that is, AC > DF and AC > GK. Hence, the two sides AB, BC being equal to DE, EF and to GH, HK, angle ABC > angle DEF and angle ABC > angle GHK (1.25).

**Step 11.** At the point B on BC construct angle CBX equal to angle DEF (1.23), BX falling within angle ABC (possible since DEF < ABC); make BX = AB (1.3) and join CX, XA (P1). Then angle XBA is the excess of ABC over DEF, which is less than GHK by hypothesis. In the triangles CBX, DEF the two sides CB, BX equal the two sides DE, EF and the included angles are equal, so CX = DF = MN (1.4). In the triangles XBA, GHK the two sides XB, BA equal the two sides GH, HK and angle XBA < angle GHK, so XA < GK = NL (1.24).

**Step 12.** In the isosceles triangle BCX, angle BXC = angle BCX (1.5), and the three angles equal two right angles (1.32); hence twice angle BXC together with angle CBX equals two right angles. Likewise twice angle BXA together with angle XBA equals two right angles. Adding (CN2), and noting that XB falls within angle CXA (B and X lying on opposite sides of CA), twice angle CXA together with angle ABC equals four right angles. In the same way, from the isosceles triangles ONM, ONL (1.5, 1.32) and Step 8, twice angle MNL together with angle LOM equals four right angles. Since angle LOM < angle ABC, twice angle MNL exceeds twice angle CXA, so angle MNL > angle CXA.

**Step 13.** Since XA < NL, cut off NN' = XA on NL (1.3) and join MN' (P1). In the triangles MNN', CXA the two sides MN, NN' equal the two sides CX, XA, and the included angle MNN' (which is angle MNL) is greater than angle CXA; therefore MN' > CA (1.24). Again, angle MN'L is an exterior angle of triangle MNN', so it is greater than angle MNN' (1.16), which is obtuse; hence angle MN'L is obtuse and exceeds each of the angles N'LM, N'ML (1.17), so ML > MN' (1.19). Therefore ML > MN' > CA; but ML = AC. This is impossible; therefore AB is not less than LO.

**Step 14.** By Steps 6, 7, 9 and 13, in every case AB > LO.

**Step 15.** Next, a straight line is found whose square equals the excess of the square on AB over the square on LO. Take UV = AB (1.3), bisect it at W (1.10), and with centre W and distance WU describe a circle (P3), of which UV is a diameter. Since LO < AB = UV, fit UY = LO into the circle (4.1) and join YV (P1). The angle UYV, being in a semicircle, is right (3.31); therefore the square on UV equals the squares on UY, YV (1.47), so that the square on YV is the excess of the square on AB over the square on LO.

**Step 16.** From O set up OR at right angles to the plane of the circle LMN (11.12), and make OR = YV (1.3); join RL, RM, RN (P1). Since RO is at right angles to the plane, the angles ROL, ROM, RON are right (D11.3). Hence the square on RL equals the squares on RO, OL (1.47), that is, the squares on YV, LO (CN2), which together equal the square on UV, i.e. on AB (Step 15, CN1); therefore RL = AB. In the same way, since OM = ON = OL, RM = AB and RN = AB.

**Step 17.** Now AB = BC = DE = EF = GH = HK, so each of RL, RM, RN equals each of these. In the triangles LRM, ABC the two sides LR, RM equal the two sides AB, BC, and the base LM equals the base AC; therefore angle LRM = angle ABC (1.8). Likewise angle MRN = angle DEF and angle NRL = angle GHK.

**Step 18.** The point R is not in the plane LMN, since RO is at right angles to that plane; hence the three plane angles LRM, MRN, NRL are not in one plane and are constructed to the one point R, so they contain a solid angle at R (D11.11). Therefore out of three plane angles LRM, MRN, NRL, equal respectively to the given angles ABC, DEF, GHK, a solid angle has been constructed at R. Q.E.F.

**USED:** 1.10, 1.13, 1.16, 1.17, 1.19, 1.20, 1.22, 1.23, 1.24, 1.25, 1.29, 1.3, 1.32, 1.4, 1.47, 1.5, 1.8, 11.12, 11.22, 3.1, 3.31, 4.1, 4.5, 5.14, 5.16, 6.2, 6.4, CN1, CN2, CN3, D1.15, D11.11, D11.3, P1, P2, P3
**Human refs (from References field):** 1.25, 1.29, 1.4, 1.47, 1.8, 11.12, 11.22, 5.16, 6.2, 6.4
**Jaccard:** 0.278 — AI adds ['1.10', '1.13', '1.16', '1.17', '1.19', '1.20', '1.22', '1.23', '1.24', '1.3', '1.32', '1.5', '3.1', '3.31', '4.1', '4.5', '5.14', 'CN1', 'CN2', 'CN3', 'D1.15', 'D11.11', 'D11.3', 'P1', 'P2', 'P3']

## Proposition 11.24
**Statement:** If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

**Step 1.** Let the solid be contained by six planes, of which the opposite ones are parallel: let the plane ABCD be parallel to the plane EFGH, the plane ABFE parallel to the plane DCGH, and the plane ADHE parallel to the plane BCGF. Each edge of the solid is the common section of the two faces meeting along it: AB is the common section of the planes ABCD and ABFE, BC of ABCD and BCGF, CD of ABCD and DCGH, DA of ABCD and ADHE; EF, FG, GH, HE are the common sections of the plane EFGH with the planes ABFE, BCGF, DCGH, ADHE respectively; and AE, BF, CG, DH are the common sections of the pairs of planes ABFE and ADHE, ABFE and BCGF, DCGH and BCGF, DCGH and ADHE respectively. I say that the opposite faces are parallelograms and are equal to one another.

**Step 2.** The parallel planes ABFE, DCGH are cut by the plane ABCD, and their common sections with it are AB, DC. Therefore AB is parallel to DC [11.16].

**Step 3.** Again, the parallel planes ADHE, BCGF are cut by the plane ABCD, and their common sections with it are AD, BC. Therefore AD is parallel to BC [11.16].

**Step 4.** Hence the quadrilateral ABCD, which lies in one plane, has AB parallel to DC and AD parallel to BC; that is, ABCD is a parallelogram.

**Step 5.** In the same manner every other face is a parallelogram. The plane ABFE cuts the parallel planes ABCD, EFGH in AB, EF and cuts the parallel planes ADHE, BCGF in AE, BF; therefore AB is parallel to EF and AE to BF [11.16], and ABFE is a parallelogram. The plane BCGF cuts the parallel planes ABCD, EFGH in BC, FG and the parallel planes ABFE, DCGH in BF, CG; therefore BC is parallel to FG and BF to CG [11.16], and BCGF is a parallelogram. The plane DCGH cuts the parallel planes ABCD, EFGH in DC, HG and the parallel planes ADHE, BCGF in DH, CG; therefore DC is parallel to HG and DH to CG [11.16], and DCGH is a parallelogram. Likewise the plane EFGH, cut by the parallel planes ABFE, DCGH in EF, HG and by the parallel planes ADHE, BCGF in EH, FG, is a parallelogram; and the plane ADHE, cut by the parallel planes ABCD, EFGH in AD, EH and by the parallel planes ABFE, DCGH in AE, DH, is a parallelogram. Thus all six faces are parallelogrammic.

**Step 6.** It remains to show that opposite faces are equal. Consider first the opposite faces ABFE and DCGH. Join AF and DG [P1].

**Step 7.** AB is parallel to DC (Step 2) and BF is parallel to CG (Step 5). The straight lines AB, BF meet one another at B and lie in the plane ABFE; the straight lines DC, CG meet one another at C and lie in the plane DCGH. Since the planes ABFE, DCGH are parallel, they do not meet [D11.8]; so the pair AB, BF and the pair DC, CG are not in the same plane. Therefore the two straight lines AB, BF meeting one another are parallel to the two straight lines DC, CG meeting one another, not in the same plane; hence they contain equal angles, and the angle ABF is equal to the angle DCG [11.10].

**Step 8.** Since ABCD is a parallelogram, its opposite sides are equal, so AB is equal to DC [1.34]. Since BCGF is a parallelogram, BF is equal to CG [1.34].

**Step 9.** In the triangles ABF, DCG the two sides AB, BF are equal to the two sides DC, CG respectively, and the angle ABF contained by them is equal to the angle DCG (Step 7). Therefore the base AF is equal to the base DG, and the triangle ABF is equal to the triangle DCG [1.4].

**Step 10.** ABFE is a parallelogram and AF is a diameter of it; the diameter bisects the parallelogram, so the triangle ABF is equal to the triangle AFE [1.34]. Likewise DG is a diameter of the parallelogram DCGH, so the triangle DCG is equal to the triangle DGH [1.34].

**Step 11.** The triangle AFE is equal to the triangle ABF, which is equal to the triangle DCG, which is equal to the triangle DGH; therefore the triangle AFE is equal to the triangle DGH [CN1]. Adding equals to equals, the triangles ABF, AFE together are equal to the triangles DCG, DGH together [CN2]; that is, the parallelogram ABFE is equal to the parallelogram DCGH.

**Step 12.** Similarly the parallelogram ABCD is equal to the parallelogram EFGH. Join AC and EG [P1]. AB, BC are parallel to EF, FG respectively (Step 5); AB, BC lie in the plane ABCD and EF, FG in the plane EFGH, and these planes, being parallel, do not meet [D11.8], so the two pairs are not in the same plane; hence the angle ABC is equal to the angle EFG [11.10]. AB is equal to EF and BC to FG, being opposite sides of the parallelograms ABFE, BCGF [1.34]; hence the triangle ABC is equal to the triangle EFG [1.4]. Since the diameters AC, EG bisect the parallelograms ABCD, EFGH [1.34], the triangle ACD is equal to the triangle EGH [CN1], and adding equals to equals the parallelogram ABCD is equal to the parallelogram EFGH [CN2]. In the same way the parallelogram ADHE is equal to the parallelogram BCGF: join AH and BG [P1]; AD, DH are parallel to BC, CG respectively (Steps 3 and 5) and lie in the parallel planes ADHE, BCGF, which do not meet [D11.8], so the angle ADH is equal to the angle BCG [11.10]; AD is equal to BC and DH to CG, being opposite sides of the parallelograms ABCD, DCGH [1.34]; hence the triangle ADH is equal to the triangle BCG [1.4]; and since the diameters AH, BG bisect the parallelograms ADHE, BCGF [1.34], the triangle AHE is equal to the triangle BGF [CN1], and the parallelogram ADHE is equal to the parallelogram BCGF [CN2].

**Step 13.** Therefore, if a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic. Q.E.D.

**USED:** 1.34, 1.4, 11.10, 11.16, CN1, CN2, D11.8, P1
**Human refs (from References field):** 1.34, 1.4, 11.10, 11.16
**Jaccard:** 0.500 — AI adds ['CN1', 'CN2', 'D11.8', 'P1']

## Proposition 11.25
**Statement:** If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.

## Proposition 11.25
**Statement:** If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.

**Step 1.** Let AD be a parallelepipedal solid, that is, a solid contained by three pairs of parallel planes; its faces are the parallelograms AC (the base), BD, AI, VD, AU, HD, of which the opposite ones are equal (11.24). Let it be cut by a plane parallel to the opposite planes AU, HD, meeting the edges AH, VC, BI, UD at E, F, G, T respectively; call this plane ET. I say that, as the base AF is to the base EC, so is the solid AT to the solid ED.

**Step 2.** Since the parallel planes ET, AU are cut by the plane AC, their common sections EF, AV are parallel; and since the parallel planes ET, HD are cut by the plane AC, EF is parallel to HC (11.16). In the same way EG, FT, GT are parallel to AB, VU, BU respectively. Hence AF and EC are parallelograms, for AE, VF and EH, FC are parts of the parallel sides AH, VC of the parallelogram AC, while EF is parallel to AV and to HC. Moreover each of the solids AT, ED is contained by parallel planes, its faces lying in the planes AC, BD, AI, VD and in the two parallel planes AU, ET (for AT) or ET, HD (for ED); therefore the opposite faces of each of the solids AT, ED are equal parallelograms (11.24).

**Step 3.** Let HA be produced beyond A and AH beyond H (P2), and let any number of straight lines AK, KL be made equal to AE, and any number HM, MN equal to EH (1.3). Through K, L, M, N draw in the plane AC straight lines parallel to AV, meeting CV produced at X, Y on the side of V and at W, Z on the side of C; through K, L, M, N draw in the plane AI straight lines parallel to AB, and through X, Y, W, Z draw in the plane VD straight lines parallel to VU, meeting IB and DU produced (1.31); let KQ, MJ be the lines so drawn through K, M in the plane AI, and XO, WR those through X, W in the plane VD. The lines drawn parallel to AV are parallel to one another, and likewise those drawn parallel to AB and those drawn parallel to VU (1.30). Let the parallelepipedal solids LO, KU, HR, NR be completed, whose bases are the parallelograms LX, KV, HW, MZ, whose faces in the plane AI are the parallelograms LQ, KB, MI, NJ, and whose end faces are KO, MR together with the planes through L and N.

**Step 4.** Since KX, KQ, which meet at K, are parallel respectively to AV, AB, which meet at A, the plane KO through KX, KQ is parallel to the plane AU through AV, AB (11.15); since the lines through L are parallel to KX, KQ, the end plane through L is parallel to the plane KO (11.15); and in the same way the plane MR is parallel to the plane HD, and the end plane through N is parallel to the plane MR. Hence each of the solids LO, KU, HR, NR is contained by parallel planes, so that its opposite faces are equal parallelograms (11.24).

**Step 5.** The parallelograms LX, KV, AF are on the equal bases LK, KA, AE and in the same parallels LN, YZ; therefore they are equal to one another (1.36). Likewise the parallelograms LQ, KB, AG are on the equal bases LK, KA, AE and in the same parallels LN, QI; therefore they are equal to one another (1.36).

**Step 6.** The faces KO, AU are opposite faces of the solid KU, and the faces AU, ET are opposite faces of the solid AT; therefore KO is equal to AU, and AU to ET (11.24), so that KO, AU, ET are equal to one another (CN1).

**Step 7.** Thus in the solids LO, KU, AT the bases LX, KV, AF are equal to one another, the faces LQ, KB, AG are equal to one another, and the end faces KO, AU, ET, one in each solid, are equal to one another; and the three remaining faces of each solid are equal to these three, being opposite to them (11.24). The three solids are therefore contained by six planes equal in multitude and in magnitude, face for face; hence the solids LO, KU, AT are equal to one another (D11.10).

**Step 8.** In the same way the parallelograms EC, HW, MZ, being on the equal bases EH, HM, MN and in the same parallels LN, YZ, are equal to one another, and so are the parallelograms EI, MI, NJ (1.36); the end faces ET, HD, MR are equal to one another, since ET, HD are opposite faces of the solid ED and HD, MR are opposite faces of the solid HR (11.24, CN1); and the remaining faces of each of the solids ED, HR, NR are equal to these, being opposite (11.24). Therefore the solids ED, HR, NR are equal to one another (D11.10).

**Step 9.** Now the base LF is made up of the parallelograms LX, KV, AF, each of which is equal to AF, and the solid LT is made up of the solids LO, KU, AT, each of which is equal to AT; and the parts are equal in multitude, there being one of each for each of the straight lines LK, KA, AE. Therefore the base LF is the same multiple of the base AF that the solid LT is of the solid AT (D5.2). For the same reason the base EZ is the same multiple of the base EC that the solid NT is of the solid ED. And since the multitude of the lines AK, KL, ... and that of the lines HM, MN, ... were taken at pleasure and independently, LF, LT are any equimultiples whatever of AF, AT, and EZ, NT are any equimultiples whatever of EC, ED.

**Step 10.** The straight line LE is either equal to EN, or greater, or less. First let LE be equal to EN. Then the parallelograms LF, EZ, being on the equal bases LE, EN and in the same parallels LN, YZ, are equal (1.36); and the solids LT, NT are equal: for their bases LF, EZ are equal, their faces in the plane AI, being on the same equal bases LE, EN and in the same parallels LN, QI, are equal (1.36), the face ET is common to both, and the remaining faces of each are equal to these, being opposite to them (11.24); so that the two solids are contained by six planes equal in multitude and in magnitude, and are equal (D11.10).

**Step 11.** Next let LE be greater than EN. From EL cut off EP equal to EN (1.3), and through P draw, as in Steps 3 and 4, a plane parallel to the plane ET (1.31, 11.15), cutting off from the solid LT the solid PT which stands on the base PF. Then, exactly as in Step 10, the base PF is equal to the base EZ (1.36), and the solid PT is equal to the solid NT (D11.10). But PF is a part of LF, and PT is a part of LT; therefore LF is greater than EZ, and LT is greater than NT (CN5). Lastly, if LE is less than EN, then by cutting off from EN a straight line equal to EL we find in the same way that LF is less than EZ and LT is less than NT.

**Step 12.** Accordingly, as LE is equal to, greater than, or less than EN, so is the base LF equal to, greater than, or less than the base EZ, and so, at the same time, is the solid LT equal to, greater than, or less than the solid NT. Consequently, if the base LF is equal to the base EZ, the solid LT is equal to the solid NT; if LF exceeds EZ, LT exceeds NT; and if LF falls short of EZ, LT falls short of NT.

**Step 13.** There are thus four magnitudes, the two bases AF, EC and the two solids AT, ED; of the first and third, AF and AT, equimultiples LF, LT have been taken, and of the second and fourth, EC and ED, any other equimultiples EZ, NT; and it has been proved that the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples, taken in corresponding order. Therefore, as the base AF is to the base EC, so is the solid AT to the solid ED (D5.5).

Therefore, if a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so is the solid to the solid.

**USED:** P2, CN1, CN5, D5.2, D5.5, D11.10, 1.3, 1.30, 1.31, 1.36, 11.15, 11.16, 11.24

**USED:** 1.3, 1.30, 1.31, 1.36, 11.15, 11.16, 11.24, CN1, CN5, D11.10, D5.2, D5.5, P2
**Human refs (from References field):** 11.24, D5.5
**Jaccard:** 0.154 — AI adds ['1.3', '1.30', '1.31', '1.36', '11.15', '11.16', 'CN1', 'CN5', 'D11.10', 'D5.2', 'P2']

## Proposition 11.26
**Statement:** On a given straight line, and at a given point on it, to construct a solid angle equal to a given solid angle.

**Step 1.** Let AB be the given straight line, A the given point on it, and let the given solid angle be the angle at D contained by the three plane angles EDC, EDF, FDC, which are constructed to the one point D and are not in one plane (D11.11); here E, C, F are points taken at pleasure on the three straight lines that bound the solid angle. Since E may be taken anywhere on its straight line, let it be so taken that DE is equal to AB (1.3).

**Step 2.** The point F does not lie in the plane through ED, DC, since the plane angles containing the solid angle are not in one plane (D11.11). From the elevated point F draw FG perpendicular to the plane through ED, DC, meeting that plane at the point G (11.11), and join DG, GE, GC, FE, FC (P1).

**Step 3.** On the straight line AB and at the point A on it, in any plane through AB, construct the angle BAL equal to the angle EDC (1.23), and in the same plane, on the same side of AB as L, construct the angle BAK equal to the angle EDG (1.23). Cut off AK equal to DG and AL equal to DC (1.3).

**Step 4.** From the point K set up KH at right angles to the plane through BA, AL (11.12), cut off KH equal to GF (1.3), and join HA, HB, HL, KB, KL (P1).

**Step 5.** Since FG is at right angles to the plane through ED, DC, it makes right angles with every straight line that meets it and lies in that plane (D11.3); the points G, D, E, C are in that plane, so GD, GE, GC lie in it, and the angles FGD, FGE, FGC are right. In the same way HK is at right angles to the plane through BA, AL, and the points K, A, B, L are in that plane, so KA, KB, KL lie in it; hence the angles HKA, HKB, HKL are right (D11.3). All these right angles are equal to one another (P4).

**Step 6.** In the triangles BAK, EDG, the side AB is equal to the side DE (Step 1), the side AK to the side DG, and the angle BAK to the angle EDG (Step 3). Therefore the base BK is equal to the base EG (1.4).

**Step 7.** In the triangles HKB, FGE, the side HK is equal to the side FG (Step 4), the side KB to the side GE (Step 6), and the right angle HKB to the right angle FGE (Step 5). Therefore the base HB is equal to the base FE (1.4).

**Step 8.** In the triangles HKA, FGD, the side HK is equal to the side FG (Step 4), the side KA to the side GD (Step 3), and the right angle HKA to the right angle FGD (Step 5). Therefore the base HA is equal to the base FD (1.4).

**Step 9.** In the triangles HAB, FDE, the two sides HA, AB are equal to the two sides FD, DE respectively (Steps 8, 1), and the base HB is equal to the base FE (Step 7). Therefore the angle BAH, contained by HA, AB, is equal to the angle EDF, contained by FD, DE (1.8).

**Step 10.** The angle BAL is equal to the angle EDC and the angle BAK to the angle EDG (Step 3). Since G falls within the angle EDC (the case here treated), the angle EDG is less than the angle EDC, so the angle BAK is less than the angle BAL, and AK falls within the angle BAL, K and L being on the same side of AB. Subtracting the equal angles BAK, EDG from the equal angles BAL, EDC, the remaining angle KAL is equal to the remaining angle GDC (CN3).

**Step 11.** In the triangles KAL, GDC, the side KA is equal to the side GD, the side AL to the side DC (Step 3), and the angle KAL to the angle GDC (Step 10). Therefore the base KL is equal to the base GC (1.4).

**Step 12.** In the triangles HKL, FGC, the side HK is equal to the side FG (Step 4), the side KL to the side GC (Step 11), and the right angle HKL to the right angle FGC (Step 5). Therefore the base HL is equal to the base FC (1.4).

**Step 13.** In the triangles HAL, FDC, the two sides HA, AL are equal to the two sides FD, DC respectively (Steps 8, 3), and the base HL is equal to the base FC (Step 12). Therefore the angle HAL, contained by HA, AL, is equal to the angle FDC, contained by FD, DC (1.8).

**Step 14.** Thus the three plane angles BAL, BAH, HAL at the point A are equal respectively to the three plane angles EDC, EDF, FDC at the point D (Steps 3, 9, 13). Moreover H is not in the plane through BA, AL, since HK is set up at right angles to that plane from K (Step 4); so the three angles BAL, BAH, HAL are constructed to the one point A and are not in one plane, and therefore contain a solid angle (D11.11). This solid angle at A is contained by three plane angles equal respectively to the three plane angles containing the solid angle at D, and is therefore equal to the solid angle at D.

**Step 15.** Therefore on the given straight line AB and at the given point A on it a solid angle has been constructed equal to the given solid angle at D. Q.E.F.

**USED:** 1.23, 1.3, 1.4, 1.8, 11.11, 11.12, CN3, D11.11, D11.3, P1, P4
**Human refs (from References field):** 1.23, 1.4, 1.8, 11.11, 11.12, D11.3
**Jaccard:** 0.545 — AI adds ['1.3', 'CN3', 'D11.11', 'P1', 'P4']

## Proposition 11.27
**Statement:** On a given straight line to describe a parallelepipedal solid similar and similarly situated to a given parallelepipedal solid.

**Step 1.** Let AB be the given straight line, and let CD be the given parallelepipedal solid, C being one of its vertices and CE, CF, CG the three edges of the solid which meet at C. Thus the solid angle at C is contained by the three plane angles ECF, FCG, GCE, and the three faces of CD which meet at C are the parallelograms GE (contained by CG, CE), GF (contained by CG, CF) and FE (contained by CF, CE).

**Step 2.** On the straight line AB and at the point A on it construct a solid angle equal to the solid angle at C, contained by the three plane angles BAH, HAK, KAB, so that the angle BAH is equal to the angle ECF, the angle BAK to the angle ECG, and the angle KAH to the angle GCF [11.26].

**Step 3.** To the three straight lines EC, CG, BA find a fourth proportional [6.12], and from A along the straight line AK let AK be cut off equal to it [1.3]; then, as EC is to CG, so is BA to AK. Again, to the three straight lines GC, CF, KA find a fourth proportional [6.12], and from A along the straight line AH let AH be cut off equal to it [1.3]; then, as GC is to CF, so is KA to AH.

**Step 4.** Since, as EC is to CG, so is BA to AK, and, as CG is to CF, so is AK to AH, therefore, ex aequali, as EC is to CF, so is BA to AH [5.22].

**Step 5.** Through B draw straight lines parallel to AH and to AK, through H straight lines parallel to AB and to AK, and through K straight lines parallel to AB and to AH [1.31], so that the parallelograms HB (on AB, AH), KB (on AB, AK) and KH (on AH, AK) are completed. The two straight lines drawn through B are parallel to the two straight lines AH, AK which meet at A and are not in the same plane with them; therefore the plane through them is parallel to the plane of KH [11.15], and in the same way the plane through the two parallels drawn at H is parallel to the plane of KB, and the plane through the two parallels drawn at K is parallel to the plane of HB [11.15]. Let the solid contained by these six planes be the parallelepipedal solid AL; its three faces which meet at A are the parallelograms HB, KB, KH.

**Step 6.** Now, since, as EC is to CG, so is BA to AK, and the angle ECG is equal to the angle BAK, the sides about the equal angles ECG, BAK are proportional. In each of the parallelograms GE, KB the opposite sides and angles are equal to these [1.34], and the angles adjacent to the angles ECG, BAK are each, together with them, equal to two right angles [1.29], so that these adjacent angles are also equal to one another [CN3]. Therefore the parallelogram GE has its angles severally equal to the angles of the parallelogram KB and the sides about the equal angles proportional; hence the parallelogram GE is similar to the parallelogram KB [D6.1].

**Step 7.** For the same reason, since, as GC is to CF, so is KA to AH, and the angle GCF is equal to the angle KAH, the parallelogram GF is similar to the parallelogram KH [1.34, 1.29, CN3, D6.1]; and since, as EC is to CF, so is BA to AH, and the angle ECF is equal to the angle BAH, the parallelogram FE is similar to the parallelogram HB [1.34, 1.29, CN3, D6.1].

**Step 8.** Therefore the three parallelograms GE, GF, FE of the solid CD which meet at C are similar respectively to the three parallelograms KB, KH, HB of the solid AL which meet at A. But the three faces of CD at C are equal and similar to the three faces of CD opposite to them, and the three faces of AL at A are equal and similar to the three faces of AL opposite to them [11.24].

**Step 9.** Hence each face of CD opposite to C, being similar to the face at C, which is similar to the corresponding face of AL at A, is itself similar to that face of AL [6.21]; and, the face of AL opposite to that face being also similar to it, the face of CD opposite to C is similar to the face of AL opposite to A [6.21]. Thus the six faces of the solid CD are similar respectively to the six faces of the solid AL.

**Step 10.** Therefore the solid AL, being contained by six planes similar to the six planes containing the solid CD, is similar to the solid CD [D11.9]; and it is similarly situated with it, the edges AB, AH, AK of AL corresponding in order to the edges CE, CF, CG of CD, and the faces HB, KB, KH at A to the faces FE, GE, GF at C.

**Step 11.** Therefore on the given straight line AB the parallelepipedal solid AL has been described similar and similarly situated to the given parallelepipedal solid CD. Q.E.F.

**USED:** 1.29, 1.3, 1.31, 1.34, 11.15, 11.24, 11.26, 5.22, 6.12, 6.21, CN3, D11.9, D6.1
**Human refs (from References field):** 5.22, 6.12, D11.9
**Jaccard:** 0.231 — AI adds ['1.29', '1.3', '1.31', '1.34', '11.15', '11.24', '11.26', '6.21', 'CN3', 'D6.1']

## Proposition 11.28
**Statement:** If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid will be bisected by the plane.

**Step 1.** Let the parallelepipedal solid have the parallelogram ABCD as one face and EFGH as the opposite face, the vertices E, F, G, H standing over A, B, C, D respectively, so that the remaining faces are ABFE, BCGF, CDHG and DAEH. The six faces fall into three opposite pairs, (ABCD, EFGH), (ABFE, DCGH), (BCGF, ADHE), and, the solid being parallelepipedal, the two faces of each pair lie in parallel planes. Hence every face is a parallelogram and the opposite faces are equal, having their sides and angles severally equal [11.24].

**Step 2.** Let AF be a diagonal of the face ABFE and DG the corresponding diagonal of the opposite face DCGH, and let the solid be cut by the plane through the diagonals AF and DG. This plane contains the four points A, D, F, G. Its common section with the plane of the face ABCD is a straight line [11.3]; since that straight line passes through A and D, it is the edge AD. In the same way the cutting plane meets the plane of EFGH in the edge FG, the plane of BCGF in the edge FG, and the plane of ADHE in the edge AD. Therefore the cutting plane meets the surface of the solid only along AF, FG, GD, DA, and the section of the solid is the quadrilateral AFGD.

**Step 3.** The planes of the opposite faces ABFE and DCGH are parallel and are cut by the plane AFGD; therefore their common sections AF and DG are parallel [11.16]. Likewise the parallel planes of ABCD and EFGH are cut by the plane AFGD in AD and FG, so that AD is parallel to FG [11.16]. Therefore the section AFGD is a parallelogram.

**Step 4.** The plane AFGD thus divides the whole solid into two solids: the solid on the side of B and C, contained by the two triangles ABF, DCG and the three parallelograms ABCD, BCGF, AFGD; and the solid on the side of E and H, contained by the two triangles AFE, DGH and the three parallelograms EFGH, ADHE, AFGD. Each of the two solids is contained by five plane figures.

**Step 5.** Since AF is a diagonal of the parallelogram ABFE, it bisects that parallelogram, so that the triangle ABF is equal to the triangle AFE, the two triangles having their sides and angles severally equal, and hence being similar as well as equal [1.34]. In the same way DG bisects the parallelogram DCGH, so that the triangle DCG is equal and similar to the triangle DGH [1.34].

**Step 6.** The parallelogram ABCD is equal to the opposite parallelogram EFGH, and the parallelogram BCGF is equal to the opposite parallelogram ADHE, since the opposite faces of a parallelepipedal solid are equal parallelograms with their sides and angles severally equal, and so are similar as well as equal [11.24]. The parallelogram AFGD is common to both solids, and so is equal and similar to itself.

**Step 7.** Therefore the solid contained by the triangles ABF, DCG and the parallelograms ABCD, BCGF, AFGD, and the solid contained by the triangles AFE, DGH and the parallelograms EFGH, ADHE, AFGD, are contained by planes equal in multitude, five and five, which taken in corresponding pairs are similar and equal in magnitude. Hence the two solids are equal and similar [D11.10].

**Step 8.** Therefore the plane AFGD drawn through the diagonals AF, DG of the opposite faces divides the parallelepipedal solid into two equal solids; that is, the solid is bisected by the plane. Q.E.D.

**USED:** 1.34, 11.16, 11.24, 11.3, D11.10
**Human refs (from References field):** 1.34, D11.10
**Jaccard:** 0.400 — AI adds ['11.16', '11.24', '11.3']

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let CM, CN be two parallelepipedal solids on the same base, the parallelogram ACBL (whose opposite corners are A and B), and of the same height. Let the sides standing up from A, C, B, L be AF, CD, BH, LM in the solid CM and AG, CE, BK, LN in the solid CN, so that the upper face of CM is FDHM and the upper face of CN is GEKN; and let the extremities F, G, M, N lie on one straight line FN and the extremities D, E, H, K on one straight line DK, the points lying in the order F, G, M, N and D, E, H, K as in the figure, so that the two upper faces overlap in GMHE. I say that the solid CM is equal to the solid CN.

**Step 2.** A parallelepipedal solid is contained by parallel planes; therefore its faces are parallelograms and its opposite faces are equal [11.24]. Hence in the solid CM the faces ACDF, CBHD, BLMH, LAFM, FDHM are parallelograms, and in the solid CN the faces ACEG, CBKE, BLNK, LAGN, GEKN are parallelograms.

**Step 3.** Since CBHD is a parallelogram, DH = CB; since CBKE is a parallelogram, EK = CB [1.34]. Therefore DH = EK [CN1]. Take away the common part EH; the remainder DE is equal to the remainder HK [CN3].

**Step 4.** In the same way, since LAFM and LAGN are parallelograms, FM = AL and GN = AL [1.34], so FM = GN [CN1]; taking away the common part GM, the remainder FG is equal to the remainder MN [CN3].

**Step 5.** In the triangles DCE, HBK the two sides CD, CE are equal to the two sides BH, BK respectively, being opposite sides of the parallelograms CBHD, CBKE [1.34], and the base DE is equal to the base HK (Step 3). Therefore the angle DCE is equal to the angle HBK [1.8], and hence the triangle DCE is equal to the triangle HBK [1.4]. Similarly AF = LM and AG = LN, being opposite sides of the parallelograms LAFM, LAGN [1.34], and FG = MN (Step 4); therefore the angle FAG is equal to the angle MLN [1.8] and the triangle AFG is equal to the triangle MLN [1.4].

**Step 6.** Since FDHM is a parallelogram, FM is parallel to DH; hence the straight lines FN, DK are parallel, and the upper faces of both solids lie in the plane of these parallels. Now FD is parallel to AC, being the opposite side of the parallelogram ACDF, and GE is parallel to AC, being the opposite side of the parallelogram ACEG; and FD, GE are two distinct straight lines of the upper plane, so they are not in one plane with AC. Therefore FD is parallel to GE [11.9]. Likewise MH and NK are each parallel to LB (opposite sides of the parallelograms BLMH, BLNK) and are not in one plane with it, so MH is parallel to NK [11.9]. Consequently FGED and MNKH, whose remaining sides FG, DE and MN, HK lie on the parallels FN, DK, are parallelograms.

**Step 7.** The parallelograms FGED, MNKH are on the equal bases DE, HK (Step 3) and in the same parallels DK, FN. Therefore the parallelogram FGED is equal to the parallelogram MNKH [1.36]. They are moreover similar as well as equal: FD = MH, being opposite sides of the parallelogram FDHM [1.34], DE = HK, and since FD is parallel to MH and the straight line DK falls on them, the exterior angle MHK is equal to the interior and opposite angle FDE [1.29].

**Step 8.** The parallelogram ACDF is equal to the parallelogram BLMH, for they are opposite faces of the parallelepipedal solid CM [11.24]; and the parallelogram ACEG is equal to the parallelogram BLNK, for they are opposite faces of the parallelepipedal solid CN [11.24].

**Step 9.** The plane ACEG passes through the edge AC of the solid CM and through the points G, E lying on the sides FM, DH of its upper face; it therefore divides the solid CM into two solids: the prism contained by the two triangles AFG, DCE and the three parallelograms ACDF, FGED, ACEG, and the solid contained by the base ACBL, the upper face GMHE and the four parallelograms ACEG, CBHE, BLMH, LAGM. In the same way the plane BLMH passes through the edge LB of the solid CN and through the points M, H lying on the sides GN, EK of its upper face; it divides the solid CN into the prism contained by the two triangles MLN, HBK and the three parallelograms BLMH, MNKH, BLNK, and the very same solid contained by ACBL, GMHE, ACEG, CBHE, BLMH, LAGM.

**Step 10.** The two prisms are each contained by five planes, and the planes of the one are equal and similar to the planes of the other respectively: the triangle AFG to the triangle MLN and the triangle DCE to the triangle HBK, which are equal in all respects (Step 5); the parallelogram FGED to the parallelogram MNKH (Step 7); and the parallelogram ACDF to the parallelogram BLMH and the parallelogram ACEG to the parallelogram BLNK, which are opposite faces of parallelepipedal solids (Step 8). Therefore the prism contained by the triangles AFG, DCE and the parallelograms ACDF, FGED, ACEG is equal to the prism contained by the triangles MLN, HBK and the parallelograms BLMH, MNKH, BLNK [D11.10].

**Step 11.** To each of these equal prisms add the same solid, namely that on the base ACBL with the upper face GMHE (Step 9). The wholes are equal [CN2]; that is, the solid CM is equal to the solid CN.

**Step 12.** If instead the extremities lie in the order F, M, G, N and D, H, E, K, so that the upper faces FDHM, GEKN do not overlap, the same reasoning applies with addition and subtraction interchanged: DE = HK and FG = MN are obtained by adding the common parts HE, MG to the equals DH, EK and FM, GN [CN2]; the two prisms AFG-DCE and MLN-HBK are shown equal exactly as in Steps 5 to 10; and the solid on the base ACBL with the upper face FDKN is made up both of the solid CM together with the prism MLN-HBK and of the solid CN together with the prism AFG-DCE, so that, the equal prisms being taken away, the remainders CM, CN are equal [CN3].

Therefore parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another. Q.E.D.

**USED:** 11.24, 1.34, CN1, CN3, 1.8, 1.4, 11.9, 1.36, 1.29, D11.10, CN2

**USED:** 1.29, 1.34, 1.36, 1.4, 1.8, 11.24, 11.9, CN1, CN2, CN3, D11.10
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.364 — AI adds ['1.29', '11.24', '11.9', 'CN1', 'CN2', 'CN3', 'D11.10']

## Proposition 11.30
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another.

**Step 1.** Let the two parallelepipedal solids stand on the same base, the parallelogram ABCD, and be of the same height. Let the sides which stand up in the first solid be AE, BF, CG, DH, so that its face opposite the base is EFGH; let the sides which stand up in the second solid be AK, BL, CM, DN, so that its opposite face is KLMN; and let the extremities E, F, G, H and K, L, M, N not be on the same straight lines. Since the base ABCD is common, call the first solid "solid EFGH" and the second "solid KLMN". I say that solid EFGH is equal to solid KLMN.

**Step 2.** Each solid, being parallelepipedal, is contained by three pairs of parallel planes; in particular the face opposite to ABCD in each solid lies in a plane parallel to the plane of ABCD. Since the solids are of the same height, these opposite faces EFGH and KLMN lie in one and the same plane parallel to the plane of ABCD; call it the upper plane. Because the upper plane and the plane of the base are parallel, they do not meet (D11.8); hence no straight line of the base, such as AB, AD, DC or BC, lies in the upper plane, and no straight line of the upper plane lies in the plane of the base.

**Step 3.** By 11.24, the faces of a solid contained by parallel planes are parallelograms. Hence in solid EFGH the faces ABFE and DCGH are parallelograms, so that EF is parallel to AB and HG is parallel to DC; and in solid KLMN the faces ADNK and BCML are parallelograms, so that KN is parallel to AD and LM is parallel to BC.

**Step 4.** Let EF, HG, KN, LM be produced in both directions (P2). Each of these straight lines lies in the upper plane, and a straight line cannot be partly in a plane and partly out of it (11.1); so each remains in the upper plane when produced. Likewise EF produced remains in the plane ABFE, HG in the plane DCGH, KN in the plane ADNK, and LM in the plane BCML (11.1).

**Step 5.** I say that EF and KN are not parallel. For suppose KN were parallel to EF. Now AB is also parallel to EF (Step 3), and AB, KN are not in one plane with EF, since EF and KN lie in the upper plane while AB does not (Step 2). Therefore, by 11.9, AB is parallel to KN. But AD is also parallel to KN (Step 3), and AB, AD are not in one plane with KN, since AB and AD lie in the plane of the base while KN does not (Step 2). Therefore, by 11.9, AB is parallel to AD. But AB and AD meet one another at A, whereas parallel straight lines, being produced indefinitely, never meet (D1.23). This is impossible; therefore KN is not parallel to EF.

**Step 6.** Now EF and KN lie in one plane, the upper plane, and are not parallel; hence, by D1.23, being produced they meet. Let them meet at O. In the same manner, since HG is parallel to DC and KN to AD, and DC, AD meet at D, the lines HG and KN are not parallel and so meet when produced; let them meet at Q. Since EF is parallel to AB and LM to BC, and AB, BC meet at B, the lines EF and LM meet; let them meet at P. Since HG is parallel to DC and LM to BC, and DC, BC meet at C, the lines HG and LM meet; let them meet at R.

**Step 7.** The points O, P, Q, R all lie in the upper plane (Step 4). Moreover, O lies on EF and on KN, hence in the plane ABFE and in the plane ADNK; P lies on EF and on LM, hence in the planes ABFE and BCML; Q lies on HG and on KN, hence in the planes DCGH and ADNK; and R lies on HG and on LM, hence in the planes DCGH and BCML (Step 4).

**Step 8.** Join AO, BP, CR, DQ (P1). Consider the solid contained by the six planes: the plane of the base ABCD, the upper plane, the plane ABFE, the plane DCGH, the plane ADNK and the plane BCML. The plane of the base and the upper plane are parallel (Step 2). The planes ABFE and DCGH are parallel, being the planes of opposite faces of the parallelepipedal solid EFGH; and the planes ADNK and BCML are parallel, being the planes of opposite faces of the parallelepipedal solid KLMN. Therefore this third solid is contained by three pairs of parallel planes; that is, it is a parallelepipedal solid.

**Step 9.** The common section of two planes which cut one another is a straight line (11.3). The planes ABFE, DCGH, ADNK, BCML each contain two points of the base plane, namely A, B; D, C; A, D; B, C respectively, so they meet the plane of the base in the straight lines AB, DC, AD, BC; hence the face of the third solid in the plane of the base is ABCD, and the third solid stands on the same base ABCD as the other two. The same four planes meet the upper plane in the straight lines EF, HG, KN, LM respectively (Step 4); so the face of the third solid in the upper plane is the quadrilateral bounded by these four lines, whose angular points are the meeting points of EF with KN, of EF with LM, of HG with LM and of HG with KN, namely O, P, R, Q (Step 6). Thus the face opposite the base is OPRQ, and since it lies in the upper plane, the third solid is of the same height as the solids EFGH and KLMN. Call the third solid "solid OPRQ".

**Step 10.** The sides which stand up in solid OPRQ are the common sections of its adjacent lateral planes. The planes ABFE and ADNK both contain the points A and O (Step 7); their common section is a straight line (11.3) passing through A and O, that is, the straight line AO. Similarly BP is the common section of the planes ABFE and BCML, CR that of the planes DCGH and BCML, and DQ that of the planes DCGH and ADNK. Thus the sides which stand up in solid OPRQ are AO, BP, CR, DQ, with extremities O, P, R, Q.

**Step 11.** Now solid EFGH and solid OPRQ are parallelepipedal solids on the same base ABCD and of the same height, and the extremities of their sides which stand up are on the same straight lines: for E, F, O, P, the extremities of AE, BF, AO, BP, are all on the straight line EF, and H, G, Q, R, the extremities of DH, CG, DQ, CR, are all on the straight line HG (Step 6). Therefore, by 11.29, solid EFGH is equal to solid OPRQ.

**Step 12.** Again, solid KLMN and solid OPRQ are parallelepipedal solids on the same base ABCD and of the same height, and the extremities of their sides which stand up are on the same straight lines: for K, N, O, Q, the extremities of AK, DN, AO, DQ, are all on the straight line KN, and L, M, P, R, the extremities of BL, CM, BP, CR, are all on the straight line LM (Step 6). Therefore, by 11.29, solid KLMN is equal to solid OPRQ.

**Step 13.** Solid EFGH and solid KLMN are each equal to solid OPRQ; therefore, by CN1, solid EFGH is equal to solid KLMN. Therefore parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another. Q.E.D.

**USED:** 11.1, 11.24, 11.29, 11.3, 11.9, CN1, D1.23, D11.8, P1, P2
**Human refs (from References field):** 11.29
**Jaccard:** 0.100 — AI adds ['11.1', '11.24', '11.3', '11.9', 'CN1', 'D1.23', 'D11.8', 'P1', 'P2']

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let AE, CF be parallelepipedal solids of the same height on the equal bases AB, CD. Let the base AB be the parallelogram AHBL, in which A and B are opposite corners (so that AB is its diameter and L is adjacent to both A and B), with sides standing up AG, HK, BE, LM and opposite face GKEM; and let the base CD be the parallelogram CPDR, in which C and D are opposite corners (R being adjacent to both C and D), with sides standing up CO, PQ, DF, RS and opposite face OQFS. I say that the solid AE is equal to the solid CF.

**Step 2.** Case 1. First let the sides standing up HK, BE, AG, LM, PQ, DF, CO, RS be at right angles to the bases AB, CD. Then LM, being at right angles to the plane of AB, is the perpendicular drawn from the opposite face GKEM to the base, that is, the height of the solid AE [D6.4]; in the same way RS is the height of the solid CF. Since the solids are of the same height, LM is equal to RS.

**Step 3.** Produce CR in a straight line beyond R to T [P2], and make RT equal to AL [1.3]. In the plane of the base CD, on the straight line RT and at the point R on it, construct the angle TRU equal to the angle ALB [1.23], taking U on the side of RT remote from D, and make RU equal to LB [1.3]. Through U draw a straight line parallel to RT and through T a straight line parallel to RU [1.31], meeting at W; thus the parallelogram RW (RTWU) is completed in the plane of CD.

**Step 4.** Since the two sides TR, RU are equal to the two sides AL, LB respectively, and the angle TRU is equal to the angle ALB, the triangle TRU is equal to the triangle ALB [1.4]. Now the diameter TU bisects the parallelogram RW and the diameter AB bisects the parallelogram AB [1.34], so that RW is double the triangle TRU and AB is double the triangle ALB; therefore the parallelogram RW is equal to the parallelogram AB [CN2]. Moreover the angles of RW are severally equal to the angles of AB: the angle at R is equal to the angle at L by construction, the opposite angles at W and at B are equal to these [1.34], and the angles at T, U and at A, H are equal, since each of them together with the angle at R or at L makes two right angles [1.29]; and the sides about the equal angles are equal, RT, RU, TW, UW being equal to AL, LB, AH, HB [1.34], and so are proportional. Therefore the parallelogram RW is also similar to the parallelogram AB [D6.1]. Thus RW is equal and similar to the base AB, that is, to HL.

**Step 5.** On the base RW let the parallelepipedal solid XU be completed having RS for one of its sides standing up; that is, its sides standing up RS, TX, WV, Ud are at right angles to the plane of CD and each equal to RS, and its face opposite to the base RW is SXVd.

**Step 6.** Since LM is at right angles to the plane of AB, in which LA lies, the angle MLA is right; and since RS is at right angles to the plane of CD, in which RT lies, the angle SRT is right [D11.3]; therefore the angles MLA, SRT are equal [P4]. Also AL is equal to RT, and LM to RS (Step 2). Hence, exactly as in Step 4, the triangle SRT is equal to the triangle MLA [1.4]; the parallelograms RX (RTXS) and AM (ALMG), being double of these triangles [1.34], are equal [CN2]; and, all their angles being right and the sides about them equal, they are similar [D6.1]. Thus the parallelogram RX is equal and similar to the parallelogram AM. In the same way, since LB is equal to RU, LM to RS, and the angles MLB, SRU are right [D11.3] and therefore equal [P4], the parallelogram SU (RUdS) is equal and similar to the parallelogram LE (LBEM).

**Step 7.** Thus the three parallelograms HL, AM, LE of the solid AE, which meet at the vertex L, are equal and similar to the three parallelograms RW, RX, SU of the solid XU, which meet at the vertex R. But the remaining three faces of AE are the faces opposite to HL, AM, LE, and are equal and similar to them; and likewise the remaining three faces of XU are equal and similar to RW, RX, SU [11.24]. Therefore the six planes containing the solid AE are equal and similar to the six planes containing the solid XU [CN1], and so the solid AE is equal to the solid XU [D11.10].

**Step 8.** Now UW is parallel to RT, while DR meets RT at R. Hence DR is not parallel to UW; for otherwise DR and RT, being both parallel to UW, would be parallel to one another [1.30], which is impossible since they meet at R [D1.23]. Therefore DR and WU, which lie in the plane of CD and are not parallel, meet when produced [D1.23, P2]; let them be produced and meet at Y. Since the whole line UW lies on the side of RT remote from D, Y lies on DR produced beyond R, so that R is between D and Y.

**Step 9.** Through T draw the straight line aTb parallel to DY [1.31]. Since DY meets RT at R, aTb is not parallel to RT [1.30, as in Step 8]; and since PD and YW are each parallel to RT (PD being opposite to CR in the parallelogram CD, and YW opposite to RT in the parallelogram RW), aTb is parallel to neither of them, for otherwise it would be parallel to RT [1.30]. Hence aTb, being in one plane with PD and with YW, meets each of them when produced [D1.23, P2]; let PD produced meet aTb at a, and let YW produced meet aTb at b.

**Step 10.** Then RTbY is a parallelogram, since RT is parallel to Yb and RY to Tb; call it YT. Also RTaD is a parallelogram, since RT is parallel to Da (which lies on the line PD) and DR to Ta; call it DT. Further, CPaT is a parallelogram, its sides CT, Pa being parallel and its sides CP, Ta being each parallel to DR and hence to one another [1.30]; it is made up of the parallelograms CD, DT, which have the common side DR. And YbaD is a parallelogram, its sides Yb, Da being each parallel to RT and hence to one another [1.30], and its sides YD, ba being parallel; it is made up of the parallelograms YT, DT, which have the common side RT. On the bases YT, DT, CPaT, YbaD let the parallelepipedal solids YX, RI, CI, YI be completed, all having their sides standing up at right angles to the plane of CD and equal to RS, and let e, c, I be the extremities of the sides standing up at Y, b, a; so that the faces of these solids opposite to their bases are SXce, SXIF, OQIX, ecIF respectively. Then the solid CI is made up of the solids CF, RI, which have the common face RF (RDFS); and the solid YI is made up of the solids YX, RI, which have the common face RX (RTXS).

**Step 11.** The solids XU, YX are on the same base, the parallelogram RX, and are of the same height, since their faces UV (UWVd) and Yc (Ybce) opposite to RX lie in one plane, namely the plane through the straight line YW containing the sides standing up at U, W, Y, b; and the extremities of their sides standing up RU, TW, Sd, XV and RY, Tb, Se, Xc lie on the same straight lines YW, eV. Therefore the solid XU is equal to the solid YX [11.29]. But the solid XU is equal to the solid AE (Step 7); therefore the solid YX is equal to the solid AE [CN1].

**Step 12.** The parallelograms RW, YT are on the same base RT and in the same parallels RT, YW; therefore RW is equal to YT [1.35]. But RW is equal to AB (Step 4), and AB is equal to CD by hypothesis; therefore YT is equal to CD [CN1].

**Step 13.** Since the parallelograms CD, YT are equal, they have the same ratio to the parallelogram DT: as CD is to DT, so is YT to DT [5.7].

**Step 14.** The parallelepipedal solid CI is cut by the plane RF, which is parallel to its opposite planes CQ (CPQO) and TI (TaIX); for RF and CQ are opposite faces of the parallelepipedal solid CF, and RF and TI are opposite faces of the parallelepipedal solid RI. Therefore, as the base CD is to the base DT, so is the solid CF to the solid RI [11.25]. Again, the parallelepipedal solid YI is cut by the plane RX, which is parallel to its opposite planes Yc (Ybce) and DI (DaIF), these being the faces opposite to RX in the solids YX, RI respectively. Therefore, as the base YT is to the base TD, so is the solid YX to the solid RI [11.25].

**Step 15.** But as CD is to DT, so is YT to DT (Step 13); therefore, as the solid CF is to the solid RI, so is the solid YX to the solid RI [5.11]. Thus the solids CF, YX have the same ratio to the solid RI; therefore CF is equal to YX [5.9]. But YX is equal to AE (Step 11); therefore the solid AE is equal to the solid CF [CN1]. This proves the proposition when the sides standing up are at right angles to the bases.

**Step 16.** Case 2. Next let the sides standing up AG, HK, BE, LM, CO, PQ, DF, RS not be at right angles to the bases AB, CD. From the points K, E, G, M draw KK′, EE′, GG′, MM′ perpendicular to the plane of the base AB [11.11], meeting it at K′, E′, G′, M′, and join K′E′, E′M′, M′G′, G′K′; likewise from the points O, Q, F, S draw OO′, QQ′, FF′, SS′ perpendicular to the plane of the base CD [11.11], meeting it at O′, Q′, F′, S′, and join O′Q′, Q′F′, F′S′, S′O′. Let KM′ denote the parallelepipedal solid so formed whose base is K′M′ (G′K′E′M′) and whose opposite face is KM (GKEM), and QS′ the parallelepipedal solid whose base is O′S′ (O′Q′F′S′) and whose opposite face is QS (OQFS).

**Step 17.** The solids KM′, QS′ have their sides standing up KK′, EE′, GG′, MM′ and OO′, QQ′, FF′, SS′ at right angles to their bases K′M′, O′S′. Their bases are equal: for K′M′ is equal to KM, the face opposite to it in the solid KM′, and KM is equal to AB, the face opposite to it in the solid AE [11.24]; AB is equal to CD by hypothesis; and in the same way CD is equal to QS, and QS to O′S′ [11.24]; therefore K′M′ is equal to O′S′ [CN1]. Their heights are equal: for KK′, being the perpendicular drawn from the face KM of the solid AE to the plane of its base AB, is the height of AE, and likewise OO′ is the height of CF [D6.4]; and AE, CF are of the same height. Therefore the solids KM′, QS′ are on equal bases, of the same height, and have their sides standing up at right angles to their bases; hence, by Case 1 (Steps 2 to 15), the solid KM′ is equal to the solid QS′.

**Step 18.** Again, the solids KM′ and AE are on the same base KM and of the same height, their faces K′M′ and AB opposite to KM lying in the one plane of AB; and the extremities K′, E′, G′, M′ and H, B, A, L of their sides standing up KK′, EE′, GG′, MM′ and KH, EB, GA, ML are not on the same straight lines. Therefore the solid KM′ is equal to the solid AE [11.30]; and should these extremities happen to lie on the same straight lines, the same conclusion follows by [11.29]. In the same way the solid QS′ is equal to the solid CF [11.30].

**Step 19.** Therefore, since KM′ is equal to QS′, while KM′ is equal to AE and QS′ to CF, the solid AE is equal to the solid CF [CN1]. Hence in every case parallelepipedal solids which are on equal bases and of the same height are equal to one another. Q.E.D.

**USED:** 1.23, 1.29, 1.3, 1.30, 1.31, 1.34, 1.35, 1.4, 11.11, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, CN1, CN2, D1.23, D11.10, D11.3, D6.1, D6.4, P2, P4
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.400 — AI adds ['1.29', '1.3', '1.30', '1.31', '1.34', '1.4', '11.11', 'CN1', 'CN2', 'D1.23', 'D11.3', 'D6.1', 'D6.4', 'P2', 'P4']

## Proposition 11.32
**Statement:** Parallelepipedal solids which are of the same height are to one another as their bases.

**Step 1.** Let AB, CD be parallelepipedal solids of the same height, with bases AE and CF respectively. Let the base AE be the parallelogram ARES, so that AE is a diameter of it and AR is parallel to SE; and let the base CF be the parallelogram CGFL, so that CF is a diameter of it, CG is parallel to LF and CL is parallel to GF. Let GN, FD be the edges of the solid CD standing up from G, F, so that the face of CD through GF is the parallelogram GD, and the face of CD through CL is the face opposite to GD. I say that, as the base AE is to the base CF, so is the solid AB to the solid CD.

**Step 2.** First a triangle equal to the base AE is constructed. Produce AR beyond R to T [P2], cut off RT equal to AR [1.3], and join ET [P1].

**Step 3.** The triangles ARE, RTE stand on the equal bases AR, RT, both lying on the straight line AT, and their common vertex E lies on SE, which is parallel to AT; so they are in the same parallels AT, SE. Therefore the triangle ARE is equal to the triangle RTE [1.38].

**Step 4.** Since AE is a diameter of the parallelogram ARES, it bisects the parallelogram; so the triangle ARE is equal to the triangle ASE [1.34]. Therefore the triangle RTE is equal to the triangle ASE [CN1].

**Step 5.** The triangle ATE is made up of the triangles ARE, RTE (RE dividing it), and the parallelogram ARES is made up of the triangles ARE, ASE (AE dividing it). Adding the triangle ARE to the equal triangles RTE, ASE, the triangle ATE is equal to the parallelogram ARES, that is, to the base AE [CN2].

**Step 6.** Now, in the plane of the base CF and on the side of GF remote from C, apply to the straight line GF a parallelogram GFHK equal to the triangle ATE, in the angle FGK equal to the angle GFL [1.44]; K is the vertex adjacent to G and H the vertex adjacent to F, so that GK is parallel to FH and GF is parallel to KH. Then the parallelogram GH is equal to the triangle ATE, and hence to the base AE [CN1].

**Step 7.** Since CG is parallel to LF and the straight line GF falls on them, the interior angles CGF, GFL on the same side are together equal to two right angles [1.29]. But the angle FGK is equal to the angle GFL; therefore the angles CGF, FGK are together equal to two right angles [CN2, CN1]. These are adjacent angles which the straight lines GC, GK, lying on opposite sides of GF, make with GF at the point G; therefore CG is in a straight line with GK [1.14].

**Step 8.** Again, since GK is parallel to FH and GF falls on them, the angles FGK, GFH are together equal to two right angles [1.29]; and the angle FGK is equal to the angle GFL, so the angles GFL, GFH are together equal to two right angles [CN2, CN1]. The straight lines FL, FH lie on opposite sides of GF; therefore LF is in a straight line with FH [1.14].

**Step 9.** Hence CK and LH are straight lines, and they are parallel, being CG and LF produced. Moreover CL is parallel to GF and GF is parallel to KH, so CL is parallel to KH [1.30]. Therefore CKHL is a parallelogram, the parallelogram CH, and it is made up of the two parallelograms CF and GH lying side by side along GF.

**Step 10.** Through K, H draw KX, HQ parallel to GN [1.31] and equal to it [1.3], and let the parallelepipedal solid GQ be completed on the base GH, Q being its vertex opposite to G; its upper face NDQX lies in the plane of the upper face of CD, and its face through KH is opposite to its face GD. The solids CD, GQ have their bases in the plane of CH and their upper faces in one plane; therefore GQ has the same height as CD, and the two solids together make up one parallelepipedal solid CQ on the base CH.

**Step 11.** The solid CQ is cut by the plane GD into the solids CD, GQ, whose bases are CF, GH; and the plane GD is parallel to the opposite faces of CQ, namely to the face through CL (opposite to GD in the parallelepipedal solid CD) and to the face through KH (opposite to GD in the parallelepipedal solid GQ). Therefore, as the base CF is to the base GH, so is the solid CD to the solid GQ [11.25].

**Step 12.** The solids AB, GQ are on equal bases, since the base GH is equal to the base AE [Step 6], and they are of the same height, since GQ has the height of CD [Step 10] and CD has by hypothesis the height of AB. Therefore the solid AB is equal to the solid GQ [11.31].

**Step 13.** Since the base GH is equal to the base AE, the base CF has to the base GH the same ratio as to the base AE [5.7]; and since the solid GQ is equal to the solid AB, the solid CD has to the solid GQ the same ratio as to the solid AB [5.7]. Therefore, by Step 11, as the base CF is to the base AE, so is the solid CD to the solid AB [5.11].

**Step 14.** Hence, inversely, as the base AE is to the base CF, so is the solid AB to the solid CD [5.7 Por.]. Therefore parallelepipedal solids which are of the same height are to one another as their bases. Q.E.D.

Note on path choice: the parallelogram equal to AE is applied to GF by 1.44 after first converting AE into an equal triangle (Steps 2–5), because 1.44 applies only a triangle to a given straight line, while 1.45 constructs a parallelogram in a given angle but not on a given line; this is the most direct route to a parallelogram on GF equal to AE.

**USED:** 1.14, 1.29, 1.3, 1.30, 1.31, 1.34, 1.38, 1.44, 11.25, 11.31, 5.11, 5.7, CN1, CN2, P1, P2
**Human refs (from References field):** 1.45, 11.25, 11.31
**Jaccard:** 0.118 — AI adds ['1.14', '1.29', '1.3', '1.30', '1.31', '1.34', '1.38', '1.44', '5.11', '5.7', 'CN1', 'CN2', 'P1', 'P2']; Human adds ['1.45']

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

Let AB, CD be similar parallelepipedal solids. Let the solid angle of AB at E be contained by the plane angles AEG, AEH, GEH, so that the three faces of AB meeting at E are the parallelograms AG (on AE, EG), AH (on AE, EH), GH (on EG, EH); and let the solid angle of CD at F be contained by CFN, CFR, NFR, the faces at F being the parallelograms CN (on CF, FN), CR (on CF, FR), NR (on FN, FR). Let AE be the side corresponding to CF, EG to FN, and EH to FR, the faces AG, AH, GH being similar to CN, CR, NR respectively. I say that solid AB has to solid CD the ratio triplicate of that which AE has to CF.

**Step 1.** Since AB, CD are similar solids, they are contained by similar planes equal in multitude (D11.9); thus AG, AH, GH are similar to CN, CR, NR respectively. Therefore (D6.1) angle AEG = angle CFN, angle AEH = angle CFR, angle GEH = angle NFR, and the sides about the equal angles are proportional: AE:EG = CF:FN and AE:EH = CF:FR. Alternately (5.16), AE:CF = EG:FN and AE:CF = EH:FR.

**Step 2.** Produce AE, GE, HE beyond E to K, L, M (P2), and cut off EK = CF, EL = FN, EM = FR (1.3). Drawing parallels through K, L, M (1.31), complete the parallelograms KL (on EK, EL), KM (on EK, EM), LM (on EL, EM), and complete the parallelepipedal solid KP having these three parallelograms for its faces at E. Complete also (1.31) the parallelogram GK on GE, EK, and on the bases GK, KL complete the parallelepipedal solids EO, QL, each having EH for its edge at E; let QE be their common face, the parallelogram on EK, EH. Since K, L lie on AE, GE produced, the parallelograms AG, GK, KL all lie in the plane AEG; and since M lies on HE produced, the parallelograms QE, KM lie in the plane AEH.

**Step 3.** Since AK, GL are straight lines cutting one another at E, angle KEL = angle AEG (1.15), and so angle KEL = angle CFN (CN1). In the same way, from the straight lines AK, HM, angle KEM = angle AEH = angle CFR, and from GL, HM, angle LEM = angle GEH = angle NFR (1.15, CN1).

**Step 4.** [Lemma] Two parallelograms which have two adjacent sides equal to two adjacent sides respectively and the included angles equal are both equal and similar. For the remaining sides of each are equal to the sides opposite them (1.34), so the four sides of the one are equal to the four sides of the other respectively; the angles opposite the equal included angles are equal to them (1.34), and the remaining two angles of each, being what is left when the included angle is taken from two right angles (1.29), are also equal (CN3); thus the angles are severally equal, and the sides about the equal angles, being equal, have the same ratios (5.7, 5.11); hence the parallelograms are similar (D6.1). Further, joining in each the diagonal which cuts off the triangle on the two given sides (P1), these triangles have two sides equal to two sides and the included angles equal, so they are equal (1.4); and each parallelogram is double its triangle (1.34); therefore the parallelograms are equal (CN2).

**Step 5.** In the parallelograms KL, CN, the sides KE, EL are equal to CF, FN (Step 2) and angle KEL = angle CFN (Step 3); by Step 4, KL is equal and similar to CN. Likewise KM, whose sides KE, EM equal CF, FR with angle KEM = angle CFR, is equal and similar to CR; and LM, whose sides EL, EM equal FN, FR with angle LEM = angle NFR, is equal and similar to NR.

**Step 6.** The three remaining faces of KP, opposite to KL, KM, LM, are parallelograms (11.24). The face opposite to KL has for two adjacent sides, meeting at M, the sides of KM and LM opposite to EK and EL, which are equal to EK, EL (1.34) and parallel to them by construction, and hence equal to CF, FN (CN1); and since these two sides meeting at M are parallel to EK, EL meeting at E and are not in the same plane with them, the angle they contain is equal to angle KEL (11.10), that is, to angle CFN (CN1). In exactly the same way the face of CD opposite to CN is a parallelogram (11.24) having two adjacent sides, meeting at R, equal to CF, FN (1.34) and containing an angle equal to angle CFN (11.10). Therefore by Step 4 these two faces, opposite to KL and CN, are equal and similar to one another; and the same argument shows the face opposite KM equal and similar to the face opposite CR, and the face opposite LM equal and similar to the face opposite NR.

**Step 7.** Thus the six faces of KP are similar and equal to the six faces of CD respectively, so that solid KP is equal and similar to solid CD (D11.10); in particular solid KP = solid CD.

**Step 8.** Since CF = EK, AE:CF = AE:EK (5.7); since FN = EL, EG:FN = EG:EL (5.7); and since FR = EM, EH:FR = EH:EM (5.7). But AE:CF = EG:FN = EH:FR (Step 1). Therefore AE:EK = GE:EL = HE:EM (5.11).

**Step 9.** The parallelograms AG, GK lie between the straight line AK and the straight line through G parallel to it, with bases AE, EK; hence AG:GK = AE:EK (6.1). The parallelograms GK, KL lie between GL and the straight line through K parallel to it, with bases GE, EL; hence GK:KL = GE:EL (6.1). The parallelograms QE, KM lie between HM and the straight line through K parallel to it, with bases HE, EM; hence QE:KM = HE:EM (6.1). Combining with Step 8, AG:GK = GK:KL = QE:KM (5.11).

**Step 10.** The solids AB, EO, QL have their bases AG, GK, KL in the plane AEG, and the faces opposite these bases all pass through H; so they are of the same height, namely the perpendicular from H to that plane. Therefore AB:EO = AG:GK and EO:QL = GK:KL (11.32). Again, the solids QL, KP have the faces QE, KM in the plane AEH, and the faces opposite to these both pass through L; so on these bases they are of the same height, the perpendicular from L to that plane. Therefore QL:KP = QE:KM (11.32).

**Step 11.** From Steps 9 and 10, AB:EO = AG:GK = GK:KL = EO:QL, and EO:QL = GK:KL = QE:KM = QL:KP; hence AB:EO = EO:QL = QL:KP (5.11). And since solid KP = solid CD (Step 7), QL:KP = QL:CD (5.7). Therefore AB:EO = EO:QL = QL:CD, so that the four solids AB, EO, QL, CD are continuously proportional, and AB has to CD the ratio triplicate of that which AB has to EO (D5.10).

**Step 12.** But AB:EO = AG:GK = AE:EK (Steps 10, 9), and AE:EK = AE:CF (Step 8); hence AB:EO = AE:CF (5.11). Therefore solid AB has to solid CD the ratio triplicate of that which the corresponding side AE has to the corresponding side CF. Q.E.D.

**USED:** D11.9, D6.1, 5.16, P2, 1.3, 1.31, 1.15, CN1, 1.34, 1.29, CN3, 5.7, 5.11, P1, 1.4, CN2, 11.24, 11.10, D11.10, 6.1, 11.32, D5.10

**USED:** 1.15, 1.29, 1.3, 1.31, 1.34, 1.4, 11.10, 11.24, 11.32, 5.11, 5.16, 5.7, 6.1, CN1, CN2, CN3, D11.10, D11.9, D5.10, D6.1, P1, P2
**Human refs (from References field):** 11.24, 11.32, 6.1, D11.10, D5.10
**Jaccard:** 0.227 — AI adds ['1.15', '1.29', '1.3', '1.31', '1.34', '1.4', '11.10', '5.11', '5.16', '5.7', 'CN1', 'CN2', 'CN3', 'D11.9', 'D6.1', 'P1', 'P2']

## Proposition 11.34
**Statement:** In equal parallelepipedal solids the bases are reciprocally proportional to the heights; and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let AB and CD be parallelepipedal solids. Let the base of AB be the parallelogram EH, with vertices E, A, H, L in order, let its sides standing up be EF, AG, HK, LB, and let the face opposite the base be the parallelogram FK (vertices F, G, K, B). Let the base of CD be the parallelogram NQ, with vertices N, C, Q, P in order, let its sides standing up be NO, CM, QR, PD, and let the face opposite the base be the parallelogram OR (vertices O, M, R, D). The height of each solid is the perpendicular drawn from the face opposite the base to the plane of the base [D6.4]. We must prove: (I) if the solid AB is equal to the solid CD, then the base EH is to the base NQ as the height of CD is to the height of AB; and (II) if the base EH is to the base NQ as the height of CD is to the height of AB, then the solid AB is equal to the solid CD.

**Step 2.** Case 1: let the sides which stand up be at right angles to the bases. Since AG is at right angles to the plane of the base EH, AG is the height of AB; likewise CM is the height of CD [D6.4]. So in this case we must prove (I) AB = CD implies EH : NQ = CM : AG, and (II) EH : NQ = CM : AG implies AB = CD.

**Step 3.** First let AG = CM. Then AB and CD are of the same height, so that AB : CD = EH : NQ [11.32].

**Step 4.** (I) Let AB = CD. Then AB : CD is the ratio of a magnitude to an equal magnitude, and so is CM : AG. Any two such ratios are the same: whatever equimultiples are taken, the multiple of the antecedent exceeds, equals or falls short of the multiple of the consequent according as the first multiplier exceeds, equals or falls short of the second, alike in both ratios [D5.5]. Hence AB : CD = CM : AG, and therefore EH : NQ = CM : AG [Step 3, 5.11].

**Step 5.** (II) Let EH : NQ = CM : AG. Then AB : CD = CM : AG [Step 3, 5.11]. But CM : AG is the ratio of a magnitude to an equal magnitude, and so is CD : CD; hence CM : AG = CD : CD [D5.5], and AB : CD = CD : CD [5.11]. Therefore AB = CD [5.9].

**Step 6.** Next let AG and CM be unequal, and first let CM be the greater. From CM cut off CT equal to AG [1.3]. In the plane of the face NCMO draw TU through T parallel to CN, meeting NO at U, and in the plane of the face CQRM draw TW through T parallel to CQ, meeting QR at W [1.31]. The straight lines TU, TW meeting at T are parallel to the straight lines CN, CQ meeting at C and are not in the plane of NQ; hence the plane through TU, TW is parallel to the plane of NQ [11.15]. Let this plane meet PD at V. It cuts off from CD the solid CV, contained by the base NQ, the plane TV parallel to it, and portions of the four side faces of CD, of which the opposite ones are parallel; so CV is a parallelepipedal solid on the base NQ. Its sides standing up CT, NU, QW, PV, being parts of CM, NO, QR, PD, are at right angles to NQ; therefore the height of CV is CT, which is equal to AG [D6.4].

**Step 7.** The solids AB and CV are thus of the same height; therefore AB : CV = EH : NQ [11.32].

**Step 8.** Now regard the parallelogram MQ (the face CQRM) as the base of the solid CD, and the parallelogram TQ (the face CQWT, which lies in the same plane) as the base of the solid CV. The faces opposite these bases, PNOD of CD and PNUV of CV, lie in one plane, which is parallel to the plane of CQRM; hence with respect to these bases the solids CD, CV are of the same height, and CD : CV = MQ : TQ [11.32].

**Step 9.** The parallelograms MQ, TQ have their bases CM, CT on the same straight line and lie between the same parallels CM, QR; they are therefore under the same height, and MQ : TQ = CM : CT [6.1]. Hence CD : CV = CM : CT [5.11]. And since CT = AG, CM : CT = CM : AG [5.7]; therefore CD : CV = CM : AG [5.11].

**Step 10.** (I) Let AB = CD. Then AB : CV = CD : CV [5.7]. But AB : CV = EH : NQ [Step 7] and CD : CV = CM : AG [Step 9]. Therefore EH : NQ = CM : AG [5.11].

**Step 11.** (II) Let EH : NQ = CM : AG. Since AB : CV = EH : NQ [Step 7] and CD : CV = CM : AG [Step 9], we have AB : CV = CD : CV [5.11]. Therefore AB = CD [5.9].

**Step 12.** If instead AG is greater than CM, the same construction is made on AG (a part of AG equal to CM is cut off, and through its extremity a plane parallel to EH is drawn), and the reasoning of Steps 6-11 with the two solids interchanged shows: (I) if AB = CD, then NQ : EH = AG : CM, whence, inversely, EH : NQ = CM : AG [5.7 Por.]; (II) if EH : NQ = CM : AG, then inversely NQ : EH = AG : CM [5.7 Por.], whence CD = AB. Thus both parts of the proposition hold whenever the sides which stand up are at right angles to the bases.

**Step 13.** Case 2: let the sides which stand up not be at right angles to the bases. From F, G, K, B draw FS, GX, KY, BZ perpendicular to the plane of EH, meeting it at S, X, Y, Z; and from O, M, R, D draw OS', MX', RY', DZ' perpendicular to the plane of NQ, meeting it at S', X', Y', Z' [11.11].

**Step 14.** Complete the solid FY. Since FS, GX, KY, BZ are at right angles to the same plane, they are parallel to one another [11.6]. FK is a parallelogram [11.24], so that FG is parallel to BK and GK to FB. Hence FG, FS meeting at F are parallel to BK, BZ meeting at B, and GK, GX meeting at G are parallel to FB, FS meeting at F, the pairs not being in one plane; so the plane through FG, FS is parallel to the plane through BK, BZ, and the plane through GK, GX is parallel to the plane through FB, FS [11.15]. Also the plane of EH, which contains S, X, Y, Z, is parallel to the plane of FK, these being opposite faces of the parallelepipedal solid AB. Thus the solid FY, contained by the planes of FK and EH and the four planes just named, is contained by three pairs of parallel planes: it is a parallelepipedal solid, having FK as one face and its opposite face SY, the parallelogram SXYZ [11.24], in the plane of EH; and its sides FS, GX, KY, BZ standing up on SY are at right angles to SY. In the same way the solid OY' is completed: a parallelepipedal solid having OR as one face, its opposite face S'Y' in the plane of NQ, and its sides OS', MX', RY', DZ' at right angles to S'Y'.

**Step 15.** The solids AB and FY are on the same base FK and of the same height, for their faces EH and SY opposite to FK lie in one plane, the plane of EH. Therefore AB = FY, whether the extremities of the sides standing up are on the same straight lines or not [11.29, 11.30]. In the same way CD = OY' [11.29, 11.30].

**Step 16.** EH and FK are opposite faces of AB, and SY and FK are opposite faces of FY; hence EH = FK and SY = FK [11.24], so that EH = SY [CN1]. In the same way NQ = OR and S'Y' = OR [11.24], so that NQ = S'Y' [CN1].

**Step 17.** The height of AB is the perpendicular drawn from its face FK to the plane of EH, that is, FS; and FS, being the side of FY standing up at right angles to its base SY, is also the height of FY [D6.4]. Likewise OS' is the height both of CD and of OY'.

**Step 18.** Since EH = SY, EH : S'Y' = SY : S'Y'; and since NQ = S'Y', EH : NQ = EH : S'Y' [5.7]. Therefore EH : NQ = SY : S'Y' [5.11].

**Step 19.** (I) Let AB = CD. Since AB = FY and CD = OY' [Step 15], FY = OY' [CN1]. The solids FY, OY' have their sides standing up at right angles to their bases SY, S'Y'; hence, by Case 1, SY : S'Y' = OS' : FS. Therefore EH : NQ = OS' : FS [Step 18, 5.11]; that is, the base of AB is to the base of CD as the height of CD is to the height of AB [Step 17].

**Step 20.** (II) Let EH : NQ = OS' : FS, the height of CD to the height of AB. Then SY : S'Y' = OS' : FS [Step 18, 5.11], so that in the solids FY, OY', whose sides standing up are at right angles to their bases, the bases are reciprocally proportional to the heights; hence, by Case 1, FY = OY'. But AB = FY and CD = OY' [Step 15]; therefore AB = CD [CN1].

**Step 21.** Therefore in equal parallelepipedal solids the bases are reciprocally proportional to the heights, and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal. Q.E.D.

Path note: in Step 8 the ratio CD : CV is taken directly from 11.32 by regarding the side faces MQ, TQ as bases; the alternative route through 11.25 (CD cut by the plane TV parallel to opposite planes) yields only the ratio of the two parts and would then require composition (5.18) to give whole to part, so the 11.32 route was chosen as the more direct.

**USED:** 1.3, 1.31, 11.11, 11.15, 11.24, 11.29, 11.30, 11.32, 11.6, 5.11, 5.7, 5.9, 6.1, CN1, D5.5, D6.4
**Human refs (from References field):** 11.25, 11.29, 11.30, 11.31, 11.32, 5.7, 5.9, 6.1
**Jaccard:** 0.333 — AI adds ['1.3', '1.31', '11.11', '11.15', '11.24', '11.6', '5.11', 'CN1', 'D5.5', 'D6.4']; Human adds ['11.25', '11.31']

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

**Step 1.** Let BAC, EDF be two equal rectilineal angles, and from the vertices A, D let the elevated straight lines AG, DM be set up, containing with the original straight lines equal angles respectively, so that the angle GAB is equal to the angle MDE and the angle GAC is equal to the angle MDF. Let G, M be points taken at random on AG, DM; from G let GL be drawn perpendicular to the plane through BA, AC, and from M let MN be drawn perpendicular to the plane through ED, DF [11.11], meeting the planes at L, N; and let LA, ND be joined [P1]. I say that the angle GAL is equal to the angle MDN.

**Step 2.** From AG let AH be cut off equal to DM [1.3]. The triangle AGL lies in one plane [11.2]; in that plane, through the point H, let HK be drawn parallel to GL [1.31]. Now HK is not parallel to AL; for otherwise GL and AL, being each parallel to HK, would be parallel to one another [1.30], whereas they meet at L. Therefore HK and AL, being in one plane and not parallel, meet when produced [D1.23]; let them meet at K. Thus K lies on the straight line AL, and, since H lies on AG, the angle HAK is the angle GAL.

**Step 3.** Since GL is at right angles to the plane through BA, AC, and HK is parallel to GL, HK is also at right angles to the plane through BA, AC [11.8]; hence HK makes right angles with every straight line in that plane which meets it [D11.3].

**Step 4.** In the plane through BA, AC let KC be drawn from K perpendicular to AC and KB perpendicular to AB [1.12], C and B being the feet of these perpendiculars on AC and AB; likewise in the plane through ED, DF let NF, NE be drawn from N perpendicular to DF, DE [1.12]. Let HC, HB, BC, MF, ME, EF be joined [P1]. Since KA, KC, KB lie in the plane through BA, AC and meet HK, the angles HKA, HKC, HKB are right [D11.3]; and since MN is at right angles to the plane through ED, DF, the angles MND, MNF, MNE are likewise right [D11.3].

**Step 5.** Since the angle HKA is right, the square on HA is equal to the squares on HK, KA [1.47]; and since the angle KCA is right, the square on KA is equal to the squares on KC, CA [1.47]. Adding the square on HK to each side of the latter equality, the squares on HK, KA are equal to the squares on HK, KC, CA [CN2]; therefore the square on HA is equal to the squares on HK, KC, CA [CN1]. Again, since the angle HKC is right, the square on HC is equal to the squares on HK, KC [1.47]; adding the square on CA, the squares on HC, CA are equal to the squares on HK, KC, CA [CN2]. Therefore the square on HA is equal to the squares on HC, CA [CN1]; hence the angle HCA is right [1.48]. In the same way, since the square on MD is equal to the squares on MN, ND, the square on ND to the squares on NF, FD, and the square on MF to the squares on MN, NF [1.47], the square on MD is equal to the squares on MF, FD [CN2, CN1], so that the angle MFD is right [1.48]. By the same argument the angles HBA, MED are also right.

**Step 6.** Since the angles HCA, MFD are right, they are equal to one another [P4]. And the angle HAC, which is the angle GAC, is equal to the angle MDF by hypothesis; and the side AH is equal to the side DM, each subtending one of the equal right angles. Therefore the triangles HAC, MDF have two angles equal to two angles respectively and one side equal to one side; hence AC is equal to DF and HC to MF [1.26]. Similarly, since the angles HBA, MED are right and therefore equal [P4], the angle HAB is equal to the angle MDE by hypothesis, and AH is equal to DM, the triangles HAB, MDE give AB equal to DE and HB equal to ME [1.26].

**Step 7.** Since AC is equal to DF and AB to DE, the two sides CA, AB are equal to the two sides FD, DE respectively; and the angle CAB is equal to the angle FDE by hypothesis. Therefore the base BC is equal to the base EF, and the remaining angles are equal to the remaining angles: the angle ACB is equal to the angle DFE, and the angle ABC to the angle DEF [1.4].

**Step 8.** The angle ACK is right, being the angle of the perpendicular KC to AC, and the angle DFN is right; therefore they are equal [P4]. Subtracting from them the equal angles ACB, DFE, the remaining angle BCK is equal to the remaining angle EFN [CN3]. In the same way the right angles ABK, DEN are equal [P4], and subtracting the equal angles ABC, DEF, the remaining angle CBK is equal to the remaining angle FEN [CN3].

**Step 9.** Therefore the triangles BCK, EFN have two angles equal to two angles respectively and the side BC, adjoining the equal angles, equal to the side EF; hence CK is equal to FN and BK to EN [1.26].

**Step 10.** Since AC is equal to DF and CK to FN, the two sides AC, CK are equal to the two sides DF, FN respectively, and the angle ACK is equal to the angle DFN, both being right [P4]; therefore the base AK is equal to the base DN [1.4].

**Step 11.** Since AH is equal to DM, the square on AH is equal to the square on DM. But the angle AKH is right, so the square on AH is equal to the squares on AK, KH [1.47]; and the angle DNM is right, so the square on DM is equal to the squares on DN, NM [1.47]. Therefore the squares on AK, KH are equal to the squares on DN, NM [CN1]. Of these the square on AK is equal to the square on DN, since AK is equal to DN; therefore the remaining square on KH is equal to the remaining square on NM [CN3], so that KH is equal to NM.

**Step 12.** Thus in the triangles HAK, MDN the two sides HA, AK are equal to the two sides MD, DN respectively, and the base HK is equal to the base MN; therefore the angle HAK is equal to the angle MDN [1.8].

**Step 13.** But the angle HAK is the angle GAL, since H lies on AG and K lies on AL (Step 2). Therefore the angle GAL is equal to the angle MDN, which was to be proved.

*Path note:* the congruence route (cutting off AH = DM and using 1.26, 1.4, 1.8) was chosen over a proportional route through Book 6 (6.4, 6.6, 6.7) because it reaches the equal angles directly without ratios; the existence of K on AL is justified by 11.2, 1.30 and D1.23 rather than read from a figure.

**USED:** P1, P4, CN1, CN2, CN3, D1.23, D11.3, 1.3, 1.4, 1.8, 1.12, 1.26, 1.30, 1.31, 1.47, 1.48, 11.2, 11.8, 11.11

**USED:** 1.12, 1.26, 1.3, 1.30, 1.31, 1.4, 1.47, 1.48, 1.8, 11.11, 11.2, 11.8, CN1, CN2, CN3, D1.23, D11.3, P1, P4
**Human refs (from References field):** 1.26, 1.4, 1.47, 1.48, 1.8, 11.8
**Jaccard:** 0.316 — AI adds ['1.12', '1.3', '1.30', '1.31', '11.11', '11.2', 'CN1', 'CN2', 'CN3', 'D1.23', 'D11.3', 'P1', 'P4']

## Proposition 11.36
**Statement:** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

**Step 1.** Let A, B, C be three straight lines in proportion, so that A : B = B : C. Let a solid angle be set out at the point E, contained by the three plane angles DEG, GEF, FED, and let each of the straight lines ED, EF, EG be made equal to the mean B [1.3]. Let the parallelepipedal solid EK be completed, having ED, EF, EG as its three edges meeting at E. Since its three edges at E are each equal to the mean B, EK is the parallelepipedal solid on the mean which is equilateral.

**Step 2.** Let LM be set out equal to A [1.3], and on the straight line LM, at the point L on it, let a solid angle be constructed equal to the solid angle at E [11.26], namely the angle contained by the plane angles NLO, OLM, MLN, so that the angle NLO is equal to the angle DEG, the angle OLM to the angle GEF, and the angle MLN to the angle FED. Let LO be made equal to B and LN equal to C [1.3], and let the parallelepipedal solid LH be completed, having LM, LN, LO as its three edges meeting at L.

**Step 3.** The solid LH is the parallelepipedal solid formed out of the three straight lines A, B, C, since its edges at L are LM = A, LO = B, LN = C; and the solid EK is equiangular with it, since by construction the solid angle at E is equal to the solid angle at L. It remains to prove that the solid LH is equal to the solid EK.

**Step 4.** Since A : B = B : C, while LM = A, EF = B, ED = B and LN = C, and equal magnitudes have the same ratio to the same magnitude and the same magnitude has the same ratio to equal magnitudes [5.7], we have LM : EF = A : B and ED : LN = B : C; therefore LM : EF = ED : LN [5.11].

**Step 5.** Consider the parallelogram MN, contained by LM, LN about the angle MLN, and the parallelogram DF, contained by ED, EF about the angle DEF. The angle MLN is equal to the angle DEF (Step 2), so the two parallelograms are equiangular; and by Step 4 the sides about the equal angles are reciprocally proportional, namely LM : EF = DE : LN. But equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal [6.14]; therefore the parallelogram MN is equal to the parallelogram DF.

**Step 6.** Now there are two equal plane angles, DEF and NLM, and on their vertices E and L there are set up the elevated straight lines EG and LO, which are equal to one another, each being equal to B [CN1], and which contain equal angles with the original straight lines respectively: the angle GED is equal to the angle OLN and the angle GEF is equal to the angle OLM (Step 2). Therefore the perpendiculars drawn from G and O to the planes through DEF and NLM are equal to one another [11.35, Porism].

**Step 7.** The perpendicular from G to the plane of DEF is the height of the solid EK standing on the base DF, and the perpendicular from O to the plane of NLM is the height of the solid LH standing on the base MN; hence the solids EK and LH are of the same height.

**Step 8.** Thus the parallelepipedal solids LH and EK are on equal bases MN, DF (Step 5) and of the same height (Step 7). But parallelepipedal solids which are on equal bases and of the same height are equal to one another [11.31]; therefore the solid LH is equal to the solid EK.

**Step 9.** And LH is the parallelepipedal solid formed out of the three proportional straight lines A, B, C, while EK is the parallelepipedal solid on the mean B which is equilateral but equiangular with LH. Therefore, if three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid. Q.E.D.

**USED:** 1.3, 11.26, 11.31, 11.35, 5.11, 5.7, 6.14, CN1
**Human refs (from References field):** 11.31, 11.35, 6.14
**Jaccard:** 0.375 — AI adds ['1.3', '11.26', '5.11', '5.7', 'CN1']

## Proposition 11.37
**Statement:** If four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described will also be proportional; and, if the parallelepipedal solids on them which are similar and similarly described be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let AB, CD, EF, GH be four straight lines, and let KA, LC, ME, NG be parallelepipedal solids described on AB, CD, EF, GH respectively, similar and similarly situated to one another, so that AB, CD, EF, GH are corresponding sides of the four solids. First let AB : CD = EF : GH; I say that KA : LC = ME : NG.

**Step 2.** Since the solid KA is similar to the solid LC, and AB, CD are corresponding sides, KA has to LC the ratio triplicate of that which AB has to CD [11.33]. For the same reason ME has to NG the ratio triplicate of that which EF has to GH [11.33].

**Step 3.** Let X be a third proportional to AB, CD, so that AB : CD = CD : X, and let Y be a third proportional to CD, X, so that CD : X = X : Y [6.11]. Then AB, CD, X, Y are four straight lines continuously proportional, and therefore AB has to Y the ratio triplicate of that which AB has to CD [D5.10]. Hence, by Step 2, KA : LC = AB : Y.

**Step 4.** In the same way let Z be a third proportional to EF, GH and W a third proportional to GH, Z [6.11], so that EF : GH = GH : Z = Z : W. Then EF has to W the ratio triplicate of that which EF has to GH [D5.10], and hence, by Step 2, ME : NG = EF : W.

**Step 5.** Since AB : CD = EF : GH by hypothesis, while CD : X = AB : CD and GH : Z = EF : GH, it follows that CD : X = GH : Z [5.11]; and since X : Y = CD : X and Z : W = GH : Z, it follows likewise that X : Y = Z : W [5.11].

**Step 6.** Thus there are two sets of magnitudes, AB, CD, X, Y and EF, GH, Z, W, equal in multitude, which taken two and two are in the same ratio; therefore, ex aequali, AB : Y = EF : W [5.22].

**Step 7.** But KA : LC = AB : Y (Step 3) and ME : NG = EF : W (Step 4); therefore KA : LC = ME : NG [5.11]. This proves the first part.

**Step 8.** Next let KA : LC = ME : NG; I say that AB : CD = EF : GH. Let O be a fourth proportional to the three straight lines AB, CD, EF, so that AB : CD = EF : O [6.12].

**Step 9.** On O describe the parallelepipedal solid PO similar and similarly situated to the solid ME, the side O corresponding to EF [11.27].

**Step 10.** Then KA, LC, ME, PO are similar and similarly described parallelepipedal solids on the straight lines AB, CD, EF, O, and AB : CD = EF : O; therefore, by the first part (Steps 2 to 7), KA : LC = ME : PO.

**Step 11.** But KA : LC = ME : NG by hypothesis; therefore ME : NG = ME : PO [5.11]. Thus the same solid ME has the same ratio to NG and to PO; therefore NG = PO [5.9].

**Step 12.** The faces of NG are similar to the corresponding faces of ME, and the faces of PO are similar to the same faces of ME; therefore the faces of NG are similar to the corresponding faces of PO [6.21]. Hence NG and PO are contained by similar planes equal in multitude, so they are similar solids [D11.9], and GH, O are corresponding sides of them, each corresponding to EF. Therefore NG has to PO the ratio triplicate of that which GH has to O [11.33].

**Step 13.** Let S be a third proportional to GH, O and T a third proportional to O, S [6.11], so that GH : O = O : S = S : T. Then GH has to T the ratio triplicate of that which GH has to O [D5.10]; hence, by Step 12, NG : PO = GH : T.

**Step 14.** Since NG = PO (Step 11), NG : PO = PO : PO [5.7]. Further, PO : PO = T : T; for if any equimultiples be taken of PO and of T according to one number, and any equimultiples of PO and of T according to another number, the former alike exceed, are alike equal to, or alike fall short of the latter [D5.5]. Therefore GH : T = NG : PO = PO : PO = T : T, so that GH : T = T : T [5.11]. Thus GH and T have the same ratio to T; therefore GH = T [5.9].

**Step 15.** Now GH is not greater than O. For if GH were greater than O, then, since GH : O = O : S and GH is greater than O, O would be greater than S; and since O : S = S : T and O is greater than S, S would be greater than T [5.14]; so that GH would be greater than O, O greater than S, and S greater than T, whence GH would be greater than T, which contradicts Step 14. Nor is GH less than O; for then in the same way O would be less than S and S less than T [5.14], so that GH would be less than T, again contradicting Step 14. Therefore GH = O.

**Step 16.** Since O = GH, EF : O = EF : GH [5.7]; and AB : CD = EF : O (Step 8); therefore AB : CD = EF : GH [5.11]. This proves the second part. Therefore, if four straight lines are proportional, the similar and similarly described parallelepipedal solids on them are proportional; and if the solids are proportional, the straight lines are proportional. Q.E.D.

**USED:** 11.27, 11.33, 5.11, 5.14, 5.22, 5.7, 5.9, 6.11, 6.12, 6.21, D11.9, D5.10, D5.5
**Human refs (from References field):** 11.33
**Jaccard:** 0.077 — AI adds ['11.27', '5.11', '5.14', '5.22', '5.7', '5.9', '6.11', '6.12', '6.21', 'D11.9', 'D5.10', 'D5.5']

## Proposition 11.38
**Statement:** If the sides of the opposite planes of a cube be bisected, and planes be carried through the points of section, the common section of the planes and the diameter of the cube bisect one another.

**Step 1.** Let the cube have the opposite faces ABCD and EFGH, with the four edges AE, BF, CG, DH joining corresponding vertices, so that its remaining faces are ABFE, BCGF, CDHG, DAEH. All six faces are equal squares [D11.25]; hence all the edges of the cube are equal, and in every face the opposite sides are equal and parallel. Let the sides of the face ABCD be bisected at K, L, M, N (K on AB, L on BC, M on CD, N on DA), and the sides of the opposite face EFGH at O, P, Q, R (O on EF, P on FG, Q on GH, R on HE). Through the points K, M, Q, O let the plane α be carried, and through L, N, R, P the plane β. Join AC and EG, and join AG, a diameter of the cube. I say that the common section of the planes α, β and the diameter AG bisect one another.

**Step 2.** The plane α and the plane of the face ABCD cut one another (α contains O, which is not in the face ABCD), so their common section is a straight line [11.3]; since K and M lie in both planes, this common section is the straight line KM. In the same way the common section of β with the face ABCD is LN, the common section of α with the face EFGH is OQ, and the common section of β with the face EFGH is PR. Hence every point of KM or of OQ lies in the plane α, and every point of LN or of PR lies in the plane β.

**Step 3.** Let KM meet AC at U. Since AB is parallel to CD and AC falls upon them, the alternate angles BAC, DCA are equal [1.29]; that is, the angle KAU is equal to the angle MCU. The angles AUK, CUM are vertical angles, hence equal [1.15]. And AK is equal to CM, these being halves of the equal sides AB, CD. Therefore the triangles AKU, CMU have two angles equal to two angles respectively and one side equal to one side, namely AK equal to CM, subtending the equal angles AUK, CUM; hence the remaining sides are equal to the remaining sides [1.26], so that AU is equal to UC. Thus U, which lies on KM and therefore in the plane α (Step 2), is the middle point of AC.

**Step 4.** Join NU and UL. AN is equal to CL, these being halves of the equal sides AD, BC; AU is equal to UC (Step 3); and, since AD is parallel to BC and AC falls upon them, the alternate angles DAC, BCA are equal [1.29], that is, the angle NAU is equal to the angle LCU. Therefore in the triangles NAU, LCU two sides are equal to two sides respectively and the included angles are equal; hence the angle AUN is equal to the angle CUL [1.4]. Now the straight line NU, standing on the straight line AC at U, makes the angles AUN, NUC together equal to two right angles [1.13]; therefore the angles NUC, CUL are together equal to two right angles, and so UN, UL, which lie on opposite sides of UC, are in a straight line with one another [1.14]. Thus U lies on LN, and therefore (Step 2) U lies in the plane β as well as in the plane α.

**Step 5.** In the same manner, if OQ meets EG at S, then ES is equal to SG [1.29, 1.15, 1.26 applied to the triangles EOS, GQS], and S lies on PR [1.29, 1.4, 1.13, 1.14 applied to the triangles RES, PGS]; so S is the middle point of EG and lies in both planes α and β.

**Step 6.** The planes α, β are distinct and have the point U in common, so they cut one another and their common section is a straight line [11.3]. The points U and S both lie in α and in β, and they are distinct, U being in the face ABCD and S in the opposite face EFGH; therefore the common section of the planes is the straight line US.

**Step 7.** AE is parallel to BF, these being opposite sides of the square ABFE, and BF is parallel to CG, these being opposite sides of the square BCGF; and AE, CG are not in the same plane with BF, since C is not in the plane of ABFE. Therefore AE is parallel to CG [11.9]. Also AE is equal to CG, both being edges of the cube. Now AC and EG join the extremities of the equal and parallel straight lines AE, CG towards the same parts; therefore AC is equal and parallel to EG [1.33].

**Step 8.** Since AC and EG are parallel, and U, A are points on AC while S, G are points on EG, the straight lines US and AG both lie in the plane of the parallels AC, EG [11.7]. Let AG and US meet at T. Since AC is parallel to EG and AG falls upon them, the alternate angles CAG, EGA are equal [1.29]; that is, the angle UAT is equal to the angle SGT. The angles ATU, GTS are vertical angles, hence equal [1.15]. And AU is equal to GS, these being halves of the equal straight lines AC, EG (Steps 3, 5, 7).

**Step 9.** Therefore the triangles AUT, GST have two angles equal to two angles respectively and one side equal to one side, namely AU equal to GS, subtending the equal angles ATU, GTS; hence the remaining sides are equal to the remaining sides [1.26]: AT is equal to TG, and UT is equal to TS.

**Step 10.** Therefore the common section US of the planes and the diameter AG of the cube bisect one another at the point T. Q.E.D.

**USED:** 1.13, 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.3, 11.7, 11.9, D11.25
**Human refs (from References field):** 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.9
**Jaccard:** 0.636 — AI adds ['1.13', '11.3', '11.7', 'D11.25']

## Proposition 11.39
**Statement:** If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms will be equal.

## Proposition 11.39
**Statement:** If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms will be equal.

**Step 1.** Let ABCDEF and GHKLMN be two prisms of equal height. Let the first stand on the parallelogram ABCD as base, its two opposite faces, which are equal, similar and parallel, being the triangles ADE and BCF, and its remaining faces being the parallelograms ABCD, ABFE, DCFE [D11.13]; thus EF is the edge opposite to the base ABCD, and the height of this prism is the perpendicular drawn from EF to the plane ABCD. Let the second stand on the triangle GHK as base, its opposite faces being the triangles GHK and LMN, and its remaining faces the parallelograms GHML, HKNM, GKNL [D11.13]; its height is the perpendicular drawn from the plane LMN to the plane GHK. Let these heights be equal, and let the parallelogram ABCD be double of the triangle GHK. I say that the prism ABCDEF is equal to the prism GHKLMN.

**Step 2.** Let the parallelepipedal solids be completed. Let the solid CP be completed on the base ABCD, having AP, BQ, CF, DE as its parallel edges, so that the triangles ADE, BCF are completed into the parallelograms ADEP, BCFQ, and the solid CP is contained by the six parallelograms ABCD, PQFE, ABQP, DCFE, ADEP, BCFQ, of which the opposite ones are parallel; its face PQFE opposite to the base lies in the plane through EF parallel to the plane ABCD. Likewise let the solid GT be completed, the triangle GHK being completed into the parallelogram GHSK, of which HK is a diameter, and the triangle LMN into the parallelogram LMTN, of which MN is a diameter, so that the solid GT is contained by the parallelograms GHSK, LMTN, GHML, HSTM, KSTN, GKNL, with GL, HM, ST, KN as its parallel edges; it stands on the base GHSK in the plane of GHK, and its opposite face LMTN lies in the plane of LMN.

**Step 3.** In the solid CP the faces ADEP and BCFQ are opposite planes, and AE, BF are their diagonals; the plane ABFE, which is a face of the first prism, passes through both of these diagonals. This plane divides the solid CP into two prisms, namely the prism ABCDEF, whose opposite faces are the triangles ADE, BCF, and the prism ABPQEF, whose opposite faces are the triangles APE, BQF. But a parallelepipedal solid cut by a plane through the diagonals of opposite planes is bisected by that plane [11.28]. Therefore the prism ABPQEF is equal to the prism ABCDEF, and the solid CP is double of the prism ABCDEF.

**Step 4.** Similarly, in the solid GT the faces GHSK and LMTN are opposite planes, with diagonals HK and MN, and the plane HKNM, a face of the second prism, passes through both. This plane divides the solid GT into the prism GHKLMN, whose opposite faces are the triangles GHK, LMN, and the prism HSKMTN, whose opposite faces are the triangles HSK, MTN; and these prisms are equal [11.28]. Therefore the solid GT is double of the prism GHKLMN.

**Step 5.** Since HK is a diameter of the parallelogram GHSK, it bisects the parallelogram [1.34]; therefore the parallelogram GHSK is double of the triangle GHK. But the parallelogram ABCD is also double of the triangle GHK, by hypothesis. Therefore the parallelogram ABCD is equal to the parallelogram GHSK [CN1].

**Step 6.** The solid CP stands on the base ABCD, and its opposite face PQFE lies in the plane through EF parallel to the base; hence the perpendicular from that face to the base ABCD is the perpendicular from EF to the plane ABCD, so that the solid CP has the same height as the prism ABCDEF. Likewise the solid GT has its base GHSK in the plane GHK and its opposite face LMTN in the plane LMN, so that it has the same height as the prism GHKLMN. But the prisms are of equal height; therefore the solids CP and GT are of the same height.

**Step 7.** Thus the parallelepipedal solids CP and GT are on the equal bases ABCD, GHSK and are of the same height. But parallelepipedal solids on equal bases and of the same height are equal to one another [11.31]. Therefore the solid CP is equal to the solid GT.

**Step 8.** Now the solid CP is double of the prism ABCDEF and the solid GT is double of the prism GHKLMN [Steps 3, 4], and the solids CP, GT are equal [Step 7]. I say that the prisms are equal. For suppose, if possible, that the prism ABCDEF is greater than the prism GHKLMN. Since the prism ABPQEF is equal to the prism ABCDEF and the prism HSKMTN is equal to the prism GHKLMN [Steps 3, 4], the prism ABPQEF is also greater than the prism HSKMTN. Then the prisms GHKLMN, HSKMTN are equal to parts of the prisms ABCDEF, ABPQEF respectively; and, these parts being added, the whole solid GT, which is made up of the prisms GHKLMN, HSKMTN, is equal to a part of the solid CP, which is made up of the prisms ABCDEF, ABPQEF [CN2]. Therefore the solid CP is greater than the solid GT [CN5]: which is impossible, since they are equal. In the same manner it is shown that the prism ABCDEF is not less than the prism GHKLMN. Therefore the prism ABCDEF is equal to the prism GHKLMN.

**Step 9.** Therefore, if there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms are equal. Q.E.D.

**USED:** D11.13, 11.28, 1.34, CN1, 11.31, CN2, CN5

**USED:** 1.34, 11.28, 11.31, CN1, CN2, CN5, D11.13
**Human refs (from References field):** 1.34, 11.28, 11.31
**Jaccard:** 0.429 — AI adds ['CN1', 'CN2', 'CN5', 'D11.13']
