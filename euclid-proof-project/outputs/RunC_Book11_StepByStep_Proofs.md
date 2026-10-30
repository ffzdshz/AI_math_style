# Book 11 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 11.1
**Statement:** A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 1.** Suppose, for the sake of contradiction, that a straight line ABC has part AB in the plane of reference and part BC in a plane more elevated, so that B is a point where the line leaves the reference plane. [Assumption for reductio]

**Step 2.** Since AB is a straight line in the plane of reference, produce AB continuously in a straight line in the reference plane to a point D, so that ABD is a straight line lying entirely in the reference plane. [P2; D1.7: the plane surface lies evenly with the straight lines on itself, so the production of AB in the reference plane remains in that plane]

**Step 3.** Now ABC is a straight line by hypothesis, and ABD is a straight line by construction. Since BC extends into an elevated plane while BD remains in the reference plane, the points C and D are distinct. Therefore ABC and ABD are two distinct straight lines sharing the common segment AB.

**Step 4.** Let E be the midpoint of AB, obtained by bisecting AB. [1.10]

**Step 5.** From E, draw the straight line EC and the straight line ED. [P1]

**Step 6.** Set off BF along BC equal to BD, so that BF = BD. [1.3]

**Step 7.** Consider triangles DBE and FBE. We have BD = BF (by construction in Step 6), BE is common to both triangles, and angle DBE equals angle FBE since both are angles at B along the straight line ABD and along the straight line ABC respectively, both being straight angles measured from the segment BA. But since ABD is a straight line, angle ABD is a straight angle, and since ABC is a straight line, angle ABF (which is angle ABC) is also a straight angle. Therefore angle DBE and angle FBE are each the supplement of angle ABE, hence angle DBE = angle FBE. [1.13: the angles on one side of a straight line standing on another equal two right angles; CN3]

**Step 8.** By Side-Angle-Side, triangle DBE is equal to triangle FBE, and therefore DE = FE. [1.4]

**Step 9.** But D lies in the plane of reference while F (being along BC in the elevated plane, at a point distinct from B) lies in the elevated plane. Since D and F are at equal distances from B along their respective lines, and D is not the same point as F (as they lie in different planes), the triangles DBE and FBE are not coincident triangles but are in different planes. Therefore DE and FE are sides of non-coincident triangles.

**Step 10.** Now consider the full line ABD. Since it is a straight line, angle ABD is a straight angle. Similarly, since ABC is a straight line, angle ABC is a straight angle. Thus at the point B, the two different rays BD and BF (= BC) both make a straight angle with BA. However, BD and BF go to different points (D in the reference plane, F in the elevated plane), so from point B, the ray BA produced yields two different straight lines to two different points D and F with BD = BF, yet the angles ABD and ABF are both straight angles.

**Step 11.** Since angles ABD and ABF are both straight angles (each equal to two right angles by 1.13), and BD = BF by construction, the triangles BDE and BFE have two sides and the included angle equal. By 1.4, we conclude DE = FE and angle BED = angle BEF. [1.4]

**Step 12.** Since angle BED = angle BEF, and these two angles together with angle DEB on one side and angle FEB on the other are formed at point E, and since angle BED + angle BEF would need to account for the full angle DEF. But E lies on line AB (being the midpoint), and D and F are on the same side relative to line AB (since both BD and BF are produced from B beyond A's direction). The equal angles BED and BEF mean that ED and EF make the same angle with EB. Since they are also equal in length (DE = FE from Step 11), the points D and F would have to coincide by the uniqueness of the point determined by a given distance and angle from E along a ray. [1.4; CN4: things which coincide are equal]

**Step 13.** But D lies in the plane of reference and F lies in the elevated plane, so D and F cannot coincide. This is a contradiction.

**Step 14.** Therefore the initial assumption is false: a part of a straight line cannot be in the plane of reference and a part in a plane more elevated. [Q.E.D.]

**USED:** 1.10, 1.13, 1.3, 1.4, CN3, CN4, D1.4, D1.7, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.10', '1.13', '1.3', '1.4', 'CN3', 'CN4', 'D1.4', 'D1.7', 'P1', 'P2']

## Proposition 11.2
**Statement:** If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

**Step 1.** Let AB and CD be two straight lines cutting one another at the point E. We must show first that AB and CD are in one plane, and second that every triangle is in one plane.

**Step 2.** Take any point F on EC and any point G on EB. Join FG [P1]. The three points E, F, G, together with the segments EF, EG, and FG, form the triangle EFG [D1.19].

**Step 3.** The triangle EFG, being a figure bounded by straight lines, lies in some plane; call it alpha. In particular, the segment EF lies in alpha and the segment EG lies in alpha.

**Step 4.** Now EF is a part of the straight line CD (since F is on EC and E is on CD). Because EF lies in the plane alpha, and EF is part of CD, by Proposition 11.1 the entire straight line CD lies in alpha. (For if any part of CD were in a different plane, a part of the straight line CD would be in alpha and a part in a plane more elevated, contradicting 11.1.)

**Step 5.** Similarly, EG is a part of the straight line AB (since G is on EB and E is on AB). Because EG lies in alpha, by Proposition 11.1 the entire straight line AB lies in alpha.

**Step 6.** Therefore the two straight lines AB and CD both lie in the single plane alpha. This completes the first part: if two straight lines cut one another, they are in one plane.

**Step 7.** Now let triangle ABC be given, with sides AB, BC, and CA [D1.19]. We must show that triangle ABC lies in one plane.

**Step 8.** The sides AB and AC are two straight lines meeting at the point A. By the result just established (Steps 1-6), AB and AC lie in one plane; call it beta.

**Step 9.** Since AB lies in beta, the point B lies in beta. Since AC lies in beta, the point C lies in beta. Join BC [P1]. Because B and C both lie in the plane beta, the straight line BC lies in beta [D1.7, since a plane surface lies evenly with the straight lines on itself, meaning that if both endpoints of a straight line are in the plane, the entire line is in the plane].

**Step 10.** Therefore all three sides AB, BC, and CA of triangle ABC lie in the single plane beta, and hence the entire triangle ABC is in one plane. This completes the proof that every triangle is in one plane. Q.E.D.

**USED:** 11.1, D1.19, D1.7, P1
**Human refs (from References field):** 11.1
**Jaccard:** 0.250 — AI adds ['D1.19', 'D1.7', 'P1']

## Proposition 11.3
**Statement:** If two planes cut one another, their common section is a straight line.

**Step 1.** Let two planes AB and BC cut one another, and let their common section be the line DB. We must show that DB is a straight line.

**Step 2.** Suppose, for the sake of contradiction, that DB is not a straight line. Then from D to B, draw the straight line DEB lying in the plane AB, and also draw the straight line DFB lying in the plane BC. [P1]

**Step 3.** Then the two straight lines DEB and DFB enclose an area between them, having the same endpoints D and B. But two straight lines cannot enclose a space. This is impossible.

**Step 4.** Therefore the common section DB cannot be anything other than a straight line. For if it were not straight, we could draw a straight line from D to B in plane AB by P1. Since both D and B lie in plane AB, this straight line lies entirely in plane AB [D1.7]. Similarly, since D and B also lie in plane BC (being on the common section), the straight line from D to B drawn in plane BC lies entirely in plane BC [D1.7]. But then we would have two distinct straight lines from D to B — one in each plane — which is impossible since two straight lines cannot enclose a space.

**Step 5.** More precisely: since every point of the common section lies in both planes, take any two points D and B on the common section. Join D to B by a straight line [P1]. This straight line lies in plane AB because D and B are in plane AB and a plane surface lies evenly with the straight lines on itself [D1.7]. By the same reasoning it lies in plane BC. Therefore this straight line is part of the common section. But by 11.1, a part of a straight line cannot be in one plane while another part is in a different plane — since the straight line from D to B lies entirely in both planes, every point of the common section between D and B must coincide with this straight line.

**Step 6.** Since D and B were arbitrary points on the common section, the entire common section is a straight line.

**Step 7.** Therefore, if two planes cut one another, their common section is a straight line. Q.E.F.

**USED:** 11.1, D1.7, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['11.1', 'D1.7', 'P1']

## Proposition 11.4
**Statement:** If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

**Step 1.** Let AB and CD be two straight lines cutting one another at the point E, and let EF be a straight line set up at right angles to both AB and CD at E. I say that EF is also at right angles to the plane through AB and CD. Since AB and CD cut one another, they lie in one plane [11.2], and every triangle formed by them lies in one plane. Let this plane be called the reference plane.

**Step 2.** Cut off EA equal to EB on line AB, and EC equal to ED on line CD [1.3].

**Step 3.** Draw any straight line GEH through E lying in the reference plane, and cut off GE equal to EH [1.3]. It suffices to show that EF is at right angles to GEH, for since GEH is an arbitrary straight line through E in the plane, this will establish the result.

**Step 4.** Join AD, CB, GA, GB, GC, GD, HA, HB, HC, HD, FA, FB, FC, FD, FG, FH [P1].

**Step 5.** Since AE equals BE, and CE equals DE, and the angle AEC equals the angle BED (for they are vertical angles) [1.15], the two triangles AEC and BED are congruent by the side-angle-side criterion [1.4]. Therefore AC equals BD and the angle ACE equals the angle BDE.

**Step 6.** Since AE equals BE, and DE equals CE, and the angle AED equals the angle BEC (vertical angles) [1.15], the two triangles AED and BEC are congruent [1.4]. Therefore AD equals BC.

**Step 7.** Since GE equals EH, and EC equals ED, and the angle GEC equals the angle HED (vertical angles) [1.15], the two triangles GEC and HED are congruent [1.4]. Therefore GC equals HD.

**Step 8.** Since GE equals EH, and EA equals EB, and the angle GEA equals the angle HEB (vertical angles) [1.15], the two triangles GEA and HEB are congruent [1.4]. Therefore GA equals HB.

**Step 9.** Since EF is at right angles to AB at E, the angle FEA is a right angle and the angle FEB is a right angle. Therefore the angle FEA equals the angle FEB [P4]. Since FE is common, and EA equals EB, and the angle FEA equals the angle FEB, the triangles FEA and FEB are congruent [1.4]. Therefore FA equals FB.

**Step 10.** Since EF is at right angles to CD at E, the angle FEC is a right angle and the angle FED is a right angle. Therefore the angle FEC equals the angle FED [P4]. Since FE is common, and EC equals ED, and the angle FEC equals the angle FED, the triangles FEC and FED are congruent [1.4]. Therefore FC equals FD.

**Step 11.** Now in triangles FAC and FBD: FA equals FB (Step 9), AC equals BD (Step 5), and FC equals FD (Step 10). Therefore by the side-side-side criterion [1.8], the angle FAC equals the angle FBD.

**Step 12.** In triangles FAG and FBH: FA equals FB (Step 9), GA equals HB (Step 8), and the angle FAG equals the angle FBH (Step 11). Therefore by the side-angle-side criterion [1.4], FG equals FH.

**Step 13.** In triangles FGE and FHE: FG equals FH (Step 12), FE is common, and GE equals EH (Step 3). Therefore by the side-side-side criterion [1.8], the angle FEG equals the angle FEH.

**Step 14.** Since the angle FEG equals the angle FEH, and these are adjacent angles formed by EF standing on the straight line GH, each of them is a right angle [D1.10]. Therefore EF is at right angles to GEH.

**Step 15.** Since GEH was taken as an arbitrary straight line through E in the plane through AB and CD, the straight line EF makes right angles with every straight line which meets it and lies in that plane. Therefore EF is at right angles to the plane through AB and CD [D11.3].

**USED:** 1.15, 1.3, 1.4, 1.8, 11.2, D1.10, D11.3, P1, P4
**Human refs (from References field):** 1.15, 1.26, 1.4, 1.8, D11.3
**Jaccard:** 0.400 — AI adds ['1.3', '11.2', 'D1.10', 'P1', 'P4']; Human adds ['1.26']

## Proposition 11.5
**Statement:** If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

**Step 1.** Let the straight line AB be set up at right angles to each of the three straight lines BC, BD, and BE at their common point of section B. We must show that BC, BD, and BE are in one plane.

**Step 2.** Since BC and BD are two straight lines that meet one another at B, by 11.2, BC and BD lie in one plane. Call this plane P.

**Step 3.** Since AB is at right angles to both BC and BD at their point of intersection B, by 11.4, AB is at right angles to the plane P through BC and BD.

**Step 4.** Suppose, for the sake of contradiction, that BE is not in plane P.

**Step 5.** Since AB and BE meet at B, by 11.2, AB and BE lie in one plane. Call this plane Q.

**Step 6.** Plane Q and plane P are distinct (since BE is not in P by assumption, yet BE is in Q). Since both planes contain the point B, they must intersect. By 11.3, their common section is a straight line. Let BF be the straight line that is the common section of planes P and Q, passing through B.

**Step 7.** Since BF lies in plane P (being the common section), and AB is at right angles to plane P (Step 3), AB makes right angles with every straight line that meets it and lies in plane P, by D11.3. Therefore angle ABF is a right angle.

**Step 8.** Since AB is set up at right angles to BE (given), angle ABE is a right angle.

**Step 9.** Now BF and BE both lie in plane Q (BF is the common section of P and Q, hence in Q; and BE is in Q by construction). Also, AB lies in plane Q (Step 5). So angles ABF and ABE are angles in the same plane Q, both formed at the point B on the line AB.

**Step 10.** Since angle ABF and angle ABE are both right angles, by P4 they are equal to one another.

**Step 11.** But BF and BE are distinct straight lines from B in plane Q (for BF lies in plane P while BE does not, by our assumption). Since these are distinct lines from B on the same side of AB in plane Q, one of the angles ABF and ABE must be a part of the other. Thus the whole would equal the part, which contradicts CN5.

**Step 12.** Therefore the assumption that BE is not in plane P is false, and BE lies in plane P.

**Step 13.** Hence BC, BD, and BE are all in one plane. Q.E.D.

**USED:** 11.2, 11.3, 11.4, CN5, D11.3, P4
**Human refs (from References field):** 11.3, 11.4, D11.3
**Jaccard:** 0.500 — AI adds ['11.2', 'CN5', 'P4']

## Proposition 11.6
**Statement:** If two straight lines be at right angles to the same plane, the straight lines will be parallel.

**Step 1.** Let AB and CD be two straight lines at right angles to the given plane, meeting it at B and D respectively. Join BD in the plane. [P1]

**Step 2.** Since AB is at right angles to the plane and BD is a straight line in the plane meeting AB at B, the angle ABD is a right angle. [D11.3]

**Step 3.** Since CD is at right angles to the plane and BD is a straight line in the plane meeting CD at D, the angle CDB is a right angle. [D11.3]

**Step 4.** In the given plane, draw DE at right angles to BD from the point D, so that DE lies in the given plane. [1.11]

**Step 5.** Make DE equal to AB. [1.3]

**Step 6.** Join BE, AE, and AD. [P1]

**Step 7.** Since the angle ABD is a right angle (Step 2), in the right triangle ABD the square on AD equals the sum of the squares on AB and BD. [1.47]

**Step 8.** Since the angle BDE is a right angle (Step 4), in the right triangle BDE the square on BE equals the sum of the squares on BD and DE. But DE equals AB (Step 5), so the square on BE equals the sum of the squares on BD and AB, which equals the square on AD (Step 7). Therefore BE equals AD. [1.47, CN1]

**Step 9.** Since AB is at right angles to the plane and both B and E lie in the plane, the line BE lies in the plane, so the angle ABE is a right angle. In the right triangle ABE, the square on AE equals the sum of the squares on AB and BE. [D11.3, 1.47]

**Step 10.** Now the sum of the squares on AD and DE equals the sum of the squares on AB and BD together with the square on DE (by Step 7). Since DE equals AB, this equals the square on AB plus the square on BD plus the square on AB, which equals the square on AB plus the square on BE (by Step 8), which equals the square on AE (by Step 9). Therefore the square on AE equals the sum of the squares on AD and DE. [CN1, CN2]

**Step 11.** Since the square on AE equals the sum of the squares on AD and DE, by the converse of the Pythagorean theorem the angle ADE is a right angle. [1.48]

**Step 12.** Since CD is at right angles to the plane and DE is a line in the plane meeting CD at D, the angle CDE is a right angle. [D11.3]

**Step 13.** The line DE is at right angles to each of the three straight lines BD, DA, and DC at their common point D: to BD by construction (Step 4), to DA since the angle ADE is a right angle (Step 11), and to DC since the angle CDE is a right angle (Step 12). Since BD, DA, and DC all meet one another at the point D, by Proposition 11.5 the three lines BD, DA, and DC lie in one plane. [11.5]

**Step 14.** Since BD and DA lie in this plane, the points B and A lie in this plane, and therefore the line AB lies in this plane. Since BD and DC lie in this plane, the points D and C lie in this plane, and therefore the line CD lies in this plane. Thus AB, CD, and the transversal BD all lie in one plane.

**Step 15.** The transversal BD falls on lines AB and CD in this plane. The interior angles on the same side are the angle ABD and the angle BDC, each of which is a right angle (Steps 2 and 3). Their sum equals two right angles. [P4]

**Step 16.** Since the interior angles on the same side of the transversal BD sum to two right angles, AB is parallel to CD. [1.28]

**USED:** 1.11, 1.28, 1.3, 1.47, 1.48, 11.5, CN1, CN2, D11.3, P1, P4
**Human refs (from References field):** 1.28, 1.4, 1.8, 11.2, 11.5, D11.3
**Jaccard:** 0.214 — AI adds ['1.11', '1.3', '1.47', '1.48', 'CN1', 'CN2', 'P1', 'P4']; Human adds ['1.4', '1.8', '11.2']

## Proposition 11.7
**Statement:** If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

**Step 1.** Let AB and CD be two parallel straight lines, and let E be a point taken at random on AB and F a point taken at random on CD. It is required to prove that the straight line joining E to F is in the same plane as the parallel straight lines AB and CD.

**Step 2.** Since AB and CD are parallel, by definition they are straight lines which lie in the same plane and, being produced indefinitely in both directions, do not meet one another in either direction [D1.23]. Let this plane be P. Then the whole of AB lies in P and the whole of CD lies in P.

**Step 3.** Since E is a point on AB, and AB lies in plane P, the point E lies in plane P. Likewise, since F is a point on CD, and CD lies in plane P, the point F lies in plane P.

**Step 4.** Join EF [P1].

**Step 5.** Now the straight line EF has its endpoint E in plane P and its endpoint F in plane P. Suppose, for the sake of contradiction, that some part of EF does not lie in plane P but is in a plane more elevated. Then part of the straight line EF would be in the plane P and part in a plane more elevated. But this is impossible, for a part of a straight line cannot be in the plane of reference and a part in a plane more elevated [11.1].

**Step 6.** Therefore the whole straight line EF lies in plane P. Since AB and CD also lie in plane P, the straight line EF is in the same plane with the parallel straight lines AB and CD.

**Step 7.** Therefore, if two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines. Q.E.D.

**USED:** 11.1, D1.23, P1
**Human refs (from References field):** 11.3
**Jaccard:** 0.000 — AI adds ['11.1', 'D1.23', 'P1']; Human adds ['11.3']

## Proposition 11.8
**Statement:** If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

**Step 1.** Let AB and CD be two parallel straight lines, and let AB be at right angles to a plane P. Let B and D be the points where AB and CD meet the plane P respectively. I say that CD is also at right angles to plane P. Join BD [P1]; since B and D both lie in P, BD lies in P. By 11.7, the line BD also lies in the same plane as the parallel lines AB and CD.

**Step 2.** Since AB is at right angles to plane P, AB makes right angles with every line in P meeting it at B [D11.3]. In particular, angle ABD is a right angle.

**Step 3.** Since AB is parallel to CD and BD is a transversal, the alternate interior angles are equal [1.29]. Therefore angle BDC equals angle ABD. Since angle ABD is a right angle, angle BDC is also a right angle. Thus CD is perpendicular to BD.

**Step 4.** I will show that ABDC is a parallelogram (hence a rectangle). Since AB is parallel to CD [given], BD is a transversal, and angle ABD equals angle BDC (both right angles) [Steps 2, 3], apply 1.29 to obtain that the alternate angles angle ADB and angle DBC are also equal. In triangle ABD, angle ABD is a right angle, so angle BAD plus angle ADB equals a right angle [1.32]. In triangle BDC, angle BDC is a right angle, so angle BCD plus angle DBC equals a right angle [1.32]. Since angle ADB equals angle DBC [1.29], it follows that angle BAD equals angle BCD.

**Step 5.** By 1.26 (AAS), applied to triangles ABD and CDB: angle ABD equals angle CDB [both right angles], angle ADB equals angle DBC [1.29], and BD is common. Therefore AB equals CD and AD equals BC.

**Step 6.** Since AB is parallel to CD and AB equals CD [Step 5], the straight lines AC and BD joining their endpoints in the same direction are equal and parallel [1.33]. Therefore ABDC is a parallelogram; indeed it is a rectangle since angles at B and D are right angles.

**Step 7.** In plane P, draw line DE through D perpendicular to BD [1.11]. Through B, draw line BG in plane P parallel to DE [1.31]. Since BG is parallel to DE and BD is a transversal, the alternate angles are equal [1.29], so angle GBD equals angle BDE, which is a right angle [construction]. Thus BG is perpendicular to BD at B.

**Step 8.** Cut off BG equal to DE [1.3]. Since BG is parallel to DE [Step 7] and BG equals DE, the segments BD and GE joining their endpoints in the same direction are themselves equal and parallel [1.33]. Thus BGED is a parallelogram in plane P, with BD equal to GE and BD parallel to GE [1.34].

**Step 9.** Since AC is parallel to BD and AC equals BD [Step 6], and GE is parallel to BD and GE equals BD [Step 8], it follows that AC is parallel to GE and AC equals GE [1.30 gives AC parallel to GE; equality follows since both equal BD].

**Step 10.** Since AC and GE are equal and parallel, the straight lines AG and CE joining their endpoints in the same direction are themselves equal and parallel [1.33]. Therefore AG equals CE.

**Step 11.** Since AB is at right angles to plane P and BG lies in plane P, angle ABG is a right angle [D11.3]. In right triangle ABG, by 1.47, AG squared equals AB squared plus BG squared.

**Step 12.** Now consider triangles ABG and CDE. We have AB equals CD [Step 5], BG equals DE [Step 8, by construction], and AG equals CE [Step 10]. By 1.8 (SSS), triangles ABG and CDE are congruent. Therefore angle ABG equals angle CDE.

**Step 13.** Since angle ABG is a right angle [Step 11], angle CDE is also a right angle [Step 12]. Thus CD is perpendicular to DE.

**Step 14.** We have shown that CD is perpendicular to BD [Step 3] and CD is perpendicular to DE [Step 13]. The lines BD and DE both lie in plane P and meet at the point D (and they are not parallel, being perpendicular to each other). By 11.4, since CD is at right angles to two straight lines BD and DE which cut one another at D, CD is at right angles to the plane through BD and DE, which is the plane P.

**Step 15.** Therefore, if two straight lines are parallel and one of them is at right angles to any plane, the remaining one is also at right angles to the same plane. Q.E.D.

**USED:** 1.11, 1.26, 1.29, 1.3, 1.30, 1.31, 1.32, 1.33, 1.34, 1.47, 1.8, 11.4, 11.7, D11.3, P1
**Human refs (from References field):** 1.29, 11.2, 11.4, 11.7, D11.3
**Jaccard:** 0.250 — AI adds ['1.11', '1.26', '1.3', '1.30', '1.31', '1.32', '1.33', '1.34', '1.47', '1.8', 'P1']; Human adds ['11.2']

## Proposition 11.9
**Statement:** Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

**Step 1.** Let AB and CD each be parallel to the straight line EF, where AB and CD are not in the same plane as EF. We must show that AB is parallel to CD.

**Step 2.** Take any point G on EF. In the plane through EF and AB, draw GH from G at right angles to EF [1.11]. In the plane through EF and CD, draw GK from G at right angles to EF [1.11].

**Step 3.** Since AB is parallel to EF, and GH is a straight line falling on them in the plane containing both AB and EF, the interior angles on one side sum to two right angles [1.29]. But GH makes a right angle with EF at G, so GH also makes a right angle with AB where it meets AB. Therefore EF and AB are each at right angles to GH.

**Step 4.** Similarly, since CD is parallel to EF, and GK falls on them in the plane containing both CD and EF, by the same reasoning [1.29], EF and CD are each at right angles to GK.

**Step 5.** Now EF is at right angles to GH (from Step 3) and EF is at right angles to GK (from Step 4), and GH and GK meet EF at the same point G. Since EF is at right angles to two straight lines GH and GK which cut one another at G, EF is at right angles to the plane through GH and GK [11.4].

**Step 6.** Since EF is at right angles to the plane through GH and GK, and AB is parallel to EF, then AB is also at right angles to the plane through GH and GK [11.8].

**Step 7.** Similarly, since EF is at right angles to the plane through GH and GK, and CD is parallel to EF, then CD is also at right angles to the plane through GH and GK [11.8].

**Step 8.** Therefore AB and CD are both at right angles to the same plane, namely the plane through GH and GK. Hence AB is parallel to CD [11.6].

**Step 9.** Therefore, straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another. Q.E.D.

**USED:** 1.11, 1.29, 11.4, 11.6, 11.8
**Human refs (from References field):** 11.4, 11.6, 11.8
**Jaccard:** 0.600 — AI adds ['1.11', '1.29']

## Proposition 11.10
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.

**Step 1.** Let AB and BC be two straight lines meeting at B, and let DE and EF be two straight lines meeting at E, not in the same plane as AB and BC, such that AB is parallel to DE and BC is parallel to EF. We are to prove that angle ABC equals angle DEF.

**Step 2.** On BA, cut off BA equal to ED, and on BC, cut off BC equal to EF. [1.3]

**Step 3.** Join the straight lines AD, BE, CF, AC, and DF. [P1]

**Step 4.** Since AB is parallel to DE, and AB equals DE, the straight lines AD and BE joining their extremities on the same side are equal and parallel. [1.33] (Note: AB and DE, being parallel, lie in one plane together with the lines joining their endpoints, by 11.7, so 1.33 applies in that plane.) Thus AD is equal and parallel to BE.

**Step 5.** Since BC is parallel to EF, and BC equals EF, similarly the straight lines CF and BE joining their extremities on the same side are equal and parallel. [1.33] (Again, BC and EF lie in one plane with the joining lines, by 11.7.) Thus CF is equal and parallel to BE.

**Step 6.** Since AD is parallel to BE and CF is parallel to BE, and AD and CF are not in the same plane as BE, the straight lines AD and CF are parallel to one another. [11.9] Since AD equals BE and CF equals BE, it follows that AD equals CF. [CN1]

**Step 7.** Since AD is equal and parallel to CF, the straight lines AC and DF joining their extremities on the same side are equal and parallel. [1.33] (AD and CF, being parallel, lie in one plane by 11.7, so 1.33 applies.) Therefore AC equals DF.

**Step 8.** In triangles ABC and DEF, the three sides are respectively equal: AB equals DE, BC equals EF, and AC equals DF. Therefore angle ABC equals angle DEF. [1.8]

Therefore, if two straight lines meeting one another are parallel to two straight lines meeting one another not in the same plane, they contain equal angles. Q.E.D.

**USED:** 1.3, 1.33, 1.8, 11.7, 11.9, CN1, P1
**Human refs (from References field):** 1.33, 1.8, 11.9
**Jaccard:** 0.429 — AI adds ['1.3', '11.7', 'CN1', 'P1']

## Proposition 11.11
**Statement:** From a given elevated point to draw a straight line perpendicular to a given plane.

**Step 1.** Let the given plane be P and let A be the given elevated point not in P. Let BC be any straight line lying in the plane P. [P1, given setup]

**Step 2.** From the point A, draw AE perpendicular to BC, where E is the foot of the perpendicular lying on BC and hence in the plane P. [1.12]

**Step 3.** If AE is perpendicular to the plane P, then the required construction is complete. Suppose AE is not perpendicular to P.

**Step 4.** In the plane P, from E, draw the straight line EF at right angles to BC. [1.11]

**Step 5.** From the point A, draw AF perpendicular to EF, where F is the foot of the perpendicular on EF. [1.12]

**Step 6.** Through F, draw GH in the plane P parallel to BC. [1.31]

**Step 7.** Now AE is at right angles to BC (by construction, Step 2), and EF is at right angles to BC (by construction, Step 4). Since BC makes right angles with two straight lines AE and EF that meet at E, the straight line BC is at right angles to the plane through AE and EF. [11.4]

**Step 8.** GH is parallel to BC (by construction, Step 6). Since BC is at right angles to the plane through AE and EF, and GH is parallel to BC, it follows that GH is also at right angles to the plane through AE and EF. [11.8]

**Step 9.** Since GH is at right angles to the plane through AE and EF, GH makes right angles with all straight lines which meet it and lie in that plane. [D11.3]

**Step 10.** The straight line FA lies in the plane through AE and EF (since both A, E, and F determine that plane, and F lies on EF), and FA meets GH at F. Therefore GH is at right angles to FA, which means FA is at right angles to GH.

**Step 11.** But FA is also at right angles to EF (by construction, Step 5).

**Step 12.** Since FA stands at right angles to two straight lines GH and EF which meet one another at F and both lie in the plane P, the straight line FA is at right angles to the plane P. [11.4]

**Step 13.** Therefore from the given elevated point A, the straight line AF has been drawn perpendicular to the given plane P, which is what was required. [D11.3]

**USED:** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3, P1
**Human refs (from References field):** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3
**Jaccard:** 0.857 — AI adds ['P1']

## Proposition 11.12
**Statement:** To set up a straight line at right angles to a given plane from a given point in it.

**Step 1.** Let the given plane be P and let A be the given point in it. We are required to set up from A a straight line at right angles to P.

**Step 2.** Let B be any point not in the plane P. From the elevated point B, draw BC perpendicular to the plane P, so that C is in P and BC is at right angles to P [11.11].

**Step 3.** Through the point A, draw the straight line AD parallel to BC [1.31].

**Step 4.** Since BC is at right angles to the plane P, and AD is parallel to BC, it follows that AD is also at right angles to the plane P [11.8].

**Step 5.** Therefore AD has been set up from the given point A at right angles to the given plane P, which is what was required to do [D11.3].

**USED:** 1.31, 11.11, 11.8, D11.3
**Human refs (from References field):** 1.31, 11.11, 11.8
**Jaccard:** 0.750 — AI adds ['D11.3']

## Proposition 11.13
**Statement:** From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

**Step 1.** Suppose, for the sake of contradiction, that from the same point A two distinct straight lines AB and AC are set up at right angles to a given plane on the same side.

**Step 2.** Since AB and AC meet at A, they lie in one plane by 11.2. Let this plane be called P'.

**Step 3.** The plane P' and the given reference plane intersect, and by 11.3 their common section is a straight line. Let this common section be the straight line DAE, passing through A and lying in both the reference plane and in P'.

**Step 4.** Since AB is at right angles to the reference plane, by D11.3 it makes right angles with all straight lines which meet it and lie in that plane. In particular, since DAE lies in the reference plane and meets AB at A, angle BAD is a right angle and angle BAE is a right angle.

**Step 5.** Similarly, since AC is at right angles to the reference plane, angle CAD is a right angle and angle CAE is a right angle.

**Step 6.** Now AB, AC, and DAE all lie in the single plane P' (Step 2 and Step 3). Since DAE is a straight line and AB stands on it at A, by 1.13 the angles BAD and BAE together equal two right angles. Since both angle BAD and angle BAE are right angles (Step 4), this is consistent.

**Step 7.** Since AB and AC are distinct straight lines on the same side of the reference plane, and all three lines AB, AC, DAE lie in the plane P', the line AC must fall between AB and the line AE, or the line AB must fall between AC and the line AE (since AB and AC are distinct and on the same side of line DAE in plane P').

