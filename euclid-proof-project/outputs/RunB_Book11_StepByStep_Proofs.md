# Book 11 of Euclid's Elements — Step-by-Step AI Proofs (Run B)

## Proposition 11.1
**Statement:** A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 1.** Suppose, for the sake of contradiction, that a part of the straight line ABC lies in the plane of reference and a part in a plane more elevated. That is, suppose the segment AB lies in the reference plane, while the segment BC is elevated above it.

**Step 2.** Since AB is a finite straight line lying in the reference plane, produce AB continuously in a straight line to a point D, remaining within the reference plane [P2]. This is possible because the reference plane is a plane surface, which by definition lies evenly with the straight lines on itself [D1.7], so the straight line produced from AB within the plane remains in the plane. Thus ABD is a straight line lying entirely in the reference plane.

**Step 3.** Now consider the two lines: the original line ABC (which by hypothesis is a single straight line with AB in the reference plane and BC elevated) and the line ABD (which is a straight line lying entirely in the reference plane). Both ABC and ABD share the common segment AB.

**Step 4.** But a straight line lies evenly with the points on itself [D1.4]. This means that the continuation of a straight line from a given segment is uniquely determined: there is only one straight line continuation of AB beyond B. Since ABD is a straight line continuation of AB (produced by P2), and ABC is also claimed to be a straight line continuation of AB (by the original hypothesis), the portions BC and BD beyond B must coincide.

**Step 5.** However, BD lies entirely in the reference plane (by construction in Step 2), while BC is elevated above the reference plane (by hypothesis). Therefore BC and BD do not coincide, which contradicts the uniqueness established in Step 4.

**Step 6.** This contradiction shows that our initial supposition is impossible. Therefore, a part of a straight line cannot be in the plane of reference and a part in a plane more elevated. Q.E.D.

**USED:** D1.4, D1.7, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D1.4', 'D1.7', 'P2']

## Proposition 11.2
**Statement:** If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

**Step 1.** Let AB and CD be two straight lines cutting one another at the point E. We are to prove first that AB and CD lie in one plane, and second that every triangle lies in one plane.

**Step 2.** Consider any plane passing through the straight line AB. Since E is a point on AB, the point E lies in this plane. Since CD passes through E, part of CD (namely the point E and an adjacent segment) is in this plane.

**Step 3.** Suppose, for the sake of contradiction, that some part of CD lies outside the plane containing AB. Then part of the straight line CD would be in the plane of reference and part in a plane more elevated. But this contradicts Proposition 11.1, which states that a part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 4.** Therefore the whole of CD lies in the same plane as AB. Hence the two straight lines AB and CD, which cut one another at E, are in one plane.

**Step 5.** Now let ABC be any triangle. The sides BA and CA are two straight lines meeting at the point A (D1.19, since a triangle is a rectilineal figure contained by three straight lines).

**Step 6.** Since BA and CA cut one another at A, by what was just proved (Steps 2-4), the straight lines BA and CA lie in one plane. Call this plane S.

**Step 7.** The point B lies on line BA and the point C lies on line CA, so both B and C are in the plane S.

**Step 8.** Join B to C by a straight line BC (P1). Since B and C are both in plane S, part of the straight line BC is in plane S.

**Step 9.** If any part of BC were outside plane S, then part of the straight line BC would be in one plane and part in another, which again contradicts Proposition 11.1.

**Step 10.** Therefore the whole of BC lies in the plane S. Since all three sides AB, AC, and BC of triangle ABC lie in the plane S, the entire triangle ABC is in one plane.

**Step 11.** Therefore, if two straight lines cut one another, they are in one plane, and every triangle is in one plane. Q.E.D.

**USED:** 11.1, D1.19, P1
**Human refs (from References field):** 11.1
**Jaccard:** 0.333 — AI adds ['D1.19', 'P1']

## Proposition 11.3
**Statement:** If two planes cut one another, their common section is a straight line.

**Step 1.** Let two planes AB and BC cut one another, and let their common section be the line DB. We must prove that DB is a straight line.

**Step 2.** Suppose, for the sake of contradiction, that DB is not a straight line.

**Step 3.** Since D and B are two points lying in the plane AB, draw the straight line DEB from D to B within the plane AB [P1]. By the definition of a plane surface, this straight line DEB lies entirely in the plane AB [D1.7].

**Step 4.** Similarly, since D and B are two points lying in the plane BC, draw the straight line DFB from D to B within the plane BC [P1]. By the definition of a plane surface, this straight line DFB lies entirely in the plane BC [D1.7].

**Step 5.** Since DEB lies entirely in plane AB and DFB lies entirely in plane BC, and these are distinct planes that cut one another, the straight lines DEB and DFB are distinct (for if they coincided, that single straight line would lie in both planes, yet by our supposition the common section DB is not straight, so the straight lines from D to B cannot coincide with DB).

**Step 6.** But then two distinct straight lines DEB and DFB have the same endpoints D and B and thus enclose a space between them. This is impossible, since two straight lines cannot enclose a space [P1].

**Step 7.** Therefore the supposition is false, and DB, the common section of the two planes, must be a straight line. Q.E.D.

**USED:** D1.7, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D1.7', 'P1']

## Proposition 11.4
**Statement:** If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

**Step 1.** Let the straight line EF be set up at right angles to two straight lines AB and CD, which cut one another at the point E. We must prove that EF is at right angles to the plane through AB and CD. [Setup from hypothesis; D11.3]

**Step 2.** Cut off EA, EB, EC, ED all equal to one another from the four segments of AB and CD at E, using Proposition 1.3. [1.3]

**Step 3.** Through E, draw any straight line GH in the plane through AB and CD, by Postulate P1. [P1]

**Step 4.** Join the straight lines AD and CB by Postulate P1. [P1]

**Step 5.** Join FA, FG, FD, FC, FH, and FB by Postulate P1. [P1]

**Step 6.** Since EA equals EB and ED equals EC (by construction in Step 2), and the angle AED equals the angle BEC (for they are vertical angles by Proposition 1.15), triangle AED is congruent to triangle BEC by Proposition 1.4. Therefore AD equals BC and angle DAE equals angle EBC. [1.15, 1.4, CN1]

**Step 7.** Since the angle AEG equals the angle BEH (for they are vertical angles by Proposition 1.15), and EA equals EB (by construction), and angle DAE equals angle EBC (from Step 6), it follows by considering triangles AEG and BEH that angle AGE equals angle BHE and EG equals EH by Proposition 1.26 (AAS congruence: angle GAE equals angle HBE, angle AEG equals angle BEH, and EA equals EB). Also AG equals BH. [1.15, 1.26]

**Step 8.** Since EA equals EB, and EF is common, and the angle AEF is a right angle and the angle BEF is a right angle (by hypothesis), the angle AEF equals the angle BEF by Postulate P4. Therefore triangle AEF is congruent to triangle BEF by Proposition 1.4. Hence FA equals FB. [P4, 1.4]

**Step 9.** Since ED equals EC, and EF is common, and the angle DEF is a right angle and the angle CEF is a right angle (by hypothesis), the angle DEF equals the angle CEF by Postulate P4. Therefore triangle DEF is congruent to triangle CEF by Proposition 1.4. Hence FD equals FC. [P4, 1.4]

**Step 10.** Now in triangles FAD and FBC: AD equals BC (from Step 6), FA equals FB (from Step 8), and FD equals FC (from Step 9). Therefore triangle FAD is congruent to triangle FBC by Proposition 1.8. Hence the angle FAD equals the angle FBC. [1.8]

**Step 11.** Now in triangles FAG and FBH: FA equals FB (from Step 8), AG equals BH (from Step 7), and the angle FAG equals the angle FBH (from Step 10). Therefore triangle FAG is congruent to triangle FBH by Proposition 1.4. Hence FG equals FH. [1.4]

**Step 12.** Since EG equals EH (from Step 7), EF is common, and FG equals FH (from Step 11), triangle FEG is congruent to triangle FEH by Proposition 1.8. Hence the angle FEG equals the angle FEH. [1.8]

**Step 13.** Since the angle FEG equals the angle FEH, and these are adjacent angles formed by EF standing on GH, and they are equal to one another, each of them is a right angle by Definition D1.10. Therefore EF is at right angles to GH. [D1.10]

**Step 14.** Since GH was drawn as an arbitrary straight line through E in the plane through AB and CD, EF makes right angles with every straight line which meets it and lies in that plane. Therefore, by Definition D11.3, EF is at right angles to the plane through AB and CD. [D11.3]

**USED:** 1.15, 1.26, 1.3, 1.4, 1.8, CN1, D1.10, D11.3, P1, P4
**Human refs (from References field):** 1.15, 1.26, 1.4, 1.8, D11.3
**Jaccard:** 0.500 — AI adds ['1.3', 'CN1', 'D1.10', 'P1', 'P4']

## Proposition 11.5
**Statement:** If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

**Step 1.** Let the straight line XA be set up at right angles to the three straight lines AB, AC, AD at their common point of section A. We must prove that AB, AC, AD are in one plane.

**Step 2.** Since XA is at right angles to both AB and AC, and AB and AC are two straight lines which cut one another at A, by 11.4, XA is at right angles to the plane through AB and AC. Call this plane P.

**Step 3.** Suppose, for the sake of contradiction, that AD is not in plane P.

**Step 4.** Consider the plane Q determined by XA and AD. Since plane Q and plane P are two distinct planes that both pass through the point A, and XA lies in Q but not entirely in P (since XA is perpendicular to P), these two planes cut one another. By 11.3, their common section is a straight line. Let this common section be the straight line AE, which lies in both planes P and Q.

**Step 5.** Since XA is at right angles to plane P (Step 2), by D11.3, XA makes right angles with every straight line which meets it and lies in plane P. Since AE lies in plane P and meets XA at A, the angle XAE is a right angle.

**Step 6.** By hypothesis, XA is set up at right angles to AD, so the angle XAD is a right angle.

**Step 7.** Since all right angles are equal to one another (P4), angle XAE equals angle XAD.

**Step 8.** Now AE and AD both lie in plane Q (AE is the intersection of P and Q, hence in Q; AD is in Q by construction), and both pass through A. Since AD is not in plane P (by our assumption in Step 3) but AE is in plane P (Step 4), the lines AD and AE are distinct.

**Step 9.** Since AE and AD are distinct lines from A lying in the same plane Q, and both lie on the same side of XA (neither coincides with XA, as XA is perpendicular to P while AE lies in P, and XA is perpendicular to AD), the angle XAE is a proper part of angle XAD, or angle XAD is a proper part of angle XAE. In either case, one of these angles is the whole and the other is a part of it.

**Step 10.** But by Step 7, angle XAE equals angle XAD. This means the whole equals the part, which contradicts CN5, since the whole is greater than the part.

**Step 11.** Therefore, the assumption in Step 3 is false, and AD must lie in plane P, the plane through AB and AC.

**Step 12.** Hence the three straight lines AB, AC, AD are all in one plane, which is what was to be proved.

**USED:** 11.3, 11.4, CN5, D11.3, P4
**Human refs (from References field):** 11.3, 11.4, D11.3
**Jaccard:** 0.600 — AI adds ['CN5', 'P4']

## Proposition 11.6
**Statement:** If two straight lines be at right angles to the same plane, the straight lines will be parallel.

**Step 1.** Let AB and CD be two straight lines at right angles to the same plane P, meeting the plane at points B and D respectively. We are to prove that AB and CD are parallel.

**Step 2.** Join BD [P1]. Since B and D are both in plane P, the line BD lies in plane P.

**Step 3.** Since AB is at right angles to plane P, it makes right angles with all straight lines which meet it and are in the plane [D11.3]. In particular, since BD is in plane P and meets AB at B, the angle ABD is a right angle.

**Step 4.** Similarly, since CD is at right angles to plane P, and BD is in plane P and meets CD at D, the angle CDB is a right angle [D11.3].

**Step 5.** In plane P, at point D, draw DE at right angles to BD [1.11]. Then DE lies in plane P and the angle BDE is a right angle.

**Step 6.** Join BE and AE [P1]. Since B and E are both in plane P, the line BE lies in plane P. Since BE is in plane P and meets AB at B, the angle ABE is a right angle [D11.3]. Since DE is in plane P and meets CD at D, the angle CDE is a right angle [D11.3].

**Step 7.** In the right triangle ABD, where the angle at B is right, by the Pythagorean theorem, AD squared equals AB squared plus BD squared [1.47].

**Step 8.** In the right triangle BDE, where the angle at D is right, by the Pythagorean theorem, BE squared equals BD squared plus DE squared [1.47].

**Step 9.** In the right triangle ABE, where the angle at B is right, by the Pythagorean theorem, AE squared equals AB squared plus BE squared [1.47].

**Step 10.** Substituting from Step 8 into Step 9, AE squared equals AB squared plus BD squared plus DE squared [CN2]. Since AB squared plus BD squared equals AD squared from Step 7, we have AE squared equals AD squared plus DE squared [CN1].

**Step 11.** Since AE squared equals AD squared plus DE squared, by the converse of the Pythagorean theorem, the angle ADE is a right angle [1.48].

**Step 12.** Now, DE is at right angles to three straight lines at their common point D: it is at right angles to BD (by construction in Step 5), at right angles to AD (proved in Step 11), and at right angles to CD (established in Step 6). The lines BD, AD, and CD meet one another at D.

**Step 13.** Since the straight line DE is set up at right angles to the three straight lines BD, AD, and CD which meet one another at their common point of section D, the three straight lines BD, AD, and CD are in one plane [11.5]. Call this plane Q.

**Step 14.** Since BD and AD lie in plane Q, and A lies on line AB while B is an endpoint of BD, the line AB lies in plane Q. Since CD lies in plane Q (from Step 13), both AB and CD lie in the same plane Q.

**Step 15.** In plane Q, the straight line BD falls on the two straight lines AB and CD. The angle ABD and the angle BDC are alternate angles. Both angle ABD and angle BDC are right angles (Steps 3 and 4). Since all right angles are equal to one another [P4], the alternate angles ABD and BDC are equal.

**Step 16.** Since the straight line BD falling on the two straight lines AB and CD makes the alternate angles equal to one another, AB is parallel to CD [1.27].

Therefore, if two straight lines are at right angles to the same plane, the straight lines are parallel. Q.E.D.

**USED:** 1.11, 1.27, 1.47, 1.48, 11.5, CN1, CN2, D11.3, P1, P4
**Human refs (from References field):** 1.28, 1.4, 1.8, 11.2, 11.5, D11.3
**Jaccard:** 0.143 — AI adds ['1.11', '1.27', '1.47', '1.48', 'CN1', 'CN2', 'P1', 'P4']; Human adds ['1.28', '1.4', '1.8', '11.2']

## Proposition 11.7
**Statement:** If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

**Step 1.** Let AB and CD be two parallel straight lines, and let E be a point taken at random on AB and F a point taken at random on CD. Join EF [P1]. We must show that EF is in the same plane as AB and CD.

**Step 2.** Since AB and CD are parallel, by definition they are in the same plane [D1.23]. Call this plane P. Since E lies on AB, the point E is in plane P. Since F lies on CD, the point F is in plane P.

**Step 3.** Let G be any point on the segment EF between E and F. We claim G is also in plane P. Suppose, for the sake of contradiction, that G is not in plane P.

**Step 4.** Since E is on AB and G is not in plane P, draw the straight line EG [P1]. Since E is in plane P and G is not, the line EG is not entirely in plane P. Similarly, draw the straight line GF [P1]. Since F is in plane P and G is not, GF is not entirely in plane P.

**Step 5.** Now consider triangle EGF. However, EG and GF together compose the line EF, and G lies on EF, so E, G, F are collinear and do not form a triangle. We therefore adjust the argument. Take a point H on AB distinct from E, so that E and H are two distinct points on AB.

**Step 6.** Consider the triangle EHF (with vertices E and H on AB, and F on CD). This is a genuine triangle since F is not on line AB (for if F were on AB, then since F is on CD, the lines AB and CD would meet, contradicting that they are parallel). By Proposition 11.2, every triangle is in one plane. Therefore triangle EHF lies in some plane Q.

**Step 7.** The side EH of triangle EHF is a segment of line AB. Since EH lies in plane Q, and a part of a straight line cannot be in one plane and the rest in a plane more elevated [11.1], the entire line AB lies in plane Q.

**Step 8.** The vertex F of triangle EHF lies in plane Q. The side EF of triangle EHF lies in plane Q. Thus EF is in plane Q.

**Step 9.** We now show that CD also lies in plane Q. The point F is on CD and in plane Q. Take a point K on CD distinct from F. Consider triangle EFK (with E on AB and F, K on CD). Since K is a point on CD which is parallel to AB, and E is on AB, triangle EFK is a genuine triangle (K is not on line AB, by the same argument as in Step 6). By 11.2, triangle EFK lies in one plane.

**Step 10.** The vertex E of triangle EFK is in plane Q (since E is on AB which lies in Q by Step 7). The vertex F is in plane Q (shown in Step 8). The side EF lies in plane Q (Step 8). Now the plane of triangle EFK contains E and F, and the plane Q also contains E and F. Since two distinct points determine a unique line, and three non-collinear points determine a unique plane, and E, F, K are non-collinear (K is not on line EF since otherwise K would be in the plane determined by triangle EHF, and being on CD... we need a more direct argument).

