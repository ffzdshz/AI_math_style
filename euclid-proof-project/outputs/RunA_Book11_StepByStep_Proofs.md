# Book 11 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 11.1
**Statement:** A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 1.** Suppose, for the sake of contradiction, that a part of a straight line is in the plane of reference and another part is in a plane more elevated. Specifically, let the straight line ABC have the part AB in the reference plane, while the part BC is in a plane more elevated, so that BC is not in the reference plane.

**Step 2.** Since AB is a finite straight line lying in the reference plane, by P2 we can produce AB continuously in a straight line. Let AB be produced in the reference plane to a point D, yielding the straight line ABD. Since AB lies in the reference plane and BD is its continuation within that plane, the entire straight line ABD lies in the reference plane.

**Step 3.** Now by D1.7, a plane surface lies evenly with the straight lines on itself. Since the reference plane is a plane surface and AB lies in it, any straight line produced from AB within the plane lies evenly in that plane. Thus ABD lies entirely in the reference plane, and in particular BD proceeds from B as the unique continuation of AB in a straight line.

**Step 4.** By D1.4, a straight line lies evenly with the points on itself. The straight line ABC, being a single straight line, has the property that the segment from A through B to C lies evenly along one direction. Similarly, ABD lies evenly along one direction from A through B to D. Both BC and BD are produced from point B as continuations of the same segment AB in a straight line.

**Step 5.** By P2, a finite straight line can be produced continuously in a straight line. This production from point B continuing from AB determines a unique direction, since by D1.4 the straight line lies evenly with the points on itself. Therefore the continuation of AB beyond B is unique: the points C and D must lie on the same ray from B, and so BC and BD coincide.

**Step 6.** But BD lies entirely in the reference plane (Step 2), while BC was assumed to be in a more elevated plane and not in the reference plane. This is a contradiction, since BC and BD are the same line segment proceeding from B (Step 5), and a single line segment cannot both lie in the reference plane and not lie in it.

**Step 7.** Therefore the assumption is false, and it is impossible for part of a straight line to be in the plane of reference and another part in a plane more elevated. If any part of a straight line is in the reference plane, the whole of it must be in that plane. Q.E.D.

**USED:** D1.4, D1.7, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D1.4', 'D1.7', 'P2']

## Proposition 11.2
**Statement:** If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

**Step 1.** Let the two straight lines AB and CD cut one another at the point E. We must show that AB and CD are in one plane, and that every triangle is in one plane.

**Step 2.** Take an arbitrary point F on EB and an arbitrary point G on EC. Draw the straight lines CB and FG [P1].

**Step 3.** Consider the triangle ECB, with sides EC, CB, and EB. Suppose, for the sake of contradiction, that triangle ECB is not in one plane. Then some part of triangle ECB lies in a plane, say the plane of reference, and some part lies in a different, more elevated plane.

**Step 4.** If the triangle ECB is not entirely in one plane, then one of its sides, say EC, has a part lying in the plane of reference and a part lying in another plane. But by Proposition 11.1, a part of a straight line cannot be in the plane of reference and a part in a plane more elevated. This is a contradiction. The same argument applies to sides EB and CB. Therefore, triangle ECB lies entirely in one plane [11.1].

**Step 5.** Since EB lies in the plane of triangle ECB and EA is the extension of EB in a straight line [P2], if EA were not in the same plane, then the straight line AB (composed of EA and EB) would have part in the plane and part not in the plane, contradicting 11.1. Therefore EA lies in the same plane as triangle ECB. Hence the whole line AB lies in this plane [11.1, P2].

**Step 6.** By the same reasoning, since EC lies in the plane of triangle ECB and ED is the extension of EC in a straight line [P2], the straight line ED also lies in this plane. Hence the whole line CD lies in the same plane as triangle ECB [11.1, P2].

**Step 7.** Therefore the two straight lines AB and CD lie in one and the same plane, which is the plane of triangle ECB.

**Step 8.** Now let FGH be any triangle, with vertices F, G, H. Draw the straight lines FG, GH, and FH [P1]. Suppose that triangle FGH is not in one plane. Then one of its sides, say FG, would have a part in one plane and a part in another, which contradicts 11.1. The same applies to GH and FH. Therefore every triangle is in one plane [11.1].

**Step 9.** Therefore, if two straight lines cut one another, they are in one plane, and every triangle is in one plane. Q.E.D.

**USED:** 11.1, P1, P2
**Human refs (from References field):** 11.1
**Jaccard:** 0.333 — AI adds ['P1', 'P2']

## Proposition 11.3
**Statement:** If two planes cut one another, their common section is a straight line.

**Step 1.** Let two planes AB and BC cut one another, and let D and B be any two points on their common section.

**Step 2.** From D to B, draw a straight line DEB in the plane AB. [P1]

**Step 3.** From D to B, draw a straight line DFB in the plane BC. [P1]

**Step 4.** Since D and B are points in the plane AB, and DEB is a straight line joining them, the straight line DEB lies entirely in the plane AB. [11.1]

**Step 5.** Since D and B are points in the plane BC, and DFB is a straight line joining them, the straight line DFB lies entirely in the plane BC. [11.1]

**Step 6.** Now if the common section of the two planes were not a straight line, then the straight lines DEB and DFB would be distinct, since one lies in plane AB and the other in plane BC, and the common section between them would not be straight.

**Step 7.** But if DEB and DFB are distinct straight lines having the same endpoints D and B, then two straight lines would enclose a space, which is impossible. [P1]

**Step 8.** Therefore DEB and DFB are not distinct; they are the same straight line. This single straight line lies in both planes (by Steps 4 and 5), and thus it is the common section of the planes.

**Step 9.** Since every two points D and B on the common section are joined by this unique straight line lying in both planes, the common section of the two planes is a straight line. [D1.4]

**Step 10.** Therefore, if two planes cut one another, their common section is a straight line. Q.E.D.

**USED:** 11.1, D1.4, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['11.1', 'D1.4', 'P1']

## Proposition 11.4
**Statement:** If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

**Step 1.** Let AB and CD be two straight lines cutting one another at the point E, and let EF be set up at right angles to both AB and CD at E. I say that EF is also at right angles to the plane through AB and CD. [D11.3]

**Step 2.** Cut off AE equal to EB along line AB from point E, and cut off CE equal to ED along line CD from point E. [1.3]

**Step 3.** Draw any straight line GEH through E in the plane through AB and CD. Join the straight lines AD, BC, AC, BD, AG, BH, GC, DH, AF, BF, CF, DF, GF, and HF. [P1; 11.2]

**Step 4.** Since AE equals EB and CE equals ED, and the angle AEC equals the angle DEB (for they are vertical angles) [1.15], therefore by the SAS criterion the triangles AEC and BED are congruent. Hence AC equals BD and the angle CAE equals the angle DBE. [1.4]

**Step 5.** Since the angle AEG and the angle BEH are vertical angles, the angle AEG equals the angle BEH. [1.15]

**Step 6.** In triangles AGE and BHE, the angle GAE equals the angle HBE (from Step 4), the angle AEG equals the angle BEH (from Step 5), and AE equals BE (by construction). Therefore by the AAS criterion, the triangles AGE and BHE are congruent. Hence GE equals HE, and AG equals BH. [1.26]

**Step 7.** Since AC equals BD (Step 4) and AG equals BH (Step 6), subtracting equals from equals gives GC equals DH. [CN3]

**Step 8.** Since AE equals EB and the angle AEF is a right angle and the angle BEF is a right angle (EF is at right angles to AB), so the angle AEF equals the angle BEF [P4]. In triangles AEF and BEF, AE equals BE, EF is common, and the included angle AEF equals the included angle BEF. By the SAS criterion, AF equals BF. [1.4]

**Step 9.** Since CE equals ED and the angle CEF is a right angle and the angle DEF is a right angle (EF is at right angles to CD), so the angle CEF equals the angle DEF [P4]. In triangles CEF and DEF, CE equals DE, EF is common, and the included angle CEF equals the included angle DEF. By the SAS criterion, CF equals DF. [1.4]

**Step 10.** In triangles ACF and BDF, we have AC equals BD (Step 4), AF equals BF (Step 8), and CF equals DF (Step 9). Therefore by the SSS criterion, the triangles ACF and BDF are congruent, and the angle ACF equals the angle BDF. [1.8]

**Step 11.** In triangles GCF and HDF, we have GC equals DH (Step 7), CF equals DF (Step 9), and the angle GCF equals the angle HDF (Step 10). Therefore by the SAS criterion, the triangles GCF and HDF are congruent. Hence GF equals HF. [1.4]

**Step 12.** In triangles GEF and HEF, we have GE equals HE (Step 6), EF is common, and GF equals HF (Step 11). Therefore by the SSS criterion, the triangles GEF and HEF are congruent. Hence the angle GEF equals the angle HEF. [1.8]

**Step 13.** Since the straight line EF standing on the straight line GH makes the adjacent angles GEF and HEF equal to one another, each of the angles GEF and HEF is a right angle, and EF is perpendicular to GH. [D1.10]

**Step 14.** Since GEH was taken as an arbitrary straight line through E in the plane through AB and CD, EF makes right angles with every straight line which meets it and lies in that plane. Therefore EF is at right angles to the plane through AB and CD. [D11.3]

**USED:** 1.15, 1.26, 1.3, 1.4, 1.8, 11.2, CN3, D1.10, D11.3, P1, P4
**Human refs (from References field):** 1.15, 1.26, 1.4, 1.8, D11.3
**Jaccard:** 0.455 — AI adds ['1.3', '11.2', 'CN3', 'D1.10', 'P1', 'P4']

## Proposition 11.5
**Statement:** If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

**Step 1.** Let the straight line AB be set up at right angles to three straight lines BC, BD, and BE at their common point of section B. We must show that BC, BD, and BE are in one plane.

**Step 2.** Since AB is at right angles to each of BC and BD, and BC and BD are two straight lines cutting one another at B, by 11.4, AB is at right angles to the plane through BC and BD. Call this plane alpha.

**Step 3.** Suppose, for the sake of contradiction, that BE is not in plane alpha. Consider the plane containing AB and BE. This plane and plane alpha are two planes that meet (since they share at least the point B). By 11.3, their common section is a straight line. Let BF be this common section, so BF is a straight line lying in plane alpha that also lies in the plane through AB and BE.

**Step 4.** Since AB is at right angles to plane alpha (Step 2), and BF is a straight line in plane alpha meeting AB at B, then by D11.3 the angle ABF is a right angle.

**Step 5.** But AB is at right angles to BE (given), so the angle ABE is also a right angle.

**Step 6.** Now AB, BE, and BF all lie in one plane (the plane through AB and BE from Step 3). In this plane, BF and BE are both drawn from point B, and each makes a right angle with AB. By P4, angle ABF equals angle ABE.

**Step 7.** But since BE is not in plane alpha (by our supposition) while BF is in plane alpha, BF and BE are distinct lines from B. Since BF lies in the plane through AB and BE, and BF is distinct from BE, one of the angles ABF and ABE is a proper part of the other. By CN5, the whole is greater than the part, so the greater angle cannot equal the lesser. This contradicts the equality established in Step 6.

**Step 8.** Therefore the supposition is false, and BE lies in plane alpha, the plane through BC and BD.

**Step 9.** Hence BC, BD, and BE are all in one plane, which is what was to be proved.

**USED:** 11.3, 11.4, CN5, D11.3, P4
**Human refs (from References field):** 11.3, 11.4, D11.3
**Jaccard:** 0.600 — AI adds ['CN5', 'P4']

## Proposition 11.6
**Statement:** If two straight lines be at right angles to the same plane, the straight lines will be parallel.

**Step 1.** Let AB and CD be two straight lines at right angles to the same plane P, meeting it at points B and D respectively. We must show that AB and CD are parallel.

**Step 2.** Join BD [P1]. In plane P, at point D, draw DE at right angles to BD [1.11], and cut off DE equal to AB [1.3]. Join BE, AE, and AD [P1].

**Step 3.** Since AB is at right angles to plane P, it makes right angles with all straight lines meeting it that lie in the plane [D11.3]. Both BD and BE lie in plane P and pass through B, so angle ABD and angle ABE are both right angles.

**Step 4.** Similarly, since CD is at right angles to plane P, it makes right angles with all lines through D in the plane [D11.3]. In particular, angle CDB and angle CDE are both right angles.

**Step 5.** In triangle ABD, since angle ABD is a right angle, we have AD squared equals AB squared plus BD squared [1.47].

**Step 6.** In triangle BDE, since angle BDE is a right angle (by construction), we have BE squared equals BD squared plus DE squared [1.47].

**Step 7.** Since DE equals AB (by construction), we may substitute to obtain BE squared equals BD squared plus AB squared. But AD squared also equals AB squared plus BD squared (Step 5). Therefore AD squared equals BE squared [CN1], and hence AD equals BE.

**Step 8.** In triangle ABE, since angle ABE is a right angle (Step 3), we have AE squared equals AB squared plus BE squared [1.47]. Substituting BE squared equals BD squared plus DE squared (Step 6), we get AE squared equals AB squared plus BD squared plus DE squared.

**Step 9.** But AD squared equals AB squared plus BD squared (Step 5), so AB squared plus BD squared plus DE squared equals AD squared plus DE squared [CN1]. Therefore AE squared equals AD squared plus DE squared.

**Step 10.** Since AE squared equals AD squared plus DE squared, by the converse of the Pythagorean theorem the angle ADE is a right angle [1.48]. That is, DE is at right angles to AD.

**Step 11.** We have now established that DE is at right angles to three straight lines at their common point D: to BD (by construction), to AD (Step 10), and to CD (Step 4, since CD is at right angles to plane P and DE lies in the plane through D). By Proposition 11.5, the three lines BD, AD, and CD all lie in one plane [11.5].

**Step 12.** Since BD and AD lie in this plane, the points B and A both lie in this plane. Therefore the straight line AB lies entirely in this plane. Likewise CD lies in this plane. Hence AB and CD are coplanar.

**Step 13.** The straight line BD falls on the two straight lines AB and CD in this plane. The angle ABD is a right angle (Step 3) and the angle CDB is a right angle (Step 4). Since all right angles are equal to one another [P4], the sum of the interior angles ABD and CDB on the same side of BD equals two right angles. Therefore AB is parallel to CD [1.28].

**USED:** 1.11, 1.28, 1.3, 1.47, 1.48, 11.5, CN1, D11.3, P1, P4
**Human refs (from References field):** 1.28, 1.4, 1.8, 11.2, 11.5, D11.3
**Jaccard:** 0.231 — AI adds ['1.11', '1.3', '1.47', '1.48', 'CN1', 'P1', 'P4']; Human adds ['1.4', '1.8', '11.2']

## Proposition 11.7
**Statement:** If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

**Step 1.** Let AB and CD be two parallel straight lines. By the definition of parallel lines (D1.23), AB and CD lie in the same plane. Call this plane P.

**Step 2.** Let E be a point taken at random on AB, and F a point taken at random on CD. Join E to F by a straight line EF (P1).

**Step 3.** Since AB lies in plane P, and E is a point on AB, the point E lies in plane P. Similarly, since CD lies in plane P, and F is a point on CD, the point F lies in plane P.

**Step 4.** Now, since both endpoints E and F of the straight line EF lie in plane P, suppose for contradiction that EF does not lie entirely in plane P. Then some part of EF would lie in plane P (since E and F are in plane P, at least the parts of EF at E and at F are in or on the boundary of plane P), while another part of EF would lie in a plane more elevated than P. But this contradicts Proposition 11.1, which states that a part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 5.** Therefore the straight line EF lies entirely in plane P, which is the same plane that contains the parallel straight lines AB and CD. Hence the straight line joining points E and F is in the same plane with the parallel straight lines AB and CD. Q.E.D.

**USED:** 11.1, D1.23, P1
**Human refs (from References field):** 11.3
**Jaccard:** 0.000 — AI adds ['11.1', 'D1.23', 'P1']; Human adds ['11.3']

## Proposition 11.8
**Statement:** If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

**Step 1.** Let AB and CD be two parallel straight lines, and let AB be at right angles to the plane P. We must show that CD is also at right angles to the plane P. Let B be the point where AB meets (or is based at) the plane P, and let D be a point of CD in (or at) the plane P.

**Step 2.** Join BD [P1]. Since BD lies in the plane P and passes through B, and AB is at right angles to the plane P, the angle ABD is a right angle [D11.3].

