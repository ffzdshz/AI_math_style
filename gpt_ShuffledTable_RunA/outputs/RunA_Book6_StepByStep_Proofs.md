# Book 6 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 6.1
**Statement:** Triangles and parallelograms which are under the same height are to one another as their bases.

**Step 1.** Let X and Y be triangles with respective bases b and c and the same height. Place their bases on one straight line ℓ, with both triangles on the same side of it; their vertices then lie on a parallel line r bounding the common height. Such placement does not change their magnitudes. We shall prove the triangle assertion directly by comparing arbitrary equimultiples. [D6.4, CN4]

**Step 2.** Choose O on ℓ and A on r. On one ray of ℓ beginning at O, mark B and C so that OB = b and OC = c, producing the line and cutting off the required lengths as necessary; join A to O, B, and C. The triangles AOB and AOC equal X and Y respectively, by I.38: their bases are respectively equal, and they lie in the same parallels. I.38 is the appropriate equality theorem here because the bases need not occupy the same position. [P2, 1.3, P1, 1.38]

**Step 3.** Let m and n be any positive integers. Along the same ray from O, lay off m successive segments each equal to b, ending at D, and n successive segments each equal to c, ending at E. Join A to every division point. Each of the m subtriangles composing AOD equals AOB, and each of the n subtriangles composing AOE equals AOC, by I.38. Adding these equal magnitudes gives
OD = m·b,  OE = n·c,
and
△AOD = m·X,  △AOE = n·Y.
Thus these constructions provide the required equimultiples of the bases and triangles. [P2, 1.3, P1, 1.38, CN2, D5.2]

**Step 4.** Since D and E lie on the same ray from O, their order also determines the comparison of the two larger triangles. If OD > OE, then E lies between O and D, so AOE is a proper part of AOD and △AOD > △AOE. If OD = OE, then D and E coincide, and the triangles are equal. If OD < OE, the reverse proper-part relation gives △AOD < △AOE. Consequently m·X and n·Y have exactly the same comparison as m·b and n·c. [CN5, CN4]

**Step 5.** Since m and n were arbitrary, the defining equimultiple criterion for equality of ratios gives
X : Y = b : c.
Therefore triangles of the same height are to one another as their bases. [D5.5]

**Step 6.** Now let P and Q be parallelograms of the same height, with bases b and c. On each base take a triangle whose vertex lies on the opposite side of its parallelogram, and denote these triangles by T and U. They have the same height, so Step 5 gives T : U = b : c. Each parallelogram has the same base as its corresponding triangle and lies in the same parallels; hence P is double T and Q is double U. This doubling gives a direct passage to parallelograms without repeating the equimultiple construction. [P1, 1.41]

**Step 7.** Parts have the same ratio as their corresponding equal multiples; therefore T : U = P : Q. Since T : U also equals b : c, it follows that P : Q = b : c. Thus triangles of the same height, and likewise parallelograms of the same height, are to one another as their bases. [5.15, 5.11]

**USED:** 1.3, 1.38, 1.41, 5.11, 5.15, CN2, CN4, CN5, D5.2, D5.5, D6.4, P1, P2
**Human refs (from References field):** 1.38, 1.41, 5.11, 5.15, D5.5
**Jaccard:** 0.385 — AI adds ['1.3', 'CN2', 'CN4', 'CN5', 'D5.2', 'D6.4', 'P1', 'P2']

## Proposition 6.2
**Statement:** If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section will be parallel to the remaining side of the triangle.

**Step 1.** Let ABC be a triangle, with D and E interior points of AB and AC respectively. Draw DE, BE, and CD. Write [XYZ] for the area of triangle XYZ. We use a direct area proof, comparing triangles on the common base DE. [P1]

**Step 2.** Triangles BDE and ADE have their bases BD and DA on the same straight line and the common vertex E, so they have the same height. Likewise, triangles CDE and ADE have bases CE and EA on the same straight line and the common vertex D. Therefore
[BDE] : [ADE] = BD : DA,
and
[CDE] : [ADE] = CE : EA. [6.1]

**Step 3.** First suppose DE is parallel to BC. Triangles BDE and CDE are on the same base DE and in the same parallels DE and BC; hence [BDE] = [CDE]. The common-base theorem is the natural choice here because the two triangles already share DE. [1.37]

**Step 4.** Equal magnitudes have the same ratio to the same magnitude, so
[BDE] : [ADE] = [CDE] : [ADE].
Combining this with Step 2 gives BD : DA = CE : EA. Thus the parallel line cuts the two sides proportionally. [5.7, 5.11]

**Step 5.** Conversely, suppose BD : DA = CE : EA. The two equalities in Step 2 then give
[BDE] : [ADE] = [CDE] : [ADE]. [6.1, 5.11]

**Step 6.** Magnitudes having the same ratio to the same magnitude are equal. Hence [BDE] = [CDE]. [5.9]

**Step 7.** Since D and E are interior points of AB and AC, B and C lie on the same side of DE. Thus BDE and CDE are equal triangles on the same base DE and on the same side. They are therefore in the same parallels: the straight line BC through their opposite vertices is parallel to DE. This common-base converse completes the reverse implication. Consequently, a line parallel to one side of a triangle cuts the other two sides proportionally, and proportional sections of those sides are joined by a line parallel to the remaining side. [1.39]

**USED:** 1.37, 1.39, 5.11, 5.7, 5.9, 6.1, P1
**Human refs (from References field):** 1.38, 1.39, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.625 — AI adds ['1.37', 'P1']; Human adds ['1.38']

## Proposition 6.3
**Statement:** If an angle of a triangle be bisected and the straight line cutting the angle cut the base also, the segments of the base will have the same ratio as the remaining sides of the triangle; and, if the segments of the base have the same ratio as the remaining sides of the triangle, the straight line joined from the vertex to the point of section will bisect the angle of the triangle.

**Step 1.** Let ABC be a triangle, and let D lie between B and C on its base. Join AD. Through C draw CE parallel to AD, meeting BA produced beyond A at E. We use this auxiliary parallel because the immediately preceding proposition, 6.2, directly compares the required base segments with segments on BE. [P1, P2, 1.31]

**Step 2.** In triangle BCE, the straight line AD is parallel to CE. Therefore the sides are cut proportionally:
BD:DC = BA:AE. [6.2]

**Step 3.** Since AD and CE are parallel, the transversal BE gives ∠BAD = ∠AEC, and the transversal AC gives ∠DAC = ∠ACE. [1.29]

**Step 4.** First suppose that AD bisects ∠BAC, so that ∠BAD = ∠DAC. The equalities in Step 3 imply ∠AEC = ∠ACE. Hence, in triangle ACE, the sides opposite these equal angles are equal: AC = AE. [CN1, 1.6]

**Step 5.** Since AE = AC, the same magnitude BA has the same ratio to each: BA:AE = BA:AC. Combining this with Step 2 yields
BD:DC = BA:AC.
Thus the segments of the base have the same ratio as the remaining sides of the triangle. [5.7, 5.11]

**Step 6.** Conversely, suppose that BD:DC = BA:AC. Together with Step 2, this gives BA:AE = BA:AC. Magnitudes to which the same magnitude has the same ratio are equal; consequently AE = AC. [5.11, 5.9]

**Step 7.** Triangle ACE is therefore isosceles, so ∠AEC = ∠ACE. Using the angle equalities from Step 3, we obtain ∠BAD = ∠DAC. Thus AD bisects ∠BAC. Both directions of the proposition are proved. [1.5, CN1]

**USED:** 1.29, 1.31, 1.5, 1.6, 5.11, 5.7, 5.9, 6.2, CN1, P1, P2
**Human refs (from References field):** 1.29, 1.5, 1.6, 5.11, 5.9, 6.2
**Jaccard:** 0.545 — AI adds ['1.31', '5.7', 'CN1', 'P1', 'P2']

## Proposition 6.4
**Statement:** In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

**Step 1.** Let the equiangular triangles be ABC and DCE, with ∠BAC = ∠CDE, ∠ABC = ∠DCE, and ∠ACB = ∠DEC. Place them with B, C, E in that order on one straight line and A, D on the same side of it; congruent placement preserves their sides and angles (CN4; P2). The given equal angles are corresponding angles along this straight line, so I.28 gives AB ∥ CD and AC ∥ DE. We use these parallels to obtain the proportions directly from VI.2.

**Step 2.** In triangle DCE, the angles ∠DCE and ∠DEC together are less than two right angles (I.32; CN5). Since ∠ABC = ∠DCE, the interior angles made by AB and DE with BE on the side containing A and D are likewise less than two right angles. Therefore, on producing BA and ED, they meet at a point F on that side (P2; P5). The parallels from Step 1 ensure that A lies between B and F and D lies between E and F.

**Step 3.** Since FA ∥ CD and FD ∥ AC, the quadrilateral FACD is a parallelogram. Its opposite sides are equal, so FA = CD and FD = AC (I.34).

**Step 4.** In triangle BFE, the straight line AC is parallel to FE. Hence it cuts BF and BE proportionally:
BA : AF = BC : CE.
Substituting AF = CD gives
AB : CD = BC : CE (VI.2; I.34).

**Step 5.** In triangle EBF, the straight line CD is parallel to BF. Hence it cuts EB and EF proportionally:
BC : CE = FD : DE.
Substituting FD = AC gives
BC : CE = AC : DE (VI.2; I.34).

**Step 6.** The ratios AB : CD and AC : DE are both the same as BC : CE. Therefore
AB : CD = AC : DE (V.11).

**Step 7.** Applying alternation to the proportions in Steps 4, 5, and 6 gives, respectively,
AB : BC = CD : CE,
BC : AC = CE : DE,
AB : AC = CD : DE (V.16).
These are precisely the proportions between the sides about the three pairs of equal angles. The corresponding pairs are AB and CD, BC and CE, and AC and DE; each pair subtends a pair of equal angles. Thus, in equiangular triangles, the sides about the equal angles are proportional, and corresponding sides are those opposite the equal angles.

