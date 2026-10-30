# Book 3 of Euclid's Elements — Step-by-Step AI Proofs (Run B)

## Proposition 3.1
**Statement:** To find the centre of a given circle.

**Step 1.** Let ABC be the given circle. It is required to find its centre.

**Step 2.** Draw any straight line AB within the circle, joining two points A, B on the circumference [P1].

**Step 3.** Bisect AB at the point D [1.10].

**Step 4.** From D, draw DC at right angles to AB [1.11], and produce DC in a straight line to E, where C and E are the points at which this perpendicular meets the circumference [P2].

**Step 5.** Bisect CE at F [1.10].

**Step 6.** I say that F is the centre of the circle ABC. For suppose it is not; if possible, let G be the centre, where G does not coincide with F.

**Step 7.** Since G is assumed to be the centre of the circle, by the definition of a circle all straight lines from G to the circumference are equal [D1.15, D1.16]. Therefore GA equals GB.

**Step 8.** Since D is the midpoint of AB, DA equals DB [by construction, Step 3]. The straight line GD is common to triangles GDA and GDB.

**Step 9.** Therefore in triangles GDA and GDB, the three sides GA, GD, DA are respectively equal to the three sides GB, GD, DB. By the SSS congruence theorem, triangle GDA is congruent to triangle GDB [1.8]. Therefore angle GDA equals angle GDB.

**Step 10.** When a straight line standing on another straight line makes the adjacent angles equal to one another, each of the equal angles is a right angle [D1.10]. Therefore angle GDA is a right angle.

**Step 11.** But angle FDA is also a right angle, since DC was drawn at right angles to AB at D [by construction, Step 4].

**Step 12.** Therefore angle GDA equals angle FDA, since all right angles are equal to one another [P4].

**Step 13.** But G does not coincide with F. Therefore one of these angles is a part of the other. This means a part equals the whole, which is impossible [CN5].

**Step 14.** Therefore G cannot be the centre of the circle. Since this argument holds for any point not coinciding with F, the point F is the centre of circle ABC.

**Step 15.** Therefore the centre of the given circle has been found, namely F. Q.E.F.

**USED:** 1.10, 1.11, 1.8, CN5, D1.10, D1.15, D1.16, P1, P2, P4
**Human refs (from References field):** 1.8, D1.10
**Jaccard:** 0.200 — AI adds ['1.10', '1.11', 'CN5', 'D1.15', 'D1.16', 'P1', 'P2', 'P4']

## Proposition 3.2
**Statement:** If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

**Step 1.** Let ABC be a circle, and let A and B be two points taken on its circumference. Join the straight line AB [P1]. We must show that AB falls within the circle.

**Step 2.** Find the centre E of circle ABC [3.1]. Join EA and EB [P1].

**Step 3.** Take an arbitrary point F on the straight line AB between A and B. We shall show that F lies within the circle by proving that EF is less than the radius.

**Step 4.** Since EA and EB are both straight lines drawn from the centre E to the circumference of circle ABC, we have EA = EB [D1.15].

**Step 5.** In triangle EAB, since EA = EB, the angles opposite these equal sides are equal: angle EAB = angle EBA [1.5].

**Step 6.** Consider triangle AEF (where F lies on AB between A and B). The angle EFA is an exterior angle of triangle AEF with respect to the side AF produced to B. Wait — more precisely, angle EFB is an exterior angle of triangle AEF, since when side AF is produced beyond F to B, angle EFB is exterior. Therefore angle EFB is greater than the interior and opposite angle EAF [1.16].

**Step 7.** Now angle EAF is the same angle as angle EAB (since F lies on AB). And angle EAB = angle EBA [from Step 5]. And angle EBA is the same angle as angle EBF (since F lies on AB). Therefore angle EFB > angle EBF.

**Step 8.** In triangle EBF, since angle EFB > angle EBF, the side opposite the greater angle is greater than the side opposite the lesser angle: EB > EF [1.19].

**Step 9.** But EB is a radius of circle ABC, being drawn from the centre E to the circumference [D1.15]. Therefore EF is less than the radius, which means point F lies within the circle.

**Step 10.** Since F was an arbitrary point on line segment AB, every point of AB lies within the circle. Therefore the straight line joining two points on the circumference of a circle falls within the circle [D1.15]. Q.E.D.

**USED:** 1.16, 1.19, 1.5, 3.1, D1.15, P1
**Human refs (from References field):** 1.16, 1.19, 1.5, 3.1
**Jaccard:** 0.667 — AI adds ['D1.15', 'P1']

## Proposition 3.3
**Statement:** If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

**Step 1.** Let ABC be a circle with centre F (found by 3.1), and let CD be a straight line through F that bisects a chord AB (not through the centre) at E, so that AE equals EB. We must show CD cuts AB at right angles. Conversely, suppose CD cuts AB at right angles at E; we must show AE equals EB.

**Part I: If CD bisects AB, then CD cuts AB at right angles.**

**Step 2.** Join FA and FB (P1). Since F is the centre of circle ABC and A, B lie on the circumference, FA equals FB (D1.15).

**Step 3.** In triangles FEA and FEB, we have: AE equals EB (given, CD bisects AB), FA equals FB (Step 2, radii), and FE is common. Therefore triangle FEA is congruent to triangle FEB, and angle FEA equals angle FEB (1.8, SSS congruence).

**Step 4.** Since FE stands on line AB making adjacent angles FEA and FEB equal to one another, each of the angles FEA and FEB is a right angle (D1.10). Therefore CD cuts AB at right angles.

**Part II: If CD cuts AB at right angles, then CD bisects AB.**

**Step 5.** Again let F be the centre, and suppose CD passes through F and meets AB at E at right angles, so that angle FEA and angle FEB are each right angles. Join FA and FB (P1).

**Step 6.** Since F is the centre and A, B are on the circle, FA equals FB (D1.15). Therefore the square on FA equals the square on FB.

**Step 7.** Since angle FEA is a right angle, the square on FA (the side subtending the right angle) equals the sum of the squares on FE and EA (1.47). Likewise, since angle FEB is a right angle, the square on FB equals the sum of the squares on FE and EB (1.47).

**Step 8.** Since the square on FA equals the square on FB (Step 6), the sum of the squares on FE and EA equals the sum of the squares on FE and EB (CN1). Subtracting the square on FE from each, the square on EA equals the square on EB (CN3).

**Step 9.** Since the square on EA equals the square on EB, and EA and EB are straight lines, EA equals EB. For if EA were greater than EB, the square on EA would be greater than the square on EB (which contradicts their equality), and similarly if EB were greater than EA. Therefore AE equals EB, and CD bisects AB.

**Step 10.** Therefore, if in a circle a straight line through the centre bisects a straight line not through the centre, it also cuts it at right angles; and if it cuts it at right angles, it also bisects it. Q.E.D.

**USED:** 1.47, 1.8, 3.1, CN1, CN3, D1.10, D1.15, P1
**Human refs (from References field):** 1.26, 1.5, 1.8, D1.10
**Jaccard:** 0.200 — AI adds ['1.47', '3.1', 'CN1', 'CN3', 'D1.15', 'P1']; Human adds ['1.26', '1.5']

## Proposition 3.4
**Statement:** If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.

**Step 1.** Let ABCD be a circle, and let AC and BD be two straight lines in the circle which cut one another at the point E, and let neither AC nor BD pass through the centre of the circle. I say that they do not bisect one another.

**Step 2.** For suppose, if possible, that they do bisect one another, so that AE equals EC and BE equals ED.

**Step 3.** Find the centre F of the circle ABCD [3.1]. Draw the straight line FE from F to E [P1].

**Step 4.** Since FE is a straight line through the centre F, and it bisects the chord AC (because AE equals EC by assumption), then by Proposition 3.3, FE cuts AC at right angles. Therefore the angle FEA is a right angle.

**Step 5.** Again, since FE is a straight line through the centre F, and it bisects the chord BD (because BE equals ED by assumption), then by Proposition 3.3, FE cuts BD at right angles. Therefore the angle FEB is a right angle.

**Step 6.** But the angle FEA was shown to be a right angle. Therefore the angle FEA equals the angle FEB, since all right angles are equal to one another [P4].

**Step 7.** But the angle FEA is greater than the angle FEB, since FEB is a part of FEA (the lines AC and BD are distinct chords meeting at E, neither passing through the centre, so they do not coincide, and the angle FEA contains the angle FEB as a part). This means the whole equals the part, which contradicts the common notion that the whole is greater than the part [CN5].

**Step 8.** Therefore AC and BD do not bisect one another. Q.E.D.

**USED:** 3.1, 3.3, CN5, P1, P4
**Human refs (from References field):** 3.1, 3.3
**Jaccard:** 0.400 — AI adds ['CN5', 'P1', 'P4']

## Proposition 3.5
**Statement:** If two circles cut one another, they will not have the same centre.

**Step 1.** Let circles ABC and CDG cut one another at the points C and B. Assume, for the sake of contradiction, that they have the same centre. Call this centre E.

**Step 2.** Join EC from E to the intersection point C. [P1]

**Step 3.** Draw any straight line EFG through E, meeting circle ABC at F and circle CDG at G, chosen so that F and G are distinct points on the same ray from E. Such a direction exists because the two circles are not identical (they cut one another, so each passes through points interior to the other and points exterior to the other), and therefore there is a radius direction along which the two circles meet the ray at different distances from E. Let F lie between E and G. [P1, P2]

**Step 4.** Because E is the centre of circle ABC, every straight line from E to the circumference of ABC equals every other. In particular, EC = EF. [D1.15, D1.16]

**Step 5.** Because E is the centre of circle CDG, every straight line from E to the circumference of CDG equals every other. In particular, EC = EG. [D1.15, D1.16]

**Step 6.** From Steps 4 and 5, EF = EG. [CN1]

**Step 7.** But F lies between E and G, so EF is a proper part of EG. Therefore EG is greater than EF, and EF is not equal to EG. [CN5]

**Step 8.** Step 6 contradicts Step 7. Therefore the assumption that the two circles have the same centre is false. Hence, if two circles cut one another, they do not have the same centre. Q.E.D.

**USED:** CN1, CN5, D1.15, D1.16, P1, P2
**Human refs (from References field):** D1.15
**Jaccard:** 0.167 — AI adds ['CN1', 'CN5', 'D1.16', 'P1', 'P2']

## Proposition 3.6
**Statement:** If two circles touch one another, they will not have the same centre.

**Step 1.** Let circle ABC and circle CDE touch one another at the point C. Suppose, for the sake of contradiction, that they have the same centre; call it F.

**Step 2.** First consider the case where the circles touch internally, so that circle CDE is within circle ABC. Join FC by P1, and draw any other straight line FEB through F, meeting the inner circle CDE at E and the outer circle ABC at B (by P1 and P2).

**Step 3.** Since F is the centre of circle ABC, we have FB = FC (by D1.15 and D1.16, all lines from the centre to the circumference are equal).

**Step 4.** Since F is the centre of circle CDE, we have FE = FC (by D1.15 and D1.16, all lines from the centre to the circumference are equal).

**Step 5.** Therefore FB = FE, since each equals FC (by CN1).

**Step 6.** But FE is a part of FB, since E lies between F and B on the line FEB. Therefore the whole FB equals its part FE, which contradicts CN5, which states that the whole is greater than the part.

**Step 7.** Now consider the case where the circles touch externally at C. By D1.15 and D1.16, the centre of a circle lies among the points within the circle. If F is the centre of circle ABC, then F lies within circle ABC. If F is also the centre of circle CDE, then F lies within circle CDE. But if two circles touch externally, a point inside one circle is outside the other (for if F were inside both, a line through F would cross both circumferences, making the circles cut one another rather than merely touch, contradicting D3.3 and the hypothesis). Therefore F cannot be the centre of both circles.

**Step 8.** In both cases, the assumption that the two circles have the same centre leads to a contradiction. Therefore, if two circles touch one another, they do not have the same centre. Q.E.D.

