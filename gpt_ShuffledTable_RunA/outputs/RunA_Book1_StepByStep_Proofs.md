# Book 1 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 1.1
**Statement:** On a given finite straight line to construct an equilateral triangle.

**Step 1.** Let AB be the given finite straight line. Use the direct two-circle construction: describe a circle with centre A and distance AB, and another with centre B and distance BA. [P3]

**Step 2.** Let C be a point where the two circles intersect, off AB. Either intersection may be chosen, since the proof uses only its membership in both circles. Draw the straight lines AC and BC. [P1]

**Step 3.** Since A is the centre of the first circle and B and C lie on its circumference, AC = AB. Since B is the centre of the second circle and A and C lie on its circumference, BC = BA. These equalities follow from the definition of a circle and its centre. [D1.15, D1.16]

**Step 4.** AB and BA are the same segment. Thus AC and BC are equal to the same segment AB, and therefore AC = BC. Hence all three segments AB, BC, and CA are equal. [CN1]

**Step 5.** The three straight lines AB, BC, and CA enclose the trilateral figure ABC. Since its three sides are equal, ABC is an equilateral triangle, constructed on the given finite straight line AB, as required. [D1.19, D1.20]

**USED:** CN1, D1.15, D1.16, D1.19, D1.20, P1, P3
**Human refs (from References field):** CN1, D1.15, P1, P3
**Jaccard:** 0.571 — AI adds ['D1.16', 'D1.19', 'D1.20']

## Proposition 1.2
**Statement:** To place at a given point (as an extremity) a straight line equal to a given straight line.

**Step 1.** Let A be the given point and BC the given straight line, naming its endpoints so that B is distinct from A. Choose the direct equilateral-triangle route supplied by the preceding proposition: join AB [P1], and construct the equilateral triangle DAB on it [1.1]. Thus DA = DB [D1.20].

**Step 2.** Describe the circle with centre B and radius BC [P3]. Produce DB beyond B to meet this circle at G [P2]. Since BG and BC are radii of this circle, BG = BC [D1.15].

**Step 3.** Since B lies between D and G, DG is greater than DB [CN5], and therefore greater than DA by Step 1. Describe the circle with centre D and radius DG [P3], and produce DA beyond A to meet it at L [P2]. The intersection is beyond A because the radius DG is greater than DA. The radii DL and DG are equal [D1.15].

**Step 4.** From the equal straight lines DL and DG subtract the equal straight lines DA and DB. Because A lies between D and L, and B between D and G, the remainders are AL and BG. Hence AL = BG [CN3].

**Step 5.** Since AL = BG and BG = BC, it follows that AL = BC [CN1]. Thus AL is a straight line equal to the given straight line BC and having the given point A as an extremity, as required.

**USED:** 1.1, CN1, CN3, CN5, D1.15, D1.20, P1, P2, P3
**Human refs (from References field):** 1.1, CN1, CN3, P1, P2, P3
**Jaccard:** 0.667 — AI adds ['CN5', 'D1.15', 'D1.20']

## Proposition 1.3
**Statement:** Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

**Step 1.** Let AB and CD be the given unequal straight lines, with AB greater than CD. At A place a straight line AE equal to CD. Proposition I.2 is the direct choice because it places the lesser length at the endpoint from which the cut is to be made. [1.2]

**Step 2.** Describe a circle with centre A and distance AE, cutting AB at F. Since AE = CD < AB, F lies between A and B. [P3]

**Step 3.** Since E and F lie on this circle, the straight lines AE and AF drawn from its centre are equal. [D1.15]

**Step 4.** Now AF = AE and CD = AE; therefore AF = CD. Thus AF has been cut off from the greater straight line AB equal to the lesser CD, as required. [CN1]

**USED:** 1.2, CN1, D1.15, P3
**Human refs (from References field):** 1.2, CN1, D1.15, P3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.4
**Statement:** If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base, the triangle will be equal to the triangle, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend.

**Step 1.** Let ABC and DEF be triangles with AB = DE, AC = DF, and ∠BAC = ∠EDF. We use direct superposition, establishing the required equalities by coincidence rather than invoking another proposition (CN4).

**Step 2.** Place triangle ABC upon triangle DEF, with A on D, the ray AB along the ray DE, and C on the same side of DE as F. Since AB = DE, B coincides with E. Thus the first pair of equal sides coincides (hypothesis; CN4).

**Step 3.** Since ∠BAC = ∠EDF, and their first sides now coincide, their second sides AC and DF have the same inclination on the chosen side of DE. Hence the ray AC coincides with the ray DF (D1.8). Since AC = DF, C consequently coincides with F (hypothesis; superposition).

**Step 4.** The bases BC and EF therefore have the same endpoints. Being straight segments between those endpoints, they coincide (D1.4), and consequently BC = EF (CN4).

**Step 5.** All three sides now coincide respectively, so the triangles themselves coincide, as do the angles at B and E and the angles at C and F. Therefore triangle ABC equals triangle DEF, ∠ABC = ∠DEF, and ∠ACB = ∠DFE (CN4). These are precisely the remaining angles opposite the corresponding equal sides AC, DF and AB, DE. Thus the bases, the triangles, and the remaining corresponding angles are equal, as required.

**USED:** CN4, D1.4, D1.8
**Human refs (from References field):** CN4
**Jaccard:** 0.333 — AI adds ['D1.4', 'D1.8']

## Proposition 1.5
**Statement:** In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

**Step 1.** Let ABC be an isosceles triangle with AB = AC and base BC [D1.20]. Produce AB beyond B and AC beyond C. Choose F on the first produced line beyond B, and extend the second to H far enough that AH > AF [P2].

**Step 2.** Since F is beyond B, AF > AB, and therefore AF > AC [CN5]. From AH cut off AG equal to AF [1.3]. Thus G lies beyond C. Join FC and BG [P1].

**Step 3.** Use the direct side–angle–side route: compare triangles AFC and AGB. We have AF = AG by construction and AC = AB by hypothesis. Their included angles FAC and GAB coincide with the same angle at A and are therefore equal [CN4]. Hence, by 1.4,
FC = GB, ∠AFC = ∠AGB, and ∠ACF = ∠ABG.
This application of 1.4 is natural because the construction supplies precisely two equal corresponding sides and their equal included angle.

**Step 4.** From AF = AG subtract AB = AC. Since A, B, F and A, C, G lie in those respective orders, the remaining segments satisfy BF = CG [CN3].

**Step 5.** Now compare triangles BFC and CGB. We have BF = CG and FC = GB. Since the rays FB and FA coincide, and the rays GC and GA coincide, the equality ∠AFC = ∠AGB from Step 3 is exactly ∠BFC = ∠CGB. Applying 1.4 again gives
∠FBC = ∠GCB and ∠BCF = ∠CBG.
The first equality proves that the angles under the base, formed by BC and the produced equal sides, are equal [1.4].

**Step 6.** Finally, ∠ACF = ∠ABG by Step 3. Within these angles, the ray CB separates ∠ACF into ∠ACB and ∠BCF, while the ray BC separates ∠ABG into ∠ABC and ∠CBG. Subtract the equal angles ∠BCF and ∠CBG obtained in Step 5. The remaining angles are equal: ∠ACB = ∠ABC [CN3]. Thus the angles at the base of the isosceles triangle are equal, and the angles under the base are also equal, as required.

**USED:** 1.3, 1.4, CN3, CN4, CN5, D1.20, P1, P2
**Human refs (from References field):** 1.3, 1.4, P1, P2
**Jaccard:** 0.500 — AI adds ['CN3', 'CN4', 'CN5', 'D1.20']

## Proposition 1.6
**Statement:** If in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another.

**Step 1.** Let ABC be a triangle with ∠ABC = ∠BCA. We must prove AC = AB. We use the cut-off construction followed by the already available side–angle–side criterion (1.3, 1.4).

**Step 2.** Suppose that AB and AC are unequal. Interchanging B and C if necessary, assume AB > AC. Cut off BD from BA equal to AC, so that D lies strictly between B and A (1.3). Join DC (P1).

**Step 3.** Since BD lies along BA, ∠DBC coincides with ∠ABC and hence equals the given angle ∠BCA. Also BC = CB, since these are the same segment (CN4 and the hypothesis).

**Step 4.** In triangles DBC and ACB, DB = AC, BC = CB, and the included angles ∠DBC and ∠ACB are equal. Therefore triangle DBC equals triangle ACB by side–angle–side (1.4).

**Step 5.** But D lies strictly between A and B, so triangle DBC is a proper part of triangle ABC. The whole triangle ABC is therefore greater than triangle DBC (CN5), contradicting Step 4. Thus AB and AC cannot be unequal, and consequently AB = AC. The sides subtending the equal angles are equal.

**USED:** 1.3, 1.4, CN4, CN5, P1
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.3', '1.4', 'CN4', 'CN5', 'P1']

## Proposition 1.7
**Statement:** Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities), and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively, namely each to that which has the same extremity with it.

**Step 1.** Let AB be the given straight line. Suppose, contrary to the assertion, that distinct points C and D on the same side of AB satisfy AC = AD and BC = BD. Join CD. We use 1.5 directly, since these equalities make ACD and BCD isosceles triangles; its angles-under-the-base conclusion will handle the interior configuration. [P1, 1.5]

**Step 2.** If A, C, D were collinear, C and D would lie on the same ray from A, since they are on the same side of AB. One of AC and AD would therefore be a proper part of the other, contrary to their equality. Similarly, B, C, D cannot be collinear. Thus no three of the four points are collinear. Since C and D are on the same side of AB, the remaining configurations are: the four points form a convex quadrilateral, or one of C and D lies strictly inside the triangle formed by the other and A, B. [CN5]

**Step 3.** First consider the convex configuration. Interchanging A and B if necessary, its boundary order is A, C, D, B. The ray CB lies strictly inside ∠ACD, and the ray DA lies strictly inside ∠BDC. Hence
∠ACD > ∠BCD, and ∠BDC > ∠ADC,
because each whole angle is greater than its proper part. [CN5]

**Step 4.** Since AC = AD, proposition 1.5 gives ∠ACD = ∠ADC. Since BC = BD, it also gives ∠BCD = ∠BDC. Substituting these equalities into the preceding inequalities yields
∠ACD > ∠BCD = ∠BDC > ∠ADC = ∠ACD,
which is impossible. Thus the convex configuration cannot occur. [1.5, CN1, CN5]

