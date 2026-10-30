# Book 2 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 2.1
**Statement:** If there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments.

**Step 1.** Let A and BC be two straight lines, and let BC be cut at any number of points; for concreteness, let it be cut at D and E, so that the segments are BD, DE, and EC. We are to show that the rectangle contained by A and BC equals the sum of the rectangles contained by A and each of the segments BD, DE, EC.

**Step 2.** From point B, draw BF at right angles to BC [1.11].

**Step 3.** On BF, cut off BG equal to A [1.3].

**Step 4.** Through G, draw GH parallel to BC [1.31].

**Step 5.** Through D, E, and C, draw DK, EL, and CH each parallel to BG, meeting GH at K, L, and H respectively [1.31].

**Step 6.** Now BH is the rectangle contained by A and BC. For BH is the parallelogram with sides BG and BC containing a right angle at B, and BG equals A; thus by the definition of a rectangular parallelogram, BH is the rectangle contained by A and BC [D2.1].

**Step 7.** Consider the parallelogram BK (that is, BGKD). Since BG is parallel to DK (by construction in Step 5) and BD is a segment of BC which is parallel to GK (a segment of GH, constructed parallel to BC in Step 4), BGKD is a parallelogram. Its opposite sides are equal, so DK equals BG [1.34]. Since BG equals A, we have DK equals A. The parallelogram BK has a right angle at B (from Step 2), and its sides containing this angle are BG (equal to A) and BD. Therefore BK is the rectangle contained by A and BD [D2.1].

**Step 8.** Consider the parallelogram DL (that is, DKLE). Since DK is parallel to EL (both constructed parallel to BG in Step 5) and DE is a segment of BC which is parallel to KL (a segment of GH), DKLE is a parallelogram. By the equality of opposite sides, EL equals DK [1.34], and since DK equals BG equals A, we have EL equals A. The angle GKD is right since it is the angle of the rectangle BGKD at K, and angle DKL is supplementary to angle GKD along the straight line GH; but actually, since BG is perpendicular to BC and DK is parallel to BG, the angle KDE is also a right angle [1.29]. Therefore DL is the rectangle contained by A and DE [D2.1].

**Step 9.** By the same reasoning applied to the parallelogram EH (that is, ELHC): EL is parallel to CH, and EC is a segment of BC parallel to LH (a segment of GH). So ELHC is a parallelogram, and CH equals EL equals A [1.34]. The angle at E in this parallelogram is right by the same argument using 1.29 applied to the parallel lines EL and BG with transversal BC. Therefore EH is the rectangle contained by A and EC [D2.1].

**Step 10.** The rectangle BH is composed of the rectangles BK, DL, and EH, since the segments BD, DE, EC together make up BC and the parallels DK, EL partition the figure BH into exactly these three sub-rectangles. That is, the rectangle contained by A and BC equals the rectangle contained by A and BD, together with the rectangle contained by A and DE, together with the rectangle contained by A and EC [CN2].

**Step 11.** The argument holds for any number of segments, since we may draw through each point of division a line parallel to BG and apply the same reasoning. Therefore, if there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments. Q.E.D.

**USED:** 1.11, 1.29, 1.3, 1.31, 1.34, CN2, D2.1
**Human refs (from References field):** 1.11, 1.3, 1.31, 1.34
**Jaccard:** 0.571 — AI adds ['1.29', 'CN2', 'D2.1']

## Proposition 2.2
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and both of the segments is equal to the square on the whole.

**Step 1.** Let AB be a straight line cut at random at the point C, so that the segments are AC and CB. We are to show that the rectangle contained by AB and AC together with the rectangle contained by AB and CB is equal to the square on AB.

**Step 2.** Construct the square on AB [1.46]. By D1.22, this square is equilateral and right-angled, and by D2.1 it is the rectangle contained by AB and AB — that is, rect(AB, AB) = sq(AB).

**Step 3.** Now consider AB itself as two straight lines (taking both to be AB), where one of them (AB) has been cut into the segments AC and CB. By Proposition 2.1, the rectangle contained by the two straight lines — that is, rect(AB, AB) — is equal to the rectangles contained by the uncut straight line and each of the segments. Therefore rect(AB, AB) = rect(AB, AC) + rect(AB, CB).