**USED:** CN1, CN5, D1.15, D1.16, D3.3, P1, P2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN1', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1', 'P2']

## Proposition 3.7
**Statement:** If on the diameter of a circle a point be taken which is not the centre of the circle, and from the point straight lines fall upon the circle, that will be greatest on which the centre is, the remainder of the same diameter will be least, and of the rest  the nearer to the straight line through the centre is always greater than the more remote, and only two equal straight lines will fall from the point on the circle, one on each side of the least straight line.

**Step 1.** Let ABCD be a circle with centre E and diameter AD. Let F be a point on AD distinct from E. Let B, C, G be points on the circumference such that B and C lie on the same side of diameter AD, with B nearer to A than C (that is, angle AEB < angle AEC), and G on the circumference distinct from these. Join EB, EC, EG [P1].

**Step 2.** Since E is the centre of the circle, EA = EB = EC = EG = ED, all being radii [D1.15, D1.16].

**Step 3.** PART I — FA IS GREATEST: Since F lies on diameter AD between E and D, we have FA = FE + EA [CN2]. Since EA = EB [D1.15], it follows that FA = FE + EB.

**Step 4.** In triangle BEF, the two sides FE and EB are together greater than the third side FB [1.20]. Therefore FA = FE + EB > FB.

**Step 5.** Since B was an arbitrary point on the circumference other than A, the line FA is greater than any other straight line from F to the circumference. Hence FA is greatest.

**Step 6.** PART II — FD IS LEAST: In triangle BEF, the two sides BF and FE are together greater than BE [1.20]. Since BE = ED [D1.15], we have BF + FE > ED.

**Step 7.** Since F lies between E and D, ED = EF + FD [CN2]. So BF + FE > EF + FD.

**Step 8.** Subtracting EF from both sides, BF > FD [CN3].

**Step 9.** Since B was an arbitrary point on the circumference other than D, the line FD is less than every other straight line from F to the circumference. Hence FD is least.

**Step 10.** PART III — NEARER TO FA IS GREATER THAN MORE REMOTE: Let B and C lie on the same side of AD with angle AEB < angle AEC, so that FB is nearer to FA than FC. Since F lies on line AD and E is also on AD, the angles BEF and BEA are supplementary: angle BEF + angle BEA = two right angles [1.13]. Likewise angle CEF + angle CEA = two right angles [1.13].

**Step 11.** Since angle AEB < angle AEC, subtracting from equals (both sums equal two right angles), we obtain angle BEF > angle CEF [CN3].

**Step 12.** In triangles BEF and CEF: EB = EC [D1.15], EF is common to both, and angle BEF > angle CEF. By Proposition 1.24, the base opposite the greater included angle is greater, so FB > FC.

**Step 13.** Hence the line from F nearer to FA is always greater than one more remote from FA. The same argument applies to points on the other side of diameter AD.

**Step 14.** PART IV — ONLY TWO EQUAL LINES, ONE ON EACH SIDE: First we show that on the same side of the diameter, no two distinct lines from F to the circumference can be equal. Suppose for contradiction that FB = FC with B and C distinct points on the same side of AD. In triangles BEF and CEF: EB = EC [D1.15], EF is common, and FB = FC. By Proposition 1.8 (SSS), the triangles are congruent, giving angle BEF = angle CEF. But then B and C lie at the same angle from EF on the same side of AD, so B and C are the same point, contradicting our assumption. Therefore no two equal lines from F reach the circumference on the same side of the diameter.

**Step 15.** Now we show that for each line FC (where C is on the circumference and FC is neither FA nor FD), there exists exactly one equal line on the opposite side. At E on line FE, construct angle FEH equal to angle FEC on the opposite side of AD [1.23], with H chosen on the circumference [P3, noting that EH = EC since both are radii].

**Step 16.** In triangles FEC and FEH: EC = EH [D1.15], EF is common, and angle FEC = angle FEH [by construction, 1.23]. By Proposition 1.4 (SAS), FC = FH.

**Step 17.** Therefore exactly two equal straight lines fall from F on the circle, one on each side of the least line FD. This completes the proof.

**USED:** 1.13, 1.20, 1.23, 1.24, 1.4, 1.8, CN2, CN3, D1.15, D1.16, P1, P3
**Human refs (from References field):** 1.20, 1.23, 1.24, 1.4
**Jaccard:** 0.333 — AI adds ['1.13', '1.8', 'CN2', 'CN3', 'D1.15', 'D1.16', 'P1', 'P3']

## Proposition 3.8
**Statement:** If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest   the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

**Step 1.** Let the given circle have center M, and let D be a point outside the circle. Draw line DA through M, meeting the circle at G (the nearer intersection) and A (the farther intersection), so that D, G, M, A are collinear in that order [P1, 3.1]. The line DA passes through the center. Let E, F be points on the concave circumference (the arc farther from D, containing A) such that E is nearer to the line through the center than F, meaning angle AME is less than angle AMF. Let H, K be points on the convex circumference (the arc nearer to D, containing G) such that H is nearer to G than K, meaning angle GMH is less than angle GMK. Join DE, DF, ME, MF, DH, DK, MH, MK [P1].

**Step 2.** Since M is the center of the circle, ME = MA, MF = MA, MH = MG, and MK = MG [D1.15].

**Step 3.** We show DA is the greatest line to the concave circumference. Consider triangle DME. Since D, M, E are not collinear (E is not on line DA), by 1.20, DE is less than DM + ME. Since ME = MA [D1.15], we have DM + ME = DM + MA = DA. Therefore DE is less than DA. The same argument applies to DF and to any other line from D to the concave circumference. Hence DA is greatest [1.20].

**Step 4.** We show that of lines to the concave circumference, the nearer to DA is greater than the more remote. Since D, M, A are collinear, angle DMA is a straight angle. Therefore angle DME + angle EMA equals two right angles, and angle DMF + angle FMA equals two right angles [1.13]. Since angle AME is less than angle AMF (E being nearer to A), it follows that angle DME is greater than angle DMF.

**Step 5.** In triangles DME and DMF, DM is common, ME = MF (both equal to MA) [D1.15], and angle DME is greater than angle DMF. By 1.24, the base DE is greater than the base DF. Hence the line to the concave circumference nearer to DA is always greater than the one more remote [1.24].

**Step 6.** We show DG is the least line to the convex circumference. Let H be any point on the convex circumference other than G. In triangle DMH, by 1.20, DH + MH is greater than DM. Since MH = MG [D1.15] and DM = DG + GM (as G lies between D and M), we have DH + MG > DG + GM, so DH > DG [CN3]. Therefore DG is less than every other line from D to the convex circumference, and DG is the least [1.20].

**Step 7.** We show that of lines to the convex circumference, the nearer to DG is less than the more remote. Since D, G, M are collinear (G between D and M), the angle DMH equals the angle GMH, and angle DMK equals angle GMK. Since H is nearer to G than K, angle DMH is less than angle DMK.

**Step 8.** In triangles DMH and DMK, DM is common, MH = MK (both equal to MG) [D1.15], and angle DMH is less than angle DMK. By 1.24, the base DH is less than the base DK. Hence the line to the convex circumference nearer to DG is always less than the more remote [1.24].

**Step 9.** We show that only two equal straight lines fall on the circle from D, one on each side of the least line DG. Given a line DE from D to the circle (with E on either circumference), construct angle DME' on the opposite side of line DA equal to angle DME [1.23], where E' is the point where ME' (with ME' = ME = radius) meets the circle [P3, D1.15]. In triangles DME and DME', DM is common, ME = ME' [D1.15], and angle DME equals angle DME' [by construction]. By 1.4, DE = DE'. Thus there exists an equal line on the other side.

**Step 10.** We show uniqueness: no two equal lines from D can fall on the same side. Suppose, for contradiction, that DE = DF where E and F are distinct points on the same side and are both on the concave circumference (or both on the convex circumference). If E is nearer to the line through the center than F, then by Steps 4-5 (concave case) DE is greater than DF, or by Steps 7-8 (convex case) DE is less than DF. In either case DE does not equal DF, contradicting the assumption. Therefore only two equal straight lines fall on the circle from the point, one on each side of the least line.

**USED:** P1, P3, D1.15, CN3, 1.4, 1.13, 1.20, 1.23, 1.24, 3.1

**USED:** 1.13, 1.20, 1.23, 1.24, 1.4, 3.1, CN3, D1.15, P1, P3
**Human refs (from References field):** 1.20, 1.21, 1.24, 1.4, 3.1
**Jaccard:** 0.364 — AI adds ['1.13', '1.23', 'CN3', 'D1.15', 'P1', 'P3']; Human adds ['1.21']

## Proposition 3.9
**Statement:** If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

**Step 1.** Let a point D be taken within circle ABC, and let more than two equal straight lines fall from D on the circle, namely DA, DB, and DC, such that DA = DB = DC.

**Step 2.** Suppose, for the sake of contradiction, that D is not the centre of circle ABC.

**Step 3.** Find the centre E of circle ABC [3.1].

**Step 4.** Since D is not the centre and E is, D and E are distinct points. Draw the straight line from D to E [P1] and produce it in both directions to meet the circle, forming a diameter of the circle through D [P2, D1.17].

**Step 5.** Since D is a point on this diameter which is not the centre of the circle, by Proposition 3.7, only two equal straight lines can fall from D on the circle, one on each side of the least straight line.

**Step 6.** But DA, DB, and DC are three equal straight lines falling from D on the circle, which is more than two. This contradicts the conclusion of Step 5.

**Step 7.** Therefore the assumption in Step 2 is false, and D is the centre of circle ABC [D1.16].

**Step 8.** Hence, if a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle. Q.E.F.

**USED:** 3.1, 3.7, D1.16, D1.17, P1, P2
**Human refs (from References field):** 1.8, 3.1, D1.10
**Jaccard:** 0.125 — AI adds ['3.7', 'D1.16', 'D1.17', 'P1', 'P2']; Human adds ['1.8', 'D1.10']

## Proposition 3.10
**Statement:** A circle does not cut a circle at more points than two.

**Step 1.** Suppose, for the sake of contradiction, that circle ABC and circle DEF cut one another at more than two points, namely at B, G, and F.

**Step 2.** Find the centre K of circle ABC. [3.1]

**Step 3.** Join KB, KG, and KF. [P1]

**Step 4.** Since K is the centre of circle ABC, and B, G, F are points on the circumference of circle ABC, we have KB = KG = KF, for all straight lines from the centre to the circumference of a circle are equal. [D1.15]

**Step 5.** Now B, G, and F also lie on the circumference of circle DEF. Thus from the point K, which lies inside or on circle DEF, there fall three equal straight lines KB, KG, KF upon circle DEF.

**Step 6.** Since more than two equal straight lines fall from the point K on circle DEF, the point K is the centre of circle DEF. [3.9]

**Step 7.** Therefore K is the centre of both circle ABC and circle DEF. But the two circles cut one another, and if two circles cut one another they do not have the same centre. [3.5]

**Step 8.** This is a contradiction. Therefore the assumption that the two circles cut one another at more than two points is false.

**Step 9.** Hence a circle does not cut a circle at more points than two. Q.E.F.

**USED:** 3.1, 3.5, 3.9, D1.15, P1
**Human refs (from References field):** 3.1, 3.5
**Jaccard:** 0.400 — AI adds ['3.9', 'D1.15', 'P1']

## Proposition 3.11
**Statement:** If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.

**Step 1.** Let two circles ABC (the larger) and ADE (the smaller) touch one another internally at the point A, and let G be the center of circle ABC and H be the center of circle ADE. We must show that the straight line GH, when produced, passes through A.

**Step 2.** Suppose, for the sake of contradiction, that the line GH produced does not pass through A. Let the line from G through H, produced beyond H, meet the larger circle ABC at B, and let it meet the smaller circle ADE at E.