**Step 5.** In the remaining configuration, interchange C and D if necessary so that D lies strictly inside triangle ABC. Produce AC beyond C to E, and AD beyond D to F. Because D is inside ABC, the ray CB lies strictly inside ∠ECD, while the ray DF lies strictly inside ∠BDC. Consequently,
∠ECD > ∠BCD, and ∠BDC > ∠CDF. [P2, CN5]

**Step 6.** Applying the angles-under-the-base conclusion of 1.5 to AC = AD gives ∠ECD = ∠CDF. Applying its base-angle conclusion to BC = BD gives ∠BCD = ∠BDC. Therefore
∠ECD > ∠BCD = ∠BDC > ∠CDF = ∠ECD,
again an impossibility. All possible configurations have now been excluded. Hence no distinct point D on the same side of AB can satisfy both AC = AD and BC = BD, which is precisely the required assertion. [1.5, CN1, CN5]

**USED:** 1.5, CN1, CN5, P1, P2
**Human refs (from References field):** 1.5
**Jaccard:** 0.200 — AI adds ['CN1', 'CN5', 'P1', 'P2']

## Proposition 1.8
**Statement:** If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines.

**Step 1.** Let ABC and DEF be triangles with AB = DE, AC = DF, and BC = EF. We must prove ∠BAC = ∠EDF. We use the uniqueness assertion of 1.7 after superposing the equal bases, since it directly addresses two equal pairs of sides erected on the same base. [Given; 1.7]

**Step 2.** Superpose triangle ABC on triangle DEF, placing B at E and BC along EF, with A on the same side of EF as D. Since BC = EF, C coincides with F. Let G be the position occupied by A. The corresponding superposed sides coincide, so EG = AB and FG = AC. [Given; CN4]

**Step 3.** Consequently EG = DE and FG = DF. If G were different from D, there would be two pairs of straight lines EG, FG and ED, FD, constructed from the extremities of the same base EF, meeting at different points on the same side of it, and equal respectively at each extremity. This is impossible by 1.7. Therefore G coincides with D. [CN1; 1.7]

**Step 4.** Thus, under the superposition, AB coincides with DE and AC with DF. Hence the angle BAC coincides with the angle EDF, and coincident magnitudes are equal. Therefore ∠BAC = ∠EDF: the angles contained by the respectively equal sides are equal, as required. [CN4]

**USED:** 1.7, CN1, CN4
**Human refs (from References field):** 1.7
**Jaccard:** 0.333 — AI adds ['CN1', 'CN4']

## Proposition 1.9
**Statement:** To bisect a given rectilineal angle.

**Step 1.** Let BAC be the given rectilineal angle. Choose a point D on the ray AB, distinct from A. Produce AC if necessary until it is longer than AD, and cut off AE on the ray AC equal to AD. Thus AD = AE. [P2, 1.3]

**Step 2.** Join DE. On DE construct the equilateral triangle DEF, choosing its vertex F on the side of DE opposite A; this is the choice for the internal bisector. Since DEF is equilateral, DF = EF. [P1, 1.1, D1.20]

**Step 3.** Join AF. In triangles DAF and EAF, AD = AE by Step 1, AF is common and therefore equal to itself, and the bases DF and EF are equal by Step 2. [P1, CN4]

**Step 4.** Apply 1.8 directly to these three corresponding side equalities: the equal sides DA, AF and EA, AF contain equal angles, so angle DAF equals angle EAF. Since AD and AE lie along the given rays AB and AC, and the opposite-side choice in Step 2 selects the interior dividing ray AF, angle BAF equals angle FAC. Hence AF bisects the given rectilineal angle BAC, as required. [1.8]

**USED:** 1.1, 1.3, 1.8, CN4, D1.20, P1, P2
**Human refs (from References field):** 1.3, 1.8
**Jaccard:** 0.286 — AI adds ['1.1', 'CN4', 'D1.20', 'P1', 'P2']

## Proposition 1.10
**Statement:** To bisect a given finite straight line.

**Step 1.** Let AB be the given finite straight line. Construct an equilateral triangle ABC on AB by 1.1. Thus AC = BC by the definition of an equilateral triangle. [1.1, D1.20]

**Step 2.** Bisect angle ACB by 1.9, and produce its internal bisector to meet AB at D. Then ∠ACD = ∠DCB, and D lies between A and B. [1.9, P2]

**Step 3.** In triangles ACD and BCD, AC = BC, while CD is common and therefore equal to itself. The included angles ∠ACD and ∠BCD are equal by Step 2. Apply the side–angle–side proposition directly, since these are precisely its hypotheses: the corresponding bases AD and DB are equal. [CN4, 1.4]

**Step 4.** Since D lies on AB and AD = DB, the given finite straight line AB has been bisected at D, as required. [1.4]

**USED:** 1.1, 1.4, 1.9, CN4, D1.20, P2
**Human refs (from References field):** 1.1, 1.4, 1.9
**Jaccard:** 0.500 — AI adds ['CN4', 'D1.20', 'P2']

## Proposition 1.11
**Statement:** To draw a straight line at right angles to a given straight line from a given point on it.

**Step 1.** Let AB be the given straight line and C the given point on it. Choose a point D on the line distinct from C. Produce the line beyond C, away from D, as necessary, to a point G such that CG is greater than CD. Thus C lies between D and G. [P2]

**Step 2.** From CG cut off CE equal to CD. Then D, C, E lie on the given straight line, with C between D and E. [1.3]

**Step 3.** On DE construct the equilateral triangle DFE. In particular, DF equals EF. [1.1, D1.20]

**Step 4.** Join C to F. The side CF is common to triangles DCF and ECF and is equal to itself. [P1, CN4]

**Step 5.** In these triangles, DC equals EC, CF equals CF, and the base DF equals the base EF. Therefore the angles contained by the corresponding equal sides are equal: ∠DCF equals ∠FCE. We use the three-side comparison directly because it matches precisely the equalities already obtained. [1.8]

**Step 6.** Since D, C, E are collinear with C between D and E, these are the adjacent angles made by CF standing on the given straight line. Their equality makes each a right angle, and CF is perpendicular to AB. Thus a straight line has been drawn at right angles to the given straight line from the given point C, as required. [D1.10]

**USED:** 1.1, 1.3, 1.8, CN4, D1.10, D1.20, P1, P2
**Human refs (from References field):** 1.1, 1.3, 1.8, D1.10
**Jaccard:** 0.500 — AI adds ['CN4', 'D1.20', 'P1', 'P2']

## Proposition 1.12
**Statement:** To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

**Step 1.** Let ℓ be the given infinite straight line, and let C be the given point not on it. Choose a point D on the other side of ℓ from C. Describe the circle with centre C and radius CD, and let E and G be its two intersections with ℓ. The choice of D on the opposite side ensures that the circle cuts ℓ rather than merely touching it. [P3]

**Step 2.** Bisect the segment EG at H, so that EH = HG. Join CE, CG, and CH. [1.10, P1]

**Step 3.** Since E and G lie on the circle with centre C, CE = CG. Also, EH = HG by the bisection, and CH is equal to itself because it is common to the two triangles EHC and GHC. [D1.15, 1.10, CN4]

**Step 4.** In triangles EHC and GHC, the two sides EH, HC equal the two sides GH, HC respectively, and the base EC equals the base GC. Therefore ∠EHC = ∠GHC. We use I.8 directly because the construction supplies precisely its two-side-and-base equalities. [1.8]

**Step 5.** Since H lies between E and G on ℓ, these are adjacent angles made by CH standing on ℓ. Being equal, each is a right angle, and CH is perpendicular to ℓ. Thus from the given point C a perpendicular straight line CH has been drawn to the given infinite straight line, as required. [D1.10]

**USED:** 1.10, 1.8, CN4, D1.10, D1.15, P1, P3
**Human refs (from References field):** 1.10, 1.8, D1.10, P1, P3
**Jaccard:** 0.714 — AI adds ['CN4', 'D1.15']

## Proposition 1.13
**Statement:** If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

**Step 1.** Let BA stand on the straight line CD at B, with C and D on opposite sides of B. The angles made are ∠CBA and ∠ABD. If BA is perpendicular to CD, these adjacent angles are both right angles, giving the first alternative. (D1.10)

**Step 2.** Suppose BA is not perpendicular to CD. By 1.11, draw BE perpendicular to CD at B, on the same side of CD as A. This is the direct construction appropriate to a point already on the given line. Both ∠CBE and ∠EBD are right angles. (1.11, D1.10)

**Step 3.** Since BA is not perpendicular to CD, BA and BE are distinct. Interchanging the names C and D if necessary, take BE to lie inside ∠CBA. Each whole angle coincides with its indicated adjacent parts; hence
∠CBA = ∠CBE + ∠EBA,
and
∠EBD = ∠EBA + ∠ABD. (CN4)

**Step 4.** Add ∠ABD to both sides of the first equality, and add ∠CBE to both sides of the second. By addition of equals, both ∠CBA + ∠ABD and ∠CBE + ∠EBD equal the same sum ∠CBE + ∠EBA + ∠ABD. They are therefore equal to one another. (CN2, CN1)
Since ∠CBE and ∠EBD are right angles, the original angles together equal two right angles. Thus a straight line set up on a straight line makes either two right angles or angles equal to two right angles.

**USED:** 1.11, CN1, CN2, CN4, D1.10
**Human refs (from References field):** 1.11, CN1, CN2, D1.10
**Jaccard:** 0.800 — AI adds ['CN4']

## Proposition 1.14
**Statement:** If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

**Step 1.** Let BC and BD meet the straight line AB at B on opposite sides of AB, and suppose that ∠ABC + ∠ABD equals two right angles. Produce CB through B to E, so that C, B, E lie in a straight line (P2). We compare BD with this continuation because Proposition 1.13 supplies exactly the angle sum appearing in the hypothesis.

**Step 2.** Since AB stands on the straight line CBE, ∠ABC + ∠ABE equals two right angles (1.13).