**Step 11.** We simplify. From Steps 6-8, the plane Q contains line AB and point F and line EF. Since H and E are distinct points on AB in plane Q, and F is in plane Q but not on AB, the three non-collinear points H, E, F determine plane Q uniquely. Now the point K is on CD. Since AB is parallel to CD, both lie in plane P [D1.23]. But plane P also contains H, E (on AB) and F (on CD). Since H, E, F are non-collinear and determine a unique plane, plane P and plane Q are the same plane.

**Step 12.** Therefore AB, CD, and EF all lie in the single plane P (which equals Q). Since E and F were arbitrary points on AB and CD respectively, the straight line EF joining them is in the same plane as the parallel straight lines AB and CD. Q.E.D.

**USED:** 11.1, 11.2, D1.23, P1
**Human refs (from References field):** 11.3
**Jaccard:** 0.000 — AI adds ['11.1', '11.2', 'D1.23', 'P1']; Human adds ['11.3']

## Proposition 11.8
**Statement:** If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

**Step 1.** Let AB and CD be two parallel straight lines, and let AB be at right angles to plane P. Let B be the point where AB meets plane P, and let D be the point where CD meets plane P. We are to show that CD is also at right angles to plane P.

**Step 2.** Since AB is at right angles to plane P, AB makes right angles with all straight lines which meet it and are in plane P (D11.3). In particular, since BD is a straight line through B in plane P, angle ABD is a right angle.

**Step 3.** Since AB and CD are parallel, by 11.7 the straight line BD joining a point on AB to a point on CD lies in the same plane as AB and CD. Call this plane Q. Thus A, B, D, and C all lie in plane Q.

**Step 4.** In plane Q, AB is parallel to CD and BD is a transversal cutting them. By 1.29, the alternate angles ABD and CDB are equal. Since angle ABD is a right angle (Step 2), angle CDB is also a right angle. Therefore CD is at right angles to BD.

**Step 5.** In plane P, at the point D, draw DE at right angles to BD (1.11), so that DE is a straight line through D in plane P perpendicular to BD.

**Step 6.** Join BE (P1). Since BE is a straight line through B lying in plane P, and AB is at right angles to plane P, angle ABE is a right angle (D11.3).

**Step 7.** In the right triangle ABE (right angle at B), by 1.47: the square on AE equals the sum of the squares on AB and BE.

**Step 8.** In the right triangle BDE (right angle at D, since DE was drawn perpendicular to BD in Step 5), by 1.47: the square on BE equals the sum of the squares on BD and DE.

**Step 9.** Substituting the result of Step 8 into Step 7: the square on AE equals the sum of the squares on AB, BD, and DE.

**Step 10.** In the right triangle ABD (right angle at B, from Step 2), by 1.47: the square on AD equals the sum of the squares on AB and BD.

**Step 11.** From Steps 9 and 10: the square on AE equals the sum of the square on AD and the square on DE.

**Step 12.** Since the square on AE equals the sum of the squares on AD and DE, by 1.48 (the converse of the Pythagorean theorem), the angle ADE is a right angle. Therefore AD is at right angles to DE at D.

**Step 13.** We now have two straight lines, BD and AD, both passing through D, such that DE is at right angles to each of them (BD perpendicular to DE by construction in Step 5, and AD perpendicular to DE by Step 12). Since BD and AD cut one another at D (they are distinct lines, as A is not on line BD because angle ABD is a right angle), by 11.4, DE is at right angles to the plane through BD and AD.

**Step 14.** The plane through BD and AD is the plane through the three non-collinear points A, B, D, which is plane Q (since A, B, D are in plane Q by Step 3, and three non-collinear points determine a unique plane). Therefore DE is at right angles to plane Q.

**Step 15.** Since CD lies in plane Q and passes through D (Step 3), and DE is at right angles to plane Q at D (Step 14), DE is at right angles to CD (D11.3).

**Step 16.** We have now shown that CD is at right angles to two straight lines lying in plane P that meet at D: namely BD (Step 4) and DE (Step 15). Since BD and DE cut one another at D (they are distinct lines meeting at D, being perpendicular to each other by construction), by 11.4, CD is at right angles to the plane through BD and DE, which is plane P.

**Step 17.** Therefore, if two straight lines are parallel and one of them is at right angles to any plane, the remaining one is also at right angles to the same plane. Q.E.D.

**USED:** 1.11, 1.29, 1.47, 1.48, 11.4, 11.7, D11.3, P1
**Human refs (from References field):** 1.29, 11.2, 11.4, 11.7, D11.3
**Jaccard:** 0.444 — AI adds ['1.11', '1.47', '1.48', 'P1']; Human adds ['11.2']

## Proposition 11.9
**Statement:** Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

**Step 1.** Let AB and CD each be parallel to the straight line EF, where AB and CD are not in the same plane as EF. We are to prove that AB is parallel to CD.

**Step 2.** Let some point G be taken on EF.

**Step 3.** From G, in the plane containing AB and EF, draw GH at right angles to EF [1.11]. Similarly, from G, in the plane containing CD and EF, draw GK at right angles to EF [1.11].

**Step 4.** Since EF is at right angles to GH (by construction) and EF is at right angles to GK (by construction), and GH and GK meet EF at the common point G, it follows that EF is at right angles to the plane through GH and GK [11.4].

**Step 5.** Now AB is parallel to EF (given), and EF has been shown to be at right angles to the plane through GH and GK. Therefore AB is also at right angles to the plane through GH and GK [11.8].

**Step 6.** Similarly, CD is parallel to EF (given), and EF is at right angles to the plane through GH and GK. Therefore CD is also at right angles to the plane through GH and GK [11.8].

**Step 7.** Thus both AB and CD are at right angles to the same plane, namely the plane through GH and GK. Therefore AB is parallel to CD [11.6].

**Step 8.** Therefore, straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another. Q.E.D.

**USED:** 1.11, 11.4, 11.6, 11.8
**Human refs (from References field):** 11.4, 11.6, 11.8
**Jaccard:** 0.750 — AI adds ['1.11']

## Proposition 11.10
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.

**Step 1.** Let AB, BC be two straight lines meeting at B, and let DE, EF be two straight lines meeting at E, such that AB is parallel to DE and BC is parallel to EF, with these pairs not in the same plane. We must show that angle ABC equals angle DEF.

**Step 2.** On BA, cut off BG equal to ED, and on BC, cut off BH equal to EF. (This is possible by 1.3, since we may set BA = ED and BC = EF by relabeling; for clarity we work directly with BA = ED and BC = EF.)

**Step 3.** Join AD, BE, and CF by P1. Since BA is parallel to ED (given) and BA = ED (by construction in Step 2), the straight lines joining their extremities in the same direction, namely BE and AD, are equal and parallel, by 1.33. Thus BE = AD and BE is parallel to AD.

**Step 4.** Similarly, since BC is parallel to EF (given) and BC = EF (by construction in Step 2), the straight lines joining their extremities in the same direction, namely BE and CF, are equal and parallel, by 1.33. Thus BE = CF and BE is parallel to CF.

**Step 5.** From Steps 3 and 4, AD = BE and CF = BE. Therefore AD = CF, by CN1.

**Step 6.** From Steps 3 and 4, AD is parallel to BE and CF is parallel to BE. Now AD and CF are not in the same plane as BE (since AB, BC are not in the same plane as DE, EF). Therefore AD is parallel to CF, by 11.9 (straight lines parallel to the same straight line and not in the same plane with it are parallel to one another).

**Step 7.** Since AD is parallel to CF (Step 6) and AD = CF (Step 5), the straight lines joining their extremities in the same direction, namely AC and DF, are equal and parallel, by 1.33. In particular, AC = DF.

**Step 8.** Now in triangles ABC and DEF, we have AB = DE, BC = EF (by construction), and AC = DF (Step 7). Therefore triangle ABC is congruent to triangle DEF, and in particular angle ABC equals angle DEF, by 1.8 (the SSS congruence theorem).

**Step 9.** Therefore, if two straight lines meeting one another are parallel to two straight lines meeting one another not in the same plane, they contain equal angles. Q.E.D.

**USED:** 1.3, 1.33, 1.8, 11.9, CN1, P1
**Human refs (from References field):** 1.33, 1.8, 11.9
**Jaccard:** 0.500 — AI adds ['1.3', 'CN1', 'P1']

## Proposition 11.11
**Statement:** From a given elevated point to draw a straight line perpendicular to a given plane.

**Step 1.** Let A be the given elevated point, and let the given plane be the reference plane. We are required to draw from A a straight line perpendicular to the given plane.

**Step 2.** Draw any straight line BC in the given plane [P1].

**Step 3.** From the point A, draw AD perpendicular to BC, meeting BC at D [1.12]. Then AD is at right angles to BC.

**Step 4.** If AD is already at right angles to the given plane, then what was required is done. If not, proceed as follows.

**Step 5.** From the point D, in the given plane, draw DE at right angles to BC [1.11].

**Step 6.** From the point A, draw AF perpendicular to DE, meeting DE at F [1.12]. Then AF is at right angles to DE.

**Step 7.** Through the point F, in the given plane, draw GH parallel to BC [1.31].

**Step 8.** Now, since BC is at right angles to DA (by Step 3) and BC is at right angles to DE (by Step 5, since DE was drawn at right angles to BC at D), and DA and DE are two straight lines meeting at D, it follows that BC is at right angles to the plane through DA and DE [11.4].

**Step 9.** Since GH is parallel to BC (by Step 7), and BC is at right angles to the plane through DA and DE (by Step 8), therefore GH is also at right angles to the plane through DA and DE [11.8].

**Step 10.** Since GH is at right angles to the plane through DA and DE, GH makes right angles with every straight line which meets it and is in that plane [D11.3]. Now AF lies in the plane through DA and DE (since F is on DE and A determines the line DA which is in that plane), and AF meets GH at F. Therefore GH is at right angles to FA, and hence FA is at right angles to GH.

**Step 11.** But AF is also at right angles to DE (by Step 6). Therefore AF is at right angles to each of the two straight lines GH and DE at the point of section F.

**Step 12.** Now GH and DE are two straight lines that meet at F and lie in the given plane. Since AF is at right angles to both GH and DE at their point of intersection F, AF is at right angles to the given plane [11.4].

**Step 13.** Therefore, from the given elevated point A, the straight line AF has been drawn perpendicular to the given plane, which is what was required to be done.

**USED:** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3, P1
**Human refs (from References field):** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3
**Jaccard:** 0.857 — AI adds ['P1']

## Proposition 11.12
**Statement:** To set up a straight line at right angles to a given plane from a given point in it.

**Step 1.** Let A be the given point in the given plane. We must construct a straight line through A that is at right angles to the plane (D11.3).

**Step 2.** Let B be any point not in the given plane, that is, a point elevated above it. Such a point exists since we are working in solid geometry.

**Step 3.** From the elevated point B, draw BC perpendicular to the given plane, where C is the foot of the perpendicular in the plane (11.11).

**Step 4.** Through the point A, draw the straight line AD parallel to BC (1.31). This is possible since A is a given point and BC is a given straight line not passing through A (for if A coincided with C, then BC itself would already be the required perpendicular at A, and we would be done).

**Step 5.** Now BC is at right angles to the given plane (by construction in Step 3), and AD is parallel to BC (by construction in Step 4). Therefore, by 11.8, AD is also at right angles to the given plane.

**Step 6.** Therefore AD has been set up from the point A at right angles to the given plane, which is what was required (D11.3).

**USED:** 1.31, 11.11, 11.8, D11.3
**Human refs (from References field):** 1.31, 11.11, 11.8
**Jaccard:** 0.750 — AI adds ['D11.3']

## Proposition 11.13
**Statement:** From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

**Step 1.** Suppose, for the sake of contradiction, that from the same point A two distinct straight lines AB and AC are set up at right angles to the same plane P on the same side.

**Step 2.** Since AB and AC both pass through the point A and are distinct, they determine a plane, and they lie in one plane together with any lines joining points on them [11.2]. Let the plane through AB and AC cut the plane P. Their common section is a straight line [11.3]; call it DE, so that A lies on line DE in plane P.

**Step 3.** Since AB is at right angles to plane P, by definition AB makes right angles with all straight lines which meet it and are in the plane P [D11.3]. In particular, since DE lies in plane P and meets AB at A, the angle BAE is a right angle.

**Step 4.** Since AC is at right angles to plane P, by the same definition [D11.3], AC makes right angles with all straight lines which meet it and are in the plane P. In particular, since DE lies in plane P and meets AC at A, the angle CAE is a right angle.

**Step 5.** Now the angles BAE and CAE are both right angles, and therefore angle BAE equals angle CAE [P4].

**Step 6.** But AB and AC are distinct straight lines on the same side of plane P, both lying in the plane through AB and AC. In this plane, they both proceed from A on the same side of line DE. Therefore angle BAE is the whole and angle CAE is a part of it (or vice versa), so the whole equals the part.

**Step 7.** This contradicts Common Notion 5, which states that the whole is greater than the part [CN5].

**Step 8.** Therefore the supposition is false, and from the same point two straight lines cannot be set up at right angles to the same plane on the same side. Q.E.D.

**USED:** 11.2, 11.3, CN5, D11.3, P4
**Human refs (from References field):** 11.3, D11.3
**Jaccard:** 0.400 — AI adds ['11.2', 'CN5', 'P4']

## Proposition 11.14
**Statement:** Planes to which the same straight line is at right angles will be parallel.

**Step 1.** Let the straight line AB be at right angles to each of the planes P and Q, where A is the foot of the perpendicular in plane P and B is the foot in plane Q. We are to prove that P and Q are parallel.

**Step 2.** Suppose, for the sake of contradiction, that the planes P and Q are not parallel. Then they meet [negation of D11.8].

**Step 3.** Since the two planes meet, their common section is a straight line; call it GH [11.3].

**Step 4.** Let K be any point on the line GH [the common section lies in both planes, so K lies in both P and Q].

**Step 5.** Join A to K and B to K [P1]. Since K lies in plane P (as GH is in the common section and hence in P), the line AK lies in plane P. Similarly, since K lies in plane Q, the line BK lies in plane Q.

**Step 6.** Since AB is at right angles to the plane P, it makes right angles with all straight lines which meet it and lie in plane P [D11.3]. The line AK meets AB at A and lies in plane P, so angle BAK is a right angle.

**Step 7.** Since AB is at right angles to the plane Q, it makes right angles with all straight lines which meet it and lie in plane Q [D11.3]. The line BK meets AB at B and lies in plane Q, so angle ABK is a right angle.

**Step 8.** Now in triangle ABK, the two angles BAK and ABK are both right angles. Therefore the sum of angles BAK and ABK equals two right angles.

**Step 9.** But in any triangle, the sum of any two angles is less than two right angles [1.17]. This contradicts Step 8.

**Step 10.** Therefore the assumption in Step 2 is false, and the planes P and Q do not meet. Hence, by definition, P and Q are parallel [D11.8].

**USED:** 1.17, 11.3, D11.3, D11.8, P1
**Human refs (from References field):** 1.17, 11.3, D11.3, D11.8
**Jaccard:** 0.800 — AI adds ['P1']

## Proposition 11.15
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

**Step 1.** Let AB and BC be two straight lines meeting one another at B, and let DE and EF be two straight lines meeting one another at E, such that AB is parallel to DE and BC is parallel to EF, and these pairs are not in the same plane. Let the plane through AB, BC be called plane P, and the plane through DE, EF be called plane Q. We must show that P and Q are parallel, that is, they do not meet.

**Step 2.** From B, draw BG perpendicular to plane Q. [11.11] Let G be the foot of the perpendicular in plane Q.

**Step 3.** Through G in plane Q, draw GH parallel to ED, and draw GK parallel to EF. [1.31]

**Step 4.** Since BG is at right angles to plane Q, BG makes right angles with all straight lines which meet it and lie in plane Q. [D11.3] Therefore angle BGH is a right angle and angle BGK is a right angle.

**Step 5.** Now AB is parallel to DE (given), and GH is parallel to DE (by construction). Since AB and GH are each parallel to DE and are not in the same plane with it, AB is parallel to GH. [11.9]

**Step 6.** Since AB is parallel to GH, and BG is a transversal meeting them both, and angle BGH is a right angle, the alternate interior angle ABG is also a right angle. [1.29]

**Step 7.** Similarly, BC is parallel to EF (given), and GK is parallel to EF (by construction). Since BC and GK are each parallel to EF and are not in the same plane with it, BC is parallel to GK. [11.9]

**Step 8.** Since BC is parallel to GK, and BG is a transversal meeting them both, and angle BGK is a right angle, the alternate interior angle CBG is also a right angle. [1.29]

**Step 9.** Since BG is at right angles to both AB and BC, which are two straight lines meeting one another at B lying in plane P, BG is at right angles to plane P. [11.4]

**Step 10.** But BG is also at right angles to plane Q (by construction in Step 2). Therefore the same straight line BG is at right angles to both plane P and plane Q.

**Step 11.** Since planes P and Q both have the same straight line BG at right angles to them, plane P is parallel to plane Q. [11.14]

**Step 12.** Therefore, if two straight lines meeting one another are parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel. Q.E.D.