**Step 3.** Since AB is parallel to CD, and BD falls on them as a transversal, the co-interior angles ABD and CDB are together equal to two right angles [1.29]. Since angle ABD is a right angle, angle CDB is also a right angle.

**Step 4.** In the plane P, draw DE at right angles to BD at the point D [1.11]. Cut off DE equal to AB [1.3].

**Step 5.** Join BE, AE, and AD [P1]. Since BE lies in plane P and passes through B, and AB is at right angles to plane P, the angle ABE is a right angle [D11.3].

**Step 6.** In the right triangle ABD (right angle at B), we have AD squared equals AB squared plus BD squared [1.47].

**Step 7.** In the right triangle BDE (right angle at D, since DE was drawn perpendicular to BD), we have BE squared equals BD squared plus DE squared [1.47].

**Step 8.** Since DE equals AB [Step 4], we may substitute to obtain BE squared equals BD squared plus AB squared. Therefore BE squared equals AD squared [Step 6, CN1]. Hence BE equals AD.

**Step 9.** In the right triangle ABE (right angle at B), we have AE squared equals AB squared plus BE squared [1.47]. Since BE squared equals BD squared plus DE squared [Step 7], we obtain AE squared equals AB squared plus BD squared plus DE squared.

**Step 10.** But AB squared plus BD squared equals AD squared [Step 6]. Therefore AE squared equals AD squared plus DE squared [CN1].

**Step 11.** Since AE squared equals AD squared plus DE squared, by the converse of the Pythagorean theorem the angle ADE is a right angle [1.48].

**Step 12.** Now DE is at right angles to BD [Step 4] and DE is at right angles to AD [Step 11]. Since BD and AD are two straight lines meeting at D, and DE is at right angles to both of them at their point of intersection, DE is at right angles to the plane through BD and AD [11.4].

**Step 13.** The plane through BD and AD contains the line AB (since A and B are both in this plane) and also contains the line CD, because AB and CD are parallel and the plane already contains AB and the point D (which lies on CD), so the line through D parallel to AB lies in this plane [11.7, since AB and CD are parallel and B, D are points on them respectively, BD lies in the same plane as AB and CD].

**Step 14.** Since DE is at right angles to the plane through BD and AD, and CD lies in that plane, DE is at right angles to CD at D [D11.3]. That is, angle CDE is a right angle.

**Step 15.** We have now established that CD is at right angles to BD [Step 3] and CD is at right angles to DE [Step 14]. Since BD and DE are two straight lines in the plane P that meet at D, and CD is at right angles to both of them at their point of intersection, CD is at right angles to the plane P [11.4].

**Step 16.** Therefore, if two straight lines are parallel and one of them is at right angles to a plane, the remaining one is also at right angles to the same plane. Q.E.D.

**USED:** 1.11, 1.29, 1.3, 1.47, 1.48, 11.4, 11.7, CN1, D11.3, P1
**Human refs (from References field):** 1.29, 11.2, 11.4, 11.7, D11.3
**Jaccard:** 0.364 — AI adds ['1.11', '1.3', '1.47', '1.48', 'CN1', 'P1']; Human adds ['11.2']

## Proposition 11.9
**Statement:** Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

**Step 1.** Let AB be parallel to EF, and let CD be parallel to EF, where AB and CD are not in the same plane as EF. We must show that AB is parallel to CD.

**Step 2.** Let G be any point on EF. In the plane containing EF and AB, draw GH from G perpendicular to EF (by 1.11). In the plane containing EF and CD, draw GK from G perpendicular to EF (by 1.11).

**Step 3.** Since AB is parallel to EF, and GH is drawn in the plane of AB and EF perpendicular to EF at G, GH is also perpendicular to AB (by 1.29, since the alternate interior angles or corresponding angles formed show that GH meets AB at right angles). More precisely: since EF is parallel to AB, and GH is perpendicular to EF, then GH is perpendicular to AB. This follows because by 1.29, since EF is parallel to AB and GH falls on them, the alternate angles are equal; since the angle at G with EF is a right angle, the angle at H with AB is also a right angle.

**Step 4.** By the same reasoning, since EF is parallel to CD and GK is perpendicular to EF in the plane of EF and CD, GK is also perpendicular to CD (by 1.29).

**Step 5.** Since GH is perpendicular to EF at G, and GK is perpendicular to EF at G, the straight line GH lies in the plane through EF and AB, and GK lies in the plane through EF and CD. Now, since GH is at right angles to EF and GK is at right angles to EF, both at the point G, we have that EF is at right angles to both GH and GK at G.

**Step 6.** Therefore, EF is at right angles to the plane through GH and GK (by 11.4, since EF is perpendicular to two straight lines GH and GK that meet at G and lie in the plane through GH and GK).

**Step 7.** Since EF is at right angles to the plane through GH and GK, and AB is parallel to EF, then AB is also at right angles to the plane through GH and GK (by 11.8, since if two straight lines are parallel and one is at right angles to a plane, the other is also at right angles to the same plane).

**Step 8.** By the same reasoning, since CD is parallel to EF and EF is at right angles to the plane through GH and GK, CD is also at right angles to the plane through GH and GK (by 11.8).

**Step 9.** Therefore, AB and CD are both at right angles to the same plane, namely the plane through GH and GK. Hence AB is parallel to CD (by 11.6, since two straight lines at right angles to the same plane are parallel).

**USED:** 1.11, 1.29, 11.4, 11.6, 11.8
**Human refs (from References field):** 11.4, 11.6, 11.8
**Jaccard:** 0.600 — AI adds ['1.11', '1.29']

## Proposition 11.10
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.

**Step 1.** Let AB, BC be two straight lines meeting one another at B, and let DE, EF be two straight lines meeting one another at E, such that AB is parallel to DE and BC is parallel to EF, and these pairs are not in the same plane. We must prove that angle ABC equals angle DEF.

**Step 2.** On BA, cut off BG equal to ED, and on BC, cut off BH equal to EF. [1.3] Join GH, AD (i.e., G to H), and similarly join the corresponding points. More precisely: set BG = ED along BA, and BH = EF along BC. Join GH. [P1]

**Step 3.** Since BG is parallel to ED (being part of the line AB which is parallel to DE) and BG = ED, join GD and BE. [P1] Since BG and ED are parallel and equal, and the four points B, G, D, E lie in one plane (by 11.7, since BG is parallel to ED and the straight line joining points on them lies in the same plane as the parallels), by 1.33 the straight lines GD and BE joining their extremities in the same direction are equal and parallel. Thus GD = BE and GD is parallel to BE.

**Step 4.** Since BH is parallel to EF (being part of the line BC which is parallel to EF) and BH = EF, join HF and BE. [P1] Since BH and EF are parallel and equal, and the four points B, H, F, E lie in one plane (by 11.7), by 1.33 the straight lines HF and BE joining their extremities in the same direction are equal and parallel. Thus HF = BE and HF is parallel to BE.

**Step 5.** Since GD and HF are each parallel to BE, and GD and HF are not in the same plane as BE (for the original lines are not in the same plane), by 11.9 GD is parallel to HF. Moreover, GD = BE and HF = BE, so GD = HF. [CN1]

**Step 6.** Since GD is parallel to HF and GD = HF, and the four points G, D, F, H lie in one plane (by 11.7, since GD is parallel to HF), by 1.33 the straight lines GH and DF joining their extremities in the same direction are equal and parallel. Thus GH = DF.

**Step 7.** Now in triangles GBH and DEF, we have BG = ED (by construction), BH = EF (by construction), and GH = DF (from Step 6). Therefore by 1.8 (SSS congruence), triangle GBH is congruent to triangle DEF, and in particular angle GBH equals angle DEF.

**Step 8.** But angle GBH is the same as angle ABC (since G lies on ray BA and H lies on ray BC). Therefore angle ABC equals angle DEF, which was to be proved.

**USED:** 1.3, 1.33, 1.8, 11.7, 11.9, CN1, P1
**Human refs (from References field):** 1.33, 1.8, 11.9
**Jaccard:** 0.429 — AI adds ['1.3', '11.7', 'CN1', 'P1']

## Proposition 11.11
**Statement:** From a given elevated point to draw a straight line perpendicular to a given plane.

**Step 1.** Let A be the given elevated point, and let the reference plane be the given plane. Draw any straight line BC in the given plane.

**Step 2.** From the point A, draw AD perpendicular to BC [1.12]. Then D is a point on BC lying in the given plane.

**Step 3.** If AD is at right angles to the given plane, then the required construction is complete. Suppose it is not; then proceed as follows.

**Step 4.** From the point D, draw DE in the given plane at right angles to BC [1.11].

**Step 5.** From the point A, draw AF perpendicular to DE [1.12]. Then F is a point on DE lying in the given plane.

**Step 6.** Through the point F, draw GH in the given plane parallel to BC [1.31].

**Step 7.** Since AD is perpendicular to BC (Step 2) and DE is perpendicular to BC (Step 4), the line BC is at right angles to both DA and DE at their common point D. Therefore BC is at right angles to the plane through ED and DA [11.4].

**Step 8.** Since GH is parallel to BC (Step 6) and BC is at right angles to the plane through ED and DA (Step 7), GH is also at right angles to the plane through ED and DA [11.8].

**Step 9.** Since GH is at right angles to the plane through ED and DA, GH makes right angles with every straight line which meets it and lies in that plane [D11.3]. Now AF lies in the plane through ED and DA (since A, D, E, and F are all in that plane) and meets GH at the point F. Therefore the angle AFG (equivalently AFH) is a right angle.

**Step 10.** AF is also at right angles to DE by construction (Step 5). Therefore AF is at right angles to both GH and DE, two straight lines which cut one another at F in the given plane.

**Step 11.** Since AF is at right angles to both GH and DE at their point of intersection F, AF is at right angles to the plane through GH and DE [11.4]. But GH and DE both lie in the given plane and intersect at F, so the plane through them is the given plane.

**Step 12.** Therefore AF is a straight line drawn from the given elevated point A perpendicular to the given plane, which is what was required to be done.

**USED:** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3
**Human refs (from References field):** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3
**Jaccard:** 1.000 — Perfect match.

## Proposition 11.12
**Statement:** To set up a straight line at right angles to a given plane from a given point in it.

**Step 1.** Let A be the given point in the given plane P. We are required to set up from A a straight line at right angles to plane P.

**Step 2.** Let B be a point not in the plane P (that is, an elevated point relative to P).

**Step 3.** From the elevated point B, draw a straight line perpendicular to the plane P by 11.11. Let BC be this perpendicular, with C the foot in the plane P. Then BC is at right angles to every straight line meeting it that lies in P, by D11.3.

**Step 4.** If C coincides with A, then BA is itself at right angles to the plane P, and the construction is complete. Assume then that C does not coincide with A.

**Step 5.** Since C is in plane P and A is in plane P, draw the straight line CA by P1. Through the point A, draw the straight line AD parallel to BC by 1.31. (Here AD is constructed in the plane through A and BC, parallel to BC.)

**Step 6.** Since BC is at right angles to the plane P, and AD is parallel to BC, it follows by 11.8 that AD is also at right angles to the plane P.

**Step 7.** Therefore AD has been set up from the given point A at right angles to the given plane P, which is what was required to be done.

**USED:** 1.31, 11.11, 11.8, D11.3, P1
**Human refs (from References field):** 1.31, 11.11, 11.8
**Jaccard:** 0.600 — AI adds ['D11.3', 'P1']

## Proposition 11.13
**Statement:** From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

**Step 1.** Suppose, for the sake of contradiction, that from the same point A two distinct straight lines AB and AC are both set up at right angles to the same plane P, on the same side of that plane.

**Step 2.** Since AB and AC are two straight lines meeting at A, by 11.2, they lie in one plane, call it Q.

**Step 3.** Since planes P and Q both exist and intersect (they share at least the point A, and the plane P contains points not in Q since AB is not in P), by 11.3 their common section is a straight line. Let this line of intersection be DAE, passing through A and lying in plane P.

**Step 4.** Since AB is at right angles to the plane P, by D11.3, AB makes right angles with every straight line that meets it and lies in plane P. In particular, since DAE lies in plane P and meets AB at A, the angle BAD is a right angle, and the angle BAE is a right angle.

**Step 5.** Similarly, since AC is at right angles to the plane P, by D11.3, AC makes right angles with every straight line that meets it and lies in plane P. In particular, since DAE lies in plane P and meets AC at A, the angle CAD is a right angle, and the angle CAE is a right angle.

**Step 6.** Now consider the configuration in the single plane Q. The lines AB, AC, and DAE all lie in plane Q. The line DAE passes through A. Both AB and AC are on the same side of line DAE (since they are on the same side of plane P, and DAE lies in plane P).

**Step 7.** Since angle BAD is a right angle (Step 4) and angle CAD is a right angle (Step 5), and AB and AC are on the same side of line DAE, we have angle BAD equals angle CAD, both being right angles, by P4.

**Step 8.** But since AB and AC are distinct lines from A on the same side of DAE, one of them, say AC, lies in the interior of angle BAD (or AB lies in the interior of angle CAD). Therefore angle CAD is a proper part of angle BAD (or vice versa).

**Step 9.** By CN5, the whole is greater than the part. So angle BAD is greater than angle CAD (or vice versa). But this contradicts Step 7, where we established that angle BAD equals angle CAD.

**Step 10.** Therefore the assumption is false, and from the same point two straight lines cannot be set up at right angles to the same plane on the same side. Q.E.D.

**USED:** 11.2, 11.3, CN5, D11.3, P4
**Human refs (from References field):** 11.3, D11.3
**Jaccard:** 0.400 — AI adds ['11.2', 'CN5', 'P4']

## Proposition 11.14
**Statement:** Planes to which the same straight line is at right angles will be parallel.

**Step 1.** Let the straight line AB be at right angles to each of the planes P and Q, meeting plane P at A and plane Q at B. We wish to show that P and Q are parallel.

**Step 2.** Suppose, for the sake of contradiction, that planes P and Q are not parallel. Then by the definition of parallel planes (D11.8), they meet one another.

**Step 3.** Since the two planes meet, their common section is a straight line; call it DE. [11.3]

**Step 4.** Take any point F on the line DE. Join AF and BF. [P1] Since A lies in plane P and F lies on DE which is in plane P, the line AF lies in plane P. Since B lies in plane Q and F lies on DE which is in plane Q, the line BF lies in plane Q.

**Step 5.** We claim that A, B, and F are not collinear, so that triangle ABF exists. Since AB is at right angles to plane P, it meets plane P only at A; since AB is at right angles to plane Q, it meets plane Q only at B. If F were on line AB, then F would lie in both plane P and plane Q, giving F = A (the only intersection of AB with P) and F = B (the only intersection of AB with Q), hence A = B, which is impossible since AB is a straight line of positive length. Therefore A, B, F are non-collinear and triangle ABF exists. By 11.2, this triangle lies in one plane.

**Step 6.** Since AB is at right angles to plane P, it makes right angles with all straight lines that meet it and lie in plane P (D11.3). The line AF meets AB at A and lies in plane P, so angle BAF is a right angle.

**Step 7.** Since AB is at right angles to plane Q, it makes right angles with all straight lines that meet it and lie in plane Q (D11.3). The line BF meets AB at B and lies in plane Q, so angle ABF is a right angle.

**Step 8.** In triangle ABF, the two angles BAF and ABF are each right angles, so together they equal two right angles. But by 1.17, any two angles of a triangle taken together are less than two right angles. This is a contradiction.

**Step 9.** Therefore the assumption that planes P and Q meet is false. Hence P and Q do not meet, and by definition (D11.8) they are parallel. Q.E.D.

**USED:** 1.17, 11.2, 11.3, D11.3, D11.8, P1
**Human refs (from References field):** 1.17, 11.3, D11.3, D11.8
**Jaccard:** 0.667 — AI adds ['11.2', 'P1']

## Proposition 11.15
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

**Step 1.** Let AB and BC be two straight lines meeting one another at B, and let DE and EF be two straight lines meeting one another at E, such that AB is parallel to DE and BC is parallel to EF, with AB, BC not in the same plane as DE, EF. We must show that the plane through AB, BC is parallel to the plane through DE, EF.

**Step 2.** From the point B, draw BG perpendicular to the plane through DE, EF [11.11]. Let G be the point where BG meets that plane.

**Step 3.** Through G, in the plane through DE, EF, draw GH parallel to ED, and draw GK parallel to EF [1.31].

