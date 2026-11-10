# Book 1 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 1.1
**Statement:** On a given finite straight line to construct an equilateral triangle.

**Step 1.** Let AB be the given finite straight line. Describe a circle with centre A and distance AB. [P3]

**Step 2.** Describe a circle with centre B and distance BA. The direct construction seeks its third vertex at an intersection of these two circles. [P3]

**Step 3.** The required existence step is not supplied by the listed foundations: one needs a common point C of the two circumferences outside the straight line AB. P3 permits describing each circle but does not guarantee their intersection. Accordingly, the verification below is conditional on the existence of such a point; either intersection would serve. [Scope of P3]

**Step 4.** Given such a point C, draw the straight lines AC and BC. [P1]

**Step 5.** Since B and C lie on the circle with centre A, AC = AB. Since A and C lie on the circle with centre B, BC = BA. Also BA = AB, since these denote the same segment. Hence AC and BC are both equal to AB and therefore equal to one another. [D1.15, CN4, CN1]

**Step 6.** Because C is outside the straight line AB, the three segments enclose a trilateral figure; because its three sides are equal, it is an equilateral triangle on AB. [D1.19, D1.20] This completes the verification conditional on Step 3. A fully justified construction under the strict stated rules requires an additional circle-intersection principle; presenting the construction as unconditional would conceal that missing premise.

**USED:** CN1, CN4, D1.15, D1.19, D1.20, P1, P3
**Human refs (from References field):** CN1, D1.15, P1, P3
**Jaccard:** 0.571 — AI adds ['CN4', 'D1.19', 'D1.20']

## Proposition 1.2
**Statement:** To place at a given point (as an extremity) a straight line equal to a given straight line.

**Step 1.** Let A be the given point and BC the given straight line, naming its endpoints so that B is distinct from A. Join AB. [P1]

**Step 2.** Construct an equilateral triangle DAB on AB. Then DA = DB. This construction supplies equal parts that can later be subtracted from equal wholes. [1.1, D1.20]

**Step 3.** Describe the circle with centre B passing through C. Produce DB beyond B to meet this circle at G, choosing the intersection for which D, B, G occur in that order. Since BG and BC are radii of this circle, BG = BC. [P3, P2, D1.15]

**Step 4.** Since DB is a proper part of DG, DG > DB; and DB = DA by Step 2, so DG > DA. Describe the circle with centre D passing through G, and produce DA beyond A to meet it at L. Thus D, A, L occur in that order. The outward extensions are chosen so that the required segments are remainders of the larger segments. [CN5, P3, P2]

**Step 5.** The radii DL and DG of the circle with centre D are equal. Subtract the equal parts DA and DB established in Step 2. Because D, A, L and D, B, G respectively occur in those orders, the remainders are AL and BG. Therefore AL = BG. [D1.15, CN3]

**Step 6.** Since AL = BG and BG = BC, it follows that AL = BC. Thus AL is a straight line equal to the given straight line BC and has the given point A as an extremity, as required. [CN1]

**USED:** 1.1, CN1, CN3, CN5, D1.15, D1.20, P1, P2, P3
**Human refs (from References field):** 1.1, CN1, CN3, P1, P2, P3
**Jaccard:** 0.667 — AI adds ['CN5', 'D1.15', 'D1.20']

## Proposition 1.3
**Statement:** Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

**Step 1.** Let AB and CD be the given unequal straight lines, with AB greater than CD. We must cut off from AB a straight line equal to CD. [Given]

**Step 2.** At A place a straight line AF equal to CD. **Path choice:** use 1.2 directly, since it supplies the lesser length at the required endpoint A. [1.2]

**Step 3.** Describe a circle with centre A and distance AF, and let its circumference cut AB at E. Since AB is greater than CD, and AF equals CD, the circle cuts AB between A and B. [P3; D1.15; Step 1; Step 2]

**Step 4.** Since E and F lie on this circle, AE equals AF: both are straight lines from its centre to its circumference. [D1.15]

**Step 5.** Now AE equals AF, and CD also equals AF; therefore AE equals CD. Thus AE has been cut off from the greater straight line AB equal to the lesser straight line CD, as required. [CN1; Steps 2–4]

**USED:** 1.2, CN1, D1.15, P3
**Human refs (from References field):** 1.2, CN1, D1.15, P3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.4
**Statement:** If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base, the triangle will be equal to the triangle, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend.

**Step 1.** Let ABC and DEF be the two triangles, with AB = DE, AC = DF, and ∠BAC = ∠EDF, as given. We shall prove that BC = EF, that triangle ABC equals triangle DEF, and that ∠ABC = ∠DEF and ∠ACB = ∠DFE. Choose the direct route of superposition, comparing the figures by coincidence (CN4); no auxiliary construction or preceding proposition is needed.

**Step 2.** Superpose triangle ABC on triangle DEF, placing A at D and the straight side AB along the direction of DE, with C on the same side of DE as F. Then B coincides with E: otherwise, one of the equal segments AB and DE would be a proper part of the other, whereas the whole is greater than its part (given AB = DE; CN5).

**Step 3.** Since AB now lies along DE and the included angles ∠BAC and ∠EDF are equal, AC lies along the direction of DF. Indeed, if their directions differed on the chosen side of DE, one of the two angles would be a proper part of the other, contradicting their equality (D1.8, D1.9; CN5). Moreover, C coincides with F, since AC = DF: unequal positions of their endpoints along that direction would again make one equal segment a proper part of the other (given AC = DF; CN5).

**Step 4.** Thus B coincides with E and C with F. The straight base BC consequently coincides with the straight base EF, since both follow the straight course between the same extremities (D1.4). Therefore BC = EF, because things which coincide are equal (CN4).

**Step 5.** All three sides of triangle ABC now coincide respectively with the three sides of triangle DEF. Hence the triangular figures contained by those boundaries coincide (D1.14, D1.19). The whole triangle ABC is therefore equal to the whole triangle DEF (CN4).

**Step 6.** The sides BA and BC coincide respectively with ED and EF, so their contained angles ∠ABC and ∠DEF coincide and are equal. Likewise, CA and CB coincide respectively with FD and FE, so ∠ACB = ∠DFE (D1.8, D1.9; CN4). The first pair is opposite the equal sides AC and DF, and the second pair is opposite the equal sides AB and DE. Together with Steps 4 and 5, these are precisely all the required conclusions.

**USED:** CN4, CN5, D1.14, D1.19, D1.4, D1.8, D1.9
**Human refs (from References field):** CN4
**Jaccard:** 0.143 — AI adds ['CN5', 'D1.14', 'D1.19', 'D1.4', 'D1.8', 'D1.9']

## Proposition 1.5
**Statement:** In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

**Step 1.** Let ABC be an isosceles triangle with AB = AC and base BC. We must prove that ∠ABC = ∠ACB and that the angles under BC formed by producing AB and AC beyond B and C are equal. [D1.20]

**Step 2.** Produce AB beyond B to F, and produce AC beyond C to E far enough that AE > AF. [P2] Since AF > AB = AC, we also have AF > AC. [CN5] Cut off AG from AE equal to AF; consequently G lies beyond C. [1.3] Path choice: cutting off a length on the specified straight line directly supplies the equal whole lengths needed for the triangle comparison.

**Step 3.** Join FC and GB. [P1]

**Step 4.** Compare triangles AFC and AGB. We have AF = AG by construction and AC = AB by hypothesis. Moreover, ∠FAC = ∠GAB, since their bounding rays coincide in reverse order. [CN4] Thus the two pairs of sides and their included angles are equal, so apply 1.4 directly. It gives FC = GB, ∠ACF = ∠ABG, and ∠AFC = ∠AGB. [1.4]

**Step 5.** Subtract AB = AC from AF = AG. Since B lies between A and F, and C lies between A and G, the remaining segments satisfy BF = CG. [CN3]

**Step 6.** Because the rays FB and FA coincide, ∠BFC = ∠AFC; because the rays GC and GA coincide, ∠CGB = ∠AGB. [CN4] Together with ∠AFC = ∠AGB from Step 4, these equalities give ∠BFC = ∠CGB. [CN1]

**Step 7.** Compare triangles BFC and CGB. Their sides BF and FC equal CG and GB respectively, by Steps 5 and 4, and their included angles ∠BFC and ∠CGB are equal by Step 6. Therefore ∠FBC = ∠GCB and ∠BCF = ∠CBG. [1.4] The first equality is precisely the equality of the angles under the base.

**Step 8.** Since F lies beyond B on AB, the angle ∠ACF consists of ∠ACB together with ∠BCF. Similarly, since G lies beyond C on AC, the angle ∠ABG consists of ∠ABC together with ∠CBG. Subtract the equal angles ∠BCF and ∠CBG from the equal angles ∠ACF and ∠ABG obtained in Step 4. The remaining angles are equal: ∠ACB = ∠ABC. [CN3] Thus both the angles at the base and, by Step 7, the angles under the base are equal, as required.

**USED:** 1.3, 1.4, CN1, CN3, CN4, CN5, D1.20, P1, P2
**Human refs (from References field):** 1.3, 1.4, P1, P2
**Jaccard:** 0.444 — AI adds ['CN1', 'CN3', 'CN4', 'CN5', 'D1.20']

## Proposition 1.6
**Statement:** If in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another.

**Step 1.** Let ABC be a triangle with ∠ABC = ∠BCA. We must prove AC = AB. Choose a proof by contradiction: suppose these sides are unequal. Interchanging B and C if necessary, suppose AB > AC; this does not change the hypothesis. [Hypothesis; symmetry of the labels.]

**Step 2.** From BA cut off BD equal to AC, with D strictly between B and A, and join DC. [1.3; P1.]

**Step 3.** Since D lies on BA, the angles DBC and ABC coincide and are equal. Thus ∠DBC = ∠BCA, by the given equality of angles. Also BC = CB, since they are the same segment. [CN4; hypothesis; CN1.]

**Step 4.** Compare triangles DBC and ACB. We have DB = AC by Step 2, BC = CB by Step 3, and the included angles ∠DBC = ∠ACB by Step 3. Therefore triangle DBC equals triangle ACB. [1.4.] We use the equality-of-triangles conclusion of 1.4 because it yields a whole–part contradiction directly.

**Step 5.** Because D lies strictly between A and B, triangle DBC is a proper part of triangle ABC, which is the same triangle as ACB. Hence triangle ACB is greater than triangle DBC, since the whole is greater than the part. This contradicts their equality in Step 4. [Step 2; CN5.]

**Step 6.** The assumption that AB and AC are unequal is therefore impossible, so AB = AC. These are precisely the sides opposite the equal angles ∠BCA and ∠ABC. Thus the sides subtending equal angles in a triangle are equal. [Steps 1–5; contradiction.]

**USED:** 1.3, 1.4, CN1, CN4, CN5, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.3', '1.4', 'CN1', 'CN4', 'CN5', 'P1']

## Proposition 1.7
**Statement:** Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities), and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively, namely each to that which has the same extremity with it.

**Step 1.** Let AB be the given straight line. Suppose, contrary to the assertion, that distinct points C and D lie on the same side of AB and satisfy AC = AD and BC = BD. Join CD. [P1]

**Step 2.** The points A, C, D cannot be collinear: because C and D are on the same side of AB, they would lie on the same ray from A, making one of AC and AD a proper part of the other, contrary to their equality. Similarly, B, C, D cannot be collinear. Thus neither vertex lies on a side of the triangle formed by AB and the other vertex. [CN5]

**Step 3.** The direct route is to apply 1.5 to the given equal-side pairs. In triangles ACD and BCD respectively, it gives
∠ACD = ∠CDA and ∠BCD = ∠CDB.
We consider separately the exterior and nested placements of the two vertices; the under-base clause of the same theorem will handle the nested placement. [1.5]