**USED:** 1.28, 1.32, 1.34, 5.11, 5.16, 6.2, CN4, CN5, P2, P5
**Human refs (from References field):** 1.17, 1.28, 1.34, 5.16, 5.22, 6.2, P5
**Jaccard:** 0.417 — AI adds ['1.32', '5.11', 'CN4', 'CN5', 'P2']; Human adds ['1.17', '5.22']

## Proposition 6.5
**Statement:** If two triangles have their sides proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let triangles ABC and DEF have corresponding sides AB, BC, CA and DE, EF, FD proportional. Thus AB:BC = DE:EF and AB:CA = DE:FD. We take the direct route of constructing an equiangular auxiliary triangle and then comparing its sides with those of DEF. On DE, construct rays at D and E, on the same side of DE, making angles equal respectively to ∠BAC and ∠ABC. [1.23]

**Step 2.** The angles ∠BAC and ∠ABC together are less than two right angles. Therefore the two constructed rays meet on the chosen side of DE; call their intersection G. We have ∠EDG = ∠BAC and ∠DEG = ∠ABC. [1.17, P5]

**Step 3.** The angles of each of triangles DEG and ABC sum to two right angles. Subtracting the two pairs of equal angles gives ∠DGE = ∠BCA. Hence these triangles are equiangular, with D corresponding to A, E to B, and G to C. [1.32, CN1, CN3]

**Step 4.** The corresponding sides of these equiangular triangles are proportional. Consequently,
AB:BC = DE:EG and AB:CA = DE:DG. [6.4]

**Step 5.** Comparing these proportions with the hypotheses gives
DE:EG = DE:EF and DE:DG = DE:FD.
Since magnitudes to which the same magnitude has the same ratio are equal, EG = EF and DG = FD. [5.11, 5.9]

**Step 6.** Triangles DEG and DEF now have their three corresponding sides equal: DE is common, EG = EF, and DG = DF. Side–side–side is the natural comparison here because all three side equalities are established. Applying it with each pair of sides as the containing sides gives ∠EDG = ∠EDF, ∠DEG = ∠DEF, and ∠DGE = ∠DFE. [1.8]

**Step 7.** Combining these angle equalities with those of Steps 2–3 yields ∠BAC = ∠EDF, ∠ABC = ∠DEF, and ∠BCA = ∠DFE. These equal angles are opposite the corresponding sides BC and EF, CA and FD, and AB and DE, respectively. Therefore the original triangles are equiangular, with equal angles subtended by corresponding sides, as required. [CN1]

**USED:** 1.17, 1.23, 1.32, 1.8, 5.11, 5.9, 6.4, CN1, CN3, P5
**Human refs (from References field):** 1.23, 1.32, 1.4, 1.8, 5.11, 5.9, 6.4
**Jaccard:** 0.545 — AI adds ['1.17', 'CN1', 'CN3', 'P5']; Human adds ['1.4']

## Proposition 6.6
**Statement:** If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular and will have those angles equal which the corresponding sides subtend.

**Step 1.** Let ABC and DEF be triangles such that ∠BAC = ∠EDF and AB:AC = DE:DF. We must prove ∠ABC = ∠DEF and ∠BCA = ∠DFE. Choose the direct route of constructing an auxiliary equiangular triangle. [Hypotheses]

**Step 2.** At E construct a ray on the same side of DE as F, making with ED an angle equal to ∠ABC. The angles BAC and ABC together are less than two right angles, since the three angles of ABC equal two right angles. Consequently, the constructed ray and the ray DF make interior angles on the same side of DE whose sum is less than two right angles. They therefore meet at a point G on that side. Thus ∠DEG = ∠ABC and ∠EDG = ∠EDF = ∠BAC. [1.23, 1.32, CN5, P5]

**Step 3.** The angle sums of triangles ABC and DEG are each two right angles. Subtracting their respective equal angles at A and D and at B and E gives ∠BCA = ∠DGE. Hence ABC and DEG are equiangular. [1.32, CN3]

**Step 4.** Apply VI.4, the earlier result that directly supplies proportional sides from equiangularity: AB:AC = DE:DG. Together with the hypothesis AB:AC = DE:DF, this gives DE:DG = DE:DF. Since the same magnitude DE has the same ratio to DG and DF, it follows that DG = DF. [6.4, 5.11, 5.9]

**Step 5.** In triangles DEG and DEF, DE is common, DG = DF, and the included angles EDG and EDF are equal, because DG and DF lie on the same ray. Therefore their remaining corresponding angles are equal: ∠DEG = ∠DEF and ∠DGE = ∠DFE. [1.4]

**Step 6.** Combining these equalities with Steps 2 and 3 yields ∠ABC = ∠DEF and ∠BCA = ∠DFE. Together with the given equality ∠BAC = ∠EDF, this proves that ABC and DEF are equiangular. Their equal angles are opposite the corresponding sides AB and DE, AC and DF, and BC and EF, respectively, as required. [CN1]

**USED:** 1.23, 1.32, 1.4, 5.11, 5.9, 6.4, CN1, CN3, CN5, P5
**Human refs (from References field):** 1.23, 1.32, 1.4, 5.11, 5.9, 6.4
**Jaccard:** 0.600 — AI adds ['CN1', 'CN3', 'CN5', 'P5']

## Proposition 6.7
**Statement:** If two triangles have one angle equal to one angle, the sides about other angles proportional, and the remaining angles either both less or both not less than a right angle, the triangles will be equiangular and will have those angles equal, the sides about which are proportional.

**Step 1.** Let ABC and DEF be triangles such that ∠BAC = ∠EDF and AB:BC = DE:EF, and suppose that ∠ACB and ∠DFE are either both less than a right angle or both not less than a right angle. If ∠ABC = ∠DEF, their remaining angles are equal by the triangle-angle sum, subtracting the equal angles. Thus it suffices to rule out ∠ABC ≠ ∠DEF. [1.32, CN3]

**Step 2.** Suppose these angles are unequal. Interchanging the triangles if necessary, take ∠ABC < ∠DEF. At E construct, inside ∠DEF, the angle ∠DEG equal to ∠ABC, with G on DF. This smaller-angle construction is chosen so that G lies between D and F. [1.23]

**Step 3.** Since G lies on DF, ∠EDG = ∠EDF = ∠BAC; also ∠DEG = ∠ABC by construction. Hence ∠DGE = ∠ACB by the triangle-angle sum and subtraction. The triangles ABC and DEG are therefore equiangular. The proportionality theorem for equiangular triangles applies directly and gives AB:BC = DE:EG. [1.32, CN3, 6.4]

**Step 4.** But AB:BC = DE:EF by hypothesis. Consequently DE:EG = DE:EF; and magnitudes to which the same magnitude has the same ratio are equal. Therefore EG = EF. [5.11, 5.9]

**Step 5.** In the isosceles triangle EGF, ∠EGF = ∠GFE. These two equal angles together are less than two right angles, so each is less than a right angle. Since G lies between D and F, ∠GFE = ∠DFE, making ∠DFE less than a right angle. On the other hand, ∠DGE and ∠EGF together equal two right angles, since GD and GF are opposite rays. Thus ∠DGE, and therefore ∠ACB, is greater than a right angle. [1.5, 1.17, 1.13]

**Step 6.** We have obtained one remaining angle less than a right angle and the other greater than a right angle, contrary to either permitted hypothesis. Hence ∠ABC = ∠DEF. Together with the given equality ∠BAC = ∠EDF, the triangle-angle sum now gives ∠ACB = ∠DFE. Therefore the triangles are equiangular, and in particular the angles about which the sides are proportional are equal. [1.32, CN3]

**USED:** 1.13, 1.17, 1.23, 1.32, 1.5, 5.11, 5.9, 6.4, CN3
**Human refs (from References field):** 1.13, 1.17, 1.23, 1.32, 1.5, 5.11, 5.9, 6.4
**Jaccard:** 0.889 — AI adds ['CN3']

## Proposition 6.8
**Statement:** If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.

**Step 1.** Let ABC be right-angled at A, and let AD be the perpendicular drawn from A to the base BC, with D on BC. Since AD is perpendicular to BC, the angles ADB and ADC are right angles; hence both equal the right angle BAC. [D1.10, P4]

**Step 2.** Since BD lies along BC, angle ABD is the same as angle ABC. The angle sums of triangles ABD and ABC are each two right angles. Subtracting their equal right angles and then their equal angles at B leaves angle BAD equal to angle ACB. Thus triangles ABD and ABC are equiangular, with correspondence A ↔ C, B ↔ B, D ↔ A. [1.32, CN3]

**Step 3.** Since CD lies along CB, angle ACD is the same as angle ACB. The angle sums of triangles ACD and ABC are each two right angles. Subtracting their equal right angles and then their equal angles at C leaves angle CAD equal to angle ABC. Thus triangles ACD and ABC are equiangular, with correspondence A ↔ B, C ↔ C, D ↔ A. [1.32, CN3]

**Step 4.** The two smaller triangles are also equiangular: angle BAD equals angle ACD, since both equal angle ACB; angle ABD equals angle CAD, since both equal angle ABC; and their angles at D are equal by Step 1. Their correspondence is therefore A ↔ C, B ↔ A, D ↔ D. [CN1]

**Step 5.** We take the direct equiangular route, applying 6.4 to each pair established above. In each pair, the sides about the corresponding equal angles are proportional. Together with the equality of the corresponding angles, this is precisely the definition of similar figures. Therefore the triangles adjoining the perpendicular are similar both to the whole triangle and to one another. [6.4, D6.1]

**USED:** 1.32, 6.4, CN1, CN3, D1.10, D6.1, P4
**Human refs (from References field):** 1.32, 6.4, D6.1
**Jaccard:** 0.429 — AI adds ['CN1', 'CN3', 'D1.10', 'P4']