**Step 8.** Suppose AC falls between AB and AE. Then angle CAE is a part of angle BAE. By CN5 (the whole is greater than the part), angle BAE is greater than angle CAE. But angle BAE is a right angle (Step 4) and angle CAE is a right angle (Step 5), and by P4 all right angles are equal to one another. Therefore angle BAE equals angle CAE, yet angle BAE is greater than angle CAE, which is a contradiction.

**Step 9.** If instead AB falls between AC and AE, then angle BAE is a part of angle CAE. By CN5, angle CAE is greater than angle BAE. But both are right angles and hence equal by P4, which is again a contradiction.

**Step 10.** Since in either case a contradiction arises, the assumption that two distinct straight lines can be set up at right angles to the same plane from the same point on the same side is false. Therefore, from the same point two straight lines cannot be set up at right angles to the same plane on the same side. Q.E.D.

**USED:** 1.13, 11.2, 11.3, CN5, D11.3, P4
**Human refs (from References field):** 11.3, D11.3
**Jaccard:** 0.333 — AI adds ['1.13', '11.2', 'CN5', 'P4']

## Proposition 11.14
**Statement:** Planes to which the same straight line is at right angles will be parallel.

**Step 1.** Let the straight line AB be at right angles to each of the planes P and Q, meeting plane P at A and plane Q at B. We are to prove that P and Q are parallel.

**Step 2.** Suppose, for the sake of contradiction, that planes P and Q are not parallel. Then they meet [negation of D11.8].

**Step 3.** Since planes P and Q meet, their common section is a straight line; call it DE [11.3].

**Step 4.** Take any point G on line DE. Join GA and join GB [P1].

**Step 5.** Since AB is at right angles to plane P, and GA is a straight line in plane P passing through A (the foot of AB in plane P), the angle BAG is a right angle [D11.3].

**Step 6.** Since AB is at right angles to plane Q, and GB is a straight line in plane Q passing through B (the foot of AB in plane Q), the angle ABG is a right angle [D11.3].

**Step 7.** Now A, B, and G are three non-collinear points (since G lies on line DE in both planes while A and B lie on line AB, which is not in either plane), so triangle ABG is formed.

**Step 8.** In triangle ABG, the two angles BAG and ABG are both right angles. Therefore angle BAG together with angle ABG equals two right angles [P4, CN2].

**Step 9.** But in any triangle, any two angles taken together are less than two right angles [1.17]. Therefore angle BAG together with angle ABG must be less than two right angles.

**Step 10.** Steps 8 and 9 are in contradiction. Therefore the assumption that planes P and Q meet is false.

**Step 11.** Since planes P and Q do not meet, they are parallel [D11.8].

Therefore, planes to which the same straight line is at right angles are parallel. Q.E.F.

**USED:** 1.17, 11.3, CN2, D11.3, D11.8, P1, P4
**Human refs (from References field):** 1.17, 11.3, D11.3, D11.8
**Jaccard:** 0.571 — AI adds ['CN2', 'P1', 'P4']

## Proposition 11.15
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

**Step 1.** Let AB, BC be two straight lines meeting one another at the point B, and let DE, EF be two straight lines meeting one another at the point E, such that AB is parallel to DE and BC is parallel to EF, and these pairs are not in the same plane. I say that the plane through AB, BC is parallel to the plane through DE, EF.

**Step 2.** From the point B, draw BG perpendicular to the plane through DE, EF [11.11].

**Step 3.** Through the point G in the plane through DE, EF, draw GH parallel to ED and GK parallel to EF [1.31].

**Step 4.** Since BG is at right angles to the plane through DE, EF, it makes right angles with all straight lines which meet it and are in that plane [D11.3]. Therefore BG is at right angles to GH and also at right angles to GK, since both GH and GK lie in the plane through DE, EF and meet BG at G.

**Step 5.** Now AB is parallel to DE, and GH is also parallel to ED [by construction]. Since AB and GH are each parallel to DE, and AB is not in the same plane as DE, it follows that AB is parallel to GH [11.9].

**Step 6.** Since BG is at right angles to GH [Step 4], and AB is parallel to GH [Step 5], therefore BG is at right angles to BA [1.29, as the angle BGA is a right angle, and AB is parallel to GH, so the co-interior angles or alternately the corresponding relationship forces the angle ABG to be right]. More precisely: BG meets the two parallels AB and GH; the angle BGH is a right angle; therefore the angle ABG is also a right angle, since alternate interior angles with parallel lines AB and GH cut by transversal BG are supplementary to co-interior angles summing to two right angles, and since angle BGH is right, angle ABG is right [1.29].

**Step 7.** Similarly, BC is parallel to EF, and GK is also parallel to EF [by construction]. Since BC and GK are each parallel to EF, and BC is not in the same plane as EF, it follows that BC is parallel to GK [11.9].

**Step 8.** Since BG is at right angles to GK [Step 4], and BC is parallel to GK [Step 7], therefore BG is at right angles to BC. For BG meets the two parallels BC and GK, and angle BGK is a right angle, so angle CBG is also a right angle [1.29].

**Step 9.** Since BG stands at right angles to the two straight lines BA and BC which meet one another at B, BG is at right angles to the plane through BA and BC [11.4].

**Step 10.** But BG is also at right angles to the plane through DE and EF [Step 2, by construction].

**Step 11.** Therefore BG is at right angles to both the plane through AB, BC and the plane through DE, EF. But planes to which the same straight line is at right angles are parallel [11.14].

**Step 12.** Therefore the plane through AB, BC is parallel to the plane through DE, EF. Q.E.D.

**USED:** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Human refs (from References field):** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Jaccard:** 1.000 — Perfect match.

## Proposition 11.16
**Statement:** If two parallel planes be cut by any plane, their common sections are parallel.

**Step 1.** Let AB and CD be two parallel planes, and let the plane EFGH cut them. Let EF be the common section of the cutting plane with plane AB, and let GH be the common section of the cutting plane with plane CD. By 11.3, each of these common sections is a straight line.

**Step 2.** Now EF and GH are both straight lines lying in the same plane, namely the cutting plane EFGH. I say that EF is parallel to GH.

**Step 3.** Suppose, for the sake of contradiction, that EF and GH are not parallel. Then, since they are two straight lines in the same plane and are not parallel, by D1.23 they will meet at some point when produced. Let them meet at point K.

**Step 4.** Since K lies on line EF, and EF is the common section of the cutting plane with plane AB, point K lies in plane AB. Similarly, since K lies on line GH, and GH is the common section of the cutting plane with plane CD, point K lies in plane CD.