**Step 4.** But rect(AB, AB) = sq(AB) [Step 2]. Therefore rect(AB, AC) + rect(AB, CB) = sq(AB).

**Step 5.** That is, the rectangle contained by the whole AB and both of the segments AC and CB is equal to the square on AB, which is what was to be proved. Q.E.D.

**USED:** 1.46, 2.1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.200 — AI adds ['2.1', 'D1.22', 'D2.1']; Human adds ['1.31']

## Proposition 2.3
**Statement:** If a straight line be cut at random, the rectangle contained by the whole and one of the segments is equal to the rectangle contained by the segments and the square on the aforesaid segment.

**Step 1.** Let AB be a straight line cut at random at the point C. We must show that the rectangle contained by AB and BC equals the rectangle contained by AC and BC together with the square on BC.

**Step 2.** Consider the two straight lines BC and AB, where BC is uncut and AB is cut into the segments AC and CB at the point C.

**Step 3.** By Proposition 2.1, if there be two straight lines and one of them be cut into any number of segments, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments. Applying this with BC as the uncut line and AB as the line cut into segments AC and CB, we obtain: the rectangle contained by AB and BC is equal to the rectangle contained by BC and AC together with the rectangle contained by BC and CB.

**Step 4.** Now the rectangle contained by BC and CB is the rectangle contained by two equal straight lines, namely BC with itself. By the definition of a square (D1.22), this is the square on BC.

**Step 5.** Therefore, substituting in the result of Step 3, the rectangle contained by AB and BC is equal to the rectangle contained by AC and BC together with the square on BC.

**Step 6.** This is precisely what was to be proved: the rectangle contained by the whole AB and the segment BC equals the rectangle contained by the segments AC and BC together with the square on BC. Q.E.D.

**USED:** 2.1, D1.22, D2.1
**Human refs (from References field):** 1.31, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', 'D1.22', 'D2.1']; Human adds ['1.31', '1.46']

## Proposition 2.4
**Statement:** If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.

**Step 1.** Let AB be a straight line cut at random at the point C. We are to show that the square on AB equals the squares on AC and CB together with twice the rectangle contained by AC and CB.

**Step 2.** Since the straight line AB has been cut at random at C, by Proposition 2.2, the rectangle contained by AB and AC together with the rectangle contained by AB and CB equals the square on AB. That is, rect(AB, AC) + rect(AB, CB) = sq(AB).

**Step 3.** Since the straight line AB has been cut at random at C, by Proposition 2.3 applied to segment AC, the rectangle contained by AB and AC equals the rectangle contained by AC and CB together with the square on AC. That is, rect(AB, AC) = rect(AC, CB) + sq(AC).

**Step 4.** Similarly, by Proposition 2.3 applied to segment CB, the rectangle contained by AB and CB equals the rectangle contained by CB and AC together with the square on CB. That is, rect(AB, CB) = rect(CB, AC) + sq(CB).

**Step 5.** Substituting the results of Steps 3 and 4 into the equation from Step 2, we obtain: sq(AB) = rect(AC, CB) + sq(AC) + rect(CB, AC) + sq(CB).

**Step 6.** Now, the rectangle contained by AC and CB is the same as the rectangle contained by CB and AC, since by Definition 2.1 a rectangular parallelogram is said to be contained by the two straight lines containing the right angle, and the two lines are the same regardless of the order in which they are named. Therefore rect(AC, CB) = rect(CB, AC).

**Step 7.** Hence, by Common Notion 2 (adding equals to equals), rect(AC, CB) + rect(CB, AC) = 2 * rect(AC, CB). Combining with the squares, we conclude: sq(AB) = sq(AC) + sq(CB) + twice rect(AC, CB).

**Step 8.** Therefore, if a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments. Q.E.D.

**USED:** 2.2, 2.3, CN2, D2.1
**Human refs (from References field):** 1.29, 1.31, 1.34, 1.46, 1.5, 1.6
**Jaccard:** 0.000 — AI adds ['2.2', '2.3', 'CN2', 'D2.1']; Human adds ['1.29', '1.31', '1.34', '1.46', '1.5', '1.6']

## Proposition 2.5
**Statement:** If a straight line be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the straight line between the points of section is equal to the square on the half.