## Proposition 6.9
**Statement:** From a given straight line to cut off a prescribed part.

**Step 1.** Let AB be the given straight line, and let the prescribed part be its nth part, where n ≥ 2 is a given integer. We must cut off a segment which, taken n times, equals AB; such a segment measures AB and is therefore a part of it. [D5.1]

**Step 2.** Draw an auxiliary straight line from A, not collinear with AB, and prolong it as necessary. Choose a point D on it. Starting with AD, mark off n consecutive equal segments along this line, obtaining points A = X₀, D = X₁, X₂, …, Xₙ = C. Each successive point is obtained by describing a circle centred at the preceding point with distance AD and taking its intersection with the forward continuation of the line. Thus AC consists of n segments each equal to AD, so AC = n·AD. [P1, P2, P3]

**Step 3.** Join CB. Through D draw a straight line parallel to CB, meeting AB at E. [P1, 1.31]

**Step 4.** Use the proportional-section theorem directly, since the constructed parallel immediately supplies its hypothesis; no passage through similar triangles is needed. In triangle CAB, DE is parallel to CB, so
CD : DA = BE : EA.
By composition,
(CD + DA) : DA = (BE + EA) : EA,
and hence
CA : AD = BA : AE. [6.2, 5.18]

**Step 5.** In this equality of ratios, take one copy of each antecedent and n copies of each consequent. Since CA = n·AD, the equality clause in the definition of equal ratios gives BA = n·AE. Consequently AE measures AB exactly n times: AE is the prescribed nth part of AB. Thus the required part has been cut off from the given straight line. [D5.5, D5.1]

**USED:** 1.31, 5.18, 6.2, D5.1, D5.5, P1, P2, P3
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.222 — AI adds ['5.18', 'D5.1', 'D5.5', 'P1', 'P2', 'P3']; Human adds ['1.3']

## Proposition 6.10
**Statement:** To cut a given uncut straight line similarly to a given cut straight line.

**Step 1.** Let the given cut straight line have successive points A₀, A₁, …, Aₙ, where A₀ and Aₙ are its endpoints, and let PQ be the given uncut straight line. From P draw an auxiliary ray not collinear with PQ. Extend it as necessary and successively cut off the given parts upon it, obtaining points X₀=P, X₁, …, Xₙ=R such that Xᵢ₋₁Xᵢ=Aᵢ₋₁Aᵢ for every i. Join RQ. These constructions use the drawing and extension postulates and the construction for cutting off a length equal to a given lesser length. [P1, P2, 1.3]

**Step 2.** Through each interior point Xᵢ draw a straight line parallel to RQ, meeting PQ at Yᵢ. Put Y₀=P and Yₙ=Q. The points Y₁, …, Yₙ₋₁ are the required candidate divisions of PQ. [1.31]

**Step 3.** Use the proportional-intercept theorem directly, since the construction consists of parallels cutting the sides of triangle PRQ. For each i with 1≤i<n, it gives
PXᵢ:XᵢR = PYᵢ:YᵢQ. [6.2]

**Step 4.** By composition, the preceding proportion gives
PR:XᵢR = PQ:YᵢQ.
Taking this proportion alternately gives
PR:PQ = XᵢR:YᵢQ.
Thus every corresponding pair of nonzero terminal portions has the same ratio as PR to PQ. [5.18, 5.16]

**Step 5.** For each i with 1≤i<n, consider the wholes Xᵢ₋₁R and Yᵢ₋₁Q and the parts XᵢR and YᵢQ to be subtracted from them. Both pairs have ratio PR:PQ by Step 4; when i=1, the wholes are PR and PQ themselves. Consequently, the ratio of whole to whole equals that of part subtracted to part subtracted. The theorem on remainders therefore gives
Xᵢ₋₁Xᵢ:Yᵢ₋₁Yᵢ = PR:PQ.
The final pair Xₙ₋₁R and Yₙ₋₁Q already has this ratio by Step 4. Hence every corresponding pair of individual parts has the same ratio. [5.11, 5.19]

**Step 6.** For any two indices i and j, Step 5 gives
Xᵢ₋₁Xᵢ:Yᵢ₋₁Yᵢ = Xⱼ₋₁Xⱼ:Yⱼ₋₁Yⱼ.
Taking this proportion alternately, and using the equal lengths constructed in Step 1, yields
Aᵢ₋₁Aᵢ:Aⱼ₋₁Aⱼ = Yᵢ₋₁Yᵢ:Yⱼ₋₁Yⱼ.
Thus the parts of PQ, in their given order, have exactly the same ratios to one another as the corresponding parts of the given cut line. Therefore PQ has been cut similarly to the given cut straight line, as required. [5.11, 5.16]

**USED:** 1.3, 1.31, 5.11, 5.16, 5.18, 5.19, 6.2, P1, P2
**Human refs (from References field):** 1.31, 1.34, 6.2
**Jaccard:** 0.200 — AI adds ['1.3', '5.11', '5.16', '5.18', '5.19', 'P1', 'P2']; Human adds ['1.34']

## Proposition 6.11
**Statement:** To two given straight lines to find a third proportional.

**Step 1.** Let the two given straight-line lengths, in their given order, be a and b. Take two rays from A not lying on the same straight line. On the first mark B and C, in the order A, B, C, so that AB = a and BC = b; on the second mark D so that AD = b. These lengths are obtained by producing the rays sufficiently and cutting off segments equal to the given lines. [P1, P2, 1.3]

**Step 2.** Join B to D. Through C draw a straight line parallel to BD, meeting AD produced beyond D at E. Thus BD is parallel to the side CE of triangle ACE. [P1, P2, 1.31]

**Step 3.** Since BD cuts the two sides of triangle ACE parallel to its remaining side, AB : BC = AD : DE. We use the parallel-cutting theorem directly because it gives the required ratios of successive segments, without a similarity argument. Substituting the constructed lengths gives a : b = b : DE. Therefore DE is a third proportional to the two given straight lines, as required. [6.2]

**USED:** 1.3, 1.31, 6.2, P1, P2
**Human refs (from References field):** 1.3, 1.31, 6.2
**Jaccard:** 0.600 — AI adds ['P1', 'P2']

## Proposition 6.12
**Statement:** To three given straight lines to find a fourth proportional.

**Step 1.** Let the three given straight lines, in their given order, have lengths a, b, and c. Draw two straight lines from O containing an angle, and produce them sufficiently far. On the first cut off OA = a and then AB = b, with O, A, B in that order. On the second cut off OC = c. [P1, P2, 1.3]

**Step 2.** Join AC. Through B draw a straight line parallel to AC, meeting the second line produced beyond C at E. We choose this direct parallel-line construction because the proportional-sections theorem gives exactly the required ratio. [P1, P2, 1.31]

**Step 3.** In triangle OBE, the straight line AC is parallel to the side BE. Therefore it cuts OB and OE proportionally:
OA : AB = OC : CE.
Since OA = a, AB = b, and OC = c, it follows that
a : b = c : CE.
Thus CE is a fourth proportional to the three given straight lines, as required. [6.2]

**USED:** 1.3, 1.31, 6.2, P1, P2
**Human refs (from References field):** 1.31, 6.2
**Jaccard:** 0.400 — AI adds ['1.3', 'P1', 'P2']

## Proposition 6.13
**Statement:** To two given straight lines to find a mean proportional.

**Step 1.** Let AB be the first given straight line. Produce AB beyond B sufficiently far, and cut off BC on the produced part equal to the second given straight line. Thus A, B, C lie in this order on one straight line. [P2, 1.3]

**Step 2.** Bisect AC at O, and describe the circle with centre O and radius OA. Since OA = OC, AC is a diameter. Take the semicircle on one side of AC. [1.10, P3]

**Step 3.** Draw a perpendicular to AC at B, producing it on the chosen side to meet the semicircle at D. Join AD and DC. [1.11, P2, P1]

**Step 4.** Since ADC is an angle in a semicircle, it is a right angle. Hence triangle ADC is right-angled at D, and DB is its perpendicular to the hypotenuse AC. We therefore use VI.8 directly: it applies to exactly this configuration and gives the similarity of the two triangles adjoining DB. Thus triangles ABD and DBC are similar, with A, B, D corresponding respectively to D, B, C. [3.31, 6.8]

**Step 5.** The corresponding sides of these similar triangles are proportional. In particular, AB corresponds to DB, and BD corresponds to BC; therefore
AB : BD = BD : BC.
Consequently BD is a mean proportional between AB and BC, which are equal to the two given straight lines. The required mean proportional has therefore been found. [D6.1]

**USED:** 1.10, 1.11, 1.3, 3.31, 6.8, D6.1, P1, P2, P3
**Human refs (from References field):** 3.31, 6.8
**Jaccard:** 0.222 — AI adds ['1.10', '1.11', '1.3', 'D6.1', 'P1', 'P2', 'P3']

## Proposition 6.14
**Statement:** In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are reciprocally proportional are equal.

**Step 1.** Let the two equiangular parallelograms be OABC and ODEF, with equal angles AOC and DOF. Place these equal angles together, so that OA and OD lie on one ray, and OC and OF on another. This placement changes neither lengths nor areas, since each figure coincides with its original upon superposition. Write P and Q for their respective areas. [CN4]

**Step 2.** Complete the parallelogram OAGF on the sides OA and OF: through A draw the parallel to OF, and through F the parallel to OA, meeting at G. Write R for its area. We use this auxiliary parallelogram as a common comparator, so that the same-height theorem applies directly to both given parallelograms. [1.31]

**Step 3.** The parallelograms OAGF and OABC, taken on bases OF and OC, lie between the same parallels: the line OCF and the line ABG. Similarly, OAGF and ODEF, taken on bases OA and OD, lie between the line OAD and the line FGE. Therefore the ratios of their areas are the ratios of their bases:
R:P = OF:OC, and R:Q = OA:OD. [6.1]