**Step 4.** Since BG is at right angles to the plane through DE, EF, BG makes right angles with all straight lines which meet it and lie in that plane [D11.3]. Therefore angle BGH is a right angle and angle BGK is a right angle.

**Step 5.** Now AB is parallel to DE (given), and GH is parallel to DE (construction). Since AB and GH are each parallel to DE, and AB is not in the same plane as DE, then AB is parallel to GH [11.9].

**Step 6.** Similarly, BC is parallel to EF (given), and GK is parallel to EF (construction). Since BC and GK are each parallel to EF, and BC is not in the same plane as EF, then BC is parallel to GK [11.9].

**Step 7.** Since AB is parallel to GH, and BG is a straight line falling on them, the interior angles on the same side, namely angle ABG and angle BGH, are together equal to two right angles [1.29]. But angle BGH is a right angle (Step 4). Therefore angle ABG is a right angle.

**Step 8.** Similarly, since BC is parallel to GK, and BG is a straight line falling on them, the interior angles on the same side, namely angle CBG and angle BGK, are together equal to two right angles [1.29]. But angle BGK is a right angle (Step 4). Therefore angle CBG is a right angle.

**Step 9.** Thus BG is at right angles to both BA and BC at their point of intersection B. Since BA and BC are two straight lines which cut one another at B, and BG is at right angles to each of them, BG is at right angles to the plane through BA and BC [11.4].

**Step 10.** But BG is also at right angles to the plane through DE, EF (Step 2). Therefore BG is at right angles to both the plane through AB, BC and the plane through DE, EF.

**Step 11.** Since the same straight line BG is at right angles to both planes, the plane through AB, BC is parallel to the plane through DE, EF [11.14].

**Step 12.** Therefore, if two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel. Q.E.D.

**USED:** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Human refs (from References field):** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Jaccard:** 1.000 — Perfect match.

## Proposition 11.16
**Statement:** If two parallel planes be cut by any plane, their common sections are parallel.

**Step 1.** Let planes P and Q be parallel, and let them be cut by another plane R. Let the common section of R with P be the line EF, and the common section of R with Q be the line GH. We must show that EF is parallel to GH.

**Step 2.** Since two planes P and R cut one another, their common section EF is a straight line, by 11.3. Likewise, since planes Q and R cut one another, their common section GH is a straight line, by 11.3.

**Step 3.** Both EF and GH lie in the cutting plane R, since each is a common section of R with another plane.

**Step 4.** Suppose, for the sake of contradiction, that EF and GH meet at some point K. Since EF is the common section of planes P and R, the point K lies in plane P. Since GH is the common section of planes Q and R, the point K also lies in plane Q. Therefore K is a point common to both planes P and Q, so they meet at K.

**Step 5.** But P and Q are parallel planes, which by definition (D11.8) do not meet. This is a contradiction. Therefore EF and GH do not meet.

**Step 6.** Since EF and GH are straight lines that lie in the same plane R and do not meet one another, they are parallel by definition (D1.23).

**Step 7.** Therefore, if two parallel planes be cut by any plane, their common sections are parallel. Q.E.D.

**USED:** 11.3, D1.23, D11.8
**Human refs (from References field):** 11.1, D1.23
**Jaccard:** 0.250 — AI adds ['11.3', 'D11.8']; Human adds ['11.1']

## Proposition 11.17
**Statement:** If two straight lines be cut by parallel planes, they will be cut in the same ratios.

**Step 1.** Let the two straight lines AB and CD be cut by three parallel planes P1, P2, and P3. Let A and C lie in P1, E and F in P2, and B and D in P3. We are to prove that AE:EB = CF:FD.

**Step 2.** Join AD [P1]. Let AD meet the plane P2 at point G. Join EG and GF [P1]. Also join AC (lying in P1) and BD (lying in P3).

**Step 3.** Consider the triangle ABD. The vertices A is in P1, B is in P3, and D is in P3. The plane of triangle ABD cuts the parallel planes P2 and P3. The common section with P2 is the line EG (since both E and G lie in P2 and in the plane of triangle ABD), and the common section with P3 is the line BD (since both B and D lie in P3 and in the plane of triangle ABD). By 11.16, since P2 and P3 are parallel, EG is parallel to BD.

**Step 4.** In triangle ABD, since EG is parallel to BD, and EG cuts side AB at E and side AD at G, by 6.2 the sides are cut proportionally: AE:EB = AG:GD.

**Step 5.** Now consider the triangle ACD. The vertices A is in P1, C is in P1, and D is in P3. The plane of triangle ACD cuts the parallel planes P1 and P2. The common section with P1 is the line AC (since both A and C lie in P1 and in the plane of triangle ACD), and the common section with P2 is the line GF (since both G and F lie in P2 and in the plane of triangle ACD). By 11.16, since P1 and P2 are parallel, GF is parallel to AC.

**Step 6.** In triangle ACD, since GF is parallel to AC, and GF cuts side CD at F and side AD at G, by 6.2 the sides are cut proportionally: CF:FD = AG:GD.

**Step 7.** From Step 4, AE:EB = AG:GD. From Step 6, CF:FD = AG:GD. Since both ratios AE:EB and CF:FD are equal to the same ratio AG:GD, by 5.11 we conclude AE:EB = CF:FD.

**Step 8.** Therefore, if two straight lines be cut by parallel planes, they will be cut in the same ratios. Q.E.D.

**USED:** 11.16, 5.11, 6.2, P1
**Human refs (from References field):** 11.16, 5.11, 6.2
**Jaccard:** 0.750 — AI adds ['P1']

## Proposition 11.18
**Statement:** If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

**Step 1.** Let the straight line AB be at right angles to the reference plane P, meeting it at point A. Let Q be any plane passing through AB. We must show that Q is at right angles to P.

**Step 2.** Since AB meets the plane P at A and lies in plane Q, and since both planes P and Q pass through the point A, the two planes P and Q cut one another. By 11.3, their common section is a straight line. Let this common section be the line CE, which passes through A.

**Step 3.** Take any point F on CE (distinct from A). At the point A on the straight line CE, draw the straight line AG in plane P perpendicular to CE, by 1.11.

**Step 4.** Since AB is at right angles to the plane P, by D11.3, AB makes right angles with every straight line which meets it and lies in P. The line CE lies in plane P (being the common section of P and Q) and meets AB at A. Therefore AB is at right angles to CE at A.

**Step 5.** Similarly, AG lies in plane P and meets AB at A. Therefore AB is at right angles to AG at A, again by D11.3.

**Step 6.** Now consider the line AG at point A. We have shown that AG is at right angles to CE (Step 3, by construction) and AG is at right angles to AB (Step 5). The lines CE and AB are two straight lines which meet at A and both lie in plane Q (CE is the common section lying in Q, and AB lies in Q by hypothesis).

**Step 7.** Since AG is at right angles to the two straight lines AB and CE which meet one another at A and lie in plane Q, by 11.4, AG is at right angles to the plane Q.

**Step 8.** Thus AG is a straight line drawn in plane P, at right angles to the common section CE of the planes P and Q, and AG has been shown to be at right angles to the remaining plane Q. Therefore, by D11.4, the plane P is at right angles to the plane Q.

**Step 9.** Since Q was taken as an arbitrary plane through AB, every plane through AB is at right angles to P. Therefore, if a straight line be at right angles to any plane, all the planes through it are also at right angles to the same plane. Q.E.D.

**USED:** 1.11, 11.3, 11.4, D11.3, D11.4
**Human refs (from References field):** 1.11, 1.28, 11.8, D11.3, D11.4
**Jaccard:** 0.429 — AI adds ['11.3', '11.4']; Human adds ['1.28', '11.8']

## Proposition 11.19
**Statement:** If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

**Step 1.** Let the two planes AB and BC be each at right angles to a reference plane P, and let them cut one another. By 11.3, their common section is a straight line; call it BD.

**Step 2.** Let B be a point on BD that lies in plane P (where the common section BD meets P). By 11.3, the common section of plane AB with plane P is a straight line; call it BE. Likewise, the common section of plane BC with plane P is a straight line; call it BF.

**Step 3.** In plane AB, at the point B, draw the straight line BG at right angles to BE (by 1.11). Since the plane AB is at right angles to the plane P, and BG has been drawn in plane AB at right angles to their common section BE, then by D11.4, BG is at right angles to the plane P.

**Step 4.** Similarly, in plane BC, at the point B, draw the straight line BH at right angles to BF (by 1.11). Since the plane BC is at right angles to the plane P, and BH has been drawn in plane BC at right angles to their common section BF, then by D11.4, BH is at right angles to the plane P.

**Step 5.** Thus from the point B, two straight lines BG and BH have both been set up at right angles to the plane P on the same side. But by 11.13, from the same point two straight lines cannot be set up at right angles to the same plane on the same side. Therefore BG and BH must be one and the same straight line.

**Step 6.** Since BG lies in plane AB and BH lies in plane BC, and BG coincides with BH, this single line lies in both planes AB and BC. But the common section of planes AB and BC is the line BD (by 11.3). Therefore this perpendicular line is the line BD itself.

**Step 7.** Since BD is at right angles to the plane P (being identical with BG, which was shown perpendicular to P in Step 3), the common section of the two planes is at right angles to the reference plane. Q.E.D.

**USED:** 1.11, 11.13, 11.3, D11.4
**Human refs (from References field):** 11.13, D11.4
**Jaccard:** 0.500 — AI adds ['1.11', '11.3']

## Proposition 11.20
**Statement:** If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

**Step 1.** Let the solid angle at A be contained by the three plane angles BAC, CAD, and DAB. We are to prove that any two of these angles taken together are greater than the remaining one.

**Step 2.** If the three plane angles are all equal, then any two together are double the remaining one and hence greater than it. The result holds immediately.

**Step 3.** If the three angles are not all equal, let angle BAC be the greatest (or one of the greatest). Since angle BAC is the greatest, the sum of the other two, angle CAD + angle DAB, is the pair we must show exceeds angle BAC. (The other two pairings each include angle BAC, which is the greatest, so those sums trivially exceed the remaining angle.)

**Step 4.** In the plane of angle BAC, construct the angle BAE equal to angle DAB, with E on the same side of AB as C, using P1 and 1.23.

**Step 5.** Take a point D on AD at any distance from A. Along ray AE, cut off AE equal to AD, by 1.3.

**Step 6.** Draw line BED through B and E, meeting AB extended if necessary. More precisely, let a straight line from B through E meet AC at some point; but we proceed as follows. Draw BE by P1.

**Step 7.** In triangles DAB and EAB, we have AD = AE (by construction in Step 5), AB is common, and angle DAB = angle BAE (by construction in Step 4). Therefore, by 1.4 (side-angle-side), triangle DAB is congruent to triangle EAB, so DB = EB and angle ABD = angle ABE.

**Step 8.** Now in triangle BDC, we have BD + DC > BC, by 1.20 (the triangle inequality). Similarly, since we constructed the line through B, E, and considering the triangle BEC or the line through these points, we use the segments along BC.

**Step 9.** Let the line through B and E meet the line AC at a point; call the intersection point G on segment AC (or its extension). Alternatively, we proceed directly: draw line BC and line DC by P1. In triangle BDC, by 1.20, we have BD + DC > BC.

**Step 10.** Since DB = EB (from Step 7), we substitute to get EB + DC > BC. Hence DC > BC - EB, that is, DC > EC (where E lies between B and C on line BC, so BC = BE + EC, giving EC = BC - BE). Thus DC > EC.

**Step 11.** Now consider triangles DAC and EAC. We have AD = AE (Step 5), AC is common, and DC > EC (Step 10). By 1.25 (if two triangles have two sides equal respectively and the base of one greater than the base of the other, the angle contained by the equal sides of the first is greater than the corresponding angle of the second), angle DAC > angle EAC.

**Step 12.** From Step 4, angle BAE = angle DAB. Adding angle EAC to angle BAE gives angle BAE + angle EAC = angle BAC (since E is interior to angle BAC). Therefore angle DAB + angle EAC = angle BAC.

**Step 13.** Since angle DAC > angle EAC (Step 11), we have angle DAB + angle DAC > angle DAB + angle EAC = angle BAC.

**Step 14.** Therefore angle DAB + angle DAC > angle BAC, which proves that the sum of any two of the three plane angles is greater than the remaining one. This completes the proof.

**USED:** 1.20, 1.23, 1.25, 1.3, 1.4, P1
**Human refs (from References field):** 1.20, 1.25, 1.4
**Jaccard:** 0.500 — AI adds ['1.23', '1.3', 'P1']

## Proposition 11.21
**Statement:** Any solid angle is contained by plane angles less than four right angles.

**Step 1.** Let the solid angle at vertex A be contained by the plane angles BAC, CAD, DAE, ..., EAB, where there are n such face angles (n >= 3), and the edges AB, AC, AD, AE, ... emanate from A. We must show that the sum of these plane angles is less than four right angles.

**Step 2.** Let the edges AB, AC, AD, AE, ..., be cut by a plane, producing the convex polygon BCDE... with n sides as the cross-section [P1]. The edges AB, AC, AD, etc. meet this plane at the points B, C, D, E, etc.

**Step 3.** Join consecutive vertices of the polygon to A, forming n triangles: triangle ABC, triangle ACD, triangle ADE, ..., triangle AEB [P1]. Each triangle lies in a plane [11.2].

**Step 4.** By 1.32, the sum of the three angles in each triangle equals two right angles. Since there are n such triangles, the total sum of all their angles is 2n right angles [CN2].

**Step 5.** The angles of these n triangles can be partitioned into two groups: (i) the angles at vertex A, which are precisely the plane angles BAC, CAD, DAE, ..., EAB constituting the solid angle, and (ii) the remaining base angles at the polygon vertices B, C, D, E, .... Therefore the sum of the face angles at A plus the sum of all base angles equals 2n right angles [CN2].

**Step 6.** At each polygon vertex, say B, consider the two base angles from the adjacent triangles: angle ABE (from triangle AEB) and angle ABC (from triangle ABC). The line AB meets the plane of the polygon at B, and A is above the plane, so at B the three edges BA, BC, BE form a solid angle, with the plane angle EBC being the interior angle of the polygon at B. By 11.20, any two of the three plane angles forming this solid angle are together greater than the remaining one, so angle ABE + angle ABC > angle EBC.

**Step 7.** Applying Step 6 at every vertex of the polygon, we obtain that the sum of all base angles from the n triangles is greater than the sum of all interior angles of the polygon BCDE... [CN2].

**Step 8.** The polygon BCDE... has n sides. By dividing this polygon into (n - 2) triangles from one vertex [P1], and applying 1.32 to each of these triangles, the sum of the interior angles of the polygon equals 2(n - 2) right angles, that is, (2n - 4) right angles [CN2].

**Step 9.** From Step 7, the sum of all base angles > (2n - 4) right angles.

**Step 10.** From Step 5, the sum of the face angles at A = 2n right angles minus the sum of all base angles. Since the sum of all base angles > (2n - 4) right angles (Step 9), and both quantities are positive, subtracting a larger quantity yields a smaller result: the sum of the face angles at A < 2n right angles - (2n - 4) right angles = 4 right angles [CN3, CN5].

**Step 11.** Therefore any solid angle is contained by plane angles whose sum is less than four right angles. Q.E.D.

**USED:** 1.32, 11.2, 11.20, CN2, CN3, CN5, P1
**Human refs (from References field):** 1.32, 11.20
**Jaccard:** 0.286 — AI adds ['11.2', 'CN2', 'CN3', 'CN5', 'P1']

## Proposition 11.22
**Statement:** If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

**Step 1.** Let the three plane angles be angle BAC, angle DEF, and angle GHK, where any two taken together are greater than the remaining one. Let the arms be equal: AB = AC = DE = DF = GH = HK. Join BC, EF, and GK. We must show that any two of BC, EF, GK are greater than the remaining one, and hence a triangle can be constructed from them by 1.22.

**Step 2.** By 1.20 (in any triangle, any two sides are greater than the remaining one), to show BC, EF, GK can form a triangle, it suffices to show that any two of them taken together are greater than the third.

**Step 3.** Consider the case where angle BAC is the greatest of the three angles (if the angles are all equal, all chords are equal by 1.4 and the result is immediate). Since angle DEF + angle GHK > angle BAC by hypothesis, and angle BAC is the greatest angle, we have angle BAC > angle DEF and angle BAC > angle GHK. By 1.24 (if two triangles have two sides equal to two sides respectively but the included angle of one is greater than the included angle of the other, then the base of the former is greater than the base of the latter), BC > EF and BC > GK. Thus BC is the greatest of the three line segments.