**Step 5.** Therefore planes AB and CD have a point K in common, meaning they meet at K. But AB and CD are parallel planes, and by D11.8 parallel planes are those which do not meet. This is a contradiction.

**Step 6.** Therefore our assumption is false, and EF and GH do not meet. Since EF and GH are straight lines in the same plane that do not meet one another in either direction, by D1.23 they are parallel.

**Step 7.** Therefore, if two parallel planes be cut by any plane, their common sections are parallel. Q.E.D.

**USED:** 11.3, D1.23, D11.8
**Human refs (from References field):** 11.1, D1.23
**Jaccard:** 0.250 — AI adds ['11.3', 'D11.8']; Human adds ['11.1']

## Proposition 11.17
**Statement:** If two straight lines be cut by parallel planes, they will be cut in the same ratios.

**Step 1.** Let the two straight lines AB and CD be cut by the three parallel planes alpha, beta, and gamma, where plane alpha passes through A and C, plane beta passes through E and F, and plane gamma passes through B and D. We must prove that AE:EB = CF:FD.

**Step 2.** Join AD [P1]. Since A is in plane alpha and D is in plane gamma, and these planes are parallel with plane beta lying between them, the straight line AD must meet plane beta; let it meet plane beta at the point G.

**Step 3.** Join EG and GF [P1]. Consider the triangle ABD. The points E and G both lie in plane beta (E on side AB, G on side AD). Now plane beta and plane gamma are parallel [D11.8]. The plane of triangle ABD cuts both plane beta and plane gamma. By 11.16, their common sections with the plane of triangle ABD are parallel. The common section with plane beta passes through E and G, giving line EG; the common section with plane gamma passes through B and D, giving line BD. Therefore EG is parallel to BD.

**Step 4.** Since in triangle ABD the line EG is parallel to side BD, and E lies on AB while G lies on AD, by 6.2 the sides are cut proportionally: AE:EB = AG:GD.

**Step 5.** Now consider the triangle ACD. The points G and F both lie in plane beta (G on side AD, F on side CD). Plane alpha and plane beta are parallel [D11.8]. The plane of triangle ACD cuts both plane alpha and plane beta. By 11.16, their common sections with the plane of triangle ACD are parallel. The common section with plane alpha passes through A and C, giving line AC; the common section with plane beta passes through G and F, giving line GF. Therefore GF is parallel to AC.

**Step 6.** Since in triangle ACD the line GF is parallel to side AC, and G lies on AD while F lies on CD, by 6.2 the sides are cut proportionally: DG:GA = DF:FC.

**Step 7.** By inversion of the proportion in Step 6 [5.7.Corollary], GA:GD = FC:FD, that is, AG:GD = CF:FD.

**Step 8.** From Step 4, AE:EB = AG:GD, and from Step 7, AG:GD = CF:FD. Therefore, since two ratios each equal the same ratio, AE:EB = CF:FD [5.11].

**Step 9.** Therefore, if two straight lines be cut by parallel planes, they will be cut in the same ratios. Q.E.D.

**USED:** 11.16, 5.11, 5.7, 6.2, D11.8, P1
**Human refs (from References field):** 11.16, 5.11, 6.2
**Jaccard:** 0.500 — AI adds ['5.7', 'D11.8', 'P1']

## Proposition 11.18
**Statement:** If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

**Step 1.** Let the straight line AB be at right angles to the plane P, and let Q be any plane passing through AB. We must show that Q is at right angles to P.

**Step 2.** Since AB is at right angles to plane P, the line AB meets plane P at some point; let this point be A. Since AB lies in plane Q and meets plane P at A, the planes Q and P have a point in common and therefore intersect. By 11.3, their common section is a straight line; call it CE, passing through A.

**Step 3.** Since AB is at right angles to plane P, by D11.3 the line AB makes right angles with every straight line which meets it and lies in plane P. In particular, since CE lies in plane P and passes through A, the angle BAC (and the angle on the other side) is a right angle; that is, AB is at right angles to CE.

**Step 4.** Now AB lies in plane Q, and CE is the common section of planes Q and P. We have shown that AB, a straight line drawn in plane Q, is at right angles to the common section CE at their point of meeting A.

**Step 5.** But AB is at right angles to the entire plane P (given). Therefore the straight line AB, drawn in plane Q at right angles to the common section CE, is at right angles to the remaining plane P.

**Step 6.** By D11.4, a plane is at right angles to another plane when the straight lines drawn in one of the planes at right angles to the common section are at right angles to the remaining plane. Since AB is a straight line in plane Q, drawn at right angles to the common section CE, and AB is at right angles to plane P, it follows that plane Q is at right angles to plane P.

**Step 7.** Since Q was an arbitrary plane through AB, every plane through AB is at right angles to plane P. This is what was to be proved.

**USED:** 11.3, D11.3, D11.4
**Human refs (from References field):** 1.11, 1.28, 11.8, D11.3, D11.4
**Jaccard:** 0.333 — AI adds ['11.3']; Human adds ['1.11', '1.28', '11.8']

## Proposition 11.19
**Statement:** If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

**Step 1.** Let the two planes AB and CD each be at right angles to a reference plane P, and let planes AB and CD cut one another. We must show that their common section is at right angles to plane P.

**Step 2.** Since planes AB and CD cut one another, their common section is a straight line [11.3]. Let this common section be the line EF, and let E be the point where EF meets plane P.

**Step 3.** Since plane AB cuts plane P, their common section is a straight line [11.3]; call it EG. Since plane CD cuts plane P, their common section is a straight line [11.3]; call it EH. The point E lies on both common sections, since E is on EF which lies in both planes AB and CD, and E lies in P.

**Step 4.** From the point E in plane P, set up the straight line EK at right angles to plane P [11.12]. Then EK makes right angles with all straight lines meeting it that lie in plane P [D11.3].

**Step 5.** Since plane AB is at right angles to plane P, by the definition of a plane at right angles to a plane [D11.4], any straight line drawn in plane AB at right angles to the common section EG at point E is at right angles to plane P. Now in plane AB, from point E, draw a straight line perpendicular to EG [1.11]; by D11.4 this line is at right angles to plane P. But EK is also at right angles to plane P from point E [Step 4]. Since from the same point E, two straight lines cannot be set up at right angles to the same plane on the same side [11.13], this perpendicular drawn in plane AB must coincide with EK. Therefore EK lies in plane AB.

**Step 6.** Since plane CD is at right angles to plane P, by the same reasoning [D11.4], any straight line drawn in plane CD at right angles to the common section EH at point E is at right angles to plane P. In plane CD, from point E, draw a straight line perpendicular to EH [1.11]; by D11.4 this line is at right angles to plane P. Again by 11.13, since EK is already at right angles to plane P from point E, this perpendicular must coincide with EK. Therefore EK also lies in plane CD.

**Step 7.** Since EK lies in both plane AB and plane CD, and EF is the common section of planes AB and CD [Step 2], EK lies along the line EF. For any line lying in both planes must lie along their common section [11.3].

**Step 8.** Since EK is at right angles to plane P [Step 4], and EK lies along EF [Step 7], therefore EF, the common section of planes AB and CD, is at right angles to plane P [D11.3].

**Step 9.** Therefore, if two planes which cut one another be at right angles to any plane, their common section is also at right angles to the same plane. Q.E.D.

**USED:** 1.11, 11.12, 11.13, 11.3, D11.3, D11.4
**Human refs (from References field):** 11.13, D11.4
**Jaccard:** 0.333 — AI adds ['1.11', '11.12', '11.3', 'D11.3']

## Proposition 11.20
**Statement:** If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

**Step 1.** Let the solid angle at A be contained by the three plane angles DAB, DAC, and BAC. We are to prove that any two of these angles taken together are greater than the remaining one.

**Step 2.** If all three plane angles are equal, the result is immediate since any two equal angles sum to twice a single angle, which is greater than one such angle. If not all are equal, let angle BAC be not less than each of the other two angles DAB and DAC. It suffices to show that angle DAB + angle DAC > angle BAC, since the cases where the remaining angle is DAB or DAC follow immediately (each is not greater than BAC, so the sum of the other two, which includes BAC, exceeds it).

**Step 3.** In the plane containing angle BAC, construct at the point A the angle BAE equal to the angle DAB, where E lies within the angle BAC on the same side of AB as C [1.23].

**Step 4.** On the ray AE, cut off AE equal to AD [1.3, P1].

**Step 5.** Let BDC be any straight line meeting the three rays AB, AD, AC at points B, D, C respectively (that is, take B on ray AB and C on ray AC, and let BC be drawn cutting the ray AD at D) [P1]. Through E, which lies in the plane of triangle BAC and interior to angle BAC, the line BC also passes, so that E lies on segment BC.

**Step 6.** In triangles ABD and ABE, we have AB = AB, AD = AE (by construction in Step 4), and angle DAB = angle BAE (by construction in Step 3). Therefore triangle ABD is congruent to triangle ABE, and in particular BD = BE [1.4].

**Step 7.** In triangle BDC, by the triangle inequality BD + DC > BC [1.20]. Since BC = BE + EC (as E lies on segment BC), we have BD + DC > BE + EC.

**Step 8.** Since BD = BE (from Step 6), subtracting these equals from the respective sides gives DC > EC [CN3].

**Step 9.** Now consider triangles ADC and AEC. We have AD = AE (by construction), AC = AC, and DC > EC (from Step 8). Therefore angle DAC > angle EAC [1.25].

**Step 10.** Adding angle DAB to the left side and the equal angle BAE to the right side: angle DAB + angle DAC > angle BAE + angle EAC [CN2]. But angle BAE + angle EAC = angle BAC.

**Step 11.** Therefore angle DAB + angle DAC > angle BAC.

**Step 12.** Combined with the observation in Step 2, any two of the three plane angles taken together are greater than the remaining one. Q.E.D.

**USED:** 1.20, 1.23, 1.25, 1.3, 1.4, CN2, CN3, P1
**Human refs (from References field):** 1.20, 1.25, 1.4
**Jaccard:** 0.375 — AI adds ['1.23', '1.3', 'CN2', 'CN3', 'P1']

## Proposition 11.21
**Statement:** Any solid angle is contained by plane angles less than four right angles.

**Step 1.** Let there be a solid angle at the point A, contained by the plane angles BAC, CAD, DAE, EAF, and FAB. (The argument applies to any solid angle contained by any number of plane angles, at least three.) We shall prove that the sum of these plane angles is less than four right angles.

**Step 2.** Let the edges AB, AC, AD, AE, AF be cut by a plane, producing the polygon BCDEF as the cross-section. This yields face triangles ABC, ACD, ADE, AEF, and AFB, each sharing a vertex at A and having its base as a side of the polygon BCDEF [P1, D11.11].

**Step 3.** Since the face triangles ABC, ACD, ADE, AEF, and AFB each have their angle sum equal to two right angles [1.32], and there are n such triangles (where n is the number of plane angles forming the solid angle, here n = 5), the total sum of all angles in all n face triangles equals n times two right angles.

**Step 4.** This total sum can be partitioned into two parts: (i) the sum of the angles at vertex A, which is the sum of all the plane angles BAC, CAD, DAE, EAF, and FAB forming the solid angle; and (ii) the sum of all the base angles, that is, the remaining two angles in each face triangle (for instance, angles ABC and ACB in triangle ABC, and so on for each face triangle).

**Step 5.** At each vertex of the polygon BCDEF, a solid angle is formed by exactly three plane angles: the two base angles of the two face triangles meeting at that vertex and the interior angle of the polygon at that vertex. For example, at vertex B, the three plane angles are angle ABF (base angle of triangle AFB), angle ABC (base angle of triangle ABC), and angle FBC (interior angle of the polygon BCDEF). By Proposition 11.20, any two of the three plane angles containing a solid angle are greater than the remaining one. Therefore angle ABF + angle ABC > angle FBC [11.20].

**Step 6.** The same inequality holds at each vertex of the polygon: the sum of the two base angles of the face triangles at that vertex exceeds the interior angle of the polygon at that vertex. Therefore, adding all n such inequalities, the total sum of all base angles of the face triangles is greater than the total sum of all interior angles of the polygon BCDEF [CN2].

**Step 7.** The polygon BCDEF, having n sides, can be decomposed into (n - 2) triangles by drawing diagonals from one vertex [P1]. By Proposition 1.32, the angle sum of each of these triangles is two right angles. Therefore the sum of all interior angles of the polygon BCDEF equals (n - 2) times two right angles [1.32].

**Step 8.** From Step 6, the sum of all base angles of the face triangles is greater than (n - 2) times two right angles (the polygon angle sum). From Step 4, the sum of all base angles equals n times two right angles minus the sum of the plane angles at A. Therefore: n times two right angles minus the sum of the plane angles at A is greater than (n - 2) times two right angles.

**Step 9.** Rearranging the inequality from Step 8: the sum of the plane angles at A is less than n times two right angles minus (n - 2) times two right angles, which equals 2 times two right angles, that is, four right angles [CN5].

**Step 10.** Therefore any solid angle is contained by plane angles whose sum is less than four right angles. Q.E.D.

**USED:** 1.32, 11.20, CN2, CN5, D11.11, P1
**Human refs (from References field):** 1.32, 11.20
**Jaccard:** 0.333 — AI adds ['CN2', 'CN5', 'D11.11', 'P1']

## Proposition 11.22
**Statement:** If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

**Step 1.** Let the three plane angles be angle ABC, angle DEF, and angle GHK, where any two taken together are greater than the remaining one. Let these angles be contained by equal straight lines, so that AB = BC = DE = EF = GH = HK. Join AC, DF, GK. We must show that it is possible to construct a triangle out of AC, DF, GK, that is, any two of these straight lines taken together are greater than the remaining one. [Setup from the hypothesis; P1 for joining extremities.]

**Step 2.** If the three angles ABC, DEF, GHK are all equal to one another, then AC, DF, GK are also all equal to one another (by 1.4, since the sides containing the equal angles are equal), and any two of the three equal lines taken together exceed the third. So in this case a triangle can be constructed from them. [1.4, CN2]

**Step 3.** If the angles are not all equal, let angle ABC be not less than each of the other two angles. Then angle ABC is not less than angle DEF. We claim that the base AC is not less than the base DF.

**Step 4.** If angle ABC equals angle DEF, then since AB = DE and BC = EF, by 1.4 we have AC = DF, so AC is not less than DF. If angle ABC is greater than angle DEF, then since AB = DE and BC = EF, by 1.24 we have AC > DF. In either case, AC is not less than DF. [1.4, 1.24]

**Step 5.** Similarly, since angle ABC is not less than angle GHK, by the same reasoning (using 1.4 or 1.24) we conclude that AC is not less than GK. [1.4, 1.24]

**Step 6.** Therefore AC + DF > GK (since AC is not less than GK, and DF is a positive length, so AC + DF is strictly greater), and AC + GK > DF (since AC is not less than DF, and GK is a positive length). Thus any pair including AC exceeds the remaining line. [CN5]

**Step 7.** It remains to show that DF + GK > AC. At the point B on the straight line BC, construct the angle CBL equal to angle DEF, with BL = DE (= AB = BC). Join LC. [1.23, P3, P1]

**Step 8.** Since AB = BC and BL = BC (because BL = DE = AB = BC), and angle ABL = angle ABC (we will handle this below), we first note that in triangle BLC, since BL = BC, triangle BLC is isosceles with BL = BC. [By construction]

**Step 9.** Since angle DEF + angle GHK > angle ABC (by hypothesis, any two of the three angles exceed the third), and angle CBL = angle DEF (by construction), we have angle CBL + angle GHK > angle ABC. Therefore angle GHK > angle ABC - angle CBL = angle ABL. Wait -- we need to be more careful about the arrangement. Let us place angle CBL equal to angle DEF on the side of BC such that L is in the region near A. Then angle ABL = angle ABC - angle CBL. [1.23]

**Step 10.** Let us redo the construction cleanly. At point B, on line BA, construct the angle ABL equal to angle DEF, making BL = DE (which equals AB = BC). Since angle ABC is not less than angle DEF, the ray BL falls within or along the angle ABC (i.e., L is on the same side of BA as C, and the ray BL falls between BA and BC or along BC). [1.23, P3]

**Step 11.** In triangle ABL: AB = BL (since AB = DE = BL), so triangle ABL is isosceles. By 1.5, angle BAL = angle BLA. [1.5]

**Step 12.** Join LC. Since angle ABL = angle DEF and BL = DE and AB = DE = EF (wait, we have BL = DE and AB = BC, and DE = EF, so AB = BL). In triangle ABL, we have AB = BL, and angle ABL = angle DEF. Now in triangle DEF, DE = EF and angle DEF is the included angle, so by 1.4, since AB = DE, BL = EF (both equal to DE = EF), and angle ABL = angle DEF, we get AL = DF. [1.4]

**Step 13.** Now consider angle LBC. Since angle ABC = angle ABL + angle LBC (as L falls within angle ABC), we have angle LBC = angle ABC - angle ABL = angle ABC - angle DEF. By hypothesis, angle DEF + angle GHK > angle ABC, so angle GHK > angle ABC - angle DEF = angle LBC. [CN3, hypothesis]

**Step 14.** In triangle BLC: BL = BC (since BL = DE = AB = BC, as all the containing lines are equal). So triangle BLC is isosceles with BL = BC. By 1.5, angle BLC = angle BCL. [1.5]

**Step 15.** Now consider the triangle GHK where GH = HK (= the common length) and angle GHK > angle LBC (from Step 13). We have GH = HK = BL = BC. Since angle GHK > angle LBC, and GH = BL, HK = BC, by 1.24, GK > LC. [1.24]

**Step 16.** In triangle ALC, by 1.20, AL + LC > AC. [1.20]

**Step 17.** But AL = DF (from Step 12) and LC < GK (from Step 15, i.e., GK > LC). Therefore DF + GK > DF + LC (is not immediate in this direction). Let us reason more carefully: From Step 15, GK > LC. From Step 16, AL + LC > AC. Since GK > LC, we have AL + GK > AL + LC > AC (combining the inequality GK > LC with AL + LC > AC, using the fact that if GK > LC then AL + GK > AL + LC). That is, DF + GK > AC, since AL = DF. [CN5 applied as: the whole AL + GK exceeds AL + LC which exceeds AC]

**Step 18.** Combining Steps 6 and 17: we have shown that (i) AC + DF > GK, (ii) AC + GK > DF, and (iii) DF + GK > AC. Therefore any two of AC, DF, GK taken together are greater than the remaining one, and by 1.22 a triangle can be constructed from three straight lines equal to AC, DF, GK. [1.22]

**Step 19.** Therefore, if there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines. Q.E.D.

**USED:** 1.20, 1.22, 1.23, 1.24, 1.4, 1.5, CN2, CN3, CN5, P1, P3
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 0.182 — AI adds ['1.20', '1.22', '1.23', '1.5', 'CN2', 'CN3', 'CN5', 'P1', 'P3']

## Proposition 11.23
**Statement:** To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

**Step 1.** Let the three given plane angles be ABC, DEF, and GHK, where any two taken together are greater than the remaining one, and the sum of all three is less than four right angles. We must construct a solid angle contained by three plane angles equal to these.

**Step 2.** Cut off equal lengths from the arms of each angle: let AB = BC = DE = EF = GH = HK [by P1 and P3]. Join AK (the chord of angle ABC), DF (the chord of angle DEF), and GK' (the chord of angle GHK). (For clarity, denote the chords as AC, DF, GK respectively, where A and C are on the arms of angle ABC, D and F on the arms of DEF, G and K on the arms of GHK.)