**Step 4.** First suppose that the given parallelograms are equal, so P = Q. The same magnitude R has the same ratio to these equal magnitudes; hence R:P = R:Q. Combining this with Step 3 gives
OA:OD = OF:OC.
Thus a side of the first parallelogram is to the corresponding side of the second as the other side of the second is to the other side of the first. The sides about the equal angles are therefore reciprocally proportional. [5.7, 5.11, D6.2]

**Step 5.** Conversely, suppose that the sides about the equal angles are reciprocally proportional, so
OA:OD = OF:OC.
By the two ratios in Step 3, it follows that R:P = R:Q. Magnitudes to which the same magnitude has the same ratio are equal; hence P = Q. Therefore the two parallelograms are equal. Both assertions are proved. [D6.2, 5.11, 5.9]

**USED:** 1.31, 5.11, 5.7, 5.9, 6.1, CN4, D6.2
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.500 — AI adds ['1.31', 'CN4', 'D6.2']; Human adds ['1.14']

## Proposition 6.15
**Statement:** In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal.

**Step 1.** Let ABC and DEF be triangles with ∠BAC = ∠EDF. Write [UVW] for the area of triangle UVW. We use one auxiliary triangle, so that the ratios can be obtained directly from triangles of the same height. Produce AB and AC as necessary, and take X on the ray AB and Y on the ray AC such that AX = DE and AY = DF, cutting off the required lengths (or retaining the existing endpoints when the lengths already agree). Join XY and XC. [P2, 1.3, P1]

**Step 2.** Since AX = DE, AY = DF, and ∠XAY = ∠EDF, the triangles AXY and DEF are equal by the side-angle-side proposition. Thus [AXY] = [DEF]. [1.4]

**Step 3.** Triangles ABC and AXC have their bases AB and AX on the same straight line and have the common vertex C; hence they have the same height. Similarly, triangles AXY and AXC have their bases AY and AC on the same straight line and have the common vertex X. Therefore
[ABC] : [AXC] = AB : AX,
and
[AXY] : [AXC] = AY : AC. [6.1]

**Step 4.** First suppose that [ABC] = [DEF]. By Step 2, [ABC] = [AXY]. Equal magnitudes have the same ratio to the same magnitude, so
[ABC] : [AXC] = [AXY] : [AXC].
Combining this with Step 3 gives AB : AX = AY : AC. Since AX = DE and AY = DF, it follows that
AB : DE = DF : AC.
Thus the sides about the equal angles are reciprocally proportional. [CN1, 5.7, 5.11, D6.2]

**Step 5.** Conversely, suppose that the sides about the equal angles are reciprocally proportional, namely AB : DE = DF : AC. Substituting AX = DE and AY = DF gives AB : AX = AY : AC. The two proportions in Step 3 therefore yield
[ABC] : [AXC] = [AXY] : [AXC].
Magnitudes having the same ratio to the same magnitude are equal; hence [ABC] = [AXY]. Together with Step 2 this gives [ABC] = [DEF]. Therefore the triangles are equal, proving both assertions. [D6.2, 5.11, 5.9, CN1]

**USED:** 1.3, 1.4, 5.11, 5.7, 5.9, 6.1, CN1, D6.2, P1, P2
**Human refs (from References field):** 1.14, 5.11, 5.7, 5.9, 6.1
**Jaccard:** 0.364 — AI adds ['1.3', '1.4', 'CN1', 'D6.2', 'P1', 'P2']; Human adds ['1.14']

## Proposition 6.16
**Statement:** If four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes be equal to the rectangle contained by the means, the four straight lines will be proportional.

**Step 1.** Let the four given straight lines, in their stated order, be a, b, c, d. Construct a parallelogram R with adjacent perpendicular sides a, d, and a parallelogram S with adjacent perpendicular sides b, c. For each construction, erect a perpendicular at an endpoint of the first side, produce it sufficiently, cut off the prescribed second side, and complete the parallelogram by drawing parallels. [1.11, P2, 1.3, 1.31]

**Step 2.** The angles of both parallelograms are right angles, by the angle properties of parallel lines; hence R and S are equiangular. They are respectively the rectangles contained by a, d and by b, c. [1.29, P4, D2.1] We take the direct route through 6.14: its reciprocal-side criterion for equiangular parallelograms supplies both required implications. [6.14]

**Step 3.** Suppose the four straight lines are proportional, so that a:b = c:d. [D5.6] Here a and d are the sides about a right angle of R, while b and c are the sides about a right angle of S. Thus the ratio of the first side of R to the first side of S equals the ratio of the second side of S to the second side of R: their sides about equal angles are reciprocally proportional. Therefore R and S are equal by 6.14. Consequently, the rectangle contained by the extremes a, d equals the rectangle contained by the means b, c. [6.14]

**Step 4.** Conversely, suppose the rectangle contained by a, d equals the rectangle contained by b, c. Then R and S are equal and equiangular. By the other implication of 6.14, their sides about equal angles are reciprocally proportional; with the same pairing of sides, this gives a:b = c:d. Hence the four straight lines, in their stated order, are proportional. Both assertions are proved. [6.14, D5.6]

**USED:** 1.11, 1.29, 1.3, 1.31, 6.14, D2.1, D5.6, P2, P4
**Human refs (from References field):** 6.14
**Jaccard:** 0.111 — AI adds ['1.11', '1.29', '1.3', '1.31', 'D2.1', 'D5.6', 'P2', 'P4']

## Proposition 6.17
**Statement:** If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to the square on the mean, the three straight lines will be proportional.

**Step 1.** Let the three straight lines, in order, be A, B, C. Their being proportional means that A:B = B:C [D5.6]. Write R(X,Y) for the rectangle contained by X,Y, and S(B) for the square on B. A square on B is precisely the rectangle contained by B,B, so R(B,B) = S(B) [D2.1, D1.22]. We use 6.16 directly, taking B as both means, because it already supplies both required implications.

**Step 2.** Suppose A, B, C are proportional. Then A:B = B:C, so the four straight lines A, B, B, C are proportional [D5.6]. By 6.16, the rectangle contained by their extremes equals the rectangle contained by their means: R(A,C) = R(B,B). Thus R(A,C) = S(B) [6.16, D2.1, D1.22].

**Step 3.** Conversely, suppose R(A,C) = S(B). Since S(B) is R(B,B), the rectangle contained by the extremes of A, B, B, C equals the rectangle contained by their means [D2.1, D1.22]. The converse of 6.16 therefore gives A:B = B:C. Hence A, B, C are proportional [6.16, D5.6]. Both assertions are proved.

**USED:** 6.16, D1.22, D2.1, D5.6
**Human refs (from References field):** 6.16
**Jaccard:** 0.250 — AI adds ['D1.22', 'D2.1', 'D5.6']

## Proposition 6.18
**Statement:** On a given straight line to describe a rectilineal figure similar and similarly situated to a given rectilineal figure.

**Step 1.** Let the given straight line be AB, and let the given rectilineal figure have successive vertices C₁, C₂, …, Cₙ. Take C₁C₂ as the side to which AB is to correspond. Draw diagonals dissecting the given figure into triangles, without adding interior vertices. Begin with the triangle incident to C₁C₂ and order the remaining triangles so that each is attached along a diagonal of a triangle already taken. We shall copy this triangular dissection, preserving the corresponding sides of attachment. [P1]

**Step 2.** First establish the triangle construction to be used repeatedly. Given a triangle UVW and a straight line XY corresponding to UV, construct at X an angle with XY equal to ∠VUW, and at Y an angle with YX equal to ∠UVW, taking both angles on the chosen side of XY. This is possible by 1.23. The two prescribed angles together are less than two right angles, since the three angles of UVW equal two right angles. Consequently, the constructed rays, produced if necessary, meet at a point Z on that side. The remaining angle ∠XZY equals ∠UWV, by subtracting the equal pairs of angles from two right angles. Thus XYZ is equiangular with UVW, with X, Y, Z corresponding respectively to U, V, W. [1.23, 1.32, P2, P5, CN3]

**Step 3.** Apply Step 2 on AB to copy the first triangle of the dissection. Whenever a triangle of the original dissection adjoins one already copied, construct its equiangular copy on the corresponding diagonal already obtained, placing it on the corresponding side of that diagonal. Continue until all triangles have been copied. Each new triangle is attached along its already constructed side, so the copies have the same incidences and order of attachment as the original triangles. Denote the resulting boundary vertices by A₁, A₂, …, Aₙ, where A₁ = A and A₂ = B. Each copied triangle is equiangular with its corresponding original triangle. [1.23, 1.32, P2, P5, CN3]

**Step 4.** At each vertex, the angle of the original figure is composed of the angles of the triangles incident to that vertex. The corresponding copied triangular angles are individually equal and occur in the same order. Adding these equal angles therefore gives equality of the corresponding angles of the two rectilineal figures. [CN2]

**Step 5.** Use 6.4 directly: it is the earlier result naturally applicable to the equiangular triangles just constructed, and supplies their corresponding side ratios without a separate proportional-length construction. To compare any two boundary sides s and t of the original figure, take a sequence of sides of the dissection
s = e₀, e₁, …, eₘ = t,
such that each consecutive pair belongs to one triangle. Let e′₀, e′₁, …, e′ₘ be their corresponding copied sides. For every consecutive pair, 6.4 gives
eᵢ : eᵢ₊₁ = e′ᵢ : e′ᵢ₊₁.
Hence, ex aequali,
s : t = s′ : t′.
In particular, the sides about every pair of corresponding equal boundary angles are proportional. [6.4, 5.22]

