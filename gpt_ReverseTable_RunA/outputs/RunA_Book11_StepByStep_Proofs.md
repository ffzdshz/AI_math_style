# Book 11 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 11.1
**Statement:** A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.

**Step 1.** Suppose, for a contradiction, that a straight line ABC has a nonzero part AB in the plane of reference π, while its continuation contains a point C above π. Use the direct route of producing AB in π: produce it beyond B to D, far enough to extend past the distance BC. Thus ABD is straight and lies in π. This is straight-line production in the plane, which lies evenly with the straight lines on itself. [P2, D1.7]

**Step 2.** The straight lines ABC and ABD have the whole segment AB in common. They cannot then separate beyond B: a straight line lies evenly with its points, so the same straight segment cannot have two different straight continuations. Consequently BC coincides with the corresponding part of BD. [D1.4]

**Step 3.** Since BD lies in π, this coincidence puts C in π, contrary to its being above π. Therefore a part of a straight line cannot be in the plane of reference and another part in a plane more elevated. [P2, D1.7, D1.4]

**USED:** D1.4, D1.7, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D1.4', 'D1.7', 'P2']

## Proposition 11.2
**Statement:** If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

**Step 1.** Let the distinct straight lines ℓ and m cut one another at O, and choose A on m different from O. Through A draw a straight line n parallel to ℓ. By the definition of parallel straight lines, ℓ and n lie in one plane, say Π. Thus both O and A lie in Π. This parallel-construction route supplies the plane without assuming that the original intersecting lines are coplanar. [1.31, D1.23]

**Step 2.** Join O to A in Π. The straight join lies in Π, since a plane lies evenly with the straight lines on itself. This join is a nonzero part of m. But a straight line cannot have one part in the plane of reference and another part elevated above it; therefore all of m lies in Π. Since ℓ already lies in Π, the two intersecting straight lines lie in one plane. [P1, D1.7, 11.1]

**Step 3.** Now let ABC be any triangle. The straight lines containing AB and AC intersect at A, so, by Step 2, they lie in one plane. Consequently B and C are in that plane, and their straight join BC also lies in it. All three sides, and hence the triangular figure they contain, are therefore in that plane. Thus every triangle is in one plane, completing both assertions. [P1, D1.7, D1.19]

**USED:** 1.31, 11.1, D1.19, D1.23, D1.7, P1
**Human refs (from References field):** 11.1
**Jaccard:** 0.167 — AI adds ['1.31', 'D1.19', 'D1.23', 'D1.7', 'P1']

## Proposition 11.3
**Statement:** If two planes cut one another, their common section is a straight line.

**Step 1.** Let Π and Σ be distinct planes which cut one another, and choose distinct points A and B in their common section. Join AB. By the defining flatness of a plane, this joining straight line lies in each plane. We take the direct route through 11.1, which prevents a straight line from leaving a plane once a portion of it lies there. [P1, D1.7, 11.1]

**Step 2.** Produce AB continuously in both directions, obtaining the straight line ℓ. Since AB lies in each plane, 11.1 implies that its continuations also lie in each plane. Thus ℓ belongs to the common section. [P2, 11.1]

**Step 3.** Suppose that the common section contains a point C not on ℓ. For every point T of the segment AB, join CT. Its endpoints belong to both planes, so the joining segment lies in both. These segments fill the triangular region ABC; hence that entire region belongs to both planes. [P1, D1.7]

**Step 4.** Choose an interior point O of this triangle, and let X be any point of Π other than O. Join OX. A nonzero initial portion of OX lies inside the triangle and therefore in Σ. If X were outside Σ, this straight line would have a portion in Σ and another portion outside it, contrary to 11.1. Consequently every point of Π lies in Σ. Interchanging the two planes gives the reverse inclusion. The planes would therefore coincide, contrary to their being distinct planes cutting one another. Thus no such point C exists. [P1, 11.1]

**Step 5.** The common section contains ℓ by Step 2 and contains no point outside ℓ by Steps 3–4. Therefore their common section is precisely the straight line ℓ. [P2, D1.7, 11.1]

**USED:** 11.1, D1.7, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['11.1', 'D1.7', 'P1', 'P2']

## Proposition 11.4
**Statement:** If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

**Step 1.** Let the straight lines a and b intersect at O, and let ℓ be perpendicular to both at O. Let Π be the plane through a and b. Such a plane exists by 11.2. The line ℓ cannot lie in Π: otherwise, choosing rays of a and b on the same side of ℓ, their angles with a fixed ray of ℓ would both be right, although one would be a proper part of the other. This contradicts the equality of right angles and the fact that the whole is greater than its part. Thus ℓ is not in Π and, by 11.1, meets Π only at O. [11.2, P4, CN5, 11.1]

**Step 2.** Choose P on ℓ, and produce PO through O to Q, taking OQ equal to OP. We use these equal, opposite segments to obtain the required right angle by triangle congruence. [P2, 1.3]

**Step 3.** Let m be any straight line through O in Π other than a or b. Choose A on a and B on b, on opposite sides of m, and join AB. It meets m at a point R between A and B; R is not O, since A, O, B are not collinear. Join PA, QA, PB, QB, PR, and QR. The triangles used below are planar by 11.2. [P1, 11.2]

**Step 4.** The angles POA and POB are right by hypothesis. Since OP and OQ are opposite rays, 1.13 shows that QOA and QOB are also right: in each case, subtracting the given right angle from two right angles leaves a right angle. Consequently, triangles POA and QOA have OP = OQ, OA common, and equal included angles; hence PA = QA. Likewise, triangles POB and QOB give PB = QB. SAS is the natural first comparison here because the two sides and their included right angles are already known. [1.13, P4, CN3, 1.4]

**Step 5.** In triangles PAB and QAB, PA = QA, PB = QB, and AB is common. Therefore their angles PAB and QAB are equal. Since R lies between A and B, it follows that ∠PAR = ∠QAR. [1.8]

**Step 6.** Triangles PAR and QAR now have PA = QA, AR common, and equal included angles. Therefore PR = QR. [1.4]

**Step 7.** In triangles POR and QOR, OP = OQ, OR is common, and PR = QR. Hence ∠POR = ∠QOR. These are adjacent angles on the straight line PQ, so each is right. Thus ℓ makes a right angle with m. [1.8, D1.10]

**Step 8.** The line m was arbitrary among the lines through O in Π other than a and b, and ℓ is perpendicular to a and b by hypothesis. Since every line in Π meeting ℓ meets it at O, ℓ makes right angles with every straight line in Π that meets it. Therefore ℓ is at right angles to Π, as required. [D11.3]

**USED:** 1.13, 1.3, 1.4, 1.8, 11.1, 11.2, CN3, CN5, D1.10, D11.3, P1, P2, P4
**Human refs (from References field):** 1.15, 1.26, 1.4, 1.8, D11.3
**Jaccard:** 0.200 — AI adds ['1.13', '1.3', '11.1', '11.2', 'CN3', 'CN5', 'D1.10', 'P1', 'P2', 'P4']; Human adds ['1.15', '1.26']

## Proposition 11.5
**Statement:** If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

**Step 1.** Let the three given straight lines be a, b, c, meeting at O, and let n make right angles with each at O. By 11.2, a and b lie in a plane Π. We use this plane because 11.4 applies immediately: n is at right angles to Π. [11.2, 11.4]

**Step 2.** Suppose, for a contradiction, that c does not lie in Π. By 11.2, n and c lie in a plane Σ, which is therefore distinct from Π. The two planes meet at O, and their common section is a straight line d through O, by 11.3. Since d lies in Π and n is at right angles to Π, n makes right angles with d at O, by the definition of a straight line at right angles to a plane. Thus, in Σ, both c and d make right angles with n at O. [11.2, 11.3, D11.3]

**Step 3.** In Σ, take a ray ON along n, and rays OC along c and OD along d on opposite sides of n. The adjacent angles CON and NOD are both right angles, by the hypothesis and Step 2, so their sum is two right angles. Apply 1.14 directly: OC and OD are in one straight line. Consequently c is the same straight line as d and lies in Π, contradicting the supposition. Therefore c lies in Π together with a and b, and the three given straight lines are in one plane. [D11.3, 1.14, 11.3]

**USED:** 1.14, 11.2, 11.3, 11.4, D11.3
**Human refs (from References field):** 11.3, 11.4, D11.3
**Jaccard:** 0.600 — AI adds ['1.14', '11.2']

## Proposition 11.6
**Statement:** If two straight lines be at right angles to the same plane, the straight lines will be parallel.

**Step 1.** Let the two distinct straight lines AB and CD be perpendicular to the plane Π at B and D respectively. Their feet are distinct: otherwise the two intersecting lines would lie in a plane Σ, whose intersection with Π would be a straight line through their common foot. Both given lines would be perpendicular to that intersection. Taking their rays on the same side of it, one of the resulting right angles would be a proper part of the other, contrary to the equality of right angles and the fact that the whole is greater than the part. Thus B ≠ D. [11.2, 11.3, D11.3, P4, CN5]

**Step 2.** Join BD in Π. In Π draw EF through D perpendicular to BD, choosing E and F on opposite sides of D with DE = DF. This is done by erecting the perpendicular, producing it, and cutting off the required equal segment. Take A on the first perpendicular, with A ≠ B, and join BE, BF, AE, AF, and AD. The joins between points of Π lie in Π, and every triangle used below lies in a plane. [P1, D1.7, 1.11, P2, 1.3, 11.2]

**Step 3.** In triangles BDE and BDF, BD is common, DE = DF, and the included angles BDE and BDF are right and therefore equal. Hence BE = BF by the side–angle–side theorem. [D1.10, P4, 1.4]

**Step 4.** Since AB is perpendicular to Π, the angles ABE and ABF are right. In triangles ABE and ABF, AB is common, BE = BF, and these included angles are equal. Consequently AE = AF. [D11.3, P4, 1.4]

**Step 5.** Now triangles ADE and ADF have AD common, DE = DF, and AE = AF. Their angles ADE and ADF are therefore equal by the side–side–side theorem. Since DE and DF are opposite rays, these equal adjacent angles are right. Thus AD is perpendicular to EF. [1.8, D1.10]

**Step 6.** The line EF is perpendicular to DB by construction, to DA by Step 5, and to DC because CD is perpendicular to Π. Thus EF is perpendicular to the three lines DB, DA, and DC at their common point D. By 11.5, those three lines lie in one plane Ω. This establishes the coplanarity needed before a planar parallel criterion can be used. [D11.3, 11.5]

**Step 7.** Since A and B lie in Ω, their joining segment AB lies in Ω; the whole straight line AB remains in that plane. The whole line CD also lies in Ω. Hence the two given lines are coplanar. [D1.7, 11.1]

**Step 8.** In Ω, the transversal BD makes right angles with AB at B and with CD at D, since BD lies in Π. Its interior angles on either chosen side therefore equal two right angles. Apply 1.28, whose same-side interior-angle criterion fits these right angles directly. It follows that AB is parallel to CD. Therefore two straight lines perpendicular to the same plane are parallel. [D11.3, 1.28]

**USED:** 1.11, 1.28, 1.3, 1.4, 1.8, 11.1, 11.2, 11.3, 11.5, CN5, D1.10, D1.7, D11.3, P1, P2, P4
**Human refs (from References field):** 1.28, 1.4, 1.8, 11.2, 11.5, D11.3
**Jaccard:** 0.375 — AI adds ['1.11', '1.3', '11.1', '11.3', 'CN5', 'D1.10', 'D1.7', 'P1', 'P2', 'P4']

## Proposition 11.7
**Statement:** If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

**Step 1.** Let ℓ and m be the given parallel straight lines, let A lie on ℓ and B on m, and let s be the straight line joining A to B. By the definition of parallels, ℓ and m lie in a plane Π and do not meet. In particular, B does not lie on ℓ. [D1.23]

**Step 2.** The straight lines ℓ and s intersect at A, so they lie in a plane Σ. We use the intersecting-lines clause of 11.2 directly, since these two lines already intersect; this supplies a plane containing the joining line and sharing ℓ with Π. [11.2]