**Step 3.** Since G is the center of circle ABC, we have GA = GB, by the definition of a circle [D1.15, D1.16].

**Step 4.** Since H is the center of circle ADE, we have HA = HE, by the definition of a circle [D1.15, D1.16].

**Step 5.** Since H lies inside the larger circle (the smaller circle being internal to the larger), the point H lies between G and B on line GB. Therefore GB = GH + HB [CN2].

**Step 6.** Since E lies on the smaller circle ADE and B lies on the larger circle ABC, and the smaller circle lies inside the larger, the point E lies between H and B on line HB. Therefore HB = HE + EB, and so HB is greater than HE [CN5].

**Step 7.** Now consider triangle GHA (which exists since by our assumption A does not lie on line GH). By the triangle inequality, GH + HA > GA [1.20].

**Step 8.** Since GA = GB (Step 3) and GB = GH + HB (Step 5), we have GA = GH + HB. Therefore GH + HA > GH + HB [substituting from Step 5 into Step 7].

**Step 9.** Subtracting GH from both sides, HA > HB [CN3].

**Step 10.** But HA = HE (Step 4), so HE > HB.

**Step 11.** This contradicts Step 6, which established that HB is greater than HE.

**Step 12.** Therefore our assumption is false, and the line GH produced must pass through the point of contact A. Q.E.D.

**USED:** 1.20, CN2, CN3, CN5, D1.15, D1.16
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['1.20', 'CN2', 'CN3', 'CN5', 'D1.15', 'D1.16']

## Proposition 3.12
**Statement:** If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

**Step 1.** Let the two circles with centres F and G touch one another externally at the point C. Join FG [P1]. I say that FG passes through C.

**Step 2.** Suppose, for the sake of contradiction, that FG does not pass through C. Join FC and GC [P1].

**Step 3.** Since F is the centre of the first circle, FC is a radius of that circle [D1.15, D1.16]. Let the straight line FG meet the circumference of the first circle at the point H (on the side toward G). Then FH is also a radius of the first circle, so FC = FH [D1.15].

**Step 4.** Since G is the centre of the second circle, GC is a radius of that circle [D1.15, D1.16]. Let the straight line GF meet the circumference of the second circle at the point K (on the side toward F). Then GK is also a radius of the second circle, so GC = GK [D1.15].

**Step 5.** Since by our assumption the line FG does not pass through C, the points F, C, G are not collinear, and so FCG is a triangle. By the triangle inequality [1.20], FC + CG > FG.

**Step 6.** Since FC = FH and GC = GK (from Steps 3 and 4), we have FH + GK > FG [CN1].

**Step 7.** Now, H lies on the first circle along line FG between F and G, and K lies on the second circle along line FG between F and G. Since the two circles touch one another externally and do not cut one another [D3.3], they are external to each other, so H and K are distinct points both lying between F and G on the segment FG. (If H and K were the same point, that point would lie on both circles and hence would be a point of contact. Since the circles touch at C, this point would be C. But then FG would pass through C, contradicting our assumption.)

**Step 8.** Since H and K are distinct points on the segment FG with H between F and K, and K between H and G, we have FG = FH + HK + KG. Since HK is a positive length, FG > FH + GK [CN5].

**Step 9.** But Step 6 established FH + GK > FG. This contradicts Step 8, which established FG > FH + GK.

**Step 10.** Therefore the assumption is false, and the straight line FG joining the centres must pass through the point of contact C. Q.E.D.

**USED:** 1.20, CN1, CN5, D1.15, D1.16, D3.3, P1
**Human refs (from References field):** 1.20
**Jaccard:** 0.143 — AI adds ['CN1', 'CN5', 'D1.15', 'D1.16', 'D3.3', 'P1']

## Proposition 3.13
**Statement:** A circle does not touch a circle at more points than one, whether it touch it internally or externally.

**Step 1.** Suppose, for the sake of contradiction, that a circle touches a circle at more than one point.

**Case I: Internal tangency.**

**Step 2.** Let circle ABDC touch circle EBFD internally at the two points B and D. [D3.3]

**Step 3.** Find the center G of circle ABDC and the center H of circle EBFD. [3.1]

**Step 4.** Join G and H, and produce the line GH. [P1, P2]

**Step 5.** Since the two circles touch internally at B, the straight line joining their centers G and H, when produced, falls on the point of contact B. [3.11]

**Step 6.** Similarly, since the two circles touch internally at D, the straight line GH produced falls on D as well. [3.11]

**Step 7.** Therefore B and D both lie on the straight line GH. That is, G, H, B, and D are all collinear.

**Step 8.** Since G is the center of circle ABDC, and B and D are on its circumference, GB equals GD. [D1.15]

**Step 9.** Since H is the center of circle EBFD, and B and D are on its circumference, HB equals HD. [D1.15]

**Step 10.** Since G, H, B, D are collinear, and GB equals GD, the point G is equidistant from B and D along the line, so G is the midpoint of segment BD (for if B and D are distinct points on a line and G lies on that line with GB equal to GD, then G bisects BD).

**Step 11.** By the same reasoning, since HB equals HD and H lies on line BD, H is also the midpoint of segment BD.

**Step 12.** Therefore G coincides with H, that is, the two circles have the same center. [CN1]

**Step 13.** But this contradicts Proposition 3.6, which states that if two circles touch one another (internally), they do not have the same center. [3.6]

**Step 14.** Therefore two circles cannot touch one another internally at more than one point.

**Case II: External tangency.**

**Step 15.** Now let circle ACK touch circle ABDC externally at two points A and C. [D3.3]

**Step 16.** Join A to C. [P1]

**Step 17.** Since A and C are both points on the circumference of circle ABDC, the straight line AC falls within circle ABDC. [3.2]

**Step 18.** But circle ACK touches circle ABDC externally, so circle ACK is outside circle ABDC except at the points of contact. [D3.3]

**Step 19.** Since A and C are both on the circumference of circle ACK, the straight line AC falls within circle ACK. [3.2]

**Step 20.** Therefore the line segment AC lies inside both circles simultaneously. But since the circles touch externally, any point between A and C that is inside circle ABDC should be outside circle ACK, and vice versa. Having AC inside both circles means the circles share interior points, so the circles cut one another. [3.2]

**Step 21.** But this contradicts the hypothesis that the circles touch one another, since by definition circles that touch do not cut one another. [D3.3]

**Step 22.** Therefore two circles cannot touch one another externally at more than one point.

**Step 23.** Hence a circle does not touch a circle at more points than one, whether it touch it internally or externally. Q.E.D.

**USED:** 3.1, 3.11, 3.2, 3.6, CN1, D1.15, D3.3, P1, P2
**Human refs (from References field):** 3.11, 3.2, D3.3
**Jaccard:** 0.333 — AI adds ['3.1', '3.6', 'CN1', 'D1.15', 'P1', 'P2']

## Proposition 3.14
**Statement:** In a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another.

**Step 1.** Let ABDC be a circle with centre E, and let AB and CD be straight lines in the circle. We prove both directions: (i) if AB equals CD, they are equally distant from the centre, and (ii) if they are equally distant from the centre, they are equal.

**Step 2.** Draw EF from E perpendicular to AB, and EG from E perpendicular to CD [P1]. Join EA and EC [P1].

**Step 3.** Since EF is a straight line through the centre E and is perpendicular to chord AB (which does not pass through the centre), EF bisects AB [3.3]. Therefore AF equals FB. Likewise, since EG is perpendicular to chord CD, EG bisects CD [3.3]. Therefore CG equals GD.

**Step 4.** (Part i: Equal chords implies equidistant.) Suppose AB equals CD. Since AB equals the sum AF plus FB, and AF equals FB, we have AB equals twice AF. Likewise CD equals twice CG. Since AB equals CD, twice AF equals twice CG, so AF equals CG [CN3, subtracting equals from equals: AF from twice AF and CG from twice CG, i.e., AB minus AF equals CD minus CG gives FB equals GD, but since AF equals FB and CG equals GD, AF equals CG].

**Step 5.** Since EA and EC are radii of circle ABDC, EA equals EC [D1.15].

**Step 6.** In right triangle AEF, the square on EA equals the sum of the squares on EF and AF [1.47]. In right triangle CEG, the square on EC equals the sum of the squares on EG and CG [1.47].

**Step 7.** Since EA equals EC [Step 5], the square on EA equals the square on EC [CN1]. Since AF equals CG [Step 4], the square on AF equals the square on CG. Therefore, subtracting equals from equals, the square on EF equals the square on EG [CN3].

**Step 8.** Since the square on EF equals the square on EG, EF equals EG. Therefore, by the definition of equal distance from the centre, AB and CD are equally distant from the centre [D3.4].

**Step 9.** (Part ii: Equidistant implies equal chords.) Now suppose conversely that AB and CD are equally distant from the centre, so that EF equals EG [D3.4].

**Step 10.** As before, EA equals EC (radii) [D1.15], so the square on EA equals the square on EC. And since EF equals EG, the square on EF equals the square on EG.

**Step 11.** By 1.47, the square on EA equals the squares on EF and AF together, and the square on EC equals the squares on EG and CG together. Subtracting the equal squares on EF and EG respectively, the square on AF equals the square on CG [CN3].

**Step 12.** Therefore AF equals CG. Since AF equals FB [Step 3] and CG equals GD [Step 3], adding equals to equals, AF plus FB equals CG plus GD [CN2]. That is, AB equals CD.

**Step 13.** Therefore in a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another. Q.E.D.

**USED:** 1.47, 3.3, CN1, CN2, CN3, D1.15, D3.4, P1
**Human refs (from References field):** 1.47, 3.1, 3.3, D3.4
**Jaccard:** 0.333 — AI adds ['CN1', 'CN2', 'CN3', 'D1.15', 'P1']; Human adds ['3.1']

## Proposition 3.15
**Statement:** Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

**Step 1.** Let ABCD be a circle with centre E, and let BC be a diameter. Let AD be any chord that is not a diameter, and let FG be another chord such that AD is nearer to the centre than FG. We must prove (i) BC is greater than AD, and (ii) AD is greater than FG.

**Step 2.** [Part (i): The diameter is greatest.] Join EA and ED from centre E to the endpoints of chord AD [P1]. Since E is the centre of the circle, EA and ED are radii, so EA = EB and ED = EC [D1.15].

**Step 3.** In triangle EAD, by the triangle inequality, EA + ED > AD [1.20].

**Step 4.** Since EA = EB and ED = EC, substituting gives EB + EC > AD [CN1]. But EB + EC = BC (since B, E, C are collinear with E between B and C, as BC is a diameter through the centre E) [D1.17]. Therefore BC > AD.

**Step 5.** Since AD was an arbitrary chord that is not a diameter, the diameter BC is greater than every other straight line in the circle. This completes Part (i).

**Step 6.** [Part (ii): The nearer chord is greater than the more remote.] Draw EH perpendicular to AD and EK perpendicular to FG from centre E [P1]. Since AD is nearer to the centre than FG, we have EH less than EK [D3.4, D3.5].

**Step 7.** Since EH is drawn from the centre and is perpendicular to chord AD, EH bisects AD, so AH = HD [3.3]. Similarly, since EK is perpendicular to chord FG, EK bisects FG, so FK = KG [3.3].

**Step 8.** In right triangle EHA, by the Pythagorean theorem, the square on EA equals the sum of the squares on EH and HA [1.47]. In right triangle EKG, the square on EG equals the sum of the squares on EK and KG [1.47].

**Step 9.** Since EA and EG are both radii of the same circle, EA = EG [D1.15], and therefore the square on EA equals the square on EG. Hence the square on EH plus the square on HA equals the square on EK plus the square on KG.

**Step 10.** Since EH is less than EK, the square on EH is less than the square on EK. Therefore the square on HA is greater than the square on KG (for if it were not, the sum of the squares on EH and HA would not equal the sum of the squares on EK and KG).