**Step 6.** The constructed figure A₁A₂…Aₙ has its angles severally equal to those of C₁C₂…Cₙ and its corresponding sides proportional. It is therefore similar to the given rectilineal figure. The preserved order of vertices and corresponding sides of attachment make it similarly situated, with A₁A₂ = AB as its prescribed side. Thus, on the given straight line, a rectilineal figure similar and similarly situated to the given rectilineal figure has been described. [D6.1]

**USED:** 1.23, 1.32, 5.22, 6.4, CN2, CN3, D6.1, P1, P2, P5
**Human refs (from References field):** 1.23, 1.32, 6.4, D6.1
**Jaccard:** 0.400 — AI adds ['5.22', 'CN2', 'CN3', 'P1', 'P2', 'P5']

## Proposition 6.19
**Statement:** Similar triangles are to one another in the duplicate ratio of the corresponding sides.

**Step 1.** Let ABC and DEF be similar triangles, with A, B, C corresponding respectively to D, E, F. Choose BC and EF as the corresponding sides under consideration. By the definition of similarity, ∠ABC = ∠DEF and AB:BC = DE:EF (D6.1). Alternating gives AB:DE = BC:EF (5.16). Thus we use the defining proportions of similarity directly.

**Step 2.** Choose the third-proportional route, which will allow the reciprocal-sides criterion for equal triangles to apply. Construct a length t such that BC:EF = EF:t (6.11). Produce BC to L so that BL is longer than t (P2), and cut off BG = t from BL (1.3). Thus G lies on the ray BC and BC:EF = EF:BG. Join AG (P1).

**Step 3.** From Steps 1 and 2, AB:DE = EF:BG (5.11). Also, because G lies on the ray BC, ∠ABG = ∠ABC = ∠DEF. Therefore the sides about the equal angles of triangles ABG and DEF are reciprocally proportional. The triangles are consequently equal in area (6.15).

**Step 4.** Triangles ABC and ABG have their bases BC and BG on the same straight line and have the same vertex A; hence they have the same height. They are therefore to one another as their bases:
[ABC]:[ABG] = BC:BG (6.1),
where brackets denote triangle areas.

**Step 5.** Since [ABG] = [DEF], the same magnitude [ABC] has the same ratio to each of them (5.7). Combining this with Step 4 gives
[ABC]:[DEF] = BC:BG (5.11).

**Step 6.** The three lengths BC, EF, BG are proportional by Step 2. Therefore BC:BG is, by definition, the duplicate ratio of BC:EF (D5.9). By Step 5, triangle ABC is consequently to triangle DEF in the duplicate ratio of BC to EF. Since BC and EF were an arbitrary pair of corresponding sides, similar triangles are to one another in the duplicate ratio of their corresponding sides.

**USED:** 1.3, 5.11, 5.16, 5.7, 6.1, 6.11, 6.15, D5.9, D6.1, P1, P2
**Human refs (from References field):** 5.11, 5.16, 6.1, 6.11, 6.15, D5.11, D5.9
**Jaccard:** 0.500 — AI adds ['1.3', '5.7', 'D6.1', 'P1', 'P2']; Human adds ['D5.11']

## Proposition 6.20
**Statement:** Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate of that which the corresponding side has to the corresponding  side.

**Step 1.** Let the similar polygons be A₁A₂…Aₙ and B₁B₂…Bₙ, with vertices listed in corresponding order. Their corresponding angles are equal, and the sides about those angles are proportional. By alternation, and equality of ratios equal to the same ratio, all corresponding sides have a common ratio, say r:
A₁A₂:B₁B₂ = A₂A₃:B₂B₃ = ⋯ = AₙA₁:BₙB₁ = r. [D6.1, 5.16, 5.11]

**Step 2.** Join A₁ and B₁ to the respective nonadjacent vertices. Denote the resulting triangles by
Tᵢ = △A₁AᵢAᵢ₊₁ and Uᵢ = △B₁BᵢBᵢ₊₁, for i = 2,…,n−1.
These divide the respective polygons into n−2 triangles each, so their multitudes are equal. We use these corresponding fans and the included-angle criterion: the given similarity supplies precisely the equal angles and proportional adjacent sides needed for that direct route. [P1]

**Step 3.** In T₂ and U₂, the angles at A₂ and B₂ are equal, and
A₁A₂:A₂A₃ = B₁B₂:B₂B₃.
Therefore these triangles are equiangular by the included-angle criterion, and their corresponding sides are proportional; hence they are similar. In particular, by alternation,
A₁A₃:B₁B₃ = A₁A₂:B₁B₂ = r. [6.6, 6.4, D6.1, 5.16]

**Step 4.** Continue successively through the fans. Suppose Tᵢ₋₁ and Uᵢ₋₁ have been proved similar and A₁Aᵢ:B₁Bᵢ = r. Subtract their equal angles at Aᵢ and Bᵢ from the equal polygon angles at those vertices. The remaining angles are equal:
∠A₁AᵢAᵢ₊₁ = ∠B₁BᵢBᵢ₊₁.
Moreover,
A₁Aᵢ:B₁Bᵢ = AᵢAᵢ₊₁:BᵢBᵢ₊₁,
so alternation gives
A₁Aᵢ:AᵢAᵢ₊₁ = B₁Bᵢ:BᵢBᵢ₊₁.
Thus Tᵢ and Uᵢ are equiangular by the included-angle criterion and have proportional corresponding sides, so they too are similar. Their side proportions also give A₁Aᵢ₊₁:B₁Bᵢ₊₁ = r. Repeating this argument proves that every corresponding pair Tᵢ, Uᵢ is similar. [CN3, 5.11, 5.16, 6.6, 6.4, D6.1]

**Step 5.** Similar triangles have the duplicate ratio of their corresponding sides. Consequently, for every i, Tᵢ:Uᵢ is the duplicate ratio of AᵢAᵢ₊₁:BᵢBᵢ₊₁, which is r. Thus all the corresponding triangle-pairs have the same ratio, namely the duplicate ratio of r. [6.19, 5.11]

**Step 6.** Since these triangle-pairs are proportional, any one antecedent is to its consequent as the sum of all the antecedents is to the sum of all the consequents. The sums are precisely the two polygons. Hence, for every i,
Tᵢ:Uᵢ = (A₁A₂…Aₙ):(B₁B₂…Bₙ).
The polygons therefore have the duplicate ratio of r, the ratio of any corresponding sides. They have also been divided into similar triangles, equal in multitude, each corresponding pair having the same ratio as the whole polygons. This proves all the assertions. [5.12]

**USED:** 5.11, 5.12, 5.16, 6.19, 6.4, 6.6, CN3, D6.1, P1
**Human refs (from References field):** 1.32, 5.12, 5.22, 6.1, 6.19, 6.4, 6.6, D6.1
**Jaccard:** 0.417 — AI adds ['5.11', '5.16', 'CN3', 'P1']; Human adds ['1.32', '5.22', '6.1']

## Proposition 6.21
**Statement:** Figures which are similar to the same rectilineal figure are also similar to one another.

**Step 1.** Let F and G be rectilineal figures each similar to the same rectilineal figure H. Match the vertices and sides of F and G through their given correspondences with H. We take the direct route through the definition of similarity: equality of corresponding angles and proportionality of the sides about them. [D6.1]

**Step 2.** Each angle of F equals its corresponding angle of H, and the corresponding angle of G equals that same angle of H. Therefore the corresponding angles of F and G are equal, since things equal to the same thing are equal to one another. [D6.1, CN1]

**Step 3.** At any corresponding vertices, let the two adjacent sides be f₁, f₂ in F; g₁, g₂ in G; and h₁, h₂ in H, listed in corresponding order. The given similarities imply
f₁ : f₂ = h₁ : h₂ and g₁ : g₂ = h₁ : h₂.
Apply the theorem on ratios equal to the same ratio directly: f₁ : f₂ = g₁ : g₂. Since the corresponding vertices were arbitrary, the sides about all corresponding equal angles of F and G are proportional. [D6.1, 5.11]

**Step 4.** Thus F and G have their corresponding angles severally equal and the sides about those angles proportional. By the definition, F and G are similar. Therefore figures which are similar to the same rectilineal figure are also similar to one another. [D6.1]

**USED:** 5.11, CN1, D6.1
**Human refs (from References field):** D6.1
**Jaccard:** 0.333 — AI adds ['5.11', 'CN1']

## Proposition 6.22
**Statement:** If four straight lines be proportional, the rectilineal figures similar and similarly described upon them will also be proportional; and, if the rectilineal figures similar and similarly described upon them be proportional, the straight lines will themselves also be proportional.

**Step 1.** Let the four straight lines be a, b, c, d. Let P and Q be similar rectilineal figures similarly described on a and b, and let R and S be similar rectilineal figures similarly described on c and d, with these sides corresponding. We use the duplicate-ratio statement of VI.20 directly, since the figures are general rectilineal figures. [6.20]

**Step 2.** Construct third proportionals x and y so that
 a:b = b:x and c:d = d:y.
By the definition of duplicate ratio, a:x is the duplicate ratio of a:b, and c:y is the duplicate ratio of c:d. Consequently,
 P:Q = a:x and R:S = c:y. [6.11, D5.9, 6.20]

**Step 3.** First suppose a:b = c:d. The proportions in Step 2 then give b:x = d:y. Applying ex aequali to the triples a, b, x and c, d, y gives a:x = c:y. Hence P:Q = R:S. This proves the forward implication. [5.11, 5.22]

**Step 4.** Conversely, suppose P:Q = R:S. Step 2 gives a:x = c:y. Construct a fourth proportional e such that a:b = c:e, and then a third proportional z such that c:e = e:z. [5.11, 6.12, 6.11]

**Step 5.** Since b:x = a:b = c:e = e:z, ex aequali gives a:x = c:z. Together with a:x = c:y, this yields c:y = c:z. Magnitudes to which the same magnitude has the same ratio are equal; therefore y = z. Thus c:e = e:y, while the original construction gives c:d = d:y. [5.11, 5.22, 5.9]