**Step 3.** All right angles are equal, and adding equals gives equal sums; hence the two right-angle sums in the hypothesis and Step 2 are equal (P4, CN2). Therefore
∠ABC + ∠ABD = ∠ABC + ∠ABE
(CN1). Subtracting the common angle ∠ABC gives
∠ABD = ∠ABE
(CN3).

**Step 4.** Since BE is the continuation of BC through B, BE and BD lie on the same side of AB. If these rays were distinct, one of the angles ∠ABD and ∠ABE would be a proper part of the other. The whole would then be greater than the part, contrary to their equality in Step 3 (CN5). Thus BD coincides with the ray BE. Since C, B, E lie in a straight line, BC and BD are in a straight line with one another, as required.

**USED:** 1.13, CN1, CN2, CN3, CN5, P2, P4
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.571 — AI adds ['CN2', 'CN5', 'P2']

## Proposition 1.15
**Statement:** If two straight lines cut one another, they make the vertical angles equal to one another.

**Step 1.** Let the straight lines AB and CD intersect at E, with A, E, B in that order and C, E, D in that order. We take the direct adjacent-angle-sum route, since Proposition 1.13 applies immediately to these intersecting lines. Applying it to EC standing on AB, EB standing on CD, and ED standing on AB, respectively, shows that each of
∠AEC + ∠CEB,
∠CEB + ∠BED,
∠BED + ∠DEA
is equal to two right angles. [1.13]

**Step 2.** All right angles are equal, and adding equals to equals gives equal wholes; hence the totals of two right angles in Step 1 are equal. Therefore, things equal to the same thing being equal to one another,
∠AEC + ∠CEB = ∠CEB + ∠BED,
and
∠CEB + ∠BED = ∠BED + ∠DEA. [P4, CN2, CN1]

**Step 3.** Subtract the common angle ∠CEB from both sides of the first equality. The remainders are equal, so ∠AEC = ∠BED. [CN3]

**Step 4.** Subtract the common angle ∠BED from both sides of the second equality. The remainders are equal, so ∠CEB = ∠DEA. Thus both pairs of vertical angles are equal, as required. [CN3]

**USED:** 1.13, CN1, CN2, CN3, P4
**Human refs (from References field):** 1.13, CN1, CN3, P4
**Jaccard:** 0.800 — AI adds ['CN2']

## Proposition 1.16
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

**Step 1.** Let ABC be a triangle, and produce BC beyond C to D. We must prove that ∠ACD is greater than each of ∠BAC and ∠ABC. [P2]

**Step 2.** Bisect AC at E. Join BE, produce it sufficiently far beyond E, and cut off EF equal to BE; join CF. Thus AE = EC and BE = EF. We choose this midpoint construction because it supplies the two equal sides needed for a direct side–angle–side argument. [1.10, P1, P2, 1.3]

**Step 3.** Since AC and BF intersect at E, the vertical angles AEB and CEF are equal. Therefore triangles AEB and CEF have two corresponding sides equal and their included angles equal. By side–angle–side, ∠BAE = ∠ECF. Since E lies on AC, ∠BAE is ∠BAC. [1.15, 1.4]

**Step 4.** Because E lies between A and C and B, E, F occur in that order, F is on the opposite side of AC from B and on the same side of BC as A. Hence CF lies strictly inside ∠ACD. Since CE is the same ray as CA, ∠ECF is a proper part of ∠ACD. The whole is greater than the part, so ∠ACD > ∠ECF = ∠BAC. [CN5]

**Step 5.** To compare the other opposite interior angle, produce AC beyond C to G. Bisect BC at M, join AM, and produce AM beyond M to N so that MN = AM; join CN. Thus BM = MC and AM = MN. [P2, 1.10, P1, 1.3]

**Step 6.** The vertical angles BMA and CMN are equal. Consequently triangles BMA and CMN have two corresponding sides and their included angles equal, so ∠MBA = ∠MCN. As B, M, C are collinear in that order, this says ∠ABC = ∠BCN. [1.15, 1.4]

**Step 7.** Since M lies between B and C and A, M, N occur in that order, N is on the opposite side of BC from A and on the same side of AC as B. Thus CN lies strictly inside ∠BCG, and the whole angle BCG is greater than its part BCN. Hence ∠BCG > ∠ABC. But ∠BCG and ∠ACD are vertical angles and are equal. Therefore ∠ACD > ∠ABC; together with Step 4, ∠ACD is greater than either interior and opposite angle, as required. [CN5, 1.15]

**USED:** 1.10, 1.15, 1.3, 1.4, CN5, P1, P2
**Human refs (from References field):** 1.10, 1.15, 1.3, 1.4, CN5, P1, P2
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.17
**Statement:** In any triangle two angles taken together in any manner are less than two right angles.

**Step 1.** Let any two angles of a triangle be chosen, and label the vertices so that these are ∠ABC and ∠ACB. Produce BC beyond C to D in a straight line. [P2]

**Step 2.** By the exterior-angle theorem, ∠ACD > ∠ABC. We use this direct exterior-angle comparison because it compares one chosen angle with the angle adjacent to the other. [1.16]

**Step 3.** Since CB and CD are opposite rays, the angles ∠ACB and ∠ACD together equal two right angles. [1.13]

**Step 4.** The sum ∠ACD + ∠ACB exceeds ∠ABC + ∠ACB by the positive excess of ∠ACD over ∠ABC; hence the latter sum is less than the former, by the whole being greater than the part. Therefore ∠ABC + ∠ACB is less than two right angles. Since the chosen pair was arbitrary, any two angles of any triangle taken together are less than two right angles. [CN5; Steps 2–3]

**USED:** 1.13, 1.16, CN5, P2
**Human refs (from References field):** 1.13, 1.16, P2
**Jaccard:** 0.750 — AI adds ['CN5']

## Proposition 1.18
**Statement:** In any triangle the greater side subtends the greater angle.

**Step 1.** Let ABC be a triangle with AC > AB. We take the direct route of forming an isosceles triangle within ABC. Cut off AD from AC equal to AB, so that D lies strictly between A and C, and join BD. [1.3, P1]

**Step 2.** Since AB = AD, triangle ABD is isosceles; therefore ∠ABD = ∠ADB. [1.5]

**Step 3.** In triangle BDC, the side CD is produced through D to A. Thus ∠ADB is an exterior angle, and the exterior-angle theorem gives directly ∠ADB > ∠BCD. Since D lies on AC, ∠BCD = ∠BCA. Hence ∠ADB > ∠BCA. [1.16]

**Step 4.** Because BD lies inside ∠ABC, the whole angle ∠ABC is greater than its part ∠ABD. Combining this with Steps 2–3 gives ∠ABC > ∠ABD = ∠ADB > ∠BCA. Thus the angle opposite the greater side AC is greater than the angle opposite AB. Therefore, in any triangle the greater side subtends the greater angle. [CN5, 1.5, 1.16]

**USED:** 1.16, 1.3, 1.5, CN5, P1
**Human refs (from References field):** 1.16, 1.3
**Jaccard:** 0.400 — AI adds ['1.5', 'CN5', 'P1']

## Proposition 1.19
**Statement:** In any triangle the greater angle is subtended by the greater side.

**Step 1.** Let ABC be a triangle with ∠ABC greater than ∠ACB. Their opposite sides are AC and AB, respectively. We compare these sides by excluding equality first, then the reverse inequality. If AC = AB, the base angles ∠ABC and ∠ACB would be equal by 1.5, contradicting the hypothesis. Thus AC ≠ AB. The base-angle theorem is the natural first choice because this case assumes equal sides. [1.5]

**Step 2.** If AC < AB, then the greater side AB would subtend the greater angle: ∠ACB > ∠ABC, by 1.18. This contradicts the hypothesis. Thus AC is not less than AB. [1.18]

**Step 3.** Since AC is neither equal to nor less than AB, it is greater than AB, by the exclusions in Steps 1–2. Hence the greater angle ∠ABC is subtended by the greater side AC. Therefore, in any triangle the greater angle is subtended by the greater side. [1.5, 1.18]

**USED:** 1.18, 1.5
**Human refs (from References field):** 1.18, 1.5
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.20
**Statement:** In any triangle two sides taken together in any manner are greater than the remaining one.

**Step 1.** Let ABC be any triangle, and choose AB and AC as the two sides to be taken together. Use an isosceles-triangle construction: produce BA beyond A sufficiently far, and cut off AD equal to AC on the produced part, so that B, A, D lie in that order. Join CD. [P2, 1.3, P1]

**Step 2.** Since AD = AC, triangle ACD is isosceles, and therefore ∠ACD = ∠CDA. The rays DA and DB coincide, so ∠CDA is also ∠BDC. Thus ∠ACD = ∠BDC. [1.5]

**Step 3.** Since A lies between B and D, ray CA lies inside ∠BCD. Hence ∠BCD is greater than its proper part ∠ACD, and consequently ∠BCD > ∠BDC. [CN5; Step 2]

**Step 4.** In triangle BCD, the greater angle ∠BCD is subtended by BD, and ∠BDC by BC. Therefore BD > BC. Proposition 1.19 is the direct choice here because the established comparison is between angles and the required comparison is between their opposite sides. [1.19]

**Step 5.** Because A lies between B and D, BD is BA and AD taken together. Adding BA to the equal lengths AD and AC gives BA + AD = BA + AC. Thus BA + AC = BD > BC. The chosen pair of sides was arbitrary; cyclic relabeling gives AB + BC > AC and AC + BC > AB as well. Therefore, in any triangle, two sides taken together in any manner are greater than the remaining one. [CN2; Steps 1–4]

**USED:** 1.19, 1.3, 1.5, CN2, CN5, P1, P2
**Human refs (from References field):** 1.19, 1.5, CN5
**Jaccard:** 0.429 — AI adds ['1.3', 'CN2', 'P1', 'P2']

## Proposition 1.21
**Statement:** If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greaterangle.

**Step 1.** Let ABC be a triangle, and let BD and CD meet at D within it, having been drawn from the extremities of BC. Produce BD beyond D to meet AC at E; thus B, D, E occur in that order, and E lies between A and C. [P2] This single continuation gives a direct route for both claims: triangle inequalities compare the lengths, and exterior-angle inequalities compare the angles.