**Step 4.** First suppose neither vertex lies inside the triangle formed by AB and the other vertex. Interchanging C and D if necessary, the four points form a convex quadrilateral in boundary order A, B, D, C. Consequently, ray CB lies strictly inside ∠ACD, and ray DA lies strictly inside ∠CDB. The whole angles are greater than their respective parts, so
∠ACD > ∠BCD and ∠CDB > ∠CDA.
Using Step 3, we obtain
∠CDB > ∠CDA = ∠ACD > ∠BCD,
contrary to ∠CDB = ∠BCD. This placement is therefore impossible. [CN5; 1.5]

**Step 5.** In the remaining noncollinear placement, one vertex lies inside the triangle formed by AB and the other vertex. Interchanging their names if necessary, let D lie inside triangle ABC. Produce AC beyond C to E, and AD beyond D to F. Since AC = AD, the equality of the angles under the base of triangle ACD gives
∠ECD = ∠CDF. [P2; 1.5]

**Step 6.** Because D is inside triangle ABC, ray CB lies strictly inside ∠ECD, while ray DF lies strictly inside ∠CDB. Hence
∠ECD > ∠BCD and ∠CDB > ∠CDF.
Together with Step 5, these yield
∠CDB > ∠CDF = ∠ECD > ∠BCD.
But Step 3 gives ∠CDB = ∠BCD, again a contradiction. Thus the nested placement is also impossible. [CN5; 1.5]

**Step 7.** The collinear boundary placements were excluded in Step 2, and the exterior and nested placements were excluded in Steps 4–6. These exhaust the placements of two distinct vertices on the same side of AB. Therefore no second point D on that side can satisfy both AC = AD and BC = BD, which proves the proposition. [Steps 2–6]

**USED:** 1.5, CN5, P1, P2
**Human refs (from References field):** 1.5
**Jaccard:** 0.250 — AI adds ['CN5', 'P1', 'P2']

## Proposition 1.8
**Statement:** If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines.

**Step 1.** Let ABC and DEF be triangles with AB = DE, AC = DF, and BC = EF. We must prove that ∠BAC = ∠EDF. (Given.)

**Step 2.** Apply triangle ABC to triangle DEF, placing B on E and BC along EF, with A on the same side of EF as D. Since BC = EF, C coincides with F: otherwise one of the equal segments would be a proper part of the other, contrary to CN5. Let G be the position occupied by A. (Superposition under CN4; given base equality; CN5.)

**Step 3.** Under this application, AB occupies EG and AC occupies FG. Thus EG = AB and FG = AC; together with the given equalities, these yield EG = ED and FG = FD. (CN4; CN1.)

**Step 4.** If G were distinct from D, the pairs ED, FD and EG, FG would stand on the same base EF, lie on the same side of it, and meet at different points, although the segments from each common extremity are equal respectively. This is impossible by 1.7. Hence G coincides with D. This is the direct path: the side equalities give precisely the same-base, same-side uniqueness configuration of 1.7. (1.7.)

**Step 5.** Consequently, the applied sides AB and AC coincide respectively with DE and DF, so their contained angle ∠BAC coincides with ∠EDF. Things which coincide are equal; therefore ∠BAC = ∠EDF, as required. (CN4.)

**USED:** 1.7, CN1, CN4, CN5
**Human refs (from References field):** 1.7
**Jaccard:** 0.250 — AI adds ['CN1', 'CN4', 'CN5']

## Proposition 1.9
**Statement:** To bisect a given rectilineal angle.

**Step 1.** Let ∠BAC be the given rectilineal angle, whose sides AB and AC are straight [D1.9]. Label the sides so that AB ≤ AC, and choose D strictly between A and B. Since the whole AB is greater than its part AD, we have AD < AB ≤ AC [CN5].

**Step 2.** Cut off AE from AC equal to AD [1.3]. Join DE [P1]. Thus AD = AE, with D and E on the respective sides of the given angle.

**Step 3.** On DE construct the equilateral triangle DEF, choosing F on the side of DE opposite A [1.1]. Consequently DF = EF [D1.20]. This opposite-side choice selects the inward direction for the eventual bisecting ray.

**Step 4.** Join AF [P1]. In triangles DAF and EAF, AD = AE by Step 2, AF = AF because it is common [CN4], and DF = EF by Step 3.

**Step 5.** Therefore ∠DAF = ∠EAF [1.8]. Here 1.8 is the direct choice: the three corresponding side equalities are already established, and it gives precisely the required equality of the angles contained by AD, AF and AE, AF.

**Step 6.** Since AD lies along AB and AE lies along AC, ∠BAF coincides with ∠DAF, while ∠FAC coincides with ∠EAF [CN4]. The opposite-side construction in Step 3 places ray AF inside ∠BAC. Thus the equality established in Step 5 says that AF divides the given angle into two equal angles. Hence the given rectilineal angle has been bisected.

**USED:** 1.1, 1.3, 1.8, CN4, CN5, D1.20, D1.9, P1
**Human refs (from References field):** 1.3, 1.8
**Jaccard:** 0.250 — AI adds ['1.1', 'CN4', 'CN5', 'D1.20', 'D1.9', 'P1']

## Proposition 1.10
**Statement:** To bisect a given finite straight line.

**Step 1.** Let AB be the given finite straight line. Construct an equilateral triangle ABC on AB (1.1). Thus AC = BC (D1.20).

**Step 2.** Bisect the angle ACB (1.9), and extend its internal bisector to meet the opposite side AB at D (P2). Thus D lies between A and B, and ∠ACD = ∠BCD (1.9).

**Step 3.** Compare triangles ACD and BCD. We have AC = BC by Step 1, CD = CD because the side is common (CN4), and ∠ACD = ∠BCD by Step 2. Therefore their bases are equal: AD = BD (1.4). This is the direct path: 1.4 applies immediately to the two equal sides and their equal included angles.

**Step 4.** Since D lies on the finite straight line AB between its extremities (Step 2), and AD = DB (Step 3, by 1.4), AB has been divided into two equal parts at D. Therefore the given finite straight line has been bisected.

**USED:** 1.1, 1.4, 1.9, CN4, D1.20, P2
**Human refs (from References field):** 1.1, 1.4, 1.9
**Jaccard:** 0.500 — AI adds ['CN4', 'D1.20', 'P2']

## Proposition 1.11
**Statement:** To draw a straight line at right angles to a given straight line from a given point on it.

**Step 1.** Let C be the given point on the given straight line. Choose another point D on that line, and produce DC beyond C to a point G so that CG is greater than CD. [P2]

**Step 2.** From CG cut off CE equal to CD. Thus D, C, E lie on the given straight line, with C between D and E, and CD = CE. [1.3]

**Step 3.** Construct the equilateral triangle DFE on DE. In particular, DF = EF. [1.1, D1.20]

**Step 4.** Join C to F. The side CF is common to triangles DCF and ECF, and hence is equal to itself. [P1, CN4]

**Step 5.** In triangles DCF and ECF, the sides DC and CF equal EC and CF respectively, and the bases DF and EF are equal. Therefore the contained angles DCF and ECF are equal. This side-based comparison is the direct choice: all three side equalities are already available, so no preliminary angle equality is needed. [1.8]

**Step 6.** Since D, C, E lie in a straight line, CF stands on that line and makes the adjacent angles DCF and FCE equal. Each is therefore a right angle, and CF is perpendicular to the given straight line at C. Thus the required straight line has been drawn. [D1.10]

**USED:** 1.1, 1.3, 1.8, CN4, D1.10, D1.20, P1, P2
**Human refs (from References field):** 1.1, 1.3, 1.8, D1.10
**Jaccard:** 0.500 — AI adds ['CN4', 'D1.20', 'P1', 'P2']

## Proposition 1.12
**Statement:** To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

**Step 1.** Let ℓ be the given infinite straight line and C the given point not on it. Choose a point O on ℓ, draw CO, and produce CO beyond O to a point D. [P1, P2]

**Step 2.** Describe the circle with centre C and radius CD. Since CO is a proper part of CD, CO < CD, so O lies inside the circle. Thus the infinite line ℓ cuts its circumference at two distinct points A and B, with O between them. [P3, CN5, D1.15]

**Step 3.** Bisect AB at H, so that AH = HB, and draw CA, CB, and CH. The chosen route is to join the centre to the midpoint of the chord AB. [1.10, P1]

**Step 4.** We have CA = CB, since both are radii of the same circle; AH = HB by the bisection; and CH = CH because it is common. [D1.15, 1.10, CN4]

**Step 5.** Apply 1.8 to triangles AHC and BHC: AH = BH and HC = HC, while their bases AC and BC are equal. Therefore ∠AHC = ∠BHC. Proposition 1.8 is the natural choice here because all three side equalities are already available, without first establishing an angle equality. [1.8]

**Step 6.** Since A, H, and B lie in that order on ℓ, these are the adjacent angles made by CH standing on ℓ. Being equal, each is a right angle, and CH is perpendicular to ℓ. Thus a perpendicular has been drawn to the given infinite straight line from the given point C not on it. [D1.10]

**USED:** 1.10, 1.8, CN4, CN5, D1.10, D1.15, P1, P2, P3
**Human refs (from References field):** 1.10, 1.8, D1.10, P1, P3
**Jaccard:** 0.556 — AI adds ['CN4', 'CN5', 'D1.15', 'P2']

## Proposition 1.13
**Statement:** If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

**Step 1.** Let C, B, D lie in that order on a straight line, and let BA stand on it, making the adjacent angles ∠CBA and ∠ABD. We must show that these are either two right angles or together equal to two right angles. [Hypothesis.]

**Step 2.** If ∠CBA = ∠ABD, each is a right angle by the definition of a right angle. This proves the first alternative. [D1.10.]

**Step 3.** Suppose instead that the two angles are unequal. Draw BE perpendicular to CD at B, on the same side of CD as A. Then ∠CBE and ∠EBD are equal right angles. The direct construction is 1.11, since the given vertex B is already on the straight line. [1.11; D1.10.]

**Step 4.** BA cannot coincide with BE, since then the original adjacent angles would be equal. Interchanging the names C and D if necessary, take BA to lie inside ∠CBE; consequently BE lies inside ∠ABD. The respective adjacent parts coincide with their whole angles, so
∠CBE = ∠CBA + ∠ABE,
and
∠ABD = ∠ABE + ∠EBD. [D1.10; CN4.]

**Step 5.** Add ∠EBD to both sides of the first equality, and add ∠CBA to both sides of the second. Thus
∠CBE + ∠EBD = ∠CBA + ∠ABE + ∠EBD,
and
∠CBA + ∠ABD = ∠CBA + ∠ABE + ∠EBD. [CN2.]

**Step 6.** Since both sums equal the same three angles, ∠CBA + ∠ABD = ∠CBE + ∠EBD. The latter are two right angles by Step 3. Hence the original angles are either themselves two right angles, as in Step 2, or together equal to two right angles, as required. [CN1; D1.10.]

**USED:** 1.11, CN1, CN2, CN4, D1.10
**Human refs (from References field):** 1.11, CN1, CN2, D1.10
**Jaccard:** 0.800 — AI adds ['CN4']

## Proposition 1.14
**Statement:** If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

**Step 1.** Let O be the given point on the straight line AO, and let OB and OC lie on opposite sides of that line. By hypothesis, ∠BOA + ∠AOC equals two right angles. We must show that OB and OC are in a straight line with one another. [Hypothesis.]

**Step 2.** Produce BO through O to D, so that B, O, D lie in a straight line, with O between B and D. [P2.] The direct path is to apply 1.13 to this extension, since it supplies a pair of adjacent angles for comparison with the given pair.

**Step 3.** Since OA stands on the straight line BOD, ∠BOA + ∠AOD equals two right angles. [1.13.] Consequently,
∠BOA + ∠AOC = ∠BOA + ∠AOD,
since both sums equal two right angles. [Hypothesis; CN1.]

**Step 4.** Subtract the common angle ∠BOA from these equal sums. The remaining angles are equal:
∠AOC = ∠AOD. [CN3.]