**Step 11.** Since the square on HA is greater than the square on KG, HA is greater than KG. For if HA were equal to KG, their squares would be equal [CN4], and if HA were less than KG, the square on HA would be less than the square on KG; both contradict Step 10.

**Step 12.** Since AH = HD, we have AD = AH + HD = HA + HA [CN2]. Similarly, FG = FK + KG = KG + KG [CN2]. Since HA is greater than KG, adding HA to itself gives a sum greater than adding KG to itself, so AD is greater than FG.

**Step 13.** Therefore, of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote. Q.E.D.

**USED:** 1.20, 1.47, 3.3, CN1, CN2, CN4, D1.15, D1.17, D3.4, D3.5, P1
**Human refs (from References field):** 1.20, 1.24, 3.14, D3.5
**Jaccard:** 0.154 — AI adds ['1.47', '3.3', 'CN1', 'CN2', 'CN4', 'D1.15', 'D1.17', 'D3.4', 'P1']; Human adds ['1.24', '3.14']

## Proposition 3.16
**Statement:** The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

**Step 1.** Let there be a circle with center F and diameter BC. Let BA be the straight line drawn from the extremity B of the diameter at right angles to BC [D1.10]. I say first that the straight line BA falls outside the circle.

**Step 2.** For suppose it does not, but if possible let it fall within the circle as BD, where D is a point on BA that lies on or within the circle. Join FD [P1].

**Step 3.** Since FA equals FB (both being radii of the circle) [D1.15], and angle FBD is a right angle (since BA is drawn at right angles to the diameter at B) [construction, D1.10], triangle FBD has a right angle at B.

**Step 4.** In triangle FBD, since the angle FBD is a right angle, the sum of angles FBD and BDF is less than two right angles [1.17]. Since angle FBD is itself a right angle, angle BDF must be less than a right angle.

**Step 5.** Therefore angle FBD is greater than angle BDF. But in any triangle the greater angle is subtended by the greater side [1.19], so FD is greater than FB.

**Step 6.** But FB is a radius of the circle, and since FD is greater than the radius, the point D lies outside the circle [D1.15]. This contradicts the assumption that D lies on or within the circle.

**Step 7.** Since D was an arbitrary point on BA other than B, every point of the line BA other than B lies outside the circle. Therefore the straight line drawn at right angles to the diameter from its extremity falls outside the circle.

**Step 8.** I say next that no other straight line can be interposed between the straight line BA and the circumference. For suppose, if possible, that a straight line BG can be placed in the space between the straight line BA and the circumference, so that BG does not cut the circle.

**Step 9.** From the center F, draw FH perpendicular to BG [1.12]. Then angle FHB is a right angle [D1.10].

**Step 10.** Now since BG lies between BA and the circumference, the angle FBG (that is, the angle between the diameter BF produced and BG) is less than the angle FBA. But angle FBA is a right angle [construction]. Therefore angle FBG is less than a right angle, meaning angle FBG is acute.

**Step 11.** In triangle FBH, the angle FHB is a right angle and angle FBH (which equals angle FBG) is acute. Since angle FHB is greater than angle FBH, the side FB opposite the greater angle is greater than the side FH opposite the lesser angle [1.19]. Therefore FB is greater than FH, that is, the radius is greater than FH.

**Step 12.** Since FH is less than the radius FB, the foot of the perpendicular H lies inside the circle [D1.15]. The line BG passes through B (a point on the circumference) and through a region inside the circle (near H). Therefore the line BG, when produced, must meet the circumference at a second point; that is, BG cuts the circle.

**Step 13.** But this contradicts the assumption that BG does not cut the circle. Therefore no straight line can be interposed between the straight line BA and the circumference.

**Step 14.** I say further that the angle of the semicircle, namely the angle contained by the diameter BC and the circumference on the side of BA, is greater than any acute rectilineal angle, and the remaining angle between BA and the circumference is less than any acute rectilineal angle.

**Step 15.** For let there be any acute rectilineal angle; suppose the angle FBG is an acute rectilineal angle less than a right angle. Then the line BG falls between BA and the diameter BC (since angle FBG is acute and angle FBA is right) on the side toward the circumference.

**Step 16.** By the argument of Steps 9 through 13, any such line BG must cut the circumference. Therefore the line BG falls within the region between the diameter and the circumference, meaning it falls inside the angle of the semicircle.

**Step 17.** Since every acute rectilineal angle FBG results in a line BG that falls within the angle of the semicircle (between the diameter and the arc), the angle of the semicircle is greater than any acute rectilineal angle [CN5, as the whole is greater than the part].

**Step 18.** Conversely, since BA is at right angles to BC, the remaining angle between BA and the circumference (the horn angle on the other side) is contained within the angle FBG for every acute rectilineal angle FBG. For the line BG always crosses the circumference before reaching BA, leaving the horn angle between the arc and BA as a proper part of any acute rectilineal angle.

**Step 19.** Therefore the remaining angle between BA and the circumference is less than any acute rectilineal angle [CN5]. This completes the proof.

**USED:** 1.12, 1.17, 1.19, CN5, D1.10, D1.15, D1.17, D3.2, P1
**Human refs (from References field):** 1.17, 1.19, 1.5
**Jaccard:** 0.200 — AI adds ['1.12', 'CN5', 'D1.10', 'D1.15', 'D1.17', 'D3.2', 'P1']; Human adds ['1.5']

## Proposition 3.17
**Statement:** From a given point to draw a straight line touching a given circle.

**Step 1.** Let A be the given point and let BCD be the given circle. Find the centre E of the given circle [3.1].

**Step 2.** Join AE [P1], and let AE meet the circle BCD at D (so that D lies between A and E, since A is outside the circle).

**Step 3.** With centre E and radius EA, describe a circle AFG [P3]. Since EA is greater than ED (the radius of circle BCD), circle AFG is larger than circle BCD.

**Step 4.** From D, draw DF at right angles to EA [1.11], where F is the point at which this perpendicular meets circle AFG.

**Step 5.** Join EF [P1]. Since EF passes from the centre E to the circumference F of circle AFG, and EB is a radius of circle BCD, the line EF (being equal to EA, both radii of circle AFG) is greater than EB (a radius of the smaller circle BCD). Therefore EF, starting from E inside circle BCD, extends beyond circle BCD. Let B be the point where EF meets circle BCD.

**Step 6.** Join AB [P1].

**Step 7.** Now consider triangles DEF and BEA. We have: DE = BE (both radii of circle BCD), EF = EA (both radii of circle AFG), and angle DEF equals angle BEA (they are the same angle at E). Therefore, by the side-angle-side criterion, triangle DEF is congruent to triangle BEA [1.4].

**Step 8.** From the congruence, angle EDF equals angle EBA. But angle EDF is a right angle (by the construction in Step 4). Therefore angle EBA is also a right angle.

**Step 9.** Since EB is a radius of circle BCD and AB makes a right angle with EB at B (a point on the circumference), the straight line AB, drawn at right angles to the diameter at its extremity, falls outside the circle [3.16]. Therefore AB meets circle BCD at B and, being produced, does not cut the circle. Hence AB touches the circle BCD at B [D3.2].

**Step 10.** Therefore from the given point A, the straight line AB has been drawn touching the given circle BCD. Q.E.F.

**USED:** 1.11, 1.4, 3.1, 3.16, D3.2, P1, P3
**Human refs (from References field):** 1.4, 3.1, 3.16
**Jaccard:** 0.429 — AI adds ['1.11', 'D3.2', 'P1', 'P3']

## Proposition 3.18
**Statement:** If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.

**Step 1.** Let the straight line DE touch the circle ABC at the point C, and let F be the centre of the circle ABC, found by 3.1. Join FC by P1. We are to show that FC is perpendicular to DE.

**Step 2.** Suppose, for the sake of contradiction, that FC is not perpendicular to DE.

**Step 3.** From F, draw FG perpendicular to the line DE, meeting DE at the point G, by 1.12. Since FC is not perpendicular to DE by assumption, G is a point on DE distinct from C.

**Step 4.** Consider triangle FGC. The angle FGC is a right angle by construction (since FG was drawn perpendicular to DE).

**Step 5.** By 1.17, any two angles of a triangle are together less than two right angles. Applying this to triangle FGC, angles FGC and FCG are together less than two right angles. Since angle FGC is itself a right angle, it follows that angle FCG is less than a right angle. Therefore angle FGC is greater than angle FCG.

**Step 6.** By 1.19, in any triangle the greater side is opposite the greater angle. In triangle FGC, since angle FGC is greater than angle FCG, the side FC (opposite angle FGC) is greater than the side FG (opposite angle FCG). That is, FC > FG.

**Step 7.** Now FC is a radius of the circle, since F is the centre and C is on the circumference. Since FG is less than FC, the point G is nearer to the centre F than the circumference of the circle, and hence G lies within the circle, by the definition of a circle (D1.15).

**Step 8.** But G lies on the straight line DE. Since DE passes through G, which is a point within the circle, the line DE must cross the circumference of the circle at some point other than C. That is, DE cuts the circle.

**Step 9.** However, DE is given as a tangent to the circle at C. By the definition of a tangent (D3.2), a tangent is a straight line which meets the circle and, being produced, does not cut the circle. Thus DE does not cut the circle, which contradicts Step 8.

**Step 10.** Therefore the supposition in Step 2 is false, and FC is perpendicular to DE (D1.10). That is, the straight line joined from the centre to the point of contact is perpendicular to the tangent. Q.E.D.

**USED:** 1.12, 1.17, 1.19, 3.1, D1.10, D1.15, D3.2, P1
**Human refs (from References field):** 1.17, 1.19
**Jaccard:** 0.250 — AI adds ['1.12', '3.1', 'D1.10', 'D1.15', 'D3.2', 'P1']

## Proposition 3.19
**Statement:** If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so drawn.

**Step 1.** Let the straight line DE touch the circle ABC at the point C, and from C let CA be drawn at right angles to DE. I say that the centre of the circle ABC is on the line CA.

**Step 2.** Suppose it is not; let the centre, if possible, be at a point F not on CA. By Proposition 3.1, the centre of a given circle can be found; let F be that centre. Join FC [P1].

**Step 3.** Since DE touches the circle ABC at C, and FC has been joined from the centre F to the point of contact C, by Proposition 3.18 the line FC is perpendicular to DE. Therefore angle FCD is a right angle [D1.10].

**Step 4.** But angle ACD is also a right angle, since CA was drawn at right angles to DE (by hypothesis).

**Step 5.** Therefore angle FCD equals angle ACD, since all right angles are equal to one another [P4].

**Step 6.** But angle FCD is a part of angle ACD, since F does not lie on CA and thus FC falls between CA and CD, making angle FCD strictly less than angle ACD. Therefore a part equals the whole, which is impossible [CN5].

**Step 7.** Therefore the assumption that the centre F does not lie on CA leads to a contradiction. Hence the centre of the circle ABC lies on the straight line CA drawn from the point of contact at right angles to the tangent DE. Q.E.D.

**USED:** 3.1, 3.18, CN5, D1.10, D3.2, P1, P4
**Human refs (from References field):** 3.18
**Jaccard:** 0.143 — AI adds ['3.1', 'CN5', 'D1.10', 'D3.2', 'P1', 'P4']

## Proposition 3.20
**Statement:** In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.

**Step 1.** Let ABDC be a circle with center E, and let angle BEC be an angle at the center and angle BAC an angle at the circumference, both standing on the same arc BC. We must show that angle BEC is double angle BAC.

**Step 2.** Join AE and produce it to a point F on the circumference [P1, P2]. We consider three cases according to the position of the center E relative to angle BAC.

**Step 3.** CASE 1: Suppose AE passes through the center so that the line AF is a diameter and one side of the inscribed angle lies along it. Consider triangle ABE. Since E is the center and A, B lie on the circle, EA = EB [D1.15]. Therefore triangle ABE is isosceles, and by Proposition 1.5, angle EAB = angle EBA.