**Step 1.** Let AB be a straight line cut into equal segments at C, so that AC = CB, and into unequal segments at D. We are to prove that rect(AD, DB) + sq(CD) = sq(CB). Without loss of generality, assume D lies between C and B, so that the order of points along the line is A, C, D, B.

**Step 2.** Since AC = CB and D lies between C and B, we have AD = AC + CD = CB + CD. That is, the line AD is composed of the two segments CB and CD. [CN2, since AC = CB and we add CD to each]

**Step 3.** Apply Proposition 2.1 to the two straight lines AD and DB, where AD has been cut into the segments CB and CD. Then rect(AD, DB) = rect(CB, DB) + rect(CD, DB). [2.1]

**Step 4.** Apply Proposition 2.3 to the line CB cut at D. Since CB = CD + DB, the rectangle contained by the whole CB and the segment DB equals the rectangle contained by the two segments CD, DB together with the square on DB. That is, rect(CB, DB) = rect(CD, DB) + sq(DB). [2.3]

**Step 5.** Substitute the result of Step 4 into Step 3: rect(AD, DB) = rect(CD, DB) + sq(DB) + rect(CD, DB) = 2 * rect(CD, DB) + sq(DB). [CN1]

**Step 6.** Add sq(CD) to both sides: rect(AD, DB) + sq(CD) = 2 * rect(CD, DB) + sq(DB) + sq(CD). [CN2]

**Step 7.** Apply Proposition 2.4 to the line CB cut at D. The square on the whole CB equals the squares on the segments CD and DB together with twice the rectangle contained by CD and DB. That is, sq(CB) = sq(CD) + sq(DB) + 2 * rect(CD, DB). [2.4]

**Step 8.** The right-hand side of Step 6, namely sq(CD) + sq(DB) + 2 * rect(CD, DB), is equal to sq(CB) by Step 7. Therefore rect(AD, DB) + sq(CD) = sq(CB). [CN1]

**Step 9.** This is the desired result: the rectangle contained by the unequal segments AD, DB of the whole line AB, together with the square on CD (the line between the points of section), equals the square on CB (the half). Q.E.D.

**USED:** 2.1, 2.3, 2.4, CN1, CN2
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', '2.3', '2.4', 'CN1', 'CN2']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.6
**Statement:** If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

**Step 1.** Let AB be a straight line bisected at C, and let BD be added to it in a straight line. We must show that rect(AD, DB) + sq(CB) = sq(CD), where AD is the whole with the added straight line, DB is the added straight line, CB is the half, and CD is the straight line made up of the half and the added straight line.

**Step 2.** Since AB is bisected at C, we have AC = CB. The line AD is composed of segments AC and CD, and since AC = CB, we have AD = CB + CD. The line CD is composed of CB and BD, so CD = CB + BD.

**Step 3.** Consider the two straight lines DB and AD, where AD has been cut into segments AC and CD. By 2.1, the rectangle contained by AD and DB equals the sum of the rectangles contained by AC and DB, and by CD and DB. Since AC = CB, this gives rect(AD, DB) = rect(CB, DB) + rect(CD, DB).

**Step 4.** Now consider the straight line CD, which is cut at B (into segments CB and BD). By 2.3, the rectangle contained by CD and DB equals the rectangle contained by CB and BD together with the square on BD. That is, rect(CD, DB) = rect(CB, BD) + sq(BD).

**Step 5.** Substituting the result of Step 4 into Step 3, we obtain rect(AD, DB) = rect(CB, DB) + rect(CB, BD) + sq(BD) = 2 * rect(CB, BD) + sq(BD).

**Step 6.** Now consider the straight line CD = CB + BD, which is cut at B. By 2.4, the square on CD equals the squares on CB and BD together with twice the rectangle contained by CB and BD. That is, sq(CD) = sq(CB) + sq(BD) + 2 * rect(CB, BD).

**Step 7.** From Step 5, we have rect(AD, DB) = 2 * rect(CB, BD) + sq(BD). Therefore sq(BD) + 2 * rect(CB, BD) = rect(AD, DB). Substituting into the result of Step 6, we get sq(CD) = sq(CB) + rect(AD, DB).

**Step 8.** By CN2, adding equal things to equals preserves equality, and rearranging, we conclude rect(AD, DB) + sq(CB) = sq(CD). That is, the rectangle contained by the whole with the added straight line and the added straight line, together with the square on the half, is equal to the square on the straight line made up of the half and the added straight line. Q.E.D.