**Step 5.** The rays OC and OD lie on the same side of AO: each lies on the side opposite OB, by the hypothesis and the straight extension in Step 2. If OC and OD were distinct, either OC would lie inside ∠AOD or OD would lie inside ∠AOC. Thus one of these angles would be a proper part of the other, and the whole would be greater than the part. [CN5.] This contradicts their equality in Step 4. Therefore OC and OD coincide.

**Step 6.** Since OD is the straight continuation of BO and OC coincides with OD, OB and OC are in a straight line with one another, as required. [P2; Steps 2 and 5.]

**USED:** 1.13, CN1, CN3, CN5, P2
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.500 — AI adds ['CN5', 'P2']; Human adds ['P4']

## Proposition 1.15
**Statement:** If two straight lines cut one another, they make the vertical angles equal to one another.

**Step 1.** Let the straight lines AB and CD cut one another at O, with A, O, B in that order and C, O, D in that order. Write α = ∠AOC, β = ∠COB, γ = ∠BOD, and δ = ∠DOA. The vertical pairs to be proved equal are α, γ and β, δ. [Hypothesis and notation]

**Step 2.** Use the adjacent-angle theorem directly, since the straight lines are already given; no auxiliary construction is needed. OC standing on AB gives α + β equal to two right angles. OB standing on CD gives β + γ equal to two right angles. OD standing on AB gives γ + δ equal to two right angles. [1.13]

**Step 3.** All right angles are equal, so any two sums consisting of two right angles are equal, by adding equals to equals. Consequently the sums in Step 2 satisfy α + β = β + γ and β + γ = γ + δ. [P4, CN2, CN1]

**Step 4.** Subtract the common angle β from the equal sums α + β and β + γ. The remaining angles are equal: α = γ, that is, ∠AOC = ∠BOD. [CN3]

**Step 5.** Subtract the common angle γ from the equal sums β + γ and γ + δ. The remaining angles are equal: β = δ, that is, ∠COB = ∠DOA. [CN3]

**Step 6.** Both pairs of vertical angles are therefore equal. Hence, if two straight lines cut one another, they make the vertical angles equal to one another. [Steps 4–5]

**USED:** 1.13, CN1, CN2, CN3, P4
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.800 — AI adds ['CN2']

## Proposition 1.16
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

**Step 1.** Let ABC be any triangle, and produce BC beyond C to D. We must prove that the exterior angle ACD is greater than each of the angles BAC and ABC. [P2]

**Step 2.** Bisect AC at E. Join BE and produce it beyond E sufficiently far to cut off EF equal to EB; join CF. Thus A, E, C occur in that order, B, E, F occur in that order, and AE = EC and BE = EF. [1.10, P1, P2, 1.3]

**Step 3.** The angles AEB and CEF are vertically opposite and therefore equal. Hence triangles AEB and CEF have two sides respectively equal and their included angles equal. By side–angle–side, their corresponding angles EAB and ECF are equal. Since the rays AE and AC coincide, as do CE and CA, this gives ∠BAC = ∠ACF. The direct path is side–angle–side: the construction supplies precisely the two side equalities and the included vertical angles needed. [1.15, 1.4, CN4]

**Step 4.** From the order of the points in Step 2, F lies on the same side of line BC as A, and on the opposite side of line AC from B. Thus ray CF lies strictly inside the exterior angle ACD. Consequently ∠ACF is a proper part of ∠ACD, so ∠ACD > ∠ACF. Together with Step 3, this proves ∠ACD > ∠BAC. [Step 2, CN5, Step 3]

**Step 5.** To compare with the other opposite angle, produce AC beyond C to G. Bisect BC at H, join AH, and produce AH beyond H sufficiently far to cut off HK equal to HA. Join CK. Thus B, H, C occur in that order, A, H, K occur in that order, and BH = HC and AH = HK. [P2, 1.10, P1, 1.3]

**Step 6.** The angles BHA and CHK are vertically opposite and therefore equal. Applying side–angle–side to triangles BHA and CHK gives ∠HBA = ∠HCK. Since BH and BC are the same ray, as are CH and CB, these are respectively the angles ABC and BCK. Therefore ∠ABC = ∠BCK. [1.15, 1.4, CN4]

**Step 7.** From the order of the points in Step 5, K lies on the opposite side of line BC from A, and on the same side of line AC as B. Hence ray CK lies strictly inside ∠BCG. The angle BCK is therefore a proper part of ∠BCG, so ∠BCG > ∠BCK = ∠ABC. [Step 5, CN5, Step 6]

**Step 8.** Since BC is produced to D and AC is produced to G, the angles BCG and ACD are vertically opposite. Therefore ∠BCG = ∠ACD. [1.15]

**Step 9.** Substituting the equality in Step 8 into the inequality in Step 7 gives ∠ACD > ∠ABC; Step 4 already gives ∠ACD > ∠BAC. Thus the exterior angle is greater than either interior and opposite angle, as required. [Steps 4, 7–8]

**USED:** 1.10, 1.15, 1.3, 1.4, CN4, CN5, P1, P2
**Human refs (from References field):** 1.10, 1.15, 1.3, 1.4, CN5, P1, P2
**Jaccard:** 0.875 — AI adds ['CN4']

## Proposition 1.17
**Statement:** In any triangle two angles taken together in any manner are less than two right angles.

**Step 1.** Let any two angles of an arbitrary triangle be selected. Label their vertices A and B, and the remaining vertex C. Produce AB beyond B to D. [P2]

**Step 2.** The exterior angle ∠CBD of triangle ABC is greater than the interior and opposite angle ∠CAB. We choose this exterior-angle route because it directly compares one selected angle with an angle adjacent to the other. [1.16]

**Step 3.** Since A, B, D lie on one straight line, the straight line BC standing on that line makes adjacent angles ∠ABC and ∠CBD whose sum equals two right angles. [1.13]

**Step 4.** By Step 2, ∠CBD equals ∠CAB together with a positive excess. Adding ∠ABC to both equal magnitudes shows that ∠ABC + ∠CBD consists of ∠ABC + ∠CAB together with that same excess. [CN2] Hence ∠ABC + ∠CAB is less than ∠ABC + ∠CBD, since the whole is greater than its proper part. [CN5] By Step 3, therefore, ∠ABC + ∠CAB is less than two right angles.

**Step 5.** The triangle and the selected pair of angles were arbitrary. Thus, in any triangle, two angles taken together in any manner are less than two right angles. [Steps 1–4]

**USED:** 1.13, 1.16, CN2, CN5, P2
**Human refs (from References field):** 1.13, 1.16, P2
**Jaccard:** 0.600 — AI adds ['CN2', 'CN5']

## Proposition 1.18
**Statement:** In any triangle the greater side subtends the greater angle.

**Step 1.** Let ABC be any triangle with AC > AB. On AC cut off AD equal to AB, so that D lies strictly between A and C. [1.3] This construction is chosen to produce an isosceles triangle and an exterior angle directly.

**Step 2.** Join B to D. [P1]

**Step 3.** Since AB = AD, the base angles of triangle ABD are equal: ∠ABD = ∠BDA. The equal sides make the isosceles-triangle theorem the direct choice here. [1.5]

**Step 4.** In triangle BDC, the side CD is produced through D to A. Therefore its exterior angle ∠BDA is greater than the interior and opposite angle ∠BCD. [1.16] Since D lies on CA, the rays CD and CA coincide, so ∠BCD = ∠BCA. [CN4] Thus ∠BDA > ∠BCA.

**Step 5.** Because D lies strictly between A and C, BD lies inside ∠ABC, and ∠ABD is a proper part of ∠ABC. Hence ∠ABC > ∠ABD. [CN5]

**Step 6.** Combining the equality and inequalities gives ∠ABC > ∠ABD = ∠BDA > ∠BCA. [Steps 3–5] Thus the angle subtended by the greater side AC is greater than the angle subtended by the lesser side AB. Since the triangle and the unequal sides were arbitrary, in any triangle the greater side subtends the greater angle.

**USED:** 1.16, 1.3, 1.5, CN4, CN5, P1
**Human refs (from References field):** 1.16, 1.3
**Jaccard:** 0.333 — AI adds ['1.5', 'CN4', 'CN5', 'P1']

## Proposition 1.19
**Statement:** In any triangle the greater angle is subtended by the greater side.

**Step 1.** Let ABC be a triangle in which ∠ABC > ∠BCA (hypothesis). Their opposite sides are AC and AB, respectively. We must show AC > AB. We choose to exclude equality and the reverse inequality, requiring no auxiliary construction.

**Step 2.** Suppose AC = AB. Then ∠ABC = ∠BCA by **1.5**, contradicting the hypothesis in Step 1. Hence AC ≠ AB. Here 1.5 is the natural choice because the assumed equality is between sides, and its conclusion concerns the opposite angles.

**Step 3.** Suppose AC < AB. Since AB is then the greater side, **1.18** gives ∠BCA > ∠ABC, again contradicting the hypothesis in Step 1. Hence AC is not less than AB.

**Step 4.** Since AC is neither equal to AB nor less than AB, it follows that AC > AB (Steps 2–3). Thus the greater angle ∠ABC is subtended by the greater side AC. As the triangle and the pair of unequal angles were arbitrary, in any triangle the greater angle is subtended by the greater side.

**USED:** 1.18, 1.5
**Human refs (from References field):** 1.18, 1.5
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.20
**Statement:** In any triangle two sides taken together in any manner are greater than the remaining one.

**Step 1.** Let ABC be any triangle. We first compare AB and AC taken together with BC. Produce BA beyond A to E so that AE is greater than AC [P2]. Cut off AD from AE equal to AC [1.3], and join CD [P1]. Thus B, A, D lie in this order on one straight line.

**Step 2.** Since AC = AD, the base angles of triangle ACD are equal: ∠ACD = ∠CDA [1.5]. The rays DA and DB coincide, so ∠CDA = ∠CDB [CN4]. Consequently, ∠ACD = ∠CDB [CN1].

**Step 3.** Since A lies between B and D, the ray CA lies inside ∠BCD. Therefore ∠BCD is greater than its part ∠ACD [CN5]. By Step 2, it follows that ∠BCD > ∠CDB.

**Step 4.** In triangle BCD, the greater angle ∠BCD is subtended by BD, while ∠CDB is subtended by BC. Hence BD > BC [1.19]. This is the direct path: the angle comparison obtained in Step 3 naturally calls for 1.19, which converts it into a side comparison.

**Step 5.** Because A lies between B and D, BD consists of BA and AD taken together. Adding BA to the equality AD = AC gives BD = BA + AC [CN2]. Thus AB + AC > BC by Step 4.

**Step 6.** The labels of the arbitrary triangle were unrestricted. Applying Steps 1–5 with (A, B, C) replaced by (B, A, C) gives AB + BC > AC; replacing them by (C, A, B) gives AC + BC > AB. Together with Step 5, these establish that any two sides of a triangle taken together are greater than the remaining side.

**USED:** 1.19, 1.3, 1.5, CN1, CN2, CN4, CN5, P1, P2
**Human refs (from References field):** 1.19, 1.5, CN5
**Jaccard:** 0.333 — AI adds ['1.3', 'CN1', 'CN2', 'CN4', 'P1', 'P2']

## Proposition 1.21
**Statement:** If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greaterangle.

**Step 1.** Let ABC be a triangle, and let BD and CD be the two straight lines drawn from the extremities of BC to a point D within the triangle. We must prove that BD + DC < AB + AC and that ∠BDC > ∠BAC. [Hypothesis]

**Step 2.** Produce BD beyond D to meet AC at E. Since D is inside triangle ABC, E lies between A and C, and D lies between B and E. Choose this single extension because it supplies both triangle inequalities for the lengths and exterior-angle comparisons for the angles. [P2; interior-point hypothesis]