**Step 2.** In triangle ABE, the two sides AB and AE together are greater than BE. [1.20] Adding EC preserves the strict excess, so
AB + AE + EC > BE + EC.
Since AE + EC = AC, it follows that
AB + AC > BE + EC. [CN2, CN5]

**Step 3.** In triangle DEC,
DE + EC > DC. [1.20]
Adding BD to both sides and using BD + DE = BE gives
BE + EC > BD + DC. [CN2, CN5]
Together with Step 2, this yields
AB + AC > BD + DC.
Thus the constructed straight lines are together less than the remaining two sides of the original triangle.

**Step 4.** In triangle DEC, the side ED is produced beyond D to B. Its exterior angle BDC is therefore greater than the interior and opposite angle DEC:
∠BDC > ∠DEC. [1.16]

**Step 5.** In triangle ABE, the side AE is produced beyond E to C. Since ED is the same ray as EB, its exterior angle is ∠DEC; since A, E, C are collinear, the opposite interior angle at A is ∠BAC. Hence
∠DEC > ∠BAC. [1.16]
Combining this with Step 4 gives ∠BDC > ∠BAC. Therefore BD and CD together are less than AB and AC together, but contain a greater angle, as required.

**USED:** 1.16, 1.20, CN2, CN5, P2
**Human refs (from References field):** 1.16, 1.20
**Jaccard:** 0.400 — AI adds ['CN2', 'CN5', 'P2']

## Proposition 1.22
**Statement:** Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manner should be greater than the remaining one.

**Step 1.** The condition is necessary: if a triangle has sides equal to the three given straight lines, then any two of its sides together are greater than the remaining side. [1.20]

**Step 2.** For the construction, let the given lengths be a, b, c, with a+b>c, a+c>b, and b+c>a. Choose a greatest given line as the base AB, and call its length c. This choice makes the direct two-circle construction particularly simple. Produce AB beyond both endpoints sufficiently far, and cut off AD=a beyond A and BE=b beyond B. Thus D, A, B, E occur in that order on one straight line. The auxiliary extensions are chosen longer than the lengths to be cut off, so the cutting-off proposition applies directly. [P2, 1.3]

**Step 3.** Describe the circle with centre A and distance AD, and the circle with centre B and distance BE. Their radii are respectively a and b. [P3, D1.15]

**Step 4.** To locate their crossing, let X be the endpoint opposite D of the first circle’s diameter through A. Then AX=AD=a. Since a≤c=AB, X lies between A and B or coincides with B. Consequently
BD=c+a>b,
whereas
BX=c−a<b,
the latter inequality following from c<a+b. Thus D is outside the circle with centre B, while X is strictly inside it. The circumference of the first circle therefore crosses the second circle between D and X; choose a crossing K on either side of the line AB. It is not on AB, since the first circle’s endpoints on that line, D and X, are respectively strictly outside and strictly inside the second circle. [D1.15, D1.17, CN2, CN5]

**Step 5.** Join AK and BK. Since K belongs to the circle with centre A, AK=AD=a; since K belongs to the circle with centre B, BK=BE=b. Also AB=c by construction. Therefore the non-collinear points A, B, K form a triangle whose three sides are equal to the three given straight lines. The required triangle has been constructed, and Step 1 establishes the stated necessity. [P1, D1.15, CN1]

**USED:** 1.20, 1.3, CN1, CN2, CN5, D1.15, D1.17, P1, P2, P3
**Human refs (from References field):** 1.20, 1.3
**Jaccard:** 0.200 — AI adds ['CN1', 'CN2', 'CN5', 'D1.15', 'D1.17', 'P1', 'P2', 'P3']

## Proposition 1.23
**Statement:** On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

**Step 1.** Let A be the given point on the given straight line AB, and let the given rectilineal angle have vertex C. Choose points D and E, distinct from C, on its respective arms, and join DE. Thus CDE is a triangle and ∠DCE is the given angle. [P1]

**Step 2.** In triangle CDE, any two sides together are greater than the third:
CD + CE > DE, CD + DE > CE, and CE + DE > CD. [1.20]

**Step 3.** Apply 1.22 to these three lengths, taking the side AF along the given ray AB, and construct triangle AFG such that AF = CD, AG = CE, and FG = DE. Produce the given straight line as necessary to accommodate AF. This is the direct triangle-construction route: Step 2 establishes exactly the inequalities required by 1.22. [P2, 1.22]

**Step 4.** The triangles FAG and DCE have FA = DC and AG = CE, and their bases FG and DE are equal. Therefore their angles contained by the corresponding equal sides are equal: ∠FAG = ∠DCE. Since AF lies along AB, the angle ∠BAG is the required angle on the given straight line at A. Thus the construction is complete. [1.8]

**USED:** 1.20, 1.22, 1.8, P1, P2
**Human refs (from References field):** 1.8
**Jaccard:** 0.200 — AI adds ['1.20', '1.22', 'P1', 'P2']

## Proposition 1.24
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

**Step 1.** Let ABC and DEF be triangles with AB = DE and AC = DF, and suppose ∠BAC > ∠EDF. We must prove BC > EF. These are the given hypotheses.

**Step 2.** Inside ∠BAC construct a ray AG such that ∠BAG = ∠EDF. On this ray take G so that AG = AC, extending a segment along the ray and cutting off the required length if necessary. Thus AG = DF also. (1.23, P2, 1.3, CN1.)

**Step 3.** Join BG. The triangles ABG and DEF have AB = DE, AG = DF, and the included angles ∠BAG = ∠EDF. Therefore BG = EF. It remains to prove BC > BG. (P1, 1.4.)

**Step 4.** If G lies on the straight line BC, then, since AG lies strictly inside ∠BAC, G lies between B and C. Consequently BC > BG, since the whole is greater than its part; together with Step 3 this gives BC > EF. Henceforth suppose G does not lie on the straight line BC. (CN5.)

**Step 5.** Bisect ∠GAC, letting its bisector meet BC at P, and join PG. Because this bisector lies strictly inside ∠BAC, P lies between B and C. This angle-bisection route is chosen to make PG equal to PC, reducing the comparison directly to the triangle inequality in BPG. (1.9, P1.)

**Step 6.** In triangles GAP and CAP, GA = CA, AP is common, and ∠GAP = ∠CAP by the bisection. Therefore their bases are equal: GP = CP. (1.4.)

**Step 7.** Since G is not on the straight line BC, BPG is a triangle. Its two sides BP and PG together are greater than BG. But PG = PC, so adding BP to these equals gives BP + PG = BP + PC = BC. Hence BC > BG. The triangle inequality is the direct comparison needed here. (1.20, CN2.)

**Step 8.** By Step 3, BG = EF; thus Step 7 gives BC > EF, and Step 4 already established the same conclusion in the collinear case. Therefore, when two corresponding pairs of sides are equal, the triangle with the greater included angle has the greater base, as required.

**USED:** 1.20, 1.23, 1.3, 1.4, 1.9, CN1, CN2, CN5, P1, P2
**Human refs (from References field):** 1.19, 1.23, 1.4, 1.5
**Jaccard:** 0.167 — AI adds ['1.20', '1.3', '1.9', 'CN1', 'CN2', 'CN5', 'P1', 'P2']; Human adds ['1.19', '1.5']

## Proposition 1.25
**Statement:** If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.

**Step 1.** Let ABC and DEF be triangles with AB = DE and AC = DF, but BC > EF. We must prove that ∠BAC > ∠EDF. We exclude equality first, then the opposite inequality.

**Step 2.** If ∠BAC = ∠EDF, the two triangles have two sides and their contained angles respectively equal. By **1.4**, their bases are equal: BC = EF. This contradicts BC > EF. Thus the contained angles are not equal. This is the first case because it is directly settled by the earlier side-angle-side proposition.

**Step 3.** If ∠BAC < ∠EDF, apply **1.24** with DEF as the first triangle and ABC as the second. Since DE = AB and DF = AC, the greater contained angle ∠EDF would give EF > BC, contrary to BC > EF. Thus ∠BAC is not less than ∠EDF.

**Step 4.** Since ∠BAC is neither equal to nor less than ∠EDF, it is greater than ∠EDF. Therefore, of two triangles having two sides respectively equal, the triangle with the greater base also has the greater angle contained by those sides, as required.

**USED:** 1.24, 1.4
**Human refs (from References field):** 1.24, 1.4
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.26
**Statement:** If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of the equal angles, they will also have the remaining sides equal tothe remaining sides and the remaining angle to the remaining angle.

**Step 1.** Let ABC and DEF be triangles with ∠ABC = ∠DEF and ∠ACB = ∠DFE. The given equal sides are either BC and EF, adjoining these angles, or, after interchanging the equal-angle pairs if necessary, AB and DE, opposite the equal angles at C and F. We use a cut-off construction followed by side–angle–side: this naturally supplies the two sides and included angle required by 1.4. [1.3, 1.4]

**Step 2.** First suppose BC = EF. If AB and DE were unequal, interchange the triangles if necessary so that AB > DE. Cut off BG = DE on BA, with G strictly between B and A, and join GC. [1.3, P1]

**Step 3.** In triangles GBC and DEF, BG = DE, BC = EF, and ∠GBC = ∠ABC = ∠DEF. Hence side–angle–side gives ∠GCB = ∠DFE. By the hypothesis, therefore, ∠GCB = ∠ACB. But G lies strictly between A and B, so ∠GCB is a proper part of ∠ACB and is smaller than it. This contradiction proves AB = DE. [1.4, CN1, CN5]

**Step 4.** Now AB = DE, BC = EF, and their included angles ∠ABC and ∠DEF are equal. Side–angle–side gives AC = DF and ∠BAC = ∠EDF. Thus all the required equalities hold when the given equal sides adjoin the equal angles. [1.4]

**Step 5.** Next suppose AB = DE, the sides opposite the given equal angles at C and F. If BC and EF were unequal, interchange the triangles if necessary so that BC > EF. Cut off BH = EF on BC, with H strictly between B and C, and join AH. [1.3, P1]

**Step 6.** In triangles ABH and DEF, AB = DE, BH = EF, and ∠ABH = ∠ABC = ∠DEF. Side–angle–side therefore gives ∠AHB = ∠DFE = ∠ACB. But in triangle AHC, CH is produced through H to B, so the exterior angle ∠AHB is greater than the opposite interior angle ∠ACH. Since C, H, B lie on the same straight line in that order, ∠ACH = ∠ACB. This contradicts the equality just obtained. Consequently BC = EF. [1.4, CN1, 1.16]