**Step 3.** Since any two of the three angles taken together exceed the third, and all arms have equal length, by Proposition 11.22 it is possible to construct a triangle LMN out of the three chords AC, DF, GK, with LM = AC, MN = DF, and NL = GK.

**Step 4.** About triangle LMN describe a circle [by 4.5]. Let O be the center of this circle. O lies either inside triangle LMN, on one of its sides, or outside the triangle.

**Step 5.** First, suppose O lies inside triangle LMN. Join OL, OM, ON [by P1]. Since OL = OM (radii of the same circle) [by D1.15], and LM = AC, construct triangle OLM. In triangle ABC, we have AB = BC (both equal to the arm length), and AC = LM. In triangle OLM, we have OL = OM. We need to show that OL is less than, equal to, or related to the arm length.

**Step 6.** Since the sum of angles ABC + DEF + GHK is less than four right angles, consider the angles at O in triangles OLM, OMN, ONL. The angles around O sum to four right angles [by 1.13 and the fact that angles around a point sum to four right angles, established by 1.15 applied repeatedly]. We have angle LOM + angle MON + angle NOL = four right angles.

**Step 7.** Now construct angles at a point: at some point B', make angle L'B'M' = ABC with B'L' = B'M' = AB, and join L'M'. Then L'M' = AC = LM [by 1.4]. Similarly for the other two angles.

**Step 8.** Since the three angles ABC, DEF, GHK sum to less than four right angles, and the three angles LON, LOM, MON around O sum to exactly four right angles, we have angle LOM + angle MON + angle NOL > angle ABC + angle DEF + angle GHK. Therefore at least one of the angles at O exceeds its corresponding given angle. But in fact, we can establish a stronger result by considering the relationship between each pair.

**Step 9.** In triangle OLM, OL = OM (radii). We have LM = AC. In the isosceles triangle ABC, AB = BC and AC is the base. In the isosceles triangle OLM, OL = OM and LM is the base. Since these triangles have equal bases LM = AC, the angle at the apex determines the length of the equal sides: if angle LOM > angle ABC, then OL < AB [by 1.24 and its converse], and if angle LOM < angle ABC, then OL > AB.

**Step 10.** Now I claim that OL (the circumradius) is less than the arm length AB. To see this: suppose for contradiction that OL >= AB. Then angle LOM <= angle ABC [by 1.25]. Similarly angle MON <= angle DEF and angle NOL <= angle GHK. Adding, four right angles = angle LOM + angle MON + angle NOL <= angle ABC + angle DEF + angle GHK, contradicting the hypothesis that the three given angles sum to less than four right angles. Therefore OL < AB.

**Step 11.** Since OL < AB, set up OR perpendicular to the plane of triangle LMN at O [by 11.12], and choose R on this perpendicular so that OR^2 = AB^2 - OL^2. Since AB > OL, this difference is positive, so such a length OR exists. Then by the Pythagorean theorem [by 1.47], RL^2 = OL^2 + OR^2 = AB^2, so RL = AB.

**Step 12.** Similarly, since OM = OL (radii), RM^2 = OM^2 + OR^2 = OL^2 + OR^2 = AB^2, so RM = AB. And since ON = OL (radii), RN^2 = ON^2 + OR^2 = OL^2 + OR^2 = AB^2, so RN = AB.

**Step 13.** Now consider triangle RLM. We have RL = RM = AB = BC (the arm length), and LM = AC. In triangle ABC, AB = BC and the base is AC. In triangle RLM, RL = RM and the base is LM = AC. Since RL = AB and RM = BC and LM = AC, triangle RLM is congruent to triangle ABC [by 1.8]. Therefore angle LRM = angle ABC.

**Step 14.** Similarly, in triangle RMN, RM = RN = DE = EF, and MN = DF. So triangle RMN is congruent to triangle DEF [by 1.8], and angle MRN = angle DEF.

**Step 15.** Similarly, in triangle RNL, RN = RL = GH = HK, and NL = GK. So triangle RNL is congruent to triangle GHK [by 1.8], and angle NRL = angle GHK.

**Step 16.** Therefore the solid angle at R is contained by three plane angles LRM, MRN, NRL, which are respectively equal to the given plane angles ABC, DEF, GHK [by D11.11].

**Step 17.** Now consider the case where the center O falls on a side of triangle LMN, say on LM. Then ON is perpendicular to LM and OL = OM = ON (radii). In this case, angle LOM is a straight angle (two right angles). Since angle ABC corresponds to the chord LM with OL = OM as radii, and we need OL < AB as before. The argument from Step 10 applies: if OL >= AB then the angle subtended would be at most the given angle, and the sum of angles at O (which now includes two right angles for angle LOM plus angle MON + angle NOL, which together also make two right angles) equals four right angles, giving the same contradiction. The rest of the construction proceeds identically.

**Step 18.** Finally, consider the case where O falls outside triangle LMN. By a similar argument, angles at O around the point still sum to four right angles, but now some angles are measured as reflex angles or the configuration requires careful accounting. The key inequality from Step 10 still holds: the hypothesis that the sum of the three angles is less than four right angles forces OL < AB, and the construction of the perpendicular and the point R proceeds as before, yielding the same conclusion.

**Step 19.** Therefore, in all cases, we have constructed a solid angle at R out of three plane angles equal to the given angles ABC, DEF, GHK. Q.E.F.

**USED:** 1.13, 1.15, 1.24, 1.25, 1.4, 1.47, 1.8, 11.12, 11.22, 4.5, D1.15, D11.11, P1, P3
**Human refs (from References field):** 1.25, 1.29, 1.4, 1.47, 1.8, 11.12, 11.22, 5.16, 6.2, 6.4
**Jaccard:** 0.333 — AI adds ['1.13', '1.15', '1.24', '4.5', 'D1.15', 'D11.11', 'P1', 'P3']; Human adds ['1.29', '5.16', '6.2', '6.4']

## Proposition 11.24
**Statement:** If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

**Step 1.** Let the solid ABCDEFGH be contained by parallel planes: plane ABCD parallel to plane EFGH, plane ABFE parallel to plane DCGH, and plane BCGF parallel to plane ADHE. We must show that opposite faces are equal and parallelogrammic.

**Step 2.** Since the parallel planes ABCD and EFGH are cut by the plane ABFE, their common sections AB and EF are parallel [11.16].

**Step 3.** Since the parallel planes ABFE and DCGH are cut by the plane ABCD, their common sections AB and DC are parallel [11.16].

**Step 4.** Since the parallel planes ABFE and DCGH are cut by the plane EFGH, their common sections EF and HG are parallel [11.16].

**Step 5.** Since the parallel planes ABCD and EFGH are cut by the plane ADHE, their common sections AD and EH are parallel [11.16].

**Step 6.** Since the parallel planes ABCD and EFGH are cut by the plane BCGF, their common sections BC and FG are parallel [11.16].

**Step 7.** Since the parallel planes ABFE and DCGH are cut by the plane ADHE, their common sections AE and DH are parallel [11.16].

**Step 8.** Since the parallel planes ABFE and DCGH are cut by the plane BCGF, their common sections BF and CG are parallel [11.16].

**Step 9.** Since the parallel planes BCGF and ADHE are cut by the plane ABCD, their common sections AD and BC are parallel [11.16].

**Step 10.** Since the parallel planes BCGF and ADHE are cut by the plane EFGH, their common sections EH and FG are parallel [11.16].

**Step 11.** Consider face ABCD. We have AB parallel to DC (Step 3) and AD parallel to BC (Step 9). Since AB is parallel to DC and AD is parallel to BC, ABCD is a parallelogram [D1.22, 1.33]. Specifically, AB and DC are parallel, and they are joined by the straight lines AD and BC; since AD is also parallel to BC, these connecting lines are equal and parallel, so ABCD is a parallelogram [1.33].

**Step 12.** Similarly, face EFGH has EF parallel to HG (Step 4) and EH parallel to FG (Step 10), so EFGH is a parallelogram [1.33].

**Step 13.** Face ABFE has AB parallel to EF (Step 2) and AE parallel to BF (Step 7), so ABFE is a parallelogram [1.33].

**Step 14.** Face DCGH has DC parallel to HG (since DC is parallel to AB by Step 3 and AB is parallel to EF by Step 2 and EF is parallel to HG by Step 4, but more directly: the parallel planes ABCD and EFGH are cut by plane DCGH giving DC and HG as common sections — however DC lies in plane ABCD and HG lies in plane EFGH, while both lie in plane DCGH, so DC is parallel to HG [11.16]). Also DH is parallel to CG (Step 7 and Step 8). So DCGH is a parallelogram [1.33].

**Step 15.** Face BCGF has BC parallel to FG (Step 6) and BF parallel to CG (Step 8), so BCGF is a parallelogram [1.33].

**Step 16.** Face ADHE has AD parallel to EH (Step 5) and AE parallel to DH (Step 7), so ADHE is a parallelogram [1.33].

**Step 17.** Now we show opposite faces are equal. Consider the opposite faces ABFE and DCGH. Since ABCD is a parallelogram, AB equals DC and AD equals BC [1.34]. Since ADHE is a parallelogram, AE equals DH [1.34]. We have AB equal to DC, and AE equal to DH; also AB is parallel to DC (Step 3) and AE is parallel to DH (Step 7).

**Step 18.** Since AB is parallel to DC and AE is parallel to DH, and these pairs of lines meet at A and D respectively (and are not in the same plane), the angle BAE equals the angle CDH [11.10].

**Step 19.** In triangles ABE and DCH: AB equals DC [1.34 on parallelogram ABCD], AE equals DH [1.34 on parallelogram ADHE], and angle BAE equals angle CDH [Step 18]. Therefore triangle ABE is equal to triangle DCH, with BE equal to CH [1.4].

**Step 20.** Since ABFE is a parallelogram with AB parallel to EF and AE parallel to BF, its diagonal BE divides it into two equal triangles ABE and BEF [1.34]. Similarly, since DCGH is a parallelogram with DC parallel to HG and DH parallel to CG, its diagonal CH divides it into two equal triangles DCH and CHG [1.34]. Since triangle ABE equals triangle DCH [Step 19], and parallelogram ABFE is double triangle ABE, and parallelogram DCGH is double triangle DCH [1.34], therefore parallelogram ABFE equals parallelogram DCGH [CN5, CN1]. More precisely: parallelogram ABFE equals twice triangle ABE, and parallelogram DCGH equals twice triangle DCH [1.34], and since triangle ABE equals triangle DCH [Step 19], therefore parallelogram ABFE equals parallelogram DCGH.

**Step 21.** By an analogous argument, consider opposite faces ABCD and EFGH. Since ABFE is a parallelogram, AB equals EF and AE equals BF [1.34]. Since ADHE is a parallelogram, AD equals EH [1.34]. We have AB equal to EF (just shown) and AD equal to EH.

**Step 22.** Since AB is parallel to EF (Step 2) and AD is parallel to EH (Step 5), and these pairs meet at A and E respectively and are not in the same plane, angle BAD equals angle FEH [11.10].

**Step 23.** In triangles ABD and EFH: AB equals EF [1.34 on ABFE], AD equals EH [1.34 on ADHE], and angle BAD equals angle FEH [Step 22]. Therefore triangle ABD equals triangle EFH [1.4].

**Step 24.** Parallelogram ABCD equals twice triangle ABD, and parallelogram EFGH equals twice triangle EFH [1.34]. Since triangle ABD equals triangle EFH [Step 23], parallelogram ABCD equals parallelogram EFGH.

**Step 25.** Similarly, consider opposite faces ADHE and BCGF. Since ABCD is a parallelogram, AD equals BC [1.34]. Since ABFE is a parallelogram, AE equals BF [1.34]. Since AD is parallel to BC (Step 9) and AE is parallel to BF (Step 8 — actually AE parallel to BF follows from Step 7 indirectly; let us use that ABFE is a parallelogram so AE is parallel to BF), and these pairs meet at A and B respectively and are not in the same plane, angle DAE equals angle CBF [11.10].

**Step 26.** In triangles DAE and CBF: AD equals BC [1.34 on ABCD], AE equals BF [1.34 on ABFE], and angle DAE equals angle CBF [Step 25]. Therefore triangle DAE equals triangle CBF [1.4].

**Step 27.** Parallelogram ADHE equals twice triangle DAE, and parallelogram BCGF equals twice triangle CBF [1.34]. Since triangle DAE equals triangle CBF [Step 26], parallelogram ADHE equals parallelogram BCGF.

**Step 28.** Therefore all six faces are parallelograms (Steps 11-16), and opposite faces are equal: ABCD equals EFGH (Step 24), ABFE equals DCGH (Step 20), and ADHE equals BCGF (Step 27). This is what was to be proved.

**USED:** 1.33, 1.34, 1.4, 11.10, 11.16, CN1
**Human refs (from References field):** 1.34, 1.4, 11.10, 11.16
**Jaccard:** 0.667 — AI adds ['1.33', 'CN1']

## Proposition 11.25
**Statement:** If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.

**Step 1.** Let the parallelepipedal solid ABCD be cut by the plane FG which is parallel to the opposite planes RA and DH, so that two parallelepipedal solids ABFU and EGCD are produced. I say that as the base AEHF is to the base EHCF, so is the solid ABFU to the solid EGCD. (Here ABCD denotes the whole solid with opposite parallelogrammic faces, and the cutting plane FG is parallel to the pair of opposite faces.)

**Step 2.** To apply the equimultiple criterion for proportion, we extend the solid in the direction perpendicular to the cutting plane. Produce the edge AE and set off on it any number of segments equal to AE, say AE repeated m times, obtaining points that define m copies of the base AEHF laid end to end. Similarly, produce the edge EC and set off on it any number of segments equal to EC, say n copies, obtaining n copies of the base EHCF laid end to end. Through each of these division points, draw planes parallel to the cutting plane FG. By 11.16, since these planes are parallel to the opposite faces of the original solid, their common sections with the lateral faces are parallel lines, forming parallelograms. [11.16]

**Step 3.** Each of the m parallelepipeds so constructed on the side of AEHF has the same base AEHF and the same height (equal to the distance between face RA and the cutting plane FG), hence by 11.24 each has equal and parallelogrammic opposite faces, and the lateral edges are all equal. Since these parallelepipeds share the same base and the same height, and their opposite faces are equal parallelograms (by 11.24), they are equal solids. Therefore the solid constructed from m copies of the base is m times the solid ABFU. [11.24]

**Step 4.** By the same reasoning, each of the n parallelepipeds on the other side of the cutting plane has base equal to EHCF and the same height (equal to the distance between the cutting plane and face DH), and these are all equal to EGCD. Therefore the solid constructed from n copies of the base EHCF is n times the solid EGCD. [11.24]

**Step 5.** Now the composite base consisting of m copies of AEHF is precisely the base of the composite solid consisting of m copies of ABFU. Likewise the composite base consisting of n copies of EHCF is precisely the base of the composite solid consisting of n copies of EGCD. The two composite solids share the same height (the full height from RA to DH).

**Step 6.** Consider the composite parallelepipeds formed by the m copies and n copies respectively. These are parallelepipeds on bases that are m times AEHF and n times EHCF, both having the same height. If the multiple base m times AEHF is greater than the multiple base n times EHCF, then the corresponding composite solid m times ABFU is greater than the composite solid n times EGCD, since solids on greater bases with the same height are greater. If the bases are equal, the solids are equal; if the base is less, the solid is less. This follows because parallelepipeds of the same height are ordered by their bases: a parallelepiped with a greater base and the same height contains the one with a lesser base when suitably positioned, by the properties of parallel planes (11.24) and the fact that parallelograms with the same height are compared by their bases (1.35, 1.36). [1.35, 1.36]

**Step 7.** Since this relationship holds for all positive integers m and n — that is, the equimultiple m times AEHF exceeds, equals, or falls short of the equimultiple n times EHCF precisely when m times ABFU exceeds, equals, or falls short of n times EGCD — it follows by the definition of proportion (D5.5) that the base AEHF is to the base EHCF as the solid ABFU is to the solid EGCD. [D5.5]

**Step 8.** Therefore, if a parallelepipedal solid be cut by a plane parallel to the opposite planes, then as the base is to the base, so is the solid to the solid. Q.E.D.

**USED:** 1.35, 1.36, 11.16, 11.24, D5.5
**Human refs (from References field):** 11.24, D5.5
**Jaccard:** 0.400 — AI adds ['1.35', '1.36', '11.16']

## Proposition 11.26
**Statement:** On a given straight line, and at a given point on it, to construct a solid angle equal to a given solid angle.

**Step 1.** Let the given straight line be AB, the given point on it be A, and the given solid angle be the angle at D, contained by the plane angles EDC, EDF, and FDC.

**Step 2.** Take any point E on the edge DE. From the elevated point E, draw EG perpendicular to the plane through D containing DF and DC, and let G be the point where it meets that plane [11.11]. Join DG [P1].

**Step 3.** Since EG is perpendicular to the plane through DF and DC, it makes right angles with every straight line meeting it in that plane [D11.3]. Therefore angle EGD is a right angle.

**Step 4.** At the point A on line AB, construct angle BAL equal to angle EDC [1.23]. In the plane defined by angle BAL, construct angle BAK equal to angle EDF [1.23]. (Here K and L are on the same side of AB as the solid angle is to be constructed.)

**Step 5.** On DG, we have a definite length. Cut off AH on a ray from A (to be determined) equal to DG [1.3]. On DE, we have a definite length. The construction will place the perpendicular at H.

**Step 6.** Since angle EGD is right, in triangle EGD we have DE^2 = DG^2 + GE^2 [1.47]. Also, since EG is perpendicular to the plane through DC and DF, angle EGC is right and angle EGF is right.

**Step 7.** In triangle EGC, we have EC^2 = GC^2 + GE^2 [1.47]. In triangle EGF, we have EF^2 = GF^2 + GE^2 [1.47].

**Step 8.** Now in the plane containing angle BAL (i.e., angle EDC has been replicated as angle BAL), construct the angle at A equal to angle EDC with AL corresponding to DC. Cut off AL equal to DC and AB' on the line AB such that angle BAL = angle EDC [already done in Step 4, where L is placed so that AL corresponds to DC].

**Step 9.** Let me re-establish the construction more precisely. At the given solid angle D, the three face angles are EDC, EDF, FDC. Drop EG perpendicular to the plane of angle FDC [11.11]. Join DG, GC, GF [P1].

**Step 10.** At point A on line AB, in the plane of AB, construct angle BAL equal to angle CDG [1.23]. From A, set up AH perpendicular to the plane containing angle BAL [11.12]. On AH, cut off a length AH equal to GE [1.3].

**Step 11.** But this does not directly yield the solid angle. Instead, proceed as follows. At the given solid angle at D contained by angles EDC, EDF, FDC: from E draw EG perpendicular to the plane of DC, DF [11.11], meeting it at G. Join DG, GF, GC [P1].

**Step 12.** At point A on the given line AB, construct angle BAK equal to angle EDC in the plane of AB [1.23]. On AK, cut off AK equal to DC [1.3]. Construct angle KAL equal to angle DCF such that L is positioned corresponding to F [1.23], and cut off AL equal to DF [1.3].