**Step 3.** In triangle ABE, AB + AE > BE. Add EC to both sides. Since AE + EC = AC, it follows that AB + AC > BE + EC. Here adding a common magnitude preserves the strict inequality: the excess remains a part of the greater whole. [1.20; CN2; CN5]

**Step 4.** In triangle DEC, DE + EC > DC. Adding BD gives BD + DE + EC > BD + DC. Since BD + DE = BE, this is BE + EC > BD + DC. Together with Step 3, this proves AB + AC > BD + DC. [1.20; CN2; CN5]

**Step 5.** In triangle DEC, ED is produced through D to B. Therefore the exterior angle ∠BDC is greater than the interior and opposite angle ∠DEC. Since the rays ED and EB coincide, ∠DEC = ∠BEC. Hence ∠BDC > ∠BEC. [1.16; CN4]

**Step 6.** In triangle ABE, AE is produced through E to C. Therefore the exterior angle ∠BEC is greater than the interior and opposite angle ∠BAE. Since the rays AE and AC coincide, ∠BAE = ∠BAC. Hence ∠BEC > ∠BAC. [1.16; CN4]

**Step 7.** Combining Steps 5 and 6 gives ∠BDC > ∠BAC. Thus the two constructed straight lines BD and DC are together less than AB and AC, but contain a greater angle, as required. [Steps 4–6; CN5]

**USED:** 1.16, 1.20, CN2, CN4, CN5, P2
**Human refs (from References field):** 1.16, 1.20
**Jaccard:** 0.333 — AI adds ['CN2', 'CN4', 'CN5', 'P2']

## Proposition 1.22
**Statement:** Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manner should be greater than the remaining one.

**Step 1.** Let the lengths of the three given straight lines be a, b, c. If a triangle has these side lengths, then a + b > c, b + c > a, and c + a > b, by 1.20. Thus the stated condition is necessary. Assume henceforth that these inequalities hold.

**Step 2.** Relabel the given lengths so that a is a greatest, and use the given segment of length a as the base AB. Mark E on AB so that AE = b: if b < a, apply 1.3; if b = a, take E = B. Path choice: choosing a greatest segment as the base makes the cutting-off construction of 1.3 directly applicable, without a separate transfer construction. [1.3]

**Step 3.** Produce BA beyond A sufficiently far, and on this produced part cut off AF equal to b. Thus F, A, E lie in that order on one straight line, and AF = AE = b. [P2, 1.3]

**Step 4.** Describe the circle Γ with centre A and radius AE, and the circle Δ with centre B and radius c. Both E and F lie on Γ, since AE = AF. [P3, D1.15]

**Step 5.** The point E is inside Δ. Indeed, if E = B, it is the centre. Otherwise, AB = AE + EB and b + c > a give AE + c > AE + EB; cancelling AE gives c > EB. On the other hand, F is outside Δ, because BF = BA + AF = a + b > c. Thus Γ has a point E inside Δ and a point F outside Δ. [Hypothesis, CN2, CN3, CN5, D1.15]

**Step 6.** Since EF passes through A and has its endpoints on Γ, it is a diameter. Consider either semicircular boundary of Γ from E to F. It begins inside the region bounded by Δ and ends outside that region, so it meets the boundary of Δ at some point C. Consequently C lies on both circles. Moreover, C is not on AB: the only points of Γ on that straight line are E and F, and neither lies on Δ. [D1.13, D1.15, D1.17, D1.18]

**Step 7.** Join AC and BC. Since C is not on AB, the three straight lines AB, BC, CA bound a triangle ABC. [P1, D1.19]

**Step 8.** Because C lies on Γ, AC = AE = b; because C lies on Δ, BC = c. Also AB = a by its selection. Therefore triangle ABC has its three sides respectively equal to the three given straight lines. Together with Step 1, this establishes both the construction under the stated condition and the necessity of that condition. [D1.15, CN1]

**USED:** 1.20, 1.3, CN1, CN2, CN3, CN5, D1.13, D1.15, D1.17, D1.18, D1.19, P1, P2, P3
**Human refs (from References field):** 1.20, 1.3
**Jaccard:** 0.143 — AI adds ['CN1', 'CN2', 'CN3', 'CN5', 'D1.13', 'D1.15', 'D1.17', 'D1.18', 'D1.19', 'P1', 'P2', 'P3']

## Proposition 1.23
**Statement:** On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

**Step 1.** Let ℓ be the given straight line and A the given point on it. Let the given rectilineal angle be ∠DCE, with D and E distinct from C on its respective sides. Since these sides do not lie in one straight line, joining DE forms triangle CDE. [D1.8, D1.9, P1]

**Step 2.** In triangle CDE, any two sides together are greater than the third. Thus
CD + CE > DE,
CD + DE > CE,
and CE + DE > CD.
These are exactly the conditions required to construct a triangle from the three lengths CD, CE, and DE. [1.20]

**Step 3.** Apply the triangle construction of 1.22, taking A as its initial vertex and a chosen direction along ℓ as the direction of its first side. Construct triangle AFG so that F lies on ℓ in that direction and
AF = CD, AG = CE, and FG = DE.
The inequalities established in Step 2 ensure that this construction applies. This is the chosen route: copy the three sides of triangle CDE, then compare the included angles. [1.22]

**Step 4.** Triangles AFG and CDE have AF = CD and AG = CE, and also their bases FG = DE. Therefore the angles contained by the corresponding equal sides are equal: ∠FAG = ∠DCE. The side–side–side criterion is the direct applicable comparison, since the construction supplies all three side equalities. Since AF lies on ℓ and the vertex of ∠FAG is A, the required rectilineal angle has been constructed on the given straight line at the given point. [1.8, D1.9]

**USED:** 1.20, 1.22, 1.8, D1.8, D1.9, P1
**Human refs (from References field):** 1.8
**Jaccard:** 0.167 — AI adds ['1.20', '1.22', 'D1.8', 'D1.9', 'P1']

## Proposition 1.24
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

**Step 1.** Let triangles ABC and DEF satisfy AB = DE, AC = DF, and ∠BAC > ∠EDF. We must prove BC > EF. (Hypotheses.) Path choice: use an auxiliary angle bisector and SAS to obtain a broken line equal to BC, then compare it with EF by 1.20. This requires no assumption about which of the given sides is longer.

**Step 2.** At A construct a ray strictly inside ∠BAC making with AB an angle equal to ∠EDF. This placement is possible because ∠EDF < ∠BAC. On that ray take X at its intersection with the circle having centre A and radius AC. Thus ∠BAX = ∠EDF and AX = AC. Join BX. (1.23; P3; D1.15; P1.)

**Step 3.** We have AB = DE, AX = AC = DF, and ∠BAX = ∠EDF. Hence triangles BAX and EDF have two corresponding sides and their included angles equal. The directly applicable result is SAS, which gives BX = EF. (CN1; 1.4.)

**Step 4.** Bisect ∠XAC, and let its bisector meet BC at M. Since this bisector lies strictly inside ∠BAC, M lies strictly between B and C. The rays occur within ∠BAC in the order AB, AX, AM, AC; consequently B and X lie on the same side of the straight line AM. Also ∠XAM = ∠MAC. (1.9; the angular placement in Step 2.)

**Step 5.** Join MX. In triangles XAM and CAM, AX = AC, AM is common, and ∠XAM = ∠CAM. Therefore XM = CM by SAS. (P1; 1.4.)

**Step 6.** We claim BM + MX > BX. If B, M, and X are not collinear, this is the triangle inequality in triangle BMX. (1.20.) If they are collinear, B and X, being on the same side of AM, lie on the same ray from M. They are distinct because AB and AX are distinct rays. Thus BX is a proper part of the longer of BM and MX, and BM + MX is greater still. The claimed inequality therefore also holds in this case. (CN5.)

**Step 7.** Since M lies between B and C, BC = BM + MC. Adding BM to the equality MC = MX gives BM + MC = BM + MX. Consequently BC = BM + MX > BX = EF. Thus the base opposite the greater included angle is greater than the other base, as required. (CN2; CN1; Steps 3, 5, and 6.)

**USED:** 1.20, 1.23, 1.4, 1.9, CN1, CN2, CN5, D1.15, P1, P3
**Human refs (from References field):** 1.19, 1.23, 1.4, 1.5
**Jaccard:** 0.167 — AI adds ['1.20', '1.9', 'CN1', 'CN2', 'CN5', 'D1.15', 'P1', 'P3']; Human adds ['1.19', '1.5']

## Proposition 1.25
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.

**Step 1.** Let ABC and DEF be triangles with AB = DE, AC = DF, and BC > EF (hypotheses). We must prove ∠BAC > ∠EDF. We use elimination of the equal and smaller cases, requiring no auxiliary construction.

**Step 2.** First suppose ∠BAC = ∠EDF. The two given side equalities and this equality of included angles imply BC = EF by **1.4**, contradicting BC > EF. Thus ∠BAC is not equal to ∠EDF. Equality is tested first because **1.4** applies immediately to the given equal sides.

**Step 3.** Next suppose ∠BAC < ∠EDF. Apply **1.24** to triangles DEF and ABC, in that order: DE = AB and DF = AC, while ∠EDF > ∠BAC. It follows that EF > BC, contradicting BC > EF. Thus ∠BAC is not less than ∠EDF.

**Step 4.** Since ∠BAC is neither equal to nor less than ∠EDF, it must be greater than ∠EDF (Steps 2–3). Therefore the greater base lies opposite the greater angle contained by the respectively equal sides, as required.

**USED:** 1.24, 1.4
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.26
**Statement:** If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of the equal angles, they will also have the remaining sides equal tothe remaining sides and the remaining angle to the remaining angle.

**Step 1.** Let ABC and DEF be triangles with ∠ABC = ∠DEF and ∠BCA = ∠EFD. We must prove equality of the remaining corresponding sides and of ∠BAC and ∠EDF, given either BC = EF or a corresponding pair of sides opposite one of the equal angles. [Hypotheses]

**Step 2.** First suppose BC = EF, the sides adjoining the equal angles. We shall establish AB = DE so that side-angle-side applies directly. If AB and DE are unequal, interchange the triangles if necessary so that AB > DE. Cut off BG = DE on BA, with G strictly between B and A, and join GC. [1.3, P1]

**Step 3.** Since BG and BA have the same direction from B, ∠GBC = ∠ABC = ∠DEF. Thus triangles GBC and DEF have BG = DE, BC = EF, and the included angles equal. Consequently ∠BCG = ∠EFD. [CN4, hypothesis, 1.4]

**Step 4.** But ∠BCA = ∠EFD by hypothesis, so ∠BCG = ∠BCA. Since G lies strictly between B and A, CG lies inside ∠BCA, and ∠BCG is a proper part of ∠BCA. This contradicts the whole being greater than its part. Therefore AB = DE. [CN1, CN5]

**Step 5.** Now AB = DE, BC = EF, and ∠ABC = ∠DEF. Apply side-angle-side directly to triangles ABC and DEF: AC = DF and ∠BAC = ∠EDF. This completes the case of the equal sides adjoining the equal angles. [1.4]

**Step 6.** Next suppose AB = DE, the sides opposite the equal angles ∠BCA and ∠EFD. The alternative AC = DF is covered by interchanging B with C and E with F. We shall establish BC = EF; here the exterior-angle inequality provides the contradiction. If BC and EF are unequal, interchange the triangles if necessary so that BC > EF. Cut off BH = EF on BC, with H strictly between B and C, and join AH. [Hypothesis, relabeling, 1.3, P1]

**Step 7.** Since BH and BC have the same direction from B, ∠ABH = ∠ABC = ∠DEF. Together with AB = DE and BH = EF, this gives, by side-angle-side in triangles ABH and DEF, ∠BHA = ∠EFD. [CN4, hypothesis, 1.4]

**Step 8.** In triangle AHC, the side CH is produced beyond H to B. Therefore its exterior angle ∠BHA is greater than the interior and opposite angle ∠HCA. But ∠HCA = ∠BCA, since CH and CB have the same direction from C, and ∠BCA = ∠EFD by hypothesis. Hence ∠BHA > ∠EFD, contradicting Step 7. Therefore BC = EF. [1.16, CN4, CN1]