**Step 6.** If e>d, then e:y>d:y and c:d>c:e. Using c:e = e:y and d:y = c:d, these inequalities give respectively c:e>d:y and d:y>c:e, a contradiction. Interchanging d and e likewise excludes e<d. Therefore e=d. [5.8, 5.13]

**Step 7.** Substituting e=d into the fourth-proportional relation constructed in Step 4 gives a:b = c:d. Thus the straight lines are proportional if and only if the similar rectilineal figures similarly described upon the corresponding pairs are proportional, as required. [6.12; Steps 3–6]

**USED:** 5.11, 5.13, 5.22, 5.8, 5.9, 6.11, 6.12, 6.20, D5.9
**Human refs (from References field):** 5.11, 5.22, 5.9, 6.11, 6.12, 6.18, 6.19
**Jaccard:** 0.455 — AI adds ['5.13', '5.8', '6.20', 'D5.9']; Human adds ['6.18', '6.19']

## Proposition 6.23
**Statement:** Equiangular parallelograms have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let the given equiangular parallelograms be ABCD and AEFG, placed with their equal angles at A, so that AB and AE lie on the same ray, and AD and AG lie on the same ray. This placement does not change either figure or its area. Write [P] for the area of a figure P. [CN4]

**Step 2.** Form the intermediate parallelogram AEHD by drawing through E a parallel to AD and through D a parallel to AE, meeting at H. Thus it has one adjacent side from each given parallelogram. We use this direct common-height construction because it permits two immediate applications of the earlier base-ratio theorem. [1.31]

**Step 3.** ABCD and AEHD have bases AB and AE on the same straight line and lie between the same parallels. Likewise, AEHD and AEFG, regarded as standing on AD and AG, lie between the same parallels. Consequently,
[ABCD] : [AEHD] = AB : AE,
and
[AEHD] : [AEFG] = AD : AG. [6.1]

**Step 4.** Construct a fourth proportional segment t to AD, AG, and AE, so that
AD : AG = AE : t. [6.12]
The second ratio in Step 3 therefore gives
[AEHD] : [AEFG] = AE : t. [5.11]
Combining this with the first ratio in Step 3, ex aequali yields
[ABCD] : [AEFG] = AB : t. [5.22]

**Step 5.** By the definition of compounded ratio, AB : t is compounded of the successive ratios AB : AE and AE : t: their sizes multiply to the size of AB : t. Since AE : t = AD : AG, this is precisely the ratio compounded of AB : AE and AD : AG. These are the ratios of the corresponding sides about the equal angles of the given parallelograms. Therefore equiangular parallelograms have to one another the ratio compounded of the ratios of their sides. [D6.5]

**USED:** 1.31, 5.11, 5.22, 6.1, 6.12, CN4, D6.5
**Human refs (from References field):** 5.11, 6.1, 6.12
**Jaccard:** 0.429 — AI adds ['1.31', '5.22', 'CN4', 'D6.5']

## Proposition 6.24
**Statement:** In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.

**Step 1.** Let ABCD be a parallelogram with diameter AC. Label the two parallelograms about this diameter AGPE and PFCH, where P lies on AC, G lies on AB, E on AD, F on BC, and H on CD. Thus GP is parallel to BC, and PF is parallel to AB. By the equal angles made with parallel lines, triangles AGP and PFC are each equiangular with triangle ABC, in the indicated vertex orders (1.29).

**Step 2.** Use these equiangular triangles directly, since they give the required adjacent-side proportions. By 6.4,
AG:GP = AB:BC, and GP:AG = BC:AB;
PF:FC = AB:BC, and FC:PF = BC:AB.

**Step 3.** The angles of AGPE are respectively equal to those of ABCD: the angle at A is common, the angle at G equals the angle at B by parallelism, and the remaining equalities follow from equality of opposite angles in parallelograms. Likewise, the angles of PFCH are respectively equal to those of ABCD: the angle at C is common, the angle at F equals the angle at B by parallelism, and opposite angles give the remaining equalities (1.29, 1.34).

**Step 4.** Opposite sides of each parallelogram are equal (1.34). Consequently, the proportions from Step 2 give
AG:GP = AB:BC,
GP:PE = BC:CD,
PE:EA = CD:DA,
EA:AG = DA:AB.
Indeed, substitute PE = AG, EA = GP, CD = AB, and DA = BC into the proportions of Step 2. Similarly, substituting CH = PF and HP = FC gives
PF:FC = AB:BC,
FC:CH = BC:CD,
CH:HP = CD:DA,
HP:PF = DA:AB.
Thus both smaller parallelograms have their sides about corresponding equal angles proportional to those of the whole (6.4, 1.34).

**Step 5.** Each smaller parallelogram is therefore equiangular with ABCD and has the sides about equal angles proportional. Hence AGPE and PFCH are each similar to ABCD, by the definition of similar rectilineal figures (D6.1).

**Step 6.** Figures similar to the same rectilineal figure are similar to one another (6.21). Therefore AGPE and PFCH are also similar to one another. Thus, in any parallelogram, the parallelograms about the diameter are similar both to the whole and to one another.

**USED:** 1.29, 1.34, 6.21, 6.4, D6.1
**Human refs (from References field):** 5.16, 5.18, 5.22, 6.2, 6.21, D6.1
**Jaccard:** 0.222 — AI adds ['1.29', '1.34', '6.4']; Human adds ['5.16', '5.18', '5.22', '6.2']

## Proposition 6.25
**Statement:** To construct one and the same figure similar to a given rectilineal figure and equal to another given rectilineal figure.

**Step 1.** Let F be the given rectilineal figure to which the required figure must be similar, and let G be the given rectilineal figure to which it must be equal. Construct squares S and T equal to F and G respectively, and denote their sides by a and b. [2.14] The squares are similar: their angles are equal right angles, and their corresponding sides have throughout the ratio a:b. [D1.22, P4, D6.1] Choose this equal-square route because the resulting proportion of sides can be used directly in the proportional-figure theorem VI.22.

**Step 2.** Choose a side c of F. Find a fourth proportional d to a, b, c, so that a:b = c:d. [6.12]

**Step 3.** On d construct a rectilineal figure H similar and similarly situated to F, with d corresponding to c. Thus H has the required similarity. [6.18]

**Step 4.** The four straight lines a, b, c, d are proportional. The squares S and T are similar figures described on the first pair, and F and H are similar and similarly situated figures on the second pair. Therefore S:T = F:H. [6.22] Since S equals F, we also have S:T = F:T. [5.7] Hence F:T = F:H. [5.11] Magnitudes to which the same magnitude has the same ratio are equal; consequently T equals H. [5.9]

**Step 5.** Since T equals G and H equals T, H equals G. [CN1] Thus the constructed figure H is both similar to the given figure F and equal to the other given figure G, as required.

**USED:** 2.14, 5.11, 5.7, 5.9, 6.12, 6.18, 6.22, CN1, D1.22, D6.1, P4
**Human refs (from References field):** 1.44, 1.45, 5.16, 6.1, 6.13, 6.18, 6.19
**Jaccard:** 0.059 — AI adds ['2.14', '5.11', '5.7', '5.9', '6.12', '6.22', 'CN1', 'D1.22', 'D6.1', 'P4']; Human adds ['1.44', '1.45', '5.16', '6.1', '6.13', '6.19']

## Proposition 6.26
**Statement:** If from a parallelogram there be taken away a parallelogram similar and similarly situated to the whole and having a common angle with it, it is about the same diameter with the whole.

**Step 1.** Let ABCD be the whole parallelogram and AEFG the parallelogram taken away, with vertices named in corresponding order. Let their common angle be at A, so that E lies on AB and G lies on AD. Draw their diameters AC and AF. [P1]

**Step 2.** Since the parallelograms are similar and similarly situated, their corresponding angles are equal and the sides about those angles proportional. Hence ∠ABC = ∠AEF and AB:BC = AE:EF. [D6.1]

**Step 3.** Apply VI.6 directly to triangles ABC and AEF: this is the natural route because Step 2 supplies precisely an equal included angle and proportional adjacent sides. The triangles are therefore equiangular, with corresponding angles equal; in particular, ∠BAC = ∠EAF. [6.6]

**Step 4.** Since AE and AB are the same ray, this equality forces AC and AF to be the same ray. Indeed, C and F lie on the same side of AB; if the rays AC and AF were distinct, one of the two equal angles would be a proper part of the other, contrary to the whole being greater than the part. Thus A, F, and C are collinear. Since the removed parallelogram lies within the whole, its diameter AF lies on AC. Therefore the removed parallelogram is about the same diameter as the whole. [CN5]

**USED:** 6.6, CN5, D6.1, P1
**Human refs (from References field):** 1.31, 5.11, 5.9, 6.24
**Jaccard:** 0.000 — AI adds ['6.6', 'CN5', 'D6.1', 'P1']; Human adds ['1.31', '5.11', '5.9', '6.24']

## Proposition 6.27
**Statement:** Of all the parallelograms applied to the same straight line and deficient by parallelogrammic figures similar and similarly situated to that described on the half of the straight line, that parallelogram is greatest which is applied to the half of the straight line and is similar to the defect.

**Step 1.** Let E be the midpoint of AB, and let EBCF be the prescribed parallelogram on the half EB. Through A draw AD parallel to EF, meeting CF produced at D, so that ABCD is a parallelogram (1.31, P2). The parallelograms AEFD and EBCF have equal corresponding sides and angles, and therefore are similar and similarly situated (1.34, 1.29, D6.1). Moreover, DF = FC, and their areas are equal because they stand on the equal bases AE and EB between the same parallels (1.34, 1.36). Write [PQRS] for the area of a parallelogram PQRS; thus [AEFD] = [EBCF].