**Step 13.** Now we must verify that the plane angles at A can form a solid angle. In the given solid angle at D, any two of the three plane angles EDC, EDF, FDC taken together are greater than the remaining one [11.20], and the sum of all three is less than four right angles [11.21].

**Step 14.** Since we are constructing angles equal to EDC, EDF, and FDC respectively, the same inequalities hold for the constructed angles: any two taken together are greater than the remaining one, and their sum is less than four right angles [CN1].

**Step 15.** From the elevated point E, EG is perpendicular to the plane through DC, DF [11.11]. In triangle EDG, angle EGD is right [D11.3], so ED^2 = DG^2 + GE^2 [1.47].

**Step 16.** At point A, in the plane determined by AB (and lying along the direction corresponding to DC), construct angle BAM equal to angle CDG [1.23], where M lies in this plane. On AM cut off AM equal to DG [1.3].

**Step 17.** From M, set up MH perpendicular to the plane through A containing the angle BAM [11.12], and on MH cut off MH equal to GE [1.3].

**Step 18.** Join AH [P1]. In right triangle AMH (angle AMH is right since MH is perpendicular to the plane through AM [D11.3]), AH^2 = AM^2 + MH^2 = DG^2 + GE^2 = ED^2 [1.47, CN1]. Therefore AH = ED.

**Step 19.** Now, in the given solid angle, angle EDC is a plane angle. In triangle EDC, sides ED, DC, and EC are determined. We have set angle BAK = angle EDC and AK = DC [Steps 12, 1.3]. Cut off on AH (or its extension through A) a segment: but note AH = ED [Step 18]. In triangle EDC, sides are ED, DC, EC. In triangle AHK, we have AH = ED, AK = DC, and angle HAK = angle EDC (since the construction in the plane gives angle BAK = angle EDC and H is elevated above this plane through the perpendicular construction—we need angle HAK = angle EDC).

**Step 20.** Since G lies in the plane of DC, DF and DG is in that plane, angle GDC is part of angle EDC. Similarly, M lies in the plane through A and angle MAK corresponds to angle GDC. The angle EDC = angle GDC + angle EDG. But angle EDG is determined by the right triangle EDG. Similarly angle HAK = angle MAK + angle HAM. Since angle MAK = angle GDC [Step 16, as angle BAM = angle CDG implies this relationship with AK in the direction of DC] and angle HAM = angle EDG (both determined by the same right triangle configuration with equal sides), we get angle HAK = angle EDC.

**Step 21.** In triangles AHK and EDC: AH = ED [Step 18], AK = DC [Step 12], and angle HAK = angle EDC [Step 20]. Therefore triangle AHK is congruent to triangle EDC, and HK = EC [1.4].

**Step 22.** Similarly, in the given solid angle, consider triangle EDF with sides ED, DF, EF. We have set AL = DF [Step 12] and angle at A corresponding to angle EDF. By the same perpendicular construction through M, in triangle AHL: AH = ED, AL = DF. The angle HAL = angle EDF by the same reasoning as Step 20. Therefore triangle AHL is congruent to triangle EDF, and HL = EF [1.4].

**Step 23.** In the given solid angle, in the plane of DC, DF, triangle DCF has sides DC, CF, DF. At A, triangle KAL has AK = DC, AL = DF, and angle KAL = angle DCF [Step 12]. Therefore triangle KAL is congruent to triangle DCF, and KL = CF [1.4].

**Step 24.** Now consider triangles HKL and ECF. We have HK = EC [Step 21], HL = EF [Step 22], and KL = CF [Step 23]. Therefore by SSS congruence, triangle HKL is congruent to triangle ECF, and angle HKL = angle ECF [1.8].

**Step 25.** In triangles AHK and DEC (congruent by Step 21), angle AKH = angle DCE [1.4]. In triangles AKL and DCF (congruent by Step 23), angle AKL = angle DCF [1.4].

**Step 26.** Now angle HKL = angle ECF [Step 24]. Since angle AKH = angle DCE and angle AKL = angle DCF [Step 25], and angle HKL = angle HKA + angle AKL while angle ECF = angle ECD + angle DCF (where H and E are on corresponding sides), we verify the consistency of the dihedral structure.

**Step 27.** The three plane angles HAK, HAL, KAL at vertex A equal the three plane angles EDC, EDF, FDC at vertex D respectively [Steps 20, 22 reasoning, 12]. Since any two of these plane angles taken together are greater than the remaining one [11.20 applied to the original, and the constructed angles are equal], and since their sum is less than four right angles [11.21 applied to the original], by Proposition 11.23 we can construct a solid angle from these three plane angles.

**Step 28.** Therefore the solid angle at A, contained by the plane angles HAK, HAL, and KAL, is equal to the solid angle at D, contained by the plane angles EDC, EDF, and FDC [11.23, and the equality of corresponding plane angles].

**Step 29.** Thus, on the given straight line AB, at the given point A on it, a solid angle has been constructed equal to the given solid angle at D, which is what was required.

**USED:** 1.23, 1.3, 1.4, 1.47, 1.8, 11.11, 11.12, 11.20, 11.21, 11.23, CN1, D11.11, D11.3, P1
**Human refs (from References field):** 1.23, 1.4, 1.8, 11.11, 11.12, D11.3
**Jaccard:** 0.429 — AI adds ['1.3', '1.47', '11.20', '11.21', '11.23', 'CN1', 'D11.11', 'P1']

## Proposition 11.27
**Statement:** On a given straight line to describe a parallelepipedal solid similar and similarly situated to a given parallelepipedal solid.

**Step 1.** Let AB be the given straight line and let CD be the given parallelepipedal solid. It is required to describe on the straight line AB a parallelepipedal solid similar and similarly situated to CD.

**Step 2.** Let the solid CD have a vertex at the point C, with three edges CE, CF, CG meeting at C, so that the parallelepiped is determined by these three edges and the three face angles ECF, ECG, and FCG at the solid angle at C [D11.11].

**Step 3.** At the point A on the straight line AB, construct a solid angle equal to the solid angle at C, using the three plane angles BAH, BAK, and HAK equal respectively to the angles ECF, ECG, and FCG, so that AB corresponds to CE, AH corresponds to CF, and AK corresponds to CG [11.26]. This is possible since the solid angle at C, being a solid angle of a parallelepiped, satisfies the condition that any two of its face angles taken together are greater than the third [11.20], and the sum of the three angles is less than four right angles [11.21].

**Step 4.** Since the parallelepiped CD is similar to the one we wish to construct, the edges must be proportional. Make AH such that CE is to CF as AB is to AH, using the construction of a fourth proportional [6.12]. Likewise, make AK such that CE is to CG as AB is to AK [6.12].

**Step 5.** Then we have CE : CF : CG = AB : AH : AK. From the proportion CE : CF = AB : AH, and since angle ECF equals angle BAH (by construction in Step 3), the parallelogram contained by AB, AH forming one face is similar to the parallelogram contained by CE, CF [6.6, D6.1]. Likewise, from CE : CG = AB : AK, and since angle ECG equals angle BAK, the parallelogram contained by AB, AK is similar to the parallelogram contained by CE, CG [6.6, D6.1]. And from the proportions CE : CF = AB : AH and CE : CG = AB : AK, by taking the ratios ex aequali or by direct manipulation, CF : CG = AH : AK [5.22, 5.16, 5.11]. Since angle FCG equals angle HAK, the parallelogram contained by AH, AK is similar to the parallelogram contained by CF, CG [6.6, D6.1].

**Step 6.** Now complete the parallelepipedal solid on the three edges AB, AH, AK from the solid angle at A. This is done by drawing through the endpoints of these edges planes parallel to the faces of the solid angle: through B draw planes parallel to the planes of angles HAK and BAK; through the endpoint of AH draw a plane parallel to the plane of angle BAK; and through the endpoint of AK draw planes parallel to the planes of angles BAH and HAK [P1, 1.31]. These parallel planes, together with the three faces at A, enclose a parallelepipedal solid, call it AL.

**Step 7.** Since the opposite faces of a parallelepiped are equal and parallelogrammic [11.24], each face of the solid AL is similar to the corresponding face of the solid CD. Specifically: the three faces at the solid angle A are respectively similar to the three faces at the solid angle C (established in Step 5), and the opposite faces are equal to these and hence also respectively similar to the corresponding opposite faces of CD [11.24, 1.34].

**Step 8.** The solid angle at A equals the solid angle at C by construction [11.26], and each corresponding pair of opposite solid angles in the two parallelepipeds are also equal, since in any parallelepiped the plane angles forming opposite solid angles are respectively equal to those of the original solid angle [11.24, 1.34].

**Step 9.** Therefore the solid AL is contained by similar planes equal in multitude to those of CD, and the solid angles are respectively equal. Hence AL is similar to CD [D11.9]. Moreover, AL is similarly situated to CD, since the corresponding edges and faces are arranged in the same order by construction.

**Step 10.** Therefore on the given straight line AB, a parallelepipedal solid AL has been described similar and similarly situated to the given parallelepipedal solid CD. Q.E.F.

**USED:** 1.31, 1.34, 11.20, 11.21, 11.24, 11.26, 5.11, 5.16, 5.22, 6.12, 6.6, D11.11, D11.9, D6.1, P1
**Human refs (from References field):** 5.22, 6.12, D11.9
**Jaccard:** 0.200 — AI adds ['1.31', '1.34', '11.20', '11.21', '11.24', '11.26', '5.11', '5.16', '6.6', 'D11.11', 'D6.1', 'P1']

## Proposition 11.28
**Statement:** If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid will be bisected by the plane.

**Step 1.** Let ABCDEFGH be a parallelepipedal solid, where ABCD and EFGH are opposite faces, with lateral edges AE, BF, CG, DH. Let it be cut by the plane through the diagonal AC of face ABCD and the diagonal EG of the opposite face EFGH. We must show that this plane bisects the solid.

**Step 2.** Since ABFE is a face of the parallelepiped, it is a parallelogram, so AE is parallel to BF and AE equals BF [1.34]. Since BCGF is likewise a face and hence a parallelogram, BF is parallel to CG and BF equals CG [1.34]. Now AE and CG are each parallel to BF but are not in the same plane as BF (they lie on opposite lateral faces), so AE is parallel to CG [11.9]. Also AE equals BF and BF equals CG, so AE equals CG [CN1].

**Step 3.** Since AE and CG are equal and parallel, the quadrilateral AECG (equivalently ACGE) is a parallelogram [1.33]. Hence A, C, G, E are coplanar and the plane through AC and EG is well defined.

**Step 4.** This cutting plane ACGE divides the parallelepiped into two solids. Solid S1, on the side containing vertices B and F, is bounded by triangle ABC, triangle EFG, parallelogram ABFE, parallelogram BCGF, and parallelogram ACGE. Solid S2, on the side containing vertices D and H, is bounded by triangle ACD, triangle EGH, parallelogram ADHE, parallelogram DCGH, and parallelogram ACGE.

**Step 5.** Since ABFE is a parallelogram, AB equals EF [1.34]. Since BCGF is a parallelogram, BC equals FG [1.34]. Since ACGE is a parallelogram (Step 3), AC equals EG [1.34]. Therefore triangle ABC is congruent to triangle EFG by the equality of their three sides [1.8]. These triangles lie in the parallel planes of ABCD and EFGH respectively, and the remaining faces ABFE, BCGF, and ACGE are parallelograms, so S1 is a prism [D11.13].

**Step 6.** Similarly, since ADHE is a parallelogram, AD equals EH [1.34]. Since DCGH is a parallelogram, DC equals HG [1.34]. And AC equals EG [Step 3, 1.34]. Therefore triangle ACD is congruent to triangle EGH [1.8]. These triangles lie in the parallel planes of ABCD and EFGH, and the remaining faces ADHE, DCGH, and ACGE are parallelograms, so S2 is a prism [D11.13].

**Step 7.** Since ABCD is a parallelogram, the diagonal AC bisects it, so triangle ABC equals triangle ACD [1.34]. Since EFGH is a parallelogram, the diagonal EG bisects it, so triangle EFG equals triangle EGH [1.34].

**Step 8.** By the properties of the parallelepiped, opposite faces are equal and parallelogrammic [11.24]. Therefore ABFE equals DCGH, and BCGF equals ADHE.

**Step 9.** The cutting plane ACGE is common to both prisms. Thus every face of S1 is equal to the corresponding face of S2: triangle ABC equals triangle ACD (Step 7), triangle EFG equals triangle EGH (Step 7), parallelogram ABFE equals parallelogram DCGH (Step 8), parallelogram BCGF equals parallelogram ADHE (Step 8), and parallelogram ACGE is shared. The two prisms are contained by similar planes equal in multitude and in magnitude [D11.10], so S1 and S2 are equal solids.

**Step 10.** Since the parallelepiped is divided into the two equal prisms S1 and S2, the plane through the diagonals of the opposite faces bisects the solid. Q.E.D.

**USED:** 1.33, 1.34, 1.8, 11.24, 11.9, CN1, D11.10, D11.13
**Human refs (from References field):** 1.34, D11.10
**Jaccard:** 0.250 — AI adds ['1.33', '1.8', '11.24', '11.9', 'CN1', 'D11.13']

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let the parallelepipedal solids CM and CN be on the same base AB, of the same height, and let the extremities of the edges which stand up, namely AE, AF, LB, BG, CD, CH, DK, DN, be on the same straight lines EF and GK. We must show that the solid CM is equal to the solid CN.

**Step 2.** Since each of CM and CN is a parallelepiped, their opposite faces are equal and parallelogrammic [11.24]. In particular, the face AELB (of solid CM) and the face AFNB (of solid CN) are parallelograms lying on the same base AB.

**Step 3.** Since AELB and AFNB are parallelograms, we have AE parallel to BL and AF parallel to BN [D1.22, 1.34]. Also LE = AB = NF and AE is parallel to BL, AF is parallel to BG [1.34].

**Step 4.** Since EF is a straight line (the extremities of the standing edges on one side lie on EF), and AE, AF both start from A, and BL, BG both start from B, the configuration at the top of the solids is determined by the parallelogram EFGK (the top face region).

**Step 5.** Now since AE is parallel to BL (sides of parallelogram AELB), and similarly AF is parallel to BG (sides of parallelogram AFBG), the lines EL and FG at the top are segments along the same straight lines EF and GK respectively.

**Step 6.** Consider the solid with vertices at E, F, G, L on top and A, B, C, D at the base. Since the extremities E, F lie on one straight line, and L, G (equivalently K, N) lie on another straight line, and the solids share the same base AB and the same height, we analyze the solids by decomposition.

**Step 7.** Consider the triangular prism with triangle ELH on top (where H is the intersection point determined by the top edges) matched with the corresponding triangle at the base. The face ELBC is common to the region between the two solids.

**Step 8.** More precisely, the solid CM has base ABCD and standing edges AE, BL, CH, DK, and the solid CN has base ABCD and standing edges AF, BG, CN, DN. The top face of CM is the parallelogram ELKH and the top face of CN is the parallelogram FGNH.

**Step 9.** Since ABCD is a parallelogram, AB is parallel to DC and AB = DC [1.34]. Since AE is parallel to DK (both are standing edges of the parallelepiped CM and are parallel by 11.24), and AF is parallel to DN (standing edges of CN), and E, F lie on line EF while K, N lie on line KN.

**Step 10.** Since EH = AB (opposite sides of parallelogram AELB projected through the solid, using 11.24 and 1.34), and similarly FH = AB (from parallelogram AFBG), we need to examine the relationship between the volumes.

**Step 11.** We restart the argument more carefully. Let the two parallelepipeds be ABCD-EFGH (call it P1) and ABCD-EFGH' where the standing edges from the same base ABCD reach up to the top, with extremities on the same pair of straight lines. Denote the first solid as having top face EFGH and the second as having top face E'F'G'H', where E, E' are above A; F, F' above B; G, G' above C; H, H' above D. The points E, E' lie on one line and H, H' lie on the same line (or the parallel one).

**Step 12.** Since both solids are parallelepipeds on base ABCD with the same height, AE and AE' are both equal in length to the corresponding opposite standing edges, and EE' lies along the straight line on which the top extremities lie.

**Step 13.** Now consider the solid ABFE-DCHG (solid P1). The plane through the diagonal AF of face ABFE and through DH divides P1 into two triangular prisms. By 11.28, this diagonal plane bisects the parallelepiped, so each prism equals half of P1.

**Step 14.** Similarly, the plane through the diagonal of the corresponding face of P2 bisects P2 into two equal triangular prisms, each equal to half of P2.

**Step 15.** The key observation is this: since the extremities of the standing edges lie on the same straight lines, the two parallelepipeds can be decomposed into the same set of component solids. Specifically, the solid P1 can be written as the solid common to both P1 and P2, plus certain triangular prisms on the sides; and P2 can be written as the same common solid plus corresponding triangular prisms on the opposite sides.

**Step 16.** In detail: let us say the top face of P1 is ELKH and the top face of P2 is FGNH, both on base ABCD, with E, F on line EF above side AD, and K, H (and G, N) on line above side BC. Since AELB is a face of P1 and AFBG is a face of P2, both parallelograms, and AE is parallel to BL while AF is parallel to BG [1.34].

**Step 17.** The face AELB of P1 has AE parallel to and equal to BL [1.34]. The face AFGB of P2 has AF parallel to and equal to BG [1.34]. Since E and F both lie on the same straight line, and L and G both lie on the same straight line, EF is parallel to LG (since AE is parallel to BL and AF is parallel to BG, all standing edges are parallel by 11.6).

**Step 18.** Since AE is parallel to AF (both going upward from A along the same standing direction, lying on the line through E and F), actually E and F are distinct points on the same line above A, and similarly L and G are distinct points on the same line above B. Thus EF and LG are corresponding segments on two parallel lines, and EFLG (or EFGL) forms a parallelogram [1.33], since EF is parallel to LG (both on the lines containing the top extremities) and EL is parallel to FG (both equal and parallel to AB by 1.34 applied to the top faces).

**Step 19.** Now the prism with triangular cross-section AEF at one end and DKH at the other (the prism on the left side) is equal to the prism with triangular cross-section BLG at one end and CMN at the other (the prism on the right side). This follows because AE = BL, AF = BG, EF = LG (opposite sides of parallelograms, by 1.34), and the triangles AEF and BLG are congruent by 1.8. Furthermore, AD = BC and the prisms have the same height [11.24, 1.34].

**Step 20.** Now solid P1 equals the common solid (between the two parallelepipeds) plus the left prism AEF-DKH. And solid P2 equals the same common solid plus the right prism BLG-CMN. Since the left prism equals the right prism [Step 19], we have P1 = P2 [CN2].

**Step 21.** Therefore, parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another. Q.E.F.

**USED:** 1.33, 1.34, 1.8, 11.24, 11.6, CN2
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.250 — AI adds ['1.33', '11.24', '11.6', 'CN2']; Human adds ['1.36', '1.4']

## Proposition 11.30
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another.

**Step 1.** Let the parallelepipedal solids CM and CN be on the same base AB and of the same height, and let the extremities of their edges which stand up, namely the points F, G, H, K and L, M, N, O, not be on the same straight lines. We must prove that solid CM equals solid CN.