**Step 3.** If Σ and Π were distinct, their common section would be a straight line. Since both planes contain ℓ, that common section would be ℓ itself. But B belongs to Σ because it lies on s, and B belongs to Π because it lies on m. Consequently B would lie on ℓ, contrary to the fact that the parallel lines ℓ and m do not meet. Therefore Σ = Π, and s lies in the same plane as both parallel straight lines, as required. [11.3, D1.23]

**USED:** 11.2, 11.3, D1.23
**Human refs (from References field):** 11.3
**Jaccard:** 0.333 — AI adds ['11.2', 'D1.23']

## Proposition 11.8
**Statement:** If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

**Step 1.** Let ℓ and m be parallel straight lines, and let ℓ be perpendicular to the plane Π at B. The parallels lie in a plane Σ. This plane is distinct from Π, and their common section is a straight line g through B. [D1.23, D11.3, 11.3]

**Step 2.** The line m meets g. For otherwise, being coplanar and not meeting, m and g would be parallel; since ℓ is also parallel to m, ℓ would be parallel to g, contrary to their meeting at B. Denote the intersection of m and g by D. Since ℓ and m do not meet, D differs from B. Now ℓ is perpendicular to BD because BD lies in Π; hence, by the angles made by a transversal of parallels, m is also perpendicular to BD. [D1.23, 1.30, D11.3, 1.29]

**Step 3.** We use the two-intersecting-lines criterion of 11.4, since BD already supplies one perpendicular to m in Π. Choose A on ℓ distinct from B. In Π draw DE perpendicular to BD at D, taking E distinct from D. Join AD within Σ, BE within Π, and AE. The triangles ABE and ADE are planar. It remains to establish that m is perpendicular to DE. [11.4, 1.11, P1, 11.2]

**Step 4.** Since ℓ is perpendicular to Π, AB is perpendicular to BE as well as to BD. Applying the theorem on the square of the hypotenuse to the right triangles ABD, BDE, and ABE gives
AD² = AB² + BD²,
BE² = BD² + DE²,
AE² = AB² + BE².
Here each squared length denotes the square on the corresponding segment. [D11.3, 1.47]

**Step 5.** Substituting the second equality into the third, and then using the first, gives
AE² = AB² + BD² + DE² = AD² + DE².
Therefore the angle ADE is right, so DE is perpendicular to DA. [CN2, CN1, 1.48]

**Step 6.** Thus DE is perpendicular to both DB and DA at their common point D. These are two intersecting straight lines in Σ. Consequently DE is perpendicular to Σ. [11.4]

**Step 7.** Since m lies in Σ and meets DE at D, DE is perpendicular to m. Therefore m is perpendicular to both DB and DE, which intersect at D and lie in Π. By the two-line criterion, m is perpendicular to Π. Hence, if two straight lines are parallel and one is perpendicular to a plane, the remaining one is also perpendicular to that plane. [D11.3, 11.4]

**USED:** 1.11, 1.29, 1.30, 1.47, 1.48, 11.2, 11.3, 11.4, CN1, CN2, D1.23, D11.3, P1
**Human refs (from References field):** 1.29, 11.2, 11.4, 11.7, D11.3
**Jaccard:** 0.286 — AI adds ['1.11', '1.30', '1.47', '1.48', '11.3', 'CN1', 'CN2', 'D1.23', 'P1']; Human adds ['11.7']

## Proposition 11.9
**Statement:** Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

**Step 1.** Let a and b each be parallel to c, with the three lines not all in one plane. By the definition of parallel lines, there is a plane Π containing a and c and a plane Σ containing b and c. These planes are distinct by the hypothesis. We use a common perpendicular plane, since coplanarity of a and b has not yet been established. [D1.23]

**Step 2.** The common section of Π and Σ is the straight line c. Choose a point O on c. In Π draw x through O perpendicular to c, and in Σ draw y through O perpendicular to c. The lines x and y are distinct: otherwise their common line would lie in both Π and Σ and hence would be c, although it is perpendicular to c. Thus x and y intersect at O. [11.3, 1.11]

**Step 3.** The intersecting lines x and y lie in a plane Ω. Since c is perpendicular to both x and y at their common point O, c is perpendicular to Ω. [11.2, 11.4]

**Step 4.** Since a is parallel to c and c is perpendicular to Ω, a is perpendicular to Ω. Likewise, since b is parallel to c, b is perpendicular to Ω. [11.8]

**Step 5.** The straight lines a and b are perpendicular to the same plane Ω; therefore they are parallel to one another. Hence straight lines parallel to the same straight line, though not all in one plane, are also parallel to one another. [11.6]

**USED:** 1.11, 11.2, 11.3, 11.4, 11.6, 11.8, D1.23
**Human refs (from References field):** 11.4, 11.6, 11.8
**Jaccard:** 0.429 — AI adds ['1.11', '11.2', '11.3', 'D1.23']

## Proposition 11.10
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.

**Step 1.** Let AB, AC meet at A, and DE, DF meet at D, with AB parallel to DE and AC parallel to DF; suppose the four lines are not in one plane. Choose endpoints in corresponding directions on each parallel pair, cutting off segments so that AB = DE and AC = DF. Join AD, BE, CF, BC, and EF. We will compare triangles ABC and DEF by their three sides. [1.3, P1]

**Step 2.** The joins AD and BE lie in the plane of the parallel lines AB and DE. Since AB and DE are equal and parallel, their corresponding joins AD and BE are also equal and parallel. Likewise, applying the same result to AC and DF gives AD and CF equal and parallel. The joins BE and CF are both directed correspondingly to AD. [11.7, 1.33]

**Step 3.** The three lines AD, BE, CF cannot all lie in one plane. For, if they did, the joins AB and DE between the parallel lines AD and BE, and the joins AC and DF between AD and CF, would also lie in that plane, contrary to the hypothesis. Thus the spatial common-parallel theorem applies: since BE and CF are each parallel to AD and the three lines are not all coplanar, BE is parallel to CF. This is why we use the spatial rather than the planar common-parallel result. [11.7, 11.9]

**Step 4.** Since BE = AD and CF = AD, we have BE = CF. [CN1]

**Step 5.** Therefore BE and CF are equal and parallel, with B, C and E, F their respective corresponding extremities. Their joins BC and EF lie in their plane and are themselves equal and parallel. In particular, BC = EF. [11.7, 1.33]

**Step 6.** In triangles ABC and DEF, we now have AB = DE, AC = DF, and BC = EF. Hence the angles contained by the first two pairs of equal sides are equal: ∠BAC = ∠EDF. Thus the two pairs of intersecting parallel straight lines contain equal corresponding angles, as required. [1.8]

**USED:** 1.3, 1.33, 1.8, 11.7, 11.9, CN1, P1
**Human refs (from References field):** 1.33, 1.8, 11.9
**Jaccard:** 0.429 — AI adds ['1.3', '11.7', 'CN1', 'P1']

## Proposition 11.11
**Statement:** From a given elevated point to draw a straight line perpendicular to a given plane.

**Step 1.** Let A be the given point outside the given plane Π. Choose a straight line ℓ in Π and a point B on ℓ. Join AB; the intersecting lines AB and ℓ lie in a plane. In that plane draw AD perpendicular to ℓ, with D on ℓ. Thus D lies in Π. [P1, 11.2, 1.12]

**Step 2.** In Π draw the straight line m through D perpendicular to ℓ. The intersecting lines AD and m lie in a plane Σ. Since A is not in Π, it is not on m; therefore, within Σ, draw AH perpendicular to m, with H on m. In particular, H lies in Π. [1.11, 11.2, 1.12]

**Step 3.** If H coincides with D, then AH is perpendicular to both ℓ and m at their common point D. Hence AH is perpendicular to Π, and the construction is complete in this case. This uses the direct two-intersecting-lines criterion, naturally supplied by the construction. [11.4]

**Step 4.** Suppose now that H is distinct from D. Since ℓ is perpendicular to both AD and m at D, it is perpendicular to their plane Σ. Also, H is not on ℓ, since ℓ and m intersect at D. Within Π draw a straight line n through H parallel to ℓ. We use this parallel to transfer the perpendicularity just obtained to the required foot H. [11.4, 1.31]

**Step 5.** Because n is parallel to ℓ and ℓ is perpendicular to Σ, n is also perpendicular to Σ. The straight line AH lies in Σ and meets n at H; consequently n makes a right angle with AH. [11.8, D11.3]

**Step 6.** Thus AH is perpendicular to both m and n at H. These are distinct intersecting straight lines in Π: m meets ℓ, whereas n is parallel to ℓ. Therefore AH is perpendicular to Π by the same two-intersecting-lines criterion. Since AH joins the given elevated point A to the point H of Π, the required perpendicular has been drawn. [11.4]

**USED:** 1.11, 1.12, 1.31, 11.2, 11.4, 11.8, D11.3, P1
**Human refs (from References field):** 1.11, 1.12, 1.31, 11.4, 11.8, D11.3
**Jaccard:** 0.750 — AI adds ['11.2', 'P1']

## Proposition 11.12
**Statement:** To set up a straight line at right angles to a given plane from a given point in it.

**Step 1.** Let Π be the given plane and A the given point in it. The direct route is to construct an auxiliary perpendicular using 11.11, then transfer its direction through A. Choose a point B outside Π and draw BC perpendicular to Π, meeting Π at C. [11.11]

**Step 2.** If C coincides with A, then AB is already the required perpendicular. Otherwise join AC. The intersecting straight lines AC and BC lie in one plane, so the following parallel construction can be performed in that plane. [11.11, P1, 11.2]

**Step 3.** In the plane containing AC and BC, draw through A a straight line AD parallel to BC. [1.31]

**Step 4.** Since BC is perpendicular to Π and AD is parallel to BC, AD is also perpendicular to Π. Thus a straight line has been set up at right angles to the given plane from the given point A in it, as required. [11.8]

**USED:** 1.31, 11.11, 11.2, 11.8, P1
**Human refs (from References field):** 1.31, 11.11, 11.8
**Jaccard:** 0.600 — AI adds ['11.2', 'P1']

## Proposition 11.13
**Statement:** From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

**Step 1.** Suppose, for a contradiction, that two distinct straight lines AB and AC are set up from the same point A at right angles to a plane Π on the same side. Use XI.6 directly, since both lines are perpendicular to the same plane: AB and AC must therefore be parallel. [11.6]

**Step 2.** Parallel straight lines, even when produced indefinitely in both directions, do not meet. But AB and AC meet at A, contradicting their parallelism. Thus from the same point two distinct straight lines cannot be set up at right angles to the same plane on the same side. [D1.23]

**USED:** 11.6, D1.23
**Human refs (from References field):** 11.3, D11.3
**Jaccard:** 0.000 — AI adds ['11.6', 'D1.23']; Human adds ['11.3', 'D11.3']

## Proposition 11.14
**Statement:** Planes to which the same straight line is at right angles will be parallel.

**Step 1.** Let Π and Σ be distinct planes perpendicular to the same straight line ℓ, at A and B respectively. First, A and B must be distinct. Otherwise, choose two distinct lines r and s in Π through their common foot, and a line t in Σ through that foot but not in Π. By the definition of perpendicularity to a plane, ℓ is perpendicular to all three lines (D11.3). Hence r, s, and t lie in one plane by XI.5. That plane must be Π: otherwise its common section with Π would contain both r and s, contrary to XI.3. This contradicts the choice of t. Thus A ≠ B. (D11.3; 11.5; 11.3)

**Step 2.** Suppose, for a contradiction, that Π and Σ meet. Their common section is a straight line; choose a point C on it different from A and B (11.3). Join AC in Π and BC in Σ. (P1; D1.7)

**Step 3.** Since AB is perpendicular to Π and AC lies in Π, ∠BAC is a right angle. Since AB is also perpendicular to Σ and BC lies in Σ, ∠ABC is a right angle (D11.3). In particular, A, B, and C are not collinear, and their triangle lies in one plane. (11.2)