**Step 9.** We now have AB = DE, BC = EF, and ∠ABC = ∠DEF. Side-angle-side in the original triangles therefore gives AC = DF and ∠BAC = ∠EDF. Thus the assertion also holds when the given equal sides subtend one of the equal angles. [1.4]

**Step 10.** In either permitted position of the given equal side, the remaining corresponding sides are equal and the remaining angles are equal, as required. [Steps 5 and 9]

**USED:** 1.16, 1.3, 1.4, CN1, CN4, CN5, P1
**Human refs (from References field):** 1.16, 1.4
**Jaccard:** 0.286 — AI adds ['1.3', 'CN1', 'CN4', 'CN5', 'P1']

## Proposition 1.27
**Statement:** If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

**Step 1.** Let the transversal meet the two coplanar straight lines at distinct points E and F. Choose A on the first line and D on the second, on opposite sides of the transversal, so that the given alternate angles are ∠AEF and ∠EFD. Thus ∠AEF = ∠EFD (hypothesis). Produce the two straight lines in both directions as necessary (P2). Path choice: use the exterior-angle inequality (1.16), since a hypothetical intersection immediately makes these angles an exterior angle and an opposite interior angle of a triangle.

**Step 2.** Suppose the lines meet at G on the same side of the transversal as D. Then FG is the same ray as FD, while EA is opposite to EG. In triangle EFG, therefore, ∠AEF is an exterior angle and ∠EFG is an opposite interior angle. Hence ∠AEF > ∠EFG by 1.16. But ∠EFG is precisely ∠EFD, contradicting the equality in Step 1. Thus the lines cannot meet on this side (1.16; hypothesis).

**Step 3.** Suppose instead that the lines meet at H on the same side of the transversal as A. Then EH is the same ray as EA, while FD is opposite to FH. In triangle EFH, therefore, ∠EFD is an exterior angle and ∠HEF is an opposite interior angle. Hence ∠EFD > ∠HEF by 1.16. But ∠HEF is precisely ∠AEF, again contradicting the equality in Step 1. Thus the lines cannot meet on this side either (1.16; hypothesis).

**Step 4.** Any meeting would have to lie on one of these two sides of the transversal, since the two lines meet the transversal at the distinct points E and F. Steps 2 and 3 exclude both possibilities. Consequently the two coplanar straight lines, produced indefinitely in both directions, do not meet; they are therefore parallel (D1.23).

**USED:** 1.16, D1.23, P2
**Human refs (from References field):** 1.16, D1.23
**Jaccard:** 0.667 — AI adds ['P2']

## Proposition 1.28
**Statement:** If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to two right angles, the straight lines will be parallel to one another.

**Step 1.** Let the transversal meet the two coplanar straight lines AB and CD at E and F respectively. Label the points in the orders A, E, B and C, F, D, with A and C on one side of the transversal and B and D on the other. Produce FE beyond E to G (P2). The path chosen in each case is to obtain equal alternate angles and apply the directly available parallelism criterion, 1.27.

**Step 2.** First suppose that the exterior angle ∠GEB equals the interior and opposite angle ∠EFD on the same side of the transversal (first hypothesis). Since AB and GF intersect at E, their vertical angles ∠GEB and ∠AEF are equal (1.15). Therefore ∠AEF = ∠EFD (CN1).

**Step 3.** The angles ∠AEF and ∠EFD are alternate angles made by the transversal EF with AB and CD. Their equality therefore implies that AB is parallel to CD (1.27). This proves the first case.

**Step 4.** Now suppose instead that the interior angles ∠BEF and ∠EFD on the same side together equal two right angles (second hypothesis). Since A, E, B lie on one straight line, ∠BEF and ∠AEF also together equal two right angles (1.13). All right angles are equal (P4), so the two pairs of right angles have equal sums (CN2). Consequently,
∠BEF + ∠AEF = ∠BEF + ∠EFD (CN1).

**Step 5.** Subtract the common angle ∠BEF from these equal sums. The remaining angles satisfy ∠AEF = ∠EFD (CN3). These are alternate angles, so AB is parallel to CD (1.27). Thus either of the stated conditions makes the two straight lines parallel to one another.

**USED:** 1.13, 1.15, 1.27, CN1, CN2, CN3, P2, P4
**Human refs (from References field):** 1.13, 1.15, 1.27
**Jaccard:** 0.375 — AI adds ['CN1', 'CN2', 'CN3', 'P2', 'P4']

## Proposition 1.29
**Statement:** A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

**Step 1.** Let the parallel straight lines AB and CD be cut by a transversal at G and H, respectively. Label the points so that A,G,B and C,H,D occur in those orders, with A,C on one side of the transversal and B,D on the other. Produce the transversal to E and F so that E,G,H,F occur in that order [P2]. Since AB and CD are parallel, they cannot meet in either direction [D1.23]. Write 2R for the magnitude of two right angles, which is independent of the right angles chosen [P4].

**Step 2.** Put α = ∠AGH, β = ∠BGH, γ = ∠GHC, and δ = ∠GHD. The adjacent angles at each intersection satisfy
α + β = 2R and γ + δ = 2R [1.13].
Path choice: first establish alternate-angle equality directly through P5; the adjacent sums supplied by 1.13 make this possible without an auxiliary construction.

**Step 3.** Suppose α > δ. Adding β gives δ + β < α + β = 2R: replacing the larger angle by the smaller makes the sum a proper part of the former sum [CN2, CN5; Step 2]. But β and δ are the interior angles on the side containing B and D. Therefore AB and CD, produced indefinitely, meet on that side [P5], contrary to their parallelism [D1.23]. Thus α cannot exceed δ.

**Step 4.** Suppose instead α < δ. Adding γ gives α + γ < δ + γ = 2R, by the same whole-and-part comparison [CN2, CN5; Step 2]. Now α and γ are the interior angles on the side containing A and C, so AB and CD meet on that side [P5], again contrary to parallelism [D1.23]. Neither inequality is possible; hence α = δ [Steps 3–4].

**Step 5.** The sums α + β and γ + δ are equal, since each equals 2R [Step 2; CN1]. Subtracting the equal angles α and δ leaves β = γ [Step 4; CN3]. Consequently both pairs of alternate angles are equal:
∠AGH = ∠GHD and ∠BGH = ∠GHC [Steps 4–5].

**Step 6.** Vertical angles are equal [1.15]. Thus the exterior angles satisfy
∠EGB = α = δ = ∠GHD,
∠AGE = β = γ = ∠GHC,
∠CHF = δ = α = ∠AGH,
and ∠DHF = γ = β = ∠BGH [Steps 4–5; CN1].
Therefore each exterior angle equals the interior and opposite angle at the other intersection.

**Step 7.** Adding β to α = δ yields β + δ = α + β = 2R [Steps 2, 4; CN2, CN1]. Adding γ to the same equality yields α + γ = δ + γ = 2R [Steps 2, 4; CN2, CN1]. These are precisely the interior-angle sums on the two sides of the transversal. Hence a straight line falling on parallel straight lines makes the alternate angles equal, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

**USED:** 1.13, 1.15, CN1, CN2, CN3, CN5, D1.23, P2, P4, P5
**Human refs (from References field):** 1.13, 1.15, CN1, CN2, P5
**Jaccard:** 0.500 — AI adds ['CN3', 'CN5', 'D1.23', 'P2', 'P4']

## Proposition 1.30
**Statement:** Straight lines parallel to the same straight line are also parallel to one another.

**Step 1.** Let a and b be straight lines in the same plane, each parallel to a straight line c. Draw a straight transversal t meeting a, b, and c at distinct points A, B, and C, respectively, producing it as necessary. [P1, P2]

**Step 2.** Fix one direction along t and one side of t. At each intersection, take the angle between the ray of t in that direction and the ray of the intersected line lying on that side. Denote these angles at A, B, and C by α, β, and γ. Since a is parallel to c, the corresponding angles α and γ are equal. [1.29]

**Step 3.** Since b is parallel to c, the corresponding angles β and γ are likewise equal. [1.29]

**Step 4.** Thus α and β are equal, since each is equal to γ. [CN1]

**Step 5.** For the two lines a and b cut by t, α and β form an exterior angle and its interior and opposite angle on the same side. Their equality therefore implies that a is parallel to b. We use the corresponding-angle criterion directly, since this is precisely the equality obtained, rather than converting it into an alternate-angle equality. Hence straight lines parallel to the same straight line are also parallel to one another. [1.28]

**USED:** 1.28, 1.29, CN1, P1, P2
**Human refs (from References field):** 1.29, CN1
**Jaccard:** 0.400 — AI adds ['1.28', 'P1', 'P2']

## Proposition 1.31
**Statement:** Through a given point to draw a straight line parallel to a given straight line.

**Step 1.** Let BC be the given straight line and A the given point in its plane, outside BC. The point must be outside BC because parallel straight lines do not meet (D1.23). Join AB (P1).

**Step 2.** On AB, at A, construct the angle EAB equal to the angle ABC, choosing E on the opposite side of AB from C (1.23).

**Step 3.** Produce EA through A to F, so that E, A, F lie on one straight line (P2).

**Step 4.** The transversal AB makes the equal alternate angles EAB and ABC with EF and BC. Therefore EF is parallel to BC (1.27). This is the directly applicable criterion, since the construction supplies equal alternate angles. Thus EF is the required straight line through A parallel to BC.

**USED:** 1.23, 1.27, D1.23, P1, P2
**Human refs (from References field):** 1.23, 1.27
**Jaccard:** 0.400 — AI adds ['D1.23', 'P1', 'P2']

## Proposition 1.32
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

**Step 1.** Let ABC be any triangle, and produce BC beyond C to D. Thus ∠ACD is the exterior angle at C, and its interior and opposite angles are ∠BAC and ∠ABC. [P2]

**Step 2.** Through C draw a straight line parallel to AB, taking its ray CE within ∠ACD. Path choice: use the available parallel construction directly, so that the parallel-line angle theorem supplies both required angle equalities without an auxiliary triangle. [1.31]

**Step 3.** Since AC falls on the parallel straight lines AB and CE, the alternate angles are equal:
∠BAC = ∠ACE. [1.29]

**Step 4.** Since the straight line BCD falls on the same parallels, the exterior angle equals the interior and opposite angle:
∠ECD = ∠ABC. [1.29]

**Step 5.** Add the equalities in Steps 3 and 4. The adjacent angles ∠ACE and ∠ECD together constitute ∠ACD, so
∠ACD = ∠BAC + ∠ABC.
Thus the exterior angle equals the two interior and opposite angles together. [CN2]

**Step 6.** Since CA stands on the straight line BCD, its adjacent angles satisfy
∠ACD + ∠ACB = two right angles. [1.13]

**Step 7.** Add ∠ACB to both sides of the equality in Step 5. Then
∠ACD + ∠ACB = ∠BAC + ∠ABC + ∠ACB. [CN2]
Combining this with Step 6 gives
∠BAC + ∠ABC + ∠ACB = two right angles. [CN1]
Since the triangle and the side produced were arbitrary, both assertions hold in any triangle.

**USED:** 1.13, 1.29, 1.31, CN1, CN2, P2
**Human refs (from References field):** 1.13, 1.29, 1.31
**Jaccard:** 0.500 — AI adds ['CN1', 'CN2', 'P2']

## Proposition 1.33
**Statement:** The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.

**Step 1.** Let AB and CD be equal and parallel straight lines, with A corresponding to C and B to D at the extremities in the same directions. Join AC and BD. We must prove that AC and BD are equal and parallel. (Given; P1.)

**Step 2.** Join BC. This single auxiliary line allows a side–angle–side comparison of triangles ABC and DCB. (P1.)