**Step 4.** It remains to show EF + GK > BC; the other two triangle inequality conditions (BC + EF > GK and BC + GK > EF) hold automatically since BC is the greatest side and the arms are equal, giving us EF > 0 and GK > 0 (as the angles are non-degenerate).

**Step 5.** At point B on line BA, on the side of BC, construct angle ABL equal to angle DEF by 1.23. On ray BL, cut off BL equal to DE by 1.3. Since AB = DE and BL = DE, we have AB = BL. Also angle ABL = angle DEF. So in triangles ABL and DEF, AB = DE, BL = DF (both equal to DE = DF), and angle ABL = angle DEF. By 1.4 (SAS congruence), triangle ABL is congruent to triangle DEF, so AL = EF.

**Step 6.** Similarly, at point B on line BA, on the side of BC, construct angle ABM equal to angle GHK by 1.23, where M is on the same side as L and C. We need angle ABL + angle ABM to be placed so that angle LBM corresponds to angle DEF + angle GHK minus overlapping considerations. Instead, let us proceed more carefully following Euclid's approach.

**Step 7.** At vertex B, construct angle ABL equal to angle DEF on the side of BC, using 1.23. Make BL = DE = AB by 1.3. Then at B, construct angle LBM equal to angle GHK, using 1.23, on the side of BL away from A (i.e., so that angle ABM = angle ABL + angle LBM = angle DEF + angle GHK). Make BM = GH = AB by 1.3.

**Step 8.** Since angle ABM = angle DEF + angle GHK > angle BAC (by hypothesis, any two of the three angles are greater than the third), and also angle ABM = angle ABL + angle LBM, we have angle ABM > angle BAC.

**Step 9.** Now in triangle ABL: AB = BL (both equal to DE), so by 1.5 (base angles of isosceles triangle are equal), angle BAL = angle BLA.

**Step 10.** In triangle BLM: BL = BM (both equal to AB = DE = GH), so by 1.5, angle BLM = angle BML.

**Step 11.** Thus angle BAL + angle BLM = angle BLA + angle BLM = angle ALM (where these angles are adjacent at L). Wait -- let us consider the full angle at L more carefully. We have angle BLA + angle BLM; these may or may not form the full angle ALM depending on configuration. Since L lies between rays BA and BC (as angle ABL < angle ABC because angle DEF < angle BAC), and M is constructed beyond L, the points A, L, M are such that angle ALM = angle BLM - angle BLA or angle ALM = angle BLA + angle BLM depending on whether A and M are on the same side of BL.

**Step 12.** Let us reconsider the construction more carefully. At B, on the ray BC, we know angle ABC = angle BAC's subtended configuration. Construct angle ABL = angle DEF with L on the same side of BA as C, and BL = AB. Then construct angle LBN = angle GHK on ray BL with N on the same side, and BN = AB. Since angle ABN = angle ABL + angle LBN = angle DEF + angle GHK, and angle DEF + angle GHK > angle BAC, we get angle ABN > angle BAC = angle ABC is not necessarily true. We need angle ABC's relationship.

**Step 13.** Let us follow Euclid's own method precisely. We set up the construction at a single point. At point O, construct three angles: angle AOB = angle BAC, angle AOC = angle DEF, and angle BOC = angle GHK, making OA = OB = OC = AB = DE = GH (the common length of the equal straight lines), using 1.23 and 1.3. Actually, the proposition is about constructing the angles at endpoints of equal lines, so let us restate: given three angles at three different vertices with equal arms, show the chords form a triangle.

**Step 14.** We work at vertex A. By 1.23, at point A on line AB, construct angle BAL equal to angle DEF, with L on the same side of AB as C. By 1.3, cut off AL = DE (= AB, since all arms are equal). Join BL. By 1.4, since AB = DE, AL = DF, and angle BAL = angle DEF, we get BL = EF.

**Step 15.** Next, at point A on line AB, construct angle BAM equal to angle DEF + angle GHK. Specifically, on ray AL construct angle LAM equal to angle GHK by 1.23, and cut off AM = GH = AB by 1.3. Then angle BAM = angle BAL + angle LAM = angle DEF + angle GHK. Join BM. By 1.4, since AL = GH, AM = HK (both equal to the common arm length), and angle LAM = angle GHK, we get LM = GK.

**Step 16.** Since angle DEF + angle GHK > angle BAC (by hypothesis), we have angle BAM > angle BAC. Now AB = AC and AB = AM (all arms are equal). In triangles ABC and ABM, AB = AB, AC = AM, but angle BAC < angle BAM. By 1.24, BC < BM. So BM > BC.

**Step 17.** In triangle ABM, since AB = AM (isosceles), by 1.5, angle ABM = angle AMB. In triangle ALM, since AL = AM (both equal to the common length), by 1.5, angle ALM = angle AML.

**Step 18.** Now angle AML < angle AMB (since angle AML is a part of angle AMB, as L lies in the interior of triangle ABM -- L is between rays AB and AM from A, and BL connects B to L). Actually, since angle BAL = angle DEF < angle BAM = angle DEF + angle GHK, ray AL lies between rays AB and AM, so L is on the same side of AM as B. By CN5 (the whole is greater than the part), angle AMB > angle AML.

**Step 19.** Similarly, angle ALM < angle ALB. Since angle ALM = angle AML (from Step 17), and angle AML < angle AMB (from Step 18), we have angle ALM < angle AMB. Also angle ABM = angle AMB (from Step 17). So angle ALM < angle ABM, which means angle ALB > angle ABL (since angle ALB > angle ALM and we need to relate these).

**Step 20.** In triangle BLM, we use 1.20: BL + LM > BM. But BM > BC from Step 16 is not directly what we need. We need BL + LM > BC. Actually, we need to show EF + GK > BC, i.e., BL + LM > BC.

**Step 21.** From Step 16, we have BC < BM. From triangle BLM (applying 1.20), BL + LM > BM. Therefore BL + LM > BM > BC, which gives BL + LM > BC, i.e., EF + GK > BC.

**Step 22.** For the other two inequalities: Since angle BAC > angle DEF (because angle BAC is the greatest), by 1.24 applied to triangles with equal arms, BC > EF. Since GK > 0 (angle GHK is a proper angle), BC + GK > EF. Similarly, since BC > GK (by 1.24, as angle BAC > angle GHK), and EF > 0, BC + EF > GK.

**Step 23.** Thus any two of BC, EF, GK taken together are greater than the remaining one. By 1.22 (out of three straight lines which are equal to three given straight lines, any two taken together being greater than the third, to construct a triangle), a triangle can be formed with sides equal to BC, EF, and GK. These are the straight lines joining the extremities of the equal straight lines containing the three given plane angles.

**Step 24.** Therefore, if there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines. Q.E.F.

**USED:** 1.20, 1.22, 1.23, 1.24, 1.3, 1.4, 1.5, CN5, P1
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 0.222 — AI adds ['1.20', '1.22', '1.23', '1.3', '1.5', 'CN5', 'P1']

## Proposition 11.23
**Statement:** To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

**Step 1.** Let the three given plane angles be ABC, DEF, and GHK, where any two taken together are greater than the remaining one, and the sum of all three is less than four right angles. We must construct a solid angle contained by angles equal to these three plane angles.

**Step 2.** Cut off equal lengths from the sides of each angle: let AB = BC = DE = EF = GH = HK, using I.3 to make these all equal to some chosen length.

**Step 3.** Join AC, DF, and GK by P1. Since the three plane angles are contained by equal straight lines, and any two of the angles are greater than the remaining one, by 11.22 it is possible to construct a triangle with sides equal to AC, DF, and GK. Construct triangle LMN such that LM = AC, MN = DF, and NL = GK, using 1.22.

**Step 4.** About triangle LMN describe a circle, using 4.5, and let its center be O. The center O lies either inside the triangle, on one of its sides, or outside the triangle.

**Step 5.** Case 1: Suppose O falls inside triangle LMN, or on one of its sides. Join OL, OM, ON by P1. Since OL = OM = ON (all being radii of the circumscribed circle, by D1.15 and D3.1).

**Step 6.** From point O, set up a straight line OP at right angles to the plane of triangle LMN, using 11.12. We must find the appropriate height for OP.

**Step 7.** Since AB = BC and LM = AC, triangle ABC is isosceles with AB = BC. Similarly, triangle LOM has OL = OM. On the base LM = AC, construct triangle ABL' (i.e., consider that AB^2 = (AC/2)^2 + h^2 for the height from B to AC). Since AB^2 = AO'^2 + BO'^2 where O' is the midpoint of AC (by a perpendicular drop), and similarly in triangle LOM, we have AB^2 - (LM/2)^2 gives the square of the distance from B to AC, and OL^2 - (LM/2)^2 gives the square of the distance from O to LM. Since AB = BC = DE = EF = GH = HK and these are the arms of the given angles, and OL is merely the circumradius, we need AB > OL so that AB^2 > OL^2 (which we shall verify).

**Step 8.** We verify that AB > OL. Since the three angles sum to less than four right angles, and from the construction in 11.22 the triangle LMN can be formed, the circumradius OL of triangle LMN is strictly less than AB. To see this: in triangle ABС (isosceles, AB = BC, base AC = LM), the angle ABC is one of the three given plane angles. Consider the isosceles triangle OLM with OL = OM and base LM. The angle LOM at the center subtends the same chord LM = AC. Since angle ABC is one of the three plane angles whose sum is less than four right angles, and the angle LOM at the center corresponds to the arc, the constraint that the three angles sum to less than four right angles ensures that OL < AB. Specifically, in any isosceles triangle on a given base, a larger apex angle corresponds to shorter equal sides, so if angle LOM >= angle ABC, then OL <= AB; but we need strict inequality. Since the sum of all three angles is less than four right angles, not all three central angles LOM, MON, NOL can equal or exceed the corresponding plane angles simultaneously (their sum would be exactly four right angles for the central angles around O), so OL < AB. Thus AB^2 > OL^2, and AB^2 - OL^2 > 0.

**Step 9.** Since AB^2 > OL^2, the difference AB^2 - OL^2 is a positive quantity. Set the square on OP equal to AB^2 - OL^2, so that OP^2 = AB^2 - OL^2. This is possible by finding a line whose square equals this difference using 1.47 in reverse (i.e., by 1.46 and related constructions, or by taking OP such that OP^2 + OL^2 = AB^2).

**Step 10.** Join PL, PM, PN by P1. Since OP is at right angles to the plane of triangle LMN (by construction in Step 6), OP is perpendicular to OL, OM, and ON (by D11.3). Therefore, in right triangle POL, PL^2 = PO^2 + OL^2 = (AB^2 - OL^2) + OL^2 = AB^2, by 1.47. Hence PL = AB.

**Step 11.** Similarly, PM^2 = PO^2 + OM^2 = (AB^2 - OL^2) + OL^2 = AB^2 (since OM = OL, both being radii). Hence PM = AB. Likewise PN^2 = PO^2 + ON^2 = AB^2, so PN = AB.

**Step 12.** Now PL = PM = AB = BC, and LM = AC. Therefore triangles PLM and ABC have all three sides equal (PL = AB, PM = BC, LM = AC), so by 1.8, angle LPM = angle ABC.

**Step 13.** Similarly, PM = PN = DE = EF and MN = DF. Therefore by 1.8, angle MPN = angle DEF.

**Step 14.** Similarly, PN = PL = GH = HK and NL = GK. Therefore by 1.8, angle NPL = angle GHK.

**Step 15.** Therefore the solid angle at P, contained by the three plane angles LPM, MPN, and NPL, is a solid angle constructed from three plane angles equal to the given angles ABC, DEF, and GHK respectively.

**Step 16.** Case 2: Suppose O falls outside triangle LMN. The construction proceeds analogously. Join OL, OM, ON. Set up OP at right angles to the plane at O using 11.12. The same argument shows AB > OL (using the constraint that the angles sum to less than four right angles), so we set OP^2 = AB^2 - OL^2. Then PL = PM = PN = AB as before, and by 1.8 the angles at P equal the given angles.

**Step 17.** Therefore, in all cases, we have constructed a solid angle at P out of three plane angles equal to the three given plane angles ABC, DEF, and GHK. Q.E.F.

**USED:** 1.22, 1.3, 1.47, 1.8, 11.12, 11.22, 4.5, D1.15, D11.11, D11.3, D3.1, P1
**Human refs (from References field):** 1.25, 1.29, 1.4, 1.47, 1.8, 11.12, 11.22, 5.16, 6.2, 6.4
**Jaccard:** 0.222 — AI adds ['1.22', '1.3', '4.5', 'D1.15', 'D11.11', 'D11.3', 'D3.1', 'P1']; Human adds ['1.25', '1.29', '1.4', '5.16', '6.2', '6.4']

## Proposition 11.24
**Statement:** If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

**Step 1.** Let the solid ABCDEFGH be contained by parallel planes: let the plane ABCD be parallel to the plane EFGH, the plane ABFE be parallel to the plane DCGH, and the plane ADHE be parallel to the plane BCGF. We must show that the opposite faces are parallelogrammic and equal.

**Step 2.** Since the two parallel planes ABCD and EFGH are cut by the plane ABFE, their common sections AB and EF are parallel [11.16].

**Step 3.** Since the two parallel planes ABCD and EFGH are cut by the plane ADHE, their common sections AD and EH are parallel [11.16].

**Step 4.** Since the two parallel planes ABFE and DCGH are cut by the plane ABCD, their common sections AB and DC are parallel [11.16].

**Step 5.** Since the two parallel planes ABFE and DCGH are cut by the plane ADHE, their common sections AE and DH are parallel [11.16].

**Step 6.** Since the two parallel planes ABFE and DCGH are cut by the plane EFGH, their common sections EF and HG are parallel [11.16].

**Step 7.** Since the two parallel planes ABFE and DCGH are cut by the plane BCGF, their common sections BF and CG are parallel [11.16].

**Step 8.** Since the two parallel planes ADHE and BCGF are cut by the plane ABCD, their common sections AD and BC are parallel [11.16].

**Step 9.** Since the two parallel planes ADHE and BCGF are cut by the plane EFGH, their common sections EH and FG are parallel [11.16].

**Step 10.** Since the two parallel planes ADHE and BCGF are cut by the plane ABFE, their common sections AE and BF are parallel [11.16].

**Step 11.** Since the two parallel planes ADHE and BCGF are cut by the plane DCGH, their common sections DH and CG are parallel [11.16].

**Step 12.** Consider face ABCD: AB is parallel to DC (Step 4), and AD is parallel to BC (Step 8). Therefore ABCD is a parallelogram [D1.22]. Likewise, consider face EFGH: EF is parallel to HG (Step 6), and EH is parallel to FG (Step 9). Therefore EFGH is a parallelogram.

**Step 13.** Consider face ABFE: AB is parallel to EF (Step 2), and AE is parallel to BF (Step 10). Therefore ABFE is a parallelogram. Likewise, consider face DCGH: DC is parallel to HG (since DC is parallel to AB by Step 4, AB is parallel to EF by Step 2, and EF is parallel to HG by Step 6, so DC is parallel to HG), and DH is parallel to CG (Step 11). Therefore DCGH is a parallelogram.

**Step 14.** Consider face ADHE: AD is parallel to EH (Step 3), and AE is parallel to DH (Step 5). Therefore ADHE is a parallelogram. Likewise, consider face BCGF: BC is parallel to FG (since BC is parallel to AD by Step 8, AD is parallel to EH by Step 3, and EH is parallel to FG by Step 9, so BC is parallel to FG), and BF is parallel to CG (Step 7). Therefore BCGF is a parallelogram.

**Step 15.** Thus every face of the solid is parallelogrammic. It remains to prove that opposite faces are equal.

**Step 16.** Consider the opposite faces ABCD and EFGH. Since ABFE is a parallelogram (Step 13), AB equals EF and AB is parallel to EF [1.34]. Since ADHE is a parallelogram (Step 14), AD equals EH and AD is parallel to EH [1.34].

**Step 17.** In parallelogram ABCD, angle DAB is the angle between AD and AB. In parallelogram EFGH, angle HEF is the angle between EH and EF. Now AB is parallel to EF (Step 2) and AD is parallel to EH (Step 3), and these pairs of lines meet at A and E respectively, not being in the same plane. By 11.10, angle DAB equals angle HEF.