**Step 4.** In any triangle, any two angles together are less than two right angles (1.17). Applied to triangle ABC, this contradicts the two right angles just obtained. This direct two-angle bound is sufficient; no full triangle angle-sum theorem is needed.

**Step 5.** Therefore Π and Σ do not meet. Planes which do not meet are parallel (D11.8). Hence planes to which the same straight line is at right angles are parallel.

**USED:** 1.17, 11.2, 11.3, 11.5, D1.7, D11.3, D11.8, P1
**Human refs (from References field):** 1.17, 11.3, D11.3, D11.8
**Jaccard:** 0.500 — AI adds ['11.2', '11.5', 'D1.7', 'P1']

## Proposition 11.15
**Statement:** If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

**Step 1.** Let AB and AC meet at A in the plane α, and let DE and DF meet at D in the plane β, with AB parallel to DE and AC parallel to DF, as given. We take the direct common-perpendicular route: it suffices to find one straight line perpendicular to both planes. [11.14]

**Step 2.** At A erect a straight line g perpendicular to α. Then g is perpendicular to both AB and AC, since these lines lie in α and meet g at A. [11.12, D11.3]

**Step 3.** If D does not lie on g, draw through D a straight line h parallel to g. Since g is perpendicular to α, h is also perpendicular to α. If D lies on g, take h to be g itself; the same perpendicularity already holds. [1.31, 11.8]

**Step 4.** We show that h is perpendicular to DE and DF. First compare the pair g, AB with the pair h, DE. When their angle-planes differ, their corresponding angles are equal by 11.10, so the angle between h and DE is right. When the angle-planes coincide and g and h are distinct, applying 1.29 successively to the two parallel pairs gives the same conclusion. When h is g itself, 1.29 applies directly to this common transversal of AB and DE. Thus h is perpendicular to DE. Applying exactly the same argument to g, AC and h, DF shows that h is perpendicular to DF. The spatial angle-transfer theorem is used where applicable; its planar counterpart is used only in the coplanar cases. [11.10, 1.29]

**Step 5.** Since h is perpendicular to the two intersecting straight lines DE and DF at their common point D, it is perpendicular to their plane β. But h is also perpendicular to α by Step 3. Therefore α and β are parallel, being planes to which the same straight line is perpendicular. Hence the planes through the given pairs of straight lines are parallel. [11.4, 11.14]

**USED:** 1.29, 1.31, 11.10, 11.12, 11.14, 11.4, 11.8, D11.3
**Human refs (from References field):** 1.29, 1.31, 11.11, 11.14, 11.4, 11.9, D11.3
**Jaccard:** 0.500 — AI adds ['11.10', '11.12', '11.8']; Human adds ['11.11', '11.9']

## Proposition 11.16
**Statement:** If two parallel planes be cut by any plane, their common sections are parallel.

**Step 1.** Let the parallel planes α and β be cut by a plane γ, and let their common sections with γ be a and b respectively. Each section is a straight line, and both lie in γ. [11.3]

**Step 2.** When a and b are produced indefinitely in either direction, they remain in their respective planes α and β, and also in γ: a straight line cannot lie partly in a plane and partly outside it. [11.1]

**Step 3.** Since α and β are parallel, they do not meet. Consequently, a and b cannot meet in either direction, even when produced; any meeting point would belong to both α and β, contrary to their parallelism. [D11.8]

**Step 4.** Thus a and b are straight lines in the same plane which, produced indefinitely in both directions, do not meet. By the definition of parallel straight lines, a is parallel to b. This defining non-intersection criterion is the direct route here, since the cutting plane already supplies their common plane. Therefore, the common sections of two parallel planes with any cutting plane are parallel. [D1.23]

**USED:** 11.1, 11.3, D1.23, D11.8
**Human refs (from References field):** 11.1, D1.23
**Jaccard:** 0.500 — AI adds ['11.3', 'D11.8']

## Proposition 11.17
**Statement:** If two straight lines be cut by parallel planes, they will be cut in the same ratios.

**Step 1.** Let three parallel planes α, β, γ, with β between the other two, cut the two straight lines at A, B, C and D, E, F respectively. We must prove AB:BC = DE:EF. First suppose A ≠ D and C ≠ F. Join AF, meeting β at G. The intersecting lines AC and AF lie in one plane, and DF and AF lie in another. We use these two planes to reduce the assertion directly to proportional division in triangles. [P1, 11.2]

**Step 2.** In the plane ACF, the sections of β and γ are BG and CF; hence BG ∥ CF. In the plane ADF, the sections of α and β are AD and GE; hence AD ∥ GE. In each case the sections are parallel because the planes being cut are parallel. [11.16]

**Step 3.** In triangle ACF, the parallel BG to the side CF cuts the other sides proportionally, giving AB:BC = AG:GF. In triangle FAD, the parallel GE to the side AD likewise gives DE:EF = AG:GF, reading both divisions from α towards γ. [6.2]

**Step 4.** Since AB:BC and DE:EF are equal to the same ratio AG:GF, they are equal to one another. Thus AB:BC = DE:EF. [5.11]

**Step 5.** If the distinct transversals share an outer intersection, only one triangle is needed. If A = D, use triangle ACF: its sections give BE ∥ CF, and therefore AB:BC = AE:EF = DE:EF. If C = F, use triangle CAD: its sections give BE ∥ AD, and therefore AB:BC = DE:EC = DE:EF. These triangles are planar, their indicated sections are parallel, and their sides are consequently divided proportionally. [11.2, 11.16, 6.2] Coincident transversals have identical corresponding segments. Thus, for any three parallel cutting planes, the corresponding divisions of the two straight lines have the same ratio, as required.

**USED:** 11.16, 11.2, 5.11, 6.2, P1
**Human refs (from References field):** 11.16, 5.11, 6.2
**Jaccard:** 0.600 — AI adds ['11.2', 'P1']

## Proposition 11.18
**Statement:** If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

**Step 1.** Let the straight line ℓ be perpendicular to the plane Π at O, and let Σ be any plane through ℓ. We shall verify the defining condition for perpendicular planes: every straight line in Σ perpendicular to its common section with Π is perpendicular to Π (D11.4). The planes are distinct and meet at O, so their common section is a straight line s through O (11.3).

**Step 2.** Since s lies in Π and meets ℓ at O, the perpendicularity of ℓ to Π implies that ℓ is perpendicular to s (D11.3).

**Step 3.** Consider any straight line m in Σ perpendicular to s, and let C be its intersection with s. If C = O, choose rays of ℓ and m on opposite sides of s. They make adjacent right angles with a ray of s, and therefore lie in one straight line by 1.14. Thus m coincides with ℓ and is perpendicular to Π by hypothesis.

**Step 4.** If C ≠ O, the transversal s makes right alternate angles with ℓ and m. These angles are equal by P4, so ℓ and m are parallel by 1.27. We use the equal-alternate-angle criterion directly because the perpendicularities supply precisely those angles. Since ℓ is perpendicular to Π, its parallel m is also perpendicular to Π (11.8).

**Step 5.** Consequently every straight line in Σ drawn perpendicular to s is perpendicular to Π. Hence Σ is perpendicular to Π by D11.4. Since Σ was an arbitrary plane through ℓ, all planes through ℓ are perpendicular to Π, as required.

**USED:** 1.14, 1.27, 11.3, 11.8, D11.3, D11.4, P4
**Human refs (from References field):** 1.11, 1.28, 11.8, D11.3, D11.4
**Jaccard:** 0.333 — AI adds ['1.14', '1.27', '11.3', 'P4']; Human adds ['1.11', '1.28']

## Proposition 11.19
**Statement:** If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

**Step 1.** Let the distinct planes α and β cut one another, and let each be perpendicular to the plane γ. Write ℓ = α ∩ β, a = α ∩ γ, and b = β ∩ γ. These common sections are straight lines. Choose a point P on ℓ; we do not assume that P lies in γ. [11.3]

**Step 2.** In α construct a straight line p through P perpendicular to a: use the construction at a point on a line if P lies on a, and otherwise the construction from a point outside a line. Similarly, in β construct a straight line q through P perpendicular to b. [1.11, 1.12]

**Step 3.** Since α is perpendicular to γ, the line p, drawn in α perpendicular to their common section a, is perpendicular to γ. For the same reason, q is perpendicular to γ. [D11.4]

**Step 4.** If p and q were distinct, then, being perpendicular to the same plane γ, they would be parallel. But both pass through P, whereas parallel straight lines do not meet. Thus p and q coincide. This comparison uses 11.6 directly because it does not require P to lie in γ. [11.6, D1.23]

**Step 5.** The coincident line p = q lies in both α and β, so it is their common section ℓ. Since p is perpendicular to γ, their common section ℓ is therefore perpendicular to γ, as required. [11.3, D11.4]

**USED:** 1.11, 1.12, 11.3, 11.6, D1.23, D11.4
**Human refs (from References field):** 11.13, D11.4
**Jaccard:** 0.143 — AI adds ['1.11', '1.12', '11.3', '11.6', 'D1.23']; Human adds ['11.13']

## Proposition 11.20
**Statement:** If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

**Step 1.** Let the solid angle have vertex O and three noncoplanar edges OA, OB, OC. We shall prove
∠AOC + ∠COB > ∠AOB.
The choice of the remaining angle ∠AOB is arbitrary, so this will establish every required inequality. [D11.11]

**Step 2.** If either ∠AOC or ∠COB is at least ∠AOB, their sum is greater than ∠AOB, since the sum is greater than either of its positive parts. Thus it remains to consider the case in which ∠AOB is greater than each of the other two angles. [CN5]

**Step 3.** Join AB. In the plane AOB, construct a ray OE inside ∠AOB such that ∠AOE = ∠AOC, and let E be its intersection with AB. Since the ray is interior, E lies between A and B. Choose the point C on the third edge so that OC = OE, extending that edge if necessary and cutting off the required length. This does not change its direction or the angles at O. Join AC and BC. Every triangle used below lies in a plane. [P1, 1.23, P2, 1.3, 11.2]

**Step 4.** In triangles AOC and AOE, OA is common, OC = OE, and ∠AOC = ∠AOE. Therefore their bases are equal:
AC = AE. [1.4]

**Step 5.** In triangle ABC, the two sides AC and CB together are greater than AB. Substituting AC = AE and AB = AE + EB gives
AE + CB > AE + EB,
and hence
CB > EB. [1.20]

**Step 6.** Compare triangles COB and EOB. They have OC = OE and OB common, while CB > EB. Therefore
∠COB > ∠EOB.
Here 1.25 is the direct choice: the established comparison is between the bases of triangles having two corresponding sides equal. [1.25]

**Step 7.** Combining this strict inequality with ∠AOC = ∠AOE gives
∠AOC + ∠COB > ∠AOE + ∠EOB = ∠AOB,
the last equality holding because OE lies inside ∠AOB. Since any of the three plane angles could have been chosen as the remaining angle, any two, taken together in any manner, are greater than the remaining one. [1.23, 1.25]

**USED:** 1.20, 1.23, 1.25, 1.3, 1.4, 11.2, CN5, D11.11, P1, P2
**Human refs (from References field):** 1.20, 1.25, 1.4
**Jaccard:** 0.300 — AI adds ['1.23', '1.3', '11.2', 'CN5', 'D11.11', 'P1', 'P2']

## Proposition 11.21
**Statement:** Any solid angle is contained by plane angles less than four right angles.

**Step 1.** Let O be the vertex of the given solid angle. Take a plane section across its successive edges, meeting them at A₁, …, Aₙ in cyclic order, and join consecutive section points. The section is a convex plane polygon, and the lateral faces are the triangles OAᵢAᵢ₊₁, with indices read cyclically. Write R for a right angle and T for the sum of the bounding plane angles ∠AᵢOAᵢ₊₁. We shall compare the angles of these lateral triangles with those of the section polygon. [D11.11, P1]

**Step 2.** Draw the diagonals of the section polygon from A₁, dividing it into n−2 triangles. By I.32, each triangle has angles equal to 2R. Adding these equalities, and observing that the triangle angles together constitute exactly the interior angles of the polygon, gives
G = (2n−4)R,
where G is the sum of those interior angles. Thus the needed polygon-angle total follows directly from I.32. [P1, 1.32, CN2]