**Step 3.** Since AB is parallel to CD, the transversal BC makes the alternate angles ∠ABC and ∠DCB equal. The stipulated pairing of extremities places A and D on opposite sides of BC, so these are indeed the alternate angles. (Given same-direction condition; 1.29.)

**Step 4.** We have AB = CD by hypothesis, and BC equals itself because it is the same segment. (CN4.) Thus triangles ABC and DCB have two sides respectively equal and their included angles equal by Step 3. By side–angle–side, their remaining sides and corresponding remaining angles are equal: AC = BD and ∠ACB = ∠DBC. (1.4.)

**Step 5.** The equal angles ∠ACB and ∠DBC are alternate angles made by BC with AC and BD. Therefore AC is parallel to BD. (1.27.) This criterion applies directly to the alternate-angle equality already obtained, without converting it to another angle condition. Together with AC = BD from Step 4, this proves that the straight lines joining the corresponding extremities are themselves equal and parallel.

**USED:** 1.27, 1.29, 1.4, CN4, P1
**Human refs (from References field):** 1.27, 1.29, 1.4
**Jaccard:** 0.600 — AI adds ['CN4', 'P1']

## Proposition 1.34
**Statement:** In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.

**Step 1.** Let ABCD be a parallelogram, with its vertices named consecutively, so that AB is parallel to CD and BC is parallel to AD. Draw the diameter AC, joining opposite vertices. [P1]

**Step 2.** Since AC falls on the parallel lines AB and CD, the alternate angles BAC and DCA are equal. Since AC also falls on the parallel lines BC and AD, the alternate angles BCA and DAC are equal. [1.29]

**Step 3.** Compare triangles ABC and CDA. They have the two pairs of equal angles established in Step 2, and their adjoining side AC is common and therefore equal to itself. [CN4] Consequently, AB = CD, BC = DA, and angle ABC = angle CDA. [1.26] Thus the opposite sides and one pair of opposite angles are equal. **Path choice:** 1.26 applies immediately to the two angle equalities and their common adjoining side, without requiring any further construction.

**Step 4.** Add the equal angles DAC and BCA to the equal angles CAB and ACD, respectively. The resulting whole angles are DAB and BCD; hence angle DAB = angle BCD. [Step 2; CN2] Thus the other pair of opposite angles is also equal.

**Step 5.** In triangles ABC and CDA, AB = CD and BC = DA, while their contained angles ABC and CDA are equal, all by Step 3. Therefore triangle ABC equals triangle CDA in area. [1.4] **Path choice:** 1.4 explicitly supplies equality of the triangles, whereas the stated conclusion of 1.26 supplies only their corresponding sides and angles.

**Step 6.** The diameter AC divides the parallelogram into precisely triangles ABC and CDA. Since these two parts are equal by Step 5, AC bisects the area. Together with Steps 3 and 4, this proves that the opposite sides and angles of the parallelogram are equal and that its diameter bisects its area. The naming of the vertices was arbitrary, so the argument applies to either diameter. [Steps 1, 3–5]

**USED:** 1.26, 1.29, 1.4, CN2, CN4, P1
**Human refs (from References field):** 1.26, 1.29, 1.4, CN2
**Jaccard:** 0.667 — AI adds ['CN4', 'P1']

## Proposition 1.35
**Statement:** Parallelograms which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EBCF be parallelograms on the same base BC, with their opposite sides AD and EF on the same straight line parallel to BC. Name the vertices so that AD and EF run in the same direction along that line. By 1.34, AD = BC and EF = BC, hence AD = EF by CN1. Also AB = DC by 1.34. We will compare two triangles removed from one enclosing quadrilateral; this route handles overlapping and separated upper sides alike.

**Step 2.** If A = E, then D = F: otherwise one of the equal segments AD and EF would be a proper part of the other, contrary to CN5. The parallelograms then coincide and are equal by CN4. Otherwise, interchange the names of the parallelograms if necessary so that A precedes E along the upper line. Then D precedes F, for otherwise EF would be a proper part of AD, contradicting AD = EF and CN5. Thus both D and E lie between A and F; their order relative to each other need not be specified.

**Step 3.** Produce AD to F (P2). From the same whole segment AF, subtract the equal segments AD and EF. The respective remainders are DF and AE, so DF = AE (CN3; the common whole is equal to itself by CN4).

**Step 4.** The opposite sides AB and DC are parallel by the hypothesis that ABCD is a parallelogram. The straight line AF meets them, and its rays AE and DF have the same direction. Therefore ∠BAE = ∠CDF, by the exterior–interior angle equality of 1.29.

**Step 5.** In triangles BAE and CDF, BA = CD by Step 1, AE = DF by Step 3, and the included angles are equal by Step 4. Therefore these triangles are equal by 1.4. Side–angle–side is the naturally first applicable triangle-equality criterion here: the required two sides and included angle are already available.

**Step 6.** Consider the enclosing quadrilateral ABCF. Since D and E both lie on AF (Step 2), removing triangle DCF from this quadrilateral leaves precisely parallelogram ABCD, while removing triangle ABE leaves precisely parallelogram EBCF. The removed triangles are equal by Step 5, and the whole quadrilateral is the same in both subtractions (CN4). Hence the remainders ABCD and EBCF are equal by CN3. Therefore parallelograms on the same base and in the same parallels are equal to one another.

**USED:** 1.29, 1.34, 1.4, CN1, CN3, CN4, CN5, P2
**Human refs (from References field):** 1.29, 1.34, 1.4, CN1, CN2, CN3
**Jaccard:** 0.556 — AI adds ['CN4', 'CN5', 'P2']; Human adds ['CN2']

## Proposition 1.36
**Statement:** Parallelograms which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EFGH be parallelograms on equal bases AB and EF lying on a straight line ℓ, with their opposite sides DC and HG lying on a straight line m parallel to ℓ. Label corresponding endpoints so that AB, EF, and DC run in the same direction along the parallels. Thus AB = EF and ℓ ∥ m. [Hypothesis.] The direct route is to introduce one auxiliary parallelogram and apply the same-base result twice. [1.35]

**Step 2.** Since opposite sides of a parallelogram are equal, DC = AB. [1.34] Together with AB = EF, this gives DC = EF. [CN1]

**Step 3.** Join DE and CF. [P1] The segments DC and EF are equal and parallel, and these joins connect their corresponding extremities. Therefore DE ∥ CF. [1.33] Since also DC ∥ EF, the quadrilateral EFCD is a parallelogram. This uses 1.33 directly because the required equal parallel segments are already available.

**Step 4.** The parallelograms ABCD and EFCD are on the same base DC and between the same parallels m and ℓ. Therefore ABCD and EFCD are equal in area. [1.35]

**Step 5.** The parallelograms EFGH and EFCD are on the same base EF and between the same parallels ℓ and m. Therefore EFGH and EFCD are equal in area. [1.35]

**Step 6.** Since ABCD and EFGH are each equal in area to EFCD, they are equal to one another. [CN1] Hence parallelograms on equal bases and in the same parallels are equal to one another.

**USED:** 1.33, 1.34, 1.35, CN1, P1
**Human refs (from References field):** 1.33, 1.34, 1.35, CN1
**Jaccard:** 0.800 — AI adds ['P1']

## Proposition 1.37
**Statement:** Triangles which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let triangles ABC and DBC have the same base BC, with their vertices A and D on a straight line ℓ parallel to BC. We must prove that the triangles are equal in area. The lines ℓ and BC do not meet. [Hypothesis; D1.23]

**Step 2.** Through C draw a straight line parallel to AB and another parallel to DB; produce them as necessary to meet ℓ at E and F respectively. [1.31; P2] These intersections exist: each constructed line is distinct from BC because it is parallel to a side that meets BC. If it did not meet ℓ, it would be parallel to ℓ, and hence parallel to BC, although it meets BC at C—a contradiction. [D1.23; 1.30]

**Step 3.** The quadrilaterals ABCE and DBCF are parallelograms: AB is parallel to CE and AE to BC, while DB is parallel to CF and DF to BC. Both parallelograms stand on the same base BC and lie between the same parallels BC and ℓ. Therefore they are equal in area. [Construction; hypothesis; 1.35] The same-base result 1.35 is the direct choice here, since the base is shared, not merely equal in length.

**Step 4.** The diagonal AC bisects the area of parallelogram ABCE, so triangle ABC is half of that parallelogram. Similarly, the diagonal DC bisects parallelogram DBCF, so triangle DBC is half of that parallelogram. [1.34]

**Step 5.** These halves are equal. Indeed, if either half exceeded the other by a positive area, adding two copies of this decomposition would make its whole equal to the other whole together with two copies of that excess. [CN2] Its whole would therefore be greater than the other whole, contrary to Step 3. [CN5] Thus triangle ABC equals triangle DBC in area. Therefore triangles on the same base and in the same parallels are equal to one another.

**USED:** 1.30, 1.31, 1.34, 1.35, CN2, CN5, D1.23, P2
**Human refs (from References field):** 1.31, 1.34, 1.35
**Jaccard:** 0.375 — AI adds ['1.30', 'CN2', 'CN5', 'D1.23', 'P2']

## Proposition 1.38
**Statement:** Triangles which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let ABC and DEF be triangles with equal bases BC = EF lying on a straight line ℓ, and with their vertices A and D on a straight line m parallel to ℓ. We must prove that the triangles are equal in area. (Hypothesis.)

**Step 2.** Through C draw a straight line parallel to AB, and through F draw a straight line parallel to DE. (1.31.) These lines meet m at points G and H respectively. Indeed, if the first did not meet m, it would be parallel to m, and consequently AB would be parallel to m, contrary to their meeting at A; the same reasoning applies to the second line and DE. (D1.23; 1.30.) Thus ABCG and DEFH are parallelograms: AB is parallel to CG, DE is parallel to FH, and their other pairs of opposite sides lie on ℓ and m. (Construction; hypothesis.)

**Step 3.** The parallelograms ABCG and DEFH are on the equal bases BC and EF and between the same parallels ℓ and m. Therefore they are equal in area. (1.36.) This is the direct equal-base route: 1.36 applies without reducing the construction to a common base.

**Step 4.** The diagonal AC bisects parallelogram ABCG, and the diagonal DF bisects parallelogram DEFH. Hence ABCG consists of two triangles each equal to ABC, while DEFH consists of two triangles each equal to DEF. (1.34.)

**Step 5.** Consequently, the double of triangle ABC equals the double of triangle DEF. (Steps 3–4; CN1.) If either triangular area exceeded the other by a positive remainder R, adding equal copies would express its double as the other double together with two copies of R. (CN2.) Its double would then be greater than the other double, since the whole is greater than the part, contradicting their equality. (CN5.) Therefore triangle ABC equals triangle DEF in area. Thus triangles on equal bases and in the same parallels are equal to one another.

**USED:** 1.30, 1.31, 1.34, 1.36, CN1, CN2, CN5, D1.23
**Human refs (from References field):** 1.31, 1.34, 1.36
**Jaccard:** 0.375 — AI adds ['1.30', 'CN1', 'CN2', 'CN5', 'D1.23']

## Proposition 1.39
**Statement:** Equal triangles which are on the same base and on the same side are also in the same parallels.

**Step 1.** Let triangles ABC and ABD be equal in area, on the same base AB, with C and D on the same side of AB. We must show that their vertices C and D lie on a straight line parallel to AB. (Hypothesis.)

**Step 2.** Through C draw a straight line ℓ parallel to AB. If D lies on ℓ, the conclusion follows immediately. Suppose, therefore, that D does not lie on ℓ. Our chosen route is to construct a comparison triangle on the very same base AB. (1.31.)

**Step 3.** Produce AD and ℓ as necessary. They must meet at a point E: otherwise they would be parallel; and, since AB is also parallel to ℓ, AD would be parallel to AB, contrary to their meeting at A. (P2, D1.23, 1.30.)