**USED:** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Human refs (from References field):** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Jaccard:** 1.000 — Perfect match.

## Proposition 11.16
**Statement:** If two parallel planes be cut by any plane, their common sections are parallel.

**Step 1.** Let planes P and Q be parallel (that is, they do not meet, by D11.8), and let a third plane R cut both of them. Let the common section of R and P be the line EF, and let the common section of R and Q be the line GH. We must show that EF is parallel to GH.

**Step 2.** Since plane R cuts plane P, their common section EF is a straight line [11.3]. Likewise, since plane R cuts plane Q, their common section GH is a straight line [11.3].

**Step 3.** The straight lines EF and GH both lie in the plane R, since each is a common section involving plane R.

**Step 4.** Suppose, for the sake of contradiction, that EF and GH are not parallel. Then, since they are straight lines in the same plane, they will meet at some point K when produced [D1.23, taken contrapositively: if they do not meet the definition of parallel, they must meet].

**Step 5.** Since K lies on EF, and EF is the common section of planes R and P, the point K lies in plane P. Since K lies on GH, and GH is the common section of planes R and Q, the point K lies in plane Q.

**Step 6.** Therefore planes P and Q have the point K in common, which means they meet. But this contradicts the hypothesis that P and Q are parallel, since parallel planes are those which do not meet [D11.8].

**Step 7.** Therefore the supposition is false, and EF and GH do not meet. Since EF and GH are straight lines lying in the same plane R and do not meet, they are parallel by definition [D1.23].

**Step 8.** Therefore, if two parallel planes be cut by any plane, their common sections are parallel. Q.E.D.

**USED:** 11.3, D1.23, D11.8
**Human refs (from References field):** 11.1, D1.23
**Jaccard:** 0.250 — AI adds ['11.3', 'D11.8']; Human adds ['11.1']

## Proposition 11.17
**Statement:** If two straight lines be cut by parallel planes, they will be cut in the same ratios.

**Step 1.** Let AB and CD be two straight lines cut by three parallel planes, where the first plane passes through A and C, the second (middle) plane passes through E and F, and the third plane passes through B and D; so that A, E, B are successive points on the first line and C, F, D are successive points on the second line. We are to prove that AE : EB = CF : FD.

**Step 2.** Join AC and BD by straight lines [P1]. Join AD by a straight line [P1]. Let AD meet the middle plane at a point G.

**Step 3.** Consider the plane containing triangle ABD. This plane is cut by the first parallel plane (which contains A) and by the middle parallel plane (which contains E and G). Since the first and middle planes are parallel, their common sections with the plane of triangle ABD are parallel [11.16]. The first plane meets the plane of triangle ABD along a line through A, and the middle plane meets the plane of triangle ABD along the line EG. Therefore EG is parallel to BD.

**Step 4.** In triangle ABD, since EG is parallel to BD and cuts side AB at E and side AD at G, by Proposition 6.2 the sides are cut proportionally: AE : EB = AG : GD.

**Step 5.** Now consider the plane containing triangle ACD. This plane is cut by the first parallel plane (which contains A and C) and by the middle parallel plane (which contains F and G). Since the first and middle planes are parallel, their common sections with the plane of triangle ACD are parallel [11.16]. The first plane meets the plane of triangle ACD along the line AC, and the middle plane meets the plane of triangle ACD along the line FG. Therefore FG is parallel to AC.

**Step 6.** In triangle ACD, since FG is parallel to AC and cuts side CD at F and side AD at G (measuring from vertex D), by Proposition 6.2 the sides are cut proportionally: DF : FC = DG : GA.

**Step 7.** Since DF : FC = DG : GA, by the definition of inverse ratio and the definition of same ratio, the inverse proportion also holds: CF : FD = AG : GD [D5.5, D5.13].

**Step 8.** From Step 4 we have AE : EB = AG : GD, and from Step 7 we have CF : FD = AG : GD. Since AE : EB and CF : FD are both the same ratio as AG : GD, they are the same ratio as one another [5.11]. Therefore AE : EB = CF : FD.

**Step 9.** Therefore, if two straight lines be cut by parallel planes, they will be cut in the same ratios. Q.E.D.

**USED:** 11.16, 5.11, 6.2, D5.13, D5.5, P1
**Human refs (from References field):** 11.16, 5.11, 6.2
**Jaccard:** 0.500 — AI adds ['D5.13', 'D5.5', 'P1']

## Proposition 11.18
**Statement:** If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

**Step 1.** Let the straight line AB be at right angles to the reference plane P, meeting P at the point A. Let Q be any plane passing through AB. We must show that Q is at right angles to P.

**Step 2.** Since both planes P and Q exist and intersect (they share at least the point A), by 11.3 their common section is a straight line. Call this common section CD.

**Step 3.** Since A is the point where AB meets plane P, A lies in plane P. And since AB lies in plane Q, A also lies in plane Q. Therefore A lies on the common section CD.

**Step 4.** Since AB is at right angles to plane P, by D11.3, AB makes right angles with every straight line which meets it and lies in plane P. Since CD lies in plane P and meets AB at A, the angle BAC (taking C as any point on CD on one side of A) is a right angle. That is, AB is perpendicular to CD at A.

**Step 5.** Let F be any point on CD other than A. In the plane Q, by 1.11, draw FG at right angles to CD at the point F, so that FG lies in plane Q.

**Step 6.** Now consider the straight line CD falling on the two straight lines AB and FG (both lying in plane Q). At A, the angle between CD and AB is a right angle (Step 4). At F, the angle between CD and FG is a right angle (Step 5). Therefore the interior angles on the same side at A and F are together equal to two right angles. By 1.28, AB is parallel to FG.

**Step 7.** Since AB is at right angles to plane P, and FG is parallel to AB, by 11.8, FG is also at right angles to plane P.

**Step 8.** Now FG is a straight line drawn in the plane Q, at right angles to the common section CD of the planes P and Q (Step 5), and FG is at right angles to the plane P (Step 7). Therefore, by D11.4, the plane Q is at right angles to the plane P.

**Step 9.** Since Q was taken as an arbitrary plane through AB, it follows that every plane through the straight line AB is at right angles to the plane P. This is what was to be proved.

**USED:** 1.11, 1.28, 11.3, 11.8, D11.3, D11.4
**Human refs (from References field):** 1.11, 1.28, 11.8, D11.3, D11.4
**Jaccard:** 0.833 — AI adds ['11.3']

## Proposition 11.19
**Statement:** If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

**Step 1.** Let the two planes AB and BC be each at right angles to a reference plane P, and let them cut one another. By 11.3, their common section is a straight line; call it BD.

**Step 2.** Suppose, for contradiction, that BD is not at right angles to the plane P.

**Step 3.** Let the plane AB meet P in the straight line DE, and let the plane BC meet P in the straight line FG; let B be a point on BD that lies on the plane P (where the common section BD meets P). By 11.3, DE and FG are each straight lines.

**Step 4.** From the point B, in the plane AB, draw BH at right angles to DE (by 1.11). Since the plane AB is at right angles to the plane P, and BH has been drawn in the plane AB at right angles to DE (their common section), BH is at right angles to the plane P (by D11.4).

**Step 5.** Similarly, from B, in the plane BC, draw BK at right angles to FG (by 1.11). Since the plane BC is at right angles to the plane P, and BK has been drawn in the plane BC at right angles to FG (their common section), BK is at right angles to the plane P (by D11.4).

**Step 6.** Thus from the point B, two straight lines BH and BK have been set up at right angles to the plane P on the same side. But this is impossible by 11.13.

**Step 7.** Therefore BH and BK must be one and the same straight line. But BH lies in the plane AB, and BK lies in the plane BC. Since this single line lies in both planes, it is their common section BD.

**Step 8.** Therefore BD is at right angles to the plane P. That is, the common section of the two planes is at right angles to the reference plane. Q.E.D.

**USED:** 1.11, 11.13, 11.3, D11.4
**Human refs (from References field):** 11.13, D11.4
**Jaccard:** 0.500 — AI adds ['1.11', '11.3']

## Proposition 11.20
**Statement:** If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

**Step 1.** Let the solid angle at A be contained by the three plane angles BAC, CAD, and DAB. We must show that any two of these, taken together, are greater than the remaining one.

**Step 2.** If the three plane angles are all equal, the result is immediate, since the sum of any two equals twice one of them, which is greater than the remaining one. If one of the three angles is less than or equal to each of the other two, then even a single one of the other two is greater than or equal to it, so the sum of two certainly exceeds the third. The only non-trivial case is when one angle is strictly greater than at least one of the others. Without loss of generality, suppose angle BAC is not less than each of the other two, that is, angle BAC is the greatest (or tied for greatest). We shall prove that angle DAB + angle CAD > angle BAC.

**Step 3.** In the plane containing angle BAC, construct angle BAE equal to angle DAB, with E on the same side of AB as C [by 1.23]. On the ray AE, cut off AE equal to AD [by 1.3].

**Step 4.** Draw a straight line through E meeting AB at some point B and AC at some point C, so that B lies on AB and C lies on AC with E between B and C [by P1]. Join DB and DC [by P1].

**Step 5.** In triangles DAB and EAB: AD = AE [by construction in Step 3], AB is common, and angle DAB = angle BAE [by construction in Step 3]. Therefore triangle DAB is congruent to triangle EAB, and in particular DB = EB [by 1.4].

**Step 6.** In triangle BDC, the two sides BD and DC are together greater than the remaining side BC [by 1.20]. Since BD = BE [from Step 5], we obtain BE + DC > BC. But BC = BE + EC [since E is between B and C, by CN2]. Therefore DC > EC [by CN5 and the common notion that if a + b > a + c then b > c, i.e., CN3 applied after subtracting BE from both sides].

**Step 7.** Now consider triangles DAC and EAC. We have AD = AE [by construction], AC is common to both, and DC > EC [from Step 6]. Therefore angle DAC > angle EAC [by 1.25].

**Step 8.** Since angle DAB = angle BAE [by construction], adding angle DAC to the left side and angle EAC to the right side of this equality, and using that angle DAC > angle EAC [from Step 7], we obtain angle DAB + angle DAC > angle BAE + angle EAC [by CN2 and the fact that adding a greater quantity to one side of an equality yields a strict inequality].

**Step 9.** But angle BAE + angle EAC = angle BAC [since E lies within angle BAC, so the angles are adjacent and sum to the whole]. Therefore angle DAB + angle CAD > angle BAC.

**Step 10.** Since angle BAC was taken as the greatest of the three plane angles, and we have shown that the sum of the other two exceeds it, the result holds for every choice of the remaining angle. Therefore, if a solid angle is contained by three plane angles, any two taken together are greater than the remaining one. Q.E.D.

**USED:** 1.20, 1.23, 1.25, 1.3, 1.4, CN2, CN3, CN5, P1
**Human refs (from References field):** 1.20, 1.25, 1.4
**Jaccard:** 0.333 — AI adds ['1.23', '1.3', 'CN2', 'CN3', 'CN5', 'P1']

## Proposition 11.21
**Statement:** Any solid angle is contained by plane angles less than four right angles.

**Step 1.** Let the solid angle at vertex A be contained by the plane angles BAC, CAD, DAE, EAF, and FAB (we take five face angles for generality; the argument works for any number greater than two). By D11.11, these plane angles are not all in the same plane and meet at A.

**Step 2.** Let the plane angles at A be cut by a plane, so that the straight lines AB, AC, AD, AE, AF meet this plane at points B, C, D, E, F respectively. The sections form the convex polygon BCDEF lying in this cutting plane. By P1, join consecutive intersection points to form the sides BC, CD, DE, EF, FB of the polygon.

**Step 3.** Let O be a point taken inside the polygon BCDEF. By P1, join O to each vertex B, C, D, E, F. This produces five triangles with vertex O: OBC, OCD, ODE, OEF, OFB. Likewise, the lines from A to the polygon vertices determine five triangles with vertex A: ABC, ACD, ADE, AEF, AFB.

**Step 4.** Since both sets contain the same number of triangles (five in each set), and by 1.32 the three angles of any triangle sum to two right angles, the sum of all angles in the five A-triangles equals ten right angles, and the sum of all angles in the five O-triangles also equals ten right angles.

**Step 5.** Consider any vertex of the polygon, say B. The point A is not in the plane of the polygon (since the face angles at A are not coplanar), so the lines BA, BF, BC form a solid angle at B. The three face angles of this solid angle are ABF, ABC, and FBC. By 11.20, angles ABF and ABC together are greater than angle FBC.

**Step 6.** But since O lies inside the polygon, the point O lies inside angle FBC, so angle FBC equals angle FBO plus angle OBC. Therefore angles ABF and ABC together are greater than angles FBO and OBC together.

**Step 7.** The same reasoning applies at each vertex of the polygon. At C: angles BCA + ACD > BCO + OCD. At D: angles CDA + ADE > CDO + ODE. At E: angles DEA + AEF > DEO + OEF. At F: angles EFA + FAB > EFO + OFB. Therefore, summing over all five polygon vertices, the total of the base angles of the A-triangles is greater than the total of the base angles of the O-triangles.

**Step 8.** Now from Step 4, in the A-triangles the sum of all angles is: (the face angles at A) + (the base angles of the A-triangles) = ten right angles. In the O-triangles the sum of all angles is: (the angles at O) + (the base angles of the O-triangles) = ten right angles.

**Step 9.** The angles at O, namely BOC, COD, DOE, EOF, FOB, are arranged around the point O and together constitute the full angle around O. By 1.13, two supplementary angles on a line equal two right angles, and by 1.15, vertical angles are equal. Applying these around point O, the angles around O sum to four right angles.

**Step 10.** From Step 8, the face angles at A equal ten right angles minus the base angles of the A-triangles, and the angles at O equal ten right angles minus the base angles of the O-triangles. Since by Step 7 the base angles of the A-triangles are greater than the base angles of the O-triangles, it follows by CN5 that ten right angles minus the base angles of the A-triangles is less than ten right angles minus the base angles of the O-triangles.

**Step 11.** That is, the sum of the face angles at A is less than the sum of the angles at O, which by Step 9 equals four right angles. Therefore the solid angle at A is contained by plane angles whose sum is less than four right angles, which was to be proved.

**USED:** 1.13, 1.15, 1.32, 11.20, CN5, D11.11, P1
**Human refs (from References field):** 1.32, 11.20
**Jaccard:** 0.286 — AI adds ['1.13', '1.15', 'CN5', 'D11.11', 'P1']

## Proposition 11.22
**Statement:** If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

**Step 1.** Let the three plane angles be angle BAC, angle EDF, and angle GHK, where any two taken together are greater than the remaining one. Let them be contained by equal straight lines, so that AB = AC = DE = DF = GH = HK. Join BC, EF, and GK. We must show that a triangle can be constructed from BC, EF, and GK.

**Step 2.** By Proposition 1.22, it suffices to show that any two of BC, EF, GK taken together are greater than the remaining one, i.e., BC + EF > GK, BC + GK > EF, and EF + GK > BC.

**Step 3.** Without loss of generality, assume angle GHK is not less than each of angle BAC and angle EDF. (If not, relabel the angles so this holds.)

**Step 4.** Since angle GHK is not less than angle BAC, and in triangles BAC and GHK we have GH = AB and HK = AC, by Proposition 1.24 (or 1.25 for the equal case), GK is not less than BC.

**Step 5.** Since angle GHK is not less than angle EDF, and in triangles EDF and GHK we have GH = DE and HK = DF, by Proposition 1.24 (or 1.25 for the equal case), GK is not less than EF.

**Step 6.** From Step 4, GK is not less than BC, so EF + GK > EF >= 0, but more precisely, since GK is not less than BC, we have EF + GK >= EF + 0, but we need EF + GK > BC. Since GK is not less than BC, EF + GK >= BC + EF > BC (as EF is a straight line of positive length). In fact, since GK >= BC, it follows immediately that EF + GK >= EF + BC > BC. But what we need is EF + GK > BC. Since EF is a line segment joining two distinct points (as angle EDF is a proper angle), EF > 0, and GK >= BC, so EF + GK > GK >= BC. Thus EF + GK > BC.

**Step 7.** Similarly from Step 5, GK >= EF, so BC + GK > GK >= EF, giving BC + GK > EF.

**Step 8.** It remains to prove the critical inequality: BC + EF > GK. At the point H, on the line HG, construct the angle GHL equal to angle BAC using Proposition 1.23, and cut off HL equal to AB (which equals GH = HK) by Proposition 1.3.

**Step 9.** In triangles GHL and BAC: GH = AB, HL = AC (both equal to the common length), and angle GHL = angle BAC (by construction). Therefore by Proposition 1.4 (SAS), triangle GHL is congruent to triangle BAC, and so GL = BC.

**Step 10.** Since angle GHL = angle BAC and angle GHK = angle GHL + angle LHK, we have angle LHK = angle GHK - angle BAC. By hypothesis, angle BAC + angle EDF > angle GHK. Therefore angle EDF > angle GHK - angle BAC = angle LHK.

**Step 11.** In triangles LHK and EDF: HL = DE (both equal to the common length) and HK = DF (both equal to the common length), and angle EDF > angle LHK (from Step 10). Therefore by Proposition 1.24 (the greater angle has the greater opposite side), EF > LK.