**Step 18.** Since in triangles DAB and HEF we have DA equal to HE (Step 16), AB equal to EF (Step 16), and angle DAB equal to angle HEF (Step 17), triangle DAB is equal to triangle HEF, and DB equals HF [1.4].

**Step 19.** Since ABCD is a parallelogram, its diagonal DB divides it into two equal triangles DAB and DCB [1.34]. Since EFGH is a parallelogram, its diagonal HF divides it into two equal triangles HEF and HGF [1.34].

**Step 20.** In triangles DCB and HGF: since ABCD is a parallelogram, DC equals AB [1.34], and AB equals EF (Step 16), and since EFGH is a parallelogram, EF equals HG [1.34]; so DC equals HG [CN1]. Similarly, BC equals AD [1.34], and AD equals EH (Step 16), and EH equals FG [1.34]; so BC equals FG [CN1]. And DB equals HF (Step 18). Therefore triangle DCB is equal to triangle HGF [1.8, 1.4].

**Step 21.** Since parallelogram ABCD equals twice triangle DAB [1.34], and parallelogram EFGH equals twice triangle HEF [1.34], and triangle DAB equals triangle HEF (Step 18), it follows that parallelogram ABCD equals parallelogram EFGH [CN2].

**Step 22.** By an analogous argument for the opposite faces ABFE and DCGH: since ABCD is a parallelogram, AB equals DC [1.34]; since ADHE is a parallelogram, AE equals DH [1.34]. The lines AB and DC are parallel (Step 4), and AE and DH are parallel (Step 5). These pairs meet at A and D respectively, not in the same plane, so angle BAE equals angle CDH [11.10]. Triangles BAE and CDH have AB equal to DC, AE equal to DH, and angle BAE equal to angle CDH, so the triangles are equal and BE equals CH [1.4]. Since parallelogram ABFE equals twice triangle BAE and parallelogram DCGH equals twice triangle CDH [1.34], the parallelograms ABFE and DCGH are equal [CN2].

**Step 23.** By an analogous argument for the opposite faces ADHE and BCGF: since ABFE is a parallelogram, AE equals BF [1.34]; since ABCD is a parallelogram, AD equals BC [1.34]. The lines AE and BF are parallel (Step 10), and AD and BC are parallel (Step 8). These pairs meet at A and B respectively, not in the same plane, so angle EAD equals angle FBC [11.10]. Triangles EAD and FBC have AE equal to BF, AD equal to BC, and angle EAD equal to angle FBC, so the triangles are equal [1.4]. Since parallelogram ADHE equals twice triangle EAD and parallelogram BCGF equals twice triangle FBC [1.34], the parallelograms ADHE and BCGF are equal [CN2].

**Step 24.** Therefore, if a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic. Q.E.D.

**USED:** 1.34, 1.4, 1.8, 11.10, 11.16, CN1, CN2, D1.22
**Human refs (from References field):** 1.34, 1.4, 11.10, 11.16
**Jaccard:** 0.500 — AI adds ['1.8', 'CN1', 'CN2', 'D1.22']

## Proposition 11.25
**Statement:** If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.

**Step 1.** Let the parallelepipedal solid ABCDEFGH (with base ABCD, top EFGH, and lateral edges AE, BF, CG, DH) be cut by a plane parallel to the opposite faces ADHE and BCGF. Let this plane meet edge AB at K, edge DC at L, edge EF at N, and edge HG at M. Then the cutting plane KLMN divides the solid into two parallelepipeds: solid S1 with base AKLD and solid S2 with base KBCL.

**Step 2.** Since the cutting plane is parallel to faces ADHE and BCGF, and these faces are parallel to each other (by 11.24, opposite faces of the parallelepiped are equal and parallelogrammic, and therefore parallel), the cutting plane KLMN is parallel to both. By 11.16, since the parallel planes ADHE and BCGF are cut by the plane ABCD, the common sections are parallel; hence AD is parallel to BC. Similarly, since the cutting plane KLMN and the plane ADHE are both cut by the plane ABCD, the common sections KL and AD are parallel (by 11.16). Likewise KL is parallel to BC.

**Step 3.** Since ABCD is a parallelogram (by 11.24), AB is parallel to DC (by 1.34). Since KL is parallel to AD and AK is part of AB which is parallel to DL (part of DC), the figure AKLD is a parallelogram (by 1.33, since AK is equal and parallel to DL). Similarly KBCL is a parallelogram.

**Step 4.** Both parallelograms AKLD and KBCL have a pair of opposite sides equal to AD (since KL = AD by 1.34 applied to parallelogram AKLD, and BC = AD by 1.34 applied to ABCD). The parallelograms AKLD and KBCL lie between the same parallel lines AD and BC (since KL is parallel to and between AD and BC). By 6.1, parallelograms between the same parallels are to one another as their bases, so AKLD : KBCL = AK : KB.

**Step 5.** We now show that the solids S1 and S2 are in the same ratio as their bases AKLD and KBCL, using the definition of equal ratios (D5.5). Take any positive integers m and n. On the line through A and B, starting from A, mark off m segments each equal to AK, obtaining points A = K_0, K_1 = K, K_2, ..., K_m. Starting from K, mark off n segments each equal to KB, obtaining points K = K'_0, K'_1 = B, K'_2, ..., K'_n. Through each of these points, draw a plane parallel to the face ADHE.

**Step 6.** Each consecutive pair of these parallel planes, together with the top and bottom planes (ABCD and EFGH) and the front and back planes (ABFE and DCGH), bounds a parallelepipedal solid. Consider the m slabs between K_0 and K_m: each slab is a parallelepiped. By 11.24, the opposite faces of each slab are equal parallelograms. Each slab has a base parallelogram congruent to AKLD (with sides equal to AK and AD and the same included angle, since all bases lie in parallel planes cut by the same parallel lateral edges). By the same reasoning, each of the n slabs on the KB side has a base congruent to KBCL.

**Step 7.** Each of the m slabs is a parallelepiped with all six faces respectively equal to the corresponding faces of solid S1: the base faces are parallelograms with sides AK and AD and equal included angles; the lateral faces likewise match (with sides AK and AE, or AD and AE, with equal included angles). Since the slabs are contained by similar planes equal in multitude and magnitude, by D11.10 each slab equals S1 as a solid figure. Similarly each of the n slabs equals S2.

**Step 8.** The m slabs placed consecutively along the direction from A toward B form a single parallelepiped whose base is a parallelogram with one side equal to m times AK and the other side equal to AD (by repeated application of the construction and 1.34). This combined solid equals m times S1 in solid content (being composed of m equal parts). Similarly, the n slabs form a parallelepiped whose base has one side equal to n times KB and the other equal to AD, and this combined solid equals n times S2.

**Step 9.** The combined base of the m slabs is a parallelogram between the same parallels as the combined base of the n slabs (both lie in the plane of ABCD, between lines parallel to AD). By 6.1, these combined bases are in the ratio m·AK : n·KB, and so the m-fold base exceeds, equals, or falls short of the n-fold base according as m·AK exceeds, equals, or falls short of n·KB.

**Step 10.** Now we show the solids follow the same ordering. Both the m-fold parallelepiped and the n-fold parallelepiped stand between the same parallel planes (the plane of ABCD and the plane of EFGH) and share the same depth dimension (AD) and the same height (AE). If m·AK = n·KB, then the m-fold and n-fold parallelepipeds have all six faces respectively equal (their bases have equal sides m·AK = n·KB and AD with the same included angle, and all other faces match correspondingly). By D11.10, these solids are equal, so m·S1 = n·S2. If m·AK > n·KB, then the n-fold parallelepiped can be placed within the m-fold parallelepiped (since they share the same height and depth dimensions, and the n-fold base fits within the m-fold base along the direction of AB). By CN5, the whole is greater than the part, so m·S1 > n·S2. Similarly, if m·AK < n·KB, then m·S1 < n·S2.

**Step 11.** Therefore, for all positive integers m and n, the m-fold of base AKLD exceeds, equals, or falls short of the n-fold of base KBCL precisely when the m-fold of solid S1 exceeds, equals, or falls short of the n-fold of solid S2. By the definition of proportionality (D5.5), AKLD : KBCL = S1 : S2.

**Step 12.** Therefore, if a parallelepipedal solid is cut by a plane parallel to the opposite planes, then as the base is to the base, so is the solid to the solid. Q.E.D.

**USED:** 1.33, 1.34, 11.16, 11.24, 6.1, CN4, CN5, D11.10, D5.5
**Human refs (from References field):** 11.24, D5.5
**Jaccard:** 0.222 — AI adds ['1.33', '1.34', '11.16', '6.1', 'CN4', 'CN5', 'D11.10']

## Proposition 11.26
**Statement:** On a given straight line, and at a given point on it, to construct a solid angle equal to a given solid angle.

**Step 1.** Let AB be the given straight line, A the given point on it, and let the given solid angle be at D, contained by the plane angles EDC, EDF, and FDC (the argument generalizes to solid angles contained by more plane angles by decomposition into trihedral components).

**Step 2.** On the straight line DE, take any point E; on DF take any point F; and on DC take any point C (these points are already named as the endpoints of the edges containing the solid angle). Join EF, FC, and EC [P1].

**Step 3.** Since the solid angle at D is contained by the three plane angles EDC, EDF, and FDC, by 11.20, any two of these plane angles taken together are greater than the remaining one. By 11.21, the three plane angles together are less than four right angles.

**Step 4.** At the point A on the straight line AB, in a plane through AB, construct the angle BAH equal to the angle EDC [1.23]. Make AH equal to DC and AB' (a point on ray AB beyond A, call it K) such that AK equals DE, by cutting off equal lengths [1.3].

**Step 5.** More precisely: on line AB, set AK equal to DE [1.3]. At point A, construct angle KAH equal to angle EDC [1.23], and make AH equal to DC [1.3]. Join KH [P1].

**Step 6.** Now construct angle KAL equal to angle EDF [1.23], in a plane different from the plane of angle KAH. Make AL equal to DF [1.3].

**Step 7.** We must verify that a triangle can be formed from KH, the line joining H to L, and KL, corresponding to the triangle formed by EC, CF, and EF respectively. In triangle EDC, since AK = DE, AH = DC, and angle KAH = angle EDC, by 1.4 (side-angle-side), triangle KAH is congruent to triangle EDC. Therefore KH = EC.

**Step 8.** Similarly, in triangle EDF, since AK = DE, AL = DF, and angle KAL = angle EDF, by 1.4, triangle KAL is congruent to triangle EDF. Therefore KL = EF.

**Step 9.** We need to determine HL such that triangle KHL corresponds to triangle ECF. In triangle DCF, since AH = DC and AL = DF, and we require angle HAL = angle CDF, construct angle HAL equal to angle CDF [1.23]. Then by 1.4, triangle HAL is congruent to triangle CDF, so HL = CF.

**Step 10.** Now we have three plane angles KAH, KAL, and HAL at vertex A, equal respectively to angles EDC, EDF, and FDC. By Step 3, any two of these angles taken together are greater than the remaining one (since they equal the original angles which satisfy this by 11.20), and their sum is less than four right angles (since they equal the original angles which satisfy this by 11.21).

**Step 11.** The straight lines AK, AH, AL are equal respectively to DE, DC, DF. The triangles KAH, KAL, HAL are congruent respectively to triangles EDC, EDF, DCF. Therefore KH = EC, KL = EF, and HL = CF, so triangle KHL is congruent to triangle ECF [1.8, since all three pairs of sides are equal].

**Step 12.** By 11.22, since any two of the three plane angles KAH, KAL, HAL taken together are greater than the remaining one, and they are contained by equal straight lines (AK = AH in the case where DE = DC, but more generally the construction uses the equal straight lines AK, AH, AL matching DE, DC, DF), and the joining lines KH, KL, HL form a triangle, the conditions for constructing a solid angle are met.

**Step 13.** By 11.23, from the three plane angles KAH, KAL, HAL (any two of which are greater than the third, and whose sum is less than four right angles), construct a solid angle at A. Specifically, 11.23 provides a solid angle at A contained by these three plane angles.

**Step 14.** The solid angle at A is contained by plane angles KAH, KAL, and HAL, which are respectively equal to the plane angles EDC, EDF, and FDC that contain the given solid angle at D.

**Step 15.** Since the plane angles containing the solid angle at A are respectively equal to the plane angles containing the solid angle at D, and the sides about those equal angles are respectively equal (AK = DE, AH = DC, AL = DF), and the bases are respectively equal (KH = EC, KL = EF, HL = CF), the solid angle at A equals the solid angle at D.

**Step 16.** Moreover, this solid angle has been constructed at the given point A on the given straight line AB, since the edge AK lies along AB.

**Step 17.** Therefore, on the given straight line AB, at the given point A on it, a solid angle has been constructed equal to the given solid angle at D. Q.E.F.

**USED:** 1.23, 1.3, 1.4, 1.8, 11.20, 11.21, 11.22, 11.23, P1
**Human refs (from References field):** 1.23, 1.4, 1.8, 11.11, 11.12, D11.3
**Jaccard:** 0.250 — AI adds ['1.3', '11.20', '11.21', '11.22', '11.23', 'P1']; Human adds ['11.11', '11.12', 'D11.3']

## Proposition 11.27
**Statement:** On a given straight line to describe a parallelepipedal solid similar and similarly situated to a given parallelepipedal solid.

**Step 1.** Let AB be the given straight line and let the parallelepiped CD be the given parallelepipedal solid, with vertex C and three edges CF, CG, CH meeting at C. We are required to describe on AB a parallelepipedal solid similar and similarly situated to CD.

**Step 2.** At the point A of the straight line AB, construct a solid angle equal to the solid angle at C, using three plane angles BAK, KAL, LAB equal respectively to the three plane angles FCG, GCH, HCF, so that the solid angle at A is equal to the solid angle at C [11.26].

**Step 3.** Since AB corresponds to CF as an edge of the solid to be constructed, we need the remaining two edges at A to be in the same ratios as the edges at C. Make AK such that CF is to CG as AB is to AK, i.e., find AK as the fourth proportional to CF, CG, and AB [6.12].

**Step 4.** Similarly, make AL such that CF is to CH as AB is to AL, i.e., find AL as the fourth proportional to CF, CG, and AB for the second pair: CF : CH = AB : AL [6.12].

**Step 5.** From these three proportions, since CF : CG = AB : AK and CF : CH = AB : AL, we also obtain by taking the ratios ex aequali and by the properties of proportional magnitudes that CG : CH = AK : AL [5.22].

**Step 6.** Complete the parallelepipedal solid AE on the three edges AB, AK, AL at the solid angle A. That is, through the endpoints of AB, AK, AL draw planes parallel to the opposite faces, forming the parallelepiped [P1, 11.15].

**Step 7.** Now we must show that the parallelepiped AE is similar and similarly situated to the parallelepiped CD. By D11.9, similar solid figures are those contained by similar planes equal in multitude. A parallelepiped has six faces, all parallelogrammic [11.24].

**Step 8.** Consider the face in the plane of angle BAK at vertex A and the corresponding face in the plane of angle FCG at vertex C. The angle BAK equals the angle FCG by construction [11.26]. Furthermore, the sides about these equal angles are proportional: AB : AK = CF : CG by Step 3. Therefore the parallelogram on AB, AK is similar to the parallelogram on CF, CG [D6.1].

**Step 9.** Similarly, consider the face in the plane of angle KAL at vertex A and the corresponding face in the plane of angle GCH at vertex C. The angle KAL equals the angle GCH by construction [11.26]. The sides about these equal angles are proportional: AK : AL = CG : CH by Step 5. Therefore the parallelogram on AK, AL is similar to the parallelogram on CG, CH [D6.1].

**Step 10.** Similarly, consider the face in the plane of angle LAB at vertex A and the corresponding face in the plane of angle HCF at vertex C. The angle LAB equals the angle HCF by construction [11.26]. The sides about these equal angles are proportional: since CF : CH = AB : AL (Step 4), we have AL : AB = CH : CF, and so AB : AL = CF : CH. Therefore the parallelogram on AB, AL is similar to the parallelogram on CF, CH [D6.1].

**Step 11.** For the three remaining opposite faces of each parallelepiped: in any parallelepiped, opposite faces are equal and similar parallelograms [11.24]. Hence the three opposite faces of AE are respectively similar to the three opposite faces of CD.