**Step 7.** Finally, AB = DE, BC = EF, and ∠ABC = ∠DEF, so side–angle–side gives AC = DF and ∠BAC = ∠EDF. Thus, in either permitted case, the remaining corresponding sides and the remaining angle are equal, as required. [1.4]

**USED:** 1.16, 1.3, 1.4, CN1, CN5, P1
**Human refs (from References field):** 1.16, 1.4
**Jaccard:** 0.333 — AI adds ['1.3', 'CN1', 'CN5', 'P1']

## Proposition 1.27
**Statement:** If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

**Step 1.** Let the transversal meet the coplanar straight lines AB and CD at distinct points E and F, with A,E,B and C,F,D in these orders, and with A,C on one side of EF and B,D on the other. By hypothesis, ∠AEF = ∠EFD. We use the exterior-angle theorem (1.16), since a supposed intersection would immediately form a triangle to which it applies.

**Step 2.** Suppose the lines, produced if necessary, meet at G on the side of EF containing B and D. In triangle EFG, ∠AEF is an exterior angle, so it is greater than the interior opposite angle ∠EFG (1.16). But the rays FG and FD coincide, so ∠EFG = ∠EFD. Thus ∠AEF > ∠EFD, contradicting the hypothesis.

**Step 3.** Suppose instead that the lines meet at H on the side of EF containing A and C. In triangle EFH, ∠EFD is an exterior angle, so it is greater than the interior opposite angle ∠HEF (1.16). But the rays EH and EA coincide, so ∠HEF = ∠AEF. Thus ∠EFD > ∠AEF, again contradicting the hypothesis.

**Step 4.** Therefore the two coplanar straight lines, produced indefinitely, meet in neither direction. By the definition of parallel straight lines (D1.23), AB and CD are parallel, as required.

**USED:** 1.16, D1.23
**Human refs (from References field):** 1.16, D1.23
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.28
**Statement:** If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to two right angles, the straight lines will be parallel to one another.

**Step 1.** Let the transversal EF meet AB at G and CD at H, with E, G, H, F in that order. Label the points so that A, G, B and C, H, D are respectively in order, with A and C on the same side of the transversal. The hypotheses are either ∠EGB = ∠GHD or ∠BGH + ∠GHD equals two right angles. In both cases we use the direct alternate-angle criterion, 1.27, by establishing ∠AGH = ∠GHD.

**Step 2.** First suppose that the exterior angle ∠EGB equals the interior and opposite angle ∠GHD. The vertical angles ∠AGH and ∠EGB are equal by 1.15. Hence ∠AGH = ∠GHD by CN1.

**Step 3.** The angles ∠AGH and ∠GHD are alternate angles. Therefore AB is parallel to CD by 1.27. This proves the first case.

**Step 4.** Now suppose that the interior angles ∠BGH and ∠GHD together equal two right angles. Since GA and GB are opposite rays, 1.13 gives that ∠AGH + ∠BGH also equals two right angles. All right angles are equal by P4, so any two sums of two right angles are equal by CN2. Consequently, by CN1,
∠AGH + ∠BGH = ∠BGH + ∠GHD.

**Step 5.** Subtract the common angle ∠BGH from these equal sums. By CN3, ∠AGH = ∠GHD. These are alternate angles, so AB is parallel to CD by 1.27. Thus either stated condition makes the two straight lines parallel to one another.

**USED:** 1.13, 1.15, 1.27, CN1, CN2, CN3, P4
**Human refs (from References field):** 1.13, 1.15, 1.27
**Jaccard:** 0.429 — AI adds ['CN1', 'CN2', 'CN3', 'P4']

## Proposition 1.29
**Statement:** A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

**Step 1.** Let the parallel straight lines AB and CD be cut by a transversal at G and H. Label the points so that A,G,B and C,H,D occur in those orders, with A and C on one side of the transversal and B and D on the other. Let E lie on the transversal with E,G,H in that order. Since AB and CD are parallel, they do not meet in either direction. Write 2R for the magnitude of two right angles. [D1.23, P4]

**Step 2.** Put α = ∠AGH, β = ∠GHD, γ = ∠BGH, and δ = ∠GHC. The adjacent angles on each straight line give
α + γ = 2R and β + δ = 2R. [1.13]
We establish the alternate-angle equality first: a failure of this equality will give exactly the same-side interior-angle inequality to which the parallel postulate applies.

**Step 3.** Suppose α > β. Adding γ preserves this strict inequality: β + γ < α + γ = 2R. Here β and γ are the interior angles on the side containing B and D. Therefore AB and CD, produced indefinitely, meet on that side, contrary to their parallelism. If instead β > α, then α + δ < β + δ = 2R. Now α and δ are the interior angles on the side containing A and C, so the lines meet on that side, again a contradiction. The strict comparisons follow by viewing the smaller angle as a proper part of the larger and adjoining the same angle to both. Thus neither angle can exceed the other, and α = β: the alternate angles ∠AGH and ∠GHD are equal. [CN5, P5, D1.23]

**Step 4.** The exterior angle ∠EGB is vertically opposite to ∠AGH, so ∠EGB = ∠AGH. Since ∠AGH = ∠GHD by Step 3, it follows that ∠EGB = ∠GHD. Thus the exterior angle equals the interior and opposite angle. [1.15, CN1]

**Step 5.** Add γ to the equality α = β. Then α + γ = β + γ. Since α + γ = 2R by Step 2, we obtain
∠BGH + ∠GHD = γ + β = 2R.
Thus the interior angles on the same side equal two right angles. [CN2, CN1]
The labeling was arbitrary: interchanging the sides of the transversal or its two intersections gives the corresponding assertions for the other angle pairs. Hence a straight line falling on parallel straight lines makes the alternate angles equal, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

**USED:** 1.13, 1.15, CN1, CN2, CN5, D1.23, P4, P5
**Human refs (from References field):** 1.13, 1.15, CN1, CN2, P5
**Jaccard:** 0.625 — AI adds ['CN5', 'D1.23', 'P4']

## Proposition 1.30
**Statement:** Straight lines parallel to the same straight line are also parallel to one another.

**Step 1.** Let the distinct straight lines a and b both be parallel to the straight line c. Draw and, as necessary, produce a transversal meeting a, b, c at distinct points A, B, C respectively [P1, P2]. Interchange the names a and b if necessary so that A is an outermost intersection; thus B and C lie on the same ray from A. Choose a point X on a on one side of the transversal, and points Y on b and Z on c on its other side.

**Step 2.** Since a is parallel to c, the alternate angles ∠XAB and ∠ACZ are equal; here AB and AC are the same ray [1.29].

**Step 3.** Since b is parallel to c, ∠ABY = ∠ACZ by the exterior-angle–interior-opposite-angle equality [1.29]. Indeed, BA and CA point in the same direction: if B is nearer A, the angle at B is exterior and that at C interior; if C is nearer A, their roles are reversed.

**Step 4.** Both ∠XAB and ∠ABY equal ∠ACZ. Therefore ∠XAB = ∠ABY [CN1].

**Step 5.** These are alternate angles made by the transversal with a and b. We therefore use the alternate-angle criterion, which directly matches the equality obtained: a is parallel to b [1.27]. Thus straight lines parallel to the same straight line are also parallel to one another.

**USED:** 1.27, 1.29, CN1, P1, P2
**Human refs (from References field):** 1.29, CN1
**Jaccard:** 0.400 — AI adds ['1.27', 'P1', 'P2']

## Proposition 1.31
**Statement:** Through a given point to draw a straight line parallel to a given straight line.

**Step 1.** Let BC be the given straight line and A the given point outside it, in the same plane. Choose a point D on BC, distinct from C, and join AD. [P1]

**Step 2.** At A, on the straight line AD, construct the angle EAD equal to the angle ADC, taking E on the opposite side of AD from C. This choice makes the equal angles alternate angles. [1.23]

**Step 3.** Produce EA beyond A to F. Thus EF is a straight line passing through A. [P2]

**Step 4.** The straight line AD falls on EF and BC and makes the alternate angles EAD and ADC equal. Therefore EF is parallel to BC. We use the alternate-angle criterion directly because these are precisely the angles made equal by the construction. Hence through the given point A a straight line parallel to the given straight line BC has been drawn, as required. [1.27]

**USED:** 1.23, 1.27, P1, P2
**Human refs (from References field):** 1.23, 1.27
**Jaccard:** 0.500 — AI adds ['P1', 'P2']

## Proposition 1.32
**Statement:** In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

**Step 1.** Let ABC be any triangle, and produce BC through C to D, so that B, C, D lie in that order on one straight line. The exterior angle is ∠ACD. [P2]

**Step 2.** Through C draw a straight line parallel to AB, and choose its ray CE on the same side of BC as A; this ray divides the exterior angle ∠ACD. This parallel construction is the direct route, since the parallel-angle theorem supplies both required angle equalities. [1.31]

**Step 3.** Since AB is parallel to CE and AC falls across them, the alternate angles ∠BAC and ∠ACE are equal. Again, since the straight line BCD falls across the same parallels, the exterior angle ∠ECD equals the interior and opposite angle ∠ABC. We use 1.29 directly for both equalities. [1.29]

**Step 4.** Adding these equalities gives
∠BAC + ∠ABC = ∠ACE + ∠ECD.
Since CE divides ∠ACD, the sum on the right is ∠ACD. Therefore the exterior angle equals the two interior and opposite angles:
∠ACD = ∠BAC + ∠ABC. [CN2]

**Step 5.** The straight line CA stands on the straight line BCD. Hence the adjacent angles ∠ACB and ∠ACD together equal two right angles. [1.13]

**Step 6.** Add ∠ACB to both sides of the equality in Step 4. It follows that
∠BAC + ∠ABC + ∠ACB = ∠ACD + ∠ACB.
By Step 5, the latter sum equals two right angles. Thus the three interior angles of ABC equal two right angles. Together with Step 4, this proves both assertions. [CN2, CN1]

**USED:** 1.13, 1.29, 1.31, CN1, CN2, P2
**Human refs (from References field):** 1.13, 1.29, 1.31
**Jaccard:** 0.500 — AI adds ['CN1', 'CN2', 'P2']