**USED:** 2.1, 2.3, 2.4, CN2
**Human refs (from References field):** 1.31, 1.36, 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.1', '2.3', '2.4', 'CN2']; Human adds ['1.31', '1.36', '1.43', '1.46']

## Proposition 2.7
**Statement:** If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

**Step 1.** Let AB be a straight line cut at random at the point C. We are to show that the squares on AB and BC together are equal to twice the rectangle contained by AB and BC together with the square on AC.

**Step 2.** Since the straight line AB has been cut at random at C, by Proposition 2.4, the square on AB is equal to the squares on AC and CB together with twice the rectangle contained by AC and CB. That is, sq(AB) = sq(AC) + sq(CB) + 2*rect(AC, CB).

**Step 3.** Adding the square on CB to both sides (by CN2), we obtain: sq(AB) + sq(CB) = sq(AC) + 2*sq(CB) + 2*rect(AC, CB).

**Step 4.** Since the straight line AB has been cut at random at C, by Proposition 2.3, the rectangle contained by AB and BC is equal to the rectangle contained by AC and CB together with the square on BC. That is, rect(AB, BC) = rect(AC, CB) + sq(BC).

**Step 5.** Therefore twice the rectangle contained by AB and BC equals twice the rectangle contained by AC and CB together with twice the square on BC (by CN2 applied to equal magnitudes doubled). That is, 2*rect(AB, BC) = 2*rect(AC, CB) + 2*sq(BC).

**Step 6.** Adding the square on AC to both sides (by CN2), we obtain: 2*rect(AB, BC) + sq(AC) = 2*rect(AC, CB) + 2*sq(BC) + sq(AC).

**Step 7.** The right-hand side of Step 3, namely sq(AC) + 2*sq(CB) + 2*rect(AC, CB), is the same sum as the right-hand side of Step 6, namely 2*rect(AC, CB) + 2*sq(BC) + sq(AC), since CB and BC denote the same segment.

**Step 8.** Therefore, by CN1, the left-hand sides are equal: sq(AB) + sq(CB) = 2*rect(AB, BC) + sq(AC).

**Step 9.** Therefore, if a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment together with the square on the remaining segment. Q.E.D.

**USED:** 2.3, 2.4, CN1, CN2
**Human refs (from References field):** 1.43, 1.46
**Jaccard:** 0.000 — AI adds ['2.3', '2.4', 'CN1', 'CN2']; Human adds ['1.43', '1.46']

## Proposition 2.8
**Statement:** If a straight line be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one straight line.

**Step 1.** Let AB be a straight line cut at random at the point C. We are to show that four times the rectangle contained by AB and BC together with the square on AC is equal to the square on the straight line AD, where AD is composed of AB and BC taken as one straight line.

**Step 2.** Produce AB to D so that BD equals BC. This is done by extending AB beyond B [P2] and cutting off BD equal to BC [1.3]. Then AD equals the sum of AB and BD, that is, the sum of AB and BC.

**Step 3.** Since the straight line AD has been cut at B, by Proposition 2.4 the square on AD is equal to the sum of the square on AB, the square on BD, and twice the rectangle contained by AB and BD. That is, sq(AD) = sq(AB) + sq(BD) + 2*rect(AB, BD).

**Step 4.** Since BD equals BC, the square on BD equals the square on BC, and the rectangle contained by AB and BD equals the rectangle contained by AB and BC. Substituting, we obtain sq(AD) = sq(AB) + sq(BC) + 2*rect(AB, BC).

**Step 5.** Now consider the straight line AB cut at C. By Proposition 2.7, the square on AB together with the square on BC is equal to twice the rectangle contained by AB and BC together with the square on AC. That is, sq(AB) + sq(BC) = 2*rect(AB, BC) + sq(AC).

**Step 6.** Substituting the result of Step 5 into the equation from Step 4: sq(AD) = 2*rect(AB, BC) + sq(AC) + 2*rect(AB, BC) [CN1].

**Step 7.** Combining the two occurrences of 2*rect(AB, BC), we obtain sq(AD) = 4*rect(AB, BC) + sq(AC) [CN2].