**Step 12.** Therefore all six faces of the parallelepiped AE are respectively similar to the six faces of the parallelepiped CD, and they are equal in multitude (both have six faces). Moreover, the solid angle at A is equal to the solid angle at C, and corresponding angles at every vertex are similarly arranged because the construction placed the edges in the same configuration.

**Step 13.** Therefore, by definition, the parallelepiped AE is similar and similarly situated to the parallelepiped CD [D11.9].

**Step 14.** Hence on the given straight line AB, the parallelepipedal solid AE has been described similar and similarly situated to the given parallelepipedal solid CD. Q.E.F.

**USED:** 11.15, 11.24, 11.26, 5.22, 6.12, D11.9, D6.1, P1
**Human refs (from References field):** 5.22, 6.12, D11.9
**Jaccard:** 0.375 — AI adds ['11.15', '11.24', '11.26', 'D6.1', 'P1']

## Proposition 11.28
**Statement:** If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid will be bisected by the plane.

**Step 1.** Let the parallelepipedal solid ABCDEFGH be cut by the plane ACGE passing through the diagonals AC and EG of the opposite faces ABCD and EFGH respectively. We must show that this plane bisects the solid.

**Step 2.** Since ABCDEFGH is a parallelepiped, by Proposition 11.24 its opposite faces are equal and parallelogrammic. In particular, face ABCD is an equal parallelogram to face EFGH, face ABFE is an equal parallelogram to face DCGH, and face BCGF is an equal parallelogram to face ADHE.

**Step 3.** Consider the face ABCD. Since ABCD is a parallelogram, its diagonal AC bisects it into two equal triangles: triangle ABC equals triangle ACD (by Proposition 1.34).

**Step 4.** Similarly, consider the opposite face EFGH. Since EFGH is a parallelogram, its diagonal EG bisects it into two equal triangles: triangle EFG equals triangle EHG (by Proposition 1.34).

**Step 5.** Now consider the face ABFE. Since ABFE is a parallelogram, AB is equal and parallel to EF (by Proposition 1.34). Likewise, from the face BCGF being a parallelogram, BC is equal and parallel to FG.

**Step 6.** The cutting plane ACGE divides the parallelepiped into two solids: the solid with triangular faces ABC and EFG on opposite ends (bounded also by the parallelogram ABFE, the parallelogram BCGF, and the plane triangle faces ACE and ACG through the cutting plane), and the solid with triangular faces ACD and EHG on opposite ends.

**Step 7.** Consider the first solid, bounded by triangles ABC and EFG as opposite faces, and by parallelograms ABFE and BCGF, and the cutting plane ACGE. Since AB is parallel and equal to EF, and BC is parallel and equal to FG, and the triangles ABC and EFG are equal, similar, and lie in parallel planes (the planes of the opposite faces ABCD and EFGH, which are parallel by Proposition 11.24), this solid is a prism (Definition 11.13).

**Step 8.** Similarly, the second solid is bounded by equal triangles ACD and EHG as opposite faces, and by parallelograms ADHE and DCGH, and the cutting plane ACGE. Since AD is parallel and equal to EH, and DC is parallel and equal to HG, and the triangles ACD and EHG are equal and similar and lie in parallel planes, this solid is also a prism.

**Step 9.** We now show these two prisms are equal. Consider that the triangular base ABC of the first prism equals the triangular base ACD of the second prism, since diagonal AC bisects parallelogram ABCD into two equal triangles (by Proposition 1.34, Step 3).

**Step 10.** Similarly, the opposite triangular faces EFG and EHG are equal, since diagonal EG bisects parallelogram EFGH into two equal triangles (by Proposition 1.34, Step 4).

**Step 11.** The lateral edges AE, BF, CG of the first prism are the same edges as AE, DH, CG of the second prism (with BF and DH both being lateral edges of the original parallelepiped). Since ABFE is a parallelogram, AE equals BF. Since ADHE is a parallelogram, AE equals DH. Thus all lateral edges of both prisms are equal (by Common Notion 1).

**Step 12.** Furthermore, the two prisms have the same height, since they share the same parallel opposite planes (the planes of ABCD and EFGH). The perpendicular distance between these parallel planes is the same for both prisms.

**Step 13.** The first prism has base triangle ABC, and the second prism has base triangle ACD, and these bases are equal (Step 9). Both prisms have the same height (Step 12). By Proposition 11.24, the opposite faces of the parallelepiped are parallel. The lateral face ACGE of each prism is the shared cutting plane. The lateral face ABFE of the first prism equals the lateral face DCGH of the second prism, and the lateral face BCGF of the first prism equals the lateral face ADHE of the second prism (by 11.24).

**Step 14.** Since the two prisms have equal and similar opposite faces (their triangular bases are equal by Steps 9 and 10) and equal corresponding lateral faces (by Step 13 and 11.24), and these faces are similarly arranged, the two prisms are equal to one another (by Definition 11.10 and Common Notion 4).

**Step 15.** Therefore the plane ACGE through the diagonals of the opposite faces bisects the parallelepipedal solid into two equal prisms. This is what was to be proved.

**USED:** 1.34, 11.24, CN1, CN4, D11.10, D11.13
**Human refs (from References field):** 1.34, D11.10
**Jaccard:** 0.333 — AI adds ['11.24', 'CN1', 'CN4', 'D11.13']

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let the parallelepipedal solids CM and CN be on the same base AB and of the same height, and let the extremities of their edges which stand up, namely the points E, F, G, H and E', F', G', H', lie on the same straight lines EE' and FF' respectively. Specifically, let solid CM have base ABCD with top face EFGH, and solid CN have the same base ABCD with top face E'F'G'H', where AE, BF, CG, DH are the standing edges of the first solid, and AE', BF', CG', DH' are the standing edges of the second. The points E, E' lie on one straight line and H, H' lie on its continuation (or the same line), while F, F' and G, G' lie on another straight line.

**Step 2.** Since CM is a parallelepiped, the face AE is a parallelogram, so AE is parallel to and equal to DH, and similarly BF is parallel to and equal to CG, by 11.24. Likewise, since CN is a parallelepiped, AE' is parallel to and equal to DH', and BF' is parallel to and equal to CG', by 11.24.

**Step 3.** Since AE is parallel to DH (both being edges standing up from the same base and part of a parallelepiped), and the extremities E, H lie on straight lines with E', H' respectively, the quadrilateral EE'H'H is a parallelogram, because EH is parallel to E'H' (both being sides of parallelogram top faces EFGH and E'F'G'H' opposite to the common direction) and EE' is parallel to HH' since AE is parallel to DH and AE' is parallel to DH'. By 1.34, EE' equals HH' and EH equals E'H'.

**Step 4.** Similarly, FF'G'G is a parallelogram, with FF' equal to GG', by the same reasoning using 1.34.

**Step 5.** Since EE' is equal to HH' and FF' is equal to GG', and EF is equal to HG (as opposite sides of parallelogram EFGH, by 1.34), and E'F' is equal to H'G' (as opposite sides of parallelogram E'F'G'H', by 1.34), the quadrilaterals EFGE' (more precisely the faces of the auxiliary solids) form parallelograms.

**Step 6.** Consider now the solid with vertices E, F, G, H, E', F', G', H'. The faces EE'F'F, HH'G'G, EE'H'H, FF'G'G, EFGH, and E'F'G'H' are all parallelograms (shown in Steps 3, 4, and by 11.24 applied to the original solids). Therefore this solid EE'FF'GG'HH' is itself a parallelepiped, by D11.13 and the characterization in 11.24.

**Step 7.** Now the solid CM (which is ABCD-EFGH) can be decomposed as follows. The plane through the diagonal EG of the top face EFGH and the corresponding diagonal of the base bisects the parallelepiped CM, by 11.28. Similarly, solid CN (which is ABCD-E'F'G'H') is bisected by the plane through its corresponding diagonals.

**Step 8.** Consider the auxiliary parallelepiped with top face EE'F'F and bottom face HH'G'G (the solid formed by the region between the two top faces and the standing edges). By 11.28, this solid is bisected by the plane through its diagonals.

**Step 9.** Now observe that solid CM equals the solid ABCD-EFGH. We add and subtract the same auxiliary pieces to relate CM and CN. The solid with base ABFE and top AE'BF' (a prism-shaped piece) is common to both solids CM and CN, since both share the base AB and the edges AE, BF (for CM) overlap with AE', BF' (for CN) in a common region.

**Step 10.** More precisely, the solid CM is composed of the prism on triangle ABE (extending to the corresponding upper region) and complementary pieces, and CN is composed similarly. Consider the solid whose base is the parallelogram ABFE and whose top is ABF'E'. The face ABFE is a parallelogram (since AE is parallel to BF by 11.24), and similarly ABF'E' is a parallelogram. The solid ABFE-E'F' forms part of both decompositions.

**Step 11.** To make the argument precise: solid CM can be written as the sum of (i) the solid on base ABFE with top ABF'E' and (ii) the solid on the remaining part of the base with the corresponding top shifted by EE'. Similarly solid CN consists of the same solid (i) and a complementary piece. But these complementary pieces are equal because the parallelogram EE'H'H equals FF'G'G (both being faces of the auxiliary parallelepiped from Step 6), and the heights are equal.

**Step 12.** By the key argument: since EFGH and E'F'G'H' are both parallelograms on the same parallel lines (EE' and HH' on one side, FF' and GG' on the other), parallelogram EFGH is equal to parallelogram E'F'G'H', by 1.35 (parallelograms on the same base and between the same parallels are equal — applied in the plane of the top faces, where EH = E'H' and EF = E'F' as bases between the same parallels).

**Step 13.** Now the solid CM has base ABCD and top EFGH with standing edges AE, BF, CG, DH. The solid CN has the same base ABCD and top E'F'G'H' with standing edges AE', BF', CG', DH'. Consider the prism formed by triangle AEE' extended along the parallelepiped to the opposite face triangle DHH'. This prism equals the prism formed by triangle BFF' extended to CGG', because AE equals BF, AE' equals BF', and EE' equals FF' (by 1.34 applied to the respective parallelogram faces), and the triangles are congruent by 1.8, with equal heights.

**Step 14.** Solid CM equals the auxiliary solid (with top face EE'F'F and base HH'G'G, the parallelepiped from Step 6) plus the solid CN, minus two prisms. But equally, solid CN equals the same auxiliary solid plus solid CM minus the same two prisms. By the symmetry of the decomposition, we can argue directly.

**Step 15.** To complete the proof cleanly: the solid CM consists of the solid with edges AB, CD on the base and EF, GH on top, together with prisms on the sides. Specifically, CM = solid(ABF'E'-DCG'H') + prism(E,E',F,F' extended to H,H',G,G') applied to one side. And CN = solid(ABF'E'-DCG'H') + prism on the other side. But these prisms are equal because their triangular cross-sections EE'F' and HH'G' are congruent (by 1.8, since EE' = HH', EF = HG from 1.34, and E'F' = H'G' from 1.34) and they have equal heights (the distance between the parallel planes of ABCD and EFGH, which equals the distance to E'F'G'H' since the solids have the same height).

**Step 16.** More directly: solid CM is the sum of solid CN, plus the prism on one side, minus the prism on the other side. Since these two prisms are equal (as shown in Step 15), adding one and subtracting an equal one leaves the solid unchanged. Therefore solid CM equals solid CN.

**Step 17.** Therefore parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another. Q.E.D.

**USED:** 1.34, 1.35, 1.8, 11.24, 11.28, CN2, CN3, D11.13
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.200 — AI adds ['1.35', '11.24', '11.28', 'CN2', 'CN3', 'D11.13']; Human adds ['1.36', '1.4']

## Proposition 11.30
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another.

**Step 1.** Let the two parallelepipedal solids CM and CN stand on the same base AB (the parallelogram ABCD) and have the same height, and let the extremities of their standing edges not be on the same straight lines. Let the standing edges of CM terminate above in the parallelogram FGHK (with AF, BG, CH, DK as standing edges), and let the standing edges of CN terminate above in the parallelogram LMNO (with AL, BM, CN, DO as standing edges). By 11.24, the top faces FGHK and LMNO are parallelograms.

**Step 2.** Since FGHK is a parallelogram, FK is parallel to GH and FG is parallel to KH, by 1.34. Since LMNO is a parallelogram, LO is parallel to MN and LM is parallel to ON, by 1.34. All standing edges of each solid are mutually parallel (by 11.24 applied to opposite faces), and since the two solids have the same base, the top vertices of both solids lie in a common plane at the same height above the base.

**Step 3.** In this common upper plane, produce lines FK and LO; since they are not in general parallel, let them meet or be extended as needed. Similarly produce lines GH and MN. Specifically, produce NK and GF until they meet at a point Q, and produce ML and HE (that is, the standing-edge endpoints along the other pair of sides) until they meet at a point P. By P1 and P2, such productions and line drawings are possible.

**Step 4.** Now construct the parallelepiped CR whose base is the same parallelogram ABCD and whose top face is determined by the parallelogram whose sides lie along the lines FG-produced and LO-produced (and their parallels GH-produced and MN-produced). That is, the top face of CR has its vertices at the intersections of lines through F and G on one hand and through L and O (or M and N) on the other.

**Step 5.** By this construction, the extremities of the standing edges of CR lie on the same straight lines as those of CM along two opposite sides (namely, along lines FG and KH, or their productions). Therefore the solids CM and CR are parallelepipeds on the same base AB, of the same height, and with the extremities of their standing edges on the same straight lines. By 11.29, solid CM equals solid CR.

**Step 6.** Likewise, the extremities of the standing edges of CR lie on the same straight lines as those of CN along the other two opposite sides (namely along lines LM and ON, or their productions). Therefore the solids CN and CR are parallelepipeds on the same base AB, of the same height, and with the extremities of their standing edges on the same straight lines. By 11.29, solid CN equals solid CR.

**Step 7.** Since solid CM equals solid CR, and solid CN equals solid CR, by CN1 (things equal to the same thing are equal to one another), solid CM equals solid CN.

**Step 8.** Therefore, parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another. Q.E.D.

**USED:** 1.34, 11.24, 11.29, CN1, P1, P2
**Human refs (from References field):** 11.29
**Jaccard:** 0.167 — AI adds ['1.34', '11.24', 'CN1', 'P1', 'P2']

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let the parallelepipedal solids AB and CD be on equal bases, namely the parallelograms FGHK and LMNO respectively, and let them have the same height. We must prove that solid AB equals solid CD.

**Step 2.** On the straight line FG, and at the point F on it, apply the parallelogram FGPQ equal to the parallelogram LMNO in the angle GFQ equal to angle MLO, using Proposition 1.45. Since FGHK and LMNO are equal by hypothesis, and FGPQ equals LMNO by construction, it follows that FGPQ equals FGHK [CN1].

**Step 3.** Erect on the base FGPQ a parallelepipedal solid RS with the same height as solids AB and CD, and with the edges standing up from F, G, P, Q parallel to the corresponding edges of solid AB standing up from F, G, H, K. This is possible by Proposition 11.27 (describing a parallelepiped similar and similarly situated to a given one on a given line) and the construction of parallel lines by Proposition 1.31.

**Step 4.** Since solid AB stands on base FGHK and solid RS stands on base FGPQ, and these two bases are equal (as shown in Step 2), and both solids have the same height, and they share the edge FG with their lateral edges from F and G being the same lines, the remaining lateral edges stand up from H, K and from P, Q respectively. Since FGHK and FGPQ are equal parallelograms on the same straight line FG, they lie in the same plane [11.7, 11.2]. The solids AB and RS are on the same base line FG with the same height.

**Step 5.** Now, solids AB and RS are on the same base (sharing the side FG in the base plane) and of the same height, with lateral edges standing up from the vertices of their respective bases. If the extremities of the sides which stand up lie on the same straight lines, then by Proposition 11.29 the solids are equal. If not, then by Proposition 11.30 they are still equal. In either case, solid AB equals solid RS.

**Step 6.** Similarly, since solid CD stands on base LMNO and solid RS stands on base FGPQ, and FGPQ was constructed equal to LMNO (Step 2), we must show solid CD equals solid RS. Apply the same method: on the straight line LM, we could construct the comparison, or equivalently, since FGPQ = LMNO, we construct on LM a parallelogram equal to FGPQ in the appropriate angle. But more directly: erect on LMNO a parallelepiped with the same lateral edge directions as RS. Since FGPQ equals LMNO and both solids have the same height, the same argument using 11.29 or 11.30 shows solid CD equals solid RS.

**Step 7.** Since solid AB equals solid RS (Step 5) and solid CD equals solid RS (Step 6), by Common Notion 1, solid AB equals solid CD.