**Step 3.** At each section vertex Aᵢ, the three lines AᵢO, AᵢAᵢ₋₁, and AᵢAᵢ₊₁ form a solid angle contained by three plane angles. By XI.20,
∠Aᵢ₋₁AᵢO + ∠OAᵢAᵢ₊₁ > ∠Aᵢ₋₁AᵢAᵢ₊₁.
This is the direct local comparison: XI.20 applies to the three angles at each section vertex, without assuming the proposition being proved. Let eᵢ be the positive excess on the left. [11.20]

**Step 4.** Apply I.32 to all n lateral triangles and add. Their angles at O sum to T; their remaining angles, grouped at the section vertices, sum to G + E, where E = e₁ + ⋯ + eₙ is positive. Consequently,
T + G + E = 2nR. [1.32, CN2]

**Step 5.** Substitute G = (2n−4)R and subtract this common angle total. It follows that
T + E = 4R.
Since E is positive, T is a proper part of four right angles and is therefore less than four right angles. Hence any solid angle is contained by plane angles whose sum is less than four right angles. [CN3, CN5]

**USED:** 1.32, 11.20, CN2, CN3, CN5, D11.11, P1
**Human refs (from References field):** 1.32, 11.20
**Jaccard:** 0.286 — AI adds ['CN2', 'CN3', 'CN5', 'D11.11', 'P1']

## Proposition 11.22
**Statement:** If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

**Step 1.** Let the three given angles be α, β, γ, and let the straight lines joining their respective extremities have lengths a, b, c. Let r be the common length of all the straight lines containing the angles. Relabel so that γ is greatest. Then c ≥ a and c ≥ b: equal angles give equal bases by 1.4, and a greater angle between equal sides gives a greater base by 1.24. We take this direct planar base-comparison route, since the containing sides are already equal. [1.4, 1.24]

**Step 2.** Since all three joining lines have positive length, c ≥ a and c ≥ b imply b+c>a and a+c>b. Thus only a+b>c remains to be established. If γ equals either α or β, then c equals the corresponding joining line, and a+b>c follows immediately. Hence it remains to consider the case γ>α and γ>β. [1.4, CN5]

**Step 3.** Write the given angle γ as ∠AOC, where OA=OC=r and AC=c. Describe the circle with centre O and radius OA. Within ∠AOC construct a ray OB making ∠AOB=α, and let B be its intersection with the circle. This ray lies strictly inside ∠AOC because 0<α<γ. Then OA=OB=OC=r. Join AB and BC. [P3, 1.23, D1.15, P1]

**Step 4.** The distinct points A, B, C are not collinear. For otherwise one would lie between the other two on their joining chord; but the interior of that chord lies within the circle, whereas all three points lie on its circumference. Thus ABC is a triangle, and consequently AC<AB+BC. [3.2, 1.20]

**Step 5.** By 1.4, AB=a, since ∠AOB=α and its containing sides both have length r. Put δ=∠BOC. The construction gives α+δ=γ, while the hypothesis gives α+β>γ; hence δ<β. The sides containing δ and those containing the given angle β are respectively equal, so 1.24 gives BC<b. Therefore
c=AC<AB+BC<a+b.
Together with the equality cases in Step 2, this establishes a+b>c in every case. [1.4, 1.24, CN5]

**Step 6.** We have now shown that any two of a, b, c taken together are greater than the remaining one. By 1.22, a triangle can therefore be constructed with its three sides respectively equal to these three joining lines. This is the required construction. [1.22]

**USED:** 1.20, 1.22, 1.23, 1.24, 1.4, 3.2, CN5, D1.15, P1, P3
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 0.200 — AI adds ['1.20', '1.22', '1.23', '3.2', 'CN5', 'D1.15', 'P1', 'P3']

## Proposition 11.23
**Statement:** To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

**Step 1.** Let the given plane angles be α, β, γ, and write q for a right angle. Thus each angle is less than 2q, and
α+β>γ, β+γ>α, γ+α>β.
In accordance with the final clause, assume also α+β+γ<4q. This last restriction is necessary for a solid angle by 11.21; it is an additional condition on the construction data. [11.21]

**Step 2.** Cut off the same positive length r on both arms of each given angle, and join the resulting endpoints. Denote the three joining segments by a, b, c, corresponding respectively to α, β, γ. By 11.22 construct a triangle ABC with BC=a, CA=b, AB=c. This is the direct route: 11.22 applies precisely to the equal-arm construction just made. [1.3, P1, 11.22]

**Step 3.** Circumscribe a circle about ABC and find its centre O. Put OA=OB=OC=R. We shall show that R<r, so that an appropriate perpendicular height above O can be constructed. Write A₀, B₀, C₀ for the interior angles of triangle ABC. [4.5, 3.1, D1.15]

**Step 4.** Suppose, to the contrary, that R≥r. Each of a, b, c is less than 2r by the triangle inequality applied to its original equal-arm triangle. Consequently each is less than 2R; none is a diameter of the circumcircle, and ABC is not right-angled. Let θa, θb, θc be the smaller central angles subtending a, b, c.

We have θa≤α, θb≤β, θc≤γ. Indeed, construct an isosceles triangle with equal sides r and vertex angle θa. Its base is (r/R)a: its angles equal those of triangle BOC by the isosceles-triangle theorem and the angle sum, and its sides are therefore proportional. This base is at most a. If θa>α, however, 1.24 would make its base greater than a, a contradiction. The other two comparisons follow identically. [1.20, 3.31, 1.23, 1.5, 1.32, 6.4, 1.24]

**Step 5.** If ABC is acute-angled, the central-angle theorem gives
θa=2A₀, θb=2B₀, θc=2C₀.
Hence θa+θb+θc=4q. The comparisons in Step 4 would then give α+β+γ≥4q, contrary to Step 1. Thus, under the supposition R≥r, the only remaining case is an obtuse triangle. Relabel the vertices and their corresponding given angles, if necessary, so that C₀ is obtuse. [3.20, 1.32]

**Step 6.** Describe a circle with centre T and radius r. On it construct successive central turns α and β, giving points X, Y, Z in that order. Then XY=a and YZ=b by side-angle-side congruence. The smaller central angle δ subtending XZ is the smaller of α+β and 4q−α−β. Both these quantities exceed γ, by Step 1; hence δ>γ.

Put d=XZ. If δ<2q, comparison of the equal-radius triangles gives d>c by 1.24. If δ=2q, then d=2r>c by the triangle inequality. Thus d>c in either case. [P3, 1.23, 1.3, 1.4, 1.24, 1.20]

**Step 7.** The radius YT lies inside angle XYZ. The isosceles triangles TXY and TYZ therefore give
∠XYZ=(2q−α)/2+(2q−β)/2=2q−(α+β)/2.
Triangles XYZ and BCA have the corresponding sides a and b equal, while their opposite sides satisfy d>c. Therefore
C₀<∠XYZ=2q−(α+β)/2.
Since C₀ is obtuse, the smaller central angle over AB is θc=4q−2C₀. Consequently
θc>α+β>γ,
contrary to θc≤γ in Step 4. Both possible cases have contradicted R≥r. Therefore R<r. [1.5, 1.32, 1.25, 3.20]

**Step 8.** Construct the required height explicitly. Bisect a segment of length r, and construct a triangle UMT with UM=MT=r/2 and UT=R. This is possible because 0<R<r. Extend UM beyond M to V with MV=UM. The circle with centre M and radius r/2 passes through U, T, V, and UV is a diameter. Thus ∠UTV is right. Put h=TV; then h>0 and
h²+R²=r².
Here squares denote the squares on the corresponding segments. [1.10, 1.22, P2, 1.3, P3, 3.31, 1.47]

**Step 9.** At O erect a straight line perpendicular to the plane ABC, and mark S on it with OS=h. Join SA, SB, SC. By the definition of perpendicularity to a plane, the angles SOA, SOB, SOC are right. Hence
SA²=OS²+OA²=h²+R²=r²,
and likewise SB²=SC²=r². Therefore SA=SB=SC=r. Moreover, S is outside the plane ABC because h>0. [11.12, 1.3, P1, D11.3, 1.47]

**Step 10.** Triangle SBC has sides r, r, a, so its angle BSC equals α by side-side-side congruence with the original equal-arm triangle. Likewise ∠CSA=β and ∠ASB=γ. Since ABC is a nondegenerate triangle and S is outside its plane, the three rays SA, SB, SC are not coplanar. They therefore form a solid angle whose three plane angles are exactly the given angles. The required solid angle has been constructed. [1.8, D11.11]

**USED:** 1.10, 1.20, 1.22, 1.23, 1.24, 1.25, 1.3, 1.32, 1.4, 1.47, 1.5, 1.8, 11.12, 11.21, 11.22, 3.1, 3.20, 3.31, 4.5, 6.4, D1.15, D11.11, D11.3, P1, P2, P3
**Human refs (from References field):** 1.25, 1.29, 1.4, 1.47, 1.8, 11.12, 11.22, 5.16, 6.2, 6.4
**Jaccard:** 0.241 — AI adds ['1.10', '1.20', '1.22', '1.23', '1.24', '1.3', '1.32', '1.5', '11.21', '3.1', '3.20', '3.31', '4.5', 'D1.15', 'D11.11', 'D11.3', 'P1', 'P2', 'P3']; Human adds ['1.29', '5.16', '6.2']

## Proposition 11.24
**Statement:** If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

**Step 1.** Let the solid have opposite faces ABCD and EFGH, with corresponding vertices A, E; B, F; C, G; D, H. Its three pairs of opposite bounding planes are therefore ABCD and EFGH, ABFE and DCGH, and ADHE and BCGF; each pair is parallel by hypothesis. In the plane of any face, its opposite sides are the common sections with a pair of parallel bounding planes. These sections are parallel by 11.16. Thus every face is parallelogrammic. [11.16]

**Step 2.** Consider the opposite faces ABCD and EFGH. Since ABFE and ADHE are parallelograms, their opposite sides give AB = EF and AD = EH. Also, by Step 1, AB is parallel to EF, and AD is parallel to EH. [1.34]

**Step 3.** For the angle comparison, use the theorem about parallel sides in different planes, since it applies directly to the sides just obtained. The intersecting straight lines AB, AD are respectively parallel to EF, EH in the opposite plane; hence angle BAD equals angle FEH. [11.10]

**Step 4.** Join BD and FH. The triangles BAD and FEH have BA = FE and AD = EH, with the included angles equal. Therefore the triangles BAD and FEH are equal. [P1, 1.4]

**Step 5.** The diagonal BD bisects the parallelogram ABCD, and FH bisects the parallelogram EFGH. Consequently these parallelograms are doubles of the equal triangles BAD and FEH, respectively, and are equal by addition of equals to equals. The choice of opposite faces was arbitrary, so the same argument applies to either remaining pair. Every face is parallelogrammic by Step 1, and every pair of opposite faces is equal. Therefore, if a solid is contained by parallel planes, its opposite planes are equal and parallelogrammic. [1.34, CN2]

**USED:** 1.34, 1.4, 11.10, 11.16, CN2, P1
**Human refs (from References field):** 1.34, 1.4, 11.10, 11.16
**Jaccard:** 0.667 — AI adds ['CN2', 'P1']

## Proposition 11.25
**Statement:** If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.

**Step 1.** Let the cutting plane F₁ be parallel to the opposite faces F₀ and F₂, dividing the given parallelepiped into solids S and T. Let b and c be their respective bases, the two portions of one face cut by F₁. Choose an edge crossing these three planes, and denote its intersections with F₀, F₁, F₂ by A, E, B, respectively. The sections in each face are parallel, and the resulting solids have parallelogram faces. [11.16, 11.24] We use the equimultiple criterion directly, because bases and solids can be repeated together without introducing an auxiliary proportion. [D5.5]