**Step 8.** But AD is composed of AB and BC as one straight line (since BD = BC). Therefore the square on AD is the square described on AB and BC as on one straight line. Hence four times the rectangle contained by AB and BC together with the square on AC equals the square described on AB and BC as on one straight line.

**Step 9.** Therefore, if a straight line be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one straight line. Q.E.F.

**USED:** 1.3, 2.4, 2.7, CN1, CN2, P2
**Human refs (from References field):** 1.36, 1.43
**Jaccard:** 0.000 — AI adds ['1.3', '2.4', '2.7', 'CN1', 'CN2', 'P2']; Human adds ['1.36', '1.43']

## Proposition 2.9
**Statement:** If a straight line be cut into equal and unequal segments, the squares on the unequal segments of the whole are double of the square on the half and of the square on the straight line between the points of section.

**Step 1.** Let AB be the given straight line, bisected at C and cut unequally at D. We must show that sq(AD) + sq(DB) = 2*sq(AC) + 2*sq(CD).

**Step 2.** Since AB is bisected at C, we have AC = CB.

**Step 3.** Since D lies on segment CB, the line AD is composed of AC and CD, so AD = AC + CD.

**Step 4.** Apply Proposition 2.4 to line AD, which is cut at C into segments AC and CD. The square on the whole AD equals the squares on the segments AC and CD together with twice the rectangle contained by AC and CD. That is, sq(AD) = sq(AC) + sq(CD) + 2*rect(AC, CD). ... (i)

**Step 5.** Now consider the line CB, which is cut at D into segments CD and DB. Apply Proposition 2.7 to the line CB cut at D: the square on the whole CB together with the square on segment CD equals twice the rectangle contained by CB and CD together with the square on the remaining segment DB. That is, sq(CB) + sq(CD) = 2*rect(CB, CD) + sq(DB).

**Step 6.** Rearranging Step 5, we obtain sq(DB) = sq(CB) + sq(CD) - 2*rect(CB, CD). ... (ii)

**Step 7.** Add equations (i) and (ii): sq(AD) + sq(DB) = sq(AC) + sq(CD) + 2*rect(AC, CD) + sq(CB) + sq(CD) - 2*rect(CB, CD).

**Step 8.** Since AC = CB (Step 2), the rectangle contained by AC and CD equals the rectangle contained by CB and CD, that is, rect(AC, CD) = rect(CB, CD). [CN1]

**Step 9.** Therefore the terms 2*rect(AC, CD) and -2*rect(CB, CD) cancel each other. [CN3]

**Step 10.** Also since AC = CB, we have sq(AC) = sq(CB). Substituting into the sum from Step 7: sq(AD) + sq(DB) = sq(AC) + sq(AC) + sq(CD) + sq(CD) = 2*sq(AC) + 2*sq(CD). [CN1, CN2]

**Step 11.** Therefore the squares on the unequal segments AD and DB of the whole line AB are together double of the square on the half AC and of the square on CD, the straight line between the points of section. Q.E.D.

**USED:** 2.4, 2.7, CN1, CN2, CN3
**Human refs (from References field):** 1.29, 1.32, 1.34, 1.47, 1.6
**Jaccard:** 0.000 — AI adds ['2.4', '2.7', 'CN1', 'CN2', 'CN3']; Human adds ['1.29', '1.32', '1.34', '1.47', '1.6']

## Proposition 2.10
**Statement:** If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

**Step 1.** Let AB be a straight line bisected at C, and let BD be added to it in a straight line. We must show that sq(AD) + sq(DB) = 2*sq(AC) + 2*sq(CD).

**Step 2.** The line AD is composed of segments AB and BD, so AD is cut at B. By 2.7 applied to line AD cut at B (taking DB as the chosen segment), we have sq(AD) + sq(DB) = 2*rect(AD, DB) + sq(AB).

**Step 3.** Since AB is bisected at C, we have AC = CB. By 2.4 applied to line AB = AC + CB, sq(AB) = sq(AC) + sq(CB) + 2*rect(AC, CB). Since CB = AC, we have sq(CB) = sq(AC) and rect(AC, CB) = sq(AC). Therefore sq(AB) = sq(AC) + sq(AC) + 2*sq(AC) = 4*sq(AC) [CN2].

**Step 4.** Substituting the result of Step 3 into Step 2: sq(AD) + sq(DB) = 2*rect(AD, DB) + 4*sq(AC).