**Step 8.** Therefore, parallelepipedal solids which are on equal bases and of the same height are equal to one another. Q.E.D.

**USED:** 1.31, 1.45, 11.2, 11.27, 11.29, 11.30, 11.7, CN1
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.125 — AI adds ['1.31', '1.45', '11.2', '11.27', '11.7', 'CN1']; Human adds ['1.23', '1.35', '11.24', '11.25', '5.11', '5.7', '5.9', 'D11.10']

## Proposition 11.32
**Statement:** Parallelepipedal solids which are of the same height are to one another as their bases.

**Step 1.** Let AB and CD be two parallelepipedal solids of the same height, with bases AE and CF respectively. We are to prove that solid AB is to solid CD as base AE is to base CF.

**Step 2.** On one side of the base AE, construct a parallelogram GM equal to the base CF, in the same rectilineal angle as the base AE. This is possible by 1.45, which allows us to construct in a given rectilineal angle a parallelogram equal to a given rectilineal figure.

**Step 3.** Complete the parallelepiped GO on the base GM with the same height as solid AB, using the same standing edges (i.e., edges parallel to and equal to those of AB). Since GM lies in the same plane as AE and shares an edge with it, and the standing edges are the same, the solids AB and GO together form a single parallelepiped, with AB and GO as two parts separated by a plane through their shared face, this plane being parallel to the opposite faces of the combined solid.

**Step 4.** By 11.25, when a parallelepipedal solid is cut by a plane parallel to its opposite faces, the two resulting solids are to one another as their bases. Applying this to the combined solid cut into AB and GO, we obtain solid AB : solid GO = base AE : base GM.

**Step 5.** Now, the base GM equals the base CF by construction (Step 2). Furthermore, solid GO and solid CD are parallelepipeds that have equal bases (since base GM = base CF) and the same height (since GO has the same height as AB, and AB and CD have the same height by hypothesis). Therefore, by 11.31, solid GO equals solid CD.

**Step 6.** Since solid AB : solid GO = base AE : base GM (Step 4), and solid GO = solid CD (Step 5), and base GM = base CF (Step 2), we may substitute equals: equal magnitudes have the same ratio to the same magnitude, and the same magnitude has the same ratio to equal magnitudes, by 5.7. Therefore solid AB : solid CD = base AE : base CF.

**Step 7.** Therefore, parallelepipedal solids which are of the same height are to one another as their bases. Q.E.D.

**USED:** 1.45, 11.25, 11.31, 5.7
**Human refs (from References field):** 1.45, 11.25, 11.31
**Jaccard:** 0.750 — AI adds ['5.7']

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

**Step 1.** Let AB and CD be similar parallelepipedal solids, and let AE be the side of AB corresponding to CF, the side of CD. We must show that solid AB is to solid CD in the triplicate ratio of AE to CF.

**Step 2.** Since AB and CD are similar parallelepipedal solids, by D11.9 they are contained by similar planes equal in multitude, and by D6.1 the sides about the equal angles are proportional. Let the three edges of AB meeting at one vertex be AE, AG, AH, and the corresponding three edges of CD meeting at one vertex be CF, CK, CL. Then AE : CF = AG : CK = AH : CL, and the angles at these vertices are respectively equal.

**Step 3.** Produce the edge AE to the point N such that AE, CF, EN are in continued proportion, that is, AE : CF = CF : EN. Further, produce to P such that CF : EN = EN : EP, giving four terms AE, CF, EN, EP in continued proportion. Then by D5.10, AE has to EP the triplicate ratio of that which AE has to CF.

**Step 4.** On AE, construct the parallelogram AEKM with the same angles as the base face of AB, making the second edge AK equal to AG. This parallelogram is the base of solid AB. Similarly, on CF construct the base parallelogram of solid CD with edges CF and CK.

**Step 5.** On EN, construct the parallelepiped with edge EN and the other two edges equal to CK and CL respectively, and with the same angles as in CD. Call this solid S1. By 11.27, we can describe on any given straight line a parallelepiped similar and similarly situated to a given one. Since AE : CF = CF : EN and AE : CF = AG : CK = AH : CL, the solid on EN with edges EN, CK, CL has its edges proportional to those of CD in a determinate way.

**Step 6.** On EP, similarly construct the parallelepiped S2 with edges EP, CK, CL and the same angles as CD.

**Step 7.** Since AE : CF = AG : CK (from similarity of AB and CD, Step 2), and AE : CF = CF : EN (by construction, Step 3), we have AG : CK = CF : EN. The base face of AB is the parallelogram with sides AE, AG, and the base face of S1 has sides EN, CK. Now the base of AB (with sides AE, AG) and the base of S1 (with sides CF, CK) -- consider instead: the base of the solid with edge CF has sides CF, CK, and the base of S1 has sides EN, CK. Since these two bases share the same second edge CK and their first edges are CF and EN respectively, by 6.1 the base on CF, CK is to the base on EN, CK as CF is to EN.

**Step 8.** Now consider solid AB which has edges AE, AG, AH and the solid CD which has edges CF, CK, CL. Since AB and CD are similar, the base faces (with sides AE, AG and CF, CK respectively) are similar parallelograms. By 6.22, since AE : CF = AG : CK, the similar parallelograms on AE, AG and on CF, CK are in the duplicate ratio of AE to CF. That is, base(AB) : base(CD) = AE^2 : CF^2 (the duplicate ratio of AE to CF, by D5.9).

**Step 9.** Since base(AB) : base(CD) is the duplicate ratio of AE to CF, and AE : CF = CF : EN (Step 3), we have AE : EN is the duplicate ratio of AE to CF (by D5.9 since AE, CF, EN are three proportionals). Therefore base(AB) : base(CD) = AE : EN.

**Step 10.** Now AB and CD have corresponding heights AH and CL. But AE : CF = AH : CL (from similarity, Step 2). Consider constructing on the base of CD a solid CD' with the same base as CD but with height AH instead of CL. Then by 11.25, solid CD' : solid CD = AH : CL = AE : CF.

**Step 11.** Consider solids AB and CD'. They have the same height AH. By 11.32, parallelepipeds of the same height are to one another as their bases. Therefore AB : CD' = base(AB) : base(CD).

**Step 12.** From Step 9, base(AB) : base(CD) = AE : EN. So AB : CD' = AE : EN.

**Step 13.** From Step 10, CD' : CD = AE : CF. And from construction (Step 3), AE : CF = CF : EN, so CF : EN = EN : EP. This gives us CD' : CD = AE : CF.

**Step 14.** We now chain the ratios using 5.22 (ex aequali). We have:
- AB : CD' = AE : EN (Step 12)
- CD' : CD = AE : CF (Step 13)

From the continued proportion AE, CF, EN, EP (Step 3), AE : CF = CF : EN = EN : EP. So AE : EN = AE : EN (the duplicate ratio of AE to CF), and AE : CF is the first ratio. Multiplying: AB : CD' and CD' : CD taken together give AB : CD.

**Step 15.** By 5.22 (ex aequali), from AB : CD' = AE : EN and CD' : CD = EN : EP, we obtain AB : CD = AE : EP.

**Step 16.** But AE, CF, EN, EP are four magnitudes in continued proportion (Step 3), so by D5.10, AE has to EP the triplicate ratio of that which AE has to CF.

**Step 17.** Therefore AB : CD = AE : EP, and AE to EP is the triplicate ratio of AE to CF. Hence the solid AB has to the solid CD the triplicate ratio of that which the corresponding side AE has to the corresponding side CF.

**Step 18.** Therefore, similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides. Q.E.D.

**USED:** 11.25, 11.27, 11.32, 5.22, 6.1, 6.22, D11.9, D5.10, D5.9, D6.1
**Human refs (from References field):** 11.24, 11.32, 6.1, D11.10, D5.10
**Jaccard:** 0.250 — AI adds ['11.25', '11.27', '5.22', '6.22', 'D11.9', 'D5.9', 'D6.1']; Human adds ['11.24', 'D11.10']

## Proposition 11.34
**Statement:** In equal parallelepipedal solids the bases are reciprocally proportional to the heights; and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let AB and CD be two parallelepipedal solids with bases EH and NQ respectively, and with perpendicular heights h_AB and h_CD respectively. We are to show: (forward) if AB equals CD then EH : NQ = h_CD : h_AB, and (converse) if EH : NQ = h_CD : h_AB then AB equals CD.

**Step 2.** Construct a parallelepiped FO on the base NQ with the same height as AB, namely height h_AB. This parallelepiped shares the base NQ with CD but has the height of AB.

**Step 3.** Since AB and FO are parallelepipedal solids of the same height h_AB, by 11.32 (parallelepipeds of the same height are to one another as their bases), AB : FO = EH : NQ. --- (i)

**Step 4.** We now establish that CD : FO = h_CD : h_AB. Both FO and CD stand on base NQ with heights h_AB and h_CD respectively. If h_AB equals h_CD, then FO equals CD by 11.31 (parallelepipeds on equal bases and of the same height are equal), and the ratio is one of equality. Assume then that h_AB is less than h_CD; the case h_AB greater than h_CD is handled symmetrically by cutting FO instead of CD.

**Step 5.** Cut the parallelepiped CD by a plane through its interior parallel to its base NQ at perpendicular height h_AB from the base. This plane is parallel to the pair of opposite faces consisting of the base and the top face. The cut divides CD into two parallelepipedal solids: a lower piece S1 on base NQ with height h_AB, and an upper piece S2 on a base congruent to NQ with height h_CD minus h_AB.

**Step 6.** By 11.25 (if a parallelepiped is cut by a plane parallel to opposite faces, the resulting solids are as their bases), S1 : S2 equals the ratio of the relevant bases. Since the cutting plane is parallel to the top and bottom faces, the bases in the sense of 11.25 are the portions of a lateral face divided by the cutting plane. These portions are two parallelograms sharing the same edge (a side of NQ) with perpendicular heights h_AB and h_CD minus h_AB respectively. By 6.1 (parallelograms under the same height are as their bases, applied here to parallelograms on the same base, whose ratio equals that of their heights), these lateral face portions are as h_AB to h_CD minus h_AB. Therefore S1 : S2 = h_AB : (h_CD minus h_AB). --- (ii)

**Step 7.** Since S1 is a parallelepiped on base NQ with height h_AB, and FO is likewise a parallelepiped on the equal base NQ with the same height h_AB, by 11.31, S1 equals FO.

**Step 8.** Since S1 and S2 together compose CD, we have S1 + S2 = CD, that is, CD = FO + S2 (substituting S1 = FO from Step 7).

**Step 9.** From (ii), S1 : S2 = h_AB : (h_CD minus h_AB). By the definition of inverse ratio (D5.13), S2 : S1 = (h_CD minus h_AB) : h_AB.

**Step 10.** By 5.18 (if magnitudes are proportional separando, they are also proportional componendo), from S2 : S1 = (h_CD minus h_AB) : h_AB we obtain (S2 + S1) : S1 = ((h_CD minus h_AB) + h_AB) : h_AB, that is, (S2 + S1) : S1 = h_CD : h_AB.

**Step 11.** Since S2 + S1 = CD (Step 8) and S1 = FO (Step 7), we conclude CD : FO = h_CD : h_AB. --- (iii)

**Step 12.** [Forward direction] Now suppose AB equals CD. Since AB equals CD, by 5.7 (equal magnitudes have the same ratio to the same magnitude), AB : FO = CD : FO.

**Step 13.** From (i), AB : FO = EH : NQ. From (iii), CD : FO = h_CD : h_AB. Since AB : FO = CD : FO (Step 12), by 5.11 (ratios which are the same with the same ratio are also the same with one another), EH : NQ = h_CD : h_AB. Thus the bases are reciprocally proportional to the heights.

**Step 14.** [Converse] Now suppose EH : NQ = h_CD : h_AB. From (i), AB : FO = EH : NQ. By hypothesis, EH : NQ = h_CD : h_AB. Therefore AB : FO = h_CD : h_AB.

**Step 15.** From (iii), CD : FO = h_CD : h_AB. Therefore AB : FO = CD : FO by 5.11 (both ratios equal h_CD : h_AB).

**Step 16.** By 5.9 (magnitudes which have the same ratio to the same magnitude are equal to one another), AB equals CD. This completes the proof of both directions.

**USED:** 11.25, 11.31, 11.32, 5.11, 5.18, 5.7, 5.9, 6.1, D5.13
**Human refs (from References field):** 11.25, 11.29, 11.30, 11.31, 11.32, 5.7, 5.9, 6.1
**Jaccard:** 0.545 — AI adds ['5.11', '5.18', 'D5.13']; Human adds ['11.29', '11.30']

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

**Step 1.** Let the two equal plane angles be angle BAC and angle EDF, situated in planes P1 and P2 respectively, with angle BAC equal to angle EDF. Let AG and DM be elevated straight lines set up at vertices A and D, making angle BAG equal to angle EDM and angle CAG equal to angle FDM. Let G be any point on AG. Make DM equal to AG by cutting off on DM (or its extension) a length equal to AG [1.3].

**Step 2.** From the elevated point G, draw GH perpendicular to plane P1 [11.11], meeting the plane at H. From the elevated point M, draw MK perpendicular to plane P2 [11.11], meeting the plane at K. Join AH and DK [P1].

**Step 3.** Since GH is at right angles to the plane P1, it makes right angles with every straight line through H lying in P1 [D11.3]. In particular, angle GHA is a right angle [D1.10]. Similarly, since MK is at right angles to plane P2, angle MKD is a right angle. All right angles are equal to one another [P4].

**Step 4.** In the plane containing G and line AB [11.2], let J be the foot of the perpendicular from G to line AB [1.12], so that angle GJA is a right angle. We show that J is also the foot of the perpendicular from H to AB: Since GH is perpendicular to plane P1 and the line HJ lies in P1 through H, angle GHJ is a right angle [D11.3]. By the Pythagorean theorem on right triangle GHJ, GH squared plus HJ squared equals GJ squared [1.47]. For any other point J-prime on AB distinct from J, angle GHJ-prime is likewise a right angle [D11.3], so GH squared plus HJ-prime squared equals GJ-prime squared [1.47]. Since angle GJA is a right angle and J-prime lies on AB, the triangle GJJ-prime has a right angle at J, giving GJ squared plus JJ-prime squared equals GJ-prime squared [1.47]. Substituting, HJ-prime squared equals HJ squared plus JJ-prime squared. By the converse of the Pythagorean theorem [1.48], angle HJJ-prime is a right angle. Since JJ-prime lies along AB, this means HJ is perpendicular to AB at J. Hence J is the foot of the perpendicular from H to line AB.

**Step 5.** By the same reasoning, let I be the foot of the perpendicular from G to line AC; then I is also the foot of the perpendicular from H to AC, with angle GIA and angle HIA both right angles. In the second configuration, let L be the foot of the perpendicular from M (and from K) to line DE, and N the foot of the perpendicular from M (and from K) to line DF, with right angles at L and N established by the same argument.

**Step 6.** In right triangles AGJ and DML: angle AJG equals angle DLM (both right angles, equal by P4), angle JAG equals angle BAG which equals angle EDM which equals angle LDM (given), and the side AG equals DM (Step 1), where AG subtends the right angle. By 1.26, the triangles are congruent, so AJ equals DL and GJ equals ML.

**Step 7.** In right triangles AGI and DMN: angle AIG equals angle DNM (both right angles), angle IAG equals angle CAG which equals angle FDM which equals angle NDM (given), and AG equals DM. By 1.26, the triangles are congruent, so AI equals DN and GI equals MN.

**Step 8.** Join JI and LN [P1]. In triangles AJI and DLN: AJ equals DL (Step 6), AI equals DN (Step 7), and the included angle JAI equals angle BAC which equals angle EDF which equals angle LDN. By 1.4, the triangles are congruent, giving JI equal to LN, angle AJI equal to angle DLN, and angle AIJ equal to angle DNL.

**Step 9.** Since angle HJA is a right angle (Step 4) and the ray JI lies in the interior of angle HJA (as both H and I are in the interior of angle BAC on the same side of line AB), the angle HJI and angle IJA together make up the right angle HJA. Thus angle HJI equals the right angle minus angle AJI [CN3]. Similarly, angle KLN equals the right angle minus angle DLN. Since angle AJI equals angle DLN (Step 8), angle HJI equals angle KLN.