**Step 4.** Since ℓ does not meet AB, its point E lies on the same side of AB as C, and hence as D. Thus E lies on the ray from A through D. Moreover, E is neither A nor D: A lies on AB, whereas D was assumed not to lie on ℓ. Consequently, either E lies between A and D, or D lies between A and E. Join BE. (D1.23; Step 2; P1.)

**Step 5.** Triangles ABC and ABE are on the same base AB and between the same parallels AB and ℓ, so they are equal. Here 1.37 is the direct choice because the base is identical, not merely equal in length. Since triangle ABC also equals triangle ABD by hypothesis, triangle ABE equals triangle ABD. (1.37, CN1.)

**Step 6.** If E lies between A and D, triangle ABE is a proper part of triangle ABD, so triangle ABD is greater than triangle ABE. If D lies between A and E, triangle ABD is a proper part of triangle ABE, so triangle ABE is greater than triangle ABD. Either case contradicts their equality in Step 5. (CN5.)

**Step 7.** Therefore D must lie on ℓ. Both triangles have their base on AB and their opposite vertices on ℓ, with ℓ parallel to AB. Hence equal triangles on the same base and on the same side are in the same parallels. (Steps 2 and 6.)

**USED:** 1.30, 1.31, 1.37, CN1, CN5, D1.23, P1, P2
**Human refs (from References field):** 1.31, 1.37, CN1
**Jaccard:** 0.375 — AI adds ['1.30', 'CN5', 'D1.23', 'P1', 'P2']

## Proposition 1.40
**Statement:** Equal triangles which are on equal bases and on the same side are also in the same parallels.

**Step 1.** Let ABC and DEF be equal triangles whose equal bases BC and EF lie on the same straight line ℓ, and whose vertices A and D lie on the same side of ℓ. We must prove that the triangles lie in the same parallels. [Given.]

**Step 2.** Join AE and AF, and through A draw a straight line m parallel to ℓ. The auxiliary triangle AEF will reduce the comparison from equal bases to the same base EF. [P1; 1.31.]

**Step 3.** Triangles ABC and AEF stand on the equal bases BC and EF and lie between the same parallels ℓ and m. Therefore triangle ABC equals triangle AEF. Here 1.38 is the applicable forward proposition because the bases are equal, rather than necessarily identical. [1.38.]

**Step 4.** Triangle DEF equals triangle ABC by hypothesis, and triangle AEF equals triangle ABC by Step 3. Hence triangle AEF equals triangle DEF. [CN1.]

**Step 5.** Triangles AEF and DEF now have the same base EF, are equal, and lie on the same side of its straight line. Thus the same-base converse applies: they lie in the same parallels. One of those parallels is ℓ, and the other contains both A and D. Since the original bases BC and EF lie on ℓ, the original triangles ABC and DEF likewise lie in these same parallels, as required. [1.39; Step 1.]

**USED:** 1.31, 1.38, 1.39, CN1, P1
**Human refs (from References field):** 1.31, 1.38, CN1
**Jaccard:** 0.600 — AI adds ['1.39', 'P1']

## Proposition 1.41
**Statement:** If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.

**Step 1.** Let ABCD be the given parallelogram, with vertices in order, and let ABE be the given triangle on the common base AB. By hypothesis, E lies on the straight line CD, which is parallel to AB. Join AC (P1). Our route is to divide the given parallelogram by its diagonal and compare one resulting triangle with ABE.

**Step 2.** The diagonal AC bisects the parallelogram ABCD into the equal triangles ABC and ACD (1.34). Thus these two triangles together constitute the whole parallelogram.

**Step 3.** Triangles ABC and ABE have the same base AB and lie between the same parallels AB and CD. They are therefore equal in area (1.37). This common-base theorem applies directly, so an equal-base comparison is unnecessary.

**Step 4.** Since triangle ACD equals triangle ABC, and triangle ABC equals triangle ABE, triangle ACD also equals triangle ABE (CN1). Adding these equalities, the two triangles ABC and ACD together equal two copies of triangle ABE (CN2). Their union is the parallelogram ABCD by Step 2. Therefore the parallelogram is double of the triangle, as required.

**USED:** 1.34, 1.37, CN1, CN2, P1
**Human refs (from References field):** 1.34, 1.37
**Jaccard:** 0.400 — AI adds ['CN1', 'CN2', 'P1']

## Proposition 1.42
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let ABC be the given triangle and θ the given rectilineal angle. Bisect BC at D, so that BD = DC, and join AD. [1.10, P1]

**Step 2.** At D construct a ray r on the same side of BC as A, making with DC an angle equal to θ. Through A draw a straight line ℓ parallel to BC, and let r meet ℓ at E, producing the lines as necessary. [1.23, 1.31, P2] This intersection exists: otherwise the straight line containing r would be parallel to ℓ and therefore to BC, although it meets BC at D. Since r points into the side containing A, E lies on that ray. [D1.23, 1.30]

**Step 3.** Through C draw a straight line parallel to DE, meeting ℓ at F, producing it as necessary. [1.31, P2] It must meet ℓ, since otherwise it would be parallel to ℓ and hence to BC, although it meets BC at C. [D1.23, 1.30] Now DC is parallel to EF, and DE is parallel to CF; therefore DCFE is a parallelogram. Its angle CDE equals θ by construction. [1.31, 1.23]

**Step 4.** Triangles ABD and ADC have equal bases BD and DC and lie between the same parallels BC and ℓ. They are therefore equal in area. [1.38] This is the natural equal-base route: bisecting BC supplies two distinct equal bases, so no reduction to a common base is needed.

**Step 5.** AD divides triangle ABC into triangles ABD and ADC. Adding triangle ADC to the equal areas established in Step 4 shows that triangle ABC is double triangle ADC. [CN2]

**Step 6.** Parallelogram DCFE and triangle ADC have the same base DC and lie between the same parallels BC and ℓ. Hence the parallelogram is double triangle ADC. [1.41] Since triangle ABC is also double that triangle, parallelogram DCFE equals triangle ABC in area. [CN1] Its angle CDE equals the given angle θ, so the required parallelogram has been constructed. [1.23]

**USED:** 1.10, 1.23, 1.30, 1.31, 1.38, 1.41, CN1, CN2, D1.23, P1, P2
**Human refs (from References field):** 1.23, 1.31, 1.38, 1.41
**Jaccard:** 0.364 — AI adds ['1.10', '1.30', 'CN1', 'CN2', 'D1.23', 'P1', 'P2']

## Proposition 1.43
**Statement:** In any parallelogram the complements of the parallelograms about the diameter are equal to one another.

**Step 1.** Let ABCD be a parallelogram, and draw its diameter AC (P1). Label the given parallelograms about this diameter AEKH and KFCG, where K lies inside AC, and E, F, G, H lie respectively on AB, BC, CD, DA. Here E, K, G are collinear, as are H, K, F. The complements are therefore EBFK and HKGD. All equalities below are equalities of areas.

**Step 2.** Since AC is a diameter of parallelogram ABCD, triangle ABC equals triangle ADC (1.34). The direct path is to use the diameter-bisection assertion of 1.34: it applies immediately to the whole parallelogram and to both parallelograms about its diameter.

**Step 3.** In parallelogram AEKH, the diameter AK bisects its area, so triangle AEK equals triangle AHK. Likewise, in parallelogram KFCG, the diameter KC bisects its area, so triangle KFC equals triangle KGC (1.34).

**Step 4.** Adding these two equalities, the triangles AEK and KFC taken together equal the triangles AHK and KGC taken together (CN2).

**Step 5.** From the equal triangles ABC and ADC of Step 2, subtract respectively the equal pairs of triangles in Step 4. Within triangle ABC, removing AEK and KFC leaves exactly the complement EBFK; within triangle ADC, removing AHK and KGC leaves exactly the complement HKGD. Equal quantities subtracted from equal quantities leave equal remainders (CN3). Hence EBFK equals HKGD: the complements of the parallelograms about the diameter are equal to one another.

**USED:** 1.34, CN2, CN3, P1
**Human refs (from References field):** 1.34, CN2, CN3
**Jaccard:** 0.750 — AI adds ['P1']

## Proposition 1.44
**Statement:** To a given straight line to apply, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let AB be the given straight line, T the given triangle, and θ the given rectilineal angle. The direct construction is to obtain the required area and angle by 1.42, then transfer the area to a parallelogram on AB by 1.43. Produce AB beyond B and, at B, construct an angle equal to θ with one arm along this continuation. (P2, 1.23)

**Step 2.** In this angle construct the parallelogram BEFG equal in area to T, with A, B, E in that order on one straight line and ∠EBG = θ. Thus BE ∥ GF and BG ∥ EF. No length is prescribed for the auxiliary side BE. (1.42)

**Step 3.** Through A draw a straight line parallel to BG, meeting FG produced beyond G at H; thus H, G, F are in that order. The intersection on this extension follows from the parallel-angle relations and the parallel postulate. Since AH ∥ BG and BG ∥ EF, also AH ∥ EF. Join HB. (1.31, P2, 1.29, P5, 1.30, P1)

**Step 4.** Produce HB beyond B to X, and FE beyond E to Y. In triangle HAB, the two angles ∠ABH and ∠HAB together are less than two right angles. This is precisely the two-angle inequality needed to establish the next intersection. Moreover, ∠EBX = ∠ABH, being vertical angles, and ∠BEY = ∠HAB, being alternate angles between AH and EF. Consequently, ∠EBX and ∠BEY together are less than two right angles. (P2, 1.17, 1.15, 1.29, CN2)

**Step 5.** Therefore the straight lines BX and EY, produced, meet at K on the side of BE containing those rays. In particular, H, B, K are in that order, as are F, E, K. (P5)

**Step 6.** Through K draw a straight line parallel to AB, meeting HA produced beyond A at L and GB produced beyond B at M. These intersections follow from the parallel-angle relations and P5. Now HF ∥ LK and HL ∥ FK, so HFKL is a parallelogram. Also AB ∥ LM and AL ∥ BM, so ABML is a parallelogram having the given segment AB as a whole side. (1.31, P2, 1.29, P5, 1.30)

**Step 7.** The diameter HK of HFKL passes through B. The straight lines ABE and GBM through B are parallel to its respective pairs of opposite sides. Hence HGBA and BEKM are the two parallelograms about this diameter, while BEFG and ABML are their complements. The complements are equal; therefore ABML equals BEFG in area. Since BEFG equals T, ABML also equals T. (1.43, CN1)

**Step 8.** Since BA and BE are opposite rays, and BM and BG are opposite rays, ∠ABM and ∠EBG are vertical angles. Thus ∠ABM = ∠EBG = θ. Therefore ABML is a parallelogram applied to the given straight line AB, in an angle equal to the given angle, and equal in area to the given triangle, as required. (1.15, CN1)

**USED:** 1.15, 1.17, 1.23, 1.29, 1.30, 1.31, 1.42, 1.43, CN1, CN2, P1, P2, P5
**Human refs (from References field):** 1.15, 1.29, 1.31, 1.42, 1.43, CN1, P5
**Jaccard:** 0.538 — AI adds ['1.17', '1.23', '1.30', 'CN2', 'P1', 'P2']

## Proposition 1.45
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.

**Step 1.** Let F be the given rectilineal figure and θ the given rectilineal angle. First dissect F into finitely many triangles. The following construction also allows F to be nonconvex. Its boundary consists of finitely many straight sides [D1.19]. Produce one side into a straight line ℓ [P2], and through each vertex not on ℓ draw a parallel to ℓ, retaining only distinct lines [1.31]. Cut the figure along these lines. Between consecutive lines there are no vertices: each component is bounded laterally by two straight boundary segments and otherwise by portions of the two parallel lines. Each nondegenerate piece is therefore a triangle or a convex quadrilateral. Divide every such quadrilateral by a diagonal [P1]. Call the resulting triangles T₁, …, Tₙ; their interiors are disjoint and together they constitute F.