**Step 5.** By 2.6, since AB is bisected at C and BD is added to it in a straight line, rect(AD, DB) + sq(CB) = sq(CD). Since CB = AC, this gives rect(AD, DB) + sq(AC) = sq(CD). Subtracting sq(AC) from both sides [CN3], rect(AD, DB) = sq(CD) - sq(AC). Hence 2*rect(AD, DB) = 2*sq(CD) - 2*sq(AC).

**Step 6.** Substituting into Step 4: sq(AD) + sq(DB) = (2*sq(CD) - 2*sq(AC)) + 4*sq(AC) = 2*sq(CD) + 2*sq(AC) [CN2, CN3].

**Step 7.** Therefore the squares on AD and DB together are double of the square on AC and the square on CD, which is what was to be proved.

**USED:** 2.4, 2.6, 2.7, CN2, CN3
**Human refs (from References field):** 1.11, 1.15, 1.29, 1.3, 1.31, 1.32, 1.34, 1.47, 1.5, 1.6, CN1, P5
**Jaccard:** 0.000 — AI adds ['2.4', '2.6', '2.7', 'CN2', 'CN3']; Human adds ['1.11', '1.15', '1.29', '1.3', '1.31', '1.32', '1.34', '1.47', '1.5', '1.6', 'CN1', 'P5']

## Proposition 2.11
**Statement:** To cut a given straight line so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.

**Step 1.** Let AB be the given straight line. Construct the square ABDC on AB, with vertices A (top-left), B (top-right), D (bottom-right), C (bottom-left). [1.46]

**Step 2.** Bisect AC at E, so that AE = EC. [1.10]

**Step 3.** Join B to E. [P1]

**Step 4.** Produce CA beyond A to a point F such that EF = EB. This is done by drawing a circle with centre E and radius EB, and letting F be the intersection of this circle with the line CA produced beyond A. [P2, P3]

**Step 5.** Construct the square FGHA on AF, where F is at top-left, G at top-right, H at bottom-right, and A at bottom-left. Then H lies on AB between A and B, and AH = AF. [1.46]

**Step 6.** Produce GH to meet line CD at K. [P2]

**Step 7.** Since AC is bisected at E and FA is added to it in a straight line, by Proposition 2.6 the rectangle contained by CF and FA together with the square on AE equals the square on EF. That is, rect(CF, FA) + sq(AE) = sq(EF). [2.6]

**Step 8.** But EF = EB by construction, so sq(EF) = sq(EB).

**Step 9.** In triangle EAB, the angle at A is a right angle (since ABDC is a square and angle BAC is a right angle). Therefore by the Pythagorean theorem, sq(EB) = sq(EA) + sq(AB). [1.47]

**Step 10.** Combining Steps 7, 8, and 9: rect(CF, FA) + sq(AE) = sq(EA) + sq(AB). Since sq(AE) = sq(EA), subtracting sq(AE) from both sides gives rect(CF, FA) = sq(AB). [CN3]

**Step 11.** Now FA = AH (both are sides of the square FGHA), so rect(CF, AH) = sq(AB).

**Step 12.** Since ABDC is a square, AC = AB. And CF = FA + AC = AH + AB. Thus the line CF, with AH as the uncut line, is cut into the segments FA (= AH) and AC (= AB). By Proposition 2.1, rect(AH, CF) = rect(AH, FA) + rect(AH, AC) = rect(AH, AH) + rect(AH, AB) = sq(AH) + rect(AH, AB). [2.1]

**Step 13.** From Steps 10-12: sq(AH) + rect(AH, AB) = sq(AB).

**Step 14.** Since H lies on AB, the line AB is cut at H into segments AH and HB. By Proposition 2.2, the rectangle contained by the whole AB and both segments equals the square on AB: rect(AB, AH) + rect(AB, HB) = sq(AB). [2.2]

**Step 15.** From Steps 13 and 14: sq(AH) + rect(AB, AH) = rect(AB, AH) + rect(AB, HB), since both equal sq(AB). Subtracting rect(AB, AH) from both sides, we obtain sq(AH) = rect(AB, HB). [CN3]

**Step 16.** Therefore the straight line AB has been cut at H so that the rectangle contained by the whole AB and the segment HB is equal to the square on the remaining segment AH. Q.E.F.