**Step 4.** Now angle BEF is an exterior angle of triangle ABE. By Proposition 1.32, angle BEF equals the sum of the two remote interior angles, that is, angle BEF = angle EAB + angle EBA. Since angle EAB = angle EBA, we have angle BEF = 2 times angle EAB. But angle BEF is the angle at the center and angle EAB is the angle at the circumference, both standing on the same arc. Therefore the angle at the center is double the angle at the circumference.

**Step 5.** CASE 2: Suppose the center E falls within the angle BAC. Join AE and produce it to F on the circumference [P1, P2]. Consider triangle ABE. Since EA = EB [D1.15], by Proposition 1.5, angle EAB = angle EBA. The exterior angle BEF of triangle ABE equals angle EAB + angle EBA [1.32], so angle BEF = 2 times angle EAB.

**Step 6.** Similarly, consider triangle ACE. Since EA = EC [D1.15], by Proposition 1.5, angle EAC = angle ECA. The exterior angle CEF of triangle ACE equals angle EAC + angle ECA [1.32], so angle CEF = 2 times angle EAC.

**Step 7.** Adding angle BEF and angle CEF, we obtain angle BEC = angle BEF + angle CEF = 2 times angle EAB + 2 times angle EAC = 2 times (angle EAB + angle EAC) = 2 times angle BAC [CN2].

**Step 8.** CASE 3: Suppose the center E falls outside the angle BAC. Again join AE and produce it to F on the circumference [P1, P2]. Consider triangle ABE. Since EA = EB [D1.15], by Proposition 1.5, angle EAB = angle EBA. The exterior angle BEF of triangle ABE equals angle EAB + angle EBA [1.32], so angle BEF = 2 times angle EAB.

**Step 9.** Similarly, consider triangle ACE. Since EA = EC [D1.15], by Proposition 1.5, angle EAC = angle ECA. The exterior angle CEF of triangle ACE equals angle EAC + angle ECA [1.32], so angle CEF = 2 times angle EAC.

**Step 10.** Subtracting angle CEF from angle BEF, we obtain angle BEC = angle BEF - angle CEF = 2 times angle EAB - 2 times angle EAC = 2 times (angle EAB - angle EAC) = 2 times angle BAC [CN3].

**Step 11.** Therefore, in all cases, the angle at the center BEC is double the angle at the circumference BAC, when both stand on the same arc BC. Q.E.F.

**USED:** 1.32, 1.5, CN2, CN3, D1.15, P1, P2
**Human refs (from References field):** 1.32, 1.5
**Jaccard:** 0.286 — AI adds ['CN2', 'CN3', 'D1.15', 'P1', 'P2']

## Proposition 3.21
**Statement:** In a circle the angles in the same segment are equal to one another.

**Step 1.** Let ABCD be a circle, and let angles BAC and BDC be angles in the same segment BADC, that is, both angles stand on the same arc BKC (the arc on the opposite side of chord BC from the segment containing points A and D). We must show that angle BAC equals angle BDC.

**Step 2.** Find the centre E of circle ABCD [3.1]. Join BE and CE [P1].

**Step 3.** Consider the central angle BEC. The angle BEC is the angle at the centre E standing on arc BKC. The inscribed angle BAC is an angle at the circumference standing on the same arc BKC. By Proposition 3.20, the angle BEC at the centre is double the angle BAC at the circumference, since both stand on the same arc BKC. That is, angle BEC = 2 * angle BAC.

**Step 4.** Similarly, the inscribed angle BDC is also an angle at the circumference standing on the same arc BKC. By Proposition 3.20 again, the angle BEC at the centre is double the angle BDC at the circumference. That is, angle BEC = 2 * angle BDC.

**Step 5.** From Steps 3 and 4, we have angle BEC = 2 * angle BAC and angle BEC = 2 * angle BDC. Since both 2 * angle BAC and 2 * angle BDC are equal to the same thing (namely angle BEC), by Common Notion 1, 2 * angle BAC = 2 * angle BDC. Therefore angle BAC = angle BDC.

**Step 6.** Therefore, in a circle, the angles in the same segment are equal to one another. Q.E.F.

**USED:** 3.1, 3.20, CN1, P1
**Human refs (from References field):** 3.20
**Jaccard:** 0.250 — AI adds ['3.1', 'CN1', 'P1']

## Proposition 3.22
**Statement:** The opposite angles of quadrilaterals in circles are equal to two right angles.

**Step 1.** Let ABCD be a quadrilateral inscribed in a circle, with vertices A, B, C, D lying consecutively on the circumference. We wish to show that the opposite angles are together equal to two right angles; that is, angle DAB + angle BCD = two right angles, and angle ABC + angle ADC = two right angles.

**Step 2.** Join the diagonals AC and BD. [P1]

**Step 3.** Consider triangle ABD. By 1.32, the three angles of this triangle sum to two right angles: angle DAB + angle ABD + angle ADB = two right angles.

**Step 4.** Now consider chord AB. The points C and D both lie on the same arc of the circle (the arc from B to A passing through C and D, since the vertices are consecutive). Therefore angles ACB and ADB are angles in the same segment, and by 3.21, angle ADB = angle ACB.

**Step 5.** Next consider chord AD. The points B and C both lie on the same arc (the arc from A to D passing through B and C). Therefore angles ABD and ACD are angles in the same segment, and by 3.21, angle ABD = angle ACD.

**Step 6.** Substituting the results of Steps 4 and 5 into the equation from Step 3: angle DAB + angle ACD + angle ACB = two right angles. [CN1]

**Step 7.** Since the ray CA lies between rays CB and CD at vertex C, we have angle ACD + angle ACB = angle BCD. [CN2]

**Step 8.** Therefore angle DAB + angle BCD = two right angles. This establishes the first pair of opposite angles.

**Step 9.** Now consider triangle ABC. By 1.32, angle BAC + angle ABC + angle BCA = two right angles.

**Step 10.** Consider chord BC. The points A and D both lie on the same arc (the arc from C to B passing through D and A). Therefore angles BAC and BDC are angles in the same segment, and by 3.21, angle BAC = angle BDC.

**Step 11.** Consider chord AB again. As in Step 4, angles BCA and BDA are angles in the same segment, and by 3.21, angle BCA = angle BDA.

**Step 12.** Substituting the results of Steps 10 and 11 into the equation from Step 9: angle BDC + angle ABC + angle BDA = two right angles. [CN1]

**Step 13.** Since the ray DB lies between rays DC and DA at vertex D, we have angle BDC + angle BDA = angle ADC. [CN2]

**Step 14.** Therefore angle ABC + angle ADC = two right angles. This establishes the second pair of opposite angles.

**Step 15.** Therefore the opposite angles of quadrilaterals in circles are together equal to two right angles. Q.E.D.

**USED:** 1.32, 3.21, CN1, CN2, P1
**Human refs (from References field):** 1.32, 3.21
**Jaccard:** 0.400 — AI adds ['CN1', 'CN2', 'P1']

## Proposition 3.23
**Statement:** On the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.

**Step 1.** Let AB be a given straight line, and suppose, for the sake of contradiction, that two similar and unequal segments of circles AEB and ADB are constructed on AB on the same side. Since the segments are unequal but share the same base AB and lie on the same side, one must contain the other. Let ADB be the outer (larger) segment and AEB the inner (smaller) segment. [D3.6, D3.11]

**Step 2.** Since the segments are similar, by the definition of similar segments (D3.11), the angles in segment AEB and the angles in segment ADB are equal to one another.

**Step 3.** Take a point D on the arc of the outer segment ADB. Join DA and DB. [P1] Then angle ADB is an angle in segment ADB. [D3.8]

**Step 4.** Since D lies on the outer arc and outside the inner circle, and B lies on the inner circle, the straight line DB must intersect the arc of the inner segment AEB at some point E. [3.2, since two points taken on a circumference have the line between them falling within the circle, D which is outside the inner circle connected to B which is on it must cross the inner arc]

**Step 5.** Join AE. [P1] Then angle AEB is an angle in segment AEB. [D3.8]

**Step 6.** Now consider triangle ADE. Since E lies between D and B on the line DB, the angle AEB is an exterior angle of triangle ADE at vertex E. By Proposition 1.16, an exterior angle of a triangle is greater than either of the non-adjacent interior angles. Therefore angle AEB is greater than angle ADE, that is, angle AEB is greater than angle ADB. [1.16]

**Step 7.** But from Step 2, because the segments are similar, angle AEB equals angle ADB. [D3.11] This contradicts the conclusion of Step 6 that angle AEB is greater than angle ADB.

**Step 8.** Therefore the assumption is false, and on the same straight line there cannot be constructed two similar and unequal segments of circles on the same side. Q.E.D.

**USED:** 1.16, 3.2, D3.11, D3.6, D3.8, P1
**Human refs (from References field):** 1.16, D3.11
**Jaccard:** 0.333 — AI adds ['3.2', 'D3.6', 'D3.8', 'P1']

## Proposition 3.24
**Statement:** Similar segments of circles on equal straight lines are equal to one another.

**Step 1.** Let AEB and CFD be similar segments of circles on equal straight lines AB and CD respectively. We must prove that segment AEB is equal to segment CFD.

**Step 2.** Since AB equals CD [given], if segment AEB is applied to segment CFD so that point A is placed on point C and the straight line AB is placed along CD, then point B will coincide with point D, because AB equals CD [CN4, D1.4].

**Step 3.** With AB coinciding with CD, the segment AEB must either coincide with segment CFD, or it must fail to coincide, in which case it falls either inside CFD, outside CFD, or intersects CFD, as in the configuration where one arc does not match the other.

**Step 4.** Suppose segment AEB does not coincide with segment CFD when so applied. Then on the same straight line CD, on the same side, there exist two segments of circles AEB (now repositioned onto CD) and CFD that are similar but unequal.

**Step 5.** But this is impossible, for by Proposition 3.23, on the same straight line there cannot be constructed two similar and unequal segments of circles on the same side [3.23].

**Step 6.** Therefore segment AEB, when applied to segment CFD, coincides with it entirely. Since they coincide, they are equal to one another [CN4].

**Step 7.** Therefore similar segments of circles on equal straight lines are equal to one another, which was to be proved.

**USED:** 3.23, CN4, D3.11, D3.6
**Human refs (from References field):** 3.10
**Jaccard:** 0.000 — AI adds ['3.23', 'CN4', 'D3.11', 'D3.6']; Human adds ['3.10']

## Proposition 3.25
**Statement:** Given a segment of a circle, to describe the complete circle of which it is a segment.

**Step 1.** Let ABC be the given segment of a circle, with AC as its base (chord) and B a point on the arc. Bisect AC at D [1.10].

**Step 2.** From D, draw a straight line at right angles to AC [1.11]. Let this perpendicular meet the arc of the segment at B. Join AB [P1].

**Step 3.** Bisect AB at E [1.10].

**Step 4.** From E, draw EG at right angles to AB [1.11], and produce it if necessary [P2]. We claim that line EG meets line DB (or DB produced). To see this, suppose for contradiction that EG is parallel to DB. Since DB is at right angles to AC, and AB is a transversal cutting the parallel lines EG and DB, the alternate interior angles are equal [1.29], so angle ABD equals angle AEG. But angle AEG is a right angle by construction. So angle ABD would be a right angle. However, in triangle ABD, angle ADB is also a right angle (since DB is perpendicular to AC). By 1.32, the three angles of triangle ABD sum to two right angles. If both angle ADB and angle ABD are right angles, their sum already equals two right angles, forcing angle DAB to be zero, which is impossible since A, B, D are distinct non-collinear points. This contradiction shows EG is not parallel to DB. Therefore EG meets line BD (or BD produced) at some point F [P2].

**Step 5.** Since E is the midpoint of AB, we have AE = EB [Step 3]. The angles AEF and BEF are both right angles [Step 4, since EG is at right angles to AB]. And EF is common to triangles AEF and BEF. Therefore, by 1.4 (Side-Angle-Side), triangle AEF is congruent to triangle BEF, and so FA = FB.