**Step 2.** Continue the four face-planes other than F₀ and F₂, retaining them as fixed lateral boundaries, and produce AB. Let m and n be arbitrary positive integers. Starting at A on the ray AB, mark m consecutive lengths equal to AE, ending at X; independently, starting at A on the same ray, mark n consecutive lengths equal to EB, ending at Y. [P2, 1.3] Through each mark draw a plane parallel to F₀: in the two lateral planes meeting along AB, draw lines parallel to the two edges of F₀ through A; the plane through these lines is parallel to F₀. [1.31, 11.15] Let U and V be the solids between F₀ and the terminal planes through X and Y, and let u and v be their bases in the original base plane.

**Step 3.** We justify the equality of the repeated pieces. Any two of these parallel section planes, together with the fixed lateral boundaries, enclose a parallelepiped with parallelogram faces. [11.24] Its two end sections have corresponding sides equal and parallel, by applying I.34 to the intervening lateral faces. Their corresponding angles are therefore equal by XI.10. Dividing the end parallelograms along corresponding diagonals and applying I.4 shows that they are equal and similar. Thus all the end sections are equal and similar. [1.34, 11.10, 1.4]

Now consider two cells whose intercepted lengths on AB are equal. Their lateral faces have equal corresponding sides by I.34 and the equality of the end-section sides just established. Corresponding angles are equal by I.29, since corresponding lateral faces lie in the same fixed plane and their section edges are parallel. Applying I.4 along corresponding diagonals shows that these faces also are equal and similar. Consequently the two cells are contained by equal and similar faces, equal in number, and hence are equal solids; their bases are equal as well. [1.34, 1.29, 1.4, D11.10]

**Step 4.** Each of the m cells constituting U has intercepted edge equal to AE, so Step 3 makes it equal to S and its base equal to b. Likewise, each of the n cells constituting V is equal to T and its base equal to c. Adding these equal pieces gives
u = m·b,  U = m·S,  v = n·c,  V = n·T.
Thus u and U are equimultiples of b and S, while v and V are equimultiples of c and T. [CN2, D5.2]

**Step 5.** Both U and V begin at F₀ and have the same four lateral boundaries. If X lies beyond Y, then V is a proper part of U, and v is a proper part of u; hence U > V and u > v. If X = Y, the solids coincide and their bases coincide. If X lies before Y, the proper containments are reversed, giving U < V and u < v. Therefore u and v have exactly the same greater-than, equality, or less-than relation as U and V. [CN5]

**Step 6.** Since m and n were arbitrary, the equimultiples m·b and n·c always alike exceed, equal, or fall short of one another as do m·S and n·T. By the definition of equal ratios,
b : c = S : T.
Therefore, as the base is to the base, so is the solid to the solid. [D5.5]

**USED:** 1.29, 1.3, 1.31, 1.34, 1.4, 11.10, 11.15, 11.16, 11.24, CN2, CN5, D11.10, D5.2, D5.5, P2
**Human refs (from References field):** 11.24, D5.5
**Jaccard:** 0.133 — AI adds ['1.29', '1.3', '1.31', '1.34', '1.4', '11.10', '11.15', '11.16', 'CN2', 'CN5', 'D11.10', 'D5.2', 'P2']

## Proposition 11.26
**Statement:** On a given straight line, and at a given point on it, to construct a solid angle equal to a given solid angle.

**Step 1.** Let A be the given point on the given straight line, and select one ray of that line as the prescribed edge. Let O be the vertex of the given solid angle. Choose two noncollinear bounding rays OB and OC, and denote its remaining bounding rays by OD_i, retaining their given face incidences. Choose points B, C, and D_i on these rays. The rays OB and OC determine a plane π. We shall copy this planar configuration first and then copy perpendicular heights; this anchors the construction directly to the prescribed edge. [D11.11, 11.2]

**Step 2.** Choose a plane Π through the given straight line. In Π construct an angle B′AC′ equal to BOC, with AB′ on the prescribed ray. Take AB′ = OB and AC′ = OC, producing the rays as necessary before cutting off the lengths. Thus the base triangles have two sides and their included angle respectively equal. Fix corresponding sides of π and Π consistently with a superposition of these base triangles. [1.23, 1.3, P2]

**Step 3.** For every D_i outside π, draw D_iH_i perpendicular to π, and record on which side of π the point D_i lies. For a D_i already in π, put H_i = D_i. Thus each remaining endpoint is specified by its foot in π and, when elevated, its perpendicular height and side. [11.11]

**Step 4.** Copy every H_i to a point K_i in Π as follows. If H_i = O, put K_i = A. If H_i lies on the straight line OB, lay off AK_i = OH_i on the corresponding ray of AB′. Otherwise construct ∠B′AK_i = ∠BOH_i, placing K_i in the half-plane relative to AB′ corresponding to the half-plane containing H_i relative to OB, and take AK_i = OH_i. These constructions preserve the complete angular position and distance of each foot relative to the base vertex and base ray, whether a foot lies inside or outside the original face angle. [1.23, 1.3, P2]

**Step 5.** Whenever D_i is outside π, erect at K_i a perpendicular to Π. On the side corresponding to that containing D_i, take a point D_i′ such that K_iD_i′ = H_iD_i. When D_i lies in π, simply put D_i′ = K_i. Join A to every D_i′. Together with AB′ and AC′, these are the constructed bounding rays; take their plane faces with the original incidences. [11.12, 1.3, P2, P1, 11.2]

**Step 6.** Verify the construction by superposition. By 1.4, triangles AB′C′ and OBC are equal: this is the immediately applicable congruence criterion, since their two sides and included angles were copied. Superpose these base triangles, taking the selected sides of their planes to correspond. Each K_i then coincides with H_i, because its distance, angular position, and half-plane were copied. The perpendicular erected at K_i consequently coincides with the perpendicular through H_i on the corresponding side: perpendicularity means making right angles with every line through the foot in the plane, and there cannot be two such perpendiculars on the same side. Their equal cut-off lengths therefore make D_i′ coincide with D_i. For endpoints originally in π, coincidence already follows from the copying of their feet. [1.4, D11.3, 11.13, CN4]

**Step 7.** Consequently all corresponding bounding rays and faces coincide under this superposition, so the constructed solid angle equals the given solid angle. At least one original bounding ray is outside π, and its copied endpoint has positive perpendicular height above or below Π; hence the constructed rays genuinely form a solid angle. Its vertex is A and one of its edges is the prescribed ray of the given straight line. The required solid angle has therefore been constructed. [CN4, D11.11]

**USED:** 1.23, 1.3, 1.4, 11.11, 11.12, 11.13, 11.2, CN4, D11.11, D11.3, P1, P2
**Human refs (from References field):** 1.23, 1.4, 1.8, 11.11, 11.12, D11.3
**Jaccard:** 0.385 — AI adds ['1.3', '11.13', '11.2', 'CN4', 'D11.11', 'P1', 'P2']; Human adds ['1.8']

## Proposition 11.27
**Statement:** On a given straight line to describe a parallelepipedal solid similar and similarly situated to a given parallelepipedal solid.

**Step 1.** Let AB be the given straight line, and let OU, OV, OW be the three edges meeting at a vertex O of the given parallelepipedal solid. We take the direct route of copying this solid angle and proportioning its edges. At A, with AB corresponding to OU, construct a solid angle equal to that at O. Let its other two edges lie on rays AX and AY, corresponding respectively to OV and OW. Thus ∠BAX = ∠UOV, ∠BAY = ∠UOW, and ∠XAY = ∠VOW, with the corresponding faces in the copied arrangement. [11.26]

**Step 2.** Construct fourth proportionals and mark X and Y on these rays so that
OU : AB = OV : AX,
and
OU : AB = OW : AY.
The fourth proportionals exist by 6.12; extend the rays as necessary and cut off the required lengths. [6.12, P2, 1.3]

**Step 3.** Complete a parallelepiped on the three edges AB, AX, AY as follows. Through B draw a plane parallel to AXY, through X a plane parallel to ABY, and through Y a plane parallel to ABX. Each such plane is constructed by drawing through the specified point two intersecting straight lines parallel to two intersecting lines in the corresponding original plane. The resulting planes are parallel by 11.15. Together with ABX, ABY, and AXY, they bound the required constructed parallelepiped. Its faces, like those of the given solid, are parallelograms. [1.31, 11.15, 11.24]

**Step 4.** The proportions in Step 2 give OV : AX = OW : AY, since both ratios equal OU : AB. Alternating these proportions gives
OU : OV = AB : AX,
OU : OW = AB : AY,
and
OV : OW = AX : AY.
Thus every pair of edges at A is proportional to its corresponding pair at O. [5.11, 5.16]

**Step 5.** Consider the faces on AB, AX and on OU, OV. Their included angles are equal by Step 1, and their adjacent sides are proportional by Step 4. In each parallelogram opposite angles and sides are equal, while adjacent angles are supplementary. Hence these two faces are equiangular and have their corresponding sides proportional, so they are similar. The same argument applies to the faces on AB, AY and OU, OW, and to those on AX, AY and OV, OW. Therefore the three faces meeting at A are respectively similar to the three faces meeting at O. [1.29, 1.34, D6.1]

**Step 6.** In either solid, corresponding sides of opposite faces are equal and parallel: they are opposite sides of the intervening parallelogram faces. Moreover, the corresponding angles of these opposite faces are equal, since their sides are respectively parallel. Each opposite face therefore has the same corresponding side lengths and angles as its partner. It follows from Step 5 that the remaining three face-pairs of the two solids also have equal corresponding angles and proportional corresponding sides, and hence are similar. [1.34, 11.10, D6.1]

**Step 7.** The constructed and given solids are thus contained by six respectively similar faces. They are therefore similar solid figures. Their corresponding edges and faces have the arrangement fixed by the copied solid angle, so the constructed solid is also similarly situated to the given one, with AB corresponding to OU. Thus on the given straight line AB a parallelepipedal solid similar and similarly situated to the given parallelepipedal solid has been described. [D11.9, 11.26]

**USED:** 1.29, 1.3, 1.31, 1.34, 11.10, 11.15, 11.24, 11.26, 5.11, 5.16, 6.12, D11.9, D6.1, P2
**Human refs (from References field):** 5.22, 6.12, D11.9
**Jaccard:** 0.133 — AI adds ['1.29', '1.3', '1.31', '1.34', '11.10', '11.15', '11.24', '11.26', '5.11', '5.16', 'D6.1', 'P2']; Human adds ['5.22']

## Proposition 11.28
**Statement:** If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid will be bisected by the plane.

**Step 1.** Let the opposite faces of the parallelepiped be ABCD and EFGH, with AE, BF, CG, DH joining corresponding vertices. Label the vertices so that the cutting plane passes through the diagonals AC and EG; its section is ACGE. By XI.24, the original faces are parallelograms, and opposite faces are equal. We take the direct route of comparing the bounding faces of the two parts, using the criterion of Definition XI.10. [11.24, D11.10]

**Step 2.** In the parallelogram ABCD, AB = CD, BC = DA, and angle ABC equals angle CDA. These are precisely the two sides and included angle required by I.4, so triangles ABC and CDA are equal, with all corresponding sides and angles equal. They are therefore also similar. The same argument in EFGH shows that triangles EFG and GHE are equal and similar. Thus the triangular faces of the two parts are equal and similar in pairs. [1.34, 1.4, D6.1]

**Step 3.** The face ABFE is opposite DCGH, and BCGF is opposite ADHE; hence these pairs are equal by XI.24. They are also similar: in the indicated vertex orders, their corresponding sides are equal by I.34 applied to the original parallelogram faces, and the rays forming corresponding angles are respectively parallel. Those angles are consequently equal by XI.10. Equal corresponding sides are proportional, so Definition VI.1 gives the required similarity. [11.24, 1.34, 11.10, D6.1]

**Step 4.** One of the two parts is bounded by the five faces ABC, EFG, ABFE, BCGF, and ACGE. The other is bounded by CDA, GHE, DCGH, ADHE, and ACGE. The first four faces in these lists are respectively equal and similar by Steps 2–3. The fifth is the very same section ACGE, hence is equal and similar to itself. Thus the two parts are contained by similar plane figures equal in both multitude and magnitude. [CN4, D6.1]