**USED:** 1.10, 1.46, 1.47, 2.1, 2.2, 2.6, CN3, P1, P2, P3
**Human refs (from References field):** 1.46, 1.47, 2.6
**Jaccard:** 0.300 — AI adds ['1.10', '2.1', '2.2', 'CN3', 'P1', 'P2', 'P3']

## Proposition 2.12
**Statement:** In obtuse-angled triangles the square on the side subtending the obtuse angle is greater than the squares on the sides containing the obtuse angle by twice the rectangle contained by one of the sides about the obtuse angle, namely that on which the   perpendicular falls, and the straight line cut off outside by the perpendicular towards the obtuse angle.

**Step 1.** Let ABC be a triangle having the angle ABC obtuse [D1.11]. We must show that the square on AC is greater than the squares on AB and BC together by twice the rectangle contained by CB and BD, where D is the foot of the perpendicular from A.

**Step 2.** From point A, draw AD perpendicular to the line BC produced [1.12]. Since the angle at B is obtuse, the foot D of the perpendicular falls on BC produced beyond B, so that D lies outside the segment BC.

**Step 3.** Consider the straight line DC, which is composed of DB and BC. Since DC is cut at B, by Proposition 2.4 the square on DC equals the square on DB plus the square on BC plus twice the rectangle contained by CB and BD. That is, sq(DC) = sq(DB) + sq(BC) + 2*rect(CB, BD) [2.4].

**Step 4.** In triangle ACD, the angle at D is a right angle (since AD is perpendicular to DC). By the Pythagorean theorem, the square on AC equals the square on AD plus the square on DC. That is, sq(AC) = sq(AD) + sq(DC) [1.47].

**Step 5.** Substituting the expression for sq(DC) from Step 3 into Step 4, we obtain: sq(AC) = sq(AD) + sq(DB) + sq(BC) + 2*rect(CB, BD).

**Step 6.** In triangle ABD, the angle at D is a right angle. By the Pythagorean theorem, the square on AB equals the square on AD plus the square on DB. That is, sq(AB) = sq(AD) + sq(DB) [1.47].

**Step 7.** Therefore sq(AD) + sq(DB) = sq(AB). Substituting this into the equation from Step 5, we get: sq(AC) = sq(AB) + sq(BC) + 2*rect(CB, BD) [CN2].

**Step 8.** Hence the square on AC exceeds the sum of the squares on AB and BC by twice the rectangle contained by CB and BD. This is precisely what was to be proved: in obtuse-angled triangles, the square on the side subtending the obtuse angle is greater than the squares on the sides containing the obtuse angle by twice the rectangle contained by one of the sides about the obtuse angle (namely that on which the perpendicular falls) and the straight line cut off outside by the perpendicular towards the obtuse angle. Q.E.D.

**USED:** 1.12, 1.47, 2.4, CN2, D1.11
**Human refs (from References field):** 1.47, 2.4
**Jaccard:** 0.400 — AI adds ['1.12', 'CN2', 'D1.11']

## Proposition 2.13
**Statement:** In acute-angled triangles the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle by twice the rectangle contained by one of the sides about the acute angle, namely that on which the perpendicular falls, and the straight line cut off within by the perpendicular towards the acute angle.

**Step 1.** Let ABC be an acute-angled triangle, with all three angles acute [D1.21]. Let the angle at B be the acute angle under consideration. From A, draw AD perpendicular to BC [1.12], so that angle ADB is a right angle [D1.10]. Since angle ABD is acute [D1.12], the foot D of the perpendicular falls between B and C, so that BD is the straight line cut off within by the perpendicular towards the acute angle at B. We are to show that the square on AC is less than the squares on AB and BC together by twice the rectangle contained by CB and BD.

**Step 2.** Since the straight line BC has been cut at random at the point D, by Proposition 2.7 the square on BC together with the square on BD is equal to twice the rectangle contained by BC and BD together with the square on CD. That is: sq(BC) + sq(BD) = 2*rect(BC, BD) + sq(CD) [2.7].

**Step 3.** Add the square on DA to both sides. Then the square on BC together with the squares on BD and DA is equal to twice the rectangle contained by BC and BD together with the squares on CD and DA [CN2]. That is: sq(BC) + sq(BD) + sq(DA) = 2*rect(BC, BD) + sq(CD) + sq(DA).