**Step 6.** Since F lies on line BD, and BD is perpendicular to AC at D, the angle FDC and angle FDA are both right angles [since BD is at right angles to AC at D; if F is on the same side as B, then angle FDA = angle BDA = right angle and angle FDC = angle BDC = right angle; if F is on the opposite side, then by 1.13, since angle BDA and angle FDA are supplementary and angle BDA is a right angle, angle FDA is also a right angle, and similarly angle FDC is a right angle].

**Step 7.** Since D is the midpoint of AC, we have AD = DC [Step 1]. The angles FDA and FDC are both right angles [Step 6]. And FD is common to triangles FDA and FDC. Therefore, by 1.4 (Side-Angle-Side), triangle FDA is congruent to triangle FDC, and so FA = FC.

**Step 8.** From Steps 5 and 7, FA = FB and FA = FC, hence FA = FB = FC [CN1].

**Step 9.** Describe the circle with center F and radius FA [P3]. Since FA = FB = FC, all three points A, B, and C lie on this circle [D1.15, since all straight lines from F to points on the circle equal FA].

**Step 10.** The chord AC and the arc through B form the given segment. Since A, B, and C all lie on the described circle, and the segment ABC is part of this circle, the described circle is the complete circle of which ABC is a segment. This completes the construction.

**USED:** 1.10, 1.11, 1.13, 1.29, 1.32, 1.4, CN1, D1.15, P1, P2, P3
**Human refs (from References field):** 1.6, 3.9
**Jaccard:** 0.000 — AI adds ['1.10', '1.11', '1.13', '1.29', '1.32', '1.4', 'CN1', 'D1.15', 'P1', 'P2', 'P3']; Human adds ['1.6', '3.9']

## Proposition 3.26
**Statement:** In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

**Step 1.** Let ABC and DEF be equal circles with centres G and H respectively. First, suppose the equal angles are at the centres: let angle BGC equal angle EHF. We are to prove that the arc BKC on which angle BGC stands equals the arc ELF on which angle EHF stands.

**Step 2.** Since the circles are equal, their radii are equal (D3.1). Thus BG = EH and GC = HF.

**Step 3.** In triangles BGC and EHF, we have BG = EH, GC = HF, and angle BGC = angle EHF. Therefore by the side-angle-side congruence theorem (1.4), triangle BGC is congruent to triangle EHF, and in particular the base BC equals the base EF.

**Step 4.** Since the angle BGC is a central angle of circle ABC standing on arc BKC, by 3.20 the angle BGC is double any angle inscribed in the major segment on the opposite side of chord BC. Similarly, the angle EHF is double any angle inscribed in the major segment on the opposite side of chord EF in circle DEF.

**Step 5.** Since angle BGC equals angle EHF, their halves are equal; that is, the angle in the segment of circle ABC on one side of BC equals the angle in the corresponding segment of circle DEF on one side of EF. By the definition of similar segments (D3.11), the segments of circle ABC cut off by BC and the corresponding segments of circle DEF cut off by EF are similar.

**Step 6.** Since BC = EF (Step 3), and the segments on BC and EF are similar (Step 5), by 3.24 these similar segments on equal straight lines are equal to one another. Thus the minor segment on BC in circle ABC equals the minor segment on EF in circle DEF.

**Step 7.** Since the circles ABC and DEF are equal, and the minor segments cut off by BC and EF are equal, the remainders are equal (CN3). That is, the major segments are also equal.

**Step 8.** Since the minor segments are equal, the arcs bounding them are equal: arc BKC (the minor arc from B to C) equals arc ELF (the minor arc from E to F). For equal segments on equal bases must have equal arcs, since a segment is the figure contained by the straight line and the circumference (D3.6), and the bases being equal, the circumferences bounding the segments must be equal for the figures to coincide.

**Step 9.** Now suppose the equal angles stand at the circumferences: let angle BAC equal angle EDF, where A is on the circumference of circle ABC and D is on the circumference of circle DEF.

**Step 10.** By 3.20, the central angle BGC is double the inscribed angle BAC, and the central angle EHF is double the inscribed angle EDF, since each pair of angles stands on the same arc.

**Step 11.** Since angle BAC equals angle EDF, their doubles are equal: angle BGC equals angle EHF (CN2, adding equals to equals, or equivalently since doubles of equals are equal).

**Step 12.** By the case already proved (Steps 1 through 8), since the central angles BGC and EHF are equal in the equal circles, the arcs on which they stand are equal: arc BC equals arc EF.

**Step 13.** Therefore, in equal circles, equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences. Q.E.D.

**USED:** 1.4, 3.20, 3.24, CN2, CN3, D3.1, D3.11, D3.6
**Human refs (from References field):** 1.4, 3.24, D3.11
**Jaccard:** 0.375 — AI adds ['3.20', 'CN2', 'CN3', 'D3.1', 'D3.6']

## Proposition 3.27
**Statement:** In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.

**Step 1.** Let ABC and DEF be equal circles with centres G and H respectively. Let angle BGC at centre G stand on circumference BC, and let angle EHF at centre H stand on circumference EF. Let circumference BC equal circumference EF. We are to show that angle BGC equals angle EHF.

**Step 2.** Suppose angle BGC is not equal to angle EHF. Then one of them is greater. Let angle BGC be greater than angle EHF.

**Step 3.** On the straight line BG and at the point G on it, construct angle BGK equal to angle EHF, where K falls on circumference BC [1.23].

**Step 4.** Since the equal circles ABC and DEF have equal angles at their centres, namely angle BGK equals angle EHF, the circumferences on which they stand are equal [3.26]. Therefore circumference BK equals circumference EF.

**Step 5.** But circumference BC also equals circumference EF by hypothesis. Therefore circumference BK equals circumference BC [CN1].

**Step 6.** But circumference BK is a part of circumference BC, so the part equals the whole, which is impossible [CN5].

**Step 7.** Therefore angle BGC is not greater than angle EHF. By the same argument, with the roles interchanged, angle EHF is not greater than angle BGC.

**Step 8.** Since neither is greater than the other, angle BGC equals angle EHF. This completes the case of angles at the centres.

**Step 9.** Now let angle BAC be an angle at the circumference of circle ABC standing on circumference BC, and let angle EDF be an angle at the circumference of circle DEF standing on circumference EF, where circumference BC equals circumference EF. We are to show that angle BAC equals angle EDF.

**Step 10.** Since angle BGC is the angle at centre G standing on circumference BC, and angle BAC is the angle at the circumference standing on the same circumference, angle BGC is double angle BAC [3.20].

**Step 11.** Similarly, angle EHF at centre H is double angle EDF at the circumference [3.20].

**Step 12.** From Step 8, angle BGC equals angle EHF. Since angle BGC equals twice angle BAC, and angle EHF equals twice angle EDF, twice angle BAC equals twice angle EDF [CN1].

**Step 13.** Subtracting angle BAC from twice angle BAC leaves angle BAC, and subtracting angle EDF from twice angle EDF leaves angle EDF. Since the doubles are equal, the halves are equal, and therefore angle BAC equals angle EDF [CN3].

**Step 14.** Therefore in equal circles, angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences. Q.E.F.

**USED:** 1.23, 3.20, 3.26, CN1, CN3, CN5
**Human refs (from References field):** 1.23, 3.20, 3.26
**Jaccard:** 0.500 — AI adds ['CN1', 'CN3', 'CN5']

## Proposition 3.28
**Statement:** In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

**Step 1.** Let ABC and DEF be equal circles, and let BG and EH be equal straight lines in them respectively, where BG is a chord of circle ABC and EH is a chord of circle DEF. We must show that the arcs cut off are equal: the major arc equal to the major and the minor arc equal to the minor.

**Step 2.** Find the centre K of circle ABC and the centre L of circle DEF. [3.1]

**Step 3.** Join KB, KG, LE, and LH. [P1]

**Step 4.** Since the circles ABC and DEF are equal, their radii are equal. [D3.1] Therefore KB equals LE, and KG equals LH.

**Step 5.** The two sides BK, KG of triangle BKG are equal to the two sides EL, LH of triangle ELH respectively (Step 4), and the base BG equals the base EH (given). Therefore triangle BKG is congruent to triangle ELH, and the angle BKG equals the angle ELH. [1.8]

**Step 6.** In equal circles, equal angles at the centres stand on equal circumferences. [3.26] Since angle BKG equals angle ELH (Step 5), the circumference BG on which angle BKG stands equals the circumference EH on which angle ELH stands. That is, the minor arc BG equals the minor arc EH.

**Step 7.** The whole circumference of circle ABC equals the whole circumference of circle DEF, since the circles are equal. [D3.1]

**Step 8.** Since the whole circumferences are equal (Step 7) and the minor arcs BG and EH are equal (Step 6), by subtracting equals from equals, the remaining major arc BG equals the remaining major arc EH. [CN3]

**Step 9.** Therefore in equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less. Q.E.F.

**USED:** 1.8, 3.1, 3.26, CN3, D3.1, P1
**Human refs (from References field):** 1.8, 3.26
**Jaccard:** 0.333 — AI adds ['3.1', 'CN3', 'D3.1', 'P1']

## Proposition 3.29
**Statement:** In equal circles equal circumferences are subtended by equal straight lines.

**Step 1.** Let ABC and DEF be equal circles, and let the circumference BGC in circle ABC be equal to the circumference EHF in circle DEF. Let BC be the straight line subtending circumference BGC and let EF be the straight line subtending circumference EHF. I say that BC equals EF.

**Step 2.** Find the centre K of circle ABC and the centre L of circle DEF [3.1].

**Step 3.** Join KB, KC, LE, and LF [P1].

**Step 4.** Since the circumference BGC equals the circumference EHF, and these are circumferences in equal circles ABC and DEF, the angle BKC at the centre K equals the angle ELF at the centre L [3.27].

**Step 5.** Since circles ABC and DEF are equal, their radii are equal [D3.1]. Therefore KB equals LE, and KC equals LF.

**Step 6.** In triangles BKC and ELF, KB equals LE, KC equals LF, and the angle BKC equals the angle ELF. Therefore, by the side-angle-side criterion, triangle BKC is congruent to triangle ELF, and so the base BC equals the base EF [1.4].

**Step 7.** Therefore in equal circles equal circumferences are subtended by equal straight lines. Q.E.D.

**USED:** 1.4, 3.1, 3.27, D3.1, P1
**Human refs (from References field):** 1.4, 3.27
**Jaccard:** 0.400 — AI adds ['3.1', 'D3.1', 'P1']

## Proposition 3.30
**Statement:** To bisect a given circumference.

**Step 1.** Let ADB be the given circumference (arc) which it is required to bisect, where A and B are the endpoints of the arc and D is a point on the arc between them.

**Step 2.** Join A to B by a straight line [P1].

**Step 3.** Bisect AB at the point C, so that AC equals CB [1.10].

**Step 4.** From the point C, draw the straight line CD at right angles to AB, meeting the circumference ADB at the point D [1.11].

**Step 5.** Consider the triangles ACD and BCD. We have AC equal to CB (Step 3), the side CD is common to both triangles, and the angle ACD is equal to the angle BCD, since each is a right angle (Step 4). Therefore, by the side-angle-side criterion, triangle ACD is congruent to triangle BCD, and hence the straight line AD is equal to the straight line DB [1.4].

**Step 6.** Now AD and DB are straight lines in the same circle. Since the same circle is equal to itself [D3.1], and the straight line AD is equal to the straight line DB (Step 5), the circumference cut off by AD equals the circumference cut off by DB, with the greater arc equal to the greater and the lesser equal to the lesser [3.28].

**Step 7.** Since D lies on the arc ADB between A and B, the arc AD and the arc DB are the parts into which D divides the circumference ADB. Since these arcs are equal (Step 6), the given circumference ADB has been bisected at the point D. Q.E.F.