## Proposition 1.33
**Statement:** The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.

**Step 1.** Let AB and CD be equal and parallel straight lines, with their endpoints named in the same direction, so that AC and BD join the corresponding extremities. Draw AC, BD, and the diagonal BC. [P1]

**Step 2.** Since AB is parallel to CD and BC falls upon them, the alternate angles ∠ABC and ∠DCB are equal. The diagonal thus supplies the included angles needed for a side–angle–side comparison. [1.29]

**Step 3.** In triangles ABC and DCB, AB equals DC by hypothesis, BC is common, and ∠ABC equals ∠DCB by Step 2. Therefore their bases AC and DB are equal, and their corresponding remaining angles ∠ACB and ∠DBC are equal. [1.4]

**Step 4.** The equal angles ∠ACB and ∠DBC are alternate angles made by BC falling on AC and BD. Hence AC is parallel to BD. We use the alternate-angle criterion because it applies directly to the angles just obtained. Together with AC = BD from Step 3, this proves that the straight lines joining the corresponding extremities are themselves equal and parallel. [1.27]

**USED:** 1.27, 1.29, 1.4, P1
**Human refs (from References field):** 1.27, 1.29, 1.4
**Jaccard:** 0.750 — AI adds ['P1']

## Proposition 1.34
**Statement:** In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.

**Step 1.** Let ABCD be a parallelogram, with vertices in order, so that AB is parallel to CD and BC is parallel to AD. Draw the diameter AC. [P1]

**Step 2.** Since AC falls on the parallel straight lines AB and CD, ∠BAC = ∠DCA. Since it also falls on the parallel straight lines BC and AD, ∠BCA = ∠DAC. These are alternate-angle equalities. [1.29]

**Step 3.** Compare triangles ABC and CDA. They have the two angle equalities just established, and the side AC adjoining those angles is common and therefore equal to itself. Apply 1.26, the direct choice because two angles and their adjoining side are already known equal. It follows that AB = CD, BC = DA, and ∠ABC = ∠CDA. Thus both pairs of opposite sides and one pair of opposite angles are equal. [CN4, 1.26]

**Step 4.** The diameter divides ∠BAD into ∠BAC and ∠CAD, and divides ∠BCD into ∠BCA and ∠ACD. By Step 2 these component angles are equal in pairs: ∠BAC = ∠ACD and ∠CAD = ∠BCA. Adding equals to equals gives ∠BAD = ∠BCD. Hence the other pair of opposite angles is also equal. [CN2]

**Step 5.** In triangles ABC and CDA, AB = CD by Step 3, AC is common, and the included angles ∠BAC and ∠DCA are equal by Step 2. Therefore the triangles are equal in area by 1.4, which explicitly supplies equality of the triangles, not merely equality of their sides and angles. These two triangles are precisely the two parts of the parallelogram separated by AC, so AC bisects its area. Either diameter can be designated AC by naming the vertices accordingly. Thus, in parallelogrammic areas, the opposite sides and angles are equal to one another, and the diameter bisects the areas. [CN4, 1.4]

**USED:** 1.26, 1.29, 1.4, CN2, CN4, P1
**Human refs (from References field):** 1.26, 1.29, 1.4, CN2
**Jaccard:** 0.667 — AI adds ['CN4', 'P1']

## Proposition 1.35
**Statement:** Parallelograms which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EBCF be the given parallelograms, with common base BC and with AD and EF lying on the same straight line parallel to BC. By 1.34, AD = BC, EF = BC, and AB = DC. Hence AD = EF. [1.34, CN1]

**Step 2.** If A and E coincide, then AD = EF makes D and F coincide also; the two parallelograms therefore coincide and are equal. Otherwise, interchange their names if necessary so that A precedes E along the upper parallel in the direction from A to D. Since AD = EF, D also precedes F. Thus D and E both lie between A and F, though their order relative to each other need not be specified. Draw AF. We shall use the common containing quadrilateral ABCF, avoiding any case distinction according to whether the upper sides overlap. [CN4, P1]

**Step 3.** Subtract the equal segments AD and EF from the same segment AF. The respective remainders are DF and AE; therefore AE = DF. [CN3]

**Step 4.** Since AB is parallel to DC, the straight line AF falling on these parallels makes the exterior angle CDF equal to the interior and opposite angle BAE. Hence ∠BAE = ∠CDF. [1.29]

**Step 5.** In triangles BAE and CDF, BA = CD by Step 1, AE = DF by Step 3, and their included angles are equal by Step 4. Apply 1.4 directly, since two sides and their included angle are known equal. Thus triangle ABE equals triangle DCF in area. [1.4]

**Step 6.** Within quadrilateral ABCF, the side DC separates parallelogram ABCD from triangle DCF; likewise, BE separates parallelogram EBCF from triangle ABE. Subtracting the equal triangles DCF and ABE from this same quadrilateral leaves equal remainders. Those remainders are precisely parallelograms ABCD and EBCF. Therefore parallelograms on the same base and in the same parallels are equal to one another. [CN3]

**USED:** 1.29, 1.34, 1.4, CN1, CN3, CN4, P1
**Human refs (from References field):** 1.29, 1.34, 1.4, CN1, CN2, CN3
**Jaccard:** 0.625 — AI adds ['CN4', 'P1']; Human adds ['CN2']

## Proposition 1.36
**Statement:** Parallelograms which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let ABCD and EFGH be parallelograms with equal bases BC and FG on one of two parallel straight lines, and opposite sides AD and EH on the other. Label the endpoints so that BC and EH run in the same direction. Join BE and CH (P1). We take the direct common-base route: compare both given parallelograms with the auxiliary quadrilateral EBCH.

**Step 2.** The opposite sides EH and FG of parallelogram EFGH are equal (1.34). Since BC = FG by hypothesis, BC = EH (CN1).

**Step 3.** BC and EH are also parallel, being on the given parallel straight lines. Therefore the straight lines BE and CH joining their corresponding extremities are parallel (1.33). Together with BC ∥ EH, this makes EBCH a parallelogram.

**Step 4.** Parallelograms ABCD and EBCH are on the same base BC and in the same given parallels. They are therefore equal in area (1.35).

**Step 5.** Parallelograms EFGH and EBCH are on the same base EH and in those same parallels. They too are equal in area (1.35).

**Step 6.** Thus ABCD and EFGH are each equal in area to EBCH, and hence are equal to one another (CN1). Therefore parallelograms on equal bases and in the same parallels are equal to one another.

**USED:** 1.33, 1.34, 1.35, CN1, P1
**Human refs (from References field):** 1.33, 1.34, 1.35, CN1
**Jaccard:** 0.800 — AI adds ['P1']

## Proposition 1.37
**Statement:** Triangles which are on the same base and in the same parallels are equal to one another.

**Step 1.** Let triangles ABC and DBC have the same base BC, with A and D on a straight line ℓ parallel to BC. Through B draw BE parallel to AC and BF parallel to DC, meeting ℓ at E and F respectively (1.31). Then AEBC and DFBC are parallelograms, since each has both pairs of opposite sides parallel.

**Step 2.** These parallelograms are on the same base BC and between the same parallels BC and ℓ. Therefore they are equal (1.35). The same-base theorem is the direct choice here because BC is common, not merely equal to another base.

**Step 3.** The diagonal AB bisects parallelogram AEBC, and the diagonal DB bisects parallelogram DFBC (1.34). Thus triangle ABC is half of the first parallelogram, and triangle DBC is half of the second.

**Step 4.** These halves must be equal. Indeed, if one exceeded the other by a nonzero area R, adding each half to itself would make the corresponding whole exceed the other whole by R + R (CN2). The whole–part principle would then make those wholes unequal (CN5), contradicting Step 2. Hence triangle ABC equals triangle DBC. Therefore triangles on the same base and in the same parallels are equal to one another.

**USED:** 1.31, 1.34, 1.35, CN2, CN5
**Human refs (from References field):** 1.31, 1.34, 1.35
**Jaccard:** 0.600 — AI adds ['CN2', 'CN5']

## Proposition 1.38
**Statement:** Triangles which are on equal bases and in the same parallels are equal to one another.

**Step 1.** Let triangles ABC and DEF have equal bases BC and EF on a straight line ℓ, with their vertices A and D on a straight line m parallel to ℓ. Through C draw a parallel to BA, meeting m at G; through F draw a parallel to ED, meeting m at H. Then BCGA and EFHD are parallelograms. [1.31]

**Step 2.** These parallelograms stand on the equal bases BC and EF and lie between the same parallels ℓ and m. Therefore they are equal in area. This is the direct equal-base route: the parallelogram theorem applies without replacing the given bases by a common base. [1.36]

**Step 3.** The diagonal AC bisects parallelogram BCGA, so triangle ABC is half of that parallelogram. Likewise, diagonal DF bisects parallelogram EFHD, so triangle DEF is half of that parallelogram. [1.34]

**Step 4.** These halves are equal. Indeed, if one half exceeded the other by a positive area, adding two copies would make its whole exceed the other whole by twice that excess: the equal smaller portions give equal totals, and the total with a positive excess is greater. This contradicts Step 2. Hence triangle ABC equals triangle DEF in area. Thus triangles on equal bases and in the same parallels are equal to one another. [CN2, CN5]

**USED:** 1.31, 1.34, 1.36, CN2, CN5
**Human refs (from References field):** 1.31, 1.34, 1.36
**Jaccard:** 0.600 — AI adds ['CN2', 'CN5']

## Proposition 1.39
**Statement:** Equal triangles which are on the same base and on the same side are also in the same parallels.

**Step 1.** Let ABC and DBC be equal triangles on the same base BC and on the same side of BC. If A=D, the parallel to BC through their common vertex gives the conclusion (1.31). Otherwise, join AD (P1). We shall prove that AD is parallel to BC.

**Step 2.** Suppose that AD is not parallel to BC. Draw through A a straight line ℓ parallel to BC (1.31), and produce BD as necessary (P2). The line BD must meet ℓ: otherwise BD would be parallel to ℓ (D1.23), and hence parallel to BC (1.30), although BD meets BC at B, contrary to D1.23. Denote their intersection by E. Since ℓ cannot cross BC, E is on the same side of BC as A and D, and therefore lies on the ray BD. Also E≠D, since otherwise ℓ would be AD. Join EC (P1).