**Step 10.** Since angle HIA is a right angle (Step 5) and the ray IJ lies in the interior of angle HIA, the angle HIJ equals the right angle minus angle AIJ [CN3]. Similarly, angle KNL equals the right angle minus angle DNL. Since angle AIJ equals angle DNL (Step 8), angle HIJ equals angle KNL.

**Step 11.** In triangles HJI and KLN: angle HJI equals angle KLN (Step 9), angle HIJ equals angle KNL (Step 10), and the side JI equals LN (Step 8). By 1.26, the triangles are congruent, so JH equals LK.

**Step 12.** In right triangles AJH and DLK: AJ equals DL (Step 6), JH equals LK (Step 11), and the included right angles at J and L are equal [P4]. By 1.4, the triangles are congruent, so AH equals DK.

**Step 13.** In right triangles GAH and MDK: the side GA equals MD (Step 1), the side AH equals DK (Step 12), and the included right angles GHA and MKD are equal [P4, Step 3]. By 1.4, the triangles are congruent. Therefore angle GAH equals angle MDK.

This is what was to be proved: the angles contained by the elevated straight lines and the lines joining the feet of the perpendiculars to the vertices are equal.

**USED:** 1.12, 1.26, 1.3, 1.4, 1.47, 1.48, 11.11, 11.2, CN3, D1.10, D11.3, P1, P4
**Human refs (from References field):** 1.26, 1.4, 1.47, 1.48, 1.8, 11.8
**Jaccard:** 0.267 — AI adds ['1.12', '1.3', '11.11', '11.2', 'CN3', 'D1.10', 'D11.3', 'P1', 'P4']; Human adds ['1.8', '11.8']

## Proposition 11.36
**Statement:** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

**Step 1.** Let A, B, C be three straight lines in continued proportion, so that A : B = B : C [D5.6, D5.8]. Let S be the parallelepipedal solid formed out of A, B, C, having given solid angles. Let T be the parallelepipedal solid on B which is equilateral (all three edges equal to B) and equiangular with S (having the same solid angles as S).

**Step 2.** Consider the bases of S and T. The base of S is the parallelogram contained by edges of length A and B, at a given angle determined by the solid angle at the base. The base of T is the parallelogram contained by edges of length B and B, at the same angle (since T is equiangular with S). Thus the two base parallelograms are equiangular.

**Step 3.** Since both base parallelograms have one pair of sides equal to B at the same included angle, the perpendicular heights drawn from these sides of length B to the opposite sides are equal (each being B times the sine of the common angle). Therefore the two base parallelograms are under the same height.

**Step 4.** Since the two base parallelograms are under the same height, by Proposition 6.1, parallelogram(A, B) : parallelogram(B, B) = A : B. That is, base of S : base of T = A : B.

**Step 5.** Since A : B = B : C (given), we have base of S : base of T = B : C.

**Step 6.** The height of the parallelepiped T is B, and the height of the parallelepiped S is C (measured in the direction perpendicular to their respective bases, which is the same direction since the solids are equiangular). Therefore height of T : height of S = B : C.

**Step 7.** From Steps 5 and 6, base of S : base of T = height of T : height of S. That is, the bases of the parallelepipedal solids S and T are reciprocally proportional to their heights.

**Step 8.** Since S and T are equiangular parallelepipedal solids whose bases are reciprocally proportional to their heights, by the converse part of Proposition 11.34, the solid S is equal to the solid T.

**Step 9.** Therefore the parallelepipedal solid formed out of the three proportional straight lines A, B, C is equal to the equilateral parallelepipedal solid on the mean B which is equiangular with it. Q.E.D.

**USED:** 11.34, 6.1, D5.6, D5.8
**Human refs (from References field):** 11.31, 11.35, 6.14
**Jaccard:** 0.000 — AI adds ['11.34', '6.1', 'D5.6', 'D5.8']; Human adds ['11.31', '11.35', '6.14']

## Proposition 11.37
**Statement:** If four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described will also be proportional; and, if the parallelepipedal solids on them which are similar and similarly described be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let A, B, C, D be four straight lines such that A is to B as C is to D. On A, B, C, D let similar and similarly described parallelepipedal solids AE, BF, CG, DH be constructed respectively.

**Step 2.** We must show first that AE is to BF as CG is to DH, and conversely.

**Part I (Forward direction): Assume A : B :: C : D. Prove AE : BF :: CG : DH.**

**Step 3.** Since AE and BF are similar parallelepipedal solids described on A and B respectively, by 11.33, AE is to BF in the triplicate ratio of A to B. That is, AE : BF is the triplicate of A : B.

**Step 4.** Similarly, since CG and DH are similar parallelepipedal solids described on C and D respectively, by 11.33, CG is to DH in the triplicate ratio of C to D. That is, CG : DH is the triplicate of C : D.

**Step 5.** Since A : B :: C : D (given), the triplicate ratio of A to B equals the triplicate ratio of C to D. To see this: since A : B :: C : D, take the three mean proportionals. Let A : B :: B' : B'' be continued so that A has to B'' the triplicate ratio of A to B (by D5.10), and similarly let C : D :: D' : D'' so that C has to D'' the triplicate ratio of C to D. Since A : B :: C : D, and proportional lines yield proportional continued proportions, the triplicate ratios are the same. More precisely, since A : B :: C : D, by 5.11 any ratio equal to A : B is also equal to C : D; the triplicate ratio is uniquely determined by the base ratio, so the triplicate of A : B equals the triplicate of C : D.

**Step 6.** Since AE : BF is the triplicate of A : B (Step 3), and CG : DH is the triplicate of C : D (Step 4), and the triplicate of A : B equals the triplicate of C : D (Step 5), therefore AE : BF :: CG : DH, by 5.11.

**Part II (Converse): Assume AE : BF :: CG : DH. Prove A : B :: C : D.**

**Step 7.** Since AE and BF are similar parallelepipedal solids on A and B, by 11.33, AE : BF is the triplicate ratio of A to B.

**Step 8.** Since CG and DH are similar parallelepipedal solids on C and D, by 11.33, CG : DH is the triplicate ratio of C to D.

**Step 9.** Since AE : BF :: CG : DH (given), and AE : BF is the triplicate of A : B, and CG : DH is the triplicate of C : D, it follows that the triplicate ratio of A to B equals the triplicate ratio of C to D, by 5.11.

**Step 10.** Now, if the triplicate ratio of A to B equals the triplicate ratio of C to D, then A : B :: C : D. For by D5.9 and D5.10, the triplicate ratio is built from the base ratio by continued proportion; if the triplicate ratios are equal, the base ratios must be equal, since by 5.9, if the first of three proportionals has to the third the duplicate ratio of what it has to the second, equal duplicate ratios force equal simple ratios, and the argument extends to triplicate ratios via the same reasoning. Alternatively, on A find B' such that A : B :: A : B' yields the same continued proportion; since equal triplicate ratios give equal final terms, the base ratios coincide.

**Step 11.** Therefore A : B :: C : D.

**Step 12.** Hence, if four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described are also proportional; and if the parallelepipedal solids on them which are similar and similarly described be proportional, the straight lines are themselves also proportional. Q.E.D.

**USED:** 11.33, 5.11, 5.9, D5.10, D5.9
**Human refs (from References field):** 11.33
**Jaccard:** 0.200 — AI adds ['5.11', '5.9', 'D5.10', 'D5.9']

## Proposition 11.38
**Statement:** If the sides of the opposite planes of a cube be bisected, and planes be carried through the points of section, the common section of the planes and the diameter of the cube bisect one another.

**Step 1.** Let ABCDEFGH be a cube, where ABCD is one face and EFGH is the opposite face, with edges AE, BF, CG, DH joining corresponding vertices, so that A is below E, B below F, C below G, and D below H. By D11.25, all six faces are equal squares. Let the diameter (space diagonal) of the cube be AG, joining vertex A to the opposite vertex G. [D11.25, P1]

**Step 2.** By 11.24, since the cube is a parallelepipedal solid, its opposite faces are equal parallelograms. In particular, face ABCD and face EFGH are equal parallelograms, face ABFE and face DCGH are equal parallelograms, and face ADHE and face BCGF are equal parallelograms. By 1.34, opposite sides of each face are equal and parallel. [11.24, 1.34]

**Step 3.** Bisect the sides of opposite faces ABCD and EFGH. By 1.10, bisect AB at K, BC at L, CD at M, DA at N on face ABCD, and bisect EF at O, FG at P, GH at Q, HE at R on face EFGH. [1.10]

**Step 4.** The first cutting plane passes through K, O, Q, M (midpoints of corresponding edges AB, EF, GH, CD). The second cutting plane passes through L, P, R, N (midpoints of corresponding edges BC, FG, HE, DA). We must show the common section of these two planes and the diagonal AG bisect one another. [P1]

**Step 5.** In face ABCD, which is a parallelogram, the diagonals AC and BD bisect each other at a point S by 1.34. Thus S is the midpoint of diagonal AC and also the midpoint of diagonal BD. [1.34]

**Step 6.** We show that K, S, M are collinear, so that S lies on the first cutting plane. In triangle ABC, K is the midpoint of AB and S is the midpoint of AC. By 6.2 (converse), since AB and AC are cut proportionally at K and S respectively, the line KS is parallel to BC. In triangle ACD, S is the midpoint of AC and M is the midpoint of CD. By 6.2 (converse), the line SM is parallel to AD. Since BC is parallel to AD (opposite sides of parallelogram ABCD, by 1.34), lines KS and SM are each parallel to BC. By 1.30, lines parallel to the same line are parallel to one another; but KS and SM share the point S, and by D1.23 parallel lines do not meet. Therefore KS and SM cannot be distinct parallel lines, so they form one and the same straight line, and K, S, M are collinear. Hence S lies on line KM in the first cutting plane. [6.2, 1.34, 1.30, D1.23]

**Step 7.** By the same reasoning applied to triangles ABD and BCD: L is the midpoint of BC, S is the midpoint of BD, and N is the midpoint of DA. In triangle ABD, S (midpoint of BD) and N (midpoint of DA) give SN parallel to AB by 6.2. In triangle BCD, S (midpoint of BD) and L (midpoint of BC) give SL parallel to CD by 6.2. Since AB is parallel to CD (by 1.34), both SL and SN are parallel to AB. By the same argument as Step 6 (using 1.30 and D1.23), L, S, N are collinear. Hence S lies on line LN in the second cutting plane. [6.2, 1.34, 1.30, D1.23]

**Step 8.** By entirely analogous reasoning on face EFGH, the diagonals EG and FH bisect each other at point T by 1.34. The midpoints O, P, Q, R of sides EF, FG, GH, HE satisfy: O, T, Q are collinear (so T lies on line OQ in the first cutting plane) and P, T, R are collinear (so T lies on line PR in the second cutting plane). [1.34, 6.2, 1.30, D1.23]

**Step 9.** Since S lies on both the first and second cutting planes, and T lies on both the first and second cutting planes, the line ST is the common section of the two cutting planes within the cube, by 11.3. [11.3]

**Step 10.** We now establish that ACGE is a parallelogram. From face ABFE (a parallelogram by 11.24), AE is parallel to BF and AE equals BF, by 1.34. From face BCGF (a parallelogram by 11.24), BF is parallel to CG and BF equals CG, by 1.34. By 1.30, since AE and CG are each parallel to BF, AE is parallel to CG. By CN1, since AE equals BF and BF equals CG, AE equals CG. [11.24, 1.34, 1.30, CN1]

**Step 11.** Since AE and CG are equal and parallel, and A, C are at one pair of extremities while E, G are at the other pair, with AC and EG joining corresponding extremities in the same direction, by 1.33 the line AC is equal and parallel to the line EG. [1.33]

**Step 12.** By 11.7, since AE and CG are parallel, any line joining a point on AE to a point on CG lies in the same plane as AE and CG. In particular, the points A, C (on lines AE and CG respectively, taking A on AE and C on CG) and E, G all lie in one plane. Therefore the quadrilateral ACGE lies entirely in one plane. Since AC is parallel to EG and AE is parallel to CG (both pairs being also equal), ACGE is a parallelogram. [11.7]

**Step 13.** In parallelogram ACGE, S is the midpoint of side AC (from Step 5) and T is the midpoint of side EG (from Step 8). Since AC is parallel to EG and AC equals EG (from Step 11), the half-segments AS and TG are equal (each being half of equal segments, by CN1) and parallel (being corresponding halves of parallel lines in the same direction). [CN1]

**Step 14.** Since AS and TG are equal and parallel, with the joins AT and SG connecting their extremities in the same direction, by 1.33 the line AT is equal and parallel to the line SG. Thus ASTG is a parallelogram (having both pairs of opposite sides equal and parallel). [1.33]

**Step 15.** We verify that ASTG lies in a plane. Since AS and TG are parallel, by 11.7 any line joining a point on AS to a point on TG lies in the same plane. The points A, S, T, G all lie in this plane, so ASTG is a planar parallelogram. [11.7]

**Step 16.** In parallelogram ASTG, the diagonals are AG and ST. By 1.34, the diagonals of a parallelogram bisect each other. Therefore AG and ST bisect each other at their common point of intersection. [1.34]

**Step 17.** But AG is the diameter of the cube, and ST is the common section of the two cutting planes (from Step 9). Therefore the common section of the planes and the diameter of the cube bisect one another, which is what was to be proved.

**USED:** 1.10, 1.30, 1.33, 1.34, 11.24, 11.3, 11.7, 6.2, CN1, D1.23, D11.25, P1
**Human refs (from References field):** 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.9
**Jaccard:** 0.056 — AI adds ['1.10', '1.30', '1.34', '11.24', '11.3', '11.7', '6.2', 'CN1', 'D1.23', 'D11.25', 'P1']; Human adds ['1.14', '1.15', '1.26', '1.29', '1.4', '11.9']

## Proposition 11.39
**Statement:** If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms will be equal.

**Step 1.** Let the first prism have parallelogram ABDE as its base and height h, and let the second prism have triangle FGH as its base and height h. By hypothesis, parallelogram ABDE is double triangle FGH.

**Step 2.** The first prism is a triangular prism (with triangular cross-sections ABC and DEC, say) resting on its parallelogram face ABDE. Complete it to a parallelepiped Q1 by adjoining the congruent complementary prism on the other side of the diagonal plane through the triangular cross-sections. By 11.28, the diagonal plane bisects the parallelepiped Q1, so Q1 is double the first prism.

**Step 3.** Observe that Q1, viewed with face ABDE as its base, has height h. This is because the face of Q1 opposite to ABDE passes through the vertices of the triangular cross-sections that lie at perpendicular distance h from the plane of ABDE, which is exactly the height of the original prism. Thus Q1 is a parallelepiped with base ABDE and height h.

**Step 4.** Complete the second prism (with triangular base FGH and opposite triangular face F'G'H' at distance h) to a parallelepiped Q2 by constructing point K such that FGHK is a parallelogram, and correspondingly K' above so that F'G'H'K' is a parallelogram. By 11.28, the diagonal plane through FH and F'H' bisects Q2, so Q2 is double the second prism.

**Step 5.** The base of Q2 is the parallelogram FGHK. By 1.34, the diagonal FH divides parallelogram FGHK into two equal triangles FGH and FHK. Therefore parallelogram FGHK is double triangle FGH.

**Step 6.** Since parallelogram ABDE is double triangle FGH (given), and parallelogram FGHK is also double triangle FGH (Step 5), we conclude that parallelogram ABDE equals parallelogram FGHK (CN1, both being equal to double triangle FGH). Thus Q1 and Q2 have equal bases.

**Step 7.** The height of Q1 from base ABDE is h (Step 3), and the height of Q2 from base FGHK is h (the distance between the parallel triangular faces of the second prism, which equals the distance between the parallel bases FGHK and F'G'H'K' of Q2). Since Q1 and Q2 are parallelepipeds on equal bases and of the same height, by 11.31 they are equal: Q1 equals Q2.

**Step 8.** Now Q1 is double the first prism (Step 2), and Q2 is double the second prism (Step 4). Since Q1 equals Q2, the first prism is equal to the second prism, for halves of equals are equal (CN3). Therefore, if there be two prisms of equal height, one with a parallelogram as base and the other a triangle, and the parallelogram be double the triangle, the prisms are equal. Q.E.D.

**USED:** 1.34, 11.28, 11.31, CN1, CN3, D11.13
**Human refs (from References field):** 1.34, 11.28, 11.31
**Jaccard:** 0.500 — AI adds ['CN1', 'CN3', 'D11.13']