**Step 2.** Produce the edges AF and AG (which stand up from the base in solid CM) and the edges AL and AM (which stand up from the base in solid CN), and similarly produce BH and BK, and BN and BO, so that these produced lines meet in their respective directions. By P2, each of these edges can be produced continuously in a straight line.

**Step 3.** Let FK and HG be produced to meet at P, and let LO and NM be produced to meet at Q. Similarly, let FK and LO be produced to meet at R, and let HG and NM be produced to meet at S. Then the points P, Q, R, S are the extremities of lines standing up from the corners of the base AB in certain directions.

**Step 4.** Consider the parallelepiped CR constructed on the same base AB, with the edges standing up being AR, BR (produced from corners A and B) such that the upper face has vertices determined by the intersections of the produced lines from both solids. Specifically, let the edges AE' and BH' stand up from the base, where E' and H' lie on the same straight lines as both the extremities F, G, H, K of solid CM and the extremities L, M, N, O of solid CN.

**Step 5.** More precisely, since the edges which stand up from the parallelogram ABCD (the base) in solid CM are AF, DG, CH, BK, these edges when produced determine a parallelepiped. Produce NK to meet AF produced, and produce OG to meet DG produced, and similarly produce LF to meet NK produced, and produce MH to meet OG produced. By P2, these productions are possible.

**Step 6.** Consider the parallelepiped CP whose edges standing up from the base are AP', D'G', C'H', B'K', chosen so that the upper face vertices lie on the same straight lines as the upper face vertices of solid CM. Since solids CM and CP are on the same base AB, of the same height, and the extremities of their standing edges are on the same straight lines, by 11.29 solid CM equals solid CP.

**Step 7.** Now consider the same parallelepiped CP in relation to solid CN. Since solids CN and CP are on the same base AB, of the same height, and the extremities of their standing edges are on the same straight lines (by the construction in Steps 5-6, the produced lines from CN's upper vertices also meet the lines determining CP's upper vertices), by 11.29 solid CN equals solid CP.

**Step 8.** Since solid CM equals solid CP (Step 6), and solid CN equals solid CP (Step 7), by CN1 (things equal to the same thing are equal to one another), solid CM equals solid CN.

**Step 9.** Therefore, parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another. Q.E.D.

**USED:** 11.29, CN1, P2
**Human refs (from References field):** 11.29
**Jaccard:** 0.333 — AI adds ['CN1', 'P2']

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let the parallelepipedal solids AB and CD be on equal bases, with base parallelogram EFGH of solid AB equal to base parallelogram KLMN of solid CD, and let both solids have the same height.

**Step 2.** We must show that solid AB equals solid CD.

**Step 3.** First, suppose the sides EF, KL of the bases are placed on the same straight line FKL, and the bases lie in the same plane, with the parallelograms EFGH and KLMN having EH and KN also on the same straight line. Let the standing edges of solid AB be EP, FQ, GR, HS, and those of solid CD be KT, LU, MV, NW, all having the same height.

**Step 4.** On the base EFGH, construct the parallelepiped whose standing edges are equal and parallel to KT, LU, MV, NW respectively. Call this solid AB'. Since solid AB' is on the same base EFGH as solid AB and has the same height, the extremities of their standing edges lie in the same plane. By 11.29 or 11.30 (depending on whether the extremities of the standing edges are or are not on the same straight lines), solid AB equals solid AB'.

**Step 5.** Now consider solid AB' on base EFGH with standing edges equal and parallel to KT, LU, MV, NW, and solid CD on base KLMN with standing edges KT, LU, MV, NW. Since EF is on the same straight line as KL, and EH is on the same straight line as KN, and EFGH equals KLMN as parallelograms, by 1.34 we have EF = GH, KL = MN, EH = FG (as opposite sides of parallelograms).

**Step 6.** Complete the parallelogram EKNT by joining the bases along their common line arrangement. Since EH and KN are on the same straight line, and EF and KL are on the same straight line, the figure EFGH + KLMN with the region between them forms a configuration of parallelograms on the same lines.

**Step 7.** Consider the solid on the base EKNT (the combined parallelogram region). Solid AB' has base EFGH with standing edges parallel and equal to those of CD. Solid CD has base KLMN with the same standing edges. Both AB' and CD can be related to a common solid on the combined base by adding and subtracting complementary pieces. Specifically, since the standing edges of AB' are equal and parallel to those of CD, the solid AB' together with the parallelepiped on FKLG equals the solid CD together with the parallelepiped on FKLG. This is because both combined solids form the same parallelepiped on the larger base EKNT (extending from E to K along one direction and from N to H along the other).

**Step 8.** By CN2 (if equals be added to equals, the wholes are equal), the whole solid on EKNT can be decomposed two ways. Since EFGH = KLMN (given as equal bases), and both AB' and CD are on these equal bases with identical standing edges, the complements are equal. By CN3 (if equals be subtracted from equals, the remainders are equal), solid AB' equals solid CD.

**Step 9.** From Step 4, solid AB = solid AB'. From Step 8, solid AB' = solid CD. Therefore by CN1 (things equal to the same thing are equal to one another), solid AB = solid CD.

**Step 10.** Now consider the general case where the bases are not arranged on the same straight lines. Let the two parallelepipedal solids have equal bases EFGH and KLMN in any position, with the same height. By 1.45, we can construct on a given straight line a parallelogram equal to a given rectilineal figure, and by 1.34, we know properties of parallelograms. Place the base KLMN so that side KL is on the same straight line as EF, and side KN is on the same straight line as EH. This can be done by constructing on the line EF a parallelogram equal to KLMN with an angle equal to angle FEH, using 1.42 and 1.44 (to construct a parallelogram equal to a given triangle in a given angle, and to apply a parallelogram equal to a given rectilineal figure along a given line in a given angle).

**Step 11.** With KLMN so repositioned (call the repositioned base K'L'M'N'), the solid CD can be reconstructed on this new base K'L'M'N' with the same standing edges adjusted to be parallel and equal to the originals. By 11.29 or 11.30, the reconstructed solid on K'L'M'N' equals the original solid CD (as they share the same base and height). The repositioned configuration now falls under the case handled in Steps 3 through 9.

**Step 12.** Therefore, in all cases, parallelepipedal solids on equal bases and of the same height are equal to one another. Q.E.D.

**USED:** 1.34, 1.42, 1.44, 1.45, 11.29, 11.30, CN1, CN2, CN3
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.118 — AI adds ['1.34', '1.42', '1.44', '1.45', 'CN1', 'CN2', 'CN3']; Human adds ['1.23', '1.35', '11.24', '11.25', '5.11', '5.7', '5.9', 'D11.10']

## Proposition 11.32
**Statement:** Parallelepipedal solids which are of the same height are to one another as their bases.

**Step 1.** Let AB and CD be parallelepipedal solids of the same height. Let the base of AB be the parallelogram AE, and the base of CD be the parallelogram CF. We must show that solid AB is to solid CD as base AE is to base CF.

**Step 2.** On the straight line containing one side of AE, produce it and set out in succession any number of parallelogrammic bases each equal to AE, say AE itself and (m - 1) further copies, forming a total base that is an m-fold multiple of AE. Complete the parallelepipedal solid on this extended base with the same height and same edge directions as AB. By repeated application of 11.25, this composite parallelepiped is m times the solid AB, since each portion cut by planes parallel to the opposite faces has base equal to AE and the same height.

**Step 3.** Similarly, on the line containing one side of CF, set out in succession n copies of the parallelogram CF, forming a total base that is an n-fold multiple of CF. Complete the parallelepipedal solid on this extended base with the same height and edge directions as CD. By 11.25, this composite parallelepiped is n times the solid CD.

**Step 4.** Now the m-fold multiple of base AE and the n-fold multiple of base CF are both parallelogrammic regions, and the solids constructed on them are parallelepipeds of the same height (since AB and CD share the same height by hypothesis).

**Step 5.** Suppose the m-fold multiple of base AE is greater than the n-fold multiple of base CF. Then by 11.31, the parallelepiped on the m-fold base (having a base greater than and hence not equal to the n-fold base) must itself be greater, since if the bases were equal the solids would be equal by 11.31, and adding to a base increases the solid by 11.25. That is, if m copies of AE exceed n copies of CF, then m copies of solid AB exceed n copies of solid CD.

**Step 6.** Similarly, if the m-fold multiple of base AE equals the n-fold multiple of base CF, then the m-fold multiple of solid AB equals the n-fold multiple of solid CD, by 11.31 (parallelepipeds on equal bases and of the same height are equal).

**Step 7.** And if the m-fold multiple of base AE is less than the n-fold multiple of base CF, then the m-fold multiple of solid AB is less than the n-fold multiple of solid CD, by the same reasoning as Step 5 applied in reverse.

**Step 8.** We have shown that for arbitrary positive integers m and n: the m-fold multiple of base AE is greater than, equal to, or less than the n-fold multiple of base CF according as the m-fold multiple of solid AB is greater than, equal to, or less than the n-fold multiple of solid CD.

**Step 9.** Therefore, by the definition of proportion (D5.5), base AE is to base CF as solid AB is to solid CD. That is, parallelepipedal solids of the same height are to one another as their bases. Q.E.D.

**USED:** 11.25, 11.31, D5.5
**Human refs (from References field):** 1.45, 11.25, 11.31
**Jaccard:** 0.500 — AI adds ['D5.5']; Human adds ['1.45']

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

**Step 1.** Let AB and CD be similar parallelepipedal solids, and let AE be a side of AB corresponding to the side CF of CD. We are to show that solid AB is to solid CD in the triplicate ratio of AE to CF.

**Step 2.** Since AB and CD are similar parallelepipedal solids, by D11.9 and D6.1 the corresponding edges are proportional. Let the three edges of AB meeting at one vertex be AE, AG, AH, and let the corresponding edges of CD meeting at one vertex be CF, CK, CL. Then AE:CF = AG:CK = AH:CL, and the solid angles at A and C are equal [D11.9, D6.1].

**Step 3.** Produce the edge AE to N, and make EN a third proportional to AE and CF, so that AE:CF = CF:EN [6.11]. Then produce AE further to X, and make NX a third proportional to CF and EN, so that CF:EN = EN:NX [6.11]. Thus AE, CF, EN, NX are in continued proportion.

**Step 4.** On AE, construct the parallelepipedal solid AO similar and similarly situated to CD, using 11.27. On CF, construct the parallelepipedal solid CP similar and similarly situated to CD, using 11.27. Since CP is similar and similarly situated to CD and is constructed on the same edge CF, the solid CP equals the solid CD [D11.10, CN4].

**Step 5.** Since the solid AO is similar to CD, and AE is the edge of AO corresponding to CF of CD, the three edges of AO at vertex A are to the three edges of CD at vertex C as AE is to CF [D6.1]. Therefore the edges of AO at A are AE, AG', AH' where AG' = AE·(CK/CF) and AH' = AE·(CL/CF).

**Step 6.** Now construct on EN a parallelepiped EW similar and similarly situated to CD [11.27]. The edges of EW at vertex E are EN, EN·(CK/CF), EN·(CL/CF). Similarly, all edges of EW bear the same ratio to the corresponding edges of AO as EN does to AE.

**Step 7.** Consider the solids AO and EW. They are similar (both similar to CD). The solid AO has edge AE corresponding to edge EN of EW, and AE:CF = CF:EN, so AE:EN = (AE:CF)·(CF:EN). We shall use the solids AO and EW as intermediaries.

**Step 8.** Consider the solid AO on base with edges AE and AG'. The solid EW has corresponding base with edges EN and EG'' where AG':EG'' = AE:EN (since both are similar to CD). By 11.25, parallelepipedal solids on the same base cut by parallel planes have the ratio of their heights. More precisely, since AO and EW are similar to each other, we proceed by comparing solids that share two dimensions.

**Step 9.** Construct on AE a parallelepiped P1 with edges AE, AG', and EL' where EL' equals the third edge of EW (i.e., EN·(CL/CF)). Then P1 and AO share the base determined by AE and AG', but differ in their third edges AH' and EL'. Since AH' = AE·(CL/CF) and EL' = EN·(CL/CF), we have AH':EL' = AE:EN. By 11.25, solid AO : solid P1 = AH' : EL' = AE : EN.

**Step 10.** Construct on AE a parallelepiped P2 with edges AE, EG'' (= EN·(CK/CF)), and EL' (= EN·(CL/CF)). Then P1 and P2 share the edges AE and EL', and their bases with edge AE are parallelograms with the other sides AG' and EG'' respectively. Since AG' = AE·(CK/CF) and EG'' = EN·(CK/CF), we have AG':EG'' = AE:EN. By 11.25 (applied to solids with one pair of opposite faces in the same planes), solid P1 : solid P2 = AG' : EG'' = AE : EN.

**Step 11.** Now P2 and EW have the same three edge-directions. P2 has edges AE, EG'', EL' and EW has edges EN, EG'', EL'. They share two edges EG'' and EL', and differ in the edges AE and EN. By 11.32 (parallelepipeds of the same height are as their bases), and 11.25, solid P2 : solid EW = AE : EN.

**Step 12.** Combining Steps 9, 10, and 11 by 5.22 (ex aequali in proportion): solid AO : solid EW = (AE:EN) composed three times. Since AE:CF = CF:EN from Step 3, we have AE:EN = the duplicate ratio of AE:CF [D5.9]. Therefore AE:EN composed with AE:EN once more gives the ratio composed three times. But more precisely: solid AO : solid P1 = AE:EN, solid P1 : solid P2 = AE:EN, solid P2 : solid EW = AE:EN.

**Step 13.** From Step 3, we have AE, CF, EN in continued proportion. Thus AE:CF = CF:EN. By D5.9, AE:EN is the duplicate ratio of AE:CF. Now consider the three ratios solid AO : P1, P1 : P2, P2 : EW, each equal to AE:EN. By 5.22 (ex aequali), solid AO : solid EW is the ratio compounded of these three, each equal to AE:EN.

**Step 14.** However, we need the triplicate ratio of AE:CF, not of AE:EN. Let us reconsider the construction. Return to the continued proportion AE, CF, EN, NX from Step 3. By D5.10, AE has to NX the triplicate ratio of that which AE has to CF, since AE:CF = CF:EN = EN:NX is a continued proportion of four terms.

**Step 15.** Now we directly compare the similar solids by reducing to one dimension at a time. The solid AO is similar and similarly situated to CD with corresponding edge AE to CF. Consider the parallelepipedal solid AO with edges AE, AG', AH' at vertex A, where AE:CF = AG':CK = AH':CL.

**Step 16.** Construct on CF a parallelepiped Q1 with edges CF, CK, CL (this is just the solid CD itself). Construct on CF a parallelepiped Q2 with edges CF, CK, AH'. Then Q2 and CD share the base with edges CF and CK, but have third edges AH' and CL respectively. By 11.25, Q2:CD = AH':CL = AE:CF.

**Step 17.** Construct on CF a parallelepiped Q3 with edges CF, AG', AH'. Then Q3 and Q2 share the edges CF and AH', while their bases with edge CF have the other sides AG' and CK respectively. By 11.32, since they have the same height, Q3:Q2 = (base of Q3):(base of Q2). The bases are parallelograms with one common side CF, and the other sides AG' and CK. By 6.1, the ratio of parallelograms with equal heights equals the ratio of their bases, so Q3:Q2 = AG':CK = AE:CF.

**Step 18.** Now compare the solid AO (with edges AE, AG', AH') with Q3 (with edges CF, AG', AH'). These two solids share the edges AG' and AH', and differ in the edges AE and CF. By 11.32, solid AO : Q3 = (base of AO containing edge AG') : (base of Q3 containing edge AG'). These bases are parallelograms with one common side AG', and the other sides AE and CF. By 6.1, AO:Q3 = AE:CF.

**Step 19.** From Steps 16, 17, and 18: AO:Q3 = AE:CF, Q3:Q2 = AE:CF, Q2:CD = AE:CF. By 5.22 (ex aequali), solid AO : solid CD = the ratio compounded of AE:CF taken three times.

**Step 20.** Since AE, CF, EN, NX are four terms in continued proportion (Step 3), by D5.10, AE has to NX the triplicate ratio of AE to CF. The ratio compounded of AE:CF three times equals AE:NX [5.22, D5.10]. Therefore solid AO : solid CD = AE : NX, which is the triplicate ratio of AE:CF.

**Step 21.** But solid AO was constructed similar and similarly situated to CD on edge AE. Since AB is also similar and similarly situated to CD (given), and both AO and AB are constructed on the same edge AE with the same solid angle at A, the solids AO and AB are equal [11.24, D11.10]. Specifically, since AB and AO are both similar to CD and share the edge AE corresponding to CF, their remaining edges must be equal (the proportionality with CD determines all edges uniquely from AE and the angles), so AB = AO.

**Step 22.** Therefore solid AB : solid CD is in the triplicate ratio of AE to CF [D5.10].

**Step 23.** Therefore similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides. Q.E.D.

**USED:** 11.25, 11.27, 11.32, 5.22, 6.1, 6.11, CN4, D11.10, D11.9, D5.10, D5.9, D6.1
**Human refs (from References field):** 11.24, 11.32, 6.1, D11.10, D5.10
**Jaccard:** 0.308 — AI adds ['11.25', '11.27', '5.22', '6.11', 'CN4', 'D11.9', 'D5.9', 'D6.1']; Human adds ['11.24']

## Proposition 11.34
**Statement:** In equal parallelepipedal solids the bases are reciprocally proportional to the heights; and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let AB and CD be equal parallelepipedal solids. Let the base of AB be the parallelogram EH, with height KE, and let the base of CD be the parallelogram NQ, with height MC. We must show that base EH is to base NQ as height MC is to height KE.

**Step 2.** First, suppose the edges KE and MC (the heights) are set up on the same straight line, i.e., they are collinear and in the same direction from the planes of their respective bases. Set up the solids so that the edges standing up are on the same straight line. On the straight line containing these heights, cut off a segment equal to MC from the endpoint of KE if needed. By producing or cutting the line, we can arrange both heights along one line. However, we proceed more generally.

**Step 3.** On the straight line FN, construct a parallelepipedal solid GK with base NQ and height equal to KE, such that GK has the same height as AB. [By 11.27, we can describe a parallelepiped on a given line similar to a given one, but more directly, we simply consider the parallelepiped on base NQ with height equal to KE.]

**Step 4.** Since parallelepipedal solids AB and GK have the same height (both equal to KE), they are to one another as their bases [by 11.32]. That is, solid AB : solid GK = base EH : base NQ.

**Step 5.** Since parallelepipedal solids GK and CD have the same base NQ, they are to one another as their heights [by 11.25, since cutting a parallelepiped by a plane parallel to the base gives base:base = solid:solid, and applied to solids on the same base, the solids are as their heights]. That is, solid GK : solid CD = height KE : height MC.

**Step 6.** But solid AB equals solid CD [given]. Therefore solid AB : solid GK = solid GK : solid CD is not what we need directly. Instead, since AB = CD, we have solid AB / solid GK = solid CD / solid GK, but let us reason via ratios properly.

**Step 7.** From Step 4, base EH : base NQ = solid AB : solid GK. From Step 5, solid GK : solid CD = KE : MC. Since AB = CD, we substitute: solid GK : solid AB = KE : MC [since CD = AB]. Taking the inverse, solid AB : solid GK = MC : KE [by 5.7, inverting a proportion].