**Step 3.** Triangles ABC and EBC have the same base BC and lie between the same parallels ℓ and BC. They are therefore equal (1.37). This is the direct same-base route: the base BC has not changed.

**Step 4.** By hypothesis, triangle ABC also equals triangle DBC. Consequently, triangles EBC and DBC are equal (CN1).

**Step 5.** But E and D are distinct points on the same ray from B. If E lies between B and D, triangle EBC is a proper part of triangle DBC; if D lies between B and E, triangle DBC is a proper part of triangle EBC. In either case the whole is greater than the part (CN5), contradicting Step 4. Thus the supposition is impossible, and AD is parallel to BC. Hence the equal triangles ABC and DBC are in the same parallels BC and AD, as required.

**USED:** 1.30, 1.31, 1.37, CN1, CN5, D1.23, P1, P2
**Human refs (from References field):** 1.31, 1.37, CN1
**Jaccard:** 0.375 — AI adds ['1.30', 'CN5', 'D1.23', 'P1', 'P2']

## Proposition 1.40
**Statement:** Equal triangles which are on equal bases and on the same side are also in the same parallels.

**Step 1.** Let ABC and DEF be equal triangles whose equal bases BC and EF lie on one straight line ℓ, with A and D on the same side of ℓ. Through A draw a straight line p parallel to ℓ. We shall show that D also lies on p. [1.31]

**Step 2.** The straight lines ED and p must meet. Otherwise they would be parallel; since ℓ is also parallel to p, ED would be parallel to ℓ, contrary to their meeting at E. Thus, producing ED if necessary, let its intersection with p be G. Since p does not meet ℓ and contains A, G is on the same side of ℓ as D; hence G lies on the ray from E through D. Join GF. [D1.23, 1.30, P2, P1]

**Step 3.** Triangles ABC and GEF are on the equal bases BC and EF and between the same parallels ℓ and p. They are therefore equal. This uses the equal-base theorem directly, rather than reducing the construction to a common base. Since ABC also equals DEF by hypothesis, GEF equals DEF. [1.38, CN1]

**Step 4.** If G were distinct from D, then, because both lie on the same ray from E, either G would lie between E and D or D would lie between E and G. In the first case triangle GEF would be a proper part of triangle DEF; in the second, triangle DEF would be a proper part of triangle GEF. Either case contradicts their equality, since the whole is greater than the part. Consequently G coincides with D. [CN5]

**Step 5.** Thus A and D both lie on p, which is parallel to the straight line ℓ containing BC and EF. Therefore the equal triangles on equal bases and on the same side are in the same parallels. [1.31]

**USED:** 1.30, 1.31, 1.38, CN1, CN5, D1.23, P1, P2
**Human refs (from References field):** 1.31, 1.38, CN1
**Jaccard:** 0.375 — AI adds ['1.30', 'CN5', 'D1.23', 'P1', 'P2']

## Proposition 1.41
**Statement:** If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.

**Step 1.** Let ABCD be a parallelogram, with vertices in order, and let ABE be a triangle on the same base AB and between the same parallels AB and CD. Thus E lies on the straight line CD. Draw the diagonal AC. [P1]

**Step 2.** Triangles ABC and ABE have the same base AB and lie between the same parallels AB and CD. They are therefore equal in area. The same-base triangle theorem applies directly, so no equal-base comparison is needed. [1.37]

**Step 3.** The diagonal AC bisects the parallelogram ABCD into the equal triangles ABC and ACD. [1.34]

**Step 4.** Since triangles ACD and ABE are each equal to triangle ABC, they are equal to one another. Thus each of the two triangles composing ABCD equals triangle ABE. Adding these equal areas, the parallelogram ABCD equals two copies of triangle ABE. Therefore the parallelogram is double the triangle, as required. [CN1, CN2]

**USED:** 1.34, 1.37, CN1, CN2, P1
**Human refs (from References field):** 1.34, 1.37
**Jaccard:** 0.400 — AI adds ['CN1', 'CN2', 'P1']

## Proposition 1.42
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let ABC be the given triangle and θ the given rectilineal angle. Bisect BC at E and join AE. Thus BE = EC. We use the half-base construction so that doubling the triangle on EC will recover the given triangle. [1.10, P1]

**Step 2.** At E, on EC, construct an angle CEF equal to θ, with EF on the same side of BC as A. Through A draw a straight line parallel to BC, and let EF meet it at F, producing the lines as necessary. [1.23, 1.31, P2]

**Step 3.** Through C draw CG parallel to EF, meeting the parallel through A at G, producing the lines as necessary. Since EC is parallel to FG and EF is parallel to CG, EFGC is a parallelogram. Its angle CEF equals the given angle θ. [1.31, P2; Step 2]

**Step 4.** The triangles ABE and AEC have equal bases BE and EC and lie between the same parallels BC and FG. Therefore they are equal. This is a direct application of the equal-base triangle theorem. Adding triangle AEC to each, the whole triangle ABC is double triangle AEC. [1.38, CN2]

**Step 5.** The parallelogram EFGC and triangle AEC have the same base EC and lie between the same parallels EC and FG. Therefore the parallelogram EFGC is double triangle AEC. [1.41]

**Step 6.** Both the given triangle ABC and the constructed parallelogram EFGC are equal to double triangle AEC; hence they are equal to one another. Since angle CEF equals θ, EFGC is the required parallelogram, equal to the given triangle and constructed in the given rectilineal angle. [CN1; Steps 2, 4–5]

**USED:** 1.10, 1.23, 1.31, 1.38, 1.41, CN1, CN2, P1, P2
**Human refs (from References field):** 1.23, 1.31, 1.38, 1.41
**Jaccard:** 0.444 — AI adds ['1.10', 'CN1', 'CN2', 'P1', 'P2']

## Proposition 1.43
**Statement:** In any parallelogram the complements of the parallelograms about the diameter are equal to one another.

**Step 1.** Let ABCD be a parallelogram with diameter AC. Let its two parallelograms about this diameter be AEKH and KFCG, where K lies on AC, E on AB, F on BC, G on CD, and H on DA; E, K, G are collinear, as are H, K, F. The complements are EBFK and HKGD. Write [X] for the area of a figure X. We take the direct diameter-bisection route, since it applies to the whole parallelogram and to both parallelograms about the diameter. By 1.34,
[ABC] = [ADC].

**Step 2.** AK is a diameter of parallelogram AEKH, and KC is a diameter of parallelogram KFCG. Applying 1.34 to each gives
[AEK] = [AHK] and [KFC] = [KGC].

**Step 3.** Adding these equal areas gives
[AEK] + [KFC] = [AHK] + [KGC].
This follows from CN2, that equals added to equals yield equal wholes.

**Step 4.** Triangle ABC is partitioned into triangle AEK, complement EBFK, and triangle KFC. Triangle ADC is partitioned into triangle AHK, complement HKGD, and triangle KGC. Subtract the equal sums in Step 3 from the equal triangles in Step 1. By CN3, the remaining areas are equal:
[EBFK] = [HKGD].
Therefore, in any parallelogram, the complements of the parallelograms about the diameter are equal to one another.

**USED:** 1.34, CN2, CN3
**Human refs (from References field):** 1.34, CN2, CN3
**Jaccard:** 1.000 — Perfect match.

## Proposition 1.44
**Statement:** To a given straight line to apply, in a given rectilineal angle, a parallelogram equal to a given triangle.

**Step 1.** Let AB be the given straight line, T the given triangle, and δ the given rectilineal angle. Construct a parallelogram BEFG equal in area to T, with ∠EBG = δ, and place it so that A, B, E lie in that order on one straight line. We use I.42 first because it supplies precisely the required area and angle; the prescribed side will then be obtained by equal complements. [1.42, P2]

**Step 2.** Through A draw AH parallel to BG, meeting FG produced beyond G at H, and join HB. Since BG is parallel to EF, AH is also parallel to EF. [1.31, P2, P1, 1.30]

**Step 3.** Since HF falls on the parallels AH and EF, the angles AHF and HFE together equal two right angles. But HB lies inside ∠AHF, so ∠BHF is less than ∠AHF. Consequently, ∠BHF and ∠HFE together are less than two right angles. Therefore HB and FE, produced, meet at K on that side of HF. In this configuration K lies beyond B on HB and beyond E on FE. [1.29, CN5, P2, P5]

**Step 4.** Through K draw a straight line parallel to FG, meeting HA produced at L and GB produced at M. Thus HFKL is a parallelogram, and HK is its diagonal, passing through B. The line ABE is parallel to its sides HF and LK, while the line GBM is parallel to its sides HL and FK. Hence HGBA and BEKM are the two parallelograms about the diagonal, and BEFG and ABML are their complements. In particular, ABML is a parallelogram with the prescribed side AB. [1.31, P2, 1.30]

**Step 5.** The complements of the parallelograms about a diagonal are equal. Therefore ABML equals BEFG in area. Since BEFG equals the given triangle T, ABML also equals T. [1.43, CN1]

**Step 6.** At B, BA and BE are opposite rays, as are BM and BG. Thus ∠ABM and ∠EBG are vertically opposite and equal. Since ∠EBG = δ, we have ∠ABM = δ. Therefore ABML is a parallelogram applied to the given straight line AB, equal to the given triangle T, and having the given rectilineal angle δ, as required. [1.15, CN1]

**USED:** 1.15, 1.29, 1.30, 1.31, 1.42, 1.43, CN1, CN5, P1, P2, P5
**Human refs (from References field):** 1.15, 1.29, 1.31, 1.42, 1.43, CN1, P5
**Jaccard:** 0.636 — AI adds ['1.30', 'CN5', 'P1', 'P2']

## Proposition 1.45
**Statement:** To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.

**Step 1.** Let Q be the given rectilineal figure and θ the given rectilineal angle. First divide Q into finitely many non-overlapping triangles T₁, …, Tₙ. An explicit construction, which does not require Q to be convex, is to draw through its vertices parallels to one chosen side, retaining existing lines where appropriate, and prolong them across Q. Between consecutive parallels there are no vertices in the open strip, so each portion of Q is bounded by two straight boundary edges and the strip boundaries: it is a triangle or a quadrilateral. Divide each quadrilateral by a diagonal. These triangles together constitute Q. [D1.19, 1.31, P2, P1]