**Step 5.** By Definition XI.10, the two solid parts are equal and similar, and in particular equal. Since together they constitute the original parallelepiped, the cutting plane bisects that solid. Therefore a plane through the diagonals of opposite faces of a parallelepiped bisects it. [D11.10]

**USED:** 1.34, 1.4, 11.10, 11.24, CN4, D11.10, D6.1
**Human refs (from References field):** 1.34, D11.10
**Jaccard:** 0.286 — AI adds ['1.4', '11.10', '11.24', 'CN4', 'D6.1']

## Proposition 11.29
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

**Step 1.** Let the two parallelepipeds be P = ABCD–EFGH and Q = ABCD–IJKL, with standing edges AE, BF, CG, DH and AI, BJ, CK, DL, respectively. By hypothesis, E, F, I, J lie on one straight line, and H, G, L, K on the parallel straight line containing the opposite upper edges. Their faces are parallelograms (11.24). If the corresponding upper vertices coincide, the solids coincide and are equal (CN4). Otherwise, interchange P and Q if necessary so that, in the direction from E to F, E precedes I. Correspondingly, F precedes J, H precedes L, and G precedes K. We use subtraction of equal end-pieces; this works whether the upper faces overlap or not.

**Step 2.** Opposite sides of the parallelogram faces give EF = IJ = AB and HG = LK = DC (1.34). Subtracting the equal segments EF and IJ from the common segment EJ gives FJ = EI. Similarly, subtracting HG and LK from HK gives GK = HL (CN3).

**Step 3.** Compare triangles AEI and BFJ. We have AE = BF by 1.34, EI = FJ by Step 2, and ∠AEI = ∠BFJ because AE is parallel to BF and EI and FJ run in the same direction along their common straight line (1.29). Thus these triangles are equal, with their remaining corresponding sides and angles equal, by 1.4. In exactly the same way, DH = CG, HL = GK, and ∠DHL = ∠CGK show that triangles DHL and CGK are equal with equal corresponding sides and angles (1.34, 1.29, 1.4). SAS is the direct choice here because the parallelogram faces already supply the required sides and included angles.

**Step 4.** Form the triangular end-pieces U, with triangular faces AEI and DHL, and V, with triangular faces BFJ and CGK. Their remaining faces correspond as follows:
ADHE ↔ BCGF,
ADLI ↔ BCKJ,
EHLI ↔ FGKJ.
The first two pairs are opposite faces of P and Q, respectively, so they are equal parallelograms (11.24). Their corresponding sides are equal by 1.34, and their corresponding angles are equal because their sides are respectively parallel (11.10). Consequently, each pair is also similar (D6.1).

**Step 5.** For the last pair, EH and IL are parallel, since both are parallel to AD; likewise FG and JK are parallel (11.9). Also EI is parallel to HL, and FJ to GK. Thus EHLI and FGKJ are parallelograms. Now EH = FG by 1.34, EI = FJ by Step 2, and ∠HEI = ∠GFJ by 1.29. Splitting each parallelogram along the diagonal opposite this included angle gives two pairs of equal triangles by 1.4 and 1.34. Hence the parallelograms are equal; their corresponding angles agree and their corresponding sides are equal, so they are similar as well (1.29, D6.1). Together with Step 3, all five faces of U therefore correspond to equal and similar faces of V. Hence U and V are equal solids (D11.10).

**Step 6.** Take the larger solid R whose end faces are ABJE and DCKH and whose other faces are ABCD, ADHE, BCKJ, and EJKH. Cutting R by the face BCGF separates it into P and V. Cutting it instead by the face ADLI separates it into Q and U. These are valid dissections regardless of whether I lies before or after F: both I and F lie on EJ, and the corresponding back vertices lie on HK. Since U = V, subtracting these equal end-pieces from the same solid R leaves equal remainders (CN3). Therefore P = Q.

Thus parallelepipedal solids on the same base and of the same height, whose standing sides terminate on the same straight lines, are equal to one another.

**USED:** 1.29, 1.34, 1.4, 11.10, 11.24, 11.9, CN3, CN4, D11.10, D6.1
**Human refs (from References field):** 1.34, 1.36, 1.4, 1.8
**Jaccard:** 0.167 — AI adds ['1.29', '11.10', '11.24', '11.9', 'CN3', 'CN4', 'D11.10', 'D6.1']; Human adds ['1.36', '1.8']

## Proposition 11.30
**Statement:** Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal to one another.

**Step 1.** Let the two solids have common base ABCD and respective opposite faces EFGH and KLMN, with the vertices in each list corresponding to A, B, C, D. Their faces are parallelograms. Since their heights are equal, their upper faces lie in one plane π parallel to the base plane. We use the direct route through XI.29: insert an intermediate solid for which the required alignment holds with each given solid in turn. [11.24, D6.4, 11.29]

**Step 2.** The lateral parallelograms show that EF, HG, KL, MN are parallel to AB, while EH, FG, KN, LM are parallel to AD. Hence, in π, these constitute two families of parallel lines, with the directions of the two adjacent sides of the base. [11.24, 11.9]

**Step 3.** Produce the upper edges as necessary, and define
R = EF ∩ KN,
S = EF ∩ LM,
T = HG ∩ LM,
U = HG ∩ KN.
These intersections exist because the two families have distinct directions. Thus RSTU is a parallelogram. The construction uses complete straight lines and requires no overlap of the given upper faces. [P2, D1.23]

**Step 4.** The parallelogram KLSR gives RS = KL, and the parallelogram ERUH gives RU = EH; if the compared segments coincide, the corresponding equality is immediate. The original lateral parallelograms give KL = AB and EH = AD. Consequently RS = AB and RU = AD. Opposite-side equalities in RSTU and ABCD then also give ST = BC and TU = CD. Thus the corresponding sides of RSTU and ABCD are equal and parallel, in the same directions. [1.34]

**Step 5.** Join AR, BS, CT, DU. Since corresponding base and upper edges are equal and parallel in the same directions, their joining edges are equal and parallel. Therefore AB SR, BC TS, CD UT, and DA RU are parallelograms. Each pair of opposite lateral planes contains two intersecting lines respectively parallel to two intersecting lines in the other plane; hence those planes are parallel. Together with the parallel planes of ABCD and RSTU, they bound a parallelepipedal solid W. Its base is ABCD and its upper face lies in π, so its height is the given height. [P1, 1.33, 11.15, D6.4]

**Step 6.** Compare the first given solid with W. Their bases and heights are the same. Moreover, E, F, R, S lie on the straight line EF, and H, G, U, T lie on the straight line HG. Thus the extremities of their standing sides have exactly the common-line alignment required by XI.29. The first solid therefore equals W. [11.29]

**Step 7.** Compare the second given solid with W, now using the other base-edge direction. The points K, N, R, U lie on KN, and L, M, S, T lie on LM. Again the bases and heights are the same, and the required alignment holds. The second solid therefore equals W. [11.29]

**Step 8.** Both given solids equal W; hence they equal one another. Therefore parallelepipedal solids on the same base and of the same height are equal in the stated case. [CN1]

**USED:** 1.33, 1.34, 11.15, 11.24, 11.29, 11.9, CN1, D1.23, D6.4, P1, P2
**Human refs (from References field):** 11.29
**Jaccard:** 0.091 — AI adds ['1.33', '1.34', '11.15', '11.24', '11.9', 'CN1', 'D1.23', 'D6.4', 'P1', 'P2']

## Proposition 11.31
**Statement:** Parallelepipedal solids which are on equal bases and of the same height are equal to one another.

**Step 1.** Let the given parallelepipedal solids be S and T, with equal bases B and C and common height h. On each base construct a right parallelepipedal solid of height h: erect a perpendicular, take on it a length h, and complete the faces by parallels (11.12, 1.3, 1.31). The remaining upright edges are perpendicular to the base, and the opposite faces are parallel (11.8, 11.15). Denote these right solids by S₀ and T₀. Then S = S₀ and T = T₀, by 11.29 when the upper endpoints have the alignment specified there, and by 11.30 otherwise. We use 11.29 first wherever its more specific hypothesis holds; 11.30 supplies precisely the remaining case. A solid already right is left unchanged.

**Step 2.** We next replace each parallelogram base by a rectangle without changing its area or the solid. For either right solid, write its base as ABCD and its opposite face as A′B′C′D′. Draw AE perpendicular to AB, meeting the line DC at E; through B draw BF parallel to AE, meeting DC at F (1.11, 1.31). Thus ABFE is a rectangle (1.29), and it equals ABCD because the two parallelograms are on AB and between the same parallels (1.35).

Erect over ABFE the right solid of height h, using the construction of Step 1. Its upper vertices above E and F, denoted E′ and F′, lie on the line D′C′. Regard the old and new solids as standing on their common face ABB′A′. Their opposite faces lie in the same plane through DC and D′C′, so their heights from that common face are equal. Moreover, the endpoints of their standing edges lie on the same two straight lines DC and D′C′. Therefore the solids are equal by 11.29. If the original base is already rectangular, no replacement is needed.

Applying this construction to S₀ and T₀ gives rectangular solids P and Q, with rectangular bases U and V. Consequently S = P, T = Q, and U = V, by the preceding equalities and CN1.

**Step 3.** Let the adjacent sides of U have lengths a, b, and those of V have lengths c, d. Both P and Q have height h. Construct a rectangular solid K whose base W has adjacent sides c, b and whose upright edges have length h, using the perpendicular-and-parallel construction of Step 1.

Place a congruent copy of P against K along a face with edge lengths b and h, on the opposite side of that face. Their union is a rectangular parallelepipedal solid, and their common face cuts it by a plane parallel to two opposite faces. Likewise, place a congruent copy of Q against K along a face with edge lengths c and h. Their union is another rectangular parallelepipedal solid with the same kind of cut. These placements use matching rectangular faces and parallel edges (1.31); the copies and their bases equal the originals by coincidence (CN4).

**Step 4.** Apply 11.25 to the first compound solid, cut into P and K, taking U and W as their bases. It gives
P : K = U : W.
Apply 11.25 to the second compound solid, cut into Q and K. It gives
Q : K = V : W.
Thus each application concerns the two parts of a single parallelepiped cut by a plane parallel to its opposite faces, exactly as required by 11.25.

**Step 5.** Since U = V, we have U : W = V : W by 5.7. Combining this with the ratios in Step 4 gives P : K = Q : K by 5.11. Hence P = Q by 5.9. Finally, S = P and T = Q, so S = T by CN1. Therefore parallelepipedal solids on equal bases and of the same height are equal to one another.

**USED:** 1.11, 1.29, 1.3, 1.31, 1.35, 11.12, 11.15, 11.25, 11.29, 11.30, 11.8, 5.11, 5.7, 5.9, CN1, CN4
**Human refs (from References field):** 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, D11.10
**Jaccard:** 0.368 — AI adds ['1.11', '1.29', '1.3', '1.31', '11.12', '11.15', '11.8', 'CN1', 'CN4']; Human adds ['1.23', '11.24', 'D11.10']

## Proposition 11.32
**Statement:** Parallelepipedal solids which are of the same height are to one another as their bases.

**Step 1.** Let S and T be parallelepipedal solids of the same height h, with bases B and C respectively. Their bases are parallelograms (11.24). A diagonal bisects each base; let b and c be triangular halves of B and C respectively (1.34).

**Step 2.** Choose a segment of length d. By applying 1.44 in a right angle, construct four rectangles consecutively in one strip of width d: the first two each equal to b, and the last two each equal to c. Each successive application is made to the outer side of the preceding rectangle, so all four rectangles have the same width and have disjoint interiors. Let R be the rectangle formed by the first pair and Q that formed by the second pair. Then R and Q share a complete side, and their union is a rectangle. Moreover, R = B and Q = C, since equals added to equals give equal wholes (CN2). We use the prescribed-side construction of 1.44 because the common width permits the auxiliary solids to be obtained by one parallel cut.