**Step 12.** In triangle GLK, by Proposition 1.20, GL + LK > GK.

**Step 13.** From Step 11, EF > LK, so GL + EF > GL + LK. Combined with Step 12, GL + EF > GL + LK > GK. That is, GL + EF > GK.

**Step 14.** From Step 9, GL = BC. Substituting, BC + EF > GK.

**Step 15.** We have now established all three inequalities: BC + EF > GK (Step 14), BC + GK > EF (Step 7), and EF + GK > BC (Step 6). Therefore by Proposition 1.22, a triangle can be constructed out of three straight lines equal to BC, EF, and GK.

**Step 16.** Therefore, if there are three plane angles of which two taken together in any manner are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines. Q.E.F.

**USED:** 1.20, 1.22, 1.23, 1.24, 1.3, 1.4, P1
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 0.286 — AI adds ['1.20', '1.22', '1.23', '1.3', 'P1']

## Proposition 11.23
**Statement:** To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

**Step 1.** Let the three given plane angles be ABC, DEF, and GHK, where any two taken together are greater than the remaining one, and the sum of all three is less than four right angles. We are to construct a solid angle contained by these three plane angles.

**Step 2.** From the sides of the angles, cut off equal segments: let AB = BC = DE = EF = GH = HK [by P3 and 1.3]. Join AC, DF, GK [by P1].

**Step 3.** Since any two of the three angles ABC, DEF, GHK are together greater than the remaining one, and the equal straight lines AB, BC, DE, EF, GH, HK contain these angles, by 11.22 it is possible to construct a triangle out of AC, DF, GK. Let triangle LMN be so constructed, with LM = AC, MN = DF, NL = GK [by 11.22].

**Step 4.** Circumscribe circle LMN about triangle LMN [by 4.5]. Let its center be O.

**Step 5.** We show that O falls within the triangle LMN. Since the sum of angles ABC, DEF, GHK is less than four right angles, we consider: if O were on a side or outside the triangle, then the angles subtended at O would yield a configuration in which the three plane angles sum to four right angles or more, contradicting the hypothesis. More precisely, construct on LM, MN, NL (considered as bases) isosceles triangles LPM, MQN, NRL with equal legs equal to AB (so LP = PM = AB, MQ = QN = DE, NR = RL = GH). Then angle LPM = angle ABC, angle MQN = angle DEF, angle NRL = angle GHK [by 1.8, since the triangles are congruent to the original angle-containing triangles by SSS].

**Step 6.** If O were on side LM of triangle LMN, then since O lies on the circle and NL, NM are chords, consider the angles at P, Q, R. The angles LPM + MQN + NRL would equal the sum of angles in triangles formed at the boundary, which forces the sum to equal four right angles (as the angles at the center on one side of a line sum to two right angles by 1.13). But the three angles sum to less than four right angles, so O does not lie on any side.

**Step 7.** If O were outside triangle LMN, similar reasoning using 1.21 (an exterior angle of a triangle is greater than either remote interior angle) and the properties of angles inscribed versus central angles would show that the three plane angles sum to more than or equal to four right angles, again contradicting the hypothesis. Therefore O lies within triangle LMN.

**Step 8.** From O, set up a perpendicular OS to the plane of circle LMN [by 11.12].

**Step 9.** Since O is the center of the circle, OL = OM = ON [by D1.15]. Now we need to find the height OS. We have AB^2 = OL^2 + OS^2 must hold so that the constructed segments from S have the right length. Since AB > OL (because O is inside the triangle and OL is merely a radius, while AB is the leg of the isosceles triangle whose base is a chord), the square on AB is greater than the square on OL [by 1.19 applied in the configuration, and the fact that the whole is greater than the part, CN5]. So AB^2 - OL^2 is a positive quantity. Let OS be such that OS^2 = AB^2 - OL^2 [by 1.47 applied inversely: given the difference of squares, we can construct such a length].

**Step 10.** More precisely, since the square on AB is greater than the square on OL, cut off from AB a segment equal to OL, and by 1.47 and 2.14, construct a straight line OS such that the square on OS equals the excess of the square on AB over the square on OL. Set OS perpendicular to the plane of the circle at O [by 11.12].

**Step 11.** Join SL, SM, SN [by P1].

**Step 12.** Since OS is at right angles to the plane of the circle, angle SOL, angle SOM, and angle SON are each right angles [by D11.3]. Therefore in right triangle SOL: SL^2 = OS^2 + OL^2 = (AB^2 - OL^2) + OL^2 = AB^2, so SL = AB [by 1.47 and CN1]. Similarly SM = AB and SN = AB.

**Step 13.** Now in triangle SLM: SL = AB, SM = AB (= BC), and LM = AC. But in triangle ABC: AB, BC are the sides and AC is the base. Since SL = AB, SM = BC, LM = AC, triangle SLM is congruent to triangle ABC [by 1.8, SSS]. Therefore angle LSM = angle ABC.

**Step 14.** Similarly, in triangle SMN: SM = DE, SN = EF, MN = DF. So triangle SMN is congruent to triangle DEF [by 1.8]. Therefore angle MSN = angle DEF.

**Step 15.** Similarly, in triangle SNL: SN = GH, SL = HK, NL = GK. So triangle SNL is congruent to triangle GHK [by 1.8]. Therefore angle NSL = angle GHK.

**Step 16.** Therefore the solid angle at S is contained by the three plane angles LSM, MSN, NSL, which are respectively equal to the given angles ABC, DEF, GHK. The solid angle at S has been constructed out of the three given plane angles. Q.E.F.

**USED:** 1.13, 1.21, 1.3, 1.47, 1.8, 11.12, 11.22, 2.14, 4.5, CN1, CN5, D1.15, D11.3, P1, P3
**Human refs (from References field):** 1.25, 1.29, 1.4, 1.47, 1.8, 11.12, 11.22, 5.16, 6.2, 6.4
**Jaccard:** 0.190 — AI adds ['1.13', '1.21', '1.3', '2.14', '4.5', 'CN1', 'CN5', 'D1.15', 'D11.3', 'P1', 'P3']; Human adds ['1.25', '1.29', '1.4', '5.16', '6.2', '6.4']

## Proposition 11.24
**Statement:** If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

**Step 1.** Let the solid ABCDEFGH be contained by parallel planes. Specifically, let the three pairs of opposite parallel planes be: ABCD parallel to EFGH, ABFE parallel to DCGH, and ADHE parallel to BCGF.

**Step 2.** Since the two parallel planes ABFE and DCGH are cut by the plane ABCD, their common sections AB and DC are parallel [11.16]. Since the two parallel planes ADHE and BCGF are cut by the plane ABCD, their common sections AD and BC are parallel [11.16]. Therefore ABCD is a parallelogram, since both pairs of opposite sides are parallel.

**Step 3.** Similarly, since the parallel planes ABFE and DCGH are cut by the plane EFGH, the common sections EF and HG are parallel [11.16]. Since the parallel planes ADHE and BCGF are cut by the plane EFGH, the common sections EH and FG are parallel [11.16]. Therefore EFGH is a parallelogram.

**Step 4.** Since the parallel planes ABCD and EFGH are cut by the plane ABFE, the common sections AB and EF are parallel [11.16]. Since the parallel planes ADHE and BCGF are cut by the plane ABFE, the common sections AE and BF are parallel [11.16]. Therefore ABFE is a parallelogram.

**Step 5.** Since the parallel planes ABCD and EFGH are cut by the plane DCGH, the common sections DC and HG are parallel [11.16]. Since the parallel planes ADHE and BCGF are cut by the plane DCGH, the common sections DH and CG are parallel [11.16]. Therefore DCGH is a parallelogram.

**Step 6.** Since the parallel planes ABCD and EFGH are cut by the plane ADHE, the common sections AD and EH are parallel [11.16]. Since the parallel planes ABFE and DCGH are cut by the plane ADHE, the common sections AE and DH are parallel [11.16]. Therefore ADHE is a parallelogram.

**Step 7.** Since the parallel planes ABCD and EFGH are cut by the plane BCGF, the common sections BC and FG are parallel [11.16]. Since the parallel planes ABFE and DCGH are cut by the plane BCGF, the common sections BF and CG are parallel [11.16]. Therefore BCGF is a parallelogram.

**Step 8.** Thus every face of the solid is parallelogrammic. It remains to show that opposite faces are equal.

**Step 9.** Consider the opposite faces ABCD and EFGH. Since ABFE is a parallelogram, AB equals EF [1.34]. Since ADHE is a parallelogram, AD equals EH [1.34].

**Step 10.** Now AB is parallel to EF (Step 4), and AD is parallel to EH (Step 6). These two pairs of lines meet one another at A and at E respectively, and they are not in the same plane. Therefore by 11.10, angle DAB equals angle HEF.

**Step 11.** Since in the two triangles DAB and HEF, AD equals EH, AB equals EF, and the included angle DAB equals angle HEF, the two triangles are equal in all respects [1.4]. In particular, DB equals HF, and angle ABD equals angle EFH.

**Step 12.** Since in parallelogram ABCD, AB equals DC and AD equals BC [1.34], and in parallelogram EFGH, EF equals HG and EH equals FG [1.34], and since AB equals EF and AD equals EH, it follows that DC equals HG and BC equals FG.

**Step 13.** Now consider triangles BCD and FGH. We have BC equals FG (Step 12), DC equals HG (Step 12). Also, BA is parallel to EF (Step 4), and BC is parallel to FG (Step 7). Since BA and BC meet at B, and EF and FG meet at F, and these are not in the same plane, angle ABC equals angle EFG [11.10]. But in parallelogram ABCD, angle ABC equals angle ADC [1.34], and in parallelogram EFGH, angle EFG equals angle EHG [1.34]. Since angle ABC equals angle EFG, we also have angle BCD equals angle FGH, because in each parallelogram adjacent angles are supplementary [1.29], and since angle ABC equals angle EFG, the supplements angle BCD and angle FGH are also equal.

**Step 14.** Thus in triangles BCD and FGH, BC equals FG, DC equals HG, and the included angle BCD equals angle FGH. Therefore the two triangles are equal in all respects [1.4].

**Step 15.** Since parallelogram ABCD is composed of triangles ABD and BCD, and parallelogram EFGH is composed of triangles EFH and FGH, and triangle ABD equals triangle EFH (Step 11) and triangle BCD equals triangle FGH (Step 14), the parallelogram ABCD equals the parallelogram EFGH [CN2].

**Step 16.** By an analogous argument for the opposite faces ABFE and DCGH: since ABCD is a parallelogram, AB equals DC [1.34]; since ADHE is a parallelogram, AE equals DH [1.34]. Also AB is parallel to DC (Step 2) and AE is parallel to DH (Step 6). Since AB and AE meet at A, and DC and DH meet at D, and these are not in the same plane, angle BAE equals angle CDH [11.10]. In triangles BAE and CDH, AB equals DC, AE equals DH, and angle BAE equals angle CDH, so the triangles are equal [1.4], giving BE equals CH. Since BCGF is a parallelogram, BF equals CG [1.34], and since ABFE is a parallelogram, AB equals EF [1.34], thus BF equals CG and EF equals HG (from EFGH). By an argument parallel to Steps 13-14, we establish that angle ABF equals angle DCG [11.10] and that the remaining triangles composing the faces are equal [1.4]. Therefore parallelogram ABFE equals parallelogram DCGH [CN2].

**Step 17.** By the same reasoning for the opposite faces ADHE and BCGF: since ABCD is a parallelogram, AD equals BC [1.34]; since ABFE is a parallelogram, AE equals BF [1.34]. Also AD is parallel to BC (Step 2) and AE is parallel to BF (Step 4). Since AD and AE meet at A, and BC and BF meet at B, and these are not in the same plane, angle DAE equals angle CBF [11.10]. In triangles DAE and CBF, AD equals BC, AE equals BF, and angle DAE equals angle CBF, so the triangles are equal [1.4]. Continuing as before, we establish through 11.10 and 1.4 that the second pair of component triangles are also equal. Therefore parallelogram ADHE equals parallelogram BCGF [CN2].

**Step 18.** Therefore, if a solid be contained by parallel planes, each face is a parallelogram, and the opposite faces are equal. Q.E.F.

**USED:** 1.29, 1.34, 1.4, 11.10, 11.16, CN2
**Human refs (from References field):** 1.34, 1.4, 11.10, 11.16
**Jaccard:** 0.667 — AI adds ['1.29', 'CN2']

## Proposition 11.25
**Statement:** If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.

**Step 1.** Let the parallelepipedal solid ABCDEFGH (with face ABCD opposite to face EFGH, face ABFE opposite to face DCGH, and face ADHE opposite to face BCGF) be cut by the plane KLMN parallel to the opposite faces ABCD and EFGH. This cutting plane divides the solid into two parallelepipedal solids: solid I with base ABCD and top face KLMN, and solid II with base KLMN and top face EFGH. We must show that as base ABCD is to base KLMN, so is solid I to solid II.

**Step 2.** Since the plane KLMN is parallel to the planes ABCD and EFGH, and the planes ABFE and DCGH cut these parallel planes, the common sections are parallel. That is, KL is parallel to AB and NM is parallel to DC, and similarly KN is parallel to AD and LM is parallel to BC, by 11.16. Hence KLMN is a parallelogram, as are all faces of both solids I and II. By 11.24, the opposite faces of each resulting solid are equal and parallelogrammic, confirming that both solids I and II are parallelepipedal.

**Step 3.** Consider the edge AE (a lateral edge of the original parallelepiped). The plane KLMN meets this edge at K, dividing it into AK and KE. Since ABFE is a parallelogram, AB is parallel to EF and AE is parallel to BF. The lateral edges of solid I (AK, BL, CM, DN) are all equal and parallel, and similarly the lateral edges of solid II (KE, LF, MG, NH) are all equal and parallel, by 11.24 and 1.34 applied to the parallelogrammic faces.

**Step 4.** Now produce the edge AD to points O, P, Q, ... beyond D, and mark off segments equal to AD as many times as needed; similarly produce BC correspondingly. That is, let AO = AD and AP = AO + AD = 2·AD, and so on, using 1.3 to cut off equal lengths and P1 to draw the corresponding lines.

**Step 5.** Through each division point on the produced line, draw planes parallel to the face ADHE (and its opposite BCGF) by extending the parallelepiped structure. Each such plane, together with the original top and bottom faces, creates a new parallelepipedal solid with a base equal in shape to ABCD and the same lateral edges as the original solid.

**Step 6.** Consider the parallelepipeds constructed on bases ABCD and ABCD' (where D' is the next adjacent copy). These solids have equal bases, since each base is a parallelogram with one pair of sides equal to AB and the other pair equal to AD, and the bases are congruent by 1.34 and 1.4. The lateral edges of all these parallelepipeds are equal (all equal to AK for solid I, or KE for solid II). The faces are determined by 11.24, and the solids are positioned so that corresponding faces coincide or are congruent. By CN4, each adjacent parallelepiped with base equal to ABCD and the same height AK is equal to solid I.

**Step 7.** Similarly, construct multiples of the base KLMN along the same direction. Each parallelepiped with base equal to KLMN and height KE is equal to solid II, by the same reasoning.

**Step 8.** Now take any equimultiple of solid I (which corresponds to taking the same multiple of base ABCD by concatenating equal copies along the direction AD) and any equimultiple of solid II (corresponding to the same multiple of base KLMN). The multiple of solid I is a parallelepiped whose base is the corresponding multiple of ABCD, and the multiple of solid II is a parallelepiped whose base is the corresponding multiple of KLMN, with the respective heights preserved.

**Step 9.** By 6.1, parallelograms under the same height are to one another as their bases. The bases ABCD and KLMN are parallelograms (by Step 2 and 11.24). The equimultiples of these bases are also parallelograms.

**Step 10.** Now we verify the equimultiple criterion of D5.5. Take arbitrary positive integers m and n. Form the solid consisting of m copies of solid I stacked along the base direction; its base is m times ABCD. Form the solid consisting of n copies of solid II stacked similarly; its base is n times KLMN. Each m-fold solid I is assembled from m equal parallelepipeds (Step 6), so the m-fold solid equals m times solid I. Similarly the n-fold solid equals n times solid II.

**Step 11.** The m-fold solid exceeds, equals, or falls short of the n-fold solid precisely when the base of the m-fold solid (which is m times base ABCD) exceeds, equals, or falls short of the base of the n-fold solid (which is n times base KLMN). This correspondence holds because parallelepipeds with the same height whose bases are equal are themselves equal, and a parallelepiped with a greater base (same height) contains one with a lesser base, so is greater by CN5.

**Step 12.** Since for all positive integers m and n, the m-fold of base ABCD exceeds, equals, or falls short of the n-fold of base KLMN precisely when the m-fold of solid I exceeds, equals, or falls short of the n-fold of solid II, we conclude by D5.5 that base ABCD is to base KLMN as solid I is to solid II.

**Step 13.** Therefore, if a parallelepipedal solid be cut by a plane parallel to the opposite planes, then as the base is to the base, so is the solid to the solid. Q.E.F.