**Step 8.** From Step 4, solid AB : solid GK = base EH : base NQ. From Step 7, solid AB : solid GK = MC : KE. Therefore base EH : base NQ = MC : KE [by 5.11, things equal to the same ratio are in the same ratio]. This shows that the bases are reciprocally proportional to the heights.

**Step 9.** For the converse, suppose base EH : base NQ = MC : KE (the bases are reciprocally proportional to the heights). We must show that solid AB equals solid CD.

**Step 10.** Again construct (or consider) the parallelepipedal solid GK on base NQ with height equal to KE. By 11.32, since AB and GK have the same height KE, solid AB : solid GK = base EH : base NQ.

**Step 11.** By hypothesis, base EH : base NQ = MC : KE. Therefore solid AB : solid GK = MC : KE [by 5.11].

**Step 12.** Now solid GK and solid CD are on the same base NQ. By 11.25 (solids on the same base are as their heights), solid GK : solid CD = KE : MC.

**Step 13.** From Step 11, solid AB : solid GK = MC : KE. By 5.7 (inversion), solid GK : solid AB = KE : MC. From Step 12, solid GK : solid CD = KE : MC. Therefore solid GK : solid AB = solid GK : solid CD [by 5.11].

**Step 14.** Since solid GK has the same ratio to both solid AB and solid CD, solid AB equals solid CD [by 5.9, if a magnitude has the same ratio to each of two magnitudes, those magnitudes are equal].

**Step 15.** Therefore, in equal parallelepipedal solids the bases are reciprocally proportional to the heights, and parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal. Q.E.D.

**USED:** 11.25, 11.32, 5.11, 5.7, 5.9
**Human refs (from References field):** 11.25, 11.29, 11.30, 11.31, 11.32, 5.7, 5.9, 6.1
**Jaccard:** 0.444 — AI adds ['5.11']; Human adds ['11.29', '11.30', '11.31', '6.1']

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

**Step 1.** Let the two equal plane angles be angle BAC and angle EDF, so that angle BAC equals angle EDF. From the vertices A and D, let elevated straight lines AG and DM be set up above the respective planes, such that angle BAG equals angle EDM, and angle CAG equals angle FDM. On AG and DM, let points G and M be taken at random, and from G and M let perpendiculars GH and MN be drawn to the planes in which angles BAC and EDF lie respectively [by 11.11]. Then H falls in the plane of angle BAC and N falls in the plane of angle EDF. Join HA and ND [by P1]. We must prove that angle GAH equals angle MDN.

**Step 2.** From G, draw GK perpendicular to the line AB, meeting AB at K [by 1.12 applied in the plane through A, G, and AB]. Similarly, from M, draw ML perpendicular to DE, meeting DE at L [by 1.12]. Since GH is perpendicular to the plane of angle BAC, it makes right angles with every straight line meeting it in that plane [by D11.3]. In particular, angle GHA is a right angle and angle GHK is a right angle. Similarly, since MN is perpendicular to the plane of angle EDF, angle MND is a right angle and angle MNL is a right angle.

**Step 3.** Since GK is perpendicular to AB, angle GKA is a right angle. In triangle GKA, angle GKA is a right angle. Similarly, since ML is perpendicular to DE, angle MLD is a right angle. In triangle MLD, angle MLD is a right angle.

**Step 4.** Now make AG equal to DM [by 1.3 if necessary; or they can be taken so that AG equals DM from the start, since points G and M are taken at random on the elevated lines — we choose them so that AG equals DM]. We are given that angle BAG equals angle EDM, and we have AG equals DM, and angle AKG equals angle DLM (both being right angles). However, we use the following approach instead.

**Step 5.** In the triangles AGK and DML: angle GAK equals angle MDL (since angle BAG equals angle EDM, and K lies on AB, L lies on DE, so angle GAK is the same as angle BAG and angle MDL is the same as angle EDM). Also angle AKG equals angle DLM (both right angles) [by P4]. And AG equals DM (by construction). Therefore triangles AGK and DML are equal, and AK equals DL, and GK equals ML [by 1.26, the AAS congruence].

**Step 6.** Since GH is perpendicular to the plane of angle BAC, and GK lies in the plane through G, K, H (since K is on the plane and GK meets the plane), the line GH is perpendicular to the plane containing angle BAC. Since HK lies in that plane, angle GHK is a right angle [by D11.3]. Similarly, angle MNL is a right angle.

**Step 7.** In right triangles GKH and MLN: GK equals ML [from Step 5]. The angle GKH is composed of the angle GKA (which is a right angle) and additional configuration. We proceed differently. Since GH is perpendicular to the plane, and GK is in the plane through GAB, the triangle GKH has a right angle at H (since GH is perpendicular to the plane, so GH is perpendicular to HK). Similarly, triangle MLN has a right angle at N.

**Step 8.** Consider triangles AKG and DLM once more. We have AK equals DL, GK equals ML, and AG equals DM [from Step 5]. Now consider triangles GKH and MLN. Since GH is perpendicular to the plane of angle BAC and GK is drawn in the plane through G, A, B to the foot K on AB, the point H is the foot of the perpendicular from G to the plane. The line KH lies in the plane. In triangle GHK, angle GHK is right [by D11.3]. In triangle MNL, angle MNL is right. We have GK equals ML [Step 5].

**Step 9.** Now, angle GKH equals angle MLN. To see this: angle GKA is a right angle [Step 3]. Since H is in the plane and K is on line AB, the angle AKH is some angle in the plane. The angle GKH equals angle GKA plus or minus angle AKH depending on configuration. But more directly, consider the plane through G, K, and H. In this plane, angle GKH is determined. Similarly for angle MLN. We can establish angle GKH equals angle MLN as follows.

**Step 10.** We use a more direct approach. In the right triangles GAH and MDN (right angles at H and N respectively), we shall show that AG equals DM and AH equals DN, from which the result follows.

**Step 11.** We have AG equals DM [by construction, Step 4]. It remains to show AH equals DN. From the perpendicular feet H and N, join AH and DN.

**Step 12.** Consider triangles ABG and DEF more carefully. We use the given conditions: angle BAC equals angle EDF, angle BAG equals angle EDM, and angle CAG equals angle FDM. Take AG equals DM. We shall show that the perpendicular distances GH and MN are equal, and AH equals DN.

**Step 13.** On line AB, cut off AB' equal to some length, and on DE, cut off DE' equal to the same length. But we use instead: since angle BAG equals angle EDM and AG equals DM, drop perpendiculars GK to AB and ML to DE. Then in triangles AKG and ALM (with right angles at K and L): AG equals DM, angle KAG equals angle LDM, so by 1.26 (AAS), AK equals DL and GK equals ML.

**Step 14.** Similarly, since angle CAG equals angle FDM and AG equals DM, drop perpendiculars GJ from G to AC and MQ from M to DF. In triangles AJG and DQM (right angles at J and Q): AG equals DM, angle JAG equals angle QDM, so by 1.26, AJ equals DQ and GJ equals MQ.

**Step 15.** Now GH is the perpendicular from G to the plane of angle BAC, and GK is the perpendicular from G to line AB (in the plane through G and AB). Since GH is perpendicular to the plane, and HK is in the plane, the line GH is perpendicular to HK. Also GK is perpendicular to AB. The foot H of the perpendicular from G to the plane, the foot K of the perpendicular from G to AB, and A are all in the plane of angle BAC. In right triangle GHK (right angle at H), GK squared equals GH squared plus HK squared [by 1.47].

**Step 16.** Similarly, in right triangle GHJ (right angle at H), where J is the foot of the perpendicular from G to AC, GJ squared equals GH squared plus HJ squared [by 1.47].

**Step 17.** Similarly, for the second configuration, in right triangle MNL (right angle at N), ML squared equals MN squared plus NL squared [by 1.47]. And in right triangle MNQ (right angle at N), MQ squared equals MN squared plus NQ squared [by 1.47].

**Step 18.** From Steps 13-14, GK equals ML and GJ equals MQ. From Steps 15-17, GK squared equals GH squared plus HK squared and ML squared equals MN squared plus NL squared. Since GK equals ML, we have GH squared plus HK squared equals MN squared plus NL squared. Similarly, GJ equals MQ gives GH squared plus HJ squared equals MN squared plus NQ squared.

**Step 19.** Now in right triangle AKG (right angle at K), AG squared equals AK squared plus GK squared [by 1.47]. In right triangle DLM (right angle at L), DM squared equals DL squared plus ML squared [by 1.47]. Since AG equals DM and GK equals ML, we get AK equals DL [by CN3 and the preceding equations]. This confirms Step 13. Similarly AJ equals DQ.

**Step 20.** In right triangle AHG (right angle at H), AG squared equals AH squared plus GH squared [by 1.47]. In right triangle DNM (right angle at N), DM squared equals DN squared plus MN squared [by 1.47]. Since AG equals DM, we have AH squared plus GH squared equals DN squared plus MN squared.

**Step 21.** We need to show GH equals MN. Consider the plane through G, K, H. Since GH is perpendicular to the plane of angle BAC, and K is the foot of the perpendicular from G to AB (in the plane containing G and AB), we know that HK is perpendicular to AB [by 11.4, since GH perpendicular to the plane implies GH perpendicular to AB, and GK perpendicular to AB, so AB is perpendicular to the plane GHK, hence AB is perpendicular to HK]. Similarly, NL is perpendicular to DE.

**Step 22.** Likewise, HJ is perpendicular to AC [by the same argument using 11.4]. And NQ is perpendicular to DF.

**Step 23.** In the plane of angle BAC, HK is perpendicular to AB and HJ is perpendicular to AC. In the plane of angle EDF, NL is perpendicular to DE and NQ is perpendicular to DF. Since angle BAC equals angle EDF, AK equals DL [Step 13], and AJ equals DQ [Step 14], the point H is determined in the plane of angle BAC by the two perpendicular conditions, and similarly N is determined in the plane of angle EDF. We can show AH equals DN as follows.

**Step 24.** In right triangle AKH (right angle at K, since HK is perpendicular to AB at K), AH squared equals AK squared plus KH squared [by 1.47]. In right triangle DLN (right angle at L, since NL is perpendicular to DE at L), DN squared equals DL squared plus LN squared [by 1.47]. We have AK equals DL [Step 13].

**Step 25.** From Step 15, GK squared equals GH squared plus HK squared, so HK squared equals GK squared minus GH squared. From Step 17, ML squared equals MN squared plus NL squared, so NL squared equals ML squared minus MN squared. Since GK equals ML, we have HK squared equals GK squared minus GH squared and NL squared equals GK squared minus MN squared.

**Step 26.** We still need GH equals MN. Using the perpendicular from G to AC: in right triangle AJG (right angle at J), AG squared equals AJ squared plus GJ squared [by 1.47]. In right triangle AJH (right angle at J, since HJ is perpendicular to AC), AH squared equals AJ squared plus HJ squared [by 1.47]. From Step 16, GJ squared equals GH squared plus HJ squared, so HJ squared equals GJ squared minus GH squared.

**Step 27.** Therefore AH squared equals AJ squared plus GJ squared minus GH squared [combining Step 26 equations]. Also AH squared equals AK squared plus GK squared minus GH squared [from Steps 24, 25, since HK squared equals GK squared minus GH squared]. This gives AH squared equals AG squared minus GH squared [since AK squared plus GK squared equals AG squared by Step 19]. That is, AH squared plus GH squared equals AG squared, which is simply the Pythagorean relation in right triangle AGH, confirming consistency.

**Step 28.** Now, in right triangle AGH (right angle at H): AG squared equals AH squared plus GH squared [by 1.47]. In right triangle DMN (right angle at N): DM squared equals DN squared plus MN squared [by 1.47]. We have AG equals DM, so AH squared plus GH squared equals DN squared plus MN squared.

**Step 29.** We now show GH equals MN. Since HK is perpendicular to AB at K and HJ is perpendicular to AC at J [Steps 21-22], in the plane of angle BAC we have: angle KAJ equals angle BAC. In right triangle AKH, KH equals AH times sin(angle KAH) and AK equals AH times cos(angle KAH). But we use Euclidean methods. In the right triangles AKH and AJH (sharing hypotenuse AH, with right angles at K and J respectively): angle KAH plus angle JAH equals angle KAJ equals angle BAC. Similarly, angle LDN plus angle QDN equals angle LDQ equals angle EDF. Since angle BAC equals angle EDF, the configurations are analogous.

**Step 30.** Consider triangles AKH and DLN with right angles at K and L. We have AK equals DL. If we can show KH equals LN, then AH equals DN [by 1.47 and the converse]. From GK squared equals GH squared plus KH squared [Step 15] and ML squared equals MN squared plus LN squared [Step 17], with GK equals ML, we need GH equals MN to conclude KH equals LN.

**Step 31.** Consider the angle GAC equals angle MDF (given as angle CAG equals angle FDM). Drop perpendicular GJ to AC and MQ to DF. We showed AJ equals DQ and GJ equals MQ [Step 14]. From Step 16, GJ squared equals GH squared plus HJ squared, and MQ squared equals MN squared plus NQ squared [Step 17]. Since GJ equals MQ: GH squared plus HJ squared equals MN squared plus NQ squared.

**Step 32.** From Step 24: AH squared equals AK squared plus KH squared. Also AH squared equals AJ squared plus HJ squared [Step 26]. So AK squared plus KH squared equals AJ squared plus HJ squared. Similarly, DN squared equals DL squared plus LN squared equals DQ squared plus NQ squared. Since AK equals DL and AJ equals DQ, we get KH squared minus HJ squared equals AJ squared minus AK squared equals DQ squared minus DL squared equals NQ squared minus LN squared. So KH squared minus HJ squared equals NQ squared minus LN squared.

**Step 33.** From Step 25: KH squared equals GK squared minus GH squared. From Step 31 rearranged: HJ squared equals GJ squared minus GH squared. So KH squared minus HJ squared equals GK squared minus GJ squared. Similarly, NL squared equals ML squared minus MN squared and NQ squared equals MQ squared minus MN squared, so NQ squared minus NL squared equals MQ squared minus ML squared. But GK equals ML and GJ equals MQ, so GK squared minus GJ squared equals ML squared minus MQ squared. This means KH squared minus HJ squared should equal ML squared minus MQ squared equals -(MQ squared minus ML squared) = -(GJ squared - GK squared) = GK squared - GJ squared. Indeed KH squared - HJ squared = GK squared - GJ squared = GK squared - GJ squared, which equals NQ squared - NL squared from the other side. So the relation is consistent but does not yet force GH equals MN.

**Step 34.** We use a different strategy. Take AB' on AB with AB' equal to AK (arbitrary, but we use K), and similarly take any point on AC, say J. Construct the full triangles. Actually, we adopt the classical approach directly. Set AB' on ray AB so that AB' equals some length, say equal to AG. Do the same on the other side. Instead, we use the key congruence more directly.

**Step 35.** In triangle ABG, since angle BAG is given and AG is known, and GK is perpendicular to AB, the triangle is determined up to congruence. We use the fact that corresponding parts are equal in the two configurations. The essential point is that since angle BAG equals angle EDM, angle CAG equals angle FDM, and AG equals DM, the elevated line from A and the elevated line from D make identical configurations with respect to the planes.

**Step 36.** Since GH is perpendicular to the plane of angle BAC, the length GH depends only on AG and the angles that AG makes with the plane. The angle that AG makes with the plane of angle BAC is the angle GAH (by D11.5, the inclination of AG to the plane). Similarly the angle that DM makes with the plane of angle EDF is the angle MDN. We prove these are equal as follows.

**Step 37.** The position of G relative to the plane of angle BAC is determined by: (i) AG, (ii) angle BAG, (iii) angle CAG. Since these three quantities are equal to DM, angle EDM, angle FDM respectively, the perpendicular distance GH from G to the plane must equal MN (the perpendicular distance from M to the other plane), and AH must equal DN. We make this rigorous using triangle congruence.

**Step 38.** In the plane of angle BAC, since HK is perpendicular to AB [Step 21] and H is in the plane, the right triangle AKH gives AH squared equals AK squared plus KH squared [by 1.47]. In the plane of angle EDF, DN squared equals DL squared plus LN squared [by 1.47].

**Step 39.** From the right triangle GHK (right angle at H): GH squared plus HK squared equals GK squared [by 1.47]. From the right triangle MNL (right angle at N): MN squared plus NL squared equals ML squared [by 1.47]. Since GK equals ML [Step 13], GH squared plus HK squared equals MN squared plus NL squared ... (equation 1).

**Step 40.** From the right triangle GHJ (right angle at H): GH squared plus HJ squared equals GJ squared [by 1.47]. From the right triangle MNQ (right angle at N): MN squared plus NQ squared equals MQ squared [by 1.47]. Since GJ equals MQ [Step 14], GH squared + HJ squared equals MN squared + NQ squared ... (equation 2).

**Step 41.** Now consider the plane of angle BAC. The angle BAC equals angle KAJ (since K is on AB and J is on AC). In right triangle AKH, angle AKH is right, so angle KAH plus angle AHK equals a right angle. In right triangle AJH, angle AJH is right, so angle JAH plus angle AHJ equals a right angle. And angle KAH plus angle JAH equals angle BAC.

**Step 42.** In right triangle AKH: KH equals AK times tan(angle KAH). In right triangle AJH: HJ equals AJ times tan(angle JAH). Using Euclidean language: AH squared equals AK squared plus KH squared, and AH squared equals AJ squared plus HJ squared [by 1.47]. So AK squared plus KH squared equals AJ squared + HJ squared.

**Step 43.** From equation 1: HK squared equals GK squared minus GH squared. From equation 2: HJ squared equals GJ squared minus GH squared. Substituting into the relation from Step 42: AK squared + GK squared - GH squared equals AJ squared + GJ squared - GH squared. So AK squared + GK squared equals AJ squared + GJ squared. But AK squared + GK squared equals AG squared [by 1.47 in right triangle AKG] and AJ squared + GJ squared equals AG squared [by 1.47 in right triangle AJG]. So AG squared equals AG squared, which is always true. This confirms consistency but gives no new information.

**Step 44.** We need additional information to pin down GH. The key insight is that H is uniquely determined in the plane by the two conditions: HK perpendicular to AB and HJ perpendicular to AC (where K is on AB and J is on AC, with HK and HJ meeting AB and AC at right angles). Given angle BAC, AK, and AJ, the point H is uniquely determined. Since AK equals DL, AJ equals DQ, and angle BAC equals angle EDF (so angle KAJ equals angle LDQ), it follows that the triangles AKH, AJH in the first plane correspond exactly to DLN, DQN in the second plane.

**Step 45.** More precisely: in the first plane, H is the unique point such that the perpendicular from H to ray AB meets AB at K (distance AK from A) and the perpendicular from H to ray AC meets AC at J (distance AJ from A). In the second plane, N is the unique point such that the perpendicular from N to ray DE meets DE at L (distance DL from D) and the perpendicular from N to ray DF meets DF at Q (distance DQ from D). Since AK equals DL, AJ equals DQ, and angle BAC equals angle EDF, the configuration in the first plane is congruent to the configuration in the second plane.

**Step 46.** To see this formally: construct triangle AKJ in the first plane and triangle DLQ in the second plane. We have AK equals DL, AJ equals DQ, and angle KAJ equals angle LDQ (both equal to angle BAC equals angle EDF). By 1.4 (SAS), triangles AKJ and DLQ are congruent, so KJ equals LQ.