**Step 2.** Construct a parallelogram ABCD equal to T₁, with ∠DAB equal to θ. Here the vertices are named consecutively. We use 1.42 first because no side has yet been prescribed; for subsequent triangles, 1.44 will allow attachment along an existing side. [1.42]

**Step 3.** Suppose ABCD is a parallelogram equal to the triangles already treated, and let T be the next triangle. Apply to BC a parallelogram BEFC equal to T, with ∠CBE equal to ∠BCD. Choose this parallelogram on the opposite side of BC from ABCD, so that their interiors do not overlap. [1.44]

**Step 4.** Since AB is parallel to DC, the interior angles ∠ABC and ∠BCD together equal two right angles. Substituting the equal angle ∠CBE gives that ∠ABC and ∠CBE together equal two right angles. Moreover, BA and BE lie on opposite sides of BC. Hence A, B, E lie on one straight line, with B between A and E.

Likewise, since BE is parallel to CF, the angles ∠CBE and ∠BCF together equal two right angles. Replacing ∠CBE by ∠BCD shows that ∠BCD and ∠BCF together equal two right angles. Since CD and CF lie on opposite sides of BC, D, C, F lie on one straight line, with C between D and F. [1.29, CN2, CN1, 1.14]

**Step 5.** Both AD and EF are parallel to BC, so AD is parallel to EF. Also, AE and DF lie respectively on the straight lines AB and DC, which are parallel. Thus AEFD is a parallelogram. Since AE has the same direction from A as AB, its angle ∠DAE is still equal to θ. [1.30, D1.23]

**Step 6.** The parallelogram AEFD consists exactly of ABCD and BEFC, joined along BC without overlapping interiors. The former equals the triangles already treated, and the latter equals T. Adding these equal areas, AEFD equals all the triangles treated together with T. Thus the construction preserves the prescribed angle while adding the next triangle’s area. [CN2]

**Step 7.** Repeat Steps 3–6 for each remaining triangle, relabelling the enlarged parallelogram ABCD before the next attachment. There are finitely many triangles, so the process ends with a parallelogram whose angle equals θ and whose area equals T₁, …, Tₙ taken together—that is, Q. Therefore a parallelogram equal to the given rectilineal figure has been constructed in the given rectilineal angle. [1.44, CN2]

**USED:** 1.14, 1.29, 1.30, 1.31, 1.42, 1.44, CN1, CN2, D1.19, D1.23, P1, P2
**Human refs (from References field):** 1.14, 1.29, 1.30, 1.33, 1.34, 1.42, 1.44, CN1, CN2
**Jaccard:** 0.500 — AI adds ['1.31', 'D1.19', 'D1.23', 'P1', 'P2']; Human adds ['1.33', '1.34']

## Proposition 1.46
**Statement:** On a given straight line to describe a square.

**Step 1.** Let AB be the given straight line. Choose the perpendicular-and-parallelogram construction, so that equality of opposite sides will supply the required equal sides. At A draw AE perpendicular to AB, and produce AE sufficiently far that AE is greater than AB. [1.11, P2]

**Step 2.** From AE cut off AD equal to AB. Thus AD = AB and angle DAB is right. [1.3]

**Step 3.** Through D draw a straight line parallel to AB, and through B draw a straight line parallel to AD; let these meet at C. Then AB is parallel to DC, and AD is parallel to BC, so ABCD is a parallelogram. [1.31]

**Step 4.** The opposite sides of this parallelogram are equal: AB = DC and AD = BC. Together with AD = AB, these equalities show that all four sides of ABCD are equal. [1.34, CN1]

**Step 5.** Since AD and BC are parallel, apply the interior-angle conclusion of 1.29 directly to the transversal AB: angles DAB and ABC together equal two right angles. Angle DAB is right; subtracting it shows that angle ABC is also right. The opposite angles of the parallelogram are equal, so angles BCD and CDA are likewise right. [1.29, P4, CN3, 1.34]

**Step 6.** Therefore ABCD is both equilateral and right-angled, and hence is a square. Thus a square has been described on the given straight line AB. [D1.22]

**USED:** 1.11, 1.29, 1.3, 1.31, 1.34, CN1, CN3, D1.22, P2, P4
**Human refs (from References field):** 1.11, 1.29, 1.31, 1.34
**Jaccard:** 0.400 — AI adds ['1.3', 'CN1', 'CN3', 'D1.22', 'P2', 'P4']

## Proposition 1.47
**Statement:** In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.

**Step 1.** Let ABC be a triangle with the angle BAC right. Construct externally the squares ABFG, ACKH, and BDEC, with vertices named in cyclic order. We use the direct area-dissection route, dividing the square on BC into two parallelograms. Each square has equal sides and right angles; its opposite sides are parallel, since the interior angles on the same side of a transversal are two right angles. [1.46, D1.22, 1.28]

**Step 2.** The angles BAC and BAG are right angles, and AC and AG lie on opposite sides of AB. Therefore C, A, G lie on one straight line. Similarly, the right angles CAB and CAH show that B, A, H lie on one straight line. [D1.22, P4, 1.14]

**Step 3.** Through A draw a straight line parallel to BD, and produce it to meet BC at M and DE at L. Since CE is also parallel to BD, this line is parallel to CE. It divides the square BDEC into the parallelograms BDLM and CELM: their other pairs of opposite sides lie on the parallel lines BC and DE. Join AD, FC, AE, and BK. [1.31, P2, 1.30, P1]

**Step 4.** The right angles DBC and FBA are equal. Adding the angle ABC to each gives
∠ABD = ∠FBC.
Also AB = FB and BD = BC, being sides of their respective squares. Thus triangles ABD and FBC are equal by the two-sides-and-included-angle criterion, which applies directly to these square sides and the established angle equality. In particular, their areas are equal. [D1.22, P4, CN2, 1.4]

**Step 5.** Parallelogram BDLM and triangle ABD have the same base BD and lie between the parallels BD and AL. Hence BDLM is double triangle ABD. Square ABFG and triangle FBC have the same base FB and lie between the parallels FB and AG, since C lies on AG produced. Hence ABFG is double triangle FBC. Proposition 1.41 is the direct comparison here because each pair has a common base and the same parallels. Since the triangles are equal, their doubles are equal; therefore BDLM equals the square ABFG. [1.41, CN2, CN1]

**Step 6.** Similarly, the right angles BCE and KCA are equal. Adding the angle ACB to each gives
∠ACE = ∠KCB.
Moreover, AC = CK and CE = CB, being sides of their respective squares. Consequently triangles ACE and KCB are equal by the two-sides-and-included-angle criterion, and so their areas are equal. [D1.22, P4, CN2, 1.4]

**Step 7.** Parallelogram CELM and triangle ACE have the same base CE and lie between the parallels CE and AL. Thus CELM is double triangle ACE. Square ACKH and triangle KCB have the same base CK and lie between the parallels CK and AH, since B lies on AH produced. Thus ACKH is double triangle KCB. The triangles are equal, so their doubles are equal; therefore CELM equals the square ACKH. [1.41, CN2, CN1]

**Step 8.** Adding these equal areas, BDLM together with CELM equals ABFG together with ACKH. But BDLM and CELM together constitute the whole square BDEC. Therefore the square on BC equals the squares on AB and AC together: the square on the side subtending the right angle equals the squares on the sides containing it. [CN2]

**USED:** 1.14, 1.28, 1.30, 1.31, 1.4, 1.41, 1.46, CN1, CN2, D1.22, P1, P2, P4
**Human refs (from References field):** 1.14, 1.4, 1.41, 1.46, CN2
**Jaccard:** 0.385 — AI adds ['1.28', '1.30', '1.31', 'CN1', 'D1.22', 'P1', 'P2', 'P4']

## Proposition 1.48
**Statement:** If in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right.

**Step 1.** Let ABC be a triangle such that the square on BC equals the squares on AB and AC together. Write S(XY) for the square on XY, understood as a magnitude. Thus S(BC) = S(AB) + S(AC). A square is equilateral and right-angled [D1.22]. We take the direct route of constructing an auxiliary right triangle and applying 1.47; once its three sides match those of ABC, 1.8 is the natural angle comparison.

**Step 2.** Produce CA through A, and draw at A a perpendicular to AC, taking its ray on the side of AC opposite B. Produce this ray sufficiently and cut off AD equal to AB. Join DC. Thus ∠DAC is right and AD = AB [P2, 1.11, 1.3, P1].

**Step 3.** Construct the squares on AD and DC [1.46]. Since AD = AB, the squares on AD and AB coincide when corresponding sides and corners are superposed: their sides are equal and their angles are all right. Hence S(AD) = S(AB) [D1.22, P4, CN4]. Adding the square on AC gives S(AD) + S(AC) = S(AB) + S(AC) [CN2].

**Step 4.** Since triangle DAC is right-angled at A, S(DC) = S(AD) + S(AC) [1.47]. By Step 3 and the hypothesis, both S(DC) and S(BC) equal S(AB) + S(AC). Therefore S(DC) = S(BC) [CN1].

**Step 5.** Consequently DC = BC. For if these sides were unequal, superposing a corner of the smaller square on a corner of the larger, with corresponding sides along the same rays, would place the smaller square as a proper part of the larger. The squares would then be unequal, since the whole is greater than its part, contrary to Step 4 [D1.22, P4, CN4, CN5].

**Step 6.** In triangles DAC and BAC, DA = BA by construction, AC is common, and DC = BC by Step 5. Therefore the angles contained by DA, AC and BA, AC are equal: ∠DAC = ∠BAC [1.8]. But ∠DAC is right by construction. Hence ∠BAC is right, which is the angle contained by the remaining two sides AB and AC. This proves the proposition.

**USED:** 1.11, 1.3, 1.46, 1.47, 1.8, CN1, CN2, CN4, CN5, D1.22, P1, P2, P4
**Human refs (from References field):** 1.47, 1.8
**Jaccard:** 0.154 — AI adds ['1.11', '1.3', '1.46', 'CN1', 'CN2', 'CN4', 'CN5', 'D1.22', 'P1', 'P2', 'P4']