**USED:** 1.10, 1.11, 1.4, 3.28, D3.1, P1
**Human refs (from References field):** 1.4, 3.28
**Jaccard:** 0.333 — AI adds ['1.10', '1.11', 'D3.1', 'P1']

## Proposition 3.31
**Statement:** In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

**Step 1.** Let ABCD be a circle with diameter BC and centre E. Let A be a point on the circumference of the semicircle on one side of BC, and let BA and AC be joined [P1]. We must show that angle BAC is a right angle.

**Step 2.** Join EA [P1]. Since EB equals EA (both are radii of the circle) [D1.15], triangle ABE is isosceles, and therefore angle ABE equals angle BAE [1.5]. Similarly, since EC equals EA (both are radii), triangle AEC is isosceles, and angle ACE equals angle CAE [1.5].

**Step 3.** Therefore angle BAC equals the sum of angles ABE and ACE, since angle BAC equals angle BAE plus angle CAE, and angle BAE equals angle ABE and angle CAE equals angle ACE.

**Step 4.** Now the three angles of triangle ABC sum to two right angles [1.32]. That is, angle BAC plus angle ABC plus angle ACB equals two right angles. But angle ABC is the same as angle ABE, and angle ACB is the same as angle ACE. So angle BAC plus angle ABE plus angle ACE equals two right angles.

**Step 5.** By Step 3, angle ABE plus angle ACE equals angle BAC. Substituting into Step 4: angle BAC plus angle BAC equals two right angles, that is, twice angle BAC equals two right angles. Therefore angle BAC equals one right angle [D1.10]. This proves the angle in a semicircle is right.

**Step 6.** Now for the angle in a greater segment. Let the straight line AC be drawn within the circle, cutting off the greater segment ABC (containing the centre) and the lesser segment ADC (not containing the centre). Take any point D on arc ADC and join AD, DC [P1]. We must show that the angle in the greater segment ABC (i.e., angle BAC as constructed above, or more generally any angle in the segment) is less than a right angle, and the angle in the lesser segment ADC (i.e., angle ADC) is greater than a right angle.

**Step 7.** Consider the quadrilateral ABCD inscribed in the circle. By Proposition 3.22, the opposite angles of a quadrilateral inscribed in a circle sum to two right angles. Therefore angle ABC plus angle ADC equals two right angles [3.22].

**Step 8.** Since the angle BAC in the semicircle on diameter BC was shown to be a right angle (Step 5), and segment ABC is greater than a semicircle (it contains the centre), the angle ABC in this greater segment is an angle in a segment greater than a semicircle. In triangle ABC with the diameter BC, angle BAC is right, so angle ABC plus angle ACB equals one right angle [1.32], meaning angle ABC is less than a right angle [CN5, D1.12].

**Step 9.** More precisely: let AC be any chord that does not pass through the centre, dividing the circle into two segments. Let F be a point on the arc of the greater segment (the one containing the centre) and join AF, FC [P1]. Consider the diameter through A; let it be AB' where B' is the diametrically opposite point. Then angle AFB' is an angle in a semicircle, which is right by Step 5. Since F lies on the greater arc cut off by AC, and B' lies on the same side as the greater segment, point C lies between B' and the other endpoint along the arc from F's perspective, meaning angle AFC is a part of angle AFB'. Therefore angle AFC is less than a right angle [CN5, D1.12].

**Step 10.** Let us give a cleaner argument for parts 2 and 3. Let AC be a chord of circle ABCD not passing through centre E. Let the greater segment be the one containing the centre, and the lesser segment be the one not containing the centre. Draw diameter AB through A [P1, P2]. Since AC is not a diameter, B and C are distinct points on the circumference.

**Step 11.** Let F be any point on the arc of the greater segment (the arc on the same side as the centre). Join AF, FC [P1]. Since AB is a diameter, angle AFB is a right angle (by Step 5, the angle in a semicircle is right).

**Step 12.** Since the greater segment with respect to chord AC contains the centre, and AB is a diameter, point C is on the arc of the semicircle on the same side as F (both on the greater-segment side). B is the endpoint of the diameter. The arc from A to B on the side of F, and the arc from A to C on the side of F: since the greater segment for AC contains the centre, and the semicircle for AB also contains the centre, point C lies on the arc AFB. Therefore FC lies within angle AFB, meaning angle AFC is less than angle AFB [CN5].

**Step 13.** Since angle AFB is a right angle and angle AFC is less than angle AFB, angle AFC is less than a right angle, i.e., it is acute [D1.12]. This proves the angle in a greater segment is less than a right angle.

**Step 14.** Now let D be any point on the arc of the lesser segment (the arc not containing the centre). Join AD, DC [P1]. Consider the cyclic quadrilateral AFDC inscribed in the circle (with F on the greater arc and D on the lesser arc relative to chord AC). By 3.22, opposite angles sum to two right angles: angle AFC plus angle ADC equals two right angles [3.22].

**Step 15.** Since angle AFC is less than a right angle (Step 13), angle ADC must be greater than a right angle, since angle AFC plus angle ADC equals two right angles [CN5]. That is, angle ADC is obtuse [D1.11]. This proves the angle in a less segment is greater than a right angle.

**Step 16.** For the fourth part: we must show that the angle of the greater segment (the mixed angle between chord AC and the arc of the greater segment) is greater than a right angle. By 3.16, the angle of a semicircle (between the diameter and the circumference) is greater than any acute rectilineal angle. The angle of the greater segment is the angle between chord AC and the circumference of the greater arc. Since the greater segment contains the centre, and the angle in the greater segment (a rectilineal angle) is acute (Step 13), the angle of the segment (the mixed angle between the chord and the arc) is greater than that rectilineal angle. Specifically: the angle of the greater segment, being the mixed angle contained by the straight line AC and the circumference of the greater arc, is greater than the right angle formed in the semicircle's construction. By 3.16, the angle of a semicircle is greater than any acute rectilineal angle; analogously, the angle of a segment greater than a semicircle is greater than a right angle [3.16, D3.7].

**Step 17.** For the fifth part: the angle of the less segment is the mixed angle between chord AC and the arc of the lesser segment. Since the angle in the lesser segment is obtuse (Step 15), and the angle of the lesser segment is the remaining mixed angle at the chord, and by 3.16 the mixed angle between a straight line and circumference on the side away from the centre is less than any acute rectilineal angle, the angle of the less segment is less than a right angle [3.16, D3.7].

**Step 18.** Therefore: in a circle, the angle in the semicircle is right; the angle in a greater segment is less than a right angle; the angle in a less segment is greater than a right angle; the angle of the greater segment is greater than a right angle; and the angle of the less segment is less than a right angle. Q.E.F.

**USED:** 1.32, 1.5, 3.16, 3.22, CN5, D1.10, D1.11, D1.12, D1.15, D3.7, P1, P2
**Human refs (from References field):** 1.17, 1.32, 1.5, 3.22, D1.10
**Jaccard:** 0.308 — AI adds ['3.16', 'CN5', 'D1.11', 'D1.12', 'D1.15', 'D3.7', 'P1', 'P2']; Human adds ['1.17']

## Proposition 3.32
**Statement:** If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

**Step 1.** Let EF be a straight line tangent to circle ABCD at point B, and let BD be a straight line drawn from B across the circle, cutting it and creating two segments. We must show that angle DBF equals the angle in the alternate segment BAD, and angle DBE equals the angle in the alternate segment BCD.

**Step 2.** Draw the diameter BA from B through the centre of the circle to the point A on the circumference [P1, P2, D1.15, D1.17]. Since EF is tangent to the circle at B [D3.2], and BA is a diameter passing through the centre, by 3.18 the diameter BA is perpendicular to the tangent EF. Therefore angle ABF is a right angle.

**Step 3.** Since BA is a diameter, the angle ADB, being an angle in the semicircle, is a right angle [3.31].

**Step 4.** In triangle ABD, the three interior angles sum to two right angles [1.32]. Since angle ADB is a right angle (Step 3), the remaining angles satisfy: angle ABD + angle BAD = one right angle.

**Step 5.** Now angle ABF is a right angle (Step 2), and angle ABF is composed of angle ABD and angle DBF. Therefore angle DBF = angle ABF minus angle ABD = one right angle minus angle ABD.

**Step 6.** From Step 4, angle BAD = one right angle minus angle ABD. Therefore angle DBF = angle BAD.

**Step 7.** The point A lies on the circumference of segment BAD, and angle BAD is formed by joining A to the endpoints B and D of the chord BD. Therefore angle BAD is an angle in segment BAD [D3.8]. Since angle DBF = angle BAD, the angle between the tangent BF and the chord BD equals the angle in the alternate segment BAD.

**Step 8.** Since EBF is a straight line, angle DBE + angle DBF = two right angles [1.13].

**Step 9.** Let C be any point on the arc BCD. Consider the quadrilateral BADC inscribed in the circle with vertices B, A, D, C on the circumference. By 3.22, the opposite angles of this inscribed quadrilateral sum to two right angles. In particular, angle BAD + angle BCD = two right angles.

**Step 10.** From Step 8, angle DBE = two right angles minus angle DBF. From Step 6, angle DBF = angle BAD. Therefore angle DBE = two right angles minus angle BAD.

**Step 11.** From Step 9, angle BCD = two right angles minus angle BAD. Therefore angle DBE = angle BCD.

**Step 12.** The point C lies on the circumference of segment BCD, and angle BCD is formed by joining C to the endpoints B and D of the chord BD. Therefore angle BCD is an angle in segment BCD [D3.8]. Since angle DBE = angle BCD, the angle between the tangent BE and the chord BD equals the angle in the alternate segment BCD.

**Step 13.** Therefore, if a straight line touches a circle, and from the point of contact a straight line is drawn across the circle cutting it, the angles which it makes with the tangent are equal to the angles in the alternate segments of the circle. Q.E.F.

**USED:** 1.13, 1.32, 3.18, 3.22, 3.31, D1.15, D1.17, D3.2, D3.8, P1, P2
**Human refs (from References field):** 1.32, 3.19, 3.22, 3.31
**Jaccard:** 0.250 — AI adds ['1.13', '3.18', 'D1.15', 'D1.17', 'D3.2', 'D3.8', 'P1', 'P2']; Human adds ['3.19']

## Proposition 3.33
**Statement:** On a given straight line to describe a segment of a circle admitting an angle equal to a given rectilineal angle.

**Step 1.** Let AB be the given straight line and C the given rectilineal angle. We consider three cases according to whether angle C is right, acute, or obtuse.

**Step 2.** (Case 1: angle C is a right angle.) Find the midpoint F of AB [1.10]. With center F and radius FA, describe the semicircle AHB [P3]. Since AHB is a semicircle, the angle in the semicircle is right [3.31]. Therefore the semicircle AHB is a segment admitting an angle equal to the right angle C.

**Step 3.** (Case 2: angle C is acute.) At the point A on line AB, construct the angle BAD equal to angle C [1.23]. Draw AE perpendicular to DA at A [1.11]. Bisect AB at F [1.10]. Draw FG from F perpendicular to AB [1.11], and let G be the point where FG meets AE [P1]. Join GB [P1].

**Step 4.** Since AF equals FB (F is the midpoint of AB) and FG is common, and angle AFG equals angle BFG (both being right angles) [P4], triangle AFG is congruent to triangle BFG [1.4]. Therefore GA equals GB.

**Step 5.** With center G and radius GA, describe a circle passing through A [P3]. Since GA equals GB [Step 4], this circle also passes through B [D1.15].

**Step 6.** Since DA is perpendicular to the radius GA at the point A on the circle (for angle DAG is right, since AE was drawn perpendicular to DA and G lies on AE), and the straight line drawn at right angles to a diameter of a circle from its extremity touches the circle [3.16], the line DA touches circle AHB at A.