**Step 2.** Construct a parallelogram ABCD equal to T₁, with ∠DAB = θ [1.42]. This is the natural first construction because no side of the required parallelogram is yet prescribed; the subsequent additions will require 1.44 because their common sides will already be fixed.

**Step 3.** Suppose ABCD is the parallelogram obtained so far, and let T be the next triangle. Apply to the straight line CB a parallelogram BEFC equal to T, on the side of BC opposite ABCD, with ∠CBE = ∠BCD [1.44]. Choosing the existing angle BCD directly supplies the angle equality needed to join the two parallelograms.

**Step 4.** Since AB is parallel to DC, the transversal BC gives
∠ABC + ∠BCD = two right angles [1.29].
Replacing ∠BCD by its equal ∠CBE gives
∠ABC + ∠CBE = two right angles [CN2, CN1].
The rays BA and BE lie on opposite sides of BC. Therefore A, B, E lie on one straight line, with B between A and E [1.14].

**Step 5.** Since BE is parallel to CF, the transversal BC gives
∠CBE + ∠BCF = two right angles [1.29].
Replacing ∠CBE by its equal ∠BCD gives
∠BCD + ∠BCF = two right angles [CN2, CN1].
The rays CD and CF lie on opposite sides of BC. Therefore D, C, F lie on one straight line, with C between D and F [1.14].

**Step 6.** Both AD and EF are parallel to BC, so AD is parallel to EF [1.30]. Moreover, AE and DF lie on the same straight lines as AB and DC respectively; hence AE is parallel to DF [D1.23]. Thus AEFD is a parallelogram. Since ray AE coincides with ray AB, its angle DAE equals ∠DAB, and therefore equals θ [CN4, CN1].

**Step 7.** The parallelograms ABCD and BEFC lie on opposite sides of their common side BC. By the straight-line continuations established in Steps 4 and 5, they together constitute exactly AEFD, without overlapping interiors. Since BEFC equals T, adding these equal areas shows that AEFD equals the triangles previously represented by ABCD together with T [1.44, CN2].

**Step 8.** Repeat Steps 3–7 for every remaining triangle of the finite dissection. Each repetition produces one parallelogram, preserves its angle θ, and adds exactly the area of the next triangle. Consequently, the final parallelogram equals all of T₁, …, Tₙ together, and hence equals F [CN2, CN1]. A parallelogram equal to the given rectilineal figure has therefore been constructed in the given rectilineal angle, as required.

**USED:** 1.14, 1.29, 1.30, 1.31, 1.42, 1.44, CN1, CN2, CN4, D1.19, D1.23, P1, P2
**Human refs (from References field):** 1.14, 1.29, 1.30, 1.33, 1.34, 1.42, 1.44, CN1, CN2
**Jaccard:** 0.467 — AI adds ['1.31', 'CN4', 'D1.19', 'D1.23', 'P1', 'P2']; Human adds ['1.33', '1.34']

## Proposition 1.46
**Statement:** On a given straight line to describe a square.

**Step 1.** Let AB be the given finite straight line. Since A lies on the given line, use 1.11 to draw AX at right angles to AB. Produce AX, if necessary, until it is greater than AB (P2), and cut off AD equal to AB (1.3). Thus AD = AB and ∠DAB is right.

**Step 2.** Through B draw a straight line ℓ parallel to AD, and through D draw a straight line m parallel to AB (1.31). These lines meet: otherwise ℓ and m would be parallel (D1.23), and, since AD is parallel to ℓ, m would also be parallel to AD (1.30), contrary to their meeting at D (D1.23). Call their intersection C. Thus AB ∥ DC and AD ∥ BC, so ABCD is a parallelogram.

**Step 3.** Path choice: because the construction already gives a parallelogram, apply its opposite-side equalities directly (1.34). These give AB = DC and AD = BC. Together with AD = AB, they show that all four sides of ABCD are equal (CN1).

**Step 4.** Since AD and BC are parallel and AB falls upon them, the interior angles ∠DAB and ∠ABC together equal two right angles (1.29). But ∠DAB is right. Subtracting this right angle from the two equal sums shows that ∠ABC is also right (P4, CN3).

**Step 5.** The opposite angles of the parallelogram are equal: ∠BCD = ∠DAB and ∠CDA = ∠ABC (1.34). Hence the angles at C and D are right also. Therefore all four angles of ABCD are right.

**Step 6.** The quadrilateral ABCD is both equilateral and right-angled, and is therefore a square (D1.22). It has the given straight line AB as a side. Thus a square has been described on the given straight line.

**USED:** 1.11, 1.29, 1.3, 1.30, 1.31, 1.34, CN1, CN3, D1.22, D1.23, P2, P4
**Human refs (from References field):** 1.11, 1.29, 1.31, 1.34
**Jaccard:** 0.333 — AI adds ['1.3', '1.30', 'CN1', 'CN3', 'D1.22', 'D1.23', 'P2', 'P4']

## Proposition 1.47
**Statement:** In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.

**Step 1.** Let ABC be a right-angled triangle, with ∠BAC right [D1.21]. Construct the squares BCDE, ABFG, and ACKH externally on BC, AB, and AC respectively, naming each square’s vertices in cyclic order [1.46]. Their sides are equal and their angles right [D1.22]; consequently their opposite sides are parallel [P4, 1.28]. Equalities between figures below mean equalities of area.

**Step 2.** Produce BC as necessary and draw AM perpendicular to its line [P2, 1.12, D1.10]. The angles ABC and ACB are each less than a right angle, since each, together with the right angle BAC, is less than two right angles [1.17]. Therefore M lies strictly between B and C. Indeed, if M were an endpoint, the corresponding angle of ABC would be right. If M lay beyond B or beyond C, respectively ∠ABC or ∠ACB would be an exterior angle of a triangle having a right angle at M, and would therefore exceed a right angle [1.16]. Both alternatives are impossible.

**Step 3.** Since AM, BE, and CD are perpendicular to BC, AM is parallel to both BE and CD [P4, 1.28]. Produce AM beyond M to meet ED at L [P2, P5]. The point L lies between E and D: the line enters the square at the interior point M of BC and cannot cross either BE or CD, to which it is parallel [D1.23]. Since BC is parallel to ED, BMLE and MCDL are parallelograms, and together they constitute the square BCDE.

**Step 4.** The angles GAB and BAC are right, and AG and AC lie on opposite sides of AB because ABFG was constructed externally. Thus G, A, and C lie on one straight line [D1.22, P4, 1.14]. Likewise, the right angles BAC and CAH show that B, A, and H lie on one straight line [D1.22, P4, 1.14].

**Step 5.** Join AE, FC, AD, and KB [P1]. At B, external placement of the squares gives
∠ABE = ∠ABC + ∠CBE,
and
∠FBC = ∠FBA + ∠ABC.
The angles CBE and FBA are both right [D1.22, P4]. Adding the common angle ABC therefore gives ∠ABE = ∠FBC [CN2].

**Step 6.** We have AB = BF and BE = BC, since these are sides of their respective squares [D1.22]. Together with ∠ABE = ∠FBC, these are precisely two pairs of equal sides and equal included angles. Thus the directly applicable side–angle–side proposition gives triangle ABE equal to triangle FBC [1.4].

**Step 7.** The parallelogram BMLE and triangle ABE have the same base BE and lie between the same parallels BE and AL. Hence BMLE is double triangle ABE [1.41]. The square ABFG and triangle FBC have the same base BF and lie between the same parallels BF and AG, because C lies on the straight line AG by Step 4. Hence ABFG is double triangle FBC [1.41]. This shared-base configuration makes 1.41 the direct area comparison. Since the two triangles are equal, their doubles are equal; therefore BMLE equals ABFG [CN2, CN1].

**Step 8.** At C, external placement similarly gives
∠ACD = ∠ACB + ∠BCD,
and
∠KCB = ∠KCA + ∠ACB.
The angles BCD and KCA are right, so these whole angles are equal [D1.22, P4, CN2]. Also AC = CK and CD = CB, by the equal sides of the squares [D1.22]. Therefore triangle ACD equals triangle KCB by the same direct side–angle–side comparison [1.4].

**Step 9.** The parallelogram MCDL and triangle ACD have the same base CD and lie between the same parallels CD and AL. Thus MCDL is double triangle ACD [1.41]. The square ACKH and triangle KCB have the same base CK and lie between the same parallels CK and AH, because B lies on the straight line AH by Step 4. Thus ACKH is double triangle KCB [1.41]. The triangles being equal by Step 8, their doubles are equal, and consequently MCDL equals ACKH [CN2, CN1].

**Step 10.** Add the equalities from Steps 7 and 9 [CN2]. Since BMLE and MCDL together constitute BCDE, the square BCDE equals the squares ABFG and ACKH taken together. These are respectively the square on BC and the squares on AB and AC. Therefore, in a right-angled triangle, the square on the side subtending the right angle equals the squares on the sides containing the right angle.

**USED:** 1.12, 1.14, 1.16, 1.17, 1.28, 1.4, 1.41, 1.46, CN1, CN2, D1.10, D1.21, D1.22, D1.23, P1, P2, P4, P5
**Human refs (from References field):** 1.14, 1.4, 1.41, 1.46, CN2
**Jaccard:** 0.278 — AI adds ['1.12', '1.16', '1.17', '1.28', 'CN1', 'D1.10', 'D1.21', 'D1.22', 'D1.23', 'P1', 'P2', 'P4', 'P5']

## Proposition 1.48
**Statement:** If in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right.

**Step 1.** Let ABC be a triangle such that the square on BC equals the squares on AB and AC together. Write S(XY) for the area of a square on XY; any auxiliary squares required may be constructed by 1.46. Thus S(BC) = S(AB) + S(AC). We must prove that angle BAC is right. [Hypothesis; 1.46]

**Step 2.** Draw a perpendicular to AC at A, choosing its ray on the opposite side of AC from B. Produce this ray sufficiently, and cut off AD equal to AB. Join DC. Then angle DAC is right. Our path is to compare ABC with this constructed right-angled triangle, so that 1.47 can be applied without assuming the desired conclusion. [1.11; P2; 1.3; P1; D1.10]

**Step 3.** Since AD = AB, the squares on AD and AB are equal: on superposing their equal sides and corresponding right angles, the squares coincide, because all the sides of each square are equal and all its angles are right. Hence S(AD) = S(AB). [D1.22; P4; CN4]

**Step 4.** Apply 1.47 to the triangle DAC, which is right-angled at A. It gives S(DC) = S(AD) + S(AC). [1.47]

**Step 5.** Add S(AC) to the equal areas in Step 3. Then S(AD) + S(AC) = S(AB) + S(AC). Combining this equality with Step 4 and the hypothesis yields S(DC) = S(BC). [CN2; CN1]

**Step 6.** Therefore DC = BC. Indeed, if these sides were unequal, superpose the squares on them with a vertex coinciding and the two side-directions through that vertex coinciding. This placement is possible because their angles are right. Since every side of each square equals its defining side, the square on the shorter segment would be a proper part of the square on the longer segment. Its area would therefore be less, contrary to Step 5. Thus the sides cannot be unequal. [D1.22; P4; CN4; CN5]

**Step 7.** In triangles DAC and BAC, DA = BA by construction, AC is common, and DC = BC by Step 6. Proposition 1.8 therefore gives angle DAC equal to angle BAC. This is the direct choice because all three corresponding side equalities are now available. Since angle DAC is right, angle BAC is right also. Thus the angle contained by the remaining two sides of the given triangle is right, as required. [CN4; 1.8; D1.10]

**USED:** 1.11, 1.3, 1.46, 1.47, 1.8, CN1, CN2, CN4, CN5, D1.10, D1.22, P1, P2, P4
**Human refs (from References field):** 1.47, 1.8
**Jaccard:** 0.143 — AI adds ['1.11', '1.3', '1.46', 'CN1', 'CN2', 'CN4', 'CN5', 'D1.10', 'D1.22', 'P1', 'P2', 'P4']