**Step 2.** Let AXYZ be any parallelogram applied to AB and deficient by a parallelogram XBWY similar and similarly situated to EBCF. Here X lies between A and B, W lies on the ray BC, Z lies on the ray AD, and Z, Y, W are collinear on a parallel to AB. By similarity, XB:BW = EB:BC. Consequently, if X lies between E and B, then W lies between B and C; if X lies between A and E, then W lies beyond C; and if X = E, then W = C (D6.1, CN5, 5.14).

**Step 3.** If X = E, the application coincides with AEFD and has the same area (CN4). Otherwise, the smaller of the two similar defects EBCF and XBWY lies inside the larger and shares its angle at B. Proposition 6.26 directly matches these hypotheses, so we choose its common-diameter route: the defects are about the same diameter, and hence B, F, Y are collinear (6.26).

**Step 4.** First suppose X lies between E and B. Put H = ZW ∩ EF, and let XY produced meet FC at J (P2). Since Y lies on the diameter BF of EBCF, the parallelograms EXYH and YWCJ are its complements. Therefore [EXYH] = [YWCJ] (1.43). Also, AEHZ and EBWH stand on the equal bases AE and EB between the same parallels, so [AEHZ] = [EBWH] (1.36).

**Step 5.** Adding the equal areas from Step 4 and using the indicated subdivisions gives
[AXYZ] + [HYJF]
= [AEHZ] + [EXYH] + [HYJF]
= [EBWH] + [YWCJ] + [HYJF]
= [EBCF]
= [AEFD]
(CN2, CN1).
The parallelogram HYJF is nondegenerate. Thus AXYZ is equal to a proper part of EBCF, and consequently [AXYZ] < [AEFD] (CN5).

**Step 6.** Now suppose X lies between A and E. Put J = XY ∩ DF, and let EF produced meet ZW at T (P2). Since F lies on the diameter BY of XBWY, the parallelograms XEFJ and FCWT are its complements; hence [XEFJ] = [FCWT] (1.43). But DF = FC by Step 1, so DFTZ and FCWT, standing on these equal bases between the same parallels DC and ZW, are equal (1.36). Therefore [XEFJ] = [DFTZ] (CN1).

**Step 7.** Subdividing and substituting the equality from Step 6, we obtain
[AEFD]
= [AXJD] + [XEFJ]
= [AXJD] + [DFTZ]
= [AXYZ] + [JFTY]
(CN2, CN1).
The parallelogram JFTY is nondegenerate, so again [AXYZ] < [AEFD] (CN5). Thus every application distinct from the half-line application has smaller area, while the application at X = E coincides with it. Therefore, of all the stated deficient parallelograms applied to AB, the greatest is AEFD, which is applied to the half AE and is similar to its defect EBCF.

**USED:** 1.29, 1.31, 1.34, 1.36, 1.43, 5.14, 6.26, CN1, CN2, CN4, CN5, D6.1, P2
**Human refs (from References field):** 1.36, 1.43, 6.26
**Jaccard:** 0.231 — AI adds ['1.29', '1.31', '1.34', '5.14', 'CN1', 'CN2', 'CN4', 'CN5', 'D6.1', 'P2']

## Proposition 6.28
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and deficient by a parallelogrammic figure similar to a given one: thus the given rectilineal figure must not be greater than the parallelogram described on the half of the straight line and similar to the defect.

**Step 1.** Let AB be the given straight line, F the given rectilineal figure, and G the parallelogram to which the defect must be similar. Write |K| for the area of a figure K. We use the excess-and-equal-complements construction. Bisect AB at M, and on MB describe the parallelogram P = MBCD similar and similarly situated to G. Through A draw AE parallel to MD, meeting CD produced at E. Thus ABCE is a parallelogram, divided into AMDE and MBCD. Since AM = MB, these two halves are equal, being on equal bases and between the same parallels. The hypothesis is |F| ≤ |P|. [1.10, 6.18, 1.31, P2, 1.36]

**Step 2.** If |F| = |P|, the parallelogram AMDE is the required application: it equals F, and its defect in the whole parallelogram ABCE is MBCD, which is similar to G. Hence assume henceforth that 0 < |F| < |P|. [1.36, CN1, 6.18]

**Step 3.** First realize the excess of P over F as an actual rectilineal figure. Construct a parallelogram S similar to P and equal to F. This is a direct use of the construction prescribing both shape and area. Since |S| < |P|, its corresponding sides are shorter, by the duplicate-ratio relation for similar polygons. Copy S into the angle CDM: cut off its corresponding adjacent sides along DC and DM, and complete the parallelogram by parallels. The equality of corresponding angles ensures that this is a congruent copy of S. It lies inside P. Let R be the rectilineal region remaining after this corner parallelogram is removed. Then |R| = |P| − |F|, and 0 < |R| < |P|. [6.25, 6.20, D6.1, 1.3, 1.31, CN4, CN3, CN5]

**Step 4.** Construct a parallelogram Q similar to P and equal to R. Again, because |Q| < |P|, its corresponding sides are shorter. Cut off DH on DC and DN on DM equal to the corresponding adjacent sides of Q, and complete the parallelogram DHTN by parallels. Thus H lies strictly between D and C, N lies strictly between D and M, and DHTN is a congruent copy of Q. In particular,
|DHTN| = |R| = |P| − |F|.
The auxiliary copy of S from Step 3 is no longer needed. [6.25, 6.20, 1.3, 1.31, D6.1, CN4]

**Step 5.** Produce HT to meet MB at X, and produce NT in both directions to meet AE at Z and BC at V. Because DHTN is similar and similarly situated to P and has the common angle at D, it is about the same diameter DB as P; hence T lies on DB. Consequently XBVT is the other parallelogram about that diameter. It is similar to P, and therefore similar to G. [P2, 6.26, 6.24, 6.21]

**Step 6.** The remaining two parallelograms MXTN and HCVT are the complements of DHTN and XBVT in P. Therefore
|MXTN| = |HCVT|.
Also, AMNZ and MBVN stand on the equal bases AM and MB and lie between the same parallels AB and ZV. Hence
|AMNZ| = |MBVN|. [1.43, 1.36]

**Step 7.** Adding the equal areas from Step 6 gives
|AXTZ| = |AMNZ| + |MXTN|
= |MBVN| + |HCVT|
= |P| − |DHTN|
= |F|.
Here MBVN together with HCVT is precisely the part of P left after DHTN is removed, and the last equality follows from Step 4. [CN2, CN3, CN1]

**Step 8.** The parallelograms AXTZ and XBVT together form the parallelogram ABVZ on the entire given line AB. Thus AXTZ is applied to AB, equals the given figure F, and is deficient by XBVT, which is similar to the given parallelogram G. Finally, the maximality theorem for applications with a similarly situated similar defect shows that their area cannot exceed the parallelogram described on half of AB and similar to that defect. Thus the stated restriction is necessary, and the construction above succeeds in every permitted case. [6.21, 6.27]