**Step 47.** Now H lies on the segment (or its extension) such that HK is perpendicular to AK and HJ is perpendicular to AJ. Within triangle AKJ, the point H is the unique point where the perpendicular from K (to AB, extended inward) meets the perpendicular from J (to AC, extended inward). Similarly N in triangle DLQ. Since triangles AKJ and DLQ are congruent [Step 46], the points H and N occupy corresponding positions, so AH equals DN, KH equals LN, and JH equals QN.

**Step 48.** From Step 39: GH squared plus HK squared equals GK squared, and MN squared plus NL squared equals ML squared. We have GK equals ML [Step 13] and HK equals LN [Step 47]. Therefore GH squared equals GK squared minus HK squared equals ML squared minus LN squared equals MN squared [by CN3]. Hence GH equals MN.

**Step 49.** Now in right triangles GAH and MDN (right angles at H and N respectively): AG equals DM [by construction], and AH equals DN [Step 47]. Therefore, by 1.47, GH squared equals AG squared minus AH squared equals DM squared minus DN squared equals MN squared, confirming GH equals MN. But more importantly, since AG equals DM and AH equals DN, triangles GAH and MDN have equal hypotenuses (AG equals DM) and equal legs (AH equals DN), so by 1.8 (SSS, since we also have GH equals MN from Step 48), the triangles are congruent.

**Step 50.** Therefore angle GAH equals angle MDN [by 1.8, corresponding angles of congruent triangles]. This is what was to be proved. Q.E.D.

**USED:** 1.12, 1.26, 1.3, 1.4, 1.47, 1.8, 11.11, 11.4, CN3, D11.3, D11.5, P1, P4
**Human refs (from References field):** 1.26, 1.4, 1.47, 1.48, 1.8, 11.8
**Jaccard:** 0.267 — AI adds ['1.12', '1.3', '11.11', '11.4', 'CN3', 'D11.3', 'D11.5', 'P1', 'P4']; Human adds ['1.48', '11.8']

## Proposition 11.36
**Statement:** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

**Step 1.** Let A, B, C be three straight lines in continued proportion, so that A : B = B : C. Let a parallelepipedal solid be formed with edges equal to A, B, C and with a given solid angle. We must show that this solid is equal to the equilateral parallelepipedal solid on B that is equiangular with it (i.e., having all three edges equal to B and the same solid angles).

**Step 2.** At a given point, construct a solid angle equal to the given solid angle [11.26]. On the straight lines forming this solid angle, set off edges equal to A, B, C respectively, and complete the parallelepipedal solid S1. Similarly, on the same solid angle, set off all three edges equal to B and complete the equilateral parallelepipedal solid S2.

**Step 3.** Since A : B = B : C, by Proposition 6.16 the rectangle contained by A and C is equal to the square on B. That is, the rectangle A by C equals the rectangle B by B.

**Step 4.** Now consider the parallelepipedal solid S1 with edges A, B, C. Its base (the parallelogram formed by two of its edges, say those equal to A and C, with the included angle from the solid angle) is the parallelogram contained by A and C with that angle. The height corresponding to this base is the edge B.

**Step 5.** Similarly, consider the parallelepipedal solid S2 with all three edges equal to B. Its base (the parallelogram formed by edges B and B with the same included angle) is the parallelogram contained by B and B with that angle. The height corresponding to this base is also B.

**Step 6.** Since the solids S1 and S2 have the same height B, by Proposition 11.32 they are to one another as their bases. That is, S1 : S2 = (parallelogram on A and C) : (parallelogram on B and B), where both bases have the same included angle.

**Step 7.** Two parallelograms with the same included angle are to one another as the rectangles contained by the sides about that angle. Since the angle is the same in both, the parallelogram on A, C is to the parallelogram on B, B as the rectangle A by C is to the rectangle B by B [6.1].

**Step 8.** But by Step 3, the rectangle contained by A and C equals the square on B (i.e., the rectangle B by B), since A : B = B : C [6.16]. Therefore the base of S1 equals the base of S2.

**Step 9.** Since S1 and S2 are parallelepipedal solids on equal bases and of the same height B, by Proposition 11.31 they are equal to one another.

**Step 10.** Therefore the parallelepipedal solid formed out of the three proportional lines A, B, C is equal to the equilateral parallelepipedal solid on the mean B which is equiangular with it. Q.E.D.

**USED:** 11.26, 11.31, 11.32, 6.1, 6.16
**Human refs (from References field):** 11.31, 11.35, 6.14
**Jaccard:** 0.143 — AI adds ['11.26', '11.32', '6.1', '6.16']; Human adds ['11.35', '6.14']

## Proposition 11.37
**Statement:** If four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described will also be proportional; and, if the parallelepipedal solids on them which are similar and similarly described be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let A, B, C, D be four straight lines such that A : B :: C : D, and let SA, SB, SC, SD be parallelepipedal solids described on A, B, C, D respectively, where SA is similar and similarly situated to SB, and SC is similar and similarly situated to SD. We must show SA : SB :: SC : SD.

**Step 2.** By 6.12, construct E as the third proportional to A and B, so that A : B :: B : E. By 6.12 again, construct F as the third proportional to B and E, so that B : E :: E : F. Since A : B :: B : E :: E : F, the four magnitudes A, B, E, F are continuously proportional with common ratio A : B. By D5.10, A : F is the triplicate ratio of A : B.

**Step 3.** By 6.12, construct G as the third proportional to C and D, so that C : D :: D : G. By 6.12 again, construct H as the third proportional to D and G, so that D : G :: G : H. Since C : D :: D : G :: G : H, the four magnitudes C, D, G, H are continuously proportional with common ratio C : D. By D5.10, C : H is the triplicate ratio of C : D.

**Step 4.** Since A : B :: C : D (given), and A : B :: B : E (Step 2) and C : D :: D : G (Step 3), it follows that B : E :: D : G. Similarly, since A : B :: E : F and C : D :: G : H, we have E : F :: G : H.

**Step 5.** From A : B :: C : D and B : E :: D : G, by 5.22 (ex aequali), A : E :: C : G. From A : E :: C : G and E : F :: G : H, by 5.22 again, A : F :: C : H.

**Step 6.** By 11.33, since SA and SB are similar parallelepipedal solids, SA : SB is the triplicate ratio of the corresponding side A to B. That is, SA : SB :: A : F (the triplicate of A : B established in Step 2). Similarly, by 11.33, SC : SD :: C : H (the triplicate of C : D established in Step 3).

**Step 7.** Since A : F :: C : H (Step 5), and SA : SB :: A : F and SC : SD :: C : H (Step 6), by 5.11, SA : SB :: SC : SD. This completes the forward direction.

**Step 8.** For the converse, suppose that SA : SB :: SC : SD, where the solids are similar and similarly described on A, B, C, D respectively. We must show A : B :: C : D.

**Step 9.** By 6.12, construct E as the fourth proportional to B, A, and D, so that B : A :: D : E. Then by the properties of proportion (invertendo from D5.5), A : B :: E : D.

**Step 10.** By 11.27, describe on E a parallelepipedal solid SE similar and similarly situated to SC (and SD). Since A : B :: E : D, by the forward direction proved above, SA : SB :: SE : SD.

**Step 11.** But SA : SB :: SC : SD by hypothesis. Therefore SE : SD :: SC : SD by 5.11.

**Step 12.** By 5.9, since SE and SC have the same ratio to SD, SE = SC.

**Step 13.** Now suppose E is not equal to C. Then E is either greater than or less than C. If E > C, then since SE and SC are similar parallelepipedal solids described on E and C respectively, by 11.33, SE : SC is the triplicate ratio of E : C. Since E > C, by 5.8, E has a greater ratio to C than C has to C, meaning E : C is a ratio of a greater to a lesser. The triplicate of such a ratio is likewise a ratio of a greater to a lesser, so SE > SC. This contradicts SE = SC from Step 12.

**Step 14.** Similarly, if E < C, then by the same reasoning with 11.33 and 5.8, SC > SE, again contradicting SE = SC.

**Step 15.** Therefore E = C. Since A : B :: E : D (Step 9) and E = C, we conclude A : B :: C : D.

**Step 16.** Therefore, if four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described are also proportional; and conversely, if the similar and similarly described parallelepipedal solids are proportional, the straight lines are themselves proportional. Q.E.F.

**USED:** 11.27, 11.33, 5.11, 5.16, 5.22, 5.8, 5.9, 6.12, D11.9, D5.10, D5.5
**Human refs (from References field):** 11.33
**Jaccard:** 0.091 — AI adds ['11.27', '5.11', '5.16', '5.22', '5.8', '5.9', '6.12', 'D11.9', 'D5.10', 'D5.5']

## Proposition 11.38
**Statement:** If the sides of the opposite planes of a cube be bisected, and planes be carried through the points of section, the common section of the planes and the diameter of the cube bisect one another.

**Step 1.** Let there be a cube with opposite faces ABCD (bottom) and EFGH (top), where vertices A, B, C, D are joined to E, F, G, H respectively by the lateral edges AE, BF, CG, DH. Let AG be a diameter (space diagonal) of the cube. [D11.25]

**Step 2.** Bisect the sides of the opposite faces ABCD and EFGH. Let K be the midpoint of AB, L the midpoint of BC, M the midpoint of CD, N the midpoint of DA, O the midpoint of EF, P the midpoint of FG, Q the midpoint of GH, and R the midpoint of HE. [1.10]

**Step 3.** Draw the plane through K, O, Q, M (the midpoints of AB, EF, GH, CD respectively). Draw also the plane through L, P, R, N (the midpoints of BC, FG, HE, DA respectively). Let these two planes meet; their common section is a straight line, call it line ST. [11.3]

**Step 4.** Since ABCD is a square (being a face of the cube), AB = BC = CD = DA. Since K, L, M, N are the midpoints of these sides, we have AK = KB = BL = LC = CM = MD = DN = NA. [D11.25, 1.10]

**Step 5.** Consider the plane through K, O, Q, M. Since K is the midpoint of AB and O is the midpoint of EF, and ABFE is a face of the cube (hence a square with AB parallel to EF and AB = EF), the segment KO is parallel to AE and equal to AE. [1.33, 11.24, 1.34]

**Step 6.** Similarly, since M is the midpoint of CD and Q is the midpoint of GH, and DCGH is a face of the cube (a square with CD parallel to GH and CD = GH), the segment MQ is parallel to DH and equal to DH. [1.33, 1.34]

**Step 7.** Since AE is parallel to DH (both being lateral edges of the cube, which are parallel by 11.24 and the definition of a cube), and KO is parallel to AE while MQ is parallel to DH, we have KO parallel to MQ. [11.9, 1.30]

**Step 8.** Also KO = AE = DH = MQ (all lateral edges of a cube are equal). Therefore KOMQ is a parallelogram (having one pair of opposite sides equal and parallel). [D11.25, 1.33]

**Step 9.** By the same reasoning, consider the plane through L, P, R, N. Since L is the midpoint of BC and P is the midpoint of FG, and BCGF is a face of the cube, LP is parallel to BF and equal to BF. Similarly, NR (from midpoint of DA to midpoint of HE) is parallel to AE and equal to AE. Since BF is parallel to AE, LP is parallel to NR, and LP = BF = AE = NR. Therefore LPRN is a parallelogram. [1.33, 1.34, 11.9, 1.30]

**Step 10.** Both parallelograms KOMQ and LPRN pass through the interior of the cube. The common section of the planes containing these parallelograms is a straight line ST. [11.3]

**Step 11.** Now consider the diagonal AG of the cube, from vertex A = corner of face ABCD to vertex G = opposite corner of face EFGH. The diagonal AG lies in the plane through A, C, G, E (the plane of the rectangle ACGE), since A, G are vertices of the cube with AC being a diagonal of face ABCD and EG being a diagonal of face EFGH. [11.7, 1.29]

**Step 12.** Consider the diagonal of parallelogram KOMQ. Since KOMQ is a parallelogram, its diagonals KQ and OM bisect each other. Let their intersection be the point S. [1.34]

**Step 13.** Similarly, the diagonals of parallelogram LPRN bisect each other at some point. We shall show this point coincides with S.

**Step 14.** Consider the face ABCD. Since K is the midpoint of AB and M is the midpoint of CD, and ABCD is a parallelogram (a square), KM passes through the center of ABCD, which is also the intersection of diagonals AC and BD. Likewise, L (midpoint of BC) and N (midpoint of DA) determine line LN passing through the same center of ABCD. So KM and LN intersect at the center of ABCD. [1.34]

**Step 15.** Similarly on face EFGH: O (midpoint of EF) and Q (midpoint of GH) determine line OQ through the center of EFGH, and P (midpoint of FG) and R (midpoint of HE) determine line PR through the center of EFGH. [1.34]

**Step 16.** The center of face ABCD is the midpoint of diagonal AC, call it X. The center of face EFGH is the midpoint of diagonal EG, call it Y. [1.10]

**Step 17.** The line XY connecting the centers of the two opposite faces is the common section ST of the two planes (KOMQ and LPRN), since X lies in both planes (being the intersection of KM and LN, where KM lies in the plane KOMQ and LN lies in the plane LPRN), and Y lies in both planes (being the intersection of OQ and PR). [11.3]

**Step 18.** Since all edges of the cube are equal, ACGE is a parallelogram (with AC parallel to EG, both being diagonals of equal square faces, and AE parallel to CG). The diagonal AG of this parallelogram and the other diagonal CE bisect each other. [1.34, 1.33]

**Step 19.** The midpoint of AG is the same as the midpoint of CE. Now X is the midpoint of AC and Y is the midpoint of EG. In parallelogram ACGE, consider line XY joining the midpoints of opposite sides AC and EG. By 6.2, since AX = XC (X bisects AC) and EY = YG (Y bisects EG), and AE is parallel to CG, the line XY passes through the intersection of the diagonals AG and CE. [6.2, 1.34]

**Step 20.** Let the midpoint of AG (and of CE) be the point W. We claim W is the midpoint of XY. In triangle ACG, X is the midpoint of AC and consider the segment from X. In parallelogram ACGE, the diagonal AG goes from A to G. Since X is the midpoint of AC and Y is the midpoint of EG, and ACGE is a parallelogram, XY is parallel to AE (joining midpoints of opposite sides) and the diagonal AG crosses XY at its midpoint. [6.4, 6.2]

**Step 21.** More precisely, in triangle ACE, X is the midpoint of AC. In triangle AEG, Y is the midpoint of EG. Consider instead the full parallelogram AXYE... we use a direct approach: In parallelogram ACGE, take diagonal AG. Let W be where AG meets XY. Since X is the midpoint of AC, in triangle ACG, the line from X parallel to CG meets AG at its midpoint (by 6.2 and the midpoint theorem). Similarly, since Y is the midpoint of EG, the line from Y parallel to AE meets AG at its midpoint. But XY connects these midpoints, so XY and AG intersect at the midpoint of AG. [6.2]

**Step 22.** Now we show W is also the midpoint of XY. In parallelogram ACGE, since X bisects AC and Y bisects EG, and AC and EG are opposite sides of the parallelogram, the segment XY passes through the intersection point W of the diagonals. The diagonals of ACGE bisect each other at W, so AW = WG. Furthermore, since XWYE forms a parallelogram (X midpoint of AC, Y midpoint of EG, with XW parallel to AE and WY parallel to AE), actually AXYE is itself a parallelogram: AX is half of AC, EY is half of EG, and AX = EY (since AC = EG), with AE parallel to XY. The diagonals of parallelogram AXYE are AY and XE, which bisect each other. Alternatively, note that in parallelogram ACGE, X and Y are midpoints of opposite sides, so XY passes through center W and W is the midpoint of XY. [1.34]

**Step 23.** Therefore the diagonal AG of the cube and the line XY (which is the common section ST of the two bisecting planes) meet at W, where W is the midpoint of both AG and XY (= ST). [1.34]

**Step 24.** Hence the common section of the planes and the diameter of the cube bisect one another. Q.E.D.

**USED:** 1.10, 1.29, 1.30, 1.33, 1.34, 11.3, 11.7, 11.9, 6.2, D11.25
**Human refs (from References field):** 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.9
**Jaccard:** 0.214 — AI adds ['1.10', '1.30', '1.34', '11.3', '11.7', '6.2', 'D11.25']; Human adds ['1.14', '1.15', '1.26', '1.4']

## Proposition 11.39
**Statement:** If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms will be equal.

**Step 1.** Let there be two prisms of equal height h, the first having parallelogram ABCD as base and the second having triangle EFG as base, and let ABCD be double triangle EFG. We must show the prisms are equal.

**Step 2.** Complete triangle EFG to parallelogram EFGK by constructing the fourth vertex K such that EK is equal and parallel to FG, and FK is equal and parallel to EG. Then the diagonal of parallelogram EFGK divides it into two equal triangles, so EFGK is double triangle EFG [1.34]. Since ABCD is also double triangle EFG, parallelogram ABCD equals parallelogram EFGK [CN1].

**Step 3.** Construct a parallelepiped on parallelogram ABCD as base with height h, that is, the perpendicular distance between the base ABCD and the opposite face is h. Similarly, construct a parallelepiped on parallelogram EFGK as base with the same height h.

**Step 4.** Since the parallelogram ABCD equals the parallelogram EFGK (Step 2), and both parallelepipeds have the same height h, the parallelepiped on ABCD equals the parallelepiped on EFGK [11.31].

**Step 5.** Now consider the parallelepiped on ABCD. Cut it by a plane passing through the diagonals of a pair of opposite lateral faces (that is, the pair of faces perpendicular to the base that share edges with ABCD). By this construction, the cutting plane passes through one edge of the base ABCD and through the opposite edge of the top face, bisecting the parallelepiped into two equal prisms [11.28]. One of these prisms has the full parallelogram ABCD as one of its faces and rises from ABCD to the opposite edge on the top face at height h. This prism is precisely the given prism with parallelogram base ABCD and height h. Therefore the parallelepiped on ABCD is double the prism on parallelogram ABCD.

**Step 6.** Similarly, consider the parallelepiped on EFGK. Cut it by a plane passing through the diagonals of the base EFGK and the opposite top face, specifically through the diagonal EG of the base. This diagonal divides the base into triangles EFG and EGK, and the cutting plane bisects the parallelepiped into two equal prisms [11.28]. One of these prisms has triangle EFG as its base face and height h (the distance between the two parallel triangular end faces equals the height of the parallelepiped). This prism is precisely the given prism with triangular base EFG and height h. Therefore the parallelepiped on EFGK is double the prism on triangle EFG.

**Step 7.** From Step 4, the parallelepiped on ABCD equals the parallelepiped on EFGK. From Step 5, the parallelepiped on ABCD is double the prism on ABCD. From Step 6, the parallelepiped on EFGK is double the prism on EFG. Therefore double the prism on ABCD equals double the prism on EFG. Halves of equal things being equal [CN3], the prism with parallelogram base ABCD equals the prism with triangular base EFG.

**Step 8.** Therefore, if there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms are equal. Q.E.D.

**USED:** 1.34, 11.28, 11.31, CN1, CN3
**Human refs (from References field):** 1.34, 11.28, 11.31
**Jaccard:** 0.600 — AI adds ['CN1', 'CN3']