**Step 4.** Since the angle ADB is a right angle, the triangle ABD is right-angled at D. Therefore by the Pythagorean theorem, the square on AB is equal to the squares on BD and DA [1.47]. That is: sq(AB) = sq(BD) + sq(DA).

**Step 5.** Since the angle ADC is also a right angle (for AD is perpendicular to BC), the triangle ACD is right-angled at D. Therefore by the Pythagorean theorem, the square on AC is equal to the squares on CD and DA [1.47]. That is: sq(AC) = sq(CD) + sq(DA).

**Step 6.** Substituting into the equation from Step 3: on the left side, sq(BD) + sq(DA) equals sq(AB) by Step 4, so the left side becomes sq(BC) + sq(AB). On the right side, sq(CD) + sq(DA) equals sq(AC) by Step 5, so the right side becomes 2*rect(BC, BD) + sq(AC) [CN1].

**Step 7.** Therefore sq(BC) + sq(AB) = 2*rect(BC, BD) + sq(AC). Equivalently, the square on AC is less than the squares on AB and BC by twice the rectangle contained by BC and BD, which is what was to be proved.

**USED:** 1.12, 1.47, 2.7, CN1, CN2, D1.10, D1.12, D1.21
**Human refs (from References field):** 1.47, 2.7
**Jaccard:** 0.250 — AI adds ['1.12', 'CN1', 'CN2', 'D1.10', 'D1.12', 'D1.21']

## Proposition 2.14
**Statement:** To construct a square equal to a given rectilineal figure.

**Step 1.** Let A be the given rectilineal figure. By 1.45, construct the rectangular parallelogram BCDE equal to the rectilineal figure A, with angle CBE being a right angle. Thus BCDE is a rectangle with area equal to A.

**Step 2.** If BE = ED, then BCDE is both equilateral and right-angled, hence a square by D1.22, and the construction is complete. Suppose then that BE is not equal to ED.

**Step 3.** Produce BE to F such that EF = ED, by P2 and 1.3. Then the rectangle contained by BE and EF equals the rectangle contained by BE and ED, which equals the area of the rectangle BCDE.

**Step 4.** Bisect BF at G, by 1.10.

**Step 5.** With center G and radius GB (equivalently GF, since G is the midpoint of BF), describe a semicircle BHF, by P3 and D1.17.

**Step 6.** Produce DE to H, where H is the point at which the produced line meets the semicircle, by P2.

**Step 7.** Join GH, by P1. Since G is the center of the semicircle BHF and both H and F lie on the circumference, GH = GF, by D1.15.

**Step 8.** Now the straight line BF has been bisected at G and cut into unequal segments at E. By 2.5, the rectangle contained by BE and EF, together with the square on GE, equals the square on GF.

**Step 9.** Since GF = GH (Step 7), the square on GF equals the square on GH.

**Step 10.** The angle GEH is a right angle, because DE was originally perpendicular to BE (since BCDE is a rectangle) and H lies on DE produced. By 1.47, the square on GH equals the square on GE together with the square on EH.

**Step 11.** From Steps 8, 9, and 10: the rectangle BE * EF + the square on GE = the square on GE + the square on EH.

**Step 12.** Subtracting the square on GE from both sides, by CN3, the rectangle contained by BE and EF equals the square on EH.

**Step 13.** But the rectangle contained by BE and EF equals the rectangle contained by BE and ED (since EF = ED, from Step 3), which equals the area of the rectangle BCDE, which equals the rectilineal figure A (Step 1).

**Step 14.** Therefore the square on EH is equal to the given rectilineal figure A.

**Step 15.** Construct the square EHKL on EH, by 1.46. This square is equal to the given rectilineal figure A.

Therefore a square has been constructed equal to the given rectilineal figure, which is what was required to do. Q.E.F.

**USED:** 1.10, 1.3, 1.45, 1.46, 1.47, 2.5, CN3, D1.15, D1.17, D1.22, P1, P2, P3
**Human refs (from References field):** 1.45, 1.47, 2.5
**Jaccard:** 0.231 — AI adds ['1.10', '1.3', '1.46', 'CN3', 'D1.15', 'D1.17', 'D1.22', 'P1', 'P2', 'P3']