**Step 7.** Since DA touches the circle at A, and AB is a straight line drawn from the point of contact A cutting the circle, by 3.32 the angle DAB equals the angle in the alternate segment AHB [3.32]. But angle DAB equals angle C [Step 3, by construction]. Therefore the angle in segment AHB equals angle C [CN1]. Thus the segment AHB on AB admits an angle equal to the given acute angle C.

**Step 8.** (Case 3: angle C is obtuse.) At the point A on line AB, construct the angle BAD equal to angle C [1.23]. Draw AE perpendicular to DA at A [1.11]. Bisect AB at F [1.10]. Draw FG from F perpendicular to AB [1.11], and let G be the point where FG meets AE (on the opposite side of AB from the previous case) [P1]. Join GB [P1].

**Step 9.** By the same reasoning as in Steps 4 and 5, GA equals GB [1.4], and the circle with center G and radius GA passes through both A and B [P3, D1.15].

**Step 10.** Since angle DAG is right (AE being perpendicular to DA, and G lying on AE), DA is perpendicular to the radius GA at the point A on the circle. Therefore DA touches the circle at A [3.16].

**Step 11.** Since DA touches the circle at A and AB cuts the circle, angle DAB equals the angle in the alternate segment AHB [3.32]. But angle DAB equals angle C [Step 8, by construction]. Therefore the angle in segment AHB equals angle C [CN1]. Thus the segment AHB on AB admits an angle equal to the given obtuse angle C.

**Step 12.** Therefore in all three cases, on the given straight line AB a segment of a circle AHB has been described admitting an angle equal to the given rectilineal angle C. Q.E.F.

**USED:** 1.10, 1.11, 1.23, 1.4, 3.16, 3.31, 3.32, CN1, D1.15, P1, P3, P4
**Human refs (from References field):** 1.4, 3.16, 3.31, 3.32
**Jaccard:** 0.333 — AI adds ['1.10', '1.11', '1.23', 'CN1', 'D1.15', 'P1', 'P3', 'P4']

## Proposition 3.34
**Statement:** From a given circle to cut off a segment admitting an angle equal to a given rectilineal angle.

**Step 1.** Let ABC be the given circle and D the given rectilineal angle. It is required to cut off from circle ABC a segment admitting an angle equal to angle D.

**Step 2.** Let B be any point on the circumference of circle ABC. Draw the straight line EBF tangent to circle ABC at the point B [3.17].

**Step 3.** At the point B on the straight line EBF, construct the angle FBC equal to the angle D, where BC is drawn from B across the circle so that it meets the circumference again at C [1.23].

**Step 4.** Since the straight line EBF touches the circle ABC at B, and from the point of contact B the straight line BC has been drawn across the circle cutting it, the angle FBC is equal to the angle in the alternate segment BAC of the circle [3.32].

**Step 5.** But the angle FBC is equal to the angle D [by construction, Step 3].

**Step 6.** Therefore the angle in the segment BAC is equal to the angle D [CN1].

**Step 7.** Therefore from the given circle ABC the segment BAC has been cut off admitting an angle equal to the given rectilineal angle D. This is what was required to do.

**USED:** 1.23, 3.17, 3.32, CN1, D3.6, D3.8
**Human refs (from References field):** 1.23, 3.32
**Jaccard:** 0.333 — AI adds ['3.17', 'CN1', 'D3.6', 'D3.8']

## Proposition 3.35
**Statement:** If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.

**Step 1.** Let ABCD be a circle, and let AC and BD be two straight lines cutting one another at the point E within the circle. We must show that the rectangle AE by EC equals the rectangle BE by ED.

**Step 2.** Case 1: Suppose both AC and BD pass through the centre F of the circle. Then E coincides with F, and AE, EC, BE, ED are all radii of the circle. Since AE = EC and BE = ED, and all four are equal to the radius, the rectangle AE by EC equals the rectangle BE by ED. [D1.15, D1.17]

**Step 3.** Case 2: Suppose AC passes through the centre F, but BD does not pass through the centre. Drop a perpendicular FG from F to BD. By 3.3, FG bisects BD, so BG = GD. [3.3, 1.12]

**Step 4.** Since the straight line AC is bisected at F and cut unequally at E, by 2.5 the rectangle AE by EC together with the square on FE equals the square on FC. [2.5]

**Step 5.** But FC is a radius of the circle, and since B is on the circle, FB is also a radius, so FC = FB. Therefore the square on FE plus the rectangle AE by EC equals the square on FB. [D1.15]

**Step 6.** Now in the right triangle FGE (with the right angle at G), by 1.47 the square on FE equals the square on FG plus the square on GE. [1.47]

**Step 7.** Also in right triangle FGB, by 1.47 the square on FB equals the square on FG plus the square on GB. [1.47]

**Step 8.** Substituting into the equation from Step 4: the rectangle AE by EC plus the square on FG plus the square on GE equals the square on FG plus the square on GB. [CN2]

**Step 9.** Subtracting the square on FG from both sides, the rectangle AE by EC plus the square on GE equals the square on GB. [CN3]

**Step 10.** Since BD is bisected at G and cut unequally at E, by 2.5 the rectangle BE by ED plus the square on GE equals the square on GB. [2.5]

**Step 11.** Therefore the rectangle AE by EC plus the square on GE equals the rectangle BE by ED plus the square on GE. [CN1]

**Step 12.** Subtracting the square on GE from both sides, the rectangle AE by EC equals the rectangle BE by ED. [CN3]

**Step 13.** Case 3: Suppose neither AC nor BD passes through the centre F. Draw the diameter FKEF' through E and the centre F (that is, the straight line through F and E, meeting the circle at K and K'). [P1, 3.1]

**Step 14.** Since KK' is a diameter passing through the centre and BD does not pass through the centre, and they intersect at E, by Case 2 the rectangle KE by EK' equals the rectangle BE by ED.

**Step 15.** Similarly, since KK' passes through the centre and AC does not, by Case 2 the rectangle KE by EK' equals the rectangle AE by EC.

**Step 16.** Therefore the rectangle AE by EC equals the rectangle BE by ED. [CN1]

**Step 17.** In all cases, if in a circle two straight lines cut one another, the rectangle contained by the segments of the one equals the rectangle contained by the segments of the other. Q.E.D.

**USED:** 1.12, 1.47, 2.5, 3.1, 3.3, CN1, CN2, CN3, D1.15, D1.17, P1
**Human refs (from References field):** 1.47, 2.5, 3.3
**Jaccard:** 0.273 — AI adds ['1.12', '3.1', 'CN1', 'CN2', 'CN3', 'D1.15', 'D1.17', 'P1']

## Proposition 3.36
**Statement:** If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the circle and the other touch it, the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference will be equal to the square on the tangent.

**Step 1.** Let D be a point taken outside the circle with centre F, let DCA be a straight line cutting the circle at C (on the convex circumference, nearer to D) and A (on the concave circumference, farther from D), and let DB be a straight line touching the circle at B. We must show that the rectangle DA times DC equals the square on DB.

**Step 2.** *Case 1: The line DCA passes through the centre F.* Since DB touches the circle at B and FB is joined from the centre to the point of contact, angle FBD is a right angle [3.18]. Now FA and FC are both radii, so FA = FB = FC [D1.15]. Thus DA = DF + FA = DF + FB, and DC = DF - FC = DF - FB.

**Step 3.** Therefore the rectangle DA times DC equals (DF + FB)(DF - FB), which equals the difference of the squares DF squared minus FB squared [2.5].

**Step 4.** Since angle FBD is right, by the Pythagorean theorem applied to triangle FBD, DF squared equals FB squared plus DB squared [1.47]. Therefore DF squared minus FB squared equals DB squared, and so DA times DC equals the square on DB.

**Step 5.** *Case 2: The line DCA does not pass through the centre.* Find the centre F of the circle [3.1]. Draw FG perpendicular to AC [1.12], meeting it at G. Join FD, FA, and FB [P1].

**Step 6.** Since FG is a straight line through the centre that cuts the chord AC at right angles, it bisects AC [3.3], so AG = GC.

**Step 7.** Since AG = GC, and DA = DG + GA while DC = DG - GC = DG - GA, the rectangle DA times DC equals (DG + GA)(DG - GA), which equals DG squared minus GA squared [2.5].

**Step 8.** In the right triangle FGD (right angle at G), by the Pythagorean theorem, FD squared equals FG squared plus GD squared [1.47], so GD squared equals FD squared minus FG squared.

**Step 9.** In the right triangle FGA (right angle at G), by the Pythagorean theorem, FA squared equals FG squared plus GA squared [1.47], so GA squared equals FA squared minus FG squared.

**Step 10.** Therefore DG squared minus GA squared equals (FD squared minus FG squared) minus (FA squared minus FG squared), which simplifies to FD squared minus FA squared.

**Step 11.** Since FA and FB are both radii of the circle, FA = FB [D1.15]. Therefore DA times DC equals FD squared minus FB squared.

**Step 12.** Since DB touches the circle at B and FB is joined from the centre to the point of contact, angle FBD is a right angle [3.18]. By the Pythagorean theorem applied to triangle FBD, FD squared equals FB squared plus BD squared [1.47], so FD squared minus FB squared equals BD squared.

**Step 13.** Therefore, in both cases, the rectangle DA times DC equals the square on DB. This is what was to be proved.

**USED:** 1.12, 1.47, 2.5, 3.1, 3.18, 3.3, D1.15, D3.2, P1
**Human refs (from References field):** 1.47, 2.6, 3.18, 3.3
**Jaccard:** 0.300 — AI adds ['1.12', '2.5', '3.1', 'D1.15', 'D3.2', 'P1']; Human adds ['2.6']

## Proposition 3.37
**Statement:** If a point be taken outside a circle and from the point there fall on the circle two straight lines, if one of them cut the circle, and the other fall on it, and if further the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference be equal to the square on the straight line which falls on the circle, the straight line which falls on it will touch the circle.

**Step 1.** Let D be a point outside the given circle, let DCA be a straight line cutting the circle at C and A (with C on the convex circumference nearer to D), and let DB be a straight line from D falling on the circle at B, such that the rectangle contained by DA and DC equals the square on DB. We must show that DB touches the circle.

**Step 2.** Suppose, for the sake of contradiction, that DB does not touch the circle. By Proposition 3.17, from the point D we can draw a straight line DE touching the circle, where E is the point of contact.

**Step 3.** Find the centre F of the circle by Proposition 3.1. Join FE, FB, and FD by Postulate 1.

**Step 4.** Since DE touches the circle at E and FE is joined from the centre F to the point of contact E, angle FED is a right angle by Proposition 3.18.

**Step 5.** Since DE touches the circle at E and from the external point D the straight line DCA cuts the circle, the rectangle contained by DA and DC equals the square on DE, by Proposition 3.36.

**Step 6.** But the rectangle contained by DA and DC also equals the square on DB, by hypothesis. Therefore the square on DE equals the square on DB, by Common Notion 1. Hence DE equals DB.

**Step 7.** Now in triangles DFE and DFB: FE equals FB, since both are radii of the circle (Definition 1.15); FD is common to both triangles; and DE equals DB, as proved in Step 6.

**Step 8.** Therefore triangle DFE is congruent to triangle DFB, by Proposition 1.8 (SSS). In particular, angle FBD equals angle FED.

**Step 9.** But angle FED is a right angle (Step 4). Therefore angle FBD is also a right angle. That is, FB is perpendicular to BD at the point B on the circle.

**Step 10.** Since FB is a radius and BD meets it at right angles at the point B on the circumference, the straight line BD, being drawn at right angles to the diameter at its extremity, touches the circle and does not cut it, by Proposition 3.16.

**Step 11.** Therefore the straight line which falls on the circle, namely DB, touches the circle. Q.E.D.

**USED:** 1.8, 3.1, 3.16, 3.17, 3.18, 3.36, CN1, D1.15, P1
**Human refs (from References field):** 1.8, 3.16, 3.18, 3.36
**Jaccard:** 0.444 — AI adds ['3.1', '3.17', 'CN1', 'D1.15', 'P1']