**USED:** 1.3, 1.34, 1.4, 11.16, 11.24, 6.1, CN4, CN5, D11.1, D11.2, D11.8, D5.5, P1
**Human refs (from References field):** 11.24, D5.5
**Jaccard:** 0.154 — AI adds ['1.3', '1.34', '1.4', '11.16', '6.1', 'CN4', 'CN5', 'D11.1', 'D11.2', 'D11.8', 'P1']

## Proposition 11.26
**Statement:** On a given straight line, and at a given point on it, to construct a solid angle equal to a given solid angle.

**Step 1.** Let the given solid angle be at D, contained by the three plane angles EDC, EDF, and FDC, with edges DC, DE, and DF. Let AB be the given straight line, and let A be the given point on it. We shall construct at A a solid angle equal to the solid angle at D. [D11.11]

**Step 2.** On DE take an arbitrary point E. From E, draw EG perpendicular to the plane through D, F, C (the plane of angle FDC), and let G be the foot of this perpendicular in that plane. [11.11]

**Step 3.** In the plane DFC, from G draw GH perpendicular to DC, meeting DC at H; and from G draw GK perpendicular to DF, meeting DF at K. Join DG, EH, and EK. [1.12, P1]

**Step 4.** We prove that angle EHD is a right angle. Since EG is perpendicular to the plane DFC, the plane through E, G, H (which contains EG) is perpendicular to the plane DFC. [11.18] The common section of these two planes is the line GH. Now DC lies in the plane DFC and is perpendicular to GH (by construction of Step 3). Since the plane EGH is at right angles to the plane DFC, and DC is drawn in the plane DFC at right angles to their common section GH, it follows that DC is at right angles to the plane EGH. [D11.4] Therefore DC is at right angles to EH, which lies in the plane EGH and passes through H. [D11.3] Hence angle EHD is a right angle.

**Step 5.** By the identical argument (replacing DC with DF and H with K throughout), angle EKD is a right angle. The plane through E, G, K contains EG, hence is perpendicular to the plane DFC [11.18]; DF is perpendicular to GK (by construction) in the plane DFC; therefore DF is perpendicular to the plane EGK [D11.4]; therefore DF is perpendicular to EK [D11.3]; hence angle EKD is a right angle.

**Step 6.** Also, since EG is perpendicular to the plane DFC, and GH and GK both lie in that plane, we have angle EGH = 90 and angle EGK = 90. [D11.3]

**Step 7.** Now begin the construction at A. At point A on line AB, in a plane through AB, construct angle BAL equal to angle CDF. [1.23] The ray AL corresponds to DF, and the ray AB corresponds to DC, so that angle BAL plays the role of angle CDF.

**Step 8.** On ray AL, cut off AH' equal to DH. [1.3] At H', in the plane BAL, erect H'P perpendicular to the line AL (that is, perpendicular to AH'). [1.11] On this perpendicular, cut off H'P equal to HG. [1.3] Join AP. [P1]

**Step 9.** In the right triangles AH'P and DHG: AH' = DH, H'P = HG, and the included angles at H' and H are both right angles. By SAS congruence, triangle AH'P is congruent to triangle DHG. [1.4] Therefore AP = DG, and angle H'AP = angle HDG.

**Step 10.** We show that the perpendicular distance from P to the ray AM (where AM is the extension along AB from A) is correctly placed. Since angle BAL = angle CDF (Step 7), and angle H'AP = angle HDG (Step 9), and H' lies on ray AL, we have angle BAP = angle BAL - angle H'AP... but let us instead argue directly. The angle PAL = angle H'AP = angle GDC (since H is on ray DC and angle HDG = angle CDG). Therefore angle PAB = angle LAB - angle LAP = angle CDF - angle CDG = angle GDF (using the fact that G lies in the interior of angle CDF, so angle CDF = angle CDG + angle GDF). [CN1]

**Step 11.** Now drop a perpendicular from P to line AB, meeting AB at K'. In the right triangle APK': angle PAK' = angle PAB = angle GDF (Step 10), and angle AK'P = 90. In the right triangle DGK: angle GDK = angle GDF, and angle DKG = 90. Since AP = DG (Step 9), the triangles APK' and DGK are congruent by AAS (two angles and the hypotenuse). [1.26] Therefore AK' = DK and K'P = KG.

**Step 12.** From P, erect the line PE' perpendicular to the plane BAL. [11.12] On PE' cut off PE' equal to GE. [1.3] Join AE', H'E', and K'E'. [P1]

**Step 13.** We prove angle E'AH' = angle EDH (i.e., the face angle E'AL = angle EDC). In the right triangles E'PH' and EGH: PE' = GE, PH' = GH (= H'P by construction), and the included angles at P and G are both right angles (PE' is perpendicular to the plane, PH' is in the plane, so angle E'PH' = 90; likewise angle EGH = 90 by Step 6). [D11.3] By SAS, triangle E'PH' is congruent to triangle EGH. [1.4] Hence E'H' = EH.

**Step 14.** We prove that angle E'H'A is a right angle. Since PE' is perpendicular to the plane BAL, the plane through E', P, H' (containing PE') is perpendicular to the plane BAL. [11.18] The common section of these planes is PH'. Line AL lies in the plane BAL and is perpendicular to PH' (because H' is on AL and PH' is perpendicular to AL by construction in Step 8). Therefore AL is at right angles to the plane E'PH'. [D11.4] Hence AL is perpendicular to E'H'. [D11.3] Since H' lies on AL, angle E'H'A is a right angle.

**Step 15.** Now in the right triangles E'H'A and EHD: AH' = DH (construction), H'E' = HE (Step 13), and the included angles at H' and H are both right angles (Step 14 and Step 4). By SAS, triangle E'H'A is congruent to triangle EHD. [1.4] Therefore AE' = DE and angle E'AH' = angle EDH. Since H' is on ray AL from A and H is on ray DC from D, we have angle E'AL = angle EDC.