**USED:** 1.10, 1.3, 1.31, 1.36, 1.43, 6.18, 6.20, 6.21, 6.24, 6.25, 6.26, 6.27, CN1, CN2, CN3, CN4, CN5, D6.1, P2
**Human refs (from References field):** 1.36, 6.18, 6.21, 6.25, 6.26
**Jaccard:** 0.263 — AI adds ['1.10', '1.3', '1.31', '1.43', '6.20', '6.24', '6.27', 'CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'D6.1', 'P2']

## Proposition 6.29
**Statement:** To a given straight line to apply a parallelogram equal to a given rectilineal figure and exceeding by a parallelogrammic figure similar to a given one.

**Step 1.** Let AB be the given straight line, R the given rectilineal figure, and S the parallelogram prescribing the shape of the excess. Write [X] for the area of a figure X. We use the midpoint-and-sum construction, with equality obtained from complements. Bisect AB at M, and on MB construct the parallelogram MBCD similar and similarly situated to S, with MD parallel to BC. [1.10, 6.18]

**Step 2.** In the angle AMD construct a parallelogram T equal to R, with its adjacent sides along the rays MA and MD. Thus T and MBCD have disjoint interiors and share an initial segment of MD. Their union is a rectilineal figure U, and
[U] = [MBCD] + [R]. [1.45]

**Step 3.** Construct a parallelogram DEFG equal to U and similar to DCBM, placing its corresponding angle at D, with E on the ray DC and G on the ray DM. [6.25]
Its area is greater than that of DCBM. Therefore E lies beyond C and G beyond M. Indeed, similarity gives DE:DG = DC:DM; if DE were no greater than DC, DG would likewise be no greater than DM, so DEFG would be contained in, or coincide with, DCBM, contrary to its greater area. Thus DCBM is contained in DEFG. [D6.1, 5.14, CN5]

**Step 4.** The parallelograms DCBM and DEFG are similar and similarly situated and have their angle at D in common. Hence they are about the same diameter: B lies on DF. [6.26]
Produce AB to meet EF at H, and produce CB through B to meet GF at K. Through A draw a parallel to DM, meeting GF produced at L. The point orders are A, M, B, H on one straight line and L, G, K, F on the parallel straight line. In particular, AHFL and BHFK are parallelograms. [P2, 1.31]

**Step 5.** In DEFG the parallelograms DCBM and BHFK are about the diameter DF. Their complements CEHB and MBKG are therefore equal. [1.43]
Also, AMGL and MBKG stand on the equal bases AM and MB and lie between the same parallels AH and LF. The equal-base proposition applies directly, giving
[AMGL] = [MBKG]. [1.36]
Consequently,
[CEHB] = [AMGL]. [CN1]

**Step 6.** The large parallelogram DEFG is partitioned into DCBM, CEHB, and MHFG. The proposed parallelogram AHFL is partitioned into AMGL and MHFG. Adding the common area [MHFG] to the equality in Step 5 gives
[DEFG] − [DCBM] = [AHFL]. [CN2]
But Step 3 and Step 2 give
[DEFG] = [DCBM] + [R].
Subtracting [DCBM], we obtain
[AHFL] = [R]. [CN3]

**Step 7.** Since DCBM and BHFK are parallelograms about the same diameter DF of DEFG, they are similar to one another. [6.24]
The prescribed parallelogram S is also similar to DCBM, so BHFK is similar to S. [6.21]
Finally, H lies beyond B, and AHFL consists of the parallelogram ABKL on AB together with the excess BHFK on BH. Thus AHFL is the required parallelogram applied to AB: it equals the given rectilineal figure R and exceeds by a parallelogram BHFK similar to the given one S. This completes the construction.

**USED:** 1.10, 1.31, 1.36, 1.43, 1.45, 5.14, 6.18, 6.21, 6.24, 6.25, 6.26, CN1, CN2, CN3, CN5, D6.1, P2
**Human refs (from References field):** 1.36, 1.43, 6.21, 6.24, 6.25, 6.26
**Jaccard:** 0.353 — AI adds ['1.10', '1.31', '1.45', '5.14', '6.18', 'CN1', 'CN2', 'CN3', 'CN5', 'D6.1', 'P2']

## Proposition 6.30
**Statement:** To cut a given finite straight line in extreme and mean ratio.

**Step 1.** Let AB be the given finite straight line. Choose the direct rectangle–square construction, since it supplies exactly the equality needed to obtain three proportional lines. By 2.11, cut AB at C so that the rectangle contained by AB and CB equals the square on AC. [2.11]

**Step 2.** Apply the converse of 6.17 to the three straight lines AB, AC, CB: the rectangle contained by the extremes equals the square on the mean, so
AB : AC = AC : CB.
The three-line proposition applies directly to the equality constructed in Step 1. [6.17]

**Step 3.** Since AC is a proper part of AB, we have AB > AC. In the proportion AB : AC = AC : CB, the first magnitude therefore exceeds the third; consequently the second exceeds the fourth. Thus AC > CB. [CN5, 5.14]

**Step 4.** We have shown that the whole AB is to the greater segment AC as AC is to the lesser segment CB. Therefore AB has been cut at C in extreme and mean ratio, as required. [D6.3]

**USED:** 2.11, 5.14, 6.17, CN5, D6.3
**Human refs (from References field):** 6.14, 6.29
**Jaccard:** 0.000 — AI adds ['2.11', '5.14', '6.17', 'CN5', 'D6.3']; Human adds ['6.14', '6.29']

## Proposition 6.31
**Statement:** In right - angled triangles the figure on the side subtending the right angle is equal to the similar and similarly described figures on the sides containing the right angle.

**Step 1.** Let ABC be right-angled at A. Denote the areas of the similar and similarly described figures on AB, AC, and BC by F_AB, F_AC, and F_BC. Construct squares on these three sides, and denote their areas by S_AB, S_AC, and S_BC (1.46). We use the square-comparison route: the equality for squares will be transferred to the given figures through the general polygonal ratio theorem, 6.20.

**Step 2.** Since BC subtends the right angle, the square on BC equals the squares on AB and AC together. Thus
S_AB + S_AC = S_BC. (1.47)

**Step 3.** The squares are similar figures, being equilateral and right-angled (D1.22, D6.1). By 6.20, each of the ratios F_AB : F_BC and S_AB : S_BC is the duplicate ratio of AB : BC. Hence they are equal by 5.11. Applying the same reasoning to AC and BC gives
F_AB : F_BC = S_AB : S_BC,
F_AC : F_BC = S_AC : S_BC.
Here 6.20 is used because it applies directly to general similar polygons, not merely to triangles. (6.20, 5.11)

**Step 4.** Taking these proportions alternately gives
F_AB : S_AB = F_BC : S_BC,
F_AC : S_AC = F_BC : S_BC.
Consequently F_AB : S_AB = F_AC : S_AC. (5.16, 5.11)

**Step 5.** Since the two latter pairs have the same ratio, their antecedents taken together have to their consequents taken together that same ratio. Therefore
(F_AB + F_AC) : (S_AB + S_AC) = F_BC : S_BC.
Using the equality from Step 2, this becomes
(F_AB + F_AC) : S_BC = F_BC : S_BC. (5.12, 5.11, 1.47)

**Step 6.** Magnitudes having the same ratio to the same magnitude are equal; hence
F_AB + F_AC = F_BC. (5.9)
Therefore the figure on the side subtending the right angle equals the similar and similarly described figures on the sides containing the right angle, taken together.

**USED:** 1.46, 1.47, 5.11, 5.12, 5.16, 5.9, 6.20, D1.22, D6.1
**Human refs (from References field):** 6.19, 6.8, D6.1
**Jaccard:** 0.091 — AI adds ['1.46', '1.47', '5.11', '5.12', '5.16', '5.9', '6.20', 'D1.22']; Human adds ['6.19', '6.8']

## Proposition 6.32
**Statement:** If two triangles having two sides proportional to two sides be placed together at one angle so that their corresponding sides are also parallel, the remaining sides of the triangles will be in a straight line.

**Step 1.** Let the two triangles be ABC and DCE, placed together at C as stipulated, with AB:AC = CD:DE, AB ∥ CD, and AC ∥ DE. In this adjoining placement, CB and CE lie on opposite sides of CD. Since AC falls on the parallels AB and CD, ∠BAC = ∠ACD. Since CD falls on the parallels AC and DE, ∠ACD = ∠CDE. Hence ∠BAC = ∠CDE. [1.29, CN1]

**Step 2.** Apply VI.6 directly, since the proportional sides AB, AC and CD, DE enclose the equal angles just established. The triangles ABC and DCE are therefore equiangular, with corresponding vertices A, D; B, C; and C, E. In particular, ∠ABC = ∠DCE. [6.6]

**Step 3.** Use the same-side interior-angle conclusion for parallels to obtain the needed angle sum directly. Since BC falls on AB ∥ CD, ∠ABC + ∠BCD equals two right angles. Adding ∠BCD to the equal angles ∠ABC and ∠DCE and using this sum gives ∠BCD + ∠DCE equal to two right angles. [1.29, CN2, CN1]

**Step 4.** At C, the straight lines CB and CE lie on opposite sides of CD and make with it the adjacent angles ∠BCD and ∠DCE, whose sum is two right angles. Therefore CB and CE are in a straight line with one another. Thus the remaining sides BC and CE of the two triangles are in a straight line, as required. [1.14]

**USED:** 1.14, 1.29, 6.6, CN1, CN2
**Human refs (from References field):** 1.14, 1.29, 1.32, 6.6
**Jaccard:** 0.500 — AI adds ['CN1', 'CN2']; Human adds ['1.32']

## Proposition 6.33
**Statement:** In equal circles angles have the same ratio as the circumferences on which they stand, whether they stand at the centres or at the circumferences.

**Step 1.** Let a and b be arcs in two equal circles, and let α and β be the central angular magnitudes standing on them. For a major arc, its central angular magnitude is understood as the sum of the adjacent central angles along that arc. We first prove α:β = a:b directly by the equimultiple criterion. We subdivide before constructing multiples, so that the constructed arcs do not overlap themselves. (D5.5)

**Step 2.** Let m and n be arbitrary positive integers. Choose a power of two q greater than 2 max(m,n). By repeated bisection, divide a and b into q equal arcs each, denoting one part of each by a₀ and b₀. These parts are minor arcs. Their corresponding central angles are equal within each subdivision; denote them by α₀ and β₀. Here III.27 is the natural direction of the correspondence to use, because the equal arc parts have already been constructed. By addition,
α = qα₀,  β = qβ₀,  a = qa₀,  b = qb₀.
Since α and β are each less than a complete revolution and q > 2 max(m,n), both mα₀ and nβ₀ are less than a straight angle. (3.30, 3.27, CN2, CN5)

**Step 3.** In one of the equal circles, start from a fixed radius. On the same side of that radius, construct m successive adjacent angles each equal to α₀; independently, starting from that same radius and proceeding in the same direction, construct n successive adjacent angles each equal to β₀. Equal central angles in equal circles stand on equal arcs. Thus the first construction gives a central angle mα₀ standing on an arc ma₀, and the second gives a central angle nβ₀ standing on an arc nb₀. Both constructions remain within a semicircle. (1.23, 3.26, CN2)

**Step 4.** Compare these two constructed angles. If mα₀ is greater than nβ₀, the second angle lies properly within the first, and its arc nb₀ is a proper part of ma₀; hence ma₀ is greater than nb₀. If the angles are equal, their arcs are equal. If the first angle is less, its arc is likewise a proper part of the second arc and is less. Thus the angular multiples and the arc multiples have the same comparison. Multiplying all four magnitudes by q preserves equality and strict inequality, by repeated addition. Consequently,
mα is greater than, equal to, or less than nβ
according as
ma is greater than, equal to, or less than nb,
respectively. (3.26, CN2, CN5)

**Step 5.** Since m and n were arbitrary, every equimultiple of α and a has the same comparison with the corresponding equimultiple of β and b. The definition of equal ratios therefore gives
α:β = a:b.
This proves the assertion for angles at the centres. (D5.5)

**Step 6.** Now let θ and φ be angles at the circumferences standing on a and b, respectively. The central angle standing on an arc is double the angle at the circumference standing on that same arc, so α = 2θ and β = 2φ. Parts have the same ratio as their corresponding equal multiples; hence θ:φ = α:β. Combining this with Step 5 yields
θ:φ = a:b.
Therefore, in equal circles, angles have the same ratio as the circumferences on which they stand, whether the angles stand at the centres or at the circumferences. (3.20, 5.15, 5.11)

**USED:** 1.23, 3.20, 3.26, 3.27, 3.30, 5.11, 5.15, CN2, CN5, D5.5
**Human refs (from References field):** 3.27, D5.5
**Jaccard:** 0.200 — AI adds ['1.23', '3.20', '3.26', '3.30', '5.11', '5.15', 'CN2', 'CN5']