**Step 3.** On the combined rectangle R ∪ Q construct a right parallelepiped W of height h: erect a perpendicular to its plane, mark off a length h upon it, and complete the construction by parallels (11.12, 1.3, 1.31). The corresponding face planes are parallel by 11.15. Through the common side of R and Q construct the plane parallel to the corresponding end faces, using parallels as in 1.31 and 11.15. This plane divides W into parallelepipeds U and V on bases R and Q. Both have height h, since they lie between the same base and opposite planes of W.

**Step 4.** Since W has been cut by a plane parallel to a pair of its opposite faces, the two resulting solids are in the ratio of their bases (11.25). Thus
U : V = R : Q.

**Step 5.** The solids S and U have equal bases B and R and the same height h; hence S = U. Likewise, T = V, because their bases C and Q are equal and their heights are the same (11.31).

**Step 6.** Substituting these equal magnitudes in the ratios (5.7), and combining equal ratios (5.11), gives
S : T = U : V = R : Q = B : C.
Therefore parallelepipedal solids which are of the same height are to one another as their bases.

**USED:** 1.3, 1.31, 1.34, 1.44, 11.12, 11.15, 11.24, 11.25, 11.31, 5.11, 5.7, CN2
**Human refs (from References field):** 1.45, 11.25, 11.31
**Jaccard:** 0.154 — AI adds ['1.3', '1.31', '1.34', '1.44', '11.12', '11.15', '11.24', '5.11', '5.7', 'CN2']; Human adds ['1.45']

## Proposition 11.33
**Statement:** Similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides.

**Step 1.** Let S and T be similar parallelepipedal solids. Let AB, AC, AD be the three edges issuing from a vertex A of S, and let ab, ac, ad be their corresponding edges at a vertex a of T. Since corresponding faces are similar, their corresponding angles are equal and
AB:ab = AC:ac = AD:ad.
We use successive changes of one edge, so that the equal-height theorem gives three equal successive ratios directly. [D11.9, D6.1]

**Step 2.** On the rays AB, AC, AD take points E, F, G such that AE = ab, AF = ac, AG = ad, producing the lines when necessary. Complete parallelepipeds by drawing parallels in the three edge directions; the resulting opposite face planes are parallel. Write Π(X,Y,Z) for the parallelepiped whose three edges at A are AX, AY, AZ, and put
S₀ = Π(B,C,D) = S,
S₁ = Π(E,C,D),
S₂ = Π(E,F,D),
S₃ = Π(E,F,G).
Also write [X,Y] for the parallelogram whose adjacent sides at A are AX and AY. [P2, 1.3, 1.31, 11.15]

**Step 3.** The three faces of S₃ incident with A have their adjacent sides respectively equal to those of the corresponding faces of T, and their included angles are equal by Step 1. Applying the side-angle-side theorem to the triangles into which diagonals divide these parallelograms shows that these corresponding faces are equal and similar. The opposite faces of each parallelepiped are equal to their corresponding incident faces. Thus S₃ and T are contained by equal and similar corresponding faces, and consequently S₃ = T. [1.4, 1.34, 11.24, D11.10]

**Step 4.** Regard [B,C] and [E,C] as the bases of S₀ and S₁. Both solids lie between the plane ABC and the same parallel plane through D, so they have the same height. Hence their ratio is the ratio of these bases. The two base parallelograms have the same altitude above the line AB, and therefore their ratio is AB:AE. Thus
S₀:S₁ = [B,C]:[E,C] = AB:AE.
[11.32, 6.1]

**Step 5.** Regard [C,D] and [F,D] as the bases of S₁ and S₂. Both solids lie between the plane ACD and the same parallel plane through E, so they have the same height. Their base parallelograms have the same altitude above the line AC. Consequently
S₁:S₂ = [C,D]:[F,D] = AC:AF.
[11.32, 6.1]

**Step 6.** Regard [D,E] and [G,E] as the bases of S₂ and S₃. Both solids lie between the plane ADE and the same parallel plane through F, so they have the same height. Their base parallelograms have the same altitude above the line AD. Consequently
S₂:S₃ = [D,E]:[G,E] = AD:AG.
[11.32, 6.1]

**Step 7.** Since AE = ab, AF = ac, and AG = ad, the proportions in Step 1 give
AB:AE = AC:AF = AD:AG = AB:ab.
Combining this with Steps 4–6 yields
S₀:S₁ = S₁:S₂ = S₂:S₃ = AB:ab.
Thus S₀, S₁, S₂, S₃ are four continuously proportional magnitudes. [5.7, 5.11]

**Step 8.** By the definition of triplicate ratio, S₀:S₃ is the triplicate ratio of S₀:S₁, hence of AB:ab. Since S₀ = S and S₃ = T, it follows that S:T is the triplicate ratio of AB:ab. The edge AB and its corresponding edge ab were arbitrary. Therefore similar parallelepipedal solids are to one another in the triplicate ratio of their corresponding sides. [D5.10, 5.7]

**USED:** 1.3, 1.31, 1.34, 1.4, 11.15, 11.24, 11.32, 5.11, 5.7, 6.1, D11.10, D11.9, D5.10, D6.1, P2
**Human refs (from References field):** 11.24, 11.32, 6.1, D11.10, D5.10
**Jaccard:** 0.333 — AI adds ['1.3', '1.31', '1.34', '1.4', '11.15', '5.11', '5.7', 'D11.9', 'D6.1', 'P2']

## Proposition 11.34
**Statement:** In equal parallelepipedal solids the bases are reciprocally proportional to the heights; and those parallelepipedal solids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let S and T be the given parallelepipedal solids, with bases of magnitudes α and β and respective heights h and k. Choose the following route: replace S by a right parallelepiped, then compare heights by using lateral faces as bases. Let ABCD be the base of S. Erect a perpendicular at A to its plane, and mark lengths AE = h and AF = k on the same side. Complete parallelepipeds U and V on ABCD with standing edges AE and AF, respectively, by drawing parallels. These constructions use 11.12, 1.3, and 1.31; the corresponding opposite face planes are parallel by 11.15. All standing edges are perpendicular to ABCD by 11.8, so U and V have heights h and k.

**Step 2.** The solids U and S have the same base and the same height; hence U = S by 11.31. We use this direct equality theorem here because no general ratio comparison is needed.

**Step 3.** The solids V and T have the same height k. Consequently, by 11.32,
V : T = α : β.

**Step 4.** Let L_h and L_k be the lateral parallelogrammic faces of U and V on AB. Take their standing edges AE and AF as their respective bases. Their common height is AB: the standing edges through A and B are perpendicular to the base plane, and therefore perpendicular to AB (D11.3). Thus, by 6.1,
L_k : L_h = AF : AE = k : h.
The planes containing L_h and L_k coincide, as do the planes containing their opposite lateral faces on CD. Therefore U and V, regarded as standing on L_h and L_k, have the same height—the perpendicular distance between this fixed pair of planes. Applying 11.32 in this orientation gives
V : U = L_k : L_h,
and hence, by 5.11,
V : U = k : h.

**Step 5.** Suppose first that S = T. Since U = S, we have U = T (CN1). Therefore V : T = V : U by 5.7. Combining this equality of ratios with Steps 3 and 4, using 5.11, yields
α : β = k : h.
Thus the bases of equal parallelepipedal solids are reciprocally proportional to their heights.

**Step 6.** Conversely, suppose that the bases are reciprocally proportional to the heights, so that α : β = k : h. Steps 3 and 4 then give V : T = V : U by 5.11. Magnitudes to which the same magnitude has the same ratio are equal, so T = U by 5.9. Since U = S, it follows that S = T (CN1). Therefore parallelepipedal solids whose bases are reciprocally proportional to their heights are equal. Both assertions are proved.

**USED:** 1.3, 1.31, 11.12, 11.15, 11.31, 11.32, 11.8, 5.11, 5.7, 5.9, 6.1, CN1, D11.3
**Human refs (from References field):** 11.25, 11.29, 11.30, 11.31, 11.32, 5.7, 5.9, 6.1
**Jaccard:** 0.312 — AI adds ['1.3', '1.31', '11.12', '11.15', '11.8', '5.11', 'CN1', 'D11.3']; Human adds ['11.25', '11.29', '11.30']

## Proposition 11.35
**Statement:** If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

**Step 1.** Let the equal plane angles be BAC and EDF, and let AX and DY be the elevated rays, with ∠BAX = ∠EDY and ∠CAX = ∠FDY. From the chosen points X and Y let XH and YK be perpendicular to the respective planes. Join AH and DK as in the statement. We must prove ∠XAH = ∠YDK. Perpendicularity to a plane gives perpendicularity to every straight line in that plane through the foot; and every triangle used below lies in a plane. [D11.3, 11.2]

**Step 2.** We may first make AX = DY without changing either angle to be proved equal. Indeed, if these lengths are unequal, shorten the longer elevated segment to equal the shorter. Through its new endpoint draw, in the triangle formed by the original elevated segment and its perpendicular, a parallel to that perpendicular. The parallel cuts the vertex-to-foot segment proportionally, so its intersection lies on the same ray from the vertex; moreover, it is perpendicular to the original plane. Thus neither ray forming the angle at that vertex changes. Relabel the resulting points X, Y and their feet H, K, so that AX = DY. [1.3, 1.31, 6.2, 11.8]

**Step 3.** Choose a transversal through H, not through A, meeting the two complete side-lines of the first angle at B and C, with H on the segment BC. This can be done across the angular sector containing H, using a parallel to a segment joining its bounding rays; if H lies on a side-line, take H itself as the corresponding endpoint. Where necessary, use the opposite of an original side-ray, and reverse the corresponding side-ray at D also. The corresponding angle equalities remain true: reversing a ray replaces the relevant angles by equal supplements. On the corresponding rays at D choose E and F with DE = AB and DF = AC. Join the auxiliary segments BC, EF, BX, CX, EY and FY. [P1, P2, 1.31, 1.3, 1.13, CN3]

**Step 4.** Apply the side–angle–side theorem to triangles ABC and DEF, to triangles ABX and DEY, and to triangles ACX and DFY. This is the direct choice because the two sides and their included angle are already equal in each pair. Consequently,
BC = EF, BX = EY, and CX = FY,
and all corresponding angles in each of these pairs are equal. [1.4]

**Step 5.** The three sides of triangle XBC now equal the corresponding three sides of triangle YEF. Hence their corresponding angles are equal, in particular ∠XBC = ∠YEF and ∠XCB = ∠YFE. Choose L on EF so that EL = BH. Such a point exists because H lies on BC and BC = EF; take L = E or L = F when H = B or H = C respectively. [1.8, 1.3]

**Step 6.** Suppose first that H is interior to BC. In triangles ABH and DEL, we have AB = DE, BH = EL, and ∠ABH = ∠DEL by Step 4. Thus AH = DL. Likewise, triangles XBH and YEL have XB = YE, BH = EL, and ∠XBH = ∠YEL by Step 5. Therefore XH = YL and ∠XHB = ∠YLE. Since XH is perpendicular to the first plane, ∠XHB is right; hence YL is perpendicular to EF. If H is an endpoint of BC, the same conclusions follow directly from Steps 4 and 5: the corresponding endpoint L satisfies AH = DL and XH = YL, while the equal corresponding angles of triangles XBC and YEF make YL perpendicular to EF. Thus in every case,
AH = DL, XH = YL, and YL ⟂ EF. [1.4, 1.8, D11.3]

**Step 7.** Triangles AXH and DYL have their three corresponding sides equal: AX = DY by Step 2, and AH = DL and XH = YL by Step 6. Therefore ∠YLD = ∠XHA and ∠YDL = ∠XAH. The former angle is right, since XH is perpendicular to the first plane. Hence YL is also perpendicular to DL. [1.8, D11.3]

**Step 8.** The straight lines EF and DL intersect at L and lie in the second plane. Since YL is perpendicular to both, it is perpendicular to that plane. [11.4]