**Step 16.** We prove angle E'AK' = angle EDK (i.e., the face angle E'AB = angle EDC... let us be precise). In the right triangles E'PK' and EGK: PE' = GE, PK' = GK (Step 11), and the included angles at P and G are both right angles (PE' perp to plane, PK' in plane gives angle E'PK' = 90; EG perp to plane, GK in plane gives angle EGK = 90). [D11.3] By SAS, triangle E'PK' is congruent to triangle EGK. [1.4] Hence E'K' = EK.

**Step 17.** We prove that angle E'K'A is a right angle. Since PE' is perpendicular to the plane BAL, the plane through E', P, K' contains PE' and is perpendicular to the plane BAL. [11.18] The common section of these planes is PK'. Line AB lies in the plane BAL and is perpendicular to PK' (because K' is the foot of perpendicular from P to AB, by Step 11). Therefore AB is at right angles to the plane E'PK'. [D11.4] Hence AB is perpendicular to E'K'. [D11.3] Since K' lies on AB, angle E'K'A is a right angle.

**Step 18.** In the right triangles E'K'A and EKD: AK' = DK (Step 11), K'E' = KE (Step 16), and the included angles at K' and K are both right angles (Step 17 and Step 5). By SAS, triangle E'K'A is congruent to triangle EKD. [1.4] Therefore angle E'AK' = angle EDK. Since K' is on ray AB from A and K is on ray DF from D, we have angle E'AB = angle EDF.

**Step 19.** The three face angles of the solid angle at A are: angle E'AL = angle EDC (Step 15), angle E'AB = angle EDF (Step 18), and angle BAL = angle FDC (Step 7, by construction). These are respectively equal to the three face angles of the solid angle at D. Therefore the solid angle at A, contained by the plane angles E'AL, E'AB, and BAL, is equal to the solid angle at D, contained by the plane angles EDC, EDF, and FDC.

**Step 20.** Therefore, on the given straight line AB, and at the given point A on it, a solid angle has been constructed equal to the given solid angle at D. Q.E.F.

**USED:** 1.11, 1.12, 1.23, 1.26, 1.3, 1.4, 11.11, 11.12, 11.18, CN1, D11.11, D11.3, D11.4, P1
**Human refs (from References field):** 1.23, 1.4, 1.8, 11.11, 11.12, D11.3
**Jaccard:** 0.333 — AI adds ['1.11', '1.12', '1.26', '1.3', '11.18', 'CN1', 'D11.11', 'D11.4', 'P1']; Human adds ['1.8']

## Proposition 11.27
**Statement:** On a given straight line to describe a parallelepipedal solid similar and similarly situated to a given parallelepipedal solid.

**Step 1.** Let AB be the given straight line, and let CD be the given parallelepipedal solid. Let the solid CD have vertex C, and let the three edges meeting at C be CE, CF, and CG, so that the solid angle at C is contained by the three plane angles ECF, FCG, and ECG. Let CE = e, CF = f, and CG = g be the lengths of these edges.

**Step 2.** We wish to construct on AB a parallelepiped similar and similarly situated to CD, with AB corresponding to the edge CE. At the point A of the straight line AB, construct a solid angle equal to the solid angle at C of the solid CD, contained by the three plane angles ECF, FCG, and ECG [11.26]. Let the three lines forming this solid angle at A be AB (corresponding to CE), AH (corresponding to CF), and AK (corresponding to CG), where the plane angle BAH equals angle ECF, the plane angle HAK equals angle FCG, and the plane angle BAK equals angle ECG.

**Step 3.** Since the parallelepipeds are to be similar, the edges about equal solid angles must be proportional [D11.9, D6.1]. We require AB : CE = AH : CF = AK : CG. Since AB and CE are given, find AH such that AB : CE = AH : CF, that is, AH = (AB · CF) / CE [6.12]. Similarly, find AK such that AB : CE = AK : CG, that is, AK = (AB · CG) / CE [6.12]. Cut off AH along the ray from A corresponding to CF, and AK along the ray from A corresponding to CG, at the lengths so determined [1.3].

**Step 4.** Through H, draw a line parallel to AK, and through K, draw a line parallel to AH [1.31]. Let these meet at L. Then AHLK is a parallelogram in the plane through AH and AK, and the face AHLK corresponds to the face CFPG of the solid CD (where P is the vertex of CD opposite to C in that face). Since AH : CF = AK : CG and angle HAK = angle FCG, the parallelogram AHLK is similar to the parallelogram CFPG [6.24, with equal contained angles and proportional sides].

**Step 5.** Similarly, through B, draw a line parallel to AH and a line parallel to AK [1.31]. Through H, draw a line parallel to AB, and through K, draw a line parallel to AB [1.31]. Complete the three pairs of parallel faces to form a parallelepiped with vertex A and edges AB, AH, AK.

**Step 6.** The face at A in the plane of AB and AH is a parallelogram with sides AB and AH and included angle BAH equal to angle ECF. Since AB : CE = AH : CF and the included angles are equal, this face is similar to the corresponding face of CD [6.24].

**Step 7.** The face at A in the plane of AB and AK is a parallelogram with sides AB and AK and included angle BAK equal to angle ECG. Since AB : CE = AK : CG and the included angles are equal, this face is similar to the corresponding face of CD [6.24].

**Step 8.** By 11.24, the opposite faces of the constructed solid are equal and parallelogrammic, so the solid is indeed a parallelepiped. Each pair of corresponding faces of the two solids is similar (having equal angles and proportional sides), and the solid angles are equal by construction.

**Step 9.** Since the solid constructed on AB has its three edges AB, AH, AK proportional to the three edges CE, CF, CG of CD (all in the same ratio AB : CE), and the solid angles at corresponding vertices are equal, the constructed parallelepiped is similar and similarly situated to CD [D11.9].

**Step 10.** Therefore, on the given straight line AB, a parallelepipedal solid has been described similar and similarly situated to the given parallelepipedal solid CD, which is what was required to be done. Q.E.F.

**USED:** 1.3, 1.31, 11.24, 11.26, 6.12, 6.24, D11.9, D6.1
**Human refs (from References field):** 5.22, 6.12, D11.9
**Jaccard:** 0.222 — AI adds ['1.3', '1.31', '11.24', '11.26', '6.24', 'D6.1']; Human adds ['5.22']

## Proposition 11.28
**Statement:** If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid will be bisected by the plane.

**Step 1.** Let the parallelepipedal solid ABCDA'B'C'D' be given, where ABCD and A'B'C'D' are opposite faces, with AA', BB', CC', DD' as lateral edges. Let the solid be cut by the plane through diagonal AC of face ABCD and diagonal A'C' of the opposite face A'B'C'D'. We must show that this plane bisects the solid.

**Step 2.** By 11.24, the opposite faces of the parallelepiped are equal and parallelogrammic. In particular, ABCD and A'B'C'D' are equal parallelograms, ABB'A' and DCC'D' are equal parallelograms, and BCC'B' and ADD'A' are equal parallelograms.

**Step 3.** By 1.34, the diagonal AC of parallelogram ABCD bisects it, so triangle ABC is equal to triangle ACD. Likewise, the diagonal A'C' of parallelogram A'B'C'D' bisects it, so triangle A'B'C' is equal to triangle A'C'D'.

**Step 4.** The cutting plane ACC'A' divides the parallelepiped into two solids. The first solid has faces: triangle ABC, triangle A'B'C', parallelogram ABB'A', parallelogram BCC'B', and the cutting plane ACC'A'. Since the two triangular faces ABC and A'B'C' are equal, are in parallel planes, and the remaining faces are parallelograms, this solid is a prism by definition (D11.13).

**Step 5.** Similarly, the second solid has faces: triangle ACD, triangle A'C'D', parallelogram DCC'D', parallelogram ADD'A', and the cutting plane ACC'A'. Since the two triangular faces ACD and A'C'D' are equal, are in parallel planes, and the remaining faces are parallelograms, this solid is also a prism by definition (D11.13).

**Step 6.** Now we compare corresponding faces of the two prisms. Triangle ABC equals triangle ACD (Step 3). Triangle A'B'C' equals triangle A'C'D' (Step 3). Parallelogram ABB'A' equals parallelogram DCC'D' (Step 2, by 11.24). Parallelogram BCC'B' equals parallelogram ADD'A' (Step 2, by 11.24). The face ACC'A' is common to both prisms.

**Step 7.** Therefore the two prisms are contained by equal planes, equal in multitude and in magnitude. By the definition of equal and similar solid figures (D11.10), the two prisms are equal to one another.

**Step 8.** Since the parallelepiped is divided into two equal prisms by the cutting plane through the diagonals of the opposite faces, the solid is bisected by the plane. Q.E.D.

**USED:** 1.34, 11.24, D11.10, D11.13
**Human refs (from References field):** 1.34, D11.10
**Jaccard:** 0.500 — AI adds ['11.24', 'D11.13']

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let there be two parallelepipedal solids CM and CN on the same base ABCD and of the same height, where CM has base ABCD and top face EFGH (with AE, BF, CG, DH as the sides which stand up), and CN has the same base ABCD and top face E'F'G'H' (with AE', BF', CG', DH' as the sides which stand up). Suppose the extremities of the sides which stand up lie on the same straight lines, that is, E, F, E', F' lie on one straight line EF', and H, G, H', G' lie on another straight line HG'.

**Step 2.** Since CM is a parallelepiped, its opposite faces are equal and parallelogrammic, by 11.24. Therefore the top face EFGH is a parallelogram equal to the base ABCD, and similarly each pair of opposite faces consists of equal parallelograms. Likewise for CN: the top face E'F'G'H' is a parallelogram equal to the base ABCD.

**Step 3.** Since EFGH is a parallelogram, EH is equal and parallel to FG. Since E'F'G'H' is a parallelogram, E'H' is equal and parallel to F'G', by 1.34. Moreover, since EH and E'H' are both equal and parallel to the same line DC (being opposite sides of the parallelogram faces of the respective solids that share the base side DC), it follows that EH is equal and parallel to E'H', by 11.9 and 1.33.

**Step 4.** Since E, E' lie on the same straight line and H, H' lie on the same straight line, and EH is equal and parallel to E'H', the figure EHH'E' is a parallelogram, by 1.33. Similarly, since FG is equal and parallel to F'G' (both being equal and parallel to BC), the figure FGG'F' is a parallelogram.

**Step 5.** Now consider the solid figure bounded by the two parallelograms EFGH and E'F'G'H' as top and bottom, and by the faces EFE'F' (which lies in a plane since E, F, E', F' are on the same straight line, making EFE' a degenerate face, but EE'F'F is a parallelogram since EF is parallel to E'F' and EE' connects them), EHH'E', FGG'F', and HGG'H'. This is the parallelepiped with base EFGH and opposite face E'F'G'H'.

**Step 6.** Consider the diagonal plane through HF and H'F' in the parallelepiped CM (base ABCD, top EFGH). By 11.28, the plane BDHF divides CM into two equal prisms: prism with triangle ABF on one base and triangle DEH on the other, and prism with triangle BCF on one base and triangle DCH on the other (more precisely, the prism ABFE-DCGH is bisected into two triangular prisms by the diagonal plane). That is, the prism contained by the triangle ABF and the triangle DCG equals the prism contained by the triangle ADE and the triangle BCG, and each is half of CM.

**Step 7.** Similarly, by 11.28, the diagonal plane through the parallelepiped CN (base ABCD, top E'F'G'H') bisects CN into two equal prisms.

**Step 8.** Now consider the prism whose base is triangle AEE' (the triangle formed at vertex A between the two standing edges AE and AE') and which extends to the triangle DHH' at the other end. And consider the prism whose base is triangle BFF' and which extends to triangle CGG'. Since AE is parallel to DH (as sides of the parallelogram ADHE), and AE' is parallel to DH' (as sides of the parallelogram ADH'E'), and EE' lies along the same line as HH', the prism on AEE'-DHH' is properly formed.

**Step 9.** The prism with triangle AEE' as base and triangle DHH' as the corresponding face has AE = DH, AE' = DH', and EE' = HH' (since AEHD and AE'H'D are parallelograms by 11.24 and 1.34, and EHH'E' is a parallelogram by Step 4). By 1.34 the opposite sides of these parallelograms are equal. Therefore triangle AEE' equals triangle DHH' and the prism is properly defined.

**Step 10.** Similarly, the prism on triangle BFF' and triangle CGG' is properly formed, with BF = CG, BF' = CG', and FF' = GG'.

**Step 11.** Now the solid CM (parallelepiped ABCD-EFGH) can be regarded as composed of: the solid ABCD-E'F'G'H' (which is CN) plus the prism on AEE'-DHH', minus the prism on BFF'-CGG'. But we can also see that the solid CM equals the solid ABCD-E'F'G'H' by the following argument using 11.28.

**Step 12.** Apply 11.28 to CM: the plane through the diagonal AF of face ABFE and the diagonal DG of the opposite face DCHG bisects CM into two equal prisms. Call these prisms P1 (containing edge AD) and P2 (containing edge BC). So CM = P1 + P2, and P1 = P2.

**Step 13.** Apply 11.28 to CN: the plane through the diagonal AF' of face ABF'E' and the diagonal DG' of the opposite face DCG'H' bisects CN into two equal prisms. Call these Q1 (containing edge AD) and Q2 (containing edge BC). So CN = Q1 + Q2, and Q1 = Q2.

**Step 14.** Consider prism P1 (from CM). It is the prism with triangular cross-section: on the side of AD, its base triangle has vertices A, E, the foot on line EF at B-side, and extends from AD to... Let us reconsider the decomposition more carefully.

**Step 15.** The parallelepiped CM has top face EFGH with E above A, F above B, G above C, H above D. The diagonal plane through BF, DH (connecting edge BF to edge DH, passing through diagonal BD of the base and diagonal FH of the top) divides CM into two prisms by 11.28: Prism-I = ABD-EFH (with triangular faces ABD and EFH) and Prism-II = BCD-FGH.

**Step 16.** Similarly, CN has top face E'F'G'H'. The diagonal plane through BF', DH' divides CN into two prisms by 11.28: Prism-III = ABD-E'F'H' and Prism-IV = BCD-F'G'H'.

**Step 17.** Now consider the auxiliary solid ABCD-EF'G'H, which shares the base ABCD with both CM and CN. Its standing edges are AE, BF', CG', DH. Since AE is parallel to DH (they stand on AD and connect to EH, which is parallel to AD by 11.24 and 1.34), and BF' is parallel to CG' (they stand on BC and connect to F'G', which is parallel to BC), this solid is also a parallelepiped.

**Step 18.** The diagonal plane through BF', DH divides the auxiliary solid ABCD-EF'G'H into two prisms by 11.28: Prism-V = ABD-EF'H and Prism-VI = BCD-F'G'H.

**Step 19.** Now compare Prism-I (ABD-EFH) with Prism-V (ABD-EF'H). They share the common base triangle ABD and the common vertex E (above A) and H (above D). The only difference is F versus F' above B, where F and F' both lie on the same straight line. The prism ABD-EFH has as one parallelogram face the figure ABFE, while ABD-EF'H has ABFE' replaced by ABF'E. However, both prisms have the same triangular base ABD, the same edge AE and DH, and BF vs BF' along the same line. By 1.35, parallelograms on the same base and between the same parallels are equal: ABFE and ABF'E are on the same base AB and between the same parallel lines (since E, F, F' and E all have their extremities on the same lines). Similarly DHGE and DHG'E... 

**Step 20.** Let us use a more direct approach. Prism-I has base ABD and opposite face EFH. Prism-V has base ABD and opposite face EF'H. Both base triangles are identical (ABD). The opposite triangles EFH and EF'H share vertices E and H, while F and F' lie on the same straight line (by hypothesis, the extremities F and F' are on the same line). Since EFH and EF'H are triangles on the same base EH and between the same parallel lines (the line through EH and the line through FF', noting FG is parallel to EH), by 1.37 (triangles on the same base and between the same parallels are equal), triangle EFH equals triangle EF'H.

**Step 21.** Moreover, Prism-I and Prism-V have equal bases (both ABD), equal opposite faces (EFH = EF'H by Step 20), and the same height (the perpendicular distance from the plane of ABCD to the plane through EH, which is the same for both since F and F' are at the same height). Since the prisms are contained between the same parallel planes (the base plane through ABCD and the top plane through E, H and the line FF'), by 11.24 and the definition of equal prisms, Prism-I = Prism-V.

**Step 22.** Now compare Prism-II (BCD-FGH) with Prism-VI (BCD-F'G'H). They share the common base triangle BCD. The opposite faces are FGH and F'G'H. Since H and H' lie on the same straight line and G, G' lie on the same straight line, and F, F' lie on the same straight line, the triangle FGH and triangle F'G'H share vertex H. But we need to compare triangles FGH and F'G'H. These triangles are on the same base FG... Actually, they share vertex H, and F, F' lie on the same line while G, G' lie on the same line. Since FG is parallel to HH'... Let us reconsider.

**Step 23.** Reconsider: Prism-II = BCD-FGH and Prism-IV = BCD-F'G'H'. These prisms both have base triangle BCD. The triangle FGH has F above B, G above C, H above D. The triangle F'G'H' has F' above B, G' above C, H' above D. Now FG is parallel to BC (by 11.24 and 1.34) and F'G' is parallel to BC. Also GH is parallel to CD and G'H' is parallel to CD. So both triangles FGH and F'G'H' are similar and equal triangles (since FG = F'G' = BC, GH = G'H' = CD, FH = F'H' = BD, all being corresponding sides of equal parallelogram faces, by 11.24 and 1.34). Therefore triangle FGH is congruent to triangle F'G'H' by 1.8.

**Step 24.** Furthermore, both Prism-II and Prism-IV lie between the same pair of parallel planes: the plane of ABCD and the plane containing the parallel lines through FF' and GG' (and HH'). The three lateral faces of each prism are parallelograms. Since the bases are equal, the opposite faces are equal, and they lie between the same parallel planes with the same height, Prism-II = Prism-IV.

**Step 25.** Also compare Prism-VI (BCD-F'G'H) with Prism-IV (BCD-F'G'H'). They share the base BCD and the edge BF' and CG'. Prism-VI has vertex H in its top face while Prism-IV has vertex H'. Since H and H' lie on the same line as the other extremities, and G'H is parallel to G'H'... We need triangle F'G'H vs triangle F'G'H'. These share edge F'G', while H and H' lie on the same line. By 1.37, triangles on the same base F'G' between the same parallels (the line F'G' and the line HH') are equal. So triangle F'G'H = triangle F'G'H'. By the same reasoning as Step 21, Prism-VI = Prism-IV.

**Step 26.** From Step 21: Prism-I = Prism-V. Therefore CM = Prism-I + Prism-II = Prism-V + Prism-II.

**Step 27.** From Step 25: Prism-VI = Prism-IV. The auxiliary solid = Prism-V + Prism-VI = Prism-V + Prism-IV. Also CN = Prism-III + Prism-IV.

**Step 28.** We need one more relation. Compare Prism-II (BCD-FGH) and Prism-VI (BCD-F'G'H). These share base BCD. The opposite triangles are FGH and F'G'H. Triangle FGH has vertices F, G, H above B, C, D respectively. Triangle F'G'H has vertices F', G', H above B, C, D (note H, not H'). Since F, F' lie on the same line and G, G' lie on the same line, and FG is parallel to F'G' (both parallel to BC), triangle FGH and F'G'H are on the base GH (shared vertex) with F and F' on the same line. By 1.37, if we take base GH, then since F and F' lie between the same parallels as GH (namely FG parallel to a line through H and F'G' parallel to the same), the triangles FGH and F'G'H are equal in area. By the prism equality argument (same base triangle BCD, equal and similarly situated opposite triangles at the same height between the same parallel planes), Prism-II = Prism-VI.

**Step 29.** Now we can conclude. CM = Prism-I + Prism-II (by Step 15 and 11.28). And CN = Prism-III + Prism-IV (by Step 16 and 11.28). The auxiliary solid = Prism-V + Prism-VI (by Step 18 and 11.28). From Step 21, Prism-I = Prism-V. From Step 28, Prism-II = Prism-VI. Therefore CM = Prism-I + Prism-II = Prism-V + Prism-VI = auxiliary solid.

**Step 30.** By entirely symmetric reasoning (now comparing the auxiliary solid ABCD-EF'G'H with CN = ABCD-E'F'G'H'), we use the fact that E, E' lie on the same line and H, H' are endpoints with H for the auxiliary solid and H' for CN. The diagonal planes divide the auxiliary solid and CN into prisms that can be compared pairwise using 1.37 and 11.28 in the same manner as above. This gives: auxiliary solid = CN.

**Step 31.** Therefore CM = auxiliary solid = CN, by CN1. That is, the two parallelepipedal solids on the same base, of the same height, and with the extremities of their standing sides on the same straight lines, are equal to one another. Q.E.D.

**USED:** 1.33, 1.34, 1.37, 11.24, 11.28, 11.9, CN1
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.100 — AI adds ['1.33', '1.37', '11.24', '11.28', '11.9', 'CN1']; Human adds ['1.36', '1.4', '1.8']

## Proposition 11.30
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another.

**Step 1.** Let the parallelepipedal solids CM and CN be on the same base AB and of the same height, and let the extremities of the sides which stand up, namely AF, AG, LM, LN, CD, CE, BH, BK, not be on the same straight lines. We must show that solid CM equals solid CN.

**Step 2.** Produce NK and DH to meet one another at R, and produce FM and GE to meet one another at Q. Produce also AQ to S and AR to T. Since the solid CM is parallelepipedal, the face opposite to ACBL is a parallelogram. Hence the pairs AF, LM and CD, BH are parallel. Similarly, since CN is parallelepipedal, AG, LN and CE, BK are parallel. By the definition of a parallelepiped (D11.13, 11.24), opposite faces are parallel and parallelogrammic.

**Step 3.** Since CH is a parallelogram (face of solid CM), DH is parallel to CB. Since CK is a parallelogram (face of solid CN), DK is parallel to CB. But there is only one line through D parallel to CB, hence DH and DK lie on the same straight line, that is, HK and DR lie on the same straight line HRK (by 11.1 and P2). By the same reasoning, since BH is parallel to CD (in solid CM) and BK is parallel to CE (in solid CN), we consider the faces on side BL: LM is parallel to AF, and LN is parallel to AG, so that FM and GE, when produced, meet at Q.

**Step 4.** Complete the parallelepiped CT with base AB whose edges standing up from A, C, B, L terminate at S, T, R, Q respectively, where AS is parallel to CR, and BQ is parallel to LT. More precisely, produce FG to meet the plane through BHK at appropriate points: let NK and DH meet at R and FM and GE meet at Q. Draw AS parallel to CR and LQ parallel to BT (by P1 and 1.31). Then DTBR is a parallelogram, and ASQL is a parallelogram, and we have the parallelepiped CR (with vertices A, S at one end corresponding to C, T, and B, R corresponding to L, Q at the other).

**Step 5.** Now consider solid CM (with standing edges AF, CD, BH, LM) and solid CR (with standing edges AS, CT, BR, LQ). These are on the same base ACBL. The extremities F, D, H, M of the standing edges of CM lie in one plane (the top face of CM), and the extremities S, T, R, Q of the standing edges of CR lie in another plane (the top face of CR). Since AF and AS both stand up from A, and CD and CT both stand up from C, and BH and BR both stand up from B, and LM and LQ both stand up from L, we examine whether the extremities are on the same straight lines.

**Step 6.** Since FG and SR both pass through the edges from A and from L (being opposite sides of faces of the respective solids), and FM produced meets GE at Q while DH produced meets NK at R, the extremities of the standing edges of CM and CR are on the same straight lines FMS-QR and DHR respectively. Specifically, F and S are on line FS (since AF and AS stand up from A, and both F and S lie on the line through F toward Q), and similarly D and T are on line DT, H and R are on line HR, and M and Q are on line MQ. Thus the edges standing up from the base ACBL for solids CM and CR have their extremities on the same straight lines. By 11.29, solid CM equals solid CR.

**Step 7.** Similarly, consider solid CN (with standing edges AG, CE, BK, LN) and solid CR (with standing edges AS, CT, BR, LQ). These are also on the same base ACBL. Since G and S are on the same straight line GS (both AG and AS stand up from A), E and T are on line ET (both CE and CT stand up from C), K and R are on line KR (both BK and BR stand up from B), and N and Q are on line NQ (both LN and LQ stand up from L), the extremities of the standing edges of CN and CR lie on the same straight lines. By 11.29, solid CN equals solid CR.

**Step 8.** Since solid CM equals solid CR (Step 6) and solid CN equals solid CR (Step 7), by CN1 (things equal to the same thing are equal to one another), solid CM equals solid CN.

**Step 9.** Therefore, parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another. Q.E.D.

**USED:** 1.31, 1.34, 11.1, 11.24, 11.29, CN1, D11.13, P1, P2
**Human refs (from References field):** 11.29
**Jaccard:** 0.111 — AI adds ['1.31', '1.34', '11.1', '11.24', 'CN1', 'D11.13', 'P1', 'P2']

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let AE and CF be parallelepipedal solids on equal parallelogrammic bases ABCD and EFGH, and of the same height.

**Step 2.** On the base ABCD, construct the right parallelepiped AE' having its standing edges perpendicular to the plane of ABCD, of the same height as AE. Since AE and AE' are on the same base ABCD and of the same height, by Proposition 11.30, AE equals AE'. Similarly, construct the right parallelepiped CF' on base EFGH with perpendicular standing edges of the same height; by 11.30, CF equals CF'.

**Step 3.** It suffices to show that AE' equals CF'. Let the vertices of AE' be A, B, C, D on the base and A', B', C', D' directly above them (the standing edges AA', BB', CC', DD' being perpendicular to the base plane). Since the standing edges are perpendicular to the base plane, by Definition 11.3, each makes right angles with every line in the base plane through its foot. In particular, the angle A'AB is right. Hence the lateral face ABB'A' is a rectangle with sides AB and AA' (equal to the common height h).

**Step 4.** Consider the solid AE' with the rectangular face ABB'A' as its base, re-orienting the parallelepiped. By Proposition 11.24, opposite faces of a parallelepiped are equal and parallel, so this re-orientation produces a valid parallelepiped on the rectangular base ABB'A'. In this orientation, the standing edges from A, B, A', B' go to D, C, D', C' respectively. Since the angle DAB in the original base parallelogram ABCD need not be a right angle, these standing edges are in general oblique to the face ABB'A'.

**Step 5.** The height of AE' in this new orientation is the perpendicular distance from the plane of face ABB'A' to the plane of the opposite face DCC'D'. This distance equals the altitude of the parallelogram ABCD with respect to side AB; call this altitude d1.

**Step 6.** By Proposition 11.30, AE' (viewed as an oblique parallelepiped on the rectangular base ABB'A') equals the right parallelepiped on the same rectangular base ABB'A' with the same height d1. This right parallelepiped is a rectangular box R1 with three perpendicular dimensions: the length AB (call it a), the original height h, and the width d1.

**Step 7.** Applying the same re-orientation and reduction to CF', we obtain that CF' equals a rectangular box R2 with perpendicular dimensions: EF (call it e), h, and d2, where d2 is the altitude of parallelogram EFGH with respect to side EF.

**Step 8.** Since parallelograms ABCD and EFGH are equal, their areas are equal. The area of ABCD equals a times d1, and the area of EFGH equals e times d2. Therefore the rectangle contained by a and d1 equals the rectangle contained by e and d2.

**Step 9.** We now show R1 equals R2. Construct a rectangular parallelepiped with base of dimensions a by (d1 + d2) and height h. This solid consists of R1 (occupying width d1) and a rectangular box R3 (of dimensions a, h, d2) placed side by side along the width direction. Cut this parallelepiped by a plane parallel to its a-by-h faces at width d1. By Proposition 11.25, the base of the piece occupying width d1 (a rectangle a by d1) is to the base of the piece occupying width d2 (a rectangle a by d2) as the first solid is to the second. By Proposition 6.1, since both rectangles have the same height a, their ratio equals d1 to d2. Therefore R1 is to R3 as d1 is to d2.

**Step 10.** Similarly, construct a rectangular parallelepiped with base of dimensions (a + e) by d2 and height h, containing R3 (occupying length a) and R2 (occupying length e) placed side by side along the length direction. Cut at length a by a plane parallel to the d2-by-h faces. By Proposition 11.25, the base of R3 (rectangle a by d2) is to the base of R2 (rectangle e by d2) as R3 is to R2. By Proposition 6.1, since both rectangles have height d2, their ratio equals a to e. Therefore R3 is to R2 as a is to e.

**Step 11.** Since the rectangle contained by a and d1 equals the rectangle contained by e and d2 (Step 8), by Proposition 6.16 the four lines are proportional: a is to e as d2 is to d1. Substituting into the result of Step 10: R3 is to R2 as d2 is to d1.

**Step 12.** From Step 9, R1 is to R3 as d1 is to d2. From Step 11, R3 is to R2 as d2 is to d1. By Proposition 5.22 (ex aequali), R1 is to R2 as d1 is to d1.

**Step 13.** Since R1 is to R2 as d1 is to d1, and d1 equals itself, R1 equals R2. For by Proposition 5.7, since R2 equals R2, the magnitude R2 has to itself the ratio of equality, which is the same ratio as d1 to d1; hence R1 is to R2 as R2 is to R2, and by Proposition 5.9 (magnitudes which have the same ratio to the same magnitude are equal), R1 equals R2.

**Step 14.** Therefore AE equals AE' (Step 2), AE' equals R1 (Step 6), R1 equals R2 (Step 13), R2 equals CF' (Step 7), and CF' equals CF (Step 2). By Common Notion 1, AE equals CF.

Therefore, parallelepipedal solids which are on equal bases and of the same height are equal to one another. Q.E.D.

**USED:** 11.24, 11.25, 11.30, 5.22, 5.7, 5.9, 6.1, 6.16, CN1, D11.3
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.333 — AI adds ['5.22', '6.1', '6.16', 'CN1', 'D11.3']; Human adds ['1.23', '1.35', '11.29', '5.11', 'D11.10']

## Proposition 11.32
**Statement:** Parallelepipedal solids which are of the same height are to one another as their bases.

**Step 1.** Let AB and CD be two parallelepipedal solids of the same height, and let AE and CF be their respective bases. We must show that solid AB is to solid CD as base AE is to base CF.

**Step 2.** On one of the edges of the base CF of solid CD, construct a parallelogram FH equal to the base AE, in the same angle as CF. This is possible by 1.45, which allows us to construct a parallelogram equal to a given rectilineal figure in a given rectilineal angle on a given straight line.

**Step 3.** On the base FH, complete the parallelepipedal solid GK with the same height as solid CD and with edges standing up parallel to those of CD. This construction is justified by 11.27, which permits describing a parallelepipedal solid similar and similarly situated to a given parallelepipedal solid on a given straight line. The solid GK has the same height as both AB and CD.

**Step 4.** Since solid AB has base AE and solid GK has base FH, and AE equals FH by construction, the two solids AB and GK stand on equal bases. Moreover, they have the same height. Therefore, by 11.31, solid AB is equal to solid GK.

**Step 5.** Now consider the solids GK and CD. They share the same height, and GK stands on base FH while CD stands on base CF, where FH and CF lie along the same line with a common edge. The solid composed of GK and CD together can be viewed as a single parallelepipedal solid that is cut by a plane parallel to its opposite faces, separating it into the portions GK (on base FH) and CD (on base CF). Therefore, by 11.25, solid GK is to solid CD as base FH is to base CF.

**Step 6.** Since solid AB equals solid GK (Step 4), by 5.7, solid AB has to solid CD the same ratio that solid GK has to solid CD. That is, solid AB is to solid CD as solid GK is to solid CD.

**Step 7.** Therefore, solid AB is to solid CD as base FH is to base CF (combining Steps 5 and 6 by 5.11).

**Step 8.** Since base FH equals base AE (by construction in Step 2), by 5.7, base FH is to base CF as base AE is to base CF.

**Step 9.** Combining Steps 7 and 8 by 5.11, solid AB is to solid CD as base AE is to base CF.

**Step 10.** Therefore, parallelepipedal solids which are of the same height are to one another as their bases. Q.E.D.

**USED:** 1.45, 11.25, 11.27, 11.31, 5.11, 5.7
**Human refs (from References field):** 1.45, 11.25, 11.31
**Jaccard:** 0.500 — AI adds ['11.27', '5.11', '5.7']

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

**Step 1.** Let AB and CD be similar parallelepipedal solids, and let AE be a side of AB corresponding to the side CF of CD. We are to prove that solid AB is to solid CD in the triplicate ratio of AE to CF.

**Step 2.** Since the parallelepipeds AB and CD are similar, their corresponding edges are proportional (D11.9, D6.1). Let the three edges of AB meeting at one vertex be AE, AG, AH, and let the three corresponding edges of CD meeting at the corresponding vertex be CF, CK, CL, so that AE : CF = AG : CK = AH : CL.

**Step 3.** Produce the edge AE in a straight line (P2). On AE produced, set off EM equal to CF, and on this line set off EN equal to CK, taking EN along the direction of AG, and set off EO equal to CL along the direction of AH. More precisely, on the three edges from the vertex E of solid AB, construct a parallelepiped EP on edges EM, EN, EO, where EM = CF, EN = CK, EO = CL, so that the parallelepiped EP is arranged on the same base-plane and same orientation as AB at vertex E.

**Step 4.** Since AE : CF = AG : CK = AH : CL, and EM = CF, EN = CK, EO = CL, we have AE : EM = AG : EN = AH : EO.

**Step 5.** The parallelogram formed by edges AE and AG is similar to the parallelogram formed by edges EM and EN, since the sides about the equal angles (the solid angles of similar solids are contained in equal plane angles by 11.24 and D11.9) are proportional: AE : EM = AG : EN (6.24, and D6.1).

**Step 6.** Likewise, the parallelogram formed by edges AG and AH is similar to that formed by EN and EO, and the parallelogram formed by edges AE and AH is similar to that formed by EM and EO, since in each case the sides about equal angles are proportional.

**Step 7.** Therefore the parallelepiped EP (on edges EM = CF, EN = CK, EO = CL, with the same angles as at the vertex of AB, which equal the angles at the corresponding vertex of CD since the solids are similar) is both equal and similar to the parallelepiped CD (D11.10). So solid EP equals solid CD.

**Step 8.** Now construct two further intermediate parallelepipeds. Let EX be the parallelepiped on edges AE, EN, EO (keeping the same angles at vertex E). Let EY be the parallelepiped on edges AE, AG, EO (keeping the same angles at vertex E).

**Step 9.** Consider solids AB and EY. These share the same edge AE and the same edge AG, but differ in the third edge: AB has edge AH while EY has edge EO. The base parallelogram in both solids (formed by AE and AG) is the same. Both solids stand on this same base and have heights AH and EO respectively along the same perpendicular direction. By 11.25, the solid AB is to the solid EY as AH is to EO. Since AH : EO = AH : CL = AE : CF (from Step 4), we have solid AB : solid EY = AE : CF.

**Step 10.** Consider solids EY and EX. These share edge AE and edge EO, but differ in their second edge: EY has AG while EX has EN. The base parallelogram of EY is formed by AE and EO, and the base of EX is the same parallelogram formed by AE and EO. Their heights along the direction of AG and EN respectively are AG and EN. By 11.25, solid EY : solid EX = AG : EN. Since AG : EN = AG : CK = AE : CF (from Step 4), we have solid EY : solid EX = AE : CF.

**Step 11.** Consider solids EX and EP. These share edge EN and edge EO, but differ in their first edge: EX has AE while EP has EM. The base parallelogram of EX is formed by EN and EO, and the base of EP is the same parallelogram formed by EN and EO. Their heights are AE and EM respectively. By 11.25, solid EX : solid EP = AE : EM. Since EM = CF, we have solid EX : solid EP = AE : CF.

**Step 12.** We now have three ratios in continuous proportion:
  solid AB : solid EY = AE : CF,
  solid EY : solid EX = AE : CF,
  solid EX : solid EP = AE : CF.

**Step 13.** Since these three ratios are all equal, the four magnitudes solid AB, solid EY, solid EX, solid EP are in continued proportion with common ratio AE : CF. By the definition of triplicate ratio (D5.10), the first (solid AB) has to the fourth (solid EP) the triplicate ratio of that which it has to the second, i.e., the triplicate ratio of AE to CF.

**Step 14.** But solid EP equals solid CD (Step 7). Therefore solid AB has to solid CD the triplicate ratio of AE to CF, that is, the triplicate ratio of the corresponding side AE to the corresponding side CF.

**Step 15.** Therefore similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides. Q.E.D.

**USED:** 11.25, 5.22, 6.24, CN1, D11.10, D11.9, D5.10, D5.9, D6.1, P2
**Human refs (from References field):** 11.24, 11.32, 6.1, D11.10, D5.10
**Jaccard:** 0.154 — AI adds ['11.25', '5.22', '6.24', 'CN1', 'D11.9', 'D5.9', 'D6.1', 'P2']; Human adds ['11.24', '11.32', '6.1']

## Proposition 11.34
**Statement:** In equal parallelepipedal solids the bases are reciprocally proportional to the heights; and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let AB and CD be two equal parallelepipedal solids. Let the base of AB be the parallelogram EH, with height the perpendicular edge AE, and let the base of CD be the parallelogram NQ, with height the perpendicular edge CN. We are to show that base EH is to base NQ as height CN is to height AE. (We treat the general case; for rectangular parallelepipeds the argument is equivalent after applying 11.31 to reduce to this setting.)

**Step 2.** On the base EH, construct a parallelepipedal solid FO with height equal to CN. This is possible by 11.27 (describing a parallelepiped similar and similarly situated to a given one on a given line) and by the general construction of parallelepipeds on a given base to a given height using 11.29 and 11.31.

**Step 3.** Since solid AB and solid FO are on the same base EH, by 11.25, solid AB is to solid FO as height AE is to height CN. More precisely, if we regard the solid with the greater height as being cut by a plane parallel to the base at the level of the lesser height, then by 11.25, the portion cut off (which equals the solid with the lesser height, by 11.31 and 11.29) is to the whole solid as the lesser height is to the greater height.

**Step 4.** Since solid FO and solid CD have the same height CN, by 11.32, solid FO is to solid CD as base EH is to base NQ.

**Step 5.** Now, since solid AB equals solid CD (given), we have solid AB : solid FO = solid CD : solid FO. But from Step 3, solid AB : solid FO = AE : CN, and from Step 4, solid FO : solid CD = base EH : base NQ, that is, solid CD : solid FO = base NQ : base EH (by 5.16, taking the inverse of the ratio from Step 4). Since solid AB = solid CD, solid AB : solid FO = solid CD : solid FO. From Step 3, this ratio equals AE : CN. From Step 4 inverted, solid CD : solid FO = base NQ : base EH. Hence AE : CN = base NQ : base EH.

**Step 6.** By 5.16 (inverse proportion), taking the inverse of both sides, CN : AE = base EH : base NQ. That is, base EH : base NQ = CN : AE, which states that the bases are reciprocally proportional to the heights. This completes the first part.

**Step 7.** For the converse, let parallelepipedal solids AB and CD be such that base EH : base NQ = height CN : height AE. We are to show solid AB = solid CD.

**Step 8.** Construct the same auxiliary solid FO as in Step 2, on base EH with height equal to CN.

**Step 9.** By 11.25 (as in Step 3), solid AB : solid FO = height AE : height CN.

**Step 10.** By 11.32 (as in Step 4), solid FO : solid CD = base EH : base NQ.

**Step 11.** By hypothesis, base EH : base NQ = CN : AE. By 5.16, taking the inverse, base NQ : base EH = AE : CN. Therefore solid FO : solid CD = base EH : base NQ = CN : AE (by hypothesis). Taking the inverse by 5.16, solid CD : solid FO = AE : CN.

**Step 12.** From Step 9, solid AB : solid FO = AE : CN. From Step 11, solid CD : solid FO = AE : CN. Therefore, by 5.11 (ratios equal to the same ratio are equal to each other), solid AB : solid FO = solid CD : solid FO.

**Step 13.** Since solid AB and solid CD have the same ratio to solid FO, by 5.9, solid AB equals solid CD. This completes the converse.

**Step 14.** Therefore, in equal parallelepipedal solids the bases are reciprocally proportional to the heights; and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal. Q.E.F.

**USED:** 11.25, 11.27, 11.29, 11.31, 11.32, 5.11, 5.16, 5.9
**Human refs (from References field):** 11.25, 11.29, 11.30, 11.31, 11.32, 5.7, 5.9, 6.1
**Jaccard:** 0.455 — AI adds ['11.27', '5.11', '5.16']; Human adds ['11.30', '5.7', '6.1']

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

**Step 1.** Let angle BAC and angle EDF be the given equal plane angles. Let AG be elevated from A and DM from D, with angle BAG = angle EDM and angle CAG = angle FDM. Let G and M be points on the elevated lines, and let GH and MN be the perpendiculars from G and M to the respective planes, with H and N in those planes. Since the angle of inclination of a line to a plane is the same for any point on the line (the right triangles formed are similar, by 6.4), we may set AG = DM without loss of generality (by 1.3).

**Step 2.** On ray AB mark off AB equal to DE, and on ray AC mark off AC equal to DF (by 1.3). Join BC, EF, BG, CG, EM, FM (by P1).

**Step 3.** In triangles ABG and DEM: AB = DE, AG = DM, and angle BAG = angle EDM. By 1.4 (SAS), the triangles are congruent. Therefore BG = EM, and the altitudes from G to AB and from M to DE are equal.

**Step 4.** In triangles ACG and DFM: AC = DF, AG = DM, and angle CAG = angle FDM. By 1.4, the triangles are congruent. Therefore CG = FM, and the altitudes from G to AC and from M to DF are equal.

**Step 5.** In triangles ABC and DEF: AB = DE, AC = DF, and angle BAC = angle EDF. By 1.4, the triangles are congruent. Therefore BC = EF. Moreover, the triangles have equal areas (by CN4, since congruent figures are equal).

**Step 6.** In triangles BGC and EMF: BG = EM (Step 3), CG = FM (Step 4), BC = EF (Step 5). By 1.8 (SSS), the triangles are congruent. Therefore the altitudes from G to BC and from M to EF are equal.

**Step 7.** Since GH is perpendicular to the plane of angle BAC, by D11.3 it makes right angles with every line through H in that plane. In particular, angle GHA = angle GHB = angle GHC = 90 degrees. By 1.47 on these right triangles: AG^2 = GH^2 + AH^2, BG^2 = GH^2 + BH^2, and CG^2 = GH^2 + CH^2. Similarly, since MN is perpendicular to the plane of angle EDF: DM^2 = MN^2 + DN^2, EM^2 = MN^2 + NE^2, and FM^2 = MN^2 + NF^2.

**Step 8.** Let h_1, h_2, h_3 denote the altitudes from G to lines AB, AC, BC respectively, which equal the corresponding altitudes from M to lines DE, DF, EF (by Steps 3, 4, 6; the equality of altitudes follows from the equal areas of the congruent triangles, by 1.41 and CN4, since equal areas with equal bases yield equal heights). Since GH is perpendicular to the base plane, each altitude h_i from G to a side of the triangle decomposes into the vertical component GH and the horizontal component d_i (the perpendicular distance from H to that side in the base plane), satisfying h_i^2 = GH^2 + d_i^2 (by 1.47, using D11.3 and 11.4 to confirm the foot of the altitude from G to a side coincides with the projection from H to that side). Similarly h_i^2 = MN^2 + d_i'^2 where d_i' is the perpendicular distance from N to the corresponding side. Since h_i is the same for both configurations: d_i^2 - d_i'^2 = MN^2 - GH^2 for i = 1, 2, 3.

**Step 9.** Suppose for contradiction that GH > MN. Then MN^2 - GH^2 < 0, so d_i < d_i' for each i = 1, 2, 3. That is, the perpendicular distance from H to each side of triangle ABC is strictly less than the corresponding perpendicular distance from N to the corresponding side of triangle DEF.

**Step 10.** We choose AB = DE and AC = DF large enough that H lies inside triangle ABC and N lies inside triangle DEF (this is always possible since AH is fixed while B and C can be taken arbitrarily far along their rays). Then by 1.41, the area of each sub-triangle equals half the product of its base and the perpendicular height from the interior point: Area(ABH) = (1/2)*AB*d_1, Area(ACH) = (1/2)*AC*d_2, Area(BCH) = (1/2)*BC*d_3, and similarly Area(DEN) = (1/2)*DE*d_1', Area(DFN) = (1/2)*DF*d_2', Area(ENF) = (1/2)*EF*d_3'.

**Step 11.** Since AB = DE and d_1 < d_1', we have Area(ABH) < Area(DEN). Since AC = DF and d_2 < d_2', Area(ACH) < Area(DFN). Since BC = EF and d_3 < d_3', Area(BCH) < Area(ENF). Adding these three inequalities (by CN2 and CN5): Area(ABH) + Area(ACH) + Area(BCH) < Area(DEN) + Area(DFN) + Area(ENF). But the left side equals Area(ABC) and the right side equals Area(DEF), and these areas are equal (Step 5). This is a contradiction.

**Step 12.** By the same argument, if GH < MN then each d_i > d_i', and every sub-triangle area on the left exceeds its counterpart on the right, giving Area(ABC) > Area(DEF), again a contradiction. Therefore GH = MN.

**Step 13.** Since GH = MN and AG = DM, from Step 7: AH^2 = AG^2 - GH^2 = DM^2 - MN^2 = DN^2. Therefore AH = DN.

**Step 14.** In right triangles GAH and MDN: GA = MD (by construction), AH = DN (Step 13), and the included angles GHA = MND = 90 degrees (Step 7). By 1.4 (SAS), triangle GAH is congruent to triangle MDN. Therefore angle GAH = angle MDN, which is what was to be proved.

**USED:** 1.3, 1.4, 1.41, 1.47, 1.8, 11.4, 6.4, CN2, CN4, CN5, D11.3, P1
**Human refs (from References field):** 1.26, 1.4, 1.47, 1.48, 1.8, 11.8
**Jaccard:** 0.200 — AI adds ['1.3', '1.41', '11.4', '6.4', 'CN2', 'CN4', 'CN5', 'D11.3', 'P1']; Human adds ['1.26', '1.48', '11.8']

## Proposition 11.36
**Statement:** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

**Step 1.** Let A, B, C be three straight lines in proportion, so that A : B :: B : C. Let S be the parallelepipedal solid formed out of the three lines A, B, C at a given solid angle, and let P be the equilateral parallelepipedal solid on B which is equiangular with S, that is, P has all three edges equal to B and the same solid angle as S. We are to prove that S equals P.

**Step 2.** Construct an intermediate parallelepipedal solid Q having edges A, B, B at the same solid angle as S and P. This is possible by constructing a solid angle equal to the given one [11.26] and completing the parallelepiped with the specified edge lengths.

**Step 3.** Compare S and Q. The solids S (with edges A, B, C) and Q (with edges A, B, B) share the same solid angle and the same edge A in one direction. Taking as their respective bases the parallelogrammic faces opposite to the edge A, both solids have the same height (the perpendicular distance between the pair of opposite faces determined by the direction of edge A, which is the same for both since the solid angle and the edge A are the same). By 11.32, S : Q equals the ratio of the base of S to the base of Q.

**Step 4.** The base of S is the parallelogram with sides B and C at the angle determined by the solid angle, and the base of Q is the parallelogram with sides B and B at the same angle. These two parallelograms share the same side B and the same included angle, so they have the same height (the perpendicular from the endpoints of side B to the line of the other side). By 6.1, parallelograms under the same height are to one another as their bases, so the base of S is to the base of Q as C is to B. Therefore S : Q :: C : B.

**Step 5.** Compare Q and P. The solids Q (with edges A, B, B) and P (with edges B, B, B) share the same solid angle and both have edge B in two of the three directions. Taking as their respective bases the parallelogrammic faces with sides B and B (which are identical parallelograms), both solids have the same base. However, we compare them by taking the direction of the differing edge as providing the height. Consider the faces with sides B and B (the second and third edges) as bases; Q has height determined by edge A and P has height determined by edge B, both in the same direction from the same solid angle. By 11.32, Q : P equals the ratio of the base of Q to the base of P, where now we orient the solids so the differing edge determines the height. Taking the pair of opposite faces perpendicular to the direction of the first edge, Q and P have the same height (both having edge B in that perpendicular direction). Their bases are parallelograms with sides A, B and sides B, B respectively, at the same angle. By 6.1, these bases are as A is to B. Therefore Q : P :: A : B.

**Step 6.** From the given proportion A : B :: B : C, by inversion [5.7 corollary], we obtain B : A :: C : B, which can be rewritten as C : B :: B : A. Therefore from Step 4, S : Q :: C : B :: B : A.

**Step 7.** We now have S : Q :: B : A (from Step 6) and Q : P :: A : B (from Step 5). Applying the ex aequali rule [5.22], which states that if S : Q :: B : A and Q : P :: A : B, then S : P :: B : B.

**Step 8.** Since B equals itself, the ratio B : B is the ratio of equality. From S : P :: B : B it follows that S : P :: P : P (since any magnitude has to itself the ratio of equality, which is the same as B : B). Therefore S and P are magnitudes to which the same magnitude P has the same ratio, and by 5.9, S equals P.

**Step 9.** Therefore the parallelepipedal solid S formed out of the three proportional straight lines A, B, C is equal to the equilateral parallelepipedal solid P on the mean B which is equiangular with S. This is what was to be proved.

**USED:** 11.26, 11.32, 5.22, 5.7, 5.9, 6.1
**Human refs (from References field):** 11.31, 11.35, 6.14
**Jaccard:** 0.000 — AI adds ['11.26', '11.32', '5.22', '5.7', '5.9', '6.1']; Human adds ['11.31', '11.35', '6.14']

## Proposition 11.37
**Statement:** If four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described will also be proportional; and, if the parallelepipedal solids on them which are similar and similarly described be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let A, B, C, D be four straight lines such that A : B :: C : D. Let similar and similarly described parallelepipedal solids be constructed on each of them: call them Solid(A), Solid(B), Solid(C), Solid(D) respectively. We must show that Solid(A) : Solid(B) :: Solid(C) : Solid(D).

**Step 2.** By 6.11, find E such that A : B :: B : E. Then by D5.9, A has to E the duplicate ratio of that which A has to B.

**Step 3.** Again by 6.11, find F such that B : E :: E : F, so that A : B :: B : E :: E : F form a continuous proportion. Equivalently, A : B :: E : F. Then by D5.10, A has to F the triplicate ratio of that which A has to B, since A, B, E, F are four magnitudes in continuous proportion.

**Step 4.** Similarly, since C : D is given, find G such that C : D :: D : G (by 6.11), and find H such that C : D :: G : H. Then C, D, G, H are in continuous proportion, and by D5.10, C has to H the triplicate ratio of that which C has to D.

**Step 5.** By 11.33, similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides. Therefore Solid(A) : Solid(B) is the triplicate ratio of A : B, which is A : F. Similarly, Solid(C) : Solid(D) is the triplicate ratio of C : D, which is C : H.

**Step 6.** Now since A : B :: C : D (given), and A : B :: B : E, and C : D :: D : G, it follows that B : E :: D : G (by 5.11, both equal to A : B and C : D respectively). Therefore by 5.22 (ex aequali), since A : B :: C : D and B : E :: D : G, we have A : E :: C : G.

**Step 7.** Again, since A : B :: E : F and C : D :: G : H, and A : B :: C : D, it follows that E : F :: G : H (by 5.11). Therefore by 5.22, since A : E :: C : G (from Step 6) and E : F :: G : H, we have A : F :: C : H.

**Step 8.** But Solid(A) : Solid(B) :: A : F and Solid(C) : Solid(D) :: C : H (from Step 5). Since A : F :: C : H (from Step 7), by 5.11, Solid(A) : Solid(B) :: Solid(C) : Solid(D). This completes the forward direction.

**Step 9.** Conversely, let Solid(A) : Solid(B) :: Solid(C) : Solid(D), where the solids are similar and similarly described on the straight lines A, B, C, D respectively. We must show that A : B :: C : D.

**Step 10.** Construct the same third proportionals as before: let A : B :: B : E :: E : F and C : D :: D : G :: G : H, so that A : F is the triplicate ratio of A : B and C : H is the triplicate ratio of C : D (by D5.10).

**Step 11.** By 11.33, Solid(A) : Solid(B) :: A : F and Solid(C) : Solid(D) :: C : H. Since Solid(A) : Solid(B) :: Solid(C) : Solid(D) (given), by 5.11 we have A : F :: C : H.

**Step 12.** Suppose for contradiction that A : B is not the same ratio as C : D. Then by 5.8, one of the two ratios is greater. Without loss of generality, suppose A has to B a greater ratio than C has to D. Then since A : B :: B : E, and C : D :: D : G, the ratio B : E is greater than D : G (for the ratios are equal to A : B and C : D respectively). By 5.22, since A has to B a greater ratio than C to D, and B has to E a greater ratio than D to G, it follows that A has to E a greater ratio than C has to G.

**Step 13.** Similarly, since A : B :: E : F and C : D :: G : H, the ratio E : F is greater than G : H. Applying 5.22 once more with A : E having a greater ratio than C : G (from Step 12) and E : F having a greater ratio than G : H, we conclude that A has to F a greater ratio than C has to H.

**Step 14.** But this contradicts A : F :: C : H established in Step 11. Therefore our supposition is false, and A : B :: C : D. This completes the converse direction.

**Step 15.** Therefore, if four straight lines be proportional, the similar and similarly described parallelepipedal solids on them are also proportional; and conversely, if the similar and similarly described parallelepipedal solids are proportional, the straight lines are themselves proportional. Q.E.D.

**USED:** 11.33, 5.11, 5.22, 5.8, 6.11, D5.10, D5.9
**Human refs (from References field):** 11.33
**Jaccard:** 0.143 — AI adds ['5.11', '5.22', '5.8', '6.11', 'D5.10', 'D5.9']

## Proposition 11.38
**Statement:** If the sides of the opposite planes of a cube be bisected, and planes be carried through the points of section, the common section of the planes and the diameter of the cube bisect one another.

**Step 1.** Let ABCDEFGH be a cube, where ABCD and EFGH are opposite faces, with edges AE, BF, CG, DH connecting them, so that A is joined to E, B to F, C to G, and D to H. By D11.25, all six faces are equal squares. Let AG be a diameter (space diagonal) of the cube.

**Step 2.** Bisect AB at K, DC at L, EF at M, and HG at N by 1.10. Likewise, bisect AD at O, BC at P, FG at R, and EH at Q by 1.10.

**Step 3.** Draw the plane through K, L, N, M (call it plane alpha), and the plane through O, P, R, Q (call it plane beta). We shall show that the common section of alpha and beta, and the diameter AG, bisect one another.

**Step 4.** We first show that KLNM is a parallelogram. Since ABCD is a square, AB is parallel to DC and AB equals DC. Since K and L are midpoints of AB and DC respectively, KL is parallel to AD (and to BC) by 1.33 applied within the face ABCD. Similarly, since EFGH is a square and M, N are midpoints of EF, HG respectively, MN is parallel to EH (and to FG). Now KM joins the midpoint of AB to the midpoint of EF on face ABFE, and LN joins the midpoint of DC to the midpoint of HG on face DCGH. Since ABFE is a parallelogram with AB parallel to EF and AB equal to EF (all edges of the cube being equal), K is the midpoint of AB and M is the midpoint of EF, so KM is parallel to AE and equal to AE by 6.2 and 1.33. Similarly, LN is parallel to DH and equal to DH. Since AE is parallel to DH and AE equals DH (edges of the cube), KM is parallel to LN and KM equals LN by CN1. Therefore KLNM is a parallelogram by 1.33.

**Step 5.** By the same reasoning, OPRQ is a parallelogram. Since O and P are midpoints of AD and BC on face ABCD, OP is parallel to AB. Since Q and R are midpoints of EH and FG on face EFGH, QR is parallel to EF. Also OQ joins midpoint of AD to midpoint of EH on face ADHE, and PR joins midpoint of BC to midpoint of FG on face BCGF. Since ADHE is a parallelogram with AD parallel to EH, OQ is parallel to AE and equals AE by the same argument as Step 4. Similarly PR is parallel to BF and equals BF. Since AE equals BF and AE is parallel to BF, we have OQ parallel to PR and OQ equal to PR by CN1. Therefore OPRQ is a parallelogram by 1.33.

**Step 6.** Now planes alpha (through KLNM) and beta (through OPRQ) cut one another, so by 11.3 their common section is a straight line. Call this line ST, where S lies on face ABCD and T lies on face EFGH.

**Step 7.** We determine S and T. In face ABCD, the line KL (part of plane alpha) connects the midpoint of AB to the midpoint of DC, and the line OP (part of plane beta) connects the midpoint of AD to the midpoint of BC. Since ABCD is a square, KL and OP are the two lines joining midpoints of opposite sides, and they intersect at the center S of square ABCD. By 1.34, the diagonals AC and BD of parallelogram ABCD bisect each other, and since KL and OP also pass through this center, S is the point where AC and BD bisect each other, that is, S is the midpoint of both AC and BD.

**Step 8.** Similarly, in face EFGH, the line MN (part of plane alpha) and the line QR (part of plane beta) intersect at the center T of square EFGH, which is the midpoint of both EG and FH.

**Step 9.** Now consider the figure ASTG, where A and G are opposite vertices of the cube and S, T are the centers of the opposite faces ABCD and EFGH. Since S is the midpoint of AC (the diagonal of face ABCD), AS equals SC. Since T is the midpoint of EG (the diagonal of face EFGH), GT equals TE.

**Step 10.** We show AS is parallel to TG. Since ABCD is a square, AC is a diagonal. The segment AS goes from A to the midpoint of AC. On face EFGH, the segment TG goes from the midpoint of EG to G. Now consider the parallelogram ACGE: since AE is parallel to CG (both are edges of the cube connecting opposite faces) and AE equals CG, ACGE is a parallelogram by 1.33. By 11.24, opposite faces of a parallelepiped are equal and parallelogrammic, confirming that the quadrilateral through A, C, G, E is a parallelogram.

**Step 11.** In parallelogram ACGE, AC is parallel to EG and AC equals EG by 1.34. Since S is the midpoint of AC and T is the midpoint of EG, the segment ST joins the midpoints of two opposite sides of parallelogram ACGE. Also AS equals half of AC, and TG equals half of EG, so AS equals TG by CN1 (since AC equals EG, their halves are equal by CN3 and the definition of bisection).

**Step 12.** We show AS is parallel to TG. In parallelogram ACGE, since AC is parallel to EG and S divides AC such that AS equals SC, and T divides EG such that ET equals TG, the line segment from A to S has the same direction as the line segment from T to G (both traverse half of a pair of parallel equal lines in corresponding directions). By 6.2, since in triangle ACG (taking CG as a transversal), and considering the parallel EG to AC within the parallelepiped structure, AS is parallel to TG.

**Step 13.** Since AS is equal to TG (Step 11) and AS is parallel to TG (Step 12), the quadrilateral ASTG is a parallelogram by 1.33.

**Step 14.** In parallelogram ASTG, AG and ST are the two diagonals. By 11.2, the two intersecting lines AG and ST determine a plane, and the parallelogram ASTG lies in this plane. By 1.34, in parallelogram ASTG, the diagonal AG bisects it. Consider triangles ASU and GTU, where U is the intersection of diagonals AG and ST. Since AS is parallel to GT (ASTG being a parallelogram), angle SAU equals angle UGT (alternate angles by 1.29), and angle ASU equals angle GTU (alternate angles by 1.29). Also AS equals GT by 1.34. Therefore triangles ASU and GTU are congruent by 1.26 (ASA). Hence AU equals UG and SU equals UT.

**Step 15.** Since AU equals UG, the diameter AG is bisected at U. Since SU equals UT, the common section ST of the two planes is bisected at U. Therefore the common section of the planes and the diameter of the cube bisect one another, which is what was to be proved.

**USED:** 1.10, 1.26, 1.29, 1.33, 1.34, 11.2, 11.24, 11.3, 6.2, CN1, CN3, D11.25
**Human refs (from References field):** 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.9
**Jaccard:** 0.188 — AI adds ['1.10', '1.34', '11.2', '11.24', '11.3', '6.2', 'CN1', 'CN3', 'D11.25']; Human adds ['1.14', '1.15', '1.4', '11.9']

## Proposition 11.39
**Statement:** If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms will be equal.

**Step 1.** Let there be two prisms of equal height h. Let the first prism have a parallelogram ABCD as its base, and let the second prism have a triangle EFG as its base. Let parallelogram ABCD be double triangle EFG. We are to prove the two prisms are equal.

**Step 2.** The first prism is a triangular prism resting on one of its parallelogram faces ABCD, with the opposite edge at perpendicular height h above the base [D11.13]. Complete this prism to a parallelepiped by constructing the parallelepiped with base ABCD and height h. By 11.28, this parallelepiped is bisected by the diagonal plane into two equal triangular prisms, one of which is our first prism. Therefore the first prism equals half of this parallelepiped.

**Step 3.** For the second prism, which has triangular base EFG and height h, complete triangle EFG to a parallelogram EFGH by constructing the point H such that EFGH is a parallelogram. The diagonal of this parallelogram divides it into two equal triangles, one of which is EFG, so parallelogram EFGH equals double triangle EFG [1.34]. Construct the parallelepiped with base EFGH and height h. By 11.28, this parallelepiped is bisected by the diagonal plane into two equal triangular prisms, one of which is the second prism on triangle EFG. Therefore the second prism equals half of this parallelepiped.

**Step 4.** Now compare the two parallelepipeds. The first has base ABCD and height h. The second has base EFGH and height h. By construction, parallelogram EFGH equals double triangle EFG [1.34]. By hypothesis, parallelogram ABCD also equals double triangle EFG. Therefore ABCD equals EFGH [CN1].

**Step 5.** Since the two parallelepipeds have equal bases and equal heights, they are equal to one another [11.31].

**Step 6.** The first prism is half of the first parallelepiped, and the second prism is half of the second parallelepiped [11.28]. Since the two parallelepipeds are equal, their halves are equal. For suppose the halves were unequal; then adding each half to itself, the doubles would be unequal [CN2], contradicting the equality of the parallelepipeds established in Step 5. Therefore the first prism equals the second prism.

**Step 7.** Therefore, if there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms are equal. Q.E.D.

**USED:** 1.34, 11.28, 11.31, CN1, CN2, D11.13
**Human refs (from References field):** 1.34, 11.28, 11.31
**Jaccard:** 0.500 — AI adds ['CN1', 'CN2', 'D11.13']