**Step 9.** Both YL and the given YK are perpendicular to the second plane. If L and K were distinct, triangle YLK would have right angles at both L and K, contrary to the theorem that any two angles of a triangle are together less than two right angles. Therefore L = K. Step 7 now gives ∠XAH = ∠YDK. The shortening in Step 2 left the original vertex-rays unchanged, so this equality holds for the originally chosen, arbitrary elevated points. Thus the joined straight lines contain equal angles with the elevated straight lines, as required. [D11.3, 1.17, CN1]

**USED:** 1.13, 1.17, 1.3, 1.31, 1.4, 1.8, 11.2, 11.4, 11.8, 6.2, CN1, CN3, D11.3, P1, P2
**Human refs (from References field):** 1.26, 1.4, 1.47, 1.48, 1.8, 11.8
**Jaccard:** 0.167 — AI adds ['1.13', '1.17', '1.3', '1.31', '11.2', '11.4', '6.2', 'CN1', 'CN3', 'D11.3', 'P1', 'P2']; Human adds ['1.26', '1.47', '1.48']

## Proposition 11.36
**Statement:** If three straight lines be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

**Step 1.** Let the three proportional straight lines have lengths a, b, c, so that a:b = b:c. Let the given parallelepiped S have concurrent edges OA = a, OB = b, OC = c. Choose the face generated by OA and OC as its base: taking the extremes as base edges leaves the mean as the lateral edge and gives a direct equal-base, equal-height proof. On the rays OA and OC take D and E with OD = OE = b, and complete a parallelepiped T with concurrent edges OD, OB, OE by drawing parallels. These constructions are permitted by P2, P3 and 1.31; the resulting opposite face planes are parallel by 11.15.

**Step 2.** The three edges OD, OB, OE are equal. Since opposite sides of each parallelogram face are equal, all edges of T equal b (1.34). Moreover, its generating rays are exactly those of S, and all remaining edges have the corresponding parallel directions. Thus corresponding face angles are equal, by 1.29 when coplanar and by 11.10 when in different planes. Consequently T is equilateral and equiangular with S.

**Step 3.** Let F be the parallelogram base of S generated by OA and OC, and G the parallelogram base of T generated by OD and OE. Their angles at O are identical, so the parallelograms are equiangular. Furthermore,
OA:OD = a:b = b:c = OE:OC.
Their sides about the equal angles are therefore reciprocally proportional. Hence F and G are equal by 6.14.

**Step 4.** Both bases lie in the plane AOC. Their opposite bases lie in the same plane through B generated by parallels to OA and OC; this plane is parallel to AOC by 11.15. Thus S and T have the same height. Being on equal bases and of the same height, they are equal by 11.31. Therefore the parallelepiped formed from the three proportional straight lines equals the equilateral parallelepiped on the mean which is equiangular with it, as required.

**USED:** 1.29, 1.31, 1.34, 11.10, 11.15, 11.31, 6.14, P2, P3
**Human refs (from References field):** 11.31, 11.35, 6.14
**Jaccard:** 0.200 — AI adds ['1.29', '1.31', '1.34', '11.10', '11.15', 'P2', 'P3']; Human adds ['11.35']

## Proposition 11.37
**Statement:** If four straight lines be proportional, the parallelepipedal solids on them which are similar and similarly described will also be proportional; and, if the parallelepipedal solids on them which are similar and similarly described be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let the four straight lines be a, b, c, d, and let P, Q, R, S be the similar and similarly described parallelepipedal solids on them, respectively. We use the triplicate-ratio theorem (11.33), since it directly relates these solids to their corresponding edges. For the converse, we shall construct a fourth proportional rather than assume that equality of triplicate ratios implies equality of the original ratios.

**Step 2.** Suppose a:b = c:d. By repeated application of 6.12, construct straight lines u, v, w, x such that

a:b = b:u = u:v, and c:d = d:w = w:x.

The corresponding successive ratios of these two chains are equal (5.11); hence, ex aequali, a:v = c:x (5.22). By D5.10 these endpoint ratios are the triplicate ratios of a:b and c:d, respectively. Therefore 11.33 gives P:Q = a:v and R:S = c:x. It follows that P:Q = R:S (5.11). This proves the forward implication.

**Step 3.** Conversely, suppose P:Q = R:S. Construct a straight line e such that a:e = c:d; this is the fourth proportional to c, d, a (6.12). On e construct a parallelepipedal solid T similar and similarly described to the given solids (11.27). Applying the forward implication just proved to a, e, c, d gives P:T = R:S. Consequently P:Q = P:T (5.11), and therefore Q = T (5.9).

**Step 4.** By repeated application of 6.12, construct straight lines h and k such that

b:e = e:h = h:k.

Since Q and T are similar solids on the corresponding edges b and e, their ratio is the triplicate ratio of b:e (11.33). Thus Q:T = b:k by D5.10. Because Q = T, the definition of equal ratios, applied with both multiples equal to one, gives b = k (D5.5).

**Step 5.** The same definition, again with both multiples equal to one, shows that the comparisons within the three equal ratios b:e, e:h, h:k must agree (D5.5). If b were greater than e, we would have b > e > h > k, contradicting b = k. If b were less than e, we would have b < e < h < k, again contradicting b = k. Hence b = e. Equal magnitudes have the same ratio to a fixed magnitude, and a fixed magnitude has the same ratio to equal magnitudes (5.7); therefore a:b = a:e = c:d (5.11). Thus the four straight lines are proportional. Both implications are proved.

**USED:** 11.27, 11.33, 5.11, 5.22, 5.7, 5.9, 6.12, D5.10, D5.5
**Human refs (from References field):** 11.33
**Jaccard:** 0.111 — AI adds ['11.27', '5.11', '5.22', '5.7', '5.9', '6.12', 'D5.10', 'D5.5']

## Proposition 11.38
**Statement:** If the sides of the opposite planes of a cube be bisected, and planes be carried through the points of section, the common section of the planes and the diameter of the cube bisect one another.

**Step 1.** Label the opposite faces of the cube ABCD and EFGH, with corresponding joining edges AE, BF, CG, DH, and let AG be the diameter under consideration. Each face is an equilateral, right-angled quadrilateral; consequently its opposite sides are parallel. [D11.25, D1.22, 1.28]

Let M, N, P, Q be the midpoints of AB, CD, BC, DA respectively, and let M′, N′, P′, Q′ be the corresponding midpoints of EF, GH, FG, HE. Denote the two given cutting planes by Π, through M, N, M′, N′, and Σ, through P, Q, P′, Q′. Join the midpoint pairs and the face diagonals AC and EG. These joins lie in their respective face planes. [P1, 11.7]

**Step 2.** Let MN meet AC at O. Since AB = CD, their halves AM and CN are equal. Here and below, halves of equal segments are equal: otherwise doubling the unequal halves would give unequal wholes. [CN2, CN5]

Because AM is parallel to CN, the alternate angles MAO and NCO are equal, as are AMO and CNO. Thus triangles AMO and CNO have two corresponding angles and the included side equal. Proposition 1.26 gives AO = CO. This angle–side–angle comparison is the direct route: the parallel sides immediately supply precisely its hypotheses. [1.29, 1.26]

Likewise, let PQ meet AC at V. The sides AQ and CP are equal and parallel. Comparing triangles AQV and CPV in the same way gives AV = CV. Hence V and O are the same midpoint of AC; two distinct midpoints would make one of two equal halves a proper part of the other. Therefore both MN and PQ pass through O. [1.29, 1.26, CN2, CN5]

**Step 3.** Apply exactly the same face argument with A, B, C, D replaced by E, F, G, H. It follows that M′N′ and P′Q′ meet at a point O′ on EG, with EO′ = O′G. [1.29, 1.26, CN2, CN5]

Thus O and O′ belong to both cutting planes. The planes are distinct, since their traces MN and PQ on ABCD are distinct. Their common section is therefore the straight line OO′. [11.3]

**Step 4.** In the square faces ABFE and BCGF, AE is parallel and equal to BF, and BF is parallel and equal to CG. Hence AE = CG, and AE is parallel to CG. For the latter inference, 11.9 is the applicable parallelism result because these three edges are not all in one plane. [D1.22, 1.28, CN1, 11.9]

The parallel edges AE and CG determine a plane containing their joins AC, EG, and AG. Joining the corresponding extremities of the equal parallel segments AE and CG gives AC parallel and equal to EG. Thus ACGE is a planar parallelogram. Moreover, OO′ lies in this same plane, since its endpoints lie on the parallel lines AC and EG. [11.7, 1.33]

**Step 5.** Since O and O′ bisect the equal segments AC and EG, AO = GO′. Also, AO is parallel to GO′. [CN2, CN5; Step 4]

Within the parallelogram ACGE, the segment OO′ joins interior points of the opposite sides AC and EG, and meets the diagonal AG at an interior point T. Equivalently, AG and OO′ are the diagonals of the convex quadrilateral AOGO′ in this plane. [11.7; Steps 2–4]

**Step 6.** Because AO is parallel to GO′, the alternate angles OAT and O′GT are equal, and AOT and GO′T are equal. Together with AO = GO′, these equalities give, by comparison of triangles AOT and GO′T,
AT = GT and OT = O′T. [1.29, 1.26]

Therefore the diameter AG and the common section OO′ of the cutting planes bisect one another, as required.

**USED:** 1.26, 1.28, 1.29, 1.33, 11.3, 11.7, 11.9, CN1, CN2, CN5, D1.22, D11.25, P1
**Human refs (from References field):** 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.9
**Jaccard:** 0.250 — AI adds ['1.28', '11.3', '11.7', 'CN1', 'CN2', 'CN5', 'D1.22', 'D11.25', 'P1']; Human adds ['1.14', '1.15', '1.4']

## Proposition 11.39
**Statement:** If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms will be equal.

**Step 1.** Let the first prism P have triangular ends ABC and DEF, with corresponding vertices A,D; B,E; C,F, and let its designated parallelogram base be ABED. Thus CF is its opposite edge. Let the second prism Q have triangular base GHI and opposite end JKL. By hypothesis, ABED is double triangle GHI, and both prisms have the same height h. We use completion to parallelepipeds, preserving these designated heights. [D11.13, D6.4]

**Step 2.** Through B draw a parallel to AC, and through C a parallel to AB, meeting at X; similarly complete DEF to the parallelogram DEYF. These constructions complete P to a parallelepiped S whose base is ABED and whose opposite face is CXYF. Since CX is parallel to AB and CF is parallel to AD, the plane CXYF is parallel to the base plane. It passes through the original opposite edge CF, so S still has height h. The plane BCFE passes through the diagonals BC and EF of the opposite faces ABXC and DEYF. It therefore bisects S, and P is one of its halves. Hence S is double P. [1.31, 11.15, D6.4, 11.28]

**Step 3.** In the same way, complete triangle GHI to parallelogram GHMI and triangle JKL to parallelogram JKNL, obtaining a parallelepiped T. Its base and opposite face remain in the original end-planes of Q, so its height is h. The plane HILK passes through the diagonals HI and KL of these opposite parallelograms and therefore bisects T. One half is precisely Q; hence T is double Q. [1.31, D6.4, 11.28]

**Step 4.** The diagonal HI bisects parallelogram GHMI, so GHMI is double triangle GHI. The given parallelogram ABED is also double that triangle. Consequently the bases GHMI and ABED are equal. Here the diagonal-bisection theorem applies directly to the constructed base. [1.34, CN1]

**Step 5.** The parallelepipeds S and T are on equal bases and have the same height h. Therefore S equals T, by the equal-base, equal-height theorem. [11.31]

**Step 6.** Since S is double P and T is double Q, the ratio S:P equals the ratio T:Q: in each case the whole is twice the corresponding prism. Because S=T, the same magnitude thus has the same ratio to P and to Q. Therefore P=Q. Hence the two given prisms are equal. [D5.5, CN1, 5.9]

**USED:** 1.31, 1.34, 11.15, 11.28, 11.31, 5.9, CN1, D11.13, D5.5, D6.4
**Human refs (from References field):** 1.34, 11.28, 11.31
**Jaccard:** 0.300 — AI adds ['1.31', '11.15', '5.9', 'CN1', 'D11.13', 'D5.5', 'D6.4']
